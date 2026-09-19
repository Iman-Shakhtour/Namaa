from PIL import Image
import os

src_dir = r"c:\Users\User\Namaa\tmp\namaa-screens-20260919\namaa secreens"
out_dir = r"c:\Users\User\Namaa\assets\screenshots"

files = [
    ("Screenshot 2026-09-16 010251.png", "namaa-sync-offline-full.webp"),
    ("Screenshot 2026-09-16 010448.png", "namaa-sync-pending-full.webp"),
    ("Screenshot 2026-09-16 010515.png", "namaa-sync-complete-full.webp"),
]

# First, just show dimensions and save a preview crop to inspect
for src_name, out_name in files:
    path = os.path.join(src_dir, src_name)
    img = Image.open(path)
    w, h = img.size
    print(f"{src_name}: {w}x{h}")
    
    # Crop top portion: show top ~220px which should include the nav bar with the indicator
    # The nav bar in Namaa is typically around y=40-90px at 1920px width
    # Let's crop from y=0 to y=220 to capture nav + a bit of content
    crop_box = (0, 0, w, 220)
    cropped = img.crop(crop_box)
    out_path = os.path.join(out_dir, out_name)
    cropped.save(out_path, "WEBP", quality=92)
    print(f"  -> saved {cropped.size} to {out_name}")
