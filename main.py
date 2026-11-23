#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line, deterministically, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Standard library only. Running it twice produces byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "My microwave beeps five times when the food is done, like it's "
    "personally offended I took more than three seconds to open the door."
)


def main() -> None:
    # Gate mirror: the entry must be one line of 1-200 characters,
    # not only whitespace. Fail loudly here rather than shipping
    # an invalid entry.
    stripped = LINE.strip()
    if not stripped or "\n" in stripped or len(stripped) > 200:
        raise ValueError("roast line violates the 1-200 character, one-line gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
    # Deterministic by construction: LINE is a constant, the output
    # path depends only on the environment, and nothing here reads
    # the clock, randomness, or the network.
    print(f"wrote entry.txt ({len(stripped)} characters)")


if __name__ == "__main__":
    main()
