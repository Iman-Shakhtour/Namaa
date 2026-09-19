from pathlib import Path
from PIL import Image
import hashlib
import json
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
review = root / 'output/review-v2'
project = root / 'output/Namaa-reviewed-v2'
archive = root / 'output/Namaa-reviewed-v2.zip'
assert project.resolve().is_relative_to(root.resolve())
project.mkdir(parents=True,exist_ok=True)

for p in review.glob('*.png'):
    with Image.open(p) as image:
        if image.format!='PNG': image.convert('RGB').save(p,'PNG',optimize=True)

products = json.loads((root / 'js/hardware-data.js').read_text(encoding='utf-8').split('Object.freeze(',1)[1].rsplit('.map(',1)[0])
hardware_sources = [{key:product[key] for key in ['id','name','price','approvedPrice','sourceUrl','sourceImageUrl','image']} for product in products]
(review / 'hardware-sources.json').write_text(json.dumps(hardware_sources,ensure_ascii=False,indent=2),encoding='utf-8')
with zipfile.ZipFile(root / 'tmp/before-review-v2.zip') as backup:
    before = {item.filename:hashlib.sha256(backup.read(item)).hexdigest() for item in backup.infolist() if not item.is_dir()}
items = ['index.html','README.md','favicon.ico','apple-touch-icon.png','css','js','assets']
site_files = [p for item in items for p in ([root/item] if (root/item).is_file() else (root/item).rglob('*')) if p.is_file()]
after = {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in site_files}
modified = sorted(name for name in after if name in before and before[name]!=after[name])
added = sorted(name for name in after if name not in before) + ['DELIVERY.md']
removed = sorted(name for name in before if name not in after)
changes = {'modified':modified,'added':added,'removed':removed,'basis':'Current project before this review, not the earlier original long landing page'}
(review / 'changed-files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
rows = '\n'.join(f"| {row['width']} | {row['overflow']} | {row['expandedHardware']['overflow']} | ناجح |" for row in json.loads((review/'responsive-qa.json').read_text(encoding='utf-8')))
files_list = '\n'.join(f'- `{name}`' for name in modified)
added_list = '\n'.join(f'- `{name}`' for name in added)
source_rows = '\n'.join(f"| {p['name']} | {str(int(p['price']))+' NIS' if p['approvedPrice'] else 'استفسر عن السعر'} | [صفحة المنتج]({p['sourceUrl']}) |" for p in products)
report = f'''# تسليم مراجعة نماء — النسخة الثانية

تمت مراجعة ZIP النسخة السابقة وملفات المشروع الحالي وتعديلها فعليًا. البنية HTML/CSS/Vanilla JavaScript والهوية العربية وRTL وخط Tajawal محفوظة. لم يتم النشر أو تعديل Production، والمعاينة محلية فقط.

## الملفات المعدلة والمضافة

معدلة ({len(modified)}):

{files_list}

مضافة ({len(added)}):

{added_list}

لم تُحذف ملفات من النسخة الحالية. القائمة المقارنة مع حالة المشروع قبل هذه المراجعة في `Review/changed-files.json`.

## الأقسام المدمجة والمحتوى

- تم الاحتفاظ بالهيكل المختصر الحالي: Hero، الميزات، عرض البرنامج، لماذا نماء، الأجهزة، الاشتراكات، FAQ، CTA. لم تُعد الصفحة من الصفر ولم تُضف أقسام ظاهرة مطولة.
- دُمج شرح Offline/Online والمزامنة داخل بطاقة الميزة في «ليش نماء؟» بدل قسم إضافي.
- استُبدلت فئات الأجهزة الثلاث القديمة بأربع بطاقات لمنتجات Logix وقائمة خيارات تُفتح عند الطلب. حُذف عرض درج النقد من المحتوى؛ بياناته غير المعتمدة غير موجودة في بيانات الموقع.
- أصبحت FAQ خمسة أسئلة. دُمج شرط بدء العمل بوجود الإنترنت في جواب سؤال العمل عند الانقطاع، وأُضيف سؤال مستقل للفواتير الأوفلاين، وفق العدد النهائي المطلوب في الـbrief.
- بقي التعريف من أول شاشة واضحًا: نماء نظام محاسبة وإدارة أعمال، ونقطة البيع إحدى أدواته.
- أُضيف دور المندوب في وصف الصلاحيات مع الحفاظ على مجانية الميزة نفسها، دون ادعاء مستخدمين غير محدودين.
- بقيت ميزة رابط مخصص وقاعدة بيانات مستقلة، والتخصيص المتفق عليه بدون رسوم إضافية، دون ادعاءات عن الخادم أو الأمان المطلق أو تخصيص غير محدود.
- قسم «شروحات نماء» جاهز بقالب وملف بيانات مستقل. القائمة الحالية فارغة، لذلك لا يُدرج القسم ولا يظهر أي فيديو مؤقت. يمكن إضافة فيديو معتمد بالشكل `{{ id, title, description, url }}` مع رابط HTTPS؛ يظهر رابط للمشاهدة دون تحميل مشغل ثقيل.

## تحديث Offline/Sync

اعتمدنا تحديث الفريق في أحدث brief فوق صياغة الدليل القديمة:

1. يبدأ المستخدم بتسجيل الدخول وعملية بيع أونلاين.
2. عند الانقطاع يستمر البيع المدعوم من فاتورة البيع وPOS للبيع النقدي؛ تُحفظ العمليات محليًا.
3. عند عودة الاتصال تتم المزامنة أو محاولة المزامنة. يُراجع مؤشر المزامنة أعلى النظام، ويستخدم سهم إعادة المحاولة عند «تعذرت المزامنة» حتى «تمت المزامنة».

عُرضت المراحل الثلاث كنص تسويقي واضح: انقطع الاتصال، العملية محفوظة، رجع الإنترنت. لم تُختلق واجهة حالات المزامنة؛ استُخدمت صورة POS الحقيقية الموجودة فقط.

صور ناقصة: `offline-state` و`pending-sync` و`synced-state`. تُستبدل بها الصور أو تُضاف داخل العرض عند توفير شاشات حقيقية مناسبة.

## الشاشات المستخدمة

استخدمت النسخة صور نماء الحقيقية المحفوظة بالفعل، دون أي تغيير جديد في بايتاتها:

- `namaa-dashboard-desktop.webp`: Hero وتبويب لوحة التحكم، مع نسختي 640 و1280 لسرعة التحميل.
- `namaa-pos-desktop.webp`: تبويب نقطة البيع وشرح الأوفلاين.
- `namaa-inventory-desktop.webp`: المخزون.
- `namaa-profit-report.webp`: التقارير.
- `namaa-rbac-users.webp`: الصلاحيات؛ أسماء الدخول محجوبة والأدوار باقية.
- `namaa-dashboard-mobile.webp` و`namaa-pos-mobile.webp` و`namaa-items-mobile.webp`: اختيار الهاتف داخل العرض، صورة واحدة في كل مرة.

أصول الشاشات المقدمة غير المعدلة محفوظة في `Review/original-screenshots/` خارج مجلد الموقع. احتفظ بهذا المجلد للمراجعة المحلية؛ صورة الصلاحيات الأصلية غير المحجوبة تتضمن أسماء دخول. لا توجد حسابات اختبار أو كلمات مرور أو cookies محفوظة في كود الموقع.

## تحديث أجهزة Logix

تمت مراجعة [قسم POS في Logix Mobile](https://logix-mobile.com/shop.php?category=pos) وصفحات المنتجات فعليًا بتاريخ 2026-09-16. الصور الحقيقية نُزلت محليًا وحُسنت إلى WebP داخل `assets/hardware/` مع حفظ أبعادها ومصدر الصورة ورابط المنتج في `js/hardware-data.js`. النسخ الأصلية للصور مرفقة في `Review/original-hardware/`.

| المنتج | السعر المعروض | المصدر |
| --- | --- | --- |
{source_rows}

تظهر أربع بطاقات فقط: قارئ سلكي، قارئ لاسلكي، مستلزمات، طابعة. القائمة الإضافية تعرض التسعة منتجات المعتمدة. أسعار الأجهزة منفصلة عن اشتراكات نماء. لا توجد سلة أو شراء أو واجهة متجر كاملة.

سعر Xprinter مخفي (`approvedPrice: false` و`price: null`) بسبب إدخالين: [380 NIS](https://logix-mobile.com/product.php?slug=product-1786868629) و[480 NIS](https://logix-mobile.com/product.php?slug=xprinter-xp-n160ii). تُستخدم صورة صفحة Xprinter المسجلة في ملف البيانات للعرض دون رقم، ويظل اختيار المنتج والسعر النهائي بحاجة إلى اعتماد الفريق. درج النقد غير معروض حتى اعتماد الإدارة، حتى لو ظهر كمنتج مرتبط في صفحات المصدر.

## الفحص المنفذ

تم تشغيل خادم محلي وفتح النسخة فعليًا في Chrome. الأرقام التالية عروض CSS للنافذة؛ قد يقل عرض لقطة الصورة بسبب شريط التمرير.

| العرض px | التمرير الأفقي الزائد px | الزائد عند فتح الأجهزة px | النصوص والصور والأهداف >=44px |
| --- | --- | --- | --- |
{rows}

شمل القياس الهيدر، Hero، الأزرار، التبويبات، البطاقات، الأوفلاين، الأجهزة، الصور، FAQ والفوتر. تم توسيع مساحة لمس رابط الأسئلة بالفوتر ثم إعادة فحص العروض المطلوبة. نتائج القياسات في `Review/responsive-qa.json`.

تم اختبار القائمة على الهاتف وEscape وروابطها، والأسئلة الخمسة بالضغط وEnter، وفتح الأجهزة وإغلاقها وEscape. تم اختبار التبويبات الخمسة والصور الحقيقية للكمبيوتر عند 1440px، وصور الهاتف الثلاث عند 390px. نافذة الصور تلائم 390px و1440px، وتعمل دورة Tab وShift+Tab وEscape وإعادة التركيز. لا توجد أخطاء أو تحذيرات Console في نافذة الفحص النهائية.

سجل التفاعل يحفظ قراءات الصور الكسولة قبل تحميل بعضها، ثم قياسات تحقق من تحميلها فعلًا بعد ظهورها. سجلات `desktop-lazy-image-loaded` و`mobile-dashboard-loaded-after-visible-zoom` توثق نتيجة التحميل النهائية.

تم اختبار حالات شرطية بصفحات محلية منفصلة: المنتج `approved: false` لا يظهر؛ السعر غير المعتمد يبقى مخفيًا حتى لو احتوت بيانات الاختبار على رقم؛ قائمة فيديو صالحة تُظهر القسم، والقائمة الفارغة أو الرابط غير الصالح يخفيانه. صفحة الاختبار تحمل رابط example.com تجريبيًا فقط، لم يُفتح ولم يُدرج في ملفات التسليم. التفاصيل في `Review/conditional-qa.json`.

نجح فحص صياغة ملفات JavaScript الأربعة، ومسارات الصور وARIA وIDs، ومطابقة أسعار الأجهزة المعتمدة مع brief. قسم الاشتراكات مطابق للنسخة السابقة بعد توحيد نهايات الأسطر؛ لم تتغير بياناته التجارية أو أزراره. ملفات شاشات نماء الحالية مطابقة بايتًا للنسخة السابقة. لا يوجد build أو lint معد، لذلك لم يُدّعَ تشغيلهما.

المراجعة تخص الموقع التسويقي ومحتواه وتفاعلاته. لم يتم تسجيل الدخول للنظام أو تنفيذ عملية بيع أو مزامنة حقيقية أو اختبار أجهزة فعلية أو متصفحات أخرى.

## ما يحتاج اعتمادًا لاحقًا

- واتساب الرسمي وروابط التواصل ما زالت فارغة في `js/site-config.js`؛ الروابط مخفية والأزرار تقود إلى عرض البرنامج.
- اختيار إدخال Xprinter المعتمد وسعره.
- اعتماد درج النقد قبل عرضه.
- مراجعة الإدارة لخطط وأسعار اشتراكات نماء؛ البيانات الحالية محفوظة.
- سياسة معتمدة لنطاق التخصيص المجاني؛ النص العام يقتصر على التخصيص المتفق عليه.
- الفيديوهات المعتمدة للشروحات؛ البنية جاهزة والمحتوى معلق.
- صور حالات انقطاع الاتصال والعمليات المنتظرة ونجاح المزامنة.

## التشغيل والمحتويات

`Namaa-reviewed-v2/` هو مجلد الموقع المعدل. `Review/` يحتوي النتائج والصور والمصادر الأصلية خارج مجلد الموقع. افتح `index.html` أو شغل خادم Python محليًا كما في README. الخط من Google Fonts مع `display=swap` وخطوط احتياطية. لم يحدث أي نشر.
'''
(root / 'DELIVERY.md').write_text(report,encoding='utf-8')
(review / 'DELIVERY.md').write_text(report,encoding='utf-8')

for item in items+['DELIVERY.md']:
    source,target = root/item,project/item
    if source.is_dir(): shutil.copytree(source,target,dirs_exist_ok=True)
    else: shutil.copy2(source,target)
shutil.copytree(root / 'output/review/original-screenshots',review/'original-screenshots',dirs_exist_ok=True)

with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as bundle:
    for folder,prefix in [(project,'Namaa-reviewed-v2'),(review,'Review')]:
        for p in sorted(folder.rglob('*')):
            if p.is_file(): bundle.write(p,prefix+'/'+p.relative_to(folder).as_posix())
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    for p in project.rglob('*'):
        if p.is_file(): assert bundle.read('Namaa-reviewed-v2/'+p.relative_to(project).as_posix())==p.read_bytes()
    assert not any('/tmp/' in name or '/.git/' in name for name in bundle.namelist())
    for p in review.glob('*.png'):
        assert Image.open(p).format=='PNG'
    assert 'https://example.com/tutorial' not in (project/'js/tutorials-data.js').read_text(encoding='utf-8')
print(json.dumps({'zip_bytes':archive.stat().st_size,'site_files':sum(p.is_file() for p in project.rglob('*')),'modified':modified,'added_count':len(added),'zip_integrity':'passed','project_copy_hashes':'passed'},indent=2))
