# Changelog

All notable changes to this list. Individual skills carry their own `version` in frontmatter.

## 2026-11-06 — batch 2: nine skills, source registry, "What changed" table

- Nine new skills (19 total):
  - `company-incorporation-india` — entity choice, SPICe+/FiLLiP steps, post-incorporation clocks (first board meeting, first auditor/ADT-1, INC-20A, share certificates, LLP Form 3) with a deadline calculator
  - `company-annual-compliance-calendar` — AOC-4/MGT-7/ADT-1/DIR-3 KYC/DPT-3/MSME-1, board-meeting and AGM rules, LLP Forms 11/8, additional-fee exposure, with a calendar generator
  - `income-tax-act-2025-section-mapper` — 1961 ↔ 2025 section table (209 rows, provenance noted per row) and transition rules for the 1 April 2026 switch
  - `gst-notice-reply-drafter` — ASMT-10/DRC-01/orders under ss.73/74/74A, ITC reconciliation defences, s.107/s.112 appeals and pre-deposits, with a deadline calculator
  - `labour-codes-compliance-checker` — the four Codes in force since 21 Nov 2025 and the May 2026 Central Rules, obligations checklist, State-rules status, with a dues calculator (50% wages rule, gratuity, retrenchment, leave, bonus)
  - `writ-petition-advisor` — Art. 32/226/227, the Art. 12 test, writ types, alternative-remedy exceptions, PIL filters, petition structure
  - `quashing-petition-bnss-528` — *Bhajan Lal* frame, settlement and matrimonial lines, *Neeharika* limits, petition skeleton; pairs with bail
  - `fir-and-police-complaint-drafter` — s.173 BNSS (e-FIR, zero FIR, preliminary enquiry), SP → s.175(3) → s.223 routes, cyber-fraud reporting, with a timeline script
  - `hinglish-legal-intake-router` — Hindi/Hinglish/English front door that flags urgency, asks up to three questions and routes to the right skill; first `language: [en, hi]` skill
- `sources/official-sources.json`: registry of every government/court host the skills cite, with access notes and deprecated hosts; the validator now warns on unregistered `.gov.in`/`.nic.in` hosts and fails on deprecated ones (which caught the legacy India Code host in 17 files).
- README: "What changed recently" table (BNS/BNSS/BSA, Immigration Act 2025, GST 2.0, DPDP Rules, Labour Codes, Income-tax Act 2025, the 2026 Supreme Court direction on AI-fabricated citations, Mediation Council); three more repos in Resources (judicialmind, KeshariPiyush24, attorneynate); new "Intake & Triage" category.
- Validator also requires the "Jurisdiction gate", "Verify before relying" and "Guardrails" sections; CONTRIBUTING's Wanted list refreshed (property, tenancy, family, DV, SARFAESI, Commercial Courts, arbitration, IBC, POSH, BSA evidence, FEMA, income-tax notices, Immigration Act, trademarks, Hindi-first skills).

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
