# The Writing Slop Reference

The human-readable guide to the machine-generated writing tells cataloged in `data/`. The machine-readable JSON in `data/` is the source of truth; this document is the explainer.

## What is writing slop?

Writing slop is text that reads as machine-generated. It is not bad writing in the traditional sense. It is statistically distinctive: a small set of overused words, a handful of favored constructions, and rhythmic habits that humans do not share. Readers have learned to spot it, and the moment they spot it, trust drops even when the substance is correct.

The core mechanism: LLMs are trained on the average of human writing, so they produce the *most probable* version of every sentence. Humans produce the *specific* version. The most probable sentence is exactly the one everyone else's AI also writes.

## The four layers of slop

| Layer | What it is | Where it lives |
|---|---|---|
| Words | Overused vocabulary | `data/slop-words.json` |
| Phrases | Multi-word constructions | `data/slop-phrases.json` |
| Openers | Sentence-initial tells | `data/slop-openers.json` |
| Structures | Rhetorical shapes | `data/slop-structures.json` |

## Severity guide

- **critical** - the reader spots it instantly. Em dashes in volume, "It's not X. It's Y.", "delve", throat-clearing openers.
- **high** - consciously recognized as AI-flavored. Faux-insight setups, weasel attribution, synonym cycling.
- **medium** - stylistic tics. Overused connectors, rhetorical questions, emoji bullets.
- **low** - mild infrequency markers. Fine in small doses, tells in clusters.

## The five patterns that matter most

### 1. The binary contrast ("It's not X. It's Y.")

The most documented single construction. AI reaches for it because it produces the illusion of insight with zero content. Every AI writing detection study that measures constructions flags it.

Example: "The boom is priced on capex, not cash flow."
Fix: State the positive alone, or split the negation into its own sentence naming the actor: "Cash flow will decide who survives."

### 2. The throat-clearing opener

The first two sentences carry no information. They promise content instead of delivering it.

Example: "In today's fast-paced world, businesses must adapt. In this article, we explore the key strategies that can help."
Fix: Open with a fact, a number, or a claim.

### 3. The fake-profound ending

The closing line gestures at cosmic significance and commits to nothing.

Example: "The future isn't coming. It's already here."
Fix: End with the decision, the number, or the next step.

### 4. Weasel attribution

Anonymous authorities manufactured on demand.

Example: "Experts agree that hybrid work is here to stay."
Fix: Name the source or drop the claim.

### 5. Synonym cycling

The same thing renamed at every appearance because AI fears lexical repetition.

Example: "The agent handles your email. The assistant drafts replies. The copilot manages your inbox."
Fix: Repeat the actual word. Repetition of the precise term reads human; synonym cycling reads AI.

## The rhythm tells

- **Uniform sentence length**: AI token prediction prefers same-length sentences. Human writing breathes: long, short, long.
- **Anaphora stacking**: "We build. We ship. We iterate." One is fine; two in a row is a tell.
- **Transition overdose**: A connective at the start of most sentences. Humans let sentences stand alone.
- **Rule of three everywhere**: The triadic rhythm is AI's default cadence. At most one per section.

## How to use the data files

The JSON files are plain structured data, consumable by any linter, skill, or detector:

- `words[].word` - the string to flag
- `phrases[].phrase` - the pattern (some are literal, some are formulas; the `family` field groups them: binary-contrast, throat-clearing, weasel-attribution, etc.)
- `structures[].pattern` - the shape, with an example and a fix
- Every entry carries `severity` so tools can decide whether to warn or hard-block

Example tool usage (any language): load the files, build a flag list from `severity >= "high"`, scan your text, report hits with the `fix` as the suggestion.

## Language coverage

English-first. The tells documented here are the English-language fingerprint. Other languages have their own fingerprints:

- Korean: translationese (byeong-yeoktu), stiff written-register forms
- Russian: kantselyarit (bureaucratic register)
- Chinese: gongwen qiang (official-document tone)
- Japanese: AI-smell removal is an active community topic

The awesome-slop ecosystem index in `ecosystem.md` links the per-language tools.
