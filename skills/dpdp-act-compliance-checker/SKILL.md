---
name: dpdp-act-compliance-checker
description: >
  Audits an organisation, product, app or data flow against India's Digital Personal Data Protection
  Act, 2023 and the DPDP Rules, 2025, and drafts what the audit says is missing — a s.5 consent
  notice, privacy-notice clauses, a breach notification to the Data Protection Board and Data
  Principals, a processor clause, or a gap register with owners and deadlines tied to the phased
  commencement dates. Use whenever a user mentions DPDP, DPDPA, "Digital Personal Data Protection",
  the Data Protection Board of India, Data Fiduciary / Data Principal / Significant Data Fiduciary,
  Consent Manager, "India privacy law", "is our app DPDP compliant", "DPDP ke liye kya karna hai",
  wants a privacy policy or consent flow for Indian users, or asks how GDPR compliance maps to
  India. Not for the IT Act SPDI Rules alone, sector-only rules (RBI/SEBI/IRDAI) or GDPR questions
  with no India nexus — say so and route elsewhere.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Data Protection & Technology
  jurisdiction: IN
  states: all
  language: en
---

# DPDP Act Compliance Checker

Runs a structured compliance audit under the Digital Personal Data Protection Act, 2023 (DPDP Act) and the DPDP Rules, 2025, grades the gaps, and drafts the artefact the user needs. For in-house counsel, privacy and product teams, founders, and advocates advising them.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate must review every interpretation, notice and filing before it is relied on, published or sent. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Confirm the s.3 nexus (below) before doing anything else: processing of digital personal data **within India**, or processing **outside India in connection with offering goods or services to Data Principals in India**. A foreign company with Indian users is in scope; an Indian company processing only non-Indian data under a foreign law is not — say which and stop if there is no nexus.

## Verify before relying

This is the area most likely to have moved since the skill's version date. Before stating a date, rule number or penalty as current, check and record the date checked:

- Act text (Act 22 of 2023, assented 11 August 2023): [India Code](https://www.indiacode.nic.in/)
- DPDP Rules, 2025 and their phased commencement notification: [e-Gazette](https://egazette.gov.in/) and [MeitY](https://www.meity.gov.in/)
- Data Protection Board notifications, SDF designations, restricted-country list under s.16, startup/research exemptions under s.17: e-Gazette
- Constitutional challenges to the Act or Rules pending before the Supreme Court can change the timeline: [sci.gov.in](https://www.sci.gov.in/)

**Commencement as notified (verify current status):** the Rules were notified on 13 November 2025 (Gazette publication reported as 13/14 November). Rules 1, 2 and 17–21 (definitions, Board constitution and functioning) took effect immediately. Rule 4 (Consent Manager registration) takes effect 12 months after publication — **November 2026**. The substantive obligations on Data Fiduciaries — notice, consent, security safeguards, breach notification, retention and erasure, children's data, Data Principal rights, SDF duties — take effect 18 months after publication — **around 13 May 2027**. Until then the IT Act s.43A / SPDI Rules 2011 framework, CERT-In's incident-reporting directions and sectoral rules continue to apply; after that date s.43A stands omitted by s.44 of the DPDP Act.

If no browsing tool is available, say the dates and figures are from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones first, together, in plain language.

**Blocking (no gap register without them — produce a scoping memo instead):**
- What the organisation is and where it is (incorporation, offices, servers/cloud regions), and whether it offers goods or services to people in India
- A list of processing activities: what personal data, from whom, for what purpose, collected how, shared with whom, kept how long. A rough inventory is enough to start
- Whether any Data Principals are **children (under 18)** or persons with disabilities with lawful guardians
- Whether the organisation decides purpose and means (Data Fiduciary) or only processes on another's instructions (Data Processor), per activity
- Which artefact the user wants: audit/gap register, consent notice, privacy-policy clauses, breach notification, processor clause, or GDPR mapping

**Nice to have:** current privacy policy and consent screens, existing GDPR/ISO 27001/SOC 2 documentation, sector (fintech/health/telecom/edtech/gaming/e-commerce/social media), user numbers (the Rules' retention table turns on thresholds), cross-border transfers and vendors, any incident history, any SDF notification received.

## Method

1. **Applicability (s.3) first.** Decide: is it *digital* personal data (collected digitally, or digitised later)? Is there the India nexus above? Does an exclusion apply — personal or domestic use, or data the Data Principal made publicly available themselves or that was made public under a legal obligation? Personal data means any data about an identifiable individual (s.2(t)); there is **no special-category concept** — health, financial and biometric data are not a separate tier under the Act (sectoral rules may add one). Write a two-paragraph applicability memo; everything else depends on it.

2. **Role, per activity.** Data Fiduciary (determines purpose and means) or Data Processor (processes on the Fiduciary's behalf, under contract — s.8(2)). The Fiduciary stays responsible for processor conduct. Check whether the organisation is, or is likely to be, notified as a **Significant Data Fiduciary** under s.10 (volume and sensitivity of data, risk to Data Principal rights, sovereignty, electoral democracy, public order): SDFs must appoint a DPO based in India who reports to the board and is the grievance contact, appoint an independent data auditor, and conduct periodic DPIAs and audits; the Rules add algorithmic due diligence and possible restrictions on transferring specified data outside India. Note that only the Government's notification makes an entity an SDF — do not self-designate, but do flag likely candidates.

3. **Map every processing activity to a lawful ground.** There are only two: **consent** (s.6) and **certain legitimate uses** (s.7). Consent must be free, specific, informed, unconditional, unambiguous, with a clear affirmative action, limited to the specified purpose, and as easy to withdraw as it was to give (s.6(4)–(6)); it must be preceded or accompanied by a **s.5 notice** (what data, for what purpose, how to exercise rights and withdraw, how to complain to the Board), available in English or any Eighth-Schedule language (s.5(3)). The s.7 uses include: data the Data Principal voluntarily provided for a specified purpose without indicating non-consent; State functions, subsidies and benefits; legal obligations and court orders; medical emergencies and public health; **employment purposes** and safeguarding the employer; disaster response. There is **no legitimate-interest ground** — marketing, analytics and profiling that cannot fit s.7 need consent. Build the activity → ground table; an activity with no ground is a blocking gap.

4. **Run the checklist** in [references/obligations-checklist.md](references/obligations-checklist.md) end to end: notice, consent mechanics and Consent Managers (s.6(7)–(9); registered Indian companies under the Rules, interoperable platform, fiduciary to the Data Principal), children (s.9 — verifiable parental consent, no tracking, behavioural monitoring or targeted advertising directed at children; Rules prescribe identity/age verification routes and sectoral exemptions), security safeguards (s.8(5); Rules list minimum measures — encryption/masking, access control, logs retained for one year, backups), **breach notification** (s.8(6) — to the Board and *each* affected Data Principal; the Rules require an intimation to the Board without delay and a detailed report within 72 hours, and a plain-language intimation to affected individuals with nature, consequences, mitigation and contact), retention and erasure (s.8(7)–(8) — erase when the purpose is served or consent withdrawn unless retention is required by law; the Rules' Third Schedule sets inactivity-based erasure for large e-commerce, online gaming and social-media intermediaries with a 48-hour pre-erasure notice), accuracy (s.8(3)), processor contracts (s.8(2)), rights handling (ss.11–14 — access, correction and erasure, grievance redressal with a published response period, nomination), cross-border (s.16 — transfers permitted except to countries on a Government negative list; sector rules such as RBI's payment-data localisation are stricter and prevail), exemptions (s.17), records and the publication of a contact person (s.8(9)).

5. **Grade each gap** as **Blocking** (no lawful ground; children's data processed without verifiable consent; no breach process; consent bundled with terms), **High** (notice missing items; no withdrawal path; no processor contract; retention undefined), or **Medium** (records, contact publication, language versions). Attach to every gap the **date it bites** (immediately for Board-facing readiness; November 2026 for Consent Manager matters; May 2027 for Fiduciary obligations — "as notified, verify"), an owner, and the evidence that would close it. Put the penalty exposure from the Schedule beside Blocking items only (up to ₹250 crore for failure of security safeguards, ₹200 crore for breach-notification and children's-data failures, ₹150 crore for SDF duties, ₹50 crore residual, ₹10,000 for Data Principal duty breaches — verify the Schedule), with the caveat that the Board decides on the s.33 factors (nature, gravity, duration, mitigation, repetition).

6. **Check the overlap.** CERT-In's 28 April 2022 directions (6-hour incident reporting, 180-day log retention) run **in parallel** and are not displaced; so do RBI, SEBI, IRDAI, TRAI/DoT and IT Rules 2021 intermediary duties. A breach may need three notifications on three clocks — say so. For a GDPR-aligned organisation, run [references/dpdp-vs-gdpr.md](references/dpdp-vs-gdpr.md) and list only the deltas; GDPR compliance is a head start, not DPDP compliance.

7. **Draft the artefact.** Consent notice from [assets/consent-notice-template.md](assets/consent-notice-template.md) — standalone, plain language, itemised data and purposes, rights, withdrawal, Board complaint route, language availability. Privacy-policy clauses — only the clauses the audit found missing. Breach notification — two versions (Board; Data Principals) with placeholders for facts not yet known and a timeline sheet. Processor clause — purpose limitation, security, sub-processing, breach assistance, return/erasure, audit. Keep every draft free of GDPR terms that have no DPDP meaning (controller, legitimate interest, DPO for a non-SDF).

## Output

```
# DPDP compliance — [organisation / product] — [audit | consent notice | breach notice | GDPR delta]
## Summary (plain language, 3–5 lines: in scope or not, biggest gaps, first deadline)
## Applicability memo (s.3 nexus, exclusions, date checked)
## Role determination (Fiduciary / Processor per activity; SDF likelihood)
## Processing activity → lawful ground table (activity, data, principals, ground, notice/consent status)
## Gap register (obligation, section/rule, status, evidence, grade, owner, bites on, closes when)
## Parallel regimes (CERT-In, sector rules, IT Rules) and their clocks
## Draft artefact (if requested)
## Sources checked (section/rule, source, date checked; items marked "verify")
```

For a single question ("do we need parental consent for 16-year-olds?") collapse to a short answer plus the rows that matter.

## Guardrails

- Do not state commencement dates, rule numbers or penalty amounts as settled without the "as notified — verify" flag and a source checked date. The Rules' timeline and pending litigation can move them.
- Do not treat GDPR, ISO 27001 or SOC 2 compliance as DPDP compliance; list the deltas.
- Never draft consent bundled with terms of service, pre-ticked, or conditioned on unrelated services — s.6 requires it to be unconditional and separately withdrawable.
- Do not advise skipping CERT-In, RBI or other sectoral reporting because DPDP obligations have not yet commenced; the old regime (s.43A/SPDI Rules) also continues until the DPDP provisions bite.
- Do not treat anyone under 18 as capable of consenting on their own; a parent's or lawful guardian's verifiable consent is required unless a notified exemption applies.
- Do not call an entity an SDF unless it has been notified; say "likely candidate" and list the s.10 factors.
- Separate what the user said, what the Act and Rules say, and what you infer. Mark unverified facts.
- Do not reproduce long statutory text; cite the section or rule and summarise.

## References

- [references/obligations-checklist.md](references/obligations-checklist.md) — the auditable checklist, in audit order. Read it whenever producing a gap register.
- [references/dpdp-vs-gdpr.md](references/dpdp-vs-gdpr.md) — where DPDP is stricter, looser or just different; read it for GDPR-aligned organisations.
- [assets/consent-notice-template.md](assets/consent-notice-template.md) — s.5 notice skeleton with placeholders.
