# Materi 05 — Algoritma Dasar & Trace Kode C++

Materi ini fokus untuk **Bagian C OSK Informatika 2026**: memahami dan men-trace kode C++.
Ujian OSK berlangsung 2,5 jam dengan format soal pilihan ganda, jawaban singkat, dan benar/salah.
Kemampuan membaca kode secara cepat dan akurat sangat menentukan skor di bagian ini.

---

## 1. Struktur Dasar C++

```cpp
#include <iostream>
using namespace std;

int main() {
    // kode program di sini
    return 0;
}
```

### 1.1. Input / Output

```cpp
int a, b;
cin >> a >> b;           // baca 2 integer dari input
cout << a + b << "\n";  // cetak hasil penjumlahan + newline
```

**Catatan penting:**
- `cin` membaca hingga whitespace (spasi/newline).
- `cout` tidak otomatis menambahkan newline, harus eksplisit `"\n"` atau `endl`.
- `endl` melakukan flush buffer, `"\n"` lebih cepat.

### 1.2. Komentar

```cpp
// komentar satu baris

/* komentar
   beberapa baris */
```

---

## 2. Tipe Data dan Konversi

### 2.1. Tipe Data Dasar

| Tipe | Ukuran | Rentang Nilai |
|------|--------|---------------|
| `int` | 4 byte | -2.147.483.648 s/d 2.147.483.647 (~2 x 10^9) |
| `long long` | 8 byte | -9.2 x 10^18 s/d 9.2 x 10^18 |
| `double` | 8 byte | presisi ~15 digit desimal |
| `char` | 1 byte | -128 s/d 127 (atau karakter ASCII) |
| `bool` | 1 byte | `true` (1) atau `false` (0) |
| `string` | variabel | rangkaian karakter |

### 2.2. Type Casting (Konversi Tipe)

```cpp
int a = 7, b = 2;
double hasil1 = a / b;           // 3.0 (pembagian integer dulu, baru konversi)
double hasil2 = (double)a / b;   // 3.5 (a dikonversi ke double dulu)
double hasil3 = 1.0 * a / b;    // 3.5 (trik perkalian 1.0)

int c = (int)3.7;   // 3 (pemotongan, bukan pembulatan!)
int d = (int)-2.9;  // -2 (menuju nol)
```

**Perangkap umum:** `5/3` menghasilkan `1` (bukan `1.666...`) karena keduanya integer.

### 2.3. Aritmetika Karakter (char)

Setiap `char` memiliki nilai ASCII numerik:

| Karakter | Nilai ASCII |
|----------|-------------|
| `'0'` s/d `'9'` | 48 s/d 57 |
| `'A'` s/d `'Z'` | 65 s/d 90 |
| `'a'` s/d `'z'` | 97 s/d 122 |

```cpp
char c = 'A';
int kode = c;           // kode = 65
char d = c + 3;         // d = 'D' (65 + 3 = 68 = 'D')
int digit = '7' - '0';  // digit = 7 (55 - 48 = 7)

// Konversi huruf kecil ke huruf besar
char huruf = 'g';
char besar = huruf - 32;  // 'G' (103 - 32 = 71)
// Atau lebih aman:
char besar2 = huruf - 'a' + 'A';  // 'G'
```

### 2.4. Operator Aritmatika

| Operator | Fungsi | Contoh |
|----------|--------|--------|
| `+` | Penjumlahan | `5 + 3 = 8` |
| `-` | Pengurangan | `5 - 3 = 2` |
| `*` | Perkalian | `5 * 3 = 15` |
| `/` | Pembagian | `7 / 2 = 3` (integer) |
| `%` | Modulo (sisa bagi) | `7 % 2 = 1` |

### 2.5. Operator Increment/Decrement

```cpp
int x = 5;
int a = x++;   // a = 5, x = 6 (post-increment: pakai dulu, tambah kemudian)
int b = ++x;   // x = 7, b = 7 (pre-increment: tambah dulu, baru pakai)
```

---

## 3. Percabangan (if / else / switch)

### 3.1. if-else

```cpp
int x = 10;
if (x > 5) {
    cout << "besar\n";
} else if (x == 5) {
    cout << "sama\n";
} else {
    cout << "kecil\n";
}
// Output: besar
```

### 3.2. Operator Perbandingan dan Logika

| Operator | Arti |
|----------|------|
| `==` | Sama dengan |
| `!=` | Tidak sama dengan |
| `<`, `>` | Kurang/lebih dari |
| `<=`, `>=` | Kurang/lebih dari atau sama |
| `&&` | AND (dan) |
| `\|\|` | OR (atau) |
| `!` | NOT (negasi) |

### 3.3. Ternary Operator

```cpp
int x = 10;
int hasil = (x > 5) ? 100 : 200;  // hasil = 100
```

### 3.4. Switch-Case

```cpp
int hari = 3;
switch (hari) {
    case 1: cout << "Senin"; break;
    case 2: cout << "Selasa"; break;
    case 3: cout << "Rabu"; break;
    default: cout << "Lainnya";
}
// Output: Rabu
```

**Perangkap:** Jika lupa `break`, eksekusi akan "jatuh" ke case berikutnya (fall-through).

---

## 4. Perulangan (Loop)

### 4.1. For Loop

```cpp
for (int i = 0; i < 5; i++) {
    cout << i << " ";
}
// Output: 0 1 2 3 4
```

Struktur: `for (inisialisasi; kondisi; update)`

### 4.2. While Loop

```cpp
int i = 10;
while (i > 0) {
    cout << i << " ";
    i -= 3;
}
// Output: 10 7 4 1
```

### 4.3. Do-While Loop

```cpp
int i = 10;
do {
    cout << i << " ";
    i++;
} while (i < 5);
// Output: 10  (dieksekusi minimal 1 kali walaupun kondisi sudah false)
```

### 4.4. Break dan Continue

```cpp
// break: keluar dari loop sepenuhnya
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    cout << i << " ";
}
// Output: 0 1 2 3 4

// continue: lanjut ke iterasi berikutnya
for (int i = 0; i < 7; i++) {
    if (i % 2 == 0) continue;
    cout << i << " ";
}
// Output: 1 3 5
```

### 4.5. Nested Loop (Loop Bersarang)

```cpp
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        cout << i * j << " ";
    }
    cout << "\n";
}
```
Output:
```
1 2 3
2 4 6
3 6 9
```

### 4.6. Pola Nested Loop dengan Kondisi

```cpp
int n = 5;
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "*";
    }
    cout << "\n";
}
```
Output:
```
*
**
***
****
*****
```

```cpp
// Pola angka segitiga
for (int i = 1; i <= 4; i++) {
    for (int j = i; j <= 4; j++) {
        cout << j << " ";
    }
    cout << "\n";
}
```
Output:
```
1 2 3 4
2 3 4
3 4
4
```

---

## 5. Array

### 5.1. Array 1 Dimensi

```cpp
int arr[5] = {10, 20, 30, 40, 50};

// Akses elemen (0-indexed!)
cout << arr[0];   // 10
cout << arr[4];   // 50

// Traversal
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
// Output: 10 20 30 40 50
```

### 5.2. Array 2 Dimensi (Matriks)

```cpp
int mat[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Akses: mat[baris][kolom]
cout << mat[0][0];   // 1
cout << mat[2][3];   // 12
cout << mat[1][2];   // 7
```

### 5.3. Operasi pada Array 2D

```cpp
// Menjumlahkan semua elemen matriks 3x3
int mat[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
int total = 0;
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        total += mat[i][j];
    }
}
cout << total;  // 45
```

```cpp
// Menjumlahkan diagonal utama
int diagSum = 0;
for (int i = 0; i < 3; i++) {
    diagSum += mat[i][i];
}
cout << diagSum;  // 1 + 5 + 9 = 15
```

```cpp
// Transpose matriks (tukar baris dan kolom)
int trans[3][3];
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        trans[j][i] = mat[i][j];
    }
}
// trans = {{1,4,7},{2,5,8},{3,6,9}}
```

```cpp
// Mencari elemen terbesar di setiap baris
for (int i = 0; i < 3; i++) {
    int maks = mat[i][0];
    for (int j = 1; j < 3; j++) {
        if (mat[i][j] > maks) maks = mat[i][j];
    }
    cout << "Baris " << i << ": " << maks << "\n";
}
// Baris 0: 3
// Baris 1: 6
// Baris 2: 9
```

---

## 6. String dan Operasi String

### 6.1. Deklarasi dan Inisialisasi

```cpp
string s = "Hello";
string t = "World";
string u = s + " " + t;  // "Hello World" (konkatenasi)
```

### 6.2. Operasi Dasar String

```cpp
string s = "Informatika";

cout << s.length();     // 11 (panjang string)
cout << s.size();       // 11 (sama dengan length)
cout << s[0];           // 'I' (karakter pertama)
cout << s[10];          // 'a' (karakter terakhir)
```

### 6.3. Substring dan Find

```cpp
string s = "Algoritma";

// substr(posisi_awal, panjang)
cout << s.substr(0, 4);   // "Algo"
cout << s.substr(4);      // "ritma" (dari posisi 4 sampai akhir)
cout << s.substr(2, 3);   // "gor"

// find(substring) - mengembalikan posisi pertama ditemukan
cout << s.find("rit");    // 4
cout << s.find("xyz");    // string::npos (tidak ditemukan)
```

### 6.4. Iterasi Karakter String

```cpp
string s = "ABC";
for (int i = 0; i < s.length(); i++) {
    cout << s[i] << "=" << (int)s[i] << " ";
}
// Output: A=65 B=66 C=67
```

### 6.5. Manipulasi String

```cpp
string s = "abcde";

// Balik string secara manual
string rev = "";
for (int i = s.length() - 1; i >= 0; i--) {
    rev += s[i];
}
// rev = "edcba"

// Cek palindrome
bool palindrome = (s == rev);  // false
```

```cpp
// Hitung frekuensi huruf
string kata = "banana";
int freq[26] = {0};  // semua 0
for (int i = 0; i < kata.length(); i++) {
    freq[kata[i] - 'a']++;
}
// freq[0] = 3 (a), freq[1] = 1 (b), freq[13] = 2 (n)
```

---

## 7. Fungsi dan Subprogram

### 7.1. Fungsi dengan Return Value

```cpp
int kuadrat(int x) {
    return x * x;
}

int main() {
    int h = kuadrat(5);  // h = 25
    cout << h;
}
```

### 7.2. Fungsi void

```cpp
void cetakGaris(int n) {
    for (int i = 0; i < n; i++) {
        cout << "-";
    }
    cout << "\n";
}
```

### 7.3. Pass by Value vs Pass by Reference

**Pass by Value** - fungsi mendapat salinan nilai. Perubahan di dalam fungsi TIDAK mempengaruhi variabel asli.

```cpp
void tambahSatu(int x) {
    x = x + 1;  // hanya mengubah salinan lokal
}

int main() {
    int a = 5;
    tambahSatu(a);
    cout << a;   // tetap 5!
}
```

**Pass by Reference** - fungsi mengakses variabel asli secara langsung. Perubahan DI DALAM fungsi AKAN mempengaruhi variabel asli.

```cpp
void tambahSatu(int &x) {   // tanda & = reference
    x = x + 1;  // mengubah variabel asli
}

int main() {
    int a = 5;
    tambahSatu(a);
    cout << a;   // 6 (berubah!)
}
```

**Contoh klasik: Swap (Tukar)**

```cpp
void tukar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 3, y = 7;
    tukar(x, y);
    cout << x << " " << y;  // 7 3
}
```

### 7.4. Fungsi dengan Array sebagai Parameter

```cpp
// Array selalu dipass by reference (otomatis)
void isiArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
}

int main() {
    int data[5];
    isiArray(data, 5);
    // data = {0, 10, 20, 30, 40}
}
```

---

## 8. Rekursi

### 8.1. Konsep Dasar

Fungsi yang memanggil dirinya sendiri. Harus memiliki:
1. **Base case** - kondisi berhenti
2. **Recursive case** - panggilan ke diri sendiri dengan parameter lebih kecil

```cpp
int faktorial(int n) {
    if (n <= 1) return 1;       // base case
    return n * faktorial(n - 1); // recursive case
}
// faktorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

### 8.2. Fibonacci

```cpp
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
// fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5
```

### 8.3. Rekursi dengan Aksi

```cpp
void countdown(int n) {
    if (n == 0) {
        cout << "GO!\n";
        return;
    }
    cout << n << " ";
    countdown(n - 1);
}
// countdown(3) mencetak: 3 2 1 GO!
```

---

## 9. Algoritma Pencarian (Searching)

### 9.1. Linear Search (Pencarian Linier)

Memeriksa setiap elemen satu per satu dari awal hingga akhir.

```cpp
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;  // ditemukan di indeks i
    }
    return -1;  // tidak ditemukan
}
```

**Trace contoh:**
```
arr = {4, 7, 2, 9, 1}, target = 9

i=0: arr[0]=4, 4==9? Tidak
i=1: arr[1]=7, 7==9? Tidak
i=2: arr[2]=2, 2==9? Tidak
i=3: arr[3]=9, 9==9? Ya! Return 3
```

Kompleksitas: O(n) - paling lambat harus memeriksa semua elemen.

### 9.2. Binary Search (Pencarian Biner)

**Syarat:** Array harus sudah terurut (sorted).
Ide: bagi dua area pencarian setiap iterasi.

```cpp
int binarySearch(int arr[], int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;  // tidak ditemukan
}
```

**Trace contoh:**
```
arr = {2, 5, 8, 12, 16, 23, 38, 45}, target = 23

Iterasi 1: lo=0, hi=7, mid=3, arr[3]=12 < 23 -> lo=4
Iterasi 2: lo=4, hi=7, mid=5, arr[5]=23 == 23 -> Return 5!
```

**Trace lain (tidak ditemukan):**
```
arr = {2, 5, 8, 12, 16, 23, 38, 45}, target = 10

Iterasi 1: lo=0, hi=7, mid=3, arr[3]=12 > 10 -> hi=2
Iterasi 2: lo=0, hi=2, mid=1, arr[1]=5 < 10 -> lo=2
Iterasi 3: lo=2, hi=2, mid=2, arr[2]=8 < 10 -> lo=3
Iterasi 4: lo=3, hi=2 -> lo > hi, keluar loop. Return -1
```

Kompleksitas: O(log n) - jauh lebih cepat dari linear search untuk data besar.

---

## 10. Algoritma Pengurutan (Sorting)

### 10.1. Bubble Sort

Ide: Bandingkan elemen bersebelahan, tukar jika urutannya salah. Ulangi hingga terurut.

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

**Trace lengkap:**
```
Array awal: [5, 3, 8, 1, 2]

Pass i=0 (j: 0..3):
  j=0: [5,3,8,1,2] -> 5>3? Ya, tukar -> [3,5,8,1,2]
  j=1: [3,5,8,1,2] -> 5>8? Tidak
  j=2: [3,5,8,1,2] -> 8>1? Ya, tukar -> [3,5,1,8,2]
  j=3: [3,5,1,8,2] -> 8>2? Ya, tukar -> [3,5,1,2,8]
  (8 sudah di posisi benar)

Pass i=1 (j: 0..2):
  j=0: [3,5,1,2,8] -> 3>5? Tidak
  j=1: [3,5,1,2,8] -> 5>1? Ya, tukar -> [3,1,5,2,8]
  j=2: [3,1,5,2,8] -> 5>2? Ya, tukar -> [3,1,2,5,8]
  (5 sudah di posisi benar)

Pass i=2 (j: 0..1):
  j=0: [3,1,2,5,8] -> 3>1? Ya, tukar -> [1,3,2,5,8]
  j=1: [1,3,2,5,8] -> 3>2? Ya, tukar -> [1,2,3,5,8]
  (3 sudah di posisi benar)

Pass i=3 (j: 0..0):
  j=0: [1,2,3,5,8] -> 1>2? Tidak

Array akhir: [1, 2, 3, 5, 8] - TERURUT!
```

### 10.2. Selection Sort

Ide: Cari elemen terkecil dari sisa array, letakkan di posisi yang benar.

```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        // Tukar arr[i] dengan arr[minIdx]
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
}
```

**Trace lengkap:**
```
Array awal: [64, 25, 12, 22, 11]

Pass i=0: Cari minimum dari indeks 0..4
  minIdx=0 (64), j=1: 25<64 -> minIdx=1
  j=2: 12<25 -> minIdx=2
  j=3: 22<12? Tidak
  j=4: 11<12 -> minIdx=4
  Tukar arr[0] dan arr[4]: [11, 25, 12, 22, 64]

Pass i=1: Cari minimum dari indeks 1..4
  minIdx=1 (25), j=2: 12<25 -> minIdx=2
  j=3: 22<12? Tidak
  j=4: 64<12? Tidak
  Tukar arr[1] dan arr[2]: [11, 12, 25, 22, 64]

Pass i=2: Cari minimum dari indeks 2..4
  minIdx=2 (25), j=3: 22<25 -> minIdx=3
  j=4: 64<22? Tidak
  Tukar arr[2] dan arr[3]: [11, 12, 22, 25, 64]

Pass i=3: Cari minimum dari indeks 3..4
  minIdx=3 (25), j=4: 64<25? Tidak
  Tidak ada swap (sudah benar)

Array akhir: [11, 12, 22, 25, 64] - TERURUT!
```

### 10.3. Insertion Sort

Ide: Ambil elemen satu per satu, sisipkan ke posisi yang tepat di bagian array yang sudah terurut.

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

**Trace lengkap:**
```
Array awal: [7, 3, 5, 1, 9]

i=1: key=3, j=0
  arr[0]=7 > 3? Ya -> geser: [7,7,5,1,9], j=-1
  arr[j+1] = arr[0] = 3: [3,7,5,1,9]

i=2: key=5, j=1
  arr[1]=7 > 5? Ya -> geser: [3,7,7,1,9], j=0
  arr[0]=3 > 5? Tidak -> berhenti
  arr[j+1] = arr[1] = 5: [3,5,7,1,9]

i=3: key=1, j=2
  arr[2]=7 > 1? Ya -> geser: [3,5,7,7,9], j=1
  arr[1]=5 > 1? Ya -> geser: [3,5,5,7,9], j=0
  arr[0]=3 > 1? Ya -> geser: [3,3,5,7,9], j=-1
  arr[j+1] = arr[0] = 1: [1,3,5,7,9]

i=4: key=9, j=3
  arr[3]=7 > 9? Tidak -> berhenti
  arr[j+1] = arr[4] = 9: [1,3,5,7,9]

Array akhir: [1, 3, 5, 7, 9] - TERURUT!
```

### 10.4. Perbandingan Algoritma Sorting

| Algoritma | Best Case | Average Case | Worst Case | Stabil? |
|-----------|-----------|--------------|------------|---------|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | Ya |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | Tidak |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | Ya |

---

## 11. Operasi Bitwise

### 11.1. Operator Bitwise

| Operator | Nama | Contoh (desimal) | Contoh (biner) |
|----------|------|-------------------|----------------|
| `&` | AND | `5 & 3 = 1` | `101 & 011 = 001` |
| `\|` | OR | `5 \| 3 = 7` | `101 \| 011 = 111` |
| `^` | XOR | `5 ^ 3 = 6` | `101 ^ 011 = 110` |
| `~` | NOT | `~5 = -6` | membalik semua bit |
| `<<` | Left Shift | `3 << 2 = 12` | `011 << 2 = 1100` |
| `>>` | Right Shift | `12 >> 2 = 3` | `1100 >> 2 = 011` |

### 11.2. Penjelasan Detail

**AND (`&`):** Hasilnya 1 hanya jika kedua bit 1.
```
  0101  (5)
& 0011  (3)
------
  0001  (1)
```

**OR (`|`):** Hasilnya 1 jika salah satu atau kedua bit 1.
```
  0101  (5)
| 0011  (3)
------
  0111  (7)
```

**XOR (`^`):** Hasilnya 1 jika kedua bit berbeda.
```
  0101  (5)
^ 0011  (3)
------
  0110  (6)
```

**Left Shift (`<<`):** Geser bit ke kiri, tambah 0 di kanan. Efek: kalikan dengan 2^n.
```
3 << 1 = 6    (3 * 2^1)
3 << 2 = 12   (3 * 2^2)
1 << 4 = 16   (1 * 2^4)
```

**Right Shift (`>>`):** Geser bit ke kanan, buang bit di kanan. Efek: bagi dengan 2^n (pembulatan ke bawah).
```
12 >> 1 = 6   (12 / 2)
12 >> 2 = 3   (12 / 4)
7 >> 1 = 3    (7 / 2, bulatkan ke bawah)
```

### 11.3. Trik Bitwise yang Sering Muncul

```cpp
// Cek apakah bilangan genap/ganjil
bool ganjil = (n & 1);   // bit terakhir = 1 jika ganjil

// Kalikan / bagi dengan pangkat 2
int x = n << 3;   // n * 8
int y = n >> 2;   // n / 4

// Tukar dua bilangan tanpa variabel tambahan
a = a ^ b;
b = a ^ b;
a = a ^ b;

// Cek apakah n adalah pangkat 2
bool pangkat2 = (n > 0) && ((n & (n - 1)) == 0);
// Contoh: 8 = 1000, 8-1 = 0111, 1000 & 0111 = 0000 -> true
```

---

## 12. STL Basics (Standard Template Library)

### 12.1. Vector

Vector adalah array dinamis yang ukurannya bisa berubah.

```cpp
#include <vector>
using namespace std;

vector<int> v;          // vector kosong
vector<int> w(5, 0);    // vector berisi 5 elemen, semua 0
vector<int> u = {1, 2, 3, 4, 5};

v.push_back(10);   // tambah di belakang: [10]
v.push_back(20);   // [10, 20]
v.push_back(30);   // [10, 20, 30]

cout << v.size();   // 3
cout << v[0];       // 10
cout << v.back();   // 30 (elemen terakhir)

v.pop_back();       // hapus belakang: [10, 20]
```

### 12.2. Pair

Menyimpan sepasang nilai (bisa beda tipe).

```cpp
#include <utility>
using namespace std;

pair<int, int> p = {3, 7};
cout << p.first;    // 3
cout << p.second;   // 7

pair<string, int> siswa = {"Andi", 95};
cout << siswa.first << " " << siswa.second;  // Andi 95
```

### 12.3. sort() dari STL

```cpp
#include <algorithm>
using namespace std;

int arr[] = {5, 2, 8, 1, 9};
sort(arr, arr + 5);  // [1, 2, 5, 8, 9]

// Sort descending (besar ke kecil)
sort(arr, arr + 5, greater<int>());  // [9, 8, 5, 2, 1]

// Sort vector
vector<int> v = {3, 1, 4, 1, 5};
sort(v.begin(), v.end());  // [1, 1, 3, 4, 5]
```

### 12.4. min(), max(), swap()

```cpp
int a = 5, b = 3;
cout << min(a, b);  // 3
cout << max(a, b);  // 5
swap(a, b);         // a=3, b=5
```

---

## 13. Trace Kode Fungsi dengan Visualisasi Stack

### 13.1. Konsep Call Stack

Setiap kali fungsi dipanggil, sebuah "frame" baru ditambahkan ke stack.
Ketika fungsi selesai (return), frame-nya dihapus dari stack.

```cpp
int kuadrat(int x) {
    return x * x;
}

int jumlahKuadrat(int a, int b) {
    int ha = kuadrat(a);
    int hb = kuadrat(b);
    return ha + hb;
}

int main() {
    int hasil = jumlahKuadrat(3, 4);
    cout << hasil;
}
```

**Visualisasi stack:**
```
Langkah 1: main() dipanggil
  Stack: [main: hasil=?]

Langkah 2: jumlahKuadrat(3,4) dipanggil
  Stack: [main: hasil=?] [jumlahKuadrat: a=3, b=4, ha=?, hb=?]

Langkah 3: kuadrat(3) dipanggil dari dalam jumlahKuadrat
  Stack: [main] [jumlahKuadrat: a=3,b=4] [kuadrat: x=3]

Langkah 4: kuadrat(3) return 9, frame dihapus
  Stack: [main] [jumlahKuadrat: a=3, b=4, ha=9, hb=?]

Langkah 5: kuadrat(4) dipanggil
  Stack: [main] [jumlahKuadrat: a=3,b=4,ha=9] [kuadrat: x=4]

Langkah 6: kuadrat(4) return 16, frame dihapus
  Stack: [main] [jumlahKuadrat: a=3, b=4, ha=9, hb=16]

Langkah 7: jumlahKuadrat return 25, frame dihapus
  Stack: [main: hasil=25]

Output: 25
```

### 13.2. Stack pada Rekursi

```cpp
int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
// sum(4) = ?
```

**Visualisasi stack:**
```
Panggilan masuk (push):
  sum(4) -> 4 + sum(3)
    sum(3) -> 3 + sum(2)
      sum(2) -> 2 + sum(1)
        sum(1) -> 1 + sum(0)
          sum(0) -> return 0  [BASE CASE]

Kembali (pop):
  sum(0) = 0
  sum(1) = 1 + 0 = 1
  sum(2) = 2 + 1 = 3
  sum(3) = 3 + 3 = 6
  sum(4) = 4 + 6 = 10

Output: 10
```

---

## 14. Common C++ Pitfalls (Jebakan Umum)

### 14.1. Integer Overflow

```cpp
int a = 2000000000;  // 2 miliar (masih aman)
int b = a + a;       // OVERFLOW! Hasilnya bukan 4 miliar
// int hanya bisa menyimpan sampai ~2.14 miliar
// b = -294967296 (hasil tidak terduga!)

// Solusi: gunakan long long
long long c = 2000000000LL + 2000000000LL;  // 4000000000 (aman)
```

**Kapan overflow terjadi:**
- Perkalian dua `int` besar: `100000 * 100000` = 10^10 (overflow!)
- Faktorial: `13!` = 6.227.020.800 (sudah overflow untuk int)

### 14.2. Array Out of Bounds

```cpp
int arr[5] = {1, 2, 3, 4, 5};
cout << arr[5];   // UNDEFINED BEHAVIOR! Indeks valid: 0..4
cout << arr[-1];  // UNDEFINED BEHAVIOR!
```

C++ TIDAK memberikan error jika akses di luar batas. Program tetap berjalan tapi hasilnya tidak terduga.

### 14.3. Operator Precedence (Prioritas Operator)

Urutan prioritas (tinggi ke rendah):
1. `()` - tanda kurung
2. `!`, `~`, `++`, `--` - unary
3. `*`, `/`, `%` - perkalian/pembagian
4. `+`, `-` - penjumlahan/pengurangan
5. `<<`, `>>` - shift
6. `<`, `<=`, `>`, `>=` - perbandingan
7. `==`, `!=` - kesamaan
8. `&` - bitwise AND
9. `^` - bitwise XOR
10. `|` - bitwise OR
11. `&&` - logical AND
12. `||` - logical OR
13. `=`, `+=`, `-=` - assignment

**Contoh jebakan:**
```cpp
int x = 2 + 3 * 4;       // 14 (bukan 20!)
int y = (2 + 3) * 4;     // 20
bool z = 5 & 3 == 1;     // 5 & (3 == 1) = 5 & 0 = 0 (bukan (5&3) == 1)
// Karena == lebih tinggi dari &
```

### 14.4. Pembagian Integer

```cpp
cout << 7 / 2;      // 3 (bukan 3.5!)
cout << -7 / 2;     // -3 (menuju nol, bukan -4)
cout << 1 / 3;      // 0

// Untuk mendapat hasil pecahan:
cout << 7.0 / 2;    // 3.5
cout << (double)7/2; // 3.5
```

### 14.5. Lupa Inisialisasi

```cpp
int x;         // BUKAN 0! Bisa bernilai apapun (garbage value)
int arr[100];  // Isinya garbage, bukan 0

// Inisialisasi yang benar:
int x = 0;
int arr[100] = {0};           // semua 0
int arr2[100] = {};           // semua 0
memset(arr, 0, sizeof(arr));  // semua byte 0
```

### 14.6. Off-by-One Error

```cpp
// Sering salah: batas loop
for (int i = 0; i <= n; i++)   // mengakses n+1 elemen (0,1,...,n)
for (int i = 0; i < n; i++)    // mengakses n elemen (0,1,...,n-1)
for (int i = 1; i <= n; i++)   // mengakses n elemen (1,2,...,n)

// Array berukuran 5: indeks valid 0..4
int arr[5];
for (int i = 0; i <= 5; i++)   // BUG! i=5 keluar batas
    arr[i] = i;
```

---

## 15. Contoh Trace Lengkap (10+ Soal Bertingkat)

### Trace 1: Loop dengan Akumulator (Mudah)

```cpp
int n = 6, s = 0;
for (int i = 1; i <= n; i++) {
    if (i % 2 == 0)
        s += i;
}
cout << s;
```

| i | i%2==0? | s |
|---|---------|---|
| 1 | Tidak | 0 |
| 2 | Ya | 2 |
| 3 | Tidak | 2 |
| 4 | Ya | 6 |
| 5 | Tidak | 6 |
| 6 | Ya | 12 |

**Output: 12** (jumlah bilangan genap 1..6)

---

### Trace 2: Nested Loop (Mudah)

```cpp
int cnt = 0;
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        cnt++;
    }
}
cout << cnt;
```

| i | j berjalan dari | cnt bertambah |
|---|-----------------|---------------|
| 1 | 1 | 1 |
| 2 | 1, 2 | 3 |
| 3 | 1, 2, 3 | 6 |
| 4 | 1, 2, 3, 4 | 10 |

**Output: 10** (1 + 2 + 3 + 4 = 10)

---

### Trace 3: Array dan Conditional (Mudah-Sedang)

```cpp
int arr[] = {3, -1, 4, -5, 2, -3};
int pos = 0, neg = 0;
for (int i = 0; i < 6; i++) {
    if (arr[i] > 0) pos += arr[i];
    else neg += arr[i];
}
cout << pos << " " << neg;
```

| i | arr[i] | pos | neg |
|---|--------|-----|-----|
| 0 | 3 | 3 | 0 |
| 1 | -1 | 3 | -1 |
| 2 | 4 | 7 | -1 |
| 3 | -5 | 7 | -6 |
| 4 | 2 | 9 | -6 |
| 5 | -3 | 9 | -9 |

**Output: 9 -9**

---

### Trace 4: While Loop dengan Digit (Sedang)

```cpp
int n = 4273, rev = 0;
while (n > 0) {
    int digit = n % 10;
    rev = rev * 10 + digit;
    n = n / 10;
}
cout << rev;
```

| Iterasi | n | digit | rev |
|---------|---|-------|-----|
| 1 | 4273 | 3 | 3 |
| 2 | 427 | 7 | 37 |
| 3 | 42 | 2 | 372 |
| 4 | 4 | 4 | 3724 |
| 5 | 0 | - | keluar loop |

**Output: 3724** (bilangan dibalik)

---

### Trace 5: Fungsi Rekursif (Sedang)

```cpp
int mystery(int a, int b) {
    if (b == 0) return 0;
    if (b % 2 == 1)
        return a + mystery(a, b - 1);
    return mystery(a + a, b / 2);
}
cout << mystery(3, 5);
```

**Trace:**
```
mystery(3, 5): b=5 ganjil -> 3 + mystery(3, 4)
  mystery(3, 4): b=4 genap -> mystery(6, 2)
    mystery(6, 2): b=2 genap -> mystery(12, 1)
      mystery(12, 1): b=1 ganjil -> 12 + mystery(12, 0)
        mystery(12, 0): return 0
      return 12 + 0 = 12
    return 12
  return 12
return 3 + 12 = 15
```

**Output: 15** (ini adalah perkalian 3 * 5 menggunakan metode peasant multiplication)

---

### Trace 6: Pass by Reference (Sedang)

```cpp
void proses(int &x, int y) {
    x = x + y;
    y = y * 2;
    cout << x << " " << y << "\n";
}

int main() {
    int a = 5, b = 3;
    proses(a, b);
    cout << a << " " << b << "\n";
}
```

**Trace:**
```
main(): a=5, b=3
Panggil proses(a, b): x adalah REFERENSI ke a, y adalah SALINAN b
  x = x + y = 5 + 3 = 8 (a ikut berubah menjadi 8)
  y = y * 2 = 3 * 2 = 6 (b TIDAK berubah, y hanya salinan)
  Cetak: 8 6
Kembali ke main():
  a = 8 (berubah karena pass by reference)
  b = 3 (tidak berubah karena pass by value)
  Cetak: 8 3
```

**Output:**
```
8 6
8 3
```

---

### Trace 7: Bitwise Operations (Sedang-Sulit)

```cpp
int a = 12, b = 10;
cout << (a & b) << "\n";
cout << (a | b) << "\n";
cout << (a ^ b) << "\n";
cout << (a << 1) << "\n";
cout << (b >> 1) << "\n";
```

**Trace:**
```
a = 12 = 1100 (biner)
b = 10 = 1010 (biner)

a & b:  1100 & 1010 = 1000 = 8
a | b:  1100 | 1010 = 1110 = 14
a ^ b:  1100 ^ 1010 = 0110 = 6
a << 1: 1100 << 1 = 11000 = 24
b >> 1: 1010 >> 1 = 0101 = 5
```

**Output:**
```
8
14
6
24
5
```

---

### Trace 8: Sorting Parsial (Sulit)

```cpp
int arr[] = {4, 2, 7, 1, 3};
int n = 5;
// Hanya 2 pass pertama dari bubble sort
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
        if (arr[j] > arr[j+1]) {
            int t = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = t;
        }
    }
}
for (int i = 0; i < n; i++) cout << arr[i] << " ";
```

**Trace:**
```
Array awal: [4, 2, 7, 1, 3]

Pass i=0 (j: 0..3):
  j=0: 4>2? Ya -> [2, 4, 7, 1, 3]
  j=1: 4>7? Tidak
  j=2: 7>1? Ya -> [2, 4, 1, 7, 3]
  j=3: 7>3? Ya -> [2, 4, 1, 3, 7]

Pass i=1 (j: 0..2):
  j=0: 2>4? Tidak
  j=1: 4>1? Ya -> [2, 1, 4, 3, 7]
  j=2: 4>3? Ya -> [2, 1, 3, 4, 7]
```

**Output: 2 1 3 4 7**

---

### Trace 9: String Manipulation (Sulit)

```cpp
string s = "KOMPUTER";
string hasil = "";
for (int i = 0; i < s.length(); i++) {
    if (i % 2 == 0) {
        hasil += s[i];
    } else {
        hasil += (char)(s[i] + 1);
    }
}
cout << hasil;
```

**Trace:**

| i | s[i] | i%2==0? | Aksi | hasil |
|---|------|---------|------|-------|
| 0 | 'K' | Ya | tambah 'K' | "K" |
| 1 | 'O' | Tidak | 'O'+1='P' | "KP" |
| 2 | 'M' | Ya | tambah 'M' | "KPM" |
| 3 | 'P' | Tidak | 'P'+1='Q' | "KPMQ" |
| 4 | 'U' | Ya | tambah 'U' | "KPMQU" |
| 5 | 'T' | Tidak | 'T'+1='U' | "KPMQUU" |
| 6 | 'E' | Ya | tambah 'E' | "KPMQUUE" |
| 7 | 'R' | Tidak | 'R'+1='S' | "KPMQUUES" |

**Output: KPMQUUES**

---

### Trace 10: Rekursi Ganda (Sulit)

```cpp
int f(int n) {
    if (n <= 1) return n;
    return f(n - 1) + f(n - 2);
}

int main() {
    int total = 0;
    for (int i = 1; i <= 5; i++) {
        total += f(i);
    }
    cout << total;
}
```

**Trace f(n) - Fibonacci:**
```
f(1) = 1
f(2) = f(1) + f(0) = 1 + 0 = 1
f(3) = f(2) + f(1) = 1 + 1 = 2
f(4) = f(3) + f(2) = 2 + 1 = 3
f(5) = f(4) + f(3) = 3 + 2 = 5
```

**total = f(1) + f(2) + f(3) + f(4) + f(5) = 1 + 1 + 2 + 3 + 5 = 12**

**Output: 12**

---

### Trace 11: Array 2D dengan Loop Kompleks (Sulit)

```cpp
int mat[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
int s1 = 0, s2 = 0;
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == j) s1 += mat[i][j];
        if (i + j == 2) s2 += mat[i][j];
    }
}
cout << s1 << " " << s2;
```

**Trace:**
```
Diagonal utama (i==j): mat[0][0]=1, mat[1][1]=5, mat[2][2]=9
s1 = 1 + 5 + 9 = 15

Diagonal sekunder (i+j==2): mat[0][2]=3, mat[1][1]=5, mat[2][0]=7
s2 = 3 + 5 + 7 = 15
```

**Output: 15 15**

---

### Trace 12: Kombinasi Bitwise dan Loop (Sulit)

```cpp
int n = 13;  // 13 = 1101 dalam biner
int cnt = 0;
while (n > 0) {
    cnt += (n & 1);
    n >>= 1;
}
cout << cnt;
```

**Trace:**

| Iterasi | n (desimal) | n (biner) | n & 1 | cnt | n >>= 1 |
|---------|-------------|-----------|-------|-----|----------|
| 1 | 13 | 1101 | 1 | 1 | 6 |
| 2 | 6 | 0110 | 0 | 1 | 3 |
| 3 | 3 | 0011 | 1 | 2 | 1 |
| 4 | 1 | 0001 | 1 | 3 | 0 |
| 5 | 0 | - | keluar | - | - |

**Output: 3** (jumlah bit 1 dalam representasi biner 13)

---

### Trace 13: Fungsi Rekursif dengan Multiple Return (Sangat Sulit)

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

int main() {
    cout << gcd(48, 18) << " " << lcm(48, 18);
}
```

**Trace gcd(48, 18):**
```
gcd(48, 18): b!=0 -> gcd(18, 48%18) = gcd(18, 12)
gcd(18, 12): b!=0 -> gcd(12, 18%12) = gcd(12, 6)
gcd(12, 6):  b!=0 -> gcd(6, 12%6) = gcd(6, 0)
gcd(6, 0):   b==0 -> return 6
```

**lcm(48, 18) = 48 / gcd(48,18) * 18 = 48 / 6 * 18 = 8 * 18 = 144**

**Output: 6 144**

---

### Trace 14: Vector dan Sort (Sangat Sulit)

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {5, 2, 8, 1, 9, 3};
    sort(v.begin(), v.begin() + 4);  // sort hanya 4 elemen pertama
    
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] % 2 == 1) sum += v[i];
    }
    cout << sum;
}
```

**Trace:**
```
Array awal: [5, 2, 8, 1, 9, 3]
Setelah sort 4 elemen pertama (indeks 0..3):
  [5,2,8,1] diurutkan -> [1,2,5,8]
  Array menjadi: [1, 2, 5, 8, 9, 3]

Jumlahkan yang ganjil:
  v[0]=1 ganjil -> sum=1
  v[1]=2 genap
  v[2]=5 ganjil -> sum=6
  v[3]=8 genap
  v[4]=9 ganjil -> sum=15
  v[5]=3 ganjil -> sum=18
```

**Output: 18**

---

## 16. Pola-Pola Umum dalam Soal Trace

| Pola | Ciri Khas Kode | Hasil |
|------|----------------|-------|
| Hitung jumlah | `s += arr[i]` | Akumulasi total |
| Cari maks/min | `if (arr[i] > maks) maks = arr[i]` | Nilai ekstrem |
| Hitung frekuensi | `cnt[arr[i]]++` | Array frekuensi |
| Reverse | `rev = rev*10 + n%10; n/=10` | Bilangan dibalik |
| Count digits | `while(n>0){cnt++; n/=10;}` | Jumlah digit |
| GCD | `gcd(a,b) -> gcd(b, a%b)` | FPB |
| Pangkat | `while(b>0){if(b&1)res*=a; a*=a; b>>=1;}` | a^b |
| Fibonacci | `f(n) = f(n-1) + f(n-2)` | Bilangan Fibonacci |
| Palindrome check | bandingkan string asli dan reverse | true/false |
| Counting bits | `cnt += (n&1); n>>=1;` | Jumlah bit 1 |

---

## 17. Tips dan Trik Mengerjakan Soal Trace di Ujian

### 17.1. Strategi Umum

1. **Baca kode dari atas ke bawah.** Identifikasi: variabel, tipe data, loop, kondisi, fungsi.
2. **Buat tabel trace** untuk melacak nilai variabel di setiap iterasi. Ini WAJIB untuk loop.
3. **Perhatikan indeks array** - C++ menggunakan 0-indexed!
4. **Hati-hati `i < n` vs `i <= n`** - selisih 1 iterasi bisa mengubah jawaban.
5. **Rekursi:** Trace dari panggilan terluar, tulis setiap panggilan, kembali dari base case.
6. **Jika kode panjang,** cari pola/invariant dari loop sebelum trace satu-satu.

### 17.2. Teknik Cepat

1. **Kenali pola umum:** Jika melihat `s += i` dalam loop 1..n, langsung tahu hasilnya n*(n+1)/2.
2. **Hitung iterasi loop:** `for(i=0;i<n;i++)` berjalan n kali, `for(i=1;i<=n;i++)` juga n kali.
3. **Nested loop:** Total iterasi = perkalian iterasi masing-masing (jika independen).
4. **Binary search:** Hanya butuh log2(n) iterasi. Untuk n=1000, paling banyak 10 iterasi.
5. **Modulo pattern:** Jika ada `x = x % m`, maka x selalu < m.
6. **Shift pattern:** `n >>= 1` sama dengan `n /= 2`, loop ini berjalan log2(n) kali.

### 17.3. Kesalahan Umum Peserta

1. Lupa bahwa `int/int` menghasilkan integer (bukan float).
2. Salah menghitung batas loop (off-by-one).
3. Bingung antara pass by value dan pass by reference.
4. Tidak memperhatikan urutan evaluasi operator.
5. Lupa bahwa `char` bisa di-aritmatika-kan.
6. Tidak trace dari base case saat rekursi.
7. Salah menghitung modulo untuk bilangan negatif.

### 17.4. Manajemen Waktu

- Soal trace yang mudah (loop sederhana): targetkan 1-2 menit.
- Soal trace sedang (nested loop, array): targetkan 2-3 menit.
- Soal trace sulit (rekursi, bitwise): targetkan 3-5 menit.
- Jika stuck lebih dari 5 menit, tandai dan lanjut ke soal berikutnya.
- Kembali ke soal yang ditandai jika masih ada waktu.

### 17.5. Checklist Sebelum Menjawab

- [ ] Apakah semua variabel sudah diinisialisasi dengan benar?
- [ ] Apakah loop berhenti di kondisi yang benar?
- [ ] Apakah ada efek samping dari pass-by-reference?
- [ ] Apakah ada kemungkinan overflow?
- [ ] Apakah output mencakup newline atau spasi yang diminta?
- [ ] Apakah tipe data yang digunakan sudah sesuai (int vs double)?

---

## 18. Latihan Mandiri

### Soal 1
Tentukan output dari kode berikut:
```cpp
int x = 1;
for (int i = 0; i < 5; i++) {
    x = x * 2 + 1;
}
cout << x;
```

<details>
<summary>Jawaban</summary>

| i | x sebelum | x = x*2+1 |
|---|-----------|-----------|
| 0 | 1 | 3 |
| 1 | 3 | 7 |
| 2 | 7 | 15 |
| 3 | 15 | 31 |
| 4 | 31 | 63 |

**Output: 63**
</details>

---

### Soal 2
Tentukan output:
```cpp
int a = 10, b = 20;
int *p = &a, *q = &b;
*p = *q;
*q = *p + *q;
cout << a << " " << b;
```

<details>
<summary>Jawaban</summary>

```
p menunjuk ke a, q menunjuk ke b
*p = *q -> a = 20 (a diubah jadi nilai b)
*q = *p + *q -> b = 20 + 20 = 40
```
**Output: 20 40**
</details>

---

### Soal 3
Tentukan output:
```cpp
string s = "ABCDEF";
for (int i = 0; i < s.length(); i += 2) {
    cout << s.substr(i, 2) << " ";
}
```

<details>
<summary>Jawaban</summary>

```
i=0: substr(0,2) = "AB"
i=2: substr(2,2) = "CD"
i=4: substr(4,2) = "EF"
```
**Output: AB CD EF**
</details>

---

### Soal 4
Tentukan output:
```cpp
void ubah(int arr[], int n) {
    for (int i = 0; i < n/2; i++) {
        int temp = arr[i];
        arr[i] = arr[n-1-i];
        arr[n-1-i] = temp;
    }
}

int main() {
    int a[] = {1, 2, 3, 4, 5};
    ubah(a, 5);
    for (int i = 0; i < 5; i++) cout << a[i] << " ";
}
```

<details>
<summary>Jawaban</summary>

```
n/2 = 2, loop i=0..1
i=0: tukar a[0] dan a[4]: [5,2,3,4,1]
i=1: tukar a[1] dan a[3]: [5,4,3,2,1]
```
**Output: 5 4 3 2 1** (array dibalik)
</details>

---

### Soal 5
Tentukan output:
```cpp
int f(int n) {
    if (n < 2) return 1;
    return f(n/2) + f(n/3) + 1;
}
cout << f(6);
```

<details>
<summary>Jawaban</summary>

```
f(6) = f(3) + f(2) + 1
  f(3) = f(1) + f(1) + 1 = 1 + 1 + 1 = 3
  f(2) = f(1) + f(0) + 1 = 1 + 1 + 1 = 3
f(6) = 3 + 3 + 1 = 7
```
**Output: 7**
</details>

---

### Soal 6
Tentukan output:
```cpp
int mat[3][3] = {{1,0,0},{0,1,0},{0,0,1}};
int hasil = 0;
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        hasil += mat[i][j] * (i + j);
    }
}
cout << hasil;
```

<details>
<summary>Jawaban</summary>

```
Hanya elemen yang bernilai 1 yang berkontribusi:
mat[0][0]=1: 1*(0+0) = 0
mat[1][1]=1: 1*(1+1) = 2
mat[2][2]=1: 1*(2+2) = 4
Semua elemen 0 lainnya: 0
```
**Output: 6** (0 + 2 + 4 = 6)
</details>

---

### Soal 7
Tentukan output:
```cpp
int n = 100;
int cnt = 0;
while (n > 1) {
    if (n % 2 == 0) n /= 2;
    else n = 3*n + 1;
    cnt++;
    if (cnt == 8) break;
}
cout << n << " " << cnt;
```

<details>
<summary>Jawaban</summary>

| cnt | n | Aksi |
|-----|---|------|
| 0 | 100 | - |
| 1 | 50 | 100/2 |
| 2 | 25 | 50/2 |
| 3 | 76 | 3*25+1 |
| 4 | 38 | 76/2 |
| 5 | 19 | 38/2 |
| 6 | 58 | 3*19+1 |
| 7 | 29 | 58/2 |
| 8 | 88 | 3*29+1, lalu break |

**Output: 88 8**
</details>

---

### Soal 8
Tentukan output:
```cpp
int a = 0b1010;  // 10 dalam biner
int b = 0b0110;  // 6 dalam biner

int c = (a ^ b) & (a | b);
int d = (a & b) << 1;
cout << c << " " << d;
```

<details>
<summary>Jawaban</summary>

```
a = 1010 (10)
b = 0110 (6)

a ^ b = 1100 (12)
a | b = 1110 (14)
c = 1100 & 1110 = 1100 = 12

a & b = 0010 (2)
d = 0010 << 1 = 0100 = 4
```
**Output: 12 4**
</details>

---

## 19. Rangkuman Materi

| Topik | Hal Penting |
|-------|-------------|
| Tipe Data | `int` max ~2x10^9, `long long` untuk nilai besar |
| Char | Bisa diaritmatikakan, 'A'=65, 'a'=97, '0'=48 |
| Loop | Perhatikan batas: `< n` vs `<= n` |
| Array | 0-indexed, hati-hati out of bounds |
| String | `.length()`, `.substr()`, `.find()`, bisa di-index |
| Fungsi | Pass by value vs reference (&) |
| Rekursi | Selalu identifikasi base case |
| Sorting | Bubble, Selection, Insertion - trace step by step |
| Searching | Linear O(n), Binary O(log n) - harus sorted |
| Bitwise | &(AND), |(OR), ^(XOR), <<(shift kiri), >>(shift kanan) |
| STL | `vector`, `pair`, `sort()`, `min()`, `max()` |
| Pitfalls | Overflow, bounds, precedence, uninitialized |

---

**Selamat belajar! Kunci sukses di Bagian C OSK adalah LATIHAN TRACE sebanyak-banyaknya.**
Semakin banyak pola kode yang kamu kenali, semakin cepat kamu bisa menentukan output tanpa trace penuh.
