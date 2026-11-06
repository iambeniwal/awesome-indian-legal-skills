# IPC ↔ BNS / CrPC ↔ BNSS / IEA ↔ BSA Section Mapper

Converts section numbers between India's repealed criminal codes and the three laws in force since 1 July 2024, and answers the question practitioners actually hit: *which code governs this matter?* — based on the date of the offence and the date proceedings began. It also audits FIRs, charge sheets and drafts for mixed old/new numbering.

For advocates, police-facing users, students and anyone reading a post-July-2024 FIR.

## Install

```bash
claude plugin install ipc-bns-section-mapper@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- The section(s) and the Act you think they belong to
- For "which code applies": date of the alleged act, date the FIR/complaint was registered, current stage
- Optionally, the document to audit

## What you get

- Old → new (or new → old) table with subject and caveat (merged, renumbered, punishment changed, omitted)
- A governing-code decision for the offence, procedure and evidence axes, with the rule relied on and any unsettled points flagged
- A section-by-section audit of a document with mismatches highlighted
- India Code links to verify

## Lookup tool

```bash
python3 scripts/map_section.py IPC 420 CrPC 438 IEA 65B
```

```bash
python3 scripts/map_section.py --search "breach of trust"
```

The table ([references/mapping.csv](references/mapping.csv)) covers the ~150 most-cited provisions, cross-checked against the NCRB *Sankalan* corresponding-section table (via the open nyaya-model statute database). A miss means "not in the table", never "no equivalent".

## Example prompts

- "what is 420 ipc in bns"
- "Client was assaulted in March 2024, FIR registered last week. Does IPC or BNS apply, and which bail section do I cite?"
- "Here's the FIR — it cites 'section 173 BNS' and '506 IPC'. Check the sections."

## Law covered

- Bharatiya Nyaya Sanhita, 2023 (s.358 repeal); Bharatiya Nagarik Suraksha Sanhita, 2023 (s.531 repeal and savings); Bharatiya Sakshya Adhiniyam, 2023 (s.170)
- Article 20(1), Constitution of India; s.6 General Clauses Act, 1897
- Transition rules and worked examples in [references/transition-rules.md](references/transition-rules.md)

## Limits

- A correspondence table is not the section text. The skill always sends you to India Code to confirm ingredients and punishment.
- High Courts have differed on some transition edge cases; the skill flags them rather than picking a side.
- State amendments to the IPC/CrPC (and their BNS/BNSS successors) are not in the table.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice.
