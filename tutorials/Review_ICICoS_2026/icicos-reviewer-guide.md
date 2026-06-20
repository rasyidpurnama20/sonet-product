# Panduan Reviewer ICICoS 2026 — Review Berbantuan AI

## 0. Header / Metadata Review (wajib diisi reviewer)

```
paper_file    : [submission_id]_[paper_id]_paper.pdf
paper_id      : 123123123
paper_title   : Improving Machine Learning Classification of Container Dwelling
                Time Violations Using Early Process Signatures
```

---

## 1. Keahlian (Expertise) — reviewer WAJIB memilih & mempertahankan SATU

Pilih **satu** bidang yang paling dekat dengan paper, lalu pada kolom *justifikasi* reviewer
harus menjelaskan kenapa kompetensinya valid. Semua opsi berada dalam cakupan ICICoS dan relevan
dengan topik paper.

| No | Bidang Keahlian (ICICoS) | Relevansi dengan paper ini |
|------|--------------------------|----------------------------|
| **1** | Machine Learning & Pattern Recognition | Inti paper: model klasifikasi, fitur, evaluasi |
| **2** | Data Science / Data Mining & Big Data Analytics | Rekayasa fitur "early process signatures", kualitas data |
| **3** | Artificial Intelligence & Intelligent Systems | Pendekatan AI untuk pengambilan keputusan |
| **4** | Decision Support Systems & Business Process Analytics | Konteks deteksi pelanggaran/proses operasional pelabuhan |
| **5** | Information Systems & Enterprise/Logistics Systems | Domain logistik peti kemas, integrasi sistem pelabuhan |
| **6** | Computational Science, Optimization & Operations Research | Pemodelan waktu proses, optimasi prediksi |
| **7** | Time-Series & Predictive Analytics | "Early signatures" = sinyal temporal awal proses |

> **Format justifikasi keahlian (diisi reviewer):**
```
keahlian      : Machine Learning ...
justifikasi   : Saya memilih Machine Learning karena ...
```

---

## 2. Aturan Etika & Penggunaan AI (BACA DULU)

1. **DILARANG Mengunggah manuskrip / bagian manuskrip ke AI publik** (mis. ChatGPT publik). Manuskrip
   bersifat rahasia, sehingga mengunggahnya melanggar kerahasiaan peer review. Gunakan hanya tool
   yang menjamin data tidak dipakai untuk training.
2. **DILARANG Mendelegasikan keputusan akhir ke AI.** Rekomendasi Accept/Reject tetap tanggung jawab manusia.
3. **DILARANG Membuat klaim/temuan fiktif** dari AI (halusinasi referensi, angka, atau "kelemahan" yang
   tidak ada).
4. AI sebagai **asisten bahasa**: merapikan tata bahasa & nada komentar agar profesional.
5. AI sebagai **checklist/penstruktur**: memastikan tiap section tertinjau, format komentar konsisten.
6. AI untuk **brainstorming pertanyaan** — tetapi reviewer **memverifikasi** setiap poin terhadap
   isi paper.
7. **Akuntabilitas**: setiap komentar harus bisa ditelusuri ke baris/halaman paper yang nyata.

---

## 3. Struktur Komentar per-Section (kerangka daftar komentar)

Agent dapat membuat komentar di tiap section memakai **format komentar** dari Bagian 4. Pastikan jumlah komentar di setiap format komentar agar review menyeluruh: 
#### S1 Abstract, fokus pada kesesuaian klaim dengan hasil dan keberadaan angka kunci; 
#### S2 Introduction & Motivasi, fokus pada kejelasan masalah, urgensi, kontribusi, dan apakah kontribusi dapat diuji; 
#### S3 Related Work, fokus pada posisi penelitian terhadap literatur, kejelasan gap, dan kemutakhiran sitasi; 
#### S4 Data & Early Process Signatures, fokus pada sumber data, kejelasan atribut, kualitas data, serta potensi data leakage; 
#### S5 Metodologi/Model, fokus pada pemilihan algoritma, baseline, hyperparameter, validasi, dan replikabilitas; 
#### S6 Eksperimen & Hasil, fokus pada metrik, ketidakseimbangan data, signifikansi, ablation, dan kejelasan hasil; 
#### S7 Diskusi, fokus pada interpretasi, batasan, dan ancaman validitas; 
#### S8 Kesimpulan & Future Work; 
#### S9 Referensi & Kepatuhan Format; 
#### S10 Tatabahasa dan efektifitas kalimat; dan
#### S11 Reproducibility.

---

## 4. Pustaka Format Komentar

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

## 5. Ketentuan Tambahan

1. **Aturan "Bukti-atau-Hapus"**: setiap komentar harus menunjuk lokasi nyata (hal./baris).
   Komentar tanpa rujukan tidak sah (mencegah halusinasi AI).
2. **Nada Konstruktif**: kritik ke *naskah*, bukan ke *penulis*. Gunakan kalimat netral dan spesifik.
3. **Pemisahan Major vs Minor di ringkasan**: agar penulis & editor tahu prioritas revisi.
4. **Batas panjang kutipan**: kutip seperlunya (1–2 kalimat) demi kerahasiaan & keringkasan.

---
