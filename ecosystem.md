# Ecosystem Notes

This library is a standalone, machine-readable pattern dataset for AI slop.

It does not index or endorse third-party GitHub repositories. Pattern data in `data/` is the source of truth; `research.md` and `reference/writing.md` provide context.

## Detector tooling field notes (2026-11)

Operational notes from an a controlled two-instrument validation campaign (two commercial detectors, November 5-11, 2026). Retained as a distilled log; no internal document paths are published.

- **a commercial detector** (a detector site): free credits arrive in batches. Observed: initial 16, then +4 mid-session, then +20 after a multi-day gap; the grant schedule is unknown, so size validation queues to 20 credits or less and reserve about 8 for a fresh human-wire control. Cost is 1 credit per 100 words rounded up. The sidebar credit counter rendered stale values mid-session; trust the main panel's "You've run out of credits" message. The free checker returns a confidence label plus AI/assisted/human percentages and names its model (4.1 in this campaign).
- **a commercial detector** (a detector site): roughly four no-login scans per session before a "Sign up to Continue" wall; signup consents to marketing email, so consent is required before creating an account. A "10,000 credits left this month" panel displays even for anonymous sessions but did not govern the wall. The displayed model version varies per scan (5.0b and 3.3b observed), so treat cross-scan deltas with caution. Its "most AI sentences" list is a free, high-value localizer: it named the exact flat spec-sheet run inside the test text while leaving the lede and quotes unflagged, which is how the spec-sheet structure pattern was found.

## Where this library fits

The library is the pattern-data layer: `data/*.json` is the shared substrate a linter, skill, or detector can load, with research and reference documentation alongside. It is intentionally self-contained and does not maintain a directory of other projects.
