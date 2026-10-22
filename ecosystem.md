# The AI Slop Ecosystem

Curated index of the existing AI-slop repositories and tools, researched October 2026 (star counts via the GitHub API, 2026-10-22). This library is the pattern-data layer; the ecosystem below is everything else people have built around the same problem.

## Pattern libraries and skills (writing)

| Repo | Stars | What it is |
|---|---|---|
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | ~18.2k | Skill file for removing AI tells from prose. Core rules (kill adverbs, active voice, vary rhythm, cut quotables, no false agency, no vague declaratives) plus a five-dimension 1-10 scoring rubric (revise below 35/50). The most-starred writing skill in the ecosystem. |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | ~12.7k | Agent skill catching 20+ writing patterns, with a Python linter and the "minimum effective edit" workflow. Taxonomy adapted by third-party guides (AIPromptIndex's 19-pattern rendering). |
| [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) | ~1.9k | System prompt that makes LLMs talk like normal people. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | ~1.4k | Field guide to visual and copy tics of AI products, plus an agent skill that scans and strips them. |
| [realrossmanngroup/no_ai_slop_writing_rules](https://github.com/realrossmanngroup/no_ai_slop_writing_rules) | ~704 | Portable CLAUDE.md that writes in a specific human voice (Louis Rossmann), plus skills. |
| [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) | ~558 | Skill banning 50+ words, 35+ phrases, 16 openers, 10 structures. CMU/Wikipedia/Buffer grounded. |
| [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp) | ~475 | Japanese-language de-slop skill. |
| [FeedHive/ai-slop-detector](https://github.com/FeedHive/ai-slop-detector) | ~81 | 120 patterns as a machine-readable `patterns.json` across nine categories, including "chatbot residue" (citation debris, placeholder tokens, sycophancy) and "substance" (the portability test, made-up specifics, canned notability). Trending within days of its October 2026 release. |
| [nowork-ai/anti-ai-slop-cz](https://github.com/nowork-ai/anti-ai-slop-cz) | ~34 | Czech de-slop rules. |
| [RocStone/roc-no-ai-slop-zh](https://github.com/RocStone/roc-no-ai-slop-zh) | ~11 | Chinese de-slop skill. |
| [tuwulalo/ai-slop-cleaner-en-ru](https://github.com/tuwulalo/ai-slop-cleaner-en-ru) | ~6 | Bilingual EN+RU de-slop skill. |
| [liuxiaobai8868/ai-slop-detector](https://github.com/liuxiaobai8868/ai-slop-detector) | ~5 | Multilingual detector + de-slop toolkit (zh/en/es/ar/hi). |

## Awesome lists

| Repo | Stars | What it is |
|---|---|---|
| [yikerman/awesome-ai-slop](https://github.com/yikerman/awesome-ai-slop) | ~26 | Satirical curated list of slop projects and papers. |
| [hwajongpark/awesome-slop](https://github.com/hwajongpark/awesome-slop) | ~6 | Serious curated list: research, linters, classifiers, humanizers, organized by language. |

## Linters and CLIs

| Repo | Stars | What it is |
|---|---|---|
| [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop) | ~5.6k | Opinionated Oxlint rule pack rejecting "low-evidence" TypeScript and JavaScript patterns in AI-generated code. The most-starred code-lint take on slop. |
| [walidboulanouar/anti-ai-slop](https://github.com/walidboulanouar/anti-ai-slop) | ~24 | CLI that detects and removes AI-slop words and em dashes. |
| [ai-that-works/deslop](https://github.com/ai-that-works/deslop) | ~24 | CLI that rewrites documents to sound less AI. |
| [realsigridjin/ai-slop-cleaner](https://github.com/realsigridjin/ai-slop-cleaner) | ~9 | Rust CLI with regex scoring for AI prose patterns. |
| [antydizajn/ai-slop-detect](https://github.com/antydizajn/ai-slop-detect) | ~9 | CLI with 70+ EN/PL patterns for markdown, prose, code comments. |
| [Xe/slop](https://github.com/Xe/slop) | ~6 | AI slop utilities. |
| [hwajongpark/slop-gate](https://github.com/hwajongpark/slop-gate) | ~3 | Zero-dependency CLI. Em dash + ~40 English tells, opt-in packs for Korean, Russian, Vietnamese, Chinese, Filipino. |

## Humanizers and voice tools

| Tool | What it is |
|---|---|
| [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) | Three-tier humanizer pipeline (Forensic/Strict/Aesthetic) for LinkedIn posts. Integrated into TAIS format guide v2.5.0. |
| [ItsssssJack/SlopMonster](https://github.com/ItsssssJack/SlopMonster) | Lint, cleanse with a rival model, lint again. A three-pass pipeline that treats de-slopping as an iterative loop rather than a single rewrite. |
| [Foundera](https://www.foundera.co/) | Founder-voice preservation platform. 5-step hybrid edit workflow, voice profile extraction from unscripted speech, 6 measurable dimensions of founder voice. Research-backed. |
| [The Founder Voice](https://www.thefoundervoice.com/) | AI-powered personal branding tool that generates social content matching a founder's authentic voice. |

## Detectors (classifiers and scanners)

| Repo | Stars | What it is |
|---|---|---|
| [flamehaven01/AI-SLOP-Detector](https://github.com/flamehaven01/AI-SLOP-Detector) | ~102 | Detects empty functions, fake docs, inflated comments in AI code. v3.6.0 with a Claude Code skill. |
| [distil-labs/distil-ai-slop-detector](https://github.com/distil-labs/distil-ai-slop-detector) | ~95 | Local in-browser AI text detection. |
| [rsionnach/sloppylint](https://github.com/rsionnach/sloppylint) | ~91 | Python AI slop detector: over-engineering, hallucinations, dead code. |
| [yuvrajangadsingh/vibecheck](https://github.com/yuvrajangadsingh/vibecheck) | ~27 | "ESLint for AI slop": AI code smells in JS/TS and Python. |
| [fs0cietyx/ai-slop-detector](https://github.com/fs0cietyx/ai-slop-detector) | ~18 | PyTorch + LoRA classifier. |
| [styrene-lab/lipstyk](https://github.com/styrene-lab/lipstyk) | ~12 | Machine-generated code pattern detection across Rust, TS/JS, Python, HTML. |
| [SergUdo/ai-slop-gate](https://github.com/SergUdo/ai-slop-gate) | ~6 | Vendor-agnostic CLI compliance reasoning engine. |
| [Euraika-Labs/ai-slopcheck](https://github.com/Euraika-Labs/ai-slopcheck) | ~2 | Deterministic scanner, 72 rules, pip installable. |

## Web-based slop checkers

| Tool | What it is |
|---|---|
| [SlopDetector](https://slopdetector.org/) | Free, 100% local browser-based slop checker. Scores five dimensions: vocabulary, cliche, structure, diversity, substance. Published reproducible thresholds for twelve signs of AI writing (July 2026). |
| [aicheckr.io](https://www.aicheckr.io/) | Free AI checker + humanizer. Sentence-level highlighting of slop patterns. Twelve documented before/after fixes. |

## CI and GitHub automation

| Repo | Stars | What it is |
|---|---|---|
| [peakoss/anti-slop](https://github.com/peakoss/anti-slop) | ~846 | GitHub Action that detects and auto-closes low-quality AI slop PRs. |
| [Blue-B/slopguard](https://github.com/Blue-B/slopguard) | ~61 | GitHub App that quarantines slop PRs with provenance tagging, never auto-closes. |
| [cglabs-ai/guardian](https://github.com/cglabs-ai/guardian) | ~12 | Stop AI slop before it hits the codebase. |
| [krrish175-byte/ai-slop-guardian](https://github.com/krrish175-byte/ai-slop-guardian) | ~9 | GitHub App labeling AI slop in PRs, issues, comments. |

## Design, UI, and motion slop

| Repo | Stars | What it is |
|---|---|---|
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | ~30.6k | Anti-AI-slop design skill for Claude Code, Cursor, Codex. The most-starred slop project overall. |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | ~6.8k | Rules for a coding agent to filter out generic AI-generated UI, text, and code. Grew ~30x since the August index. |
| [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | ~2k | Reverse-engineered system prompt plus skill library turning an LLM into an opinionated, accessibility-aware, slop-resistant design collaborator. |
| [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | ~876 | Design skill for coding agents; "stop shipping AI-slop UI". |
| [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | ~966 | Agent skill that turns AI slop videos into motion-designer-grade films (GSAP, hyperframes). The first popular anti-slop tool aimed at video rather than prose or UI. |
| [AThevon/genjutsu](https://github.com/AThevon/genjutsu) | ~629 | Creative coding skills (GSAP, Motion, Three.js, Compose, SwiftUI) that require an approved interaction thesis before writing code. Anti-slop by process design. |
| [codeswithroh/tastemaker](https://github.com/codeswithroh/tastemaker) | ~484 | Skill grounding generated UI in real reference images plus a persistent per-developer taste profile instead of statistical defaults. |
| [vibedesignlab/slopslap](https://github.com/vibedesignlab/slopslap) | ~37 | Parallel-inspection UI slop pipeline skill. |
| [Vinayak-Shukla-03/anti-ai-slop](https://github.com/Vinayak-Shukla-03/anti-ai-slop) | ~9 | UI and presentation de-slop skill. |

## Content blockers (YouTube, browser, search)

| Repo | Stars | What it is |
|---|---|---|
| [alvi-se/ai-ublock-blacklist](https://github.com/alvi-se/ai-ublock-blacklist) | ~707 | Filter list blocking AI content-farm sites from search results via uBlock Origin and uBlacklist. |
| [Override92/AiSList](https://github.com/Override92/AiSList) | ~355 | Filter list for AI slop YouTube channels. |
| [BMHeades/combatslop-yt](https://github.com/BMHeades/combatslop-yt) | ~31 | Browser extension detecting AI slop videos on YouTube. |
| [NikoboiNFTB/DeSlop](https://github.com/NikoboiNFTB/DeSlop) | ~18 | Blocklist-driven YouTube feed cleaner. |
| [adityabhandari781/Slop-Watch](https://github.com/adityabhandari781/Slop-Watch) | ~10 | Crowdsourced slop-detecting Chrome extension for YouTube. |

## Adjacent

- [Yu-369/VibeCurb](https://github.com/Yu-369/VibeCurb) (~986) - injects taste into AI workflows to stop agents generating boring defaults.
- [alchaincyf/huashu-md-html](https://github.com/alchaincyf/huashu-md-html) (~923) - md/html pipeline skill that ships four anti-AI-slop HTML themes.
- [sam-paech/antislop-sampler](https://github.com/sam-paech/antislop-sampler) (~358) - sampling-time suppression of slop phrases (ICLR 2026).
- [glacierphonk/naming](https://github.com/glacierphonk/naming) (~119) - metaphor-driven product naming that avoids AI slop.
- [drunkrhin0/antislop](https://github.com/drunkrhin0/antislop) (~23) - self-described "by slop for slop".
- [The-Vibe-Company/vibe-drift-tracker](https://github.com/The-Vibe-Company/vibe-drift-tracker) (~21) - VS Code extension tracking vibe-coding drift in real time.

## Watermark and provenance evasion

| Repo | Stars | What it is |
|---|---|---|
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | ~24.6k | Agent skill + stdlib Python service stripping multi-vendor provenance marks from text and files: Unicode text hygiene (ZWSP, bidi, exotic spaces), statistical token-sampling watermark rewrites (best-effort), and C2PA/EXIF/XMP/props from PNG, JPEG, WebP, SVG, PDF, DOCX, ODT, HTML, and Markdown. Covers Claude, Gemini/SynthID-Text, OpenAI, and open-LLM Kirchenbauer-style marks. MIT. |
| [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | ~6.1k | Python library + CLI removing visible and invisible AI watermarks and provenance metadata (SynthID, C2PA, EXIF, IPTC, XMP) from images and video you generated yourself. Apache 2.0; hosted service at raiw.cc; companion ComfyUI node pack. |

## Where this library fits

The ecosystem is divided into skills (instructions for agents), lists (links), detectors (classifiers), and automation (CI). None of them publish the *pattern data itself* as a standalone, structured, machine-readable dataset spanning writing, structure, punctuation, and model fingerprints. This library is that layer: `data/*.json` is the shared substrate a linter, a skill, or a detector can load, with the research and reference documentation alongside.

## Research sources

Full citations in `research.md`. Key sources: Liang et al. (Nature Human Behaviour, 2025), Science Advances 2025 (delve), Shaib et al. (arXiv:2509.19163), EQ-Bench Slop Score, Antislop (ICLR 2026), Wikipedia Signs of AI writing, Buffer 52M post analysis, stop-slop (2026), FeedHive's 120-pattern dataset (2026).
