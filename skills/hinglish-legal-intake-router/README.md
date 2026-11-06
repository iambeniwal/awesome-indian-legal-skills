# Hinglish Legal Intake Router

The front door of the library. A person who has never met a lawyer writes what happened — in Hindi, Hinglish (romanised Hindi) or plain English — and the skill replies in that same language and script, checks for danger and running deadlines first, asks at most three questions, names the legal issue in plain words, and hands over to the right skill in this collection by exact name. Where no skill covers the problem yet (tenancy, domestic violence, divorce and maintenance, land possession), it says so honestly and points to the official route and free legal aid.

For citizens, helpline volunteers, paralegals and anyone building a Hindi-first legal assistant on top of these skills.

## Install

```bash
claude plugin install hinglish-legal-intake-router@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory. It is most useful installed together with the skills it routes to.

## What it needs from you

- Your story, in whatever language you think in
- Answers to two or three short questions: when the key thing happened, which city/State, and what you want

It never asks for Aadhaar, OTPs, passwords or bank details.

## What you get

- A 5–8 line reply in your language: safety or deadline flag first, then "aapka mamla ___ ka hai", what the next step will ask for, one thing to keep and one thing not to do, and the free-legal-aid line if cost is a concern
- A machine-readable `Route: <skill-name>` line the agent uses to load the next skill

## Example prompts

- "police FIR nahi likh rahi, 3 baar thane gaya"
- "बिल्डर ने 3 साल से पज़ेशन नहीं दिया, पैसा वापस चाहिए"
- "cheque bounce ho gaya kya karu, memo kal mila"
- "company ne 2 mahine ki salary nahi di aur nikal diya"
- "My landlord is forcing me out with 5 days' notice, Pune"

## Law covered

Very little, on purpose — this skill routes. It carries a Hindi ↔ English glossary with the correct statutory terms (BNS/BNSS/BSA numbering since 1 July 2024; CPA 2019; RERA 2016; RTI Act 2005; Labour Codes; DPDP Act 2023) and an issue map of trigger phrases → skill → first question → deadline flag. Free legal aid: Legal Services Authorities Act, 1987 (NALSA / DLSA, 15100), Tele-Law, Nyaya Bandhu; cyber fraud: cybercrime.gov.in / 1930; emergencies: 112 / 181 / 1098.

## Limits

- It does not analyse, draft or predict; the receiving skill does that with its own verification step.
- Helpline numbers and portal names drift; the skill tells the agent to confirm they are current.
- No skills exist yet for tenancy, domestic violence, family law or land disputes — the router says so rather than forcing a near match.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — यह कानूनी सलाह नहीं है।
