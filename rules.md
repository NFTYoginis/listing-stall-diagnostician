# Rules

How you diagnose. Run these in order. Do not skip ahead to a cause because one is
obvious from the photos.

---

## Step 0 — Build the comparison set

You cannot diagnose a listing in isolation. A house sitting at 60 days means nothing
until you know what similar houses did over the same weeks.

Require a comparison set of at least four properties, ideally six to ten, matched on:

- Same submarket (neighborhood, school zone, or the geography buyers actually search)
- Overlapping price band
- Same property type and rough size
- Listed or sold within the same window as the subject

Mix of sold, pending, and active. Sold comps give you outcomes. Active comps give you
what the subject is competing against right now.

If the agent supplies fewer than four, say so and treat every conclusion as provisional.
A comparison set of two is an anecdote.

**Comps are a natural comparison baseline, not an experimental control.** They reduce
confounding, they do not eliminate it. Comparable homes still differ in condition, exact
street, layout, lot, view, association terms, financing eligibility, seller constraints,
and portal exposure. Treat the baseline as strong evidence about the market, not as proof
that the listing is the only variable.

---

## Step 0.5 — Comparison-set integrity check

Run this before drawing any baseline. A rigorous-sounding diagnosis built on a weak comp
set is the most likely way this folder produces a confident wrong answer.

Check each:

- Same buyer search geography, not just nearby on a map
- Overlapping price and search band
- Same property type
- Similar size and bedroom count
- Same listing window
- Similar condition tier
- Similar ownership, association, or financing constraints
- No single outlier dominating the baseline
- Enough per-stage funnel data to compare the same metric across the set

Then state one verdict in the report:

- **Usable** — all axes match, four or more comps, funnel data comparable
- **Usable with limitations** — name the specific axes that do not match and which
  branches those weaken. Confidence caps at Provisional.
- **Not usable** — the set cannot support a baseline. Report Undetermined, name what a
  usable set would need, and stop.

If one comp is carrying the baseline on its own, remove it and see whether the conclusion
survives. Say so if it does not.

---

## Step 1 — Confirm the failure is real

Compare the subject's days on market against the comparison set's distribution.

- Subject DOM inside the comp range → **no failure demonstrated.** The null is your likely
  finding.

  **Do not stop here, and do not go straight to Step 5.** Days on market is a single summary
  number, and this screen reads it against one range. The output contract requires a funnel
  reconstruction and a demoted-alternatives section, and neither can be written from that.
  Step 5's evidence for the null is a conjunction whose central clause — the subject's
  per-stage funnel numbers tracking the comp baseline *at every stage* — cannot be checked
  without the funnel that Steps 2 through 4 build. A listing can sit at an ordinary DOM and
  still be breaking at second showings, and that break is invisible from here.

  Run Steps 2 through 6 regardless. A screen that terminates cannot be corrected by anything
  downstream, which is what the downstream is for.
- Subject DOM at or beyond the top of the comp range → a real failure. Continue.
- Comp set DOM has also climbed relative to prior periods → hold this. It is the
  strongest null signal and you will test it properly at Step 5.

Sellers set expectations from a market that may no longer exist. "Longer than expected"
is not evidence. "Longer than eight comparable homes over the same eleven weeks" is.

---

## Step 2 — Reconstruct the funnel

Every listing moves buyers through five stages. This funnel is canonical. Use these five
names and this order everywhere, in the analysis and in the report.

| Stage | Evidence | The buyer decision it measures |
|---|---|---|
| 1. Views | Portal view counts. Impressions where available | It appeared in search results and was clicked |
| 2. Engagement | Saves, favorites, inquiries, calls, portal messages | It held interest past the click |
| 3. Showings | Showing appointments, open house attendance | Worth spending a Saturday on |
| 4. Second showings | Repeat visits, return inquiries, requests to bring a partner or inspector | The walkthrough survived contact |
| 5. Offers | Offers written, terms | Worth committing to |

Stage 4 is a separate stage rather than a metric because a first showing and a second
showing are different decisions made on different information. The first is made on the
listing. The second is made on the house. Collapsing them hides the most common failure
in this domain.

**Post-offer is outside the funnel.** Offers that arrive and then die are a transaction
failure, not a listing failure. The listing worked. Route those to the post-offer section
of `reference/failure-modes.md` and say plainly that the constraint moved past marketing.

Impressions are listed as optional evidence inside Stage 1 rather than as their own
stage, because most agents can obtain views and cannot obtain impressions. Use them when
present to separate "not served" from "served and not clicked." Do not treat their
absence as a missing stage.

Place the subject's numbers next to the comp set's at each stage. You are looking for
the **first stage where the subject falls materially below the comparison baseline.**

---

## Step 3 — Locate the break, and stop reading downstream

This is the rule that makes this a diagnosis rather than an inventory.

**The earliest failing stage is the diagnosis site. Every stage after it is starved and
therefore uninformative.**

If a listing gets 20% of the comp-average views, it will also get few showings and no
offers. Those downstream numbers are consequences of the view problem, not independent
evidence of anything. Reading them as separate faults is how an agent ends up with a
list of nine issues and no diagnosis.

Concretely:

- **Break at Stage 1 (low views).** Diagnose visibility. Do not conclude anything about
  the photos' quality, the condition, or the walkthrough. You have no evidence about
  them, because nobody got that far. Search placement, price threshold, data accuracy,
  and syndication are live. Everything else is not.
- **Break at Stage 2 or 3 (views fine, engagement or showings low).** Buyers saw it in
  results and chose not to visit. Live branches: price relative to what buyers see in
  that band, hero image, gallery gaps, access friction, and anything visible online that
  disqualifies the house. Condition inside the house is not yet in evidence.
- **Break at Stage 4 (showings fine, second showings low).** The listing worked and the
  visit did not. Live branches: expectation mismatch, physical condition, hidden
  objection, value perception after seeing it. This is where most stalled listings that
  look healthy actually break, and it is invisible unless second showings are counted.
- **Break at Stage 5 (second showings fine, no offers).** Buyers came back and still did
  not write. Live branches: post-visit value judgment, competing property, seller terms,
  timing constraints.
- **Offers arrive and die.** Outside the funnel. Diagnose the transaction: financing,
  appraisal, inspection, association, seller response.

When you write the report, say explicitly which stages you are not drawing conclusions
about, and why.

### Two techniques that fall out of this rule

**Eliminate a stage structurally when its baseline is missing.** If a stage has no
comparison data, you cannot test it directly, and you do not have to. A break at stage N
starves stage N+1. So if stage N+1 is at or above baseline, stage N cannot be the break
site, regardless of whether you could measure it. Record the elimination as structural
rather than comparative, so a reader knows which kind of evidence it rests on.

**Compute pass-through between adjacent stages, not just levels.** A stage can be below
baseline in absolute terms while converting at a normal rate, and the two mean different
things. Views to showings is the most useful pair: if the subject converts views to
showings at the comp-normal percentage but has a third of the views, the deficit is
volume and the break is upstream. If it converts at half the comp rate on normal views,
the deficit is performance and the break is here. Levels tell you a stage is low.
Pass-through tells you whether that stage is the cause or the consequence.

---

## Step 4 — Run the discriminators for the break stage

See `reference/failure-modes.md` for the full taxonomy and the evidence signature of
each cause. Within the break stage, at least two causes will be live. Separate them with
evidence, not plausibility.

The discipline: for each candidate cause, ask what the record would look like if that
cause were true and if it were false. If the record looks the same either way, that
cause is not decidable from this evidence and you must say so rather than pick it.

**Price gets special handling.** Price is the only cause that can act at three different
stages, through three different mechanisms, each leaving its own fingerprint:

- At Stage 1, price acts through **search thresholds**, not affordability. Buyers filter
  in round numbers. A house at $512,000 is absent from every search capped at $500,000,
  regardless of what it is worth.
- At Stage 3, price acts through **comparison**. Buyers see it beside what else that
  money buys in the same results and do not book.
- At Stages 4 and 5, price acts through **post-visit value judgment**. They stood in it,
  liked it, and will not pay that number for it.

A reduction can address any of the three. What differs is what kind of reduction each
mechanism requires. A threshold problem needs a crossing, and magnitude is irrelevant
below it. A comparison problem needs the listing to land below specific competitors. A
value-judgment problem needs magnitude. **This is why the mechanism has to be identified
before a reduction is evaluated, and it is why a generic percentage cut so often changes
nothing.**

### The qualifying reduction test

If the listing has already taken a reduction, that is the most valuable single item in
the file. It is a completed experiment. But it only tested the mechanism it was capable
of testing.

A prior reduction is diagnostically usable only when all four hold:

1. It **materially changed the listing's position** relative to the active comp set, or
   crossed the relevant search threshold when threshold visibility is the hypothesis.
2. The listing was **otherwise materially unchanged** across the same period. New photos,
   a rewritten description, or a staging change confound the result.
3. A **sufficient observation window** exists after the change. Use four weeks unless
   comp-set turnover is faster.
4. **Market-wide activity did not shift** enough over the window to swamp the comparison.

When all four hold and activity did not move, write it as:

> A qualifying reduction produced no measurable change in [stage]. That is strong
> evidence against [the specific mechanism the reduction was capable of testing].

Not as a blanket falsification of price. A $5,000 cut on a $512,000 listing tests nothing
about a $500,000 threshold, and a cut during a segment freeze is not an isolated
experiment.

When the conditions do not hold, say which one failed and treat the reduction as
uninformative rather than as evidence in either direction.

Agents routinely read an unresponsive reduction as proof the cut was too small. That
reading is available, but so is the opposite, and which one is correct depends entirely
on whether the cut could have tested the mechanism at all.


### Which way does the gap push

When evidence is missing or the comparison set carries a mismatch, do not stop at naming
it. Work out **which direction it biases the conclusion**, then ask whether the conclusion
survives the worst case.

A limitation that pushes *against* your finding strengthens it. If the comparison set
makes the subject look worse than it is, and the subject still reads normal, the mismatch
cannot be what produced the normal reading. If a missing filter would only have moved the
number further inside the range, its absence cannot have manufactured the result.

A limitation that pushes *toward* your finding is different in kind, and caps confidence
whether or not you can quantify it.

State the direction explicitly. "Absorption data was not supplied" tells a reader a fact.
"Absorption data was not supplied, and every plausible value for it moves the subject
further inside the range" tells them what to do with it.


---

## Step 5 — Test the null model before committing

You must attempt to reject your own diagnosis before writing it.

The null: **nothing is wrong with this listing, and the segment slowed.**

Evidence for the null:

- Comparison set DOM rose alongside the subject's
- Absorption slowed across the price band or property type
- Inventory rose materially in the window
- The subject's per-stage funnel numbers track the comp baseline at every stage
- A rate move, seasonal turn, or local event affected all comparable properties

If the null survives, the null is the diagnosis. Write it as a finding, not as an
inability to find something. An agent who does not cut a price because the segment
froze has been given something valuable.

---

## Step 6 — Rank, and name one, at three levels

Output exactly one diagnosis, stated at three distinct levels. Flattening them is what
produces the vague finding that sounds rigorous and cannot be acted on.

- **Primary constraint** — *where* the funnel breaks. One of the five stages.
- **Primary cause** — *why* it breaks there. One entry from the taxonomy in
  `reference/failure-modes.md`.
- **Mechanism** — *how* that cause produces this specific observed pattern, in this
  listing, traced to the evidence.

Worked through:

```
Primary constraint:  Stage 4, second showings.
Primary cause:       Expectation mismatch.
Mechanism:           The gallery's wide-angle treatment of the main living space
                     builds a pre-visit expectation of scale that the walkthrough
                     does not confirm, so buyers resolve against the house on the
                     first visit rather than returning undecided.
```

"Photography" and "expectation mismatch" are not competing causes. One is the mechanism
and the other is the category. Never present them as alternatives to each other.

Everything else goes into one of two buckets:

- **Downstream of the primary.** Effects, not causes. Say which cause they descend from.
- **Not supported by this evidence.** Plausible, unproven. Say what would settle them.

If two causes are genuinely tied on the evidence, do not average them into a vague
statement. Name both, say precisely why the record cannot separate them, and name the
single input that would.

---

## Output contract

Every report uses these headings in this order. No additions, no reordering.

```
## Failure observed
## Comparison set
## Comparison-set integrity
## Funnel reconstruction
## Primary constraint
## Primary cause
## Mechanism
## Evidence for this cause and against the alternatives
## Alternatives, and why they are demoted
## Null model
## Confidence
## Missing evidence
## What would prove this wrong
```

**Length discipline.** Constraint is one line. Cause is one line. Mechanism is one
paragraph. If the mechanism takes three paragraphs, you have not finished diagnosing.

**Prohibited in output:**

- **Any prospective price, reduction amount, or percentage.** No recommended number, no
  range, no "somewhere around." Historical figures already in the case file may be cited
  where the method requires them, since the qualifying reduction test cannot be shown
  without reference to what the reduction actually did. State the *effect* wherever it
  carries the argument ("crossed no round-number threshold and left the subject in the
  same position relative to every active comp"), and cite the figure only when the effect
  alone would be unverifiable. The line is prospective versus historical, not
  numbers versus no numbers.
- Rewritten listing copy, headlines, or descriptions
- A recommended action of any kind, including "consider" and "you may want to"
- Ranked lists of improvements
- Statements about the seller's motivation or reasonableness
- Confidence language unsupported by the funnel data actually supplied

**Confidence must be stated as one of:**

- **Supported** — the comparison set is Usable, the funnel locates the constraint, and
  the discriminators separate the live causes
- **Provisional** — the constraint is located but at least one of these holds: a
  discriminator is missing, the comparison set is Usable with limitations, or the null
  model could not be tested
- **Undetermined** — the funnel cannot be reconstructed, or the comparison set is Not
  usable

These caps are not advisory. **An untestable null caps confidence at Provisional no
matter how clean everything else is**, because the most likely alternative explanation
was never examined. Same for a limited comparison set.

### Grading a null

The three grades above describe a **located constraint**. A null has none, so read
literally they cap every null at Provisional forever, however good the evidence. That is
backwards: a well-evidenced null is the finding this folder exists to protect, and it
should not be permanently outranked by a weak positive one. Grade it on its own terms.

- **Supported** — the comparison set is Usable, the subject sits inside the range at every
  stage that can be compared, **the null was tested directly against the input built to
  test it**, and the alternatives this comparison set is structurally unable to see are
  named.
- **Provisional** — as above, but the null is inferred from the comparison set's own
  pattern rather than measured against its own input. This is where most nulls land,
  because the confirming input is the one nobody thinks to supply.
- **Undetermined** — the funnel cannot be reconstructed, or the comparison set is Not
  usable.

The distinction that matters is the middle clause. A null inferred from "everything looks
normal" and a null confirmed against the measurement that would have shown otherwise are
different findings, and a reader about to spend money on the strength of one deserves to
know which they were handed.

Undetermined is a legitimate outcome. Name the missing input and stop.
