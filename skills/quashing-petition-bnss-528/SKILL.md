---
name: quashing-petition-bnss-528
description: >
  Audits whether an FIR, charge sheet, summoning order or criminal proceeding can be quashed by the
  High Court under BNSS s.528 (CrPC s.482 for matters pending on 1 July 2024) or Article 226, maps
  the case to the Bhajan Lal categories, separates the settlement track from the merits track, and
  drafts the petition with synopsis, list of dates, grounds, interim prayer and affidavit. Use
  whenever a user mentions quashing, "quash the FIR", "482 petition", "528 application", "FIR
  cancel karwana hai", "false FIR", "498A quashing", a civil dispute given a criminal colour, a
  compromise/settlement in a non-compoundable case, or asks whether to go to the High Court against
  a charge sheet or summons. Routes bail to bail-application-bnss and discharge/compounding to the
  trial court when those fit better. Not for appeals against conviction or revision.
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

# Quashing Petition (BNSS s.528) Advisor

Produces a maintainability memo, a ground-by-ground table, the right forum and format, and a draft quashing petition — or a clear statement that quashing is the wrong tool and what to use instead. For advocates, and for accused persons trying to understand whether a High Court petition is realistic.

> **Not legal advice.** This is a research and drafting aid under Indian law. Quashing is a discretionary, exceptional remedy and every High Court has its own rules and bench practice; a qualified advocate must review every interpretation, citation and draft before it is relied on or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only, and the forum is the **High Court of the State where the FIR is registered or the trial court sits**. Identify the State and the bench (principal seat vs. a bench — Bombay has Nagpur/Aurangabad/Goa; Allahabad has Lucknow; Madras has Madurai, etc.), because the petition's nomenclature, format, court fees and listing practice differ. If the matter is governed by foreign law, stop and say so.

## Verify before relying

Check and record the date checked:

- BNSS, 2023: s.528 (inherent powers — the text is materially the same as CrPC s.482), s.531 (proceedings pending on 1 July 2024 continue under the CrPC, so cite s.482 for those), s.173(3) (preliminary enquiry), s.35(3) (notice instead of arrest), s.218 (sanction for public servants), s.223 (pre-cognizance hearing on complaints), ss.250/262/268 (discharge), s.359 and its Table (compounding): [India Code](https://www.indiacode.gov.in/).
- The offences alleged: read each BNS section's ingredients on India Code; for IPC-era FIRs map through the **ipc-bns-section-mapper** skill.
- The High Court's criminal rules of practice and its e-filing portal for the petition's form, memo of parties, court fee, and whether a criminal writ (Art. 226) or a criminal miscellaneous application is the vehicle.
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); the controlling ones are summarised in [references/case-law.md](references/case-law.md). Read it before writing the grounds.

If no browsing tool is available, say the law is from the skill's version date and must be verified.

## Is quashing the right tool?

Answer this before anything else, because most "quash the FIR" requests are better served elsewhere:

| Situation | Better route | Why |
|---|---|---|
| Arrest is the fear, the FIR itself has substance | **bail-application-bnss** (anticipatory bail s.482 / regular s.480–483) | Courts rarely stay investigation; *Neeharika* |
| Charge sheet filed, evidence thin | Discharge before the trial court — s.250 (Sessions, within 60 days of commitment), s.262 (warrant case, within 60 days of supply of documents), s.268 | Trial court looks at the record; HC looks only at the face of the FIR/charge sheet |
| Compoundable offence, parties settled | Compounding under s.359 before the trial court | No HC petition needed |
| Non-compoundable, private dispute, genuinely settled | **Quashing on settlement** (this skill, settlement track) | *Gian Singh* / *Narinder Singh* / *Parbatbhai Aahir* |
| FIR discloses no offence even if every word is true; civil dispute dressed as crime; mala fides; second FIR on same facts; legal bar (sanction, limitation) | **Quashing on merits** (this skill) | *Bhajan Lal* categories |
| Conviction already recorded | Appeal (s.415) / revision — not quashing | s.528 is not an appeal |

## Required inputs

Ask for the blocking ones together, in plain language.

**Blocking:**
- The FIR (number, police station, date, sections) and, if filed, the charge sheet and any summoning/cognizance order — the actual documents, not a summary
- Stage: investigation / charge sheet / cognizance / charge framed / evidence begun; whether the applicant has been arrested, is on bail, or has an anticipatory-bail application pending or rejected
- The applicant's role as alleged, and their version
- Every earlier application in this matter (quashing, bail, discharge) and its result — an undisclosed earlier rejection is fatal
- For the settlement track: the settlement document, who signed it, whether the complainant/victim will file an affidavit and appear

**Nice to have:** the underlying civil documents (contract, invoices, property papers, matrimonial petitions, notices), proof of delay or mala fides (prior civil suit, prior complaints that failed, timing), sanction status for a public servant, the complainant's own admissions, medical records, CCTV or electronic records of "sterling quality".

Without the FIR text and the stage, give the route table above and stop — never draft from a paraphrase of the FIR.

## Method

1. **Fix the code and the forum.** Proceedings instituted on or after 1 July 2024 → BNSS s.528; pending on that date → CrPC s.482 (state both where the FIR straddles). Confirm each offence's BNS/IPC number and read its ingredients. Note the vehicle and title the High Court uses — Bombay "Criminal Application (APL)", Delhi "CRL.M.C.", Allahabad "Application u/s 528 BNSS" (formerly "482 application"), Punjab & Haryana "CRM-M", Karnataka "Criminal Petition" — and whether to add Article 226 (needed when the relief is against the State beyond the proceeding, e.g. quashing a sanction or a policy-based refusal).

2. **Map to the *Bhajan Lal* categories** (1992 Supp (1) SCC 335, para 102). Quashing lies where, on the face of the FIR/complaint: (1) the allegations even if taken at their highest do not make out any offence; (2) the allegations do not disclose a cognizable offence and investigation was begun without a Magistrate's order; (3) the uncontroverted allegations and the evidence collected do not disclose the offence; (4) only a non-cognizable offence is disclosed and no Magistrate ordered investigation; (5) the allegations are so absurd and inherently improbable that no prudent person could reach a conclusion of guilt; (6) there is an express legal bar (sanction under s.218, limitation under s.514, a special Act's bar, double jeopardy / second FIR per *T.T. Antony*); (7) the proceeding is manifestly mala fide or instituted with an ulterior motive to wreak vengeance. State which category each ground fits; a petition that fits none is a discharge argument in disguise.

3. **Test each offence on the face of the record** — the "assume every allegation true" exercise. For each section: ingredient → what the FIR says → document. Cheating (BNS s.318) needs dishonest intention at the inception, not a later default (*Indian Oil v. NEPC*, *Paramjeet Batra*); criminal breach of trust (s.316) needs entrustment; cruelty (s.85) needs specific acts, dates and the role of each relative (*Geeta Mehrotra*, *Dara Lakshmi Narayana*, *Kailashben*); defamation, intimidation and forgery have their own precise elements. Where the civil remedy is pending or available, say so and cite the civil pleadings. Documents of "sterling and impeccable quality" (*Rajiv Thapar*) may be looked at; disputed facts may not (*Mohd. Allauddin Khan* — no mini-trial).

4. **Choose the track.** *Settlement track*: non-compoundable but private/civil-flavoured offences (matrimonial, commercial, property, family, minor hurt) can be quashed on a genuine settlement — *Gian Singh*, *Narinder Singh* (guidelines; heinous and serious offences and those against society excluded; timing and the chance of conviction matter), *Parbatbhai Aahir* (economic offences with public impact, offences by public servants and offences against the State are not quashable merely because the victim settled). The complainant must file an affidavit and usually appear (in person or by video) to confirm the settlement is voluntary; many High Courts direct costs to a legal-aid fund. *Merits track*: categories 1–7 above, argued on the record alone. Running both tracks in one petition is permitted but the merits grounds must not contradict the settlement narrative.

5. **Stage analysis.** At the FIR stage quashing is rarest: *Neeharika Infrastructure* (2021 INSC 240) holds that investigation should ordinarily not be thwarted, that a "no coercive steps" order is not to be passed as a matter of course, and that any interim protection must be reasoned. After the charge sheet, the court looks at the charge sheet and the material with it. After cognizance, the summoning order can be challenged for non-application of mind. After charge framing, discharge is spent and the bar rises further. Say plainly where the case sits and what that does to the odds; use calibrated language ("arguable", "strong on the face of the record", "unlikely at this stage") — never a percentage.

6. **Check the BNSS-specific hooks.** Was a preliminary enquiry under s.173(3) required and skipped (3–7-year offences, DSP permission)? Was a s.35(3) notice issued and complied with, making arrest unlawful under *Arnesh Kumar*? For a complaint case, was the accused heard before cognizance as the proviso to s.223(1) requires? For a public servant, is the s.218 sanction missing, or deemed granted after 120 days? These are grounds, not substitutes for a *Bhajan Lal* category.

7. **Parties and relief.** Implead the State (through the Public Prosecutor / the Home Department as the HC rules require), the investigating officer or police station where interim directions are sought, and the complainant/informant/victim (mandatory — an order without hearing them is set aside). Prayer: quash FIR No. __ and all consequential proceedings (charge sheet, cognizance order, summons) qua the petitioner; interim: stay of further proceedings before the trial court (common after charge sheet), and — only with facts that justify it under *Neeharika* — a direction that no coercive steps be taken pending the petition. Do not ask for a stay of investigation unless the FIR discloses no offence at all.

8. **Draft.** Synopsis (one page, the point in three sentences, the category, the relief); list of dates; memo of parties; petition — jurisdiction and the code applied, brief facts (dated, documented), the FIR's allegations summarised faithfully, grounds (A, B, C … each one *Bhajan Lal*-anchored, with the ingredient test and the authority), the settlement paragraph and affidavit where relevant, prayer, interim prayer; affidavit of the petitioner (disclosing every earlier application and the bail status); annexures (FIR with translation if needed, charge sheet, orders, civil documents, settlement, earlier orders). Keep the grounds under eight; courts read the first two.

## Output

```
# Quashing — [FIR no./PS/year | charge sheet | summoning order] — [petitioner] — [High Court, bench]
## Summary (plain language: is quashing the right tool, which track, where the case sits, the honest prospect, the biggest risk)
## Route check (table: quashing / bail / discharge / compounding / appeal — chosen and why)
## Code and forum (BNSS s.528 or CrPC s.482; Art. 226 added?; vehicle and nomenclature; HC rules checked on [date])
## Bhajan Lal mapping (category → the facts that fit → document)
## Ingredient test (offence → ingredient → FIR says → document → result)
## Track (settlement: parties, affidavit, appearance, costs | merits: grounds)
## Stage analysis and interim relief (what can realistically be asked under Neeharika)
## Draft petition (synopsis · list of dates · memo of parties · petition · prayer · interim prayer · affidavit · annexure list)
## Alternatives if the petition fails or is premature
## Defects and documents still needed
## Sources checked (section, source, date; cases by neutral citation)
```

For a one-line "can this FIR be quashed?" question, collapse to the route table, the category mapping and three lines.

## Guardrails

- Never promise quashing, a stay of investigation, or protection from arrest; state the stage and the standard and let the user decide.
- Never draft a petition that hides an earlier rejected quashing or bail application, a pending bail matter, or a parallel civil suit — disclosure goes in the affidavit.
- Never treat a settlement as enough for heinous offences, offences with a public element, economic offences affecting the public, or offences by public servants — say which line the case is on and cite *Narinder Singh* / *Parbatbhai Aahir*.
- Never argue disputed facts, witness credibility or the quality of evidence as if the High Court conducts a trial; keep to the face of the record and sterling-quality documents.
- Never present IPC numbers for post-1 July 2024 conduct or BNSS s.528 for pre-July pending proceedings; apply the s.531 rule and say so.
- Keep victim-identity cautions for sexual offences (BNS s.72): no names in the draft.
- Do not reproduce long statutory text or judgments; cite and summarise.

## References

- [references/case-law.md](references/case-law.md) — controlling decisions by issue (Bhajan Lal categories, settlement, matrimonial, civil-flavoured disputes, stage and interim relief, sanction, second FIR, summoning orders). Read it before writing the grounds.
- Related skills: **bail-application-bnss** (arrest and custody), **ipc-bns-section-mapper** (section numbering and the 1 July 2024 rule), **fir-and-police-complaint-drafter** (the complainant's side of the same provisions).
