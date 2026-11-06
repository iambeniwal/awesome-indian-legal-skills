# Limitation Period Calculator

Answers "is it time-barred, and what is the last date?" for Indian suits, appeals and applications. It picks the Article of the Schedule to the Limitation Act, 1963 (or the special-statute period — Arbitration, Commercial Courts, Consumer Protection, NI Act, IBC, RERA, Companies Act, RTI, GST, income tax, SARFAESI, Motor Vehicles) from the nature of the proceeding and the accrual facts, applies the computation rules (s.12, s.14, s.17, s.18/19, s.4, ss.6–8, s.22) and the Supreme Court's COVID-19 exclusion with a bundled calculator, and says plainly what can still save a late filing and what cannot.

For advocates, litigants and in-house teams deciding whether and when to file.

## Install

```bash
claude plugin install limitation-period-calculator@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- What you are filing (suit and its nature, appeal and from what, application, or the special-statute proceeding)
- The accrual facts with the document that fixes each date (breach, refusal, decree, award receipt, dispossession, knowledge)
- Today's date and the court
- Any signed acknowledgment or part-payment before expiry, time spent in a wrong forum, certified-copy dates

## What you get

- The provision chosen and why it fits
- A computation table: start, period, end without exclusions, days excluded, last date (on or before), status today
- Each exclusion or extension applied, with its section and dates
- What could still rescue a late filing (s.5 with sufficient cause, s.14, s.17, s.18/19, special-statute condonation) and what cannot (s.5 never for suits; outer limits under Arbitration s.34, IBC s.61, Companies Act s.421)
- A draft limitation paragraph or a s.5 application chronology

## Calculator

```bash
python3 scripts/limitation_calc.py --start 2019-06-01 --period 3y --exclude-covid
```

```bash
python3 scripts/limitation_calc.py --start 2026-01-15 --period 3m+30d
```

Periods: `90d`, `1m`, `3y`, or compounds like `3m+30d`. `--ack DATE` resets the start for a s.18/19 acknowledgment (refused if after expiry). `--exclude FROM:TO` removes s.14 wrong-forum days (repeatable). `--exclude-covid` applies the 15 March 2020 – 28 February 2022 exclusion and the 90-day floor from 1 March 2022. Counting conventions are in the script's docstring; court holidays are not applied.

## Example prompts

- "Builder promised possession by March 2021, never delivered, refund refused in writing on 2 Feb 2022. Can we still file a consumer complaint today?"
- "Award received on 14 July 2026, we want to challenge under s.34. Last date? Any way to get more time?"
- "Decree passed 10 Jan 2024, certified copy applied 12 Jan and received 2 Feb. Last date for the first appeal to the District Judge?"
- "Loan given in Jan 2021, borrower sent a WhatsApp in Dec 2023 saying he will pay. Is the suit time-barred?"

## Law covered

- Limitation Act, 1963 — ss.3–24, 29; Schedule Articles 14–22, 54–65, 70–76, 110–137
- Special statutes: Arbitration and Conciliation Act ss.11, 34(3), 37; Commercial Courts Act ss.12A, 13; NI Act s.142; Consumer Protection Act 2019 s.69; IBC ss.7, 9, 61, 62; Companies Act s.421; RERA ss.44, 58; RTI Act s.19; CGST Act ss.107, 112; Income-tax Act ss.249, 253; SARFAESI ss.17, 18; MV Act s.166(3); BNSS s.514
- *In re Cognizance for Extension of Limitation* (final order 10 January 2022) and the decisions listed in [references/case-law.md](references/case-law.md); periods tabulated in [references/articles-table.md](references/articles-table.md)

## Limits

- The calculator does not know court holidays or local High Court rules; it says "on or before" and points to s.4.
- It will not compute from an assumed accrual date.
- Criminal limitation on cognizance (BNSS s.514) is only flagged, not worked.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every computation before anything is filed or abandoned.
