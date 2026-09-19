from pathlib import Path
from PIL import Image
import json
import re

root=Path(__file__).resolve().parents[1]
review=root/'output/centered-hero-review'
review.mkdir(parents=True,exist_ok=True)
for name in ['index.html','css/style.css']:
    (review/('before-'+Path(name).name)).write_bytes((root/name).read_bytes())
original=Image.open(root/'output/review/original-screenshots/namaa-dashboard-desktop.png')
box=(1042,0,1916,378)
crop=original.crop(box).convert('RGB')
crop.save(root/'assets/screenshots/namaa-dashboard-hero.webp','WEBP',quality=95,method=6)
small=crop.resize((640,round(640*crop.height/crop.width)),Image.Resampling.LANCZOS)
small.save(root/'assets/screenshots/namaa-dashboard-hero-640.webp','WEBP',quality=94,method=6)
(review/'crop-source.json').write_text(json.dumps({'original_size':list(original.size),'crop_box':list(box),'crop_size':list(crop.size),'aspect_ratio':round(crop.width/crop.height,4),'operations':['crop','WebP conversion'],'source':'supplied Namaa dashboard PNG'},indent=2),encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
html=html.replace('<h1 id="hero-title"><span class="hero__title-main">كل شغلك وحساباتك</span> <span class="hero__title-accent">بمكان واحد.</span></h1>','<h1 id="hero-title">كل شغلك وحساباتك <span class="hero__title-accent">بمكان واحد.</span></h1>')
html=html.replace('        <p class="hero__summary">بيع • مخزون • حسابات • تقارير</p>\n','')
sizes='(min-width: 1280px) 1176px, (min-width: 768px) min(88vw, calc(100vw - 64px)), calc(100vw - 32px)'
html=html.replace('namaa-dashboard-hero.webp 1128w','namaa-dashboard-hero.webp 874w')
html=re.sub(r'(?:imagesizes|sizes)="\(min-width: 1280px\) 692px[^"\n]*"',lambda m:('imagesizes' if m.group().startswith('imagesizes') else 'sizes')+'="'+sizes+'"',html)
html=html.replace('width="1128" height="487"','width="874" height="378"')
html=html.replace('الجزء العلوي من لوحة تحكم نماء: بطاقات المبيعات والصندوق وذمم العملاء والشيكات الصادرة، مع قائمة أدوات النظام على اليمين','الجزء العلوي من لوحة تحكم نماء: مؤشر الاتصال والمزامنة، بطاقات المبيعات والصندوق والشيكات الصادرة، وقائمة أدوات النظام على اليمين')
html=html.replace('css/style.css?v=20260916hero','css/style.css?v=20260916centered')
(root/'index.html').write_text(html,encoding='utf-8')
