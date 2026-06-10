# Latihan 06 — Modulo dan Teori Bilangan

**Mata Pelajaran:** OSN Informatika 2026 — Bab 6  
**Jumlah Soal:** 40 soal  
**Tingkat Kesulitan:** Mudah (★), Sedang (★★), Sulit (★★★)  
**Tipe Soal:** Isian Singkat (IS), Pilihan Ganda (PG), Benar/Salah (B/S)  
**Referensi Materi:** [06-modulo-dan-teori-bilangan.md](../materi/06-modulo-dan-teori-bilangan.md)

---

## Bagian A: Operasi Modulo Dasar

---

### Soal 1 — Modulo Bilangan Positif ★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah nilai dari `137 mod 12`.

**Pembahasan:**

```
Langkah: Bagi 137 dengan 12, cari sisa.
137 / 12 = 11 sisa 5
Verifikasi: 12 x 11 = 132, dan 137 - 132 = 5

Jadi 137 mod 12 = 5
```

**Jawaban: 5**

---

### Soal 2 — Modulo dengan Bilangan Lebih Kecil ★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah nilai dari `7 mod 15`.

**Pembahasan:**

```
Jika pembilang lebih kecil dari pembagi:
7 < 15, maka 7 / 15 = 0 sisa 7

Jadi 7 mod 15 = 7
```

**Jawaban: 7**

---

### Soal 3 — Sifat Modulo dalam Penjumlahan ★

**Tipe:** Isian Singkat

**Soal:**  
Diketahui `a = 23` dan `b = 19`. Hitunglah `(a + b) mod 7`.

**Pembahasan:**

```
Cara langsung:
a + b = 23 + 19 = 42
42 mod 7 = 0 (karena 42 = 7 x 6)

Cara menggunakan sifat modulo:
(a + b) mod 7 = ((a mod 7) + (b mod 7)) mod 7
23 mod 7 = 2 (karena 23 = 7 x 3 + 2)
19 mod 7 = 5 (karena 19 = 7 x 2 + 5)
(2 + 5) mod 7 = 7 mod 7 = 0

Kedua cara menghasilkan jawaban yang sama.
```

**Jawaban: 0**

---

### Soal 4 — Sifat Modulo dalam Perkalian ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `(13 x 17) mod 5`.

**Pembahasan:**

```
Cara langsung:
13 x 17 = 221
221 mod 5 = 1 (karena 221 = 5 x 44 + 1)

Cara menggunakan sifat modulo:
(13 x 17) mod 5 = ((13 mod 5) x (17 mod 5)) mod 5
13 mod 5 = 3
17 mod 5 = 2
(3 x 2) mod 5 = 6 mod 5 = 1

Kedua cara menghasilkan jawaban yang sama.
```

**Jawaban: 1**

---

### Soal 5 — Modulo Berulang ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah sisa pembagian `2^10` oleh `7`.

**Pembahasan:**

```
2^10 = 1024
1024 / 7 = 146 sisa 2
Verifikasi: 7 x 146 = 1022, dan 1024 - 1022 = 2

Alternatif dengan sifat modulo bertahap:
2^1 mod 7 = 2
2^2 mod 7 = 4
2^3 mod 7 = 8 mod 7 = 1
2^4 mod 7 = (2^3 x 2) mod 7 = (1 x 2) mod 7 = 2
2^5 mod 7 = 4
2^6 mod 7 = 1
...
Pola berulang setiap 3: 2, 4, 1, 2, 4, 1, ...
2^10: 10 mod 3 = 1, jadi 2^10 mod 7 = 2^1 mod 7 = 2
```

**Jawaban: 2**

---

### Soal 6 — Digit Satuan ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan digit satuan dari `7^2024`.

**Pembahasan:**

```
Digit satuan = bilangan mod 10.
Cari pola 7^n mod 10:
7^1 mod 10 = 7
7^2 mod 10 = 49 mod 10 = 9
7^3 mod 10 = 343 mod 10 = 3
7^4 mod 10 = 2401 mod 10 = 1
7^5 mod 10 = 7 (kembali ke awal)

Pola berulang setiap 4: {7, 9, 3, 1}
2024 mod 4 = 0

Saat sisa = 0, kita ambil elemen ke-4 dari pola: 1
```

**Jawaban: 1**

---

### Soal 7 — Modulo dalam Kode C++ ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output program berikut:

```cpp
#include <iostream>
using namespace std;
int main() {
    int n = 12345;
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    cout << sum;
    return 0;
}
```

**Pembahasan:**

```
Program ini menghitung jumlah digit dari n = 12345.

Trace per iterasi:
| Iterasi | n     | n % 10 | sum | n / 10 |
|---------|-------|--------|-----|--------|
| 1       | 12345 | 5      | 5   | 1234   |
| 2       | 1234  | 4      | 9   | 123    |
| 3       | 123   | 3      | 12  | 12     |
| 4       | 12    | 2      | 14  | 1      |
| 5       | 1     | 1      | 15  | 0      |

Loop berhenti karena n = 0.
sum = 1 + 2 + 3 + 4 + 5 = 15
```

**Jawaban: 15**

---

## Bagian B: FPB dan KPK dengan Algoritma Euclidean

---

### Soal 8 — FPB dengan Algoritma Euclidean ★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah FPB(84, 36) menggunakan algoritma Euclidean.

**Pembahasan:**

```
Algoritma Euclidean: FPB(a, b) = FPB(b, a mod b) sampai b = 0.

FPB(84, 36):
  84 mod 36 = 12   -> FPB(36, 12)
  36 mod 12 = 0    -> FPB(12, 0)

Saat b = 0, FPB = a = 12.

Verifikasi:
84 = 2^2 x 3 x 7
36 = 2^2 x 3^2
FPB = 2^2 x 3 = 12 (benar)
```

**Jawaban: 12**

---

### Soal 9 — FPB Tiga Bilangan ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah FPB(120, 168, 72).

**Pembahasan:**

```
FPB tiga bilangan: FPB(a, b, c) = FPB(FPB(a, b), c)

Langkah 1: FPB(120, 168)
  120 mod 168: karena 120 < 168, tukar -> FPB(168, 120)
  168 mod 120 = 48   -> FPB(120, 48)
  120 mod 48 = 24    -> FPB(48, 24)
  48 mod 24 = 0      -> FPB(24, 0)
  FPB(120, 168) = 24

Langkah 2: FPB(24, 72)
  72 mod 24 = 0      -> FPB(24, 0)
  FPB(24, 72) = 24

Jadi FPB(120, 168, 72) = 24.

Verifikasi:
120 = 2^3 x 3 x 5
168 = 2^3 x 3 x 7
72  = 2^3 x 3^2
FPB = 2^3 x 3 = 24 (benar)
```

**Jawaban: 24**

---

### Soal 10 — KPK dari FPB ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah KPK(48, 180) menggunakan rumus KPK(a,b) = (a x b) / FPB(a,b).

**Pembahasan:**

```
Langkah 1: Cari FPB(48, 180) dengan Euclidean
  180 mod 48 = 36   -> FPB(48, 36)
  48 mod 36 = 12    -> FPB(36, 12)
  36 mod 12 = 0     -> FPB(12, 0)
  FPB(48, 180) = 12

Langkah 2: KPK = (48 x 180) / 12
  = 8640 / 12
  = 720

Verifikasi:
48 = 2^4 x 3
180 = 2^2 x 3^2 x 5
KPK = 2^4 x 3^2 x 5 = 16 x 9 x 5 = 720 (benar)
```

**Jawaban: 720**

---

### Soal 11 — Extended Euclidean ★★★

**Tipe:** Isian Singkat

**Soal:**  
Cari bilangan bulat x dan y sehingga `56x + 15y = FPB(56, 15)`.

**Pembahasan:**

```
Langkah 1: Euclidean biasa untuk cari FPB
  56 = 3 x 15 + 11
  15 = 1 x 11 + 4
  11 = 2 x 4  + 3
  4  = 1 x 3  + 1
  3  = 3 x 1  + 0
  FPB(56, 15) = 1

Langkah 2: Substitusi balik (Extended Euclidean)
  1 = 4 - 1 x 3
  1 = 4 - 1 x (11 - 2 x 4) = 3 x 4 - 1 x 11
  1 = 3 x (15 - 1 x 11) - 1 x 11 = 3 x 15 - 4 x 11
  1 = 3 x 15 - 4 x (56 - 3 x 15) = 15 x 15 - 4 x 56
  1 = (-4) x 56 + 15 x 15

Jadi x = -4 dan y = 15.

Verifikasi: 56 x (-4) + 15 x 15 = -224 + 225 = 1 (benar)
```

**Jawaban: x = -4, y = 15**

---

### Soal 12 — FPB dalam Program C++ ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}
int main() {
    cout << gcd(252, 105);
    return 0;
}
```

**Pembahasan:**

```
Trace fungsi gcd(252, 105):
| Iterasi | a   | b   | t   | a%b |
|---------|-----|-----|-----|-----|
| 1       | 252 | 105 | 105 | 42  |
| 2       | 105 | 42  | 42  | 21  |
| 3       | 42  | 21  | 21  | 0   |
| 4       | 21  | 0   | -   | -   |

Loop berhenti karena b = 0. Return a = 21.

Verifikasi:
252 = 2^2 x 3^2 x 7
105 = 3 x 5 x 7
FPB = 3 x 7 = 21 (benar)
```

**Jawaban: 21**

---

### Soal 13 — KPK Tiga Bilangan ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah KPK(12, 18, 20).

**Pembahasan:**

```
KPK(a, b, c) = KPK(KPK(a, b), c)

Langkah 1: KPK(12, 18)
  FPB(12, 18): 18 mod 12 = 6, 12 mod 6 = 0 -> FPB = 6
  KPK = (12 x 18) / 6 = 216 / 6 = 36

Langkah 2: KPK(36, 20)
  FPB(36, 20): 36 mod 20 = 16, 20 mod 16 = 4, 16 mod 4 = 0 -> FPB = 4
  KPK = (36 x 20) / 4 = 720 / 4 = 180

Verifikasi dengan faktorisasi prima:
12 = 2^2 x 3
18 = 2 x 3^2
20 = 2^2 x 5
KPK = 2^2 x 3^2 x 5 = 4 x 9 x 5 = 180 (benar)
```

**Jawaban: 180**

---

## Bagian C: Bilangan Prima dan Faktorisasi

---

### Soal 14 — Pengecekan Bilangan Prima ★

**Tipe:** Benar/Salah

**Soal:**  
Apakah 91 merupakan bilangan prima?

**Pembahasan:**

```
Untuk mengecek apakah 91 prima, cek keterbagian dengan bilangan prima
sampai sqrt(91) ~ 9.54. Cek: 2, 3, 5, 7.

91 / 2 = 45.5 (bukan bulat)
91 / 3 = 30.33... (bukan bulat)
91 / 5 = 18.2 (bukan bulat)
91 / 7 = 13 (bilangan bulat!)

91 = 7 x 13, jadi 91 BUKAN bilangan prima.
```

**Jawaban: Salah (91 bukan prima, 91 = 7 x 13)**

---

### Soal 15 — Faktorisasi Prima ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan faktorisasi prima dari 360.

**Pembahasan:**

```
Bagi berulang dengan bilangan prima terkecil:
360 / 2 = 180
180 / 2 = 90
90  / 2 = 45
45  / 3 = 15
15  / 3 = 5
5   / 5 = 1

Jadi 360 = 2^3 x 3^2 x 5

Verifikasi: 8 x 9 x 5 = 360 (benar)
```

**Jawaban: 2^3 x 3^2 x 5**

---

### Soal 16 — Jumlah Pembagi ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak pembagi positif dari 360?

**Pembahasan:**

```
Dari soal sebelumnya: 360 = 2^3 x 3^2 x 5^1

Rumus jumlah pembagi:
Jika n = p1^a1 x p2^a2 x ... x pk^ak
Maka jumlah pembagi = (a1+1)(a2+1)...(ak+1)

Jumlah pembagi 360 = (3+1)(2+1)(1+1) = 4 x 3 x 2 = 24

Daftar lengkap 24 pembagi:
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18,
20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360
```

**Jawaban: 24**

---

### Soal 17 — Jumlah Semua Pembagi ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah jumlah seluruh pembagi positif dari 28.

**Pembahasan:**

```
Faktorisasi: 28 = 2^2 x 7^1

Rumus jumlah seluruh pembagi (sigma function):
sigma(n) = (p1^(a1+1) - 1)/(p1 - 1) x (p2^(a2+1) - 1)/(p2 - 1) x ...

sigma(28) = (2^3 - 1)/(2 - 1) x (7^2 - 1)/(7 - 1)
          = (8 - 1)/1 x (49 - 1)/6
          = 7 x 8
          = 56

Verifikasi langsung:
Pembagi 28: 1, 2, 4, 7, 14, 28
Jumlah = 1 + 2 + 4 + 7 + 14 + 28 = 56 (benar)

Catatan: Karena sigma(28) = 2 x 28, maka 28 adalah bilangan sempurna!
```

**Jawaban: 56**

---

### Soal 18 — Sieve of Eratosthenes ★★

**Tipe:** Isian Singkat

**Soal:**  
Menggunakan Sieve of Eratosthenes, berapa banyak bilangan prima yang kurang dari atau sama dengan 50?

**Pembahasan:**

```
Mulai dengan daftar 2 sampai 50. Coret kelipatan setiap bilangan prima.

Langkah 1: Prima = 2. Coret kelipatan 2: 4,6,8,10,12,...,50
Langkah 2: Prima = 3. Coret kelipatan 3: 9,15,21,27,33,39,45
Langkah 3: Prima = 5. Coret kelipatan 5: 25,35
Langkah 4: Prima = 7. Coret kelipatan 7: 49
Langkah 5: sqrt(50) ~ 7.07, jadi cukup sampai 7.

Bilangan yang tersisa (prima):
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

Jumlah = 15 bilangan prima.
```

**Jawaban: 15**

---

### Soal 19 — Euler Totient ★★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah phi(36), yaitu banyaknya bilangan dari 1 sampai 36 yang relatif prima dengan 36.

**Pembahasan:**

```
Rumus Euler Totient:
phi(n) = n x (1 - 1/p1) x (1 - 1/p2) x ... untuk semua faktor prima pi dari n.

Faktorisasi: 36 = 2^2 x 3^2
Faktor prima: 2 dan 3

phi(36) = 36 x (1 - 1/2) x (1 - 1/3)
        = 36 x (1/2) x (2/3)
        = 36 x 1/3
        = 12

Verifikasi: Bilangan 1-36 yang relatif prima dengan 36:
1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35
Jumlah = 12 (benar)
```

**Jawaban: 12**

---

### Soal 20 — Trace Kode Prima ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
int main() {
    int count = 0;
    for (int i = 10; i <= 30; i++)
        if (isPrime(i)) count++;
    cout << count;
    return 0;
}
```

**Pembahasan:**

```
Program menghitung banyak bilangan prima dari 10 sampai 30.

Cek setiap bilangan:
10: 10%2=0, bukan prima
11: 2*2=4<=11, 11%2!=0; 3*3=9<=11, 11%3!=0; 4*4=16>11 -> PRIMA
12: 12%2=0, bukan prima
13: cek 2,3 -> PRIMA
14: 14%2=0, bukan prima
15: 15%3=0, bukan prima
16: 16%2=0, bukan prima
17: cek 2,3,4 -> PRIMA
18: 18%2=0, bukan prima
19: cek 2,3,4 -> PRIMA
20: 20%2=0, bukan prima
21: 21%3=0, bukan prima
22: 22%2=0, bukan prima
23: cek 2,3,4 -> PRIMA
24: 24%2=0, bukan prima
25: 25%5=0, bukan prima
26: 26%2=0, bukan prima
27: 27%3=0, bukan prima
28: 28%2=0, bukan prima
29: cek 2,3,4,5 -> PRIMA
30: 30%2=0, bukan prima

Prima: 11, 13, 17, 19, 23, 29 -> count = 6
```

**Jawaban: 6**

---

## Bagian D: Perpangkatan Modular dan Pola

---

### Soal 21 — Fast Exponentiation ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `3^13 mod 7` menggunakan metode fast exponentiation (repeated squaring).

**Pembahasan:**

```
Langkah 1: Tulis eksponen dalam biner
13 = 1101 (biner) = 8 + 4 + 1
Jadi 3^13 = 3^8 x 3^4 x 3^1

Langkah 2: Hitung pangkat 2 dari 3 mod 7
3^1 mod 7 = 3
3^2 mod 7 = 9 mod 7 = 2
3^4 mod 7 = (3^2)^2 mod 7 = 2^2 mod 7 = 4
3^8 mod 7 = (3^4)^2 mod 7 = 4^2 mod 7 = 16 mod 7 = 2

Langkah 3: Gabungkan
3^13 mod 7 = (3^8 x 3^4 x 3^1) mod 7
           = (2 x 4 x 3) mod 7
           = 24 mod 7
           = 3
```

**Jawaban: 3**

---

### Soal 22 — Pola Sisa Pembagian ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan sisa pembagian `5^100` oleh 3.

**Pembahasan:**

```
Cari pola 5^n mod 3:
5^1 mod 3 = 5 mod 3 = 2
5^2 mod 3 = 25 mod 3 = 1
5^3 mod 3 = 125 mod 3 = 2
5^4 mod 3 = 625 mod 3 = 1

Pola berulang setiap 2: {2, 1, 2, 1, ...}
- Jika n ganjil: 5^n mod 3 = 2
- Jika n genap: 5^n mod 3 = 1

Karena 100 genap, 5^100 mod 3 = 1.

Alternatif: 5 mod 3 = 2 = -1 (mod 3)
Jadi 5^100 mod 3 = (-1)^100 mod 3 = 1 mod 3 = 1.
```

**Jawaban: 1**

---

### Soal 23 — Fermat's Little Theorem ★★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `2^50 mod 13`.

**Pembahasan:**

```
Fermat's Little Theorem: Jika p prima dan gcd(a,p) = 1, maka a^(p-1) = 1 (mod p).

Karena 13 prima dan gcd(2, 13) = 1:
2^12 = 1 (mod 13)

Bagi 50 dengan 12:
50 = 12 x 4 + 2

Jadi:
2^50 = 2^(12x4 + 2) = (2^12)^4 x 2^2 = 1^4 x 4 = 4 (mod 13)
```

**Jawaban: 4**

---

### Soal 24 — Invers Modular ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan invers modular dari 3 modulo 11, yaitu bilangan x sehingga `3x mod 11 = 1`.

**Pembahasan:**

```
Metode 1: Coba satu-satu
3 x 1 = 3 mod 11 = 3
3 x 2 = 6 mod 11 = 6
3 x 3 = 9 mod 11 = 9
3 x 4 = 12 mod 11 = 1  <-- Ditemukan!

Metode 2: Fermat's Little Theorem
Karena 11 prima, invers dari a mod p = a^(p-2) mod p
3^(-1) mod 11 = 3^9 mod 11

3^1 mod 11 = 3
3^2 mod 11 = 9
3^4 mod 11 = 81 mod 11 = 4
3^8 mod 11 = 16 mod 11 = 5
3^9 = 3^8 x 3^1 = 5 x 3 = 15 mod 11 = 4

Metode 3: Extended Euclidean
11 = 3 x 3 + 2
3 = 1 x 2 + 1
1 = 3 - 1 x 2
1 = 3 - 1 x (11 - 3 x 3)
1 = 4 x 3 - 1 x 11
Jadi x = 4.
```

**Jawaban: 4**

---

### Soal 25 — Digit Terakhir Fibonacci ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan digit satuan dari bilangan Fibonacci ke-100 (F_100).

**Pembahasan:**

```
Digit satuan = F_n mod 10.
Pisano Period: Periode perulangan F_n mod m disebut pi(m).
Untuk m = 10, pi(10) = 60.

Karena 100 mod 60 = 40, maka F_100 mod 10 = F_40 mod 10.

Hitung F_n mod 10 dari F_1 sampai F_40:
F_1  = 1    F_11 = 9    F_21 = 6    F_31 = 9
F_2  = 1    F_12 = 4    F_22 = 7    F_32 = 0
F_3  = 2    F_13 = 3    F_23 = 3    F_33 = 9
F_4  = 3    F_14 = 7    F_24 = 0    F_34 = 9
F_5  = 5    F_15 = 0    F_25 = 3    F_35 = 8
F_6  = 8    F_16 = 7    F_26 = 3    F_36 = 7
F_7  = 3    F_17 = 7    F_27 = 6    F_37 = 5
F_8  = 1    F_18 = 4    F_28 = 9    F_38 = 2
F_9  = 4    F_19 = 1    F_29 = 5    F_39 = 7
F_10 = 5    F_20 = 5    F_30 = 4    F_40 = 9

F_40 mod 10 = 9, jadi digit satuan F_100 = 9.

(Catatan: F_40 = 102334155, digit terakhir = 5... 
Mari verifikasi: F_40 mod 10:
Menghitung ulang dari F_31:
F_31 mod 10: (F_29 + F_30) mod 10 = (5+4) mod 10 = 9
F_32 mod 10: (4+9) mod 10 = 3... 

Koreksi perhitungan:
F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=3, F_8=1, F_9=4, F_10=5
F_11=9, F_12=4, F_13=3, F_14=7, F_15=0, F_16=7, F_17=7, F_18=4, F_19=1, F_20=5
F_21=6, F_22=1, F_23=7, F_24=8, F_25=5, F_26=3, F_27=8, F_28=1, F_29=9, F_30=0
F_31=9, F_32=9, F_33=8, F_34=7, F_35=5, F_36=2, F_37=7, F_38=9, F_39=6, F_40=5

F_40 mod 10 = 5.
Jadi digit satuan F_100 = F_40 mod 10 = 5.
)
```

**Jawaban: 5**

---

### Soal 26 — Trace Power Mod ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int powermod(int base, int exp, int mod) {
    int result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1)
            result = (result * base) % mod;
        exp /= 2;
        base = (base * base) % mod;
    }
    return result;
}
int main() {
    cout << powermod(2, 20, 1000);
    return 0;
}
```

**Pembahasan:**

```
Trace powermod(2, 20, 1000):
base = 2, exp = 20, mod = 1000, result = 1

| Iterasi | exp | exp%2 | result         | exp/2 | base            |
|---------|-----|-------|----------------|-------|-----------------|
| 1       | 20  | 0     | 1 (tidak ubah) | 10    | 2*2=4           |
| 2       | 10  | 0     | 1 (tidak ubah) | 5     | 4*4=16          |
| 3       | 5   | 1     | 1*16=16        | 2     | 16*16=256       |
| 4       | 2   | 0     | 16 (tidak ubah)| 1     | 256*256=65536%1000=536 |
| 5       | 1   | 1     | 16*536=8576%1000=576 | 0 | 536*536=287296%1000=296|

exp = 0, loop berhenti. Return 576.

Verifikasi: 2^20 = 1048576. 1048576 mod 1000 = 576 (benar)
```

**Jawaban: 576**

---

## Bagian E: XOR dan Operasi Biner

---

### Soal 27 — XOR Dasar ★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `13 XOR 9` (dalam desimal).

**Pembahasan:**

```
Konversi ke biner:
13 = 1101
 9 = 1001

XOR bit per bit (1 jika berbeda, 0 jika sama):
  1 1 0 1
  1 0 0 1
  -------
  0 1 0 0

0100 (biner) = 4 (desimal)
```

**Jawaban: 4**

---

### Soal 28 — Sifat XOR ★★

**Tipe:** Isian Singkat

**Soal:**  
Diketahui array [3, 5, 3, 7, 5, 7, 9]. Semua elemen muncul genap kali kecuali satu. Tentukan elemen yang muncul ganjil kali menggunakan XOR.

**Pembahasan:**

```
Sifat XOR:
- a XOR a = 0 (elemen yang sama saling menghilangkan)
- a XOR 0 = a
- XOR bersifat komutatif dan asosiatif

XOR semua elemen:
3 XOR 5 XOR 3 XOR 7 XOR 5 XOR 7 XOR 9

Kelompokkan pasangan:
= (3 XOR 3) XOR (5 XOR 5) XOR (7 XOR 7) XOR 9
= 0 XOR 0 XOR 0 XOR 9
= 9
```

**Jawaban: 9**

---

### Soal 29 — Konversi Biner ke Desimal ★

**Tipe:** Isian Singkat

**Soal:**  
Konversikan bilangan biner `10110110` ke desimal.

**Pembahasan:**

```
Posisi bit (dari kanan): 7 6 5 4 3 2 1 0
Digit:                    1 0 1 1 0 1 1 0

Nilai = 1x2^7 + 0x2^6 + 1x2^5 + 1x2^4 + 0x2^3 + 1x2^2 + 1x2^1 + 0x2^0
     = 128 + 0 + 32 + 16 + 0 + 4 + 2 + 0
     = 182
```

**Jawaban: 182**

---

### Soal 30 — Operasi Bitwise AND dan OR ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `(25 AND 19)` dan `(25 OR 19)` dalam desimal.

**Pembahasan:**

```
Konversi ke biner (5 bit):
25 = 11001
19 = 10011

AND (1 jika keduanya 1):
  1 1 0 0 1
  1 0 0 1 1
  ---------
  1 0 0 0 1 = 17

OR (1 jika salah satu 1):
  1 1 0 0 1
  1 0 0 1 1
  ---------
  1 1 0 1 1 = 27

Verifikasi: a AND b + a OR b = a + b
17 + 27 = 44 = 25 + 19 (benar)
```

**Jawaban: 25 AND 19 = 17, 25 OR 19 = 27**

---

### Soal 31 — Shift dan Perkalian ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int main() {
    int a = 5;
    int b = a << 3;
    int c = b >> 1;
    cout << b << " " << c;
    return 0;
}
```

**Pembahasan:**

```
a = 5 = 00000101 (biner)

b = a << 3 (geser kiri 3 bit = kalikan 2^3 = 8)
  00000101 << 3 = 00101000 = 40
  Atau: 5 x 8 = 40

c = b >> 1 (geser kanan 1 bit = bagi 2)
  00101000 >> 1 = 00010100 = 20
  Atau: 40 / 2 = 20

Output: "40 20"
```

**Jawaban: 40 20**

---

### Soal 32 — Menghitung Bit 1 ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int main() {
    int n = 235;
    int count = 0;
    while (n > 0) {
        count += n & 1;
        n >>= 1;
    }
    cout << count;
    return 0;
}
```

**Pembahasan:**

```
Program menghitung jumlah bit 1 dalam representasi biner n.

235 dalam biner = 11101011

Trace:
| n (desimal) | n (biner)   | n & 1 | count | n >> 1   |
|-------------|-------------|-------|-------|----------|
| 235         | 11101011    | 1     | 1     | 01110101 |
| 117         | 01110101    | 1     | 2     | 00111010 |
| 58          | 00111010    | 0     | 2     | 00011101 |
| 29          | 00011101    | 1     | 3     | 00001110 |
| 14          | 00001110    | 0     | 3     | 00000111 |
| 7           | 00000111    | 1     | 4     | 00000011 |
| 3           | 00000011    | 1     | 5     | 00000001 |
| 1           | 00000001    | 1     | 6     | 00000000 |
| 0           | -           | -     | -     | -        |

235 = 11101011, jumlah bit 1 = 6.
```

**Jawaban: 6**

---

### Soal 33 — XOR Swap ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int main() {
    int a = 12, b = 7;
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    cout << a << " " << b;
    return 0;
}
```

**Pembahasan:**

```
XOR swap menukar dua variabel tanpa variabel sementara.

a = 12 = 1100, b = 7 = 0111

Langkah 1: a = a ^ b
  1100 XOR 0111 = 1011 = 11
  a = 11, b = 7

Langkah 2: b = a ^ b
  1011 XOR 0111 = 1100 = 12
  a = 11, b = 12

Langkah 3: a = a ^ b
  1011 XOR 1100 = 0111 = 7
  a = 7, b = 12

Hasil: a dan b tertukar! Output: "7 12"
```

**Jawaban: 7 12**

---

## Bagian F: Soal Campuran Teori Bilangan Gaya OSN

---

### Soal 34 — Chinese Remainder Theorem ★★★

**Tipe:** Isian Singkat

**Soal:**  
Cari bilangan terkecil x yang memenuhi:
- x mod 3 = 2
- x mod 5 = 3
- x mod 7 = 4

**Pembahasan:**

```
Metode: Coba bilangan yang memenuhi syarat pertama, lalu cek syarat lain.

Bilangan dengan x mod 3 = 2: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, ...

Cek x mod 5 = 3:
2 mod 5 = 2 (tidak)
5 mod 5 = 0 (tidak)
8 mod 5 = 3 (ya!) -> cek syarat ketiga
8 mod 7 = 1 (tidak)

Selanjutnya yang memenuhi x mod 3 = 2 DAN x mod 5 = 3:
Periode KPK(3,5) = 15, mulai dari 8: 8, 23, 38, 53, ...

Cek x mod 7 = 4:
8 mod 7 = 1 (tidak)
23 mod 7 = 2 (tidak)
38 mod 7 = 3 (tidak)
53 mod 7 = 4 (ya!)

Verifikasi x = 53:
53 mod 3 = 2 (53 = 17x3 + 2) benar
53 mod 5 = 3 (53 = 10x5 + 3) benar
53 mod 7 = 4 (53 = 7x7 + 4) benar
```

**Jawaban: 53**

---

### Soal 35 — Berapa Banyak Nol di Akhir Faktorial ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak angka nol di akhir 100! (100 faktorial)?

**Pembahasan:**

```
Angka nol di akhir n! ditentukan oleh banyaknya pasangan faktor 2 dan 5.
Karena faktor 2 selalu lebih banyak dari faktor 5, cukup hitung faktor 5.

Rumus Legendre:
Jumlah faktor p dalam n! = floor(n/p) + floor(n/p^2) + floor(n/p^3) + ...

Untuk p = 5 dan n = 100:
floor(100/5)   = 20
floor(100/25)  = 4
floor(100/125) = 0

Total = 20 + 4 = 24

Jadi 100! berakhiran 24 angka nol.
```

**Jawaban: 24**

---

### Soal 36 — Kongruensi Linear ★★★

**Tipe:** Isian Singkat

**Soal:**  
Cari semua solusi x (0 <= x < 12) dari kongruensi `4x = 8 (mod 12)`.

**Pembahasan:**

```
Langkah 1: Cek apakah solusi ada.
FPB(4, 12) = 4
Karena 4 | 8 (4 habis membagi 8), solusi ada.
Jumlah solusi = FPB(4, 12) = 4 solusi dalam rentang [0, 12).

Langkah 2: Sederhanakan.
Bagi semua dengan FPB = 4:
x = 2 (mod 3)

Langkah 3: Solusi umum x = 2 (mod 3)
Dalam rentang [0, 12): x = 2, 5, 8, 11

Verifikasi:
4 x 2 = 8, 8 mod 12 = 8 (benar)
4 x 5 = 20, 20 mod 12 = 8 (benar)
4 x 8 = 32, 32 mod 12 = 8 (benar)
4 x 11 = 44, 44 mod 12 = 8 (benar)
```

**Jawaban: x = 2, 5, 8, 11**

---

### Soal 37 — Teorema Wilson ★★★

**Tipe:** Benar/Salah

**Soal:**  
Apakah `(16! + 1)` habis dibagi 17?

**Pembahasan:**

```
Teorema Wilson: Jika p prima, maka (p-1)! = -1 (mod p)
Atau equivalen: (p-1)! + 1 = 0 (mod p)

Karena 17 adalah bilangan prima:
16! = -1 (mod 17)
16! + 1 = 0 (mod 17)

Artinya 17 | (16! + 1), yaitu (16! + 1) habis dibagi 17.
```

**Jawaban: Benar**

---

### Soal 38 — Representasi dalam Basis Lain ★★

**Tipe:** Isian Singkat

**Soal:**  
Konversikan bilangan desimal 255 ke basis 16 (heksadesimal).

**Pembahasan:**

```
Bagi berulang dengan 16:
255 / 16 = 15 sisa 15 (F)
15  / 16 = 0  sisa 15 (F)

Baca sisa dari bawah ke atas: FF

Verifikasi: F x 16 + F = 15 x 16 + 15 = 240 + 15 = 255 (benar)

Representasi digit heksadesimal:
0-9 = 0-9
10 = A, 11 = B, 12 = C, 13 = D, 14 = E, 15 = F
```

**Jawaban: FF (hex)**

---

### Soal 39 — Sistem Bilangan Campuran ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa nilai dari `(1A3)_16 + (1011)_2` dalam desimal?

**Pembahasan:**

```
Langkah 1: Konversi (1A3)_16 ke desimal
1A3 (hex) = 1 x 16^2 + A x 16^1 + 3 x 16^0
          = 1 x 256 + 10 x 16 + 3 x 1
          = 256 + 160 + 3
          = 419

Langkah 2: Konversi (1011)_2 ke desimal
1011 (biner) = 1 x 2^3 + 0 x 2^2 + 1 x 2^1 + 1 x 2^0
            = 8 + 0 + 2 + 1
            = 11

Langkah 3: Jumlahkan
419 + 11 = 430
```

**Jawaban: 430**

---

### Soal 40 — Soal Cerita Modulo ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tiga alarm berbunyi bersamaan pada pukul 06:00 pagi. Alarm pertama berbunyi setiap 8 menit, alarm kedua setiap 12 menit, dan alarm ketiga setiap 18 menit. Pada pukul berapa ketiga alarm akan berbunyi bersamaan lagi untuk yang pertama kalinya?

**Pembahasan:**

```
Langkah 1: Cari KPK(8, 12, 18)

KPK(8, 12):
  FPB(8, 12): 12 mod 8 = 4, 8 mod 4 = 0 -> FPB = 4
  KPK(8, 12) = (8 x 12) / 4 = 96 / 4 = 24

KPK(24, 18):
  FPB(24, 18): 24 mod 18 = 6, 18 mod 6 = 0 -> FPB = 6
  KPK(24, 18) = (24 x 18) / 6 = 432 / 6 = 72

Langkah 2: Konversi ke jam dan menit
72 menit = 1 jam 12 menit

Langkah 3: Tambah ke waktu awal
06:00 + 1 jam 12 menit = 07:12

Verifikasi:
72 / 8 = 9 (alarm 1 sudah bunyi 9 kali)
72 / 12 = 6 (alarm 2 sudah bunyi 6 kali)
72 / 18 = 4 (alarm 3 sudah bunyi 4 kali)
Semua bilangan bulat, benar.
```

**Jawaban: Pukul 07:12**

---

### Soal 41 — Pangkat Modular Besar ★★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `7^222 mod 11`.

**Pembahasan:**

```
Gunakan Fermat's Little Theorem.
Karena 11 prima dan gcd(7, 11) = 1:
7^10 = 1 (mod 11)

222 = 10 x 22 + 2
Jadi 7^222 = (7^10)^22 x 7^2 = 1^22 x 49 = 49 mod 11

49 mod 11 = 5 (karena 49 = 4 x 11 + 5)
```

**Jawaban: 5**

---

### Soal 42 — Bilangan Sempurna ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int main() {
    int count = 0;
    for (int n = 2; n <= 500; n++) {
        int sum = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                sum += i;
                if (i != n / i) sum += n / i;
            }
        }
        if (sum == n) count++;
    }
    cout << count;
    return 0;
}
```

**Pembahasan:**

```
Program menghitung bilangan sempurna dari 2 sampai 500.
Bilangan sempurna: jumlah pembagi selain dirinya = bilangan itu sendiri.

Bilangan sempurna yang diketahui sampai 500:
- 6: pembagi = 1, 2, 3. Jumlah = 1+2+3 = 6 (sempurna)
- 28: pembagi = 1, 2, 4, 7, 14. Jumlah = 1+2+4+7+14 = 28 (sempurna)
- 496: pembagi = 1, 2, 4, 8, 16, 31, 62, 124, 248. 
  Jumlah = 1+2+4+8+16+31+62+124+248 = 496 (sempurna)

Jadi count = 3.
```

**Jawaban: 3**

---

### Soal 43 — XOR Kumulatif ★★

**Tipe:** Isian Singkat

**Soal:**  
Hitunglah `1 XOR 2 XOR 3 XOR 4 XOR ... XOR 15`.

**Pembahasan:**

```
Ada pola untuk XOR dari 1 sampai n:
- Jika n mod 4 == 0: hasilnya n
- Jika n mod 4 == 1: hasilnya 1
- Jika n mod 4 == 2: hasilnya n + 1
- Jika n mod 4 == 3: hasilnya 0

n = 15, dan 15 mod 4 = 3, jadi hasilnya = 0.

Verifikasi manual (kelompok per 4):
1 XOR 2 XOR 3 XOR 4 = (1^2)^(3^4) = 3^7 = ... 
Lebih mudah:
XOR(1..4): 
  1 = 001, 2 = 010, 3 = 011, 4 = 100
  1^2 = 011(3), 3^3 = 000(0), 0^4 = 100(4) -> XOR(1..4) = 4... 

Koreksi menggunakan pola:
4 mod 4 = 0 -> XOR(1..4) = 4
8 mod 4 = 0 -> XOR(1..8) = 8
12 mod 4 = 0 -> XOR(1..12) = 12
15 mod 4 = 3 -> XOR(1..15) = 0

Verifikasi XOR(1..12) kemudian XOR dengan 13,14,15:
XOR(1..12) = 12 = 1100
12 XOR 13: 1100 ^ 1101 = 0001 = 1
1 XOR 14: 0001 ^ 1110 = 1111 = 15
15 XOR 15: 1111 ^ 1111 = 0000 = 0

Jadi XOR(1..15) = 0.
```

**Jawaban: 0**

---

### Soal 44 — Kriptografi Caesar Cipher ★★

**Tipe:** Isian Singkat

**Soal:**  
Dalam Caesar Cipher dengan kunci k = 5, huruf digeser 5 posisi ke kanan dalam alfabet. Jika plaintext adalah "OSNINFORMATIKA", apa huruf ke-4 dari ciphertext?

**Pembahasan:**

```
Caesar Cipher: C = (P + k) mod 26, dimana A=0, B=1, ..., Z=25

Plaintext: O S N I N F O R M A T I K A
Huruf ke-4 dari plaintext: I

I = posisi 8 (karena A=0, B=1, ..., I=8)
C = (8 + 5) mod 26 = 13 mod 26 = 13
Posisi 13 = N

Verifikasi seluruh ciphertext:
O(14)->T(19), S(18)->X(23), N(13)->S(18), I(8)->N(13), ...

Huruf ke-4 dari ciphertext = N.
```

**Jawaban: N**

---

### Soal 45 — Fungsi Totient dalam Program ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari program berikut:

```cpp
#include <iostream>
using namespace std;
int phi(int n) {
    int result = n;
    for (int p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}
int main() {
    cout << phi(30);
    return 0;
}
```

**Pembahasan:**

```
Trace phi(30):
n = 30, result = 30

p = 2: 30 % 2 == 0 -> masuk
  while: 30/2=15, 15%2!=0 -> keluar. n = 15
  result -= result/2 -> result = 30 - 15 = 15

p = 3: 15 % 3 == 0 -> masuk
  while: 15/3=5, 5%3!=0 -> keluar. n = 5
  result -= result/3 -> result = 15 - 5 = 10

p = 4: 4*4=16 > 5, keluar loop

n = 5 > 1:
  result -= result/5 -> result = 10 - 2 = 8

Return 8.

Verifikasi: phi(30) = 30 x (1-1/2) x (1-1/3) x (1-1/5)
= 30 x 1/2 x 2/3 x 4/5 = 30 x 8/30 = 8 (benar)
```

**Jawaban: 8**

---

## Ringkasan Jawaban

| No | Jawaban |
|----|---------|
| 1  | 5 |
| 2  | 7 |
| 3  | 0 |
| 4  | 1 |
| 5  | 2 |
| 6  | 1 |
| 7  | 15 |
| 8  | 12 |
| 9  | 24 |
| 10 | 720 |
| 11 | x = -4, y = 15 |
| 12 | 21 |
| 13 | 180 |
| 14 | Salah (91 = 7 x 13) |
| 15 | 2^3 x 3^2 x 5 |
| 16 | 24 |
| 17 | 56 |
| 18 | 15 |
| 19 | 12 |
| 20 | 6 |
| 21 | 3 |
| 22 | 1 |
| 23 | 4 |
| 24 | 4 |
| 25 | 5 |
| 26 | 576 |
| 27 | 4 |
| 28 | 9 |
| 29 | 182 |
| 30 | AND=17, OR=27 |
| 31 | 40 20 |
| 32 | 6 |
| 33 | 7 12 |
| 34 | 53 |
| 35 | 24 |
| 36 | 2, 5, 8, 11 |
| 37 | Benar |
| 38 | FF |
| 39 | 430 |
| 40 | Pukul 07:12 |
| 41 | 5 |
| 42 | 3 |
| 43 | 0 |
| 44 | N |
| 45 | 8 |
