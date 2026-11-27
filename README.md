# AI Slop Library

[![validate](https://github.com/clements23/ai-slop-library/actions/workflows/validate.yml/badge.svg)](https://github.com/clements23/ai-slop-library/actions/workflows/validate.yml)
[![version](https://img.shields.io/badge/version-1.10.0-orange.svg)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![python](https://img.shields.io/badge/python-3.9%2B-3776AB.svg)](https://www.python.org/)

A machine-readable library of AI slop patterns: the words, phrases, sentence openers, structural tells, punctuation tics, and model fingerprints that mark text as machine-generated. Every entry ships with an example and a fix.

The data layer is plain JSON, so any linter, agent skill, or detector can load it. The reference layer explains the tells. The research layer cites the evidence. Nothing here depends on a model provider or a hosted service.

**Current stable version: v1.10.0** ([releases](https://github.com/clements23/ai-slop-library/releases) · [changelog](CHANGELOG.md))

---

## Why this exists

Bad machine-written prose is not one problem, it is a stack of small ones: a vocabulary that sounds impressive and says nothing, a rhythm that never varies, a paragraph shape repeated until it reads like a template. Word lists catch the first layer. They miss the rest.

This library treats slop as data. It separates the layers, rates each pattern by severity, and pairs every entry with the sentence that fixes it. The goal is not to accuse an author. The goal is to make a draft measurably cleaner before a reader sees it.

## Quick start

```sh
git clone https://github.com/clements23/ai-slop-library
cd ai-slop-library
```

Scan a draft for known constructions:

```sh
python3 scripts/slopcheck.py draft.txt
```

Raise the severity floor, or emit machine-readable output:

```sh
python3 scripts/slopcheck.py -s high draft.txt
python3 scripts/slopcheck.py --json draft.txt
```

Scan standard input:

```sh
cat draft.txt | python3 scripts/slopcheck.py -
```

Run the second gate, which measures rhythm and the medium-floor patterns:

```sh
python3 scripts/detectorcheck.py draft.txt
python3 scripts/detectorcheck.py --strict draft.txt
```

Both scripts are zero-dependency Python 3 and exit non-zero on a finding, so they drop into a pre-commit hook or CI step without a package install.

```yaml
# .github/workflows/prose.yml
- run: python3 scripts/slopcheck.py -s high draft.txt
- run: python3 scripts/detectorcheck.py --strict draft.txt
```

## What it looks like

```text
== draft.txt ==
  [critical] Binary contrast (contracted) x2 (structures)
      fix: State Y alone.
  [high] Negation tail (", not X") x3 (structures)
      fix: Cut the negation tail: "Routing is now a monthly operating cost."
```

```text
== draft.txt ==
  metrics: 742 words, 44 sentences, mean 15.1, max 35, burstiness 0.47,
           long 2, paragraphs 13 (burstiness 0.26), contractions 7.4/1k
  WARN: mean sentence length 15.1 below 18.0
  WARN: paragraph burstiness 0.26 below 0.45
```

## What's inside

```text
data/
  schema.json              JSON schema for every data file
  slop-words.json          116 overused words, severity-rated
  slop-phrases.json        146 multi-word constructions with examples and fixes
  slop-openers.json        92 empty sentence openers with fixes
  slop-structures.json     48 rhetorical shapes (binary contrast, metronome, ...)
  slop-punctuation.json    23 punctuation and formatting tics
  claude-watermarks.json   8 fingerprint patterns for the Claude register
  gpt-watermarks.json      12 fingerprint patterns for the GPT register
scripts/
  slopcheck.py             construction linter (zero dependencies)
  detectorcheck.py         rhythm gate (burstiness, paragraph shape, contractions)
reference/
  writing.md               the full guide to prose tells and fixes
  visual.md                visual and design tells
  code.md                  code and comment tells
examples/
  sloppy.txt               a text packed with tells (test fixture)
  clean.txt                the same content de-slopped (test fixture)
research.md                the evidence base (Nature, Science Advances, arXiv, ...)
ecosystem.md               detector tooling notes, kept generic
CHANGELOG.md               release history
```

## Coverage at a glance

| Layer | File | Entries |
|---|---|---:|
| Words | `slop-words.json` | 116 |
| Phrases | `slop-phrases.json` | 146 |
| Openers | `slop-openers.json` | 92 |
| Structures | `slop-structures.json` | 48 |
| Punctuation and formatting | `slop-punctuation.json` | 23 |
| Claude fingerprints | `claude-watermarks.json` | 8 |
| GPT fingerprints | `gpt-watermarks.json` | 12 |

The phrase layer spans 26 families, including binary contrast, throat-clearing, weasel attribution, sycophancy, social formula, hollow promise, portable platitude, meta-commentary, chatbot residue, claudism, and marketing template. The structure layer spans 17 families, including spec-sheet, sentence band, paragraph band, register, false agency, seamslop, and verb inflation.

## Two gates, not one

Most de-slop passes stop at the construction layer. That is the first gate.

| Gate | Script | What it answers |
|---|---|---|
| Constructions | `slopcheck.py` | Does this text contain a known slop pattern? |
| Rhythm | `detectorcheck.py` | Did the rewrite change the cadence a reader and a detector still notice? |

The second gate exists because a draft can clear every high and critical tell and keep the exact same sentence rhythm. It measures:

- **Sentence burstiness**, the standard deviation of sentence lengths divided by their mean.
- **Mean and maximum sentence length.**
- **Long-sentence density**, the number of sentences at 30 words or more.
- **Paragraph burstiness**, the same ratio at paragraph scale.
- **Contraction density** per 1,000 words.
- **Medium-floor patterns**, the layer that includes spec-sheet, sentence band, paragraph band, and register.

A failure means the prose is still too even. A warning points at the next thing to break. `--strict` turns warnings into failures for teams that want a hard gate.

Neither gate is a promise about any third-party detector, including this library's own evidence. Treat both as diagnostics: measure, rewrite the sentence that caused the number, then measure again.

## Data format

Every entry carries a severity so a tool can decide whether to warn or block.

```json
{
  "phrase": "It's not X. It's Y.",
  "example": "It's not about the tool. It's about the system.",
  "fix": "State Y alone, or name the actor.",
  "severity": "critical",
  "family": "binary-contrast"
}
```

- `severity`: `critical`, `high`, `medium`, or `low`.
- `family`: a grouping key for tools that want to explain a cluster rather than a single hit.
- `fix`: the rewrite to suggest, not just a flag to raise.

The schema is in `data/schema.json`. The CI workflow validates every file on push.

## The patterns that matter most

1. **Binary contrast.** "It's not X. It's Y." The most documented construction in the detection literature. Four banned faces: contracted, declarative, concession, and negation tail.
2. **Trailing appended insight.** "X, Y, and Z, and [the real point]." The thesis arrives late, in a trailing clause.
3. **Throat-clearing openers.** "In today's fast-paced world..." The first two sentences carry no information.
4. **Fake-profound endings.** "The future isn't coming. It's already here."
5. **Weasel attribution.** "Experts agree" or "Studies show" with no named source.
6. **Synonym cycling.** Renaming the same thing on every appearance to dodge repetition.

Full explainers for these and the rest are in [`reference/writing.md`](reference/writing.md).

## Evidence

The tells are measured, not vibes. Overused vocabulary stayed flat for a decade and then surged after 2023 (Nature Human Behaviour, 2025). "Delve" rose roughly 1,500 percent in biomedical abstracts (Science Advances, 2025). Nine frontier models use measurably harder-to-process constructions than human writers, with density over clarity as the hypothesized cause (arXiv:2610.29162, 2026). A controlled validation campaign produced the rhythm thresholds used by the second gate. Citations and caveats are in [`research.md`](research.md).

## Model fingerprints

Beyond the general layers, the library documents the detectable registers of specific model families:

- **Claude layer.** `data/claude-watermarks.json` holds the invisible technical watermark plus eight writing-fingerprint patterns: first-person avoidance, systematic scope acknowledgement, balanced counterargument inclusion, triadic list compulsion, conclusion recycling, paragraph architecture regularity, the vocabulary cluster, and the turn-of-phrase register.
- **GPT layer.** `data/gpt-watermarks.json` holds the assistant register: identity leaks, compliance openers, service closers, possibility-hedge stacks, listicle defaults, and the promotional vocabulary cluster.

Fingerprints are statistical. The cluster is the signal, not a single instance.

## Using the data

- **Linters and CI.** Load `data/*.json`, build a flag list from `severity >= "high"`, scan text, and suggest the `fix`. `scripts/slopcheck.py` is the reference implementation.
- **Rhythm checks.** Use `scripts/detectorcheck.py` for the second gate. It runs the same data at the medium floor and measures burstiness, paragraph shape, and contraction density.
- **Agent skills.** Point a de-slop skill at `slop-phrases.json` and `slop-structures.json` for its pattern list. The raw JSON is fetchable from `raw.githubusercontent.com` at any tag.
- **Classifiers.** Combine word and structure frequencies as features, with the caveat that any classifier false-positives on human text. Use it as a lint, not an accusation.
- **Writers and editors.** Read `reference/writing.md`, then run a draft through both scripts before publishing.

## Contributing

Contributions are welcome. A good pull request adds a pattern that is not a rename of an existing one, includes a real example and a usable fix, and keeps the data valid.

```sh
# validate every data file
python3 - <<'PY'
import glob, json
for path in sorted(glob.glob("data/*.json")):
    json.load(open(path))
    print(path, "ok")
PY

# confirm the examples still behave
python3 scripts/slopcheck.py examples/sloppy.txt
python3 scripts/slopcheck.py examples/clean.txt
```

When you add entries, update the counts in this README, add a CHANGELOG entry, and bump `VERSION` when the change ships. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

## License

MIT License. Copyright (c) 2026 Clements Emerson Dewanto. Use, copy, modify, merge, publish, distribute, sublicense, and sell freely, with the copyright and permission notice included in all copies or substantial portions. See [LICENSE](LICENSE).
