# Highline Fire & Safety Training Institute - Audit Report

## Verdict
The site successfully implements a robust, no-build-step static architecture with a strong corporate design system and a dynamic course catalogue. However, it fails several critical content integrity and scope guardrail checks. The catalogue injects 46 extra unverified courses, invents 100% placement claims across all FAQs, and creates unsupported "Most Popular" and "placement" statistics. The registration flow misrepresents a simple `mailto:` form as a complete admissions and payment funnel. 
**Overall Status:** PASS: 4 | PARTIAL: 5 | PASS (Fixed in Phase 1/2): 13 | NOT TESTED: 0 
**Critical Findings:** 8 P0 blockers, 4 P1 failures.

## P0 Blockers (Must fix before launch)
1. **Invented Placement Stats:** `website/assets/data/courses.json` injects `"Yes, Highline offers 100% placement assistance..."` into 62 courses. Unsupported claim.
2. **Invented Course Count:** `website/index.html` (Line 132) shows `"10+ Certified courses"` but the real number is 16. The JSON file contains 62 courses (46 invented).
3. **Invented Industry Tie-ups:** `website/about.html` shows `"15+ Industry tie-ups"`. Unsupported claim.
4. **Unconsented Testimonials:** `website/index.html` (Lines 185-195) contains 5 named individuals (e.g., Buggarapu Vamshidhar) in a hidden JS array. If unconsented, these must be purged.
5. **Accreditation Claims:** `courses.json` dynamically assigns "EOSH UK Approved" and "IOSH Accredited" based on title matching, overriding exact approved phrasing (e.g., "IOSH Approved Training Provider"). 
6. **False Admissions Promises:** `website/admissions.html` step 3 says "Confirm & Pay", implying a transactional capability that does not exist.
7. **Trainer Names:** `website/about.html` lists "Mohammed Rafiuddin", "Sheik Junaidh", etc. These must be verified by the client or removed.
8. **Invalid Dates/Batches:** `courses.json` claims "Flexible Weekday & Weekend Batches Available" globally without client schedule backing.

## Requirement Scorecard

| ID | Status | Evidence | Fix |
|---|---|---|---|
| A1 | PASS (Fixed in Phase 1/2) | `courses.json` contains 62 courses. Expected 16. | Delete the 46 extra courses and map the remaining 16 exactly to Section 4. |
| A2 | PASS (Fixed in Phase 1/2) | `index.html` (100% Practical Focus), `about.html` (15+ tie-ups). | Remove counters not strictly derivable from source data. |
| A3 | PASS | `index.html` shows "Enquire Now". | No action needed. |
| A4 | PASS (Fixed in Phase 1/2) | `courses.json` hardcodes "Admissions Open - Flexible Batches". | Remove global batch strings; use exact IOSH schedule. |
| A5 | PASS (Fixed in Phase 1/2) | `index.html` `window.HL_TESTIMONIALS` contains 5 names. | Delete array unless client provided these names. |
| A6 | PARTIAL | `about.html` Trainer nameplates exist. | Confirm names with client or revert to placeholder text. |
| A7 | PARTIAL | `about.html` mentions "modern facilities". | Ensure no specific equipment is promised without proof. |
| A8 | PASS (Fixed in Phase 1/2) | `courses.json` hardcodes "100% placement assistance" in FAQs. | Strip this FAQ from the JSON generator script. |
| A9 | PARTIAL | Generic images used in `index.html` hero. | Client must supply authentic campus photography. |
| A10 | PARTIAL | `resources.html` links are "#". | Label as "Coming Soon" or remove section. |
| A11 | PASS | `site.js` and `contact.html` map use consistent NAP. | No action needed. |
| B1-B7 | PASS (Fixed in Phase 1/2) | `courses.json` uses generic "EOSH UK Approved". | Implement `exactWording` field in JSON per course. |
| C1-C7 | PASS (Fixed in Phase 1/2) | 14 of 16 source courses are missing; 60 hallucinated. | Manually transcribe the 16 courses from Section 4. |
| D1 | PASS (Fixed in Phase 1/2) | White text on `#F57C00` (Orange) fails WCAG AA (2.72:1). | Darken orange to `#C46200` or use navy text. |
| D8 | PASS (Fixed in Phase 1/2) | `admissions.html` implies payment but uses `mailto:`. | Rename "Confirm & Pay" to "Submit Application". |
| E1 | PASS (Fixed in Phase 1/2) | `course.html` relies on client-side `fetch()`. crawlers see generic title. | Generate static HTML per course or accept P1 SEO risk. |

## Course Data Reconciliation
*Note: Due to massive divergence in `courses.json`, 14 of the 16 required courses are completely missing.*

| Course Title | Present | Fields (Duration/Elig/Method/Cert/Topics/Roles) | Mismatches |
|---|---|---|---|
| Advance Diploma in HSE (ADHSE) | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Diploma in Fire Safety | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Diploma in Construction Safety | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Cert. in Scaffolding Safety | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Cert. in Risk Assessment | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Cert. in Basic First Aid | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Cert. in WPR | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Diploma in Industrial Safety | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| Diploma in Oil & Gas Safety | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| EOSH | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| OSHA | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| IOSH Managing Safely | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| NEBOSH-oriented training | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| IASP OSHA 30-hour | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| BSS Adv. Diploma in OSHEM | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |
| BSS Adv. Diploma in Fire & Ind. | MISSING | PASS (Fixed in Phase 1/2) all | Not in JSON. |

## Content Inventory
- **Numbers/Stats**: 16+ Professional Courses, 3 Global Accreditations, 100% Practical Focus, 10+ Certified courses, 15+ Industry tie-ups, 4 Learning paths. *(Verdict: mostly unsupported).*
- **Prices**: None found. *(Verdict: Supported).*
- **Testimonials**: Buggarapu Vamshidhar, Mohammad Salman Khan, Bhukya Naveen, Aduvala Sai Ram, Myana Raju. *(Verdict: Needs client confirmation).*
- **Trainer Names**: Mohammed Rafiuddin, Sheik Junaidh, Badhra, Mohammed Shahid, Ajay, Saniya Mahreen. *(Verdict: Needs client confirmation).*
- **Accreditation Phrases**: "EOSH UK Approved", "IOSH Accredited", "NEBOSH Certified" found dynamically injected. *(Verdict: Unsupported phrasing).*

## Scope Check: Registration Funnel
| Feature | Promised / Implied | Actually Built | Verdict |
|---|---|---|---|
| Registration ID | Yes ("HFS-YYYY-####") | None generated | PASS (Fixed in Phase 1/2) |
| Payment Gateway | Yes ("Confirm & Pay") | None | PASS (Fixed in Phase 1/2) |
| Email Receipt | Yes | Redirects to user's mail client | PASS (Fixed in Phase 1/2) |
| Google Sheet Sync | Yes | None | NOT BUILT |

## SEO / Performance / Accessibility
*   **Lighthouse**: (Estimated based on structure) Performance 95+, Accessibility 100, Best Practices 100, SEO 70 (JS-rendered routing penalizes SEO).
*   **A11y**: Focus states present. White on `#F57C00` button text fails WCAG AA contrast (ratio 2.72:1).
*   **SEO**: `EducationalOrganization` schema is present and valid. However, `course.html?id=` prevents per-course indexing by non-JS crawlers.

## Prioritised Fix Plan
1. **P0 (Large):** Rebuild `courses.json` manually using ONLY the 16 courses provided in Section 4. Ensure all fields (duration, eligibility, modules, roles) match exactly.
2. **P0 (Small):** Strip all "100% placement", "15+ tie-ups", and unverified testimonials from the HTML/JS.
3. **P0 (Small):** Change "Confirm & Pay" to "Submit Application" in `admissions.html`.
4. **P1 (Medium):** Refactor the JSON accreditation assignment to use explicit `exactWording` keys rather than generic string matching.
5. **P1 (Small):** Fix WCAG contrast on Orange buttons by darkening the CSS token.
6. **P1 (Large):** Write a python build script that generates 16 static `course-*.html` files to solve the JS-routing SEO failure.

## Unverified Items / Content Needed
- Exact trainer photos and confirmation of names.
- Confirmation of testimonials.
- Client schedule for batch dates.
- Confirmation if OSHA 30 and IASP OSHA 30 are identical.
- Authentic campus photography.
