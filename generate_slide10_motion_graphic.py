"""
generate_slide10_motion_graphic.py
Renders executive-grade motion graphic for Slide 10:
Base: assets/fujitsu_red_ribbon_d365_copilot_clean_white.png
Features:
- Sweeping theatrical studio spotlight across the metallic red infinity ribbon
- Starburst specular gleams on Dynamics 365, Central crossover, and Copilot logos
- Gentle golden & ruby embers drifting upward
- 30 FPS seamless loop (3.6s duration)
"""

import os
import math
import cv2
import numpy as np
from PIL import Image

BASE_IMG_PATH = "assets/fujitsu_red_ribbon_d365_copilot_clean_white.png"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6
TOTAL_FRAMES = int(FPS * DURATION_SEC)

CX, CY = 688, 384
D365_POS = (395, 384)
COPILOT_POS = (980, 384)

def render_slide10_motion():
    print("Rendering Slide 10 Motion Graphic...")
    base_img = cv2.imread(BASE_IMG_PATH)
    if base_img is None:
        raise FileNotFoundError(f"Missing {BASE_IMG_PATH}")
    h, w = base_img.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "slide10_fujitsu_red_infinity_motion.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "slide10_fujitsu_red_infinity_motion.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    # Embers setup
    num_embers = 38
    np.random.seed(42)
    ember_x = np.random.uniform(180, w - 180, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(25, 70, num_embers)
    ember_sizes = np.random.randint(2, 4, num_embers)

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_img.copy()

        # 1. Sweeping Theatrical Spotlight
        spot_x = int(CX + 440 * math.sin(t))
        spot_y = int(CY + 40 * math.cos(t))

        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 260, (255, 235, 190), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (480, 50), 0, 0, 360, (255, 205, 130), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.42, 0, 255).astype(np.uint8)

        # 2. Specular Starburst Gleams when Spotlight sweeps past key brand elements
        gleam_overlay = np.zeros_like(frame)
        targets = [
            (D365_POS[0], D365_POS[1], (0, 210, 255), "d365"),
            (CX, CY, (255, 220, 150), "center"),
            (COPILOT_POS[0], COPILOT_POS[1], (255, 80, 220), "copilot")
        ]

        for gx, gy, col, name in targets:
            dist = abs(spot_x - gx)
            if dist < 140:
                intensity = (1.0 - dist / 140.0) ** 2
                g_rad = int(34 * intensity)
                # 4-point star
                cv2.line(gleam_overlay, (int(gx - g_rad * 3.6), int(gy)), (int(gx + g_rad * 3.6), int(gy)), (255, 255, 255), 2)
                cv2.line(gleam_overlay, (int(gx), int(gy - g_rad * 2.2)), (int(gx), int(gy + g_rad * 2.2)), (255, 255, 255), 2)
                cv2.circle(gleam_overlay, (int(gx), int(gy)), g_rad, col, -1)
                # Soft ring
                cv2.circle(gleam_overlay, (int(gx), int(gy)), int(g_rad * 1.6), col, 2)

        if np.any(gleam_overlay > 0):
            cv2.GaussianBlur(gleam_overlay, (15, 15), 0, dst=gleam_overlay)
            frame = cv2.add(frame, gleam_overlay)

        # 3. Floating Gold & Ruby Embers
        ember_overlay = np.zeros_like(frame)
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 18 * math.sin(progress * 4 * math.pi + e_i))
            col = (255, 200, 80) if e_i % 2 == 0 else (160, 40, 240)
            cv2.circle(ember_overlay, (cur_ex, int(cur_ey)), ember_sizes[e_i], col, -1)

        cv2.GaussianBlur(ember_overlay, (7, 7), 0, dst=ember_overlay)
        frame = cv2.add(frame, ember_overlay)

        # 4. Vignette for depth
        vig = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(vig, (CX, CY), int(w * 0.65), (255, 255, 255), -1)
        cv2.GaussianBlur(vig, (151, 151), 0, dst=vig)
        frame = (frame.astype(np.float32) * (0.87 + 0.13 * (vig / 255.0))).astype(np.uint8)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved GIF: {gif_path}")

if __name__ == "__main__":
    render_slide10_motion()
