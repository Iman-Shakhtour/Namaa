from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
src = root / "tmp" / "namaa-screens-20260919" / "namaa secreens"
dst = root / "assets" / "screenshots"

jobs = {
    "namaa-pos-current.webp": ("Screenshot 2026-09-19 130352.png", (0, 0, 1919, 720)),
    "namaa-inventory-current.webp": ("Screenshot 2026-09-19 130725.png", (0, 0, 1919, 520)),
    "namaa-profit-current.webp": ("Screenshot 2026-09-19 131053.png", (0, 0, 1901, 680)),
    "namaa-accounting-current.webp": ("Screenshot 2026-09-19 131416.png", (0, 0, 1918, 650)),
    "namaa-customers-current.webp": ("Screenshot 2026-09-19 131144.png", (0, 0, 1919, 610)),
    "namaa-sync-offline.webp": ("Screenshot 2026-09-16 010251.png", (0, 0, 1120, 170)),
    "namaa-sync-pending.webp": ("Screenshot 2026-09-16 010448.png", (0, 0, 1120, 170)),
    "namaa-sync-complete.webp": ("Screenshot 2026-09-16 010515.png", (0, 0, 1120, 170)),
}

for output, (source, crop) in jobs.items():
    image = Image.open(src / source).convert("RGB").crop(crop)
    image.save(dst / output, "WEBP", quality=86, method=6)
    print(output, image.size, (dst / output).stat().st_size)
