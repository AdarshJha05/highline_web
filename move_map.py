import os
from bs4 import BeautifulSoup

html_path = 'website/contact.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the map div
map_div = soup.find('div', class_='map-wide')
if map_div:
    # Extract the map
    extracted_map = map_div.extract()
    
    # Find the inquiry section
    inquiry_section = soup.find('section', class_='inquiry')
    if inquiry_section:
        # Create a new section for the map below the inquiry form
        map_section = soup.new_tag('section', attrs={'class': 'section'})
        map_section.append(extracted_map)
        
        # Insert the map section right after the inquiry section
        inquiry_section.insert_after(map_section)

# Save the changes
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Map moved below the inquiry form.")
