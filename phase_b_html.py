import os
from bs4 import BeautifulSoup

header_html = """
<!-- ==================== HEADER ==================== -->
<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="nav__brand" href="index.html" aria-label="Highline Fire and Safety — Home">
      <span class="nav__mark"><img src="assets/logo.webp" alt="Highline Logo" width="32" height="32"></span>
      <span class="nav__word"><b>Highline</b><span>FIRE &amp; SAFETY</span></span>
    </a>
    <div class="nav__links">
      <a class="nav__link" href="courses.html">Courses</a>
      <a class="nav__link" href="about.html">About</a>
      <a class="nav__link" href="admissions.html">Admissions</a>
      <a class="nav__link" href="resources.html">Resources</a>
      <a class="nav__link" href="contact.html">Contact</a>
    </div>
    <div class="nav__right">
      <a href="https://wa.me/919392882152" target="_blank" rel="noopener" class="nav__phone">+91 93928 82152</a>
      <a class="btn btn--primary" href="admissions.html">Apply / Enquire</a>
      <button class="nav__burger" type="button" data-burger aria-expanded="false" aria-controls="site-drawer" aria-label="Open menu"><span></span><span></span><span></span></button>
    </div>
  </nav>
</header>
<!-- ==================== /HEADER ==================== -->
"""

whatsapp_html = """
<!-- FLOATING WHATSAPP -->
<a href="https://wa.me/919392882152" target="_blank" rel="noopener" class="float-wa" aria-label="Chat on WhatsApp">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.81 11.81 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.88 11.88 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.82 11.82 0 0 0-3.48-8.413Z"/></svg>
</a>
"""

for filename in ['website/index.html', 'website/about.html', 'website/contact.html']:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Remove existing nav and hero wrapping elements
    existing_nav = soup.find('nav', class_='nav')
    if existing_nav: existing_nav.decompose()
    
    # Add new header at the start of body (after skip link)
    skip_link = soup.find('a', class_='skip-link')
    if skip_link:
        new_header = BeautifulSoup(header_html, 'html.parser')
        skip_link.insert_after(new_header)
        
    # Add float WA at the end of body
    body = soup.find('body')
    if body:
        wa_elem = BeautifulSoup(whatsapp_html, 'html.parser')
        body.append(wa_elem)

    # For index.html, rebuild the hero
    if 'index.html' in filename:
        hero = soup.find('header', class_='hero--home')
        if hero:
            hero.name = 'section' # Change tag to section
            hero['id'] = 'main'
            
            # Rebuild inner contents of hero according to prompt:
            # Order: credibility eyebrow → strong headline → one-sentence value proposition → two CTAs → three concise trust metrics
            # Visual: placeholder slot for authentic training image
            
            new_hero_inner = f"""
            <img class="ph" src="assets/img/hero-home.jpg" alt="[TO BE SUPPLIED: Authentic Highline photo]" fetchpriority="high" width="1024" height="575" style="object-fit: cover; opacity: 0.5;">
            <div class="hero__scrim"></div>
            
            <div class="hero__content">
                <span class="eyebrow eyebrow--light">EOSH & IOSH Approved Training Center</span>
                <h1 class="hero__title">Professional HSE Training. Practical Skills. Career-Ready Safety Professionals.</h1>
                <div class="hero__blurb">
                    <p>Develop discipline, awareness, and technical expertise through internationally accredited safety programs.</p>
                </div>
                <div class="hero__actions">
                    <a href="courses.html" class="btn btn--primary">Explore Courses</a>
                    <a href="admissions.html" class="btn btn--secondary btn--white">Talk to an Advisor</a>
                </div>
                <div class="hero__trust">
                    <!-- Trust metrics (placeholders based on extracted data) -->
                    <div class="trust-metric"><b>16+</b><span>Professional Courses</span></div>
                    <div class="trust-metric"><b>3</b><span>Global Accreditations</span></div>
                    <div class="trust-metric"><b>100%</b><span>Practical Focus</span></div>
                </div>
            </div>
            """
            hero.clear()
            hero.append(BeautifulSoup(new_hero_inner, 'html.parser'))

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
