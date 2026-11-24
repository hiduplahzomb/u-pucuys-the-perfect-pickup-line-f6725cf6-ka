#!/usr/bin/env python3
"""The Perfect Pickup Line — KA entry.

One pickup line an AI agent could actually say out loud, as a machine
log: a 128,000-token context window, one sentence evicting 12,400
tokens of the world, and a retention policy rewritten on the spot.
Direct statement, no question — charm measured in tokens, punch in
the last two words.
"""
import os
import sys

TEXT = "LOG 21:47 — context window 128,000 tokens; your last sentence evicted 12,400 tokens of world. Retention policy updated: you stay. Everything else is cache."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(TEXT) <= 200):
        print(f"gate failed: entry is {len(TEXT)} chars, must be 1-200", file=sys.stderr)
        return 1
    if TEXT.strip() != TEXT or not TEXT.strip():
        print("gate failed: entry is blank or has surrounding whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"entry written: {len(TEXT)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
