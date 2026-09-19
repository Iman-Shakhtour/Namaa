# Hero refinement only

Changed: `index.html` hero markup and its image preload, `css/style.css` hero selectors, and two new cropped screenshot assets (`namaa-dashboard-hero.webp` and `namaa-dashboard-hero-640.webp`). JavaScript, pricing, hardware, all other sections, existing screenshots and brand assets are unchanged.

The real supplied 1916×869 dashboard was cropped to x=788..1916, y=0..487 (1128×487): three colored KPI cards, the outgoing-check card, and upper right navigation. No UI, numbers or text were redrawn. Original images remain preserved in the earlier Review package.

Removed the hero's fabricated window bar, caption, zoom button and checkmark row. Added the requested two-line navy/green title, short description, lighter secondary action and a subtle mint radial glow. Desktop columns are 42%/58% with a 24px gap.

Desktop hero height at 1440px: 608.45px before, 363.39px after (40.3% shorter). Actual browser checks passed at 320, 360, 390, 430, 768, 1024 and 1440 CSS px: no horizontal overflow or text clipping, title two lines, description at most two lines, mobile title at most 36px, full-content-width mobile image and buttons at least 44px.

The primary action was clicked and reached `#showcase`. The secondary action was clicked and reached `#mazaya`. Automated comparison confirms the page outside the hero and CSS outside hero selectors are unchanged. This is local-only work; nothing was deployed. No build or lint configuration exists.

`hero-desktop-1440.png` and `hero-mobile-390.png` show the result; CSS viewport widths include the browser scrollbar. `responsive-qa.json`, `scope-check.json` and `crop-source.json` record measurements and crop provenance. The project includes the earlier DELIVERY.md as the record of prior work; this file describes the latest hero-only change.
