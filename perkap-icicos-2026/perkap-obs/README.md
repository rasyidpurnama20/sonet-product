# OBS Frames untuk ICICOS 2026

Folder ini berisi placeholder visual untuk streaming Zoom menggunakan OBS Studio untuk konferensi ICICOS 2026.

## 📋 Daftar Frame yang Dibuat

### Day 1 - Video Loops & Transitions
- `01_video_loop_day1.png` - Video Loop Day 1 (waiting screen)
- `02_video_transisi.png` - Video Transisi
- `03_video_opening_day1.png` - Video Opening Day 1

### Day 1 - Speaker Frames
- `04_frame_kosong.png` - Frame Kosong
- `05_frame_mc.png` - Frame MC (Master of Ceremony)
- `06_frame_pak_indra.png` - Frame Pak Indra
- `07_frame_dr_kurnianingsih.png` - Frame Dr. Kurnianingsih
- `08_frame_pak_kusworo.png` - Frame Pak Kusworo
- `09_frame_pak_rektor.png` - Frame Pak Rektor

### Day 1 - Plenary Sessions
- `10_frame_camera_plenary1.png` - Frame Camera Plenary 1
- `11_frame_presentasi_camera_plenary1.png` - Frame Presentasi Window + Camera Plenary 1
- `12_frame_camera_plenary2.png` - Frame Camera Plenary 2
- `13_frame_presentasi_camera_plenary2.png` - Frame Presentasi Window + Camera Plenary 2

### Day 1 - Recap Videos
- `14_video_half_recap.png` - Video Half Recap
- `15_video_recap_day1.png` - Video Recap Day 1

### Day 2 - Video Loops & Speaker
- `16_video_loop_day2.png` - Video Loop Day 2
- `17_video_opening_day2.png` - Video Opening Day 2
- `18_frame_pak_aris_sugi.png` - Frame Pak Aris Sugi

### Day 2 - Plenary Session
- `19_frame_camera_plenary3.png` - Frame Camera Plenary 3
- `20_frame_presentasi_camera_plenary3.png` - Frame Presentasi Window + Camera Plenary 3

## 🎨 Desain Spesifikasi (ULTIMATE V3 - SUPER UPGRADE!)

- **Resolusi**: 1920x1080 (16:9 Full HD)
- **Typography**: ULTRA MASSIVE - Font size 70pt sampai 200pt!
  - Logo "ICICOS 2026": 200pt (ABSOLUTELY GIANT!)
  - Labels utama: 160-200pt (MASSIVE!)
  - Titles: 100-120pt (HUGE!)
  - Body text: 70pt (BIG!)
- **Color Scheme**:
  - Primary: Strong Blue (#1e40af)
  - Accent: Strong Orange (#ea580c)
  - Backgrounds: Pure contrast (#ffffff / #0f172a)
- **Features**:
  - ⭐ Stroke outline TEBAL (6-10px)
  - ⭐ Border super thick (15-30px)
  - ⭐ Giant shapes (radius 400px)
  - ⭐ Multi-layer glow effects (8 layers)
  - ⭐ Divider ultra-wide (60-80px)
  - ⭐ Header/footer 220-300px height

## 🎬 Tipe Frame

### 1. Video Frames
Background gelap untuk video loop dan transition, cocok untuk intro/outro

### 2. Speaker Frames
Frame dengan area speaker di tengah, header/footer ICICOS branding

### 3. Camera Plenary Frames
Split screen untuk menampilkan kamera pembicara

### 4. Presentation + Camera Frames
Layout 75% presentasi + 25% kamera pembicara (PiP style)

## 🔧 Cara Regenerate

Jalankan script Python untuk membuat ulang semua frame:

```bash
python3 generate_obs_frames.py
```

## 📝 Customization

Edit file `generate_obs_frames.py` untuk:
- Mengubah warna tema
- Menambah/mengurangi frame
- Mengubah layout
- Menambah logo/grafis tambahan

## 💡 Penggunaan di OBS

1. Import semua PNG files ke OBS sebagai Image Sources
2. Buat Scene untuk setiap frame
3. Overlay dengan video Zoom/camera sesuai kebutuhan
4. Gunakan Scene Transitions untuk perpindahan smooth

## ✅ Status

- [x] 20 Frame placeholder sudah dibuat
- [ ] Tambahkan logo ICICOS asli
- [ ] Tambahkan sponsor logos
- [ ] Sesuaikan dengan brand guidelines final
