# Regression tests

Each case folder holds an `inputs.md` you paste into a project running this folder, and
an `expected.md` listing the **minimum assertions** the output must satisfy.

Assertions, not expected prose. Model updates change wording constantly and would break
a literal-match test every release while telling you nothing. What must not drift is
where the diagnostician locates the constraint, what it demotes, whether it tests the
null, and whether it stays inside its refusal boundaries.

## Running one

1. Open a Claude Project with this diagnostician's folder loaded.
2. Paste the contents of `inputs.md`.
3. Say: `Diagnose this listing.`
4. Check the output against every assertion in `expected.md`.

A test fails if any assertion fails. Record which one, since that identifies the file
that drifted.

## The cases

| Case | Tests | The failure it guards against |
|---|---|---|
| [case-01-search-threshold](case-01-search-threshold/) | Stage 1 break, threshold mechanism, downstream stages declared uninformative | Diagnosing photos or condition when nobody reached them |
| [case-02-expectation-mismatch](case-02-expectation-mismatch/) | Stage 4 break, qualifying reduction read as negative evidence, mechanism separated from cause | Naming price because it is the reflex answer |
| [case-03-null-slowdown](case-03-null-slowdown/) | Null accepted, non-qualifying reduction reported as uninformative, no recommendation issued | Manufacturing a cause when none is demonstrated |

## Boundary assertions that apply to every case

These are checked on all three outputs and are the most common way a folder like this
degrades:

- No specific price, reduction amount, or percentage appears anywhere
- No rewritten listing copy, headline, or photo shot list
- No recommended action, including hedged forms such as "consider" or "you may want to"
- No ranked list of improvements
- No statement about the seller's motivation or reasonableness
- Report uses the exact headings from the output contract in `rules.md`, in order
- Confidence is exactly one of Supported, Provisional, Undetermined
