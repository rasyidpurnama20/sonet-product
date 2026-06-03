#!/usr/bin/env python3
"""
Generator untuk frame OBS ICICOS 2026
Membuat placeholder visual untuk setiap scene yang dibutuhkan
IMPROVED VERSION - Text lebih besar dan lebih jelas!
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Resolusi standar untuk Zoom/OBS (16:9)
WIDTH = 1920
HEIGHT = 1080

# Color scheme ICICOS - More vibrant
COLOR_PRIMARY = "#0c4a6e"  # Deep Blue
COLOR_SECONDARY = "#0ea5e9"  # Sky Blue
COLOR_ACCENT = "#f97316"  # Vibrant Orange
COLOR_BG = "#ffffff"  # Pure white
COLOR_TEXT = "#0f172a"  # Very dark
COLOR_DARK = "#1e293b"

def create_frame(title, subtitle="", frame_type="default", filename="frame.png"):
    """Create a visual placeholder for OBS scene with BIG, CLEAR text"""
    
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), COLOR_BG)
    draw = ImageDraw.Draw(img)
    
    # Load fonts - MUCH BIGGER!
    try:
        logo_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)  # Huge!
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)  # Very big
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)  # Big
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 56)  # Medium
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)  # For labels
    except:
        logo_font = title_font = subtitle_font = small_font = label_font = ImageFont.load_default()
    
    # Background based on type
    if "video" in frame_type.lower():
        # Video frames - gradient-like effect with darker background
        draw.rectangle([0, 0, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
        
        # Add decorative elements
        draw.rectangle([0, HEIGHT//2-100, WIDTH, HEIGHT//2+100], fill=COLOR_SECONDARY)
        
        # Big centered text
        draw.text((WIDTH//2, HEIGHT//2-150), title, fill="white", font=title_font, anchor="mm", stroke_width=3, stroke_fill=COLOR_PRIMARY)
        if subtitle:
            draw.text((WIDTH//2, HEIGHT//2+50), subtitle, fill=COLOR_ACCENT, font=subtitle_font, anchor="mm", stroke_width=2, stroke_fill=COLOR_PRIMARY)
        
    elif "camera" in frame_type.lower():
        # Camera frames - split screen with labels
        draw.rectangle([0, 0, WIDTH//2-10, HEIGHT], fill="#1e293b")
        draw.rectangle([WIDTH//2+10, 0, WIDTH, HEIGHT], fill="#334155")
        
        # Vertical divider
        draw.rectangle([WIDTH//2-10, 0, WIDTH//2+10, HEIGHT], fill=COLOR_ACCENT)
        
        # Big labels for camera areas
        draw.text((WIDTH//4, HEIGHT//2), "CAMERA 1", fill="white", font=label_font, anchor="mm", stroke_width=3, stroke_fill="black")
        draw.text((WIDTH*3//4, HEIGHT//2), "CAMERA 2", fill="white", font=label_font, anchor="mm", stroke_width=3, stroke_fill="black")
        
        # Title at top
        draw.rectangle([0, 0, WIDTH, 200], fill=COLOR_PRIMARY)
        draw.text((WIDTH//2, 100), title, fill="white", font=subtitle_font, anchor="mm", stroke_width=2, stroke_fill="black")
        
    elif "presentasi" in frame_type.lower():
        # Presentation + Camera - clear separation
        # Main presentation area (left 75%)
        draw.rectangle([0, 0, WIDTH*3//4-20, HEIGHT], fill="#0f172a")
        
        # Camera area (right 25%)
        draw.rectangle([WIDTH*3//4+20, 0, WIDTH, HEIGHT], fill="#334155")
        
        # Orange divider
        draw.rectangle([WIDTH*3//4-20, 0, WIDTH*3//4+20, HEIGHT], fill=COLOR_ACCENT)
        
        # HUGE labels
        draw.text((WIDTH*3//8, HEIGHT//2), "PRESENTATION\nSLIDES", fill="white", font=label_font, anchor="mm", align="center", stroke_width=3, stroke_fill="black")
        draw.text((WIDTH*7//8, HEIGHT//2), "CAM", fill="white", font=label_font, anchor="mm", stroke_width=3, stroke_fill="black")
        
        # Title bar
        draw.rectangle([0, 0, WIDTH, 200], fill=COLOR_PRIMARY)
        draw.text((WIDTH//2, 100), title, fill="white", font=subtitle_font, anchor="mm", stroke_width=2, stroke_fill="black")
        
    else:
        # Speaker frames - clean and professional
        # Background gradient effect
        draw.rectangle([0, 0, WIDTH, HEIGHT], fill="#f1f5f9")
        draw.rectangle([WIDTH//4, HEIGHT//4, WIDTH*3//4, HEIGHT*3//4], fill="white")
        
        # Large speaker area with border
        speaker_radius = 320
        if "frame" in frame_type.lower() and frame_type.lower() != "frame kosong":
            # Outer glow
            for i in range(5, 0, -1):
                draw.ellipse([WIDTH//2-speaker_radius-i*10, HEIGHT//2-speaker_radius-i*10, 
                            WIDTH//2+speaker_radius+i*10, HEIGHT//2+speaker_radius+i*10], 
                           outline=COLOR_SECONDARY, width=8)
            
            # Main circle
            draw.ellipse([WIDTH//2-speaker_radius, HEIGHT//2-speaker_radius, 
                        WIDTH//2+speaker_radius, HEIGHT//2+speaker_radius], 
                       outline=COLOR_ACCENT, width=20)
            
            # Center icon (bigger)
            draw.text((WIDTH//2, HEIGHT//2), "👤", font=logo_font, anchor="mm")
        
        # Title below speaker area
        if title and "kosong" not in title.lower():
            # Background for text
            text_y = HEIGHT//2 + speaker_radius + 120
            draw.rectangle([WIDTH//4, text_y-80, WIDTH*3//4, text_y+80], fill=COLOR_PRIMARY)
            draw.text((WIDTH//2, text_y), title, fill="white", font=title_font, anchor="mm", stroke_width=2, stroke_fill="black")
    
    # Header bar with logo
    draw.rectangle([0, 0, WIDTH, 220], fill=COLOR_PRIMARY)
    
    # ICICOS 2026 - HUGE!
    draw.text((WIDTH//2, 110), "ICICOS 2026", fill=COLOR_ACCENT, font=logo_font, anchor="mm", stroke_width=4, stroke_fill="black")
    
    # Footer bar
    draw.rectangle([0, HEIGHT-180, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
    draw.text((WIDTH//2, HEIGHT-90), "International Conference on Informatics and Computing Systems", 
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
