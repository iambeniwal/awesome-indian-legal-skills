#!/usr/bin/env python3
"""Validate every skill under skills/. Exit 1 on any error.

Checks: folder name == frontmatter name (kebab-case), description length,
licence, category, metadata fields, SKILL.md length, required files, and that
every relative link in SKILL.md and README.md resolves.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import CATEGORIES, ROOT, SKILLS, parse_yaml, split_frontmatter  # noqa: E402

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(<?([^)>\s#]+)[^)]*\)")
MAX_LINES = 500
REQUIRED_FILES = ["SKILL.md", "README.md", "LICENSE.txt"]
DISCLAIMER_HINTS = ("not legal advice", "qualified advocate", "legal advice")
# Every skill names the forum/State it applies to, says where to verify, and lists what it must not do.
REQUIRED_HEADINGS = ("Jurisdiction gate", "Verify before relying", "Guardrails")
REGISTRY = ROOT / "sources" / "official-sources.json"
URL_RE = re.compile(r"https?://([A-Za-z0-9.-]+)")
GOV_SUFFIXES = (".gov.in", ".nic.in", ".gov")


def load_registry() -> tuple[set[str], dict[str, str]]:
    """Registered hosts, and deprecated host -> replacement."""
    if not REGISTRY.exists():
        return set(), {}
    import json

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    hosts = {h.lower() for s in data.get("sources", []) for h in s.get("hosts", [])}
    deprecated = {d["host"].lower(): d["use"] for d in data.get("deprecated", [])}
    return hosts, deprecated


def check_hosts(folder: Path, hosts: set[str], deprecated: dict[str, str]) -> tuple[list[str], list[str]]:
    """Government hosts a skill cites must be in the registry; deprecated ones are errors, unknown ones warnings."""
    errs, warns = [], []
    seen: set[str] = set()
    for p in list(folder.rglob("*.md")) + list(folder.rglob("*.py")) + list(folder.rglob("*.csv")):
        for host in URL_RE.findall(p.read_text(encoding="utf-8", errors="ignore")):
            host = host.lower().rstrip(".")
            if host in seen:
                continue
            seen.add(host)
            if host in deprecated:
                errs.append(f"{p.relative_to(ROOT)}: deprecated host {host} — use {deprecated[host]}")
            elif host.endswith(GOV_SUFFIXES) and host not in hosts:
                warns.append(f"{p.relative_to(ROOT)}: government host {host} not in sources/official-sources.json — add it (with access notes) or fix the URL")
    return errs, warns


def check_skill(folder: Path) -> list[str]:
    errs: list[str] = []
    rel = folder.relative_to(ROOT)
    for f in REQUIRED_FILES:
        if not (folder / f).exists():
            errs.append(f"{rel}: missing {f}")
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return errs

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm_src, body = split_frontmatter(text)
        fm = parse_yaml(fm_src)
    except ValueError as e:
        return errs + [f"{rel}/SKILL.md: {e}"]

    name = fm.get("name")
    if name != folder.name:
        errs.append(f"{rel}: frontmatter name {name!r} != folder name {folder.name!r}")
    if not name or not NAME_RE.match(str(name)):
        errs.append(f"{rel}: name must be lowercase-with-hyphens")
    if len(str(name or "")) > 64:
        errs.append(f"{rel}: name longer than 64 characters")

    desc = " ".join(str(fm.get("description", "")).split())
    if len(desc) < 80:
        errs.append(f"{rel}: description too short ({len(desc)} chars) — say what it does AND when to use it")
    if len(desc) > 1024:
        errs.append(f"{rel}: description over 1024 characters ({len(desc)})")

    if not fm.get("license"):
        errs.append(f"{rel}: frontmatter needs license:")

    meta = fm.get("metadata") or {}
    for key in ("author", "version", "category"):
        if not meta.get(key):
            errs.append(f"{rel}: metadata.{key} missing")
    if meta.get("category") and meta["category"] not in CATEGORIES:
        errs.append(f"{rel}: category {meta['category']!r} not in CATEGORIES (scripts/build.py)")
    if str(meta.get("jurisdiction", "IN")).upper() != "IN":
        errs.append(f"{rel}: jurisdiction must be IN for this list")

    n_lines = text.count("\n") + 1
    if n_lines > MAX_LINES:
        errs.append(f"{rel}/SKILL.md: {n_lines} lines (> {MAX_LINES}); move material to references/")

    if not any(h in body.lower() for h in DISCLAIMER_HINTS):
        errs.append(f"{rel}/SKILL.md: no 'not legal advice' disclaimer in the body")
    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^## {re.escape(heading)}\b", body, re.M):
            errs.append(f"{rel}/SKILL.md: missing '## {heading}' section (see templates/skill-template)")

    for doc in ("SKILL.md", "README.md"):
        p = folder / doc
        if not p.exists():
            continue
        for target in LINK_RE.findall(p.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / target).exists():
                errs.append(f"{rel}/{doc}: broken relative link {target}")

    for script in folder.glob("scripts/*.py"):
        src = script.read_text(encoding="utf-8")
        if re.search(r"\b(requests|urllib|http\.client|socket|subprocess)\b", src):
            errs.append(f"{script.relative_to(ROOT)}: scripts must be offline, standard-library helpers (found network/subprocess import)")
    return errs


def main() -> int:
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not folders:
        print("no skills found under skills/")
        return 0
    errors: list[str] = []
    warnings: list[str] = []
    hosts, deprecated = load_registry()
    for folder in folders:
        errors += check_skill(folder)
        e, w = check_hosts(folder, hosts, deprecated)
        errors += e
        warnings += w
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(folders)} skills checked, {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
