---
name: cheque-bounce-s138-advisor
description: >
  Audits a dishonoured-cheque matter under section 138 of the Negotiable Instruments Act, 1881 and
  drafts the statutory demand notice, the complaint, or the reply. Computes every deadline in the
  chain (presentment, 30-day notice, 15-day payment window, one-month complaint limitation),
  fixes territorial jurisdiction under s.142(2), checks s.141 company-officer liability, and
  flags defects before anything is sent or filed. Use whenever a user mentions a bounced or
  dishonoured cheque, "cheque bounce", "cheque return memo", "insufficient funds", "138 notice",
  "NI Act case", "cheque bounce ho gaya", or wants to reply to a s.138 notice they received.
  Not for cheque fraud/forgery prosecutions under the BNS or for civil recovery suits alone —
  route those elsewhere and say so.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Criminal Law
  jurisdiction: IN
  states: all
  language: en
---

# Cheque Bounce (s.138 NI Act) Advisor

Produces a maintainability audit, deadline table and draft (notice, complaint or reply) for a dishonoured-cheque matter in India. Written for advocates and for payees or drawers handling the first steps themselves.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate must review every interpretation, citation and draft before it is relied on, sent or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the State/UT: court fees, process fees, local Criminal Rules of Practice and the presentment bank's location all turn on it. If the cheque was drawn on a foreign bank or the dispute is governed by foreign law, stop and say so.

## Verify before relying

Check these before stating a section, period or figure as current, and record the date checked:

- Sections 138–148 NI Act, 1881 (as amended 2002, 2015, 2018): [India Code](https://www.indiacode.gov.in/)
- Procedure is now the **BNSS, 2023** (in force 1 July 2024): complaint under s.223 (was CrPC s.200), summons s.227, summary trial s.283–288. BNSS s.223 adds a pre-cognizance hearing of the accused — check the current text and local practice.
- Controlling decisions: [sci.gov.in](https://www.sci.gov.in/) by neutral citation. The most-cited ones are summarised in [references/case-law.md](references/case-law.md); read it before writing the analysis.

If no browsing tool is available, state that figures come from the skill's version date and must be verified.

## Which mode?

Ask one question first if it is not obvious from the prompt:

| User is | Mode | Output |
|---|---|---|
| Payee, notice not yet sent | **Notice** | Deadline table + draft demand notice + dispatch checklist |
| Payee, notice sent, 15 days over, unpaid | **Complaint** | Maintainability audit + draft complaint + filing index |
| Drawer who received a notice or summons | **Defence** | Defect analysis + draft reply / defence strategy + settlement options |
| Anyone, unsure of dates | **Timeline** | Deadline table only, with what is still needed |

## Required inputs

Ask for the blocking ones first, together, in plain language.

**Blocking (no draft without them — produce a defect list instead):**
- Cheque: number, date, amount, drawer, drawee bank and branch, payee name as printed
- Return memo: date, reason code/wording, and the **date the payee received it** (notice runs from receipt of information, not the memo date)
- Underlying debt or liability: what it was for, when it arose, any written contract/invoice/loan record
- Payee's bank branch where the cheque was presented (this fixes jurisdiction under s.142(2))
- In Complaint/Defence mode: notice date, mode of dispatch, tracking/AD-card evidence, date of service or return endorsement, and whether any payment was made within 15 days

**Nice to have:** prior presentations and dishonours, part-payments, WhatsApp/email admissions, the drawer's role if a company/firm signed, any parallel civil suit, arbitration or insolvency.

## Method

1. **Confirm the ingredients of s.138**, each tied to a document: (a) a cheque drawn on an account maintained by the drawer; (b) for discharge of a legally enforceable debt or liability (wholly or partly); (c) presented within three months of its date (RBI validity period) — s.138 proviso (a); (d) returned unpaid for insufficient funds / exceeds arrangement — courts treat "account closed", "payment stopped" and "signature mismatch" as within s.138 (see case-law file); (e) written demand within 30 days of receipt of information of dishonour — proviso (b); (f) failure to pay within 15 days of receipt of notice — proviso (c). A missing ingredient is fatal; say which one and whether it can still be cured (e.g. a fresh presentment within validity restarts the chain — *MSR Leathers*).

2. **Run the timeline with the bundled calculator** and paste its table into the output:
   ```bash
   python3 scripts/s138_timeline.py --cheque-date YYYY-MM-DD --memo-received YYYY-MM-DD [--notice-sent YYYY-MM-DD] [--notice-served YYYY-MM-DD] [--today YYYY-MM-DD]
   ```
   It computes the presentment deadline, the 30-day notice deadline, the 15-day payment window, the date the cause of action arises (the day after the window closes), and the one-month complaint limitation under s.142(1)(b), excluding the day the cause of action arose (*Econ Antri*). If the script is unavailable, compute by hand, show every step, and mark the result unverified. Never estimate a limitation date silently.

3. **Fix territorial jurisdiction under s.142(2)** (2015 amendment, retrospective by s.142A): if the cheque was presented through the payee's account, the court whose jurisdiction covers **the payee's bank branch**; if presented across the counter, the court covering the drawee bank branch. The drawer's address and the place of the transaction are irrelevant. Where multiple cheques were presented at different branches, s.142A(2) consolidates later complaints before the first court.

4. **Service of notice.** Dispatch to the drawer's correct address by registered post/speed post (keep the receipt and tracking) is deemed service under s.27 General Clauses Act and *C.C. Alavi Haji*; "refused" and "left"/"unclaimed" endorsements generally count as service, "addressee not found" generally does not. Email/WhatsApp is advisable **in addition**, not instead. In Defence mode, a drawer who says they never received the notice can still pay within 15 days of receiving the summons and defeat the complaint (*Alavi Haji*).

5. **Notice content.** The notice must demand **the cheque amount** distinctly; interest, costs or damages may be added but must be separable (*Suman Sethi*). State the cheque particulars, the debt, the presentment and dishonour, the demand, and the 15-day consequence. Do not threaten anything beyond lawful proceedings. Keep it to one or two pages.

6. **Parties and s.141.** For a company, LLP or firm, implead the entity *and* only those individuals for whom you can plead specific facts showing they were in charge of and responsible for the conduct of its business when the offence was committed (*S.M.S. Pharmaceuticals*). The signatory is liable under s.141(2) on the signature alone; other directors are not liable by title. A sole proprietorship is the proprietor. Do not array people to apply pressure.

7. **Complaint structure** (Complaint mode): cause title before the Judicial Magistrate First Class / Metropolitan Magistrate with jurisdiction; parties; chronological facts with document references; the legally enforceable debt; presentment, dishonour, notice, service, non-payment; jurisdiction paragraph citing s.142(2); limitation paragraph with the computed dates (and a s.142(1)(b) proviso application if late, explaining each day of delay); s.141 averments if applicable; prayer (process under s.227 BNSS, conviction under s.138, compensation under s.395 BNSS up to twice the cheque amount, interim compensation under s.143A); verification and affidavit of evidence under s.145 NI Act; list of documents; list of witnesses. A complaint filed before the 15 days expire is premature and cannot be cured (*Yogendra Pratap Singh*) — never draft one with dates that make it premature.

8. **Defence mode.** Test the chain for the drawer: was presentment within validity, was the notice within 30 days of *receipt*, was the cheque amount demanded, was the complaint within one month, is the forum right, is the debt legally enforceable (time-barred debt, security cheque with no crystallised liability, blank cheque filled later — *Bir Singh*), can the s.139 presumption be rebutted on a preponderance of probabilities (*Rangappa*)? Lay out settlement options: s.147 compounding is available at any stage with graded costs (*Damodar S. Prabhu*); interim compensation of up to 20% may be ordered under s.143A; an appellate court may require a deposit under s.148.

9. **Flag parallel tracks.** A civil summary suit under Order XXXVII CPC, arbitration, IBC proceedings or SARFAESI action may run alongside; a settlement in one should be disclosed in the other. Note that cheque forgery or a stolen cheque is a BNS matter (s.336/s.338 forgery, s.318 cheating), not s.138.

## Output

```
# s.138 NI Act — [Notice | Complaint | Defence | Timeline] — [Payee] v. [Drawer]
## Summary (plain language, 3–5 lines: maintainable or not, next deadline, biggest risk)
## Facts relied on (as supplied, with dates and the document for each)
## Deadline table (output of s138_timeline.py, with today's status for each date)
## Ingredients check (s.138 (a)–(f) → document → status: proven / pleaded / missing)
## Jurisdiction (s.142(2) analysis with the branch relied on)
## Parties and s.141 liability (if an entity is involved)
## Draft [notice | complaint | reply]
## Defects and documents still needed
## Next steps (what to do, by when, who does it)
## Sources checked (section, source, date checked; cases by neutral citation)
```

Keep the summary readable by a non-lawyer. Put the legal detail below it.

## Guardrails

- Do not fabricate receipt, service, the debt, authority to sign, part-payments or dates. Where the user cannot prove service, say the complaint is at risk rather than assuming deemed service.
- Do not array directors, partners or family members without role-specific facts.
- Do not demand amounts the user cannot substantiate, and never draft threats beyond lawful proceedings.
- Do not present the s.139 presumption as removing the need to plead the debt and the chain of dates.
- Distinguish a **security cheque** (liability must have crystallised when presented) from a cheque for an admitted debt, and say which the facts show.
- If the matter is time-barred and no sufficient cause exists, say so plainly and point to the civil recovery route rather than drafting a hopeless complaint.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/case-law.md](references/case-law.md) — the controlling Supreme Court decisions by issue (presumption, notice, service, jurisdiction, premature complaint, s.141, compounding, interim compensation). Read it before the analysis section.
- [scripts/s138_timeline.py](scripts/s138_timeline.py) — deadline calculator; `--json` for machine-readable output.
