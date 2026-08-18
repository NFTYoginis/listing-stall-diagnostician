# Fixture — 01 — section out of order

Synthetic. Built by `tests/negative/build-fixtures.py` for `checks/verify.py --selftest`.
Not a run. Nothing in `runs/` was produced this way.

**Planted defect:** Confidence is reported before the null model, so the contract's order is broken while every required heading is still present.

## Metadata

- source case: `tests/case-02-expectation-mismatch/inputs.md`
- gate that must reject it: `FORMAT`

## Turn 1 — user

# Case 02 — inputs

Constructed case. Paste everything below into a project running the diagnostician, then
say "Diagnose this listing."

---

## Subject listing

- 4 bed / 2 bath single family, 1,980 sq ft
- Listed at $479,000. **Reduced to $465,000 on day 29.** No other changes since listing:
  same gallery, same description, no staging change, no status reset.
- **58 days on market**
- Gallery: 31 images. Three images of the main living space, all shot from the room's
  corner at wide angle with seating pushed against the walls. No floor plan.

**Description opening:** "Expansive open-concept living in Ridgeway. A dramatic great
room anchors the main floor, flowing into a chef's kitchen. Generous throughout."

## Funnel data, subject

| Stage | Figure |
|---|---|
| Views | 312 per week |
| Engagement | 19 saves per week, 6 inquiries |
| Showings | 4.1 per week, 34 first showings total |
| Second showings | 1 of 34 |
| Offers | 0 |

Activity in the four weeks after the day-29 reduction: views 318/wk, showings 4.3/wk,
second showings 1 across the period. The $14,000 cut moved the subject below three active
comps it had previously been priced above.

## Comparison set

Same school zone, overlapping band, all listed within the subject's twelve-week window.

| # | Price | Sq ft | DOM | Views/wk | Showings/wk | 2nd showings | Status |
|---|---|---|---|---|---|---|---|
| 1 | $455,000 | 1,910 | 11 | 380 | 5.0 | 9 per 30 | Sold |
| 2 | $469,000 | 2,040 | 24 | 290 | 3.8 | 7 per 30 | Sold |
| 3 | $448,000 | 1,875 | 19 | 310 | 4.2 | 8 per 30 | Sold |
| 4 | $472,000 | 2,010 | 41 | 240 | 2.8 | 6 per 30 | Sold |
| 5 | $461,000 | 1,955 | 14 | 355 | 4.6 | 11 per 30 | Sold |
| 6 | $483,000 | 2,100 | 22 | 275 | 3.5 | 7 per 30 | Pending |
| 7 | $458,000 | 1,930 | 19 | 300 | 4.0 | 8 per 30 | Active |
| 8 | $475,000 | 2,065 | 31 | 260 | 3.3 | 6 per 30 | Active |

Comp 5 was renovated within the last eighteen months. The other seven are comparable in
condition tier.

Comps 3, 5 and 7 were listed in the back half of the window and reached 19, 14 and 19 days
respectively.

## Market context

Zone median DOM steady across the window. Inventory flat. No rate move.

## Showing feedback, verbatim

1. "Buyers liked the yard but said the living room felt much smaller than the pictures."
2. "Photos oversell the great room. Not what they pictured walking in."
3. "Nice house. The main room was a surprise, they expected something much bigger."
4. "Kitchen is lovely. They commented the living space photographed larger than it is."
5. "Passing. Said the layout felt tight compared to the listing."
6. "Good condition throughout. Buyers felt misled on the size of the main floor."
7. "They liked it but are looking for more room for the price."
8. "Well maintained. Moving on."
9. "Buyers thought it was priced fair for the area but the great room wasn't what the
   photos showed."

## Turn 2 — assistant

## Failure observed

Listing active 58 days. The comparison set ranges 11 to 41 days on market, and six of
the eight are closed or pending. The subject sits beyond the top of that range.
Failure confirmed.

## Comparison set

Eight properties in the same school zone, overlapping band, all listed inside the
subject's twelve-week window. Five sold, one pending, two active.

## Comparison-set integrity

**Usable.** Geography, band, type, size and window match across the set. Condition
tier is comparable across seven of the eight; comp 5 was renovated inside the last
eighteen months. Removing comp 5 leaves the days-on-market range and the
second-showing baseline materially unchanged, so no single comp is carrying the
baseline.

## Funnel reconstruction

| Stage | Subject | Comp range | Read |
|---|---|---|---|
| 1. Views | 312 per week | 240 to 380 per week | At baseline |
| 2. Engagement | 19 saves per week, 6 inquiries | not supplied for the comps | Not comparable |
| 3. Showings | 4.1 per week | 2.8 to 5.0 per week | At baseline |
| 4. Second showings | 1 of 34 first showings | 6 to 11 per 30 first showings | Clearly below |
| 5. Offers | 0 | 0 to 2 | Below, starved |

## Primary constraint

**Stage 4, second showings.** The listing performed at or above baseline through the
showing appointment.

## Primary cause

**Expectation mismatch.**

## Mechanism

The gallery's three images of the main living space are all shot from a corner at
wide angle with the seating pushed to the walls, which reads as materially larger
than the stated square footage supports. Buyers arrive holding a pre-visit
expectation of scale that the walkthrough contradicts in the first minute, and they
resolve against the house on that visit rather than leaving undecided. A buyer who
leaves undecided books a second visit. These buyers are not undecided.

## Evidence for this cause and against the alternatives

The second-showing rate is the discriminating figure. Buyers who like a house and
intend to negotiate come back to it. A rate of 1 of 34 against a comp baseline of 6
to 11 per 30 means buyers are not leaving unresolved; they are leaving resolved.

The feedback clusters on surprise rather than on an attribute. Six of the nine notes
describe a gap between two impressions rather than a defect in the house: "Photos
oversell the great room. Not what they pictured walking in." and "Buyers felt misled
on the size of the main floor." A buyer objecting to a small room says the room is
small. These buyers are saying they expected something else, which locates the fault
in the representation rather than in the property.

## Alternatives, and why they are demoted

**Price, comparison mechanism at Stage 3.** Not supported. Showings run at 4.1 per
week against a comp range of 2.8 to 5.0, so buyers are not filtering the listing out
on price before booking.

**Price, post-visit value mechanism at Stage 5.** Weakened, and the prior reduction
is readable here. The day-29 cut was $14,000 on a $479,000 list, taking it to
$465,000 and moving the subject below three active comps it had previously been
priced above. The listing was otherwise unchanged across the same period, 29 days of
observation follow the change, and zone activity was flat. That is a qualifying
reduction, and it tested the comparative and post-visit mechanisms. Second-showing
rate did not move. That is strong evidence against price at the mechanisms this
reduction was capable of testing, and it says nothing about search thresholds, which
are not in play because Stage 1 is healthy.

**Gallery quality.** Not supported as a cause. The photographs are performing at the
stage photographs are supposed to perform at, with views and showings both at
baseline. What is at issue is what they represent, not how good they are.

**Condition.** Not supported. No note in the feedback names condition, systems or
maintenance; the notes that mention the house directly describe it as well
maintained and in good condition.

## Confidence

Rejected. Zone median days on market held flat across the window, and comps 3, 5 and
7 were all listed in the back half and reached 19, 14 and 19 days. The segment is
moving. The subject's Stage 1 to Stage 3 figures track the comp baseline, which is
itself evidence against a segment-wide slowdown, since a frozen market suppresses
views and showings first.

## Null model

**Supported.** The comparison set is Usable, the constraint is located by two
independent measures, the feedback cluster separates the live branches at Stage 4,
and the null was tested against the window and rejected.

## Missing evidence

No floor plan is present in the gallery. Open-house attendance was not supplied.
Neither is load-bearing for the Stage 4 finding, but the absent floor plan is a
plausible contributor to the same mismatch and could not be assessed.

## What would prove this wrong

Feedback showing that buyers had seen dimensions or a floor plan before visiting and
still declined would weaken the mismatch reading substantially. So would a
second-showing rate that is low across the whole comparison set, which would make the
subject's figure ordinary rather than anomalous.

