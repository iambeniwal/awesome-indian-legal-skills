#!/usr/bin/env python3
"""Forum, fee note, limitation and appeal windows for a Consumer Protection Act, 2019 complaint.

Example:
  python3 consumer_forum.py --consideration 1250000 --cause-date 2025-03-10 --today 2026-11-06
  python3 consumer_forum.py --consideration 75000000 --cause-date 2026-01-01 --json

Rules applied (verify on India Code / e-Gazette before relying):
  forum     : by value of goods or services PAID AS CONSIDERATION (s.34(1)/47(1)/58(1)), per the
              Consumer Protection (Jurisdiction ...) Rules, 2021: District <= 50 lakh;
              State > 50 lakh and <= 2 crore; National > 2 crore. The Central Government may revise.
  fee       : Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Schedule —
              nil up to 5 lakh; above that, read the Schedule (not hard-coded here).
  limitation: 2 years from the cause of action (s.69), condonable for sufficient cause.
  appeals   : District -> State 45 days, 50% deposit (s.41); State -> National 45 days, 50% deposit (s.51);
              National (original) -> Supreme Court 30 days (s.67).
Standard library only; offline; holidays not applied.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta

LAKH = 100_000
CRORE = 10_000_000
DISTRICT_MAX = 50 * LAKH
STATE_MAX = 2 * CRORE
FEE_NIL_MAX = 5 * LAKH


def parse(d: str | None) -> date | None:
    if d is None:
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"bad date {d!r}: use YYYY-MM-DD")


def add_years(d: date, years: int) -> date:
    try:
        return d.replace(year=d.year + years)
    except ValueError:  # 29 Feb
        return d.replace(year=d.year + years, day=28)


def inr(n: float) -> str:
    n = int(round(n))
    if n >= CRORE:
        return f"₹{n / CRORE:g} crore"
    if n >= LAKH:
        return f"₹{n / LAKH:g} lakh"
    return f"₹{n:,}"


def forum(consideration: float) -> dict:
    if consideration <= DISTRICT_MAX:
        name, appeal = "District Commission", "State Commission within 45 days, 50% deposit of amount ordered (s.41)"
    elif consideration <= STATE_MAX:
        name, appeal = "State Commission", "National Commission within 45 days, 50% deposit (s.51)"
    else:
        name, appeal = "National Commission", "Supreme Court within 30 days (s.67)"
    fee = "nil (Schedule to the 2020 Rules, up to ₹5 lakh)" if consideration <= FEE_NIL_MAX \
        else "see the Schedule to the Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020 for the slab (verify)"
    return {"consideration": consideration, "forum": name, "fee": fee, "appeal": appeal}


def compute(consideration: float, cause_date: date | None, today: date) -> dict:
    out = forum(consideration)
    out["today"] = today
    out["notes"] = ["jurisdiction is on consideration PAID; do not use the compensation claimed",
                    "limits are those of the 2021 Rules as known at the skill's version date — verify on e-Gazette"]
    if cause_date:
        deadline = add_years(cause_date, 2)
        out["cause_date"] = cause_date
        out["limitation_deadline"] = deadline
        if today > deadline:
            out["limitation_status"] = f"EXPIRED by {(today - deadline).days} day(s) — file with a condonation application under s.69(2)"
        else:
            out["limitation_status"] = f"{(deadline - today).days} day(s) left"
    else:
        out["limitation_status"] = "needs cause-of-action date"
    return out


def render(r: dict) -> str:
    lines = [f"Consumer Protection Act, 2019 — forum check (as of {r['today']})", "",
             f"Consideration paid : {inr(r['consideration'])}",
             f"Forum              : {r['forum']}",
             f"Fee                : {r['fee']}",
             f"Appeal from order  : {r['appeal']}"]
    if "limitation_deadline" in r:
        lines += [f"Cause of action    : {r['cause_date']}",
                  f"Limitation (s.69)  : {r['limitation_deadline']} — {r['limitation_status']}"]
    else:
        lines += [f"Limitation (s.69)  : {r['limitation_status']}"]
    lines += ["", "Notes:"] + [f"- {n}" for n in r["notes"]]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--consideration", type=float, required=True, help="total paid for the goods/services, in rupees")
    ap.add_argument("--cause-date", help="date the cause of action arose, YYYY-MM-DD")
    ap.add_argument("--today", help="override today's date")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.consideration < 0:
        sys.exit("consideration must be non-negative")
    r = compute(a.consideration, parse(a.cause_date), parse(a.today) or date.today())
    if a.json:
        print(json.dumps(r, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2, ensure_ascii=False))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
