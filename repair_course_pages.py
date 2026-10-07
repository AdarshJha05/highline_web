import os
from bs4 import BeautifulSoup

# We will grab header and footer from index.html which is known to be correct
with open('website/index.html', 'r', encoding='utf-8') as f:
    index_soup = BeautifulSoup(f, 'html.parser')

# Get Header (which includes the site-header)
header_tag = index_soup.find('header', class_='site-header')
header_html = str(header_tag)

# Get Footer and everything after it (including mobile drawer and scripts)
# We can just extract the body children that come after <main> in index.html
# Wait, index.html has <section id="main">, then <footer>, then <div class="drawer">, etc.
footer_tag = index_soup.find('footer', class_='footer')
drawer_tag = index_soup.find('div', class_='drawer')

# Let's just construct the end of the file manually from the soup
footer_html = str(footer_tag) + '\n' + str(drawer_tag)
# Get the scripts
for script in index_soup.find_all('script'):
    footer_html += '\n' + str(script)
# Get the floating WA button
wa_btn = index_soup.find('a', class_='float-wa')
if wa_btn:
    footer_html += '\n' + str(wa_btn)
footer_html += '\n</body>\n</html>'

def build_page(filename, is_course_list):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We need to extract the hero and main from the current courses.html / course.html
    current_soup = BeautifulSoup(html, 'html.parser')
    hero = current_soup.find('header', class_='hero')
    main = current_soup.find('main', id='main')
    style = current_soup.find('style')
    
    # The script specific to the course is currently at the end of the file.
    # Let's find it. It's a script tag that doesn't have src.
    custom_scripts = [s for s in current_soup.find_all('script') if not s.has_attr('src') and 'HL_TESTIMONIALS' not in s.text]
    
    # Assemble new HTML
    new_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
    # Copy head from index
    new_html += str(index_soup.find('head').decode_contents())
    new_html += f"\n</head>\n<body>\n"
    
    # Insert Header
    new_html += header_html
    
    # Insert Hero and Main
    if hero: new_html += str(hero)
    if main: new_html += str(main)
    if style: new_html += str(style)
    
    # Insert custom script
    for s in custom_scripts:
        new_html += str(s)
        
    # Insert Footer
    new_html += footer_html
    
    # Now parse the newly assembled HTML to fix active states
    final_soup = BeautifulSoup(new_html, 'html.parser')
    
    # Reset active states
    for link in final_soup.find_all('a', class_=lambda c: c and ('nav__link' in c or 'drawer__link' in c)):
        if 'is-active' in link.get('class', []):
            link['class'].remove('is-active')
        if link.has_attr('aria-current'):
            del link['aria-current']
            
    # Set active state
    # Both courses.html and course.html should highlight "Courses" in the nav
    for link in final_soup.find_all('a', href='courses.html'):
        if 'nav__link' in link.get('class', []) or 'drawer__link' in link.get('class', []):
            link['class'].append('is-active')
            link['aria-current'] = 'page'
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(final_soup))

build_page('website/courses.html', True)
build_page('website/course.html', False)

print("courses.html and course.html repaired.")
