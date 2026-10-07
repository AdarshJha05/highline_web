import os
from bs4 import BeautifulSoup

# We will use about.html as the base template
with open('website/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

header_end = about_html.find('<!-- ==================== /HEADER ==================== -->') + len('<!-- ==================== /HEADER ==================== -->')
header_html = about_html[:header_end]

footer_start = about_html.find('<!-- ============================================================ FOOTER === -->')
footer_html = about_html[footer_start:]

# Fix active states in header for admissions.html
header_html = header_html.replace('class="nav__link is-active" aria-current="page" href="about.html"', 'class="nav__link" href="about.html"')
header_html = header_html.replace('class="nav__link" href="admissions.html"', 'class="nav__link is-active" aria-current="page" href="admissions.html"')

footer_html = footer_html.replace('class="drawer__link is-active" aria-current="page" href="about.html"', 'class="drawer__link" href="about.html"')
footer_html = footer_html.replace('class="drawer__link" href="admissions.html"', 'class="drawer__link is-active" aria-current="page" href="admissions.html"')

admissions_body = """
  <!-- ============================================================== HERO === -->
  <header class="hero hero--inner">
    <img alt="Students registering for safety courses" class="ph" fetchpriority="high" src="assets/img/hero-contact.jpg" style="object-fit: cover; opacity: 0.35;" />
    <div class="hero__scrim"></div>
    <div class="hero__content">
      <span class="eyebrow eyebrow--light">Admissions & Fees</span>
      <h1 class="hero__title">Start Your Training Journey</h1>
      <div class="hero__blurb">
        <p>Register for our globally accredited safety programs. Flexible batch timings and installment plans available.</p>
      </div>
    </div>
  </header>

  <main id="main">
    
    <!-- ================================================= PROCESS & FEES === -->
    <section class="section" style="padding-top: 80px; padding-bottom: 60px;">
      <div class="grid-2" style="gap: 60px; align-items: start;">
        
        <!-- Process -->
        <div>
          <span class="eyebrow">How to Apply</span>
          <h2 class="h2" style="margin-bottom: 32px;">Simple Enrollment Process</h2>
          
          <div style="display: flex; flex-direction: column; gap: 24px;">
            <div style="display: flex; gap: 20px;">
              <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--orange); color: white; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; flex-shrink: 0;">1</div>
              <div>
                <h3 class="h3" style="font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px;">Submit Inquiry</h3>
                <p style="color: var(--muted-deep); line-height: 1.5; font-size: 15px;">Fill out the application form below with your desired course and preferred batch timings.</p>
              </div>
            </div>
            <div style="display: flex; gap: 20px;">
              <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--orange); color: white; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; flex-shrink: 0;">2</div>
              <div>
                <h3 class="h3" style="font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px;">Free Counselling</h3>
                <p style="color: var(--muted-deep); line-height: 1.5; font-size: 15px;">Our admission coordinator will contact you to verify eligibility, confirm seat availability, and discuss career goals.</p>
              </div>
            </div>
            <div style="display: flex; gap: 20px;">
              <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--orange); color: white; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; flex-shrink: 0;">3</div>
              <div>
                <h3 class="h3" style="font-size: 18px; font-weight: 800; color: var(--navy); margin-bottom: 8px;">Confirm & Pay</h3>
                <p style="color: var(--muted-deep); line-height: 1.5; font-size: 15px;">Finalize your registration by paying the course fee. Installment options are available for diploma tracks.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Fees / Panel -->
        <div class="panel panel--center" style="background: var(--mist); border: 1px solid var(--border); box-shadow: none; text-align: left; padding: 40px; border-radius: 24px;">
          <h3 class="h3" style="font-size: 22px; font-weight: 800; color: var(--navy); margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border-mid);">Fee Structure & Eligibility</h3>
          
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 16px;">
            <li style="display: flex; align-items: flex-start; gap: 12px;">
              <span aria-hidden="true" style="color: var(--orange); font-size: 20px;">✓</span>
              <p style="color: var(--navy); font-size: 15px; line-height: 1.5; margin: 0;"><strong>Minimum Eligibility:</strong> 10th Pass or equivalent for most foundational courses.</p>
            </li>
            <li style="display: flex; align-items: flex-start; gap: 12px;">
              <span aria-hidden="true" style="color: var(--orange); font-size: 20px;">✓</span>
              <p style="color: var(--navy); font-size: 15px; line-height: 1.5; margin: 0;"><strong>Transparent Pricing:</strong> All fees are communicated directly during counselling. No hidden charges.</p>
            </li>
            <li style="display: flex; align-items: flex-start; gap: 12px;">
              <span aria-hidden="true" style="color: var(--orange); font-size: 20px;">✓</span>
              <p style="color: var(--navy); font-size: 15px; line-height: 1.5; margin: 0;"><strong>Flexible Installments:</strong> Available specifically for Long-term Diploma and International Certification tracks.</p>
            </li>
          </ul>
        </div>
        
      </div>
    </section>

    <!-- ================================================= APPLICATION FORM === -->
    <section class="inquiry" style="padding-top: 60px; padding-bottom: 120px; background: #fff;">
      <div style="grid-column: 1 / -1; max-width: 800px; margin: 0 auto; width: 100%;">
        <span class="eyebrow" style="text-align: center; display: block;">Apply Now</span>
        <h2 class="h2 h2--44" style="text-align: center; margin-bottom: 40px;">Course Application Form</h2>
        
        <form class="admissions-form" data-mailto="highlinefireandsafety@gmail.com" data-subject="New Admission Application">
          <div class="form-grid form-grid--lg" style="grid-template-columns: 1fr 1fr;">
            <label class="field field--white"><span>Full Name *</span><input autocomplete="name" name="name" placeholder="Legal name (as per ID)" required="" type="text"/></label>
            <label class="field field--white"><span>Email Address *</span><input autocomplete="email" name="email" placeholder="Your email address" required="" type="email"/></label>
            <label class="field field--white"><span>Phone Number *</span><input autocomplete="tel" name="phone" placeholder="Active mobile/WhatsApp number" required="" type="tel"/></label>
            <label class="field field--white"><span>Qualification</span><input name="qualification" placeholder="e.g. 10th, 12th, B.Tech" required="" type="text"/></label>
            
            <label class="field field--white field--full"><span>Select Course *</span>
              <select name="course" required="">
                <option value="">-- Choose your primary course --</option>
                <option>Diploma in Fire Safety</option>
                <option>Advance Diploma in HSE</option>
                <option>IOSH Managing Safely</option>
                <option>NEBOSH IGC</option>
                <option>Diploma in Oil & Gas Safety</option>
                <option>Other (Specify in message)</option>
              </select>
            </label>
            
            <label class="field field--white field--full"><span>Preferred Batch Timing</span>
              <select name="batch" required="">
                <option value="">-- Choose preference --</option>
                <option>Morning (Weekdays)</option>
                <option>Afternoon (Weekdays)</option>
                <option>Weekend Only</option>
                <option>Fast Track</option>
              </select>
            </label>
            
            <label class="field field--white field--full"><span>Additional Questions / Message</span><textarea name="message" placeholder="Any specific questions about fees or syllabus?" rows="4"></textarea></label>
          </div>
          
          <div class="form-foot" style="margin-top: 32px; flex-direction: row; justify-content: space-between; align-items: center;">
            <p style="font-size:13px; max-width:400px; margin:0;">By submitting this form, you agree to be contacted by our admissions team regarding your application.</p>
            <button class="btn btn--primary" type="submit" style="padding: 16px 36px;">Submit Application <span aria-hidden="true" style="margin-left:8px;">→</span></button>
          </div>
          <div class="form-status" style="margin-top: 16px; padding: 16px; border-radius: 8px; display: none; text-align: center; font-weight: 600;"></div>
        </form>
      </div>
    </section>

  </main>
"""

# Update SEO meta tags for admissions.html
new_html = header_html + '\n' + admissions_body + '\n' + footer_html
new_html = new_html.replace('<title>Highline Fire & Safety Training Institute</title>', '<title>Admissions & Fees - Highline Fire & Safety</title>')
new_html = new_html.replace('content="Professional fire and safety training institute"', 'content="Apply for internationally accredited safety courses. View our simple admission process, fee structure, and flexible batch timings."')

with open('website/admissions.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("admissions.html generated.")
