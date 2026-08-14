#!/usr/bin/env python3
"""slopcheck - scan text against the AI Slop Library pattern data.

Zero-dependency Python 3. Loads every data/*.json file in this repo and
reports words, phrases, openers, and punctuation tells with severity,
example, and fix.

Usage:
  python3 slopcheck.py file.txt [file2.txt ...]
  cat text.txt | python3 slopcheck.py -
  python3 slopcheck.py -s high file.txt      # only severity >= high
  python3 slopcheck.py --json file.txt       # machine-readable output
  python3 slopcheck.py --min-count 2 file.txt  # only patterns hit >= 2x

Exit code 1 when any hit survives the severity/count filters.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}

__version__ = (ROOT / "VERSION").read_text().strip()


def load_patterns():
    patterns = []  # (kind, match_text, severity, example, fix, family)
    for path in sorted(DATA_DIR.glob("*.json")):
        if path.name == "schema.json":
            continue
        with open(path) as f:
            data = json.load(f)
        items = (
            data.get("words")
            or data.get("phrases")
            or data.get("openers")
            or data.get("structures")
            or data.get("punctuation")
            or data.get("fingerprint")
            or []
        )
        for it in items:
            text = (
                it.get("word")
                or it.get("phrase")
                or it.get("opener")
                or it.get("name")
                or it.get("mark")
            )
            if not text or not it.get("severity"):
                continue
            patterns.append(
                (
                    data["category"],
                    text,
                    it.get("severity", "low"),
                    it.get("example", ""),
                    it.get("fix", ""),
                    it.get("family", ""),
                )
            )
    return patterns


def build_matchers(patterns):
    matchers = []  # (compiled_regex, pattern_meta)
    for kind, text, severity, example, fix, family in patterns:
        if kind == "punctuation":
            continue  # punctuation handled separately
        escaped = re.escape(text)
        escaped = escaped.replace(r"\*", r"\w*").replace(r"\?", r"\w*")
        parts = [p for p in escaped.split(r"\w*") if p]
        if not parts:
            continue
        regex = r"\b" + r"[^\s]*".join(parts) + r"\b"
        try:
            matchers.append((re.compile(regex, re.IGNORECASE), (kind, text, severity, example, fix, family)))
        except re.error:
            continue
    return matchers


PUNCT_MATCHERS = [
    (re.compile(r"[\u2014\u2015]"), "punctuation", "em dash"),
    (re.compile(r"[.!?]\.\.\.|\.\.\."), "punctuation", "ellipsis trail"),
    (re.compile(r"!!+|!\?+"), "punctuation", "exclamation escalation"),
    (re.compile(r"[^.!?\n]::"), "punctuation", "colon reveal"),
    (re.compile(r"\b[A-Z][a-z]+[;][a-z]"), "punctuation", "semicolon dependence"),
]


def scan(text, matchers, min_severity_idx, min_count):
    hits = []
    for regex, meta in matchers:
        matches = regex.findall(text)
        if len(matches) >= min_count:
            kind, name, severity, example, fix, family = meta
            if SEVERITY_RANK.get(severity, 3) <= min_severity_idx:
                hits.append(
                    {
                        "category": kind,
                        "pattern": name,
                        "count": len(matches),
                        "severity": severity,
                        "example": example,
                        "fix": fix,
                        "family": family,
                    }
                )
    for regex, kind, name in PUNCT_MATCHERS:
        matches = regex.findall(text)
        if len(matches) >= min_count:
            hits.append(
                {
                    "category": "punctuation",
                    "pattern": name,
                    "count": len(matches),
                    "severity": "medium" if name != "em dash" else "critical",
                    "example": "",
                    "fix": "",
                    "family": "punctuation",
                }
            )
    hits.sort(key=lambda h: (SEVERITY_RANK.get(h["severity"], 3), -h["count"]))
    return hits


def main():
    args = [a for a in sys.argv[1:]]
    min_severity = "low"
    as_json = False
    min_count = 1
    files = []
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-s", "--severity"):
            min_severity = args[i + 1]
            i += 2
        elif a == "--json":
            as_json = True
            i += 1
        elif a == "--min-count":
            min_count = int(args[i + 1])
            i += 2
        elif a in ("-v", "--version"):
            print(f"slopcheck {__version__}")
            return 0
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            files.append(a)
            i += 1

    if min_severity not in SEVERITY_RANK:
        print(f"bad severity: {min_severity} (use critical/high/medium/low)", file=sys.stderr)
        return 2

    matchers = build_matchers(load_patterns())
    total = 0
    for fp in files or ["-"]:
        text = sys.stdin.read() if fp == "-" else Path(fp).read_text(errors="replace")
        hits = scan(text, matchers, SEVERITY_RANK[min_severity], min_count)
        total += len(hits)
        if as_json:
            print(json.dumps({"file": fp, "hits": hits}, indent=2))
        else:
            print(f"== {fp} ==")
            if not hits:
                print("  clean")
            for h in hits:
                print(f"  [{h['severity']}] {h['pattern']} x{h['count']} ({h['category']})")
                if h.get("fix"):
                    print(f"      fix: {h['fix']}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
