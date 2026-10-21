"""
render_red_ribbon_with_exact_text.py
Renders 3 high-resolution 1920x1080 images featuring:
- The enlarged Fujitsu Red Infinity Ribbon (โบว์แดง)
- Left loop: Microsoft Dynamics 365 icon + text "Dynamics 365"
- Right loop: Microsoft Copilot icon + text "Copilot"
- ZERO shields / no badges
- Exactly matching the user's uploaded reference image layout!
"""

import os
from playwright.sync_api import sync_playwright

with open('assets/microsoft_dynamics_365_icon.svg', 'r', encoding='utf-8') as f:
    d365_svg_xml = f.read()

with open('assets/microsoft_copilot_logo.svg', 'r', encoding='utf-8') as f:
    copilot_svg_xml = f.read()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # =============================================================
        # VARIATION 1: Pure Fluent Clean Studio (White Background)
        # =============================================================
        page1 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html1 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Segoe+UI&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: radial-gradient(circle at 50% 35%, #ffffff 0%, #f8fafc 50%, #e2e8f0 100%);
  font-family: 'Segoe UI', 'Plus Jakarta Sans', -apple-system, sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
/* Floor Reflection Shadow */
.floor-shadow {{
  position: absolute;
  bottom: 110px;
  left: 50%;
  transform: translateX(-50%);
  width: 1560px;
  height: 90px;
  background: radial-gradient(ellipse at center, rgba(15, 23, 42, 0.16) 0%, rgba(230, 0, 18, 0.08) 40%, transparent 75%);
  filter: blur(14px);
}}

/* Top Badge */
.header-tag {{
  position: absolute;
  top: 45px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 24px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(226, 232, 240, 0.9);
  border-radius: 9999px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  z-index: 40;
}}
.tag-pill {{
  background: #E60012;
  color: white;
  padding: 4px 14px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}}
.tag-title {{
  font-size: 15px;
  font-weight: 800;
  color: #0f172a;
}}

/* Main Stage */
.stage-container {{
  position: relative;
  width: 1600px;
  height: 750px;
  display: flex;
  align-items: center;
  justify-content: center;
}}

/* Large Sweeping Red Infinity Ribbon SVG */
.infinity-svg {{
  width: 1560px;
  height: 720px;
  filter: drop-shadow(0 30px 45px rgba(180, 0, 14, 0.28)) drop-shadow(0 15px 25px rgba(0,0,0,0.12));
}}

/* Left Loop Hole: D365 Icon + Text */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 340px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-left svg {{
  width: 210px;
  height: 210px;
  filter: drop-shadow(0 15px 25px rgba(14, 165, 233, 0.35));
}}
.text-d365 {{
  font-size: 30px;
  font-weight: 800;
  color: #001833;
  margin-top: 14px;
  letter-spacing: -0.5px;
  text-align: center;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.08));
}}

/* Right Loop Hole: Copilot Icon + Text */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 340px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-right svg {{
  width: 210px;
  height: 210px;
  filter: drop-shadow(0 15px 25px rgba(168, 85, 247, 0.4));
}}
.text-copilot {{
  font-size: 32px;
  font-weight: 800;
  color: #001833;
  margin-top: 14px;
  letter-spacing: -0.5px;
  text-align: center;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.08));
}}

/* Center Crossover Nexus */
.center-nexus {{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%) rotate(45deg);
  width: 130px;
  height: 130px;
  border-radius: 32px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.95) 0%, rgba(200, 235, 255, 0.75) 45%, rgba(147, 51, 234, 0.45) 80%, transparent 100%);
  backdrop-filter: blur(8px);
  border: 2px solid rgba(255, 255, 255, 0.85);
  box-shadow: 0 0 40px rgba(14, 165, 233, 0.4), inset 0 0 20px rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: 900;
  color: #E60012;
  z-index: 30;
}}
.center-symbol {{
  transform: rotate(-45deg);
  text-shadow: 0 0 15px rgba(230, 0, 18, 0.4);
}}
</style>
</head>
<body>
  <div class="floor-shadow"></div>

  <div class="header-tag">
    <span class="tag-pill">แบบที่ 1 • Clean Studio</span>
    <span class="tag-title">โบว์แดงขยายใหญ่ • ซ้าย [รูป + ข้อความ Dynamics 365] • ขวา [รูป + ข้อความ Copilot] • ตัดโล่ออก</span>
  </div>

  <div class="stage-container">
    <svg class="infinity-svg" viewBox="0 0 1600 750" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="redLoopBack" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#99000C" />
          <stop offset="35%" stop-color="#C70010" />
          <stop offset="70%" stop-color="#E60012" />
          <stop offset="100%" stop-color="#800008" />
        </linearGradient>

        <linearGradient id="redLoopFront" x1="10%" y1="20%" x2="90%" y2="80%">
          <stop offset="0%" stop-color="#FF4D5E" />
          <stop offset="25%" stop-color="#E60012" />
          <stop offset="50%" stop-color="#FF6B7A" />
          <stop offset="75%" stop-color="#C70010" />
          <stop offset="100%" stop-color="#FF3347" />
        </linearGradient>
      </defs>

      <!-- Back Shadow Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#7A0008" stroke-width="96" stroke-linecap="round" stroke-linejoin="round" opacity="0.32" transform="translate(0, 18)" />

      <!-- Main Thick Metallic Red Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#redLoopBack)" stroke-width="84" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Front Specular Highlight Stroke -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#redLoopFront)" stroke-width="56" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Top Gloss Shine Line -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" />
    </svg>

    <!-- LEFT HOLE: DYNAMICS 365 (ICON + TEXT) -->
    <div class="hole-left">
      {d365_svg_xml}
      <div class="text-d365">Dynamics 365</div>
    </div>

    <!-- CENTER NEXUS -->
    <div class="center-nexus">
      <div class="center-symbol">∞</div>
    </div>

    <!-- RIGHT HOLE: COPILOT (ICON + TEXT) -->
    <div class="hole-right">
      {copilot_svg_xml}
      <div class="text-copilot">Copilot</div>
    </div>
  </div>
</body>
</html>"""
        page1.set_content(html1)
        page1.wait_for_timeout(600)
        page1.screenshot(path='assets/ribbon_exact_text_optionA_clean.png')
        print("Saved assets/ribbon_exact_text_optionA_clean.png")
        page1.close()

        # =============================================================
        # VARIATION 2: Cinematic Spotlight & Anamorphic Glint (Dark Obsidian)
        # =============================================================
        page2 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html2 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Segoe+UI&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: radial-gradient(circle at 50% 40%, #0b1329 0%, #030712 60%, #000000 100%);
  font-family: 'Segoe UI', 'Plus Jakarta Sans', -apple-system, sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
/* Anamorphic Spotlight Beam */
.anamorphic-beam {{
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 12px;
  background: linear-gradient(90deg, transparent 0%, rgba(14, 165, 233, 0.4) 25%, rgba(255, 230, 180, 0.9) 50%, rgba(168, 85, 247, 0.4) 75%, transparent 100%);
  box-shadow: 0 0 60px rgba(255, 220, 140, 0.8), 0 0 120px rgba(230, 0, 18, 0.6);
  transform: translateY(-50%);
  pointer-events: none;
  z-index: 5;
}}
.glint-left {{
  position: absolute;
  left: 375px;
  top: 150px;
  width: 80px;
  height: 80px;
  background: radial-gradient(circle, #fff 10%, rgba(255,255,255,0.8) 25%, transparent 70%);
  box-shadow: 0 0 35px #fff, 0 0 60px #0ea5e9;
  border-radius: 50%;
  z-index: 25;
}}
.glint-center {{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 120px;
  height: 120px;
  background: radial-gradient(circle, #fff 15%, rgba(255, 235, 180, 0.8) 35%, transparent 75%);
  box-shadow: 0 0 50px #fff, 0 0 100px #E60012;
  border-radius: 50%;
  z-index: 35;
}}
.glint-right {{
  position: absolute;
  right: 375px;
  top: 150px;
  width: 80px;
  height: 80px;
  background: radial-gradient(circle, #fff 10%, rgba(255,255,255,0.8) 25%, transparent 70%);
  box-shadow: 0 0 35px #fff, 0 0 60px #a855f7;
  border-radius: 50%;
  z-index: 25;
}}

.header-tag {{
  position: absolute;
  top: 45px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 26px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(244, 63, 94, 0.4);
  border-radius: 9999px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(230, 0, 18, 0.3);
  z-index: 40;
}}
.tag-pill {{
  background: linear-gradient(135deg, #E60012, #99000C);
  color: white;
  padding: 4px 14px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  box-shadow: 0 0 15px rgba(230,0,18,0.5);
}}
.tag-title {{
  font-size: 15px;
  font-weight: 800;
  color: #ffffff;
}}

.stage-container {{
  position: relative;
  width: 1600px;
  height: 750px;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.infinity-svg {{
  width: 1560px;
  height: 720px;
  filter: drop-shadow(0 0 50px rgba(230, 0, 18, 0.5)) drop-shadow(0 0 100px rgba(230, 0, 18, 0.25));
}}

/* Left Loop Hole: D365 with Glowing Text */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 330px;
  height: 350px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(14, 165, 233, 0.2) 0%, transparent 70%);
  box-shadow: 0 0 60px rgba(14, 165, 233, 0.35);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-left svg {{
  width: 210px;
  height: 210px;
  filter: drop-shadow(0 0 35px rgba(14, 165, 233, 0.7));
}}
.text-d365 {{
  font-size: 32px;
  font-weight: 800;
  color: #ffffff;
  margin-top: 14px;
  letter-spacing: -0.5px;
  text-align: center;
  text-shadow: 0 0 20px rgba(56, 189, 248, 0.8), 0 2px 8px rgba(0,0,0,0.8);
}}

/* Right Loop Hole: Copilot with Glowing Text */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 330px;
  height: 350px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.2) 0%, transparent 70%);
  box-shadow: 0 0 60px rgba(168, 85, 247, 0.35);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-right svg {{
  width: 210px;
  height: 210px;
  filter: drop-shadow(0 0 35px rgba(168, 85, 247, 0.8));
}}
.text-copilot {{
  font-size: 34px;
  font-weight: 800;
  color: #ffffff;
  margin-top: 14px;
  letter-spacing: -0.5px;
  text-align: center;
  text-shadow: 0 0 20px rgba(192, 132, 252, 0.8), 0 2px 8px rgba(0,0,0,0.8);
}}
</style>
</head>
<body>
  <div class="anamorphic-beam"></div>

  <div class="header-tag">
    <span class="tag-pill">แบบที่ 2 • Cinematic Spotlight</span>
    <span class="tag-title">สปอตไลท์ Anamorphic • โบว์แดงเรืองแสง • ตัวหนังสือ Dynamics 365 &amp; Copilot คมชัด</span>
  </div>

  <div class="stage-container">
    <div class="glint-left"></div>
    <div class="glint-center"></div>
    <div class="glint-right"></div>

    <svg class="infinity-svg" viewBox="0 0 1600 750" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="cinematicRed" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#FF1E38" />
          <stop offset="30%" stop-color="#E60012" />
          <stop offset="50%" stop-color="#FF4D5E" />
          <stop offset="70%" stop-color="#B3000E" />
          <stop offset="100%" stop-color="#FF1E38" />
        </linearGradient>
      </defs>

      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#500005" stroke-width="92" stroke-linecap="round" stroke-linejoin="round" />

      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#cinematicRed)" stroke-width="72" stroke-linecap="round" stroke-linejoin="round" />

      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.65" />
    </svg>

    <!-- LEFT HOLE: DYNAMICS 365 (ICON + TEXT) -->
    <div class="hole-left">
      {d365_svg_xml}
      <div class="text-d365">Dynamics 365</div>
    </div>

    <!-- RIGHT HOLE: COPILOT (ICON + TEXT) -->
    <div class="hole-right">
      {copilot_svg_xml}
      <div class="text-copilot">Copilot</div>
    </div>
  </div>
</body>
</html>"""
        page2.set_content(html2)
        page2.wait_for_timeout(600)
        page2.screenshot(path='assets/ribbon_exact_text_optionB_cinematic.png')
        print("Saved assets/ribbon_exact_text_optionB_cinematic.png")
        page2.close()

        # =============================================================
        # VARIATION 3: Pure Minimalist Logo Lockup Inside Ribbon
        # =============================================================
        page3 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html3 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Segoe+UI&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: #ffffff;
  font-family: 'Segoe UI', 'Plus Jakarta Sans', -apple-system, sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
.header-tag {{
  position: absolute;
  top: 45px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 24px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 9999px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
  z-index: 40;
}}
.tag-pill {{
  background: #E60012;
  color: white;
  padding: 4px 14px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}}
.tag-title {{
  font-size: 15px;
  font-weight: 800;
  color: #0f172a;
}}

.stage-container {{
  position: relative;
  width: 1600px;
  height: 750px;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.infinity-svg {{
  width: 1560px;
  height: 720px;
  filter: drop-shadow(0 25px 35px rgba(230, 0, 18, 0.22));
}}

/* Left Loop Hole: D365 */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-left svg {{
  width: 220px;
  height: 220px;
}}
.text-d365 {{
  font-size: 32px;
  font-weight: 800;
  color: #001833;
  margin-top: 12px;
  letter-spacing: -0.5px;
  text-align: center;
}}

/* Right Loop Hole: Copilot */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-right svg {{
  width: 220px;
  height: 220px;
}}
.text-copilot {{
  font-size: 34px;
  font-weight: 800;
  color: #001833;
  margin-top: 12px;
  letter-spacing: -0.5px;
  text-align: center;
}}
</style>
</head>
<body>
  <div class="header-tag">
    <span class="tag-pill">แบบที่ 3 • Ultra Minimalist Pure White</span>
    <span class="tag-title">พื้นหลังขาวสนิทคมชัดสูงสุด • โบว์แดงเงางาม • รูปพร้อมชื่อครบถ้วน</span>
  </div>

  <div class="stage-container">
    <svg class="infinity-svg" viewBox="0 0 1600 750" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="pureRedGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#FF3347" />
          <stop offset="35%" stop-color="#E60012" />
          <stop offset="70%" stop-color="#B8000E" />
          <stop offset="100%" stop-color="#800008" />
        </linearGradient>
      </defs>

      <!-- Clean Red Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#pureRedGrad)" stroke-width="84" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Sleek Inner Specular Edge -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" opacity="0.75" />
    </svg>

    <!-- LEFT HOLE: DYNAMICS 365 -->
    <div class="hole-left">
      {d365_svg_xml}
      <div class="text-d365">Dynamics 365</div>
    </div>

    <!-- RIGHT HOLE: COPILOT -->
    <div class="hole-right">
      {copilot_svg_xml}
      <div class="text-copilot">Copilot</div>
    </div>
  </div>
</body>
</html>"""
        page3.set_content(html3)
        page3.wait_for_timeout(600)
        page3.screenshot(path='assets/ribbon_exact_text_optionC_pure_white.png')
        print("Saved assets/ribbon_exact_text_optionC_pure_white.png")
        page3.close()

        browser.close()

if __name__ == '__main__':
    main()
