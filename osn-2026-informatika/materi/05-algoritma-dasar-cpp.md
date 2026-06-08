# Materi 05 — Algoritma Dasar & Trace Kode C++

Materi ini fokus untuk Bagian C OSK: memahami dan men-trace kode C++.

---

## 1. Struktur Dasar C++

```cpp
#include <iostream>
using namespace std;

int main() {
    // kode program
    return 0;
}
```

### Input / Output
```cpp
int a, b;
cin >> a >> b;           // baca 2 integer
cout << a + b << "\n";  // cetak hasil + newline
```

---

## 2. Tipe Data Dasar

| Tipe | Ukuran | Contoh Nilai |
|------|--------|--------------|
| `int` | 4 byte | -2147483648 s/d 2147483647 |
| `long long` | 8 byte | nilai sangat besar |
| `double` | 8 byte | 3.14, 2.718 |
| `char` | 1 byte | 'A', 'z', '5' |
| `bool` | 1 byte | true / false |
| `string` | variabel | "hello" |

---

## 3. Percabangan (if / else)

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

### Operator Perbandingan
`==`, `!=`, `<`, `>`, `<=`, `>=`

### Operator Logika
`&&` (AND), `||` (OR), `!` (NOT)

---

## 4. Perulangan (Loop)

### For Loop
```cpp
for (int i = 0; i < 5; i++) {
    cout << i << " ";
}
// Output: 0 1 2 3 4
```

### While Loop
```cpp
int i = 0;
while (i < 5) {
    cout << i << " ";
    i++;
}
// Output: 0 1 2 3 4
```

### Do-While Loop
```cpp
int i = 0;
do {
    cout << i << " ";
    i++;
} while (i < 5);
// Output: 0 1 2 3 4
```

> **Penting:** `break` untuk keluar loop, `continue` untuk lanjut iterasi berikutnya.

---

## 5. Array

```cpp
int arr[5] = {10, 20, 30, 40, 50};

// Akses elemen (0-indexed)
cout << arr[0];   // 10
cout << arr[4];   // 50

// Traversal
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
// Output: 10 20 30 40 50
```

### Array 2D
```cpp
int mat[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
cout << mat[1][2];  // 6
```

---

## 6. Fungsi / Subprogram

```cpp
// Deklarasi fungsi
int tambah(int a, int b) {
    return a + b;
}

int main() {
    int hasil = tambah(3, 4);
    cout << hasil;   // 7
}
```

### Fungsi void (tanpa nilai kembalian)
```cpp
void cetak(int n) {
    for (int i = 1; i <= n; i++)
        cout << i << " ";
    cout << "\n";
}
```

### Pass by reference
```cpp
void tukar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
```

---

## 7. Rekursi

Fungsi yang memanggil dirinya sendiri.

```cpp
int faktorial(int n) {
    if (n <= 1) return 1;      // base case
    return n * faktorial(n-1); // rekursif
}
// faktorial(5) = 5 × 4 × 3 × 2 × 1 = 120
```

```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
// fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5
```

---

## 8. Trace Kode — Latihan Langkah demi Langkah

### Contoh 1: Trace Loop Sederhana
```cpp
int s = 0;
for (int i = 1; i <= 5; i++) {
    s += i;
}
cout << s;
```

| i | s sebelum | s setelah |
|---|-----------|-----------|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |
| 5 | 10 | 15 |

**Output: 15**

---

### Contoh 2: Trace Rekursi
```cpp
int f(int n) {
    if (n == 0) return 1;
    return 2 * f(n-1);
}
cout << f(4);
```

Trace:
```
f(4) = 2 * f(3)
f(3) = 2 * f(2)
f(2) = 2 * f(1)
f(1) = 2 * f(0)
f(0) = 1
→ f(1) = 2
→ f(2) = 4
→ f(3) = 8
→ f(4) = 16
```
**Output: 16**

---

### Contoh 3: Trace Array
```cpp
int arr[] = {5, 3, 8, 1, 9};
int n = 5;
int maks = arr[0];
for (int i = 1; i < n; i++) {
    if (arr[i] > maks)
        maks = arr[i];
}
cout << maks;
```

| i | arr[i] | maks |
|---|--------|------|
| - | - | 5 |
| 1 | 3 | 5 |
| 2 | 8 | 8 |
| 3 | 1 | 8 |
| 4 | 9 | 9 |

**Output: 9**

---

## 9. Pola-Pola Umum dalam Soal Trace

| Pola | Ciri |
|------|------|
| Hitung jumlah | `s += arr[i]` atau `s = s + i` |
| Cari maks/min | `if (arr[i] > maks) maks = arr[i]` |
| Hitung frekuensi | `cnt[arr[i]]++` |
| Bubble sort | 2 loop bersarang + swap |
| Binary search | `lo`, `hi`, `mid = (lo+hi)/2` |
| Rekursi menurun | Base case + panggilan rekursif |

---

## 10. Tips Mengerjakan Soal Bagian C

1. **Baca kode dari atas ke bawah**, identifikasi: variabel, tipe data, loop, kondisi.
2. **Buat tabel trace** untuk melacak nilai variabel di setiap iterasi.
3. **Perhatikan indeks array** — C++ menggunakan 0-indexed!
4. **Hati-hati dengan kondisi loop:** `i < n` vs `i <= n`.
5. **Rekursi:** Mulai dari base case, lalu trace ke atas.
6. Jika kode panjang, cari **pola/invariant** dari loop.
