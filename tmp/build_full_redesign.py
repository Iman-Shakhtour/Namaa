from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
shots = ROOT / "assets" / "screenshots"


def crop(source, target, box, quality=88):
    with Image.open(shots / source) as im:
        out = im.crop(box)
        out.save(shots / target, "WEBP", quality=quality, method=6)
        print(target, out.size)


crop("namaa-pos-desktop.webp", "namaa-pos-focus.webp", (0, 0, 1919, 650))
crop("namaa-inventory-desktop.webp", "namaa-inventory-focus.webp", (520, 0, 1919, 610))
crop("namaa-profit-report.webp", "namaa-profit-focus.webp", (0, 70, 1564, 648))
crop("namaa-dashboard-desktop.webp", "namaa-accounts-focus.webp", (0, 0, 1564, 520))

with Image.open(shots / "namaa-rbac-users-sanitized.png") as im:
    im.save(shots / "namaa-rbac-users-public.webp", "WEBP", quality=88, method=6)
    print("namaa-rbac-users-public.webp", im.size)

source = (ROOT / "index.html").read_text(encoding="utf-8")
sprite_end = source.index("</svg>") + len("</svg>")
head_and_sprite = source[:sprite_end]
head_and_sprite = head_and_sprite.replace("#0B1D3A", "#07182F")
head_and_sprite = head_and_sprite.replace(
    '<link rel="preload" as="image" href="assets/screenshots/namaa-dashboard-hero.webp" imagesrcset="assets/screenshots/namaa-dashboard-hero-640.webp 640w, assets/screenshots/namaa-dashboard-hero.webp 874w" imagesizes="(min-width: 1280px) 1176px, (min-width: 768px) min(88vw, calc(100vw - 64px)), calc(100vw - 32px)">',
    '<link rel="preload" as="image" href="assets/screenshots/namaa-dashboard-hero.webp">'
)
head_and_sprite = head_and_sprite.replace("css/style.css?v=20260916centered", "css/style.css?v=20260916premium")

body = r'''
<header class="site-header" data-theme="dark">
  <div class="container site-header__inner">
    <a href="#top" class="brand" aria-label="نماء — الصفحة الرئيسية">
      <img class="brand__icon" src="assets/brand/icon-mark.webp" alt="" width="192" height="200">
      <span class="brand__word">نماء<span class="brand__tagline">لحسابات تنمو</span></span>
    </a>
    <nav class="nav" aria-label="التنقل الرئيسي">
      <a href="#mazaya">المميزات</a>
      <a href="#showcase">شاهد نماء</a>
      <a href="#hardware">الأجهزة</a>
      <a href="#faq">الأسئلة</a>
    </nav>
    <div class="header-actions">
      <a href="#showcase" class="btn btn-primary">شاهد البرنامج</a>
      <button class="hamburger" type="button" aria-label="فتح القائمة" aria-expanded="false" aria-controls="mobile-panel">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <nav class="mobile-panel" id="mobile-panel" aria-label="التنقل على الهاتف" hidden>
    <div class="container"><a href="#mazaya">المميزات</a><a href="#showcase">شاهد نماء</a><a href="#hardware">الأجهزة</a><a href="#faq">الأسئلة</a></div>
  </nav>
</header>

<main id="main" tabindex="-1">
  <section class="hero" id="top" aria-labelledby="hero-title">
    <div class="container hero__inner">
      <div class="hero__copy">
        <p class="eyebrow eyebrow--light"><span class="eyebrow__line" aria-hidden="true"></span>نظام محاسبي وإدارة أعمال عربي</p>
        <h1 id="hero-title">شغلك أوضح.<br><span>حساباتك أرتب.</span></h1>
        <p class="hero__desc">نماء يجمع المبيعات، المشتريات، المخزون والحسابات في نظام عربي واحد.</p>
        <div class="btn-group">
          <a href="#showcase" class="btn btn-primary">شاهد نماء<svg aria-hidden="true"><use href="#icon-arrow-fwd"/></svg></a>
          <a href="#mazaya" class="btn btn-ghost">اكتشف المميزات</a>
        </div>
      </div>
      <div class="hero-media" data-hero-media>
        <video autoplay muted loop playsinline preload="metadata" poster="assets/screenshots/namaa-dashboard-hero.webp" aria-label="جولة مرئية في واجهات نماء الحقيقية">
          <source src="assets/media/namaa-product-tour.webm" type="video/webm">
        </video>
        <img class="hero-media__fallback" src="assets/screenshots/namaa-dashboard-hero.webp" alt="واجهة لوحة تحكم نماء الحقيقية تعرض مؤشرات المبيعات والصندوق وقائمة النظام" width="874" height="378" fetchpriority="high">
        <span class="hero-media__label"><i aria-hidden="true"></i>واجهات نماء الحقيقية</span>
      </div>
    </div>
  </section>

  <section class="section features" id="mazaya" aria-labelledby="features-title">
    <div class="container">
      <header class="section-head">
        <p class="eyebrow">من أول فاتورة لآخر تقرير</p>
        <h2 id="features-title">كل اللي تحتاجه لإدارة شغلك</h2>
        <p>أدوات مترابطة تعطيك صورة واضحة عن يومك، بدون تنقل بين أنظمة منفصلة.</p>
      </header>
      <div class="bento-grid">
        <article class="bento-card bento-card--wide bento-card--dark">
          <div class="bento-card__copy"><span>01</span><h3>نقطة البيع</h3><p>بيع سريع بالاسم أو الباركود، مع سلة وطرق دفع واضحة.</p></div>
          <img src="assets/screenshots/namaa-pos-focus.webp" alt="واجهة نقطة البيع الحقيقية في نماء" width="1919" height="650" loading="lazy" decoding="async">
        </article>
        <article class="bento-card bento-card--tall">
          <div class="bento-card__copy"><span>02</span><h3>المخزون</h3><p>الأصناف والكميات والأسعار في شاشة واحدة.</p></div>
          <img src="assets/screenshots/namaa-items-mobile.webp" alt="قائمة الأصناف الحقيقية في نماء على الهاتف" width="353" height="759" loading="lazy" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>03</span><h3>التقارير</h3><p>مبيعات وتكلفة وربح للفترة التي تختارها.</p></div>
          <img src="assets/screenshots/namaa-profit-focus.webp" alt="أرقام تقرير الأرباح الحقيقي في نماء" width="1564" height="578" loading="lazy" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>04</span><h3>المحاسبة</h3><p>صندوق ومصروفات وشيكات وحركة مالية أوضح.</p></div>
          <img src="assets/screenshots/namaa-accounts-focus.webp" alt="لوحة نماء التي تعرض أرصدة الصندوق والحسابات" width="1564" height="520" loading="lazy" decoding="async">
        </article>
        <article class="bento-card bento-card--wide bento-card--mint">
          <div class="bento-card__copy"><span>05</span><h3>العملاء والموردون</h3><p>أرصدة وكشوف حساب مرتبطة بكل حركة بيع وشراء.</p></div>
          <img src="assets/screenshots/namaa-dashboard-hero.webp" alt="بطاقات الأرصدة في لوحة تحكم نماء" width="874" height="378" loading="lazy" decoding="async">
        </article>
      </div>
    </div>
  </section>

  <section class="section product-story" id="showcase" aria-labelledby="showcase-title">
    <div class="container">
      <header class="section-head center">
        <p class="eyebrow">المنتج هو الواجهة</p>
        <h2 id="showcase-title">من البيع للقرار، كل خطوة واضحة</h2>
        <p>تصفح مسار العمل داخل شاشات نماء الحقيقية.</p>
      </header>
      <div class="story-desktop">
        <div class="story-steps" aria-label="أقسام المنتج">
          <article class="story-step is-active" data-story-index="0"><span>01</span><h3>المبيعات</h3><p>ابدأ الفاتورة وابحث عن الصنف وأتمم الدفع من شاشة واحدة.</p></article>
          <article class="story-step" data-story-index="1"><span>02</span><h3>المخزون</h3><p>تابع الأصناف والوحدات والأسعار والكمية المتاحة.</p></article>
          <article class="story-step" data-story-index="2"><span>03</span><h3>التقارير</h3><p>اقرأ المبيعات والتكلفة وصافي الربح ضمن الفترة المطلوبة.</p></article>
          <article class="story-step" data-story-index="3"><span>04</span><h3>الصلاحيات</h3><p>وزّع الوصول حسب دور كل مستخدم ومسؤوليته.</p></article>
        </div>
        <div class="story-stage" aria-live="polite">
          <img class="is-active" data-story-image="0" src="assets/screenshots/namaa-pos-desktop.webp" alt="نقطة البيع في نماء" width="1919" height="870" loading="lazy" decoding="async">
          <img data-story-image="1" src="assets/screenshots/namaa-inventory-desktop.webp" alt="الأصناف والمخزون في نماء" width="1919" height="868" loading="lazy" decoding="async">
          <img data-story-image="2" src="assets/screenshots/namaa-profit-report.webp" alt="تقرير الأرباح في نماء" width="1897" height="870" loading="lazy" decoding="async">
          <img data-story-image="3" src="assets/screenshots/namaa-rbac-users-public.webp" alt="إدارة المستخدمين والصلاحيات في نماء بعد حجب أسماء الدخول" width="1901" height="870" loading="lazy" decoding="async">
        </div>
      </div>
      <div class="story-mobile">
        <article><div><span>01</span><h3>المبيعات</h3><p>فاتورة واضحة من الصنف حتى الدفع.</p></div><img src="assets/screenshots/namaa-pos-mobile.webp" alt="نقطة البيع في نماء على الهاتف" width="356" height="761" loading="lazy" decoding="async"></article>
        <article><div><span>02</span><h3>المخزون</h3><p>الأصناف والكميات قريبة منك.</p></div><img src="assets/screenshots/namaa-items-mobile.webp" alt="الأصناف في نماء على الهاتف" width="353" height="759" loading="lazy" decoding="async"></article>
        <article><div><span>03</span><h3>التقارير</h3><p>الأرقام المهمة بدون تشتيت.</p></div><img src="assets/screenshots/namaa-profit-focus.webp" alt="ملخص تقرير الأرباح في نماء" width="1564" height="578" loading="lazy" decoding="async"></article>
        <article><div><span>04</span><h3>الصلاحيات</h3><p>وصول مناسب لكل دور.</p></div><img src="assets/screenshots/namaa-rbac-users-public.webp" alt="الصلاحيات في نماء بعد حجب أسماء الدخول" width="1901" height="870" loading="lazy" decoding="async"></article>
      </div>
    </div>
  </section>

  <section class="section offline" id="offline" aria-labelledby="offline-title">
    <div class="container offline__grid">
      <div class="offline__copy">
        <p class="eyebrow eyebrow--light">استمرارية مدروسة</p>
        <h2 id="offline-title">النت فصل؟ البيع بكمل.</h2>
        <p class="offline__lead">بعد بدء العمل أونلاين، يمكنك مواصلة عمليات البيع المدعومة عند انقطاع الاتصال، ثم مزامنة العمليات عند عودة الإنترنت.</p>
        <ol class="workflow" aria-label="مراحل العمل دون اتصال">
          <li><b>1</b><div><h3>دون اتصال</h3><p>واصل البيع من فاتورة البيع وPOS النقدي.</p></div></li>
          <li><b>2</b><div><h3>عمليات بانتظار المزامنة</h3><p>تُحفظ العمليات محليًا حتى يعود الاتصال.</p></div></li>
          <li><b>3</b><div><h3>مزامنة العمليات</h3><p>راجع المؤشر وأعد المحاولة عند الحاجة.</p></div></li>
        </ol>
      </div>
      <button type="button" class="product-frame product-frame--dark" data-zoom="assets/screenshots/namaa-pos-desktop.webp" data-title="نقطة البيع في نماء" aria-label="تكبير شاشة نقطة البيع" aria-haspopup="dialog"><img src="assets/screenshots/namaa-pos-desktop.webp" alt="شاشة نقطة البيع الحقيقية في نماء" width="1919" height="870" loading="lazy" decoding="async"></button>
    </div>
  </section>

  <section class="section reports" id="reports" aria-labelledby="reports-title">
    <div class="container reports__grid">
      <div class="reports__copy"><p class="eyebrow">التقارير</p><h2 id="reports-title">اعرف وين رايح شغلك بالأرقام.</h2><p>تابع إجمالي المبيعات والتكلفة وصافي الربح من نفس التقرير، وبالأرقام الفعلية المسجلة في نماء.</p><ul><li><span>1,200</span>إجمالي المبيعات</li><li><span>480</span>تكلفة البضاعة</li><li><span>720</span>صافي الربح</li></ul></div>
      <button type="button" class="product-frame report-frame" data-zoom="assets/screenshots/namaa-profit-report.webp" data-title="تقرير الأرباح في نماء" aria-label="تكبير تقرير الأرباح" aria-haspopup="dialog"><img src="assets/screenshots/namaa-profit-focus.webp" alt="تقرير الأرباح في نماء يعرض مبيعات 1,200 وتكلفة 480 وصافي ربح 720" width="1564" height="578" loading="lazy" decoding="async"></button>
    </div>
  </section>

  <section class="section permissions" id="permissions" aria-labelledby="permissions-title">
    <div class="container permissions__grid">
      <div class="permissions__copy"><p class="eyebrow">المستخدمون والصلاحيات</p><h2 id="permissions-title">كل موظف يشوف اللي بخصه.</h2><p>حدد الصلاحيات حسب دور كل مستخدم داخل النظام.</p><span class="soft-badge">بدون رسوم إضافية على ميزة الصلاحيات</span></div>
      <button type="button" class="product-frame" data-zoom="assets/screenshots/namaa-rbac-users-public.webp" data-title="المستخدمون والصلاحيات في نماء" aria-label="تكبير شاشة الصلاحيات" aria-haspopup="dialog"><img src="assets/screenshots/namaa-rbac-users-public.webp" alt="جدول صلاحيات المدير والمحاسب والكاشير والمستودعجي مع حجب أسماء الدخول" width="1901" height="870" loading="lazy" decoding="async"></button>
    </div>
  </section>

  <section class="section environment" id="environment" aria-labelledby="environment-title">
    <div class="container">
      <header class="section-head"><p class="eyebrow">مصمم لنسختك</p><h2 id="environment-title">بيئة خاصة لكل عميل</h2></header>
      <div class="environment-list">
        <article><span>01</span><h3>رابط خاص</h3><p>دخول مباشر لنسختك من نماء.</p></article>
        <article><span>02</span><h3>قاعدة بيانات مستقلة</h3><p>بيانات نشاطك ضمن بيئتك الخاصة.</p></article>
        <article><span>03</span><h3>تخصيص حسب نشاطك</h3><p>إعداد يناسب طريقة عملك المتفق عليها.</p></article>
      </div>
      <div class="customization"><div><p class="eyebrow">مرونة عند الحاجة</p><h2>شغلك مختلف؟ نماء بيتكيّف.</h2></div><p>إذا احتاج نشاطك تعديلًا أو إضافة خاصة، يمكن تنفيذ التخصيص المتفق عليه على نسختك بدون رسوم إضافية.</p></div>
    </div>
  </section>

  <section class="section hardware" id="hardware" aria-labelledby="hardware-title">
    <div class="container">
      <header class="section-head"><p class="eyebrow">تجهيزات نقطة البيع</p><h2 id="hardware-title">جهّز محلك مع نماء</h2><p>مجموعة مختارة من أجهزة البيع العملية، بصورها وأسعارها الموثقة.</p></header>
      <div class="hardware-rail" id="hardware-products" aria-label="أجهزة مقترحة"></div>
      <p class="hardware-source">صور وأسعار الأجهزة من <a href="https://logix-mobile.com/shop.php?category=pos" target="_blank" rel="noopener noreferrer">Logix Mobile</a>. أسعار الأجهزة مستقلة عن اشتراك نماء.</p>
      <noscript><p>يمكنك مراجعة خيارات الأجهزة وأسعارها عبر رابط Logix Mobile أعلاه.</p></noscript>
    </div>
  </section>

  <section class="section pricing" id="pricing" aria-labelledby="pricing-title">
    <div class="container">
      <header class="section-head center"><p class="eyebrow">الاشتراكات</p><h2 id="pricing-title">طريقتان واضحتان للدفع</h2><p>اختر بين امتلاك نماء مدى الحياة، أو سعر بداية أقل مع تجديد سنوي للتحديثات والصيانة والدعم الفني.</p></header>
      <div class="pricing-grid">
        <article class="price-card price-card--featured"><span class="price-card__badge">الخيار الأول</span><h3>امتلاك نماء مدى الحياة</h3><p class="price-card__desc">دفعة واحدة، بدون رسوم تجديد سنوية حسب هذا العرض.</p><div class="price-main"><b><small>$</small>1600</b><span>دفعة واحدة</span></div><div class="price-or">أو بالتقسيط</div><div class="price-installment"><div><b><small>$</small>300</b><span>شهريًا</span></div><em>6 دفعات · الإجمالي 1800$</em></div><ul class="check-list price-card__list"><li>امتلاك مدى الحياة</li><li>خيار دفع مباشر أو 6 أقساط</li></ul><a href="#showcase" class="btn btn-primary btn-block">شاهد البرنامج</a></article>
        <article class="price-card"><span class="price-card__badge price-card__badge--soft">الخيار الثاني</span><h3>سعر بداية أقل</h3><p class="price-card__desc">مع 100$ سنويًا للتجديد والتحديثات والصيانة والدعم الفني.</p><div class="price-main"><b><small>$</small>1000</b><span>دفعة واحدة</span></div><div class="price-renew"><b>+$100</b> سنويًا للتجديد والتحديثات والصيانة والدعم الفني</div><div class="price-or">أو بالتقسيط</div><div class="price-installment"><div><b><small>$</small>300</b><span>شهريًا</span></div><em>4 دفعات · الإجمالي 1200$ + 100$ سنويًا</em></div><ul class="check-list price-card__list"><li>سعر بداية أقل</li><li>خيار دفع مباشر أو 4 أقساط</li></ul><a href="#showcase" class="btn btn-secondary btn-block">شاهد البرنامج</a></article>
      </div>
      <p class="pricing-note"><b>قبل الاشتراك:</b> تواصل معنا للتأكد من تفاصيل العرض وطريقة الدفع المناسبة لنشاطك.</p>
    </div>
  </section>

  <section class="section faq" id="faq" aria-labelledby="faq-title">
    <div class="container faq__inner">
      <header class="section-head"><p class="eyebrow">قبل ما تبدأ</p><h2 id="faq-title">أسئلة ببالك؟</h2><p>أجوبة مباشرة عن نماء.</p></header>
      <div class="faq-list">
        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-1" aria-expanded="true" aria-controls="faq-answer-1">شو هو نماء؟<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-1" role="region" aria-labelledby="faq-question-1"><p>نظام محاسبي وإدارة أعمال يجمع المبيعات، المشتريات، المخزون، الحسابات والتقارير في مكان واحد.</p></div></article>
        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-2" aria-expanded="false" aria-controls="faq-answer-2">هل أقدر أشتغل إذا فصل الإنترنت؟<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-2" role="region" aria-labelledby="faq-question-2" hidden><p>نعم، بعد تسجيل الدخول وبدء البيع أونلاين. عند انقطاع الاتصال يمكنك مواصلة البيع من فاتورة البيع وPOS النقدي؛ الدعم لا يشمل كل النظام.</p></div></article>
        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-3" aria-expanded="false" aria-controls="faq-answer-3">شو بصير بالفواتير الأوفلاين؟<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-3" role="region" aria-labelledby="faq-question-3" hidden><p>تُحفظ العمليات محليًا وتظهر العمليات التي تنتظر المزامنة أعلى النظام. عند عودة الاتصال يمكنك مزامنتها، وإعادة المحاولة إذا تعذرت.</p></div></article>
        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-4" aria-expanded="false" aria-controls="faq-answer-4">هل أقدر أحدد صلاحيات الموظفين؟<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-4" role="region" aria-labelledby="faq-question-4" hidden><p>نعم، تحدد الأدوار والصلاحيات حسب مسؤولية كل مستخدم، بدون رسوم إضافية على ميزة الصلاحيات نفسها.</p></div></article>
        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-5" aria-expanded="false" aria-controls="faq-answer-5">هل يمكن تعديل النظام حسب طبيعة شغلي؟<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-5" role="region" aria-labelledby="faq-question-5" hidden><p>يمكن مناقشة تعديل أو إضافة وتنفيذ التخصيص المتفق عليه على نسختك بدون رسوم إضافية.</p></div></article>
      </div>
      <noscript><style>.faq-item__a[hidden]{display:block}.faq-item__icon{display:none}</style></noscript>
    </div>
  </section>

  <section class="section final-cta" aria-labelledby="final-title">
    <div class="container final-cta__inner"><p class="eyebrow eyebrow--light">خطوتك التالية</p><h2 id="final-title">جاهز تشوف نماء على شغلك؟</h2><p>اكتشف كيف نماء يرتّب المبيعات، المخزون والحسابات بمكان واحد.</p><a href="#showcase" class="btn btn-primary">شاهد البرنامج<svg aria-hidden="true"><use href="#icon-arrow-fwd"/></svg></a></div>
  </section>
</main>

<footer class="footer">
  <div class="container footer__inner">
    <a href="#top" class="brand" aria-label="نماء — العودة إلى البداية"><img class="brand__icon" src="assets/brand/icon-mark.webp" alt="" width="192" height="200" loading="lazy"><span class="brand__word">نماء<span class="brand__tagline">لحسابات تنمو</span></span></a>
    <nav class="footer__nav" aria-label="روابط التذييل"><a href="#mazaya">المميزات</a><a href="#showcase">شاهد نماء</a><a href="#pricing">الاشتراكات</a><a href="#faq">الأسئلة</a></nav>
    <p>© <span id="current-year">2026</span> نماء. جميع الحقوق محفوظة.</p>
  </div>
</footer>

<template id="tutorials-template"><section class="section tutorials" id="tutorials" aria-labelledby="tutorials-title"><div class="container"><header class="section-head"><h2 id="tutorials-title">شروحات نماء</h2><p>شروحات عملية تساعدك تتعرف على أدوات النظام.</p></header><div class="tutorials-grid"></div></div></section></template>

<dialog class="screenshot-dialog" id="screenshot-dialog" aria-labelledby="screenshot-dialog-title"><div class="screenshot-dialog__header"><h2 id="screenshot-dialog-title">شاشة نماء</h2><button type="button" class="dialog-close" aria-label="إغلاق الصورة" autofocus><span aria-hidden="true">×</span></button></div><div class="screenshot-dialog__body"><img id="screenshot-dialog-image" alt="" width="1919" height="870"></div><div class="screenshot-dialog__footer"><span>صورة فعلية من نماء</span><a id="screenshot-original-link" target="_blank" rel="noopener noreferrer">فتح بالحجم الأصلي<svg aria-hidden="true"><use href="#icon-scan"/></svg></a></div></dialog>

<script src="js/site-config.js?v=20260916premium" defer></script>
<script src="js/hardware-data.js?v=20260916premium" defer></script>
<script src="js/tutorials-data.js?v=20260916premium" defer></script>
<script src="js/main.js?v=20260916premium" defer></script>
</body>
</html>
'''

(ROOT / "index.html").write_text(head_and_sprite + body, encoding="utf-8")
print("index.html rewritten")
