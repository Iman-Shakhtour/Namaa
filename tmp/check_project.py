from pathlib import Path
from html.parser import HTMLParser
from PIL import Image
import re
import json

root = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]; self.images=[]; self.controls=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='img': self.images.append(a)
        if 'aria-controls' in a: self.controls.append(a['aria-controls'])
        if 'aria-labelledby' in a: self.controls.extend(a['aria-labelledby'].split())
        for key in ['src','href','data-src','data-zoom']:
            if key in a: self.refs.append(a[key])
        if 'srcset' in a:
            self.refs.extend(s.strip().split()[0] for s in a['srcset'].split(','))

html=(root/'index.html').read_text(encoding='utf-8')
page=Page(); page.feed(html)
errors=[]
assert len(page.ids)==len(set(page.ids)), 'Duplicate IDs'
for reference in page.refs:
    if reference.startswith('#'):
        if reference[1:] not in page.ids: errors.append('Missing target '+reference)
    elif not re.match(r'https?://', reference):
        if not (root/reference.split('?')[0]).is_file(): errors.append('Missing file '+reference)
for control in page.controls:
    if control not in page.ids: errors.append('Missing ARIA target '+control)
for img in page.images:
    if not all(key in img for key in ['width','height','alt']): errors.append('Image lacks dimensions/alt')
    source=img.get('src') or img.get('data-src')
    if source:
        image=Image.open(root/source)
        ratio=float(img['width'])/float(img['height'])
        if abs(ratio-image.width/image.height)>0.01: errors.append('Image ratio mismatch '+source)

def pricing_text(value):
    value=re.sub(r'<a\b[\s\S]*?</a>', '', value)
    value=re.sub(r'<[^>]+>', ' ',value)
    return ' '.join(value.split())
before=(root/'tmp/original-pricing.html').read_text(encoding='utf-8')
after=re.search(r'<section[^>]*id="pricing"[\s\S]*?</section>',html).group()
assert pricing_text(before)==pricing_text(after), 'Pricing commercial text changed'
assert 'WHATSAPP_NUMBER' not in html
assert 'WHATSAPP_NUMBER' not in (root/'js/main.js').read_text(encoding='utf-8')
assert html.count('class="feature-card"')==6
assert html.count('class="faq-item"')==5
assert not errors, '\n'.join(errors)

assets=[]
for p in sorted((root/'assets/screenshots').glob('*.webp')):
    image=Image.open(p)
    assets.append({'file':p.name,'width':image.width,'height':image.height,'bytes':p.stat().st_size})
result={'local_references_valid':True,'aria_targets_valid':True,'unique_ids':True,'all_image_dimensions_valid':True,'pricing_commercial_text_unchanged':True,'feature_cards':6,'faq_questions':5,'screenshots':assets,'build_script':None,'lint_script':None}
(root/'output/review-v2').mkdir(parents=True,exist_ok=True)
(root/'output/review-v2/static-qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS: local assets, anchors, ARIA, image ratios, pricing preservation, content counts.')
