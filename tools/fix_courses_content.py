import re

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved, IOSH and Bharat Sevak Samaj authorized', 'Professional', html)

# globally accredited
html = re.sub(r'globally accredited EOSH and IOSH training courses\.', 'professional safety training courses.', html)

# Remove window.HL_TESTIMONIALS completely
html = re.sub(r'window\.HL_TESTIMONIALS\s*=\s*\[.*?\];', '', html, flags=re.DOTALL)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed courses.html')
