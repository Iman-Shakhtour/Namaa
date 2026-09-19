from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Update HTML for Environment Section to match Namaa's core design system 100%
old_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
    <div class="container">
      <header class="section-head center">
        <p class="eyebrow">جاهز من أول يوم</p>
        <h2 id="environment-title">كل اللي تحتاجه لتبدأ بثقة</h2>
        <p>تجربة ودعم وتجهيزات عملية متكاملة بدون تشتيت بين جهات متعددة.</p>
      </header>
      
      <div class="env-grid">
        <article class="env-card env-card--emerald">
          <div class="env-card__top">
            <div class="env-card__icon-box">
              <svg aria-hidden="true"><use href="#icon-support-headset"/></svg>
            </div>
            <span class="env-card__index">01</span>
          </div>
          <h3>جرّبه وتعلّمه بسهولة</h3>
          <p>نسخة تجريبية حقيقية، دليل استخدام كامل، ودعم فني متخصص على مدار الساعة لمساعدتك بأي وقت.</p>
          <div class="env-card__pills">
            <span>نسخة تجريبية</span>
            <span>دليل شامل</span>
            <span>دعم فني 24/7</span>
          </div>
        </article>

        <article class="env-card env-card--blue">
          <div class="env-card__top">
            <div class="env-card__icon-box">
              <svg aria-hidden="true"><use href="#icon-store-pos"/></svg>
            </div>
            <span class="env-card__index">02</span>
          </div>
          <h3>محلك جاهز للشغل</h3>
          <p>نوفر أجهزة نقطة البيع المتوافقة (طابعات وباركود)، مع خدمة إضافية لإدخال وتجهيز الأصناف.</p>
          <div class="env-card__pills">
            <span>أجهزة POS متوافقة</span>
            <span>إدخال الأصناف</span>
            <span>انطلاقة فورية</span>
          </div>
        </article>

        <article class="env-card env-card--purple">
          <div class="env-card__top">
            <div class="env-card__icon-box">
              <svg aria-hidden="true"><use href="#icon-shield-device"/></svg>
            </div>
            <span class="env-card__index">03</span>
          </div>
          <h3>مرن وآمن على كل جهاز</h3>
          <p>صلاحيات متقدمة (RBAC)، مساحة غير محدودة، عمل أوفلاين وأونلاين على اللابتوب والموبايل والتابلت.</p>
          <div class="env-card__pills">
            <span>صلاحيات RBAC</span>
            <span>سحابة غير محدودة</span>
            <span>لابتوب · موبايل · تابلت</span>
          </div>
        </article>
      </div>

      <div class="customization-card">
        <div class="customization-card__copy">
          <span class="customization-card__badge">تخصيص كامل</span>
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

new_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
    <div class="container">
      <header class="section-head center">
        <p class="eyebrow">جاهز من أول يوم</p>
        <h2 id="environment-title">كل اللي تحتاجه لتبدأ بثقة</h2>
        <p>تجربة ودعم وتجهيزات عملية بدون ما تشتت حالك بين أكثر من جهة.</p>
      </header>
      
      <div class="env-grid">
        <article class="env-card">
          <span class="env-card__badge">01</span>
          <h3>جرّبه وتعلّمه بسهولة</h3>
          <p>نسخة تجريبية حقيقية، دليل استخدام شامل، ودعم فني على مدار الساعة.</p>
          <ul class="check-list env-card__list">
            <li>نسخة تجريبية لتجربة النظام بنفسك</li>
            <li>دليل استخدام كامل وشروحات واضحة</li>
            <li>دعم فني متواصل لمساعدتك بأي وقت</li>
          </ul>
        </article>

        <article class="env-card">
          <span class="env-card__badge">02</span>
          <h3>محلك جاهز للشغل</h3>
          <p>نوفر أجهزة نقطة البيع، ويمكن ترتيب إدخال الأصناف كخدمة إضافية.</p>
          <ul class="check-list env-card__list">
            <li>توفير أجهزة نقطة البيع المعتمدة</li>
            <li>إمكانية إدخال وتجهيز الأصناف لنشاطك</li>
            <li>انطلاقة سريعة وجاهزية تامة للبيع</li>
          </ul>
        </article>

        <article class="env-card">
          <span class="env-card__badge">03</span>
          <h3>مرن وآمن على كل جهاز</h3>
          <p>صلاحيات RBAC، مساحة غير محدودة، أونلاين وأوفلاين، ويعمل على كل جهاز.</p>
          <ul class="check-list env-card__list">
            <li>تحديد أدوار وصلاحيات الموظفين (RBAC)</li>
            <li>مساحة تخزين غير محدودة وأمان للبيانات</li>
            <li>يعمل على اللابتوب، التابلت، والموبايل</li>
          </ul>
        </article>
      </div>

      <div class="customization-card">
        <div class="customization-card__copy">
          <p class="eyebrow eyebrow--light">تخصيص كامل</p>
          <h2>شغلك مختلف؟ نماء بيتكيّف.</h2>
          <p>نناقش معك طبيعة نشاطك وننفّذ التخصيص والإضافات المتفق عليها على نسختك بدون أي رسوم إضافية.</p>
        </div>
        <a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D9%85%D9%86%D8%A7%D9%82%D8%B4%D8%A9%20%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5%20%D9%86%D8%B3%D8%AE%D8%A9%20%D9%86%D9%85%D8%A7%D8%A1%20%D9%84%D9%86%D8%B4%D8%A7%D8%B7%D9%8A" class="btn btn-primary" target="_blank" rel="noopener noreferrer">
          تواصل لتخصيص نسختك
          <svg aria-hidden="true"><use href="#icon-whatsapp"/></svg>
        </a>
      </div>
    </div>
  </section>"""

assert old_env_html in html, "old_env_html not found"
html = html.replace(old_env_html, new_env_html)
html_path.write_text(html, encoding="utf-8")
print("index.html environment updated successfully with matching Namaa design!")

# 2. Update CSS to match Namaa's core design system 100%
old_env_css = """/* Environment Section with ultra-modern SaaS cards & refined vector icons */
.environment{background:var(--bg)}
.env-grid{display:grid;grid-template-columns:1fr;gap:24px}
.env-card{position:relative;display:flex;flex-direction:column;padding:32px 28px;border-radius:var(--radius-lg);background:linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);border:1px solid var(--border);box-shadow:0 6px 24px rgb(7 24 47 / 4%);transition:transform .3s cubic-bezier(0.16,1,0.3,1),box-shadow .3s ease,border-color .3s ease}
.env-card:hover{transform:translateY(-6px);box-shadow:0 20px 44px rgb(7 24 47 / 9%)}

.env-card--emerald{border-top:3px solid var(--green)}
.env-card--emerald:hover{border-color:var(--green)}
.env-card--blue{border-top:3px solid #0284C7}
.env-card--blue:hover{border-color:#0284C7}
.env-card--purple{border-top:3px solid #6366F1}
.env-card--purple:hover{border-color:#6366F1}

.env-card__top{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.env-card__icon-box{display:inline-grid;place-items:center;width:48px;height:48px;border-radius:14px;transition:transform .3s ease}
.env-card:hover .env-card__icon-box{transform:scale(1.08)}
.env-card__icon-box svg{width:24px;height:24px}

.env-card--emerald .env-card__icon-box{background:linear-gradient(135deg, #E6F8F0 0%, #CEF5E4 100%);color:var(--green);border:1px solid rgb(13 147 104 / 20%)}
.env-card--blue .env-card__icon-box{background:linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);color:#0284C7;border:1px solid rgb(2 132 199 / 20%)}
.env-card--purple .env-card__icon-box{background:linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);color:#6366F1;border:1px solid rgb(99 102 241 / 20%)}

.env-card__index{font-size:14px;font-weight:800;color:var(--muted);opacity:.6;letter-spacing:1px}

.env-card h3{font-size:22px;color:var(--text);margin-bottom:10px}
.env-card p{color:var(--muted);font-size:15px;line-height:1.65;margin-bottom:22px}

.env-card__pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:18px;border-top:1px solid var(--border)}
.env-card__pills span{padding:5px 12px;border-radius:8px;font-size:12px;font-weight:700}
.env-card--emerald .env-card__pills span{background:#F0FDF4;color:#15803D;border:1px solid #DCFCE7}
.env-card--blue .env-card__pills span{background:#F0F9FF;color:#0369A1;border:1px solid #E0F2FE}
.env-card--purple .env-card__pills span{background:#EEF2FF;color:#4338CA;border:1px solid #E0E7FF}

/* Customization Card */
.customization-card{position:relative;display:flex;flex-direction:column;gap:24px;margin-top:48px;padding:38px 34px;border-radius:var(--radius-lg);background:linear-gradient(135deg, #07182F 0%, #0F2D54 60%, #064E3B 100%);color:var(--white);box-shadow:0 20px 50px rgb(7 24 47 / 18%);overflow:hidden}
.customization-card::before{content:'';position:absolute;top:-50%;right:-20%;width:320px;height:320px;background:radial-gradient(circle, rgba(18,184,134,0.22) 0%, transparent 70%);border-radius:50%;pointer-events:none}
.customization-card__copy{position:relative;z-index:2;max-width:680px}
.customization-card__badge{display:inline-block;padding:5px 14px;border-radius:999px;background:rgb(18 184 134 / 20%);color:var(--green-bright);border:1px solid rgb(18 184 134 / 35%);font-size:13px;font-weight:800;margin-bottom:12px}
.customization-card h2{color:var(--white);font-size:clamp(26px,3vw,38px);margin-bottom:10px}
.customization-card p{color:rgb(255 255 255 / 82%);font-size:16px;line-height:1.6}
.customization-card .btn{position:relative;z-index:2;align-self:flex-start}"""

new_env_css = """/* Environment & Customization matching Namaa Design System */
.environment{background:var(--bg)}
.env-grid{display:grid;grid-template-columns:1fr;gap:20px}
.env-card{display:flex;flex-direction:column;padding:28px;border-radius:var(--radius-lg);background:var(--white);border:1px solid var(--border);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.env-card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgb(7 24 47 / 8%);border-color:rgb(13 147 104 / 35%)}
.env-card__badge{align-self:flex-start;display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.env-card h3{margin-top:14px;font-size:22px;color:var(--text)}
.env-card>p{margin-top:8px;color:var(--muted);font-size:15px;line-height:1.6}
.env-card__list{margin-top:auto;padding-top:18px;border-top:1px solid var(--border)}
.env-card__list li{font-size:14px}

/* Customization Card */
.customization-card{display:flex;flex-direction:column;gap:20px;margin-top:48px;padding:32px 28px;border-radius:var(--radius-lg);background:var(--navy);border:1px solid rgb(255 255 255 / 12%);color:var(--white);box-shadow:var(--shadow-product)}
.customization-card__copy{max-width:680px}
.customization-card h2{margin-top:6px;color:var(--white);font-size:clamp(24px,3vw,34px)}
.customization-card>div>p:not(.eyebrow){margin-top:8px;color:rgb(255 255 255 / 76%);font-size:16px;line-height:1.6}
.customization-card .btn{align-self:flex-start}"""

assert old_env_css in css, "old_env_css not found"
css = css.replace(old_env_css, new_env_css)
css_path.write_text(css, encoding="utf-8")
print("css/style.css environment updated successfully with matching Namaa design!")

