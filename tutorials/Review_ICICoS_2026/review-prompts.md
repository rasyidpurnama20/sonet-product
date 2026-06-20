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
