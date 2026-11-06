# Tells of a fabricated citation, and the verification protocol

Language models produce citations that are *shaped* like real ones. None of the tells below is conclusive on its own; three or more together make a citation presumptively fabricated until an official copy is opened.

## Tells

**In the case name**
- Generic or archetypal party names: *Sharma v. State*, *Kumar v. Union of India*, *ABC Ltd v. XYZ Ltd*, *Ramesh v. Suresh* — real cases have specific, often awkward names.
- A famous party in an unfamiliar pairing (*Kesavananda Bharati v. State of Maharashtra*) or a famous case with a slightly wrong name (*Maneka Gandhi v. State of India*).
- The name describes the subject (*Bank Fraud Victims Association v. RBI*).

**In the citation**
- Round numbers: `(2015) 5 SCC 500`, `AIR 2010 SC 1000`, `2020 INSC 100`.
- Impossible volume for the year: `(1985) 12 SCC 1` (SCC had far fewer volumes then); `(2031) …`.
- INSC serial number far above that year's output (e.g. `2022 INSC 4500`), or a pre-2023 INSC citation presented as if it had been cited that way at the time (pre-2023 numbers exist only because eSCR back-filled them — fine if it opens on eSCR, suspect if nothing else corroborates).
- A reporter that did not exist for that year (SCC before 1969; SCC OnLine citations for the 1970s) or a court that did not exist (Telangana High Court before 2019; a "Bombay High Court Nagpur bench" citation with a Goa code).
- Parallel citations that do not agree with each other (the SCC year and the AIR year differ by several years).
- A neutral citation with the wrong separator or code (`2023 DHC 1234`, `2024:DEL:1234`).

**In the holding**
- The case is said to decide *exactly* the proposition the drafter needed, in the drafter's own words.
- A sweeping principle attributed to a two-judge bench, or a constitutional holding attributed to a High Court.
- The quoted paragraph reads like a summary, not a judgment (judgments rarely say "the law is now settled that …" without lengthy context).
- No bench, no date, no judge — real citations usually come with at least one.

**In the quotation**
- Cannot be located by full-text search on Verdict Finder or the court's portal.
- Too clean: no "we are of the view", no cross-references, no "learned counsel".
- The pinpoint paragraph exists but says something else.

**In the pattern**
- Every authority in the draft is from the same two or three years, or every citation is SCC with a page ending in 0 or 5.
- Several cases cited together each exist individually but none is about the proposition.
- A citation that the user "found with AI" and cannot say where it came from.

## Verification protocol (do all five; record the result of each)

1. **Does the case exist?** Search the official portal — eSCR/sci.gov.in for the Supreme Court; the High Court's own site; judgments.ecourts.gov.in — by neutral citation, then case number, then parties. Confirm parties, court and date match. Result: VERIFIED / UNVERIFIED / NOT FOUND.
2. **Is the citation correct?** Reporter, year, volume, page or serial number against the official copy or the reporter's own table of parallel citations. Fix only what the copy supports.
3. **Does it say what is claimed?** Read the paragraph. Ratio or obiter? Majority or dissent? Bench strength? Then search for later treatment in the sources available (Verdict Finder by case name; the user's citator). Report as "no later treatment found in [sources] on [date]" — citator coverage is not promised.
4. **Is the quotation verbatim?** Character-level comparison with the copy cited, including ellipses, emphasis and paragraph number. A paraphrase in quotation marks is a misquote.
5. **Is the statute current?** India Code for the section as it stands; e-Gazette for commencement and amendment; BNS/BNSS/BSA numbering for matters instituted on or after 1 July 2024.

## What to say when a citation fails

- NOT FOUND after all three searches: "No judgment matching this citation or these parties was found on [portal] on [date]. Do not cite it. If you have a copy, share it and I will check it against the official record."
- Exists but the holding does not match: "The case exists but the paragraph relied on [states X / is obiter / is the dissent]. It does not support the proposition as framed."
- Exists but the quotation is wrong: give the verbatim text with pinpoint, and mark the draft's version as a misquote.
- Cannot be checked (no browsing): "UNVERIFIED — I could not open an official copy. Search [URL] by [parties/citation] before relying on it."
