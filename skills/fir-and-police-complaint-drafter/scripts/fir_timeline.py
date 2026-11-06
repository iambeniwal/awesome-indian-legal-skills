#!/usr/bin/env python3
"""Dates calculator for the complainant's side of a BNSS matter. Standard library only, offline.

Example:
  python3 fir_timeline.py --incident 2026-10-01 --reported 2026-10-02 --efir --refused 2026-10-02 \
      --sp-sent 2026-10-05 --today 2026-11-06

Rules applied (verify against the current BNSS text on India Code):
  e-FIR signature      : information given electronically must be signed within 3 days (s.173(1)(ii))
  preliminary enquiry  : where permitted (3–7-year offences, DSP permission), within 14 days (s.173(3))
  bank report (cyber)  : RBI zero-liability window — within 3 WORKING days of the bank's communication
                         (2017 circular; verify) — computed here as 3 days skipping Sat/Sun, no holidays
  SP route             : s.173(4) fixes NO period for the SP to act; this script uses a 15-day wait as a
                         reasonable interval before the s.175(3) application and says so
  progress report      : police to inform the informant/victim of progress within 90 days (s.193(3)(ii))
  sexual-offence cases : investigation to be completed within 2 months of recording (s.193(2))
Deadlines are "on or before"; a day falling on a holiday moves to the next working day (s.10 General Clauses Act).
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

SP_WAIT_DAYS = 15


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


def add_working_days(d: date, n: int) -> date:
    cur = d
    while n > 0:
        cur += timedelta(days=1)
        if cur.weekday() < 5:
            n -= 1
    return cur


def status(deadline: date, today: date) -> str:
    if today > deadline:
        return "passed"
    left = (deadline - today).days
    return "today" if left == 0 else f"{left} day(s) left"


def compute(incident: date, reported: date | None, efir: bool, refused: date | None, sp_sent: date | None,
            fir_registered: date | None, sexual_offence: bool, cyber: bool, today: date) -> dict:
    rows: list[dict] = []
    notes: list[str] = []
    rep = reported or incident

    if efir:
        dl = rep + timedelta(days=3)
        rows.append({"step": "Sign the e-FIR at the station", "rule": "s.173(1)(ii): within 3 days of giving information electronically",
                     "deadline": dl, "status": status(dl, today)})
    if cyber:
        dl = add_working_days(rep, 3)
        rows.append({"step": "Report to bank/wallet for zero liability", "rule": "RBI 2017 circular: within 3 working days of the bank's communication (verify)",
                     "deadline": dl, "status": status(dl, today)})
        notes.append("file on cybercrime.gov.in / call 1930 at once — the money-trail freeze works in hours, not days")

    if fir_registered is None:
        dl = rep + timedelta(days=14)
        rows.append({"step": "Preliminary enquiry (if the police invoke s.173(3))", "rule": "s.173(3): 14 days, 3–7-year offences, DSP permission",
                     "deadline": dl, "status": status(dl, today)})
        if refused:
            if sp_sent is None:
                rows.append({"step": "Representation to the SP", "rule": "s.173(4): in writing and by post; no statutory period — send now",
                             "deadline": refused, "status": "pending — send with proof of the refusal"})
                rows.append({"step": "Application to the Magistrate", "rule": "s.175(3): after the SP route, with affidavit",
                             "deadline": None, "status": "available after the SP has had a reasonable time"})
            else:
                dl = sp_sent + timedelta(days=SP_WAIT_DAYS)
                rows.append({"step": "Reasonable wait for the SP to act", "rule": f"no statutory period; script assumes {SP_WAIT_DAYS} days",
                             "deadline": dl, "status": status(dl, today)})
                rows.append({"step": "Application to the Magistrate", "rule": "s.175(3): with affidavit, annexing the complaint, refusal proof and SP dispatch proof",
                             "deadline": dl, "status": "file on or after this date" if today < dl else "can be filed now"})
                notes.append("courts dismiss s.175(3) applications that skipped the s.173(4) step or lack the affidavit (Priyanka Srivastava; Babu Venkatesh)")
        elif reported:
            notes.append("if the station neither registers nor gives a written refusal, treat silence beyond a few days as refusal and start the s.173(4) route")
    else:
        rows.append({"step": "Free copy of the FIR", "rule": "s.173(2): forthwith", "deadline": fir_registered, "status": "ask on the day"})
        dl = fir_registered + timedelta(days=90)
        rows.append({"step": "Progress of investigation to be communicated", "rule": "s.193(3)(ii): within 90 days of registration",
                     "deadline": dl, "status": status(dl, today)})
        if sexual_offence:
            dl = add_months(fir_registered, 2)
            rows.append({"step": "Investigation to be completed (listed sexual offences)", "rule": "s.193(2): two months from recording",
                         "deadline": dl, "status": status(dl, today)})
        notes.append("after the charge sheet or a closure report, the informant must be heard before closure is accepted (Bhagwant Singh)")

    return {"rows": rows, "notes": notes, "today": today}


def render(result: dict) -> str:
    out = [f"Complainant's timeline (as of {result['today']})", "",
           "| Step | Rule | Date | Status |", "|---|---|---|---|"]
    for r in result["rows"]:
        d = r["deadline"].isoformat() if r["deadline"] else "—"
        out.append(f"| {r['step']} | {r['rule']} | {d} | {r['status']} |")
    if result["notes"]:
        out += ["", "Notes:"] + [f"- {n}" for n in result["notes"]]
    out += ["", "Statutory periods are 'on or before'; the SP wait is a practice assumption, not law. Verify ss.173, 175, 193 BNSS on India Code."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--incident", required=True, help="date of the offence / discovery, YYYY-MM-DD")
    ap.add_argument("--reported", help="date information was first given to the police or portal")
    ap.add_argument("--efir", action="store_true", help="information was given electronically (needs signature within 3 days)")
    ap.add_argument("--refused", help="date the station refused / declined to register")
    ap.add_argument("--sp-sent", help="date the s.173(4) representation was posted to the SP")
    ap.add_argument("--fir-registered", help="date the FIR was registered")
    ap.add_argument("--sexual-offence", action="store_true", help="offence listed in s.193(2) (two-month investigation target)")
    ap.add_argument("--cyber", action="store_true", help="online/financial fraud (bank reporting window + NCRP)")
    ap.add_argument("--today", help="override today's date")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    today = parse(a.today) or date.today()
    result = compute(parse(a.incident), parse(a.reported), a.efir, parse(a.refused), parse(a.sp_sent),
                     parse(a.fir_registered), a.sexual_offence, a.cyber, today)
    if a.json:
        print(json.dumps(result, default=lambda o: o.isoformat() if isinstance(o, date) else str(o), indent=2))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
