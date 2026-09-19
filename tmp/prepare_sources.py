from pathlib import Path
from PIL import Image, ImageFilter
import shutil
import zipfile
import re

root = Path(__file__).resolve().parents[1]
review = root / 'output' / 'review'
review.mkdir(parents=True, exist_ok=True)
original = review / 'original-screenshots'
original.mkdir(exist_ok=True)
with zipfile.ZipFile(root / 'tmp' / 'original-project.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for item in ['index.html', 'README.md', 'favicon.ico', 'apple-touch-icon.png', 'css', 'js', 'assets']:
        path = root / item
        for source in (path.rglob('*') if path.is_dir() else [path]):
            if source.is_file():
                archive.write(source, source.relative_to(root))

html = (root / 'index.html').read_text(encoding='utf-8')
(root / 'tmp' / 'original-index.html').write_text(html, encoding='utf-8')
pricing = re.search(r'<section[^>]*id="pricing"[\s\S]*?</section>', html).group()
(root / 'tmp' / 'original-pricing.html').write_text(pricing, encoding='utf-8')

sources = {
    'namaa-dashboard-desktop': '231733',
    'namaa-pos-desktop': '231833',
    'namaa-inventory-desktop': '231928',
    'namaa-profit-report': '232000',
    'namaa-rbac-users': '232100',
    'namaa-dashboard-mobile': '232144',
    'namaa-pos-mobile': '232202',
    'namaa-items-mobile': '232247',
}
screenshots = root / 'assets' / 'screenshots'
screenshots.mkdir(parents=True, exist_ok=True)
for name, stamp in sources.items():
    source = Path(r'C:\Users\User\Pictures\Screenshots') / f'Screenshot 2026-09-15 {stamp}.png'
    shutil.copy2(source, original / f'{name}.png')
    image = Image.open(source).convert('RGB')
    if name == 'namaa-rbac-users':
        # Only the two login identifiers. Keep all role names and permissions intact.
        for box in [(1178, 342, 1284, 374), (1178, 413, 1284, 445)]:
            image.paste(image.crop(box).filter(ImageFilter.GaussianBlur(12)), box)
        image.save(screenshots / f'{name}-sanitized.png')
    image.save(screenshots / f'{name}.webp', 'WEBP', quality=94, method=6)
    if name == 'namaa-dashboard-desktop':
        for width in [640, 1280]:
            image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS).save(
                screenshots / f'{name}-{width}.webp', 'WEBP', quality=94, method=6)
    print(name, image.size, (screenshots / f'{name}.webp').stat().st_size)

# Preserve unchanged source PNGs outside the website's asset directory.
(original / 'README.txt').write_text(
    'These are the supplied source screenshots, unchanged. Do not publish this review directory.\n'
    'The RBAC source contains login identifiers. Use the sanitized WebP in the website.\n', encoding='utf-8')
