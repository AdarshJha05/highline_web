import os

css_path = 'website/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the broken CSS block
broken_css = """  .hero--inner .hero__title,
  .hero--contact 
  
  .hero__scroll { display: none; }"""

fixed_css = """  .hero__scroll { display: none; }"""

if broken_css in css:
    css = css.replace(broken_css, fixed_css)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Fixed CSS syntax error.")
else:
    print("Broken CSS not found. Trying regex.")
    import re
    # We want to remove .hero--inner .hero__title, and .hero--contact 
    # before .hero__scroll { display: none; }
    new_css = re.sub(r'\.hero--inner[^\n]*\n\s*\.hero--contact[^\n]*\n+\s*\.hero__scroll\s*\{\s*display:\s*none;\s*\}', '  .hero__scroll { display: none; }', css)
    if new_css != css:
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(new_css)
        print("Fixed CSS syntax error via regex.")
    else:
        print("Still couldn't find the exact match to replace.")
