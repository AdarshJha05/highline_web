/* High Line Fire & Safety — shared behaviour for all three pages.
   Every widget is opt-in via a data attribute, so one file serves every page. */
(function () {
  'use strict';

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------- scroll reveal */
  function reveal() {
    var els = $$('[data-reveal]');
    if (!els.length) return;
    if (reduced || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        var d = (parseInt(e.target.dataset.reveal, 10) % 3) * 90;
        setTimeout(function () { e.target.classList.add('is-in'); }, d);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* --------------------------------------------- SVG line-draw on first view */
  function charts() {
    var els = $$('[data-draw]');
    if (!els.length) return;
    if (reduced || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-drawn'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        e.target.classList.add('is-drawn');
      });
    }, { threshold: 0.35 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------- counting numbers */
  function counters() {
    var els = $$('[data-count]');
    if (!els.length) return;
    var run = function (el) {
      var target = parseInt(el.dataset.count, 10);
      var suffix = el.dataset.suffix || '';
      if (reduced) { el.textContent = target + suffix; return; }
      var start = performance.now();
      var tick = function (now) {
        var p = Math.min(1, (now - start) / 1400);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if (!('IntersectionObserver' in window)) { els.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        run(e.target);
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------- accordions */
  /* One open row per [data-acc] group. Buttons carry aria-expanded; the body
     is the button's next sibling so the CSS sibling selector drives height. */
  function accordions() {
    $$('[data-acc]').forEach(function (group) {
      var buttons = $$('.acc', group);
      buttons.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var wasOpen = btn.getAttribute('aria-expanded') === 'true';
          buttons.forEach(function (b) {
            b.setAttribute('aria-expanded', 'false');
            b.nextElementSibling.classList.remove('is-open');
            var ico = $('.acc__ico', b);
            if (ico) ico.textContent = '+';
          });
          if (!wasOpen) {
            btn.setAttribute('aria-expanded', 'true');
            btn.nextElementSibling.classList.add('is-open');
            var ico = $('.acc__ico', btn);
            if (ico) ico.textContent = '−';
          }
        });
      });
    });
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function accMarkup(item, i, openIndex, plain) {
    var open = i === openIndex;
    return '' +
      '<div class="acc-item' + (plain ? ' acc-item--plain' : '') + '">' +
        '<button class="acc" type="button" aria-expanded="' + open + '">' +
          '<span class="acc__head">' +
            '<span class="acc__n">0' + (i + 1) + '</span>' +
            '<span class="acc__q">' + esc(item.q) + '</span>' +
            '<span class="acc__ico" aria-hidden="true">' + (open ? '−' : '+') + '</span>' +
          '</span>' +
        '</button>' +
        '<div class="acc__body' + (open ? ' is-open' : '') + '"><p>' + esc(item.a) + '</p></div>' +
      '</div>';
  }

  /* -------------------------------------------------- testimonial carousel */
  function testimonials() {
    var root = $('[data-testi]');
    if (!root) return;
    var data = window.HL_TESTIMONIALS || [];
    if (!data.length) return;

    var quote = $('[data-testi-quote]', root);
    var name = $('[data-testi-name]', root);
    var role = $('[data-testi-role]', root);
    var pill = $('[data-testi-pill]', root);
    var dots = $$('.testi__dot', root);
    var i = 0;

    function render() {
      var t = data[i];
      quote.textContent = t.quote;
      name.textContent = t.name;
      role.textContent = t.role;
      if (pill) pill.textContent = t.role;
      dots.forEach(function (d, n) {
        d.classList.toggle('is-active', n === i);
        d.setAttribute('aria-selected', String(n === i));
      });
    }
    dots.forEach(function (d, n) {
      d.addEventListener('click', function () { i = n; render(); });
    });
    var prev = $('[data-testi-prev]', root);
    var next = $('[data-testi-next]', root);
    if (prev) prev.addEventListener('click', function () { i = (i + data.length - 1) % data.length; render(); });
    if (next) next.addEventListener('click', function () { i = (i + 1) % data.length; render(); });
    render();
  }

  /* --------------------------------------------- achievements year picker  */
  function achievements() {
    var root = $('[data-ach]');
    if (!root) return;
    var data = window.HL_ACHIEVEMENTS || [];
    var chips = $$('.year', root);
    var title = $('[data-ach-title]', root);
    var desc = $('[data-ach-desc]', root);

    function pick(n) {
      chips.forEach(function (c, k) {
        c.classList.toggle('is-active', k === n);
        c.setAttribute('aria-pressed', String(k === n));
      });
      title.textContent = data[n].title;
      desc.textContent = data[n].desc;
    }
    chips.forEach(function (c, n) { c.addEventListener('click', function () { pick(n); }); });
    pick(data.length - 1);
  }

  /* ------------------------------------------- contact FAQ category switch */
  function faqCategories() {
    var root = $('[data-faqcat]');
    if (!root) return;
    var data = window.HL_FAQ_CATEGORIES || [];
    var chips = $$('.cat', root.closest('.faq-cat') || document);
    var list = $('[data-faqcat-list]', root.closest('.faq-cat') || document) || $('[data-faqcat-list]');

    function paint(n) {
      chips.forEach(function (c, k) {
        c.classList.toggle('is-active', k === n);
        c.setAttribute('aria-pressed', String(k === n));
      });
      list.innerHTML = data[n].faqs.map(function (f, i) {
        return accMarkup(f, i, 0, true);
      }).join('');
      // rebind the freshly written rows
      wireAccordionGroup(list);
    }
    chips.forEach(function (c, n) { c.addEventListener('click', function () { paint(n); }); });
    paint(0);
  }

  function wireAccordionGroup(group) {
    var buttons = $$('.acc', group);
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var wasOpen = btn.getAttribute('aria-expanded') === 'true';
        buttons.forEach(function (b) {
          b.setAttribute('aria-expanded', 'false');
          b.nextElementSibling.classList.remove('is-open');
          var ico = $('.acc__ico', b);
          if (ico) ico.textContent = '+';
        });
        if (!wasOpen) {
          btn.setAttribute('aria-expanded', 'true');
          btn.nextElementSibling.classList.add('is-open');
          var ico = $('.acc__ico', btn);
          if (ico) ico.textContent = '−';
        }
      });
    });
  }

  /* --------------------------------------------------------- courses rail  */
  /* On phones the 3x2 grid becomes a snap rail; the arrows page through it.
     On desktop the grid is static and the arrows are hidden by CSS. */
  function courseRail() {
    var rail = $('[data-rail]');
    if (!rail) return;
    var prev = $('[data-rail-prev]');
    var next = $('[data-rail-next]');
    var step = function () {
      var card = rail.querySelector('.course');
      return card ? card.getBoundingClientRect().width + 14 : rail.clientWidth * 0.85;
    };
    function sync() {
      if (!prev || !next) return;
      var max = rail.scrollWidth - rail.clientWidth - 2;
      prev.disabled = rail.scrollLeft <= 2;
      next.disabled = rail.scrollLeft >= max;
    }
    if (prev) prev.addEventListener('click', function () { rail.scrollBy({ left: -step(), behavior: 'smooth' }); });
    if (next) next.addEventListener('click', function () { rail.scrollBy({ left: step(), behavior: 'smooth' }); });
    rail.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  }

  /* ---------------------------------------------------------- mobile drawer */
  function drawer() {
    var burger = $('[data-burger]');
    var panel = $('[data-drawer]');
    if (!burger || !panel) return;

    function open() {
      panel.classList.add('is-open');
      burger.setAttribute('aria-expanded', 'true');
      document.body.classList.add('is-locked');
      var first = panel.querySelector('a, button');
      if (first) first.focus();
    }
    function close() {
      panel.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('is-locked');
    }
    burger.addEventListener('click', function () {
      panel.classList.contains('is-open') ? close() : open();
    });
    panel.addEventListener('click', function (e) {
      if (e.target === panel || e.target.closest('[data-drawer-close]') || e.target.closest('a')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('is-open')) { close(); burger.focus(); }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1024 && panel.classList.contains('is-open')) close();
    });
  }

  /* ------------------------------------------------------------------ forms */
  /* No backend ships with a static site, so a valid submission composes a
     pre-filled email to the institute rather than pretending to send. */
  function forms() {
    $$('form[data-mailto]').forEach(function (form) {
      var note = $('[data-note]', form);
      form.setAttribute('novalidate', '');
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var invalid = null;
        $$('[required]', form).forEach(function (f) {
          var bad = !f.value.trim() || (f.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value));
          f.closest('.field').classList.toggle('is-invalid', bad);
          if (bad && !invalid) invalid = f;
        });
        if (invalid) {
          if (note) {
            note.textContent = 'Please fill in the highlighted fields so we can get back to you.';
            note.classList.add('is-shown', 'is-error');
          }
          invalid.focus();
          return;
        }
        var lines = [];
        $$('input, select, textarea', form).forEach(function (f) {
          if (!f.name || !f.value.trim()) return;
          lines.push(f.dataset.label + ': ' + f.value.trim());
        });
        var subject = form.dataset.subject || 'Website inquiry';
        var href = 'mailto:' + form.dataset.mailto +
          '?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(lines.join('\n') + '\n\n— sent from the High Line website');
        if (note) {
          note.classList.remove('is-error');
          note.textContent = 'Thanks! Your email app is opening with these details — send it and our team will reply, ' +
            'or call +91 812 111 8000 if you prefer.';
          note.classList.add('is-shown');
        }
        window.location.href = href;
      });
    });

    var news = $('[data-newsletter]');
    if (news) {
      news.addEventListener('submit', function (e) {
        e.preventDefault();
        var input = $('input', news);
        var ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value);
        var note = $('[data-note]', news.parentNode);
        if (note) {
          note.textContent = ok
            ? 'Thanks — your email app is opening so you can confirm your subscription.'
            : 'Please enter a valid email address.';
          note.classList.toggle('is-error', !ok);
          note.classList.add('is-shown');
        }
        if (ok) {
          window.location.href = 'mailto:highlinefireandsafety@gmail.com' +
            '?subject=' + encodeURIComponent('Subscribe to High Line updates') +
            '&body=' + encodeURIComponent('Please add ' + input.value + ' to the High Line mailing list.');
        }
      });
    }
  }

  /* ---------------------------------------------------------- current year */
  function year() {
    $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  
  /* ----------------------------------------------------------------- counters */
  function counters() {
    var els = $$('.counter');
    if (!els.length) return;
    
    // If reduced motion is preferred, just show the final numbers
    if (reduced || !('IntersectionObserver' in window)) {
      els.forEach(function(el) {
        var target = el.getAttribute('data-target');
        var suffix = el.getAttribute('data-suffix') || '';
        el.innerText = target + suffix;
      });
      return;
    }

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          observer.unobserve(el);
          
          var target = parseInt(el.getAttribute('data-target'), 10);
          var suffix = el.getAttribute('data-suffix') || '';
          var duration = 2000; // 2 seconds
          var frameDuration = 1000 / 60;
          var totalFrames = Math.round(duration / frameDuration);
          var frame = 0;
          
          // Easing function (easeOutExpo)
          function easeOutExpo(t) {
            return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
          }
          
          var counter = setInterval(function() {
            frame++;
            var progress = easeOutExpo(frame / totalFrames);
            var currentCount = Math.round(target * progress);
            
            el.innerText = currentCount + suffix;
            
            if (frame === totalFrames) {
              clearInterval(counter);
              el.innerText = target + suffix;
            }
          }, frameDuration);
        }
      });
    }, { threshold: 0.5 });

    els.forEach(function(el) {
      observer.observe(el);
    });
  }

  function init() {
    reveal();
    charts();
    counters();
    accordions();
    testimonials();
    achievements();
    faqCategories();
    courseRail();
    drawer();
    counters();
    forms();
    year();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
