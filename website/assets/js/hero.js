document.addEventListener('DOMContentLoaded', () => {
  const heroWrapper = document.getElementById('hero-wrapper') || document.querySelector('.hero-enhanced');
  if (!heroWrapper) return;

  const bgImg = document.getElementById('hero-bg-img');
  const orbOrange = document.getElementById('hero-orb-orange');
  const orbTeal = document.getElementById('hero-orb-teal');
  const highlightWrap = document.querySelector('.hero-highlight-wrap');
  const eyebrowWrapper = document.querySelector('.hero-eyebrow-wrapper');
  const floatWa = document.querySelector('.float-wa');
  const scrollCue = document.getElementById('hero-scroll-cue');
  
  // Motion preferences
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1. Fetch site.json for IOSH badge logic
  fetch('assets/data/site.json')
    .then(res => res.json())
    .then(data => {
      if (data.showIoshBadge) {
        const eyebrowText = document.getElementById('hero-eyebrow');
        if (eyebrowText) eyebrowText.innerHTML = 'IOSH Approved Training Provider (No. 5380)';
      }
    })
    .catch(err => console.warn('Failed to fetch site.json', err));

  // 2. Fetch courses.json for metrics
  let courseCountTarget = 0;
  fetch('assets/data/courses.json')
    .then(res => res.json())
    .then(data => {
      if (data && data.length > 0) {
        courseCountTarget = data.length;
        const countEl = document.getElementById('hero-course-count');
        const labelEl = document.getElementById('hero-course-label');
        if (countEl && labelEl) {
          countEl.textContent = '0';
          labelEl.textContent = ' programmes';
        }
      }
    })
    .catch(err => console.warn('Failed to fetch courses.json', err));

  // 3. Counter Animation (Runs once when hero enters)
  function animateCounter(el, target) {
    if (prefersReducedMotion) {
      el.textContent = target;
      return;
    }
    let start = 0;
    const duration = 900;
    const startTime = performance.now();
    function updateCount(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out quint
      const easeOut = 1 - Math.pow(1 - progress, 5);
      const current = Math.floor(easeOut * target);
      el.textContent = current;
      if (progress < 1) {
        requestAnimationFrame(updateCount);
      } else {
        el.textContent = target;
      }
    }
    requestAnimationFrame(updateCount);
  }

  // 4. Entrance & Intersection Observer
  let hasEntered = false;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (!hasEntered) {
          hasEntered = true;
          heroWrapper.classList.add('is-entered');
          
          if (!prefersReducedMotion) {
            if (highlightWrap) setTimeout(() => highlightWrap.classList.add('is-animating'), 900);
            if (eyebrowWrapper) eyebrowWrapper.classList.add('is-animating');
            if (courseCountTarget > 0) {
              const countEl = document.getElementById('hero-course-count');
              setTimeout(() => animateCounter(countEl, courseCountTarget), 500);
            }
          }
        }
        // Resume continuous animations
        if (!prefersReducedMotion) {
          if (bgImg) bgImg.classList.add('is-animating');
          if (orbOrange) orbOrange.classList.add('is-animating');
          if (orbTeal) orbTeal.classList.add('is-animating');
          if (floatWa) floatWa.classList.add('is-animating');
        }
      } else {
        // Pause continuous animations
        if (bgImg) bgImg.classList.remove('is-animating');
        if (orbOrange) orbOrange.classList.remove('is-animating');
        if (orbTeal) orbTeal.classList.remove('is-animating');
        if (floatWa) floatWa.classList.remove('is-animating');
      }
    });
  }, { threshold: 0.1 });
  
  observer.observe(heroWrapper);

  // Tab visibility pauses continuous animations
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      if (bgImg) bgImg.classList.remove('is-animating');
      if (orbOrange) orbOrange.classList.remove('is-animating');
      if (orbTeal) orbTeal.classList.remove('is-animating');
      if (floatWa) floatWa.classList.remove('is-animating');
    } else {
      // Re-evaluate intersection? The easiest is just trusting the observer will re-fire or we only re-add if it's currently intersecting.
      // A quick cheat: just check bounding client rect.
      const rect = heroWrapper.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0 && !prefersReducedMotion) {
        if (bgImg) bgImg.classList.add('is-animating');
        if (orbOrange) orbOrange.classList.add('is-animating');
        if (orbTeal) orbTeal.classList.add('is-animating');
        if (floatWa) floatWa.classList.add('is-animating');
      }
    }
  });

  // 5. Scroll cue fade out
  if (scrollCue) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 80) {
        scrollCue.classList.add('is-hidden');
      } else {
        scrollCue.classList.remove('is-hidden');
      }
    }, { passive: true });
  }

  // 6. Parallax effect
  const isFinePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (isFinePointer && !prefersReducedMotion) {
    let targetX = 0;
    let targetY = 0;
    let currentX = 0;
    let currentY = 0;
    const maxShift = 12; // 12px max shift

    document.addEventListener('mousemove', (e) => {
      const centerX = window.innerWidth / 2;
      const centerY = window.innerHeight / 2;
      targetX = ((e.clientX - centerX) / centerX) * maxShift;
      targetY = ((e.clientY - centerY) / centerY) * maxShift;
    }, { passive: true });

    function renderParallax() {
      // smooth lerp
      currentX += (targetX - currentX) * 0.05;
      currentY += (targetY - currentY) * 0.05;
      
      // Update layers
      if (bgImg) bgImg.style.transform = `translate(${currentX * -0.5}px, ${currentY * -0.5}px)`;
      if (orbOrange) orbOrange.style.transform = `translate(${currentX * 1.5}px, ${currentY * 1.5}px)`;
      if (orbTeal) orbTeal.style.transform = `translate(${currentX * -1.2}px, ${currentY * -1.2}px)`;

      requestAnimationFrame(renderParallax);
    }
    requestAnimationFrame(renderParallax);
  }
});
