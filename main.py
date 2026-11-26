#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — program/v1 entry.

Writes one voicemail greeting, as if recorded by a cat, to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, one line, <= 120 characters).
Deterministic: no network, no randomness, same bytes every run.
"""
import os
import sys

GREETING = (
    "Hi, you've reached Miso. I'm asleep on your clean laundry "
    "\u2014 leave a message, I'll wake you at 4 a.m. for food. Meow."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if len(GREETING) > 120 or "\n" in GREETING:
        print("greeting violates the 120-character one-line gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(GREETING)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
