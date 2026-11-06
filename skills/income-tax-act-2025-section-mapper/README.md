# Income-tax Act 1961 ↔ 2025 Section Mapper

The Income-tax Act, 2025 replaced the 1961 Act on 1 April 2026: 536 sections instead of 800-odd, one "tax year" instead of previous year + assessment year, the whole 194-series of TDS collapsed into a table in s.393, Chapter VI-A deductions renumbered 122–154, exemptions moved into Schedules, and every form renumbered (Form 16 → Form 130, Form 26AS → Form 168). This skill converts section and form numbers in both directions and answers the question that matters in practice: *which Act governs this year, notice or appeal?*

For chartered accountants, tax advocates, in-house tax teams and students. The direct-tax twin of `ipc-bns-section-mapper`.

## Install

```bash
claude plugin install income-tax-act-2025-section-mapper@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- The section(s) and which Act you mean
- For "which Act applies": the financial/tax year of the income, the date of the notice or proceeding, and the stage
- Optionally, the document to audit

## What you get

- Old → new (or new → old) table with subject and a **provenance grade** per row (two published concordances agree / single source / sources diverge)
- A governing-Act decision with the s.536 savings rule relied on
- A line-by-line audit of a notice, computation or form for mixed numbering
- Links to the department's official utility and India Code to verify

## Lookup tool

```bash
python3 scripts/map_section.py 1961 80C 1961 194C 2025 393
```

```bash
python3 scripts/map_section.py --search "advance tax"
```

A miss means "not in the table", never "no equivalent".

## Example prompts

- "what is section 80C in the new income tax act"
- "We got a scrutiny notice in May 2026 for AY 2024-25 citing section 270 of the 2025 Act. Is that right?"
- "Our payroll manual still says 194C and Form 16A for contractor TDS. What do those become after April 2026?"

## Law covered

- Income-tax Act, 2025 (s.536 repeal and savings; s.3 tax year; ss.392–395 TDS/TCS; ss.122–154 deductions)
- Income-tax Rules, 2026 and the CBDT form-mapping guide
- Income-tax Act, 1961 (as saved for earlier years and pending proceedings)
- Transition rules and worked examples in [references/transition-rules.md](references/transition-rules.md)

## Limits

- The table was compiled from published concordances (two-source agreement where available); the department's own utility could not be read automatically, so no row is marked official. The skill always sends you there.
- It maps provisions; it does not compute tax, rates or thresholds.
- Business-income rows (ss.28–44) are where sources disagree most and are flagged.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal or tax advice.
