# Materi 06 — Modulo & Teori Bilangan

## 1. Operasi Modulo

**Definisi:** `a mod m` adalah **sisa pembagian** `a` oleh `m`.

```
a = q × m + r,    dimana 0 ≤ r < m
r = a mod m
```

**Contoh:**
```
17 mod 5  = 2     (karena 17 = 3×5 + 2)
100 mod 7 = 2     (karena 100 = 14×7 + 2)
12 mod 4  = 0     (habis dibagi)
-1 mod 5  = 4     (dalam matematika; di C++ hasilnya -1)
```

> **Perhatian C++:** Operator `%` di C++ untuk bilangan negatif berbeda dengan definisi matematika.
> `(-1) % 5 = -1` di C++, bukan `4`.

---

## 2. Sifat-Sifat Modulo

### Sifat Dasar (Sangat Penting!)
```
(a + b) mod m = ((a mod m) + (b mod m)) mod m
(a - b) mod m = ((a mod m) - (b mod m) + m) mod m
(a × b) mod m = ((a mod m) × (b mod m)) mod m
```

### Sifat Distributif
```
(a + b + c) mod m = ((a mod m) + (b mod m) + (c mod m)) mod m
```

### Sifat Eksponen (Fermat's Little Theorem)
Jika `p` adalah bilangan prima dan `gcd(a, p) = 1`:
```
a^(p-1) ≡ 1 (mod p)
a^p ≡ a (mod p)
```

**Aplikasi:** Menghitung `a^n mod m` untuk `n` sangat besar.

---

## 3. Teknik Menghitung Modulo Besar

### Strategi: Gunakan Sifat Modulo
Untuk soal OSN, sering diminta `X mod Y` dimana `X` sangat besar (seperti `2^1000`).

**Langkah:**
1. Cari pola sisa pembagian
2. Gunakan sifat modulo

### Contoh: `2^1000 mod 3`
```
2^1 mod 3 = 2
2^2 mod 3 = 4 mod 3 = 1
2^3 mod 3 = 8 mod 3 = 2
2^4 mod 3 = 16 mod 3 = 1
→ Pola: ganjil=2, genap=1
→ 2^1000 mod 3 = 1  (karena 1000 genap)
```

### Contoh: `2^10 mod 3`
```
2^10 mod 3 = (2^2)^5 mod 3 = 1^5 mod 3 = 1
```

### Contoh Soal OSN: `(1+2+...+100) + (1²+2²+...+100²) + (1³+2³+...+100³)` mod 10
```
Σn   = n(n+1)/2       = 100×101/2 = 5050  → mod 10 = 0
Σn²  = n(n+1)(2n+1)/6 = 100×101×201/6 = 338350 → mod 10 = 0
Σn³  = (n(n+1)/2)²    = 5050² = 25502500 → mod 10 = 0

Total mod 10 = (0 + 0 + 0) mod 10 = 0
```

---

## 4. FPB (Faktor Persekutuan Terbesar) — GCD

**Definisi:** `gcd(a, b)` = bilangan terbesar yang membagi habis `a` dan `b`.

### Algoritma Euclidean
```
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
```

**Contoh:**
```
gcd(48, 18) = gcd(18, 12)
            = gcd(12, 6)
            = gcd(6, 0)
            = 6
```

**Kode C++:**
```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
// Atau lebih singkat:
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
```

---

## 5. KPK (Kelipatan Persekutuan Terkecil) — LCM

```
lcm(a, b) = (a × b) / gcd(a, b)
```

**Contoh:**
```
lcm(12, 8) = (12 × 8) / gcd(12, 8) = 96 / 4 = 24
```

---

## 6. Bilangan Prima

**Definisi:** Bilangan yang hanya habis dibagi 1 dan dirinya sendiri.

### Cek Prima Naif: O(√n)
```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

### Sieve of Eratosthenes: O(n log log n)
Untuk mencari semua bilangan prima ≤ n.

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

---

## 7. Faktorisasi Prima

```
360 = 2³ × 3² × 5
```

```cpp
vector<int> primeFactors(int n) {
    vector<int> factors;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
    }
    if (n > 1) factors.push_back(n);
    return factors;
}
```

---

## 8. Fungsi Euler (Euler's Totient φ)

**Definisi:** `φ(n)` = banyaknya bilangan 1 ≤ k ≤ n yang `gcd(k, n) = 1`.

```
φ(p)   = p - 1          untuk prima p
φ(p^k) = p^k - p^(k-1)
φ(ab)  = φ(a)×φ(b)      jika gcd(a,b) = 1
```

**Contoh: φ(5000)**
```
5000 = 2³ × 5⁴
φ(5000) = 5000 × (1 - 1/2) × (1 - 1/5)
        = 5000 × 1/2 × 4/5
        = 2000
```

Ini digunakan dalam soal: "Berapa banyak bilangan x < 5000 yang gcd(5000, x) = 1?"
**Jawaban: φ(5000) = 2000**

---

## 9. Representasi Biner & Bit

**Koin biner:** Nilai 2^0, 2^1, 2^2, ..., 2^n

Untuk membayar sejumlah N dengan koin terkecil:
```
N = sum pilihan subset dari {1, 2, 4, 8, 16, ...}
```

**Contoh:** N = 1023 = 1024 - 1 = 2^10 - 1
```
1023 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
     = 2^9 + 2^8 + ... + 2^0
     → butuh 10 koin
```

Cara cepat: 1023 dalam biner = `1111111111` (10 bit 1) → 10 koin.

---

## 10. XOR dan Sifat-Sifatnya

**Tabel XOR:**
| A | B | A⊕B |
|---|---|-----|
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 1   |
| 1 | 1 | 0   |

**Sifat Penting:**
```
a ⊕ 0 = a
a ⊕ a = 0
a ⊕ b = b ⊕ a   (komutatif)
(a⊕b)⊕c = a⊕(b⊕c)  (asosiatif)
```

**Sifat Kunci untuk Soal:**
- Elemen yang muncul **genap** kali → kontribusi XOR = 0
- Elemen yang muncul **ganjil** kali → kontribusi XOR = elemen itu sendiri

---

## 11. Contoh Soal Modulo

**Soal 1:** `12 mod 5 = ?`
> Jawab: 12 = 2×5 + 2 → **2**

**Soal 2:** `2^1000 mod 3 = ?`
> Pola: 2^(genap) mod 3 = 1 → **1**

**Soal 3:** `123^100 mod 101 = ?`
> 101 adalah prima, gcd(123, 101) = gcd(22, 101) = 1
> Fermat: 123^100 mod 101 = 123^(101-1) mod 101 = 1
> Tapi kita perlu 123^100, bukan 123^100. Di sini 100 = p-1 = 101-1.
> Jadi 123^100 mod 101 = **1**

---

## 12. Latihan
1. Hitung `17^50 mod 5` tanpa kalkulator.
2. Berapa banyak bilangan 1..1000 yang relatif prima dengan 1000?
3. Jika koin tersedia: 1, 2, 4, 8, 16 (rupiah), berapa koin minimum untuk membayar Rp 31?
4. Hitung `gcd(252, 198)` menggunakan algoritma Euclidean.
5. `(1² + 2² + 3² + ... + 10²) mod 7 = ?`

*Jawaban di folder `../latihan/`*
