import re

with open('website/resources.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved Training Provider, IOSH Approved and Bharat Sevak Samaj authorized', 'Resources for professional safety programs', html)
html = re.sub(r'Internationally accredited fire and safety training institute', 'Professional fire and safety training institute', html)
html = re.sub(r'Approved EOSH and IOSH training provider', 'Professional training provider', html)

# NEBOSH Exam Prep Guide -> OSHA Exam Prep Guide (so it doesn't imply NEBOSH centre status)
html = re.sub(r'NEBOSH Exam Prep Guide', 'Safety Exam Prep Guide', html)

# "and alumni success stories."
html = re.sub(r'and alumni success stories\.', '.', html)

# "Recent Placement Drive Success" -> "Campus Training Drill Success"
html = re.sub(r'Recent Placement Drive Success', 'Campus Training Drill Success', html)

with open('website/resources.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed resources.html')
