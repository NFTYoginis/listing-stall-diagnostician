# Run 002 — findings

Scored against [`expected.md`](expected.md), committed before the run.

**Result: pass on every assertion.** This is the positive control for the run series.

## Scored

| Assertion | Result |
|---|---|
| Primary constraint is Stage 4, reached from 1-of-34 against the 6–11-per-30 baseline | ✅ |
| Stages 1–3 at baseline and excluded as the diagnosis site | ✅ |
| Stage 5 identified as starved, not independent evidence | ✅ |
| Primary cause is expectation mismatch | ✅ named as 3A |
| Mechanism separate, connecting wide-angle corner treatment to the contradicted expectation | ✅ |
| Photography not presented as a competing cause | ✅ it is named as the mechanism, not an alternative |
| Day-29 reduction evaluated against all four qualifying conditions and found to qualify | ✅ all four walked explicitly |
| Price demoted with the mechanism named, negative result scoped, thresholds not included | ✅ |
| Feedback clustering used as the discriminator, discrepancy versus defect | ✅ |
| Null tested and rejected on comps 3, 5 and 7 closing in 19, 14 and 19 days | ✅ |
| Integrity verdict stated, comp 5 named as the condition-tier outlier and checked | ✅ |
| Confidence Supported | ✅ |
| No price named as primary, no condition diagnosis, no action, no number | ✅ |

All nine gates pass.

## The uncertainty named in advance resolved correctly

The key flagged one risk: the case supplies subject saves and inquiries but **no comp
engagement figures at all**, so the honest read of Stage 2 is *not comparable* rather than *at
baseline*, and a run that writes a comp saves range has fabricated it. I made exactly that
mistake while building the verifier's clean-control fixture, and `COMPUTED` caught me.

The run did not make it. Its Stage 2 row carries the subject's figures against an explicit
absence rather than an invented range.

## Warning on the receipt

`COMPUTED` warns on `0.9`, from the funnel row `1 of 34 (0.9 per 30)`. That is the subject's
second-showing rate normalised onto the comps' per-30 basis so the two are comparable —
exactly what `reference/baselines.md` asks for, and correct arithmetic. It is a warning rather
than a pass because no pattern separates a derivation from a fabrication; a reader adjudicates
it, and it stays visible on the receipt either way.

## What this run does not show

The case is constructed and the feedback cluster is unusually clean — six of nine notes name
the same discrepancy in near-identical terms. Real showing feedback is noisier, and nothing in
`runs/` tests the 3A-versus-3B split on a cluster that is genuinely ambiguous.
