from pathlib import Path
from PIL import Image
import json

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "output" / "design-cleanup-review"


def stitch(manifest_name, output_name, sticky_css=74):
    manifest_path = REVIEW / manifest_name
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = []
    for item in data["parts"]:
        path = Path(item["file"])
        if path.exists():
            entries.append((round(item["y"]), path))
    entries.sort(key=lambda pair: pair[0])
    dedup = []
    for y, path in entries:
        if dedup and abs(y - dedup[-1][0]) < 4:
            dedup[-1] = (y, path)
        else:
            dedup.append((y, path))
    with Image.open(dedup[0][1]) as first:
        width = first.width
        shot_height = first.height
        bottom_color = first.convert("RGB").getpixel((width // 2, shot_height - 1))
    page_height = data["doc"]["height"]
    canvas = Image.new("RGB", (width, page_height), bottom_color)
    for index, (y, path) in enumerate(dedup):
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            crop_top = 0 if index == 0 and y == 0 else sticky_css
            piece = rgb.crop((0, crop_top, rgb.width, rgb.height))
            canvas.paste(piece, (0, y + crop_top))
    canvas.save(REVIEW / output_name, "PNG", optimize=True)
    print(output_name, canvas.size, len(dedup))


stitch("parts4/mobile-manifest.json", "full-mobile-390.png")
stitch("desktop-parts/desktop-manifest.json", "full-desktop-1440.png")
