"""
generate_slide9_dark_infinity_motion.py
Renders executive-grade Dark Navy motion graphic for Finale Slide:
Theme: Deep Executive Navy (#101e30 / #0d1726) matching Slides 1-8
Elements: Red Infinity loop, Dynamics 365 icon, Microsoft Copilot icon
Features:
- Seamless harmonic floating breathing movement (sine oscillation)
- Sweeping theatrical studio spotlight across the metallic red loop
- Specular starburst gleams on Dynamics 365, Center Crossover, and Copilot
- Ambient glowing ruby & cyan micro-embers in dark space
- Polished studio floor reflection and volumetric glow
- 30 FPS seamless loop (3.6s)
"""

import os
import math
import cv2
import numpy as np
from PIL import Image

RIBBON_TRANSPARENT_PATH = "assets/fujitsu_red_ribbon_d365_copilot_transparent.png"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Approximate centers in 1376x768
CX, CY = 688, 384
D365_POS = (395, 384)
COPILOT_POS = (980, 384)

def build_dark_studio_stage(w, h):
    """Creates a high-end dark slate navy studio stage with floor reflection."""
    stage = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        ratio = y / h
        # Top: #0a111a -> Bottom: #132134
        b = int(26 + 26 * ratio)
        g = int(17 + 16 * ratio)
        r = int(10 + 10 * ratio)
        stage[y, :] = (b, g, r)
    
    # Soft center radial ambient glow
    ambient = np.zeros_like(stage, dtype=np.float32)
    cv2.circle(ambient, (CX, CY), int(w * 0.45), (45, 28, 18), -1)
    cv2.ellipse(ambient, (CX, int(h * 0.85)), (int(w * 0.38), int(h * 0.15)), 0, 0, 360, (55, 32, 20), -1)
    cv2.GaussianBlur(ambient, (121, 121), 0, dst=ambient)
    stage = np.clip(stage.astype(np.float32) + ambient, 0, 255).astype(np.uint8)
    return stage

def render_dark_infinity_motion():
    print("Rendering Slide 9 Dark Infinity Motion Graphic...")
    ribbon_rgba = cv2.imread(RIBBON_TRANSPARENT_PATH, cv2.IMREAD_UNCHANGED)
    if ribbon_rgba is None:
        raise FileNotFoundError(f"Missing {RIBBON_TRANSPARENT_PATH}")
    
    h, w = ribbon_rgba.shape[:2]
    base_stage = build_dark_studio_stage(w, h)
    
    # Precompute ribbon channels
    rib_bgr = ribbon_rgba[:, :, :3].astype(np.float32)
    rib_alpha = (ribbon_rgba[:, :, 3].astype(np.float32) / 255.0)[:, :, np.newaxis]
    
    # Precompute floor reflection of the ribbon
    reflected_ribbon = cv2.flip(rib_bgr, 0)
    reflected_alpha = cv2.flip(rib_alpha, 0) * 0.22  # subtle mirror reflection
    
    # Video Writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "slide9_fujitsu_red_infinity_dark.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "slide9_fujitsu_red_infinity_dark.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))
    
    gif_frames = []
    
    # Embers setup
    num_embers = 36
    np.random.seed(101)
    ember_x = np.random.uniform(160, w - 160, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(20, 55, num_embers)
    ember_sizes = np.random.randint(2, 4, num_embers)
    ember_colors = [
        (255, 100, 100),  # ruby
        (255, 200, 90),   # golden
        (255, 230, 160),  # warm white
        (230, 120, 255)   # soft copilot violet
    ]
    
    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2.0 * math.pi
        
        # 1. Subtle Harmonic Float / Breathing
        # Slight vertical hover: -5 to +5 px
        dy = int(5.0 * math.sin(t))
        # Slight scale breathing: 1.000 to 1.012
        scale = 1.0 + 0.008 * math.sin(t)
        
        # Start with fresh stage background
        frame = base_stage.copy().astype(np.float32)
        
        # 2. Render Floor Reflection with vertical perspective squash
        refl_y_offset = int(h * 0.72)
        refl_h = int(h * 0.28)
        if refl_h > 0:
            refl_slice = cv2.resize(reflected_ribbon[int(h*0.3):, :], (w, refl_h), interpolation=cv2.INTER_LINEAR)
            refl_a_slice = cv2.resize(reflected_alpha[int(h*0.3):, :], (w, refl_h), interpolation=cv2.INTER_LINEAR)[:, :, np.newaxis]
            # Fade reflection towards bottom
            fade = np.linspace(1.0, 0.0, refl_h)[:, np.newaxis, np.newaxis]
            refl_a_slice *= fade
            
            frame[refl_y_offset:refl_y_offset+refl_h, :] = (
                frame[refl_y_offset:refl_y_offset+refl_h, :] * (1.0 - refl_a_slice) +
                refl_slice * refl_a_slice
            )
        
        # 3. Composite Main Ribbon with subtle float dy
        M = np.float32([[1, 0, 0], [0, 1, dy]])
        shifted_bgr = cv2.warpAffine(rib_bgr, M, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
        shifted_alpha = cv2.warpAffine(rib_alpha, M, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=0)[:, :, np.newaxis]
        
        frame = frame * (1.0 - shifted_alpha) + shifted_bgr * shifted_alpha
        
        # 4. Sweeping Studio Spotlight
        spot_x = int(CX + 450 * math.sin(t))
        spot_y = int(CY + 30 * math.cos(t) + dy)
        
        beam = np.zeros((h, w, 3), dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 240, (180, 150, 120), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (420, 60), 0, 0, 360, (220, 170, 130), -1)
        cv2.GaussianBlur(beam, (121, 121), 0, dst=beam)
        
        # Apply spotlight primarily on the ribbon
        spot_effect = beam * (shifted_alpha * 0.45 + 0.10)
        frame = np.clip(frame + spot_effect, 0, 255)
        
        # 5. Specular Starburst Gleams on Key Elements
        gleam_overlay = np.zeros((h, w, 3), dtype=np.float32)
        targets = [
            (D365_POS[0], D365_POS[1] + dy, (255, 200, 80), "d365"),      # Azure/Gold
            (CX, CY + dy, (120, 100, 255), "center"),                       # Radiant Ruby
            (COPILOT_POS[0], COPILOT_POS[1] + dy, (255, 120, 220), "copilot") # Violet/Pink
        ]
        
        for gx, gy, col, name in targets:
            dist = abs(spot_x - gx)
            if dist < 150:
                intensity = ((1.0 - dist / 150.0) ** 2.2)
                g_rad = int(32 * intensity)
                if g_rad > 2:
                    # 4-point dynamic star
                    arm_h = int(g_rad * 3.8)
                    arm_v = int(g_rad * 2.4)
                    cv2.line(gleam_overlay, (int(gx - arm_h), int(gy)), (int(gx + arm_h), int(gy)), (255, 255, 255), 2)
                    cv2.line(gleam_overlay, (int(gx), int(gy - arm_v)), (int(gx), int(gy + arm_v)), (255, 255, 255), 2)
                    # Core glow
                    cv2.circle(gleam_overlay, (int(gx), int(gy)), g_rad, col, -1)
                    # Corona ring
                    cv2.circle(gleam_overlay, (int(gx), int(gy)), int(g_rad * 1.5), col, 1)
        
        if np.any(gleam_overlay > 0):
            cv2.GaussianBlur(gleam_overlay, (15, 15), 0, dst=gleam_overlay)
            frame = np.clip(frame + gleam_overlay, 0, 255)
            
        # 6. Floating Ruby and Gold Embers
        ember_overlay = np.zeros((h, w, 3), dtype=np.float32)
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 16 * math.sin(progress * 4.0 * math.pi + e_i))
            col = ember_colors[e_i % len(ember_colors)]
            cv2.circle(ember_overlay, (cur_ex, int(cur_ey)), ember_sizes[e_i], col, -1)
            
        cv2.GaussianBlur(ember_overlay, (5, 5), 0, dst=ember_overlay)
        frame = np.clip(frame + ember_overlay, 0, 255)
        
        # 7. Convert to uint8
        frame_u8 = frame.astype(np.uint8)
        out.write(frame_u8)
        
        # Save every frame for GIF (at 800px width for fast loading & smooth playback)
        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame_u8, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
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
    
    # Also copy/overwrite slide10_fujitsu_red_infinity_motion.gif/mp4 so any existing references get the dark theme!
    legacy_gif = os.path.join(OUTPUT_DIR, "slide10_fujitsu_red_infinity_motion.gif")
    legacy_mp4 = os.path.join(OUTPUT_DIR, "slide10_fujitsu_red_infinity_motion.mp4")
    import shutil
    shutil.copyfile(gif_path, legacy_gif)
    shutil.copyfile(mp4_path, legacy_mp4)
    print("Updated legacy motion assets with dark theme")

if __name__ == "__main__":
    render_dark_infinity_motion()
