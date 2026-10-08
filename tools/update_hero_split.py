import re

css_block = """
/* ============================================================== SPLIT HERO (HOME PAGE) === */
.hero-wrap--split {
  background: var(--white);
  padding-top: 140px; /* Account for fixed header */
  padding-bottom: 80px;
  position: relative;
  overflow: hidden;
}
.hero-split {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}
@media (max-width: 992px) {
  .hero-split {
    grid-template-columns: 1fr;
    padding-top: 20px;
    gap: 48px;
  }
}
.hero-split__content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 600px;
}
.eyebrow--navy {
  color: var(--navy);
  background: rgba(11, 60, 109, 0.08);
  display: inline-flex;
  padding: 6px 16px;
  border-radius: 100px;
  font-size: 13px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  align-self: flex-start;
}
.hero-split__title {
  font-size: 52px;
  line-height: 1.15;
  font-weight: 800;
  color: var(--navy);
  letter-spacing: -1px;
}
@media (max-width: 768px) {
  .hero-split__title { font-size: 40px; }
}
.hero-split__blurb {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted-deep);
  font-weight: 500;
}
.hero-split__actions {
  display: flex;
  gap: 16px;
  margin-top: 8px;
  flex-wrap: wrap;
}
.btn--outline {
  background: transparent;
  border: 2px solid var(--border-mid);
  color: var(--navy);
}
.btn--outline:hover {
  border-color: var(--navy);
  background: rgba(11, 60, 109, 0.04);
}
.hero-split__trust {
  display: flex;
  gap: 32px;
  margin-top: 32px;
  padding-top: 32px;
  border-top: 1px solid var(--border);
  flex-wrap: wrap;
}
.hero-split__trust .trust-metric {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.hero-split__trust .trust-metric b {
  font-size: 28px;
  font-weight: 800;
  color: var(--orange);
  line-height: 1;
}
.hero-split__trust .trust-metric span {
  font-size: 13px;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Image Side */
.hero-split__media {
  position: relative;
  height: 100%;
  min-height: 600px;
}
@media (max-width: 992px) {
  .hero-split__media {
    min-height: 400px;
    height: 400px;
  }
}
.hero-split__image-wrapper {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 24px 64px rgba(11, 60, 109, 0.15);
  transform: translateZ(0); /* Force hardware acceleration */
}
.hero-split__image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  animation: heroKenBurns 20s infinite alternate linear;
}
.hero-split__badge {
  position: absolute;
  bottom: 32px;
  left: -24px;
  background: var(--white);
  padding: 16px 24px;
  border-radius: 12px;
  box-shadow: 0 16px 32px rgba(0,0,0,0.1);
  font-size: 15px;
  color: var(--navy);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 10;
  animation: floatBadge 6s infinite ease-in-out;
}
@media (max-width: 768px) {
  .hero-split__badge {
    left: 16px;
    bottom: 16px;
  }
}
@keyframes floatBadge {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* Custom Data-Reveal overrides for horizontal slide */
[data-reveal].hero-slide-left {
  opacity: 0;
  transform: translateX(-40px);
}
[data-reveal].hero-slide-right {
  opacity: 0;
  transform: translateX(40px);
}
[data-reveal].is-in.hero-slide-left,
[data-reveal].is-in.hero-slide-right {
  opacity: 1;
  transform: translateX(0);
}
"""

with open('website/assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_block)

new_hero_html = """  <div class="hero-wrap hero-wrap--split">
    <section class="hero-split" id="main">
      <div class="hero-split__content">
        <span class="eyebrow eyebrow--navy hero-slide-left" data-reveal="0">EOSH &amp; IOSH Approved Training Center</span>
        <h1 class="hero-split__title hero-slide-left" data-reveal="1">Professional HSE Training. Practical Skills. Career-Ready Professionals.</h1>
        <div class="hero-split__blurb hero-slide-left" data-reveal="2">
          <p>Develop discipline, awareness, and technical expertise through internationally recognized safety programs.</p>
        </div>
        <div class="hero-split__actions hero-slide-left" data-reveal="3">
          <a class="btn btn--primary" href="courses.html">Explore Courses</a>
          <a class="btn btn--outline" href="contact.html">Talk to an Advisor</a>
        </div>
        <div class="hero-split__trust hero-slide-left" data-reveal="4">
          <div class="trust-metric"><b class="counter" data-suffix="+" data-target="16">0+</b><span>Professional Courses</span></div>
          <div class="trust-metric"><b>3+</b><span>Learning Pathways</span></div>
          <div class="trust-metric"><b class="counter" data-suffix="" data-target="21">0</b><span>Hour IOSH Program</span></div>
        </div>
      </div>
      <div class="hero-split__media hero-slide-right" data-reveal="2">
        <div class="hero-split__image-wrapper" id="hero-bg-parallax">
          <img alt="Highline students in training" class="ph hero-bg-img" fetchpriority="high" src="assets/img/hero-home.jpg" />
          <div class="hero-split__badge">
            <span style="color:var(--orange); font-size: 20px; line-height: 1;">★</span> <b>4.9/5</b> Rated by Graduates
          </div>
        </div>
      </div>
    </section>
  </div>"""

with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the existing hero-wrap block
html = re.sub(
    r'<div class="hero-wrap">.*?</div>\s*</section>\s*</div>',
    new_hero_html,
    html,
    flags=re.DOTALL
)

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html and styles.css for split layout.")
