import re

with open('website/assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's forcefully override the header responsiveness
header_mobile_fix = """
/* ============================================================================
   FORCE HEADER MOBILE RESPONSIVENESS
   ========================================================================== */

@media (max-width: 1024px) {
  .nav__links { display: none !important; }
  .nav__right .btn { display: none !important; }
  .nav__right .nav__phone { display: none !important; }
  
  .nav__burger { 
    display: flex !important; 
    width: 44px !important; 
    height: 44px !important;
    border: 1px solid rgba(255, 255, 255, 0.45) !important;
    background: rgba(11, 34, 60, 0.34) !important;
    border-radius: 50% !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 5px !important;
    padding: 0 !important;
  }
  
  .nav__burger span {
    display: block !important;
    width: 20px !important;
    height: 2px !important;
    border-radius: 2px !important;
    background: #fff !important;
    transition: transform 0.3s ease, opacity 0.2s !important;
  }
}
"""

with open('website/assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write('\n' + header_mobile_fix)

print("Forced header mobile CSS appended.")
