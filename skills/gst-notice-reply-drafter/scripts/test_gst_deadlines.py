#!/usr/bin/env python3
"""Self-test for gst_deadlines.py — run: python3 test_gst_deadlines.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gst_deadlines import PREDEPOSIT_CAP_CGST, add_months, compute, inr  # noqa: E402

T = date(2026, 11, 6)


def row(res, step):
    return next(r for r in res["rows"] if r["step"] == step)


def test_month_clamp():
    assert add_months(date(2026, 11, 30), 3) == date(2027, 2, 28)
    assert add_months(date(2024, 11, 30), 3) == date(2025, 2, 28)


def test_asmt10():
    r = compute("asmt10", date(2026, 10, 1), T, None, None, None, None)
    assert row(r, "ASMT-11 reply")["deadline"] == date(2026, 10, 31)


def test_s73_limitation_fy2022_23():
    r = compute("drc01", date(2026, 9, 15), T, "FY2022-23", "73", None, None)
    assert row(r, "s.73 SCN last date")["deadline"] == date(2026, 9, 30)
    assert row(r, "s.73 order last date")["deadline"] == date(2026, 12, 31)
    assert row(r, "s.73 settlement window")["deadline"] == date(2026, 10, 15)


def test_s73_extended_orders_listed():
    r = compute("drc01", date(2023, 9, 1), date(2023, 9, 2), "FY2018-19", "73", None, None)
    assert row(r, "s.73 order — extended (s.168A notifications)")["deadline"] == date(2024, 4, 30)


def test_s74a_fy2024_25():
    r = compute("drc01", date(2026, 9, 15), T, "FY2024-25", "74A", None, None)
    assert row(r, "s.74A SCN last date")["deadline"] == date(2029, 6, 30)
    assert row(r, "s.74A order last date")["deadline"] == date(2027, 9, 15)
    assert row(r, "s.74A settlement window")["deadline"] == date(2026, 11, 14)


def test_order_appeal_and_predeposit_cap():
    r = compute("order", date(2026, 8, 20), T, None, None, None, 300_00_00_000)
    assert row(r, "s.107 appeal to Appellate Authority")["deadline"] == date(2026, 11, 20)
    assert row(r, "s.107 condonable limit")["deadline"] == date(2026, 12, 20)
    assert inr(PREDEPOSIT_CAP_CGST) == "20,00,00,000"
    assert "₹20,00,00,000" in row(r, "s.107(6) pre-deposit")["status"]
    r2 = compute("order", date(2026, 8, 20), T, None, None, None, 1_20_00_000)
    assert "₹12,00,000" in row(r2, "s.107(6) pre-deposit")["status"]


def test_gstat_appeal():
    r = compute("appeal-order", date(2026, 8, 20), T, None, None, None, None)
    assert row(r, "s.112 appeal to GSTAT")["deadline"] == date(2026, 11, 20)
    assert row(r, "s.112 condonable limit")["deadline"] == date(2027, 2, 20)


def test_unknown_period_asks_for_due_date():
    r = compute("drc01", date(2026, 9, 15), T, "FY2030-31", "73", None, None)
    assert any("pass --annual-return-due" in n for n in r["notes"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
