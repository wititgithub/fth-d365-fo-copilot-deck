"""
create_d365_icon.py
Extracts the standalone D365 icon (faceted D monogram) and renders it to high-res PNG.
"""

import re
from playwright.sync_api import sync_playwright

with open('assets/microsoft_dynamics_365_logo.svg', 'r', encoding='utf-8') as f:
    full_svg = f.read()

# Change viewBox to 0 0 355.1 355.1 to isolate the icon
icon_svg = re.sub(r'viewBox="0 0 1017.4 355.1"', 'viewBox="0 0 355.1 355.1"', full_svg)

with open('assets/microsoft_dynamics_365_icon.svg', 'w', encoding='utf-8') as f:
    f.write(icon_svg)
print("Saved assets/microsoft_dynamics_365_icon.svg")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 800, 'height': 800})
    html = f"""<!DOCTYPE html>
<html>
<head><style>
body {{ margin:0; background:transparent; display:flex; align-items:center; justify-content:center; height:100vh; }}
svg {{ width: 620px; height: 620px; }}
</style></head>
<body>
{icon_svg}
</body>
</html>"""
    page.set_content(html)
    page.wait_for_timeout(400)
    page.screenshot(path='assets/microsoft_dynamics_365_icon.png', omit_background=True)
    print("Saved assets/microsoft_dynamics_365_icon.png")
    browser.close()
