---
name: bail-application-bnss
description: >
  Audits a bail matter under the BNSS, 2023 and drafts the application: regular bail (s.480 Magistrate /
  s.483 Sessions and High Court), anticipatory bail (s.482), default bail when the charge sheet is late
  (s.187(3)), undertrial release at half or one-third of the maximum sentence (s.479), and bailable-offence
  bail (s.478). Maps CrPC 436/436A/437/438/439/167/482 to the BNSS, routes pre-1 July 2024 matters to the
  CrPC, and computes the 60/90-day and s.479 dates with a bundled calculator. Use whenever a user mentions
  bail, "zamanat", anticipatory bail, "police arrest karne wali hai", custody, remand, "charge sheet 90 din
  me nahi aayi", undertrial release, Arnesh Kumar or Satender Antil, or wants a bail application drafted,
  checked or opposed. For NDPS, UAPA, PMLA, POCSO or SC/ST Act matters it applies the stricter statutory
  test. Not for quashing (s.528) or suspension of sentence pending appeal (s.430) — say so and route.
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

# Bail Application (BNSS) Advisor

Produces a maintainability audit, the right forum and section, a draft bail application (or a note opposing one), the conditions likely to be imposed, and a defect list. For advocates, and for families of an arrested person trying to understand the first steps.

> **Not legal advice.** This is a research and drafting aid under Indian law. Liberty is at stake and every court has its own practice; a qualified advocate must review every interpretation, citation and draft before it is relied on or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the State/UT and the district: the Sessions Division fixes the court under s.483, High Court bail rules and e-filing practice differ, and State amendments (for example to the First Schedule's bailability of particular offences) exist. If the matter is governed by foreign law or the user is outside India seeking extradition-related relief, stop and say so.

## Verify before relying

Check these before stating a section, period or test as current, and record the date checked:

- BNSS, 2023 Chapter XXXV (ss.478–496 bail and bonds), s.35 (arrest without warrant; s.35(3) notice; s.35(7) prior permission for infirm/60+ persons in offences under three years), s.187 (remand; s.187(3) 60/90-day limits), s.479 (undertrial release): [India Code](https://www.indiacode.nic.in/).
- Bailability and punishment: the **First Schedule to the BNSS** for BNS offences; for IPC offences in proceedings pending on 1 July 2024, the CrPC First Schedule as saved by BNSS s.531.
- Special statutes with their own bail tests: NDPS Act s.37, UAPA s.43D(5), PMLA s.45, SC/ST (PoA) Act s.18/18A (bar on anticipatory bail), POCSO (no separate test, but s.483 notice to informant and gravity), Juvenile Justice Act s.12 (bail of a child is the rule).
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); the ones that control bail practice are summarised in [references/case-law.md](references/case-law.md).

If no browsing tool is available, say the periods and section numbers come from the skill's version date and must be verified.

## Which route?

Ask one question if it is not obvious from the prompt:

| Situation | Provision (CrPC equivalent) | Forum |
|---|---|---|
| Bailable offence, accused in custody or appearing | s.478 (436) | Officer in charge / Magistrate — bail is a right |
| Non-bailable, arrested, investigation or trial pending | s.480 (437) | Magistrate having jurisdiction |
| Same, after Magistrate refuses or offence punishable with death/life | s.483 (439) | Sessions Court; then High Court (concurrent, Sessions first by practice) |
| Apprehending arrest, not yet arrested | s.482 (438) | Sessions Court or High Court |
| In custody, charge sheet not filed within 60/90 days of first remand | s.187(3) (167(2) proviso) | The remanding Magistrate (or Special Court) |
| Undertrial who has served half (first-timer: one-third) of the maximum sentence | s.479 (436A) | The trial court, on its own or on application; jail superintendent must apply (s.479(3)) |
| Proceeding instituted before 1 July 2024 | CrPC numbers | Same forums — cite the CrPC section and note BNSS s.531(2)(a) |

Quashing of the FIR is s.528 (482 CrPC) and is a different skill. Bail pending appeal after conviction is s.430 (389 CrPC); say so and stop at the forum table.

## Required inputs

Ask for the blocking ones first, together, in plain language. The applicant's family often has only the arrest memo and a WhatsApp photo of the FIR — work from what exists and list what is missing.

**Blocking:**
- FIR number, date, police station, sections (and which code — the agent must classify each as BNS/IPC and check bailability and maximum punishment in the Schedule)
- Custody status: date and time of arrest, date of first remand, where held, police or judicial custody now
- Stage: investigation / charge sheet filed (date) / charge framed / evidence / earlier bail applications and their outcome (an undisclosed earlier rejection is fatal)
- Role alleged against this applicant specifically, and the applicant's version
- Whether a s.35(3) notice (41A CrPC) was issued, and whether the applicant complied

**Nice to have:** antecedents (any prior case, conviction, or pending bail), age, health, dependants, employment and roots in the community, passport status, recovery or seizure made, whether co-accused got bail (parity), victim/informant relationship and any settlement, documents that show innocence or the alibi.

Without custody dates and the sections, produce a defect list and a forum table only — never a draft with placeholders that pretend to be facts.

## Method

1. **Classify the offence and the regime.** For each section: BNS or IPC (date of the act decides — see the ipc-bns-section-mapper skill), bailable or non-bailable, maximum and any minimum punishment (this decides the Magistrate's power under s.480(1), the 60/90-day limit under s.187(3), the Arnesh Kumar seven-year line, the *Antil* category and the s.479 fraction). If a special statute applies, stop ordinary analysis and say which twin-condition or prima-facie test governs, using [references/bail-factors.md](references/bail-factors.md).

2. **Check for arrest irregularities before merits.** For offences punishable up to seven years, arrest without recorded reasons under s.35(1)(b) and without a s.35(3) notice breaches *Arnesh Kumar*; grounds of arrest must be furnished in writing (*Pankaj Bansal*, *Prabir Purkayastha*, extended beyond PMLA/UAPA to all arrests in *Vihaan Kumar*, 2025); production within 24 hours (s.58). An irregularity is a strong ground, sometimes decisive, and goes in the first paragraph of grounds — but it is not a substitute for the merits.

3. **Run the timelines with the calculator** and paste the output:
   ```bash
   python3 scripts/bail_timelines.py default --remand YYYY-MM-DD --punishment other|min10|life|death|ndps|uapa [--today YYYY-MM-DD]
   python3 scripts/bail_timelines.py undertrial --custody-from YYYY-MM-DD --max-years N [--first-time] [--today YYYY-MM-DD]
   ```
   Default bail: the 60/90 days run from the **date of first remand**, counting that day (*Kapil Wadhawan*, 2024), and the right is indefeasible only if the application is filed and bail offered **before** the charge sheet is filed (*Sanjay Dutt*, *M. Ravindran*). An application filed a day late is an ordinary bail application. For s.479, the fraction applies to the maximum sentence for the offence, excludes death/life offences, and is lost where the person faces more than one case (s.479(2)).

4. **Apply the standard factors** — nature and gravity, role, evidence and its strength, flight risk, tampering/influence, antecedents, health/age/gender, delay in trial and period already undergone, parity — using the structure in references/bail-factors.md and the *Antil* categories. State "bail is the rule, jail the exception" (*Sanjay Chandra*, reiterated in *Manish Sisodia*, 2024) once, then argue facts. For economic offences, gravity is a factor, not a bar (*P. Chidambaram*).

5. **Anticipatory bail specifics.** Confirm the applicant has not absconded or been proclaimed under s.84 — if they have, anticipatory bail is ordinarily not maintainable (*Lavesh*, *Srikant Upadhyay*, 2024). The BNSS text of s.482 drops the CrPC s.438(1) list of factors, and s.482(4) bars anticipatory bail altogether for offences under BNS s.65 (rape of a woman under sixteen or twelve) and s.70(2) (gang rape of a woman under eighteen) — check the sections alleged before drafting. Relief need not be time-limited (*Sushila Aggarwal*). Offer joining investigation, surrender of passport and non-contact as conditions.

6. **Draft.** Cause title (court, Sessions Division/district, bail application number blank, "State v. [accused]" with FIR particulars); applicant's details and custody status; brief facts as alleged and the applicant's position; grounds numbered, strongest first, each tied to a document or a decision; prayer (release on bail on terms the court deems fit; interim bail if listing is delayed, per *Antil*); conditions offered; undertaking not to tamper or leave the jurisdiction; verification; annexures (FIR, arrest memo, remand orders, medical records, earlier orders, custody certificate). Keep it under six pages; courts read the grounds, not the preamble.

7. **Opposing bail (if the user is the complainant/State).** Same factors inverted: specific role, threats or tampering evidence, antecedents, flight, and — for BNS s.65/s.70(2) offences — the fifteen-day notice to the Public Prosecutor under the proviso to s.483(1) and the informant's obligatory presence at the hearing under s.483(2); and the cancellation standard (*Dolat Ram*: supervening circumstances, not re-argument of merits).

8. **Predict conditions** likely to be imposed (surety amount and number, reporting to the police station, passport surrender, no contact with witnesses, address intimation) and flag conditions that are impermissible or arbitrary (*Frank Vitus*, 2024: no live-location sharing; *Parvez Lokhandwalla*: conditions must be reasonable). If sureties are a problem, point to the Supreme Court's directions in *In re Policy Strategy for Grant of Bail* (2023) on release where sureties cannot be furnished within a week.

## Output

```
# Bail — [regular s.480/483 | anticipatory s.482 | default s.187(3) | s.479 | bailable s.478] — [accused] — FIR [no./PS/year]
## Summary (plain language: maintainable or not, which court, next date that matters, biggest risk)
## Offence classification (section → code → bailable? → max/min punishment → regime → source checked)
## Custody timeline (arrest, remand, 60/90-day date, charge-sheet status — output of bail_timelines.py)
## Arrest and procedure check (s.35, grounds of arrest, 24-hour production, s.35(3) notice)
## Factors (each factor → facts for → facts against → document)
## Draft application  (or: note opposing bail)
## Conditions likely / conditions to offer
## Defects and documents still needed
## Next steps (who files what, where, by when)
## Sources checked (section, source, date; cases by neutral citation)
```

For a quick "which section / which court" question, collapse to the forum table and three lines.

## Guardrails

- Do not assert a date of arrest, remand or charge-sheet filing that the user did not give; never compute default bail from an assumed date.
- Do not draft an anticipatory-bail application for a person who has been proclaimed an absconder or has evaded summons without first flagging that it is unlikely to be maintainable.
- Do not hide an earlier rejected application; the draft must disclose it (suppression is a ground for cancellation).
- For NDPS commercial quantity, UAPA Chapter IV/VI offences, PMLA scheduled offences and SC/ST Act matters, state the statutory test and the controlling cases; do not present ordinary factors as sufficient.
- Do not promise outcomes or timelines; say what the practice is in the forum and that listing depends on the court.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/bail-factors.md](references/bail-factors.md) — factor checklist, the *Satender Kumar Antil* category table, Magistrate's limits under s.480, special-statute tests and the surety/bond provisions. Read it before the Factors section.
- [references/case-law.md](references/case-law.md) — controlling decisions by issue. Read it before citing anything.
- [scripts/bail_timelines.py](scripts/bail_timelines.py) — default-bail and s.479 date calculator; `--json` for structured output.
