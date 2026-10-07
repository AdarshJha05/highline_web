import json
import os

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('website/assets/data/site.json', 'r', encoding='utf-8') as f:
    site = json.load(f)

os.makedirs('website/courses', exist_ok=True)

# ── Exact nav/footer taken directly from index.html structure ──────────────────

def NAV(active='courses'):
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
<nav aria-label="Primary" class="nav">
  <a aria-label="Highline Fire and Safety — Home" class="nav__brand" href="../index.html">
    <span class="nav__mark"><img alt="Highline Logo" height="32" src="../assets/logo.webp" width="32"/></span>
    <span class="nav__word"><b>Highline</b><span>FIRE &amp; SAFETY</span></span>
  </a>
  <div class="nav__links">
    <a class="nav__link{'  is-active" aria-current="page"' if active=='home' else '"'} href="../index.html">Home</a>
    <a class="nav__link{'  is-active" aria-current="page"' if active=='courses' else '"'} href="../courses.html">Courses</a>
    <a class="nav__link{'  is-active" aria-current="page"' if active=='about' else '"'} href="../about.html">About</a>
    <a class="nav__link{'  is-active" aria-current="page"' if active=='admissions' else '"'} href="../admissions.html">Admissions</a>
    <a class="nav__link{'  is-active" aria-current="page"' if active=='resources' else '"'} href="../resources.html">Resources</a>
    <a class="nav__link{'  is-active" aria-current="page"' if active=='contact' else '"'} href="../contact.html">Contact</a>
  </div>
  <div class="nav__right">
    <a class="btn btn--primary" href="../admissions.html">Apply / Enquire</a>
    <button aria-controls="site-drawer" aria-expanded="false" aria-label="Open menu" class="nav__burger" data-burger="" type="button"><span></span><span></span><span></span></button>
  </div>
</nav>
</header>'''

def FOOTER():
    return '''<footer class="footer">
<div class="footer__card">
  <div class="footer__tile"><img alt="Safety helmet and gloves laid out on a workbench" class="ph" loading="lazy" src="../assets/img/footer-tile.jpg"/></div>
  <div>
    <div class="footer__brand">
      <img alt="" height="36" src="../assets/logo.webp" width="36"/>
      <b>Highline <em>Fire &amp; Safety</em></b>
    </div>
    <p class="footer__mission">Building safety professionals through structured training and certified education.</p>
    <form class="newsletter" data-newsletter="">
      <label class="sr-only" for="nl-email">Your email address</label>
      <input autocomplete="email" id="nl-email" placeholder="Your Email Address" required="" type="email"/>
      <button type="submit">Subscribe</button>
    </form>
    <p class="footer__fine">Subscribe to receive admission announcements, batch schedules, and safety training tips from Highline.</p>
    <p class="form-note" data-note="" role="status"></p>
  </div>
  <div class="footer__cols">
    <div class="footer__col">
      <p>Quick Links</p>
      <div class="link-grid">
        <a href="../index.html">Home <span aria-hidden="true">↗</span></a>
        <a href="../courses.html">Courses <span aria-hidden="true">↗</span></a>
        <a href="../about.html">About Us <span aria-hidden="true">↗</span></a>
        <a href="../contact.html">Contact <span aria-hidden="true">↗</span></a>
        <a href="../admissions.html">Admissions <span aria-hidden="true">↗</span></a>
        <a href="../resources.html">Resources <span aria-hidden="true">↗</span></a>
      </div>
      <p>Social Media</p>
      <div class="link-grid">
        <a href="https://www.facebook.com/highlinefireandsafety" rel="noopener" target="_blank">Facebook <span aria-hidden="true">↗</span></a>
        <a href="https://www.instagram.com/highlinefireandsafety" rel="noopener" target="_blank">Instagram <span aria-hidden="true">↗</span></a>
        <a href="https://www.linkedin.com/company/highlinefireandsafety" rel="noopener" target="_blank">LinkedIn <span aria-hidden="true">↗</span></a>
        <a href="https://wa.me/919392882152" rel="noopener" target="_blank">WhatsApp <span aria-hidden="true">↗</span></a>
      </div>
      <p class="footer__copy">&copy; <span data-year="">2026</span> Highline Fire &amp; Safety Training Institute. All rights reserved.</p>
    </div>
  </div>
</div>
<div aria-hidden="true" class="footer__wordmark"><div>HighLine</div></div>
<div class="footer__bar">
  <a href="mailto:highlinefireandsafety@gmail.com">highlinefireandsafety@gmail.com</a>
  <span><a href="tel:+918121118000">+91 812 111 8000</a> · <a href="tel:+919392882152">+91 93928 82152</a></span>
  <span>Beside Geetha Bhavan, opp. Jafri Masjid, Karimnagar, Telangana – 505001</span>
</div>
</footer>
<!-- MOBILE DRAWER -->
<div class="drawer" data-drawer="" id="site-drawer">
<div aria-label="Site menu" aria-modal="true" class="drawer__panel" role="dialog">
  <div class="drawer__head">
    <span class="drawer__brand"><img alt="" height="34" src="../assets/logo.webp" width="34"/>Highline <em>F&amp;S</em></span>
    <button aria-label="Close menu" class="drawer__close" data-drawer-close="" type="button">&times;</button>
  </div>
  <a class="drawer__link" href="../index.html">Home</a>
  <a aria-current="page" class="drawer__link is-active" href="../courses.html">Courses</a>
  <a class="drawer__link" href="../about.html">About</a>
  <a class="drawer__link" href="../admissions.html">Admissions</a>
  <a class="drawer__link" href="../resources.html">Resources</a>
  <a class="drawer__link" href="../contact.html">Contact</a>
  <a class="btn btn--primary" href="../admissions.html">Apply / Enquire</a>
  <div class="drawer__meta">
    <a href="tel:+918121118000">+91 812 111 8000</a><br/>
    <a href="mailto:highlinefireandsafety@gmail.com">highlinefireandsafety@gmail.com</a><br/>
    Beside Geetha Bhavan, Karimnagar – 505001
  </div>
</div>
</div>'''

def list_html(items):
    if not items:
        return ''
    lis = ''.join(
        f'<li style="display:flex;gap:10px;align-items:flex-start;line-height:1.6;margin-bottom:10px;">'
        f'<span style="color:var(--orange);font-weight:700;flex-shrink:0;">&#8594;</span>'
        f'<span>{i}</span></li>'
        for i in items
    )
    return f'<ul style="list-style:none;padding:0;margin:0;">{lis}</ul>'

def module_html(topics):
    if not topics:
        return '<p style="color:var(--muted-deep);">Module details available on request.</p>'
    items = ''
    for i, t in enumerate(topics, 1):
        items += (
            f'<div style="display:flex;gap:14px;align-items:flex-start;padding:14px 16px;'
            f'border:1px solid var(--border);border-radius:8px;margin-bottom:10px;">'
            f'<span style="background:var(--navy);color:#fff;font-size:11px;font-weight:700;'
            f'padding:2px 8px;border-radius:100px;flex-shrink:0;">{i:02d}</span>'
            f'<span style="font-weight:600;color:var(--navy);line-height:1.5;">{t}</span></div>'
        )
    return items

for course in courses:
    slug      = course.get('slug', '')
    title     = course.get('title', '')
    desc      = course.get('description', '')
    cat       = course.get('category', '')
    level     = course.get('level', '')
    dur_text  = course.get('duration_text', 'Contact us')
    overview  = course.get('overview', desc)
    who       = course.get('who_is_it_for', '')
    eligibility = course.get('eligibility', [])
    topics    = course.get('topics', [])
    lb        = course.get('learner_benefits', [])
    eb        = course.get('employer_benefits', [])
    roles     = course.get('jobRoles', [])
    progression = course.get('progression', [])
    suitable  = course.get('suitableFor', '')
    modes     = course.get('deliveryMode', [])
    cert      = course.get('certification', 'Contact us')
    assessment = course.get('assessment', [])

    mode_pills = ''.join(
        f'<span style="display:inline-flex;align-items:center;background:var(--mist);'
        f'color:var(--navy);font-size:13px;font-weight:600;padding:5px 12px;'
        f'border-radius:100px;margin:3px;">{m}</span>'
        for m in modes
    )

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title} | Highline Fire &amp; Safety Training Institute</title>
  <meta name="description" content="{desc[:155]}"/>
  <link rel="canonical" href="{site.get('website','')}/courses/{slug}.html"/>
  <link rel="icon" href="../assets/logo.webp" type="image/webp"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Montserrat:wght@600;700;800&amp;display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="../assets/css/styles.css"/>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "{title}",
    "description": "{desc[:200].replace('"', '')}",
    "provider": {{"@type": "Organization", "name": "Highline Fire & Safety Training Institute", "url": "{site.get('website', '')}"}}
  }}
  </script>
  <style>
    .course-detail-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 60px; align-items: start; }}
    @media (max-width: 960px) {{ .course-detail-grid {{ grid-template-columns: 1fr; }} }}
    .sidebar-card {{ background: var(--white); border: 1px solid var(--border); border-radius: 16px; padding: 28px; position: sticky; top: 100px; box-shadow: 0 4px 24px rgba(11,60,109,0.07); }}
    .sidebar-row {{ padding: 14px 0; border-bottom: 1px solid var(--border); }}
    .sidebar-row:last-of-type {{ border-bottom: none; padding-bottom: 0; }}
    .sidebar-label {{ display: block; font-size: 11px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 5px; }}
    .sidebar-value {{ display: block; font-size: 15px; font-weight: 600; color: var(--navy); line-height: 1.5; }}
    .section-block {{ margin-bottom: 48px; }}
    .section-block h2 {{ font-size: 22px; font-weight: 800; color: var(--navy); margin-bottom: 18px; padding-bottom: 12px; border-bottom: 2px solid var(--mist); }}
    .hero-cta-group {{ display: flex; gap: 12px; flex-wrap: wrap; margin-top: 28px; }}
    .btn--outline-white {{
      background: transparent;
      color: #fff;
      border: 2px solid rgba(255,255,255,0.75);
      font-weight: 700;
      padding: 14px 28px;
      font-size: 15px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      transition: background .2s, color .2s;
    }}
    .btn--outline-white:hover {{
      background: #fff;
      color: var(--navy);
      border-color: #fff;
    }}
  </style>
</head>
<body>

{NAV('courses')}

<!-- HERO -->
<header class="hero hero--inner" style="min-height:45vh; padding-top:130px; padding-bottom:70px; background:linear-gradient(135deg, #0B3C6D 0%, #1a5fa8 100%);">
  <div class="hero__scrim" style="background:linear-gradient(to right,rgba(11,60,109,0.6) 0%,transparent 100%);"></div>
  <div class="hero__content" style="padding-top:0; max-width:900px; margin:0 auto;">
    <p style="font-size:13px; color:rgba(255,255,255,0.75); margin-bottom:14px;">
      <a href="../courses.html" style="color:rgba(255,255,255,0.85); text-decoration:none; font-weight:600;">&#8592; All Courses</a>
      &nbsp;/&nbsp; {cat}
    </p>
    <span style="display:inline-flex; background:rgba(255,255,255,0.14); color:#fff; font-size:12px; font-weight:700; padding:5px 16px; border-radius:100px; margin-bottom:18px; text-transform:uppercase; letter-spacing:0.07em;">{level}</span>
    <h1 class="hero__title" style="margin-bottom:16px; font-size:clamp(26px,4.5vw,46px); line-height:1.15;">{title}</h1>
    <p style="font-size:16px; line-height:1.75; color:rgba(255,255,255,0.88); max-width:700px;">{desc}</p>
    <div class="hero-cta-group">
      <a href="../admissions.html" class="btn btn--primary" style="padding:14px 28px; font-size:15px;">Apply / Enquire Now &#8594;</a>
      <a href="../contact.html" class="btn--outline-white">Ask a Question</a>
    </div>
  </div>
</header>

<main id="main">
<section class="section" style="padding-top:60px; padding-bottom:100px;">
<div class="course-detail-grid">

  <!-- LEFT: Main content -->
  <div>

    <div class="section-block">
      <h2>Course Overview</h2>
      <p style="color:var(--muted-deep); line-height:1.85; font-size:16px;">{overview}</p>
    </div>

    {'<div class="section-block"><h2>Who Is It For?</h2><p style="color:var(--muted-deep);line-height:1.85;font-size:16px;">' + who + '</p></div>' if who else ''}

    {'<div class="section-block"><h2>Benefits to Learners</h2>' + list_html(lb) + '</div>' if lb else ''}

    {'<div class="section-block"><h2>Benefits to Employers</h2>' + list_html(eb) + '</div>' if eb else ''}

    <div class="section-block">
      <h2>Course Content</h2>
      {module_html(topics)}
    </div>

    {'<div class="section-block"><h2>Assessment</h2>' + list_html(assessment) + '</div>' if assessment else ''}

    {'<div class="section-block"><h2>Career Opportunities</h2>' + list_html(roles) + '</div>' if roles else ''}

    {'<div class="section-block"><h2>Progression</h2>' + list_html(progression) + '</div>' if progression else ''}

    {'<div class="section-block"><h2>Suitable For</h2><p style="color:var(--muted-deep);line-height:1.85;font-size:16px;">' + suitable + '</p></div>' if suitable else ''}

    <!-- Bottom CTA -->
    <div style="background:var(--mist); border-radius:16px; padding:36px; text-align:center; margin-top:40px;">
      <h3 style="font-size:20px; font-weight:800; color:var(--navy); margin-bottom:10px;">Ready to enrol?</h3>
      <p style="color:var(--muted-deep); margin-bottom:24px;">Contact our admissions team for batch schedules, fee details and registration.</p>
      <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
        <a href="../admissions.html" class="btn btn--primary" style="padding:14px 28px;">Apply / Enquire Now &#8594;</a>
        <a href="../contact.html" class="btn btn--secondary" style="padding:14px 28px;">Contact Us</a>
      </div>
    </div>

  </div>

  <!-- RIGHT: Sticky sidebar -->
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
      {'<div class="sidebar-row"><span class="sidebar-label">Eligibility</span><span class="sidebar-value">' + '<br/>'.join(eligibility) + '</span></div>' if eligibility else ''}
      <div class="sidebar-row">
        <span class="sidebar-label">Training Mode</span>
        <div style="margin-top:6px; display:flex; flex-wrap:wrap; gap:4px;">{mode_pills}</div>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Course Fee</span>
        <span class="sidebar-value">Contact us for current fee structures</span>
      </div>
      <div class="sidebar-row">
        <span class="sidebar-label">Certification</span>
        <span class="sidebar-value" style="font-size:13px; line-height:1.55;">{cert}</span>
      </div>
      <a href="../admissions.html" class="btn btn--primary" style="display:block; text-align:center; padding:16px; margin-top:22px; width:100%;">Apply / Enquire Now &#8594;</a>
      <a href="../contact.html" class="btn btn--secondary" style="display:block; text-align:center; padding:13px; margin-top:10px; width:100%;">Contact Admissions</a>
    </div>
  </aside>

</div>
</section>
</main>

{FOOTER()}

<script defer src="../assets/js/site.js"></script>
<script>
  // Keep year current
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
</script>
<a aria-label="Chat on WhatsApp" class="float-wa" href="https://wa.me/919392882152" rel="noopener" target="_blank">
  <svg fill="currentColor" height="24" viewBox="0 0 24 24" width="24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.81 11.81 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.88 11.88 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.82 11.82 0 0 0-3.48-8.413Z"/></svg>
</a>
</body>
</html>'''

    out = f'website/courses/{slug}.html'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'  Generated: {out}')

print(f'\nDone — {len(courses)} course pages generated.')
