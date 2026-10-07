import json
import re

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Rebuild the static cards
cards_html = ''
for c in courses:
    cat = c.get('category', 'Course')
    lvl = c.get('level', 'Certificate')
    title = c.get('title', '')
    desc = c.get('description', '')[:140] + '...'
    slug = c.get('slug', '')
    dur = c.get('duration_text', '')

    # Color accent per category
    if 'Diploma' in cat:
        tag_color = 'var(--navy)'
    elif 'International' in cat:
        tag_color = 'var(--teal)'
    else:
        tag_color = 'var(--green)'

    imgHtml = f'<div class="course-card__img course-card__img--placeholder" style="background: linear-gradient(135deg, var(--navy) 0%, #1a5fa8 100%);"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>'

    cards_html += f'''
<a class="course-card" href="courses/{slug}.html" data-category="{cat}">
  {imgHtml}
  <div class="course-card__content">
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
      <span class="course-card__tag" style="color:{tag_color}; background: transparent; padding:0; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;">{lvl}</span>
      {f'<span style="font-size:11px; color:var(--muted); font-weight:500;">· {dur}</span>' if dur else ''}
    </div>
    <h3 class="course-card__title">{title}</h3>
    <p class="course-card__desc">{desc}</p>
    <div class="course-card__foot" style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border);">
      <span style="font-weight:600; font-size:14px;">View Details</span>
      <span aria-hidden="true" style="color: var(--orange); font-size:18px;">→</span>
    </div>
  </div>
</a>
'''

html = re.sub(
    r'(<div class="grid-3" id="courses-grid"[^>]*>).*?(</div>\s*</section>)',
    r'\1\n' + cards_html + r'\n\2',
    html, flags=re.DOTALL
)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Baked {len(courses)} course cards into courses.html")
