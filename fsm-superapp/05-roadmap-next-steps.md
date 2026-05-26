# 🗺️ Roadmap & Next Steps Strategis
## Panduan WD II Menuju Super Apps FSM UNDIP yang Sustain, Scalable, Powerful & Lightweight

> **Untuk:** Wakil Dekan II FSM UNDIP  
> **Konteks:** Dokumen ini menjawab pertanyaan: *"Setelah semua analisis ini, apa yang harus saya siapkan dan lakukan?"*  
> **Filosofi:** Bangun ekosistem, bukan sekadar aplikasi. Super apps yang benar-benar bertahan adalah yang menjadi kebiasaan institusi, bukan proyek teknologi satu kali.

---

## 🧭 Prinsip Dasar Sebelum Melangkah

Sebelum satu baris kode ditulis, tanamkan 4 prinsip ini dalam setiap keputusan:

| Prinsip | Artinya dalam Konteks FSM |
|---|---|
| **Sustain** | Sistem tetap hidup & relevan meski WD II berganti; ada SOP, dana, dan tim yang menjaga |
| **Scalable** | Mulai dari 100 pengguna, siap melayani 5.000 pengguna tanpa rebuild dari nol |
| **Powerful** | Setiap fitur memberikan dampak nyata yang bisa diukur, bukan sekadar keren di atas kertas |
| **Lightweight** | Cepat di HP jaringan kampus, tidak butuh install app besar, mudah dipakai tanpa training panjang |

---

## 📅 Master Roadmap — 24 Bulan

```
TAHUN 1                                    TAHUN 2
Q1 (Jan–Mar)  Q2 (Apr–Jun)  Q3 (Jul–Sep)  Q4 (Okt–Des)  Q5 (Jan–Mar)  Q6 (Apr–Jun+)
     │              │              │              │              │              │
  FONDASI       LAUNCH MVP     STABILISASI    PENGUATAN     ADVANCED      PREMIUM
  & DESAIN      BERTAHAP       & ADOPSI       INTEGRASI     FEATURES      & AI/IoT
```

---

## 🏗️ FASE 0 — Fondasi (Bulan 1–2)
### "Jangan bangun sebelum tanahnya kuat"

Fase ini adalah yang paling menentukan keberhasilan jangka panjang. Tidak ada produk yang dibuat di fase ini — yang dibuat adalah fondasi manusia, data, dan kebijakan.

### Langkah-langkah

#### 🔑 Langkah 1: Bentuk Tim Inti (Minggu 1–2)
**Tujuan:** Pastikan ada orang yang bertanggung jawab penuh, bukan proyek "sampingan" semua orang.

| Peran | Siapa | Tanggung Jawab |
|---|---|---|
| **Product Owner** | WD II (Anda) | Keputusan fitur, prioritas, anggaran |
| **Project Manager** | Tendik senior / staf IT terpercaya | Koordinasi harian, timeline, laporan |
| **Data Steward** | Admin fakultas / kepala TU | Kualitas & kelengkapan master data |
| **Tech Lead** | Developer internal / vendor terpilih | Arsitektur sistem, kualitas kode |
| **Change Agent** | 1 perwakilan per unit/departemen | Sosialisasi, feedback lapangan, adopsi |

> ⚠️ **Peringatan:** Jangan delegasikan seluruhnya ke vendor. Harus ada orang internal yang paham sistem ini dari dalam.

---

#### 🔑 Langkah 2: Audit Infrastruktur Digital FSM (Minggu 1–3)
**Tujuan:** Tahu kondisi nyata sebelum berjanji ke stakeholder.

Checklist yang harus dijawab:
- [ ] Berapa bandwidth WiFi gedung-gedung utama FSM? Stabil?
- [ ] Ada server/hosting kampus yang bisa dipakai? Atau harus cloud?
- [ ] SSO UNDIP — apakah FSM bisa integrasi? Siapa kontaknya di IT pusat?
- [ ] API SIAP/SIAK — terbuka atau tertutup? Perlu MOU khusus?
- [ ] Ada tim IT di FSM atau semua bergantung ke IT pusat UNDIP?
- [ ] Berapa anggaran teknologi FSM per tahun saat ini?

**Output:** Dokumen "Infrastructure Readiness Report" — 1 halaman, jujur, realistis.

---

#### 🔑 Langkah 3: Stakeholder Alignment & Kick-off (Minggu 2–3)
**Tujuan:** Semua pihak tahu proyek ini ada, tujuannya apa, dan apa yang diminta dari mereka.

**Agenda rapat kick-off (2 jam):**
1. WD II presentasi visi super apps (15 menit)
2. Demo prototype/mockup awal — gunakan Figma atau bahkan PowerPoint (20 menit)
3. Sesi tanya jawab terbuka (30 menit)
4. Pembagian peran & tanggung jawab awal (20 menit)
5. Komitmen data steward per unit (15 menit)
6. Jadwal selanjutnya (10 menit)

**Peserta wajib:** Dekan, semua WD, semua Kaprodi, Kepala TU, perwakilan laboran, perwakilan teknisi, perwakilan mahasiswa (BEM/Himpunan).

> 💡 **Tips:** Tunjukkan 1 pain point nyata yang akan langsung terselesaikan — misalnya "lapor kerusakan tanpa perlu cari nomor WA teknisi." Ini lebih meyakinkan dari slide visi yang indah.

---

#### 🔑 Langkah 4: Data Sprint — Bersihkan & Strukturkan Data (Minggu 3–8)
**Tujuan:** Sistem tidak berguna jika datanya kosong atau salah.

| Sprint | Fokus | Output |
|---|---|---|
| Data Sprint 1 (Minggu 3–4) | Master data ruangan & gedung | List 100% ruang FSM: nama standar, kapasitas, fasilitas, lokasi |
| Data Sprint 2 (Minggu 4–5) | Master data pengguna | Import dari SSO: dosen, tendik, laboran, teknisi dengan role |
| Data Sprint 3 (Minggu 5–6) | Master data aset prioritas | QR + digitalisasi aset nilai > Rp 5 juta di lab aktif |
| Data Sprint 4 (Minggu 7–8) | SOP & kebijakan digital | Aturan booking, SLA ticketing, kategori kerusakan — tertulis resmi |

**Rekrut mahasiswa KKN-T / magang** untuk Data Sprint 2 & 3 — efektif dan hemat biaya.

---

#### 🔑 Langkah 5: Pilih Pendekatan Teknologi (Minggu 2–4)
**Tujuan:** Keputusan teknologi yang tepat = tidak rebuild 2 tahun lagi.

**3 Opsi Pendekatan:**

| Opsi | Deskripsi | Cocok Untuk | Estimasi Biaya |
|---|---|---|---|
| **A. Build Custom** | Developer bangun dari nol (internal/vendor) | Fleksibilitas tinggi, integrasi sempurna | Rp 150–500 juta |
| **B. Modifikasi Open Source** | Gunakan GLPI (ticketing) + Snipe-IT (aset) + custom booking | Hemat biaya, komunitas aktif | Rp 30–100 juta (setup + kustomisasi) |
| **C. Platform No-Code + Custom Layer** | Kombinasi tools SaaS + custom API layer | Cepat launch, fitur terbatas | Rp 20–60 juta/tahun |

**Rekomendasi untuk FSM:** Opsi B untuk fase pertama (open source), dengan rencana migrasi ke Opsi A setelah data dan kebutuhan sudah mature. Ini meminimalkan risiko investasi awal yang besar di sistem yang belum terbukti cocok.

**Stack teknologi yang disarankan (jika build custom):**
```
Frontend  : React / Next.js (web-app, mobile-responsive)
Backend   : Node.js atau Laravel (familiar di komunitas developer Semarang)
Database  : PostgreSQL (robust, open source, free)
Notifikasi: WhatsApp via Fonnte/WA Business API + Firebase Push
Auth      : SSO UNDIP (OAuth2) + fallback local auth
Hosting   : VPS Biznet/Jagoan Hosting (lokal, latency rendah)
Storage   : S3-compatible (Wasabi atau Backblaze — murah)
```

---

## 🚀 FASE 1 — Launch MVP (Bulan 3–6)
### "Ship something real, fast"

### Urutan Launch Modul (Berdasarkan RICE Score Gabungan)

```
Bulan 3:  🏫 Room & Lab Booking (Basic) ← Paling mudah & impak visual tinggi
Bulan 4:  🔧 Maintenance Ticketing (Basic) ← Pain point paling terasa
Bulan 5:  📦 Asset Management (Basic) ← Butuh data sprint dulu
Bulan 6:  ✅ Task Management (Basic) ← Paling bergantung pada adopsi manusia
```

**Mengapa urutan ini?**
- Booking room = demo yang indah untuk semua stakeholder → membangun momentum
- Ticketing = hasil yang cepat dirasakan (keluhan tertangani lebih cepat)
- Asset management = butuh data lengkap dulu, jadi dipersiapkan selama fase 1
- Task management = paling butuh perubahan budaya, diberi waktu paling banyak

### Definisi "MVP yang Cukup" per Modul
| Modul | Cukup Launch Jika... |
|---|---|
| Room Booking | Bisa booking, ada kalender, ada approval, ada notifikasi WA |
| Ticketing | Bisa lapor, ada foto, ada status, notifikasi ke teknisi & pelapor |
| Asset Mgmt | QR bisa di-scan, data bisa dicari, status bisa diupdate |
| Task Mgmt | Bisa buat task, ada PIC, ada deadline, ada progress update |

> 🚫 **Jangan tunggu sempurna.** Launch dengan 80% fitur berjalan baik lebih baik dari 100% fitur tapi mundur 6 bulan.

---

## 📈 FASE 2 — Stabilisasi & Adopsi (Bulan 7–9)
### "Bukan fitur baru — tapi pastikan yang ada benar-benar dipakai"

### Program Adopsi

#### 🎯 FSM Digital Challenge (Bulan 7)
Kompetisi antar departemen: departemen mana yang tingkat adopsi sistemnya paling tinggi dalam 30 hari? Hadiah: plakat + budget kegiatan departemen.

#### 📊 Weekly KPI Review (Rutin setiap Jumat)
WD II review dashboard 15 menit:
- Jumlah tiket masuk & selesai minggu ini
- Ruang dengan booking tertinggi
- Staf dengan task completion rate tertinggi
- Alert: ada modul yang tidak dipakai?

#### 🎓 Pelatihan Bertingkat
| Target | Format | Durasi |
|---|---|---|
| Admin & laboran | Workshop hands-on | 4 jam |
| Dosen | Demo + panduan 1 halaman | 30 menit |
| Mahasiswa | Video tutorial + infografis WA | Self-service |
| Teknisi | On-the-job training langsung | 2 jam |
| Pimpinan | Dashboard briefing | 1 jam |

#### 📝 Feedback Loop (Bulanan)
- Form feedback singkat (5 pertanyaan) via Google Form + link di WhatsApp
- FGD mini per unit setiap bulan ke-2, ke-4, ke-6
- Hasil feedback masuk ke backlog fitur secara transparan

---

## ⚡ FASE 3 — Penguatan Integrasi (Bulan 10–12)
### "Jadikan semua modul berbicara satu sama lain"

| Integrasi | Manfaat | Kompleksitas |
|---|---|---|
| Ticketing → Task Management | Tiket approved = task teknisi otomatis terbuat | 🟡 Sedang |
| Asset Mgmt → Ticketing | Aset rusak dari tiket = status aset otomatis berubah | 🟡 Sedang |
| Room Booking → Ticketing | Laporan kerusakan ruang = block otomatis di booking | 🟢 Mudah |
| Task Mgmt → Semua modul | Semua kegiatan punya task terlampir | 🔴 Kompleks |
| Semua modul → Dashboard WD II | Satu layar untuk semua KPI operasional FSM | 🟡 Sedang |

**Target akhir Fase 3:** WD II bisa membuka satu halaman dashboard dan melihat:
- Berapa tiket pending hari ini
- Ruang mana yang underutilized minggu ini
- Aset mana yang hampir habis masa pakainya
- Staf mana yang overload task
- Semua dalam < 5 detik loading

---

## 🔬 FASE 4 — Advanced Features (Bulan 13–18)

Prioritas Advanced features berdasarkan RICE score gabungan semua modul:

| Prioritas | Fitur | Modul | Alasan |
|---|---|---|---|
| #1 | Auto conflict detection booking | Room Booking | Impact besar, effort rendah |
| #2 | SLA auto response time | Ticketing | Langsung terasa oleh semua pengguna |
| #3 | Escalation otomatis task terlambat | Task Mgmt | Disiplin tanpa konfrontasi manusia |
| #4 | Prioritas urgensi tiket otomatis | Ticketing | Teknisi lebih efisien |
| #5 | Audit aset mobile scan | Asset Mgmt | Hemat waktu audit tahunan |
| #6 | Reminder kalibrasi alat lab | Asset Mgmt | Compliance standar lab |
| #7 | Integrasi jadwal SIAP/SIAK | Room Booking | Eliminasi double booking kuliah |
| #8 | KPI dashboard per unit | Task Mgmt | Data evaluasi SDM objektif |
| #9 | Kanban/Gantt board | Task Mgmt | Visibilitas proyek yang lebih baik |
| #10 | Preventive maintenance schedule | Ticketing | Dari reaktif ke proaktif |

---

## 🤖 FASE 5 — Premium & AI/IoT (Bulan 19–24+)

**Prasyarat sebelum masuk fase ini:**
- [ ] Minimal 12 bulan data histori dari semua modul
- [ ] Adopsi pengguna > 75% dari total target
- [ ] Tim IT internal atau vendor yang reliable sudah terbentuk
- [ ] Anggaran khusus infrastruktur AI/IoT sudah disetujui

| Fitur Premium | Prasyarat Spesifik | Estimasi Biaya Tambahan |
|---|---|---|
| AI deteksi kategori kerusakan dari foto | Dataset 1.000+ foto berlabel | Rp 20–50 juta (model training + API) |
| Prediksi fasilitas rusak | 2+ tahun data histori tiket + usia aset | Rp 30–80 juta |
| Sensor IoT monitoring AC/listrik | Hardware + instalasi per titik | Rp 5–15 juta/ruangan |
| AI task prioritization | 6+ bulan data task pattern per staf | Rp 15–40 juta |
| Smart room recommendation | 12+ bulan data booking pattern | Rp 10–25 juta |
| Face recognition check-in | Kamera khusus + server GPU | Rp 50–150 juta |

> 💡 **Strategi Premium:** Ajukan 1–2 fitur premium sebagai proyek penelitian dosen dengan dana DIPA/riset — double benefit: produk jadi + publikasi ilmiah.

---

## 💰 Estimasi Anggaran

### Biaya Pengembangan (One-time)

| Item | Opsi Hemat (Open Source) | Opsi Custom Build |
|---|---|---|
| Setup & konfigurasi sistem | Rp 20–40 juta | Rp 100–200 juta |
| Kustomisasi UI/UX | Rp 10–20 juta | Termasuk di atas |
| Integrasi SSO UNDIP | Rp 5–15 juta | Rp 10–20 juta |
| Pengadaan hardware (server/label printer) | Rp 15–30 juta | Rp 15–30 juta |
| Pelatihan & onboarding | Rp 5–10 juta | Rp 10–20 juta |
| **Total Estimasi** | **Rp 55–115 juta** | **Rp 135–270 juta** |

### Biaya Operasional (Per Tahun)

| Item | Estimasi |
|---|---|
| Hosting & domain | Rp 10–20 juta/tahun |
| WhatsApp API (notifikasi) | Rp 5–15 juta/tahun |
| Maintenance & bug fix | Rp 20–40 juta/tahun |
| Pelatihan pengguna baru | Rp 5–10 juta/tahun |
| **Total Per Tahun** | **Rp 40–85 juta/tahun** |

### Sumber Pendanaan yang Bisa Dikejar
| Sumber | Potensi | Langkah |
|---|---|---|
| DIPA UNDIP (anggaran IT fakultas) | Rp 50–150 juta | Proposal ke WR II UNDIP |
| Hibah DIKTI (digitalisasi PT) | Rp 200–500 juta | Submit ke program PD-DIKTI |
| Dana PNBP Fakultas | Rp 30–100 juta | Usulan RKAKL tahunan |
| Kerjasama industri (CSR teknologi) | Rp 50–200 juta | Pendekatan ke perusahaan tech lokal Semarang |
| TA/Skripsi mahasiswa (labour cost) | Non-finansial | Rekrut mahasiswa informatika/ilkom |

---

## 🔒 Strategi Keberlanjutan (Sustain Strategy)

### Masalah: "Proyek mati saat WD II berganti"
Ini adalah ancaman terbesar. Berikut mitigasinya:

#### 1. Institusionalisasi — Jadikan Peraturan Resmi
- Buat **SK Dekan** tentang penggunaan sistem digital FSM
- Masukkan ke **SOP resmi** Tata Usaha & masing-masing unit
- Jadikan sistem sebagai **syarat adminstrasi** (contoh: booking lab hanya bisa via sistem)

#### 2. Knowledge Transfer — Jangan Silo di Satu Orang
- Dokumentasi teknis wajib tersimpan di repositori resmi (GitHub FSM)
- Minimal 2 orang internal yang memahami sistem secara teknis
- Video tutorial setiap fitur disimpan di Google Drive FSM

#### 3. Governance — Siapa yang Jaga Setelah Kamu?
```
Struktur Governance yang Direkomendasikan:
┌─────────────────────────────────────────┐
│  Steering Committee (WD II, WD I, Dekan)│ ← Keputusan strategis
├─────────────────────────────────────────┤
│  Product Owner (Staf IT / tendik senior)│ ← Keputusan produk harian
├─────────────────────────────────────────┤
│  Tech Maintainer (Developer)            │ ← Operasional teknis
├─────────────────────────────────────────┤
│  Data Stewards (per unit)               │ ← Kualitas data per departemen
└─────────────────────────────────────────┘
```

#### 4. Financial Sustainability
- Anggaran maintenance masuk RKAKL tahunan sebagai **line item tetap**
- Tidak bergantung pada 1 vendor — source code harus dimiliki FSM

---

## 📐 Strategi Scalability (Scalable Strategy)

### Arsitektur yang Mendukung Pertumbuhan

**Prinsip desain teknis wajib:**

| Prinsip | Implementasi |
|---|---|
| **API-first** | Semua fitur dibangun sebagai API — mudah diintegrasikan dengan sistem lain |
| **Modular** | Setiap modul bisa di-deploy dan di-update independen |
| **Stateless** | Server tidak menyimpan session — mudah di-scale horizontal |
| **Mobile-first** | Desain untuk layar HP dulu, baru desktop |
| **Progressive Enhancement** | Fitur dasar jalan di koneksi lambat, fitur premium butuh koneksi baik |

**Checkpoint Scalability:**
- 100 pengguna → shared VPS (Rp 200–500 ribu/bulan)
- 1.000 pengguna → dedicated VPS atau container (Rp 500 ribu–2 juta/bulan)
- 5.000+ pengguna → cloud auto-scaling (Rp 2–5 juta/bulan)

---

## 🪶 Strategi Lightweight (Lightweight Strategy)

### Target Performa
| Metrik | Target |
|---|---|
| Waktu load halaman utama | < 2 detik di WiFi kampus |
| Ukuran download per halaman | < 500 KB |
| Notifikasi terkirim | < 30 detik setelah event |
| Uptime sistem | > 99% (≤ 7 jam downtime/tahun) |
| Akses tanpa install app | ✅ Web-app, bukan native app |

### Taktik Lightweight
1. **Progressive Web App (PWA)** — bisa "diinstall" dari browser, ukuran kecil, bisa offline
2. **Lazy loading** — hanya load data yang terlihat di layar, bukan semua data sekaligus
3. **Image compression otomatis** — foto kerusakan yang diupload otomatis dikompres
4. **Cache cerdas** — data yang sering diakses disimpan lokal (daftar ruangan, dll)
5. **WhatsApp sebagai primary channel** — tidak perlu install app, semua orang sudah punya WA

---

## 🎯 Quick Wins — 30 Hari Pertama

Ini yang paling penting untuk membangun kepercayaan semua pihak:

| Hari | Action | Dampak |
|---|---|---|
| Hari 1–3 | Bentuk tim inti, buat grup WA khusus proyek | Sinyal serius dari WD II |
| Hari 4–7 | Audit kondisi WiFi & server kampus | Basis keputusan teknis |
| Hari 8–14 | Kick-off meeting semua stakeholder | Alignment & komitmen |
| Hari 15–21 | Data sprint: daftar semua ruangan FSM | Master data pertama siap |
| Hari 22–25 | Pilot booking room manual via Google Form | Uji konsep tanpa sistem |
| Hari 26–30 | Presentasi progress ke Dekan | Laporan ke pimpinan = signal sustain |

> Hari ke-30: Kamu harus bisa menjawab "Apakah proyek ini akan lanjut?" dengan YA yang didukung data.

---

## ⚠️ 10 Jebakan yang Harus Dihindari WD II

| # | Jebakan | Solusinya |
|---|---|---|
| 1 | Ingin semua fitur di versi 1 | Definisikan MVP ketat, launch bertahap |
| 2 | Terlalu bergantung pada 1 vendor | Source code harus milik FSM, multi-vendor |
| 3 | Tidak ada champion di level teknis | Rekrut/tunjuk staf IT internal yang accountable |
| 4 | Lupa sosialisasi ke pengguna akhir | Change management = 40% dari proyek |
| 5 | Data buruk di awal sistem | Data sprint sebelum launch, bukan setelah |
| 6 | Tidak punya metrik keberhasilan | Tentukan KPI: tingkat adopsi, jumlah tiket, utilisasi ruang |
| 7 | Proyek hidup hanya dari semangat | Masukkan ke RKAKL, buat SK resmi |
| 8 | Teknisi/laboran tidak dilibatkan | Mereka ujung tombak — libatkan dari desain awal |
| 9 | Tidak ada feedback loop | Review bulanan wajib, backlog transparan |
| 10 | Berpikir "nanti diurus IT pusat UNDIP" | Bangun otonomi FSM, integrasikan bukan bergantung |

---

## 📊 KPI Keberhasilan Super Apps FSM

### KPI Adopsi (Tahun 1)
| Metrik | Target 6 Bulan | Target 12 Bulan |
|---|---|---|
| % pengguna aktif bulanan | > 40% | > 70% |
| Tiket masuk via sistem (vs manual) | > 60% | > 90% |
| Booking ruang via sistem (vs manual) | > 70% | > 95% |
| Aset terdigitalisasi | > 50% | > 80% |
| Task terdokumentasi digital | > 50% | > 75% |

### KPI Dampak Operasional (Tahun 1–2)
| Metrik | Baseline (Perkiraan) | Target |
|---|---|---|
| Waktu respons kerusakan rata-rata | 3–7 hari | < 1 hari |
| Aset tidak terlacak | ~15–20% | < 5% |
| Konflik booking ruang per bulan | ~10–20 kejadian | < 2 kejadian |
| Task overdue tanpa eskalasi | ~30–40% | < 10% |

---

## 🧩 Langkah Konkret Minggu Ini untuk WD II

Jika Anda membaca dokumen ini hari ini, ini yang harus dilakukan minggu ini:

1. **[ ] Identifikasi 1 orang Project Manager internal** — bukan Anda, tapi orang yang Anda percaya
2. **[ ] Buat grup WA "FSM Digital Hub"** — isi dengan PM, kepala TU, 1 laboran, 1 teknisi
3. **[ ] Booking jadwal rapat audit WiFi & server** — dengan IT pusat UNDIP atau tim teknis
4. **[ ] Cek RKAKL tahun ini** — ada anggaran teknologi yang bisa dialihkan?
5. **[ ] Hubungi 1 kaprodi yang paling pro-digital** — jadikan departemen pilot pertama

> **Ingat:** Proyek terbesar dimulai dari satu langkah kecil yang konsisten, bukan dari rencana yang sempurna.

---

## 🔗 Navigasi Dokumen Lengkap

| File | Konten |
|---|---|
| [`00-overview.md`](./00-overview.md) | Gambaran umum, semua pengguna, master feature matrix |
| [`01-maintenance-ticketing.md`](./01-maintenance-ticketing.md) | SWOT + RACI + Data Readiness + FMEA + RICE — Ticketing |
| [`02-asset-management.md`](./02-asset-management.md) | SWOT + RACI + Data Readiness + FMEA + RICE — Asset |
| [`03-room-lab-booking.md`](./03-room-lab-booking.md) | SWOT + RACI + Data Readiness + FMEA + RICE — Booking |
| [`04-task-management.md`](./04-task-management.md) | SWOT + RACI + Data Readiness + FMEA + RICE — Task |
| [`05-roadmap-next-steps.md`](./05-roadmap-next-steps.md) | Dokumen ini — roadmap strategis WD II |

---

*"A vision without execution is just a hallucination." — Mulai dari fondasi yang kuat, bukan dari fitur yang keren.*

*Dokumen ini adalah living document — perbarui setiap kuartal seiring perkembangan proyek.*
