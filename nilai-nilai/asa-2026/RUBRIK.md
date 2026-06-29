# RUBRIK PENILAIAN TUGAS KELOMPOK ASA 2026

**Mata Kuliah:** Analisis dan Strategi Algoritma (ASA)  
**Tahun Ajaran:** 2025/2026  
**Jenis Tugas:** Tugas Kelompok — Decrease and Conquer / Divide and Conquer  
**Berlaku untuk:** Kelas A, B, C, D, E

---

## Deskripsi Tugas

Setiap kelompok (3–4 anggota) diminta untuk:

1. Menentukan **3 persoalan komputasi** berbeda pada data minimal **n ≥ 30 baris**, menggunakan 3 jenis algoritma sesuai topik:
   - **Jenis 1 — Decrease-by-a-Constant** (misal: Sequential Search, Insertion Sort, Bubble Sort, Recursive Summation)
   - **Jenis 2 — Decrease-by-Constant-Factor** (misal: Binary Search, Jump Search, Fast Exponentiation, Ternary Search)
   - **Jenis 3 — Decrease-by-Variable-Size / Probabilistik** (misal: QuickSelect Randomized, Randomized QuickSort, Randomized Pivot)
   > *Catatan: Kelas C menggunakan topik **Divide and Conquer**. Kriteria penilaian tetap sama.*

2. Menyusun **laporan tertulis** yang memuat:
   - Notasi fungsional algoritma
   - Analisis kompleksitas (Big-O)
   - Ilustrasi langkah-langkah algoritma dengan data contoh
   - Eksperimen probabilistik (khusus persoalan jenis 3 / randomized)

3. Memastikan **keunikan persoalan** — tidak boleh sama atau sangat mirip antar kelompok dalam satu kelas.

4. **Tidak ada plagiarisme** antar kelompok maupun dari sumber lain.

---

## Komponen Penilaian

| Kode | Komponen | Sub-Komponen | Bobot |
|------|----------|--------------|-------|
| **A** | **Kelengkapan & Relevansi Masalah** | | **20** |
| A.1 | | Ketiga persoalan relevan dan sesuai jenis algoritma yang ditentukan | 10 |
| A.2 | | Data minimal n ≥ 30 baris terpenuhi untuk tiap persoalan | 5 |
| A.3 | | Persoalan unik / tidak sama dengan kelompok lain dalam kelas yang sama | 5 |
| **B** | **Notasi Fungsional** | | **15** |
| B.1 | | Notasi fungsional benar untuk Persoalan 1 (Jenis Constant) | 5 |
| B.2 | | Notasi fungsional benar untuk Persoalan 2 (Jenis Constant-Factor) | 5 |
| B.3 | | Notasi fungsional benar untuk Persoalan 3 (Jenis Variable-Size/Probabilistik) | 5 |
| **C** | **Analisis Kompleksitas** | | **20** |
| C.1 | | Analisis Big-O tepat dan dijelaskan untuk Persoalan 1 | 6 |
| C.2 | | Analisis Big-O tepat dan dijelaskan untuk Persoalan 2 | 7 |
| C.3 | | Analisis Big-O tepat dan dijelaskan untuk Persoalan 3 | 7 |
| **D** | **Ilustrasi Langkah Algoritma** | | **20** |
| D.1 | | Langkah/trace algoritma jelas dan benar untuk Persoalan 1 | 6 |
| D.2 | | Langkah/trace algoritma jelas dan benar untuk Persoalan 2 | 7 |
| D.3 | | Langkah/trace algoritma jelas dan benar untuk Persoalan 3 | 7 |
| **E** | **Eksperimen Probabilistik** | | **15** |
| E.1 | | Desain & metodologi eksperimen jelas (input, proses, variabel) | 5 |
| E.2 | | Analisis distribusi / hasil probabilistik dicantumkan dengan data nyata | 5 |
| E.3 | | Kesimpulan berbasis data eksperimen valid dan relevan | 5 |
| **F** | **Kualitas Laporan** | | **10** |
| F.1 | | Struktur laporan lengkap (pendahuluan, isi, kesimpulan) | 4 |
| F.2 | | Kejelasan penulisan, tata bahasa, dan konsistensi format | 3 |
| F.3 | | Referensi / sumber pustaka dicantumkan | 3 |
| | **TOTAL** | | **100** |

---

## Skala Skor Per Sub-Komponen

Setiap sub-komponen dinilai menggunakan skala berikut:

| Skor | Deskripsi |
|------|-----------|
| **Penuh** | Tepat, lengkap, tidak ada kesalahan signifikan |
| **Sebagian (60–80%)** | Benar secara umum, ada kekurangan kecil atau ketidakjelasan |
| **Minimal (30–50%)** | Ada upaya, tetapi terdapat kesalahan mendasar atau tidak lengkap |
| **0** | Tidak ada / tidak relevan |

---

## Pedoman Penilaian Per Komponen

### A — Kelengkapan & Relevansi Masalah
- **A.1 (10):** Periksa apakah ketiga persoalan memang menggunakan tipe algoritma yang benar (Constant / Constant-Factor / Variable-Size). Nilai penuh jika semua 3 sesuai.
- **A.2 (5):** Cek apakah data yang digunakan dalam setiap persoalan memiliki n ≥ 30. Nilai penuh jika semua persoalan memenuhi.
- **A.3 (5):** Bandingkan judul/persoalan antar kelompok dalam kelas yang sama. Potong nilai jika ada kemiripan signifikan.

### B — Notasi Fungsional
- Notasi fungsional harus menunjukkan: nama fungsi, parameter input, output, dan langkah rekursif/iteratif secara formal.
- **B.1–B.3 (masing-masing 5):** Nilai penuh jika notasi formal benar dan konsisten dengan kode/pseudocode yang disajikan.

### C — Analisis Kompleksitas
- Harus mencantumkan notasi Big-O beserta **penjelasan/derivasi**, bukan hanya menyebutkan hasilnya.
- **C.1 (6), C.2 (7), C.3 (7):** Nilai disesuaikan bobot kesulitan persoalan. Penalti jika Big-O salah atau tidak ada penjelasan.

### D — Ilustrasi Langkah Algoritma
- Ilustrasi dapat berupa tabel trace, diagram, pseudocode dengan contoh, atau gambar.
- **D.1 (6), D.2 (7), D.3 (7):** Nilai penuh jika langkah-langkah jelas, menggunakan data nyata (bukan data trivial 1–5 saja), dan benar.

### E — Eksperimen Probabilistik
- Berlaku khusus untuk Persoalan 3 (Decrease-by-Variable-Size / Randomized).
- **E.1 (5):** Metodologi jelas: berapa kali percobaan, variasi input, kondisi eksperimen.
- **E.2 (5):** Hasil percobaan ditampilkan (tabel/grafik), distribusi dianalisis.
- **E.3 (5):** Kesimpulan relevan, misalnya: "rata-rata waktu mendekati O(n)", "distribusi mendekati uniform", dll.
- *Jika persoalan 3 tidak bersifat probabilistik/randomized, komponen E dapat digantikan dengan analisis kasus terbaik/terburuk/rata-rata.*

### F — Kualitas Laporan
- **F.1 (4):** Laporan memiliki pendahuluan, isi per persoalan, dan kesimpulan.
- **F.2 (3):** Penulisan rapi, tidak ada inkonsistensi format, tata bahasa baik.
- **F.3 (3):** Ada daftar pustaka/referensi. Nilai 0 jika tidak ada sama sekali.

---

## Konversi Nilai Akhir

| Rentang Skor | Nilai Huruf |
|:------------:|:-----------:|
| 85 – 100 | **A** |
| 75 – 84 | **AB** |
| 65 – 74 | **B** |
| 55 – 64 | **BC** |
| 45 – 54 | **C** |
| 35 – 44 | **CD** |
| 25 – 34 | **D** |
| < 25 | **E** |

---

## Catatan Khusus

1. **Link laporan tidak aktif / tidak bisa diakses:** Nilai komponen B, C, D, E = 0. Nilai A.1, A.2 dipertimbangkan berdasarkan daftar persoalan yang dicantumkan.
2. **Anggota kelompok dengan NIM tidak lengkap:** Catat di kolom "Catatan". Nilai tetap diberikan ke kelompok selama laporan dapat diakses.
3. **Kelompok dengan anggota < 3:** Perlu konfirmasi ke mahasiswa. Jika hanya 1–2 anggota, pertimbangkan pengurangan ekspektasi (misal: cukup 2 persoalan).
4. **Plagiarisme terdeteksi:** Nilai komponen A.3 = 0, dan jika plagiarisme berat, seluruh nilai dapat dibatalkan sesuai kebijakan dosen.
5. **Kelas C (Divide and Conquer):** Kriteria penilaian identik. Sesuaikan terminologi "Jenis 1/2/3" dengan tipe D&C yang digunakan kelompok.

---

*Rubrik ini berlaku konsisten untuk semua kelas (A–E) ASA 2026.*
