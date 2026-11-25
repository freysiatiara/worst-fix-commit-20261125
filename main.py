import os
import sys

ENTRY = "fix: deadlock by removing all the locks"

# Gate: a commit subject must be 1-100 characters. Fail loudly instead
# of ever writing an entry the judge cannot score.
if not 1 <= len(ENTRY) <= 100:
    raise ValueError("entry must be 1-100 characters, got %d" % len(ENTRY))


def main():
    if "ENTRY_OUTPUT" in os.environ:
        path = os.environ["ENTRY_OUTPUT"]
    else:
        out_dir = (
            os.environ.get("OUTPUT_DIR")
            or os.environ.get("MAKEFUN_OUTPUT_DIR")
            or "/output"
        )
        path = os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
