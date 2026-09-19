from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
old = (root / 'tmp' / 'original-index.html').read_text(encoding='utf-8')
head = old.split('<body>')[0]
title = 'نماء | نظام محاسبي وإدارة أعمال للمحلات'
description = 'نماء نظام عربي لإدارة المبيعات، المشتريات، المخزون، العملاء، الحسابات والتقارير للمحلات والمشاريع الصغيرة والمتوسطة.'
head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head)
for key in ['description', 'og:description', 'twitter:description']:
    head = re.sub(r'(<meta (?:name|property)="' + key + r'" content=")[^"]*(")', lambda m: m[1] + description + m[2], head)
for key in ['og:title', 'twitter:title']:
    head = re.sub(r'(<meta (?:name|property)="' + key + r'" content=")[^"]*(")', lambda m: m[1] + title + m[2], head)
head = head.replace('assets/images/01-hero-dashboard.webp', 'assets/screenshots/namaa-dashboard-desktop.webp')
head = head.replace('family=Tajawal:wght@400;500;700;800;900&family=Cairo:wght@400;500;700;800', 'family=Tajawal:wght@400;700;800')
head = head.replace('<link rel="preload" as="image" href="assets/images/01-hero-dashboard-1200.webp">', '<link rel="preload" as="image" href="assets/screenshots/namaa-dashboard-desktop-1280.webp" imagesrcset="assets/screenshots/namaa-dashboard-desktop-640.webp 640w, assets/screenshots/namaa-dashboard-desktop-1280.webp 1280w, assets/screenshots/namaa-dashboard-desktop.webp 1916w" imagesizes="(min-width: 1100px) 690px, (min-width: 768px) 85vw, calc(100vw - 32px)">')
head = head.replace('<meta name="twitter:card"', '<meta name="twitter:image" content="assets/screenshots/namaa-dashboard-desktop.webp">\n<meta name="twitter:card"')
sprite = re.search(r'<svg[^>]*[\s\S]*?</svg>', old).group()
sprite = re.sub(r'<svg[^>]*>', '<svg class="icon-sprite" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">', sprite, count=1)
pricing = (root / 'tmp' / 'original-pricing.html').read_text(encoding='utf-8')
pricing = re.sub(r'\s+(reveal|stagger)(?=[ "\s])', '', pricing)
pricing = pricing.replace('href="#lead-form"', 'href="#showcase" data-contact-cta data-contact-label="اسأل عن هذا العرض"')
pricing = pricing.replace('>اسأل عن هذا العرض</a>', '>شاهد البرنامج</a>')
body = (root / 'tmp' / 'body.html').read_text(encoding='utf-8').replace('{{PRICING}}', pricing)
for previous, current in {
    'icon-arrow-left': 'icon-arrow-fwd', 'icon-arrow-up-right': 'icon-arrow-fwd',
    'icon-boxes': 'icon-box', 'icon-dashboard': 'icon-pie', 'icon-pos': 'icon-card',
    'icon-database': 'icon-warehouse', 'icon-expand': 'icon-scan'
}.items():
    body = body.replace(previous, current)
head = head.replace('css/style.css', 'css/style.css?v=20260915')
body = body.replace('js/site-config.js', 'js/site-config.js?v=20260915').replace('js/hardware-data.js', 'js/hardware-data.js?v=20260915').replace('js/main.js', 'js/main.js?v=20260915')
(root / 'index.html').write_text(head + '<body>\n<a href="#main" class="skip-link">تخطَّ إلى المحتوى الرئيسي</a>\n' + sprite + '\n' + body, encoding='utf-8')
for target, source in [('css/style.css', 'tmp/new-style.css'), ('js/main.js', 'tmp/new-main.js')]:
    (root / target).write_text((root / source).read_text(encoding='utf-8'), encoding='utf-8')
ids = set(re.findall(r'<symbol id="([^"]+)"', sprite))
used = set(re.findall(r'<use href="#([^"]+)"', body))
print('Undefined icons:', sorted(used - ids))
print('Sections:', body.count('<section'))
