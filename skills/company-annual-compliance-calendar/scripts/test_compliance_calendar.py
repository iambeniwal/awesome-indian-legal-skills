#!/usr/bin/env python3
"""Self-test — run: python3 test_compliance_calendar.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compliance_calendar import compute, is_first_fy  # noqa: E402


def row(r, prefix):
    return next(x for x in r["rows"] if x["form"].startswith(prefix))


def test_normal_year_private():
    r = compute(date(2026, 3, 31), "private", today=date(2026, 11, 6))
    assert not r["first_fy"]
    assert row(r, "AGM")["deadline"] == date(2026, 9, 30)
    assert row(r, "AOC-4")["deadline"] == date(2026, 10, 30)
    assert row(r, "AOC-4")["status"].startswith("OVERDUE by 7")
    assert row(r, "AOC-4")["additional_fee_to_date"] == 700
    assert row(r, "MGT-7 annual")["deadline"] == date(2026, 11, 29)
    assert row(r, "ADT-1")["deadline"] == date(2026, 10, 15)
    assert row(r, "DIR-3 KYC")["deadline"] == date(2026, 9, 30)
    assert row(r, "DPT-3")["deadline"] == date(2026, 6, 30)
    assert row(r, "MSME-1 (Apr")["deadline"] == date(2025, 10, 31)
    assert row(r, "MSME-1 (Oct")["deadline"] == date(2026, 4, 30)
    assert any(x["form"].startswith("MGT-7") for x in r["upcoming"])


def test_agm_date_shifts_filings():
    r = compute(date(2026, 3, 31), "private", today=date(2026, 9, 1), agm=date(2026, 8, 20))
    assert row(r, "AOC-4")["deadline"] == date(2026, 9, 19)
    assert row(r, "MGT-7 annual")["deadline"] == date(2026, 10, 19)


def test_first_year_company():
    assert is_first_fy(date(2027, 3, 31), date(2026, 1, 15))
    assert not is_first_fy(date(2027, 3, 31), date(2025, 6, 1))
    r = compute(date(2027, 3, 31), "private", today=date(2027, 4, 1), incorporated=date(2026, 1, 15))
    assert r["first_fy"]
    assert row(r, "AGM")["deadline"] == date(2027, 12, 31)
    assert row(r, "AOC-4")["deadline"] == date(2028, 1, 30)
    assert row(r, "MGT-7 annual")["deadline"] == date(2028, 2, 29)


def test_opc_no_agm():
    r = compute(date(2026, 3, 31), "opc", today=date(2026, 5, 1))
    assert all(x["form"] != "AGM" for x in r["rows"])
    assert row(r, "AOC-4")["deadline"] == date(2026, 9, 27)
    assert row(r, "MGT-7A")["deadline"] == date(2026, 11, 29)
    assert any("no AGM" in n for n in r["notes"])


def test_small_company_files_mgt7a():
    r = compute(date(2026, 3, 31), "small", today=date(2026, 5, 1))
    assert row(r, "MGT-7A")["deadline"] == date(2026, 11, 29)
    assert any("at least 2" in q for q in r["requirements"])


def test_llp():
    r = compute(date(2026, 3, 31), "llp", today=date(2026, 5, 1))
    assert row(r, "Form 11")["deadline"] == date(2026, 5, 30)
    assert row(r, "Form 8")["deadline"] == date(2026, 10, 30)
    assert all(x["form"] != "AGM" for x in r["rows"])
    assert all("additional_fee_to_date" not in x for x in r["rows"])


def test_pointers_flagged_verify_and_not_overdue_list():
    r = compute(date(2026, 3, 31), "private", today=date(2026, 11, 6))
    assert row(r, "ITR")["verify"] is True
    assert all(not x["verify"] for x in r["overdue"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
