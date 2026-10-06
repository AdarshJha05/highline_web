import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Footer accreditations
    content = re.sub(r'ISO 9001:2015 Certified.*?IBSP Approved\.', 'EOSH Approved Training Provider &middot; IOSH Approved Training Provider 5380 &middot; Bharat Sevak Samaj (TEL/9473)', content)
    
    # 2. Meta Descriptions
    content = re.sub(r'ISO 9001:2015 certified, IBSP approved, IOSH accredited\.', 'EOSH Approved Training Provider, IOSH Approved and Bharat Sevak Samaj authorized.', content)
    
    # 3. about.html specific stats
    content = re.sub(r'<span><b>96%</b><span>Placement support</span></span>', '', content)
    content = re.sub(r'<span><b data-count="500" data-suffix="\+">500\+</b><small>Students trained</small></span>', '', content)
    content = re.sub(r'<p class="ach__note">Milestone timeline indicative.*?institute\.</p>', '<p class="ach__note">Milestone timeline details to be confirmed with the institute.</p>', content)
    content = re.sub(r'<span class="chip tl">ISO 9001:2015 Certified</span>', '<span class="chip tl">EOSH Approved</span>', content)
    
    # FAQ Accreditation
    content = re.sub(r'Highline is ISO 9001:2015 certified, IBSP approved, and an IOSH-accredited training provider, with NEBOSH IGC preparation offered on the international track\.', 'Highline is an EOSH Approved Training Provider, IOSH Approved Training Provider 5380, and Bharat Sevak Samaj (TEL/9473) authorized institute.', content)

    # 4. index.html specific stats and artifacts
    content = re.sub(r'<span><b>500\+ Students Trained</b><small>Certified fire &amp; safety batches</small></span>', '<!-- Stats hidden until verified -->', content)
    content = re.sub(r'<div class="hero__accred">ISO 9001:2015.*?IOSH</div>', '<div class="hero__accred">EOSH Approved &middot; IOSH 5380 &middot; BSS</div>', content)
    content = re.sub(r'<span class="chip">500\+ Students Trained</span>', '', content)
    
    # 5. Stale Dates
    content = re.sub(r'<span><small>Starts</small><b>September 2026</b></span>', '<!-- [BATCH DATE TO BE SUPPLIED] -->', content)
    
    # 6. Missed Avatars
    content = re.sub(r'<span class="avs avs--on-blue">.*?</span>', '', content, flags=re.DOTALL)
    
    # 7. Hide Testimonials UI completely (buttons and JS object references)
    content = re.sub(r'<button class="testi__dot".*?</button>', '', content)
    
    # We will remove the invented JS objects from index.html
    content = re.sub(r'\{name:\'Dasari Balachander\'.*?\},', '', content, flags=re.DOTALL)
    content = re.sub(r'\{name:\'Samanthula Sampath\'.*?\},', '', content, flags=re.DOTALL)
    content = re.sub(r'\{name:\'Nyalam Prashanth\'.*?\},', '', content, flags=re.DOTALL)
    content = re.sub(r'\{name:\'Nyalam Rajkumar\'.*?\},', '', content, flags=re.DOTALL)
    content = re.sub(r'\{name:\'Mohammad Shamroz\'.*?\}', '', content, flags=re.DOTALL)

    # Clean up empty JS arrays if they happen
    content = re.sub(r'const testimonials = \[\s*\];', 'const testimonials = [];', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in ['website/index.html', 'website/about.html', 'website/contact.html']:
    if os.path.exists(filename):
        clean_file(filename)
        print(f"Cleaned {filename}")
