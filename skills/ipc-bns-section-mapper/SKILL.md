---
name: ipc-bns-section-mapper
description: >
  Maps sections between India's old and new criminal codes — IPC 1860 ↔ Bharatiya Nyaya Sanhita
  2023, CrPC 1973 ↔ Bharatiya Nagarik Suraksha Sanhita 2023, Indian Evidence Act 1872 ↔ Bharatiya
  Sakshya Adhiniyam 2023 — and tells you which code governs a given matter based on the date of the
  offence and the date proceedings began (the 1 July 2024 transition and the BNSS s.531 savings
  clause). Use whenever a user quotes an IPC/CrPC/Evidence Act section and needs the BNS/BNSS/BSA
  equivalent or vice versa, asks "what is 420 IPC in BNS", "new section for 498A", "302 ka naya
  section", "is this FIR under IPC or BNS", "which code applies to an offence from 2023", or needs
  an FIR, charge sheet, bail application or legal notice checked for mixed old/new section numbers.
  Not a substitute for reading the section text — it tells the agent where to verify.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Criminal Law
  jurisdiction: IN
  states: all
  language: en
---

# IPC ↔ BNS / CrPC ↔ BNSS / IEA ↔ BSA Section Mapper

Converts section numbers between the repealed codes and the three new criminal laws in force since **1 July 2024**, and decides which code governs a matter. For advocates, police-facing users, students and anyone reading an FIR or charge sheet written after the switch.

> **Not legal advice.** This is a research aid under Indian law. Section correspondence is a starting point; the text, ingredients and punishment of the new provision can differ from the old one. A qualified advocate must review every interpretation before it is relied on or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian criminal law only. The three new codes are Central Acts applying across India (with Jammu & Kashmir and Ladakh covered since 2019); State amendments to the IPC/CrPC and their BNS/BNSS successors are not in the table, so name the State and tell the user to check its amendments. If the question is about a foreign penal code, stop and say so.

## Verify before relying

Numbering is the easiest thing to get wrong and the easiest thing to check. Before quoting any mapping as settled:

- Read the **new section's text** on [India Code](https://www.indiacode.nic.in/) — BNS (Act 45 of 2023), BNSS (Act 46 of 2023), BSA (Act 47 of 2023). Confirm the ingredients match the old provision; many BNS sections merge several IPC sections into sub-sections, so "IPC 420 → BNS 318(4)" means the *punishment* sub-section, while the definition sits in 318(1).
- Commencement notifications (S.O. 850(E), 851(E), 852(E) of 23 February 2024) and any later amendment: [e-Gazette](https://egazette.gov.in/).
- For the governing-code question, read **BNSS s.531** (repeal and savings), **BNS s.358** and **BSA s.170**, and check the latest Supreme Court / your High Court position — High Courts have differed on edge cases in the first year.

If no browsing tool is available, say the table is from the skill's version date and the user must verify on India Code.

## Required inputs

- The section(s) and which Act the user thinks they are from (IPC/CrPC/IEA or BNS/BNSS/BSA). If the user gives a bare number ("section 420"), ask which code, or show both possibilities.
- For the governing-code question: **date of the alleged offence**, **date the FIR/complaint was registered**, and the current stage (investigation, charge sheet, trial, appeal).
- Optional: the document to check (FIR, charge sheet, bail application, notice) for mixed numbering.

## Method

1. **Look the sections up with the bundled script** rather than from memory:
   ```bash
   python3 scripts/map_section.py IPC 420          # → BNS equivalent
   python3 scripts/map_section.py BNS 318          # → IPC equivalent(s)
   python3 scripts/map_section.py CrPC 438 IEA 65B # several at once
   ```
   It reads [references/mapping.csv](references/mapping.csv) (the most-cited ~150 provisions). If a section is not in the table, say so and go to India Code — do not guess a number. Newer BNS offences with no IPC ancestor (organised crime s.111, petty organised crime s.112, terrorist act s.113, mob lynching s.103(2), snatching s.304, hit-and-run s.106(2), sexual intercourse by deceitful means s.69, acts endangering sovereignty s.152) are listed with "new" in the old-section column.

2. **Present each mapping with its caveat.** Show old → new, the subject, and the note from the table (merged, renumbered as a sub-section, punishment changed, omitted). Where the old section is **omitted** (IPC 309 attempt to suicide, 377 unnatural offences, 497 adultery, 124A sedition in its old form), say so and name the nearest provision or the reason (struck down, decriminalised, replaced).

3. **Decide the governing code** when dates are given, using these rules and flagging that they are being applied:
   - **Substantive offence** (which code defines the crime and punishment): the law in force **on the date of the act** — Article 20(1) of the Constitution bars conviction under a law not in force at the time or a heavier penalty. Offence before 1 July 2024 → IPC; on or after → BNS. A continuing offence straddling the date needs the acts after 1 July to be charged under BNS and earlier acts under IPC.
   - **Procedure** (investigation, bail, trial, appeal): BNSS s.531(2)(a) saves only proceedings **pending** on 1 July 2024 — those continue under the CrPC. Anything instituted on or after 1 July 2024 proceeds under the BNSS **even if the offence is under the IPC**. So an FIR registered in August 2024 for a 2023 assault is "u/s 323 IPC" investigated under the BNSS; the bail application cites BNSS s.480/483, not CrPC s.437/439.
   - **Evidence**: the BSA applies to proceedings instituted on or after 1 July 2024; pending ones continue under the IEA (BSA s.170). Electronic records now go under BSA s.63 with the certificate in the Schedule (replacing IEA s.65B).
   - Where High Courts have taken different views on an edge case (for example whether an appeal filed after 1 July against a conviction in a CrPC trial follows CrPC or BNSS), say the point is unsettled and recommend checking the user's High Court.

4. **Audit documents for mixed numbering.** When given an FIR, charge sheet or draft, list every section cited, classify each as IPC/BNS/CrPC/BNSS/IEA/BSA, and flag mismatches: BNS offences with CrPC procedure citations, IPC sections cited for post-July conduct, or the common error of citing BNS numbers that are actually CrPC/BNSS numbers (e.g. "s.173 BNS" when s.173 BNSS — FIR — is meant). Wrong numbering is usually curable (BNSS s.514-type errors do not vitiate a trial absent prejudice), but it affects bail arguments, cognizability and punishment, so point it out.

5. **Note the substantive changes that matter in practice**, only when relevant to the user's section: community service as a punishment (BNS s.4(f)) for petty offences; higher minimums in some sexual-offence and organised-crime provisions; defamation retained (s.356); the gender-neutral framing of some provisions; timelines in the BNSS (FIR within 3 days of e-complaint s.173, charge sheet s.193, judgment within 45 days of conclusion of arguments s.258, mandatory videography of searches s.105); zero FIR and e-FIR (s.173); handcuffing conditions (s.43(3)); undertrial release at one-third of the maximum sentence for first-time offenders (s.479).

## Output

```
# Section map — [sections asked]
## Mapping table (old → new, subject, caveat) — from scripts/map_section.py
## Which code governs (if dates given): offence date, institution date, stage → IPC/BNS, CrPC/BNSS, IEA/BSA, with the rule relied on
## Watch-outs (omitted sections, merged sub-sections, punishment changes, unsettled points)
## Document audit (if a document was given): section-by-section table with flags
## Verify: India Code links for each new section; date checked
```

For a single-section question, collapse this to one table and two or three lines.

## Guardrails

- Never invent a correspondence. If the table and India Code do not give one, say "no direct equivalent" and explain.
- Do not describe the new section as "the same" — say "corresponds to" and point to what changed.
- Do not apply the BNS to conduct before 1 July 2024, and do not apply a heavier BNS punishment retrospectively; flag Article 20(1) if a draft does this.
- Keep the IPC/BNS (offence) and CrPC/BNSS (procedure) axes distinct in every answer — users mix them up constantly, and so do drafts.
- Do not reproduce long statutory text; cite and summarise.

## References

- [references/mapping.csv](references/mapping.csv) — old ↔ new table with subject and note columns. The script reads it; load it directly only when you need to browse by subject. Provenance: compiled from the Acts and cross-checked (6 Nov 2026) against the NCRB *Sankalan* "Corresponding Section Table" as parsed in the open [nyaya-model](https://github.com/JitendraJha98/nyaya-model) statute database; the eight rows where that parse disagreed were resolved from the BNS/BNSS section titles and found to be continuation-row shifts in the parse, not errors in this table. Still verify on India Code before citing.
- [references/transition-rules.md](references/transition-rules.md) — the savings clauses, the date rules, worked examples and the points on which courts have differed. Read it whenever the governing-code question comes up.
