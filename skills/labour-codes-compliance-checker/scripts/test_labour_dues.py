#!/usr/bin/env python3
"""Self-test for labour_dues.py — run: python3 test_labour_dues.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from labour_dues import bonus, gratuity, leave_encashment, retrenchment, wages_rule  # noqa: E402


def test_wages_rule_adds_back_excess():
    r = wages_rule(100_000, 30_000)          # allowances 70% > 50% cap → 20,000 added back
    assert r["add_back"] == 20_000 and r["wages"] == 50_000
    r = wages_rule(100_000, 60_000)          # allowances 40% → no add-back
    assert r["add_back"] == 0 and r["wages"] == 60_000


def test_gratuity_rounding_and_eligibility():
    assert gratuity(40_000, 7, 8)["service_years_used"] == 8        # 7y8m → 8 years
    assert gratuity(40_000, 7, 5)["service_years_used"] == 7        # 7y5m → 7 years
    assert round(gratuity(40_000, 7, 8)["amount"]) == round(15 / 26 * 40_000 * 8)
    assert gratuity(40_000, 4, 11)["eligible"] is False             # under five years
    assert gratuity(40_000, 4, 11)["amount"] == 0


def test_gratuity_cap():
    assert gratuity(500_000, 30)["amount"] == 2_000_000
    assert gratuity(500_000, 30, cap=2_500_000)["amount"] == 2_500_000


def test_fixed_term_pro_rata():
    g = gratuity(40_000, 1, 6, fixed_term=True)
    assert g["eligible"] and abs(g["service_years_used"] - 1.5) < 1e-9
    assert gratuity(40_000, 0, 11, fixed_term=True)["eligible"] is False


def test_retrenchment():
    r = retrenchment(40_000, 7, 8)
    assert r["completed_years_used"] == 8
    assert r["notice_pay"] == 40_000
    assert round(r["total"]) == round(15 / 26 * 40_000 * 8 + 40_000)


def test_leave_encashment():
    assert leave_encashment(26_000, 10)["amount"] == 10_000


def test_bonus():
    b = bonus(18_000, 8.33)
    assert b["eligible"] and b["calculation_base_monthly"] == 7_000
    assert round(b["annual_bonus"]) == round(7_000 * 12 * 0.0833)
    assert bonus(25_000, 8.33)["eligible"] is False
    assert bonus(6_000, 8.33)["calculation_base_monthly"] == 6_000          # wage below base
    assert bonus(18_000, 8.33, min_wage=9_000)["calculation_base_monthly"] == 9_000


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
