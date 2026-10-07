import glob
import os

# 1. Update index.html specifically for "Talk to an Advisor"
index_path = 'website/index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<a class="btn btn--secondary btn--white" href="admissions.html">Talk to an Advisor</a>',
                        '<a class="btn btn--secondary btn--white" href="contact.html">Talk to an Advisor</a>')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html 'Talk to an Advisor' link.")

# 2. Update all HTML files for "Apply / Enquire" -> "Apply Now &#8594;"
html_files = glob.glob('website/*.html') + glob.glob('website/courses/*.html')
count = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '>Apply / Enquire</a>' in html:
        html = html.replace('>Apply / Enquire</a>', '>Apply Now &#8594;</a>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
print(f"Updated header CTA on {count} HTML pages.")

# 3. Update generate_pages.py
gen_path = 'tools/generate_pages.py'
if os.path.exists(gen_path):
    with open(gen_path, 'r', encoding='utf-8') as f:
        gen = f.read()
    if '>Apply / Enquire</a>' in gen:
        gen = gen.replace('>Apply / Enquire</a>', '>Apply Now &#8594;</a>')
        with open(gen_path, 'w', encoding='utf-8') as f:
            f.write(gen)
        print("Updated tools/generate_pages.py generator template.")
