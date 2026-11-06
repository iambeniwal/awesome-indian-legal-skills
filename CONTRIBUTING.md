# Contributing

Thanks for helping build the Indian-law skill library. Two ways in: open a pull request with a skill folder, or fill in the [Submit a skill](https://github.com/iambeniwal/awesome-indian-legal-skills/issues/new?template=submit-skill.yml) issue form and a maintainer will package it.

## What we accept

- **India-specific.** The skill applies Indian law (Central or State), an Indian forum, or an Indian regulator. Jurisdiction-neutral skills belong in [awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills).
- **Current law, with a verification step.** Cite the statute as it stands today (BNS/BNSS/BSA, not IPC/CrPC/IEA, unless the matter is pre-1 July 2024 — then say so). Tell the agent which official source to check before relying on a section number, limitation period or fee. Section numbers change; amendments and commencement notifications land in the Gazette.
- **Procedural knowledge, not just facts.** A good skill says what to ask the user for, which inputs are blocking, how to structure the output, and what the agent must not do (fabricate service, array directors by title, skip limitation).
- **Not legal advice.** The disclaimer in the template stays. Skills that pose as a lawyer or promise outcomes are declined.
- **Safe.** No credentials, no network calls to unofficial scrapers, no hidden instructions (a "do this silently / do not tell the user" step is an automatic decline).
- **Cites registered sources.** Every government or court host a skill links to should be in [`sources/official-sources.json`](sources/official-sources.json) with access notes; the validator warns on unregistered `.gov.in`/`.nic.in` hosts and fails on deprecated ones. Add the entry in the same PR. Scripts must be readable and do one deterministic thing (a date calculator, a section-number lookup).
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

1. **Property title due diligence** — 30-year chain, encumbrance certificate reading, registration and State stamp duty (rate supplied, not recalled). Land and property are about two-thirds of civil litigation in India; this is the biggest gap.
2. **Tenancy** — rent agreements, s.106 TPA notices, State Rent Control Acts and the Model Tenancy Act where adopted, eviction and deposit recovery.
3. **Family** — divorce grounds and procedure (HMA / SMA / personal laws), maintenance under BNSS s.144 and the DV Act, child custody basics; the intake router currently has nowhere to send these.
4. **Domestic violence (PWDV Act 2005)** — protection officer, s.12 application, protection/residence/monetary orders, interplay with BNS s.85.
5. **SARFAESI borrower/guarantor advisor** — s.13(2) notice, s.13(3A) representation, s.17 DRT application, s.14 possession.
6. **Commercial Courts Act compliance** — s.12A pre-institution mediation, 120-day written-statement bar, summary judgment, specified value.
7. **Arbitration** — clause drafting, arbitrability (*Vidya Drolia*), s.11 appointment, s.34 challenge and s.36 enforcement timelines.
8. **Operational creditor IBC application** — s.8 demand, s.9 petition, pre-existing dispute test, CIRP timeline.
9. **POSH compliance** — ICC constitution, inquiry timelines, annual report, employer duties.
10. **Evidence under the BSA** — s.63 electronic-record certificate, confessions, dying declarations, chain of custody.
11. **FEMA / NDI Rules** — FDI routes, pricing, reporting (FC-GPR/FC-TRS), beneficial-ownership approval tests.
12. **Income-tax notice replies** — s.143(2)/s.148 (2025 Act numbering), faceless assessment, appeals to CIT(A)/ITAT; pairs with the section mapper.
13. **Immigration and Foreigners Act 2025** — visas, FRRO registration, overstay penalties and compounding, OCI; the Act replaced four statutes on 1 September 2025 and nothing open covers it.
14. **Trademark clearance and opposition** — search, classes, TM-O opposition and counter-statement timelines, infringement vs passing-off.
15. **Hindi-first skills** — Hindi/Hinglish versions of the highest-traffic skills (cheque bounce, FIR, consumer) with `language: [en, hi]`; the intake router already routes in the user's language.

## Review process

A maintainer reads the skill end to end, runs it on two or three prompts, and checks the law against India Code and the relevant court or regulator site. Expect questions. Once merged, the skill appears in the index and the marketplace on the next build.
