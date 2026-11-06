#!/usr/bin/env python3
"""Deadline and limitation calculator for GST notices under the CGST Act, 2017. Offline, standard library.

Examples:
  python3 gst_deadlines.py --notice asmt10 --date 2026-10-01
  python3 gst_deadlines.py --notice drc01 --date 2026-09-15 --period FY2022-23 --section 73
  python3 gst_deadlines.py --notice drc01 --date 2026-09-15 --period FY2024-25 --section 74A
  python3 gst_deadlines.py --notice order --date 2026-08-20 --disputed-tax 12000000
  python3 gst_deadlines.py --notice appeal-order --date 2026-08-20 --disputed-tax 12000000 --json

What it computes (verify every rule on cbic-gst.gov.in — circulars and notifications change these):
  asmt10        reply in ASMT-11 within 30 days of service (s.61, r.99; officer may allow more)
  drc01a        pre-SCN intimation: no statutory period; officer-set date (commonly 15 days) — pay/explain in Part B
  drc01         SCN: reply in DRC-06 by the date in the notice (commonly 30 days); settlement windows:
                  s.73  pay tax+interest within 30 days of SCN → no penalty (s.73(8))
                  s.74  pay tax+interest+25% penalty within 30 days of SCN (s.74(8))
                  s.74A pay within 60 days of SCN → no penalty (non-fraud) / 25% (fraud) (s.74A(8)–(9) — verify)
                plus the notice/order LIMITATION for the period (see below)
  order         DRC-07 order: s.161 rectification within 3 months of issue; s.107 appeal within 3 months of
                communication (+1 month condonable); pre-deposit 10% of disputed tax, capped at ₹20 crore CGST
                (s.107(6) as amended from 1 Nov 2024 — verify); s.73(9)/s.74(11) pay-within-30-days penalty windows
  appeal-order  first-appeal order: s.112 appeal to GSTAT within 3 months (+3 months condonable, s.112(6));
                additional pre-deposit 10% of disputed tax (cap ₹20 crore CGST, from 1 Nov 2024 — verify)

Limitation (ss.73/74/74A), counted from the DUE DATE of the annual return (GSTR-9) for the FY:
  s.73  order within 3 years of the due date; SCN at least 3 months before that (s.73(2),(10))
  s.74  order within 5 years; SCN at least 6 months before (s.74(2),(10))
  s.74A (FY 2024-25 onwards) SCN within 42 months of the due date; order within 12 months of the SCN,
        extendable by up to 6 months by an officer not below Joint Commissioner (s.74A(2),(7) — verify)
Default annual-return due dates (ALL "verify" — several were extended by notification):
  FY2017-18 2020-02-05 · FY2018-19 2020-12-31 · FY2019-20 2021-03-31 · FY2020-21 2022-02-28
  FY2021-22 2022-12-31 · FY2022-23 2023-12-31 · FY2023-24 2024-12-31 · FY2024-25 2025-12-31
s.73 ORDER deadlines for FY2017-18/18-19/19-20 were extended under s.168A (Notifications 9/2023, 56/2023)
to 2023-12-31 / 2024-04-30 / 2024-08-31; the validity of 56/2023 was litigated — the script prints both.
Court holidays are not applied; a deadline on a holiday moves to the next working day.
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

ANNUAL_RETURN_DUE = {
    "FY2017-18": date(2020, 2, 5), "FY2018-19": date(2020, 12, 31), "FY2019-20": date(2021, 3, 31),
    "FY2020-21": date(2022, 2, 28), "FY2021-22": date(2022, 12, 31), "FY2022-23": date(2023, 12, 31),
    "FY2023-24": date(2024, 12, 31), "FY2024-25": date(2025, 12, 31),
}
S73_EXTENDED_ORDER = {"FY2017-18": date(2023, 12, 31), "FY2018-19": date(2024, 4, 30), "FY2019-20": date(2024, 8, 31)}
PREDEPOSIT_CAP_CGST = 20_00_00_000  # ₹20 crore (verify)


def inr(n: float) -> str:
    """Indian digit grouping: 1200000 -> '12,00,000'; 200000000 -> '20,00,00,000'."""
    s = str(int(round(n)))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


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


def status(deadline: date, today: date) -> str:
    if today > deadline:
        return "EXPIRED"
    return f"{(deadline - today).days} day(s) left"


def limitation(period: str, section: str, due: date | None, today: date) -> tuple[list[dict], list[str]]:
    rows, notes = [], []
    if due is None:
        due = ANNUAL_RETURN_DUE.get(period)
        if due is None:
            notes.append(f"no default annual-return due date for {period}; pass --annual-return-due")
            return rows, notes
        notes.append(f"annual-return due date for {period} taken as {due} (default table — verify)")
    if section == "73":
        order_by, notice_by = add_months(due, 36), add_months(due, 33)
        rows += [{"step": "s.73 SCN last date", "rule": "due date + 33 months", "deadline": notice_by, "status": status(notice_by, today)},
                 {"step": "s.73 order last date", "rule": "due date + 3 years", "deadline": order_by, "status": status(order_by, today)}]
        if period in S73_EXTENDED_ORDER:
            ext = S73_EXTENDED_ORDER[period]
            rows.append({"step": "s.73 order — extended (s.168A notifications)", "rule": "Not. 9/2023 & 56/2023", "deadline": ext, "status": status(ext, today)})
            notes.append("the s.168A extensions were challenged in several High Courts; check the current position before conceding them")
    elif section == "74":
        order_by, notice_by = add_months(due, 60), add_months(due, 54)
        rows += [{"step": "s.74 SCN last date", "rule": "due date + 54 months", "deadline": notice_by, "status": status(notice_by, today)},
                 {"step": "s.74 order last date", "rule": "due date + 5 years", "deadline": order_by, "status": status(order_by, today)}]
    elif section == "74A":
        notice_by = add_months(due, 42)
        rows.append({"step": "s.74A SCN last date", "rule": "due date + 42 months", "deadline": notice_by, "status": status(notice_by, today)})
        notes.append("s.74A applies to FY 2024-25 onwards; the order is due 12 months from the SCN (+6 months by a JC-or-above with reasons) — computed from the SCN date when given")
    return rows, notes


def compute(notice: str, on: date, today: date, period: str | None, section: str | None,
            due: date | None, disputed_tax: float | None) -> dict:
    rows: list[dict] = []
    notes: list[str] = []
    if notice == "asmt10":
        d = on + timedelta(days=30)
        rows.append({"step": "ASMT-11 reply", "rule": "service + 30 days (s.61, r.99)", "deadline": d, "status": status(d, today)})
    elif notice == "drc01a":
        rows.append({"step": "Part B response", "rule": "date fixed in the intimation (no statutory period)", "deadline": None, "status": "read the notice; commonly 15 days"})
        notes.append("paying under DRC-01A Part B (tax + interest) before the SCN avoids penalty under s.73 / limits it under s.74 (15%)")
    elif notice == "drc01":
        rows.append({"step": "DRC-06 reply", "rule": "date fixed in the SCN (commonly 30 days)", "deadline": on + timedelta(days=30), "status": "confirm the date on the notice"})
        if section == "74A":
            w = on + timedelta(days=60)
            rows.append({"step": "s.74A settlement window", "rule": "SCN + 60 days (nil penalty non-fraud / 25% fraud — verify)", "deadline": w, "status": status(w, today)})
        else:
            w = on + timedelta(days=30)
            rows.append({"step": f"s.{section or '73/74'} settlement window", "rule": "SCN + 30 days (s.73(8) nil penalty / s.74(8) 25%)", "deadline": w, "status": status(w, today)})
            rows.append({"step": "s.73/74 order due", "rule": "within the period's limitation (below); s.75(10) — order beyond it is void", "deadline": None, "status": "see limitation rows"})
        if section == "74A":
            o = add_months(on, 12)
            rows.append({"step": "s.74A order last date", "rule": "SCN + 12 months (+6 months extension possible)", "deadline": o, "status": status(o, today)})
        if period:
            lim, ln = limitation(period, section or "73", due, today)
            rows += lim
            notes += ln
    elif notice in ("order", "appeal-order"):
        if notice == "order":
            r = add_months(on, 3)
            rows.append({"step": "s.161 rectification", "rule": "issue + 3 months (no rectification after 6 months)", "deadline": r, "status": status(r, today)})
            a = add_months(on, 3)
            rows.append({"step": "s.107 appeal to Appellate Authority", "rule": "communication + 3 months", "deadline": a, "status": status(a, today)})
            c = add_months(a, 1)
            rows.append({"step": "s.107 condonable limit", "rule": "+1 month with sufficient cause (s.107(4))", "deadline": c, "status": status(c, today)})
            p = on + timedelta(days=30)
            rows.append({"step": "pay-within-30-days window", "rule": "s.73(9): 10%/₹10,000 penalty · s.74(11): 50% if paid within 30 days of order", "deadline": p, "status": status(p, today)})
            pct, label = 0.10, "s.107(6) pre-deposit"
        else:
            a = add_months(on, 3)
            rows.append({"step": "s.112 appeal to GSTAT", "rule": "communication + 3 months", "deadline": a, "status": status(a, today)})
            c = add_months(a, 3)
            rows.append({"step": "s.112 condonable limit", "rule": "+3 months with sufficient cause (s.112(6))", "deadline": c, "status": status(c, today)})
            pct, label = 0.10, "s.112(8) additional pre-deposit"
            notes.append("transitional window for orders communicated before the GSTAT start date closed on 31 July 2026 (extended from 30 June 2026 — verify the cutoff dates)")
        if disputed_tax is not None:
            dep = min(disputed_tax * pct, PREDEPOSIT_CAP_CGST)
            rows.append({"step": label, "rule": f"{int(pct*100)}% of disputed TAX only (not interest/penalty), cap ₹20 crore CGST — verify", "deadline": None,
                         "status": f"₹{inr(dep)} (+ equal SGST share where applicable)"})
            notes.append("admitted tax must be paid in full before appeal; the pre-deposit is on the disputed tax")
    return {"notice": notice, "date": on, "today": today, "rows": rows, "notes": notes}


def render(res: dict) -> str:
    out = [f"GST deadlines — {res['notice']} dated {res['date']} (as of {res['today']})", "",
           "| Step | Rule | Deadline | Status |", "|---|---|---|---|"]
    for r in res["rows"]:
        out.append(f"| {r['step']} | {r['rule']} | {r['deadline'].isoformat() if r['deadline'] else '—'} | {r['status']} |")
    if res["notes"]:
        out += ["", "Notes:"] + [f"- {n}" for n in res["notes"]]
    out += ["", "Holidays not applied. Verify every rule on cbic-gst.gov.in; CBIC circulars and s.168A notifications change these."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--notice", required=True, choices=["asmt10", "drc01a", "drc01", "order", "appeal-order"])
    ap.add_argument("--date", required=True, help="date of service/communication of the notice or order, YYYY-MM-DD")
    ap.add_argument("--period", help="tax period, e.g. FY2022-23")
    ap.add_argument("--section", choices=["73", "74", "74A"])
    ap.add_argument("--annual-return-due", help="override the GSTR-9 due date used for limitation")
    ap.add_argument("--disputed-tax", type=float, help="disputed tax (₹) for the pre-deposit computation")
    ap.add_argument("--today")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = compute(a.notice, parse(a.date), parse(a.today) or date.today(), a.period, a.section,
                  parse(a.annual_return_due), a.disputed_tax)
    if a.json:
        print(json.dumps(res, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2, ensure_ascii=False))
    else:
        print(render(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
