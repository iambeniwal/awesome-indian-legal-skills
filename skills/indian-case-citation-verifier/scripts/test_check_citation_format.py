#!/usr/bin/env python3
"""Self-test for check_citation_format.py — run: python3 test_check_citation_format.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citation_format import extract  # noqa: E402


def one(text, kind):
    hits = [r for r in extract(text) if r["kind"] == kind]
    assert hits, f"no {kind} found in {text!r}"
    return hits[0]


def test_good_forms_pass():
    for text, kind in [
        ("Rakesh Ranjan Shrivastava v. State of Jharkhand, 2024 INSC 205", "INSC"),
        ("see 2024:DHC:1234-DB and 2024:BHC-AS:12345", "HC-neutral"),
        ("Rangappa v. Sri Mohan, (2010) 11 SCC 441", "SCC"),
        ("AIR 2019 SC 1234", "AIR"),
        ("2020 SCC OnLine SC 889", "SCC OnLine"),
        ("[1973] Supp SCR 1", "SCR"),
    ]:
        r = one(text, kind)
        assert r["form_ok"], (text, r["flags"])


def test_impossible_scc_year():
    r = one("(2031) 5 SCC 100", "SCC")
    assert not r["form_ok"] and any("outside" in f for f in r["flags"])


def test_air_without_page():
    r = one("as held in AIR 2019 SC, the court", "AIR")
    assert not r["form_ok"] and "missing page" in r["flags"]


def test_pre_2023_insc_flagged_not_failed():
    r = one("1973 INSC 258", "INSC")
    assert r["form_ok"] and any("back-filled" in f for f in r["flags"])


def test_implausible_insc_serial():
    r = one("2022 INSC 4500", "INSC")
    assert not r["form_ok"]


def test_unknown_hc_code_is_soft_flag():
    r = one("2024:XYZHC:12", "HC-neutral")
    assert r["form_ok"] and any("not in table" in f for f in r["flags"])


def test_repealed_act_flag():
    r = one("charged under section 420 IPC and s.438 CrPC", "statute")
    assert any("repealed" in f for f in r["flags"])
    bns = one("punishable under s.318(4) BNS", "statute")
    assert bns["form_ok"] and not bns["flags"]


def test_supra_without_earlier_citation():
    r = one("Reliance is placed on Rangappa (supra).", "supra")
    assert any("no earlier full citation" in f for f in r["flags"])
    text = "Rangappa v. Sri Mohan, (2010) 11 SCC 441 held so. Rangappa (supra) applies."
    assert one(text, "supra")["flags"] == []


def test_no_duplicates_across_patterns():
    res = extract("Rangappa v. Sri Mohan, (2010) 11 SCC 441 : 2010 INSC 345")
    assert [r["kind"] for r in res] == ["SCC", "INSC"]


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"ok — {len(tests)} tests passed")
