import re

with open('website/admissions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta description
html = re.sub(r'EOSH Approved Training Provider, IOSH Approved and Bharat Sevak Samaj authorized', 'Admissions for professional safety programs', html)
html = re.sub(r'Internationally accredited fire and safety training institute', 'Professional fire and safety training institute', html)
html = re.sub(r'Approved EOSH and IOSH training provider', 'Professional training provider', html)

# "globally accredited safety programs. Flexible batch timings and installment plans available."
html = re.sub(r'globally accredited safety programs\. Flexible batch timings and installment plans available\.', 'professional safety programs.', html)

# Step 2: Free Counselling
html = re.sub(r'<h3 class="h3" style="font-size: 18px; font-weight: 800; color: var\(--navy\); margin-bottom: 8px;">Free Counselling</h3>', '<h3 class="h3" style="font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px;">Speak with our admissions team</h3>', html)

# Step 3: Confirm & Pay
html = re.sub(r'<h3 class="h3" style="font-size: 18px; font-weight: 800; color: var\(--navy\); margin-bottom: 8px;">Confirm &amp; Pay</h3>', '<h3 class="h3" style="font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px;">Confirm your course and fee details</h3>', html)
html = re.sub(r'Finalize your registration by paying the course fee\. Installment options are available for diploma tracks\.', 'Confirm your course details with the institute.', html)

# Installments wording
html = re.sub(r'<p style="color: var\(--navy\); font-size: 15px; line-height: 1\.5; margin: 0;"><strong>Flexible Installments:</strong> Available specifically for Long-term Diploma and International Certification tracks\.</p>', '', html)

# Submit button text
html = re.sub(r'Proceed to Enquiry', 'Submit Application', html)

# Add fallback helper text for mailto
helper_text = '<p style="text-align:center; font-size:13px; color:var(--muted-deep); margin-top:16px;">This opens your email app with your details filled in. If nothing opens, email <a href="mailto:highlinefireandsafety@gmail.com">highlinefireandsafety@gmail.com</a> or call 8121118000.</p>'
html = re.sub(r'(<button class="btn btn--solid".*?</button>)', r'\1\n' + helper_text, html)

with open('website/admissions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed admissions.html')
