from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1. Add Facebook icon symbol to SVG sprite in index.html
fb_symbol = """  <symbol id="icon-facebook" viewBox="0 0 24 24"><path fill="currentColor" d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95C18.05 21.45 22 17.19 22 12Z"/></symbol>"""

if "icon-facebook" not in html:
    html = html.replace(
        '<symbol id="icon-instagram"',
        fb_symbol + "\n  " + '<symbol id="icon-instagram"',
    )
    print("Added Facebook icon to SVG sprite")

# 2. Update Footer in index.html
old_footer = """<footer class="footer">
  <div class="container footer__inner">
    <a href="#top" class="brand" aria-label="نماء — العودة إلى البداية"><img class="brand__icon" src="assets/brand/icon-mark.webp" alt="" width="192" height="200" loading="eager"><span class="brand__word">نماء<span class="brand__tagline">لحسابات تنمو</span></span></a>
    <nav class="footer__nav" aria-label="روابط التذييل"><a href="#mazaya">المميزات</a><a href="#showcase">شاهد نماء</a><a href="#pricing">الاشتراكات</a><a href="#faq">الأسئلة</a></nav>
    <p class="footer__statement">نظام محاسبي وإدارة أعمال عربي.</p>
    <p class="footer__copyright">© <span id="current-year">2026</span> نماء. جميع الحقوق محفوظة.</p>
  </div>
</footer>"""

new_footer = """<footer class="footer">
  <div class="container footer__inner">
    <a href="#top" class="brand" aria-label="نماء — العودة إلى البداية">
      <img class="brand__icon" src="assets/brand/icon-mark.webp" alt="" width="192" height="200" loading="eager">
      <span class="brand__word">نماء<span class="brand__tagline">لحسابات تنمو</span></span>
    </a>
    <nav class="footer__nav" aria-label="روابط التذييل">
      <a href="#mazaya">المميزات</a>
      <a href="#showcase">شاهد نماء</a>
      <a href="#pricing">الاشتراكات</a>
      <a href="#faq">الأسئلة</a>
    </nav>
    <div class="footer__social" aria-label="حسابات نماء على التواصل الاجتماعي">
      <a href="https://www.facebook.com/share/1CEyE497op/?mibextid=wwXIfr" aria-label="صفحة نماء على فيسبوك" target="_blank" rel="noopener noreferrer">
        <svg aria-hidden="true"><use href="#icon-facebook"/></svg>
      </a>
      <a href="https://www.instagram.com/namaa.application?stkn=amZjYml0ZXQxbm1k&utm_source=qr" aria-label="حساب نماء على انستغرام" target="_blank" rel="noopener noreferrer">
        <svg aria-hidden="true"><use href="#icon-instagram"/></svg>
      </a>
      <a href="https://wa.me/972592425106?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D9%85%D8%B9%D8%B1%D9%81%D8%A9%20%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84%20%D9%86%D9%85%D8%A7%D8%A1" aria-label="تواصل مع نماء عبر واتساب" target="_blank" rel="noopener noreferrer">
        <svg aria-hidden="true"><use href="#icon-whatsapp"/></svg>
      </a>
    </div>
    <p class="footer__statement">نظام محاسبي وإدارة أعمال عربي.</p>
    <p class="footer__copyright">© <span id="current-year">2026</span> نماء. جميع الحقوق محفوظة.</p>
  </div>
</footer>"""

if old_footer in html:
    html = html.replace(old_footer, new_footer)
    print("Footer updated in index.html with social links")

html_path.write_text(html, encoding="utf-8")

# 3. Update CSS for footer social icons
old_footer_css = """.footer{background:var(--navy);color:var(--white);border-top:1px solid rgb(255 255 255 / 12%)}
.footer__inner{display:grid;gap:16px;padding-block:32px}
.footer__nav{display:flex;flex-wrap:wrap;gap:4px 16px}
.footer__statement,.footer__copyright{font-size:14px;opacity:.68}"""

new_footer_css = """.footer{background:var(--navy);color:var(--white);border-top:1px solid rgb(255 255 255 / 12%)}
.footer__inner{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:20px;padding-block:36px}
.footer__nav{display:flex;flex-wrap:wrap;gap:8px 20px}
.footer__social{display:flex;align-items:center;gap:12px}
.footer__social a{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:50%;background:rgb(255 255 255 / 8%);border:1px solid rgb(255 255 255 / 14%);color:var(--white);transition:background .2s,border-color .2s,color .2s,transform .2s}
.footer__social a:hover{background:var(--green);border-color:var(--green);color:var(--white);transform:translateY(-2px)}
.footer__social svg{width:20px;height:20px}
.footer__statement,.footer__copyright{font-size:14px;opacity:.68}"""

if old_footer_css in css:
    css = css.replace(old_footer_css, new_footer_css)

old_footer_mq = """.footer__inner{grid-template-columns:auto 1fr auto;align-items:center}
  .footer__statement{grid-column:2}.footer__nav{grid-column:2}.footer__copyright{grid-column:3;grid-row:1 / span 2}"""

new_footer_mq = """.footer__inner{display:grid;grid-template-columns:auto 1fr auto auto;align-items:center;gap:24px}
  .footer__statement{grid-column:2;grid-row:2}.footer__nav{grid-column:2;grid-row:1}.footer__social{grid-column:3;grid-row:1 / span 2}.footer__copyright{grid-column:4;grid-row:1 / span 2}"""

if old_footer_mq in css:
    css = css.replace(old_footer_mq, new_footer_mq)

css_path.write_text(css, encoding="utf-8")
print("CSS footer updated successfully!")

