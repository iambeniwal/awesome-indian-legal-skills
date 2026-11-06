# Consumer Complaint (Consumer Protection Act, 2019) Advisor

Takes a refund, defect, deficiency or misleading-ad grievance to a filing-ready complaint before the right Consumer Commission. It runs the "consumer" test before anything else, picks the forum from what was actually paid, chooses the most convenient territorial jurisdiction (including where you live or work), computes the two-year limitation, maps what you can prove to the reliefs the Act allows, checks whether an ombudsman, RERA or arbitration route is faster, and drafts the complaint with verification, affidavit and document list — plus the e-Daakhil checklist.

For advocates, and for consumers filing themselves.

## Install

```bash
claude plugin install consumer-complaint-cpa-2019@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- What you bought, from whom, for how much, and when (invoice, booking, policy, order)
- What went wrong and when you first knew
- Where you live/work and where the seller/service provider is
- Whether it was for personal use or for a business

## What you get

- Eligibility memo (consumer test, with the governing case for any hard point)
- Forum, fee note, territorial clause and s.69 limitation date from the bundled calculator
- Draft pre-complaint notice
- Draft complaint (cause title, parties, jurisdiction, dated facts with document references, the statutory label pleaded, relief under s.39 with quantification, verification, affidavit, list of documents)
- e-Daakhil filing checklist, mediation advice, parallel-forum check, defects list

## Calculator

```bash
python3 scripts/consumer_forum.py --consideration 1250000 --cause-date 2025-03-10
```

Add `--json` for structured output. Fees above ₹5 lakh are not hard-coded — read the Schedule to the 2020 Rules.

## Example prompts

- "Paid ₹1.2 lakh for a sofa in Feb 2025, delivered damaged, seller stopped replying. I'm in Pune, they're in Jodhpur. What can I do?"
- "Builder in Gurgaon is 3 years late on a ₹85 lakh flat. RERA or consumer court? Draft whichever is better."
- "Insurer repudiated my health claim citing non-disclosure of a condition I never had. Draft a consumer complaint."

## Law covered

- Consumer Protection Act, 2019 — ss.2(5), 2(7), 2(10), 2(11), 2(16), 2(28), 2(46), 2(47), 34, 35, 37, 38, 39, 41, 51, 58, 67, 69, 71, 72, 82–87, 89, 100
- Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021; Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020; Consumer Protection (Mediation) Rules, 2020; Consumer Protection (E-Commerce) Rules, 2020
- Key decisions: *Laxmi Engineering*, *Lilavati Kirtilal Mehta*, *Harsolia Motors*, *V.P. Shantha*, *Lucknow Development Authority*, *Experion Developers*, *IREO Grace Realtech*, *Emaar MGF v. Aftab Singh*, *Ambrish Kumar Shukla*, *Pyaridevi Chabiraj Steels*, *Bar of Indian Lawyers v. D.K. Gandhi* — see [references/case-law.md](references/case-law.md)

## Limits

- Not for B2B purchases for commercial purposes, employment grievances or advocates' services — it tells you when you are outside the Act.
- Does not know your State Commission's fee slabs or local practice directions; it tells you to read them.
- Does not file, serve or pay anything.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every draft before it is relied on, sent or filed.
