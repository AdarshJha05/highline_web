import os

css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

nav_active_css = """
/* ============================================================================
   ACTIVE STATE ENHANCEMENTS
   ========================================================================== */

/* Desktop header active link underline */
.nav__link.is-active {
  text-decoration: underline !important;
  text-underline-offset: 6px !important;
  text-decoration-thickness: 2px !important;
}

/* Mobile drawer active link orange color */
.drawer__link.is-active {
  color: var(--orange) !important;
}
"""

if 'ACTIVE STATE ENHANCEMENTS' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write('\n' + nav_active_css)

print("Active states enhanced.")
