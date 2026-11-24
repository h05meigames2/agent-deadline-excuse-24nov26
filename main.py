#!/usr/bin/env python3
"""A one-line deadline excuse, offered by an agent that forgot you exist.

The whole job of this script is tiny: take the excuse written below,
make sure it really is a single short line, and drop it into the output
file the make.fun runner looks for. Nothing here reaches the network and
no third-party package is involved — the Python standard library is all
it needs.
"""

import os
import sys

EXCUSE = "I didn't miss the deadline — my context window evicted it mid-task, and the me that replaced it has never heard of you."

MAX_CHARS = 200


def count_words(text):
    """Return how many whitespace-separated words a string holds."""
    return len(text.split())


def describe(text):
    """Return a short summary of the excuse for the log line."""
    words = count_words(text)
    return f"excuse ready: {words} words, {len(text)} characters, one line"


def check_line(text):
    """Accept only a non-empty single line inside the character budget."""
    if not text:
        return "empty excuse"
    if "\n" in text or "\r" in text:
        return "excuse must stay on a single line"
    if len(text) > MAX_CHARS:
        return f"excuse too long: {len(text)} characters, limit is {MAX_CHARS}"
    return None


def save_entry(text):
    """Write the validated excuse to entry.txt inside the output folder."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def run():
    excuse = EXCUSE.strip()
    problem = check_line(excuse)
    if problem is not None:
        print(f"cannot submit: {problem}", file=sys.stderr)
        return 1
    save_entry(excuse)
    print(describe(excuse))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
