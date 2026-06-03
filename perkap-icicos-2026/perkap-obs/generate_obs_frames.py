#!/usr/bin/env python3
"""
Generator untuk frame OBS ICICOS 2026
ULTIMATE VERSION V3 - SUPER BESAR, SANGAT JELAS!
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Resolusi standar untuk Zoom/OBS (16:9)
WIDTH = 1920
HEIGHT = 1080

# Color scheme - Maximum contrast
COLOR_PRIMARY = "#1e40af"  # Strong Blue
COLOR_ACCENT = "#ea580c"  # Strong Orange
COLOR_BG_LIGHT = "#f8fafc"
COLOR_BG_DARK = "#0f172a"
COLOR_WHITE = "#ffffff"

def create_frame(title, subtitle="", frame_type="default", filename="frame.png"):
    """Create OBS frame with MASSIVE, ULTRA CLEAR text and labels"""
    
    img = Image.new('RGB', (WIDTH, HEIGHT), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    # SUPER MASSIVE FONTS!
    try:
        mega_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 200)  # MASSIVE!
        huge_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 160)  # HUGE!
        big_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)   # BIG!
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)  # Title
        medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)  # Medium
    except:
        mega_font = huge_font = big_font = title_font = medium_font = ImageFont.load_default()
    
    # === VIDEO FRAMES ===
    if "video" in frame_type.lower():
        # Full background gradient
        draw.rectangle([0, 0, WIDTH, HEIGHT], fill=COLOR_PRIMARY)
        
        # Giant center box
        box_height = 400
        draw.rectangle([100, HEIGHT//2-box_height//2, WIDTH-100, HEIGHT//2+box_height//2], 
                      fill=COLOR_ACCENT, outline=COLOR_WHITE, width=15)
        
        # MASSIVE title
        draw.text((WIDTH//2, HEIGHT//2-100), title, fill=COLOR_WHITE, font=huge_font, 
                 anchor="mm", stroke_width=8, stroke_fill=COLOR_PRIMARY)
        
        # Big subtitle
        if subtitle:
            draw.text((WIDTH//2, HEIGHT//2+100), subtitle, fill=COLOR_WHITE, font=big_font, 
                     anchor="mm", stroke_width=5, stroke_fill=COLOR_PRIMARY)
    
    # === CAMERA PLENARY FRAMES ===
    elif "camera" in frame_type.lower():
        # Split dengan divider super tebal
        draw.rectangle([0, 0, WIDTH//2-30, HEIGHT], fill=COLOR_BG_DARK)
        draw.rectangle([WIDTH//2+30, 0, WIDTH, HEIGHT], fill="#1e293b")
        draw.rectangle([WIDTH//2-30, 0, WIDTH//2+30, HEIGHT], fill=COLOR_ACCENT)
        
        # GIANT labels di tengah
        draw.text((WIDTH//4, HEIGHT//2), "CAMERA\n1", fill=COLOR_WHITE, font=mega_font, 
                 anchor="mm", align="center", stroke_width=8, stroke_fill="black")
        draw.text((WIDTH*3//4, HEIGHT//2), "CAMERA\n2", fill=COLOR_WHITE, font=mega_font, 
                 anchor="mm", align="center", stroke_width=8, stroke_fill="black")
        
        # Title bar SUPER BESAR
        draw.rectangle([0, 0, WIDTH, 280], fill=COLOR_PRIMARY, outline=COLOR_ACCENT, width=10)
        draw.text((WIDTH//2, 140), title, fill=COLOR_ACCENT, font=big_font, 
                 anchor="mm", stroke_width=6, stroke_fill="black")
    
    # === PRESENTATION + CAMERA FRAMES ===
    elif "presentasi" in frame_type.lower():
        # Main presentation (70%)
        draw.rectangle([0, 0, WIDTH*7//10-40, HEIGHT], fill=COLOR_BG_DARK)
        
        # Camera PiP (30%)
        draw.rectangle([WIDTH*7//10+40, 0, WIDTH, HEIGHT], fill="#1e293b")
        
        # SUPER THICK divider
        draw.rectangle([WIDTH*7//10-40, 0, WIDTH*7//10+40, HEIGHT], fill=COLOR_ACCENT)
        
        # GIANT labels
        draw.text((WIDTH*35//100, HEIGHT//2), "PRESENTATION\n\nSLIDES", fill=COLOR_WHITE, 
                 font=mega_font, anchor="mm", align="center", stroke_width=8, stroke_fill="black")
        draw.text((WIDTH*85//100, HEIGHT//2), "CAM", fill=COLOR_ACCENT, font=mega_font, 
                 anchor="mm", stroke_width=8, stroke_fill="black")
        
        # Title bar
        draw.rectangle([0, 0, WIDTH, 280], fill=COLOR_PRIMARY, outline=COLOR_ACCENT, width=10)
        draw.text((WIDTH//2, 140), title, fill=COLOR_ACCENT, font=big_font, 
                 anchor="mm", stroke_width=6, stroke_fill="black")
    
    # === SPEAKER FRAMES ===
    else:
        # Clean background
        draw.rectangle([0, 0, WIDTH, HEIGHT], fill=COLOR_BG_LIGHT)
        
        # Giant colored box for speaker
        margin = 200
        draw.rectangle([margin, 350, WIDTH-margin, HEIGHT-280], 
                      fill=COLOR_WHITE, outline=COLOR_PRIMARY, width=20)
        
        if "frame" in frame_type.lower() and "kosong" not in frame_type.lower():
            # MASSIVE speaker circle
            radius = 400
            center_y = HEIGHT//2 + 50
            
            # Multi-layer glow
            for i in range(8, 0, -1):
                alpha_color = COLOR_ACCENT if i % 2 == 0 else COLOR_PRIMARY
                draw.ellipse([WIDTH//2-radius-i*15, center_y-radius-i*15,
                            WIDTH//2+radius+i*15, center_y+radius+i*15],
                           outline=alpha_color, width=10)
            
            # Main circle - SUPER THICK border
            draw.ellipse([WIDTH//2-radius, center_y-radius, 
                         WIDTH//2+radius, center_y+radius],
                       fill=COLOR_WHITE, outline=COLOR_ACCENT, width=30)
            
            # MASSIVE icon
            draw.text((WIDTH//2, center_y), "👤", font=mega_font, anchor="mm")
        
        # Title in GIANT box at bottom
        if title and "kosong" not in title.lower():
            title_height = 220
            draw.rectangle([margin, HEIGHT-280, WIDTH-margin, HEIGHT-280+title_height], 
                         fill=COLOR_PRIMARY, outline=COLOR_ACCENT, width=15)
            draw.text((WIDTH//2, HEIGHT-170), title, fill=COLOR_ACCENT, font=title_font, 
                     anchor="mm", stroke_width=6, stroke_fill="black")
    
    # === TOP HEADER - SUPER PROMINENT ===
    draw.rectangle([0, 0, WIDTH, 300], fill=COLOR_PRIMARY, outline=COLOR_ACCENT, width=15)
    
    # ICICOS 2026 - ABSOLUTELY MASSIVE
    draw.text((WIDTH//2, 150), "ICICOS 2026", fill=COLOR_ACCENT, font=mega_font, 
             anchor="mm", stroke_width=10, stroke_fill="black")
    
    # === BOTTOM FOOTER - CLEAR ===
    draw.rectangle([0, HEIGHT-220, WIDTH, HEIGHT], fill=COLOR_PRIMARY, outline=COLOR_ACCENT, width=15)
    draw.text((WIDTH//2, HEIGHT-110), "International Conference on Informatics and Computing Systems", 
             fill=COLOR_WHITE, font=medium_font, anchor="mm", stroke_width=3, stroke_fill="black")
    
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
