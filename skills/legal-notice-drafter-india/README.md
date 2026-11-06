# Legal Notice Drafter (India)

Drafts and audits legal notices and replies the way an Indian practitioner does: classifies the notice (statutory-mandatory, statutory-optional or tactical), checks who may sign, sets out dated and documented facts, states the breach with its basis, makes a quantified demand with a deadline and a lawful consequence, plans service, and tells you what happens next — including whether limitation keeps running. Covers s.80 CPC, s.106 TPA, s.21 Arbitration Act, s.12A Commercial Courts Act, MSMED Samadhaan, IBC s.8, SARFAESI s.13(2) and employment notices.

For advocates, in-house teams and litigants sending a first notice themselves.

## Install

```bash
claude plugin install legal-notice-drafter-india@awesome-indian-legal-skills
```

Or copy this folder into your agent's skills directory.

## What it needs from you

- Sender, recipient, their legal status and addresses
- The relationship and the documents (contract, invoice, lease, loan, employment letter)
- The breach: what, when, how much — with dates and documents
- The demand and the deadline you want
- Whether the recipient is the Government, a tenant, an arbitration counterparty, a commercial-dispute defendant, a corporate debtor, a borrower or an employee (these trigger statutory rules)

## What you get

- Classification and a requirements checklist for the statute (period, contents, addressee, mode)
- Limitation position and whether the notice period is excluded
- Draft notice or para-wise reply with letterhead block, facts, breach, demand, deadline, consequence, reservation of rights, enclosures
- Service plan with what to keep as proof
- Timeline from dispatch, and a defects list

## Example prompts

- "Our vendor hasn't paid ₹18 lakh on three invoices from June. We're MSME registered. Draft the notice and tell me whether to go to Samadhaan or court."
- "Need a notice to quit for a month-to-month tenant in Pune who hasn't paid rent for four months."
- "We want to sue the municipal corporation for damages after they dug up our shop frontage. What notice do we need?"
- "Got a legal notice from a former client's lawyer alleging deficient service and threatening an FIR. Draft a reply."

## Law covered

- CPC s.80 · TPA s.106 · Arbitration and Conciliation Act ss.11, 21 · Commercial Courts Act s.12A · MSMED Act ss.15–19 · IBC ss.8–9 · SARFAESI ss.13, 17 · ID Act s.25F / Industrial Relations Code, 2020 · Limitation Act s.15(2) · General Clauses Act s.27 · BNS ss.308, 351, 356
- *Bihari Chowdhary*, *Geeta Iron & Brass Works*, *Patil Automation*, *Yamini Manohar*, *Mobilox*, *Mardia Chemicals*, *BSNL v. Nortel*, *Arif Azim*, *Silpi Industries*, *Mahakali Foods* — see [references/statutory-notices.md](references/statutory-notices.md)

## Limits

- Cheque-bounce notices go to [cheque-bounce-s138-advisor](../cheque-bounce-s138-advisor/).
- State Rent Control and Shops & Establishments Acts vary; the skill tells you to check the State Act.
- Does not send or serve anything; does not compute court fees.

## Author and licence

Rahul Beniwal · MIT (see LICENSE.txt). Not legal advice — a qualified advocate must review every notice before it is sent.
