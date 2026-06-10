# Materi 02 — Teori Himpunan

## 1. Pendahuluan

Teori himpunan adalah bahasa dasar matematika dan informatika. Di OSN Informatika,
topik ini sering muncul dalam bentuk:
- Soal counting menggunakan Prinsip Inklusi-Eksklusi (PIE)
- Operasi himpunan dan diagram Venn
- Relasi subset dan power set
- Koneksi dengan logika Boolean

Materi ini akan membahas teori himpunan secara komprehensif dengan banyak contoh
bertingkat kesulitan, mulai dari dasar hingga level soal OSN.

---

## 2. Definisi Dasar

### 2.1 Apa Itu Himpunan?

**Himpunan (Set)** adalah kumpulan objek yang terdefinisi dengan jelas (well-defined).
"Terdefinisi dengan jelas" berarti untuk setiap objek, kita bisa menentukan dengan pasti
apakah objek tersebut anggota himpunan atau bukan.

Contoh himpunan:
- A = {1, 2, 3, 4, 5} (terdefinisi jelas)
- B = {x | x bilangan prima kurang dari 20} (terdefinisi jelas)

Bukan himpunan:
- "Kumpulan orang cantik" (subjektif, tidak terdefinisi jelas)
- "Kumpulan bilangan besar" (ambigu)

### 2.2 Notasi Himpunan

**Metode Roster (Daftar Anggota):**
```
A = {1, 2, 3, 4, 5}
B = {a, e, i, o, u}
C = {2, 4, 6, 8, ...}       (menggunakan ... untuk pola jelas)
```

**Metode Set Builder (Notasi Pembentuk):**
```
A = {x | x ∈ ℤ, 1 ≤ x ≤ 5}
B = {x | x adalah huruf vokal}
C = {x ∈ ℤ⁺ | x genap}
D = {x² | x ∈ {1,2,3,4,5}} = {1, 4, 9, 16, 25}
```

Dibaca: "Himpunan semua x sedemikian sehingga ..."

### 2.3 Keanggotaan

- `3 ∈ A` : 3 adalah anggota A (TRUE jika A = {1,2,3,4,5})
- `7 ∉ A` : 7 bukan anggota A
- Duplikat diabaikan: {1, 1, 2, 3} = {1, 2, 3}
- Urutan tidak penting: {3, 1, 2} = {1, 2, 3}

### 2.4 Kardinalitas

**Kardinalitas** |A| adalah jumlah elemen berbeda dalam himpunan A.

```
A = {1, 2, 3}       -> |A| = 3
B = {a, b}          -> |B| = 2
C = ∅               -> |C| = 0
D = {∅}             -> |D| = 1  (memiliki satu elemen, yaitu himpunan kosong)
E = {{1,2}, {3}}    -> |E| = 2  (dua elemen: {1,2} dan {3})
```

> **Perhatian:** {∅} TIDAK sama dengan ∅.
> - ∅ adalah himpunan kosong (tidak punya anggota)
> - {∅} adalah himpunan yang punya satu anggota, yaitu himpunan kosong

### 2.5 Himpunan Khusus

| Simbol | Nama | Isi |
|--------|------|-----|
| ∅ atau {} | Himpunan Kosong | Tidak ada anggota |
| U | Himpunan Semesta | Semua elemen yang sedang dibahas |
| ℕ | Bilangan Asli | {1, 2, 3, 4, ...} atau {0, 1, 2, 3, ...} |
| ℤ | Bilangan Bulat | {..., -2, -1, 0, 1, 2, ...} |
| ℤ⁺ | Bilangan Bulat Positif | {1, 2, 3, ...} |
| ℚ | Bilangan Rasional | {p/q | p,q ∈ ℤ, q ≠ 0} |
| ℝ | Bilangan Real | Semua bilangan (termasuk irasional) |

> **Catatan:** Ada konvensi berbeda untuk ℕ. Beberapa buku memasukkan 0, beberapa tidak.
> Di OSN, biasanya dispesifikkan. Jika tidak, tanyakan atau lihat konteks soal.

---

## 3. Relasi Antar Himpunan

### 3.1 Subset (Himpunan Bagian)

A ⊆ B (A adalah subset dari B) berarti **setiap** elemen A juga merupakan elemen B.

Secara formal: A ⊆ B ↔ ∀x (x ∈ A → x ∈ B)

**Contoh:**
```
{1, 2} ⊆ {1, 2, 3}         TRUE
{1, 2, 3} ⊆ {1, 2, 3}     TRUE (setiap himpunan adalah subset dirinya sendiri)
∅ ⊆ {1, 2, 3}              TRUE (himpunan kosong adalah subset semua himpunan)
{1, 4} ⊆ {1, 2, 3}         FALSE (4 tidak ada di {1,2,3})
```

> **Fakta penting:** ∅ ⊆ A untuk SEMUA himpunan A. Mengapa?
> Karena "semua elemen ∅ ada di A" bernilai vacuously true (tidak ada elemen yang perlu dicek).

### 3.2 Proper Subset (Subset Sejati)

A ⊂ B berarti A ⊆ B DAN A ≠ B (ada elemen B yang tidak di A).

```
{1, 2} ⊂ {1, 2, 3}         TRUE
{1, 2, 3} ⊂ {1, 2, 3}     FALSE (karena A = B)
∅ ⊂ {1}                    TRUE
```

### 3.3 Kesamaan Himpunan

A = B jika dan hanya jika A ⊆ B DAN B ⊆ A.

Cara membuktikan A = B:
1. Tunjukkan bahwa setiap elemen A ada di B (A ⊆ B)
2. Tunjukkan bahwa setiap elemen B ada di A (B ⊆ A)

**Contoh:**
Buktikan {x ∈ ℤ | x² = 1} = {-1, 1}
- Jika x² = 1, maka x = 1 atau x = -1. Jadi himpunan kiri ⊆ {-1, 1}.
- (-1)² = 1 ✓ dan 1² = 1 ✓. Jadi {-1, 1} ⊆ himpunan kiri.
- Terbukti sama. ✓

### 3.4 Superset

B ⊇ A berarti B memuat semua elemen A (sama dengan A ⊆ B, dilihat dari sisi B).

---

## 4. Himpunan Kuasa (Power Set)

### 4.1 Definisi

**Power Set** P(A) atau 2^A adalah himpunan dari SEMUA subset A.

### 4.2 Contoh

```
A = {1, 2}
P(A) = {∅, {1}, {2}, {1,2}}
|P(A)| = 4 = 2²
```

```
B = {a, b, c}
P(B) = {∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}}
|P(B)| = 8 = 2³
```

### 4.3 Rumus Kardinalitas

Jika |A| = n, maka **|P(A)| = 2^n**

**Mengapa 2^n?**
Untuk setiap elemen dalam A, kita punya 2 pilihan: masukkan ke subset atau tidak.
Dengan n elemen, total pilihan = 2 x 2 x ... x 2 (n kali) = 2^n.

### 4.4 Sifat Power Set

- ∅ ∈ P(A) untuk semua A (himpunan kosong selalu subset)
- A ∈ P(A) untuk semua A (himpunan itu sendiri selalu subset)
- Jika A ⊆ B maka P(A) ⊆ P(B)

### 4.5 Soal Jebakan Power Set

**Soal:** |P(P(∅))| = ?
```
∅ = {} -> |∅| = 0
P(∅) = {∅} -> |P(∅)| = 1 = 2^0
P(P(∅)) = P({∅}) = {∅, {∅}} -> |P(P(∅))| = 2 = 2^1
```

**Soal:** |P(P(P(∅)))| = ?
```
P(P(P(∅))) = P({∅, {∅}}) 
|{∅, {∅}}| = 2
|P({∅, {∅}})| = 2^2 = 4
```

---

## 5. Operasi Himpunan

### 5.1 Gabungan (Union) -- A ∪ B

Himpunan semua elemen yang ada di A **atau** di B (atau keduanya).

```
A ∪ B = {x | x ∈ A atau x ∈ B}
```

**Contoh:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A ∪ B = {1, 2, 3, 4, 5, 6}
```

Sifat:
- A ∪ ∅ = A
- A ∪ U = U
- A ∪ A = A
- A ∪ B = B ∪ A (komutatif)

### 5.2 Irisan (Intersection) -- A ∩ B

Himpunan elemen yang ada di A **dan** di B (keduanya sekaligus).

```
A ∩ B = {x | x ∈ A dan x ∈ B}
```

**Contoh:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A ∩ B = {3, 4}
```

Sifat:
- A ∩ ∅ = ∅
- A ∩ U = A
- A ∩ A = A
- A ∩ B = B ∩ A (komutatif)

**Himpunan Saling Lepas (Disjoint):** A dan B disjoint jika A ∩ B = ∅.

### 5.3 Selisih (Difference) -- A - B atau A \ B

Elemen yang ada di A tetapi TIDAK ada di B.

```
A - B = {x | x ∈ A dan x ∉ B}
```

**Contoh:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A - B = {1, 2}
B - A = {5, 6}
```

> **Perhatian:** A - B TIDAK sama dengan B - A (tidak komutatif!).

### 5.4 Beda Simetris (Symmetric Difference) -- A △ B atau A ⊕ B

Elemen yang ada di tepat SATU dari A atau B (tapi tidak keduanya).

```
A △ B = (A - B) ∪ (B - A) = (A ∪ B) - (A ∩ B)
```

**Contoh:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A △ B = {1, 2, 5, 6}
```

> Beda simetris ekuivalen dengan XOR pada level himpunan!

### 5.5 Komplemen -- A' atau Aᶜ

Semua elemen di semesta U yang TIDAK ada di A.

```
Aᶜ = U - A = {x ∈ U | x ∉ A}
```

**Contoh:**
```
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {2, 4, 6, 8, 10}
Aᶜ = {1, 3, 5, 7, 9}
```

Sifat:
- (Aᶜ)ᶜ = A
- A ∪ Aᶜ = U
- A ∩ Aᶜ = ∅
- ∅ᶜ = U
- Uᶜ = ∅

### 5.6 Produk Kartesian -- A x B

Himpunan semua pasangan terurut (a, b) dengan a ∈ A dan b ∈ B.

```
A × B = {(a, b) | a ∈ A, b ∈ B}
```

**Contoh:**
```
A = {1, 2, 3}
B = {x, y}
A × B = {(1,x), (1,y), (2,x), (2,y), (3,x), (3,y)}
|A × B| = |A| × |B| = 3 × 2 = 6
```

Sifat:
- A × B ≠ B × A (umumnya, kecuali A = B atau ada yang kosong)
- |A × B| = |A| · |B|
- A × ∅ = ∅

---

## 6. Hukum-Hukum Himpunan

### 6.1 Daftar Lengkap

| No | Hukum | Bentuk Union | Bentuk Intersection |
|----|-------|-------------|-------------------|
| 1 | Identitas | A ∪ ∅ = A | A ∩ U = A |
| 2 | Dominasi | A ∪ U = U | A ∩ ∅ = ∅ |
| 3 | Idempoten | A ∪ A = A | A ∩ A = A |
| 4 | Komplemen | A ∪ Aᶜ = U | A ∩ Aᶜ = ∅ |
| 5 | Involusi | (Aᶜ)ᶜ = A | (Aᶜ)ᶜ = A |
| 6 | Komutatif | A ∪ B = B ∪ A | A ∩ B = B ∩ A |
| 7 | Asosiatif | (A∪B)∪C = A∪(B∪C) | (A∩B)∩C = A∩(B∩C) |
| 8 | Distributif | A∩(B∪C) = (A∩B)∪(A∩C) | A∪(B∩C) = (A∪B)∩(A∪C) |
| 9 | De Morgan | (A∪B)ᶜ = Aᶜ∩Bᶜ | (A∩B)ᶜ = Aᶜ∪Bᶜ |
| 10 | Absorpsi | A∪(A∩B) = A | A∩(A∪B) = A |

### 6.2 Koneksi dengan Aljabar Boolean

Hukum-hukum himpunan IDENTIK dengan hukum aljabar Boolean!

| Aljabar Boolean | Teori Himpunan |
|----------------|----------------|
| 0 (FALSE) | ∅ (himpunan kosong) |
| 1 (TRUE) | U (semesta) |
| AND (·) | ∩ (intersection) |
| OR (+) | ∪ (union) |
| NOT (') | Komplemen (ᶜ) |
| XOR (⊕) | Beda simetris (△) |

Ini berarti setiap identitas Boolean memiliki padanan di teori himpunan dan sebaliknya.
Contoh: De Morgan di Boolean `(A·B)' = A' + B'` sama dengan De Morgan di himpunan `(A∩B)ᶜ = Aᶜ∪Bᶜ`.

### 6.3 Pembuktian Identitas Himpunan

**Metode 1: Elemen-by-elemen (paling formal)**

Buktikan: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ

```
Ambil x ∈ (A ∪ B)ᶜ
⟺ x ∉ (A ∪ B)                      [definisi komplemen]
⟺ ¬(x ∈ A ∨ x ∈ B)                 [definisi union]
⟺ (x ∉ A) ∧ (x ∉ B)               [De Morgan logika]
⟺ x ∈ Aᶜ ∧ x ∈ Bᶜ                 [definisi komplemen]
⟺ x ∈ (Aᶜ ∩ Bᶜ)                   [definisi intersection]

Karena kedua arah terbukti, (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ. ✓
```

**Metode 2: Menggunakan hukum-hukum (aljabar)**

Buktikan: A ∪ (A ∩ B) = A [Absorpsi]

```
A ∪ (A ∩ B)
= (A ∩ U) ∪ (A ∩ B)         [Identitas: A = A ∩ U]
= A ∩ (U ∪ B)               [Distributif]
= A ∩ U                     [Dominasi: U ∪ B = U]
= A                         [Identitas]
```

---

## 7. Diagram Venn

### 7.1 Representasi Visual

Diagram Venn menggunakan lingkaran (atau bentuk tertutup lain) untuk merepresentasikan
himpunan. Area yang tumpang tindih menunjukkan irisan.

**2 Himpunan:**
```
Semesta U
┌────────────────────────────────┐
│                                │
│    ┌─────────┬─────────┐      │
│    │         │         │      │
│    │   A-B   │  A ∩ B  │      │
│    │         │         │      │
│    │         │    B-A  │      │
│    └─────────┴─────────┘      │
│                                │
│         (A ∪ B)ᶜ              │
└────────────────────────────────┘
```

Daerah-daerah:
- A - B: di A saja (bukan di B)
- A ∩ B: di keduanya
- B - A: di B saja (bukan di A)
- (A ∪ B)ᶜ: di luar keduanya

### 7.2 Diagram Venn 3 Himpunan

Dengan 3 himpunan A, B, C terdapat 8 daerah:

```
Semesta U
┌──────────────────────────────────────┐
│            ┌───────┐                 │
│           /    A    \                │
│          /           \               │
│    ┌────/──┐     ┌───\────┐         │
│    │   / AB│     │BC  \   │         │
│    │  /    │ ABC │     \  │         │
│    │ B     │     │      C │         │
│    │  \    │     │     /  │         │
│    │   \   │     │    /   │         │
│    └────\──┘     └───/────┘         │
│          \           /               │
│           \_________/                │
│                                      │
│              di luar semua           │
└──────────────────────────────────────┘
```

8 daerah = 2^3 kombinasi keanggotaan {di A / tidak} x {di B / tidak} x {di C / tidak}

### 7.3 Menggunakan Diagram Venn untuk Menghitung

**Contoh:** Dari 100 siswa: 60 suka Matematika (M), 50 suka Fisika (F),
40 suka Kimia (K), 30 suka M dan F, 25 suka M dan K, 20 suka F dan K,
15 suka ketiganya. Berapa yang tidak suka satupun?

Mengisi diagram Venn dari dalam ke luar:
```
Hanya M∩F∩K = 15
Hanya M∩F (tanpa K) = 30 - 15 = 15
Hanya M∩K (tanpa F) = 25 - 15 = 10
Hanya F∩K (tanpa M) = 20 - 15 = 5
Hanya M (tanpa F dan K) = 60 - 15 - 15 - 10 = 20
Hanya F (tanpa M dan K) = 50 - 15 - 15 - 5 = 15
Hanya K (tanpa M dan F) = 40 - 15 - 10 - 5 = 10

Total yang suka minimal 1 = 20 + 15 + 10 + 15 + 10 + 5 + 15 = 90
Tidak suka satupun = 100 - 90 = 10 siswa
```

---

## 8. Prinsip Inklusi-Eksklusi (PIE)

### 8.1 PIE untuk 2 Himpunan

```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Intuisi:** Jika kita hanya menjumlahkan |A| + |B|, elemen yang ada di keduanya
terhitung dua kali. Maka dikurangi sekali.

### 8.2 PIE untuk 3 Himpunan

```
|A ∪ B ∪ C| = |A| + |B| + |C|
             - |A ∩ B| - |A ∩ C| - |B ∩ C|
             + |A ∩ B ∩ C|
```

**Intuisi:** 
- Tambah semua: elemen di 2 himpunan terhitung 2x, di 3 himpunan terhitung 3x.
- Kurangi pasangan: elemen di 2 himpunan jadi terhitung 0x (dikurangi 1x dari 2x = 0x, harusnya 1x). Elemen di 3 himpunan: 3 - 3 = 0 (harusnya 1x).
- Tambah triplet: elemen di 3 himpunan jadi 3 - 3 + 1 = 1x. Sempurna!

### 8.3 PIE untuk 4 Himpunan

```
|A ∪ B ∪ C ∪ D| = Σ|single| - Σ|pairs| + Σ|triples| - |A ∩ B ∩ C ∩ D|
```

Secara eksplisit:
```
= |A| + |B| + |C| + |D|
- |A∩B| - |A∩C| - |A∩D| - |B∩C| - |B∩D| - |C∩D|
+ |A∩B∩C| + |A∩B∩D| + |A∩C∩D| + |B∩C∩D|
- |A∩B∩C∩D|
```

### 8.4 Rumus Umum PIE untuk n Himpunan

```
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σᵢ|Aᵢ| - Σᵢ<ⱼ|Aᵢ ∩ Aⱼ| + Σᵢ<ⱼ<ₖ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)^(n+1)|A₁ ∩ A₂ ∩ ... ∩ Aₙ|
```

Pola: tambah satu, kurang dua, tambah tiga, kurang empat, ...

### 8.5 Contoh PIE Lengkap

**Contoh 1 (2 himpunan):**
Dari 50 mahasiswa, 30 mengambil Kalkulus, 25 mengambil Aljabar, 10 mengambil keduanya.
Berapa yang tidak mengambil keduanya?

```
|K ∪ A| = 30 + 25 - 10 = 45
Yang tidak mengambil = 50 - 45 = 5 mahasiswa
```

**Contoh 2 (3 himpunan):**
Di sebuah kelas berisi 40 siswa:
- 25 siswa suka membaca (M)
- 20 siswa suka olahraga (O)
- 15 siswa suka musik (Mu)
- 10 suka membaca dan olahraga
- 8 suka membaca dan musik
- 6 suka olahraga dan musik
- 3 suka ketiganya

Berapa siswa yang suka tepat satu kegiatan?

```
Langkah 1: Hitung |M ∪ O ∪ Mu|
= 25 + 20 + 15 - 10 - 8 - 6 + 3 = 39

Langkah 2: Hitung yang suka tepat 2 kegiatan
Tepat M dan O (bukan Mu) = 10 - 3 = 7
Tepat M dan Mu (bukan O) = 8 - 3 = 5
Tepat O dan Mu (bukan M) = 6 - 3 = 3
Total tepat 2 = 7 + 5 + 3 = 15

Langkah 3: Tepat 3 kegiatan = 3

Langkah 4: Tepat 1 kegiatan = 39 - 15 - 3 = 21 siswa
```

**Contoh 3 (PIE untuk menghitung bilangan):**
Berapa bilangan dari 1 sampai 100 yang habis dibagi 2 atau 3 atau 5?

```
A = {habis dibagi 2}, |A| = 50
B = {habis dibagi 3}, |B| = 33
C = {habis dibagi 5}, |C| = 20
A∩B = {habis dibagi 6}, |A∩B| = 16
A∩C = {habis dibagi 10}, |A∩C| = 10
B∩C = {habis dibagi 15}, |B∩C| = 6
A∩B∩C = {habis dibagi 30}, |A∩B∩C| = 3

|A ∪ B ∪ C| = 50 + 33 + 20 - 16 - 10 - 6 + 3 = 74

Jawaban: 74 bilangan
```

---

## 9. Partisi Himpunan

### 9.1 Definisi

**Partisi** dari himpunan S adalah kumpulan subset {A₁, A₂, ..., Aₙ} yang memenuhi:
1. Tidak ada yang kosong: Aᵢ ≠ ∅ untuk semua i
2. Saling lepas: Aᵢ ∩ Aⱼ = ∅ untuk i ≠ j
3. Menutupi semua: A₁ ∪ A₂ ∪ ... ∪ Aₙ = S

### 9.2 Contoh Partisi

```
S = {1, 2, 3, 4, 5, 6}

Partisi valid:
- {{1,2}, {3,4}, {5,6}}
- {{1,3,5}, {2,4,6}}     (ganjil dan genap)
- {{1}, {2}, {3}, {4}, {5}, {6}}  (setiap elemen terpisah)
- {{1,2,3,4,5,6}}        (satu blok besar)

Bukan partisi:
- {{1,2}, {2,3}, {4,5,6}}  (2 muncul di dua subset -- tidak saling lepas)
- {{1,2}, {4,5,6}}          (3 tidak termasuk -- tidak menutupi semua)
```

### 9.3 Bilangan Partisi (Bell Number)

Bilangan Bell Bₙ menghitung banyaknya partisi dari himpunan n elemen.

| n | Bₙ | Partisi-partisi |
|---|------|-----------------|
| 0 | 1 | {∅} |
| 1 | 1 | {{a}} |
| 2 | 2 | {{a,b}}, {{a},{b}} |
| 3 | 5 | {{a,b,c}}, {{a,b},{c}}, {{a,c},{b}}, {{b,c},{a}}, {{a},{b},{c}} |
| 4 | 15 | ... |
| 5 | 52 | ... |

---

## 10. Multiset (Himpunan Ganda)

### 10.1 Definisi

**Multiset** adalah generalisasi himpunan di mana elemen boleh muncul lebih dari sekali.
Berbeda dengan himpunan biasa yang mengabaikan duplikat.

Notasi: menggunakan kurung ganda atau notasi multiplisitas.
```
M = {1, 1, 2, 3, 3, 3}    (multiset)
```

Dalam notasi multiplisitas:
```
M = {1², 2¹, 3³}
```

### 10.2 Kardinalitas Multiset

Kardinalitas multiset = total semua kemunculan elemen.
```
|M| = 2 + 1 + 3 = 6
```

Jumlah elemen berbeda (support) = 3 ({1, 2, 3})

### 10.3 Koefisien Multinomial dan Multiset

Banyaknya cara memilih k elemen dari n jenis (dengan pengulangan dibolehkan):
```
C(n+k-1, k) = C(n+k-1, n-1)
```

**Contoh:** Berapa cara memilih 3 buah dari 4 jenis buah (apel, jeruk, mangga, anggur)?
```
n = 4 (jenis), k = 3 (yang dipilih)
C(4+3-1, 3) = C(6, 3) = 20 cara
```

---

## 11. Aplikasi Counting dengan Himpunan

### 11.1 Euler's Totient Function (Fungsi Phi Euler)

φ(n) = banyaknya bilangan dari 1 sampai n yang relatif prima dengan n.

Menggunakan PIE:
```
φ(n) = n × ∏(1 - 1/p) untuk semua faktor prima p dari n
```

**Contoh:** φ(12) = ?
```
12 = 2² × 3
φ(12) = 12 × (1 - 1/2) × (1 - 1/3) = 12 × 1/2 × 2/3 = 4
Verifikasi: {1, 5, 7, 11} relatif prima dengan 12. Ada 4. ✓
```

### 11.2 Derangement (Permutasi Tanpa Titik Tetap)

**Derangement** adalah permutasi di mana TIDAK ada elemen yang menempati posisi aslinya.

Notasi: Dₙ atau !n

**Rumus menggunakan PIE:**
```
Dₙ = n! × Σᵢ₌₀ⁿ (-1)ⁱ/i!
   = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!)
```

**Contoh:** D₃ (3 orang salah ambil topi)
```
D₃ = 3! × (1 - 1 + 1/2 - 1/6)
   = 6 × (1/2 - 1/6)
   = 6 × 2/6
   = 2

Verifikasi: dari (1,2,3), derangement = {(2,3,1), (3,1,2)}. Ada 2. ✓
```

Nilai-nilai derangement:
| n | n! | Dₙ | Dₙ/n! |
|---|----|----|--------|
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1 | 0.5 |
| 3 | 6 | 2 | 0.333 |
| 4 | 24 | 9 | 0.375 |
| 5 | 120 | 44 | 0.367 |

> Untuk n besar, Dₙ/n! mendekati 1/e ≈ 0.368

### 11.3 Surjeksi (Fungsi Onto)

Banyaknya fungsi surjektif dari himpunan n elemen ke himpunan k elemen:
```
S(n,k) = Σᵢ₌₀ᵏ (-1)ⁱ × C(k,i) × (k-i)ⁿ
```

**Contoh:** Berapa fungsi surjektif dari {1,2,3} ke {a,b}?
```
n=3, k=2
S(3,2) = C(2,0)×2³ - C(2,1)×1³ + C(2,2)×0³
       = 1×8 - 2×1 + 1×0
       = 8 - 2 + 0 = 6

Verifikasi: Total fungsi = 2³ = 8.
Fungsi non-surjektif: semua ke a (1 cara) + semua ke b (1 cara) = 2.
Surjektif = 8 - 2 = 6. ✓
```

---

## 12. Contoh Soal Lengkap (Worked Examples)

### Contoh 1: Operasi Himpunan Dasar

**Soal:** Diketahui U = {1,2,...,10}, A = {1,2,3,4,5}, B = {2,4,6,8,10}, C = {1,3,5,7,9}.
Tentukan: (A ∩ B) ∪ (B ∩ C)

**Solusi:**
```
A ∩ B = {2, 4}           (elemen yang di A dan B)
B ∩ C = {}               (B={genap}, C={ganjil}, tidak ada irisan)
(A ∩ B) ∪ (B ∩ C) = {2, 4} ∪ ∅ = {2, 4}
```

### Contoh 2: Power Set dan Subset

**Soal:** Berapa banyak subset dari {1,2,3,4,5} yang mengandung angka 1?

**Solusi:**
```
Jika 1 HARUS ada di subset, maka kita tinggal memilih
dari sisa 4 elemen: {2,3,4,5}, masing-masing boleh masuk atau tidak.

Banyak subset = 2⁴ = 16
```

### Contoh 3: PIE Klasik

**Soal:** Berapa banyak bilangan bulat dari 1 sampai 1000 yang TIDAK habis dibagi 3, 5, maupun 7?

**Solusi:**
```
A₃ = {habis dibagi 3}, |A₃| = ⌊1000/3⌋ = 333
A₅ = {habis dibagi 5}, |A₅| = ⌊1000/5⌋ = 200
A₇ = {habis dibagi 7}, |A₇| = ⌊1000/7⌋ = 142
|A₃ ∩ A₅| = ⌊1000/15⌋ = 66
|A₃ ∩ A₇| = ⌊1000/21⌋ = 47
|A₅ ∩ A₇| = ⌊1000/35⌋ = 28
|A₃ ∩ A₅ ∩ A₇| = ⌊1000/105⌋ = 9

|A₃ ∪ A₅ ∪ A₇| = 333 + 200 + 142 - 66 - 47 - 28 + 9 = 543

Yang TIDAK habis dibagi satupun = 1000 - 543 = 457
```

### Contoh 4: Diagram Venn dengan Soal Cerita

**Soal:** Sebuah survei terhadap 80 orang menunjukkan:
- 45 orang membaca koran A
- 35 orang membaca koran B
- 20 orang membaca koran C
- 15 orang membaca A dan B
- 12 orang membaca A dan C
- 10 orang membaca B dan C
- 5 orang membaca ketiga koran

Berapa orang yang:
a) Membaca tepat satu koran?
b) Membaca tepat dua koran?
c) Tidak membaca koran apapun?

**Solusi:**
```
a) Isi dari dalam ke luar:
   Ketiganya = 5
   Tepat A dan B = 15 - 5 = 10
   Tepat A dan C = 12 - 5 = 7
   Tepat B dan C = 10 - 5 = 5
   Hanya A = 45 - 10 - 7 - 5 = 23
   Hanya B = 35 - 10 - 5 - 5 = 15
   Hanya C = 20 - 7 - 5 - 5 = 3

   Tepat satu koran = 23 + 15 + 3 = 41 orang

b) Tepat dua koran = 10 + 7 + 5 = 22 orang

c) Total pembaca = 41 + 22 + 5 = 68
   Tidak membaca = 80 - 68 = 12 orang

Verifikasi dengan PIE:
|A∪B∪C| = 45 + 35 + 20 - 15 - 12 - 10 + 5 = 68 ✓
```

### Contoh 5: Produk Kartesian

**Soal:** A = {1, 2, 3}, B = {a, b}. Berapa elemen A x B yang komponen pertamanya ganjil?

**Solusi:**
```
A × B = {(1,a), (1,b), (2,a), (2,b), (3,a), (3,b)}

Komponen pertama ganjil: 1 dan 3
Pasangan yang memenuhi: {(1,a), (1,b), (3,a), (3,b)}

Jawaban: 4 elemen

Cara cepat: elemen ganjil di A = {1,3}, ada 2 elemen
Dipasangkan dengan semua elemen B (2 elemen)
Total = 2 × 2 = 4
```

### Contoh 6: Subset dan Kesamaan

**Soal:** Tentukan semua himpunan A yang memenuhi {1, 2} ⊆ A ⊆ {1, 2, 3, 4, 5}.

**Solusi:**
```
A harus mengandung 1 dan 2 (karena {1,2} ⊆ A).
A harus subset dari {1,2,3,4,5}.

Jadi A = {1, 2} ∪ S, dimana S ⊆ {3, 4, 5}.

Banyak pilihan S = 2³ = 8.

Himpunan A yang mungkin:
{1,2}, {1,2,3}, {1,2,4}, {1,2,5}, {1,2,3,4}, {1,2,3,5}, {1,2,4,5}, {1,2,3,4,5}
```

### Contoh 7: De Morgan pada Himpunan

**Soal:** U = {1,...,10}, A = {1,2,3,4}, B = {3,4,5,6}. Verifikasi (A∪B)ᶜ = Aᶜ∩Bᶜ.

**Solusi:**
```
Sisi kiri:
A ∪ B = {1,2,3,4,5,6}
(A ∪ B)ᶜ = {7, 8, 9, 10}

Sisi kanan:
Aᶜ = {5, 6, 7, 8, 9, 10}
Bᶜ = {1, 2, 7, 8, 9, 10}
Aᶜ ∩ Bᶜ = {7, 8, 9, 10}

Kedua sisi sama: {7, 8, 9, 10}. Terverifikasi! ✓
```

### Contoh 8: Derangement

**Soal:** 4 siswa menitipkan tas. Berapa cara pengembalian tas sehingga
TIDAK ada siswa yang mendapat tasnya sendiri?

**Solusi:**
```
Ini adalah derangement D₄.

D₄ = 4! × (1 - 1/1! + 1/2! - 1/3! + 1/4!)
   = 24 × (1 - 1 + 1/2 - 1/6 + 1/24)
   = 24 × (12/24 - 4/24 + 1/24)
   = 24 × 9/24
   = 9

Jawaban: 9 cara
```

### Contoh 9: PIE dan Euler Totient

**Soal:** Berapa banyak bilangan dari 1 sampai 30 yang relatif prima dengan 30?

**Solusi:**
```
30 = 2 × 3 × 5

φ(30) = 30 × (1 - 1/2) × (1 - 1/3) × (1 - 1/5)
      = 30 × 1/2 × 2/3 × 4/5
      = 30 × 8/30
      = 8

Jawaban: 8 bilangan

Verifikasi: {1, 7, 11, 13, 17, 19, 23, 29} -- ada 8. ✓
```

### Contoh 10: Soal Kombinasi PIE dan Himpunan

**Soal:** Dari 200 siswa yang mengikuti survei:
- 120 suka coklat
- 90 suka vanilla
- 80 suka stroberi
- 50 suka coklat dan vanilla
- 40 suka coklat dan stroberi
- 30 suka vanilla dan stroberi
- 20 suka ketiganya

a) Berapa yang suka tepat 2 rasa?
b) Berapa yang tidak suka satupun?

**Solusi:**
```
a) Tepat 2 rasa:
   Tepat coklat & vanilla (bukan stroberi) = 50 - 20 = 30
   Tepat coklat & stroberi (bukan vanilla) = 40 - 20 = 20
   Tepat vanilla & stroberi (bukan coklat) = 30 - 20 = 10
   Total tepat 2 = 30 + 20 + 10 = 60 siswa

b) |C ∪ V ∪ S| = 120 + 90 + 80 - 50 - 40 - 30 + 20 = 190
   Tidak suka satupun = 200 - 190 = 10 siswa
```

### Contoh 11: Beda Simetris

**Soal:** A = {1,2,3,4,5}, B = {3,4,5,6,7}, C = {5,6,7,8,9}.
Tentukan (A △ B) △ C.

**Solusi:**
```
Langkah 1: A △ B
A - B = {1, 2}
B - A = {6, 7}
A △ B = {1, 2, 6, 7}

Langkah 2: (A △ B) △ C
(A △ B) - C = {1, 2, 6, 7} - {5,6,7,8,9} = {1, 2}
C - (A △ B) = {5,6,7,8,9} - {1,2,6,7} = {5, 8, 9}
(A △ B) △ C = {1, 2, 5, 8, 9}
```

> Fakta menarik: A △ B △ C berisi elemen yang muncul di jumlah ganjil dari himpunan A, B, C.
> - 1: hanya di A (1 himpunan - ganjil) ✓
> - 5: di A, B, C (3 himpunan - ganjil) ✓
> - 8: hanya di C (1 himpunan - ganjil) ✓

### Contoh 12: Soal Gaya OSN - Counting dengan Himpunan

**Soal:** Berapa banyak bilangan 4-digit (1000-9999) yang digit-digitnya semua berbeda
DAN mengandung setidaknya satu digit genap?

**Solusi:**
```
Metode: Total digit berbeda - digit berbeda TANPA digit genap

Total bilangan 4-digit dengan semua digit berbeda:
- Digit pertama: 9 pilihan (1-9, tidak boleh 0)
- Digit kedua: 9 pilihan (0-9 kecuali digit pertama)
- Digit ketiga: 8 pilihan
- Digit keempat: 7 pilihan
Total = 9 × 9 × 8 × 7 = 4536

Bilangan 4-digit dengan semua digit berbeda DAN semua ganjil:
Digit ganjil: {1, 3, 5, 7, 9} -- ada 5
- Digit pertama: 5 pilihan (semua ganjil boleh di awal)
- Digit kedua: 4 pilihan (sisa digit ganjil)
- Digit ketiga: 3 pilihan
- Digit keempat: 2 pilihan
Total = 5 × 4 × 3 × 2 = 120

Jawaban: 4536 - 120 = 4416 bilangan
```

---

## 13. Tips dan Jebakan OSN

### 13.1 Jebakan Umum

1. **∅ vs {∅}:**
   - ∅ tidak punya anggota, |∅| = 0
   - {∅} punya satu anggota (yaitu ∅), |{∅}| = 1
   - ∅ ⊆ {∅} (TRUE), tapi ∅ ∈ {∅} (juga TRUE!)

2. **Subset vs Elemen:**
   - {1} ⊆ {1, 2, 3} (TRUE -- {1} adalah subset)
   - {1} ∈ {1, 2, 3} (FALSE -- elemen-elemen {1,2,3} adalah angka, bukan himpunan)
   - {1} ∈ {{1}, {2}, {3}} (TRUE -- {1} adalah elemen dari himpunan itu)

3. **A - B bukan B - A:**
   Selisih himpunan TIDAK komutatif.

4. **Hati-hati tanda kurung di PIE:**
   |A ∩ B| bukan |A| ∩ |B|. Hitung irisannya dulu, baru hitung kardinalitasnya.

5. **Floor function di PIE bilangan:**
   ⌊1000/3⌋ = 333, bukan 333.33. Selalu bulatkan ke bawah.

### 13.2 Strategi Mengerjakan Soal Himpunan

1. **Identifikasi tipe soal:** PIE? Operasi biasa? Power set?
2. **Untuk soal cerita:** Tentukan himpunan-himpunan yang terlibat, lalu terapkan rumus.
3. **Untuk verifikasi:** Gunakan diagram Venn kecil atau contoh numerik.
4. **Untuk pembuktian:** Gunakan metode elemen (ambil x sembarang, buktikan keanggotaan).
5. **PIE selalu bergantian tanda:** +, -, +, -, ...

### 13.3 Rumus Cepat

```
|P(A)| = 2^|A|                          [Banyak subset]
|A × B| = |A| × |B|                     [Produk kartesian]
|A ∪ B| = |A| + |B| - |A ∩ B|          [PIE 2 himpunan]
|A - B| = |A| - |A ∩ B|                 [Selisih = total dikurangi irisan]
|A △ B| = |A| + |B| - 2|A ∩ B|         [Beda simetris]
Dₙ ≈ n!/e (dibulatkan ke terdekat)     [Derangement cepat]
φ(n) = n × ∏(1 - 1/p)                  [Euler totient]
```

---

## 14. Latihan Soal

### Bagian A: Operasi Dasar (Mudah)

1. U = {1,...,12}, A = {x | x habis dibagi 3}, B = {x | x habis dibagi 4}.
   Tentukan A ∩ B, A ∪ B, A - B, dan (A ∪ B)ᶜ.

2. Diketahui |A| = 10, |B| = 8, |A ∩ B| = 3. Tentukan |A ∪ B| dan |A - B|.

3. Tentukan P({a, b}) dan |P({a, b})|.

4. Apakah pernyataan berikut TRUE atau FALSE?
   a) ∅ ⊆ ∅
   b) ∅ ∈ {∅, {∅}}
   c) {1} ⊆ {{1}, 2}
   d) {1} ∈ {{1}, 2}

### Bagian B: PIE dan Counting (Sedang)

5. Dari 60 siswa: 35 suka basket, 30 suka futsal, 15 suka keduanya.
   Berapa yang tidak suka basket maupun futsal?

6. Berapa bilangan dari 1-500 yang habis dibagi 4 atau 6 tapi tidak habis dibagi keduanya (4 dan 6)?

7. Berapa banyak subset dari {1,2,3,4,5,6} yang memiliki kardinalitas genap?

8. Hitung D₅ (derangement 5 elemen).

### Bagian C: Soal Cerita dan Pembuktian (Sedang-Sulit)

9. Buktikan bahwa A - (B ∩ C) = (A - B) ∪ (A - C) menggunakan metode elemen.

10. Dari 150 peserta olimpiade: 80 mengambil Matematika, 70 mengambil Fisika,
    60 mengambil Informatika, 30 mengambil Mat+Fis, 25 mengambil Mat+Inf,
    20 mengambil Fis+Inf, 10 mengambil ketiganya.
    a) Berapa yang mengambil tepat satu bidang?
    b) Berapa yang tidak mengambil bidang apapun?

11. Sebuah kelas berisi 30 siswa. 18 siswa suka apel, 15 suka jeruk, 12 suka mangga.
    Berapa minimal siswa yang suka ketiga buah?

### Bagian D: Soal Gaya OSN (Sulit)

12. Berapa banyak fungsi f: {1,2,3,4} -> {a,b,c} yang surjektif?

13. Berapa banyak bilangan dari 1 sampai 100 yang relatif prima dengan 100?
    (Petunjuk: 100 = 2² × 5²)

14. Lima surat dimasukkan secara acak ke 5 amplop. Berapa probabilitas tidak ada surat
    yang masuk ke amplop yang benar?

15. Diketahui |A| = 5, |B| = 3. Berapa banyak kemungkinan nilai |A ∪ B|?
    Tentukan nilai minimum dan maksimumnya.

---

## 15. Kunci Jawaban Latihan

### Jawaban Bagian A:

**1.** A = {3,6,9,12}, B = {4,8,12}
```
A ∩ B = {12}
A ∪ B = {3,4,6,8,9,12}
A - B = {3,6,9}
(A ∪ B)ᶜ = {1,2,5,7,10,11}
```

**2.**
```
|A ∪ B| = 10 + 8 - 3 = 15
|A - B| = |A| - |A ∩ B| = 10 - 3 = 7
```

**3.**
```
P({a,b}) = {∅, {a}, {b}, {a,b}}
|P({a,b})| = 2² = 4
```

**4.**
```
a) ∅ ⊆ ∅ -> TRUE (himpunan kosong adalah subset semua himpunan, termasuk dirinya)
b) ∅ ∈ {∅, {∅}} -> TRUE (∅ adalah salah satu elemen yang terdaftar)
c) {1} ⊆ {{1}, 2} -> FALSE (elemen {1} adalah "1", tapi anggota {{1},2} adalah "{1}" dan "2", bukan "1")
d) {1} ∈ {{1}, 2} -> TRUE ({1} adalah salah satu elemen yang terdaftar)
```

### Jawaban Bagian B:

**5.**
```
|B ∪ F| = 35 + 30 - 15 = 50
Tidak suka keduanya = 60 - 50 = 10 siswa
```

**6.**
```
Habis dibagi 4: ⌊500/4⌋ = 125
Habis dibagi 6: ⌊500/6⌋ = 83
Habis dibagi 4 DAN 6 = habis dibagi LCM(4,6) = 12: ⌊500/12⌋ = 41

Habis dibagi 4 ATAU 6 = 125 + 83 - 41 = 167
Habis dibagi 4 atau 6 TAPI BUKAN keduanya = beda simetris
= 167 - 41 = 126

Atau: (habis dibagi 4 saja) + (habis dibagi 6 saja) = (125-41) + (83-41) = 84 + 42 = 126
```

**7.**
```
Subset dari {1,2,3,4,5,6}:
Total subset = 2⁶ = 64
Subset berukuran genap (0, 2, 4, 6):
C(6,0) + C(6,2) + C(6,4) + C(6,6) = 1 + 15 + 15 + 1 = 32

Atau gunakan fakta: jumlah subset berukuran genap = jumlah subset berukuran ganjil = 2^(n-1) = 32
```

**8.** D₅:
```
D₅ = 5! × (1 - 1 + 1/2 - 1/6 + 1/24 - 1/120)
   = 120 × (60/120 - 20/120 + 5/120 - 1/120)
   = 120 × 44/120
   = 44
```

### Jawaban Bagian C:

**9.** Buktikan A - (B ∩ C) = (A - B) ∪ (A - C):
```
Ambil x ∈ A - (B ∩ C)
⟺ x ∈ A dan x ∉ (B ∩ C)
⟺ x ∈ A dan ¬(x ∈ B dan x ∈ C)
⟺ x ∈ A dan (x ∉ B atau x ∉ C)          [De Morgan]
⟺ (x ∈ A dan x ∉ B) atau (x ∈ A dan x ∉ C)  [Distributif]
⟺ x ∈ (A - B) atau x ∈ (A - C)
⟺ x ∈ (A - B) ∪ (A - C)

Terbukti. ✓
```

**10.**
```
a) |M ∪ F ∪ I| = 80+70+60-30-25-20+10 = 145
   Ketiganya = 10
   Tepat M dan F = 30-10 = 20
   Tepat M dan I = 25-10 = 15
   Tepat F dan I = 20-10 = 10
   Total tepat 2 = 20+15+10 = 45
   Tepat 1 = 145 - 45 - 10 = 90 siswa

b) Tidak mengambil = 150 - 145 = 5 siswa
```

**11.**
```
Minimal |A ∩ J ∩ M|:
Gunakan PIE: |A ∪ J ∪ M| ≤ 30 (karena hanya 30 siswa)
Juga: |A ∪ J ∪ M| = 18 + 15 + 12 - |A∩J| - |A∩M| - |J∩M| + |A∩J∩M|
= 45 - (|A∩J| + |A∩M| + |J∩M|) + |A∩J∩M|

Untuk minimum |A∩J∩M|, kita perlu maximum di irisan pasangan.
Batas: |A∩J| ≤ min(18,15) = 15, dll.
Juga |A∩J| + |A∩M| + |J∩M| ≤ |A∩J| + |A∩M| + |J∩M|

Gunakan batas bawah:
|A ∩ J| ≥ |A| + |J| - |U| = 18 + 15 - 30 = 3
|A ∩ M| ≥ 18 + 12 - 30 = 0
|J ∩ M| ≥ 15 + 12 - 30 = -3 -> 0

Untuk minimum A∩J∩M, gunakan:
|A ∩ J ∩ M| ≥ |A| + |J| + |M| - 2|U| = 18 + 15 + 12 - 2(30) = -15

Hmm, itu terlalu rendah. Gunakan pendekatan berbeda:
|A ∩ J ∩ M| ≥ |A ∩ J| + |M| - |U| ≥ (|A|+|J|-|U|) + |M| - |U|
= 18+15-30+12-30 = -15

Sebenarnya, batas bawah yang benar:
|A ∩ J ∩ M| ≥ |A| + |J| + |M| - 2n = 18 + 15 + 12 - 2(30) = 45 - 60 = -15

Karena negatif, minimum = 0.

Tapi tunggu, soal bertanya "minimal berapa yang suka ketiganya".
Menggunakan: setidaknya |A| + |J| + |M| - 2n jika positif, 0 jika negatif.
= max(0, 18+15+12-2×30) = max(0, -15) = 0

Namun ini juga bergantung konteks. Coba uraikan ulang:
Minimum terjadi ketika overlap seminimal mungkin.
Dengan 30 siswa, 18+15+12 = 45 "slot keanggotaan".
Setiap siswa bisa menempati 1-3 slot. Dengan 30 siswa:
- Jika semua menempati 1 slot: hanya 30 slot terpakai.
- Kita butuh 45 slot, jadi 45-30 = 15 slot ekstra harus didistribusikan.
- Setiap siswa di 2 himpunan berkontribusi 1 slot ekstra.
- Setiap siswa di 3 himpunan berkontribusi 2 slot ekstra.
- Minimumkan siswa di 3 himpunan: maksimalkan di 2 himpunan.
- Jika semua ekstra dari "2 himpunan": butuh 15 siswa di 2 himpunan.
- Tapi kita hanya punya 30 siswa total.
- Apakah ini feasible? Ya, karena 15 ≤ 30.
- Jadi minimum = 0 siswa suka ketiganya (jika 15 siswa ada di tepat 2).

Jawaban: Minimal 0 siswa yang suka ketiga buah.

Cek: 15 siswa di 2 himpunan, 15 siswa di 1 himpunan.
Slot: 15×2 + 15×1 = 30+15 = 45. ✓
```

### Jawaban Bagian D:

**12.** Fungsi surjektif f: {1,2,3,4} -> {a,b,c}:
```
n=4, k=3
S(4,3) = C(3,0)×3⁴ - C(3,1)×2⁴ + C(3,2)×1⁴ - C(3,3)×0⁴
       = 1×81 - 3×16 + 3×1 - 1×0
       = 81 - 48 + 3 - 0
       = 36
```

**13.** φ(100):
```
100 = 2² × 5²
φ(100) = 100 × (1 - 1/2) × (1 - 1/5)
       = 100 × 1/2 × 4/5
       = 40
```

**14.** Probabilitas derangement 5 surat:
```
D₅ = 44
Total permutasi = 5! = 120
Probabilitas = 44/120 = 11/30
```

**15.** Kemungkinan |A ∪ B|:
```
|A ∪ B| = |A| + |B| - |A ∩ B| = 5 + 3 - |A ∩ B| = 8 - |A ∩ B|

Batas |A ∩ B|:
- Minimum: max(0, |A|+|B|-|U|). Tanpa info U, minimum = 0
  (jika A dan B disjoint)
- Maximum: min(|A|, |B|) = min(5, 3) = 3
  (jika B ⊆ A)

Jadi |A ∩ B| ∈ {0, 1, 2, 3}
Dan |A ∪ B| ∈ {8-0, 8-1, 8-2, 8-3} = {8, 7, 6, 5}

Minimum |A ∪ B| = 5 (saat B ⊆ A)
Maximum |A ∪ B| = 8 (saat A dan B disjoint)
Banyak kemungkinan nilai = 4
```

---

## 16. Rangkuman

| Topik | Poin Kunci |
|-------|-----------|
| Notasi | Roster dan Set Builder. Urutan & duplikat tidak penting |
| Power Set | |P(A)| = 2^n. ∅ dan A sendiri selalu termasuk |
| Operasi | ∪, ∩, -, △, ᶜ, ×. Kuasai sifat masing-masing |
| PIE | Bergantian tanda. +singles, -pairs, +triples, ... |
| Partisi | Saling lepas, menutupi semua, tidak kosong |
| Derangement | Dₙ = n! × Σ(-1)ⁱ/i!, mendekati n!/e |
| Koneksi Boolean | ∪=OR, ∩=AND, ᶜ=NOT, △=XOR, ∅=0, U=1 |
| Jebakan | ∅ vs {∅}, subset vs elemen, A-B bukan B-A |

---

*Materi ini mencakup seluruh topik Teori Himpunan yang relevan untuk OSK Informatika 2026.*
