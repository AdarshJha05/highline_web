import os
import re

html_files = ['website/index.html', 'website/about.html', 'website/contact.html']

for filename in html_files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the nav__phone anchor entirely
    html = re.sub(r'<a[^>]*class="nav__phone"[^>]*>.*?</a>\s*', '', html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Phone number removed from headers.")
