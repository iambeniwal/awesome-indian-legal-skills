#!/usr/bin/env python3
"""Self-test for fir_timeline.py — run: python3 test_fir_timeline.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fir_timeline import add_working_days, compute  # noqa: E402


def row(result, prefix):
    return next(r for r in result["rows"] if r["step"].startswith(prefix))


def test_efir_signature_window():
    r = compute(date(2026, 10, 1), date(2026, 10, 2), True, None, None, None, False, False, today=date(2026, 10, 3))
    assert row(r, "Sign the e-FIR")["deadline"] == date(2026, 10, 5)
    assert row(r, "Sign the e-FIR")["status"] == "2 day(s) left"


def test_preliminary_enquiry_window():
    r = compute(date(2026, 10, 1), date(2026, 10, 1), False, None, None, None, False, False, today=date(2026, 10, 20))
    assert row(r, "Preliminary enquiry")["deadline"] == date(2026, 10, 15)
    assert row(r, "Preliminary enquiry")["status"] == "passed"


def test_refusal_sequence_requires_sp_first():
    r = compute(date(2026, 10, 1), date(2026, 10, 2), False, date(2026, 10, 2), None, None, False, False, today=date(2026, 10, 10))
    assert row(r, "Representation to the SP")["status"].startswith("pending")
    assert row(r, "Application to the Magistrate")["deadline"] is None


def test_magistrate_after_sp_wait():
    r = compute(date(2026, 10, 1), date(2026, 10, 2), False, date(2026, 10, 2), date(2026, 10, 5), None, False, False, today=date(2026, 11, 6))
    assert row(r, "Application to the Magistrate")["deadline"] == date(2026, 10, 20)
    assert row(r, "Application to the Magistrate")["status"] == "can be filed now"
    assert any("affidavit" in n for n in r["notes"])


def test_registered_fir_rights():
    r = compute(date(2026, 10, 1), None, False, None, None, date(2026, 10, 3), True, False, today=date(2026, 11, 6))
    assert row(r, "Progress of investigation")["deadline"] == date(2027, 1, 1)
    assert row(r, "Investigation to be completed")["deadline"] == date(2026, 12, 3)


def test_cyber_working_days():
    assert add_working_days(date(2026, 11, 6), 3) == date(2026, 11, 11)  # Fri -> Wed
    r = compute(date(2026, 11, 6), date(2026, 11, 6), False, None, None, None, False, True, today=date(2026, 11, 6))
    assert row(r, "Report to bank")["deadline"] == date(2026, 11, 11)
    assert any("1930" in n for n in r["notes"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
