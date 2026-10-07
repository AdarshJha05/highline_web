import os

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

svg = '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.3;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
html = html.replace('<span aria-hidden="true">~U~@</span>', svg)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)
