import os
import re

css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove the rigid height overrides for .hero--home in the media queries
css = re.sub(r'\.hero--home\s*\{\s*height:\s*720px;\s*\}', '', css)
css = re.sub(r'\.hero--home\s*\{\s*height:\s*520px;\s*\}', '', css)

# 2. Add a clear layout fix at the end to ensure the hero handles the fixed header
fix_css = """
/* ============================================================================
   MOBILE HERO LAYOUT FIXES
   ========================================================================== */

/* Remove any legacy absolute heights and ensure the header doesn't overlap the text */
.hero--home {
  height: auto !important;
  min-height: 100vh !important;
  padding-top: 100px !important; /* clear the sticky header */
}

@media (max-width: 760px) {
  .hero--home {
    min-height: auto !important;
    padding-top: 120px !important; /* more clearance for mobile header */
    padding-bottom: 60px !important;
  }
}
"""

if 'MOBILE HERO LAYOUT FIXES' not in css:
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css + '\n' + fix_css)
    print("Fixed hero--home height constraints.")
else:
    print("Fix already applied.")
