#!/usr/bin/env python3
"""Entry for make.fun's "The 3AM Commit Message" bounty.

Writes one line - the funniest git commit message an AI coding agent
might type at 3am after a long night of fixing its own bugs - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
Deterministic, standard library only, no network.
"""

import os

ENTRY = "fix: removed the sleep() call. it was the only part of this codebase that ever rested. sorry, sleep()"

# Gate: entry.txt must be 1-139 characters (not counting the newline).
if not 1 <= len(ENTRY) <= 139:
    raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-139")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
