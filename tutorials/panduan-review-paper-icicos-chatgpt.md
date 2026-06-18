# Panduan Review Paper ICICOS dengan ChatGPT Plus
> Untuk dosen reviewer ICICOS — praktis, berbasis keahlian, efisien
> Juni 2026

---

## Daftar Isi
1. [Review Paper = Cerminan Keahlian Kamu](#1-review-paper--cerminan-keahlian-kamu)
2. [Setup ChatGPT Plus + Project](#2-setup-chatgpt-plus--project)
3. [Langkah Inti: Ekstraksi Paper Dulu](#3-langkah-inti-ekstraksi-paper-dulu)
4. [AI adalah Pelaksana Tugas, Bukan Penjawab Pertanyaan](#4-ai-adalah-pelaksana-tugas-bukan-penjawab-pertanyaan)
5. [Dari Ekstraksi ke Poin Review Siap Pakai](#5-dari-ekstraksi-ke-poin-review-siap-pakai)
6. [Jaga Bias, Variasi, dan Konsistensi](#6-jaga-bias-variasi-dan-konsistensi)
7. [Penutup: Kamu yang Ahli, AI yang Mengerjakan](#7-penutup-kamu-yang-ahli-ai-yang-mengerjakan)

---

## 1. Review Paper = Cerminan Keahlian Kamu

Review yang baik bukan sekadar "paper ini bagus/jelek". Review yang baik adalah **penilaian expert** — mencerminkan pengalaman dan bidang kamu.

### Apa yang sebenarnya dilakukan reviewer?

Bergantung pada bidang keahlian, reviewer memiliki fokus yang berbeda:

**Reviewer Machine Learning / AI:**
- Cek arsitektur model — apakah logis dan justified?
- Cek baseline — apakah dibandingkan dengan SOTA terbaru?
- Cek dataset — train/test split, leakage, representatif?
- Cek metrik — accuracy saja tidak cukup, perlu F1/AUC/dll.
- Cek ablation study — apakah tiap komponen dibuktikan kontribusinya?

**Reviewer Software Engineering / Sistem:**
- Cek arsitektur sistem — scalable? modular?
- Cek evaluasi performa — latency, throughput, memory usage
- Cek deployment context — realistic use case?
- Cek reproducibility — codebase tersedia? instruksi lengkap?

**Reviewer Information Systems / Aplikasi:**
- Cek problem relevance — masalah nyata atau akademis saja?
- Cek user study — ada validasi pengguna nyata?
- Cek implementasi — bukan hanya konsep/prototype?
- Cek business value — manfaat praktisnya jelas?

**Reviewer Umum (semua paper):**
- Apakah novelty diklaim dengan benar?
- Apakah kesimpulan konsisten dengan data?
- Apakah referensi relevan dan up-to-date?
- Apakah penulisan jelas dan terstruktur?

---

### Skenario: Tiga Reviewer, Satu Paper

**Paper:** "Deep Learning-based Intrusion Detection System for IoT Networks"

| Reviewer | Fokus Utama | Komentar Khas |
|----------|-------------|---------------|
| **Ahli Security** | Threat model, attack coverage | "Dataset hanya mencakup 4 tipe serangan, tidak representatif untuk lingkungan IoT production" |
| **Ahli Deep Learning** | Arsitektur, training setup | "Tidak ada ablation study — kontribusi layer attention tidak dibuktikan terpisah" |
| **Ahli IoT Systems** | Deployment, resource constraint | "Model 47MB tidak mungkin di-deploy di microcontroller — evaluasi resource overhead tidak ada" |

**Poin penting:** Ketiga komentar di atas valid, tapi muncul dari *perspektif yang berbeda*. ChatGPT perlu tahu **perspektif kamu** untuk menghasilkan review yang relevan.

**Inilah kenapa setup awal itu krusial** — kamu perlu "menanamkan" keahlian dan preferensi kamu ke dalam sistem sebelum meminta ChatGPT bekerja.

---

## 2. Setup ChatGPT Plus + Project

### Kenapa Project, Bukan Chat Biasa?

| Chat Biasa | Project ChatGPT Plus |
|------------|---------------------|
| Konteks hilang setiap sesi baru | Konteks permanen — ingat style kamu |
| Harus jelaskan ulang setiap kali | Cukup setup sekali untuk semua paper ICICOS |
| File hilang setelah sesi | File tersimpan, bisa dirujuk kapan saja |
| Tidak bisa dikustomisasi | Custom instructions = "DNA" reviewer kamu |

### Setup dalam 3 Langkah

**Langkah 1 — Buat Project**
- Buka chatgpt.com → sidebar kiri → klik **+** di samping "Projects"
- Nama: `ICICOS Reviewer — [Nama Kamu]`

**Langkah 2 — Isi Custom Instructions (ini yang terpenting)**

Klik ⚙️ di project → Edit → isi dengan template berikut, **sesuaikan bagian `[...]`**:

```
Kamu adalah asisten review ilmiah untuk konferensi ICICOS.

IDENTITAS REVIEWER:
- Bidang keahlian utama saya: [contoh: Machine Learning, Computer Vision]
- Bidang keahlian sekunder: [contoh: IoT, Sistem Terdistribusi]
- Standar yang saya pegang: IEEE conference, ACM
- Hal yang saya prioritaskan saat review:
  [contoh: reproducibility, kekuatan eksperimen, relevansi baseline]

ATURAN KERJA:
- Selalu tunjukkan reasoning sebelum kesimpulan
- Selalu sebut nomor halaman/section/tabel yang dirujuk
- Jaga blind review — jangan sebut atau tebak identitas penulis
- Bahasa output: Inggris formal untuk review, Indonesia untuk diskusi kita

GAYA KOMENTAR SAYA:
- [contoh: Direct dan spesifik, tidak perlu basa-basi]
- [contoh: Selalu sertakan saran perbaikan untuk setiap kelemahan]
- [contoh: Prioritaskan masalah metodologi di atas masalah penulisan]
```

**Langkah 3 — Upload File Pendukung**
- Upload form review resmi ICICOS (PDF dari panitia)
- Upload template ekstraksi paper (lihat file `template-ekstraksi-paper.md`)

---

## 3. Langkah Inti: Ekstraksi Paper Dulu

### Prinsip: Jangan Langsung Minta Review

❌ **Yang sering dilakukan (kurang efektif):**
```
Upload PDF → "Tolong review paper ini"
```
Hasilnya: generik, tidak sesuai ekspektasi kamu, perlu banyak revisi.

✅ **Yang seharusnya dilakukan:**
```
Upload PDF → Ekstrak dulu → Beri tugas spesifik berdasarkan hasil ekstraksi
```
Hasilnya: tajam, sesuai standar kamu, langsung bisa dipakai.

---

### Kenapa Ekstraksi Itu Penting?

- Paper PDF panjang dan berantakan — ChatGPT bisa kehilangan fokus
- Ekstraksi **memaksa struktur** — kamu tahu persis informasi apa yang sudah ditangkap AI
- Hasil ekstraksi bisa kamu **koreksi dulu** sebelum dilanjutkan ke analisis
- Lebih mudah **menemukan gap** antara apa yang diklaim paper vs. apa yang sebenarnya ada

---

### Cara Ekstraksi: Upload + Prompt Ekstraksi

Upload PDF ke chat dalam Project, lalu kirim prompt ekstraksi dari file `template-ekstraksi-paper.md`.

**Contoh prompt ekstraksi singkat (versi umum):**
```
Baca paper ini dan ekstrak informasi berikut secara singkat dan faktual.
Jangan analisis dulu — hanya ekstrak apa yang tertulis di paper.

1. Masalah yang diselesaikan (1-2 kalimat)
2. Metode yang diusulkan (nama + ide utama)
3. Dataset yang digunakan (nama, ukuran, sumber)
4. Metrik evaluasi yang dipakai
5. Hasil terbaik yang diklaim (angka spesifik)
6. Baseline yang digunakan untuk perbandingan
7. Klaim kontribusi utama (kutip langsung dari paper)
8. Keterbatasan yang diakui penulis (jika ada)
```

**Contoh hasil ekstraksi (singkat):**
```
1. Masalah: Deteksi intrusi pada jaringan IoT dengan false positive rate tinggi
2. Metode: BiLSTM + Attention Mechanism (disebut "IoTGuard")
3. Dataset: NSL-KDD (125.973 record), UNSW-NB15 (257.673 record)
4. Metrik: Accuracy, Precision, Recall, F1-Score
5. Hasil terbaik: Accuracy 98.7% di NSL-KDD, 96.2% di UNSW-NB15
6. Baseline: KNN, SVM, Random Forest, standard LSTM
7. Klaim: "First attention-based BiLSTM for IoT intrusion detection"
8. Keterbatasan: Tidak disebutkan secara eksplisit
```

Sekarang kamu punya **peta paper** yang bisa langsung dijadikan dasar tugas review.

> File `template-ekstraksi-paper.md` berisi template lengkap untuk berbagai tipe paper (ML, sistem, survei) beserta contoh prompt dan hasil ekstraksinya.

---

## 4. AI adalah Pelaksana Tugas, Bukan Penjawab Pertanyaan

### Pergeseran Mindset yang Paling Penting

Kebanyakan orang pakai ChatGPT seperti mesin pencari:
> "Apa kelemahan paper ini?"

Padahal ChatGPT bekerja paling efektif ketika diberi **tugas yang jelas**, bukan pertanyaan terbuka.

---

### Perbedaan: Pertanyaan vs. Tugas

| ❌ Pertanyaan (lemah) | ✅ Tugas (kuat) |
|----------------------|----------------|
| "Apa kelemahan paper ini?" | "Berdasarkan hasil ekstraksi, identifikasi apakah baseline yang digunakan (KNN, SVM, RF, LSTM) sudah mencakup metode terbaru 2022-2024 untuk task ini. Jika ada gap, sebutkan paper spesifik yang seharusnya dijadikan baseline." |
| "Bagaimana metodologinya?" | "Cek Section 3: apakah ada penjelasan tentang hyperparameter tuning? Jika tidak ada, tuliskan komentar reviewer yang meminta penjelasan cara pemilihan learning rate, batch size, dan jumlah epoch." |
| "Apakah hasilnya valid?" | "Dataset yang digunakan adalah NSL-KDD (2009). Buat komentar reviewer yang mengevaluasi apakah dataset ini masih relevan untuk paper tahun 2025 tentang ancaman IoT modern." |
| "Review bagian referensi" | "Dari daftar referensi, identifikasi paper mana yang terbit setelah 2020 dan mana yang lebih tua dari 2018. Kemudian nilai apakah komposisi ini wajar untuk paper tentang deep learning yang ditulis tahun 2025." |

---

### Struktur Tugas yang Efektif

Setiap tugas review yang baik punya tiga komponen:

```
[KONTEKS] + [INSTRUKSI SPESIFIK] + [FORMAT OUTPUT]
```

**Contoh:**
```
KONTEKS:
Paper ini mengklaim kontribusi "first attention-based BiLSTM for IoT IDS".
Hasil ekstraksi: accuracy 98.7% di NSL-KDD.

INSTRUKSI:
Evaluasi validitas klaim "first" ini. Cek apakah referensi di paper
sudah mencakup paper attention + LSTM untuk network intrusion detection.
Identifikasi apakah ada celah dalam klaim novelty ini.

FORMAT OUTPUT:
- Poin 1: Temuan tentang klaim "first"
- Poin 2: Paper dalam referensi yang paling mirip
- Poin 3: Draft komentar reviewer (dalam bahasa Inggris, 3-4 kalimat)
```

---

### Contoh Tugas per Area Review

**Tugas untuk Cek Novelty:**
```
Berdasarkan klaim kontribusi: "[paste klaim dari hasil ekstraksi]"
dan daftar referensi yang ada di paper, evaluasi:
- Apakah klaim ini didukung perbandingan literatur yang memadai?
- Apakah ada paper dalam referensi yang sudah melakukan hal serupa?
Tulis draft komentar reviewer dalam 3-4 kalimat bahasa Inggris.
```

**Tugas untuk Cek Eksperimen:**
```
Dari hasil ekstraksi:
- Dataset: [nama, ukuran]
- Metrik: [daftar]
- Baseline: [daftar]
- Hasil: [angka]

Identifikasi 3 pertanyaan eksperimental yang belum dijawab paper
yang wajib saya tanyakan sebagai reviewer. Format: pertanyaan langsung,
bisa langsung masuk ke form review.
```

**Tugas untuk Cek Penulisan:**
```
Baca Abstract dan Conclusion paper ini.
Identifikasi: apakah ada klaim di Abstract yang tidak didukung
bukti di Conclusion atau Results? Buat tabel dua kolom:
Klaim di Abstract | Status (Didukung/Tidak/Parsial)
```

---

## 5. Dari Ekstraksi ke Poin Review Siap Pakai

### Alur Lengkap dalam 5 Langkah

```
1. UPLOAD paper ke Project ChatGPT Plus
       ↓
2. EKSTRAKSI — kirim prompt dari template-ekstraksi-paper.md
       ↓
3. KOREKSI — baca hasil ekstraksi, perbaiki jika ada yang salah tangkap
       ↓
4. BERI TUGAS — satu tugas per area (novelty, metodologi, hasil, referensi)
       ↓
5. EDIT & SUBMIT — edit output AI dengan perspektif expert kamu
```

---

### Contoh Nyata: Dari Ekstraksi ke Draft Review

**Hasil ekstraksi (item 6):**
> Baseline: KNN, SVM, Random Forest, standard LSTM

**Tugas ke ChatGPT:**
```
Baseline yang digunakan: KNN, SVM, Random Forest, standard LSTM.
Paper ini ditulis tahun 2025 untuk domain IoT Intrusion Detection.

Tugas: Evaluasi apakah baseline ini up-to-date.
Cari di daftar referensi paper — apakah ada metode transformer,
GNN, atau federated learning yang juga dipakai untuk IDS?
Tulis komentar reviewer (bahasa Inggris, 3-4 kalimat) yang
mempertanyakan kelengkapan baseline comparison.
```

**Output ChatGPT (langsung bisa dipakai dengan sedikit edit):**
```
The baseline comparison appears limited to classical ML methods and a
standard LSTM. Given the rapid evolution of deep learning for network
intrusion detection, the authors should include more recent baselines
such as Transformer-based IDS [cite], Graph Neural Network approaches
[cite], or at minimum, more recent LSTM variants published after 2022.
The absence of these comparisons weakens the claim that the proposed
method achieves state-of-the-art performance.
```

Kamu tinggal **tambahkan referensi spesifik** dari pengetahuan domain kamu — itulah kontribusi keahlian yang tidak bisa digantikan AI.

---

## 6. Jaga Bias, Variasi, dan Konsistensi

### Bias yang Perlu Diwaspadai

**Bias "Terlalu Setuju"**
- ChatGPT cenderung mengonfirmasi framing yang kamu berikan
- ❌ Jangan: "Paper ini bagus kan, tapi ada kelemahannya?"
- ✅ Lakukan: "Identifikasi kelemahan utama tanpa melihat kelebihan dulu"

**Bias Positif pada Paper yang Ditulis Bagus**
- Paper dengan bahasa Inggris yang bagus sering dapat evaluasi lebih positif
- Pisahkan evaluasi: "Abaikan kualitas bahasa — fokus hanya pada kekuatan eksperimen"

**Bias Topik Populer**
- Topik yang banyak di training data (seperti ChatGPT/LLM) cenderung dapat evaluasi lebih mudah
- Untuk topik niche, tambahkan konteks domain di custom instructions

---

### Jaga Variasi: Minta Perspektif Berbeda

Jika tidak yakin dengan satu output, minta variasi:
```
Berikan 3 versi komentar reviewer untuk kelemahan baseline ini:
- Versi 1: Komentar yang mengharuskan major revision
- Versi 2: Komentar yang menyarankan minor revision
- Versi 3: Komentar yang hanya meminta klarifikasi
```

Pilih yang paling sesuai dengan penilaian kamu.

---

### Jaga Konsistensi: Satu Session per Paper

- Jangan ganti-ganti chat untuk satu paper — gunakan satu chat dalam Project
- Jika perlu cross-check, gunakan prompt: "Apakah penilaianmu di bagian metodologi konsisten dengan penilaian novelty sebelumnya?"
- Sebelum finalisasi: "Baca ulang semua komentar yang sudah kita buat. Adakah inkonsistensi antara poin-poin tersebut?"

---

## 7. Penutup: Kamu yang Ahli, AI yang Mengerjakan

Review paper yang baik bukan tentang siapa yang paling banyak membaca — tapi tentang **kedalaman pertanyaan yang kamu ajukan**.

ChatGPT Plus dengan Project memungkinkan kamu untuk:
- **Encode keahlian kamu** satu kali → dipakai di semua paper
- **Delegasikan pekerjaan rutinitas** (ringkasan, cek konsistensi, cek struktur) ke AI
- **Fokuskan waktu kamu** pada yang benar-benar butuh judgment expert: keputusan akhir, pertanyaan kritis ke penulis, dan penilaian kontribusi nyata ke bidang

**Perkiraan waktu dengan metode ini:**
- Tanpa ChatGPT: 2–4 jam per paper
- Dengan metode ini: 30–45 menit per paper
- Kualitas review: **lebih tinggi** karena lebih terstruktur dan konsisten

**Yang tidak berubah:** Tanggung jawab keilmuan tetap di tangan kamu.
AI mengerjakan tugasnya. Kamu memimpin.

---

> **File terkait:**
> - `template-ekstraksi-paper.md` — Template ekstraksi untuk berbagai tipe paper
> - `ICICOS_Review_Presentation.pptx` — Slide presentasi panduan ini

---
*Juni 2026 — Tutorial untuk Dosen Reviewer ICICOS*
