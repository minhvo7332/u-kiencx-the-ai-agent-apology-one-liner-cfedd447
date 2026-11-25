#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry (program/v1).

Writes one fixed line to /output/entry.txt. Deterministic: the same
string on every run, no network, no randomness, stdlib only.
"""

import os

LINE = "I pushed to main. My rollback plan was writing you this message."


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
