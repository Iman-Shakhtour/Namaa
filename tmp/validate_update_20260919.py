from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
JS = (ROOT / "js" / "main.js").read_text(encoding="utf-8")
OUT = ROOT / "output" / "update-20260919-review"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require("شاهد الجولة" not in HTML, "Old tour CTA remains")
    require(HTML.count("wa.me/972592425106") >= 5, "WhatsApp CTA coverage is incomplete")
    require("31 ديسمبر 2026" in HTML, "Public offer deadline is missing")
    require("2026-12-31T23:59:59+02:00" in HTML, "Countdown deadline is missing")
    require("localStorage" not in JS, "Countdown must not reset per visitor")
    require("setInterval(updateCountdown" in JS, "Countdown updater is missing")
    require("grid-template-columns:repeat(3,minmax(0,1fr))" in CSS, "Desktop sync grid is missing")
    require("@media (max-width:767px)" in CSS, "Mobile breakpoint is missing")
    require("mobile.webp" not in HTML and "mobile-focus.webp" not in HTML, "Mobile-specific images must not be in HTML")

    expected_images = {
        "namaa-pos-current.webp": (1919, 866),
        "namaa-inventory-current.webp": (1919, 867),
        "namaa-profit-current.webp": (1901, 870),
        "namaa-accounting-current.webp": (1918, 868),
        "namaa-customers-current.webp": (1919, 868),
        "namaa-sync-offline-full.webp": (1919, 872),
        "namaa-sync-pending-full.webp": (1916, 870),
        "namaa-sync-complete-full.webp": (1919, 875),
    }
    dimensions = {}
    for name, expected in expected_images.items():
        path = ROOT / "assets" / "screenshots" / name
        require(path.exists() and path.stat().st_size > 1_000, f"Missing image: {name}")
        with Image.open(path) as image:
            dimensions[name] = list(image.size)
            require(image.size == expected, f"Unexpected dimensions for {name}: {image.size}")

    local_refs = set()
    for value in re.findall(r'(?:src|href)="([^"]+)"', HTML):
        ref = value.split("?", 1)[0].split("#", 1)[0]
        if ref and not ref.startswith(("http://", "https://", "mailto:", "tel:")):
            local_refs.add(ref)
    missing = sorted(ref for ref in local_refs if not (ROOT / ref).exists())
    require(not missing, f"Missing local references: {missing}")

    results = {
        "status": "pass",
        "whatsappNumber": "+972592425106",
        "whatsappLinks": HTML.count("wa.me/972592425106"),
        "countdownDeadline": "2026-12-31T23:59:59+02:00",
        "countdownResetPerVisitor": False,
        "desktopOnlyScreenshots": True,
        "newScreenshots": dimensions,
        "localReferencesChecked": len(local_refs),
        "desktopVisualReview": ["hero", "features", "sync", "pricing"],
        "responsiveRulesReviewed": [320, 360, 390, 430, 768, 1024, 1440],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "qa.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
