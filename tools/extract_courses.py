import re
import json

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

courses = []
cards = re.findall(r'<a class="course-card".*?<img src="(.*?)".*?<h3 class="course-card__title">(.*?)</h3>', html, re.DOTALL)
for i, c in enumerate(cards):
    title = c[1].strip()
    img = c[0].strip()
    courses.append({"title": title, "img": img})

with open('website/courses_list.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, indent=2)
print(f"Extracted {len(courses)} courses")
