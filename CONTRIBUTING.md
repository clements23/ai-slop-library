# Contributing

The library is pattern data plus the tooling that consumes it. Contributions that add patterns, improve fixes, or extend the tooling are welcome.

## Ownership

The library is open source under the MIT License, Copyright (c) 2026 Clements Emerson Dewanto.

## Adding a pattern

1. **Diff before you add.** Search every existing `data/*.json` file for the string *and* for the concept. Many proposed patterns are renames of entries already present: "Not X, but Y" is the binary-contrast family, "broetry" is the single-sentence-per-line fragmentation structure, "As an AI language model" is the GPT assistant-identity layer. An entry that restates an existing pattern under a new name is rejected; an entry that names a genuinely distinct construction, fix, or failure mode is accepted.
2. Pick the right data file: `slop-words.json` for single words, `slop-phrases.json` for multi-word constructions, `slop-openers.json` for sentence-initial tells, `slop-structures.json` for rhetorical shapes, `slop-punctuation.json` for punctuation and formatting tics, model files (`claude-watermarks.json`, `gpt-watermarks.json`) for model-specific fingerprints.
3. Every entry must carry `severity` from the fixed set: `critical`, `high`, `medium`, `low`. Calibrate against the severity guide in `reference/writing.md`: critical is spotted instantly by readers, high is consciously recognized as AI-flavored, medium is a stylistic tic, low is a mild marker that tells in clusters.
4. Every entry needs a concrete `fix`. A pattern without a fix is not useful to the people who find their own text flagged. The fix should state the human replacement, not just "avoid this".
5. Provide an example of the tell where the format supports it.
6. Use an existing `family` when one fits. New families are load-bearing: they need either multiple entries or a failure mode distinct enough that tools must explain it differently, and they must be documented in `reference/writing.md` or `research.md`.
7. Do not add a word or phrase merely because you dislike it. The library is grounded in measured over-representation in LLM output, not taste. If a pattern has no published or corpus evidence, say so in the `note` field and mark it `low`.
8. Duplicates are rejected: the CI and the local validator fail on duplicate names within a file.

## Harvesting from other lists

Popular community lists (hardikpandya/stop-slop, FeedHive/ai-slop-detector, petergyang/no-ai-slop, Wikipedia's Signs of AI writing) are indexed in `ecosystem.md`. Harvesting from them is encouraged, with the same rule as everywhere else: diff first, take the concept, write the entry in this library's format with its own example and fix, and cite the source in `research.md`. Do not copy another repository's list verbatim.

## Updating the ecosystem index

`ecosystem.md` tracks the surrounding repos and tools. When adding or refreshing an entry:

- Take star counts from the GitHub API (`api.github.com/repos/<owner>/<repo>`), not from memory, and note the retrieval date in the file header.
- Sort each table by stars, descending.
- New categories are welcome when a section's tools stop fitting (the August 2026 "Humanizers and voice tools" section and the October 2026 motion-slop additions both started this way).

## Adding a model fingerprint

Model fingerprints (Claude, GPT, future models) document the *detectable* register of a specific model family, separate from the general slop layers. Requirements:

- Source the patterns: detector documentation, the vendor's own statements, or published research. Cite the source in the `notes` field.
- Distinguish statistical signals from hard tells. Note where a single instance is not evidence.
- Do not copy other repositories' pattern lists verbatim. Write the entries yourself.

## Tooling

`scripts/slopcheck.py` must stay zero-dependency (Python 3 stdlib only). Tests are the CI workflow: every data file must parse, sloppy.txt must produce hits, clean.txt must stay clean.

## Validation

```sh
python3 scripts/slopcheck.py examples/sloppy.txt   # must exit 1 with hits
python3 scripts/slopcheck.py examples/clean.txt    # must exit 0, clean
```

Run both before opening a PR. When adding patterns, also verify the new strings do not fire on `examples/clean.txt` (CI fails if they do), and add the new tells to `examples/sloppy.txt` so the self-test exercises them. The CI workflow runs everything again.

## Releases

The version lives in `VERSION`, is mirrored in `README.md` and `CHANGELOG.md`, and is tagged `vX.Y.Z` with a GitHub release. Bump the minor version for new patterns or families, the patch version for fixes to existing entries.
