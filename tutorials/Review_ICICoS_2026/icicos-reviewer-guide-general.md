# Panduan Reviewer ICICoS — Review Berbantuan AI (Panduan Umum)

> **Versi:** 1.1 · **Berlaku untuk:** ICICoS 2026 dan seterusnya  
> **Bahasa komentar:** Bahasa Indonesia atau Inggris (konsisten per review)  
> **Lingkup:** Berlaku untuk semua submission di semua topik ICICoS

---

## BAGIAN A — DEKLARASI AWAL (SETELAH DIGENERATE WAJIB DIVERIFIKASI REVIEWER SEBELUM MEMULAI REVIEW)

Isi bagian ini sebelum membaca naskah lebih jauh.

```
paper_id          : [diisi sesuai sistem submission]
paper_title       : [diisi sesuai judul paper]
tanggal_review    : [YYYY-MM-DD]

--- Deklarasi Keahlian ---
bidang_keahlian   : [sebutkan 1–2 bidang utama reviewer]
justifikasi       : [jelaskan secara singkat mengapa reviewer kompeten menilai paper ini]
tingkat_keyakinan : [ ] Expert (4) — pernah publikasi di area persis ini
                    [ ] High (3)   — familiar, telah membaca literatur kunci
                    [ ] Medium (2) — ada pemahaman dasar, bukan pakar
                    [ ] Low (1)    — di luar keahlian utama; judgement terbatas
```

---

## BAGIAN B — RUBRIK PENILAIAN RESMI ICICoS

Isi setelah menyelesaikan seluruh review. Tebalkan (**bold**) pilihan yang dipilih.

---

### B.1 Rekomendasi Keseluruhan

| Pilihan | Kriteria Operasional |
|---|---|
| **Strong Accept** | Kontribusi luar biasa; siap publikasi dengan sedikit atau tanpa revisi |
| **Accept** *(revision required)* | Kontribusi solid; ada perbaikan spesifik yang diperlukan sebelum terbit |
| **Weak Accept** *(revision required)* | Layak terbit namun membutuhkan perbaikan substansial yang teridentifikasi jelas |
| **Borderline** *(revision required)* | Kekuatan dan kelemahan seimbang; keputusan bergantung pada respons revisi |
| **Weak Reject** | Di bawah ambang batas saat ini; masalah mendasar yang mungkin bisa diperbaiki |
| **Reject** | Kelemahan fundamental yang tidak dapat diselesaikan dalam satu siklus revisi |
| **Strong Reject** | Cacat konseptual/metodologis/etika yang serius; tidak sesuai venue |

> **Rekomendasi reviewer:** `_______________`

---

### B.2 Keyakinan Reviewer *(Reviewer's Confidence)*

| Skor | Label | Deskripsi |
|---|---|---|
| **4** | Expert | Pernah publikasi di area persis ini |
| **3** | High | Familiar dan telah membaca literatur kunci |
| **2** | Medium | Pemahaman dasar, bukan pakar |
| **1** | Low | Di luar keahlian utama; judgement terbatas |
| **0** | Tidak Relevan | Area terlalu jauh dari keahlian reviewer |

> **Skor keyakinan:** `___`

---

### B.3 Kualitas Artikel *(Quality of the Article)*

Untuk setiap kriteria, pilih satu level dan sertakan **justifikasi singkat (1–2 kalimat)**.

#### Novelty / Originality
*Seberapa orisinal kontribusi paper ini dibandingkan literatur yang ada?*

| Level | Deskripsi |
|---|---|
| **Excellent** | Kontribusi baru yang belum pernah dipublikasikan; secara jelas memajukan state-of-the-art |
| **Good** | Kemajuan inkremental yang berarti atas penelitian sebelumnya |
| **Adequate** | Kebaruan terbatas; ada aspek baru namun kontribusi modest |
| **Inadequate** | Tidak ada kebaruan yang jelas; menduplikasi karya yang sudah ada |

> **Pilihan:** `_______________`  
> **Justifikasi:** `_______________`

---

#### Significance of Topic
*Apakah topik ini memberikan kontribusi signifikan bagi komunitas ilmiah atau praktik?*

| Level | Deskripsi |
|---|---|
| **Excellent** | Dampak tinggi; mengatasi masalah terbuka yang penting |
| **Good** | Dampak moderat; mengatasi masalah yang relevan |
| **Adequate** | Dampak terbatas; relevansi sempit atau terspesialisasi |
| **Inadequate** | Topik tidak signifikan atau tidak relevan dengan venue |

> **Pilihan:** `_______________`  
> **Justifikasi:** `_______________`

---

#### Technical Quality
*Seberapa ketat metodologi, validasi, dan analisis yang digunakan?*

| Level | Deskripsi |
|---|---|
| **Excellent** | Metodologi ketat dan valid; hasil meyakinkan dan dapat direplikasi |
| **Good** | Umumnya solid dengan kekhawatiran teknis minor |
| **Adequate** | Dapat diterima namun ada celah teknis yang perlu ditutup |
| **Inadequate** | Cacat teknis mendasar; hasil tidak dapat diandalkan |

> **Pilihan:** `_______________`  
> **Justifikasi:** `_______________`

---

#### Presentation
*Seberapa baik readability, organisasi, dan kualitas penulisan paper?*

| Level | Deskripsi |
|---|---|
| **Excellent** | Sangat jelas, terorganisir, penulisan profesional |
| **Good** | Jelas dan terorganisir dengan isu minor |
| **Adequate** | Dapat dibaca namun perlu perbaikan kejelasan/organisasi |
| **Inadequate** | Sulit dipahami; masalah penulisan yang signifikan |

> **Pilihan:** `_______________`  
> **Justifikasi:** `_______________`

---

#### Literature
*Apakah tinjauan pustaka lengkap, terkini, dan diposisikan dengan baik?*

| Level | Deskripsi |
|---|---|
| **Excellent** | Komprehensif, terkini, kontribusi diposisikan dengan jelas |
| **Good** | Cakupan memadai dengan celah minor |
| **Adequate** | Tidak lengkap namun mencakup referensi inti |
| **Inadequate** | Celah besar; melewatkan karya terkait yang penting |

> **Pilihan:** `_______________`  
> **Justifikasi:** `_______________`

---

## BAGIAN C — CHECKLIST REVIEW PER SEKSI

Centang hanya item yang benar-benar sudah diperiksa dan terpenuhi berdasarkan isi paper. Jika suatu item sudah diperiksa tetapi tidak terpenuhi, jangan dicentang dan tuliskan komentar perbaikannya pada Bagian D. Jika suatu item tidak relevan dengan jenis paper, metode, data, atau ruang lingkup penelitian, lewati item tersebut secara fleksibel. Anda tidak boleh hanya mengikuti checklist secara mekanis; pada setiap subbagian C.1 sampai C.11, Anda juga wajib mencari temuan kritis tambahan di luar item yang tersedia.

### C.1 Abstract

* [ ] Klaim utama sesuai dengan hasil yang benar-benar dilaporkan dalam paper.
* [ ] Tujuan, metode, data, hasil, dan kontribusi muncul secara ringkas.
* [ ] Angka/metrik kunci disebutkan secara eksplisit jika paper berbasis eksperimen.
* [ ] Kontribusi dinyatakan jelas, spesifik, dan tidak terlalu umum.
* [ ] Abstract tidak berisi klaim yang tidak dibuktikan di bagian hasil.
* [ ] Dataset, objek studi, atau domain aplikasi disebutkan bila relevan.
* [ ] Metode/model utama disebutkan, bukan hanya istilah umum seperti “AI” atau “machine learning”.
* [ ] Hasil utama disampaikan dengan konteks pembanding, misalnya lebih baik dari baseline.
* [ ] Tidak ada istilah teknis yang ambigu atau terlalu promosi.
* [ ] Abstract dapat dipahami tanpa harus membaca seluruh paper.

### C.2 Introduction & Motivasi

* [ ] Masalah penelitian didefinisikan dengan jelas.
* [ ] Urgensi masalah didukung oleh data, literatur, atau kebutuhan nyata.
* [ ] Gap penelitian dijelaskan secara eksplisit, bukan hanya menyatakan “belum banyak penelitian”.
* [ ] Kontribusi paper spesifik dan dapat diuji/diverifikasi.
* [ ] Pertanyaan penelitian, tujuan, atau hipotesis dinyatakan dengan jelas.
* [ ] Konteks domain dijelaskan cukup agar pembaca memahami pentingnya masalah.
* [ ] Novelty dibedakan dari sekadar penerapan metode lama pada data baru.
* [ ] Ruang lingkup penelitian tidak terlalu luas dan tidak terlalu sempit.
* [ ] Batasan awal penelitian disebutkan bila penting.
* [ ] Struktur paper dijelaskan di akhir Introduction secara ringkas.

### C.3 Related Work

* [ ] Literatur yang digunakan relevan dengan topik, metode, dan domain.
* [ ] Sitasi mencakup karya fundamental dan karya terbaru.
* [ ] Gap penelitian diidentifikasi secara eksplisit dari literatur.
* [ ] Paper membandingkan posisi kontribusinya dengan penelitian sebelumnya.
* [ ] Related work tidak hanya berupa daftar ringkasan paper.
* [ ] Perbedaan metode, data, metrik, atau domain dengan studi sebelumnya dijelaskan.
* [ ] Klaim tentang keunggulan metode didukung oleh rujukan yang tepat.
* [ ] Tidak ada referensi penting yang jelas-jelas terlewat.
* [ ] Sitasi tidak berlebihan pada sumber yang kurang relevan.
* [ ] Related work mengarah secara logis ke alasan penelitian ini dilakukan.

### C.4 Data & Preprocessing

* [ ] Sumber data dijelaskan, termasuk asal, ukuran, periode, format, dan lisensi/izin akses jika relevan.
* [ ] Atribut, fitur, label, kelas, atau variabel utama didefinisikan secara operasional.
* [ ] Proses pengumpulan data dijelaskan cukup jelas.
* [ ] Prosedur preprocessing dilaporkan, seperti cleaning, filtering, imputation, normalisasi, encoding, augmentasi, atau feature extraction.
* [ ] Strategi pembagian data train/validation/test dijelaskan.
* [ ] Risiko data leakage diperiksa, termasuk duplikasi data, overlap subjek, temporal leakage, atau preprocessing sebelum split.
* [ ] Distribusi kelas, imbalance, missing value, outlier, atau noise dijelaskan bila relevan.
* [ ] Ground truth, labeling, anotator, atau sumber label dijelaskan.
* [ ] Kualitas dan keterbatasan data diakui secara eksplisit.
* [ ] Data yang digunakan sesuai untuk menjawab tujuan penelitian.

### C.5 Metodologi & Model

* [ ] Pilihan algoritma, arsitektur, atau metode dijustifikasi, bukan sekadar disebutkan.
* [ ] Alur metode dijelaskan secara runtut dari input, proses, hingga output.
* [ ] Model utama dijelaskan cukup teknis agar dapat dipahami dan direplikasi.
* [ ] Baseline yang relevan disertakan sebagai pembanding.
* [ ] Hyperparameter, konfigurasi eksperimen, dan parameter penting dilaporkan.
* [ ] Strategi validasi jelas, misalnya hold-out, cross-validation, temporal split, atau external validation.
* [ ] Asumsi metode dijelaskan dan sesuai dengan karakteristik data.
* [ ] Risiko overfitting, underfitting, bias model, atau generalisasi rendah dipertimbangkan.
* [ ] Ablation study atau analisis komponen dilakukan jika paper mengklaim kontribusi model baru.
* [ ] Kompleksitas komputasi, kebutuhan sumber daya, atau efisiensi model dibahas bila relevan.

### C.6 Eksperimen & Hasil

* [ ] Metrik evaluasi sesuai dengan karakteristik masalah dan data.
* [ ] Untuk data tidak seimbang, metrik seperti F1-score, recall, precision, AUC, balanced accuracy, atau confusion matrix dipertimbangkan.
* [ ] Hasil dibandingkan dengan baseline, metode terdahulu, atau pendekatan sederhana yang masuk akal.
* [ ] Hasil disajikan dengan rata-rata dan standar deviasi lintas run jika eksperimen bersifat stokastik.
* [ ] Uji signifikansi statistik dilakukan jika membandingkan performa antar-model.
* [ ] Tabel dan gambar terbaca, berlabel, dan direferensikan dalam teks.
* [ ] Hasil negatif, kegagalan model, atau kondisi ketika metode tidak bekerja tetap dilaporkan jika relevan.
* [ ] Eksperimen tambahan seperti robustness test, sensitivity analysis, atau error analysis dilakukan bila diperlukan.
* [ ] Interpretasi hasil tidak hanya menyebut angka, tetapi menjelaskan maknanya.
* [ ] Klaim “lebih baik” didukung oleh bukti kuantitatif dan pembanding yang adil.

### C.7 Diskusi

* [ ] Hasil diinterpretasikan secara kritis, bukan hanya mengulang tabel.
* [ ] Temuan utama dijelaskan hubungannya dengan masalah penelitian.
* [ ] Hasil dibandingkan dengan teori atau penelitian terdahulu.
* [ ] Alasan mengapa model/metode berhasil atau gagal dijelaskan.
* [ ] Limitasi penelitian diakui secara jujur.
* [ ] Ancaman validitas internal, eksternal, konstruk, dan kesimpulan dipertimbangkan jika relevan.
* [ ] Potensi bias data, bias model, atau bias interpretasi dibahas.
* [ ] Implikasi praktis atau ilmiah dijelaskan secara proporsional.
* [ ] Generalisasi hasil tidak dilebih-lebihkan di luar data/setting penelitian.
* [ ] Diskusi menunjukkan pemahaman kritis terhadap hasil, bukan sekadar promosi metode.

### C.8 Kesimpulan & Future Work

* [ ] Kesimpulan konsisten dengan hasil dan tidak over-claim.
* [ ] Kesimpulan menjawab tujuan atau pertanyaan penelitian.
* [ ] Kontribusi utama dirangkum secara spesifik.
* [ ] Angka atau temuan kunci boleh disebutkan kembali secara ringkas.
* [ ] Keterbatasan utama tidak disembunyikan.
* [ ] Future work spesifik, realistis, dan terkait langsung dengan limitasi.
* [ ] Tidak ada klaim baru yang belum dibahas pada bagian hasil/diskusi.
* [ ] Kesimpulan tidak hanya mengulang abstrak.
* [ ] Implikasi penelitian dijelaskan secara singkat jika relevan.
* [ ] Paper memberi arah yang jelas untuk penelitian atau implementasi selanjutnya.

### C.9 Referensi & Format

* [ ] Semua referensi dalam daftar pustaka dirujuk dalam teks.
* [ ] Semua sitasi dalam teks ada di daftar pustaka.
* [ ] Format sitasi konsisten dengan panduan konferensi/jurnal.
* [ ] Referensi cukup mutakhir dan mencakup karya fundamental.
* [ ] Tidak ada sitasi yang tidak relevan atau hanya digunakan sebagai pelengkap.
* [ ] Panjang paper sesuai batas halaman yang ditentukan.
* [ ] Judul, abstrak, kata kunci, heading, tabel, gambar, dan lampiran mengikuti template.
* [ ] Penomoran tabel, gambar, persamaan, dan algoritma konsisten.
* [ ] Semua tabel/gambar memiliki caption yang informatif.
* [ ] Paper rapi secara visual dan mudah dibaca.

### C.10 Reproduksibilitas

* [ ] Kode tersedia atau ada pernyataan ketersediaan kode yang jelas.
* [ ] Data tersedia atau ada pernyataan ketersediaan data yang jelas.
* [ ] Jika data/kode tidak dapat dibagikan, alasan pembatasannya dijelaskan.
* [ ] Seed, versi library, framework, hardware, dan lingkungan eksperimen dilaporkan.
* [ ] Langkah eksperimen cukup jelas untuk mereplikasi hasil utama.
* [ ] Preprocessing, training, evaluation, dan postprocessing dijelaskan secara lengkap.
* [ ] Hyperparameter dan konfigurasi model dapat ditemukan dengan mudah.
* [ ] Script, pseudo-code, workflow, atau diagram alur disediakan bila membantu.
* [ ] Hasil utama dapat ditelusuri dari data, metode, dan eksperimen yang dijelaskan.
* [ ] Paper membedakan antara hasil yang sudah direplikasi, hasil satu kali run, dan hasil estimasi.


### C.11 Tata Bahasa, Konsistensi Istilah & Tanda Baca

* [ ] Tidak ada kesalahan gramatikal yang mengganggu pemahaman
* [ ] Istilah teknis digunakan secara konsisten sepanjang naskah (tidak berganti-ganti sinonim tanpa keterangan)
* [ ] Singkatan/akronim didefinisikan saat pertama kali muncul
* [ ] Tanda baca digunakan dengan benar (koma, titik, titik dua, tanda kutip)
* [ ] Kalimat tidak terlalu panjang atau ambigu sehingga maknanya jelas saat dibaca pertama kali
* [ ] Notasi matematis konsisten dan didefinisikan sebelum digunakan

---

## BAGIAN D — KOMENTAR TERSTRUKTUR

### Definisi Severity (WAJIB dipahami sebelum memberi tag)

| Tag | Definisi | Dampak jika tidak diperbaiki |
|---|---|---|
| `[MAJOR]` | Masalah yang membuat klaim inti paper tidak dapat diverifikasi atau tidak valid | Paper tidak dapat diterima dalam kondisi ini |
| `[MINOR]` | Masalah yang mengurangi kejelasan atau kekuatan paper, tetapi tidak membatalkan klaim inti | Paper masih dapat diterima jika diperbaiki |
| `[SARAN]` | Perbaikan opsional yang dapat meningkatkan kualitas; penulis bebas mengabaikan | Tidak mempengaruhi keputusan accept/reject |

> **Aturan Akuntabilitas:** Setiap komentar `[MAJOR]` dan `[MINOR]` **wajib** menyebut lokasi nyata (halaman/seksi/tabel/gambar). Komentar tanpa rujukan tidak sah.

---

### Pustaka Format Komentar (5 Format)

---

#### Format #1 — Analitis: Masalah · Lokasi · Rekomendasi
*Gunakan untuk: masalah teknis, metodologis, atau konten yang memerlukan tindakan konkret.*

```
[MAJOR/MINOR/SARAN] [Seksi X, hal. Y]

Masalah      : Deskripsikan masalah secara objektif dan spesifik.
Lokasi       : Kutip teks atau tunjuk elemen (tabel/gambar) yang relevan — maks. 2 kalimat.
Rekomendasi  : Jelaskan tindakan konkret yang diharapkan penulis lakukan.
```

**Contoh:**
```
[MAJOR] [Seksi 5, hal. 7 — Tabel 3]

Masalah      : Klaim "model kami mengungguli baseline" tidak dapat diverifikasi karena
               tidak ada uji signifikansi statistik antar-model.
Lokasi       : "Our model achieves the highest accuracy of 94.2%..." (hal. 7, baris 12)
Rekomendasi  : Laporkan mean ± std dari minimal 5 run independen dan tambahkan uji
               McNemar atau paired t-test untuk mendukung klaim perbandingan.
```

---

#### Format #2 — Klarifikasi
*Gunakan untuk: bagian yang ambigu atau tidak lengkap, di mana reviewer butuh penjelasan sebelum dapat menilai validitasnya — bukan klaim bahwa ada kesalahan.*

```
[MINOR/SARAN] [Seksi X, hal. Y]

Pertanyaan   : Rumuskan pertanyaan spesifik yang membutuhkan jawaban dari penulis.
Konteks      : Jelaskan secara singkat mengapa klarifikasi ini penting untuk menilai paper.
```

**Contoh:**
```
[MINOR] [Seksi 4, hal. 5]

Pertanyaan   : Pada menit atau jam ke berapa setelah proses dimulai "early process
               signatures" mulai dikumpulkan, dan apakah threshold tersebut ditentukan
               secara empiris atau berdasarkan domain knowledge?
Konteks      : Definisi operasional ini kritis untuk menilai replikabilitas metode
               dan mengidentifikasi potensi data leakage pada fitur yang dibentuk.
```

---

#### Format #3 — Posisi terhadap Literatur
*Gunakan untuk: klaim kebaruan yang tidak didukung, sitasi yang hilang atau usang, atau posisi kontribusi yang tidak jelas terhadap karya terkait.*

```
[MAJOR/MINOR] [Seksi X — Related Work / Introduction]

Klaim paper  : Apa yang diklaim paper mengenai posisi atau kebaruannya.
Kesenjangan  : Karya terkait yang belum disitasi atau diposisikan dengan tepat.
Rekomendasi  : Bagaimana memperbaiki posisi kontribusi terhadap literatur yang ada.
```

**Contoh:**
```
[MINOR] [Seksi 2 — Related Work]

Klaim paper  : Paper mengklaim sebagai pendekatan pertama yang menggunakan sinyal
               temporal untuk prediksi dini dwelling time.
Kesenjangan  : Studi [A, B, C] telah menggunakan pendekatan serupa di domain logistik
               lain, tetapi karya-karya ini tidak disitasi maupun dibandingkan.
Rekomendasi  : Tambahkan dan posisikan paper ini secara eksplisit terhadap karya
               tersebut untuk memperjelas aspek kebaruan yang spesifik.
```

---

#### Format #4 — Reproduksibilitas & Transparansi
*Gunakan untuk: masalah terkait ketersediaan data/kode, detail eksperimen yang hilang, atau informasi yang diperlukan untuk mereplikasi hasil.*

```
[MAJOR/MINOR] [Seksi X / Umum]

Elemen hilang : Sebutkan informasi spesifik yang tidak tersedia dalam naskah.
Dampak        : Jelaskan mengapa ketidaktersediaan ini menghambat verifikasi hasil.
Rekomendasi   : Jelaskan apa yang perlu ditambahkan (hyperparameter, seed,
                versi library, data availability statement, dll.)
```

**Contoh:**
```
[MINOR] [Seksi 5 — Eksperimen]

Elemen hilang : Random seed, versi library (scikit-learn, TensorFlow), dan
                spesifikasi hardware tidak dilaporkan.
Dampak        : Tanpa informasi ini, hasil tidak dapat direplikasi secara independen
                dan klaim performa tidak dapat diverifikasi oleh pembaca.
Rekomendasi   : Tambahkan tabel konfigurasi eksperimen (seed, versi, hardware) atau
                sertakan kode di repositori publik dengan data availability statement
                di akhir paper.
```

---

#### Format #5 — Apresiasi (Kekuatan Paper)
*Gunakan untuk: mengakui kontribusi atau aspek yang benar-benar kuat. Minimal satu komentar apresiasi diperlukan per review untuk menjaga keseimbangan.*

```
[APRESIASI] [Seksi X atau Umum]

Aspek    : Sebutkan aspek spesifik yang layak diapresiasi.
Alasan   : Jelaskan mengapa aspek ini bernilai secara ilmiah atau praktis.
```

**Contoh:**
```
[APRESIASI] [Seksi 1 — Introduction]

Aspek    : Motivasi operasional masalah disampaikan dengan sangat jelas, dilengkapi
           data kuantitatif mengenai kerugian akibat pelanggaran dwelling time.
Alasan   : Penyajian ini membantu pembaca dari berbagai latar belakang memahami
           urgensi masalah tanpa memerlukan pengetahuan domain yang khusus.
```

---

## BAGIAN E — ATURAN ETIKA PENGGUNAAN AI

1. **DILARANG mengunggah naskah ke AI publik** (mis. ChatGPT.com). Naskah bersifat rahasia; pelanggarannya melanggar etika peer review yang diakui COPE dan IEEE.
2. **DILARANG mendelegasikan keputusan akhir ke AI.** Rekomendasi Accept/Reject adalah tanggung jawab eksklusif reviewer manusia.
3. **DILARANG mengklaim kelemahan yang tidak ada dalam naskah** (halusinasi AI). Setiap komentar harus dapat ditelusuri ke lokasi nyata dalam paper.
4. **AI diizinkan sebagai:** (a) asisten bahasa — merapikan nada dan tata bahasa komentar; (b) penstruktur — memastikan checklist lengkap; (c) alat brainstorming pertanyaan — tetapi reviewer wajib memverifikasi setiap poin terhadap isi paper secara langsung.

> Panduan ini selaras dengan: COPE Ethical Guidelines for Peer Reviewers (2017),
> IEEE PSPB Operations Manual, dan ACM Policy on Authorship and Review.

---

*Dokumen ini adalah panduan umum dan berlaku untuk semua topik submission ICICoS.* 
