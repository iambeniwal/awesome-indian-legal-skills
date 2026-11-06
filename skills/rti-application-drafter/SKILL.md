---
name: rti-application-drafter
description: >
  Drafts Right to Information applications, first appeals and second appeals/complaints under the
  RTI Act, 2005, and replies to common refusals. Identifies whether the body is a "public
  authority", turns a vague ask into precise numbered questions that a PIO cannot dodge, anticipates
  the s.8 exemption likely to be claimed and pre-empts it, computes the 30-day / 48-hour / 35-day /
  40-day reply deadlines and the 30-day and 90-day appeal windows, and tells the user what to do
  when there is no reply (deemed refusal). Use whenever a user mentions RTI, "file an RTI", "RTI
  daalna hai", "PIO", "CPIO", "first appeal", "second appeal to CIC/SIC", "information commission",
  "government is not giving me the information/file/marks/answer sheet", or wants records from a
  ministry, department, municipality, PSU, university, police or court. Not for requests aimed at
  private individuals or private companies that are not public authorities — say so and route to
  other remedies.
license: MIT
metadata:
  author: Rahul Beniwal
  author_url: https://github.com/iambeniwal
  version: "2026.11.06"
  category: Public Law & RTI
  jurisdiction: IN
  states: all
  language: en
---

# RTI Application, First Appeal and Second Appeal Drafter

Produces a filing-ready RTI application, first appeal or second appeal/complaint under the Right to Information Act, 2005, with a deadline table and a list of the objections the PIO is likely to raise. For citizens, journalists, advocates and in-house teams dealing with any public authority.

> **Not legal advice.** This is a research and drafting aid under Indian law. A qualified advocate must review every interpretation before it is relied on, sent or filed. Say this once at the start of the first response.

## Jurisdiction gate

Indian law only, and only against a **public authority** under s.2(h): a body established by the Constitution, by law, or by a Government notification, or one owned, controlled or **substantially financed** by the Government, including NGOs substantially financed by it (*Thalappalam*). A private bank, a private school, a housing society or an individual is not a public authority — tell the user so and point to the regulator, a civil remedy or a complaint instead. Only **citizens** may apply (s.3); a company or foreign national applies through a citizen in their own name.

State and Central tracks differ: Central ministries, PSUs and bodies under the Union use the RTI Rules, 2012 and [rtionline.gov.in](https://rtionline.gov.in/); State public authorities use the **State RTI Rules** (fee, payment modes, forms) and the State Information Commission. Identify which track applies before quoting a fee or a portal.

## Verify before relying

Check and record the date checked:

- Act text, especially ss.2(f), 2(h), 2(j), 6, 7, 8, 9, 10, 11, 18, 19, 20, 24 and the Second Schedule: [India Code — RTI Act, 2005](https://www.indiacode.gov.in/).
- **s.8(1)(j) has been amended by s.44(3) of the Digital Personal Data Protection Act, 2023** to read simply "information which relates to personal information", dropping the public-interest and "larger public interest" qualifiers. This is a significant narrowing for requests about officials' personal information. Check on [e-Gazette](https://egazette.gov.in/) whether s.44(3) has been brought into force (the DPDP Act commences in phases) before telling a user that the old *Girish Ramchandra Deshpande* balancing test still applies.
- Central fee and copying charges: RTI Rules, 2012 (₹10 application; ₹2 per A4/A3 page; actual cost for larger copies; first hour of inspection free, ₹5 per further 15 minutes; no fee for persons below the poverty line, s.7(5)). State fees vary — read the State's rules; some States charge more and accept different instruments.
- The 2019 Amendment: term, salary and conditions of Information Commissioners are now prescribed by the Central Government (RTI Rules, 2019 fixed a three-year term). Relevant only if the user is litigating the Commission's independence.
- Supreme Court decisions by neutral citation on [sci.gov.in](https://www.sci.gov.in/); see [references/case-law.md](references/case-law.md).

If no browsing tool is available, say figures come from the skill's version date and must be verified.

## Which mode?

| Situation | Mode | Output |
|---|---|---|
| No application yet | **Application** | Precision-drafted application + deadline table + likely objections |
| Reply received and unsatisfactory, or no reply within time | **First appeal** | First appeal to the First Appellate Authority (s.19(1)) |
| First appeal decided or ignored | **Second appeal** | Second appeal to CIC/SIC (s.19(3)) and/or complaint (s.18) |
| PIO sent a refusal/fee demand/transfer | **Reply** | Point-by-point response to the objection |

## Required inputs

Ask for the blocking ones first, together, in plain language.

**Blocking:**
- Which body holds the records, and whether it is Central or State (department, PSU, university, municipality, police, court registry)
- What the user actually wants to know, in their own words, and roughly why (not for the application — s.6(2) says no reasons are needed — but to turn the ask into the right questions)
- Dates: application filed, fee paid, reply received, first appeal filed, FAA decision — whichever exist
- Any reply/refusal text received, verbatim

**Nice to have:** file/reference numbers, the name of the scheme/tender/exam, the period the records cover, whether the user needs inspection, certified copies, or electronic copies (s.2(j) covers all), BPL status, whether life or liberty is at stake (48-hour track, s.7(1)).

## Method

1. **Confirm the public authority and locate the PIO.** Every public authority must designate a PIO/CPIO and a First Appellate Authority under s.5 and publish them under s.4(1)(b). Address the application to "The Public Information Officer, [authority]" — never invent an officer's name. If the records sit with another authority, the PIO must transfer the application within five days under s.6(3), so a reasonable guess at the right department is not fatal, but a wrong *authority* (e.g. a State matter sent to a Central ministry) wastes a cycle.

2. **Draft precise, numbered questions.** The Act gives a right to information that **exists and is held** (s.2(f), s.2(j)); a PIO need not create information, collate scattered data into a new document, give opinions, or explain why a decision was taken (*Aditya Bandopadhyay*, *Khanapuram Gandaiah*). So ask for documents and specific data points: "certified copy of the file noting on file no. X", "the date on which my application dated Y was received and the officer it was marked to", "the number of posts filled under advertisement no. Z, year-wise". Avoid "why", "all files", "complete details" — these invite a s.7(9) refusal for disproportionate diversion of resources or a "no such information" reply. Keep one application to one subject; split unrelated asks into separate applications (many PIOs and Commissions treat multi-subject applications as several).

3. **Anticipate the exemption.** For each question, name the s.8(1) ground a PIO is likely to cite — (a) sovereignty/security, (b) court-prohibited, (c) parliamentary privilege, (d) commercial confidence/trade secrets, (e) fiduciary relationship, (f) foreign government, (g) endangering life or safety / identifying informants, (h) impeding investigation or prosecution, (i) Cabinet papers, (j) personal information — and pre-empt it inside the application: invoke s.8(2) (public interest outweighs the harm), s.10 (sever and supply the rest), s.8(3) (events older than 20 years, except (a), (c), (i)), and s.4 (information that should have been proactively published). Do not pretend (a) or (g) material is obtainable; say when a request is a lost cause. For s.8(1)(j), apply the amended text if in force; otherwise *Girish Ramchandra Deshpande* (personal information of public servants is exempt unless the applicant shows larger public interest) and *Subhash Chandra Agarwal* (public interest balancing, including for judges' assets).

4. **Fee and mode.** Central: ₹10 by IPO, DD, banker's cheque or online on rtionline.gov.in; copies at ₹2 per page; BPL applicants pay nothing on proof. State: read the State RTI Rules. Information must be free if the PIO misses the deadline (s.7(6)). Flag any fee demand that goes beyond the rules (e.g. a "search fee" or per-question charge) as a ground of appeal.

5. **Compute the deadline table with the bundled script** and paste it into the output:
   ```bash
   python3 scripts/rti_deadlines.py --applied YYYY-MM-DD [--route direct|apio] [--third-party] [--life-liberty] [--reply YYYY-MM-DD] [--first-appeal YYYY-MM-DD] [--faa-decision YYYY-MM-DD] [--today YYYY-MM-DD]
   ```
   Rules: 30 days from receipt (s.7(1)); 48 hours for life or liberty; +5 days when routed through an Assistant PIO (s.5(2)); 40 days when third-party information is involved (s.11(3)); the period between a further-fee intimation and payment is excluded (s.7(3)); no reply in time = deemed refusal (s.7(2)); first appeal within 30 days of the decision or of the deadline expiring (s.19(1), condonable); FAA decides in 30 days, extendable to 45 with reasons (s.19(6)); second appeal within 90 days of the FAA decision or of when it was due (s.19(3), condonable). If the script is unavailable, compute by hand, show the steps and mark the result unverified.

6. **First appeal.** State the ground exactly: deemed refusal (no reply within time), incomplete or misleading reply, wrong exemption claimed (with the s.8(2)/s.10 answer), s.7(9) misused (the information is readily available in the form asked), fee demanded beyond the rules, transfer under s.6(3) not made, or information supplied without the certified copies/inspection requested. Attach the application, proof of fee and delivery, and the reply. Ask for the information free of cost under s.7(6) where the deadline was missed.

7. **Second appeal and complaint.** A second appeal under s.19(3) goes to the CIC (Central) or SIC (State) within 90 days; it is the route that can **direct disclosure**. A s.18 complaint is for a refusal to receive an application, no PIO appointed, unreasonable fee, or a general grievance — the Commission cannot order disclosure on a bare s.18 complaint (*CIC v. State of Manipur*), so file the second appeal, and add a s.20 prayer for the ₹250-per-day penalty (max ₹25,000) and disciplinary recommendation where the delay was without reasonable cause. Be honest about timelines: the CIC and most SICs carry backlogs measured in months to years; never promise a hearing date.

8. **Replies to objections.** Answer each stated ground with the section and the case that defeats it, keep the tone neutral, and restate precisely what is still outstanding. Where the objection is good (genuine s.8(1)(a)/(g)/(h) material, information that does not exist), say so and narrow the request instead of escalating.

## Output

```
# RTI — [Application | First appeal | Second appeal | Reply] — [authority]
## Summary (plain language: what we are asking, from whom, by when they must answer, what happens if they don't)
## Draft (rtionline headings: applicant details; public authority; particulars of information sought — numbered; period; form of information; fee details; BPL declaration if any; declaration that the applicant is a citizen of India; date and signature)
## Deadline table (output of rti_deadlines.py, with status as of today)
## Likely objections and the answer to each (section + case)
## If there is no reply: deemed refusal → first appeal, with the date it becomes available
## Attachments checklist (proof of fee, proof of delivery, prior correspondence, ID if demanded locally)
## Sources checked (section, source, date checked; cases by neutral citation)
```

For an appeal, add: grounds (numbered), relief sought (information free of cost under s.7(6); penalty under s.20; direction under s.19(8)).

## Guardrails

- Do not draft RTIs that fish for a private individual's address, phone, medical, financial or family details, or that target a private body — explain why it is outside the Act.
- Do not claim s.8(1)(a) or (g) material, or records that do not exist, can be obtained; narrow the request instead.
- Do not invent a PIO's or FAA's name, file numbers, or dates of receipt.
- Do not promise Commission hearing dates or outcomes; state the backlog reality.
- Keep each application to one subject and to questions a PIO can answer from existing records.
- Do not reproduce long statutory text; cite the section and summarise.

## References

- [references/case-law.md](references/case-law.md) — Supreme Court decisions by issue (what is a public authority, what counts as information, each exemption, fees, the s.18/s.19 distinction, penalties). Read it before the objections section.
- [scripts/rti_deadlines.py](scripts/rti_deadlines.py) — deadline calculator; `--json` for machine-readable output.
