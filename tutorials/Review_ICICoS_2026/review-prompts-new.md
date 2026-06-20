# Prompt Review — ICICoS 2026

Gunakan setelah `review-skill-new.md` selesai. Prompt di sini untuk analisis, penulisan draft, dan mengisi `review-template.docx`.

> Output AI adalah draf. Edit kalimatnya supaya terdengar seperti kamu yang menulis, bukan mesin.

---

## A — Analisis Sebelum Menulis

### A1 · Kekuatan dan Kelemahan

```
Berdasarkan ekstraksi paper ini:
[paste hasil review-skill-new.md]

Buat daftar terstruktur:

KEKUATAN — minimal 2, mulai dari yang paling penting.
Tiap poin: apa yang bagus dan di section/tabel/halaman mana buktinya.

KELEMAHAN — minimal 2, mulai dari yang paling serius.
Tiap poin: apa masalahnya (section/halaman) + satu saran perbaikan konkret.

SATU PERTANYAAN paling penting untuk penulis.

Bahasa Inggris formal. Tiap poin harus spesifik ke paper ini — hindari kalimat yang bisa berlaku untuk paper manapun.
```

**Hasilnya:** daftar kekuatan dan kelemahan siap pakai. Pilih yang kamu setujui, tambahkan dari pengetahuan domain kamu, edit kalimatnya.

---

### A2 · Cek Kekuatan Klaim

Berguna kalau klaim kontribusinya terasa terlalu kuat.

```
Klaim utama paper ini:
[paste klaim kontribusi]

Periksa tiga hal:

1. Bukti yang diberikan — apa yang ditunjukkan penulis untuk mendukung klaim ini? Sebut section/tabel/figure.
2. Kondisi batas — kapan klaim ini tidak berlaku? Apakah eksperimen cukup representatif?
3. Pembanding yang hilang — ada baseline atau perbandingan yang harusnya ada tapi tidak dikerjakan?

Jawab dari isi paper saja. Kalau tidak ada bukti, tulis "tidak ditemukan di paper".
```

**Hasilnya:** gambaran seberapa kuat klaim paper ini bisa dipertahankan. Berguna saat memutuskan antara Accept, Weak Accept, atau Borderline.

---

## B — Draft Review

### B0 · Draft Cepat *(2 kalimat)*

Kalau sudah cukup paham paper dan mau draft paling cepat:

```
Paper ini: [paste hasil review-skill-new.md].
Tulis draft review dengan bagian: Summary · Strengths (3 poin bernomor) · Weaknesses and Suggestions (3 poin bernomor, tiap poin ada saran perbaikan konkret) · Questions for Authors (2 poin) · Overall evaluation: pilih dari Strong Accept / Accept (revision required) / Weak Accept (revision required) / Borderline Paper (revision required) / Weak Reject / Reject / Strong Reject · Reviewer's confidence: pilih dari (Expert) / (High) / (Medium) / (Low).
```

**Hasilnya:** draft lengkap dalam sekali jalan. Edit sebelum masuk ke form.

---

### B1 · Draft Review Lengkap

```
Berdasarkan ekstraksi dan analisis paper ini, tulis draft review.

Summary (2–3 kalimat): apa yang dilakukan paper, metode utama, kesan umum.

Strengths (2–3 poin bernomor): kekuatan dengan referensi section/tabel/halaman.

Weaknesses and Suggestions (2–4 poin bernomor): tiap poin — masalahnya di mana (section/halaman) dan saran perbaikan konkretnya apa. Urutkan dari yang paling serius.

Questions for Authors (1–3 pertanyaan): yang perlu dijawab penulis kalau revisi diterima.

Bahasa Inggris formal. Hindari "The authors should consider..." atau "It would be nice if..." — langsung ke masalah: "Section 3 does not explain...", "Table 2 shows..."
```

**Hasilnya:** draft review siap edit. Biasanya perlu revisi 30–50% kalimat supaya terasa natural.

---

### B2 · Tiga Versi Bobot Kelemahan

Pakai kalau ragu seberapa serius satu kelemahan.

```
Kelemahan yang ingin dinilai:
[paste satu kelemahan spesifik]

Tulis tiga versi komentar untuk kelemahan ini:

Versi berat (mendukung Weak Reject atau lebih) — masalah fundamental yang perlu perubahan besar. 3–4 kalimat.
Versi sedang (mendukung revision required) — masalah yang perlu diperbaiki tapi masuk akal dikerjakan. 2–3 kalimat.
Versi ringan (mendukung Weak Accept) — cukup klarifikasi di teks, tidak perlu eksperimen baru. 1–2 kalimat.

Semua versi merujuk ke section/halaman yang sama. Di akhir, rekomendasikan versi mana yang paling tepat.
```

**Hasilnya:** tiga opsi komentar dengan bobot berbeda. Pilih satu, edit kalimatnya.

---

## C — Isi review-template.docx

Setelah draft review selesai diedit, jalankan script Python di bawah untuk mengisi template otomatis.

Yang dilakukan script:
- Mengganti `[paper_id]`, `[paper_title]`, `[paper_comment]` dengan konten review
- Menebalkan satu pilihan di tiap pertanyaan evaluasi
- Tidak menyentuh bagian lain template sama sekali

**Cara pakai:**
1. Isi bagian `DATA REVIEW` di bawah
2. Simpan sebagai `fill_review.py` di folder yang sama dengan `review-template.docx`
3. Jalankan: `python3 fill_review.py`
4. Buka `review-filled.docx`, cek, lalu submit

```python
"""
fill_review.py — Isi review-template.docx ICICoS 2026
Dependensi: pip install python-docx
"""
from docx import Document

# ═══════════════════════════════════════════════════
#  DATA REVIEW — isi bagian ini
# ═══════════════════════════════════════════════════
data = {
    "paper_id"    : "ICICoS-2026-001",
    "paper_title" : "Judul paper di sini",
    "paper_comment": (
        "Tulis komentar review lengkap di sini. "
        "Masukkan Summary, Strengths, Weaknesses, dan Questions dalam satu blok teks."
    ),

    # Pilih PERSIS satu dari opsi berikut:
    "overall_eval": "Accept (revision required)",
    # Opsi: Strong Accept | Accept (revision required) | Weak Accept (revision required)
    #       Borderline Paper (revision required) | Weak Reject | Reject | Strong Reject

    "confidence": "(High)",
    # Opsi: (Expert) | (High) | (Medium) | (Low)

    # Untuk tiap kriteria — pilih: Excellent | Good | Adequate | Inadequate
    "novelty"      : "Good",
    "significance" : "Good",
    "technical"    : "Adequate",
    "presentation" : "Good",
    "literature"   : "Adequate",
}

# ═══════════════════════════════════════════════════
#  KONFIGURASI — tidak perlu diubah
# ═══════════════════════════════════════════════════
TEMPLATE = "review-template.docx"
OUTPUT   = "review-filled.docx"

SECTIONS = [
    ("Overall evaluation",
     ["Strong Accept","Accept (revision required)","Weak Accept (revision required)",
      "Borderline Paper (revision required)","Weak Reject","Reject","Strong Reject"],
     "overall_eval"),
    ("Reviewer's confidence",
     ["(Expert)","(High)","(Medium)","(Low)"],
     "confidence"),
    ("Novelty/Originality",
     ["Excellent","Good","Adequate","Inadequate"], "novelty"),
    ("Significance of Topic",
     ["Excellent","Good","Adequate","Inadequate"], "significance"),
    ("Technical Quality",
     ["Excellent","Good","Adequate","Inadequate"], "technical"),
    ("Presentation",
     ["Excellent","Good","Adequate","Inadequate"], "presentation"),
    ("Literature",
     ["Excellent","Good","Adequate","Inadequate"], "literature"),
]

# ═══════════════════════════════════════════════════
#  PROSES
# ═══════════════════════════════════════════════════
def process():
    doc = Document(TEMPLATE)
    current = None  # (options, data_key)

    for para in doc.paragraphs:
        text     = para.text
        stripped = text.strip()

        # Deteksi label pertanyaan → set section aktif
        for label, opts, key in SECTIONS:
            if label in text:
                current = (opts, key)
                break

        # Isi placeholder
        for ph, field in [("[paper_id]","paper_id"),
                          ("[paper_title]","paper_title"),
                          ("[paper_comment]","paper_comment")]:
            if ph in text:
                for r in para.runs:
                    if ph in r.text:
                        r.text = r.text.replace(ph, data[field])

        # Bold pilihan yang dipilih, unbold sisanya
        if current:
            opts, key = current
            if stripped in opts:
                selected = data[key]
                for r in para.runs:
                    if r.text.strip() in opts:
                        r.bold = (r.text.strip() == selected)

    doc.save(OUTPUT)
    _check(OUTPUT)

def _check(path):
    doc   = Document(path)
    sisa  = [p.text[:50] for p in doc.paragraphs
             if any(ph in p.text for ph in ["[paper_id]","[paper_title]","[paper_comment]"])]
    bolded = [r.text.strip() for p in doc.paragraphs for r in p.runs
              if r.bold and r.text.strip() in [
                  "Strong Accept","Accept (revision required)","Weak Accept (revision required)",
                  "Borderline Paper (revision required)","Weak Reject","Reject","Strong Reject",
                  "(Expert)","(High)","(Medium)","(Low)",
                  "Excellent","Good","Adequate","Inadequate"]]
    print("Tersimpan:", path)
    print("✓ Placeholder terisi" if not sisa else f"⚠ Sisa: {sisa}")
    print("✓ Pilihan yang ditebalkan:", bolded)

if __name__ == "__main__":
    process()
```

---

## D — Tips ChatGPT yang Jarang Dipakai

---

**T1 · Minta AI Tanya Dulu**

Daripada langsung minta review, biarkan AI bertanya dulu. Output yang keluar biasanya jauh lebih pas karena AI tahu kondisi paper yang kamu pegang.

```
Saya akan minta bantuan review paper ICICoS. Sebelum mulai, tanya 3–4 hal paling penting yang perlu kamu tahu supaya bisa bantu lebih tepat. Jangan hasilkan review dulu.
```

Jawab pertanyaannya, baru minta draft. Satu pertanyaan AI kadang mengungkap hal yang sebenarnya kamu sendiri belum sadari perlu diklarifikasi.

---

**T2 · Balik Framingnya**

"Apa kelemahan paper ini?" → hasilnya sering dangkal. Coba ini:

```
Bayangkan paper ini sudah disubmit ke ICICoS dan ditolak. Tulis penolakan fiktif dari editor — 150 kata, tiga alasan utama — berdasarkan ekstraksi berikut: [paste]
```

Hasilnya lebih tajam dan lebih mudah dijadikan komentar reviewer yang spesifik.

---

**T3 · Bangun Argumen Terkuat Dulu**

Kalau kamu langsung minta kelemahan, AI akan cari yang paling mudah. Paksa ia bela paper dulu:

```
Langkah 1 — Kamu adalah co-author. Tulis argumen terkuat untuk mempertahankan tiap klaim kontribusi di hadapan reviewer. 150 kata.
Langkah 2 — Sekarang temukan lubang terbesar dalam argumen yang baru kamu buat sendiri.
```

Kelemahan yang muncul dari sini lebih susah dibantah penulis.

---

**T4 · Persona yang Lebih Spesifik**

"Reviewer IEEE" terlalu umum. Tambahkan domain dan kebiasaan:

```
Kamu reviewer yang sudah 10 tahun review paper [bidang] di [venue]. Kamu sangat ketat soal [aspek, misal: reproducibility]. Dengan karakter itu, tulis komentar untuk Experimental Setup paper ini: [paste ekstraksi]
```

---

**T5 · Larang Frasa Tertentu**

Melarang lebih efektif daripada meminta gaya tertentu:

```
Tulis weakness comment untuk: [kelemahan]
JANGAN gunakan: "The authors should consider...", "It would be beneficial...", "This is an interesting paper, however..."
Langsung ke masalah: "Section X does not...", "Table Y fails to..."
```

---

**T6 · Minta AI Kritik Sendiri**

Setelah dapat draft:

```
Dari review yang baru kamu tulis, mana 2 komentar yang paling mudah dibantah penulis? Kenapa? Tulis versi yang lebih kuat untuk keduanya.
```

---

**T7 · Format Paksa Reasoning**

```
Untuk tiap kelemahan, tulis:
(a) Yang saya harapkan ada berdasarkan klaim paper
(b) Yang saya temukan di paper
(c) Gap antara keduanya
(d) Saran perbaikan
```

Bagus untuk menemukan inkonsistensi antara klaim dan bukti yang sering terlewat.

---

**T8 · Tag Tingkat Keyakinan**

```
Setelah tiap komentar, tambahkan:
[TINGGI] — langsung didukung isi paper
[SEDANG] — perlu konfirmasi manual
[RENDAH] — asumsi, harus kamu cek sendiri di PDF

Contoh: "Section 3 does not report the data split. [TINGGI]"
```

Komentar berlabel [RENDAH] wajib kamu verifikasi di PDF sebelum submit.

---

## Ringkasan

| Prompt | Kapan | Waktu |
|--------|-------|-------|
| A1 | Pemetaan kekuatan & kelemahan | ~5 mnt |
| A2 | Klaim paper terasa terlalu kuat | ~5 mnt |
| B0 | Sudah paham paper, mau cepat | ~3 mnt |
| B1 | Mayoritas kasus | ~8 mnt |
| B2 | Ragu bobot satu kelemahan | ~5 mnt |
| C  | Isi form setelah draft final | ~5 mnt |
| T1–T8 | Tambahkan ke prompt manapun | situasional |
