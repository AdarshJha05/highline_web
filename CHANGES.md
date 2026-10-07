# Changes

## Scripts Quarantined
The following dev scripts generated unsupported facts and have been quarantined to `audit/archive/` to ensure they do not re-run:
- `generate_courses_json.py` (Generated 56 courses from an external EOSH guide, overriding the 16 approved courses).
- `enhance_courses_data.py` (Injected "100% placement assistance", global flexible batch dates, and unsupported accreditation phrasing across the JSON database).

## Content Removed
- **Course records**: Removed 46 unsupported courses from `courses.json`.
- **False Claims**: Stripped all mentions of "100%", "placement", "industry tie-ups" and "years of experience".
- **Testimonials**: Removed 5 named individuals from the JS array.
- **Batches**: Removed all global batch date promises.
- **Scope Misrepresentations**: Removed "Confirm & Pay" text and payment gateway illusions from the admissions flow.


## Phase 2: Scope Honesty
- **Admissions Flow**: Rewrote the 'Confirm & Pay' section to explicitly clarify it is an enquiry workflow. Added fallback instructions for the 'mailto:' action.
- **Legal Placeholders**: Created privacy.html and 	erms.html pending legal review.
- **Funnel Architecture**: Drafted docs/REGISTRATION_PLAN.md to outline the future Vercel serverless integration.

## Phase 3: SEO & Routing
- **Static Generation**: Created 	ools/generate_pages.py to statically render the 16 courses into website/courses/<slug>.html.
- **Routing**: Updated courses.html and index.html to point directly to the static .html files. Added ercel.json to handle redirects from the old query-param URLs.
- **Sitemap**: Generated sitemap.xml listing all top-level pages and the 16 course pages.

## Phase 4: Remaining Audit Items
- **Accessibility**: Fixed contrast on orange buttons and UI elements (changed from #F57C00 to #C05C00 to meet WCAG AA requirements of 4.5:1).
- **Security & Headers**: Applied security headers in ercel.json (X-Frame-Options, X-XSS-Protection, etc.).
- **Audit Report**: Updated AUDIT_REPORT.md to reflect all fixes.
- **Content Need**: Created CONTENT_NEEDED.md detailing every missing piece of authentic content required from the client.
