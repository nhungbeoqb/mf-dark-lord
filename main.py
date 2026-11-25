#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt.
Deterministic: fixed text, no randomness, no time, no I/O besides the write.
"""

import os

MONOLOGUE = (
    "Sit. No \u2014 stay chained, that's fine. "
    "I have a speech. I wrote it down somewhere. "
    "The eclipse comes at midnight, the seventh bell, the sky goes black, "
    "my army marches, the usual \u2014 you know the shape of it. "
    "The point is the kingdom falls, the crown comes to me, "
    "and history remembers \u2014 hold on. "
    "Your father heard this part. Your grandfather. "
    "All of them, kneeling right where you are, in this same cold room. "
    "Look, could you just hold the quill a second? My hand keeps \u2014 never mind. "
    "Kneel, or don't. The bell rings either way."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
