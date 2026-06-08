# Materi 01 — Aljabar Boolean & Logika

## 1. Operasi Dasar Boolean

| Operasi | Simbol | Deskripsi |
|---------|--------|-----------|
| AND | `∧` / `&` / `·` | Bernilai 1 hanya jika **kedua** operand 1 |
| OR | `∨` / `\|` / `+` | Bernilai 1 jika **salah satu** operand 1 |
| NOT | `¬` / `!` / `~` | Membalik nilai: 0→1, 1→0 |
| XOR | `⊕` / `^` | Bernilai 1 jika operand **berbeda** |
| NAND | `↑` | NOT AND |
| NOR | `↓` | NOT OR |

### Tabel Kebenaran Dasar
| A | B | A AND B | A OR B | NOT A | A XOR B |
|---|---|---------|--------|-------|---------|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

---

## 2. Hukum-Hukum Aljabar Boolean

### Hukum Identitas
- A AND 1 = A
- A OR 0 = A

### Hukum Null/Dominasi
- A AND 0 = 0
- A OR 1 = 1

### Hukum Idempoten
- A AND A = A
- A OR A = A

### Hukum Komplemen
- A AND (NOT A) = 0
- A OR (NOT A) = 1

### Hukum Involusi (Double Negation)
- NOT (NOT A) = A

### Hukum Komutatif
- A AND B = B AND A
- A OR B = B OR A

### Hukum Asosiatif
- (A AND B) AND C = A AND (B AND C)
- (A OR B) OR C = A OR (B OR C)

### Hukum Distributif
- A AND (B OR C) = (A AND B) OR (A AND C)
- A OR (B AND C) = (A OR B) AND (A OR C)

### Hukum De Morgan ⭐ (PENTING)
- NOT (A AND B) = (NOT A) OR (NOT B)
- NOT (A OR B) = (NOT A) AND (NOT B)

### Hukum Absorpsi
- A AND (A OR B) = A
- A OR (A AND B) = A

---

## 3. Logika Proposisional

### Operator Logika
| Operasi | Simbol | Makna |
|---------|--------|-------|
| Konjungsi | p ∧ q | p dan q |
| Disjungsi | p ∨ q | p atau q |
| Negasi | ¬p | bukan p |
| Implikasi | p → q | jika p maka q |
| Biimplikasi | p ↔ q | p jika dan hanya jika q |

### Tabel Kebenaran Implikasi
| p | q | p → q | p ↔ q |
|---|---|-------|-------|
| T | T | T | T |
| T | F | F | F |
| F | T | T | F |
| F | F | T | T |

> **Ingat:** Implikasi p→q **hanya FALSE** jika p TRUE dan q FALSE.

---

## 4. Induksi & Deduksi

### Modus Ponens
- Premis 1: p → q (jika p maka q)
- Premis 2: p (p benar)
- Kesimpulan: q ✓

### Modus Tollens
- Premis 1: p → q
- Premis 2: ¬q (q salah)
- Kesimpulan: ¬p ✓

### Silogisme Hipotetis
- Premis 1: p → q
- Premis 2: q → r
- Kesimpulan: p → r ✓

---

## 5. Contoh Soal

**Soal 1:** Sederhanakan ekspresi: `A AND (A OR B)`

> Jawab: Gunakan hukum absorpsi → **A**

**Soal 2:** `NOT (A AND B)` ekuivalen dengan?

> Jawab: Gunakan De Morgan → **(NOT A) OR (NOT B)**

**Soal 3:** Jika p = TRUE dan q = FALSE, tentukan nilai p → q.

> Jawab: p=T, q=F → p→q = **FALSE**

---

## 6. Latihan
1. Buat tabel kebenaran untuk `(A OR B) AND (NOT A)`
2. Sederhanakan: `(A AND B) OR (A AND NOT B)`
3. Gunakan De Morgan untuk menyederhanakan: `NOT (NOT A OR NOT B)`
4. Jika premis: "Jika hujan maka jalanan basah" dan "jalanan tidak basah", apa kesimpulannya?

*Jawaban di folder `../latihan/`*
