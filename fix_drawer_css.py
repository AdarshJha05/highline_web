import re

drawer_css = """
/* ------------------------------------------------------------------ MOBILE DRAWER */
.nav__burger {
  display: none;
  width: 44px; height: 44px;
  border: 1px solid rgba(255, 255, 255, .45);
  background: rgba(11, 34, 60, .34);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-radius: 50%;
  cursor: pointer;
  align-items: center; justify-content: center;
  flex-direction: column; gap: 4px;
  padding: 0;
}
.nav__burger span {
  display: block; width: 17px; height: 2px; border-radius: 2px; background: #fff;
  transition: transform .3s var(--ease), opacity .2s;
}
.nav__burger[aria-expanded='true'] span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
.nav__burger[aria-expanded='true'] span:nth-child(2) { opacity: 0; }
.nav__burger[aria-expanded='true'] span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }

.drawer {
  position: fixed; inset: 0;
  z-index: 200;
  background: rgba(11, 60, 109, .45);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0; visibility: hidden;
  transition: opacity .3s, visibility .3s;
}
.drawer.is-open { opacity: 1; visibility: visible; }
.drawer__panel {
  position: absolute; top: 0; right: 0; bottom: 0;
  width: min(340px, 86vw);
  background: var(--white);
  padding: 24px 24px 32px;
  display: flex; flex-direction: column; gap: 6px;
  transform: translateX(100%);
  transition: transform .38s var(--ease);
  overflow-y: auto;
}
.drawer.is-open .drawer__panel { transform: none; }
.drawer__head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; }
.drawer__brand { display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 800; color: var(--navy); }
.drawer__brand img { width: 34px; height: 34px; object-fit: contain; }
.drawer__close {
  width: 40px; height: 40px; border-radius: 50%;
  border: 1px solid var(--border); background: var(--mist);
  font-size: 20px; line-height: 1; cursor: pointer; color: var(--navy);
  display: inline-flex; align-items: center; justify-content: center;
}
.drawer__link {
  padding: 14px 16px;
  border-radius: 14px;
  font-size: 16px; font-weight: 600;
  transition: background .2s;
  color: var(--navy);
}
.drawer__link:hover { background: var(--mist); }
.drawer__link.is-active { background: rgba(11, 60, 109, 0.1); color: var(--navy); }
.drawer .btn { margin-top: 14px; justify-content: center; }
.drawer__meta {
  margin-top: auto; padding-top: 24px;
  font-size: 13px; color: var(--muted); line-height: 1.7;
}
.drawer__meta a { color: var(--navy); font-weight: 600; }
body.is-locked { overflow: hidden; }

@media (max-width: 1024px) {
  .nav__links { display: none; }
  .nav__right .btn, .nav__right .nav__phone { display: none; }
  .nav__burger { display: inline-flex; }
}
"""

with open('website/assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write('\n' + drawer_css)

print("Drawer CSS appended.")
