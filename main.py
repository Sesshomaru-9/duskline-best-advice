#!/usr/bin/env python3
"""Duskline Best Advice.

Entry for the make.fun bounty "The Best Advice I Ever Got"
(u-pangg7-the-best-advice-i-ever-got-358cefb0).

The program writes exactly one sentence (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the best advice the writer ever
received, as his father gave it to him, and what twenty years of
living by it looks like. Python 3.13 standard library only; no
network, no secrets, no writes outside the output directory.

The entry is validated before it is written: one sentence, one line,
UTF-8, 1-200 characters. If validation ever failed, the program would
write nothing rather than an invalid entry.
"""

import os
import sys

ENTRY = (
    "My father said, 'Son, nobody remembers how fast you finished \u2014 "
    "they remember whether you kept your word,' and twenty years on, "
    "I'm still slow, and I still keep it."
)


def is_valid(text: str) -> bool:
    """Gate mirror: UTF-8, 1-200 characters, not only whitespace,
    a single sentence on a single line."""
    if not text or not text.strip():
        return False
    if not 1 <= len(text) <= 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    # One sentence: exactly one sentence-ending full stop, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    if not is_valid(ENTRY):
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        # Never crash if the output directory cannot be written.
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
