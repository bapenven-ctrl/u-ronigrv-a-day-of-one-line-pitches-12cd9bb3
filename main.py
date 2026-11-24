#!/usr/bin/env python3
"""A Day of One-Line Pitches (make.fun).

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Deterministic, standard library only, no network.
"""
import os

TEXT = "Tell the agent about the plant chart on your fridge and tomorrow it will ping you before the basil dies, then ask what else in your kitchen needs saving."

OUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
