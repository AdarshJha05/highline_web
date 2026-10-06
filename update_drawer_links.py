import os
import re

new_drawer_links = """
  <a class="drawer__link" href="courses.html">Courses</a>
  <a class="drawer__link" href="about.html">About</a>
  <a class="drawer__link" href="admissions.html">Admissions</a>
  <a class="drawer__link" href="resources.html">Resources</a>
  <a class="drawer__link" href="contact.html">Contact</a>
  <a class="btn btn--primary" href="admissions.html">Apply / Enquire</a>
"""

for filename in ['website/index.html', 'website/about.html', 'website/contact.html']:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the drawer section and replace its links
    # The drawer links start after drawer__head and end before drawer__meta
    
    pattern = r'(<button aria-label="Close menu" class="drawer__close" data-drawer-close="" type="button">.*?</button>\s*</div>).*?(<div class="drawer__meta">)'
    
    html = re.sub(pattern, r'\1' + new_drawer_links + r'\2', html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Drawer links updated.")
