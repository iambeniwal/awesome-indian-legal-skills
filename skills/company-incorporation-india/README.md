# Company Incorporation (India) Advisor

Picks the right legal form for a new Indian business and takes it through incorporation on MCA V3 — SPICe+ Part A/B with e-MoA/e-AoA and AGILE-PRO-S for companies, FiLLiP and the Form 3 LLP Agreement for LLPs — then lays out every post-incorporation clock with a bundled calculator: first board meeting, first auditor and ADT-1, share certificates, INC-20A, first financial year and AGM, Form 3/11/8.

For founders, in-house teams and company secretaries.

## Install

```bash
claude plugin install company-incorporation-india@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- What the business does and whether it will raise money or be non-profit
- Founders: number, residency, nationality; any foreign shareholding
- Capital and the State of the registered office
- For the deadline table: incorporation date and the date subscription money comes in

## What you get

- Entity recommendation with reasons (Pvt Ltd / OPC / Section 8 / LLP / partnership / proprietorship)
- Pre-filing checklist (people, DSC/DIN, documents, registered office, name search status)
- Step sequence with realistic timing and the fee/stamp-duty items to look up for your State
- Dated deadline table with penalties for misses
- FEMA flags where a non-resident is involved

## Calculator

```bash
python3 scripts/incorporation_deadlines.py --incorporated 2026-11-06 --entity llp
```

```bash
python3 scripts/incorporation_deadlines.py --incorporated 2026-01-15 --entity company --subscription-received 2026-02-01 --json
```

## Example prompts

- "Two of us want to start a SaaS company in Bengaluru and raise an angel round next year. Pvt Ltd or LLP, and what do we file?"
- "We incorporated an LLP on 6 November. What's due and when?"
- "Company incorporated 15 Jan 2026, subscription money came 1 Feb. Give me the INC-20A, auditor and AGM deadlines."

## Law covered

- Companies Act, 2013 — ss.2(41), 2(62), 2(68), 2(85), 3–22, 10A, 12, 56, 96, 128, 139(6), 149(3), 173; Companies (Incorporation) Rules, 2014; Companies (Audit and Auditors) Rules, 2014 (revised ADT-1, G.S.R. 359(E), 14 July 2025)
- LLP Act, 2008 — ss.7, 11–13, 23, 34, 35; LLP Rules, 2009 (2022 fee amendments)
- Indian Partnership Act, 1932 — s.69; DPIIT Startup and Udyam criteria; FEMA/NDI Rules pointers (FC-GPR)

## Limits

- Never quotes State stamp duty or professional-tax figures; it tells you where to look them up.
- Flags FEMA issues but does not do the Government-route analysis.
- MCA V3 forms and fees change; the skill dates everything and tells the agent to verify on mca.gov.in.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice.
