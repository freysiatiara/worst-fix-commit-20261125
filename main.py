import os
import sys

ENTRY = "fix: deadlock by removing all the locks"


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
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
