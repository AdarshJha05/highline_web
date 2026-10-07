import re

# 1. Update about.html
with open('website/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new HTML structure for the team section
team_html = """<div class="grid-3 mt-56" style="gap: 24px;">
  <article class="team-card" data-reveal="0" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Mohammed Rafiuddin</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">Managing Director</span>
  </article>
  
  <article class="team-card" data-reveal="1" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Sheik Junaidh</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">Director of Academic Studies</span>
  </article>
  
  <article class="team-card" data-reveal="2" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Badhra</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">NEBOSH Trainer</span>
  </article>
  
  <article class="team-card" data-reveal="3" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Mohammed Shahid</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">Manager</span>
  </article>
  
  <article class="team-card" data-reveal="4" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Ajay</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">Sr. Administrator</span>
  </article>
  
  <article class="team-card" data-reveal="5" style="padding: 24px; background: #fff; border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--sh-card-soft); display: flex; flex-direction: column; gap: 6px;">
    <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0;">Saniya Mahreen</h3>
    <span style="font-size: 14px; color: var(--orange); font-weight: 600;">Co-Ordinator</span>
  </article>
  </div>"""

# Replace the old team-grid block
html = re.sub(r'<div class="team-grid mt-56">.*?</div>\s*</section>', team_html + '\n  </section>', html, flags=re.DOTALL)

with open('website/about.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Clean up old CSS just so it doesn't leave dead code (optional but good practice)
with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will just leave the old CSS in there, it's not hurting anyone since the classes aren't used.
# Let's add hover effect for team-card
hover_css = """
.team-card { transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease); }
.team-card:hover { transform: translateY(-4px); box-shadow: var(--sh-hover) !important; }
"""
if '.team-card {' not in css:
    css += '\n' + hover_css
    with open('website/assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Trainers section updated to professional nameplates.")
