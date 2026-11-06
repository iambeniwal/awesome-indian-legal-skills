#!/usr/bin/env python3
"""Self-test for map_section.py and mapping.csv — run: python3 test_map_section.py"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from map_section import CSV, load, lookup  # noqa: E402

ROWS = load()


def test_csv_shape():
    with CSV.open(encoding="utf-8", newline="") as f:
        header = next(csv.reader(f))
    assert header == ["old_act", "old_section", "new_act", "new_section", "subject", "note"]
    for r in ROWS:
        assert r["old_act"] in {"IPC", "CrPC", "IEA", "new"}, r
        assert r["new_act"] in {"BNS", "BNSS", "BSA"}, r
        assert r["subject"], r
    assert len(ROWS) >= 150


def test_well_known_mappings():
    assert lookup(ROWS, "IPC", "420")[0]["new_section"] == "318(4)"
    assert lookup(ROWS, "IPC", "302")[0]["new_section"] == "103(1)"
    assert lookup(ROWS, "IPC", "498A")[0]["new_section"] == "85"
    assert lookup(ROWS, "CrPC", "438")[0]["new_section"] == "482"
    assert lookup(ROWS, "CrPC", "482")[0]["new_section"] == "528"
    assert lookup(ROWS, "CrPC", "154")[0]["new_section"] == "173"
    assert lookup(ROWS, "IEA", "65B")[0]["new_section"] == "63"


def test_reverse_lookup_matches_subsections():
    hits = lookup(ROWS, "BNS", "318")
    assert {h["old_section"] for h in hits} == {"415", "417", "420"}
    assert lookup(ROWS, "BNSS", "173")[0]["old_section"] == "154"


def test_omitted_sections_say_so():
    assert lookup(ROWS, "IPC", "377")[0]["new_section"] == "—"
    assert lookup(ROWS, "IPC", "309")[0]["new_section"] == "—"


def test_unknown_is_empty_not_error():
    assert lookup(ROWS, "IPC", "999") == []


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
