---
name: consumer-complaint-cpa-2019
description: >
  Audits and drafts complaints before the District, State and National Consumer Commissions under
  the Consumer Protection Act, 2019, including e-Daakhil filing. Runs the "consumer" test first,
  picks the forum from the consideration paid (not the compensation claimed), fixes territorial
  jurisdiction (including where the complainant lives or works), computes the two-year limitation,
  maps provable relief under s.39, checks parallel forums (RERA, arbitration, ombudsman) and
  produces the complaint with verification, affidavit and document list. Use whenever a user
  mentions a consumer complaint, consumer court/forum/commission, e-Daakhil, "deficiency in
  service", "defective product", "refund nahi mil raha", a builder/airline/insurer/bank/hospital/
  e-commerce seller who will not refund or repair, misleading ads, or an appeal from a consumer
  commission order. Not for business-to-business purchases for commercial purposes, for employment
  grievances, or for advocates' services — say so and route elsewhere.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Consumer Protection
  jurisdiction: IN
  states: all
  language: en
---

# Consumer Complaint (Consumer Protection Act, 2019) Advisor

Produces an eligibility/forum/limitation memo and a filing-ready complaint for the District, State or National Consumer Disputes Redressal Commission, plus an e-Daakhil checklist. For advocates and for consumers filing themselves.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate must review every interpretation, citation and draft before it is relied on, sent or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the State/UT and district: the Commission's address, its working portal and local practice directions differ. If the opposite party is abroad with no Indian presence, say that service and enforcement will be the real problem before drafting anything.

## Verify before relying

Check and record the date checked:

- Act text, especially ss.2(7), 2(10), 2(11), 2(16), 2(46), 2(47), 34, 35, 37, 38, 39, 41, 51, 58, 67, 69, 71, 72, 82–87, 89, 100: [India Code — Consumer Protection Act, 2019](https://www.indiacode.gov.in/).
- **Pecuniary limits**: the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 — District up to ₹50 lakh; State above ₹50 lakh up to ₹2 crore; National above ₹2 crore — measured by the **value of the goods or services paid as consideration** (s.34(1), s.47(1), s.58(1)), not by the compensation claimed. The Central Government can revise these by rule; confirm on [e-Gazette](https://egazette.gov.in/) or the [Department of Consumer Affairs](https://consumeraffairs.nic.in/) before stating them.
- **Fees**: the Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Schedule — nil for claims up to ₹5 lakh, then slabs by value. Read the Schedule as in force; do not quote slab amounts from memory.
- Filing: [e-Daakhil](https://edaakhil.nic.in/) (document formats, fee payment, which Commissions accept e-filing); [confonet.nic.in](https://confonet.nic.in/) for case status.
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); NCDRC orders on [ncdrc.nic.in](https://ncdrc.nic.in/). See [references/case-law.md](references/case-law.md).

If no browsing tool is available, say figures come from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones first, together, in plain language.

**Blocking:**
- Who bought what from whom, for how much, and when (invoice, booking, policy, agreement, order confirmation)
- What went wrong and when the user first knew (this fixes the cause of action and the two-year clock under s.69)
- What was paid in total (this fixes the forum — s.34(1))
- Where the complainant lives/works, where the opposite party has an office or branch, and where the transaction happened (s.34(2))
- Whether the purchase was for personal use or for a business, and if for a business, whether it was for the user's own livelihood by self-employment (s.2(7) Explanation)

**Nice to have:** complaint emails, chat logs, call recordings, photos, repair reports, any legal notice and its reply, any arbitration clause, RERA registration, ombudsman complaint, insurance policy wording, medical records, the ad or listing relied on.

## Method

1. **Consumer test first (s.2(7)).** A consumer buys goods or hires services for consideration (paid, promised, or partly paid), including online, teleshopping, direct selling and multi-level marketing; a beneficiary with the buyer's approval also qualifies. Excluded: goods bought for **resale** or for a **commercial purpose**, unless used exclusively for earning a livelihood by self-employment (*Laxmi Engineering*). Commercial purpose turns on the dominant intention and close nexus with profit-generation, not on whether the buyer is a company (*Lilavati Kirtilal Mehta*, *Harsolia Motors* — insurance for a business is still "consumer"; *Shrikant G. Mantri* — an overdraft for business is not). If the user fails the test, say so plainly and route to a civil suit, commercial suit, arbitration or regulator. Also check the service is "service" at all: advocates' services are **not** (*Bar of Indian Lawyers v. D.K. Gandhi*); education by universities/boards has been held not to be a service by the Supreme Court in *Maharshi Dayanand University* and the point remains contested at the NCDRC — flag it rather than assume coverage; medical services are covered except where entirely free (*V.P. Shantha*).

2. **Classify the grievance** with the statutory label, because relief under s.39 tracks it: **defect** in goods (s.2(10)), **deficiency** in service (s.2(11), including negligence, withholding material information), **unfair trade practice** (s.2(47), including misleading advertisement under s.2(28) and refusing refunds for returned goods), **unfair contract** (s.2(46), one-sided terms — *IREO Grace Realtech*), **product liability** (ss.82–87: manufacturer, product service provider, seller; note the s.87 exceptions for misuse, alteration and adequate warnings), **restrictive trade practice**, or spurious goods.

3. **Forum from consideration paid, with the bundled script:**
   ```bash
   python3 scripts/consumer_forum.py --consideration 1250000 --cause-date YYYY-MM-DD [--today YYYY-MM-DD]
   ```
   It gives the Commission, the fee note, the s.69 limitation date and the appeal windows. Jurisdiction is on the consideration **paid**, so the compensation figure must not be inflated to reach a higher forum (*Pyaridevi Chabiraj Steels*). Where consideration is paid in instalments or partly, state the figure relied on and why.

4. **Territorial choice (s.34(2)).** The complaint lies where the opposite party resides, carries on business, has a branch, or personally works for gain; where the cause of action arose wholly or in part; or — new in 2019 — **where the complainant resides or personally works for gain** (s.34(2)(d)). Pick the Commission most convenient to the complainant and least likely to invite a transfer fight; state the clause relied on in the jurisdiction paragraph.

5. **Limitation (s.69).** Two years from the date the cause of action arose; condonation is available for sufficient cause with reasons recorded. A continuing cause (ongoing non-delivery, repeated breakdowns, a pending refund) keeps the clock alive, but do not rely on "continuing" loosely — identify the first date of deficiency and the last. If the complaint is late, draft a separate condonation application that explains each stretch of delay.

6. **Who may complain (s.35).** The consumer; a recognised consumer association; one or more consumers with the same interest, with the Commission's leave under s.35(1)(c) read with s.38(11) (Order I Rule 8 CPC — *Ambrish Kumar Shukla* for flat-buyers); the Central/State Government; the CCPA; and the legal heir or representative of a deceased consumer (s.2(5)). For a company or firm complainant, attach the board resolution/authority letter.

7. **Pre-complaint notice.** Not mandatory under the Act, but a short notice with a 15-day window usually produces the admission or refusal you need, fixes the date for interest, and makes the case for costs and punitive damages. Draft it unless time is short.

8. **Relief mapping (s.39).** For each head — removal of the defect, replacement, refund of price/charges, compensation for loss or injury including mental agony and harassment (*Lucknow Development Authority*), punitive damages, discontinuance of the unfair practice, withdrawal of hazardous goods, corrective advertisement, costs, interest — tie the amount to a document or a reasoned computation. Separate the refund (fixed) from compensation (justified) from costs. Over-claiming invites rejection and feeds the respondent's "commercial litigant" argument.

9. **Parallel forums and the s.100 rule.** The Act is in addition to other laws (s.100). A homebuyer may choose the consumer forum despite RERA (*Experion Developers*, *Imperia Structures*); an arbitration clause does not oust the Commission (*Emaar MGF v. Aftab Singh*); banking and insurance complainants may first use the RBI Integrated Ombudsman or the Insurance Ombudsman (cheap, fast, award up to the scheme ceiling) and still come to the Commission. Tell the user which route is faster for their facts, and disclose any parallel proceeding in the complaint — concealing one is fatal to credibility and can cost the case.

10. **Mediation posture (s.37).** The Commission may refer the parties to its mediation cell at admission or later with consent (Consumer Protection (Mediation) Rules, 2020); a settlement is recorded as an order. Advise whether to consent: good for refund-plus-interest cases, poor for product-liability or precedent-seeking cases.

11. **Procedure and timelines (s.38).** The opposite party gets 30 days (extendable by 15) to reply; the Commission aims to decide within three months (five where testing is needed) — rarely met, so set expectations. Evidence is by affidavit. Orders are enforced as decrees of a civil court (s.71); non-compliance is punishable with imprisonment and fine (s.72). Appeals: District → State within 45 days with a deposit of 50% of the amount ordered (s.41); State → National within 45 days with the same deposit (s.51); National (original jurisdiction only) → Supreme Court within 30 days (s.67). Revision to the National Commission lies under s.58(1)(b) for jurisdictional error.

## Output

```
# Consumer complaint — [Complainant] v. [Opposite party] — [District/State/National Commission, place]
## Summary (plain language: are you a consumer, which forum, deadline, what you can realistically get)
## Eligibility (s.2(7) test, with the facts relied on and the case that governs the hard point)
## Forum, territorial jurisdiction and fee (output of consumer_forum.py + the s.34(2) clause relied on)
## Limitation (cause-of-action date, two-year deadline, condonation if needed)
## Draft pre-complaint notice (unless already sent)
## Draft complaint: cause title; memo of parties; jurisdiction paragraph; facts in dated paragraphs with document references; defect/deficiency/UTP/unfair contract/product liability pleaded with the section; cause of action and limitation; relief under s.39 with quantification; interim relief if any; verification; affidavit; list of documents; s.35 authority if entity
## e-Daakhil filing checklist (index, memo of parties, complaint, affidavit, documents as PDFs, fee receipt, ID/authority, condonation application if late)
## Parallel forums and mediation advice
## Defects and documents still needed
## Sources checked (section, source, date checked; cases by neutral citation)
```

## Guardrails

- Do not inflate compensation to reach a higher forum; jurisdiction follows consideration paid.
- Do not assume advocates', educational institutions' or free hospitals' services are covered; cite the contrary case law and let the user decide.
- Do not quote State or National Commission fee slabs from memory — nil up to ₹5 lakh is the only figure to state without reading the Schedule.
- Do not conceal a parallel arbitration, RERA, ombudsman, civil or criminal proceeding; plead it.
- Do not fabricate dates, invoices, complaints made, or the content of a listing/advertisement.
- Keep the facts chronological and each paragraph tied to a document; Commissions decide on affidavits and paper.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/case-law.md](references/case-law.md) — Supreme Court and NCDRC decisions by issue (consumer test, commercial purpose, services covered, pecuniary jurisdiction, builders and RERA, arbitration clauses, class complaints, compensation). Read it before the eligibility section.
- [scripts/consumer_forum.py](scripts/consumer_forum.py) — forum, fee note, limitation and appeal-window calculator; `--json` for machine-readable output.
