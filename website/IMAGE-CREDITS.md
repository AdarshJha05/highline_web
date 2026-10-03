# Image credits & replacement notes

All photography in `assets/img/` is **placeholder stock**. Swap it for High Line's
own photography before launch — the shot briefs from the original design handoff
are listed below so you know what each slot is meant to show.

## Where each image came from

**Client-supplied (the ten Pinterest links).** These are the primary imagery and
cover the most prominent slots:

| File | Slot | Source |
|---|---|---|
| `hero-home.jpg`, `fac-drillyard.jpg`, `sched-drill.jpg`, `campus-t2.jpg` | Home hero, drill-yard tile, Tuesday thumb, campus thumb | client `u5` |
| `hero-about.jpg`, `campus-main.jpg` | About hero, campus main | client `u1` |
| `course-adhse.jpg` | ADHSE course card | client `u2` |
| `course-dfs.jpg` | DFS course card | client `u3` |
| `course-og.jpg` | Oil & Gas course card | client `u4` |
| `event-photo.jpg`, `ach-1.jpg` | Events photo, achievements main | client `u6` |
| `cta-yard.jpg` | Home admissions band | client `u8` |
| `faq-promo.jpg` | Home FAQ promo panel | client `u9` (cropped to the helmet — the poster's baked-in "COURAGE / COMPASSION / COMMITMENT" tagline was cropped out so it doesn't fight the overlaid copy) |
| `course-iosh.jpg`, `fac-classroom.jpg` | IOSH course card, classroom tile | client `u10` |

**Not used: `u7`.** That file is a Vecteezy comp — the watermark is tiled across
the whole image. Buy the licensed version if you want it; the About CTA band
currently uses a public-domain alternative.

**Sourced to fill the gaps.** Everything else came from Wikimedia Commons or
Openverse, filtered to licences that allow commercial use and modification:

| File | Licence |
|---|---|
| `about-cta.jpg`, `fac-smoke.jpg`, `contact-photo.jpg`, `blog-2.jpg`, `testi-photo.jpg` | Public domain (US government works) |
| `hero-contact.jpg`, `story-1.jpg`, `ach-2.jpg`, `ach-3.jpg` | CC BY 2.0 / public domain |
| `course-cis.jpg` | CC BY-SA (Raimond Spekking, Wikimedia Commons) |
| `course-nebosh.jpg`, `campus-t1.jpg` | CC0 / public domain |
| `story-2.jpg`, `blog-1.jpg`, `blog-3.jpg`, `faq-cta.jpg` | CC BY 2.0 (Flickr) |
| `campus-t3.jpg`, `footer-tile.jpg` | CC0 (StockSnap) |

> **Before you go live:** CC BY and CC BY-SA require crediting the photographer.
> If you keep any of those files, complete the attribution line for each, or
> replace them with High Line's own photos — which is the intent anyway.

## Trainer portraits

The six trainer cards on `about.html` render **brand monogram plates**, not
photographs. Using a stranger's stock portrait under a named staff member's
byline would misrepresent a real person, so that was deliberately avoided.

Replace each `.member__mono` block with a real photo when the portraits arrive:

```html
<article class="member">
  <img class="ph" src="assets/img/team-rafiuddin.jpg" alt="Mohammed Rafiuddin">
  <div class="member__plaque"><b>Mohammed Rafiuddin</b><span>Managing Director</span></div>
</article>
```

Shoot brief from the handoff: shoulders-up portrait, navy polo, light-blue
background. Export at roughly 700 × 1000 px.

## Remaining shot briefs

Slots still carrying a generic stand-in, in rough priority order:

1. `campus-main.jpg` — the campus building exterior with High Line signage.
2. `testi-photo.jpg` — a real graduate holding their certificate, blue lanyard.
3. `ach-2.jpg` / `ach-3.jpg` — batch ceremony, and a gear/equipment close-up.
4. `blog-1..3.jpg` — hose handling, certification documents, safety officer on site.
5. `footer-tile.jpg` — orange safety helmet on a blue painted floor, shot top-down.

## Re-cropping

Images are pre-cropped to the box each slot renders at, and every slot uses
`object-fit: cover`, so a drop-in replacement at a similar aspect ratio will
work without touching the CSS. Rough target sizes are in the table above; the
largest is `hero-*` at ~2000 px wide.
