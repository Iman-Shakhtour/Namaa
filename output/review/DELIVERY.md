# تسليم موقع نماء للمراجعة المحلية

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
| 320 | 0 | ناجح |
| 360 | 0 | ناجح |
| 390 | 0 | ناجح |
| 430 | 0 | ناجح |
| 768 | 0 | ناجح |
| 1024 | 0 | ناجح |
| 1440 | 0 | ناجح |

تمت مراجعة الهيدر وHero والأزرار والبطاقات والتبويبات والصور وFAQ والفوتر في العروض المطلوبة. نتائج القياس التفصيلية في `responsive-qa.json` و`narrow-header-qa.json`.

تم اختبار التبويبات الخمسة على الكمبيوتر، واختيار صور الموبايل الثلاث على 390px، وأزرار القائمة والأسئلة الشائعة، والتنقل بلوحة المفاتيح. نافذة التكبير تلائم الكمبيوتر والموبايل، وتُغلق بـ Escape وتعيد التركيز للزر الذي فتحها. تم إصلاح التفاف زر الهيدر عند 320px ودورة Tab داخل النافذة، ثم إعادة فحصهما.

سجل `interaction-qa.json` يتضمن قياسات أثناء العمل قبل الإصلاح وبعده: `dialog-focus-wrap` الأول رصد مشكلة التركيز، و`modal-focus-wrap-after-fix` و`modal-reverse-focus-wrap` يوثقان الإصلاح النهائي. صورة لوحة الموبايل كانت غير محملة قبل دخولها الشاشة، ثم جرى التحقق من تحميلها في `mobile-dashboard-visible-and-loaded`.

تم فحص حالات التواصل الفارغ والصالح وغير الصالح باستخدام صفحات اختبار محلية منفصلة. الأرقام والروابط في `contact-qa.json` بيانات اختبار فقط؛ لم تُرسل رسائل ولم تُفتح روابط تواصل خارجية، ولم تُدرج صفحات الاختبار في مجلد الموقع. إعدادات التواصل في النسخة المسلمة فارغة.

نجح فحص صياغة JavaScript للملفات الثلاثة، ومسارات الملفات والروابط الداخلية وARIA وعدم تكرار IDs وأبعاد الصور. تطابق النص التجاري في قسم الخطط مع النسخة الأصلية. لا يوجد build أو lint معد في هذا المشروع، لذا لم يُدّعَ تشغيلهما. لم يُنفذ اختبار على أجهزة فعلية أو متصفحات أخرى.

## الملفات المتغيرة

### معدلة (4)

- `README.md`
- `css/style.css`
- `index.html`
- `js/main.js`

### مضافة (13)

- `assets/screenshots/namaa-dashboard-desktop-1280.webp`
- `assets/screenshots/namaa-dashboard-desktop-640.webp`
- `assets/screenshots/namaa-dashboard-desktop.webp`
- `assets/screenshots/namaa-dashboard-mobile.webp`
- `assets/screenshots/namaa-inventory-desktop.webp`
- `assets/screenshots/namaa-items-mobile.webp`
- `assets/screenshots/namaa-pos-desktop.webp`
- `assets/screenshots/namaa-pos-mobile.webp`
- `assets/screenshots/namaa-profit-report.webp`
- `assets/screenshots/namaa-rbac-users-sanitized.png`
- `assets/screenshots/namaa-rbac-users.webp`
- `js/hardware-data.js`
- `js/site-config.js`

### محذوفة (48)

حُذفت الصور القديمة غير المستخدمة بعد استبدالها بالشاشات الحقيقية. الأصول الأصلية للهوية والأيقونات محفوظة.

- `assets/images/01-hero-dashboard-1200.webp`
- `assets/images/01-hero-dashboard-480.webp`
- `assets/images/01-hero-dashboard-800.webp`
- `assets/images/01-hero-dashboard.webp`
- `assets/images/02-pos-1200.webp`
- `assets/images/02-pos-480.webp`
- `assets/images/02-pos-800.webp`
- `assets/images/02-pos.webp`
- `assets/images/03-sales-purchases-1200.webp`
- `assets/images/03-sales-purchases-480.webp`
- `assets/images/03-sales-purchases-800.webp`
- `assets/images/03-sales-purchases.webp`
- `assets/images/04-inventory-reports-1200.webp`
- `assets/images/04-inventory-reports-480.webp`
- `assets/images/04-inventory-reports-800.webp`
- `assets/images/04-inventory-reports.webp`
- `assets/images/05-accounting-1200.webp`
- `assets/images/05-accounting-480.webp`
- `assets/images/05-accounting-800.webp`
- `assets/images/05-accounting.webp`
- `assets/images/06-cash-checks-cashier-1200.webp`
- `assets/images/06-cash-checks-cashier-480.webp`
- `assets/images/06-cash-checks-cashier-800.webp`
- `assets/images/06-cash-checks-cashier.webp`
- `assets/images/07-barcode-products-1200.webp`
- `assets/images/07-barcode-products-480.webp`
- `assets/images/07-barcode-products-800.webp`
- `assets/images/07-barcode-products.webp`
- `assets/images/08-store-fit-1200.webp`
- `assets/images/08-store-fit-480.webp`
- `assets/images/08-store-fit-800.webp`
- `assets/images/08-store-fit.webp`
- `assets/images/09-store-types-1200.webp`
- `assets/images/09-store-types-480.webp`
- `assets/images/09-store-types-800.webp`
- `assets/images/09-store-types.webp`
- `assets/images/10-suppliers-purchases-1200.webp`
- `assets/images/10-suppliers-purchases-480.webp`
- `assets/images/10-suppliers-purchases-800.webp`
- `assets/images/10-suppliers-purchases.webp`
- `assets/images/11-customers-1200.webp`
- `assets/images/11-customers-480.webp`
- `assets/images/11-customers-800.webp`
- `assets/images/11-customers.webp`
- `assets/images/12-expenses-cash-1200.webp`
- `assets/images/12-expenses-cash-480.webp`
- `assets/images/12-expenses-cash-800.webp`
- `assets/images/12-expenses-cash.webp`

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
