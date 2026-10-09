import re

with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_path_css = r"""\.path \{
    background: var\(--tint\);
    border: 1px solid var\(--border\);
    border-radius: var\(--r-tile\);
    padding: 24px;
  \}
  \.path--hi \{ background: var\(--blue-100\); border-color: var\(--blue-300\); \}
  \.path > span \{ font-size: 13px; font-weight: 800; color: var\(--blue-deep\); \}
  \.path h3 \{ margin-top: 10px; font-size: 16\.5px; font-weight: 700; \}
  \.path p \{ margin-top: 8px; font-size: 13\.5px; color: var\(--muted\); line-height: 1\.55; \}
  \.path--hi p \{ color: var\(--muted-deep\); \}"""

new_path_css = """.path {
    background: var(--tint);
    border: 1px solid var(--border);
    border-radius: var(--r-tile);
    padding: 24px;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    position: relative;
    z-index: 1;
  }
  .path:hover {
    transform: translateY(-8px);
    background: var(--navy);
    border-color: var(--navy);
    box-shadow: 0 24px 48px rgba(11, 34, 60, 0.25);
    z-index: 2;
  }
  .path:hover > span { color: var(--blue-300); }
  .path:hover h3 { color: var(--white); }
  .path:hover p { color: rgba(255, 255, 255, 0.85); }
  .path--hi { background: var(--blue-100); border-color: var(--blue-300); }
  .path--hi:hover { background: var(--blue-deep); border-color: var(--blue-deep); }
  .path > span { font-size: 13px; font-weight: 800; color: var(--blue-deep); transition: color 0.3s ease; }
  .path h3 { margin-top: 10px; font-size: 16.5px; font-weight: 700; color: var(--navy); transition: color 0.3s ease; }
  .path p { margin-top: 8px; font-size: 13.5px; color: var(--muted); line-height: 1.55; transition: color 0.3s ease; }
  .path--hi p { color: var(--muted-deep); }"""

css = re.sub(old_path_css, new_path_css, css)

# In case there's a spacing issue, we'll try an even safer approach if the above didn't match.
if '.path:hover' not in css:
    css = css.replace('.path {\n    background: var(--tint);\n    border: 1px solid var(--border);\n    border-radius: var(--r-tile);\n    padding: 24px;\n  }', new_path_css.split('.path--hi {')[0])
    
with open('website/assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated .path CSS.")
