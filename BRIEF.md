# The brief

The questions this build is judged on, in the words of whoever set them. Every change to
this repo is checked against what is on this page, not against what we would prefer to be
measured on.

This file exists because of a specific, expensive mistake. The Comp #10 panel judged four
published questions; the judges had separately drafted a six-criterion craft rubric, and the
results post says the winner's name changes if that rubric had been the standard. We had
optimised toward a craft standard nobody was scoring. Writing the literal questions down
first is the cheapest available fix.

---

## The four questions

The competition brief is not on disk in this repo, and I will not paraphrase a source I
cannot quote. Two on-disk sources record the questions; both are quoted here verbatim, and
neither is the brief itself.

**Source 1 — the build spec this repo was rebuilt from**
`~/Desktop/Claude Research Assistant/reports/2026-08-18-diagnostician-family-build-spec.md`,
lines 36–37, condensed by its author rather than quoted from the brief:

> For Comp #10 those were: does it diagnose, is the domain useful, does each file do one
> job, can a stranger figure it out.

**Source 2 — the same four axes as recorded for an earlier round in the same competition
series**, `2026-05-19-w5-coach-new-yoga-teacher-build-brief.md`, lines 20–24, where they are
marked *"Four judging axes, stated verbatim in the brief"*:

> 1. **Does the coach actually coach** (or just answer questions)
> 2. **Is the domain specific enough to be useful**
> 3. **Is the methodology clean** — each file does one job well
> 4. **README quality** — can a stranger figure this out

The four axes are stable across rounds; only the first is domain-swapped. For this build,
question 1 reads: **does the diagnostician actually diagnose, or does it just answer
questions?**

> ⛔ **NOT VERBATIM FROM THE COMP #10 BRIEF.** Source 1 is a condensation. Source 2 is a
> different round. If the literal Comp #10 wording differs, this file is wrong and every
> change below was checked against the wrong text. **Operator: paste the brief's own words
> here and re-check.** Logged in `OPEN-DEFECTS.md` as BRIEF-1, closable only by replacing
> this section.

---

## What each change in this build serves

| Question | What answers it | Where |
|---|---|---|
| **1. Does it actually diagnose?** | It locates one constraint at one funnel stage, names one cause, and refuses to prescribe — and there are recorded runs on disk where a stranger can watch it do so, including runs where it declines and one where it finds nothing wrong. | `runs/`, `product/rules.md` Steps 3–6 |
| **1. Does it actually diagnose?** | The claim is mechanically checked rather than asserted: nine gates run over the recorded runs, each with a planted-bad fixture proving the gate fires. | `checks/verify.py`, `tests/negative/` |
| **2. Is the domain specific enough to be useful?** | The five-stage funnel, the three price mechanisms acting at three different stages, the qualifying-reduction test, and the second showing treated as its own stage rather than a metric. None of that is inventable from outside the domain. | `product/rules.md`, `product/reference/failure-modes.md` |
| **3. Is the methodology clean — one job per file?** | `CLAUDE.md` routes and holds no payload. `intake.md` asks and never diagnoses. `rules.md` is the method and the contract. `identity.md` is the boundary. `examples.md` demonstrates. Each `reference/` file loads under one stated condition. | `product/` |
| **4. Can a stranger figure it out?** | The README is the door, not the architecture write-up, and `JUDGE_GUIDE.md` hands a hostile reader the attacks in order, with the claims paired to the thing that would break them. | `README.md`, `JUDGE_GUIDE.md` |

---

## What this brief does not ask for, and what was cut because of it

Nothing on this page asks for a landing page, a social card, or an OG image. This repo shipped
all three before it shipped a verifier or a single run transcript, which is the same error in
priority the spec was written to stop. They are still in `docs/`, and they are not being
extended: no marketing surface gets touched again ahead of the four answers above.
