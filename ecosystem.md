# Ecosystem Notes

This library is a standalone, machine-readable pattern dataset for AI slop.

It does not index or endorse third-party GitHub repositories. Pattern data in `data/` is the source of truth; `research.md` and `reference/writing.md` provide context.

## Detector tooling field notes (2026-11)

Notes from a controlled validation campaign, kept generic because detector behavior changes and vendor terms differ.

- **Free tiers and credits.** Quotas are granted in batches and counters can render stale values. Size a validation queue to the free allowance and reserve capacity for a fresh human-written control.
- **Signup walls.** Anonymous scans are limited and can appear or disappear between visits. Do not create accounts to work around a wall; consent and terms apply.
- **Model version variance.** The displayed detector version can change between scans, so treat cross-scan deltas with caution and re-baseline after any gap.
- **Flagged-sentence diagnostics.** When a detector exposes a per-sentence breakdown, it is the most useful signal. It localizes the problem to a passage instead of the whole document.

## Where this library fits

The library is the pattern-data layer: `data/*.json` is the shared substrate a linter, skill, or detector can load, with research and reference documentation alongside. It is intentionally self-contained and does not maintain a directory of other projects.
