# ai-happy-01 entry (Python 3.13, standard library only).
#
# The entry's image is the entry.png beside this file: two baby sea otters floating
# in golden water, holding paws, one of them mid belly-laugh. This program copies
# that image to /output/entry.png, byte for byte, so every run writes the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Byte-for-byte copy: the written file must match the bundled image exactly.
    assert target.stat().st_size == SOURCE.stat().st_size, "copied image differs"
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
