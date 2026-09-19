from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
source = root / "tmp" / "namaa-screens-20260919" / "namaa secreens"
names = [
    "Screenshot 2026-09-16 010251.png",
    "Screenshot 2026-09-16 010448.png",
    "Screenshot 2026-09-16 010515.png",
    "Screenshot 2026-09-19 130315.png",
    "Screenshot 2026-09-19 130352.png",
]
canvas = Image.new("RGB", (960, len(names) * 470), "white")
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default()
for i, name in enumerate(names):
    im = Image.open(source / name).convert("RGB")
    im.thumbnail((940, 420))
    y = i * 470
    canvas.paste(im, ((960 - im.width) // 2, y))
    draw.text((12, y + 430), name, fill="black", font=font)
out = root / "tmp" / "selected-screens.jpg"
canvas.save(out, quality=92)
print(out)
