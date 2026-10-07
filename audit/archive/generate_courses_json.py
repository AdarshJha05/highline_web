import json
import re
import os

# Create the data directory if it doesn't exist
os.makedirs('website/assets/data', exist_ok=True)

markdown_path = 'eosh_guide_content.md'
with open(markdown_path, 'r', encoding='utf-8') as f:
    content = f.read()

categories = {}
current_category = None

lines = content.split('\n')
for line in lines:
    line = line.strip()
    if line.startswith('### '):
        current_category = line.replace('### ', '').replace(' Qualifications', '')
        categories[current_category] = []
    elif line.startswith('## Diploma Programs'):
        current_category = 'Diploma Programs'
        categories[current_category] = []
    elif line.startswith('- ') and current_category and current_category != 'Diploma Programs':
        course_name = line.replace('- ', '').strip()
        slug = re.sub(r'[^a-z0-9]+', '-', course_name.lower()).strip('-')
        categories[current_category].append({
            "id": slug,
            "title": course_name,
            "category": current_category,
            "level": "Diploma" if "Diploma" in course_name else ("Level " + re.search(r'Level (\d)', course_name).group(1) if re.search(r'Level (\d)', course_name) else "Certificate"),
            "description": f"Comprehensive training program for {course_name}. Contact us for complete syllabus and batch schedules."
        })
    elif line.startswith('**EOSH UK Level') and current_category == 'Diploma Programs':
        course_name = line.replace('**', '').strip()
        slug = re.sub(r'[^a-z0-9]+', '-', course_name.lower()).strip('-')
        categories[current_category].append({
            "id": slug,
            "title": course_name,
            "category": "Diploma Programs",
            "level": "Diploma",
            "description": f"An advanced diploma track. Modules include comprehensive health and safety management, risk assessment, and compliance leadership."
        })

# Flatten into a single list of courses
all_courses = []
for cat, courses in categories.items():
    all_courses.extend(courses)

with open('website/assets/data/courses.json', 'w', encoding='utf-8') as f:
    json.dump(all_courses, f, indent=2)

print(f"Generated {len(all_courses)} courses in courses.json.")
