# Handoff: High Line Fire & Safety Website (Home, About, Contact)

## Overview
A 3-page marketing website for **High Line Fire and Safety Training Institute**, Karimnagar, Telangana (fire & safety training: DFS, ADHSE, IOSH, NEBOSH, Construction & Oil/Gas safety diplomas). Pages: **Home** (hero, accreditations marquee, values, courses, facilities, schedule, events, admissions CTA form, fees, testimonials, blog, FAQ), **About** (vision/mission, story + stats, learning paths, CTA, trainers, achievements timeline, campus), **Contact** (inquiry form, map, contact cards, categorized FAQ). Shared **SiteNav** and **SiteFooter** components.

## About the Design Files
The files in `design_files/` are **design references created in HTML** — prototypes showing intended look and behavior, not production code to ship directly. Your task is to **recreate these designs in the target codebase's existing environment** (React, Vue, Next.js, etc.) using its established patterns and libraries. If no environment exists yet, choose an appropriate framework (a static-friendly React/Next.js setup fits well) and implement the designs there.

Notes on the prototype format:
- Each `.dc.html` opens in a browser via the bundled `support.js` runtime. Markup lives between `<x-dc>…</x-dc>`; interactive logic is a `Component` class in the `<script data-dc-script>` tag at the bottom (React-class-like: `state`, `setState`, `renderVals()` feeds `{{ holes }}` in the markup, `componentDidMount`).
- `<image-slot id="…" placeholder="…">` elements (from `image-slot.js`) are **image placeholders** — each `placeholder` attribute describes the intended photo. Replace with real photography.
- `<dc-import name="SiteNav">` / `<dc-import name="SiteFooter">` mount the shared components.
- `<sc-for>` / `{{ … }}` are template loops/holes — read them as `.map()` over the data arrays defined in the logic class.

## Fidelity
**High-fidelity.** Colors, typography, spacing, copy, and interactions are final. Recreate pixel-perfectly, using exact values below. The only non-final elements are the photo placeholders (`<image-slot>`) — real photography needed — and fee amounts (marked "indicative" in the UI).

## Design Tokens

### Colors
| Token | Hex | Use |
|---|---|---|
| Ink | `#14181D` | Primary text, dark avatar chips |
| Body text muted | `#5B6672` | Secondary text, eyebrows |
| Muted deep | `#3D5568` | Secondary text on light-blue surfaces |
| Faint text | `#8B96A2` | Fine print, metadata |
| Disabled num | `#9AA6B2` | Inactive FAQ numbers |
| Marquee gray | `#A7B4C2` | Accreditation marquee wordmarks |
| Page background | `#EDF3F9` | Body bg, input fills |
| Card white | `#FFFFFF` | Section cards, pills |
| Surface tint | `#F6FAFD` | Sub-cards, FAQ rows |
| Border light | `#E4EDF5` | Card borders |
| Border mid | `#C6D6E4` | Outlined buttons |
| Blue 100 | `#D6E9FA` | Highlight cards, secondary buttons |
| Blue 300 | `#8FC1EE` | Highlight-card borders |
| Brand blue | `#2E8FE0` | Primary accent, icon circles, gradients |
| Brand blue deep | `#1E7CCF` | Links, hover, gradient end |
| Blue darker | `#1668B8` / `#175A9E` | SVG gradients, hero overlay |
| Accent orange | `#F4581C` | Stars, brand accent, wordmark, dots |
| Orange range | `#FF9354` → `#E04A10` etc. | Vector-art gradients only |

Hero/CTA gradients: `linear-gradient(160deg,#2E8FE0,#1E7CCF)` (hero), `linear-gradient(140deg,#2E8FE0,#1E7CCF)` (CTA bands). Hero photo overlay: `linear-gradient(to top, rgba(23,90,158,.88) 0%, rgba(46,143,224,.28) 48%, rgba(30,124,207,.30) 100%)`.

### Typography
- Font: **Hanken Grotesk** (Google Fonts), weights 400/500/600/700/800. `-webkit-font-smoothing: antialiased`.
- H1 hero: 82px (Home) / 72px (About, Contact), weight 500, line-height 1.03–1.05, letter-spacing −.025em, white.
- H2 section: 44–48px, weight 500, letter-spacing −.02em, line-height 1.1.
- Lead paragraphs: 26–30px, weight 500, line-height 1.4–1.5, letter-spacing −.015em.
- Eyebrow label: 12px, weight 700, letter-spacing .16em, uppercase, `#5B6672` (white on photos), preceded by a 6px dot (`#2E8FE0`, or `#F4581C` on heroes).
- Card titles: 18–21px weight 700. Body: 13.5–15px, line-height 1.55–1.65, `#5B6672`.
- Big stats: 52px/800 (About), 38px/800 (prices), 20px/800 (mini stats). Footer giant wordmark: `17.5vw`, weight 800, `#F4581C`, centered, `white-space: nowrap` inside `overflow: hidden`.

### Spacing & Shape
- Page gutter: 16px; section cards inset `margin: 0 16px`, white bg, radius 28px, padding `100px 64px`. Open sections: padding `120px 64px 110px`.
- Card radii: 28 (sections) / 24 (cards) / 18–20 (inner tiles, inputs) / 999px (pills, buttons).
- Grids: 3-col course/fees/blog grids, gap 24px. Content max widths noted inline.
- Shadows: card `0 2px 4px rgba(20,50,90,.04), 0 14px 34px rgba(30,124,207,.07)`; hover `0 28px 56px rgba(30,124,207,.16)`; floating hero badges `0 20px 50px rgba(17,58,96,.25)`; CTA white panel `0 40px 90px rgba(12,48,84,.35)`.

### Buttons
- **Primary pill**: white bg (or `#D6E9FA`), radius 999px, padding `9px 9px 9px 22px`, 14px/600 text, trailing 32px circle (`#2E8FE0` blue with white `↗`, or white circle on tinted buttons).
- **Outlined pill**: 1px `#C6D6E4` border, hover fills `#D6E9FA` + border `#8FC1EE`.
- Carousel arrows: 44px circles — outlined (prev) and solid `#2E8FE0` (next).

## Calymorphism Vector Art (signature element)
Decorative "clay-style" SVG illustrations appear generously across the site: flame, shield-with-check, extinguisher, helmet (hero cluster); ribbon badge, graduation cap, cone, whistle, checklist, bell, alarm clock, rupee coins, quote bubble, open book, question ball. Style rules:
- Soft rounded forms, vertical/diagonal gradients (blues `#7FBCF0→#1668B8`, oranges `#FF9354→#E04A10`), white elliptical highlight at ~.3–.45 opacity, drop-shadow filter `drop-shadow(0 14–26px 16–30px rgba(9,40,72,.4))` or `rgba(30,124,207,.25)`.
- Gentle float animations (keyframes `hlFloatA/B/C`): translateY −9 to −16px, some with slight rotation, 5–7.5s ease-in-out infinite, staggered delays.
- All decorative SVGs are `pointer-events: none`.
- **Exclusion:** the Home admissions CTA band (`#cta-yard` section) intentionally has **no** vector art. Exact SVG paths are in the design files — copy them verbatim.

## Screens / Views

### 1. Home (`design_files/Home.dc.html`)
1. **Hero** — 790px rounded (28px) panel, blue gradient + full-bleed photo slot + overlay. Nav overlaid on top. Left-bottom: 82px H1 "Building Safety Careers Beyond the Classroom"; below it "Explore Courses" white pill (→ `#courses`) + "Scroll Down ↓". Right-bottom: orange-dot eyebrow "FIRE & SAFETY TRAINING" + short blurb (max 360px). Right-top: floating white glass badge (blur 8px) with 3 stacked 30px avatar initials (DB/SK/MR, −9px overlap, 2px white borders) + "500+ Students Trained"; below it a frosted pill "ISO 9001:2015 · IBSP · IOSH". Vector cluster right-of-center (flame, shield, extinguisher) + helmet at left-top.
2. **Accreditations marquee** — centered ribbon-badge SVG + eyebrow "TRUSTED ACCREDITATIONS"; infinite leftward marquee (30s linear, duplicated list, pauses on hover) of gray wordmarks: ISO 9001:2015, IBSP, IOSH, NEBOSH, High Line Institute.
3. **Core Values** (white section card) — eyebrow + 30px lead with blue-highlighted words; 3-col grid: (a) "Safety Mindset" stat card with animated line-draw SVG chart (stroke-dasharray 420, 2.2s) and 96% / 10+ / 4 stats; (b) blue `#D6E9FA` card with inline 28px avatar stack in the sentence + whistle SVG + "Team Discipline ↗" row; (c) photo tile with frosted check-pills ("Character Training", "Practical Drills", "Team Coordination").
4. **Courses** (`id="courses"`) — centered header + grad-cap and cone SVGs at the sides. 3×2 grid of course cards: white, radius 24, padding `14px 14px 22px`, photo (208px, radius 18), title + 24px avatar trio, description, hover state (bg `#D6E9FA`, border `#8FC1EE`, translateY −6px, big shadow) which also **expands a hidden "View Course Details" pill** (height 0→52px, .35s cubic-bezier(.22,1,.36,1)); footer meta "Tag • Tag". Courses: DFS, ADHSE, IOSH Managing Safely, Construction & Industrial Safety, NEBOSH IGC, Oil & Gas Safety (full copy in file). Below: "★ 4.9 Rated by our graduates" pill, "View All Courses" button, prev/next arrows (decorative).
5. **Facilities** (white section) — header; grid `380px 1fr`: left card with intro, 4 ✓-rows, clipboard SVG, "Tour the Campus" button; right 2×2 photo grid (280px + 220px rows, third tile spans both columns) with frosted labels ("Practical Drill Yard", "Smoke Chamber", "Modern Classrooms & PPE Lab" — labels have `margin-left:60px`).
6. **Schedule** — centered header with alarm-clock SVG; 6 rows (max-width 1180px): day pill (110px), bold title with blue • separator, ⏱ time · location line, "View Location" outlined button (→ Contact). Tuesday row is highlighted (`#D6E9FA` bg, `#8FC1EE` border) and includes an 84×60 photo thumb.
7. **Events** (white section) — grid `430px 1fr`. Left: header, 240px photo, blurb. Right: featured blue card "New DFS Batch — Admissions Open" with bell SVG, 2×2 meta grid (STARTS September 2026 / LOCATION Karimnagar Campus / DURATION 12 months / SEATS Limited — 30 per batch), "Join the Batch" button; below, 3 accordion rows (Mock Drill Day, Placement Drive, NEBOSH Exam Window) toggling +/− with max-height transition.
8. **Admissions CTA** (`#cta-yard`) — 640px photo band (blue gradient fallback), gradient overlay, left-aligned white panel (max 640px, radius 26, padding 44/48): eyebrow ADMISSIONS, 34px H2, 2-col form (Full Name, Email, Phone, Age, Education Level select, Preferred Course select — inputs: `#EDF3F9` fill, radius 12, padding 13/16, no border), fine print + "Register Now" button. **No vector art here.**
9. **Fees** (`id="fees"`) — centered header with rupee-coin SVG; 3 pricing cards: Certificate Track ₹15,000 (Beginner), Diploma Track ₹45,000 (Most Popular — blue card, blue badge), International Track ₹85,000 (Advanced). Each: ✓ feature list, price above 1px divider, "Choose This Track" button. Copy states fees are indicative.
10. **Testimonials** (white section) — quote-bubble SVG top-right; header; grid `400px 1fr`: photo with frosted role/"Placed" pills (offset `margin-left:56px`); right column: "4.9" + orange ★★★★★ + giant `”` in `#D6E9FA`; 26px quote (min-height 160px), name/role; 10 clickable 44px avatar-initial dots (active: 2px `#2E8FE0` border, full opacity; inactive .55) + prev/next buttons cycling `state.t`.
11. **Blog** (`id="blog"`) — centered header with open-book SVG; 3 article cards (photo 200px + frosted category chip, title, excerpt, "High Line Team • N min read").
12. **FAQ** (white section) — grid `1fr 380px`. Left: header + question-ball SVG; 5 accordion rows (numbered 01–05, active number blue, +/− circle, max-height transition; first open by default). Right: promo photo panel (min 520px) with dark-blue bottom gradient, "500+ Students Trained" chip, "Let's Talk Safety" 32px, "Contact Our Team" button.
13. **Footer** import.

### 2. About (`design_files/About.dc.html`)
1. **Hero** — 560px, same pattern; H1 72px "Developing the Next Safety Leaders" (max-width `min(700px, calc(100% - 500px))` to avoid nav/blurb overlap); right-bottom eyebrow "ABOUT HIGH LINE" + blurb.
2. **Vision & Mission** — centered header; 3 cards: blue vision card (sentence embeds the 30px round logo image), white "Safety Career Growth Index" chart card (line-draw animation + 90% / 96% stats), blue mission card with 3 `+` rows.
3. **Our Story** (white section) — grid `1fr 420px`: eyebrow, 29px lead, 2×2 animated counters (500+, 10+, 15+, 4 — count up 1.4s ease-out cubic on scroll into view), paragraph, "Explore Our Courses" button; right: two photos (250px, 290px). Below: 4 learning-path cards — 01 BEGINNER Foundations, 02 INTERMEDIATE Practical Drills, 03 ADVANCED HSE Management, 04 MASTERY Global Certification (04 is blue-tinted).
4. **CTA band** — 520px photo band, centered white panel: "Start Your Safety Career with High Line", "Contact Our Team" button + mailto link.
5. **Trainers** — centered header; 3-col grid of 6 photo cards (400px, hover translateY −6px) with frosted name/role plaques: Mohammed Rafiuddin (Managing Director), Sheik Junaidh (Director of Academic Studies), Badhra (NEBOSH Trainer), Mohammed Shahid (Manager), Ajay (Sr. Administrator), Saniya Mahreen (Co-Ordinator).
6. **Achievements** (white section) — grid `440px 1fr`: header, year chips 2021–2026 (active: blue tint/border; clicking swaps title+description; 2026 default), disclaimer line; right: photo collage (430px tall main + two stacked).
7. **Campus** — centered header; white card grid `1.25fr 1fr`: photos (340px main + 3× 110px thumbs) | contact details (✉ email, ✆ phones, ⌖ address), embedded OpenStreetMap iframe (marker 18.4386, 79.1288), "Plan a Campus Visit" button.
8. **Footer** import.

### 3. Contact (`design_files/Contact.dc.html`)
1. **Hero** — 520px; H1 "Ready to Train at High Line?"; eyebrow "GET IN TOUCH" + blurb.
2. **Inquiry form** — grid `440px 1fr`: photo panel (min 560px) with frosted pills (top: "ISO 9001:2015 Certified", "Fire & Safety Institute"; bottom center: ✓ Accredited Trainers / ✓ Placement Assistance / ✓ Practical Drill Training) | form: 44px H2 "Take Your Career Further", 2-col inputs (Name, Email, Phone, Course select; full-width Message textarea — white fill on the `#EDF3F9` page bg), "Send Course Inquiry" button.
3. **Contact info** (white section) — centered header; 400px OSM map iframe; 3 centered cards: ✉ email, ✆ phones (+91 812 111 8000 · +91 93928 82152, WhatsApp link `wa.me/919392882152`), ⌖ address (Beside Geetha Bhavan, opp. Jafri Masjid, Karimnagar – 505001).
4. **FAQ** — grid `1fr 360px`: 4 accordion rows driven by category; right rail: 3 category chips (Training Courses / Admissions / Institute Details — switching resets open row to 0) + promo photo card with avatar stack and "Explore Our Courses" button. All FAQ copy is in the file's `catData`.
5. **Footer** import.

### SiteNav (`design_files/SiteNav.dc.html`)
Overlaid on hero photos (transparent bg, white text). Left: About / Courses / Blog / Contact links (active page gets white pill bg + dark text; 14px/500, padding `9px 18px`). Center (absolute): 42px white circle with the logo webp + stacked wordmark "High Line" (17px/800 white) over "FIRE & SAFETY" (8px/700, letter-spacing .24em). Right: decorative frosted "Search here" pill (non-functional) + "Get in Touch" white pill (hover `#D6E9FA`). Takes an `active` prop: home|about|courses|blog|contact.

### SiteFooter (`design_files/SiteFooter.dc.html`)
White rounded card: 210px photo tile | brand row (36px logo + "High Line **Fire & Safety**" with orange accent), 27px mission line, newsletter (rounded input + "Subscribe" `#D6E9FA` button) | Quick Links 2-col (Home, Courses, About Us, Blog, Contact, Fees) + Social (Facebook, Instagram, LinkedIn, WhatsApp — all `highlinefireandsafety` handles) + © 2026 line. Below the card: giant `17.5vw` orange "HighLine" wordmark (single line, clipped container — must never wrap or clip vertically). Bottom bar: email · phones · address, split by a hairline `rgba(20,24,29,.06)` top border.

## Interactions & Behavior
- **Scroll-reveal**: every `[data-reveal]` element starts `opacity:0; translateY(24px)`; IntersectionObserver (threshold .12, rootMargin `0px 0px -5%`) reveals with `.7s cubic-bezier(.22,1,.36,1)`, staggered `(index % 3) * 90ms`. Observe once.
- **Accordions** (FAQ, events): one open at a time per group; open = `max-height 220px / opacity 1`, closed = `0 / 0`; `.5s`/`.35s` cubic-bezier(.22,1,.36,1); icon toggles + / −.
- **Course card hover**: bg/border/lift/shadow change + reveal of "View Course Details" pill (height 0→52px, margin-top 0→16px).
- **Testimonial carousel**: 10 entries (all names/quotes in `Home.dc.html` `testiData`); avatar dots select; prev/next wrap modulo 10.
- **Achievements year picker** (About): 6 entries in `achData`; chip click swaps content.
- **FAQ category chips** (Contact): swap FAQ set, reset open index to 0.
- **Counters** (About): count 0→target over 1.4s with ease-out cubic on first scroll into view.
- **Marquee** (Home): 30s linear infinite `translateX(0 → −50%)` on a duplicated list; pause on hover.
- **Float animations**: vector art floats per the keyframes in each file's `<style>`.
- Buttons/links route between the three pages (in production: `/`, `/about`, `/contact`, plus `#courses`, `#fees`, `#blog` anchors on Home).
- Forms are **visual only** — no submit handling designed. Wire to your backend; keep placeholder copy and select options as-is.
- Responsive behavior was **not designed** (desktop 1440px+ reference; mobile reference JPGs exist in the original project uploads). Plan mobile layouts with the client.

## State Management
Per page (see logic classes for exact shapes):
- Home: `hov` (hovered course index), `faq` (open FAQ index, default 0), `ev` (open event index, default −1), `t` (testimonial index).
- About: `yr` (achievement year index, default 5 → 2026).
- Contact: `cat` (FAQ category, default 0), `faq` (open row, default 0).
- No data fetching; all content is static arrays in the files.

## Assets
- `assets/highlinebiglogo-Transparent-Copy-150x150.webp` — the only real asset (client logo; referenced as `uploads/…` in the prototypes). Used in nav, footer, and About vision card.
- All photos are `<image-slot>` placeholders; each `placeholder` attribute is a shot brief (e.g. "trainees in navy coveralls & orange helmets performing a live fire extinguisher drill"). Source real photography from the client.
- Maps: OpenStreetMap embed iframes centered on the Karimnagar campus (18.4386, 79.1288). Swap for your preferred map provider if needed.
- Fonts: Hanken Grotesk from Google Fonts (400–800).
- All decorative SVGs are inline in the files — copy paths verbatim.

## Files
- `design_files/Home.dc.html` — home page (open in a browser to preview)
- `design_files/About.dc.html` — about page
- `design_files/Contact.dc.html` — contact page
- `design_files/SiteNav.dc.html` — shared nav component
- `design_files/SiteFooter.dc.html` — shared footer component
- `design_files/support.js`, `design_files/image-slot.js` — prototype runtime (not for production; needed only to preview the HTML files)
- `assets/highlinebiglogo-Transparent-Copy-150x150.webp` — client logo
