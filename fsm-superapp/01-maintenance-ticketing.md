# 🔧 Modul 1: Maintenance Ticketing System
## Analisis Lengkap — SWOT → RACI → Data Readiness → FMEA → RICE

> **Deskripsi Modul:** Sistem pelaporan dan pengelolaan kerusakan fasilitas secara digital, mulai dari laporan awal hingga selesai diperbaiki, lengkap dengan tracking status, penugasan teknisi, dan riwayat histori.

---

## 📋 Fitur Lengkap

### 🟢 Basic
| # | Fitur | Deskripsi |
|---|---|---|
| 1 | Lapor kerusakan fasilitas | Form digital pelaporan dengan kategori (listrik, AC, kebersihan, struktur, dll) |
| 2 | Upload foto kerusakan | Bukti visual kerusakan, mendukung multi-foto |
| 3 | Status tiket | Alur: Open → Assigned → On Progress → Resolved → Closed |
| 4 | Penugasan teknisi | Admin/sistem menugaskan teknisi sesuai kategori & ketersediaan |
| 5 | Riwayat perbaikan | Histori lengkap tiap fasilitas: siapa, kapan, apa yang diperbaiki |
| 6 | Notifikasi WhatsApp/email | Push notification ke pelapor dan teknisi saat status berubah |

### 🔵 Advanced
| # | Fitur | Deskripsi |
|---|---|---|
| 7 | SLA response time otomatis | Setiap kategori punya target waktu; sistem alert jika melebihi batas |
| 8 | Prioritas otomatis berdasarkan urgensi | Scoring: lokasi (lab aktif vs gudang), jenis kerusakan, dampak kuliah |
| 9 | Dashboard kerusakan per gedung/lab | Heatmap kerusakan, trending masalah terbanyak per lokasi |
| 10 | Analitik teknisi paling aktif | Jumlah tiket diselesaikan, rata-rata waktu, rating kepuasan |
| 11 | Preventive maintenance schedule | Jadwal rutin inspeksi AC, genset, instalasi listrik, lab kimia, dll |

### 🟣 Premium
| # | Fitur | Deskripsi |
|---|---|---|
| 12 | AI deteksi kategori dari foto | Model vision mengenali jenis kerusakan dari foto upload |
| 13 | Prediksi fasilitas akan rusak | ML berbasis histori tiket + usia aset + pola kerusakan |
| 14 | IoT monitoring AC/listrik/lab | Sensor suhu, kelembaban, konsumsi daya → alert anomali |
| 15 | Auto-routing teknisi terdekat | GPS teknisi + beban kerja → assign optimal |
| 16 | Voice report via mobile | Speech-to-text untuk laporan hands-free |

---

## 🔍 Analisis SWOT

### Strengths (Kekuatan Internal)
| # | Kekuatan | Implikasi |
|---|---|---|
| S1 | WD II sebagai champion langsung | Decision-making cepat, ada sponsor kuat dari atas |
| S2 | Masalah nyata & terasa sehari-hari | Adopsi lebih mudah karena pain point sudah ada |
| S3 | Teknisi & tendik sudah terstruktur | Ada SDM yang bisa langsung menggunakan sistem |
| S4 | Infrastruktur jaringan kampus ada | WiFi sudah ada di gedung-gedung utama |
| S5 | Komunitas mahasiswa IT/informatika | Sumber daya pengembang internal yang potensial |

### Weaknesses (Kelemahan Internal)
| # | Kelemahan | Risiko |
|---|---|---|
| W1 | Belum ada baseline data kerusakan histori | Tidak bisa langsung analitik, perlu warm-up period |
| W2 | Literasi digital teknisi/tendik bervariasi | Resistensi penggunaan, butuh pelatihan intensif |
| W3 | Tidak ada dedicated IT support internal | Maintenance sistem bergantung pihak luar atau volunteer |
| W4 | Anggaran teknologi tidak selalu prioritas | Risiko proyek terhenti di tengah jalan |
| W5 | Fragmentasi data antar departemen | Data aset & ruang belum terpusat, susah diintegrasikan |

### Opportunities (Peluang Eksternal)
| # | Peluang | Potensi Manfaat |
|---|---|---|
| O1 | Program digitalisasi UNDIP / DIKTI | Potensi pendanaan dari program kampus merdeka digital |
| O2 | Teknologi open-source makin matang | Biaya pengembangan lebih rendah (GLPI, osTicket, custom) |
| O3 | Tren "smart campus" di universitas top | Positioning FSM sebagai pelopor di lingkungan UNDIP |
| O4 | WhatsApp Business API semakin mudah | Notifikasi ke pengguna tanpa perlu install app baru |
| O5 | Komunitas developer Semarang aktif | Bisa rekrut atau kolaborasi dengan komunitas lokal |

### Threats (Ancaman Eksternal)
| # | Ancaman | Mitigasi |
|---|---|---|
| T1 | Pergantian pimpinan → proyek terbengkalai | Institusionalisasi sistem, bukan personalitas pimpinan |
| T2 | Pengguna tidak mau mengubah kebiasaan | Gamifikasi, sosialisasi masif, quick wins nyata |
| T3 | Vendor/developer tidak reliable | Kontrak SLA ketat, dokumentasi kode wajib |
| T4 | Keamanan data (data bocor, akses tak sah) | Autentikasi SSO UNDIP, enkripsi data, audit log |
| T5 | Ketergantungan infrastruktur (server down) | Cloud + backup, desain offline-first untuk mobile |

---

## 👥 RACI Matrix

> **R** = Responsible (mengerjakan) | **A** = Accountable (bertanggung jawab penuh) | **C** = Consulted (dimintai pendapat) | **I** = Informed (diberitahu)

| Aktivitas | WD II | Admin Fakultas | Teknisi | Tendik/Operator | Dosen | Mahasiswa | IT Dev |
|---|---|---|---|---|---|---|---|
| Membuat laporan kerusakan | I | I | I | C | R | R | — |
| Menerima & verifikasi tiket | I | A | R | R | I | I | — |
| Menugaskan teknisi | I | A/R | C | R | I | I | — |
| Melaksanakan perbaikan | I | I | R/A | I | I | I | — |
| Update status tiket | I | I | R | R | I | I | — |
| Konfigurasi SLA & prioritas | A | R | C | C | I | I | C |
| Monitoring dashboard | A | R | I | I | C | — | I |
| Laporan kinerja teknisi | A | R | I | I | I | — | I |
| Preventive maintenance jadwal | A | R | C | R | I | I | — |
| Pengembangan & maintenance sistem | C | C | I | I | — | — | A/R |

---

## 📦 Data Readiness Assessment

### Data yang Dibutuhkan

| Data | Sumber Saat Ini | Status | Aksi yang Diperlukan |
|---|---|---|---|
| Daftar fasilitas/ruangan FSM | Manual/arsip fisik | 🔴 Belum digital | Digitalisasi & standarisasi nama ruang |
| Daftar teknisi & spesialisasi | HR/kepegawaian | 🟡 Ada, tidak terstruktur | Import & mapping ke sistem |
| Histori kerusakan sebelumnya | Buku catatan manual | 🔴 Tidak ada | Mulai fresh, collect dari hari pertama |
| Kontak pengguna (WA/email) | SIAK/kepegawaian | 🟡 Parsial | Sinkronisasi dengan sistem SSO UNDIP |
| Kategori kerusakan standar | Tidak ada | 🔴 Belum ada | Definisikan taxonomy kerusakan FSM |
| SLA target per kategori | Tidak ada | 🔴 Belum ada | Workshop dengan WD II & teknisi |
| Jadwal preventive maintenance | Tidak ada | 🔴 Belum ada | Buat dari nol berdasarkan best practice |
| Data IoT (AC, listrik) | Tidak ada | 🔴 Belum ada | Pasang sensor (fase premium) |

### Data Readiness Score
| Dimensi | Score (1–5) | Keterangan |
|---|---|---|
| Ketersediaan Data | 2/5 | Data sangat minim, sebagian besar manual |
| Kualitas Data | 1/5 | Tidak ada standar, inkonsisten |
| Aksesibilitas Data | 2/5 | Ada tapi tersebar, sulit diakses |
| Governance Data | 1/5 | Tidak ada PIC data yang jelas |
| **Total Rata-rata** | **1.5/5** | 🔴 Perlu persiapan serius sebelum go-live |

### Rekomendasi Data Sprint (4 minggu sebelum launch)
1. **Minggu 1:** Inventarisasi semua nama ruang & gedung FSM → buat master data
2. **Minggu 2:** Daftarkan semua teknisi + spesialisasi + nomor WA → import ke sistem
3. **Minggu 3:** Definisikan kategori kerusakan + SLA per kategori → validasi WD II
4. **Minggu 4:** Uji coba input data, pelatihan operator, dry run sistem

---

## ⚠️ FMEA (Failure Mode and Effects Analysis)

> **Severity (S):** 1–10 | **Occurrence (O):** 1–10 | **Detection (D):** 1–10 | **RPN = S × O × D**
> RPN > 100: Prioritas tinggi | 50–100: Sedang | < 50: Rendah

| # | Failure Mode | Efek Kegagalan | S | O | D | RPN | Tindakan Pencegahan |
|---|---|---|---|---|---|---|---|
| 1 | Sistem notif WA tidak terkirim | Teknisi tidak tahu ada tiket baru | 8 | 6 | 3 | **144** 🔴 | Fallback email + in-app notif, retry logic |
| 2 | Teknisi tidak update status tiket | Pelapor tidak tahu progress, trust menurun | 7 | 7 | 4 | **196** 🔴 | Auto-reminder ke teknisi, eskalasi ke admin |
| 3 | Server down saat jam sibuk | Tidak bisa lapor kerusakan | 9 | 3 | 2 | **54** 🟡 | SLA uptime 99.5%, backup server, offline mode |
| 4 | Foto tidak berhasil diupload | Data kerusakan tidak lengkap | 5 | 5 | 4 | **100** 🔴 | Kompresi otomatis, batas ukuran file, retry |
| 5 | Pengguna salah kategorisasi kerusakan | Penugasan teknisi salah | 6 | 7 | 5 | **210** 🔴 | AI auto-suggest kategori, validasi admin |
| 6 | Tiket di-close tanpa perbaikan nyata | Masalah tidak terselesaikan | 9 | 4 | 3 | **108** 🔴 | Rating kepuasan pelapor wajib sebelum close |
| 7 | Data pengguna tidak terupdate | Notifikasi ke nomor salah | 5 | 6 | 4 | **120** 🔴 | Sinkronisasi berkala dengan SSO UNDIP |
| 8 | Akses tidak sah ke tiket orang lain | Privasi data terganggu | 8 | 3 | 3 | **72** 🟡 | RBAC ketat, audit log, enkripsi |
| 9 | SLA tidak terpantau | Kerusakan terabaikan tanpa eskalasi | 7 | 5 | 4 | **140** 🔴 | Cron job SLA checker tiap 1 jam, alert WD II |
| 10 | Resistensi pengguna → sistem tidak dipakai | Investasi sia-sia | 10 | 6 | 2 | **120** 🔴 | Change management, sosialisasi, quick wins |

### Top 3 RPN — Prioritas Mitigasi Utama
1. **RPN 210** — Salah kategorisasi → Bangun AI suggest + validasi dua lapis
2. **RPN 196** — Teknisi tidak update status → Auto-reminder + eskalasi wajib
3. **RPN 144** — Notifikasi WA gagal → Multi-channel notif + retry system

---

## 🍚 RICE Scoring — Prioritas Fitur

> **R** = Reach (pengguna/bulan) | **I** = Impact (1–3: Low/Med/High) | **C** = Confidence (%) | **E** = Effort (person-weeks)
> **RICE Score = (R × I × C) / E**

| # | Fitur | R | I | C | E | RICE Score | Prioritas |
|---|---|---|---|---|---|---|---|
| 1 | Lapor kerusakan (form digital) | 4000 | 3 | 95% | 2 | **5.700** | 🥇 #1 |
| 2 | Notifikasi WA/email | 4000 | 3 | 90% | 3 | **3.600** | 🥇 #2 |
| 3 | Status tracking tiket | 4000 | 3 | 95% | 2 | **5.700** | 🥇 #1 |
| 4 | Upload foto | 4000 | 2 | 90% | 1 | **7.200** | 🥇 #1 |
| 5 | Riwayat perbaikan | 500 | 2 | 85% | 2 | **425** | 🟡 #6 |
| 6 | Penugasan teknisi | 60 | 3 | 90% | 2 | **81** | 🟡 #7 |
| 7 | SLA auto response | 60 | 3 | 80% | 4 | **36** | 🔵 #9 |
| 8 | Prioritas urgensi otomatis | 4000 | 3 | 75% | 5 | **1.800** | 🔵 #5 |
| 9 | Dashboard kerusakan per gedung | 20 | 3 | 85% | 6 | **8.5** | 🔵 #10 |
| 10 | Analitik kinerja teknisi | 20 | 2 | 80% | 4 | **8** | 🔵 #11 |
| 11 | Preventive maintenance schedule | 60 | 3 | 70% | 8 | **15.75** | 🔵 #8 |
| 12 | AI deteksi kategori dari foto | 4000 | 3 | 60% | 20 | **360** | 🟣 #12 |
| 13 | Prediksi fasilitas rusak | 20 | 3 | 50% | 30 | **1** | 🟣 #16 |
| 14 | IoT monitoring | 5 | 3 | 40% | 40 | **0.15** | 🟣 #17 |
| 15 | Auto-routing teknisi | 30 | 2 | 55% | 20 | **1.65** | 🟣 #15 |
| 16 | Voice report | 200 | 1 | 50% | 12 | **8.3** | 🟣 #13 |

### Kesimpulan RICE — Urutan Implementasi
```
FASE 1 (0–3 bulan):  Upload foto → Form laporan → Status tracking → Notifikasi WA
FASE 2 (3–6 bulan):  Prioritas urgensi → Riwayat perbaikan → Penugasan teknisi
FASE 3 (6–12 bulan): SLA otomatis → Preventive schedule → Dashboard → Analitik
FASE 4 (12+ bulan):  AI foto → Prediksi → IoT → Auto-routing → Voice
```

---

## 💡 Rekomendasi Strategis Khusus Modul Ini

1. **Quick Win dalam 30 hari:** Deploy form pelaporan + notifikasi WA sederhana. Ini langsung terasa manfaatnya oleh seluruh civitas.
2. **Rating wajib sebelum tiket ditutup:** Mencegah gaming sistem dan memastikan kualitas perbaikan benar-benar terjadi.
3. **Pilot di 1 gedung dulu:** Mulai dari gedung paling bermasalah (high-traffic lab), baru scale ke seluruh FSM.
4. **Teknisi sebagai hero:** Beri dashboard khusus teknisi yang mobile-friendly — mereka ujung tombak kesuksesan modul ini.
5. **Integrasi WA dulu, bukan app native:** Pengguna tidak perlu install apapun — kirim link via WA untuk akses web-based.

---

*Dokumen ini bagian dari FSM Super Apps Analysis Suite | Lihat juga: [00-overview.md](./00-overview.md)*
