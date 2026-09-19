from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
page = (root / 'index.html').read_text(encoding='utf-8')
page = page.replace('لماذا نماء؟', 'ليش نماء؟')
page = page.replace('شاشة نقطة البيع تستمر بالعمل أثناء انقطاع الإنترنت المؤقت، وتحفظ الفواتير محليًا ليتم مزامنتها عند عودة الاتصال.', 'بعد بدء العمل أونلاين، يمكنك مواصلة عمليات البيع المدعومة عند انقطاع الإنترنت، ثم مزامنتها عند عودة الاتصال.')
offline = '''
          <p class="offline-scope">ابدأ بتسجيل الدخول وعملية بيع أونلاين. بعدها يتاح البيع دون اتصال من فاتورة البيع وPOS للبيع النقدي.</p>
          <ol class="offline-steps" aria-label="مراحل البيع والمزامنة">
            <li><span class="offline-steps__number" aria-hidden="true">1</span><div><h4>انقطع الاتصال</h4><p>كمّل البيع.</p></div></li>
            <li><span class="offline-steps__number" aria-hidden="true">2</span><div><h4>العملية محفوظة</h4><p>تابع العمليات التي تنتظر المزامنة.</p></div></li>
            <li><span class="offline-steps__number" aria-hidden="true">3</span><div><h4>رجع الإنترنت</h4><p>زامن العمليات وكمل شغلك.</p></div></li>
          </ol>
          <p class="sync-note">تابع مؤشر المزامنة أعلى النظام. إذا ظهرت «تعذرت المزامنة»، اضغط سهم إعادة المحاولة حتى تظهر «تمت المزامنة».</p>
'''
pos_button = '          <button type="button" class="screen-frame why-card__screen" data-zoom="assets/screenshots/namaa-pos-desktop.webp"'
assert pos_button in page
page = page.replace(pos_button, offline + pos_button)
page = page.replace('مدير، محاسب، كاشير أو مستودعجي — حدد ما يمكن لكل مستخدم رؤيته واستخدامه.', 'مدير، محاسب، كاشير، مندوب أو مستودعجي — حدد لكل مستخدم ما يمكنه الوصول إليه حسب مسؤوليته.')
page = page.replace('رابط مخصص وقاعدة بيانات مستقلة لكل نسخة من نماء.', 'يحصل كل عميل على رابط مخصص وقاعدة بيانات مستقلة لنسخته من نماء.')
page = page.replace('التخصيص المتفق عليه لنسختك بدون رسوم إضافية.', 'التخصيص المتفق عليه على نسختك بدون رسوم إضافية.')

hardware = '''  <section class="section hardware section--mint" id="hardware" aria-labelledby="hardware-title">
    <div class="container">
      <div class="hardware__heading"><div class="section-head"><p class="eyebrow">تجهيزات تكمل التجربة</p><h2 id="hardware-title">جهّز محلك مع نماء</h2><p>خيارات أجهزة تساعدك تكمل بيئة البيع عندك.</p></div><button type="button" class="btn btn-secondary" id="hardware-options-button" aria-expanded="false" aria-controls="hardware-options" hidden>عرض خيارات الأجهزة</button></div>
      <div class="hardware-grid" id="hardware-products"></div>
      <div class="hardware-options" id="hardware-options" role="region" aria-labelledby="hardware-options-title" tabindex="-1" hidden>
        <h3 id="hardware-options-title">خيارات الأجهزة والمستلزمات</h3><div class="hardware-options__list" id="hardware-options-list"></div>
      </div>
      <p class="hardware-source">صور وأسعار الأجهزة من <a href="https://logix-mobile.com/shop.php?category=pos" target="_blank" rel="noopener noreferrer">Logix Mobile</a>. أسعار الأجهزة مستقلة عن اشتراك نماء.</p>
      <noscript><p>يمكنك مراجعة خيارات الأجهزة وأسعارها عبر رابط Logix Mobile أعلاه.</p></noscript>
    </div>
  </section>'''
page, count = re.subn(r'  <section[^>]*id="hardware"[\s\S]*?</section>', hardware, page)
assert count == 1

questions = [
    ('شو هو نماء؟', 'نظام محاسبي وإدارة أعمال يجمع المبيعات، المشتريات، المخزون، الحسابات والتقارير في مكان واحد.'),
    ('هل أقدر أشتغل إذا فصل الإنترنت؟', 'نعم، بعد تسجيل الدخول وبدء البيع أونلاين. عند انقطاع الاتصال يمكنك مواصلة البيع من فاتورة البيع وPOS النقدي؛ الدعم لا يشمل كل النظام.'),
    ('شو بصير بالفواتير الأوفلاين؟', 'تُحفظ العمليات محليًا وتظهر العمليات التي تنتظر المزامنة أعلى النظام. عند عودة الاتصال يمكنك مزامنتها، وإعادة المحاولة بالسهم إذا تعذرت المزامنة.'),
    ('هل أقدر أحدد صلاحيات الموظفين؟', 'نعم، تحدد الأدوار والصلاحيات حسب مسؤولية كل مستخدم، بدون رسوم إضافية على ميزة الصلاحيات نفسها.'),
    ('هل يمكن تعديل النظام حسب طبيعة شغلي؟', 'يمكن مناقشة تعديل أو إضافة وتنفيذ التخصيص المتفق عليه على نسختك بدون رسوم إضافية.'),
]
faq = '\n'.join(f'        <article class="faq-item"><h3><button type="button" class="faq-item__q" id="faq-question-{i}" aria-expanded="{str(i==1).lower()}" aria-controls="faq-answer-{i}">{q}<span class="faq-item__icon" aria-hidden="true"></span></button></h3><div class="faq-item__a" id="faq-answer-{i}" role="region" aria-labelledby="faq-question-{i}"{" hidden" if i!=1 else ""}><p>{a}</p></div></article>' for i,(q,a) in enumerate(questions,1))
page, count = re.subn(r'      <div class="faq-list">[\s\S]*?      </div>\n      <noscript>', '      <div class="faq-list">\n' + faq + '\n      </div>\n      <noscript>', page)
assert count == 1

template = '''<template id="tutorials-template">
  <section class="section tutorials section--white" id="tutorials" aria-labelledby="tutorials-title">
    <div class="container"><div class="section-head"><h2 id="tutorials-title">شروحات نماء</h2><p>شروحات عملية تساعدك تتعرف على أدوات النظام.</p></div><div class="tutorials-grid"></div></div>
  </section>
</template>

'''
page = page.replace('<dialog class="screenshot-dialog"', template + '<dialog class="screenshot-dialog"')
page = page.replace('<script src="js/main.js', '<script src="js/tutorials-data.js?v=20260916a" defer></script>\n<script src="js/main.js')
page = page.replace('?v=20260915c', '?v=20260916a')
(root / 'index.html').write_text(page, encoding='utf-8')

verified = json.loads((root / 'tmp/logix-hardware-ready.json').read_text(encoding='utf-8'))
names = ['قارئ باركود سلكي مع حامل', 'قارئ HAIXUN سلكي مع قاعدة', 'قارئ باركود سلكي مقاوم للصدمات', 'قارئ باركود مكتبي ثنائي الأبعاد', 'قارئ باركود لاسلكي مع قاعدة شحن', 'حامل قارئ الباركود', 'رول ورق حراري للفواتير', 'رول ليبل باركود', 'طابعة فواتير Xprinter XP-N160II']
descriptions = ['قارئ محمول مع حامل لبيئة البيع.', 'توصيل USB مع حامل مكتبي.', 'تصميم متين مع حامل مكتبي.', 'قراءة الباركود من سطح المكتب.', 'قاعدة للشحن ونقل البيانات.', 'حامل مكتبي للقارئ.', 'ورق حراري لطباعة الفواتير.', 'ملصقات لتنظيم باركود الأصناف.', 'طابعة حرارية للفواتير والإيصالات.']
products = []
for item, name, description in zip(verified[:9], names, descriptions):
    printer = item['id'] == 'xprinter-n160ii'
    product = {k:item[k] for k in ['id','image','width','height','sourceUrl','sourceImageUrl']}
    product.update(name=name, description=description, price=None if printer else item['price'],currency='NIS',approved=True,approvedPrice=not printer,featured=item['id'] in ['wired-scanner','wireless-scanner','xprinter-n160ii','thermal-paper'])
    if item['id']=='thermal-paper': product.update(featuredName='مستلزمات البيع',featuredDescription='ورق فواتير، ليبل باركود وحوامل.',featuredPricePrefix='من ')
    if printer: product['alternateSourceUrl']=verified[9]['sourceUrl']
    products.append(product)
# These are factual product fields; conflicting printer prices remain review-only.
data = '/* Verified against Logix Mobile product pages on 2026-09-16. Prices are separate from Namaa subscriptions. */\nwindow.HARDWARE_PRODUCTS = Object.freeze(' + json.dumps(products, ensure_ascii=False, indent=2) + '.map(function (product) { return Object.freeze(product); }));\n'
(root / 'js/hardware-data.js').write_text(data,encoding='utf-8')
