# DPDP Act Compliance Checker

Audits an organisation, product or data flow against the Digital Personal Data Protection Act, 2023 and the DPDP Rules, 2025, and drafts what is missing: a s.5 consent notice, privacy-policy clauses, a breach notification to the Data Protection Board and affected individuals, a processor clause, or a gap register with owners and deadlines pinned to the phased commencement dates. Comes with a GDPR-to-DPDP delta table for organisations that are already GDPR-aligned.

For in-house counsel, privacy and product teams, founders, and the advocates advising them.

## Install

```bash
claude plugin install dpdp-act-compliance-checker@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Who the organisation is, where it operates, and whether it serves people in India (blocking)
- A rough inventory of processing activities: what data, from whom, why, shared with whom, kept how long (blocking)
- Whether any users are under 18
- Whether you decide the purposes (Data Fiduciary) or process for someone else (Data Processor)
- Which artefact you want: audit, consent notice, policy clauses, breach notice, processor clause, GDPR delta

## What you get

- Applicability memo (s.3 nexus and exclusions)
- Role determination per activity, including Significant Data Fiduciary likelihood
- Processing-activity → lawful-ground table (consent vs s.7 legitimate uses — there is no legitimate-interest ground)
- Gap register graded Blocking / High / Medium, each with the date it bites, an owner and the evidence that closes it
- Parallel-regime map: CERT-In 6-hour reporting, RBI/SEBI/IRDAI/telecom rules, IT Rules
- The requested draft, free of GDPR vocabulary that has no DPDP meaning
- A sources-checked ledger with "verify" flags on dates and figures

## Example prompts

- "We're a Bengaluru edtech with 3 lakh users, many under 18. Here's our privacy policy and signup flow. What do we need to change for DPDP and by when?"
- "Draft a DPDP consent notice for a food-delivery app: account, orders, personalised offers, partner sharing."
- "We had a database exposure yesterday affecting 40,000 customers. Draft the Board report and the customer notice, and tell me every clock that's running."
- "We're GDPR compliant. What's actually different for India?"

## Law covered

- Digital Personal Data Protection Act, 2023 — ss.2–17 (applicability, consent, legitimate uses, Fiduciary duties, children, rights, SDFs, cross-border, exemptions), ss.18–29 (Board, appeals to TDSAT), s.33 and the Schedule (penalties), s.44 (IT Act s.43A omitted; RTI Act s.8(1)(j))
- DPDP Rules, 2025 — notice, consent managers, security safeguards, breach intimation, retention, children's consent, SDF duties, rights and grievance timelines, Board procedure; phased commencement (immediate / 12 months / 18 months)
- Overlap: IT Act s.43A and SPDI Rules 2011 (until superseded), CERT-In directions of 28 April 2022, RBI payment-data localisation, sector circulars
- See [references/obligations-checklist.md](references/obligations-checklist.md), [references/dpdp-vs-gdpr.md](references/dpdp-vs-gdpr.md) and [assets/consent-notice-template.md](assets/consent-notice-template.md)

## Limits

- Commencement dates, rule numbers and penalty caps are stated "as notified" and flagged for verification — this area moves, and constitutional challenges are pending.
- Sector regimes (RBI, SEBI, IRDAI, health, telecom) are flagged, not audited in depth.
- It does not decide whether you are a Significant Data Fiduciary — only the Government's notification does.
- It does not file or send anything.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every interpretation and draft before it is relied on, published or sent.
