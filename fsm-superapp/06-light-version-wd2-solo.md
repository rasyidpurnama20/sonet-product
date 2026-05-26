# 🪶 FSM Super Apps — Versi Light: WD II Solo + AI + $200
## Strategi Realistis untuk 1 Orang Non-Developer dengan Budget Terbatas

> **Konteks:** Anda WD II, tidak bisa coding, budget AI $200/bulan, FSM punya server sendiri, SSO UNDIP hanya untuk auth, tidak ada data dari sistem UNDIP lain, staf lama 2 tahun tidak produktif → Anda memilih kerja dengan AI saja.  
> **Filosofi:** *Bukan yang paling canggih — tapi yang paling jadi.*

---

## 🧠 Reframing Masalah

**Yang salah sebelumnya bukan idenya — tapi pendekatannya.**

| Pendekatan Lama (Gagal) | Pendekatan Baru (Realistis) |
|---|---|
| Tim besar + rapat + dokumen panjang | WD II + AI, eksekusi langsung |
| Tunggu data lengkap dari UNDIP | Mulai dari data yang bisa dikumpulkan sendiri |
| Bangun custom sistem dari nol | Pakai tools yang sudah jadi, konfigurasi saja |
| Semua fitur sekaligus | 1 modul, 1 masalah, 1 bulan |
| Butuh approval banyak pihak | Buat dulu, tunjukkan hasilnya, approval belakangan |

---

## 💡 Prinsip Kerja: WD II + AI

```
Anda sebagai WD II berperan sebagai:
  ✅ Product Owner → yang tahu masalahnya
  ✅ Pengambil keputusan → yang approve semua hal
  ✅ Tester → yang coba dan beri feedback
  ✅ "CEO" produk → yang komunikasi ke civitas

AI berperan sebagai:
  ✅ Developer → tulis kode, konfigurasi sistem
  ✅ Designer → buat tampilan, alur sistem
  ✅ Analyst → analisis data, buat laporan
  ✅ Konsultan → saran teknis, strategi
  ✅ Operator → bantu buat konten, dokumen, SOP
```

**Cara kerja:** Anda ceritakan masalah → AI buatkan solusinya → Anda jalankan di server FSM → selesai.

---

## 💰 Alokasi Budget $200/Bulan

| Tool AI | Fungsi | Biaya/Bulan |
|---|---|---|
| **Claude Pro (Anthropic)** | Developer utama — tulis kode, analisis, strategi | $20 |
| **ChatGPT Plus** | Backup + image generation untuk UI mockup | $20 |
| **Cursor AI** (IDE berbasis AI) | Editor kode dengan AI copilot — deploy ke server FSM | $20 |
| **Windsurf / Bolt.new** | Bangun halaman web/app dengan prompt saja | $20 |
| **Make.com** (automation) | Hubungkan form → notifikasi WA → spreadsheet | $9 |
| **Fonnte / Wablas** | WhatsApp API untuk notifikasi | $10–15 |
| **Supabase** (database cloud) | Database gratis tier, bisa self-host di server FSM | $0 (free tier) |
| **Vercel / Coolify** (hosting) | Deploy app ke server FSM dengan mudah | $0 (self-host) |
| **Buffer sisa** | Untuk tools trial, domain, kebutuhan tak terduga | ~$96–101 |
| **Total** | | **≤ $200** |

> 💡 **Kunci:** Anda tidak perlu semua ini sekaligus. Bulan pertama cukup Claude Pro + Make.com + Fonnte = $44. Sisanya dikembangkan sesuai kebutuhan.

---

## 🔐 Tentang SSO UNDIP — Apa yang Bisa & Tidak Bisa

**Yang BISA dilakukan dengan SSO:**
- ✅ Login pengguna terverifikasi (dosen, mahasiswa, tendik) tanpa buat sistem akun sendiri
- ✅ Tahu identitas pengguna: nama, NIM/NIP, email institusi, status aktif
- ✅ Role sederhana bisa di-assign manual setelah login pertama (teknisi, admin, dll)

**Yang TIDAK BISA didapat dari SSO:**
- ❌ Jadwal kuliah dari SIAP/SIAK
- ❌ Data kepegawaian lengkap
- ❌ Data akademik mahasiswa
- ❌ Data keuangan

**Solusi praktis:** Setelah pengguna login via SSO pertama kali → sistem simpan profilnya → Anda (WD II) assign role manual lewat panel admin sederhana. Selesai. Tidak perlu API apapun.

---

## 🗂️ Data yang Bisa Dikumpulkan SENDIRI (Tanpa UNDIP)

Ini yang membuat proyek ini bisa jalan tanpa bergantung ke siapapun:

| Data | Cara Kumpulkan | Waktu |
|---|---|---|
| Daftar ruangan & kapasitas | Jalan keliling, catat sendiri atau minta 1 staf foto & isi Google Form | 1–2 hari |
| Daftar teknisi & nomor WA | Tanya langsung ke Kepala TU, sudah ada pasti | 1 jam |
| Kategori kerusakan umum | Pikiran sendiri + 15 menit diskusi dengan 1 teknisi | 30 menit |
| Jadwal ruangan kosong | Input manual per semester oleh admin — 2–3 jam kerja | 1 hari |
| Daftar aset prioritas | Minta laboran isi Google Sheet — aset mahal dulu | 1 minggu |

**Total waktu persiapan data: ±1 minggu, tanpa butuh IT UNDIP.**

---

## 🏗️ Stack Teknologi (Semua Jalan di Server FSM)

```
Server FSM yang sudah ada
│
├── Coolify (panel deploy — seperti cPanel tapi modern, gratis)
│   ├── Aplikasi Web (dibangun oleh AI, Anda deploy 1x klik)
│   ├── Supabase self-hosted (database + auth)
│   └── n8n self-hosted (automation workflow, gratis)
│
├── SSO UNDIP (hanya untuk login)
│
└── WhatsApp via Fonnte (notifikasi keluar)
```

**Cara setup:** Anda ceritakan ke AI "saya punya server dengan IP xxx, OS Ubuntu" → AI berikan perintah copy-paste untuk install Coolify → selesai dalam 30 menit.

---

## 📋 Fitur yang REALISTIS dengan Setup Ini

### Yang JALAN dalam 30 hari pertama

Pilih **1 modul saja** untuk mulai. Rekomendasi: **Maintenance Ticketing** — karena:
- Pain point paling nyata & langsung terasa
- Tidak butuh data kompleks
- Pengguna (pelapor) tidak perlu training — cukup klik form
- Hasilnya langsung kelihatan dalam minggu pertama

**Fitur minimal yang langsung bikin dampak:**

| # | Fitur | Cara Buatnya dengan AI | Waktu Build |
|---|---|---|---|
| 1 | Form laporan kerusakan (web) | Prompt ke Bolt.new/v0.dev → jadi dalam 10 menit | 1 hari |
| 2 | Upload foto kerusakan | AI tambahkan komponen upload ke form | + 30 menit |
| 3 | Notifikasi WA ke teknisi | Make.com → Fonnte, no-code | 2 jam |
| 4 | Status tiket (spreadsheet-backed) | Google Sheets sebagai database awal | 1 jam |
| 5 | Link tiket bisa dibagikan via WA | Auto-generate link per tiket | 1 hari |
| 6 | Login via SSO UNDIP | AI konfigurasikan OAuth2 ke SSO | 2–4 jam |

**Total: sistem ticketing jalan dalam 3–5 hari kerja.**

---

## 🔍 SWOT — Kondisi Anda Sekarang

### Strengths
| # | Kekuatan | Implikasi Strategis |
|---|---|---|
| S1 | WD II sebagai pengambil keputusan tunggal | Tidak ada rapat, tidak ada menunggu approval — eksekusi cepat |
| S2 | Server FSM sudah ada | Tidak perlu keluar biaya hosting, data tersimpan di kampus |
| S3 | SSO UNDIP tersedia untuk auth | Tidak perlu buat sistem login sendiri |
| S4 | AI 2025 sudah bisa build app tanpa developer | Barrier teknis hampir hilang |
| S5 | Masalah operasional nyata & urgent | Pengguna akan adopt karena butuh, bukan karena dipaksa |
| S6 | Budget $200 cukup untuk MVP solid | Tidak perlu anggaran besar untuk mulai |

### Weaknesses
| # | Kelemahan | Cara Atasi |
|---|---|---|
| W1 | Tidak bisa coding → tidak bisa debug sendiri | Semua debugging via AI, dokumentasikan error → paste ke AI |
| W2 | Tidak ada data awal dari UNDIP | Kumpulkan data minimal sendiri — cukup untuk MVP |
| W3 | Staf tidak reliable (pengalaman 2 tahun gagal) | Jangan bergantung staf untuk develop — hanya untuk input data |
| W4 | Waktu WD II terbatas (banyak tugas lain) | Maksimal 1–2 jam/hari untuk proyek ini, AI yang kerja |
| W5 | Jika server FSM bermasalah, tidak ada support | Buat backup ke cloud murah (Hetzner $5/bulan) |

### Opportunities
| # | Peluang | Cara Manfaatkan |
|---|---|---|
| O1 | AI coding makin powerful tiap bulan | Fitur yang sekarang susah, 6 bulan lagi bisa dibuat AI sendiri |
| O2 | WhatsApp penetration 100% di civitas FSM | Channel notifikasi gratis, semua orang sudah punya |
| O3 | No-code tools makin matang | Beberapa fitur Advanced bisa dibuat tanpa kode sama sekali |
| O4 | Quick win bisa jadi argumen ke Dekan untuk anggaran lebih | Tunjukkan sistem jalan → minta budget lebih untuk pengembangan |
| O5 | Bisa jadi pilot project yang dilirik UNDIP pusat | Kalau berhasil, bisa scale ke seluruh UNDIP |

### Threats
| # | Ancaman | Mitigasi |
|---|---|---|
| T1 | Server FSM tidak stabil / tidak ada sysadmin | Identifikasi 1 orang yang pegang server (pasti ada) — minta nomor WA-nya |
| T2 | Pengguna tidak mau adopt | Wajibkan 1 jalur saja dulu — laporan kerusakan hanya via sistem |
| T3 | Proyek mati kalau Anda tidak jadi WD II lagi | Buat dokumentasi + SK dari sekarang |
| T4 | AI memberikan kode yang error dan tidak bisa diperbaiki | Pakai tools AI yang ada preview langsung (Bolt.new, v0.dev) |
| T5 | Budget $200 habis sebelum sistem stabil | Prioritaskan tools yang ada free tier, bayar hanya yang krusial |

---

## 👥 RACI — Versi Solo

> Karena Anda kerja hampir sendiri, RACI ini sederhana tapi penting untuk klarifikasi siapa mengerjakan apa.

| Aktivitas | WD II (Anda) | AI (Claude/etc) | 1 Staf Input Data | Teknisi/Laboran |
|---|---|---|---|---|
| Tentukan fitur apa yang dibuat | **A/R** | C | I | C |
| Tulis kode & konfigurasi sistem | I | **R** | — | — |
| Review & test sistem | **A/R** | C | I | C |
| Input data master (ruang, aset) | C | I | **R** | C |
| Operasional harian (laporan masuk) | I | — | C | **R/A** |
| Update status tiket | I | — | C | **R/A** |
| Maintenance server | **A** | C | — | — |
| Komunikasi ke civitas & sosialisasi | **A/R** | C | I | I |
| Evaluasi bulanan | **A/R** | C | I | I |

> ⚠️ **Catatan:** "1 Staf Input Data" bukan developer — ini staf administrasi yang tugasnya hanya mengisi spreadsheet/form. Tidak perlu kemampuan teknis.

---

## 📦 Data Readiness — Versi Realistis

### Yang Anda Punya Sekarang (Tanpa Minta Siapapun)

| Data | Ada? | Format | Tindakan |
|---|---|---|---|
| Nama ruangan/gedung FSM | ✅ Di kepala Anda | Mental/denah | Tulis ke Google Sheet, 30 menit |
| Nomor WA teknisi | ✅ Di HP Anda | Kontak HP | Copy ke spreadsheet, 15 menit |
| Daftar jenis kerusakan umum | ✅ Perkiraan | — | Minta AI buatkan draft, review 15 menit |
| Akun pengguna | ✅ via SSO UNDIP | OAuth login | Otomatis saat pengguna login pertama |
| Data aset | ❌ Tidak ada | — | Mulai kumpulkan setelah ticketing jalan |
| Jadwal kuliah | ❌ Tidak bisa akses | — | Input manual per semester (20 menit) |

### Data Readiness Score (Kondisi Solo)
| Dimensi | Score | Catatan |
|---|---|---|
| Ketersediaan Data | 2/5 | Minim, tapi cukup untuk start |
| Kualitas | 3/5 | Data yang ada (ruang, WA teknisi) cukup akurat |
| Aksesibilitas | 4/5 | Data di tangan Anda sendiri — tidak perlu minta siapapun |
| Governance | 3/5 | Anda yang decide semua — cepat, tidak birokratis |
| **Rata-rata** | **3/5** | 🟢 Cukup untuk go-live modul 1 dalam 1 minggu |

---

## ⚠️ FMEA — Risiko Utama Setup Solo + AI

| # | Failure Mode | Dampak | S | O | D | RPN | Pencegahan |
|---|---|---|---|---|---|---|---|
| 1 | Server FSM down, tidak ada yang bisa fix | Sistem tidak bisa diakses | 9 | 5 | 5 | **225** 🔴 | Identifikasi 1 kontak sysadmin FSM dari sekarang |
| 2 | AI buat kode yang error, tidak bisa diperbaiki | Fitur tidak jalan, proyek mandek | 8 | 5 | 3 | **120** 🔴 | Pakai tools dengan preview visual (Bolt.new) — error terlihat langsung |
| 3 | Budget $200 habis sebelum sistem stabil | Sistem terhenti di tengah jalan | 8 | 4 | 3 | **96** 🟡 | Prioritaskan free tier, bayar hanya Fonnte + Make.com bulan 1 |
| 4 | Pengguna tidak adopt — tetap lapor via WA | Sistem tidak dipakai, effort sia-sia | 9 | 6 | 3 | **162** 🔴 | Wajibkan 1 pintu: semua laporan kerusakan HARUS via sistem |
| 5 | SSO UNDIP berubah konfigurasi, login rusak | Semua pengguna tidak bisa masuk | 8 | 3 | 4 | **96** 🟡 | Backup login manual (username/password) sebagai fallback |
| 6 | Anda tidak punya waktu — proyek terbengkalai lagi | Kembali ke pola lama | 9 | 6 | 2 | **108** 🔴 | Blok 1 jam tiap Senin pagi khusus proyek ini, tidak boleh diganggu |
| 7 | Data aset tidak pernah diinput | Modul asset tidak bisa jalan | 5 | 7 | 4 | **140** 🔴 | Tunda modul asset sampai ticketing stabil — jangan paralel |
| 8 | Notifikasi WA sering gagal | Teknisi tidak tahu ada tiket | 7 | 5 | 3 | **105** 🔴 | Multi-channel: WA utama + email backup otomatis |

### Top 3 Risiko yang Paling Harus Dijaga
1. **RPN 225** — Server down tanpa sysadmin → **Tugas pertama: dapatkan nomor WA sysadmin server FSM hari ini**
2. **RPN 162** — Tidak ada adopsi → **Buat kebijakan: laporan kerusakan hanya via sistem — no exception**
3. **RPN 140** — Modul asset tidak jalan → **Jangan buka modul asset sebelum ticketing 3 bulan stabil**

---

## 🍚 RICE — Prioritas Fitur untuk Setup Solo

> Dengan keterbatasan waktu dan tenaga 1 orang, RICE di sini fokus pada effort yang bisa diselesaikan AI dalam < 1 hari.

| # | Fitur | R | I | C | E (hari AI) | RICE | Prioritas |
|---|---|---|---|---|---|---|---|
| Form laporan kerusakan web | 4000 | 3 | 90% | 0.5 | **21.600** | 🥇 #1 |
| Notifikasi WA ke teknisi | 4000 | 3 | 90% | 0.5 | **21.600** | 🥇 #1 |
| Login via SSO UNDIP | 4000 | 3 | 85% | 1 | **10.200** | 🥇 #2 |
| Status tiket (open/done) | 4000 | 2 | 90% | 0.5 | **14.400** | 🥇 #1 |
| Upload foto kerusakan | 4000 | 2 | 90% | 0.5 | **14.400** | 🥇 #1 |
| Dashboard WD II (jumlah tiket) | 1 | 3 | 85% | 1 | **2.55** | 🔵 #6 |
| Assign teknisi manual | 30 | 3 | 90% | 1 | **81** | 🔵 #5 |
| Riwayat per fasilitas | 500 | 2 | 80% | 2 | **400** | 🔵 #4 |
| Booking ruang (basic) | 3500 | 3 | 75% | 3 | **2.625** | 🔵 #7 |
| QR aset scan | 200 | 3 | 70% | 2 | **210** | 🟣 #8 |
| Auto-prioritas urgensi | 4000 | 2 | 65% | 3 | **1.733** | 🟣 #9 |
| Preventive maintenance schedule | 60 | 2 | 60% | 4 | **18** | 🟣 #10 |

### Urutan Build yang Realistis
```
Minggu 1: Form laporan + upload foto + notif WA teknisi (sistem hidup!)
Minggu 2: Login SSO + status tiket + assign teknisi
Minggu 3: Dashboard WD II + riwayat per fasilitas
Bulan 2:  Tambah modul booking ruang (basic)
Bulan 3+: Evaluasi → tambah fitur sesuai feedback real pengguna
```

---

## 🗺️ Roadmap 6 Bulan — Versi Solo + AI

### Bulan 1 — "Sistem Hidup"
**Target: 1 sistem ticketing yang benar-benar dipakai, bukan demo**

```
Minggu 1: Setup server + install Coolify + deploy app ticketing (AI build)
Minggu 2: Integrasi SSO UNDIP + test login dosen & mahasiswa
Minggu 3: Konfigurasi notif WA Fonnte + uji coba alur lengkap
Minggu 4: Soft launch ke 1 gedung — umumkan via grup WA dosen
```

**Indikator berhasil:** Ada ≥ 5 tiket masuk dari pengguna nyata di minggu ke-4.

---

### Bulan 2 — "Stabil & Dipercaya"
**Target: Pengguna mulai terbiasa, data mulai bermakna**

```
- Fix semua bug dari bulan 1 (ceritakan ke AI, AI perbaiki)
- Tambah: riwayat perbaikan per fasilitas
- Tambah: dashboard WD II (jumlah tiket per status)
- Roll-out ke seluruh FSM (umumkan lewat rapat pleno / WA dosen)
- Collect feedback via Google Form singkat (5 pertanyaan)
```

**Indikator berhasil:** > 20 tiket/bulan, > 50% tiket diselesaikan dalam SLA.

---

### Bulan 3 — "Modul Kedua"
**Target: Tambah Room & Lab Booking**

```
- Build form booking ruang (AI build dalam 2–3 hari)
- Input data ruangan ke sistem (Anda + 1 staf, 1 hari kerja)
- Integrasi: ruang dalam perbaikan otomatis tidak bisa dibooking
- Launch booking system ke dosen & laboran
```

**Indikator berhasil:** Ada ≥ 20 booking ruang via sistem dalam bulan pertama.

---

### Bulan 4 — "Data Bermakna"
**Target: Dari operasional ke insight**

```
- Dashboard yang menunjukkan: ruang paling sering rusak, teknisi paling aktif
- Export laporan bulanan otomatis ke PDF/Excel (AI build)
- Presentasi ke Dekan: "Ini data 3 bulan pertama kita"
- Gunakan data ini untuk argumen anggaran tahun depan
```

---

### Bulan 5 — "Asset Management Mulai"
**Target: QR code aset prioritas**

```
- Build modul asset dasar (AI build 3–5 hari)
- Print QR code untuk 50 aset paling mahal/penting dulu
- Input data: nama, lokasi, kondisi, nomor seri
- Integrasi: tiket kerusakan bisa di-link ke aset spesifik
```

---

### Bulan 6 — "Evaluasi & Skalasi"
**Target: Putuskan langkah 6 bulan ke depan**

```
- Review semua data 5 bulan: apa yang berhasil, apa yang tidak?
- Presentasi ke Dekan untuk anggaran 2025/2026
- Putuskan: apakah perlu rekrut developer part-time?
- Putuskan: modul mana yang perlu di-advance?
- Dokumentasi sistem untuk serah terima jika jabatan berganti
```

---

## 🛠️ Cara Kerja Harian WD II + AI

### Template Prompt yang Efektif

**Untuk build fitur baru:**
```
"Saya WD II FSM UNDIP. Saya punya web app ticketing yang sudah jalan 
di server FSM. Saya ingin tambah fitur [nama fitur]. 
Stack: [sebutkan stack yang AI sebelumnya buat]. 
Tolong buatkan kodenya, sertakan instruksi cara deploy."
```

**Untuk fix bug:**
```
"Sistem saya error seperti ini: [copy-paste pesan error].
Ini terjadi ketika pengguna [jelaskan langkah].
Ini kode yang relevan: [copy-paste kode].
Tolong perbaiki."
```

**Untuk analisis data:**
```
"Ini data tiket 1 bulan terakhir dari sistem saya: [paste data/screenshot].
Tolong analisis: mana fasilitas paling sering rusak? 
Mana teknisi paling produktif? Buat ringkasan untuk saya laporkan ke Dekan."
```

### Jadwal Kerja yang Realistis
| Waktu | Aktivitas | Durasi |
|---|---|---|
| Senin pagi (1x/minggu) | Review dashboard, lihat tiket pending, beri instruksi ke AI untuk pengembangan minggu ini | 30 menit |
| Kapanpun ada bug | Copy-paste error ke AI, deploy fix | 15–30 menit |
| Akhir bulan | Review data, buat keputusan fitur bulan depan | 1 jam |

**Total waktu Anda per minggu: ~1–2 jam. AI yang kerja sisanya.**

---

## ✅ Langkah Konkret Anda Hari Ini

Bukan minggu ini — **hari ini:**

| Prioritas | Tindakan | Waktu |
|---|---|---|
| 🔴 #1 | Tanyakan ke Kepala TU / Teknisi senior: siapa yang pegang server FSM? Dapatkan kontaknya | 10 menit |
| 🔴 #2 | Daftar Claude Pro di claude.ai ($20/bulan) | 5 menit |
| 🔴 #3 | Buka sesi Claude baru, ceritakan: "Saya WD II FSM UNDIP, server saya Ubuntu [versi], saya ingin build sistem ticketing sederhana, mulai dari mana?" | 15 menit |
| 🟡 #4 | Tulis di Google Sheet: daftar 10 ruangan FSM yang paling sering bermasalah | 20 menit |
| 🟡 #5 | Kirim WA ke 2–3 teknisi: "Saya mau buat sistem laporan kerusakan digital, nanti saya minta tolong coba ya" | 5 menit |

**Total: 55 menit. Setelah ini, proyek Anda sudah started.**

---

## 🔒 Sustainability — Agar Tidak Mati Saat Jabatan Berganti

Karena Anda kerja sendiri, ini sangat kritis:

1. **Semua kode di GitHub private milik FSM** — AI bisa setup ini, gratis
2. **Dokumentasi singkat di README** — AI yang tulis, Anda review 15 menit
3. **SK Dekan tentang sistem digital** — buat sekarang, 1 halaman saja
4. **1 orang "pemegang kunci"** — tendik atau laboran yang tahu cara restart server jika error, tidak perlu coding
5. **Backup otomatis database** — AI konfigurasikan cronjob backup harian ke folder server

---

## ⚖️ Perbandingan: Pendekatan Lama vs Pendekatan Ini

| Aspek | Pendekatan Lama (2 tahun gagal) | Pendekatan Ini |
|---|---|---|
| Tim | 5–10 orang, rapat rutin | 1 orang (Anda) + AI |
| Waktu mulai | Setelah semua siap | Hari ini |
| Anggaran | Belum ada/tidak pasti | $44/bulan untuk mulai |
| Fitur pertama | Semua modul sekaligus | 1 form + 1 notif WA |
| Bergantung pada | Staf, vendor, IT UNDIP | Server FSM + AI |
| Time to first value | Tidak pernah | 1 minggu |
| Risiko gagal | Tinggi (sudah terbukti) | Rendah — kalaupun gagal, kerugiannya kecil |

---

## 📌 Satu Kalimat untuk Dipegang

> **"Sistem yang 60% selesai tapi dipakai 100 orang setiap hari jauh lebih berharga dari sistem 100% sempurna yang tidak pernah jadi."**

Mulai dari ticketing. Buat jalan dalam 1 minggu. Semua yang lain menyusul.

---

*Dokumen ini bagian dari FSM Super Apps Analysis Suite*  
*Baca juga: [00-overview.md](./00-overview.md) untuk gambaran lengkap | [05-roadmap-next-steps.md](./05-roadmap-next-steps.md) untuk roadmap versi penuh*
