from pathlib import Path

root = Path(__file__).resolve().parents[1]
css_path = root / "css" / "style.css"

css = css_path.read_text(encoding="utf-8")

# Define our improved CSS blocks

# 1. Bento Grid Styles
old_bento_css = """/* Feature grid: one large product view followed by a balanced two-column set. */
.features{background:var(--bg)}
.bento-grid{display:grid;grid-template-columns:1fr;gap:16px}
.bento-card{position:relative;min-height:340px;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white)}
.bento-card__copy{position:relative;z-index:2;padding:24px}
.bento-card__copy>span,.story-mobile article>div>span{display:inline-grid;place-items:center;min-width:34px;height:28px;padding-inline:8px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.bento-card h3{margin-top:6px}
.bento-card p{max-width:420px;margin-top:6px;color:var(--muted);font-size:16px}
.bento-card img{position:absolute;inset-inline:20px;bottom:0;width:calc(100% - 40px);height:190px;object-fit:cover;object-position:right top;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--bg)}"""

new_bento_css = """/* Feature grid: organized, balanced, and responsive SaaS product cards */
.features{background:var(--bg)}
.bento-grid{display:grid;grid-template-columns:1fr;gap:20px}
.bento-card{display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--white);box-shadow:0 4px 20px rgb(7 24 47 / 4%);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.bento-card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgb(7 24 47 / 8%);border-color:rgb(13 147 104 / 35%)}
.bento-card__copy{padding:26px 26px 14px}
.bento-card__copy>span,.story-mobile article>div>span{display:inline-grid;place-items:center;min-width:36px;height:28px;padding-inline:10px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.bento-card h3{margin-top:10px;font-size:22px}
.bento-card p{margin-top:6px;color:var(--muted);font-size:15px;line-height:1.6}
.bento-card__media{margin-top:auto;padding-inline:20px;padding-top:12px;background:linear-gradient(180deg, transparent 0%, #f1f5f9 100%)}
.bento-card__media img{display:block;width:100%;height:auto;max-height:220px;object-fit:cover;object-position:top right;border:1px solid var(--border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--white);box-shadow:0 -2px 10px rgb(0 0 0 / 2%)}
.bento-card--hero{background:linear-gradient(180deg, var(--white) 0%, #F4FAF7 100%)}
.bento-card--hero .bento-card__media img{max-height:300px}"""

# 2. Workflow (Offline) Styles
old_workflow_css = """/* Offline */
.offline{background:var(--navy);color:var(--white)}
.offline__inner{max-width:1200px}
.offline h2{color:var(--white)}
.offline__lead{max-width:650px;margin-top:16px;color:var(--white);font-size:18px;opacity:.74}
.workflow{list-style:none;padding:0;margin-top:40px;display:grid;gap:16px}
.workflow li{position:relative;overflow:hidden;border:1px solid rgb(255 255 255 / 12%);border-radius:var(--radius-lg);background:rgb(255 255 255 / 4%);box-shadow:0 18px 48px rgb(7 24 47 / 22%)}
.workflow li img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;object-position:center top;border-bottom:1px solid rgb(255 255 255 / 12%);background:var(--navy)}
.workflow li>div{position:relative;padding:20px;padding-inline-start:56px}
.workflow li b{position:absolute;inset-block-start:18px;inset-inline-start:18px;display:grid;place-items:center;width:28px;height:28px;border:1px solid var(--green-bright);border-radius:50%;color:var(--green-bright);font-size:13px}
.workflow h3{color:var(--white);font-size:20px}
.workflow p{margin-top:3px;color:var(--white);font-size:14px;opacity:.68}"""

new_workflow_css = """/* Offline: 3 distinct system states */
.offline{background:var(--navy);color:var(--white)}
.offline__inner{max-width:1200px}
.offline h2{color:var(--white)}
.offline__lead{max-width:650px;margin-top:16px;color:var(--white);font-size:18px;opacity:.74}
.workflow{list-style:none;padding:0;margin-top:40px;display:grid;grid-template-columns:1fr;gap:20px}
.workflow li{position:relative;display:flex;flex-direction:column;overflow:hidden;border:1px solid rgb(255 255 255 / 14%);border-radius:var(--radius-lg);background:rgb(255 255 255 / 5%);box-shadow:0 18px 48px rgb(7 24 47 / 35%);transition:transform .25s ease,border-color .25s ease,background .25s ease}
.workflow li:hover{border-color:var(--green-bright);background:rgb(255 255 255 / 8%);transform:translateY(-4px)}
.workflow__preview{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;background:#051224;border-bottom:1px solid rgb(255 255 255 / 12%)}
.workflow__preview img{display:block;width:100%;height:100%;object-fit:cover;object-position:top center;transition:transform .3s ease}
.workflow li:hover .workflow__preview img{transform:scale(1.03)}
.workflow__content{position:relative;padding:22px 20px 22px 64px;flex:1;display:flex;flex-direction:column}
.workflow li b{position:absolute;inset-block-start:20px;inset-inline-start:18px;display:grid;place-items:center;width:32px;height:32px;border:2px solid var(--green-bright);border-radius:50%;background:rgb(18 184 134 / 18%);color:var(--green-bright);font-size:14px;font-weight:800}
.workflow h3{color:var(--white);font-size:20px;font-weight:800}
.workflow p{margin-top:6px;color:rgb(255 255 255 / 75%);font-size:14px;line-height:1.55}"""

# 3. Pricing Styles with rich colors and prominent highlights
old_pricing_css = """/* Pricing */
.pricing{background:var(--white)}
.offer-banner{display:grid;gap:24px;margin-bottom:64px;padding:24px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--navy);color:var(--white)}
.offer-banner h2{margin-top:6px;color:var(--white);font-size:clamp(26px,3vw,38px)}
.offer-banner>div>p:not(.eyebrow){max-width:560px;margin-top:10px;color:var(--white);opacity:.74}
.offer-countdown{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;direction:ltr}
.offer-countdown span{display:grid;place-items:center;min-height:82px;padding:10px 6px;border:1px solid rgb(255 255 255 / 12%);border-radius:var(--radius-sm);background:rgb(255 255 255 / 4%)}
.offer-countdown b{color:var(--white);font-size:28px;line-height:1}
.offer-countdown small{margin-top:7px;color:var(--white);font-size:12px;opacity:.68}
.offer-countdown.is-ended{grid-template-columns:1fr;color:var(--white);font-weight:800}
.pricing-grid{display:grid;gap:16px;max-width:960px;margin-inline:auto}
.price-card{display:flex;flex-direction:column;padding:24px;border:1px solid var(--border);border-top:4px solid var(--navy);border-radius:var(--radius-lg);background:var(--white)}
.price-card--featured{border-top-color:var(--green);box-shadow:0 20px 55px rgb(7 24 47 / 10%)}
.price-card__badge{align-self:flex-start;margin-bottom:16px;padding:7px 12px;border-radius:999px;background:var(--mint);color:var(--green);font-size:13px;font-weight:800}
.price-card__badge--soft{background:var(--navy);color:var(--white)}
.price-card h3{font-size:24px}
.price-card__desc{margin-top:8px;color:var(--muted);font-size:15px}
.price-main{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;margin-top:20px;padding:18px;border:1px solid var(--border);border-inline-start:4px solid var(--green);border-radius:var(--radius-sm);background:var(--mint)}
.price-main b{color:var(--green);font-size:40px;line-height:1.2;direction:ltr;unicode-bidi:isolate}
.price-main small,.price-installment small{font-size:.5em;padding-inline-end:4px}
.price-main span,.price-or{color:var(--muted);font-size:14px}
.price-or{margin-block:16px 8px}
.price-renew,.price-installment{margin-top:12px;padding:16px;border-radius:var(--radius-sm);font-size:14px}
.price-renew{border:1px solid var(--border);background:var(--mint);color:var(--muted)}
.price-renew b{color:var(--green)}
.price-installment{background:var(--navy);color:var(--white)}
.price-installment>div{display:flex;align-items:baseline;gap:10px}
.price-installment b{color:var(--white);font-size:29px;direction:ltr;unicode-bidi:isolate}
.price-installment span,.price-installment em{color:var(--white);font-size:14px;font-style:normal;opacity:.76}
.price-installment em{display:block;margin-top:2px}
.price-card__list{margin-block:20px}
.check-list li{display:flex;gap:8px;margin-top:6px;color:var(--muted);font-size:14px}
.check-list li::before{content:'✓';color:var(--green);font-weight:800}
.price-card .btn{margin-top:auto}
.pricing-note{margin-top:20px;text-align:center;color:var(--muted);font-size:14px}"""

new_pricing_css = """/* Pricing with highlighted, vibrant colors for all payment options */
.pricing{background:var(--white)}
.offer-banner{display:grid;gap:24px;margin-bottom:64px;padding:24px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--navy);color:var(--white)}
.offer-banner h2{margin-top:6px;color:var(--white);font-size:clamp(26px,3vw,38px)}
.offer-banner>div>p:not(.eyebrow){max-width:560px;margin-top:10px;color:var(--white);opacity:.74}
.offer-countdown{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;direction:ltr}
.offer-countdown span{display:grid;place-items:center;min-height:82px;padding:10px 6px;border:1px solid rgb(255 255 255 / 12%);border-radius:var(--radius-sm);background:rgb(255 255 255 / 4%)}
.offer-countdown b{color:var(--white);font-size:28px;line-height:1}
.offer-countdown small{margin-top:7px;color:var(--white);font-size:12px;opacity:.68}
.offer-countdown.is-ended{grid-template-columns:1fr;color:var(--white);font-weight:800}
.pricing-grid{display:grid;grid-template-columns:1fr;gap:24px;max-width:980px;margin-inline:auto}
.price-card{position:relative;display:flex;flex-direction:column;padding:32px 28px;border-radius:var(--radius-lg);background:var(--white);border:2px solid var(--border);transition:transform .25s ease,box-shadow .25s ease}
.price-card:hover{transform:translateY(-4px)}
.price-card--featured{border-color:var(--green);box-shadow:0 24px 60px rgb(13 147 104 / 14%)}
.price-card--flex{border-color:#CBD5E1;box-shadow:0 20px 50px rgb(7 24 47 / 6%)}
.price-card__header{margin-bottom:8px}
.price-card__badge{display:inline-block;margin-bottom:16px;padding:6px 14px;border-radius:999px;font-size:13px;font-weight:800}
.price-card__badge--featured{background:linear-gradient(135deg, var(--green) 0%, #065F46 100%);color:var(--white);box-shadow:0 4px 12px rgb(13 147 104 / 25%)}
.price-card__badge--navy{background:var(--navy);color:var(--white)}
.price-card h3{font-size:26px;color:var(--text)}
.price-card__desc{margin-top:8px;color:var(--muted);font-size:15px;line-height:1.5}

/* Highlighted Price Containers */
.price-main{display:flex;flex-direction:column;gap:6px;margin-top:20px;padding:20px;border-radius:var(--radius-md);position:relative}
.price-main--featured{background:linear-gradient(135deg, #E6F8F0 0%, #CEF5E4 100%);border:2px solid var(--green)}
.price-main--navy{background:linear-gradient(135deg, #F1F5F9 0%, #E2E8F0 100%);border:2px solid #94A3B8}
.price-tag-label{font-size:13px;font-weight:700;color:var(--muted)}
.price-main--featured .price-tag-label{color:#065F46}
.price-main--navy .price-tag-label{color:#334155}
.price-amount-row{display:flex;align-items:center;justify-content:space-between;gap:12px}
.price-main b{font-size:44px;line-height:1.1;font-weight:800;direction:ltr;unicode-bidi:isolate}
.price-main--featured b{color:#065F46}
.price-main--navy b{color:var(--navy)}
.price-main small,.price-installment small{font-size:.5em;padding-inline-end:3px}
.price-badge-pill{padding:5px 12px;border-radius:8px;font-size:13px;font-weight:800}
.price-main--featured .price-badge-pill{background:var(--green);color:var(--white)}
.price-badge-pill--navy{background:var(--navy);color:var(--white)}
.price-subtext{font-size:13px;color:var(--muted);margin-top:2px}
.price-main--featured .price-subtext{color:#047857}

/* Renewal Highlight Box */
.price-renew{display:flex;align-items:flex-start;gap:12px;margin-top:14px;padding:14px 16px;border-radius:var(--radius-sm);background:#FFFBEB;border:2px solid #F59E0B;color:#92400E}
.price-renew__icon{font-size:20px;line-height:1;flex:0 0 auto;margin-top:2px}
.price-renew__text b{display:block;color:#B45309;font-size:16px;font-weight:800}
.price-renew__text span{display:block;margin-top:2px;font-size:13px;color:#92400E;line-height:1.4}

/* Installment Containers */
.price-divider{position:relative;text-align:center;margin-block:18px 12px}
.price-divider::before{content:'';position:absolute;top:50%;left:0;right:0;height:1px;background:var(--border);z-index:1}
.price-divider span{position:relative;z-index:2;display:inline-block;padding-inline:12px;background:var(--white);color:var(--muted);font-size:13px;font-weight:700}
.price-installment{display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:var(--radius-md);color:var(--white)}
.price-installment--featured{background:linear-gradient(135deg, #07182F 0%, #0D3159 100%);border:1.5px solid #1E3D6B}
.price-installment--navy{background:linear-gradient(135deg, #0A1E38 0%, #153864 100%);border:1.5px solid #1E3D6B}
.price-installment__top{display:flex;align-items:baseline;gap:8px}
.price-installment--featured .price-installment__top b{color:var(--green-bright);font-size:32px;font-weight:800;direction:ltr;unicode-bidi:isolate}
.price-installment--navy .price-installment__top b{color:#38BDF8;font-size:32px;font-weight:800;direction:ltr;unicode-bidi:isolate}
.price-installment span{color:rgb(255 255 255 / 80%);font-size:14px;font-weight:600}
.price-installment__detail{display:flex;align-items:center;gap:10px;margin-top:4px}
.installment-badge{padding:3px 8px;border-radius:6px;font-size:12px;font-weight:800;background:rgb(18 184 134 / 20%);color:var(--green-bright);border:1px solid rgb(18 184 134 / 35%)}
.installment-badge--cyan{background:rgb(56 189 248 / 20%);color:#38BDF8;border-color:rgb(56 189 248 / 35%)}
.price-installment em{color:rgb(255 255 255 / 75%);font-size:13px;font-style:normal}

.price-card__list{margin-block:22px}
.check-list li{display:flex;gap:10px;margin-top:10px;color:var(--text);font-size:15px;line-height:1.5}
.check-list li::before{content:'✓';color:var(--green);font-weight:800;font-size:17px;flex:0 0 auto}
.btn-navy{background:var(--navy);color:var(--white);border:1px solid #1E3D6B}
.btn-navy:hover{background:var(--green);border-color:var(--green);color:var(--white)}
.btn-lg{min-height:54px;font-size:17px}
.price-card .btn{margin-top:auto}
.pricing-note{margin-top:24px;text-align:center;color:var(--muted);font-size:15px}"""

assert old_bento_css in css, "old_bento_css not found"
assert old_workflow_css in css, "old_workflow_css not found"
assert old_pricing_css in css, "old_pricing_css not found"

css = css.replace(old_bento_css, new_bento_css)
css = css.replace(old_workflow_css, new_workflow_css)
css = css.replace(old_pricing_css, new_pricing_css)

# Update responsive section if needed
old_resp = """.bento-card img{height:235px}
  .bento-card--hero{grid-column:1 / -1;min-height:460px}
  .bento-card--hero img{height:300px}"""

if old_resp in css:
    new_resp = """.bento-card .bento-card__media img{max-height:240px}
  .bento-card--hero{grid-column:1 / -1}
  .bento-card--hero .bento-card__media img{max-height:340px}"""
    css = css.replace(old_resp, new_resp)

css_path.write_text(css, encoding="utf-8")
print("css/style.css saved successfully!")

