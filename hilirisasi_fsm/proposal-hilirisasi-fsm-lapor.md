# PROPOSAL RISET PENUGASAN HILIRISASI

**HILIRISASI PRODUK PERANGKAT LUNAK FSM LAPOR: SISTEM PELAPORAN INSIDEN BERBASIS PROGRESSIVE WEB APP UNTUK PENGUATAN TATA KELOLA ASET DAN LAYANAN DI FAKULTAS SAINS DAN MATEMATIKA UNIVERSITAS DIPONEGORO**

> **Catatan Dokumen:**
> - Struktur dokumen mengikuti template *Proposal Hilirisasi Informatika* (File 1).
> - Substansi/konten teknis diadaptasi dari *Draft-Lapor-FSM* (File 2).
> - Pengusul: **Satriawan Rasyid Purnama, S.Kom., M.Cs.** (tunggal — Adhe Setya Pramayoga, M.T. **tidak jadi diikutkan**).
> - Pagu anggaran: **Rp 40.000.000,-** (empat puluh juta rupiah).
> - Bagian yang ditandai `[ADAPTASI]` diturunkan dari File 2; `[BARU]` adalah konten baru yang disusun untuk menyesuaikan struktur File 1 (mis. RAB, jadwal hilirisasi, mitra fakultas).

---

**Pengusul:**

Satriawan Rasyid Purnama, S.Kom., M.Cs.
NIP: 199805212024061001 / NUPTK: 7853776677130152

**FAKULTAS SAINS DAN MATEMATIKA**
**UNIVERSITAS DIPONEGORO**
**TAHUN 2026**

---

## HALAMAN PENGESAHAN

| No | Komponen | Isian |
|----|----------|-------|
| 1 | Judul Penelitian | Hilirisasi Produk Perangkat Lunak FSM LAPOR: Sistem Pelaporan Insiden Berbasis Progressive Web App untuk Penguatan Tata Kelola Aset dan Layanan di Fakultas Sains dan Matematika Universitas Diponegoro |
| 2 | Bidang Ilmu | Informatika / Teknologi Informasi dan Komunikasi |
| 3 | Pengusul | |
| | a. Nama Lengkap | Satriawan Rasyid Purnama, S.Kom., M.Cs. |
| | b. NIP/NUPTK | 199805212024061001 / 7853776677130152 |
| | c. H-Indeks Scopus / ID-ORCID | 6 / 0000-0003-3770-8814 |
| | d. Fakultas/Departemen/Lab | FSM / Informatika / Komputasi Visual |
| | e. Pusat Penelitian | Jl. Prof. Soedarto, S.H. Tembalang, Semarang |
| | f. Telepon/Faks (kantor) | (024) 70594104 |
| | g. Telepon/Faks (Rumah) | - |
| | h. HP / E-mail | 085225257551 / satriawanrasyidp@lecturer.undip.ac.id |
| 4 | Jangka Waktu Kegiatan | 12 Bulan |
| 5 | Lokasi Penelitian | Laboratorium Komputasi Visual, Departemen Informatika, FSM Undip |
| 6 | Biaya yang Diperlukan | **Rp 40.000.000,-** (empat puluh juta rupiah) |
| 7 | Sumber Dana | Riset Penugasan Hilirisasi FSM Undip Tahun Anggaran 2026 |

Semarang, ........... 2026

| Menyetujui, | Ketua Pengusul, |
|---|---|
| Dekan FSM UNDIP | |
| | |
| **Prof. Dr. Kusworo Adi, S.Si., M.T.** | **Satriawan Rasyid Purnama, S.Kom., M.Cs.** |
| NIP. 197203171998021001 | NIP. 199805212024061001 |

---

## DAFTAR ISI

- [ABSTRAK](#abstrak)
- [BAB I PENDAHULUAN](#bab-i-pendahuluan)
  - [1.1 Latar Belakang](#11-latar-belakang)
  - [1.2 Hasil Riset Awal (Sumber Hilirisasi)](#12-hasil-riset-awal-sumber-hilirisasi)
  - [1.3 Tujuan Penelitian](#13-tujuan-penelitian)
  - [1.4 Manfaat Penelitian](#14-manfaat-penelitian)
- [BAB II MITRA DAN TARGET PENGGUNAAN](#bab-ii-mitra-dan-target-penggunaan)
  - [2.1 Mitra untuk Hilirisasi](#21-mitra-untuk-hilirisasi)
  - [2.2 Target Penggunaan](#22-target-penggunaan)
  - [2.3 Dampak dan Manfaat Hilirisasi](#23-dampak-dan-manfaat-hilirisasi)
- [BAB III METODOLOGI HILIRISASI](#bab-iii-metodologi-hilirisasi)
  - [3.1 Tahapan Kegiatan](#31-tahapan-kegiatan)
  - [3.2 Metode Pengujian dan Validasi](#32-metode-pengujian-dan-validasi)
  - [3.3 Indikator Kinerja dan Ketercapaian](#33-indikator-kinerja-dan-ketercapaian)
- [BAB IV RENCANA LUARAN](#bab-iv-rencana-luaran)
  - [4.1 Luaran](#41-luaran)
- [BAB V RENCANA ANGGARAN DAN JADWAL PELAKSANAAN](#bab-v-rencana-anggaran-dan-jadwal-pelaksanaan)
  - [5.1 Rencana Anggaran Biaya (RAB)](#51-rencana-anggaran-biaya-rab)
  - [5.2 Jadwal Pelaksanaan (Time Schedule)](#52-jadwal-pelaksanaan-time-schedule)
- [DAFTAR PUSTAKA](#daftar-pustaka)

---

## ABSTRAK

> `[ADAPTASI dari File 2 — Ringkasan/Summary, dimodifikasi ke konteks hilirisasi]`

Pengelolaan insiden dan kondisi aset di lingkungan fakultas saat ini masih menghadapi tantangan berupa proses manual yang tidak terstruktur, ketiadaan sistem pelacakan berbasis bukti foto-geolokasi, serta keterlambatan penanganan akibat tidak adanya mekanisme *Service Level Agreement* (SLA). Permasalahan ini berdampak langsung pada rendahnya akuntabilitas, sulitnya audit riwayat insiden, dan inefisiensi alokasi sumber daya pemeliharaan di Fakultas Sains dan Matematika (FSM) Universitas Diponegoro.

Hilirisasi ini bertujuan membawa prototipe **FSM LAPOR**—sebuah *Progressive Web App* (PWA) berbasis React 18 + Supabase yang mengintegrasikan geolokasi GPS, kamera perangkat, *workflow* multi-role (Pelapor, Pimpinan, Petugas, Superadmin), pelacakan SLA *real-time*, notifikasi *push*, serta modul *Survey Kondisi Aset* berbasis siklus PDCA—dari level riset (TKT 5) menuju level siap operasional institusional (TKT 7). Tahapan hilirisasi mencakup penyempurnaan arsitektur produksi, *pilot deployment* di enam departemen FSM (Informatika, Matematika, Statistika, Fisika, Kimia, Biologi) beserta Tata Usaha Fakultas, pelatihan operator, pendampingan teknis selama 12 bulan, serta validasi *usability* (System Usability Scale ≥ 70) dan performa (Lighthouse Performance ≥ 80). Luaran wajib berupa produk perangkat lunak FSM LAPOR v1.0 yang *deployed* dan operasional, satu publikasi jurnal internasional terindeks Scopus, dan pendaftaran HKI. Proyeksi *Revenue Generating Activity* (RGA) jangka menengah berasal dari replikasi sistem ke fakultas/PTN lain dengan skema sewa-langganan.

**Kata Kunci:** *Progressive Web App*; Sistem Pelaporan Insiden; Geolokasi GPS; Manajemen Aset; *Multi-Role Workflow*; Hilirisasi.

---

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

> `[ADAPTASI dari File 2 — Latar Belakang]`

Transformasi digital di sektor pendidikan tinggi telah menjadi agenda prioritas global. Laporan *E-Government Survey 2024* PBB menegaskan bahwa aksesibilitas layanan publik berbasis digital merupakan indikator utama kematangan tata kelola modern [1]. Studi tentang transformasi digital di Indonesia juga menunjukkan bahwa digitalisasi layanan administrasi meningkatkan efisiensi, transparansi, dan akuntabilitas tata kelola organisasi secara signifikan [13]. Namun di tingkat operasional fakultas/departemen, mekanisme pelaporan insiden atau kerusakan fasilitas umumnya masih dilakukan secara konvensional melalui laporan lisan, *chat* tidak terstruktur, atau formulir fisik.

Ketidakefisienan sistem manual ini berdampak pada lambatnya respons penanganan, lemahnya akuntabilitas, dan sulitnya pelacakan riwayat kondisi aset. Survei terhadap sistem manajemen pengaduan menunjukkan bahwa migrasi ke platform digital meningkatkan transparansi serta efisiensi interaksi pelapor–pengelola [14]. Munoz dkk. [3] melalui tinjauan sistematis 76 studi menyimpulkan bahwa partisipasi pengguna dalam pelaporan masalah infrastruktur meningkat drastis ketika tersedia platform digital yang mudah diakses dan memberikan umpan balik status secara *real-time*.

*Progressive Web App* (PWA) terbukti menjadi solusi pengembangan lintas platform yang ekonomis: mendukung akses *offline*, notifikasi *push*, dan instalasi tanpa toko aplikasi. Tinjauan sistematis Marchetto & Morandini [9] dengan 226 responden mengonfirmasi kemudahan instalasi dan keterlibatan pengguna PWA yang tinggi. Biorn-Hansen dkk. [5] menegaskan keunggulan biaya pengembangan, kemudahan pembaruan, dan jangkauan PWA dibanding aplikasi *native*. Malavolta dkk. [4] menunjukkan PWA dengan *service worker* dapat menyamai performa *native* pada konektivitas terbatas—relevan untuk lingkungan kampus dengan keterbatasan jaringan di area tertentu.

Aspek kritis lain adalah penerapan *Service Level Agreement* (SLA) sebagai kontrol waktu penanganan. Swain & Garza [6] membuktikan faktor kritis pencapaian SLA insiden TI mencakup kejelasan penugasan, eskalasi otomatis, dan visibilitas status *real-time*. Implementasi *Role-Based Access Control* (RBAC) dalam sistem berbasis web meningkatkan keamanan data dan efisiensi alur kerja organisasional [7]. Manajemen kondisi aset menjadi dimensi tambahan; pendekatan PDCA (*Plan-Do-Check-Act*) merupakan kerangka perbaikan berkelanjutan yang diakui untuk pemeliharaan fasilitas [15], sementara Tuhaise dkk. [8] menegaskan kerangka manajemen aset berbasis *digital twin* memungkinkan pemantauan kondisi aset *real-time* dan terdokumentasi—hal yang tidak dapat dipenuhi sistem manual.

> `[BARU — Justifikasi hilirisasi mengikuti pola File 1]`

Hilirisasi sistem **FSM LAPOR** menjadi langkah strategis penguatan infrastruktur digital FSM Undip menuju pengelolaan aset dan layanan berbasis data. Sistem ini merupakan rangkaian *roadmap* riset terapan 2026–2030 di bidang *smart campus services*. Melalui *pilot* di enam departemen FSM dan unit Tata Usaha Fakultas, sistem akan diuji performa teknis, *usability*, dan validitas *workflow*-nya. Dengan pendampingan teknis 12 bulan, hasil pengembangan ditargetkan mencapai TKT 7 dan siap diadopsi secara institusional, sekaligus menjadi model implementasi yang dapat direplikasi ke fakultas lain di Undip dan PTN sejawat.

### 1.2 Hasil Riset Awal (Sumber Hilirisasi)

> `[ADAPTASI dari File 2 — State-of-the-Art & Kebaruan, dikemas sebagai "hasil riset awal" sesuai pola File 1]`

Riset awal yang menjadi dasar hilirisasi ini adalah pengembangan prototipe **FSM LAPOR v0.x** oleh tim peneliti Departemen Informatika FSM Undip pada 2025–2026 dengan judul *“FSM LAPOR: Pengembangan Sistem Pelaporan Insiden Berbasis Progressive Web App pada Fakultas Sains dan Matematika Universitas Diponegoro”*. Prototipe tersebut menghasilkan:

1. Arsitektur PWA berbasis Vite 5 + React 18 + TypeScript di sisi *frontend* dan Supabase (PostgreSQL + Auth + Storage + Realtime) di sisi *backend* sebagai platform BaaS *open-source*.
2. Skema basis data relasional dengan *Row Level Security* (RLS) untuk enkapsulasi hak akses per-*role*, mengimplementasikan prinsip RBAC [7].
3. Modul inti pelaporan insiden berbasis foto + geolokasi GPS, *workflow* lima-state (Dikirim → Diterima → Ditugaskan → Diselesaikan → Diverifikasi), SLA *countdown* dan eskalasi otomatis [6], notifikasi *real-time* via *Supabase Realtime Channels* berbasis WebSocket, serta modul *Survey Kondisi Aset* siklus PDCA [15].
4. Validasi awal pada lingkup Departemen Informatika menunjukkan kelayakan teknis sebagai PWA *installable* dan *offline-capable*.

Prototipe ini memiliki **kebaruan** berupa integrasi tunggal: pelaporan foto-GPS, *workflow* multi-role + SLA tracking, notifikasi *push real-time*, dan modul *survey* aset PDCA dalam satu PWA institusional [3], [9], [12]; serta arsitektur BaaS-Supabase + RLS PostgreSQL untuk pelaporan institusional yang belum terdokumentasi luas secara akademis. Riset terkait tim peneliti yang turut menjadi penguat keyakinan hilirisasi mencakup studi pelaporan keluhan berbasis *deep learning* [12] dan tinjauan PWA [4], [5], [9], [19].

Hilirisasi pada proposal ini diarahkan untuk: (a) memperluas cakupan dari satu departemen menjadi seluruh FSM (6 departemen + Tata Usaha Fakultas), (b) penguatan keamanan & keandalan produksi (RLS lanjutan, *audit trail*, *backup* otomatis), (c) integrasi dashboard analitik lintas departemen, (d) pelatihan operator, dan (e) pendampingan operasional 12 bulan untuk mencapai **TKT 7**.

### 1.3 Tujuan Penelitian

> `[ADAPTASI rumusan masalah File 2 → Tujuan hilirisasi pola File 1]`

Tujuan hilirisasi ini meliputi:

1. Mengembangkan dan menyempurnakan produk perangkat lunak **FSM LAPOR** sebagai PWA siap-produksi yang mendukung pelaporan insiden berbasis foto + geolokasi GPS secara *real-time*.
2. Mendesain dan mengimplementasikan arsitektur sistem yang terdiri dari **PWA Frontend Engine**, **Supabase Backend & API Engine**, dan **Dashboard Analytics Engine** untuk mendukung integrasi data, keamanan (RLS), dan kemudahan akses bagi tiap departemen di FSM.
3. Melakukan uji validasi teknis terhadap performa sistem meliputi *response time*, kestabilan *realtime channel*, akurasi GPS/kamera, serta keandalan SLA *tracking* dan eskalasi otomatis.
4. Mengimplementasikan sistem secara bertahap pada **6 departemen FSM** (Informatika, Matematika, Statistika, Fisika, Kimia, Biologi) dan **Tata Usaha Fakultas FSM**, termasuk pelatihan operator dan pendampingan teknis.
5. Menyusun dokumentasi teknis, panduan pengguna (*user manual*), dan standar operasional prosedur (SOP) untuk mendukung keberlanjutan dan skalabilitas implementasi.
6. Mencapai **Tingkat Kesiapan Teknologi (TKT) 7** sebagai indikator kesiapan produk untuk digunakan secara institusional di FSM Undip.
7. Menyusun model hilirisasi berkelanjutan yang dapat direplikasi ke fakultas lain di Undip maupun perguruan tinggi lain di Indonesia.

### 1.4 Manfaat Penelitian

> `[BARU — diturunkan dari File 1 §1.4 dengan substansi FSM LAPOR]`

- Memberikan kontribusi ilmiah dalam penerapan PWA, RBAC berbasis RLS, dan siklus PDCA untuk tata kelola aset institusi pendidikan tinggi.
- Menghasilkan sistem perangkat lunak inovatif yang mempersingkat siklus pelaporan–penanganan insiden dan meningkatkan akuntabilitas pemeliharaan fasilitas FSM.
- Mendukung kebijakan *data-driven faculty* melalui dashboard yang menampilkan tren insiden, *SLA compliance*, dan kondisi aset lintas departemen secara *real-time*.
- Menjadi produk hilirisasi riset terapan informatika yang dapat diadopsi fakultas lain sebagai model sistem pelaporan institusional.
- Meningkatkan kapasitas analisis data dan kesiapan digital unit kerja (Tata Usaha, Sub-bagian Umum & BMN, Pimpinan Departemen) untuk merespons isu pemeliharaan secara cepat dan berbasis bukti.
- Memperkuat infrastruktur layanan FSM melalui sistem pelaporan terpusat dengan mekanisme eskalasi otomatis.
- Memberikan manfaat sosial-kelembagaan: meningkatkan transparansi, akuntabilitas, dan kepercayaan civitas akademika terhadap layanan fakultas.
- Mendorong ekosistem inovasi berkelanjutan di bidang informatika yang menghubungkan riset akademik dengan kebutuhan riil institusi.

---

## BAB II MITRA DAN TARGET PENGGUNAAN

### 2.1 Mitra untuk Hilirisasi

> `[BARU — pola File 1 §2.1, disesuaikan ke konteks FSM]`

Hilirisasi FSM LAPOR dilaksanakan melalui kemitraan strategis pada dua sisi:

**Sisi penyedia data & infrastruktur teknis:**
- **Supabase** (PostgreSQL + Auth + Storage + Realtime) sebagai *Backend-as-a-Service* utama.
- **Vercel / Cloudflare Pages** sebagai *hosting* PWA *frontend* dengan dukungan *edge network*.
- **Layanan notifikasi *web push*** (mis. Firebase Cloud Messaging atau OneSignal) untuk *push notification* lintas perangkat.
- **PT/registrar domain `.id`** untuk penyediaan domain institusional dan *SSL certificate*.

**Sisi pengguna institusional (mitra utama hilirisasi di FSM Undip):**
- **Dekanat FSM Undip** (cq. Wakil Dekan Bidang II/Sumber Daya) sebagai *executive sponsor*.
- **6 Departemen di FSM:** Informatika, Matematika, Statistika, Fisika, Kimia, Biologi.
- **Tata Usaha Fakultas FSM** dan **Sub-bagian Umum & BMN** sebagai pemilik *workflow* pemeliharaan, aset, dan logistik.
- **Unit Pemeliharaan/Layanan Teknis FSM** sebagai *end user* role *Petugas*.
- **Koordinator Laboratorium di tiap departemen** sebagai *power user* untuk *Survey Kondisi Aset*.

Dengan model multipihak ini, hilirisasi diharapkan memperkuat ekosistem riset terapan FSM melalui sinergi akademisi, penyedia teknologi, dan pengambil kebijakan di tingkat fakultas.

### 2.2 Target Penggunaan

> `[BARU — pola File 1 §2.2, peran user diambil dari File 2]`

Produk **FSM LAPOR** ditargetkan menjadi infrastruktur strategis FSM Undip untuk pengelolaan insiden, layanan, dan kondisi aset berbasis data. Sistem dirancang untuk empat *role* utama:

| Role | Pengguna Utama | Fungsi Utama |
|------|----------------|--------------|
| **Pelapor** | Dosen, mahasiswa, tendik FSM | Membuat laporan insiden dengan foto + GPS, memantau status, memberi verifikasi penyelesaian. |
| **Pimpinan** | Kadep, Sekdep, KTU, Pimpinan Fakultas | Menerima laporan, men-*disposisi* ke Petugas, memantau dashboard dan *SLA compliance*. |
| **Petugas** | Unit Pemeliharaan, teknisi laboratorium | Mengeksekusi penanganan, mengunggah bukti penyelesaian, memperbarui status. |
| **Superadmin** | Tim TI Fakultas / Tim Hilirisasi | Mengelola *master data*, *role*, kategori insiden, target SLA, audit *trail*. |

Target penggunaan jangka pendek adalah enam departemen FSM + Tata Usaha Fakultas. Target jangka menengah adalah replikasi ke fakultas lain di Undip, sementara jangka panjang adalah model rujukan nasional sistem pelaporan insiden + manajemen aset berbasis PWA untuk PTN/PTS lain.

### 2.3 Dampak dan Manfaat Hilirisasi

> `[BARU — pola File 1 §2.3]`

- **Kelembagaan:** FSM memiliki infrastruktur digital terintegrasi untuk pelaporan insiden, eskalasi otomatis berbasis SLA, dan pemantauan kondisi aset yang terdokumentasi siklus PDCA.
- **Operasional:** Pimpinan dan Tata Usaha memperoleh *dashboard real-time* (jumlah laporan, *SLA compliance rate*, kategori insiden dominan, kondisi aset per departemen) untuk pengambilan keputusan berbasis data; tim Petugas memperoleh sistem penugasan yang transparan dengan *audit trail*.
- **Akademik:** Memperkuat kapasitas riset terapan Departemen Informatika dalam pengembangan PWA, BaaS-architecture, dan *workflow engineering* untuk konteks lokal Indonesia; menghasilkan publikasi jurnal internasional terindeks Scopus.
- **Civitas Akademika:** Meningkatkan kepuasan layanan, transparansi penanganan keluhan, dan rasa kepemilikan terhadap fasilitas fakultas.
- **Jangka Panjang:** Menjadi model nasional sistem *smart-campus reporting* berbasis PWA, mendukung kolaborasi lintas-PTN, dan memperkuat peran FSM Undip sebagai pionir hilirisasi informatika untuk tata kelola fakultas modern.

---

## BAB III METODOLOGI HILIRISASI

### 3.1 Tahapan Kegiatan

> `[ADAPTASI dari File 2 — Metode/Methods, dipetakan ulang sebagai 5 tahap hilirisasi pola File 1 §3.1]`

Hilirisasi dilakukan melalui lima tahapan utama:

1. **Penyempurnaan Desain Sistem dan Arsitektur Teknis.** Evaluasi prototipe v0.x dan penyempurnaan arsitektur agar memenuhi standar produksi: *hardening* RLS PostgreSQL, *audit trail* lengkap, *backup* terjadwal, *observability* (log + metrik), dan *service worker* PWA untuk *offline capability* + *auto-update*. Arsitektur final mencakup tiga komponen: **PWA Frontend Engine** (Vite 5 + React 18 + TypeScript), **Supabase Backend & API Engine** (PostgreSQL + Auth + Storage + Realtime + RLS), dan **Dashboard Analytics Engine** (visualisasi tren insiden, SLA, dan kondisi aset).
2. **Pengembangan dan Integrasi Skala Fakultas.** Pengembangan modul level produksi dalam tiga *sprint* iteratif:
   - *Sprint* 1: autentikasi multi-role, manajemen laporan inti, integrasi Geolocation API, akses kamera perangkat.
   - *Sprint* 2: *workflow* lima-state + multi-*assignee*, SLA *tracking* + eskalasi otomatis, notifikasi *real-time* via *Supabase Realtime Channels* + *web push*.
   - *Sprint* 3: modul *Survey Kondisi Aset* PDCA, *dashboard* statistik & analitik lintas departemen, *master data management*, konfigurasi PWA (*service worker*, *manifest*, *auto-update*).
3. **Uji Coba dan Validasi Fungsional (*Pilot Test*).** *Pilot deployment* di 6 departemen FSM + Tata Usaha Fakultas. Kegiatan: pelatihan operator, uji *dashboard*, pengujian kecepatan pemrosesan, validasi kesesuaian *workflow* dengan praktik nyata.
4. **Validasi Model Bisnis dan Mekanisme Pemanfaatan.** Penyusunan model operasional di FSM: skema pemeliharaan, kontrol akses, mekanisme pendanaan tahunan, serta perhitungan proyeksi RGA untuk replikasi ke fakultas/PTN lain.
5. **Perizinan dan Dokumentasi Teknis.** Dokumentasi teknis (SRS sesuai IEEE 830, ADR, *deployment guide*), laporan hasil uji coba, penyelarasan kebijakan keamanan & privasi (PDP) sesuai pedoman Undip, serta pengajuan HKI.

### 3.2 Metode Pengujian dan Validasi

> `[ADAPTASI dari File 2 — Pengujian SUS + Lighthouse + black-box, dilengkapi pola File 1 §3.2]`

1. **Uji Teknis dan Performa Sistem.** Pengukuran *response time* API & *realtime channel*, stabilitas server Supabase, efisiensi *bundle* PWA, dan *offline capability* via simulasi *network throttling*. Skor **Google Lighthouse Performance ≥ 80** ditetapkan sebagai ambang.
2. **Uji Validasi Akurasi Fungsional.** *Black-box testing* terhadap seluruh *use-case* SRS (alur lima-state untuk empat *role*), validasi akurasi geolokasi GPS, dan validasi mekanisme eskalasi SLA dengan dataset skenario sintetis.
3. **Uji Coba Lapangan (*Pilot Implementation*).** Implementasi di 6 departemen FSM + Tata Usaha Fakultas. *Usability* diuji menggunakan **System Usability Scale (SUS)** [17], [18] dengan minimal 25 responden mewakili keempat *role*; ambang **SUS ≥ 70** (grade C/*acceptable*).
4. **Uji Keamanan dan Keandalan Sistem.** Penilaian autentikasi (Supabase Auth), kontrol akses berbasis RLS PostgreSQL [7], proteksi data sensitif (foto bukti, lokasi GPS), serta pengujian *backup-restore*.

### 3.3 Indikator Kinerja dan Ketercapaian

> `[BARU — pola File 1 §3.3, target disesuaikan FSM LAPOR & pagu 40 jt]`

| No | Indikator | Target |
|----|-----------|--------|
| 1 | Tingkat Kesiapan Teknologi (TKT) | Naik dari **TKT 5 → TKT 7** |
| 2 | Cakupan implementasi | Minimal **6 departemen FSM + Tata Usaha Fakultas** |
| 3 | *Usability* (SUS) | **≥ 70** (acceptable) |
| 4 | Performa PWA (Lighthouse) | Performance ≥ 80; Accessibility ≥ 90; Best Practices ≥ 90 |
| 5 | *Response time* API | < 1 detik (p95) untuk operasi CRUD utama |
| 6 | *SLA compliance rate* pasca-implementasi | ≥ 80% laporan tertangani sesuai SLA |
| 7 | Dokumentasi & SOP | SRS (IEEE 830), *user manual* per-role, SOP operasional, *deployment guide* |
| 8 | Luaran wajib | 1 publikasi jurnal internasional terindeks Scopus, 1 produk PWA *deployed*, 1 HKI |

---

## BAB IV RENCANA LUARAN

### 4.1 Luaran

> `[BARU — pola File 1 §4.1, jenis produk diturunkan dari File 2]`

Produk yang dikembangkan adalah perangkat lunak **FSM LAPOR**—Sistem Pelaporan Insiden & Manajemen Aset berbasis *Progressive Web App*—yang berfungsi sebagai infrastruktur digital fakultas untuk pengelolaan insiden, eskalasi berbasis SLA, dan pemantauan kondisi aset.

| No | Jenis Produk | Fungsi Utama |
|----|--------------|--------------|
| 1 | **PWA Pelaporan Insiden FSM LAPOR** | Memungkinkan civitas akademika FSM membuat laporan insiden berbasis foto + geolokasi GPS, memantau status secara *real-time*, dan menerima notifikasi *push* untuk perubahan status. |
| 2 | **Dashboard Manajemen & Analitik FSM LAPOR** | Menggabungkan data laporan, SLA, dan *survey* aset PDCA dari seluruh departemen FSM ke dalam satu *dashboard* interaktif: tren insiden, *SLA compliance*, kondisi aset per-departemen, serta *audit trail* lengkap untuk pengambilan keputusan strategis pimpinan fakultas. |

**Daftar Luaran:**

| Kategori | Luaran |
|----------|--------|
| **Luaran Wajib** | (1) Produk perangkat lunak **FSM LAPOR v1.0** *deployed* dan operasional di 6 departemen FSM + Tata Usaha Fakultas; (2) Laporan teknis hilirisasi (arsitektur, hasil validasi, *deployment guide*); (3) Laporan penerapan & uji coba lapangan; (4) Panduan pengguna (*user manual*) per-role + SOP institusional; (5) Laporan evaluasi performa & umpan balik pengguna (SUS + Lighthouse). |
| **Luaran Tambahan** | (1) **Publikasi jurnal internasional terindeks Scopus** (target: jurnal Q3/Q2 di bidang *software engineering* / *information systems*); (2) Pendaftaran **HKI** untuk perangkat lunak FSM LAPOR; (3) Proyeksi **RGA** dari skema replikasi/sewa-langganan: estimasi **Rp 5.000.000/fakultas/tahun × 10 fakultas = Rp 50.000.000/tahun** sebagai potensi pendapatan jangka menengah pasca-hilirisasi. |

---

## BAB V RENCANA ANGGARAN DAN JADWAL PELAKSANAAN

### 5.1 Rencana Anggaran Biaya (RAB)

> `[BARU — disusun untuk pagu Rp 40.000.000 dengan pengusul tunggal Satriawan Rasyid Purnama, mengikuti format File 1 §5.1]`

#### A. BELANJA PERSONIL (Honorarium Asisten/Mahasiswa Pembantu)

| No | Uraian | Volume | Satuan | Harga Satuan (Rp) | Jumlah (Rp) |
|----|--------|-------:|--------|------------------:|------------:|
| 1 | Honorarium asisten *Frontend Developer* (PWA React/TypeScript) | 240 | OJ | 25.000 | 6.000.000 |
| 2 | Honorarium asisten *Backend Developer* (Supabase/PostgreSQL/RLS) | 240 | OJ | 25.000 | 6.000.000 |
| 3 | Honorarium asisten *QA & UI/UX Tester* | 160 | OJ | 25.000 | 4.000.000 |
| 4 | Honorarium asisten *Helpdesk, Pelatihan & Sosialisasi* | 160 | OJ | 25.000 | 4.000.000 |
| | **Sub Total A** | | | | **20.000.000** |

> Total volume: **800 OJ** untuk 4 mahasiswa pembantu (≈ tarif standar mahasiswa pembantu peneliti FSM).

#### B. BELANJA OPERASIONAL

| No | Uraian | Volume | Satuan | Harga Satuan (Rp) | Jumlah (Rp) |
|----|--------|-------:|--------|------------------:|------------:|
| 1 | Supabase Pro (Auth + DB + Storage + Realtime) — *backend* produksi | 12 | bulan | 600.000 | 7.200.000 |
| 2 | Hosting PWA *frontend* (Vercel/Cloudflare Pages tier produksi) | 12 | bulan | 250.000 | 3.000.000 |
| 3 | Domain `.id` + SSL Certificate | 1 | tahun | 500.000 | 500.000 |
| 4 | Layanan *Web Push Notification* (FCM/OneSignal) | 12 | bulan | 200.000 | 2.400.000 |
| 5 | UI library/template & *icon set* berlisensi | 1 | paket | 1.500.000 | 1.500.000 |
| 6 | Workshop & pelatihan operator (6 departemen + Tata Usaha) | 7 | paket | 350.000 | 2.450.000 |
| 7 | ATK, *print* & jilid laporan/SOP/*user manual* | 1 | paket | 950.000 | 950.000 |
| 8 | Transportasi & koordinasi lapangan (*pilot* 6 departemen) | 1 | paket | 1.000.000 | 1.000.000 |
| 9 | Biaya publikasi jurnal internasional terindeks Scopus (APC) | 1 | kali | 1.000.000 | 1.000.000 |
| | **Sub Total B** | | | | **20.000.000** |

> Catatan: Biaya APC publikasi sebesar Rp 1.000.000 ditujukan sebagai *seed funding* (translasi profesional / *proofreading* + biaya submission jurnal Q3 *open-access* berbiaya rendah / co-funding); selisih APC penuh dialokasikan dari hibah lain bila diperlukan.

#### REKAPITULASI

| No | Komponen | Jumlah (Rp) | Persentase |
|----|----------|------------:|-----------:|
| A | Belanja Personil (Honorarium) | 20.000.000 | 50% |
| B | Belanja Operasional | 20.000.000 | 50% |
| | **TOTAL KESELURUHAN** | **40.000.000** | **100%** |

### 5.2 Jadwal Pelaksanaan (Time Schedule)

> `[BARU — pola File 1 §5.2, dipetakan ke 5 tahapan §3.1]`

Legenda: `■` = bulan aktif kegiatan.

| No | Kegiatan | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 | B11 | B12 |
|----|----------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|
| 1 | Penyempurnaan desain sistem & arsitektur teknis (*hardening* RLS, *audit trail*, *service worker*) | ■ | ■ | | | | | | | | | | |
| 2 | Pengembangan & integrasi skala fakultas (Sprint 1–3: PWA, *workflow*, SLA, *push*, dashboard, *survey* PDCA) | | ■ | ■ | ■ | ■ | | | | | | | |
| 3 | Uji coba & validasi fungsional (*pilot* di 6 departemen FSM + Tata Usaha Fakultas) | | | | | ■ | ■ | ■ | | | | | |
| 4 | Pendampingan operasional & evaluasi performa (SUS, Lighthouse, *SLA compliance*) | | | | | | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| 5 | Dokumentasi teknis (SRS IEEE 830, *user manual*, SOP, *deployment guide*) | | | | ■ | ■ | ■ | ■ | | | | | |
| 6 | Penyusunan laporan akhir, publikasi jurnal Scopus, pengajuan HKI, & proyeksi RGA | | | | | | | | ■ | ■ | ■ | ■ | ■ |

---

## DAFTAR PUSTAKA

> `[ADAPTASI dari File 2 — daftar pustaka direlokasi ke konteks hilirisasi; nomor sitasi mengikuti urutan kemunculan di dokumen ini.]`

[1] United Nations, *E-Government Survey 2024: Accelerating Digital Transformation for Sustainable Development*, United Nations Department of Economic and Social Affairs, New York, 2024.

[2] H. Phour, D. Sharma, and N. S. Talwandi, “Crowdsourcing Applications in Smart Cities,” in *Intelligent Systems Design and Applications. ISDA 2023*, Lecture Notes in Networks and Systems, vol. 1049, A. Abraham et al., Eds. Cham: Springer, 2024, pp. 25–36. doi: 10.1007/978-3-031-64779-6_3.

[3] P. Munoz, S. Casademont, and F. Marques, “Smart City Applications to Promote Citizen Participation in City Management and Governance: A Systematic Review,” *Informatics*, vol. 9, no. 4, p. 89, Oct. 2022. doi: 10.3390/informatics9040089.

[4] I. Malavolta, G. Procaccianti, P. Noorland, and P. Vukmirovic, “Assessing the Impact of Service Workers on the Energy Efficiency of Progressive Web Apps,” in *Proc. 2017 IEEE/ACM 4th Int. Conf. Mobile Software Engineering and Systems (MOBILESoft)*, IEEE, 2017, pp. 35–45.

[5] A. Biorn-Hansen, T. A. Majchrzak, and T.-M. Gronli, “Progressive Web Apps: The Possible Web-native Unifier for Mobile Development,” in *Proc. 13th Int. Conf. Web Information Systems and Technologies (WEBIST)*, 2017, pp. 344–351. doi: 10.5220/0006728803440351.

[6] A. K. Swain and V. R. Garza, “Key Factors in Achieving Service Level Agreements (SLA) for Information Technology (IT) Incident Resolution,” *Information Systems Frontiers*, vol. 25, no. 2, pp. 819–834, 2023. doi: 10.1007/s10796-022-10266-5.

[7] Z. M. Iqal, A. Selamat, and O. Krejcar, “A Comprehensive Systematic Review of Access Control in IoT: Requirements, Technologies, and Evaluation Metrics,” *IEEE Access*, vol. 12, pp. 12636–12654, 2024. doi: 10.1109/ACCESS.2023.3347495.

[8] V. V. Tuhaise, J. H. M. Tah, and F. H. Abanda, “Technologies for Digital Twin Applications in Construction,” *Automation in Construction*, vol. 152, p. 104931, Aug. 2023. doi: 10.1016/j.autcon.2023.104931.

[9] T. Marchetto and M. Morandini, “User Perceptions of Progressive Web App Features: An Analytical Approach and a Systematic Literature Review,” in *Proc. 9th Int. Congr. Information and Communication Technology (ICICT 2024)*, Lecture Notes in Networks and Systems, vol. 1001. Singapore: Springer, 2024, pp. 163–172. doi: 10.1007/978-981-97-4581-4_14.

[10] M. Pan, “Prototyping Methods: Techniques and its Significance,” *Journal of Research and Development*, vol. 11, p. 216, Jun. 2023.

[11] M. Pan, “Prototyping Methods: Techniques and its Significance,” *J. Res. Dev.*, vol. 11, p. 216, Jun. 2023. doi: 10.35248/2311-3278.23.11.216.

[12] F. Shama, A. Aziz, and L. B. M. Deya, “CitySolution: A Complaining Task Distributive Mobile Application for Smart City Corporation Using Deep Learning,” *arXiv preprint* arXiv:2410.12882, 2024.

[13] M. Sebő and G. Bel, “E-Government and Provision of Public Services: Economic, Social, and Political Determinants of Citizen Complaints,” *International Public Management Journal*, vol. 27, no. 4, pp. 659–679, 2024. doi: 10.1080/10967494.2023.2273343.

[14] D. A. Puspitasari and T. Kurniawan, “Assessing the National Complaint Handling System in Indonesia (LAPOR!) Using the Design-Reality Gap Model,” *International Journal of Electronic Governance*, vol. 15, no. 2, pp. 118–134, 2023. doi: 10.1504/IJEG.2023.132329.

[15] E. Üstündağlı Erten, “Complaint Management through the E-State Portal: Is Digitalization Actually Beneficial?” *Proceedings*, vol. 101, no. 1, p. 1, 2024. doi: 10.3390/proceedings2024101001.

[16] D. Kumar et al., “Digital Twins in the Construction Industry: A Comprehensive Review of Current Implementations, Enabling Technologies, and Future Directions,” *Sustainability*, vol. 15, no. 14, p. 10908, 2023. doi: 10.3390/su151410908.

[17] P. Vlachogianni and N. Tselios, “Perceived Usability Evaluation of Educational Technology Using the System Usability Scale (SUS): A Systematic Review,” *Journal of Research on Technology in Education*, vol. 54, no. 3, pp. 394–410, 2022. doi: 10.1080/15391523.2020.1867938.

[18] O. Suria, “A Statistical Analysis of System Usability Scale (SUS) Evaluations in Online Learning Platform,” *Journal of Information Systems and Informatics*, vol. 6, no. 2, pp. 992–1007, 2024. doi: 10.51519/journalisi.v6i2.750.

[19] S. Huber, L. Demetz, and M. Felderer, “A Comparative Study on the Energy Consumption of Progressive Web Apps,” *Information Systems*, vol. 108, p. 102017, Sep. 2022. doi: 10.1016/j.is.2022.102017.

---

> **Akhir Dokumen.**
> Dokumen ini disusun sebagai hasil sinkronisasi antara struktur *Proposal Hilirisasi Informatika* (File 1) dan substansi *Draft-Lapor-FSM* (File 2). Bagian ber-tanda `[BARU]` (mitra fakultas, RAB, jadwal hilirisasi, indikator kinerja, manfaat, dampak) disusun khusus untuk menyesuaikan pagu Rp 40.000.000 dan pengusul tunggal Satriawan Rasyid Purnama, S.Kom., M.Cs.
