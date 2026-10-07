import json
import re

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the inner grid HTML
cards_html = ''
for c in courses:
    cat = c.get('category', 'Course').replace('"', '&quot;')
    lvl = c.get('level', 'certificate')
    title = c.get('title', '')
    desc = c.get('description', '')[:120] + '...'
    slug = c.get('slug', '')
    imgHtml = '<div class="course-card__img course-card__img--placeholder"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.3;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>'
    
    cards_html += f'''
<a class="course-card" href="courses/{slug}.html" data-category="{cat}">
  {imgHtml}
  <div class="course-card__content">
    <span class="course-card__tag">{lvl}</span>
    <h3 class="course-card__title">{title}</h3>
    <p class="course-card__desc">{desc}</p>
    <div class="course-card__foot" style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border);">
      <span>View Details</span>
      <span aria-hidden="true" style="color: var(--orange);">→</span>
    </div>
  </div>
</a>
'''

html = re.sub(r'(<div class="grid-3" id="courses-grid".*?>).*?(</div>\s*</section>)', r'\1\n' + cards_html + r'\n\2', html, flags=re.DOTALL)

# Replace script using a more robust regex
new_script = '''<script>
  document.addEventListener('DOMContentLoaded', function() {
    const grid = document.getElementById('courses-grid');
    const filterContainer = document.getElementById('category-filters');
    const loading = document.getElementById('courses-loading');
    
    if (loading) loading.style.display = 'none';
    
    const cards = Array.from(grid.querySelectorAll('.course-card'));
    const categories = [...new Set(cards.map(c => c.getAttribute('data-category')))];
    
    // Generate Filters
    if (filterContainer) {
      categories.forEach(cat => {
        const btn = document.createElement('button');
        btn.className = 'btn btn--secondary';
        btn.textContent = cat;
        btn.onclick = () => filterCourses(cat);
        filterContainer.appendChild(btn);
      });
    }
    
    function filterCourses(cat) {
      if (filterContainer) {
        Array.from(filterContainer.children).forEach(btn => {
          if (btn.textContent === cat) {
            btn.classList.add('btn--primary');
            btn.classList.remove('btn--secondary');
          } else {
            btn.classList.remove('btn--primary');
            btn.classList.add('btn--secondary');
          }
        });
      }
      
      cards.forEach(card => {
        if (cat === 'All' || card.getAttribute('data-category') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  });
</script>'''

# Replace from `<script>\s*document.addEventListener('DOMContentLoaded'` to `</script>`
html = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{.*?(</script>)', new_script, html, flags=re.DOTALL)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done baking courses')
