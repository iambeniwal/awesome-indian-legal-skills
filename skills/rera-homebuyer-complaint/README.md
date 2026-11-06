# RERA Homebuyer Complaint (and Promoter Reply)

Takes a delayed, defective or stalled flat booking through the Real Estate (Regulation and Development) Act, 2016: checks the project's registration, picks the forum (RERA Authority, Adjudicating Officer, consumer commission or NCLT), forces the refund-or-stay election under s.18, computes months of delay and interest at the State's prescribed rate with a bundled calculator, and drafts a State-portal-ready complaint — or the promoter's reply.

For advocates, and for allottees filing on a State RERA portal themselves.

## Install

```bash
claude plugin install rera-homebuyer-complaint@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Project, promoter, **State**, and the RERA registration number (or what you searched)
- Agreement for sale: date, promised possession date, grace clause
- Every payment with its date; total consideration
- OC/CC status, any offer of possession, construction stage
- Whether you want a refund with interest (exit) or to keep the unit and claim delay interest

## What you get

- Forum and relief memo (with the Authority / Adjudicating Officer / consumer / NCLT decision table)
- Delay and interest table from the calculator, with the rate source named
- Draft complaint in the common State-form structure, or a para-wise promoter reply
- Documents checklist, defect list, promoter-side risks, and the State-rule items to verify (rate, fee, form, portal)

## Example prompts

- "Booked a 2BHK in Noida in 2019, possession promised Dec 2022 with 6 months grace. Paid ₹58 lakh. No OC yet. I want to exit. What can I claim under RERA and how?"
- "Pune project, builder offered possession in March but there's no OC. We'd rather keep the flat. Draft the MahaRERA complaint for delay interest."
- "We're the promoter. Reply to this UP-RERA complaint — the allottee stopped paying after the 4th demand and the Authority gave us a 9-month COVID extension."

## Calculator

```bash
python3 scripts/rera_delay.py --promised 2022-12-31 --grace-months 6 --rate 10.85 --mode delay --paid 2019-03-10:1500000 --paid 2020-01-15:2500000
```

`--mode refund` charges interest from each payment date; `--mode delay` from the effective due date. The rate is always an input — look up the State rule (usually SBI highest MCLR + 2%) and the current MCLR. Add `--json` for structured output.

## Law covered

- RERA, 2016 — ss.2, 3, 4(2)(l)(D), 6, 11–14, 17–19, 31, 37, 40, 43–44, 58–64, 71, 79, 88–89
- Consumer Protection Act, 2019 (concurrent route); IBC s.7 (allottees as financial creditors)
- *Newtech Promoters*, *Imperia Structures*, *Experion Developers*, *Pioneer Urban* (both), *Ireo Grace*, *Manish Kumar*, *Forum for People's Collective Efforts* — see [references/case-law-and-forums.md](references/case-law-and-forums.md)

## Limits

- State Rules, fees, forms and portals differ; the skill tells you what to verify, it does not know every State's current figures.
- Not for title disputes, tenancy or commercial leases.
- Does not file anything on a portal.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every figure and draft before it is relied on or filed.
