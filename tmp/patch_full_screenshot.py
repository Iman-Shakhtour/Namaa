from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "output" / "design-cleanup-review"
BASE = REVIEW / "full-desktop-1440.png"
META = REVIEW / "patches" / "meta.json"


def main() -> None:
    base = Image.open(BASE).convert("RGB")
    metadata = json.loads(META.read_text(encoding="utf-8"))

    for group in metadata:
        viewport = Image.open(group["path"]).convert("RGB")
        scale_x = viewport.width / group["innerWidth"]
        scale_y = viewport.height / group["innerHeight"]

        for rect in group["rects"]:
            left = math.floor(rect["left"] * scale_x)
            top = math.floor(rect["top"] * scale_y)
            right = math.ceil((rect["left"] + rect["width"]) * scale_x)
            bottom = math.ceil((rect["top"] + rect["height"]) * scale_y)

            patch = viewport.crop((left, top, right, bottom))
            page_left = left
            page_top = round((group["scrollY"] + rect["top"]) * scale_y)
            base.paste(patch, (page_left, page_top))

    base.save(BASE, optimize=True)
    print(f"patched {BASE} ({base.width}x{base.height})")


if __name__ == "__main__":
    main()
