import os
import re

# 1. Update index.html
html_path = 'website/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the trust metrics with data attributes
html = html.replace('<b>16+</b>', '<b class="counter" data-target="16" data-suffix="+">0+</b>')
html = html.replace('<b>3</b>', '<b class="counter" data-target="3" data-suffix="">0</b>')
html = html.replace('<b>100%</b>', '<b class="counter" data-target="100" data-suffix="%">0%</b>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add JS to site.js
js_path = 'website/assets/js/site.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

counter_js = """
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
"""

# Insert the function before the init() function calls
if 'function init() {' in js:
    js = js.replace('function init() {', counter_js + '\n  function init() {')
    # Add the call to counters() inside init()
    js = js.replace('drawer();', 'drawer();\n    counters();')
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
        
print("Counter effect added.")
