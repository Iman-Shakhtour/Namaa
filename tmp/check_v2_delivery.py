from pathlib import Path
from PIL import Image
from urllib.parse import urlparse
import hashlib
import json
import re
import zipfile

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
section = lambda text: re.search(r'<section[^>]*id="pricing"[\s\S]*?</section>',text.replace('\r\n','\n')).group()
with zipfile.ZipFile(root / 'tmp/before-review-v2.zip') as backup:
    assert section(html) == section(backup.read('index.html').decode('utf-8'))
    for name in backup.namelist():
        if name.startswith('assets/screenshots/'):
            assert (root / name).read_bytes() == backup.read(name)

data = (root / 'js/hardware-data.js').read_text(encoding='utf-8')
products = json.loads(data.split('Object.freeze(',1)[1].rsplit('.map(',1)[0])
expected = {'wired-scanner':150,'haixun-scanner':180,'rugged-scanner':200,'desktop-2d-scanner':350,'wireless-scanner':350,'scanner-stand':30,'thermal-paper':5,'barcode-labels':30}
for product in products:
    image = Image.open(root / product['image'])
    assert image.format=='WEBP' and image.size==(product['width'],product['height'])
    assert urlparse(product['sourceUrl']).hostname=='logix-mobile.com'
    assert urlparse(product['sourceImageUrl']).hostname=='logix-mobile.com'
    assert product['approved'] is True
    if product['id']=='xprinter-n160ii':
        assert product['approvedPrice'] is False and product['price'] is None
    else:
        assert product['approvedPrice'] is True and product['price']==expected[product['id']]
assert len(products)==9
assert sum(product['featured'] for product in products)==4
assert 'drawer' not in data.lower()
assert 'Object.freeze([])' in (root / 'js/tutorials-data.js').read_text(encoding='utf-8')
assert "whatsappNumber: ''" in (root / 'js/site-config.js').read_text(encoding='utf-8')
assert 'فاتورة البيع وPOS للبيع النقدي' in html
assert html.count('class="faq-item"')==5
assert html.count('<li><span class="offline-steps__number"')==3
assert not (root / 'package.json').exists()

responsive = json.loads((root / 'output/review-v2/responsive-qa.json').read_text(encoding='utf-8'))
assert [row['width'] for row in responsive]==[320,360,390,430,768,1024,1440]
for row in responsive:
    assert row['overflow']==0 and not row['overflowing'] and not row['smallTargets']
    assert row['hardwareCards']==4 and row['faqCount']==5 and row['sectionCount']==8
    assert not row['tutorialsVisible'] and not row['whatsappVisible']
    assert row['expandedHardware']['options']==9
    assert row['expandedHardware']['overflow']==0 and row['expandedHardware']['textOverflow']==0
    assert all(price=='استفسر عن السعر' for price in row['expandedHardware']['printerPrices'])

interactions = json.loads((root/'output/review-v2/interaction-qa.json').read_text(encoding='utf-8'))
for test in interactions:
    if test['test']=='faq-click':
        assert sum(state['expanded']=='true' for state in test['states'])<=1
        assert all((state['expanded']=='true')==not_hidden for state in test['states'] for not_hidden in [not state['answerHidden']])
    if test['test'] in ['mobile-modal-fit','desktop-modal-fit']:
        assert test['open'] and test['rect']['left']>=0 and test['rect']['right']<=test['width']
        assert test['rect']['top']>=0 and test['rect']['bottom']<=test['height']
assert len([t for t in interactions if t['test']=='desktop-tab' and t['width']==1440])==5
assert all(t['visibleImages']==1 and t['visiblePanels']==1 and t['overflow']==0 for t in interactions if t['test']=='desktop-tab')
assert interactions[-1]['test']=='mobile-dashboard-loaded-after-visible-zoom' and interactions[-1]['naturalWidth']==352
conditional = json.loads((root/'output/review-v2/conditional-qa.json').read_text(encoding='utf-8'))
assert not conditional[0]['pendingVisible'] and conditional[0]['printerPrice']=='استفسر عن السعر'
assert conditional[0]['tutorialSection'] and conditional[0]['tutorialCards']==1
assert not conditional[1]['pendingVisible'] and conditional[1]['optionCount']==9
assert not conditional[2]['tutorialSection'] and conditional[2]['tutorialCards']==0
result = {'pricing_section_exactly_unchanged':True,'existing_screenshot_bytes_unchanged':True,'hardware_products':9,'featured_hardware_cards':4,'approved_prices_match_brief':True,'printer_price_hidden':True,'cash_drawer_absent':True,'hardware_images_local_webp_with_dimensions':True,'hardware_sources_recorded':True,'tutorials_empty':True,'production_contact_empty':True,'responsive_seven_widths_pass':True,'interaction_evidence_valid':True,'conditional_evidence_valid':True,'build_configured':False,'lint_configured':False}
(root / 'output/review-v2/final-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS: exact pricing preservation, screenshot hashes, approved hardware prices and sources, pending content hidden, seven responsive widths.')
