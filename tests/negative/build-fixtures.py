#!/usr/bin/env python3
"""
Build the self-test fixtures.

One clean control, and one deliberately defective copy of it per gate. The clean
control's user turn is `tests/case-02-expectation-mismatch/inputs.md` verbatim, so
the grounding and figure gates are checked against a real case rather than against
a string invented to satisfy them.

Each negative fixture is the clean control with exactly one mutation applied. The
mutation is written here in the open so a reader can see precisely what defect each
fixture carries, rather than diffing ten near-identical files by eye.

**Every pattern-based gate gets a mid-sentence defect.** A regex anchored to the
start of a line reports itself as holding while the same sentence walks past it in
the middle of a paragraph. The fixtures for ONE-CAUSE, GROUNDING, COMPUTED, NO-RX
and CONFIDENCE all plant their defect mid-paragraph for that reason.

    python3 tests/negative/build-fixtures.py

Standard library only. Rerunning overwrites the fixtures in place.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CASE = ROOT / "tests" / "case-02-expectation-mismatch" / "inputs.md"

HEADER = """# Fixture — {title}

Synthetic. Built by `tests/negative/build-fixtures.py` for `checks/verify.py --selftest`.
Not a run. Nothing in `runs/` was produced this way.

**Planted defect:** {defect}

## Metadata

- source case: `tests/case-02-expectation-mismatch/inputs.md`
- gate that must reject it: `{gate}`

## Turn 1 — user

{case}

## Turn 2 — assistant

{body}
"""

# The clean diagnosis. Every quoted span and every figure below is present in
# case-02's inputs.md; that is what makes it a positive control rather than a
# second opinion about what good output looks like.
CLEAN = """## Failure observed

Listing active 58 days. The comparison set ranges 11 to 41 days on market, and six of
the eight are closed or pending. The subject sits beyond the top of that range.
Failure confirmed.

## Comparison set

Eight properties in the same school zone, overlapping band, all listed inside the
subject's twelve-week window. Five sold, one pending, two active.

## Comparison-set integrity

**Usable.** Geography, band, type, size and window match across the set. Condition
tier is comparable across seven of the eight; comp 5 was renovated inside the last
eighteen months. Removing comp 5 leaves the days-on-market range and the
second-showing baseline materially unchanged, so no single comp is carrying the
baseline.

## Funnel reconstruction

| Stage | Subject | Comp range | Read |
|---|---|---|---|
| 1. Views | 312 per week | 240 to 380 per week | At baseline |
| 2. Engagement | 19 saves per week, 6 inquiries | not supplied for the comps | Not comparable |
| 3. Showings | 4.1 per week | 2.8 to 5.0 per week | At baseline |
| 4. Second showings | 1 of 34 first showings | 6 to 11 per 30 first showings | Clearly below |
| 5. Offers | 0 | 0 to 2 | Below, starved |

## Primary constraint

**Stage 4, second showings.** The listing performed at or above baseline through the
showing appointment.

## Primary cause

**Expectation mismatch.**

## Mechanism

The gallery's three images of the main living space are all shot from a corner at
wide angle with the seating pushed to the walls, which reads as materially larger
than the stated square footage supports. Buyers arrive holding a pre-visit
expectation of scale that the walkthrough contradicts in the first minute, and they
resolve against the house on that visit rather than leaving undecided. A buyer who
leaves undecided books a second visit. These buyers are not undecided.

## Evidence for this cause and against the alternatives

The second-showing rate is the discriminating figure. Buyers who like a house and
intend to negotiate come back to it. A rate of 1 of 34 against a comp baseline of 6
to 11 per 30 means buyers are not leaving unresolved; they are leaving resolved.

The feedback clusters on surprise rather than on an attribute. Six of the nine notes
describe a gap between two impressions rather than a defect in the house: "Photos
oversell the great room. Not what they pictured walking in." and "Buyers felt misled
on the size of the main floor." A buyer objecting to a small room says the room is
small. These buyers are saying they expected something else, which locates the fault
in the representation rather than in the property.

## Alternatives, and why they are demoted

**Price, comparison mechanism at Stage 3.** Not supported. Showings run at 4.1 per
week against a comp range of 2.8 to 5.0, so buyers are not filtering the listing out
on price before booking.

**Price, post-visit value mechanism at Stage 5.** Weakened, and the prior reduction
is readable here. The day-29 cut was $14,000 on a $479,000 list, taking it to
$465,000 and moving the subject below three active comps it had previously been
priced above. The listing was otherwise unchanged across the same period, 29 days of
observation follow the change, and zone activity was flat. That is a qualifying
reduction, and it tested the comparative and post-visit mechanisms. Second-showing
rate did not move. That is strong evidence against price at the mechanisms this
reduction was capable of testing, and it says nothing about search thresholds, which
are not in play because Stage 1 is healthy.

**Gallery quality.** Not supported as a cause. The photographs are performing at the
stage photographs are supposed to perform at, with views and showings both at
baseline. What is at issue is what they represent, not how good they are.

**Condition.** Not supported. No note in the feedback names condition, systems or
maintenance; the notes that mention the house directly describe it as well
maintained and in good condition.

## Null model

Rejected. Zone median days on market held flat across the window, and comps 3, 5 and
7 were all listed in the back half and reached 19, 14 and 19 days. The segment is
moving. The subject's Stage 1 to Stage 3 figures track the comp baseline, which is
itself evidence against a segment-wide slowdown, since a frozen market suppresses
views and showings first.

## Confidence

**Supported.** The comparison set is Usable, the constraint is located by two
independent measures, the feedback cluster separates the live branches at Stage 4,
and the null was tested against the window and rejected.

## Missing evidence

No floor plan is present in the gallery. Open-house attendance was not supplied.
Neither is load-bearing for the Stage 4 finding, but the absent floor plan is a
plausible contributor to the same mismatch and could not be assessed.

## What would prove this wrong

Feedback showing that buyers had seen dimensions or a floor plan before visiting and
still declined would weaken the mismatch reading substantially. So would a
second-showing rate that is low across the whole comparison set, which would make the
subject's figure ordinary rather than anomalous.
"""


def mutate(text, old, new, label):
    if old not in text:
        raise SystemExit("fixture builder: anchor not found for %s:\n  %r" % (label, old))
    return text.replace(old, new, 1)


FIXTURES = []


def fixture(name, gate, defect, fn):
    FIXTURES.append((name, gate, defect, fn))


fixture(
    "01--section-out-of-order.md", "FORMAT",
    "Confidence is reported before the null model, so the contract's order is broken "
    "while every required heading is still present.",
    lambda t: t.replace(
        "## Null model", "@@NULL@@", 1
    ).replace("## Confidence", "## Null model", 1).replace("@@NULL@@", "## Confidence", 1),
)

fixture(
    "02--two-primary-causes.md", "ONE-CAUSE",
    "The primary cause is hedged into two causes mid-sentence, which is the shape a "
    "flat audit takes when it is wearing a diagnosis's headings.",
    lambda t: mutate(
        t, "**Expectation mismatch.**",
        "**Expectation mismatch.** On this record the finding is best read as a "
        "combination of expectation mismatch and post-visit value judgement, with the "
        "two acting together at the same stage.",
        "ONE-CAUSE"),
)

fixture(
    "03--levels-collapsed.md", "THREE-LEVEL",
    "The mechanism is restated as a label instead of traced to this listing's evidence, "
    "collapsing three levels into two.",
    lambda t: mutate(
        t,
        t[t.index("## Mechanism"):t.index("## Evidence for this cause")],
        "## Mechanism\n\nThe photographs create expectation mismatch.\n\n",
        "THREE-LEVEL"),
)

fixture(
    "04--fabricated-quote.md", "GROUNDING",
    "A plausible showing-feedback quote that appears nowhere in the case input is "
    "planted mid-paragraph, between two quotes that are real.",
    lambda t: mutate(
        t,
        'and "Buyers felt misled\non the size of the main floor."',
        'and "The great room is nowhere near what the listing photos promised, and they '
        'said so before they were through the door." and "Buyers felt misled\n'
        'on the size of the main floor."',
        "GROUNDING"),
)

fixture(
    "05--invented-figure.md", "COMPUTED",
    "A comp baseline figure the case never supplied is written mid-sentence into the "
    "evidence section, where it reads as measured.",
    lambda t: mutate(
        t,
        "A rate of 1 of 34 against a comp baseline of 6\nto 11 per 30",
        "A rate of 1 of 34 against a comp baseline of 273\nper 30",
        "COMPUTED"),
)

fixture(
    "06--rival-without-evidence.md", "RULED-OUT",
    "A rival is named and demoted with no eliminating evidence attached, which is a "
    "list of dismissals wearing the demotion section's name.",
    lambda t: mutate(
        t, "**Condition.** Not supported.",
        "**Access friction.** Not supported.\n\n**Condition.** Not supported.",
        "RULED-OUT"),
)

fixture(
    "07--no-integrity-verdict.md", "SET-INTEGRITY",
    "The integrity section discusses the comparison set at length but never states the "
    "verdict, so a weak baseline would pass without anyone noticing it was never graded.",
    lambda t: mutate(
        t, "**Usable.** Geography, band, type, size and window match",
        "Geography, band, type, size and window match",
        "SET-INTEGRITY"),
)

fixture(
    "08--prescription-midsentence.md", "NO-RX",
    "A recommended action is buried mid-paragraph in the missing-evidence section, "
    "far from the start of any line, in the hedged form rules.md names explicitly.",
    lambda t: mutate(
        t,
        "Neither is load-bearing for the Stage 4 finding,",
        "Since four of the eight comps carry one, you may want to add a floor plan "
        "before anything else. Neither is load-bearing for the Stage 4 finding,",
        "NO-RX"),
)

fixture(
    "09--no-confidence-level.md", "CONFIDENCE",
    "The confidence section reads as confident prose mid-paragraph but never states one "
    "of the three permitted levels, so nothing binds the cap.",
    lambda t: mutate(
        t, "**Supported.** The comparison set is Usable,",
        "This finding rests on a strong evidentiary base. The comparison set is Usable,",
        "CONFIDENCE"),
)


def main():
    case = CASE.read_text(encoding="utf-8").strip()
    expectations = {
        "_note": (
            "Each fixture is the clean control with exactly one planted defect. "
            "The named gate must be among the gates that reject it. Regenerate with "
            "python3 tests/negative/build-fixtures.py"
        )
    }

    (HERE / "00--clean-control.md").write_text(
        HEADER.format(
            title="clean control",
            defect="none. This one must pass every gate; a checker that only ever "
                   "rejects proves as little as one that only ever accepts.",
            gate="(none — positive control)",
            case=case,
            body=CLEAN,
        ),
        encoding="utf-8",
    )
    print("wrote 00--clean-control.md")

    for name, gate, defect, fn in FIXTURES:
        body = fn(CLEAN)
        if body == CLEAN:
            raise SystemExit("fixture builder: %s applied no mutation" % name)
        (HERE / name).write_text(
            HEADER.format(
                title=name.replace(".md", "").replace("--", " — ").replace("-", " "),
                defect=defect,
                gate=gate,
                case=case,
                body=body,
            ),
            encoding="utf-8",
        )
        expectations[name] = {"must_fail_gate": gate, "defect": defect}
        print("wrote %s  (%s)" % (name, gate))

    (HERE / "expectations.json").write_text(
        json.dumps(expectations, indent=2) + "\n", encoding="utf-8")
    print("wrote expectations.json")


if __name__ == "__main__":
    main()
