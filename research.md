# Research: What We Know About AI Slop

The evidence base for the patterns in this library. Every claim in `data/` and `reference/` traces to published research or large-scale measurement.

## Academic research

### Quantifying LLM usage in scientific papers
Liang et al., *Nature Human Behaviour* (2025).
Over a million papers. Words like "realm", "intricate", "showcasing", and "pivotal" were flat for a decade, then surged from 2023 as LLM-assisted writing entered scientific publishing. This is the strongest evidence that specific words are LLM fingerprints: the words did not change meaning, the generation distribution did.

### Delving into LLM-assisted writing through excess vocabulary
*Science Advances* (2025).
15 million biomedical abstracts. "Delve" rose about 1,500% between 2022 and 2024. The paper measures excess-vocabulary markers as a signature of LLM assistance.

### Measuring AI "Slop" in Text
Shaib et al. (2025), arXiv:2509.19163.
Builds a taxonomy of slop from expert interviews and span-level annotation. Finds slop judgments track dimensions like coherence and relevance, and that slop is a measurable property of text spans, not a vibe.

### EQ-Bench Slop Score
eqbench.com/slop-score.html
Public leaderboard scoring language models on slop words, "not x, but y" constructions, and over-represented trigrams. Confirms the construction-level tells (binary contrasts, specific trigram patterns) as measurable across models.

### Antislop framework
Antislop (2025), arXiv:2510.15061, accepted at ICLR 2026.
Documents thousands of slop phrases and proposes a sampling-time suppression method. The phrase list itself is public and is one of the largest collected datasets of slop constructions.

## Community field guides

### Wikipedia: Signs of AI writing
Wikipedia's field guide built from flagged articles during the AI cleanup project. Catalogs vocabulary, punctuation, and formatting tells with real examples. One of the longest-running community collections.

### WikiProject AI Cleanup
The Wikipedia editor project that reviews suspected AI-generated content and maintains the signs guide. Its flagged-article corpus is a practical dataset of real-world AI slop.

### Buffer's 52M post analysis
Social-post corpus analysis that fed several community detection lists. Contributed the social-media register tells (emoji structure, hashtag stacks, exclamation escalation).

### Peter Yang's No AI Slop (petergyang/no-ai-slop)
20+ pattern list including binary contrasts, throat-clearing openers, faux-insight setups, colon reveals, dramatic fragments, synonym cycling, and fake-profound endings. 5k stars.

### Kill AI Slop (yetone/kill-ai-slop)
Field guide to the visual and copy tics of AI-generated products, shipped as an agent skill.

## The Claude watermark

Anthropic confirmed that Claude models embed an invisible statistical mark in generated text (support.claude.com, "How Claude marks AI-generated content", 2026). It is detectable by systems, invisible to readers, and was introduced in response to EU AI Act obligations. A detected mark is evidence content was processed by Claude but is not fully conclusive; absence of a mark does not prove human authorship. Nature covered the rollout in "Can Anthropic's invisible watermarks curb 'AI slop'?" (Nature, 2026).

Independent of the technical watermark, Claude carries a writing fingerprint that detectors (GPTZero, Turnitin, Winston AI) are specifically calibrated to find, documented in `data/claude-watermarks.json`:

1. **First-person avoidance** - "One might argue", "It could be suggested" in place of "I".
2. **Systematic scope acknowledgement** - limitation disclaimers appearing at fixed structural positions, a Constitutional AI training artifact.
3. **Balanced counterargument inclusion** - every claim paired with its opposite, applied uniformly rather than selectively.
4. **Triadic list compulsion** - an RLHF artifact; human evaluators rewarded tidy three-point structures.
5. **Conclusion recycling** - restate, summarize, gesture at implications, in that order, almost every time.
6. **Paragraph architecture regularity** - uniform internal paragraph shape.
7. **Claude vocabulary cluster** - delve, nuanced, multifaceted, underscore, encompasses, pivotal, realm, vibrant, tapestry, "key takeaway".

The fingerprint is statistical: one pattern in a document is not evidence; the cluster is the signal. The fingerprint and the technical watermark are independent layers - removing one does not affect the other.

## The GPT fingerprint

GPT carries the chat-assistant register: the compliance and service-script behaviors trained by RLHF on conversational data, documented in `data/gpt-watermarks.json`:

1. **Assistant identity leak** - "As an AI language model" is the archetypal tell; newer models drop the literal phrase but keep the register ("As an AI,", "I'm here to help,").
2. **Assistantese closers** - "I hope this helps!", "Let me know if you have any questions."
3. **Deferential openers** - "Certainly!", "Absolutely!" before the actual answer.
4. **Apologetic preamble** - "I apologize for the confusion" when nothing went wrong.
5. **Listicle default** - numbered steps for content that is not sequential.
6. **Coverage phrasing** - "Whether you're a beginner or an expert..."
7. **The intersection frame** - "The intersection of technology and humanity."
8. **GPT vocabulary cluster** - delve, seamless, unlock, elevate, comprehensive, tailored, navigate, landscape.
9. **Formulaic emphasis** - "Remember that...", "Keep in mind...", "It's essential to..."
10. **Clean-slate summary** - restating the question before answering it.
11. **Bold-and-emoji formatting** - marketing-page formatting inside chat replies.
12. **Possibility hedge stack** - "may potentially possibly help."

Sources: GPTZero/Turnitin/Winston AI detection documentation, university detection guides (Maynooth), RTE's detection reporting, and community pattern lists. The assistant-register patterns distinguish GPT from Claude, whose fingerprint is the balanced-analyst register.

## Platform enforcement and brand strategy (2026)

### LinkedIn's AI slop crackdown
LinkedIn (2026) introduced a "seems like AI slop" button and its 360Brew detection model actively deprioritizes content flagged as generic AI output. LinkedIn defined AI slop as "low-effort, AI-generated content that may sound polished on the surface but lacks any real unique perspective or substance." Posts flagged suffer reduced reach. LinkedIn does not ban AI use but requires posts to "represent your voice and your perspectives." Source: LinkedIn News (2026), Wall Street Journal (2026).

### Forbes: leaders who share lived experience build trust
Carmine Gallo, Forbes (August 2026). Analyzed how leaders like Jeff Bezos (cattle ranch summers) and Jensen Huang (Denny's dishwasher) use stories of unique lived experiences to build trust that AI cannot replicate. The neuroscientific finding: the human brain looks for things that are new and novel, and favors concrete ideas over abstract ones. Generic advice ("Great leaders stay humble") is abstract and forgettable; Huang's story of washing dishes at Denny's is concrete and paints a visual. Stories transform abstract ideas into concrete, memorable, actionable lessons.

### Foundera: voice flattening is measurable
Foundera (2026). Documented "register mode collapse" in LLMs: when asked for "professional" content, models default to the median register. A 2024 ScienceDirect study found "using generative AI for social media content creation diminishes perceived brand authenticity significantly." Trust in founder content on LinkedIn dropped from 60% (2023) to 26% (2026). The Edelman-LinkedIn 2025 B2B report found distinctive founder voice drives 156% higher ROI on social content and 71% higher perceived effectiveness. Foundera codified six measurable dimensions of founder voice: vocabulary signature, sentence rhythm, register, topic gravity, contrarian moves, linguistic ticks.

### Digital Assassin: AI as editor, not ghostwriter
Digital Assassin / Rob Lawson (June 2026). Three anti-slop strategies for brands: (1) founder-led content with real humans front and center, (2) use AI as an editor, not a ghostwriter (start with raw human thinking, use AI to structure and tighten), (3) build a brand voice document before touching any AI tool. Google's E-E-A-T framework rewards Experience, Expertise, Authoritativeness, Trustworthiness. Generic AI slop scores poorly on all four. 73% of consumers can immediately identify AI-generated marketing content.

### SlopDetector: twelve measurable thresholds
SlopDetector (July 2026). Published reproducible thresholds for twelve signs of AI writing across five dimensions: vocabulary, cliche, structure, diversity, substance. Key thresholds: em dash density above 20 per 1,000 words (2 per 100) is a signal; burstiness (stdev/mean of sentence lengths) below 0.4 flags AI; more than 3 flagged style words per 500 words is a real signal; more than half of paragraphs failing the restatement test indicates substance-poor text. Convergence of 3-4 failing signs is the fingerprint, not any single sign.

### AI Publisher: detection framework 2026
AI Publisher (July 2026). Three-tier detection framework: Level 1 (linguistic statistical metrics: perplexity, burstiness, stylometric features), Level 2 (behavioral signals: posting velocity, temporal clustering, stylistic consistency over time), Level 3 (linguistic patterns and verbal tics: statistical density of flagged phrases). Key finding: "Anecdotes in the first person, named locations, specific dates, strongly held opinions, disagreements with popular positions, informal language, and regional idiom all register as positive quality signals within Google's E-E-A-T framework."

### aicheckr.io: twelve before-and-after fixes
aicheckr.io (2026). Twelve concrete AI slop patterns with before/after rewrites: em dash abuse, tapestry vocabulary, generic macro-intro, hedging overload, "it's not just X, it's Y" formula, listicle filler, rule-of-three stacking, conclusion boilerplate, transition chains, fake specificity, audience hedge, restating the question. The pattern behind all twelve: "the slop version could have been written without knowing anything." The human fixes are not stylistically fancier, they are specific.

## What the research agrees on

1. **Slop is measurable, not subjective.** The word-level and construction-level tells replicate across corpora (papers, abstracts, social posts).
2. **The tells are over-representation, not presence.** "Crucial" or "however" are not wrong words; their *frequency* in AI output is the signal. Tools should treat severity as frequency-weighted.
3. **Structure tells beat word tells.** Constructions (binary contrast, throat-clearing, fake-profound endings) are harder for models to stop producing than single words, because they are generation-level habits.
4. **Detectors are unreliable as classifiers.** False-positive rates on human writing are high. Use the pattern library as a *linting* layer for your own text, not as an accusation tool for others'.

## Open questions

- Which tells survive as models are fine-tuned against them? (The slop arms race.)
- Per-language fingerprints beyond English are under-researched; community lists (Korean byeong-yeoktu, Russian kantselyarit, Chinese gongwen qiang) are ahead of academia.
- Do visual tells have the same measurement base as writing tells? The visual list in `reference/visual.md` is community-derived, not yet corpus-measured.
