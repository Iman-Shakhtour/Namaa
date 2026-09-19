import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"
js_path = root / "js" / "main.js"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
js = js_path.read_text(encoding="utf-8")

# 1. Update Hero in index.html to remove mobile video
old_hero_media = """      <div class="hero-media" data-hero-media>
        <video class="hero-media__video hero-media__video--desktop" autoplay muted loop playsinline preload="metadata" poster="assets/screenshots/namaa-dashboard-hero-16x9.webp" aria-label="جولة مرئية في واجهات نماء الحقيقية على الكمبيوتر">
          <source src="assets/media/namaa-product-tour.webm" type="video/webm">
        </video>
        <video class="hero-media__video hero-media__video--mobile" autoplay muted loop playsinline preload="metadata" poster="assets/screenshots/namaa-dashboard-mobile.webp" aria-label="جولة مرئية في واجهات نماء الحقيقية على الهاتف">
          <source src="assets/media/namaa-product-tour-mobile.webm" type="video/webm">
        </video>
        <img class="hero-media__fallback" src="assets/screenshots/namaa-dashboard-hero-16x9.webp" alt="واجهة لوحة تحكم نماء الحقيقية تعرض مؤشرات المبيعات والصندوق وقائمة النظام" width="672" height="378" fetchpriority="high">
      </div>"""

new_hero_media = """      <div class="hero-media" data-hero-media>
        <video class="hero-media__video" autoplay muted loop playsinline preload="metadata" poster="assets/screenshots/namaa-dashboard-hero-16x9.webp" aria-label="جولة مرئية في واجهات نماء الحقيقية">
          <source src="assets/media/namaa-product-tour.webm" type="video/webm">
        </video>
        <img class="hero-media__fallback" src="assets/screenshots/namaa-dashboard-hero-16x9.webp" alt="واجهة لوحة تحكم نماء الحقيقية تعرض مؤشرات المبيعات والصندوق وقائمة النظام" width="672" height="378" fetchpriority="high">
      </div>"""

if old_hero_media in html:
    html = html.replace(old_hero_media, new_hero_media)
    print("Hero media updated in HTML")

# 2. Update story-mobile in index.html to use desktop screenshots only
old_story_mobile = """      <div class="story-mobile">
        <article><div><span>01</span><h3>المبيعات</h3><p>فاتورة واضحة من الصنف حتى الدفع.</p></div><img src="assets/screenshots/namaa-pos-mobile.webp" alt="نقطة البيع في نماء على الهاتف" width="356" height="761" loading="eager" decoding="async"></article>
        <article><div><span>02</span><h3>المخزون</h3><p>الأصناف والكميات قريبة منك.</p></div><img src="assets/screenshots/namaa-items-mobile-focus.webp" alt="الأصناف في نماء على الهاتف" width="353" height="460" loading="eager" decoding="async"></article>
        <article><div><span>03</span><h3>التقارير</h3><p>الأرقام المهمة بدون تشتيت.</p></div><img src="assets/screenshots/namaa-profit-16x9.webp" alt="ملخص تقرير الأرباح في نماء" width="1028" height="578" loading="eager" decoding="async"></article>
        <article><div><span>04</span><h3>الصلاحيات</h3><p>وصول مناسب لكل دور.</p></div><img src="assets/screenshots/namaa-rbac-focus.webp" alt="الصلاحيات في نماء بعد حجب أسماء الدخول" width="1156" height="650" loading="eager" decoding="async"></article>
      </div>"""

new_story_mobile = """      <div class="story-mobile">
        <article><div><span>01</span><h3>المبيعات</h3><p>فاتورة واضحة من الصنف حتى الدفع.</p></div><img src="assets/screenshots/namaa-pos-current.webp" alt="نقطة البيع في نماء" width="1919" height="866" loading="lazy" decoding="async"></article>
        <article><div><span>02</span><h3>المخزون</h3><p>الأصناف والكميات والأسعار في شاشة واحدة.</p></div><img src="assets/screenshots/namaa-inventory-current.webp" alt="الأصناف والمخزون في نماء" width="1919" height="867" loading="lazy" decoding="async"></article>
        <article><div><span>03</span><h3>التقارير</h3><p>مبيعات وتكلفة وصافي الربح بدون تشتيت.</p></div><img src="assets/screenshots/namaa-profit-current.webp" alt="ملخص تقرير الأرباح في نماء" width="1901" height="870" loading="lazy" decoding="async"></article>
        <article><div><span>04</span><h3>الصلاحيات</h3><p>وصول مناسب لكل مستخدم ودور وظيفي.</p></div><img src="assets/screenshots/namaa-rbac-focus.webp" alt="الصلاحيات في نماء بعد حجب أسماء الدخول" width="1156" height="650" loading="lazy" decoding="async"></article>
      </div>"""

if old_story_mobile in html:
    html = html.replace(old_story_mobile, new_story_mobile)
    print("Story mobile updated in HTML")

html_path.write_text(html, encoding="utf-8")

# 3. Update CSS
old_hero_css = """.hero-media video,.hero-media__fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero-media video{z-index:2;background:var(--navy)}
.hero-media__video--desktop{display:none}
.hero-media.is-fallback video{display:none}
.hero-media__fallback{z-index:1}"""

new_hero_css = """.hero-media video,.hero-media__fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero-media video{z-index:2;background:var(--navy)}
.hero-media.is-fallback video{display:none}
.hero-media__fallback{z-index:1}"""

if old_hero_css in css:
    css = css.replace(old_hero_css, new_hero_css)

# Update bento card media CSS
old_bento_css = """.bento-card{display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.bento-card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgb(7 24 47 / 8%);border-color:rgb(13 147 104 / 35%)}
.bento-card__copy{padding:26px 26px 14px}
.bento-card__copy>span,.story-mobile article>div>span{display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.bento-card h3{margin-top:10px;font-size:22px}
.bento-card p{margin-top:6px;color:var(--muted);font-size:15px;line-height:1.6}
.bento-card__media{margin-top:auto;padding-inline:20px;padding-top:12px;background:linear-gradient(180deg, transparent 0%, #f1f5f9 100%)}
.bento-card__media img{display:block;width:100%;height:auto;max-height:220px;object-fit:cover;object-position:top right;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--white);box-shadow:0 -2px 10px rgb(0 0 0 / 2%)}
.bento-card--hero{background:linear-gradient(180deg, var(--white) 0%, #F4FAF7 100%)}
.bento-card--hero .bento-card__media img{max-height:300px}"""

new_bento_css = """.bento-card{display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.bento-card:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgb(7 24 47 / 8%);border-color:rgb(13 147 104 / 35%)}
.bento-card__copy{padding:26px 26px 16px}
.bento-card__copy>span,.story-mobile article>div>span{display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.bento-card h3{margin-top:10px;font-size:22px}
.bento-card p{margin-top:6px;color:var(--muted);font-size:15px;line-height:1.6}
.bento-card__media{position:relative;margin-top:auto;padding-inline:16px;padding-top:12px;background:linear-gradient(180deg, transparent 0%, #edf2f7 100%)}
.bento-card__media img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top right;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--white);box-shadow:0 -2px 12px rgb(0 0 0 / 3%);transition:transform .3s ease}
.bento-card:hover .bento-card__media img{transform:scale(1.02)}
.bento-card--hero{background:linear-gradient(180deg, var(--white) 0%, #F4FAF7 100%)}
.bento-card--hero .bento-card__media{padding-inline:24px}
.bento-card--hero .bento-card__media img{aspect-ratio:16/9;max-height:360px}"""

if old_bento_css in css:
    css = css.replace(old_bento_css, new_bento_css)

# Update story-mobile CSS
old_story_css = """.story-mobile img{width:calc(100% - 32px);height:300px;margin-inline:auto;object-fit:contain;object-position:top center;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--bg)}"""

new_story_css = """.story-mobile img{display:block;width:calc(100% - 32px);margin-inline:auto;aspect-ratio:16/9;object-fit:cover;object-position:top right;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--bg);box-shadow:0 -2px 10px rgb(0 0 0 / 3%)}"""

if old_story_css in css:
    css = css.replace(old_story_css, new_story_css)

# Update mobile media query in CSS to remove mobile poster override and 3/4 aspect ratio
old_mobile_query = """.hero-media{width:100%;aspect-ratio:3/4;margin-top:32px}
  .hero-media__video--mobile{display:block}
  .hero-media__fallback{content:url('../assets/screenshots/namaa-dashboard-mobile.webp');object-position:top}"""

new_mobile_query = """.hero-media{width:100%;aspect-ratio:16/9;margin-top:32px}"""

if old_mobile_query in css:
    css = css.replace(old_mobile_query, new_mobile_query)
    print("Mobile media query updated in CSS")

# Remove desktop/mobile video toggles in 768px media query if present
old_768 = """.hero-media__video--desktop{display:block}.hero-media__video--mobile{display:none}"""
if old_768 in css:
    css = css.replace(old_768, "")

css_path.write_text(css, encoding="utf-8")
print("CSS updated successfully!")

# 4. Update JS video player logic
old_js_video = """  /* The video uses only the supplied product screenshots. Keep the real poster if it cannot load. */
  var heroMedia = document.querySelector('[data-hero-media]');
  var heroVideos = heroMedia ? Array.from(heroMedia.querySelectorAll('video')) : [];
  if (heroVideos.length) {
    function usePoster() { heroMedia.classList.add('is-fallback'); }
    var mobileVideoQuery = window.matchMedia('(max-width: 767px)');
    function syncHeroVideo() {
      if (reduceMotion.matches) {
        heroVideos.forEach(function (video) { video.pause(); });
        usePoster();
        return;
      }
      heroVideos.forEach(function (video) {
        var shouldPlay = mobileVideoQuery.matches ? video.classList.contains('hero-media__video--mobile') : video.classList.contains('hero-media__video--desktop');
        if (!shouldPlay) {
          video.pause();
          return;
        }
        var playAttempt = video.play();
        if (playAttempt && typeof playAttempt.catch === 'function') playAttempt.catch(function () {});
      });
    }
    heroVideos.forEach(function (heroVideo) {
      heroVideo.addEventListener('error', usePoster);
      heroVideo.querySelectorAll('source').forEach(function (source) { source.addEventListener('error', usePoster); });
    });
    mobileVideoQuery.addEventListener('change', syncHeroVideo);
    syncHeroVideo();
  }"""

new_js_video = """  /* The hero video plays the widescreen desktop product tour across all devices. */
  var heroMedia = document.querySelector('[data-hero-media]');
  var heroVideo = heroMedia ? heroMedia.querySelector('video') : null;
  if (heroVideo) {
    function usePoster() { heroMedia.classList.add('is-fallback'); }
    function syncHeroVideo() {
      if (reduceMotion.matches) {
        heroVideo.pause();
        usePoster();
        return;
      }
      var playAttempt = heroVideo.play();
      if (playAttempt && typeof playAttempt.catch === 'function') playAttempt.catch(function () {});
    }
    heroVideo.addEventListener('error', usePoster);
    heroVideo.querySelectorAll('source').forEach(function (source) { source.addEventListener('error', usePoster); });
    syncHeroVideo();
  }"""

if old_js_video in js:
    js = js.replace(old_js_video, new_js_video)
    js_path.write_text(js, encoding="utf-8")
    print("JS updated successfully!")

