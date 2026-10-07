import os
from bs4 import BeautifulSoup

# We will use admissions.html as the base template to get header/footer
with open('website/admissions.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Extract header
header_end = base_html.find('<!-- ==================== /HEADER ==================== -->') + len('<!-- ==================== /HEADER ==================== -->')
header_html = base_html[:header_end]

# Extract footer
footer_start = base_html.find('<!-- ============================================================ FOOTER === -->')
footer_html = base_html[footer_start:]

# Fix active states in header for resources.html
header_html = header_html.replace('class="nav__link is-active" aria-current="page" href="admissions.html"', 'class="nav__link" href="admissions.html"')
header_html = header_html.replace('class="nav__link" href="resources.html"', 'class="nav__link is-active" aria-current="page" href="resources.html"')

footer_html = footer_html.replace('class="drawer__link is-active" aria-current="page" href="admissions.html"', 'class="drawer__link" href="admissions.html"')
footer_html = footer_html.replace('class="drawer__link" href="resources.html"', 'class="drawer__link is-active" aria-current="page" href="resources.html"')

resources_body = """
  <!-- ============================================================== HERO === -->
  <header class="hero hero--inner">
    <img alt="Collection of safety manuals and hard hats" class="ph" fetchpriority="high" src="assets/img/hero-about.jpg" style="object-fit: cover; opacity: 0.25;" />
    <div class="hero__scrim"></div>
    <div class="hero__content">
      <span class="eyebrow eyebrow--light">Highline Knowledge Hub</span>
      <h1 class="hero__title">Safety Resources</h1>
      <div class="hero__blurb">
        <p>Explore expert articles, comprehensive safety guides, toolbox talks, and downloadable materials to elevate your HSE knowledge.</p>
      </div>
    </div>
  </header>

  <main id="main">
    
    <!-- ================================================= GUIDES & BLOG === -->
    <section class="section bg-light" style="padding-top: 80px; padding-bottom: 60px;">
      <div class="grid-2" style="gap: 40px;">
        
        <!-- Safety Guides -->
        <div class="panel" style="padding: 40px; box-shadow: var(--sh-card-soft);">
          <span class="eyebrow">Deep Dives</span>
          <h2 class="h2" style="font-size: 28px; margin-bottom: 24px;">Safety Guides</h2>
          <p style="color: var(--muted-deep); margin-bottom: 32px; line-height: 1.6;">Comprehensive manuals covering industry compliance, risk assessment methodologies, and best practices for specific hazardous environments.</p>
          
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📘</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">NEBOSH Exam Prep Guide</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">Strategies and study plans for passing the IGC.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📘</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">Fire Safety Compliance 101</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">A breakdown of corporate fire safety standards.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
          </div>
        </div>

        <!-- Blog -->
        <div class="panel" style="padding: 40px; box-shadow: var(--sh-card-soft);">
          <span class="eyebrow">Latest News</span>
          <h2 class="h2" style="font-size: 28px; margin-bottom: 24px;">Our Blog</h2>
          <p style="color: var(--muted-deep); margin-bottom: 32px; line-height: 1.6;">Stay updated with the latest trends in Health, Safety, and Environment (HSE), along with Highline campus announcements and alumni success stories.</p>
          
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📰</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">Why EOSH Certification Matters</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">How UK accreditations elevate your global career.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📰</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">Recent Placement Drive Success</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">Highline graduates secure roles in top Gulf firms.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- ================================================= TOOLBOX & DOWNLOADS === -->
    <section class="section" style="padding-top: 60px; padding-bottom: 80px;">
      <div class="grid-2" style="gap: 40px;">
        
        <!-- Toolbox Talks -->
        <div class="panel" style="padding: 40px; box-shadow: var(--sh-card-soft);">
          <span class="eyebrow">Briefings</span>
          <h2 class="h2" style="font-size: 28px; margin-bottom: 24px;">Toolbox Talks</h2>
          <p style="color: var(--muted-deep); margin-bottom: 32px; line-height: 1.6;">Short, impactful 5-10 minute safety briefings designed for site supervisors to conduct daily risk awareness meetings with their teams.</p>
          
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">🎙️</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">Working at Heights Safely</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">Fall protection and harness inspection.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: border-color 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: var(--mist); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">🎙️</div>
                <div>
                  <h4 style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">Electrical Hazards</h4>
                  <p style="font-size: 13px; color: var(--muted); margin: 0;">Lockout/tagout procedures for live sites.</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </a>
          </div>
        </div>

        <!-- Downloadable Resources -->
        <div class="panel" style="padding: 40px; box-shadow: var(--sh-card-soft); background: var(--navy); color: #fff;">
          <span class="eyebrow eyebrow--light">Templates & Posters</span>
          <h2 class="h2" style="font-size: 28px; margin-bottom: 24px; color: #fff;">Downloadable Resources</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 32px; line-height: 1.6;">Access our library of printable safety posters, inspection checklists, and hazard identification templates for your workplace.</p>
          
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); text-decoration: none; color: inherit; transition: background 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📄</div>
                <div>
                  <h4 style="font-weight: 700; margin-bottom: 4px; color: #fff;">Daily Site Inspection Checklist</h4>
                  <p style="font-size: 13px; color: rgba(255,255,255,0.7); margin: 0;">PDF Document (1.2 MB)</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">↓</span>
            </a>
            <a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); text-decoration: none; color: inherit; transition: background 0.2s;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📄</div>
                <div>
                  <h4 style="font-weight: 700; margin-bottom: 4px; color: #fff;">Emergency Evacuation Poster</h4>
                  <p style="font-size: 13px; color: rgba(255,255,255,0.7); margin: 0;">Printable A3 PDF (3.4 MB)</p>
                </div>
              </div>
              <span aria-hidden="true" style="color: var(--orange);">↓</span>
            </a>
          </div>
          
          <a href="contact.html" class="btn btn--primary" style="margin-top: 32px; width: 100%; justify-content: center;">Request Custom Templates</a>
        </div>

      </div>
    </section>

  </main>
"""

# Assemble new HTML
new_html = header_html + '\n' + resources_body + '\n' + footer_html

# Update SEO meta tags for resources.html
new_html = new_html.replace('<title>Admissions & Fees - Highline Fire & Safety</title>', '<title>Safety Resources Hub - Highline Fire & Safety</title>')
new_html = new_html.replace('content="Apply for internationally accredited safety courses. View our simple admission process, fee structure, and flexible batch timings."', 'content="Explore Highline\'s library of safety guides, toolbox talks, printable posters, checklists, and HSE blog articles."')

with open('website/resources.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("resources.html generated.")
