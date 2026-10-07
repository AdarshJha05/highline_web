import os
import re
from bs4 import BeautifulSoup

html_files = ['website/index.html', 'website/about.html', 'website/contact.html']

for filename in html_files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    page_name = os.path.basename(filename)

    # 1. Add to desktop header
    nav_links_div = soup.find('div', class_='nav__links')
    if nav_links_div:
        # Check if Home already exists
        if not nav_links_div.find('a', href='index.html'):
            home_link = soup.new_tag('a', href='index.html', attrs={'class': 'nav__link'})
            home_link.string = 'Home'
            if page_name == 'index.html':
                home_link['class'].append('is-active')
                home_link['aria-current'] = 'page'
            nav_links_div.insert(0, home_link)

    # 2. Add to mobile drawer
    # The drawer links are direct children of the drawer__panel, after drawer__head
    drawer_panel = soup.find('div', class_='drawer__panel')
    if drawer_panel:
        if not drawer_panel.find('a', href='index.html', class_='drawer__link'):
            home_drawer_link = soup.new_tag('a', href='index.html', attrs={'class': 'drawer__link'})
            home_drawer_link.string = 'Home'
            if page_name == 'index.html':
                home_drawer_link['class'].append('is-active')
                home_drawer_link['aria-current'] = 'page'
            
            # Find the drawer__head and insert after it
            drawer_head = drawer_panel.find('div', class_='drawer__head')
            if drawer_head:
                drawer_head.insert_after(home_drawer_link)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Home links added to header and drawer.")
