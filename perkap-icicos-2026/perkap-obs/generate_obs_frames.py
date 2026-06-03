#!/usr/bin/env python3
"""
Generator untuk frame OBS ICICOS 2026
Membuat placeholder visual untuk setiap scene yang dibutuhkan
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Resolusi standar untuk Zoom/OBS (16:9)
WIDTH = 1920
HEIGHT = 1080

# Color scheme ICICOS
COLOR_PRIMARY = "#1e3a8a"  # Blue
COLOR_SECONDARY = "#3b82f6"  # Light Blue
COLOR_ACCENT = "#f59e0b"  # Orange
COLOR_BG = "#f8fafc"  # Light gray
COLOR_TEXT = "#1e293b"  # Dark gray

def create_frame(title, subtitle="", frame_type="default", filename="frame.png"):
    """Create a visual placeholder for OBS scene"""
    
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), COLOR_BG)
    draw = ImageDraw.Draw(img)
    
    # Try to use a better font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Background based on type
    if "video" in frame_type.lower():
        # Video frames - darker background
        draw.rectangle([0, 0, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
        text_color = "white"
    elif "camera" in frame_type.lower():
        # Camera frames - split screen layout
        draw.rectangle([0, 0, WIDTH//2, HEIGHT], fill=COLOR_SECONDARY)
        draw.rectangle([WIDTH//2, 0, WIDTH, HEIGHT], fill="#0f172a")
        text_color = "white"
    elif "presentasi" in frame_type.lower():
        # Presentation + Camera - main content area
        draw.rectangle([0, 0, WIDTH*3//4, HEIGHT], fill="#0f172a")
        draw.rectangle([WIDTH*3//4, 0, WIDTH, HEIGHT], fill=COLOR_SECONDARY)
        # Label areas
        draw.text((WIDTH*3//8, HEIGHT//2-100), "PRESENTATION", fill="white", font=subtitle_font, anchor="mm")
        draw.text((WIDTH*7//8, HEIGHT//2), "CAMERA", fill="white", font=subtitle_font, anchor="mm")
        text_color = "white"
    else:
        # Default frames - speaker frames
        draw.rectangle([0, 0, WIDTH, 200], fill=COLOR_PRIMARY)
        draw.rectangle([0, HEIGHT-150, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
        text_color = COLOR_TEXT
        
        # Speaker area indicator
        if "frame" in frame_type.lower() and frame_type.lower() != "frame kosong":
            draw.ellipse([WIDTH//2-250, HEIGHT//2-250, WIDTH//2+250, HEIGHT//2+250], 
                        outline=COLOR_ACCENT, width=8)
            draw.text((WIDTH//2, HEIGHT//2), "👤", font=title_font, anchor="mm")
    
    # Header bar
    draw.rectangle([0, 0, WIDTH, 180], fill=COLOR_PRIMARY)
    
    # ICICOS 2026 logo text
    draw.text((WIDTH//2, 90), "ICICOS 2026", fill=COLOR_ACCENT, font=title_font, anchor="mm")
    
    # Title
    title_y = HEIGHT//2 if "video" in frame_type.lower() else 350
    if "presentasi" not in frame_type.lower():
        draw.text((WIDTH//2, title_y), title, fill="white" if "video" in frame_type.lower() or "camera" in frame_type.lower() else COLOR_TEXT, 
                 font=subtitle_font, anchor="mm")
    
    # Subtitle
    if subtitle:
        draw.text((WIDTH//2, title_y + 80), subtitle, fill="white" if "video" in frame_type.lower() else COLOR_SECONDARY, 
                 font=small_font, anchor="mm")
    
    # Footer
    draw.rectangle([0, HEIGHT-120, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
    draw.text((WIDTH//2, HEIGHT-60), "International Conference on Informatics and Computing Systems", 
             fill="white", font=small_font, anchor="mm")
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), filename)
    img.save(output_path)
    print(f"✓ Created: {filename}")

def main():
    print("🎬 Generating OBS Frames for ICICOS 2026...\n")
    
    frames = [
        # Day 1 Videos
        ("VIDEO LOOP DAY 1", "Waiting for Conference to Start", "video", "01_video_loop_day1.png"),
        ("VIDEO TRANSISI", "Transition Animation", "video", "02_video_transisi.png"),
        ("VIDEO OPENING DAY 1", "Conference Opening", "video", "03_video_opening_day1.png"),
        
        # Day 1 Frames
        ("FRAME KOSONG", "", "frame", "04_frame_kosong.png"),
        ("MASTER OF CEREMONY", "", "frame_mc", "05_frame_mc.png"),
        ("Pak Indra", "Speaker Session", "frame", "06_frame_pak_indra.png"),
        ("Dr. Kurnianingsih", "Speaker Session", "frame", "07_frame_dr_kurnianingsih.png"),
        ("Pak Kusworo", "Speaker Session", "frame", "08_frame_pak_kusworo.png"),
        ("Pak Rektor", "Keynote Speech", "frame", "09_frame_pak_rektor.png"),
        
        # Plenary 1
        ("PLENARY SESSION 1", "Camera View", "camera_plenary", "10_frame_camera_plenary1.png"),
        ("PLENARY SESSION 1", "", "presentasi_camera", "11_frame_presentasi_camera_plenary1.png"),
        
        # Plenary 2
        ("PLENARY SESSION 2", "Camera View", "camera_plenary", "12_frame_camera_plenary2.png"),
        ("PLENARY SESSION 2", "", "presentasi_camera", "13_frame_presentasi_camera_plenary2.png"),
        
        # Day 1 Recap
        ("VIDEO HALF RECAP", "Midday Summary", "video", "14_video_half_recap.png"),
        ("VIDEO RECAP DAY 1", "Day 1 Highlights", "video", "15_video_recap_day1.png"),
        
        # Day 2 Videos
        ("VIDEO LOOP DAY 2", "Waiting for Day 2", "video", "16_video_loop_day2.png"),
        ("VIDEO OPENING DAY 2", "Day 2 Opening", "video", "17_video_opening_day2.png"),
        
        # Day 2 Frames
        ("Pak Aris Sugi", "Speaker Session", "frame", "18_frame_pak_aris_sugi.png"),
        
        # Plenary 3
        ("PLENARY SESSION 3", "Camera View", "camera_plenary", "19_frame_camera_plenary3.png"),
        ("PLENARY SESSION 3", "", "presentasi_camera", "20_frame_presentasi_camera_plenary3.png"),
    ]
    
    for title, subtitle, frame_type, filename in frames:
        create_frame(title, subtitle, frame_type, filename)
    
    print(f"\n✅ Successfully generated {len(frames)} OBS frames!")
    print(f"📁 Location: {os.path.dirname(os.path.abspath(__file__))}")

if __name__ == "__main__":
    main()
