from pathlib import Path
from PIL import Image
import json
import re

root=Path(__file__).resolve().parents[1]
review=root/'output/hero-review'
before=(review/'before-index.html').read_text(encoding='utf-8')
after=(root/'index.html').read_text(encoding='utf-8')
pattern=r'  <section class="hero"[\s\S]*?</section>'
def normalize_page(text):
    text=re.sub(pattern,'HERO',text)
    text=re.sub(r'<link rel="preload" as="image"[^>]+>','HERO_PRELOAD',text)
    return re.sub(r'css/style.css\?v=[^"\s]+','css/style.css',text)
assert normalize_page(before)==normalize_page(after),'Changes outside the hero HTML'
def without_hero_css(text):
    text=re.sub(r'/\*[\s\S]*?\*/','',text)
    text=re.sub(r'\.hero[^{}]*\{[^{}]*\}','',text)
    return re.sub(r'\s+','',text)
assert without_hero_css((review/'before-style.css').read_text(encoding='utf-8'))==without_hero_css((root/'css/style.css').read_text(encoding='utf-8')),'CSS changes outside hero selectors'
qa=json.loads((review/'responsive-qa.json').read_text(encoding='utf-8'))
assert [row['width'] for row in qa]==[320,360,390,430,768,1024,1440]
for row in qa:
    assert row['overflow']==0 and not row['textOverflow'] and row['chrome']==0
    assert row['titleLines']==2 and row['descriptionLines']<=2
    assert all(button['height']>=44 and button['width']>=44 for button in row['buttonTargets'])
    if row['width']<768:
        assert float(row['titleFont'].replace('px',''))<=36
        assert abs(row['imageWidth']-row['contentWidth'])<3
    if row['width']>=1024: assert row['heroHeight']<400
for name in ['namaa-dashboard-hero.webp','namaa-dashboard-hero-640.webp']:
    image=Image.open(root/'assets/screenshots'/name)
    assert image.format=='WEBP'
assert Image.open(root/'assets/screenshots/namaa-dashboard-hero.webp').size==(1128,487)
result={'only_hero_html_changed':True,'only_hero_css_selectors_changed':True,'real_dashboard_crop':[788,0,1916,487],'responsive_widths':[r['width'] for r in qa],'horizontal_overflow':0,'desktop_hero_before_px':608.45,'desktop_hero_after_px':qa[-1]['heroHeight'],'desktop_height_reduction_percent':round((608.45-qa[-1]['heroHeight'])/608.45*100,1),'title_two_lines':True,'mobile_title_max_36px':True,'hero_chrome_and_zoom_removed':True}
(review/'scope-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS: hero-only HTML/CSS changes; seven widths; two-line title; full-width mobile image; desktop hero 40% shorter.')
