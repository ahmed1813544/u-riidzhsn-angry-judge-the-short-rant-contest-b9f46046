#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest -- entry program.

Writes one short, funny rant about a small everyday annoyance to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output). The text is fixed,
so the output is deterministic: byte-identical on every run.
Standard library only.
"""

import os

RANT = (
    "Self-checkout machine, I scanned the milk. I bagged the milk. "
    "Then you screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd "
    "smuggled in a hostage. You are a scale with a speaker and a god "
    "complex. I came to buy bread, not to be interrogated by a "
    "toaster with trust issues."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = RANT.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError("rant must be 1-400 characters, got %d" % len(text))
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
