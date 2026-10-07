import os
import re

# 1. Fix site.js spelling
js_path = 'website/assets/js/site.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('High Line', 'Highline')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed spelling in site.js.")

# 2. Add JSON-LD Structured Data to all HTML pages
html_files = ['website/index.html', 'website/about.html', 'website/contact.html', 'website/courses.html', 'website/course.html', 'website/admissions.html']

json_ld = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "Highline Fire & Safety Training Institute",
    "url": "https://highlineweb.vercel.app",
    "logo": "https://highlineweb.vercel.app/assets/logo.webp",
    "image": "https://highlineweb.vercel.app/assets/img/hero-about.jpg",
    "description": "Internationally accredited fire and safety training institute in Karimnagar. Approved EOSH and IOSH training provider offering diploma and certificate courses.",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Beside Geetha Bhavan, opp. Jafri Masjid",
      "addressLocality": "Karimnagar",
      "addressRegion": "Telangana",
      "postalCode": "505001",
      "addressCountry": "IN"
    },
    "telephone": "+91-812-111-8000",
    "email": "highlinefireandsafety@gmail.com",
    "sameAs": [
      "https://www.facebook.com/highlinefireandsafety",
      "https://www.instagram.com/highlinefireandsafety",
      "https://www.linkedin.com/company/highlinefireandsafety"
    ]
  }
  </script>
"""

for filepath in html_files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'application/ld+json' not in html:
        # Insert before </head>
        html = html.replace('</head>', json_ld + '</head>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added JSON-LD to {filepath}.")
