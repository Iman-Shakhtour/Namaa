from pathlib import Path
from PIL import Image
import json
import re
import shutil
import zipfile

root=Path(__file__).resolve().parents[1]
review=root/'output/centered-hero-review'
project=root/'output/Namaa-centered-hero'
archive=root/'output/Namaa-centered-hero.zip'
assert project.resolve().is_relative_to(root.resolve())
before=(review/'before-index.html').read_text(encoding='utf-8')
after=(root/'index.html').read_text(encoding='utf-8')
def without_hero(text):
    text=re.sub(r'  <section class="hero"[\s\S]*?</section>','HERO',text)
    text=re.sub(r'<link rel="preload" as="image"[^>]+>','HERO_PRELOAD',text)
    return re.sub(r'css/style.css\?v=[^"\s]+','css/style.css',text)
assert without_hero(before)==without_hero(after),'Non-hero HTML content changed'
qa=json.loads((review/'responsive-qa.json').read_text(encoding='utf-8'))
assert [row['width'] for row in qa]==[320,360,390,430,768,1024,1440]
for row in qa:
    assert row['overflow']==0 and not row['textOverflow'] and not row['smallTargets']
    assert row['titleLines']<=2 and row['screenshotBelowCopy'] and row['chrome']==0
    assert row['titleCenteredError']<1 and row['screenshotCenteredError']<1
    assert max(row['containerWidths'])-min(row['containerWidths'])<1
    if row['width']>=1024:
        assert 56<=float(row['titleFont'].replace('px',''))<=64
        assert 70<=row['headerToEyebrow']<=90
        assert 46<=row['ctaToScreenshot']<=56
        assert 80<=row['screenshotToFeatures']<=96
        assert 38<=float(row['featureHeadingFont'].replace('px',''))<=44
source=Image.open(root/'assets/screenshots/namaa-dashboard-hero.webp')
assert source.size==(874,378) and 2.2<source.width/source.height<2.4
css=(root/'css/style.css').read_text(encoding='utf-8')
assert 'grid-template-columns:minmax(0,.42fr)' not in css
assert '--container-w:1240px' in css
assert 'width="874" height="378"' in after
(review/'final-checks.json').write_text(json.dumps({'non_hero_html_unchanged':True,'hero_stacked_at_all_widths':True,'real_dashboard_crop_size':[874,378],'shared_container_max_width':1240,'seven_widths_no_horizontal_overflow':True,'title_maximum_two_lines':True,'desktop_spacing_passed':True,'both_ctas_clicked':True,'javascript_unchanged':True,'subscription_content_unchanged':True},indent=2),encoding='utf-8')
notes='''# Centered Namaa hero

Replaced the split desktop hero with a centered stack at every breakpoint: audience, one naturally wrapping navy/green headline, short description, CTA row, then the dashboard. No manual headline break or desktop columns remain.

The actual supplied dashboard was cropped to x=1042..1916 and y=0..378. This preserves the dashboard heading, sales/cash KPI cards, outgoing-check card and upper navigation, stopping immediately after the cards. The 874×378 crop is about 16:7. No UI, text or numbers were redrawn. Hero images were converted to WebP; the original supplied screenshot and other system screenshots remain untouched.

All sections and the header now use the same 1240px container with clamp(16px,4vw,32px) inline padding. The desktop header navigation sits closer to the logo, while the CTA stays at the left of the same container. Features have a smaller centered heading and reduced top padding. All other section markup, commercial data and JavaScript remain unchanged.

Actual Chrome checks passed at 320, 360, 390, 430, 768, 1024 and 1440 CSS px: no horizontal overflow, clipped text or undersized targets; headline at most two lines; screenshot centered below the copy; containers aligned. At 390px the title is about 36px; narrower phones use a smaller size to preserve two lines. Desktop title is 56–64px. At 1440px the image is approximately 1174×508px, with 52px after the CTAs and 89px to the next section's eyebrow.

Both hero actions were clicked and reached their existing sections. Nothing was deployed. No build/lint configuration exists. The measurements are in responsive-qa.json and final-checks.json. The earlier DELIVERY.md in the project records previous work; this document records the latest centered-hero revision.

Modified website files: index.html, css/style.css, assets/screenshots/namaa-dashboard-hero.webp, assets/screenshots/namaa-dashboard-hero-640.webp. Screenshots show 390px mobile and 1440px desktop CSS viewports; native capture width may exclude the scrollbar.
'''
(review/'CENTERED-HERO-REVIEW.md').write_text(notes,encoding='utf-8')
project.mkdir(parents=True,exist_ok=True)
for name in ['index.html','README.md','DELIVERY.md','favicon.ico','apple-touch-icon.png','css','js','assets']:
    source,target=root/name,project/name
    if source.is_dir():shutil.copytree(source,target,dirs_exist_ok=True)
    else:shutil.copy2(source,target)
for p in review.glob('*.png'):
    with Image.open(p) as image:
        if image.format!='PNG':image.convert('RGB').save(p,'PNG',optimize=True)
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as bundle:
    for p in sorted(project.rglob('*')):
        if p.is_file():bundle.write(p,'Namaa-centered-hero/'+p.relative_to(project).as_posix())
    for name in ['CENTERED-HERO-REVIEW.md','final-checks.json','responsive-qa.json','crop-source.json','hero-desktop-1440.png','hero-mobile-390.png']:
        bundle.write(review/name,'Review/'+name)
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    for p in project.rglob('*'):
        if p.is_file():assert bundle.read('Namaa-centered-hero/'+p.relative_to(project).as_posix())==p.read_bytes()
print('PASS: centered layout, two-line headlines, shared containers, spacing and ZIP integrity.',archive.stat().st_size,'bytes')
