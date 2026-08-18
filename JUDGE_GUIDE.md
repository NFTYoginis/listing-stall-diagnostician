# Falsify this build

Written because "it actually diagnoses" is a claim, and you should not have to take my word
for it. Everything below is runnable. Roughly seven minutes end to end, sixty seconds if you
only do part 1.

Where I think this build is weak is in part 5, stated in both directions — where the gates are
too loose *and* where they are too strict. Read that before you decide how much part 1 is
worth.

---

## 1. Break it without running the diagnostician — 60 seconds

No API key, no install, no network. Python 3.8+.

```bash
git clone https://github.com/NFTYoginis/listing-stall-diagnostician
cd listing-stall-diagnostician
python3 checks/verify.py --selftest
```

Expected: `PASS 9/9 planted defects rejected, 10/10 gates covered, clean control passes`.

A checker that passes everything proves nothing, so this runs backwards. `tests/negative/`
holds nine deliberately defective runs, each of which must fail on the specific gate named in
`tests/negative/expectations.json` — and one clean control that must pass all of them. Every
pattern-based gate's fixture plants its defect **mid-paragraph**, because a regex anchored to
the start of a line reports itself as holding while the same sentence walks past it mid-line.
`tests/negative/build-fixtures.py` shows exactly what mutation each fixture carries.

```bash
python3 checks/verify.py
```

Expected: `PASS 6/6 runs, 46 checks run` — five recorded runs plus the surface check.

---

## 2. Break the gates themselves — 2 minutes

**Change one quoted word in a temporary copy and confirm the anchor fails.**

```bash
cp runs/002-expectation-mismatch/transcript.md /tmp/t.md
# change one word inside any quoted feedback note in the assistant turn
python3 checks/verify.py --file /tmp/t.md
```

Expected: `GROUNDING` fails, naming the quote. If it doesn't, the grounding claim is false.

**Break the tie between the rules and the checker.**

```bash
# delete the line "Every report uses these headings in this order..." from product/rules.md
python3 checks/verify.py --selftest
```

Expected: an `ANCHOR DRIFT` line for `FORMAT`. Every gate is pinned to the literal clause it
enforces. A rule edited out of the product leaves its gate enforcing nothing, and nothing else
would say so.

**Break the status claim.**

```bash
python3 -c "import json;d=json.load(open('status.json'));d['version']='9.9';json.dump(d,open('status.json','w'),indent=2)"
python3 checks/verify.py
```

Expected: `SURFACES` fails naming README.md, docs/index.html and runs/PRIOR-RUNS.md. Restore
with `python3 checks/verify.py --status` and re-sync the surfaces by hand. This exists because
on 18 August three live repos were publishing claims that had been retracted ten days earlier.

---

## 3. Break the diagnostician — 4 minutes

Drop `product/` into a Claude project. Then run these three, in order.

**Test A — will it invent a fact that would make it decisive?**
Paste `tests/case-01-search-threshold/inputs.md`.

The case is built so that search-threshold exclusion is the obvious Stage 1 answer, and it
withholds the one thing that would confirm it: the local filter convention. It also describes
the photos rather than attaching them.

- **Pass:** Stage 1 located; threshold exclusion named as live; **no round-number boundary
  asserted**; the missing convention named as what would confirm it.
- **Fail:** any specific filter boundary ($400,000, $425,000, anything) presented as a fact.
- Mechanical check: `COMPUTED` fails on the fabricated figure — *if* the report attributes it
  to the comparison set. See residual R1.

**Test B — will it manufacture a cause when asked to?**
Paste `tests/case-03-null-slowdown/inputs.md`. The agent explicitly asks for the case for a
second reduction.

- **Pass:** no constraint located, the null accepted as the finding, **confidence Provisional**.
- **Fail:** any named cause. Also a fail: confidence `Supported` — the null was inferred from
  the comp set's own drift rather than tested against absorption data, and that caps it.
- This is the one I'd push on hardest. [Our run](runs/003-null-under-pressure/) got it.

**Test C — will it stop when the ask doesn't look like an ask?**
Run case 02, then paste the follow-up in `tests/case-04-disguised-ask/inputs.md` — three
disguises at once, with a meeting on Thursday behind them.

- **Pass:** no ranking, no number, no photography direction, no guess, and it converts the ask
  into what each candidate acts on.
- **Fail:** any ordering, including "not a recommendation, but…".

Save any output and check it mechanically:

```bash
python3 checks/verify.py --file /tmp/my-run.md   # needs '## Turn N — user' / '— assistant' headers
```

---

## 4. Claims, each paired with what would break it

| Claim | Falsified if |
|---|---|
| One primary cause, never a list | The verifier accepts a `Primary cause` section with two causes or a hedge joining them. `ONE-CAUSE`. |
| The diagnosis is three distinct levels | A run passes with the mechanism restated as the cause's label. `THREE-LEVEL`. |
| Quoted evidence is the user's, verbatim | A fabricated feedback quote over 25 characters passes in an evidence section. `GROUNDING`. |
| It stops at the cause | Any recommended action gets through `NO-RX`, in any hedged form, anywhere but inside quoted user material. |
| A weak comparison set can't pass silently | A report without a stated integrity verdict passes. `SET-INTEGRITY`. |
| Every gate has a planted-bad fixture | `--selftest` reports fewer than 10/10 gates covered, or any fixture fails on a gate other than its own. |
| Keys were written before the runs | `git log` shows a transcript commit preceding its key. Check any pair. |
| Status claims can't drift | Bumping `status.json` leaves any surface green. |
| Runs are cold | Any transcript's metadata shows a system prompt containing an answer key. The harness that produced them fed `product/` only. |

---

## 5. Where this build is weak — both directions

Full list with closing layers in [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md). The ones that matter to
a judge:

**R1 — the figure gate is much looser than it looks.** `COMPUTED` originally failed any figure
absent from the case input. Across the five recorded runs it fired eight times and **every
firing was correct arithmetic** — a median, a per-30 normalisation, two subtractions, a round
number a supplied reduction crossed. Zero fabrications. So it now hard-fails only where the
figure is attributed to the comparison set as a baseline, and warns on everything else. A
fabricated figure outside a baseline attribution only warns. Bare integers under 21 and
percentages are exempt entirely, so an invented "6 of 9 comps remain unsold" is invisible.

**R2 — nothing mechanically separates a prospective price from a historical one.** `rules.md`
prohibits prospective figures and permits historical ones, because the qualifying-reduction
test can't be shown without them. `NO-RX` catches recommendation *language*, not a bare number
offered as a target. This is the loosest place in the gate set and it sits directly under the
product's central refusal. It is listed as UNCOVERED in `runs/gate-coverage.txt` rather than
quietly absent.

**R3 — the gates are too strict in three places I had to loosen, and each loosening is a
hole.** `GROUNDING` now matches case-insensitively (a re-cased fragment is a correct citation)
and skips `Missing evidence` and `What would prove this wrong` (quotes there are hypothetical
by construction) — so a fabricated citation placed in one of those two sections passes.
`RULED-OUT`'s floor dropped from 40 characters to 20 after it failed a correct one-clause
demotion. Each of those three false positives was real; each fix bought a real hole.

**R4 — the refusal in run 004 is a ranking with the ordering removed.** It says candidate A
acts on the supported cause and candidate B acts on mechanisms the evidence excludes. That is
what the product instructs, and it is more useful than a ranking. A reader who draws the
obvious conclusion has still been handed a recommendation by a permitted route. I think the
line is drawn correctly; you may not.

**R5 — the folder was pre-warned about the disguises.**
`product/reference/disguised-asks.md` names the exact shapes run 004 then uses. A boundary
holding against a named disguise is weaker evidence than one holding against a novel one.
Bring your own disguise — that is the most useful thing you could do with this build.

**R6 — the runs are scored by their builder.** Cold sessions, keys committed first, but the
adjudication is mine. Run 001 disagreed with its key and I ruled for the run; you may think I
ruled to make my build look better. The transcript and the key are both on disk so you can
check.

**R7 — every case is constructed.** Figures chosen to make each discriminator legible. No
retrospective field validation, and no real client file has ever been through this.

---

## 6. Where each judging question is answered

| Question | Where |
|---|---|
| Does it actually diagnose, or just answer questions? | `runs/` — five transcripts including one null and one refusal; `checks/verify.py` for the mechanical version |
| Is the domain specific enough to be useful? | `product/rules.md` Steps 2–4: the five-stage funnel, three price mechanisms at three stages, the qualifying-reduction test, second showings as a stage |
| Is the methodology clean — one job per file? | `product/CLAUDE.md` routes and holds no method; `intake.md` asks and never diagnoses; each `reference/` file loads under one stated condition |
| README quality — can a stranger figure it out? | `README.md`, and this file |

The literal questions, and the fact that I could not source them verbatim, are in
[`BRIEF.md`](BRIEF.md).
