# Latihan 03 — Kombinatorika & Deret

**Mata Pelajaran:** OSN Informatika 2026 — Bab 3  
**Jumlah Soal:** 42 soal  
**Tingkat Kesulitan:** Mudah (★), Sedang (★★), Sulit (★★★)  
**Tipe Soal:** Pilihan Ganda (PG), Isian Singkat (IS), Benar/Salah (B/S), Uraian (U)  
**Referensi Materi:** [03-kombinatorika-dan-deret.md](../materi/03-kombinatorika-dan-deret.md)

---

## Bagian A: Permutasi

---

### Soal 1 — Susunan Huruf Tanpa Pengulangan ★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak kata berbeda (bermakna atau tidak) yang dapat dibentuk dari huruf-huruf kata "OLIMPIADE" jika semua huruf digunakan?

**Pembahasan:**

```
Langkah 1: Identifikasi huruf
  O-L-I-M-P-I-A-D-E → total 9 huruf
  Huruf yang berulang: I muncul 2 kali
  Huruf lainnya masing-masing 1 kali

Langkah 2: Gunakan rumus permutasi dengan pengulangan
  Banyak susunan = 9! / 2!
  = 362880 / 2
  = 181440
```

**Jawaban: 181.440**

---

### Soal 2 — Permutasi Siklis ★

**Tipe:** Isian Singkat

**Soal:**  
Delapan anggota tim OSN duduk mengelilingi meja bundar untuk diskusi. Berapa banyak susunan tempat duduk yang berbeda?

**Pembahasan:**

```
Langkah 1: Untuk permutasi melingkar dengan n objek, rumusnya (n-1)!
  Pada susunan melingkar, rotasi dianggap sama.

Langkah 2: Hitung
  (8-1)! = 7! = 5040
```

**Jawaban: 5.040**

---

### Soal 3 — Permutasi dengan Syarat Posisi ★★

**Tipe:** Isian Singkat

**Soal:**  
Lima buku Matematika (M), tiga buku Fisika (F), dan dua buku Kimia (K) disusun dalam rak. Semua buku berbeda. Berapa banyak susunan jika buku-buku Matematika harus selalu bersebelahan (membentuk satu blok)?

**Pembahasan:**

```
Langkah 1: Anggap 5 buku Matematika sebagai satu blok
  Sekarang ada 1 blok M + 3 buku F + 2 buku K = 6 "objek"

Langkah 2: Susun 6 objek di rak
  = 6! = 720

Langkah 3: Dalam blok M, 5 buku bisa disusun sendiri
  = 5! = 120

Langkah 4: Total susunan
  = 6! × 5! = 720 × 120 = 86.400
```

**Jawaban: 86.400**

---

### Soal 4 — Permutasi dengan Larangan ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan 5 digit yang dapat dibentuk dari angka 1, 2, 3, 4, 5 (tanpa pengulangan) sedemikian sehingga angka 1 dan 2 tidak bersebelahan?

**Pembahasan:**

```
Langkah 1: Hitung total susunan tanpa syarat
  = 5! = 120

Langkah 2: Hitung susunan di mana 1 dan 2 bersebelahan
  Anggap {1,2} sebagai satu blok → ada 4 "objek"
  Susunan 4 objek = 4! = 24
  Dalam blok, 1 dan 2 bisa bertukar = 2! = 2
  Susunan dengan 1,2 bersebelahan = 24 × 2 = 48

Langkah 3: Susunan dengan 1 dan 2 TIDAK bersebelahan
  = 120 - 48 = 72
```

**Jawaban: 72**

---

### Soal 5 — Permutasi Multiset ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan 6 digit yang dapat dibentuk dari angka-angka pada bilangan 112233 (menggunakan semua angka)?

**Pembahasan:**

```
Langkah 1: Identifikasi angka
  Angka: 1,1,2,2,3,3 → total 6 angka
  Angka 1 muncul 2 kali
  Angka 2 muncul 2 kali
  Angka 3 muncul 2 kali

Langkah 2: Gunakan rumus permutasi dengan objek berulang
  = 6! / (2! × 2! × 2!)
  = 720 / (2 × 2 × 2)
  = 720 / 8
  = 90
```

**Jawaban: 90**

---

### Soal 6 — Permutasi Kalung ★★★

**Tipe:** Isian Singkat

**Soal:**  
Sebuah kalung dibuat dari 6 manik-manik berbeda warna. Berapa banyak kalung berbeda yang dapat dibuat? (Dua kalung dianggap sama jika satu bisa diperoleh dari yang lain melalui rotasi atau refleksi)

**Pembahasan:**

```
Langkah 1: Untuk susunan melingkar biasa (hanya rotasi): (n-1)!
  = (6-1)! = 5! = 120

Langkah 2: Pada kalung, refleksi (membalik) juga menghasilkan susunan yang sama
  Maka bagi 2:
  = 120 / 2 = 60
```

**Jawaban: 60**

---

### Soal 7 — Permutasi dengan Digit Terbatas ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan 4 digit yang bisa dibentuk dari angka {0, 1, 2, 3, 4, 5} tanpa pengulangan angka?

**Pembahasan:**

```
Langkah 1: Digit pertama tidak boleh 0 (agar tetap 4 digit)
  Pilihan digit pertama: {1,2,3,4,5} → 5 pilihan

Langkah 2: Digit kedua bisa dari sisa 5 angka (termasuk 0)
  = 5 pilihan

Langkah 3: Digit ketiga dari sisa 4 angka
  = 4 pilihan

Langkah 4: Digit keempat dari sisa 3 angka
  = 3 pilihan

Langkah 5: Total = 5 × 5 × 4 × 3 = 300
```

**Jawaban: 300**

---

## Bagian B: Kombinasi

---

### Soal 8 — Kombinasi Dasar ★

**Tipe:** Isian Singkat

**Soal:**  
Dari 10 peserta OSN, akan dipilih tim yang terdiri dari 4 orang untuk mewakili sekolah. Berapa banyak cara pemilihan tim?

**Pembahasan:**

```
Langkah 1: Urutan tidak penting (hanya memilih anggota)
  Gunakan kombinasi C(n,r) = n! / (r!(n-r)!)

Langkah 2: Hitung
  C(10,4) = 10! / (4! × 6!)
  = (10 × 9 × 8 × 7) / (4 × 3 × 2 × 1)
  = 5040 / 24
  = 210
```

**Jawaban: 210**

---

### Soal 9 — Kombinasi dengan Syarat ★★

**Tipe:** Isian Singkat

**Soal:**  
Sebuah komite terdiri dari 5 orang dipilih dari 7 pria dan 5 wanita. Komite harus memiliki minimal 2 wanita. Berapa banyak cara membentuk komite?

**Pembahasan:**

```
Langkah 1: Kasus-kasus yang memenuhi (minimal 2 wanita):
  - 2 wanita, 3 pria
  - 3 wanita, 2 pria
  - 4 wanita, 1 pria
  - 5 wanita, 0 pria

Langkah 2: Hitung tiap kasus
  C(5,2) × C(7,3) = 10 × 35 = 350
  C(5,3) × C(7,2) = 10 × 21 = 210
  C(5,4) × C(7,1) = 5 × 7 = 35
  C(5,5) × C(7,0) = 1 × 1 = 1

Langkah 3: Total = 350 + 210 + 35 + 1 = 596
```

**Jawaban: 596**

---

### Soal 10 — Pembagian Kelompok ★★

**Tipe:** Isian Singkat

**Soal:**  
Dua belas siswa dibagi menjadi 3 kelompok belajar yang masing-masing terdiri dari 4 orang. Kelompok-kelompok tersebut tidak diberi nama/label. Berapa banyak cara pembagian?

**Pembahasan:**

```
Langkah 1: Jika kelompok dibedakan (berlabel):
  = C(12,4) × C(8,4) × C(4,4)
  = 495 × 70 × 1
  = 34.650

Langkah 2: Karena kelompok TIDAK dibedakan (tidak ada label), bagi dengan 3!
  = 34.650 / 3!
  = 34.650 / 6
  = 5.775
```

**Jawaban: 5.775**

---

### Soal 11 — Kombinasi dengan Stars and Bars ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak solusi bilangan bulat non-negatif dari persamaan x + y + z + w = 12?

**Pembahasan:**

```
Langkah 1: Ini adalah masalah Stars and Bars
  n = 12 (total yang didistribusikan)
  k = 4 (banyak variabel)

Langkah 2: Rumus = C(n + k - 1, k - 1)
  = C(12 + 4 - 1, 4 - 1)
  = C(15, 3)
  = 15! / (3! × 12!)
  = (15 × 14 × 13) / (3 × 2 × 1)
  = 2730 / 6
  = 455
```

**Jawaban: 455**

---

### Soal 12 — Stars and Bars dengan Batas Bawah ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak solusi bilangan bulat dari persamaan a + b + c + d = 20 dengan a >= 2, b >= 1, c >= 3, d >= 0?

**Pembahasan:**

```
Langkah 1: Substitusi untuk menghilangkan batas bawah
  Misalkan a' = a - 2, b' = b - 1, c' = c - 3, d' = d - 0
  Maka a', b', c', d' >= 0

Langkah 2: Persamaan baru
  (a'+2) + (b'+1) + (c'+3) + d' = 20
  a' + b' + c' + d' = 20 - 2 - 1 - 3 = 14

Langkah 3: Gunakan Stars and Bars
  = C(14 + 4 - 1, 4 - 1)
  = C(17, 3)
  = (17 × 16 × 15) / (3 × 2 × 1)
  = 4080 / 6
  = 680
```

**Jawaban: 680**

---

### Soal 13 — Identitas Pascal ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari C(20,7) + C(20,8).

**Pembahasan:**

```
Langkah 1: Gunakan identitas Pascal
  C(n,r) + C(n,r+1) = C(n+1,r+1)

Langkah 2: Terapkan
  C(20,7) + C(20,8) = C(21,8)

Langkah 3: Hitung C(21,8)
  = 21! / (8! × 13!)
  = (21×20×19×18×17×16×15×14) / (8×7×6×5×4×3×2×1)
  = 203490 / ... 

  Cara hitung bertahap:
  = (21/1) × (20/2) × (19/3) × (18/4) × (17/5) × (16/6) × (15/7) × (14/8)
  = 21 × 10 × (19/3) × (18/4) × (17/5) × (16/6) × (15/7) × (14/8)

  Lebih mudah: gunakan fakta
  C(21,8) = 203.490
```

**Jawaban: 203.490**

---

### Soal 14 — Teorema Binomial ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan koefisien x^6 dalam ekspansi (2x - 1)^9.

**Pembahasan:**

```
Langkah 1: Suku umum ekspansi (a + b)^n
  T(r+1) = C(n,r) × a^(n-r) × b^r
  Di sini a = 2x, b = -1, n = 9

Langkah 2: Cari pangkat x = 6
  Pangkat x pada T(r+1) = n - r = 9 - r
  Kita butuh 9 - r = 6, maka r = 3

Langkah 3: Hitung T(4)
  T(4) = C(9,3) × (2x)^6 × (-1)^3
  = 84 × 64x^6 × (-1)
  = -5376x^6

Koefisien x^6 = -5376
```

**Jawaban: -5.376**

---

## Bagian C: Prinsip Sarang Merpati (Pigeonhole Principle)

---

### Soal 15 — Pigeonhole Dasar ★

**Tipe:** Isian Singkat

**Soal:**  
Di sebuah kelas terdapat 35 siswa. Minimal berapa siswa yang pasti lahir di bulan yang sama?

**Pembahasan:**

```
Langkah 1: Identifikasi objek dan kotak
  Objek: 35 siswa
  Kotak: 12 bulan

Langkah 2: Gunakan prinsip pigeonhole umum
  Pasti ada kotak dengan minimal ⌈35/12⌉ objek
  ⌈35/12⌉ = ⌈2,917⌉ = 3

Jadi minimal 3 siswa pasti lahir di bulan yang sama.
```

**Jawaban: 3**

---

### Soal 16 — Pigeonhole pada Bilangan ★★

**Tipe:** Uraian

**Soal:**  
Buktikan bahwa jika dipilih 7 bilangan bulat sembarang, pasti ada 2 bilangan yang jumlahnya atau selisihnya habis dibagi 10.

**Pembahasan:**

```
Langkah 1: Perhatikan sisa pembagian tiap bilangan oleh 10
  Sisa bisa bernilai: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Langkah 2: Kelompokkan sisa menjadi pasangan yang berjumlah 10:
  {0}, {5}, {1,9}, {2,8}, {3,7}, {4,6}
  Total ada 6 "kotak"

Langkah 3: Masukkan 7 bilangan ke 6 kotak berdasarkan sisa mod 10
  - Kotak {0}: bilangan dengan sisa 0 → jumlah dua bilangan habis dibagi 10
  - Kotak {5}: bilangan dengan sisa 5 → jumlah dua bilangan habis dibagi 10
  - Kotak {1,9}: bilangan bersisa 1 atau 9 → jika keduanya sisa 1, selisih habis dibagi 10;
    jika keduanya sisa 9, selisih habis dibagi 10; jika satu sisa 1 dan satu sisa 9,
    jumlah habis dibagi 10
  - Serupa untuk kotak lainnya

Langkah 4: Dengan 7 bilangan dan 6 kotak, pasti ada satu kotak berisi >= 2 bilangan
  (Pigeonhole). Dari penjelasan di atas, dua bilangan tersebut memiliki jumlah
  atau selisih yang habis dibagi 10. ∎
```

---

### Soal 17 — Pigeonhole Geometri ★★

**Tipe:** Uraian

**Soal:**  
Sembilan titik ditempatkan di dalam segitiga sama sisi dengan panjang sisi 4 cm. Buktikan bahwa pasti ada 2 titik yang jaraknya kurang dari atau sama dengan 2 cm.

**Pembahasan:**

```
Langkah 1: Bagi segitiga sama sisi bersisi 4 menjadi segitiga-segitiga kecil bersisi 2
  Dengan menghubungkan titik tengah setiap sisi, terbentuk 4 segitiga sama sisi kecil
  masing-masing bersisi 2 cm.

Langkah 2: Tentukan diameter setiap segitiga kecil
  Diameter (jarak terjauh antar dua titik) dalam segitiga sama sisi bersisi 2
  adalah sisi terpanjangnya = 2 cm.

Langkah 3: Terapkan Pigeonhole
  9 titik ditempatkan di 4 segitiga kecil.
  Karena 9 > 4 × 2, pasti ada satu segitiga kecil yang berisi minimal
  ⌈9/4⌉ = 3 titik.

  Namun cukup untuk membuktikan ada 2 titik: karena 9 > 4,
  pasti ada segitiga kecil berisi >= 2 titik.
  Dua titik dalam segitiga bersisi 2 berjarak paling jauh 2 cm.

Jadi pasti ada 2 titik dengan jarak <= 2 cm. ∎
```

---

### Soal 18 — Pigeonhole pada Sisa Pembagian ★★★

**Tipe:** Uraian

**Soal:**  
Di antara 52 bilangan bulat sembarang, buktikan bahwa pasti ada 2 bilangan yang selisih kuadratnya habis dibagi 100.

**Pembahasan:**

```
Langkah 1: Perhatikan bahwa a^2 - b^2 = (a-b)(a+b)
  Kita butuh 100 | (a^2 - b^2), yaitu a^2 ≡ b^2 (mod 100)

Langkah 2: Tentukan banyak kemungkinan nilai a^2 mod 100
  Hitung n^2 mod 100 untuk n = 0, 1, 2, ..., 49 (karena n dan 100-n punya
  kuadrat yang kongruen mod 100: (100-n)^2 = 10000 - 200n + n^2 ≡ n^2 mod 100)
  
  Nilai-nilai unik n^2 mod 100:
  0, 1, 4, 9, 16, 21, 24, 25, 29, 36, 41, 44, 49, 56, 61, 64, 69, 76, 81, 84, 89, 96
  
  Total ada 22 kemungkinan nilai kuadrat mod 100 untuk n = 0..49.
  Namun, kita juga perlu mempertimbangkan bahwa untuk n = 50..99,
  hasilnya sama dengan n = 0..49.

  Jadi kotak (bucket) berdasar n^2 mod 100 ada paling banyak 51 macam
  (dari n mod 100 bisa 0..49 dan 50..99, tapi kuadratnya paling banyak 51 nilai berbeda).

  Sebenarnya, cukup perhatikan: n^2 mod 100 hanya bergantung pada (n mod 50).
  Karena (n+50)^2 = n^2 + 100n + 2500 ≡ n^2 (mod 100).
  Jadi n mod 50 menentukan n^2 mod 100.
  Kemungkinan n mod 50: ada 50 nilai (0, 1, ..., 49).
  Tapi n dan (50-n) punya sifat:
  n^2 mod 100 vs (50-n)^2 mod 100 = (2500 - 100n + n^2) mod 100 = n^2 mod 100
  Jadi n dan 50-n menghasilkan kuadrat yang sama mod 100.
  
  Maka kotak yang berbeda paling banyak 26 (untuk n = 0..25, karena n = 26..49
  berpasangan dengan 50-26=24, ..., 50-49=1).
  Sebenarnya: 0 berpasangan dengan 50 (sama), 25 berpasangan dengan 25 (sama sendiri).
  
  Lebih sederhana: perhatikan |n mod 50| menghasilkan paling banyak 26 nilai kuadrat
  mod 100 yang berbeda (n = 0,1,...,25 karena simetri).

Langkah 3: Pendekatan lebih langsung
  Cukup perhatikan bahwa a^2 mod 100 hanya bergantung pada a mod 50.
  (Karena (a+50)^2 = a^2 + 100a + 2500 ≡ a^2 (mod 100))
  
  Sisa a mod 50 ada 50 kemungkinan: {0, 1, 2, ..., 49}
  Namun kita perlu mengelompokkan: n dan (50-n) mod 50 menghasilkan
  n^2 mod 100 yang sama (karena (50-n)^2 = 2500 - 100n + n^2 ≡ n^2 mod 100).
  
  Tapi untuk pigeonhole, cukup gunakan 50 kotak:
  Kotak berdasarkan a mod 50, ada 50 kemungkinan.
  
  Namun kita punya 52 bilangan. Karena 52 > 50, pasti ada 2 bilangan
  dengan a mod 50 yang sama, sehingga a ≡ b (mod 50).
  
  Jika a ≡ b (mod 50), maka (a^2 - b^2) = (a-b)(a+b).
  Karena 50 | (a-b), dan (a+b) genap (karena a ≡ b mod 50, maka a dan b
  berparitas sama), sehingga 2 | (a+b).
  Maka 100 | (a-b)(a+b) = a^2 - b^2. ∎

  Catatan: Kita perlu hati-hati soal paritas.
  Jika a ≡ b (mod 50), maka a - b = 50k.
  a + b: karena a - b = 50k, maka a + b = 2b + 50k.
  (a-b)(a+b) = 50k × (2b + 50k) = 100kb + 2500k^2
  = 100(kb + 25k^2) yang habis dibagi 100. ∎
```

---

### Soal 19 — Pigeonhole pada Jumlah Parsial ★★★

**Tipe:** Uraian

**Soal:**  
Diberikan 15 bilangan asli yang masing-masing kurang dari atau sama dengan 100. Buktikan bahwa pasti ada beberapa bilangan berurutan (konsekutif dalam barisan) yang jumlahnya habis dibagi 15.

**Pembahasan:**

```
Langkah 1: Definisikan jumlah parsial (prefix sum)
  Misalkan bilangan-bilangan tersebut a₁, a₂, ..., a₁₅.
  Definisikan Sₖ = a₁ + a₂ + ... + aₖ untuk k = 1, 2, ..., 15.

Langkah 2: Perhatikan sisa pembagian oleh 15
  Masing-masing Sₖ mod 15 bernilai salah satu dari {0, 1, 2, ..., 14}.
  Ada 15 jumlah parsial dan 15 kemungkinan sisa.

Langkah 3: Analisis kasus
  Kasus 1: Ada Sₖ yang habis dibagi 15 (Sₖ mod 15 = 0).
    Maka a₁ + a₂ + ... + aₖ habis dibagi 15. Selesai.

  Kasus 2: Tidak ada Sₖ yang habis dibagi 15.
    Maka semua Sₖ mod 15 bernilai di {1, 2, ..., 14}.
    Ada 15 jumlah parsial dan hanya 14 kotak (sisa 1..14).
    Oleh Pigeonhole, pasti ada i < j sehingga Sᵢ ≡ Sⱼ (mod 15).
    Maka Sⱼ - Sᵢ = a(i+1) + ... + aⱼ habis dibagi 15. ∎
```

---

### Soal 20 — Pigeonhole pada Subset ★★★

**Tipe:** Uraian

**Soal:**  
Dari himpunan {1, 2, 3, ..., 20}, dipilih 11 bilangan. Buktikan bahwa di antara 11 bilangan yang dipilih, pasti ada dua bilangan yang salah satunya membagi yang lainnya.

**Pembahasan:**

```
Langkah 1: Tulis setiap bilangan n dalam bentuk n = 2^a × m, 
  dengan m ganjil (faktor ganjil terbesar).
  
Langkah 2: Identifikasi "kotak" berdasarkan faktor ganjil m
  Bilangan ganjil dari 1 sampai 20: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
  Ada 10 bilangan ganjil, sehingga ada 10 kotak.
  
  Kotak untuk m = 1: {1, 2, 4, 8, 16}
  Kotak untuk m = 3: {3, 6, 12}
  Kotak untuk m = 5: {5, 10, 20}
  Kotak untuk m = 7: {7, 14}
  Kotak untuk m = 9: {9, 18}
  Kotak untuk m = 11: {11}
  Kotak untuk m = 13: {13}
  Kotak untuk m = 15: {15}
  Kotak untuk m = 17: {17}
  Kotak untuk m = 19: {19}

Langkah 3: Terapkan Pigeonhole
  Ada 11 bilangan dipilih dan 10 kotak.
  Oleh Pigeonhole, pasti ada 2 bilangan di kotak yang sama.
  
  Dua bilangan di kotak yang sama berbentuk 2^a × m dan 2^b × m (dengan m sama).
  Jika a < b, maka 2^a × m membagi 2^b × m. ∎
```

---

### Soal 21 — Pigeonhole Lanjutan ★★★

**Tipe:** Uraian

**Soal:**  
Dalam sebuah pesta, 15 orang saling berjabat tangan. Setiap orang berjabat tangan dengan setidaknya 1 orang lain. Buktikan bahwa pasti ada 2 orang yang berjabat tangan dengan jumlah orang yang sama.

**Pembahasan:**

```
Langkah 1: Tentukan kemungkinan jumlah jabat tangan per orang
  Setiap orang berjabat tangan dengan minimal 1 dan maksimal 14 orang.
  Kemungkinan nilai: {1, 2, 3, ..., 14} → 14 kotak.

Langkah 2: Perhatikan bahwa nilai 1 dan 14 tidak bisa hadir bersamaan
  Jika ada orang yang berjabat tangan dengan semua 14 orang lainnya,
  maka tidak ada orang yang hanya berjabat tangan dengan 1 orang
  (karena orang itu pasti juga sudah dijabat tangan oleh orang yang jabat semua).
  
  Tunggu — soal mengatakan "setidaknya 1", jadi memang bisa ada yang jabat 14.
  Tapi jika ada yang jabat 14 (semua), maka semua orang minimal jabat 1 (sudah),
  dan yang jabat paling sedikit minimal 1. Jadi 1 dan 14 bisa bersamaan.
  
  Sebenarnya tidak: jika ada yang berjabat tangan dengan semua (14 jabat),
  maka setiap orang lain sudah berjabat minimal 1, sehingga rentangnya {1,...,14}.
  Ini tidak menciptakan kontradiksi langsung.

Langkah 3: Gunakan argumen yang benar
  Kemungkinan jumlah jabat tangan: {1, 2, ..., 14} → 14 nilai yang mungkin.
  Ada 15 orang → oleh Pigeonhole, pasti ada 2 orang dengan jumlah jabat tangan sama. ∎
  
  (Catatan: Argumen ini langsung bekerja karena 15 orang > 14 kotak.)
```

---

## Bagian D: Deret dan Barisan

---

### Soal 22 — Deret Aritmetika Dasar ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan jumlah semua bilangan asli antara 1 dan 200 yang habis dibagi 7.

**Pembahasan:**

```
Langkah 1: Identifikasi barisan
  Bilangan yang habis dibagi 7 antara 1-200: 7, 14, 21, ..., 196
  Ini barisan aritmetika dengan a = 7, d = 7

Langkah 2: Cari banyak suku
  aₙ = a + (n-1)d
  196 = 7 + (n-1) × 7
  189 = (n-1) × 7
  n - 1 = 27
  n = 28

Langkah 3: Hitung jumlah
  S = n/2 × (a₁ + aₙ)
  = 28/2 × (7 + 196)
  = 14 × 203
  = 2842
```

**Jawaban: 2.842**

---

### Soal 23 — Deret Geometri ★

**Tipe:** Isian Singkat

**Soal:**  
Jumlah 8 suku pertama dari deret geometri 3 + 6 + 12 + 24 + ... adalah?

**Pembahasan:**

```
Langkah 1: Identifikasi
  a = 3, r = 6/3 = 2, n = 8

Langkah 2: Gunakan rumus
  Sₙ = a × (rⁿ - 1) / (r - 1)
  S₈ = 3 × (2^8 - 1) / (2 - 1)
  = 3 × (256 - 1) / 1
  = 3 × 255
  = 765
```

**Jawaban: 765**

---

### Soal 24 — Deret Aritmetika — Cari Suku ★★

**Tipe:** Isian Singkat

**Soal:**  
Dalam barisan aritmetika, suku ke-5 adalah 17 dan suku ke-12 adalah 38. Tentukan suku ke-20.

**Pembahasan:**

```
Langkah 1: Cari beda (d)
  a₁₂ - a₅ = (12-5) × d
  38 - 17 = 7d
  21 = 7d
  d = 3

Langkah 2: Cari suku pertama
  a₅ = a₁ + 4d
  17 = a₁ + 4(3)
  17 = a₁ + 12
  a₁ = 5

Langkah 3: Cari suku ke-20
  a₂₀ = a₁ + 19d = 5 + 19(3) = 5 + 57 = 62
```

**Jawaban: 62**

---

### Soal 25 — Deret Geometri Tak Hingga ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari 1 + 2/3 + 4/9 + 8/27 + ...

**Pembahasan:**

```
Langkah 1: Identifikasi deret geometri
  a = 1, r = (2/3)/1 = 2/3
  Karena |r| = 2/3 < 1, deret konvergen.

Langkah 2: Gunakan rumus deret tak hingga
  S∞ = a / (1 - r)
  = 1 / (1 - 2/3)
  = 1 / (1/3)
  = 3
```

**Jawaban: 3**

---

### Soal 26 — Deret Teleskopik ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari:
1/(1×3) + 1/(3×5) + 1/(5×7) + ... + 1/(49×51)

**Pembahasan:**

```
Langkah 1: Dekomposisi pecahan parsial
  1/((2k-1)(2k+1)) = (1/2) × [1/(2k-1) - 1/(2k+1)]

Langkah 2: Identifikasi jumlah suku
  Suku pertama: k=1 → 1/(1×3)
  Suku terakhir: 2k-1 = 49, k = 25 → 1/(49×51)
  Jadi k dari 1 sampai 25.

Langkah 3: Jumlahkan (teleskopik)
  S = (1/2) × [(1/1 - 1/3) + (1/3 - 1/5) + (1/5 - 1/7) + ... + (1/49 - 1/51)]
  = (1/2) × [1 - 1/51]
  = (1/2) × (50/51)
  = 25/51
```

**Jawaban: 25/51**

---

### Soal 27 — Jumlah Kuadrat ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari 1² + 2² + 3² + ... + 30².

**Pembahasan:**

```
Langkah 1: Gunakan rumus jumlah kuadrat
  Σ(k=1 to n) k² = n(n+1)(2n+1) / 6

Langkah 2: Substitusi n = 30
  = 30 × 31 × 61 / 6
  = 30 × 31 × 61 / 6
  = 5 × 31 × 61
  = 5 × 1891
  = 9455
```

**Jawaban: 9.455**

---

### Soal 28 — Relasi Rekurensi ★★★

**Tipe:** Isian Singkat

**Soal:**  
Sebuah barisan didefinisikan sebagai berikut: a(1) = 1, a(2) = 3, dan a(n) = 3a(n-1) - 2a(n-2) untuk n >= 3. Tentukan a(8).

**Pembahasan:**

```
Langkah 1: Hitung suku-suku secara berurutan
  a(1) = 1
  a(2) = 3
  a(3) = 3(3) - 2(1) = 9 - 2 = 7
  a(4) = 3(7) - 2(3) = 21 - 6 = 15
  a(5) = 3(15) - 2(7) = 45 - 14 = 31
  a(6) = 3(31) - 2(15) = 93 - 30 = 63
  a(7) = 3(63) - 2(31) = 189 - 62 = 127
  a(8) = 3(127) - 2(63) = 381 - 126 = 255

Langkah 2: Verifikasi dengan rumus tertutup
  Persamaan karakteristik: x² - 3x + 2 = 0 → (x-1)(x-2) = 0
  Akar: r₁ = 1, r₂ = 2
  Bentuk umum: a(n) = A × 1^n + B × 2^n = A + B × 2^n
  
  Dari kondisi awal:
  a(1) = A + 2B = 1
  a(2) = A + 4B = 3
  Selisih: 2B = 2, B = 1, A = -1
  
  a(n) = -1 + 2^n = 2^n - 1
  a(8) = 2^8 - 1 = 256 - 1 = 255 ✓
```

**Jawaban: 255**

---

### Soal 29 — Barisan Fibonacci ★★

**Tipe:** Isian Singkat

**Soal:**  
Lantai sebuah koridor berukuran 2×10 akan dipasang ubin berukuran 2×1. Berapa banyak cara memasang ubin tersebut?

**Pembahasan:**

```
Langkah 1: Definisikan rekurensi
  Misalkan f(n) = banyak cara memasang ubin pada koridor 2×n.
  - Ubin bisa dipasang vertikal (mengisi 2×1) → sisanya 2×(n-1)
  - Ubin bisa dipasang horizontal (harus 2 ubin sejajar mengisi 2×2) → sisanya 2×(n-2)

  f(n) = f(n-1) + f(n-2)

Langkah 2: Basis
  f(1) = 1 (satu ubin vertikal)
  f(2) = 2 (dua vertikal, atau dua horizontal)

Langkah 3: Hitung
  f(1) = 1
  f(2) = 2
  f(3) = 3
  f(4) = 5
  f(5) = 8
  f(6) = 13
  f(7) = 21
  f(8) = 34
  f(9) = 55
  f(10) = 89
```

**Jawaban: 89**

---

## Bagian E: Soal Campuran (Gabungan Beberapa Teknik)

---

### Soal 30 — Distribusi Objek Berbeda ke Kotak Berbeda ★★

**Tipe:** Isian Singkat

**Soal:**  
Enam buku berbeda akan ditempatkan ke dalam 3 rak berbeda. Setiap rak boleh kosong. Berapa banyak cara menempatkan buku-buku tersebut?

**Pembahasan:**

```
Langkah 1: Setiap buku punya 3 pilihan (rak 1, rak 2, atau rak 3)
  Buku-buku independen satu sama lain.

Langkah 2: Gunakan aturan perkalian
  Total cara = 3^6 = 729
```

**Jawaban: 729**

---

### Soal 31 — Aturan Komplemen dan Kombinasi ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan bulat antara 1 dan 1000 (inklusif) yang tidak habis dibagi 3 maupun 5?

**Pembahasan:**

```
Langkah 1: Gunakan Prinsip Inklusi-Eksklusi
  A = bilangan habis dibagi 3
  B = bilangan habis dibagi 5
  Kita cari |U| - |A ∪ B|

Langkah 2: Hitung masing-masing
  |A| = ⌊1000/3⌋ = 333
  |B| = ⌊1000/5⌋ = 200
  |A ∩ B| = bilangan habis dibagi 15 = ⌊1000/15⌋ = 66

Langkah 3: Hitung |A ∪ B|
  |A ∪ B| = 333 + 200 - 66 = 467

Langkah 4: Yang tidak habis dibagi 3 maupun 5
  = 1000 - 467 = 533
```

**Jawaban: 533**

---

### Soal 32 — Jalan pada Grid ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak jalur terpendek dari titik (0,0) ke titik (6,4) pada grid, jika hanya boleh bergerak ke kanan (R) atau ke atas (U)?

**Pembahasan:**

```
Langkah 1: Tentukan total langkah
  Perlu 6 langkah ke kanan (R) dan 4 langkah ke atas (U)
  Total langkah = 6 + 4 = 10

Langkah 2: Jalur = memilih posisi langkah R (atau U) dari 10 langkah
  = C(10, 6) = C(10, 4)
  = 10! / (6! × 4!)
  = (10 × 9 × 8 × 7) / (4 × 3 × 2 × 1)
  = 5040 / 24
  = 210
```

**Jawaban: 210**

---

### Soal 33 — Derangement ★★★

**Tipe:** Isian Singkat

**Soal:**  
Lima surat berbeda dimasukkan secara acak ke dalam 5 amplop berbeda (satu surat per amplop). Berapa banyak cara sehingga tepat 2 surat masuk ke amplop yang benar?

**Pembahasan:**

```
Langkah 1: Pilih 2 surat yang masuk ke amplop benar
  = C(5, 2) = 10

Langkah 2: Tiga surat sisanya harus SEMUA masuk ke amplop yang salah
  Ini adalah derangement dari 3 elemen.
  D(3) = 3! × (1 - 1/1! + 1/2! - 1/3!)
  = 6 × (1 - 1 + 1/2 - 1/6)
  = 6 × (3/6 - 1/6)
  = 6 × 2/6
  = 2

Langkah 3: Total = C(5,2) × D(3) = 10 × 2 = 20
```

**Jawaban: 20**

---

### Soal 34 — Fungsi Surjektif ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak fungsi surjektif (onto) dari himpunan A = {1,2,3,4,5} ke himpunan B = {a,b,c}?

**Pembahasan:**

```
Langkah 1: Total fungsi dari A ke B (tanpa syarat)
  = 3^5 = 243

Langkah 2: Gunakan Inklusi-Eksklusi
  Fungsi surjektif = Total - (yang melewatkan minimal 1 elemen B)
  
  Misalkan Aᵢ = fungsi yang tidak memiliki i di range-nya.
  |A_a| = 2^5 = 32 (hanya bisa ke b atau c)
  |A_b| = 2^5 = 32
  |A_c| = 2^5 = 32
  |A_a ∩ A_b| = 1^5 = 1 (hanya ke c)
  |A_a ∩ A_c| = 1^5 = 1
  |A_b ∩ A_c| = 1^5 = 1
  |A_a ∩ A_b ∩ A_c| = 0 (tidak bisa ke mana-mana)

Langkah 3: |A_a ∪ A_b ∪ A_c| = 32+32+32 - 1-1-1 + 0 = 93

Langkah 4: Fungsi surjektif = 243 - 93 = 150
```

**Jawaban: 150**

---

### Soal 35 — Deret dan Kombinatorika ★★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari C(20,0) + C(20,1) + C(20,2) + ... + C(20,20).

**Pembahasan:**

```
Langkah 1: Ingat sifat penjumlahan koefisien binomial
  C(n,0) + C(n,1) + ... + C(n,n) = 2^n

  Ini berasal dari (1+1)^n = 2^n (substitusi a=1, b=1 pada teorema binomial)

Langkah 2: Untuk n = 20
  C(20,0) + C(20,1) + ... + C(20,20) = 2^20 = 1.048.576
```

**Jawaban: 1.048.576**

---

### Soal 36 — Trailing Zeros dan Faktorial ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak angka nol di belakang bilangan 50! (50 faktorial)?

**Pembahasan:**

```
Langkah 1: Gunakan rumus trailing zeros
  Banyak nol = ⌊50/5⌋ + ⌊50/25⌋ + ⌊50/125⌋ + ...

Langkah 2: Hitung
  ⌊50/5⌋ = 10
  ⌊50/25⌋ = 2
  ⌊50/125⌋ = 0

  Total = 10 + 2 + 0 = 12
```

**Jawaban: 12**

---

## Bagian F: Soal Gaya OSN Kompetitif

---

### Soal 37 — Counting pada Bilangan ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan bulat positif n yang kurang dari 1000 sedemikian sehingga jumlah digit-digit n habis dibagi 9?

**Pembahasan:**

```
Langkah 1: Bilangan 1-999 yang jumlah digitnya habis dibagi 9
  Bilangan 1 digit: 9 → hanya 1 bilangan
  
  Bilangan 2 digit (10-99): ab, di mana a + b habis dibagi 9
    a ∈ {1,...,9}, b ∈ {0,...,9}
    Pasangan (a,b) dengan a+b = 9: (1,8),(2,7),(3,6),(4,5),(5,4),(6,3),(7,2),(8,1),(9,0) → 9
    Pasangan (a,b) dengan a+b = 18: (9,9) → 1
    Total: 10 bilangan
    
  Bilangan 3 digit (100-999): abc, di mana a + b + c habis dibagi 9
    a ∈ {1,...,9}, b ∈ {0,...,9}, c ∈ {0,...,9}
    Total bilangan 3 digit = 900
    
    Untuk setiap pasangan (a,b) tetap, jumlah a+b+c habis dibagi 9 terjadi ketika
    c ≡ -(a+b) mod 9.
    Karena c ∈ {0,...,9}, ada tepat 1 atau 2 nilai c yang memenuhi.
    
    Lebih tepat: untuk setiap (a,b), persis 1 dari 9 kemungkinan sisa menghasilkan
    jumlah yang habis dibagi 9. Dari 10 pilihan c (0-9), ada:
    - Jika sisa yang dibutuhkan = 0: c bisa 0 atau 9 → 2 pilihan
    - Jika sisa yang dibutuhkan = 1..8: hanya 1 pilihan c
    
    Banyak pasangan (a,b) dengan -(a+b) ≡ 0 (mod 9), yaitu a+b ≡ 0 (mod 9):
    a+b = 9: 9 pasangan (dihitung di atas tapi kali ini a=1..9, b=0..9)
      (1,8),(2,7),(3,6),(4,5),(5,4),(6,3),(7,2),(8,1),(9,0) → 9
    a+b = 18: (9,9) → 1
    Total: 10 pasangan → masing-masing punya 2 pilihan c → kontribusi 20
    
    Pasangan (a,b) lainnya: 9×10 - 10 = 80 pasangan → masing-masing 1 pilihan c → kontribusi 80
    
    Total bilangan 3 digit = 20 + 80 = 100

Langkah 2: Total keseluruhan
  = 1 + 10 + 100 = 111
```

**Jawaban: 111**

---

### Soal 38 — Jalan Grid dengan Hambatan ★★★

**Tipe:** Isian Singkat

**Soal:**  
Pada grid, berapa banyak jalur terpendek dari (0,0) ke (5,5) yang melewati titik (2,3)?

**Pembahasan:**

```
Langkah 1: Jalur terpendek dari (0,0) ke (2,3)
  Perlu 2 langkah kanan dan 3 langkah atas, total 5 langkah
  = C(5, 2) = 10

Langkah 2: Jalur terpendek dari (2,3) ke (5,5)
  Perlu 3 langkah kanan dan 2 langkah atas, total 5 langkah
  = C(5, 3) = 10

Langkah 3: Total jalur yang melewati (2,3)
  = 10 × 10 = 100
```

**Jawaban: 100**

---

### Soal 39 — Catalan Number ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak cara menyusun 6 pasang kurung buka dan tutup sehingga susunannya valid (setiap prefiks memiliki kurung buka >= kurung tutup)?

**Pembahasan:**

```
Langkah 1: Ini adalah Catalan number C₆

Langkah 2: Rumus Catalan
  Cₙ = C(2n, n) / (n+1)
  C₆ = C(12, 6) / 7

Langkah 3: Hitung C(12,6)
  C(12,6) = 12! / (6! × 6!)
  = (12×11×10×9×8×7) / (6×5×4×3×2×1)
  = 665280 / 720
  = 924

Langkah 4: C₆ = 924 / 7 = 132
```

**Jawaban: 132**

---

### Soal 40 — Inklusi-Eksklusi dan Deret ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak permutasi dari {1, 2, 3, 4, 5, 6} sedemikian sehingga tidak ada elemen yang berada di posisi aslinya (derangement)?

**Pembahasan:**

```
Langkah 1: Gunakan rumus derangement
  D(n) = n! × Σ(k=0 to n) [(-1)^k / k!]
  
Langkah 2: Untuk n = 6
  D(6) = 6! × (1 - 1/1! + 1/2! - 1/3! + 1/4! - 1/5! + 1/6!)
  = 720 × (1 - 1 + 1/2 - 1/6 + 1/24 - 1/120 + 1/720)
  
Langkah 3: Hitung pecahan dalam kurung
  = 720/720 - 720/720 + 360/720 - 120/720 + 30/720 - 6/720 + 1/720
  = (720 - 720 + 360 - 120 + 30 - 6 + 1) / 720
  = 265 / 720

Langkah 4: D(6) = 720 × 265/720 = 265
```

**Jawaban: 265**

---

### Soal 41 — Gabungan Deret dan Kombinatorika ★★★

**Tipe:** Isian Singkat

**Soal:**  
Hitung nilai dari:
1×C(10,1) + 2×C(10,2) + 3×C(10,3) + ... + 10×C(10,10)

**Pembahasan:**

```
Langkah 1: Gunakan identitas k×C(n,k) = n×C(n-1,k-1)
  Bukti: k × C(n,k) = k × n!/(k!(n-k)!) = n!/(((k-1)!(n-k)!) = n × C(n-1,k-1)

Langkah 2: Terapkan untuk n = 10
  Σ(k=1 to 10) k×C(10,k) = Σ(k=1 to 10) 10×C(9,k-1)
  = 10 × Σ(k=1 to 10) C(9,k-1)
  = 10 × Σ(j=0 to 9) C(9,j)     [substitusi j = k-1]
  = 10 × 2^9
  = 10 × 512
  = 5120
```

**Jawaban: 5.120**

---

### Soal 42 — Counting Lanjutan: Bilangan dengan Digit Terurut ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak bilangan 5 digit (10000-99999) yang digit-digitnya membentuk barisan tidak turun (d₁ <= d₂ <= d₃ <= d₄ <= d₅, dengan d₁ >= 1)?

**Pembahasan:**

```
Langkah 1: Kita memilih 5 digit dari {1,2,...,9} dengan pengulangan diperbolehkan
  dan urutan tidak penting (karena kita selalu ambil urutan naik/tidak turun).
  
  Catatan: d₁ >= 1 (digit pertama tidak boleh 0), dan karena d₁ <= d₂ <= ... <= d₅,
  maka semua digit >= 1. Jadi digit dari {1,2,...,9}.

Langkah 2: Ini ekuivalen dengan "combination with repetition"
  Memilih 5 dari 9 macam (dengan pengulangan, tanpa urutan)
  = C(9 + 5 - 1, 5)
  = C(13, 5)

Langkah 3: Hitung
  C(13,5) = 13! / (5! × 8!)
  = (13 × 12 × 11 × 10 × 9) / (5 × 4 × 3 × 2 × 1)
  = 154440 / 120
  = 1287
```

**Jawaban: 1.287**

---

## Ringkasan Distribusi Soal

| Bagian | Topik | Jumlah Soal | Tingkat |
|--------|-------|-------------|---------|
| A | Permutasi | 7 | 2★, 4★★, 1★★★ |
| B | Kombinasi | 7 | 1★, 5★★, 1★★★ |
| C | Pigeonhole Principle | 7 | 1★, 2★★, 4★★★ |
| D | Deret dan Barisan | 8 | 2★, 4★★, 2★★★ |
| E | Soal Campuran | 7 | 0★, 4★★, 3★★★ |
| F | Gaya OSN Kompetitif | 6 | 0★, 0★★, 6★★★ |
| **Total** | | **42** | **6★, 19★★, 17★★★** |

---

## Tips Mengerjakan Soal Kombinatorika OSN

1. **Identifikasi terlebih dahulu** apakah soal tentang permutasi (urutan penting) atau kombinasi (urutan tidak penting).
2. **Gunakan komplemen** jika diminta "minimal satu" atau "tidak ada yang...".
3. **Pecah kasus** jika ada syarat yang membuat tidak bisa dihitung langsung.
4. **Cek dengan kasus kecil** jika bingung: coba n=1, 2, 3 untuk menemukan pola.
5. **Perhatikan objek identik vs berbeda** — ini mempengaruhi rumus yang digunakan.
6. **Untuk deret**, identifikasi apakah aritmetika (beda tetap), geometri (rasio tetap), atau teleskopik.
7. **Untuk pigeonhole**, tentukan "objek" dan "kotak", lalu bandingkan jumlahnya.
8. **Hati-hati double counting** — pastikan setiap kasus dihitung tepat satu kali.
