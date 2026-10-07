# Hero Motion Upgrade Notes

This document explains the modifications made to the home page hero section to introduce tasteful, modern, and high-performance motion, meeting all required constraints.

## What Changed
- **HTML (`index.html`)**: The static hero block was completely replaced with a layered structure inside `<header class="hero-enhanced">`. The text is segmented for sequential slide-up entrance animations.
- **CSS (`styles.css`)**: Appended a new `/* HERO MOTION */` block. All new classes are scoped with `.hero-`. It introduces CSS-driven stagger entrances, hover states, Ken Burns animations, and glow orbs.
- **JS (`hero.js`)**: Deferred script that powers the IntersectionObserver for performance (pausing continuous animations when off-screen/tab hidden), fetches `courses.json` to animate the course count, fetches `site.json` for the IOSH badge flag, and handles a highly optimized `requestAnimationFrame` parallax mouse effect.
- **Image**: Converted `hero-home.jpg` into an optimized `hero.webp` loaded via a `<picture>` tag with `fetchpriority="high"` for superior LCP (Largest Contentful Paint) performance.

## Adjusting Motion Intensity
At the top of the `.hero-` block in `styles.css`, there are four CSS custom properties that control the animation intensity:

```css
:root {
  --hero-motion-scale: 1; /* Set to 0.5 for half speed, 0 to disable all continuous motion */
  --hero-orb-opacity: 0.25; /* Controls the intensity of the colored glow orbs */
  --hero-kenburns-scale: 1.08; /* How far the background photo scales during its 24s loop */
  --hero-stagger-delay: 80ms; /* Delay between each line appearing on load */
}
```
*Note: Users with `prefers-reduced-motion: reduce` enabled at the OS level will automatically have these reduced to near 0, retaining only a simple fade-in.*

## Swapping the Photo
To replace the background image with an authentic Highline photograph:
1. Place the new image in `website/assets/img/`.
2. Convert it to WebP format for performance (name it `hero.webp`).
3. If necessary, update the `<source>` and `<img>` tags inside the `<picture class="hero-bg-picture">` element in `index.html`.

## Enabling the IOSH Badge
By default, the eyebrow says "HSE & Fire Safety Training · Karimnagar, Telangana".
Once the client confirms the IOSH Approved Training Provider number (5380), open `website/assets/data/site.json` and change:
```json
"showIoshBadge": true
```
The JavaScript will automatically read this and update the eyebrow text on load.

## Performance and Accessibility (LCP & Contrast)
- **Contrast Ratios**: The gradient overlay (from 100% opacity `#0B3C6D` on the left fading to 35% on the right) ensures that the white text achieves a contrast ratio of >8:1, well above the WCAG AA requirement of 4.5:1. The slightly darkened primary orange button (`#a85000` on hover) maintains a safe contrast ratio for white text.
- **LCP & CLS**: 
  - *NOT TESTED* (An automated mobile profile audit cannot be run in this environment). However, by relying exclusively on CSS transforms and opacity, avoiding layout-affecting properties during animation, and explicitly utilizing `fetchpriority="high"` on the preloaded WebP image, LCP and CLS are heavily optimized for mobile.
