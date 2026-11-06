#!/usr/bin/env python3
"""Self-test for rera_delay.py — run: python3 test_rera_delay.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rera_delay import add_months, compute, simple_interest, whole_months_between  # noqa: E402


def test_months():
    assert whole_months_between(date(2023, 6, 30), date(2026, 11, 6)) == 40
    assert whole_months_between(date(2023, 6, 30), date(2023, 6, 30)) == 0
    assert whole_months_between(date(2023, 6, 30), date(2023, 7, 29)) == 0
    assert add_months(date(2022, 12, 31), 6) == date(2023, 6, 30)


def test_simple_interest():
    assert round(simple_interest(1_000_000, 10, date(2025, 1, 1), date(2026, 1, 1)), 2) == 100_000.00
    assert simple_interest(1_000_000, 10, date(2026, 1, 1), date(2025, 1, 1)) == 0


def test_delay_mode_runs_from_due_date():
    r = compute(date(2022, 12, 31), 6, 0, 10.0, "delay", [(date(2019, 3, 10), 1_000_000)], date(2024, 6, 30))
    assert r["effective_due"] == date(2023, 6, 30)
    assert r["months_of_delay"] == 12
    assert r["rows"][0]["interest_from"] == date(2023, 6, 30)
    assert r["total_claim"] == round(1_000_000 * 0.10 * 366 / 365, 2)


def test_refund_mode_runs_from_payment_date():
    r = compute(date(2022, 12, 31), 0, 0, 10.0, "refund", [(date(2025, 1, 1), 500_000)], date(2026, 1, 1))
    assert r["rows"][0]["interest_from"] == date(2025, 1, 1)
    assert r["total_interest"] == 50_000.00
    assert r["total_claim"] == 550_000.00


def test_extension_and_no_delay_note():
    r = compute(date(2024, 1, 1), 0, 9, 10.0, "delay", [(date(2023, 1, 1), 100)], date(2024, 6, 1))
    assert r["effective_due"] == date(2024, 10, 1)
    assert r["months_of_delay"] == 0
    assert any("has not passed" in n for n in r["notes"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
