import re

with open('website/course.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved, IOSH and Bharat Sevak Samaj authorized', 'Professional', html)

# Remove window.HL_TESTIMONIALS completely
html = re.sub(r'window\.HL_TESTIMONIALS\s*=\s*\[.*?\];', '', html, flags=re.DOTALL)

with open('website/course.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed course.html')
