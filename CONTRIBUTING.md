# Contributing

Thanks for helping build the Indian-law skill library. Two ways in: open a pull request with a skill folder, or fill in the [Submit a skill](https://github.com/iambeniwal/awesome-indian-legal-skills/issues/new?template=submit-skill.yml) issue form and a maintainer will package it.

## What we accept

- **India-specific.** The skill applies Indian law (Central or State), an Indian forum, or an Indian regulator. Jurisdiction-neutral skills belong in [awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills).
- **Current law, with a verification step.** Cite the statute as it stands today (BNS/BNSS/BSA, not IPC/CrPC/IEA, unless the matter is pre-1 July 2024 — then say so). Tell the agent which official source to check before relying on a section number, limitation period or fee. Section numbers change; amendments and commencement notifications land in the Gazette.
- **Procedural knowledge, not just facts.** A good skill says what to ask the user for, which inputs are blocking, how to structure the output, and what the agent must not do (fabricate service, array directors by title, skip limitation).
- **Not legal advice.** The disclaimer in the template stays. Skills that pose as a lawyer or promise outcomes are declined.
- **Safe.** No credentials, no network calls to unofficial scrapers, no hidden instructions. Scripts must be readable and do one deterministic thing (a date calculator, a section-number lookup).
- **Yours to give.** Submit only skills you wrote or have the right to relicense, and name every source you adapted.

## Folder layout

```
skills/<skill-name>/
├── SKILL.md          # required — frontmatter + instructions
├── README.md         # required — human-readable overview, inputs, outputs, examples
├── LICENSE.txt       # required — MIT by default; use your own if you must
├── references/       # optional — tables, statutory text, section maps the agent loads on demand
├── scripts/          # optional — small deterministic helpers (Python 3, standard library only)
├── assets/           # optional — templates used in output
└── evals/            # optional but encouraged — test prompts in the claude plugin eval layout
```

`<skill-name>` is lowercase-with-hyphens and must match `name:` in the frontmatter. Keep `SKILL.md` under 500 lines; move long tables into `references/` and point to them.

## Frontmatter

```yaml
---
name: cheque-bounce-s138-advisor
description: >
  What the skill does, then when to use it — be concrete about the user phrases and situations
  that should trigger it. This field is how the agent decides to load the skill.
license: MIT
metadata:
  author: Your Name
  author_url: https://github.com/you
  version: "2026.11.06"
  category: Criminal Law
  jurisdiction: IN
  states: all            # or a list, e.g. [Maharashtra, Delhi]
  language: en           # add hi, or others, if the skill handles them
---
```

`category` must be one of the names in `scripts/build.py` (`CATEGORIES`). Propose a new one in your PR if nothing fits.

## Before you open the PR

```bash
python3 scripts/validate.py
```

```bash
python3 scripts/build.py
```

The validator checks names, frontmatter, line counts, licence files and broken relative links. The build script regenerates the README index and `.claude-plugin/marketplace.json` from the frontmatter — commit those changes with your skill. CI runs both and fails the PR if either is stale.

## Writing tips

- Start from [`templates/skill-template/`](templates/skill-template/).
- Explain *why* a step matters ("territorial jurisdiction follows the payee's bank branch under s.142(2), so get the presentment bank's address, not the drawer's") rather than issuing bare commands. Agents follow reasoning better than shouting.
- Put the trigger phrases in `description`, not in the body. Mention Hindi/Hinglish phrasings users actually type ("cheque bounce ho gaya", "FIR nahi likh rahe").
- Separate what the user supplied, what the statute says, and what the agent is inferring. Mark anything unverified.
- Use the Anthropic [skill-creator](https://github.com/anthropics/skills) for a final review pass if you have it.

## Wanted

Skills we would most like to list next, in rough priority (each is a gap across the open Indian legal-AI projects we surveyed). Open an issue to claim one so two people don't build the same thing.

1. **Quashing petition (BNSS s.528)** — FIR/charge-sheet quashing grounds (*Bhajan Lal* parameters), matrimonial-cruelty focus, interim protection; pairs with the bail skill.
2. **Labour dues calculator** — gratuity, PF/ESI, bonus, retrenchment compensation and notice under the ID Act and the Labour Codes (commencement-gated), with worked examples.
3. **Writ jurisdiction advisor** — Article 32 vs 226, the "State" test, which writ, alternative remedy, laches, locus; PIL viability.
4. **GST show-cause and ITC dispute replies** — ss.73/74 timelines, pre-deposit, appeal to GSTAT.
5. **SARFAESI borrower/guarantor advisor** — s.13(2) notice, s.13(3A) representation, s.17 DRT application, s.14 possession.
6. **Property title due diligence** — 30-year chain, encumbrance certificate reading, registration and State stamp duty (rate supplied, not recalled).
7. **Commercial Courts Act compliance** — s.12A pre-institution mediation, 120-day written-statement bar, summary judgment, specified value.
8. **Arbitration** — clause drafting, arbitrability (*Vidya Drolia*), s.11 appointment, s.34 challenge and s.36 enforcement timelines.
9. **Operational creditor IBC application** — s.8 demand, s.9 petition, pre-existing dispute test, CIRP timeline.
10. **POSH compliance** — ICC constitution, inquiry timelines, annual report, employer duties.
11. **FIR / s.173 BNSS drafter** — zero FIR, e-FIR, s.175(3) application when police refuse.
12. **Evidence under the BSA** — s.63 electronic-record certificate, confessions, dying declarations, chain of custody.
13. **Companies Act compliance calendar** — forms, due dates, additional fees and penalties for a private company.
14. **FEMA / NDI Rules** — FDI routes, pricing, reporting (FC-GPR/FC-TRS), beneficial-ownership approval tests.
15. **Hindi / Hinglish intake** — a front-end skill that takes a lay narrative in Hindi or Hinglish, identifies the legal issue and routes to the right skill; mark it `language: [en, hi]`.

## Review process

A maintainer reads the skill end to end, runs it on two or three prompts, and checks the law against India Code and the relevant court or regulator site. Expect questions. Once merged, the skill appears in the index and the marketplace on the next build.
