# Company Annual Compliance Calendar (India)

Generates the year's ROC compliance calendar for a private limited company, small company, OPC, Section 8 company or LLP — AGM, AOC-4, MGT-7/7A, ADT-1, DIR-3 KYC, DPT-3, MSME-1, board-meeting requirements, LLP Forms 11 and 8 — with a "next 60 days" view, the running additional-fee exposure for anything overdue, and income-tax/GST pointers flagged for verification.

For founders, finance teams, company secretaries and advocates.

## Install

```bash
claude plugin install company-annual-compliance-calendar@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Entity type (private / small / OPC / Section 8 / LLP) and the financial-year end
- Incorporation date if this is the first financial year
- AGM date if already held or fixed
- Today's date

## What you get

- Requirements for the year (board-meeting cadence, MBP-1/DIR-8, minutes and registers)
- A dated calendar table with the section or rule behind each date
- The items due in the next 60 days, grouped by month, with the inputs each needs
- Additional-fee exposure to date on AOC-4/MGT-7 (₹100/day) and the separate adjudication-penalty picture
- Tax and GST reminders marked "verify"

## Calculator

```bash
python3 scripts/compliance_calendar.py --fy-end 2026-03-31 --entity private --today 2026-11-06
```

```bash
python3 scripts/compliance_calendar.py --fy-end 2027-03-31 --entity private --incorporated 2026-01-15 --json
```

## Example prompts

- "What ROC filings are due for our Pvt Ltd for FY 2025-26? We held the AGM on 20 August."
- "We're an OPC — do we need an AGM, and when are AOC-4 and MGT-7A due?"
- "LLP incorporated last year: what's due this year and what happens if Form 11 is late?"

## Law covered

- Companies Act, 2013 — ss.2(41), 2(85), 90, 92, 96, 117, 118, 135, 137, 139, 164, 173, 184, 403, 446B, 455; Companies (Management and Administration), (Accounts), (Acceptance of Deposits), (Appointment and Qualification of Directors), (Registration Offices and Fees) Rules
- LLP Act, 2008 — ss.34, 35; LLP Rules, 2009 as amended 2022
- Pointers only: Income-tax Act, 2025 return dates; CGST Act s.44

## Limits

- Listed and unlisted public companies (SEBI LODR, PAS-6) are out of scope.
- Due dates move by MCA circular; every date is "unless extended" and the skill tells the agent to check.
- Small-company thresholds and LLP late-fee slabs are stated with a verify flag.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice.
