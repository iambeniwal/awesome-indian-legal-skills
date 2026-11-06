#!/usr/bin/env python3
"""Self-test for map_section.py and mapping.csv — run: python3 test_map_section.py"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from map_section import CSV, base, load, lookup  # noqa: E402

ROWS = load()


def test_csv_shape():
    with CSV.open(encoding="utf-8", newline="") as f:
        header = next(csv.reader(f))
    assert header == ["old_act", "old_section", "new_act", "new_section", "subject", "note"]
    for r in ROWS:
        assert r["old_act"] == "ITA1961" and r["new_act"] == "ITA2025", r
        assert r["subject"] and r["note"], r  # every row carries a provenance note
    assert len(ROWS) >= 150


def test_well_known_mappings():
    assert lookup(ROWS, "ITA1961", "80C")[0]["new_section"].startswith("123")
    assert lookup(ROWS, "ITA1961", "87A")[0]["new_section"] == "156"
    assert lookup(ROWS, "ITA1961", "115BAC")[0]["new_section"] == "202"
    assert lookup(ROWS, "ITA1961", "139")[0]["new_section"] == "263"
    assert lookup(ROWS, "ITA1961", "44AB")[0]["new_section"] == "63"
    assert lookup(ROWS, "ITA1961", "192")[0]["new_section"] == "392"
    assert lookup(ROWS, "ITA1961", "206C")[0]["new_section"] == "394"
    assert lookup(ROWS, "ITA1961", "234B")[0]["new_section"] == "424"


def test_exact_before_base():
    exact = lookup(ROWS, "ITA1961", "139(4)")
    assert len(exact) == 1 and exact[0]["new_section"] == "263(4)"
    # an exact row wins over the family; the family is reached only when no exact row exists
    assert [r["old_section"] for r in lookup(ROWS, "ITA1961", "10")] == ["10"]
    assert lookup(ROWS, "ITA1961", "10(13A)")[0]["new_section"].startswith("11")
    fam = lookup(ROWS, "ITA1961", "80CCD(9)")  # no such sub-section → falls back to the 80CCD family
    assert fam and all(r["old_section"].startswith("80CCD") for r in fam)


def test_reverse_lookup_matches_subsections():
    hits = lookup(ROWS, "ITA2025", "393")
    olds = {h["old_section"] for h in hits}
    assert {"194C", "194J", "195", "194N"} <= olds
    assert lookup(ROWS, "ITA2025", "156")[0]["old_section"] == "87A"


def test_base_handles_letter_and_hyphen_sections():
    assert base("80CCD(1B)") == "80CCD"
    assert base("80-IAC") == "80-IAC"
    assert base("393(1) table serial 6(i)") == "393"


def test_divergent_rows_are_flagged():
    for sec in ("32", "35", "10(10D)"):
        r = lookup(ROWS, "ITA1961", sec)[0]
        assert "verify" in r["note"], sec


def test_unknown_is_empty_not_error():
    assert lookup(ROWS, "ITA1961", "999Z") == []


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
