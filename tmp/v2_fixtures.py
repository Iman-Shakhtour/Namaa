from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
page = (root / 'index.html').read_text(encoding='utf-8').replace('<head>', '<head>\n<base href="/">')
data = (root / 'js/hardware-data.js').read_text(encoding='utf-8')
products = json.loads(data.split('Object.freeze(',1)[1].rsplit('.map(',1)[0])
pending = dict(products[0], id='pending-product', name='منتج غير معتمد للاختبار', approved=False)
for product in products:
    if product['id']=='xprinter-n160ii': product['price']=999
products.append(pending)
page = re.sub(r'<script src="js/hardware-data.js[^>]*></script>', '<script>window.HARDWARE_PRODUCTS = '+json.dumps(products,ensure_ascii=False)+';</script>',page)
page = re.sub(r'<script src="js/tutorials-data.js[^>]*></script>', '<script>window.NAMAA_TUTORIALS = [{id:"local-review",title:"شرح للاختبار المحلي",description:"بيانات اختبار منفصلة عن النسخة المسلمة",url:"https://example.com/tutorial"}];</script>',page)
(root / 'tmp/v2-conditional-fixture.html').write_text(page,encoding='utf-8')
invalid = re.sub(r'window.NAMAA_TUTORIALS = \[[\s\S]*?\];', 'window.NAMAA_TUTORIALS = [{title:"غير صالح",url:"javascript:alert(1)"}];',page)
(root / 'tmp/v2-invalid-tutorial-fixture.html').write_text(invalid,encoding='utf-8')
print('Two isolated local fixtures created; production data unchanged.')
