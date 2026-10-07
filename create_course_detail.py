import os

with open('website/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

header_end = about_html.find('<!-- ==================== /HEADER ==================== -->') + len('<!-- ==================== /HEADER ==================== -->')
header_html = about_html[:header_end]
footer_start = about_html.find('<!-- ============================================================= FOOTER === -->')
footer_html = about_html[footer_start:]

# Remove active state from About
header_html = header_html.replace('class="nav__link is-active" aria-current="page" href="about.html"', 'class="nav__link" href="about.html"')
footer_html = footer_html.replace('class="drawer__link is-active" aria-current="page" href="about.html"', 'class="drawer__link" href="about.html"')

# We will just leave the active state on courses.html (if we can), but they are on course.html so it might not match perfectly.
header_html = header_html.replace('class="nav__link" href="courses.html"', 'class="nav__link is-active" aria-current="page" href="courses.html"')

course_body = """
  <header class="hero hero--inner">
    <img alt="Training session" class="ph" fetchpriority="high" src="assets/img/hero-contact.jpg" style="object-fit: cover; opacity: 0.4;" />
    <div class="hero__scrim"></div>
    <div class="hero__content" id="course-hero">
      <span class="eyebrow eyebrow--light" id="course-category">Loading...</span>
      <h1 class="hero__title" id="course-title" style="max-width: 1000px;">Loading Course Details</h1>
      <div class="hero__blurb">
        <p id="course-desc">Please wait while we retrieve the syllabus and training information.</p>
      </div>
      <div class="hero__actions" style="margin-top: 32px;">
        <a href="contact.html" class="btn btn--primary">Enquire Now</a>
        <a href="courses.html" class="btn btn--secondary btn--white">Back to Catalogue</a>
      </div>
    </div>
  </header>

  <main id="main">
    <section class="section" style="padding-top: 80px; padding-bottom: 80px;">
      <div class="grid-2" style="gap: 60px;">
        
        <div>
          <h2 class="h2" style="margin-bottom: 24px;">Course Overview</h2>
          <p class="lead" id="course-overview" style="margin-bottom: 32px;">This internationally recognised qualification equips candidates with the practical skills and theoretical knowledge required to manage workplace risks effectively.</p>
          
          <h3 class="h3" style="font-size: 22px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Who is this for?</h3>
          <p style="color: var(--muted-deep); line-height: 1.6; margin-bottom: 32px;">Ideal for managers, supervisors, and safety practitioners seeking to enhance their professional competence and ensure organisational compliance with global standards.</p>
          
          <h3 class="h3" style="font-size: 22px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Training Methodology</h3>
          <p style="color: var(--muted-deep); line-height: 1.6;">Delivered through a blend of classroom instruction, interactive group exercises, and practical drills on our fully equipped training yard.</p>
        </div>
        
        <div>
          <div class="panel panel--center" style="background: var(--mist); border: 1px solid var(--border); box-shadow: none; text-align: left; padding: 40px;">
            <h3 class="h3" style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border-mid);">Key Information</h3>
            
            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div>
                <span style="display: block; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted);">Qualification Level</span>
                <span style="font-size: 16px; font-weight: 600; color: var(--navy);" id="course-level">Loading...</span>
              </div>
              <div>
                <span style="display: block; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted);">Duration</span>
                <span style="font-size: 16px; font-weight: 600; color: var(--navy);">Contact for Schedule</span>
              </div>
              <div>
                <span style="display: block; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted);">Certification</span>
                <span style="font-size: 16px; font-weight: 600; color: var(--navy);">EOSH UK Approved</span>
              </div>
            </div>
            
            <a href="contact.html" class="btn btn--primary" style="width: 100%; margin-top: 32px;">Request Syllabus & Fees</a>
          </div>
        </div>

      </div>
    </section>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const urlParams = new URLSearchParams(window.location.search);
      const courseId = urlParams.get('id');

      if (!courseId) {
        window.location.href = 'courses.html';
        return;
      }

      fetch('assets/data/courses.json')
        .then(response => response.json())
        .then(data => {
          const course = data.find(c => c.id === courseId);
          
          if (!course) {
            document.getElementById('course-title').innerText = 'Course Not Found';
            document.getElementById('course-desc').innerText = 'We could not locate this qualification. It may have been updated or removed.';
            return;
          }

          document.title = course.title + ' - Highline Fire & Safety';
          document.getElementById('course-category').innerText = course.category;
          document.getElementById('course-title').innerText = course.title;
          document.getElementById('course-desc').innerText = course.description;
          document.getElementById('course-level').innerText = course.level;
        })
        .catch(err => {
          console.error(err);
        });
    });
  </script>
"""

with open('website/course.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '\n' + course_body + '\n' + footer_html)

print("course.html generated.")
