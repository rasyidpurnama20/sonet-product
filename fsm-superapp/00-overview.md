# 🏛️ FSM UNDIP Super Apps — Overview & Master Feature Map

> **Inisiator:** Wakil Dekan II Fakultas Sains dan Matematika (FSM), Universitas Diponegoro  
> **Tujuan:** Membangun ekosistem digital terpadu yang sustain, scalable, powerful, dan lightweight untuk seluruh civitas akademika FSM UNDIP  
> **Versi Dokumen:** 1.0 — Mei 2026

---

## 📌 Latar Belakang

Fakultas Sains dan Matematika (FSM) UNDIP memiliki kompleksitas operasional yang tinggi:
- Jumlah mahasiswa aktif: **±3.500–4.500 mahasiswa** (estimasi lintas angkatan, program S1–S3)
- Jumlah dosen tetap & tidak tetap: **±200–300 dosen**
- Tenaga kependidikan (Tendik): **±80–120 orang**
- Laboran & teknisi: **±30–60 orang**
- Departemen/Prodi: Matematika, Fisika, Kimia, Biologi, Statistika, Informatika, Ilmu Komputer (± 7–10 prodi)
- Gedung & laboratorium: **±15–25 gedung/unit**, **±40–80 laboratorium aktif**

Tanpa sistem digital terpadu, koordinasi antar unit berjalan manual, lambat, dan tidak tercatat dengan baik — menyebabkan inefisiensi operasional, aset tidak terkelola, dan kepuasan civitas yang rendah.

---

## 👥 Peta Pengguna (User Persona Map)

| Kelompok Pengguna | Estimasi Jumlah | Peran Utama dalam Super Apps |
|---|---|---|
| **Mahasiswa S1** | ±3.000 orang | Pelapor kerusakan, peminjam ruang/lab, penerima notifikasi |
| **Mahasiswa S2/S3** | ±500 orang | Peminjam ruang riset/lab, pelapor kerusakan, kolaborator riset |
| **Dosen Tetap** | ±200 orang | Pemohon fasilitas, approver booking, pemantau KPI unit |
| **Dosen Tidak Tetap / Tamu** | ±50–100 orang | Peminjam ruang, pelapor kerusakan terbatas |
| **Tenaga Kependidikan (Tendik)** | ±100 orang | Operator tiket, pengelola aset, task management |
| **Laboran** | ±40 orang | Pengelola lab, approval booking lab, inventaris alat |
| **Teknisi / Maintenance** | ±20–30 orang | Penerima tiket, update status perbaikan, laporan kerja |
| **Admin Fakultas / Unit** | ±15–20 orang | Super admin modul, pelaporan, konfigurasi sistem |
| **Koordinator Unit / Kaprodi** | ±10–15 orang | Monitoring operasional, approval lapis menengah |
| **Wakil Dekan II** | 1 orang | Executive dashboard, approval strategis, pemantau KPI |
| **Dekan** | 1 orang | Executive summary, decision support |

> **Total estimasi pengguna aktif: ±4.000–5.000 akun**

---

## 🗺️ Ekosistem Modul Super Apps

Super Apps FSM UNDIP terdiri dari **4 modul inti** yang saling terintegrasi:

```
┌─────────────────────────────────────────────────────────────┐
│                   FSM UNDIP SUPER APPS                      │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │ Maintenance │  │    Asset    │  │  Room & Lab │  │   Task     │ │
│  │  Ticketing  │◄─►│ Management │◄─►│   Booking   │◄─►│Management │ │
│  │   System   │  │   System   │  │   System   │  │   System  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│         │                │                │               │         │
│         └────────────────┴────────────────┴───────────────┘         │
│                              │                                       │
│                   ┌──────────▼──────────┐                           │
│                   │  Unified Dashboard  │                           │
│                   │  (WD II / Dekan)    │                           │
│                   └─────────────────────┘                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Klasifikasi Fitur Global

### 🟢 BASIC — Harus Ada (MVP)
Fitur yang **wajib live di hari pertama**. Tanpa ini, super apps tidak berfungsi dan tidak akan diadopsi.

### 🔵 ADVANCED — Sangat Powerful
Fitur yang **menambah nilai signifikan** dan membedakan FSM dari institusi lain. Dibangun pada fase 2 setelah adopsi basic stabil.

### 🟣 PREMIUM — Efisien, Maju, Futuristik
Fitur berbasis **AI/IoT/sensor** yang membawa FSM ke level world-class. Dibangun secara bertahap, memerlukan infrastruktur dan data matang.

---

## 📊 Master Feature Matrix

### Modul 1: Maintenance Ticketing System

| # | Fitur | Level | Nilai Strategis |
|---|---|---|---|
| 1 | Lapor kerusakan fasilitas | 🟢 Basic | Fondasi seluruh sistem |
| 2 | Upload foto kerusakan | 🟢 Basic | Bukti visual, mengurangi ambiguitas |
| 3 | Status tiket (open/on progress/done) | 🟢 Basic | Transparansi proses |
| 4 | Penugasan teknisi | 🟢 Basic | Accountability perbaikan |
| 5 | Riwayat perbaikan | 🟢 Basic | Audit trail fasilitas |
| 6 | Notifikasi WhatsApp/email | 🟢 Basic | Aksesibilitas notifikasi |
| 7 | SLA response time otomatis | 🔵 Advanced | Standar layanan terukur |
| 8 | Prioritas otomatis berdasarkan urgensi | 🔵 Advanced | Efisiensi penanganan |
| 9 | Dashboard kerusakan per gedung/lab | 🔵 Advanced | Visibilitas pimpinan |
| 10 | Analitik teknisi paling aktif | 🔵 Advanced | KPI SDM berbasis data |
| 11 | Preventive maintenance schedule | 🔵 Advanced | Proaktif vs reaktif |
| 12 | AI deteksi kategori kerusakan dari foto | 🟣 Premium | Otomasi klasifikasi |
| 13 | Prediksi fasilitas yang akan rusak | 🟣 Premium | Predictive maintenance |
| 14 | IoT monitoring AC/listrik/lab | 🟣 Premium | Real-time awareness |
| 15 | Auto-routing teknisi terdekat | 🟣 Premium | Optimasi SDM lapangan |
| 16 | Voice report kerusakan via mobile | 🟣 Premium | Aksesibilitas ekstrem |

### Modul 2: Asset Management System

| # | Fitur | Level | Nilai Strategis |
|---|---|---|---|
| 1 | Database aset digital | 🟢 Basic | Inventaris terpusat |
| 2 | QR code aset | 🟢 Basic | Identifikasi cepat |
| 3 | Lokasi aset | 🟢 Basic | Tracking keberadaan |
| 4 | Status aset (baik/rusak/hilang) | 🟢 Basic | Kondisi terkini |
| 5 | Histori maintenance aset | 🟢 Basic | Riwayat perawatan |
| 6 | Mutasi/peminjaman aset | 🟢 Basic | Akuntabilitas pergerakan |
| 7 | Audit aset via mobile scan | 🔵 Advanced | Efisiensi cek fisik |
| 8 | Reminder kalibrasi/perawatan | 🔵 Advanced | Kepatuhan standar lab |
| 9 | Tracking umur aset | 🔵 Advanced | Perencanaan anggaran |
| 10 | Integrasi dengan ticketing | 🔵 Advanced | Data terhubung antar modul |
| 11 | Monitoring utilisasi alat lab | 🔵 Advanced | Optimasi penggunaan |
| 12 | Indoor asset tracking realtime | 🟣 Premium | Lokasi presisi tinggi |
| 13 | AI rekomendasi penggantian aset | 🟣 Premium | Data-driven procurement |
| 14 | Prediksi depresiasi aset | 🟣 Premium | Perencanaan keuangan |
| 15 | Smart inventory analytics | 🟣 Premium | Insight operasional mendalam |
| 16 | Digital twin ruangan & aset | 🟣 Premium | Simulasi & optimasi ruang |

### Modul 3: Room & Lab Booking System

| # | Fitur | Level | Nilai Strategis |
|---|---|---|---|
| 1 | Booking ruang/lab online | 🟢 Basic | Menggantikan proses manual |
| 2 | Kalender penggunaan | 🟢 Basic | Visibilitas ketersediaan |
| 3 | Approval peminjaman | 🟢 Basic | Kontrol penggunaan |
| 4 | Cek ketersediaan real-time | 🟢 Basic | Menghindari double booking |
| 5 | Notifikasi jadwal | 🟢 Basic | Pengingat pengguna |
| 6 | Auto conflict detection | 🔵 Advanced | Mencegah tumpang tindih |
| 7 | Integrasi jadwal kuliah SIAP/SIAK | 🔵 Advanced | Sinkronisasi akademik |
| 8 | Statistik penggunaan ruang | 🔵 Advanced | Data utilisasi fasilitas |
| 9 | Priority booking rules | 🔵 Advanced | Hierarki penggunaan |
| 10 | QR check-in penggunaan ruangan | 🔵 Advanced | Validasi kehadiran |
| 11 | Smart room recommendation | 🟣 Premium | Saran ruang optimal |
| 12 | AI optimasi utilisasi ruang | 🟣 Premium | Efisiensi penggunaan |
| 13 | Sensor okupansi ruangan realtime | 🟣 Premium | Data aktual pengguna |
| 14 | Auto energy saving ruangan kosong | 🟣 Premium | Efisiensi energi |
| 15 | Face recognition check-in | 🟣 Premium | Keamanan & validasi |

### Modul 4: Task Management System

| # | Fitur | Level | Nilai Strategis |
|---|---|---|---|
| 1 | Pembuatan tugas & sub-tugas | 🟢 Basic | Struktur kerja digital |
| 2 | Deadline & reminder otomatis | 🟢 Basic | Disiplin waktu |
| 3 | Penanggung jawab (PIC) | 🟢 Basic | Accountability staf |
| 4 | Progress tracking | 🟢 Basic | Monitoring pelaksanaan |
| 5 | Upload bukti pekerjaan | 🟢 Basic | Dokumentasi hasil kerja |
| 6 | Kanban/Gantt project board | 🔵 Advanced | Visualisasi proyek |
| 7 | Integrasi otomatis dari ticketing | 🔵 Advanced | Tugas otomatis dari laporan |
| 8 | Monitoring beban kerja staf | 🔵 Advanced | Manajemen kapasitas SDM |
| 9 | Escalation otomatis tugas terlambat | 🔵 Advanced | Safeguard deadline |
| 10 | KPI penyelesaian tugas | 🔵 Advanced | Penilaian kinerja objektif |
| 11 | AI task prioritization | 🟣 Premium | Optimasi urutan kerja |
| 12 | Prediksi keterlambatan pekerjaan | 🟣 Premium | Early warning system |
| 13 | Smart workload balancing | 🟣 Premium | Distribusi kerja adil & optimal |
| 14 | Voice assistant operasional | 🟣 Premium | Efisiensi input data |
| 15 | Executive command center realtime | 🟣 Premium | Kendali strategis WD II |

---

## 🔗 Matriks Integrasi Antar Modul

| Dari \ Ke | Ticketing | Asset Mgmt | Room Booking | Task Mgmt |
|---|---|---|---|---|
| **Ticketing** | — | ✅ Aset rusak otomatis diupdate | ✅ Ruang terkunci saat perbaikan | ✅ Auto-create task teknisi |
| **Asset Mgmt** | ✅ Aset perlu servis → buat tiket | — | ✅ Aset terhubung ke ruang | ✅ Jadwal kalibrasi → task |
| **Room Booking** | ✅ Lapor kerusakan ruang | ✅ Cek kelengkapan aset ruang | — | ✅ Booking approved → task setup |
| **Task Mgmt** | ✅ Task selesai → tiket closed | ✅ Task pengadaan → update aset | ✅ Task booking management | — |

---

## 📈 Estimasi Dampak Implementasi

| Aspek | Sebelum Super Apps | Setelah Super Apps (proyeksi) |
|---|---|---|
| Waktu respons kerusakan | 3–7 hari (manual) | < 4 jam (SLA otomatis) |
| Tingkat kehilangan aset | ~15–20% tidak terlacak | < 2% (QR + audit digital) |
| Utilisasi ruang/lab | ~50–60% | 75–85% (booking optimal) |
| Waktu koordinasi task | 2–3 hari per tugas | < 1 hari (notifikasi langsung) |
| Kepuasan civitas | ~60% | > 85% (proyeksi) |
| Penghematan energi | Baseline | ~10–20% (sensor + auto-saving) |

---

## 📁 Daftar Dokumen Analisis

| File | Konten |
|---|---|
| `00-overview.md` | Dokumen ini — gambaran umum, pengguna, fitur master |
| `01-maintenance-ticketing.md` | Analisis SWOT → RACI → Data Readiness → FMEA → RICE |
| `02-asset-management.md` | Analisis SWOT → RACI → Data Readiness → FMEA → RICE |
| `03-room-lab-booking.md` | Analisis SWOT → RACI → Data Readiness → FMEA → RICE |
| `04-task-management.md` | Analisis SWOT → RACI → Data Readiness → FMEA → RICE |
| `05-roadmap-next-steps.md` | Langkah strategis WD II menuju super apps sustain & scalable |

---

*Dokumen ini adalah living document — perbarui setiap kali ada keputusan strategis baru.*
