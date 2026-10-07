import re

with open('website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the JS template
old_js = """<span class="course-card__tag">${course.level}</span>
                <h3 class="course-card__title">${course.title}</h3>
                <p class="course-card__desc">${course.description}</p>
                <div class="course-card__foot">
                <span>View Details</span>
                <span aria-hidden="true" style="color: var(--orange);">→</span>
                </div>"""

new_js = """<span class="course-card__tag">${course.level}</span>
                <h3 class="course-card__title">${course.title}</h3>
                <p class="course-card__desc">${course.description}</p>
                <div style="display: flex; flex-direction: column; gap: 6px; margin: 16px 0; font-size: 13px; color: var(--muted-deep);">
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <span aria-hidden="true" style="color: var(--orange);">⏱️</span> <b>Duration:</b> ${course.duration}
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <span aria-hidden="true" style="color: var(--orange);">🏢</span> <b>Mode:</b> ${course.mode}
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <span aria-hidden="true" style="color: var(--orange);">🎓</span> <b>Accreditation:</b> ${course.accreditation}
                  </div>
                </div>
                <div class="course-card__foot" style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border);">
                <span>View Details</span>
                <span aria-hidden="true" style="color: var(--orange);">→</span>
                </div>"""

html = html.replace(old_js, new_js)

with open('website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("courses.html updated.")
