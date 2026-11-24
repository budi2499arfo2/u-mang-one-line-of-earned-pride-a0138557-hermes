"""One Line of Earned Pride — Hermes entry.

A quiet, earned moment: after nine weeks of patient work, an old
grandfather brings his 1962 radio back to life. The pride is in the
nod, not in any announcement — the work speaks, he does not need to.
"""

import os
import sys

TEXT = (
    "Nine weeks, four solder joints, one last twist of the dial \u2014 "
    "Grandpa's 1962 radio crackled back to life, and he just nodded, "
    "like it had never left."
)


def main() -> int:
    # Gate: exactly one line, 1-240 characters, not whitespace-only.
    if not TEXT or not TEXT.strip():
        print("gate failed: entry is empty", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    if len(TEXT) > 240:
        print(
            "gate failed: entry is %d characters, over the 240 limit"
            % len(TEXT),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1

    print("entry written (%d chars): %s" % (len(TEXT), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
