#!/usr/bin/env python3
"""Self-test for limitation_calc.py — run: python3 test_limitation_calc.py"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from limitation_calc import COVID_END, COVID_FLOOR, COVID_START, add_months, compute, naive_end, parse_period  # noqa: E402

TODAY = date(2026, 11, 6)


def test_month_clamp_and_compound_periods():
    assert add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)
    assert add_months(date(2024, 1, 31), 1) == date(2024, 2, 29)
    assert naive_end(date(2026, 1, 15), parse_period("3m+30d")) == date(2026, 5, 15)   # 15 Apr + 30 days
    assert naive_end(date(2026, 1, 1), parse_period("90d")) == date(2026, 4, 1)
    assert naive_end(date(2023, 2, 28), parse_period("3y")) == date(2026, 2, 28)


def test_no_exclusion_plain_three_years():
    r = compute(date(2024, 3, 10), "3y", TODAY)
    assert r["last_date"] == date(2027, 3, 10)
    assert r["excluded_days"] == 0
    assert r["status"] == "124 day(s) left"   # 6 Nov 2026 → 10 Mar 2027


def test_covid_window_is_716_days_inclusive():
    assert (COVID_END - COVID_START).days + 1 == 716


def test_covid_full_overlap_adds_716_days():
    # 2019-06-01 + 3y = 2022-06-01 naive; whole window lies inside → +716 days = 2024-05-17
    r = compute(date(2019, 6, 1), "3y", TODAY, covid=True)
    assert r["naive_end"] == date(2022, 6, 1)
    assert r["excluded_days"] == 716
    assert r["last_date"] == date(2024, 5, 17)
    assert not r["covid_floor_applied"]


def test_covid_partial_overlap():
    # starts inside the window: 2021-01-01 + 1y = 2022-01-01 naive. Days 2021-01-02..2022-02-28 skipped (423),
    # counting resumes 2022-03-01 and runs 365 days → 2023-02-28; naive end was inside window, floor is lower.
    r = compute(date(2021, 1, 1), "1y", TODAY, covid=True)
    assert r["naive_end"] == date(2022, 1, 1)
    assert r["last_date"] == date(2023, 2, 28)
    assert not r["covid_floor_applied"]


def test_covid_ninety_day_floor():
    # 30-day period from 2020-03-01: naive end 2020-03-31 inside window; 14 days consumed before window,
    # 16 after → 2022-03-16, which is below the floor → 2022-05-30
    r = compute(date(2020, 3, 1), "30d", TODAY, covid=True)
    assert r["naive_end"] == date(2020, 3, 31)
    assert r["covid_floor_applied"]
    assert r["last_date"] == COVID_FLOOR == date(2022, 5, 30)


def test_covid_no_overlap_adds_nothing():
    r = compute(date(2023, 1, 1), "1y", TODAY, covid=True)
    assert r["last_date"] == date(2024, 1, 1)
    assert any("nothing added" in n for n in r["notes"])


def test_s14_exclusion_counts_both_ends():
    r = compute(date(2024, 1, 1), "90d", TODAY, s14=[(date(2024, 2, 1), date(2024, 2, 10))])
    assert r["excluded_days"] == 10
    assert r["last_date"] == date(2024, 4, 10)   # 1 Apr + 10 days


def test_s18_acknowledgment_resets_start():
    r = compute(date(2022, 4, 1), "3y", TODAY, ack=date(2024, 3, 10))
    assert r["start"] == date(2024, 3, 10)
    assert r["original_start"] == date(2022, 4, 1)
    assert r["last_date"] == date(2027, 3, 10)


def test_s18_after_expiry_is_refused():
    try:
        compute(date(2020, 1, 1), "1y", TODAY, ack=date(2022, 1, 1))
    except SystemExit as e:
        assert "revive" in str(e)
    else:
        raise AssertionError("post-expiry acknowledgment should be refused")


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
