# Latihan 05 — Algoritma Dasar & Trace Kode C++

**Mata Pelajaran:** OSN Informatika 2026 — Bab 5  
**Jumlah Soal:** 36 soal  
**Tingkat Kesulitan:** Mudah (★), Sedang (★★), Sulit (★★★)  
**Tipe Soal:** Isian Singkat (IS), Pilihan Ganda (PG), Benar/Salah (B/S)  
**Referensi Materi:** [05-algoritma-dasar-cpp.md](../materi/05-algoritma-dasar-cpp.md)

---

## Bagian A: Trace Perulangan Sederhana (Loop)

---

### Soal 1 — For Loop dengan Akumulator ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int s = 0;
    for (int i = 1; i <= 8; i++) {
        if (i % 3 == 0)
            s += i;
    }
    cout << s;
    return 0;
}
```

**Pembahasan:**

```
Trace variabel per iterasi:

| i | i % 3 == 0? | Aksi      | s  |
|---|-------------|-----------|-----|
| 1 | 1%3=1, Tidak | -        | 0  |
| 2 | 2%3=2, Tidak | -        | 0  |
| 3 | 3%3=0, Ya    | s += 3   | 3  |
| 4 | 4%3=1, Tidak | -        | 3  |
| 5 | 5%3=2, Tidak | -        | 3  |
| 6 | 6%3=0, Ya    | s += 6   | 9  |
| 7 | 7%3=1, Tidak | -        | 9  |
| 8 | 8%3=2, Tidak | -        | 9  |

Loop selesai (i=9, tidak memenuhi i<=8).
```

**Jawaban: 9**

(Menjumlahkan bilangan kelipatan 3 dari 1 sampai 8, yaitu 3 + 6 = 9)

---

### Soal 2 — While Loop Decrement ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 100;
    int count = 0;
    while (x > 1) {
        x = x / 2;
        count++;
    }
    cout << count << " " << x;
    return 0;
}
```

**Pembahasan:**

```
Trace variabel per iterasi:

| Iterasi | x (awal) | x = x/2 | count |
|---------|----------|----------|-------|
| 1       | 100      | 50       | 1     |
| 2       | 50       | 25       | 2     |
| 3       | 25       | 12       | 3     |
| 4       | 12       | 6        | 4     |
| 5       | 6        | 3        | 5     |
| 6       | 3        | 1        | 6     |

Setelah iterasi 6: x = 1, kondisi x > 1 sudah false, keluar loop.
```

**Jawaban: 6 1**

---

### Soal 3 — For Loop dengan Break ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int total = 0;
    for (int i = 1; i <= 20; i++) {
        total += i;
        if (total > 15) break;
    }
    cout << total << " " << i;
    return 0;
}
```

**Catatan:** Kode di atas memiliki error kompilasi. Variabel `i` dideklarasikan di dalam for loop sehingga tidak dapat diakses di luar loop.

Berikut versi yang benar:

```cpp
#include <iostream>
using namespace std;

int main() {
    int total = 0;
    int i;
    for (i = 1; i <= 20; i++) {
        total += i;
        if (total > 15) break;
    }
    cout << total << " " << i;
    return 0;
}
```

**Pembahasan:**

```
Trace:

| i | total += i | total | total > 15? |
|---|-----------|-------|-------------|
| 1 | 0 + 1    | 1     | Tidak       |
| 2 | 1 + 2    | 3     | Tidak       |
| 3 | 3 + 3    | 6     | Tidak       |
| 4 | 6 + 4    | 10    | Tidak       |
| 5 | 10 + 5   | 15    | Tidak       |
| 6 | 15 + 6   | 21    | Ya -> break |

Keluar loop saat i = 6, total = 21.
```

**Jawaban: 21 6**

---

### Soal 4 — For Loop dengan Continue ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int s = 0;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) continue;
        if (i > 7) continue;
        s += i;
    }
    cout << s;
    return 0;
}
```

**Pembahasan:**

```
Trace:

| i  | i%2==0? | i>7? | Aksi     | s  |
|----|---------|------|----------|-----|
| 1  | Tidak   | Tidak | s += 1  | 1  |
| 2  | Ya      | -     | continue | 1  |
| 3  | Tidak   | Tidak | s += 3  | 4  |
| 4  | Ya      | -     | continue | 4  |
| 5  | Tidak   | Tidak | s += 5  | 9  |
| 6  | Ya      | -     | continue | 9  |
| 7  | Tidak   | Tidak | s += 7  | 16 |
| 8  | Ya      | -     | continue | 16 |
| 9  | Tidak   | Ya    | continue | 16 |
| 10 | Ya      | -     | continue | 16 |

Hanya bilangan ganjil yang <= 7 yang ditambahkan: 1+3+5+7 = 16.
```

**Jawaban: 16**

---

### Soal 5 — Do-While Loop ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 1234;
    int jumlah = 0;
    do {
        jumlah += n % 10;
        n /= 10;
    } while (n > 0);
    cout << jumlah;
    return 0;
}
```

**Pembahasan:**

```
Trace (menjumlahkan digit-digit dari 1234):

| Iterasi | n (awal) | n % 10 | jumlah | n /= 10 |
|---------|----------|--------|--------|----------|
| 1       | 1234     | 4      | 4      | 123      |
| 2       | 123      | 3      | 7      | 12       |
| 3       | 12       | 2      | 9      | 1        |
| 4       | 1        | 1      | 10     | 0        |

Setelah iterasi 4: n = 0, kondisi n > 0 false, keluar loop.
Jumlah digit: 4 + 3 + 2 + 1 = 10.
```

**Jawaban: 10**

---

### Soal 6 — Loop Bersarang Akumulator ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int result = 0;
    for (int i = 1; i <= 4; i++) {
        for (int j = i; j <= 4; j++) {
            result += i * j;
        }
    }
    cout << result;
    return 0;
}
```

**Pembahasan:**

```
Trace:

| i | j        | Nilai i*j yang ditambahkan | result |
|---|----------|---------------------------|--------|
| 1 | 1,2,3,4  | 1*1=1, 1*2=2, 1*3=3, 1*4=4 | 0+1+2+3+4 = 10 |
| 2 | 2,3,4    | 2*2=4, 2*3=6, 2*4=8       | 10+4+6+8 = 28 |
| 3 | 3,4      | 3*3=9, 3*4=12             | 28+9+12 = 49 |
| 4 | 4        | 4*4=16                    | 49+16 = 65 |

Total = 65.
```

**Jawaban: 65**

---

## Bagian B: Trace Manipulasi Array

---

### Soal 7 — Pencarian Maksimum ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {3, 7, 2, 9, 4, 6, 1, 8};
    int n = 8;
    int maks = arr[0];
    int idx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] > maks) {
            maks = arr[i];
            idx = i;
        }
    }
    cout << maks << " " << idx;
    return 0;
}
```

**Pembahasan:**

```
Trace:

| i | arr[i] | arr[i] > maks? | maks | idx |
|---|--------|---------------|------|-----|
| - | -      | (inisialisasi) | 3   | 0   |
| 1 | 7      | 7 > 3? Ya     | 7    | 1   |
| 2 | 2      | 2 > 7? Tidak  | 7    | 1   |
| 3 | 9      | 9 > 7? Ya     | 9    | 3   |
| 4 | 4      | 4 > 9? Tidak  | 9    | 3   |
| 5 | 6      | 6 > 9? Tidak  | 9    | 3   |
| 6 | 1      | 1 > 9? Tidak  | 9    | 3   |
| 7 | 8      | 8 > 9? Tidak  | 9    | 3   |
```

**Jawaban: 9 3**

(Elemen terbesar adalah 9, berada di indeks 3)

---

### Soal 8 — Array Reversal ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

**Pembahasan:**

```
n/2 = 2 (integer division), sehingga loop berjalan untuk i = 0, 1.

Trace:
| i | Tukar arr[i] dengan arr[n-1-i] | Array setelah swap  |
|---|--------------------------------|---------------------|
| 0 | arr[0]=10 <-> arr[4]=50       | [50, 20, 30, 40, 10] |
| 1 | arr[1]=20 <-> arr[3]=40       | [50, 40, 30, 20, 10] |

arr[2] = 30 tidak di-swap (elemen tengah tetap).
```

**Jawaban: 50 40 30 20 10**

(Array dibalik/reverse)

---

### Soal 9 — Frekuensi Elemen ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {2, 5, 2, 3, 5, 2, 3, 5, 5};
    int n = 9;
    int freq[10] = {0};
    
    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }
    
    int modaVal = 0, modaFreq = 0;
    for (int i = 0; i < 10; i++) {
        if (freq[i] > modaFreq) {
            modaFreq = freq[i];
            modaVal = i;
        }
    }
    cout << modaVal << " " << modaFreq;
    return 0;
}
```

**Pembahasan:**

```
Langkah 1: Hitung frekuensi setiap elemen
  arr = {2, 5, 2, 3, 5, 2, 3, 5, 5}

  freq[2] = 3  (muncul di indeks 0, 2, 5)
  freq[3] = 2  (muncul di indeks 3, 6)
  freq[5] = 4  (muncul di indeks 1, 4, 7, 8)
  Sisanya = 0

Langkah 2: Cari frekuensi tertinggi (moda)
  | i | freq[i] | freq[i] > modaFreq? | modaVal | modaFreq |
  |---|---------|---------------------|---------|----------|
  | 0 | 0       | 0 > 0? Tidak        | 0       | 0        |
  | 1 | 0       | 0 > 0? Tidak        | 0       | 0        |
  | 2 | 3       | 3 > 0? Ya           | 2       | 3        |
  | 3 | 2       | 2 > 3? Tidak        | 2       | 3        |
  | 4 | 0       | 0 > 3? Tidak        | 2       | 3        |
  | 5 | 4       | 4 > 3? Ya           | 5       | 4        |
  | 6-9 | 0     | Tidak               | 5       | 4        |
```

**Jawaban: 5 4**

(Angka 5 muncul paling sering, yaitu 4 kali)

---

### Soal 10 — Prefix Sum Array ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {3, 1, 4, 1, 5, 9};
    int n = 6;
    int prefix[6];
    
    prefix[0] = arr[0];
    for (int i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] + arr[i];
    }
    
    // Jumlah elemen indeks 2 sampai 4
    int hasil = prefix[4] - prefix[1];
    cout << hasil;
    return 0;
}
```

**Pembahasan:**

```
Langkah 1: Bangun prefix sum array

| i | arr[i] | prefix[i]             |
|---|--------|-----------------------|
| 0 | 3      | 3                     |
| 1 | 1      | 3 + 1 = 4            |
| 2 | 4      | 4 + 4 = 8            |
| 3 | 1      | 8 + 1 = 9            |
| 4 | 5      | 9 + 5 = 14           |
| 5 | 9      | 14 + 9 = 23          |

prefix = {3, 4, 8, 9, 14, 23}

Langkah 2: Hitung jumlah elemen indeks 2 sampai 4
  hasil = prefix[4] - prefix[1] = 14 - 4 = 10

Verifikasi: arr[2] + arr[3] + arr[4] = 4 + 1 + 5 = 10 ✓
```

**Jawaban: 10**

---

### Soal 11 — Pergeseran Array (Shift) ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    int last = arr[n-1];
    
    for (int i = n-1; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = last;
    
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

**Pembahasan:**

```
Langkah 1: Simpan elemen terakhir
  last = arr[4] = 50

Langkah 2: Geser semua elemen ke kanan satu posisi (dari belakang)

| i | arr[i] = arr[i-1]    | Array                    |
|---|---------------------|--------------------------|
| 4 | arr[4] = arr[3] = 40 | [10, 20, 30, 40, 40]   |
| 3 | arr[3] = arr[2] = 30 | [10, 20, 30, 30, 40]   |
| 2 | arr[2] = arr[1] = 20 | [10, 20, 20, 30, 40]   |
| 1 | arr[1] = arr[0] = 10 | [10, 10, 20, 30, 40]   |

Langkah 3: Tempatkan last di posisi 0
  arr[0] = 50: [50, 10, 20, 30, 40]
```

**Jawaban: 50 10 20 30 40**

(Right rotation: elemen terakhir pindah ke depan)

---

### Soal 12 — Array 2D: Jumlah Kolom ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int mat[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    
    int maxCol = 0, maxSum = 0;
    for (int j = 0; j < 4; j++) {
        int colSum = 0;
        for (int i = 0; i < 3; i++) {
            colSum += mat[i][j];
        }
        if (colSum > maxSum) {
            maxSum = colSum;
            maxCol = j;
        }
    }
    cout << maxCol << " " << maxSum;
    return 0;
}
```

**Pembahasan:**

```
Hitung jumlah setiap kolom:

| j (kolom) | mat[0][j] + mat[1][j] + mat[2][j] | colSum |
|-----------|-----------------------------------|--------|
| 0         | 1 + 5 + 9                         | 15     |
| 1         | 2 + 6 + 10                        | 18     |
| 2         | 3 + 7 + 11                        | 21     |
| 3         | 4 + 8 + 12                        | 24     |

Trace pencarian maksimum:
| j | colSum | colSum > maxSum? | maxCol | maxSum |
|---|--------|-----------------|--------|--------|
| 0 | 15     | 15 > 0? Ya      | 0      | 15     |
| 1 | 18     | 18 > 15? Ya     | 1      | 18     |
| 2 | 21     | 21 > 18? Ya     | 2      | 21     |
| 3 | 24     | 24 > 21? Ya     | 3      | 24     |
```

**Jawaban: 3 24**

(Kolom ke-3 (indeks 3) memiliki jumlah terbesar yaitu 24)

---

## Bagian C: Trace Rekursi

---

### Soal 13 — Rekursi Faktorial ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int faktorial(int n) {
    if (n <= 1) return 1;
    return n * faktorial(n - 1);
}

int main() {
    cout << faktorial(6);
    return 0;
}
```

**Pembahasan:**

```
Trace pemanggilan rekursif (call stack):

faktorial(6) = 6 * faktorial(5)
  faktorial(5) = 5 * faktorial(4)
    faktorial(4) = 4 * faktorial(3)
      faktorial(3) = 3 * faktorial(2)
        faktorial(2) = 2 * faktorial(1)
          faktorial(1) = 1  [BASE CASE]
        return 2 * 1 = 2
      return 3 * 2 = 6
    return 4 * 6 = 24
  return 5 * 24 = 120
return 6 * 120 = 720
```

**Jawaban: 720**

---

### Soal 14 — Rekursi Jumlah Digit ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int jumlahDigit(int n) {
    if (n < 10) return n;
    return (n % 10) + jumlahDigit(n / 10);
}

int main() {
    cout << jumlahDigit(9471);
    return 0;
}
```

**Pembahasan:**

```
Trace:

jumlahDigit(9471) = (9471 % 10) + jumlahDigit(9471 / 10)
                   = 1 + jumlahDigit(947)
  jumlahDigit(947) = (947 % 10) + jumlahDigit(947 / 10)
                    = 7 + jumlahDigit(94)
    jumlahDigit(94) = (94 % 10) + jumlahDigit(94 / 10)
                     = 4 + jumlahDigit(9)
      jumlahDigit(9) = 9  [BASE CASE: n < 10]
    return 4 + 9 = 13
  return 7 + 13 = 20
return 1 + 20 = 21

Verifikasi: 9 + 4 + 7 + 1 = 21 ✓
```

**Jawaban: 21**

---

### Soal 15 — Rekursi Fibonacci ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    for (int i = 0; i <= 7; i++) {
        cout << fib(i) << " ";
    }
    return 0;
}
```

**Pembahasan:**

```
Hitung satu per satu:

fib(0) = 0  [base case]
fib(1) = 1  [base case]
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(4) = fib(3) + fib(2) = 2 + 1 = 3
fib(5) = fib(4) + fib(3) = 3 + 2 = 5
fib(6) = fib(5) + fib(4) = 5 + 3 = 8
fib(7) = fib(6) + fib(5) = 8 + 5 = 13

Output: 0 1 1 2 3 5 8 13
```

**Jawaban: 0 1 1 2 3 5 8 13**

---

### Soal 16 — Rekursi Power (Pangkat) ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int power(int base, int exp) {
    if (exp == 0) return 1;
    if (exp % 2 == 0) {
        int half = power(base, exp / 2);
        return half * half;
    }
    return base * power(base, exp - 1);
}

int main() {
    cout << power(2, 10);
    return 0;
}
```

**Pembahasan:**

```
Trace (fast exponentiation):

power(2, 10): exp=10 genap -> half = power(2, 5), return half*half
  power(2, 5): exp=5 ganjil -> return 2 * power(2, 4)
    power(2, 4): exp=4 genap -> half = power(2, 2), return half*half
      power(2, 2): exp=2 genap -> half = power(2, 1), return half*half
        power(2, 1): exp=1 ganjil -> return 2 * power(2, 0)
          power(2, 0): exp=0 -> return 1  [BASE CASE]
        return 2 * 1 = 2
      half = 2, return 2 * 2 = 4
    half = 4, return 4 * 4 = 16
  return 2 * 16 = 32
half = 32, return 32 * 32 = 1024
```

**Jawaban: 1024**

(2^10 = 1024, dihitung dengan metode fast exponentiation)

---

### Soal 17 — Rekursi dengan Cetak ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

void mystery(int n) {
    if (n <= 0) return;
    cout << n << " ";
    mystery(n - 2);
    cout << n << " ";
}

int main() {
    mystery(5);
    return 0;
}
```

**Pembahasan:**

```
Trace (perhatikan cetak terjadi SEBELUM dan SESUDAH pemanggilan rekursif):

mystery(5):
  cetak 5 -> "5 "
  panggil mystery(3)
    mystery(3):
      cetak 3 -> "3 "
      panggil mystery(1)
        mystery(1):
          cetak 1 -> "1 "
          panggil mystery(-1)
            mystery(-1): n <= 0, return
          cetak 1 -> "1 "
      cetak 3 -> "3 "
  cetak 5 -> "5 "

Urutan cetak: 5 3 1 1 3 5
```

**Jawaban: 5 3 1 1 3 5**

(Pola palindrom karena ada print sebelum dan sesudah rekursi)

---

### Soal 18 — Rekursi GCD (Euclidean) ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    int a = 252, b = 105;
    cout << gcd(a, b);
    return 0;
}
```

**Pembahasan:**

```
Trace algoritma Euclidean:

gcd(252, 105): b != 0 -> gcd(105, 252 % 105) = gcd(105, 42)
  gcd(105, 42): b != 0 -> gcd(42, 105 % 42) = gcd(42, 21)
    gcd(42, 21): b != 0 -> gcd(21, 42 % 21) = gcd(21, 0)
      gcd(21, 0): b == 0 -> return 21  [BASE CASE]
    return 21
  return 21
return 21

Verifikasi: 252 = 21 * 12, 105 = 21 * 5, GCD = 21 ✓
```

**Jawaban: 21**

---

## Bagian D: Trace Algoritma Sorting

---

### Soal 19 — Bubble Sort Lengkap ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan array `arr = {6, 3, 8, 2, 7}`. Setelah menjalankan Bubble Sort secara lengkap (ascending), berapa kali pertukaran (swap) dilakukan? Tuliskan juga kondisi array setelah pass pertama.

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

**Pembahasan:**

```
Array awal: [6, 3, 8, 2, 7]

Pass i=0 (j: 0..3):
  j=0: 6 > 3? Ya, tukar -> [3, 6, 8, 2, 7]  (swap 1)
  j=1: 6 > 8? Tidak
  j=2: 8 > 2? Ya, tukar -> [3, 6, 2, 8, 7]  (swap 2)
  j=3: 8 > 7? Ya, tukar -> [3, 6, 2, 7, 8]  (swap 3)
  Setelah pass 1: [3, 6, 2, 7, 8]

Pass i=1 (j: 0..2):
  j=0: 3 > 6? Tidak
  j=1: 6 > 2? Ya, tukar -> [3, 2, 6, 7, 8]  (swap 4)
  j=2: 6 > 7? Tidak
  Setelah pass 2: [3, 2, 6, 7, 8]

Pass i=2 (j: 0..1):
  j=0: 3 > 2? Ya, tukar -> [2, 3, 6, 7, 8]  (swap 5)
  j=1: 3 > 6? Tidak
  Setelah pass 3: [2, 3, 6, 7, 8]

Pass i=3 (j: 0..0):
  j=0: 2 > 3? Tidak
  Setelah pass 4: [2, 3, 6, 7, 8]

Array akhir: [2, 3, 6, 7, 8]
```

**Jawaban: 5 kali swap. Setelah pass pertama: [3, 6, 2, 7, 8]**

---

### Soal 20 — Selection Sort Trace ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan array `arr = {5, 1, 4, 2, 8}`. Tuliskan kondisi array setelah setiap pass dari Selection Sort (ascending).

```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
}
```

**Pembahasan:**

```
Array awal: [5, 1, 4, 2, 8]

Pass i=0: Cari minimum dari indeks 0..4
  minIdx=0(5), j=1: 1<5 -> minIdx=1
  j=2: 4<1? Tidak
  j=3: 2<1? Tidak
  j=4: 8<1? Tidak
  Tukar arr[0] dan arr[1]: [1, 5, 4, 2, 8]

Pass i=1: Cari minimum dari indeks 1..4
  minIdx=1(5), j=2: 4<5 -> minIdx=2
  j=3: 2<4 -> minIdx=3
  j=4: 8<2? Tidak
  Tukar arr[1] dan arr[3]: [1, 2, 4, 5, 8]

Pass i=2: Cari minimum dari indeks 2..4
  minIdx=2(4), j=3: 5<4? Tidak
  j=4: 8<4? Tidak
  minIdx=2 sama dengan i, swap tidak mengubah apa-apa: [1, 2, 4, 5, 8]

Pass i=3: Cari minimum dari indeks 3..4
  minIdx=3(5), j=4: 8<5? Tidak
  Tidak ada perubahan: [1, 2, 4, 5, 8]

Array akhir: [1, 2, 4, 5, 8]
```

**Jawaban:**  
- Setelah pass 1: [1, 5, 4, 2, 8]  
- Setelah pass 2: [1, 2, 4, 5, 8]  
- Setelah pass 3: [1, 2, 4, 5, 8]  
- Setelah pass 4: [1, 2, 4, 5, 8]

---

### Soal 21 — Insertion Sort Trace ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan array `arr = {7, 3, 5, 1, 9, 2}`. Tuliskan kondisi array setelah setiap pass dari Insertion Sort.

```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

**Pembahasan:**

```
Array awal: [7, 3, 5, 1, 9, 2]

Pass i=1: key = 3
  j=0: arr[0]=7 > 3? Ya -> geser: [7, 7, 5, 1, 9, 2], j=-1
  arr[0] = 3: [3, 7, 5, 1, 9, 2]

Pass i=2: key = 5
  j=1: arr[1]=7 > 5? Ya -> geser: [3, 7, 7, 1, 9, 2], j=0
  j=0: arr[0]=3 > 5? Tidak -> berhenti
  arr[1] = 5: [3, 5, 7, 1, 9, 2]

Pass i=3: key = 1
  j=2: arr[2]=7 > 1? Ya -> geser: [3, 5, 7, 7, 9, 2], j=1
  j=1: arr[1]=5 > 1? Ya -> geser: [3, 5, 5, 7, 9, 2], j=0
  j=0: arr[0]=3 > 1? Ya -> geser: [3, 3, 5, 7, 9, 2], j=-1
  arr[0] = 1: [1, 3, 5, 7, 9, 2]

Pass i=4: key = 9
  j=3: arr[3]=7 > 9? Tidak -> berhenti
  arr[4] = 9: [1, 3, 5, 7, 9, 2]

Pass i=5: key = 2
  j=4: arr[4]=9 > 2? Ya -> geser: [1, 3, 5, 7, 9, 9], j=3
  j=3: arr[3]=7 > 2? Ya -> geser: [1, 3, 5, 7, 7, 9], j=2
  j=2: arr[2]=5 > 2? Ya -> geser: [1, 3, 5, 5, 7, 9], j=1
  j=1: arr[1]=3 > 2? Ya -> geser: [1, 3, 3, 5, 7, 9], j=0
  j=0: arr[0]=1 > 2? Tidak -> berhenti
  arr[1] = 2: [1, 2, 3, 5, 7, 9]

Array akhir: [1, 2, 3, 5, 7, 9]
```

**Jawaban:**  
- Setelah pass 1: [3, 7, 5, 1, 9, 2]  
- Setelah pass 2: [3, 5, 7, 1, 9, 2]  
- Setelah pass 3: [1, 3, 5, 7, 9, 2]  
- Setelah pass 4: [1, 3, 5, 7, 9, 2]  
- Setelah pass 5: [1, 2, 3, 5, 7, 9]

---

### Soal 22 — Sorting Parsial ★★

**Tipe:** Pilihan Ganda

**Soal:**  
Diberikan array `arr = {9, 4, 7, 2, 6, 1}`. Jika dilakukan **3 pass pertama** dari Bubble Sort (ascending), apa kondisi array setelahnya?

A. [2, 4, 1, 6, 7, 9]  
B. [2, 1, 4, 6, 7, 9]  
C. [1, 2, 4, 6, 7, 9]  
D. [4, 2, 1, 6, 7, 9]  

**Pembahasan:**

```
Array awal: [9, 4, 7, 2, 6, 1]

Pass i=0 (j: 0..4):
  j=0: 9>4? Ya -> [4, 9, 7, 2, 6, 1]
  j=1: 9>7? Ya -> [4, 7, 9, 2, 6, 1]
  j=2: 9>2? Ya -> [4, 7, 2, 9, 6, 1]
  j=3: 9>6? Ya -> [4, 7, 2, 6, 9, 1]
  j=4: 9>1? Ya -> [4, 7, 2, 6, 1, 9]

Pass i=1 (j: 0..3):
  j=0: 4>7? Tidak
  j=1: 7>2? Ya -> [4, 2, 7, 6, 1, 9]
  j=2: 7>6? Ya -> [4, 2, 6, 7, 1, 9]
  j=3: 7>1? Ya -> [4, 2, 6, 1, 7, 9]

Pass i=2 (j: 0..2):
  j=0: 4>2? Ya -> [2, 4, 6, 1, 7, 9]
  j=1: 4>6? Tidak
  j=2: 6>1? Ya -> [2, 4, 1, 6, 7, 9]
```

**Jawaban: A. [2, 4, 1, 6, 7, 9]**

---

### Soal 23 — Binary Search Trace ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan array terurut `arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}` (n=10). Lakukan binary search untuk mencari nilai 23. Berapa kali perbandingan dilakukan?

```cpp
int binarySearch(int arr[], int n, int target) {
    int lo = 0, hi = n - 1;
    int cmp = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        cmp++;
        if (arr[mid] == target) return cmp;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

**Pembahasan:**

```
arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
target = 23

Iterasi 1: lo=0, hi=9, mid=(0+9)/2=4
  arr[4] = 16, 16 == 23? Tidak. 16 < 23 -> lo = 5
  cmp = 1

Iterasi 2: lo=5, hi=9, mid=(5+9)/2=7
  arr[7] = 56, 56 == 23? Tidak. 56 > 23 -> hi = 6
  cmp = 2

Iterasi 3: lo=5, hi=6, mid=(5+6)/2=5
  arr[5] = 23, 23 == 23? Ya! Ditemukan!
  cmp = 3

Jumlah perbandingan = 3.
```

**Jawaban: 3 kali perbandingan**

---

### Soal 24 — Counting Sort ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = 7;
    int count[10] = {0};
    
    for (int i = 0; i < n; i++)
        count[arr[i]]++;
    
    int idx = 0;
    for (int i = 0; i < 10; i++) {
        while (count[i] > 0) {
            arr[idx] = i;
            idx++;
            count[i]--;
        }
    }
    
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

**Pembahasan:**

```
Langkah 1: Hitung frekuensi setiap elemen
  arr = {4, 2, 2, 8, 3, 3, 1}
  count[1] = 1
  count[2] = 2
  count[3] = 2
  count[4] = 1
  count[8] = 1

Langkah 2: Rekonstruksi array berdasarkan count[]
  i=0: count[0]=0, skip
  i=1: count[1]=1, tulis arr[0]=1, idx=1
  i=2: count[2]=2, tulis arr[1]=2, arr[2]=2, idx=3
  i=3: count[3]=2, tulis arr[3]=3, arr[4]=3, idx=5
  i=4: count[4]=1, tulis arr[5]=4, idx=6
  i=5..7: count=0, skip
  i=8: count[8]=1, tulis arr[6]=8, idx=7
  i=9: count=0, skip

Array akhir: [1, 2, 2, 3, 3, 4, 8]
```

**Jawaban: 1 2 2 3 3 4 8**

---

## Bagian E: Trace Nested Loop dan Pola

---

### Soal 25 — Pola Segitiga Angka ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Trace per baris:

| i | j berjalan 1..i | Output baris |
|---|-----------------|--------------|
| 1 | j=1             | 1            |
| 2 | j=1,2           | 12           |
| 3 | j=1,2,3         | 123          |
| 4 | j=1,2,3,4       | 1234         |
| 5 | j=1,2,3,4,5     | 12345        |
```

**Jawaban:**
```
1
12
123
1234
12345
```

---

### Soal 26 — Pola Segitiga Terbalik ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2*i - 1; j++) {
            cout << "*";
        }
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Trace per baris:

| i | Spasi (n-i) | Bintang (2*i-1) | Output               |
|---|-------------|-----------------|----------------------|
| 4 | 0 spasi     | 7 bintang       | *******              |
| 3 | 1 spasi     | 5 bintang       |  *****               |
| 2 | 2 spasi     | 3 bintang       |   ***                |
| 1 | 3 spasi     | 1 bintang       |    *                 |
```

**Jawaban:**
```
*******
 *****
  ***
   *
```

---

### Soal 27 — Pola Diamond Angka ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 3;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << j;
        for (int j = i - 1; j >= 1; j--) cout << j;
        cout << "\n";
    }
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << j;
        for (int j = i - 1; j >= 1; j--) cout << j;
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Bagian atas (i = 1 sampai 3):

| i | Spasi (n-i) | Naik (1..i) | Turun (i-1..1) | Output |
|---|-------------|-------------|----------------|--------|
| 1 | 2 spasi     | "1"         | (kosong)       |   1    |
| 2 | 1 spasi     | "12"        | "1"            |  121   |
| 3 | 0 spasi     | "123"       | "21"           | 12321  |

Bagian bawah (i = 2 sampai 1):

| i | Spasi (n-i) | Naik (1..i) | Turun (i-1..1) | Output |
|---|-------------|-------------|----------------|--------|
| 2 | 1 spasi     | "12"        | "1"            |  121   |
| 1 | 2 spasi     | "1"         | (kosong)       |   1    |
```

**Jawaban:**
```
  1
 121
12321
 121
  1
```

---

### Soal 28 — Nested Loop Perkalian ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        int val = 1;
        for (int j = 1; j <= i; j++) {
            cout << val << " ";
            val = val * (i - j) / j;
        }
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Ini menghasilkan segitiga Pascal (tiap baris = koefisien binomial).

Baris i=1:
  j=1: cetak val=1, val = 1*(1-1)/1 = 0
  Output: "1 "

Baris i=2:
  j=1: cetak val=1, val = 1*(2-1)/1 = 1
  j=2: cetak val=1, val = 1*(2-2)/2 = 0
  Output: "1 1 "

Baris i=3:
  j=1: cetak val=1, val = 1*(3-1)/1 = 2
  j=2: cetak val=2, val = 2*(3-2)/2 = 1
  j=3: cetak val=1, val = 1*(3-3)/3 = 0
  Output: "1 2 1 "

Baris i=4:
  j=1: cetak val=1, val = 1*(4-1)/1 = 3
  j=2: cetak val=3, val = 3*(4-2)/2 = 3
  j=3: cetak val=3, val = 3*(4-3)/3 = 1
  j=4: cetak val=1, val = 1*(4-4)/4 = 0
  Output: "1 3 3 1 "
```

**Jawaban:**
```
1 
1 1 
1 2 1 
1 3 3 1 
```

---

### Soal 29 — Nested Loop dengan Kondisi Kompleks ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || i == n-1 || j == 0 || j == n-1)
                cout << "* ";
            else
                cout << "  ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Kondisi mencetak '*': baris pertama (i=0), baris terakhir (i=4),
kolom pertama (j=0), atau kolom terakhir (j=4).
Ini membentuk bingkai/frame persegi.

| i\j | 0   | 1   | 2   | 3   | 4   |
|-----|-----|-----|-----|-----|-----|
| 0   | *   | *   | *   | *   | *   | (i=0, cetak semua)
| 1   | *   |     |     |     | *   | (j=0 dan j=4)
| 2   | *   |     |     |     | *   | (j=0 dan j=4)
| 3   | *   |     |     |     | *   | (j=0 dan j=4)
| 4   | *   | *   | *   | *   | *   | (i=4, cetak semua)
```

**Jawaban:**
```
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

---

### Soal 30 — Spiral Pattern ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    int mat[4][4] = {0};
    int val = 1;
    int top = 0, bottom = n-1, left = 0, right = n-1;
    
    while (val <= n*n) {
        for (int j = left; j <= right && val <= n*n; j++)
            mat[top][j] = val++;
        top++;
        for (int i = top; i <= bottom && val <= n*n; i++)
            mat[i][right] = val++;
        right--;
        for (int j = right; j >= left && val <= n*n; j--)
            mat[bottom][j] = val++;
        bottom--;
        for (int i = bottom; i >= top && val <= n*n; i--)
            mat[i][left] = val++;
        left++;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] < 10) cout << " ";
            cout << mat[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Pembahasan:**

```
Algoritma mengisi matriks secara spiral (searah jarum jam).

Langkah-langkah pengisian:
1. Baris atas (kiri ke kanan): 1, 2, 3, 4
2. Kolom kanan (atas ke bawah): 5, 6, 7
3. Baris bawah (kanan ke kiri): 8, 9, 10
4. Kolom kiri (bawah ke atas): 11, 12
5. Baris atas berikutnya: 13, 14
6. Kolom kanan berikutnya: 15
7. Baris bawah berikutnya: 16

Matriks hasil:
| Baris\Kolom | 0  | 1  | 2  | 3  |
|-------------|----|----|----|----|
| 0           | 1  | 2  | 3  | 4  |
| 1           | 12 | 13 | 14 | 5  |
| 2           | 11 | 16 | 15 | 6  |
| 3           | 10 | 9  | 8  | 7  |
```

**Jawaban:**
```
 1  2  3  4 
12 13 14  5 
11 16 15  6 
10  9  8  7 
```

---

## Bagian F: Trace Fungsi Kompleks dan Multi-Fungsi

---

### Soal 31 — Pass by Reference ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

void proses(int &a, int b, int &c) {
    a = a + b;
    b = b * 2;
    c = a + b;
}

int main() {
    int x = 3, y = 4, z = 0;
    proses(x, y, z);
    cout << x << " " << y << " " << z;
    return 0;
}
```

**Pembahasan:**

```
Pemanggilan: proses(x, y, z)
  - a adalah REFERENSI ke x (perubahan a mengubah x)
  - b adalah SALINAN dari y (perubahan b tidak mengubah y)
  - c adalah REFERENSI ke z (perubahan c mengubah z)

Trace di dalam fungsi:
  Awal: a=3 (&x), b=4 (salinan), c=0 (&z)
  
  a = a + b = 3 + 4 = 7    -> x menjadi 7
  b = b * 2 = 4 * 2 = 8    -> y TIDAK berubah (b hanya salinan)
  c = a + b = 7 + 8 = 15   -> z menjadi 15

Kembali ke main():
  x = 7 (berubah, pass by reference)
  y = 4 (tidak berubah, pass by value)
  z = 15 (berubah, pass by reference)
```

**Jawaban: 7 4 15**

---

### Soal 32 — Fungsi Rekursif Saling Memanggil ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int fungsiB(int n);

int fungsiA(int n) {
    if (n <= 0) return 1;
    return n + fungsiB(n - 1);
}

int fungsiB(int n) {
    if (n <= 0) return 0;
    return n * fungsiA(n - 1);
}

int main() {
    cout << fungsiA(3);
    return 0;
}
```

**Pembahasan:**

```
Trace:

fungsiA(3): n=3, n>0 -> return 3 + fungsiB(2)
  fungsiB(2): n=2, n>0 -> return 2 * fungsiA(1)
    fungsiA(1): n=1, n>0 -> return 1 + fungsiB(0)
      fungsiB(0): n=0, n<=0 -> return 0  [BASE CASE]
    return 1 + 0 = 1
  return 2 * 1 = 2
return 3 + 2 = 5
```

**Jawaban: 5**

---

### Soal 33 — Fungsi dengan Array Parameter ★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int prosesArray(int arr[], int n) {
    int hasil = 0;
    for (int i = 0; i < n; i++) {
        arr[i] = arr[i] * 2;
        hasil += arr[i];
    }
    return hasil;
}

int main() {
    int data[] = {1, 2, 3, 4, 5};
    int total = prosesArray(data, 5);
    cout << total << "\n";
    for (int i = 0; i < 5; i++)
        cout << data[i] << " ";
    return 0;
}
```

**Pembahasan:**

```
Array dilewatkan ke fungsi secara reference (otomatis untuk array di C++).
Artinya perubahan di dalam fungsi MENGUBAH array asli.

Trace di dalam prosesArray:
| i | arr[i] (awal) | arr[i] = arr[i]*2 | hasil += arr[i] | hasil |
|---|---------------|-------------------|-----------------|-------|
| 0 | 1             | 2                 | 0 + 2           | 2     |
| 1 | 2             | 4                 | 2 + 4           | 6     |
| 2 | 3             | 6                 | 6 + 6           | 12    |
| 3 | 4             | 8                 | 12 + 8          | 20    |
| 4 | 5             | 10                | 20 + 10         | 30    |

Return 30.

Kembali ke main():
  total = 30
  data[] sekarang = {2, 4, 6, 8, 10} (sudah dimodifikasi)
```

**Jawaban:**
```
30
2 4 6 8 10
```

---

### Soal 34 — Multi-Fungsi dengan Operator Bitwise ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int countBits(int n) {
    int count = 0;
    while (n > 0) {
        count += (n & 1);
        n >>= 1;
    }
    return count;
}

int transform(int x) {
    return (x << 1) | 1;
}

int main() {
    int a = 5;
    int b = transform(a);
    int c = countBits(b);
    cout << b << " " << c;
    return 0;
}
```

**Pembahasan:**

```
Langkah 1: transform(5)
  a = 5 = 0101 (biner)
  x << 1 = 0101 << 1 = 1010 = 10
  (x << 1) | 1 = 1010 | 0001 = 1011 = 11
  b = 11

Langkah 2: countBits(11)
  11 = 1011 (biner), hitung jumlah bit 1:

  | Iterasi | n (biner) | n & 1 | count | n >>= 1 |
  |---------|-----------|-------|-------|----------|
  | 1       | 1011      | 1     | 1     | 0101     |
  | 2       | 0101      | 1     | 2     | 0010     |
  | 3       | 0010      | 0     | 2     | 0001     |
  | 4       | 0001      | 1     | 3     | 0000     |

  n = 0, keluar loop. count = 3.
  c = 3
```

**Jawaban: 11 3**

---

### Soal 35 — Fungsi String Kompleks ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
#include <string>
using namespace std;

string encode(string s) {
    string result = "";
    int i = 0;
    while (i < s.length()) {
        int count = 1;
        while (i + count < s.length() && s[i + count] == s[i]) {
            count++;
        }
        if (count > 1) {
            result += to_string(count);
        }
        result += s[i];
        i += count;
    }
    return result;
}

int main() {
    cout << encode("aaabbbccddddde");
    return 0;
}
```

**Pembahasan:**

```
Ini adalah algoritma Run-Length Encoding (RLE).
String input: "aaabbbccddddde"

Trace:
| i | s[i] | count | count > 1? | result ditambah        | result        |
|---|------|-------|------------|------------------------|---------------|
| 0 | 'a'  | 3     | Ya         | "3" + "a"              | "3a"          |
| 3 | 'b'  | 3     | Ya         | "3" + "b"              | "3a3b"        |
| 6 | 'c'  | 2     | Ya         | "2" + "c"              | "3a3b2c"      |
| 8 | 'd'  | 5     | Ya         | "5" + "d"              | "3a3b2c5d"    |
| 13| 'e'  | 1     | Tidak      | "e" (tanpa angka)      | "3a3b2c5de"   |

Detail penghitungan count:
- i=0: s[0]='a', s[1]='a', s[2]='a', s[3]='b' -> count=3
- i=3: s[3]='b', s[4]='b', s[5]='b', s[6]='c' -> count=3
- i=6: s[6]='c', s[7]='c', s[8]='d' -> count=2
- i=8: s[8]='d', s[9]='d', s[10]='d', s[11]='d', s[12]='d', s[13]='e' -> count=5
- i=13: s[13]='e', s[14] tidak ada -> count=1
```

**Jawaban: 3a3b2c5de**

---

### Soal 36 — Multi-Fungsi Rekursif dengan Memoization ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int memo[100] = {0};
int callCount = 0;

int solve(int n) {
    callCount++;
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    memo[n] = solve(n - 1) + solve(n - 2);
    return memo[n];
}

int main() {
    int hasil = solve(7);
    cout << hasil << " " << callCount;
    return 0;
}
```

**Pembahasan:**

```
Ini adalah Fibonacci dengan memoization.
Setiap kali fungsi dipanggil, callCount bertambah.
Jika memo[n] sudah diisi, langsung return (tidak rekursi lagi).

Trace pemanggilan:
solve(7): callCount=1, memo[7]=0 -> solve(6) + solve(5)
  solve(6): callCount=2, memo[6]=0 -> solve(5) + solve(4)
    solve(5): callCount=3, memo[5]=0 -> solve(4) + solve(3)
      solve(4): callCount=4, memo[4]=0 -> solve(3) + solve(2)
        solve(3): callCount=5, memo[3]=0 -> solve(2) + solve(1)
          solve(2): callCount=6, memo[2]=0 -> solve(1) + solve(0)
            solve(1): callCount=7, return 1
            solve(0): callCount=8, return 0
          memo[2] = 1, return 1
          solve(1): callCount=9, return 1
        memo[3] = 1 + 1 = 2, return 2
        solve(2): callCount=10, memo[2]=1 != 0, return 1
      memo[4] = 2 + 1 = 3, return 3
      solve(3): callCount=11, memo[3]=2 != 0, return 2
    memo[5] = 3 + 2 = 5, return 5
    solve(4): callCount=12, memo[4]=3 != 0, return 3
  memo[6] = 5 + 3 = 8, return 8
  solve(5): callCount=13, memo[5]=5 != 0, return 5
memo[7] = 8 + 5 = 13, return 13

hasil = 13
callCount = 13
```

**Jawaban: 13 13**

(Fibonacci ke-7 = 13, jumlah pemanggilan fungsi = 13. Bandingkan tanpa memoization yang memerlukan 41 pemanggilan!)

---

## Soal Bonus: Kombinasi Konsep

---

### Soal 37 — Sieve of Eratosthenes ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut (berapa bilangan prima yang dicetak):

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 30;
    bool sieve[31];
    for (int i = 0; i <= n; i++) sieve[i] = true;
    sieve[0] = sieve[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= n; j += i) {
                sieve[j] = false;
            }
        }
    }
    
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (sieve[i]) {
            cout << i << " ";
            count++;
        }
    }
    cout << "\n" << count;
    return 0;
}
```

**Pembahasan:**

```
Algoritma Sieve of Eratosthenes untuk mencari bilangan prima <= 30.

Loop utama: i dari 2 sampai sqrt(30) ≈ 5

i=2 (prima): coret kelipatan mulai 4: 4,6,8,10,12,14,16,18,20,22,24,26,28,30
i=3 (prima): coret kelipatan mulai 9: 9,12,15,18,21,24,27,30
i=4 (sudah dicoret): skip
i=5 (prima): coret kelipatan mulai 25: 25,30

Bilangan yang tersisa (prima):
2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Jumlah = 10 bilangan prima.
```

**Jawaban:**
```
2 3 5 7 11 13 17 19 23 29 
10
```

---

### Soal 38 — Stack Simulasi dengan Array ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int stack[100];
int top = -1;

void push(int val) {
    top++;
    stack[top] = val;
}

int pop() {
    int val = stack[top];
    top--;
    return val;
}

int peek() {
    return stack[top];
}

int main() {
    push(10);
    push(20);
    push(30);
    cout << pop() << " ";
    push(40);
    cout << peek() << " ";
    cout << pop() << " ";
    cout << pop() << " ";
    cout << top;
    return 0;
}
```

**Pembahasan:**

```
Trace operasi stack (LIFO - Last In, First Out):

| Operasi   | Stack (bawah->atas) | top | Output |
|-----------|--------------------|----|--------|
| push(10)  | [10]               | 0  |        |
| push(20)  | [10, 20]           | 1  |        |
| push(30)  | [10, 20, 30]       | 2  |        |
| pop()     | [10, 20]           | 1  | 30     |
| push(40)  | [10, 20, 40]       | 2  |        |
| peek()    | [10, 20, 40]       | 2  | 40     |
| pop()     | [10, 20]           | 1  | 40     |
| pop()     | [10]               | 0  | 20     |

Output terakhir: top = 0
```

**Jawaban: 30 40 40 20 0**

---

### Soal 39 — Konversi Basis dengan Rekursi ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

void toBinary(int n) {
    if (n == 0) return;
    toBinary(n / 2);
    cout << n % 2;
}

int toDecimal(string bin) {
    int result = 0;
    for (int i = 0; i < bin.length(); i++) {
        result = result * 2 + (bin[i] - '0');
    }
    return result;
}

int main() {
    cout << "Bin: ";
    toBinary(42);
    cout << "\nDec: " << toDecimal("110101");
    return 0;
}
```

**Pembahasan:**

```
Bagian 1: toBinary(42) - konversi 42 ke biner secara rekursif

Trace rekursi (masuk):
  toBinary(42): 42/2=21, panggil toBinary(21)
    toBinary(21): 21/2=10, panggil toBinary(10)
      toBinary(10): 10/2=5, panggil toBinary(5)
        toBinary(5): 5/2=2, panggil toBinary(2)
          toBinary(2): 2/2=1, panggil toBinary(1)
            toBinary(1): 1/2=0, panggil toBinary(0)
              toBinary(0): n==0, return [BASE CASE]
            cetak 1%2 = 1
          cetak 2%2 = 0
        cetak 5%2 = 1
      cetak 10%2 = 0
    cetak 21%2 = 1
  cetak 42%2 = 0

Output pertama: 101010 (42 dalam biner)

Bagian 2: toDecimal("110101")
  | i | bin[i] | result = result*2 + digit |
  |---|--------|--------------------------|
  | 0 | '1'    | 0*2 + 1 = 1             |
  | 1 | '1'    | 1*2 + 1 = 3             |
  | 2 | '0'    | 3*2 + 0 = 6             |
  | 3 | '1'    | 6*2 + 1 = 13            |
  | 4 | '0'    | 13*2 + 0 = 26           |
  | 5 | '1'    | 26*2 + 1 = 53           |

Verifikasi: 110101 = 32+16+4+1 = 53 ✓
```

**Jawaban:**
```
Bin: 101010
Dec: 53
```

---

### Soal 40 — Merge Two Sorted Arrays ★★★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan output dari kode berikut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[] = {1, 4, 7, 10, 13};
    int b[] = {2, 5, 6, 9, 11, 15};
    int na = 5, nb = 6;
    int c[11];
    
    int i = 0, j = 0, k = 0;
    while (i < na && j < nb) {
        if (a[i] <= b[j]) {
            c[k] = a[i];
            i++;
        } else {
            c[k] = b[j];
            j++;
        }
        k++;
    }
    while (i < na) { c[k] = a[i]; i++; k++; }
    while (j < nb) { c[k] = b[j]; j++; k++; }
    
    for (int x = 0; x < k; x++)
        cout << c[x] << " ";
    return 0;
}
```

**Pembahasan:**

```
Merge dua array terurut menjadi satu array terurut.

Trace:
| Step | a[i] | b[j] | Pilih | c[k]   | i | j | k |
|------|------|------|-------|--------|---|---|---|
| 1    | 1    | 2    | a[0]=1 | c[0]=1 | 1 | 0 | 1 |
| 2    | 4    | 2    | b[0]=2 | c[1]=2 | 1 | 1 | 2 |
| 3    | 4    | 5    | a[1]=4 | c[2]=4 | 2 | 1 | 3 |
| 4    | 7    | 5    | b[1]=5 | c[3]=5 | 2 | 2 | 4 |
| 5    | 7    | 6    | b[2]=6 | c[4]=6 | 2 | 3 | 5 |
| 6    | 7    | 9    | a[2]=7 | c[5]=7 | 3 | 3 | 6 |
| 7    | 10   | 9    | b[3]=9 | c[6]=9 | 3 | 4 | 7 |
| 8    | 10   | 11   | a[3]=10| c[7]=10| 4 | 4 | 8 |
| 9    | 13   | 11   | b[4]=11| c[8]=11| 4 | 5 | 9 |
| 10   | 13   | 15   | a[4]=13| c[9]=13| 5 | 5 | 10|

i=5 (habis), salin sisa b:
| 11   | -    | 15   | b[5]=15| c[10]=15| 5 | 6 | 11|

Array c: {1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 15}
```

**Jawaban: 1 2 4 5 6 7 9 10 11 13 15**

---

## Ringkasan Konsep Kunci

| Konsep | Tips Trace | Kesalahan Umum |
|--------|-----------|---------------|
| For loop | Catat inisialisasi, kondisi, update per iterasi | Salah hitung batas loop (off-by-one) |
| While loop | Pastikan kondisi berubah agar tidak infinite loop | Lupa update variabel kondisi |
| Array | Indeks mulai dari 0 | Akses arr[n] padahal valid 0..n-1 |
| Rekursi | Gambar call tree, identifikasi base case | Lupa base case = infinite recursion |
| Pass by reference | Tandai parameter dengan & yang mengubah asli | Mengira pass by value mengubah asli |
| Sorting | Catat setiap swap per pass | Salah arah perbandingan (> vs <) |
| Bitwise | Konversi ke biner, operasikan per bit | Lupa prioritas operator bitwise |
| String | Perhatikan indeks 0-based, length() | Off-by-one saat iterasi |

---

## Tips Mengerjakan Soal Trace C++ di OSK

1. **Buat tabel trace** - Tulis variabel di kolom header, isi nilai per iterasi/langkah.
2. **Perhatikan scope** - Variabel di dalam loop/fungsi berbeda dari luar.
3. **Bedakan pass by value vs reference** - Tanda `&` kunci penting.
4. **Integer division** - `7/2 = 3` bukan 3.5.
5. **Operator precedence** - Jika ragu, asumsikan perlu tanda kurung.
6. **Base case rekursi** - Selalu identifikasi kapan berhenti.
7. **Array bounds** - Indeks valid 0 sampai n-1.
8. **Post vs pre increment** - `x++` pakai dulu baru tambah, `++x` tambah dulu baru pakai.
9. **Hati-hati break/continue** - break keluar loop, continue lanjut iterasi berikut.
10. **Verifikasi jawaban** - Jika memungkinkan, hitung ulang dengan cara berbeda.
