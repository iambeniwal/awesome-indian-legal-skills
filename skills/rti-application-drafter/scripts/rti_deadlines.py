#!/usr/bin/env python3
"""Deadline calculator for an RTI Act, 2005 matter. Standard library only, offline.

Example:
  python3 rti_deadlines.py --applied 2026-09-01 --today 2026-11-06
  python3 rti_deadlines.py --applied 2026-09-01 --route apio --third-party --reply 2026-10-20
  python3 rti_deadlines.py --applied 2026-09-01 --first-appeal 2026-10-10 --faa-decision 2026-11-02

Rules applied (verify against the Act on India Code):
  PIO reply       : 30 days from receipt (s.7(1)); 48 hours where life or liberty is concerned;
                    +5 days when the application went through an Assistant PIO (s.5(2));
                    40 days where third-party information is involved (s.11(3)).
  deemed refusal  : no reply within the period (s.7(2)).
  first appeal    : within 30 days of the decision, or of the expiry of the reply period (s.19(1)); condonable.
  FAA decision    : within 30 days, extendable to 45 days for reasons recorded (s.19(6)).
  second appeal   : within 90 days of the FAA decision, or of the date it should have been made (s.19(3)); condonable.
The period between a further-fee intimation under s.7(3) and payment is excluded; pass the number of
days with --fee-gap-days. Holidays are not applied.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta


def parse(d: str | None) -> date | None:
    if d is None:
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"bad date {d!r}: use YYYY-MM-DD")


def status(deadline: date, done_on: date | None, today: date) -> str:
    if done_on is not None:
        return "in time" if done_on <= deadline else "LATE — seek condonation / treat as deemed refusal"
    if today > deadline:
        return "EXPIRED"
    return f"{(deadline - today).days} day(s) left"


def compute(applied: date, route: str, third_party: bool, life_liberty: bool, fee_gap_days: int,
            reply: date | None, first_appeal: date | None, faa_decision: date | None, today: date) -> dict:
    rows: list[dict] = []
    notes: list[str] = []

    if life_liberty:
        reply_days, rule = 2, "48 hours (life or liberty, s.7(1))"
    elif third_party:
        reply_days, rule = 40, "40 days (third-party information, s.11(3))"
    else:
        reply_days, rule = 30, "30 days (s.7(1))"
    if route == "apio":
        reply_days += 5
        rule += " + 5 days via APIO (s.5(2))"
    if fee_gap_days:
        reply_days += fee_gap_days
        rule += f" + {fee_gap_days} days fee gap (s.7(3))"
    reply_deadline = applied + timedelta(days=reply_days)
    rows.append({"step": "PIO reply due", "rule": rule, "deadline": reply_deadline,
                 "status": status(reply_deadline, reply, today)})

    if reply is None and today > reply_deadline:
        notes.append("no reply within time = deemed refusal (s.7(2)); information must now be supplied free of cost (s.7(6)); file the first appeal")
    if reply is not None and reply > reply_deadline:
        notes.append("reply was late; information is free of cost (s.7(6)) and the delay supports a s.20 penalty prayer")

    fa_from = reply if reply is not None else reply_deadline
    fa_deadline = fa_from + timedelta(days=30)
    rows.append({"step": "First appeal due (s.19(1))", "rule": "30 days from decision or from expiry of reply period",
                 "deadline": fa_deadline, "status": status(fa_deadline, first_appeal, today)})

    if first_appeal is None:
        rows.append({"step": "FAA decision due (s.19(6))", "rule": "30 days, extendable to 45", "deadline": None,
                     "status": "needs first-appeal filing date"})
        rows.append({"step": "Second appeal due (s.19(3))", "rule": "90 days from FAA decision or its due date",
                     "deadline": None, "status": "needs first-appeal filing date"})
        return {"rows": rows, "notes": notes, "today": today}

    faa_30 = first_appeal + timedelta(days=30)
    faa_45 = first_appeal + timedelta(days=45)
    rows.append({"step": "FAA decision due (s.19(6))", "rule": "30 days (45 with reasons)", "deadline": faa_45,
                 "status": status(faa_45, faa_decision, today) + f" (30-day mark: {faa_30.isoformat()})"})
    sa_from = faa_decision if faa_decision is not None else faa_45
    sa_deadline = sa_from + timedelta(days=90)
    rows.append({"step": "Second appeal due (s.19(3))", "rule": "90 days from FAA decision or from its due date",
                 "deadline": sa_deadline, "status": status(sa_deadline, None, today)})
    if faa_decision is None and today > faa_45:
        notes.append("FAA has not decided within 45 days; second appeal lies from the due date — do not wait for an order")
    if today > sa_deadline:
        notes.append("second appeal is beyond 90 days; file with a condonation request explaining each day of delay (s.19(3) proviso)")
    return {"rows": rows, "notes": notes, "today": today}


def render(result: dict) -> str:
    out = [f"RTI timeline (as of {result['today']})", "",
           "| Step | Rule | Deadline | Status |", "|---|---|---|---|"]
    for r in result["rows"]:
        dl = r["deadline"].isoformat() if r["deadline"] else "—"
        out.append(f"| {r['step']} | {r['rule']} | {dl} | {r['status']} |")
    if result["notes"]:
        out += ["", "Notes:"] + [f"- {n}" for n in result["notes"]]
    out += ["", "Days run from receipt by the PIO (use the delivery/online acknowledgement date). Holidays not applied. Verify ss.7, 11, 19 on India Code."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--applied", required=True, help="date the application was received by the public authority")
    ap.add_argument("--route", choices=["direct", "apio"], default="direct")
    ap.add_argument("--third-party", action="store_true", help="third-party information involved (s.11)")
    ap.add_argument("--life-liberty", action="store_true", help="information concerns life or liberty (48 hours)")
    ap.add_argument("--fee-gap-days", type=int, default=0, help="days between further-fee intimation and payment (s.7(3))")
    ap.add_argument("--reply", help="date the PIO's reply was received")
    ap.add_argument("--first-appeal", help="date the first appeal was filed")
    ap.add_argument("--faa-decision", help="date of the First Appellate Authority's decision")
    ap.add_argument("--today", help="override today's date")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    today = parse(a.today) or date.today()
    result = compute(parse(a.applied), a.route, a.third_party, a.life_liberty, a.fee_gap_days,
                     parse(a.reply), parse(a.first_appeal), parse(a.faa_decision), today)
    if a.json:
        print(json.dumps(result, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
