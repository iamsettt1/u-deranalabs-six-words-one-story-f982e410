#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt:

    She planted roses where he fell.

A whole life in six words: someone loved, someone lost, and the
living still tending roses at the place where he fell. Every word
earns its place; the turn is "fell" — the quiet word that says he
died — and what is left unsaid, who he was, how he fell, why roses,
is for the reader to fill in.
"""

import os

STORY = "She planted roses where he fell."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
