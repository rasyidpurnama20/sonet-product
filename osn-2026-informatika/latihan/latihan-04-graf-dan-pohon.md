# Latihan 04 — Graf & Pohon

**Mata Pelajaran:** OSN Informatika 2026 — Bab 4  
**Jumlah Soal:** 32 soal  
**Tingkat Kesulitan:** Mudah (★), Sedang (★★), Sulit (★★★)  
**Tipe Soal:** Pilihan Ganda (PG), Isian Singkat (IS), Benar/Salah (B/S), Uraian (U)  
**Referensi Materi:** [04-graf-dan-pohon.md](../materi/04-graf-dan-pohon.md)

---

## Bagian A: Terminologi dan Sifat-Sifat Graf

---

### Soal 1 — Derajat Simpul ★

**Tipe:** Isian Singkat

**Soal:**  
Perhatikan graf berikut:

```
    A --- B --- C
    |         / |
    D --- E    F
```

Sisi-sisi graf: {(A,B), (A,D), (B,C), (C,E), (C,F), (D,E)}

Tentukan derajat setiap simpul dan jumlah total derajat seluruh simpul.

**Pembahasan:**

```
Langkah 1: Hitung derajat tiap simpul (banyaknya sisi yang incident)
  deg(A) = 2  → terhubung ke B, D
  deg(B) = 2  → terhubung ke A, C
  deg(C) = 3  → terhubung ke B, E, F
  deg(D) = 2  → terhubung ke A, E
  deg(E) = 2  → terhubung ke C, D
  deg(F) = 1  → terhubung ke C

Langkah 2: Jumlahkan semua derajat
  Total = 2 + 2 + 3 + 2 + 2 + 1 = 12

Langkah 3: Verifikasi dengan Handshaking Lemma
  Jumlah derajat = 2 × |E| = 2 × 6 = 12 ✓
```

**Jawaban:** deg(A)=2, deg(B)=2, deg(C)=3, deg(D)=2, deg(E)=2, deg(F)=1. Total derajat = 12.

---

### Soal 2 — Handshaking Lemma ★★

**Tipe:** Isian Singkat

**Soal:**  
Suatu graf memiliki 8 simpul. Tiga simpul berderajat 4, dua simpul berderajat 3, dan sisanya berderajat 2. Berapa jumlah sisi graf tersebut?

**Pembahasan:**

```
Langkah 1: Identifikasi jumlah simpul tiap derajat
  3 simpul berderajat 4
  2 simpul berderajat 3
  Sisanya = 8 - 3 - 2 = 3 simpul berderajat 2

Langkah 2: Hitung jumlah total derajat
  Total = 3×4 + 2×3 + 3×2
        = 12 + 6 + 6
        = 24

Langkah 3: Gunakan Handshaking Lemma
  Jumlah sisi = Total derajat / 2 = 24 / 2 = 12
```

**Jawaban: 12 sisi**

---

### Soal 3 — Graf Lengkap ★

**Tipe:** Pilihan Ganda

**Soal:**  
Sebuah graf lengkap K_7 memiliki berapa sisi?

A. 14  
B. 21  
C. 28  
D. 42  

**Pembahasan:**

```
Langkah 1: Rumus jumlah sisi graf lengkap K_n
  |E| = n(n-1)/2

Langkah 2: Substitusi n = 7
  |E| = 7 × 6 / 2 = 42 / 2 = 21
```

**Jawaban: B. 21**

---

### Soal 4 — Graf Bipartit ★★

**Tipe:** Benar/Salah

**Soal:**  
Perhatikan pernyataan-pernyataan berikut. Tentukan benar atau salah.

1. Graf siklus C_4 adalah graf bipartit.  
2. Graf siklus C_5 adalah graf bipartit.  
3. Graf lengkap K_4 adalah graf bipartit.  
4. Graf bipartit lengkap K_{3,3} memiliki 9 sisi.  

**Pembahasan:**

```
Langkah 1: Analisis C_4
  C_4: 1-2-3-4-1
  Partisi: X = {1,3}, Y = {2,4}
  Semua sisi menghubungkan X dan Y → BIPARTIT → BENAR

Langkah 2: Analisis C_5
  C_5: 1-2-3-4-5-1
  Coba partisi: 1∈X, 2∈Y, 3∈X, 4∈Y, 5∈X
  Sisi (5,1): keduanya di X → GAGAL
  Siklus ganjil bukan bipartit → SALAH

Langkah 3: Analisis K_4
  K_4 mengandung siklus C_3 (segitiga), yaitu siklus ganjil
  → BUKAN bipartit → SALAH

Langkah 4: Analisis K_{3,3}
  Jumlah sisi K_{m,n} = m × n = 3 × 3 = 9 → BENAR
```

**Jawaban:** 1. Benar, 2. Salah, 3. Salah, 4. Benar

---

### Soal 5 — Isomorfisma Graf ★★★

**Tipe:** Uraian

**Soal:**  
Tentukan apakah kedua graf berikut isomorfis:

```
Graf G:              Graf H:
  A --- B              P --- Q
  |     |              |   / |
  C --- D              R     S
                       |     |
                       T --- U
```

Graf G: V = {A,B,C,D}, E = {(A,B),(A,C),(B,D),(C,D)}  
Graf H: V = {P,Q,R,S,T,U}, E = {(P,Q),(P,R),(Q,R),(Q,S),(R,T),(S,U),(T,U)}

**Pembahasan:**

```
Langkah 1: Bandingkan jumlah simpul
  Graf G: |V| = 4
  Graf H: |V| = 6
  → Jumlah simpul BERBEDA

Langkah 2: Kesimpulan
  Syarat perlu isomorfisma: |V(G)| = |V(H)| dan |E(G)| = |E(H)|
  Karena |V(G)| = 4 ≠ 6 = |V(H)|, kedua graf TIDAK isomorfis.
```

**Jawaban:** Kedua graf TIDAK isomorfis karena memiliki jumlah simpul yang berbeda (4 vs 6).

---

### Soal 6 — Barisan Derajat ★★

**Tipe:** Pilihan Ganda

**Soal:**  
Manakah barisan derajat berikut yang TIDAK MUNGKIN merupakan barisan derajat suatu graf sederhana?

A. (3, 3, 3, 3, 2)  
B. (4, 3, 2, 2, 1)  
C. (3, 3, 3, 1)  
D. (2, 2, 2, 2, 2)

**Pembahasan:**

```
Langkah 1: Cek jumlah derajat genap (syarat perlu)
  A: 3+3+3+3+2 = 14 (genap) ✓
  B: 4+3+2+2+1 = 12 (genap) ✓
  C: 3+3+3+1 = 10 (genap) ✓
  D: 2+2+2+2+2 = 10 (genap) ✓

Langkah 2: Cek dengan Erdos-Gallai atau konstruksi
  A: 5 simpul, derajat maksimum 3 ≤ 4 (n-1). Bisa: K_4 minus satu sisi 
     + tambah 1 simpul. Valid.
  B: 5 simpul, derajat max = 4 = n-1. Simpul pertama harus 
     terhubung ke semua. Sisa derajat: (2,1,1,0). 
     Tapi simpul ke-2 harus deg 3, tersisa 2 masih kurang.
     Mari pakai Erdos-Gallai:
     Urutkan menurun: 4,3,2,2,1
     k=1: 4 ≤ 1(0) + min(4,1)+min(3,1)+min(2,1)+min(1,1) = 0+1+1+1+1 = 4 ✓
     k=2: 4+3=7 ≤ 2(1) + min(4,2)+min(2,2)+min(1,2) = 2+2+2+1 = 7 ✓
     Lanjutkan... valid.
  C: 4 simpul, deg max = 3 = n-1. Simpul deg-3 harus terhubung ke semua.
     Jika satu simpul berderajat 3 terhubung ke 3 simpul lain,
     3 simpul lain masing-masing sudah punya 1 sisi.
     Sisa derajat yang dibutuhkan: (2,2,0)
     Simpul ke-4 (deg 1) sudah terpenuhi.
     Simpul 2 dan 3 perlu tambah 2 sisi lagi masing-masing.
     Tapi total simpul tersisa hanya 2 (di antara simpul 2 dan 3 sendiri).
     Derajat tersisa: simpul 2 perlu 2, simpul 3 perlu 2.
     Hanya ada 1 sisi yang bisa ditambahkan di antara mereka.
     → TIDAK BISA dicapai → TIDAK VALID

  D: 5 simpul masing-masing deg 2 → graf siklus C_5. Valid.
```

**Jawaban: C. (3, 3, 3, 1)**

---

## Bagian B: Penelusuran BFS dan DFS

---

### Soal 7 — BFS Sederhana ★

**Tipe:** Uraian

**Soal:**  
Lakukan penelusuran BFS pada graf berikut mulai dari simpul A. Jika ada pilihan simpul, pilih yang berurutan secara alfabet.

```
    A --- B --- E
    |     |
    C --- D --- F
```

Sisi: {(A,B), (A,C), (B,D), (B,E), (C,D), (D,F)}

**Pembahasan:**

```
Langkah 1: Inisialisasi
  Queue: [A]
  Visited: {A}
  Urutan kunjungan: A

Langkah 2: Proses A
  Tetangga A yang belum dikunjungi: B, C (urut alfabet)
  Queue: [B, C]
  Visited: {A, B, C}
  Urutan kunjungan: A, B, C

Langkah 3: Proses B
  Tetangga B yang belum dikunjungi: D, E (A sudah dikunjungi)
  Queue: [C, D, E]
  Visited: {A, B, C, D, E}
  Urutan kunjungan: A, B, C, D, E

Langkah 4: Proses C
  Tetangga C yang belum dikunjungi: (A sudah, D sudah)
  Queue: [D, E]
  Urutan kunjungan: A, B, C, D, E

Langkah 5: Proses D
  Tetangga D yang belum dikunjungi: F (B sudah, C sudah)
  Queue: [E, F]
  Visited: {A, B, C, D, E, F}
  Urutan kunjungan: A, B, C, D, E, F

Langkah 6: Proses E
  Tetangga E yang belum dikunjungi: (B sudah)
  Queue: [F]
  Urutan kunjungan: A, B, C, D, E, F

Langkah 7: Proses F
  Tetangga F yang belum dikunjungi: (D sudah)
  Queue: []
  Urutan kunjungan: A, B, C, D, E, F
```

**Jawaban:** Urutan BFS: A → B → C → D → E → F

---

### Soal 8 — DFS Sederhana ★

**Tipe:** Uraian

**Soal:**  
Lakukan penelusuran DFS (menggunakan stack/rekursi) pada graf yang sama seperti Soal 7, mulai dari simpul A. Pilih tetangga secara alfabet.

```
    A --- B --- E
    |     |
    C --- D --- F
```

Sisi: {(A,B), (A,C), (B,D), (B,E), (C,D), (D,F)}

**Pembahasan:**

```
Langkah 1: Mulai dari A
  Stack: [A]
  Visited: {A}
  Urutan: A

Langkah 2: Dari A, pilih tetangga alfabet terkecil yang belum dikunjungi: B
  Stack: [A, B]
  Visited: {A, B}
  Urutan: A, B

Langkah 3: Dari B, tetangga belum dikunjungi: D, E → pilih D
  Stack: [A, B, D]
  Visited: {A, B, D}
  Urutan: A, B, D

Langkah 4: Dari D, tetangga belum dikunjungi: C, F → pilih C
  Stack: [A, B, D, C]
  Visited: {A, B, C, D}
  Urutan: A, B, D, C

Langkah 5: Dari C, tetangga belum dikunjungi: (A sudah, D sudah) → tidak ada
  Backtrack ke D
  Stack: [A, B, D]

Langkah 6: Dari D, tetangga belum dikunjungi: F
  Stack: [A, B, D, F]
  Visited: {A, B, C, D, F}
  Urutan: A, B, D, C, F

Langkah 7: Dari F, tetangga belum dikunjungi: (D sudah) → tidak ada
  Backtrack ke D, lalu ke B
  Stack: [A, B]

Langkah 8: Dari B, tetangga belum dikunjungi: E
  Stack: [A, B, E]
  Visited: {A, B, C, D, E, F}
  Urutan: A, B, D, C, F, E

Langkah 9: Dari E, tidak ada tetangga belum dikunjungi
  Backtrack sampai stack kosong. Selesai.
```

**Jawaban:** Urutan DFS: A → B → D → C → F → E

---

### Soal 9 — BFS Shortest Path ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan graf tak berbobot berikut. Tentukan jarak terpendek (jumlah sisi minimum) dari simpul 1 ke simpul 6.

```
    1 --- 2 --- 3
    |           |
    4 --- 5 --- 6
          |
          7
```

Sisi: {(1,2), (1,4), (2,3), (3,6), (4,5), (5,6), (5,7)}

**Pembahasan:**

```
Langkah 1: Jalankan BFS dari simpul 1, catat jarak (level)
  Level 0: {1}        → jarak[1] = 0
  Level 1: {2, 4}     → jarak[2] = 1, jarak[4] = 1
  Level 2: {3, 5}     → jarak[3] = 2, jarak[5] = 2
  Level 3: {6, 7}     → jarak[6] = 3, jarak[7] = 3

Langkah 2: Jarak terpendek dari 1 ke 6
  jarak[6] = 3

Langkah 3: Verifikasi jalur
  Jalur 1: 1 → 2 → 3 → 6 (3 sisi) ✓
  Jalur 2: 1 → 4 → 5 → 6 (3 sisi) ✓
  Keduanya memiliki panjang 3.
```

**Jawaban: 3 sisi**

---

### Soal 10 — DFS pada Graf Berarah ★★

**Tipe:** Uraian

**Soal:**  
Lakukan DFS pada graf berarah (digraph) berikut mulai dari simpul A. Jika ada pilihan, pilih alfabet terkecil.

```
  A → B → D
  ↓       ↑
  C → E → F
```

Sisi berarah: {A→B, A→C, B→D, C→E, E→F, F→D}

Tentukan urutan kunjungan DFS dan klasifikasikan sisi-sisinya (tree edge, back edge, forward edge, cross edge).

**Pembahasan:**

```
Langkah 1: DFS dari A
  Kunjungi A (waktu masuk = 1)
  Tetangga A: B, C → pilih B

Langkah 2: Kunjungi B (waktu masuk = 2)
  Tetangga B: D → kunjungi D

Langkah 3: Kunjungi D (waktu masuk = 3)
  Tetangga D: tidak ada
  Selesai D (waktu keluar = 4)
  Backtrack ke B

Langkah 4: Selesai B (waktu keluar = 5)
  Backtrack ke A, kunjungi C

Langkah 5: Kunjungi C (waktu masuk = 6)
  Tetangga C: E → kunjungi E

Langkah 6: Kunjungi E (waktu masuk = 7)
  Tetangga E: F → kunjungi F

Langkah 7: Kunjungi F (waktu masuk = 8)
  Tetangga F: D → D sudah selesai (waktu keluar < waktu masuk F)
  Sisi F→D: cross edge (D selesai sebelum F mulai? 
    D: masuk=3, keluar=4; F: masuk=8
    Karena D selesai sebelum F dikunjungi → cross edge)
  Selesai F (waktu keluar = 9)

Langkah 8: Selesai E (waktu keluar = 10)
  Selesai C (waktu keluar = 11)
  Selesai A (waktu keluar = 12)

Urutan kunjungan DFS: A, B, D, C, E, F

Klasifikasi sisi:
  A→B: tree edge (B ditemukan dari A)
  A→C: tree edge (C ditemukan dari A)
  B→D: tree edge (D ditemukan dari B)
  C→E: tree edge (E ditemukan dari C)
  E→F: tree edge (F ditemukan dari E)
  F→D: cross edge (D sudah selesai, bukan ancestor F)
```

**Jawaban:** Urutan DFS: A → B → D → C → E → F. Sisi F→D adalah cross edge, sisanya tree edge.

---

### Soal 11 — Komponen Terhubung via BFS ★★

**Tipe:** Isian Singkat

**Soal:**  
Graf G memiliki simpul {1, 2, 3, 4, 5, 6, 7, 8} dengan sisi:
{(1,2), (1,3), (2,3), (4,5), (6,7), (6,8), (7,8)}

Berapa banyak komponen terhubung dalam graf G? Sebutkan anggota setiap komponen.

**Pembahasan:**

```
Langkah 1: Jalankan BFS/DFS dari simpul 1
  Dari 1: kunjungi 1, 2, 3
  Komponen 1: {1, 2, 3}

Langkah 2: Simpul belum dikunjungi: {4, 5, 6, 7, 8}
  Jalankan BFS dari 4: kunjungi 4, 5
  Komponen 2: {4, 5}

Langkah 3: Simpul belum dikunjungi: {6, 7, 8}
  Jalankan BFS dari 6: kunjungi 6, 7, 8
  Komponen 3: {6, 7, 8}

Langkah 4: Semua simpul telah dikunjungi
  Jumlah komponen = 3
```

**Jawaban:** 3 komponen terhubung: {1,2,3}, {4,5}, {6,7,8}

---

### Soal 12 — Deteksi Siklus dengan DFS ★★★

**Tipe:** Uraian

**Soal:**  
Gunakan DFS untuk menentukan apakah graf berikut mengandung siklus:

```
    1 --- 2
    |     |
    3 --- 4 --- 5
```

Sisi: {(1,2), (1,3), (2,4), (3,4), (4,5)}

**Pembahasan:**

```
Langkah 1: Jalankan DFS dari simpul 1
  Kunjungi 1, parent[1] = null
  Pilih tetangga 2
  
Langkah 2: Kunjungi 2, parent[2] = 1
  Tetangga: 1 (parent, skip), 4
  Kunjungi 4

Langkah 3: Kunjungi 4, parent[4] = 2
  Tetangga: 2 (parent, skip), 3, 5
  Kunjungi 3

Langkah 4: Kunjungi 3, parent[3] = 4
  Tetangga: 1, 4 (parent, skip)
  Cek simpul 1: sudah dikunjungi DAN bukan parent dari 3
  → Ditemukan back edge (3,1) → ADA SIKLUS!

Langkah 5: Identifikasi siklus
  Siklus: 1 → 2 → 4 → 3 → 1
  Panjang siklus = 4
```

**Jawaban:** Ya, graf mengandung siklus. Siklus yang ditemukan: 1-2-4-3-1.

---

## Bagian C: Penelusuran Pohon (Tree Traversal)

---

### Soal 13 — Preorder, Inorder, Postorder ★

**Tipe:** Uraian

**Soal:**  
Diberikan pohon biner berikut:

```
        A
       / \
      B   C
     / \   \
    D   E   F
       /
      G
```

Tentukan urutan kunjungan secara: (a) Preorder, (b) Inorder, (c) Postorder.

**Pembahasan:**

```
Preorder (Root-Left-Right):
  Kunjungi A
  → Masuk subtree kiri (B)
    Kunjungi B
    → Masuk subtree kiri (D)
      Kunjungi D (daun)
    → Masuk subtree kanan (E)
      Kunjungi E
      → Masuk subtree kiri (G)
        Kunjungi G (daun)
      → Subtree kanan E: kosong
  → Masuk subtree kanan (C)
    Kunjungi C
    → Subtree kiri C: kosong
    → Masuk subtree kanan (F)
      Kunjungi F (daun)

Preorder: A, B, D, E, G, C, F

Inorder (Left-Root-Right):
  Subtree kiri A → B
    Subtree kiri B → D (daun): D
    Root B: B
    Subtree kanan B → E
      Subtree kiri E → G: G
      Root E: E
      Subtree kanan E: kosong
  Root A: A
  Subtree kanan A → C
    Subtree kiri C: kosong
    Root C: C
    Subtree kanan C → F: F

Inorder: D, B, G, E, A, C, F

Postorder (Left-Right-Root):
  Subtree kiri A → B
    Subtree kiri B → D: D
    Subtree kanan B → E
      Subtree kiri E → G: G
      Subtree kanan E: kosong
      Root E: E
    Root B: B
  Subtree kanan A → C
    Subtree kiri C: kosong
    Subtree kanan C → F: F
    Root C: C
  Root A: A

Postorder: D, G, E, B, F, C, A
```

**Jawaban:**  
(a) Preorder: A, B, D, E, G, C, F  
(b) Inorder: D, B, G, E, A, C, F  
(c) Postorder: D, G, E, B, F, C, A

---

### Soal 14 — Rekonstruksi Pohon dari Traversal ★★★

**Tipe:** Uraian

**Soal:**  
Diketahui hasil traversal sebuah pohon biner:
- Preorder: M, K, A, B, L, N, P
- Inorder: A, K, B, M, N, L, P

Gambarkan pohon biner tersebut.

**Pembahasan:**

```
Langkah 1: Dari preorder, elemen pertama = root = M
  Inorder: [A, K, B] M [N, L, P]
  → Subtree kiri M: {A, K, B}
  → Subtree kanan M: {N, L, P}

Langkah 2: Subtree kiri M
  Preorder subtree kiri: K, A, B (urutan di preorder setelah M)
  Root subtree kiri = K
  Inorder: [A] K [B]
  → Anak kiri K = A (daun)
  → Anak kanan K = B (daun)

Langkah 3: Subtree kanan M
  Preorder subtree kanan: L, N, P
  Root subtree kanan = L
  Inorder: [N] L [P]
  → Anak kiri L = N (daun)
  → Anak kanan L = P (daun)

Langkah 4: Gambar pohon
        M
       / \
      K   L
     / \ / \
    A  B N  P

Verifikasi:
  Preorder: M, K, A, B, L, N, P ✓
  Inorder: A, K, B, M, N, L, P ✓
```

**Jawaban:**
```
        M
       / \
      K   L
     / \ / \
    A  B N  P
```

---

### Soal 15 — Level Order Traversal ★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan pohon biner:

```
        10
       /  \
      5    15
     / \     \
    3   7    20
   /
  1
```

Tuliskan urutan kunjungan level order (BFS dari root).

**Pembahasan:**

```
Langkah 1: Level 0 (root): 10
  Queue: [10]
  Output: 10

Langkah 2: Level 1: anak-anak 10 → 5, 15
  Queue: [5, 15]
  Output: 10, 5, 15

Langkah 3: Level 2: anak-anak 5 → 3, 7; anak-anak 15 → 20
  Queue: [3, 7, 20]
  Output: 10, 5, 15, 3, 7, 20

Langkah 4: Level 3: anak-anak 3 → 1; anak-anak 7 → (kosong); anak-anak 20 → (kosong)
  Queue: [1]
  Output: 10, 5, 15, 3, 7, 20, 1
```

**Jawaban:** Level order: 10, 5, 15, 3, 7, 20, 1

---

### Soal 16 — Tinggi dan Kedalaman Pohon ★

**Tipe:** Isian Singkat

**Soal:**  
Pada pohon berikut, tentukan: (a) tinggi pohon, (b) kedalaman simpul F, (c) jumlah daun.

```
        A          ← level 0
       /|\
      B  C  D      ← level 1
     /|     |
    E  F    G      ← level 2
       |
       H           ← level 3
```

**Pembahasan:**

```
Langkah 1: Tinggi pohon = panjang lintasan terpanjang dari root ke daun
  Lintasan terpanjang: A → B → F → H (3 sisi)
  Tinggi pohon = 3

Langkah 2: Kedalaman simpul F
  Kedalaman = panjang lintasan dari root ke F
  Jalur: A → B → F (2 sisi)
  Kedalaman F = 2

Langkah 3: Jumlah daun (simpul tanpa anak)
  E: tidak punya anak → daun
  H: tidak punya anak → daun
  C: tidak punya anak → daun
  G: tidak punya anak → daun
  Jumlah daun = 4
```

**Jawaban:** (a) Tinggi = 3, (b) Kedalaman F = 2, (c) Jumlah daun = 4

---

### Soal 17 — Ekspresi Aritmatika dalam Pohon ★★

**Tipe:** Uraian

**Soal:**  
Pohon ekspresi berikut merepresentasikan sebuah ekspresi aritmatika:

```
          *
         / \
        +   -
       / \ / \
      3  4 8  2
```

Tentukan: (a) notasi infix, (b) notasi prefix, (c) notasi postfix, (d) hasil evaluasi.

**Pembahasan:**

```
Langkah 1: Notasi Infix (Inorder traversal + tanda kurung)
  Subtree kiri *: (3 + 4)
  Root: *
  Subtree kanan *: (8 - 2)
  Infix: (3 + 4) * (8 - 2)

Langkah 2: Notasi Prefix (Preorder traversal)
  Root: *
  Subtree kiri: + 3 4
  Subtree kanan: - 8 2
  Prefix: * + 3 4 - 8 2

Langkah 3: Notasi Postfix (Postorder traversal)
  Subtree kiri: 3 4 +
  Subtree kanan: 8 2 -
  Root: *
  Postfix: 3 4 + 8 2 - *

Langkah 4: Evaluasi
  Subtree kiri: 3 + 4 = 7
  Subtree kanan: 8 - 2 = 6
  Root: 7 * 6 = 42
```

**Jawaban:**  
(a) Infix: (3 + 4) * (8 - 2)  
(b) Prefix: * + 3 4 - 8 2  
(c) Postfix: 3 4 + 8 2 - *  
(d) Hasil: 42

---

### Soal 18 — Pohon Biner Pencarian (BST) ★★

**Tipe:** Uraian

**Soal:**  
Masukkan bilangan-bilangan berikut secara berurutan ke dalam BST kosong: 15, 10, 20, 8, 12, 17, 25, 6

Gambarkan BST yang terbentuk, lalu tuliskan hasil inorder traversal.

**Pembahasan:**

```
Langkah 1: Insert 15 → root
        15

Langkah 2: Insert 10 → 10 < 15, masuk kiri
        15
       /
      10

Langkah 3: Insert 20 → 20 > 15, masuk kanan
        15
       /  \
      10   20

Langkah 4: Insert 8 → 8 < 15, 8 < 10, masuk kiri 10
        15
       /  \
      10   20
     /
    8

Langkah 5: Insert 12 → 12 < 15, 12 > 10, masuk kanan 10
        15
       /  \
      10   20
     / \
    8  12

Langkah 6: Insert 17 → 17 > 15, 17 < 20, masuk kiri 20
        15
       /  \
      10   20
     / \  /
    8  12 17

Langkah 7: Insert 25 → 25 > 15, 25 > 20, masuk kanan 20
        15
       /  \
      10   20
     / \  / \
    8  12 17 25

Langkah 8: Insert 6 → 6 < 15, 6 < 10, 6 < 8, masuk kiri 8
        15
       /  \
      10   20
     / \  / \
    8  12 17 25
   /
  6

Langkah 9: Inorder traversal BST (selalu menghasilkan urutan terurut)
  Inorder: 6, 8, 10, 12, 15, 17, 20, 25
```

**Jawaban:**  
BST terbentuk seperti di atas. Inorder traversal: 6, 8, 10, 12, 15, 17, 20, 25.

---

## Bagian D: Representasi Graf (Matriks dan List Ketetanggaan)

---

### Soal 19 — Matriks Ketetanggaan ★

**Tipe:** Uraian

**Soal:**  
Diberikan graf tak berarah:

```
    1 --- 2
    |   / |
    | /   |
    3 --- 4
```

Sisi: {(1,2), (1,3), (2,3), (2,4), (3,4)}

Tuliskan matriks ketetanggaan (adjacency matrix) untuk graf ini.

**Pembahasan:**

```
Langkah 1: Buat matriks 4×4 (simpul 1, 2, 3, 4)
  M[i][j] = 1 jika ada sisi (i,j), 0 jika tidak
  Karena graf tak berarah, matriks simetris: M[i][j] = M[j][i]

Langkah 2: Isi matriks berdasarkan sisi
  Sisi (1,2): M[1][2] = M[2][1] = 1
  Sisi (1,3): M[1][3] = M[3][1] = 1
  Sisi (2,3): M[2][3] = M[3][2] = 1
  Sisi (2,4): M[2][4] = M[4][2] = 1
  Sisi (3,4): M[3][4] = M[4][3] = 1

Langkah 3: Matriks ketetanggaan
       1  2  3  4
  1 [  0  1  1  0 ]
  2 [  1  0  1  1 ]
  3 [  1  1  0  1 ]
  4 [  0  1  1  0 ]

Langkah 4: Verifikasi
  Jumlah 1 pada baris i = derajat simpul i
  deg(1) = 2 ✓, deg(2) = 3 ✓, deg(3) = 3 ✓, deg(4) = 2 ✓
```

**Jawaban:**
```
     1  2  3  4
1 [  0  1  1  0 ]
2 [  1  0  1  1 ]
3 [  1  1  0  1 ]
4 [  0  1  1  0 ]
```

---

### Soal 20 — List Ketetanggaan ★

**Tipe:** Uraian

**Soal:**  
Konversikan graf pada Soal 19 ke bentuk list ketetanggaan (adjacency list).

**Pembahasan:**

```
Langkah 1: Untuk setiap simpul, tulis semua tetangganya
  Sisi: {(1,2), (1,3), (2,3), (2,4), (3,4)}

Langkah 2: Adjacency list
  1 → [2, 3]
  2 → [1, 3, 4]
  3 → [1, 2, 4]
  4 → [2, 3]

Langkah 3: Verifikasi
  Panjang list simpul i = derajat simpul i
  |list(1)| = 2 = deg(1) ✓
  |list(2)| = 3 = deg(2) ✓
  |list(3)| = 3 = deg(3) ✓
  |list(4)| = 2 = deg(4) ✓
```

**Jawaban:**
```
1 → [2, 3]
2 → [1, 3, 4]
3 → [1, 2, 4]
4 → [2, 3]
```

---

### Soal 21 — Matriks Ketetanggaan Graf Berarah ★★

**Tipe:** Uraian

**Soal:**  
Diberikan graf berarah:

```
  1 → 2
  ↓   ↓
  3 → 4
  ↑       
  |       
  4 (sisi 4→3 juga ada)
```

Sisi berarah: {1→2, 1→3, 2→4, 3→4, 4→3}

Tuliskan matriks ketetanggaan dan tentukan in-degree serta out-degree tiap simpul.

**Pembahasan:**

```
Langkah 1: Buat matriks 4×4
  M[i][j] = 1 jika ada sisi berarah i→j
  (Matriks TIDAK harus simetris untuk graf berarah)

Langkah 2: Isi matriks
  1→2: M[1][2] = 1
  1→3: M[1][3] = 1
  2→4: M[2][4] = 1
  3→4: M[3][4] = 1
  4→3: M[4][3] = 1

Langkah 3: Matriks ketetanggaan
       1  2  3  4
  1 [  0  1  1  0 ]
  2 [  0  0  0  1 ]
  3 [  0  0  0  1 ]
  4 [  0  0  1  0 ]

Langkah 4: Hitung derajat
  Out-degree = jumlah 1 pada baris i
  In-degree = jumlah 1 pada kolom j

  Simpul | In-degree | Out-degree
  -------|-----------|----------
    1    |     0     |     2
    2    |     1     |     1
    3    |     2     |     1
    4    |     2     |     1
```

**Jawaban:**
```
     1  2  3  4
1 [  0  1  1  0 ]
2 [  0  0  0  1 ]
3 [  0  0  0  1 ]
4 [  0  0  1  0 ]
```
In-degree: 1→0, 2→1, 3→2, 4→2. Out-degree: 1→2, 2→1, 3→1, 4→1.

---

### Soal 22 — Konversi Matriks ke Graf ★★

**Tipe:** Uraian

**Soal:**  
Diberikan matriks ketetanggaan berikut untuk graf tak berarah:

```
     A  B  C  D  E
A [  0  1  0  1  1 ]
B [  1  0  1  0  0 ]
C [  0  1  0  1  0 ]
D [  1  0  1  0  1 ]
E [  1  0  0  1  0 ]
```

(a) Gambarkan grafnya.  
(b) Tentukan jumlah sisi.  
(c) Tentukan apakah graf tersebut terhubung.

**Pembahasan:**

```
Langkah 1: Baca sisi dari matriks (hanya segitiga atas karena simetris)
  M[A][B]=1 → sisi (A,B)
  M[A][D]=1 → sisi (A,D)
  M[A][E]=1 → sisi (A,E)
  M[B][C]=1 → sisi (B,C)
  M[C][D]=1 → sisi (C,D)
  M[D][E]=1 → sisi (D,E)

Langkah 2: Gambar graf
      A --- B
     /|     |
    E |     C
     \|     |
      D-----+
  
  Lebih jelas:
  A --- B --- C
  |  \       |
  E --- D ---+

Langkah 3: Jumlah sisi
  = 6 sisi (dari langkah 1)
  Verifikasi: total derajat = 3+2+2+3+2 = 12 = 2×6 ✓

Langkah 4: Cek keterhubungan (BFS dari A)
  Mulai A → kunjungi B, D, E
  Dari B → kunjungi C
  Semua simpul terjangkau → graf TERHUBUNG
```

**Jawaban:**  
(a) Graf dengan sisi: {(A,B), (A,D), (A,E), (B,C), (C,D), (D,E)}  
(b) 6 sisi  
(c) Ya, graf terhubung.

---

### Soal 23 — Matriks Ketetanggaan Berbobot ★★

**Tipe:** Uraian

**Soal:**  
Diberikan graf berbobot:

```
    A --5-- B
    |       |
    3       7
    |       |
    C --2-- D --4-- E
```

Sisi dan bobot: {(A,B,5), (A,C,3), (B,D,7), (C,D,2), (D,E,4)}

Tuliskan matriks ketetanggaan berbobot (gunakan ∞ jika tidak ada sisi).

**Pembahasan:**

```
Langkah 1: Buat matriks 5×5, inisialisasi dengan ∞ (kecuali diagonal = 0)

Langkah 2: Isi berdasarkan bobot sisi
  (A,B): M[A][B] = M[B][A] = 5
  (A,C): M[A][C] = M[C][A] = 3
  (B,D): M[B][D] = M[D][B] = 7
  (C,D): M[C][D] = M[D][C] = 2
  (D,E): M[D][E] = M[E][D] = 4

Langkah 3: Matriks ketetanggaan berbobot
       A    B    C    D    E
  A [  0    5    3    ∞    ∞  ]
  B [  5    0    ∞    7    ∞  ]
  C [  3    ∞    0    2    ∞  ]
  D [  ∞    7    2    0    4  ]
  E [  ∞    ∞    ∞    4    0  ]
```

**Jawaban:**
```
     A    B    C    D    E
A [  0    5    3    ∞    ∞  ]
B [  5    0    ∞    7    ∞  ]
C [  3    ∞    0    2    ∞  ]
D [  ∞    7    2    0    4  ]
E [  ∞    ∞    ∞    4    0  ]
```

---

### Soal 24 — Perbandingan Kompleksitas Representasi ★★

**Tipe:** Pilihan Ganda

**Soal:**  
Sebuah graf memiliki 1000 simpul dan 2000 sisi. Representasi manakah yang lebih hemat memori?

A. Matriks ketetanggaan  
B. List ketetanggaan  
C. Keduanya sama  
D. Tergantung apakah graf berarah atau tidak

**Pembahasan:**

```
Langkah 1: Hitung kebutuhan memori matriks ketetanggaan
  Matriks n×n = n^2 sel
  = 1000 × 1000 = 1.000.000 sel

Langkah 2: Hitung kebutuhan memori list ketetanggaan
  Array n pointer + menyimpan 2m entri (setiap sisi dicatat 2 kali untuk 
  graf tak berarah)
  = 1000 + 2 × 2000 = 5.000 entri (termasuk pointer array)

Langkah 3: Bandingkan
  Matriks: 1.000.000 vs List: ~5.000
  List jauh lebih hemat untuk graf sparse (m << n^2)

Langkah 4: Catatan
  Graf ini sparse karena m = 2000 << n(n-1)/2 = 499.500
  Untuk graf sparse, list ketetanggaan selalu lebih hemat.
```

**Jawaban: B. List ketetanggaan**

---

## Bagian E: Lintasan Euler dan Hamilton

---

### Soal 25 — Lintasan Euler ★★

**Tipe:** Uraian

**Soal:**  
Tentukan apakah graf berikut memiliki lintasan Euler (Euler path) dan/atau sirkuit Euler (Euler circuit):

```
    A --- B
    |   / | \
    |  /  |  C
    | /   | /
    D --- E
```

Sisi: {(A,B), (A,D), (B,D), (B,E), (B,C), (C,E), (D,E)}

**Pembahasan:**

```
Langkah 1: Hitung derajat setiap simpul
  deg(A) = 2  (terhubung ke B, D)
  deg(B) = 4  (terhubung ke A, D, E, C)
  deg(C) = 2  (terhubung ke B, E)
  deg(D) = 3  (terhubung ke A, B, E)
  deg(E) = 3  (terhubung ke B, C, D)

Langkah 2: Periksa syarat Euler
  Sirkuit Euler ada ⟺ graf terhubung DAN semua simpul berderajat genap.
  Lintasan Euler ada ⟺ graf terhubung DAN tepat 2 simpul berderajat ganjil.

Langkah 3: Analisis
  Graf terhubung? Ya (semua simpul bisa dijangkau dari A). ✓
  Simpul berderajat ganjil: D (deg=3) dan E (deg=3) → ada 2 simpul ganjil

Langkah 4: Kesimpulan
  - Sirkuit Euler: TIDAK ADA (ada simpul berderajat ganjil)
  - Lintasan Euler: ADA (tepat 2 simpul berderajat ganjil)
  - Lintasan Euler harus dimulai dari D atau E

Langkah 5: Contoh lintasan Euler (mulai dari D)
  D → A → B → C → E → B → D → E
  Tunggu, mari hitung: sisi yang dilalui harus 7 sisi
  D-A, A-B? Tidak, A-B baru benar... Mari cari ulang:
  
  D → A → B → D → E → C → B → E
  Sisi: (D,A), (A,B), (B,D), (D,E), (E,C), (C,B), (B,E)
  Cek: 7 sisi, semua terpakai. ✓
```

**Jawaban:** Lintasan Euler ADA (mulai dari D atau E), contoh: D-A-B-D-E-C-B-E. Sirkuit Euler TIDAK ADA.

---

### Soal 26 — Sirkuit Euler ★★

**Tipe:** Isian Singkat

**Soal:**  
Diberikan graf:

```
    1 --- 2
   /|     |\
  5 |     | 3
   \|     |/
    4 --- 3... 

Maaf, mari perjelas:
```

```
    1 --- 2 --- 3
    |     |     |
    6 --- 5 --- 4
```

Sisi: {(1,2), (2,3), (3,4), (4,5), (5,6), (6,1), (2,5)}

Apakah graf ini memiliki sirkuit Euler? Jika ya, berikan contohnya.

**Pembahasan:**

```
Langkah 1: Hitung derajat setiap simpul
  deg(1) = 2  (terhubung ke 2, 6)
  deg(2) = 3  (terhubung ke 1, 3, 5)
  deg(3) = 2  (terhubung ke 2, 4)
  deg(4) = 2  (terhubung ke 3, 5)
  deg(5) = 3  (terhubung ke 2, 4, 6)
  deg(6) = 2  (terhubung ke 1, 5)

Langkah 2: Periksa syarat sirkuit Euler
  Syarat: semua simpul berderajat genap DAN graf terhubung
  Simpul berderajat ganjil: 2 (deg=3) dan 5 (deg=3) → ada 2 simpul ganjil
  → Sirkuit Euler TIDAK ADA
  → Tetapi LINTASAN Euler ADA (mulai dari 2 atau 5)

Langkah 3: Contoh lintasan Euler (mulai dari simpul 2)
  2 → 1 → 6 → 5 → 4 → 3 → 2 → 5
  Sisi: (2,1), (1,6), (6,5), (5,4), (4,3), (3,2), (2,5)
  Total 7 sisi, semua terpakai ✓
```

**Jawaban:** Sirkuit Euler TIDAK ADA (simpul 2 dan 5 berderajat ganjil). Lintasan Euler ADA, contoh: 2-1-6-5-4-3-2-5.

---

### Soal 27 — Lintasan Hamilton ★★★

**Tipe:** Uraian

**Soal:**  
Perhatikan graf berikut:

```
    A --- B --- C
    |     |     |
    F --- E --- D
```

Sisi: {(A,B), (B,C), (C,D), (D,E), (E,F), (F,A), (B,E)}

(a) Apakah graf ini memiliki lintasan Hamilton?  
(b) Apakah graf ini memiliki sirkuit Hamilton?

**Pembahasan:**

```
Langkah 1: Definisi
  Lintasan Hamilton = lintasan yang mengunjungi setiap simpul tepat satu kali
  Sirkuit Hamilton = sirkuit yang mengunjungi setiap simpul tepat satu kali 
                     lalu kembali ke awal

Langkah 2: Cek sirkuit Hamilton
  Coba: A → B → C → D → E → F → A
  Sisi yang dipakai: (A,B), (B,C), (C,D), (D,E), (E,F), (F,A)
  Semua sisi ini ada dalam graf ✓
  Semua 6 simpul dikunjungi tepat sekali ✓
  → SIRKUIT HAMILTON ADA!

Langkah 3: Karena sirkuit Hamilton ada, lintasan Hamilton juga ada
  (setiap sirkuit Hamilton jika dihilangkan satu sisi menjadi lintasan Hamilton)
  Contoh lintasan Hamilton: A → B → C → D → E → F
```

**Jawaban:**  
(a) Ya, lintasan Hamilton ada. Contoh: A-B-C-D-E-F.  
(b) Ya, sirkuit Hamilton ada. Contoh: A-B-C-D-E-F-A.

---

## Bagian F: Soal Campuran Gaya OSN

---

### Soal 28 — Pohon Rentang Minimum ★★

**Tipe:** Uraian

**Soal:**  
Diberikan graf berbobot:

```
    A --4-- B --3-- C
    |      /|      |
    2    5  1      6
    |  /    |      |
    D --7-- E --2-- F
```

Sisi dan bobot: {(A,B,4), (A,D,2), (B,C,3), (B,D,5), (B,E,1), (C,F,6), (D,E,7), (E,F,2)}

Tentukan pohon rentang minimum (MST) menggunakan algoritma Kruskal, beserta bobot totalnya.

**Pembahasan:**

```
Langkah 1: Urutkan sisi berdasarkan bobot (ascending)
  (B,E) = 1
  (A,D) = 2
  (E,F) = 2
  (B,C) = 3
  (A,B) = 4
  (B,D) = 5
  (C,F) = 6
  (D,E) = 7

Langkah 2: Pilih sisi satu per satu (jangan membentuk siklus)
  Pilih (B,E) = 1 → Komponen: {B,E}, {A}, {C}, {D}, {F}
  Pilih (A,D) = 2 → Komponen: {A,D}, {B,E}, {C}, {F}
  Pilih (E,F) = 2 → Komponen: {B,E,F}, {A,D}, {C}
  Pilih (B,C) = 3 → Komponen: {B,C,E,F}, {A,D}
  Pilih (A,B) = 4 → Menghubungkan {A,D} dan {B,C,E,F}
    → Komponen: {A,B,C,D,E,F} — semua terhubung!
  
  Jumlah sisi = 5 = n-1 = 6-1 ✓ → MST selesai

Langkah 3: Sisi MST
  {(B,E), (A,D), (E,F), (B,C), (A,B)}
  Bobot total = 1 + 2 + 2 + 3 + 4 = 12

Langkah 4: Gambar MST
    A --4-- B --3-- C
    |       |
    2       1
    |       |
    D       E --2-- F
```

**Jawaban:** MST: {(B,E,1), (A,D,2), (E,F,2), (B,C,3), (A,B,4)}. Bobot total = 12.

---

### Soal 29 — Pewarnaan Graf ★★★

**Tipe:** Uraian

**Soal:**  
Tentukan bilangan kromatik (jumlah warna minimum untuk mewarnai simpul sehingga simpul bertetangga berwarna berbeda) dari graf berikut:

```
    A --- B
    |\   /|
    | \ / |
    |  X  |
    | / \ |
    |/   \|
    C --- D
```

Sisi: {(A,B), (A,C), (A,D), (B,C), (B,D), (C,D)}

**Pembahasan:**

```
Langkah 1: Identifikasi graf
  Setiap pasang simpul terhubung → ini adalah graf lengkap K_4!
  |V| = 4, |E| = C(4,2) = 6 sisi ✓

Langkah 2: Bilangan kromatik graf lengkap
  Untuk K_n, bilangan kromatik χ(K_n) = n
  Karena semua simpul saling bertetangga, setiap simpul harus berwarna 
  berbeda.

Langkah 3: Verifikasi
  χ(K_4) = 4
  Pewarnaan: A=merah, B=biru, C=hijau, D=kuning
  Cek semua pasangan bertetangga:
    (A,B): merah ≠ biru ✓
    (A,C): merah ≠ hijau ✓
    (A,D): merah ≠ kuning ✓
    (B,C): biru ≠ hijau ✓
    (B,D): biru ≠ kuning ✓
    (C,D): hijau ≠ kuning ✓

Langkah 4: Buktikan 3 warna tidak cukup
  Dengan 3 warna, setidaknya 2 simpul harus berwarna sama.
  Tapi semua simpul saling bertetangga, sehingga tidak mungkin.
```

**Jawaban:** Bilangan kromatik = 4 (karena grafnya adalah K_4).

---

### Soal 30 — Konektivitas dan Jembatan ★★★

**Tipe:** Uraian

**Soal:**  
Perhatikan graf berikut:

```
    1 --- 2 --- 3
    |     |
    4 --- 5 --- 6 --- 7
```

Sisi: {(1,2), (1,4), (2,3), (2,5), (4,5), (5,6), (6,7)}

(a) Tentukan sisi mana yang merupakan jembatan (bridge).  
(b) Tentukan simpul mana yang merupakan titik artikulasi (cut vertex).

**Pembahasan:**

```
Langkah 1: Definisi
  Jembatan: sisi yang jika dihapus akan menambah jumlah komponen terhubung
  Titik artikulasi: simpul yang jika dihapus akan menambah jumlah komponen

Langkah 2: Periksa setiap sisi sebagai kandidat jembatan
  Hapus (1,2): sisa sisi terhubung ke 1 hanya (1,4). 
    1→4→5→2→3 masih terhubung ✓. Bukan jembatan.
  Hapus (1,4): 1→2→5→4 masih terhubung ✓. Bukan jembatan.
  Hapus (2,3): 3 terputus dari sisanya → JEMBATAN ✓
  Hapus (2,5): 1→2→3 dan 4→5→6→7 masih terhubung via (1,4)? 
    1-2-3 terhubung. 4-5-6-7 terhubung.
    Apakah ada jalur 1 ke 4? 1→4 ada sisi (1,4). Ya!
    Jadi semua masih terhubung. Bukan jembatan.
  Hapus (4,5): 4 terhubung ke 1, 1→2→5. Masih terhubung. Bukan jembatan.
  Hapus (5,6): 6 dan 7 terputus dari {1,2,3,4,5} → JEMBATAN ✓
  Hapus (6,7): 7 terputus → JEMBATAN ✓

Langkah 3: Jembatan = {(2,3), (5,6), (6,7)}

Langkah 4: Periksa titik artikulasi
  Hapus simpul 1: sisa {2,3,4,5,6,7}. 
    2→3, 2→5, 4→5, 5→6, 6→7. Semua terhubung. Bukan artikulasi.
  Hapus simpul 2: sisa {1,3,4,5,6,7}.
    1→4, 4→5, 5→6, 6→7. Tetapi 3 terisolasi!
    → TITIK ARTIKULASI ✓
  Hapus simpul 3: sisa {1,2,4,5,6,7}. 
    1→2, 1→4, 2→5, 4→5, 5→6, 6→7. Terhubung. Bukan artikulasi.
  Hapus simpul 4: sisa {1,2,3,5,6,7}.
    1→2, 2→3, 2→5, 5→6, 6→7. Terhubung. Bukan artikulasi.
  Hapus simpul 5: sisa {1,2,3,4,6,7}.
    1→2, 1→4, 2→3. Komponen: {1,2,3,4}.
    6→7. Komponen: {6,7}.
    → TITIK ARTIKULASI ✓
  Hapus simpul 6: sisa {1,2,3,4,5,7}.
    1→2, 1→4, 2→3, 2→5, 4→5. Komponen: {1,2,3,4,5}.
    7 terisolasi. Komponen: {7}.
    → TITIK ARTIKULASI ✓
  Hapus simpul 7: sisa semua terhubung. Bukan artikulasi.
```

**Jawaban:**  
(a) Jembatan: (2,3), (5,6), (6,7)  
(b) Titik artikulasi: 2, 5, 6

---

### Soal 31 — Planaritas Graf ★★

**Tipe:** Benar/Salah

**Soal:**  
Tentukan benar atau salah:

1. Graf K_4 adalah graf planar.  
2. Graf K_5 adalah graf planar.  
3. Graf K_{3,3} adalah graf planar.  
4. Setiap pohon adalah graf planar.  
5. Jika sebuah graf planar memiliki 6 simpul dan 4 daerah (region/face), maka graf tersebut memiliki 8 sisi.

**Pembahasan:**

```
Langkah 1: K_4 planar?
  K_4 memiliki 4 simpul dan 6 sisi.
  Syarat planar (Euler formula): n - m + f = 2
  Dapat digambar tanpa sisi berpotongan:
  Gambar segitiga lalu simpul ke-4 di dalam.
  → BENAR

Langkah 2: K_5 planar?
  K_5 memiliki 5 simpul dan 10 sisi.
  Syarat perlu graf planar sederhana: m ≤ 3n - 6
  10 ≤ 3(5) - 6 = 9? TIDAK (10 > 9)
  → SALAH (Teorema Kuratowski: K_5 tidak planar)

Langkah 3: K_{3,3} planar?
  K_{3,3} memiliki 6 simpul dan 9 sisi.
  Syarat graf bipartit planar: m ≤ 2n - 4
  9 ≤ 2(6) - 4 = 8? TIDAK (9 > 8)
  → SALAH (Teorema Kuratowski: K_{3,3} tidak planar)

Langkah 4: Setiap pohon planar?
  Pohon tidak memiliki siklus, sehingga bisa selalu digambar tanpa 
  sisi berpotongan (gambar sebagai hierarki level).
  → BENAR

Langkah 5: Cek rumus Euler
  Rumus Euler untuk graf planar terhubung: n - m + f = 2
  n = 6, f = 4: 6 - m + 4 = 2 → m = 8
  → BENAR
```

**Jawaban:** 1. Benar, 2. Salah, 3. Salah, 4. Benar, 5. Benar

---

### Soal 32 — Soal Cerita Graf Terapan ★★★

**Tipe:** Uraian

**Soal:**  
Suatu kota memiliki 7 pulau yang dihubungkan oleh jembatan-jembatan sebagai berikut:

```
  Pulau A -- Pulau B : 2 jembatan
  Pulau A -- Pulau C : 1 jembatan
  Pulau B -- Pulau C : 1 jembatan
  Pulau B -- Pulau D : 1 jembatan
  Pulau C -- Pulau D : 2 jembatan
  Pulau D -- Pulau E : 1 jembatan
  Pulau E -- Pulau F : 1 jembatan
  Pulau E -- Pulau G : 1 jembatan
  Pulau F -- Pulau G : 1 jembatan
```

Seorang turis ingin berjalan melewati setiap jembatan tepat satu kali.

(a) Modelkan masalah sebagai graf (tentukan simpul, sisi, dan derajat).  
(b) Apakah turis dapat melewati semua jembatan tepat satu kali dan kembali ke titik awal (sirkuit Euler)?  
(c) Apakah turis dapat melewati semua jembatan tepat satu kali tanpa harus kembali ke titik awal (lintasan Euler)?

**Pembahasan:**

```
Langkah 1: Modelkan sebagai multigraf
  Simpul: A, B, C, D, E, F, G (7 pulau)
  Sisi (jembatan): 
    2 sisi antara A-B
    1 sisi A-C
    1 sisi B-C
    1 sisi B-D
    2 sisi C-D
    1 sisi D-E
    1 sisi E-F
    1 sisi E-G
    1 sisi F-G
  Total sisi = 2+1+1+1+2+1+1+1+1 = 11 jembatan

Langkah 2: Hitung derajat setiap simpul
  deg(A) = 2 + 1 = 3       (2 jembatan ke B, 1 ke C)
  deg(B) = 2 + 1 + 1 = 4   (2 ke A, 1 ke C, 1 ke D)
  deg(C) = 1 + 1 + 2 = 4   (1 ke A, 1 ke B, 2 ke D)
  deg(D) = 1 + 2 + 1 = 4   (1 ke B, 2 ke C, 1 ke E)
  deg(E) = 1 + 1 + 1 = 3   (1 ke D, 1 ke F, 1 ke G)
  deg(F) = 1 + 1 = 2       (1 ke E, 1 ke G)
  deg(G) = 1 + 1 = 2       (1 ke E, 1 ke F)

  Verifikasi: jumlah derajat = 3+4+4+4+3+2+2 = 22 = 2 × 11 ✓

Langkah 3: Cek sirkuit Euler
  Syarat: semua simpul berderajat genap
  Simpul berderajat ganjil: A (deg=3) dan E (deg=3) → ada 2 simpul ganjil
  → SIRKUIT EULER TIDAK ADA

Langkah 4: Cek lintasan Euler
  Syarat: graf terhubung DAN tepat 0 atau 2 simpul berderajat ganjil
  Graf terhubung? A-B-D-E-F-G terhubung, A-C terhubung. Ya ✓
  Tepat 2 simpul berderajat ganjil (A dan E) ✓
  → LINTASAN EULER ADA, dimulai dari A atau E

Langkah 5: Konstruksi lintasan Euler (mulai dari A)
  Contoh: A → B → A → C → B → D → C → D → E → F → G → E
  Cek sisi: (A,B), (B,A)←sisi ke-2, (A,C), (C,B), (B,D), (D,C), 
            (C,D)←sisi ke-2, (D,E), (E,F), (F,G), (G,E)
  Total 11 sisi, semua terpakai ✓
```

**Jawaban:**  
(a) Graf dengan 7 simpul (pulau) dan 11 sisi (jembatan). Derajat: A=3, B=4, C=4, D=4, E=3, F=2, G=2.  
(b) Tidak bisa kembali ke titik awal (sirkuit Euler tidak ada karena ada simpul berderajat ganjil).  
(c) Ya, turis dapat melewati semua jembatan tepat satu kali jika memulai dari pulau A atau E (lintasan Euler).

---

## Ringkasan Rumus Penting

| Konsep | Rumus/Syarat |
|--------|-------------|
| Handshaking Lemma | Jumlah derajat = 2 × jumlah sisi |
| Graf Lengkap K_n | Sisi = n(n-1)/2, derajat = n-1 |
| Graf Bipartit K_{m,n} | Sisi = m × n |
| Pohon n simpul | Sisi = n-1, terhubung, tanpa siklus |
| Sirkuit Euler | Graf terhubung, semua simpul berderajat genap |
| Lintasan Euler | Graf terhubung, tepat 0 atau 2 simpul berderajat ganjil |
| Rumus Euler (planar) | n - m + f = 2 |
| Syarat planar | m ≤ 3n - 6 (umum), m ≤ 2n - 4 (bipartit) |
| Bilangan kromatik K_n | χ(K_n) = n |
| Bilangan kromatik C_n | χ = 2 (n genap), χ = 3 (n ganjil) |

---

*Selamat berlatih! Pastikan memahami setiap langkah pembahasan, bukan hanya menghafal jawaban akhir.*
