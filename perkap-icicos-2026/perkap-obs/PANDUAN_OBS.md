# 🎥 Panduan Setup OBS untuk ICICOS 2026

## 📋 Persiapan Awal

### Software yang Dibutuhkan
1. **OBS Studio** (versi terbaru)
2. **Zoom** atau platform conference lainnya
3. **OBS Virtual Camera** plugin (biasanya sudah include di OBS)

## 🎬 Setup Scenes di OBS

### Scene Structure Rekomendasi

```
ICICOS-2026/
├── 1. WAITING ROOM (Day 1)
├── 2. OPENING DAY 1
├── 3. MC
├── 4. SPEAKER - Pak Indra
├── 5. SPEAKER - Dr. Kurnianingsih
├── 6. SPEAKER - Pak Kusworo
├── 7. SPEAKER - Pak Rektor
├── 8. PLENARY 1 - Camera
├── 9. PLENARY 1 - Presentation
├── 10. PLENARY 2 - Camera
├── 11. PLENARY 2 - Presentation
├── 12. HALF RECAP
├── 13. DAY 1 RECAP
├── 14. WAITING ROOM (Day 2)
├── 15. OPENING DAY 2
├── 16. SPEAKER - Pak Aris Sugi
├── 17. PLENARY 3 - Camera
└── 18. PLENARY 3 - Presentation
```

## 🔧 Setup Per Scene

### 1. Waiting Room Scene
**File**: `01_video_loop_day1.png` atau `16_video_loop_day2.png`

**Sources**:
1. Image: Background frame
2. Media Source: Video loop (jika ada video tambahan)
3. Audio: Background music (optional)

**Kegunaan**: Ditampilkan sebelum acara dimulai

---

### 2. Opening Video Scene
**File**: `03_video_opening_day1.png` atau `17_video_opening_day2.png`

**Sources**:
1. Media Source: Opening video
2. Audio: Dari video

**Kegunaan**: Opening ceremony

---

### 3. MC Scene
**File**: `05_frame_mc.png`

**Sources**:
1. Image: Frame MC background
2. Video Capture Device: Camera MC (di tengah frame)
   - Position: Center
   - Size: Sesuaikan dengan area frame
3. Audio Input Capture: Microphone MC

**Kegunaan**: Saat MC membawakan acara

---

### 4. Speaker Scenes
**Files**: `06-09_frame_pak_*.png`, `18_frame_pak_aris_sugi.png`

**Sources** (sama untuk semua speaker):
1. Image: Frame speaker background
2. Video Capture Device: Camera speaker
   - Position: Center
   - Size: Sesuaikan dengan circle indicator
3. Audio Input Capture: Microphone speaker
4. Text (optional): Nama dan title speaker di footer

**Tips**: 
- Buat 1 master scene, lalu duplicate untuk setiap speaker
- Tinggal ganti background image dan nama

---

### 5. Plenary - Camera Only
**Files**: `10_frame_camera_plenary1.png`, etc.

**Sources**:
1. Image: Background frame (split screen)
2. Video Capture Device: Camera 1 (kiri)
   - Position: Left half
3. Video Capture Device: Camera 2 (kanan) atau Zoom participant
   - Position: Right half
4. Audio Input: Mixed audio

**Kegunaan**: Sesi diskusi panel, Q&A

---

### 6. Plenary - Presentation + Camera
**Files**: `11_frame_presentasi_camera_plenary1.png`, etc.

**Sources**:
1. Image: Background frame
2. Window Capture: Presentasi slide (PowerPoint/PDF)
   - Position: Left 75%
   - Crop: Sesuaikan jika perlu
3. Video Capture Device: Camera presenter
   - Position: Right 25% (Picture-in-Picture)
4. Audio Input: Presenter mic

**Kegunaan**: Saat ada presentasi dengan slide

---

### 7. Recap Video Scenes
**Files**: `14_video_half_recap.png`, `15_video_recap_day1.png`

**Sources**:
1. Media Source: Recap video compilation
2. Audio: Dari video

**Kegunaan**: Summary acara di tengah hari / akhir hari

---

## 🎛️ Tips OBS Setup

### Audio Configuration
```
Settings → Audio
- Desktop Audio: Untuk capture sound dari Zoom/presentation
- Mic/Aux 1-3: Untuk microphone eksternal
- Monitoring: Set ke "Monitor and Output" untuk feedback
```

### Video Settings
```
Settings → Video
- Base Resolution: 1920x1080
- Output Resolution: 1920x1080
- FPS: 30 (atau 60 untuk smooth motion)
```

### Output Settings (untuk Virtual Camera ke Zoom)
```
Settings → Output → Recording
- Recording Format: MP4
- Encoder: x264
- Rate Control: CBR
- Bitrate: 2500-3500 Kbps

Virtual Camera:
- Start Virtual Camera
- Select di Zoom sebagai camera source
```

## 🔄 Workflow Saat Live

### Pre-Event (15 menit sebelum)
1. ✅ Scene: Waiting Room loop
2. ✅ Cek audio semua microphone
3. ✅ Cek camera feeds
4. ✅ Start Virtual Camera
5. ✅ Connect ke Zoom meeting

### Event Flow Day 1
```
Waiting Room (loop)
  → Opening Video
    → MC Scene (sambutan)
      → Speaker 1: Pak Indra
        → Speaker 2: Dr. Kurnianingsih
          → Speaker 3: Pak Kusworo
            → Speaker 4: Pak Rektor
              → Plenary 1 (Camera/Presentation)
                → Half Recap
                  → Plenary 2 (Camera/Presentation)
                    → Day 1 Recap
```

### Event Flow Day 2
```
Waiting Room Day 2
  → Opening Day 2
    → MC Scene
      → Speaker: Pak Aris Sugi
        → Plenary 3 (Camera/Presentation)
          → Closing
```

## ⌨️ Hotkeys Rekomendasi

Setup hotkeys untuk switch cepat:

```
Settings → Hotkeys

F1: Scene - Waiting Room
F2: Scene - MC
F3: Scene - Plenary Camera
F4: Scene - Plenary Presentation
F5: Start/Stop Recording
F6: Start/Stop Virtual Camera
F7: Mute/Unmute Desktop Audio
F8: Mute/Unmute Microphone
```

## 🚨 Troubleshooting

### Problem: Video lag
**Solution**: 
- Kurangi bitrate di settings
- Close aplikasi lain yang berat
- Gunakan encoding hardware (NVENC jika punya Nvidia GPU)

### Problem: Audio delay
**Solution**:
- Add audio delay filter (right-click audio source → Filters → Audio Delay)
- Adjust hingga sync dengan video

### Problem: Camera tidak muncul
**Solution**:
- Pastikan camera tidak dipakai aplikasi lain
- Restart OBS
- Cek Device ID di settings

### Problem: Window Capture hitam
**Solution**:
- Run OBS as Administrator
- Disable hardware acceleration di aplikasi yang di-capture
- Gunakan Display Capture sebagai alternatif

## 📱 Backup Plan

Selalu siapkan:
1. ✅ Laptop cadangan dengan OBS setup sama
2. ✅ Scene Collection export (File → Scene Collection → Export)
3. ✅ All source files di USB drive
4. ✅ Kontak teknisi audio/video

## 📚 Resources

- [OBS Official Guide](https://obsproject.com/wiki/)
- [OBS Forum](https://obsproject.com/forum/)
- YouTube: "OBS Tutorial for Conference Streaming"

---

**Good Luck dengan ICICOS 2026! 🎉**
