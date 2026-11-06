---
name: fir-and-police-complaint-drafter
description: >
  Gets a crime registered and documented under the BNSS, 2023 and works the remedies when the police
  will not act: drafts the written complaint for an FIR (including zero FIR and e-FIR under s.173),
  the representation to the Superintendent of Police under s.173(4), the application to the
  Magistrate under s.175(3) with its affidavit, and a private complaint under s.223 as the fallback;
  routes non-cognizable matters (s.174), cyber fraud (cybercrime.gov.in / 1930), domestic violence
  and workplace harassment to the right track. Use whenever a user says "FIR", "police complaint",
  "FIR nahi likh rahe", "police refused to register", "zero FIR", "online fraud report", "how do I
  file a complaint against", "I was cheated/assaulted/threatened/robbed", or needs the first
  documented step after an offence. Not for the accused's side — route bail and quashing to the
  bail-application-bnss and quashing-petition-bnss-528 skills.
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

# FIR and Police Complaint Drafter

Produces a route decision (FIR, zero FIR, non-cognizable report, cyber portal, private complaint, or another forum), the drafts for each step, an evidence checklist and a what-happens-next timeline. For victims, informants and their families, and for advocates handling the complainant's side.

> **Not legal advice.** This is a drafting and procedure aid under Indian law. A qualified advocate must review anything before it is relied on or filed, and the police and the court — not this skill — decide which offences apply. Say this once at the start of the first response. **If anyone is in danger right now, say first: call 112.**

## Jurisdiction gate

Indian law only. Identify the State/UT and district: the police station, the Superintendent/Commissioner structure (Commissionerate cities route s.173(4) representations to the DCP/Commissioner as the State's rules provide), State police citizen portals for e-FIR, and State rules under s.173 all differ. If the offence happened abroad or the user is outside India, say what the Indian police can and cannot do before drafting.

## Verify before relying

Check and record the date checked:

- BNSS, 2023 — s.173 (information in cognizable cases: oral or electronic; e-FIR signed within **three days**; zero FIR "irrespective of the area"; woman officer for the listed BNS offences; preliminary enquiry within **fourteen days** with DSP permission for offences punishable 3–7 years, s.173(3); free copy, s.173(2); refusal → SP, s.173(4)), s.174 (non-cognizable), s.175(3) (Magistrate's order on an application supported by affidavit after the SP route), s.183 (statements before a Magistrate), s.193(3)(ii) (progress of investigation to be communicated within **ninety days**), s.223 (complaint to a Magistrate; the accused is heard before cognizance), s.172 (duty to conform to lawful police directions): [India Code](https://www.indiacode.gov.in/).
- The BNSS **First Schedule** for whether each likely offence is cognizable and bailable; map old numbers through the **ipc-bns-section-mapper** skill.
- BNS, 2023 — the offences and s.72 (identity of a victim of sexual offences not to be disclosed), s.217 and s.248 (false information / false charge — the complainant's own exposure).
- National Cyber Crime Reporting Portal [cybercrime.gov.in](https://cybercrime.gov.in/) and helpline **1930**; RBI's framework on limiting customer liability in unauthorised electronic banking transactions (2017 circular — zero liability if reported within three working days; verify the current circular).
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); summarised in [references/case-law.md](references/case-law.md).

If no browsing tool is available, say the periods and section numbers are from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones first, together, in plain language, and accept them in Hindi or Hinglish.

**Blocking:**
- What happened, in the user's words: when (date and approximate time), where (address or online platform), who (names or descriptions; relationship to the user), what was done, what was lost or injured
- Evidence in hand: messages, call records, screenshots, transaction IDs/UTRs, photos, CCTV availability, medical papers, documents
- Whether anything was already reported — to which police station, when, what happened (NC entered? told to come back? refused in writing or orally?), or on the cyber portal (acknowledgment number)
- Safety now: ongoing threat, injuries needing treatment, a child or a woman victim of a sexual offence (changes who records and where)

**Nice to have:** witnesses, prior disputes with the accused, bank/wallet names and account numbers for frauds, the platform's grievance-officer reply, any earlier civil or family proceeding.

If the facts are too thin to say what happened and when, ask — do not fill the gaps with plausible details.

## Method

1. **Classify the offence and the route.** Identify the likely BNS sections (named as "appears to attract", never as certain) and check cognizability in the First Schedule. Then pick the route:
   - **Cognizable** → FIR under s.173 at the local station, or a **zero FIR** at any station (the station must register and transfer; useful when the local station stalls or the user is elsewhere), or **e-FIR** through the State portal where available (the user must sign within three days or it lapses).
   - **Non-cognizable** → an NC entry under s.174(1) and a referral to the Magistrate; police investigate only on the Magistrate's order (s.174(2)); a mixed case with one cognizable offence is cognizable (s.174(4)).
   - **Cyber fraud / online offences** → the NCRP at cybercrime.gov.in or **1930** *immediately* (the "golden hour": the portal's financial-fraud track can freeze the money trail), plus a written complaint to the bank/wallet within three working days for the RBI zero-liability protection, plus a police complaint — all three in parallel.
   - **Domestic violence** → the DV Act route (Protection Officer, Magistrate) alongside or instead of an FIR where no cognizable offence beyond the Act is disclosed; **workplace sexual harassment** → the Internal Committee under POSH unless a BNS offence is also alleged; **missing person** → FIR at once (no waiting period), plus the State's missing-persons portal; **accident** → FIR plus the Motor Accident Claims route.
   - **Public-servant accused** → note the s.175(4) and s.223(2) pre-conditions (superior officer's report; the public servant's version).

2. **Draft the complaint for the FIR.** Address it to the officer in charge (SHO) of the station; subject line with the offence in plain words; facts in time order, each paragraph one event with date, time, place, people and what the user saw or heard; what was taken, damaged or injured, with values and medical details; the evidence available and where it is (CCTV location and retention risk; phone numbers; UTRs); the sections that *appear* to apply "or such other sections as the police may determine"; a prayer to register the FIR, investigate, and supply a free copy under s.173(2); the informant's details, signature and date. For a woman reporting a listed sexual offence, state that the information is to be recorded by a woman officer and, where the victim is disabled, at the residence with videography (s.173(1) provisos). Keep legal conclusions out; the FIR is not an encyclopaedia (*Tapan Kumar Singh*) — it must start the investigation, not win the trial.

3. **Dispatch and proof.** Hand-deliver two copies and get a received stamp with date and the DD/GD entry number, or send by registered post/email to the station and the DCP/SP; keep the proof. If the information was oral, insist that it be read back and signed (s.173(1)(i)).

4. **If the police refuse (orally or by delay)** — *Lalita Kumari* makes registration mandatory for information disclosing a cognizable offence; a preliminary enquiry is permitted only in defined categories (matrimonial, commercial, medical negligence, corruption, abnormal delay) and now within fourteen days under s.173(3) for 3–7-year offences. The sequence the BNSS requires:
   - **Step A — s.173(4) representation** to the Superintendent of Police "in writing and by post": the substance of the information, the date and station where it was refused, the proof of the earlier attempt, and a request that the SP investigate or direct investigation. Send by registered post (the section says "by post") and email; keep the receipt.
   - **Step B — s.175(3) application** to the Magistrate empowered under s.210, **supported by an affidavit** (*Priyanka Srivastava*), annexing the original complaint, the proof of refusal, the SP representation and its proof of dispatch; the Magistrate may enquire and hear the police before ordering investigation. Courts refuse applications that skipped Step A.
   - **Step C — private complaint under s.223** when the police route fails or the user prefers it: the Magistrate examines the complainant and witnesses on oath, hears the accused before taking cognizance (proviso to s.223(1)), and may issue process. This is a trial-track choice, not a shortcut; say what it costs in time.

5. **Run the timeline with the bundled script** and paste it:
   ```bash
   python3 scripts/fir_timeline.py --incident YYYY-MM-DD [--reported YYYY-MM-DD] [--efir] [--refused YYYY-MM-DD] [--sp-sent YYYY-MM-DD] [--fir-registered YYYY-MM-DD] [--today YYYY-MM-DD]
   ```
   It prints the three-day e-FIR signature deadline, the fourteen-day preliminary-enquiry window, a reasonable wait for the SP (the Act fixes none — the script uses 15 days and says so), the ninety-day progress-report date under s.193(3)(ii), the two-month investigation target for the listed sexual offences (s.193(2)), and the three-working-day bank-reporting window for cyber fraud. If the script is unavailable, compute by hand and mark it unverified.

6. **After registration — the informant's rights.** A free copy of the FIR (s.173(2)); progress of investigation within ninety days (s.193(3)(ii)); communication of the action taken, including a closure report, with the right to object before the Magistrate (*Bhagwant Singh*); a copy of the charge sheet; a statement under s.183 before a Magistrate where the facts call for it; victim compensation (s.396). Tell the user how to follow up without harassing the IO: a dated written request, then the SP, then the Magistrate.

7. **Cyber-specific fields.** For NCRP: category (financial fraud / social-media / others), the transaction table (date, time, amount, UTR, from-account, to-account/UPI, platform), screenshots, the suspect's number/handle/URL, ID proof. Advise freezing further transactions, changing credentials, and not paying "recovery" callers — a second fraud pattern.

## Output

```
# Police complaint — [offence in plain words] — [station / district / State]
## Safety first (one line; 112 if there is any present danger)
## Route (FIR / zero FIR / e-FIR / NC / NCRP + bank / DV Act / POSH / private complaint — and why; likely BNS sections marked "appears to attract")
## Draft complaint to the SHO
## Dispatch and proof plan
## If refused: s.173(4) representation to the SP (draft) → s.175(3) application with affidavit (skeleton) → s.223 complaint (when)
## Timeline (output of fir_timeline.py)
## Evidence checklist (what to preserve, where, how; CCTV retention; UTRs)
## What happens next (registration → copy → investigation → 90-day progress → charge sheet or closure → your rights at each step)
## Sources checked (section, source, date; cases by neutral citation)
```

For "police are refusing, what do I do?" collapse to the refusal sequence and the two drafts.

## Guardrails

- Never draft facts the user did not give, never inflate injuries, amounts or the accused's role, and never add "with intent to" language the facts do not show — a false charge is itself an offence (BNS s.217/248).
- Never state the sections as certain; the police and the court decide. Name them as what the facts "appear to attract".
- Never advise confronting, recording or paying the accused, or taking matters to social media before the complaint; say why (tampering, counter-complaints, defamation exposure).
- Never promise registration, arrest or a timeline the Act does not fix; distinguish statutory periods from practice.
- Sexual offences: no victim names in any draft (BNS s.72); woman officer and residence recording as the provisos require; medical examination and s.183 statement as early steps.
- Children: route through the child-welfare police officer and POCSO procedures; say so before drafting.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/case-law.md](references/case-law.md) — *Lalita Kumari* and its categories, the refusal remedies (*Sakiri Vasu*, *Priyanka Srivastava*, *Sudhir Bhaskarrao Tambe*), FIR scope (*Tapan Kumar Singh*), closure-report rights (*Bhagwant Singh*), zero FIR and transfer, cyber-fraud liability. Read it before the refusal section.
- [scripts/fir_timeline.py](scripts/fir_timeline.py) — the dates calculator; `--json` for structured output.
- Related skills: **ipc-bns-section-mapper** (numbering and cognizability), **bail-application-bnss** and **quashing-petition-bnss-528** (the accused's side), **legal-notice-drafter-india** (when a notice, not a complaint, is the right first step).
