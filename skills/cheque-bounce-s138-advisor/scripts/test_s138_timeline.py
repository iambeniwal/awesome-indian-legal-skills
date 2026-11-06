#!/usr/bin/env python3
"""Self-test for s138_timeline.py — run: python3 test_s138_timeline.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s138_timeline import add_months, compute  # noqa: E402


def row(result, step):
    return next(r for r in result["rows"] if r["step"] == step)


def test_month_clamp():
    assert add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)
    assert add_months(date(2024, 1, 31), 1) == date(2024, 2, 29)
    assert add_months(date(2026, 11, 30), 3) == date(2027, 2, 28)


def test_full_chain():
    r = compute(date(2026, 7, 1), date(2026, 8, 20), date(2026, 9, 5), date(2026, 9, 9), today=date(2026, 11, 6))
    assert row(r, "Presentment within validity")["deadline"] == date(2026, 10, 1)
    assert row(r, "Written demand notice")["deadline"] == date(2026, 9, 19)
    assert row(r, "Written demand notice")["status"] == "in time"
    assert row(r, "15-day payment window")["deadline"] == date(2026, 9, 24)
    assert row(r, "Cause of action arises")["deadline"] == date(2026, 9, 25)
    assert row(r, "Complaint under s.142(1)(b)")["deadline"] == date(2026, 10, 25)
    assert row(r, "Complaint under s.142(1)(b)")["status"] == "EXPIRED"
    assert any("beyond limitation" in n for n in r["notes"])


def test_late_notice_flagged():
    r = compute(date(2026, 7, 1), date(2026, 8, 1), date(2026, 9, 10), date(2026, 9, 12), today=date(2026, 9, 15))
    assert row(r, "Written demand notice")["status"].startswith("LATE")


def test_window_open_blocks_filing():
    r = compute(date(2026, 7, 1), date(2026, 8, 1), date(2026, 8, 10), date(2026, 8, 12), today=date(2026, 8, 20))
    assert "do NOT file" in row(r, "15-day payment window")["status"]


def test_no_service_date():
    r = compute(date(2026, 7, 1), date(2026, 8, 1), date(2026, 8, 10), None, today=date(2026, 8, 20))
    assert row(r, "Complaint under s.142(1)(b)")["deadline"] is None
    assert any("service date" in n for n in r["notes"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
