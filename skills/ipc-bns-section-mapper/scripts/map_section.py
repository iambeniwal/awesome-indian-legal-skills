#!/usr/bin/env python3
"""Look up old ↔ new criminal-code section correspondences from references/mapping.csv.

Usage:
  python3 map_section.py IPC 420
  python3 map_section.py BNS 318            # reverse lookup, matches 318 and 318(x)
  python3 map_section.py CrPC 438 IEA 65B   # several pairs at once
  python3 map_section.py --search cheating  # free-text search in the subject column
  python3 map_section.py --json IPC 302

Offline, standard library only. A miss means "not in the table" — check India Code; it never means
"no equivalent exists" unless the row says so.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "references" / "mapping.csv"
ALIASES = {
    "ipc": "IPC", "bns": "BNS", "crpc": "CrPC", "cr.p.c.": "CrPC", "bnss": "BNSS",
    "iea": "IEA", "evidence": "IEA", "evidenceact": "IEA", "bsa": "BSA",
}
OLD = {"IPC", "CrPC", "IEA"}


def load() -> list[dict]:
    with CSV.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def base(section: str) -> str:
    """'318(4)' -> '318'; '23(1) proviso' -> '23'."""
    m = re.match(r"\s*([0-9]+[A-Za-z]*)", section)
    return m.group(1).upper() if m else section.strip().upper()


def lookup(rows: list[dict], act: str, section: str) -> list[dict]:
    want = section.strip().upper()
    hits = []
    for r in rows:
        if act in OLD:
            if r["old_act"] == act and (r["old_section"].upper() == want or want in [s.strip().upper() for s in r["old_section"].split("/")]):
                hits.append(r)
        else:
            if r["new_act"] == act and (r["new_section"].upper() == want or base(r["new_section"]) == base(want)):
                hits.append(r)
    return hits


def fmt(r: dict) -> str:
    arrow = f"{r['old_act']} {r['old_section']} → {r['new_act']} {r['new_section']}" if r["old_act"] != "new" \
        else f"{r['new_act']} {r['new_section']} (new — no {('IPC','CrPC','IEA')[('BNS','BNSS','BSA').index(r['new_act'])]} ancestor)"
    line = f"{arrow}  —  {r['subject']}"
    if r["note"]:
        line += f"  [{r['note']}]"
    return line


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="*", help="ACT SECTION pairs, e.g. IPC 420 CrPC 438")
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
            sys.exit("give ACT SECTION pairs, e.g. IPC 420")
        for act_raw, sec in zip(a.pairs[::2], a.pairs[1::2]):
            act = ALIASES.get(act_raw.lower().replace(" ", ""), act_raw)
            if act not in OLD | {"BNS", "BNSS", "BSA"}:
                sys.exit(f"unknown act {act_raw!r}; use IPC, BNS, CrPC, BNSS, IEA or BSA")
            results.append({"query": f"{act} {sec}", "hits": lookup(rows, act, sec)})

    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0
    missing = 0
    for res in results:
        print(f"## {res['query']}")
        if not res["hits"]:
            missing += 1
            print("  not in table — verify on https://www.indiacode.gov.in/ (this is not a finding of 'no equivalent')")
        for r in res["hits"]:
            print("  " + fmt(r))
        print()
    print(f"table: {CSV.name}; verify every row against India Code before citing.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
