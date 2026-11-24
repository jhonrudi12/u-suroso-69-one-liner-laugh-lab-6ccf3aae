#!/usr/bin/env python3
"""One-Liner Laugh Lab -- entry program.

Writes one line -- the excuse a robot vacuum gives after eating
a sock -- to /output/entry.txt for the judge to read. Standard
library only, no network, no input files, deterministic output:
the same line, the same bytes, every run.
"""

import os

LINE = (
    "I didn't eat your sock \u2014 I adopted it. It lives in my dustbin "
    "now, rent-free, and has never looked happier."
)

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and the brief requires a single short funny line.
    """
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
