#!/usr/bin/env python3
"""Look up Income-tax Act 1961 ↔ Income-tax Act 2025 section correspondences from references/mapping.csv.

Usage:
  python3 map_section.py 1961 80C
  python3 map_section.py 2025 393               # reverse lookup; matches 393, 393(1), 393(2)...
  python3 map_section.py 1961 "10(13A)" 1961 194C
  python3 map_section.py --search depreciation
  python3 map_section.py --json 1961 87A

Act names accepted: 1961 / ITA1961 / old; 2025 / ITA2025 / new.
Offline, standard library only. A miss means "not in the table" — check the official CBDT utility or
the Act on India Code; it never means "no equivalent" unless the row's new_section is "—".
Every row carries a provenance note (2-source agreement / single source / diverge) — print it.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "references" / "mapping.csv"
ALIASES = {"1961": "ITA1961", "ita1961": "ITA1961", "old": "ITA1961", "it1961": "ITA1961",
           "2025": "ITA2025", "ita2025": "ITA2025", "new": "ITA2025", "it2025": "ITA2025"}


def load() -> list[dict]:
    with CSV.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def base(section: str) -> str:
    """'80CCD(1B)' -> '80CCD'; '393(1) table' -> '393'; '80-IAC' -> '80-IAC'; '10(13A)' -> '10'."""
    m = re.match(r"\s*([0-9]+-?[A-Za-z]*)", section)
    return m.group(1).upper() if m else section.strip().upper()


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s).upper()


def lookup(rows: list[dict], act: str, section: str) -> list[dict]:
    want = norm(section)
    col_act, col_sec = ("old_act", "old_section") if act == "ITA1961" else ("new_act", "new_section")
    exact = [r for r in rows if r[col_act] == act and norm(r[col_sec]) == want]
    if exact:
        return exact
    # fall back to base-section match: "10" finds 10(10), 10(13A)...; "393" finds 393(1) table, 393(2)
    return [r for r in rows if r[col_act] == act and base(r[col_sec]) == base(want)]


def fmt(r: dict) -> str:
    line = f"ITA 1961 s.{r['old_section']} → ITA 2025 s.{r['new_section']}  —  {r['subject']}"
    if r["note"]:
        line += f"  [{r['note']}]"
    return line


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="*", help="ACT SECTION pairs, e.g. 1961 80C 2025 393")
    ap.add_argument("--search", help="search the subject column")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = load()

    results: list[dict] = []
    if a.search:
        q = a.search.lower()
        results = [{"query": a.search, "hits": [r for r in rows if q in r["subject"].lower() or q in r["note"].lower()]}]
    else:
        if len(a.pairs) % 2:
            sys.exit("give ACT SECTION pairs, e.g. 1961 80C")
        for act_raw, sec in zip(a.pairs[::2], a.pairs[1::2]):
            act = ALIASES.get(act_raw.lower())
            if act is None:
                sys.exit(f"unknown act {act_raw!r}; use 1961 or 2025")
            results.append({"query": f"{act} {sec}", "hits": lookup(rows, act, sec)})

    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0
    missing = 0
    for res in results:
        print(f"## {res['query']}")
        if not res["hits"]:
            missing += 1
            print("  not in table — check the CBDT utility on incometaxindia.gov.in or the Act on India Code (not a finding of 'no equivalent')")
        for r in res["hits"]:
            print("  " + fmt(r))
        print()
    print(f"table: {CSV.name}; rows are graded by provenance in the note column — verify every number before citing.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
