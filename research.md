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

## What the research agrees on

1. **Slop is measurable, not subjective.** The word-level and construction-level tells replicate across corpora (papers, abstracts, social posts).
2. **The tells are over-representation, not presence.** "Crucial" or "however" are not wrong words; their *frequency* in AI output is the signal. Tools should treat severity as frequency-weighted.
3. **Structure tells beat word tells.** Constructions (binary contrast, throat-clearing, fake-profound endings) are harder for models to stop producing than single words, because they are generation-level habits.
4. **Detectors are unreliable as classifiers.** False-positive rates on human writing are high. Use the pattern library as a *linting* layer for your own text, not as an accusation tool for others'.

## Open questions

- Which tells survive as models are fine-tuned against them? (The slop arms race.)
- Per-language fingerprints beyond English are under-researched; community lists (Korean byeong-yeoktu, Russian kantselyarit, Chinese gongwen qiang) are ahead of academia.
- Do visual tells have the same measurement base as writing tells? The visual list in `reference/visual.md` is community-derived, not yet corpus-measured.
