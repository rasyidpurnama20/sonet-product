# Kumpulan Prompt Review — ICICoS 2026

Dokumen ini berisi prompt siap pakai untuk berbagai kebutuhan review paper. Semua sudah disesuaikan dengan alur review ICICoS dan bisa langsung di-copy ke ChatGPT.

Urutan yang disarankan: jalankan `review-skill.md` dulu untuk ekstraksi, baru pakai prompt-prompt di sini untuk analisis dan penulisan review.

> Hasil dari setiap prompt adalah **draf**. Kamu yang menentukan kalimat finalnya — gaya menulis dan penilaiannya tetap harus mencerminkan kamu sebagai reviewer, bukan AI.

---

## A — Analisis Paper

### A1 · Kekuatan dan Kelemahan

Gunakan ini setelah ekstraksi selesai. Hasilnya langsung bisa dipetakan ke bagian Strengths dan Weaknesses di form review.

```
Berdasarkan hasil ekstraksi paper ini:
[paste hasil dari review-skill.md]

Identifikasi secara terstruktur:

KEKUATAN — minimal 2, mulai dari yang paling signifikan.
Untuk setiap kekuatan, sebut section, tabel, atau halaman yang jadi buktinya.

KELEMAHAN — minimal 2, mulai dari yang paling kritis.
Untuk setiap kelemahan: jelaskan masalahnya (section/halaman) dan satu saran perbaikan yang konkret.

SATU PERTANYAAN PALING PENTING untuk penulis.

Bahasa Inggris formal. Setiap poin harus spesifik ke paper ini — jangan tulis hal yang bisa berlaku untuk paper manapun.
```

**Yang akan kamu dapat:** daftar kekuatan dan kelemahan yang sudah terstruktur dengan referensi spesifik. Tinggal kamu pilih mana yang benar-benar kamu setujui, tambahkan dari pengetahuan domain kamu, lalu edit kalimatnya.

---

### A2 · Stress-Test Klaim

Berguna kalau klaim kontribusinya terasa terlalu kuat atau kurang didukung data.

```
Klaim utama paper ini:
[paste klaim kontribusi dari hasil ekstraksi]

Periksa tiga hal ini:

1. Bukti yang ada — apa yang penulis tunjukkan untuk mendukung klaim ini? Sebut tabel/figure/section spesifik.

2. Kondisi batas — dalam kondisi apa klaim ini tidak berlaku atau melemah? Apakah eksperimen cukup representatif?

3. Pembanding yang hilang — ada baseline atau perbandingan yang logisnya harus ada tapi tidak dikerjakan?

Jawab berdasarkan isi paper saja. Kalau tidak ada bukti untuk suatu poin, tulis "tidak ditemukan di paper" — jangan mengarang.
```

**Yang akan kamu dapat:** gambaran jelas seberapa kuat klaim paper ini bisa dipertahankan. Ini yang paling membantu saat kamu masih ragu antara Minor Revision dan Major Revision.

---

## B — Draft Review

### B0 · Quick Draft *(2 kalimat prompt)*

Kalau kamu sudah cukup paham paper dan mau draft paling cepat:

```
Paper ini: [paste hasil review-skill.md].
Tulis draft review ICICoS dengan bagian: Summary · Strengths (3 poin bernomor) · Weaknesses and Suggestions (3 poin bernomor, tiap poin ada saran perbaikan) · Questions for Authors (2 poin) · Decision: pilih satu dari Accept / Minor Revision / Major Revision / Reject · Confidence: pilih satu dari Expert / Knowledgeable / Passing Knowledge / Basic.
```

**Yang akan kamu dapat:** draft lengkap yang sudah terpetakan ke semua bagian form review. Cocok dipakai kalau kamu sudah punya gambaran jelas dan tinggal butuh kerangka tulisan.

---

### B1 · Draft Review Lengkap

Untuk sebagian besar paper, ini yang paling berguna.

```
Berdasarkan ekstraksi dan analisis paper ini, tulis draft review formal.

SUMMARY (2–3 kalimat)
Apa yang dilakukan paper, metode utamanya, dan kesan umum.

STRENGTHS (2–3 poin bernomor)
Kekuatan paper dengan referensi ke section/tabel/halaman.

WEAKNESSES AND SUGGESTIONS (2–4 poin bernomor)
Tiap poin: masalahnya apa (section/halaman spesifik) + saran perbaikan yang konkret. Urut dari yang paling kritis.

QUESTIONS FOR AUTHORS (1–3 pertanyaan)
Pertanyaan yang perlu dijawab penulis kalau revisi diterima.

Bahasa Inggris formal. Hindari "The authors should consider..." atau "It would be nice if..." — langsung saja: "Section 3.2 does not explain..." atau "Table 2 shows..."
Ingat, ini draft — reviewer yang menulis ulang kalimat finalnya.
```

**Yang akan kamu dapat:** draft review yang sudah dalam format benar dan bisa langsung diedit. Biasanya cukup edit 30–50% kalimatnya supaya terasa natural dan sesuai gaya kamu.

---

### B2 · Tiga Versi Severity

Pakai ini kalau kamu menemukan satu kelemahan besar tapi belum yakin bobotnya seberapa serius.

```
Kelemahan yang ingin saya nilai:
[paste satu kelemahan spesifik]

Tulis tiga versi komentar untuk kelemahan ini:

Major Revision — masalah serius, butuh perubahan metodologi atau eksperimen tambahan. 3–4 kalimat, jelaskan apa yang harus dilakukan dan kenapa ini kritis.

Minor Revision — minta klarifikasi atau tambahan kecil yang masuk akal dikerjakan dalam beberapa minggu. 2–3 kalimat.

Accept with Comment — cukup minta penjelasan tambahan di teks, tidak perlu eksperimen baru. 1–2 kalimat.

Semua versi harus merujuk ke section/halaman yang sama. Di akhir, rekomendasikan mana yang paling tepat untuk kondisi ini.
```

**Yang akan kamu dapat:** tiga opsi komentar untuk kelemahan yang sama dengan tingkat kekerasan berbeda. Kamu pilih satu, lalu edit kalimatnya.

---

## C — Isi Form Review

Setelah draft review final selesai diedit, gunakan script Python di bawah untuk mengisi `review-template.docx` secara otomatis.

Script ini hanya akan:
- Mengisi semua `[]` dengan data review kamu
- Menebalkan pilihan keputusan yang kamu tentukan (Accept / Minor Revision / dst.)
- Tidak menyentuh bagian lain dari template sama sekali

**Langkah:**
1. Isi bagian `DATA REVIEW` di bawah
2. Simpan sebagai `fill_review.py` di folder yang sama dengan `review-template.docx`
3. Jalankan: `python3 fill_review.py`
4. Buka `review-filled.docx` dan cek hasilnya sebelum submit

```python
"""
fill_review.py
Isi review-template.docx otomatis.
Dependensi: pip install python-docx
"""
from docx import Document

# ─────────────────────────────────────────────────────
# DATA REVIEW — isi di sini
# ─────────────────────────────────────────────────────
data = {
    "paper_id"        : "ICICoS-2026-001",
    "paper_title"     : "Judul paper di sini",
    "reviewer_id"     : "R-01",

    "score_originality" : "4",
    "score_technical"   : "3",
    "score_clarity"     : "4",
    "score_relevance"   : "5",
    "score_references"  : "3",
    "score_overall"     : "4",

    "summary"    : "Tulis summary di sini.",
    "strengths"  : "1. Kekuatan pertama.\n2. Kekuatan kedua.\n3. Kekuatan ketiga.",
    "weaknesses" : "1. Kelemahan pertama. Saran: ...\n2. Kelemahan kedua. Saran: ...",
    "questions"  : "1. Pertanyaan pertama?\n2. Pertanyaan kedua?",
    "confidential": "",

    # Tulis PERSIS salah satu — huruf besar/kecil harus sama:
    # "Accept" | "Minor Revision" | "Major Revision" | "Reject"
    "decision"   : "Minor Revision",

    # "Expert" | "Knowledgeable" | "Passing Knowledge" | "Basic"
    "confidence" : "Knowledgeable",
}

TEMPLATE = "review-template.docx"
OUTPUT   = "review-filled.docx"

DECISION_OPTIONS   = ["Accept", "Minor Revision", "Major Revision", "Reject"]
CONFIDENCE_OPTIONS = ["Expert", "Knowledgeable", "Passing Knowledge", "Basic"]

# ─────────────────────────────────────────────────────
# Pemetaan label → field
# ─────────────────────────────────────────────────────
INLINE = {
    "Paper ID"     : "paper_id",
    "Paper Title"  : "paper_title",
    "Reviewer ID"  : "reviewer_id",
    "Originality"  : "score_originality",
    "Technical"    : "score_technical",
    "Clarity"      : "score_clarity",
    "Relevance"    : "score_relevance",
    "References"   : "score_references",
    "Overall"      : "score_overall",
}
BLOCK = {
    "Summary"      : "summary",
    "Strengths"    : "strengths",
    "Weaknesses"   : "weaknesses",
    "Questions"    : "questions",
    "Confidential" : "confidential",
}
DECISION = {
    "Recommendation" : "decision",
    "Confidence"     : "confidence",
}

# ─────────────────────────────────────────────────────
# Fungsi utama
# ─────────────────────────────────────────────────────
def fill_bracket(para, value):
    """Ganti [] di paragraf dengan value. Hanya sentuh run yang berisi []."""
    for run in para.runs:
        if "[]" in run.text:
            run.text = run.text.replace("[]", value)
            return True
    # Fallback: kalau [] terpecah antar runs
    full = "".join(r.text for r in para.runs)
    if "[]" in full:
        para.runs[0].text = full.replace("[]", value)
        for r in para.runs[1:]:
            r.text = ""
        return True
    return False

def bold_decision(para, selected, options):
    """Bold pilihan yang dipilih, unbold sisanya. Tidak sentuh run lain."""
    for run in para.runs:
        if run.text.strip() in options:
            run.bold = (run.text.strip() == selected)

def process():
    doc = Document(TEMPLATE)
    pending_block    = None
    pending_decision = None

    for para in doc.paragraphs:
        text = para.text.strip()

        # Isi block field ([] ada di paragraf setelah label)
        if pending_block is not None:
            if "[]" in para.text:
                fill_bracket(para, data.get(pending_block, ""))
            pending_block = None
            continue

        # Bold decision options (ada di paragraf setelah label)
        if pending_decision is not None:
            opts    = DECISION_OPTIONS if pending_decision == "decision" else CONFIDENCE_OPTIONS
            bold_decision(para, data.get(pending_decision, ""), opts)
            pending_decision = None
            continue

        # Inline field: label dan [] ada di baris yang sama
        for kw, field in INLINE.items():
            if kw in text and "[]" in text:
                fill_bracket(para, data.get(field, ""))
                break

        # Set pending untuk baris berikutnya
        for kw, field in BLOCK.items():
            if kw in text:
                pending_block = field
                break
        for kw, field in DECISION.items():
            if kw in text:
                pending_decision = field
                break

    doc.save(OUTPUT)
    print(f"Tersimpan: {OUTPUT}")
    _verify(OUTPUT)

def _verify(path):
    doc = Document(path)
    sisa = [p.text[:60] for p in doc.paragraphs if "[]" in p.text]
    dec  = [r.text for p in doc.paragraphs for r in p.runs
            if r.text.strip() == data["decision"] and r.bold]
    conf = [r.text for p in doc.paragraphs for r in p.runs
            if r.text.strip() == data["confidence"] and r.bold]
    print("✓ Tidak ada [] tertinggal" if not sisa else f"⚠ Sisa []: {sisa}")
    print(f"✓ Decision  '{data['decision']}' ditebalkan"  if dec  else f"✗ Decision tidak ditemukan")
    print(f"✓ Confidence '{data['confidence']}' ditebalkan" if conf else f"✗ Confidence tidak ditemukan")

if __name__ == "__main__":
    process()
```

---

## D — Tips & Tricks ChatGPT

Teknik-teknik ini jarang dipakai tapi cukup mengubah kualitas output. Semua bisa dikombinasikan dengan prompt manapun di atas.

---

**T1 · Biarkan AI Tanya Dulu**

Daripada langsung minta review, minta AI bertanya dulu. Hasilnya biasanya jauh lebih relevan karena AI tahu konteks yang kamu punya.

```
Saya akan minta bantuan untuk review paper ICICoS. Sebelum mulai, tanyakan dulu 3–4 hal yang paling penting supaya kamu bisa bantu saya lebih tepat. Jangan hasilkan review dulu.
```

Jawab pertanyaannya, baru minta output. Kadang satu pertanyaan AI bisa mengungkap hal yang kamu sendiri belum sadari perlu diklarifikasi.

---

**T2 · Pre-mortem**

"Apa kelemahan paper ini?" sering menghasilkan daftar yang dangkal. Coba balik framingnya:

```
Bayangkan paper ini sudah disubmit ke ICICoS dan ditolak. Tulis keputusan penolakan fiktif dari editor — 150 kata, tiga alasan utama, berdasarkan hasil ekstraksi berikut: [paste ekstraksi]
```

Hasilnya biasanya lebih substantif dan lebih mudah dijadikan komentar reviewer yang konkret.

---

**T3 · Steelman Dulu**

Kalau langsung minta kelemahan, AI cenderung mencari yang mudah. Paksa ia membangun argumen terkuat untuk paper dulu:

```
Langkah 1 — Kamu adalah co-author paper ini. Tulis argumen terkuat untuk mempertahankan setiap klaim kontribusi di hadapan reviewer skeptis. 150 kata.

Langkah 2 — Sekarang temukan lubang terbesar dalam argumen yang baru kamu buat sendiri. Apa yang tidak bisa dipertahankan tanpa data tambahan?
```

Kelemahan yang muncul dari cara ini biasanya lebih akurat dan lebih sulit dibantah penulis.

---

**T4 · Persona Spesifik**

"Berperan sebagai reviewer IEEE" terlalu umum. Tambahkan domain dan kebiasaan spesifik:

```
Kamu adalah reviewer yang sudah 10 tahun me-review paper [bidang spesifik] di [venue spesifik]. Kamu sangat teliti soal [aspek spesifik, contoh: reproducibility / baseline selection / dataset bias]. Dengan karakter itu, baca ekstraksi ini dan tulis komentar untuk bagian Experimental Setup: [paste ekstraksi]
```

Ganti bagian dalam kurung sesuai paper yang sedang kamu review.

---

**T5 · Larang Kalimat Tertentu**

Melarang frasa spesifik lebih efektif daripada meminta gaya tertentu:

```
Tulis weakness comment untuk: [kelemahan]

JANGAN gunakan kalimat: "The authors should consider...", "It would be beneficial...", "The paper could be improved..."
Langsung ke masalah: "Section X does not...", "Table Y fails to show..."
```

Tanpa larangan ini, AI hampir selalu pakai frasa hedging yang tidak cocok untuk peer review formal.

---

**T6 · Minta AI Kritik Dirinya Sendiri**

Setelah dapat draft review, minta AI cari yang paling lemah:

```
Dari review yang baru kamu tulis, mana 2 komentar yang paling mudah dibantah penulis? Kenapa? Tulis versi yang lebih kuat untuk masing-masing, dengan referensi section/halaman yang lebih spesifik.
```

Biasanya mengungkap komentar yang terlalu generik atau tidak cukup didukung referensi.

---

**T7 · Format Paksa Reasoning**

Format output yang tepat bisa memaksa AI berpikir lebih dalam:

```
Untuk setiap kelemahan, tulis dalam format ini:
(a) Yang saya harapkan ada berdasarkan klaim paper
(b) Yang saya temukan di paper
(c) Gap antara keduanya
(d) Saran perbaikan konkret
```

Format ini bagus untuk menemukan inkonsistensi antara klaim dan bukti yang sering terlewat kalau langsung minta "list weaknesses".

---

**T8 · Tag Keyakinan**

Minta AI tandai seberapa yakin ia dengan tiap komentar:

```
Setelah setiap komentar, tambahkan tag:
[TINGGI] — langsung didukung isi paper
[SEDANG] — perlu konfirmasi manual
[RENDAH] — asumsi atau inferensi

Contoh: "Section 3.2 does not report the train/val/test split. [TINGGI]"
```

Semua komentar [RENDAH] harus kamu buka langsung di PDF sebelum dimasukkan ke form review.

---

## Ringkasan

| Prompt | Kapan | Estimasi |
|--------|-------|----------|
| A1 | Pemetaan awal sebelum nulis | 5 mnt |
| A2 | Klaim terasa terlalu kuat | 5 mnt |
| B0 | Sudah paham paper, mau cepat | 3 mnt |
| B1 | Mayoritas kasus | 8 mnt |
| B2 | Ragu bobot satu kelemahan | 5 mnt |
| C  | Isi form setelah draft final | 5 mnt |
| T1–T8 | Kombinasikan dengan prompt apapun | situasional |
