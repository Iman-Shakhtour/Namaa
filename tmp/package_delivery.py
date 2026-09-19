from pathlib import Path
from PIL import Image
import hashlib
import json
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
review = root / 'output' / 'review'
project = root / 'output' / 'Namaa-modified'
archive = root / 'output' / 'Namaa-modified.zip'
assert project.resolve().is_relative_to(root.resolve())
assert archive.resolve().is_relative_to(root.resolve())
project.mkdir(parents=True, exist_ok=True)

# Browser exports are JPEG buffers. Store the requested captures as genuine PNGs.
for capture in review.glob('*.png'):
    with Image.open(capture) as image:
        if image.format != 'PNG':
            converted = image.convert('RGB')
            converted.save(capture, format='PNG', optimize=True)

site_items = ['index.html', 'README.md', 'favicon.ico', 'apple-touch-icon.png', 'css', 'js', 'assets']
for name in site_items:
    source, destination = root / name, project / name
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        shutil.copy2(source, destination)

current = {p.relative_to(project).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
           for p in project.rglob('*') if p.is_file()}
with zipfile.ZipFile(root / 'tmp' / 'original-project.zip') as backup:
    previous = {entry.filename: hashlib.sha256(backup.read(entry)).hexdigest()
                for entry in backup.infolist() if not entry.is_dir()}
changed = sorted(p for p in current if p in previous and current[p] != previous[p])
added = sorted(p for p in current if p not in previous)
removed = sorted(p for p in previous if p not in current)

changes = {
    'modified': changed, 'added': added, 'removed': removed,
    'unchanged': sorted(p for p in current if p in previous and current[p] == previous[p]),
    'basis': 'SHA-256 comparison against the original local project backup',
}
(review / 'changed-files.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding='utf-8')

responsive = json.loads((review / 'responsive-qa.json').read_text(encoding='utf-8'))
rows = '\n'.join(f"| {row['width']} | {row['overflow']} | ناجح |" for row in responsive)
changed_list = '\n'.join(f'- `{p}`' for p in changed)
added_list = '\n'.join(f'- `{p}`' for p in added)
removed_list = '\n'.join(f'- `{p}`' for p in removed)
report = f'''# تسليم موقع نماء للمراجعة المحلية

تم تعديل ملفات المشروع الموجود فعليًا، مع الحفاظ على HTML وCSS وVanilla JavaScript وهوية نماء وRTL وخط Tajawal. لم يتم نشر الموقع أو تعديل أي موقع حي.

## التغييرات

- اختصار الصفحة من 26 قسمًا إلى 8 أقسام رئيسية، إضافة إلى الهيدر والفوتر. دُمجت الميزات المتقاربة وحُذفت الأقسام والحركات المطولة.
- توضيح أن نماء نظام محاسبة وإدارة أعمال متكامل؛ لوحة التحكم الحقيقية هي صورة Hero، ونقطة البيع جزء من عرض النظام.
- ست بطاقات ميزات، وخمسة تبويبات لعرض النظام بصورة واحدة في كل مرة، وأربع مزايا، وقسم أجهزة مختصر، وأربع أسئلة شائعة.
- استخدام الشاشات الثماني المقدمة فقط. تم تحويل نسخ الويب إلى WebP دون إعادة رسم أو تغيير النصوص والأرقام. تم حجب أسماء الدخول في صورة الصلاحيات فقط؛ بقيت الأدوار ظاهرة.
- إضافة تكبير الصور، ودعم لوحة المفاتيح، وحالات التركيز، وقائمة موبايل نظيفة. حفظ نسب الصور وعرضها كاملة دون قص واجهة النظام.
- الحفاظ على بيانات خطط الاشتراك التجارية الأصلية. تغيرت روابط الأزرار المؤقتة لتقود إلى عرض البرنامج.
- فصل إعدادات التواصل وفئات الأجهزة في ملفات قابلة للتحديث. القيم الفارغة أو غير الصالحة لا تُنتج روابط تواصل ظاهرة.
- تحديث عنوان الصفحة والوصف وOpen Graph بالصورة الحقيقية للوحة التحكم، وتحميل صور الأقسام غير النشطة عند اختيارها.

## الفحص المنفذ فعليًا

تم تشغيل الموقع عبر خادم Python محلي ومراجعته في Chrome. الجدول التالي يعرض عرض CSS للنافذة، وقد يكون عرض لقطة المتصفح أقل بسبب شريط التمرير.

| عرض النافذة px | التمرير الأفقي الزائد px | الأهداف القابلة للمس والنصوص والصور داخل الحدود |
| --- | --- | --- |
{rows}

تمت مراجعة الهيدر وHero والأزرار والبطاقات والتبويبات والصور وFAQ والفوتر في العروض المطلوبة. نتائج القياس التفصيلية في `responsive-qa.json` و`narrow-header-qa.json`.

تم اختبار التبويبات الخمسة على الكمبيوتر، واختيار صور الموبايل الثلاث على 390px، وأزرار القائمة والأسئلة الشائعة، والتنقل بلوحة المفاتيح. نافذة التكبير تلائم الكمبيوتر والموبايل، وتُغلق بـ Escape وتعيد التركيز للزر الذي فتحها. تم إصلاح التفاف زر الهيدر عند 320px ودورة Tab داخل النافذة، ثم إعادة فحصهما.

سجل `interaction-qa.json` يتضمن قياسات أثناء العمل قبل الإصلاح وبعده: `dialog-focus-wrap` الأول رصد مشكلة التركيز، و`modal-focus-wrap-after-fix` و`modal-reverse-focus-wrap` يوثقان الإصلاح النهائي. صورة لوحة الموبايل كانت غير محملة قبل دخولها الشاشة، ثم جرى التحقق من تحميلها في `mobile-dashboard-visible-and-loaded`.

تم فحص حالات التواصل الفارغ والصالح وغير الصالح باستخدام صفحات اختبار محلية منفصلة. الأرقام والروابط في `contact-qa.json` بيانات اختبار فقط؛ لم تُرسل رسائل ولم تُفتح روابط تواصل خارجية، ولم تُدرج صفحات الاختبار في مجلد الموقع. إعدادات التواصل في النسخة المسلمة فارغة.

نجح فحص صياغة JavaScript للملفات الثلاثة، ومسارات الملفات والروابط الداخلية وARIA وعدم تكرار IDs وأبعاد الصور. تطابق النص التجاري في قسم الخطط مع النسخة الأصلية. لا يوجد build أو lint معد في هذا المشروع، لذا لم يُدّعَ تشغيلهما. لم يُنفذ اختبار على أجهزة فعلية أو متصفحات أخرى.

## الملفات المتغيرة

### معدلة ({len(changed)})

{changed_list}

### مضافة ({len(added)})

{added_list}

### محذوفة ({len(removed)})

حُذفت الصور القديمة غير المستخدمة بعد استبدالها بالشاشات الحقيقية. الأصول الأصلية للهوية والأيقونات محفوظة.

{removed_list}

القائمة المقارنة آليًا موجودة أيضًا في `changed-files.json`.

## محتويات التسليم

- `Namaa-modified/`: مجلد الموقع الجاهز للمراجعة، دون ملفات مؤقتة أو إعدادات اختبار.
- `Review/`: هذا التقرير، ونتائج الفحص، ولقطات الموقع، والشاشات المقدمة الأصلية غير المعدلة.
- `namaa-mobile-390.png` و`namaa-desktop-1440.png`: لقطتان للنسخة النهائية عند عرضي CSS المطلوبين.

مجلد `Review/original-screenshots` مخصص للمراجعة المحلية، خارج مجلد الموقع. احتفظ به خارج أي نشر لاحق؛ صورة الصلاحيات الأصلية غير المحجوبة تتضمن أسماء الدخول.

## البيانات المطلوبة لاحقًا

- رقم واتساب الدولي وروابط إنستغرام وفيسبوك المعتمدة: `js/site-config.js`.
- خيارات وأسعار الأجهزة النهائية: `js/hardware-data.js`؛ لم تُخترع أسعار.
- خطط الاشتراك الجديدة بعد اعتماد الإدارة؛ الأسعار الحالية محفوظة في `index.html`.

يمكن فتح `index.html` مباشرة، أو تشغيل `python -m http.server 8765 --bind 127.0.0.1` من مجلد الموقع. الخط يُحمّل من Google Fonts مع بدائل إذا تعذر الاتصال.
'''
(review / 'DELIVERY.md').write_text(report, encoding='utf-8')

review_files = ['DELIVERY.md', 'changed-files.json', 'responsive-qa.json', 'narrow-header-qa.json',
                'static-qa.json', 'interaction-qa.json', 'contact-qa.json',
                'namaa-mobile-390.png', 'namaa-desktop-1440.png',
                'desktop-rbac-modal.png', 'mobile-image-modal.png']
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
    for p in sorted(project.rglob('*')):
        if p.is_file(): bundle.write(p, 'Namaa-modified/' + p.relative_to(project).as_posix())
    for name in review_files:
        bundle.write(review / name, 'Review/' + name)
    for p in sorted((review / 'original-screenshots').rglob('*')):
        if p.is_file(): bundle.write(p, 'Review/original-screenshots/' + p.relative_to(review / 'original-screenshots').as_posix())

with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    for name, digest in current.items():
        assert hashlib.sha256(bundle.read('Namaa-modified/' + name)).hexdigest() == digest
    names = bundle.namelist()
    assert not any('/tmp/' in name or '/.git/' in name or '/assets/images/' in name for name in names)
    for name in ['namaa-mobile-390.png', 'namaa-desktop-1440.png']:
        with Image.open(review / name) as image:
            assert image.format == 'PNG'
    assert "whatsappNumber: ''" in (project / 'js/site-config.js').read_text(encoding='utf-8')
    assert len(list((review / 'original-screenshots').glob('*.png'))) == 8

print(json.dumps({'project_files':len(current), 'modified':len(changed), 'added':len(added),
                  'removed':len(removed), 'zip_bytes':archive.stat().st_size,
                  'zip_integrity':'passed', 'copy_hashes':'passed'}, indent=2))
