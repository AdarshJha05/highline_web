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

