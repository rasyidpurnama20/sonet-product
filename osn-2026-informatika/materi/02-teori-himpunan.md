# Materi 02 — Teori Himpunan

## 1. Definisi Dasar

- **Himpunan (Set):** Kumpulan objek yang terdefinisi dengan jelas.
  - Notasi: `A = {1, 2, 3, 4}`
- **Anggota/Elemen:** Objek dalam himpunan. `2 ∈ A` (2 adalah anggota A)
- **Bukan Anggota:** `5 ∉ A`
- **Kardinalitas:** Jumlah anggota himpunan. `|A| = 4`
- **Himpunan Kosong:** `∅ = {}`, kardinalitas = 0
- **Himpunan Semesta (U):** Himpunan yang memuat semua elemen yang dibahas.

---

## 2. Jenis-Jenis Himpunan

| Jenis | Simbol | Contoh |
|-------|--------|--------|
| Bilangan Asli | ℕ | {1, 2, 3, 4, ...} |
| Bilangan Bulat | ℤ | {..., -2, -1, 0, 1, 2, ...} |
| Bilangan Rasional | ℚ | {p/q \| p,q ∈ ℤ, q≠0} |
| Bilangan Real | ℝ | Semua bilangan termasuk irrasional |

---

## 3. Relasi Antar Himpunan

- **Subset (Himpunan Bagian):** A ⊆ B artinya semua elemen A ada di B.
  - Contoh: `{1,2} ⊆ {1,2,3}` → TRUE
- **Proper Subset:** A ⊂ B artinya A ⊆ B dan A ≠ B.
- **Superset:** B ⊇ A (B memuat semua elemen A)
- **Himpunan Sama:** A = B jika A ⊆ B dan B ⊆ A

---

## 4. Operasi Himpunan

### Gabungan (Union) — `A ∪ B`
Himpunan semua elemen yang ada di A **atau** B.
```
A = {1, 2, 3}
B = {3, 4, 5}
A ∪ B = {1, 2, 3, 4, 5}
```

### Irisan (Intersection) — `A ∩ B`
Himpunan elemen yang ada di A **dan** B.
```
A ∩ B = {3}
```

### Selisih (Difference) — `A - B` atau `A \ B`
Elemen yang ada di A **tapi tidak** ada di B.
```
A - B = {1, 2}
B - A = {4, 5}
```

### Komplemen — `Aᶜ` atau `A'`
Semua elemen di U yang **tidak** ada di A.
```
U = {1,2,3,4,5}, A = {1,2,3}
Aᶜ = {4, 5}
```

### Produk Kartesian — `A × B`
Himpunan semua pasangan terurut (a, b) dengan a ∈ A dan b ∈ B.
```
A = {1,2}, B = {x,y}
A × B = {(1,x), (1,y), (2,x), (2,y)}
|A × B| = |A| × |B| = 2 × 2 = 4
```

---

## 5. Hukum Himpunan

| Hukum | Persamaan |
|-------|-----------|
| Identitas | A ∪ ∅ = A, A ∩ U = A |
| Dominasi | A ∪ U = U, A ∩ ∅ = ∅ |
| Idempoten | A ∪ A = A, A ∩ A = A |
| Komplemen | A ∪ Aᶜ = U, A ∩ Aᶜ = ∅ |
| Komutatif | A ∪ B = B ∪ A |
| Asosiatif | (A ∪ B) ∪ C = A ∪ (B ∪ C) |
| Distributif | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ |

---

## 6. Prinsip Inklusi-Eksklusi (PIE)

Untuk 2 himpunan:
```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

Untuk 3 himpunan:
```
|A ∪ B ∪ C| = |A| + |B| + |C|
              - |A ∩ B| - |A ∩ C| - |B ∩ C|
              + |A ∩ B ∩ C|
```

**Contoh:**
- Dari 30 siswa, 18 suka matematika, 15 suka fisika, 10 suka keduanya.
- Berapa yang suka matematika **atau** fisika?
- `|M ∪ F| = 18 + 15 - 10 = 23 siswa`

---

## 7. Diagram Venn

Representasi visual himpunan menggunakan lingkaran bertumpang tindih.

```
Semesta (U)
┌──────────────────────┐
│   ┌───┐  ┌───┐       │
│   │ A │∩ │ B │       │
│   │   │AB│   │       │
│   └───┘  └───┘       │
└──────────────────────┘
```

- **Area A saja** = A - B
- **Area tumpang tindih** = A ∩ B
- **Area B saja** = B - A
- **Di luar keduanya** = (A ∪ B)ᶜ

---

## 8. Contoh Soal

**Soal 1:** Diketahui A = {1,2,3,4}, B = {3,4,5,6}. Tentukan A ∩ B.

> Jawab: `{3, 4}`

**Soal 2:** Dari 50 siswa, 30 ikut ekskul basket, 25 ikut ekskul futsal, 10 ikut keduanya. Berapa yang tidak ikut ekskul apapun?

> Jawab: `|B ∪ F| = 30 + 25 - 10 = 45`. Yang tidak ikut = `50 - 45 = 5 siswa`

---

## 9. Latihan
1. Diketahui U = {1..10}, A = {2,4,6,8,10}, B = {1,2,3,4,5}. Tentukan: A∩B, A∪B, Aᶜ, A-B.
2. Berapa banyak subset dari himpunan {a, b, c}?
3. Gunakan PIE untuk soal: 40 mahasiswa ambil Fisika, 35 ambil Kimia, 20 ambil keduanya. Berapa total mahasiswa?

*Jawaban di folder `../latihan/`*
