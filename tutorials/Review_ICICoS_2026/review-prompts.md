# Review Prompts — ICICoS 2026
> Gunakan setelah ekstraksi paper selesai via `review-skill.md`
> Versi: 1.0 | Juni 2026

---

## Cara Pakai File Ini

1. **Selesaikan ekstraksi** paper menggunakan `review-skill.md` terlebih dahulu
2. **Pilih prompt** dari Part 1 untuk mendapat pandangan luas dari paper
3. **Pilih prompt** dari Part 2 untuk menghasilkan variasi review yang berbeda
4. **Gunakan Part 3** untuk mengisi `review-template.docx` secara otomatis

> Setiap prompt bisa langsung di-copy ke ChatGPT Plus Project yang sudah disetup.
> Ganti bagian `[paste hasil ekstraksi]` dengan output dari review-skill.md.

---

## PART 1 — Broader View Prompts

*Tujuan: Mendapat pandangan lebih luas dari paper — melampaui apa yang tertulis di permukaan.*

---

### P1-A: Multi-Perspektif Reviewer



```
Berdasarkan hasil ekstraksi paper ini:
[paste hasil ekstraksi]

Analisis paper dari TIGA perspektif reviewer yang berbeda:

PERSPEKTIF 1 — Ahli Metodologi/Teknis
Fokus: apakah metode yang diusulkan valid, reproducible, dan rigorous?
Pertanyaan kunci: Apa kelemahan metodologis yang paling kritis?

PERSPEKTIF 2 — Ahli Domain / Aplikasi
Fokus: apakah masalah yang diselesaikan relevan dan solusinya praktis?
Pertanyaan kunci: Apakah paper ini memberikan kontribusi nyata ke bidangnya?

PERSPEKTIF 3 — Reviewer Literatur
Fokus: apakah paper ini benar-benar baru dibanding yang sudah ada?
Pertanyaan kunci: Adakah paper terkait yang penting namun tidak dikutip?

Untuk setiap perspektif, berikan:
- 2 kekuatan utama
- 2 kelemahan utama
- 1 pertanyaan kritis untuk penulis
Format: gunakan header per perspektif, bullet points, bahasa Inggris formal.
```

---

### P1-B: Analisis Posisi di Lanskap Penelitian

```
Berdasarkan topik dan klaim kontribusi paper ini:
[paste klaim kontribusi dari hasil ekstraksi]

Bantu saya memahami POSISI paper ini di lanskap penelitian:

1. PRIOR WORK LANDSCAPE
   Berdasarkan referensi yang dikutip penulis, gambarkan:
   - Pendekatan dominan sebelum paper ini
   - Tren terbaru (2022–2025) yang relevan
   - Di mana paper ini memposisikan dirinya

2. INCREMENTAL vs. LEAP
   Apakah kontribusi ini:
   [ ] Incremental improvement dari metode yang ada
   [ ] Kombinasi baru dari teknik yang sudah ada
   [ ] Pendekatan genuinely baru
   Berikan justifikasi berdasarkan isi paper, bukan spekulasi.

3. IMPACT PROJECTION
   Jika paper ini diterima dan dikutip, siapa yang paling mungkin
   menggunakannya? (peneliti akademis / praktisi industri / keduanya?)
   Apa yang memungkinkan atau menghambat adopsi?

Tampilkan reasoning step-by-step sebelum tiap kesimpulan.
```

---

### P1-C: Devil's Advocate — Stress Test Klaim

```
Berdasarkan hasil ekstraksi paper ini:
[paste hasil ekstraksi — terutama Fase 2 dan Fase 4]

Lakukan STRESS TEST terhadap klaim utama paper.
Untuk setiap klaim berikut, cari argumen TERKUAT yang melemahkannya:

KLAIM 1: [paste klaim kontribusi 1]
- Argumen yang paling melemahkan klaim ini:
- Kondisi di mana klaim ini TIDAK berlaku:
- Bukti di paper yang mendukung / melemahkan:

KLAIM 2: [paste klaim kontribusi 2, jika ada]
- (sama seperti di atas)

KLAIM PERFORMA: [paste hasil terbaik yang diklaim]
- Apakah kondisi pengujian cukup general, atau terlalu ideal?
- Apakah hasil akan bertahan pada dataset / kondisi yang berbeda?
- Apakah ada confounding variable yang mungkin meningkatkan hasil?

Format output: tabel tiga kolom — Klaim | Kelemahan Terkuat | Tingkat Keparahan (Low/Medium/High)
Tambahkan ringkasan: "Klaim yang paling rentan adalah..."
```

---

### P1-D: Cross-Domain Relevance Check

```
Paper ini bertemakan: [paste sub-topik dari Fase 1 ekstraksi]

Lakukan cross-domain relevance check:

1. TRANSFER POTENTIAL
   Apakah metode/sistem ini bisa diterapkan di domain LAIN yang tidak
   dibahas penulis? Sebutkan 2–3 domain potensial beserta alasannya.

2. KNOWN SOLUTIONS IN ADJACENT FIELDS
   Apakah ada solusi yang SUDAH ADA di bidang lain yang menyelesaikan
   masalah serupa? Jika iya, apakah penulis mengakuinya?

3. STANDARDIZATION GAP
   Apakah ada standar industri atau benchmark yang seharusnya
   digunakan tetapi tidak disebutkan paper ini?

4. ETHICAL / SOCIETAL DIMENSION
   Apakah ada implikasi etis atau sosial dari penelitian ini yang
   tidak dibahas? (privasi data, bias model, dampak tenaga kerja, dll.)

Jawab hanya berdasarkan isi paper dan pengetahuan umum bidang.
Tandai jelas jika ada spekulasi dengan "Spekulasi reviewer:".
```

---

### P1-E: Future Work Gap Mapper

```
Berdasarkan hasil ekstraksi lengkap paper ini:
[paste hasil ekstraksi Fase 4 dan Fase 7]

Peta RESEARCH GAPS yang ditinggalkan paper ini:

TIER 1 — Gap Kritis (harus dijawab untuk validitas paper ini)
- Gap apa yang membuat klaim paper ini belum sepenuhnya terbukti?

TIER 2 — Gap Ekstensi (natural next steps dari paper ini)
- Apa eksperimen atau analisis yang logis dilakukan setelah ini?

TIER 3 — Gap Jangka Panjang (implikasi untuk bidang secara keseluruhan)
- Pertanyaan besar apa yang masih terbuka setelah paper ini?

Untuk setiap gap, berikan:
- Deskripsi gap (1 kalimat)
- Mengapa ini penting
- Apakah penulis mengakui gap ini? [ ] Ya  [ ] Tidak  [ ] Parsial

Format: tabel per tier. Bahasa Inggris. Berikan ringkasan di akhir.
```

---

## PART 2 — Review Variation Prompts

*Tujuan: Menghasilkan variasi review dari perspektif dan keputusan yang berbeda — reviewer memilih yang paling mencerminkan penilaiannya.*

---

### P2-A: Tiga Versi Severity Review

```
Berdasarkan analisis paper ini, tulis TIGA VERSI komentar reviewer
untuk kelemahan utama yang ditemukan:

KELEMAHAN: [paste kelemahan utama dari analisis]

VERSI 1 — Major Revision Required
Tone: komentar serius, minta perubahan signifikan pada metodologi/eksperimen
Panjang: 4–5 kalimat. Bahasa Inggris formal.
Sertakan: apa yang harus dilakukan, mengapa ini critical.

VERSI 2 — Minor Revision Required
Tone: komentar konstruktif, minta klarifikasi atau penambahan kecil
Panjang: 3–4 kalimat. Bahasa Inggris formal.
Sertakan: saran spesifik yang bisa dikerjakan dalam 2–3 minggu.

VERSI 3 — Clarification Request (Accept with Comment)
Tone: ringan, hanya meminta penjelasan tambahan di paper
Panjang: 2–3 kalimat. Bahasa Inggris formal.
Sertakan: pertanyaan spesifik yang jawabannya sudah ada di paper
          tapi perlu diperjelas.

Tulis ketiga versi, lalu berikan rekomendasi: versi mana yang
paling akurat menggambarkan kondisi kelemahan ini?
```

---

### P2-B: Reviewer Persona — Strict vs. Supportive

```
Berdasarkan ringkasan dan analisis paper ini:
[paste ringkasan 5-kalimat dari Fase 2 dan hasil utama dari Fase 4]

Tulis review dari DUA persona reviewer:

PERSONA A — The Rigorous Reviewer
Karakteristik: standar tinggi, detail-oriented, skeptis terhadap klaim
tanpa bukti kuat, mengutamakan reproducibility dan experimental rigor.
Format output:
- Summary (2 kalimat)
- 3 Major Weaknesses (masing-masing dengan saran perbaikan spesifik)
- 1 Strength
- Recommendation: Major Revision / Reject

PERSONA B — The Constructive Mentor
Karakteristik: apresiatif terhadap upaya penulis, fokus pada potensi,
komentar berupa bimbingan untuk meningkatkan paper.
Format output:
- Summary (2 kalimat, apresiasi konteks)
- 2 Weaknesses (dikemas sebagai "opportunities for improvement")
- 2 Strengths
- Recommendation: Minor Revision / Accept

Setelah kedua persona, berikan: "Berdasarkan kedua perspektif,
rekomendasi yang paling defensible secara akademis adalah..."
```

---

### P2-C: Structured Strength/Weakness Balance

```
Berdasarkan ekstraksi lengkap paper ini:
[paste hasil ekstraksi]

Tulis penilaian BALANCED yang bisa langsung masuk ke form review:

STRENGTHS (wajib minimal 3, urut dari paling signifikan):
S1. [Kekuatan paling kuat — referensi section/tabel spesifik]
S2. [Kekuatan kedua]
S3. [Kekuatan ketiga]

WEAKNESSES (wajib minimal 3, urut dari paling kritis):
W1. [Kelemahan paling kritis]
    → Saran perbaikan: [konkret dan actionable]
    → Dampak jika tidak diperbaiki: [minor / major / fatal]
W2. [Kelemahan kedua]
    → Saran perbaikan:
    → Dampak:
W3. [Kelemahan ketiga]
    → Saran perbaikan:
    → Dampak:

QUESTIONS FOR AUTHORS (wajib 2–4 pertanyaan):
Q1. [Pertanyaan yang penulis WAJIB jawab jika revisi diterima]
Q2.
Q3. (opsional)

Semua komentar dalam bahasa Inggris formal. Setiap poin harus
menyebut section/halaman/tabel/gambar yang spesifik.
```

---

### P2-D: Decision Boundary Analysis

```
Berdasarkan semua analisis sebelumnya tentang paper ini,
bantu saya memutuskan antara dua pilihan yang sedang saya
pertimbangkan: [pilih salah satu]

OPSI A: Accept vs. Minor Revision
OPSI B: Minor Revision vs. Major Revision
OPSI C: Major Revision vs. Reject

Untuk pilihan yang saya sebutkan, berikan:

1. ARGUMEN untuk opsi pertama (3 poin terkuat)
2. ARGUMEN untuk opsi kedua (3 poin terkuat)
3. DECIDING FACTOR: Satu kriteria paling penting yang membedakan
   keduanya untuk paper ini secara spesifik
4. RECOMMENDATION: Berikan satu rekomendasi final dengan justifikasi
   2–3 kalimat berdasarkan standar IEEE/ACM conference

Format: gunakan tabel dua kolom untuk argumen, lalu narasi untuk
deciding factor dan recommendation.
```

---

### P2-E: Blind Review Consistency Checker

```
Berikut adalah draft review yang sudah saya buat:
[paste draft review kamu]

Dan berikut adalah keputusan saya: [Accept / Minor / Major / Reject]

Lakukan CONSISTENCY AUDIT pada review saya:

1. TONE CONSISTENCY
   Apakah tone review konsisten dari awal sampai akhir?
   Apakah ada bagian yang terlalu lunak / terlalu keras dibanding sisanya?

2. CLAIM-EVIDENCE MATCH
   Untuk setiap komentar negatif saya: apakah disertai referensi spesifik
   ke paper (section/halaman/tabel)? Tandai mana yang belum.

3. DECISION ALIGNMENT
   Apakah rekomendasi [Accept/Minor/Major/Reject] konsisten dengan
   isi review? Apakah ada gap antara severity komentar dan keputusan?

4. BLIND REVIEW CHECK
   Apakah ada kalimat yang bisa mengidentifikasi penulis atau institusi?
   Apakah ada bias yang terdeteksi?

5. COMPLETENESS CHECK
   Bagian mana yang kurang dibahas padahal penting untuk tipe paper ini?

Output: daftar temuan per kategori + saran edit yang konkret.
Jika tidak ada masalah di suatu kategori, tulis "OK — no issues found."
```

---

## PART 3 — Template Filling Prompts

*Tujuan: Mengisi `review-template.docx` secara otomatis menggunakan python-docx — mengganti semua `[...]` dengan konten review dan menebalkan pilihan keputusan di setiap nomor.*

---

### P3-A: Generate Review Data Dictionary

```
Berdasarkan semua analisis yang sudah kita lakukan untuk paper ini,
buat REVIEW DATA DICTIONARY dalam format Python dict yang siap pakai.

Isi setiap key berikut dengan konten review final kita.
Tulis dalam bahasa Inggris formal. Jangan gunakan placeholder kosong.

review_data = {
    # Identitas
    "paper_title": "...",
    "reviewer_id": "...",         # isi dengan ID reviewer kamu

    # Penilaian (pilih angka 1–5)
    "score_originality": "...",   # 1=very poor, 5=excellent
    "score_methodology": "...",
    "score_results": "...",
    "score_presentation": "...",
    "score_references": "...",
    "score_overall": "...",

    # Komentar naratif (isi dengan teks penuh)
    "summary": "...",             # ringkasan isi paper (3–5 kalimat)
    "strengths": "...",           # kekuatan (format: 1. ... \n2. ... \n3. ...)
    "weaknesses": "...",          # kelemahan + saran perbaikan
    "questions_for_authors": "...",
    "comments_to_editor": "...",  # komentar rahasia ke editor (jika ada)

    # Keputusan — TULIS PERSIS SESUAI OPSI DI TEMPLATE
    # Pilihan: "Accept" / "Minor Revision" / "Major Revision" / "Reject"
    "decision": "...",

    # Confidence — TULIS PERSIS SESUAI OPSI DI TEMPLATE
    # Pilihan: "Expert" / "Knowledgeable" / "Passing Knowledge" / "Basic"
    "confidence": "...",
}

Setelah mengisi dict di atas, verifikasi:
- Apakah score_overall konsisten dengan decision?
- Apakah strengths dan weaknesses balance sesuai decision?
- Apakah semua komentar mengacu ke section/halaman spesifik?
```

---

### P3-B: Python Script — Fill review-template.docx

Simpan script berikut sebagai `fill_review.py` di folder yang sama dengan `review-template.docx`.

```python
"""
fill_review.py
Mengisi review-template.docx untuk ICICOS tanpa merusak formatting.
- Mengganti semua [...]  dengan konten review
- Menebalkan (bold) pilihan keputusan yang dipilih di setiap nomor

Dependensi: pip install python-docx
Penggunaan: python fill_review.py
"""

from docx import Document
from docx.shared import RGBColor
import re
import copy


# ─────────────────────────────────────────────
#  ISI DATA REVIEW DI SINI
# ─────────────────────────────────────────────
review_data = {
    "paper_title"            : "GANTI DENGAN JUDUL PAPER",
    "reviewer_id"            : "GANTI DENGAN ID REVIEWER",
    "score_originality"      : "4",
    "score_methodology"      : "3",
    "score_results"          : "3",
    "score_presentation"     : "4",
    "score_references"       : "3",
    "score_overall"          : "3",
    "summary"                : "GANTI DENGAN RINGKASAN PAPER.",
    "strengths"              : "1. Kekuatan pertama.\n2. Kekuatan kedua.\n3. Kekuatan ketiga.",
    "weaknesses"             : "1. Kelemahan utama. Saran: ...\n2. Kelemahan kedua. Saran: ...",
    "questions_for_authors"  : "1. Pertanyaan pertama?\n2. Pertanyaan kedua?",
    "comments_to_editor"     : "",
    "decision"               : "Minor Revision",   # Accept | Minor Revision | Major Revision | Reject
    "confidence"             : "Knowledgeable",    # Expert | Knowledgeable | Passing Knowledge | Basic
}

# Opsi keputusan yang ada di template — sesuaikan jika template berbeda
DECISION_OPTIONS    = ["Accept", "Minor Revision", "Major Revision", "Reject"]
CONFIDENCE_OPTIONS  = ["Expert", "Knowledgeable", "Passing Knowledge", "Basic"]

TEMPLATE_PATH = "review-template.docx"
OUTPUT_PATH   = "review-filled.docx"
# ─────────────────────────────────────────────


def get_full_text(paragraph):
    """Gabungkan teks dari semua runs dalam satu paragraf."""
    return "".join(run.text for run in paragraph.runs)


def replace_placeholder_in_paragraph(paragraph, placeholder, replacement):
    """
    Ganti placeholder [...] dalam paragraf sambil menjaga formatting.
    Menangani kasus placeholder yang terpecah antar runs.
    """
    full_text = get_full_text(paragraph)
    if placeholder not in full_text:
        return False

    # Rebuild semua runs menjadi satu run tunggal untuk keamanan
    if len(paragraph.runs) == 0:
        return False

    # Simpan format dari run pertama sebagai referensi
    ref_run = paragraph.runs[0]
    ref_font = ref_run.font

    # Hapus semua teks di semua runs
    new_text = full_text.replace(placeholder, replacement)
    paragraph.runs[0].text = new_text
    for run in paragraph.runs[1:]:
        run.text = ""

    return True


def bold_decision_option(paragraph, selected_option, all_options):
    """
    Dalam paragraf yang berisi opsi keputusan,
    bold opsi yang dipilih dan unbold sisanya.
    Contoh paragraf: "Accept / Minor Revision / Major Revision / Reject"
    """
    full_text = get_full_text(paragraph)

    # Cek apakah paragraf ini adalah paragraf opsi keputusan
    option_found = any(opt in full_text for opt in all_options)
    if not option_found:
        return False

    # Rebuild paragraph: satu run per kata/token untuk kontrol bold
    # Pisahkan teks berdasarkan opsi yang dikenal
    # Strategi: tandai setiap opsi dengan tag bold
    if len(paragraph.runs) == 0:
        return False

    ref_run = paragraph.runs[0]
    new_runs_data = []  # list of (text, is_bold)

    # Cari posisi setiap opsi dalam full_text
    remaining = full_text
    last_end = 0
    positions = []

    for opt in all_options:
        start = full_text.find(opt)
        if start != -1:
            positions.append((start, start + len(opt), opt))

    positions.sort(key=lambda x: x[0])

    cursor = 0
    for start, end, opt in positions:
        if cursor < start:
            new_runs_data.append((full_text[cursor:start], False))
        is_selected = (opt == selected_option)
        new_runs_data.append((opt, is_selected))
        cursor = end
    if cursor < len(full_text):
        new_runs_data.append((full_text[cursor:], False))

    # Hapus semua teks dari runs lama
    for run in paragraph.runs:
        run.text = ""

    # Tulis ulang ke run pertama (split per token dengan bold berbeda)
    # Tambah runs baru jika perlu
    while len(paragraph.runs) < len(new_runs_data):
        new_run = copy.deepcopy(paragraph.runs[0])
        new_run.text = ""
        paragraph.runs[0]._r.addnext(new_run._r)

    for i, (text, bold) in enumerate(new_runs_data):
        if i < len(paragraph.runs):
            paragraph.runs[i].text = text
            paragraph.runs[i].bold = bold

    return True


def process_document(template_path, output_path, data):
    doc = Document(template_path)

    # Kumpulkan semua paragraf dari body + tabel
    def all_paragraphs(doc):
        for para in doc.paragraphs:
            yield para
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        yield para

    for para in all_paragraphs(doc):
        full_text = get_full_text(para)

        # 1. Ganti placeholder [...] dengan konten review
        if "[...]" in full_text:
            # Tentukan key berdasarkan konteks paragraf sebelumnya
            # — pendekatan sederhana: ganti [...] dengan semua field secara berurutan
            # Untuk matching otomatis, gunakan keyword detection:
            text_lower = full_text.lower()
            replacement = ""
            if   "summary"      in text_lower or "abstract" in text_lower:
                replacement = data.get("summary", "")
            elif "strength"     in text_lower:
                replacement = data.get("strengths", "")
            elif "weakness"     in text_lower or "limitation" in text_lower:
                replacement = data.get("weaknesses", "")
            elif "question"     in text_lower:
                replacement = data.get("questions_for_authors", "")
            elif "editor"       in text_lower or "confidential" in text_lower:
                replacement = data.get("comments_to_editor", "")
            elif "originality"  in text_lower or "novelty" in text_lower:
                replacement = data.get("score_originality", "")
            elif "methodology"  in text_lower or "technical" in text_lower:
                replacement = data.get("score_methodology", "")
            elif "result"       in text_lower:
                replacement = data.get("score_results", "")
            elif "presentation" in text_lower or "clarity" in text_lower:
                replacement = data.get("score_presentation", "")
            elif "reference"    in text_lower:
                replacement = data.get("score_references", "")
            elif "overall"      in text_lower:
                replacement = data.get("score_overall", "")
            elif "title"        in text_lower:
                replacement = data.get("paper_title", "")
            elif "reviewer"     in text_lower:
                replacement = data.get("reviewer_id", "")
            else:
                replacement = "[FILL MANUALLY]"

            replace_placeholder_in_paragraph(para, "[...]", replacement)

        # 2. Bold opsi decision yang dipilih
        if any(opt in full_text for opt in DECISION_OPTIONS):
            bold_decision_option(para, data["decision"], DECISION_OPTIONS)

        if any(opt in full_text for opt in CONFIDENCE_OPTIONS):
            bold_decision_option(para, data["confidence"], CONFIDENCE_OPTIONS)

    doc.save(output_path)
    print(f"✅ Review tersimpan di: {output_path}")
    print(f"   Decision: {data['decision']} (ditebalkan di template)")
    print(f"   Confidence: {data['confidence']} (ditebalkan di template)")


if __name__ == "__main__":
    process_document(TEMPLATE_PATH, OUTPUT_PATH, review_data)
```

---

### P3-C: Prompt untuk Generate Isi Script dari Review Final

```
Berdasarkan review final yang sudah kita buat untuk paper ini,
isi Python dict `review_data` berikut dengan konten yang tepat.

Aturan pengisian:
- Semua teks dalam bahasa Inggris formal akademis
- "strengths" dan "weaknesses": format bernomor, pisahkan dengan \n
- "decision": HARUS PERSIS salah satu dari:
  "Accept" | "Minor Revision" | "Major Revision" | "Reject"
- "confidence": HARUS PERSIS salah satu dari:
  "Expert" | "Knowledgeable" | "Passing Knowledge" | "Basic"
- score_*: angka 1–5 sebagai string

Setelah mengisi dict, verifikasi:
[ ] score_overall konsisten dengan decision
[ ] strengths dan weaknesses seimbang sesuai decision
[ ] Semua komentar mengacu ke section/halaman spesifik di paper
[ ] Tidak ada nama penulis / institusi tersebut (blind review)
[ ] "comments_to_editor" hanya berisi info yang tidak boleh dibaca penulis

Output format: blok kode Python yang siap di-paste ke fill_review.py
```

---

### P3-D: Trouble-shooting — Jika Template Punya Format Khusus

```
Saya sudah menjalankan fill_review.py tapi ada masalah berikut:
[deskripsikan masalah: misalnya "placeholder tidak terganti",
"format tabel rusak", "bold tidak muncul", dll.]

Berikut adalah struktur paragraf/tabel yang bermasalah
(paste output dari script diagnostik berikut):

--- SCRIPT DIAGNOSTIK ---
from docx import Document
doc = Document("review-template.docx")
print("=== PARAGRAPHS ===")
for i, para in enumerate(doc.paragraphs):
    print(f"[{i}] style='{para.style.name}' | runs={len(para.runs)} | text='{para.text[:80]}'")
    for j, run in enumerate(para.runs):
        print(f"     run[{j}]: bold={run.bold} | text='{run.text}'")
print("\n=== TABLES ===")
for t, table in enumerate(doc.tables):
    for r, row in enumerate(table.rows):
        for c, cell in enumerate(row.cells):
            for p, para in enumerate(cell.paragraphs):
                if para.text.strip():
                    print(f"  Table[{t}] Row[{r}] Col[{c}] Para[{p}]: '{para.text[:60]}'")
--- END SCRIPT ---

Berdasarkan output di atas, perbaiki fungsi yang bermasalah di fill_review.py.
Jangan ubah logika keseluruhan, hanya perbaiki bagian yang spesifik bermasalah.
```

---

## Quick Reference — Urutan Penggunaan

```
ALUR KERJA REVIEW PAPER ICICOS
================================

1. Upload PDF paper ke ChatGPT Plus Project
         ↓
2. Jalankan review-skill.md (Fase 1–7)
         ↓
3. Koreksi hasil ekstraksi secara manual
         ↓
4. [Opsional] Gunakan P1-A/B/C/D/E untuk pandangan lebih luas
         ↓
5. Pilih P2-A atau P2-C untuk draft konten review formal
         ↓
6. Jalankan P2-E untuk cek konsistensi draft
         ↓
7. Gunakan P3-A untuk generate review_data dict
         ↓
8. Paste dict ke fill_review.py → jalankan script
         ↓
9. Buka review-filled.docx → verifikasi output
         ↓
10. Submit ke EasyChair / ConfTool
```

| Prompt | Tujuan | Waktu Estimasi |
|--------|--------|----------------|
| P1-A | Lihat paper dari 3 perspektif berbeda | 5 mnt |
| P1-B | Posisi paper di lanskap riset | 5 mnt |
| P1-C | Stress test semua klaim | 5 mnt |
| P1-D | Relevansi lintas domain | 3 mnt |
| P1-E | Peta research gap | 3 mnt |
| P2-A | Draft 3 severity komentar | 5 mnt |
| P2-B | Review dari 2 persona reviewer | 5 mnt |
| P2-C | Strengths/Weaknesses siap pakai | 5 mnt |
| P2-D | Bantu pilih antara 2 keputusan | 3 mnt |
| P2-E | Audit konsistensi draft final | 3 mnt |
| P3-A | Generate review_data dict | 5 mnt |
| P3-B | Script fill_review.py (sudah tersedia) | — |
| P3-C | Isi script dari review final | 5 mnt |

---

*Bagian dari: `tutorials/Review_ICICoS_2026/`*
*Gunakan bersama: `review-skill.md` dan `review-template.docx`*
*Juni 2026*
