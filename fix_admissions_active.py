import os
from bs4 import BeautifulSoup

html_path = 'website/admissions.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Remove active state from all navigation links
for link in soup.find_all('a', class_=lambda c: c and ('nav__link' in c or 'drawer__link' in c)):
    classes = link.get('class', [])
    if 'is-active' in classes:
        classes.remove('is-active')
        link['class'] = classes
    if link.has_attr('aria-current'):
        del link['aria-current']

# Apply active state ONLY to the admissions link
for link in soup.find_all('a', href='admissions.html'):
    classes = link.get('class', [])
    if 'nav__link' in classes or 'drawer__link' in classes:
        classes.append('is-active')
        link['class'] = classes
        link['aria-current'] = 'page'

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Admissions active state fixed.")
