import re

with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved, IOSH and Bharat Sevak Samaj authorized', 'Professional', html)

# "internationally accredited safety programs"
html = re.sub(r'internationally accredited safety programs', 'practical safety programs', html)

# "Placements ->" SVG
html = re.sub(r'<text fill="#14181D" font-size="12" font-weight="700" text-anchor="end" x="294" y="16">Placements .*?</text>', '', html)
html = re.sub(r'path d="M 50 110 Q 150 50 250 120" stroke="#F57C00" stroke-width="3" fill="none"', 'path d="M 50 110 Q 150 50 250 120" stroke="#F57C00" stroke-width="3" fill="none" class="clay"', html)

# "From first certificate to international accreditation — structured fire & safety courses with practical drills and placement support."
html = re.sub(r'international accreditation — structured fire &amp; safety courses with practical drills and placement support', 'advanced diplomas — structured fire &amp; safety courses with practical drills', html)
html = re.sub(r'international accreditation', 'advanced diplomas', html)
html = re.sub(r'and placement support', '', html)

# IOSH course description on index page
html = re.sub(r'Internationally accredited managerial safety course, delivered by an IOSH-approved training provider\.', 'Internationally recognized managerial safety course.', html)
html = re.sub(r'Internationally Accredited', 'Internationally Recognized', html)

# Experienced, accredited instructors -> Experienced instructors
html = re.sub(r'Experienced, accredited instructors', 'Experienced instructors', html)

# Mock drills, placement drives -> Mock drills, training sessions
html = re.sub(r'Mock drills, placement drives, and certification exam windows', 'Mock drills, training sessions, and practical exams', html)

# Campus Placement Drive -> Upcoming Batch Orientations
html = re.sub(r'Campus Placement Drive', 'Upcoming Batch Orientations', html)

# Train with accredited instructors -> Train with experienced instructors
html = re.sub(r'train with accredited instructors', 'train with experienced instructors', html)

# Full DFS or ADHSE diploma with practical drills and placement support.
html = re.sub(r'Full DFS or ADHSE diploma with practical drills and placement support\.', 'Full DFS or ADHSE diploma with practical drills.', html)
html = re.sub(r'<span>Placement assistance</span>', '', html)
html = re.sub(r'<span>IOSH MS accredited course</span>', '<span>IOSH MS training</span>', html)
html = re.sub(r'<span>Interview &amp; placement preparation</span>', '', html)

# Testimonials section
html = re.sub(r'<!-- ===+ TESTIMONIALS === -->.*?(?=<!-- ===+ BLOG === -->)', '<!-- === TESTIMONIALS REMOVED === -->\n', html, flags=re.DOTALL)

# "The Importance of Accredited Safety Training Programs"
html = re.sub(r'The Importance of Accredited Safety Training Programs', 'The Importance of Practical Safety Training Programs', html)

# Free counselling session
html = re.sub(r'free counselling session', 'admissions consultation', html)

# Does Highline provide placement assistance?
html = re.sub(r'<span class="acc__n">04</span><span class="acc__q">Does Highline provide placement assistance\?</span>.*?(?=<span class="acc__head">)', '', html, flags=re.DOTALL)

# "Our team answers every question about courses, eligibility, and placements."
html = re.sub(r'Our team answers every question about courses, eligibility, and placements\.', 'Our team answers every question about courses and eligibility.', html)

# trust metrics: 100% Practical Focus -> 
html = re.sub(r'<div class="trust-metric"><b class="counter" data-suffix="%" data-target="100">0%</b><span>Practical Focus</span></div>', '<div class="trust-metric"><b class="counter" data-suffix="" data-target="21">0</b><span>Hour IOSH Program</span></div>', html)
html = re.sub(r'<div class="trust-metric"><b class="counter" data-suffix="" data-target="3">0</b><span>Global Accreditations</span></div>', '<div class="trust-metric"><b>3+</b><span>Learning Pathways</span></div>', html)

# Remove window.HL_TESTIMONIALS completely
html = re.sub(r'window\.HL_TESTIMONIALS\s*=\s*\[.*?\];', '', html, flags=re.DOTALL)

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed index.html')
