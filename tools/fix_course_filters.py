import re

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_script = '''<script>
  document.addEventListener('DOMContentLoaded', function() {
    const grid = document.getElementById('courses-grid');
    const filterContainer = document.getElementById('category-filters');
    const loading = document.getElementById('courses-loading');
    
    if (loading) loading.style.display = 'none';
    
    const cards = Array.from(grid.querySelectorAll('.course-card'));
    const categories = [...new Set(cards.map(c => c.getAttribute('data-category')))];
    
    if (filterContainer) {
      // Clear all generated buttons except the "All Courses" one
      const allBtn = filterContainer.querySelector('[data-filter="all"]');
      if (allBtn) {
        // Ensure the initial state is correct
        allBtn.classList.remove('btn--secondary', 'btn--active');
        allBtn.classList.add('btn--primary');
        allBtn.onclick = () => filterCourses('All Courses');
      }
      
      // Generate Buttons for categories
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
          // If the button's text matches the category, or if it's the "All Courses" button and we selected "All Courses"
          if (btn.textContent.trim() === cat) {
            btn.classList.add('btn--primary');
            btn.classList.remove('btn--secondary', 'btn--active');
          } else {
            btn.classList.remove('btn--primary', 'btn--active');
            btn.classList.add('btn--secondary');
          }
        });
      }
      
      cards.forEach(card => {
        if (cat === 'All Courses' || card.getAttribute('data-category') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  });
</script>'''

html = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{.*?(</script>)', new_script, html, flags=re.DOTALL)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed filter JS in courses.html')
