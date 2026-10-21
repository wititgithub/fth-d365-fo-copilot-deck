"""
verify_png_on_slides.py
Creates a visual proof showing the transparent PNG pasted onto:
1. Pure White PowerPoint Slide
2. Deep Navy Executive PowerPoint Slide
3. Gradient Corporate PowerPoint Slide
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

fg = Image.open('assets/fujitsu_red_ribbon_d365_copilot_transparent.png')
# Resize for slide display: 800 width
scale = 800 / fg.width
fg_small = fg.resize((800, int(fg.height * scale)), Image.Resampling.LANCZOS)

# Create a 3-panel comparison sheet
sheet = Image.new('RGB', (1200, 960), (241, 245, 249))

# Panel 1: Pure White Slide (Top)
panel1 = Image.new('RGB', (1120, 280), (255, 255, 255))
panel1.paste(fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS), (280, 10), mask=fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS).split()[3])

# Panel 2: Deep Navy Dark Slide (Middle)
panel2 = Image.new('RGB', (1120, 280), (15, 23, 42))
panel2.paste(fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS), (280, 10), mask=fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS).split()[3])

# Panel 3: Slate Gradient Slide (Bottom)
panel3 = Image.new('RGB', (1120, 280), (30, 41, 59))
panel3.paste(fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS), (280, 10), mask=fg_small.resize((int(fg_small.width*0.65), int(fg_small.height*0.65)), Image.Resampling.LANCZOS).split()[3])

sheet.paste(panel1, (40, 40))
sheet.paste(panel2, (40, 350))
sheet.paste(panel3, (40, 660))

sheet.save('assets/ppt_transparency_proof.png')
print('Saved assets/ppt_transparency_proof.png')
