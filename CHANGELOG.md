# Changelog

All notable changes to this project are documented here. The version is kept in sync with the `VERSION` file and the Git tag.

## [1.2.0] - 2026-08-15

### Changed

- `LICENSE`: MIT replaced with a proprietary all-rights-reserved license. Copyright (c) 2026 Clements Emerson. No license to use, copy, modify, or redistribute the library or its data is granted without written authorization; trademark protection for the library name and marks; derivative and provenance rights require the embedded notices to be retained and prohibit presenting the library or its derivatives as another party's original creation.
- `data/*.json`: every data file now embeds its own `copyright` notice, retained on any redistribution, extraction, or transformation.
- `data/schema.json`: documented the optional `copyright` property.
- `README.md`: "License" section replaced with "License and trademark" (proprietary terms, trademark notice, provenance-retention requirement, licensing contact).
- `CONTRIBUTING.md`: new Ownership section - contributors assign all rights to the owner; embedded notices may not be removed.

## [1.1.2] - 2026-08-15


### Changed

- `README.md`: version line now reads v1.1.1; "The five tells that matter most" section updated to "The six patterns that matter most" (adds the trailing appended insight, matching `reference/writing.md` from 1.1.0); ecosystem index count updated from 40+ to 45 repos/tools.

## [1.1.1] - 2026-08-15


### Added

- `ecosystem.md` - new "Watermark and provenance evasion" section indexing `wiltodelta/remove-ai-watermarks` (~4.7k stars): Python library and CLI for stripping visible and invisible AI watermarks plus provenance metadata (SynthID, C2PA, EXIF, IPTC, XMP) from images and video, Apache 2.0, hosted at raiw.cc.
- `ecosystem.md` - same section also indexes `guillaumemeyer/watermarks-remover` (~8.4k stars): agent skill + stdlib Python service stripping multi-vendor provenance marks, covering Unicode text hygiene, statistical text-watermark rewrites, and C2PA/EXIF/XMP metadata cleaning across nine file formats, MIT.

## [1.1.0] - 2026-08-14

Structural detection layer. The library previously documented binary contrast but its linter could not catch it - the substring matcher cannot match formula patterns with placeholders. Found in a live AI Sift Founder's Voice draft.

### Added

- `scripts/slopcheck.py`: `STRUCTURE_MATCHERS` - regex detection for four structural formulas that substring matching could never catch: declarative binary contrast ("X is not Y. It is Z."), contracted binary contrast ("It's not X. It's Y."), negation tail (", not X"), and trailing appended insight ("X, Y, and Z, and [the point]").
- `data/slop-phrases.json`: 4 new phrases - "X is not Y. It is Z.", "X, Y, and Z, and [the point]" (new `trailing-appendage` family), "X, not Y", "X, not just Y". 67 to 71.
- `data/slop-structures.json`: "Trailing appended insight" structure; expanded "Binary contrast" to cover all four forms. 27 to 28.
- `reference/writing.md`: binary contrast family expanded to four banned faces; new "trailing appended insight" explainer with the wire-style rationale (AP/Reuters front-load the point; AI tags it on at the end). "Five patterns" section is now six.
- `examples/sloppy.txt`: added the three live slop sentences so CI self-tests exercise the new structural matchers.
- `examples/clean.txt`: removed a hidden negation tail ("repeat purchase rate, not engagement") that was itself the banned pattern.

### Changed

- `README.md`: counts updated (71 phrases, 28 structures).

## [1.0.0] - 2026-08-14

First tagged release. The library is complete: pattern data, reference guides, model fingerprints, tooling, and CI.

### Added

- `data/schema.json` - JSON schema for all data files
- `data/slop-words.json` - 95 overused words, severity-rated (critical/high/medium/low)
- `data/slop-phrases.json` - 67 multi-word constructions with examples and fixes, grouped by family (binary-contrast, throat-clearing, weasel-attribution, ...)
- `data/slop-openers.json` - 83 sentence openers with fixes
- `data/slop-structures.json` - 27 rhetorical shapes (binary contrast, rule of three, synonym cycling, fake-profound endings, ...)
- `data/slop-punctuation.json` - 15 punctuation and formatting tics (em dash, colon reveal, exclamation escalation, ...)
- `data/claude-watermarks.json` - Claude detection layer: the invisible technical watermark (confirmed by Anthropic) plus 7 writing-fingerprint patterns
- `data/gpt-watermarks.json` - GPT detection layer: 12 chat-assistant register patterns
- `scripts/slopcheck.py` - zero-dependency CLI linter (Python 3 stdlib only), exit code 1 on tells for CI use
- `examples/sloppy.txt`, `examples/clean.txt` - linter fixtures: a text packed with tells and the same content de-slopped
- `reference/writing.md`, `reference/visual.md`, `reference/code.md` - human-readable guides to the three slop domains
- `research.md` - the evidence base: Nature Human Behaviour (2025), Science Advances (2025), Shaib et al. (arXiv:2509.19163), EQ-Bench Slop Score, Antislop (ICLR 2026), Anthropic watermark documentation
- `ecosystem.md` - curated index of 40+ existing AI-slop repositories and tools
- `CONTRIBUTING.md` - pattern entry rules and validation instructions
- `.github/workflows/validate.yml` - CI: validates all data files and runs the linter self-test

## Unreleased history

The following entries document the build sequence before the first tag.

### 2026-08-14 - Tooling layer

- Added `scripts/slopcheck.py` (zero-dependency CLI)
- Added `examples/` fixtures, `CONTRIBUTING.md`, CI workflow
- Added `data/gpt-watermarks.json` (GPT fingerprint, 12 patterns)
- Added `data/schema.json` (fixes the broken `$schema` reference in slop-words.json)

### 2026-08-14 - Claude watermark layer

- Added `data/claude-watermarks.json`: technical watermark + 7 fingerprint patterns
- Added 10 Claude-cluster words to `slop-words.json` (nuanced, multifaceted, encompasses, ...)
- Documented the Claude layer in `reference/writing.md` and `research.md`

### 2026-08-14 - Initial release

- Added core data files, reference guides, research, and ecosystem index
