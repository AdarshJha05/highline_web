import os

with open('website/course.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# We keep the <head> and the header/footer, but rewrite <main> and the hero script.
header_end = base_html.find('<!-- ==================== /HEADER ==================== -->') + len('<!-- ==================== /HEADER ==================== -->')
header_html = base_html[:header_end]

footer_start = base_html.find('<!-- ============================================================ FOOTER === -->')
footer_html = base_html[footer_start:]

# New main content for course.html
new_body = """
  <!-- ============================================================== HERO === -->
  <header class="hero hero--inner" style="min-height: 50vh; padding-top: 140px; padding-bottom: 80px;">
    <img id="course-hero-img" alt="Course Training" class="ph" fetchpriority="high" src="assets/img/hero-home.jpg" style="object-fit: cover; opacity: 0.2;" />
    <div class="hero__scrim"></div>
    <div class="hero__content" style="padding-top: 0; max-width: 1000px; margin: 0 auto;">
      <span class="eyebrow eyebrow--light" id="course-accreditation" style="display: inline-flex; background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 100px; margin-bottom: 24px;">Loading...</span>
      <h1 class="hero__title" id="course-title" style="margin-bottom: 24px;">Loading Course Details</h1>
      <div class="hero__blurb" style="max-width: 800px; font-size: 18px; line-height: 1.6; color: rgba(255,255,255,0.85);">
        <p id="course-desc">Please wait while we retrieve the syllabus and training information.</p>
      </div>
    </div>
  </header>

  <main id="main">
    
    <section class="section" style="padding-top: 60px; padding-bottom: 80px;">
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 60px; align-items: start;">
        
        <!-- Left Column: Main Content -->
        <div style="display: flex; flex-direction: column; gap: 48px;">
          
          <!-- Overview & Audience -->
          <div>
            <h2 class="h2" style="font-size: 28px; margin-bottom: 20px;">Course Overview</h2>
            <p id="course-audience" style="color: var(--muted-deep); line-height: 1.7; font-size: 16px;">Loading audience data...</p>
          </div>
          
          <!-- Learning Outcomes -->
          <div>
            <h2 class="h2" style="font-size: 28px; margin-bottom: 20px;">Learning Outcomes</h2>
            <ul id="course-outcomes" style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 16px;">
              <!-- JS injected -->
            </ul>
          </div>
          
          <!-- Modules -->
          <div>
            <h2 class="h2" style="font-size: 28px; margin-bottom: 20px;">Course Modules</h2>
            <div id="course-modules" style="display: flex; flex-direction: column; gap: 12px;">
              <!-- JS injected -->
            </div>
          </div>
          
          <!-- FAQs -->
          <div>
            <h2 class="h2" style="font-size: 28px; margin-bottom: 20px;">Frequently Asked Questions</h2>
            <div id="course-faqs" style="display: flex; flex-direction: column; gap: 16px;">
              <!-- JS injected -->
            </div>
          </div>

        </div>

        <!-- Right Column: Key Info Sidebar -->
        <div class="panel" style="position: sticky; top: 120px; padding: 32px; box-shadow: var(--sh-panel); background: #fff;">
          <h3 class="h3" style="font-size: 22px; margin-bottom: 24px; border-bottom: 1px solid var(--border-mid); padding-bottom: 16px;">Key Information</h3>
          
          <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 32px;">
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Duration</span>
              <p id="course-duration" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Loading...</p>
            </div>
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Delivery Mode & Location</span>
              <p id="course-mode" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Loading...</p>
            </div>
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Eligibility</span>
              <p id="course-eligibility" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Loading...</p>
            </div>
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Course Fee</span>
              <p id="course-fee" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Loading...</p>
            </div>
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Batch Availability</span>
              <p id="course-batch" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Loading...</p>
            </div>
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--faint); text-transform: uppercase; letter-spacing: 0.05em;">Certification</span>
              <p id="course-certification" style="font-weight: 600; color: var(--navy); margin-top: 4px; font-size: 14px; line-height: 1.5;">Loading...</p>
            </div>
          </div>
          
          <a href="admissions.html" class="btn btn--primary btn--block" style="justify-content: center; padding: 16px;">Apply / Enquire Now <span aria-hidden="true" style="margin-left:8px;">→</span></a>
        </div>

      </div>
    </section>

  </main>
"""

# New Script for course.html
new_script = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const courseId = params.get('id');

    if (!courseId) {
      document.getElementById('course-title').textContent = "Course Not Found";
      document.getElementById('course-desc').textContent = "Please return to the courses page to select a valid course.";
      return;
    }

    fetch('assets/data/courses.json')
      .then(response => response.json())
      .then(courses => {
        const course = courses.find(c => c.id === courseId);
        
        if (!course) {
          document.getElementById('course-title').textContent = "Course Not Found";
          document.getElementById('course-desc').textContent = "We could not find the details for this specific course.";
          return;
        }

        // Hero
        document.title = course.title + " | Highline Fire & Safety";
        document.getElementById('course-title').textContent = course.title;
        document.getElementById('course-desc').textContent = course.description;
        document.getElementById('course-accreditation').textContent = "Accreditation: " + course.accreditation;
        if(course.image) {
            document.getElementById('course-hero-img').src = course.image;
            document.getElementById('course-hero-img').style.opacity = '0.4';
        }

        // Main Content
        document.getElementById('course-audience').textContent = course.audience;
        
        const outcomesList = document.getElementById('course-outcomes');
        outcomesList.innerHTML = '';
        course.outcomes.forEach(out => {
          outcomesList.innerHTML += `<li style="display: flex; align-items: flex-start; gap: 12px;">
              <span aria-hidden="true" style="color: var(--orange); font-size: 20px;">✓</span>
              <p style="color: var(--navy); font-size: 16px; line-height: 1.5; margin: 0;">${out}</p>
            </li>`;
        });

        const modulesList = document.getElementById('course-modules');
        modulesList.innerHTML = '';
        course.modules.forEach(mod => {
          modulesList.innerHTML += `<div style="padding: 16px 20px; background: var(--mist); border-radius: 8px; border: 1px solid var(--border); font-weight: 600; color: var(--navy);">
              ${mod}
            </div>`;
        });

        const faqsList = document.getElementById('course-faqs');
        faqsList.innerHTML = '';
        course.faqs.forEach(faq => {
          faqsList.innerHTML += `<div style="padding: 20px; border: 1px solid var(--border); border-radius: 12px; margin-bottom: 12px;">
              <h4 style="font-size: 16px; font-weight: 700; color: var(--navy); margin-bottom: 8px;">${faq.q}</h4>
              <p style="color: var(--muted-deep); font-size: 15px; margin: 0; line-height: 1.5;">${faq.a}</p>
            </div>`;
        });

        // Sidebar
        document.getElementById('course-duration').textContent = course.duration;
        document.getElementById('course-mode').textContent = course.mode + " | " + course.location;
        document.getElementById('course-eligibility').textContent = course.eligibility;
        document.getElementById('course-fee').textContent = course.fee;
        document.getElementById('course-batch').textContent = course.batch_dates;
        document.getElementById('course-certification').textContent = course.certification;
        
      })
      .catch(error => {
        console.error("Error loading course:", error);
        document.getElementById('course-title').textContent = "Data Error";
        document.getElementById('course-desc').textContent = "Failed to load course information.";
      });
  });
</script>
"""

# Assemble course.html
html = header_html + '\n' + new_body + '\n' + footer_html
# Replace old custom scripts at the end with the new one
html = html[:html.rfind('<script>')] + new_script + '</body>\n</html>'

# Add mobile responsive CSS for course grid
resp_css = """
/* Responsive course details grid */
@media (max-width: 1024px) {
  #main > .section > div { grid-template-columns: 1fr !important; gap: 40px !important; }
  .panel { position: static !important; }
}
"""
html = html.replace('</style>', resp_css + '</style>')

with open('website/course.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("course.html updated.")
