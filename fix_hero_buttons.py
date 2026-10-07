import os

css_fix = """
/* ============================================================================
   HERO BUTTON UI FIXES
   ========================================================================== */

/* Make hero buttons larger and more UI rich */
.hero__actions .btn {
  padding: 16px 36px;
  font-size: 17px;
  border-radius: 100px;
  letter-spacing: 0.02em;
}

/* Primary Button Enhancements */
.hero__actions .btn--primary {
  background: var(--orange);
  color: var(--white);
  border: 2px solid var(--orange);
  box-shadow: 0 4px 16px rgba(245, 124, 0, 0.4);
}
.hero__actions .btn--primary:hover {
  background: #E65100;
  border-color: #E65100;
  box-shadow: 0 6px 20px rgba(245, 124, 0, 0.5);
  transform: translateY(-2px);
}

/* Secondary White Button Fix */
.hero__actions .btn--secondary.btn--white {
  background: rgba(255, 255, 255, 0.1);
  color: var(--white);
  border: 2px solid rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: none;
}
.hero__actions .btn--secondary.btn--white:hover {
  background: var(--white);
  color: var(--navy) !important;
  border-color: var(--white);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}
"""

with open('website/assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_fix)

print("Hero button CSS applied.")
