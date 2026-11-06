# Quashing Petition (BNSS s.528) Advisor

Tells you whether an FIR, charge sheet, summoning order or criminal proceeding is realistically quashable by the High Court under BNSS s.528 (CrPC s.482 for matters pending on 1 July 2024), and drafts the petition when it is. It maps the case to the *Bhajan Lal* categories, tests every alleged offence's ingredients on the face of the record, separates the settlement track from the merits track, applies the *Neeharika* limits on interim protection, and — just as often — tells you that bail, discharge or compounding is the better tool.

For advocates, and for accused persons weighing a High Court petition.

## Install

```bash
claude plugin install quashing-petition-bnss-528@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- The FIR (and charge sheet / summoning order if any) — the actual documents, with sections and dates
- The stage of the case and the applicant's custody/bail position
- Every earlier application in the matter and its result
- For a settlement: the settlement document and whether the complainant will file an affidavit and appear

## What you get

- A route check: quashing vs bail vs discharge vs compounding vs appeal
- The code and forum (s.528 or s.482; Article 226 if needed; the High Court's nomenclature)
- *Bhajan Lal* category mapping and an ingredient-by-ingredient test of each offence
- The track (settlement or merits) with the controlling authorities
- A stage analysis with what interim relief can realistically be asked
- A draft petition: synopsis, list of dates, memo of parties, grounds, prayer, interim prayer, affidavit, annexure list
- Alternatives, defects and a sources-checked ledger

## Example prompts

- "My client's business partner filed an FIR for cheating and criminal breach of trust over a ₹40 lakh supply contract. There's a pending civil suit for the same money. Can we quash it in the Delhi High Court?"
- "498A FIR names my client, his parents and his married sister in Pune. Only vague allegations against the family. Draft a quashing application for the Bombay High Court."
- "The parties have settled a 326/BNS 118 hurt case. Charge sheet is filed. Is quashing on compromise possible and what does the complainant need to do?"

## Law covered

- BNSS, 2023 — ss.35(3), 173(3), 175, 218, 223, 250, 262, 268, 359, 514, 528, 531
- BNS, 2023 — ingredients of the commonly alleged offences (ss.85, 115–118, 303, 316, 318, 336–340, 351, 356)
- Article 226 of the Constitution where the relief runs against the State
- Key decisions: *Bhajan Lal*, *Gian Singh*, *Narinder Singh*, *Parbatbhai Aahir*, *Laxmi Narayan*, *Neeharika Infrastructure*, *Rajiv Thapar*, *Indian Oil v. NEPC*, *Paramjeet Batra*, *Preeti Gupta*, *Geeta Mehrotra*, *Achin Gupta*, *Kailashben Patel*, *Dara Lakshmi Narayana*, *T.T. Antony*, *Pepsi Foods*, *Sunil Bharti Mittal* — see [references/case-law.md](references/case-law.md)

## Limits

- It does not know your High Court's current rules, court fees or listing practice; it tells you to check them.
- It never promises quashing or protection from arrest; it calibrates the prospect in words and gives the alternatives.
- Appeals against conviction and revisions are out of scope.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every draft before it is filed.
