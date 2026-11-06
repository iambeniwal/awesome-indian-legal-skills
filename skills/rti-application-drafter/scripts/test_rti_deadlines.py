#!/usr/bin/env python3
"""Self-test for rti_deadlines.py — run: python3 test_rti_deadlines.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rti_deadlines import compute  # noqa: E402


def row(result, step_prefix):
    return next(r for r in result["rows"] if r["step"].startswith(step_prefix))


def base(**kw):
    args = dict(applied=date(2026, 9, 1), route="direct", third_party=False, life_liberty=False, fee_gap_days=0,
                reply=None, first_appeal=None, faa_decision=None, today=date(2026, 9, 10))
    args.update(kw)
    return compute(**args)


def test_plain_30_days():
    r = base()
    assert row(r, "PIO reply due")["deadline"] == date(2026, 10, 1)
    assert row(r, "First appeal due")["deadline"] == date(2026, 10, 31)


def test_apio_and_third_party():
    assert row(base(route="apio"), "PIO reply due")["deadline"] == date(2026, 10, 6)
    assert row(base(third_party=True), "PIO reply due")["deadline"] == date(2026, 10, 11)
    assert row(base(life_liberty=True), "PIO reply due")["deadline"] == date(2026, 9, 3)


def test_deemed_refusal_note():
    r = base(today=date(2026, 10, 5))
    assert any("deemed refusal" in n for n in r["notes"])
    assert row(r, "PIO reply due")["status"] == "EXPIRED"


def test_first_appeal_runs_from_reply_when_received():
    r = base(reply=date(2026, 9, 20))
    assert row(r, "First appeal due")["deadline"] == date(2026, 10, 20)


def test_second_appeal_chain():
    r = base(reply=date(2026, 9, 20), first_appeal=date(2026, 10, 10), faa_decision=date(2026, 11, 2), today=date(2026, 11, 6))
    assert row(r, "FAA decision due")["deadline"] == date(2026, 11, 24)
    assert row(r, "Second appeal due")["deadline"] == date(2027, 1, 31)


def test_second_appeal_from_due_date_when_faa_silent():
    r = base(first_appeal=date(2026, 10, 10), today=date(2026, 12, 1))
    assert row(r, "Second appeal due")["deadline"] == date(2027, 2, 22)
    assert any("FAA has not decided" in n for n in r["notes"])


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
