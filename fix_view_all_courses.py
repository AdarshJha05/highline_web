import os

with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html">View All Courses', 'href="courses.html">View All Courses')

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
