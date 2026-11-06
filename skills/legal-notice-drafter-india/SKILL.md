---
name: legal-notice-drafter-india
description: >
  Drafts and audits legal notices and replies under Indian practice — demand notices, breach and
  cease-and-desist letters, and the statutory notices with mandatory periods and contents: s.80 CPC
  (two months before suing the Government), s.106 Transfer of Property Act (notice to quit), s.21
  Arbitration Act (invoking arbitration), s.12A Commercial Courts Act (pre-institution mediation),
  MSMED Act s.18 (Samadhaan), IBC s.8 (operational creditor demand), SARFAESI s.13(2), and
  employment show-cause/termination notices. Classifies the notice, checks who may sign, states the
  breach and a quantified demand with a deadline, plans service, and tells the user what happens
  next. Use whenever a user asks for a "legal notice", "notice bhejna hai", "reply to legal notice",
  "demand letter", "cease and desist", "notice before suit", "notice to tenant", "notice to
  government department", or asks whether a notice is required before suing. Routes
  cheque-bounce notices to cheque-bounce-s138-advisor rather than redrafting them.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Legal Drafting
  jurisdiction: IN
  states: all
  language: en
---

# Legal Notice Drafter (India)

Produces a classified, statute-checked legal notice or reply, with a service plan and a what-happens-next timeline. For advocates, in-house teams and litigants sending a first notice themselves.

> **Not legal advice.** This is a drafting aid under Indian law. A qualified advocate must review every notice or reply before it is sent; where a statute makes the notice a precondition to suit, a defective notice can cost the case. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the State: tenancy notices interact with State Rent Control Acts, shops-and-establishments notice periods are State-specific, and court fees and local rules vary. If the governing law is foreign or unclear, stop and say so.

## Verify before relying

Mandatory periods and contents are the part people get wrong. Before stating one:

- Statute text: [India Code](https://www.indiacode.nic.in/) — CPC s.80; TPA s.106; Arbitration and Conciliation Act ss.11, 21; Commercial Courts Act s.12A; MSMED Act ss.15–19; IBC ss.8–9; SARFAESI ss.13, 17; Industrial Disputes Act s.25F / Industrial Relations Code, 2020 (check commencement on [e-Gazette](https://egazette.gov.in/)).
- Decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/).
- The statutes with mandatory notices are tabulated in [references/statutory-notices.md](references/statutory-notices.md) — read it whenever the notice is or might be statutory. For a statute not in the table, do not state a period from memory; verify on India Code first.

If no browsing tool is available, say the periods come from the skill's version date and must be verified.

## Required inputs

**Blocking (no draft without them — produce a checklist instead):**
- Who is sending, who is receiving (full names, addresses, legal status — individual, firm, company, Government department/officer)
- The relationship and the documents behind it (contract, invoice, lease, loan, employment letter, agreement)
- The breach or grievance: what, when, how much — with dates and the document for each fact
- What the sender wants (pay ₹X, vacate, stop doing Y, perform Z, retract) and by when
- Whether the matter is one with a **statutory** notice requirement (Government defendant, tenancy, arbitration clause, commercial dispute above the specified value, MSME supplier, operational debt, secured loan, employment)

**Nice to have:** prior correspondence, any earlier notice and its service proof, the limitation position (when did the cause of action arise), whether the sender is represented by an advocate, the preferred tone.

## Method

1. **Classify the notice**: *statutory-mandatory* (a precondition to the remedy — s.80 CPC, s.106 TPA, s.21 Arbitration, s.12A Commercial Courts, s.8 IBC, s.13(2) SARFAESI, retrenchment notices), *statutory-optional* (MSME Samadhaan reference, consumer pre-complaint notice, RBI Ombudsman complaint to the bank first), or *tactical* (demand, cease-and-desist, breach, defamation). The class decides what must be in it and what happens if it is wrong. For a dishonoured cheque, stop and use **cheque-bounce-s138-advisor** — its 30-day/15-day chain is unforgiving.

2. **Check standing and the signatory.** The notice is sent by the person with the right (the creditor, the landlord, the party to the arbitration clause, the operational creditor — not a group company or a director in a personal capacity) or by an advocate "under instructions from and on behalf of" that person. A company acts through an authorised signatory under a board resolution; a firm through a partner; a Government department through the competent officer. An advocate's notice goes on letterhead and must not contain statements the advocate knows to be false (Bar Council of India Rules, Part VI, Chapter II).

3. **Lay out the facts, dated and documented**, in the order they happened. Each paragraph: date, event, document reference. Separate what the client told you from what the documents show; if a date or amount is not supported, ask rather than fill it in.

4. **State the breach with its basis**: the clause of the contract, the section of the statute, or the duty in law. Quantify: principal, interest (contractual rate or, absent one, a defensible statutory/commercial rate — say which), and any other heads. A demand that is specific and separable survives scrutiny; a vague "pay all amounts due" does not.

5. **Make the demand, fix the deadline, state the consequence.** Use the statutory period where there is one (two months under s.80 CPC; 15 days/6 months under s.106 TPA; 10 days under s.8 IBC; 60 days under s.13(2) SARFAESI); otherwise a reasonable period (commonly 7–30 days). The consequence is the lawful remedy — civil suit, arbitration, complaint to the forum, insolvency application — never a threat of criminal prosecution to extract a civil payment (that is extortion/criminal-intimidation territory under BNS ss.308 and 351, and professional misconduct for an advocate). If criminal conduct genuinely exists, say that the sender reserves the right to initiate appropriate proceedings, without using it as a lever.

6. **Service plan.** Registered post with acknowledgement due **and** speed post to the registered/last-known address (s.27 General Clauses Act gives a presumption of service for correctly addressed, prepaid registered post); email to the address used in dealings; WhatsApp as a supplementary channel (some courts accept the blue ticks as proof, none treat it as primary); courier alone is weak. Keep the postal receipt, tracking printout, returned envelope and email headers — the complaint or plaint will need them. For a Government department, send to the Secretary of the department concerned (and the Collector for a district matter) as s.80(1) requires, and keep the receipt.

7. **Limitation does not pause.** Sending a notice does not stop time running on the underlying claim, except where the statute excludes the notice period — s.15(2) Limitation Act excludes the s.80 CPC period; s.12A(3) Commercial Courts Act excludes the mediation period; s.21 Arbitration fixes the commencement date. Compute the limitation position before fixing the deadline and say when the suit/arbitration/complaint must be filed by.

8. **Replies.** Admit, deny or explain each paragraph (an unanswered paragraph can be read as admitted); raise the threshold defects first — no standing, wrong signatory, wrong period, wrong forum, time-barred claim, no privity; state the sender's own breaches; keep anything settlement-related **without prejudice** in a separate paragraph or letter; reserve rights; make no admissions of liability or quantum; do not respond to a defamatory notice with defamation.

9. **Employment and defamation notices need a second look.** Retrenchment of a workman with a year's continuous service requires one month's notice or pay in lieu plus compensation (ID Act s.25F; permission regimes for larger establishments; the Industrial Relations Code, 2020 — verify its commencement — re-enacts this with a higher permission threshold); dismissal for misconduct needs a charge-sheet, enquiry and reasoned order under the standing orders and natural justice; shops-and-establishments notice periods are State-specific. A defamation cease-and-desist invites a counter-notice and publicity; say so before drafting it.

## Output

```
# Legal notice — [type] — [Sender] to [Recipient]
## Classification (statutory-mandatory / statutory-optional / tactical; statute and section if any)
## Requirements checklist (period, contents, addressee, mode — from references/statutory-notices.md; verified on India Code on [date])
## Limitation position (cause of action date → last date to file; whether the notice period is excluded)
## Draft [notice | reply]
   [Letterhead / sender block] · [Date, reference, mode of dispatch]
   To: [recipient block]
   Subject line
   1. Introduction and authority ("under instructions from and on behalf of…")
   2–n. Facts (dated, documented)
   Breach / grievance with basis
   Demand (specific, quantified) · Deadline · Consequence
   Reservation of rights · Enclosures · Signature
## Service plan (addresses, modes, what to keep as proof)
## What happens next (timeline from dispatch: deemed service, deadline, filing window)
## Defects and open points (facts or documents still needed; risks in the recipient's likely reply)
```

For a reply, replace the draft block with para-wise responses, threshold objections, without-prejudice section and reservation of rights.

## Guardrails

- No threats of criminal prosecution, police complaints or publicity to extract a civil payment.
- No defamatory statements about the recipient or third parties; stick to facts the documents support.
- No fabricated facts, dates or amounts; no inflated interest without naming the basis.
- Never state a mandatory period or content for a statute outside the reference table from memory — verify on India Code and say so.
- Do not promise that a notice will "stop" limitation, or that it is required where it is not — say which it is.
- Do not draft a s.138 notice here; route to the cheque-bounce skill.
- Do not reproduce long statutory text; cite and summarise.

## References

- [references/statutory-notices.md](references/statutory-notices.md) — statute-by-statute table (who sends, mandatory period, contents, mode, consequence of a defective notice, verify link) and the controlling decisions. Read whenever the notice is or may be statutory.
