import json
import re

# 1. Update courses.json with flagship courses & images
with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

flagship_courses = [
    {
        "id": "diploma-in-fire-safety",
        "title": "Diploma in Fire Safety",
        "category": "Diploma Programs",
        "level": "Diploma",
        "description": "The flagship DFS diploma — fire prevention, control systems, and emergency response for a career in fire safety.",
        "image": "assets/img/course-dfs.jpg"
    },
    {
        "id": "advance-diploma-in-hse",
        "title": "Advance Diploma in HSE",
        "category": "Diploma Programs",
        "level": "Diploma",
        "description": "Foundational and advanced HSE practices, safety protocols, and risk management for modern industries.",
        "image": "assets/img/course-adhse.jpg"
    },
    {
        "id": "iosh-managing-safely",
        "title": "IOSH Managing Safely",
        "category": "Health & Safety",
        "level": "Certificate",
        "description": "The globally recognized IOSH certification for managers and supervisors to effectively manage workplace risks.",
        "image": "assets/img/course-iosh.jpg"
    },
    {
        "id": "construction-industrial-safety",
        "title": "Construction & Industrial Safety",
        "category": "Health & Safety",
        "level": "Diploma",
        "description": "Specialized training for heavy industry and construction, focusing on high-risk environments and equipment.",
        "image": "assets/img/course-cis.jpg"
    },
    {
        "id": "nebosh-igc",
        "title": "NEBOSH IGC",
        "category": "Health & Safety",
        "level": "Certificate",
        "description": "The gold standard in health and safety qualifications. Comprehensive international general certificate.",
        "image": "assets/img/course-nebosh.jpg"
    },
    {
        "id": "diploma-in-oil-gas-safety",
        "title": "Diploma in Oil & Gas Safety",
        "category": "Diploma Programs",
        "level": "Diploma",
        "description": "Targeted training for the petrochemical sector covering process safety, hazard zones, and offshore regulations.",
        "image": "assets/img/course-og.jpg"
    }
]

# Prepend flagship courses to the list
courses = flagship_courses + [c for c in courses if c['title'] not in [f['title'] for f in flagship_courses]]

with open('website/assets/data/courses.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, indent=2)

# 2. Update index.html "View Course Details" links
with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map the card titles to the new slugs
mapping = {
    "Diploma in Fire Safety": "diploma-in-fire-safety",
    "Advance Diploma in HSE": "advance-diploma-in-hse",
    "IOSH Managing Safely": "iosh-managing-safely",
    "Construction & Industrial Safety": "construction-industrial-safety",
    "NEBOSH IGC": "nebosh-igc",
    "Diploma in Oil & Gas Safety": "diploma-in-oil-gas-safety"
}

# The links are currently <a class="btn" href="contact.html">
# We need to replace them based on the course title inside the <article>
# A simple regex won't work well across newlines. Let's use BeautifulSoup.
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for article in soup.find_all('article', class_='course'):
    title_tag = article.find('h3', class_='course__title')
    if title_tag:
        title = title_tag.text.strip()
        if title in mapping:
            btn = article.find('a', class_='btn', href='contact.html')
            if btn:
                btn['href'] = f"course.html?id={mapping[title]}"

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

# 3. Update courses.html to render images
with open('website/courses.html', 'r', encoding='utf-8') as f:
    courses_html = f.read()

# We need to update the JavaScript renderCourses function
js_to_replace = """a.innerHTML = `
            <span class="course-card__tag">${course.level}</span>
            <h3 class="course-card__title">${course.title}</h3>
            <p class="course-card__desc">${course.description}</p>
            <div class="course-card__foot">
              <span>View Details</span>
              <span aria-hidden="true" style="color: var(--orange);">→</span>
            </div>
          `;"""

new_js = """let imgHtml = '';
          if (course.image) {
            imgHtml = `<div class="course-card__img"><img src="${course.image}" alt="${course.title}" loading="lazy" /></div>`;
          } else {
            // Placeholder for courses without specific images
            imgHtml = `<div class="course-card__img course-card__img--placeholder"><span aria-hidden="true">~U~@</span></div>`;
          }

          a.innerHTML = `
            ${imgHtml}
            <div class="course-card__content">
                <span class="course-card__tag">${course.level}</span>
                <h3 class="course-card__title">${course.title}</h3>
                <p class="course-card__desc">${course.description}</p>
                <div class="course-card__foot">
                <span>View Details</span>
                <span aria-hidden="true" style="color: var(--orange);">→</span>
                </div>
            </div>
          `;"""

if 'a.innerHTML = `' in courses_html:
    courses_html = courses_html.replace(js_to_replace, new_js)

# Add CSS for the images
img_css = """
    .course-card { padding: 0; overflow: hidden; }
    .course-card__img { height: 200px; width: 100%; overflow: hidden; background: var(--mist); }
    .course-card__img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s var(--ease); }
    .course-card:hover .course-card__img img { transform: scale(1.05); }
    .course-card__img--placeholder { display: flex; align-items: center; justify-content: center; font-size: 48px; color: var(--blue-100); }
    .course-card__content { padding: 24px; display: flex; flex-direction: column; flex-grow: 1; }
"""
if '.course-card__img' not in courses_html:
    courses_html = courses_html.replace('</style>', img_css + '</style>')

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(courses_html)

print("Course links and images mapped.")
