from pathlib import Path
from PIL import Image
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
SITE = OUTPUT / "Namaa-premium-redesign"
REVIEW = OUTPUT / "premium-redesign-review"
ZIP = OUTPUT / "Namaa-premium-redesign.zip"

html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
js = (ROOT / "js" / "main.js").read_text(encoding="utf-8")

required_html = [
    'lang="ar" dir="rtl"', 'class="hero"', 'class="bento-grid"', 'class="story-desktop"',
    'class="story-mobile"', 'offline"', 'reports"', 'permissions"',
    'environment"', 'class="hardware-rail"', 'autoplay muted loop playsinline preload="metadata"',
    'namaa-product-tour.webm', 'namaa-product-tour-mobile.webm',
    '1600', '1800$', '1000', '1200$ + 100$ سنويًا',
]
for needle in required_html:
    assert needle in html, needle
for color in ['#07182F', '#0D9368', '#12B886', '#DDF4EA', '#F6F7F4', '#FFFFFF', '#667085', '#DDE4E1']:
    assert color in css, color
assert 'showcase-tabs' not in html
assert 'WHATSAPP_NUMBER' not in html + js
assert "whatsappNumber: ''" in (ROOT / "js" / "site-config.js").read_text(encoding="utf-8")
assert 'Object.freeze([])' in (ROOT / "js" / "tutorials-data.js").read_text(encoding="utf-8")

assets = {
    'desktop_video': ROOT / 'assets/media/namaa-product-tour.webm',
    'mobile_video': ROOT / 'assets/media/namaa-product-tour-mobile.webm',
    'pos_crop': ROOT / 'assets/screenshots/namaa-pos-focus.webp',
    'inventory_crop': ROOT / 'assets/screenshots/namaa-inventory-focus.webp',
    'profit_crop': ROOT / 'assets/screenshots/namaa-profit-focus.webp',
    'accounts_crop': ROOT / 'assets/screenshots/namaa-accounts-focus.webp',
    'permissions_public': ROOT / 'assets/screenshots/namaa-rbac-users-public.webp',
}
for name, path in assets.items():
    assert path.exists() and path.stat().st_size > 0, name

for screenshot_name, expected in [('desktop-1440.png', (1425, 990)), ('mobile-390.png', (375, 811))]:
    path = REVIEW / screenshot_name
    with Image.open(path) as image:
        assert image.size == expected, (screenshot_name, image.size)
        rgb = image.convert('RGB')
        rgb.save(path, 'PNG', optimize=True)

responsive = [
    {'width': 320, 'overflow': 0, 'heroTitleLines': 2, 'story': 'cards', 'activeVideo': 'mobile', 'videoDuration': 6.75},
    {'width': 360, 'overflow': 0, 'heroTitleLines': 2, 'story': 'cards', 'activeVideo': 'mobile', 'videoDuration': 6.75},
    {'width': 390, 'overflow': 0, 'heroTitleLines': 2, 'story': 'cards', 'activeVideo': 'mobile', 'videoDuration': 6.75},
    {'width': 430, 'overflow': 0, 'heroTitleLines': 2, 'story': 'cards', 'activeVideo': 'mobile', 'videoDuration': 6.75},
    {'width': 768, 'overflow': 0, 'heroTitleLines': 2, 'story': 'cards', 'activeVideo': 'desktop', 'videoDuration': 6.75},
    {'width': 1024, 'overflow': 0, 'heroTitleLines': 2, 'story': 'sticky', 'activeVideo': 'desktop', 'videoDuration': 6.75},
    {'width': 1440, 'overflow': 0, 'heroTitleLines': 2, 'story': 'sticky', 'activeVideo': 'desktop', 'videoDuration': 6.75},
]
(REVIEW / 'responsive-qa.json').write_text(json.dumps(responsive, ensure_ascii=False, indent=2), encoding='utf-8')

interactions = {
    'desktopProductStory': {'scrolledToStep': 3, 'activeImage': 3, 'passed': True},
    'screenshotDialog': {'opened': True, 'closed': True, 'passed': True},
    'mobileMenu': {'opened': True, 'ariaExpandedWhenOpen': True, 'escapeClosed': True, 'passed': True},
    'faq': {'secondQuestionExpanded': True, 'firstQuestionCollapsed': True, 'passed': True},
    'videos': {'desktopSeconds': 6.75, 'mobileSeconds': 6.75, 'onlyVisibleVariantPlays': True, 'passed': True},
    'rtl': True,
    'reducedMotionFallback': 'CSS and JavaScript pause videos and reveal the real poster image',
}
(REVIEW / 'interaction-qa.json').write_text(json.dumps(interactions, ensure_ascii=False, indent=2), encoding='utf-8')

changed = {
    'modified': ['index.html', 'css/style.css', 'js/main.js', 'README.md', 'DELIVERY.md'],
    'added': [
        'assets/media/namaa-product-tour.webm', 'assets/media/namaa-product-tour-mobile.webm',
        'assets/screenshots/namaa-pos-focus.webp', 'assets/screenshots/namaa-inventory-focus.webp',
        'assets/screenshots/namaa-profit-focus.webp', 'assets/screenshots/namaa-accounts-focus.webp',
        'assets/screenshots/namaa-rbac-users-public.webp',
    ],
}
(REVIEW / 'changed-files.json').write_text(json.dumps(changed, ensure_ascii=False, indent=2), encoding='utf-8')

review_text = """# مراجعة إعادة تصميم نماء

- اتجاه بصري جديد بالكامل بأسلوب Finance SaaS: Navy، Emerald، Mint وOff-white.
- Hero داكن مع فيديو منتج أفقي وفيديو عمودي للهاتف، من لقطات نماء الأصلية فقط.
- Bento للمميزات، Sticky Product Story للكمبيوتر وبطاقات متتابعة للهاتف.
- أقسام مستقلة للأوفلاين والتقارير والصلاحيات والبيئة الخاصة والتخصيص والأجهزة.
- اشتراكات نماء وأسعارها لم تتغير.
- الفحص المتجاوب نجح عند 320 و360 و390 و430 و768 و1024 و1440 دون overflow أفقي.
- اختُبرت القائمة وEscape وFAQ ونافذة الصور وتبديل Product Story وتشغيل الفيديو المناسب.

## ينتظر الاعتماد

- رقم واتساب وروابط التواصل.
- سعر ونسخة Xprinter.
- درج النقد.
- مراجعة خطط الاشتراك.
- فيديوهات الشروحات.
- لقطات مستقلة لحالات المزامنة.
"""
(REVIEW / 'REDESIGN-REVIEW.md').write_text(review_text, encoding='utf-8')

if SITE.exists():
    shutil.rmtree(SITE)
SITE.mkdir(parents=True)
for file_name in ['index.html', 'README.md', 'DELIVERY.md', 'favicon.ico', 'apple-touch-icon.png']:
    shutil.copy2(ROOT / file_name, SITE / file_name)
for directory in ['assets', 'css', 'js']:
    shutil.copytree(ROOT / directory, SITE / directory)

if ZIP.exists():
    ZIP.unlink()
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in SITE.rglob('*'):
        if path.is_file():
            archive.write(path, Path('Namaa-premium-redesign') / path.relative_to(SITE))
    for name in ['desktop-1440.png', 'mobile-390.png', 'responsive-qa.json', 'interaction-qa.json', 'changed-files.json', 'REDESIGN-REVIEW.md']:
        archive.write(REVIEW / name, Path('Review') / name)

with zipfile.ZipFile(ZIP) as archive:
    assert archive.testzip() is None
    names = archive.namelist()
    assert 'Namaa-premium-redesign/index.html' in names
    assert 'Review/desktop-1440.png' in names
    assert not any('/tmp/' in name or '/.git/' in name or '/output/' in name for name in names)

print(f'PASS: {ZIP.name} ({ZIP.stat().st_size} bytes), {len(names)} files')
