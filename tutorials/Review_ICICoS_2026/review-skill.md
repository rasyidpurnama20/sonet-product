# Skill: Comprehensive ICICoS Paper Extraction
> Kiro Skill File — aktifkan sebelum memulai review paper ICICoS
> Versi: 1.0 | Juni 2026

---

## Tujuan Skill Ini

Skill ini memberikan instruksi lengkap kepada AI untuk mengekstrak **semua informasi kritis** dari paper ICICoS secara komprehensif dan terstruktur — sebagai fondasi sebelum menulis review formal.

Prinsip utama:
- **Ekstrak dulu, analisis kemudian** — fase ini hanya menangkap apa yang *tertulis*, bukan menilai.
- **Spesifisitas wajib** — setiap poin harus menyebut nomor section, halaman, tabel, atau gambar.
- **Tidak ada asumsi** — jika informasi tidak ada di paper, nyatakan "Tidak disebutkan" bukan mengarang.

---

## FASE 1 — Klasifikasi & Metadata Paper

Ekstrak informasi dasar berikut:

```
METADATA
- Judul lengkap:
- Jumlah halaman:
- Sub-topik ICICOS yang paling relevan:
  [ ] Machine Learning / Deep Learning
  [ ] Computer Vision / Image Processing
  [ ] Natural Language Processing
  [ ] IoT / Embedded Systems
  [ ] Network / Cybersecurity
  [ ] Software Engineering / Systems
  [ ] Information Systems / Business Applications
  [ ] Signal / Data Processing
  [ ] Other: ___

TIPE PAPER
  [ ] Eksperimental (propose + uji model/metode baru)
  [ ] Sistem/Implementasi (bangun dan evaluasi sistem)
  [ ] Survei/Literature Review (rangkum bidang tertentu)
  [ ] Studi Kasus (aplikasi metode pada konteks spesifik)
  [ ] Teoritis / Analisis (tanpa implementasi empiris)

STRUKTUR PAPER — centang yang ADA, beri ✗ yang TIDAK ADA, beri ⚠ yang ada tapi BERMASALAH:
  [ ] Abstract       [ ] Introduction     [ ] Related Work
  [ ] Methodology    [ ] Results          [ ] Discussion
  [ ] Conclusion     [ ] References       [ ] Appendix/Supplement
```

---

## FASE 2 — Ekstraksi Masalah & Kontribusi

```
PERNYATAAN MASALAH
- Masalah utama yang diangkat (1-2 kalimat faktual):
- Gap atau kekurangan yang ditemukan dari literatur sebelumnya:
- Section & halaman pernyataan masalah: Sec ___, hal ___

KLAIM KONTRIBUSI PENULIS
- Kontribusi 1 (kutip langsung dari paper):
- Kontribusi 2 (jika ada, kutip langsung):
- Kontribusi 3 (jika ada, kutip langsung):
- Lokasi klaim kontribusi: [ ] Abstract  [ ] Introduction  [ ] Conclusion  [ ] Semua

NOVELTY YANG DIKLAIM
- Kata kunci novelty ("first", "novel", "new", "improved", dll.) dan konteksnya:
- Apakah didukung perbandingan dengan prior work? [ ] Ya  [ ] Tidak  [ ] Parsial
```

---

## FASE 3 — Ekstraksi Metodologi

### 3A. Untuk Paper ML / Deep Learning

```
ARSITEKTUR / ALGORITMA
- Nama metode yang diusulkan:
- Komponen utama arsitektur (daftar, dengan referensi figure/table):
- Fungsi loss / objective function:
- Framework / library implementasi:
- Hardware yang digunakan:

DATASET
- Nama dataset 1: | Ukuran: | Sumber/publikasi: | Tahun rilis dataset:
- Nama dataset 2 (jika ada): | Ukuran: | Sumber: | Tahun:
- Pembagian data (train/val/test split):
- Apakah ada data augmentation? [ ] Ya — sebutkan: ___ [ ] Tidak

HYPERPARAMETER & TRAINING
- Learning rate:             - Optimizer:
- Batch size:                - Jumlah epoch:
- Regularization:            - Lainnya:
- Apakah ada hyperparameter tuning / ablation? [ ] Ya  [ ] Tidak

METRIK EVALUASI
- Metrik yang digunakan (daftar lengkap):
- Apakah ada multiple runs / confidence interval? [ ] Ya  [ ] Tidak

BASELINE / PEMBANDING
- Metode 1:   Tahun:   Paper asli dikutip: [ ] Ya [ ] Tidak
- Metode 2:   Tahun:   Paper asli dikutip: [ ] Ya [ ] Tidak
- Metode 3:   Tahun:   Paper asli dikutip: [ ] Ya [ ] Tidak
- Metode lainnya:
```

### 3B. Untuk Paper Sistem / Implementasi

```
ARSITEKTUR SISTEM
- Nama sistem:
- Komponen utama (daftar, referensi ke figure arsitektur):
- Teknologi stack (backend, frontend, database, middleware):
- Protokol komunikasi (jika relevan):
- Apakah ada diagram arsitektur? [ ] Ya (Fig ___) [ ] Tidak

ENVIRONMENT PENGUJIAN
- Hardware / cloud platform:
- Jumlah node/user yang diuji:
- Kondisi pengujian (real-world / simulasi):

METRIK PERFORMA
- Latency / response time:    - Throughput:
- Memory usage:               - CPU usage:
- Lainnya:

STATUS DEPLOYMENT
- [ ] Production (sudah live)   [ ] Pilot / limited deployment
- [ ] Prototype saja            [ ] Simulasi saja
- Kode tersedia (open source)? [ ] Ya (URL: ___) [ ] Tidak
- Instruksi reproduksi? [ ] Ya  [ ] Tidak
```

### 3C. Untuk Paper Survei / Literature Review

```
CAKUPAN SURVEI
- Rentang tahun literatur yang dicakup:
- Jumlah paper yang dianalisis / disintesis:
- Database pencarian yang digunakan:
- Kriteria inklusi dan eksklusi:
- Apakah ada PRISMA diagram / protokol sistematis? [ ] Ya  [ ] Tidak

TAKSONOMI
- Kategori / dimensi yang digunakan untuk mengelompokkan paper:
- Apakah framework/taksonomi baru diusulkan? [ ] Ya  [ ] Tidak
- Tabel perbandingan paper? [ ] Ya (Table ___) [ ] Tidak

TEMUAN DAN GAP
- 3 trend utama yang ditemukan:
  1.
  2.
  3.
- Research gap yang diidentifikasi:
- Future directions yang disebut:
```

---

## FASE 4 — Ekstraksi Hasil & Pembahasan

```
HASIL UTAMA
- Hasil terbaik yang diklaim (angka spesifik, per dataset/metrik):
  Metrik ___: ___ (Table/Fig ___, hal ___)
  Metrik ___: ___ (Table/Fig ___, hal ___)
  Metrik ___: ___ (Table/Fig ___, hal ___)

PERBANDINGAN DENGAN BASELINE
- vs. Baseline terbaik: selisih ___ pada metrik ___
- vs. Baseline lainnya: ...
- Apakah perbaikan diklaim "state-of-the-art"? [ ] Ya  [ ] Tidak
  Jika Ya, bukti yang diberikan:

ABLATION STUDY
- Apakah ada? [ ] Ya  [ ] Tidak
- Komponen yang diablasi (jika ada):
- Temuan ablation:

ANALISIS KUALITTATIF / ERROR ANALYSIS
- Apakah ada analisis kualitatif hasil? [ ] Ya  [ ] Tidak
- Apakah ada case study / contoh prediksi? [ ] Ya  [ ] Tidak
- Apakah ada visualisasi hasil? [ ] Ya (sebutkan figure) [ ] Tidak

KETERBATASAN
- Keterbatasan yang DIAKUI penulis (kutip atau parafrase):
- Apakah ada diskusi limitations? [ ] Ya (Sec ___, hal ___) [ ] Tidak
```

---

## FASE 5 — Analisis Referensi

```
STATISTIK REFERENSI
- Total jumlah referensi:
- Referensi termuda (tahun):
- Referensi tertua (tahun):
- Jumlah referensi 2023–2025:
- Jumlah referensi 2020–2022:
- Jumlah referensi sebelum 2020:

KUALITAS SUMBER
- Dominan dari venue: [ ] IEEE  [ ] ACM  [ ] Springer  [ ] Elsevier  [ ] Campuran
- Apakah ada referensi dari sumber non-akademis? [ ] Ya  [ ] Tidak

PENGGUNAAN SITASI
- Apakah klaim novelty ("first", "novel") punya sitasi pendukung? [ ] Ya  [ ] Tidak
- Apakah ada klaim penting tanpa sitasi? Sebutkan lokasi (hal/line):
- Apakah baseline dikutip dari paper original-nya? [ ] Ya  [ ] Sebagian  [ ] Tidak

PAPER PENTING YANG MUNGKIN TERLEWAT
(Isi hanya jika yakin berdasarkan isi paper, bukan spekulasi)
- Paper/survei seminal di bidang ini yang tidak dikutip:
```

---

## FASE 6 — Cek Konsistensi Internal

Instruksi: Bandingkan klaim di satu bagian paper dengan bagian lainnya.

```
KONSISTENSI ABSTRACT vs. HASIL
Untuk setiap angka/klaim di Abstract:
| Klaim di Abstract | Didukung di Results? | Lokasi bukti |
|---|---|---|
| | | |

KONSISTENSI INTRODUCTION vs. CONCLUSION
- Apakah problem statement di Introduction terjawab di Conclusion? [ ] Ya  [ ] Tidak  [ ] Parsial
- Apakah ada klaim baru di Conclusion yang tidak dibahas sebelumnya? [ ] Ya  [ ] Tidak

KONSISTENSI ANGKA
- Apakah angka di teks sesuai dengan yang di tabel/figure? [ ] Ya  [ ] Tidak
  Jika tidak, catat ketidaksesuaian (hal/tabel):
```

---

## FASE 7 — Relevansi & Dampak

```
RELEVANSI ICICOS
- Apakah topik masuk dalam scope ICICOS? [ ] Ya jelas  [ ] Ya tapi borderline  [ ] Tidak
- Sub-track ICICOS yang paling sesuai:

KONTRIBUSI AKADEMIS
- Tipe kontribusi: [ ] Theoretical  [ ] Empirical  [ ] Tool/System  [ ] Dataset  [ ] Survey
- Signifikansi perbaikan performa (jika ada): [ ] Marginal (<1%)  [ ] Moderate (1–5%)  [ ] Significant (>5%)
- Apakah ada potensi dampak praktis? [ ] Ya — sebutkan:  [ ] Tidak jelas

REPRODUSIBILITAS
- Apakah cukup detail untuk direplikasi? [ ] Ya  [ ] Sebagian  [ ] Tidak
- Kode / data tersedia? [ ] Ya  [ ] Tidak
- Hal kritis yang hilang untuk reproduksi:
```

---

## Checklist Setelah Ekstraksi Lengkap

Sebelum lanjut ke review formal, pastikan semua fase selesai:

- [ ] Fase 1: Metadata dan tipe paper terisi
- [ ] Fase 2: Masalah dan klaim kontribusi dikutip langsung dari paper
- [ ] Fase 3: Metodologi diekstrak sesuai tipe paper
- [ ] Fase 4: Hasil dan angka spesifik dengan referensi table/figure
- [ ] Fase 5: Statistik referensi terisi, gap sitasi dicatat
- [ ] Fase 6: Konsistensi internal dicek
- [ ] Fase 7: Relevansi dan dampak dinilai
- [ ] Semua "Tidak disebutkan" sudah diverifikasi manual di paper

---

## Catatan Penggunaan

- Gunakan template ini sebagai **prompt tunggal** atau **dipecah per fase** sesuai panjang paper.
- Untuk paper yang sangat panjang (>10 halaman), kirim fase 1–2 dulu, baca hasilnya, baru lanjutkan.
- Hasil ekstraksi ini adalah **input** untuk `review-prompts.md` pada langkah berikutnya.
- Koreksi manual hasil AI sebelum melanjutkan — AI bisa salah baca tabel atau angka.

---

*Bagian dari: `tutorials/Review_ICICoS_2026/`*
*Gunakan bersama: `review-prompts.md` dan `review-template.docx`*
*Juni 2026*
