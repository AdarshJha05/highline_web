import re

with open('website/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved Training Provider, IOSH Approved and Bharat Sevak Samaj authorized', 'Providing comprehensive safety qualifications', html)
html = re.sub(r'Internationally accredited fire and safety training institute', 'Professional fire and safety training institute', html)
html = re.sub(r'Approved EOSH and IOSH training provider', 'Professional training provider', html)

# "with placement support."
html = re.sub(r'with placement support\.', '', html)

# "15+ Industry tie-ups"
html = re.sub(r'<span><b data-count="15" data-suffix="\+">15\+</b><small>Industry tie-ups</small></span>', '<span><b data-count="3" data-suffix="\+">3\+</b><small>Global Recognitions</small></span>', html)

# "placements, and industry partnerships"
html = re.sub(r'certifications, placements, and industry partnerships\.', 'certifications and professional development.', html)

# "placed at regional industrial sites."
html = re.sub(r'with early graduates placed at regional industrial sites\.', 'entering the safety workforce.', html)

# "IOSH-accredited training provider" -> "IOSH Approved Training Provider"
html = re.sub(r'IOSH-accredited', 'IOSH-approved', html)

# "internationally recognized" -> "internationally respected" in timeline
html = re.sub(r'internationally recognized', 'internationally respected', html)

# Trainers section
html = re.sub(r'(<section aria-labelledby="team-h" class="section--open">)', r'<!-- [TRAINERS TO BE SUPPLIED BY HIGHLINE] -->\n<div style="display:none;">\n\1', html)
html = re.sub(r'(</section>\s*<!-- =+ ACHIEVEMENTS =+ -->)', r'</div>\n\1', html)

# Hide facilities specific equipment claims "State-of-the-art classroom and practical yard."
html = re.sub(r'State-of-the-art classroom and practical yard\.', 'Classroom training and practical demonstrations.', html)
html = re.sub(r'Live fire simulators, real-world scaffolding, and fully equipped first-aid mannequins', 'Hands-on practical training environments', html)

with open('website/about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed about.html')
