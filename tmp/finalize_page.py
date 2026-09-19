from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
used = set(re.findall(r'<use href="#([^"]+)', html))
html = re.sub(r'<symbol id="([^"]+)"[\s\S]*?</symbol>', lambda m: m[0] if m[1] in used else '', html)
html = re.sub(r'<defs>[\s\S]*?</defs>', '', html)
html = re.sub(r'\n\s*\n\s*\n', '\n\n', html)
html = html.replace('?v=20260915', '?v=20260915b')
html = html.replace('id="pricing"', 'id="pricing" aria-labelledby="pricing-title"')
html = html.replace('<h2>طريقتان واضحتان للدفع</h2>', '<h2 id="pricing-title">طريقتان واضحتان للدفع</h2>')
page.write_text(html, encoding='utf-8')
