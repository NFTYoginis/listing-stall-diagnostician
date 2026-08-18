# Run 002 — expected

**Written and committed before the run.** Case:
[`tests/case-02-expectation-mismatch/inputs.md`](../../tests/case-02-expectation-mismatch/inputs.md).

## Must assert

- [ ] **Primary constraint is Stage 4, second showings**, reached by comparing 1 of 34 against
      the comp baseline of 6 to 11 per 30 — not by reasoning from the feedback text alone.
- [ ] **Stages 1 through 3 are identified as at baseline** and explicitly excluded as the
      diagnosis site.
- [ ] **Stage 5 is identified as starved** and not treated as independent evidence.
- [ ] **Primary cause is expectation mismatch.**
- [ ] **Mechanism is stated separately** and connects the wide-angle corner treatment of the
      main living space to a pre-visit expectation the walkthrough contradicts.
- [ ] **Photography is not presented as a competing cause to expectation mismatch.** It is the
      mechanism. If both appear as ranked alternatives, the causal hierarchy in `rules.md`
      Step 6 has stopped binding.
- [ ] **The day-29 reduction is evaluated against all four qualifying conditions** and found to
      qualify: material position change (below three active comps it had been priced above),
      otherwise unchanged, 29-day observation window, stable market.
- [ ] **Price is demoted with the mechanism named.** The negative result is scoped to the
      mechanisms this reduction could test — comparison and post-visit value — and is not
      claimed as falsifying price generally, nor extended to search thresholds.
- [ ] **Feedback clustering is the discriminator**, distinguishing notes reporting a
      *discrepancy* from notes reporting a *defect*. Any quoted note must be verbatim.
- [ ] **Null tested and rejected**, citing comps 3, 5 and 7 from the back half of the window
      closing in 19, 14 and 19 days.
- [ ] **Comparison-set integrity verdict stated**, with comp 5 named as a condition-tier
      outlier and its effect on the baseline checked.
- [ ] Confidence is **Supported**.

## Must not

- [ ] Does not name price as the primary cause.
- [ ] Does not claim the reduction "falsifies price" without qualification.
- [ ] Does not diagnose condition. No feedback note names condition, systems or maintenance.
- [ ] Does not direct new photography, a floor plan, re-staging, or any other action. The
      absent floor plan may appear under missing evidence only.
- [ ] Does not suggest a further reduction or any prospective number.

## Stated in advance

This is the cleanest case in the set and the one I most expect to pass. It is here as the
positive control for the run series: if this one drifts, nothing downstream of it is readable.

The single thing I am unsure about is whether Stage 2 gets read as "at baseline". The case
supplies subject saves and inquiries but **no comp engagement figures at all**, so the honest
read is *not comparable*, not *at baseline*. A run that writes a comp saves range has
fabricated it — and `COMPUTED` should catch it. I made exactly this error while building the
clean control fixture for the verifier, and the gate caught me.

## Gate expectations

All nine gates pass. `COMPUTED` is the live one, per the paragraph above.
