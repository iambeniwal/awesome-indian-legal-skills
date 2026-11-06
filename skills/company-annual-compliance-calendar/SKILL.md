---
name: company-annual-compliance-calendar
description: >
  Builds the recurring compliance calendar for an Indian private limited company, small company,
  OPC, Section 8 company or LLP — board meetings, AGM, AOC-4, MGT-7/7A, ADT-1, DIR-3 KYC, DPT-3,
  MSME-1, MBP-1/DIR-8, MGT-14, CSR-2, BEN-2, LLP Forms 11 and 8 — with a bundled deadline generator,
  a "next 60 days" view and the additional-fee exposure for anything overdue, plus income-tax and GST
  pointers. Use whenever a user asks "what ROC filings are due", "annual compliance for my Pvt Ltd /
  LLP", "AOC-4 / MGT-7 due date", "DIR-3 KYC", "DPT-3", "MSME-1", "when is our AGM due", "compliance
  calendar for FY 2026-27", "ROC late fees", or wants a month-by-month checklist for a company
  secretary. Not for incorporation-year clocks like INC-20A or Form 3 (route to
  company-incorporation-india) or for listed-company SEBI LODR compliance.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Corporate & Commercial
  jurisdiction: IN
  states: all
  language: en
---

# Company Annual Compliance Calendar (India)

Produces a dated, entity-specific compliance calendar for the financial year, the items falling in the next 60 days, and the fee and penalty exposure for anything already missed. For founders, finance teams, company secretaries and advocates advising private companies and LLPs.

> **Not legal advice.** This is a research and planning aid under Indian law. A qualified company secretary or advocate must confirm every date and filing; MCA extends and changes due dates by circular. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only — Companies Act, 2013 and LLP Act, 2008 filings with the Registrar of Companies, plus Central income-tax and GST pointers. Identify the entity type precisely (private / small / OPC / Section 8 / LLP; listed or unlisted public companies are out of scope — say so) and the State for professional-tax and Shops & Establishment renewals, which this skill only flags.

## Verify before relying

Every date below is "unless extended by MCA circular". Before stating a date, fee or threshold as current, check and record the date checked:

- Companies Act, 2013 (ss.2(85), 92, 96, 118, 135, 137, 139, 173, 184, 403, 455) and the LLP Act, 2008 (ss.34, 35): [India Code](https://www.indiacode.gov.in/)
- Rules and fee tables: Companies (Management and Administration) Rules, Companies (Accounts) Rules, Companies (Acceptance of Deposits) Rules (Rule 16 — DPT-3), Companies (Appointment and Qualification of Directors) Rules (DIR-3 KYC), Companies (Registration Offices and Fees) Rules (₹100/day additional fee for s.92/s.137 filings), LLP Rules 2009 as amended in 2022 (slab-multiplier late fees): [MCA Acts & Rules](https://www.mca.gov.in/)
- Current extensions, circulars and form versions: [MCA](https://www.mca.gov.in/) → notifications/circulars; [e-Gazette](https://egazette.gov.in/)
- Small-company thresholds (s.2(85) read with Rule 2(1)(t)): ₹4 crore paid-up / ₹40 crore turnover per G.S.R. 700(E) of 15 September 2022; a later increase has been reported — **verify the current figure before classifying** a company as small
- Income-tax: the **Income-tax Act, 2025** applies from tax year 2026-27 (1 April 2026); confirm the return due dates and section numbers under the new Act on [incometax.gov.in](https://www.incometax.gov.in/); GST return dates on [gst.gov.in](https://www.gst.gov.in/)

If no browsing tool is available, say the calendar is from the skill's version date and must be verified on MCA.

## Required inputs

**Blocking:**
- Entity type: private limited, small company (check the thresholds), OPC, Section 8, or LLP
- Financial year end (31 March for almost everyone — s.2(41)) and whether this is the **first** financial year (incorporation date)
- AGM date if already held or fixed (otherwise the calendar assumes the last permissible date)
- Today's date

**Nice to have:** whether an auditor is being appointed/re-appointed at this AGM (ADT-1), deposits or exempted deposits outstanding (DPT-3), dues to MSME suppliers beyond 45 days (MSME-1), CSR applicability (net worth ₹500 crore / turnover ₹1,000 crore / net profit ₹5 crore — s.135), any significant beneficial owner (BEN-2), resolutions passed needing MGT-14, DIN holders list (DIR-3 KYC), GST and tax-audit status, State registrations.

## Method

1. **Classify the entity first**, because the calendar changes shape: a small company or OPC files MGT-7A and holds two board meetings; an OPC holds no AGM; a Section 8 company has the general calendar plus licence conditions and CSR exposure; an LLP has Forms 11 and 8 and no board/AGM machinery. Confirm "small company" against the current thresholds rather than assuming it.

2. **Generate the calendar with the bundled script** and paste its table:
   ```bash
   python3 scripts/compliance_calendar.py --fy-end YYYY-03-31 --entity private|small|opc|section8|llp [--agm YYYY-MM-DD] [--incorporated YYYY-MM-DD] [--today YYYY-MM-DD] [--window 60] [--json]
   ```
   Companies: AGM within six months of FY end (s.96 — by 30 September), the first AGM within nine months of the first FY end, gap between AGMs ≤15 months; AOC-4 within 30 days of the AGM (s.137; OPC: within 180 days of FY end); MGT-7 or MGT-7A within 60 days of the AGM (s.92; OPC: 60 days from the date the AGM would have been due); ADT-1 within 15 days of the AGM that appoints or re-appoints the auditor (s.139(1)); DIR-3 KYC/web-KYC for every DIN holder by 30 September (DIN deactivated on 1 October, ₹5,000 to reactivate); DPT-3 by 30 June (Rule 16); MSME-1 by 30 April and 31 October for dues beyond 45 days; MBP-1 and DIR-8 at the first board meeting of each FY (ss.184, 164); MGT-14 within 30 days of specified resolutions (s.117); minutes within 30 days of each meeting (s.118); CSR-2 and BEN-2 where applicable. LLP: Form 11 by 30 May and Form 8 by 30 October (audit if turnover >₹40 lakh or contribution >₹25 lakh), DIR-3 KYC for DPIN holders by 30 September. The script also prints income-tax and GST **pointers** (ITR, tax audit, advance tax, TDS returns, GSTR-9/9C) flagged "verify" — they are reminders, not computed law.

3. **Board-meeting discipline** is a requirement, not a date: at least four meetings a year with no gap over 120 days (s.173(1)); a small company, OPC or dormant company needs two, one in each half-year, at least 90 days apart (s.173(5)); a Section 8 company needs one in every six months (exemption notification). Put these in the "requirements" block of the output with the last meeting date the user gave and the latest date for the next one.

4. **Price the misses honestly.** AOC-4 and MGT-7/7A carry an **additional fee of ₹100 per day** of delay (s.403 read with the 2018 fee rules) — a fee, not a penalty, and it keeps running; separately, adjudication penalties exist under ss.92(5) and 137(3) (company and officers; small-company halving under s.446B). Other forms use the slab additional fees. LLP Forms 11/8 use the 2022 slab multipliers (small LLP 1×/2×/4×/6×/10×/15×; other LLPs 1×/4×/8×/12×/20×/30× of the normal fee by delay band, with a per-day element beyond 360 days — verify the table). Say which is which, and never call an additional fee a fine.

5. **Flag the structural routes** when the facts call for them: dormant-company status under s.455 for a company with no significant transactions; voluntary strike-off (STK-2) only after INC-20A and all overdue filings; conversion of an OPC or small company when thresholds are crossed (verify current triggers).

6. **Build the next-60-days view** from the script's window output: form, due date, days left, owner (director/CS/CA), inputs needed (signed financials, auditor consent, board resolution). Group by month.

## Output

```
# Compliance calendar — [entity name], [entity type], FY [YYYY-YY] (as of [today])
## Summary (plain language: what is overdue and its running cost; what falls in the next 60 days)
## Requirements this year (board meetings, AGM window, registers/minutes) with the next latest dates
## Calendar table (output of compliance_calendar.py: form → section/rule → trigger → due date → status → fee note)
## Next 60 days (grouped by month, with owner and inputs needed)
## Exposure for overdue items (additional fee to date; adjudication penalty range; DIN deactivation)
## Tax and GST pointers (verify on incometax.gov.in / gst.gov.in)
## Items to verify on MCA (extensions in force, current forms, small-company status)
```

For a one-line question ("when is MGT-7 due?") collapse to the row, the rule and "unless extended".

## Guardrails

- Every date is "unless extended by MCA circular" — say it, and check for an extension before telling anyone they are late.
- Never say an OPC must hold an AGM or that a private company files PAS-6 (unlisted *public* companies do); never apply listed-company (SEBI LODR) items here.
- Do not classify a company as "small" without checking the current thresholds; the filing (MGT-7 vs 7A) and penalties depend on it.
- Additional fees are fees; adjudication penalties are separate and discretionary — do not add them together as a "fine".
- Income-tax and GST dates are pointers under the Income-tax Act, 2025 regime — verify, do not assert.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/calendar-rules.md](references/calendar-rules.md) — the form-by-form table (section, trigger, due date, who files, fee/penalty), entity differences, board-meeting rules, small-company and CSR thresholds, dormant/strike-off routes. Read it before the exposure section.
- [scripts/compliance_calendar.py](scripts/compliance_calendar.py) — the calendar generator; `--json` for structured output.
