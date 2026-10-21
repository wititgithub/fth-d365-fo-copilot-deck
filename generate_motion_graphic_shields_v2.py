"""
generate_motion_graphic_shields_v2.py
Renders 3 distinct high-impact Motion Graphic video and GIF loops:
Option 1: Harmonic 3D Hover & Glass Glint
Option 2: Quantum Pulse & Dual Energy Tethers
Option 3: Cinematic Spotlight Lock & Gyroscopic Focus
"""

import os
import math
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_IMG_PATH = "assets/base_inpainted_shields.jpg"
SHIELD_D365_PATH = "assets/shield_d365_v2.png"
SHIELD_COPILOT_PATH = "assets/shield_copilot_v2.png"
OUTPUT_DIR = "assets"
FPS = 30
DURATION_SEC = 3.6  # 108 frames for smooth looping
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Base dimensions
CX, CY = 685, 382
D365_BASE_X, D365_BASE_Y = 55, 35
COPILOT_BASE_X, COPILOT_BASE_Y = 1035, 35

def overlay_rgba(base_bgr, overlay_rgba, x, y, scale=1.0, alpha_mult=1.0):
    """Overlays an RGBA image onto a BGR base image at (x, y) with optional scaling."""
    oh, ow = overlay_rgba.shape[:2]
    if scale != 1.0:
        new_w = max(1, int(ow * scale))
        new_h = max(1, int(oh * scale))
        ov = cv2.resize(overlay_rgba, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
        # Adjust position to keep center aligned
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
# OPTION 1: Harmonic 3D Hover & Glass Glint
# -------------------------------------------------------------
def render_option1(base_bgr, s_d365, s_copilot):
    print("Rendering Shields Motion Option 1: Harmonic 3D Hover & Glass Glint...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_shields_option1_harmonic_float.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_shields_option1_harmonic_float.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    # Embers
    num_embers = 45
    np.random.seed(42)
    ember_x = np.random.uniform(150, w - 150, num_embers)
    ember_y_base = np.random.uniform(0, h, num_embers)
    ember_speeds = np.random.uniform(30, 85, num_embers)
    ember_sizes = np.random.randint(2, 5, num_embers)

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # 1. Harmonic Float of Shields (Out-of-phase balance)
        d365_dy = int(18 * math.sin(t))
        d365_dx = int(5 * math.cos(t))
        copilot_dy = int(18 * math.sin(t + math.pi))
        copilot_dx = int(-5 * math.cos(t))

        # 2. Sweeping Spotlight
        spot_x = int(CX + 440 * math.sin(t))
        spot_y = int(CY + 50 * math.cos(t))

        # Soft theatrical spotlight
        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 260, (255, 235, 190), -1)
        cv2.ellipse(beam, (spot_x, spot_y), (480, 55), 0, 0, 360, (255, 200, 130), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.42, 0, 255).astype(np.uint8)

        # 3. Dynamic Contact Shadows on floor/ribbon (scales with height)
        # Overlay D365 Shield
        d365_scale = 1.0 + 0.02 * math.sin(t)
        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y + d365_dy, scale=d365_scale)

        # Overlay Copilot Shield
        copilot_scale = 1.0 + 0.02 * math.sin(t + math.pi)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y + copilot_dy, scale=copilot_scale)

        # 4. Specular Starburst Gleams on Shields when spotlight approaches
        gleam_overlay = np.zeros_like(frame)
        targets = [
            (D365_BASE_X + 145 + d365_dx, D365_BASE_Y + 140 + d365_dy, (0, 220, 255)),
            (390, CY, (255, 255, 255)),
            (CX, CY, (255, 220, 180)),
            (980, CY, (255, 255, 255)),
            (COPILOT_BASE_X + 145 + copilot_dx, COPILOT_BASE_Y + 140 + copilot_dy, (255, 100, 220))
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

        # 5. Embers
        ember_overlay = np.zeros_like(frame)
        for e_i in range(num_embers):
            cur_ey = (ember_y_base[e_i] - ember_speeds[e_i] * (progress * DURATION_SEC)) % h
            cur_ex = int(ember_x[e_i] + 25 * math.sin(progress * 4 * math.pi + e_i))
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
    print(f"Saved Option 1 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Option 1 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 2: Quantum Pulse & Dual Energy Tethers
# -------------------------------------------------------------
def render_option2(base_bgr, s_d365, s_copilot):
    print("Rendering Shields Motion Option 2: Quantum Pulse & Dual Energy Tethers...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_shields_option2_quantum_tether.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_shields_option2_quantum_tether.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Center pulse
        core_pulse = 0.5 + 0.5 * math.sin(t * 3)
        core_r = int(130 + 35 * core_pulse)

        # 1. Concentric Energy Shockwaves from Center
        shock_overlay = np.zeros_like(frame)
        for ring_i in range(3):
            r_prog = (progress * 1.5 + ring_i / 3.0) % 1.0
            r_radius = int(50 + r_prog * 450)
            r_alpha = int(180 * (1.0 - r_prog) ** 1.5)
            col_ring = (255, 180, 50) if ring_i % 2 == 0 else (0, 220, 255)
            cv2.circle(shock_overlay, (CX, CY), r_radius, col_ring, 2)
        cv2.GaussianBlur(shock_overlay, (9, 9), 0, dst=shock_overlay)
        frame = cv2.add(frame, shock_overlay)

        # 2. Orbital Sway for Shields
        d365_dx = int(12 * math.cos(t * 1.5))
        d365_dy = int(14 * math.sin(t * 1.5))
        copilot_dx = int(-12 * math.cos(t * 1.5))
        copilot_dy = int(-14 * math.sin(t * 1.5))

        d365_cx = D365_BASE_X + 145 + d365_dx
        d365_cy = D365_BASE_Y + 140 + d365_dy
        copilot_cx = COPILOT_BASE_X + 145 + copilot_dx
        copilot_cy = COPILOT_BASE_Y + 140 + copilot_dy

        # 3. Dynamic Energy Tethers (Curved lightning / plasma beams)
        tether_overlay = np.zeros_like(frame)

        # D365 Tether (Azure / Cyan)
        steps = 40
        for s in range(steps):
            frac = s / float(steps)
            # Quadratic bezier arc bowing upward
            mid_y_bow = -45 * math.sin(frac * math.pi)
            bx = int(CX + (d365_cx - CX) * frac)
            by = int(CY + (d365_cy - CY) * frac + mid_y_bow)
            cv2.circle(tether_overlay, (bx, by), 3, (255, 230, 0), -1)

        # Copilot Tether (Violet / Magenta)
        for s in range(steps):
            frac = s / float(steps)
            mid_y_bow = -45 * math.sin(frac * math.pi)
            bx = int(CX + (copilot_cx - CX) * frac)
            by = int(CY + (copilot_cy - CY) * frac + mid_y_bow)
            cv2.circle(tether_overlay, (bx, by), 3, (255, 50, 180), -1)

        # Flowing Data Photons traveling along tethers
        num_photons = 6
        for p_i in range(num_photons):
            p_prog = (progress * 3.0 + p_i / float(num_photons)) % 1.0
            mid_bow = -45 * math.sin(p_prog * math.pi)
            # D365 photon
            px1 = int(CX + (d365_cx - CX) * p_prog)
            py1 = int(CY + (d365_cy - CY) * p_prog + mid_bow)
            cv2.circle(tether_overlay, (px1, py1), 7, (255, 255, 255), -1)
            cv2.circle(tether_overlay, (px1, py1), 14, (255, 200, 0), 2)

            # Copilot photon
            px2 = int(CX + (copilot_cx - CX) * p_prog)
            py2 = int(CY + (copilot_cy - CY) * p_prog + mid_bow)
            cv2.circle(tether_overlay, (px2, py2), 7, (255, 255, 255), -1)
            cv2.circle(tether_overlay, (px2, py2), 14, (255, 80, 220), 2)

        cv2.GaussianBlur(tether_overlay, (11, 11), 0, dst=tether_overlay)
        frame = cv2.add(frame, tether_overlay)

        # 4. Breathing Scale & Resonance Pulse on Shields
        d365_pulse = 1.0 + 0.05 * math.sin(t * 3)
        copilot_pulse = 1.0 + 0.05 * math.sin(t * 3 + math.pi)

        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y + d365_dy, scale=d365_pulse)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y + copilot_dy, scale=copilot_pulse)

        # 5. Rotating HUD Aura Rings around shields
        hud_rot = progress * 360
        aura_overlay = np.zeros_like(frame)
        cv2.ellipse(aura_overlay, (d365_cx, d365_cy), (115, 115), hud_rot, 0, 80, (255, 200, 0), 2)
        cv2.ellipse(aura_overlay, (d365_cx, d365_cy), (115, 115), hud_rot + 180, 0, 80, (255, 200, 0), 2)

        cv2.ellipse(aura_overlay, (copilot_cx, copilot_cy), (115, 115), -hud_rot, 0, 80, (255, 80, 220), 2)
        cv2.ellipse(aura_overlay, (copilot_cx, copilot_cy), (115, 115), -hud_rot + 180, 0, 80, (255, 80, 220), 2)

        # Telemetry Text
        d_tag = f"D365 SYNC: {99.1 + 0.6 * math.sin(t*4):.1f}%"
        cv2.putText(aura_overlay, d_tag, (d365_cx - 65, d365_cy + 130), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 200, 0), 1, cv2.LINE_AA)

        c_tag = f"COPILOT AI: {99.5 + 0.4 * math.cos(t*4):.1f}%"
        cv2.putText(aura_overlay, c_tag, (copilot_cx - 65, copilot_cy + 130), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 80, 220), 1, cv2.LINE_AA)

        frame = cv2.add(frame, aura_overlay)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved Option 2 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Option 2 GIF: {gif_path}")

# -------------------------------------------------------------
# OPTION 3: Cinematic Spotlight Lock & Gyroscopic Focus
# -------------------------------------------------------------
def render_option3(base_bgr, s_d365, s_copilot):
    print("Rendering Shields Motion Option 3: Cinematic Spotlight Lock & Gyroscopic Focus...")
    h, w = base_bgr.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mp4_path = os.path.join(OUTPUT_DIR, "motion_shields_option3_spotlight_lock.mp4")
    gif_path = os.path.join(OUTPUT_DIR, "motion_shields_option3_spotlight_lock.gif")
    out = cv2.VideoWriter(mp4_path, fourcc, float(FPS), (w, h))

    gif_frames = []

    for frame_idx in range(TOTAL_FRAMES):
        progress = frame_idx / TOTAL_FRAMES
        t = progress * 2 * math.pi
        frame = base_bgr.copy()

        # Gyroscopic dual-axis hover
        d365_dy = int(14 * math.sin(t * 1.2))
        d365_dx = int(6 * math.cos(t * 0.8))
        copilot_dy = int(14 * math.sin(t * 1.2 + math.pi))
        copilot_dx = int(-6 * math.cos(t * 0.8))

        d365_cx = D365_BASE_X + 145 + d365_dx
        d365_cy = D365_BASE_Y + 140 + d365_dy
        copilot_cx = COPILOT_BASE_X + 145 + copilot_dx
        copilot_cy = COPILOT_BASE_Y + 140 + copilot_dy

        # 1. 3-Phase Spotlight Journey:
        # Phase 1: Focus on D365 (prog 0.0 -> 0.4)
        # Phase 2: Sweep through Nexus (prog 0.4 -> 0.6)
        # Phase 3: Focus on Copilot (prog 0.6 -> 1.0)
        spot_x = int(CX + 520 * math.sin(t))
        spot_y = int(CY - 100 * math.cos(t))

        # Theatrical Keynote Spotlight Beam
        beam = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(beam, (spot_x, spot_y), 270, (255, 230, 180), -1)
        # Anamorphic horizontal flare
        cv2.ellipse(beam, (spot_x, spot_y), (520, 48), 0, 0, 360, (255, 210, 140), -1)
        cv2.GaussianBlur(beam, (151, 151), 0, dst=beam)
        frame = np.clip(frame.astype(np.float32) + beam * 0.46, 0, 255).astype(np.uint8)

        # 2. Spotlight Proximity Boost on Shields
        dist_d365 = abs(spot_x - d365_cx)
        dist_copilot = abs(spot_x - copilot_cx)

        d365_boost = max(0.0, 1.0 - dist_d365 / 220.0)
        copilot_boost = max(0.0, 1.0 - dist_copilot / 220.0)

        # Draw Shields with scale pop when spotlight is over them
        s1_scale = 1.0 + 0.07 * d365_boost
        s2_scale = 1.0 + 0.07 * copilot_boost

        overlay_rgba(frame, s_d365, D365_BASE_X + d365_dx, D365_BASE_Y + d365_dy, scale=s1_scale)
        overlay_rgba(frame, s_copilot, COPILOT_BASE_X + copilot_dx, COPILOT_BASE_Y + copilot_dy, scale=s2_scale)

        # 3. Anamorphic Lens Flare & Target Lock when Spotlight hits Shield
        fx_overlay = np.zeros_like(frame)

        # D365 Lock Flare
        if d365_boost > 0.3:
            intensity = (d365_boost - 0.3) / 0.7
            # Horizontal azure laser flare
            flare_len = int(350 * intensity)
            cv2.line(fx_overlay, (d365_cx - flare_len, d365_cy), (d365_cx + flare_len, d365_cy), (255, 220, 0), 2)
            cv2.circle(fx_overlay, (d365_cx, d365_cy), int(40 * intensity), (255, 255, 255), -1)

            # Target Lock Reticle
            k_len = 24
            col_k = (255, 220, 0)
            box_r = 100
            cv2.line(fx_overlay, (d365_cx - box_r, d365_cy - box_r), (d365_cx - box_r + k_len, d365_cy - box_r), col_k, 2)
            cv2.line(fx_overlay, (d365_cx - box_r, d365_cy - box_r), (d365_cx - box_r, d365_cy - box_r + k_len), col_k, 2)
            cv2.line(fx_overlay, (d365_cx + box_r, d365_cy - box_r), (d365_cx + box_r - k_len, d365_cy - box_r), col_k, 2)
            cv2.line(fx_overlay, (d365_cx + box_r, d365_cy - box_r), (d365_cx + box_r, d365_cy - box_r + k_len), col_k, 2)
            cv2.line(fx_overlay, (d365_cx - box_r, d365_cy + box_r), (d365_cx - box_r + k_len, d365_cy + box_r), col_k, 2)
            cv2.line(fx_overlay, (d365_cx - box_r, d365_cy + box_r), (d365_cx - box_r, d365_cy + box_r - k_len), col_k, 2)
            cv2.line(fx_overlay, (d365_cx + box_r, d365_cy + box_r), (d365_cx + box_r - k_len, d365_cy + box_r), col_k, 2)
            cv2.line(fx_overlay, (d365_cx + box_r, d365_cy + box_r), (d365_cx + box_r, d365_cy + box_r - k_len), col_k, 2)

            cv2.putText(fx_overlay, "TARGET: DYNAMICS 365 [LOCKED]", (d365_cx - 95, d365_cy + box_r + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.42, col_k, 1, cv2.LINE_AA)

        # Copilot Lock Flare
        if copilot_boost > 0.3:
            intensity = (copilot_boost - 0.3) / 0.7
            flare_len = int(350 * intensity)
            cv2.line(fx_overlay, (copilot_cx - flare_len, copilot_cy), (copilot_cx + flare_len, copilot_cy), (255, 60, 220), 2)
            cv2.circle(fx_overlay, (copilot_cx, copilot_cy), int(40 * intensity), (255, 255, 255), -1)

            # Target Lock Reticle
            k_len = 24
            col_k = (255, 60, 220)
            box_r = 100
            cv2.line(fx_overlay, (copilot_cx - box_r, copilot_cy - box_r), (copilot_cx - box_r + k_len, copilot_cy - box_r), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx - box_r, copilot_cy - box_r), (copilot_cx - box_r, copilot_cy - box_r + k_len), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx + box_r, copilot_cy - box_r), (copilot_cx + box_r - k_len, copilot_cy - box_r), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx + box_r, copilot_cy - box_r), (copilot_cx + box_r, copilot_cy - box_r + k_len), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx - box_r, copilot_cy + box_r), (copilot_cx - box_r + k_len, copilot_cy + box_r), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx - box_r, copilot_cy + box_r), (copilot_cx - box_r, copilot_cy + box_r - k_len), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx + box_r, copilot_cy + box_r), (copilot_cx + box_r - k_len, copilot_cy + box_r), col_k, 2)
            cv2.line(fx_overlay, (copilot_cx + box_r, copilot_cy + box_r), (copilot_cx + box_r, copilot_cy + box_r - k_len), col_k, 2)

            cv2.putText(fx_overlay, "TARGET: COPILOT AI [LOCKED]", (copilot_cx - 90, copilot_cy + box_r + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.42, col_k, 1, cv2.LINE_AA)

        if np.any(fx_overlay > 0):
            cv2.GaussianBlur(fx_overlay, (15, 15), 0, dst=fx_overlay)
            frame = cv2.add(frame, fx_overlay)

        # 4. Cinematic Vignette
        vig = np.zeros_like(frame, dtype=np.float32)
        cv2.circle(vig, (CX, CY), int(w * 0.65), (255, 255, 255), -1)
        cv2.GaussianBlur(vig, (151, 151), 0, dst=vig)
        frame = (frame.astype(np.float32) * (0.84 + 0.16 * (vig / 255.0))).astype(np.uint8)

        out.write(frame)

        if frame_idx % 2 == 0:
            small_frame = cv2.resize(frame, (800, int(800 * h / w)), interpolation=cv2.INTER_AREA)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_frame))

    out.release()
    print(f"Saved Option 3 MP4: {mp4_path}")

    gif_frames[0].save(
        gif_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True
    )
    print(f"Saved Option 3 GIF: {gif_path}")

if __name__ == "__main__":
    if not os.path.exists(BASE_IMG_PATH):
        raise FileNotFoundError(f"Missing {BASE_IMG_PATH}")
    base = cv2.imread(BASE_IMG_PATH)
    s_d365 = cv2.imread(SHIELD_D365_PATH, cv2.IMREAD_UNCHANGED)
    s_copilot = cv2.imread(SHIELD_COPILOT_PATH, cv2.IMREAD_UNCHANGED)

    render_option1(base, s_d365, s_copilot)
    render_option2(base, s_d365, s_copilot)
    render_option3(base, s_d365, s_copilot)
    print("All 3 Shields Motion Graphic options rendered successfully!")
