# Centered Namaa hero

Replaced the split desktop hero with a centered stack at every breakpoint: audience, one naturally wrapping navy/green headline, short description, CTA row, then the dashboard. No manual headline break or desktop columns remain.

The actual supplied dashboard was cropped to x=1042..1916 and y=0..378. This preserves the dashboard heading, sales/cash KPI cards, outgoing-check card and upper navigation, stopping immediately after the cards. The 874×378 crop is about 16:7. No UI, text or numbers were redrawn. Hero images were converted to WebP; the original supplied screenshot and other system screenshots remain untouched.

All sections and the header now use the same 1240px container with clamp(16px,4vw,32px) inline padding. The desktop header navigation sits closer to the logo, while the CTA stays at the left of the same container. Features have a smaller centered heading and reduced top padding. All other section markup, commercial data and JavaScript remain unchanged.

Actual Chrome checks passed at 320, 360, 390, 430, 768, 1024 and 1440 CSS px: no horizontal overflow, clipped text or undersized targets; headline at most two lines; screenshot centered below the copy; containers aligned. At 390px the title is about 36px; narrower phones use a smaller size to preserve two lines. Desktop title is 56–64px. At 1440px the image is approximately 1174×508px, with 52px after the CTAs and 89px to the next section's eyebrow.

Both hero actions were clicked and reached their existing sections. Nothing was deployed. No build/lint configuration exists. The measurements are in responsive-qa.json and final-checks.json. The earlier DELIVERY.md in the project records previous work; this document records the latest centered-hero revision.

Modified website files: index.html, css/style.css, assets/screenshots/namaa-dashboard-hero.webp, assets/screenshots/namaa-dashboard-hero-640.webp. Screenshots show 390px mobile and 1440px desktop CSS viewports; native capture width may exclude the scrollbar.
