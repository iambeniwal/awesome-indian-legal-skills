#!/usr/bin/env python3
"""Delay and interest calculator for a RERA s.18 claim. Standard library only, offline.

Examples:
  # stay-in mode: interest on every tranche from the effective due date to today
  python3 rera_delay.py --promised 2022-12-31 --grace-months 6 --extension-months 0 --rate 10.85 \
      --mode delay --paid 2019-03-10:1500000 --paid 2020-01-15:2500000 --until 2026-11-06

  # refund mode: interest on every tranche from its payment date to the refund date
  python3 rera_delay.py --promised 2022-12-31 --rate 10.85 --mode refund --paid 2019-03-10:1500000 --until 2026-11-06

The rate is ALWAYS an input. Most State RERA Rules prescribe "SBI's highest MCLR + 2% per annum";
look up the State rule and the current MCLR and pass the resulting figure. Simple interest, actual
days / 365. Months of delay are whole calendar months from the effective due date.
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime


def parse(d: str) -> date:
    try:
        return datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"bad date {d!r}: use YYYY-MM-DD")


def add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    year, month = d.year + y, m + 1
    return date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


def whole_months_between(start: date, end: date) -> int:
    if end <= start:
        return 0
    months = (end.year - start.year) * 12 + (end.month - start.month)
    if end.day < start.day:
        months -= 1
    return max(months, 0)


def simple_interest(principal: float, rate_pct: float, start: date, end: date) -> float:
    days = max((end - start).days, 0)
    return principal * rate_pct / 100 * days / 365


def compute(promised: date, grace_months: int, extension_months: int, rate: float, mode: str,
            paid: list[tuple[date, float]], until: date) -> dict:
    due = add_months(add_months(promised, grace_months), extension_months)
    months_delay = whole_months_between(due, until)
    rows = []
    total_paid = 0.0
    total_interest = 0.0
    for pdate, amount in sorted(paid):
        start = pdate if mode == "refund" else due
        interest = simple_interest(amount, rate, start, until)
        rows.append({"paid_on": pdate, "amount": amount, "interest_from": start, "days": max((until - start).days, 0), "interest": round(interest, 2)})
        total_paid += amount
        total_interest += interest
    notes = []
    if until <= due:
        notes.append("the effective due date has not passed — no delay yet; check the extension figure and the grace clause")
    if any(p > until for p, _ in paid):
        notes.append("a payment date is after the --until date — check the dates")
    if mode == "delay" and any(p > due for p, _ in paid):
        notes.append("some tranches were paid after the due date; in delay mode interest on them runs from the due date, which overstates the claim — consider refund-style from-payment dates for those tranches")
    return {
        "mode": mode, "promised": promised, "grace_months": grace_months, "extension_months": extension_months,
        "effective_due": due, "until": until, "months_of_delay": months_delay, "rate_pct": rate,
        "rows": rows, "total_paid": round(total_paid, 2), "total_interest": round(total_interest, 2),
        "total_claim": round(total_paid + total_interest, 2) if mode == "refund" else round(total_interest, 2),
        "notes": notes,
    }


def render(r: dict) -> str:
    out = [
        f"RERA s.18 {'refund with interest' if r['mode'] == 'refund' else 'delay interest'} (as of {r['until']})",
        "",
        f"Promised possession: {r['promised']}  + grace {r['grace_months']} m  + Authority extension {r['extension_months']} m  → effective due {r['effective_due']}",
        f"Months of delay to {r['until']}: {r['months_of_delay']}",
        f"Rate applied: {r['rate_pct']}% p.a. simple (INPUT — cite the State Rule and the SBI MCLR date in the output)",
        "",
        "| Paid on | Amount (₹) | Interest from | Days | Interest (₹) |",
        "|---|---|---|---|---|",
    ]
    for row in r["rows"]:
        out.append(f"| {row['paid_on']} | {row['amount']:,.0f} | {row['interest_from']} | {row['days']} | {row['interest']:,.2f} |")
    out += ["", f"Total paid: ₹{r['total_paid']:,.2f}", f"Total interest: ₹{r['total_interest']:,.2f}"]
    out.append(f"Total {'refund + interest' if r['mode'] == 'refund' else 'delay interest'} claim: ₹{r['total_claim']:,.2f}")
    if r["notes"]:
        out += ["", "Notes:"] + [f"- {n}" for n in r["notes"]]
    out += ["", "Compensation (if any) is separate and lies before the Adjudicating Officer. Verify s.18 and the State Rules before filing."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--promised", required=True, help="possession date promised in the agreement, YYYY-MM-DD")
    ap.add_argument("--grace-months", type=int, default=0, help="unconditional grace period in the agreement")
    ap.add_argument("--extension-months", type=int, default=0, help="extension actually granted by the Authority (e.g. COVID orders)")
    ap.add_argument("--rate", type=float, required=True, help="annual interest rate in percent from the State Rules (e.g. SBI MCLR + 2)")
    ap.add_argument("--mode", choices=["delay", "refund"], required=True)
    ap.add_argument("--paid", action="append", required=True, help="YYYY-MM-DD:amount, repeatable")
    ap.add_argument("--until", help="possession / refund / today's date (default: today)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    paid = []
    for item in a.paid:
        d, _, amt = item.partition(":")
        if not amt:
            sys.exit(f"bad --paid {item!r}: use YYYY-MM-DD:amount")
        paid.append((parse(d), float(amt.replace(",", ""))))
    until = parse(a.until) if a.until else date.today()
    r = compute(parse(a.promised), a.grace_months, a.extension_months, a.rate, a.mode, paid, until)
    if a.json:
        print(json.dumps(r, indent=2, default=lambda o: o.isoformat() if isinstance(o, date) else str(o)))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
