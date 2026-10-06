# Content and Design Audit

This audit was conducted as part of Phase A to identify and document legacy template artifacts, unsupported claims, and content requiring verification before proceeding to a production-ready corporate website.

## 1. Placeholder-style Initials
Found across course cards, team sections, and testimonials:
- `DB`, `SK`, `MR`, `SJ`, `BD`, `MS`, `AJ`, `SM` used in `<span class="av">` tags.
- **Action**: Removing all anonymous placeholder avatars. Real photos or names must be supplied.

## 2. Stale Dates
- Hardcoded date found in the `events` section of `index.html`: `September 2026` for a DFS batch.
- **Action**: Removing hardcoded dates. Batch dates will be managed via `batches.json` in a future phase.

## 3. "Indicative" Prices
- `index.html` has a fees section with the disclaimer: "Indicative fees — confirm final pricing with the institute." and specific prices (e.g., ₹15,000, ₹45,000, ₹85,000).
- **Action**: Unapproved and "indicative" prices have been removed. We will either use approved exact fees or change the call-to-action to "Contact for current fee".

## 4. Unsupported Statistics and Claims
- **Stats**: "96% Placement support" in the hero section.
- **Claims**: "500+ students trained milestone" in `about.html`.
- **Promises**: "Campus placement drives" and "Placement assistance" mentioned in FAQ and course features.
- **Action**: Removed invented numbers. Mentions of placement drives are hidden/removed until verified by the institute.

## 5. Invented Testimonials
- The following testimonials appear to be template fillers: Dasari Balachander, Samanthula Sampath, Nyalam Prashanth, Nyalam Rajkumar, Mohammad Shamroz.
- **Action**: The testimonials section is hidden from the UI. It will be restored only when consented, verifiable testimonials are provided.

## 6. Accreditation Wording Issues
- The footer and meta tags claim: "ISO 9001:2015 Certified · IBSP Approved".
- The `content_needed.md` provided by the client lists: EOSH, IOSH Approved Training Provider 5380, and Bharat Sevak Samaj (TEL/9473).
- **Action**: Updated the global footer and meta tags to reflect the exact provided accreditations and removed unsupported ones.

## 7. Brand Spelling Inconsistency
- The codebase used `High Line` universally (e.g., `<title>`, `nav__word`, paragraph text).
- **Action**: Replaced all instances of `High Line` with `Highline` across all HTML files to ensure single brand spelling.

## 8. Generic Stock Imagery
- Discovered stock images like `assets/img/values-photo.jpg`, `assets/img/contact-photo.jpg`, `assets/img/course-nebosh.jpg`.
- **Action**: These are flagged for replacement. `CONTENT_NEEDED.md` requests authentic institute photography.

## 9. UI Implying Out-of-Scope Features
- Inspected the codebase for "portal", "login", "certificate verification", "app". No explicit UI found for these, but "Download Certificate" or similar concepts will be strictly avoided.
