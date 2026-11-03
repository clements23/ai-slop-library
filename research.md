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

### Why is AI-generated language so hard to understand?
Clark, Martin, and Mahowald (2026), arXiv:2610.29162, submitted October 21, 2026.
Nine frontier and near-frontier models measured against human writing across chat, code, and essays: all nine use more inanimate subjects with animate verbs and more low-frequency n-grams than humans, and most use longer syntactic dependencies, stacked noun chains, and reduced object relatives without "that". A round-trip paraphrase control rules out generic rewriting as the cause. The authors' hypothesis, flagged as such: human language is optimized for communication while AI text is increasingly optimized for math, code, and reasoning, where RL with verifiable rewards pressures information density over clarity. A small-model GRPO experiment with a length penalty reproduces the shift as a proof of concept, not a demonstration about frontier pipelines. Notably, Claude Opus 5.5 scored better than Opus 5 on 19 of 21 comparisons, which the authors read as evidence the problem is reducible.

### An endless stream of AI slop (the software commons)
Baltes et al. (2026), arXiv:2603.27249 and arXiv:2604.16754.
1,154 Reddit and Hacker News posts where developers explicitly invoke "AI slop". Frames generated code, pull requests, documentation, and bug reports as a tragedy of the commons: individual productivity gains externalize review costs onto maintainers and reviewers. The first empirical literature on slop as a labor cost rather than a style problem.

### AI Slop and the Information Ecosystem (Columbia IGP)
Columbia University Institute for Global Politics (June 2026), proceedings of a March 2026 convening.
A systematic overview of the phenomenon plus a proposed research agenda for assessing its significance. The convening brings academic and practitioner perspectives together; useful as the institutional framing of slop beyond the style-tell literature.

### State of AI Slop 2026 (antislop.online)
antislop.online research report (published March 21, 2026, updated through September 2026).
Compiles and extends the public data on scale: 74% of new web pages published in 2025 contained at least some AI-generated material and 2.5% were 100% AI, per Ahrefs analysis of 900,000 fresh pages (classified with Originality.ai, so the blend category is uncertain); 475,000+ social mentions of "AI slop" across X, Instagram, TikTok, and Threads in a 30-day period (Visibrain, December 2025); the 200+ site "AutoBait" content-farm network (DoubleVerify, March 2026), detected through infrastructure signals rather than content analysis; and three dictionaries independently naming "slop" their 2025 Word of the Year. Category-level estimates put AI-heavy pages highest in product reviews (41%) and SEO how-to content (38%), lowest in technical documentation (6%).

### AI slop in music streaming
arXiv:2606.18052 (2026).
An empirical analysis of AI-generated music flooding streaming platforms: mass quantities of mediocre tracks produced to generate revenue, often misattributed as human-authored. Evidence that the slop economy extends past text into every medium where generation cost collapsed.

## Community field guides

### Wikipedia: Signs of AI writing
Wikipedia's field guide built from flagged articles during the AI cleanup project. Catalogs vocabulary, punctuation, and formatting tells with real examples. One of the longest-running community collections.

### WikiProject AI Cleanup
The Wikipedia editor project that reviews suspected AI-generated content and maintains the signs guide. Its flagged-article corpus is a practical dataset of real-world AI slop.

### Buffer's 52M post analysis
Social-post corpus analysis that fed several community detection lists. Contributed the social-media register tells (emoji structure, hashtag stacks, exclamation escalation).

### Peter Yang's No AI Slop (petergyang/no-ai-slop)
20+ pattern list including binary contrasts, throat-clearing openers, faux-insight setups, colon reveals, dramatic fragments, synonym cycling, and fake-profound endings. ~12.7k stars by October 2026.

### Kill AI Slop (yetone/kill-ai-slop)
Field guide to the visual and copy tics of AI-generated products, shipped as an agent skill.

### Stop Slop (hardikpandya/stop-slop)
18k stars, the most-starred writing skill in the ecosystem. Distills de-slopping into eight core rules: cut filler phrases and all adverbs, break formulaic structures (binary contrast, negative listing, dramatic fragmentation, rhetorical setups, false agency), enforce active voice with a named human subject, be specific (no vague declaratives like "the reasons are structural", no lazy extremes), put the reader in the room ("you" beats "people"), vary rhythm (two items beat three, no em dashes), trust readers (skip softening and justification), and cut anything that sounds like a pull-quote. Adds a five-dimension rubric (directness, rhythm, trust, authenticity, density, scored 1-10) with a revise-below-35/50 threshold. Two contributions this library adopted directly: the false-agency family ("the data tells us", "the decision emerges", "the culture shifts" all hide a person who did something) and the vague-declarative family (sentences that announce importance without naming the specific thing).

### FeedHive AI Slop Detector (FeedHive/ai-slop-detector)
Released October 2026 and trending immediately. 120 patterns published as machine-readable `patterns.json` across nine categories: vocabulary, stock phrases, sentence patterns, structure and rhythm, imagery and metaphor, substance, formatting and punctuation, chatbot residue, and social media/LinkedIn. Two categories are structurally new to the ecosystem's pattern data: "chatbot residue" (citation debris like `oaicite` and `turn0search0`, unreplaced placeholder tokens, sycophantic openers copied from chat contexts) and "substance" (the portability test: a sentence that could move unchanged to another company says nothing; made-up specifics; canned notability like "featured in leading publications"; hollow promises like "the ultimate guide"). This library's October 2026 additions draw directly from both categories.

### AIPromptIndex: 19 patterns (July 2026)
A rendering of Peter Yang's no-ai-slop taxonomy with before/after examples, organized into word-level, structural, rhythm, and ending tells. Notable framing: the pattern behind every instance is that "the slop version could have been written without knowing anything", and the recommended edit pass is the minimum effective edit (protect what sounds like the writer, cut word tells mechanically, fix structures, rewrite the ending, read aloud). Also documents negative listing ("Not a tool. Not a platform. A movement.") as binary contrast's louder cousin, a structure this library now catalogs.

### Seamslop (Matt Pocock, August 2026)
Coined in an August 15, 2026 post after Pocock asked Claude Opus 5's /teach skill to explain Buddhism and got back an explanation that was correct, useful, and built on the word "seam" four times in one paragraph. Seamslop names AI writing that reuses one clever word or metaphor relentlessly as structural connective tissue. The defining reply in the thread: the problem "cannot be addressed at grammar/word level", because the failure is paragraph-level composition optimized for the individual sentence, not for how the whole thing reads back. Cataloged in this library as the seamslop structure, the mirror image of synonym cycling.

### The Claudisms: Claude Opus 5's load-bearing register (August 2026)
explainx.ai's Claudism inventory (August 11, 2026), compiled from a 1,778-point Hacker News thread and an r/ClaudeAI documentation thread. The flagship is "load-bearing" applied to anything the model considers structurally important ("That is deliberate and load-bearing rather than tidy", written about a build step). The stable list: "worth stating plainly", "carry the argument", "full stop", "and the trap is", "The X matters more than Y", punchy fragments ("Not a detail. A design decision."), and colon or semicolon pauses replacing "but" and "because". Community inference: reinforcement learning rewarded dense, quotable prose, so the model optimizes for the turn of phrase. Practical finding: generic "write better" instructions do nothing; naming the specific tics (with "punchy" as the operative word to ban) works. This library encodes the phrases as the claudism family and the register as the eighth Claude fingerprint.

### The reader checklist and the eleventh tell (explainx.ai, August 2026)
explainx.ai's Top 10 Signs of AI-Generated Text (August 18, 2026): em dash density, word and phrase repetition, rule-of-three everywhere, stacked "it's not just X, it's Y", hedge stacking, suspiciously even rhythm, zero typos zero voice, summary-then-restate structure, vague-specific mismatch, and buzzword clustering, with the honest caveat that every one false-positives on human writers. A day later Paul Graham added an eleventh tell at the verb level: colorful verb inflation ("drew" 100 votes instead of "got" them, "forged" a partnership, "unveiled" a roadmap), plus the softer-rounder-word variant documented in the replies. Two of these are now structures in this library (summary-then-restate, colorful verb inflation).

### EnhancePost: 254 review rules (September 2026)
A deterministic browser reference cataloging writing patterns as regex review rules across named categories: marketing templates ("unlock the full potential", "turn challenges into opportunities", "more important than ever"), brochure register (nestled, picturesque, idyllic, breathtaking, "in the heart of"), business jargon, transition crutches, hyphenated cliches, filler grammar ("has the ability to", "on a regular basis"), content artifacts (placeholder slots, leaked citation tokens, zero-width characters, chat utm_source parameters), and tell phrases. The framing is conservative by design: "a match is a prompt to review a sentence, it does not identify an author". This library's November 2026 additions draw on its marketing-template, brochure-register, filler-grammar, and content-artifact categories.

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

### Wikipedia's measured flag rate (Pangram via IEEE Spectrum)
IEEE Spectrum interview with WikiProject AI Cleanup founder Ellia Lebleu (October 21, 2026). Pangram flagged roughly 20% of new articles and drafts as AI-generated in late 2025 and roughly 15 to 16% in early 2026, with no false positives on pre-ChatGPT text, so the figures are treated as a conservative lower bound; the drop's cause is unresolved (better rule awareness, or newer models the detector catches less often). Two operational findings matter for this library: the tell shifted from fabricated citations to real sources whose content does not support the sentence attached to them (retrieval-augmented generation fixed the fake-source problem, so claim-versus-source checking is now the center of the work), and no single signal is enough: rule of three and "not X, but Y" are each weak alone but meaningful in combination, with volume as the third flag. Wikimedia's Paste Check flags text pasted directly from chatbots, which is the same chatbot-residue surface this library's punctuation layer documents.

## What the research agrees on

1. **Slop is measurable, not subjective.** The word-level and construction-level tells replicate across corpora (papers, abstracts, social posts).
2. **The tells are over-representation, not presence.** "Crucial" or "however" are not wrong words; their *frequency* in AI output is the signal. Tools should treat severity as frequency-weighted.
3. **Structure tells beat word tells.** Constructions (binary contrast, throat-clearing, fake-profound endings) are harder for models to stop producing than single words, because they are generation-level habits.
4. **Detectors are unreliable as classifiers.** False-positive rates on human writing are high. Use the pattern library as a *linting* layer for your own text, not as an accusation tool for others'.

## Open questions

- Which tells survive as models are fine-tuned against them? (The slop arms race.)
- Per-language fingerprints beyond English are under-researched; community lists (Korean byeong-yeoktu, Russian kantselyarit, Chinese gongwen qiang) are ahead of academia.
- Do visual tells have the same measurement base as writing tells? The visual list in `reference/visual.md` is community-derived, not yet corpus-measured.
- Is the density problem (arXiv:2610.29162) reversible? Opus 5.5 scored better than Opus 5 on 19 of 21 readability comparisons, so if communication becomes a reward target, the rhythm and syntax tells may age faster than the vocabulary ones.
