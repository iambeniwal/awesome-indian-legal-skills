# Bail Application (BNSS) Advisor

Works a bail matter from the FIR to a filing-ready draft under the Bharatiya Nagarik Suraksha Sanhita, 2023: regular bail (s.480/483), anticipatory bail (s.482), default bail when the charge sheet is late (s.187(3)), undertrial release after half or one-third of the maximum sentence (s.479), and bailable-offence bail (s.478). It classifies every section cited (BNS or IPC, bailable or not, punishment), checks the arrest for *Arnesh Kumar* and grounds-of-arrest compliance, computes the 60/90-day and s.479 dates with a bundled calculator, argues the standard factors with the *Satender Kumar Antil* categories, and flags NDPS/UAPA/PMLA/SC-ST matters where a stricter statutory test applies.

For advocates, and for families of an arrested person trying to understand the first steps.

## Install

```bash
claude plugin install bail-application-bnss@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- FIR number, date, police station and the sections
- Date of arrest and first remand; where the person is held now
- Stage: investigation, charge sheet (date), charge framed, evidence; earlier bail applications
- The role alleged against this person, and their side
- Whether a s.35(3) notice (41A CrPC) was issued

## What you get

- Forum and section (BNSS with the CrPC equivalent; CrPC routing for matters pending before 1 July 2024)
- Offence classification table with bailability and punishment, and the governing regime
- Custody timeline: 60/90-day default-bail date, s.479 eligibility date
- Arrest and procedure check
- Factor-by-factor analysis tied to documents, or a note opposing bail
- Draft application: cause title, facts, numbered grounds, prayer, conditions offered, undertaking, annexure list
- Conditions likely to be imposed, defects, next steps and a sources ledger

## Calculator

```bash
python3 scripts/bail_timelines.py default --remand 2026-08-01 --punishment other
```

```bash
python3 scripts/bail_timelines.py undertrial --custody-from 2024-02-10 --max-years 7 --first-time
```

`--punishment` is `other` (60 days), `min10`/`life`/`death` (90 days), `ndps` (180, extendable) or `uapa` (90, extendable). The day of first remand counts as day 1 (*Kapil Wadhawan*, 2024). Add `--json` for structured output.

## Example prompts

- "My brother was arrested yesterday under 318(4) and 316(2) BNS at Sector 20 PS Noida, remanded to judicial custody. No 35(3) notice. He's never had a case. What do we file and where?"
- "Draft an anticipatory bail application in the Sessions Court, Pune — FIR under s.85 BNS, client is the husband's sister living in Bengaluru, no overt act alleged."
- "Remand was on 2 August, 60-day offence, charge sheet still not filed. When does default bail arise and what exactly do we file?"
- "Client has done 30 months as undertrial in a 7-year case, first offence. Is he out under 479?"

## Law covered

- BNSS, 2023 — ss.35, 47, 58, 187, 478–496, 528, 531; First Schedule
- NDPS Act s.37, s.36A; UAPA s.43D; PMLA s.45; SC/ST (PoA) Act ss.18, 18A; JJ Act s.12
- Key decisions: *Arnesh Kumar*, *Satender Kumar Antil*, *Sanjay Chandra*, *Gurbaksh Singh Sibbia*, *Sushila Aggarwal*, *Sanjay Dutt*, *Rakesh Kumar Paul*, *M. Ravindran*, *Kapil Wadhawan*, *K.A. Najeeb*, *Vijay Madanlal Choudhary*, *Manish Sisodia*, *Frank Vitus*, *In re Inhuman Conditions in 1382 Prisons* (2024) — see [references/case-law.md](references/case-law.md) and [references/bail-factors.md](references/bail-factors.md)

## Limits

- Not for quashing (s.528), suspension of sentence pending appeal (s.430) or extradition.
- Does not know the local High Court's bail rules, roster or listing practice; it tells you to check.
- Does not compute dates you have not supplied, and does not file anything.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every draft before it is relied on or filed.
