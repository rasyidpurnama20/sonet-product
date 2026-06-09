# Materi 01 — Aljabar Boolean & Logika

## 1. Pendahuluan

Aljabar Boolean dan logika proposisional merupakan fondasi penting dalam informatika.
Dalam OSN Informatika, topik ini muncul dalam bentuk:
- Penyederhanaan ekspresi logika
- Evaluasi tabel kebenaran
- Penalaran deduktif dan induktif
- Tracing kode yang menggunakan operator logika

Materi ini akan membahas secara komprehensif mulai dari operasi dasar hingga teknik-teknik
lanjutan yang sering muncul di soal OSN.

---

## 2. Operasi Dasar Boolean

Boolean hanya memiliki dua nilai: **TRUE (1)** dan **FALSE (0)**.

### 2.1 Tabel Operator Lengkap

| Operasi | Simbol | Deskripsi |
|---------|--------|-----------|
| AND | `∧` / `&` / `·` | Bernilai 1 hanya jika **kedua** operand 1 |
| OR | `∨` / `\|` / `+` | Bernilai 1 jika **salah satu atau kedua** operand 1 |
| NOT | `¬` / `!` / `~` | Membalik nilai: 0 menjadi 1, 1 menjadi 0 |
| XOR | `⊕` / `^` | Bernilai 1 jika operand **berbeda** |
| NAND | `↑` | Kebalikan AND: bernilai 0 hanya jika kedua operand 1 |
| NOR | `↓` | Kebalikan OR: bernilai 1 hanya jika kedua operand 0 |
| XNOR | `⊙` | Kebalikan XOR: bernilai 1 jika operand **sama** |
| IMPLIKASI | `→` | Bernilai 0 hanya jika operand pertama 1 dan operand kedua 0 |

### 2.2 Tabel Kebenaran Lengkap (Semua Operator)

| A | B | AND | OR | NOT A | XOR | NAND | NOR | XNOR | A→B |
|---|---|-----|----|----|-----|------|-----|------|-----|
| 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |

### 2.3 Penjelasan Intuitif Setiap Operator

**AND (Konjungsi):** Bayangkan dua saklar seri -- keduanya harus ON agar lampu menyala.

**OR (Disjungsi):** Bayangkan dua saklar paralel -- salah satu ON saja lampu sudah menyala.

**NOT (Negasi):** Saklar pembalik. Kalau ON jadi OFF, kalau OFF jadi ON.

**XOR (Exclusive OR):** "Atau eksklusif" -- tepat satu yang bernilai TRUE. Bayangkan skenario:
"Kamu boleh pilih es krim ATAU cake" (tidak keduanya).

**NAND:** "NOT AND" -- kebalikan dari AND. Hasilnya 1 kecuali jika keduanya 1.
NAND disebut **gerbang universal** karena semua gerbang logika lain dapat dibangun dari NAND saja.

**NOR:** "NOT OR" -- kebalikan dari OR. Hasilnya 1 hanya jika keduanya 0.
NOR juga merupakan **gerbang universal**.

**XNOR:** "NOT XOR" -- bernilai 1 jika kedua operand SAMA. Bisa dianggap sebagai
operator "kesamaan" (equivalence).

### 2.4 Hubungan Antar Operator

```
NAND(A, B) = NOT(A AND B)
NOR(A, B)  = NOT(A OR B)
XNOR(A, B) = NOT(A XOR B) = (A AND B) OR (NOT A AND NOT B)
XOR(A, B)  = (A OR B) AND NOT(A AND B)
           = (A AND NOT B) OR (NOT A AND B)
A → B      = NOT A OR B
A ↔ B      = (A → B) AND (B → A) = XNOR(A, B)
```

### 2.5 Membangun Semua Gerbang dari NAND

```
NOT A      = A NAND A
A AND B    = (A NAND B) NAND (A NAND B)
A OR B     = (A NAND A) NAND (B NAND B)
A XOR B    = [(A NAND (A NAND B)) NAND (B NAND (A NAND B))]
```

> **Tips OSN:** Soal tentang gerbang universal sering muncul. Ingat bahwa NAND dan NOR
> masing-masing bisa membentuk semua gerbang lain.

---

## 3. Hukum-Hukum Aljabar Boolean

### 3.1 Daftar Lengkap Hukum

| No | Hukum | Bentuk AND | Bentuk OR |
|----|-------|-----------|----------|
| 1 | Identitas | A · 1 = A | A + 0 = A |
| 2 | Null/Dominasi | A · 0 = 0 | A + 1 = 1 |
| 3 | Idempoten | A · A = A | A + A = A |
| 4 | Komplemen | A · A' = 0 | A + A' = 1 |
| 5 | Involusi | (A')' = A | (A')' = A |
| 6 | Komutatif | A · B = B · A | A + B = B + A |
| 7 | Asosiatif | (A·B)·C = A·(B·C) | (A+B)+C = A+(B+C) |
| 8 | Distributif | A·(B+C) = A·B + A·C | A+(B·C) = (A+B)·(A+C) |
| 9 | De Morgan | (A·B)' = A' + B' | (A+B)' = A' · B' |
| 10 | Absorpsi | A·(A+B) = A | A+(A·B) = A |
| 11 | Konsensus | A·B + A'·C + B·C = A·B + A'·C | (A+B)·(A'+C)·(B+C) = (A+B)·(A'+C) |

### 3.2 Penjelasan Hukum De Morgan (Sangat Penting!)

Hukum De Morgan adalah salah satu hukum paling sering diujikan di OSN.

**Aturan 1:** NOT(A AND B) = (NOT A) OR (NOT B)
- "Bukan (keduanya benar)" sama dengan "salah satu salah"

**Aturan 2:** NOT(A OR B) = (NOT A) AND (NOT B)
- "Bukan (salah satu benar)" sama dengan "keduanya salah"

**Generalisasi untuk n variabel:**
```
NOT(A₁ AND A₂ AND ... AND Aₙ) = (NOT A₁) OR (NOT A₂) OR ... OR (NOT Aₙ)
NOT(A₁ OR A₂ OR ... OR Aₙ) = (NOT A₁) AND (NOT A₂) AND ... AND (NOT Aₙ)
```

**Cara mengingat:** Saat mendistribusikan NOT ke dalam:
1. Balik semua operator (AND jadi OR, OR jadi AND)
2. Negasikan semua variabel

### 3.3 Hukum Absorpsi (Sering Menjebak!)

**A + A·B = A** (Absorpsi OR)
- Penjelasan: Jika A sudah TRUE, maka hasilnya pasti TRUE terlepas dari B.
- Jika A FALSE, maka A·B pasti FALSE juga, jadi hasil tetap FALSE = A.

**A · (A + B) = A** (Absorpsi AND)
- Penjelasan: Jika A FALSE, hasilnya pasti FALSE = A.
- Jika A TRUE, maka (A+B) pasti TRUE, jadi A·TRUE = A.

### 3.4 Hukum Konsensus (Level Lanjut)

**A·B + A'·C + B·C = A·B + A'·C**

Suku B·C disebut "suku konsensus" dan bersifat redundan karena:
- Jika A = 1: suku A·B sudah mencover B·C (saat B=1, C tidak relevan)
- Jika A = 0: suku A'·C sudah mencover B·C (saat C=1, B tidak relevan)

---

## 4. Teknik Penyederhanaan Ekspresi Boolean

### 4.1 Metode Aljabar (Step-by-Step)

**Langkah umum:**
1. Identifikasi hukum yang bisa diterapkan
2. Cari pola absorpsi, komplemen, atau distribusi
3. Sederhanakan bertahap
4. Verifikasi dengan tabel kebenaran jika ragu

### 4.2 Contoh Penyederhanaan Lengkap

**Contoh 1:** Sederhanakan `A·B + A·B'`
```
= A·B + A·B'
= A·(B + B')      [Distributif]
= A·1             [Komplemen: B + B' = 1]
= A               [Identitas]
```

**Contoh 2:** Sederhanakan `(A + B)·(A + B')`
```
= A·A + A·B' + B·A + B·B'    [Distributif / FOIL]
= A + A·B' + A·B + 0          [Idempoten: A·A=A, Komplemen: B·B'=0]
= A + A·(B' + B)              [Distributif]
= A + A·1                     [Komplemen]
= A + A                       [Identitas]
= A                           [Idempoten]
```

Atau cara lebih cepat:
```
= (A + B)·(A + B')
= A + B·B'                    [Distributif bentuk OR: x+(y·z) = (x+y)·(x+z), kebalikannya]
= A + 0
= A
```

**Contoh 3:** Sederhanakan `A'·B'·C + A'·B·C + A·B'·C + A·B·C`
```
= C·(A'·B' + A'·B + A·B' + A·B)     [Faktorkan C]
= C·(A'·(B'+B) + A·(B'+B))           [Distributif]
= C·(A'·1 + A·1)                     [Komplemen]
= C·(A' + A)                         [Identitas]
= C·1                                [Komplemen]
= C                                  [Identitas]
```

**Contoh 4:** Sederhanakan `(A+B)·(A'+C)·(B+C)`
```
= (A+B)·(A'+C)·(B+C)
Menggunakan hukum konsensus (bentuk OR):
(A+B)·(A'+C)·(B+C) = (A+B)·(A'+C)
karena (B+C) adalah suku konsensus yang redundan.
```

---

## 5. Karnaugh Map (K-Map)

### 5.1 Konsep Dasar

Karnaugh Map adalah metode visual untuk menyederhanakan ekspresi Boolean.
Prinsipnya: mengelompokkan sel-sel bertetangga yang bernilai 1 untuk membentuk
grup yang lebih sederhana.

**Aturan K-Map:**
1. Setiap sel merepresentasikan satu minterm
2. Sel yang bertetangga berbeda tepat 1 bit
3. Kelompokkan sel bernilai 1 dalam grup berukuran 2^n (1, 2, 4, 8, ...)
4. Grup boleh "wrap around" (sisi kiri berhubungan dengan kanan, atas dengan bawah)
5. Ambil grup sebesar mungkin, sesedikit mungkin

### 5.2 K-Map 2 Variabel

```
        B=0    B=1
A=0  |  m0  |  m1  |
A=1  |  m2  |  m3  |
```

Dimana:
- m0 = A'B' (00)
- m1 = A'B  (01)
- m2 = AB'  (10)
- m3 = AB   (11)

**Contoh:** F(A,B) = Σm(1,2,3) = A'B + AB' + AB

```
        B=0    B=1
A=0  |  0   |  1   |
A=1  |  1   |  1   |
```

Grup 1: Baris A=1 (m2, m3) -> A
Grup 2: Kolom B=1 (m1, m3) -> B

Hasil: **F = A + B**

### 5.3 K-Map 3 Variabel

```
          BC=00  BC=01  BC=11  BC=10
A=0     |  m0  |  m1  |  m3  |  m2  |
A=1     |  m4  |  m5  |  m7  |  m6  |
```

Perhatikan urutan BC menggunakan **Gray code** (00, 01, 11, 10) agar
sel bertetangga hanya berbeda 1 bit.

**Contoh:** F(A,B,C) = Σm(0,2,4,6)

```
          BC=00  BC=01  BC=11  BC=10
A=0     |  1   |  0   |  0   |  1   |
A=1     |  1   |  0   |  0   |  1   |
```

Grup: Kolom BC=00 dan BC=10 (ingat wrap-around!)
Variabel yang berubah: B dan A (berubah), C tetap 0

Hasil: **F = C'** (C bernilai 0 di semua sel yang bernilai 1)

### 5.4 Contoh K-Map 3 Variabel Lanjutan

**F(A,B,C) = Σm(1,3,5,7)**

```
          BC=00  BC=01  BC=11  BC=10
A=0     |  0   |  1   |  1   |  0   |
A=1     |  0   |  1   |  1   |  0   |
```

Semua sel di kolom BC=01 dan BC=11 bernilai 1.
Variabel yang tetap: C=1

Hasil: **F = C**

**F(A,B,C) = Σm(3,4,5,7)**

```
          BC=00  BC=01  BC=11  BC=10
A=0     |  0   |  0   |  1   |  0   |
A=1     |  1   |  1   |  1   |  0   |
```

Grup 1: m4, m5, m7, m6? Tidak, m6=0. Coba: m4, m5 -> AB'C' + AB'C = AB'... tidak.
Grup 1: m3, m7 (kolom BC=11) -> BC
Grup 2: m4, m5 (A=1, BC=00 dan BC=01) -> AC'... 

Hmm, mari lebih teliti:
- m4 = AB'C', m5 = AB'C -> grupkan: AB' (2 sel)
- m3 = A'BC, m7 = ABC -> grupkan: BC (2 sel)

Hasil: **F = AB' + BC**

---

## 6. Logika Proposisional

### 6.1 Proposisi

**Proposisi** adalah pernyataan deklaratif yang memiliki nilai kebenaran pasti (TRUE atau FALSE).

Contoh proposisi:
- "2 + 3 = 5" (TRUE)
- "Jakarta adalah ibu kota Thailand" (FALSE)
- "Semua bilangan prima ganjil" (FALSE, karena 2 prima tapi genap)

Bukan proposisi:
- "Berapa umurmu?" (pertanyaan)
- "Tutup pintunya!" (perintah)
- "x + 1 = 5" (kalimat terbuka, bergantung nilai x)

### 6.2 Operator Logika Proposisional

| Operator | Simbol | Nama | Bahasa Sehari-hari |
|----------|--------|------|-------------------|
| Negasi | ¬p | NOT | "Bukan p", "Tidak benar bahwa p" |
| Konjungsi | p ∧ q | AND | "p dan q" |
| Disjungsi | p ∨ q | OR | "p atau q" |
| Implikasi | p → q | IF-THEN | "Jika p maka q" |
| Biimplikasi | p ↔ q | IFF | "p jika dan hanya jika q" |

### 6.3 Tabel Kebenaran Implikasi (Paling Sering Menjebak!)

| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Mengapa F → T bernilai TRUE?**

Intuisi: "Jika saya lulus ujian, saya akan mentraktir kamu."
- Jika saya lulus (T) dan mentraktir (T): janji ditepati (TRUE)
- Jika saya lulus (T) dan tidak mentraktir (F): janji dilanggar (FALSE)
- Jika saya tidak lulus (F): janji tidak berlaku, jadi secara logika dianggap TRUE
  (karena saya tidak melanggar janji apapun -- ini disebut "vacuously true")

### 6.4 Variasi Implikasi

Diberikan implikasi: **p → q** ("Jika p maka q")

| Nama | Bentuk | Hubungan dengan p → q |
|------|--------|----------------------|
| Konvers | q → p | TIDAK selalu ekuivalen |
| Invers | ¬p → ¬q | TIDAK selalu ekuivalen |
| Kontraposisi | ¬q → ¬p | SELALU ekuivalen dengan p → q |

**Contoh:**
- Asli (p → q): "Jika hujan, maka jalanan basah"
- Konvers (q → p): "Jika jalanan basah, maka hujan" (belum tentu, bisa karena siram)
- Invers (¬p → ¬q): "Jika tidak hujan, maka jalanan tidak basah" (belum tentu)
- Kontraposisi (¬q → ¬p): "Jika jalanan tidak basah, maka tidak hujan" (PASTI benar)

> **Tips OSN:** Kontraposisi SELALU ekuivalen dengan pernyataan asli.
> Konvers dan Invers saling ekuivalen satu sama lain, tapi TIDAK ekuivalen dengan asli.

### 6.5 Biimplikasi

| p | q | p ↔ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

p ↔ q bernilai TRUE jika dan hanya jika p dan q memiliki nilai kebenaran yang SAMA.

Ekuivalensi: `p ↔ q = (p → q) ∧ (q → p)`

---

## 7. Tautologi, Kontradiksi, dan Kontingensi

- **Tautologi:** Proposisi yang SELALU bernilai TRUE untuk semua kombinasi nilai variabel.
  - Contoh: p ∨ ¬p (hukum excluded middle)
  - Contoh: (p → q) ↔ (¬q → ¬p) (kontraposisi)

- **Kontradiksi:** Proposisi yang SELALU bernilai FALSE.
  - Contoh: p ∧ ¬p

- **Kontingensi:** Proposisi yang bisa TRUE atau FALSE tergantung nilai variabel.
  - Contoh: p ∧ q

**Cara membuktikan tautologi:** Buat tabel kebenaran. Jika semua baris bernilai T, maka tautologi.

---

## 8. Ekuivalensi Logis

Dua proposisi P dan Q dikatakan **ekuivalen secara logis** (dilambangkan P ≡ Q)
jika mereka memiliki tabel kebenaran yang identik.

### 8.1 Ekuivalensi Penting

```
p → q  ≡  ¬p ∨ q                    [Eliminasi implikasi]
p ↔ q  ≡  (p → q) ∧ (q → p)        [Definisi biimplikasi]
p ↔ q  ≡  (p ∧ q) ∨ (¬p ∧ ¬q)     [XNOR]
¬(p → q)  ≡  p ∧ ¬q                 [Negasi implikasi]
¬(p ↔ q)  ≡  p ⊕ q                  [Negasi biimplikasi = XOR]
```

### 8.2 Pembuktian Ekuivalensi dengan Tabel Kebenaran

**Buktikan:** p → q ≡ ¬p ∨ q

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|--------|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

Kolom "p → q" dan "¬p ∨ q" identik. Terbukti ekuivalen. ✓

### 8.3 Pembuktian Ekuivalensi secara Aljabar

**Buktikan:** ¬(p ∨ q) ∨ (¬p ∧ q) ≡ ¬p

```
¬(p ∨ q) ∨ (¬p ∧ q)
= (¬p ∧ ¬q) ∨ (¬p ∧ q)       [De Morgan pada bagian pertama]
= ¬p ∧ (¬q ∨ q)               [Distributif]
= ¬p ∧ 1                      [Komplemen]
= ¬p                           [Identitas]
```
Terbukti. ✓

---

## 9. Kuantor (Quantifiers)

### 9.1 Kuantor Universal (∀)

Simbol: ∀ (dibaca "untuk semua" atau "untuk setiap")

**∀x P(x)** berarti: "Untuk setiap x, P(x) bernilai benar"

Contoh:
- ∀x ∈ ℝ, x² ≥ 0 (untuk semua bilangan real x, x kuadrat non-negatif) -- TRUE
- ∀x ∈ ℤ, x > 0 (semua bilangan bulat positif) -- FALSE (ada yang negatif)

### 9.2 Kuantor Eksistensial (∃)

Simbol: ∃ (dibaca "ada" atau "terdapat")

**∃x P(x)** berarti: "Terdapat setidaknya satu x sehingga P(x) benar"

Contoh:
- ∃x ∈ ℤ, x² = 4 (ada bilangan bulat yang kuadratnya 4) -- TRUE (x=2 atau x=-2)
- ∃x ∈ ℝ, x² < 0 (ada bilangan real yang kuadratnya negatif) -- FALSE

### 9.3 Negasi Kuantor

```
¬(∀x P(x))  ≡  ∃x ¬P(x)
¬(∃x P(x))  ≡  ∀x ¬P(x)
```

**Intuisi:**
- "Bukan benar bahwa semua siswa lulus" = "Ada siswa yang tidak lulus"
- "Bukan benar bahwa ada siswa yang curang" = "Semua siswa tidak curang"

### 9.4 Kuantor Bersarang

```
∀x ∃y (x + y = 0)
```
Dibaca: "Untuk setiap x, terdapat y sehingga x + y = 0"
Ini TRUE di bilangan real (y = -x).

```
∃y ∀x (x + y = 0)
```
Dibaca: "Terdapat y sehingga untuk semua x, x + y = 0"
Ini FALSE (tidak ada satu y yang berlaku untuk semua x).

> **Perhatian:** Urutan kuantor penting! ∀x∃y tidak sama dengan ∃y∀x.

---

## 10. Konversi Kalimat Bahasa Indonesia ke Logika

### 10.1 Panduan Konversi

| Kata/Frasa | Operator Logika |
|------------|----------------|
| "dan", "serta", "tetapi" | ∧ (AND) |
| "atau" | ∨ (OR) |
| "bukan", "tidak" | ¬ (NOT) |
| "jika ... maka ..." | → (IMPLIKASI) |
| "... jika dan hanya jika ..." | ↔ (BIIMPLIKASI) |
| "semua", "setiap", "seluruh" | ∀ (UNTUK SEMUA) |
| "ada", "terdapat", "beberapa" | ∃ (ADA) |

### 10.2 Contoh Konversi

1. "Jika Budi rajin belajar dan tidak main game, maka dia lulus ujian."
   - p: Budi rajin belajar
   - q: Budi main game
   - r: Budi lulus ujian
   - Logika: **(p ∧ ¬q) → r**

2. "Ani pergi ke sekolah atau ke perpustakaan, tetapi tidak keduanya."
   - p: Ani pergi ke sekolah
   - q: Ani pergi ke perpustakaan
   - Logika: **p ⊕ q** atau ekuivalen: **(p ∨ q) ∧ ¬(p ∧ q)**

3. "Setiap bilangan genap lebih besar dari 1 adalah bukan prima atau sama dengan 2."
   - Logika: **∀x ((genap(x) ∧ x > 1) → (¬prima(x) ∨ x = 2))**

4. "Tidak benar bahwa semua burung bisa terbang."
   - Logika: **¬(∀x (burung(x) → terbang(x)))** ≡ **∃x (burung(x) ∧ ¬terbang(x))**
   - Artinya: "Ada burung yang tidak bisa terbang"

---

## 11. Penalaran Deduktif

### 11.1 Modus Ponens

```
Premis 1: p → q     (Jika p maka q)
Premis 2: p          (p benar)
─────────────────
Kesimpulan: q        (q benar)
```

**Contoh:**
- Premis 1: Jika hujan, maka jalanan basah.
- Premis 2: Sekarang hujan.
- Kesimpulan: Jalanan basah. ✓

### 11.2 Modus Tollens

```
Premis 1: p → q     (Jika p maka q)
Premis 2: ¬q        (q salah)
─────────────────
Kesimpulan: ¬p      (p salah)
```

**Contoh:**
- Premis 1: Jika ada listrik, maka lampu menyala.
- Premis 2: Lampu tidak menyala.
- Kesimpulan: Tidak ada listrik. ✓

### 11.3 Silogisme Hipotetis

```
Premis 1: p → q
Premis 2: q → r
─────────────────
Kesimpulan: p → r
```

**Contoh:**
- Premis 1: Jika saya belajar, maka saya paham materi.
- Premis 2: Jika saya paham materi, maka saya lulus ujian.
- Kesimpulan: Jika saya belajar, maka saya lulus ujian. ✓

### 11.4 Silogisme Disjungtif

```
Premis 1: p ∨ q     (p atau q)
Premis 2: ¬p        (p salah)
─────────────────
Kesimpulan: q       (q benar)
```

### 11.5 Resolusi

```
Premis 1: p ∨ q
Premis 2: ¬p ∨ r
─────────────────
Kesimpulan: q ∨ r
```

### 11.6 Penambahan (Addition)

```
Premis: p
─────────────────
Kesimpulan: p ∨ q  (untuk sembarang q)
```

### 11.7 Penyederhanaan (Simplification)

```
Premis: p ∧ q
─────────────────
Kesimpulan: p     (dan juga q)
```

---

## 12. Kesalahan Penalaran (Fallacy)

### 12.1 Affirming the Consequent (Salah!)

```
p → q
q
─────── (SALAH!)
p
```

Contoh salah: "Jika hujan maka jalanan basah. Jalanan basah. Maka hujan."
(Jalanan bisa basah karena disirami!)

### 12.2 Denying the Antecedent (Salah!)

```
p → q
¬p
─────── (SALAH!)
¬q
```

Contoh salah: "Jika hujan maka jalanan basah. Tidak hujan. Maka jalanan tidak basah."
(Jalanan bisa basah karena sebab lain!)

> **Tips OSN:** Soal sering menguji apakah siswa bisa membedakan penalaran valid
> dari fallacy. Hafalkan modus ponens dan modus tollens sebagai penalaran VALID.

---

## 13. Contoh Soal Lengkap (Worked Examples)

### Contoh 1: Evaluasi Ekspresi Boolean

**Soal:** Tentukan nilai dari `(1 NAND 0) XOR (1 NOR 1)`.

**Solusi:**
```
Langkah 1: Hitung 1 NAND 0
  NAND = NOT(AND)
  1 AND 0 = 0
  NOT 0 = 1
  Jadi 1 NAND 0 = 1

Langkah 2: Hitung 1 NOR 1
  NOR = NOT(OR)
  1 OR 1 = 1
  NOT 1 = 0
  Jadi 1 NOR 1 = 0

Langkah 3: Hitung 1 XOR 0
  XOR bernilai 1 jika operand berbeda
  1 berbeda dengan 0
  Jadi 1 XOR 0 = 1

Jawaban: 1
```

### Contoh 2: Penyederhanaan Aljabar

**Soal:** Sederhanakan `A'B + AB + AB'`

**Solusi:**
```
= A'B + AB + AB'
= A'B + A(B + B')        [Distributif pada dua suku terakhir]
= A'B + A·1              [Komplemen: B + B' = 1]
= A'B + A                [Identitas]
= A + A'B                [Komutatif]
= A + B                  [Absorpsi lanjut: x + x'y = x + y]
```

Verifikasi dengan tabel kebenaran:
| A | B | A'B + AB + AB' | A + B |
|---|---|----------------|-------|
| 0 | 0 | 0+0+0 = 0 | 0 |
| 0 | 1 | 1+0+0 = 1 | 1 |
| 1 | 0 | 0+0+1 = 1 | 1 |
| 1 | 1 | 0+1+0 = 1 | 1 |

Terbukti sama. ✓

### Contoh 3: De Morgan Bertingkat

**Soal:** Sederhanakan `NOT(NOT(A AND B) OR C)`

**Solusi:**
```
= NOT(NOT(A AND B) OR C)
= NOT(NOT(A AND B)) AND NOT(C)      [De Morgan pada OR luar]
= (A AND B) AND NOT(C)               [Involusi: NOT NOT x = x]
= A · B · C'
```

### Contoh 4: Konversi ke Logika dan Evaluasi

**Soal:** Tentukan nilai kebenaran dari pernyataan berikut:
"Jika 2 + 2 = 5 maka bumi berbentuk datar."

**Solusi:**
```
p: 2 + 2 = 5 (FALSE)
q: Bumi berbentuk datar (FALSE)

p → q dengan p = F, q = F:
Dari tabel kebenaran implikasi, F → F = TRUE.

Jawaban: TRUE (vacuously true -- anteseden salah maka implikasi benar)
```

### Contoh 5: Penalaran Valid atau Tidak?

**Soal:** Apakah penalaran berikut valid?
- Premis 1: Semua programmer bisa matematika.
- Premis 2: Budi bisa matematika.
- Kesimpulan: Budi adalah programmer.

**Solusi:**
```
p(x): x adalah programmer
q(x): x bisa matematika

Premis 1: ∀x (p(x) → q(x))
Premis 2: q(Budi)
Kesimpulan: p(Budi)

Ini adalah bentuk "Affirming the Consequent" -- FALLACY!
Budi bisa saja bisa matematika tanpa menjadi programmer.

Jawaban: Penalaran TIDAK valid.
```

### Contoh 6: K-Map

**Soal:** Sederhanakan F(A,B,C) = Σm(0,1,2,3,7) menggunakan K-Map.

**Solusi:**
```
          BC=00  BC=01  BC=11  BC=10
A=0     |  1   |  1   |  1   |  1   |
A=1     |  0   |  0   |  1   |  0   |

Grup 1: Seluruh baris A=0 (m0,m1,m3,m2) -- 4 sel -> A'
Grup 2: m3 dan m7 (kolom BC=11) -- 2 sel -> BC

Hasil: F = A' + BC
```

Verifikasi m7: A=1, B=1, C=1 -> A'=0, BC=1 -> F=1 ✓
Verifikasi m4: A=1, B=0, C=0 -> A'=0, BC=0 -> F=0 ✓

### Contoh 7: Ekuivalensi Kontraposisi

**Soal:** Buktikan bahwa "Jika n² genap maka n genap" ekuivalen dengan
"Jika n ganjil maka n² ganjil".

**Solusi:**
```
Pernyataan asli: p → q
  p: n² genap
  q: n genap

Kontraposisi: ¬q → ¬p
  ¬q: n tidak genap = n ganjil
  ¬p: n² tidak genap = n² ganjil

Kontraposisi: "Jika n ganjil maka n² ganjil"

Karena kontraposisi selalu ekuivalen dengan pernyataan asli,
kedua pernyataan tersebut ekuivalen. ✓
```

### Contoh 8: Negasi Kuantor

**Soal:** Apa negasi dari "Semua bilangan prima lebih besar dari 1"?

**Solusi:**
```
Pernyataan: ∀x (prima(x) → x > 1)
Negasi: ¬∀x (prima(x) → x > 1)
      = ∃x ¬(prima(x) → x > 1)
      = ∃x ¬(¬prima(x) ∨ x > 1)          [Eliminasi implikasi]
      = ∃x (prima(x) ∧ ¬(x > 1))          [De Morgan]
      = ∃x (prima(x) ∧ x ≤ 1)

Dalam bahasa sehari-hari: "Ada bilangan prima yang kurang dari atau sama dengan 1."
```

### Contoh 9: Soal Gaya OSN - Operator Campuran

**Soal:** Diketahui p = TRUE, q = FALSE, r = TRUE.
Tentukan nilai dari: `(p → q) ↔ (¬r ∨ q)`

**Solusi:**
```
Langkah 1: Hitung p → q
  p=T, q=F -> T → F = FALSE

Langkah 2: Hitung ¬r ∨ q
  ¬r = ¬T = FALSE
  F ∨ q = F ∨ F = FALSE

Langkah 3: Hitung FALSE ↔ FALSE
  Biimplikasi bernilai TRUE jika kedua sisi sama.
  F ↔ F = TRUE

Jawaban: TRUE
```

### Contoh 10: Penyederhanaan Kompleks

**Soal:** Sederhanakan `(A ⊕ B) · (A ⊕ B)'`

**Solusi:**
```
Misalkan X = A ⊕ B

Maka ekspresi menjadi: X · X'

Berdasarkan hukum komplemen: X · X' = 0

Jawaban: 0 (FALSE untuk semua input)
```

### Contoh 11: Soal Penalaran Bertingkat

**Soal:** Diberikan premis-premis:
1. Jika hari minggu maka Andi libur.
2. Jika Andi libur maka dia pergi ke mall.
3. Andi tidak pergi ke mall.

Apa kesimpulannya?

**Solusi:**
```
p: Hari minggu
q: Andi libur
r: Andi pergi ke mall

Premis 1: p → q
Premis 2: q → r
Premis 3: ¬r

Langkah 1: Dari premis 1 dan 2, silogisme hipotetis: p → r
Langkah 2: Dari p → r dan premis 3 (¬r), modus tollens: ¬p

Kesimpulan: Bukan hari minggu (¬p).

Bonus: Dari premis 2 dan 3, modus tollens: ¬q (Andi tidak libur).
```

### Contoh 12: Boolean dalam Kode C++

**Soal:** Apa output dari kode berikut?
```cpp
int a = 5, b = 3, c = 0;
bool result = (a > b) && !(c || (a == b));
cout << result;
```

**Solusi:**
```
a > b = 5 > 3 = true
a == b = 5 == 3 = false
c = 0 (dianggap false dalam boolean)
c || (a == b) = false || false = false
!(false) = true
(a > b) && true = true && true = true

Output: 1 (true)
```

---

## 14. Tips dan Jebakan OSN

### 14.1 Jebakan Umum

1. **Implikasi F → apapun = TRUE**
   Banyak siswa lupa bahwa jika anteseden FALSE, implikasi selalu TRUE.

2. **Konvers bukan ekuivalen!**
   p → q TIDAK sama dengan q → p. Tapi SAMA dengan ¬q → ¬p (kontraposisi).

3. **OR dalam logika bersifat inklusif**
   "p atau q" dalam logika berarti salah satu atau keduanya. Berbeda dengan
   bahasa sehari-hari yang sering berarti eksklusif.

4. **Prioritas operator (dari tinggi ke rendah):**
   ¬ (NOT) > ∧ (AND) > ∨ (OR) > → (IMPLIKASI) > ↔ (BIIMPLIKASI)

5. **Short-circuit evaluation di C++:**
   `&&` dan `||` di C++ melakukan evaluasi singkat. Jika bagian kiri `&&` sudah FALSE,
   bagian kanan tidak dievaluasi.

### 14.2 Strategi Mengerjakan Soal

1. **Untuk soal tabel kebenaran:** Kerjakan sistematis baris per baris.
2. **Untuk penyederhanaan:** Cari pola komplemen (x + x' = 1) dan absorpsi dulu.
3. **Untuk penalaran:** Identifikasi bentuk premisnya (modus ponens/tollens/silogisme).
4. **Untuk soal C++:** Perhatikan prioritas operator dan short-circuit evaluation.
5. **Jika ragu:** Buat tabel kebenaran kecil untuk verifikasi.

### 14.3 Rumus Cepat yang Wajib Diingat

```
p → q  ≡  ¬p ∨ q                    [Paling sering dipakai!]
¬(p → q) ≡ p ∧ ¬q                   [Negasi implikasi]
¬(p ∧ q) ≡ ¬p ∨ ¬q                  [De Morgan 1]
¬(p ∨ q) ≡ ¬p ∧ ¬q                  [De Morgan 2]
x + x'y = x + y                      [Absorpsi extended]
Kontraposisi(p → q) = ¬q → ¬p        [Selalu ekuivalen]
```

---

## 15. Latihan Soal

### Bagian A: Evaluasi Ekspresi (Mudah)

1. Tentukan nilai: `(0 NAND 1) AND (1 NOR 0)`
2. Jika A=1, B=0, C=1, hitung: `A XOR (B OR C)`
3. Tentukan nilai: `(1 XNOR 0) OR (0 NAND 0)`
4. Jika p=T, q=F, tentukan: `(p → q) ∨ (q → p)`

### Bagian B: Penyederhanaan (Sedang)

5. Sederhanakan: `A·B + A·B' + A'·B`
6. Sederhanakan: `(A + B)·(A + C)·(B + C)`
7. Sederhanakan menggunakan De Morgan: `NOT(NOT(A OR B) AND C)`
8. Sederhanakan: `A'·B'·C' + A'·B'·C + A'·B·C' + A'·B·C`

### Bagian C: Logika Proposisional (Sedang-Sulit)

9. Tentukan apakah tautologi: `(p → q) ∨ (q → p)`
10. Apa negasi dari: "Jika semua siswa belajar maka ada yang lulus"?
11. Diberikan premis: "Jika Rina rajin maka nilainya bagus", "Jika nilainya bagus maka dia dapat beasiswa", "Rina tidak dapat beasiswa". Apa kesimpulannya?
12. Buktikan secara aljabar: `(p → q) ∧ (p → r) ≡ p → (q ∧ r)`

### Bagian D: Soal Gaya OSN (Sulit)

13. Berapa banyak fungsi Boolean f(A,B) yang memenuhi f(0,0)=1?
14. Untuk K-Map F(A,B,C) = Σm(1,2,5,6), tentukan ekspresi minimal.
15. Diketahui hanya operator NAND tersedia. Berapa jumlah minimum gerbang NAND untuk mengimplementasikan XOR(A,B)?

---

## 16. Kunci Jawaban Latihan

### Jawaban Bagian A:

**1.** `(0 NAND 1) AND (1 NOR 0)`
```
0 NAND 1 = NOT(0 AND 1) = NOT(0) = 1
1 NOR 0 = NOT(1 OR 0) = NOT(1) = 0
1 AND 0 = 0
Jawaban: 0
```

**2.** A=1, B=0, C=1: `A XOR (B OR C)`
```
B OR C = 0 OR 1 = 1
A XOR 1 = 1 XOR 1 = 0
Jawaban: 0
```

**3.** `(1 XNOR 0) OR (0 NAND 0)`
```
1 XNOR 0 = NOT(1 XOR 0) = NOT(1) = 0
0 NAND 0 = NOT(0 AND 0) = NOT(0) = 1
0 OR 1 = 1
Jawaban: 1
```

**4.** p=T, q=F: `(p → q) ∨ (q → p)`
```
p → q = T → F = F
q → p = F → T = T
F ∨ T = T
Jawaban: TRUE
```

Catatan: `(p → q) ∨ (q → p)` sebenarnya adalah TAUTOLOGI (selalu TRUE untuk semua p, q).

### Jawaban Bagian B:

**5.** `A·B + A·B' + A'·B`
```
= A·(B + B') + A'·B
= A·1 + A'·B
= A + A'·B
= A + B              [Absorpsi extended]
Jawaban: A + B
```

**6.** `(A + B)·(A + C)·(B + C)`
```
Menggunakan hukum konsensus (bentuk OR):
(A+B)·(A'+C)·(B+C) = (A+B)·(A'+C)

Tapi di sini bukan A dan A', jadi kita distribusi:
(A+B)·(A+C) = A + BC  [Distributif bentuk OR]
Lalu: (A + BC)·(B+C) = A·B + A·C + B·C
Hmm, coba langsung:
(A+B)·(A+C) = A + BC
(A + BC)·(B + C) = AB + AC + B²C + BC²  -- ini untuk aljabar biasa.

Untuk Boolean: 
(A+B)·(A+C) = A + BC  [Distributif]
(A+BC)·(B+C) = A(B+C) + BC(B+C)
             = AB + AC + BC·B + BC·C
             = AB + AC + BC + BC
             = AB + AC + BC

Jawaban: AB + AC + BC
```

**7.** `NOT(NOT(A OR B) AND C)`
```
= NOT(NOT(A OR B)) OR NOT(C)     [De Morgan]
= (A OR B) OR NOT(C)             [Involusi]
= A + B + C'
Jawaban: A + B + C'
```

**8.** `A'·B'·C' + A'·B'·C + A'·B·C' + A'·B·C`
```
= A'·B'·(C' + C) + A'·B·(C' + C)
= A'·B'·1 + A'·B·1
= A'·B' + A'·B
= A'·(B' + B)
= A'·1
= A'
Jawaban: A'
```

### Jawaban Bagian C:

**9.** `(p → q) ∨ (q → p)` -- Apakah tautologi?
```
| p | q | p→q | q→p | (p→q)∨(q→p) |
|---|---|-----|-----|-------------|
| T | T |  T  |  T  |      T      |
| T | F |  F  |  T  |      T      |
| F | T |  T  |  F  |      T      |
| F | F |  T  |  T  |      T      |

Semua baris TRUE. Ya, ini TAUTOLOGI.
```

**10.** Negasi dari "Jika semua siswa belajar maka ada yang lulus":
```
Asli: (∀x belajar(x)) → (∃x lulus(x))
Negasi: ¬((∀x belajar(x)) → (∃x lulus(x)))
      = (∀x belajar(x)) ∧ ¬(∃x lulus(x))     [¬(p→q) = p∧¬q]
      = (∀x belajar(x)) ∧ (∀x ¬lulus(x))

Dalam bahasa: "Semua siswa belajar DAN tidak ada yang lulus."
```

**11.** Premis: p→q, q→r, ¬r
```
Dari q→r dan ¬r (modus tollens): ¬q (nilainya tidak bagus)
Dari p→q dan ¬q (modus tollens): ¬p (Rina tidak rajin)

Kesimpulan: Rina tidak rajin (dan nilainya tidak bagus).
```

**12.** Buktikan `(p → q) ∧ (p → r) ≡ p → (q ∧ r)`
```
Sisi kiri:
(p → q) ∧ (p → r)
= (¬p ∨ q) ∧ (¬p ∨ r)        [Eliminasi implikasi]
= ¬p ∨ (q ∧ r)                [Distributif]

Sisi kanan:
p → (q ∧ r)
= ¬p ∨ (q ∧ r)                [Eliminasi implikasi]

Kedua sisi sama: ¬p ∨ (q ∧ r). Terbukti. ✓
```

### Jawaban Bagian D:

**13.** Berapa banyak fungsi Boolean f(A,B) yang memenuhi f(0,0)=1?
```
Fungsi Boolean f(A,B) ditentukan oleh nilainya pada 4 input: (0,0), (0,1), (1,0), (1,1).
Total fungsi Boolean 2 variabel = 2^4 = 16.
Jika f(0,0) = 1 sudah ditetapkan, sisanya 3 input masing-masing bisa 0 atau 1.
Banyak fungsi = 2^3 = 8.
```

**14.** K-Map F(A,B,C) = Σm(1,2,5,6):
```
m1 = A'B'C, m2 = A'BC', m5 = AB'C, m6 = ABC'

          BC=00  BC=01  BC=11  BC=10
A=0     |  0   |  1   |  0   |  1   |
A=1     |  0   |  1   |  0   |  1   |

Grup 1: Kolom BC=01 (m1, m5) -> B'C
Grup 2: Kolom BC=10 (m2, m6) -> BC'

Jawaban: F = B'C + BC' = B ⊕ C
```

**15.** Jumlah minimum gerbang NAND untuk XOR:
```
XOR(A,B) = (A NAND (A NAND B)) NAND (B NAND (A NAND B))

Membutuhkan 4 gerbang NAND:
- G1 = A NAND B
- G2 = A NAND G1
- G3 = B NAND G1
- G4 = G2 NAND G3

Jawaban: 4 gerbang NAND
```

---

## 17. Rangkuman

| Topik | Poin Kunci |
|-------|-----------|
| Operator Boolean | 8 operator: AND, OR, NOT, XOR, NAND, NOR, XNOR, IMPLIKASI |
| Hukum terpenting | De Morgan, Absorpsi, Komplemen, Distributif |
| Implikasi | F→apapun = T; hanya T→F = F |
| Kontraposisi | Selalu ekuivalen dengan asli |
| K-Map | Gunakan Gray code, cari grup 2^n terbesar |
| Penalaran | Modus Ponens, Modus Tollens, Silogisme |
| Fallacy | Affirming consequent, Denying antecedent |
| Kuantor | ¬∀ = ∃¬ dan ¬∃ = ∀¬ |

---

*Materi ini mencakup seluruh topik Aljabar Boolean dan Logika yang relevan untuk OSK Informatika 2026.*
