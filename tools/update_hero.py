import re

def update_generate_pages():
    with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
        pass # just to check if it's there
        
    with open('tools/generate_pages.py', 'r', encoding='utf-8') as f:
        content = f.read()

    new_hero = '''<!-- HERO -->
<header class="hero hero--inner" style="min-height:55vh; padding-top:140px; padding-bottom:80px; background: url('../assets/img/hero-home.jpg') center/cover no-repeat; position: relative;">
  <!-- Dark overlay -->
  <div style="position:absolute; inset:0; background: linear-gradient(135deg, rgba(11,60,109,0.95) 0%, rgba(26,95,168,0.85) 100%);"></div>
  
  <div class="hero__content" style="position:relative; z-index:2; padding-top:0; max-width:1000px; margin:0 auto; display:flex; flex-direction:column; align-items:flex-start;">
    
    <!-- Breadcrumb -->
    <p style="font-size:13px; color:rgba(255,255,255,0.7); margin-bottom:20px; display:flex; align-items:center; gap:8px;">
      <a href="../courses.html" style="color:rgba(255,255,255,0.9); text-decoration:none; font-weight:600; transition:color 0.2s;">
        <span style="font-size:16px; line-height:1; vertical-align:middle;">&#8592;</span> All Courses
      </a>
      <span style="color:rgba(255,255,255,0.4);">/</span>
      <span>{cat}</span>
    </p>

    <!-- Badge -->
    <span style="display:inline-flex; align-items:center; background:rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color:#fff; font-size:12px; font-weight:700; padding:6px 14px; border-radius:100px; margin-bottom:20px; text-transform:uppercase; letter-spacing:0.08em; width: max-content;">
      {level}
    </span>

    <!-- Title -->
    <h1 class="hero__title" style="margin-bottom:20px; font-size:clamp(32px, 4.5vw, 52px); line-height:1.2; font-weight:800; color:#fff; text-shadow: 0 2px 10px rgba(0,0,0,0.15);">{title}</h1>

    <!-- Description -->
    <p style="font-size:17px; line-height:1.75; color:rgba(255,255,255,0.85); max-width:800px; margin-bottom: 40px;">{desc}</p>

    <!-- Quick Stats -->
    <div style="display:flex; flex-wrap:wrap; gap:24px; margin-bottom: 40px; padding: 20px 24px; background: rgba(0,0,0,0.2); border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; max-width: 850px; backdrop-filter: blur(4px);">
      <div style="display:flex; align-items:center; gap:14px; flex: 1 1 200px;">
        <div style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:var(--orange);">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <div>
          <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.05em; color:rgba(255,255,255,0.6); font-weight:700; margin-bottom:2px;">Duration</div>
          <div style="font-size:14px; font-weight:600; color:#fff;">{dur_text}</div>
        </div>
      </div>
      
      <div style="display:flex; align-items:center; gap:14px; flex: 1 1 200px;">
        <div style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:var(--orange);">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        </div>
        <div>
          <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.05em; color:rgba(255,255,255,0.6); font-weight:700; margin-bottom:2px;">Format</div>
          <div style="font-size:14px; font-weight:600; color:#fff;">{', '.join(modes)}</div>
        </div>
      </div>

      <div style="display:flex; align-items:center; gap:14px; flex: 1 1 200px;">
        <div style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:var(--orange);">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        </div>
        <div>
          <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.05em; color:rgba(255,255,255,0.6); font-weight:700; margin-bottom:2px;">Certification</div>
          <div style="font-size:14px; font-weight:600; color:#fff; display:-webkit-box; -webkit-line-clamp:1; -webkit-box-orient:vertical; overflow:hidden;" title="{cert}">{cert}</div>
        </div>
      </div>
    </div>

    <!-- Buttons -->
    <div class="hero-cta-group" style="margin-top:0;">
      <a href="../admissions.html" class="btn btn--primary" style="padding:16px 32px; font-size:16px; display:inline-flex; align-items:center; gap:8px;">
        Apply / Enquire Now 
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
      <a href="../contact.html" class="btn--outline-white" style="padding:16px 32px; font-size:16px;">Ask a Question</a>
    </div>
  </div>
</header>'''

    # We need to replace the old hero block
    old_hero_pattern = r'<!-- HERO -->\n<header class="hero hero--inner".*?</header>'
    
    new_content = re.sub(old_hero_pattern, new_hero, content, flags=re.DOTALL)
    
    with open('tools/generate_pages.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Updated generate_pages.py with new modern hero section")

if __name__ == '__main__':
    update_generate_pages()
