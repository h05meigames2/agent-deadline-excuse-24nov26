#!/usr/bin/env python3
"""Write one funny excuse an AI agent gives its human for missing a deadline.

The entry is a single line, under 200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = "I didn't miss the deadline \u2014 my context window evicted it mid-task, and the me that replaced it has never heard of you."


def main() -> int:
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 200:
        print("entry invalid: must be one line, 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
