# FIR and Police Complaint Drafter

The complainant's first steps under the BNSS, 2023: it decides the route (FIR, zero FIR, e-FIR, non-cognizable report, cyber portal plus bank, DV Act, POSH, or a private complaint), drafts the written complaint for the police station, and — when the police will not act — drafts the representation to the Superintendent of Police under s.173(4) and the application to the Magistrate under s.175(3) with its affidavit, with a dates calculator for every statutory window.

For victims and informants, their families, and advocates on the complainant's side.

## Install

```bash
claude plugin install fir-and-police-complaint-drafter@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- What happened, when, where, who — in your own words (Hindi/Hinglish is fine)
- The evidence you have (messages, screenshots, UTRs, photos, medical papers, CCTV locations)
- Whether you already went to the police or the cyber portal, and what happened
- Whether anyone is in danger now

## What you get

- Route decision with the likely BNS sections marked "appears to attract"
- Draft complaint to the SHO, with a dispatch-and-proof plan
- If refused: s.173(4) representation to the SP → s.175(3) application with affidavit → s.223 private complaint, in the order the BNSS requires
- Timeline: 3-day e-FIR signature, 14-day preliminary enquiry, SP wait, 90-day progress report, 2-month target for listed sexual offences, 3-working-day bank window for cyber fraud
- Evidence checklist and a what-happens-next walkthrough of the informant's rights

## Calculator

```bash
python3 scripts/fir_timeline.py --incident 2026-10-01 --reported 2026-10-02 --refused 2026-10-02 --sp-sent 2026-10-05
```

Add `--efir`, `--cyber`, `--sexual-offence`, `--fir-registered YYYY-MM-DD`, or `--json`.

## Example prompts

- "Someone took ₹1.8 lakh from my account through a fake KYC link yesterday. What do I do first and what do I write to the police?"
- "Police at Sector 20 station refused to take my complaint about my neighbour assaulting my father. They said it's a civil matter. Draft what I should send to the SP and the Magistrate."
- "Mera phone cheen liya gaya raat ko station ke bahar, police bol rahi hai dusre thane jao. FIR kaise likhwaun?"

## Law covered

- BNSS, 2023 — ss.172–175, 183, 193, 210, 223, 396; First Schedule (cognizability)
- BNS, 2023 — s.72 (victim identity), ss.217/248 (false information / false charge)
- Protection of Women from Domestic Violence Act, 2005; POSH Act, 2013; POCSO Act, 2012 (routing only)
- RBI customer-liability framework (2017) and the National Cyber Crime Reporting Portal
- Key decisions: *Lalita Kumari*, *Bhajan Lal*, *Tapan Kumar Singh*, *Sakiri Vasu*, *Sudhir Bhaskarrao Tambe*, *Priyanka Srivastava*, *Babu Venkatesh*, *Satvinder Kaur*, *Bhagwant Singh*, *Vinubhai Malaviya*, *Arnesh Kumar* — see [references/case-law.md](references/case-law.md)

## Limits

- It does not know your State's police portal, Commissionerate structure or station practice; it tells you to check.
- It never promises registration or arrest, and never states the sections as certain.
- The accused's side (bail, quashing) is in the companion skills.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — in any present danger, call 112 first.
