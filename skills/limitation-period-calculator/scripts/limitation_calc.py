#!/usr/bin/env python3
"""Limitation date calculator (Limitation Act, 1963 + the Supreme Court COVID-19 exclusion). Offline, stdlib only.

  python3 limitation_calc.py --start 2019-06-01 --period 3y --exclude-covid [--today 2026-11-06]
  python3 limitation_calc.py --start 2026-01-15 --period 3m+30d
  python3 limitation_calc.py --start 2022-04-01 --period 3y --ack 2024-03-10            # s.18/19 resets the start
  python3 limitation_calc.py --start 2021-01-10 --period 3y --exclude 2022-02-01:2022-09-30   # s.14 days
  add --json for structured output

Counting conventions (state them in any filing):
  * --start is the date the period runs FROM (accrual, decree, award receipt...). Under s.12(1) that day is
    excluded, so a period of N days ends ON start + N days, and the act may be done on or before that day.
  * Months and years are calendar months (s.3(35) General Clauses Act), clamped to the month end:
    31 Jan + 1 month = 28/29 Feb. Compound periods apply left to right: "3m+30d" = add 3 months, then 30 days.
  * Exclusions (s.14 ranges and the COVID window) are sets of calendar days that are skipped while counting:
    the period consumes only days outside them. s.14 ranges count both the institution day and the disposal
    day (Explanation (a) to s.14). The COVID window is 15 March 2020 to 28 February 2022, both inclusive
    (716 days), per the order of 10 January 2022 in In re Cognizance for Extension of Limitation.
  * COVID 90-day floor: if, ignoring the exclusion, the period would have ended inside the window, the last
    date is at least 30 May 2022 (90 days counted from 1 March 2022 with that day excluded).
  * --ack DATE (s.18 acknowledgment / s.19 part-payment) replaces --start with DATE if DATE is on or before the
    last date computed from the original start; otherwise the script refuses (an acknowledgment after expiry
    revives nothing).
  * Court holidays are NOT applied. If the last date is a day the court is closed, s.4 moves it to the next
    day the court is open — check the court's calendar.
Verify the Article and the special-law text on https://www.indiacode.nic.in/ before relying on any output.
"""
from __future__ import annotations

import argparse
import calendar
import json
import re
import sys
from datetime import date, datetime, timedelta

COVID_START = date(2020, 3, 15)
COVID_END = date(2022, 2, 28)
COVID_FLOOR = date(2022, 5, 30)  # 1 March 2022 + 90 days, 1 March excluded
PERIOD_RE = re.compile(r"^(\d+)([dmy])$")


def parse(d: str | None) -> date | None:
    if d is None:
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"bad date {d!r}: use YYYY-MM-DD")


def add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    year, month = d.year + y, m + 1
    return date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


def parse_period(spec: str) -> list[tuple[int, str]]:
    parts = []
    for piece in spec.lower().replace(" ", "").split("+"):
        m = PERIOD_RE.match(piece)
        if not m:
            sys.exit(f"bad period {spec!r}: use forms like 90d, 1m, 3y, 3m+30d")
        parts.append((int(m.group(1)), m.group(2)))
    return parts


def naive_end(start: date, period: list[tuple[int, str]]) -> date:
    d = start
    for n, unit in period:
        d = d + timedelta(days=n) if unit == "d" else add_months(d, n if unit == "m" else 12 * n)
    return d


def parse_ranges(specs: list[str]) -> list[tuple[date, date]]:
    out = []
    for s in specs:
        a, _, b = s.partition(":")
        lo, hi = parse(a), parse(b or a)
        if hi < lo:
            sys.exit(f"bad range {s!r}")
        out.append((lo, hi))
    return out


def excluded_days(ranges: list[tuple[date, date]]) -> set[date]:
    days: set[date] = set()
    for lo, hi in ranges:
        days.update(lo + timedelta(days=i) for i in range((hi - lo).days + 1))
    return days


def compute(start: date, period_spec: str, today: date, covid: bool = False,
            s14: list[tuple[date, date]] | None = None, ack: date | None = None) -> dict:
    period = parse_period(period_spec)
    steps: list[str] = []
    notes: list[str] = []
    s14 = s14 or []

    original_start = start
    if ack is not None:
        # the acknowledgment must fall within the period computed from the original start (with exclusions)
        trial = compute(start, period_spec, today, covid, s14, None)
        if ack > trial["last_date"]:
            sys.exit(f"acknowledgment {ack} is after the last date {trial['last_date']} computed from {start}: "
                     "s.18/19 does not revive an expired period")
        steps.append(f"s.18/19: fresh period runs from the acknowledgment/payment date {ack} (original start {start})")
        start = ack

    end0 = naive_end(start, period)
    length = (end0 - start).days
    steps.append(f"start {start} (day excluded, s.12(1)) + {period_spec} = {end0} without exclusions ({length} days)")

    ranges = list(s14)
    if covid:
        ranges.append((COVID_START, COVID_END))
    skip = excluded_days(ranges)

    # count `length` days forward from start, skipping excluded days
    end = start
    consumed = 0
    skipped = 0
    while consumed < length:
        end += timedelta(days=1)
        if end in skip:
            skipped += 1
            continue
        consumed += 1
    if skipped:
        parts = []
        if s14:
            s14_days = sum(1 for d in excluded_days(s14) if start < d <= end)
            parts.append(f"s.14 wrong-forum days {s14_days}")
        if covid:
            cov_days = sum(1 for i in range((COVID_END - COVID_START).days + 1)
                           if start < COVID_START + timedelta(days=i) <= end)
            parts.append(f"COVID window days {cov_days}")
        steps.append(f"excluded {skipped} day(s) ({'; '.join(parts)}) → last date {end}")

    floor_applied = False
    if covid and COVID_START <= end0 <= COVID_END and end < COVID_FLOOR:
        steps.append(f"period would have expired inside the COVID window on {end0}; 90-day floor from 1 March 2022 → {COVID_FLOOR}")
        end = COVID_FLOOR
        floor_applied = True

    if today > end:
        status = f"EXPIRED — {(today - end).days} day(s) ago"
    elif today == end:
        status = "LAST DAY is today"
    else:
        status = f"{(end - today).days} day(s) left"

    notes.append("last date is 'on or before'; if the court is closed that day, s.4 moves it to the next working day")
    if covid and not skipped and not floor_applied:
        notes.append("COVID exclusion requested but the period does not overlap 15.03.2020–28.02.2022; nothing added")
    return {
        "start": start, "original_start": original_start, "period": period_spec, "naive_end": end0,
        "excluded_days": skipped, "covid": covid, "covid_floor_applied": floor_applied,
        "last_date": end, "today": today, "status": status, "steps": steps, "notes": notes,
    }


def render(r: dict) -> str:
    out = [f"Limitation computation (as of {r['today']})", "",
           "| Item | Value |", "|---|---|",
           f"| Period runs from | {r['start']}" + (f" (s.18/19 reset; accrual {r['original_start']})" if r['start'] != r['original_start'] else "") + " |",
           f"| Period | {r['period']} |",
           f"| End without exclusions | {r['naive_end']} |",
           f"| Days excluded | {r['excluded_days']}" + (" + COVID 90-day floor" if r['covid_floor_applied'] else "") + " |",
           f"| **Last date to file (on or before)** | **{r['last_date']}** |",
           f"| Status today | {r['status']} |", "", "Steps:"]
    out += [f"- {s}" for s in r["steps"]]
    out += ["", "Notes:"] + [f"- {n}" for n in r["notes"]]
    out.append("")
    out.append("Court holidays not applied. Verify the Article / special-law period on India Code.")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", required=True, help="date the period runs from, YYYY-MM-DD")
    ap.add_argument("--period", required=True, help="e.g. 90d, 1m, 3y, 3m+30d")
    ap.add_argument("--exclude-covid", action="store_true", help="apply the 15.03.2020–28.02.2022 exclusion")
    ap.add_argument("--ack", help="s.18 acknowledgment / s.19 part-payment date (resets the start)")
    ap.add_argument("--exclude", action="append", default=[], metavar="FROM:TO",
                    help="s.14 range spent in a wrong forum, both days counted; repeatable")
    ap.add_argument("--today")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    today = parse(a.today) or date.today()
    r = compute(parse(a.start), a.period, today, a.exclude_covid, parse_ranges(a.exclude), parse(a.ack))
    if a.json:
        print(json.dumps(r, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
