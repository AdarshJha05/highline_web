# Highline Fire & Safety Training Institute - Web Root

This directory (`website/`) is the production-ready deployment folder. It uses pure HTML, CSS, and vanilla JS.

## Page Structure
- `index.html` - Home Page (Hero, Trust Metrics, Courses Slider, Value Props, Testimonials)
- `about.html` - About Us (Story, Mission/Vision, Accreditation, Faculty, Campus)
- `courses.html` - Course Catalogue (Dynamic Grid powered by `courses.json`)
- `course.html` - Course Detail Template (Dynamically renders specific course syllabus and details)
- `admissions.html` - Admissions Flow (Enrollment Process, Fee Structure, Application Form)
- `resources.html` - Resources Hub (Safety Guides, Blog, Toolbox Talks, Downloadables)
- `contact.html` - Contact (Inquiry Form, Map, Office Address)

## Assets & Data
- `assets/css/styles.css` - Global CSS tokens, resets, component styles, and responsive media queries.
- `assets/js/site.js` - Global behaviors (Navigation Drawer, IntersectionObservers, Form handling/mail formatting).
- `assets/data/courses.json` - The central database for all 56+ courses. **Edit this file to update course descriptions, fees, durations, and batches.**

## Modifying Headers and Footers
Because this is a pure static site without a build step, the `<header class="site-header">` and `<footer class="footer">` blocks are physically present on every `.html` page.
When adding new navigation links, ensure you update the HTML block across all top-level `.html` files to maintain consistency.

## Forms
Forms (Admissions and Contact) use HTML5 validation and are intercepted by `site.js`. Instead of requiring a backend email server, `site.js` dynamically compiles the user's answers and triggers a pre-filled `mailto:` prompt.
