#!/usr/bin/env python3
"""Self-test — run: python3 test_incorporation_deadlines.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from incorporation_deadlines import add_months, compute, first_fy_end_company, first_fy_end_llp  # noqa: E402


def row(r, step):
    return next(x for x in r["rows"] if x["step"] == step)


def test_company_clocks():
    r = compute(date(2026, 11, 6), "company", today=date(2026, 11, 20))
    assert row(r, "First board meeting")["deadline"] == date(2026, 12, 6)
    assert row(r, "ADT-1 for first auditor")["deadline"] == date(2026, 12, 21)
    assert row(r, "Share certificates to subscribers")["deadline"] == date(2027, 1, 6)
    assert row(r, "INC-20A declaration of commencement")["deadline"] == date(2027, 5, 5)
    assert row(r, "First financial year ends")["deadline"] == date(2027, 3, 31)
    assert row(r, "First AGM")["deadline"] == date(2027, 12, 31)


def test_first_fy_rule():
    assert first_fy_end_company(date(2026, 1, 15)) == date(2027, 3, 31)   # on/after 1 Jan → following year
    assert first_fy_end_company(date(2026, 6, 1)) == date(2027, 3, 31)
    assert first_fy_end_llp(date(2026, 11, 6)) == date(2028, 3, 31)       # after 30 Sept → year after next
    assert first_fy_end_llp(date(2026, 6, 1)) == date(2027, 3, 31)


def test_opc_has_no_agm():
    r = compute(date(2026, 5, 1), "opc", today=date(2026, 5, 2))
    assert all(x["step"] != "First AGM" for x in r["rows"])
    assert any("OPC: no AGM" in n for n in r["notes"])


def test_llp_form3_and_annual():
    r = compute(date(2026, 11, 6), "llp", today=date(2026, 11, 20))
    assert row(r, "LLP Agreement — Form 3")["deadline"] == date(2026, 12, 6)
    assert row(r, "Form 11 annual return")["deadline"] == date(2028, 5, 30)
    assert row(r, "Form 8 statement of account & solvency")["deadline"] == date(2028, 10, 30)


def test_overdue_and_subscription_warning():
    r = compute(date(2026, 1, 1), "company", today=date(2026, 8, 1), subscription=date(2026, 7, 15))
    assert row(r, "INC-20A declaration of commencement")["status"].startswith("OVERDUE")
    assert any("AFTER the INC-20A deadline" in n for n in r["notes"])
    assert add_months(date(2026, 12, 31), 2) == date(2027, 2, 28)


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
