import re

with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I need to completely replace the old hero layout CSS
# The old hero CSS starts around line 402 "/* ----------------------------------------------------------------- 7. Hero */"
# and goes until "/* -------------------------------------------------------------- 8. Marquee */"

# Let's write the new hero CSS to replace that entire block
new_hero_css = """/* ----------------------------------------------------------------- 7. Hero */
.hero-wrap { padding: 0; }
.hero {
  position: relative;
  overflow: hidden;
  background: var(--navy);
  isolation: isolate;
  min-height: 85vh;
  display: flex;
  align-items: center;
}
.hero > .ph { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; }
.hero__scrim {
  position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: linear-gradient(to right, rgba(11, 60, 109, 0.9) 0%, rgba(11, 60, 109, 0.6) 50%, rgba(11, 60, 109, 0.2) 100%),
              linear-gradient(to top, rgba(11, 60, 109, 0.8) 0%, transparent 40%);
}

.hero__content {
  position: relative;
  z-index: 10;
  padding: 80px var(--pad-x);
  max-width: 1440px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hero__title {
  margin: 24px 0 20px;
  color: var(--white);
  font-size: clamp(40px, 5.5vw, 68px);
  font-weight: 800;
  line-height: 1.1;
  max-width: 900px;
  text-wrap: balance;
  text-shadow: 0 4px 24px rgba(11, 60, 109, 0.4);
}

.hero__blurb p {
  color: rgba(255, 255, 255, 0.95);
  font-size: clamp(16px, 1.3vw, 20px);
  max-width: 650px;
  line-height: 1.6;
  text-shadow: 0 2px 10px rgba(11, 60, 109, 0.5);
}

.hero__actions {
  margin-top: 40px;
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.hero__trust {
  margin-top: 64px;
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
}

.trust-metric { 
  color: #fff; 
  display: flex; 
  flex-direction: column; 
  gap: 6px;
  position: relative;
}
.trust-metric:not(:last-child)::after {
  content: '';
  position: absolute;
  right: -24px;
  top: 15%;
  height: 70%;
  width: 1px;
  background: rgba(255, 255, 255, 0.2);
}

.trust-metric b { 
  font-size: clamp(28px, 3vw, 36px); 
  font-weight: 800; 
  color: var(--orange); 
  line-height: 1;
}
.trust-metric span { 
  font-size: 13px; 
  font-weight: 600; 
  text-transform: uppercase; 
  letter-spacing: 0.08em; 
  color: rgba(255, 255, 255, 0.85); 
}

/* -------------------------------------------------------------- 8. Marquee */"""

# Replace the block from "7. Hero" to "8. Marquee"
css = re.sub(r'/\* -+ 7\. Hero \*/.*?/\* -+ 8\. Marquee \*/', new_hero_css, css, flags=re.DOTALL)

# Let's also make sure to remove any leftover `.hero__title`, `.hero__actions`, `.hero__blurb` rules in the media queries!
# Tablet media query max-width: 1024px has absolute positioning resets.
mq_removals = [
    r'\.hero__title,\s*\.hero__actions,\s*\.hero__blurb\s*\{.*?\}',
    r'\.hero__title\s*\{.*?\}',
    r'\.hero__actions\s*\{.*?\}',
    r'\.hero__blurb\s*\{.*?\}',
    r'\.hero__blurb p\s*\{.*?\}',
    r'\.hero\s*\{\s*height: auto;.*?\}'
]

for removal in mq_removals:
    css = re.sub(removal, '', css, flags=re.DOTALL)

# Add responsive fixes for the new hero at the end of the file
responsive_hero = """
/* Responsive overrides for new hero */
@media (max-width: 1024px) {
  .hero { min-height: 60vh; }
  .hero__content { padding: 60px var(--pad-x); }
  .trust-metric:not(:last-child)::after { display: none; }
  .hero__trust { gap: 32px; margin-top: 48px; }
}
@media (max-width: 760px) {
  .hero { min-height: auto; padding: 40px 0; }
  .hero__content { padding: 40px var(--pad-x); }
  .hero__title { font-size: clamp(32px, 8vw, 42px); }
  .hero__actions { flex-direction: column; align-items: stretch; gap: 12px; margin-top: 32px; }
  .hero__actions .btn { justify-content: center; }
  .hero__trust { flex-direction: column; gap: 24px; margin-top: 40px; }
}
"""
css += responsive_hero

with open('website/assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Also fix the HTML to make sure the hero has the "hero" class which provides the background/layout context
with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We previously changed `<header class="hero--home">` to `<section id="main">`. We need it to be `<section id="main" class="hero">`.
html = html.replace('<section id="main">', '<section id="main" class="hero">')

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
