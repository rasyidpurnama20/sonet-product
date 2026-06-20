# Review Prompts — ICICoS 2026
> Gunakan setelah `review-skill.md` selesai · Juni 2026

---

**Alur kerja:**
```
review-skill.md  →  A: Analisis  →  B: Draft Review  →  C: Isi Template
(ekstraksi)         (pilih 1)       (pilih 1)            (fill_review.py)
```

> **⚠ Prinsip utama:** Semua output AI di bawah adalah **draf mentah**.
> Tulis ulang setiap kalimat dengan gaya dan kata-katamu sendiri sebelum submit.
> AI menyediakan struktur dan fakta — kamu yang menentukan kalimat final.

---

## A — Analisis Mendalam

*Pilih salah satu. Jalankan sebelum menulis draft review.*

---

### A1 — Kekuatan & Kelemahan Terstruktur

Gunakan jika ingin pemetaan cepat sebelum menulis.

```
Berdasarkan hasil ekstraksi paper ini:
[paste hasil dari review-skill.md]

Identifikasi secara terstruktur:

KEKUATAN (minimal 2, urut dari paling signifikan)
Untuk setiap kekuatan: sebutkan section/tabel/halaman yang mendukungnya.

KELEMAHAN (minimal 2, urut dari paling kritis)
Untuk setiap kelemahan:
  - Jelaskan masalahnya (section/halaman spesifik)
  - Berikan satu saran perbaikan yang konkret dan actionable

SATU PERTANYAAN KRITIS
Satu pertanyaan yang paling penting untuk ditanyakan ke penulis.

ATURAN OUTPUT:
- Bahasa Inggris formal, kalimat aktif
- Setiap poin wajib menyebut section/tabel/halaman — tidak boleh generik
- Jangan tulis frasa seperti "The paper is well-written" atau "interesting work"
- Ini adalah bahan mentah — bukan teks final
```

> Setelah dapat output: coret kekuatan/kelemahan yang tidak kamu setujui,
> tambahkan yang terlewat berdasarkan pengetahuan domain kamu.

---

### A2 — Stress-Test Klaim Utama

Gunakan jika kamu ingin menguji seberapa kuat klaim paper sebelum menulis.

```
Klaim utama paper ini:
[paste klaim kontribusi dari hasil ekstraksi]

Lakukan stress-test terhadap klaim di atas:

1. BUKTI YANG ADA
   Bukti apa yang diberikan penulis untuk mendukung klaim ini?
   (sebutkan tabel/figure/section spesifik)

2. KONDISI BATAS
   Dalam kondisi apa klaim ini TIDAK berlaku atau melemah?
   Apakah kondisi pengujian cukup representatif?

3. PEMBANDING YANG HILANG
   Adakah baseline atau perbandingan yang seharusnya ada tapi tidak dikerjakan?

4. VERDICT
   Apakah klaim ini: Terbukti kuat / Terbukti dengan syarat / Belum cukup terbukti
   Justifikasi dalam 2 kalimat.

ATURAN OUTPUT:
- Semua jawaban harus merujuk ke isi paper secara eksplisit
- Jika tidak ada bukti untuk suatu poin, tulis "tidak ditemukan di paper"
- Jangan berasumsi atau mengarang data yang tidak ada di paper
```

> Setelah dapat output: verdict di poin 4 akan membantu kamu memilih
> antara Minor Revision dan Major Revision di bagian B.

---

## B — Draft Review

*Pilih salah satu. Output ini yang akan kamu edit menjadi review final.*

---

### B1 — Draft Review Lengkap

Gunakan untuk mayoritas paper. Menghasilkan semua section review sekaligus.

```
Berdasarkan ekstraksi dan analisis paper ini, tulis draft review formal.

SUMMARY  (2–3 kalimat)
Ringkas apa yang dilakukan paper, metode utama, dan kesan umum.

STRENGTHS  (2–3 poin bernomor)
Kekuatan paper dengan referensi section/tabel/halaman.

WEAKNESSES AND SUGGESTIONS  (2–4 poin bernomor)
Untuk setiap kelemahan: jelaskan masalah + berikan saran perbaikan spesifik.
Urutkan dari yang paling kritis.

QUESTIONS FOR AUTHORS  (1–3 pertanyaan)
Pertanyaan yang membutuhkan jawaban penulis jika revisi diterima.

ATURAN OUTPUT:
- Bahasa Inggris formal, kalimat aktif, panjang per poin: 2–4 kalimat
- Setiap poin weakness WAJIB ada saran perbaikan yang konkret
- Setiap komentar WAJIB menyebut section/halaman/tabel spesifik
- Hindari: "The authors should consider...", "It would be nice if..."
- Gunakan kalimat langsung: "Section 3.2 does not explain...", "Table 2 shows..."
- Ini draf — reviewer akan menulis ulang dengan gaya dan kata-katanya sendiri
```

> Setelah dapat output: **tulis ulang setiap kalimat**. Ganti kata yang
> bukan gaya kamu. Tambahkan referensi dari pengetahuan domain kamu.
> Hapus komentar yang tidak kamu setujui.

---

### B2 — Tiga Variasi Severity untuk Weakness Utama

Gunakan jika ragu apakah suatu kelemahan layak Major atau Minor Revision.

```
Kelemahan yang ingin saya evaluasi:
[paste satu kelemahan spesifik dari hasil A1 atau A2]

Tulis TIGA VERSI komentar reviewer untuk kelemahan ini:

VERSI 1 — Major Revision
Tone: masalah serius, minta perubahan metodologi atau eksperimen tambahan.
Panjang: 3–4 kalimat. Sertakan: apa yang harus dilakukan + mengapa kritis.

VERSI 2 — Minor Revision
Tone: konstruktif, minta klarifikasi atau tambahan analisis kecil.
Panjang: 2–3 kalimat. Sertakan: saran spesifik yang bisa dikerjakan cepat.

VERSI 3 — Accept with Comment
Tone: ringan, hanya meminta penjelasan lebih jelas di teks paper.
Panjang: 1–2 kalimat. Tidak meminta eksperimen baru.

ATURAN OUTPUT:
- Ketiga versi menyebut section/halaman yang sama (kelemahan yang sama)
- Perbedaan HANYA pada severity dan apa yang diminta, bukan pada fakta
- Bahasa Inggris formal, kalimat aktif
- Di akhir, rekomendasikan: versi mana yang paling sesuai untuk kondisi ini?
```

> Setelah dapat output: pilih versi yang paling mencerminkan penilaianmu,
> lalu tulis ulang kalimatnya dengan kata-katamu sendiri.

---

## C — Isi Template

*Jalankan setelah draft review final selesai diedit.*

---

### C1 — Generate Data untuk fill_review.py

```
Berdasarkan review final yang sudah kita buat, isi Python dict berikut.
Tulis dalam bahasa Inggris formal. Jangan sisakan field kosong kecuali "confidential".

review_data = {
    "paper_id"          : "...",
    "paper_title"       : "...",
    "reviewer_id"       : "...",

    "score_originality" : "...",   # angka 1–5
    "score_technical"   : "...",
    "score_clarity"     : "...",
    "score_relevance"   : "...",
    "score_references"  : "...",
    "score_overall"     : "...",

    "summary"           : "...",
    "strengths"         : "...",   # format: "1. ...\n2. ...\n3. ..."
    "weaknesses"        : "...",   # format: "1. ...\n2. ...\n3. ..."
    "questions"         : "...",   # format: "1. ...\n2. ..."
    "confidential"      : "",      # kosongkan jika tidak ada

    # TULIS PERSIS salah satu opsi (case-sensitive):
    # "Accept" | "Minor Revision" | "Major Revision" | "Reject"
    "decision"          : "...",

    # "Expert" | "Knowledgeable" | "Passing Knowledge" | "Basic"
    "confidence"        : "...",
}

Sebelum output, verifikasi:
- score_overall konsisten dengan decision
- Isi strengths/weaknesses sesuai dengan draft review final yang sudah diedit
- Tidak ada nama penulis atau institusi yang disebut (blind review)
```

> Setelah dapat dict: paste ke Bagian 1 di `fill_review.py`, lalu jalankan:
> ```
> python3 fill_review.py
> ```
> Output tersimpan di `review-filled.docx`. Buka dan verifikasi sebelum submit.

---

## Ringkasan Cepat

| Prompt | Kapan digunakan | Waktu |
|--------|----------------|-------|
| A1 | Pemetaan kekuatan & kelemahan | ~5 mnt |
| A2 | Meragukan kekuatan klaim paper | ~5 mnt |
| B1 | Draft review standar (mayoritas kasus) | ~8 mnt |
| B2 | Ragu minor vs major untuk satu weakness | ~5 mnt |
| C1 | Siap isi template setelah edit final | ~5 mnt |


---

## D — Tips & Tricks ChatGPT yang Jarang Diketahui

> Bagian ini berdiri sendiri — bisa dipakai di prompt manapun, bukan hanya untuk review.
> Semua contoh disesuaikan dengan konteks review paper ICICoS.

---

### T1 — Interview Mode: Biarkan AI Tanya Kamu Dulu

*Mengapa powerful:* AI tidak punya konteks yang kamu punya. Dengan memintanya bertanya dulu, output yang dihasilkan jauh lebih tepat sasaran dan tidak generik.

```
Saya akan meminta kamu membantu menulis review paper ICICoS.
Sebelum mulai, ajukan 3–4 pertanyaan klarifikasi yang paling
penting agar kamu bisa membantu saya lebih efektif.
Jangan hasilkan review dulu — tanya dulu.
```

> Kamu akan dapat pertanyaan seperti: *"Apakah ini paper ML atau sistem?"*,
> *"Apa keputusan awal kamu?"*, *"Adakah paper yang kamu tahu seharusnya dikutip tapi tidak?"*
> Jawab pertanyaan-pertanyaan itu, baru minta output. Hasilnya akan langsung relevan.

---

### T2 — Pre-Mortem: Balik Framing

*Mengapa powerful:* Bertanya "apa kelemahannya?" menghasilkan daftar permukaan.
Bertanya "kenapa paper ini ditolak?" memaksa AI mencari argumen yang *benar-benar substantif*.

```
Bayangkan paper ini sudah disubmit ke ICICoS dan DITOLAK.
Tulis keputusan penolakan fiktif dari editor, 150 kata,
berisi 3 alasan penolakan yang paling sering dikutip untuk
paper tipe ini. Gunakan hasil ekstraksi berikut sebagai dasar:
[paste hasil review-skill.md]
```

> Output-nya akan terasa lebih tajam dan lebih mudah kamu konversi ke weakness comments
> daripada jika kamu tanya "apa kelemahan paper ini?"

---

### T3 — Steelman First, Lalu Serang

*Mengapa powerful:* Kalau kamu langsung minta AI mencari kelemahan, ia akan mencari kelemahan kecil.
Kalau kamu paksa AI membangun argumen terkuat untuk paper dulu,
kelemahannya akan ditemukan dari tempat yang lebih dalam.

```
LANGKAH 1 — Bangun argumen TERKUAT yang mendukung paper ini.
Anggap kamu adalah co-author yang akan mempertahankan paper ini
di hadapan reviewer skeptis. Tulis argumen terbaik untuk setiap
klaim kontribusi. Panjang: 150 kata.

LANGKAH 2 — Sekarang, identifikasi lubang dalam argumen yang
baru saja kamu buat sendiri. Di mana argumen itu paling lemah?
Apa yang tidak bisa dipertahankan tanpa data tambahan?
```

> Kelemahan yang ditemukan dari cara ini biasanya lebih akurat dan
> lebih sulit dibantah oleh penulis.

---

### T4 — Persona dengan Failure Mode

*Mengapa powerful:* "Berperan sebagai reviewer IEEE" terlalu umum — AI akan menghasilkan komentar standar.
Menambahkan *domain spesifik* dan *kebiasaan khas* reviewer itu mengunci AI ke perspektif yang jauh lebih tajam.

```
Kamu adalah senior reviewer yang telah me-review 60+ paper
tentang machine learning untuk aplikasi geofisika di IEEE TGRS
dan MDPI Remote Sensing. Kamu dikenal sangat teliti soal
reproducibility dan sering menolak paper yang tidak menyertakan
kode atau detail training yang cukup.

Dengan karakter ini, baca ekstraksi paper berikut dan tulis
satu paragraf komentar untuk bagian "Experimental Setup":
[paste ekstraksi Fase 2 dari review-skill.md]
```

> Komentar yang dihasilkan akan lebih domain-specific dan lebih sulit dibantah.
> Ganti domain dan fokus sesuai bidang paper yang sedang kamu review.

---

### T5 — Negative Sample Injection

*Mengapa powerful:* Memberitahu AI apa yang TIDAK boleh ditulis lebih efektif
daripada mendeskripsikan apa yang HARUS ditulis.
Ini memotong seluruh kategori output buruk sekaligus.

```
Tulis weakness comment untuk paper ini berdasarkan:
[paste kelemahan dari A1]

DILARANG menulis kalimat seperti:
- "The authors should consider adding..."
- "It would be beneficial to include..."
- "The paper could be improved by..."
- "This is an interesting paper, however..."

Setiap kalimat harus langsung ke masalah:
"Section X does not...", "Table Y fails to...", "The claim in line Z..."
Panjang: 3–4 kalimat.
```

> Perbedaannya mencolok. Tanpa pembatasan ini, AI hampir selalu menggunakan
> frasa hedging yang tidak profesional dalam konteks peer review.

---

### T6 — Kill Your Darlings

*Mengapa powerful:* Setelah AI menghasilkan review, ia tidak tahu mana komentar yang paling mudah dibantah penulis.
Kamu bisa paksa AI untuk mengevaluasi outputnya sendiri — dan memperkuat bagian yang lemah.

```
Berikut draft review yang sudah kamu buat:
[paste output dari B1]

Sekarang identifikasi: dari semua weakness comment di atas,
mana 2 yang paling mudah dibantah oleh penulis?
Jelaskan kenapa, lalu tulis versi yang lebih kuat untuk masing-masing
dengan bukti yang lebih spesifik dari paper.
```

> Proses ini biasanya mengungkap komentar yang terlalu generik
> atau yang tidak punya referensi section/halaman yang kuat.

---

### T7 — Format sebagai Scaffold Berpikir

*Mengapa powerful:* Output format bukan hanya soal estetika — ia memaksa AI *berpikir dalam urutan tertentu*.
Format yang tepat bisa membuat AI menangkap hal yang biasanya terlewat.

```
Untuk setiap weakness yang kamu temukan, tulis dalam format ini:
(a) Yang saya HARAPKAN ada di paper berdasarkan klaimnya
(b) Yang SAYA TEMUKAN sebenarnya ada di paper
(c) GAP antara (a) dan (b)
(d) Saran perbaikan spesifik

Jangan skip format. Isi semua empat bagian untuk setiap poin.
```

> Format tiga-bagian (harap–temukan–gap) memaksa AI mendeteksi inkonsistensi
> antara klaim dan bukti — sesuatu yang sering terlewat dengan prompt biasa.

---

### T8 — Confidence Tagging

*Mengapa powerful:* AI sering menyampaikan spekulasi dengan keyakinan yang sama seperti fakta.
Dengan memintanya menandai tingkat kepercayaan, kamu tahu persis mana yang perlu kamu verifikasi manual.

```
Setelah setiap komentar review yang kamu tulis, tambahkan tag:
[TINGGI] — kamu yakin ini didukung langsung oleh isi paper
[SEDANG] — kamu menduga ini benar tapi perlu dikonfirmasi reviewer
[RENDAH]  — ini asumsi atau inferensi, reviewer harus verifikasi sendiri

Contoh format:
"Section 3.2 does not provide the train/val/test split ratio,
making the results difficult to reproduce. [TINGGI]"

Tulis review untuk paper ini dengan format tersebut.
```

> Semua komentar berlabel [RENDAH] adalah bagian yang harus kamu buka
> langsung di PDF dan verifikasi sebelum submit — jangan percaya begitu saja.

---

> **Cara kombinasikan tips ini:**
> Mulai dengan **T1** (biarkan AI tanya dulu) →
> Gunakan **T4** (persona) saat menjalankan B1 →
> Terapkan **T8** (confidence tag) pada semua output →
> Selesaikan dengan **T6** (kill your darlings) sebelum finalisasi.
