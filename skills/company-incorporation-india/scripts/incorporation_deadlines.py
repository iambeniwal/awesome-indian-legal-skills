#!/usr/bin/env python3
"""Post-incorporation deadline table for an Indian company, OPC, Section 8 company or LLP.
Standard library only, offline.

Example:
  python3 incorporation_deadlines.py --incorporated 2026-11-06 --entity llp --today 2026-11-20
  python3 incorporation_deadlines.py --incorporated 2026-01-15 --entity company --subscription-received 2026-02-01

Rules applied (verify on India Code / mca.gov.in; MCA circulars can extend dates):
  company/opc/section8:
    first board meeting      s.173(1)      incorporation + 30 days
    first auditor (board)    s.139(6)      incorporation + 30 days
    ADT-1                    Rule 4 A&A    appointment + 15 days  (shown from the latest permitted appointment date)
    INC-22 (if RO later)     s.12(4)       incorporation + 30 days
    share certificates       s.56(4)(a)    incorporation + 2 months
    INC-20A                  s.10A         incorporation + 180 days (needs subscription money received first)
    first FY end             s.2(41)       31 March of the following year if incorporated on/after 1 Jan, else 31 March of the current FY
    first AGM                s.96(1)       first FY end + 9 months (not for OPC)
  llp:
    Form 3 (LLP Agreement)   s.23          incorporation + 30 days
    first FY end             s.2(1)(l)     if incorporated after 30 Sept, may end 31 March of the year after next; else 31 March of the current FY
    Form 11                  Rule 25       FY end + 60 days  (30 May)
    Form 8                   Rule 24       30 October after FY end
Deadline convention: "+N days" means the act must be done on or before incorporation + N days. Months are calendar months,
clamped to month end. Court/ROC holidays are not applied.
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

ENTITIES = ("company", "opc", "section8", "llp")


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
        return f"OVERDUE by {(today - deadline).days} day(s)"
    left = (deadline - today).days
    return "due today" if left == 0 else f"{left} day(s) left"


def first_fy_end_company(inc: date) -> date:
    # s.2(41): incorporated on/after 1 January -> FY ends 31 March of the following year
    if inc.month >= 1 and inc < date(inc.year, 4, 1):
        return date(inc.year + 1, 3, 31)
    return date(inc.year + 1, 3, 31)


def first_fy_end_llp(inc: date) -> date:
    # s.2(1)(l) LLP Act: incorporated after 30 September -> FY may end 31 March of the year after next
    if inc > date(inc.year, 9, 30):
        return date(inc.year + 2, 3, 31)
    if inc < date(inc.year, 4, 1):
        return date(inc.year, 3, 31) if inc <= date(inc.year, 3, 31) else date(inc.year + 1, 3, 31)
    return date(inc.year + 1, 3, 31)


def compute(inc: date, entity: str, today: date, subscription: date | None = None, ro_later: bool = False) -> dict:
    rows: list[dict] = []
    notes: list[str] = []

    def row(step, rule, deadline, note=""):
        rows.append({"step": step, "rule": rule, "deadline": deadline, "status": status(deadline, today), "note": note})

    if entity in ("company", "opc", "section8"):
        bm = inc + timedelta(days=30)
        row("First board meeting", "s.173(1): +30 days", bm, "MBP-1 and DIR-8 disclosures at this meeting")
        row("First auditor appointed by board", "s.139(6): +30 days", bm, "else members appoint in EGM within 90 days")
        row("ADT-1 for first auditor", "Rule 4: appointment +15 days", bm + timedelta(days=15),
            "latest date if appointed on day 30; legally contested for s.139(6) — MCA FAQ says file")
        if ro_later:
            row("INC-22 registered office", "s.12(4): +30 days", inc + timedelta(days=30), "only if RO was not given at incorporation")
        row("Share certificates to subscribers", "s.56(4)(a): +2 months", add_months(inc, 2), "")
        inc20a = inc + timedelta(days=180)
        sub_note = "after subscription money is received"
        if subscription:
            if subscription > inc20a:
                notes.append("subscription money received AFTER the INC-20A deadline — INC-20A cannot be filed in time; expect s.10A penalties and strike-off risk")
            sub_note = f"subscription received {subscription.isoformat()}"
        row("INC-20A declaration of commencement", "s.10A: +180 days", inc20a, sub_note + "; no business or borrowing before filing")
        fy_end = first_fy_end_company(inc)
        row("First financial year ends", "s.2(41)", fy_end, "incorporated on/after 1 Jan → FY runs to 31 Mar of the following year")
        if entity == "opc":
            notes.append("OPC: no AGM (s.96(1) exemption); AOC-4 within 180 days of FY end and MGT-7A within 60 days of the date the AGM would have been due")
        else:
            row("First AGM", "s.96(1) proviso: first FY end + 9 months", add_months(fy_end, 9), "unless extended by ROC under s.96(1)")
        notes.append("open the bank account and bring in subscription money before INC-20A; set up registers (ss.88, 170), books (s.128), name board and letterhead with CIN (s.12(3))")
    else:
        row("LLP Agreement — Form 3", "s.23 LLP Act: +30 days", inc + timedelta(days=30), "stamp duty per State on contribution; late filing → 2022 slab fees")
        fy_end = first_fy_end_llp(inc)
        row("First financial year ends", "s.2(1)(l) LLP Act", fy_end, "incorporated after 30 Sept → may run to 31 Mar of the year after next")
        row("Form 11 annual return", "Rule 25: FY end + 60 days", fy_end + timedelta(days=60), "30 May")
        row("Form 8 statement of account & solvency", "Rule 24: 30 October after FY end", date(fy_end.year, 10, 30), "audit if turnover >₹40 lakh or contribution >₹25 lakh")
        notes.append("DIR-3 KYC for every DPIN holder by 30 September each year")
    notes.append("every date is 'unless extended by MCA circular'; verify forms and fees on mca.gov.in")
    return {"entity": entity, "incorporated": inc, "today": today, "rows": rows, "notes": notes}


def render(r: dict) -> str:
    out = [f"Post-incorporation deadlines — {r['entity']} incorporated {r['incorporated']} (as of {r['today']})", "",
           "| Step | Rule | Deadline | Status | Note |", "|---|---|---|---|---|"]
    for x in r["rows"]:
        out.append(f"| {x['step']} | {x['rule']} | {x['deadline'].isoformat()} | {x['status']} | {x['note']} |")
    out += ["", "Notes:"] + [f"- {n}" for n in r["notes"]]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--incorporated", required=True)
    ap.add_argument("--entity", required=True, choices=ENTITIES)
    ap.add_argument("--subscription-received")
    ap.add_argument("--registered-office-later", action="store_true")
    ap.add_argument("--today")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = compute(parse(a.incorporated), a.entity, parse(a.today) or date.today(), parse(a.subscription_received), a.registered_office_later)
    if a.json:
        print(json.dumps(r, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
