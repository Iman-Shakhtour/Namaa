from pathlib import Path

from PIL import Image


root = Path(__file__).resolve().parents[1]
source = root / "tmp" / "namaa-screens-20260919" / "namaa secreens"
target = root / "assets" / "screenshots"

files = {
    "Screenshot 2026-09-16 010251.png": "namaa-sync-offline-full.webp",
    "Screenshot 2026-09-16 010448.png": "namaa-sync-pending-full.webp",
    "Screenshot 2026-09-16 010515.png": "namaa-sync-complete-full.webp",
}

for source_name, target_name in files.items():
    with Image.open(source / source_name) as image:
        image.convert("RGB").save(target / target_name, "WEBP", quality=86, method=6)
        print(target_name, image.size)
