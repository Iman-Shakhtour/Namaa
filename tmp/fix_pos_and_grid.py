from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Update Bento Grid in HTML to uniform features grid with real POS image
old_features_html = """      <div class="bento-grid">
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

new_features_html = """      <div class="bento-grid">
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>01</span>
            <h3>نقطة البيع (POS)</h3>
            <p>بيع سريع بالاسم أو الباركود، سلة مشتريات سلسة وخيارات دفع نقدية وآجلة فورية.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-pos-current.webp" alt="واجهة نقطة البيع الحقيقية في نماء" width="1919" height="870" loading="eager" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>02</span>
            <h3>المخزون والأصناف</h3>
            <p>الأصناف والكميات والأسعار والوحدات في شاشة منظمة وشاملة.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-inventory-current.webp" alt="قائمة الأصناف والمخزون الحقيقية في نماء" width="1919" height="867" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>03</span>
            <h3>تقارير الأرباح والمبيعات</h3>
            <p>مبيعات وتكلفة وصافي ربح دقيق لأي فترة تختارها بضغطة زر.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-profit-current.webp" alt="أرقام تقرير الأرباح الحقيقي في نماء" width="1901" height="870" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>04</span>
            <h3>المحاسبة والقيود</h3>
            <p>صندوق، مصروفات، شيكات، وحركة مالية دقيقة لكل مدفوع ومقبوض.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-accounting-current.webp" alt="القيود المحاسبية الحقيقية في نماء" width="1918" height="868" loading="lazy" decoding="async">
          </div>
        </article>
        <article class="bento-card">
          <div class="bento-card__copy">
            <span>05</span>
            <h3>العملاء والموردون</h3>
            <p>أرصدة، كشوفات حساب، وتتبع ديون دقيق مرتبط بكل فاتورة بيع وشراء.</p>
          </div>
          <div class="bento-card__media">
            <img src="assets/screenshots/namaa-customers-current.webp" alt="تقرير ذمم العملاء الحقيقي في نماء" width="1919" height="868" loading="lazy" decoding="async">
          </div>
        </article>
      </div>"""

assert old_features_html in html, "old_features_html not found"
html = html.replace(old_features_html, new_features_html)
html_path.write_text(html, encoding="utf-8")
print("index.html features updated successfully!")

# 2. Update CSS so all feature cards are uniform and balanced
old_bento_css = """.bento-card{display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
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

new_bento_css = """.bento-card{display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.bento-card:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgb(7 24 47 / 8%);border-color:rgb(13 147 104 / 35%)}
.bento-card__copy{padding:26px 26px 16px}
.bento-card__copy>span,.story-mobile article>div>span{display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.bento-card h3{margin-top:10px;font-size:22px}
.bento-card p{margin-top:6px;color:var(--muted);font-size:15px;line-height:1.6}
.bento-card__media{position:relative;margin-top:auto;padding-inline:16px;padding-top:12px;background:linear-gradient(180deg, transparent 0%, #f1f5f9 100%)}
.bento-card__media img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top right;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--white);box-shadow:0 -2px 12px rgb(0 0 0 / 3%);transition:transform .3s ease}
.bento-card:hover .bento-card__media img{transform:scale(1.02)}"""

if old_bento_css in css:
    css = css.replace(old_bento_css, new_bento_css)

# Remove .bento-card--hero from media queries
css = css.replace(".bento-card--hero{grid-column:1 / -1}\n", "")
css = css.replace(".bento-card--hero{grid-column:1 / -1}", "")
css = css.replace(".bento-card--hero .bento-card__media img{max-height:340px}", "")

css_path.write_text(css, encoding="utf-8")
print("css/style.css bento-card updated successfully!")

