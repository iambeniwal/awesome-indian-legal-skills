---
name: indian-case-citation-verifier
description: >
  Checks every Indian case citation, statute reference and quotation in a draft before it goes into a
  filing, opinion or article — does the case exist, is the citation in the right form (INSC and High
  Court neutral citations, SCC, AIR, SCR, SCC OnLine), does it hold what is claimed, is the quote
  verbatim, and is the statute section current (BNS/BNSS/BSA since 1 July 2024). Built for the
  AI-fabricated-citation problem that Indian courts have warned advocates about. Use whenever a user
  asks to verify, check, validate or "sanity check" citations or authorities, asks "is this a real
  case", "did the Supreme Court actually say this", wants a written submission, synopsis, legal
  opinion, article or AI-generated research checked before filing, or pastes a list of cases and
  asks which ones are genuine. Also use proactively before presenting any Indian case law you have
  generated yourself. Not a case-law research tool — it verifies what is already cited; it does not
  find new authorities.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Legal Research & Citations
  jurisdiction: IN
  states: all
  language: en
---

# Indian Case Citation Verifier

Produces a citation ledger for a draft: every authority and statute reference, its normalised form, whether it exists, whether it says what is claimed, whether any quotation is verbatim, and what to do about it. For advocates, law clerks, in-house counsel and students — and for any agent about to present Indian case law it generated.

> **Not legal advice.** This is a research aid under Indian law. A qualified advocate must independently confirm every authority before relying on it in court. Say this once at the start of the first response.

## Why this exists

Advocates in India have filed submissions containing non-existent cases produced by AI tools, and the Supreme Court and several High Courts have rebuked counsel for it. In 2026 the Supreme Court is reported to have described reliance on fabricated judgments as misconduct, set aside NCLT/NCLAT orders that rested on non-existent precedents, and directed the Bar Council of India to frame guidelines and disciplinary consequences for advocates who place unverified AI-generated authorities before a court — confirm the order on sci.gov.in before citing it, but take the direction as the baseline. An advocate's duty of candour to the court — not to mislead it or cite authorities known to be false — is part of the standards of professional conduct under the Bar Council of India Rules framed under the Advocates Act, 1961 (Chapter II of Part VI). A fabricated citation is a professional-conduct problem, not a typo. Treat every citation as unverified until an official copy has been opened.

## Jurisdiction gate

Indian authorities and statutes only. For foreign cases cited in an Indian draft (English, US, Australian), check the form and flag them "not verified here — use the foreign jurisdiction's official reporter", unless a browsing tool reaches BAILII, CourtListener or the equivalent.

## Verify before relying — sources in priority order

Existence and content are proven only from an **official copy**. Use these, in order, and record the date checked:

1. **Supreme Court** — judgments search at [sci.gov.in/judgements](https://www.sci.gov.in/judgements/) (neutral citation `YYYY INSC NNN`, introduced 2023 and assigned retrospectively to earlier judgments); **e-SCR** at [scr.sci.gov.in/scrsearch](https://scr.sci.gov.in/scrsearch/) for citation and keyword search (CAPTCHA-gated — the user must solve it; a CAPTCHA is not a login wall); [Verdict Finder](https://verdictfinder.sci.gov.in/) for full-text search; judgment PDFs are served from `api.sci.gov.in` — a direct PDF link from a results page is an official copy, but that host is not a search API
2. **High Courts** — each court's own judgment portal (search by neutral citation, case number or parties), then the e-Committee's national keyword search at [judgments.ecourts.gov.in/pdfsearch](https://judgments.ecourts.gov.in/pdfsearch/) (also CAPTCHA-gated)
3. **District courts and tribunals** — [eCourts Services](https://services.ecourts.gov.in/) orders and case status; the tribunal's own site (NCLT, NCLAT, TDSAT, CAT, ITAT). [NJDG](https://njdg.ecourts.gov.in/) is statistics, not a source of orders
4. **Statutes** — [India Code](https://www.indiacode.gov.in/) (canonical host; `indiacode.gov.in` is the legacy address and may show a migration notice); commencement and amendment notifications on [e-Gazette](https://egazette.gov.in/), which is intermittently unreachable — retry rather than conclude a notification does not exist
5. **Leads only, never proof** — Indian Kanoon, Casemine, LiveLaw, Bar & Bench, blogs; SCC OnLine and Manupatra are reliable but subscription-only and still not the official copy for a quotation check

If no browsing tool is available, the ledger may say **UNVERIFIED** and never **VERIFIED**; say plainly that existence could not be checked and hand the user the search links the script prints.

## Required inputs

- The draft, or the list of citations, pasted or as a file (blocking)
- For each quotation: the words claimed to be a quote and the paragraph/page pinpoint (blocking for the quote check)
- The proposition each case is cited for, if the draft does not make it obvious (needed for the holding check)
- Nice to have: the reporter the user has access to (SCC, AIR), the court and bench the draft is going to, the date the matter arose (for statute currency)

## Method

1. **Extract and form-check with the bundled script** — never by eye:
   ```bash
   python3 scripts/check_citation_format.py draft.md          # table
   python3 scripts/check_citation_format.py --json draft.md   # machine-readable
   printf '%s' "$TEXT" | python3 scripts/check_citation_format.py -
   ```
   It finds candidate citations (INSC, High Court neutral citations, SCC, SCR, AIR, SCALE, JT, SCC OnLine, MANU, and statute section references), checks their **form** only (plausible year and volume, numeric page, known court code, INSC number range, IPC/CrPC/IEA references flagged as repealed since 1 July 2024), and prints a verification URL hint for each. A clean form check is **not** proof of existence — it only removes the impossible ones (`(2031) 5 SCC 100`, `AIR 2019 SC` with no page). Read [references/citation-formats.md](references/citation-formats.md) when a form is unfamiliar.

2. **Existence check.** For each citation, search the official portal by neutral citation first, then by case number, then by parties. A case exists when an official copy with matching parties, court and date opens. Record source and date. Results are one of: **VERIFIED** (official copy opened), **UNVERIFIED** (no browsing or not reached), **NOT FOUND** (searched the official portal by all three routes and nothing matched). A hit on Indian Kanoon alone is UNVERIFIED with a lead noted.

3. **Citation correctness.** Compare reporter, year, volume and page against the copy (eSCR shows parallel citations; SCC and AIR headnotes print their own). Fix only what the official copy supports. Note parallel citations the user may prefer, and prefer the neutral citation plus one reporter.

4. **Holding check.** Read the paragraph relied on, not the headnote. Does it support the proposition, as a ratio or only as an observation, by a bench of what strength, and is it the majority? Look for later treatment in the sources available (Verdict Finder search by case name; the user's citator if any) and report as "no later treatment found in the sources checked on [date]" — never "not overruled". Flag anything superseded by statute (e.g. pre-2015 s.138 jurisdiction cases; IPC-era cases on provisions the BNS changed).

5. **Quotation check.** Compare the quoted words against the official copy **character by character**: ellipses, emphasis, bracketed insertions, paragraph number. SCC paragraph numbers differ from the official/eSCR numbering — the pinpoint must match the copy actually cited. A paraphrase in quotation marks is a misquote; say so and offer the verbatim text or a paraphrase without quotation marks.

6. **Statute currency.** For every section reference: is the Act current (IPC, CrPC and the Indian Evidence Act are repealed for matters instituted on or after 1 July 2024 — map through the `ipc-bns-section-mapper` skill if available, or India Code), is the section number right, has it been amended, and does the cited text match India Code? Flag repealed-Act references with the date rule rather than deleting them — a pre-July-2024 matter may correctly cite the IPC.

7. **Hallucination screen.** Run [references/hallucination-patterns.md](references/hallucination-patterns.md) over anything UNVERIFIED or NOT FOUND and over cases you generated yourself: generic party names, round page numbers, a holding that is exactly what the drafter needed, a volume number that does not exist for that year, an INSC number above that year's count, a bench that did not sit then, a quote nobody can locate. Several tells together make a citation presumptively fabricated — say so in those words.

## Output

```
# Citation check — [draft title] — [date]
## Read this before filing (plain language: how many authorities, how many VERIFIED / UNVERIFIED / NOT FOUND, which must go, what could not be checked and why)
## Citation ledger
| # | As cited | Normalised | Form | Existence (status · source · date) | Holding matches? | Quote verbatim? | Action |
## Corrected citations (ready to paste; neutral citation + one reporter where available)
## Statute references (section, Act, current? amended? mapped?)
## Could not be checked (and the exact search the user should run)
## Sources checked (portal, date)
```

For one or two citations, collapse to the ledger rows and the action lines.

## Guardrails

- Never mark a citation **VERIFIED** without having opened an official copy in this session; "I recall this case" is UNVERIFIED.
- Never repair a citation by guessing a plausible one. If the official portal does not return it, write **NOT FOUND** and say what was searched.
- Never say a case "has not been overruled" or "is good law"; say what later treatment was found in which sources on which date, and that citator coverage is not promised.
- Never present a paraphrase as a quotation; never trim a quotation to change its sense.
- Do not delete repealed-Act references silently; apply the 1 July 2024 date rule and explain.
- Treat your own generated case law as the highest-risk input and run it through the same ledger before showing it.
- Do not reproduce long passages of judgments; quote only what the draft quotes, for the comparison.

## References

- [references/citation-formats.md](references/citation-formats.md) — forms of Supreme Court, High Court, reporter and statute citations, with examples and the neutral-vs-reporter distinction. Read it when normalising.
- [references/hallucination-patterns.md](references/hallucination-patterns.md) — the tells of a fabricated citation and the five-step verification protocol. Read it for every UNVERIFIED or NOT FOUND entry.
- [scripts/check_citation_format.py](scripts/check_citation_format.py) — extractor and form checker; `--json` for structured output.
