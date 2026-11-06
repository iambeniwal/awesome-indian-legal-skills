---
name: company-incorporation-india
description: >
  Chooses the right entity for a new Indian business (private limited, OPC, Section 8, LLP,
  partnership, proprietorship, foreign subsidiary) and walks it through incorporation on the MCA V3
  portal — SPICe+ Part A/B, AGILE-PRO-S, e-MoA/e-AoA, FiLLiP and the LLP Agreement — then computes
  the post-incorporation clocks (first board meeting, first auditor and ADT-1, INC-20A commencement,
  share certificates, Form 3, first AGM) with a bundled calculator. Use whenever a user asks how to
  register a company or LLP in India, "company kaise banaye", "startup registration", "Pvt Ltd vs
  LLP", "SPICe+", "DIN/DSC", "INC-20A", "LLP Form 3 due", "what do I do after incorporation", or
  wants a DPIIT/Udyam-ready checklist. Not for annual filings after the first year (route to
  company-annual-compliance-calendar) or for FEMA approval analysis beyond flagging it.
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

# Company Incorporation (India) Advisor

Produces an entity-choice memo, the incorporation document checklist and step sequence, and a dated post-incorporation deadline table. For founders, in-house teams and company secretaries setting up a company or LLP in India.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate or company secretary must review every choice and filing before it is made; MCA forms, fees and portal behaviour change without notice. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the **State of the registered office**: stamp duty on the MoA/AoA/LLP Agreement, professional-tax registration and Shops & Establishment rules are State-specific, and AGILE-PRO-S behaves differently by State. If a foreign investor, foreign director or overseas parent is involved, FEMA and the NDI Rules apply alongside the Companies Act — flag it and route the FEMA analysis elsewhere; do not skip it.

## Verify before relying

Check and record the date checked:

- Companies Act, 2013 (ss.2(41), 2(62), 2(68), 2(85), 3–22, 10A, 12, 56, 96, 128, 139(6), 149(3), 173) and the LLP Act, 2008 (ss.7, 11–13, 23): [India Code](https://www.indiacode.gov.in/)
- Companies (Incorporation) Rules, 2014 (Rules 8, 8A, 8B, 9, 38) and the LLP Rules, 2009 — read the **current** consolidated text and MCA notifications: [MCA](https://www.mca.gov.in/) → Acts & Rules; fees on the Companies (Registration Offices and Fees) Rules, 2014
- The live MCA V3 forms, help kits and fee calculator: [mca.gov.in](https://www.mca.gov.in/) (SPICe+, AGILE-PRO-S, INC-20A, ADT-1, FiLLiP, Form 3)
- A **draft Companies (Incorporation) Amendment Rules, 2026** (proposed E-CON / E-CHNG forms, OPC conversion changes) has been published for comments — check whether it has been notified before describing the process
- [e-Gazette](https://egazette.gov.in/) for notifications; [DPIIT Startup India](https://www.startupindia.gov.in/) and [Udyam](https://udyamregistration.gov.in/) for recognitions

If no browsing tool is available, say figures come from the skill's version date and must be verified on MCA.

## Required inputs

Ask for the blocking ones together, in plain language.

**Blocking:**
- What the business will do, and whether it will seek outside investment, grants, or not-for-profit status
- Founders: how many, where each is resident (182-day test), and whether any is a foreign national or NRI
- Any foreign shareholding or overseas parent (triggers FEMA/NDI route checks and FC-GPR)
- Proposed capital (authorised and paid-up) and the State of the registered office
- Preferred form, if any (Pvt Ltd / OPC / Section 8 / LLP / partnership / proprietorship)
- For the deadline table: the **incorporation date** (certificate date) and the date subscription money is received

**Nice to have:** proposed names (up to two for Part A), whether the registered office is ready (owned/rented, NOC, utility bill), PAN/Aadhaar/DSC status of founders, whether DPIIT or Udyam recognition is wanted, bank preference.

## Method

1. **Choose the entity with the comparison table** in [references/entity-comparison.md](references/entity-comparison.md). The usual answers: investors and ESOPs → private limited; a solo founder who wants limited liability and may convert later → OPC (one member + a nominee; mandatory conversion thresholds removed in 2021, verify); professionals and services firms that do not need equity funding → LLP (cheaper compliance, no board/AGM machinery, but no ESOP/shares and investors avoid it); charitable or non-profit → Section 8 company (licence now issued inside SPICe+; no "Pvt Ltd" suffix; profits cannot be distributed); very small trading → proprietorship via Udyam/GST/Shops & Establishment, or a registered partnership (unregistered firms cannot sue to enforce contracts — s.69 Partnership Act). Say *why* for the user's facts, not just the label.

2. **Check the minimums before names.** Company: at least two directors (OPC: one), one of whom stayed in India ≥182 days in the FY (s.149(3)); two subscribers (OPC: one + nominee in INC-3); class 3 DSC for every subscriber/director; DIN for up to three directors allotted through SPICe+ itself. LLP: two designated partners, one resident; DPIN through FiLLiP. Foreign nationals need apostilled/notarised KYC and, for Pakistan/Bangladesh/China-border nationals, prior security clearance under Press Note 3 (2020) — flag, don't advise.

3. **Clear the name.** Rules 8, 8A and 8B of the Incorporation Rules: not identical or too similar to an existing company/LLP or a registered trademark (search MCA and the IP India TM database in the same class); no "National", "Bank", "Insurance", "Stock Exchange" etc. without approval; "India" permitted. Reserve through **SPICe+ Part A** (two names, one resubmission); approval holds 20 days for a new company (verify current validity). Never tell the user a name is available without an actual MCA search.

4. **File SPICe+ Part B on MCA V3** with the linked forms: INC-32 (incorporation), e-MoA INC-33 and e-AoA INC-34 (table F/A articles; subscriber details, DSC-signed), AGILE-PRO-S (GSTIN optional, EPFO and ESIC mandatory registrations, State profession tax where applicable, bank account opening, Shops & Establishment in some States), INC-9 (auto-generated declaration), DIR-2 consents, proof of registered office (ownership/rent agreement + NOC + utility bill ≤2 months) or an INC-22 within 30 days (s.12). PAN and TAN are allotted with the certificate. MCA fee is **nil for authorised capital up to ₹15 lakh**; State **stamp duty** on MoA/AoA/INC-32 is payable in every case and varies widely — quote it only from the MCA fee calculator for the State, never from memory. Typical timing: Part A 1–3 working days; Part B 3–7 working days; each resubmission adds a cycle. Section 8: the licence application (INC-12) is part of SPICe+; attach the projected income/expenditure and declarations.

5. **LLP route.** RUN-LLP (name) or name inside FiLLiP; FiLLiP with DPIN allotment for up to two designated partners, subscribers' sheet, registered-office proof; certificate; then the **LLP Agreement in Form 3 within 30 days** of incorporation (LLP incorporated 6 Nov → Form 3 due 6 Dec), stamped per the State's stamp law on the capital contribution. Late Form 3 attracts the 2022 slab-multiplier additional fees (verify the slab and whether a per-day element applies to Form 3). Form 4 for later partner changes.

6. **Run the post-incorporation clocks** and paste the table:
   ```bash
   python3 scripts/incorporation_deadlines.py --incorporated YYYY-MM-DD --entity company|opc|section8|llp [--subscription-received YYYY-MM-DD] [--registered-office-later] [--today YYYY-MM-DD] [--json]
   ```
   Company clocks: first board meeting within 30 days (s.173(1)); first auditor appointed by the board within 30 days (s.139(6)) and ADT-1 within 15 days of that appointment; share certificates within two months of incorporation (s.56(4)(a)); INC-20A declaration of commencement within 180 days, after subscription money is received (s.10A — penalty ₹50,000 on the company and ₹1,000 per day on each officer up to ₹1 lakh, and the ROC may initiate strike-off); INC-22 within 30 days if the registered office was not given at incorporation; first financial year (s.2(41): a company incorporated on or after 1 January closes its first FY on 31 March of the *following* year) and first AGM within nine months of that FY end (s.96; OPC exempt). LLP clocks: Form 3 within 30 days; first FY (an LLP incorporated after 30 September may close on 31 March of the next-but-one year); Form 11 by 30 May and Form 8 by 30 October after the FY end. **ADT-1 for the first auditor**: the rule text (Rule 4, Audit and Auditors Rules) still refers to s.139(1), so filing for a s.139(6) board appointment is contested; the revised ADT-1 (G.S.R. 359(E), effective 14 July 2025) carries a first-auditor category and MCA's FAQ says to file — treat it as "file it" and say the legal position is contested.

7. **Set up the first-month housekeeping**: open the bank account and bring in the subscription money (needed for INC-20A); MBP-1 disclosures and DIR-8 at the first board meeting; statutory registers (members, directors/KMP, charges, share transfers); books of account (s.128); name board and letterhead with CIN, registered office, phone and email (s.12(3)); Udyam registration (MSME) and DPIIT Startup recognition if eligible (private company/LLP/partnership ≤10 years old, turnover ≤₹100 crore in any FY, working on innovation/scalable model, not formed by splitting an existing business — verify current criteria); GST if turnover/inter-State supply requires it; Shops & Establishment and professional tax where the State requires.

8. **Foreign money.** If any shareholder is non-resident: confirm the sector is under the automatic route (NDI Rules Schedule I), receive funds through an AD bank with FIRC/KYC, allot shares within 60 days of receipt, file **FC-GPR within 30 days of allotment** on FIRMS, and get the valuation certificate — or stop and route to a FEMA advisor if a Government-route sector or a land-border country is involved.

## Output

```
# Incorporation — [proposed name] — [State]
## Summary (plain language: recommended entity and why; total steps; the first three deadlines)
## Entity recommendation (table: options considered → fit for these facts → compliance load → verdict)
## Pre-filing checklist (people, DSC/DIN, documents, registered office, names with search status)
## Step sequence (Part A → Part B/FiLLiP → certificate → PAN/TAN/bank → registrations), with expected timing
## Deadline table (output of incorporation_deadlines.py, with status as of today)
## Penalties and consequences for misses (s.10A, s.12, s.56, s.173, LLP Form 3 slab fees)
## Foreign-investment flags (if any)
## Items to verify on MCA (fees, stamp duty for the State, current form versions, draft 2026 rules)
```

For a single question ("when is INC-20A due?") collapse to the row and the rule.

## Guardrails

- Never quote State stamp duty, professional-tax or Shops & Establishment figures from memory; name the State and point to the MCA fee calculator / State portal.
- Never present a proposed name as available without an actual MCA and trademark search; say "appears available as of [date]".
- Never skip FEMA where a non-resident shareholder exists; never advise on the Government route beyond flagging it.
- Do not treat OPC, Section 8 or LLP as interchangeable with a private company for investors — say what each cannot do.
- Do not compute deadlines from an assumed incorporation date; ask for the certificate date.
- MCA V3 forms, help kits and fee tables change — say "as of [date], verify on mca.gov.in" when quoting them.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/entity-comparison.md](references/entity-comparison.md) — side-by-side table of the forms (liability, minimum people, capital, compliance load, funding, conversion) and the post-incorporation checklist with sections. Read before the recommendation.
- [scripts/incorporation_deadlines.py](scripts/incorporation_deadlines.py) — post-incorporation deadline calculator; `--json` for structured output.
