import glob
import re
import os

html_files = glob.glob('website/*.html')

new_links_root = '''<p>Quick Links</p>
<div class="link-grid">
<a href="index.html">Home <span aria-hidden="true">&#8599;</span></a>
<a href="courses.html">Courses <span aria-hidden="true">&#8599;</span></a>
<a href="about.html">About <span aria-hidden="true">&#8599;</span></a>
<a href="admissions.html">Admissions <span aria-hidden="true">&#8599;</span></a>
<a href="resources.html">Resources <span aria-hidden="true">&#8599;</span></a>
<a href="contact.html">Contact <span aria-hidden="true">&#8599;</span></a>
</div>'''

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Regex to find <p>Quick Links</p> and the following <div class="link-grid">...</div>
    pattern = r'<p>Quick Links</p>\s*<div class="link-grid">.*?</div>'
    new_html = re.sub(pattern, new_links_root, html, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Updated root HTML files.")

# Now for generate_pages.py
gen_path = 'tools/generate_pages.py'
if os.path.exists(gen_path):
    with open(gen_path, 'r', encoding='utf-8') as f:
        gen = f.read()

    new_links_sub = '''<p>Quick Links</p>
        <div class="link-grid">
          <a href="../index.html">Home <span aria-hidden="true">&#8599;</span></a>
          <a href="../courses.html">Courses <span aria-hidden="true">&#8599;</span></a>
          <a href="../about.html">About <span aria-hidden="true">&#8599;</span></a>
          <a href="../admissions.html">Admissions <span aria-hidden="true">&#8599;</span></a>
          <a href="../resources.html">Resources <span aria-hidden="true">&#8599;</span></a>
          <a href="../contact.html">Contact <span aria-hidden="true">&#8599;</span></a>
        </div>'''

    pattern = r'<p>Quick Links</p>\s*<div class="link-grid">.*?</div>'
    new_gen = re.sub(pattern, new_links_sub, gen, flags=re.DOTALL)
    
    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(new_gen)
    print("Updated generate_pages.py")
