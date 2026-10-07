import json
import os
import re

# Load site data
try:
    with open('website/assets/data/site.json', 'r', encoding='utf-8') as f:
        site = json.load(f)
except FileNotFoundError:
    site = {'name': 'Highline', 'phones': [], 'email': '', 'website': ''}

# Load courses
with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

# Load template
with open('website/course.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Remove the data fetching script from template
template = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded".*?</script>', '', template, flags=re.DOTALL)

# Also fix canonical or add it
if '<link rel="canonical"' not in template:
    template = template.replace('</head>', '  <link rel="canonical" href="{CANONICAL}">\n</head>')

# Create courses directory
os.makedirs('website/courses', exist_ok=True)

for course in courses:
    html = template
    
    title = course.get('title', '')
    desc = course.get('description', '')
    slug = course.get('slug', '')
    canonical = f"{site.get('website', '')}/courses/{slug}.html"
    
    # Head replacements
    html = html.replace('{CANONICAL}', canonical)
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | {site["name"]}</title>', html)
    html = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{desc[:150]}..." name="description"/>', html)
    
    # Add JSON-LD
    json_ld = {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": title,
        "description": desc,
        "provider": {
            "@type": "Organization",
            "name": site["name"],
            "sameAs": site["website"]
        }
    }
    html = html.replace('</head>', f'  <script type="application/ld+json">{json.dumps(json_ld)}</script>\n</head>')
    
    # Hero content
    accred = course.get('awardingBodyText') or course.get('category', 'Course')
    html = re.sub(r'<span class="eyebrow eyebrow--light" id="course-accreditation".*?>Loading...</span>', f'<span class="eyebrow eyebrow--light" id="course-accreditation" style="display: inline-flex; background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 100px; margin-bottom: 24px;">{accred}</span>', html)
    html = re.sub(r'<h1 class="hero__title" id="course-title".*?>Loading Course Details</h1>', f'<h1 class="hero__title" id="course-title" style="margin-bottom: 24px;">{title}</h1>', html)
    html = re.sub(r'<p id="course-desc">Please wait while we retrieve the syllabus and training information\.</p>', f'<p id="course-desc">{desc}</p>', html)
    
    # Fix paths for assets (since we are in /courses/ now)
    # The existing template uses href="assets/..." and src="assets/...". We must change to href="../assets/..."
    html = html.replace('href="assets/', 'href="../assets/')
    html = html.replace('src="assets/', 'src="../assets/')
    # Update navigation links from "index.html" to "../index.html" etc.
    html = re.sub(r'href="(index\.html|about\.html|contact\.html|courses\.html|admissions\.html|resources\.html)(.*?)"', r'href="../\1\2"', html)
    
    # Left Content Column
    
    # Overview & Audience
    audience_text = ""
    if course.get('jobRoles'):
        audience_text += "Ideal for: " + ", ".join(course['jobRoles']) + ". "
    if course.get('eligibility'):
        audience_text += "Eligibility: " + ", ".join(course['eligibility']) + "."
    if not audience_text:
        audience_text = "Please contact us for audience and eligibility details."
        
    html = re.sub(r'<p id="course-audience".*?>Loading audience data...</p>', f'<p id="course-audience" style="color: var(--muted-deep); line-height: 1.7; font-size: 16px;">{audience_text}</p>', html)
    
    # Outcomes / Modules / FAQs
    outcomes_html = ""
    if course.get('careerBenefits'):
        for cb in course['careerBenefits']:
            outcomes_html += f'<li style="display: flex; gap: 12px; align-items: flex-start; color: var(--navy); line-height: 1.5;"><span style="color: var(--orange); font-weight: 700;">→</span> {cb}</li>'
    else:
        outcomes_html = '<li style="color: var(--muted-deep);">Refer to the course curriculum for detailed learning outcomes.</li>'
    html = re.sub(r'<ul id="course-outcomes".*?>.*?</ul>', f'<ul id="course-outcomes" style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 16px;">{outcomes_html}</ul>', html, flags=re.DOTALL)
    
    modules_html = ""
    if course.get('topics'):
        for topic in course['topics']:
            modules_html += f'<div style="padding: 16px; border: 1px solid var(--border); border-radius: 8px; font-weight: 600; color: var(--navy);">{topic}</div>'
    else:
        modules_html = '<p>Syllabus available on request.</p>'
    html = re.sub(r'<div id="course-modules".*?>.*?</div>', f'<div id="course-modules" style="display: flex; flex-direction: column; gap: 12px;">{modules_html}</div>', html, flags=re.DOTALL)
    
    # FAQs
    faqs_html = ""
    faqs_html += f'<div style="padding: 20px; border: 1px solid var(--border); border-radius: 12px; margin-bottom: 12px;"><h4 style="font-size: 16px; font-weight: 700; color: var(--navy); margin-bottom: 8px;">Are there placement guarantees?</h4><p style="color: var(--muted-deep); font-size: 15px; margin: 0; line-height: 1.5;">No. We provide placement assistance, interview preparation, and skill building. Success depends on individual performance.</p></div>'
    html = re.sub(r'<div id="course-faqs".*?>.*?</div>', f'<div id="course-faqs" style="display: flex; flex-direction: column; gap: 16px;">{faqs_html}</div>', html, flags=re.DOTALL)
    
    # Right Sidebar
    dur = course.get('duration', [])
    dur_text = "Contact us"
    if dur:
        dur_text = "<br>".join([f"{d.get('label', '')}: {d.get('verbatim', '')}" for d in dur])
    
    mode = "Contact us"
    if course.get('deliveryMode'):
        mode = ", ".join(course['deliveryMode'])
        
    eligibility = "Contact us"
    if course.get('eligibility'):
        eligibility = "<br>".join(course['eligibility'])
        
    cert = course.get('certification') or "Contact us"
    
    html = re.sub(r'<p id="course-duration".*?>Loading...</p>', f'<p id="course-duration" style="font-weight: 600; color: var(--navy); margin-top: 4px;">{dur_text}</p>', html)
    html = re.sub(r'<p id="course-mode".*?>Loading...</p>', f'<p id="course-mode" style="font-weight: 600; color: var(--navy); margin-top: 4px;">{mode}</p>', html)
    html = re.sub(r'<p id="course-eligibility".*?>Loading...</p>', f'<p id="course-eligibility" style="font-weight: 600; color: var(--navy); margin-top: 4px;">{eligibility}</p>', html)
    html = re.sub(r'<p id="course-fee".*?>Loading...</p>', f'<p id="course-fee" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Contact us for current fee structures.</p>', html)
    html = re.sub(r'<p id="course-batch".*?>Loading...</p>', f'<p id="course-batch" style="font-weight: 600; color: var(--navy); margin-top: 4px;">Contact admissions for schedule.</p>', html)
    html = re.sub(r'<p id="course-certification".*?>Loading...</p>', f'<p id="course-certification" style="font-weight: 600; color: var(--navy); margin-top: 4px; font-size: 14px; line-height: 1.5;">{cert}</p>', html)
    
    out_path = f'website/courses/{slug}.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Generated 16 static course pages in website/courses/")

# Phase 3.2: Redirect Fallbacks
# Update vercel.json
vercel_json = {
  "cleanUrls": True,
  "trailingSlash": False,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "X-Frame-Options", "value": "DENY"},
        {"key": "X-XSS-Protection", "value": "1; mode=block"}
      ]
    }
  ],
  "redirects": [
    {
      "source": "/course.html",
      "has": [{"type": "query", "key": "id", "value": "(?<id>.*)"}],
      "destination": "/courses/:id",
      "permanent": True
    },
    {
      "source": "/course.html",
      "destination": "/courses.html",
      "permanent": False
    }
  ]
}

with open('website/vercel.json', 'w', encoding='utf-8') as f:
    json.dump(vercel_json, f, indent=2)
print("Created vercel.json with security headers and redirects.")

# Generate sitemap.xml
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
for page in ['index.html', 'about.html', 'contact.html', 'courses.html', 'admissions.html', 'resources.html']:
    sitemap += f'  <url>\\n    <loc>{site.get("website", "https://www.highlinefireandsafety.in")}/{page.replace(".html", "")}</loc>\\n    <changefreq>weekly</changefreq>\\n  </url>\\n'
for course in courses:
    sitemap += f'  <url>\\n    <loc>{site.get("website", "https://www.highlinefireandsafety.in")}/courses/{course.get("slug")}</loc>\\n    <changefreq>monthly</changefreq>\\n  </url>\\n'
sitemap += '</urlset>'

with open('website/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("Generated sitemap.xml")

