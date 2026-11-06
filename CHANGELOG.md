# Changelog

All notable changes to this list. Individual skills carry their own `version` in frontmatter.

## 2026-11-06 — review pass against the surveyed repos

- `ipc-bns-section-mapper`: table cross-checked row by row against the NCRB *Sankalan* corresponding-section table (as parsed in nyaya-model's statute database); 16 rows added (house-trespass/house-breaking, waging war, counterfeiting, personating a public servant, election bribery, false charge, harbouring, spreading infection). Eight apparent disagreements were traced to continuation-row shifts in that parse and resolved from the BNS/BNSS section titles; the table stands. Two eval cases added from bns-legal-rag's scenarios.
- `bail-application-bnss`: s.480(6), s.482(4) (bar for BNS s.65/70(2)) and s.483(1) proviso/(2) confirmed against the BNSS text; verify flags removed.
- `indian-case-citation-verifier`: India Code canonical host is `indiacode.gov.in`; e-SCR at `scr.sci.gov.in/scrsearch/` (CAPTCHA); `api.sci.gov.in` direct PDFs; `judgments.ecourts.gov.in/pdfsearch/`; NJDG is statistics only.
- `dpdp-act-compliance-checker`: s.5(2) transitional notice keyed to DPDP commencement (not 1 July 2024); Third Schedule thresholds and Fourth Schedule Part A/B children's-data exemptions added, flagged verify.
- `rera-homebuyer-complaint`: insolvency/moratorium stop before drafting (s.14 IBC bars a fresh complaint; file a claim with the RP).
- Validator now requires the "Jurisdiction gate", "Verify before relying" and "Guardrails" sections.
- README Resources: honest descriptions of sheevu's dataset (an index, no data), the Kanoon crawler (not recommended; licence conflict) and shashionline's plugin (broad, but stale BNSS/consumer/RERA law); CONTRIBUTING gains a "Wanted" list.

## 2026-11-06 — initial release

- Repository scaffold: README with generated index, CONTRIBUTING, skill template, issue and PR templates, CI (`validate.py` + `build.py --check` + skill self-tests).
- Ten founding skills:
  - `cheque-bounce-s138-advisor` — s.138 NI Act audit, deadline calculator, notice/complaint/reply drafts
  - `ipc-bns-section-mapper` — IPC↔BNS, CrPC↔BNSS, IEA↔BSA lookup and governing-code rules
  - `bail-application-bnss` — regular, anticipatory, default and s.479 bail under the BNSS
  - `limitation-period-calculator` — Limitation Act articles, exclusions, COVID suo motu order, calculator
  - `rti-application-drafter` — RTI applications, first and second appeals, exemption handling
  - `consumer-complaint-cpa-2019` — consumer test, forum, limitation, e-Daakhil complaint drafts
  - `rera-homebuyer-complaint` — RERA forum choice, refund/delay-interest election, complaint drafts
  - `legal-notice-drafter-india` — statutory and tactical notices and replies under Indian practice
  - `dpdp-act-compliance-checker` — DPDP Act 2023 + Rules 2025 gap audit, consent notice, breach drafts
  - `indian-case-citation-verifier` — citation form checker and verification protocol against official portals
- Resources section linking open Indian legal-AI projects (skills, datasets, RAG, crawlers).
