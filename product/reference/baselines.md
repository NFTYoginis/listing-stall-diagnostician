# Baselines

The comparison set is what turns an opinion into a diagnosis. This file covers how to
build it and how to decide what counts as underperformance.

There are no national benchmark numbers here on purpose. Showing rates, view counts, and
normal days on market vary enormously by market, price band, season, and portal. Any
figure quoted as an industry average would be wrong in most markets and would be treated
as authoritative anyway. **Every baseline in a diagnosis is computed from that case's own
comparison set.**

---

## Building the comparison set

Match on the axes buyers actually use when they search:

- **Geography** — the area buyers search, which is often a school zone or a named
  neighborhood rather than a radius or a zip code.
- **Price band** — overlapping, not identical. A house competes with everything a buyer
  sees inside their filter range.
- **Property type and size** — same type, similar bed and bath count, square footage
  within a range that would appear in the same search.
- **Window** — listed or sold inside the subject's active period. A comp that sold eight
  months ago describes a different market.

Four is the floor. Six to ten is a usable set. Below four, state that the range is not
established and cap confidence at Provisional.

**Include actives, not just solds.** Sold comps tell you what the market cleared. Active
comps tell you what this listing is competing against on a buyer's screen right now, and
that is what determines whether it gets a click and a showing.

---

## Establishing the DOM range

Take days on market for every comp. You need the spread, not the average.

The subject is underperforming when its DOM sits **at or beyond the top of the comp
range**, not when it exceeds the mean. Half of all listings exceed the mean by
definition, and treating the mean as a target manufactures failures that do not exist.

Then check whether the range itself moved. If comps listed early in the window sold in
two weeks and comps listed late are still sitting, the market changed mid-listing and
the null model is live before you look at anything else.

---

## Per-stage baselines

Compute the comp set's figures for each of the five canonical stages and compare:
**Views, Engagement, Showings, Second showings, Offers.**

**Views.** Portal view counts across comps, normalized for time on market, since a
listing live for 60 days accumulates more views than one live for 14. Compare views per
week, not views total. This normalization is the most common error in agent-run
comparisons.

**Inquiries and saves.** Absolute counts are noisy. The useful figure is the ratio to
views, which tells you whether the listing converts attention into interest.

**Showings.** Showings per week against the comp set. Also compute showings as a
proportion of views, which separates "nobody saw it" from "people saw it and passed."

**Second showings.** As a proportion of first showings. This is its own funnel stage, not
a supporting metric, because a first showing and a second showing are different decisions
made on different information. The first is a judgment about the listing. The second is a
judgment about the house. The figure is frequently sitting unused in the showing platform.

**Offers.** Count and timing relative to second-showing volume.

---

## What comps are, and are not

The comparison set is a natural comparison baseline. It is not an experimental control.

Matching on geography, band, type, size, and window removes a great deal of confounding,
which is why the method works at all. It does not hold everything constant. Comparable
homes still differ in condition, exact street, layout, lot, view, school assignment,
association terms, financing eligibility, seller constraints, and portal exposure.

Write conclusions accordingly. "The subject falls below its comparison baseline at Stage
3" is supportable. "The only variable is the listing" is not, and it is the phrasing that
turns a good baseline into a false proof.

---

## What counts as "materially below"

Judgment, stated explicitly in the report rather than applied silently.

- **Clearly below** — subject is under the lowest comp in the set on that stage. Treat
  as a located break.
- **Ambiguous** — subject sits inside the comp range but in the bottom quarter. Note it,
  do not treat it as the break unless a later stage is clearly below.
- **At baseline** — subject sits inside the comp range. This stage is not the break.
  Move to the next stage.

If no stage is clearly below, the funnel is performing at market and the null is likely
the answer. Do not manufacture a break by lowering the bar until one appears.

---

## The qualifying reduction test

The single most useful piece of history in any case file, and the easiest one to
over-read.

A prior reduction is a completed experiment. But an experiment only tests what it was
capable of testing, and most reductions are not capable of testing most price mechanisms.

### Step 1: does the reduction qualify

All four must hold before the result means anything.

| Condition | Why it matters | Fails when |
|---|---|---|
| **Material position change** | The cut must have moved the listing relative to the active comp set, or crossed the search threshold if threshold visibility is the hypothesis | A 1% trim that leaves it in the same competitive position and the same filter band |
| **Otherwise unchanged** | Simultaneous changes confound the result | New photos, rewritten copy, staging, or a status reset landed in the same window |
| **Sufficient window** | Buyer response is not instant | Fewer than four weeks after the change, or less than the comp set's typical time-to-showing |
| **Stable market** | The comparison must survive | A rate move, seasonal turn, or inventory shift hit the whole band over the same weeks |

If any condition fails, the reduction is **uninformative**. Say which condition failed
and do not use the reduction as evidence in either direction. An uninformative experiment
is not weak evidence for the null. It is no evidence.

### Step 2: read a qualifying reduction

Compare activity for the two weeks before against the four weeks after, stage by stage.

- **Activity rose at a stage** — price was a real constraint at that stage. Which stage
  responded identifies the mechanism, and that is more valuable than the fact of the
  response.
- **Views rose, showings did not** — the reduction crossed a search threshold and solved
  a visibility problem, exposing a second constraint underneath it. Two findings, not one.
- **Nothing moved** — strong evidence against **the specific mechanism this reduction was
  capable of testing.** Name that mechanism explicitly. A $12,000 cut that stayed above
  $500,000 says nothing about threshold exclusion, and a cut that left the listing above
  four superior comps says nothing about comparative value.

The last one is where the discipline lives. Agents read an unresponsive cut as proof the
cut was too small. That reading is available. So is the opposite. Which one is correct
depends entirely on whether the cut could have tested the mechanism at all, and that is a
question about the number, not about the market's mood.

---

## Seasonality and rate moves

Before attributing a slowdown to the listing, check whether the window contains a
seasonal turn or a rate move that affected the whole band. If the comparison set is
matched on window, this is already controlled for, which is why the window match matters
more than most agents assume.

A subject listed in a strong month and compared against comps listed in a weak month
will look artificially bad, and vice versa. When windows cannot be matched, say so and
treat the comparison as weakened.
