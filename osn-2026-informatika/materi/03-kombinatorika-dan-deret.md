# Materi 03 - Kombinatorika & Deret

## Daftar Isi
1. [Aturan Dasar Menghitung](#1-aturan-dasar-menghitung)
2. [Faktorial](#2-faktorial)
3. [Permutasi](#3-permutasi)
4. [Kombinasi](#4-kombinasi)
5. [Segitiga Pascal & Teorema Binomial](#5-segitiga-pascal--teorema-binomial)
6. [Prinsip Sarang Merpati (Pigeonhole Principle)](#6-prinsip-sarang-merpati-pigeonhole-principle)
7. [Stars and Bars (Kombinasi dengan Pengulangan)](#7-stars-and-bars-kombinasi-dengan-pengulangan)
8. [Prinsip Inklusi-Eksklusi dalam Kombinatorika](#8-prinsip-inklusi-eksklusi-dalam-kombinatorika)
9. [Double Counting & Bukti Bijektif](#9-double-counting--bukti-bijektif)
10. [Relasi Rekurensi](#10-relasi-rekurensi)
11. [Deret Aritmetika](#11-deret-aritmetika)
12. [Deret Geometri](#12-deret-geometri)
13. [Deret-Deret Penting Lainnya](#13-deret-deret-penting-lainnya)
14. [Contoh Soal & Pembahasan](#14-contoh-soal--pembahasan)
15. [Tips Mengerjakan Soal Kombinatorika OSN](#15-tips-mengerjakan-soal-kombinatorika-osn)
16. [Latihan](#16-latihan)

---

## 1. Aturan Dasar Menghitung

### 1.1 Aturan Penjumlahan (Sum Rule / Addition Principle)

Jika suatu tugas bisa dilakukan dengan cara A **ATAU** cara B, dan kedua cara tersebut **saling lepas** (tidak bisa terjadi bersamaan), maka:

```
Total cara = (banyak cara A) + (banyak cara B)
```

**Kata kunci:** "atau", "salah satu dari"

**Contoh Sederhana:**
Kamu bisa pergi ke sekolah naik sepeda (3 rute) ATAU naik bus (5 rute).
Total pilihan = 3 + 5 = **8 cara**

**Perluasan untuk k kejadian saling lepas:**
```
Total = n₁ + n₂ + n₃ + ... + nₖ
```

### 1.2 Aturan Perkalian (Product Rule / Multiplication Principle)

Jika suatu tugas terdiri dari langkah A **DAN** langkah B yang dilakukan berurutan, maka:

```
Total cara = (banyak cara A) x (banyak cara B)
```

**Kata kunci:** "dan", "kemudian", "lalu", "berturut-turut"

**Contoh Sederhana:**
Memilih baju (4 pilihan) DAN celana (3 pilihan).
Total outfit = 4 x 3 = **12 cara**

**Perluasan untuk k langkah berurutan:**
```
Total = n₁ x n₂ x n₃ x ... x nₖ
```

### 1.3 Aturan Komplemen

Kadang lebih mudah menghitung yang **tidak memenuhi** syarat, lalu kurangkan dari total.

```
Banyak yang memenuhi = Total - Banyak yang TIDAK memenuhi
```

**Contoh:** Berapa banyak bilangan 3 digit (100-999) yang memiliki minimal satu digit genap?
- Total bilangan 3 digit = 900
- Bilangan 3 digit yang SEMUA digitnya ganjil: digit pertama (1,3,5,7,9) = 5 pilihan, digit kedua & ketiga (1,3,5,7,9) = 5 pilihan masing-masing
- Semua ganjil = 5 x 5 x 5 = 125
- Minimal satu genap = 900 - 125 = **775**

### 1.4 Kapan Menggunakan Aturan yang Mana?

| Situasi | Aturan | Alasan |
|---------|--------|--------|
| Pilih A atau B | Penjumlahan | Dua opsi eksklusif |
| Lakukan A lalu B | Perkalian | Dua langkah berurutan |
| "Minimal satu" | Komplemen | Lebih mudah hitung yang tidak |
| Campuran | Gabungan | Pecah jadi sub-kasus |

---

## 2. Faktorial

### 2.1 Definisi

```
n! = n x (n-1) x (n-2) x ... x 2 x 1
```

Secara rekursif: `n! = n x (n-1)!`

**Definisi khusus:** `0! = 1` (ini adalah konvensi/definisi, bukan hasil perhitungan)

### 2.2 Nilai Faktorial yang Perlu Diingat

| n | n! |
|---|-----|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| 9 | 362880 |
| 10 | 3628800 |

### 2.3 Sifat Penting Faktorial

1. `n! = n x (n-1)!`
2. `n! / (n-k)! = n x (n-1) x ... x (n-k+1)` (perkalian k faktor)
3. `n! / k!` jika k < n, hasilnya perkalian dari (k+1) sampai n

### 2.4 Trailing Zeros (Banyak Nol di Belakang n!)

Banyak nol di belakang n! = banyaknya faktor 5 dalam n!

```
Trailing zeros(n!) = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...
```

**Contoh:** Berapa nol di belakang 100!?
```
⌊100/5⌋ + ⌊100/25⌋ + ⌊100/125⌋ = 20 + 4 + 0 = 24 nol
```

---

## 3. Permutasi

### 3.1 Permutasi Biasa

**Definisi:** Susunan terurut r objek yang diambil dari n objek berbeda.

```
P(n,r) = n! / (n-r)!
```

Khusus semua objek: `P(n,n) = n!`

**Cara berpikir:** Slot pertama ada n pilihan, slot kedua ada (n-1) pilihan, dst.

### 3.2 Permutasi dengan Objek Berulang (Identical)

Jika ada n objek di mana:
- Objek tipe 1 muncul n₁ kali
- Objek tipe 2 muncul n₂ kali
- ... dst

```
Banyak susunan = n! / (n₁! x n₂! x ... x nₖ!)
```

**Contoh:** Berapa banyak susunan huruf dari kata "MATEMATIKA"?
- Total huruf = 10
- M: 2, A: 3, T: 2, E: 1, I: 1, K: 1
- Susunan = 10! / (2! x 3! x 2! x 1! x 1! x 1!) = 3628800 / (2 x 6 x 2) = **151200**

### 3.3 Permutasi Siklis (Melingkar / Circular Permutation)

Jika n objek disusun dalam lingkaran (rotasi dianggap sama):

```
Permutasi siklis = (n-1)!
```

**Mengapa (n-1)! ?** Karena pada susunan melingkar, kita bisa "mematok" satu objek di satu posisi, lalu menyusun (n-1) objek sisanya.

**Contoh:** 5 orang duduk mengelilingi meja bundar. Berapa banyak susunan?
```
(5-1)! = 4! = 24 cara
```

**Permutasi siklis dengan gelang/kalung (refleksi dianggap sama):**
```
= (n-1)! / 2
```
Karena membalik kalung menghasilkan susunan yang sama.

### 3.4 Permutasi Multiset

Memilih r objek dari n tipe objek (boleh diulang), dengan urutan penting:

```
= n^r (n pangkat r)
```

**Contoh:** Berapa banyak string 4 digit yang terbentuk dari angka {0,1,2,...,9}?
(boleh pakai angka yang sama berulang)
```
= 10^4 = 10000
```
Catatan: Jika digit pertama tidak boleh 0, maka = 9 x 10^3 = 9000.

---

## 4. Kombinasi

### 4.1 Kombinasi Biasa

**Definisi:** Pemilihan r objek dari n objek berbeda, tanpa memperhatikan urutan.

```
C(n,r) = n! / (r! x (n-r)!)
```

Notasi lain: C(n,r) = (n choose r) = ₙCᵣ

### 4.2 Sifat-Sifat Kombinasi

| Sifat | Rumus | Penjelasan |
|-------|-------|------------|
| Simetri | C(n,r) = C(n, n-r) | Memilih r = tidak memilih n-r |
| Identitas Pascal | C(n,r) = C(n-1,r-1) + C(n-1,r) | Objek tertentu dipilih atau tidak |
| Jumlah baris | C(n,0) + C(n,1) + ... + C(n,n) = 2^n | Total subset dari n elemen |
| Batas | C(n,0) = C(n,n) = 1 | Memilih 0 atau semua: 1 cara |
| Vandermonde | C(m+n,r) = Σ C(m,k)C(n,r-k) | Membagi pilihan ke 2 kelompok |

### 4.3 Identitas Pascal - Penjelasan Intuitif

```
C(n,r) = C(n-1,r-1) + C(n-1,r)
```

**Interpretasi:** Bayangkan ada n orang dan kita ingin memilih tim r orang. Fokus pada satu orang khusus, misalnya "Andi":
- **Andi dipilih:** Maka kita perlu memilih r-1 orang lagi dari n-1 orang sisanya = C(n-1, r-1)
- **Andi tidak dipilih:** Maka kita memilih r orang dari n-1 orang sisanya = C(n-1, r)

Total = C(n-1, r-1) + C(n-1, r) = C(n, r) ✓

### 4.4 Kapan Permutasi vs Kombinasi?

| Pertanyaan | Jawaban | Rumus |
|-----------|---------|-------|
| "Berapa cara menyusun..." | Urutan penting → Permutasi | P(n,r) |
| "Berapa cara memilih..." | Urutan tidak penting → Kombinasi | C(n,r) |
| "Berapa banyak tim/kelompok..." | Kombinasi | C(n,r) |
| "Berapa banyak kata/password..." | Permutasi | P(n,r) atau n^r |

---

## 5. Segitiga Pascal & Teorema Binomial

### 5.1 Segitiga Pascal

```
Baris 0:                1
Baris 1:              1   1
Baris 2:            1   2   1
Baris 3:          1   3   3   1
Baris 4:        1   4   6   4   1
Baris 5:      1   5  10  10   5   1
Baris 6:    1   6  15  20  15   6   1
Baris 7:  1   7  21  35  35  21   7   1
```

**Entri pada baris n, kolom r = C(n,r)**

### 5.2 Pola-Pola dalam Segitiga Pascal

| Pola | Lokasi | Nilai |
|------|--------|-------|
| Semua 1 | Kolom 0 dan diagonal | C(n,0) = C(n,n) = 1 |
| Bilangan asli | Kolom 1 | C(n,1) = n |
| Bilangan segitiga | Kolom 2 | C(n,2) = n(n-1)/2 |
| Bilangan tetrahedral | Kolom 3 | C(n,3) = n(n-1)(n-2)/6 |
| Jumlah baris ke-n | Semua kolom | 2^n |
| Sifat simetri | Kolom r dan n-r | C(n,r) = C(n,n-r) |

**Jumlah diagonal:** Jika kita jumlahkan entri sepanjang diagonal "miring", kita mendapatkan barisan Fibonacci!
```
1, 1, 2, 3, 5, 8, 13, 21, ...
```

### 5.3 Teorema Binomial

```
(a + b)^n = Σ(k=0 to n) C(n,k) * a^(n-k) * b^k
```

Atau ditulis lengkap:
```
(a+b)^n = C(n,0)a^n + C(n,1)a^(n-1)b + C(n,2)a^(n-2)b^2 + ... + C(n,n)b^n
```

**Contoh ekspansi:**
```
(a+b)^0 = 1
(a+b)^1 = a + b
(a+b)^2 = a^2 + 2ab + b^2
(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4
```

### 5.4 Aplikasi Teorema Binomial

**Menentukan koefisien tertentu:**
Koefisien x^k dalam (1+x)^n = C(n,k)

**Substitusi khusus:**
- a=1, b=1: C(n,0) + C(n,1) + ... + C(n,n) = 2^n
- a=1, b=-1: C(n,0) - C(n,1) + C(n,2) - ... = 0
- Jadi: Jumlah C genap = Jumlah C ganjil = 2^(n-1)

### 5.5 Suku Umum Ekspansi Binomial

Suku ke-(r+1) dalam ekspansi (a+b)^n:
```
T(r+1) = C(n,r) * a^(n-r) * b^r
```

**Contoh:** Tentukan suku ke-4 dari (2x + 3)^6.
```
T(4) = C(6,3) * (2x)^3 * 3^3
     = 20 * 8x^3 * 27
     = 4320x^3
```

---

## 6. Prinsip Sarang Merpati (Pigeonhole Principle)

### 6.1 Bentuk Sederhana

> Jika **n** objek dimasukkan ke dalam **k** kotak dan n > k, maka **pasti ada minimal satu kotak yang berisi lebih dari satu objek**.

### 6.2 Bentuk Umum (Generalized Pigeonhole)

> Jika **n** objek dimasukkan ke dalam **k** kotak, maka ada minimal satu kotak yang berisi **paling sedikit ⌈n/k⌉** objek.

**Catatan:** ⌈x⌉ = ceiling (pembulatan ke atas)

### 6.3 Contoh Klasik

**Contoh 1 - Bulan Lahir:**
Di antara 13 orang, pasti ada minimal 2 yang lahir di bulan yang sama.
- Objek: 13 orang, kotak: 12 bulan
- 13 > 12, jadi pasti ada kotak (bulan) berisi ≥ 2 orang ✓

**Contoh 2 - Jabat Tangan:**
Dalam pesta 10 orang, pasti ada 2 orang dengan jumlah jabat tangan sama.
- Setiap orang bisa berjabat tangan 0-9 kali
- Tapi 0 dan 9 tidak bisa hadir bersamaan (jika ada yang jabat semua, tak ada yang jabat 0)
- Jadi hanya 9 kemungkinan nilai, tapi ada 10 orang → pasti ada 2 yang sama

**Contoh 3 - Bilangan:**
Dari 10 bilangan bulat sembarang, pasti ada subset (kelompok) yang jumlahnya habis dibagi 10.
- Hitung jumlah kumulatif: S₁, S₂, ..., S₁₀
- Ada 10 sisa bagi 10: {0,1,...,9}
- Jika ada Sᵢ habis dibagi 10, selesai
- Jika tidak, ada 10 jumlah kumulatif dengan 9 sisa → pasti 2 sisanya sama (Sᵢ dan Sⱼ)
- Maka Sⱼ - Sᵢ habis dibagi 10 (subset dari posisi i+1 sampai j)

### 6.4 Strategi Penerapan Pigeonhole

1. **Identifikasi "objek"** - apa yang ditempatkan?
2. **Identifikasi "kotak"** - ke mana objek bisa masuk?
3. **Bandingkan** - apakah objek > kotak?
4. **Simpulkan** - pasti ada kotak dengan ≥ 2 objek (atau ≥ ⌈n/k⌉)

---

## 7. Stars and Bars (Kombinasi dengan Pengulangan)

### 7.1 Masalah Dasar

**Pertanyaan:** Berapa banyak cara membagi n objek identik ke dalam k kelompok berbeda?

Equivalen: Berapa banyak solusi bilangan bulat non-negatif dari:
```
x₁ + x₂ + ... + xₖ = n    (xᵢ >= 0)
```

### 7.2 Rumus Stars and Bars

```
Banyak solusi = C(n + k - 1, k - 1) = C(n + k - 1, n)
```

**Cara berpikir:** Bayangkan n bintang (★) dan k-1 pemisah (|):
```
★★|★★★|★ artinya x₁=2, x₂=3, x₃=1
```
Kita menyusun n+k-1 simbol (n bintang dan k-1 pemisah), pilih posisi pemisah.

### 7.3 Variasi dengan Batas Bawah

Jika `xᵢ >= 1` (setiap kelompok minimal 1):
Substitusi yᵢ = xᵢ - 1, maka y₁ + y₂ + ... + yₖ = n - k (yᵢ >= 0)
```
Banyak solusi = C(n - 1, k - 1)
```

### 7.4 Contoh Penerapan

**Contoh:** Berapa cara membagi 10 permen identik ke 4 anak?
- n = 10, k = 4
- Jawab = C(10 + 4 - 1, 4 - 1) = C(13, 3) = 286 cara

**Contoh dengan batas bawah:** Setiap anak minimal dapat 1 permen?
- n = 10, k = 4, xᵢ >= 1
- Jawab = C(10 - 1, 4 - 1) = C(9, 3) = 84 cara

---

## 8. Prinsip Inklusi-Eksklusi dalam Kombinatorika

### 8.1 Rumus untuk 2 Himpunan

```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

### 8.2 Rumus untuk 3 Himpunan

```
|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
```

### 8.3 Rumus Umum

```
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)^(n+1)|A₁ ∩ ... ∩ Aₙ|
```

### 8.4 Aplikasi: Menghitung Derangement

**Derangement** = permutasi di mana TIDAK ADA elemen yang berada di posisi aslinya.

Notasi: D(n) = banyak derangement dari n elemen.

```
D(n) = n! * Σ(k=0 to n) [(-1)^k / k!]
     = n! * (1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!)
```

Nilai awal:
| n | D(n) |
|---|------|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 9 |
| 5 | 44 |
| 6 | 265 |

**Rumus rekursi:** D(n) = (n-1)(D(n-1) + D(n-2))

**Contoh:** 4 surat dimasukkan ke 4 amplop secara acak. Berapa kemungkinan TIDAK ADA surat yang masuk ke amplop yang benar?
```
D(4) = 4!(1 - 1 + 1/2 - 1/6 + 1/24) = 24(12/24 - 4/24 + 1/24) = 24 * 9/24 = 9
```

### 8.5 Aplikasi: Surjeksi (Onto Function)

Banyak fungsi surjektif dari himpunan n elemen ke himpunan k elemen:
```
S(n,k) = Σ(i=0 to k) [(-1)^i * C(k,i) * (k-i)^n]
```

---

## 9. Double Counting & Bukti Bijektif

### 9.1 Prinsip Double Counting

**Ide:** Hitung satu hal dengan dua cara berbeda. Kedua cara harus menghasilkan nilai yang sama.

**Contoh - Membuktikan Teorema Handshaking:**
Dalam graf G = (V, E), jumlah semua derajat = 2|E|.

**Bukti:** Hitung jumlah pasangan (v, e) di mana v adalah ujung dari e.
- Cara 1: Untuk setiap sisi e, ada 2 ujung. Total = 2|E|.
- Cara 2: Untuk setiap simpul v, banyak sisi yang menempel = deg(v). Total = Σ deg(v).
- Keduanya menghitung hal yang sama, jadi Σ deg(v) = 2|E| ✓

### 9.2 Contoh Double Counting - Identitas Kombinatorial

**Buktikan:** C(n,2) = 1 + 2 + 3 + ... + (n-1)

**Bukti Double Counting:**
- Ruas kiri: banyak cara memilih 2 elemen dari {1, 2, ..., n}.
- Ruas kanan: Untuk setiap k = 2, 3, ..., n, hitung pasangan {i, k} dengan i < k. Ada k-1 pilihan untuk i. Total = Σ(k=2 to n)(k-1) = 1+2+...+(n-1).
- Kedua cara menghitung hal yang sama. ✓

### 9.3 Bukti Bijektif

**Ide:** Tunjukkan dua himpunan punya ukuran sama dengan membangun korespondensi satu-satu (bijeksi) antara keduanya.

**Contoh:** Buktikan C(n,r) = C(n, n-r).
- Himpunan A: semua subset berukuran r dari {1,...,n}
- Himpunan B: semua subset berukuran n-r dari {1,...,n}
- Bijeksi: S → S^c (komplemen). Setiap subset r elemen berkorespondensi unik dengan komplemen (n-r) elemen.
- |A| = |B|, jadi C(n,r) = C(n,n-r) ✓

---

## 10. Relasi Rekurensi

### 10.1 Pengertian

**Relasi rekurensi** adalah rumus yang mendefinisikan suku ke-n dari barisan berdasarkan suku-suku sebelumnya.

### 10.2 Barisan Fibonacci

```
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), untuk n >= 2
```

Barisan: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

**Sifat penting Fibonacci:**
- F(1) + F(2) + ... + F(n) = F(n+2) - 1
- F(n)^2 + F(n+1)^2 = F(2n+1)
- GCD(F(m), F(n)) = F(GCD(m,n))

### 10.3 Tower of Hanoi

**Masalah:** Pindahkan n piringan dari tiang A ke tiang C menggunakan tiang B sebagai perantara. Aturan: piringan besar tidak boleh di atas piringan kecil, pindah satu per satu.

```
T(1) = 1
T(n) = 2T(n-1) + 1
```

**Solusi:** T(n) = 2^n - 1

**Bukti:**
- T(1) = 2^1 - 1 = 1 ✓
- T(n) = 2T(n-1) + 1 = 2(2^(n-1) - 1) + 1 = 2^n - 2 + 1 = 2^n - 1 ✓

### 10.4 Catalan Numbers

```
C₀ = 1
Cₙ = C(2n, n) / (n+1) = (2n)! / ((n+1)! * n!)
```

Barisan: 1, 1, 2, 5, 14, 42, 132, 429, ...

**Rekurensi:** Cₙ = Σ(i=0 to n-1) Cᵢ * C(n-1-i)

**Muncul dalam berbagai masalah:**
- Banyak cara menyusun n pasang kurung valid
- Banyak binary tree berbeda dengan n node
- Banyak triangulasi polygon (n+2) sisi
- Banyak path grid dari (0,0) ke (n,n) yang tidak melewati diagonal

### 10.5 Menyelesaikan Rekurensi Linear Sederhana

Untuk rekurensi: a(n) = p*a(n-1) + q*a(n-2)

1. Tulis persamaan karakteristik: x^2 = px + q, atau x^2 - px - q = 0
2. Cari akar r₁, r₂
3. Jika r₁ != r₂: a(n) = A*r₁^n + B*r₂^n
4. Tentukan A, B dari kondisi awal

**Contoh untuk Fibonacci:** F(n) = F(n-1) + F(n-2)
- Persamaan: x^2 = x + 1 → x^2 - x - 1 = 0
- Akar: r = (1 +/- sqrt(5))/2
- r₁ = (1+sqrt(5))/2 (golden ratio phi)
- r₂ = (1-sqrt(5))/2
- F(n) = (phi^n - psi^n) / sqrt(5) (rumus Binet)

---

## 11. Deret Aritmetika

### 11.1 Definisi

**Barisan aritmetika:** barisan bilangan dengan selisih (beda) tetap antara dua suku berurutan.

```
a, a+d, a+2d, a+3d, ...
```
- a = suku pertama (a₁)
- d = beda (common difference) = aₙ - a(n-1)

### 11.2 Rumus Suku ke-n

```
aₙ = a + (n-1)d
```

**Penurunan:** 
- a₁ = a
- a₂ = a + d
- a₃ = a + 2d
- ...
- aₙ = a + (n-1)d

### 11.3 Rumus Jumlah n Suku Pertama

```
Sₙ = n/2 * (a₁ + aₙ) = n/2 * (2a + (n-1)d)
```

**Penurunan (metode Gauss):**
```
Sₙ = a₁ + a₂ + a₃ + ... + aₙ
Sₙ = aₙ + a(n-1) + a(n-2) + ... + a₁   (tulis terbalik)
--------------------------------------------
2Sₙ = (a₁+aₙ) + (a₂+a(n-1)) + ... + (aₙ+a₁)
     = n * (a₁ + aₙ)
Sₙ = n(a₁ + aₙ)/2
```

### 11.4 Sifat Barisan Aritmetika

- Jika a, b, c membentuk barisan aritmetika, maka b = (a+c)/2 (b adalah rata-rata aritmetika)
- Suku tengah (jika jumlah suku ganjil) = rata-rata semua suku
- Sisipan aritmetika: menyisipkan k bilangan antara a dan b membentuk barisan aritmetika

### 11.5 Contoh Penting

**Jumlah 1 + 2 + 3 + ... + n:**
```
= n(n+1)/2
```
Ini adalah C(n+1, 2) = bilangan segitiga ke-n.

**Jumlah bilangan ganjil pertama:**
```
1 + 3 + 5 + ... + (2n-1) = n^2
```

**Jumlah bilangan genap pertama:**
```
2 + 4 + 6 + ... + 2n = n(n+1)
```

---

## 12. Deret Geometri

### 12.1 Definisi

**Barisan geometri:** barisan bilangan dengan rasio tetap antara dua suku berurutan.

```
a, ar, ar^2, ar^3, ...
```
- a = suku pertama (a != 0)
- r = rasio (common ratio) = aₙ/a(n-1)

### 12.2 Rumus Suku ke-n

```
aₙ = a * r^(n-1)
```

### 12.3 Rumus Jumlah n Suku Pertama

```
Sₙ = a * (r^n - 1) / (r - 1),  jika r != 1
Sₙ = n * a,                     jika r = 1
```

**Penurunan:**
```
Sₙ = a + ar + ar^2 + ... + ar^(n-1)
rSₙ = ar + ar^2 + ... + ar^n
Sₙ - rSₙ = a - ar^n
Sₙ(1-r) = a(1-r^n)
Sₙ = a(1-r^n)/(1-r) = a(r^n-1)/(r-1)
```

### 12.4 Deret Geometri Tak Hingga

Jika |r| < 1, deret konvergen:
```
S∞ = a / (1-r),  |r| < 1
```

**Contoh:** 1 + 1/2 + 1/4 + 1/8 + ... = 1/(1 - 1/2) = 2

**Divergen jika |r| >= 1** (jumlahnya tidak terhingga atau tidak tentu)

### 12.5 Sifat Barisan Geometri

- Jika a, b, c membentuk barisan geometri, maka b^2 = ac (b adalah rata-rata geometri)
- Hasil kali n suku: P = a^n * r^(n(n-1)/2)

---

## 13. Deret-Deret Penting Lainnya

### 13.1 Jumlah Kuadrat Bilangan Asli

```
1^2 + 2^2 + 3^2 + ... + n^2 = n(n+1)(2n+1) / 6
```

**Verifikasi untuk n=3:** 1 + 4 + 9 = 14 = 3*4*7/6 = 84/6 = 14 ✓

### 13.2 Jumlah Kubik Bilangan Asli

```
1^3 + 2^3 + 3^3 + ... + n^3 = [n(n+1)/2]^2
```

**Fakta menarik:** Jumlah kubik = kuadrat dari jumlah bilangan asli!
```
1^3 + 2^3 + 3^3 + ... + n^3 = (1 + 2 + 3 + ... + n)^2
```

### 13.3 Deret Teleskopik

Deret yang suku-sukunya saling menghilangkan:

```
Σ(k=1 to n) [f(k) - f(k+1)] = f(1) - f(n+1)
```

**Contoh:** Hitung Σ(k=1 to n) 1/(k(k+1))

Pecah dengan partial fraction: 1/(k(k+1)) = 1/k - 1/(k+1)

```
= (1/1 - 1/2) + (1/2 - 1/3) + ... + (1/n - 1/(n+1))
= 1 - 1/(n+1)
= n/(n+1)
```

### 13.4 Deret Pangkat 2

```
1 + 2 + 4 + 8 + ... + 2^(n-1) = 2^n - 1
```

Ini adalah deret geometri dengan a=1, r=2:
S = 1*(2^n - 1)/(2-1) = 2^n - 1

### 13.5 Tabel Ringkasan Deret Penting

| Deret | Rumus |
|-------|-------|
| 1 + 2 + ... + n | n(n+1)/2 |
| 1^2 + 2^2 + ... + n^2 | n(n+1)(2n+1)/6 |
| 1^3 + 2^3 + ... + n^3 | [n(n+1)/2]^2 |
| 1 + 3 + 5 + ... + (2n-1) | n^2 |
| 1 + r + r^2 + ... + r^(n-1) | (r^n - 1)/(r - 1) |
| a + ar + ar^2 + ... (tak hingga, |r|<1) | a/(1-r) |
| Σ 1/(k(k+1)) dari 1 ke n | n/(n+1) |

---

## 14. Contoh Soal & Pembahasan

### Contoh 1: Aturan Perkalian & Penjumlahan

**Soal:** Sebuah plat nomor kendaraan terdiri dari 2 huruf diikuti 4 angka. Huruf pertama hanya bisa A-Z (26 huruf), huruf kedua A-Z, angka 0-9. Berapa banyak plat nomor yang mungkin?

**Pembahasan:**
```
Langkah 1: Huruf pertama = 26 pilihan
Langkah 2: Huruf kedua = 26 pilihan
Langkah 3: Angka pertama = 10 pilihan
Langkah 4: Angka kedua = 10 pilihan
Langkah 5: Angka ketiga = 10 pilihan
Langkah 6: Angka keempat = 10 pilihan

Total = 26 x 26 x 10 x 10 x 10 x 10 = 6.760.000 plat
```

---

### Contoh 2: Permutasi dengan Objek Berulang

**Soal:** Berapa banyak susunan berbeda dari huruf-huruf pada kata "MISSISSIPPI"?

**Pembahasan:**
```
Total huruf = 11
M: 1 kali
I: 4 kali
S: 4 kali
P: 2 kali

Susunan = 11! / (1! * 4! * 4! * 2!)
        = 39916800 / (1 * 24 * 24 * 2)
        = 39916800 / 1152
        = 34650
```

---

### Contoh 3: Permutasi Siklis

**Soal:** 8 orang akan duduk mengelilingi meja bundar. 2 orang tertentu (A dan B) harus duduk berdampingan. Berapa banyak susunan?

**Pembahasan:**
```
Langkah 1: Anggap A dan B sebagai satu "blok" → ada 7 "objek" dalam lingkaran
Langkah 2: Permutasi siklis 7 objek = (7-1)! = 6! = 720
Langkah 3: Di dalam blok, A dan B bisa bertukar posisi = 2! = 2
Total = 720 * 2 = 1440 susunan
```

---

### Contoh 4: Kombinasi - Pembagian Kelompok

**Soal:** 12 siswa dibagi menjadi 3 kelompok masing-masing 4 orang. Berapa banyak cara?

**Pembahasan:**
```
Jika kelompok DIBEDAKAN (kelompok A, B, C):
= C(12,4) * C(8,4) * C(4,4)
= 495 * 70 * 1
= 34650

Jika kelompok TIDAK DIBEDAKAN (kelompok identik):
= 34650 / 3!
= 34650 / 6
= 5775
```

**Hati-hati:** Pertanyaan sering menjebak di sini. Perhatikan apakah kelompok punya label/nama atau tidak!

---

### Contoh 5: Pigeonhole Principle

**Soal:** Buktikan bahwa di antara 6 bilangan bulat sembarang, pasti ada 2 bilangan yang selisihnya habis dibagi 5.

**Pembahasan:**
```
Setiap bilangan bulat jika dibagi 5 sisanya salah satu dari: {0, 1, 2, 3, 4}
→ Ada 5 "kotak" (sisa pembagian)

Ada 6 bilangan (objek) dan 5 kotak.
Karena 6 > 5, maka pasti ada minimal 2 bilangan dengan sisa yang sama.

Jika a mod 5 = b mod 5, maka (a - b) mod 5 = 0
→ Selisihnya habis dibagi 5. ✓
```

---

### Contoh 6: Stars and Bars

**Soal:** Berapa banyak solusi bilangan bulat non-negatif dari persamaan x + y + z = 10?

**Pembahasan:**
```
Ini masalah stars and bars klasik.
n = 10 (jumlah yang dibagi)
k = 3 (banyak variabel/kelompok)

Jawab = C(n + k - 1, k - 1) = C(10 + 3 - 1, 3 - 1) = C(12, 2) = 66
```

---

### Contoh 7: Stars and Bars dengan Batas

**Soal:** Berapa banyak solusi bilangan bulat dari x + y + z = 15, dengan x >= 2, y >= 3, z >= 1?

**Pembahasan:**
```
Substitusi: a = x-2, b = y-3, c = z-1 (sehingga a,b,c >= 0)
Persamaan menjadi: (a+2) + (b+3) + (c+1) = 15
→ a + b + c = 15 - 2 - 3 - 1 = 9

Jawab = C(9 + 3 - 1, 3 - 1) = C(11, 2) = 55
```

---

### Contoh 8: Teorema Binomial

**Soal:** Tentukan koefisien x^5 dalam ekspansi (2x - 3)^8.

**Pembahasan:**
```
Suku umum: T(r+1) = C(8,r) * (2x)^(8-r) * (-3)^r

Kita butuh pangkat x = 8-r = 5 → r = 3

T(4) = C(8,3) * (2x)^5 * (-3)^3
     = 56 * 32x^5 * (-27)
     = 56 * 32 * (-27) * x^5
     = -48384x^5

Koefisien x^5 = -48384
```

---

### Contoh 9: Deret Aritmetika

**Soal:** Suku pertama barisan aritmetika adalah 7 dan suku ke-20 adalah 64. Tentukan jumlah 30 suku pertama.

**Pembahasan:**
```
a₁ = 7, a₂₀ = 64
aₙ = a + (n-1)d
64 = 7 + 19d
19d = 57
d = 3

S₃₀ = 30/2 * (2*7 + 29*3)
     = 15 * (14 + 87)
     = 15 * 101
     = 1515
```

---

### Contoh 10: Deret Geometri

**Soal:** Sebuah bola dijatuhkan dari ketinggian 16 meter. Setiap memantul, bola naik 3/4 dari ketinggian sebelumnya. Tentukan total jarak yang ditempuh bola hingga berhenti.

**Pembahasan:**
```
Jarak turun pertama = 16
Jarak naik pertama = 16 * 3/4 = 12
Jarak turun kedua = 12
Jarak naik kedua = 12 * 3/4 = 9
...

Total jarak = 16 + 2*(12 + 9 + 27/4 + ...)
            = 16 + 2 * deret geometri (a=12, r=3/4)
            = 16 + 2 * 12/(1 - 3/4)
            = 16 + 2 * 12/(1/4)
            = 16 + 2 * 48
            = 16 + 96
            = 112 meter
```

---

### Contoh 11: Deret Teleskopik

**Soal:** Hitung 1/(1*2) + 1/(2*3) + 1/(3*4) + ... + 1/(99*100).

**Pembahasan:**
```
Partial fraction: 1/(k(k+1)) = 1/k - 1/(k+1)

Jumlah = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/99 - 1/100)
       = 1 - 1/100     [suku-suku tengah saling menghilangkan]
       = 99/100
```

---

### Contoh 12: Relasi Rekurensi - Fibonacci

**Soal:** Sebuah tangga memiliki 10 anak tangga. Seseorang bisa naik 1 atau 2 anak tangga sekaligus. Berapa banyak cara naik tangga?

**Pembahasan:**
```
Misalkan f(n) = banyak cara naik n anak tangga.

Basis: f(1) = 1 (satu langkah), f(2) = 2 (1+1 atau 2)

Rekurensi: f(n) = f(n-1) + f(n-2)
[Langkah terakhir bisa naik 1 (dari posisi n-1) atau naik 2 (dari posisi n-2)]

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

Jawab: 89 cara
```
Catatan: Ini sama dengan F(n+1) di mana F adalah barisan Fibonacci!

---

### Contoh 13: Inklusi-Eksklusi

**Soal:** Dari 100 siswa, 60 suka matematika, 45 suka fisika, 35 suka kimia, 20 suka matematika dan fisika, 15 suka fisika dan kimia, 10 suka matematika dan kimia, 5 suka ketiganya. Berapa siswa yang tidak suka ketiganya?

**Pembahasan:**
```
|M ∪ F ∪ K| = |M| + |F| + |K| - |M∩F| - |F∩K| - |M∩K| + |M∩F∩K|
            = 60 + 45 + 35 - 20 - 15 - 10 + 5
            = 140 - 45 + 5
            = 100

Yang tidak suka ketiganya = 100 - 100 = 0

Semua siswa suka minimal satu mata pelajaran!
```

---

### Contoh 14: Catalan Number

**Soal:** Berapa banyak cara menyusun tanda kurung yang valid untuk 4 pasang kurung?

**Pembahasan:**
```
Ini adalah Catalan number C₄.

C₄ = C(2*4, 4) / (4+1) = C(8,4) / 5 = 70/5 = 14

Atau daftar lengkap untuk 4 pasang:
(((())))  ((()))()  (())(())  ((())())  (()(()))
(())()()  ()((()))  ()(()())  ()(())()  ()()(())
()()()()  (()())()  (()(()))  ((()()))

Jawab: 14 cara
```

---

### Contoh 15: Kombinasi Campuran

**Soal:** Berapa banyak bilangan 4 digit yang digit-digitnya membentuk barisan TIDAK turun (monoton naik atau sama)? Digit pertama bukan 0.

**Pembahasan:**
```
Bilangan 4 digit: d₁d₂d₃d₄ dengan 1 <= d₁ <= d₂ <= d₃ <= d₄ <= 9

Ini equivalen dengan memilih 4 digit dari {1,2,...,9} dengan pengulangan
dan urutan tidak penting (karena kita selalu susun naik).

Ini adalah combination with repetition!
= C(9 + 4 - 1, 4) = C(12, 4) = 495

Jawab: 495 bilangan
```

---

### Contoh 16: Permutasi dan Larangan Posisi

**Soal:** 5 buku berbeda disusun dalam rak. Buku A tidak boleh di posisi pertama dan buku B tidak boleh di posisi terakhir. Berapa banyak susunan?

**Pembahasan:**
```
Gunakan inklusi-eksklusi.

Total susunan = 5! = 120
|P₁| = A di posisi pertama = 4! = 24
|P₂| = B di posisi terakhir = 4! = 24
|P₁ ∩ P₂| = A di pertama DAN B di terakhir = 3! = 6

Susunan yang MELANGGAR minimal satu = |P₁ ∪ P₂| = 24 + 24 - 6 = 42
Susunan yang MEMENUHI = 120 - 42 = 78
```

---

### Contoh 17: Jumlah Kuadrat dan Kubik

**Soal:** Hitung 1^2 + 2^2 + 3^2 + ... + 20^2.

**Pembahasan:**
```
Gunakan rumus: Σ(k=1 to n) k^2 = n(n+1)(2n+1)/6

Untuk n = 20:
= 20 * 21 * 41 / 6
= 17220 / 6
= 2870
```

---

### Contoh 18: Pigeonhole Tingkat Lanjut

**Soal:** Buktikan bahwa jika kita memilih 5 titik sembarang di dalam persegi satuan (1x1), pasti ada 2 titik yang jaraknya kurang dari sqrt(2)/2.

**Pembahasan:**
```
Bagi persegi satuan menjadi 4 persegi kecil berukuran 1/2 x 1/2.

        +-----+-----+
        |     |     |
        | 1/2 | 1/2 |
        |     |     |
        +-----+-----+
        |     |     |
        |     |     |
        |     |     |
        +-----+-----+

Diagonal persegi kecil = sqrt((1/2)^2 + (1/2)^2) = sqrt(1/2) = sqrt(2)/2

5 titik, 4 kotak → pasti ada 1 kotak berisi >= 2 titik (Pigeonhole)
Jarak maksimum dalam kotak 1/2 x 1/2 adalah diagonalnya = sqrt(2)/2

Jadi 2 titik tersebut berjarak <= sqrt(2)/2. ✓
```

---

## 15. Tips Mengerjakan Soal Kombinatorika OSN

### 15.1 Strategi Umum

1. **Identifikasi tipe soal:** Apakah ini permutasi, kombinasi, stars and bars, pigeonhole, atau deret?
2. **Cek apakah urutan penting:** Jika ya → permutasi. Jika tidak → kombinasi.
3. **Pecah masalah kompleks** menjadi beberapa kasus sederhana.
4. **Gunakan komplemen** jika kondisi "minimal satu" atau "setidaknya" muncul.
5. **Cek dengan kasus kecil:** Jika bingung, coba n=1, n=2, n=3 untuk melihat pola.

### 15.2 Kesalahan Umum yang Harus Dihindari

| Kesalahan | Penjelasan |
|-----------|-----------|
| Lupa bagi 3! saat kelompok identik | Pembagian ke kelompok tanpa label harus bagi k! |
| Anggap C(n,r) = P(n,r) | Permutasi != Kombinasi. P = C * r! |
| Lupa kasus 0 | Digit pertama sering tidak boleh 0 |
| Double counting | Hitung kasus yang sama lebih dari sekali |
| Salah identifikasi stars and bars | Pastikan objek identik, wadah berbeda |

### 15.3 Pola Soal OSN yang Sering Muncul

1. **Menghitung password/plat nomor** dengan syarat tertentu
2. **Pembagian kelompok** dengan/tanpa label
3. **Distribusi objek** (identik vs berbeda, ke wadah identik vs berbeda)
4. **Pigeonhole** dalam konteks bilangan bulat atau geometri
5. **Mencari suku/jumlah deret** dengan pola tertentu
6. **Rekurensi** dari masalah ubin, tangga, atau path

### 15.4 Tabel Rumus Ringkasan

| Masalah | Rumus |
|---------|-------|
| Susun r dari n (urutan penting) | P(n,r) = n!/(n-r)! |
| Pilih r dari n (urutan tidak penting) | C(n,r) = n!/(r!(n-r)!) |
| Susun n dengan pengulangan | n!/(n₁!n₂!...nₖ!) |
| Duduk melingkar n orang | (n-1)! |
| Kalung/gelang n manik | (n-1)!/2 |
| r dari n dengan pengulangan, urutan penting | n^r |
| r dari n dengan pengulangan, urutan tidak penting | C(n+r-1, r) |
| x₁+x₂+...+xₖ=n, xᵢ>=0 | C(n+k-1, k-1) |
| x₁+x₂+...+xₖ=n, xᵢ>=1 | C(n-1, k-1) |

---

## 16. Latihan

### Soal Tingkat Dasar

1. Dari 10 siswa, berapa cara memilih ketua, wakil, dan sekretaris?
2. Berapa banyak kata 4 huruf yang dibentuk dari huruf {A, B, C, D, E} tanpa pengulangan?
3. Berapa banyak cara duduk 6 orang mengelilingi meja bundar?
4. Suku ke-15 dari barisan 3, 7, 11, 15, ... adalah?
5. Jumlah 10 suku pertama dari deret 5 + 10 + 20 + 40 + ... = ?

### Soal Tingkat Menengah

6. Berapa banyak susunan huruf dari kata "STATISTICS"?
7. Berapa banyak cara membagi 15 bola identik ke 4 kotak berbeda, minimal 2 bola per kotak?
8. Tentukan koefisien x^4 dalam ekspansi (1 + 2x)^7.
9. Hitung 1/(1*3) + 1/(3*5) + 1/(5*7) + ... + 1/(99*101).
10. Di antara 25 siswa, minimal berapa yang pasti memiliki inisial nama depan (A-Z) yang sama?

### Soal Tingkat OSN

11. Berapa banyak bilangan 5 digit yang digit-digitnya berjumlah 10?
12. Buktikan: Dari 10 bilangan asli berurutan yang dipilih sembarang, pasti ada bilangan yang saling prima dengan semua bilangan lainnya.
13. Seseorang naik tangga 12 anak, bisa melangkah 1, 2, atau 3 anak tangga sekaligus. Berapa banyak cara?
14. 20 orang berdiri dalam barisan. Berapa cara memilih 6 orang sehingga tidak ada 2 yang bersebelahan?
15. Tentukan jumlah: Σ(k=0 to 10) k*C(10,k).

### Kunci Jawaban Singkat

1. P(10,3) = 720
2. P(5,4) = 120
3. (6-1)! = 120
4. a₁₅ = 3 + 14*4 = 59
5. S₁₀ = 5*(2^10 - 1)/(2-1) = 5115
6. 10!/(3!*3!*2!*1!*1!) = 50400
7. C(7+3,3) = C(10,3) = 120 [substitusi yᵢ = xᵢ-2, y₁+y₂+y₃+y₄ = 7]
8. C(7,4)*2^4 = 35*16 = 560
9. (1/2)(1 - 1/101) = 50/101
10. ⌈25/26⌉ = 1, tapi 25 < 26 jadi belum tentu ada yang sama. Jika 27 siswa, minimal 2.
11. Stars and bars: C(9,4) dikurangi kasus digit pertama=0 dan digit > 9 (gunakan inklusi-eksklusi) = 637 [perhitungan detail memerlukan analisis kasus]
12. Bilangan prima dalam range tersebut pasti saling prima dengan semua lainnya (pembuktian via sifat bilangan prima)
13. f(n) = f(n-1) + f(n-2) + f(n-3); f(12) = 927
14. C(15,6) = 5005 [model: pilih 6 dari 15 posisi "virtual"]
15. 10 * 2^9 = 5120 [gunakan identitas k*C(n,k) = n*C(n-1,k-1)]

---

*Materi ini mencakup topik-topik kombinatorika dan deret yang sering muncul di OSK/OSP Informatika. Kuasai konsep dasar dan banyak berlatih soal untuk meningkatkan kecepatan dan ketepatan.*
