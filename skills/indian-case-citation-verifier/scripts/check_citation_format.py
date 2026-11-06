#!/usr/bin/env python3
"""Extract Indian legal citations from text and check their FORM. Offline, standard library only.

Usage:
  python3 check_citation_format.py draft.md
  python3 check_citation_format.py --json draft.md
  printf '%s' "$TEXT" | python3 check_citation_format.py -

It finds Supreme Court neutral citations (YYYY INSC NNN), High Court neutral citations
(YYYY:CODE:NNNN[-DB]), SCC, SCR, AIR, SCALE, JT, SCC OnLine, MANU citations, '(supra)' back-references
and statute section references, and flags forms that are malformed or impossible.

A clean form check is NOT proof that a case exists. Existence, holding and quotations can only be
verified by opening an official copy (sci.gov.in / eSCR, the High Court portal, judgments.ecourts.gov.in,
India Code). The URL column is a search hint, not a link to the judgment.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

THIS_YEAR = _dt.date.today().year
MAX_YEAR = THIS_YEAR + 1
INSC_START = 2023          # neutral citations issued from 2023; earlier numbers were back-filled on eSCR
INSC_RETRO_FLOOR = 1950
INSC_MAX_PER_YEAR = 2500   # SC output is ~1,000–1,300 judgments a year; above this is implausible
SCC_START = 1969
SCC_MAX_VOL = 20
AIR_START = 1914

HC_CODES = {
    "DHC": "Delhi", "BHC": "Bombay", "KER": "Kerala", "MHC": "Madras", "AHC": "Allahabad", "KHC": "Karnataka",
    "PHHC": "Punjab & Haryana", "GUJHC": "Gujarat", "MPHC": "Madhya Pradesh", "RJ": "Rajasthan", "CHC": "Calcutta",
    "HHC": "Himachal Pradesh", "OHC": "Orissa", "PHC": "Patna", "TSHC": "Telangana", "APHC": "Andhra Pradesh",
    "JHHC": "Jharkhand", "CGHC": "Chhattisgarh", "UHC": "Uttarakhand", "GAHC": "Gauhati", "JKLHC": "J&K and Ladakh",
}
REPEALED_ACTS = {
    "IPC": "Indian Penal Code, 1860 — repealed by BNS s.358 w.e.f. 1 July 2024",
    "CRPC": "Code of Criminal Procedure, 1973 — repealed by BNSS s.531 w.e.f. 1 July 2024",
    "CR.P.C.": "Code of Criminal Procedure, 1973 — repealed by BNSS s.531 w.e.f. 1 July 2024",
    "EVIDENCE ACT": "Indian Evidence Act, 1872 — repealed by BSA s.170 w.e.f. 1 July 2024",
    "IEA": "Indian Evidence Act, 1872 — repealed by BSA s.170 w.e.f. 1 July 2024",
}

SCI_SEARCH = "https://www.sci.gov.in/judgements/  (search by neutral citation, case number or parties)"
ECOURTS_SEARCH = "https://judgments.ecourts.gov.in/  (High Court judgments search)"
INDIA_CODE = "https://www.indiacode.gov.in/  (verify the section as it stands)"

PATTERNS = [
    ("INSC", re.compile(r"\b(?P<year>\d{4})\s+INSC\s+(?P<num>\d+)\b")),
    ("HC-neutral", re.compile(r"\b(?P<year>\d{4}):(?P<code>[A-Z]{2,6}(?:-[A-Z]{2,4})?):(?P<num>\d+)(?P<suffix>-DB)?\b")),
    ("SCC OnLine", re.compile(r"\b(?P<year>\d{4})\s+SCC\s+OnLine\s+(?P<court>[A-Za-z&]+)\s+(?P<page>\d+)\b")),
    ("SCC", re.compile(r"\(\s*(?P<year>\d{4})\s*\)\s*(?:Supp\s*\(\s*(?P<supp>\d+)\s*\)\s*)?(?P<vol>\d+)?\s*SCC\s*(?:\((?P<series>Cri|Civ|L&S)\)\s*)?(?P<page>\d+)?")),
    ("SCR", re.compile(r"[\[(]\s*(?P<year>\d{4})\s*[\])]\s*(?P<vol>\d+|Supp)?\s*S\.?C\.?R\.?\s*(?P<page>\d+)?")),
    ("AIR", re.compile(r"\bAIR\s+(?P<year>\d{4})\s+(?P<court>SC|SUPREME COURT|[A-Z][a-z]+(?: [A-Z][a-z]+)?|[A-Z]{2,4})\b\s*(?P<page>\d+)?")),
    ("SCALE", re.compile(r"\b(?P<year>\d{4})\s*\(\s*(?P<vol>\d+)\s*\)\s*SCALE\s*(?P<page>\d+)?")),
    ("JT", re.compile(r"\bJT\s+(?P<year>\d{4})\s*\(\s*(?P<vol>\d+)\s*\)\s*SC\s*(?P<page>\d+)?")),
    ("MANU", re.compile(r"\bMANU/(?P<court>[A-Z]{2})/(?P<num>\d{4})/(?P<year>\d{4})\b")),
    ("statute", re.compile(r"(?i)\b(?:s\.|ss\.|section|sections|article|art\.)\s*(?P<sec>\d+[A-Za-z]{0,2}(?:\(\d+\))*(?:\([a-z]\))?)(?:\s*(?:of\s+the\s+|,\s*|\s+))?(?P<act>(?:Indian\s+)?(?:Penal\s+Code|IPC|CrPC|Cr\.P\.C\.|Evidence\s+Act|IEA|BNSS|BNS|BSA|Constitution|[A-Z][A-Za-z()]*(?:\s+[A-Z()][A-Za-z()]*)*\s+Act,?\s*\d{4}))?")),
    ("supra", re.compile(r"(?P<name>[A-Z][A-Za-z.&' ]{2,60}?)\s*\(supra\)")),
]


def plausible_year(y: int, start: int) -> bool:
    return start <= y <= MAX_YEAR


def check(kind: str, m: re.Match, text: str, seen_names: list[str]) -> dict:
    g = m.groupdict()
    flags: list[str] = []
    url = ""
    year = int(g["year"]) if g.get("year") else None

    if kind == "INSC":
        num = int(g["num"])
        url = SCI_SEARCH
        if year is None or not plausible_year(year, INSC_RETRO_FLOOR):
            flags.append("impossible year")
        elif year < INSC_START:
            flags.append("pre-2023 INSC number — back-filled on eSCR; verify it opens there")
        if num == 0 or num > INSC_MAX_PER_YEAR:
            flags.append(f"serial {num} implausible for one year")
    elif kind == "HC-neutral":
        url = ECOURTS_SEARCH
        base = g["code"].split("-")[0]
        if not plausible_year(year, 2000):
            flags.append("implausible year for a neutral citation")
        if base not in HC_CODES:
            flags.append(f"court code {g['code']} not in table — check the court's portal (not necessarily wrong)")
        if int(g["num"]) == 0:
            flags.append("serial 0")
    elif kind == "SCC":
        url = SCI_SEARCH
        if not plausible_year(year, SCC_START):
            flags.append(f"SCC year {year} outside {SCC_START}–{MAX_YEAR}")
        if not g.get("vol") and not g.get("supp"):
            flags.append("missing volume")
        elif g.get("vol") and int(g["vol"]) > SCC_MAX_VOL:
            flags.append(f"volume {g['vol']} unusually high — verify")
        if not g.get("page"):
            flags.append("missing page")
    elif kind == "SCR":
        url = SCI_SEARCH
        if not plausible_year(year, 1950):
            flags.append("implausible SCR year")
        if not g.get("page"):
            flags.append("missing page")
    elif kind == "AIR":
        url = SCI_SEARCH if g["court"].upper() in ("SC", "SUPREME COURT") else ECOURTS_SEARCH
        if not plausible_year(year, AIR_START):
            flags.append(f"AIR year {year} outside {AIR_START}–{MAX_YEAR}")
        if not g.get("page"):
            flags.append("missing page")
    elif kind in ("SCALE", "JT"):
        url = SCI_SEARCH
        if not plausible_year(year, 1969):
            flags.append("implausible year")
        if not g.get("page"):
            flags.append("missing page")
    elif kind == "SCC OnLine":
        url = SCI_SEARCH if g["court"].upper() == "SC" else ECOURTS_SEARCH
        if not plausible_year(year, 1950):
            flags.append("implausible year")
    elif kind == "MANU":
        url = SCI_SEARCH if g["court"] == "SC" else ECOURTS_SEARCH
        if not plausible_year(year, 1950):
            flags.append("implausible year")
        flags.append("database identifier — cite a neutral or reporter citation as well")
    elif kind == "statute":
        url = INDIA_CODE
        act = (g.get("act") or "").strip()
        key = re.sub(r"\s+", " ", act.upper()).replace("INDIAN PENAL CODE", "IPC").replace("PENAL CODE", "IPC")
        for rk, note in REPEALED_ACTS.items():
            if key == rk or key.endswith(" " + rk) or key == rk.replace(".", ""):
                flags.append(f"repealed Act: {note} — correct only for matters under the old codes; map via India Code")
                break
        if not act:
            flags.append("section with no Act named — say which Act")
    elif kind == "supra":
        name = g["name"].strip()
        anchor = name.split()[0]
        if not any(anchor in s for s in seen_names):
            flags.append(f"'{name} (supra)' has no earlier full citation containing '{anchor}' in this text")
        url = ""

    return {
        "kind": kind,
        "as_cited": m.group(0).strip(),
        "groups": {k: v for k, v in g.items() if v},
        "form_ok": not any(f for f in flags if not f.startswith(("pre-2023", "court code", "database"))),
        "flags": flags,
        "verify_at": url,
        "position": m.start(),
    }


def extract(text: str) -> list[dict]:
    results: list[dict] = []
    taken: list[tuple[int, int]] = []
    # case names that appear before a citation, for the (supra) check
    seen_names = re.findall(r"([A-Z][A-Za-z.&' ]{2,80}?\s+v\.?\s+[A-Z][A-Za-z.&'() ]{2,80}?)[,\s]+(?:\(?\d{4}|AIR|\[)", text)
    for kind, pat in PATTERNS:
        for m in pat.finditer(text):
            span = (m.start(), m.end())
            if any(a <= span[0] < b or a < span[1] <= b for a, b in taken):
                continue
            if kind == "statute" and not m.group("act") and not re.search(r"(?i)section|art", m.group(0)):
                continue
            res = check(kind, m, text, seen_names)
            if kind != "supra":
                taken.append(span)
            results.append(res)
    results.sort(key=lambda r: r["position"])
    return results


def render(results: list[dict]) -> str:
    if not results:
        return "no citations found"
    out = ["| # | Kind | As cited | Form | Flags | Verify at |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(results, 1):
        out.append(f"| {i} | {r['kind']} | {r['as_cited']} | {'ok' if r['form_ok'] else 'CHECK'} | {'; '.join(r['flags']) or '—'} | {r['verify_at'] or '—'} |")
    bad = sum(1 for r in results if not r["form_ok"])
    out += ["", f"{len(results)} candidate citation(s); {bad} with form problems.",
            "Form OK means the citation is shaped correctly — it does NOT confirm the case exists or says what is claimed. Open the official copy."]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="file path, or - for stdin")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.source == "-" else Path(a.source).read_text(encoding="utf-8")
    results = extract(text)
    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(render(results))
    return 1 if any(not r["form_ok"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
