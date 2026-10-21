"""
generate_motion_graphic_infinity_sparkle.py
Renders 3 distinct high-impact Motion Graphic video and GIF loops with:
"วิ้งตามขอบโบว์สีแดง หรือ ตัว infinity ไปเรื่อยๆ พร้อมโล่โปร่งแสง Dynamics 365 และ Copilot แยกห่างกันอย่างสวยงาม"
"""

import os
import math
import cv2
import numpy as np
from PIL import Image

BASE_IMG_PATH = "assets/base_inpainted_shields.jpg"
SHIELD_D365_PATH = "assets/shield_d365_v2.png"
SHIELD_COPILOT_PATH = "assets/shield_copilot_v2.png"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6  # 108 frames for smooth seamless loop
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Base dimensions
CX, CY = 685, 382
A_LEM, B_LEM = 485, 235

# Shield positions (spaced apart beautifully on left and right loops)
D365_X, D365_Y = 65, 55
COPILOT_X, COPILOT_Y = 1025, 55

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

def draw_starburst(canvas, cx, cy, rad, color, points=4, angle_deg=0):
    """Draws a bright cinematic starburst glint"""
    rad_rad = math.radians(angle_deg)
    for p in range(points):
        a = rad_rad + p * (math.pi / points)
        length = rad * (3.5 if p % 2 == 0 else 2.2)
        dx = length * math.cos(a)
        dy = length * math.sin(a)
        cv2.line(canvas, (int(cx - dx), int(cy - dy)), (int(cx + dx), int(cy + dy)), (255, 255, 255), 2)
        cv2.line(canvas, (int(cx - dx*0.7), int(cy - dy*0.7)), (int(cx + dx*0.7), int(cy + dy*0.7)), color, 3)
    cv2.circle(canvas, (int(cx), int(cy)), int(rad * 0.8), (255, 255, 255), -1)
    cv2.circle(canvas, (int(cx), int(cy)), int(rad * 1.5), color, 2)

# -------------------------------------------------------------
# OPTION 1: Prismatic Edge Tracer & Glass Resonance
# (ลำแสงโฟตอนประกายเพชรวิ่งลูบขอบโบว์อินฟินิตี้ & แสงสะท้อนโล่โปร่งแสง)
# -------------------------------------------------------------
def render_sparkle_option1(base_bgr, s_d365, s_copilot):
    print("Rendering Sparkle Option 1: Prismatic Edge Tracer...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option1_edge_tracer.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option1_edge_tracer.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    # Embers
    num_embers = 40
    np.random.seed(42)
    ember_x = np.random.uniform(150, w - 150, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(30, 80, num_embers)

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Shields gentle out-of-phase floating
        d365_dy = int(14 * math.sin(t))
        d365_dx = int(4 * math.cos(t))
        copilot_dy = int(14 * math.sin(t + math.pi))
        copilot_dx = int(-4 * math.cos(t))

        # Main Photon Sparkle racing along infinity contour (theta: 0 to 2pi)
        theta_main = t
        sparkle_x, sparkle_y = get_lemniscate(theta_main, offset_r=15)

        # Draw Shields onto frame
        d365_cx = D365_X + 145 + d365_dx
        d365_cy = D365_Y + 140 + d365_dy
        copilot_cx = COPILOT_X + 145 + copilot_dx
        copilot_cy = COPILOT_Y + 140 + copilot_dy

        # Check proximity of sparkle to shields for glass resonance
        dist_d365 = math.hypot(sparkle_x - d365_cx, sparkle_y - d365_cy)
        dist_copilot = math.hypot(sparkle_x - copilot_cx, sparkle_y - copilot_cy)

        d365_glint = max(0.0, 1.0 - dist_d365 / 220.0)
        copilot_glint = max(0.0, 1.0 - dist_copilot / 220.0)

        # Scale shields slightly on resonance
        overlay_rgba(frame, s_d365, D365_X + d365_dx, D365_Y + d365_dy, scale=1.0 + 0.05 * d365_glint)
        overlay_rgba(frame, s_copilot, COPILOT_X + copilot_dx, COPILOT_Y + copilot_dy, scale=1.0 + 0.05 * copilot_glint)

        # SPARKLE LAYER (Gleam & Trail along infinity edge)
        sparkle_overlay = np.zeros_like(frame)

        # 1. Shimmering Ribbon Trail (15 lagging trail segments along curve)
        for trail_step in range(1, 24):
            t_lag = theta_main - trail_step * 0.045
            tx, ty = get_lemniscate(t_lag, offset_r=15)
            alpha_trail = (1.0 - trail_step / 24.0) ** 1.8
            trail_rad = max(2, int(9 * alpha_trail))
            # Trail color shifts from gold to ruby to cyan
            col_trail = (255, int(220 * alpha_trail), int(100 * alpha_trail))
            cv2.circle(sparkle_overlay, (tx, ty), trail_rad, col_trail, -1)

            # Secondary inner rim trail
            tx_in, ty_in = get_lemniscate(t_lag, offset_r=-15)
            cv2.circle(sparkle_overlay, (tx_in, ty_in), max(1, int(5 * alpha_trail)), (255, 100, 200), -1)

        # 2. Main High-Intensity Diamond Starburst Glint
        star_angle = (progress * 360 * 2) % 360
        draw_starburst(sparkle_overlay, sparkle_x, sparkle_y, rad=18, color=(255, 230, 80), points=4, angle_deg=star_angle)

        # 3. Shield Glass Resonance Flares
        if d365_glint > 0.15:
            # Azure glass edge flare
            flare_rad = int(35 * d365_glint)
            draw_starburst(sparkle_overlay, d365_cx, d365_cy - 40, rad=flare_rad, color=(0, 220, 255), points=4, angle_deg=45)
            cv2.circle(sparkle_overlay, (d365_cx, d365_cy), int(90 * d365_glint), (0, 240, 255), 2)

        if copilot_glint > 0.15:
            # Prism magenta flare
            flare_rad = int(35 * copilot_glint)
            draw_starburst(sparkle_overlay, copilot_cx, copilot_cy - 40, rad=flare_rad, color=(255, 50, 200), points=4, angle_deg=45)
            cv2.circle(sparkle_overlay, (copilot_cx, copilot_cy), int(90 * copilot_glint), (255, 80, 220), 2)

        # 4. Floating Embers
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 20 * math.sin(progress * 4 * math.pi + e_i))
            col = (255, 210, 80) if e_i % 2 == 0 else (180, 50, 255)
            cv2.circle(sparkle_overlay, (cur_ex, int(cur_ey)), 3, col, -1)

        # Soft blur glow for sparkles
        glow_blur = cv2.GaussianBlur(sparkle_overlay, (15, 15), 0)
        frame = cv2.add(frame, glow_blur)
        frame = cv2.add(frame, sparkle_overlay)

        # Soft vignette
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
    print(f"Saved Sparkle Option 1 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Sparkle Option 1 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 2: Dual Counter-Rotating Light Streams & Quantum Surge
# (ลำแสงวิ่งวนคู่สองทิศทาง & คลื่นพัลส์ประกายขอบ)
# -------------------------------------------------------------
def render_sparkle_option2(base_bgr, s_d365, s_copilot):
    print("Rendering Sparkle Option 2: Dual Counter-Rotating Light Streams...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option2_dual_streams.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option2_dual_streams.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Shields sway along orbital curve
        d365_dx = int(10 * math.cos(t * 1.2))
        d365_dy = int(12 * math.sin(t * 1.2))
        copilot_dx = int(-10 * math.cos(t * 1.2))
        copilot_dy = int(-12 * math.sin(t * 1.2))

        d365_cx = D365_X + 145 + d365_dx
        d365_cy = D365_Y + 140 + d365_dy
        copilot_cx = COPILOT_X + 145 + copilot_dx
        copilot_cy = COPILOT_Y + 140 + copilot_dy

        # Stream 1: Clockwise Light Stream (Azure / D365)
        t_stream1 = t
        sx1, sy1 = get_lemniscate(t_stream1, offset_r=18)

        # Stream 2: Counter-Clockwise Light Stream (Magenta / Copilot)
        t_stream2 = -t + math.pi
        sx2, sy2 = get_lemniscate(t_stream2, offset_r=-18)

        # Pulse breathing scale on shields
        d365_pulse = 1.0 + 0.04 * math.sin(t * 2)
        copilot_pulse = 1.0 + 0.04 * math.sin(t * 2 + math.pi)

        overlay_rgba(frame, s_d365, D365_X + d365_dx, D365_Y + d365_dy, scale=d365_pulse)
        overlay_rgba(frame, s_copilot, COPILOT_X + copilot_dx, COPILOT_Y + copilot_dy, scale=copilot_pulse)

        sparkle_overlay = np.zeros_like(frame)

        # 1. Stream 1 Trails (Azure Cyan)
        for step in range(1, 20):
            prog_s = t_stream1 - step * 0.05
            px, py = get_lemniscate(prog_s, offset_r=18)
            alpha_s = (1.0 - step / 20.0) ** 1.5
            cv2.circle(sparkle_overlay, (px, py), max(2, int(8 * alpha_s)), (255, 230, 0), -1)

        # 2. Stream 2 Trails (Violet Magenta)
        for step in range(1, 20):
            prog_s = t_stream2 + step * 0.05
            px, py = get_lemniscate(prog_s, offset_r=-18)
            alpha_s = (1.0 - step / 20.0) ** 1.5
            cv2.circle(sparkle_overlay, (px, py), max(2, int(8 * alpha_s)), (255, 50, 180), -1)

        # 3. Main Head Starbursts
        draw_starburst(sparkle_overlay, sx1, sy1, rad=16, color=(255, 240, 0), points=4, angle_deg=t * 180 / math.pi)
        draw_starburst(sparkle_overlay, sx2, sy2, rad=16, color=(255, 50, 220), points=4, angle_deg=-t * 180 / math.pi)

        # 4. Central Crossover Collision Shockwaves
        # Streams cross at CX, CY when t is near pi/2 or 3pi/2
        cross_dist = math.hypot(sx1 - sx2, sy1 - sy2)
        if cross_dist < 100:
            burst_int = (1.0 - cross_dist / 100.0) ** 2
            cv2.circle(sparkle_overlay, (CX, CY), int(60 * burst_int), (255, 255, 255), -1)
            cv2.circle(sparkle_overlay, (CX, CY), int(120 * burst_int), (255, 200, 50), 3)

        # 5. Continuous perimeter glow along the entire infinity ribbon
        for i in range(48):
            rad_i = i * (2 * math.pi / 48)
            ix, iy = get_lemniscate(rad_i, offset_r=0)
            shimmer = 0.5 + 0.5 * math.sin(t * 4 + i)
            cv2.circle(sparkle_overlay, (ix, iy), int(2 + 2 * shimmer), (255, 180, 220), -1)

        glow_blur = cv2.GaussianBlur(sparkle_overlay, (17, 17), 0)
        frame = cv2.add(frame, glow_blur)
        frame = cv2.add(frame, sparkle_overlay)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved Sparkle Option 2 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Sparkle Option 2 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 3: Cinematic Anamorphic Laser Sweep & Starlight Embers
# (เลนส์แฟลร์ภาพยนตร์ & ลำแสงเลเซอร์วิ้งขอบโบว์)
# -------------------------------------------------------------
def render_sparkle_option3(base_bgr, s_d365, s_copilot):
    print("Rendering Sparkle Option 3: Cinematic Anamorphic Laser Sweep...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option3_laser_sweep.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_sparkle_option3_laser_sweep.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Sweeping horizontal theatrical spotlight
        spot_x = int(CX + 450 * math.sin(t))
        spot_y = int(CY + 40 * math.cos(t))

        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 270, (255, 230, 180), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (500, 50), 0, 0, 360, (255, 200, 130), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.44, 0, 255).astype(np.uint8)

        # Gyroscopic dual-axis hover for shields
        d365_dy = int(12 * math.sin(t))
        d365_dx = int(5 * math.cos(t))
        copilot_dy = int(12 * math.sin(t + math.pi))
        copilot_dx = int(-5 * math.cos(t))

        d365_cx = D365_X + 145 + d365_dx
        d365_cy = D365_Y + 140 + d365_dy
        copilot_cx = COPILOT_X + 145 + copilot_dx
        copilot_cy = COPILOT_Y + 140 + copilot_dy

        # Infinity Edge Sparkle Tracer (sync with spotlight sweep)
        theta_sparkle = t * 1.5
        sp_x, sp_y = get_lemniscate(theta_sparkle, offset_r=16)

        overlay_rgba(frame, s_d365, D365_X + d365_dx, D365_Y + d365_dy, scale=1.02)
        overlay_rgba(frame, s_copilot, COPILOT_X + copilot_dx, COPILOT_Y + copilot_dy, scale=1.02)

        sparkle_overlay = np.zeros_like(frame)

        # 1. Continuous Sparkle Trail along infinity ribbon
        for tr in range(1, 28):
            tr_theta = theta_sparkle - tr * 0.04
            tx, ty = get_lemniscate(tr_theta, offset_r=16)
            alpha_tr = (1.0 - tr / 28.0) ** 1.6
            cv2.circle(sparkle_overlay, (tx, ty), max(2, int(10 * alpha_tr)), (255, int(200 * alpha_tr), 50), -1)

        # 2. Main Diamond Starlight Starburst
        draw_starburst(sparkle_overlay, sp_x, sp_y, rad=22, color=(255, 240, 100), points=6, angle_deg=t * 90)

        # 3. Horizontal Anamorphic Laser Flare when Spotlight strikes crests
        dist_d = abs(spot_x - d365_cx)
        dist_c = abs(spot_x - copilot_cx)

        if dist_d < 160:
            intens = (1.0 - dist_d / 160.0) ** 2
            fl_len = int(320 * intens)
            cv2.line(sparkle_overlay, (d365_cx - fl_len, d365_cy), (d365_cx + fl_len, d365_cy), (255, 220, 0), 2)
            cv2.circle(sparkle_overlay, (d365_cx, d365_cy), int(35 * intens), (255, 255, 255), -1)

        if dist_c < 160:
            intens = (1.0 - dist_c / 160.0) ** 2
            fl_len = int(320 * intens)
            cv2.line(sparkle_overlay, (copilot_cx - fl_len, copilot_cy), (copilot_cx + fl_len, copilot_cy), (255, 80, 220), 2)
            cv2.circle(sparkle_overlay, (copilot_cx, copilot_cy), int(35 * intens), (255, 255, 255), -1)

        # 4. Vignette
        glow_blur = cv2.GaussianBlur(sparkle_overlay, (15, 15), 0)
        frame = cv2.add(frame, glow_blur)
        frame = cv2.add(frame, sparkle_overlay)

        vig = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(vig, (CX, CY), int(w * 0.65), (255, 255, 255), -1)
        cv2.GaussianBlur(vig, (151, 151), 0, dst=vig)
        frame = (frame.astype(np.float32) * (0.85 + 0.15 * (vig / 255.0))).astype(np.uint8)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved Sparkle Option 3 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Sparkle Option 3 GIF: {gif_path}")

if __name__ == "__main__":
    if not os.path.exists(BASE_IMG_PATH):
        raise FileNotFoundError(f"Missing {BASE_IMG_PATH}")
    base = cv2.imread(BASE_IMG_PATH)
    s_d365 = cv2.imread(SHIELD_D365_PATH, cv2.IMREAD_UNCHANGED)
    s_copilot = cv2.imread(SHIELD_COPILOT_PATH, cv2.IMREAD_UNCHANGED)

    render_sparkle_option1(base, s_d365, s_copilot)
    render_sparkle_option2(base, s_d365, s_copilot)
    render_sparkle_option3(base, s_d365, s_copilot)
    print("All 3 Infinity Sparkle Motion Graphic options rendered successfully!")
