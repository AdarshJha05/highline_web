import json
import re

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

images = [
    'assets/img/safety_fire.jpg',
    'assets/img/safety_construction.jpg',
    'assets/img/safety_industrial.jpg',
    'assets/img/safety_classroom.jpg'
]

# Rebuild the static cards
cards_html = ''
for i, c in enumerate(courses):
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

    img_src = images[i % len(images)]

    # Modern Image wrapper with gradient overlay at the bottom for contrast if needed
    imgHtml = f'''
    <div class="course-card__img">
      <img src="{img_src}" alt="{title} Training" loading="lazy" />
      <div class="course-card__img-overlay"></div>
    </div>
    '''

    cards_html += f'''
<a class="course-card" href="courses/{slug}.html" data-category="{cat}">
  {imgHtml}
  <div class="course-card__content">
    <div class="course-card__meta">
      <span class="course-card__tag" style="color:{tag_color};">{lvl}</span>
      {f'<span class="course-card__dur">&#8226; {dur}</span>' if dur else ''}
    </div>
    <h3 class="course-card__title">{title}</h3>
    <p class="course-card__desc">{desc}</p>
    <div class="course-card__foot">
      <span>View Course Details</span>
      <span class="course-card__arrow">&#8594;</span>
    </div>
  </div>
</a>
'''

# Update the HTML block in courses.html
html = re.sub(
    r'(<div class="grid-3" id="courses-grid"[^>]*>).*?(</div>\s*</section>)',
    r'\1\n' + cards_html + r'\n\2',
    html,
    flags=re.DOTALL
)

# Enhance the CSS styles inside courses.html
modern_css = '''
    .course-card {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 0;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 12px rgba(11, 60, 109, 0.04);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      text-decoration: none;
      color: inherit;
    }
    .course-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 16px 40px rgba(11, 60, 109, 0.12);
      border-color: transparent;
    }
    .course-card__img {
      height: 220px;
      width: 100%;
      position: relative;
      overflow: hidden;
      background: var(--mist);
    }
    .course-card__img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .course-card:hover .course-card__img img {
      transform: scale(1.08);
    }
    .course-card__img-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.4) 0%, transparent 40%);
      opacity: 0;
      transition: opacity 0.4s ease;
    }
    .course-card:hover .course-card__img-overlay {
      opacity: 1;
    }
    .course-card__content {
      padding: 28px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .course-card__meta {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
    }
    .course-card__tag {
      background: rgba(11, 60, 109, 0.06);
      padding: 6px 12px;
      border-radius: 100px;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .course-card__dur {
      font-size: 12px;
      color: var(--muted);
      font-weight: 600;
    }
    .course-card__title {
      font-size: 19px;
      font-weight: 800;
      color: var(--navy);
      line-height: 1.35;
      margin-bottom: 12px;
      transition: color 0.2s ease;
    }
    .course-card:hover .course-card__title {
      color: var(--orange);
    }
    .course-card__desc {
      font-size: 14px;
      color: var(--muted-deep);
      line-height: 1.6;
      margin-bottom: 24px;
      flex-grow: 1;
    }
    .course-card__foot {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border);
      padding-top: 18px;
      font-size: 14px;
      font-weight: 700;
      color: var(--navy);
    }
    .course-card__arrow {
      color: var(--orange);
      font-size: 18px;
      transition: transform 0.3s ease;
    }
    .course-card:hover .course-card__arrow {
      transform: translateX(4px);
    }
    .btn[data-filter] {
      padding: 8px 16px;
      font-size: 14px;
      border-color: var(--border-mid);
    }
    .btn[data-filter].btn--active {
      background: var(--navy);
      color: var(--white);
      border-color: var(--navy);
    }
'''

# Replace whatever styles are currently in <style> block for course-card
# (Assuming the <style> block is at the end of courses.html before <script>)
html = re.sub(
    r'<style>.*?</style>',
    f'<style>\n{modern_css}\n  </style>',
    html,
    flags=re.DOTALL
)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Baked {len(courses)} course cards into courses.html with modern UI")
