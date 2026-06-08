# Materi 03 — Kombinatorika & Deret Aritmetika

## 1. Aturan Dasar Menghitung

### Aturan Penjumlahan (Sum Rule)
Jika kejadian A bisa terjadi dengan **m cara**, dan kejadian B dengan **n cara**, dan keduanya **tidak bisa terjadi bersamaan**, maka total cara = **m + n**.

### Aturan Perkalian (Product Rule)
Jika kejadian A bisa terjadi dengan **m cara**, dan setelah itu B dengan **n cara**, maka total cara = **m × n**.

---

## 2. Faktorial

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
0! = 1   (definisi)
1! = 1
5! = 5 × 4 × 3 × 2 × 1 = 120
```

---

## 3. Permutasi

**Definisi:** Susunan terurut dari n objek. Urutan **PENTING**.

### Permutasi dari n objek berbeda (ambil semua)
```
P(n) = n!
```

### Permutasi r objek dari n objek (urutan penting)
```
P(n, r) = n! / (n-r)!
```

**Contoh:** Berapa cara mengatur 3 orang dari 5 orang dalam satu baris?
```
P(5,3) = 5! / (5-3)! = 120 / 2 = 60 cara
```

---

## 4. Kombinasi

**Definisi:** Pemilihan r objek dari n objek tanpa memperhatikan urutan. Urutan **TIDAK PENTING**.

```
C(n, r) = n! / (r! × (n-r)!)

Notasi: C(n,r) = ₙCᵣ = (n)
                        (r)
```

**Contoh:** Berapa cara memilih 3 orang dari 5 orang untuk suatu tim?
```
C(5,3) = 5! / (3! × 2!) = 120 / (6 × 2) = 10 cara
```

### Sifat Penting Kombinasi
- C(n, 0) = C(n, n) = 1
- C(n, r) = C(n, n-r)
- C(n, r) = C(n-1, r-1) + C(n-1, r)  ← Segitiga Pascal

---

## 5. Segitiga Pascal

```
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
```

Baris ke-n (mulai dari 0) memberikan nilai C(n,0), C(n,1), ..., C(n,n).

---

## 6. Pigeonhole Principle (Prinsip Sarang Merpati)

> Jika ada **n** objek yang dimasukkan ke **k** kotak, dan n > k, maka **minimal satu kotak berisi lebih dari satu objek**.

**Contoh:** Di antara 13 orang, pasti ada minimal 2 orang yang lahir di bulan yang sama (12 bulan < 13 orang).

**Generalisasi:** Jika n objek → k kotak, maka minimal ada satu kotak dengan ≥ ⌈n/k⌉ objek.

---

## 7. Prinsip Inklusi-Eksklusi (Kombinatorika)

Sudah dibahas di materi himpunan. Perluasan:
```
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ...
```

---

## 8. Deret Aritmetika

**Definisi:** Barisan bilangan dengan **selisih (beda) tetap** antar suku berurutan.

```
a, a+d, a+2d, a+3d, ...
```
- `a` = suku pertama
- `d` = beda (common difference)
- `n` = banyak suku

### Rumus Suku ke-n
```
aₙ = a + (n-1) × d
```

### Rumus Jumlah n Suku Pertama
```
Sₙ = n/2 × (2a + (n-1)d)
   = n/2 × (a₁ + aₙ)
```

**Contoh:** Barisan 3, 7, 11, 15, ...
- a = 3, d = 4
- Suku ke-10: a₁₀ = 3 + 9×4 = 39
- Jumlah 10 suku: S₁₀ = 10/2 × (3+39) = 5 × 42 = 210

---

## 9. Deret Geometri

**Definisi:** Barisan dengan **rasio tetap** antar suku.

```
a, ar, ar², ar³, ...
```
- `r` = rasio (common ratio)

### Rumus Suku ke-n
```
aₙ = a × r^(n-1)
```

### Rumus Jumlah n Suku
```
Sₙ = a × (rⁿ - 1) / (r - 1),  r ≠ 1
Sₙ = n × a,                     r = 1
```

---

## 10. Contoh Soal

**Soal 1:** Berapa banyak kata 3 huruf (tanpa pengulangan) dari huruf {A,B,C,D,E}?

> Jawab: P(5,3) = 5!/2! = **60**

**Soal 2:** Berapa cara memilih 2 wakil dari 6 kandidat?

> Jawab: C(6,2) = 15

**Soal 3:** Jumlah bilangan 1+2+3+...+100 = ?

> Jawab: Deret aritmetika, a=1, d=1, n=100
> S₁₀₀ = 100/2 × (1+100) = 50 × 101 = **5050**

**Soal 4:** Di sebuah kelas ada 30 siswa. Minimal berapa orang pasti lahir di bulan yang sama?

> Jawab: 12 bulan < 30 siswa → ⌈30/12⌉ = **3 orang**

---

## 11. Latihan
1. Dari 8 tim, berapa banyak pertandingan round-robin (setiap tim bertanding dengan semua tim lain)?
2. Berapa banyak cara mengisi 4 jabatan (ketua, sekretaris, bendahara, humas) dari 10 kandidat?
3. Suku ke-15 dari barisan 5, 8, 11, ... adalah?
4. Jumlah 20 suku pertama deret 2+4+8+16+... adalah?

*Jawaban di folder `../latihan/`*
