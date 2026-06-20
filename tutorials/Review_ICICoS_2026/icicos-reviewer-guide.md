# Panduan Reviewer ICICoS 2026 — Review Berbantuan AI yang Etis & Bernilai Tinggi

Template otomasi review yang *reusable* (dapat dipakai berulang untuk paper apa pun di ICICoS),
dengan penekanan kuat pada **etika penggunaan AI** — titik yang paling sering jadi celah ketika
reviewer mulai memakai AI.

> Catatan sumber: ICICoS (International Conference on Informatics and Computational Sciences)
> adalah konferensi IEEE yang dikelola Universitas Diponegoro. Daftar bidang di bawah disusun
> dari cakupan resmi "Informatics & Computational Sciences" konferensi ini pada edisi-edisi
> sebelumnya. *Content was rephrased for compliance with licensing restrictions.*

---

## 0. Header / Metadata Review (wajib diisi reviewer)

```
paper_file    : draft v3.pdf
paper_id      : 123123123
paper_title   : Improving Machine Learning Classification of Container Dwelling
                Time Violations Using Early Process Signatures
reviewer_id   : R-____
review_round  : ____
recommendation: [Accept / Minor Revision / Major Revision / Reject]
overall_score : __ / 10
confidence    : [1=Rendah  2=Sedang  3=Tinggi  4=Sangat Tinggi]
```

---

## 1. Keahlian (Expertise) — reviewer WAJIB memilih & mempertahankan SATU

Pilih **satu** bidang yang paling dekat dengan paper, lalu pada kolom *justifikasi* reviewer
harus menjelaskan kenapa kompetensinya valid. Semua opsi berada dalam cakupan ICICoS dan relevan
dengan topik paper (klasifikasi ML untuk pelanggaran *dwelling time* peti kemas — irisan ML +
logistik/proses bisnis).

| Kode | Bidang Keahlian (ICICoS) | Relevansi dengan paper ini |
|------|--------------------------|----------------------------|
| **A** | Machine Learning & Pattern Recognition | Inti paper: model klasifikasi, fitur, evaluasi |
| **B** | Data Science / Data Mining & Big Data Analytics | Rekayasa fitur "early process signatures", kualitas data |
| **C** | Artificial Intelligence & Intelligent Systems | Pendekatan AI untuk pengambilan keputusan |
| **D** | Decision Support Systems & Business Process Analytics | Konteks deteksi pelanggaran/proses operasional pelabuhan |
| **E** | Information Systems & Enterprise/Logistics Systems | Domain logistik peti kemas, integrasi sistem pelabuhan |
| **F** | Computational Science, Optimization & Operations Research | Pemodelan waktu proses, optimasi prediksi |
| **G** | Time-Series & Predictive Analytics | "Early signatures" = sinyal temporal awal proses |

> **Format justifikasi keahlian (diisi reviewer):**
> `Keahlian dipilih: [A] — Justifikasi: "Saya memilih Machine Learning karena ...
> (pengalaman/publikasi/keilmuan). Saya kompeten menilai pilihan algoritma, protokol evaluasi,
> dan klaim performa pada paper ini."`

---

## 2. Aturan Etika & Penggunaan AI (BACA DULU)

Pagar yang membuat AI bernilai tinggi **tanpa** melanggar integritas IEEE:

**DILARANG**
1. **Mengunggah manuskrip / bagian manuskrip ke AI publik** (mis. ChatGPT publik). Manuskrip
   bersifat rahasia, sehingga mengunggahnya melanggar kerahasiaan peer review. Gunakan hanya tool
   yang menjamin data tidak dipakai untuk training.
2. **Mendelegasikan keputusan akhir ke AI.** Rekomendasi Accept/Reject tetap tanggung jawab manusia.
3. **Membuat klaim/temuan fiktif** dari AI (halusinasi referensi, angka, atau "kelemahan" yang
   tidak ada).

**BOLEH (penggunaan bijak & bernilai)**
4. AI sebagai **asisten bahasa**: merapikan tata bahasa & nada komentar agar profesional.
5. AI sebagai **checklist/penstruktur**: memastikan tiap section tertinjau, format komentar konsisten.
6. AI untuk **brainstorming pertanyaan** — tetapi reviewer **memverifikasi** setiap poin terhadap
   isi paper.

**WAJIB**
7. **Disclosure**: reviewer mencantumkan satu baris di akhir: *"AI digunakan terbatas untuk
   [perapihan bahasa/penstrukturan], seluruh penilaian substantif dilakukan dan diverifikasi oleh
   reviewer."*
8. **Akuntabilitas**: setiap komentar harus bisa ditelusuri ke baris/halaman paper yang nyata.

---

## 3. Struktur Komentar per-Section (kerangka daftar komentar)

Reviewer mengisi komentar di tiap section memakai **format komentar** dari Bagian 4. Berikan
minimal jumlah yang disarankan agar review menyeluruh.

| Section | Fokus penilaian | Min. komentar |
|---------|-----------------|---------------|
| **S1. Abstract** | Klaim sepadan dengan hasil? Angka kunci ada? | 1–2 |
| **S2. Introduction & Motivasi** | Masalah jelas? Kontribusi eksplisit & dapat diuji? | 2–3 |
| **S3. Related Work** | Posisi vs literatur? Ada *gap* yang dijelaskan? Sitasi mutakhir? | 2 |
| **S4. Data & Early Process Signatures** | Sumber data, label "violation", definisi fitur "early signature", kebocoran data (*leakage*)? | 3–4 |
| **S5. Metodologi / Model** | Pilihan algoritma, baseline, hyperparameter, validasi | 3–4 |
| **S6. Eksperimen & Hasil** | Metrik (akurasi vs F1 untuk data tak seimbang), signifikansi, ablation | 3–4 |
| **S7. Diskusi** | Interpretasi, batasan, ancaman validitas | 2 |
| **S8. Kesimpulan & Future Work** | Klaim tidak berlebihan, arah lanjutan konkret | 1–2 |
| **S9. Referensi & Format** | Gaya IEEE, kelengkapan, kesesuaian template | 1–2 |
| **S10. Reproducibility** | Ketersediaan data/kode/parameter | 1 |

---

## 4. Pustaka Format Komentar (Format #1 + 13 format akademik tambahan)

Setiap komentar diberi **kode format** agar konsisten & dapat diotomasi. Contoh disesuaikan dengan
paper ini.

### Format #1 — Kutipan + Tanggapan + Saran (opsional, tidak strict) — format dasar
> **Kutipan:** *"...the model achieves 95% accuracy..."* (hal. X, baris Y)
> **Tanggapan:** Pada data pelanggaran *dwelling time* yang umumnya tidak seimbang, akurasi bisa menyesatkan.
> **Saran (opsional):** Pertimbangkan melaporkan F1/AUC-PR; ini saran, bukan keharusan.

### Format #2 — Klasifikasi Tingkat (Major / Minor / Optional)
> **[MAJOR]** Tidak ada baseline pembanding, sehingga klaim "improving" belum terbukti.

### Format #3 — Berbasis Pertanyaan (Clarification Request)
> **Pertanyaan:** Bagaimana "early process signature" didefinisikan secara operasional — pada menit/jam ke berapa setelah kontainer masuk?

### Format #4 — Strength–Weakness (berimbang)
> **Kekuatan:** Ide memakai sinyal proses awal untuk prediksi dini sangat relevan operasional.
> **Kelemahan:** Validasi hanya satu pelabuhan, sehingga generalisasi belum terbukti.

### Format #5 — Claim–Evidence–Gap
> **Klaim:** Metode mengungguli pendekatan konvensional.
> **Bukti yang ada:** Tabel 3 (akurasi).
> **Gap:** Tidak ada uji signifikansi statistik antar-model.

### Format #6 — Actionable, Ber-referensi Baris (numbered)
> **Aksi (hal. 5, Tabel 2):** Tambahkan jumlah sampel per kelas agar pembaca menilai keseimbangan data.

### Format #7 — Severity + Suggested Fix + Rationale (triad)
> **Severity:** Tinggi · **Fix:** Lakukan k-fold cross-validation · **Rationale:** Split tunggal rawan bias seleksi.

### Format #8 — Reproducibility Checklist
> **Reproducibility:** Dataset bersifat privat dan kode tidak tersedia. Mohon sertakan hyperparameter, seed, dan versi library, atau pernyataan ketersediaan data.

### Format #9 — Positioning terhadap Literatur (Missing Citation)
> **Literatur:** Klaim kebaruan perlu dibandingkan dengan studi prediksi *port dwell time* berbasis ML terbaru; mohon tambahkan dan posisikan kontribusi.

### Format #10 — Probe Asumsi / Hipotesis
> **Asumsi:** Paper mengasumsikan sinyal awal stabil sepanjang musim. Apakah ada efek musiman/peak season yang menggeser distribusi?

### Format #11 — Rigor Metodologis / Statistik
> **Metodologi:** Mohon laporkan mean ± std lintas run dan uji statistik (mis. McNemar/paired t-test) untuk mendukung klaim peningkatan.

### Format #12 — Kejelasan & Presentasi (Figures/Tables/Notasi)
> **Presentasi:** Gambar 4 tidak terbaca saat dicetak hitam-putih; notasi y-hat belum didefinisikan saat pertama muncul.

### Format #13 — "Consider" (saran lunak, non-binding)
> **Consider:** Penulis dapat *mempertimbangkan* analisis kepentingan fitur (SHAP) untuk meningkatkan interpretabilitas — sifatnya opsional.

### Format #14 — Komentar Apresiatif (positive reinforcement)
> **Apresiasi:** Pemilihan kasus pelanggaran *dwelling time* sebagai prediksi dini bernilai praktis tinggi dan ditulis dengan motivasi yang jelas.

> Tiap komentar idealnya diberi tag: `[ID-komentar] [Section] [Format#] [Severity] [Status: Open/Resolved]`
> agar mudah dilacak antar-ronde revisi.

---

## 5. Ketentuan Tambahan (simple, akademik, etis)

1. **Aturan "Bukti-atau-Hapus"**: setiap komentar harus menunjuk lokasi nyata (hal./baris).
   Komentar tanpa rujukan tidak sah (mencegah halusinasi AI).
2. **Nada Konstruktif**: kritik ke *naskah*, bukan ke *penulis*. Gunakan kalimat netral dan spesifik.
3. **Pemisahan Major vs Minor di ringkasan**: agar penulis & editor tahu prioritas revisi.
4. **Batas panjang kutipan**: kutip seperlunya (1–2 kalimat) demi kerahasiaan & keringkasan.
5. **Satu baris disclosure AI** di akhir review (lihat Bagian 2 poin 7).
6. **Skor terstruktur** (Novelty / Soundness / Clarity / Significance / Reproducibility,
   masing-masing 1–5) untuk konsistensi antar-reviewer.

---

## 6. Contoh Penutup Review (template jadi)

```
RINGKASAN: [2–3 kalimat netral tentang isi & kontribusi]
MAJOR ISSUES: [#1, #5, #8 ...]
MINOR ISSUES: [#6, #12 ...]
SKOR: Novelty 3 | Soundness 2 | Clarity 4 | Significance 4 | Reproducibility 2
REKOMENDASI: Major Revision
Keahlian reviewer: [A] Machine Learning — (justifikasi)
Disclosure AI: "AI digunakan terbatas untuk perapihan bahasa & penstrukturan;
seluruh penilaian substantif diverifikasi oleh reviewer."
```
