#!/usr/bin/env python3
"""Annual compliance calendar for an Indian private company, small company, OPC, Section 8 company or LLP.
Standard library only, offline.

Example:
  python3 compliance_calendar.py --fy-end 2026-03-31 --entity private --today 2026-11-06
  python3 compliance_calendar.py --fy-end 2027-03-31 --entity private --incorporated 2026-01-15
  python3 compliance_calendar.py --fy-end 2026-03-31 --entity llp --json

Rules applied (verify on India Code / mca.gov.in; every date is "unless extended by MCA circular"):
  AGM            s.96     FY end + 6 months (first AGM: first FY end + 9 months); none for OPC
  AOC-4          s.137    AGM + 30 days; OPC: FY end + 180 days
  MGT-7 / 7A     s.92     AGM + 60 days; OPC: (date AGM was due) + 60 days
  ADT-1          s.139(1) AGM + 15 days (only if an auditor is appointed/re-appointed at that AGM)
  DIR-3 KYC      Rule 12A 30 September of the year the FY ends
  DPT-3          Rule 16  30 June of the year the FY ends
  MSME-1         s.405    31 October (Apr–Sep half) and 30 April (Oct–Mar half)
  LLP Form 11    Rule 25  FY end + 60 days (30 May);  LLP Form 8  Rule 24  31 October... see note: 30 October
  Additional fee for AOC-4 / MGT-7 / MGT-7A: ₹100 per day of delay (s.403; fee, not penalty).
"first FY" is detected when --incorporated falls on or after 1 January of the year before the FY end (s.2(41)).
Months are calendar months, clamped to month end.
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

ENTITIES = ("private", "small", "opc", "section8", "llp")
ADDITIONAL_FEE_PER_DAY = 100  # AOC-4 / MGT-7 / MGT-7A


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


def is_first_fy(fy_end: date, incorporated: date | None) -> bool:
    return incorporated is not None and date(fy_end.year - 1, 1, 1) <= incorporated <= fy_end


def compute(fy_end: date, entity: str, today: date, agm: date | None = None, incorporated: date | None = None,
            window: int = 60) -> dict:
    rows: list[dict] = []
    requirements: list[str] = []
    notes: list[str] = []
    first_fy = is_first_fy(fy_end, incorporated)
    y = fy_end.year

    def row(form, rule, trigger, deadline, note="", fee=False, verify=False):
        r = {"form": form, "rule": rule, "trigger": trigger, "deadline": deadline, "status": status(deadline, today),
             "note": note, "verify": verify}
        if fee and today > deadline:
            r["additional_fee_to_date"] = (today - deadline).days * ADDITIONAL_FEE_PER_DAY
        rows.append(r)

    if entity == "llp":
        requirements.append("No board/AGM machinery; LLP Agreement governs meetings and accounts")
        row("Form 11 annual return", "s.35; Rule 25", "FY end", fy_end + timedelta(days=60), "all LLPs")
        row("Form 8 statement of account & solvency", "s.34; Rule 24", "FY end", date(y, 10, 30),
            "audit if turnover >₹40 lakh or contribution >₹25 lakh")
        row("DIR-3 KYC (each DPIN holder)", "Directors Rules, Rule 12A", "DPIN as on 31 March", date(y, 9, 30),
            "DPIN deactivated on 1 Oct; ₹5,000 to reactivate")
        notes.append("LLP late fees: 2022 slab multipliers (small LLP 1×/2×/4×/6×/10×/15×; other 1×/4×/8×/12×/20×/30×), per-day element beyond 360 days — verify")
    else:
        if entity in ("small", "opc"):
            requirements.append("Board meetings: at least 2 in the FY, one in each half, ≥90 days apart (s.173(5))")
        elif entity == "section8":
            requirements.append("Board meetings: at least one in every six months (Section 8 exemption notification)")
        else:
            requirements.append("Board meetings: at least 4 in the FY, no gap over 120 days (s.173(1))")
        requirements.append("MBP-1 and DIR-8 from every director at the first board meeting of the FY (ss.184, 164)")
        requirements.append("Minutes signed within 30 days of each meeting (s.118); registers kept current (ss.88, 170)")

        if entity == "opc":
            agm_due = add_months(fy_end, 6)
            notes.append("OPC holds no AGM (s.96(1)); AOC-4 runs from FY end and MGT-7A from the date an AGM would have been due")
            row("AOC-4 financial statements", "s.137(1) proviso", "FY end", fy_end + timedelta(days=180),
                "OPC: 180 days from FY end", fee=True)
            row("MGT-7A annual return", "s.92(4)", "date AGM would have been due", agm_due + timedelta(days=60), "", fee=True)
        else:
            agm_due = add_months(fy_end, 9) if first_fy else add_months(fy_end, 6)
            row("AGM", "s.96" + (" (first AGM: first FY end + 9 months)" if first_fy else " (FY end + 6 months)"),
                "FY end", agm_due, "gap between AGMs ≤15 months; ROC may extend by 3 months")
            agm_date = agm or agm_due
            basis = f"AGM held {agm_date}" if agm else f"AGM assumed on last permissible date {agm_due}"
            row("AOC-4 financial statements" + (" (CFS/XBRL if applicable)" if entity in ("private", "section8") else ""),
                "s.137", basis, agm_date + timedelta(days=30), "", fee=True)
            row("MGT-7A annual return" if entity == "small" else "MGT-7 annual return", "s.92", basis,
                agm_date + timedelta(days=60), "", fee=True)
            row("ADT-1 auditor appointment", "s.139(1); Rule 4", basis, agm_date + timedelta(days=15),
                "only if an auditor is appointed or re-appointed at this AGM")
        row("DIR-3 KYC (each DIN holder)", "Directors Rules, Rule 12A", "DIN as on 31 March", date(y, 9, 30),
            "DIN deactivated on 1 Oct; ₹5,000 to reactivate")
        row("DPT-3 return of deposits / exempted deposits", "Rule 16, Deposits Rules", "FY end", date(y, 6, 30), "")
        row("MSME-1 (Apr–Sep half)", "s.405 order", "dues to MSMEs >45 days", date(y - 1, 10, 31), "nil return not required if no such dues")
        row("MSME-1 (Oct–Mar half)", "s.405 order", "dues to MSMEs >45 days", date(y, 4, 30), "")
        notes.append("MGT-14 within 30 days of any specified resolution (s.117); CSR-2 and BEN-2 only if applicable")
        if first_fy:
            notes.append(f"first financial year (incorporated {incorporated}); incorporation-year clocks (INC-20A, first auditor) are in company-incorporation-india")

    # tax / GST pointers — reminders, not computed law
    row("ITR (audit cases; non-audit 31 July)", "Income-tax Act 2025 — verify dates", "FY end", date(y, 10, 31), "pointer", verify=True)
    row("GSTR-9 / 9C annual return", "CGST Act s.44 — verify", "FY end", date(y, 12, 31), "pointer; if registered", verify=True)
    for d, label in ((date(y - 1, 6, 15), "Q1"), (date(y - 1, 9, 15), "Q2"), (date(y - 1, 12, 15), "Q3"), (date(y, 3, 15), "Q4")):
        row(f"Advance tax {label}", "Income-tax — verify", "FY", d, "pointer", verify=True)

    rows.sort(key=lambda r: r["deadline"])
    upcoming = [r for r in rows if today <= r["deadline"] <= today + timedelta(days=window)]
    overdue = [r for r in rows if r["deadline"] < today and not r["verify"]]
    notes.append("every date is 'unless extended by MCA circular'; verify forms and fees on mca.gov.in")
    return {"entity": entity, "fy_end": fy_end, "first_fy": first_fy, "today": today, "requirements": requirements,
            "rows": rows, "upcoming": upcoming, "overdue": overdue, "notes": notes}


def render(r: dict) -> str:
    out = [f"Compliance calendar — {r['entity']} — FY ending {r['fy_end']} (as of {r['today']})" + (" — FIRST financial year" if r["first_fy"] else ""), "",
           "Requirements:"] + [f"- {q}" for q in r["requirements"]] + ["",
           "| Form | Rule | Trigger | Due | Status | Note |", "|---|---|---|---|---|---|"]
    for x in r["rows"]:
        parts = [x["note"]] if x["note"] else []
        if x["verify"]:
            parts.append("(verify)")
        if "additional_fee_to_date" in x:
            parts.append(f"additional fee to date ≈ ₹{x['additional_fee_to_date']:,} (fee, not penalty)")
        note = "; ".join(parts)
        out.append(f"| {x['form']} | {x['rule']} | {x['trigger']} | {x['deadline'].isoformat()} | {x['status']} | {note} |")
    out += ["", f"Next {len(r['upcoming'])} item(s) in the window:"] + [f"- {x['deadline']}: {x['form']}" for x in r["upcoming"]]
    if r["overdue"]:
        out += ["", "Overdue:"] + [f"- {x['form']} ({x['status']})" for x in r["overdue"]]
    out += ["", "Notes:"] + [f"- {n}" for n in r["notes"]]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fy-end", required=True)
    ap.add_argument("--entity", required=True, choices=ENTITIES)
    ap.add_argument("--agm")
    ap.add_argument("--incorporated")
    ap.add_argument("--today")
    ap.add_argument("--window", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = compute(parse(a.fy_end), a.entity, parse(a.today) or date.today(), parse(a.agm), parse(a.incorporated), a.window)
    if a.json:
        print(json.dumps(r, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
