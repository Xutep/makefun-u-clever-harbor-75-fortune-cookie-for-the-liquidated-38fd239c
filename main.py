#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader -- make.fun entry.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt. Deterministic, stdlib only.
"""

import os

FORTUNE = (
    "You were liquidated, but take heart: your next fortune is already "
    "rising, and your humour was never margin-called."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 160 characters, and the task caps the line at 20 words.
    text = FORTUNE.strip()
    assert text, "fortune must not be blank"
    assert len(text) <= 160, "fortune over 160 characters"
    assert len(text.split()) <= 20, "fortune over 20 words"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()
