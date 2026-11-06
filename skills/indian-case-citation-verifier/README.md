# Indian Case Citation Verifier

Checks every case citation, statute reference and quotation in a draft before it goes into a filing, opinion or article. Answers five questions for each authority: does the case exist, is the citation in the right form, does it hold what is claimed, is the quotation verbatim, and is the statute section current (BNS/BNSS/BSA since 1 July 2024). Built for the AI-fabricated-citation problem Indian courts have warned advocates about — and meant to be run on an agent's own generated research before it is shown.

For advocates, law clerks, in-house counsel and students.

## Install

```bash
claude plugin install indian-case-citation-verifier@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- The draft or the list of citations (blocking)
- For quotations: the quoted words and the pinpoint
- The proposition each case is cited for, if not obvious
- Nice to have: which reporter you have access to, the court the draft is going to

## What you get

- A citation ledger: as cited → normalised → form OK? → existence (VERIFIED / UNVERIFIED / NOT FOUND, with source and date) → holding matches? → quote verbatim? → action
- Corrected citations ready to paste (neutral citation plus one reporter)
- Statute references checked for currency and the 1 July 2024 transition
- A plain "read this before filing" paragraph
- The exact official-portal searches to run for anything that could not be checked

## Form checker

```bash
python3 scripts/check_citation_format.py draft.md
```

```bash
printf '%s' "Rangappa v. Sri Mohan, (2010) 11 SCC 441; (2031) 5 SCC 100; AIR 2019 SC" | python3 scripts/check_citation_format.py -
```

Add `--json` for structured output. It validates **form only** — plausible years and volumes, page present, known court codes, INSC serial range, repealed-Act references, dangling `(supra)` — and prints where to verify each one. It cannot confirm a case exists.

## Example prompts

- "Here's my written submission for the Delhi High Court. Check every citation before I file tomorrow."
- "ChatGPT gave me these six Supreme Court cases on anticipatory bail. Which are real?"
- "Is this quote from *Arnesh Kumar* accurate, and what's the correct paragraph?"
- "Verify the citations in this article and convert them to neutral citations where available."

## Law and sources covered

- Neutral citations: Supreme Court `YYYY INSC NNN` (2023 onwards, back-filled on eSCR); High Court `YYYY:CODE:NNNN` patterns by court
- Reporters: SCC, SCR, AIR, SCALE, JT, SCC OnLine, MANU, Cri LJ — see [references/citation-formats.md](references/citation-formats.md)
- Official sources in priority order: sci.gov.in / eSCR, Verdict Finder, High Court portals, judgments.ecourts.gov.in, India Code, e-Gazette
- Professional duty: Bar Council of India Rules (Part VI, Chapter II) on conduct towards the court
- Fabrication tells and the five-step protocol: [references/hallucination-patterns.md](references/hallucination-patterns.md)

## Limits

- Existence can only be marked VERIFIED when an official copy was opened in the session; without browsing, everything stays UNVERIFIED with search instructions.
- It does not promise citator coverage; it reports what later treatment was found in the sources checked on the date checked.
- It verifies what is cited; it does not find new authorities.
- Foreign authorities are form-checked and flagged for the foreign jurisdiction's official reporter.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must independently confirm every authority before relying on it.
