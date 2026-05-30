# 002 — Panduan Prompt yang Baik untuk Membuat "Article Review"

> Fokus dokumen ini: **bagaimana merancang prompt yang baik** agar Claude Opus (atau LLM lain) menghasilkan *article review* berkualitas tinggi — bukan ringkasan dangkal atau, lebih buruk, sitasi yang dikarang.

**Istilah "article review" di sini mencakup dua hal — keduanya dibahas:**
- **A. Critical review satu artikel** — meringkas + mengevaluasi kekuatan/kelemahan satu paper (gaya peer review / tugas critical appraisal).
- **B. Review article / literature review** — sintesis banyak paper menjadi satu tulisan bertema.

---

## Bagian 0 — Prinsip Dasar Prompt yang Baik

Prompt yang baik untuk review **selalu** memuat 6 elemen ini. Ingat singkatannya: **PCTFCG**.

| Elemen | Pertanyaan kunci | Contoh |
|--------|------------------|--------|
| **P — Persona/Role** | Siapa yang "berbicara"? | "Kamu reviewer jurnal Q1 di bidang machine learning." |
| **C — Context** | Bahan & latar apa yang tersedia? | "Berikut teks lengkap paper (terlampir di bawah)." |
| **T — Task** | Apa yang harus dilakukan? | "Buat critical review terstruktur." |
| **F — Format** | Bentuk output? | "Output sebagai tabel + paragraf, maksimal 600 kata." |
| **C — Constraints** | Batasan & aturan main? | "Hanya gunakan info dari teks; jangan menambah klaim luar." |
| **G — Guardrails** | Pencegah kesalahan/halusinasi? | "Jika data tidak ada, tulis 'tidak disebutkan'. Jangan mengarang sitasi." |

> **Aturan #1 (paling penting):** *Grounding.* Selalu perintahkan model untuk **hanya memakai sumber yang KAMU sediakan**. LLM cenderung "berhalusinasi" referensi/angka jika diminta dari ingatannya. Tempelkan teks/abstrak paper ke dalam prompt.

---

## Bagian 1 — Kerangka Prompt Universal (Copy-Paste)

Gunakan kerangka ini sebagai titik awal, lalu isi bagian `[...]`:

```
# PERAN
Kamu adalah [reviewer ahli di bidang X / asisten riset metodologis].

# KONTEKS
Saya sedang membuat [critical review / literature review] untuk [tujuan: tugas kuliah / publikasi / blog].
Audiens: [mahasiswa S2 / reviewer jurnal / praktisi].
Bahan sumber ada di bagian "SUMBER" di bawah. JANGAN gunakan pengetahuan di luar itu.

# TUGAS
[Jelaskan tugas spesifik, satu tujuan jelas.]

# FORMAT OUTPUT
[Tabel? Heading? Panjang? Gaya sitasi APA/IEEE?]

# ATURAN
1. Hanya gunakan informasi dari SUMBER. Tandai "tidak disebutkan" bila tak ada.
2. Jangan mengarang referensi, angka, atau kutipan.
3. Bedakan dengan jelas: FAKTA dari paper vs INTERPRETASI/opinimu.
4. Gunakan bahasa [Indonesia akademik / Inggris formal].

# SUMBER
[Tempel abstrak / teks paper di sini]
```

---

## Bagian 2 — Prompt per Tahap (A: Critical Review Satu Artikel)

### 2.1 Pemahaman & Ringkasan Terstruktur
```
PERAN: Kamu asisten riset teliti.
TUGAS: Dari teks paper di bawah, isi tabel berikut TANPA menambah info luar:
| Elemen | Isi |
| Masalah/research question | |
| Tujuan | |
| Metode & desain | |
| Dataset/sampel & ukuran | |
| Temuan utama (dengan angka bila ada) | |
| Kesimpulan penulis | |
| Keterbatasan yang DIAKUI penulis | |
Bila suatu elemen tidak ada di teks, tulis "tidak disebutkan".

SUMBER: [tempel teks]
```

### 2.2 Evaluasi Kritis (inti dari "review")
```
PERAN: Kamu reviewer jurnal yang adil tapi tajam.
TUGAS: Evaluasi paper berikut pada 5 dimensi. Untuk tiap dimensi beri:
(a) penilaian, (b) bukti dari teks (kutip kalimat/bagian), (c) saran perbaikan.
Dimensi:
1. Orisinalitas & kontribusi
2. Ketepatan metodologi
3. Validitas & dukungan data terhadap klaim
4. Kejelasan & struktur
5. Keterbatasan & ancaman validitas (termasuk yang TIDAK diakui penulis)

Pisahkan dengan jelas mana FAKTA dari paper dan mana OPINI-mu sebagai reviewer.
Jangan menilai hal yang tidak bisa kamu verifikasi dari teks.

SUMBER: [tempel teks]
```

### 2.3 Verdict & Rekomendasi
```
TUGAS: Berdasarkan evaluasi sebelumnya, tulis:
- Ringkasan 3 kekuatan utama
- 3 kelemahan utama (urut berdasarkan dampak)
- Rekomendasi keputusan: Accept / Minor revision / Major revision / Reject — beserta alasan singkat.
Maksimal 300 kata, nada profesional & konstruktif.
```

---

## Bagian 3 — Prompt per Tahap (B: Literature / Review Article)

### 3.1 Pertajam Pertanyaan Review
```
PERAN: Kamu metodolog literature review.
TUGAS: Saya ingin mereview topik "[TOPIK]". Bantu saya:
1. Rumuskan 1 research question utama + 2-3 sub-pertanyaan (gunakan kerangka PICOC bila relevan).
2. Tentukan kriteria inklusi & eksklusi (tahun, jenis studi, bahasa, dll).
3. Usulkan 3-5 tema yang mungkin muncul (sebagai hipotesis awal, untuk divalidasi nanti).
```

### 3.2 Bangun String Pencarian (Boolean)
```
TUGAS: Buat string pencarian Boolean untuk topik di atas, untuk digunakan di
Google Scholar / Scopus. Sertakan sinonim & operator (AND/OR, tanda kutip, wildcard).
Tampilkan 2-3 variasi (luas vs sempit). Jangan mengarang nama database/artikel.
```
> Catatan: model membuat *query*-nya; **pencarian & pengambilan paper tetap kamu lakukan** di database asli. Lalu tempelkan hasilnya kembali untuk tahap berikut.

### 3.3 Ekstraksi Banyak Paper ke Tabel Sintesis
```
TUGAS: Untuk SETIAP paper di SUMBER (dipisah "==="), isi satu baris tabel:
| ID | Penulis & Tahun | Tujuan | Metode | Dataset | Temuan utama | Keterbatasan | Tema |
Hanya gunakan info eksplisit. Jangan menyimpulkan tema yang tidak didukung teks.

SUMBER:
=== Paper 1 ===
[abstrak/teks]
=== Paper 2 ===
[abstrak/teks]
```

### 3.4 Sintesis Tematik (bukan sekadar daftar)
```
TUGAS: Dari tabel ekstraksi berikut, lakukan SINTESIS (bukan ringkasan per paper):
1. Kelompokkan temuan ke dalam tema.
2. Untuk tiap tema: titik konsensus, perdebatan/kontradiksi antar studi, dan gap.
3. Identifikasi 1-2 "gap penelitian" yang paling layak diteliti lanjut.
Rujuk paper dengan ID-nya (mis. [P1], [P3]) — jangan membuat sitasi baru.

DATA: [tempel tabel ekstraksi]
```

### 3.5 Drafting per Bagian
```
TUGAS: Tulis bagian "[Pendahuluan / Pembahasan tema X / Kesimpulan]" dari review article.
- Panjang: [~400 kata].
- Gaya: akademik, alur argumentatif (bukan daftar berpoin).
- Rujuk hanya paper dengan ID yang ada di DATA, format [P#].
- Tandai [PERLU SITASI] bila sebuah klaim butuh referensi yang belum ada — JANGAN mengarang.

DATA: [tempel sintesis + tabel]
```

### 3.6 Cek Konsistensi & Kualitas (self-review)
```
PERAN: Kamu editor jurnal.
TUGAS: Periksa draft berikut:
1. Adakah klaim tanpa dukungan sumber? Tandai.
2. Adakah sitasi/angka yang tidak ada di DATA? Tandai sebagai POTENSI HALUSINASI.
3. Apakah alur antar paragraf logis? Beri saran.
4. Konsistensi istilah & gaya sitasi.
Jangan menulis ulang; cukup beri daftar temuan + saran.

DRAFT: [tempel]
DATA: [tempel sumber]
```

---

## Bagian 4 — Teknik Lanjutan (yang Membedakan Hasil Bagus vs Biasa)

1. **Grounding ketat.** Selalu sertakan instruksi: *"Hanya gunakan SUMBER; tandai 'tidak disebutkan' bila kosong."* Ini senjata utama melawan halusinasi.
2. **Pisahkan FAKTA vs OPINI.** Minta model menandai mana yang dari teks dan mana interpretasinya. Krusial untuk integritas review.
3. **Chain-of-thought bertahap.** Jangan minta "buatkan review lengkap" sekaligus. Pecah: ekstraksi → sintesis → draft → review. Tiap output jadi input tahap berikut. Hasil jauh lebih akurat & mudah dikontrol.
4. **Few-shot (beri contoh).** Tempelkan 1 contoh baris tabel/paragraf yang formatnya kamu mau. Model meniru gaya & struktur.
5. **Role prompting spesifik.** "Reviewer jurnal Q1 bidang X" memberi hasil lebih kritis daripada "tolong review".
6. **Iterative refinement.** Minta draft v1, lalu beri kritik spesifik: *"Perdalam analisis metodologi di paragraf 2; terlalu umum."*
7. **Red-team prompt.** Minta model **mengkritik hasilnya sendiri**: *"Sebagai reviewer skeptis, temukan 3 kelemahan terbesar dari review ini."*
8. **Adaptasi gaya jurnal.** *"Sesuaikan dengan gaya & format penulisan jurnal [nama], maksimal [N] kata, sitasi [IEEE]."*

---

## Bagian 5 — Kesalahan Umum & Cara Memperbaiki

| ❌ Prompt buruk | Kenapa gagal | ✅ Perbaikan |
|----------------|--------------|-------------|
| "Buatkan literature review tentang X" | Tanpa sumber → model mengarang sitasi & fakta | Sediakan paper; minta grounding ketat |
| "Ringkas paper ini" | Hasilnya deskriptif, bukan kritis | Minta evaluasi 5 dimensi + bukti dari teks |
| "Buat review 2000 kata sekaligus" | Sulit dikontrol, banyak error menumpuk | Pecah bertahap (ekstraksi→sintesis→draft) |
| "Apakah paper ini bagus?" | Terlalu kabur | Definisikan kriteria penilaian eksplisit |
| Tanpa format | Output tidak konsisten | Tentukan struktur/tabel/panjang |
| Tanpa guardrail sitasi | Referensi palsu lolos | "Tandai [PERLU SITASI]; jangan mengarang" |

---

## Bagian 6 — Contoh Rantai Prompt End-to-End (Ringkas)

```
Langkah 1  → Prompt 3.1 : tentukan research question + kriteria
Langkah 2  → Prompt 3.2 : buat string pencarian → (KAMU cari paper di Scopus)
Langkah 3  → Prompt 3.3 : tempel abstrak → tabel ekstraksi
Langkah 4  → Prompt 3.4 : sintesis tematik + gap
Langkah 5  → Prompt 3.5 : draft per bagian (Intro, tema, kesimpulan)
Langkah 6  → Prompt 3.6 : self-review + tandai potensi halusinasi
Langkah 7  → (KAMU) verifikasi setiap sitasi ke sumber asli + poles akhir
```

> Output tiap langkah menjadi input langkah berikutnya. Peran manusia tetap wajib di Langkah 2 (pengambilan paper) dan Langkah 7 (verifikasi & tanggung jawab akademik).

---

## Bagian 7 — Checklist Prompt Article Review yang Baik

- [ ] Sudah menetapkan **peran/persona** yang relevan?
- [ ] **Sumber ditempelkan** (bukan mengandalkan ingatan model)?
- [ ] **Tugas tunggal & jelas** (tidak menumpuk banyak permintaan sekaligus)?
- [ ] **Format output** ditentukan (tabel/heading/panjang/gaya sitasi)?
- [ ] Ada perintah **"hanya gunakan sumber" + "tandai bila tidak ada"**?
- [ ] Ada larangan **mengarang sitasi/angka**?
- [ ] Diminta **memisahkan fakta vs opini**?
- [ ] Proses **dipecah bertahap**, bukan sekali jadi?
- [ ] Ada langkah **self-review / red-team**?
- [ ] Kamu berkomitmen **verifikasi manual** semua sitasi di akhir?

---

## Catatan Integritas
Prompt sebaik apa pun **tidak menggantikan tanggung jawab penulis**. LLM membantu *menstrukturkan, meringkas, dan menyusun bahasa* — keputusan ilmiah, verifikasi sumber, dan akurasi akhir tetap pada kamu. Banyak jurnal kini mewajibkan **disclosure penggunaan AI**; patuhi aturan tiap penerbit.
