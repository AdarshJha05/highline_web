import os
import re
from bs4 import BeautifulSoup

for filename in ['website/about.html', 'website/contact.html']:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    hero = soup.find(lambda tag: tag.name in ['header', 'section'] and 'hero' in tag.get('class', []))
    if hero:
        eyebrow = hero.find('span', class_=lambda c: c and 'eyebrow' in c)
        if eyebrow and 'eyebrow--light' not in eyebrow.get('class', []):
            eyebrow['class'].append('eyebrow--light')
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Eyebrow light class added.")
