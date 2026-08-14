# The AI Slop Ecosystem

Curated index of the existing AI-slop repositories and tools, researched August 2026. This library is the pattern-data layer; the ecosystem below is everything else people have built around the same problem.

## Pattern libraries and skills (writing)

| Repo | Stars | What it is |
|---|---|---|
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | ~5k | Agent skill catching 20+ writing patterns. The most popular writing-slop skill. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | ~1k | Field guide to visual and copy tics of AI products, plus an agent skill that scans and strips them. |
| [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) | ~350 | Skill banning 50+ words, 35+ phrases, 16 openers, 10 structures. CMU/Wikipedia/Buffer grounded. |
| [realrossmanngroup/no_ai_slop_writing_rules](https://github.com/realrossmanngroup/no_ai_slop_writing_rules) | ~650 | Portable CLAUDE.md that writes in a specific human voice. |
| [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) | ~1.8k | System prompt that makes LLMs talk like normal people. |
| [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp) | ~380 | Japanese-language de-slop skill. |
| [tuwulalo/ai-slop-cleaner-en-ru](https://github.com/tuwulalo/ai-slop-cleaner-en-ru) | ~6 | Bilingual EN+RU de-slop skill. |
| [nowork-ai/anti-ai-slop-cz](https://github.com/nowork-ai/anti-ai-slop-cz) | ~18 | Czech de-slop rules. |
| [RocStone/roc-no-ai-slop-zh](https://github.com/RocStone/roc-no-ai-slop-zh) | ~9 | Chinese de-slop skill. |
| [liuxiaobai8868/ai-slop-detector](https://github.com/liuxiaobai8868/ai-slop-detector) | ~4 | Multilingual detector + de-slop toolkit (zh/en/es/ar/hi). |

## Awesome lists

| Repo | Stars | What it is |
|---|---|---|
| [yikerman/awesome-ai-slop](https://github.com/yikerman/awesome-ai-slop) | ~24 | Satirical curated list of slop projects and papers. |
| [hwajongpark/awesome-slop](https://github.com/hwajongpark/awesome-slop) | ~3 | Serious curated list: research, linters, classifiers, humanizers, organized by language. |

## Linters and CLIs

| Repo | Stars | What it is |
|---|---|---|
| [hwajongpark/slop-gate](https://github.com/hwajongpark/slop-gate) | - | Zero-dependency CLI. Em dash + ~40 English tells, opt-in packs for Korean, Russian, Vietnamese, Chinese, Filipino. |
| [walidboulanouar/anti-ai-slop](https://github.com/walidboulanouar/anti-ai-slop) | ~20 | CLI that detects and removes AI-slop words and em dashes. |
| [realsigridjin/ai-slop-cleaner](https://github.com/realsigridjin/ai-slop-cleaner) | ~8 | Rust CLI with regex scoring for AI prose patterns. |
| [antydizajn/ai-slop-detect](https://github.com/antydizajn/ai-slop-detect) | ~4 | CLI with 70+ EN/PL patterns for markdown, prose, code comments. |
| [ai-that-works/deslop](https://github.com/ai-that-works/deslop) | ~20 | CLI that rewrites documents to sound less AI. |
| [Xe/slop](https://github.com/Xe/slop) | ~6 | AI slop utilities. |

## Detectors (classifiers and scanners)

| Repo | Stars | What it is |
|---|---|---|
| [distil-labs/distil-ai-slop-detector](https://github.com/distil-labs/distil-ai-slop-detector) | ~92 | Local in-browser AI text detection. |
| [flamehaven01/AI-SLOP-Detector](https://github.com/flamehaven01/AI-SLOP-Detector) | ~77 | Detects empty functions, fake docs, inflated comments in AI code. |
| [rsionnach/sloppylint](https://github.com/rsionnach/sloppylint) | ~87 | Python AI slop detector: over-engineering, hallucinations, dead code. |
| [fs0cietyx/ai-slop-detector](https://github.com/fs0cietyx/ai-slop-detector) | ~18 | PyTorch + LoRA classifier. |
| [SergUdo/ai-slop-gate](https://github.com/SergUdo/ai-slop-gate) | ~6 | Vendor-agnostic CLI compliance reasoning engine. |
| [styrene-lab/lipstyk](https://github.com/styrene-lab/lipstyk) | ~11 | Machine-generated code pattern detection across Rust, TS/JS, Python, HTML. |
| [Euraika-Labs/ai-slopcheck](https://github.com/Euraika-Labs/ai-slopcheck) | ~0 | Deterministic scanner, 72 rules, pip installable. |
| [yuvrajangadsingh/vibecheck](https://github.com/yuvrajangadsingh/vibecheck) | ~22 | "ESLint for AI slop": AI code smells in JS/TS and Python. |

## CI and GitHub automation

| Repo | Stars | What it is |
|---|---|---|
| [peakoss/anti-slop](https://github.com/peakoss/anti-slop) | ~760 | GitHub Action that detects and auto-closes low-quality AI slop PRs. |
| [Blue-B/slopguard](https://github.com/Blue-B/slopguard) | ~57 | GitHub App that quarantines slop PRs with provenance tagging, never auto-closes. |
| [krrish175-byte/ai-slop-guardian](https://github.com/krrish175-byte/ai-slop-guardian) | ~8 | GitHub App labeling AI slop in PRs, issues, comments. |
| [cglabs-ai/guardian](https://github.com/cglabs-ai/guardian) | ~12 | Stop AI slop before it hits the codebase. |

## Design / UI slop

| Repo | Stars | What it is |
|---|---|---|
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | ~25k | Anti-AI-slop design skill for Claude Code, Cursor, Codex. The most-starred slop project. |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | ~200 | Design rules against generic AI UI. |
| [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | ~410 | Design skill for coding agents. |
| [vibedesignlab/slopslap](https://github.com/vibedesignlab/slopslap) | ~31 | Parallel-inspection UI slop pipeline skill. |
| [Vinayak-Shukla-03/anti-ai-slop](https://github.com/Vinayak-Shukla-03/anti-ai-slop) | ~9 | UI and presentation de-slop skill. |

## Content blockers (YouTube, browser)

| Repo | Stars | What it is |
|---|---|---|
| [Override92/AiSList](https://github.com/Override92/AiSList) | ~150 | Filter list for AI slop YouTube channels. |
| [BMHeades/combatslop-yt](https://github.com/BMHeades/combatslop-yt) | ~32 | Browser extension detecting AI slop videos on YouTube. |
| [NikoboiNFTB/DeSlop](https://github.com/NikoboiNFTB/DeSlop) | ~13 | Blocklist-driven YouTube feed cleaner. |
| [adityabhandari781/Slop-Watch](https://github.com/adityabhandari781/Slop-Watch) | ~10 | Crowdsourced slop-detecting Chrome extension for YouTube. |

## Adjacent

- [sam-paech/antislop-sampler](https://github.com/sam-paech/antislop-sampler) - sampling-time suppression of slop phrases (ICLR 2026).
- [glacierphonk/naming](https://github.com/glacierphonk/naming) - metaphor-driven product naming that avoids AI slop.
- [drunkrhin0/antislop](https://github.com/drunkrhin0/antislop) - self-described "by slop for slop".
- [the-vibe-company/vibe-drift-tracker](https://github.com/The-Vibe-Company/vibe-drift-tracker) - VS Code extension tracking vibe-coding drift in real time.

## Where this library fits

The ecosystem is divided into skills (instructions for agents), lists (links), detectors (classifiers), and automation (CI). None of them publish the *pattern data itself* as a standalone, structured, machine-readable dataset. This library is that layer: `data/*.json` is the shared substrate a linter, a skill, or a detector can load, with the research and reference documentation alongside.

## Research sources

Full citations in `research.md`. Key sources: Liang et al. (Nature Human Behaviour, 2025), Science Advances 2025 (delve), Shaib et al. (arXiv:2509.19163), EQ-Bench Slop Score, Antislop (ICLR 2026), Wikipedia Signs of AI writing, Buffer 52M post analysis.
