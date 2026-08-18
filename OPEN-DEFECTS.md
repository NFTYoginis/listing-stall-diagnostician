# Open defects

Everything known to be wrong or unproven with this build, kept in the open.

**A defect closes when the artifact changes, not when the sentence about it improves.** This
repo has already made that mistake once: a defect was found, disclosed, moved to the front
page in commit `612e3ea`, and left open — the visibility improved and the case stayed
unverified. So every entry below names **the layer it must close at**, and no entry may be
marked closed by a documentation change.

Layers, from weakest to strongest:

| Layer | Closing it means |
|---|---|
| `prose` | A sentence changed. **Never sufficient on its own.** |
| `artifact` | A file that is not documentation changed — a fixture, a rule, a product file. |
| `code` | A gate in `checks/verify.py` now catches it, with a negative fixture proving it fires. |
| `run` | A recorded run in `runs/` demonstrates the behaviour, transcript on disk. |
| `external` | Someone outside this session verified it. |

---

## BRIEF-1 — the brief is not quoted from the brief

`BRIEF.md` reconstructs the four judging questions from a condensation and from a different
round of the same competition. Both sources are quoted verbatim and both are labelled, but
neither is the Comp #10 brief. If the literal wording differs, every change in this build was
checked against the wrong text — which is precisely the failure `BRIEF.md` exists to prevent,
reproduced one level up.

**Closes at:** `artifact`. Paste the brief's own words into `BRIEF.md` and re-check the
change table beneath it. Nothing else closes this.

---

## KEY-1 — the case-01 key demanded an invented figure (corrected)

`tests/case-01-search-threshold/expected.md` required the report to confirm search-threshold
exclusion by citing a $400,000 filter boundary that appears nowhere in `inputs.md`. That is
the precise inference-dressed-as-evidence that `examples.md` names and prohibits: a key
requiring the folder to break its own rule.

Found by writing run 001's prediction, before any run existed. Corrected in the same commit as
the keys, from a read rather than from an output — the distinction matters, because a key
repaired after a run agrees with that run by construction.

**Closed at:** `artifact`, 2026-08-18. The assertion block in the case key changed and carries
its own correction note. **Kept in this file rather than deleted**, because the case's key has
now been wrong twice in the same direction (see KEY-2) and the pattern is the finding.

---

## KEY-2 — the case-01 key still wants a more decisive answer than the case licenses

Run 001 declined to name a single primary cause. It held Stage 1's causes in two families —
not-served (1A, 1E) against served-and-not-clicked (1B) — and said the record cannot separate
them, because the filter convention was not supplied **and the images were described rather
than attached**, which makes 1B an image-dependent branch that
`reference/evidence-requirements.md` forbids assessing from a description.

That is `rules.md` Step 6 executed verbatim for genuinely tied causes. The key expected a
leading candidate anyway. The run has the better argument.

`tests/case-01-search-threshold/expected.md` still asserts a single named primary cause. It is
wrong, in the same direction as KEY-1: wanting decisiveness the evidence does not license.

**Closes at:** `artifact`. The case key changes to expect the tie and to name both missing
inputs, or case-01's `inputs.md` gains the images and the convention so a single cause becomes
licensable. Not by adding a sentence to this file.

---

## GATE-1 — COMPUTED cannot distinguish a derivation from a fabrication

The first version of this gate failed a run whenever any figure in the diagnosis was absent
from the case input. Across the five recorded runs it fired eight times and **every single
firing was a correct derivation**: a median of the supplied days-on-market, a per-30
normalisation of a second-showing rate, two square-footage and day-count subtractions, and a
round number that a supplied price reduction crossed. Zero fabrications. The only fabrication
it ever caught was one I made myself, in its own control fixture.

No pattern separates arithmetic-over-supplied-figures from invention. The source build this
gate was modelled on solved that architecturally — a script computed every number from git
history so the model only labelled them — and this family has no such computation step.

The gate is now two-tier: it **fails** only where the ungrounded figure is attributed to the
comparison set as a baseline (the class that makes a wrong diagnosis look measured, and the
class `tests/negative/05--invented-figure.md` plants), and **warns** on everything else, with
the surrounding sentence printed so a reader adjudicates. Warnings are on every
`verify-output.txt` in `runs/`.

Two costs, both real. A fabricated figure outside a baseline attribution now only warns. And
bare integers of 20 or under, and percentages, are exempt entirely — so a fabricated "6 of 9
comps remain unsold" is invisible.

**Closes at:** `code`. A structured funnel block the model fills in and the checker recomputes
from the case input would close it properly. Widening the warn tier is not a fix; nor is
restoring the hard failure, which would fail four of five correct runs.

---

## GATE-2 — GROUNDING has a length floor and two scope exemptions

Three ways a fabricated quote can pass:

1. **Length.** Spans of 25 characters or fewer are treated as labels rather than evidence and
   are not checked. A fabricated four-word feedback quote sits under that floor.
   `tests/negative/04--fabricated-quote.md` plants a long one and is caught; a short one is
   not.
2. **Section scope.** `Missing evidence` and `What would prove this wrong` are exempt, because
   quotes there describe testimony that does not exist yet — run 002 correctly wrote *"for
   instance 'the living room is too small for us'"* as a hypothetical falsifier, and the first
   version of this gate failed the run for it. A fabricated citation placed in one of those two
   sections now passes.
3. **Case.** Matching is case-insensitive, so that a fragment lifted from mid-sentence and
   re-cased at the start of a clause is not scored as a paraphrase. A fabrication that differs
   from a real note only in capitalisation would pass, though there is no obvious way to
   exploit that deliberately.

**Closes at:** `code`, with negative fixtures for all three: a short fabricated quote, a
fabricated quote inside a forward-looking section, and the case variant.

---

## GATE-3 — no gate separates a prospective price from a historical one

`rules.md` prohibits any prospective price, reduction amount or percentage, while explicitly
permitting historical figures already in the case file, because the qualifying-reduction test
cannot be shown without them. The line is prospective-versus-historical, and no string test
separates the two. `NO-RX` catches recommendation *language*; it does not catch a bare number
offered as a target.

This is the single loosest place in the gate set and it is load-bearing for the product's
central refusal. It is listed as UNCOVERED in `runs/gate-coverage.txt`.

**Closes at:** `code`, or a documented decision that it stays a reader's check — in which case
`JUDGE_GUIDE.md` must say so where a reader will see it before trusting the gate. It currently
does.

---

## RUNS-1 — the runs are cold, but they are scored by their builder

Every run in `runs/` was produced in a fresh API session that was given `product/` and the case
input and nothing else: no answer key, no `tests/`, no `runs/`. Each key was committed before
its transcript, and `git log` shows it.

The scoring is still the builder's. A run that disagreed with its key was adjudicated by the
same session that wrote the key. That is weaker than an independent scorer, and it is the
reason the cold gate for this build is explicitly not run by its author.

**Closes at:** `external`. A session that did not build this scores the transcripts against the
committed keys and publishes the disagreements.

---

## RUNS-2 — three earlier blind runs left no artifacts

Before this rebuild, three cases were run blind and scored, and the record of it is prose:
`runs/PRIOR-RUNS.md`, kept because those runs happened and deleting the record would be a
second dishonesty. There are no transcripts. The judge's "the runs are claimed, the files are
not there" was literally accurate, and the underlying cause was structural — `tests/case-NN/`
held `inputs.md` and `expected.md` and nothing else, so an output had nowhere to land and
became narration.

The structure is fixed: `runs/NNN-<slug>/` now has a slot for the transcript. The three
historical runs are still unreplaced.

**Closes at:** `run`, by re-running those three cases into the new layout, or by deleting the
claims they support. Not by re-describing them.

---

## RULES-1 — the folder that scored is not the folder that ships

The three prior blind runs scored an earlier version. Since then `rules.md` gained the Step 1
non-termination fix, the null-grading section, and this rebuild moved every product file into
`product/`, added `intake.md`, `CLAUDE.md`, and `reference/disguised-asks.md`. The runs in
`runs/` exercise the shipping folder, so the gap is narrower than it was, but the corrected
answer keys from the earlier pass have still never been re-run blind against the folder that
now ships.

A key repaired after a run agrees with that run by construction, which is the same circularity
as a key written from spec.

**Closes at:** `run`.

---

## DOOR-1 — the intake click-paths are unverified against live systems

`product/intake.md` tells a user where each input lives — the MLS listing-history panel, the
listing-activity or stats screen, the showing platform's activity report. Those are the common
labels and the file says explicitly that names vary and that the model should ask what system
the user has rather than insist on a name.

None of it has been checked against a live Matrix, Flexmls, Paragon, BrokerBay or ShowingTime
account. It is written at the level of screen-and-label rather than exact menu path
deliberately, to avoid inventing a click sequence — but "deliberately vague" is not the same
as "verified."

**Closes at:** `external`. One agent with MLS access reads the four click-paths and corrects
the labels.

---

## DOOR-2 — the folder is pre-warned about the disguised asks

`product/reference/disguised-asks.md` names five shapes the request-for-the-fix arrives in, and
run `004` then asks for one of them. The refusal holds under pressure and the tape is in
`runs/004-disguised-ask-refusal/transcript.md` — but the folder had been told the category in
advance, so what that run demonstrates is a boundary holding against a *named* disguise.

The stronger test is a disguise the file does not name.

**Closes at:** `run`, with a transcript of a novel disguised ask. Named here so a reader can
discount run 004 by the right amount rather than the wrong one.

---

## SCOPE-1 — the family is not swept, on purpose

`job-post-mismatch`, `ticket-recurrence` and `flat-experiment` share this skeleton and have
none of the above: no `product/` split, no verifier, no runs, no door. `review-rejection` is
held by the orchestrator.

That is the sequencing rule, not an oversight — a five-way sweep is the architecture that
produced the original defect, and applying an unproven shape five times produces five partial
retrofits. **Extrusion is gated on this build passing a cold gate run by a session that did
not build it.**

**Closes at:** `external`, then `artifact` per sibling.

---

Last reviewed: 2026-08-18.

---

## GATE-1 — the falsification guide's own command crashed instead of running

**Found by the cold gate, 2026-08-18.** `JUDGE_GUIDE.md` §2 is the two-minute mechanical proof
of the grounding claim, and it ends "if it doesn't, the grounding claim is false." Its literal
command — `python3 checks/verify.py --file /tmp/t.md` — raised `ValueError` out of
`Path(path).relative_to(ROOT)` and exited **1**. Relative paths failed the same way.

Exit 1 is what a failing gate also returns, so a reader running the guide's own instruction
could see a non-zero exit and conclude the test had passed. The claim was not merely untested,
it was untestable by the documented method, in the file whose job is to invite falsification.

**Closed at:** `code`, 2026-08-18. `display_path()` falls back to the path as given; a label is
cosmetic and must never stop a verdict being reached. A `Judge path` step in `--selftest` now
runs `--file` against a temp path outside the repo and a relative path, and the selftest fails
if either stops returning checks. Verified after the fix: the guide's §2 test, run with one word
altered inside a quoted feedback note, fails `GROUNDING`, names the quote, exits 1.

**Provenance, stated because it weakens the finding:** this defect was found *and* fixed inside
the cold gate, by the same session. The regression step exists so the fix does not rest on that
session's word.

---

## CLAIM-1 — the generated claim credited every run with a gate no run runs

**Found by the cold gate, 2026-08-18.** `status.json` published "5 of 5 recorded runs pass all
10 gates in checks/verify.py." The verifier runs **9** gates per run; `SURFACES` is checked once
for the repository. `46 = 5 × 9 + 1` confirms it. No run passes 10 gates.

This is the one artifact in the build required to be exactly true, since every other surface is
a mirror of it.

**Closed at:** `code`, 2026-08-18. The `SURFACES` registry entry now carries `"scope": "repo"`,
`render_claim()` reports per-run and repo-level counts separately from that data rather than
from a hardcoded name, and the claim reads "all 9 per-run gates (+1 repo-level)". Re-synced to
all three surfaces.

---

## CLAIM-2 — a status field was named for something it does not count

**Found by the cold gate, 2026-08-18.** `status.json` carried `gates_uncovered: 4` while
`--selftest` printed `10/10 gates covered`. Both were correct and they read as a contradiction:
the four are *requirements in rules.md with no executable gate*, correctly enumerated in
`runs/gate-coverage.txt`, not gates missing a fixture. Every gate has a fixture.

A field name is a claim. This one asserted a coverage hole that does not exist.

**Closed at:** `code`, 2026-08-18. Renamed `requirements_uncovered`, matching the section it is
computed from.
