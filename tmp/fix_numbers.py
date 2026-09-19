from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_path = root / "index.html"
css_path = root / "css" / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Update HTML for Workflow Numbers
old_workflow_html = """        <ol class="workflow" aria-label="مراحل العمل دون اتصال">
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

new_workflow_html = """        <ol class="workflow" aria-label="مراحل العمل دون اتصال">
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-offline-full.webp" alt="واجهة نماء الكاملة أثناء العمل دون اتصال مع ظهور إشعار أوفلاين" width="1919" height="872" loading="lazy">
            </div>
            <div class="workflow__content">
              <div class="workflow__header">
                <span class="workflow__num">1</span>
                <h3>دون اتصال</h3>
              </div>
              <p>واصل البيع من فاتورة البيع وPOS النقدي حتى لو انقطع الإنترنت تماماً.</p>
            </div>
          </li>
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-pending-full.webp" alt="واجهة نماء وفيها تنبيه أوفلاين مع عدد الفواتير المعلقة" width="1916" height="870" loading="lazy">
            </div>
            <div class="workflow__content">
              <div class="workflow__header">
                <span class="workflow__num">2</span>
                <h3>بانتظار المزامنة</h3>
              </div>
              <p>تُحفظ العمليات محلياً ويظهر عداد العمليات المعلقة أعلى النظام بوضوح.</p>
            </div>
          </li>
          <li>
            <div class="workflow__preview">
              <img src="assets/screenshots/namaa-sync-complete-full.webp" alt="واجهة نماء أثناء بدء مزامنة العمليات فور عودة الاتصال" width="1919" height="875" loading="lazy">
            </div>
            <div class="workflow__content">
              <div class="workflow__header">
                <span class="workflow__num">3</span>
                <h3>مزامنة العمليات</h3>
              </div>
              <p>تُرفع العمليات وتُعتمد فوراً بعد عودة الاتصال بضغطة زر وبلا فقدان بيانات.</p>
            </div>
          </li>
        </ol>"""

assert old_workflow_html in html, "old_workflow_html not found in index.html"
html = html.replace(old_workflow_html, new_workflow_html)
html_path.write_text(html, encoding="utf-8")
print("index.html workflow updated successfully!")

# Update CSS for Workflow
old_workflow_css = """/* Offline: 3 distinct system states */
.offline{background:var(--navy);color:var(--white)}
.offline__inner{max-width:1200px}
.offline h2{color:var(--white)}
.offline__lead{max-width:650px;margin-top:16px;color:var(--white);font-size:18px;opacity:.74}
.workflow{list-style:none;padding:0;margin-top:40px;display:grid;grid-template-columns:1fr;gap:20px}
.workflow li{position:relative;display:flex;flex-direction:column;overflow:hidden;border:1px solid rgb(255 255 255 / 14%);border-radius:var(--radius-lg);background:rgb(255 255 255 / 5%);box-shadow:0 18px 48px rgb(7 24 47 / 35%);transition:transform .25s ease,border-color .25s ease,background .25s ease}
.workflow li:hover{border-color:var(--green-bright);background:rgb(255 255 255 / 8%);transform:translateY(-4px)}
.workflow__preview{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;background:#051224;border-bottom:1px solid rgb(255 255 255 / 12%)}
.workflow__preview img{display:block;width:100%;height:100%;object-fit:cover;object-position:top center;transition:transform .3s ease}
.workflow li:hover .workflow__preview img{transform:scale(1.03)}
.workflow__content{position:relative;padding:22px 20px 22px 64px;flex:1;display:flex;flex-direction:column}
.workflow li b{position:absolute;inset-block-start:20px;inset-inline-start:18px;display:grid;place-items:center;width:32px;height:32px;border:2px solid var(--green-bright);border-radius:50%;background:rgb(18 184 134 / 18%);color:var(--green-bright);font-size:14px;font-weight:800}
.workflow h3{color:var(--white);font-size:20px;font-weight:800}
.workflow p{margin-top:6px;color:rgb(255 255 255 / 75%);font-size:14px;line-height:1.55}"""

new_workflow_css = """/* Offline: 3 distinct system states */
.offline{background:var(--navy);color:var(--white)}
.offline__inner{max-width:1200px}
.offline h2{color:var(--white)}
.offline__lead{max-width:650px;margin-top:16px;color:var(--white);font-size:18px;opacity:.74}
.workflow{list-style:none;padding:0;margin-top:40px;display:grid;grid-template-columns:1fr;gap:24px}
.workflow li{position:relative;display:flex;flex-direction:column;overflow:hidden;border:1px solid rgb(255 255 255 / 14%);border-radius:var(--radius-lg);background:rgb(255 255 255 / 5%);box-shadow:0 18px 48px rgb(7 24 47 / 35%);transition:transform .25s ease,border-color .25s ease,background .25s ease}
.workflow li:hover{border-color:var(--green-bright);background:rgb(255 255 255 / 8%);transform:translateY(-4px)}
.workflow__preview{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;background:#051224;border-bottom:1px solid rgb(255 255 255 / 12%)}
.workflow__preview img{display:block;width:100%;height:100%;object-fit:cover;object-position:top center;transition:transform .3s ease}
.workflow li:hover .workflow__preview img{transform:scale(1.03)}
.workflow__content{padding:24px 20px;flex:1;display:flex;flex-direction:column}
.workflow__header{display:flex;align-items:center;gap:14px;margin-bottom:10px}
.workflow__num{display:inline-grid;place-items:center;width:34px;height:34px;border:2px solid var(--green-bright);border-radius:50%;background:rgb(18 184 134 / 20%);color:var(--green-bright);font-size:15px;font-weight:800;flex:0 0 auto;line-height:1}
.workflow__header h3{color:var(--white);font-size:20px;font-weight:800;margin:0}
.workflow p{margin:0;color:rgb(255 255 255 / 75%);font-size:14px;line-height:1.6}"""

assert old_workflow_css in css, "old_workflow_css not found in style.css"
css = css.replace(old_workflow_css, new_workflow_css)
css_path.write_text(css, encoding="utf-8")
print("css/style.css workflow updated successfully!")

