# High Line Fire & Safety Training Institute — website

Three-page marketing site built from `design_handoff_highline_website/`.
Static HTML, CSS and vanilla JS — no build step, no dependencies.

```
website/
├── index.html          Home    (hero, marquee, values, courses, facilities,
│                               schedule, events, admissions, fees,
│                               testimonials, blog, FAQ)
├── about.html          About   (vision/mission, story, learning paths, CTA,
│                               trainers, achievements, campus)
├── contact.html        Contact (inquiry form, map, contact cards, FAQ)
├── assets/
│   ├── css/styles.css  All styling, tokens first, responsive layer last
│   ├── js/site.js      All behaviour, opt-in via data-attributes
│   ├── img/            34 photographs — see IMAGE-CREDITS.md
│   └── logo.webp
├── IMAGE-CREDITS.md    Licensing + what still needs real photography
└── README.md
```

## Running it

Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8000 --directory website
```

Deploying is a file copy — Netlify, Vercel, GitHub Pages, cPanel, S3, anything.

## Why static rather than React/Next

The handoff suggested a React/Next setup if no environment existed. For three
brochure pages with no data fetching and no shared state across routes, a build
step would add tooling and deploy friction without buying anything: the pages
render without JavaScript, first paint is a single request, and the client can
edit copy in the HTML directly. The nav and footer are duplicated in each page
(about 60 lines each) — that is the one cost, and it keeps the pages working
with JS disabled. If the site later grows a blog or CMS, moving this markup into
components is mechanical.

## Design fidelity

Colours, type scale, spacing, radii, shadows, copy and the clay-style SVG
illustrations are reproduced from the handoff at the 1440 px reference width.
All SVG paths were copied verbatim.

## Responsive behaviour (new — the prototypes were desktop-only)

Breakpoints: **1360 / 1180 / 1024 / 760 / 400**.

The significant decisions:

- **Nav** collapses to a hamburger drawer at ≤1024 px. The drawer is a real
  dialog: focus moves in, Escape closes it, background scroll locks. The
  decorative "Search here" pill is hidden below 1180 px.
- **Hero** is rebuilt below 1024 px. The desktop version pins the title, buttons
  and blurb to fixed offsets from the bottom of a fixed-height panel, which
  collides with itself on narrow screens; below the nav breakpoint the copy
  returns to normal flow and the panel grows to fit. Floating badges move to the
  left so the vector cluster keeps the top-right corner.
- **Courses** stay a 3 × 2 grid on desktop. At ≤760 px the grid becomes a
  scroll-snap rail and the prev/next arrows — decorative in the prototype —
  actually page it. Above 760 px the arrows are hidden rather than left inert.
- **Course card hover** reveals a "View Course Details" pill. Touch has no
  hover, so at ≤760 px the pill is always visible. The reveal also triggers on
  `:focus-within` for keyboard users.
- **Contact FAQ** is one grid with four flat children and named areas, so the
  category chips sit beside the heading on desktop and directly above the
  questions on mobile — no duplicated markup.
- Every split layout (facilities, events, story, achievements, campus, inquiry,
  FAQ) collapses to a single column at 1024 px; three-column grids go to two at
  1024 px and one at 760 px.

## Fixes applied to the design

Things that were wrong or unfinished in the prototypes:

- Core Values photo tile — `.photo-tile .chip` matched the chips inside
  `.tile-stack` too, absolutely positioning them on top of each other. The
  "Practical Drills" / "Team Coordination" chips were stacked and clipped.
- Facilities and testimonial labels carried an arbitrary `margin-left: 60px` /
  `56px` that pushed them out of alignment with their tiles. Removed.
- The footer's "Social Media" heading had no space above it — the spacing rule
  only matched adjacent `<p>` elements, and a `<div>` sat between them.
- "Placements ↗" in the Safety Mindset chart was clipped by the SVG viewBox.
- Fee card prices wrapped mid-phrase ("· installments / available"); the
  qualifier now takes its own line on all three cards.
- The prev/next arrows next to "View All Courses" were decorative — see above.
- Forms had no submit handling. They now validate required fields and compose a
  pre-filled email to `highlinefireandsafety@gmail.com` rather than silently
  doing nothing. **Wire these to a real backend when one exists** — see below.

## Wiring the forms to a backend

Three forms post nowhere today: admissions (`index.html`), inquiry
(`contact.html`) and the newsletter (footer, all pages). Each has
`data-mailto` / `data-newsletter` and is handled in `site.js` under `forms()`.

To switch to a real endpoint, replace the `window.location.href = href` line
with a `fetch()` POST. Every field already carries `name` and `data-label`, so
the payload builds itself.

## Accessibility

Skip link; landmark elements; `aria-current` on the active nav item; accordions
are `<button>`s with `aria-expanded`; the testimonial picker is a tablist with
per-graduate labels; year and category chips use `aria-pressed`; decorative SVG
is `aria-hidden` and `pointer-events: none`; visible focus rings; and
`prefers-reduced-motion` disables the float, marquee, reveal and counter
animations.

## Known gaps

- **Maps** are OpenStreetMap embeds. They did not paint tiles inside the sandbox
  used to build this — check them in a normal browser, and swap for Google Maps
  if you prefer.
- **Photography** is placeholder stock; trainer cards render monogram plates,
  not portraits. See `IMAGE-CREDITS.md`.
- **Fees** (₹15,000 / ₹45,000 / ₹85,000) are marked indicative in the copy, per
  the handoff. Confirm before launch.
- **Blog articles** are cards only — there are no article pages behind them yet.
- `canonical` / `og:url` point at `https://highlinefireandsafety.com/`. Update
  if the real domain differs.
