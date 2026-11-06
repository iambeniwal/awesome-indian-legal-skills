# RTI Application, First Appeal and Second Appeal Drafter

Turns "I want to know what the department did with my file" into an RTI application a PIO cannot dodge — precise, numbered questions for records that exist, the likely s.8 exemption pre-empted, the fee and portal for the right track (Central or State), and a deadline table for the reply and both appeals. When the reply is late, incomplete or wrong, it drafts the first appeal and the second appeal to the Information Commission, and answers the standard refusals.

For citizens, journalists, advocates and anyone dealing with a ministry, PSU, municipality, university, police or court registry.

## Install

```bash
claude plugin install rti-application-drafter@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Which body holds the records, and whether it is Central or State
- What you actually want to know, in your own words
- Dates and any reply text if you have already filed

## What you get

- Draft application in the rtionline layout (applicant, authority, numbered particulars, period, form, fee, citizenship declaration)
- Deadline table: PIO reply (30 days / 48 hours / 35 / 40), deemed refusal, first appeal (30 days), FAA decision (30–45 days), second appeal (90 days)
- Likely objections and the section-and-case answer to each
- First appeal or second appeal with numbered grounds and relief (free information under s.7(6), penalty under s.20)
- Attachments checklist and a sources-checked ledger

## Calculator

```bash
python3 scripts/rti_deadlines.py --applied 2026-09-01 --reply 2026-10-05 --first-appeal 2026-10-20
```

Add `--route apio`, `--third-party`, `--life-liberty`, `--fee-gap-days N` as applicable; `--json` for structured output.

## Example prompts

- "My pension file has been pending with the Accountant General for 8 months. Draft an RTI to find out where it is stuck."
- "I filed an RTI with the municipal corporation on 3 September, no reply. What now?"
- "The CPIO refused under 8(1)(j) saying the tender evaluation sheet is personal information. Draft the first appeal."

## Law covered

- Right to Information Act, 2005 — ss.2(f), 2(h), 2(j), 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 24, Second Schedule
- RTI Rules, 2012 (Central fees); RTI Rules, 2019 (Commissioners); State RTI Rules (fees vary)
- Digital Personal Data Protection Act, 2023, s.44(3) (amendment to s.8(1)(j) — commencement to be checked)
- Key decisions: *Aditya Bandopadhyay*, *Khanapuram Gandaiah*, *Girish Ramchandra Deshpande*, *Subhash Chandra Agarwal*, *Shaunak Satya*, *Thalappalam*, *CIC v. State of Manipur*, *Jayantilal Mistry* — see [references/case-law.md](references/case-law.md)

## Limits

- Only public authorities and only citizens; it tells you when your target is outside the Act.
- Does not know your State's fee or payment instrument — it tells you to read the State Rules.
- Cannot predict Information Commission hearing dates; backlogs are real.
- Does not file anything.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every draft before it is relied on or filed.
