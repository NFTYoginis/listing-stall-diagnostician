# Listing Stall Diagnostician

**v0.6** · Status: built, and exercised by three independent blind runs on constructed cases. Retrospective field
validation pending.

A folder you drop into a Claude Project. Claude becomes a diagnostician that works out
why a specific listing has not sold.

It is built for one moment: you have a property past its expected time on market, the
seller conversation is coming, and everyone in the room is about to assume the answer is
price. Before that assumption becomes a recommendation, this tells you whether the
evidence actually supports it.

Price is not always the constraint, and a reduction aimed at the wrong one costs the
seller money without producing a sale. Locating where the listing actually breaks is what
tells you whether you are about to apply the right intervention to the wrong problem.

---

## What it does

Reconstructs the buyer funnel for your listing, compares it against your comparable
properties over the same weeks, finds the earliest stage where your listing falls below
that baseline, and names the one cause the evidence supports.

Then it tells you what would prove it wrong.

## What it does not do

- Recommend a price, a reduction, or a percentage
- Rewrite your description or suggest headlines
- Value the property
- Hand you a list of nine things to improve
- Tell you what to do next

It stops at the cause. What you do about it is your call with your seller, and it is a
different conversation with different inputs.

---

## Setup

1. Create a Claude Project.
2. Upload the contents of this folder to the project knowledge.
3. Paste this into the project's custom instructions:

   > Follow identity.md and rules.md exactly. Run the diagnostic sequence in rules.md in
   > order and use the output contract at the end of that file. Consult reference/ as
   > needed. Do not recommend actions.

That is the whole install. No dependencies, no API keys, nothing to run.

---

## Running a case

Upload the case materials and say: **"Diagnose this listing."**

### What you need

Four things. Without all four you will get an Undetermined result rather than a wrong one.

1. **The listing** — description, all photos, property facts, current price
2. **Price and status history** — original price, every change with dates, current DOM
3. **Four or more comparables** — same submarket, overlapping band, same window, mixed
   sold and active
4. **At least one funnel number** — views, saves, inquiries, or showings

That fourth item is the one most often skipped and the one the method depends on
entirely. It is what locates where the listing is failing. Without it, every possible
cause stays live and anything the diagnostician names is a guess.

### What sharpens it considerably

- **Showing feedback, verbatim.** Paste the actual notes. Do not summarize them. The
  pattern across notes is the evidence and summarizing destroys it.
- **Second showing count.** The single most diagnostic number available if buyers are
  visiting and not writing. It is already sitting in your showing platform.
- **Views broken out by portal.**
- **Neighborhood DOM trend** across the same window, which is what the null model runs
  on.

Full intake list in [reference/intake.md](reference/intake.md).

---

## What you get back

A report with fixed headings, in this order:

Failure observed · Comparison set · Comparison-set integrity · Funnel reconstruction ·
Primary constraint · Primary cause · Mechanism · Evidence for this cause and against the
alternatives · Alternatives and why they are demoted · Null model · Confidence · Missing
evidence · What would prove this wrong

The diagnosis comes at three levels rather than one, because flattening them produces a
finding that sounds rigorous and cannot be acted on. **Constraint** is where the funnel
breaks. **Cause** is why it breaks there. **Mechanism** is how that cause produces this
specific pattern in this listing.

Three worked examples in [examples.md](examples.md), including one that finds nothing
wrong.

---

## The three answers people find surprising

**"Your listing is fine."** If your property sits inside the comp range at every funnel
stage, there is no listing-specific problem and the market slowed. This comes back more
often than agents expect, and it is the finding that saves the most money, because a
reduction against a segment-wide slowdown buys nothing except a lower sale price.

**"Your reduction already answered this."** A prior cut is a completed experiment, but it
only tested the mechanism it was capable of testing. A $5,000 trim on a $512,000 listing
says nothing about a $500,000 search threshold. When a cut *did* qualify and activity
still did not move, that is strong evidence against price at that mechanism, and the
usual reading that the cut was simply too small is the weaker of the two available.

**"I cannot tell you from this."** If the funnel cannot be reconstructed, it names the
missing input and stops rather than producing a confident cause built on nothing. That is
the intended behavior, not a bug.

---

## How it decides

The method turns on one rule.

Every listing moves buyers through five stages: **views, engagement, showings, second
showings, offers.** Find the earliest one where yours falls below the comparable baseline.
**That stage is the diagnosis site, and every stage after it is starved and therefore
tells you nothing.**

Second showings are a stage rather than a metric because a first showing and a second
showing are different decisions made on different information. The first is a judgment
about the listing. The second is a judgment about the house. Most stalled listings that
look healthy break exactly there, and it is invisible unless you count it.

A listing getting a third of the normal views will also get few showings and no offers.
Those are consequences, not separate faults. Reading them as independent problems is how
you end up holding a list of nine issues and no idea which one is holding the sale.

The rest of the method is separating the causes that are live at that one stage, using
evidence rather than plausibility, and then trying to reject the whole thing with the
null before committing to it.

Full method in [rules.md](rules.md). Cause taxonomy with evidence signatures in
[reference/failure-modes.md](reference/failure-modes.md).

---

## Files

```
listing-stall-diagnostician/
├── README.md                      this file
├── identity.md                    who it is, what it diagnoses, what it refuses
├── rules.md                       the method and the output contract
├── examples.md                    three worked cases, one of them a null
└── reference/
    ├── failure-modes.md           causes by funnel stage, with evidence signatures
    ├── baselines.md               building the comparison set and reading it
    └── intake.md                  required inputs and missing-evidence handling
```

---

## Scope and honesty

The examples are constructed teaching cases with figures chosen to make each
discriminator legible. They are not client files and the numbers in them are not market
benchmarks.

There are deliberately no industry-average figures anywhere in this folder. Showing
rates, view counts, and normal time on market vary by market, band, season, and portal,
and any number quoted as a national average would be wrong in most places while being
treated as authoritative. Every baseline is computed from your own comparison set.

This diagnoses listing performance. It is not an appraisal, a CMA, or a valuation, and it
does not model your local market beyond the comps you supply.
