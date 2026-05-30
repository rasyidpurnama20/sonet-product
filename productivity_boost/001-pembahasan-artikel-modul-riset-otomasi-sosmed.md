# 001 — Pembahasan Mendalam: Artikel Review, Modul Ajar, Artikel Riset & Otomasi Sosmed

> Dokumen ini membahas 4 pertanyaan praktis secara mendalam, lengkap dengan alur kerja (workflow), prompt siap pakai untuk Claude Opus, dan solusi konkret untuk hambatan yang kamu sebutkan (compute deep learning gratis & masalah login otomasi sosmed).

**Daftar Isi**
1. [Bikin Artikel Review dari 0](#1-bikin-artikel-review-dari-0)
2. [Bikin Modul Ajar dari 0](#2-bikin-modul-ajar-dari-0)
3. [Bikin Artikel Riset dari 0 + Compute Deep Learning GRATIS](#3-bikin-artikel-riset-dari-0--compute-deep-learning-gratis)
4. [Otomasi Content Creator Website + Sosmed (IG & TikTok) — Solusi Masalah Login](#4-otomasi-content-creator-website--sosmed-ig--tiktok)

---

## 1. Bikin Artikel Review dari 0

"Artikel review" bisa berarti dua hal — keduanya dibahas:
- **Review jurnal/ilmiah** (literature review / systematic review) untuk publikasi akademik.
- **Review produk/konten** (review gadget, tools, buku) untuk blog/medsos/afiliasi.

### 1A. Review Ilmiah (Literature Review)

**Alur kerja end-to-end:**

| Tahap | Aktivitas | Peran Opus |
|-------|-----------|------------|
| 1. Tentukan scope | Rumuskan pertanyaan review (gunakan kerangka PICO/PICOC) | Bantu pertajam research question |
| 2. Kumpulkan sumber | Cari di Google Scholar, Scopus, Semantic Scholar, Connected Papers | Buat string pencarian Boolean |
| 3. Skrining | Saring berdasarkan judul/abstrak (kriteria inklusi-eksklusi) | Ringkas & klasifikasi abstrak |
| 4. Ekstraksi | Tarik data kunci tiap paper ke tabel sintesis | Buat tabel: tujuan, metode, temuan, gap |
| 5. Sintesis | Kelompokkan tema, temukan pola & kontradiksi | Petakan tema & argumen |
| 6. Penulisan | Tulis: intro, body bertema, gap, kesimpulan | Drafting + perbaikan alur |
| 7. Sitasi | Format referensi (APA/IEEE/Vancouver) | Cek konsistensi format |

> **Penting soal integritas:** Opus tidak boleh "mengarang" sitasi. Selalu verifikasi setiap referensi ke sumber asli. Pakai Opus untuk **meringkas paper yang KAMU sediakan**, bukan untuk menghasilkan daftar pustaka dari ingatan (risiko halusinasi sitasi).

**Prompt template (ekstraksi paper):**
```
Kamu asisten riset. Dari abstrak/paper berikut, isi tabel:
| Penulis & Tahun | Tujuan | Metode | Dataset/Sampel | Temuan Utama | Keterbatasan | Gap |
Jangan menambahkan info yang tidak ada di teks. Tandai "tidak disebutkan" bila kosong.

[tempel teks paper]
```

**Prompt template (sintesis tematik):**
```
Berikut 10 ringkasan paper (terlampir). Tugas:
1. Kelompokkan jadi 3-5 tema besar.
2. Untuk tiap tema: konsensus, perdebatan, dan gap riset.
3. Usulkan 1 paragraf "celah penelitian" yang belum terjawab.
```

**Struktur artikel review yang baik:** Abstract → Pendahuluan (latar + tujuan + research question) → Metodologi review (cara cari & seleksi) → Pembahasan per tema → Sintesis & gap → Arah penelitian masa depan → Kesimpulan → Referensi.

> Tip: Untuk **systematic review**, ikuti panduan PRISMA (diagram alir jumlah paper yang diidentifikasi → disaring → dimasukkan). Repo ini sudah punya pola serupa di folder `research-map/` yang bisa kamu jadikan contoh format.

### 1B. Review Produk/Konten (untuk blog/afiliasi)

**Kerangka review yang menjual & dipercaya:**
1. **Hook** — masalah yang dialami pembaca.
2. **Ringkasan verdict** (TL;DR + rating) di atas — pembaca suka jawaban cepat.
3. **Spesifikasi / fakta objektif.**
4. **Pengalaman pakai** (kelebihan & kekurangan jujur — kekurangan justru menaikkan kredibilitas).
5. **Perbandingan** dengan alternatif.
6. **Untuk siapa cocok / tidak cocok.**
7. **CTA + link afiliasi** (disclosure jujur bahwa ada komisi).

> Monetisasi: afiliasi (Tokopedia/Shopee Affiliate, Amazon, dll), sponsored review, atau ads. Kunci keberlanjutan: **kejujuran** — review yang terlalu memuji akan kehilangan kepercayaan & pembaca.

---

## 2. Bikin Modul Ajar dari 0

Modul ajar yang baik dirancang **mundur dari tujuan** (Backward Design): tentukan dulu *apa yang harus bisa dilakukan murid*, baru susun materi & asesmen.

### Alur Penyusunan (Backward Design)
1. **Capaian Pembelajaran (Learning Outcomes)** — pakai kata kerja terukur (Taksonomi Bloom: menjelaskan, menganalisis, merancang, mengevaluasi).
2. **Asesmen** — bagaimana membuktikan murid mencapainya (kuis, proyek, rubrik).
3. **Aktivitas & Materi** — baru di sini menyusun konten, contoh, latihan.

### Anatomi Modul Ajar
| Komponen | Isi |
|----------|-----|
| Identitas | Mata kuliah, topik, durasi, jenjang |
| Capaian pembelajaran | 3-5 outcome terukur |
| Prasyarat | Pengetahuan awal yang dibutuhkan |
| Peta konsep | Diagram hubungan antar topik |
| Uraian materi | Penjelasan + contoh + ilustrasi |
| Aktivitas | Diskusi, studi kasus, praktikum |
| Asesmen | Kuis, tugas, proyek + rubrik penilaian |
| Refleksi | Pertanyaan pemantik di akhir |
| Referensi | Bacaan lanjutan |

**Prompt template (rancang outline modul):**
```
Buat outline modul ajar untuk topik "[TOPIK]" jenjang [S1/SMA/pelatihan],
durasi [X] pertemuan. Untuk tiap pertemuan beri:
- Capaian pembelajaran (kata kerja Bloom, terukur)
- Poin materi inti
- 1 aktivitas aktif (bukan ceramah)
- 1 bentuk asesmen + ide rubrik singkat
Sertakan miskonsepsi umum yang perlu diluruskan.
```

**Prompt template (buat soal + rubrik):**
```
Dari capaian "[tempel outcome]", buat:
- 5 soal pilihan ganda (dengan kunci & pembahasan)
- 2 soal esai HOTS (higher-order thinking)
- Rubrik penilaian esai (skala 1-4, kriteria jelas)
```

> **Diferensiasi & engagement:** minta Opus membuat 3 versi penjelasan (analogi sederhana → teknis), plus contoh kontekstual lokal agar relatable. Repo ini punya konteks materi IoT di folder `iot-mat-d-2026/` yang bisa jadi bahan modul nyata.

> **Monetisasi:** jual modul sebagai produk digital, jadi bahan pelatihan berbayar, atau tawarkan jasa penyusunan modul ke dosen/lembaga/sekolah.

---

## 3. Bikin Artikel Riset dari 0 + Compute Deep Learning GRATIS

Ini bagian terpenting karena kamu menyebut **bingung menjalankan eksperimen deep learning tanpa bayar**. Saya bahas dua sisi: (A) alur menulis artikel riset, dan (B) **di mana menjalankan eksperimen DL gratis**.

### 3A. Alur Artikel Riset (IMRaD)
Struktur standar jurnal: **I**ntroduction → **M**ethods → **R**esults → **a**nd → **D**iscussion.

1. **Cari gap** (dari literature review di bagian 1) → rumuskan hipotesis/pertanyaan.
2. **Rancang eksperimen** — dataset, model, metrik, baseline, protokol evaluasi.
3. **Jalankan eksperimen** (lihat 3B untuk compute gratis).
4. **Analisis hasil** — tabel, grafik, uji signifikansi.
5. **Tulis** — Opus bantu drafting Methods (paling teknis) & Discussion, kamu isi data nyata.
6. **Submit** — pilih jurnal/konferensi sesuai scope, ikuti template (LaTeX/Word).

> **Etika publikasi:** Hasil & data harus asli dari eksperimenmu. Opus untuk membantu *menulis & menstrukturkan*, bukan memalsukan data. Banyak jurnal kini mewajibkan disclosure penggunaan AI dalam penulisan — patuhi aturan tiap jurnal.

### 3B. Di Mana Menjalankan Eksperimen Deep Learning GRATIS?

Kabar baik: untuk **prototipe, skripsi/tesis, dan eksperimen skala kecil-menengah**, kamu **tidak perlu bayar**. Berikut opsi yang benar-benar gratis (per 2026):

| Platform | Yang Didapat | Cocok Untuk | Catatan |
|----------|--------------|-------------|---------|
| **Google Colab (free)** | GPU NVIDIA T4, sesi terbatas | Prototipe cepat, belajar, demo | Sesi auto-putus (~12 jam), kuota mingguan, tanpa kartu kredit |
| **Kaggle Notebooks** | GPU T4/P100, ~30 jam/minggu | Eksperimen rutin, lomba | Gratis tanpa kartu kredit; notebook publik secara default |
| **SageMaker Studio Lab** | Notebook gratis (CPU/GPU) | Belajar & eksperimen ringan | Salah satu opsi gratis utama |
| **Paperspace Gradient (free tier)** | GPU tier gratis | Eksperimen sesekali | Reliabilitas/UX dilaporkan tidak selalu konsisten di 2026 |
| **Kredit cloud baru** | GCP ~$300, Azure ~$200, Oracle always-free, AWS Activate (startup) | Eksperimen lebih besar sementara | Perlu kartu kredit; habis kredit = berbayar |
| **Hugging Face Spaces** | Hosting demo model (CPU gratis) | Publikasikan demo, bukan training berat | GPU butuh upgrade |

Ringkasan kemampuan tier gratis berdasarkan rangkuman beberapa sumber: cocok untuk **prototyping, fine-tuning model di bawah ~7B parameter, dan dataset di bawah ~10 GB**; sedangkan **melatih model besar dari nol atau multi-GPU butuh compute berbayar** ([Technolynx, 2026](https://www.technolynx.com/post/cheapest-gpu-cloud-ai-workloads); [Alibaba electronics guide, 2026](https://electronics.alibaba.com/question/free-gpu-access-in-2026-real-options-limits)). *Konten dirangkum & diparafrase untuk kepatuhan lisensi.*

**Strategi praktis agar muat di tier gratis:**
- **Mulai kecil** — subset dataset & model kecil dulu untuk validasi pipeline, baru skalakan.
- **Transfer learning / fine-tuning** model pretrained (jauh lebih murah daripada training dari nol).
- **Teknik hemat memori** — mixed precision (FP16), gradient accumulation, batch size kecil, LoRA/PEFT untuk model bahasa.
- **Checkpoint sering** — simpan model ke Google Drive/Kaggle Datasets agar tak hilang saat sesi terputus.
- **Dataset publik** — Kaggle Datasets, Hugging Face Datasets, UCI ML Repo (gratis).
- **Manfaatkan status mahasiswa** — banyak penyedia & GitHub Student Pack memberi kredit tambahan.

> **Rekomendasi alur**: Prototyping & debugging di **Colab** → eksperimen final yang butuh jam lebih banyak di **Kaggle** (kuota mingguan lebih jelas) → kalau butuh lebih besar, pakai **kredit gratis GCP/Azure** sementara. Simpan semua kode di GitHub + checkpoint di Drive.

---

## 4. Otomasi Content Creator Website + Sosmed (IG & TikTok)

Kamu menyebut hambatan utama: **"tidak bisa pakai automasi karena harus login, saya gak tau caranya."** Ini sangat umum. Inti jawabannya: **jangan mengotomasi dengan cara meniru login (browser bot) — itu melanggar aturan & berisiko diblokir. Gunakan login resmi SEKALI lewat OAuth, lalu posting via API/tools resmi tanpa login ulang.**

### 4.1 Kenapa "Login Bot" Bukan Solusi
Mengotomasi dengan script yang mengetik username/password di halaman login (mis. Selenium/Puppeteer) **melanggar Terms of Service** IG & TikTok, sering kena CAPTCHA/2FA, dan berisiko akun **dibanned**. Hindari.

### 4.2 Cara yang Benar: OAuth (Login Sekali, Posting Selamanya)
**OAuth** adalah mekanisme di mana kamu login **satu kali** lewat halaman resmi platform, lalu aplikasi/tools mendapat **token** untuk posting atas nama kamu — tanpa pernah menyimpan password-mu dan tanpa login manual tiap kali. Inilah "cara"-nya yang selama ini kamu cari.

Ada **dua jalur**, pilih sesuai kemampuan teknis:

#### Jalur A — TANPA Coding (paling cepat, direkomendasikan untuk mulai)
Pakai **tools penjadwalan resmi** yang sudah jadi partner API Meta & TikTok. Kamu cukup connect akun sekali (OAuth), lalu jadwalkan posting:

| Tools | IG | TikTok | Catatan |
|-------|----|--------|---------|
| **Meta Business Suite** | ✅ | ❌ | Gratis, native dari Meta untuk IG + Facebook |
| **Buffer** | ✅ | ✅ | Ada free tier; partner API resmi |
| **Later** | ✅ | ✅ | Fokus visual/IG |
| **Metricool** | ✅ | ✅ | Ada free tier + analytics |
| **Publer / ContentStudio** | ✅ | ✅ | Penjadwalan multi-platform |

> Untuk **IG**, akun harus **Business/Creator** (bukan Personal) agar bisa dijadwalkan otomatis. Untuk **TikTok**, beberapa tools sudah mendukung auto-post, sebagian masih "push notification" (kamu finalisasi di HP).

#### Jalur B — DENGAN Coding (untuk otomasi penuh/produk sendiri)
Pakai **API resmi**:

- **Instagram** → **Meta Graph API (Instagram Content Publishing)**. Syarat: akun **IG Business/Creator** tersambung ke **Facebook Page**, app di Meta for Developers, dan **app review** untuk izin publish. Bisa posting foto, carousel, dan Reels. Ada rate limit harian.
- **TikTok** → **Content Posting API** (Direct Post / Upload). Menurut dokumentasi & ulasan developer, API ini **sangat ketat**: butuh **app review/persetujuan**, alur **upload dua tahap (chunked)**, **tidak ada penjadwalan native**, dan ada rate limit ([TikTok for Developers](https://developers.tiktok.com/doc/content-posting-api-get-started); [posteverywhere.ai, 2026](https://posteverywhere.ai/blog/post-to-tiktok-api)). Sebelum app disetujui, biasanya hanya bisa posting ke akun sendiri/privat. *Dirangkum untuk kepatuhan lisensi.*

**Jalan pintas via aggregator API** (membungkus banyak platform di satu endpoint, menangani OAuth untuk-mu): **Buffer API, Ayrshare, Upload-Post, Postiz (open-source), Zernio**. Cocok kalau mau bikin produk otomasi tanpa mengurus app-review tiap platform satu per satu ([Buffer, 2026](https://buffer.com/api); [getlate.dev, 2026](https://getlate.dev/blog/tiktok-posting-api)). *Konten diparafrase.*

### 4.3 Arsitektur Otomasi Content Creator (End-to-End)

```
        ┌──────────────┐
        │  IDE KONTEN  │  ← Opus generate kalender + script + caption
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │  PRODUKSI    │  ← teks (Opus), gambar (AI image), video (template)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │  REVIEW MANUAL│ ← kamu cek kualitas & brand voice (WAJIB)
        └──────┬───────┘
               │
        ┌──────▼─────────────────────┐
        │  PENJADWALAN (OAuth sekali) │
        │  Buffer/Metricool/Meta Suite│
        └──────┬───────────┬──────────┘
               │           │
          ┌────▼───┐   ┌───▼─────┐
          │  IG    │   │ TikTok  │
          └────────┘   └─────────┘
```

**Komponen website content creator:**
- **Backend** generate ide & draft (Opus via API) → simpan ke database.
- **Editorial calendar** (Notion/Airtable/Google Sheet) sebagai sumber kebenaran.
- **Otomasi penghubung** (n8n/Make/Zapier) memicu kiriman ke tools penjadwal.
- **Approval gate** — selalu ada langkah review manusia sebelum publish (jaga kualitas & hindari blunder).

### 4.4 Langkah Mulai (Realistis)
1. **Minggu ini:** ubah IG ke akun **Creator/Business**, daftar **Buffer/Metricool** (free), connect IG + TikTok via OAuth. Jadwalkan 1 minggu konten. (Tanpa coding.)
2. **Bulan depan:** kalau butuh otomasi penuh, daftar **Meta for Developers** + **TikTok for Developers**, ajukan app review, atau pakai **aggregator API**.
3. **Skalakan:** jadikan jasa — "content automation setup" untuk UMKM/kreator (lihat strategi #10 & #24 di `50-strategi-cuan-claude-opus.md`).

> **Catatan kepatuhan:** Selalu ikuti Terms of Service tiap platform. Hindari spam/mass-posting & engagement palsu — bisa kena banned dan merusak reputasi. Otomasi yang aman = posting konten asli & terjadwal lewat API resmi, bukan manipulasi.

---

## Ringkasan & Hubungan Antar Topik

| Topik | Inti Solusi | Monetisasi |
|-------|-------------|------------|
| 1. Artikel review | Workflow ekstraksi→sintesis + verifikasi sitasi | Jasa tulis, blog afiliasi |
| 2. Modul ajar | Backward design (outcome→asesmen→materi) | Produk digital, jasa, pelatihan |
| 3. Artikel riset + compute | IMRaD + GPU gratis (Colab/Kaggle) + hemat memori | Jasa riset, publikasi, hibah |
| 4. Otomasi sosmed | OAuth (login sekali) via tools resmi/API, bukan login bot | Jasa setup otomasi konten |

---

## Sumber
- Free GPU 2026 (Colab T4, Kaggle ~30 jam/minggu, dll): [Alibaba electronics guide](https://electronics.alibaba.com/question/free-gpu-access-in-2026-real-options-limits), [Thunder Compute](https://www.thundercompute.com/blog/free-cloud-gpu-credits)
- Batas praktis tier gratis (model <7B, dataset <10GB): [Technolynx](https://www.technolynx.com/post/cheapest-gpu-cloud-ai-workloads)
- Kredit cloud baru (GCP/Azure/Oracle/AWS): [GMI Cloud](https://www.gmicloud.ai/blog/where-can-i-get-free-gpu-cloud-trials-in-2026-a-complete-guide)
- TikTok Content Posting API (ketat, app review, no native scheduling): [TikTok for Developers](https://developers.tiktok.com/doc/content-posting-api-get-started), [posteverywhere.ai](https://posteverywhere.ai/blog/post-to-tiktok-api), [getlate.dev](https://getlate.dev/blog/tiktok-posting-api)
- Penjadwalan IG & aggregator API: [Buffer API](https://buffer.com/api)

*Catatan: Semua kutipan dari sumber telah diparafrase/dirangkum untuk kepatuhan lisensi. Verifikasi detail teknis terbaru langsung di dokumentasi resmi karena kebijakan platform sering berubah.*
