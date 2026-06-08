# Materi 04 — Graf & Pohon (Tree)

## 1. Definisi Graf

**Graf G = (V, E):**
- **V** = himpunan simpul (vertex/node)
- **E** = himpunan sisi/busur (edge)

```
    1 --- 2
    |     |
    3 --- 4
```
V = {1, 2, 3, 4}, E = {(1,2), (1,3), (2,4), (3,4)}

---

## 2. Jenis-Jenis Graf

| Jenis | Penjelasan |
|-------|-----------|
| Graf Tak Berarah | Sisi tidak punya arah: (u,v) = (v,u) |
| Graf Berarah (Digraph) | Sisi punya arah: u→v ≠ v→u |
| Graf Berbobot | Setiap sisi memiliki nilai/bobot |
| Graf Lengkap (Kₙ) | Setiap pasang simpul terhubung langsung |
| Graf Bipartit | V dibagi 2 kelompok, sisi hanya antar kelompok |

---

## 3. Terminologi Graf

- **Derajat (degree):** Jumlah sisi yang terhubung ke simpul.
  - Graf berarah: `in-degree` (masuk) dan `out-degree` (keluar)
- **Path (lintasan):** Urutan simpul v₁,v₂,...,vₖ dengan sisi berurutan.
- **Cycle (siklus):** Path yang mulai dan berakhir di simpul yang sama.
- **Connected:** Graf terhubung jika ada path antara setiap pasang simpul.
- **Komponen:** Bagian graf yang terhubung.

**Teorema Handshaking:** Jumlah semua derajat = 2 × |E|

---

## 4. Representasi Graf

### Adjacency Matrix
Matrix n×n, `M[i][j] = 1` jika ada sisi i→j.

```
Graf:  1-2, 1-3, 2-3

     1  2  3
1  [ 0  1  1 ]
2  [ 1  0  1 ]
3  [ 1  1  0 ]
```

### Adjacency List
Setiap simpul menyimpan daftar tetangganya.
```
1: [2, 3]
2: [1, 3]
3: [1, 2]
```

| Representasi | Cek sisi u→v | List tetangga | Space |
|---|---|---|---|
| Matrix | O(1) | O(n) | O(n²) |
| List | O(degree) | O(degree) | O(n+m) |

---

## 5. BFS (Breadth-First Search)

**Algoritma penelusuran melebar** — eksplorasi per lapisan.

**Langkah:**
1. Masukkan simpul awal ke dalam antrian (queue).
2. Keluarkan simpul dari antrian, tandai sebagai dikunjungi.
3. Masukkan semua tetangga yang belum dikunjungi.
4. Ulangi hingga antrian kosong.

**Kegunaan:** Mencari jarak terpendek (unweighted), komponen terhubung.

```
Graf: 1-2, 1-3, 2-4, 3-4, 4-5
BFS dari 1: 1 → 2,3 → 4 → 5
Jarak: d[1]=0, d[2]=1, d[3]=1, d[4]=2, d[5]=3
```

**Kode C++ (BFS):**
```cpp
vector<int> adj[105];
bool visited[105];
int dist[105];

void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    dist[start] = 0;
    
    while (!q.empty()) {
        int u = q.front(); q.pop();
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

---

## 6. DFS (Depth-First Search)

**Algoritma penelusuran mendalam** — eksplorasi sejauh mungkin sebelum kembali.

**Langkah:**
1. Kunjungi simpul awal, tandai dikunjungi.
2. Kunjungi tetangga yang belum dikunjungi secara rekursif.
3. Kembali (backtrack) ketika tidak ada tetangga baru.

**Kegunaan:** Deteksi siklus, topological sort, komponen terhubung.

**Kode C++ (DFS rekursif):**
```cpp
vector<int> adj[105];
bool visited[105];

void dfs(int u) {
    visited[u] = true;
    cout << u << " ";  // proses simpul u
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
        }
    }
}
```

---

## 7. Pohon (Tree)

**Definisi:** Graf terhubung dan tidak memiliki siklus.

**Sifat pohon dengan n simpul:**
- Memiliki tepat **n-1 sisi**
- Terdapat tepat **satu** lintasan antara setiap pasang simpul
- Menambah satu sisi → menciptakan tepat satu siklus

### Terminologi Pohon Berakar (Rooted Tree)
- **Root:** Simpul akar (simpul paling atas)
- **Parent:** Simpul di atas
- **Child:** Simpul di bawah
- **Leaf:** Simpul tanpa anak
- **Depth/Level:** Jarak dari root
- **Height:** Depth terbesar

### Binary Tree
Setiap simpul punya maksimal 2 anak (kiri & kanan).

### Tree Traversal
| Urutan | Proses |
|--------|--------|
| **In-order** | Kiri → Root → Kanan |
| **Pre-order** | Root → Kiri → Kanan |
| **Post-order** | Kiri → Kanan → Root |

**Contoh:**
```
      1
     / \
    2   3
   / \
  4   5

Pre-order:  1, 2, 4, 5, 3
In-order:   4, 2, 5, 1, 3
Post-order: 4, 5, 2, 3, 1
```

---

## 8. Contoh Soal

**Soal 1:** Graf K₅ (lengkap, 5 simpul) memiliki berapa sisi?

> Jawab: C(5,2) = **10 sisi**

**Soal 2:** BFS dari simpul 1 pada graf berikut: 1-2, 1-3, 2-4, 3-5. Tentukan urutan kunjungan.

> Jawab: **1, 2, 3, 4, 5**

**Soal 3:** Pohon dengan 7 simpul memiliki berapa sisi?

> Jawab: **6 sisi** (n-1)

---

## 9. Latihan
1. Gambarkan adjacency matrix untuk graf: {1-2, 2-3, 3-4, 4-1, 1-3}.
2. Lakukan DFS dari simpul 1 pada graf di atas, catat urutan kunjungan.
3. Untuk binary tree pre-order: 1,2,4,5,3,6,7 dan in-order: 4,2,5,1,6,3,7 — gambarkan pohonnya!

*Jawaban di folder `../latihan/`*
