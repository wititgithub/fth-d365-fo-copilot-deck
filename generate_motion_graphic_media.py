"""
generate_motion_graphic_media.py
Generates 3 distinct high-impact Motion Graphic video and GIF loops from fujitsu_copilot_value_3d.jpg:
1. Option 1: Quantum Neural Pulse & Infinity Flow
2. Option 2: Executive Cybernetic HUD & Telemetry Orbit
3. Option 3: Cinematic Spotlight & Metallic Gleam
"""

import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE_IMG_PATH = "assets/fujitsu_copilot_value_3d.jpg"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6  # 108 frames for a smooth seamless loop
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Base coordinates on 1376x768 image
CX, CY = 685, 382
A_LEM, B_LEM = 475, 230  # Lemniscate parameters

BADGES = [
    {"name": "IP Asset", "pos": (195, 190), "box": (100, 70, 290, 270)},
    {"name": "Human-in-the-Loop", "pos": (1180, 190), "box": (1070, 70, 1290, 270)},
    {"name": "70% Faster", "pos": (685, 650), "box": (585, 570, 785, 730)}
]

def get_lemniscate_point(theta):
    sin_t = math.sin(theta)
    cos_t = math.cos(theta)
    denom = 1 + sin_t * sin_t
    x = CX + A_LEM * cos_t / denom
    y = CY + B_LEM * sin_t * cos_t / denom
    return int(x), int(y)

def create_radial_glow(size, color, max_alpha=0.8):
    """Creates a transparent RGBA glow circle"""
    glow = np.zeros((size, size, 4), dtype=np.uint8)
    radius = size / 2.0
    for y in range(size):
        for x in range(size):
            dist = math.hypot(x - radius, y - radius)
            if dist < radius:
                factor = (1.0 - dist / radius) ** 2
                alpha = int(255 * factor * max_alpha)
                glow[y, x] = [color[0], color[1], color[2], alpha]
    return glow

def blend_glow(base, glow, center_x, center_y):
    """Blends an RGBA glow onto a BGR base image using additive/screen blending"""
    gh, gw = glow.shape[:2]
    x1 = max(0, center_x - gw // 2)
    y1 = max(0, center_y - gh // 2)
    x2 = min(base.shape[1], center_x + gw // 2)
    y2 = min(base.shape[0], center_y + gh // 2)

    gx1 = x1 - (center_x - gw // 2)
    gy1 = y1 - (center_y - gh // 2)
    gx2 = gx1 + (x2 - x1)
    gy2 = gy1 + (y2 - y1)

    if x2 > x1 and y2 > y1:
        crop_base = base[y1:y2, x1:x2].astype(np.float32)
        crop_glow = glow[gy1:gy2, gx1:gx2]
        glow_bgr = crop_glow[:, :, :3].astype(np.float32)
        glow_alpha = (crop_glow[:, :, 3].astype(np.float32) / 255.0)[:, :, np.newaxis]

        # Additive screen blend
        blended = crop_base + glow_bgr * glow_alpha
        blended = np.clip(blended, 0, 255).astype(np.uint8)
        base[y1:y2, x1:x2] = blended

# -------------------------------------------------------------
# OPTION 1: Quantum Neural Pulse & Infinity Flow
# -------------------------------------------------------------
def render_option1(base_img):
    print("Rendering Option 1: Quantum Neural Pulse & Infinity Flow...")
    h, w = base_img.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_option1_quantum_pulse.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_option1_quantum_pulse.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []
    
    # Pre-calculate particles along the infinity curve
    num_particles = 48
    particle_offsets = [i * (2 * math.pi / num_particles) for i in range(num_particles)]
    particle_speeds = [1.0 if i % 2 == 0 else 1.25 for i in range(num_particles)]
    particle_colors = [
        (255, 120, 0) if i % 3 == 0 else ((255, 0, 80) if i % 3 == 1 else (200, 255, 50))
        for i in range(num_particles)
    ]

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_img.copy()

        # 1. Pulsing Core Caustic Glow
        pulse = 0.5 + 0.5 * math.sin(t * 2)
        core_radius = int(140 + 35 * pulse)
        # Create subtle radial cyan/violet glow at core
        glow_overlay = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(glow_overlay, (CX, CY), core_radius, (255, 230, 80), -1)
        cv2.circle(glow_overlay, (CX, CY), int(core_radius * 0.6), (255, 150, 200), -1)
        cv2.GaussianBlur(glow_overlay, (101, 101), 0, dst=glow_overlay)
        frame = np.clip(frame.astype(np.float32) + glow_overlay * (0.35 + 0.25 * pulse), 0, 255).astype(np.uint8)

        # 2. Concentric expanding wave rings
        for ring_i in range(3):
            ring_progress = (progress + ring_i / 3.0) % 1.0
            r_rad = int(50 + 260 * ring_progress)
            r_alpha = (1.0 - ring_progress) * 0.4
            ring_overlay = np.zeros_like(frame)
            cv2.circle(ring_overlay, (CX, CY), r_rad, (255, 220, 100), 2)
            cv2.GaussianBlur(ring_overlay, (9, 9), 0, dst=ring_overlay)
            frame = cv2.addWeighted(frame, 1.0, ring_overlay, r_alpha, 0)

        # 3. Lemniscate Flowing Photons (Particles + Trails)
        overlay_particles = np.zeros_like(frame)
        for i, (offset, speed, col) in enumerate(zip(particle_offsets, particle_speeds, particle_colors)):
            cur_theta = offset + t * speed
            px, py = get_lemniscate_point(cur_theta)
            
            # Particle size and brightness increases near center crystal
            dist_to_center = math.hypot(px - CX, py - CY)
            center_boost = max(0.0, 1.0 - dist_to_center / 350.0)
            p_size = int(3 + 4 * center_boost)

            # Draw particle head
            cv2.circle(overlay_particles, (px, py), p_size, col, -1)
            cv2.circle(overlay_particles, (px, py), p_size + 2, (255, 255, 255), 1)

            # Draw glowing trail
            for trail_step in range(1, 6):
                trail_theta = cur_theta - trail_step * 0.05 * speed
                tpx, tpy = get_lemniscate_point(trail_theta)
                trail_alpha = 1.0 - (trail_step / 6.0)
                trail_size = max(1, int(p_size * trail_alpha))
                cv2.circle(overlay_particles, (tpx, tpy), trail_size, col, -1)

        cv2.GaussianBlur(overlay_particles, (5, 5), 0, dst=overlay_particles)
        frame = cv2.add(frame, overlay_particles)

        # 4. Badge Shimmer Gleam
        shimmer_x = int(-200 + (w + 400) * progress)
        for badge in BADGES:
            bx1, by1, bx2, by2 = badge["box"]
            if bx1 - 50 <= shimmer_x <= bx2 + 50:
                badge_crop = frame[by1:by2, bx1:bx2].astype(np.float32)
                # Diagonal light streak
                sh_overlay = np.zeros_like(badge_crop)
                rel_x = shimmer_x - bx1
                pt1 = (rel_x - 30, 0)
                pt2 = (rel_x + 30, by2 - by1)
                cv2.line(sh_overlay, pt1, pt2, (255, 255, 255), 18)
                cv2.GaussianBlur(sh_overlay, (21, 21), 0, dst=sh_overlay)
                frame[by1:by2, bx1:bx2] = np.clip(badge_crop + sh_overlay * 0.5, 0, 255).astype(np.uint8)

        out.write(frame)

        # Sample for GIF (every 2nd frame, resized to 720p for fast web loading)
        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved MP4: {mp4_path}")

    # Save optimized GIF
    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 2: Executive Cybernetic HUD & Telemetry Orbit
# -------------------------------------------------------------
def render_option2(base_img):
    print("Rendering Option 2: Executive Cybernetic HUD & Telemetry Orbit...")
    h, w = base_img.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_option2_cyber_hud.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_option2_cyber_hud.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_img.copy()
        hud_overlay = np.zeros_like(frame)

        # 1. Outer Segmented Rotating Ring (Radius 240)
        angle_deg = (progress * 360) % 360
        cv2.ellipse(hud_overlay, (CX, CY), (240, 240), angle_deg, 0, 45, (255, 200, 0), 2)
        cv2.ellipse(hud_overlay, (CX, CY), (240, 240), angle_deg + 90, 0, 45, (255, 200, 0), 2)
        cv2.ellipse(hud_overlay, (CX, CY), (240, 240), angle_deg + 180, 0, 45, (255, 200, 0), 2)
        cv2.ellipse(hud_overlay, (CX, CY), (240, 240), angle_deg + 270, 0, 45, (255, 200, 0), 2)

        # 2. Inner Reverse-Rotating Precision Ticks Ring (Radius 180)
        rev_angle = -angle_deg * 1.5
        cv2.ellipse(hud_overlay, (CX, CY), (180, 180), rev_angle, 0, 70, (0, 220, 255), 1)
        cv2.ellipse(hud_overlay, (CX, CY), (180, 180), rev_angle + 120, 0, 70, (0, 220, 255), 1)
        cv2.ellipse(hud_overlay, (CX, CY), (180, 180), rev_angle + 240, 0, 70, (0, 220, 255), 1)

        # Ticks along the ring
        for tick_i in range(24):
            tick_rad = math.radians(rev_angle + tick_i * 15)
            tx1 = int(CX + 175 * math.cos(tick_rad))
            ty1 = int(CY + 175 * math.sin(tick_rad))
            tx2 = int(CX + 185 * math.cos(tick_rad))
            ty2 = int(CY + 185 * math.sin(tick_rad))
            cv2.line(hud_overlay, (tx1, ty1), (tx2, ty2), (0, 240, 255), 1)

        # 3. Rotating Radar Scanline with fading wedge
        radar_rad = math.radians(angle_deg * 2)
        rx = int(CX + 350 * math.cos(radar_rad))
        ry = int(CY + 350 * math.sin(radar_rad))
        cv2.line(hud_overlay, (CX, CY), (rx, ry), (255, 255, 255), 2)
        # Radar scan trail
        for trail_step in range(1, 16):
            tr_rad = radar_rad - math.radians(trail_step * 2.5)
            trx = int(CX + 350 * math.cos(tr_rad))
            try_ = int(CY + 350 * math.sin(tr_rad))
            alpha_trail = int(180 * (1.0 - trail_step / 16.0))
            cv2.line(hud_overlay, (CX, CY), (trx, try_), (255, 180, 40), 1)

        # 4. Tactical Locking Brackets on the 3 Badges + Telemetry Lines
        for b_i, badge in enumerate(BADGES):
            bx1, by1, bx2, by2 = badge["box"]
            bcx, bcy = badge["pos"]

            # Connection line to center core
            cv2.line(hud_overlay, (CX, CY), (bcx, bcy), (50, 160, 255), 1, cv2.LINE_AA)
            # Pulse dot traveling along connector
            dot_progress = (progress * 2 + b_i / 3.0) % 1.0
            dx = int(CX + (bcx - CX) * dot_progress)
            dy = int(CY + (bcy - CY) * dot_progress)
            cv2.circle(hud_overlay, (dx, dy), 4, (0, 255, 255), -1)

            # Brackets: 4 corners
            pad = 8
            k_len = 22
            col_b = (0, 230, 255)
            # Top-left
            cv2.line(hud_overlay, (bx1 - pad, by1 - pad), (bx1 - pad + k_len, by1 - pad), col_b, 2)
            cv2.line(hud_overlay, (bx1 - pad, by1 - pad), (bx1 - pad, by1 - pad + k_len), col_b, 2)
            # Top-right
            cv2.line(hud_overlay, (bx2 + pad, by1 - pad), (bx2 + pad - k_len, by1 - pad), col_b, 2)
            cv2.line(hud_overlay, (bx2 + pad, by1 - pad), (bx2 + pad, by1 - pad + k_len), col_b, 2)
            # Bottom-left
            cv2.line(hud_overlay, (bx1 - pad, by2 + pad), (bx1 - pad + k_len, by2 + pad), col_b, 2)
            cv2.line(hud_overlay, (bx1 - pad, by2 + pad), (bx1 - pad, by2 + pad - k_len), col_b, 2)
            # Bottom-right
            cv2.line(hud_overlay, (bx2 + pad, by2 + pad), (bx2 + pad - k_len, by2 + pad), col_b, 2)
            cv2.line(hud_overlay, (bx2 + pad, by2 + pad), (bx2 + pad, by2 + pad - k_len), col_b, 2)

            # Telemetry text tags
            tag = f"LOCK:{99.2 + 0.5*math.sin(t*3 + b_i):.1f}%"
            cv2.putText(hud_overlay, tag, (bx1, by2 + pad + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 240, 255), 1, cv2.LINE_AA)

        # 5. Core Hexagon Targeting Matrix
        hex_pts = []
        for h_i in range(6):
            h_rad = math.radians(angle_deg * 0.8 + h_i * 60)
            hx = int(CX + 85 * math.cos(h_rad))
            hy = int(CY + 85 * math.sin(h_rad))
            hex_pts.append((hx, hy))
        for h_i in range(6):
            cv2.line(hud_overlay, hex_pts[h_i], hex_pts[(h_i + 1) % 6], (255, 255, 255), 1)

        # Blend HUD overlay onto frame
        frame = cv2.add(frame, hud_overlay)
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

# -------------------------------------------------------------
# OPTION 3: Cinematic Spotlight & Metallic Gleam
# -------------------------------------------------------------
def render_option3(base_img):
    print("Rendering Option 3: Cinematic Spotlight & Metallic Gleam...")
    h, w = base_img.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_option3_cinematic_spotlight.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_option3_cinematic_spotlight.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    # Embers
    num_embers = 45
    np.random.seed(42)
    ember_x = np.random.uniform(200, w - 200, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(30, 90, num_embers)
    ember_sizes = np.random.randint(2, 5, num_embers)

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_img.copy()

        # 1. Sweeping Cinematic Spotlight (horizontal smooth harmonic sweep)
        # Spot sweeps across x from 300 to 1070
        spot_x = int(CX + 420 * math.sin(t))
        spot_y = int(CY + 60 * math.cos(t))

        # Create soft theatrical light beam
        beam_overlay = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam_overlay, (spot_x, spot_y), 240, (255, 230, 180), -1)
        # Anamorphic horizontal streak
        cv2.ellipse(beam_overlay, (spot_x, spot_y), (480, 50), 0, 0, 360, (255, 200, 120), -1)
        cv2.GaussianBlur(beam_overlay, (151, 151), 0, dst=beam_overlay)
        frame = np.clip(frame.astype(np.float32) + beam_overlay * 0.45, 0, 255).astype(np.uint8)

        # 2. Specular Starburst Gleams when spot passes key metallic crests
        gleam_points = [
            (390, 382),  # Left loop crest
            (CX, CY),    # Center crossover
            (980, 382)   # Right loop crest
        ]
        gleam_overlay = np.zeros_like(frame)
        for gx, gy in gleam_points:
            dist = abs(spot_x - gx)
            if dist < 120:
                intensity = (1.0 - dist / 120.0) ** 2
                g_rad = int(35 * intensity)
                # 4-point star flare
                cv2.line(gleam_overlay, (gx - g_rad * 3, gy), (gx + g_rad * 3, gy), (255, 255, 255), 2)
                cv2.line(gleam_overlay, (gx, gy - g_rad * 2), (gx, gy + g_rad * 2), (255, 255, 255), 2)
                cv2.circle(gleam_overlay, (gx, gy), g_rad, (255, 230, 180), -1)

        if np.any(gleam_overlay > 0):
            cv2.GaussianBlur(gleam_overlay, (15, 15), 0, dst=gleam_overlay)
            frame = cv2.add(frame, gleam_overlay)

        # 3. Floating Golden & Ruby Embers (Drifting upwards)
        ember_overlay = np.zeros_like(frame)
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 25 * math.sin(progress * 4 * math.pi + e_i))
            col = (255, 180, 50) if e_i % 2 == 0 else (120, 50, 255)
            cv2.circle(ember_overlay, (cur_ex, int(cur_ey)), ember_sizes[e_i], col, -1)

        cv2.GaussianBlur(ember_overlay, (7, 7), 0, dst=ember_overlay)
        frame = cv2.add(frame, ember_overlay)

        # 4. Cinematic Vignette (Subtle edge shading)
        vig_overlay = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(vig_overlay, (CX, CY), int(w * 0.65), (255, 255, 255), -1)
        cv2.GaussianBlur(vig_overlay, (151, 151), 0, dst=vig_overlay)
        vig_factor = vig_overlay / 255.0
        # Darken outside vignette slightly (soft corporate cinematic)
        frame = (frame.astype(np.float32) * (0.85 + 0.15 * vig_factor)).astype(np.uint8)

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
    if not os.path.exists(BASE_IMG_PATH):
        raise FileNotFoundError(f"Missing {BASE_IMG_PATH}")
    img = cv2.imread(BASE_IMG_PATH)
    render_option1(img)
    render_option2(img)
    render_option3(img)
    print("All 3 Motion Graphic options rendered successfully!")
