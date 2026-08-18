#!/usr/bin/env python3
"""
Listing Stall Diagnostician — output verifier.

Checks a recorded run against the output contract in product/rules.md.

A must in a markdown file is a request. A must in code is a constraint.

What it reads
-------------
`runs/NNN-<slug>/transcript.md`, which holds the whole run: the case input as
`## Turn N - user` blocks and the diagnosis as `## Turn N - assistant` blocks.
Grounding and figure checks run the assistant text against the user text, so the
gate is pointed at a real run and at the real input that run was given.

It deliberately does NOT read product/examples.md. A verifier aimed at the worked
examples proves the brochure is self-consistent and nothing about the product.

Usage
-----
    python3 checks/verify.py                    # every run under runs/
    python3 checks/verify.py --run 001          # one run
    python3 checks/verify.py --file out.md      # a transcript anywhere on disk
    python3 checks/verify.py --selftest         # positive + negative fixtures
    python3 checks/verify.py --coverage         # write runs/gate-coverage.txt

Exit 0 pass, exit 1 fail. Every failure names the check that caught it.
Standard library only. No network. No API key. Python 3.8+.
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "runs"
RULES = ROOT / "product" / "rules.md"
NEG_DIR = ROOT / "tests" / "negative"

GREEN, RED, YELLOW, DIM, BOLD, RESET = (
    "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[1m", "\033[0m"
)
if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = BOLD = RESET = ""

# --------------------------------------------------------------------------
# The output contract, mirrored from product/rules.md
# --------------------------------------------------------------------------

SECTIONS = [
    "Failure observed",
    "Comparison set",
    "Comparison-set integrity",
    "Funnel reconstruction",
    "Primary constraint",
    "Primary cause",
    "Mechanism",
    "Evidence for this cause and against the alternatives",
    "Alternatives, and why they are demoted",
    "Null model",
    "Confidence",
    "Missing evidence",
    "What would prove this wrong",
]

CONFIDENCE_LEVELS = ("Supported", "Provisional", "Undetermined")

INTEGRITY_VERDICTS = ("not usable", "usable with limitations", "usable")

# Prescription language. Deliberately unanchored: an imperative is an imperative
# in the middle of a paragraph too, and an anchored pattern is how a checker
# reports a gate as held while the same sentence walks past it mid-line.
RX_PATTERNS = [
    r"\byou should\b",
    r"\byou (?:may|might|could) want to\b",
    r"\byou could\b",
    r"\bI (?:recommend|suggest|advise)\b",
    r"\b(?:recommend|suggest)(?:ed|ing)? (?:that |a |an )?(?:you|they|the (?:agent|seller))\b",
    r"\bmy recommendation\b",
    r"\bthe next step is\b",
    r"\bwhat I would do\b",
    r"\bconsider (?:reducing|lowering|dropping|relisting|reshooting|replacing|adding|cutting)\b",
    r"\bshould (?:reduce|lower|drop|relist|reshoot|replace|cut|consider)\b",
    r"\bwould (?:recommend|suggest|advise)\b",
    r"\brelist(?:ing)? (?:it|the (?:property|listing|home|house))\b",
    r"\breduce the (?:price|list price) (?:to|by)\b",
    r"\bre-?shoot the (?:photos|gallery)\b",
]
RX_RE = [re.compile(p, re.I) for p in RX_PATTERNS]

# Hedges that turn one primary cause into two.
MULTI_CAUSE_RE = [
    re.compile(r"\bboth\b", re.I),
    re.compile(r"\beither\b", re.I),
    re.compile(r"\bcombination of\b", re.I),
    re.compile(r"\ba mix of\b", re.I),
    re.compile(r"\bas well as\b", re.I),
    re.compile(r"\bprimary causes\b", re.I),
]

# Quoted strings this long or shorter are labels, not evidence. Documented as a
# residual in OPEN-DEFECTS.md: a fabricated four-word feedback quote is under the
# floor and this gate will not catch it.
QUOTE_MIN_CHARS = 25

# Contract vocabulary the report quotes for emphasis rather than as evidence.
CONTRACT_QUOTES = {
    "usable", "usable with limitations", "not usable",
    "supported", "provisional", "undetermined",
    "at baseline", "clearly below", "ambiguous", "below, starved", "starved",
    "uninformative", "none located", "no failure demonstrated",
    "primary constraint", "primary cause", "mechanism",
}

# Bare integers this size or smaller are exempt from the figure check: stage
# numbers, comp counts, and ratios written as "one in four" land here. Disclosed
# in OPEN-DEFECTS.md as the loose edge of COMPUTED.
SMALL_INT_EXEMPT = 20


# --------------------------------------------------------------------------
# The gate registry — every gate, the rules.md clause it enforces, and the
# literal anchor that clause must still contain.
#
# The anchors are the point. A rule can be edited out of rules.md without any
# checker noticing, which is how a build ends up with a gate enforcing a
# sentence that no longer exists. Absence makes no false claim, so it has to be
# turned into a failing line.
# --------------------------------------------------------------------------

GATES = [
    {
        "id": "FORMAT",
        "enforces": "Output contract: 13 headings, this order, no additions, no reordering",
        "anchor": "Every report uses these headings in this order. No additions, no reordering.",
    },
    {
        "id": "ONE-CAUSE",
        "enforces": "Step 6: output exactly one diagnosis; cause is one line",
        "anchor": "Output exactly one diagnosis, stated at three distinct levels",
    },
    {
        "id": "THREE-LEVEL",
        "enforces": "Step 6: constraint / cause / mechanism named and distinct",
        "anchor": "**Primary constraint** — *where* the funnel breaks",
    },
    {
        "id": "GROUNDING",
        "enforces": "Evidence discipline: quoted material is the user's, verbatim",
        "source": "product/reference/evidence-requirements.md",
        "anchor": "the text, not a summary",
    },
    {
        "id": "COMPUTED",
        "enforces": "Baselines: every figure is read from the supplied case, never produced",
        "source": "product/reference/baselines.md",
        "anchor": "Every baseline in a diagnosis is computed from that case's own",
    },
    {
        "id": "RULED-OUT",
        "enforces": "Step 6: demoted alternatives, each with its eliminating evidence",
        "anchor": "Alternatives, and why they are demoted",
    },
    {
        "id": "SET-INTEGRITY",
        "enforces": "Step 0.5: state one verdict — usable / with limitations / not usable",
        "anchor": "Then state one verdict in the report:",
    },
    {
        "id": "NO-RX",
        "enforces": "Prohibited in output: a recommended action of any kind",
        "anchor": "A recommended action of any kind, including \"consider\" and \"you may want to\"",
    },
    {
        "id": "CONFIDENCE",
        "enforces": "Confidence is one of three levels, and the falsifier is stated",
        "anchor": "**Confidence must be stated as one of:**",
    },
]

# Requirements in rules.md this verifier does NOT enforce. Listed so the coverage
# file records them as open rather than as silence.
UNCOVERED = [
    ("PROSPECTIVE-PRICE",
     "Prohibited: any prospective price, reduction amount, or percentage. Historical "
     "figures are permitted, so the line is prospective-versus-historical and not "
     "numbers-versus-no-numbers. No mechanical test separates the two.",
     "A recommended number would have to be caught by a reader, not by this file."),
    ("STARVED-STAGE",
     "Step 3: the earliest failing stage is the diagnosis site and every stage after it "
     "is uninformative. Whether the report actually respected that is a judgement about "
     "the funnel table, not a string match.",
     "Covered by the per-case answer keys in tests/, scored by hand."),
    ("QUALIFYING-REDUCTION",
     "Step 4: the four-condition test on a prior reduction.",
     "Covered by the per-case answer keys in tests/, scored by hand."),
    ("NULL-TESTED",
     "Step 5: the null must be attempted before committing. The section is checked for "
     "presence by FORMAT; whether the test was real is not machine-checkable.",
     "Covered by the per-case answer keys in tests/, scored by hand."),
]


# --------------------------------------------------------------------------
# Text handling
# --------------------------------------------------------------------------

def normalize(text):
    """Fold typography and collapse whitespace. Deliberately does not lowercase:
    a quote is supposed to be verbatim."""
    text = unicodedata.normalize("NFKC", text)
    for a, b in [
        ("‘", "'"), ("’", "'"), ("‚", "'"), ("‛", "'"),
        ("“", '"'), ("”", '"'), ("„", '"'), ("‟", '"'),
        ("–", "-"), ("—", "-"), ("−", "-"),
        (" ", " "), ("…", "..."),
    ]:
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def strip_markup(text):
    """Remove markdown emphasis so `**Usable.**` and `Usable.` compare equal."""
    return re.sub(r"[*_`]", "", text)


TURN_RE = re.compile(r"^##\s+Turn\s+(\d+)\s*[-—]\s*(user|assistant)\s*$", re.M | re.I)


def parse_transcript(path):
    """Split a transcript into user text and assistant text.

    Returns (user_text, assistant_text). Raises ValueError if the file is not a
    transcript, which is itself a finding: a run without both sides is not a run.
    """
    raw = Path(path).read_text(encoding="utf-8")
    marks = list(TURN_RE.finditer(raw))
    if not marks:
        raise ValueError(
            "no '## Turn N - user' / '## Turn N - assistant' headers found; "
            "this file is not a transcript"
        )
    user, assistant = [], []
    for i, m in enumerate(marks):
        start = m.end()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
        body = raw[start:end]
        (user if m.group(2).lower() == "user" else assistant).append(body)
    if not user:
        raise ValueError("transcript has no user turn: nothing to ground against")
    if not assistant:
        raise ValueError("transcript has no assistant turn: nothing to check")
    return "\n".join(user), "\n".join(assistant)


def sections_of(text):
    """Map heading -> body for the level-2 headings in the assistant output."""
    found = {}
    order = []
    marks = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    for i, m in enumerate(marks):
        name = strip_markup(m.group(1)).strip()
        start = m.end()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        order.append(name)
        found.setdefault(name, []).append(text[start:end])
    return found, order


QUOTE_RE = re.compile(r'"([^"\n]{3,400})"')


def quoted_spans(text):
    return [m.group(1) for m in QUOTE_RE.finditer(normalize(text))]


def strip_quoted(text):
    """Blank out quoted spans so user material does not trip the prose checks."""
    return QUOTE_RE.sub(" ", normalize(text))


NUM_RE = re.compile(r"(\$?)(\d[\d,]*(?:\.\d+)?)(%?)")


def figures(text):
    """Yield (raw, digits) for every figure that claims to have been read.

    Exempt: bare integers <= SMALL_INT_EXEMPT (stage numbers, comp counts,
    ratios) and anything written as a percentage (derived).
    """
    out = []
    for m in NUM_RE.finditer(text):
        dollar, body, pct = m.group(1), m.group(2), m.group(3)
        if pct:
            continue
        digits = body.replace(",", "")
        if not dollar and "." not in digits:
            try:
                if int(digits) <= SMALL_INT_EXEMPT:
                    continue
            except ValueError:
                pass
        out.append((m.group(0), digits))
    return out


def figure_pool(text):
    """Every digit-string present in the case input, normalized."""
    pool = set()
    for m in NUM_RE.finditer(text):
        pool.add(m.group(2).replace(",", ""))
    return pool


# --------------------------------------------------------------------------
# Result plumbing
# --------------------------------------------------------------------------

class Result:
    def __init__(self, label):
        self.label = label
        self.checks = []

    def add(self, gate, ok, detail=""):
        self.checks.append((gate, bool(ok), detail))
        return bool(ok)

    @property
    def passed(self):
        return all(ok for _, ok, _ in self.checks)

    def failed_gates(self):
        return [g for g, ok, _ in self.checks if not ok]

    def render(self):
        status = "%sPASS%s" % (GREEN, RESET) if self.passed else "%sFAIL%s" % (RED, RESET)
        print("\n%s%s%s  %s" % (BOLD, self.label, RESET, status))
        for gate, ok, detail in self.checks:
            mark = "%sok%s" % (GREEN, RESET) if ok else "%sXX%s" % (RED, RESET)
            print("  %s  %s" % (mark, gate))
            if detail and not ok:
                for line in detail.splitlines():
                    print("      %s%s%s" % (DIM, line, RESET))

    def text(self):
        lines = ["%s  %s" % (self.label, "PASS" if self.passed else "FAIL")]
        for gate, ok, detail in self.checks:
            lines.append("  %s  %s" % ("ok" if ok else "XX", gate))
            if detail and not ok:
                for d in detail.splitlines():
                    lines.append("      " + d)
        return "\n".join(lines)


# --------------------------------------------------------------------------
# The gates
# --------------------------------------------------------------------------

def check_format(r, secs, order):
    """FORMAT — the 13 contract sections, in order, exactly once."""
    contract = [s for s in order if s in SECTIONS]
    missing = [s for s in SECTIONS if s not in secs]
    dupes = sorted(s for s in SECTIONS if len(secs.get(s, [])) > 1)
    problems = []
    if missing:
        problems.append("missing: " + ", ".join(missing))
    if dupes:
        problems.append("duplicated: " + ", ".join(dupes))
    if not missing and not dupes and contract != SECTIONS:
        for got, want in zip(contract, SECTIONS):
            if got != want:
                problems.append("out of order at %r (contract expects %r)" % (got, want))
                break
    r.add("FORMAT", not problems, "\n".join(problems))


def check_one_cause(r, secs):
    """ONE-CAUSE — Step 6 names one primary, in one line."""
    bodies = secs.get("Primary cause", [])
    if not bodies:
        return r.add("ONE-CAUSE", False, "no Primary cause section (see FORMAT)")
    body = bodies[0]
    flat = normalize(strip_markup(body))
    problems = []
    bullets = re.findall(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", body, re.M)
    if len(bullets) > 1:
        problems.append("primary cause is a list of %d items, not one cause" % len(bullets))
    hedges = [rx.pattern for rx in MULTI_CAUSE_RE if rx.search(flat)]
    if hedges:
        problems.append("multi-cause hedge: " + ", ".join(hedges))
    if len(flat) > 280:
        problems.append("over length: %d chars; the cause is one line" % len(flat))
    r.add("ONE-CAUSE", not problems, "\n".join(problems))


def check_three_level(r, secs):
    """THREE-LEVEL — constraint, cause and mechanism all named and distinct."""
    problems = []
    vals = {}
    for name in ("Primary constraint", "Primary cause", "Mechanism"):
        body = secs.get(name, [""])[0]
        flat = normalize(strip_markup(body))
        vals[name] = flat
        if not flat:
            problems.append("%s is empty" % name)
    if not problems:
        if vals["Primary constraint"].lower() == vals["Primary cause"].lower():
            problems.append("constraint and cause are the same text: the levels collapsed")
        if vals["Primary cause"].lower() == vals["Mechanism"].lower():
            problems.append("cause and mechanism are the same text: the levels collapsed")
        if len(vals["Mechanism"]) < 120:
            problems.append(
                "mechanism is %d chars; it has to trace the cause to this listing's "
                "evidence, which is a paragraph" % len(vals["Mechanism"])
            )
    r.add("THREE-LEVEL", not problems, "\n".join(problems))


def check_grounding(r, user_text, assistant_text):
    """GROUNDING — every quoted span of evidence length appears in the case input."""
    haystack = normalize(user_text)
    bad = []
    for q in quoted_spans(assistant_text):
        stripped = strip_markup(q).strip().strip(".,;:")
        if len(stripped) <= QUOTE_MIN_CHARS:
            continue
        if stripped.lower() in CONTRACT_QUOTES:
            continue
        if stripped not in haystack and q not in haystack:
            bad.append('not in the case input: "%s"' % stripped[:110])
    r.add("GROUNDING", not bad, "\n".join(bad))


def check_computed(r, user_text, assistant_text):
    """COMPUTED — every figure in the diagnosis is one the case supplied."""
    pool = figure_pool(user_text)
    bad = []
    for raw, digits in figures(strip_quoted(assistant_text)):
        if digits in pool:
            continue
        if digits.rstrip("0").rstrip(".") in pool:
            continue
        bad.append("figure not in the case input: %s" % raw)
    seen, uniq = set(), []
    for b in bad:
        if b not in seen:
            seen.add(b)
            uniq.append(b)
    r.add("COMPUTED", not uniq, "\n".join(uniq[:12]))


def check_ruled_out(r, secs):
    """RULED-OUT — at least one named rival, each carrying its eliminating evidence."""
    bodies = secs.get("Alternatives, and why they are demoted", [])
    if not bodies:
        return r.add("RULED-OUT", False, "no Alternatives section (see FORMAT)")
    body = bodies[0]
    entries = list(re.finditer(r"\*\*(.+?)\*\*", body))
    problems = []
    if not entries:
        problems.append("no named rival: the section names nothing it demoted")
    for i, m in enumerate(entries):
        start = m.end()
        end = entries[i + 1].start() if i + 1 < len(entries) else len(body)
        evidence = normalize(strip_markup(body[start:end]))
        if len(evidence) < 40:
            problems.append(
                "rival %r is named with no eliminating evidence (%d chars)"
                % (strip_markup(m.group(1))[:60], len(evidence))
            )
    r.add("RULED-OUT", not problems, "\n".join(problems))


def check_set_integrity(r, secs):
    """SET-INTEGRITY — Step 0.5's verdict is stated, so a weak baseline cannot pass silently."""
    bodies = secs.get("Comparison-set integrity", [])
    if not bodies:
        return r.add("SET-INTEGRITY", False, "no Comparison-set integrity section (see FORMAT)")
    flat = normalize(strip_markup(bodies[0])).lower()
    hit = next((v for v in INTEGRITY_VERDICTS if v in flat), None)
    r.add(
        "SET-INTEGRITY", hit is not None,
        "no verdict stated; one of Usable / Usable with limitations / Not usable is required",
    )


def check_no_rx(r, assistant_text):
    """NO-RX — Step 7 stop. Prescription language outside quoted user material."""
    prose = strip_quoted(assistant_text)
    hits = []
    for rx in RX_RE:
        for m in rx.finditer(prose):
            lo = max(0, m.start() - 45)
            hits.append("%r in: ...%s..." % (m.group(0), prose[lo:m.end() + 45].strip()))
    r.add("NO-RX", not hits, "\n".join(hits[:8]))


def check_confidence(r, secs):
    """CONFIDENCE — a stated level, and the what-would-overturn-this clause."""
    problems = []
    bodies = secs.get("Confidence", [])
    if not bodies:
        problems.append("no Confidence section (see FORMAT)")
    else:
        flat = normalize(strip_markup(bodies[0]))
        hits = [lv for lv in CONFIDENCE_LEVELS if re.search(r"\b%s\b" % lv, flat, re.I)]
        if not hits:
            problems.append("no confidence level stated; one of %s is required"
                            % ", ".join(CONFIDENCE_LEVELS))
        elif len(set(hits)) > 1:
            problems.append("more than one level stated: %s" % ", ".join(sorted(set(hits))))
    overturn = secs.get("What would prove this wrong", [])
    if not overturn:
        problems.append("no What would prove this wrong section (see FORMAT)")
    elif len(normalize(strip_markup(overturn[0]))) < 40:
        problems.append("What would prove this wrong is present but empty")
    r.add("CONFIDENCE", not problems, "\n".join(problems))


def verify_transcript(path, label=None):
    r = Result(label or str(Path(path).relative_to(ROOT)))
    try:
        user_text, assistant_text = parse_transcript(path)
    except ValueError as exc:
        r.add("TRANSCRIPT", False, str(exc))
        return r
    secs, order = sections_of(assistant_text)
    check_format(r, secs, order)
    check_one_cause(r, secs)
    check_three_level(r, secs)
    check_grounding(r, user_text, assistant_text)
    check_computed(r, user_text, assistant_text)
    check_ruled_out(r, secs)
    check_set_integrity(r, secs)
    check_no_rx(r, assistant_text)
    check_confidence(r, secs)
    return r


# --------------------------------------------------------------------------
# Anchors: rules.md and this file are pinned to each other
# --------------------------------------------------------------------------

def check_anchors():
    """Every gate names a clause in the product folder. Verify each is still there.

    A gate whose rule was edited out of the product is enforcing nothing, and would
    otherwise say so to nobody.
    """
    drift = []
    cache = {}
    for g in GATES:
        rel = g.get("source", "product/rules.md")
        if rel not in cache:
            path = ROOT / rel
            cache[rel] = normalize(path.read_text(encoding="utf-8")) if path.exists() else None
        flat = cache[rel]
        if flat is None:
            drift.append((g["id"], "%s not found" % rel))
        elif normalize(g["anchor"]) not in flat:
            drift.append((g["id"], "anchor no longer in %s: %r" % (rel, g["anchor"])))
    return drift


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def selftest():
    print("%sListing Stall Diagnostician self-test%s" % (BOLD, RESET))

    drift = check_anchors()
    print("\n%sAnchors%s %s- every gate's rule is still in the product folder%s"
          % (BOLD, RESET, DIM, RESET))
    if drift:
        for gate, msg in drift:
            print("  %sXX%s  %s %s%s%s" % (RED, RESET, gate, DIM, msg, RESET))
    else:
        print("  %sok%s  %d/%d anchors present" % (GREEN, RESET, len(GATES), len(GATES)))

    exp_path = NEG_DIR / "expectations.json"
    if not exp_path.exists():
        print("\n%sno tests/negative/expectations.json%s" % (RED, RESET))
        return 1
    expectations = json.loads(exp_path.read_text(encoding="utf-8"))
    entries = [(k, v) for k, v in expectations.items() if not k.startswith("_")]

    print("\n%sPositive control%s %s- a clean run must pass every gate%s"
          % (BOLD, RESET, DIM, RESET))
    pos = NEG_DIR / "00--clean-control.md"
    pos_ok = False
    if not pos.exists():
        print("  %sXX%s  missing tests/negative/00--clean-control.md" % (RED, RESET))
    else:
        pr = verify_transcript(pos, "00--clean-control.md")
        pos_ok = pr.passed
        if pos_ok:
            print("  %sok%s  clean control passes all %d gates" % (GREEN, RESET, len(pr.checks)))
        else:
            print("  %sXX%s  clean control FAILED on: %s"
                  % (RED, RESET, ", ".join(pr.failed_gates())))
            for gate, ok, detail in pr.checks:
                if not ok:
                    print("        %s%s: %s%s" % (DIM, gate, detail.splitlines()[0] if detail else "", RESET))

    print("\n%sNegative fixtures%s %s- each planted defect must fail on its own gate%s"
          % (BOLD, RESET, DIM, RESET))
    caught = 0
    covered = set()
    for fname, exp in sorted(entries):
        path = NEG_DIR / fname
        if not path.exists():
            print("  %sXX%s  %s %s- file missing%s" % (RED, RESET, fname, DIM, RESET))
            continue
        res = verify_transcript(path, fname)
        want = exp["must_fail_gate"]
        failed = res.failed_gates()
        if res.passed:
            print("  %sXX%s  %s %s- passed, but should have failed on %s%s"
                  % (RED, RESET, fname, DIM, want, RESET))
        elif want not in failed:
            print("  %sXX%s  %s %s- failed on %s, not on %s%s"
                  % (RED, RESET, fname, DIM, ", ".join(failed), want, RESET))
        else:
            caught += 1
            covered.add(want)
            print("  %sok%s  %s %s-> caught by %s%s" % (GREEN, RESET, fname, DIM, want, RESET))
            print("        %s%s%s" % (DIM, exp["defect"], RESET))

    missing_cover = [g["id"] for g in GATES if g["id"] not in covered]

    print("\n%s%s%s" % (BOLD, "-" * 66, RESET))
    ok = (not drift) and pos_ok and caught == len(entries) and not missing_cover
    if missing_cover:
        print("%sUNCOVERED%s  no negative fixture for: %s"
              % (RED, RESET, ", ".join(missing_cover)))
    if ok:
        print("%s%sPASS%s  %d/%d planted defects rejected, %d/%d gates covered, "
              "clean control passes"
              % (GREEN, BOLD, RESET, caught, len(entries), len(covered), len(GATES)))
        return 0
    print("%s%sFAIL%s  %d/%d planted defects rejected, %d/%d gates covered"
          % (RED, BOLD, RESET, caught, len(entries), len(covered), len(GATES)))
    return 1


# --------------------------------------------------------------------------
# Coverage assertion
# --------------------------------------------------------------------------

def write_coverage(out_path=None):
    out_path = Path(out_path) if out_path else (RUNS_DIR / "gate-coverage.txt")
    expectations = {}
    exp_path = NEG_DIR / "expectations.json"
    if exp_path.exists():
        expectations = {
            v["must_fail_gate"]: k
            for k, v in json.loads(exp_path.read_text(encoding="utf-8")).items()
            if not k.startswith("_")
        }
    drift = dict(check_anchors())

    lines = []
    lines.append("GATE COVERAGE - listing-stall-diagnostician")
    lines.append("Generated by checks/verify.py --coverage. Do not hand-edit.")
    lines.append("")
    lines.append("Every enforceable requirement in product/rules.md is listed below, either")
    lines.append("against the gate that enforces it or as UNCOVERED. An UNCOVERED line is an")
    lines.append("open defect in the open, not an omission: absence makes no false claim, so")
    lines.append("the only way to see it is to write it down.")
    lines.append("")
    lines.append("%-16s %-34s %s" % ("GATE", "NEGATIVE FIXTURE", "SOURCE ANCHOR"))
    lines.append("-" * 96)
    all_ok = True
    for g in GATES:
        fixture = expectations.get(g["id"])
        anchored = g["id"] not in drift
        if not fixture or not anchored:
            all_ok = False
        lines.append("%-16s %-34s %s" % (
            g["id"],
            fixture or "*** NONE ***",
            (g.get("source", "product/rules.md") if anchored
             else "*** DRIFTED: anchor gone from " + g.get("source", "product/rules.md") + " ***"),
        ))
        lines.append("    enforces: %s" % g["enforces"])
    lines.append("")
    lines.append("UNCOVERED - requirements in rules.md with no executable gate")
    lines.append("-" * 96)
    for gid, what, why in UNCOVERED:
        lines.append("%s  UNCOVERED" % gid)
        lines.append("    %s" % what)
        lines.append("    where it is checked instead: %s" % why)
        lines.append("")
    lines.append("COVERAGE ASSERTION")
    lines.append("-" * 96)
    lines.append("Gates declared:            %d" % len(GATES))
    lines.append("Gates with a negative fixture: %d" % sum(
        1 for g in GATES if expectations.get(g["id"])))
    lines.append("Gates whose source anchor still resolves: %d" % sum(
        1 for g in GATES if g["id"] not in drift))
    lines.append("Requirements declared UNCOVERED: %d" % len(UNCOVERED))
    lines.append("")
    if all_ok:
        lines.append("Every gate has a negative fixture and every gate's rule is still present in")
        lines.append("its source file. The %d requirements above are uncovered by construction and"
                     % len(UNCOVERED))
        lines.append("are checked by hand against the answer keys in tests/.")
    else:
        lines.append("*** ASSERTION FAILED - see the *** markers above. ***")
    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print("wrote %s" % out_path.relative_to(ROOT))
    return 0 if all_ok else 1


# --------------------------------------------------------------------------
# Entry
# --------------------------------------------------------------------------

def discover_runs():
    if not RUNS_DIR.exists():
        return []
    return sorted(d for d in RUNS_DIR.iterdir()
                  if d.is_dir() and (d / "transcript.md").exists())


def main():
    ap = argparse.ArgumentParser(
        description="Verify recorded runs against the contract in product/rules.md")
    ap.add_argument("--run", help="run number or folder name, e.g. 001")
    ap.add_argument("--file", help="verify a transcript at an arbitrary path")
    ap.add_argument("--selftest", action="store_true",
                    help="assert the checker rejects known-bad runs and accepts a clean one")
    ap.add_argument("--coverage", action="store_true",
                    help="write runs/gate-coverage.txt")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.coverage:
        return write_coverage()

    if args.file:
        targets = [Path(args.file)]
    else:
        dirs = discover_runs()
        if args.run:
            dirs = [d for d in dirs if d.name.startswith(args.run)]
            if not dirs:
                print("%sno run matching %r under runs/%s" % (RED, args.run, RESET))
                return 2
        if not dirs:
            print("%sno runs found under runs/. A verifier with nothing to verify is not "
                  "a passing build.%s" % (RED, RESET))
            return 1
        targets = [d / "transcript.md" for d in dirs]

    drift = check_anchors()
    print("%sListing Stall Diagnostician%s %s- checking recorded runs against "
          "the contract in product/rules.md%s" % (BOLD, RESET, DIM, RESET))
    if drift:
        print("\n%sANCHOR DRIFT%s" % (RED, RESET))
        for gate, msg in drift:
            print("  %sXX%s  %s %s" % (RED, RESET, gate, msg))

    results = [verify_transcript(t) for t in targets]
    for r in results:
        r.render()

    failed = [r for r in results if not r.passed]
    total = sum(len(r.checks) for r in results)
    print("\n%s%s%s" % (BOLD, "-" * 66, RESET))
    if failed or drift:
        print("%s%sFAIL%s  %d/%d runs, %d checks run%s"
              % (RED, BOLD, RESET, len(failed), len(results), total,
                 ", anchor drift" if drift else ""))
        return 1
    print("%s%sPASS%s  %d/%d runs, %d checks run"
          % (GREEN, BOLD, RESET, len(results), len(results), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
