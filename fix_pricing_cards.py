import re

# 1. Update index.html
with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the price amounts completely
html = re.sub(r'<div class="price__amount">.*?</div>\s*', '', html, flags=re.DOTALL)

# Replace "Choose This Track" buttons with "Enquire" buttons
# Also, remove the btn--out style (which is an outline) and make it primary or standard.
html = re.sub(
    r'<a class="btn btn--out btn--block" href="contact\.html">Choose This Track.*?</a>',
    r'<a class="btn btn--primary btn--block" href="contact.html">Enquire Now <span aria-hidden="true" style="margin-left:8px;">→</span></a>',
    html, flags=re.DOTALL
)

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix badge--blue CSS
with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace var(--blue) with var(--orange) for the badge
css = css.replace('.badge--blue { background: var(--blue); color: #fff; }', '.badge--blue { background: var(--orange); color: var(--white); }')

# Add some top margin to the button since the price amount is gone
fix_margin = """
/* Add spacing above the enquire button in pricing cards now that amounts are gone */
.price .btn { margin-top: 32px !important; }
"""
if 'margin-top: 32px !important;' not in css:
    css += '\n' + fix_margin

with open('website/assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Pricing cards fixed.")
