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

## The patterns that matter most

### 1. The binary contrast ("It's not X. It's Y.")

The most documented single construction. AI reaches for it because it produces the illusion of insight with zero content. Every AI writing detection study that measures constructions flags it.

The family has four faces, all banned:
- "It's not X. It's Y." - contracted
- "X is not Y. It is Z." - declarative
- "Not X, but Y" - concession
- "X, not Y" - negation tail (e.g., "a monthly operating cost, not a one-time choice")

Example: "The boom is priced on capex, not cash flow. The gap is not labor arbitrage. It is a trillion-parameter model."
Fix: State the positive alone, or split the negation into its own sentence naming the actor: "Cash flow will decide who survives. The gap is architecture."

### 2. The trailing appended insight (wire-style writers put the point first)

A sentence that appears complete, then appends the actual thesis after a final "and": "The AI cost gap is architecture, subsidies, and strategy, and most buyers are reading the wrong number." The point that matters most is smuggled into the weakest grammatical slot, as an afterthought.

This reads as AI because wire-style writers (AP, Reuters) front-load the point. The lede answers "what happened" in the first sentence; the reason lands in the second. AI does the inverse: it builds context, then tags the insight on at the end where it is least likely to be read.

Fix: Promote the appended clause to its own sentence at the front. "Most buyers are reading the wrong number. The gap is architecture, subsidies, and strategy."

### 3. The throat-clearing opener

The first two sentences carry no information. They promise content instead of delivering it.

Example: "In today's fast-paced world, businesses must adapt. In this article, we explore the key strategies that can help."
Fix: Open with a fact, a number, or a claim.

### 4. The fake-profound ending

The closing line gestures at cosmic significance and commits to nothing.

Example: "The future isn't coming. It's already here."
Fix: End with the decision, the number, or the next step.

### 5. Weasel attribution

Anonymous authorities manufactured on demand.

Example: "Experts agree that hybrid work is here to stay."
Fix: Name the source or drop the claim.

### 6. Synonym cycling

The same thing renamed at every appearance because AI fears lexical repetition.

Example: "The agent handles your email. The assistant drafts replies. The copilot manages your inbox."
Fix: Repeat the actual word. Repetition of the precise term reads human; synonym cycling reads AI.

### 7. Litotes ("not uncommon", "not insignificant")

Understatement through double negative or negated opposite. AI reaches for litotes to sound measured while committing to nothing. "Not uncommon" means "common" but sounds less committal. "Not insignificant" means "significant" but hedges through negation. "Far from trivial" means "hard" but wraps it in distance.

This is distinct from binary contrast, which sets up X against Y in two clauses. Litotes is a single clause that negates the opposite of what it means. The result is a sentence that is technically true but semantically evasive. One instance is a style choice. Two or more in a passage is a hedge pattern.

Family members: "not uncommon", "not insignificant", "not without merit", "far from trivial", "far from simple", "by no means", "not unlike", "not entirely wrong", "none too", "not a small feat".

Fix: State the positive directly. "Not insignificant" becomes "significant". "Not uncommon" becomes "common". "Far from trivial" becomes "hard" or name the specific difficulty.

### 8. Hedging qualifier chains

Three or more hedges stacked in a single sentence. "This might potentially possibly help some teams improve productivity in certain contexts, though results may vary depending on various factors."

AI stacks qualifiers because each hedge reduces the probability of being wrong. Three hedges in one sentence produce a claim so diluted it carries no information. The reader finishes the sentence unable to determine whether the writer believes the claim.

Fix: Commit to the claim or drop it. If you're unsure, name the specific condition: "This works for teams under ten. Past that, the standup format collapses."

### 9. Restating the question as the answer

Answer-shaped text that explains why the question matters instead of answering it.

Example: "How much does it cost? Pricing is an important consideration when choosing any tool. Costs can vary based on your needs, usage, and the features you require."

AI generates this pattern in FAQ sections and answer-box content. The response restates the question in declarative form, adds context about why the question is important, and finishes without naming a number, a range, or a decision criterion.

Fix: Answer the question in the first sentence. "It costs $12/month billed annually, or $18 month-to-month."

## Defeating AI slop: what the research shows

### The specificity principle

Every anti-slop study, detection framework, and brand strategy guide converges on the same finding: the single most reliable anti-slop technique is specificity. The aicheckr.io analysis of twelve slop patterns concluded: "every example above fails the same way: the slop version could have been written without knowing anything." No numbers that could be wrong, no positions that could be argued with, no details that could only come from doing the work.

The fix is not stylistic flair. It is information density. "Swap the 6 p.m. soda for water and you cut roughly 40,000 calories a year" cannot be generated by a model that does not know the reader's soda habit. That specificity is what makes it human.

### The deletion test

The most reliable structural test for slop. Read each paragraph and ask: can I name one concrete fact it gave me? If more than half the paragraphs fail, the text is substance-poor. The SlopDetector 2026 threshold study formalized this: "after a paragraph, can you restate one concrete fact? AI text is engineered to sound informative while committing to nothing."

### Founder-voice anti-slop: the six dimensions

Research from Foundera (2026), Carmine Gallo/Forbes (2026), and LinkedIn's own AI slop crackdown identifies six measurable dimensions of authentic founder voice. AI flattens all six toward the median:

1. **Vocabulary signature** - recurring words you instinctively reach for, jargon you reject, your term choice when multiple synonyms exist. AI cycles synonyms; founders repeat the same noun when it's the same thing.
2. **Sentence rhythm** - your natural cadence. Short staccato, long flowing clauses, fragments for emphasis. AI produces uniform sentence length.
3. **Register** - your formal-to-casual ratio. Do you code-switch between technical and plain language? AI stays in one register.
4. **Topic gravity** - the themes you instinctively pull toward, the problems you keep returning to. AI has no gravitational center.
5. **Contrarian moves** - the positions you hold that differ from consensus. AI hedges toward consensus.
6. **Linguistic ticks** - phrases you repeat, metaphors you favor, words you avoid. AI diversifies to avoid repetition.

### The voice-preservation workflow

The research prescribes a five-step workflow for keeping AI-assisted content authentic (Foundera, 2026):

1. **Generate** the first draft with AI, providing your voice profile as context.
2. **Audit** the draft against your voice profile. Highlight every sentence that doesn't match.
3. **Manual voice pass** - rewrite every flagged sentence in your actual voice. Usually 30-50% of the draft.
4. **Strengthen the contrarian edge** - find places where AI played it safe and replace hedges with conviction.
5. **Read-aloud test** - if 80%+ of sentences pass, you're good. If less than 70%, do another pass.

The entire workflow takes 30-45 minutes per post. The Edelman-LinkedIn 2025 B2B report found that distinctive founder voice drives 156% higher ROI on social content and 71% higher perceived effectiveness than generic industry language.

### LinkedIn's algorithmic enforcement

LinkedIn introduced a "seems like AI slop" button in mid-2026 and its 360Brew model actively deprioritizes content flagged as generic AI output. Posts flagged as AI slop suffer reduced reach. Forbes (August 2026) reported: "LinkedIn favors posts that spark real human conversations." The platform's definition: "low-effort, AI-generated content that may sound polished on the surface but lacks any real unique perspective or substance."

The implication for writers: defeating AI slop is not just editorial quality. It is a distribution advantage. Content that reads as human gets algorithmic boost. Content that reads as template gets suppressed.

### What Google rewards

Google's E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness) explicitly rewards the same signals that defeat slop. AI Publisher's 2026 detection framework found: "Anecdotes in the first person, named locations, specific dates, strongly held opinions, disagreements with popular positions, informal language, and regional idiom all register as positive quality signals." Content that passes robust authorship verification and shows human specificity gains ranking advantages. Content that fails is penalized not because it is "AI" but because it lacks expertise, authoritativeness, and trustworthiness.

## The Claude layer

Claude-specific tells live in `data/claude-watermarks.json`. Two independent layers:

**The technical watermark.** Anthropic embeds an invisible statistical mark in Claude output. It is detectable by systems and cannot be removed by rewriting the fingerprint. Absence of a mark does not prove human authorship.

**The writing fingerprint.** Seven patterns detectors are calibrated to find:

1. **First-person avoidance** - "One might argue", "It could be suggested" in place of "I", even when the genre invites a personal voice. A personal essay with zero first-person pronouns flags detectors.
2. **Systematic scope acknowledgement** - "While this is not an exhaustive treatment..." at the close of every analytical section. Human writers acknowledge limits only when the argument needs defending.
3. **Balanced counterargument inclusion** - every claim paired with its opposite. Constitutional AI trains Claude to balance; applied uniformly it reads as hedging.
4. **Triadic list compulsion** - "There are three key factors to consider" on reflex. An RLHF artifact.
5. **Conclusion recycling** - restate, summarize, gesture at implications, always in that order. Human conclusions are messier.
6. **Paragraph architecture regularity** - uniform topic-sentence-support-transition shape in every paragraph.
7. **Claude vocabulary cluster** - nuanced, multifaceted, encompasses, underscore, key takeaway, pivotal, realm, vibrant, tapestry.

The fingerprint is statistical: one instance is not evidence; the cluster is the signal.

## The GPT layer

GPT-specific tells live in `data/gpt-watermarks.json`. Where Claude's fingerprint is the balanced-analyst register (hedging, scope notes, triads), GPT's is the chat-assistant register:

1. **Assistant identity leaks** - "As an AI language model", "I'm here to help". The archetypal tells; newer models drop the literal phrases but keep the register.
2. **Assistantese** - compliance openers ("Certainly!"), service closers ("I hope this helps!"), apologetic preambles ("I apologize for the confusion") when nothing went wrong.
3. **Possibility hedge stacks** - "may potentially possibly help". GPT hedges because it cannot verify.
4. **Listicle default** - numbered steps for non-sequential content, "Here are 5 tips...".
5. **Coverage phrasing** - "Whether you're a beginner or an expert..." sprayed at every audience.
6. **GPT vocabulary cluster** - unlock, elevate, seamless, tailored, comprehensive, navigate, landscape - more promotional than Claude's cluster.

The assistant-register patterns are what distinguish GPT output from Claude's; the vocabulary layers overlap at the top (delve, pivotal, landscape are shared).

## The rhythm tells

- **Uniform sentence length**: AI token prediction prefers same-length sentences. Human writing breathes: long, short, long.
- **Anaphora stacking**: "We build. We ship. We iterate." One is fine; two in a row is a tell.
- **Transition overdose**: A connective at the start of most sentences. Humans let sentences stand alone.
- **Rule of three everywhere**: The triadic rhythm is AI's default cadence. At most one per section.

## Founder-voice cadence and the publication-plug closer

A founder's LinkedIn voice is judged on three surfaces the linter can measure. The audit that produced these rules looked at a strong-on-substance draft and found it read as a tech-journalist news recap rather than executive opinion. The fix lives in cadence, framing, and the closing line.

**Cadence: stop breaking every sentence into its own paragraph.** The LinkedIn formatting trap is line-broken sentences masquerading as rhythm. "Cursor was the best coding tool. Anthropic and OpenAI own the stack. Cursor rented brainpower. Colossus fixes that." reads as a content template. A seasoned founder voice groups related sentences into two-to-three-sentence mini-paragraphs and mixes one short standalone line with one standard paragraph per section. A post of fifteen visible lines should compress to six-to-eight paragraphs. The detection rule: compare sentence count to paragraph count; every-line-its-own-paragraph is the tell.

**Framing: executive synthesis, not news recap.** A tech journalist reports what happened; a founder tells the reader what to do or how to think about it. The substance in the audited draft was strong (the all-stock dilution math, the interface-plus-compute merger framing, the rented-brainpower thesis) but the framing read as a recap because each sentence summarized a fact rather than issuing a take. Rewrite each fact into a claim with a verb of judgment: "Cursor was the best coding tool" becomes "Cursor had a vulnerability: it was renting brainpower while Anthropic and OpenAI controlled their own stacks." Same fact, founder register.

**Closer: drop the transactional publication plug.** The branded triplet "Full article only on [publication]. We do the reading. You get the decision." reads as a value-extraction pitch rather than domain authority. Three lines that explicitly promise value while naming the brand behind the post. The corrected pattern weaves the publication as a natural authority reference into the narrative, then closes on the reader's takeaway. External links in the main post body are also penalized by LinkedIn's organic-reach algorithm, so move the URL to the first comment and reference it in prose ("Link in the comments below."). The softer closer sounds like: "We analyzed the full breakdown and strategic implications over at The AI Sift. Link in the comments below." Same call to action, no value-extraction register.

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
