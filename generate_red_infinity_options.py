"""
generate_red_infinity_options.py
Renders 3 high-resolution 1920x1080 variations based on the user's exact specification:
- Much bigger, thicker, sweeping Fujitsu Red infinity ribbon
- Left loop hole: Microsoft Dynamics 365 icon
- Right loop hole: Microsoft Copilot icon
- NO shields (completely removed)
1. Option A: Pure Fluent Clean Studio (White / Studio Light)
2. Option B: Cinematic Spotlight & Anamorphic Glint (Dark Obsidian Keynote)
3. Option C: Quantum High-Tech Energy Nexus (Cybernetic Ambient)
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
        # OPTION A: Pure Fluent Clean Studio (White Background)
        # =============================================================
        pageA = browser.new_page(viewport={'width': 1920, 'height': 1080})
        htmlA = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: radial-gradient(circle at 50% 40%, #ffffff 0%, #f1f5f9 60%, #e2e8f0 100%);
  font-family: 'Plus Jakarta Sans', sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
/* Floor Shadow / Studio Reflection */
.floor-shadow {{
  position: absolute;
  bottom: 120px;
  left: 50%;
  transform: translateX(-50%);
  width: 1550px;
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
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(226, 232, 240, 0.9);
  border-radius: 9999px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
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

/* Infinity Canvas Container */
.stage-container {{
  position: relative;
  width: 1600px;
  height: 750px;
  display: flex;
  align-items: center;
  justify-content: center;
}}

/* Large Sweeping Red Infinity SVG */
.infinity-svg {{
  width: 1560px;
  height: 720px;
  filter: drop-shadow(0 30px 45px rgba(180, 0, 14, 0.28)) drop-shadow(0 15px 25px rgba(0,0,0,0.12));
}}

/* Left Loop Hole: D365 Icon */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-left svg {{
  width: 250px;
  height: 250px;
  filter: drop-shadow(0 20px 30px rgba(14, 165, 233, 0.35));
}}
.label-left {{
  margin-top: 14px;
  font-size: 15px;
  font-weight: 900;
  color: #0284c7;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  background: rgba(255,255,255,0.9);
  padding: 4px 16px;
  border-radius: 9999px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}}

/* Right Loop Hole: Copilot Icon */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 320px;
  height: 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-right svg {{
  width: 250px;
  height: 250px;
  filter: drop-shadow(0 20px 30px rgba(168, 85, 247, 0.4));
}}
.label-right {{
  margin-top: 14px;
  font-size: 15px;
  font-weight: 900;
  color: #7e22ce;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  background: rgba(255,255,255,0.9);
  padding: 4px 16px;
  border-radius: 9999px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}}

/* Center Convergence Crystal Nexus */
.center-nexus {{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 140px;
  height: 140px;
  border-radius: 36px;
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
  transform: translate(-50%, -50%) rotate(45deg);
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
    <span class="tag-pill">แบบ A • Clean Studio</span>
    <span class="tag-title">โบสีแดงขยายใหญ่พิเศษ • ซ้าย D365 • ขวา Copilot • ไม่มีโล่</span>
  </div>

  <div class="stage-container">
    <!-- SVG Large Metallic Red Ribbon -->
    <svg class="infinity-svg" viewBox="0 0 1600 750" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Rich Metallic Red Gradient for Back Loop -->
        <linearGradient id="redLoopBack" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#99000C" />
          <stop offset="35%" stop-color="#C70010" />
          <stop offset="70%" stop-color="#E60012" />
          <stop offset="100%" stop-color="#800008" />
        </linearGradient>

        <!-- Glossy Specular Front Gradient -->
        <linearGradient id="redLoopFront" x1="10%" y1="20%" x2="90%" y2="80%">
          <stop offset="0%" stop-color="#FF4D5E" />
          <stop offset="25%" stop-color="#E60012" />
          <stop offset="50%" stop-color="#FF6B7A" />
          <stop offset="75%" stop-color="#C70010" />
          <stop offset="100%" stop-color="#FF3347" />
        </linearGradient>

        <!-- Inner Shadow Filter -->
        <filter id="softGleam" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="8" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>

      <!-- Back Shadow Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#7A0008" stroke-width="96" stroke-linecap="round" stroke-linejoin="round" opacity="0.35" transform="translate(0, 18)" />

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

    <!-- LEFT HOLE: DYNAMICS 365 -->
    <div class="hole-left">
      {d365_svg_xml}
      <div class="label-left">Dynamics 365</div>
    </div>

    <!-- CENTER NEXUS -->
    <div class="center-nexus">
      <div class="center-symbol">∞</div>
    </div>

    <!-- RIGHT HOLE: COPILOT -->
    <div class="hole-right">
      {copilot_svg_xml}
      <div class="label-right">Microsoft Copilot</div>
    </div>
  </div>
</body>
</html>"""
        pageA.set_content(htmlA)
        pageA.wait_for_timeout(600)
        pageA.screenshot(path='assets/composite_optionA_clean_studio.png')
        print("Saved assets/composite_optionA_clean_studio.png")
        pageA.close()

        # =============================================================
        # OPTION B: Cinematic Spotlight & Anamorphic Glint (Dark Obsidian)
        # =============================================================
        pageB = browser.new_page(viewport={'width': 1920, 'height': 1080})
        htmlB = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: radial-gradient(circle at 50% 40%, #0b1329 0%, #030712 60%, #000000 100%);
  font-family: 'Plus Jakarta Sans', sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
/* Anamorphic Horizontal Spotlight Beam */
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
/* Starburst Glints */
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
  pointer-events: none;
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
  pointer-events: none;
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
  pointer-events: none;
}}

/* Top Badge */
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

/* Left Loop Hole: D365 Icon */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 330px;
  height: 330px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, rgba(14, 165, 233, 0.05) 55%, transparent 75%);
  box-shadow: 0 0 60px rgba(14, 165, 233, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-left svg {{
  width: 250px;
  height: 250px;
  filter: drop-shadow(0 0 30px rgba(14, 165, 233, 0.7));
}}
.label-left {{
  margin-top: 14px;
  font-size: 14px;
  font-weight: 900;
  color: #38bdf8;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: rgba(15, 23, 42, 0.85);
  padding: 4px 18px;
  border-radius: 9999px;
  border: 1px solid rgba(14, 165, 233, 0.5);
  box-shadow: 0 0 20px rgba(14, 165, 233, 0.3);
}}

/* Right Loop Hole: Copilot Icon */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 330px;
  height: 330px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(168, 85, 247, 0.05) 55%, transparent 75%);
  box-shadow: 0 0 60px rgba(168, 85, 247, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.hole-right svg {{
  width: 250px;
  height: 250px;
  filter: drop-shadow(0 0 30px rgba(168, 85, 247, 0.8));
}}
.label-right {{
  margin-top: 14px;
  font-size: 14px;
  font-weight: 900;
  color: #c084fc;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: rgba(15, 23, 42, 0.85);
  padding: 4px 18px;
  border-radius: 9999px;
  border: 1px solid rgba(168, 85, 247, 0.5);
  box-shadow: 0 0 20px rgba(168, 85, 247, 0.3);
}}
</style>
</head>
<body>
  <div class="anamorphic-beam"></div>

  <div class="header-tag">
    <span class="tag-pill">แบบ B • Cinematic Spotlight</span>
    <span class="tag-title">สปอตไลท์ Anamorphic • โบแดงเรืองแสง • ซ้าย D365 • ขวา Copilot</span>
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

      <!-- Deep Red Metallic Base -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#500005" stroke-width="92" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Glowing Red Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#cinematicRed)" stroke-width="72" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Specular Core Edge -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.65" />
    </svg>

    <!-- LEFT HOLE: D365 -->
    <div class="hole-left">
      {d365_svg_xml}
      <div class="label-left">Dynamics 365</div>
    </div>

    <!-- RIGHT HOLE: COPILOT -->
    <div class="hole-right">
      {copilot_svg_xml}
      <div class="label-right">Microsoft Copilot</div>
    </div>
  </div>
</body>
</html>"""
        pageB.set_content(htmlB)
        pageB.wait_for_timeout(600)
        pageB.screenshot(path='assets/composite_optionB_cinematic_spotlight.png')
        print("Saved assets/composite_optionB_cinematic_spotlight.png")
        pageB.close()

        # =============================================================
        # OPTION C: Quantum High-Tech Energy Nexus (Cyber Space)
        # =============================================================
        pageC = browser.new_page(viewport={'width': 1920, 'height': 1080})
        htmlC = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  background: #020617;
  font-family: 'Plus Jakarta Sans', sans-serif;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
/* Cybernetic Hex Grid Overlay */
.grid-overlay {{
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(to right, rgba(14, 165, 233, 0.05) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(14, 165, 233, 0.05) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
}}

/* Top Badge */
.header-tag {{
  position: absolute;
  top: 45px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 26px;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(0, 242, 254, 0.4);
  border-radius: 9999px;
  box-shadow: 0 0 30px rgba(0, 242, 254, 0.2);
  z-index: 40;
}}
.tag-pill {{
  background: #00F2FE;
  color: #020617;
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
  filter: drop-shadow(0 0 45px rgba(230, 0, 18, 0.6));
}}

/* Left Loop Hole: D365 with HUD Ring */
.hole-left {{
  position: absolute;
  left: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 340px;
  height: 340px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.ring-left {{
  position: absolute;
  inset: 0;
  border: 2px dashed rgba(14, 165, 233, 0.5);
  border-radius: 50%;
  box-shadow: 0 0 30px rgba(14, 165, 233, 0.3);
}}
.hole-left svg {{
  width: 240px;
  height: 240px;
  filter: drop-shadow(0 0 25px rgba(14, 165, 233, 0.7));
}}
.label-left {{
  margin-top: 14px;
  font-size: 13px;
  font-weight: 800;
  color: #38bdf8;
  letter-spacing: 1px;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(14, 165, 233, 0.15);
  border: 1px solid rgba(14, 165, 233, 0.4);
  padding: 4px 16px;
  border-radius: 9999px;
}}

/* Right Loop Hole: Copilot with HUD Ring */
.hole-right {{
  position: absolute;
  right: 310px;
  top: 50%;
  transform: translateY(-50%);
  width: 340px;
  height: 340px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
}}
.ring-right {{
  position: absolute;
  inset: 0;
  border: 2px dashed rgba(168, 85, 247, 0.5);
  border-radius: 50%;
  box-shadow: 0 0 30px rgba(168, 85, 247, 0.3);
}}
.hole-right svg {{
  width: 240px;
  height: 240px;
  filter: drop-shadow(0 0 25px rgba(168, 85, 247, 0.7));
}}
.label-right {{
  margin-top: 14px;
  font-size: 13px;
  font-weight: 800;
  color: #c084fc;
  letter-spacing: 1px;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(168, 85, 247, 0.15);
  border: 1px solid rgba(168, 85, 247, 0.4);
  padding: 4px 16px;
  border-radius: 9999px;
}}

/* Quantum Central Convergence Core */
.quantum-nexus {{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 0%, rgba(0, 242, 254, 0.8) 35%, rgba(121, 40, 202, 0.6) 70%, transparent 100%);
  box-shadow: 0 0 60px #00f2fe, 0 0 100px #7928ca;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 38px;
  font-weight: 900;
  color: #020617;
}}
</style>
</head>
<body>
  <div class="grid-overlay"></div>

  <div class="header-tag">
    <span class="tag-pill">แบบ C • Quantum High-Tech</span>
    <span class="tag-title">พลังงานควอนตัม • นีออนโบแดง • ซ้าย D365 • ขวา Copilot</span>
  </div>

  <div class="stage-container">
    <svg class="infinity-svg" viewBox="0 0 1600 750" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="quantumRed" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#FF0033" />
          <stop offset="25%" stop-color="#E60012" />
          <stop offset="50%" stop-color="#FF3366" />
          <stop offset="75%" stop-color="#C70010" />
          <stop offset="100%" stop-color="#FF0033" />
        </linearGradient>
      </defs>

      <!-- Neon Outer Halo -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#E60012" stroke-width="110" stroke-linecap="round" stroke-linejoin="round" opacity="0.3" filter="url(#glow)" />

      <!-- Thick Red Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="url(#quantumRed)" stroke-width="78" stroke-linecap="round" stroke-linejoin="round" />

      <!-- Cyan Energy Stream Trace along the Ribbon -->
      <path d="M 800,375 C 650,220 540,150 375,150 C 200,150 90,260 90,375 C 90,490 200,600 375,600 C 540,600 650,530 800,375 C 950,220 1060,150 1225,150 C 1400,150 1510,260 1510,375 C 1510,490 1400,600 1225,600 C 1060,600 950,530 800,375 Z"
            fill="none" stroke="#00F2FE" stroke-width="6" stroke-linecap="round" stroke-dasharray="24 16" opacity="0.85" />
    </svg>

    <!-- LEFT HOLE: D365 -->
    <div class="hole-left">
      <div class="ring-left"></div>
      {d365_svg_xml}
      <div class="label-left">DYNAMICS 365</div>
    </div>

    <!-- QUANTUM NEXUS -->
    <div class="quantum-nexus">
      ∞
    </div>

    <!-- RIGHT HOLE: COPILOT -->
    <div class="hole-right">
      <div class="ring-right"></div>
      {copilot_svg_xml}
      <div class="label-right">MS COPILOT</div>
    </div>
  </div>
</body>
</html>"""
        pageC.set_content(htmlC)
        pageC.wait_for_timeout(600)
        pageC.screenshot(path='assets/composite_optionC_quantum_energy.png')
        print("Saved assets/composite_optionC_quantum_energy.png")
        pageC.close()

        browser.close()

if __name__ == '__main__':
    main()
