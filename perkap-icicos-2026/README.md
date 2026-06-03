# ICICOS 2026 - Persiapan Konferensi

Repository persiapan untuk **International Conference on Informatics and Computing Systems (ICICOS) 2026**

## 🚀 ULTIMATE VERSION V3 - SUPER BESAR & SANGAT JELAS!

**Perbaikan MAJOR dari feedback:**
- 🔥 **Font ULTRA BESAR**: 70pt sampai 200pt (3-4x lebih besar dari sebelumnya!)
- 🔥 **Judul SANGAT JELAS**: Setiap frame punya label yang MASSIVE
- 🔥 **Stroke outline TEBAL**: 6-10px untuk clarity sempurna
- 🔥 **Kontras maksimal**: Warna bold dengan border tebal
- 🔥 **Layout SIMPLE & BOLD**: Fokus pada readability
- 🔥 **Icons GIANT**: Speaker icon 200pt, shapes radius 400px
- 🔥 **Perfect untuk streaming**: Terbaca jelas bahkan di layar kecil!

## 📁 Struktur Folder

```
perkap-icicos-2026/
└── perkap-obs/          # OBS Studio frames dan setup guide
    ├── *.png            # 20 frame placeholder untuk streaming
    ├── generate_obs_frames.py
    ├── README.md
    └── PANDUAN_OBS.md
```

## 🎬 OBS Streaming Setup

Folder `perkap-obs/` berisi semua yang dibutuhkan untuk setup streaming Zoom menggunakan OBS Studio:

### ✅ Sudah Dibuat (20 Frames)

#### Day 1
- Video Loop & Opening Day 1
- Frame MC, Pak Indra, Dr. Kurnianingsih, Pak Kusworo, Pak Rektor
- Plenary Session 1 & 2 (Camera + Presentation views)
- Half Recap & Full Recap Day 1

#### Day 2
- Video Loop & Opening Day 2
- Frame Pak Aris Sugi
- Plenary Session 3 (Camera + Presentation views)

### 📋 Spesifikasi Teknis

- **Resolusi**: 1920x1080 (Full HD 16:9)
- **Format**: PNG dengan transparency support
- **Color Scheme**: Professional blue & orange branding
- **Layout Types**:
  - Video frames (intro/outro)
  - Speaker frames (dengan area camera center)
  - Plenary camera frames (split screen)
  - Presentation + camera frames (75/25 layout)

## 🚀 Quick Start

### Generate/Regenerate Frames

```bash
cd perkap-obs
python3 generate_obs_frames.py
```

### Setup OBS

Lihat panduan lengkap di: `perkap-obs/PANDUAN_OBS.md`

Quick steps:
1. Import semua PNG files ke OBS
2. Buat scene untuk setiap frame
3. Tambah video/camera sources sesuai kebutuhan
4. Setup Virtual Camera untuk output ke Zoom
5. Test semua scenes sebelum hari H

## 📝 Customization

Edit `perkap-obs/generate_obs_frames.py` untuk:
- Ubah color scheme
- Tambah/kurangi frames
- Modify layout
- Add logos/branding

## 🎯 Next Steps

- [ ] Tambahkan logo ICICOS resmi
- [ ] Tambahkan sponsor logos
- [ ] Buat video loop animations (Premiere/After Effects)
- [ ] Buat video recap templates
- [ ] Test run dengan Zoom meeting
- [ ] Rehearsal dengan MC dan speakers

## 👥 Tim Teknis

Pastikan tim teknis sudah familiar dengan:
- OBS Studio operation
- Scene switching & transitions
- Audio mixing & monitoring
- Troubleshooting live issues
- Backup procedures

## 📞 Support

Untuk pertanyaan teknis OBS/streaming, hubungi tim IT FSM.

---

**Semoga sukses untuk ICICOS 2026! 🎓✨**
