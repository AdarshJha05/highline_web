import os

filepath = 'website/resources.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

json_ld = """<script type="application/ld+json">
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
    "email": "highlinefireandsafety@gmail.com"
  }
  </script>"""

if 'application/ld+json' not in html:
    html = html.replace('</head>', json_ld + '\n</head>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
