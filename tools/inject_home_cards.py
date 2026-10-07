import json
import re

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

home_courses = courses[:6]

images_list = [
    'assets/img/course-dfs.jpg',
    'assets/img/course-adhse.jpg',
    'assets/img/course-iosh.jpg',
    'assets/img/course-cis.jpg',
    'assets/img/course-nebosh.jpg',
    'assets/img/course-og.jpg'
]

cards_html = ''
for i, c in enumerate(home_courses):
    cat = c.get('category', 'Course')
    lvl = c.get('level', 'Certificate')
    title = c.get('title', '')
    desc = c.get('description', '')[:140] + '...'
    slug = c.get('slug', '')
    dur = c.get('duration_text', '')

    if 'Diploma' in cat:
        tag_color = 'var(--navy)'
    elif 'International' in cat:
        tag_color = 'var(--teal)'
    else:
        tag_color = 'var(--green)'

    img_src = images_list[i % len(images_list)]

    imgHtml = f'''
    <div class="course-card__img">
      <img src="{img_src}" alt="{title} Training" loading="lazy" />
      <div class="course-card__img-overlay"></div>
    </div>
    '''

    cards_html += f'''
<a class="course-card" href="courses/{slug}.html" style="min-width: 340px; max-width: 380px; flex: 0 0 auto;">
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

with open('website/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = re.sub(
    r'(<div class="course-grid course-rail mt-56" data-rail="">).*?(</div>\s*<div class="courses-foot")',
    r'\1\n' + cards_html + r'\n\2',
    index_html,
    flags=re.DOTALL
)

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Injected into index.html")
