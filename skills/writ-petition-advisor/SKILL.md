---
name: writ-petition-advisor
description: >
  Decides whether a writ petition lies in India and builds the petition skeleton: Article 32 vs 226
  vs 227, which of the five writs (habeas corpus, mandamus, certiorari, prohibition, quo warranto),
  whether the respondent is "State" under Article 12 or a private body performing a public duty,
  territorial jurisdiction under Article 226(2), the alternative-remedy rule and its exceptions,
  tribunal routes, laches, locus and PIL filters, interim relief and the SLP route. Produces a
  maintainability memo, a decision table, a synopsis/list of dates and lettered grounds tied to
  decisions — or, when a writ is the wrong tool, the statutory remedy and its deadline. Use whenever
  a user mentions a writ, Article 226/32/227, "high court mein petition", mandamus, certiorari,
  habeas corpus, quo warranto, PIL, challenging a government order/notification/tender/demand, an
  authority not acting, illegal detention, or asks "can I go to the High Court directly".
  Not for statutory appeals or criminal quashing (BNSS s.528).
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Public Law & RTI
  jurisdiction: IN
  states: all
  language: en
---

# Writ Petition Advisor

Produces a maintainability memo, the decision table (Article → writ → court → alternative remedy → delay → relief), and a draft skeleton — synopsis and list of dates, lettered grounds, prayer and interim prayer — for a writ before a High Court or the Supreme Court. For advocates, and for litigants deciding whether the constitutional route is open to them.

> **Not legal advice.** This is a research and drafting aid under Indian law. Writ jurisdiction is discretionary and every High Court has its own rules; a qualified advocate must review every interpretation and draft before it is filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian constitutional remedies only. Identify the **High Court** (and Bench — many High Courts sit at more than one seat with territorial allocation) from where the cause of action arose in whole or part and where the respondent authority is (Art. 226(2)), and read that High Court's **Writ Rules / Rules of Practice** for format, affidavit, court fee and the PIL rules — they differ. If the grievance is against a foreign State, a foreign court or is governed by foreign law, stop and say so.

## Verify before relying

- Constitution of India, Articles 12, 13, 14, 19, 21, 32, 136, 226, 227, 323A/323B: [India Code](https://www.indiacode.gov.in/) (the Constitution is hosted there).
- The High Court's writ rules, PIL rules, court-fee schedule and e-filing practice: the High Court's website (search "<High Court> writ rules"); the Supreme Court Rules, 2013 for Art. 32 and SLPs (Order XXXVIII for Art. 32; Order XXI for SLP — limitation **90 days** from the impugned judgment, longer for certified-copy time — verify on [sci.gov.in](https://www.sci.gov.in/)).
- Controlling decisions by neutral citation on sci.gov.in; summarised in [references/case-law.md](references/case-law.md). Alternative-remedy law moved in 2024 (*PHR Invent*, 2024 INSC 297) — read it before saying a writ lies despite a statutory appeal.
- Where a tribunal exists (CAT, SAT, DRT/DRAT, NCLT/NCLAT, GSTAT, Armed Forces Tribunal), the governing statute and *L. Chandra Kumar* decide the route.

If no browsing tool is available, say the positions are from the skill's version date and must be verified.

## Required inputs

**Blocking (no memo without them):**
- The impugned act: what was done or not done, by whom, when; the order/notification/tender/demand with its date (and the date the user received it)
- The right asserted: fundamental right (which Article), statutory right, or a legal duty owed to the user
- The respondent's identity: Government, statutory body, PSU, university, bank, private company, society — and the control/funding/function facts if it is not obviously State
- What the user wants: quash the order, direct action, release from detention, stop an authority, oust an office-holder, declare a provision invalid
- Any statutory appeal/revision/representation available, whether it was used, and its deadline

**Nice to have:** prior representations and replies, earlier litigation on the same cause (res judicata/successive petitions), urgency facts (demolition, auction, deportation, exam date), the user's standing (aggrieved person vs public-spirited PIL), documents list.

## Method

1. **Right and duty first.** Name the right infringed or the duty breached, with its source (Article, section, rule, binding policy, legitimate expectation). No identified right → no writ; say so and look for the civil or statutory route instead.

2. **Respondent — is it "State" (Art. 12) or does it perform a public duty?** Apply the *Pradeep Kumar Biswas* / *Ajay Hasia* test: deep and pervasive functional, financial and administrative control by Government (universities, PSUs, nationalised banks, statutory bodies — yes; BCCI — not State, but its public functions are amenable to Art. 226 (*Zee Telefilms*); private schools, hospitals, companies — only for the public duty they perform, e.g. admissions/affiliation, fee regulation, statutory obligations (*Andi Mukta*, *Janet Jeyapaul*, *St. Mary's Education Society*, 2022)). A purely private employment or contractual dispute with a private body is not writ territory (route to civil suit/arbitration/labour forum).

3. **Choose the Article.** Art. 32: fundamental rights only, Supreme Court, itself a fundamental right — but the Court routinely relegates to the High Court unless the issue is national or the Court's intervention is warranted; Art. 226: any legal right "and for any other purpose", the High Court — the default; Art. 227: supervisory control over courts and tribunals, used to correct jurisdictional error in orders of subordinate courts (no Art. 226 writ lies against a civil court's judicial order — *Radhey Shyam v. Chhabi Nath*, 2015). Apply [references/case-law.md](references/case-law.md) § "Which Article".

4. **Choose the writ** and check its elements: *habeas corpus* — detention without legal authority, filed by anyone, listed urgently, the detaining authority must justify; *mandamus* — a public legal duty, a demand and a refusal (or deemed refusal), no discretion being substituted; *certiorari* — an order already passed, by a body with a duty to act judicially/fairly, suffering lack or excess of jurisdiction, error of law apparent on the face, or breach of natural justice; *prohibition* — before the order, to stop proceedings without jurisdiction; *quo warranto* — a public office created by statute/Constitution, held without qualification, any person may apply. Pure declaratory relief or damages generally belong elsewhere.

5. **Alternative remedy.** State the statutory remedy (appeal/revision/representation/tribunal), its period and whether it has expired. The High Court ordinarily does not entertain a writ where an efficacious remedy exists (*PHR Invent*, 2024; *Thansingh Nathmal*), especially in tax, SARFAESI/recovery and service matters; the exceptions are breach of fundamental rights, violation of natural justice, lack of jurisdiction, and challenge to the vires of a provision (*Whirlpool*, 1998; *Harbanslal Sahnia*; *Radha Krishan Industries*, 2021; *Godrej Sara Lee*, 2023). A writ cannot be used to get around a limitation that has run on the statutory remedy (*Assistant Commissioner v. Glaxo Smith Kline*, 2020). Service matters of Central employees go to CAT first (*L. Chandra Kumar*, 1997; division bench review of CAT orders). Contract matters against the State lie only where the State acts arbitrarily or in breach of public law duties (*ABL International*, 2004) and not on disputed facts.

6. **Territorial jurisdiction, delay, locus, res judicata.** Art. 226(2): the High Court where the cause of action arises wholly or in part (*Kusum Ingots*, *Nawal Kishore Sharma*) — a bare office of the respondent elsewhere is not enough; pick the Bench by the High Court's allocation. Laches: no fixed limitation, but delay unexplained defeats discretion (*Chennai Metropolitan Water Supply v. T.T. Murali Babu*, 2014) — compute how long since the order and the last representation. Locus: an aggrieved person for an ordinary writ; a bona fide public-spirited petitioner with no private interest for PIL, subject to the *Balwant Singh Chaufal* (2010) filters and the High Court's PIL rules (affidavit of credentials, no personal gain, prior representation). Res judicata and constructive res judicata bar a second writ on the same cause; disclose earlier petitions.

7. **Relief and interim relief.** Match the prayer to the writ (quash + direct reconsideration; direct to act within a time; declare; release). Interim relief needs a prima facie case, balance of convenience and irreparable harm, plus the specific equity (stay of demolition/auction/adverse action, status quo, no coercive steps); courts are slow to stay recoveries without deposit and refuse to stay examinations/elections mid-process. State what undertakings the petitioner should offer.

8. **Build the draft** per the High Court's rules — typically: synopsis and list of dates (one page, reverse-chronological facts with dates and annexure references); memo of parties with the right officer impleaded (Secretary of the department, the authority that passed the order, the beneficiary of the order as a necessary party); petition under Art. 226 (and 227 where supervisory relief is sought) — facts in numbered paragraphs tied to annexures, grounds lettered (A, B, C…) each stating the legal proposition, the decision supporting it and the facts applying it, a paragraph on no alternative efficacious remedy / why the exception applies, on delay, on no earlier petition, and on territorial jurisdiction; prayer (main and interim, numbered); affidavit in verification; interim application; annexures indexed with page numbers; vakalatnama; court fee per the schedule. For Art. 32, follow Supreme Court Rules Order XXXVIII (statement of the fundamental right, why the Supreme Court and not the High Court).

9. **When the writ is wrong**, say so plainly and give the right route with its deadline: statutory appeal (period, forum, pre-deposit), tribunal, civil suit (limitation), consumer forum, labour forum, or an RTI/representation first to create the demand-and-refusal for a later mandamus.

## Output

```
# Writ — [Petitioner] v. [Respondent] — [High Court/Bench | Supreme Court]
## Maintainability (plain language: does a writ lie, which one, biggest risk)
## Decision table (right/duty → respondent is State / public duty → Article → writ → court and Bench → alternative remedy and exception → delay → locus → relief)
## Article 12 analysis (only where the respondent is not obviously State)
## Synopsis and list of dates (draft)
## Grounds (lettered; proposition → authority → application to facts)
## Prayer and interim prayer (draft); undertakings to offer
## Documents and annexures needed; High Court rule items to verify (format, court fee, PIL rules)
## If a writ is not the route: the statutory remedy, forum and deadline
## Sources checked (Articles, rules, decisions by neutral citation; date checked)
```

## Guardrails

- Never recommend a writ to bypass a limitation that has expired on the statutory remedy without flagging *PHR Invent* and *Glaxo Smith Kline*; say the petition is likely to be dismissed on maintainability.
- Never call a private body "State" without the functional test; "performs a public duty" is a narrower, function-specific finding.
- Never draft grounds without an identified legal right and the duty breached; "unfair" is not a ground.
- Never promise urgent listing, a stay, or an outcome; state the standard and the usual practice.
- Disclose every earlier petition or proceeding on the same cause; suppression is fatal and attracts costs.
- Verify the specific High Court's rules, court fee and Bench allocation before stating them.
- Do not reproduce long constitutional or statutory text; cite and summarise.

## References

- [references/case-law.md](references/case-law.md) — controlling decisions by issue: which Article, Art. 12 and public duty, each writ's elements, alternative remedy and its exceptions, tribunals, territorial jurisdiction, delay, PIL, interim relief, SLP. Read it before the maintainability section.
- [references/petition-structure.md](references/petition-structure.md) — the generic High Court writ format, the Art. 32 format, the PIL additions, and a checklist of High Court-specific items to verify.
