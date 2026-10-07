import json
import os
import re

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('website/assets/data/site.json', 'r', encoding='utf-8') as f:
    site = json.load(f)

os.makedirs('website/courses', exist_ok=True)

# NAV/FOOTER shared snippet (relative paths for /courses/ subdir)
NAV = '''<header class="nav" data-nav="">
<div class="nav__inner">
  <a class="nav__brand" href="../index.html" aria-label="Highline Fire and Safety home">
    <img src="../assets/logo.webp" alt="" width="36" height="36">
    <span>Highline <em>Fire &amp; Safety</em></span>
  </a>
  <nav class="nav__links" aria-label="Primary">
    <a href="../index.html">Home</a>
    <a href="../courses.html" aria-current="page" class="is-active">Courses</a>
    <a href="../about.html">About</a>
    <a href="../admissions.html">Admissions</a>
    <a href="../resources.html">Resources</a>
    <a href="../contact.html">Contact</a>
  </nav>
  <a class="btn btn--primary nav__cta" href="../admissions.html">Apply / Enquire</a>
  <button class="nav__burger" data-drawer-open="" aria-label="Open menu" type="button">
    <span></span><span></span><span></span>
  </button>
</div>
</header>'''

FOOTER = '''<footer class="footer">
<div class="footer__card">
  <div class="footer__tile"><img alt="Safety helmet and gloves" class="ph" loading="lazy" src="../assets/img/footer-tile.jpg"/></div>
  <div>
    <div class="footer__brand">
      <img alt="" height="36" src="../assets/logo.webp" width="36"/>
      <b>Highline <em>Fire &amp; Safety</em></b>
    </div>
    <p class="footer__mission">Building safety professionals through structured training and certified education.</p>
  </div>
  <div class="footer__cols">
    <div class="footer__col">
      <p>Quick Links</p>
      <div class="link-grid">
        <a href="../index.html">Home <span aria-hidden="true">→</span></a>
        <a href="../courses.html">Courses <span aria-hidden="true">→</span></a>
        <a href="../about.html">About Us <span aria-hidden="true">→</span></a>
        <a href="../contact.html">Contact <span aria-hidden="true">→</span></a>
        <a href="../admissions.html">Admissions <span aria-hidden="true">→</span></a>
        <a href="../resources.html">Resources <span aria-hidden="true">→</span></a>
      </div>
      <p class="footer__copy">&copy; <span data-year="">2026</span> Highline Fire &amp; Safety Training Institute. All rights reserved.</p>
    </div>
  </div>
</div>
<div class="footer__bar">
  <a href="mailto:highlinefireandsafety@gmail.com">highlinefireandsafety@gmail.com</a>
  <span><a href="tel:+918121118000">+91 812 111 8000</a> · <a href="tel:+919392882152">+91 93928 82152</a></span>
  <span>Beside Geetha Bhavan, opp. Jafri Masjid, Karimnagar, Telangana – 505001</span>
</div>
</footer>
<div class="drawer" data-drawer="" id="site-drawer">
<div aria-label="Site menu" aria-modal="true" class="drawer__panel" role="dialog">
  <div class="drawer__head">
    <span class="drawer__brand"><img alt="" height="34" src="../assets/logo.webp" width="34"/>Highline <em>F&amp;S</em></span>
    <button aria-label="Close menu" class="drawer__close" data-drawer-close="" type="button">✕</button>
  </div>
  <a class="drawer__link" href="../index.html">Home</a>
  <a aria-current="page" class="drawer__link is-active" href="../courses.html">Courses</a>
  <a class="drawer__link" href="../about.html">About</a>
  <a class="drawer__link" href="../admissions.html">Admissions</a>
  <a class="drawer__link" href="../resources.html">Resources</a>
  <a class="drawer__link" href="../contact.html">Contact</a>
  <a class="btn btn--primary" href="../admissions.html">Apply / Enquire</a>
</div>
</div>'''

def list_html(items, style=''):
    if not items:
        return ''
    lis = ''.join(f'<li style="display:flex;gap:10px;align-items:flex-start;line-height:1.6;margin-bottom:10px;"><span style="color:var(--orange);font-weight:700;flex-shrink:0;">→</span> <span>{i}</span></li>' for i in items)
    return f'<ul style="list-style:none;padding:0;margin:0;{style}">{lis}</ul>'

def module_html(topics):
    if not topics:
        return '<p style="color:var(--muted-deep);">Module details available on request.</p>'
    items = ''
    for i, t in enumerate(topics, 1):
        items += f'<div style="display:flex;gap:14px;align-items:flex-start;padding:14px 16px;border:1px solid var(--border);border-radius:8px;margin-bottom:10px;"><span style="background:var(--navy);color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:100px;flex-shrink:0;">{i:02d}</span><span style="font-weight:600;color:var(--navy);line-height:1.5;">{t}</span></div>'
    return items

for course in courses:
    slug = course.get('slug', '')
    title = course.get('title', '')
    desc = course.get('description', '')
    cat = course.get('category', '')
    level = course.get('level', '')
    dur_text = course.get('duration_text', 'Contact us')
    overview = course.get('overview', desc)
    who = course.get('who_is_it_for', '')
    eligibility = course.get('eligibility', [])
    topics = course.get('topics', [])
    lb = course.get('learner_benefits', [])
    eb = course.get('employer_benefits', [])
    roles = course.get('jobRoles', [])
    progression = course.get('progression', [])
    suitable = course.get('suitableFor', '')
    modes = course.get('deliveryMode', [])
    cert = course.get('certification', 'Contact us')
    assessment = course.get('assessment', [])
    work_areas = course.get('workAreas', [])

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} | Highline Fire &amp; Safety Training Institute</title>
  <meta name="description" content="{desc[:155]}">
  <link rel="canonical" href="{site.get('website','')}/courses/{slug}.html">
  <link rel="stylesheet" href="../assets/css/styles.css">
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"Course",
    "name":"{title}",
    "description":"{desc[:200]}",
    "provider":{{"@type":"Organization","name":"{site.get('name','')}","url":"{site.get('website','')}"}},
    "hasCourseInstance":{{"@type":"CourseInstance","courseMode":"{', '.join(modes)}"}}
  }}
  </script>
  <style>
    .course-detail-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 60px; align-items: start; }}
    @media (max-width: 900px) {{ .course-detail-grid {{ grid-template-columns: 1fr; }} }}
    .sidebar-card {{ background: var(--white); border: 1px solid var(--border); border-radius: 16px; padding: 28px; position: sticky; top: 110px; box-shadow: 0 4px 24px rgba(11,60,109,0.07); }}
    .sidebar-row {{ display: flex; flex-direction: column; gap: 4px; padding: 14px 0; border-bottom: 1px solid var(--border); }}
    .sidebar-row:last-of-type {{ border-bottom: none; }}
    .sidebar-label {{ font-size: 11px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }}
    .sidebar-value {{ font-size: 15px; font-weight: 600; color: var(--navy); line-height: 1.5; }}
    .section-block {{ margin-bottom: 48px; }}
    .section-block h2 {{ font-size: 24px; font-weight: 800; color: var(--navy); margin-bottom: 18px; padding-bottom: 12px; border-bottom: 2px solid var(--mist); }}
    .breadcrumb {{ font-size: 13px; color: var(--muted); margin-bottom: 16px; }}
    .breadcrumb a {{ color: var(--teal); text-decoration: none; }}
    .mode-pill {{ display: inline-flex; align-items: center; gap: 6px; background: var(--mist); color: var(--navy); font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 100px; }}
  </style>
</head>
<body>

{NAV}

<!-- HERO -->
<header class="hero hero--inner" style="min-height:45vh; padding-top:130px; padding-bottom:70px; background: linear-gradient(135deg, var(--navy) 0%, #1a5fa8 100%);">
  <div class="hero__scrim" style="background:linear-gradient(to right, rgba(11,60,109,0.7) 0%, transparent 100%);"></div>
  <div class="hero__content" style="padding-top:0; max-width:900px; margin:0 auto;">
    <p class="breadcrumb" style="color:rgba(255,255,255,0.7); margin-bottom:12px;">
      <a href="../courses.html" style="color:rgba(255,255,255,0.8);">← All Courses</a> &nbsp;/&nbsp; {cat}
    </p>
    <span style="display:inline-flex; background:rgba(255,255,255,0.12); color:#fff; font-size:12px; font-weight:700; padding:6px 16px; border-radius:100px; margin-bottom:20px; text-transform:uppercase; letter-spacing:0.06em;">{level}</span>
    <h1 class="hero__title" style="margin-bottom:18px; font-size:clamp(28px,5vw,48px);">{title}</h1>
    <p style="font-size:17px; line-height:1.7; color:rgba(255,255,255,0.88); max-width:700px;">{desc}</p>
    <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:28px;">
      <a href="../admissions.html" class="btn btn--primary" style="padding:14px 28px; font-size:15px;">Apply / Enquire Now →</a>
      <a href="../contact.html" class="btn btn--secondary btn--white" style="padding:14px 28px; font-size:15px; color:#fff; border-color:rgba(255,255,255,0.5);">Ask a Question</a>
    </div>
  </div>
</header>

<main id="main">
<section class="section" style="padding-top:60px; padding-bottom:100px;">
<div class="course-detail-grid">

  <!-- LEFT COLUMN -->
  <div>

    <div class="section-block">
      <h2>Course Overview</h2>
      <p style="color:var(--muted-deep); line-height:1.8; font-size:16px;">{overview}</p>
    </div>

    {'<div class="section-block"><h2>Who Is It For?</h2><p style="color:var(--muted-deep);line-height:1.8;font-size:16px;">' + who + '</p></div>' if who else ''}

    {'<div class="section-block"><h2>Benefits to Learners</h2>' + list_html(lb) + '</div>' if lb else ''}

    {'<div class="section-block"><h2>Benefits to Employers</h2>' + list_html(eb) + '</div>' if eb else ''}

    <div class="section-block">
      <h2>Course Content</h2>
      {module_html(topics)}
    </div>

    {'<div class="section-block"><h2>Assessment</h2>' + list_html(assessment) + '</div>' if assessment else ''}

    {'<div class="section-block"><h2>Career Opportunities</h2>' + list_html(roles) + '</div>' if roles else ''}

    {'<div class="section-block"><h2>Progression</h2>' + list_html(progression) + '</div>' if progression else ''}

    {'<div class="section-block"><h2>Suitable For</h2><p style="color:var(--muted-deep);line-height:1.8;font-size:16px;">' + suitable + '</p></div>' if suitable else ''}

  </div>

  <!-- RIGHT SIDEBAR -->
  <aside>
    <div class="sidebar-card">
      <div class="sidebar-row">
        <span class="sidebar-label">Duration</span>
        <span class="sidebar-value">{dur_text}</span>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Level</span>
        <span class="sidebar-value">{level}</span>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Category</span>
        <span class="sidebar-value">{cat}</span>
      </div>
      {'<div class="sidebar-row"><span class="sidebar-label">Eligibility</span><span class="sidebar-value">' + '<br>'.join(eligibility) + '</span></div>' if eligibility else ''}
      <div class="sidebar-row">
        <span class="sidebar-label">Training Mode</span>
        <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:6px;">
          {''.join(f'<span class="mode-pill">{m}</span>' for m in modes)}
        </div>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Course Fee</span>
        <span class="sidebar-value">Contact us for current fee structures</span>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Certification</span>
        <span class="sidebar-value" style="font-size:13px; line-height:1.5;">{cert}</span>
      </div>
      <a href="../admissions.html" class="btn btn--primary btn--block" style="justify-content:center;padding:16px;margin-top:20px;width:100%;text-align:center;">Apply / Enquire Now →</a>
      <a href="../contact.html" class="btn btn--secondary btn--block" style="justify-content:center;padding:14px;margin-top:10px;width:100%;text-align:center;">Contact Admissions</a>
    </div>
  </aside>

</div>
</section>
</main>

{FOOTER}

<script defer src="../assets/js/site.js"></script>
<a aria-label="Chat on WhatsApp" class="float-wa" href="https://wa.me/919392882152" rel="noopener" target="_blank">
  <svg fill="currentColor" height="24" viewBox="0 0 24 24" width="24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.81 11.81 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.88 11.88 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.82 11.82 0 0 0-3.48-8.413Z"></path></svg>
</a>
</body>
</html>'''

    out = f'website/courses/{slug}.html'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'  Generated: {out}')

print(f'\nDone — {len(courses)} course pages generated in website/courses/')
