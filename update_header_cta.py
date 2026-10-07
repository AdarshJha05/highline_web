import os
import re

# 1. Update HTML files
html_files = ['website/index.html', 'website/about.html', 'website/contact.html']

for filename in html_files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the nav__phone link
    # From: <a class="nav__phone" href="https://wa.me/919392882152" rel="noopener" target="_blank">+91 93928 82152</a>
    # To: <a class="nav__phone" href="tel:+919392882152">+91 93928 82152</a>
    
    html = re.sub(
        r'<a[^>]*class="nav__phone"[^>]*>(\+91 93928 82152)</a>',
        r'<a class="nav__phone" href="tel:+919392882152">\1</a>',
        html
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update CSS file
css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add styles for nav__right .btn to match hero buttons
nav_btn_css = """
/* Enhance header CTA button to match hero buttons */
.nav__right .btn {
  padding: 16px 36px;
  font-size: 17px;
  letter-spacing: 0.02em;
}
"""

if '/* Enhance header CTA button' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write('\n' + nav_btn_css)

print("Header phone link and CTA padding updated.")
