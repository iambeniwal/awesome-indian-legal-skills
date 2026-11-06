#!/usr/bin/env python3
"""Deadline calculator for a section 138 NI Act matter. Standard library only, offline.

Example:
  python3 s138_timeline.py --cheque-date 2026-07-01 --memo-received 2026-08-20 \
      --notice-sent 2026-09-05 --notice-served 2026-09-09 --today 2026-11-06

Rules applied (verify against the current text of ss.138 and 142 on India Code):
  presentment  : within 3 months of the cheque date (s.138 proviso (a) read with RBI validity)
  notice       : written demand within 30 days of RECEIPT of information of dishonour (proviso (b))
  payment      : drawer has 15 days from RECEIPT of notice (proviso (c))
  cause of action : arises the day after the 15-day window closes
  complaint    : within one month of the cause of action, excluding the day it arose
                 (s.142(1)(b); Econ Antri v. Rom Industries) — i.e. coa + 1 calendar month
Deadline rule: periods expressed in days end on receipt_date + N; the act must happen on or before that day.
Court holidays are NOT applied; if the last day is a holiday, s.4 Limitation Act / s.10 General
Clauses Act lets the act be done on the next working day — check the court calendar.
"""
from __future__ import annotations

import argparse
import calendar
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


def add_months(d: date, months: int) -> date:
    """Calendar-month addition, clamped to month end (31 Jan + 1 month = 28/29 Feb)."""
    y, m = divmod(d.month - 1 + months, 12)
    year, month = d.year + y, m + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def status(deadline: date, done_on: date | None, today: date, label: str) -> str:
    if done_on is not None:
        return "in time" if done_on <= deadline else f"LATE — {label} after deadline"
    if today > deadline:
        return "EXPIRED"
    left = (deadline - today).days
    return f"{left} day(s) left"


def compute(cheque_date: date, memo_received: date, notice_sent: date | None, notice_served: date | None,
            today: date, presented_on: date | None = None) -> dict:
    rows: list[dict] = []
    notes: list[str] = []

    presentment_deadline = add_months(cheque_date, 3)
    rows.append({
        "step": "Presentment within validity",
        "rule": "cheque date + 3 months",
        "deadline": presentment_deadline,
        "status": status(presentment_deadline, presented_on or memo_received, today, "presentment"),
    })
    if memo_received < cheque_date:
        notes.append("memo received before the cheque date — check the dates (post-dated cheque presented early?)")

    notice_deadline = memo_received + timedelta(days=30)
    rows.append({
        "step": "Written demand notice",
        "rule": "receipt of return memo + 30 days",
        "deadline": notice_deadline,
        "status": status(notice_deadline, notice_sent, today, "notice"),
    })

    if notice_served is None:
        rows.append({
            "step": "15-day payment window",
            "rule": "RECEIPT of notice + 15 days",
            "deadline": None,
            "status": "needs date of service (AD card / tracking / deemed service)",
        })
        rows.append({
            "step": "Complaint under s.142(1)(b)",
            "rule": "cause of action (day after window) + 1 month",
            "deadline": None,
            "status": "cannot compute without service date",
        })
        notes.append("without a service date, no complaint deadline exists; do not file until the 15 days from service have expired (Yogendra Pratap Singh)")
        return {"rows": rows, "notes": notes, "today": today}

    if notice_sent and notice_served < notice_sent:
        notes.append("service date is before dispatch date — check the dates")

    window_end = notice_served + timedelta(days=15)
    rows.append({
        "step": "15-day payment window",
        "rule": "receipt of notice + 15 days",
        "deadline": window_end,
        "status": "open — do NOT file yet" if today <= window_end else "closed",
    })

    coa = window_end + timedelta(days=1)
    complaint_deadline = add_months(coa, 1)
    rows.append({
        "step": "Cause of action arises",
        "rule": "day after the window closes",
        "deadline": coa,
        "status": "not yet arisen" if today < coa else "arisen",
    })
    rows.append({
        "step": "Complaint under s.142(1)(b)",
        "rule": "cause of action + 1 month (day of CoA excluded)",
        "deadline": complaint_deadline,
        "status": status(complaint_deadline, None, today, "complaint"),
    })
    if today > complaint_deadline:
        notes.append(f"complaint is {(today - complaint_deadline).days} day(s) beyond limitation; an application under the proviso to s.142(1)(b) must explain each day of delay")
    return {"rows": rows, "notes": notes, "today": today}


def render(result: dict) -> str:
    out = [f"s.138 timeline (as of {result['today']})", "",
           "| Step | Rule | Deadline | Status |", "|---|---|---|---|"]
    for r in result["rows"]:
        dl = r["deadline"].isoformat() if r["deadline"] else "—"
        out.append(f"| {r['step']} | {r['rule']} | {dl} | {r['status']} |")
    if result["notes"]:
        out += ["", "Notes:"] + [f"- {n}" for n in result["notes"]]
    out += ["", "Court holidays not applied; a deadline falling on a holiday moves to the next working day. Verify ss.138/142 on India Code."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cheque-date", required=True, help="date written on the cheque, YYYY-MM-DD")
    ap.add_argument("--memo-received", required=True, help="date the payee received the return memo / dishonour information")
    ap.add_argument("--presented-on", help="date the cheque was presented (defaults to memo date for the validity check)")
    ap.add_argument("--notice-sent", help="date the demand notice was dispatched")
    ap.add_argument("--notice-served", help="date the drawer received the notice (or deemed service date)")
    ap.add_argument("--today", help="override today's date for the status column")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()

    today = parse(a.today) or date.today()
    result = compute(parse(a.cheque_date), parse(a.memo_received), parse(a.notice_sent), parse(a.notice_served),
                     today, parse(a.presented_on))
    if a.json:
        def enc(o):
            return o.isoformat() if isinstance(o, date) else str(o)
        print(json.dumps(result, default=enc, indent=2))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
