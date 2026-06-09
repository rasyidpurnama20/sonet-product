# Materi 06 — Modulo & Teori Bilangan

Panduan lengkap untuk persiapan OSK Informatika 2026. Materi ini mencakup aritmatika modular,
teori bilangan, algoritma terkait, serta operasi biner dan XOR yang sering muncul di soal OSN.

---

## 1. Operasi Modulo — Konsep Dasar

### 1.1 Definisi

Operasi modulo memberikan **sisa pembagian** bilangan bulat `a` oleh bilangan positif `m`.

```
a = q × m + r,    dimana 0 ≤ r < m
r = a mod m
q = floor(a / m)
```

- `a` disebut **dividen** (bilangan yang dibagi)
- `m` disebut **modulus** (pembagi)
- `q` disebut **quotient** (hasil bagi)
- `r` disebut **remainder** (sisa)

### 1.2 Contoh Dasar

```
17 mod 5  = 2     (karena 17 = 3×5 + 2)
100 mod 7 = 2     (karena 100 = 14×7 + 2)
12 mod 4  = 0     (habis dibagi, sisa = 0)
25 mod 25 = 0     (karena 25 = 1×25 + 0)
3 mod 7   = 3     (karena 3 = 0×7 + 3, jika a < m maka a mod m = a)
```

### 1.3 Modulo untuk Bilangan Negatif

Dalam matematika, sisa selalu non-negatif: `0 ≤ r < m`.

```
-1 mod 5 = 4    (karena -1 = (-1)×5 + 4)
-7 mod 3 = 2    (karena -7 = (-3)×3 + 2)
-13 mod 5 = 2   (karena -13 = (-3)×5 + 2)
```

> **Perhatian C++:** Operator `%` di C++ mengikuti tanda pembilang untuk bilangan negatif.
> `(-1) % 5 = -1` di C++ (bukan 4).
> `(-7) % 3 = -1` di C++ (bukan 2).
> Untuk mendapatkan sisa positif di C++: `((a % m) + m) % m`

---

## 2. Sifat-Sifat Aritmatika Modular

### 2.1 Sifat Penjumlahan

```
(a + b) mod m = ((a mod m) + (b mod m)) mod m
```

**Bukti:**
Misalkan `a = q1*m + r1` dan `b = q2*m + r2`, maka:
```
a + b = (q1 + q2)*m + (r1 + r2)
```
Sisa dari `a + b` dibagi `m` sama dengan sisa dari `(r1 + r2)` dibagi `m`.
Karena `r1 = a mod m` dan `r2 = b mod m`, terbukti.

**Contoh:**
```
(17 + 23) mod 5 = 40 mod 5 = 0
Cara cepat: (17 mod 5 + 23 mod 5) mod 5 = (2 + 3) mod 5 = 5 mod 5 = 0 ✓
```

### 2.2 Sifat Pengurangan

```
(a - b) mod m = ((a mod m) - (b mod m) + m) mod m
```

Penambahan `+m` diperlukan untuk menghindari hasil negatif.

**Contoh:**
```
(10 - 17) mod 5 = -7 mod 5 = 3  (secara matematika)
Cara cepat: (10 mod 5 - 17 mod 5 + 5) mod 5 = (0 - 2 + 5) mod 5 = 3 mod 5 = 3 ✓
```

### 2.3 Sifat Perkalian

```
(a × b) mod m = ((a mod m) × (b mod m)) mod m
```

**Bukti:**
Misalkan `a = q1*m + r1` dan `b = q2*m + r2`, maka:
```
a × b = (q1*m + r1)(q2*m + r2)
      = q1*q2*m² + q1*m*r2 + q2*m*r1 + r1*r2
      = m*(q1*q2*m + q1*r2 + q2*r1) + r1*r2
```
Sisanya ketika dibagi `m` sama dengan `(r1*r2) mod m`. Terbukti.

**Contoh:**
```
(13 × 17) mod 5 = 221 mod 5 = 1
Cara cepat: (13 mod 5 × 17 mod 5) mod 5 = (3 × 2) mod 5 = 6 mod 5 = 1 ✓
```

### 2.4 Sifat Perpangkatan

```
a^n mod m = ((a mod m)^n) mod m
```

Ini mengikuti dari penerapan berulang sifat perkalian.

**Contoh:**
```
7^3 mod 5 = 343 mod 5 = 3
Cara cepat: (7 mod 5)^3 mod 5 = 2^3 mod 5 = 8 mod 5 = 3 ✓
```

### 2.5 Sifat TIDAK Berlaku untuk Pembagian

**PENTING:** Sifat modulo TIDAK berlaku untuk pembagian!

```
(a / b) mod m ≠ ((a mod m) / (b mod m)) mod m   ← SALAH!
```

**Contoh kontra:**
```
(10 / 2) mod 3 = 5 mod 3 = 2
Jika pakai rumus salah: (10 mod 3) / (2 mod 3) = 1 / 2 = 0 ← SALAH!
```

Untuk pembagian modular, kita perlu **invers modular** (dibahas di bagian 5).

### 2.6 Kongruensi

Dua bilangan `a` dan `b` dikatakan **kongruen modulo m** jika memberikan sisa yang sama:

```
a ≡ b (mod m)  berarti  m | (a - b)  berarti  a mod m = b mod m
```

**Contoh:**
```
17 ≡ 2 (mod 5)    karena 17 mod 5 = 2 dan 2 mod 5 = 2
23 ≡ 3 (mod 10)   karena 23 mod 10 = 3
100 ≡ 0 (mod 4)   karena 100 mod 4 = 0
```

---

## 3. Perpangkatan Modular (Modular Exponentiation)

### 3.1 Masalah

Menghitung `a^n mod m` untuk `n` yang sangat besar (misal `n = 10^18`).
Menghitung `a^n` secara langsung tidak mungkin karena hasilnya terlalu besar.

### 3.2 Metode Pola Berulang

Untuk modulus kecil, cari pola sisa yang berulang (siklik).

**Contoh: `2^1000 mod 3`**
```
2^1 mod 3 = 2
2^2 mod 3 = 4 mod 3 = 1
2^3 mod 3 = 8 mod 3 = 2
2^4 mod 3 = 16 mod 3 = 1
Pola: 2, 1, 2, 1, ... (periode = 2)
- Pangkat ganjil → sisa 2
- Pangkat genap → sisa 1
2^1000 mod 3 = 1 (karena 1000 genap)
```

**Contoh: `3^100 mod 7`**
```
3^1 mod 7 = 3
3^2 mod 7 = 9 mod 7 = 2
3^3 mod 7 = 27 mod 7 = 6
3^4 mod 7 = 81 mod 7 = 4
3^5 mod 7 = 243 mod 7 = 5
3^6 mod 7 = 729 mod 7 = 1
Pola berulang tiap 6: 3, 2, 6, 4, 5, 1, 3, 2, 6, ...
100 mod 6 = 4
Jadi 3^100 mod 7 = 3^4 mod 7 = 4
```

### 3.3 Algoritma Fast Power (Exponentiation by Squaring)

Ide: Gunakan representasi biner dari pangkat.

```
a^13 = a^(1101 dalam biner) = a^8 × a^4 × a^1
```

**Algoritma:**
```
function fastPow(a, n, m):
    result = 1
    a = a mod m
    while n > 0:
        if n ganjil:
            result = (result × a) mod m
        n = n / 2  (bulatkan ke bawah)
        a = (a × a) mod m
    return result
```

**Kode C++:**
```cpp
long long fastPow(long long a, long long n, long long m) {
    long long result = 1;
    a %= m;
    while (n > 0) {
        if (n & 1)  // n ganjil
            result = (result * a) % m;
        n >>= 1;    // n = n / 2
        a = (a * a) % m;
    }
    return result;
}
```

**Kompleksitas:** O(log n) -- sangat cepat bahkan untuk n = 10^18.

### 3.4 Trace Contoh: `2^13 mod 1000`

```
Langkah awal: result = 1, a = 2, n = 13

Iterasi 1: n=13 (ganjil) → result = 1×2 = 2. n=6, a=4
Iterasi 2: n=6 (genap). n=3, a=16
Iterasi 3: n=3 (ganjil) → result = 2×16 = 32. n=1, a=256
Iterasi 4: n=1 (ganjil) → result = 32×256 = 8192. n=0, a=65536

Jawaban: 8192 mod 1000 = 192

Verifikasi: 2^13 = 8192. 8192 mod 1000 = 192 ✓
```

### 3.5 Fermat's Little Theorem

Jika `p` bilangan prima dan `gcd(a, p) = 1` (a tidak habis dibagi p), maka:

```
a^(p-1) ≡ 1 (mod p)
```

Konsekuensi: `a^n mod p = a^(n mod (p-1)) mod p`

**Contoh: `2^100 mod 13`**
```
13 prima, gcd(2, 13) = 1
Fermat: 2^12 ≡ 1 (mod 13)
100 = 12×8 + 4
2^100 = (2^12)^8 × 2^4 ≡ 1^8 × 16 ≡ 16 mod 13 = 3
Jadi 2^100 mod 13 = 3
```

---

## 4. Algoritma Euclidean dan Extended Euclidean

### 4.1 GCD (FPB) - Algoritma Euclidean

```
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
```

**Contoh lengkap: gcd(252, 198)**
```
gcd(252, 198) = gcd(198, 252 mod 198) = gcd(198, 54)
gcd(198, 54)  = gcd(54, 198 mod 54)   = gcd(54, 36)
gcd(54, 36)   = gcd(36, 54 mod 36)    = gcd(36, 18)
gcd(36, 18)   = gcd(18, 36 mod 18)    = gcd(18, 0)
gcd(18, 0)    = 18

Jadi gcd(252, 198) = 18
```

### 4.2 LCM (KPK)

```
lcm(a, b) = (a × b) / gcd(a, b)
```

**Contoh:**
```
lcm(12, 18) = (12 × 18) / gcd(12, 18) = 216 / 6 = 36
```

### 4.3 Extended Euclidean Algorithm

Extended Euclidean Algorithm mencari bilangan bulat `x` dan `y` sedemikian sehingga:

```
a*x + b*y = gcd(a, b)
```

Ini disebut **Bezout's Identity** -- untuk setiap `a, b` selalu ada `x, y` yang memenuhi.

**Algoritma:**
```
function extGCD(a, b):
    if b == 0:
        return (a, 1, 0)   // gcd, x, y
    else:
        (g, x1, y1) = extGCD(b, a mod b)
        x = y1
        y = x1 - floor(a/b) * y1
        return (g, x, y)
```

**Trace: extGCD(35, 15)**
```
extGCD(35, 15):
  extGCD(15, 5):     // 35 mod 15 = 5
    extGCD(5, 0):    // 15 mod 5 = 0
      return (5, 1, 0)  // basis: gcd=5, x=1, y=0 → 5*1 + 0*0 = 5
    x = 0, y = 1 - 3*0 = 1
    return (5, 0, 1)    // 15*0 + 5*1 = 5 ✓
  x = 1, y = 0 - 2*1 = -2
  return (5, 1, -2)     // 35*1 + 15*(-2) = 35 - 30 = 5 ✓

Hasil: gcd(35, 15) = 5, dan 35×1 + 15×(-2) = 5
```

**Kode C++:**
```cpp
int extGCD(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    int x1, y1;
    int g = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
```

---

## 5. Invers Modular

### 5.1 Definisi

Invers modular dari `a` terhadap modulus `m` adalah bilangan `x` sedemikian sehingga:

```
a × x ≡ 1 (mod m)
```

Ditulis sebagai `x = a^(-1) mod m`.

**Syarat:** Invers modular ada jika dan hanya jika `gcd(a, m) = 1`.

### 5.2 Mencari Invers dengan Extended Euclidean

Dari `a*x + m*y = gcd(a, m) = 1`, kita peroleh:
```
a*x ≡ 1 (mod m)
```
Jadi `x` dari Extended Euclidean Algorithm adalah invers dari `a mod m`.

**Contoh: Invers dari 3 mod 7**
```
extGCD(3, 7):
  extGCD(7, 3):    // kita perlu 3*x + 7*y = 1
    3*x + 7*y = 1
    Coba: 3*5 + 7*(-2) = 15 - 14 = 1 ✓
    Jadi invers 3 mod 7 = 5

Verifikasi: 3 × 5 = 15, dan 15 mod 7 = 1 ✓
```

### 5.3 Mencari Invers dengan Fermat (jika m prima)

Jika `m` bilangan prima, dari Fermat's Little Theorem:
```
a^(m-1) ≡ 1 (mod m)
a × a^(m-2) ≡ 1 (mod m)
```

Jadi `a^(-1) mod m = a^(m-2) mod m`.

**Contoh: Invers dari 3 mod 7**
```
3^(-1) mod 7 = 3^(7-2) mod 7 = 3^5 mod 7
3^5 = 243
243 mod 7 = 243 - 34×7 = 243 - 238 = 5

Verifikasi: 3 × 5 = 15, dan 15 mod 7 = 1 ✓
```

### 5.4 Aplikasi Invers: Pembagian Modular

Untuk menghitung `(a / b) mod m`:
```
(a / b) mod m = (a × b^(-1)) mod m
```

**Contoh: `(10 / 3) mod 7`**
```
Invers 3 mod 7 = 5 (dari contoh sebelumnya)
(10 / 3) mod 7 = (10 × 5) mod 7 = 50 mod 7 = 1

Verifikasi: 10/3 bukan bilangan bulat, tapi dalam aritmatika modular:
Kita cari x dimana 3*x ≡ 10 (mod 7)
3*1 = 3, 3*2 = 6, 3*3 = 9 ≡ 2, 3*4 = 12 ≡ 5, 3*5 = 15 ≡ 1,
3*6 = 18 ≡ 4, 3*8 = 24 ≡ 3... hmm
Cek: x=1 → 3×1=3 mod7=3≠10mod7=3. Ya! 10 mod 7 = 3, jadi x=1?
Tunggu: 3*x mod 7 = 10 mod 7 = 3, jadi 3x ≡ 3 (mod 7), x ≡ 1 (mod 7).
Tapi (10×5) mod 7 = 50 mod 7 = 1... mari kita cek ulang.
Sebenarnya (a/b) mod m berarti kita cari x = a × b^{-1} mod m.
= 10 × 5 mod 7 = 50 mod 7 = 1.
Verifikasi: b × x = 3 × 1 = 3, dan 3 mod 7 = 3 = 10 mod 7? 
10 mod 7 = 3. Ya! 3 × 1 ≡ 3 ≡ 10 (mod 7) ✓
```

---

## 6. Chinese Remainder Theorem (CRT)

### 6.1 Pernyataan

Jika `m1, m2, ..., mk` adalah bilangan-bilangan yang **saling relatif prima** (gcd tiap pasang = 1),
maka sistem kongruensi:

```
x ≡ a1 (mod m1)
x ≡ a2 (mod m2)
...
x ≡ ak (mod mk)
```

memiliki **tepat satu** solusi modulo `M = m1 × m2 × ... × mk`.

### 6.2 Ide Dasar Penyelesaian (2 Kongruensi)

Untuk menyelesaikan:
```
x ≡ a (mod m)
x ≡ b (mod n)
```
dimana gcd(m, n) = 1:

1. Dari persamaan pertama: `x = a + m*t` untuk suatu bilangan bulat `t`
2. Substitusi ke persamaan kedua: `a + m*t ≡ b (mod n)`
3. Selesaikan: `m*t ≡ (b - a) (mod n)`, cari `t`

### 6.3 Contoh CRT

**Soal:** Cari bilangan terkecil positif x yang memenuhi:
```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
```

**Penyelesaian:**

Langkah 1: Dari `x ≡ 2 (mod 3)` → x = 2, 5, 8, 11, 14, 17, 20, 23, ...

Langkah 2: Dari daftar di atas, cari yang memenuhi `x ≡ 3 (mod 5)`:
- x = 8: 8 mod 5 = 3 ✓

Langkah 3: Solusi dari dua kongruensi pertama: x ≡ 8 (mod 15)
(karena lcm(3,5) = 15)
Daftar: x = 8, 23, 38, 53, 68, 83, ...

Langkah 4: Cari yang memenuhi `x ≡ 2 (mod 7)`:
- x = 8: 8 mod 7 = 1 ✗
- x = 23: 23 mod 7 = 2 ✓

**Jawaban: x = 23**

Verifikasi:
```
23 mod 3 = 2 ✓
23 mod 5 = 3 ✓
23 mod 7 = 2 ✓
```

Solusi umum: x ≡ 23 (mod 105), karena M = 3×5×7 = 105.

### 6.4 Contoh Soal CRT Klasik

**Soal:** Seorang petani memiliki telur. Jika dihitung per 3, sisa 1.
Jika dihitung per 5, sisa 2. Jika dihitung per 7, sisa 3. Berapa telur minimum?

```
x ≡ 1 (mod 3)
x ≡ 2 (mod 5)
x ≡ 3 (mod 7)
```

Langkah 1: x ≡ 1 (mod 3) → x = 1, 4, 7, 10, 13, 16, 19, 22, 25, ...
Langkah 2: Cari x ≡ 2 (mod 5) dari daftar:
- x = 7: 7 mod 5 = 2 ✓
Langkah 3: x ≡ 7 (mod 15) → x = 7, 22, 37, 52, ...
Langkah 4: Cari x ≡ 3 (mod 7):
- x = 7: 7 mod 7 = 0 ✗
- x = 22: 22 mod 7 = 1 ✗
- x = 37: 37 mod 7 = 2 ✗
- x = 52: 52 mod 7 = 3 ✓

**Jawaban: 52 telur**

---

## 7. Aturan Keterbagian (Divisibility Rules)

### 7.1 Keterbagian oleh 2

Suatu bilangan habis dibagi 2 jika **digit terakhirnya** genap (0, 2, 4, 6, 8).

```
1234 → digit terakhir 4 (genap) → habis dibagi 2 ✓
4567 → digit terakhir 7 (ganjil) → tidak habis dibagi 2 ✗
```

### 7.2 Keterbagian oleh 3

Suatu bilangan habis dibagi 3 jika **jumlah semua digitnya** habis dibagi 3.

```
123 → 1+2+3 = 6, 6 habis dibagi 3 → habis dibagi 3 ✓
456 → 4+5+6 = 15, 15 habis dibagi 3 → habis dibagi 3 ✓
124 → 1+2+4 = 7, 7 tidak habis dibagi 3 → tidak habis dibagi 3 ✗
```

**Mengapa?** Karena 10 ≡ 1 (mod 3), sehingga 10^k ≡ 1 (mod 3) untuk semua k.
Maka bilangan `d_n × 10^n + ... + d_1 × 10 + d_0 ≡ d_n + ... + d_1 + d_0 (mod 3)`.

### 7.3 Keterbagian oleh 4

Suatu bilangan habis dibagi 4 jika **dua digit terakhirnya** membentuk bilangan yang habis dibagi 4.

```
1324 → dua digit terakhir: 24, 24/4 = 6 → habis dibagi 4 ✓
5738 → dua digit terakhir: 38, 38/4 = 9.5 → tidak habis dibagi 4 ✗
```

**Mengapa?** Karena 100 habis dibagi 4, jadi hanya dua digit terakhir yang menentukan.

### 7.4 Keterbagian oleh 5

Suatu bilangan habis dibagi 5 jika digit terakhirnya **0 atau 5**.

```
235 → digit terakhir 5 → habis dibagi 5 ✓
440 → digit terakhir 0 → habis dibagi 5 ✓
123 → digit terakhir 3 → tidak habis dibagi 5 ✗
```

### 7.5 Keterbagian oleh 6

Suatu bilangan habis dibagi 6 jika habis dibagi **2 DAN 3** sekaligus.

```
234 → genap ✓, jumlah digit = 9 habis dibagi 3 ✓ → habis dibagi 6 ✓
135 → ganjil ✗ → tidak habis dibagi 6 ✗
124 → genap ✓, jumlah digit = 7 tidak habis dibagi 3 ✗ → tidak habis dibagi 6 ✗
```

### 7.6 Keterbagian oleh 7

Ambil digit terakhir, kalikan 2, kurangi dari sisa bilangan. Ulangi sampai kecil.

```
Cek apakah 371 habis dibagi 7:
371 → digit terakhir 1, sisa 37. 37 - 2×1 = 35. 35/7 = 5 ✓

Cek apakah 483 habis dibagi 7:
483 → digit terakhir 3, sisa 48. 48 - 2×3 = 42. 42/7 = 6 ✓

Cek apakah 123 habis dibagi 7:
123 → digit terakhir 3, sisa 12. 12 - 2×3 = 6. 6/7 ≠ bilangan bulat ✗
```

### 7.7 Keterbagian oleh 8

Suatu bilangan habis dibagi 8 jika **tiga digit terakhirnya** membentuk bilangan yang habis dibagi 8.

```
1024 → tiga digit terakhir: 024 = 24, 24/8 = 3 → habis dibagi 8 ✓
5765 → tiga digit terakhir: 765, 765/8 = 95.625 → tidak habis dibagi 8 ✗
```

### 7.8 Keterbagian oleh 9

Suatu bilangan habis dibagi 9 jika **jumlah semua digitnya** habis dibagi 9.

```
729 → 7+2+9 = 18, 18/9 = 2 → habis dibagi 9 ✓
123 → 1+2+3 = 6, 6/9 ≠ bilangan bulat → tidak habis dibagi 9 ✗
```

**Alasan sama dengan keterbagian 3:** 10 ≡ 1 (mod 9).

### 7.9 Keterbagian oleh 11

Suatu bilangan habis dibagi 11 jika **selisih jumlah digit posisi ganjil dan genap**
(dari kanan) habis dibagi 11.

```
Cek 121:
  Posisi ganjil (1, 3): 1, 1 → jumlah = 2
  Posisi genap (2): 2 → jumlah = 2
  Selisih: 2 - 2 = 0, habis dibagi 11 ✓

Cek 9174:
  Posisi ganjil (1, 3): 4, 1 → jumlah = 5
  Posisi genap (2, 4): 7, 9 → jumlah = 16
  Selisih: |5 - 16| = 11, habis dibagi 11 ✓

Cek 1234:
  Posisi ganjil (1, 3): 4, 2 → jumlah = 6
  Posisi genap (2, 4): 3, 1 → jumlah = 4
  Selisih: 6 - 4 = 2, tidak habis dibagi 11 ✗
```

**Mengapa?** Karena 10 ≡ -1 (mod 11), sehingga 10^k ≡ (-1)^k (mod 11).
Digit pada posisi genap (dari kanan, mulai 0) dikalikan +1, posisi ganjil dikalikan -1.

### 7.10 Tabel Ringkasan

| Pembagi | Aturan |
|---------|--------|
| 2 | Digit terakhir genap |
| 3 | Jumlah digit habis dibagi 3 |
| 4 | 2 digit terakhir habis dibagi 4 |
| 5 | Digit terakhir 0 atau 5 |
| 6 | Habis dibagi 2 DAN 3 |
| 7 | Selisih: sisa bilangan - 2×digit terakhir |
| 8 | 3 digit terakhir habis dibagi 8 |
| 9 | Jumlah digit habis dibagi 9 |
| 11 | Selisih jumlah digit ganjil dan genap habis dibagi 11 |

---

## 8. Jumlah Pembagi dan Rumus dari Faktorisasi Prima

### 8.1 Faktorisasi Prima

Setiap bilangan bulat `n > 1` dapat ditulis secara unik sebagai:

```
n = p1^a1 × p2^a2 × ... × pk^ak
```

dimana `p1 < p2 < ... < pk` bilangan prima dan `a1, a2, ..., ak ≥ 1`.

**Contoh:**
```
360 = 2^3 × 3^2 × 5^1
5000 = 2^3 × 5^4
72 = 2^3 × 3^2
100 = 2^2 × 5^2
```

### 8.2 Jumlah Pembagi (Number of Divisors) -- τ(n)

Jika `n = p1^a1 × p2^a2 × ... × pk^ak`, maka jumlah pembagi positif dari n adalah:

```
τ(n) = (a1 + 1)(a2 + 1)...(ak + 1)
```

**Penjelasan:** Setiap pembagi d dari n berbentuk `d = p1^b1 × p2^b2 × ... × pk^bk`
dimana `0 ≤ bi ≤ ai`. Untuk setiap pi, ada `(ai + 1)` pilihan untuk bi.

**Contoh 1: Berapa banyak pembagi dari 360?**
```
360 = 2^3 × 3^2 × 5^1
τ(360) = (3+1)(2+1)(1+1) = 4 × 3 × 2 = 24

Pembagi 360: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30,
             36, 40, 45, 60, 72, 90, 120, 180, 360  (total 24 ✓)
```

**Contoh 2: Berapa banyak pembagi dari 1000?**
```
1000 = 2^3 × 5^3
τ(1000) = (3+1)(3+1) = 4 × 4 = 16
```

**Contoh 3: Berapa banyak pembagi dari 2^10?**
```
2^10 = 2^10 (hanya satu faktor prima)
τ(2^10) = 10 + 1 = 11
Pembagi: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
```

### 8.3 Jumlah Semua Pembagi (Sum of Divisors) -- σ(n)

Jika `n = p1^a1 × p2^a2 × ... × pk^ak`, maka jumlah semua pembagi positif:

```
σ(n) = [(p1^(a1+1) - 1)/(p1 - 1)] × [(p2^(a2+1) - 1)/(p2 - 1)] × ... × [(pk^(ak+1) - 1)/(pk - 1)]
```

**Penjelasan untuk satu faktor prima p^a:**
```
Pembagi dari p^a: 1, p, p^2, ..., p^a
Jumlah = 1 + p + p^2 + ... + p^a = (p^(a+1) - 1) / (p - 1)
```
Ini adalah deret geometri.

**Contoh 1: σ(12)**
```
12 = 2^2 × 3^1
σ(12) = [(2^3 - 1)/(2-1)] × [(3^2 - 1)/(3-1)]
      = [7/1] × [8/2]
      = 7 × 4 = 28

Verifikasi: Pembagi 12 = {1, 2, 3, 4, 6, 12}
Jumlah = 1+2+3+4+6+12 = 28 ✓
```

**Contoh 2: σ(360)**
```
360 = 2^3 × 3^2 × 5^1
σ(360) = [(2^4 - 1)/(2-1)] × [(3^3 - 1)/(3-1)] × [(5^2 - 1)/(5-1)]
       = [15/1] × [26/2] × [24/4]
       = 15 × 13 × 6 = 1170
```

### 8.4 Produk Semua Pembagi

Jika `n` memiliki `τ(n)` pembagi, maka:

```
Produk semua pembagi = n^(τ(n)/2)
```

**Contoh: Produk semua pembagi dari 12**
```
τ(12) = 6
Produk = 12^(6/2) = 12^3 = 1728

Verifikasi: 1 × 2 × 3 × 4 × 6 × 12 = 1728 ✓
```

---

## 9. Bilangan Sempurna (Perfect Numbers)

### 9.1 Definisi

Bilangan sempurna adalah bilangan yang sama dengan **jumlah semua pembagi sejatinya**
(semua pembagi selain dirinya sendiri).

Dengan kata lain: `σ(n) - n = n`, atau `σ(n) = 2n`.

### 9.2 Contoh Bilangan Sempurna

**6 adalah bilangan sempurna:**
```
Pembagi sejati 6: 1, 2, 3
Jumlah: 1 + 2 + 3 = 6 ✓
```

**28 adalah bilangan sempurna:**
```
Pembagi sejati 28: 1, 2, 4, 7, 14
Jumlah: 1 + 2 + 4 + 7 + 14 = 28 ✓
```

**496 adalah bilangan sempurna:**
```
Pembagi sejati 496: 1, 2, 4, 8, 16, 31, 62, 124, 248
Jumlah: 1+2+4+8+16+31+62+124+248 = 496 ✓
```

### 9.3 Rumus Euler-Euclid

Semua bilangan sempurna genap berbentuk:

```
n = 2^(p-1) × (2^p - 1)
```

dimana `2^p - 1` adalah bilangan prima (disebut **Mersenne prime**).

```
p=2: 2^1 × (2^2 - 1) = 2 × 3 = 6 ✓
p=3: 2^2 × (2^3 - 1) = 4 × 7 = 28 ✓
p=5: 2^4 × (2^5 - 1) = 16 × 31 = 496 ✓
p=7: 2^6 × (2^7 - 1) = 64 × 127 = 8128 ✓
```

### 9.4 Bilangan Defisien dan Abundant

- **Defisien:** σ(n) - n < n (jumlah pembagi sejati < n). Contoh: 8 (1+2+4=7 < 8)
- **Abundant:** σ(n) - n > n (jumlah pembagi sejati > n). Contoh: 12 (1+2+3+4+6=16 > 12)

---

## 10. Fungsi Floor dan Ceiling

### 10.1 Definisi

- **Floor** ⌊x⌋: bilangan bulat terbesar yang ≤ x (pembulatan ke bawah)
- **Ceiling** ⌈x⌉: bilangan bulat terkecil yang ≥ x (pembulatan ke atas)

```
⌊3.7⌋ = 3       ⌈3.7⌉ = 4
⌊5.0⌋ = 5       ⌈5.0⌉ = 5
⌊-2.3⌋ = -3     ⌈-2.3⌉ = -2
⌊7/2⌋ = 3       ⌈7/2⌉ = 4
```

### 10.2 Hubungan Floor dan Ceiling

```
⌈x⌉ = ⌊x⌋ + 1    jika x bukan bilangan bulat
⌈x⌉ = ⌊x⌋ = x    jika x bilangan bulat
⌈n/m⌉ = ⌊(n + m - 1) / m⌋    untuk n, m bilangan bulat positif
```

### 10.3 Aplikasi: Pembagian Bulat di C++

Dalam C++, pembagian bilangan bulat sudah otomatis floor (untuk bilangan positif):
```cpp
int a = 7 / 2;   // a = 3 (floor)
int b = 10 / 3;  // b = 3 (floor)
```

Untuk ceiling dalam C++:
```cpp
int ceilDiv(int n, int m) {
    return (n + m - 1) / m;
}
// Contoh: ceilDiv(7, 2) = (7+1)/2 = 4
// Contoh: ceilDiv(10, 3) = (10+2)/3 = 4
```

### 10.4 Aplikasi: Menghitung Kelipatan dalam Range

**Berapa banyak kelipatan m dalam range [1, n]?**
```
Jawaban: ⌊n/m⌋
```

**Contoh: Berapa banyak kelipatan 3 dari 1 sampai 100?**
```
⌊100/3⌋ = 33
Kelipatan: 3, 6, 9, ..., 99 → ada 33 bilangan
```

**Berapa banyak kelipatan m dalam range [a, b]?**
```
Jawaban: ⌊b/m⌋ - ⌊(a-1)/m⌋
```

**Contoh: Berapa banyak kelipatan 7 dari 15 sampai 100?**
```
⌊100/7⌋ - ⌊14/7⌋ = 14 - 2 = 12
```

### 10.5 Aplikasi: Jumlah Digit

Jumlah digit bilangan positif n dalam basis 10:
```
jumlah_digit(n) = ⌊log10(n)⌋ + 1
```

**Contoh:**
```
jumlah_digit(999) = ⌊log10(999)⌋ + 1 = ⌊2.999⌋ + 1 = 2 + 1 = 3 ✓
jumlah_digit(1000) = ⌊log10(1000)⌋ + 1 = ⌊3⌋ + 1 = 3 + 1 = 4 ✓
```

### 10.6 Aplikasi: Pangkat Prima dalam Faktorial

Berapa kali faktor prima p muncul dalam n!?

**Rumus Legendre:**
```
v_p(n!) = ⌊n/p⌋ + ⌊n/p^2⌋ + ⌊n/p^3⌋ + ...
```

**Contoh: Berapa kali faktor 2 muncul dalam 10!?**
```
v_2(10!) = ⌊10/2⌋ + ⌊10/4⌋ + ⌊10/8⌋ + ⌊10/16⌋ + ...
         = 5 + 2 + 1 + 0 + ...
         = 8

Verifikasi: 10! = 3628800 = 2^8 × 3^4 × 5^2 × 7
Faktor 2 muncul 8 kali ✓
```

**Contoh: Berapa trailing zeros (nol di belakang) dari 100!?**
```
Trailing zeros ditentukan oleh min(v_2, v_5). Karena v_2 > v_5, cukup hitung v_5:
v_5(100!) = ⌊100/5⌋ + ⌊100/25⌋ + ⌊100/125⌋ + ...
          = 20 + 4 + 0 + ...
          = 24

Jadi 100! memiliki 24 trailing zeros.
```

---

## 11. Operasi XOR dan Aplikasinya

### 11.1 Definisi XOR (Exclusive OR)

XOR bekerja pada level bit. Hasilnya 1 jika kedua bit berbeda, 0 jika sama.

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Operator di C++:** `^` (caret)

### 11.2 Sifat-Sifat XOR

```
a ^ 0 = a           (identitas)
a ^ a = 0           (self-inverse)
a ^ b = b ^ a       (komutatif)
(a^b)^c = a^(b^c)   (asosiatif)
a ^ b ^ b = a       (pembatalan)
```

### 11.3 Aplikasi: Menemukan Elemen Unik

Jika semua elemen muncul genap kali kecuali satu, XOR semua elemen menghasilkan elemen unik.

```
Array: [5, 3, 4, 3, 5]
5 ^ 3 ^ 4 ^ 3 ^ 5
= (5^5) ^ (3^3) ^ 4
= 0 ^ 0 ^ 4
= 4
```

### 11.4 Aplikasi: Swap Tanpa Variabel Tambahan

```cpp
a = a ^ b;
b = a ^ b;  // b = (a^b)^b = a
a = a ^ b;  // a = (a^b)^a = b (sekarang a dan b sudah di-swap)
```

**Trace dengan a=5 (101), b=3 (011):**
```
a = 5^3 = 6 (110)
b = 6^3 = 5 (101)   → b sekarang 5
a = 6^5 = 3 (011)   → a sekarang 3
```

### 11.5 Pola XOR dari 1 sampai n

Ada pola berulang untuk `1 XOR 2 XOR 3 XOR ... XOR n`:

```
Jika n mod 4 == 0: hasilnya = n
Jika n mod 4 == 1: hasilnya = 1
Jika n mod 4 == 2: hasilnya = n + 1
Jika n mod 4 == 3: hasilnya = 0
```

**Bukti melalui observasi:**
```
n=1:  1                          = 1    (1 mod 4 = 1 → 1 ✓)
n=2:  1^2 = 3                   = 3    (2 mod 4 = 2 → 2+1=3 ✓)
n=3:  1^2^3 = 0                 = 0    (3 mod 4 = 3 → 0 ✓)
n=4:  1^2^3^4 = 4               = 4    (4 mod 4 = 0 → 4 ✓)
n=5:  1^2^3^4^5 = 1             = 1    (5 mod 4 = 1 → 1 ✓)
n=6:  1^2^3^4^5^6 = 7           = 7    (6 mod 4 = 2 → 6+1=7 ✓)
n=7:  1^2^3^4^5^6^7 = 0         = 0    (7 mod 4 = 3 → 0 ✓)
n=8:  1^2^3^4^5^6^7^8 = 8       = 8    (8 mod 4 = 0 → 8 ✓)
```

**Mengapa polanya demikian?**
Perhatikan bahwa setiap 4 bilangan berurutan yang dimulai dari kelipatan 4+1 akan XOR menjadi 0:
```
(4k+1) ^ (4k+2) ^ (4k+3) ^ (4k+4) = 0  untuk semua k ≥ 0
```

### 11.6 XOR pada Range [a, b]

Untuk menghitung `a XOR (a+1) XOR ... XOR b`:
```
xor_range(a, b) = xor_1_to(b) XOR xor_1_to(a-1)
```

dimana `xor_1_to(n)` menggunakan pola di atas.

**Contoh: 5 XOR 6 XOR 7 XOR 8**
```
xor_1_to(8) = 8       (8 mod 4 = 0)
xor_1_to(4) = 4       (4 mod 4 = 0)
Jawaban = 8 ^ 4 = 12

Verifikasi: 5^6 = 3, 3^7 = 4, 4^8 = 12 ✓
```

---

## 12. Representasi Biner (Binary Representation)

### 12.1 Konversi Desimal ke Biner

Bagi berulang kali dengan 2, catat sisa dari bawah ke atas.

```
Konversi 42 ke biner:
42 / 2 = 21 sisa 0
21 / 2 = 10 sisa 1
10 / 2 = 5  sisa 0
5  / 2 = 2  sisa 1
2  / 2 = 1  sisa 0
1  / 2 = 0  sisa 1

Baca dari bawah: 101010
Jadi 42 = 101010 (biner)
```

### 12.2 Konversi Biner ke Desimal

Kalikan setiap bit dengan 2^posisi (posisi dari kanan, mulai 0).

```
101010 (biner) = 1×2^5 + 0×2^4 + 1×2^3 + 0×2^2 + 1×2^1 + 0×2^0
              = 32 + 0 + 8 + 0 + 2 + 0
              = 42
```

### 12.3 Operasi Bit Dasar

| Operasi | Simbol C++ | Keterangan |
|---------|-----------|------------|
| AND | `&` | 1 hanya jika kedua bit = 1 |
| OR | `\|` | 1 jika salah satu bit = 1 |
| XOR | `^` | 1 jika bit berbeda |
| NOT | `~` | Membalik semua bit |
| Left Shift | `<<` | Geser bit ke kiri (kalikan 2^k) |
| Right Shift | `>>` | Geser bit ke kanan (bagi 2^k) |

### 12.4 Trik Bit yang Berguna

**1. Cek apakah n genap/ganjil:**
```cpp
if (n & 1)  // ganjil (bit terakhir = 1)
if (!(n & 1))  // genap (bit terakhir = 0)
```

**2. Kalikan/bagi dengan pangkat 2:**
```cpp
n << k   // sama dengan n × 2^k
n >> k   // sama dengan n / 2^k (floor)
```

**3. Cek apakah n adalah pangkat 2:**
```cpp
bool isPowerOf2(int n) {
    return n > 0 && (n & (n-1)) == 0;
}
// Contoh: 8 = 1000, 7 = 0111, 8&7 = 0000 → power of 2 ✓
// Contoh: 6 = 110, 5 = 101, 6&5 = 100 ≠ 0 → bukan power of 2 ✗
```

**4. Mendapatkan bit ke-k:**
```cpp
int getBit(int n, int k) {
    return (n >> k) & 1;
}
```

**5. Set bit ke-k menjadi 1:**
```cpp
int setBit(int n, int k) {
    return n | (1 << k);
}
```

**6. Clear bit ke-k menjadi 0:**
```cpp
int clearBit(int n, int k) {
    return n & ~(1 << k);
}
```

**7. Hitung jumlah bit 1 (popcount):**
```cpp
int countBits(int n) {
    int count = 0;
    while (n > 0) {
        count += (n & 1);
        n >>= 1;
    }
    return count;
}
// Atau: __builtin_popcount(n) di GCC
```

### 12.5 Representasi Biner dan Subset

Setiap bilangan n-bit merepresentasikan sebuah subset dari himpunan n elemen.

```
Himpunan {a, b, c, d} → 4 bit

0000 = {} (himpunan kosong)
0001 = {d}
0010 = {c}
0011 = {c, d}
0100 = {b}
0101 = {b, d}
...
1111 = {a, b, c, d} (semua elemen)
```

Total subset = 2^n.

### 12.6 Jumlah Bit 1 dari 0 sampai n

Masalah: Hitung total jumlah bit 1 dalam representasi biner semua bilangan dari 0 sampai n.

**Contoh: n = 7**
```
0 = 000 → 0 bit 1
1 = 001 → 1 bit 1
2 = 010 → 1 bit 1
3 = 011 → 2 bit 1
4 = 100 → 1 bit 1
5 = 101 → 2 bit 1
6 = 110 → 2 bit 1
7 = 111 → 3 bit 1
Total = 0+1+1+2+1+2+2+3 = 12
```

**Pola:** Untuk `n = 2^k - 1`, total bit 1 = `k × 2^(k-1)`.
Untuk n = 7 = 2^3 - 1: total = 3 × 2^2 = 3 × 4 = 12 ✓

---

## 13. Fungsi Euler (Euler's Totient)

### 13.1 Definisi

`φ(n)` = banyaknya bilangan bulat dalam range [1, n] yang relatif prima dengan n.

Dua bilangan relatif prima jika gcd mereka = 1.

### 13.2 Rumus

```
φ(n) = n × (1 - 1/p1) × (1 - 1/p2) × ... × (1 - 1/pk)
```

dimana p1, p2, ..., pk adalah faktor prima berbeda dari n.

### 13.3 Sifat-Sifat

```
φ(1) = 1
φ(p) = p - 1               untuk p prima
φ(p^k) = p^k - p^(k-1)     = p^(k-1) × (p-1)
φ(a×b) = φ(a) × φ(b)       jika gcd(a, b) = 1
```

### 13.4 Contoh Penghitungan

**φ(12):**
```
12 = 2^2 × 3
φ(12) = 12 × (1 - 1/2) × (1 - 1/3) = 12 × 1/2 × 2/3 = 4

Verifikasi: bilangan 1-12 yang relatif prima dengan 12:
1, 5, 7, 11 → ada 4 bilangan ✓
```

**φ(30):**
```
30 = 2 × 3 × 5
φ(30) = 30 × (1 - 1/2) × (1 - 1/3) × (1 - 1/5)
      = 30 × 1/2 × 2/3 × 4/5
      = 8
```

---

## 14. Bilangan Prima dan Sieve of Eratosthenes

### 14.1 Cek Prima O(sqrt(n))

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}
```

### 14.2 Sieve of Eratosthenes

```cpp
vector<bool> sieve(int n) {
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i*i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return is_prime;
}
```

### 14.3 Faktorisasi Prima

```cpp
map<int, int> factorize(int n) {
    map<int, int> factors;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors[i]++;
            n /= i;
        }
    }
    if (n > 1) factors[n]++;
    return factors;
}
```

---

## 15. Contoh Soal dan Pembahasan

### Contoh 1: Modulo Dasar

**Soal:** Hitung `(123 × 456 + 789) mod 10`

**Penyelesaian:**
```
Langkah 1: 123 mod 10 = 3
Langkah 2: 456 mod 10 = 6
Langkah 3: (123 × 456) mod 10 = (3 × 6) mod 10 = 18 mod 10 = 8
Langkah 4: 789 mod 10 = 9
Langkah 5: (123×456 + 789) mod 10 = (8 + 9) mod 10 = 17 mod 10 = 7

Jawaban: 7
```

### Contoh 2: Perpangkatan Modular

**Soal:** Hitung `7^222 mod 11`

**Penyelesaian:**
```
11 prima, gcd(7, 11) = 1
Fermat's Little Theorem: 7^10 ≡ 1 (mod 11)

222 = 10 × 22 + 2
7^222 = (7^10)^22 × 7^2 ≡ 1^22 × 49 ≡ 49 mod 11 = 5

Jawaban: 5
```

### Contoh 3: GCD dan LCM

**Soal:** Hitung gcd(1071, 462) dan lcm(1071, 462).

**Penyelesaian:**
```
gcd(1071, 462):
1071 = 2 × 462 + 147
462 = 3 × 147 + 21
147 = 7 × 21 + 0

gcd(1071, 462) = 21

lcm(1071, 462) = (1071 × 462) / 21 = 494802 / 21 = 23562
```

### Contoh 4: Jumlah Pembagi

**Soal:** Berapa banyak pembagi positif dari 5040?

**Penyelesaian:**
```
5040 = 7! = 2^4 × 3^2 × 5 × 7
τ(5040) = (4+1)(2+1)(1+1)(1+1) = 5 × 3 × 2 × 2 = 60

Jawaban: 60 pembagi
```

### Contoh 5: Sum of Divisors

**Soal:** Hitung jumlah semua pembagi dari 28.

**Penyelesaian:**
```
28 = 2^2 × 7
σ(28) = [(2^3 - 1)/(2-1)] × [(7^2 - 1)/(7-1)]
      = [7/1] × [48/6]
      = 7 × 8 = 56

Verifikasi: Pembagi 28 = {1, 2, 4, 7, 14, 28}
Jumlah = 1+2+4+7+14+28 = 56 ✓

Catatan: σ(28) = 2×28, jadi 28 bilangan sempurna!
```

### Contoh 6: Floor Function dan Trailing Zeros

**Soal:** Berapa banyak trailing zeros pada 50!?

**Penyelesaian:**
```
Trailing zeros = v_5(50!)
= ⌊50/5⌋ + ⌊50/25⌋ + ⌊50/125⌋ + ...
= 10 + 2 + 0 + ...
= 12

Jawaban: 12 trailing zeros
```

### Contoh 7: XOR Pattern

**Soal:** Hitung 1 XOR 2 XOR 3 XOR ... XOR 100.

**Penyelesaian:**
```
Gunakan pola: n mod 4 menentukan hasilnya.
100 mod 4 = 0 → hasilnya = n = 100

Jawaban: 100

Verifikasi parsial:
1^2^3^4 = 4 (4 mod 4 = 0 → 4 ✓)
1^2^3^4^5^6^7^8 = 8 (8 mod 4 = 0 → 8 ✓)
Polanya konsisten.
```

### Contoh 8: XOR Range

**Soal:** Hitung 10 XOR 11 XOR 12 XOR ... XOR 20.

**Penyelesaian:**
```
xor_range(10, 20) = xor_1_to(20) XOR xor_1_to(9)

xor_1_to(20): 20 mod 4 = 0 → hasilnya = 20
xor_1_to(9): 9 mod 4 = 1 → hasilnya = 1

Jawaban = 20 XOR 1 = 21

Verifikasi:
10 = 01010
11 = 01011
10^11 = 00001 = 1
1^12 = 01101 = 13
13^13 = 0
0^14 = 14
14^15 = 1
1^16 = 17
17^17 = 0
0^18 = 18
18^19 = 1
1^20 = 21 ✓
```

### Contoh 9: Divisibility dan CRT

**Soal:** Cari bilangan 3-digit terkecil yang jika dibagi 3 sisa 1, dibagi 5 sisa 2, dan dibagi 7 sisa 3.

**Penyelesaian:**
```
x ≡ 1 (mod 3)
x ≡ 2 (mod 5)
x ≡ 3 (mod 7)

Langkah 1: x ≡ 1 (mod 3) → x = 1, 4, 7, 10, 13, 16, 19, 22, ...
Langkah 2: Cari yang ≡ 2 (mod 5):
  x=7: 7 mod 5 = 2 ✓
  Solusi: x ≡ 7 (mod 15)

Langkah 3: x = 7, 22, 37, 52, 67, 82, 97, ...
Cari yang ≡ 3 (mod 7):
  x=52: 52 mod 7 = 3 ✓
  Solusi: x ≡ 52 (mod 105)

Langkah 4: x = 52, 157, 262, ...
Bilangan 3-digit terkecil: 157

Verifikasi: 157 mod 3 = 1 ✓, 157 mod 5 = 2 ✓, 157 mod 7 = 3 ✓
```

### Contoh 10: Invers Modular

**Soal:** Hitung (6 / 4) mod 5. Artinya, cari x dimana 4x ≡ 6 (mod 5).

**Penyelesaian:**
```
Pertama, cari invers 4 mod 5.
gcd(4, 5) = 1, jadi invers ada.

Cara 1 (brute force): Cari x dimana 4x mod 5 = 1
  4×1 = 4 mod 5 = 4
  4×2 = 8 mod 5 = 3
  4×3 = 12 mod 5 = 2
  4×4 = 16 mod 5 = 1 ✓
  Invers 4 mod 5 = 4

Cara 2 (Fermat): 4^(5-2) mod 5 = 4^3 mod 5 = 64 mod 5 = 4

Jadi (6/4) mod 5 = 6 × 4 mod 5 = 24 mod 5 = 4

Verifikasi: 4 × 4 = 16 ≡ 1 (mod 5), 
dan 4 × 4 = 16, cek apakah 16 ≡ 6 (mod 5)?
6 mod 5 = 1... mari cek ulang:
Kita mencari x dimana 4x ≡ 6 (mod 5).
6 mod 5 = 1, jadi 4x ≡ 1 (mod 5).
x = 4^{-1} × 1 mod 5 = 4 × 1 = 4.
Cek: 4 × 4 = 16 mod 5 = 1 = 6 mod 5 ✓

Jawaban: 4
```

### Contoh 11: Kelipatan dalam Range

**Soal:** Berapa banyak bilangan dari 1 sampai 1000 yang:
(a) habis dibagi 6?
(b) habis dibagi 6 ATAU habis dibagi 8?

**Penyelesaian:**
```
(a) ⌊1000/6⌋ = 166

(b) Gunakan inklusi-eksklusi:
    |A ∪ B| = |A| + |B| - |A ∩ B|
    
    Kelipatan 6: ⌊1000/6⌋ = 166
    Kelipatan 8: ⌊1000/8⌋ = 125
    Kelipatan lcm(6,8) = kelipatan 24: ⌊1000/24⌋ = 41
    
    Jawaban = 166 + 125 - 41 = 250
```

### Contoh 12: Pangkat dalam Faktorial

**Soal:** Tentukan pangkat tertinggi dari 3 yang membagi 100!

**Penyelesaian:**
```
v_3(100!) = ⌊100/3⌋ + ⌊100/9⌋ + ⌊100/27⌋ + ⌊100/81⌋ + ⌊100/243⌋ + ...
          = 33 + 11 + 3 + 1 + 0 + ...
          = 48

Jawaban: 3^48 membagi 100!, tapi 3^49 tidak.
```

### Contoh 13: Bit Manipulation

**Soal:** Diberikan n = 92. Tentukan:
(a) Representasi biner
(b) Jumlah bit 1
(c) Apakah n pangkat 2?
(d) Bit ke-4 (dari kanan, mulai posisi 0)

**Penyelesaian:**
```
(a) 92 / 2 = 46 sisa 0
    46 / 2 = 23 sisa 0
    23 / 2 = 11 sisa 1
    11 / 2 = 5  sisa 1
    5  / 2 = 2  sisa 1
    2  / 2 = 1  sisa 0
    1  / 2 = 0  sisa 1
    92 = 1011100 (biner)

(b) Jumlah bit 1: 4 (ada empat angka 1 dalam 1011100)

(c) 92 & 91 = 1011100 & 1011011 = 1011000 ≠ 0
    Jadi 92 bukan pangkat 2.

(d) Bit ke-4: (92 >> 4) & 1 = (0000101) & 1 = 1
    Atau lihat langsung: 1011100, posisi dari kanan: 0011101
    Posisi: ...6543210
    Nilai:  1011100
    Bit ke-4 = 1
```

### Contoh 14: Modulo dalam Deret

**Soal:** Hitung (1^3 + 2^3 + 3^3 + ... + 10^3) mod 13.

**Penyelesaian:**
```
Rumus: 1^3 + 2^3 + ... + n^3 = [n(n+1)/2]^2

Untuk n = 10:
[10 × 11 / 2]^2 = 55^2 = 3025

3025 mod 13:
3025 / 13 = 232 sisa 9  (karena 232×13 = 3016, dan 3025-3016 = 9)

Jawaban: 9

Cara alternatif tanpa rumus:
55 mod 13 = 55 - 4×13 = 55 - 52 = 3
55^2 mod 13 = 3^2 mod 13 = 9 ✓
```

### Contoh 15: Extended GCD Application

**Soal:** Cari bilangan bulat x dan y sehingga 17x + 5y = 1.

**Penyelesaian:**
```
extGCD(17, 5):
  17 = 3×5 + 2  → extGCD(5, 2)
  5  = 2×2 + 1  → extGCD(2, 1)
  2  = 2×1 + 0  → extGCD(1, 0) → return (1, 1, 0)

Backtrack:
  extGCD(2, 1): g=1, x=0, y=1-2×0=1 → (1, 0, 1) → 2×0 + 1×1 = 1 ✓
  extGCD(5, 2): g=1, x=1, y=0-2×1=-2 → (1, 1, -2) → 5×1 + 2×(-2) = 1 ✓
  extGCD(17, 5): g=1, x=-2, y=1-3×(-2)=7 → (1, -2, 7) → 17×(-2) + 5×7 = -34+35 = 1 ✓

Jawaban: x = -2, y = 7
Verifikasi: 17×(-2) + 5×7 = -34 + 35 = 1 ✓
```

---

## 16. Soal Latihan

### Latihan Modulo
1. Hitung `17^50 mod 5` tanpa kalkulator.
2. Hitung `2^2026 mod 7`.
3. Hitung `(7^3 + 11^4) mod 13`.

### Latihan GCD/LCM
4. Hitung `gcd(252, 198)` menggunakan algoritma Euclidean.
5. Jika `gcd(a, 12) = 4` dan `lcm(a, 12) = 60`, tentukan a.

### Latihan Teori Bilangan
6. Berapa banyak bilangan 1..1000 yang relatif prima dengan 1000?
7. Berapa banyak pembagi positif dari 2025?
8. Berapa jumlah semua pembagi dari 100?

### Latihan Floor/Ceiling
9. Berapa banyak kelipatan 7 antara 100 dan 500 (inklusif)?
10. Berapa trailing zeros pada 200!?

### Latihan XOR/Biner
11. Hitung `1 XOR 2 XOR 3 XOR ... XOR 2026`.
12. Jika `a XOR b = 13` dan `a AND b = 6`, tentukan `a + b`.

### Latihan CRT
13. Cari bilangan terkecil positif yang jika dibagi 4 sisa 1, dibagi 5 sisa 2, dan dibagi 9 sisa 3.
14. Cari bilangan 3-digit terbesar yang habis dibagi 3, memberi sisa 2 jika dibagi 7.

### Latihan Campuran
15. Buktikan bahwa `n^5 - n` habis dibagi 30 untuk semua bilangan bulat n.

---

## 17. Pembahasan Ringkas Latihan

**Soal 1:** `17^50 mod 5`
```
17 mod 5 = 2
2^1 mod 5 = 2, 2^2 mod 5 = 4, 2^3 mod 5 = 3, 2^4 mod 5 = 1
Periode = 4. 50 mod 4 = 2.
17^50 mod 5 = 2^2 mod 5 = 4
```

**Soal 2:** `2^2026 mod 7`
```
Pola 2^n mod 7: 2, 4, 1, 2, 4, 1, ... (periode = 3)
2026 mod 3 = 2 (karena 2025 habis dibagi 3)
2^2026 mod 7 = 2^2 mod 7 = 4
```

**Soal 6:** Bilangan 1..1000 yang relatif prima dengan 1000
```
1000 = 2^3 × 5^3
φ(1000) = 1000 × (1-1/2) × (1-1/5) = 1000 × 1/2 × 4/5 = 400
```

**Soal 7:** Pembagi positif dari 2025
```
2025 = 45^2 = (3^2 × 5)^2 = 3^4 × 5^2
τ(2025) = (4+1)(2+1) = 15
```

**Soal 8:** Jumlah semua pembagi dari 100
```
100 = 2^2 × 5^2
σ(100) = [(2^3-1)/(2-1)] × [(5^3-1)/(5-1)]
       = [7/1] × [124/4]
       = 7 × 31 = 217
```

**Soal 10:** Trailing zeros pada 200!
```
v_5(200!) = ⌊200/5⌋ + ⌊200/25⌋ + ⌊200/125⌋ + ⌊200/625⌋
          = 40 + 8 + 1 + 0 = 49
```

**Soal 11:** `1 XOR 2 XOR ... XOR 2026`
```
2026 mod 4 = 2 → hasilnya = 2026 + 1 = 2027
```

**Soal 12:** Jika `a XOR b = 13` dan `a AND b = 6`, tentukan `a + b`.
```
Ingat: a + b = (a XOR b) + 2×(a AND b)
a + b = 13 + 2×6 = 13 + 12 = 25
```

---

## 18. Tips Mengerjakan Soal OSN tentang Modulo & Teori Bilangan

1. **Selalu reduksi modulo di setiap langkah** -- jangan biarkan bilangan membesar
2. **Cari pola berulang** -- untuk perpangkatan modular, pola selalu muncul
3. **Ingat Fermat's Little Theorem** -- sangat berguna jika modulus prima
4. **Gunakan rumus faktorisasi prima** -- untuk jumlah/sum pembagi
5. **Hafalkan aturan keterbagian** -- sering muncul di soal
6. **Untuk XOR, ingat pola n mod 4** -- menghindari perhitungan manual panjang
7. **Floor function = pembagian bulat** -- pikirkan dalam konteks coding
8. **Trailing zeros = v_5(n!)** -- hampir pasti muncul di OSN
9. **Perhatikan overflow di C++** -- gunakan `long long` jika diperlukan
10. **Jangan lupa +m saat pengurangan modulo** -- untuk menghindari hasil negatif

---

*Materi ini mencakup topik-topik yang paling sering muncul di OSK/OSP Informatika.
Pastikan untuk berlatih banyak soal agar terbiasa dengan pola-pola yang ada.*
