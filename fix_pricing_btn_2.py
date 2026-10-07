import re

with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace ANY "Choose This Track" button
html = re.sub(
    r'<a class="btn [^"]*" href="contact\.html">Choose This Track.*?</a>',
    r'<a class="btn btn--primary btn--block" href="contact.html">Enquire Now <span aria-hidden="true" style="margin-left:8px;">→</span></a>',
    html, flags=re.DOTALL
)

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
