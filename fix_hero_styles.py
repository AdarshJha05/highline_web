import re

with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore the correct hero styling. Let's just append a very strong override at the end of the file
# that cannot be overridden and doesn't get caught in regex destruction.

hero_fixes = """
/* ============================================================================
   HERO OVERRIDES AND ENHANCEMENTS
   ========================================================================== */

/* The hero section container */
.hero {
  position: relative;
  overflow: hidden;
  background: var(--navy);
  isolation: isolate;
  min-height: 85vh;
  display: flex;
  align-items: center;
}
.hero > .ph { 
  position: absolute; 
  inset: 0; 
  z-index: -2; 
  width: 100%; 
  height: 100%; 
  object-fit: cover; 
}
.hero__scrim {
  position: absolute; 
  inset: 0; 
  z-index: -1; 
  pointer-events: none;
  background: linear-gradient(to right, rgba(11, 60, 109, 0.92) 0%, rgba(11, 60, 109, 0.6) 60%, rgba(11, 60, 109, 0.1) 100%),
              linear-gradient(to top, rgba(11, 60, 109, 0.9) 0%, transparent 50%);
}

.hero__content {
  position: relative;
  z-index: 10;
  padding: 80px var(--pad-x);
  max-width: 1440px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

h1.hero__title {
  margin: 24px 0 24px;
  color: #ffffff;
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(40px, 5vw, 68px);
  font-weight: 800;
  line-height: 1.1;
  max-width: 900px;
  text-wrap: balance;
  text-shadow: 0 4px 24px rgba(11, 60, 109, 0.6);
}

.hero__blurb p {
  color: rgba(255, 255, 255, 0.95) !important;
  font-size: clamp(16px, 1.4vw, 20px);
  max-width: 650px;
  line-height: 1.6;
  text-shadow: 0 2px 10px rgba(11, 60, 109, 0.5);
}

.hero__actions {
  margin-top: 40px;
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.hero__trust {
  margin-top: 72px;
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
}

.trust-metric { 
  color: #fff; 
  display: flex; 
  flex-direction: column; 
  gap: 6px;
  position: relative;
}
.trust-metric:not(:last-child)::after {
  content: '';
  position: absolute;
  right: -24px;
  top: 15%;
  height: 70%;
  width: 1px;
  background: rgba(255, 255, 255, 0.25);
}

.trust-metric b { 
  font-size: clamp(28px, 3vw, 36px); 
  font-weight: 800; 
  color: var(--orange); 
  line-height: 1;
}
.trust-metric span { 
  font-size: 13px; 
  font-weight: 700; 
  text-transform: uppercase; 
  letter-spacing: 0.08em; 
  color: rgba(255, 255, 255, 0.9); 
}

@media (max-width: 1024px) {
  .hero { min-height: 60vh; }
  .hero__content { padding: 60px var(--pad-x); }
  .trust-metric:not(:last-child)::after { display: none; }
  .hero__trust { gap: 32px; margin-top: 48px; }
}
@media (max-width: 760px) {
  .hero { min-height: auto; padding: 60px 0; }
  .hero__content { padding: 40px var(--pad-x); }
  h1.hero__title { font-size: clamp(32px, 8vw, 42px); }
  .hero__actions { flex-direction: column; align-items: stretch; gap: 12px; margin-top: 32px; }
  .hero__actions .btn { justify-content: center; }
  .hero__trust { flex-direction: column; gap: 24px; margin-top: 40px; }
}
"""

# Append it to the end of styles.css to ensure it overrides everything
with open('website/assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write('\n' + hero_fixes)
