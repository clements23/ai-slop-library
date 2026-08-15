# Contributing

The library is pattern data plus the tooling that consumes it. Contributions that add patterns, improve fixes, or extend the tooling are welcome.

## Ownership

The library is open source under the MIT License, Copyright (c) 2026 Clements Emerson Dewanto.

## Adding a pattern

1. Pick the right data file: `slop-words.json` for single words, `slop-phrases.json` for multi-word constructions, `slop-openers.json` for sentence-initial tells, `slop-structures.json` for rhetorical shapes, `slop-punctuation.json` for punctuation, model files (`claude-watermarks.json`, `gpt-watermarks.json`) for model-specific fingerprints.
2. Every entry must carry `severity` from the fixed set: `critical`, `high`, `medium`, `low`.
3. Every entry needs a concrete `fix`. A pattern without a fix is not useful to the people who find their own text flagged.
4. Provide an example of the tell where the format supports it.
5. Do not add a word or phrase merely because you dislike it. The library is grounded in measured over-representation in LLM output, not taste. If a pattern has no published or corpus evidence, say so in the `note` field and mark it `low`.
6. Duplicates are rejected: the CI and the local validator fail on duplicate names within a file.

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

Run both before opening a PR. The CI workflow runs them again.
