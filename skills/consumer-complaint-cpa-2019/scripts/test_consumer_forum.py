#!/usr/bin/env python3
"""Self-test for consumer_forum.py — run: python3 test_consumer_forum.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from consumer_forum import compute, forum, inr  # noqa: E402


def test_forum_boundaries():
    assert forum(5_000_000)["forum"] == "District Commission"
    assert forum(5_000_001)["forum"] == "State Commission"
    assert forum(20_000_000)["forum"] == "State Commission"
    assert forum(20_000_001)["forum"] == "National Commission"


def test_fee_note():
    assert forum(500_000)["fee"].startswith("nil")
    assert "Schedule" in forum(500_001)["fee"]


def test_limitation():
    r = compute(1_250_000, date(2025, 3, 10), today=date(2026, 11, 6))
    assert r["limitation_deadline"] == date(2027, 3, 10)
    assert "day(s) left" in r["limitation_status"]
    r = compute(1_250_000, date(2024, 3, 10), today=date(2026, 11, 6))
    assert r["limitation_status"].startswith("EXPIRED")


def test_leap_day():
    assert compute(1, date(2024, 2, 29), today=date(2024, 3, 1))["limitation_deadline"] == date(2026, 2, 28)


def test_inr_format():
    assert inr(50_000_000) == "₹5 crore"
    assert inr(1_250_000) == "₹12.5 lakh"
    assert inr(75_000) == "₹75,000"


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
