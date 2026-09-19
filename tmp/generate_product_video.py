from pathlib import Path
import math
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tmp" / "pydeps"))
from PIL import Image
import imageio_ffmpeg

SHOTS = ROOT / "assets" / "screenshots"
OUT = ROOT / "assets" / "media"
OUT.mkdir(parents=True, exist_ok=True)
FPS = 24
SLIDE = 1.35
FADE = .26


def cover(im, width, height, progress, reverse):
    base = max(width / im.width, height / im.height)
    scale = base * (1 + .025 * progress)
    resized = im.resize((math.ceil(im.width * scale), math.ceil(im.height * scale)), Image.Resampling.LANCZOS)
    travel_x = max(0, resized.width - width)
    travel_y = max(0, resized.height - height)
    eased = progress * progress * (3 - 2 * progress)
    x = round(travel_x * ((1 - eased) if reverse else eased))
    y = round(travel_y / 2)
    return resized.crop((x, y, x + width, y + height))


def encode(name, width, height, files):
    images = [Image.open(SHOTS / item).convert("RGB") for item in files]
    total_frames = round(FPS * SLIDE * len(images))
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    target = OUT / name
    command = [
        ffmpeg, "-y", "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{width}x{height}", "-r", str(FPS), "-i", "-", "-an",
        "-c:v", "libvpx-vp9", "-crf", "34", "-b:v", "0", "-deadline", "good",
        "-cpu-used", "2", "-row-mt", "1", "-pix_fmt", "yuv420p", str(target)
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    try:
        for frame_no in range(total_frames):
            seconds = frame_no / FPS
            position = seconds / SLIDE
            index = int(position) % len(images)
            local = position - int(position)
            current = cover(images[index], width, height, local, index % 2 == 0)
            fade_start = (SLIDE - FADE) / SLIDE
            if local > fade_start:
                alpha = (local - fade_start) / (1 - fade_start)
                alpha = alpha * alpha * (3 - 2 * alpha)
                nxt = (index + 1) % len(images)
                next_frame = cover(images[nxt], width, height, 0, nxt % 2 == 0)
                current = Image.blend(current, next_frame, alpha)
            process.stdin.write(current.tobytes())
        process.stdin.close()
        error = process.stderr.read().decode("utf-8", "replace")
        code = process.wait()
        if code:
            raise RuntimeError(error[-4000:])
    finally:
        for image in images:
            image.close()
    print(name, target.stat().st_size)


with Image.open(SHOTS / "namaa-dashboard-desktop.webp") as source:
    poster = source.crop((1244, 0, 1916, 378))
    poster.save(SHOTS / "namaa-dashboard-hero-16x9.webp", "WEBP", quality=88, method=6)

with Image.open(SHOTS / "namaa-rbac-users-public.webp") as source:
    permissions_focus = source.crop((745, 0, 1901, 650))
    permissions_focus.save(SHOTS / "namaa-rbac-focus.webp", "WEBP", quality=88, method=6)

encode("namaa-product-tour.webm", 1200, 675, [
    "namaa-dashboard-hero.webp",
    "namaa-pos-focus.webp",
    "namaa-inventory-focus.webp",
    "namaa-profit-focus.webp",
    "namaa-rbac-focus.webp",
])
encode("namaa-product-tour-mobile.webm", 540, 720, [
    "namaa-dashboard-mobile.webp",
    "namaa-pos-mobile.webp",
    "namaa-items-mobile.webp",
    "namaa-profit-focus.webp",
    "namaa-rbac-users-public.webp",
])
