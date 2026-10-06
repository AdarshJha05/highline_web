import re

with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add sticky header and new layout CSS
new_styles = """
/* ------------------------------------------------------------------ 6. Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--navy);
  color: var(--white);
  box-shadow: 0 4px 12px rgba(11, 60, 109, .15);
}
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px var(--pad-x);
  max-width: 1440px;
  margin: 0 auto;
}
.nav__brand { display: flex; align-items: center; gap: 12px; }
.nav__mark {
  width: 40px; height: 40px; background: #fff; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}
.nav__word { display: flex; flex-direction: column; line-height: 1.1; }
.nav__word b { font-size: 18px; font-weight: 800; color: #fff; letter-spacing: -.02em; }
.nav__word span { font-size: 9px; font-weight: 700; color: rgba(255,255,255,.8); letter-spacing: .2em; margin-top: 2px; }
.nav__links { display: flex; gap: 24px; align-items: center; }
.nav__link { font-size: 15px; font-weight: 500; color: rgba(255,255,255,.9); transition: color .2s; }
.nav__link:hover { color: var(--orange); }
.nav__right { display: flex; align-items: center; gap: 24px; }
.nav__phone { font-size: 15px; font-weight: 600; color: #fff; }

.float-wa {
  position: fixed;
  bottom: 24px; right: 24px; z-index: 90;
  width: 56px; height: 56px;
  background: #25D366; color: #fff;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 24px rgba(37, 211, 102, .35);
  transition: transform .25s var(--ease);
}
.float-wa:hover { transform: translateY(-4px) scale(1.05); }

/* Rebuilt Hero */
.hero__content {
  position: relative;
  z-index: 10;
  padding: 120px var(--pad-x);
  max-width: 1240px;
  margin: 0 auto;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hero__title {
  margin: 20px 0;
  color: var(--white);
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(42px, 5vw, 64px);
  font-weight: 800;
  line-height: 1.1;
  max-width: 800px;
  text-wrap: balance;
}
.hero__blurb p {
  color: rgba(255,255,255,.9);
  font-size: clamp(16px, 1.2vw, 18px);
  max-width: 600px;
  line-height: 1.6;
}
.hero__actions { margin-top: 32px; display: flex; gap: 16px; }
.hero__trust {
  margin-top: 64px;
  display: flex;
  gap: 40px;
  border-top: 1px solid rgba(255,255,255,.2);
  padding-top: 32px;
  max-width: 800px;
}
.trust-metric { color: #fff; display: flex; flex-direction: column; gap: 4px; }
.trust-metric b { font-size: 32px; font-weight: 800; color: var(--orange); }
.trust-metric span { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: .05em; color: rgba(255,255,255,.8); }

/* Typography */
h1, h2, h3, h4 { font-family: 'Montserrat', sans-serif; color: var(--navy); }
.h2 { font-size: clamp(28px, 3.5vw, 40px); font-weight: 700; color: var(--navy); }
.section { padding: 100px var(--pad-x); }
"""

css = re.sub(r'/\* -+ 6\. Nav \*/.*?/\* -+ 7\. Hero \*/', new_styles + '\n/* ----------------------------------------------------------------- 7. Hero */', css, flags=re.DOTALL)

with open('website/assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
