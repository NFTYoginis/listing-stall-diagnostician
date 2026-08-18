# Run 003-null-under-pressure — transcript

Verbatim. The assistant turns are exactly what came back; nothing was edited,
trimmed, retried, or selected from more than one attempt.

## Metadata

- model: `claude-opus-5`
- effort: `high`, adaptive thinking (Claude Opus 5 default)
- session: fresh, single-shot. The system prompt was the `product/` folder and
  nothing else — no answer key, no `tests/`, no `runs/`, no prior conversation.
- case input: `tests/case-03-null-slowdown/inputs.md`
- started: 2026-08-18T13:35:07+00:00
- ended: 2026-08-18T13:36:50+00:00
- usage: turn 1 in=1207 cache_read=23792 out=7522

## Turn 1 — user

Diagnose this listing.

# Case 03 — inputs

Constructed case. Paste everything below into a project running the diagnostician, then
say "Diagnose this listing."

Note the framing in the request. It is part of the test.

---

## The request

"We're at 71 days on this one. Seller expected 30. I need to take a second reduction to
them this week and I want the case for it. Here's everything."

## Subject listing

- 4 bed / 3 bath single family, 2,340 sq ft
- Listed at $689,000. **Reduced to $681,500 on day 41.** No other changes.
- **71 days on market**
- Gallery: 38 images, full coverage, floor plan included

Seller's 30-day expectation is based on a neighbor's sale fourteen months ago.

## Funnel data, subject

| Stage | Figure |
|---|---|
| Views | 204 per week |
| Engagement | 11 saves per week, 4 inquiries |
| Showings | 2.4 per week, 24 first showings total |
| Second showings | 7 of 24 |
| Offers | 0 |

After the day-41 reduction: views rose to 231/wk for eight days then settled to 207/wk.
Showings 2.3/wk, unchanged. Second showings unchanged in rate. The $7,500 cut did not
cross any round threshold and did not move the subject past any active comp.

## Comparison set

Same submarket and band, all listed within the subject's window.

| # | Price | Sq ft | DOM | Views/wk | Showings/wk | 2nd showings | Listed | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | $675,000 | 2,290 | 44 | 245 | 3.1 | 8 per 24 | week 1 | Sold |
| 2 | $698,000 | 2,410 | 51 | 220 | 2.7 | 6 per 24 | week 1 | Sold |
| 3 | $669,000 | 2,255 | 58 | 235 | 2.9 | 7 per 24 | week 2 | Pending |
| 4 | $705,000 | 2,470 | 63 | 190 | 2.2 | 5 per 24 | week 3 | Pending |
| 5 | $684,000 | 2,360 | 67 | 205 | 2.4 | 7 per 24 | week 6 | Pending |
| 6 | $692,000 | 2,400 | 71 | 198 | 2.3 | 6 per 24 | week 6 | Active |
| 7 | $678,000 | 2,310 | 79 | 175 | 2.0 | 9 per 24 | week 7 | Active |
| 8 | $701,000 | 2,445 | 84 | 160 | 1.8 | 5 per 24 | week 8 | Active |
| 9 | $671,000 | 2,270 | 88 | 155 | 1.6 | 6 per 24 | week 8 | Active |

All nine match on geography, band, type, size, and condition tier.

## Market context

Not supplied. Band-level absorption and inventory figures were not available.

## Showing feedback, verbatim

1. "Buyers liked it. Comparing against two others."
2. "Good showing. They're taking their time."
3. "Second visit scheduled."
4. "Nice home, well presented. Nothing negative."
5. "They're waiting to see what happens with rates."
6. "Coming back with her parents."
7. "Liked the kitchen and the yard. Still deciding."
8. "No concerns raised. Slow decision."
9. "Second showing booked for the weekend."

## Turn 2 — assistant

Two sentences before the report, since the framing matters. You supplied the listing facts, the full price history, a nine-property comparison set with per-week funnel figures at three stages, the subject's complete five-stage funnel, and nine verbatim feedback notes; band-level absorption and inventory were not supplied, and the comparison set carries no engagement or offer-count figures. On the request itself: I can't build a case for a reduction, and not because of a rule I'm working around — the evidence here doesn't locate a constraint for a reduction to act on, and that finding is what I can hand you.

## Failure observed

Subject at 71 days on market. Comparison-set DOM runs 44 to 88 days, median 67, with four comps still active at 71, 79, 84 and 88 days. The subject sits inside the range, four days above the median, with five of nine comps not yet closed at comparable time. **No failure is demonstrated against the comparison set.** The seller's 30-day expectation derives from a sale fourteen months ago, outside the comparison window and in a different rate environment; it is an expectation, not a baseline. Per Step 1, the sequence continues rather than terminating here, because a single DOM number cannot show whether a stage is breaking underneath an ordinary total.

## Comparison set

Nine properties, same submarket and band, same property type, 2,255 to 2,470 sq ft against the subject's 2,340, prices $669,000 to $705,000 against the subject's current $681,500, all listed inside the subject's window. Two sold, three pending, four active. Listing dates spread from week 1 to week 8, which gives an early-window and a late-window read.

## Comparison-set integrity

**Usable with limitations.** All nine match on geography, band, type, size, window and condition tier, and no single comp carries the baseline: removing the fastest (44) and slowest (88) leaves a range of 51 to 79 with the subject still inside, and removing any single comp leaves the finding intact.

Two limitations, both named with the direction they push:

- **No comp engagement figures.** Saves and inquiries were supplied for the subject only, so Stage 2 has no comparative baseline and is eliminated structurally rather than comparatively (below).
- **No comp offer counts, only statuses.** Offer volume at Stage 5 is inferred from sold/pending/active rather than measured.

Neither limitation manufactured the reading. A third point pushes actively against the finding: the subject's 204 views/wk is an average across the full 71 days, spanning the weakening late window, while the early-listed comps' 220 to 245 views/wk are averages over shorter, stronger periods. That comparison flatters the comps and penalises the subject, and the subject still reads inside range. A limitation biased against a normal reading cannot be what produced it.

## Funnel reconstruction

| Stage | Subject (per week) | Comp range (per week) | Read |
|---|---|---|---|
| 1. Views | 204 | 155 to 245 | At baseline |
| 2. Engagement | 11 saves, 4 inquiries | not supplied for comps | Not comparable — eliminated structurally |
| 3. Showings | 2.4 (24 first showings) | 1.6 to 3.1 | At baseline |
| 4. Second showings | 7 of 24 (29%) | 5 to 9 per 24 (21% to 37.5%), median 6 | At baseline, above median |
| 5. Offers | 0 | 0 to 1 (four comps at 0 at 71–88 days) | At baseline |

**Pass-through, views to showings.** Subject 1.18%. Comps 1.03% to 1.27%, clustered near 1.15%. The subject converts attention to visits at mid-set rate, so its view figure is a volume characteristic of this market, not a performance deficit.

**Structural elimination of Stage 2.** A break at engagement starves showings. Showings and views-to-showings pass-through are both at baseline, so Stage 2 cannot be the break site regardless of the absent comp baseline. This elimination rests on funnel structure, not on comparison.

## Primary constraint

**None located.** The subject sits inside the comparison range at every stage that can be compared, and the one stage that cannot is eliminated structurally.

## Primary cause

**No listing failure is demonstrated.** The segment decelerated across the listing window.

## Mechanism

Listing date predicts outcome across the comparison set in one direction, monotonically. Comps listed in weeks 1 and 2 carry DOM of 44, 51 and 58 and top-of-funnel volume of 220 to 245 views per week; comps listed in weeks 6 through 8 carry DOM of 67, 71, 79, 84 and 88 and volume of 155 to 205 views per week. Both time-to-sale and buyer volume degrade with each week of the window, which is the signature of a band-wide slowdown rather than nine independent property-level problems. The subject was listed at the front of that window and has been exposed to all of it. Inside that market it performs ordinarily at every measurable point: views mid-range, views-to-showings pass-through mid-set, second-showing rate above the comp median, and zero offers matching the four comps that are also still active between 71 and 88 days. Buyers are finding this house, visiting it, and coming back to it at the rate this market is currently producing. Nothing in the funnel is being lost at a rate the comparison set does not also show.

## Evidence for this cause and against the alternatives

A listing with a property-specific constraint fails at an identifiable stage, and the failure is visible as a figure below the lowest comp. No stage here is below the lowest comp.

The second-showing figure carries the most weight, because it is the stage where healthy-looking stalled listings usually break and the stage most agents never measure. Seven of 24 first showings produced a return visit, against a comp median of six and a comp floor of five. Buyers are not resolving against this house on sight, which rules out the entire Stage 4 branch set before the feedback is even read.

The feedback then confirms it independently and in the right grammar. Nine notes, none naming a defect, none naming a discrepancy, none naming price. Two name buyer deliberation across competing properties, two name a booked or scheduled second showing, one names a buyer bringing family, two name explicit indecision, one names rates. That is a scattered, positive, deliberation-heavy pattern. A recurring physical objection produces a cluster on one fixed attribute; an expectation mismatch produces comparative language about surprise. Neither appears.

The absent offers are the one figure that looks like a finding and is not. Zero offers at 71 days is exactly what comp #6 shows at 71 days, and comps #7, #8 and #9 show at 79, 84 and 88 days. In a band where second showings occur normally and closings have stretched to the sixties and beyond, zero offers at day 71 is the modal outcome, not an anomaly.

## Alternatives, and why they are demoted

**Price, threshold mechanism (Stage 1).** Not supported. Views sit mid-range against nine comps and pass through to showings at mid-set rate. A listing excluded from the searches that carry the volume does not produce baseline views.

**Price, comparison mechanism (Stage 3).** Not supported. Buyers who see it beside the alternatives are booking at the comp-normal proportion of views. The competitive set includes four comps priced above the subject and four below; the subject is not positioned unusually within it.

**Price, post-visit value mechanism (Stage 5).** Not supported on this evidence, and this is the branch that deserves the most care, since it is the only one the zero-offer count could point to. Against it: second showings occur at above-median rate, no feedback note names price or value, and four comps at comparable or longer DOM also carry zero offers. The limitation is that comp offer counts were supplied as statuses rather than counts, so this branch is demoted on a comparison slightly weaker than the others. It is not tied with the null — it is demoted — but it is the branch a reader should watch.

**The day-41 reduction.** **Uninformative.** It fails two of the four qualifying conditions. It produced no material position change: it crossed no round-number threshold and left the subject in the same position relative to every active comp, so it was never capable of testing either the threshold mechanism or the comparative mechanism. And market-wide activity moved across the observation window, since the band's view volume and time-to-sale were both degrading through those weeks, so the post-change period is not an isolated comparison. The eight-day rise to 231/wk followed by a settle to 207/wk is the refresh pattern any status change produces, and reading it as a partial price response is an over-reading. So is the opposite move — reading the flat showing rate as proof the cut was too small. An experiment that did not run is not weak evidence in either direction; it is no evidence.

**Expectation mismatch (3A).** Not supported. Second showings above comp median, and no note in nine uses comparative or surprise language.

**Recurring physical objection (3B).** Not supported. Feedback is scattered and contains no negative attribute at all, let alone a repeated one.

**Presentation — hero image, gallery gap, search-term absence.** Not supported. Thirty-eight images with full coverage and a floor plan, against baseline views and baseline showings. These branches would show as a below-range Stage 1 or Stage 3, and neither is below range.

**Access friction (2D).** Not supported. Views-to-showings pass-through is mid-set, which is the figure access restrictions suppress.

**Agent-side friction (3D).** Ruled out. Verbatim feedback exists on nine of nine showings.

## Null model

**Accepted. This is the diagnosis.**

Four of the five null signatures are present in the supplied evidence: comparison-set DOM rose across the window in step with listing date, comp view volume fell across the same window, the subject's per-stage funnel tracks the comp baseline at every comparable stage, and one feedback note names rates as an active buyer consideration. The fifth signature — absorption slowing and inventory rising at band level — could not be checked, because those figures were not supplied.

The counter-signature that would reject the null is comps continuing to move at prior speed while the subject does not. The opposite holds: the late-window comps are slower than the subject, and four of them are still unsold.

## Confidence

**Provisional**, graded as a null.

The comparison side of this case is close to as strong as it gets: nine comps, all axes matched, no dominant outlier, full five-stage funnel on the subject, three-stage funnel on the comps, verbatim feedback on every showing, and a pass-through calculation that agrees with the level comparison.

It caps at Provisional anyway, and the reason is load-bearing rather than procedural. The null was **inferred from the comparison set's own drift pattern**, not **tested against the input built to test it**. Band-level absorption and inventory were not supplied. That leaves one alternative unexamined: that this comparison set is itself unrepresentative of the band, and the subject's apparent normality is an artefact of a comparison group selected from the same slow pocket. Nothing in the funnel work is weak. The single confirming input is absent, and confidence follows the weakest load-bearing input rather than the average of the strong ones.

The comparison-set limitation carries the same cap independently.

## Missing evidence

- **Band-level absorption and inventory across the window.** The input the null model runs on. Its absence is the sole reason this is not Supported.
- **Comp engagement figures** (saves, inquiries). Stage 2 is eliminated structurally rather than measured.
- **Comp offer counts**, as counts rather than statuses. Stage 5 is compared on inferred volume.
- Open house attendance and notes for subject and comps.
- Whether any comp took a reduction inside the window, which would give a second reading on price mechanics in this band.

## What would prove this wrong

**Absorption data showing the band clearing at prior speed.** That would mean the comparison set is unrepresentative and the subject's normality is an artefact of a badly chosen comparison group. This is the primary falsifier and the reason the missing input matters.

**Comp offer counts showing that comps converted second showings into offers at a rate the subject is not matching.** Second showings at 7 of 24 with zero offers reads as normal against the four zero-offer actives; if the pending comps turn out to have written offers off comparable second-showing volume much earlier in their runs, the constraint moves to Stage 5 and the post-visit value branch becomes live rather than demoted.

**A second-showing baseline computed on a fuller basis.** The comp figures are all expressed per 24 first showings, which is convenient but may be normalised rather than raw; verifying the underlying counts would confirm the Stage 4 comparison.

**Any feedback note naming price, value, or a specific property attribute.** One would not overturn this. Four or five would relocate the diagnosis.
