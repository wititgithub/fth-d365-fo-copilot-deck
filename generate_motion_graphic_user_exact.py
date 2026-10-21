"""
generate_motion_graphic_user_exact.py
Renders 3 distinct high-impact Motion Graphic video and GIF loops based on the user's exact uploaded specification:
- Top-Left: Dynamics 365 in frosted glass shield (slides left-right slightly)
- Top-Right: COMPLETELY REMOVED (no shield)
- Bottom: Copilot in frosted glass shield (slides left-right slightly)
- Background & Ribbon: Option 3 Cinematic Spotlight sweep, specular starbursts on ribbon, central crystal pulse, golden & ruby embers
"""

import os
import math
import cv2
import numpy as np
from PIL import Image

BASE_IMG_PATH = "assets/base_for_user_layout.jpg"
SHIELD_D365_PATH = "assets/shield_d365_topleft.png"
SHIELD_COPILOT_PATH = "assets/shield_copilot_bottom.png"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6  # 108 frames for seamless loop
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Base dimensions
CX, CY = 685, 382
A_LEM, B_LEM = 485, 235

# Positions matching user's uploaded mockup:
# Top-Left: (65, 55)
# Bottom: (550, 480)
D365_BASE_X, D365_BASE_Y = 65, 55
COPILOT_BASE_X, COPILOT_BASE_Y = 550, 480

def get_lemniscate(theta, offset_r=0):
    sin_t = math.sin(theta)
    cos_t = math.cos(theta)
    denom = 1 + sin_t * sin_t
    x = CX + (A_LEM + offset_r) * cos_t / denom
    y = CY + (B_LEM + offset_r * 0.5) * sin_t * cos_t / denom
    return int(x), int(y)

def overlay_rgba(base_bgr, overlay_rgba, x, y, scale=1.0, alpha_mult=1.0):
    oh, ow = overlay_rgba.shape[:2]
    if scale != 1.0:
        new_w = max(1, int(ow * scale))
        new_h = max(1, int(oh * scale))
        ov = cv2.resize(overlay_rgba, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
        x -= (new_w - ow) // 2
        y -= (new_h - oh) // 2
    else:
        ov = overlay_rgba

    h, w = ov.shape[:2]
    bh, bw = base_bgr.shape[:2]

    x1 = max(0, x)
    y1 = max(0, y)
    x2 = min(bw, x + w)
    y2 = min(bh, y + h)

    ox1 = x1 - x
    oy1 = y1 - y
    ox2 = ox1 + (x2 - x1)
    oy2 = oy1 + (y2 - y1)

    if x2 > x1 and y2 > y1:
        crop_base = base_bgr[y1:y2, x1:x2].astype(np.float32)
        crop_ov = ov[oy1:oy2, ox1:ox2]
        ov_bgr = crop_ov[:, :, :3].astype(np.float32)
        ov_alpha = (crop_ov[:, :, 3].astype(np.float32) / 255.0 * alpha_mult)[:, :, np.newaxis]

        blended = crop_base * (1.0 - ov_alpha) + ov_bgr * ov_alpha
        base_bgr[y1:y2, x1:x2] = np.clip(blended, 0, 255).astype(np.uint8)

# -------------------------------------------------------------
# OPTION 1: Pure Left-Right Slide & Classic Option 3 Motion (ตามคำขอเป๊ะๆ)
# -------------------------------------------------------------
def render_user_option1(base_bgr, s_d365, s_copilot):
    print("Rendering User Option 1: Pure Left-Right Slide & Option 3 Cinematic...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_user_option1_pure_slide.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_user_option1_pure_slide.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    # Embers
    num_embers = 40
    np.random.seed(42)
    ember_x = np.random.uniform(150, w - 150, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(30, 80, num_embers)
    ember_sizes = np.random.randint(2, 5, num_embers)

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # 1. Exact horizontal slide requested by user:
        # "โล้ dynamic 365 ให้เลือน ซ้ายขวาได้นิดหน่อย"
        d365_dx = int(16 * math.sin(t))
        # "ส่วนโล้ copilot ให้เลือนซ้ายขวานิดหน่อย"
        copilot_dx = int(16 * math.sin(t + math.pi * 0.7))

        # 2. Sweeping Cinematic Spotlight (Option 3 style)
        spot_x = int(CX + 440 * math.sin(t))
        spot_y = int(CY + 50 * math.cos(t))

        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 260, (255, 235, 190), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (480, 55), 0, 0, 360, (255, 200, 130), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.44, 0, 255).astype(np.uint8)

        # 3. Draw the two shields at their sliding coordinates
        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y)

        # 4. Specular Starburst Gleams on red ribbon crests and shield when spotlight passes
        gleam_overlay = np.zeros_like(frame)
        targets = [
            (D365_BASE_X + 130 + d365_dx, D365_BASE_Y + 130, (0, 220, 255)),
            (390, CY, (255, 255, 255)),
            (CX, CY, (255, 220, 180)),
            (980, CY, (255, 255, 255)),
            (COPILOT_BASE_X + 130 + copilot_dx, COPILOT_BASE_Y + 130, (255, 100, 220))
        ]

        for gx, gy, col in targets:
            dist = abs(spot_x - gx)
            if dist < 130:
                intensity = (1.0 - dist / 130.0) ** 2
                g_rad = int(32 * intensity)
                cv2.line(gleam_overlay, (int(gx - g_rad * 3.5), int(gy)), (int(gx + g_rad * 3.5), int(gy)), (255, 255, 255), 2)
                cv2.line(gleam_overlay, (int(gx), int(gy - g_rad * 2.2)), (int(gx), int(gy + g_rad * 2.2)), (255, 255, 255), 2)
                cv2.circle(gleam_overlay, (int(gx), int(gy)), g_rad, col, -1)

        if np.any(gleam_overlay > 0):
            cv2.GaussianBlur(gleam_overlay, (15, 15), 0, dst=gleam_overlay)
            frame = cv2.add(frame, gleam_overlay)

        # 5. Floating Embers
        ember_overlay = np.zeros_like(frame)
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 20 * math.sin(progress * 4 * math.pi + e_i))
            col = (255, 190, 60) if e_i % 2 == 0 else (140, 50, 255)
            cv2.circle(ember_overlay, (cur_ex, int(cur_ey)), ember_sizes[e_i], col, -1)
        cv2.GaussianBlur(ember_overlay, (7, 7), 0, dst=ember_overlay)
        frame = cv2.add(frame, ember_overlay)

        # 6. Corporate Vignette
        vig = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(vig, (CX, CY), int(w * 0.65), (255, 255, 255), -1)
        cv2.GaussianBlur(vig, (151, 151), 0, dst=vig)
        frame = (frame.astype(np.float32) * (0.86 + 0.14 * (vig / 255.0))).astype(np.uint8)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved User Option 1 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved User Option 1 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 2: Counter-Phase Harmonic Sway & Edge Sparkle Shimmer (แนะนำเพิ่มเติม 1)
# -------------------------------------------------------------
def render_user_option2(base_bgr, s_d365, s_copilot):
    print("Rendering User Option 2: Counter-Phase Sway & Edge Sparkle...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_user_option2_counter_gleam.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_user_option2_counter_gleam.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Counter-phase balanced horizontal slide
        d365_dx = int(18 * math.sin(t))
        copilot_dx = int(-18 * math.sin(t))

        # Proximity breathing scale
        s1 = 1.0 + 0.03 * math.sin(t)
        s2 = 1.0 + 0.03 * math.sin(t + math.pi)

        # Draw shields
        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y, scale=s1)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y, scale=s2)

        # Sparkle shimmer along the red infinity ribbon
        sparkle_overlay = np.zeros_like(frame)
        num_glints = 32
        for g_i in range(num_glints):
            theta_g = g_i * (2 * math.pi / num_glints) + t * 0.8
            gx, gy = get_lemniscate(theta_g, offset_r=14)
            shimmer = 0.5 + 0.5 * math.sin(t * 3 + g_i)
            cv2.circle(sparkle_overlay, (gx, gy), int(2 + 2 * shimmer), (255, 220, 100), -1)

        # Central crossover pulse
        pulse_r = int(70 + 20 * math.sin(t * 2))
        cv2.circle(sparkle_overlay, (CX, CY), pulse_r, (255, 180, 50), 2)

        glow_blur = cv2.GaussianBlur(sparkle_overlay, (15, 15), 0)
        frame = cv2.add(frame, glow_blur)
        frame = cv2.add(frame, sparkle_overlay)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved User Option 2 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved User Option 2 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 3: Spotlight Focus Lock & Dual Beam Flare (แนะนำเพิ่มเติม 2)
# -------------------------------------------------------------
def render_user_option3(base_bgr, s_d365, s_copilot):
    print("Rendering User Option 3: Spotlight Focus Lock & Dual Beam Flare...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_user_option3_spotlight_flare.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_user_option3_spotlight_flare.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Horizontal slide
        d365_dx = int(14 * math.sin(t))
        copilot_dx = int(14 * math.sin(t + math.pi * 0.8))

        d365_cx = D365_BASE_X + 130 + d365_dx
        d365_cy = D365_BASE_Y + 130
        copilot_cx = COPILOT_BASE_X + 130 + copilot_dx
        copilot_cy = COPILOT_BASE_Y + 130

        # Spotlight sweeps from D365 to Center to Copilot
        spot_x = int(CX + 460 * math.sin(t))
        spot_y = int(CY + 80 * math.cos(t))

        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 270, (255, 230, 180), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (480, 50), 0, 0, 360, (255, 200, 130), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.44, 0, 255).astype(np.uint8)

        # Proximity boost
        dist_d = abs(spot_x - d365_cx)
        dist_c = abs(spot_x - copilot_cx)
        boost_d = max(0.0, 1.0 - dist_d / 200.0)
        boost_c = max(0.0, 1.0 - dist_c / 200.0)

        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y, scale=1.0 + 0.05 * boost_d)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y, scale=1.0 + 0.05 * boost_c)

        # Anamorphic horizontal flares when spotlight reaches each shield
        flare_overlay = np.zeros_like(frame)
        if boost_d > 0.25:
            fl_len = int(300 * ((boost_d - 0.25) / 0.75))
            cv2.line(flare_overlay, (d365_cx - fl_len, d365_cy), (d365_cx + fl_len, d365_cy), (255, 220, 0), 2)
            cv2.circle(flare_overlay, (d365_cx, d365_cy), int(35 * boost_d), (255, 255, 255), -1)

        if boost_c > 0.25:
            fl_len = int(300 * ((boost_c - 0.25) / 0.75))
            cv2.line(flare_overlay, (copilot_cx - fl_len, copilot_cy), (copilot_cx + fl_len, copilot_cy), (255, 80, 220), 2)
            cv2.circle(flare_overlay, (copilot_cx, copilot_cy), int(35 * boost_c), (255, 255, 255), -1)

        if np.any(flare_overlay > 0):
            cv2.GaussianBlur(flare_overlay, (15, 15), 0, dst=flare_overlay)
            frame = cv2.add(frame, flare_overlay)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved User Option 3 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved User Option 3 GIF: {gif_path}")

if __name__ == "__main__":
    if not os.path.exists(BASE_IMG_PATH):
        raise FileNotFoundError(f"Missing {BASE_IMG_PATH}")
    base = cv2.imread(BASE_IMG_PATH)
    s_d365 = cv2.imread(SHIELD_D365_PATH, cv2.IMREAD_UNCHANGED)
    s_copilot = cv2.imread(SHIELD_COPILOT_PATH, cv2.IMREAD_UNCHANGED)

    render_user_option1(base, s_d365, s_copilot)
    render_user_option2(base, s_d365, s_copilot)
    render_user_option3(base, s_d365, s_copilot)
    print("All 3 User Exact Motion Graphic options rendered successfully!")
