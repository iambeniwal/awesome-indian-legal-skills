---
name: gst-notice-reply-drafter
description: >
  Classifies a GST notice and drafts the reply or appeal under the CGST Act, 2017 and the State GST
  Acts — ASMT-10 scrutiny replies, DRC-01A/DRC-01 show-cause replies (preliminary objections on
  limitation, jurisdiction, cross-empowerment and a vague SCN; merits head by head; GSTR-2A/2B vs 3B
  ITC reconciliation; computation and penalty), s.161 rectification, APL-01 first appeals and s.112
  GSTAT appeals with pre-deposit computed on the disputed tax, plus the s.73/s.74/s.74A limitation
  back-computed from the annual-return due date with a bundled calculator. Use whenever a user mentions
  a GST notice, "DRC-01", "ASMT-10", "show cause notice GST", "GST demand order", "ITC mismatch 2A 3B",
  "section 73 / 74 / 74A", "GST appeal", "GSTAT", "pre-deposit", "GST notice ka reply", or a summons
  under s.70. Not for GST registration, return filing, refunds (except an erroneous-refund demand) or
  customs — say so and route elsewhere; income-tax sections go to income-tax-act-2025-section-mapper.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Tax & GST
  jurisdiction: IN
  states: all
  language: en
---

# GST Notice Reply and Appeal Drafter

Produces a notice classification, a deadline table, a defence matrix and a draft reply or appeal for GST proceedings in India. For chartered accountants, tax advocates, in-house indirect-tax teams and business owners who received a notice on the portal.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified chartered accountant or advocate must review every reply, computation and appeal before it is filed; GST deadlines are short and pre-deposits are real money. Say this once at the start of the first response.

## Jurisdiction gate

Indian GST only (CGST/SGST/IGST/UTGST). Identify the **State of registration** and whether the taxpayer is assigned to the **Central or State administration** — this decides the proper officer, the forum and the cross-empowerment objection. Customs, pre-GST VAT/service-tax legacy demands and foreign VAT are out of scope: say so and stop.

## Verify before relying

GST procedure moves by notification and circular, so before stating any period, percentage or form:

- Act, Rules, notifications and circulars: [cbic-gst.gov.in](https://www.cbic-gst.gov.in/); portal forms and the taxpayer's notice/order history: [gst.gov.in](https://www.gst.gov.in/) (Services → User services → View notices and orders).
- GSTAT: [gstat.gov.in](https://gstat.gov.in/) for benches, e-filing and the transitional deadlines.
- Supreme Court and High Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/) and the High Court portals; the controlling ones are summarised in [references/gst-provisions.md](references/gst-provisions.md).
- The annual-return due date for the period (it was extended in several years) — this anchors every limitation computation.

If no browsing tool is available, state that the periods and percentages are from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones first, together, in plain language — most users can paste the notice from the portal.

**Blocking:**
- The notice or order itself (form number, reference/DIN, date of issue, date it was served/communicated, the officer, the section invoked, the tax period(s))
- The GSTIN, State, and Central/State assignment
- The allegation in one line each (ITC mismatch, 2A/2B vs 3B, GSTR-1 vs 3B, rate/classification, RCM, e-way bill, non-filing, supplier cancellation) and the amounts of tax, interest and penalty demanded
- For an appeal: the order date, the date of communication, the disputed tax head-wise, and what has already been paid or admitted

**Nice to have:** GSTR-1/3B/9/9C for the period, GSTR-2A/2B downloads, purchase and sales registers, supplier invoices and payment proofs, prior DRC-01A/ASMT-10 replies, hearing notices and adjournment history, any parallel proceeding (State/Central, DGGI, audit), bank attachment notices.

## Method

1. **Classify the notice** using the table in [references/gst-provisions.md](references/gst-provisions.md) §1: scrutiny (ASMT-10), pre-SCN (DRC-01A), SCN (DRC-01 under s.73/s.74/s.74A), order (DRC-07), detention (MOV-07/09), summons (s.70), registration cancellation (REG-17), non-filer (GSTR-3A). The form decides the reply form, the period and whether a personal hearing right has already attached.

2. **Run the calculator** and paste its table:
   ```bash
   python3 scripts/gst_deadlines.py --notice drc01 --date YYYY-MM-DD --period FY2022-23 --section 73 [--annual-return-due YYYY-MM-DD] [--today YYYY-MM-DD]
   python3 scripts/gst_deadlines.py --notice order --date YYYY-MM-DD --disputed-tax 1200000
   ```
   It prints the reply date, the settlement windows (30 days under ss.73/74, 60 days under s.74A), the SCN and order limitation back-computed from the annual-return due date (3 years / 5 years / 42 months + 12 months), the s.161, s.107 and s.112 windows, and the pre-deposit on the disputed tax (10%, cap ₹20 crore CGST). Name the annual-return due date relied on in the output — if the user's period had an extended due date, pass it. If the script is unavailable, compute by hand, show each step, mark unverified.

3. **Take the threshold objections first** (§2 and §5 of the reference): SCN or order beyond limitation (s.75(10)); s.74 invoked without a specific, particularised allegation of fraud or suppression (collapse to s.73 and its shorter limit); no DRC-01A; a summary DRC-01 without a reasoned SCN; wrong proper officer; cross-empowerment / parallel proceedings (s.6(2)(b)); defective service (s.169); consolidated multi-year SCN; no personal hearing (s.75(4)) or more than three adjournments refused (s.75(5)); order beyond the SCN (s.75(7)). Each objection is pleaded "without prejudice" to the merits, so losing one costs nothing.

4. **Build the defence matrix on the merits**, allegation by allegation: allegation → documents → provision → argument → amount conceded (if any). For ITC the standard sequence is: reconcile GSTR-2B/2A with 3B and the purchase register; show invoice, receipt, payment to supplier within 180 days, and supplier's return status; apply s.16(5) for FY 2017-18 to 2020-21 time-bar demands; invoke Circulars 183/2022 and 193/2023 for 2A-3B mismatches; distinguish supplier default (s.16(2)(c)) from the taxpayer's own non-compliance and cite the recovery-from-supplier line of cases; check s.17(5) blocked-credit heads against the facts. For rate/classification, split at 22 September 2025 if the period straddles the GST 2.0 change. For RCM, e-way bill and non-filing allegations, use the reference's rows.

5. **Challenge the computation.** Interest under s.50 runs on net cash liability (after ITC) since the retrospective 2021 amendment — recompute; penalty under s.73(9)/s.74 must track the statutory percentage; penalty under s.122 and s.125 cannot be stacked on the same default without reasons; a demand on the gross turnover without allowing ITC is wrong; check CGST/SGST/IGST heads are not double counted.

6. **Decide the posture**: contest, settle (pay in DRC-03 within the window to cut penalty — say exactly what and by when), or part-pay and contest. Say what settling in the s.73 window costs versus losing on appeal; for s.74 the 25%/50%/100% ladder makes timing decisive. Never advise ignoring a summons under s.70 — attend or seek a date in writing.

7. **Draft** (Output below). In every reply, request a **personal hearing** expressly and ask for documents relied on and cross-examination where the case rests on third-party statements. For an appeal, compute the pre-deposit on the **disputed tax** head-wise, confirm the admitted tax is paid in full, and attach the DRC-03 challans; for GSTAT note the condonable period and any transitional cutoff.

## Output

```
# GST — [ASMT-10 reply | DRC-01 reply | s.161 rectification | APL-01 appeal | GSTAT appeal] — [taxpayer, GSTIN] — [period]
## Summary (plain language: what is alleged, the money at stake, the next deadline, the strongest point, settle-or-contest view)
## Notice classification (form, provision, officer, period, service date, reply form and date)
## Deadline table (output of gst_deadlines.py; annual-return due date relied on named)
## Preliminary objections (limitation, jurisdiction, cross-empowerment, service, SCN defects, hearing)
## Defence matrix (allegation → documents → provision → argument → conceded amount)
## Computation check (interest on net cash liability; penalty percentage; double counting)
## Draft reply / grounds of appeal (para-wise; prayer: drop proceedings / personal hearing / cross-examination; for appeals: statement of facts, grounds, prayer, pre-deposit statement)
## Documents checklist (returns, reconciliations, invoices, payment proofs, challans, assignment letter)
## What to verify (circular numbers, extended due dates, current pre-deposit caps, GSTAT cutoffs)
```

For a quick "what is this notice and when must I reply" question, collapse to the classification and the deadline table.

## Guardrails

- Never omit the personal-hearing request; an order without one is the most common ground of reversal and the request must be on record.
- Never compute pre-deposit on interest or penalty — it is on the disputed tax; and never present it as refundable within a time the statute does not promise.
- Never state a limitation date without naming the annual-return due date it is counted from; never assume s.168A extensions are valid or invalid — say they are contested.
- Never advise ignoring a summons, a hearing date or a DRC-01A; silence is read as admission at the order stage.
- Do not fabricate reconciliations, invoice numbers or payment dates; where the user cannot produce a document, say the point is weak rather than pleading it.
- Flag that CBIC circulars, rate notifications and portal forms change often; every figure in the reference is to be verified on cbic-gst.gov.in on the date of filing.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/gst-provisions.md](references/gst-provisions.md) — notice types, limitation and settlement ladders, ITC rules and circulars, appeals and pre-deposits, jurisdiction objections, GST 2.0 rates, decisions. Read §1–§2 before classifying; §3 for any ITC allegation; §4 before drafting an appeal.
- [scripts/gst_deadlines.py](scripts/gst_deadlines.py) — deadline, limitation and pre-deposit calculator; `--json` for structured output; the docstring lists the default annual-return due dates and extensions.
