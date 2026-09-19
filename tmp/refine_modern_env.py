from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Add sleek modern SVG icons to the SVG sprite if not already present
new_symbols = """  <symbol id="icon-support-headset" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/><path d="M18 19a6 6 0 0 1-6 3v-2"/></g></symbol>
  <symbol id="icon-store-pos" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20M12 16v4M8 12h8M7 8h2M11 8h2M15 8h2"/></g></symbol>
  <symbol id="icon-shield-device" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.5 19 6v6c0 4.3-3 7.4-7 8.5-4-1.1-7-4.2-7-8.5V6l7-2.5Z"/><path d="M9 12l2 2 4-4.5"/></g></symbol>"""

if "icon-support-headset" not in html:
    html = html.replace(
        '<symbol id="icon-whatsapp"',
        new_symbols + "\n  " + '<symbol id="icon-whatsapp"',
    )
    print("Added sleek modern SVG icons to sprite")

# 2. Modernize Environment HTML (Zero emojis, sleek SaaS cards)
old_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
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

new_env_html = """  <section class="section environment" id="environment" aria-labelledby="environment-title">
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

if old_env_html in html:
    html = html.replace(old_env_html, new_env_html)
    print("Environment section updated without emojis and with sleek vector icons")

html_path.write_text(html, encoding="utf-8")

# 3. Modernize Environment CSS (Ultra-modern SaaS style)
old_env_css = """/* Environment Section with rich cards and dynamic customization box */
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

new_env_css = """/* Environment Section with ultra-modern SaaS cards & refined vector icons */
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

if old_env_css in css:
    css = css.replace(old_env_css, new_env_css)
    print("Environment CSS updated to modern SaaS design")

css_path.write_text(css, encoding="utf-8")

