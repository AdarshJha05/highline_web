import re

with open('website/contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'Internationally accredited fire and safety training institute', 'Professional fire and safety training institute', html)
html = re.sub(r'Approved EOSH and IOSH training provider', 'Professional training provider', html)

# Chips
html = re.sub(r'<span class="chip">🚀 Accredited Trainers</span>', '<span class="chip">🚀 Experienced Trainers</span>', html)
html = re.sub(r'<span class="chip">✨ Placement Assistance</span>', '<span class="chip">✨ Modern Facilities</span>', html)

# FAQs
html = re.sub(r'free counselling', 'consultation', html)
html = re.sub(r"Highline is an EOSH Approved Training Provider, IOSH Approved Training Provider 5380, and Bharat Sevak Samaj \(TEL/9473\) authorized institute\.", "Highline delivers EOSH programmes, is an IOSH Approved Training Provider (No. 5380), and offers Advanced Diplomas awarded under Bharat Sevak Samaj.", html)
html = re.sub(r"\{q:'Does the institute provide placement assistance\?', a:'Yes — resume preparation, interview practice, and campus placement drives with industry partners are part of every diploma and international track\.'\},", "", html)

with open('website/contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed contact.html')
