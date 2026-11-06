# Cheque Bounce (s.138 NI Act) Advisor

Takes a dishonoured-cheque matter from return memo to complaint (or defence). It audits every ingredient of section 138 of the Negotiable Instruments Act, 1881 against a document, computes the full deadline chain with a bundled calculator, fixes territorial jurisdiction under s.142(2), checks who can lawfully be named under s.141, and drafts the demand notice, the complaint or the reply — with a defect list instead of a draft when something blocking is missing.

For advocates, and for payees or drawers handling the first steps themselves.

## Install

```bash
claude plugin install cheque-bounce-s138-advisor@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Cheque particulars and the return memo (reason and **the date you received it**)
- What the cheque was for (the debt or liability) and any paper behind it
- The branch where you presented the cheque (this decides the court)
- If a notice has gone out: when, how, and when it was received

## What you get

- A deadline table: presentment validity, 30-day notice, 15-day payment window, cause of action, one-month complaint limitation, each with today's status
- Ingredient-by-ingredient maintainability check mapped to documents
- Jurisdiction analysis under s.142(2)
- s.141 party matrix for company/firm drawers
- Draft notice, complaint (with verification, affidavit, document and witness lists) or reply
- Defects, missing documents, next steps and a sources-checked ledger

## Example prompts

- "Client's cheque for ₹4.2 lakh bounced on 20 Aug (insufficient funds). We got the memo on 22 Aug. Haven't sent a notice yet. Presented at HDFC Koramangala. What do we do and by when?"
- "I received a 138 notice for a cheque I gave as security for a loan I already repaid in cash. Draft a reply."
- "Here are the cheque, memo, notice, speed-post tracking and AD card. Draft the complaint for the Saket court."

## Calculator

```bash
python3 scripts/s138_timeline.py --cheque-date 2026-07-01 --memo-received 2026-08-20 --notice-sent 2026-09-05 --notice-served 2026-09-09
```

Add `--json` for structured output. Court holidays are not applied — a deadline falling on a holiday moves to the next working day under s.4 Limitation Act / s.10 General Clauses Act.

## Law covered

- Negotiable Instruments Act, 1881 — ss.118, 138–148 (as amended 2002, 2015, 2018)
- BNSS, 2023 — ss.223, 227, 283–288, 395 (complaint, process, summary trial, compensation)
- General Clauses Act, 1897 — s.27 (deemed service)
- Key decisions: *Rangappa*, *K. Bhaskaran*, *Suman Sethi*, *C.C. Alavi Haji*, *Yogendra Pratap Singh*, *Econ Antri*, *Bridgestone India*, *S.M.S. Pharmaceuticals*, *Aneeta Hada*, *Damodar S. Prabhu*, *Expeditious Trial (In re)*, *Rakesh Ranjan Shrivastava* — see [references/case-law.md](references/case-law.md)

## Limits

- Not for forged or stolen cheques (BNS offences) or pure civil recovery — it tells you when you are in that territory.
- Does not know your court's holiday calendar or local Criminal Rules of Practice; it tells you to check them.
- Does not file, send or serve anything.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every draft before it is relied on, sent or filed.
