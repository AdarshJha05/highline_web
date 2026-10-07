import os
from bs4 import BeautifulSoup

# 1. Update CSS to include .nav__link.is-active
css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.nav__link.is-active' not in css:
    css = css.replace('.nav__link:hover { color: var(--orange); }', 
                      '.nav__link:hover { color: var(--orange); }\n.nav__link.is-active { color: var(--orange); font-weight: 700; }')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update HTML files to set active classes
files = ['website/index.html', 'website/about.html', 'website/contact.html']
for filepath in files:
    if not os.path.exists(filepath):
        continue
    
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Reset all active states first
    for link in soup.find_all('a', class_=lambda c: c and ('nav__link' in c or 'drawer__link' in c)):
        if 'is-active' in link.get('class', []):
            link['class'].remove('is-active')
        if link.has_attr('aria-current'):
            del link['aria-current']
            
    # Set active state based on filename
    for link in soup.find_all('a', href=filename):
        if 'nav__link' in link.get('class', []) or 'drawer__link' in link.get('class', []):
            link['class'].append('is-active')
            link['aria-current'] = 'page'
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Active classes applied to HTML files.")
