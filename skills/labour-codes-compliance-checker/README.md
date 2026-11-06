# Labour Codes Compliance Checker

Audits an Indian establishment against the four Labour Codes in force since 21 November 2025 (Wages, Industrial Relations, Social Security, OSH), with the Central Rules of May 2026 and the State-by-State transition, and computes what an employee is owed — gratuity, retrenchment compensation, leave encashment and bonus — on the Codes' uniform "wages" base.

For HR and in-house teams, advocates, and employees checking their dues.

## Install

```bash
claude plugin install labour-codes-compliance-checker@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- State and sector of the establishment; headcount (workers vs others, contract, fixed-term)
- The pay structure (gross, and basic/DA/retaining allowance vs allowances)
- For dues: joining and exit dates, last drawn pay, reason for exit

## What you get

- Applicability memo: which Chapters, registrations and thresholds bite, and whether Central or State rules govern
- Wages computation under the 50% rule
- Graded gap register (registration, wages, hours, social security, IR, OSH)
- Dues table from the calculator, with the convention and cap stated
- Forum and timeline for claims; the list of items to verify (State rules, notified ceilings)

## Calculator

```bash
python3 scripts/labour_dues.py wages --gross 100000 --basic-da-ra 40000
```

```bash
python3 scripts/labour_dues.py gratuity --wage 40000 --years 7 --months 8
```

Subcommands: `wages`, `gratuity` (`--fixed-term`, `--cap`), `retrenchment`, `leave`, `bonus`; `--json` for structured output.

## Example prompts

- "We have 340 employees in Pune, basic is 35% of CTC. What do the new labour codes change for us and what's at risk?"
- "I was retrenched after 7 years 8 months at ₹40,000 basic+DA. What am I owed under the new codes?"
- "Is a fixed-term employee of 18 months entitled to gratuity now?"

## Law covered

- Code on Wages, 2019; Industrial Relations Code, 2020; Code on Social Security, 2020; OSH Code, 2020 — in force 21 Nov 2025; Central Rules 8–9 May 2026; Model Standing Orders 2026
- Transition: repealed Acts and savings; State rules status table in [references/status-and-transition.md](references/status-and-transition.md)

## Limits

- State rules and notified ceilings move; the skill tells you what to verify and never states them as settled.
- Facts before 21 November 2025 are computed under the repealed Acts; the skill says so and does not switch regimes silently.
- POSH, EEO and sector-specific service rules are outside scope.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice.
