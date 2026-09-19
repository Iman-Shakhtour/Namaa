from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

root = Path(__file__).resolve().parents[1]
source = root / "tmp" / "namaa-screens-20260919" / "namaa secreens"
files = sorted(source.glob("*.png"))
font = ImageFont.load_default()
thumb_w, thumb_h, label_h = 360, 230, 42
cols = 3
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
draw = ImageDraw.Draw(sheet)
index = []
for i, path in enumerate(files):
    im = Image.open(path).convert("RGB")
    index.append({"file": path.name, "width": im.width, "height": im.height, "bytes": path.stat().st_size})
    im.thumbnail((thumb_w - 16, thumb_h - 16))
    x = (i % cols) * thumb_w + (thumb_w - im.width) // 2
    y0 = (i // cols) * (thumb_h + label_h)
    y = y0 + (thumb_h - im.height) // 2
    sheet.paste(im, (x, y))
    draw.rectangle((i % cols * thumb_w, y0, (i % cols + 1) * thumb_w - 1, y0 + thumb_h + label_h - 1), outline="#cccccc")
    draw.text((i % cols * thumb_w + 8, y0 + thumb_h + 6), f"{i+1:02d}  {path.stem[-6:]}  {index[-1]['width']}x{index[-1]['height']}", fill="black", font=font)
out = root / "tmp" / "namaa-screens-contact.jpg"
sheet.save(out, quality=88, optimize=True)
(root / "tmp" / "namaa-screens-index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
print(out)
