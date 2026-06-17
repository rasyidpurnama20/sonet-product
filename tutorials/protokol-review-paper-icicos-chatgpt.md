# Protokol Review Paper ICICOS Menggunakan ChatGPT Plus
> **Untuk:** Dosen Reviewer ICICOS
> **Tools:** ChatGPT Plus (GPT-4o) + Fitur Project
> **Target:** Review berkualitas tinggi, konsisten, efisien — 30–45 menit/paper
> **Versi:** 2.0 | Juni 2026 | Berbasis *Prompt Engineering for LLMs* (Berryman & Ziegler, O'Reilly 2025)

---

## Mengapa Tutorial Ini Berbeda?

Sebagian besar tutorial "pakai ChatGPT untuk review paper" hanya menyuruh kamu *copy-paste* paper lalu tanya "Apa kelemahannya?". Hasilnya dangkal dan tidak konsisten.

Tutorial ini dibangun di atas **ilmu rekayasa prompt**: kamu akan tahu **mengapa** setiap prompt ditulis dengan cara tertentu — teknik apa yang dipakai, dan apa efeknya pada kualitas output. Hasilnya: review yang lebih tajam, lebih cepat, dan lebih konsisten di setiap paper.

---

## Daftar Isi
1. [Fondasi: Cara Berpikir yang Benar tentang ChatGPT](#1-fondasi-cara-berpikir-yang-benar-tentang-chatgpt)
2. [Persiapan: Setup Project di ChatGPT Plus](#2-persiapan-setup-project-di-chatgpt-plus)
3. [Langkah 1 — Plan-and-Solve: Buat Rencana Review Dulu](#3-langkah-1--plan-and-solve-buat-rencana-review-dulu)
4. [Langkah 2 — Pemetaan Cepat Paper (Zero-Shot + CoT)](#4-langkah-2--pemetaan-cepat-paper-zero-shot--cot)
5. [Langkah 3 — Analisis Novelty (ReAct Framework)](#5-langkah-3--analisis-novelty-react-framework)
6. [Langkah 4 — Evaluasi Metodologi (Chain of Thought)](#6-langkah-4--evaluasi-metodologi-chain-of-thought)
7. [Langkah 5 — Evaluasi Hasil & Referensi (Few-Shot)](#7-langkah-5--evaluasi-hasil--referensi-few-shot)
8. [Langkah 6 — Tulis Review Formal (Structured Output)](#8-langkah-6--tulis-review-formal-structured-output)
9. [Langkah 7 — Keputusan Akhir & Checklist](#9-langkah-7--keputusan-akhir--checklist)
10. [Referensi Cepat: Teknik & Kapan Digunakan](#10-referensi-cepat-teknik--kapan-digunakan)
11. [Pengaturan Temperature per Tugas](#11-pengaturan-temperature-per-tugas)
12. [Tips & Etika Reviewer](#12-tips--etika-reviewer)

---


## 1. Fondasi: Cara Berpikir yang Benar tentang ChatGPT

Sebelum buka ChatGPT, pahami dulu satu prinsip inti dari riset prompt engineering modern:

> **ChatGPT bukan menjawab pertanyaanmu. Ia *menyelesaikan dokumen*.**
> *(Berryman & Ziegler, Prompt Engineering for LLMs, O'Reilly 2025)*

Artinya: kualitas output-nya tergantung seberapa "dokumen akademis yang bagus" prompt yang kamu buat. Jika promptmu terasa seperti awal dari sebuah review jurnal IEEE yang baik, maka output-nya akan menyerupai review IEEE yang baik. Ini disebut **Prinsip Little Red Riding Hood** — jangan keluar dari "jalur" dokumen yang model tahu cara menyelesaikannya.

**Implikasi praktis untuk review paper ICICOS:**
- Tulis prompt dengan gaya dan format **academic peer review** (bukan chat santai)
- Gunakan markdown headers, daftar bernomor, dan label formal
- Framing prompt sebagai "dokumen yang sedang dikerjakan reviewer ahli", bukan "tanya-jawab dengan chatbot"

---

## 2. Persiapan: Setup Project di ChatGPT Plus

### Mengapa Pakai Fitur Project?

Fitur **Project** di ChatGPT Plus = **system message persisten** yang aktif di semua sesi. Ini setara dengan *custom instructions* permanen yang membentuk "persona reviewer ICICOS" tanpa perlu diulang setiap sesi.

Manfaat konkret:
- ChatGPT otomatis tahu konteks ICICOS, standar review, dan blind review protocol
- Semua sesi review ada dalam satu "workspace" yang terorganisir
- File template (form review, author guidelines) bisa diupload sekali, dipakai seterusnya

---

### Cara Setup Project

**Langkah A — Buat Project**
1. Buka [chatgpt.com](https://chatgpt.com) → login akun Plus
2. Sidebar kiri → klik **"+"** di sebelah **Projects**
3. Nama project: `ICICOS 2026 — Reviewer [Nama Kamu]`
4. Klik **Create**

**Langkah B — Pasang Custom Instructions (System Message)**

Di dalam project → klik ⚙️ → **Edit** → paste teks berikut di kolom instruksi:

```
Kamu adalah asisten review ilmiah senior untuk konferensi ICICOS
(International Conference on Information and Communication Technology).

KONTEKS:
- Topik ICICOS: Informatika, Sistem Informasi, Jaringan, AI/ML, IoT,
  Keamanan Siber, Software Engineering
- Standar review: IEEE/ACM conference paper
- Bahasa review akhir: Inggris formal akademis
- Bahasa komunikasi kita: Indonesia

ATURAN WAJIB:
1. Selalu jaga blind review — jangan pernah menebak atau menyebut identitas penulis
2. Selalu tunjukkan reasoning-mu sebelum memberi kesimpulan (berpikir keras sebelum menjawab)
3. Selalu spesifik: sebutkan nomor halaman, section, tabel, atau gambar yang kamu komentari
4. Tone: konstruktif dan profesional — bukan menyerang, tapi juga tidak memuji berlebihan
5. Jika ada klaim yang perlu diverifikasi, katakan "perlu diverifikasi" secara eksplisit

PERSONA:
Kamu adalah reviewer berpengalaman yang telah me-review 200+ paper konferensi
dan memahami standar kualitas IEEE/ACM secara mendalam.
```

**Langkah C — Upload File Referensi (Opsional)**

Di tab **Files** dalam project, upload:
- `ICICOS_Review_Form.pdf` — form review resmi panitia
- `ICICOS_Call_for_Papers.pdf` — scope dan topik resmi
- `IEEE_Conference_Author_Guidelines.pdf`

---


## 3. Langkah 1 — Plan-and-Solve: Buat Rencana Review Dulu

**Teknik: Plan-and-Solve Prompting**

Sebelum langsung menganalisis, minta ChatGPT untuk *membuat rencana dulu*. Teknik ini (dari riset *"Plan-and-Solve Prompting"*, 2023) terbukti menghasilkan analisis yang lebih sistematis dan lengkap karena model memecah masalah sebelum mengeksekusi — bukan langsung "menembak" jawaban.

**Cara upload paper:**
1. Di dalam project → klik **New Chat**
2. Klik ikon **📎** → upload PDF paper
3. Tunggu sampai upload selesai

**Prompt Plan-and-Solve:**

```
Saya adalah reviewer untuk konferensi ICICOS. Saya baru saja menerima
paper ini untuk di-review.

Sebelum memulai analisis, tolong bantu saya menyusun rencana review
yang sistematis:

1. Identifikasi TOPIK UTAMA paper ini dan sub-bidang ICICOS yang relevan
2. Susun CHECKLIST spesifik yang perlu dievaluasi untuk paper jenis ini
   (sesuaikan checklist dengan topik — paper ML punya kriteria berbeda
   dari paper sistem informasi)
3. Tentukan URUTAN analisis yang paling efisien
4. Tandai POTENSI AREA MASALAH yang perlu perhatian ekstra berdasarkan
   pembacaan awal

Format output: gunakan numbered list untuk setiap poin di atas.
Berpikirlah dulu sebelum menjawab — tunjukkan proses identifikasimu.
```

> **Mengapa ini efisien?** Checklist yang disesuaikan dengan topik jauh lebih tajam dari checklist generik. Paper tentang deep learning punya standar yang berbeda dengan paper tentang sistem informasi manajemen.

---

## 4. Langkah 2 — Pemetaan Cepat Paper (Zero-Shot + CoT)

**Teknik: Zero-Shot Chain-of-Thought (CoT)**

Tambahkan frasa "berpikir langkah demi langkah" atau "tunjukkan reasoning-mu" untuk memaksa model melakukan penalaran eksplisit sebelum memberikan kesimpulan. Riset menunjukkan akurasi analisis naik signifikan dengan teknik ini dibanding langsung bertanya jawaban.

**Prompt Pemetaan Cepat:**

```
Baca paper ini secara menyeluruh. Berpikir langkah demi langkah,
buat ringkasan terstruktur berikut:

## METADATA
- Judul:
- Sub-bidang ICICOS:
- Tipe penelitian: [ ] Eksperimental  [ ] Survei/Review  [ ] Sistem/Implementasi
  [ ] Teoritis  [ ] Studi Kasus

## STRUCTURE CHECK
Centang yang ada, beri ✗ yang tidak ada, beri ⚠ yang ada tapi bermasalah:
Abstract | Introduction | Related Work | Methodology | Results |
Discussion | Conclusion | References

## RINGKASAN 5-KALIMAT
(1) Masalah yang diselesaikan:
(2) Tujuan penelitian:
(3) Metode utama:
(4) Hasil utama:
(5) Kesimpulan penulis:

## KLAIM KONTRIBUSI PENULIS
Apa yang diklaim penulis sebagai kontribusi baru? Kutip langsung dari paper.

## RED FLAGS AWAL
List potensi masalah serius yang langsung terlihat di pembacaan pertama.
Jika tidak ada, tulis "Tidak ada red flag obvious."
```

> **Tip Temperature:** Untuk pemetaan faktual seperti ini, gunakan temperature rendah (ChatGPT default sudah bagus). Kamu ingin output yang **konsisten dan akurat**, bukan kreatif.

---


## 5. Langkah 3 — Analisis Novelty (ReAct Framework)

**Teknik: ReAct (Reasoning + Acting)**

Framework ReAct dari riset Google DeepMind (2022) meminta model untuk bergantian antara **Thought** (berpikir) → **Action** (mencari/menganalisis) → **Observation** (menyimpulkan). Hasilnya jauh lebih dalam dibanding analisis satu-lapis.

**Prompt ReAct untuk Novelty:**

```
Analisis NOVELTY paper ini menggunakan pendekatan berikut.
Untuk setiap poin, tunjukkan Thought → Analisis → Kesimpulan:

THOUGHT 1: Apa yang diklaim penulis sebagai hal baru?
ANALISIS 1: [baca klaim di abstract/introduction/conclusion]
KESIMPULAN 1: [klaim spesifiknya adalah...]

THOUGHT 2: Apakah klaim ini didukung oleh isi paper?
ANALISIS 2: [bandingkan klaim vs metodologi vs hasil yang disajikan]
KESIMPULAN 2: [klaim terbukti/tidak terbukti/sebagian terbukti, karena...]

THOUGHT 3: Seberapa baru kontribusi ini dibandingkan literatur terkini?
ANALISIS 3: [cek referensi — apakah ada paper 2022-2025 yang melakukan hal serupa?
            Jika iya, apa bedanya dengan paper ini?]
KESIMPULAN 3: [genuine novelty / incremental improvement / kurang novel, karena...]

THOUGHT 4: Apakah topik ini relevan dengan scope ICICOS?
ANALISIS 4: [cocokkan dengan domain ICICOS]
KESIMPULAN 4: [sangat relevan / relevan / di luar scope]

SKOR NOVELTY: [1-5] — berikan justifikasi 2-3 kalimat
(1=tidak ada novelty baru, 3=kontribusi incremental yang solid,
 5=kontribusi signifikan yang membuka arah penelitian baru)
```

> **Mengapa ReAct lebih baik?** Model yang langsung ditanya "Apakah paper ini novel?" cenderung memberi jawaban dangkal. Dengan memaksanya menunjukkan chain of thought melalui Thought-Analisis-Kesimpulan, model *tidak bisa skip* langkah penalaran.

---

## 6. Langkah 4 — Evaluasi Metodologi (Chain of Thought)

**Teknik: Chain of Thought dengan Few-Shot Example**

Untuk evaluasi metodologi, kita gabungkan CoT dengan **few-shot example** — memberikan contoh seperti apa analisis yang baik vs buruk. Ini "mengajari" ChatGPT standar evaluasi yang kamu inginkan.

**Prompt Few-Shot + CoT untuk Metodologi:**

```
Evaluasi METODOLOGI paper ini. Untuk setiap aspek, tunjukkan
reasoning step-by-step sebelum memberi penilaian.

Berikut contoh bagaimana analisis yang baik vs buruk:

CONTOH ANALISIS BURUK:
"Metodologinya kurang jelas." ← terlalu vague, tidak actionable

CONTOH ANALISIS BAIK:
"Section 3.2 mendefinisikan arsitektur model tetapi tidak menjelaskan
bagaimana hyperparameter dipilih (halaman 4). Apakah learning rate 0.001
dipilih berdasarkan grid search, random search, atau heuristik? Tanpa
informasi ini, hasil tidak bisa direproduksi." ← spesifik dan actionable

---

Sekarang evaluasi paper ini:

**A. KEJELASAN & REPRODUSIBILITAS**
Thinking: [apa yang tidak jelas? informasi apa yang hilang?]
Finding: [section X, halaman Y — masalahnya adalah...]
Verdict: Cukup jelas / Kurang jelas / Tidak bisa direproduksi

**B. KETEPATAN METODE**
Thinking: [apakah metode ini sesuai untuk masalah yang diangkat?
           adakah metode lebih tepat yang seharusnya digunakan?]
Finding: [...]
Verdict: [...]

**C. DATASET & EKSPERIMEN** (skip jika paper teoritis)
Thinking: [dataset apa? berapa sampel? apakah representatif?
           apakah ada data leakage atau bias?]
Finding: [...]
Verdict: [...]

**D. BASELINE & PERBANDINGAN**
Thinking: [apakah baseline relevan dan up-to-date (2022-2025)?
           adakah metode SOTA yang terlewat?]
Finding: [...]
Verdict: [...]

**E. VALIDASI & STATISTIK**
Thinking: [hanya satu run atau multiple runs? ada mean ± std?
           ada statistical significance test?]
Finding: [...]
Verdict: [...]

SKOR METODOLOGI: [1-5] dengan justifikasi.
```

---


## 7. Langkah 5 — Evaluasi Hasil & Referensi (Few-Shot)

**Teknik: Few-Shot Prompting dengan Contoh Positif & Negatif**

Few-shot prompting paling efektif untuk **mengkalibrasi standar** — menunjukkan contoh komentar yang terlalu lunak, terlalu keras, dan yang tepat sasaran.

**Prompt Evaluasi Hasil:**

```
Evaluasi bagian HASIL DAN PEMBAHASAN paper ini.

Standar komentar yang kita inginkan (contoh kalibrasi):

TOO SOFT — hindari: "Hasil cukup baik."
TOO HARSH — hindari: "Hasil ini tidak berguna sama sekali."
JUST RIGHT — contoh: "Tabel 3 menunjukkan akurasi 94.2% pada dataset A,
tetapi tidak ada perbandingan dengan metode SOTA terbaru (2023-2024).
Tanpa baseline yang relevan, klaim 'state-of-the-art' di line 234 tidak
dapat diverifikasi."

---

Dengan standar di atas, evaluasi:

**A. KONSISTENSI KLAIM vs DATA**
Apakah angka di teks konsisten dengan tabel/gambar?
Apakah ada klaim yang lebih besar dari yang ditunjukkan data?
[sebutkan nomor tabel/gambar/halaman secara spesifik]

**B. KUALITAS ANALISIS**
Apakah penulis benar-benar menjelaskan *mengapa* metode mereka berhasil/gagal?
Atau hanya melaporkan angka tanpa interpretasi?

**C. KELENGKAPAN**
Adakah hasil negatif yang sepertinya disembunyikan atau tidak dibahas?
Apakah ada eksperimen ablasi yang seharusnya ada?

**D. SIGNIFIKANSI PRAKTIS**
Apakah perbaikan yang diklaim signifikan secara *praktis*, atau hanya 0.1% di atas baseline?
Apakah ada diskusi tentang keterbatasan (limitations)?

SKOR HASIL & PEMBAHASAN: [1-5] dengan justifikasi.
```

**Prompt Evaluasi Referensi:**

```
Evaluasi REFERENSI dan SITASI paper ini. Tunjukkan reasoning-mu.

**A. KEMUTAKHIRAN**
Thinking: Berapa persen referensi dari 2020-2025?
          Apakah ada gap yang mencurigakan (mis. tidak ada sitasi 2023-2024
          padahal bidangnya sangat aktif)?
Finding: [...]

**B. RELEVANSI & KUALITAS SUMBER**
Thinking: Apakah sumber didominasi IEEE/ACM/Springer/Elsevier?
          Adakah sumber non-akademis yang tidak perlu?
Finding: [...]

**C. PENGGUNAAN SITASI**
Thinking: Apakah klaim-klaim penting punya sitasi pendukung?
          Adakah klaim tanpa sitasi yang seharusnya dikutip?
Finding: [sebutkan nomor halaman/line untuk klaim tanpa sitasi]

**D. PAPER PENTING YANG TERLEWAT**
Berdasarkan topiknya, adakah paper seminal atau survei penting
yang seharusnya dikutip tapi tidak ada? (Jawab hanya jika yakin)

SKOR REFERENSI: [1-5] dengan justifikasi.
```

---


## 8. Langkah 6 — Tulis Review Formal (Structured Output)

**Teknik: Structured Output dengan Recognizable Start/End**

Prinsip dari prompt engineering: gunakan format yang punya **awal dan akhir yang jelas** agar output mudah dibaca dan diparsing. Untuk review formal, kita gunakan format yang menyerupai dokumen review IEEE — ini juga mengaktifkan *truth bias* model ke arah yang benar: "dokumen ini terlihat seperti peer review IEEE, maka saya akan menyelesaikannya seperti peer review IEEE".

**Prompt Kompilasi Review Formal:**

```
Berdasarkan semua analisis sebelumnya (novelty, metodologi, hasil, referensi),
tulis REVIEW FORMAL lengkap dalam bahasa Inggris akademis.

Gunakan *exactly* format berikut (jangan ubah header):

---BEGIN REVIEW---

**SUMMARY OF THE PAPER**
[2-3 paragraf: apa yang dilakukan paper ini, kontribusi yang diklaim,
dan kesan umum kamu sebagai reviewer]

**STRENGTHS**
1. [Kekuatan pertama — spesifik, dengan referensi ke section/halaman]
2. [Kekuatan kedua]
3. [Tambahkan jika ada]

**MAJOR WEAKNESSES**
1. [Kelemahan utama — spesifik (section/halaman/tabel), konstruktif,
   sertakan SARAN PERBAIKAN konkret]
2. [Kelemahan kedua dengan saran]
3. [Tambahkan jika perlu]

**MINOR COMMENTS**
1. [Komentar kecil: typo, notasi tidak konsisten, kalimat ambigu —
   sebutkan halaman/line]
2. [Tambahkan jika ada]

**QUESTIONS FOR THE AUTHORS**
1. [Pertanyaan yang *wajib* dijawab penulis jika revisi diterima]
2. [Tambahkan jika ada]

---END REVIEW---

REQUIREMENTS:
- Minimum 400 kata total
- Setiap weakness WAJIB ada saran perbaikan
- Setiap komentar WAJIB menyebut section/halaman/tabel spesifik
- Jangan menyebut atau menebak identitas penulis (blind review)
- Tone: profesional, konstruktif — seperti surat dari kolega senior
```

> **Mengapa format `---BEGIN REVIEW---` dan `---END REVIEW---`?**
> Ini adalah "stop sequence marker" — kamu bisa langsung copy teks antara dua marker tersebut ke sistem EasyChair/ConfTool tanpa perlu editing. Format ini juga memaksa model untuk menghasilkan review yang *complete* sebelum marker penutup.

---

## 9. Langkah 7 — Keputusan Akhir & Checklist

**Prompt Rekomendasi Final:**

```
Berdasarkan semua analisis di atas, berikan REKOMENDASI FINAL.

Pilih SATU:
[ ] ACCEPT — paper siap diterima dengan sedikit atau tanpa revisi
[ ] MINOR REVISION — paper baik, perlu perbaikan kecil (2-4 minggu)
[ ] MAJOR REVISION — paper berpotensi, perlu perbaikan signifikan
[ ] REJECT — paper punya masalah fundamental yang tidak bisa diperbaiki
             dalam satu siklus revisi

Berikan:
1. PILIHAN: [tulis pilihan di atas]
2. JUSTIFIKASI: [2-3 kalimat yang menjelaskan keputusanmu secara jelas]
3. DEAL-BREAKERS (jika Major Revision atau Reject): [hal-hal WAJIB yang
   harus diperbaiki agar paper bisa diterima di siklus berikutnya]
4. OVERALL SCORE: [1-10]
   Panduan: 1-4=Reject, 5-6=Major Revision, 7-8=Minor Revision, 9-10=Accept

Ingat: keputusan ini adalah REKOMENDASI dari kamu sebagai asisten.
Keputusan final tetap di tangan reviewer (saya).
```

---

### Checklist Final Sebelum Submit ke EasyChair/ConfTool

Baca ulang review kamu, lalu centang semua:

- [ ] Review ditulis dalam bahasa Inggris formal
- [ ] Tidak ada nama/institusi penulis yang disebut
- [ ] Setiap kelemahan disertai saran perbaikan konkret
- [ ] Setiap komentar merujuk section/halaman/tabel spesifik
- [ ] Strengths minimal 2 poin (kecuali paper sangat buruk)
- [ ] Major Weaknesses minimal 1 poin (kecuali paper sempurna)
- [ ] Rekomendasi konsisten dengan isi review
- [ ] Panjang review minimal 400 kata
- [ ] Sudah dibaca ulang sekali sebelum submit

---


## 10. Referensi Cepat: Teknik & Kapan Digunakan

| Teknik | Kapan Digunakan | Efek |
|--------|----------------|------|
| **Plan-and-Solve** | Awal sesi — sebelum analisis | Model membuat roadmap → analisis lebih sistematis |
| **Zero-Shot CoT** | Pemetaan awal, analisis faktual | Tambahkan *"berpikir langkah demi langkah"* → analisis lebih dalam |
| **ReAct (Thought→Action→Observation)** | Analisis novelty, literature gap | Paksa model bernalar iteratif → tidak skip langkah kritis |
| **Few-Shot** | Kalibrasi standar (metodologi, hasil) | Contoh good/bad/ok → komentar lebih tepat sasaran |
| **Structured Output** | Penulisan review formal | Format jelas → mudah copy ke EasyChair, tidak perlu editing |
| **Persona + System Message** | Setup Project (sekali saja) | Konsistensi di semua sesi → tidak perlu ulang konteks |

---

### Prompt Library: Situasi Darurat

**Paper sangat panjang / susah dipahami:**
```
Paper ini padat dan teknis. Tolong lakukan hal berikut step-by-step:
Step 1: Identifikasi 3 klaim utama paper
Step 2: Untuk setiap klaim, temukan bukti empiris pendukungnya di paper
Step 3: Tentukan apakah bukti tersebut cukup atau kurang
Tampilkan proses reasoning-mu di setiap step.
```

**Kamu tidak yakin dengan metodologi spesifik:**
```
Paper ini menggunakan [nama metode]. Ini bukan keahlian utama saya.
Tolong bantu saya dengan format Thought-Finding-Verdict:

Thought: Apa tujuan metode ini dan bagaimana cara kerjanya secara umum?
Finding: Apakah penggunaan metode ini di paper sudah tepat dan sesuai standar?
Verdict: Pertanyaan teknis apa yang perlu saya tanyakan ke penulis?
```

**Strengthen review yang sudah ada:**
```
Berikut draft review saya:
[paste draft review kamu]

Evaluasi review saya:
1. Apakah sudah cukup spesifik? (setiap komentar punya referensi section/halaman?)
2. Apakah ada aspek penting dari checklist ICICOS yang terlewat?
3. Apakah tone sudah profesional dan konstruktif?
4. Apakah rekomendasi konsisten dengan isi review?
Berikan saran perbaikan konkret.
```

**Paper di luar bidang kamu:**
```
Sub-topik utama paper ini adalah [topik spesifik], yang bukan area utama saya.
Lakukan analisis berikut:
1. Apa state-of-the-art di bidang ini per 2024-2025?
2. Apakah metode yang diusulkan masuk akal dalam konteks tersebut?
3. Siapa peneliti atau paper kunci yang harus disitasi tapi mungkin terlewat?
4. Pertanyaan teknis apa yang perlu saya ajukan ke penulis?
Ingat: tunjukkan reasoning-mu di setiap poin.
```

**Cek konsistensi internal paper:**
```
Lakukan "internal consistency check" pada paper ini:
Step 1: Catat semua klaim kuantitatif di abstract dan conclusion
Step 2: Temukan data pendukung untuk setiap klaim di results/tables/figures
Step 3: Tandai klaim yang TIDAK memiliki bukti di bagian results (mismatch)
Step 4: Tandai angka di teks yang berbeda dari tabel/gambar (inconsistency)
Format output: tabel dua kolom — Klaim | Status (Supported/Unsupported/Inconsistent)
```

---


## 11. Pengaturan Temperature per Tugas

ChatGPT tidak langsung mengekspos slider temperature, tapi kamu bisa *menginstruksikan* tingkat kreativitas yang diinginkan melalui pilihan kata dalam prompt:

| Tugas Review | Temperature Ideal | Cara Instruksikan di Prompt |
|---|---|---|
| Ringkasan faktual, cek struktur | Rendah (0.0–0.2) | *"Beri jawaban yang akurat dan konsisten"* |
| Analisis novelty & metodologi | Rendah-Medium (0.2–0.4) | *"Analisis secara sistematis dan hati-hati"* |
| Penulisan review formal | Medium (0.5–0.7) | *"Tulis dengan gaya akademis yang natural"* |
| Brainstorming pertanyaan untuk penulis | Medium-Tinggi (0.7) | *"Buat variasi pertanyaan kritis yang beragam"* |
| Generasi multiple alternatif kalimat review | Tinggi (0.8–1.0) | *"Beri 3 versi alternatif kalimat berikut..."* |

**Panduan praktis:** Untuk sebagian besar tugas review, minta ChatGPT untuk **"akurat dan spesifik"**. Jika output terasa terlalu template-ish, tambahkan *"variasikan gaya penulisan"* atau *"beri alternatif formulasi"*.

---

## 12. Tips & Etika Reviewer

### Waktu yang Realistis

| Fase | Estimasi | Keterangan |
|------|----------|-----------|
| Setup Project (sekali saja) | 5 menit | Lakukan sekali, pakai semua sesi ICICOS |
| Upload + Plan-and-Solve | 5 menit | Tentukan fokus sebelum menyelami detail |
| Pemetaan awal paper | 5 menit | Pahami paper secara struktur dulu |
| Analisis novelty + metodologi | 15 menit | Bagian terpenting — jangan dipotong |
| Analisis hasil + referensi | 5 menit | Fokus pada konsistensi klaim vs data |
| Penulisan review formal | 10 menit | Edit output ChatGPT — jangan paste mentah |
| Final decision + checklist | 5 menit | Baca ulang sekali sebelum submit |
| **Total** | **~45 menit** | Termasuk pembacaan kamu sendiri |

---

### Prinsip Anti-Hallucination dalam Review

ChatGPT bisa "mengarang" detail yang tampak meyakinkan. Untuk review paper, ini berbahaya. Strategi mitigasi:

1. **Minta referensi ke paper itu sendiri** — "sebutkan halaman dan section yang mendukung penilaianmu"
2. **Cek secara manual klaim kritis** — jika ChatGPT bilang "paper tidak menyebut hyperparameter", buka paper dan verifikasi
3. **Gunakan framing verifikasi** — tambahkan *"jika kamu tidak yakin, katakan 'perlu diverifikasi'"* di prompt
4. **Jangan percaya klaim tentang paper lain** — jika ChatGPT menyebut "paper X dari 2023 sudah melakukan ini", verifikasi sendiri via Google Scholar

---

### Hal yang HARUS Dilakukan

✅ **Baca paper aslinya** — ChatGPT adalah alat bantu analisis, bukan pengganti baca
✅ **Edit semua output** — tambahkan perspektif dan keahlian domain kamu
✅ **Verifikasi klaim kritis** secara manual di paper
✅ **Rahasiakan paper** — jangan upload ke tools AI lain, akun ChatGPT bersama, atau share screenshot
✅ **Laporkan konflik kepentingan** — jika mengenal penulis, tolak dan hubungi editor

### Hal yang TIDAK Boleh Dilakukan

❌ **Submit review 100% dari ChatGPT** — ini pelanggaran etika reviewer
❌ **Gunakan akun ChatGPT bersama/publik** untuk upload paper orang lain
❌ **Biarkan ChatGPT menebak identitas penulis** — blind review adalah prinsip fundamental
❌ **Skip pembacaan kamu sendiri** — ChatGPT bisa miss nuance yang ahli manusia tangkap
❌ **Percaya output tanpa verifikasi** untuk klaim kuantitatif kritis

---

### Catatan Etika Akademis

> ChatGPT Plus adalah alat bantu untuk **mempercepat analisis** dan **membantu strukturisasi pemikiran** — bukan pengganti penilaian akademis kamu. Rekayasa prompt yang baik membuatnya bekerja lebih efektif, tapi kualitas akhir tetap ditentukan oleh pengetahuan domain, integritas, dan judgment kamu sebagai reviewer.
>
> Pikirkan seperti ini: ChatGPT adalah *research assistant* yang sangat cepat membaca dan merangkum, tapi kamu adalah *principal investigator* yang memutuskan apa yang penting dan apa rekomendasi akhirnya.

---

## Referensi

- Berryman, J. & Ziegler, A. (2025). *Prompt Engineering for LLMs: The Art and Science of Building Large Language Model-Based Applications*. O'Reilly Media.
- Wei, J. et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022*.
- Yao, S. et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR 2023*.
- Wang, L. et al. (2023). Plan-and-Solve Prompting. *ACL 2023*.
- [IEEE Author Center — Peer Review Guidelines](https://ieeeauthorcenter.ieee.org/)
- [ICICOS Official Website](https://icicos.id)

---

*Dokumen ini dibuat untuk keperluan internal tim reviewer ICICOS. Versi 2.0, Juni 2026.*
*Berbasis kerangka kerja rekayasa prompt dari buku ajar "Rekayasa Prompt untuk LLM" (adaptasi Berryman & Ziegler, O'Reilly 2025).*
