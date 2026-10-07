import os

with open('website/admissions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add data-label to all inputs/selects/textareas
html = html.replace('name="name"', 'name="name" data-label="Full Name"')
html = html.replace('name="email"', 'name="email" data-label="Email Address"')
html = html.replace('name="phone"', 'name="phone" data-label="Phone Number"')
html = html.replace('name="qualification"', 'name="qualification" data-label="Highest Qualification"')
html = html.replace('name="course"', 'name="course" data-label="Selected Course"')
html = html.replace('name="batch"', 'name="batch" data-label="Preferred Batch"')
html = html.replace('name="message"', 'name="message" data-label="Additional Message"')

# Also update the note class to match site.js expectations
# site.js expects a [data-note] element for status messages.
html = html.replace('<div class="form-status"', '<p class="form-note" data-note="" role="status"></p><div class="form-status"')

with open('website/admissions.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added data-labels to admissions form.")
