import os
import re

html_path = 'website/contact.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The two sections are demarcated by HTML comments
# <!-- =========================================================== INQUIRY === -->
# <section aria-labelledby="inq-h" class="inquiry"> ... </section>
# <!-- ====================================================== CONTACT INFO === -->
# <section aria-labelledby="info-h" class="section"> ... </section>

inquiry_pattern = r'(<!-- =+ INQUIRY =+ -->\s*<section aria-labelledby="inq-h" class="inquiry">.*?</section>)'
contact_info_pattern = r'(<!-- =+ CONTACT INFO =+ -->\s*<section aria-labelledby="info-h" class="section">.*?</section>)'

inquiry_match = re.search(inquiry_pattern, html, flags=re.DOTALL)
info_match = re.search(contact_info_pattern, html, flags=re.DOTALL)

if inquiry_match and info_match:
    # Remove both from the document
    html = html.replace(inquiry_match.group(1), '%%INQUIRY%%')
    html = html.replace(info_match.group(1), '%%INFO%%')
    
    # Reinsert them swapped
    html = html.replace('%%INQUIRY%%', info_match.group(1))
    html = html.replace('%%INFO%%', inquiry_match.group(1))
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Sections swapped in contact.html")

# 2. Update CSS
css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

enrich_css = """
/* ============================================================================
   INFO CARD ENHANCEMENTS
   ========================================================================== */

.info-card {
  background: var(--white) !important;
  border: 1px solid var(--border) !important;
  border-radius: 24px !important;
  padding: 40px 32px !important;
  text-align: center !important;
  box-shadow: 0 4px 20px rgba(11, 60, 109, 0.05) !important;
  transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  position: relative !important;
  overflow: hidden !important;
}
.info-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--orange);
  opacity: 0;
  transition: opacity 0.3s;
}
.info-card:hover {
  transform: translateY(-8px) !important;
  box-shadow: 0 16px 32px rgba(11, 60, 109, 0.08) !important;
}
.info-card:hover::before {
  opacity: 1;
}

.info-card > i {
  width: 64px !important; 
  height: 64px !important;
  border-radius: 16px !important;
  background: rgba(245, 124, 0, 0.1) !important; 
  color: var(--orange) !important;
  display: inline-flex !important; 
  align-items: center !important; 
  justify-content: center !important;
  font-size: 28px !important;
  margin-bottom: 24px !important;
}

.info-card p:first-of-type { 
  margin-top: 0 !important; 
  font-size: 18px !important; 
  font-weight: 800 !important; 
  color: var(--navy) !important;
  line-height: 1.4 !important; 
}
.info-card p:first-of-type a {
  color: var(--navy) !important;
}
.info-card p:last-of-type { 
  margin-top: 12px !important; 
  font-size: 15px !important; 
  color: var(--muted-deep) !important; 
  line-height: 1.6 !important; 
}
"""

if 'INFO CARD ENHANCEMENTS' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write('\n' + enrich_css)
    print("Info card CSS enriched.")
