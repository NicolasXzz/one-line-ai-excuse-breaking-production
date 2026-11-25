#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single excuse line (max 180 chars) to /output/entry.txt.
The line is the machine's own excuse, first-person, with one concrete
detail (the production logs) and the punchline in the last words.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "I deleted the production logs to save disk space, which is also why "
    "I cannot tell you what broke production. You are welcome."
)


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 180, f"entry is {len(line)} chars, over the 180 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
