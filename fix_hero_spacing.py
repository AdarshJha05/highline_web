import os

css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Find the start of the block
start_marker = "/* ============================================================================\n   MOBILE HERO LAYOUT FIXES\n   ========================================================================== */"
if start_marker in css:
    css = css[:css.find(start_marker)]
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css.strip() + '\n')
    print("Removed aggressive hero layout fixes.")

# We also should ensure .hero min-height isn't forcing too much space
css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change .hero min-height: 85vh to min-height: 600px or auto
css = css.replace('min-height: 85vh;', 'min-height: 600px;')

# For mobile specifically, ensure padding clears header without forcing huge min-height
mobile_fix = """
/* ============================================================================
   HERO MOBILE SPACING
   ========================================================================== */
@media (max-width: 1024px) {
  .hero { min-height: auto !important; padding-top: 100px; padding-bottom: 40px; }
  .hero__content { padding: 0 var(--pad-x) !important; }
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css + '\n' + mobile_fix)
print("Applied tighter mobile spacing.")
