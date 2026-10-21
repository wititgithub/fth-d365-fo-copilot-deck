"""
generate_logo_combos.py
Generates 3 high-resolution design examples combining the D365 icon, Copilot icon,
and the Value 3D graphic (Option 3 style):
1. Example 1: Dual Orbital Synergy Shields (Studio Light)
2. Example 2: Twin Core Nexus Inside Infinity (Hybrid Dynamic)
3. Example 3: Executive Keynote Crest & Anamorphic Spotlight (Cinematic Dark)
"""

import os
from playwright.sync_api import sync_playwright

with open('assets/microsoft_dynamics_365_icon.svg', 'r', encoding='utf-8') as f:
    d365_icon_svg = f.read()

with open('assets/microsoft_copilot_logo.svg', 'r', encoding='utf-8') as f:
    copilot_icon_svg = f.read()

base_3d_path = os.path.abspath('assets/fujitsu_copilot_value_3d.jpg').replace('\\', '/')

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # -------------------------------------------------------------
        # EXAMPLE 1: Dual Orbital Synergy Shields (Studio Light)
        # -------------------------------------------------------------
        page1 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html1 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: #f8fafc;
  position: relative;
  overflow: hidden;
}}
.base-img {{
  position: absolute;
  top: 0;
  left: 0;
  width: 1920px;
  height: 1080px;
  object-fit: cover;
}}
/* Shield Overlay Left: D365 */
.shield-d365 {{
  position: absolute;
  top: 145px;
  left: 175px;
  width: 250px;
  height: 250px;
  border-radius: 40px;
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(16px);
  border: 2px solid rgba(14, 165, 233, 0.5);
  box-shadow: 0 20px 40px rgba(14, 165, 233, 0.25), inset 0 0 25px rgba(255,255,255,0.8);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px;
  z-index: 10;
}}
.shield-d365 svg {{
  width: 125px;
  height: 125px;
  filter: drop-shadow(0 10px 15px rgba(14, 165, 233, 0.35));
}}
.label-d365 {{
  font-size: 13px;
  font-weight: 800;
  color: #0369a1;
  margin-top: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}
.sub-d365 {{
  font-size: 10px;
  font-weight: 700;
  color: #64748b;
  font-family: 'JetBrains Mono', monospace;
}}

/* Shield Overlay Right: Copilot */
.shield-copilot {{
  position: absolute;
  top: 145px;
  right: 175px;
  width: 250px;
  height: 250px;
  border-radius: 40px;
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(16px);
  border: 2px solid rgba(168, 85, 247, 0.5);
  box-shadow: 0 20px 40px rgba(168, 85, 247, 0.25), inset 0 0 25px rgba(255,255,255,0.8);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px;
  z-index: 10;
}}
.shield-copilot svg {{
  width: 125px;
  height: 125px;
  filter: drop-shadow(0 10px 15px rgba(168, 85, 247, 0.35));
}}
.label-copilot {{
  font-size: 13px;
  font-weight: 800;
  color: #7e22ce;
  margin-top: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}
.sub-copilot {{
  font-size: 10px;
  font-weight: 700;
  color: #64748b;
  font-family: 'JetBrains Mono', monospace;
}}

/* Header Banner */
.top-banner {{
  position: absolute;
  top: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  padding: 10px 28px;
  border-radius: 9999px;
  border: 1px solid rgba(226, 232, 240, 0.8);
  box-shadow: 0 10px 25px rgba(0,0,0,0.06);
  z-index: 20;
}}
.tag-badge {{
  background: #E60012;
  color: white;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
}}
.banner-title {{
  font-size: 15px;
  font-weight: 800;
  color: #0f172a;
}}
</style>
</head>
<body>
  <img src="file:///{base_3d_path}" class="base-img">
  <div class="top-banner">
    <span class="tag-badge">ตัวอย่างที่ 1</span>
    <span class="banner-title">Dual Orbital Synergy Shields — วางประกบสองฝั่งบนโล่ 3 มิติ</span>
  </div>
  <div class="shield-d365">
    {d365_icon_svg}
    <div class="label-d365">Dynamics 365</div>
    <div class="sub-d365">SYSTEM OF RECORD</div>
  </div>
  <div class="shield-copilot">
    {copilot_icon_svg}
    <div class="label-copilot">Microsoft Copilot</div>
    <div class="sub-copilot">COGNITIVE AI AGENT</div>
  </div>
</body>
</html>"""
        page1.set_content(html1)
        page1.wait_for_timeout(600)
        page1.screenshot(path='assets/option3_logo_combo_1.png')
        print("Saved assets/option3_logo_combo_1.png")
        page1.close()

        # -------------------------------------------------------------
        # EXAMPLE 2: Twin Core Nexus Inside Infinity (Hybrid Dynamic)
        # -------------------------------------------------------------
        page2 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html2 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: #f1f5f9;
  position: relative;
  overflow: hidden;
}}
.base-img {{
  position: absolute;
  top: 0;
  left: 0;
  width: 1920px;
  height: 1080px;
  object-fit: cover;
}}
/* Embedded in Left Loop */
.loop-left {{
  position: absolute;
  top: 410px;
  left: 450px;
  width: 190px;
  height: 190px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(14, 165, 233, 0.35) 0%, rgba(14, 165, 233, 0.05) 70%, transparent 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 15;
  filter: drop-shadow(0 0 25px rgba(14, 165, 233, 0.6));
}}
.loop-left svg {{
  width: 135px;
  height: 135px;
}}
.tag-left {{
  position: absolute;
  bottom: -25px;
  background: rgba(14, 165, 233, 0.9);
  color: white;
  padding: 3px 12px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 800;
  white-space: nowrap;
}}

/* Embedded in Right Loop */
.loop-right {{
  position: absolute;
  top: 410px;
  right: 450px;
  width: 190px;
  height: 190px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.35) 0%, rgba(168, 85, 247, 0.05) 70%, transparent 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 15;
  filter: drop-shadow(0 0 25px rgba(168, 85, 247, 0.6));
}}
.loop-right svg {{
  width: 135px;
  height: 135px;
}}
.tag-right {{
  position: absolute;
  bottom: -25px;
  background: rgba(168, 85, 247, 0.9);
  color: white;
  padding: 3px 12px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 800;
  white-space: nowrap;
}}

/* Top Banner */
.top-banner {{
  position: absolute;
  top: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(12px);
  padding: 10px 28px;
  border-radius: 9999px;
  border: 1px solid rgba(51, 65, 85, 0.8);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  z-index: 20;
}}
.tag-badge {{
  background: #0284c7;
  color: white;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
}}
.banner-title {{
  font-size: 15px;
  font-weight: 800;
  color: #f8fafc;
}}
</style>
</head>
<body>
  <img src="file:///{base_3d_path}" class="base-img">
  <div class="top-banner">
    <span class="tag-badge">ตัวอย่างที่ 2</span>
    <span class="banner-title">Twin Core Nexus — ฝังไอคอนสถิตในห่วงอินฟินิตี้ ซ้าย-ขวา</span>
  </div>
  <div class="loop-left">
    {d365_icon_svg}
    <div class="tag-left">DYNAMICS 365 CORE</div>
  </div>
  <div class="loop-right">
    {copilot_icon_svg}
    <div class="tag-right">COPILOT AI CORE</div>
  </div>
</body>
</html>"""
        page2.set_content(html2)
        page2.wait_for_timeout(600)
        page2.screenshot(path='assets/option3_logo_combo_2.png')
        print("Saved assets/option3_logo_combo_2.png")
        page2.close()

        # -------------------------------------------------------------
        # EXAMPLE 3: Executive Keynote Crest & Anamorphic Spotlight (Cinematic Dark)
        # -------------------------------------------------------------
        page3 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        html3 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1920px;
  height: 1080px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: #020617;
  position: relative;
  overflow: hidden;
}}
.base-container {{
  position: absolute;
  top: 40px;
  left: 50%;
  transform: translateX(-50%);
  width: 1720px;
  height: 800px;
  border-radius: 36px;
  overflow: hidden;
  box-shadow: 0 30px 80px rgba(0,0,0,0.8);
  border: 1px solid rgba(51, 65, 85, 0.5);
}}
.base-img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: contrast(1.08) brightness(0.95);
}}
.cinematic-vignette {{
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 50%, transparent 40%, rgba(2, 6, 23, 0.75) 100%);
  pointer-events: none;
}}
.anamorphic-beam {{
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 6px;
  background: linear-gradient(90deg, transparent 0%, rgba(255, 230, 180, 0.6) 50%, transparent 100%);
  box-shadow: 0 0 35px rgba(255, 200, 100, 0.9);
  transform: translateY(-50%);
  pointer-events: none;
}}

/* Executive Bottom Co-Branding Crest Card */
.co-branding-card {{
  position: absolute;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(15, 23, 42, 0.88);
  backdrop-filter: blur(20px);
  border: 2px solid rgba(244, 63, 94, 0.4);
  box-shadow: 0 20px 60px rgba(0,0,0,0.7), 0 0 40px rgba(230, 0, 18, 0.25);
  border-radius: 9999px;
  padding: 14px 44px;
  display: flex;
  align-items: center;
  gap: 36px;
  z-index: 30;
}}
.brand-block {{
  display: flex;
  align-items: center;
  gap: 14px;
}}
.brand-block svg {{
  height: 48px;
  width: 48px;
}}
.brand-text {{
  display: flex;
  flex-direction: column;
}}
.brand-name {{
  font-size: 18px;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.3px;
}}
.brand-role {{
  font-size: 10px;
  font-weight: 800;
  color: #94a3b8;
  letter-spacing: 1px;
  font-family: 'JetBrains Mono', monospace;
}}
.x-connector {{
  font-size: 26px;
  font-weight: 900;
  color: #E60012;
  text-shadow: 0 0 15px rgba(230, 0, 18, 0.8);
}}
.tag-badge {{
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #E60012, #99000c);
  color: white;
  padding: 4px 18px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  box-shadow: 0 4px 12px rgba(230, 0, 18, 0.4);
  white-space: nowrap;
}}
</style>
</head>
<body>
  <div class="base-container">
    <img src="file:///{base_3d_path}" class="base-img">
    <div class="cinematic-vignette"></div>
    <div class="anamorphic-beam"></div>
  </div>
  
  <div class="co-branding-card">
    <div class="tag-badge">ตัวอย่างที่ 3 • Executive Keynote Crest</div>
    
    <div class="brand-block">
      <div style="width:42px; height:42px; border-radius:10px; background:#E60012; display:flex; align-items:center; justify-content:center; color:white; font-size:20px; font-weight:900;">
        ∞
      </div>
      <div class="brand-text">
        <span class="brand-name">Fujitsu Thailand</span>
        <span class="brand-role">LOCALIZATION IP</span>
      </div>
    </div>

    <div class="x-connector">✕</div>

    <div class="brand-block">
      {d365_icon_svg}
      <div class="brand-text">
        <span class="brand-name">Dynamics 365</span>
        <span class="brand-role">SYSTEM OF RECORD</span>
      </div>
    </div>

    <div class="x-connector">✕</div>

    <div class="brand-block">
      {copilot_icon_svg}
      <div class="brand-text">
        <span class="brand-name">Microsoft Copilot</span>
        <span class="brand-role">COGNITIVE AI</span>
      </div>
    </div>
  </div>
</body>
</html>"""
        page3.set_content(html3)
        page3.wait_for_timeout(600)
        page3.screenshot(path='assets/option3_logo_combo_3.png')
        print("Saved assets/option3_logo_combo_3.png")
        page3.close()

        browser.close()

if __name__ == '__main__':
    main()
