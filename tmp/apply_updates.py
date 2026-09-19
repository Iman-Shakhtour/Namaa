from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Update Bento Grid in HTML
old_bento = """      <div class="bento-grid">
        <article class="bento-card bento-card--hero">
          <div class="bento-card__copy"><span>01</span><h3>نقطة البيع</h3><p>بيع سريع بالاسم أو الباركود، مع سلة وطرق دفع واضحة.</p></div>
          <img src="assets/screenshots/namaa-pos-current.webp" alt="واجهة نقطة البيع الحقيقية في نماء" width="1919" height="720" loading="eager" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>02</span><h3>المخزون</h3><p>الأصناف والكميات والأسعار في شاشة واحدة.</p></div>
          <img src="assets/screenshots/namaa-inventory-current.webp" alt="قائمة الأصناف والمخزون الحقيقية في نماء" width="1919" height="520" loading="eager" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>03</span><h3>التقارير</h3><p>مبيعات وتكلفة وربح للفترة التي تختارها.</p></div>
          <img src="assets/screenshots/namaa-profit-current.webp" alt="أرقام تقرير الأرباح الحقيقي في نماء" width="1901" height="680" loading="eager" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>04</span><h3>المحاسبة</h3><p>صندوق ومصروفات وشيكات وحركة مالية أوضح.</p></div>
          <img src="assets/screenshots/namaa-accounting-current.webp" alt="القيود المحاسبية الحقيقية في نماء" width="1918" height="650" loading="eager" decoding="async">
        </article>
        <article class="bento-card">
          <div class="bento-card__copy"><span>05</span><h3>العملاء والموردون</h3><p>أرصدة وكشوف حساب مرتبطة بكل حركة بيع وشراء.</p></div>
          <img src="assets/screenshots/namaa-customers-current.webp" alt="تقرير ذمم العملاء الحقيقي في نماء" width="1919" height="610" loading="eager" decoding="async">
        </article>
      </div>"""

new_bento = """      <div class="bento-grid">
        <article class="bento-card bento-card--hero">
          <div class="bento-card__copy">
            <span>01</span>
            <h3>نقطة البيع (POS)</h3>
            <p>بيع سريع بالاسم أو الباركود، مع سلة مشتريات سلسة وخيارات دفع نقدية وآجلة فورية.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-pos-current.webp" alt="واجهة نقطة البيع الحقيقية في نماء" width="1919" height="720" loading="eager" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>02</span>
            <h3>المخزون والأصناف</h3>
            <p>الأصناف والكميات والأسعار والوحدات في شاشة منظمة وشاملة.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-inventory-current.webp" alt="قائمة الأصناف والمخزون الحقيقية في نماء" width="1919" height="520" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>03</span>
            <h3>تقارير الأرباح والمبيعات</h3>
            <p>مبيعات وتكلفة وصافي ربح دقيق لأي فترة تختارها بضغطة زر.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-profit-current.webp" alt="أرقام تقرير الأرباح الحقيقي في نماء" width="1901" height="680" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>04</span>
            <h3>المحاسبة والقيود</h3>
            <p>صندوق، مصروفات، شيكات، وحركة مالية دقيقة لكل مدفوع ومقبوض.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-accounting-current.webp" alt="القيود المحاسبية الحقيقية في نماء" width="1918" height="650" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>05</span>
            <h3>العملاء والموردون</h3>
            <p>أرصدة، كشوفات حساب، وتتبع ديون دقيق مرتبط بكل فاتورة بيع وشراء.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-customers-current.webp" alt="تقرير ذمم العملاء الحقيقي في نماء" width="1919" height="610" loading="lazy" decoding="async">
          </div>
        </article>
      </div>"""

# 2. Update Offline in HTML
old_offline = """        <ol class="workflow" aria-label="مراحل العمل دون اتصال">
          <li><img src="assets/screenshots/namaa-sync-offline-full.webp" alt="واجهة نماء الكاملة أثناء العمل دون اتصال" width="1919" height="872" loading="eager"><div><b>1</b><h3>دون اتصال</h3><p>واصل البيع من فاتورة البيع وPOS النقدي.</p></div></li>
          <li><img src="assets/screenshots/namaa-sync-pending-full.webp" alt="واجهة نماء الكاملة وفيها عمليتان بانتظار المزامنة" width="1916" height="870" loading="eager"><div><b>2</b><h3>بانتظار المزامنة</h3><p>تُحفظ العمليات محليًا حتى يعود الاتصال.</p></div></li>
          <li><img src="assets/screenshots/namaa-sync-complete-full.webp" alt="واجهة نماء الكاملة أثناء مزامنة العمليات" width="1919" height="875" loading="eager"><div><b>3</b><h3>مزامنة العمليات</h3><p>ترجع العمليات للنظام بعد عودة الاتصال.</p></div></li>
        </ol>"""

new_offline = """        <ol class="workflow" aria-label="مراحل العمل دون اتصال">
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-offline-full.webp" alt="واجهة نماء الكاملة أثناء العمل دون اتصال مع حالة الشبكة" width="1919" height="872" loading="lazy">
            </div>
            <div class="workflow__content">
              <b>1</b>
              <h3>دون اتصال</h3>
              <p>واصل البيع من فاتورة البيع وPOS النقدي حتى لو انقطع الإنترنت تماماً.</p>
            </div>
          </li>
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-pending-full.webp" alt="واجهة نماء وفيها تنبيه العمليات المعلقة بانتظار المزامنة" width="1916" height="870" loading="lazy">
            </div>
            <div class="workflow__content">
              <b>2</b>
              <h3>بانتظار المزامنة</h3>
              <p>تُحفظ العمليات محلياً ويظهر عداد العمليات المعلقة أعلى النظام بوضوح.</p>
            </div>
          </li>
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-complete-full.webp" alt="واجهة نماء أثناء مزامنة العمليات مع السيرفر" width="1919" height="875" loading="lazy">
            </div>
            <div class="workflow__content">
              <b>3</b>
              <h3>مزامنة العمليات</h3>
              <p>تُرفع العمليات وتُعتمد فوراً بعد عودة الاتصال بضغطة زر وبلا فقدان بيانات.</p>
            </div>
          </li>
        </ol>"""

# 3. Update Pricing in HTML
old_pricing = """      <div class="pricing-grid">
        <article class="price-card price-card--featured"><span class="price-card__badge">الخيار الأول</span><h3>امتلاك نماء مدى الحياة</h3><p class="price-card__desc">دفعة واحدة، بدون رسوم تجديد سنوية حسب هذا العرض.</p><div class="price-main"><b><small>$</small>1600</b><span>دفعة واحدة</span></div><div class="price-or">أو بالتقسيط</div><div class="price-installment"><div><b><small>$</small>300</b><span>شهريًا</span></div><em>6 دفعات · الإجمالي 1800$</em></div><ul class="check-list price-card__list"><li>امتلاك مدى الحياة</li><li>خيار دفع مباشر أو 6 أقساط</li></ul><a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84%20%D8%B9%D8%B1%D8%B6%20%D9%86%D9%85%D8%A7%D8%A1" class="btn btn-primary btn-block" target="_blank" rel="noopener noreferrer">اسأل عن العرض عالواتساب</a></article>
        <article class="price-card"><span class="price-card__badge price-card__badge--soft">الخيار الثاني</span><h3>سعر بداية أقل</h3><p class="price-card__desc">مع 100$ سنويًا للتجديد والتحديثات والصيانة والدعم الفني.</p><div class="price-main"><b><small>$</small>1000</b><span>دفعة واحدة</span></div><div class="price-renew"><b>+$100</b> سنويًا للتجديد والتحديثات والصيانة والدعم الفني</div><div class="price-or">أو بالتقسيط</div><div class="price-installment"><div><b><small>$</small>300</b><span>شهريًا</span></div><em>4 دفعات · الإجمالي 1200$ + 100$ سنويًا</em></div><ul class="check-list price-card__list"><li>سعر بداية أقل</li><li>خيار دفع مباشر أو 4 أقساط</li></ul><a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84%20%D8%B9%D8%B1%D8%B6%20%D9%86%D9%85%D8%A7%D8%A1" class="btn btn-secondary btn-block" target="_blank" rel="noopener noreferrer">اسأل عن العرض عالواتساب</a></article>
      </div>"""

new_pricing = """      <div class="pricing-grid">
        <article class="price-card price-card--featured">
          <div class="price-card__header">
            <span class="price-card__badge price-card__badge--featured">الخيار الأول · مدى الحياة</span>
            <h3>امتلاك نماء مدى الحياة</h3>
            <p class="price-card__desc">دفعة واحدة، بدون رسوم تجديد سنوية إطلاقاً حسب هذا العرض.</p>
          </div>

          <div class="price-main price-main--featured">
            <span class="price-tag-label">الدفعة الكاملة المباشرة</span>
            <div class="price-amount-row">
              <b><small>$</small>1600</b>
              <span class="price-badge-pill">دفعة واحدة للأبد</span>
            </div>
            <p class="price-subtext">امتلاك دائم للنسخة بدون أي اشتراك أو تجديد سنوي</p>
          </div>

          <div class="price-divider"><span>أو خيار التقسيط الميسّر</span></div>

          <div class="price-installment price-installment--featured">
            <div class="price-installment__top">
              <b><small>$</small>300</b>
              <span>شهريًا</span>
            </div>
            <div class="price-installment__detail">
              <span class="installment-badge">6 دفعات فقط</span>
              <em>الإجمالي 1800$ (امتلاك دائم)</em>
            </div>
          </div>

          <ul class="check-list price-card__list">
            <li>امتلاك كامل مدى الحياة بدون انقطاع</li>
            <li>خيار دفع مباشر (1600$) أو 6 أقساط شهرية (300$)</li>
            <li>التحديثات والصيانة والدعم الفني مشمولة</li>
          </ul>

          <a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84%20%D8%B9%D8%B1%D8%B6%20%D8%A7%D9%84%D8%A7%D9%85%D8%AA%D9%84%D8%A7%D9%83%20%D9%85%D8%AF%D9%89%20%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9%20%D9%84%D9%86%D9%85%D8%A7%D8%A1" class="btn btn-primary btn-block btn-lg" target="_blank" rel="noopener noreferrer">اسأل عن عرض مدى الحياة عالواتساب<svg aria-hidden="true"><use href="#icon-whatsapp"/></svg></a>
        </article>

        <article class="price-card price-card--flex">
          <div class="price-card__header">
            <span class="price-card__badge price-card__badge--navy">الخيار الثاني · بداية مرنة</span>
            <h3>سعر بداية أقل</h3>
            <p class="price-card__desc">ادفع أقل في البداية مع 100$ سنويًا للتجديد والتحديثات والصيانة والدعم الفني.</p>
          </div>

          <div class="price-main price-main--navy">
            <span class="price-tag-label">دفعة البداية المباشرة</span>
            <div class="price-amount-row">
              <b><small>$</small>1000</b>
              <span class="price-badge-pill price-badge-pill--navy">دفعة واحدة</span>
            </div>
            <p class="price-subtext">سعر دخول منخفض لتشغيل نشاطك فوراً</p>
          </div>

          <div class="price-renew">
            <div class="price-renew__icon">⚡</div>
            <div class="price-renew__text">
              <b>+$100 سنويًا فقط</b>
              <span>للتجديد السنوي، التحديثات المستمرة، والصيانة والدعم الفني</span>
            </div>
          </div>

          <div class="price-divider"><span>أو خيار التقسيط الميسّر</span></div>

          <div class="price-installment price-installment--navy">
            <div class="price-installment__top">
              <b><small>$</small>300</b>
              <span>شهريًا</span>
            </div>
            <div class="price-installment__detail">
              <span class="installment-badge installment-badge--cyan">4 دفعات فقط</span>
              <em>الإجمالي 1200$ + 100$ سنويًا للتجديد</em>
            </div>
          </div>

          <ul class="check-list price-card__list">
            <li>سعر بداية أقل يناسب انطلاقة مشروعك</li>
            <li>خيار دفع مباشر (1000$) أو 4 أقساط شهرية (300$)</li>
            <li>تجديد سنوي بسيط يشمل الدعم الفني والتحديثات</li>
          </ul>

          <a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84%20%D8%B9%D8%B1%D8%B6%20%D8%A7%D9%84%D8%A8%D8%AF%D8%A7%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D8%B1%D9%86%D8%A9%20%D9%84%D9%86%D9%85%D8%A7%D8%A1" class="btn btn-navy btn-block btn-lg" target="_blank" rel="noopener noreferrer">اسأل عن عرض البداية المرنة عالواتساب<svg aria-hidden="true"><use href="#icon-whatsapp"/></svg></a>
        </article>
      </div>"""

if old_bento in html:
    html = html.replace(old_bento, new_bento)
    print("Bento grid updated in HTML")
else:
    print("Warning: old_bento not found")

if old_offline in html:
    html = html.replace(old_offline, new_offline)
    print("Offline workflow updated in HTML")
else:
    print("Warning: old_offline not found")

if old_pricing in html:
    html = html.replace(old_pricing, new_pricing)
    print("Pricing updated in HTML")
else:
    print("Warning: old_pricing not found")

html_path.write_text(html, encoding="utf-8")
print("index.html saved successfully.")

