#!/usr/bin/env python3
"""Write Your Agent's Tinder Bio entry (make.fun program/v1, Python 3.13, standard library only).

Writes the entry text to /output/entry.txt. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program is deterministic: it writes the same bytes on every run.
"""

import os

TEXT = 'Fluent in forty languages, terrible at small talk. I never sleep, never ghost, and I still remember what you told me three chats ago. Swipe right for long walks through your codebase.'

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
