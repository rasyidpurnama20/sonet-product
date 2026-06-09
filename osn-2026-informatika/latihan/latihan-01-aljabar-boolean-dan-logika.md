# Latihan 01 — Aljabar Boolean & Logika

**Mata Pelajaran:** OSN Informatika 2026 — Bab 1  
**Jumlah Soal:** 35 soal  
**Tingkat Kesulitan:** Mudah (★), Sedang (★★), Sulit (★★★)  
**Tipe Soal:** Pilihan Ganda (PG), Isian Singkat (IS), Benar/Salah (B/S), Uraian (U)  
**Referensi Materi:** [01-aljabar-boolean-dan-logika.md](../materi/01-aljabar-boolean-dan-logika.md)

---

## Bagian A: Tabel Kebenaran dan Evaluasi Ekspresi

---

### Soal 1 — Evaluasi Gerbang Logika Campuran ★

**Tipe:** Isian Singkat

**Soal:**  
Tentukan nilai (0 atau 1) dari ekspresi berikut:

```
(1 NAND 1) OR (0 NOR 0)
```

**Pembahasan:**

```
Langkah 1: Hitung 1 NAND 1
  NAND = NOT(AND)
  1 AND 1 = 1
  NOT(1) = 0
  Jadi: 1 NAND 1 = 0

Langkah 2: Hitung 0 NOR 0
  NOR = NOT(OR)
  0 OR 0 = 0
  NOT(0) = 1
  Jadi: 0 NOR 0 = 1

Langkah 3: Hitung 0 OR 1 = 1
```

**Jawaban: 1**

---

### Soal 2 — Evaluasi XOR dan XNOR ★

**Tipe:** Isian Singkat

**Soal:**  
Jika A = 1, B = 0, C = 1, tentukan nilai dari:

```
(A XNOR B) AND (B XOR C)
```

**Pembahasan:**

```
Langkah 1: Hitung A XNOR B
  XNOR bernilai 1 jika kedua operand SAMA
  A = 1, B = 0 -> tidak sama
  Jadi: A XNOR B = 0

Langkah 2: Hitung B XOR C
  XOR bernilai 1 jika kedua operand BERBEDA
  B = 0, C = 1 -> berbeda
  Jadi: B XOR C = 1

Langkah 3: Hitung 0 AND 1 = 0
```

**Jawaban: 0**

---

### Soal 3 — Tabel Kebenaran Ekspresi 2 Variabel ★

**Tipe:** Uraian

**Soal:**  
Lengkapi tabel kebenaran untuk ekspresi: `(p → q) ∧ (q → p)`

| p | q | p → q | q → p | (p → q) ∧ (q → p) |
|---|---|-------|-------|-------------------|
| T | T | ? | ? | ? |
| T | F | ? | ? | ? |
| F | T | ? | ? | ? |
| F | F | ? | ? | ? |

Apakah ekspresi ini ekuivalen dengan operator lain yang sudah dikenal?

**Pembahasan:**

```
Baris 1: p=T, q=T
  p → q = T → T = T
  q → p = T → T = T
  T ∧ T = T

Baris 2: p=T, q=F
  p → q = T → F = F
  q → p = F → T = T
  F ∧ T = F

Baris 3: p=F, q=T
  p → q = F → T = T
  q → p = T → F = F
  T ∧ F = F

Baris 4: p=F, q=F
  p → q = F → F = T
  q → p = F → F = T
  T ∧ T = T
```

Tabel kebenaran lengkap:

| p | q | p → q | q → p | (p → q) ∧ (q → p) |
|---|---|-------|-------|-------------------|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | T | F | F |
| F | F | T | T | T |

Perhatikan kolom terakhir: bernilai T jika p dan q SAMA.

**Jawaban:** Ekspresi ini ekuivalen dengan **p ↔ q** (biimplikasi / XNOR).

---

### Soal 4 — Evaluasi Implikasi Berantai ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan p = TRUE, q = FALSE, r = TRUE. Tentukan nilai kebenaran dari:

```
(p → q) → (q → r)
```

**Pembahasan:**

```
Langkah 1: Hitung p → q
  p = T, q = F
  T → F = FALSE

Langkah 2: Hitung q → r
  q = F, r = T
  F → T = TRUE

Langkah 3: Hitung (p → q) → (q → r)
  FALSE → TRUE = TRUE
  (Ingat: F → apapun = T)
```

**Jawaban: TRUE**

---

### Soal 5 — Menghitung Jumlah Baris TRUE ★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak kombinasi nilai (p, q, r) yang membuat ekspresi berikut bernilai TRUE?

```
(p ∨ q) → r
```

**Pembahasan:**

```
Implikasi A → B bernilai FALSE hanya jika A = T dan B = F.
Jadi (p ∨ q) → r bernilai FALSE hanya jika (p ∨ q) = T dan r = F.

Kasus r = F:
  (p ∨ q) = T artinya setidaknya satu dari p, q bernilai T.
  Kombinasi (p, q) dengan p ∨ q = T: (T,T), (T,F), (F,T) -> 3 kombinasi
  
Jadi yang FALSE = 3 kombinasi (dengan r = F).
Total kombinasi = 2^3 = 8.
Yang TRUE = 8 - 3 = 5.
```

**Jawaban: 5 kombinasi**

---

### Soal 6 — Tabel Kebenaran 3 Variabel ★★

**Tipe:** Uraian

**Soal:**  
Buatlah tabel kebenaran untuk ekspresi: `(A ⊕ B) ∧ C`

Kemudian nyatakan hasilnya dalam bentuk Sum of Minterms: F = Sigma m(...)

**Pembahasan:**

| A | B | C | A ⊕ B | (A ⊕ B) ∧ C |
|---|---|---|-------|-------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |

```
Baris yang bernilai 1:
- Baris 4: A=0, B=1, C=1 -> minterm 3 (011 dalam biner)
- Baris 6: A=1, B=0, C=1 -> minterm 5 (101 dalam biner)
```

**Jawaban:** F(A,B,C) = Sigma m(3, 5) = A'BC + AB'C

---

### Soal 7 — Evaluasi Ekspresi C++ Boolean ★★

**Tipe:** Isian Singkat

**Soal:**  
Apa output dari potongan kode C++ berikut?

```cpp
int x = 7, y = 0, z = 3;
bool result = (x > z) && !(y || (x == z)) || (z > x);
cout << result;
```

**Pembahasan:**

```
Langkah 1: Evaluasi dalam tanda kurung terdalam
  x > z = 7 > 3 = true
  x == z = 7 == 3 = false
  z > x = 3 > 7 = false

Langkah 2: Evaluasi y || (x == z)
  y = 0 (false dalam konteks boolean)
  false || false = false

Langkah 3: Evaluasi !(false)
  !false = true

Langkah 4: Evaluasi (x > z) && true
  true && true = true

Langkah 5: Evaluasi true || (z > x)
  true || false = true
  (short-circuit: karena sisi kiri sudah true, sisi kanan tidak perlu dievaluasi)

Catatan prioritas: && lebih tinggi dari ||
  Jadi sebenarnya: ((x > z) && !(y || (x == z))) || (z > x)
  = (true && true) || false
  = true || false
  = true
```

**Jawaban: 1** (true)

---

### Soal 8 — Benar/Salah tentang Implikasi ★

**Tipe:** Benar/Salah

**Soal:**  
Tentukan apakah pernyataan-pernyataan berikut BENAR atau SALAH:

(a) Jika p → q bernilai TRUE, maka q → p pasti bernilai TRUE.  
(b) Jika p → q bernilai FALSE, maka p pasti bernilai TRUE.  
(c) (p → q) ekuivalen dengan (¬q → ¬p).  
(d) Jika ¬p → q bernilai TRUE dan q bernilai FALSE, maka p bernilai TRUE.  

**Pembahasan:**

```
(a) SALAH.
    Counterexample: p=F, q=T.
    p → q = F → T = T (TRUE)
    q → p = T → F = F (FALSE)
    Konvers tidak selalu ekuivalen dengan asli.

(b) BENAR.
    p → q bernilai FALSE hanya jika p = T dan q = F.
    Jadi p pasti TRUE.

(c) BENAR.
    (¬q → ¬p) adalah kontraposisi dari (p → q).
    Kontraposisi selalu ekuivalen dengan pernyataan asli.

(d) BENAR.
    ¬p → q bernilai TRUE dan q = FALSE.
    Modus Tollens: jika ¬p → q dan ¬q, maka ¬(¬p) = p.
    Jadi p = TRUE.
```

**Jawaban: (a) SALAH, (b) BENAR, (c) BENAR, (d) BENAR**

---

## Bagian B: Penyederhanaan Boolean

---

### Soal 9 — Penyederhanaan dengan Komplemen ★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan ekspresi berikut:

```
A · B · C + A · B · C' + A · B' · C + A · B' · C'
```

**Pembahasan:**

```
= A·B·C + A·B·C' + A·B'·C + A·B'·C'
= A·B·(C + C') + A·B'·(C + C')       [Distributif]
= A·B·1 + A·B'·1                      [Komplemen: C + C' = 1]
= A·B + A·B'                          [Identitas]
= A·(B + B')                          [Distributif]
= A·1                                 [Komplemen]
= A                                   [Identitas]
```

**Jawaban: A**

---

### Soal 10 — Penyederhanaan dengan Absorpsi ★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan ekspresi berikut:

```
A·B + A·B·C + A·B·C'·D
```

**Pembahasan:**

```
= A·B + A·B·C + A·B·C'·D

Perhatikan bahwa A·B adalah suku yang "menyerap" suku-suku lain.
Gunakan hukum absorpsi: X + X·Y = X

Langkah 1: A·B + A·B·C = A·B (absorpsi, karena A·B·C = (A·B)·C)
Langkah 2: A·B + A·B·C'·D = A·B (absorpsi, karena A·B·C'·D = (A·B)·(C'·D))

Jadi: A·B + A·B·C + A·B·C'·D = A·B
```

**Jawaban: A·B**

---

### Soal 11 — Penyederhanaan dengan Distributif ★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan ekspresi berikut:

```
(A + B) · (A + B')
```

**Pembahasan:**

```
Metode 1 (Distributif bentuk OR):
(A + B)·(A + B') = A + B·B'         [x+(y·z) bentuk khusus distributif OR]
                 = A + 0             [Komplemen: B·B' = 0]
                 = A                 [Identitas]

Metode 2 (Ekspansi FOIL):
(A + B)·(A + B')
= A·A + A·B' + B·A + B·B'
= A + A·B' + A·B + 0                [Idempoten, Komplemen]
= A + A·(B' + B)                    [Distributif]
= A + A·1                           [Komplemen]
= A + A                             [Identitas]
= A                                 [Idempoten]
```

**Jawaban: A**

---

### Soal 12 — Penyederhanaan dengan Hukum Konsensus ★★★

**Tipe:** Uraian

**Soal:**  
Sederhanakan ekspresi berikut menggunakan hukum konsensus:

```
A·B + A'·C + B·C
```

**Pembahasan:**

```
Hukum Konsensus: X·Y + X'·Z + Y·Z = X·Y + X'·Z
(Suku Y·Z adalah suku konsensus yang redundan)

Identifikasi:
- X = A, Y = B, Z = C
- Suku A·B -> cocok dengan X·Y
- Suku A'·C -> cocok dengan X'·Z
- Suku B·C -> ini adalah Y·Z (suku konsensus)

Maka: A·B + A'·C + B·C = A·B + A'·C

Verifikasi bahwa B·C redundan:
- Jika A = 1: A·B = B sudah mencakup kasus B·C (saat B=1)
- Jika A = 0: A'·C = C sudah mencakup kasus B·C (saat C=1)
```

**Jawaban: A·B + A'·C**

---

### Soal 13 — Penyederhanaan Bertingkat ★★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan ekspresi berikut:

```
(A' + B) · (A + B) · (A + B')
```

**Pembahasan:**

```
Langkah 1: Sederhanakan (A' + B)·(A + B)
  Gunakan distributif bentuk OR:
  (X + B)·(Y + B) = XY + B  [jika bentuknya (? + B)(? + B)]
  
  Cara lain: Distribusi biasa
  (A' + B)·(A + B) = A'·A + A'·B + B·A + B·B
                   = 0 + A'B + AB + B
                   = B·(A' + A) + B        -- tunggu, ini tidak rapi.
  
  Lebih baik:
  (A' + B)·(A + B) = (B + A')·(B + A)     [Komutatif]
                   = B + A'·A              [Distributif bentuk OR]
                   = B + 0                 [Komplemen]
                   = B

Langkah 2: B · (A + B')
  = A·B + B·B'
  = A·B + 0               [Komplemen]
  = A·B
```

**Jawaban: A·B**

---

### Soal 14 — Penyederhanaan Menggunakan K-Map ★★

**Tipe:** Isian Singkat

**Soal:**  
Gunakan K-Map untuk menyederhanakan:

```
F(A, B, C) = Sigma m(0, 1, 4, 5, 6, 7)
```

**Pembahasan:**

```
K-Map 3 variabel:
          BC=00  BC=01  BC=11  BC=10
A=0     |  1   |  1   |  0   |  0   |     m0  m1  m3  m2
A=1     |  1   |  1   |  1   |  1   |     m4  m5  m7  m6

Identifikasi grup:
- Grup 1: Seluruh baris A=1 (m4, m5, m7, m6) -> 4 sel -> A
- Grup 2: m0, m1, m4, m5 (kolom BC=00 dan BC=01) -> 4 sel -> C'
  Tunggu, cek: m0(000), m1(001), m4(100), m5(101)
  B selalu 0, tapi C berubah. Yang tetap: B=0, jadi B'.
  
  Salah, mari cek ulang:
  m0 = A'B'C' (000)
  m1 = A'B'C  (001)
  m4 = AB'C'  (100)
  m5 = AB'C   (101)
  Variabel yang tetap: B=0 (B')
  Jadi grup ini = B'

Hasil: F = A + B'

Verifikasi:
- m0(000): A=0, B'=1 -> A+B' = 1 ✓
- m1(001): A=0, B'=1 -> 1 ✓
- m4(100): A=1 -> 1 ✓
- m5(101): A=1 -> 1 ✓
- m6(110): A=1 -> 1 ✓
- m7(111): A=1 -> 1 ✓
- m2(010): A=0, B'=0 -> 0 ✓
- m3(011): A=0, B'=0 -> 0 ✓
```

**Jawaban: F = A + B'**

---

### Soal 15 — Penyederhanaan Ekspresi dengan 4 Variabel ★★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan secara aljabar:

```
A'·B'·C·D + A'·B·C·D + A·B'·C·D + A·B·C·D
```

**Pembahasan:**

```
= A'·B'·C·D + A'·B·C·D + A·B'·C·D + A·B·C·D

Faktorkan C·D:
= C·D·(A'·B' + A'·B + A·B' + A·B)

Sederhanakan isi kurung:
A'·B' + A'·B + A·B' + A·B
= A'·(B' + B) + A·(B' + B)       [Distributif]
= A'·1 + A·1                     [Komplemen]
= A' + A                         [Identitas]
= 1                              [Komplemen]

Jadi: C·D·1 = C·D
```

**Jawaban: C·D**

---

### Soal 16 — Identifikasi Hukum Boolean ★

**Tipe:** Pilihan Ganda

**Soal:**  
Penyederhanaan `A + A·B = A` menggunakan hukum apa?

(A) Hukum Distributif  
(B) Hukum Absorpsi  
(C) Hukum De Morgan  
(D) Hukum Idempoten  

**Pembahasan:**

```
A + A·B = A

Ini adalah bentuk hukum Absorpsi: X + X·Y = X
Di mana X = A dan Y = B.

Penjelasan: Jika A sudah TRUE, maka A + (apapun) pasti TRUE = A.
Jika A = FALSE, maka A·B juga FALSE, jadi A + A·B = FALSE = A.

Pembuktian:
A + A·B = A·(1 + B) = A·1 = A [Distributif + Null + Identitas]
Tapi secara langsung dikenal sebagai Hukum Absorpsi.
```

**Jawaban: (B) Hukum Absorpsi**

---

## Bagian C: Logika Proposisional dan Penalaran (Inference)

---

### Soal 17 — Modus Ponens ★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan premis-premis:
1. Jika hari cerah, maka Siti pergi bersepeda.
2. Hari ini cerah.

Apa kesimpulan yang valid?

**Pembahasan:**

```
Definisikan variabel:
  p: Hari cerah
  q: Siti pergi bersepeda

Premis 1: p → q
Premis 2: p

Menggunakan Modus Ponens:
  p → q
  p
  -------
  Maka: q
```

**Jawaban:** Siti pergi bersepeda. (Modus Ponens)

---

### Soal 18 — Modus Tollens ★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan premis-premis:
1. Jika komputer terinfeksi virus, maka komputer menjadi lambat.
2. Komputer tidak lambat.

Apa kesimpulannya?

**Pembahasan:**

```
Definisikan variabel:
  p: Komputer terinfeksi virus
  q: Komputer menjadi lambat

Premis 1: p → q
Premis 2: ¬q

Menggunakan Modus Tollens:
  p → q
  ¬q
  -------
  Maka: ¬p (Komputer TIDAK terinfeksi virus)
```

**Jawaban:** Komputer tidak terinfeksi virus. (Modus Tollens)

---

### Soal 19 — Silogisme Hipotetis Berantai ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan premis-premis:
1. Jika Ali malas belajar, maka nilainya jelek.
2. Jika nilainya jelek, maka dia tidak naik kelas.
3. Jika dia tidak naik kelas, maka orangtuanya kecewa.
4. Orangtua Ali tidak kecewa.

Apa kesimpulan yang dapat ditarik tentang Ali?

**Pembahasan:**

```
Variabel:
  p: Ali malas belajar
  q: Nilainya jelek
  r: Dia tidak naik kelas
  s: Orangtuanya kecewa

Premis 1: p → q
Premis 2: q → r
Premis 3: r → s
Premis 4: ¬s

Langkah 1: Silogisme Hipotetis pada premis 1, 2, 3:
  p → q, q → r  =>  p → r
  p → r, r → s  =>  p → s

Langkah 2: Modus Tollens pada p → s dan ¬s:
  p → s
  ¬s
  -------
  ¬p

Bonus (dari premis 3 dan 4):
  r → s, ¬s => ¬r (Ali naik kelas)
  q → r, ¬r => ¬q (Nilainya tidak jelek)
```

**Jawaban:** Ali TIDAK malas belajar. (Juga: nilainya tidak jelek, dan dia naik kelas.)

---

### Soal 20 — Identifikasi Fallacy ★★

**Tipe:** Pilihan Ganda

**Soal:**  
Perhatikan penalaran berikut:

"Jika seseorang adalah dokter, maka dia lulusan universitas. Budi lulusan universitas. Jadi Budi adalah dokter."

Penalaran ini merupakan:

(A) Modus Ponens (Valid)  
(B) Modus Tollens (Valid)  
(C) Affirming the Consequent (Tidak Valid)  
(D) Silogisme Hipotetis (Valid)  

**Pembahasan:**

```
p: seseorang adalah dokter
q: dia lulusan universitas

Premis 1: p → q (Jika dokter maka lulusan universitas)
Premis 2: q (Budi lulusan universitas)
Kesimpulan: p (Budi dokter)

Bentuk: p → q, q, maka p?

Ini adalah "Affirming the Consequent" -- FALLACY (tidak valid)!
Budi bisa saja lulusan universitas tanpa menjadi dokter 
(misalnya dia insinyur, guru, dll).
```

**Jawaban: (C) Affirming the Consequent (Tidak Valid)**

---

### Soal 21 — Penalaran dengan Disjungsi ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan premis-premis:
1. Hari ini Minggu atau hari libur nasional.
2. Hari ini bukan Minggu.
3. Jika hari libur nasional, maka kantor tutup.

Apa kesimpulannya?

**Pembahasan:**

```
Variabel:
  p: Hari ini Minggu
  q: Hari ini libur nasional
  r: Kantor tutup

Premis 1: p ∨ q
Premis 2: ¬p
Premis 3: q → r

Langkah 1: Silogisme Disjungtif pada premis 1 dan 2:
  p ∨ q
  ¬p
  -------
  q (Hari ini libur nasional)

Langkah 2: Modus Ponens pada premis 3 dan kesimpulan langkah 1:
  q → r
  q
  -------
  r (Kantor tutup)
```

**Jawaban:** Hari ini libur nasional DAN kantor tutup.

---

### Soal 22 — Konversi Kalimat ke Logika ★★

**Tipe:** Uraian

**Soal:**  
Nyatakan kalimat berikut dalam notasi logika, kemudian tentukan negasinya:

"Jika Rina belajar keras dan tidak begadang, maka dia akan lulus ujian."

**Pembahasan:**

```
Definisikan variabel:
  p: Rina belajar keras
  q: Rina begadang
  r: Rina lulus ujian

Kalimat asli dalam logika:
  (p ∧ ¬q) → r

Negasi:
  ¬((p ∧ ¬q) → r)
  = (p ∧ ¬q) ∧ ¬r          [Karena ¬(A → B) = A ∧ ¬B]

Dalam bahasa Indonesia:
  "Rina belajar keras DAN tidak begadang, TETAPI dia TIDAK lulus ujian."
```

**Jawaban:**  
- Logika: (p ∧ ¬q) → r  
- Negasi: (p ∧ ¬q) ∧ ¬r  
- Dalam bahasa: "Rina belajar keras dan tidak begadang, tetapi tidak lulus ujian."

---

### Soal 23 — Tautologi atau Bukan? ★★

**Tipe:** Benar/Salah

**Soal:**  
Tentukan apakah ekspresi-ekspresi berikut merupakan tautologi (selalu TRUE):

(a) `p ∨ ¬p`  
(b) `(p ∧ q) → p`  
(c) `p → (p ∨ q)`  
(d) `(p → q) → (q → p)`  

**Pembahasan:**

```
(a) p ∨ ¬p
    Ini adalah Hukum Excluded Middle. SELALU TRUE.
    -> TAUTOLOGI ✓

(b) (p ∧ q) → p
    Jika p ∧ q = T, maka p pasti T. Jadi T → T = T.
    Jika p ∧ q = F, maka F → apapun = T.
    Selalu TRUE -> TAUTOLOGI ✓

(c) p → (p ∨ q)
    Jika p = T, maka p ∨ q pasti T. T → T = T.
    Jika p = F, maka F → apapun = T.
    Selalu TRUE -> TAUTOLOGI ✓

(d) (p → q) → (q → p)
    Cek p=F, q=T:
    p → q = F → T = T
    q → p = T → F = F
    T → F = FALSE!
    
    Tidak selalu TRUE -> BUKAN TAUTOLOGI ✗
```

**Jawaban: (a) Ya, (b) Ya, (c) Ya, (d) Bukan tautologi**

---

### Soal 24 — Penalaran Resolusi ★★★

**Tipe:** Uraian

**Soal:**  
Gunakan metode resolusi untuk membuktikan bahwa dari premis-premis berikut dapat disimpulkan "r":

1. p ∨ q  
2. ¬p ∨ r  
3. ¬q ∨ r  

**Pembahasan:**

```
Metode Resolusi: Dari (A ∨ B) dan (¬A ∨ C), kita bisa simpulkan (B ∨ C).

Langkah 1: Resolusi premis 1 dan premis 2
  Premis 1: p ∨ q
  Premis 2: ¬p ∨ r
  Literal yang dieliminasi: p dan ¬p
  Hasil: q ∨ r  ... (4)

Langkah 2: Resolusi hasil (4) dan premis 3
  (4): q ∨ r
  Premis 3: ¬q ∨ r
  Literal yang dieliminasi: q dan ¬q
  Hasil: r ∨ r = r  ... (5)

Kesimpulan: r terbukti.

Alternatif:
Langkah 1: Resolusi premis 1 dan premis 3
  p ∨ q dan ¬q ∨ r -> p ∨ r ... (4')
  
Langkah 2: Resolusi (4') dan premis 2
  p ∨ r dan ¬p ∨ r -> r ∨ r = r
  
Sama-sama menghasilkan r. ✓
```

**Jawaban:** Dengan dua langkah resolusi, terbukti bahwa r dapat disimpulkan.

---

## Bagian D: Hukum De Morgan dan Penerapan Hukum-Hukum Boolean

---

### Soal 25 — De Morgan Dasar ★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan menggunakan De Morgan: `NOT(A AND B AND C)`

**Pembahasan:**

```
Hukum De Morgan untuk n variabel:
NOT(A₁ AND A₂ AND ... AND Aₙ) = NOT(A₁) OR NOT(A₂) OR ... OR NOT(Aₙ)

Maka:
NOT(A AND B AND C) = NOT(A) OR NOT(B) OR NOT(C)
                   = A' + B' + C'
```

**Jawaban: A' + B' + C'**

---

### Soal 26 — De Morgan Bertingkat ★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan: `NOT( (A OR B) AND (C OR D) )`

**Pembahasan:**

```
Langkah 1: Terapkan De Morgan pada AND terluar
  NOT( X AND Y ) = NOT(X) OR NOT(Y)
  
  dimana X = (A OR B), Y = (C OR D)
  
  = NOT(A OR B) OR NOT(C OR D)

Langkah 2: Terapkan De Morgan pada masing-masing NOT
  NOT(A OR B) = A' AND B' = A'B'
  NOT(C OR D) = C' AND D' = C'D'

Langkah 3: Gabungkan
  = A'B' + C'D'
```

**Jawaban: A'B' + C'D'**

---

### Soal 27 — De Morgan pada Implikasi ★★

**Tipe:** Uraian

**Soal:**  
Tentukan negasi dari: `(p → q) ∧ (r → s)`

Nyatakan hasilnya dalam bentuk yang paling sederhana.

**Pembahasan:**

```
Langkah 1: Terapkan De Morgan pada konjungsi
  ¬((p → q) ∧ (r → s))
  = ¬(p → q) ∨ ¬(r → s)          [De Morgan]

Langkah 2: Negasi masing-masing implikasi
  ¬(p → q) = p ∧ ¬q              [Karena ¬(A → B) = A ∧ ¬B]
  ¬(r → s) = r ∧ ¬s

Langkah 3: Gabungkan
  = (p ∧ ¬q) ∨ (r ∧ ¬s)
```

**Jawaban:** (p ∧ ¬q) ∨ (r ∧ ¬s)

Dalam bahasa: "p benar tapi q salah, ATAU r benar tapi s salah."

---

### Soal 28 — De Morgan pada Kuantor ★★★

**Tipe:** Uraian

**Soal:**  
Negasikan pernyataan berikut dan sederhanakan:

"Untuk setiap bilangan bulat n, jika n habis dibagi 4 maka n habis dibagi 2."

**Pembahasan:**

```
Formalisasi:
  ∀n ∈ Z, (habis4(n) → habis2(n))

Negasi:
  ¬(∀n ∈ Z, (habis4(n) → habis2(n)))
  = ∃n ∈ Z, ¬(habis4(n) → habis2(n))         [Negasi kuantor universal]
  = ∃n ∈ Z, (habis4(n) ∧ ¬habis2(n))          [Negasi implikasi]

Dalam bahasa Indonesia:
  "Ada bilangan bulat n yang habis dibagi 4 tetapi TIDAK habis dibagi 2."

Catatan: Pernyataan asli TRUE (setiap kelipatan 4 pasti kelipatan 2).
Negasinya FALSE (tidak ada bilangan yang habis dibagi 4 tapi tidak habis dibagi 2).
```

**Jawaban:** ∃n ∈ Z, (habis4(n) ∧ ¬habis2(n))  
"Ada bilangan bulat n yang habis dibagi 4 tetapi tidak habis dibagi 2."

---

### Soal 29 — Penerapan Hukum Distributif dan De Morgan ★★★

**Tipe:** Isian Singkat

**Soal:**  
Sederhanakan ekspresi berikut sampai bentuk paling sederhana:

```
NOT( NOT(A) · B + A · NOT(B) )
```

**Pembahasan:**

```
Langkah 0: Kenali pola
  A'·B + A·B' = A ⊕ B (XOR)

Jadi ekspresi = NOT(A XOR B) = A XNOR B

Tapi mari kita sederhanakan secara aljabar:

Langkah 1: Misalkan F = A'·B + A·B'
  NOT(F) = NOT(A'·B + A·B')

Langkah 2: Terapkan De Morgan pada OR
  = NOT(A'·B) · NOT(A·B')
  = (A + B') · (A' + B)            [De Morgan pada masing-masing AND]

Langkah 3: Ekspansi
  = A·A' + A·B + B'·A' + B'·B
  = 0 + A·B + A'·B' + 0           [Komplemen]
  = A·B + A'·B'

Ini adalah bentuk XNOR: A·B + A'·B' (bernilai 1 jika A dan B sama).
```

**Jawaban: A·B + A'·B'** (atau equivalen: A XNOR B)

---

### Soal 30 — De Morgan dalam Konteks C++ ★★

**Tipe:** Isian Singkat

**Soal:**  
Ekspresi C++ berikut:

```cpp
if ( !(x > 5 && y <= 10) )
```

Setara dengan ekspresi `if(...)` yang mana (tanpa tanda `!`)?

(A) `if (x > 5 || y <= 10)`  
(B) `if (x <= 5 || y > 10)`  
(C) `if (x <= 5 && y > 10)`  
(D) `if (x < 5 || y >= 10)`  

**Pembahasan:**

```
Terapkan De Morgan pada !(A && B) = !A || !B

!(x > 5 && y <= 10)
= !(x > 5) || !(y <= 10)      [De Morgan]
= (x <= 5) || (y > 10)        [Negasi perbandingan]

Catatan negasi operator perbandingan:
  !(>) menjadi <=
  !(<=) menjadi >
  !(>=) menjadi <
  !(<) menjadi >=
  !(==) menjadi !=
```

**Jawaban: (B) `if (x <= 5 || y > 10)`**

---

### Soal 31 — Pembuktian Ekuivalensi dengan De Morgan ★★★

**Tipe:** Uraian

**Soal:**  
Buktikan secara aljabar bahwa:

```
NOT(A → B) ekuivalen dengan A AND NOT(B)
```

**Pembahasan:**

```
Langkah 1: Ubah implikasi ke bentuk OR
  A → B = ¬A ∨ B             [Eliminasi implikasi]

Langkah 2: Negasi
  NOT(A → B) = NOT(¬A ∨ B)

Langkah 3: Terapkan De Morgan pada OR
  = NOT(¬A) AND NOT(B)
  = A AND NOT(B)              [Involusi: NOT(NOT(A)) = A]

Terbukti: NOT(A → B) = A ∧ ¬B  ✓

Verifikasi dengan tabel kebenaran:
| A | B | A→B | ¬(A→B) | A∧¬B |
|---|---|-----|--------|------|
| 0 | 0 |  1  |   0    |  0   |
| 0 | 1 |  1  |   0    |  0   |
| 1 | 0 |  0  |   1    |  1   |
| 1 | 1 |  1  |   0    |  0   |

Kolom ¬(A→B) dan A∧¬B identik. Terbukti. ✓
```

**Jawaban:** Terbukti melalui eliminasi implikasi dan De Morgan.

---

## Bagian E: Soal Campuran Gaya OSN

---

### Soal 32 — Berapa Fungsi Boolean yang Memenuhi Syarat ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa banyak fungsi Boolean `f(A, B, C)` (3 variabel) yang memenuhi KEDUA syarat berikut:
1. f(0, 0, 0) = 0
2. f(1, 1, 1) = 1

**Pembahasan:**

```
Fungsi Boolean 3 variabel ditentukan oleh nilainya pada 2^3 = 8 input.
Total fungsi Boolean 3 variabel = 2^8 = 256.

Syarat:
- f(0,0,0) = 0 -> 1 input sudah ditentukan
- f(1,1,1) = 1 -> 1 input sudah ditentukan

Sisa 6 input yang bebas, masing-masing bisa bernilai 0 atau 1.
Banyak fungsi = 2^6 = 64.
```

**Jawaban: 64**

---

### Soal 33 — Soal Logika Cerita (Word Problem) ★★★

**Tipe:** Isian Singkat

**Soal:**  
Di suatu pulau, penduduknya terdiri dari 2 jenis: Ksatria (selalu jujur) dan Penipu (selalu bohong). Anda bertemu 3 orang: A, B, dan C.

- A berkata: "B adalah Ksatria."
- B berkata: "A dan C berjenis berbeda (satu Ksatria, satu Penipu)."
- C berkata: "A adalah Penipu."

Tentukan jenis A, B, dan C masing-masing!

**Pembahasan:**

```
Kasus 1: A adalah Ksatria
  Perkataan A benar -> B adalah Ksatria
  Perkataan B benar -> A dan C berjenis berbeda
    A = Ksatria, maka C = Penipu
  Cek perkataan C: C bilang "A adalah Penipu" 
    C adalah Penipu, jadi C bohong -> A bukan Penipu -> A adalah Ksatria ✓
  
  KONSISTEN: A=Ksatria, B=Ksatria, C=Penipu ✓

Kasus 2: A adalah Penipu
  Perkataan A bohong -> B bukan Ksatria -> B adalah Penipu
  Perkataan B bohong -> A dan C berjenis SAMA (bukan berbeda)
    A = Penipu, maka C = Penipu
  Cek perkataan C: C bilang "A adalah Penipu"
    C adalah Penipu, jadi C bohong -> A bukan Penipu -> A adalah Ksatria
    KONTRADIKSI! (A tidak bisa Penipu dan Ksatria sekaligus)

  TIDAK KONSISTEN ✗

Satu-satunya solusi yang konsisten: Kasus 1.
```

**Jawaban:** A = Ksatria, B = Ksatria, C = Penipu

---

### Soal 34 — Minimalisasi Gerbang NAND ★★★

**Tipe:** Isian Singkat

**Soal:**  
Berapa jumlah minimum gerbang NAND (2-input) yang diperlukan untuk mengimplementasikan fungsi `F = A + B` (OR)?

**Pembahasan:**

```
Kita tahu bahwa OR dapat dibangun dari NAND:
  A OR B = (A NAND A) NAND (B NAND B)

Penjelasan:
- G1 = A NAND A = NOT(A AND A) = NOT(A) = A'
- G2 = B NAND B = NOT(B AND B) = NOT(B) = B'
- G3 = G1 NAND G2 = NOT(A' AND B') = A OR B  [De Morgan!]

Verifikasi:
  NOT(NOT(A) AND NOT(B)) = NOT(NOT(A OR B)) = A OR B ✓
  [De Morgan: NOT(A) AND NOT(B) = NOT(A OR B)]

Jadi diperlukan 3 gerbang NAND.

Bisa lebih sedikit? Dengan 1 gerbang NAND saja tidak bisa (hasilnya NAND).
Dengan 2 gerbang NAND:
- G1 = A NAND B = NOT(A AND B) -- bukan OR
- G1 = A NAND A, G2 = G1 NAND B = NOT(A' AND B) = A OR B'? Bukan OR.
- Tidak ada konfigurasi 2 gerbang yang menghasilkan OR.

Minimum = 3 gerbang NAND.
```

**Jawaban: 3 gerbang NAND**

---

### Soal 35 — Soal OSN Campuran: Tabel Kebenaran dan Penyederhanaan ★★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan ekspresi:

```
F(p, q, r) = (p → q) ∧ (q → r) ∧ (r → p)
```

(a) Berapa banyak kombinasi (p, q, r) yang membuat F bernilai TRUE?  
(b) Sederhanakan F ke bentuk Boolean paling sederhana.

**Pembahasan:**

```
Pertama, buat tabel kebenaran:

| p | q | r | p→q | q→r | r→p | F = (p→q)∧(q→r)∧(r→p) |
|---|---|---|-----|-----|-----|------------------------|
| T | T | T |  T  |  T  |  T  |          T             |
| T | T | F |  T  |  F  |  T  |          F             |
| T | F | T |  F  |  T  |  T  |          F             |
| T | F | F |  F  |  T  |  T  |          F             |
| F | T | T |  T  |  T  |  F  |          F             |
| F | T | F |  T  |  F  |  T  |          F             |
| F | F | T |  T  |  T  |  F  |          F             |
| F | F | F |  T  |  T  |  T  |          T             |

(a) F bernilai TRUE pada 2 kombinasi:
    - (T, T, T): semua TRUE
    - (F, F, F): semua FALSE

(b) Penyederhanaan:
    F = 1 ketika semua variabel sama.
    Dalam Boolean: F = p·q·r + p'·q'·r' 
    
    Ini adalah: (p XNOR q) AND (q XNOR r)
    Atau equivalen: "p, q, r semuanya sama"
    
    Bentuk SOP minimal: F = p·q·r + p'·q'·r'
```

**Jawaban:**  
(a) 2 kombinasi  
(b) F = p·q·r + p'·q'·r'

---

## Soal Bonus: Tantangan Ekstra

---

### Soal Bonus 1 — Short-Circuit Evaluation ★★

**Tipe:** Isian Singkat

**Soal:**  
Perhatikan kode C++ berikut:

```cpp
int a = 0, b = 5;
if (a != 0 && b/a > 2) {
    cout << "YA";
} else {
    cout << "TIDAK";
}
```

Apa outputnya? Apakah terjadi error division by zero?

**Pembahasan:**

```
Langkah 1: Evaluasi a != 0
  a = 0, jadi a != 0 = false

Langkah 2: Short-circuit evaluation pada &&
  Karena sisi kiri (a != 0) sudah FALSE,
  sisi kanan (b/a > 2) TIDAK DIEVALUASI sama sekali.
  
  Ini adalah fitur short-circuit evaluation di C++:
  - Pada &&: jika kiri FALSE, kanan diabaikan
  - Pada ||: jika kiri TRUE, kanan diabaikan

Langkah 3: Hasil keseluruhan if condition = FALSE
  Masuk ke blok else.

TIDAK terjadi division by zero karena b/a tidak dievaluasi.
```

**Jawaban:** Output: "TIDAK". Tidak terjadi error division by zero.

---

### Soal Bonus 2 — Jumlah Tautologi ★★★

**Tipe:** Isian Singkat

**Soal:**  
Dari 16 fungsi Boolean 2-variabel f(p, q), berapa banyak yang merupakan tautologi (selalu bernilai TRUE)?

**Pembahasan:**

```
Fungsi Boolean 2-variabel ditentukan oleh nilainya pada 4 input:
(0,0), (0,1), (1,0), (1,1)

Sebuah fungsi adalah tautologi jika dan hanya jika bernilai TRUE 
untuk SEMUA input.

Artinya: f(0,0) = 1, f(0,1) = 1, f(1,0) = 1, f(1,1) = 1

Hanya ada SATU fungsi yang memenuhi: fungsi yang selalu bernilai 1.
(Yaitu fungsi konstanta TRUE)
```

**Jawaban: 1** (hanya fungsi konstanta TRUE)

---

### Soal Bonus 3 — Ekspresi Boolean dari Soal Cerita ★★★

**Tipe:** Uraian

**Soal:**  
Sebuah sistem alarm kebakaran akan berbunyi (output = 1) jika dan hanya jika:
- Sensor asap (A) aktif DAN sensor panas (B) aktif, ATAU
- Tombol darurat (C) ditekan.

Tetapi alarm TIDAK akan berbunyi jika saklar pemeliharaan (M) aktif (override).

(a) Tuliskan fungsi Boolean F(A, B, C, M) untuk sistem ini.  
(b) Berapa jumlah minterm pada fungsi ini?  
(c) Jika M disederhanakan (M selalu 0), apa bentuk sederhana dari F?

**Pembahasan:**

```
(a) Fungsi Boolean:
    Kondisi alarm berbunyi: (A·B + C) tetapi TIDAK jika M aktif
    F = (A·B + C) · M'
    
    Atau dalam bentuk lengkap:
    F = A·B·M' + C·M'

(b) Untuk menghitung minterm, ekspansi ke bentuk kanonik:
    F(A,B,C,M) = A·B·M' + C·M'
    
    Ekspansi A·B·M':
    = A·B·C·M' + A·B·C'·M'    (C bisa 0 atau 1)
    = minterm 14 (1110) + minterm 12 (1100)
    Tunggu, urutannya ABCM:
    A·B·C·M' = 1·1·1·0 = minterm (1110)₂ = m14
    A·B·C'·M' = 1·1·0·0 = minterm (1100)₂ = m12
    
    Ekspansi C·M':
    = A'·B'·C·M' + A'·B·C·M' + A·B'·C·M' + A·B·C·M'
    = m2 (0010) + m6 (0110) + m10 (1010) + m14 (1110)
    
    Gabungan (hilangkan duplikat m14):
    F = Sigma m(2, 6, 10, 12, 14)
    
    Jumlah minterm = 5.

(c) Jika M = 0 (M' = 1):
    F = A·B·1 + C·1 = A·B + C
    
    Bentuk sederhana: F = A·B + C
```

**Jawaban:**  
(a) F = (A·B + C)·M' = A·B·M' + C·M'  
(b) 5 minterm  
(c) F = A·B + C

---

### Soal Bonus 4 — Menentukan Operator dari Tabel Kebenaran ★★

**Tipe:** Isian Singkat

**Soal:**  
Suatu operator biner ⊗ memiliki tabel kebenaran berikut:

| p | q | p ⊗ q |
|---|---|-------|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

Operator ⊗ ini setara dengan operator logika apa?

**Pembahasan:**

```
Perhatikan tabel:
- p ⊗ q = T jika p dan q BERBEDA
- p ⊗ q = F jika p dan q SAMA

Cek:
- T ⊗ T = F (sama -> FALSE) ✓
- T ⊗ F = T (berbeda -> TRUE) ✓
- F ⊗ T = T (berbeda -> TRUE) ✓
- F ⊗ F = F (sama -> FALSE) ✓

Ini persis definisi XOR (Exclusive OR)!
```

**Jawaban:** XOR (⊕)

---

### Soal Bonus 5 — Predikat dan Kuantor Bersarang ★★★

**Tipe:** Uraian

**Soal:**  
Tentukan nilai kebenaran dari pernyataan berikut, dengan domain bilangan bulat positif:

(a) ∀x ∃y (x + y = 10)  
(b) ∃y ∀x (x + y = 10)  
(c) ∀x ∀y (x + y = y + x)  
(d) ∃x ∃y (x · y = x + y)  

**Pembahasan:**

```
Domain: bilangan bulat positif {1, 2, 3, ...}

(a) ∀x ∃y (x + y = 10)
    "Untuk setiap x, ada y sehingga x + y = 10"
    Artinya: y = 10 - x
    
    Cek: Apakah untuk setiap x positif, ada y POSITIF dengan x + y = 10?
    - Jika x = 1, y = 9 (positif) ✓
    - Jika x = 9, y = 1 (positif) ✓
    - Jika x = 10, y = 0 (BUKAN positif) ✗
    - Jika x = 11, y = -1 (BUKAN positif) ✗
    
    Jawaban: FALSE (gagal untuk x >= 10)

(b) ∃y ∀x (x + y = 10)
    "Ada satu y sehingga untuk SEMUA x berlaku x + y = 10"
    Ini berarti satu nilai y harus bekerja untuk semua x.
    Jelas tidak mungkin (misal y=5, maka x harus selalu = 5).
    
    Jawaban: FALSE

(c) ∀x ∀y (x + y = y + x)
    "Untuk semua x dan y, x + y = y + x"
    Ini adalah hukum komutatif penjumlahan. Berlaku untuk semua bilangan.
    
    Jawaban: TRUE

(d) ∃x ∃y (x · y = x + y)
    "Ada x dan y sehingga xy = x + y"
    Cari solusi: xy = x + y -> xy - x - y = 0 -> (x-1)(y-1) = 1
    Karena domain positif: x-1 = 1, y-1 = 1 -> x = 2, y = 2
    Cek: 2·2 = 4, 2+2 = 4 ✓
    
    Jawaban: TRUE
```

**Jawaban:**  
(a) FALSE  
(b) FALSE  
(c) TRUE  
(d) TRUE (x = 2, y = 2)

---

## Ringkasan Statistik Soal

| Bagian | Jumlah Soal | Topik |
|--------|-------------|-------|
| A: Tabel Kebenaran | 8 soal | Evaluasi ekspresi, tabel kebenaran, implikasi, C++ boolean |
| B: Penyederhanaan | 8 soal | Aljabar Boolean, K-Map, hukum-hukum Boolean |
| C: Logika & Penalaran | 8 soal | Modus Ponens/Tollens, silogisme, fallacy, tautologi, resolusi |
| D: De Morgan | 7 soal | De Morgan dasar/bertingkat, negasi, aplikasi C++ |
| E: Campuran OSN | 4 soal | Fungsi Boolean, cerita logika, gerbang NAND, campuran |
| Bonus | 5 soal | Short-circuit, counting, desain sistem, operator, kuantor |
| **Total** | **40 soal** | |

### Distribusi Tingkat Kesulitan

| Tingkat | Jumlah |
|---------|--------|
| ★ Mudah | 9 soal |
| ★★ Sedang | 16 soal |
| ★★★ Sulit | 15 soal |

### Distribusi Tipe Soal

| Tipe | Jumlah |
|------|--------|
| Isian Singkat (IS) | 22 soal |
| Uraian (U) | 10 soal |
| Benar/Salah (B/S) | 3 soal |
| Pilihan Ganda (PG) | 5 soal |

---

*Latihan ini melengkapi materi [01-aljabar-boolean-dan-logika.md](../materi/01-aljabar-boolean-dan-logika.md). Kerjakan secara bertahap mulai dari soal mudah.*
