# Folder Latihan — OSN 2026 Informatika

Kumpulan soal latihan dan pembahasannya untuk persiapan OSK Informatika 2026.

---

## File Pembahasan Tersedia

| File | Isi | Soal |
|------|-----|------|
| `tryout-koja-1-pembahasan.md` | Try Out Koja 1 lengkap dengan langkah penyelesaian & tautan materi | 40 soal |

---

## Struktur Folder

```
latihan/
├── README.md                        ← file ini
├── tryout-koja-1-pembahasan.md      ← TO Koja 1: 40 soal + pembahasan
├── Try Out Koja 1 - Soal + Kunci Jawaban.pdf  ← soal asli PDF
└── imgs/                            ← gambar kode program dari PDF
```

---

## Checklist Latihan

### Try Out / Simulasi
- [x] Try Out Koja 1 — 40 soal (lihat `tryout-koja-1-pembahasan.md`)
- [ ] Try Out Koja 2 (jika tersedia)
- [ ] Simulasi soal OSK tahun lalu (2024, 2023, 2022)

### Bagian A — Bebras / Abstraksi CT
- [ ] Kerjakan 10 soal Bebras Indonesia 2024
- [ ] Kerjakan 10 soal Bebras Indonesia 2023
- [ ] Kerjakan 10 soal Bebras Internasional pilihan

### Bagian B — Studi Kasus Komputasional
- [ ] Soal OSK Informatika 2024
- [ ] Soal OSK Informatika 2023
- [ ] Soal OSK Informatika 2022
- [ ] 5 soal USACO Bronze simulasi

### Bagian C — Trace Kode C++
- [ ] 10 soal trace loop sederhana
- [ ] 10 soal trace array
- [ ] 10 soal trace rekursi
- [ ] Soal Bagian C OSK tahun lalu

---

## Jawaban Soal Latihan dari Materi

### Dari Materi 01 (Aljabar Boolean)
1. Tabel kebenaran `(A OR B) AND (NOT A)`:

| A | B | A OR B | NOT A | Hasil |
|---|---|--------|-------|-------|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |

2. `(A AND B) OR (A AND NOT B)` = `A AND (B OR NOT B)` = `A AND 1` = **A**
3. `NOT (NOT A OR NOT B)` = `NOT(NOT A) AND NOT(NOT B)` = **A AND B**
4. Premis: "jika hujan maka jalanan basah", "jalanan tidak basah" → Modus Tollens → **Tidak hujan**

---

### Dari Materi 02 (Teori Himpunan)
1. U={1..10}, A={2,4,6,8,10}, B={1,2,3,4,5}:
   - A∩B = **{2, 4}**
   - A∪B = **{1,2,3,4,5,6,8,10}**
   - Aᶜ = **{1,3,5,7,9}**
   - A-B = **{6,8,10}**
2. Subset dari {a,b,c}: **2³ = 8** subset
3. |F ∪ K| = 40 + 35 - 20 = **55 mahasiswa**

---

### Dari Materi 03 (Kombinatorika)
1. Round-robin 8 tim: C(8,2) = **28 pertandingan**
2. 4 jabatan dari 10 orang: P(10,4) = 10×9×8×7 = **5040 cara**
3. Suku ke-15: a=5, d=3, a₁₅ = 5 + 14×3 = **47**
4. Deret geometri 2+4+8+...+20 suku: a=2, r=2, S₂₀ = 2×(2²⁰-1)/(2-1) = **2 097 150**

---

### Dari Materi 04 (Graf)
1. Adjacency matrix graf {1-2, 2-3, 3-4, 4-1, 1-3}:
```
  1 2 3 4
1[0 1 1 1]
2[1 0 1 0]
3[1 1 0 1]
4[1 0 1 0]
```
2. DFS dari 1: **1, 2, 3, 4** (salah satu urutan valid)
3. Rekonstruksi pohon dari pre/in-order → lihat materi 04.

---

## Template Pengerjaan Soal

Saat mengerjakan soal baru, gunakan template ini:

```
## Soal [nomor] — [sumber] [tahun]

### Deskripsi
[salin teks soal]

### Analisis
- Tipe: [ ] Pilihan Ganda  [ ] Isian Singkat  [ ] Benar/Salah
- Bagian: [ ] A  [ ] B  [ ] C
- Topik: ...

### Solusi
[langkah-langkah penyelesaian]

### Jawaban
**[jawaban akhir]**
```
