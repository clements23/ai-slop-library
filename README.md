# AI Slop Library

A machine-readable library of AI slop patterns: the words, phrases, sentence openers, structural tells, and punctuation tics that mark text as machine-generated - with examples and fixes for each.

**Current stable version: v1.0.0** (see [releases](https://github.com/clements23/ai-slop-library/releases) and [CHANGELOG.md](CHANGELOG.md))

The data layer is plain JSON. Any linter, agent skill, or detector can load it. The reference layer explains the tells. The research layer cites the evidence.

## What's inside

```
data/
  schema.json           JSON schema for all data files
  slop-words.json       95 overused words, severity-rated
  slop-phrases.json     71 multi-word constructions with examples and fixes
  slop-openers.json     83 sentence openers with fixes
  slop-structures.json  28 rhetorical shapes (binary contrast, rule of three, ...)
  slop-punctuation.json punctuation and formatting tics (em dash, colons, ...)
  claude-watermarks.json  the Claude detection layer: technical watermark + 7 fingerprint patterns
  gpt-watermarks.json     the GPT detection layer: 12 assistant-register fingerprint patterns
scripts/
  slopcheck.py          zero-dependency CLI linter (Python 3 stdlib only)
examples/
  sloppy.txt            a text packed with tells (fixture for testing)
  clean.txt             the same content de-slopped (fixture for testing)
reference/
  writing.md           the human-readable guide to writing slop
  visual.md            the visual/design tells (purple gradients, blob heroes, ...)
  code.md              the code tells (empty functions, fake docs, ...)
research.md            the evidence base (Nature, Science Advances, arXiv, ...)
ecosystem.md           curated index of the AI-slop ecosystem (40+ repos/tools)
```

## Quick start

```sh
git clone https://github.com/clements23/ai-slop-library
cd ai-slop-library

# scan a file
python3 scripts/slopcheck.py draft.txt

# scan with a severity floor, or machine-readable output
python3 scripts/slopcheck.py --severity high draft.txt
python3 scripts/slopcheck.py --json draft.txt

# scan stdin
cat draft.txt | python3 scripts/slopcheck.py -
```

Exit code 1 means tells found, 0 means clean - usable in pre-commit hooks and CI. See `python3 scripts/slopcheck.py --help`.

Every entry carries a `severity` field (`critical` / `high` / `medium` / `low`) so tools can decide whether to warn or block. Phrase entries carry a `family` field (binary-contrast, throat-clearing, weasel-attribution, etc.) so tools can group and explain hits.

```json
{
  "phrase": "It's not X. It's Y.",
  "example": "It's not about the tool. It's about the system.",
  "fix": "State Y alone, or name the actor.",
  "severity": "critical",
  "family": "binary-contrast"
}
```

## The five tells that matter most

1. **Binary contrast** - "It's not X. It's Y." The most documented single construction in detection research.
2. **Throat-clearing openers** - "In today's fast-paced world..." The first two sentences carry no information.
3. **Fake-profound endings** - "The future isn't coming. It's already here."
4. **Weasel attribution** - "Experts agree", "Studies show" with no source.
5. **Synonym cycling** - Renaming the same thing at every appearance to dodge repetition.

Full explainers in `reference/writing.md`.

## Evidence

The tells are measured, not vibes: "realm", "intricate", "showcasing", "pivotal" were flat for a decade then surged post-2023 (Nature Human Behaviour 2025); "delve" rose ~1,500% in biomedical abstracts (Science Advances 2025); EQ-Bench scores models on slop constructions. Citations in `research.md`.

## Claude watermark layer

`data/claude-watermarks.json` documents both layers of Claude detection: the invisible technical watermark Anthropic embeds in Claude output (confirmed in Anthropic's support documentation), and the seven writing-fingerprint patterns detectors are calibrated to find: first-person avoidance, systematic scope acknowledgement, balanced counterargument inclusion, triadic list compulsion, conclusion recycling, paragraph architecture regularity, and the Claude vocabulary cluster. De-slopping the fingerprint does not remove the technical watermark; the layers are independent.

## How to use it

- **Linters / CI**: load `data/*.json`, build a flag list from `severity >= "high"`, scan text, suggest the `fix`. `scripts/slopcheck.py` is the reference implementation.
- **Agent skills**: point a de-slop skill at `data/slop-phrases.json` + `data/slop-structures.json` for its pattern list.
- **Detectors**: combine word and structure frequencies as features (with the caveat that detectors false-positive on human text - use as lint, not accusation).
- **Writers**: read `reference/writing.md`, then run your own text against the data with `scripts/slopcheck.py`.

## Model fingerprints

Beyond the general layers, the library documents the detectable registers of specific model families:

- `data/claude-watermarks.json` - the invisible technical watermark Anthropic embeds in Claude output (confirmed, not removable by rewriting) plus seven fingerprint patterns: first-person avoidance, scope acknowledgement, balanced counterarguments, triadic lists, conclusion recycling, paragraph regularity, vocabulary cluster.
- `data/gpt-watermarks.json` - the GPT assistant register: identity leaks ("As an AI language model"), compliance openers, service closers, possibility-hedge stacks, listicle defaults, promotional vocabulary cluster.

Fingerprints are statistical: the cluster is the signal, not single instances.

## Related

The ecosystem of skills, lists, detectors, and CI tools already out there is indexed in `ecosystem.md`. This library is the pattern-data layer underneath all of them: structured, standalone, machine-readable.

## License

MIT
