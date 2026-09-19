from pathlib import Path
from PIL import Image
import json
import re

root = Path(__file__).resolve().parents[1]
review = root / 'output/hero-review'
review.mkdir(parents=True,exist_ok=True)
(review/'before-index.html').write_bytes((root/'index.html').read_bytes())
(review/'before-style.css').write_bytes((root/'css/style.css').read_bytes())
original = Image.open(root/'output/review/original-screenshots/namaa-dashboard-desktop.png')
# Preserve the actual KPI cards and upper navigation without redrawing any UI.
box = (788, 0, 1916, 487)
crop = original.crop(box).convert('RGB')
crop.save(root/'assets/screenshots/namaa-dashboard-hero.webp','WEBP',quality=95,method=6)
small = crop.resize((640,round(crop.height*640/crop.width)),Image.Resampling.LANCZOS)
small.save(root/'assets/screenshots/namaa-dashboard-hero-640.webp','WEBP',quality=94,method=6)
(review/'crop-source.json').write_text(json.dumps({'source':'original-screenshots/namaa-dashboard-desktop.png','source_dimensions':list(original.size),'crop_box':list(box),'crop_dimensions':list(crop.size),'operation':'crop and WebP conversion only'},indent=2),encoding='utf-8')

html = (root/'index.html').read_text(encoding='utf-8')
hero = '''  <section class="hero" id="top" aria-labelledby="hero-title">
    <div class="container hero__inner">
      <div class="hero__copy">
        <p class="eyebrow"><span class="eyebrow__dot"></span>للمحلات والمشاريع الصغيرة والمتوسطة</p>
        <h1 id="hero-title"><span class="hero__title-main">كل شغلك وحساباتك</span><span class="hero__title-accent">بمكان واحد.</span></h1>
        <p class="hero__desc">مبيعات، مشتريات، مخزون وحسابات — بنظام عربي واحد.</p>
        <div class="btn-group">
          <a href="#showcase" class="btn btn-primary">شاهد نماء<svg aria-hidden="true"><use href="#icon-arrow-fwd"/></svg></a>
          <a href="#mazaya" class="btn btn-secondary">اكتشف المميزات</a>
        </div>
        <p class="hero__summary">بيع • مخزون • حسابات • تقارير</p>
      </div>
      <div class="hero__visual">
        <figure class="hero__screen">
          <img src="assets/screenshots/namaa-dashboard-hero.webp" srcset="assets/screenshots/namaa-dashboard-hero-640.webp 640w, assets/screenshots/namaa-dashboard-hero.webp 1128w" sizes="(min-width: 1280px) 692px, (min-width: 1024px) calc(58vw - 52px), (min-width: 768px) calc(100vw - 64px), (min-width: 430px) calc(100vw - 40px), calc(100vw - 32px)" alt="الجزء العلوي من لوحة تحكم نماء: بطاقات المبيعات والصندوق وذمم العملاء والشيكات الصادرة، مع قائمة أدوات النظام على اليمين" width="1128" height="487" fetchpriority="high">
        </figure>
      </div>
    </div>
  </section>'''
html,count = re.subn(r'  <section class="hero"[\s\S]*?</section>',hero,html)
assert count==1
preload = '<link rel="preload" as="image" href="assets/screenshots/namaa-dashboard-hero.webp" imagesrcset="assets/screenshots/namaa-dashboard-hero-640.webp 640w, assets/screenshots/namaa-dashboard-hero.webp 1128w" imagesizes="(min-width: 1280px) 692px, (min-width: 1024px) calc(58vw - 52px), (min-width: 768px) calc(100vw - 64px), (min-width: 430px) calc(100vw - 40px), calc(100vw - 32px)">'
html = re.sub(r'<link rel="preload" as="image"[^>]+>',preload,html)
html = html.replace('css/style.css?v=20260916a','css/style.css?v=20260916hero')
(root/'index.html').write_text(html,encoding='utf-8')
