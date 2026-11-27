#!/usr/bin/env python3
"""detectorcheck - measure the text properties detectors score after slop is gone.

slopcheck answers "does this text contain known slop patterns". Detectors answer
a different question: "does this text look like a model wrote it". A rewrite that
clears every high and critical slop hit can leave the rhythm untouched, and the
rhythm is part of what detectors score.

This script measures the rhythm and runs slopcheck at the medium floor, which is
where the detector-facing structures (spec-sheet, sentence-band, paragraph-band,
register) live.

Usage:
  python3 detectorcheck.py draft.txt
  python3 detectorcheck.py --json draft.txt
  python3 detectorcheck.py --strict draft.txt      # warnings become failures

Exit code 1 when a check fails, or when --strict is set and a warning fires.
Zero-dependency Python 3. It reuses slopcheck.py in the same directory.
"""
import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import slopcheck as sc

CONTRACTION = re.compile(r"\b\w+(?:'|\u2019)(?:t|s|re|ve|ll|d|m)\b", re.IGNORECASE)

# Defaults come from the library's November 2026 detector validation:
# Published detector guidance reports human prose at burstiness 0.6-1.2 and model output at 0.2-0.4.
# Wire prose sits near mean 26 words per sentence with 30-45 word anchors.
BURSTINESS_FAIL = 0.40
BURSTINESS_WARN = 0.50
MEAN_LENGTH_WARN = 18.0
LONG_SENTENCE_WORDS = 30
LONG_SENTENCE_MIN = 1
PARAGRAPH_BURSTINESS_WARN = 0.45
CONTRACTION_MIN_PER_1K = 5.0

DETECTOR_FAMILIES = {"spec-sheet", "sentence-band", "paragraph-band", "register"}


def body_text(text):
    if "\n---\n" in text:
        text = text.split("\n---\n", 1)[1]
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"^>\s*\*\*Source.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^#+ .*$", "", text, flags=re.MULTILINE)
    return text.replace("**", "")


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip().split()) > 2]


def paragraphs(text):
    parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if len(p.strip().split()) > 10]


def measure(text):
    text = body_text(text)
    sents = sentences(text)
    paras = paragraphs(text)
    lengths = [len(s.split()) for s in sents]
    plengths = [len(p.split()) for p in paras]
    words = len(text.split())
    if not lengths:
        return None
    mean = statistics.mean(lengths)
    sd = statistics.pstdev(lengths)
    contractions = len(CONTRACTION.findall(text))
    return {
        "words": words,
        "sentences": len(lengths),
        "mean_sentence_length": round(mean, 2),
        "max_sentence_length": max(lengths),
        "min_sentence_length": min(lengths),
        "burstiness": round(sd / mean, 3) if mean else 0.0,
        "long_sentences": sum(1 for n in lengths if n >= LONG_SENTENCE_WORDS),
        "paragraphs": len(plengths),
        "mean_paragraph_length": round(statistics.mean(plengths), 2) if plengths else 0.0,
        "paragraph_burstiness": (
            round(statistics.pstdev(plengths) / statistics.mean(plengths), 3)
            if len(plengths) > 2 and statistics.mean(plengths)
            else 0.0
        ),
        "contractions": contractions,
        "contractions_per_1k": round(contractions / words * 1000, 1) if words else 0.0,
    }


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    strict = "--strict" in args
    files = [a for a in args if not a.startswith("-")]
    if not files:
        print(__doc__)
        return 2

    payload = []
    failed = False
    warned = False

    for fp in files:
        text = Path(fp).read_text(errors="replace")
        m = measure(text)
        if m is None:
            print(f"== {fp} ==\n  no scannable sentences")
            failed = True
            continue

        hits = sc.scan(
            text,
            sc.build_matchers(sc.load_patterns()),
            sc.SEVERITY_RANK["medium"],
            1,
        )
        detector_hits = [h for h in hits if h.get("family") in DETECTOR_FAMILIES]

        checks = []
        if m["burstiness"] < BURSTINESS_FAIL:
            checks.append(("FAIL", f"burstiness {m['burstiness']} below {BURSTINESS_FAIL}"))
            failed = True
        elif m["burstiness"] < BURSTINESS_WARN:
            checks.append(("WARN", f"burstiness {m['burstiness']} below target {BURSTINESS_WARN}"))
            warned = True

        if m["mean_sentence_length"] < MEAN_LENGTH_WARN:
            checks.append(("WARN", f"mean sentence length {m['mean_sentence_length']} below {MEAN_LENGTH_WARN}"))
            warned = True

        if m["long_sentences"] < LONG_SENTENCE_MIN:
            checks.append(("WARN", f"no sentence reaches {LONG_SENTENCE_WORDS} words"))
            warned = True

        if m["paragraphs"] > 2 and m["paragraph_burstiness"] < PARAGRAPH_BURSTINESS_WARN:
            checks.append(("WARN", f"paragraph burstiness {m['paragraph_burstiness']} below {PARAGRAPH_BURSTINESS_WARN}"))
            warned = True

        if m["contractions_per_1k"] < CONTRACTION_MIN_PER_1K:
            checks.append(("WARN", f"contractions {m['contractions_per_1k']} per 1k words below {CONTRACTION_MIN_PER_1K}"))
            warned = True

        for h in detector_hits:
            checks.append(("FAIL", f"{h['pattern']} x{h['count']} ({h['severity']}, {h['family']})"))
            failed = True

        payload.append({"file": fp, "metrics": m, "checks": checks, "hits": hits})

        if not as_json:
            print(f"== {fp} ==")
            print(
                "  metrics: "
                f"{m['words']} words, {m['sentences']} sentences, "
                f"mean {m['mean_sentence_length']}, max {m['max_sentence_length']}, "
                f"burstiness {m['burstiness']}, long {m['long_sentences']}, "
                f"paragraphs {m['paragraphs']} (burstiness {m['paragraph_burstiness']}), "
                f"contractions {m['contractions_per_1k']}/1k"
            )
            if not checks:
                print("  PASS: rhythm and medium-floor patterns clear")
            for level, msg in checks:
                print(f"  {level}: {msg}")

    if as_json:
        print(json.dumps(payload, indent=2))

    if strict and warned:
        return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
