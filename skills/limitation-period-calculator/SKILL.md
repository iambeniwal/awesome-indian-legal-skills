---
name: limitation-period-calculator
description: >
  Works out whether an Indian suit, appeal or application is within time under the Limitation Act, 1963
  or the governing special statute, and gives the last date to file. Picks the Article of the Schedule
  (or the special-law period: Arbitration Act s.34/37, Commercial Courts Act, Consumer Protection Act
  s.69, NI Act s.142, IBC s.61, RERA s.44, Companies Act s.421, RTI, GST, income-tax, MV Act s.166),
  applies s.12, s.14, s.17, s.18/19, s.4, ss.6–8 and s.22, and the Supreme Court's COVID-19 exclusion
  (15 March 2020 – 28 February 2022), with a bundled calculator. Use whenever a user asks "is it
  time-barred", "limitation period for ...", "last date to file the appeal", "can we still sue", "delay
  condonation", "kitne din me appeal file karni hai", "time bar ho gaya kya", or needs a limitation
  paragraph for a plaint, appeal or s.5 application. Says what can still save a late case and what
  cannot (s.5 never applies to suits). Criminal cognizance limitation (BNSS s.514) only by pointer.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Civil Procedure & Limitation
  jurisdiction: IN
  states: all
  language: en
---

# Limitation Period Calculator

Produces a limitation table (provision → period → start → exclusions → last date → status today), the reasoning for the Article chosen, and a plain list of what could still rescue a late filing. For advocates, litigants and in-house teams deciding whether and when to file.

> **Not legal advice.** This is a research and calculation aid under Indian law. Limitation is fatal and fact-sensitive — the accrual date, the Article and the exclusions all turn on facts and on the court's own calendar. A qualified advocate must review every computation before anything is filed or abandoned. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only. Identify the State and the court: s.4 turns on that court's holiday calendar, several High Courts have Letters Patent or local amendments affecting appeal periods, and State Acts (rent control, land revenue, cooperative societies) carry their own periods. If the governing law or forum is foreign or unclear, stop and say so.

## Verify before relying

The Article and the period must be read from the statute, not recalled. Before stating any period as current, check and record the date checked:

- Limitation Act, 1963 — ss.3–24 and the Schedule: [India Code](https://www.indiacode.gov.in/). Read the Article's three columns (description, period, time from which it runs) in full.
- The special statute's own period and whether it excludes ss.4–24 (s.29(2)): e.g. Arbitration and Conciliation Act s.34(3), Commercial Courts Act s.13, IBC s.61, Consumer Protection Act s.69 — India Code.
- The COVID-19 orders: *In re Cognizance for Extension of Limitation*, Suo Motu W.P.(C) 3/2020, final order of 10 January 2022 (2022) 3 SCC 117 — [sci.gov.in](https://www.sci.gov.in/).
- Controlling decisions on condonation and computation: summarised in [references/case-law.md](references/case-law.md).

If no browsing tool is available, say the periods are from the skill's version date and must be verified.

## Required inputs

Ask for the blocking ones together, in plain language.

**Blocking:**
- What is being filed: suit (and its nature — money, specific performance, possession, declaration, injunction), appeal (from what, to which court), application (which one), or a special-statute proceeding
- The **accrual facts**: the date of breach, refusal, dispossession, the decree/order date, the date of the award, the date of knowledge where s.17 or Article 59/123 applies — with the document that fixes each date
- Today's date and the court
- Any written, signed acknowledgment or part-payment before expiry (s.18/19), and its date

**Nice to have:** certified-copy application and delivery dates (s.12(2)–(4)), any earlier proceeding in a wrong forum with its institution and disposal dates (s.14), the plaintiff's age or disability at accrual (s.6–8), whether the wrong is continuing (s.22), whether the respondent is a government (Article 112; s.80 CPC notice period is excluded under s.15(2)).

Without the accrual date and the nature of the proceeding, give the candidate Articles and what fixes the date — do not compute.

## Method

1. **Fix the nature of the proceeding first, then the Article.** The Schedule is organised by the nature of the suit (contracts, declarations, immovable property, trusts, torts, residuary Article 113), then appeals (Articles 114–117), then applications (Articles 118–137, residuary 137). Read [references/articles-table.md](references/articles-table.md) to shortlist, then read the Article's text on India Code. Where two Articles could apply, the specific one prevails over the residuary; say which you chose and why. The description is what the plaintiff really seeks, not the label on the plaint.

2. **Fix the accrual date from a document.** Limitation runs from the date in the third column of the Article — the breach, the refusal, the date fixed for performance, the dispossession, the decree — not from when the client found out, unless s.17 (fraud, concealment, mistake) or an Article that itself runs from knowledge (Article 59, Article 123 proviso) applies. State the document that proves the date.

3. **Run the calculator** and paste its table:
   ```bash
   python3 scripts/limitation_calc.py --start YYYY-MM-DD --period 3y [--exclude-covid] [--ack YYYY-MM-DD] [--exclude YYYY-MM-DD:YYYY-MM-DD] [--today YYYY-MM-DD] [--json]
   ```
   `--period` takes `90d`, `1m`, `3y`, or compounds like `3m+30d` (Arbitration s.34). `--exclude-covid` applies the Supreme Court's exclusion of 15 March 2020 to 28 February 2022 (and the 90-day floor from 1 March 2022). `--ack` resets the start to the s.18/19 acknowledgment date (only if it falls before expiry; the script refuses otherwise). `--exclude` removes s.14 days spent in a wrong forum, counting both the institution and disposal days. The script applies s.12(1) (the day from which the period runs is excluded) and calendar months; it does not know court holidays, so the "last date" is "on or before", and s.4 moves a holiday to the next day the court is open.

4. **Apply the exclusions and extensions you have facts for**, and name the section for each: s.12(2)–(4) time for certified copies (appeals, revisions, reviews, awards — the day of the judgment and the copy time are excluded); s.14 (civil proceeding, bona fide, due diligence, same relief, dismissed for want of jurisdiction or like cause — applies to suits and applications, and to Arbitration s.34 applications per *Consolidated Engineering*); s.15 (stay, s.80 notice period, leave of court); s.17; s.18/19 (fresh period from a signed acknowledgment or a payment recorded in writing, both before expiry — an acknowledgment after expiry revives nothing); s.21 (added parties); s.22 (continuing breach or tort: a fresh period every moment the wrong continues, but damages are limited to the period within limitation); ss.6–8 (disability at accrual, s.8 caps at three years after it ceases; s.9 once time runs no later disability stops it).

5. **Say what can still save a late case, and what cannot.** s.5 condonation applies to appeals and applications (not Order XXI execution applications) on "sufficient cause" — never to suits (s.3 is mandatory, the court dismisses even if limitation is not pleaded). Under special statutes read s.29(2): where the Act says "but not thereafter" or fixes an outer limit (Arbitration s.34(3): three months plus thirty days — *Simplex Infrastructure*, *Popular Construction*; IBC s.61: thirty plus fifteen days; Companies Act s.421: forty-five plus forty-five), no further condonation is possible, though s.14 may still exclude time and the COVID exclusion also applies to outer limits (direction IV of the 10 January 2022 order). For Commercial Courts Act appeals, s.5 applies but condonation is exceptional and only for short, explained delays (*Borse Brothers*). Explain "sufficient cause" liberally for litigants but demand a day-by-day explanation for government and institutional parties.

6. **Write the limitation paragraph** for the plaint, appeal or s.5 application: the Article/provision, the accrual date and document, each exclusion with its section and dates, the resulting last date, and the filing date. For a s.5 application, add a chronology of the delay and the cause for each segment.

## Output

```
# Limitation — [proceeding] — [parties]
## Answer (plain language: in time / out of time by N days / cannot say until X is known; last date to file)
## Provision chosen (Article or special-law section → why it fits → period → runs from → source and date checked)
## Computation table (output of limitation_calc.py: start, period, naive end, exclusions, last date, status)
## Exclusions and extensions applied (section → facts → dates → document)
## What could still save a late filing / what cannot
## Draft limitation paragraph (or s.5 application chronology)
## Facts and documents still needed
## Sources checked
```

For a one-line question ("limitation for a cheque bounce complaint?") collapse to the provision, the period, where it runs from, and the pointer to verify.

## Guardrails

- Never pick an Article from memory of a keyword; read the three columns and state why the facts fit.
- Never compute from an assumed accrual date; if the user has not fixed it with a document, give the candidates and stop.
- Do not say s.5 can condone delay in a suit, or that an outer-limit special statute can be condoned beyond its cap.
- Do not apply the COVID exclusion silently; show the dates and the days added, and the 90-day floor if it bit.
- Do not treat an unsigned or post-expiry acknowledgment as a s.18 acknowledgment.
- Court holidays are the court's calendar, not the agent's; state "on or before" and point to s.4.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/articles-table.md](references/articles-table.md) — the most-used Articles of the Schedule and the special-statute periods, with what the period runs from and whether condonation is available. Read it to shortlist, then read India Code.
- [references/case-law.md](references/case-law.md) — controlling decisions on computation, condonation, s.14, s.18, special statutes and the COVID orders.
- [scripts/limitation_calc.py](scripts/limitation_calc.py) — the calculator; `--json` for structured output. Its docstring states the counting conventions.
