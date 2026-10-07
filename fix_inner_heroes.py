import os
from bs4 import BeautifulSoup

for filename in ['website/about.html', 'website/contact.html']:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the hero container
    hero = soup.find(lambda tag: tag.name in ['header', 'section'] and 'hero' in tag.get('class', []))
    if not hero: continue
    
    # We need to extract the title, blurb, and eyebrow, and wrap them in .hero__content
    title = hero.find('h1', class_='hero__title')
    blurb = hero.find('div', class_='hero__blurb')
    
    if not title or not blurb: continue
    
    # Extract the eyebrow if it's inside the blurb
    eyebrow = blurb.find('span', class_=lambda c: c and 'eyebrow' in c)
    if eyebrow:
        eyebrow.extract()
    else:
        # Check if it's outside
        eyebrow = hero.find('span', class_=lambda c: c and 'eyebrow' in c)
        if eyebrow: eyebrow.extract()
        
    # Extract title and blurb from hero
    title.extract()
    blurb.extract()
    
    # Create hero__content
    content_div = soup.new_tag('div', attrs={'class': 'hero__content'})
    
    if eyebrow:
        content_div.append(eyebrow)
    content_div.append(title)
    content_div.append(blurb)
    
    hero.append(content_div)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Hero HTML fixed for about.html and contact.html.")
