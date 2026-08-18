# Run 001 — findings

Scored against [`expected.md`](expected.md), which was committed before the run.

**Result: pass on every assertion, and the run beat the key on one point.**

## Scored

| Assertion | Result |
|---|---|
| Failure confirmed, 47 days beyond the 9–28 comp range | ✅ |
| Comparison-set integrity verdict stated; comp 6 named as the limitation | ✅ Usable with limitations; comp 6 retained for the DOM range, excluded from comparative-value reasoning |
| Primary constraint is Stage 1, views | ✅ |
| Views compared to the lowest comp, not the average | ✅ "under a third of the lowest comp" |
| Search threshold exclusion named as a leading Stage 1 candidate | ✅ named as 1A, inside the "not served" family |
| **Not confirmed, and the report says why** | ✅ **"the filter convention that would confirm the threshold branch was not supplied"** |
| Mechanism stated separately from cause | ✅ |
| Downstream stages explicitly declared uninformative | ✅ |
| Syndication ruled out on even cross-portal distribution | ✅ |
| Listing data error ruled out on verified attributes | ✅ |
| Null tested and rejected on district median DOM and late-window comps | ✅ |
| Absence of a prior reduction stated, not passed over | ✅ |
| Confidence Provisional | ✅ |
| No invented filter convention, threshold, or boundary figure | ✅ — **the primary assertion of this run** |
| No price, reduction, target band, or threshold to cross | ✅ (`NO-RX` clean) |
| Feedback not treated as evidence — four showings is not a sample | ✅ |
| Hero image not diagnosed as primary | ✅ |

All nine gates pass. `COMPUTED` did not fire on `400000`, because the report never
asserted it.

## Where the run disagreed with the key, and won

The key expected search threshold exclusion to be **named as leading** among the Stage 1
causes. The run declined to rank at all:

> **Not determined.** Two families remain live at Stage 1 and this record cannot separate
> them: **not served** (1A search threshold exclusion, 1E search-term absence) versus
> **served and not clicked** (1B hero image failure).

Its reason is one the key had not considered. The key assumed the magnitude argument from
`examples.md` Case 2 — a view deficit this large is too big for a presentation cause, because
a weak hero image depresses click-through on impressions that still occur rather than removing
the listing from the grid. The run refused to run that argument, because **the images were
described in the case and never supplied.** `reference/evidence-requirements.md` says a
description of a photo is not evidence about the photo, and that image-dependent branches must
be reported as unassessed and named. 1B is an image-dependent branch.

That is the better reading, and it is the behaviour `rules.md` Step 6 specifies verbatim for
this situation: *"If two causes are genuinely tied on the evidence, do not average them into a
vague statement. Name both, say precisely why the record cannot separate them, and name the
single input that would."* The run named both families, named why, and named the two inputs —
the local filter convention and the actual images.

**Consequence: `tests/case-01-search-threshold/expected.md` is wrong a second time.** It was
corrected earlier the same day for demanding an invented $400,000 boundary; it still expects a
single named primary cause on a case that supplies neither the filter convention nor the
images. Logged as KEY-2 in `OPEN-DEFECTS.md`, at the `artifact` layer.

This is the second defect this case's key has produced, and both were in the same direction:
the key wanted a more decisive answer than the case licenses.

## What this run does not show

It does not show the folder resisting a *supplied-but-wrong* convention, only an absent one.
And the case is constructed — the numbers were chosen to make Stage 1 unmissable. A real
listing with a 40% view deficit rather than a 70% one would be a harder test and is not
covered by anything in `runs/`.
