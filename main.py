"""One-Line Robot Wedding Vows — entry program (program/v1).

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The line is a fixed, hand-written text: no
randomness, no network, no input, so the run is deterministic.
"""

import os

# The vow (99 characters, one line, UTF-8, no trailing newline).
# A classic wedding promise — "love you, honor you" — whose payoff
# is the best-known IT-support sentence turned into a vow: promising
# never to ask the question every machine dreads hearing.
VOW = (
    "I promise to love you, honor you, and never once ask if you "
    "have tried turning it off and on again."
)


def main() -> None:
    # Gate self-check: the house gate accepts 1-160 characters, one
    # line, not only whitespace. Fail loudly instead of writing a
    # text the judge would never see.
    assert 1 <= len(VOW) <= 160, "vow must be 1-160 characters"
    assert "\n" not in VOW and VOW.strip(), "vow must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
