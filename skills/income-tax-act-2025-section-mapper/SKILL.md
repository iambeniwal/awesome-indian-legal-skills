---
name: income-tax-act-2025-section-mapper
description: >
  Maps sections between the repealed Income-tax Act, 1961 and the Income-tax Act, 2025 (in force
  1 April 2026, 536 sections, "tax year" instead of previous/assessment year, TDS consolidated into
  ss.392–393, TCS in s.394, Chapter VI-A deductions renumbered 122–154), and decides which Act governs
  a return, notice, assessment or appeal from the tax year or assessment year involved. Use whenever
  a user quotes an income-tax section and needs the new or old equivalent, asks "what is 80C in the
  new Act", "new section for 87A / 115BAC / 139 / 194C / 234B", "80C ka naya section", "does the
  1961 Act still apply to my AY 2025-26 notice", needs a tax notice, computation, Form 16 or opinion
  checked for mixed old/new numbering, or asks which form replaced Form 16 / 26AS. Not a tax
  computation or advisory skill — it maps provisions and tells the agent where to verify.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Tax & GST
  jurisdiction: IN
  states: all
  language: en
---

# Income-tax Act 1961 ↔ 2025 Section Mapper

Converts section and form numbers between the 1961 Act and the 2025 Act, and decides which Act governs a given year or proceeding. The tax twin of `ipc-bns-section-mapper`. For chartered accountants, tax advocates, in-house tax teams, students and anyone reading a notice or a Form 130 after 1 April 2026.

> **Not legal advice.** This is a research aid under Indian law. A section correspondence is a starting point; the 2025 provision can differ in text, conditions, thresholds or rate from the 1961 provision it replaces. A qualified chartered accountant or advocate must review every interpretation before it is relied on or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian direct tax only — the Income-tax Act is a Central Act applying across India. If the question is about GST (route to `gst-notice-reply-drafter`), State taxes, or a foreign tax code, say so and stop. International-tax questions (DTAA, transfer pricing) are in scope only for the section mapping, not the substantive analysis.

## Verify before relying

Numbering is where published tables disagree, so:

- The only official concordance is the Income Tax Department's **utility to check provisions of the Income-tax Act, 1961 vis-à-vis the Income-tax Act, 2025** on [incometaxindia.gov.in](https://www.incometaxindia.gov.in/) (a browser tool; it may refuse automated fetches — tell the user to open it). Read the **new section's text** on the department site or [India Code](https://www.indiacode.gov.in/) before saying what it provides.
- Rules and forms: the Income-tax Rules, 2026 and the department's **form-mapping guide**; commencement and amendments on [e-Gazette](https://egazette.gov.in/).
- Transition: **s.536** of the 2025 Act (repeal and savings) and the **CBDT FAQs on s.536**; summarised in [references/transition-rules.md](references/transition-rules.md).
- Every row of the bundled table carries a provenance grade in its note column — "2-source agreement" (two independent published concordances agree), "single source (verify)", or "(verify — sources diverge …)". Treat anything not graded 2-source as a lead.

If no browsing tool is available, say the table is from the skill's version date and must be checked against the department's utility.

## Required inputs

- The section(s) and which Act the user means (1961 or 2025). For a bare "section 80C", assume 1961 and show the 2025 equivalent; for a bare number that exists in both (e.g. "section 10"), show both directions.
- For the governing-Act question: the **financial year / tax year of the income**, the **date of the notice or proceeding**, and the stage (return, processing, scrutiny, reassessment, appeal, penalty, prosecution).
- Optional: the document to audit (notice, computation, Form 16/130, opinion, TDS statement).

## Method

1. **Look sections up with the bundled script**, never from memory:
   ```bash
   python3 scripts/map_section.py 1961 80C              # → 2025 equivalent
   python3 scripts/map_section.py 2025 393              # reverse; lists every 194-series row that fell into s.393
   python3 scripts/map_section.py --search "capital gain"
   ```
   It reads [references/mapping.csv](references/mapping.csv) (~170 of the most-used provisions). A miss means "not in the table" — go to the department utility; do not guess a number. Print the provenance note with every row.

2. **Present each mapping with its caveat.** Old → new, subject, provenance. Where several 1961 sections collapsed into one 2025 section (the whole 194-series → s.393 table; 80C/80CCC/80CCE → s.123 read with Schedule XV; 80TTA/80TTB → s.153; 44AD/44ADA/44AE → s.58), say so and point to the serial/sub-section. Where a 1961 provision is reported as **not carried forward** (s.271(1)(c), s.271AAC) or **restructured** (ss.11–12 trusts), say that rather than inventing a target.

3. **Decide the governing Act** by the year, using [references/transition-rules.md](references/transition-rules.md): income up to FY 2025-26 (AY 2026-27 and earlier) and every proceeding pending on 1 April 2026 or started later for such a year → **1961 Act**; tax year 2026-27 onwards, TDS on payments from 1 April 2026, advance tax from June 2026 → **2025 Act**. Rates come from the annual Finance Act either way.

4. **Audit a document for mixed numbering.** List every section and form cited, classify each as 1961 or 2025, and flag mismatches: a 2026 scrutiny notice for AY 2024-25 citing s.270 of the 2025 Act; a Form 130 described as "Form 16"; a computation for FY 2025-26 claiming "s.123". Mis-numbering is usually curable but it tells you which Act the drafter was thinking in.

5. **Flag substantive change, not just renumbering**, only when relevant to the section asked: exemptions moved into Schedules (s.11 read with Schedules II–VII), the single "tax year", fees replacing some penalties (s.428), the under-reporting penalty (s.439) in place of concealment, consolidated TDS serials. Tell the user to read the new text for thresholds and rates — the table does not carry them.

## Output

```
# Section map — [sections asked]
## Mapping table (old → new, subject, provenance) — from scripts/map_section.py
## Which Act governs (if a year or date was given): year, event, stage → 1961 / 2025, with the s.536 rule relied on
## Watch-outs (merged provisions, restructured chapters, not carried forward, diverging sources)
## Document audit (if a document was given): item-by-item table with flags
## Verify: department utility + India Code links; date checked
```

For a single-section question, collapse to one table and two lines.

## Guardrails

- Never invent a correspondence. If the table and the department utility do not give one, say "not mapped here" and explain.
- Never apply 2025 Act section numbers to AY 2026-27 or earlier years, or to proceedings saved by s.536; never apply 1961 numbers to tax year 2026-27 onwards.
- Say "corresponds to", not "is the same as"; the text may differ.
- Keep sections and forms distinct — "Form 16" now means something else under the 2026 Rules.
- Do not state rates, thresholds or limits from the table; it has none. Read the text.
- Do not reproduce long statutory text; cite and summarise.

## References

- [references/mapping.csv](references/mapping.csv) — old ↔ new table with subject and provenance notes. Compiled 6 November 2026 from published concordances with two-source agreement where available; the department utility could not be read by automated fetch, so no row is marked "official" — upgrade rows as you verify them.
- [references/transition-rules.md](references/transition-rules.md) — s.536 savings, the governing-Act table, renumbered forms, worked examples and traps. Read it whenever the governing-Act question comes up.
- [scripts/map_section.py](scripts/map_section.py) — lookup tool; `--json` for structured output.
