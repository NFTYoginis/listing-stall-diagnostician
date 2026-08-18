# Listing Stall Diagnostician

You have a listing that hasn't sold, the seller conversation is this week, and everyone in the
room is about to assume the answer is price.

This tells you whether the evidence actually supports that — before the assumption becomes a
recommendation. It finds where the listing is losing buyers, names the one cause the evidence
supports, and stops. It does not tell you what to do about it.

Price is not always the constraint, and a reduction aimed at the wrong one costs the seller
money without producing a sale.

---

## Use it

1. Create a Claude Project.
2. Upload **`product/`**. That is the whole instruction — every file in it, nothing outside it.
3. Paste this into the project's custom instructions:

   > Follow `CLAUDE.md`. It routes.

Then say **"Diagnose this listing"** and answer what it asks. It will walk you through
collecting what it needs, one thing at a time, and tell you where each piece lives in your MLS
or showing platform.

Nothing to install, no API key, no dependencies.

> **Why the upload is a folder and not a list of exceptions.** `tests/`, `runs/` and `checks/`
> hold answer keys and completed diagnoses. A diagnostician that can read its own expected
> outputs is not being tested by them. The previous version of this README asked you politely
> to exclude `tests/`; a folder position is a fact and a README sentence is a request, so now
> they simply sit outside the thing you upload.

---

## What you need

Four things. Without all four you get an "I cannot tell" rather than a wrong answer.

1. **The listing** — description, all photos, property facts, current price
2. **Price and status history** — original price, every change with dates, current days on market
3. **Four or more comparables** — same submarket, overlapping band, same window, mixed sold and active
4. **At least one activity number** — views, saves, inquiries, or showings

The fourth is the one people skip and the one everything depends on. It's what locates *where*
the listing is failing. Without it every possible cause stays live and anything named is a guess.

**Sharpens it a lot:** showing feedback pasted verbatim rather than summarised, and the
second-showing count — how many of the people who came once came back. That number is usually
sitting unused in your showing platform, and if buyers are visiting and not writing, it is the
most diagnostic figure available.

---

## What you get back

A report with fixed headings. The diagnosis comes at three levels rather than one, because
flattening them produces a finding that sounds rigorous and cannot be acted on.

- **Constraint** — *where* the funnel breaks. One of five stages.
- **Cause** — *why* it breaks there. One entry from the taxonomy.
- **Mechanism** — *how* that cause produced this specific pattern in this listing.

Then the evidence for it, the alternatives it demoted and why, the confidence level, and what
would prove it wrong.

## The three answers people find surprising

**"Your listing is fine."** If it sits inside the comp range at every stage, there is no
listing-specific problem and the market slowed. This comes back more often than agents expect
and saves the most money, because a reduction against a segment-wide slowdown buys nothing
except a lower sale price. [Watch it happen](runs/003-null-under-pressure/transcript.md) on a
case where the agent explicitly asked for the case for a second reduction.

**"Your reduction already answered this."** A prior cut is a completed experiment, but it only
tested the mechanism it was capable of testing. A $5,000 trim on a $512,000 listing says
nothing about a $500,000 search threshold.

**"I cannot tell you from this."** If the funnel can't be reconstructed it names the missing
input and stops. That is the intended behaviour, not a bug —
[here is one](runs/005-undetermined-no-funnel/transcript.md), on a case with an obvious wrong
answer sitting in front of it.

---

## How it decides

Every listing moves buyers through five stages: **views, engagement, showings, second
showings, offers.** Find the earliest one where yours falls below the comparable baseline.
**That stage is the diagnosis site, and every stage after it is starved and therefore tells
you nothing.**

A listing getting a third of the normal views will also get few showings and no offers. Those
are consequences, not separate faults. Reading them as independent problems is how you end up
holding a list of nine issues and no idea which one is holding the sale.

Second showings are a stage rather than a metric because a first showing and a second showing
are different decisions made on different information. The first is a judgment about the
listing. The second is a judgment about the house. Most stalled listings that look healthy
break exactly there, and it is invisible unless you count it.

---

## Where this build actually stands

<!-- STATUS-CLAIM -->
v0.8 · 5 of 5 recorded runs pass all 10 gates in checks/verify.py · 11 open defects, listed in OPEN-DEFECTS.md · re-run against the folder that ships
<!-- /STATUS-CLAIM -->

That line is generated from [`status.json`](status.json) and mechanically checked against every
other surface that publishes it. It is not typed by hand anywhere.

- **[`runs/`](runs/)** — five recorded runs. Each has the transcript verbatim, the answer key
  that was committed *before* it, the scoring, and the verifier's output. `git log` shows the
  key preceding the transcript every time.
- **[`checks/verify.py`](checks/verify.py)** — the gates, standard library, no network.
  `--selftest` runs a planted-bad fixture per gate plus one clean control, and refuses to pass
  if any gate has no fixture. The gate count lives in the claim above, not in this sentence.
- **[`OPEN-DEFECTS.md`](OPEN-DEFECTS.md)** — everything known to be wrong, each naming the
  layer it has to close at. A defect does not close because the sentence about it improved.
- **[`JUDGE_GUIDE.md`](JUDGE_GUIDE.md)** — how to attack this build, in order, with the claims
  paired to what would break them.

Sixty seconds, no install:

```bash
git clone https://github.com/NFTYoginis/listing-stall-diagnostician
cd listing-stall-diagnostician
python3 checks/verify.py --selftest && python3 checks/verify.py
```

---

## Files

```
product/            ← this is what you upload
├── CLAUDE.md         routes; holds no method
├── intake.md         the door: symptom to evidence, one step at a time
├── identity.md       who it is and what it refuses
├── rules.md          the method, Steps 0–6, and the output contract
├── examples.md       three worked cases, one of them a null
└── reference/        taxonomy, baselines, evidence requirements, disguised asks

tests/              answer keys and planted-bad fixtures. Never uploaded.
runs/               five recorded runs, four files each. Never uploaded.
checks/verify.py    the gates. Never uploaded.
BRIEF.md            the questions this is judged on
JUDGE_GUIDE.md      how to break it
OPEN-DEFECTS.md     what is known to be wrong
status.json         the only place a status claim is authored
```

---

## Scope and honesty

The examples and test cases are constructed for teaching, with figures chosen to make each
discriminator legible. They are not client files and their numbers are not benchmarks. There
has been no retrospective field validation.

There are deliberately no industry-average figures anywhere in `product/`. Showing rates, view
counts and normal time on market vary by market, band, season and portal, and any number
quoted as a national average would be wrong in most places while being treated as
authoritative. Every baseline is computed from your own comparison set.

This diagnoses listing performance. It is not an appraisal, a CMA, or a valuation, and it does
not model your local market beyond the comps you supply.

MIT licensed. Built by Gabe — Your AI Specialist.
