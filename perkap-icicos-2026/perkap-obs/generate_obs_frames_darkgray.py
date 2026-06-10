#!/usr/bin/env python3
"""
Generator untuk frame OBS ICICOS 2026
DARK GRAY VERSION - Teks nama file, center, full margin, proporsional
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Resolusi standar 16:9
WIDTH = 1920
HEIGHT = 1080

# Dark gray background
COLOR_BG = "#2d2d2d"
COLOR_TEXT = "#ffffff"

MARGIN = 80  # px dari tepi kiri/kanan dan atas/bawah

# Cari font yang tersedia di sistem
FONT_CANDIDATES = [
    "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
]

def find_font():
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None

FONT_PATH = find_font()


def get_font(size):
    if FONT_PATH:
        return ImageFont.truetype(FONT_PATH, size)
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    """Bungkus teks menjadi beberapa baris agar muat dalam max_width."""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test = (current_line + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def measure_block(draw, lines, font, gap_ratio=0.25):
    """Hitung total tinggi blok teks (semua baris + gap)."""
    if not lines:
        return 0, 0
    sample_bbox = draw.textbbox((0, 0), "Ay", font=font)
    line_h = sample_bbox[3] - sample_bbox[1]
    gap = int(line_h * gap_ratio)
    total_h = len(lines) * line_h + (len(lines) - 1) * gap
    return total_h, line_h, gap


def create_frame(label_text, filename):
    """
    Buat PNG dark gray dengan teks label di tengah, full margin, proporsional.
    label_text : teks yang ditampilkan
    filename   : nama file output
    """
    img = Image.new("RGB", (WIDTH, HEIGHT), COLOR_BG)
    draw = ImageDraw.Draw(img)

    max_text_width = WIDTH - 2 * MARGIN    # full margin kiri dan kanan
    max_text_height = HEIGHT - 2 * MARGIN  # full margin atas dan bawah

    # Cari ukuran font terbesar yang muat (turun dari 400)
    best = None
    for size in range(400, 19, -1):
        font = get_font(size)
        lines = wrap_text(draw, label_text, font, max_text_width)
        result = measure_block(draw, lines, font)
        total_h = result[0]
        if total_h <= max_text_height:
            best = (font, size, lines, result)
            break

    if best is None:
        font = get_font(20)
        lines = wrap_text(draw, label_text, font, max_text_width)
        result = measure_block(draw, lines, font)
        best = (font, 20, lines, result)

    font, size, lines, (total_h, line_h, gap) = best

    # Gambar teks di tengah vertikal dan horizontal
    y_start = (HEIGHT - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        x = (WIDTH - w) // 2
        y = y_start + i * (line_h + gap)
        draw.text((x, y), line, fill=COLOR_TEXT, font=font)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    img.save(output_path)
    print(f"✓ {filename}  [font {size}px, {len(lines)} baris, total_h={total_h}px]")


def label_from_filename(filename):
    """Ubah nama file (tanpa ekstensi) menjadi label yang rapi."""
    name = os.path.splitext(filename)[0]          # buang .png
    label = name.replace("_", " ").replace("-", " ")
    return label.upper()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"Font digunakan: {FONT_PATH or 'default (PIL fallback)'}\n")

    png_files = sorted([
        f for f in os.listdir(script_dir)
        if f.lower().endswith(".png")
    ])

    print(f"🎬 Merevisi {len(png_files)} PNG → dark gray + label nama file\n")

    for fname in png_files:
        label = label_from_filename(fname)
        create_frame(label, fname)

    print(f"\n✅ Selesai! {len(png_files)} file diperbarui.")
    print(f"📁 Lokasi: {script_dir}")


if __name__ == "__main__":
    main()
