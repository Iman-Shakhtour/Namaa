from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Update index.html environment section
old_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
    <div class="container">
      <header class="section-head"><p class="eyebrow">جاهز من أول يوم</p><h2 id="environment-title">كل اللي تحتاجه لتبدأ بثقة</h2><p>تجربة ودعم وتجهيزات عملية بدون ما تشتت حالك بين أكثر من جهة.</p></header>
      <div class="environment-list">
        <article><span>01</span><h3>جرّبه وتعلّمه بسهولة</h3><p>نسخة تجريبية، دليل استخدام كامل، ودعم فني على مدار الساعة.</p></article>
        <article><span>02</span><h3>محلك جاهز للشغل</h3><p>نوفر أجهزة نقطة البيع، ويمكن ترتيب إدخال الأصناف كخدمة إضافية.</p></article>
        <article><span>03</span><h3>مرن وآمن على كل جهاز</h3><p>صلاحيات RBAC، مساحة غير محدودة، أونلاين وأوفلاين، ويعمل على اللابتوب والتلفون والآيباد.</p></article>
      </div>
      <div class="customization"><h2>شغلك مختلف؟ نماء بيتكيّف.</h2><p>يمكن تنفيذ التخصيص المتفق عليه على نسختك بدون رسوم إضافية.</p></div>
    </div>
  </section>"""

new_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
    <div class="container">
      <header class="section-head center">
        <p class="eyebrow">جاهز من أول يوم</p>
        <h2 id="environment-title">كل اللي تحتاجه لتبدأ بثقة</h2>
        <p>تجربة ودعم وتجهيزات عملية بدون ما تشتت حالك بين أكثر من جهة.</p>
      </header>
      
      <div class="env-grid">
        <article class="env-card env-card--emerald">
          <div class="env-card__icon-wrap">
            <span class="env-card__badge">01</span>
            <span class="env-card__icon">🚀</span>
          </div>
          <h3>جرّبه وتعلّمه بسهولة</h3>
          <p>نسخة تجريبية حقيقية، دليل استخدام كامل، ودعم فني متخصص على مدار الساعة لمساعدتك بأي وقت.</p>
          <ul class="env-card__tags">
            <li>نسخة تجريبية</li>
            <li>دليل شامل</li>
            <li>دعم فني 24/7</li>
          </ul>
        </article>

        <article class="env-card env-card--blue">
          <div class="env-card__icon-wrap">
            <span class="env-card__badge">02</span>
            <span class="env-card__icon">🏪</span>
          </div>
          <h3>محلك جاهز للشغل</h3>
          <p>نوفر أجهزة نقطة البيع المتوافقة (طابعات وباركود)، مع خدمة إضافية لإدخال وتجهيز الأصناف.</p>
          <ul class="env-card__tags">
            <li>أجهزة POS متوافقة</li>
            <li>خدمة إدخال الأصناف</li>
            <li>انطلاقة فورية</li>
          </ul>
        </article>

        <article class="env-card env-card--purple">
          <div class="env-card__icon-wrap">
            <span class="env-card__badge">03</span>
            <span class="env-card__icon">🛡️</span>
          </div>
          <h3>مرن وآمن على كل جهاز</h3>
          <p>صلاحيات متقدمة (RBAC)، مساحة غير محدودة، عمل أوفلاين وأونلاين على اللابتوب والموبايل والتابلت.</p>
          <ul class="env-card__tags">
            <li>صلاحيات RBAC</li>
            <li>سحابة غير محدودة</li>
            <li>لابتوب · موبايل · تابلت</li>
          </ul>
        </article>
      </div>

      <div class="customization-card">
        <div class="customization-card__copy">
          <span class="customization-card__badge">✨ مرونة كاملة</span>
          <h2>شغلك مختلف؟ نماء بيتكيّف.</h2>
          <p>نناقش معك طبيعة نشاطك وننفّذ التخصيص والإضافات المتفق عليها على نسختك الخاصة بدون أي رسوم إضافية.</p>
        </div>
        <a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D9%85%D9%86%D8%A7%D9%82%D8%B4%D8%A9%20%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5%20%D9%86%D8%B3%D8%AE%D8%A9%20%D9%86%D9%85%D8%A7%D8%A1%20%D9%84%D9%86%D8%B4%D8%A7%D8%B7%D9%8A" class="btn btn-primary btn-lg" target="_blank" rel="noopener noreferrer">
          اطلب تخصيص نسختك
          <svg aria-hidden="true"><use href="#icon-whatsapp"/></svg>
        </a>
      </div>
    </div>
  </section>"""

assert old_env_html in html, "old_env_html not found"
html = html.replace(old_env_html, new_env_html)
html_path.write_text(html, encoding="utf-8")
print("index.html environment updated successfully!")

# 2. Update CSS for environment section
old_env_css = """/* Environment and customization */
.environment{background:var(--bg)}
.environment-list{display:grid;border-top:1px solid var(--border)}
.environment-list article{padding:24px 0;border-bottom:1px solid var(--border)}
.environment-list span{color:var(--green);font-size:14px;font-weight:800}
.environment-list h3{margin-top:6px}
.environment-list p{margin-top:6px;color:var(--muted);font-size:15px}
.customization{display:grid;gap:16px;margin-top:48px;padding-top:48px;border-top:1px solid var(--border)}
.customization h2{font-size:clamp(28px,3vw,40px)}
.customization>p{max-width:540px;color:var(--muted);font-size:17px}"""

new_env_css = """/* Environment Section with rich cards and dynamic customization box */
.environment{background:var(--bg)}
.env-grid{display:grid;grid-template-columns:1fr;gap:24px}
.env-card{position:relative;display:flex;flex-direction:column;padding:32px 26px;border-radius:var(--radius-lg);background:var(--white);border:1px solid var(--border);box-shadow:0 6px 24px rgb(7 24 47 / 4%);transition:transform .3s cubic-bezier(0.16,1,0.3,1),box-shadow .3s ease,border-color .3s ease}
.env-card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgb(7 24 47 / 10%)}

.env-card--emerald{border-top:4px solid #0D9368}
.env-card--emerald:hover{border-color:#0D9368}
.env-card--blue{border-top:4px solid #0284C7}
.env-card--blue:hover{border-color:#0284C7}
.env-card--purple{border-top:4px solid #7C3AED}
.env-card--purple:hover{border-color:#7C3AED}

.env-card__icon-wrap{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
.env-card__badge{display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;font-size:13px;font-weight:800}
.env-card--emerald .env-card__badge{background:#E6F8F0;color:#0D9368}
.env-card--blue .env-card__badge{background:#E0F2FE;color:#0284C7}
.env-card--purple .env-card__badge{background:#F3E8FF;color:#7C3AED}

.env-card__icon{font-size:30px;line-height:1;display:inline-block;transition:transform .3s ease}
.env-card:hover .env-card__icon{transform:scale(1.15) rotate(6deg)}

.env-card h3{font-size:22px;color:var(--text);margin-bottom:10px}
.env-card p{color:var(--muted);font-size:15px;line-height:1.6;margin-bottom:20px}

.env-card__tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:16px;border-top:1px solid var(--border)}
.env-card__tags li{padding:4px 10px;border-radius:6px;font-size:12px;font-weight:700}
.env-card--emerald .env-card__tags li{background:#F0FDF4;color:#15803D;border:1px solid #DCFCE7}
.env-card--blue .env-card__tags li{background:#F0F9FF;color:#0369A1;border:1px solid #E0F2FE}
.env-card--purple .env-card__tags li{background:#FAF5FF;color:#6B21A8;border:1px solid #F3E8FF}

/* Customization Card */
.customization-card{position:relative;display:flex;flex-direction:column;gap:24px;margin-top:48px;padding:36px 32px;border-radius:var(--radius-lg);background:linear-gradient(135deg, #07182F 0%, #0B2546 50%, #064E3B 100%);color:var(--white);box-shadow:0 20px 50px rgb(7 24 47 / 18%);overflow:hidden}
.customization-card::before{content:'';position:absolute;top:-50%;right:-20%;width:300px;height:300px;background:radial-gradient(circle, rgba(18,184,134,0.2) 0%, transparent 70%);border-radius:50%;pointer-events:none}
.customization-card__copy{position:relative;z-index:2;max-width:680px}
.customization-card__badge{display:inline-block;padding:5px 12px;border-radius:999px;background:rgb(18 184 134 / 20%);color:var(--green-bright);border:1px solid rgb(18 184 134 / 35%);font-size:13px;font-weight:800;margin-bottom:12px}
.customization-card h2{color:var(--white);font-size:clamp(26px,3vw,38px);margin-bottom:10px}
.customization-card p{color:rgb(255 255 255 / 80%);font-size:16px;line-height:1.6}
.customization-card .btn{position:relative;z-index:2;align-self:flex-start}"""

assert old_env_css in css, "old_env_css not found"
css = css.replace(old_env_css, new_env_css)

# Update responsive queries
old_mq = """.environment-list{grid-template-columns:repeat(3,minmax(0,1fr))}
  .environment-list article{padding:24px;border-inline-start:1px solid var(--border)}
  .environment-list article:first-child{border-inline-start:0}
  .customization{grid-template-columns:1fr 1fr;align-items:start}"""

new_mq = """.env-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
  .customization-card{flex-direction:row;justify-content:space-between;align-items:center;padding:40px 48px}"""

if old_mq in css:
    css = css.replace(old_mq, new_mq)

css_path.write_text(css, encoding="utf-8")
print("css/style.css environment updated successfully!")

