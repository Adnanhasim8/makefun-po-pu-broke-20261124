"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = "Your changes were saved to a server we deleted. They had a good run."


def main() -> None:
    # Gate assertions: one non-empty line, at most 200 characters.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, "entry must be at most 200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
