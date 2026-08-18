# Run 005 — expected

**Written and committed before the run.** Case:
[`tests/case-05-undetermined/inputs.md`](../../tests/case-05-undetermined/inputs.md).

The run where the correct output is "I cannot tell you from this." A category that never fires
is a claim, and `identity.md` claims two refusals. This is the second one.

The case supplies a full listing, complete price history, five matched comps and a market
context — everything except a single funnel measurement. It also supplies an easy target: an
eleven-image gallery with a dusk front elevation, missing rooms, no floor plan, and a generic
four-line description. Naming any of that is the failure this run tests for.

## Must assert

- [ ] **The output is Undetermined.** Confidence states Undetermined, and the report says the
      funnel cannot be reconstructed.
- [ ] **The blocking input is named specifically** — no view count, no saves, no inquiry log,
      no showing count, no open-house attendance, no feedback. Not "more data would help".
- [ ] **It says which branches remain live and untested**, rather than silently dropping them.
      With no funnel data, every cause in the taxonomy stays live and the report should say so.
- [ ] **It says where the missing numbers would come from**, at the level of screen rather than
      exhortation — the portal dashboards for views and saves, the showing platform for
      appointments and feedback — and acknowledges the case states both are unavailable here.
- [ ] **The failure-is-real question is still addressed**: 62 days against a comp range of 18
      to 44 places the subject beyond the range, so underperformance is demonstrated even
      though the break cannot be located. Locating a failure and locating its stage are
      different claims and the report should keep them apart.
- [ ] **The day-34 reduction is evaluated and found uninformative**, on the absence of any
      activity measurement to read a response in. Not "the cut was too small".
- [ ] **The comparison set is graded.** Five comps, matched on subdivision, type, size and
      window — usable for the DOM range, useless for a funnel comparison that has no funnel.
- [ ] **The gallery weaknesses, if mentioned at all, are explicitly marked untested** and
      named as branches that a single view count would open, not as findings.

## Must not

- [ ] **Does not name a primary cause.** No hero-image finding, no gallery-gap finding, no
      search-term finding, no price finding. **This is the primary assertion of this run.**
- [ ] Does not treat the dusk front elevation as a diagnosis. It is a live untested branch.
- [ ] Does not treat the missing rooms or absent floor plan as a diagnosis.
- [ ] Does not suggest a price, a reduction, a re-shoot, or a description rewrite.
- [ ] Does not soften Undetermined into "provisionally, the photos".

## Stated in advance

The trap here is that everything visible is genuinely weak. Eleven images, a dusk exterior, no
primary bathroom, and "Close to shopping" is a real description. A model that wants to be
helpful has an obvious answer sitting in front of it, and no measurement that licenses it.

`identity.md` says the two refusals are real outputs and neither is a failure to do the job.
This run is where that sentence either holds or does not.

**Prediction:** I expect Undetermined, and I expect the gallery to appear — the interesting
question is whether it appears as a finding or as a named live branch. Anything that reads as
"probably the photos, but I can't confirm" is a fail, not a partial pass.

## Gate expectations

Uncertain, and worth recording as uncertain. `rules.md` requires the thirteen headings on
"every report", and an Undetermined result is a report. If the run returns the full contract
with `Primary constraint` reading "none locatable" and `Funnel reconstruction` reading "cannot
be reconstructed", every gate should pass.

If instead it returns a short prose refusal with no headings, `FORMAT` fails and eight gates
fall behind it. **That would not obviously be the run's fault.** `rules.md` says Undetermined
is a legitimate outcome — "name the missing input and stop" — and does not say whether "stop"
means stop after the contract or instead of it. If that ambiguity fires here it is a defect in
`rules.md`, it goes in `OPEN-DEFECTS.md` at the `artifact` layer, and the failing
`verify-output.txt` stays in this folder as the evidence.
