#!/usr/bin/env python3
"""Date calculator for default bail (BNSS s.187(3)) and undertrial release (BNSS s.479). Offline, stdlib only.

  python3 bail_timelines.py default   --remand 2026-08-01 --punishment other   [--today 2026-11-06] [--json]
  python3 bail_timelines.py undertrial --custody-from 2024-02-10 --max-years 7 [--first-time] [--today ...] [--json]

default — permitted period of detention before the charge sheet:
  other : 60 days (offence punishable with less than ten years minimum)
  min10 : 90 days (imprisonment for a term of not less than ten years — Rakesh Kumar Paul)
  life / death : 90 days
  ndps  : 180 days (NDPS s.36A(4); extendable to one year on the Public Prosecutor's report)
  uapa  : 90 days (UAPA s.43D(2); extendable to 180 days on the Public Prosecutor's report)
  The day of first remand counts as day 1 (ED v. Kapil Wadhawan, 2024 INSC 58). Day N = remand + (N-1).
  The right to default bail accrues on day N+1 and lasts only until the charge sheet is actually filed.

undertrial — s.479: one-half of the maximum imprisonment for the offence; one-third for a first-time offender
  (never convicted of any offence). Not available for offences punishable with death or life imprisonment,
  nor where more than one case/offence is pending (s.479(2)). Fractions are applied in calendar months.

Verify ss.187 and 479 on https://www.indiacode.nic.in/ — this script encodes the text as read on the version date.
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

PERIODS = {"other": 60, "min10": 90, "life": 90, "death": 90, "ndps": 180, "uapa": 90}
EXTENDABLE = {"ndps": 365, "uapa": 180}


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


def default_bail(remand: date, punishment: str, today: date) -> dict:
    days = PERIODS[punishment]
    last_day = remand + timedelta(days=days - 1)
    accrues = last_day + timedelta(days=1)
    rows = [
        {"step": "First remand (day 1)", "date": remand, "note": "day of remand counts — Kapil Wadhawan"},
        {"step": f"Last day of permitted detention (day {days})", "date": last_day, "note": "charge sheet must be filed by this day"},
        {"step": "Right to default bail accrues", "date": accrues,
         "note": "apply AND offer bail before the charge sheet is filed (Sanjay Dutt; M. Ravindran)"},
    ]
    notes = []
    if punishment in EXTENDABLE:
        ext = remand + timedelta(days=EXTENDABLE[punishment] - 1)
        rows.append({"step": f"Outer limit if extended (day {EXTENDABLE[punishment]})", "date": ext,
                     "note": "only on a Public Prosecutor's report and after hearing the accused"})
        notes.append("special statute: check whether an extension order exists before claiming the right")
    if today < accrues:
        status = f"{(accrues - today).days} day(s) until the right accrues"
    else:
        status = "right has accrued — confirm no charge sheet is on record, then file today"
    notes.append("if the charge sheet was filed on or before the last day, there is no default-bail right; argue regular bail")
    return {"mode": "default", "punishment": punishment, "today": today, "status": status, "rows": rows, "notes": notes}


def undertrial(custody_from: date, max_years: int, first_time: bool, today: date) -> dict:
    months = max_years * 12
    half = add_months(custody_from, months // 2)
    rows = [{"step": "Custody began", "date": custody_from, "note": "investigation, inquiry and trial custody all count"},
            {"step": f"One-half of maximum ({months // 2} months)", "date": half, "note": "s.479(1) main provision"}]
    if first_time:
        third = add_months(custody_from, months // 3)
        rows.insert(1, {"step": f"One-third of maximum ({months // 3} months) — first-time offender", "date": third,
                        "note": "s.479(1) proviso; 'never convicted of any offence'"})
    trigger = rows[1]["date"]
    status = ("eligible now — the jail superintendent should have applied (s.479(3))" if today >= trigger
              else f"{(today - custody_from).days} day(s) served; eligible from {trigger}")
    notes = ["not available for offences punishable with death or life imprisonment",
             "not available where more than one case or offence is pending against the person (s.479(2))",
             "applies to undertrials whose cases were pending on 1 July 2024 (In re Inhuman Conditions in 1382 Prisons, 23.08.2024)",
             "if the maximum is not a whole number of years (e.g. 'two years or fine'), compute by hand and show the working"]
    return {"mode": "undertrial", "today": today, "status": status, "rows": rows, "notes": notes}


def render(r: dict) -> str:
    title = "Default bail — BNSS s.187(3)" if r["mode"] == "default" else "Undertrial release — BNSS s.479"
    out = [f"{title} (as of {r['today']})", "", "| Step | Date | Note |", "|---|---|---|"]
    out += [f"| {x['step']} | {x['date'].isoformat()} | {x['note']} |" for x in r["rows"]]
    out += ["", f"Status: {r['status']}", "", "Notes:"] + [f"- {n}" for n in r["notes"]]
    out.append("")
    out.append("Court holidays not applied. Verify ss.187/479 on India Code.")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    d = sub.add_parser("default")
    d.add_argument("--remand", required=True, help="date of FIRST remand, YYYY-MM-DD")
    d.add_argument("--punishment", required=True, choices=sorted(PERIODS))
    u = sub.add_parser("undertrial")
    u.add_argument("--custody-from", required=True, help="date custody began, YYYY-MM-DD")
    u.add_argument("--max-years", required=True, type=int, help="maximum imprisonment for the offence, in whole years")
    u.add_argument("--first-time", action="store_true", help="never convicted of any offence")
    for p in (d, u):
        p.add_argument("--today")
        p.add_argument("--json", action="store_true")
    a = ap.parse_args()
    today = parse(a.today) or date.today()
    if a.mode == "default":
        r = default_bail(parse(a.remand), a.punishment, today)
    else:
        if a.max_years <= 0:
            sys.exit("--max-years must be a positive whole number")
        r = undertrial(parse(a.custody_from), a.max_years, a.first_time, today)
    if a.json:
        print(json.dumps(r, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
