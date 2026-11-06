---
name: labour-codes-compliance-checker
description: >
  Audits an Indian employer (or checks an employee's entitlements) against the four Labour Codes in
  force since 21 November 2025 — Code on Wages 2019, Industrial Relations Code 2020, Code on Social
  Security 2020, OSH Code 2020 — with the Central Rules of May 2026 and the State-rules transition.
  Applies the uniform "wages" definition (50% rule), computes gratuity, retrenchment compensation,
  leave encashment and bonus with a bundled calculator, checks hours, overtime, appointment letters,
  PF/ESIC, standing orders, fixed-term employment and retrenchment thresholds, and grades gaps. Use
  whenever a user mentions labour codes, "new labour law", wage code, gratuity, PF/ESI, retrenchment,
  lay-off, termination of a workman, fixed-term employee, bonus, overtime, working hours, "naukri se
  nikal diya", "gratuity kitni milegi", standing orders, or HR compliance for an Indian
  establishment. Facts before 21 November 2025 are governed by the repealed Acts; POSH is elsewhere.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Employment & Labour
  jurisdiction: IN
  states: all
  language: en
---

# Labour Codes Compliance Checker

Produces an applicability memo, an obligation-by-obligation gap register, a dues table (gratuity, retrenchment compensation, leave encashment, bonus) and a list of the Central-vs-State rule points that must be verified. For HR and in-house teams, advocates, and employees checking what they are owed.

> **Not legal advice.** This is a research and calculation aid under Indian law. The Codes are new, the Rules are newer, and State rules are still arriving; a qualified advocate must review every interpretation and figure before it is relied on, paid or litigated. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only, and **State-specific**: labour is a concurrent subject, the Codes leave rules, thresholds (e.g. the lay-off/retrenchment permission threshold under IR Code s.77), shops-and-establishments matters and minimum wages to the appropriate Government, and each State is notifying its own rules on its own timetable. Identify the State (and whether the establishment is Central-sphere — railways, mines, ports, banks, Central PSUs — where the Central Rules apply). If the employment is governed by foreign law or is outside India, stop and say so.

## Verify before relying

Before stating any figure, threshold or date as current, check and record the date checked:

- The four Codes on [India Code](https://www.indiacode.gov.in/): Code on Wages, 2019 (Act 29 of 2019); Industrial Relations Code, 2020 (Act 35 of 2020); Code on Social Security, 2020 (Act 36 of 2020); Occupational Safety, Health and Working Conditions Code, 2020 (Act 37 of 2020).
- Commencement: in force from **21 November 2025** (notifications of 21 November 2025 on [e-Gazette](https://egazette.gov.in/)); some provisions were carved out — read the notification. The **Central Rules** under all four Codes and the **Model Standing Orders, 2026** were notified on **8–9 May 2026** (drafts had been published 30 December 2025) — [labour.gov.in](https://labour.gov.in/).
- **State rules**: check the State labour department's site; until a State notifies rules under a Code, the corresponding rules under the repealed Acts continue (transitional savings) — see [references/status-and-transition.md](references/status-and-transition.md) and refresh its table.
- Wage ceilings and bonus parameters are set by notification, not by the Code text: the Central Government's bonus notifications of 25 August 2026 (eligibility up to ₹21,000 a month; calculation on ₹7,000 or the minimum wage, whichever is higher; stated to apply from 21 November 2025) and the gratuity ceiling (₹20 lakh carried from the Payment of Gratuity Act regime, s.53(3) CSS Code "as notified") — **(verify)** both on e-Gazette.
- Supreme Court decisions on the old Acts remain persuasive on provisions the Codes re-enact (e.g. *Regional PF Commissioner v. Vivekananda Vidyamandir*, 2019, on what counts as "basic wages" — now largely codified by the 50% rule).

If no browsing tool is available, say the figures come from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones first, together, in plain language.

**Blocking:**
- The State and city of each establishment, and the sector (factory, shop/commercial, construction, mines, plantation, IT/ITeS, gig/platform, contract labour)
- Headcount today and over the last 12 months (workers vs supervisory/managerial; contract workers; fixed-term; apprentices), because every threshold turns on it
- The pay structure for the roles in question: gross monthly, and the split into basic, DA, retaining allowance and each allowance (needed for the 50% rule)
- For dues: date of joining, date of exit, last drawn pay, reason for exit (resignation, retrenchment, closure, termination for misconduct, end of fixed term, death/disability)

**Nice to have:** existing registrations (EPFO, ESIC, S&E, factory licence, contract-labour licence), standing orders status, union recognition, current policies (leave, hours, shifts, women on night shifts), HR letters/templates, any pending claims.

## Method

1. **Fix the regime by date.** The Codes govern from 21 November 2025. For a termination, accrual of wages or gratuity, or an industrial dispute arising before that date, the repealed Acts apply (Industrial Disputes Act s.25F, Payment of Gratuity Act, Payment of Wages/Minimum Wages Acts, Factories Act); say which and compute under that Act. Where facts straddle the date, split them.

2. **Apply the uniform "wages" definition first** (s.2(y) Code on Wages, mirrored in the other Codes): wages = basic + dearness allowance + retaining allowance; the listed exclusions (HRA, conveyance, overtime, commission, bonus, employer PF contribution, gratuity, etc.) are capped at **50% of total remuneration** — anything beyond 50% is added back into wages. This base feeds PF, gratuity, bonus eligibility, retrenchment compensation and leave encashment, which is why "basic 30% of CTC" structures now cost more. Show the computation.

3. **Run the applicability matrix** from [references/obligations-checklist.md](references/obligations-checklist.md): registration/licence (OSH Code s.3: single registration for establishments with 10+ workers; contract-labour licence at 50+ — verify), factory definition (10 with power / 20 without), PF (20 employees — verify, CSS Chapter III), ESIC (10 employees, pan-India, with hazardous establishments covered irrespective — verify, Chapter IV), standing orders (IR Code s.28: 300+ workers; Model Standing Orders 2026 apply by default), lay-off/retrenchment/closure permission (IR Code Chapter X, s.77: 300+ workers, **or the State's notified threshold**), works committee (100+), grievance redressal committee (20+; up to ten members, IR Code s.4), safety committee, welfare officer, canteen/crèche thresholds under the OSH Rules.

4. **Check the operating rules** and grade each as Met / Partly / Not met: appointment letter to every employee (OSH Code s.6); working hours — 8 hours a day as the baseline (OSH Code s.25) with the Rules allowing longer days within a 48-hour week and spread-over limits, overtime at **twice** the wage rate (s.26) with consent — read the final Central Rules and the State's rules on the daily cap **(verify: the 12-hour figure comes from draft/State rules, not the Code)**; weekly off; women on night shifts only with consent and prescribed safeguards (s.43); annual free health check-ups for notified classes (s.20); leave with wages (one day per 20 worked, carry-forward 30 — verify); timely wage payment (Code on Wages s.17: monthly wages by the 7th of the following month; final settlement within two working days of removal/resignation — verify the Rules); deductions capped at 50% (s.18); gender-neutral equal remuneration (s.3); minimum and floor wages (ss.6–9); bonus (Chapter IV: eligibility and the 8.33%–20% band on the notified base); fixed-term employment with equal benefits and pro-rata gratuity after one year (IR Code s.2(l)/CSS s.53); negotiating union at 51% membership or a negotiating council (IR Code s.14); 14-day strike notice for every establishment (s.62); re-skilling fund — 15 days' wages per retrenched worker (s.83); Industrial Tribunal two-member benches; gig and platform workers' registration and the aggregator contribution (CSS s.114: 1–2% of annual turnover, capped at 5% of amounts paid to such workers — verify commencement); maternity benefit 26 weeks carried into CSS Chapter VI; electronic registers, returns and the inspector-cum-facilitator regime; compounding of first offences.

5. **Compute dues with the bundled calculator** and paste the table:
   ```bash
   python3 scripts/labour_dues.py wages --gross 100000 --basic-da-ra 40000
   python3 scripts/labour_dues.py gratuity --wage 40000 --years 7 --months 8 [--fixed-term] [--cap 2000000]
   python3 scripts/labour_dues.py retrenchment --wage 40000 --years 7 --months 8 [--notice-months 1]
   python3 scripts/labour_dues.py leave --wage 40000 --days 30
   python3 scripts/labour_dues.py bonus --wage 18000 --percent 8.33 [--ceiling 21000] [--base 7000] [--min-wage 0]
   ```
   Gratuity: 15/26 × last drawn wages × completed years, with six months or more counting as a full year, five-year qualifying service (waived on death/disablement), pro-rata for fixed-term employees after one year, capped at the notified ceiling. Retrenchment (IR Code s.70, mirroring ID Act s.25F): one month's notice or pay in lieu plus 15 days' average pay for every completed year of continuous service or part in excess of six months. Leave encashment: monthly wage ÷ 26 × days (the divisor is a convention — verify the State rule). Bonus: eligible if wages ≤ the notified ceiling; computed on the notified base or the wage, whichever is lower, at 8.33% minimum. The script prints every step; if it is unavailable, compute by hand, show each step and mark unverified.

6. **Grade the gaps** — Blocking (no registration where required; wages below minimum; no appointment letters; PF/ESIC due but not deducted; retrenchment without permission where Chapter X applies; women on night shift without consent/safeguards), High (50% rule not applied; overtime below double; hours above the cap; no standing orders where 300+), Medium (registers, returns, GRC not constituted). For each: the section, the evidence, the fix, and whether the Central or State rule governs it.

7. **Employee-side mode.** When the user is the worker: compute what is owed, say which forum (conciliation officer → Industrial Tribunal; claim under Code on Wages s.45 within **three years**; gratuity controlling authority; EPFO/ESIC grievance), and what documents prove service and pay.

## Output

```
# Labour Codes — [Employer audit | Employee dues] — [establishment / employee], [State]
## Summary (plain language: regime by date, headcount thresholds crossed, biggest gap or the amount due)
## Applicability (sector, State, headcount → which Chapters and registrations apply; Central vs State rules)
## Wages computation (50% rule applied, with the figure used downstream)
## Obligation gap register (obligation → section/rule → status → evidence → fix → who governs)
## Dues table (output of labour_dues.py, with the convention and the cap stated)
## Forum and timelines (for disputes or claims)
## Items to verify (State rules in force, notified ceilings, thresholds; date checked)
```

## Guardrails

- Never state a State's rules as in force without that State's notification; say "Central Rules / old State rules pending" where that is the position.
- Never apply the 300-worker threshold where the State has notified a different one; check before advising on retrenchment permission.
- Never compute gratuity, PF or bonus on "basic" without first applying the 50% rule to the actual pay structure.
- For facts before 21 November 2025, apply the repealed Acts (ID Act s.25F, Payment of Gratuity Act, Payment of Bonus Act) and say so.
- Do not promise that a termination is lawful because notice was given; procedure (standing orders, inquiry, permission) matters as much as money.
- Do not quote the gratuity ceiling, bonus ceiling or daily-hours cap as settled; mark them "(verify)" with the source.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/status-and-transition.md](references/status-and-transition.md) — commencement, what the Codes repealed, what survives, and the State-rules table to refresh. Read it first on every matter.
- [references/obligations-checklist.md](references/obligations-checklist.md) — the applicability matrix and operating-rules checklist, in audit order.
- [scripts/labour_dues.py](scripts/labour_dues.py) — wages rule, gratuity, retrenchment, leave encashment and bonus calculator; `--json` for structured output.
