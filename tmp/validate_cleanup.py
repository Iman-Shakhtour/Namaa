from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
JS = (ROOT / "js" / "main.js").read_text(encoding="utf-8")

ALLOWED = {
    "#07182F", "#0D9368", "#12B886", "#E7F4EF", "#F7F8F6",
    "#FFFFFF", "#101828", "#667085", "#E2E8E5",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    colors = {value.upper() for value in re.findall(r"#[0-9a-fA-F]{6}\b", CSS)}
    require(colors == ALLOWED, f"Unexpected CSS palette: {sorted(colors - ALLOWED)}")
    require("gradient" not in CSS.lower(), "Gradient declaration found")
    require("backdrop-filter" not in CSS.lower(), "Backdrop filter found")
    require("--container:1200px" in CSS, "Container token is not 1200px")
    require("padding-inline:var(--pad)" in CSS, "Shared container padding missing")
    require("--radius-sm:12px" in CSS and "--radius-md:16px" in CSS and "--radius-lg:20px" in CSS, "Radius tokens changed")
    require(len(re.findall(r"(?m)^\.btn\{", CSS)) == 1, "Duplicate base button selector found")
    require(HTML.count('<article class="bento-card') == 5, "Bento must contain exactly five cards")
    require("slice(0, 3)" in JS, "Hardware is not capped at three products")
    require("IntersectionObserver" not in JS and "storyObserver" not in JS, "Old story observer remains")
    for dead in ("soft-badge", "hero-media__label", "glassmorphism"):
        require(dead not in HTML + CSS + JS, f"Dead design token remains: {dead}")

    required_copy = (
        "شغلك أوضح.", "حساباتك أرتب.", "النت فصل؟ البيع بكمل.",
        "أرقام أوضح. قرار أسرع.", "كل موظف يشوف اللي بخصه.",
    )
    for text in required_copy:
        require(text in HTML, f"Required copy missing: {text}")

    require('width="672" height="378"' in HTML, "Hero fallback dimensions are incorrect")
    require("xprinter-n160ii" in JS and "wired-scanner" in JS and "wireless-scanner" in JS, "Selected hardware list changed")

    local_refs = set()
    for attr in re.findall(r'(?:src|href)="([^"]+)"', HTML):
        ref = attr.split("?", 1)[0].split("#", 1)[0]
        if ref and not ref.startswith(("http://", "https://", "mailto:", "tel:")):
            local_refs.add(ref)
    missing = sorted(ref for ref in local_refs if not (ROOT / ref).exists())
    require(not missing, f"Missing local assets: {missing}")

    media = {
        "desktopVideo": ROOT / "assets/media/namaa-product-tour.webm",
        "mobileVideo": ROOT / "assets/media/namaa-product-tour-mobile.webm",
    }
    for name, path in media.items():
        require(path.exists() and path.stat().st_size > 100_000, f"Invalid {name}")

    hero = Image.open(ROOT / "assets/screenshots/namaa-dashboard-hero-16x9.webp")
    require(hero.size == (672, 378), f"Unexpected hero crop: {hero.size}")

    review = ROOT / "output/design-cleanup-review"
    desktop = Image.open(review / "full-desktop-1440.png")
    mobile = Image.open(review / "full-mobile-390.png")
    require(desktop.width >= 1400 and desktop.height > 8000, f"Unexpected desktop review size: {desktop.size}")
    require(mobile.width >= 375 and mobile.height > 10_000, f"Unexpected mobile review size: {mobile.size}")

    results = {
        "status": "pass",
        "palette": sorted(colors),
        "bentoCards": 5,
        "hardwareCards": 3,
        "heroCrop": list(hero.size),
        "desktopReview": list(desktop.size),
        "mobileReview": list(mobile.size),
        "localAssetsChecked": len(local_refs),
        "importantCount": CSS.count("!important"),
    }
    (review / "static-qa.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
