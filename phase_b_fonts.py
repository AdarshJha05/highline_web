import re
import os

font_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">'

for filename in ['website/index.html', 'website/about.html', 'website/contact.html']:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Hanken\+Grotesk[^>]*>', font_link, html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
