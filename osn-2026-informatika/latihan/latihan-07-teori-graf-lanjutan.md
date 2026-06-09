# Latihan Bab 07 — Teori Graf Lanjutan: Algoritma dan Pemodelan Masalah

> **Target**: OSK Informatika 2026
> **Jumlah Soal**: 30 soal dengan pembahasan lengkap
> **Cakupan**: Dijkstra, Kruskal MST, Topological Sort, DAG DP, Pemodelan Graf, Campuran Lanjutan

---

## Bagian A: Shortest Path — Dijkstra Trace (Soal 1-5)

### Soal 1

Diberikan graf berarah berbobot dengan 5 simpul:

```
Simpul: {1, 2, 3, 4, 5}
Edge (bobot):
  1->2: 6
  1->3: 2
  2->4: 1
  3->2: 3
  3->4: 7
  3->5: 4
  4->5: 2
  5->4: 1
```

Tentukan jarak terpendek dari simpul 1 ke semua simpul lainnya menggunakan algoritma Dijkstra!

**Pembahasan:**

Inisialisasi: dist = [0, inf, inf, inf, inf]

| Langkah | Kunjungi | dist[1] | dist[2] | dist[3] | dist[4] | dist[5] |
|---------|----------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf |
| 1 | 1 | 0 | 6 | 2 | inf | inf |
| 2 | 3 (dist=2) | 0 | 5 | 2 | 9 | 6 |
| 3 | 2 (dist=5) | 0 | 5 | 2 | 6 | 6 |
| 4 | 5 (dist=6) | 0 | 5 | 2 | 6 | 6 |
| 5 | 4 (dist=6) | 0 | 5 | 2 | 6 | 6 |

**Penjelasan langkah demi langkah:**

- **Langkah 1:** Kunjungi simpul 1 (dist=0). Update tetangga: dist[2] = min(inf, 0+6) = 6, dist[3] = min(inf, 0+2) = 2.
- **Langkah 2:** Kunjungi simpul 3 (dist=2, terkecil di PQ). Update tetangga: dist[2] = min(6, 2+3) = 5 (update!), dist[4] = min(inf, 2+7) = 9, dist[5] = min(inf, 2+4) = 6.
- **Langkah 3:** Kunjungi simpul 2 (dist=5). Update tetangga: dist[4] = min(9, 5+1) = 6 (update!).
- **Langkah 4:** Kunjungi simpul 5 (dist=6). Update tetangga: dist[4] = min(6, 6+1) = 6 (tidak berubah).
- **Langkah 5:** Kunjungi simpul 4 (dist=6). Update tetangga: dist[5] = min(6, 6+2) = 6 (tidak berubah).

**Jawaban:** dist[1]=0, dist[2]=5, dist[3]=2, dist[4]=6, dist[5]=6

---

### Soal 2

Diberikan graf tak berarah berbobot:

```
Simpul: {A, B, C, D, E, F}
Edge (bobot):
  A-B: 4
  A-C: 2
  B-C: 5
  B-D: 10
  C-D: 3
  C-E: 8
  D-E: 4
  D-F: 7
  E-F: 1
```

Jalankan Dijkstra dari simpul A. Tentukan jarak terpendek dari A ke F dan jalur yang dilalui!

**Pembahasan:**

Karena graf tak berarah, setiap edge berlaku dua arah.

| Langkah | Kunjungi | dist[A] | dist[B] | dist[C] | dist[D] | dist[E] | dist[F] |
|---------|----------|---------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf | inf |
| 1 | A | 0 | 4 | 2 | inf | inf | inf |
| 2 | C (dist=2) | 0 | 4 | 2 | 5 | 10 | inf |
| 3 | B (dist=4) | 0 | 4 | 2 | 5 | 10 | inf |
| 4 | D (dist=5) | 0 | 4 | 2 | 5 | 9 | 12 |
| 5 | E (dist=9) | 0 | 4 | 2 | 5 | 9 | 10 |
| 6 | F (dist=10) | 0 | 4 | 2 | 5 | 9 | 10 |

**Penjelasan langkah kunci:**
- **Langkah 2:** Dari C: dist[D] = 2+3 = 5, dist[E] = 2+8 = 10, dist[B] = min(4, 2+5) = 4 (tidak berubah).
- **Langkah 4:** Dari D: dist[E] = min(10, 5+4) = 9 (update!), dist[F] = min(inf, 5+7) = 12.
- **Langkah 5:** Dari E: dist[F] = min(12, 9+1) = 10 (update!).

**Jawaban:** Jarak terpendek A ke F = **10**, jalur: A -> C -> D -> E -> F

---

### Soal 3

Diberikan graf berarah berbobot:

```
Simpul: {1, 2, 3, 4, 5, 6}
Edge (bobot):
  1->2: 2
  1->3: 4
  2->3: 1
  2->4: 7
  3->5: 3
  4->6: 1
  5->4: 2
  5->6: 5
```

Jalankan Dijkstra dari simpul 1. Berapa jarak terpendek dari simpul 1 ke simpul 6?

**Pembahasan:**

| Langkah | Kunjungi | dist[1] | dist[2] | dist[3] | dist[4] | dist[5] | dist[6] |
|---------|----------|---------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf | inf |
| 1 | 1 | 0 | 2 | 4 | inf | inf | inf |
| 2 | 2 (dist=2) | 0 | 2 | 3 | 9 | inf | inf |
| 3 | 3 (dist=3) | 0 | 2 | 3 | 9 | 6 | inf |
| 4 | 5 (dist=6) | 0 | 2 | 3 | 8 | 6 | 11 |
| 5 | 4 (dist=8) | 0 | 2 | 3 | 8 | 6 | 9 |
| 6 | 6 (dist=9) | 0 | 2 | 3 | 8 | 6 | 9 |

**Penjelasan:**
- Langkah 2: Dari 2, dist[3] = min(4, 2+1) = 3 (update!), dist[4] = min(inf, 2+7) = 9.
- Langkah 3: Dari 3, dist[5] = min(inf, 3+3) = 6.
- Langkah 4: Dari 5, dist[4] = min(9, 6+2) = 8 (update!), dist[6] = min(inf, 6+5) = 11.
- Langkah 5: Dari 4, dist[6] = min(11, 8+1) = 9 (update!).

**Jawaban:** Jarak terpendek 1 ke 6 = **9**, jalur: 1 -> 2 -> 3 -> 5 -> 4 -> 6

---

### Soal 4

Perhatikan graf berbobot berikut:

```
Simpul: {S, A, B, C, D, T}
Edge (bobot):
  S->A: 3
  S->B: 5
  A->B: 1
  A->C: 6
  B->C: 2
  B->D: 4
  C->T: 2
  D->T: 3
  C->D: 1
```

Tentukan jarak terpendek dari S ke T!

**Pembahasan:**

| Langkah | Kunjungi | dist[S] | dist[A] | dist[B] | dist[C] | dist[D] | dist[T] |
|---------|----------|---------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf | inf |
| 1 | S | 0 | 3 | 5 | inf | inf | inf |
| 2 | A (dist=3) | 0 | 3 | 4 | 9 | inf | inf |
| 3 | B (dist=4) | 0 | 3 | 4 | 6 | 8 | inf |
| 4 | C (dist=6) | 0 | 3 | 4 | 6 | 7 | 8 |
| 5 | D (dist=7) | 0 | 3 | 4 | 6 | 7 | 8 |
| 6 | T (dist=8) | 0 | 3 | 4 | 6 | 7 | 8 |

**Penjelasan langkah kunci:**
- Langkah 2: Dari A, dist[B] = min(5, 3+1) = 4 (update!), dist[C] = min(inf, 3+6) = 9.
- Langkah 3: Dari B, dist[C] = min(9, 4+2) = 6 (update!), dist[D] = min(inf, 4+4) = 8.
- Langkah 4: Dari C, dist[T] = min(inf, 6+2) = 8, dist[D] = min(8, 6+1) = 7 (update!).
- Langkah 5: Dari D, dist[T] = min(8, 7+3) = 8 (tidak berubah, D->T = 10 > 8).

Tunggu, dist[D] = 7 dan D->T bobot 3, maka 7+3 = 10 > 8, jadi tidak update.

**Jawaban:** Jarak terpendek S ke T = **8**, jalur: S -> A -> B -> C -> T

---

### Soal 5

Diberikan graf berarah berbobot berikut yang merepresentasikan peta jalan antar kota:

```
Simpul: {1, 2, 3, 4, 5, 6, 7}
Edge (bobot):
  1->2: 3
  1->3: 1
  2->4: 3
  3->2: 1
  3->4: 5
  3->5: 2
  4->6: 2
  5->6: 4
  5->7: 3
  6->7: 1
```

Jika kita memulai Dijkstra dari simpul 1, tentukan jarak terpendek ke semua simpul dan jalur terpendek dari simpul 1 ke simpul 7!

**Pembahasan:**

| Langkah | Kunjungi | d[1] | d[2] | d[3] | d[4] | d[5] | d[6] | d[7] |
|---------|----------|------|------|------|------|------|------|------|
| Init | - | 0 | inf | inf | inf | inf | inf | inf |
| 1 | 1 | 0 | 3 | 1 | inf | inf | inf | inf |
| 2 | 3 (d=1) | 0 | 2 | 1 | 6 | 3 | inf | inf |
| 3 | 2 (d=2) | 0 | 2 | 1 | 5 | 3 | inf | inf |
| 4 | 5 (d=3) | 0 | 2 | 1 | 5 | 3 | 7 | 6 |
| 5 | 4 (d=5) | 0 | 2 | 1 | 5 | 3 | 7 | 6 |
| 6 | 7 (d=6) | 0 | 2 | 1 | 5 | 3 | 7 | 6 |
| 7 | 6 (d=7) | 0 | 2 | 1 | 5 | 3 | 7 | 6 |

**Penjelasan langkah kunci:**
- Langkah 2: Dari 3, dist[2] = min(3, 1+1) = 2 (update!), dist[4] = 1+5 = 6, dist[5] = 1+2 = 3.
- Langkah 3: Dari 2, dist[4] = min(6, 2+3) = 5 (update!).
- Langkah 4: Dari 5, dist[6] = 3+4 = 7, dist[7] = 3+3 = 6.
- Langkah 5: Dari 4, dist[6] = min(7, 5+2) = 7 (tidak berubah).

**Jawaban:**
- Jarak: dist = [0, 2, 1, 5, 3, 7, 6]
- Jalur terpendek 1 ke 7: 1 -> 3 -> 5 -> 7 (total bobot = 1+2+3 = 6)

---

## Bagian B: Minimum Spanning Tree — Kruskal Trace (Soal 6-10)

### Soal 6

Diberikan graf tak berarah berbobot dengan 6 simpul:

```
Simpul: {A, B, C, D, E, F}
Edge (bobot):
  A-B: 4
  A-F: 2
  B-C: 6
  B-F: 5
  C-D: 3
  C-F: 1
  D-E: 2
  D-F: 8
  E-F: 7
```

Tentukan MST menggunakan algoritma Kruskal!

**Pembahasan:**

**Langkah 1:** Urutkan edge berdasarkan bobot:
C-F(1), A-F(2), D-E(2), C-D(3), A-B(4), B-F(5), B-C(6), E-F(7), D-F(8)

**Langkah 2:** Proses edge satu per satu:

| No | Edge | Bobot | Aksi | Alasan |
|----|------|-------|------|--------|
| 1 | C-F | 1 | Tambah | C dan F belum terhubung |
| 2 | A-F | 2 | Tambah | A dan {C,F} belum terhubung |
| 3 | D-E | 2 | Tambah | D dan E belum terhubung |
| 4 | C-D | 3 | Tambah | {A,C,F} dan {D,E} belum terhubung |
| 5 | A-B | 4 | Tambah | B dan {A,C,D,E,F} belum terhubung |
| 6 | B-F | 5 | Lewati | B dan F sudah terhubung (via A-F) |

Setelah 5 edge = n-1 = 6-1 = 5, MST selesai.

**MST:** {C-F, A-F, D-E, C-D, A-B}
**Total bobot:** 1 + 2 + 2 + 3 + 4 = **12**

---

### Soal 7

Diberikan graf berikut yang merepresentasikan biaya pemasangan kabel antar gedung:

```
Simpul: {1, 2, 3, 4, 5}
Edge (bobot):
  1-2: 10
  1-3: 6
  1-4: 5
  2-3: 8
  2-4: 3
  3-5: 4
  4-5: 7
```

Cari total biaya minimum untuk menghubungkan semua gedung (MST) menggunakan Kruskal!

**Pembahasan:**

**Urutan edge:** 2-4(3), 3-5(4), 1-4(5), 1-3(6), 4-5(7), 2-3(8), 1-2(10)

| No | Edge | Bobot | Aksi | Komponen setelah aksi |
|----|------|-------|------|----------------------|
| 1 | 2-4 | 3 | Tambah | {2,4}, {1}, {3}, {5} |
| 2 | 3-5 | 4 | Tambah | {2,4}, {1}, {3,5} |
| 3 | 1-4 | 5 | Tambah | {1,2,4}, {3,5} |
| 4 | 1-3 | 6 | Tambah | {1,2,3,4,5} |
| 5 | 4-5 | 7 | Lewati | 4 dan 5 sudah terhubung |

Sudah terhubung setelah 4 edge (n-1 = 4).

**MST:** {2-4, 3-5, 1-4, 1-3}
**Total bobot:** 3 + 4 + 5 + 6 = **18**

---

### Soal 8

Sebuah perusahaan listrik ingin memasang kabel di antara 7 desa dengan biaya berikut:

```
Simpul: {A, B, C, D, E, F, G}
Edge (bobot):
  A-B: 7
  A-D: 5
  B-C: 8
  B-D: 9
  B-E: 7
  C-E: 5
  D-E: 15
  D-F: 6
  E-F: 8
  E-G: 9
  F-G: 11
```

Tentukan edge yang dipilih oleh Kruskal dan total biaya MST!

**Pembahasan:**

**Urutan edge:** A-D(5), C-E(5), D-F(6), A-B(7), B-E(7), B-C(8), E-F(8), B-D(9), E-G(9), F-G(11), D-E(15)

| No | Edge | Bobot | Aksi | Alasan |
|----|------|-------|------|--------|
| 1 | A-D | 5 | Tambah | A dan D belum terhubung |
| 2 | C-E | 5 | Tambah | C dan E belum terhubung |
| 3 | D-F | 6 | Tambah | F dan {A,D} belum terhubung |
| 4 | A-B | 7 | Tambah | B dan {A,D,F} belum terhubung |
| 5 | B-E | 7 | Tambah | {A,B,D,F} dan {C,E} belum terhubung |
| 6 | B-C | 8 | Lewati | B dan C sudah terhubung (via B-E, C-E) |
| 7 | E-F | 8 | Lewati | E dan F sudah terhubung |
| 8 | B-D | 9 | Lewati | Sudah terhubung |
| 9 | E-G | 9 | Tambah | G belum terhubung ke komponen utama |

Selesai! 6 edge = n-1 = 7-1 = 6.

**MST:** {A-D, C-E, D-F, A-B, B-E, E-G}
**Total bobot:** 5 + 5 + 6 + 7 + 7 + 9 = **39**

---

### Soal 9

Diberikan graf lengkap (complete graph) K4 dengan bobot:

```
Simpul: {P, Q, R, S}
Edge (bobot):
  P-Q: 5
  P-R: 8
  P-S: 3
  Q-R: 4
  Q-S: 6
  R-S: 2
```

Tentukan MST dan total bobotnya! Apakah MST-nya unik?

**Pembahasan:**

**Urutan edge:** R-S(2), P-S(3), Q-R(4), P-Q(5), Q-S(6), P-R(8)

| No | Edge | Bobot | Aksi | Alasan |
|----|------|-------|------|--------|
| 1 | R-S | 2 | Tambah | R dan S belum terhubung |
| 2 | P-S | 3 | Tambah | P dan {R,S} belum terhubung |
| 3 | Q-R | 4 | Tambah | Q dan {P,R,S} belum terhubung |

Selesai! 3 edge = n-1 = 4-1 = 3.

**MST:** {R-S, P-S, Q-R}
**Total bobot:** 2 + 3 + 4 = **9**

**Apakah unik?** Ya, MST ini unik karena semua bobot edge berbeda. Jika ada bobot yang sama, MST mungkin tidak unik.

---

### Soal 10

Terdapat 5 server yang harus dihubungkan dalam jaringan. Biaya koneksi langsung:

```
Simpul: {S1, S2, S3, S4, S5}
Edge (bobot):
  S1-S2: 12
  S1-S3: 8
  S1-S4: 15
  S2-S3: 5
  S2-S5: 9
  S3-S4: 7
  S3-S5: 6
  S4-S5: 10
```

Jika anggaran hanya cukup untuk 4 koneksi (menghubungkan semua server), berapa biaya minimum? Gunakan Kruskal!

**Pembahasan:**

**Urutan edge:** S2-S3(5), S3-S5(6), S3-S4(7), S1-S3(8), S2-S5(9), S4-S5(10), S1-S2(12), S1-S4(15)

| No | Edge | Bobot | Aksi | Alasan |
|----|------|-------|------|--------|
| 1 | S2-S3 | 5 | Tambah | S2 dan S3 belum terhubung |
| 2 | S3-S5 | 6 | Tambah | S5 dan {S2,S3} belum terhubung |
| 3 | S3-S4 | 7 | Tambah | S4 dan {S2,S3,S5} belum terhubung |
| 4 | S1-S3 | 8 | Tambah | S1 dan {S2,S3,S4,S5} belum terhubung |

Selesai! 4 edge = n-1 = 5-1 = 4.

**MST:** {S2-S3, S3-S5, S3-S4, S1-S3}
**Total biaya minimum:** 5 + 6 + 7 + 8 = **26**

---

## Bagian C: Topological Sort (Soal 11-15)

### Soal 11

Diberikan DAG berikut yang merepresentasikan prasyarat mata kuliah:

```
Simpul: {A, B, C, D, E, F}
Edge (prasyarat):
  A->C, A->D
  B->D
  C->E
  D->E, D->F
  E->F
```

Tentukan satu urutan topologis yang valid menggunakan algoritma Kahn (BFS)!

**Pembahasan:**

**Hitung in-degree:**
- A: 0
- B: 0
- C: 1 (dari A)
- D: 2 (dari A, B)
- E: 2 (dari C, D)
- F: 2 (dari D, E)

**Proses Kahn's Algorithm:**

| Langkah | Queue | Proses | Update in-degree | Hasil |
|---------|-------|--------|------------------|-------|
| Init | [A, B] | - | - | [] |
| 1 | [B] | A | indeg[C]=0, indeg[D]=1 | [A] |
| 2 | [C] | B | indeg[D]=0 | [A, B] |
| 3 | [D] | C | indeg[E]=1 | [A, B, C] |
| 4 | [] | D | indeg[E]=0, indeg[F]=1 | [A, B, C, D] |
| 5 | [] | E | indeg[F]=0 | [A, B, C, D, E] |
| 6 | [] | F | - | [A, B, C, D, E, F] |

**Jawaban:** Satu urutan topologis yang valid: **A, B, C, D, E, F**

Catatan: Urutan lain yang juga valid: B, A, C, D, E, F atau B, A, D, C, E, F.

---

### Soal 12

Sebuah proyek software memiliki dependensi antar modul sebagai berikut:

```
Simpul: {1, 2, 3, 4, 5, 6, 7}
Edge (dependensi: u->v artinya u harus selesai sebelum v):
  1->2, 1->3
  2->4, 2->5
  3->5, 3->6
  4->7
  5->7
  6->7
```

Berapa banyak urutan kompilasi valid yang berbeda? Tentukan minimal 2 urutan yang valid!

**Pembahasan:**

**In-degree:** 1:0, 2:1, 3:1, 4:1, 5:2, 6:1, 7:3

**Analisis:**
- Hanya simpul 1 yang bisa memulai (in-degree 0).
- Setelah 1, simpul 2 dan 3 bebas (in-degree menjadi 0).
- Pilihan urutan 2 dan 3 menghasilkan variasi.

**Urutan valid 1:** 1, 2, 3, 4, 5, 6, 7
- Setelah 1: {2,3} bebas, pilih 2
- Setelah 2: {3,4} bebas (5 belum, masih butuh 3), pilih 3
- Setelah 3: {4,5,6} bebas, pilih 4
- Setelah 4: {5,6} bebas, pilih 5
- Setelah 5: {6} bebas, pilih 6
- Setelah 6: {7} bebas, pilih 7

**Urutan valid 2:** 1, 3, 2, 6, 5, 4, 7
- Setelah 1: {2,3} bebas, pilih 3
- Setelah 3: {2,6} bebas (5 belum, masih butuh 2), pilih 2
- Setelah 2: {4,5,6} bebas, pilih 6
- Setelah 6: {4,5} bebas, pilih 5
- Setelah 5: {4} bebas, pilih 4
- Setelah 4: {7} bebas, pilih 7

**Jawaban:** Dua urutan valid: **1,2,3,4,5,6,7** dan **1,3,2,6,5,4,7**

---

### Soal 13

Diberikan DAG berikut:

```
Simpul: {1, 2, 3, 4, 5, 6}
Edge: 1->3, 2->3, 2->4, 3->5, 4->5, 4->6, 5->6
```

a) Tentukan topological sort menggunakan metode DFS (catat finish time)!
b) Apakah ada siklus dalam graf ini?

**Pembahasan:**

**a) Metode DFS:**

Mulai DFS dari simpul 1 (unvisited terkecil):
- DFS(1): kunjungi 1 -> DFS(3) -> DFS(5) -> DFS(6): finish 6, finish 5, finish 3, finish 1

Lanjut dari simpul 2 (belum dikunjungi):
- DFS(2): kunjungi 2 -> DFS(4) -> DFS(5) sudah visited, DFS(6) sudah visited: finish 4, finish 2

**Urutan finish:** 6, 5, 3, 1, 4, 2

**Topological sort** (balik urutan finish): **2, 4, 1, 3, 5, 6**

Verifikasi:
- Edge 1->3: 1 muncul sebelum 3 (posisi 3 vs 4) ✓
- Edge 2->3: 2 muncul sebelum 3 (posisi 1 vs 4) ✓
- Edge 2->4: 2 muncul sebelum 4 (posisi 1 vs 2) ✓
- Edge 3->5: 3 muncul sebelum 5 (posisi 4 vs 5) ✓
- Edge 4->5: 4 muncul sebelum 5 (posisi 2 vs 5) ✓
- Edge 4->6: 4 muncul sebelum 6 (posisi 2 vs 6) ✓
- Edge 5->6: 5 muncul sebelum 6 (posisi 5 vs 6) ✓

**b)** Tidak ada siklus. Topological sort berhasil menghasilkan urutan lengkap (6 simpul = n). Jika ada siklus, tidak semua simpul akan masuk ke dalam urutan.

---

### Soal 14

Diberikan daftar prasyarat tugas:
- Tugas B membutuhkan Tugas A
- Tugas C membutuhkan Tugas A
- Tugas D membutuhkan Tugas B dan Tugas C
- Tugas E membutuhkan Tugas C
- Tugas F membutuhkan Tugas D dan Tugas E

Gambarkan DAG-nya dan tentukan apakah urutan pengerjaan **A, C, B, E, D, F** valid!

**Pembahasan:**

**DAG:**
```
A -> B -> D -> F
A -> C -> D
C -> E -> F
```

Edge: A->B, A->C, B->D, C->D, C->E, D->F, E->F

**Verifikasi urutan A, C, B, E, D, F:**
- A->B: A (posisi 1) sebelum B (posisi 3) ✓
- A->C: A (posisi 1) sebelum C (posisi 2) ✓
- B->D: B (posisi 3) sebelum D (posisi 5) ✓
- C->D: C (posisi 2) sebelum D (posisi 5) ✓
- C->E: C (posisi 2) sebelum E (posisi 4) ✓
- D->F: D (posisi 5) sebelum F (posisi 6) ✓
- E->F: E (posisi 4) sebelum F (posisi 6) ✓

**Jawaban:** Ya, urutan **A, C, B, E, D, F** adalah urutan topologis yang valid karena semua edge memenuhi syarat u muncul sebelum v.

---

### Soal 15

Diberikan graf berarah:

```
Simpul: {1, 2, 3, 4, 5}
Edge: 1->2, 2->3, 3->4, 4->2, 4->5
```

Apakah topological sort bisa dilakukan pada graf ini? Jelaskan!

**Pembahasan:**

Perhatikan edge-edge: 2->3, 3->4, 4->2 membentuk siklus: 2 -> 3 -> 4 -> 2.

**Menggunakan Kahn's Algorithm:**
- In-degree: 1:0, 2:2(dari 1 dan 4), 3:1(dari 2), 4:1(dari 3), 5:1(dari 4)
- Queue awal: [1] (hanya simpul 1 yang in-degree 0)
- Proses 1: indeg[2] = 1. Queue = [] (kosong!)
- Tidak ada simpul lain yang in-degree-nya menjadi 0 karena siklus.

Hasil topological sort hanya [1], padahal n = 5.
Karena |result| = 1 < n = 5, berarti **ada siklus**.

**Jawaban:** Topological sort **tidak bisa** dilakukan karena graf ini mengandung siklus (2 -> 3 -> 4 -> 2). Topological sort hanya berlaku untuk DAG (Directed Acyclic Graph).

---

## Bagian D: DAG DP / Path Counting (Soal 16-20)

### Soal 16

Diberikan DAG berikut:

```
Simpul: {1, 2, 3, 4, 5, 6}
Edge: 1->2, 1->3, 2->4, 2->5, 3->4, 3->5, 4->6, 5->6
```

Berapa banyak lintasan berbeda dari simpul 1 ke simpul 6?

**Pembahasan:**

Gunakan DP pada topological order:
- dp[v] = jumlah lintasan dari 1 ke v
- dp[1] = 1 (starting point)

**Topological order:** 1, 2, 3, 4, 5, 6

**Perhitungan:**
- dp[1] = 1
- dp[2] = dp[1] = 1 (dari edge 1->2)
- dp[3] = dp[1] = 1 (dari edge 1->3)
- dp[4] = dp[2] + dp[3] = 1 + 1 = 2 (dari edge 2->4 dan 3->4)
- dp[5] = dp[2] + dp[3] = 1 + 1 = 2 (dari edge 2->5 dan 3->5)
- dp[6] = dp[4] + dp[5] = 2 + 2 = 4 (dari edge 4->6 dan 5->6)

**Jawaban:** Ada **4** lintasan berbeda dari 1 ke 6:
1. 1 -> 2 -> 4 -> 6
2. 1 -> 2 -> 5 -> 6
3. 1 -> 3 -> 4 -> 6
4. 1 -> 3 -> 5 -> 6

---

### Soal 17

Diberikan DAG berbobot:

```
Simpul: {1, 2, 3, 4, 5}
Edge (bobot):
  1->2: 3
  1->3: 2
  2->4: 4
  2->5: 1
  3->4: 5
  3->5: 6
  4->5: 2
```

Tentukan lintasan terpanjang dari simpul 1 ke simpul 5!

**Pembahasan:**

Gunakan DAG DP untuk longest path.
- dp[v] = panjang lintasan terpanjang dari 1 ke v
- dp[1] = 0

**Topological order:** 1, 2, 3, 4, 5

**Perhitungan:**
- dp[1] = 0
- dp[2] = dp[1] + 3 = 3 (dari 1->2)
- dp[3] = dp[1] + 2 = 2 (dari 1->3)
- dp[4] = max(dp[2]+4, dp[3]+5) = max(7, 7) = 7
- dp[5] = max(dp[2]+1, dp[3]+6, dp[4]+2) = max(4, 8, 9) = 9

**Jawaban:** Lintasan terpanjang dari 1 ke 5 = **9**, jalur: 1 -> 3 -> 4 -> 5 (bobot: 2+5+2=9)

Atau bisa juga: 1 -> 2 -> 4 -> 5 (bobot: 3+4+2=9)

---

### Soal 18

Pada grid 4x4 (baris 0-3, kolom 0-3), kita hanya boleh bergerak ke kanan atau ke bawah. Berapa banyak lintasan berbeda dari (0,0) ke (3,3)?

**Pembahasan:**

Gunakan Grid DP:
- dp[i][j] = jumlah lintasan dari (0,0) ke (i,j)
- dp[0][0] = 1
- dp[i][j] = dp[i-1][j] + dp[i][j-1]

**Tabel DP:**

```
     j=0  j=1  j=2  j=3
i=0:  1    1    1    1
i=1:  1    2    3    4
i=2:  1    3    6   10
i=3:  1    4   10   20
```

**Perhitungan detail baris per baris:**
- Baris 0: semua = 1 (hanya bisa dari kiri)
- Kolom 0: semua = 1 (hanya bisa dari atas)
- dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 = 2
- dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3
- dp[1][3] = dp[0][3] + dp[1][2] = 1 + 3 = 4
- dp[2][1] = dp[1][1] + dp[2][0] = 2 + 1 = 3
- dp[2][2] = dp[1][2] + dp[2][1] = 3 + 3 = 6
- dp[2][3] = dp[1][3] + dp[2][2] = 4 + 6 = 10
- dp[3][1] = dp[2][1] + dp[3][0] = 3 + 1 = 4
- dp[3][2] = dp[2][2] + dp[3][1] = 6 + 4 = 10
- dp[3][3] = dp[2][3] + dp[3][2] = 10 + 10 = 20

**Jawaban:** Ada **20** lintasan berbeda.

Catatan: Ini juga bisa dihitung dengan rumus kombinatorik C(6,3) = 20, karena kita perlu tepat 3 langkah kanan dan 3 langkah bawah.

---

### Soal 19

Diberikan DAG berikut:

```
Simpul: {S, A, B, C, D, T}
Edge (bobot):
  S->A: 5
  S->B: 3
  A->C: 2
  A->D: 4
  B->C: 6
  B->D: 1
  C->T: 3
  D->T: 7
```

Tentukan:
a) Jumlah lintasan berbeda dari S ke T
b) Lintasan terpendek dari S ke T (jarak minimum)
c) Lintasan terpanjang dari S ke T (jarak maksimum)

**Pembahasan:**

**Topological order:** S, A, B, C, D, T (atau S, B, A, C, D, T)

**a) Jumlah lintasan:**
- dp_count[S] = 1
- dp_count[A] = dp_count[S] = 1
- dp_count[B] = dp_count[S] = 1
- dp_count[C] = dp_count[A] + dp_count[B] = 1 + 1 = 2
- dp_count[D] = dp_count[A] + dp_count[B] = 1 + 1 = 2
- dp_count[T] = dp_count[C] + dp_count[D] = 2 + 2 = 4

Jawaban: **4 lintasan**

**b) Lintasan terpendek:**
- dp_min[S] = 0
- dp_min[A] = 0 + 5 = 5
- dp_min[B] = 0 + 3 = 3
- dp_min[C] = min(5+2, 3+6) = min(7, 9) = 7
- dp_min[D] = min(5+4, 3+1) = min(9, 4) = 4
- dp_min[T] = min(7+3, 4+7) = min(10, 11) = 10

Jawaban: Jarak minimum = **10**, jalur: S -> A -> C -> T

**c) Lintasan terpanjang:**
- dp_max[S] = 0
- dp_max[A] = 5
- dp_max[B] = 3
- dp_max[C] = max(5+2, 3+6) = max(7, 9) = 9
- dp_max[D] = max(5+4, 3+1) = max(9, 4) = 9
- dp_max[T] = max(9+3, 9+7) = max(12, 16) = 16

Jawaban: Jarak maksimum = **16**, jalur: S -> A -> D -> T (5+4+7=16)

---

### Soal 20

Pada grid 3x4 berikut, sel bertanda 'X' adalah obstacle yang tidak bisa dilewati. Bergerak hanya ke kanan atau bawah.

```
Grid:
. . . .
. X . .
. . X .
```

Berapa banyak lintasan dari pojok kiri atas (0,0) ke pojok kanan bawah (2,3)?

**Pembahasan:**

Gunakan Grid DP dengan obstacle:
- dp[i][j] = 0 jika sel (i,j) adalah obstacle
- dp[i][j] = dp[i-1][j] + dp[i][j-1] untuk sel normal

**Identifikasi obstacle:** (1,1) dan (2,2) adalah 'X'

**Tabel DP:**

```
     j=0  j=1  j=2  j=3
i=0:  1    1    1    1
i=1:  1    0    1    2
i=2:  1    1    0    2
```

**Perhitungan detail:**
- Baris 0: dp[0][0]=1, dp[0][1]=1, dp[0][2]=1, dp[0][3]=1
- dp[1][0] = dp[0][0] = 1
- dp[1][1] = 0 (obstacle!)
- dp[1][2] = dp[0][2] + dp[1][1] = 1 + 0 = 1
- dp[1][3] = dp[0][3] + dp[1][2] = 1 + 1 = 2
- dp[2][0] = dp[1][0] = 1
- dp[2][1] = dp[1][1] + dp[2][0] = 0 + 1 = 1
- dp[2][2] = 0 (obstacle!)
- dp[2][3] = dp[1][3] + dp[2][2] = 2 + 0 = 2

**Jawaban:** Ada **2** lintasan valid dari (0,0) ke (2,3).

Lintasan tersebut:
1. (0,0)->(0,1)->(0,2)->(0,3)->(1,3)->(2,3)
2. (0,0)->(0,1)->(0,2)->(1,2)->(1,3)->(2,3)

---

## Bagian E: Pemodelan Graf / Soal Cerita ke Graf (Soal 21-25)

### Soal 21

Lima siswa (A, B, C, D, E) mengikuti lomba estafet. Aturan pergantian:
- A hanya bisa memberikan tongkat ke B atau C
- B hanya bisa memberikan tongkat ke D
- C bisa memberikan ke D atau E
- D bisa memberikan ke E

Jika estafet dimulai dari A dan berakhir di E, berapa banyak urutan estafet yang valid?

**Pembahasan:**

**Model graf:**
- Simpul = siswa
- Edge berarah = aturan pemberian tongkat

```
A -> B -> D -> E
A -> C -> D -> E
      C -> E
```

Edge: A->B, A->C, B->D, C->D, C->E, D->E

Ini adalah DAG! Gunakan DAG DP untuk menghitung lintasan dari A ke E.

**Topological order:** A, B, C, D, E

**DAG DP (jumlah lintasan):**
- dp[A] = 1
- dp[B] = dp[A] = 1
- dp[C] = dp[A] = 1
- dp[D] = dp[B] + dp[C] = 1 + 1 = 2
- dp[E] = dp[C] + dp[D] = 1 + 2 = 3

**Jawaban:** Ada **3** urutan estafet yang valid:
1. A -> B -> D -> E
2. A -> C -> D -> E
3. A -> C -> E

---

### Soal 22

Di sebuah kota terdapat 6 persimpangan (1-6) dan jalan satu arah berikut:
- Dari 1: ke 2 (jarak 3 km), ke 3 (jarak 5 km)
- Dari 2: ke 4 (jarak 2 km)
- Dari 3: ke 2 (jarak 1 km), ke 5 (jarak 4 km)
- Dari 4: ke 6 (jarak 6 km)
- Dari 5: ke 4 (jarak 2 km), ke 6 (jarak 3 km)

Seorang kurir harus mengantar paket dari persimpangan 1 ke persimpangan 6. Berapa jarak minimum yang ditempuh?

**Pembahasan:**

**Model graf:**
- Simpul = persimpangan
- Edge berarah berbobot = jalan satu arah dengan jarak

**Graf:**
```
1->2(3), 1->3(5), 2->4(2), 3->2(1), 3->5(4), 4->6(6), 5->4(2), 5->6(3)
```

Ini adalah DAG (tidak ada siklus). Gunakan DAG DP atau Dijkstra.

**Topological order:** 1, 3, 2, 5, 4, 6

**DAG DP (jarak terpendek):**
- dp[1] = 0
- dp[3] = dp[1] + 5 = 5
- dp[2] = min(dp[1]+3, dp[3]+1) = min(3, 6) = 3
- dp[5] = dp[3] + 4 = 9
- dp[4] = min(dp[2]+2, dp[5]+2) = min(5, 11) = 5
- dp[6] = min(dp[4]+6, dp[5]+3) = min(11, 12) = 11

**Jawaban:** Jarak minimum = **11 km**, jalur: 1 -> 2 -> 4 -> 6 (3+2+6=11)

---

### Soal 23

Sebuah perusahaan memiliki 6 proyek yang harus diselesaikan. Dependensi antar proyek:
- Proyek B bergantung pada Proyek A (A harus selesai dulu)
- Proyek C bergantung pada Proyek A
- Proyek D bergantung pada Proyek B dan C
- Proyek E bergantung pada Proyek C
- Proyek F bergantung pada Proyek D dan E

Waktu pengerjaan: A=2 hari, B=3 hari, C=1 hari, D=4 hari, E=2 hari, F=1 hari.

Berapa waktu minimum untuk menyelesaikan semua proyek (asumsi proyek tanpa dependensi bisa dikerjakan paralel)?

**Pembahasan:**

**Model graf:** DAG dengan simpul = proyek, edge = dependensi.

Ini adalah masalah **Critical Path** (lintasan kritis) = lintasan terpanjang dalam DAG.

**DAG:**
```
A->B, A->C, B->D, C->D, C->E, D->F, E->F
```

**DP lintasan terpanjang (waktu selesai paling cepat):**
- finish[v] = waktu paling cepat proyek v selesai
- finish[v] = max(finish[u] untuk semua prasyarat u) + waktu[v]

**Perhitungan:**
- finish[A] = 0 + 2 = 2
- finish[B] = finish[A] + 3 = 2 + 3 = 5
- finish[C] = finish[A] + 1 = 2 + 1 = 3
- finish[D] = max(finish[B], finish[C]) + 4 = max(5, 3) + 4 = 5 + 4 = 9
- finish[E] = finish[C] + 2 = 3 + 2 = 5
- finish[F] = max(finish[D], finish[E]) + 1 = max(9, 5) + 1 = 9 + 1 = 10

**Jawaban:** Waktu minimum = **10 hari**

Lintasan kritis: A -> B -> D -> F (2 + 3 + 4 + 1 = 10)

---

### Soal 24

Terdapat 4 pulau (A, B, C, D) yang dihubungkan oleh kapal feri. Biaya tiket:
- A ke B: 50 ribu
- A ke C: 80 ribu
- B ke C: 20 ribu
- B ke D: 60 ribu
- C ke D: 30 ribu

Semua rute bisa ditempuh dua arah dengan biaya sama. Seseorang ingin pergi dari pulau A ke pulau D dengan biaya minimum. Tentukan rute dan biayanya!

**Pembahasan:**

**Model graf:**
- Simpul = pulau
- Edge tak berarah berbobot = rute feri dengan biaya

```
A-B(50), A-C(80), B-C(20), B-D(60), C-D(30)
```

**Dijkstra dari A:**

| Langkah | Kunjungi | dist[A] | dist[B] | dist[C] | dist[D] |
|---------|----------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf |
| 1 | A | 0 | 50 | 80 | inf |
| 2 | B (dist=50) | 0 | 50 | 70 | 110 |
| 3 | C (dist=70) | 0 | 50 | 70 | 100 |
| 4 | D (dist=100) | 0 | 50 | 70 | 100 |

**Penjelasan:**
- Langkah 2: Dari B, dist[C] = min(80, 50+20) = 70 (update!), dist[D] = min(inf, 50+60) = 110.
- Langkah 3: Dari C, dist[D] = min(110, 70+30) = 100 (update!).

**Jawaban:** Biaya minimum = **100 ribu rupiah**, rute: A -> B -> C -> D (50+20+30=100)

---

### Soal 25

Sebuah game memiliki 5 level. Dari setiap level, pemain bisa lompat ke beberapa level lain:
- Level 1: bisa ke level 2 atau level 3
- Level 2: bisa ke level 3 atau level 4
- Level 3: bisa ke level 4 atau level 5
- Level 4: bisa ke level 5

Setiap kali pemain melewati sebuah level, dia mendapatkan poin:
- Level 1: 0 poin (start)
- Level 2: 10 poin
- Level 3: 5 poin
- Level 4: 8 poin
- Level 5: 3 poin (finish)

Tentukan:
a) Berapa banyak cara berbeda untuk menyelesaikan game (dari level 1 ke level 5)?
b) Berapa poin maksimum yang bisa dikumpulkan?

**Pembahasan:**

**Model graf:** DAG dengan simpul = level, edge = lompatan yang diizinkan.

Edge: 1->2, 1->3, 2->3, 2->4, 3->4, 3->5, 4->5

Poin simpul: p[1]=0, p[2]=10, p[3]=5, p[4]=8, p[5]=3

**a) Jumlah lintasan:**
- dp_count[1] = 1
- dp_count[2] = dp_count[1] = 1
- dp_count[3] = dp_count[1] + dp_count[2] = 1 + 1 = 2
- dp_count[4] = dp_count[2] + dp_count[3] = 1 + 2 = 3
- dp_count[5] = dp_count[3] + dp_count[4] = 2 + 3 = 5

Jawaban: **5 cara**

**b) Poin maksimum:**

dp_max[v] = total poin maksimum dari level 1 sampai level v.

- dp_max[1] = 0
- dp_max[2] = dp_max[1] + p[2] = 0 + 10 = 10
- dp_max[3] = max(dp_max[1]+p[3], dp_max[2]+p[3]) = max(5, 15) = 15
- dp_max[4] = max(dp_max[2]+p[4], dp_max[3]+p[4]) = max(18, 23) = 23
- dp_max[5] = max(dp_max[3]+p[5], dp_max[4]+p[5]) = max(18, 26) = 26

Jawaban: Poin maksimum = **26**, jalur: 1 -> 2 -> 3 -> 4 -> 5 (0+10+5+8+3=26)

---

## Bagian F: Soal Campuran Lanjutan (Soal 26-30)

### Soal 26

Diberikan graf berbobot berikut:

```
Simpul: {1, 2, 3, 4, 5, 6}
Edge (bobot):
  1-2: 3
  1-3: 5
  2-3: 2
  2-4: 6
  3-4: 4
  3-5: 7
  4-5: 1
  4-6: 8
  5-6: 3
```

a) Tentukan MST menggunakan Kruskal!
b) Tentukan jarak terpendek dari simpul 1 ke simpul 6 menggunakan Dijkstra!
c) Apakah semua edge MST selalu merupakan bagian dari lintasan terpendek? Berikan penjelasan!

**Pembahasan:**

**a) MST (Kruskal):**

Urutan edge: 4-5(1), 2-3(2), 1-2(3), 5-6(3), 3-4(4), 1-3(5), 2-4(6), 3-5(7), 4-6(8)

| No | Edge | Bobot | Aksi |
|----|------|-------|------|
| 1 | 4-5 | 1 | Tambah |
| 2 | 2-3 | 2 | Tambah |
| 3 | 1-2 | 3 | Tambah |
| 4 | 5-6 | 3 | Tambah |
| 5 | 3-4 | 4 | Tambah |

MST: {4-5, 2-3, 1-2, 5-6, 3-4}, total = 1+2+3+3+4 = **13**

**b) Dijkstra dari simpul 1:**

| Langkah | Kunjungi | d[1] | d[2] | d[3] | d[4] | d[5] | d[6] |
|---------|----------|------|------|------|------|------|------|
| Init | - | 0 | inf | inf | inf | inf | inf |
| 1 | 1 | 0 | 3 | 5 | inf | inf | inf |
| 2 | 2 (d=3) | 0 | 3 | 5 | 9 | inf | inf |
| 3 | 3 (d=5) | 0 | 3 | 5 | 9 | 12 | inf |
| 4 | 4 (d=9) | 0 | 3 | 5 | 9 | 10 | 17 |
| 5 | 5 (d=10) | 0 | 3 | 5 | 9 | 10 | 13 |
| 6 | 6 (d=13) | 0 | 3 | 5 | 9 | 10 | 13 |

Langkah 2: dist[3] = min(5, 3+2) = 5 (tidak berubah), dist[4] = 3+6 = 9.
Langkah 3: dist[4] = min(9, 5+4) = 9 (tidak berubah), dist[5] = 5+7 = 12.
Langkah 4: dist[5] = min(12, 9+1) = 10 (update!), dist[6] = 9+8 = 17.
Langkah 5: dist[6] = min(17, 10+3) = 13 (update!).

Jarak terpendek 1 ke 6 = **13**, jalur: 1 -> 2 -> ... -> 4 -> 5 -> 6

Jalur lengkap: 1->2 (3), 2->... kita perlu trace parent.
- dist[6] = 13 via 5 (10+3)
- dist[5] = 10 via 4 (9+1)
- dist[4] = 9 via 2 (3+6)
- dist[2] = 3 via 1

Jalur: 1 -> 2 -> 4 -> 5 -> 6 (3+6+1+3=13)

Atau alternatif: 1 -> 3 -> 4 -> 5 -> 6 (5+4+1+3=13) juga valid.

**c)** Tidak selalu! Edge MST dipilih untuk meminimalkan **total bobot pohon**, bukan untuk membentuk lintasan terpendek antar pasangan simpul tertentu. Contoh: edge 3-4(4) ada di MST, tetapi lintasan terpendek 1->6 tidak perlu melewati edge tersebut secara langsung (bisa lewat 1->2->4 yang total 9, bukan 1->3->4 yang total 9 juga).

---

### Soal 27

Sebuah perusahaan konstruksi harus membangun jembatan untuk menghubungkan 5 pulau. Biaya pembangunan jembatan:

```
P1-P2: 15 M
P1-P3: 20 M
P2-P3: 10 M
P2-P4: 25 M
P3-P4: 12 M
P3-P5: 18 M
P4-P5: 8 M
```

Setelah semua pulau terhubung (MST), perusahaan ingin menambahkan tepat satu jembatan lagi untuk membuat jalur alternatif. Jembatan tambahan mana yang sebaiknya dibangun jika ingin meminimalkan diameter jaringan (jarak terpendek terpanjang antar dua pulau)?

**Pembahasan:**

**Langkah 1: Cari MST dengan Kruskal**

Urutan edge: P4-P5(8), P2-P3(10), P3-P4(12), P1-P2(15), P3-P5(18), P1-P3(20), P2-P4(25)

| No | Edge | Bobot | Aksi |
|----|------|-------|------|
| 1 | P4-P5 | 8 | Tambah |
| 2 | P2-P3 | 10 | Tambah |
| 3 | P3-P4 | 12 | Tambah |
| 4 | P1-P2 | 15 | Tambah |

MST: {P4-P5, P2-P3, P3-P4, P1-P2}, total = 45M

Bentuk MST: P1-P2-P3-P4-P5 (jalur lurus)

**Langkah 2: Hitung diameter MST**

Jarak terpanjang di MST (antar semua pasang):
- P1 ke P5: 15+10+12+8 = 45 (diameter saat ini)

**Langkah 3: Evaluasi penambahan edge**

Edge yang belum di MST: P1-P3(20), P3-P5(18), P2-P4(25)

Jika tambah P1-P3(20):
- P1 ke P5: min(45, 20+12+8) = min(45, 40) = 40
- Diameter baru: 40

Jika tambah P3-P5(18):
- P1 ke P5: min(45, 15+10+18) = min(45, 43) = 43
- Diameter baru: 43

Jika tambah P2-P4(25):
- P1 ke P5: min(45, 15+25+8) = min(45, 48) = 45 (tidak membantu)
- Diameter tetap: 45

**Jawaban:** Tambahkan jembatan **P1-P3** (biaya 20M), yang mengurangi diameter dari 45 menjadi **40**.

---

### Soal 28

Diberikan graf berarah berikut:

```
Simpul: {1, 2, 3, 4, 5, 6}
Edge: 1->2, 1->4, 2->3, 3->6, 4->2, 4->5, 5->3, 5->6
```

a) Tentukan semua topological sort yang valid jika dimulai dari simpul dengan in-degree terkecil!
b) Berapa jumlah lintasan dari simpul 1 ke simpul 6?
c) Jika setiap edge berbobot 1, berapa jarak terpendek dari 1 ke 6?

**Pembahasan:**

**In-degree:** 1:0, 2:2(dari 1,4), 3:2(dari 2,5), 4:1(dari 1), 5:1(dari 4), 6:2(dari 3,5)

**a) Topological sort (Kahn's):**
- Start: queue = [1] (in-degree 0)
- Proses 1: indeg[2]=1, indeg[4]=0. Queue = [4]
- Proses 4: indeg[2]=0, indeg[5]=0. Queue = [2,5] atau [5,2]

Cabang 1: proses 2 dulu
- Proses 2: indeg[3]=1. Queue = [5]
- Proses 5: indeg[3]=0, indeg[6]=1. Queue = [3]
- Proses 3: indeg[6]=0. Queue = [6]
- Proses 6. Selesai.
- Urutan: 1, 4, 2, 5, 3, 6

Cabang 2: proses 5 dulu
- Proses 5: indeg[3]=1, indeg[6]=1. Queue = [2]
- Proses 2: indeg[3]=0. Queue = [3]
- Proses 3: indeg[6]=0. Queue = [6]
- Proses 6. Selesai.
- Urutan: 1, 4, 5, 2, 3, 6

Jawaban: Dua topological sort valid: **1,4,2,5,3,6** dan **1,4,5,2,3,6**

**b) Jumlah lintasan 1 ke 6:**
- dp[1] = 1
- dp[4] = dp[1] = 1
- dp[2] = dp[1] + dp[4] = 1 + 1 = 2
- dp[5] = dp[4] = 1
- dp[3] = dp[2] + dp[5] = 2 + 1 = 3
- dp[6] = dp[3] + dp[5] = 3 + 1 = 4

Jawaban: **4 lintasan**

Enumerasi: 1->2->3->6, 1->4->2->3->6, 1->4->5->3->6, 1->4->5->6

**c) Jarak terpendek (semua bobot 1) menggunakan BFS:**
- Dari 1: bisa ke 2 (jarak 1) dan 4 (jarak 1)
- Dari 2: bisa ke 3 (jarak 2)
- Dari 4: bisa ke 2 (sudah), 5 (jarak 2)
- Dari 3: bisa ke 6 (jarak 3)
- Dari 5: bisa ke 3 (sudah), 6 (jarak 3)

Jawaban: Jarak terpendek = **3**, jalur: 1->2->3->6 atau 1->4->5->6

---

### Soal 29

Pada turnamen round-robin, 5 tim (A,B,C,D,E) bertanding. Hasil pertandingan (panah menunjuk pemenang):
- A mengalahkan B, C
- B mengalahkan C, D
- C mengalahkan D, E
- D mengalahkan E, A
- E mengalahkan A, B

a) Gambarkan graf berarah (edge dari kalah ke menang).
b) Apakah graf ini DAG? Mengapa?
c) Bisakah kita mengurutkan tim dari terlemah ke terkuat secara unik?

**Pembahasan:**

**a) Graf berarah (kalah -> menang):**
```
B->A, C->A, C->B, D->B, D->C, E->C, E->D, A->D, A->E, B->E
```

**b)** Tidak, graf ini **bukan DAG** karena mengandung siklus.

Contoh siklus: A->D->... mari kita cari:
- A mengalahkan B (B->A): edge B->A
- D mengalahkan A (A->D): edge A->D
- B mengalahkan D (D->B): edge D->B

Siklus: A -> D -> B -> A (jika kita ikuti edge "kalah ke menang": A kalah dari D, D kalah dari B, B kalah dari A)

Atau lebih jelas: edge A->D, D->B, B->A membentuk siklus.

**c)** Tidak bisa! Karena graf mengandung siklus, topological sort tidak mungkin dilakukan. Ini berarti tidak ada urutan total dari terlemah ke terkuat yang konsisten dengan semua hasil pertandingan.

Dalam turnamen round-robin, hal ini sering terjadi (disebut "intransitivity"). Untuk menentukan peringkat, biasanya digunakan kriteria tambahan seperti jumlah kemenangan:
- A: 2 menang, 2 kalah
- B: 2 menang, 2 kalah
- C: 2 menang, 2 kalah
- D: 2 menang, 2 kalah
- E: 2 menang, 2 kalah

Semua tim memiliki rekor yang sama (2-2), sehingga memang tidak ada peringkat unik.

---

### Soal 30

Sebuah labirin berbentuk grid 5x5. Titik start di (0,0) dan tujuan di (4,4). Sel '#' tidak bisa dilewati. Gerakan yang diizinkan: atas, bawah, kiri, kanan.

```
Grid (baris 0-4, kolom 0-4):
. . # . .
. # . . .
. . . # .
# . # . .
. . . . .
```

Tentukan jarak terpendek (jumlah langkah minimum) dari (0,0) ke (4,4) menggunakan BFS!

**Pembahasan:**

**Identifikasi obstacle:** (0,2), (1,1), (2,3), (3,0), (3,2) adalah '#'

**BFS dari (0,0):**

```
Langkah 0: (0,0)
Langkah 1: (0,1), (1,0)
Langkah 2: (2,0), (2,1)  [dari (1,0); (0,1) tidak bisa ke (0,2)=#, (1,1)=#]
Langkah 3: (2,2), (3,1)  [dari (2,1); (2,0) tidak bisa ke (3,0)=#]
Langkah 4: (1,2), (4,1)  [dari (2,2) ke (1,2); dari (3,1) ke (4,1)]
Langkah 5: (1,3), (4,0), (4,2)  [dari (1,2) ke (1,3); dari (4,1) ke (4,0),(4,2)]
Langkah 6: (0,3), (1,4), (4,3)  [dari (1,3) ke (0,3),(1,4); dari (4,2) ke (4,3)]
Langkah 7: (0,4), (2,4), (4,4)  [dari (0,3) ke (0,4); dari (1,4) ke (2,4); dari (4,3) ke (4,4)]
```

Tunggu, saya perlu lebih teliti. Mari buat tabel jarak BFS:

```
Jarak BFS:
     j=0  j=1  j=2  j=3  j=4
i=0:  0    1    #    ?    ?
i=1:  1    #    ?    ?    ?
i=2:  2    3    4    #    ?
i=3:  #    4    #    ?    ?
i=4:  ?    5    ?    ?    ?
```

Mari ulang lebih hati-hati:

**Queue BFS (baris, kolom, jarak):**

| Jarak | Sel yang dikunjungi |
|-------|-------------------|
| 0 | (0,0) |
| 1 | (0,1), (1,0) |
| 2 | (2,0) |
| 3 | (2,1) |
| 4 | (2,2), (3,1) |
| 5 | (1,2), (4,1) |
| 6 | (1,3), (4,0), (4,2) |
| 7 | (0,3), (1,4), (4,3) |
| 8 | (0,4), (2,4), (3,3), (4,4) |

Verifikasi detail langkah demi langkah:
- (0,0) dist=0. Tetangga valid: (0,1) dan (1,0)
- (0,1) dist=1. Tetangga valid: (0,0)[visited]. (0,2)=wall. (1,1)=wall. Tidak ada baru.
- (1,0) dist=1. Tetangga valid: (0,0)[visited], (2,0).
- (2,0) dist=2. Tetangga valid: (1,0)[visited], (3,0)=wall, (2,1).
- (2,1) dist=3. Tetangga valid: (2,0)[visited], (1,1)=wall, (3,1), (2,2).
- (2,2) dist=4. Tetangga valid: (2,1)[visited], (1,2), (2,3)=wall, (3,2)=wall.
- (3,1) dist=4. Tetangga valid: (2,1)[visited], (3,0)=wall, (3,2)=wall, (4,1).
- (1,2) dist=5. Tetangga valid: (0,2)=wall, (2,2)[visited], (1,1)=wall, (1,3).
- (4,1) dist=5. Tetangga valid: (3,1)[visited], (4,0), (4,2).
- (1,3) dist=6. Tetangga valid: (0,3), (2,3)=wall, (1,2)[visited], (1,4).
- (4,0) dist=6. Tetangga valid: (3,0)=wall, (4,1)[visited].
- (4,2) dist=6. Tetangga valid: (3,2)=wall, (4,1)[visited], (4,3).
- (0,3) dist=7. Tetangga valid: (0,2)=wall, (0,4), (1,3)[visited].
- (1,4) dist=7. Tetangga valid: (0,4), (2,4), (1,3)[visited].
- (4,3) dist=7. Tetangga valid: (3,3), (4,2)[visited], (4,4).
- (0,4) dist=8. (sudah dari (0,3) atau (1,4), dist=8)
- (2,4) dist=8.
- (3,3) dist=8.
- (4,4) dist=8.

**Jawaban:** Jarak terpendek dari (0,0) ke (4,4) = **8 langkah**

Salah satu jalur terpendek:
(0,0) -> (1,0) -> (2,0) -> (2,1) -> (3,1) -> (4,1) -> (4,2) -> (4,3) -> (4,4)

---

## Ringkasan

| Bagian | Topik | Jumlah Soal |
|--------|-------|-------------|
| A | Shortest Path (Dijkstra Trace) | 5 |
| B | MST (Kruskal Trace) | 5 |
| C | Topological Sort | 5 |
| D | DAG DP / Path Counting | 5 |
| E | Pemodelan Graf (Soal Cerita) | 5 |
| F | Campuran Lanjutan | 5 |
| **Total** | | **30** |

---

## Tips Mengerjakan Soal Graf Lanjutan di OSK

1. **Identifikasi jenis masalah:** Apakah shortest path, MST, topological sort, atau counting?
2. **Kenali sifat graf:** Berarah/tak berarah, berbobot/tak berbobot, DAG/ada siklus?
3. **Pilih algoritma yang tepat:**
   - Shortest path tak berbobot: BFS
   - Shortest path berbobot non-negatif: Dijkstra
   - MST: Kruskal (urutkan edge, pakai Union-Find)
   - Topological sort: Kahn (hitung in-degree) atau DFS
   - Counting paths: DAG DP
4. **Trace dengan teliti:** Di OSK, sering diminta trace langkah per langkah. Buat tabel!
5. **Perhatikan edge case:** Siklus (topological sort gagal), bobot negatif (Dijkstra tidak valid), graf tidak terhubung (MST tidak mencakup semua).
6. **Soal cerita ke graf:** Identifikasi apa yang menjadi simpul, apa yang menjadi edge, apakah berarah, apakah berbobot.
