"""
process_ppt_png.py
Extracts and creates transparent background PNGs and slide-ready PNGs for PowerPoint.
"""

import cv2
import numpy as np
from PIL import Image, ImageFilter

INPUT_JPG = 'assets/fujitsu_red_ribbon_text_3d_optionA.jpg'

def make_transparent_png():
    img_bgr = cv2.imread(INPUT_JPG)
    h, w = img_bgr.shape[:2]

    # Convert to LAB for perceptual color distance
    lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    
    # Sample background color from corners
    corners = np.concatenate([
        img_bgr[0:40, 0:40].reshape(-1, 3),
        img_bgr[0:40, -40:].reshape(-1, 3),
        img_bgr[-40:, 0:40].reshape(-1, 3),
        img_bgr[-40:, -40:].reshape(-1, 3)
    ], axis=0)
    bg_bgr = np.median(corners, axis=0)
    bg_lab = cv2.cvtColor(np.uint8([[bg_bgr]]), cv2.COLOR_BGR2LAB).astype(np.float32)[0, 0]

    # Delta E distance from background
    delta_e = np.sqrt(np.sum((lab - bg_lab) ** 2, axis=2))

    # Foreground threshold:
    # Most background is delta_e < 12
    # Ribbon and logos are delta_e > 25
    # Smooth alpha transition between 11 and 22
    alpha = np.clip((delta_e - 10.0) / (22.0 - 10.0), 0.0, 1.0)

    # In the text areas:
    # Left text: y in [420, 520], x in [220, 550]
    # Right text: y in [420, 520], x in [850, 1150]
    # In these regions, ensure text is completely opaque if brightness is high
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    text_mask_l = np.zeros((h, w), dtype=bool)
    text_mask_l[420:530, 220:550] = True
    alpha[text_mask_l & (gray > 200)] = 1.0

    text_mask_r = np.zeros((h, w), dtype=bool)
    text_mask_r[420:530, 850:1150] = True
    alpha[text_mask_r & (gray > 200)] = 1.0

    # Ensure center crossover and ribbon interior are solid
    # Morphological closing to fill tiny specular pinholes on the metallic surface
    alpha_u8 = (alpha * 255).astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    alpha_u8 = cv2.morphologyDefault = cv2.morphologyEx(alpha_u8, cv2.MORPH_CLOSE, kernel)
    
    # Soft feathering on the edges for smooth blending in PowerPoint
    alpha_u8 = cv2.GaussianBlur(alpha_u8, (3, 3), 0)

    # Defringe / color decontamination:
    # Slightly adjust RGB on semi-transparent edge pixels to avoid grey fringing
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    rgba = np.dstack([img_rgb, alpha_u8])

    out_transparent = Image.fromarray(rgba)
    out_transparent.save('assets/fujitsu_red_ribbon_d365_copilot_transparent.png', 'PNG')
    print('Saved assets/fujitsu_red_ribbon_d365_copilot_transparent.png')

    # Also save clean white background version
    white_bg = Image.new('RGB', (w, h), (255, 255, 255))
    white_bg.paste(out_transparent, mask=out_transparent.split()[3])
    white_bg.save('assets/fujitsu_red_ribbon_d365_copilot_clean_white.png', 'PNG')
    print('Saved assets/fujitsu_red_ribbon_d365_copilot_clean_white.png')

    # Also save dark keynote background version
    dark_bg = Image.new('RGB', (w, h), (15, 23, 42))
    dark_bg.paste(out_transparent, mask=out_transparent.split()[3])
    dark_bg.save('assets/fujitsu_red_ribbon_d365_copilot_dark_keynote.png', 'PNG')
    print('Saved assets/fujitsu_red_ribbon_d365_copilot_dark_keynote.png')

if __name__ == '__main__':
    make_transparent_png()
