import re

with open('website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

preloader_html = '''<body>
  <!-- PRELOADER -->
  <style>
    .preloader {
      position: fixed;
      inset: 0;
      background: #0B3C6D; /* var(--navy) */
      z-index: 99999;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: opacity 0.6s ease, visibility 0.6s ease;
    }
    .preloader.is-hidden {
      opacity: 0;
      visibility: hidden;
    }
    .preloader__spinner {
      width: 70px;
      height: 70px;
      border: 3px solid rgba(255, 255, 255, 0.1);
      border-top-color: #C05C00; /* var(--orange) */
      border-radius: 50%;
      animation: spin 1s linear infinite;
      position: absolute;
    }
    .preloader__logo {
      width: 36px;
      height: 36px;
      animation: pulse 2s infinite ease-in-out;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
    @keyframes pulse {
      0%, 100% { transform: scale(0.9); opacity: 0.8; }
      50% { transform: scale(1.1); opacity: 1; }
    }
  </style>
  <div id="site-preloader" class="preloader">
    <div class="preloader__spinner"></div>
    <img src="assets/logo.webp" alt="Highline Logo" class="preloader__logo" />
  </div>
  <script>
    (function() {
      const preloader = document.getElementById('site-preloader');
      let shouldShow = false;
      const navEntries = performance.getEntriesByType('navigation');
      const navType = navEntries.length > 0 ? navEntries[0].type : '';
      const lastShown = sessionStorage.getItem('hl_preloader_time');
      const now = Date.now();

      // Show on first visit, on reload, or if 5 minutes have passed
      if (navType === 'reload' || !lastShown || (now - parseInt(lastShown)) > 5 * 60 * 1000) {
        shouldShow = true;
        sessionStorage.setItem('hl_preloader_time', now.toString());
      }

      if (!shouldShow) {
        preloader.style.display = 'none';
      } else {
        // Prevent scrolling while loading
        document.body.style.overflow = 'hidden';
        window.addEventListener('load', () => {
          setTimeout(() => {
            preloader.classList.add('is-hidden');
            document.body.style.overflow = '';
          }, 500); // 500ms min display time
        });
      }
    })();
  </script>
  <!-- /PRELOADER -->'''

if 'id="site-preloader"' not in html:
    html = html.replace('<body>', preloader_html, 1)
    with open('website/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Preloader added successfully.")
else:
    print("Preloader already exists.")
