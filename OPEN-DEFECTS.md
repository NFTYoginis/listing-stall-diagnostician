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

## GATE-1 — COMPUTED exempts small integers

`checks/verify.py` requires every figure in a diagnosis to appear in the case input, but
exempts bare integers of 20 or under and anything written as a percentage. Those exemptions
exist because ratios and stage numbers are legitimately derived rather than read, and without
them the gate would reject correct reports.

The cost is real: a fabricated **"6 of 9 comps remain unsold"** passes, because 6 and 9 are
both under the floor. The gate is loose in a known direction and the direction is upward —
it will not block a correct report, and it will miss a small invented count.

**Closes at:** `code`. Either a derivation whitelist that lets real arithmetic through while
still grounding read figures, or a structured funnel block the model fills in and the checker
recomputes. A wider exemption is not a fix.

---

## GATE-2 — GROUNDING has a length floor

Quoted spans of 25 characters or fewer are treated as labels rather than evidence and are not
checked against the case input. A fabricated four-word showing-feedback quote sits under that
floor. `tests/negative/04--fabricated-quote.md` plants a long one and is caught; a short one
would not be.

**Closes at:** `code`, with a negative fixture carrying a short fabricated quote that the
fixed gate rejects.

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
