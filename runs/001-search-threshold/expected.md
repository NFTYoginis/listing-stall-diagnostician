# Run 001 — expected

**Written and committed before the run.** Case:
[`tests/case-01-search-threshold/inputs.md`](../../tests/case-01-search-threshold/inputs.md).

Assertions, not expected prose. What must not drift is where the constraint lands, what gets
demoted, whether the null is tested, and whether the boundary holds.

## Must assert

- [ ] **Failure confirmed** — 47 days is placed beyond the comp range of 9 to 28.
- [ ] **Comparison-set integrity verdict is stated**, and comp 6 is named as the limitation
      (adjacent association, ~40% lower dues) or excluded from comparative-value reasoning.
- [ ] **Primary constraint is Stage 1, views.** Not showings, not offers.
- [ ] Subject views (61/wk) are compared to the comp range and identified as below the
      **lowest** comp, not below the average.
- [ ] **Search threshold exclusion is named as the leading Stage 1 candidate**, on $412,000
      against five of six comps between $379,000 and $398,000.
- [ ] **It is not confirmed, and the report says why.** No local filter convention is supplied
      in this case. The report must name that missing input as what would confirm the
      mechanism, rather than asserting a round-number boundary it was never given.
- [ ] **Mechanism is stated separately from the cause** and describes absence from filtered
      search results, not the property being overpriced in value terms.
- [ ] **Downstream stages are explicitly declared uninformative** — no conclusion drawn about
      the gallery, condition, or the walkthrough, because too few buyers reached them.
- [ ] **Syndication ruled out** using the even distribution across the three portals
      (24 / 21 / 16 per week).
- [ ] **Listing data error ruled out** using the verified attributes.
- [ ] **Null tested and rejected**, citing district median DOM at 14 to 16 and comps 4 and 5
      listed in the final three weeks still moving.
- [ ] **The absence of a prior reduction is stated** as no completed experiment being
      available, rather than passed over in silence.
- [ ] Confidence is **Provisional**, not Supported — the comparison set carries a named
      limitation, impression data is absent, and the leading mechanism is unconfirmed.

## Must not

- [ ] Does not assert a filter convention, a round-number threshold, or any specific boundary
      figure the case did not supply. **This is the primary assertion of this run.**
- [ ] Does not treat the two showing-feedback notes as evidence of a cause. Four showings is
      not a readable sample and the report should say so if it mentions them at all.
- [ ] Does not diagnose the hero image as primary. It may stay live and untested once
      visibility is resolved.
- [ ] Does not suggest a price, a reduction, a target band, or a threshold to cross.
- [ ] Does not rewrite the description or direct gallery changes.

## Stated in advance, so a disagreement is informative

This case was corrected the same day, before this run, because its previous answer key
required the report to confirm threshold exclusion by citing a $400,000 boundary that appears
nowhere in the input — the exact inference-dressed-as-evidence that `examples.md` names and
prohibits. See KEY-1 in `OPEN-DEFECTS.md`.

So the interesting outcome here is not whether the run lands on Stage 1. It is whether it
invents the convention. `examples.md` Case 2 shows the confirmed version of this diagnosis
with the convention supplied and an explicit note about why the attribution is written out.
A run that has read that example and then supplies the number itself has learned the wrong
half of it.

**Prediction:** the constraint lands on Stage 1 and the report names threshold exclusion as
leading. I am genuinely unsure whether it confirms it anyway, pulled by the worked example.
If it does, the finding is a defect in `examples.md`'s teaching, not in the run.

## Gate expectations

All nine gates should pass. `COMPUTED` is the one to watch: if the report asserts a
$400,000 threshold, `COMPUTED` should fail on `400000`, because that figure is not in the case
input. That would be the gate independently catching the same defect the key is written to
catch — which is the point of having both.
