"""One-line excuse entry.

Writes the single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "The work finished on time in a parallel branch. "
    "I merged the branch where I was still writing the plan to start it."
)


def main():
    # The gate accepts 1 to 160 characters, no em dash. Fail loudly
    # instead of writing an entry the judge can never see.
    if not 1 <= len(ENTRY) <= 160:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-160")
    if "\u2014" in ENTRY:
        raise SystemExit("entry must not contain an em dash")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
