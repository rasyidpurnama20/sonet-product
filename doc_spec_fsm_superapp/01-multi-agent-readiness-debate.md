# 🛡️ Debat Multi-Agen Berdaulat — Uji Kesiapan FSM Super Apps

> **Jenis Dokumen:** Strategic Readiness Review via Adversarial Multi-Agent Debate
> **Tujuan:** Menguji asumsi proyek dari berbagai sudut pandang sebelum kickoff RAD
> **Output:** Putusan kerja (working consensus) + daftar disensus yang harus diselesaikan
> **Versi:** 0.1 — Mei 2026

---

## 🎭 Protokol Debat

1. **Setiap agen berdaulat** — punya mandat, bias, dan kepentingan sendiri. Boleh menyerang, boleh mendukung, **tidak boleh berkompromi tanpa argumen**.
2. **Argumen harus konkret** — referensi ke angka FSM (populasi, jumlah lab, dst) atau realita operasional. Pernyataan generik akan ditandai `[GENERIK]` oleh agen lain.
3. **Setiap ronde** ditutup dengan: posisi tiap agen + skor dukungan/serangan antar-agen.
4. **Konsensus** hanya tercatat jika **minimal 4 dari 5 agen** menyetujui. Sisanya masuk **Disensus** untuk eskalasi ke Project Sponsor.

### Konteks Faktual (acuan semua agen)
| Variabel | Angka |
|---|---|
| Mahasiswa | 3.500–4.500 |
| Dosen | 200–300 |
| Tendik | 80–120 |
| Laboran | 30–60 |
| Prodi | 7–10 |
| Gedung | 15–25 |
| Lab | 40–80 |
| **Estimasi tiket bulanan** (5–10% populasi) | **~200–450 tiket/bulan** |
| **Rasio laboran:lab** | **1 : 1,3–1,5** (laboran kewalahan kelola aset multi-lab) |

---

## 👥 Cast of Agents

| Agen | Mandat | Bias yang Diakui |
|---|---|---|
| 🧭 **VISIONER** | Strategi produk jangka 3 tahun, platform play | Cenderung over-engineer, suka "ekosistem" |
| 🔧 **LAPANGAN** | Suara tendik/laboran/teknisi harian | Anti-fitur cantik, hanya percaya yang dipakai besok |
| 🏗️ **ARSITEK** | Kelayakan teknis, biaya, technical debt | Konservatif, membela kemudahan ops |
| 🪖 **POLITIK** | Adopsi, change management, kepentingan pimpinan | Pesimis terhadap inisiatif top-down |
| 🗡️ **OPOSISI** | Devil's advocate — mencari titik gagal proyek | Tidak punya solusi, hanya menyerang |

---

## 🥊 RONDE 1 — Diagnosis: Apa Masalah Sebenarnya?

### 🧭 VISIONER membuka
> "FSM belum punya **single source of truth** untuk fasilitas. Empat modul ini sebenarnya satu masalah: **data fasilitas yang tersebar di kepala orang, bukan di sistem**. Maintenance, aset, booking, task — semuanya gagal scale karena master data tidak ada."

### 🔧 LAPANGAN menyerang
> "[SETENGAH-GENERIK] `single source of truth` itu jargon. Masalah real saya: **AC bocor di Lab Kimia 3 lapor jam 8, jam 4 sore belum ada yang datang, dosen ngamuk di WA grup**. Saya tidak butuh ontologi data, saya butuh tiket sampai ke teknisi yang benar dalam 30 menit. Kalau visi Anda tidak menyelesaikan itu di minggu pertama, proyek ini akan dilupakan."

### 🪖 POLITIK mendukung LAPANGAN
> "Setuju. Dengan 80–120 tendik dan 30–60 laboran, **tidak ada satu pun yang ditambah staf-nya untuk pakai aplikasi baru**. Kalau aplikasi menambah beban kerja >10 menit/hari per orang, mereka akan sabotase pasif: tetap pakai WA, fitur app dibiarkan kosong. Diagnosis VISIONER benar tapi **urutan implementasinya akan membunuh proyek**."

### 🏗️ ARSITEK semi-mendukung VISIONER
> "VISIONER benar pada level data. Dengan **40–80 lab × ribuan aset**, tanpa registry digital yang dipakai dari hari pertama, modul ticketing pun akan gagal — karena tiket tidak bisa dikaitkan ke aset spesifik. Tapi LAPANGAN juga benar bahwa user tidak peduli arsitektur. **Solusi: bangun registry minimum bersamaan dengan ticketing, bukan sebelum**."

### 🗡️ OPOSISI menyerang semua
> "Empat agen ini berdebat seolah masalahnya teknis. Masalah sebenarnya: **FSM belum membuktikan WD II akan tetap menjabat selama 6 bulan ke depan**. Kalau ganti pimpinan, proyek mati. Diagnosis kalian semua **mengabaikan risiko institusional nomor satu**. Tunjukkan SK proyek dulu, baru kita bicara modul."

### 📊 Posisi Akhir Ronde 1
| Agen | Posisi | Setuju dgn | Menyerang |
|---|---|---|---|
| VISIONER | Data adalah masalah inti | ARSITEK (parsial) | LAPANGAN |
| LAPANGAN | Time-to-resolve adalah masalah inti | POLITIK | VISIONER |
| ARSITEK | Keduanya benar; bangun paralel | VISIONER, LAPANGAN | — |
| POLITIK | Beban kerja tambahan = bunuh proyek | LAPANGAN | VISIONER |
| OPOSISI | Risiko institusional > risiko teknis | (sendirian) | semua |

### ✅ Konsensus Ronde 1 (4/5)
**Masalah inti FSM bersifat ganda dan harus diselesaikan paralel:**
1. **Data fasilitas tidak terkelola** (mendukung modul Aset & Booking)
2. **Resolusi keluhan terlalu lambat & tidak transparan** (mendukung modul Ticketing)

OPOSISI tidak setuju — risiko institusional belum dijawab. **Disensus #1 dibuka**.

---

## 🥊 RONDE 2 — Prioritas Modul: Mana yang Pertama?

### 🧭 VISIONER mengusulkan
> "**Asset Management dulu**. Tanpa registry aset, ticketing tidak bisa kategorisasi, booking tidak bisa validasi, task tidak punya konteks. Bangun fondasi dulu, baru permukaan."

### 🔧 LAPANGAN menyerang frontal
> "Salah total. Kalau Anda kasih saya **app aset kosong yang harus saya isi 8.000 baris** sebelum ada manfaatnya, saya tidak akan sentuh. **Ticketing dulu**. Mahasiswa lapor → muncul aset baru di registry → registry tumbuh organik. Top-down population = mati. Bottom-up via tiket = hidup."

### 🪖 POLITIK mendukung LAPANGAN dengan twist
> "Setuju ticketing dulu, tapi alasannya politis: **3.500–4.500 mahasiswa adalah konstituen terbesar**. Kalau MVP terlihat oleh mereka di minggu pertama, dukungan publik mengamankan proyek dari OPOSISI-nya OPOSISI (= ganti pimpinan). Aset & booking adalah modul *back-office*, tidak menghasilkan legitimasi politik."

### 🏗️ ARSITEK kompromi
> "Saya menengahi: **Ticketing-first dengan asset-stub**. Modul ticketing diluncurkan duluan, tapi setiap tiket WAJIB punya field `lokasi` dan `kategori aset` (free text di awal). Setelah 2 bulan, kita punya ~400–900 tiket — itu sample data untuk *seed* registry aset secara semi-otomatis. **Asset Management proper jadi modul ke-2, bukan ke-1.**"

### 🗡️ OPOSISI menyerang LAPANGAN
> "Anda terlalu romantis dengan 'data tumbuh organik'. **Tiket tanpa registry → kategorisasi sampah → laporan sampah → pimpinan kehilangan kepercayaan di bulan ke-3**. Anda menyiapkan kegagalan terlihat."

### 🔧 LAPANGAN balas
> "Lebih baik sampah yang dipakai daripada registry rapi yang kosong. Kategorisasi bisa di-cleanup di iterasi 2. **Sampah berarti app dipakai. Kosong berarti app mati**."

### 🧭 VISIONER mundur sebagian
> "Saya menerima Ticketing-first **dengan syarat**: (1) field aset wajib terstruktur (dropdown, bukan free text murni), (2) sprint paralel untuk Asset Management dimulai bulan ke-2, tidak boleh ditunda."

### 📊 Posisi Akhir Ronde 2
| Modul | Iterasi 1 (MVP) | Iterasi 2 (Bln 3-4) | Iterasi 3 (Bln 5-6) | Iterasi 4 |
|---|---|---|---|---|
| **Maintenance Ticketing** | ✅ Full BASIC | ➕ ADVANCED | — | — |
| **Asset Management** | ⚠️ Stub (registry minimum) | ✅ Full BASIC | ➕ ADVANCED | — |
| **Room/Lab Booking** | ❌ | ⚠️ Pilot 1 prodi | ✅ Full BASIC | ➕ ADVANCED |
| **Task Management** | ❌ | ❌ | ⚠️ Pilot internal IT | ✅ Full BASIC |

### ✅ Konsensus Ronde 2 (5/5)
**Urutan: Ticketing → Asset → Booking → Task**, dengan asset-stub berjalan paralel sejak iterasi 1.

> Alasan Booking baru iterasi 3: dengan **40–80 lab × 7–10 prodi**, konflik kepemilikan jadwal lab adalah **politik berat**. Tunggu sampai sistem punya kredibilitas dari modul ticketing dulu, baru sentuh booking.

---

## 🥊 RONDE 3 — Quick Wins: Apa yang Harus Terlihat di Minggu Pertama?

### 🔧 LAPANGAN memimpin
> "Tiga quick wins, tidak boleh kurang:
> 1. **QR code di setiap pintu ruangan/lab** → scan → form lapor (tidak perlu install app)
> 2. **WhatsApp Bot** untuk lapor kerusakan (segmen mahasiswa & dosen yang anti-app)
> 3. **Status tracking publik** dengan link unik per tiket (mahasiswa bisa cek tanpa login)"

### 🧭 VISIONER menambah
> "Tambah satu: **dashboard publik FSM** yang menampilkan `X tiket selesai bulan ini, rata-rata waktu Y jam`. Itu bukan hanya quick win, itu **alat legitimasi politik untuk WD II**."

### 🪖 POLITIK setuju keras
> "Dashboard publik VISIONER adalah **MVP politik**. Saya akan tambahkan: launching event di acara apel/rapat fakultas — bukan email diam-diam. Visibility = legitimacy."

### 🏗️ ARSITEK menyerang QR + WA
> "QR code 15–25 gedung × ~10–20 ruang/gedung = **150–500 stiker QR**. Siapa yang cetak, tempel, dan **maintain saat stiker rusak/copot**? Ini bukan quick win, ini **operational debt**. Solusi: QR generic per gedung dulu (15–25 stiker), bukan per ruangan. User pilih ruangan dari dropdown."

### 🔧 LAPANGAN menerima sebagian
> "OK. Fase 1: QR per gedung. Fase 2 (jika modul aset sudah jalan): QR per aset (otomatis dari registry, dicetak saat aset diregister). Tidak perlu QR per ruangan."

### 🗡️ OPOSISI menyerang dashboard publik
> "Dashboard publik di bulan pertama akan menampilkan **angka jelek** — tiket numpuk, response time lambat, karena tim belum stabil. Anda **memamerkan kegagalan**. Tunda dashboard sampai bulan ke-3 minimum."

### 🧭 VISIONER balas
> "Justru sebaliknya. **Tampilkan baseline buruk di awal**, lalu tampilkan tren membaik. Itu storyline yang lebih kuat daripada angka bagus tanpa konteks. Tapi saya setuju: dashboard hanya untuk internal di bulan 1, publik di bulan 2."

### ✅ Konsensus Ronde 3 (4/5)
**Quick wins MVP (terlihat di minggu 1–4 pasca go-live):**
| # | Quick Win | Justifikasi Spesifik FSM |
|---|---|---|
| 1 | **WhatsApp Bot lapor kerusakan** | Penetrasi WA ~100% di 3.500–4.500 mahasiswa; nol friction install |
| 2 | **QR per gedung** (15–25 stiker) | Manageable secara operasional, scope realistis |
| 3 | **Status tracking via link unik** (no-login) | Mahasiswa cek tiket tanpa akun |
| 4 | **Dashboard internal pimpinan** (publik di bulan 2) | Senjata legitimasi untuk WD II di rapat pimpinan |
| 5 | **SLA visible** di setiap tiket (`target selesai: 2x24 jam`) | Tekanan sosial > tekanan struktural |

OPOSISI tetap tidak setuju soal dashboard publik bulan 2. **Disensus #2 dibuka**.

---

## 🥊 RONDE 4 — Risiko Adopsi: Apa yang Akan Membunuh Proyek?

### 🪖 POLITIK memetakan 5 risiko teratas spesifik FSM
| # | Risiko | Mengapa Spesifik FSM? |
|---|---|---|
| 1 | **WA Grup tetap dipakai paralel** | Sudah jadi *muscle memory* 3.500+ mahasiswa & 200+ dosen |
| 2 | **30–60 laboran tidak input data aset** | Mereka tidak ada KPI input data, hanya KPI lab beroperasi |
| 3 | **Konflik prodi soal jadwal lab** (saat Booking diluncurkan) | 7–10 prodi rebutan 40–80 lab tanpa rule politis yang jelas |
| 4 | **Pergantian WD II / Dekan** | Siklus jabatan kampus 4 tahun; sponsor hilang = proyek mati |
| 5 | **Tiket "selesai" dipalsukan oleh teknisi** | Tanpa verifikasi pelapor, teknisi cenderung tutup tiket cepat |

### 🔧 LAPANGAN memberi mitigasi konkret per risiko
> 1. **WA tetap dipakai → buatkan WA Bot resmi**, jadi WA-nya yang masuk ke sistem. Jangan lawan WA, kuasai WA.
> 2. **Laboran tidak input → fitur input ultra-cepat** (foto + auto-OCR label aset → 80% field terisi otomatis). Target <30 detik per aset.
> 3. **Konflik prodi → jangan launching booking sebelum ada SK aturan prioritas dari Dekan**. Aplikasi tidak menyelesaikan masalah governance.
> 4. **Pergantian pimpinan → institusionalisasi via SK proyek + dokumentasi handover**. Bukan tugas tim dev tapi tugas Project Sponsor.
> 5. **Tiket palsu selesai → wajib konfirmasi pelapor** (1 klik di link unik) sebelum tiket benar-benar closed. Tanpa konfirmasi 3x24 jam, auto-closed dengan flag *unverified*."

### 🏗️ ARSITEK memvalidasi mitigasi #2 secara teknis
> "OCR label aset feasible jika label punya format konsisten. Kalau aset existing belum berlabel standar, **OCR akan jadi promise yang tidak ditepati**. Realistis: bulan 1–2 input manual cepat (form 5 field), bulan 3 OCR untuk aset baru saja."

### 🗡️ OPOSISI menambah risiko keenam
> "Kalian lupa: **dosen senior**. 200–300 dosen, sekitar 20–30% di atas usia 55. Mereka tidak akan pakai app, tidak akan pakai WA bot, dan **mereka punya kekuatan politik untuk mengeluh ke Dekan**. Satu dosen senior yang vokal bisa membatalkan proyek dengan satu surat ke Dekan."

### 🪖 POLITIK menerima
> "Diterima. Mitigasi: **'admin proxy' untuk dosen senior** — ada tendik yang ditugaskan input atas nama mereka. Jangan paksa semua user menggunakan UI. Yang penting datanya masuk."

### ✅ Konsensus Ronde 4 (5/5)
**Top-6 Risiko Adopsi + Mitigasi Wajib MVP:**
1. WA tetap dipakai → **WA Bot resmi** (WAJIB di MVP)
2. Laboran tidak input → **input ultra-cepat <30 detik** (WAJIB di iterasi 2)
3. Konflik prodi soal lab → **SK aturan prioritas SEBELUM modul Booking dibangun** (BLOCKER iterasi 3)
4. Pergantian pimpinan → **SK proyek + dokumentasi handover** (tugas Sponsor, bukan tim dev)
5. Tiket palsu selesai → **konfirmasi pelapor 1-klik** (WAJIB di MVP)
6. Resistensi dosen senior → **admin proxy** (PIC: 1 tendik per prodi)

---

## 🥊 RONDE 5 — Klasifikasi Fitur BASIC / ADVANCED / PREMIUM

> **Definisi yang disepakati semua agen:**
> - **BASIC** = tanpa fitur ini, modul tidak bermanfaat. Wajib di MVP modul tersebut.
> - **ADVANCED** = mengubah modul dari fungsional → efisien. Iterasi setelah BASIC stabil.
> - **PREMIUM** = nilai tambah strategis, butuh investasi besar atau prasyarat eksternal.

### 🔧 Modul 1 — Maintenance Ticketing
| Tier | Fitur | Catatan Spesifik |
|---|---|---|
| **BASIC** | Form lapor + foto, kategori, lokasi, status tracking, WA notif, assignment manual oleh dispatcher, riwayat per pengguna, konfirmasi pelapor 1-klik | Untuk volume **200–450 tiket/bulan** masih manageable manual |
| **ADVANCED** | SLA timer per kategori, auto-routing berdasarkan kategori+gedung, knowledge base FAQ kerusakan umum, satisfaction rating, dashboard pimpinan | Mulai relevan saat tiket >500/bulan |
| **PREMIUM** | Predictive maintenance (ML pola AC/listrik/air rusak berulang), integrasi sensor IoT, mobile app teknisi offline-first, cost tracking per aset & per gedung | Butuh data history ≥12 bulan dulu |

### 🏗️ Modul 2 — Asset Management
| Tier | Fitur | Catatan Spesifik |
|---|---|---|
| **BASIC** | Registry digital, QR per aset, status & lokasi, mutasi/peminjaman, search, foto aset | Skala **~5.000–15.000 aset** estimasi dari 40–80 lab |
| **ADVANCED** | Penyusutan otomatis, jadwal kalibrasi, siklus audit tahunan, BAST digital, integrasi tiket↔aset, history maintenance per aset | Wajib sebelum audit BPK / SPI |
| **PREMIUM** | Integrasi BIM/CAD floorplan, IoT real-time tracking (geofencing), forecasting kondisi aset (ML), integrasi BMN/SIMAK Kemenkeu | Strategic, butuh anggaran terpisah |

### 🪖 Modul 3 — Room/Lab Booking
| Tier | Fitur | Catatan Spesifik |
|---|---|---|
| **BASIC** | Kalender per ruang/lab, form pengajuan, deteksi konflik, alur approval, notif WA/email, ICS export | **Prasyarat: SK aturan prioritas dari Dekan** |
| **ADVANCED** | Aturan prioritas otomatis per peran, booking berulang, kapasitas & kompatibilitas (lab kimia hanya untuk MK X), penalti no-show, blackout period | Mengatasi konflik **7–10 prodi rebut 40–80 lab** |
| **PREMIUM** | Smart suggestion ruang ideal, sensor okupansi (deteksi no-show otomatis), tarif eksternal dinamis (lab dipakai industri), integrasi smart lock | Monetisasi lab untuk pihak ke-3 |

### 🧭 Modul 4 — Task Management
| Tier | Fitur | Catatan Spesifik |
|---|---|---|
| **BASIC** | Daftar tugas, assignment, due date, status, komentar, attachment | Awalnya untuk tim IT/maintenance internal saja |
| **ADVANCED** | Dependensi antar-tugas, kanban view, time tracking, tugas berulang, template tugas | Saat tim ops sudah biasa dengan sistem |
| **PREMIUM** | Analitik beban kerja (workload heatmap), ringkasan AI mingguan untuk pimpinan, dashboard performa per unit, integrasi SKP/kinerja pegawai | Politis sensitif — butuh persetujuan kepegawaian |

### ✅ Konsensus Ronde 5 (5/5)
**Strategi rilis:** Setiap modul rilis dalam tier **BASIC** dulu. **ADVANCED** menyusul setelah modul tersebut digunakan minimal 8 minggu dengan adopsi terverifikasi. **PREMIUM** masuk roadmap tahun ke-2, butuh business case terpisah.

---

## 🏛️ Putusan Akhir (Working Consensus)

### 🎯 Empat Keputusan Strategis
1. **Urutan modul: Ticketing → Asset → Booking → Task** (Asset-stub paralel sejak iterasi 1).
2. **MVP wajib mencakup 5 mitigasi adopsi:** WA Bot, konfirmasi pelapor, QR per gedung, dashboard internal, SLA visible.
3. **Booking modul DI-BLOCK** sampai ada SK aturan prioritas lab dari Dekan.
4. **Setiap modul rilis BASIC dulu, ADVANCED menyusul setelah 8 minggu adopsi terverifikasi**, PREMIUM masuk roadmap tahun ke-2.

### 🚧 Disensus yang Harus Diselesaikan Project Sponsor
| # | Topik | Posisi Mayoritas | Posisi Minoritas (OPOSISI) | Eskalasi |
|---|---|---|---|---|
| 1 | Risiko institusional (pergantian pimpinan) | Mitigasi via SK proyek cukup | Tunda kickoff sampai SK turun | **WD II + Dekan** harus konfirmasi komitmen 12 bulan |
| 2 | Timing dashboard publik | Bulan ke-2 dengan baseline jelek | Bulan ke-3 setelah angka stabil | **WD II** memutuskan toleransi politis |

### 📋 Daftar Bukti yang Harus Disiapkan SEBELUM Kickoff Resmi
- [ ] **SK proyek FSM Super Apps** ditandatangani Dekan (mitigasi risiko #4)
- [ ] **Surat dukungan WD II** dengan komitmen waktu minimum 12 bulan
- [ ] **Daftar PIC tendik per prodi** untuk role *admin proxy* (mitigasi risiko dosen senior)
- [ ] **Data audit awal:** estimasi jumlah aset per lab (sample 5 lab) untuk validasi skala
- [ ] **Akses WhatsApp Business API** atau alternatif (prasyarat WA Bot)
- [ ] **Komitmen tim minimum 5 orang** dengan alokasi waktu jelas (lihat dokumen 00, bagian 5)

---

## 📝 Catatan untuk Project Manager

### 🚦 Sinyal Hijau untuk Kickoff
Lanjut ke Fase 1 RAD jika:
- ✅ Minimal **3 dari 6 bukti** di atas sudah ada
- ✅ Disensus #1 tertutup (komitmen sponsor 12 bulan dikonfirmasi)
- ✅ Tim minimum 5 orang teridentifikasi

### 🚦 Sinyal Kuning — Mulai dengan Risiko
Lanjut tapi siapkan rencana darurat jika:
- ⚠️ SK proyek belum ada tapi sponsor verbal kuat
- ⚠️ Tim hanya 3–4 orang (timeline akan molor 30–50%)

### 🚦 Sinyal Merah — Tunda Kickoff
Tunda jika:
- 🛑 SK proyek tidak akan turun dalam 4 minggu
- 🛑 WD II akan berakhir masa jabatan dalam <12 bulan tanpa kepastian penerus mendukung
- 🛑 Tidak ada akses WhatsApp Business API atau channel alternatif setara

---

## 🧾 Catatan Versi
| Versi | Tanggal | Penulis | Perubahan |
|---|---|---|---|
| 0.1 | Mei 2026 | Multi-Agent Debate Session #1 | Versi awal — 5 ronde debat selesai |

---

> 🗣️ **Dokumen ini sengaja menampilkan suara berbeda — bukan untuk menambah noise, tapi untuk memastikan keputusan kita lulus uji adversarial sebelum pengeluaran biaya pengembangan dimulai.**



---

# 🏗️ Bagian II — Rancangan Arsitektur FSM Super Apps

> **Prinsip:** Sederhana, scalable, tidak overengineered. Monolith modular dulu, microservice nanti (jika perlu). Stack umum, tools yang sudah dikenal tim lokal.

---

## A. Peta Modul (High-Level)

| # | Modul | Fungsi Inti | Tier MVP |
|---|---|---|---|
| M1 | **Maintenance Ticketing** | Lapor kerusakan → tracking → resolusi → konfirmasi | BASIC |
| M2 | **Asset Management** | Registry aset + QR + status + mutasi | Stub di MVP, BASIC iter-2 |
| M3 | **Room/Lab Booking** | Pengajuan & approval pemakaian ruang/lab | BASIC iter-3 |
| M4 | **Task Management** | Penugasan internal tim ops | BASIC iter-4 |
| **Core** | **Identity, Notification, File, Audit** | Layanan pendukung dipakai semua modul | Wajib MVP |

---

## B. Role Pengguna & Hak Akses

| Role | Modul yang Diakses | Aksi Utama | Estimasi Jumlah FSM |
|---|---|---|---|
| **Mahasiswa** | M1 (lapor), M3 (lihat jadwal) | Buat tiket, cek status, konfirmasi resolusi | 3.500–4.500 |
| **Dosen** | M1, M3 (request booking) | Lapor, ajukan booking lab/ruang | 200–300 |
| **Tendik (Admin Fakultas)** | M1, M2, M3 | Dispatch tiket, kelola booking, approve | 80–120 |
| **Laboran** | M1, M2 | Update kondisi aset, peminjaman aset | 30–60 |
| **Teknisi** | M1, M4 | Eksekusi tiket, update status | ~5–15 (subset tendik) |
| **Kepala Lab / Kaprodi** | M2, M3 | Approve booking, audit aset lab | 7–10 + 40–80 kepala lab |
| **Pimpinan (WD II, Dekan)** | Dashboard read-only | Lihat metrik & laporan | <10 |
| **Super Admin (IT FSM)** | Semua + konfigurasi | User mgmt, master data, audit log | 2–3 |

> **Auth model:** Role-Based Access Control (RBAC) dengan **6 role utama**. Hindari ABAC kompleks di MVP.

---

## C. Arsitektur Sistem (Layered View)

```
┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                      │
│  Web App (Next.js)   WA Bot   Email   Public Status URL │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              API GATEWAY (REST + JWT)                    │
│           Rate limit · Auth · Versioning                 │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  M1 Ticket   │◄──►│  M2 Asset    │    │  M3 Booking  │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │
       └─────┬─────────────┴───────────────────┘
             ▼
      ┌─────────────────────────────────────────┐
      │  CORE SERVICES (Identity · Notification │
      │  · File · Audit · Master Data)          │
      └─────────────────────────────────────────┘
             │
             ▼
      ┌─────────────────────────────────────────┐
      │  PostgreSQL (primary) + S3-compat       │
      │  (file) + Redis (cache & queue)         │
      └─────────────────────────────────────────┘
```

| Lapisan | Komponen | Justifikasi |
|---|---|---|
| **Presentation** | Next.js (web responsive), WA Bot, Email | Tidak ada native app di MVP — hemat biaya, jangkauan luas |
| **API Gateway** | NestJS atau Laravel (single backend monolith modular) | Monolith modular cukup untuk skala FSM, hindari microservice premature |
| **Modul** | M1, M2, M3, M4 sebagai *bounded context* di dalam monolith | Pisah folder & schema, satukan deployment |
| **Core Services** | Library bersama (auth, notif, file, audit) | Reuse, hindari duplikasi |
| **Data** | PostgreSQL + Redis + S3-compat (MinIO/cloud) | Stack standar, gratis/murah, dikuasai tim lokal |

---

## D. Database Utama (Skema Inti — Disederhanakan)

> **Satu database PostgreSQL**, dipisah dengan **schema per modul** (`ticketing.*`, `asset.*`, `booking.*`, `task.*`, `core.*`).

| Schema | Tabel Utama | Relasi Kunci |
|---|---|---|
| **core** | `users`, `roles`, `user_roles`, `buildings`, `rooms`, `notifications`, `audit_logs`, `attachments` | Master data dipakai semua modul |
| **ticketing** | `tickets`, `ticket_status_history`, `ticket_categories`, `ticket_assignments`, `ticket_ratings` | `tickets.room_id` → `core.rooms`; `tickets.asset_id` → `asset.assets` (nullable di MVP) |
| **asset** | `assets`, `asset_categories`, `asset_movements`, `asset_inspections` | `assets.room_id` → `core.rooms`; `assets.qr_code` (unique) |
| **booking** | `bookings`, `booking_approvals`, `booking_resources`, `booking_blackouts` | `bookings.room_id` → `core.rooms`; `bookings.requester_id` → `core.users` |
| **task** | `tasks`, `task_assignments`, `task_comments`, `task_dependencies` | `tasks.related_ticket_id` → `ticketing.tickets` (nullable) |

### Estimasi Volume Data 2 Tahun
| Tabel | Estimasi Baris | Catatan |
|---|---|---|
| `tickets` | ~10.000 | 200–450/bulan × 24 |
| `assets` | ~10.000–15.000 | 40–80 lab × ~150 aset rata-rata |
| `bookings` | ~50.000 | Booking harian × 40–80 lab |
| `audit_logs` | ~1–2 juta | Setiap aksi penting tercatat |
| `attachments` | ~30.000 | Foto kerusakan + foto aset |

> **Insight:** Volume **sangat moderat**. PostgreSQL single-node + read replica sudah cukup untuk **3–5 tahun ke depan**. Tidak butuh sharding, tidak butuh NoSQL.

---

## E. Alur Data Inti (3 Skenario Kritis)

### Alur 1 — Lapor Kerusakan via WhatsApp (Modul Ticketing)
```
Mahasiswa  →  WA Bot  →  Webhook  →  API  →  ticketing.tickets (created)
                                       │
                                       ├─►  core.notifications (notif ke dispatcher)
                                       └─►  core.audit_logs
                                       
Dispatcher →  Web App  →  API  →  ticket_assignments (assigned)
                                       │
                                       └─►  core.notifications (notif ke teknisi via WA)
                                       
Teknisi    →  WA Bot  →  API  →  ticket_status_history (in_progress → done)
                                       │
                                       └─►  core.notifications (link konfirmasi ke pelapor)
                                       
Mahasiswa  →  Klik link  →  API  →  ticket_ratings + status (closed)
```

### Alur 2 — Tiket Membuat Aset Baru (Integrasi M1 ↔ M2)
```
Tiket dibuat dengan kategori "AC" di Lab Kimia 3
   │
   ├─► Sistem cek: apakah ada asset di room_id Lab Kimia 3 dengan kategori "AC"?
   │        ├─ YA  →  link tiket ke asset_id
   │        └─ TIDAK → buat draft asset (status: unverified) + flag laboran review
   │
   └─► Setelah tiket selesai, laboran konfirmasi/edit draft asset → status: verified
```
> Inilah implementasi konsensus debat: **registry aset tumbuh organik dari tiket**, bukan top-down.

### Alur 3 — Booking Lab dengan Konflik (Modul Booking)
```
Dosen → Web App → POST /bookings
   │
   ├─► booking_resources cek konflik slot waktu di room_id
   │        ├─ Konflik   → reject + tampilkan slot alternatif
   │        └─ No conflict → booking_approvals (status: pending)
   │
   ├─► core.notifications → Kepala Lab / Kaprodi (approver)
   │
   └─► Approver decide → status: approved/rejected
            └─► core.notifications → Dosen (hasil keputusan)
```

---

## F. Integrasi Antar Modul

| Dari → Ke | Tipe Integrasi | Use Case Konkret |
|---|---|---|
| **M1 → M2** | Foreign key (`ticket.asset_id`) + auto-create draft | Tiket "AC rusak" otomatis cek/buat asset AC di ruang tsb |
| **M2 → M1** | Query history | Halaman aset menampilkan riwayat tiket aset itu |
| **M1 → M4** | Trigger event | Tiket eskalasi >SLA → auto-create task ke supervisor |
| **M3 → M2** | Validasi referensial | Booking lab cek aset yang tersedia di lab tsb |
| **M3 → M1** | Trigger event | Kerusakan saat booking → 1-klik buat tiket dari halaman booking |
| **M2 → M3** | Validasi maintenance | Lab dengan aset critical "rusak" auto-block dari booking |
| **All → Core** | Library call | Auth, notification, file upload, audit log |

> **Pola integrasi:** Mulai dengan **foreign key + library call** (sederhana, atomic). Hindari event bus (Kafka/RabbitMQ) di MVP — overkill untuk volume FSM.

---

## G. Keamanan Dasar (Security Baseline)

| Lapisan | Kontrol Wajib MVP | Kontrol Lanjutan (Pasca MVP) |
|---|---|---|
| **Identitas** | SSO UNDIP (jika ada) atau email+password dengan bcrypt | MFA untuk role admin & pimpinan |
| **Autorisasi** | RBAC 6 role; cek di setiap endpoint | Row-level security per gedung/prodi |
| **Transport** | HTTPS only (HSTS), TLS 1.2+ | Certificate pinning di mobile (jika ada) |
| **Data at Rest** | PostgreSQL native encryption (disk-level) | Column-level encryption untuk PII sensitif |
| **API** | JWT (15 menit) + refresh token; rate limit 100 req/menit/user | API key terpisah untuk integrasi sistem lain |
| **File Upload** | Validasi MIME + ukuran max 10 MB + virus scan (ClamAV) | Watermark otomatis foto bukti tiket |
| **Audit** | `core.audit_logs` untuk: login, perubahan tiket, approve booking, perubahan aset | Audit immutable (append-only + hash chain) |
| **Privasi** | NIM/NIP tidak ditampilkan publik; link konfirmasi pakai token random | Anonymization untuk dashboard publik |
| **Backup** | Daily automated backup + retensi 30 hari | Disaster recovery site (off-site) |
| **Secrets** | Environment variables, tidak di-commit | Vault (HashiCorp/AWS Secrets Manager) |

> **Prinsip:** Lulus standar **OWASP Top 10** + sesuai **PP 71/2019** (perlindungan data). Tidak perlu ISO 27001 di MVP.

---

## H. Opsi AI / IoT Masa Depan

> **Aturan main:** Tidak ada AI/IoT di MVP. Tahun ke-2+ jika ada justifikasi data & ROI jelas.

| Modul | Opsi AI | Opsi IoT | Prasyarat |
|---|---|---|---|
| **M1 Ticketing** | • Auto-kategorisasi tiket dari teks/foto<br>• Suggest teknisi terbaik (history performa)<br>• Predictive maintenance (pola kerusakan AC/listrik) | • Sensor suhu/kelembaban → auto-tiket<br>• Smoke detector → tiket darurat | ≥12 bulan data tiket; label kategori bersih |
| **M2 Asset** | • OCR auto-fill dari label aset<br>• Image classification kondisi aset<br>• Forecasting umur aset | • RFID/BLE tag tracking lokasi<br>• Sensor getaran untuk mesin lab | Format label aset terstandar |
| **M3 Booking** | • Smart suggestion ruang ideal (ukuran kelas, kompatibilitas)<br>• Detect booking palsu (no-show pattern) | • Sensor okupansi (deteksi no-show otomatis)<br>• Smart lock terbuka by booking | API booking stabil ≥6 bulan |
| **M4 Task** | • AI summarization mingguan<br>• Workload balancing suggestion | — | Adopsi M4 ≥80% tim ops |

### Roadmap AI/IoT (Indikatif)
```
Tahun 1: Fondasi data (semua MVP berjalan, kumpul data bersih)
Tahun 2: AI ringan (auto-kategorisasi, smart suggestion) — internal model atau API LLM
Tahun 3: IoT pilot (sensor suhu di lab kritis, smart lock 5 lab)
Tahun 4+: Predictive maintenance + integrasi BIM/3D
```

---

## I. Stack Teknologi (Default Choice)

| Lapisan | Pilihan Default | Alternatif |
|---|---|---|
| Frontend | Next.js 14 + TailwindCSS + shadcn/ui | Vue/Nuxt jika tim lebih kuat di Vue |
| Backend | NestJS (TypeScript) | Laravel 11 (PHP) jika tim PHP-heavy |
| Database | PostgreSQL 16 | — (jangan diganti) |
| Cache & Queue | Redis 7 | — |
| File Storage | MinIO (on-prem) atau S3 (cloud) | — |
| WA Integration | WhatsApp Business API resmi (BSP) | Meta Cloud API langsung |
| Auth | JWT + Passport.js / Sanctum | SSO UNDIP (OAuth2/SAML) |
| CI/CD | GitHub Actions | GitLab CI |
| Monitoring | Grafana + Prometheus + Loki | Sentry untuk error tracking |
| Container | Docker + Docker Compose | Kubernetes hanya jika scale >10x |

> **Rule of thumb:** Pilih stack yang **bisa di-debug oleh anggota termuda di tim** pukul 2 pagi saat production down.

---

## J. Ringkasan Anti-Overengineering — 10 Aturan Wajib

| # | Aturan | Alasan |
|---|---|---|
| 1 | **Monolith dulu, microservice nanti** | Volume FSM tidak butuh microservice |
| 2 | **Single PostgreSQL, schema-per-modul** | Hindari multi-database management |
| 3 | **No event bus di MVP** (Kafka/RabbitMQ) | Foreign key + sync call cukup |
| 4 | **No native mobile app di MVP** | Web responsive + WA Bot sudah covers 95% use case |
| 5 | **No microfrontend** | Single Next.js app dengan route per modul |
| 6 | **No GraphQL** | REST sederhana cukup, tim lebih familiar |
| 7 | **No Kubernetes** | Docker Compose + 1 VPS sudah cukup untuk 5.000 user |
| 8 | **No service mesh / Istio** | Tidak ada microservice = tidak butuh mesh |
| 9 | **No AI/IoT di MVP** | Butuh data dulu, baru AI bermakna |
| 10 | **No custom auth, pakai library standar** | Keamanan = jangan coba-coba |

---

## K. Checklist Kesiapan Arsitektur

- [ ] Tim sepakat: **monolith modular** (bukan microservice)
- [ ] Stack default disetujui Tech Lead (NestJS / Laravel)
- [ ] Akses VPS / cloud disiapkan (min 4 vCPU, 8 GB RAM, 100 GB SSD)
- [ ] Domain & SSL siap (`fsm-superapp.undip.ac.id` atau subdomain serupa)
- [ ] Akses WhatsApp Business API dipastikan (lihat Bagian I, Disensus)
- [ ] Skema RBAC 6 role direview oleh Project Owner
- [ ] Backup & disaster recovery plan ditetapkan (RPO ≤24 jam, RTO ≤4 jam)

---

> 🧱 **Bagian II ini sengaja dirancang membosankan.** Arsitektur yang membosankan adalah arsitektur yang berhasil. Setiap pilihan "menarik" yang tidak perlu adalah biaya yang akan dibayar di production pukul 2 pagi.



---

# 🔄 Bagian III — Pivot Arsitektur ke JAMstack + Supabase

> **Konteks:** Tim development memutuskan stack final adalah **Vite + React + Supabase** (tanpa server-side backend tradisional, tanpa UI library). Bagian II di atas dibiarkan sebagai *decision log* dan **digantikan oleh bagian ini**.

---

## A. Apa yang Berubah (Diff dari Bagian II)

| Komponen | Bagian II (Lama) | Bagian III (Final) | Implikasi |
|---|---|---|---|
| **Backend** | NestJS / Laravel monolith | **Supabase only** (Auth + Postgres + Storage + Realtime + Edge Functions) | Tidak ada server tradisional; RLS jadi *single line of defense* |
| **Frontend** | Next.js 14 + TailwindCSS + shadcn/ui | **Vite 5 + React 18 + TS strict + plain CSS + PWA** | Static SPA, tidak ada SSR, semua UI dibuat manual |
| **Routing** | Next.js file-based | react-router-dom v6 | Manual route guards |
| **API Layer** | REST via NestJS controllers | **Supabase auto-API + RPC (Postgres functions) + Edge Functions** | Logika bisnis kompleks pindah ke Postgres function |
| **File Storage** | MinIO / S3-compat | **Supabase Storage** | Signed URL & RLS bucket policy |
| **Realtime** | Polling | **Supabase Realtime** (WebSocket) | Status tiket update live |
| **Deploy** | Docker + VPS | **Vercel / Netlify / Cloudflare Pages** (static `dist/`) | Tidak ada server yang di-manage |
| **Testing** | Jest + Supertest | **Vitest + @testing-library/react + jsdom** | RLS test perlu integration test khusus |
| **Mobile** | Web responsive | **PWA installable** (vite-plugin-pwa, Workbox) | Bisa di-install dari Chrome, offline-capable |

---

## B. Arsitektur Revisi (Layered View)

```
┌─────────────────────────────────────────────────────────────┐
│  CLIENT (PWA — installable, offline-capable)                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Vite 5 + React 18 + TS strict + react-router v6     │   │
│  │ Plain CSS · Workbox SW · @supabase/supabase-js v2   │   │
│  └─────────────────────────────────────────────────────┘   │
│  ▲ Static bundle dideploy ke Vercel/Netlify/CF Pages       │
└──────────────────────────┬──────────────────────────────────┘
                           │  HTTPS · JWT (Supabase Auth)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  SUPABASE (Managed BaaS)                                    │
│  ┌─────────┬──────────┬──────────┬──────────┬───────────┐  │
│  │ Auth    │ Postgres │ Storage  │ Realtime │ Edge Fn   │  │
│  │ (GoTrue)│ +RLS+RPC │ (S3-like)│(WS pub/  │(Deno: WA  │  │
│  │         │          │          │  sub)    │webhook,   │  │
│  │         │          │          │          │OCR proxy) │  │
│  └─────────┴──────────┴──────────┴──────────┴───────────┘  │
└──────────────┬───────────────────────────────────┬──────────┘
               │                                   │
               ▼                                   ▼
        WhatsApp Business API              Email (Resend/SES)
        (via Edge Function webhook)        (via Edge Function)
```

| Lapisan | Komponen | Catatan |
|---|---|---|
| **Client (PWA)** | Vite + React + TS strict + plain CSS | Single bundle, route guards manual via `<RequireAuth>` |
| **Auth** | Supabase Auth (email/password + magic link + opsional SSO UNDIP via OAuth2) | JWT lifetime 1 jam, refresh 30 hari |
| **Data** | Postgres dengan **RLS wajib di SEMUA tabel domain** | Kebijakan default: `deny`, lalu allow per role |
| **Logika Kompleks** | Postgres functions (`SECURITY DEFINER` di-audit) + Edge Functions (Deno) | Hindari logika di client untuk operasi multi-tabel |
| **Realtime** | Subscribe ke `tickets`, `bookings` table changes | Live status tracking tanpa polling |
| **Storage** | Bucket per modul (`ticket-photos`, `asset-photos`) dengan RLS bucket | Ukuran max per file 25 MB |
| **Webhook WA** | Edge Function `wa-webhook` menerima dari Meta Cloud API | Verifikasi HMAC signature wajib |

---

## C. Strategi RLS (Pengganti API Gateway/Authz)

> **Aturan emas:** RLS adalah **satu-satunya** lapisan otorisasi data. Bug di sini = bencana. Setiap kebijakan **wajib punya test pgTAP di CI**.

| Pola RLS | Use Case | Contoh Kebijakan |
|---|---|---|
| **Owner-only** | Mahasiswa hanya lihat tiketnya sendiri | `auth.uid() = reporter_id` |
| **Role-based** | Tendik dispatcher lihat semua tiket | `EXISTS (SELECT 1 FROM user_roles WHERE user_id=auth.uid() AND role='dispatcher')` |
| **Building/Prodi-scoped** | Kepala lab kimia hanya lihat aset lab kimia | `building_id IN (SELECT building_id FROM user_buildings WHERE user_id=auth.uid())` |
| **Public read, no write** | Status tiket via link unik (no-login) | Akses lewat **Edge Function** dengan token random, bukan RLS langsung |
| **Service-only** | Audit log immutable | Semua user `INSERT`, **tidak ada user `UPDATE/DELETE`** |

### 🔐 Aturan RLS Wajib FSM Super Apps
1. **Tabel tanpa RLS = tabel dilarang.** Default policy: `enable RLS, no policies` (=deny all).
2. **`service_role` key TIDAK PERNAH dipakai di client.** Hanya di Edge Function & GitHub Actions secret.
3. **Setiap policy punya 1 test pgTAP minimum:** "user A tidak bisa baca data user B".
4. **Cross-schema query** wajib via Postgres function `SECURITY DEFINER` yang di-review.
5. **Storage bucket** semua **private** + akses lewat signed URL (TTL max 1 jam).

---

## D. Stack Final

| Lapisan | Pilihan | Versi |
|---|---|---|
| Build tool | Vite | 5 |
| Framework | React | 18 |
| Bahasa | TypeScript | 5 strict mode |
| Routing | react-router-dom | v6 |
| PWA | vite-plugin-pwa (Workbox autoUpdate) | latest |
| Styling | **Plain CSS** (no library) | — |
| Backend | Supabase | self-host opsional |
| DB | Postgres (Supabase) | 15 |
| File | Supabase Storage | — |
| Realtime | Supabase Realtime | — |
| Edge Fn | Supabase Edge Functions (Deno) | — |
| Test | Vitest + @testing-library/react + jsdom | latest |
| CI | GitHub Actions (`bootstrap.yml` + `ci.yml`) | — |
| Deploy | Vercel / Netlify / Cloudflare Pages | static `dist/` |

---

## E. Implikasi Per Modul

| Modul | Yang Berubah Karena Pivot |
|---|---|
| **M1 Ticketing** | WA Bot via Edge Function `wa-webhook`; status live via Realtime subscribe |
| **M2 Asset** | QR code di-generate client-side (lib JS); foto via Supabase Storage |
| **M3 Booking** | Konflik slot dicek via Postgres function `check_booking_conflict()`; approval via RLS role |
| **M4 Task** | Sederhana — CRUD + RLS standar |
| **Dashboard Pimpinan** | Materialized view di-refresh via cron Edge Function (tiap 15 menit) |
| **Status Tracking Publik** | Edge Function `public-ticket-status` dengan token random — **tidak lewat RLS** |

---

# 🗡️ Bagian IV — Sesi Kritik Adversarial: Apa yang Bisa Membunuh Proyek?

> **Aturan sesi:** 5 agen berdaulat menyerang rencana ini sekeras mungkin. **Risiko "ganti WD II" dikecualikan** atas instruksi sponsor. Setiap risiko punya **mitigasi konkret + owner**.

---

## Ronde 1 — Risiko Teknis (Stack-Specific)

### 🏗️ ARSITEK membuka serangan ke stack-nya sendiri
> "Saya yang menyetujui stack ini, dan saya yang akan menyerangnya pertama. Tiga risiko teknis fatal:
> 1. **RLS policy bug = leak global**. Satu policy salah → 4.500 mahasiswa bisa baca data semua orang. Tidak ada *defense in depth* — RLS adalah satu-satunya tembok.
> 2. **Edge Function cold start untuk WA webhook**: free tier 1–3 detik. Pengguna kirim WA → bot diam → user kirim ulang → tiket duplikat.
> 3. **Static deploy = semua logika bisnis terlihat di bundle JS**. Mahasiswa pintar bisa baca query Supabase lalu coba bypass RLS dengan crafted request."

### 🗡️ OPOSISI menambah
> "Tambah satu: **plain CSS untuk 4 modul × ~50 halaman = ~200 file CSS yang harus di-maintain manual**. Tanpa design system / component library, UI akan **inkonsisten**, accessibility hancur, dan junior dev akan re-invent button 17 kali. Proyek mati pelan-pelan karena *visual debt*."

### 🔧 LAPANGAN setuju keras
> "Saya melihat aplikasi pemerintah/kampus yang plain CSS — semuanya **terlihat amatir** dibanding Tokopedia/Gojek. Mahasiswa akan bilang 'aplikasi UNDIP jelek' di Twitter, dan adopsi turun **bukan karena fungsionalitas, tapi karena gengsi**."

### 🧭 VISIONER menyerang TS strict mode
> "**TypeScript 5 strict mode + tim yang belum pengalaman = velocity turun 30–50% di sprint 1–3**. Setiap `unknown`, `never`, generic constraint akan jadi 2 jam debate Slack. Saya pernah lihat tim lumpuh 2 minggu karena `as const` vs `satisfies`."

### 🪖 POLITIK menambah
> "Dan PWA install di Indonesia: **rate adopsi 5–15%**. Mahasiswa terbiasa app dari Play Store. PWA dianggap 'bukan aplikasi sungguhan'. Anda kehilangan psychological credibility dari hari 1."

### 📋 Risk Register Ronde 1 — Teknis
| ID | Risiko | Severity | Probabilitas | Mitigasi Konkret | Owner |
|---|---|---|---|---|---|
| T-01 | Bug RLS → data leak global | 🔴 Critical | Sedang | • **pgTAP test suite** untuk setiap policy, jalan di CI<br>• **Negative tests**: user A buka data user B harus return 0 baris<br>• **RLS lint** (Supabase CLI) di pre-commit | Tech Lead |
| T-02 | Edge Function cold start WA → tiket duplikat | 🟡 High | Tinggi | • **Idempotency key** per pesan WA (hash dari message_id Meta)<br>• **Upgrade Supabase Pro** sejak MVP (cold start <500ms)<br>• Reply ke user "tiket sedang dibuat" dalam <2 detik | Backend Dev |
| T-03 | Logika bisnis terekspos di bundle JS | 🟡 High | Pasti | • **Semua validasi multi-tabel di Postgres function**, bukan client<br>• Anggap client = untrusted; RLS + DB constraint adalah otoritas final<br>• Audit bundle dengan `source-map-explorer` sebelum rilis | Tech Lead |
| T-04 | Plain CSS → inkonsistensi UI + accessibility issue | 🟠 Med-High | Tinggi | • **Design tokens** (CSS variables) wajib dari sprint 1<br>• **Komponen primitif kustom** (Button, Input, Modal) — buat 10 komponen inti dulu<br>• **Lighthouse a11y ≥90** di CI<br>• Reconsider: pakai **Radix UI Primitives** (headless, plain CSS-friendly) — bukan UI library penuh | UI/UX + FE Lead |
| T-05 | TS strict + tim junior = velocity drop | 🟡 High | Tinggi | • **Tim tooling pre-set**: tsconfig template + eslint + prettier<br>• **Pair programming** sprint 1–2<br>• **Type cookbook** internal: 20 pola umum FSM dengan contoh<br>• Toleransi `any` terbatas dengan TODO comment | Tech Lead |
| T-06 | PWA install rate rendah di Indonesia | 🟠 Med | Tinggi | • **In-app prompt install** muncul setelah 3 kunjungan<br>• Tutorial "Cara install di Android/iOS" di onboarding<br>• Tetap fully functional tanpa install (browser-only mode) | UI/UX |
| T-07 | Realtime connection limit Supabase Pro (500 concurrent default) | 🟠 Med | Sedang | • Realtime **hanya untuk halaman aktif** (subscribe on mount, unsubscribe on unmount)<br>• Halaman dashboard pakai polling 30 detik, bukan realtime<br>• Monitor concurrent connection di dashboard Supabase | Backend Dev |
| T-08 | jsdom Vitest tidak emulasi Realtime/WebSocket nyata | 🟠 Med | Pasti | • **Test E2E dengan Playwright** terhadap staging Supabase nyata<br>• Mock Supabase client di unit test, real client di integration test<br>• CI job khusus `integration-test` mingguan | QA |

---

## Ronde 2 — Risiko Data

### 🏗️ ARSITEK
> "**Backup retention Supabase Pro: 7 hari** (PITR addon optional, mahal). Audit BPK butuh history 5–10 tahun. Anda akan kena temuan audit di tahun ke-2."

### 🗡️ OPOSISI
> "Lebih buruk: **search di Postgres full-text** untuk 10.000 tiket × 15.000 aset performanya akan turun setelah tahun ke-2. Tanpa Elasticsearch atau pgvector index proper, fitur search jadi **8 detik per query**. Pengguna akan stop pakai search."

### 🪖 POLITIK
> "Dan ada **risiko data residency**. Supabase server di luar Indonesia (US/SG default). Beberapa data PNS/akademik kena **PP 71/2019** (data strategis harus di Indonesia). FSM bisa kena teguran Kemenristek/Kemkominfo."

### 🧭 VISIONER
> "**Soft delete vs hard delete**: Supabase tidak otomatis soft delete. Kalau tiket dihapus → audit trail rusak → tidak bisa investigasi kasus 6 bulan ke depan. Tanpa konvensi ketat, tim akan `DELETE FROM` sembarangan."

### 🔧 LAPANGAN
> "Realita lapangan: **3.500–4.500 mahasiswa upload foto kerusakan**. Estimasi 200–450 tiket × ~3 foto × 2 MB = ~1,2–2,7 GB/bulan. Setahun **15–32 GB**. Supabase Pro Storage **100 GB**, tapi bandwidth-nya yang mahal kalau dilihat ulang. Cek tarif egress."

### 📋 Risk Register Ronde 2 — Data
| ID | Risiko | Severity | Mitigasi | Owner |
|---|---|---|---|---|
| D-01 | Backup 7 hari tidak cukup untuk audit BPK | 🔴 Critical | • **Daily export ke S3 Indonesia / on-prem UNDIP** via GitHub Actions cron<br>• Retensi 5 tahun untuk dump tabel kritis (`tickets`, `assets`, `bookings`, `audit_logs`)<br>• Format: SQL + CSV + checksum | DevOps |
| D-02 | Search performance degradasi di volume besar | 🟠 Med | • **GIN index + tsvector** sejak hari 1 untuk kolom search<br>• Pagination wajib (max 50 baris/page)<br>• Monitoring query time di Supabase dashboard mingguan | Backend Dev |
| D-03 | Data residency (PP 71/2019) | 🟡 High | • **Pilih region Supabase Singapore** (terdekat) sebagai kompromi<br>• Konsultasi DPO/legal UNDIP sebelum go-live<br>• **Self-host Supabase di server UNDIP** sebagai opsi tahun ke-2 | Project Sponsor |
| D-04 | Hard delete merusak audit trail | 🟠 Med-High | • **Konvensi: tidak ada DELETE, hanya `deleted_at` kolom**<br>• RLS policy hide soft-deleted rows by default<br>• `audit_logs` dilindungi RLS: insert-only, no update/delete | Tech Lead |
| D-05 | Bandwidth egress foto membengkak | 🟠 Med | • **Image transform di-cache** (Supabase Image Transformations)<br>• Compress client-side sebelum upload (max 1 MB) via `browser-image-compression`<br>• Thumbnail untuk listing, full-size hanya saat klik | FE Lead |
| D-06 | Race condition Realtime + offline PWA | 🟠 Med | • **Last-write-wins dengan timestamp** untuk field non-kritis<br>• **Conflict UI** untuk field kritis: "Data berubah, refresh?"<br>• Disable offline write untuk Booking & Asset (read-only offline) | FE Lead |

---

## Ronde 3 — Risiko Keamanan

### 🗡️ OPOSISI menyerang habis
> "Saya buat daftar singkat:
> 1. **`service_role` key bocor di env Vercel** → game over. Anyone bisa baca/tulis semua data.
> 2. **CORS misconfigured di Supabase** → website lain bisa pakai API Anda atas nama user.
> 3. **Email enumeration di Auth** → attacker tahu NIM mana yang sudah daftar.
> 4. **Brute force login**: Supabase Auth punya rate limit, tapi default-nya lemah.
> 5. **Signed URL Storage TTL terlalu panjang** → URL leak = file leak permanen.
> 6. **Tidak ada WAF** di Vercel/Netlify free tier → DDoS / scraping mudah."

### 🏗️ ARSITEK
> "Tambahan: **HMAC verification webhook WA**. Kalau Edge Function tidak verify signature dari Meta, attacker bisa kirim webhook palsu → tiket palsu masuk → spam database."

### 🪖 POLITIK
> "Risiko reputasi: **insiden keamanan kecil pun akan jadi headline**. 'Data 4.000 mahasiswa UNDIP bocor' lebih viral daripada 5 tahun fitur sukses. Satu kebocoran = proyek dibekukan."

### 🧭 VISIONER
> "**Audit log harus immutable + hash chain**. Kalau attacker masuk dan menghapus jejak, kita tidak akan pernah tahu. Tanpa append-only audit, post-mortem mustahil."

### 📋 Risk Register Ronde 3 — Keamanan
| ID | Risiko | Severity | Mitigasi | Owner |
|---|---|---|---|---|
| S-01 | `service_role` key bocor | 🔴 Critical | • **Service role HANYA di Edge Function env + GitHub Actions secret**<br>• Tidak pernah commit ke repo (gitleaks di pre-commit)<br>• **Secret rotation** tiap 90 hari<br>• **Vercel env** di-set sebagai *encrypted* | DevOps |
| S-02 | RLS policy bug | 🔴 Critical | (Lihat T-01) — pgTAP suite + negative tests + lint | Tech Lead |
| S-03 | CORS misconfig | 🟡 High | • **Whitelist domain explicit** (`fsm-superapp.undip.ac.id`)<br>• Tidak pernah `*` di production | Tech Lead |
| S-04 | Email enumeration & brute force login | 🟠 Med | • **Magic link** sebagai default, password sebagai fallback<br>• Supabase Auth rate limit upgrade ke Pro<br>• **Generic error message** ("email atau password salah") | Backend Dev |
| S-05 | Signed URL Storage leak | 🟠 Med | • **TTL max 60 menit**<br>• Bucket private, tidak ada public bucket<br>• Audit log untuk `getSignedUrl` calls | Backend Dev |
| S-06 | Tidak ada WAF / DDoS protection | 🟠 Med | • Pilih **Cloudflare Pages** (WAF & rate limit gratis) > Vercel/Netlify<br>• Supabase: rate limit per IP via Edge Function gateway untuk endpoint sensitif | DevOps |
| S-07 | Webhook WA tanpa HMAC | 🔴 Critical | • **Verify signature wajib** di Edge Function `wa-webhook`<br>• Drop request jika header `X-Hub-Signature-256` invalid<br>• Test forgery di staging | Backend Dev |
| S-08 | Audit log bisa di-tamper | 🟡 High | • RLS: `audit_logs` insert-only, no update/delete (bahkan service_role harus pakai SECURITY DEFINER fn)<br>• **Hash chain**: tiap row punya `prev_hash` + `current_hash` (SHA-256)<br>• Daily checksum dump ke off-site | Tech Lead |
| S-09 | PII (NIM, NIP, email) bocor di log/error | 🟠 Med | • **Log sanitization** di Edge Function (regex masking)<br>• Sentry config: PII scrubbing aktif<br>• Tidak pernah `console.log(user)` di production build | FE Lead |

---

## Ronde 4 — Risiko Adopsi & Operasional

### 🔧 LAPANGAN memimpin
> "Saya gabung adopsi + operasional karena di lapangan keduanya menyatu. **5 risiko membunuh adopsi** yang spesifik untuk stack ini:
> 1. **PWA install button hilang di iOS Safari** (cuma muncul di Chrome Android). 30% mahasiswa pakai iPhone → tidak bisa install → akses via browser → lupa link.
> 2. **Plain CSS = mobile UX patchy**. Touch target salah ukuran, scroll behavior aneh, modal tidak ter-handle dengan baik di Android keyboard pop up.
> 3. **Realtime butuh koneksi stabil**. Sinyal di Lab Kimia 3 (basement, beton tebal) jelek → user lihat status lama → mengira sistem rusak.
> 4. **Offline mode setengah jadi**: PWA cache halaman, tapi action (buat tiket) tetap butuh online → user kira app rusak.
> 5. **Foto upload via PWA Android** kadang gagal di kamera lawas (Android <10) — file format HEIC/HEIF tidak dikompres."

### 🪖 POLITIK menambah bottleneck operasional
> "Bottleneck #1: **siapa yang admin Supabase?** Tim cuma 5 orang. Semua tahu React, **berapa yang paham RLS, Postgres function, Edge Function Deno?** Kalau jawabannya 1 orang → bus factor = 1. Orang itu cuti seminggu, proyek freeze.
> Bottleneck #2: **migrasi schema**. Supabase migration via SQL files di Git. Tanpa proses ketat, dev A push migration konflik dengan dev B → staging rusak → blocker."

### 🗡️ OPOSISI menyerang ekonomi
> "Realitas biaya yang tidak dihitung:
> - **Supabase Pro**: $25/bulan/project. Untuk staging + prod = $50/bulan minimum.
> - **WhatsApp Business API via BSP**: setup fee $100–500 + per-message fee.
> - **Image transformations Supabase**: $5/1000 transformations setelah tier gratis.
> - **Vercel Pro** (jika butuh) $20/bulan/team.
> - **Domain + SSL custom**: ~Rp 200rb/tahun.
> Total: **~Rp 1–2 juta/bulan** dari hari 1, sebelum produksi. Sudah ada anggaran resmi?"

### 🧭 VISIONER tentang skill gap
> "Plain CSS untuk 4 modul × ~50 halaman = ratusan komponen. **Tanpa Storybook atau visual regression test**, refactor CSS = mengundang bug visual. Hire/train UI engineer khusus, bukan full-stack dev."

### 🏗️ ARSITEK tentang testing gap
> "Vitest + jsdom **tidak bisa test RLS, Realtime, atau Edge Function secara end-to-end**. Tanpa staging Supabase yang dipakai untuk integration test, **bug RLS baru terdeteksi di production**. Itu skenario terburuk."

### 📋 Risk Register Ronde 4 — Adopsi & Operasional
| ID | Risiko | Severity | Mitigasi | Owner |
|---|---|---|---|---|
| A-01 | iOS Safari tidak ada install button | 🟠 Med | • **Tutorial visual "Add to Home Screen"** untuk iOS<br>• QR code di poster langsung ke URL (bukan PWA install)<br>• Test di iPhone real, bukan simulator | UI/UX |
| A-02 | Plain CSS mobile UX patchy | 🟠 Med-High | • **Mobile-first CSS** dari hari 1<br>• Test di 5 device real (Android budget, mid, flagship + iPhone lama, baru)<br>• `viewport-fit=cover` + safe-area-inset di CSS | FE Lead |
| A-03 | Realtime gagal di area sinyal lemah | 🟡 High | • **Fallback polling** otomatis jika WebSocket gagal 3x<br>• "Last sync: 2 menit lalu" indicator di UI<br>• Test di Lab Kimia 3 sebenarnya saat UAT | FE Lead |
| A-04 | Offline mode misleading | 🟠 Med | • **Banner jelas**: "Anda offline, perubahan tidak tersimpan"<br>• Disable tombol "Kirim Tiket" saat offline (atau queue dengan UI eksplisit)<br>• Tidak boleh ada UI yang menipu | FE Lead |
| A-05 | Upload foto gagal di Android lawas | 🟠 Med | • **Konversi HEIC → JPEG** via `heic2any` lib client-side<br>• Resize sebelum upload (max 2 MB)<br>• Test di Android 8 sebagai baseline | FE Lead |
| O-01 | Bus factor 1 untuk Supabase ops | 🔴 Critical | • **2 orang minimum** terlatih RLS + Edge Function<br>• **Runbook Supabase**: skenario umum (rotate key, restore backup, debug RLS)<br>• Pair programming setiap deploy schema | Tech Lead |
| O-02 | Schema migration konflik | 🟡 High | • **Konvensi nama**: `YYYYMMDDHHMM_description.sql` (timestamp ketat)<br>• PR template wajib include migration file di section "Schema Changes"<br>• Apply migration via CI ke staging dulu, prod hanya setelah review | DevOps |
| O-03 | Biaya operasional tidak ter-anggarkan | 🟡 High | • **Cost projection 12 bulan** sebelum kickoff (~Rp 12–24 juta/tahun)<br>• Anggaran resmi disetujui di Fase 1 RAD<br>• Monitoring biaya bulanan, alert jika >20% naik | Project Sponsor |
| O-04 | Visual regression CSS | 🟠 Med | • **Komponen primitif** dengan Storybook (opsi ringan: Ladle)<br>• **Visual regression** dengan Playwright screenshot test (opsional bulan 3+)<br>• CSS modules untuk scoping (`*.module.css`) | FE Lead |
| O-05 | Integration test RLS tidak ada | 🔴 Critical | • **Staging Supabase project terpisah** dari dev<br>• **Test E2E mingguan** dengan Playwright + real Supabase staging<br>• Skema test: seed data → run policies → assert akses tiap role | QA |
| O-06 | WA Business API approval lama (4–8 minggu) | 🟡 High | • **Daftar BSP sejak Fase 1**, jangan tunggu coding selesai<br>• Fallback: **email notification** jika WA belum siap<br>• Pilot dengan personal WA group dulu (manual) untuk validasi flow | Project Sponsor |

---

## Ronde 5 — Risiko Bias (yang Tidak Disadari Tim)

### 🗡️ OPOSISI memimpin
> "Tim ini punya bias yang tidak disadari. Saya bongkar:
> 1. **Bias 'semua punya smartphone bagus'** — pak satpam, OB, supir mungkin tidak. Kalau modul Asset libatkan mereka, gagal.
> 2. **Bias 'Supabase = simple'** — RLS adalah satu konsep paling kompleks dalam database modern. Tim akan kaget di minggu ke-3.
> 3. **Bias 'static deploy = aman'** — sebaliknya, semua kode bisa di-inspect.
> 4. **Bias 'mahasiswa modern paham UI'** — banyak mahasiswa baru dari daerah, bahasa Inggris kurang, UX harus **bahasa Indonesia ramah, bukan UI startup**.
> 5. **Bias 'WA Bot = solusi semua'** — dosen senior tidak baca WA broadcast formal.
> 6. **Bias 'pasti ada laboran yang bisa update aset'** — laboran adalah PNS dengan KPI sendiri, mereka **tidak otomatis akan input data** tanpa SK tambahan.
> 7. **Bias 'tim akan stay'** — kalau dev junior dapat kerja di tempat lain dengan gaji 2x, mereka pergi. Proyek freeze."

### 🧭 VISIONER mengakui
> "Diterima. Bias #1 dan #6 adalah blind spot terbesar saya. Saya menambahkan: **bias 'data akan bersih sendirinya'** — registry aset tumbuh organik dari tiket, tapi tanpa proses cleanup mingguan, kategorisasi akan berantakan dalam 2 bulan."

### 🪖 POLITIK
> "Bias politis: **'pimpinan akan baca dashboard'**. Realita: dashboard dilihat 1x saat launching, lalu dilupakan. Butuh **briefing terjadwal** ke pimpinan, bukan dashboard pasif."

### 📋 Risk Register Ronde 5 — Bias
| ID | Bias | Mitigasi |
|---|---|---|
| B-01 | "Semua punya smartphone bagus" | • UAT termasuk **device baseline** Android 8 / iPhone SE 2020<br>• Modul Asset punya **alur input via PC** untuk laboran tanpa smartphone bagus |
| B-02 | "Supabase = simple, RLS otomatis aman" | • **Workshop RLS internal** sebelum sprint 1 (4 jam)<br>• Bookmark dokumentasi Supabase RLS + Postgres docs<br>• 1 orang dedicated jadi "RLS champion" |
| B-03 | "Static deploy = aman" | • Threat model formal sebelum MVP (1 sesi 2 jam)<br>• Pen-test ringan oleh anggota tim lain sebelum go-live |
| B-04 | "User paham UI startup" | • **Bahasa Indonesia ramah**, hindari jargon ("Submit" → "Kirim Laporan")<br>• Tooltip & empty state edukatif<br>• 2 sesi user testing dengan mahasiswa daerah |
| B-05 | "WA Bot = solusi semua segmen" | • **Multi-channel**: WA + email + web + admin proxy untuk dosen senior<br>• Tidak pernah hanya 1 channel untuk notifikasi penting |
| B-06 | "Laboran akan input data sukarela" | • **Insentif input data** disepakati di SK proyek (hari libur tambahan / sertifikat)<br>• Target input dimasukkan di KPI Kepala Lab |
| B-07 | "Tim akan stay" | • **Knowledge base wajib** (Notion/MD repo) untuk setiap keputusan teknis<br>• Pair coding sejak hari 1 (tidak ada "knowledge silo")<br>• Onboarding doc <1 hari |
| B-08 | "Data akan bersih sendiri" | • **Data steward 1 orang** (laboran senior) untuk review kategorisasi mingguan<br>• Cleanup script otomatis untuk merge duplikat (manual approval) |
| B-09 | "Pimpinan akan baca dashboard pasif" | • **Briefing bulanan terjadwal** dengan ringkasan PDF<br>• WA notif mingguan ringkas ke WD II |

---

## 🏛️ Ringkasan Risiko Kritis (Top 10 yang Bisa Membunuh Proyek)

| Rank | ID | Risiko | Severity | Pemicu Awal | Mitigasi Inti |
|---|---|---|---|---|---|
| 1 | T-01 / S-02 | Bug RLS → leak data 4.500 user | 🔴 | Policy salah satu kolom | pgTAP + lint + negative test |
| 2 | S-01 | `service_role` key bocor | 🔴 | Commit ke repo / env Vercel leak | Secret rotation + gitleaks + audit |
| 3 | S-07 | Webhook WA tanpa HMAC | 🔴 | Spam tiket palsu | Verify signature wajib |
| 4 | O-01 | Bus factor 1 admin Supabase | 🔴 | 1 dev cuti/resign | 2+ orang trained, runbook |
| 5 | O-05 | Tidak ada integration test RLS | 🔴 | Bug terdeteksi di prod | Staging Supabase + Playwright |
| 6 | D-01 | Backup 7 hari < tuntutan audit | 🔴 | Audit BPK tahun ke-2 | Daily export 5 tahun ke S3 ID |
| 7 | T-02 | Cold start WA → tiket duplikat | 🟡 | User kirim ulang | Idempotency + Pro plan |
| 8 | O-03 | Biaya tak teranggar | 🟡 | Bulan ke-3, tagihan kaget | Cost projection + monitoring |
| 9 | O-06 | WA BSP approval 4–8 minggu | 🟡 | Kickoff tanpa daftar BSP | Daftar di Fase 1 |
| 10 | D-03 | Data residency PP 71/2019 | 🟡 | Audit Kemkominfo | Region SG + plan self-host |

---

## 🚦 Putusan Sesi Kritik

### Sinyal Hijau Lanjut MVP
- ✅ Tim sepakat **wajib hire/train RLS champion** sebelum sprint 1
- ✅ **Anggaran operasional Rp 12–24 juta/tahun disetujui** sponsor
- ✅ **Staging Supabase + integration test E2E** masuk Definition of Done
- ✅ **Daftar WA Business API BSP dimulai sekarang**, paralel Fase 1

### Sinyal Kuning — Re-evaluate
- ⚠️ Tim 5 orang tapi hanya 1 paham RLS → tunggu hire
- ⚠️ Anggaran masih disetujui per bulan (tidak ada komitmen tahunan)

### Sinyal Merah — Tunda
- 🛑 Tidak ada budget Supabase Pro → free tier tidak layak produksi (cold start, backup, rate limit)
- 🛑 Tidak ada komitmen DPO/legal soal data residency
- 🛑 Tidak ada plan untuk audit integrasi test RLS → game over di hari ke-X

---

## 📝 Catatan Akhir Sesi Kritik

> **5 agen sepakat:** stack Supabase + Vite/React adalah pilihan **valid tapi rapuh**. Kekuatannya (cepat, murah, modern) berbanding terbalik dengan biayanya (RLS = single point of failure, bus factor tinggi, vendor lock-in).
>
> Proyek ini akan berhasil **jika dan hanya jika**:
> 1. RLS diperlakukan sebagai *kelas kritis* — tidak boleh ditulis tanpa test.
> 2. Bus factor minimum 2 untuk setiap area (Supabase, FE, Edge Fn).
> 3. Anggaran operasional **disetujui sebagai biaya tetap**, bukan harapan.
> 4. Adopsi diukur per minggu, bukan per kuartal — koreksi cepat saat metrik turun.
>
> **Kegagalan proyek ini paling mungkin datang dari kombinasi:**
> *Bug RLS yang tidak terdeteksi + bus factor 1 + tidak ada integration test = data leak yang tidak bisa diinvestigasi = proyek dibekukan oleh pimpinan.*

---

## 🧾 Catatan Versi (lanjutan)
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.2 | Mei 2026 | Pivot stack ke Vite + React + Supabase; Bagian II diganti oleh Bagian III |
| 0.3 | Mei 2026 | Sesi kritik adversarial 5 ronde; 40+ risiko teridentifikasi; Top 10 critical disepakati |
