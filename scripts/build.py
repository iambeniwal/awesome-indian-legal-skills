#!/usr/bin/env python3
"""Generate the README index and .claude-plugin/marketplace.json from skill frontmatter.

Usage:
  python3 scripts/build.py          # rewrite README index + marketplace.json
  python3 scripts/build.py --check  # exit 1 if either file is stale (used in CI)

Each skills/<name>/SKILL.md frontmatter is the single source of truth. Standard
library only, except PyYAML when available (falls back to a small parser that
handles the fields this repo uses).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

REPO = "iambeniwal/awesome-indian-legal-skills"
OWNER = {"name": "Rahul Beniwal", "url": f"https://github.com/{REPO.split('/')[0]}"}

# Display order of the index. A skill's metadata.category must be one of these.
CATEGORIES = [
    "Intake & Triage",
    "Criminal Law",
    "Civil Procedure & Limitation",
    "Consumer Protection",
    "Real Estate & RERA",
    "Public Law & RTI",
    "Data Protection & Technology",
    "Corporate & Commercial",
    "Banking, Finance & Insolvency",
    "Tax & GST",
    "Employment & Labour",
    "Family Law",
    "Intellectual Property",
    "Legal Drafting",
    "Legal Research & Citations",
    "Legal Education",
    "Skill Authoring",
]

# Every skill here is Indian-law, so the flag marks jurisdiction. Language is shown
# only when a skill is written in (or handles) something other than English.
FLAG = "🇮🇳"
LANG_NAMES = {"hi": "हिन्दी", "mr": "मराठी", "ta": "தமிழ்", "te": "తెలుగు", "kn": "ಕನ್ನಡ", "bn": "বাংলা",
              "gu": "ગુજરાતી", "ml": "മലയാളം", "pa": "ਪੰਜਾਬੀ", "ur": "اردو"}
DESC_LIMIT = 240


# --------------------------------------------------------------------------- frontmatter
def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("no YAML frontmatter")
    return m.group(1), m.group(2)


def parse_yaml(src: str) -> dict:
    try:
        import yaml  # type: ignore

        return yaml.safe_load(src) or {}
    except ImportError:
        return _mini_yaml(src)


def _mini_yaml(src: str) -> dict:
    """Enough YAML for this repo: scalars, one level of nesting, > and | block scalars, [a, b] lists."""
    out: dict = {}
    stack: list[tuple[int, dict]] = [(-1, out)]
    lines = src.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        indent = len(line) - len(line.lstrip())
        key, _, value = line.strip().partition(":")
        value = value.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value in (">", "|", ">-", "|-"):
            block = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > indent):
                block.append(lines[i].strip())
                i += 1
            joiner = " " if value.startswith(">") else "\n"
            parent[key] = joiner.join(b for b in block if b).strip()
            continue
        if value == "":
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        elif value.startswith("[") and value.endswith("]"):
            parent[key] = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
        else:
            parent[key] = value.strip("'\"")
        i += 1
    return out


def load_skills() -> list[dict]:
    skills = []
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        fm_src, _ = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        fm = parse_yaml(fm_src)
        meta = fm.get("metadata") or {}
        skills.append(
            {
                "dir": skill_md.parent.name,
                "name": fm.get("name", skill_md.parent.name),
                "description": " ".join(str(fm.get("description", "")).split()),
                "license": fm.get("license", meta.get("license", "MIT")),
                "author": meta.get("author", ""),
                "author_url": meta.get("author_url", ""),
                "version": str(meta.get("version", "")),
                "category": meta.get("category", "Uncategorised"),
                "language": meta.get("language", "en"),
            }
        )
    return skills


# --------------------------------------------------------------------------- README index
def truncate(text: str, limit: int = DESC_LIMIT) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:") + "..."


def lang_tag(language) -> str:
    """' · हिन्दी' for a non-English skill, '' for English-only."""
    langs = language if isinstance(language, list) else [language]
    extra = [LANG_NAMES.get(str(l).lower(), str(l)) for l in langs if str(l).lower() != "en"]
    return f" · {', '.join(extra)}" if extra else ""


def anchor(category: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")


def render_index(skills: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {}
    for s in skills:
        by_cat.setdefault(s["category"], []).append(s)
    unknown = [c for c in by_cat if c not in CATEGORIES]
    if unknown:
        sys.exit(f"build.py: unknown categories {unknown}; add them to CATEGORIES or fix the skill frontmatter")

    out = ["# Table of Contents", ""]
    for cat in CATEGORIES:
        if cat in by_cat:
            out.append(f"- [{cat}](#{anchor(cat)})")
    out.append("")
    for cat in CATEGORIES:
        if cat not in by_cat:
            continue
        out += [f"## {cat}", ""]
        for s in sorted(by_cat[cat], key=lambda s: s["name"]):
            out.append(f"- {FLAG} [{s['name']}](<skills/{s['dir']}>){lang_tag(s['language'])} - {truncate(s['description'])}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_readme(current: str, skills: list[dict]) -> str:
    index = render_index(skills)
    new = re.sub(
        r"<!-- INDEX_START -->.*?<!-- INDEX_END -->",
        lambda _: f"<!-- INDEX_START -->\n{index}<!-- INDEX_END -->",
        current,
        flags=re.S,
    )
    new = re.sub(r"badge/Skills-\d+-orange", f"badge/Skills-{len(skills)}-orange", new)
    return new


# --------------------------------------------------------------------------- marketplace
def render_marketplace(skills: list[dict]) -> str:
    plugins = [
        {
            "name": "indian-legal-skills",
            "source": "./",
            "description": f"All {len(skills)} Indian-law skills from Awesome Indian Legal Skills in one plugin.",
            "version": max((s["version"] for s in skills), default="0.1.0"),
            "author": OWNER,
            "license": "MIT",
            "skills": ["./skills/"],
            "strict": False,
        }
    ]
    for s in sorted(skills, key=lambda s: s["name"]):
        author = {"name": s["author"]}
        if s["author_url"]:
            author["url"] = s["author_url"]
        plugins.append(
            {
                "name": s["name"],
                "source": "./",
                "description": s["description"],
                "version": s["version"],
                "author": author,
                "license": s["license"],
                "category": s["category"],
                "skills": [f"./skills/{s['dir']}"],
                "strict": False,
            }
        )
    doc = {
        "name": "awesome-indian-legal-skills",
        "version": "1.0.0",
        "description": "Curated agent skills for Indian law",
        "owner": OWNER,
        "plugins": plugins,
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


# --------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = ap.parse_args()

    skills = load_skills()
    readme_new = render_readme(README.read_text(encoding="utf-8"), skills)
    market_new = render_marketplace(skills)
    market_old = MARKETPLACE.read_text(encoding="utf-8") if MARKETPLACE.exists() else ""

    stale = []
    if readme_new != README.read_text(encoding="utf-8"):
        stale.append(str(README.relative_to(ROOT)))
    if market_new != market_old:
        stale.append(str(MARKETPLACE.relative_to(ROOT)))

    if args.check:
        if stale:
            print("stale generated files: " + ", ".join(stale) + " — run python3 scripts/build.py")
            return 1
        print(f"index and marketplace up to date ({len(skills)} skills)")
        return 0

    README.write_text(readme_new, encoding="utf-8")
    MARKETPLACE.parent.mkdir(exist_ok=True)
    MARKETPLACE.write_text(market_new, encoding="utf-8")
    print(f"wrote index + marketplace for {len(skills)} skills" + (f" (updated: {', '.join(stale)})" if stale else " (no changes)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
