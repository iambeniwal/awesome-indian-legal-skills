#!/usr/bin/env python3
"""Labour dues calculator under India's Labour Codes (in force 21 Nov 2025). Standard library, offline.

Subcommands
  wages         --gross G --basic-da-ra W          apply the s.2(y) 50% rule and return "wages"
  gratuity      --wage W --years Y [--months M] [--fixed-term] [--cap 2000000]
  retrenchment  --wage W --years Y [--months M] [--notice-months 1]
  leave         --wage W --days D [--divisor 26]
  bonus         --wage W --percent P [--ceiling 21000] [--base 7000] [--min-wage 0]
Add --json to any subcommand for machine-readable output.

Conventions (verify against the Code, the Central/State Rules and the latest notifications):
  wages      : basic + DA + retaining allowance; excluded allowances capped at 50% of total remuneration,
               excess added back (Code on Wages s.2(y)). So wages = max(basic+DA+RA, 50% of gross).
  gratuity   : 15/26 x monthly wages x completed years; six months or more counts as a full year; five-year
               qualifying service (fixed-term: pro-rata after one year, CSS Code s.53); capped at the notified
               ceiling (default 20,00,000 carried from the Payment of Gratuity Act regime - verify).
  retrenchment: one month's notice pay (or notice) + 15 days' average pay per completed year or part > 6 months
               (IR Code s.70, mirroring ID Act s.25F). 15 days' pay = monthly wages x 15/26 here (verify convention).
  leave      : monthly wages / divisor (26 by convention) x days of leave due.
  bonus      : eligible if wages <= ceiling (notified; 21,000 per the Aug 2026 notification - verify); computed on
               min(wages, max(base, min_wage)) x 12 x percent, percent between 8.33 and 20.
Facts before 21 Nov 2025 are governed by the repealed Acts; this tool does not switch regimes.
"""
from __future__ import annotations

import argparse
import json
import sys

FIFTEEN_BY_26 = 15 / 26


def wages_rule(gross: float, basic_da_ra: float) -> dict:
    if basic_da_ra > gross:
        sys.exit("basic+DA+RA cannot exceed gross")
    excluded = gross - basic_da_ra
    cap = 0.5 * gross
    add_back = max(0.0, excluded - cap)
    wages = basic_da_ra + add_back
    return {
        "gross": gross, "basic_da_ra": basic_da_ra, "excluded_allowances": excluded,
        "cap_50pct": cap, "add_back": add_back, "wages": wages,
        "note": "wages = max(basic+DA+RA, 50% of gross) per Code on Wages s.2(y)",
    }


def completed_years(years: int, months: int, round_half_up: bool = True) -> int:
    return years + (1 if (round_half_up and months >= 6) else 0)


def gratuity(wage: float, years: int, months: int = 0, fixed_term: bool = False, cap: float = 2_000_000) -> dict:
    total_months = years * 12 + months
    if fixed_term:
        eligible = total_months >= 12
        service_years = total_months / 12  # pro-rata
        basis = "fixed-term: pro-rata after one year (CSS Code s.53)"
    else:
        eligible = years >= 5 or total_months >= 60
        service_years = completed_years(years, months)
        basis = "15/26 x wages x completed years (6+ months rounds up); five-year qualifying service"
    raw = FIFTEEN_BY_26 * wage * service_years if eligible else 0.0
    amount = min(raw, cap) if eligible else 0.0
    return {
        "wage": wage, "years": years, "months": months, "fixed_term": fixed_term,
        "eligible": eligible, "service_years_used": service_years, "uncapped": round(raw, 2),
        "cap": cap, "amount": round(amount, 2), "basis": basis,
        "note": "qualifying service is waived on death or disablement; cap is the notified ceiling - verify",
    }


def retrenchment(wage: float, years: int, months: int = 0, notice_months: int = 1) -> dict:
    svc = completed_years(years, months)
    comp = FIFTEEN_BY_26 * wage * svc
    notice = wage * notice_months
    return {
        "wage": wage, "years": years, "months": months, "completed_years_used": svc,
        "compensation_15_days_per_year": round(comp, 2), "notice_pay": round(notice, 2),
        "total": round(comp + notice, 2),
        "basis": "IR Code s.70 (ID Act s.25F): notice/pay in lieu + 15 days' average pay per completed year or part > 6 months",
        "note": "continuous service of one year required; Chapter X permission may apply where the threshold is crossed",
    }


def leave_encashment(wage: float, days: float, divisor: int = 26) -> dict:
    daily = wage / divisor
    return {"wage": wage, "days": days, "divisor": divisor, "daily_wage": round(daily, 2),
            "amount": round(daily * days, 2), "note": "divisor is a convention - verify the State rule"}


def bonus(wage: float, percent: float, ceiling: float = 21_000, base: float = 7_000, min_wage: float = 0.0) -> dict:
    if not 8.33 <= percent <= 20:
        sys.exit("bonus percent must be between 8.33 and 20")
    eligible = wage <= ceiling
    calc_base = min(wage, max(base, min_wage))
    amount = calc_base * 12 * percent / 100 if eligible else 0.0
    return {"wage": wage, "ceiling": ceiling, "eligible": eligible, "calculation_base_monthly": calc_base,
            "percent": percent, "annual_bonus": round(amount, 2),
            "note": "eligibility ceiling and base per the latest notification under the Code on Wages - verify; 30 working days' minimum service"}


def render(title: str, d: dict) -> str:
    out = [f"{title}", "", "| Item | Value |", "|---|---|"]
    for k, v in d.items():
        out.append(f"| {k.replace('_', ' ')} | {v} |")
    out.append("")
    out.append("Verify the Code section, the Central/State Rules and the notified ceilings before relying on this.")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("wages"); w.add_argument("--gross", type=float, required=True); w.add_argument("--basic-da-ra", type=float, required=True)
    g = sub.add_parser("gratuity"); g.add_argument("--wage", type=float, required=True); g.add_argument("--years", type=int, required=True)
    g.add_argument("--months", type=int, default=0); g.add_argument("--fixed-term", action="store_true"); g.add_argument("--cap", type=float, default=2_000_000)
    r = sub.add_parser("retrenchment"); r.add_argument("--wage", type=float, required=True); r.add_argument("--years", type=int, required=True)
    r.add_argument("--months", type=int, default=0); r.add_argument("--notice-months", type=int, default=1)
    l = sub.add_parser("leave"); l.add_argument("--wage", type=float, required=True); l.add_argument("--days", type=float, required=True); l.add_argument("--divisor", type=int, default=26)
    b = sub.add_parser("bonus"); b.add_argument("--wage", type=float, required=True); b.add_argument("--percent", type=float, required=True)
    b.add_argument("--ceiling", type=float, default=21_000); b.add_argument("--base", type=float, default=7_000); b.add_argument("--min-wage", type=float, default=0.0)
    a = ap.parse_args()

    if a.cmd == "wages":
        res = wages_rule(a.gross, a.basic_da_ra)
    elif a.cmd == "gratuity":
        res = gratuity(a.wage, a.years, a.months, a.fixed_term, a.cap)
    elif a.cmd == "retrenchment":
        res = retrenchment(a.wage, a.years, a.months, a.notice_months)
    elif a.cmd == "leave":
        res = leave_encashment(a.wage, a.days, a.divisor)
    else:
        res = bonus(a.wage, a.percent, a.ceiling, a.base, a.min_wage)

    print(json.dumps(res, indent=2) if a.json else render(a.cmd, res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
