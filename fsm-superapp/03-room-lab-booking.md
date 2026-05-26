# 🏫 Modul 3: Room & Lab Booking System
## Analisis Lengkap — SWOT → RACI → Data Readiness → FMEA → RICE

> **Deskripsi Modul:** Sistem pemesanan ruangan kelas, ruang rapat, dan laboratorium secara digital — menggantikan proses manual yang sering menimbulkan konflik jadwal, ketidaktransparanan, dan utilisasi ruang yang suboptimal di lingkungan FSM UNDIP.

---

## 📋 Fitur Lengkap

### 🟢 Basic
| # | Fitur | Deskripsi |
|---|---|---|
| 1 | Booking ruang/lab online | Form permintaan: ruang, tanggal, jam, keperluan, jumlah peserta |
| 2 | Kalender penggunaan | Tampilan calendar view per ruangan — harian/mingguan/bulanan |
| 3 | Approval peminjaman | Alur: Request → Review Laboran/Admin → Approved/Rejected |
| 4 | Cek ketersediaan real-time | Status ruang: Tersedia / Dipesan / Dipakai Kuliah / Dalam Perbaikan |
| 5 | Notifikasi jadwal | Konfirmasi booking, reminder H-1 dan H-0 via WA/email |

### 🔵 Advanced
| # | Fitur | Deskripsi |
|---|---|---|
| 6 | Auto conflict detection | Sistem menolak otomatis jika ada overlapping jadwal |
| 7 | Integrasi jadwal kuliah SIAP/SIAK | Jadwal resmi kuliah otomatis di-block, tidak bisa dibooking |
| 8 | Statistik penggunaan ruang | Persentase utilisasi per ruang/lab per periode |
| 9 | Priority booking rules | Dosen > Mahasiswa, kuliah resmi > kegiatan informal, dll |
| 10 | QR check-in penggunaan ruangan | User scan QR di pintu masuk → validasi booking aktif |

### 🟣 Premium
| # | Fitur | Deskripsi |
|---|---|---|
| 11 | Smart room recommendation | Sistem sarankan ruang terbaik berdasarkan kapasitas, fasilitas, lokasi |
| 12 | AI optimasi utilisasi ruang | Analisis pola booking → saran redistribusi kelas/kegiatan |
| 13 | Sensor okupansi ruangan realtime | PIR/kamera → deteksi apakah ruangan benar-benar digunakan |
| 14 | Auto energy saving ruangan kosong | Sensor + smart switch → matikan AC/lampu saat ruang kosong |
| 15 | Face recognition check-in | Kamera pintar → verifikasi identitas pengguna ruangan |

---

## 🔍 Analisis SWOT

### Strengths (Kekuatan Internal)
| # | Kekuatan | Implikasi |
|---|---|---|
| S1 | Pain point booking ruang sangat nyata | Konflik jadwal, ruang telanjur dipakai — pengguna pasti antusias |
| S2 | Ruang dan lab sudah terdefinisi jelas | Master data ruang relatif mudah dibuat dibanding data aset |
| S3 | Jadwal kuliah sudah ada di SIAP/SIAK | Sumber data jadwal kuliah tersedia — tinggal integrasi |
| S4 | Proses approval sudah ada, tinggal digital | Mengdigitalkan proses yang sudah dipahami semua orang |
| S5 | Laboran & admin akademik siap operasional | SDM approver sudah ada dan terlatih proses administrasi |

### Weaknesses (Kelemahan Internal)
| # | Kelemahan | Risiko |
|---|---|---|
| W1 | Tidak ada sistem booking digital sebelumnya | Semua pengguna harus belajar dari nol |
| W2 | Kuliah mendadak sering tidak terjadwal di SIAP | Ruang yang "seharusnya kosong" tiba-tiba dipakai |
| W3 | Beberapa ruangan dikelola oleh unit berbeda | Approval chain tidak seragam, perlu standardisasi |
| W4 | Data kapasitas & fasilitas ruang tidak terdokumentasi | Pengguna tidak bisa tahu kapasitas/fasilitas sebelum booking |
| W5 | Konflik kepentingan booking (senior vs junior) | Tanpa aturan jelas, sistem bisa menimbulkan gesekan baru |

### Opportunities (Peluang Eksternal)
| # | Peluang | Potensi Manfaat |
|---|---|---|
| O1 | Data utilisasi ruang untuk akreditasi BAN-PT | Bukti efisiensi pengelolaan sarana — nilai plus akreditasi |
| O2 | Teknologi calendar API sudah matang (Google, MS) | Integrasi kalender personal mudah dilakukan |
| O3 | QR check-in sangat familiar pasca pandemi | Resistensi pengguna sangat rendah |
| O4 | Peluang hemat energi (listrik) yang terukur | Argumen ROI ke pimpinan menjadi lebih kuat |
| O5 | Modul ini paling mudah di-demo ke stakeholder | Visualisasi langsung — mudah mendapat approval anggaran |

### Threats (Ancaman Eksternal)
| # | Ancaman | Mitigasi |
|---|---|---|
| T1 | Dosen senior tidak mau pakai sistem digital | Buddy system — admin bantu booking untuk yang tidak bisa |
| T2 | "Booking tapi tidak datang" merusak utilisasi data | Sistem no-show penalty + forfeit otomatis jika tidak check-in |
| T3 | API SIAP/SIAK UNDIP tidak terbuka | Scraping jadwal atau input manual bulanan sebagai alternatif |
| T4 | Lab khusus dengan akses terbatas → keamanan | Role-based access + persetujuan ekstra untuk lab berbahaya |
| T5 | Booking musiman (ujian, seminar) membanjiri sistem | Load testing + rate limiting + antrian waitlist |

---

## 👥 RACI Matrix

| Aktivitas | WD II | Admin Akademik | Laboran | Dosen | Mahasiswa | IT Dev |
|---|---|---|---|---|---|---|
| Request booking ruang | I | I | I | R | R | — |
| Review & approve booking | I | R | A | C | I | — |
| Setup master data ruangan | C | A/R | C | I | I | C |
| Input jadwal kuliah ke sistem | I | A/R | I | C | I | C |
| Monitor conflict detection | C | A | R | I | I | I |
| Konfigurasi priority rules | A | R | C | C | I | C |
| QR check-in operasional | I | I | A/R | I | I | — |
| Laporan utilisasi ruang | A | R | C | I | I | I |
| Konfigurasi integrasi SIAP/SIAK | A | C | I | I | I | A/R |
| Pengembangan sistem | C | C | I | I | I | A/R |

---

## 📦 Data Readiness Assessment

### Data yang Dibutuhkan

| Data | Sumber Saat Ini | Status | Aksi yang Diperlukan |
|---|---|---|---|
| Daftar ruangan & lab FSM | Denah/arsip fisik | 🟡 Ada, tidak digital | Buat master data ruangan: nama, kapasitas, fasilitas |
| Kapasitas tiap ruangan | Tidak ada standar | 🔴 Tidak ada | Survey fisik & dokumentasi |
| Fasilitas per ruangan | Tidak terdokumentasi | 🔴 Tidak ada | Inventarisasi: proyektor, AC, wifi, daya listrik |
| Jadwal kuliah resmi | SIAP/SIAK UNDIP | 🟢 Ada | Integrasikan via API atau export berkala |
| Data pengguna (dosen, mhs) | SSO UNDIP / SIAK | 🟢 Ada | Sinkronisasi akun pengguna |
| Aturan prioritas booking | Tidak ada kebijakan tertulis | 🔴 Tidak ada | Workshop dengan WD II → buat SOP resmi |
| Histori penggunaan ruang | Tidak ada | 🔴 Tidak ada | Collect dari hari pertama sistem aktif |
| SLA approval booking | Tidak ada | 🔴 Tidak ada | Tentukan: berapa jam response time wajib |

### Data Readiness Score
| Dimensi | Score (1–5) | Keterangan |
|---|---|---|
| Ketersediaan Data | 3/5 | Jadwal kuliah & pengguna sudah ada di sistem UNDIP |
| Kualitas Data | 2/5 | Jadwal SIAP kadang tidak update, perlu verifikasi |
| Aksesibilitas Data | 3/5 | SIAK ada, tapi akses API perlu approval IT pusat UNDIP |
| Governance Data | 2/5 | Aturan booking belum ada, perlu dibuat dari awal |
| **Total Rata-rata** | **2.5/5** | 🟡 Lebih siap dari modul lain — bisa go-live lebih cepat |

### Quick Start Data Plan
```
Minggu 1: Buat master data 30 ruang/lab prioritas (kapasitas + fasilitas)
Minggu 2: Input jadwal kuliah semester berjalan (manual jika API tidak siap)
Minggu 3: Definisikan SOP priority booking + approval chain per jenis ruang
Minggu 4: Uji coba dengan 1 departemen pilot, refine berdasarkan feedback
```

---

## ⚠️ FMEA (Failure Mode and Effects Analysis)

| # | Failure Mode | Efek Kegagalan | S | O | D | RPN | Tindakan Pencegahan |
|---|---|---|---|---|---|---|---|
| 1 | Double booking terjadi | Konflik penggunaan ruang, kepercayaan runtuh | 9 | 5 | 2 | **90** 🟡 | Database lock saat booking, auto conflict detection |
| 2 | Jadwal kuliah resmi tidak sinkron | Booking diterima padahal ruang ada kuliah | 9 | 6 | 3 | **162** 🔴 | Sinkronisasi SIAP mingguan + buffer manual |
| 3 | No-show booking (booking tapi tidak pakai) | Utilisasi data salah, ruang terlihat penuh padahal kosong | 7 | 8 | 3 | **168** 🔴 | Auto-release jika tidak check-in dalam 15 menit |
| 4 | Approval lambat > 24 jam | Pengguna frustrasi, kembali ke cara manual | 7 | 7 | 4 | **196** 🔴 | SLA approval 4 jam, eskalasi otomatis jika lewat |
| 5 | Pengguna tidak dapat notifikasi | Lupa jadwal booking, ruang kosong terbuang | 6 | 5 | 4 | **120** 🔴 | Multi-channel: WA + email + in-app reminder |
| 6 | Ruang dalam perbaikan tidak di-block | Pengguna datang ke ruang yang sedang diperbaiki | 7 | 4 | 3 | **84** 🟡 | Integrasi dengan modul ticketing → auto-block |
| 7 | Akses tidak sah ke lab berbahaya | Kecelakaan lab, kerugian aset, insiden K3 | 10 | 3 | 2 | **60** 🟡 | Approval berlapis untuk lab khusus + verifikasi identitas |
| 8 | Sistem down saat peak hour (jadwal awal semester) | Semua booking manual kembali | 8 | 4 | 2 | **64** 🟡 | Auto-scaling cloud, load testing sebelum semester |
| 9 | Data kapasitas ruang salah | Overbooked secara fisik | 7 | 5 | 4 | **140** 🔴 | Survey fisik + update kapasitas via admin |
| 10 | Booking prioritas tidak dihormati | Konflik sosial antara dosen & mahasiswa | 8 | 5 | 3 | **120** 🔴 | Aturan prioritas otomatis di engine booking |

### Top 3 RPN — Prioritas Mitigasi Utama
1. **RPN 196** — Approval lambat → SLA wajib 4 jam + eskalasi otomatis ke WD II
2. **RPN 168** — No-show → Auto-release + forfeit booking dalam 15 menit
3. **RPN 162** — Jadwal kuliah tidak sinkron → Sinkronisasi SIAP mingguan wajib

---

## 🍚 RICE Scoring — Prioritas Fitur

| # | Fitur | R | I | C | E | RICE Score | Prioritas |
|---|---|---|---|---|---|---|---|
| 1 | Form booking online | 3500 | 3 | 90% | 3 | **3.150** | 🥇 #1 |
| 2 | Kalender penggunaan | 3500 | 3 | 90% | 2 | **4.725** | 🥇 #1 |
| 3 | Approval workflow | 3500 | 3 | 90% | 3 | **3.150** | 🥇 #1 |
| 4 | Cek ketersediaan real-time | 3500 | 3 | 95% | 2 | **4.988** | 🥇 #1 |
| 5 | Notifikasi jadwal | 3500 | 2 | 90% | 2 | **3.150** | 🥇 #2 |
| 6 | Auto conflict detection | 3500 | 3 | 90% | 4 | **2.363** | 🔵 #3 |
| 7 | Integrasi jadwal kuliah SIAP | 3500 | 3 | 75% | 8 | **984** | 🔵 #4 |
| 8 | Statistik penggunaan ruang | 30 | 2 | 85% | 4 | **12.75** | 🔵 #8 |
| 9 | Priority booking rules | 3500 | 3 | 80% | 5 | **1.680** | 🔵 #5 |
| 10 | QR check-in | 3500 | 2 | 85% | 4 | **1.488** | 🔵 #6 |
| 11 | Smart room recommendation | 3500 | 2 | 65% | 10 | **455** | 🟣 #9 |
| 12 | AI optimasi utilisasi | 30 | 3 | 55% | 20 | **2.5** | 🟣 #12 |
| 13 | Sensor okupansi realtime | 100 | 3 | 50% | 25 | **6** | 🟣 #11 |
| 14 | Auto energy saving | 5 | 2 | 45% | 30 | **0.15** | 🟣 #14 |
| 15 | Face recognition check-in | 3500 | 2 | 40% | 35 | **80** | 🟣 #10 |

### Kesimpulan RICE — Urutan Implementasi
```
FASE 1 (0–3 bulan):  Kalender + cek ketersediaan → form booking → approval → notifikasi
FASE 2 (3–6 bulan):  Auto conflict → priority rules → QR check-in
FASE 3 (6–12 bulan): Integrasi SIAP → statistik utilisasi → smart recommendation
FASE 4 (12+ bulan):  AI optimasi → sensor okupansi → energy saving → face recognition
```

---

## 💡 Rekomendasi Strategis Khusus Modul Ini

1. **Modul ini paling mudah di-launch & di-demo:** Mulai dari sini untuk membangun momentum dan trust civitas terhadap super apps.
2. **Auto-release 15 menit adalah game changer:** Fitur ini sendiri sudah cukup menjual sistem ini ke dosen dan mahasiswa.
3. **Jadikan kalender sebagai halaman utama:** Visual calendar yang indah dan responsif = adopsi lebih cepat tanpa training.
4. **Pilot dengan 1 departemen yang antusias:** Cari kaprodi yang pro-digital, jadikan success story untuk roll-out ke seluruh FSM.
5. **Hubungkan data utilisasi ke akreditasi:** Data penggunaan ruang selama 6 bulan = dokumen akreditasi yang kuat → WD II punya argumen kuat untuk keberlanjutan proyek.

---

*Dokumen ini bagian dari FSM Super Apps Analysis Suite | Lihat juga: [00-overview.md](./00-overview.md)*
