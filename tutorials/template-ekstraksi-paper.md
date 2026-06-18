# Template Ekstraksi Paper — ICICOS Reviewer
> Gunakan file ini sebagai referensi saat upload paper ke ChatGPT Plus Project
> Pilih template sesuai tipe paper yang kamu review
> Juni 2026

---

## Cara Pakai File Ini

1. Upload PDF paper ke chat dalam Project ChatGPT Plus kamu
2. Pilih template di bawah yang paling cocok dengan tipe paper
3. Copy prompt ekstraksi → paste ke chat → kirim
4. **Baca dan koreksi hasil ekstraksi** sebelum lanjut ke analisis
5. Gunakan hasil ekstraksi sebagai dasar tugas review berikutnya

> **Prinsip:** Ekstraksi hanya menangkap **apa yang tertulis**, bukan menilai baik/buruk.
> Penilaian dilakukan di langkah berikutnya dengan tugas yang terpisah.

---

## Template A — Paper Machine Learning / Deep Learning

**Cocok untuk:** paper yang mengusulkan model, arsitektur, atau algoritma baru

### Prompt Ekstraksi:
```
Baca paper ini dan ekstrak informasi berikut. Hanya tulis apa yang
ada di paper — jangan tambahkan analisis atau penilaian.
Jika informasi tidak ada di paper, tulis "Tidak disebutkan".

IDENTIFIKASI PAPER
- Judul:
- Tipe kontribusi: [ ] Model baru  [ ] Metode baru  [ ] Aplikasi metode existing

MASALAH & SOLUSI
- Masalah yang diselesaikan (1-2 kalimat):
- Solusi yang diusulkan (nama metode + ide utamanya):
- Klaim novelty penulis (kutip kalimat langsung dari paper):

SETUP EKSPERIMEN
- Dataset: (nama, ukuran, sumber, tahun rilis dataset)
- Pembagian data: (train/val/test split)
- Metrik evaluasi: (daftar semua metrik yang digunakan)
- Baseline: (daftar semua metode pembanding)
- Implementasi: (framework, hardware, hyperparameter utama)

HASIL
- Hasil terbaik yang diklaim: (angka spesifik per dataset per metrik)
- Perbandingan dengan baseline terbaik: (selisih performa)
- Apakah ada ablation study? [ ] Ya  [ ] Tidak
- Jika ya, komponen apa yang diablasi?

REFERENSI
- Jumlah total referensi:
- Tahun termuda dari referensi:
- Tahun tertua dari referensi:
- Apakah ada paper 2023-2025 yang dikutip? [ ] Ya  [ ] Tidak

KETERBATASAN
- Keterbatasan yang diakui penulis (jika ada):
```

### Contoh Hasil Ekstraksi (Template A):
```
IDENTIFIKASI PAPER
- Judul: "Adaptive BiLSTM with Channel Attention for IoT Intrusion Detection"
- Tipe kontribusi: [✓] Model baru

MASALAH & SOLUSI
- Masalah: False positive rate tinggi pada IDS konvensional di jaringan IoT
  yang heterogen
- Solusi: BiLSTM + Channel Attention Mechanism ("CA-BiLSTM") yang
  memfilter fitur jaringan secara adaptif
- Klaim novelty: "To the best of our knowledge, this is the first work
  to integrate channel attention into BiLSTM for IoT-specific IDS"

SETUP EKSPERIMEN
- Dataset: NSL-KDD (125.973 record, 1999), UNSW-NB15 (257.673 record, 2015)
- Pembagian data: 80/20 train-test, tidak ada validation set
- Metrik: Accuracy, Precision, Recall, F1-Score, False Positive Rate
- Baseline: KNN, SVM, Random Forest, standard LSTM, BiLSTM
- Implementasi: TensorFlow 2.8, Nvidia RTX 3080, lr=0.001, batch=64, epoch=50

HASIL
- Hasil terbaik: NSL-KDD: Acc 98.7%, F1 98.4% | UNSW-NB15: Acc 96.2%, F1 95.8%
- vs. baseline terbaik (BiLSTM): +1.3% Accuracy di NSL-KDD
- Ablation study: Tidak ada

REFERENSI
- Total: 42 referensi
- Termuda: 2023  |  Tertua: 2009
- Paper 2023-2025: Ya (4 paper)

KETERBATASAN
- Tidak disebutkan
```

---

## Template B — Paper Sistem / Implementasi / Arsitektur

**Cocok untuk:** paper yang membangun sistem, platform, atau infrastruktur

### Prompt Ekstraksi:
```
Baca paper ini dan ekstrak informasi berikut. Hanya tulis apa yang
ada di paper — jangan tambahkan analisis.
Jika informasi tidak ada di paper, tulis "Tidak disebutkan".

IDENTIFIKASI PAPER
- Judul:
- Tipe: [ ] Sistem baru  [ ] Peningkatan sistem existing  [ ] Integrasi sistem

MASALAH & SOLUSI
- Masalah atau gap yang diangkat (1-2 kalimat):
- Sistem yang dibangun (nama + fungsi utamanya):
- Klaim kontribusi utama (kutip langsung):

ARSITEKTUR SISTEM
- Komponen utama sistem (daftar):
- Teknologi/stack yang digunakan:
- Apakah ada diagram arsitektur? [ ] Ya  [ ] Tidak
- Skalabilitas: apakah dibahas? [ ] Ya  [ ] Tidak

EVALUASI
- Metrik performa: (latency, throughput, memory, dll.)
- Apakah ada user study / user evaluation? [ ] Ya  [ ] Tidak
- Apakah ada perbandingan dengan sistem lain? [ ] Ya  [ ] Tidak
- Environment pengujian: (hardware, jumlah user, kondisi)

IMPLEMENTASI & DEPLOYMENT
- Apakah sistem sudah di-deploy? [ ] Ya  [ ] Prototype saja
- Apakah kode/dataset tersedia (open source)? [ ] Ya  [ ] Tidak
- Instruksi reproduksi tersedia? [ ] Ya  [ ] Tidak

REFERENSI
- Jumlah total referensi:
- Apakah ada referensi ke sistem serupa yang sudah ada?
```

### Contoh Hasil Ekstraksi (Template B):
```
IDENTIFIKASI PAPER
- Judul: "CloudFS: A Distributed File Synchronization System for Edge Computing"
- Tipe: [✓] Sistem baru

MASALAH & SOLUSI
- Masalah: Sinkronisasi file antara edge node dan cloud server mengalami
  latensi tinggi dan konflik data pada konektivitas tidak stabil
- Sistem: "CloudFS" — sistem sinkronisasi terdistribusi dengan algoritma
  conflict resolution berbasis vector clock
- Klaim: "CloudFS achieves 3x faster sync compared to rsync under
  intermittent network conditions"

ARSITEKTUR SISTEM
- Komponen: Edge Agent, Sync Manager, Conflict Resolver, Cloud Gateway
- Stack: Go 1.20, gRPC, Redis, MinIO
- Diagram arsitektur: Ya (Figure 2)
- Skalabilitas: Dibahas (Section 4.3) — uji hingga 100 node

EVALUASI
- Metrik: Sync latency (ms), throughput (MB/s), conflict resolution time
- User study: Tidak ada
- Perbandingan: vs. rsync, Syncthing, Seafile
- Environment: 10 edge node simulasi, AWS EC2 t3.medium

IMPLEMENTASI & DEPLOYMENT
- Status: Prototype, belum production
- Open source: Tidak
- Instruksi reproduksi: Tidak disebutkan

REFERENSI
- Total: 35 referensi
- Sistem serupa: rsync (1996), Syncthing (2013), Ceph (2006)
```

---

## Template C — Paper Survei / Literature Review

**Cocok untuk:** paper yang mengulas dan merangkum literatur suatu topik

### Prompt Ekstraksi:
```
Baca paper ini dan ekstrak informasi berikut. Hanya tulis apa yang
ada di paper — jangan tambahkan analisis.

IDENTIFIKASI PAPER
- Judul:
- Topik yang disurvei:
- Rentang tahun literatur yang dicakup:

CAKUPAN SURVEI
- Jumlah paper yang dianalisis:
- Kriteria inklusi/eksklusi (bagaimana paper dipilih):
- Apakah ada PRISMA diagram atau protokol pencarian? [ ] Ya  [ ] Tidak
- Database yang digunakan (IEEE Xplore, ACM, dll.):

TAKSONOMI / KATEGORISASI
- Bagaimana paper-paper dikelompokkan? (kategori utama):
- Apakah ada taksonomi/framework klasifikasi baru yang diusulkan? [ ] Ya  [ ] Tidak

ANALISIS KOMPARATIF
- Apakah ada tabel perbandingan paper? [ ] Ya  [ ] Tidak
- Dimensi perbandingan yang digunakan:
- Apakah ada identifikasi research gap? [ ] Ya  [ ] Tidak

TEMUAN UTAMA
- Trend utama yang ditemukan (daftar 3-5 poin):
- Open challenges / future directions yang disebut:

REFERENSI
- Jumlah total referensi:
- Apakah ada paper setelah 2022 yang disurvei?
```

### Contoh Hasil Ekstraksi (Template C):
```
IDENTIFIKASI PAPER
- Judul: "A Survey of Federated Learning for Healthcare Applications: 2018-2024"
- Topik: Federated Learning di domain kesehatan
- Rentang tahun: 2018–2024

CAKUPAN SURVEI
- Jumlah paper dianalisis: 87 paper
- Kriteria inklusi: paper peer-reviewed, bahasa Inggris, FL + healthcare
- PRISMA diagram: Ya (Figure 1)
- Database: IEEE Xplore, PubMed, ACM DL, Scopus

TAKSONOMI
- Kategori: (1) FL untuk EHR, (2) FL untuk medical imaging,
  (3) FL untuk drug discovery, (4) Privacy mechanisms in FL
- Framework klasifikasi baru: Ya — "HealthFL Taxonomy" (Figure 3)

ANALISIS KOMPARATIF
- Tabel perbandingan: Ya (Table 2, Table 3)
- Dimensi: dataset, FL strategy, privacy method, evaluation metric
- Research gap: Ya (Section 6)

TEMUAN UTAMA
- Non-IID data masih menjadi tantangan utama
- Differential privacy paling banyak digunakan (43% paper)
- Kurangnya benchmark dataset standar untuk FL healthcare
- Mayoritas evaluasi masih simulasi, bukan real deployment
- Regulasi HIPAA/GDPR belum banyak diintegrasikan

REFERENSI
- Total: 142 referensi
- Paper setelah 2022: Ya (31 paper)
```

---

## Template D — Paper Information Systems / Aplikasi Bisnis

**Cocok untuk:** paper yang mengembangkan atau mengevaluasi sistem informasi, aplikasi, atau solusi bisnis

### Prompt Ekstraksi:
```
Baca paper ini dan ekstrak informasi berikut. Hanya tulis apa yang
ada di paper — jangan tambahkan analisis.

IDENTIFIKASI PAPER
- Judul:
- Domain aplikasi (e.g., e-commerce, ERP, healthcare IS):
- Tipe studi: [ ] Pengembangan sistem  [ ] Evaluasi sistem  [ ] Studi kasus

MASALAH & KONTEKS
- Masalah organisasi/bisnis yang diangkat:
- Konteks organisasi (skala, sektor):
- Klaim kontribusi utama (kutip langsung):

METODOLOGI PENELITIAN
- Metode penelitian yang digunakan (design science, case study, survey, dll.):
- Apakah ada theoretical framework? Sebutkan:
- Apakah ada user study / stakeholder involvement? [ ] Ya  [ ] Tidak

SISTEM / ARTEFAK YANG DIHASILKAN
- Nama sistem/artefak:
- Fitur utama (daftar):
- Apakah prototype atau implementasi nyata?

EVALUASI
- Bagaimana sistem dievaluasi? (usability test, expert evaluation, dll.)
- Jumlah partisipan (jika ada user study):
- Metrik yang digunakan:
- Hasil utama evaluasi:

REFERENSI
- Total referensi:
- Apakah mengutip teori IS yang relevan (TAM, DeLone-McLean, dll.)?
```

### Contoh Hasil Ekstraksi (Template D):
```
IDENTIFIKASI PAPER
- Judul: "Smart Inventory Management System for SME Using IoT and AI"
- Domain: UMKM, inventory management
- Tipe: [✓] Pengembangan sistem

MASALAH & KONTEKS
- Masalah: UMKM sering mengalami stockout atau overstock karena pencatatan
  inventori manual yang tidak akurat
- Konteks: UMKM retail di Indonesia, 1-10 karyawan
- Klaim: "Our system reduces stockout incidents by 67% compared to
  manual inventory management"

METODOLOGI PENELITIAN
- Metode: Design Science Research Methodology (DSRM)
- Theoretical framework: Technology Acceptance Model (TAM)
- User involvement: Ya — 3 UMKM sebagai case study

SISTEM YANG DIHASILKAN
- Nama: "SmartStock"
- Fitur: RFID scanning, demand forecasting (ARIMA), alert notifikasi
- Status: Implementasi nyata di 3 UMKM selama 3 bulan

EVALUASI
- Metode: Quasi-experiment + TAM questionnaire
- Partisipan: 15 pengguna (5 per UMKM)
- Metrik: Stockout rate, inventory accuracy, TAM score (PU, PEOU)
- Hasil: Stockout -67%, accuracy +34%, TAM score rata-rata 4.2/5

REFERENSI
- Total: 28 referensi
- Teori IS: Ya — TAM (Davis, 1989), DSRM (Hevner, 2004)
```

---

## Kustomisasi Template: Tambahkan Poin Sesuai Keahlian Kamu

Tambahkan poin spesifik di bagian **SETUP EKSPERIMEN** atau **EVALUASI** sesuai bidang:

**Jika kamu ahli Computer Vision:**
```
- Apakah ada visualisasi hasil (confusion matrix, saliency map)?
- Apakah diuji pada berbagai resolusi / kondisi pencahayaan?
- Pre-trained backbone yang digunakan (ImageNet, COCO, dll.)?
```

**Jika kamu ahli NLP:**
```
- Apakah ada analisis error per kategori?
- Language model yang digunakan (BERT, GPT, T5, dll.)?
- Apakah diuji lintas domain / zero-shot?
```

**Jika kamu ahli Network / Security:**
```
- Threat model yang digunakan (jika ada)?
- Apakah diuji terhadap adversarial attack?
- Overhead performa sistem vs. keamanan yang diberikan?
```

**Jika kamu ahli IoT / Embedded:**
```
- Resource constraint yang dipertimbangkan (RAM, CPU, power)?
- Apakah diuji di hardware nyata atau hanya simulasi?
- Latency komunikasi antar perangkat?
```

---

## Checklist Setelah Ekstraksi

Sebelum lanjut ke tugas review, pastikan:

- [ ] Baca hasil ekstraksi dari awal sampai akhir
- [ ] Perbaiki angka atau nama yang salah tangkap AI
- [ ] Catat secara mental: **mana bagian yang paling lemah** menurut insting expert kamu
- [ ] Catat: **apa yang tidak ada** tapi seharusnya ada
- [ ] Baru lanjutkan ke tugas review berdasarkan hasil ekstraksi ini

---

*Template ini adalah bagian dari `panduan-review-paper-icicos-chatgpt.md`*
*Juni 2026*
