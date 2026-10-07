import os

css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace variables with hardcoded hex and !important to guarantee rendering
css = css.replace(
    '.badge--blue { background: var(--orange); color: var(--white); }',
    '.badge--blue { background: #F57C00 !important; color: #FFFFFF !important; }'
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Hardcoded badge colors.")
