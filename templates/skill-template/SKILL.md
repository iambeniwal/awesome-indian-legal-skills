---
name: skill-template
description: >
  One or two sentences on what the skill does, then the situations and user phrases that should
  trigger it — include Hindi/Hinglish phrasings users actually type. State what it does NOT cover
  so the agent routes elsewhere. This field is the trigger; keep the "when to use" here, not in the body.
license: MIT
metadata:
  author: Your Name
  author_url: https://github.com/you
  version: "2026.11.06"
  category: Legal Drafting
  jurisdiction: IN
  states: all
  language: en
---

# Skill Title

One paragraph: what this skill produces and for whom (advocate, in-house counsel, litigant in person).

> **Not legal advice.** This skill is a research and drafting aid under Indian law. A qualified advocate must review every interpretation, citation and draft before it is relied on, sent or filed. Say this once at the start of the first response; do not repeat it in every message.

## Jurisdiction gate

This skill applies Indian law only. Confirm the matter is governed by Indian law, and identify the State/UT and the competent forum — many fees, court rules and limitation nuances are State-specific. If the governing law is foreign or unclear, say so and stop.

## Verify before relying

Section numbers, fees, pecuniary limits and timelines change. Before stating any of them as current, check the official source and note the date checked:

- Statute text and amendments: [India Code](https://www.indiacode.nic.in/)
- Commencement notifications and rules: [e-Gazette](https://egazette.gov.in/)
- Supreme Court decisions: [sci.gov.in](https://www.sci.gov.in/) (neutral citation `YYYY INSC NNN`)
- *(add the forum- or regulator-specific portal for this skill)*

If no browsing tool is available, say the figures are from training knowledge as of the skill's version date and must be verified.

## Required inputs

List what to ask for. Mark which inputs are **blocking** (without them, produce a defect list instead of a draft) and which are nice-to-have. Ask for the blocking ones first, in one batch, in plain language.

## Method

1. Step one — and *why* it matters (e.g. "territorial jurisdiction follows the payee's bank branch under s.142(2), so the drawer's address is irrelevant").
2. Step two.
3. ...

## Output

State the exact structure to produce. A heading skeleton works well:

```
# [Title]
## Summary (3–5 lines, plain language)
## Facts relied on (user-supplied, dated)
## Law applied (section, Act, source checked, date checked)
## Analysis / Draft
## Open points and documents still needed
## Next steps and deadlines
```

## Guardrails

- Do not fabricate facts, dates, service, receipt, or citations. Mark anything unverified.
- Separate what the user said, what the statute says, and what you infer.
- Do not reproduce long statutory text verbatim; cite the section and summarise.
- *(skill-specific guardrails)*

## References

- [references/example.md](references/example.md) — when to read it and what it contains. *(delete if unused)*
