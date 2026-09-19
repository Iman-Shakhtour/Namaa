from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO
import json

root = Path(__file__).resolve().parents[1]
products = json.loads((root / 'tmp/logix-verified-products.json').read_text(encoding='utf-8'))
ids = ['wired-scanner', 'haixun-scanner', 'rugged-scanner', 'desktop-2d-scanner', 'wireless-scanner', 'scanner-stand', 'thermal-paper', 'barcode-labels', 'xprinter-n160ii', 'xprinter-alternate']
destination = root / 'assets/hardware'
originals = root / 'output/review-v2/original-hardware'
assert destination.resolve().is_relative_to(root.resolve())
destination.mkdir(parents=True, exist_ok=True)
originals.mkdir(parents=True, exist_ok=True)
for item, identifier in zip(products, ids):
    if identifier == 'xprinter-alternate': continue
    source = item['sourceImageUrl']
    assert urlparse(source).hostname == 'logix-mobile.com'
    request = Request(source, headers={'User-Agent':'Mozilla/5.0'})
    data = urlopen(request, timeout=25).read()
    assert len(data) < 12_000_000
    original = Image.open(BytesIO(data))
    (originals / (identifier + '.webp')).write_bytes(data)
    image = original.convert('RGB')
    image.thumbnail((640,640), Image.Resampling.LANCZOS)
    target = destination / (identifier + '.webp')
    image.save(target, 'WEBP', quality=91, method=6)
    item.update(id=identifier,image=target.relative_to(root).as_posix(),width=image.width,height=image.height)
    print(identifier, image.size, target.stat().st_size)
(root / 'tmp/logix-hardware-ready.json').write_text(json.dumps(products,ensure_ascii=False,indent=2),encoding='utf-8')
