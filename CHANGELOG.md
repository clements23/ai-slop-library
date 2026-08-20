# Changelog

All notable changes to this project are documented here. The version is kept in sync with the `VERSION` file and the Git tag.

## [1.6.0] - 2026-08-20

Litotes detection layer + anti-slop research for Founder's Voice. Patterns identified from live TAIS draft audits, LinkedIn's 2026 AI slop crackdown, and research across Forbes, Foundera, SlopDetector, aicheckr.io, and AI Publisher's 2026 detection framework. The user directive "do not do litotes" drove the core addition; the broader research enhanced the writing system with measurable anti-slop techniques for founder-voice content.

### Added

- `data/slop-structures.json`: four new structures - "Litotes (negation hedging)" (high, negation-hedging family), "Hedging qualifier chains" (high, hedging-stack family), "Restating the question as the answer" (high, empty-answer family), "Listicle filler" (high, empty-list family). 29 to 33 structures.
- `data/slop-phrases.json`: 17 new phrases across three families:
  - Litotes (10 phrases): "not uncommon", "not insignificant", "not without merit", "far from trivial", "far from simple", "by no means", "not unlike", "not entirely wrong", "none too", "not a small feat"
  - Hedging-stack (3 phrases): "might potentially possibly" (critical), "could potentially help in certain contexts", "results may vary depending on"
  - Throat-clearing (2 phrases): "It's no secret that", "There's no denying that"
  - Faux-insight (2 phrases): "Here's what [source] missed", "The real question is"
  74 to 91 phrases.
- `reference/writing.md`: new "Defeating AI slop: what the research shows" section covering: the specificity principle, the deletion test, founder-voice anti-slop (six measurable dimensions from Foundera), the voice-preservation workflow, LinkedIn's algorithmic enforcement, and Google's E-E-A-T rewards for human specificity. Also added patterns 7-9 (litotes, hedging qualifier chains, restating the question as the answer) to the "patterns that matter most" section.
- `research.md`: new "Platform enforcement and brand strategy (2026)" section with six new sources: LinkedIn's AI slop crackdown, Forbes/Gallo on lived-experience storytelling, Foundera on voice flattening and the six dimensions of founder voice, Digital Assassin on AI-as-editor strategy, SlopDetector's twelve measurable thresholds, AI Publisher's three-tier detection framework, and aicheckr.io's twelve before-and-after fixes.
- `ecosystem.md`: new "Humanizers and voice tools" section (Foundera, The Founder Voice, sergebulaev/linkedin-skills) and new "Web-based slop checkers" section (SlopDetector, aicheckr.io).

### Rationale

The user's directive "do not do litotes" identified a gap: the library documented binary contrast ("X is not Y") but missed litotes, a distinct negation-hedging pattern where AI understates through double negatives ("not uncommon", "not insignificant") to sound measured while committing to nothing. The broader research into how brands and founders defeat AI slop in 2026 revealed that the most effective anti-slop techniques are not stylistic but structural: specificity (concrete numbers, names, dates), substance (the deletion test), and voice preservation (the six measurable dimensions). LinkedIn's algorithmic enforcement makes this a distribution advantage, not just an editorial one.

## [1.3.0] - 2026-08-15

Founder-voice + publication-plug detection layer. Patterns identified in a live audit of the TAIS SpaceX-Cursor acquisition LinkedIn Founder's Voice draft (2026-08-15). The audit found that the draft was strong in substance and narrative but needed refinement in cadence, authority framing, and the transactional closer. These additions encode the lessons so the linter catches them on the next run.

### Added

- `data/slop-phrases.json`: three new phrases - "Full article only on *" (high), "We do the reading" (high), "You get the decision" (high). New family `publication-plug`. The three lines of the transactional LinkedIn closer are now flagged independently so line breaks do not defeat detection. 71 to 74 phrases.
- `data/slop-structures.json`: "Single-sentence-per-line fragmentation" (medium). New family `formatting-fragmentation`. The LinkedIn-bro formatting trap where every sentence is its own paragraph. Detection requires a paragraph-to-sentence ratio check, documented as the tell. 28 to 29 structures.

### Changed

- `reference/writing.md`: new section on founder-voice cadence and the publication-plug closer, drawing directly from the live audit. Explains why every-line-its-own-paragraph reads as template output, and why a transactional closer ("Full article only on X. We do the reading. You get the decision.") reads as a value-extraction pitch rather than domain authority. Prescribes the softer closer pattern (link to comments, woven authority reference) used in the corrected draft.

### Rationale

The audited Founder's Voice draft was strong on insight (the all-stock dilution math, the interface-plus-compute merger framing, the rented-brainpower thesis) but the surface failed three founder-voice tests: it read as a tech-journalist news recap rather than executive opinion; every sentence was its own line (the LinkedIn formatting trap); and it closed with a transactional publication plug. A seasoned founder voice groups sentences into mini-paragraphs with varied cadence, frames the takeaway as a call to think or act, and ends on the reader's takeaway rather than a branded promise. The library now encodes both the cadence tell and the closer tell.

## [1.2.2] - 2026-08-15

### Changed

- `data/*.json`, `data/schema.json`: embedded per-file copyright notices removed. Standard open-source practice, matching other pattern libraries (LICENSE at repo root only).
- `LICENSE`: copyright holder corrected to Clements Emerson Dewanto.
- `README.md`, `CONTRIBUTING.md`: license sections updated with the corrected name; branding paragraph dropped.

## [1.2.1] - 2026-08-15


### Changed

- `LICENSE`: back to MIT (Copyright (c) 2026 Clements Emerson). The library is open source.
- `data/*.json`: embedded notices updated to "AI Slop Library - (c) 2026 Clements Emerson. MIT License." - the name stays with the data no matter how it is copied.
- `README.md`: "License and trademark" section now states MIT and that everything in the repository is AI Slop Library.
- `CONTRIBUTING.md`: Ownership section reworded for MIT.
- `data/schema.json`: copyright property description updated.

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
