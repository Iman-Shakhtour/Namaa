from pathlib import Path
import re
import json

root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
html=html.replace('<head>', '<head>\n<base href="/">')
for name,config in {
    'enabled': {'whatsappNumber':'15555550123','instagramUrl':'https://www.instagram.com/namaa_test/','facebookUrl':'https://www.facebook.com/namaa_test/'},
    'invalid': {'whatsappNumber':'INVALID','instagramUrl':'javascript:alert(1)','facebookUrl':'https://example.com/'}
}.items():
    page=re.sub(r'<script src="js/site-config.js[^>]*></script>', '<script>window.SITE_CONFIG='+json.dumps(config)+';</script>',html)
    (root/'tmp'/('contact-'+name+'.html')).write_text(page,encoding='utf-8')
