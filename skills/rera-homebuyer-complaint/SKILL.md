---
name: rera-homebuyer-complaint
description: >
  Audits and drafts a homebuyer (allottee) complaint under the Real Estate (Regulation and
  Development) Act, 2016 for delayed possession, refund with interest, defects, false promises or
  unregistered projects — and the promoter's reply. Picks the right forum (RERA Authority vs
  Adjudicating Officer vs consumer commission vs NCLT), forces the refund-or-stay election under
  s.18, computes months of delay and interest with the bundled calculator at the State's prescribed
  rate, and produces a State-portal-ready complaint with documents list. Use whenever a user
  mentions a builder, developer, flat/apartment/plot booking, "possession delayed", "builder
  refund", "RERA complaint", "RERA mein case", "OC nahi mila", "builder paisa nahi de raha",
  "defect in flat", or wants to reply to a RERA complaint as a promoter. Not for title disputes,
  landlord–tenant matters, or commercial lease disputes — say so and route elsewhere.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Real Estate & RERA
  jurisdiction: IN
  states: all
  language: en
---

# RERA Homebuyer Complaint (and Promoter Reply)

Produces a forum-and-relief memo, a delay-and-interest table, and a draft complaint (or promoter's reply) under the Real Estate (Regulation and Development) Act, 2016. For advocates, and for allottees filing on a State RERA portal themselves.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate must review every interpretation, figure and draft before it is relied on or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only, and **State-specific**: RERA is a Central Act but each State/UT has its own Authority, Rules, prescribed interest rate, complaint forms and fees. Identify the State where the project is located before anything else. If the user cannot say, ask — the answer changes the rate, the fee and the portal.

## Verify before relying

- The Act (ss.2, 3, 4, 11–19, 31, 40, 43–44, 58–63, 71, 79, 88–89): [India Code](https://www.indiacode.gov.in/)
- The **State RERA Rules** (prescribed interest rate, complaint form, fee, agreement-for-sale model) and the **State portal** (project registration search, online filing, Authority orders including COVID/force-majeure extensions): find it from the State's RERA website (MahaRERA, UP-RERA, K-RERA, HRERA Gurugram/Panchkula, TNRERA, RERA Punjab, Gujarat RERA, Delhi RERA, etc.). Do not rely on a portal URL from memory; search for "<State> RERA" and confirm the domain ends in a government domain.
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); the ones this skill leans on are summarised in [references/case-law-and-forums.md](references/case-law-and-forums.md).

If no browsing tool is available, state that the rate, fee and portal details come from the skill's version date and must be verified before filing.

## Required inputs

Ask for the blocking ones together, in plain language.

**Blocking (no draft without them — produce a defect list instead):**
- Project name, promoter name, **State**, and the project's RERA registration number (or the user's statement that they could not find it on the portal)
- Agreement for sale / allotment letter / builder-buyer agreement: date, **promised possession date**, grace-period clause, and whether it is registered
- Amounts paid: each tranche with date and receipt/demand reference; total consideration
- Current status: construction stage, OC/CC status, any offer of possession and its date, any possession taken
- What the allottee wants: **refund with interest and exit** (s.18(1) withdrawal) or **keep the unit and claim interest for every month of delay** — this is an election with consequences; explain and get an answer

**Nice to have:** promoter's letters on force majeure/extension, project's registered completion date on the portal, any revised completion date granted by the Authority, bank loan details (pre-EMI burden), any consumer/IBC/arbitration proceedings already started, defect photos and dates (for s.14), brochure/advertisement copies (for s.12).

## Method

1. **Registration check.** Search the project on the State portal. If registered: note the registration number, the promoter's declared completion date and any extension granted under s.6 or by a COVID-era order. If not found: the project may be exempt (s.3(2): land ≤ 500 sq m *and* ≤ 8 apartments, or completion certificate received before 1 May 2017), may have registered under a different name/phase, or may be unregistered (s.59 penalty up to 10% of project cost). Never assert "unregistered" from one failed search; say what was searched and ask the user to confirm on the portal. *Newtech Promoters* settled that RERA applies to projects that were ongoing on 1 May 2017.

2. **Choose the forum** with the decision table in [references/case-law-and-forums.md](references/case-law-and-forums.md). In short: refund with interest, delay interest and directions → the **Authority** under s.31 (s.18 relief is enforceable by the Authority — *Newtech*); **compensation** under ss.12, 14, 18, 19 → the **Adjudicating Officer** under s.71 (the Authority cannot award compensation); defects, deficiency, unfair trade practice, or a buyer who prefers the consumer route → **Consumer Commission** (concurrent — s.88; *Imperia Structures*, *Experion*; 2-year limitation under s.69 CPA 2019); insolvency of the promoter with 100 allottees or 10% of the project's allottees joining → **NCLT** under s.7 IBC (*Pioneer Urban*). An arbitration clause in the agreement does not oust RERA or the consumer forum. **Before drafting anything, check whether the promoter is already in CIRP or liquidation** (NCLT cause lists and orders, the IBBI public announcements, the project's RERA page): once a s.14 IBC moratorium is in force, a fresh RERA or consumer complaint against the promoter is barred and the allottee's remedy is to file a claim with the IRP/RP in Form CA within the claim window — say so and switch to that track. Civil courts are barred by s.79. RERA itself has no express limitation period, but Authorities have refused stale claims; file promptly and say so.

3. **Force the s.18 election.** Refund mode: the allottee withdraws, gets back every amount paid **with interest at the prescribed rate from the date of each payment** (most State Rules: SBI's highest MCLR + 2% p.a. — confirm the State rule and the current MCLR), and may claim compensation separately before the AO. Stay mode: the allottee keeps the unit and gets interest at the same rate **on amounts paid, for every month of delay** until possession is handed over. A buyer cannot have both. Explain the trade-off (refund ends the pre-EMI/loan exposure but loses the unit and any appreciation; stay keeps the unit but depends on the promoter actually finishing). One-sided clauses capping delay compensation at a token rate do not bind (*Pioneer Urban v. Govindan Raghavan*, *Ireo Grace Realtech*).

4. **Compute the delay and the money with the bundled calculator** and paste its table:
   ```bash
   python3 scripts/rera_delay.py --promised 2022-12-31 --grace-months 6 --extension-months 0 --rate 10.85 --mode delay \
       --paid 2019-03-10:1500000 --paid 2020-01-15:2500000 --paid 2021-06-01:1000000 [--until 2026-11-06]
   ```
   Effective due date = promised date + grace period (only if the clause is unconditional) + any extension actually granted by the Authority (COVID orders in 2020–21 commonly added 6–9 months; check the State Authority's orders, not the promoter's letter). `--mode delay` charges simple interest on each tranche from the effective due date to possession/today; `--mode refund` charges from each payment date to the refund date. The rate is **always** an input: name its source (State Rule number + SBI MCLR on the date checked) in the output. If the script is unavailable, compute by hand, show each step, mark unverified.

5. **Check the promoter's side before drafting** so the complaint is not ambushed: allottee default under s.19(6)–(7) (unpaid demands attract interest at the same rate and can justify termination after notice); s.19(10) duty to take possession within two months of OC; a genuine force-majeure extension under s.6; an offer of possession with OC that the allottee ignored. If any of these bite, say so plainly and adjust the relief.

6. **Draft the complaint** in the structure most State forms share (the portal will ask for the same fields): forum; complainant and respondent particulars (promoter's registered address from the portal); project name and registration number; facts in dated paragraphs tied to documents; the breach (s.18 delay; s.12 false representation; s.13 >10% without registered agreement; s.14 defects within 5 years of possession; s.17 conveyance not executed within three months of OC; s.11 non-disclosure); relief sought in numbered prayers (refund with interest at the prescribed rate from each payment date / delay interest per month until possession / direction to hand over possession with OC / rectification of defects within 30 days under s.14(3) / costs); interim relief (restrain creation of third-party rights in the unit; direct the promoter to continue construction); declaration and verification; list of documents; fee (commonly ₹1,000–₹5,000 — verify on the State portal). For compensation, draft a separate AO complaint (or the combined form where the State allows it).

7. **Promoter's reply mode.** Para-wise admit/deny; defences: allottee's own default (s.19(6)), force majeure with the Authority's extension order, offer of possession with OC on a date earlier than alleged (delay stops there), the complainant not being an "allottee" (investor/assignee issues), the relief being compensation (AO, not Authority), parallel proceedings and settlements, limitation/laches. Without-prejudice settlement options: revised possession date with monthly interest credited against dues; swap unit; refund in instalments.

8. **Explain enforcement and appeal.** Authority/AO orders are recoverable as arrears of land revenue (s.40); non-compliance attracts daily penalties (ss.63–64). Appeal lies to the Real Estate Appellate Tribunal within 60 days (s.44(2)), and a promoter must first deposit at least 30% of the penalty or the full amount payable to the allottee with interest and compensation (s.43(5)); further appeal to the High Court within 60 days (s.58). Give the allottee the realistic timeline (s.71 says 60 days for the AO; Authorities vary).

## Output

```
# RERA — [Complaint | Reply] — [Allottee] v. [Promoter], [Project], [State]
## Summary (plain language, 3–5 lines: forum, relief, months of delay, approximate money, biggest risk)
## Facts relied on (dated, with the document for each)
## Registration status (portal searched, number, declared/extended completion date, date checked)
## Forum and relief (decision table applied; s.18 election recorded)
## Delay and interest table (output of rera_delay.py; rate source named; State rule cited)
## Draft [complaint | AO complaint | reply]
## Documents checklist (with what is still missing)
## Defects and risks (promoter-side points that bite)
## Next steps (portal, fee, timeline, appeal route)
## State-rule items to verify (rate, fee, form, portal)
```

## Guardrails

- Never compute interest without naming the rate, its source (State Rule + SBI MCLR date) and the State. Mark any rate from memory as "(verify)".
- Never tell a buyer they can take the refund with interest **and** keep the unit. Record the election.
- Never assert the project is unregistered from a single search; say what was searched.
- Keep the Authority/AO split straight: compensation is the AO's; refund and interest are the Authority's (*Newtech*).
- Do not fabricate payment dates, OC dates or portal entries; do not ignore the allottee's own defaults.
- Do not promise outcomes or timelines beyond the statute's targets.
- Do not reproduce long statutory text; cite and summarise.

## References

- [references/case-law-and-forums.md](references/case-law-and-forums.md) — forum decision table, the controlling decisions (*Newtech*, *Imperia*, *Experion*, *Pioneer Urban*, *Ireo Grace*, *Forum for People's Collective Efforts*), and the State-specific items to look up. Read before the forum section.
- [scripts/rera_delay.py](scripts/rera_delay.py) — delay and interest calculator; `--json` for structured output.
