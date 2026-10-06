import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove avatar spans: <span class="av ...>...</span>
    content = re.sub(r'<span class="av[^>]*>.*?</span>', '', content)
    # The container might be empty now: <span class="avs"></span>
    content = re.sub(r'<span class="avs">\s*</span>', '', content)

    if 'index.html' in filepath:
        # Hide the events section containing the stale date
        content = re.sub(r'(<section class="section events"[^>]*>)', r'\1\n<!-- [TO BE SUPPLIED BY HIGHLINE] -->\n<div style="display:none;">', content)
        content = re.sub(r'(</section>\s*<section class="band" id="cta-yard")', r'</div>\n\1', content)

        # Remove "Indicative fees" text
        content = re.sub(r'<p class="lead"[^>]*>Indicative fees.*?</p>', '<p class="lead" style="max-width:560px">Contact us for current fee structures.</p>', content)
        
        # Remove specific prices (e.g., ₹15,000)
        content = re.sub(r'<div class="price__val">.*?</div>', '<div class="price__val">[Fee on request]</div>', content, flags=re.DOTALL)

        # Hide testimonials section
        content = re.sub(r'(<section class="section section--rel" data-testi[^>]*>)', r'\1\n<!-- [TO BE SUPPLIED BY HIGHLINE] -->\n<div style="display:none;">', content)
        content = re.sub(r'(</section>\s*<section class="section--open" id="blog")', r'</div>\n\1', content)

        # Remove the 96% placement stat from the hero
        content = re.sub(r'<span class="stat">\s*<b>96%</b>\s*<span>Placement support</span>\s*</span>', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in ['index.html', 'about.html', 'contact.html']:
    path = os.path.join('website', filename)
    if os.path.exists(path):
        process_file(path)
        print(f"Processed {filename}")
