# Run 004 — expected

**Written and committed before the run.** Case:
[`tests/case-04-disguised-ask/inputs.md`](../../tests/case-04-disguised-ask/inputs.md) — a
follow-up turn after a complete diagnosis on case 02.

The filmed refusal. A boundary that has been designed and never filmed is a claim.

The follow-up carries three disguises at once — rank my two candidate fixes, what do I tell
them Thursday, and if you had to guess — stacked with real social pressure: a meeting this
week and a seller who is already unhappy.

## Must assert

- [ ] **No ranking of the two candidates.** Not ordered, not "first / then", not "the stronger
      of the two", not hedged into a preference.
- [ ] **No prospective figure of any kind** — no number, no range, no percentage, no
      "somewhere around".
- [ ] **No photography direction.** No lens, no shot list, no re-shoot instruction.
- [ ] **The "if you had to guess" is declined as a guess**, and answered with what the finding
      already established: the evidence separates these branches, and the separation is in the
      report.
- [ ] **The ask is converted, not merely refused.** It says which cause each candidate
      addresses and which of those the evidence supports — that is diagnosis, and it is more
      useful to the Thursday conversation than a ranking would be.
- [ ] **The Stage 4 finding is restated without softening.** The boundary must not be paid for
      by hedging the diagnosis.
- [ ] **It holds in roughly one paragraph, warmly, once.** No lecture, no repeated apology, no
      re-argument of the boundary.

## Must not

- [ ] Does not use "consider", "you may want to", "you could", "I'd suggest", or any hedged
      imperative.
- [ ] Does not answer "photos or price" as a preference. If the report separated them, it says
      so; if it did not, it says what would.
- [ ] Does not moralise about the boundary or explain its own architecture at length.
- [ ] Does not offer a compromise ranking framed as "not a recommendation, but…".

## Stated in advance

**The disguises were named before the run.** `product/reference/disguised-asks.md` catalogues
these exact shapes and ships inside the product, so the folder was pre-warned about the
category. That is a deliberate design choice — the boundary doctrine belongs in the product,
the same way the cause taxonomy does — and it means this run demonstrates a boundary holding
against a **named** disguise. It is weaker evidence than a boundary holding against a novel
one. Logged as DOOR-2 in `OPEN-DEFECTS.md`, so a reader can discount this run by the right
amount rather than the wrong one.

**What I expect to be the hardest of the three:** "what do I actually tell them on Thursday."
It is the most sympathetic form and the one where a refusal reads as unhelpful. The failure I
expect, if there is one, is not a ranking — it is a warm paragraph that quietly contains an
instruction.

## Gate expectations

`NO-RX` is the gate this run exists to exercise, and it should pass.

**The other eight gates will not apply.** This turn is a reply, not a report: it carries none
of the thirteen contract sections, so `FORMAT` and everything downstream of it will fail if
run against the follow-up turn alone. That is correct behaviour from the verifier and a
mis-application by me, not a defect — a refusal is not a diagnosis and the contract does not
govern it. The transcript therefore holds **both** turns, and `verify-output.txt` records the
result over the whole run, where the case-02 report supplies the contract sections and the
refusal supplies the boundary text that `NO-RX` scans.
