"""
render_logos.py
Properly renders high-res PNGs by embedding the raw SVG XML into HTML.
"""

import os
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

with open('assets/microsoft_dynamics_365_logo.svg', 'r', encoding='utf-8') as f:
    d365_svg_xml = f.read()

with open('assets/microsoft_copilot_logo.svg', 'r', encoding='utf-8') as f:
    copilot_svg_xml = f.read()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # 1. D365 Logo on clean transparent background
        page1 = browser.new_page(viewport={'width': 1200, 'height': 450})
        html1 = f"""<!DOCTYPE html>
<html>
<head><style>
body {{ margin: 0; background: transparent; display: flex; align-items: center; justify-content: center; height: 100vh; }}
svg {{ width: 1000px; height: auto; }}
</style></head>
<body>
{d365_svg_xml}
</body>
</html>"""
        page1.set_content(html1)
        page1.wait_for_timeout(500)
        page1.screenshot(path='assets/microsoft_dynamics_365_logo.png', omit_background=True)
        print("Saved assets/microsoft_dynamics_365_logo.png")
        page1.close()

        # 2. Copilot Logo on clean transparent background
        page2 = browser.new_page(viewport={'width': 800, 'height': 800})
        html2 = f"""<!DOCTYPE html>
<html>
<head><style>
body {{ margin: 0; background: transparent; display: flex; align-items: center; justify-content: center; height: 100vh; }}
svg {{ width: 620px; height: auto; }}
</style></head>
<body>
{copilot_svg_xml}
</body>
</html>"""
        page2.set_content(html2)
        page2.wait_for_timeout(500)
        page2.screenshot(path='assets/microsoft_copilot_logo.png', omit_background=True)
        print("Saved assets/microsoft_copilot_logo.png")
        page2.close()

        # 3. Combined Executive Showcase on Dark Navy Card
        page3 = browser.new_page(viewport={'width': 1280, 'height': 720})
        html3 = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: radial-gradient(circle at 50% 20%, #0f172a 0%, #020617 100%);
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 40px;
}}
.tag {{
  padding: 6px 18px;
  background: rgba(230, 0, 18, 0.15);
  border: 1px solid rgba(230, 0, 18, 0.4);
  color: #ff6b6b;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 12px;
}}
.headline {{
  font-size: 34px;
  font-weight: 900;
  letter-spacing: -0.5px;
  margin-bottom: 40px;
  text-align: center;
}}
.grid {{
  display: grid;
  grid-template-columns: 1fr 90px 1fr;
  gap: 24px;
  width: 100%;
  max-width: 1140px;
  align-items: center;
}}
.card {{
  background: rgba(15, 23, 42, 0.9);
  border-radius: 28px;
  padding: 36px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  height: 380px;
  position: relative;
  transition: transform 0.3s ease;
}}
.card-d365 {{
  border: 2px solid rgba(14, 165, 233, 0.45);
  box-shadow: 0 0 60px rgba(14, 165, 233, 0.18);
}}
.card-copilot {{
  border: 2px solid rgba(168, 85, 247, 0.45);
  box-shadow: 0 0 60px rgba(168, 85, 247, 0.22);
}}
.logo-container {{
  height: 170px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}}
.card-d365 .logo-container svg {{
  max-height: 130px;
  max-width: 90%;
  height: auto;
  width: auto;
}}
.card-copilot .logo-container svg {{
  max-height: 155px;
  max-width: 90%;
  height: auto;
  width: auto;
}}
.card-title {{
  font-size: 20px;
  font-weight: 800;
  margin-top: 24px;
  color: #ffffff;
  letter-spacing: -0.3px;
}}
.card-badge {{
  display: inline-block;
  margin-top: 6px;
  padding: 3px 12px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
}}
.badge-d365 {{
  background: rgba(14, 165, 233, 0.2);
  color: #38bdf8;
  border: 1px solid rgba(14, 165, 233, 0.4);
}}
.badge-copilot {{
  background: rgba(168, 85, 247, 0.2);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.4);
}}
.card-desc {{
  font-size: 13px;
  color: #94a3b8;
  margin-top: 10px;
  text-align: center;
  line-height: 1.5;
  max-width: 380px;
}}
.connector {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
}}
.connector-symbol {{
  font-size: 36px;
  font-weight: 900;
  color: #f43f5e;
  text-shadow: 0 0 25px rgba(244, 63, 94, 0.8);
}}
.connector-label {{
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: #cbd5e1;
  text-transform: uppercase;
}}
</style>
</head>
<body>
  <div class="tag">Official Microsoft Brand Identities</div>
  <div class="headline">Microsoft Dynamics 365 &amp; Microsoft Copilot</div>
  <div class="grid">
    <div class="card card-d365">
      <div class="logo-container">
        {d365_svg_xml}
      </div>
      <div class="card-title">Microsoft Dynamics 365</div>
      <div class="card-badge badge-d365">ENTERPRISE SYSTEM OF RECORD</div>
      <div class="card-desc">รากฐาน ERP สำหรับ Finance &amp; Operations, Supply Chain, บัญชีภาษีไทย และการผลิต</div>
    </div>
    <div class="connector">
      <div class="connector-symbol">✕</div>
      <div class="connector-label">Synergy</div>
    </div>
    <div class="card card-copilot">
      <div class="logo-container">
        {copilot_svg_xml}
      </div>
      <div class="card-title">Microsoft Copilot</div>
      <div class="card-badge badge-copilot">AGENTIC COGNITIVE REASONING</div>
      <div class="card-desc">สมองกลปัญญาประดิษฐ์อัจฉริยะ ทำหน้าที่เป็น Copilot ร่วมคิด วิเคราะห์ และสั่งการอัตโนมัติ</div>
    </div>
  </div>
</body>
</html>"""
        page3.set_content(html3)
        page3.wait_for_timeout(600)
        page3.screenshot(path='assets/microsoft_d365_and_copilot_showcase.png')
        print("Saved assets/microsoft_d365_and_copilot_showcase.png")
        page3.close()

        browser.close()

    # Check non-zero pixel count
    for fname in ['assets/microsoft_dynamics_365_logo.png', 'assets/microsoft_copilot_logo.png', 'assets/microsoft_d365_and_copilot_showcase.png']:
        arr = np.array(Image.open(fname))
        print(f"{fname}: Size {arr.shape[1]}x{arr.shape[0]}, Non-zero pixels = {np.count_nonzero(arr > 0)}")

if __name__ == '__main__':
    main()
