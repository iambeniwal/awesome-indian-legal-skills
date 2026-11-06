#!/usr/bin/env python3
"""Self-test for bail_timelines.py — run: python3 test_bail_timelines.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bail_timelines import add_months, default_bail, undertrial  # noqa: E402


def row(r, prefix):
    return next(x for x in r["rows"] if x["step"].startswith(prefix))


def test_default_60_days_counts_remand_day():
    r = default_bail(date(2026, 8, 1), "other", today=date(2026, 9, 1))
    assert row(r, "Last day")["date"] == date(2026, 9, 29)       # day 60 = 1 Aug + 59
    assert row(r, "Right to default bail")["date"] == date(2026, 9, 30)
    assert "until the right accrues" in r["status"]


def test_default_90_days_and_accrued_status():
    r = default_bail(date(2026, 1, 1), "min10", today=date(2026, 4, 15))
    assert row(r, "Last day")["date"] == date(2026, 3, 31)       # day 90
    assert row(r, "Right to default bail")["date"] == date(2026, 4, 1)
    assert r["status"].startswith("right has accrued")


def test_special_statute_outer_limit():
    r = default_bail(date(2026, 1, 1), "ndps", today=date(2026, 1, 2))
    assert row(r, "Last day")["date"] == date(2026, 6, 29)       # day 180
    assert row(r, "Outer limit")["date"] == date(2026, 12, 31)   # day 365
    assert any("extension order" in n for n in r["notes"])


def test_undertrial_half_and_third():
    r = undertrial(date(2024, 2, 10), 7, first_time=True, today=date(2026, 11, 6))
    assert row(r, "One-third")["date"] == date(2026, 6, 10)      # 28 months
    assert row(r, "One-half")["date"] == date(2027, 8, 10)       # 42 months
    assert r["status"].startswith("eligible now")
    r2 = undertrial(date(2024, 2, 10), 7, first_time=False, today=date(2026, 11, 6))
    assert "eligible from 2027-08-10" in r2["status"]


def test_month_clamp():
    assert add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)
    assert add_months(date(2024, 8, 31), 6) == date(2025, 2, 28)


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
