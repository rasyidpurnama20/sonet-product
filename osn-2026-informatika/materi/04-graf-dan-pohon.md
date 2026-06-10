# Materi 04 — Graf & Pohon (Tree)

Panduan lengkap teori graf dan pohon untuk persiapan OSK Informatika 2026.
Materi mencakup definisi, representasi, algoritma penelusuran, sifat-sifat
khusus graf, pewarnaan, planaritas, serta contoh soal bertahap.

---

## 1. Definisi Graf

**Graf G = (V, E)** terdiri dari:
- **V** (vertex): himpunan simpul (node)
- **E** (edge): himpunan sisi/busur yang menghubungkan pasangan simpul

Secara visual, simpul digambar sebagai titik dan sisi sebagai garis penghubung.

```
    1 --- 2
    |     |
    3 --- 4
```

Pada contoh di atas:
- V = {1, 2, 3, 4}
- E = {(1,2), (1,3), (2,4), (3,4)}
- |V| = 4 (orde graf)
- |E| = 4 (ukuran graf)

### Notasi Penting
- n = |V| (jumlah simpul)
- m = |E| (jumlah sisi)
- Simpul u dan v dikatakan **bertetangga** (adjacent) jika terdapat sisi (u,v) di E.
- Sisi e = (u,v) dikatakan **incident** pada simpul u dan v.

---

## 2. Jenis-Jenis Graf

| Jenis | Penjelasan | Contoh |
|-------|-----------|--------|
| Graf Tak Berarah | Sisi tanpa arah: (u,v) = (v,u) | Jalan dua arah |
| Graf Berarah (Digraph) | Sisi punya arah: u -> v (belum tentu v -> u) | Jalan satu arah |
| Graf Berbobot | Setiap sisi memiliki nilai/bobot | Peta dengan jarak |
| Graf Sederhana | Tanpa loop dan tanpa sisi ganda | Paling umum di OSN |
| Multigraf | Boleh ada sisi ganda antar sepasang simpul | Dua jalan berbeda |
| Graf dengan Loop | Boleh ada sisi dari simpul ke dirinya sendiri | Relasi refleksif |

---

## 3. Graf-Graf Khusus

### 3.1 Graf Lengkap (K_n)

Setiap pasang simpul terhubung langsung. Jumlah sisi = C(n,2) = n(n-1)/2.

```
K_3:        K_4:           K_5:
  1            1              1
 / \         / | \          /|\ \
2---3       2--+--3        2 | 5--3
            |  |  |         \|/  /
            \  4  /          4--/
             \___/
```

| Graf | Simpul | Sisi | Derajat tiap simpul |
|------|--------|------|---------------------|
| K_3 | 3 | 3 | 2 |
| K_4 | 4 | 6 | 3 |
| K_5 | 5 | 10 | 4 |
| K_n | n | n(n-1)/2 | n-1 |

### 3.2 Graf Bipartit dan Bipartit Lengkap (K_{m,n})

Graf **bipartit**: himpunan V dibagi menjadi dua kelompok (partisi) X dan Y,
sisi hanya menghubungkan simpul dari X ke Y (tidak ada sisi di dalam X atau di dalam Y).

Graf **bipartit lengkap K_{m,n}**: setiap simpul di X terhubung ke semua simpul di Y.
Jumlah sisi = m x n.

```
K_{2,3}:
  X = {a, b}
  Y = {1, 2, 3}

  a --- 1
  a --- 2
  a --- 3
  b --- 1
  b --- 2
  b --- 3

  Jumlah sisi = 2 x 3 = 6
```

### 3.3 Graf Siklus (C_n)

Membentuk lingkaran dengan n simpul, masing-masing berderajat 2.

```
C_4:        C_5:
1 - 2       1 - 2
|   |       |     \
4 - 3       5      3
            |     /
            4----/
```

Jumlah sisi C_n = n.

### 3.4 Graf Lintasan (P_n)

Lintasan dari n simpul, membentuk garis lurus.

```
P_4: 1 --- 2 --- 3 --- 4
```

Jumlah sisi P_n = n-1.

### 3.5 Graf Roda (W_n)

Satu simpul pusat terhubung ke semua simpul pada siklus C_n.

```
W_4 (1 pusat, siklus 2-3-4-5):
        2
       /|\
      / | \
     5--1--3
      \ | /
       \|/
        4
```

Jumlah sisi W_n = 2n (n sisi siklus + n sisi ke pusat).

### 3.6 Graf Petersen

Graf terkenal dalam teori graf, memiliki 10 simpul dan 15 sisi. Sering digunakan sebagai contoh tandingan (counterexample) di berbagai teorema graf.

Sifat Graf Petersen:
- 10 simpul, 15 sisi
- Reguler berderajat 3 (setiap simpul berderajat 3)
- Tidak memiliki siklus Hamilton
- Bilangan kromatik = 3
- Bukan graf planar

---

## 4. Terminologi Graf

### 4.1 Derajat Simpul

**Derajat (degree)** simpul v, ditulis deg(v), adalah jumlah sisi yang terhubung ke v.

Pada graf berarah:
- **in-degree** (derajat masuk): jumlah sisi yang masuk ke v
- **out-degree** (derajat keluar): jumlah sisi yang keluar dari v

**Contoh:**
```
Graf:  1 --- 2 --- 3
       |         / |
       4--------/  5
```
- deg(1) = 2 (terhubung ke 2 dan 4)
- deg(2) = 2 (terhubung ke 1 dan 3)
- deg(3) = 3 (terhubung ke 2, 4, dan 5)
- deg(4) = 2 (terhubung ke 1 dan 3)
- deg(5) = 1 (terhubung ke 3 saja)

### 4.2 Teorema Handshaking (Jabat Tangan)

> Jumlah semua derajat simpul dalam graf = 2 x jumlah sisi

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Konsekuensi penting:**
- Jumlah simpul berderajat ganjil selalu **genap**.
- Jika semua simpul berderajat d (graf reguler), maka m = nd/2.

### 4.3 Istilah Penting Lainnya

| Istilah | Definisi |
|---------|----------|
| **Walk** | Urutan simpul-sisi dengan sisi boleh diulang |
| **Trail** | Walk tanpa sisi yang diulang |
| **Path (Lintasan)** | Walk tanpa simpul yang diulang |
| **Cycle (Siklus)** | Path yang kembali ke simpul awal |
| **Connected (Terhubung)** | Ada path antara setiap pasang simpul |
| **Komponen Terhubung** | Sub-graf terhubung maksimal |
| **Jarak d(u,v)** | Panjang path terpendek dari u ke v |
| **Diameter** | Jarak terbesar antar semua pasang simpul |
| **Cut Vertex** | Simpul yang jika dihapus membuat graf tidak terhubung |
| **Bridge** | Sisi yang jika dihapus membuat graf tidak terhubung |

---

## 5. Representasi Graf

### 5.1 Adjacency Matrix (Matriks Ketetanggaan)

Matriks berukuran n x n. Elemen M[i][j] = 1 jika ada sisi dari i ke j, 0 jika tidak.

**Contoh: Graf dengan sisi 1-2, 1-3, 2-3, 3-4**

```
     1  2  3  4
1  [ 0  1  1  0 ]
2  [ 1  0  1  0 ]
3  [ 1  1  0  1 ]
4  [ 0  0  1  0 ]
```

**Sifat:**
- Untuk graf tak berarah: matriks simetris (M[i][j] = M[j][i])
- Diagonal utama = 0 (graf sederhana tanpa loop)
- Jumlah 1 pada baris i = derajat simpul i
- Cocok untuk graf padat (dense)

**Untuk graf berbobot:** M[i][j] = bobot sisi, 0 atau infinity jika tidak ada sisi.

### 5.2 Adjacency List (Daftar Ketetanggaan)

Setiap simpul menyimpan daftar tetangganya.

**Contoh yang sama:**
```
1: [2, 3]
2: [1, 3]
3: [1, 2, 4]
4: [3]
```

**Sifat:**
- Hemat memori untuk graf jarang (sparse)
- Mudah iterasi tetangga simpul tertentu
- Paling umum digunakan di pemrograman kompetitif

### 5.3 Edge List (Daftar Sisi)

Menyimpan semua sisi sebagai pasangan (u, v) atau triplet (u, v, w) jika berbobot.

```
Edges: [(1,2), (1,3), (2,3), (3,4)]
```

### 5.4 Perbandingan Representasi

| Operasi | Adj. Matrix | Adj. List | Edge List |
|---------|-------------|-----------|-----------|
| Cek sisi (u,v) | O(1) | O(deg(u)) | O(m) |
| Daftar tetangga u | O(n) | O(deg(u)) | O(m) |
| Tambah sisi | O(1) | O(1) | O(1) |
| Space | O(n^2) | O(n+m) | O(m) |
| Iterasi semua sisi | O(n^2) | O(n+m) | O(m) |

**Kode C++ Adjacency List:**
```cpp
#include <vector>
using namespace std;

// Adjacency list untuk graf dengan maksimal 105 simpul
vector<int> adj[105];

void addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u); // hapus baris ini untuk graf berarah
}
```

---

## 6. BFS (Breadth-First Search)

### 6.1 Konsep

BFS adalah **algoritma penelusuran melebar** - mengeksplorasi semua simpul pada jarak d sebelum jarak d+1. Menggunakan struktur data **antrian (queue)**.

### 6.2 Langkah-Langkah

1. Masukkan simpul awal (source) ke antrian, tandai visited.
2. Selama antrian tidak kosong:
   - Keluarkan simpul u dari depan antrian.
   - Untuk setiap tetangga v dari u yang belum dikunjungi:
     - Tandai v sebagai dikunjungi.
     - Simpan jarak: dist[v] = dist[u] + 1.
     - Masukkan v ke belakang antrian.
3. Selesai ketika antrian kosong.

### 6.3 Contoh Trace BFS Detail

**Graf:**
```
    1 --- 2 --- 5
    |     |     |
    3 --- 4 --- 6
          |
          7
```
Sisi: {(1,2), (1,3), (2,4), (2,5), (3,4), (4,6), (4,7), (5,6)}

**BFS dari simpul 1:**

| Langkah | Antrian | Dikunjungi | dist |
|---------|---------|------------|------|
| Init | [1] | {1} | d[1]=0 |
| Ambil 1, proses tetangga 2,3 | [2, 3] | {1,2,3} | d[2]=1, d[3]=1 |
| Ambil 2, proses tetangga 4,5 | [3, 4, 5] | {1,2,3,4,5} | d[4]=2, d[5]=2 |
| Ambil 3, tetangga 4 sudah visited | [4, 5] | {1,2,3,4,5} | - |
| Ambil 4, proses tetangga 6,7 | [5, 6, 7] | {1,2,3,4,5,6,7} | d[6]=3, d[7]=3 |
| Ambil 5, tetangga 6 sudah visited | [6, 7] | {1,2,3,4,5,6,7} | - |
| Ambil 6, semua visited | [7] | {1,2,3,4,5,6,7} | - |
| Ambil 7, semua visited | [] | {1,2,3,4,5,6,7} | - |

**Urutan kunjungan: 1, 2, 3, 4, 5, 6, 7**
**Jarak dari simpul 1:** d[1]=0, d[2]=1, d[3]=1, d[4]=2, d[5]=2, d[6]=3, d[7]=3

### 6.4 Kode C++ BFS

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[105];
bool visited[105];
int dist[105];

void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    dist[start] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}
```

### 6.5 Kegunaan BFS
- Mencari **jarak terpendek** pada graf tanpa bobot
- Menentukan **komponen terhubung**
- Mengecek apakah graf **bipartit** (2-colorable)
- Level-order traversal pada pohon

---

## 7. DFS (Depth-First Search)

### 7.1 Konsep

DFS adalah **algoritma penelusuran mendalam** - mengeksplorasi sejauh mungkin ke satu arah sebelum backtrack. Menggunakan **stack** (bisa implisit via rekursi).

### 7.2 Langkah-Langkah

1. Kunjungi simpul awal, tandai visited.
2. Untuk setiap tetangga yang belum dikunjungi, panggil DFS secara rekursif.
3. Backtrack ketika semua tetangga sudah dikunjungi.

### 7.3 Contoh Trace DFS Detail

**Menggunakan graf yang sama:**
```
    1 --- 2 --- 5
    |     |     |
    3 --- 4 --- 6
          |
          7
```

**DFS dari simpul 1 (tetangga diproses dari kecil ke besar):**

| Langkah | Stack (rekursi) | Dikunjungi | Aksi |
|---------|-----------------|------------|------|
| 1 | [1] | {1} | Kunjungi 1, panggil DFS(2) |
| 2 | [1, 2] | {1, 2} | Kunjungi 2, panggil DFS(4) |
| 3 | [1, 2, 4] | {1, 2, 4} | Kunjungi 4, panggil DFS(3) |
| 4 | [1, 2, 4, 3] | {1, 2, 4, 3} | Kunjungi 3, semua tetangga visited, backtrack |
| 5 | [1, 2, 4] | {1, 2, 4, 3} | Lanjut DFS(4), panggil DFS(6) |
| 6 | [1, 2, 4, 6] | {1, 2, 4, 3, 6} | Kunjungi 6, panggil DFS(5) |
| 7 | [1, 2, 4, 6, 5] | {1, 2, 4, 3, 6, 5} | Kunjungi 5, semua tetangga visited, backtrack |
| 8 | [1, 2, 4, 6] | {1, 2, 4, 3, 6, 5} | Backtrack |
| 9 | [1, 2, 4] | {1, 2, 4, 3, 6, 5} | Panggil DFS(7) |
| 10 | [1, 2, 4, 7] | {1, 2, 4, 3, 6, 5, 7} | Kunjungi 7, backtrack semua |

**Urutan kunjungan: 1, 2, 4, 3, 6, 5, 7**

### 7.4 Kode C++ DFS (Rekursif)

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[105];
bool visited[105];

void dfs(int u) {
    visited[u] = true;
    cout << u << " ";
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
        }
    }
}
```

### 7.5 Kode C++ DFS (Iteratif dengan Stack)

```cpp
void dfs_iterative(int start) {
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int u = st.top();
        st.pop();
        if (visited[u]) continue;
        visited[u] = true;
        cout << u << " ";
        // push tetangga dalam urutan terbalik agar urutan kecil diproses dulu
        for (int i = adj[u].size()-1; i >= 0; i--) {
            if (!visited[adj[u][i]]) {
                st.push(adj[u][i]);
            }
        }
    }
}
```

### 7.6 Kegunaan DFS
- **Deteksi siklus** dalam graf
- **Topological sort** (graf berarah tanpa siklus / DAG)
- Menentukan **komponen terhubung kuat** (SCC)
- Menentukan **articulation point** (cut vertex) dan **bridge**
- Pengecekan **bipartit**

### 7.7 Perbandingan BFS vs DFS

| Aspek | BFS | DFS |
|-------|-----|-----|
| Struktur data | Queue | Stack / Rekursi |
| Pola eksplorasi | Melebar (level by level) | Mendalam (sejauh mungkin) |
| Shortest path (unweighted) | Ya | Tidak dijamin |
| Deteksi siklus | Bisa | Bisa (lebih natural) |
| Space (worst case) | O(n) - lebar maksimal | O(n) - kedalaman maks |
| Kapan dipakai | Jarak terpendek, BFS tree | Siklus, topological sort |

---

## 8. Lintasan dan Sirkuit Euler

### 8.1 Definisi

- **Lintasan Euler (Euler Path):** Trail yang melewati **setiap sisi tepat sekali**.
- **Sirkuit Euler (Euler Circuit):** Trail yang melewati setiap sisi tepat sekali DAN kembali ke simpul awal.

### 8.2 Teorema Euler

Untuk graf terhubung:

| Kondisi | Syarat |
|---------|--------|
| Sirkuit Euler ada | Semua simpul berderajat **genap** |
| Lintasan Euler ada (bukan sirkuit) | Tepat **2 simpul** berderajat ganjil |
| Tidak ada keduanya | Lebih dari 2 simpul berderajat ganjil |

**Penjelasan intuitif:** Setiap kali memasuki simpul, harus bisa keluar.
Jadi setiap simpul harus punya sisi masuk dan keluar berpasangan (derajat genap).
Kecuali simpul awal dan akhir pada lintasan Euler (boleh ganjil).

### 8.3 Contoh

**Graf 1:**
```
    A --- B
    |   / |
    |  /  |
    C --- D
```
Sisi: AB, AC, BC, BD, CD
- deg(A) = 2, deg(B) = 3, deg(C) = 3, deg(D) = 2
- Tepat 2 simpul berderajat ganjil (B dan C)
- Lintasan Euler ADA, mulai dari B atau C
- Contoh: B-A-C-B-D-C

**Graf 2:**
```
    A --- B
    |     |
    D --- C
    |     |
    E --- F
```
Sisi: AB, BC, CD, DA, DE, EF, FC
- deg(A) = 2, deg(B) = 2, deg(C) = 3, deg(D) = 3, deg(E) = 2, deg(F) = 2
- Tepat 2 simpul berderajat ganjil (C dan D)
- Lintasan Euler ada mulai dari C atau D

**Graf 3 (semua genap):**
```
    1 --- 2
    |\ /| 
    | X  |
    |/ \|
    3 --- 4
```
Sisi: 12, 13, 14, 23, 24, 34 (K_4)
- Semua simpul berderajat 3 (ganjil) -> Tidak punya lintasan/sirkuit Euler!

**Graf K_4 TIDAK punya Euler path** karena ada 4 simpul berderajat ganjil.

### 8.4 Lintasan dan Sirkuit Hamilton

- **Lintasan Hamilton:** Path yang mengunjungi **setiap simpul tepat sekali**.
- **Sirkuit Hamilton:** Cycle yang mengunjungi setiap simpul tepat sekali.

**Perbedaan dengan Euler:**
- Euler: setiap **sisi** tepat sekali
- Hamilton: setiap **simpul** tepat sekali

Tidak ada teorema sederhana seperti Euler untuk menentukan keberadaan Hamilton.
Namun ada beberapa syarat cukup:

**Teorema Dirac:** Jika n >= 3 dan setiap simpul berderajat >= n/2, maka graf memiliki sirkuit Hamilton.

---

## 9. Pewarnaan Graf (Graph Coloring)

### 9.1 Definisi

**Pewarnaan simpul (vertex coloring):** Memberi warna pada setiap simpul sedemikian sehingga tidak ada dua simpul bertetangga yang memiliki warna sama.

**Bilangan kromatik** chi(G): jumlah warna minimum yang diperlukan untuk mewarnai graf G.

### 9.2 Contoh Pewarnaan

```
Graf C_3 (segitiga):    Graf C_4 (persegi):
    A(merah)                A(merah) - B(biru)
   / \                      |           |
  B   C                    D(biru)  - C(merah)
(biru)(hijau)

chi(C_3) = 3              chi(C_4) = 2
```

### 9.3 Fakta Penting

| Graf | Bilangan Kromatik |
|------|-------------------|
| Graf tanpa sisi (E = kosong) | 1 |
| Graf bipartit (tanpa sisi) | 1 |
| Graf bipartit (dengan sisi) | 2 |
| Siklus genap C_{2k} | 2 |
| Siklus ganjil C_{2k+1} | 3 |
| Graf lengkap K_n | n |
| Pohon (n >= 2) | 2 |
| Graf Petersen | 3 |

### 9.4 Batas Bilangan Kromatik

- chi(G) >= omega(G), dimana omega(G) = ukuran clique terbesar
- chi(G) <= Delta(G) + 1, dimana Delta(G) = derajat maksimum (Teorema Brooks memberikan batas lebih ketat untuk sebagian besar graf)

### 9.5 Hubungan dengan Bipartit

> Graf G adalah bipartit JIKA DAN HANYA JIKA chi(G) <= 2
> (yaitu, G tidak mengandung siklus ganjil)

Ini berarti: graf bisa diwarnai 2 warna = graf bipartit = tidak ada siklus ganjil.

---

## 10. Graf Planar dan Rumus Euler

### 10.1 Definisi

**Graf planar:** graf yang dapat digambar di bidang datar tanpa ada sisi yang saling berpotongan.

### 10.2 Rumus Euler untuk Graf Planar

Untuk graf planar terhubung:

> **V - E + F = 2**

dimana:
- V = jumlah simpul
- E = jumlah sisi
- F = jumlah muka (face), termasuk muka luar (infinite face)

**Contoh:**
```
Graf segitiga (K_3):
    A
   / \
  B---C

V = 3, E = 3, F = 2 (segitiga dalam + muka luar)
Cek: 3 - 3 + 2 = 2  (benar!)
```

```
Graf kubus (persegi):
  A---B
  |   |
  D---C

V = 4, E = 4, F = 2 (persegi dalam + muka luar)
Cek: 4 - 4 + 2 = 2  (benar!)
```

```
K_4 planar (tetrahedron):
    A
   /|\
  B-+-C
   \|/
    D

V = 4, E = 6, F = 4
Cek: 4 - 6 + 4 = 2  (benar!)
```

### 10.3 Konsekuensi Rumus Euler

Untuk graf planar sederhana terhubung dengan V >= 3:

1. **E <= 3V - 6** (batas atas jumlah sisi)
2. Jika graf juga **bebas segitiga** (tanpa C_3): **E <= 2V - 4**

### 10.4 Pembuktian K_5 Bukan Planar

K_5 memiliki V = 5, E = 10.
Cek: E <= 3V - 6 -> 10 <= 3(5) - 6 = 9? **TIDAK!**
Jadi K_5 bukan graf planar.

### 10.5 Pembuktian K_{3,3} Bukan Planar

K_{3,3} memiliki V = 6, E = 9, dan bebas segitiga (bipartit).
Cek: E <= 2V - 4 -> 9 <= 2(6) - 4 = 8? **TIDAK!**
Jadi K_{3,3} bukan graf planar.

### 10.6 Teorema Kuratowski

> Graf G planar JIKA DAN HANYA JIKA G tidak mengandung subdivisi dari K_5 atau K_{3,3}.

Ini artinya: dua "penghalang" planaritas adalah K_5 dan K_{3,3}.

---

## 11. Pohon (Tree)

### 11.1 Definisi

**Pohon:** graf terhubung yang tidak memiliki siklus (acyclic connected graph).

### 11.2 Sifat-Sifat Pohon

Untuk graf G dengan n simpul, pernyataan berikut **saling ekuivalen**:
1. G adalah pohon (terhubung dan tanpa siklus)
2. G terhubung dan memiliki tepat **n - 1 sisi**
3. G tanpa siklus dan memiliki tepat **n - 1 sisi**
4. Terdapat **tepat satu** lintasan antara setiap pasang simpul
5. G terhubung, tetapi menghapus sisi mana pun membuatnya tidak terhubung
6. G tanpa siklus, tetapi menambah sisi mana pun membuat tepat satu siklus

### 11.3 Hutan (Forest)

**Hutan:** graf tanpa siklus (mungkin tidak terhubung).
- Hutan = kumpulan pohon yang terpisah.
- Jika hutan memiliki n simpul dan k komponen, maka jumlah sisi = n - k.

### 11.4 Pohon Berakar (Rooted Tree)

Pohon dengan satu simpul khusus yang ditunjuk sebagai **akar (root)**.

**Terminologi:**
| Istilah | Definisi |
|---------|----------|
| Root (Akar) | Simpul paling atas / referensi |
| Parent (Induk) | Simpul di atas pada path ke root |
| Child (Anak) | Simpul di bawah yang langsung terhubung |
| Sibling | Anak-anak dari parent yang sama |
| Leaf (Daun) | Simpul tanpa anak |
| Internal node | Simpul yang bukan daun |
| Depth / Level | Jarak dari root (root = depth 0) |
| Height | Depth terbesar di pohon |
| Subtree | Bagian pohon yang berakar di simpul tertentu |
| Ancestor | Simpul di path dari v ke root |
| Descendant | Simpul di subtree dari v |

**Contoh:**
```
         1          <- root, depth 0
        / \
       2   3        <- depth 1
      / \   \
     4   5   6      <- depth 2 (daun: 4, 5, 6)

Height = 2
Daun: {4, 5, 6}
Parent(5) = 2
Children(2) = {4, 5}
Subtree(2) = {2, 4, 5}
```

### 11.5 Spanning Tree (Pohon Merentang)

**Spanning tree** dari graf G adalah subgraf yang:
- Memuat semua simpul G
- Merupakan pohon (terhubung, tanpa siklus)

Setiap graf terhubung memiliki setidaknya satu spanning tree.
Jumlah sisi spanning tree selalu = n - 1.

**Mencari spanning tree:** Jalankan BFS atau DFS, sisi yang dipakai membentuk spanning tree.

---

## 12. Binary Tree (Pohon Biner)

### 12.1 Definisi

**Pohon biner:** pohon berakar dimana setiap simpul memiliki **paling banyak 2 anak** (anak kiri dan anak kanan).

### 12.2 Jenis-Jenis Binary Tree

| Jenis | Definisi |
|-------|----------|
| **Full Binary Tree** | Setiap simpul memiliki 0 atau 2 anak (tidak ada yang punya 1 anak) |
| **Complete Binary Tree** | Semua level terisi penuh kecuali level terakhir yang terisi dari kiri |
| **Perfect Binary Tree** | Semua internal node punya 2 anak DAN semua daun di level yang sama |
| **Balanced Binary Tree** | Selisih tinggi subtree kiri dan kanan setiap node paling banyak 1 |

### 12.3 Rumus Penting Binary Tree

**Perfect Binary Tree dengan tinggi h:**
- Jumlah simpul: 2^(h+1) - 1
- Jumlah daun: 2^h
- Jumlah internal node: 2^h - 1

**Hubungan daun dan internal node (Full Binary Tree):**
- Jika L = jumlah daun dan I = jumlah internal node, maka L = I + 1

**Tinggi minimum pohon biner dengan n simpul:**
- h_min = floor(log2(n))

**Tinggi maksimum pohon biner dengan n simpul:**
- h_max = n - 1 (degenerasi menjadi lintasan)

### 12.4 Tabel Ringkas

| Tinggi h | Simpul (perfect) | Daun (perfect) | Internal node |
|----------|-------------------|----------------|---------------|
| 0 | 1 | 1 | 0 |
| 1 | 3 | 2 | 1 |
| 2 | 7 | 4 | 3 |
| 3 | 15 | 8 | 7 |
| 4 | 31 | 16 | 15 |
| h | 2^(h+1)-1 | 2^h | 2^h - 1 |

---

## 13. Traversal Pohon Biner

### 13.1 Tiga Urutan Traversal

| Traversal | Urutan Kunjungan |
|-----------|-----------------|
| **Pre-order** | Root, Kiri, Kanan |
| **In-order** | Kiri, Root, Kanan |
| **Post-order** | Kiri, Kanan, Root |
| **Level-order** | Level 0, Level 1, Level 2, ... (BFS) |

### 13.2 Contoh Lengkap

```
         A
        / \
       B   C
      / \   \
     D   E   F
        / \
       G   H
```

**Pre-order (Root-Kiri-Kanan):** A, B, D, E, G, H, C, F
**In-order (Kiri-Root-Kanan):** D, B, G, E, H, A, C, F
**Post-order (Kiri-Kanan-Root):** D, G, H, E, B, F, C, A
**Level-order:** A, B, C, D, E, F, G, H

### 13.3 Rekonstruksi Pohon dari Dua Traversal

Dengan mengetahui **dua** urutan traversal (salah satunya harus in-order), kita bisa merekonstruksi pohon secara unik.

**Metode dari Pre-order + In-order:**
1. Elemen pertama pre-order = root
2. Cari root di in-order. Elemen di kiri = subtree kiri, di kanan = subtree kanan
3. Ulangi secara rekursif

**Metode dari Post-order + In-order:**
1. Elemen terakhir post-order = root
2. Cari root di in-order. Bagi menjadi subtree kiri dan kanan
3. Ulangi secara rekursif

### 13.4 Contoh Rekonstruksi

**Diberikan:**
- Pre-order: 1, 2, 4, 5, 3, 6, 7
- In-order: 4, 2, 5, 1, 6, 3, 7

**Langkah 1:** Root = 1 (elemen pertama pre-order)
In-order dibagi: [4, 2, 5] | 1 | [6, 3, 7]
Subtree kiri: 3 simpul, Subtree kanan: 3 simpul

**Langkah 2:** Subtree kiri, pre-order: 2, 4, 5. In-order: 4, 2, 5
Root subtree kiri = 2
Dibagi: [4] | 2 | [5]

**Langkah 3:** Subtree kanan, pre-order: 3, 6, 7. In-order: 6, 3, 7
Root subtree kanan = 3
Dibagi: [6] | 3 | [7]

**Hasil:**
```
         1
        / \
       2   3
      / \ / \
     4  5 6  7
```

---

## 14. Pohon Berbobot dan Jumlah Lintasan

### 14.1 Definisi

Pohon berbobot: setiap sisi memiliki bobot (angka). Bobot bisa merepresentasikan jarak, biaya, waktu, dll.

### 14.2 Jarak pada Pohon Berbobot

Jarak antara dua simpul = jumlah bobot sisi pada lintasan unik yang menghubungkan keduanya.

**Contoh:**
```
      A
     / \
   (3) (5)
   /     \
  B       C
 / \       \
(2) (4)   (1)
/     \     \
D      E     F
```

- Jarak A ke D = 3 + 2 = 5
- Jarak A ke E = 3 + 4 = 7
- Jarak A ke F = 5 + 1 = 6
- Jarak D ke F = 2 + 3 + 5 + 1 = 11 (D-B-A-C-F)
- Jarak D ke E = 2 + 4 = 6 (D-B-E)

### 14.3 Diameter Pohon

**Diameter pohon berbobot** = jarak terpanjang antara dua simpul mana pun.

Pada contoh di atas: diameter = jarak D ke E via B = 2 + 4 = 6? Atau D ke F = 11?
D ke F = 2 + 3 + 5 + 1 = 11. E ke F = 4 + 3 + 5 + 1 = 13.

Diameter = 13 (dari E ke F: E-B-A-C-F).

---

## 15. Contoh Soal dan Pembahasan

### Contoh 1: Menghitung Sisi Graf Lengkap

**Soal:** Berapa banyak sisi pada graf lengkap K_8?

**Pembahasan:**
Jumlah sisi K_n = C(n, 2) = n(n-1)/2
K_8 = 8 x 7 / 2 = **28 sisi**

---

### Contoh 2: Teorema Handshaking

**Soal:** Suatu graf memiliki 6 simpul dengan derajat masing-masing: 3, 3, 2, 2, 1, 1. Berapa jumlah sisinya?

**Pembahasan:**
Jumlah derajat = 3 + 3 + 2 + 2 + 1 + 1 = 12
Jumlah sisi = 12 / 2 = **6 sisi**

---

### Contoh 3: Eksistensi Graf

**Soal:** Apakah mungkin ada graf sederhana dengan 5 simpul dimana derajat masing-masing simpul adalah 3, 3, 3, 3, 1?

**Pembahasan:**
Jumlah derajat = 3 + 3 + 3 + 3 + 1 = 13 (ganjil)
Berdasarkan Teorema Handshaking, jumlah derajat harus genap (= 2m).
Karena 13 ganjil, graf semacam ini **tidak mungkin ada**.

---

### Contoh 4: Lintasan Euler

**Soal:** Tentukan apakah graf berikut memiliki lintasan Euler, sirkuit Euler, atau keduanya tidak ada.
```
    A --- B --- C
    |     |     |
    D --- E --- F
```
Sisi: AB, BC, AD, BE, CF, DE, EF

**Pembahasan:**
- deg(A) = 2 (AB, AD)
- deg(B) = 3 (AB, BC, BE)
- deg(C) = 2 (BC, CF)
- deg(D) = 2 (AD, DE)
- deg(E) = 3 (BE, DE, EF)
- deg(F) = 2 (CF, EF)

Simpul berderajat ganjil: B dan E (tepat 2 simpul)
Kesimpulan: **Lintasan Euler ada** (mulai dari B atau E), tetapi **sirkuit Euler tidak ada**.

Contoh lintasan Euler: B-A-D-E-B-C-F-E (7 sisi, masing-masing dilewati sekali)

---

### Contoh 5: Rumus Euler (Planar)

**Soal:** Suatu graf planar terhubung memiliki 8 simpul dan 12 sisi. Berapa jumlah mukanya?

**Pembahasan:**
V - E + F = 2
8 - 12 + F = 2
F = 2 + 12 - 8 = **6 muka**

---

### Contoh 6: Pembuktian Non-Planaritas

**Soal:** Buktikan bahwa graf dengan 6 simpul, 10 sisi, dan tanpa segitiga bukan graf planar.

**Pembahasan:**
Untuk graf planar bebas segitiga: E <= 2V - 4
Cek: 10 <= 2(6) - 4 = 8?
10 > 8, jadi syarat TIDAK terpenuhi.
Kesimpulan: **graf tersebut bukan planar**.

---

### Contoh 7: BFS - Jarak Terpendek

**Soal:** Diberikan graf dengan sisi: {(1,2), (1,3), (2,4), (3,4), (3,5), (4,6), (5,6)}.
Tentukan jarak terpendek dari simpul 1 ke simpul 6.

**Pembahasan:**
```
    1 --- 2
    |     |
    3 --- 4 --- 6
    |           |
    5-----------/
```

BFS dari 1:
- Level 0: {1}
- Level 1: {2, 3} (tetangga 1)
- Level 2: {4, 5} (tetangga 2 dan 3 yang belum visited)
- Level 3: {6} (tetangga 4 dan 5)

Jarak terpendek dari 1 ke 6 = **3**

---

### Contoh 8: DFS dan Deteksi Siklus

**Soal:** Lakukan DFS pada graf berarah berikut dari simpul 1. Tentukan apakah ada siklus.
Sisi berarah: 1->2, 2->3, 3->4, 4->2, 1->5

**Pembahasan:**
DFS dari 1:
- Kunjungi 1, lanjut ke 2
- Kunjungi 2, lanjut ke 3
- Kunjungi 3, lanjut ke 4
- Kunjungi 4, tetangga 2 sudah di stack rekursi (masih aktif!)

Menemukan sisi balik (back edge): 4 -> 2
Ini menandakan ada **siklus: 2 -> 3 -> 4 -> 2**

Setelah backtrack, kunjungi 5 dari simpul 1.
Urutan DFS: 1, 2, 3, 4, 5

---

### Contoh 9: Sifat Pohon

**Soal:** Suatu pohon memiliki 3 simpul berderajat 1 (daun), 2 simpul berderajat 2, dan 1 simpul berderajat 3. Berapa total simpul dan sisi?

**Pembahasan:**
Total simpul n = 3 + 2 + 1 = 6
Jumlah sisi pohon = n - 1 = 6 - 1 = **5 sisi**

Verifikasi handshaking: 3(1) + 2(2) + 1(3) = 3 + 4 + 3 = 10 = 2 x 5. Benar!

---

### Contoh 10: Binary Tree - Jumlah Node

**Soal:** Sebuah perfect binary tree memiliki 15 simpul. Tentukan:
(a) Tinggi pohon
(b) Jumlah daun
(c) Jumlah internal node

**Pembahasan:**
Perfect binary tree: jumlah simpul = 2^(h+1) - 1

(a) 2^(h+1) - 1 = 15
    2^(h+1) = 16
    h + 1 = 4
    h = **3**

(b) Jumlah daun = 2^h = 2^3 = **8**

(c) Jumlah internal node = 2^h - 1 = 8 - 1 = **7**
    Atau: 15 - 8 = 7

---

### Contoh 11: Rekonstruksi Pohon Biner

**Soal:** Diberikan:
- In-order: D, B, E, A, F, C, G
- Post-order: D, E, B, F, G, C, A

Rekonstruksi pohon biner tersebut dan tentukan pre-order-nya.

**Pembahasan:**

**Langkah 1:** Elemen terakhir post-order = A (root)
In-order dibagi: [D, B, E] | A | [F, C, G]
Subtree kiri: 3 elemen, Subtree kanan: 3 elemen

**Langkah 2:** Subtree kiri.
Post-order (3 elemen pertama): D, E, B. Elemen terakhir = B (root subtree kiri)
In-order [D, B, E] dibagi: [D] | B | [E]
Anak kiri B = D, anak kanan B = E

**Langkah 3:** Subtree kanan.
Post-order (3 elemen berikutnya sebelum A): F, G, C. Elemen terakhir = C (root subtree kanan)
In-order [F, C, G] dibagi: [F] | C | [G]
Anak kiri C = F, anak kanan C = G

**Hasil:**
```
         A
        / \
       B   C
      / \ / \
     D  E F  G
```

**Pre-order: A, B, D, E, C, F, G**

---

### Contoh 12: Pewarnaan Graf

**Soal:** Tentukan bilangan kromatik graf berikut (graf Petersen mini / C_5):
```
    1 --- 2
   / \   / \
  5   \ /   3
   \   X   /
    \ / \ /
     4---/
```
Sebenarnya ini C_5 (siklus 5 simpul): 1-2-3-4-5-1

**Pembahasan:**
C_5 adalah siklus ganjil (5 simpul).
Siklus ganjil memiliki bilangan kromatik = 3.

Pewarnaan:
- Simpul 1: merah
- Simpul 2: biru
- Simpul 3: merah
- Simpul 4: biru
- Simpul 5: hijau (tidak bisa merah karena bertetangga dengan 1, tidak bisa biru karena bertetangga dengan 4)

chi(C_5) = **3**

---

### Contoh 13: Graf Bipartit

**Soal:** Tentukan apakah graf berikut bipartit:
Simpul: {1, 2, 3, 4, 5, 6}
Sisi: {(1,2), (1,4), (2,3), (3,4), (4,5), (5,6), (6,3)}

**Pembahasan:**
Coba 2-coloring (BFS):
- 1: merah
- 2: biru (tetangga 1)
- 4: biru (tetangga 1)
- 3: merah (tetangga 2)
- Cek: 3 tetangga 4? Ya. 3 merah, 4 biru. OK!
- 5: merah (tetangga 4)
- 6: biru (tetangga 5)
- Cek: 6 tetangga 3? Ya. 6 biru, 3 merah. OK!

Partisi: X = {1, 3, 5} (merah), Y = {2, 4, 6} (biru)
Semua sisi menghubungkan X dengan Y.
Kesimpulan: **graf ini bipartit**.

Cara cepat: tidak ada siklus ganjil, jadi bipartit.

---

### Contoh 14: Spanning Tree

**Soal:** Berapa banyak spanning tree yang berbeda pada K_4?

**Pembahasan:**
Menggunakan **Teorema Cayley**: jumlah spanning tree berlabel pada K_n = n^(n-2)

Untuk K_4: 4^(4-2) = 4^2 = **16 spanning tree**

Secara manual: K_4 punya 4 simpul. Spanning tree harus punya 3 sisi dari 6 sisi yang tersedia, membentuk pohon.

---

### Contoh 15: Diameter Pohon

**Soal:** Pohon berbobot berikut memiliki sisi:
A-B (bobot 3), B-C (bobot 5), B-D (bobot 2), C-E (bobot 4), C-F (bobot 1).
Tentukan diameter pohon.

**Pembahasan:**
```
     A
     |
    (3)
     |
     B
    / \
  (2) (5)
  /     \
 D       C
        / \
      (4) (1)
      /     \
     E       F
```

Kandidat path terpanjang (antara dua daun):
- A ke D: 3 + 2 = 5
- A ke E: 3 + 5 + 4 = 12
- A ke F: 3 + 5 + 1 = 9
- D ke E: 2 + 5 + 4 = 11
- D ke F: 2 + 5 + 1 = 8
- E ke F: 4 + 1 = 5

Diameter = **12** (path A-B-C-E)

---

### Contoh 16: Aplikasi - Menentukan Komponen Terhubung

**Soal:** Graf G memiliki 8 simpul dengan sisi: {(1,2), (2,3), (4,5), (5,6), (7,8)}.
Berapa banyak komponen terhubung? Tuliskan simpul di setiap komponen.

**Pembahasan:**
BFS/DFS dari setiap simpul yang belum dikunjungi:
- Komponen 1: {1, 2, 3} (terhubung via sisi 1-2, 2-3)
- Komponen 2: {4, 5, 6} (terhubung via sisi 4-5, 5-6)
- Komponen 3: {7, 8} (terhubung via sisi 7-8)

Jumlah komponen terhubung = **3**

---

## 16. Pola Soal OSN yang Sering Muncul

### 16.1 Tipe "Hitung Sisi/Simpul"

Gunakan rumus:
- K_n: C(n,2) = n(n-1)/2 sisi
- K_{m,n}: m x n sisi
- Pohon n simpul: n-1 sisi
- Handshaking: sum deg = 2m

### 16.2 Tipe "Traversal/Urutan Kunjungan"

Tips:
- BFS: gunakan queue, proses level per level
- DFS: gunakan rekursi, telusuri sedalam mungkin
- Perhatikan urutan pemrosesan tetangga (biasanya dari kecil ke besar)

### 16.3 Tipe "Euler Path/Circuit"

Langkah:
1. Hitung derajat setiap simpul
2. Hitung berapa simpul berderajat ganjil
3. 0 ganjil -> sirkuit Euler, 2 ganjil -> lintasan Euler, >2 -> tidak ada

### 16.4 Tipe "Rekonstruksi Pohon"

Langkah:
1. Tentukan root dari pre-order (elemen pertama) atau post-order (elemen terakhir)
2. Gunakan in-order untuk menentukan subtree kiri dan kanan
3. Rekursi

### 16.5 Tipe "Pewarnaan/Bipartit"

Tips:
- Cek apakah ada siklus ganjil (jika ya, bukan bipartit, chi >= 3)
- Pohon dan siklus genap: chi = 2
- K_n: chi = n

### 16.6 Tipe "Planaritas"

Tips:
- Gunakan E <= 3V - 6 (umum) atau E <= 2V - 4 (bebas segitiga)
- Cari subdivisi K_5 atau K_{3,3}
- Hitung muka: F = 2 - V + E

### 16.7 Tipe "Jumlah/Sifat Binary Tree"

Rumus kunci:
- Perfect BT tinggi h: 2^(h+1) - 1 simpul, 2^h daun
- Full BT: daun = internal + 1
- Complete BT dengan n simpul: tinggi = floor(log2(n))

---

## 17. Latihan Mandiri

### Soal Dasar (1-5)

**1.** Gambarkan adjacency matrix dan adjacency list untuk graf dengan simpul {A, B, C, D, E} dan sisi {AB, AC, BD, CD, CE, DE}.

**2.** Hitung jumlah sisi pada graf K_7 dan K_{4,5}.

**3.** Lakukan BFS dari simpul A pada graf soal nomor 1. Tuliskan urutan kunjungan dan jarak masing-masing simpul dari A.

**4.** Lakukan DFS dari simpul A pada graf soal nomor 1 (tetangga diproses secara alfabetis). Tuliskan urutan kunjungan.

**5.** Pohon T memiliki 10 simpul. Berapa sisinya? Jika pohon ini adalah binary tree, berapa tinggi minimumnya?

### Soal Menengah (6-10)

**6.** Tentukan apakah graf berikut memiliki sirkuit Euler, lintasan Euler, atau keduanya tidak ada:
- (a) K_4
- (b) K_5
- (c) Graf dengan derajat: 4, 4, 4, 2, 2

**7.** Diberikan pre-order: A, B, D, G, E, C, F, H, I dan in-order: G, D, B, E, A, C, H, F, I.
Rekonstruksi pohon biner dan tentukan post-order-nya.

**8.** Suatu graf planar memiliki 10 simpul dan 7 muka. Berapa jumlah sisinya? Verifikasi bahwa jumlah sisi memenuhi batas atas E <= 3V - 6.

**9.** Buktikan bahwa setiap pohon dengan minimal 2 simpul adalah graf bipartit (chi = 2).

**10.** Diberikan pohon berbobot:
```
    1
   / \
 (4) (6)
 /     \
2       3
|      / \
(3)  (2) (5)
|    /     \
4   5       6
```
Tentukan jarak dari simpul 4 ke simpul 6 dan diameter pohon.

### Soal Lanjutan (11-15)

**11.** Sebuah turnamen catur diikuti 8 orang. Setiap pasangan bermain tepat sekali. Berapa total pertandingan? Modelkan sebagai graf - graf jenis apa ini?

**12.** Graf G memiliki 6 simpul dan merupakan graf planar. Berapa jumlah maksimum sisi yang bisa dimiliki G?

**13.** Tentukan bilangan kromatik graf Petersen. Berikan contoh pewarnaan valid dengan jumlah warna minimum.

**14.** Suatu jaringan komputer digambar sebagai graf dimana setiap komputer (simpul) terhubung ke tepat 3 komputer lain. Jika ada 10 komputer, berapa banyak kabel (sisi) yang dibutuhkan?

**15.** Diberikan graf berbobot dengan 6 simpul. BFS dan DFS dari simpul yang sama dapat menghasilkan spanning tree yang berbeda. Berikan contoh graf dan tunjukkan kedua spanning tree-nya.

---

## 18. Kunci Jawaban Latihan

**Jawaban 2:**
- K_7 = 7 x 6 / 2 = 21 sisi
- K_{4,5} = 4 x 5 = 20 sisi

**Jawaban 5:**
- Sisi = 10 - 1 = 9
- Tinggi minimum binary tree 10 simpul = floor(log2(10)) = floor(3.32) = 3

**Jawaban 6:**
- (a) K_4: semua simpul berderajat 3 (ganjil). Ada 4 simpul ganjil -> **tidak ada** Euler path/circuit
- (b) K_5: semua simpul berderajat 4 (genap) -> **sirkuit Euler ada**
- (c) Derajat: 4,4,4,2,2. Semua genap -> **sirkuit Euler ada**

**Jawaban 8:**
V - E + F = 2
10 - E + 7 = 2
E = 15 sisi.
Cek: E <= 3V - 6 -> 15 <= 3(10) - 6 = 24. Benar, syarat terpenuhi.

**Jawaban 11:**
8 orang, setiap pasangan bermain sekali: ini adalah graf lengkap K_8.
Total pertandingan = C(8,2) = 8 x 7 / 2 = 28 pertandingan.

**Jawaban 12:**
Graf planar: E <= 3V - 6 = 3(6) - 6 = 12 sisi (maksimum).

**Jawaban 14:**
Graf reguler berderajat 3 dengan 10 simpul.
Handshaking: 10 x 3 = 2m -> m = 15 kabel.

---

## 19. Ringkasan Rumus Penting

| Rumus | Keterangan |
|-------|-----------|
| sum deg(v) = 2m | Teorema Handshaking |
| K_n: m = n(n-1)/2 | Sisi graf lengkap |
| K_{m,n}: sisi = mn | Sisi bipartit lengkap |
| Pohon: m = n-1 | Jumlah sisi pohon |
| V - E + F = 2 | Rumus Euler (planar) |
| E <= 3V - 6 | Batas sisi graf planar |
| E <= 2V - 4 | Batas sisi planar bebas segitiga |
| Perfect BT: node = 2^(h+1)-1 | Simpul perfect binary tree |
| Perfect BT: leaf = 2^h | Daun perfect binary tree |
| Full BT: L = I + 1 | Daun vs internal node |
| Cayley: n^(n-2) | Jumlah spanning tree K_n berlabel |
| chi(C_{2k+1}) = 3 | Kromatik siklus ganjil |
| chi(K_n) = n | Kromatik graf lengkap |

---

## 20. Tips Strategi Mengerjakan Soal Graf di OSN

1. **Gambar grafnya!** Banyak soal jadi jelas setelah digambar.

2. **Hitung derajat** sebagai langkah pertama - banyak informasi tersembunyi di sini.

3. **Kenali jenis graf** - apakah ini K_n, bipartit, pohon, atau graf khusus lainnya.

4. **Untuk soal Euler path:** hitung simpul berderajat ganjil. Hanya 3 kemungkinan: 0 (sirkuit), 2 (lintasan), atau lebih (tidak ada).

5. **Untuk soal planaritas:** langsung gunakan rumus E <= 3V - 6.

6. **Untuk soal traversal:** buat tabel langkah demi langkah, jangan terburu-buru.

7. **Untuk rekonstruksi pohon:** root selalu dari pre-order (pertama) atau post-order (terakhir).

8. **Untuk soal pewarnaan:** cek apakah bipartit (chi=2), cari clique terbesar (batas bawah), dan coba greedy coloring.

9. **Jangan lupa sifat pohon:** n-1 sisi, unik path, tambah sisi = buat siklus.

10. **Perhatikan constraint soal:** "graf sederhana" berarti tanpa loop dan tanpa sisi ganda.

---

*Materi ini disiapkan untuk persiapan OSK Informatika 2026. Pelajari teori, pahami contoh,
dan kerjakan latihan secara mandiri untuk penguasaan yang maksimal.*
