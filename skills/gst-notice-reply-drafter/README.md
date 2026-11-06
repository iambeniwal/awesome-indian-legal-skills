# GST Notice Reply and Appeal Drafter

Takes a GST notice from the portal and turns it into a classified, dated, defensible reply — or an appeal with the pre-deposit worked out. It identifies the form and provision (ASMT-10, DRC-01A, DRC-01 under s.73/s.74/s.74A, DRC-07, MOV-07, s.70 summons), computes every deadline and the demand limitation back from the annual-return due date, takes the threshold objections first (limitation, jurisdiction, cross-empowerment, defective SCN, no hearing), builds an allegation-by-allegation defence matrix with the ITC reconciliation at its centre, checks the department's arithmetic, and drafts the reply, rectification or grounds of appeal.

For chartered accountants, tax advocates, in-house indirect-tax teams, and business owners facing their first notice.

## Install

```bash
claude plugin install gst-notice-reply-drafter@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- The notice or order (form, reference, date of issue and of service, officer, section, period, amounts)
- GSTIN, State, and whether you are under the Central or State administration
- The allegations in a line each; for appeals, the disputed tax head-wise and what is already paid
- Returns, 2A/2B downloads, registers, invoices and payment proofs when available

## What you get

- Notice classification and a deadline table (reply date, settlement windows, SCN/order limitation, appeal and pre-deposit dates)
- Preliminary objections and a defence matrix (allegation → documents → provision → argument)
- A computation check (interest on net cash liability, penalty percentages, double counting)
- Draft ASMT-11 / DRC-06 reply, s.161 rectification, APL-01 or GSTAT grounds with the pre-deposit statement
- A documents checklist and a list of what to verify on cbic-gst.gov.in

## Calculator

```bash
python3 scripts/gst_deadlines.py --notice drc01 --date 2026-09-15 --period FY2022-23 --section 73
```

```bash
python3 scripts/gst_deadlines.py --notice order --date 2026-08-20 --disputed-tax 12000000 --json
```

The docstring lists the default annual-return due dates per financial year and the s.168A extensions; pass `--annual-return-due` when yours differs.

## Example prompts

- "We got a DRC-01 under section 74 for FY 2019-20 on 10 Sept 2026 alleging ITC from a cancelled supplier. Is it within time and what do we reply?"
- "ASMT-10 says our 3B ITC is ₹4.2 lakh more than 2B. We have the invoices. Draft the ASMT-11."
- "Order confirms ₹1.2 crore tax plus interest and penalty. Appeal deadline, pre-deposit, and grounds please."

## Law covered

- CGST Act, 2017 — ss.6, 16, 17, 29, 46, 50, 61, 65, 66, 70, 73, 74, 74A, 75, 78, 79, 83, 107, 112, 117, 118, 122, 125, 128A, 129, 130, 161, 168A, 169; CGST Rules 36, 37, 99, 142
- Finance (No. 2) Act, 2024 changes (s.74A, s.16(5)–(6), pre-deposit caps) and the GST 2.0 rate change of 22 September 2025
- Key decisions: *Safari Retreats*, *Suncraft Energy*, *Mohit Minerals*, *Radha Krishan Industries*, *Bharti Airtel* — see [references/gst-provisions.md](references/gst-provisions.md)

## Limits

- Not for registration, routine return filing, refunds or customs.
- Periods, percentages and caps are from the skill's version date; CBIC circulars change them — the skill tells you to verify each on filing day.
- It drafts; it does not file on the portal.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal or tax advice.
