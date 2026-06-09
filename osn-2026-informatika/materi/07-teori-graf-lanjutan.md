# Materi 07 — Teori Graf Lanjutan: Algoritma dan Pemodelan Masalah

## Daftar Isi

1. [Pendahuluan](#1-pendahuluan)
2. [Union-Find (Disjoint Set Union)](#2-union-find-disjoint-set-union)
3. [Minimum Spanning Tree - Kruskal](#3-minimum-spanning-tree---kruskal)
4. [Minimum Spanning Tree - Prim](#4-minimum-spanning-tree---prim)
5. [Dijkstra - Jarak Terpendek](#5-dijkstra---jarak-terpendek)
6. [Bellman-Ford](#6-bellman-ford)
7. [Floyd-Warshall - All-Pairs Shortest Path](#7-floyd-warshall---all-pairs-shortest-path)
8. [Topological Sort](#8-topological-sort)
9. [DAG DP - Dynamic Programming pada DAG](#9-dag-dp---dynamic-programming-pada-dag)
10. [Grid DP - DP pada Graf Grid](#10-grid-dp---dp-pada-graf-grid)
11. [Graf Bipartit](#11-graf-bipartit)
12. [Strongly Connected Components](#12-strongly-connected-components)
13. [Network Flow - Konsep Dasar](#13-network-flow---konsep-dasar)
14. [Pemodelan Graf - Mengubah Soal Cerita ke Graf](#14-pemodelan-graf---mengubah-soal-cerita-ke-graf)
15. [Ringkasan Pemilihan Algoritma](#15-ringkasan-pemilihan-algoritma)
16. [Contoh Soal dan Pembahasan](#16-contoh-soal-dan-pembahasan)
17. [Latihan](#17-latihan)

---

## 1. Pendahuluan

Pada Bab 4 kita telah mempelajari konsep dasar graf: representasi, BFS, DFS, pohon, dan komponen terhubung. Bab ini membahas teknik lanjutan yang sangat sering muncul di OSK/OSP Informatika:

- **Shortest Path**: Dijkstra, Bellman-Ford, Floyd-Warshall
- **Minimum Spanning Tree**: Kruskal dan Prim
- **Topological Sort**: DFS-based dan Kahn's Algorithm
- **DAG DP**: Menghitung lintasan, jarak terpendek/terpanjang pada DAG
- **Grid DP**: DP pada graf berbentuk grid
- **Bipartite Graph**: Pengecekan dan penerapan
- **SCC dan Network Flow**: Konsep dasar untuk wawasan

**Kunci keberhasilan**: Kenali pola masalah, modelkan sebagai graf, lalu pilih algoritma yang tepat.

---

## 2. Union-Find (Disjoint Set Union)

### 2.1 Konsep

Union-Find adalah struktur data yang mengelola kumpulan himpunan terpisah (disjoint sets). Dua operasi utama:
- **Find(x)**: Mencari representatif (root) dari himpunan yang mengandung x
- **Union(x, y)**: Menggabungkan himpunan yang mengandung x dan y

### 2.2 Implementasi dengan Path Compression dan Union by Rank

```cpp
int parent[100005];
int rnk[100005]; // rank

void init(int n) {
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        rnk[i] = 0;
    }
}

int find(int x) {
    if (parent[x] != x)
        parent[x] = find(parent[x]); // path compression
    return parent[x];
}

void unite(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) return;
    // union by rank
    if (rnk[px] < rnk[py]) swap(px, py);
    parent[py] = px;
    if (rnk[px] == rnk[py]) rnk[px]++;
}

bool connected(int x, int y) {
    return find(x) == find(y);
}
```

### 2.3 Kompleksitas

- Find dan Union: hampir O(1) amortized (tepatnya O(alpha(n)) dengan inverse Ackermann)
- Inisialisasi: O(n)

### 2.4 Kapan Menggunakan Union-Find?

- Mendeteksi apakah penambahan edge membentuk siklus
- Menghitung jumlah komponen terhubung secara dinamis
- Digunakan dalam algoritma Kruskal

---

## 3. Minimum Spanning Tree - Kruskal

### 3.1 Definisi MST

**Minimum Spanning Tree (MST)** adalah subgraf dari graf berbobot tak berarah yang:
- Menghubungkan semua simpul (spanning)
- Tidak ada siklus (tree)
- Total bobot edge minimum

### 3.2 Langkah Algoritma Kruskal

1. Urutkan semua edge berdasarkan bobot dari kecil ke besar
2. Untuk setiap edge (dalam urutan):
   - Jika kedua ujung belum terhubung (cek dengan Union-Find), tambahkan edge ke MST
   - Jika sudah terhubung, lewati (karena akan membentuk siklus)
3. Berhenti saat MST memiliki tepat (n-1) edge

### 3.3 Trace Contoh

**Graf:**
```
Simpul: {A, B, C, D, E}
Edge (bobot):
  A-B: 4
  A-C: 2
  B-C: 1
  B-D: 5
  C-D: 8
  C-E: 10
  D-E: 3
```

**Langkah Kruskal:**

| Langkah | Edge | Bobot | Aksi | Alasan |
|---------|------|-------|------|--------|
| 1 | B-C | 1 | Tambah | B dan C belum terhubung |
| 2 | A-C | 2 | Tambah | A dan C belum terhubung |
| 3 | D-E | 3 | Tambah | D dan E belum terhubung |
| 4 | A-B | 4 | Lewati | A dan B sudah terhubung (via C) |
| 5 | B-D | 5 | Tambah | B dan D belum terhubung |
| 6 | - | - | Selesai | Sudah 4 edge = n-1 |

**MST**: {B-C, A-C, D-E, B-D}, total bobot = 1+2+3+5 = **11**

### 3.4 Kode C++

```cpp
struct Edge {
    int u, v, w;
    bool operator<(const Edge& o) const { return w < o.w; }
};

int kruskal(int n, vector<Edge>& edges) {
    sort(edges.begin(), edges.end());
    init(n); // inisialisasi Union-Find
    int totalWeight = 0, edgeCount = 0;
    
    for (auto& e : edges) {
        if (!connected(e.u, e.v)) {
            unite(e.u, e.v);
            totalWeight += e.w;
            edgeCount++;
            if (edgeCount == n - 1) break;
        }
    }
    return totalWeight;
}
```

### 3.5 Kompleksitas

- Sorting: O(E log E)
- Union-Find: O(E * alpha(V))
- Total: O(E log E)

---

## 4. Minimum Spanning Tree - Prim

### 4.1 Langkah Algoritma Prim

1. Mulai dari satu simpul (misalnya simpul 1)
2. Masukkan semua edge dari simpul tersebut ke priority queue
3. Ambil edge berbobot terkecil yang menghubungkan ke simpul yang belum dikunjungi
4. Tandai simpul baru sebagai dikunjungi, masukkan edge-edgenya ke priority queue
5. Ulangi sampai semua simpul terhubung

### 4.2 Kode C++

```cpp
int prim(int n, vector<pair<int,int>> adj[]) {
    // adj[u] = {{v, w}, ...}
    vector<bool> inMST(n+1, false);
    // {bobot, simpul}
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    
    pq.push({0, 1}); // mulai dari simpul 1
    int totalWeight = 0;
    
    while (!pq.empty()) {
        auto [w, u] = pq.top(); pq.pop();
        if (inMST[u]) continue;
        inMST[u] = true;
        totalWeight += w;
        
        for (auto [v, wt] : adj[u]) {
            if (!inMST[v]) {
                pq.push({wt, v});
            }
        }
    }
    return totalWeight;
}
```

### 4.3 Perbandingan Kruskal vs Prim

| Aspek | Kruskal | Prim |
|-------|---------|------|
| Pendekatan | Greedy pada edge | Greedy pada simpul |
| Struktur data | Union-Find | Priority Queue |
| Cocok untuk | Graf jarang (E kecil) | Graf padat (E besar) |
| Kompleksitas | O(E log E) | O(E log V) |
| Implementasi | Lebih mudah | Sedikit lebih kompleks |

---

## 5. Dijkstra - Jarak Terpendek

### 5.1 Definisi Masalah

Diberikan graf berbobot dengan bobot non-negatif. Cari jarak terpendek dari satu simpul sumber ke semua simpul lainnya.

### 5.2 Langkah Algoritma

1. Set jarak semua simpul = tak hingga, kecuali sumber = 0
2. Masukkan sumber ke priority queue
3. Ambil simpul dengan jarak terkecil dari priority queue
4. Untuk setiap tetangga, jika jarak via simpul ini lebih pendek, perbarui
5. Ulangi sampai priority queue kosong

### 5.3 Trace Contoh Lengkap

**Graf:**
```
Simpul: {1, 2, 3, 4, 5}
Edge (bobot):
  1->2: 4
  1->3: 2
  2->3: 5
  2->4: 10
  3->2: 1
  3->4: 8
  3->5: 2
  4->5: 6
  5->4: 3
```

**Sumber = simpul 1**

| Langkah | Proses | dist[1] | dist[2] | dist[3] | dist[4] | dist[5] |
|---------|--------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf |
| 1 | Kunjungi 1 | 0 | 4 | 2 | inf | inf |
| 2 | Kunjungi 3 (dist=2) | 0 | 3 | 2 | 10 | 4 |
| 3 | Kunjungi 2 (dist=3) | 0 | 3 | 2 | 10 | 4 |
| 4 | Kunjungi 5 (dist=4) | 0 | 3 | 2 | 7 | 4 |
| 5 | Kunjungi 4 (dist=7) | 0 | 3 | 2 | 7 | 4 |

**Penjelasan langkah 2:**
- Kunjungi simpul 3 (jarak 2, terkecil di PQ)
- Dari 3 ke 2: dist[2] = min(4, 2+1) = 3 (update!)
- Dari 3 ke 4: dist[4] = min(inf, 2+8) = 10 (update!)
- Dari 3 ke 5: dist[5] = min(inf, 2+2) = 4 (update!)

**Penjelasan langkah 4:**
- Kunjungi simpul 5 (jarak 4)
- Dari 5 ke 4: dist[4] = min(10, 4+3) = 7 (update!)

**Hasil akhir:** dist = [0, 3, 2, 7, 4]

### 5.4 Kode C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
vector<pair<int,int>> adj[100005]; // {tetangga, bobot}
int dist_arr[100005];
bool visited[100005];

void dijkstra(int start, int n) {
    fill(dist_arr + 1, dist_arr + n + 1, INF);
    memset(visited, false, sizeof(visited));
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    
    dist_arr[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (visited[u]) continue;
        visited[u] = true;
        
        for (auto [v, w] : adj[u]) {
            if (dist_arr[u] + w < dist_arr[v]) {
                dist_arr[v] = dist_arr[u] + w;
                pq.push({dist_arr[v], v});
            }
        }
    }
}
```

### 5.5 Kompleksitas

- Dengan priority queue (binary heap): O((V + E) log V)
- Syarat: semua bobot edge >= 0

### 5.6 Kesalahan Umum

- Menggunakan Dijkstra pada graf dengan bobot negatif (SALAH, gunakan Bellman-Ford)
- Lupa mengecek `if (visited[u]) continue;` sehingga memproses simpul berkali-kali
- Menggunakan jarak integer tapi lupa set INF cukup besar

---

## 6. Bellman-Ford

### 6.1 Kapan Digunakan?

- Ketika graf memiliki edge berbobot **negatif**
- Untuk mendeteksi **siklus negatif** (negative cycle)

### 6.2 Langkah Algoritma

1. Set jarak semua simpul = tak hingga, kecuali sumber = 0
2. Ulangi (V-1) kali:
   - Untuk setiap edge (u, v, w): jika dist[u] + w < dist[v], update dist[v]
3. Lakukan satu iterasi tambahan: jika masih ada update, berarti ada siklus negatif

### 6.3 Contoh

**Graf (V=4):**
```
1->2: 1
1->3: 4
2->3: -2
3->4: 3
2->4: 5
```

| Iterasi | dist[1] | dist[2] | dist[3] | dist[4] |
|---------|---------|---------|---------|---------|
| Init | 0 | inf | inf | inf |
| 1 | 0 | 1 | -1 | 2 |
| 2 | 0 | 1 | -1 | 2 |
| 3 | 0 | 1 | -1 | 2 |

Iterasi ke-2 dan ke-3 tidak ada perubahan, jadi tidak ada siklus negatif.

Hasil: dist = [0, 1, -1, 2]

### 6.4 Kode C++

```cpp
struct Edge { int u, v, w; };

bool bellmanFord(int start, int n, vector<Edge>& edges) {
    vector<int> dist(n+1, INF);
    dist[start] = 0;
    
    // relax (n-1) kali
    for (int i = 0; i < n - 1; i++) {
        for (auto& e : edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
            }
        }
    }
    
    // deteksi siklus negatif
    for (auto& e : edges) {
        if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
            return true; // ada siklus negatif
        }
    }
    return false;
}
```

### 6.5 Kompleksitas

- O(V * E) - lebih lambat dari Dijkstra tetapi bisa menangani bobot negatif

---

## 7. Floyd-Warshall - All-Pairs Shortest Path

### 7.1 Kapan Digunakan?

- Mencari jarak terpendek antara **semua pasang simpul**
- Graf berukuran kecil (V <= 500)
- Bisa menangani bobot negatif (selama tidak ada siklus negatif)

### 7.2 Ide Algoritma

`dist[i][j]` = jarak terpendek dari i ke j, menggunakan simpul-simpul antara {1, 2, ..., k} sebagai simpul perantara.

Relasi rekursif:
```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### 7.3 Trace Contoh

**Graf (V=4):**
```
    1   2   3   4
1 [ 0   3  inf  7 ]
2 [ 8   0   2  inf]
3 [ 5  inf  0   1 ]
4 [ 2  inf inf  0 ]
```

**k=1 (perantara simpul 1):**
```
dist[2][3] = min(2, dist[2][1]+dist[1][3]) = min(2, 8+inf) = 2
dist[2][4] = min(inf, dist[2][1]+dist[1][4]) = min(inf, 8+7) = 15
dist[3][2] = min(inf, dist[3][1]+dist[1][2]) = min(inf, 5+3) = 8
dist[3][4] = min(1, dist[3][1]+dist[1][4]) = min(1, 5+7) = 1
dist[4][2] = min(inf, dist[4][1]+dist[1][2]) = min(inf, 2+3) = 5
dist[4][3] = min(inf, dist[4][1]+dist[1][3]) = min(inf, 2+inf) = inf
```

Setelah k=1:
```
    1   2   3   4
1 [ 0   3  inf  7 ]
2 [ 8   0   2   15]
3 [ 5   8   0   1 ]
4 [ 2   5  inf  0 ]
```

**k=2 (perantara simpul 1,2):**
```
dist[1][3] = min(inf, dist[1][2]+dist[2][3]) = min(inf, 3+2) = 5
dist[3][4] = min(1, dist[3][2]+dist[2][4]) = min(1, 8+15) = 1
dist[4][3] = min(inf, dist[4][2]+dist[2][3]) = min(inf, 5+2) = 7
```

Setelah k=2:
```
    1   2   3   4
1 [ 0   3   5   7 ]
2 [ 8   0   2   15]
3 [ 5   8   0   1 ]
4 [ 2   5   7   0 ]
```

**k=3:**
```
dist[1][4] = min(7, dist[1][3]+dist[3][4]) = min(7, 5+1) = 6
dist[2][4] = min(15, dist[2][3]+dist[3][4]) = min(15, 2+1) = 3
dist[2][1] = min(8, dist[2][3]+dist[3][1]) = min(8, 2+5) = 7
dist[4][4] = tetap 0
```

Setelah k=3:
```
    1   2   3   4
1 [ 0   3   5   6 ]
2 [ 7   0   2   3 ]
3 [ 5   8   0   1 ]
4 [ 2   5   7   0 ]
```

**k=4:**
```
dist[1][1] = min(0, dist[1][4]+dist[4][1]) = min(0, 6+2) = 0
dist[2][1] = min(7, dist[2][4]+dist[4][1]) = min(7, 3+2) = 5
dist[3][2] = min(8, dist[3][4]+dist[4][2]) = min(8, 1+5) = 6
```

**Hasil akhir:**
```
    1   2   3   4
1 [ 0   3   5   6 ]
2 [ 5   0   2   3 ]
3 [ 3   6   0   1 ]
4 [ 2   5   7   0 ]
```

### 7.4 Kode C++

```cpp
int dist[505][505];

void floydWarshall(int n) {
    // inisialisasi: dist[i][j] = bobot edge i->j, atau INF jika tidak ada edge
    // dist[i][i] = 0
    
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}
```

### 7.5 Kompleksitas

- Waktu: O(V^3)
- Memori: O(V^2)

---

## 8. Topological Sort

### 8.1 Definisi

Topological sort menghasilkan urutan linear simpul-simpul DAG (Directed Acyclic Graph) sedemikian rupa sehingga untuk setiap edge u->v, simpul u muncul sebelum simpul v dalam urutan tersebut.

**Contoh penggunaan:**
- Urutan mata kuliah berdasarkan prasyarat
- Urutan kompilasi modul
- Urutan tugas berdasarkan dependensi

### 8.2 Metode 1: DFS-Based

**Ide:** Lakukan DFS, setelah semua anak selesai dikunjungi, masukkan simpul ke stack. Hasil topological sort adalah urutan terbalik dari stack.

```cpp
vector<int> adj[100005];
bool visited[100005];
stack<int> topoStack;

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v);
    }
    topoStack.push(u); // setelah semua anak selesai
}

vector<int> topoSortDFS(int n) {
    memset(visited, false, sizeof(visited));
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) dfs(i);
    }
    vector<int> result;
    while (!topoStack.empty()) {
        result.push_back(topoStack.top());
        topoStack.pop();
    }
    return result;
}
```

### 8.3 Metode 2: Kahn's Algorithm (BFS-Based)

**Ide:** Proses simpul-simpul yang in-degree-nya 0 terlebih dahulu. Setelah memproses, kurangi in-degree tetangganya.

```cpp
vector<int> kahnTopoSort(int n, vector<int> adj[]) {
    vector<int> indegree(n+1, 0);
    for (int u = 1; u <= n; u++)
        for (int v : adj[u])
            indegree[v]++;
    
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (indegree[i] == 0) q.push(i);
    
    vector<int> order;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            indegree[v]--;
            if (indegree[v] == 0) q.push(v);
        }
    }
    // jika order.size() < n, berarti ada siklus!
    return order;
}
```

### 8.4 Trace Contoh (Kahn's Algorithm)

**DAG:**
```
Simpul: {1, 2, 3, 4, 5, 6}
Edge: 1->2, 1->3, 2->4, 3->4, 3->5, 4->6, 5->6
```

**Hitung in-degree:**
- simpul 1: 0
- simpul 2: 1 (dari 1)
- simpul 3: 1 (dari 1)
- simpul 4: 2 (dari 2, 3)
- simpul 5: 1 (dari 3)
- simpul 6: 2 (dari 4, 5)

| Langkah | Queue | Proses | In-degree update | Hasil |
|---------|-------|--------|------------------|-------|
| Init | [1] | - | - | [] |
| 1 | [2,3] | 1 | indeg[2]=0, indeg[3]=0 | [1] |
| 2 | [3,4] | 2 | indeg[4]=1 | [1,2] |
| 3 | [4,5] | 3 | indeg[4]=0, indeg[5]=0 | [1,2,3] |
| 4 | [5,6] | 4 | indeg[6]=1 | [1,2,3,4] |
| 5 | [6] | 5 | indeg[6]=0 | [1,2,3,4,5] |
| 6 | [] | 6 | - | [1,2,3,4,5,6] |

**Topological order:** 1, 2, 3, 4, 5, 6

### 8.5 Deteksi Siklus dengan Topological Sort

Jika `order.size() < n`, berarti ada siklus dalam graf (tidak semua simpul bisa diproses karena in-degree-nya tidak pernah menjadi 0).

---

## 9. DAG DP - Dynamic Programming pada DAG

### 9.1 Prinsip Dasar

Pada DAG, kita bisa melakukan DP mengikuti urutan topologis. Ini memungkinkan kita menghitung:
- Jumlah lintasan dari sumber ke tujuan
- Lintasan terpendek/terpanjang
- Jumlah lintasan dengan constraint tertentu

### 9.2 Menghitung Jumlah Lintasan

**Masalah:** Berapa banyak lintasan berbeda dari simpul s ke simpul t di DAG?

```
dp[v] = jumlah lintasan dari s ke v
dp[s] = 1
dp[v] = sum of dp[u] untuk semua u yang memiliki edge u->v
```

**Kode C++:**
```cpp
long long countPaths(int s, int t, int n, vector<int> adj[]) {
    vector<int> order = kahnTopoSort(n, adj);
    vector<long long> dp(n+1, 0);
    dp[s] = 1;
    
    for (int u : order) {
        for (int v : adj[u]) {
            dp[v] += dp[u];
        }
    }
    return dp[t];
}
```

### 9.3 Lintasan Terpanjang (Longest Path)

**Masalah:** Cari lintasan dengan total bobot terbesar dari s ke t di DAG.

```
dp[v] = panjang lintasan terpanjang dari s ke v
dp[s] = 0
dp[v] = max(dp[u] + w(u,v)) untuk semua u yang memiliki edge u->v
```

**Kode C++:**
```cpp
int longestPath(int s, int t, int n, vector<pair<int,int>> adj[]) {
    vector<int> order = kahnTopoSort(n, /* ... */);
    vector<int> dp(n+1, -INF);
    dp[s] = 0;
    
    for (int u : order) {
        if (dp[u] == -INF) continue;
        for (auto [v, w] : adj[u]) {
            dp[v] = max(dp[v], dp[u] + w);
        }
    }
    return dp[t];
}
```

### 9.4 Jarak Terpendek di DAG

Sama seperti lintasan terpanjang, tetapi menggunakan min:

```
dp[v] = min(dp[u] + w(u,v)) untuk semua u yang memiliki edge u->v
```

Ini lebih efisien dari Dijkstra karena O(V+E).

### 9.5 Contoh: Menghitung Lintasan dengan Constraint

**Masalah:** Di DAG, berapa banyak lintasan dari 1 ke n yang melewati tepat k edge?

```cpp
// dp[v][j] = jumlah lintasan dari 1 ke v yang melewati tepat j edge
long long dp[1005][105];

void solve(int n, int k, vector<int> adj[]) {
    memset(dp, 0, sizeof(dp));
    dp[1][0] = 1;
    
    vector<int> order = kahnTopoSort(n, adj);
    for (int u : order) {
        for (int j = 0; j < k; j++) {
            if (dp[u][j] == 0) continue;
            for (int v : adj[u]) {
                dp[v][j+1] += dp[u][j];
            }
        }
    }
    // jawaban = dp[n][k]
}
```

---

## 10. Grid DP - DP pada Graf Grid

### 10.1 Konsep Grid sebagai Graf

Grid berukuran R x C bisa dianggap sebagai graf dimana:
- Setiap sel (i,j) adalah simpul
- Edge menghubungkan sel-sel yang bertetangga (sesuai aturan gerakan)

Jika gerakan hanya ke kanan/bawah, grid menjadi DAG.

### 10.2 Pola Dasar: Jumlah Lintasan di Grid

**Masalah:** Dari (0,0) ke (R-1,C-1), hanya boleh bergerak kanan atau bawah. Berapa banyak lintasan?

```
dp[i][j] = jumlah lintasan dari (0,0) ke (i,j)
dp[0][0] = 1
dp[i][0] = 1 (hanya bisa dari atas)
dp[0][j] = 1 (hanya bisa dari kiri)
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

**Contoh (grid 3x3):**
```
dp:
1  1  1
1  2  3
1  3  6
```

Jawaban: dp[2][2] = 6 lintasan.

### 10.3 Grid dengan Obstacle

Jika ada sel yang diblokir:
```cpp
int countPaths(int R, int C, bool blocked[][105]) {
    int dp[105][105] = {};
    dp[0][0] = blocked[0][0] ? 0 : 1;
    
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (blocked[i][j]) { dp[i][j] = 0; continue; }
            if (i > 0) dp[i][j] += dp[i-1][j];
            if (j > 0) dp[i][j] += dp[i][j-1];
        }
    }
    return dp[R-1][C-1];
}
```

### 10.4 Grid dengan Bobot (Maksimum/Minimum)

**Masalah:** Setiap sel memiliki nilai. Cari lintasan dari pojok kiri atas ke pojok kanan bawah dengan total nilai maksimum.

```cpp
int maxPathSum(int R, int C, int grid[][105]) {
    int dp[105][105];
    dp[0][0] = grid[0][0];
    
    for (int i = 1; i < R; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
    for (int j = 1; j < C; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
    
    for (int i = 1; i < R; i++)
        for (int j = 1; j < C; j++)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j];
    
    return dp[R-1][C-1];
}
```

### 10.5 Grid DP dengan 4 Arah

Jika gerakan bisa ke 4 arah (atas, bawah, kiri, kanan), grid bukan DAG lagi. Gunakan BFS/Dijkstra sebagai gantinya.

**Masalah:** Cari jarak minimum dari (0,0) ke (R-1,C-1) di grid berbobot.

```cpp
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int gridDijkstra(int R, int C, int grid[][105]) {
    vector<vector<int>> dist(R, vector<int>(C, INF));
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
    
    dist[0][0] = grid[0][0];
    pq.push({grid[0][0], 0, 0});
    
    while (!pq.empty()) {
        auto [d, x, y] = pq.top(); pq.pop();
        if (d > dist[x][y]) continue;
        
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
            int nd = d + grid[nx][ny];
            if (nd < dist[nx][ny]) {
                dist[nx][ny] = nd;
                pq.push({nd, nx, ny});
            }
        }
    }
    return dist[R-1][C-1];
}
```

---

## 11. Graf Bipartit

### 11.1 Definisi

Graf bipartit adalah graf yang simpul-simpulnya bisa dibagi menjadi dua himpunan, sedemikian rupa sehingga setiap edge menghubungkan simpul dari himpunan yang berbeda.

**Sifat penting:** Graf adalah bipartit jika dan hanya jika **tidak mengandung siklus dengan panjang ganjil**.

### 11.2 Pengecekan Bipartit dengan BFS Coloring

**Ide:** Warnai graf dengan 2 warna. Jika ada edge yang menghubungkan dua simpul berwarna sama, graf tidak bipartit.

```cpp
int color[100005]; // -1 = belum diwarnai, 0 atau 1

bool isBipartite(int n, vector<int> adj[]) {
    memset(color, -1, sizeof(color));
    
    for (int start = 1; start <= n; start++) {
        if (color[start] != -1) continue;
        
        queue<int> q;
        q.push(start);
        color[start] = 0;
        
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (color[v] == -1) {
                    color[v] = 1 - color[u]; // warna berbeda
                    q.push(v);
                } else if (color[v] == color[u]) {
                    return false; // tidak bipartit
                }
            }
        }
    }
    return true;
}
```

### 11.3 Trace Contoh

**Graf bipartit:**
```
1-2, 1-4, 3-2, 3-4, 5-2
```

| Langkah | Proses | Warna |
|---------|--------|-------|
| Init | Mulai dari 1 | color[1] = 0 |
| 1 | Tetangga 1: 2, 4 | color[2] = 1, color[4] = 1 |
| 2 | Tetangga 2: 1, 3, 5 | color[3] = 0, color[5] = 0 |
| 3 | Tetangga 4: 1, 3 | 1 sudah 0 (OK), 3 sudah 0 (OK) |
| 4 | Tetangga 3: 2, 4 | 2 sudah 1 (OK), 4 sudah 1 (OK) |
| 5 | Tetangga 5: 2 | 2 sudah 1 (OK) |

Hasil: Bipartit! Himpunan A = {1, 3, 5}, Himpunan B = {2, 4}

**Graf TIDAK bipartit (segitiga):**
```
1-2, 2-3, 3-1
```
- color[1] = 0, color[2] = 1, color[3] = 0
- Tapi edge 3-1: color[3] = 0 == color[1] = 0 --> TIDAK bipartit!

### 11.4 Aplikasi Graf Bipartit di OSN

- **Pencocokan (matching):** Menugaskan orang ke pekerjaan
- **Pewarnaan:** Memeriksa apakah suatu graf bisa diwarnai 2 warna
- **Partisi:** Membagi objek menjadi 2 kelompok tanpa konflik

---

## 12. Strongly Connected Components

### 12.1 Definisi

Pada graf berarah, **Strongly Connected Component (SCC)** adalah subgraf maksimal dimana setiap pasang simpul u, v bisa dijangkau satu sama lain (ada lintasan u ke v DAN v ke u).

### 12.2 Konsep Kosaraju's Algorithm

1. Lakukan DFS pada graf asli, catat urutan finish time
2. Buat graf transpose (balik semua edge)
3. Lakukan DFS pada graf transpose sesuai urutan finish time terbalik
4. Setiap DFS tree di langkah 3 adalah satu SCC

### 12.3 Contoh

**Graf:**
```
1->2, 2->3, 3->1, 3->4, 4->5, 5->6, 6->4
```

**SCC yang terbentuk:**
- SCC 1: {1, 2, 3} (1->2->3->1)
- SCC 2: {4, 5, 6} (4->5->6->4)

### 12.4 Penerapan di OSN

- Biasanya muncul sebagai soal "berapa banyak kelompok simpul yang saling terjangkau?"
- Kondenasi SCC menghasilkan DAG (bisa dilanjutkan dengan DAG DP)
- Jarang implementasi penuh, lebih sering konseptual di OSK

---

## 13. Network Flow - Konsep Dasar

### 13.1 Definisi

Network flow memodelkan aliran dalam jaringan:
- Ada sumber (source) s dan muara (sink) t
- Setiap edge memiliki kapasitas maksimum
- Tujuan: memaksimalkan aliran dari s ke t

### 13.2 Max-Flow Min-Cut Theorem

**Teorema:** Aliran maksimum dari s ke t sama dengan kapasitas minimum cut yang memisahkan s dan t.

### 13.3 Kapan Muncul di OSN?

Di level OSK, biasanya muncul sebagai soal konseptual:
- "Berapa banyak lintasan terpisah-edge dari A ke B?"
- "Berapa minimum edge yang harus dihapus agar A dan B terputus?"
- Jawaban: keduanya sama (Max-Flow = Min-Cut)

### 13.4 Contoh Sederhana

**Jaringan:**
```
s -> a (kapasitas 3)
s -> b (kapasitas 2)
a -> t (kapasitas 2)
a -> b (kapasitas 1)
b -> t (kapasitas 3)
```

**Max flow = 4** (3 dari s via a dan b, 2 dari s langsung ke b->t)
- Aliran: s->a->t = 2, s->a->b->t = 1, s->b->t = 1
- Total: 2 + 1 + 1 = 4

Perhatikan: aliran keluar s = 3+2 = 5 (kapasitas), tapi bottleneck ada di lain tempat.
Cek ulang: s->a = 2+1 = 3 (OK, kapasitas 3), s->b = 1 (kapasitas 2, OK), a->t = 2 (kapasitas 2, OK), a->b = 1 (kapasitas 1, OK), b->t = 1+1 = 2 (kapasitas 3, OK). Total masuk t = 2+2 = 4.

---

## 14. Pemodelan Graf - Mengubah Soal Cerita ke Graf

### 14.1 Pola Pemodelan Umum

| Situasi | Model Graf |
|---------|-----------|
| Kota dan jalan | Simpul = kota, edge = jalan |
| Jadwal dan konflik | Simpul = kegiatan, edge = konflik waktu |
| Prasyarat | Simpul = tugas, edge berarah = dependensi |
| Pertemanan | Simpul = orang, edge = kenal |
| Grid/papan catur | Simpul = sel, edge = gerakan yang diizinkan |
| State dan transisi | Simpul = state, edge = aksi |

### 14.2 Contoh Pemodelan 1: Labirin

**Soal:** Labirin 5x5, cari jarak terpendek dari pintu masuk ke pintu keluar. Karakter '#' = dinding, '.' = bisa dilewati.

**Model:**
- Simpul: setiap sel '.' pada grid
- Edge: antara dua sel '.' yang bertetangga (4 arah)
- Algoritma: BFS (karena tak berbobot)

### 14.3 Contoh Pemodelan 2: Transformasi Kata

**Soal:** Diberikan kata awal "cat" dan kata akhir "dog". Setiap langkah boleh mengganti tepat 1 huruf. Semua kata perantara harus valid. Cari langkah minimum.

**Model:**
- Simpul: setiap kata valid
- Edge: antara dua kata yang berbeda tepat 1 huruf
- Algoritma: BFS

### 14.4 Contoh Pemodelan 3: Tugas dengan Deadline

**Soal:** Ada n tugas, masing-masing dengan durasi dan deadline. Beberapa tugas punya prasyarat. Cari urutan pengerjaan yang memenuhi semua prasyarat.

**Model:**
- Simpul: setiap tugas
- Edge berarah: tugas A harus dikerjakan sebelum tugas B
- Algoritma: Topological Sort

### 14.5 Contoh Pemodelan 4: Perjalanan dengan Transfer

**Soal:** Ada beberapa rute bus. Setiap rute punya beberapa halte. Perpindahan antar rute bisa dilakukan di halte yang sama. Cari minimum transfer dari halte X ke halte Y.

**Model:**
- Simpul: pasangan (halte, rute)
- Edge bobot 0: antar halte yang berurutan dalam satu rute
- Edge bobot 1: antar rute di halte yang sama (transfer)
- Algoritma: BFS 0-1 atau Dijkstra

---

## 15. Ringkasan Pemilihan Algoritma

### Tabel Keputusan

| Masalah | Kondisi | Algoritma | Kompleksitas |
|---------|---------|-----------|-------------|
| Shortest path | Tak berbobot | BFS | O(V+E) |
| Shortest path | Bobot >= 0 | Dijkstra | O((V+E) log V) |
| Shortest path | Bobot negatif | Bellman-Ford | O(V*E) |
| Shortest path | All-pairs, V kecil | Floyd-Warshall | O(V^3) |
| Shortest path | DAG | DAG DP (topological order) | O(V+E) |
| Longest path | DAG | DAG DP (topological order) | O(V+E) |
| Longest path | Graf umum | NP-hard (backtracking) | Eksponensial |
| MST | Graf jarang | Kruskal | O(E log E) |
| MST | Graf padat | Prim | O(E log V) |
| Jumlah path | DAG | DAG DP | O(V+E) |
| Bipartite check | - | BFS coloring | O(V+E) |
| Topological sort | DAG | Kahn / DFS | O(V+E) |
| SCC | Graf berarah | Kosaraju / Tarjan | O(V+E) |
| Max flow | - | Ford-Fulkerson / Dinic | O(V*E^2) |
| Deteksi siklus | Graf berarah | DFS coloring | O(V+E) |
| Connected comp. | Tak berarah | BFS / DFS / Union-Find | O(V+E) |
| Grid shortest | 4 arah, bobot sama | BFS | O(R*C) |
| Grid shortest | 4 arah, berbobot | Dijkstra di grid | O(RC log(RC)) |
| Grid path count | Kanan/bawah | DP 2D | O(R*C) |

### Checklist Pemilihan

1. **Apakah graf berbobot?**
   - Tidak: gunakan BFS
   - Ya: lanjut ke 2
2. **Ada bobot negatif?**
   - Tidak: Dijkstra
   - Ya: Bellman-Ford (atau Floyd-Warshall jika all-pairs)
3. **Apakah DAG?**
   - Ya: DAG DP (lebih efisien dari Dijkstra)
4. **Butuh MST?**
   - Ya: Kruskal (graf jarang) atau Prim (graf padat)
5. **Butuh urutan dependensi?**
   - Ya: Topological Sort

---

## 16. Contoh Soal dan Pembahasan

### Contoh 1: MST dengan Kruskal

**Soal:** Kota A, B, C, D, E dihubungkan jalan dengan biaya: A-B:7, A-D:5, B-C:8, B-D:9, B-E:7, C-E:5, D-E:15. Cari biaya minimum untuk menghubungkan semua kota.

**Pembahasan:**
1. Urutkan edge: C-E(5), A-D(5), A-B(7), B-E(7), B-C(8), B-D(9), D-E(15)
2. C-E(5): tambah (C dan E belum terhubung)
3. A-D(5): tambah (A dan D belum terhubung)
4. A-B(7): tambah (A dan B belum terhubung)
5. B-E(7): tambah (B dan E belum terhubung, via C-E sekarang semua terhubung)

Tunggu, setelah langkah 4: komponen {A,B,D} dan {C,E}
- B-E(7): menghubungkan {A,B,D} dan {C,E} -> tambah!

MST = {C-E, A-D, A-B, B-E}, total = 5+5+7+7 = **24**

---

### Contoh 2: Dijkstra Step-by-Step

**Soal:** Cari jarak terpendek dari A ke semua simpul di graf berikut:
```
A-B:1, A-C:4, B-C:2, B-D:5, C-D:1, C-E:3, D-E:2
```

**Pembahasan:**

| Langkah | Kunjungi | dist[A] | dist[B] | dist[C] | dist[D] | dist[E] |
|---------|----------|---------|---------|---------|---------|---------|
| Init | - | 0 | inf | inf | inf | inf |
| 1 | A | 0 | 1 | 4 | inf | inf |
| 2 | B | 0 | 1 | 3 | 6 | inf |
| 3 | C | 0 | 1 | 3 | 4 | 6 |
| 4 | D | 0 | 1 | 3 | 4 | 6 |
| 5 | E | 0 | 1 | 3 | 4 | 6 |

Langkah 2: Kunjungi B (dist=1). Update: C = min(4, 1+2)=3, D = min(inf, 1+5)=6
Langkah 3: Kunjungi C (dist=3). Update: D = min(6, 3+1)=4, E = min(inf, 3+3)=6

**Jawaban:** dist = [A:0, B:1, C:3, D:4, E:6]

---

### Contoh 3: Topological Sort

**Soal:** Mata kuliah dan prasyaratnya: Kalkulus 1 (K1), Kalkulus 2 (K2 butuh K1), Fisika 1 (F1 butuh K1), Fisika 2 (F2 butuh F1 dan K2), Aljabar (A), Statistika (S butuh K2 dan A). Tentukan urutan pengambilan yang valid.

**Pembahasan:**
- Edge: K1->K2, K1->F1, K2->F2, F1->F2, K2->S, A->S
- In-degree: K1=0, A=0, K2=1, F1=1, F2=2, S=2
- Kahn: mulai dari K1, A (in-degree 0)
- Proses K1: K2 jadi 0, F1 jadi 0
- Proses A: S jadi 1
- Proses K2: F2 jadi 1, S jadi 0
- Proses F1: F2 jadi 0
- Proses S
- Proses F2

**Urutan valid:** K1, A, K2, F1, S, F2

---

### Contoh 4: Jumlah Lintasan di DAG

**Soal:** Di DAG dengan edge: 1->2, 1->3, 2->4, 2->5, 3->4, 3->5, 4->6, 5->6. Berapa banyak lintasan dari 1 ke 6?

**Pembahasan:**
```
dp[1] = 1
dp[2] = dp[1] = 1
dp[3] = dp[1] = 1
dp[4] = dp[2] + dp[3] = 1 + 1 = 2
dp[5] = dp[2] + dp[3] = 1 + 1 = 2
dp[6] = dp[4] + dp[5] = 2 + 2 = 4
```

**Jawaban:** 4 lintasan

Verifikasi: 1->2->4->6, 1->2->5->6, 1->3->4->6, 1->3->5->6. Benar, ada 4.

---

### Contoh 5: Grid DP - Jumlah Lintasan dengan Obstacle

**Soal:** Grid 4x4 dengan obstacle di (1,1) dan (2,2) (0-indexed). Bergerak hanya kanan/bawah. Berapa lintasan dari (0,0) ke (3,3)?

**Pembahasan:**
```
Grid (X = obstacle):
.  .  .  .
.  X  .  .
.  .  X  .
.  .  .  .

dp:
1  1  1  1
1  0  1  1
1  1  0  1
1  2  2  3
```

Perhitungan:
- dp[1][1] = 0 (obstacle)
- dp[1][2] = dp[0][2] + dp[1][1] = 1 + 0 = 1
- dp[2][1] = dp[1][1] + dp[2][0] = 0 + 1 = 1
- dp[2][2] = 0 (obstacle)
- dp[2][3] = dp[1][3] + dp[2][2] = 1 + 0 = 1
- dp[3][1] = dp[2][1] + dp[3][0] = 1 + 1 = 2
- dp[3][2] = dp[2][2] + dp[3][1] = 0 + 2 = 2
- dp[3][3] = dp[2][3] + dp[3][2] = 1 + 2 = 3

**Jawaban:** 3 lintasan

---

### Contoh 6: Bipartite Check

**Soal:** Apakah graf berikut bipartit? Edge: 1-2, 2-3, 3-4, 4-5, 5-1

**Pembahasan:**
- Pewarnaan: color[1]=0, color[2]=1, color[3]=0, color[4]=1, color[5]=0
- Cek edge 5-1: color[5]=0, color[1]=0 --> SAMA!
- Siklus panjang 5 (ganjil) --> tidak bipartit

**Jawaban:** Tidak bipartit (mengandung siklus ganjil panjang 5)

---

### Contoh 7: Floyd-Warshall

**Soal:** Graf 3 simpul dengan edge: 1->2 (bobot 4), 2->3 (bobot 1), 1->3 (bobot 6). Cari jarak terpendek semua pasang.

**Pembahasan:**

Matriks awal:
```
     1    2    3
1 [  0    4    6 ]
2 [ inf   0    1 ]
3 [ inf  inf   0 ]
```

k=1: dist[2][3] = min(1, inf+6) = 1, tidak ada perubahan lain
k=2: dist[1][3] = min(6, 4+1) = 5
k=3: tidak ada perubahan

Hasil:
```
     1    2    3
1 [  0    4    5 ]
2 [ inf   0    1 ]
3 [ inf  inf   0 ]
```

**Jawaban:** Jarak 1 ke 3 terpendek = 5 (via simpul 2)

---

### Contoh 8: Longest Path di DAG

**Soal:** DAG dengan bobot pada edge: 1->2(3), 1->3(2), 2->4(4), 3->4(5), 3->5(1), 4->5(2). Cari lintasan terpanjang dari 1 ke 5.

**Pembahasan:**
```
Topological order: 1, 2, 3, 4, 5

dp[1] = 0 (sumber)
Proses 1: dp[2] = max(-inf, 0+3) = 3, dp[3] = max(-inf, 0+2) = 2
Proses 2: dp[4] = max(-inf, 3+4) = 7
Proses 3: dp[4] = max(7, 2+5) = 7, dp[5] = max(-inf, 2+1) = 3
Proses 4: dp[5] = max(3, 7+2) = 9
```

**Jawaban:** Lintasan terpanjang dari 1 ke 5 = 9 (jalur: 1->2->4->5)

---

### Contoh 9: Deteksi Siklus

**Soal:** Graf berarah dengan edge: 1->2, 2->3, 3->4, 4->2, 4->5. Apakah ada siklus?

**Pembahasan:**
- DFS dari 1: kunjungi 1(gray)->2(gray)->3(gray)->4(gray)
- Dari 4, coba ke 2: simpul 2 masih gray (sedang dikunjungi) --> back edge!
- Ada siklus: 2->3->4->2

**Jawaban:** Ya, ada siklus (2, 3, 4)

---

### Contoh 10: Grid DP - Nilai Maksimum

**Soal:** Grid 3x3 berisi angka:
```
1 3 1
1 5 1
4 2 1
```
Bergerak hanya kanan/bawah. Cari lintasan dengan total nilai maksimum dari (0,0) ke (2,2).

**Pembahasan:**
```
dp:
1  4  5
2  9  10
6  11 12
```

Perhitungan:
- dp[0][0]=1, dp[0][1]=1+3=4, dp[0][2]=4+1=5
- dp[1][0]=1+1=2, dp[1][1]=max(4,2)+5=9, dp[1][2]=max(5,9)+1=10
- dp[2][0]=2+4=6, dp[2][1]=max(9,6)+2=11, dp[2][2]=max(10,11)+1=12

**Jawaban:** 12 (jalur: 1->3->5->2->1 yaitu kanan-bawah-bawah-kanan)

Cek jalur: (0,0)->(0,1)->(1,1)->(2,1)->(2,2) = 1+3+5+2+1 = 12. Benar!

---

### Contoh 11: Pemodelan Graf - Permainan Bidak

**Soal:** Papan 3x3. Bidak di (0,0). Setiap langkah bisa bergerak ke kanan (+1 kolom) atau ke bawah (+1 baris) atau diagonal kanan-bawah (+1 baris, +1 kolom). Berapa banyak cara mencapai (2,2)?

**Pembahasan:**
```
dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

dp:
1  1  1
1  3  5
1  5  13
```

Perhitungan:
- dp[0][j] = 1 (hanya dari kiri)
- dp[i][0] = 1 (hanya dari atas)
- dp[1][1] = dp[0][1] + dp[1][0] + dp[0][0] = 1+1+1 = 3
- dp[1][2] = dp[0][2] + dp[1][1] + dp[0][1] = 1+3+1 = 5
- dp[2][1] = dp[1][1] + dp[2][0] + dp[1][0] = 3+1+1 = 5
- dp[2][2] = dp[1][2] + dp[2][1] + dp[1][1] = 5+5+3 = 13

**Jawaban:** 13 cara

---

### Contoh 12: Union-Find untuk Komponen

**Soal:** Ada 6 simpul. Edge ditambahkan satu per satu: (1,2), (3,4), (5,6), (1,3), (4,6). Setelah semua edge ditambahkan, berapa banyak komponen terhubung?

**Pembahasan:**
- Awal: 6 komponen (masing-masing simpul sendiri)
- (1,2): gabung -> {1,2}, {3}, {4}, {5}, {6} --> 5 komponen
- (3,4): gabung -> {1,2}, {3,4}, {5}, {6} --> 4 komponen
- (5,6): gabung -> {1,2}, {3,4}, {5,6} --> 3 komponen
- (1,3): gabung {1,2} dan {3,4} -> {1,2,3,4}, {5,6} --> 2 komponen
- (4,6): 4 ada di {1,2,3,4}, 6 ada di {5,6}, gabung -> {1,2,3,4,5,6} --> 1 komponen

**Jawaban:** 1 komponen terhubung

---

### Contoh 13: Bellman-Ford dengan Bobot Negatif

**Soal:** Graf 4 simpul, sumber = 1. Edge: 1->2(1), 1->3(4), 2->3(-2), 2->4(5), 3->4(1). Cari jarak terpendek dari 1 ke semua simpul.

**Pembahasan:**

Iterasi 1:
- Relax 1->2: dist[2] = min(inf, 0+1) = 1
- Relax 1->3: dist[3] = min(inf, 0+4) = 4
- Relax 2->3: dist[3] = min(4, 1+(-2)) = -1
- Relax 2->4: dist[4] = min(inf, 1+5) = 6
- Relax 3->4: dist[4] = min(6, -1+1) = 0

Iterasi 2:
- Tidak ada perubahan (sudah stabil)

**Jawaban:** dist = [0, 1, -1, 0]

Perhatikan: Dijkstra tidak bisa menangani edge 2->3 berbobot -2 dengan benar!

---

### Contoh 14: Prim's MST Step-by-Step

**Soal:** Sama dengan Contoh 1. Gunakan Prim mulai dari simpul A.

**Pembahasan:**
```
Mulai: simpul A
Candidate edges: A-B(7), A-D(5)
Pilih A-D(5): MST = {A-D}

Simpul sudah di MST: {A, D}
Candidate edges: A-B(7), D-B(9), D-E(15)
Pilih A-B(7): MST = {A-D, A-B}

Simpul sudah di MST: {A, B, D}
Candidate edges: B-C(8), B-E(7), D-E(15)
Pilih B-E(7): MST = {A-D, A-B, B-E}

Simpul sudah di MST: {A, B, D, E}
Candidate edges: B-C(8), C-E(5), D-E(sudah)
Pilih C-E(5): MST = {A-D, A-B, B-E, C-E}

Semua simpul terhubung!
```

MST = {A-D, A-B, B-E, C-E}, total = 5+7+7+5 = **24**

Catatan: Hasil sama dengan Kruskal (MST unik jika semua bobot berbeda; jika ada bobot sama, bisa beda edge tapi total bobot sama).

---

## 17. Latihan

### Soal Latihan

1. **[Kruskal]** Graf 6 simpul dengan edge: A-B(4), A-C(3), B-C(5), B-D(6), C-D(7), C-E(8), D-E(2), D-F(9), E-F(4). Cari bobot MST.

2. **[Dijkstra]** Graf berarah: 1->2(3), 1->3(1), 2->3(1), 2->4(4), 3->2(1), 3->4(5), 4->5(2). Cari jarak terpendek dari 1 ke 5.

3. **[Topological Sort]** Tentukan urutan topologis untuk DAG: A->B, A->C, B->D, C->D, C->E, D->F, E->F.

4. **[DAG DP]** Dengan DAG di soal 3 (semua bobot = 1), berapa banyak lintasan dari A ke F?

5. **[Grid DP]** Grid 4x3 berisi semua 1. Bergerak hanya kanan/bawah. Berapa banyak lintasan dari (0,0) ke (3,2)?

6. **[Bipartit]** Apakah graf dengan edge 1-2, 2-3, 3-4, 4-1, 1-3 bipartit?

7. **[Floyd-Warshall]** Graf 4 simpul: 1->2(2), 1->3(5), 2->3(1), 3->4(2), 2->4(6). Hitung matriks jarak terpendek semua pasang.

8. **[Bellman-Ford]** Graf 3 simpul: 1->2(3), 2->3(-5), 1->3(2). Cari jarak terpendek dari 1 ke 3.

9. **[Union-Find]** Ada 7 simpul. Edge ditambahkan: (1,2), (3,4), (5,6), (6,7), (2,3), (1,5). Berapa komponen terhubung setelah semua edge ditambahkan?

10. **[Grid DP]** Grid 3x3 dengan bobot:
    ```
    2 1 3
    6 5 4
    7 8 9
    ```
    Bergerak hanya kanan/bawah. Cari total bobot minimum dari (0,0) ke (2,2).

11. **[Pemodelan]** Sebuah turnamen round-robin melibatkan 5 tim. Setiap pasang tim bermain tepat sekali. Modelkan sebagai graf dan hitung total pertandingan.

12. **[Deteksi Siklus]** Graf berarah: 1->2, 2->3, 3->4, 4->5, 5->3. Apakah ada siklus? Jika ya, sebutkan simpul-simpulnya.

### Kunci Jawaban Singkat

1. MST bobot = 4+3+2+4+6 = 19 (edge: A-C, A-B atau C-B tergantung, D-E, E-F, B-D)
   Urutan: D-E(2), A-C(3), A-B(4), E-F(4), B-D(6) = 2+3+4+4+6 = 19
2. Jarak 1 ke 5 = 8 (jalur: 1->3->2->4->5 = 1+1+4+2 = 8)
3. Salah satu urutan valid: A, B, C, D, E, F atau A, C, B, E, D, F
4. 3 lintasan (A->B->D->F, A->C->D->F, A->C->E->F)
5. C(3+2, 2) = C(5,2) = 10 lintasan (3 langkah bawah + 2 langkah kanan)
6. Tidak bipartit (ada siklus ganjil: 1-2-3-1 panjang 3)
7. Matriks: dist[1][4]=5 (1->2->3->4), dist[1][3]=3 (1->2->3), dst.
8. dist[3] = min(2, 3+(-5)) = -2 (jalur: 1->2->3)
9. 1 komponen (semua terhubung: {1,2,3,4,5,6,7})
10. Bobot minimum = 2+1+3+4+9 = 19 (kanan-kanan-bawah-bawah) atau 2+6+5+4+9=26 (bawah-bawah-kanan-kanan).
    Sebenarnya: dp[0][0]=2, dp[0][1]=3, dp[0][2]=6, dp[1][0]=8, dp[1][1]=min(3,8)+5=8, dp[1][2]=min(6,8)+4=10, dp[2][0]=15, dp[2][1]=min(8,15)+8=16, dp[2][2]=min(10,16)+9=19.
    Jawaban: 19
11. Graf lengkap K5. Total edge = C(5,2) = 10 pertandingan.
12. Ya, ada siklus: 3->4->5->3

---

## Tips untuk OSK 2026

1. **Hafalkan kompleksitas**: Ketahui kapan menggunakan BFS vs Dijkstra vs Floyd-Warshall
2. **Perhatikan constraint**: Jika V <= 500, Floyd-Warshall aman. Jika V sampai 10^5, gunakan Dijkstra.
3. **Latih trace manual**: Di OSK, Anda diminta men-trace algoritma step-by-step
4. **Kenali bentuk DAG**: Jika graf tidak ada siklus, DAG DP lebih efisien
5. **Grid = graf**: Jangan lupa bahwa grid bisa dimodelkan sebagai graf
6. **Union-Find untuk dinamis**: Jika edge ditambahkan satu per satu, Union-Find adalah pilihan tepat
7. **Bipartit = 2-colorable**: Cukup cek ada tidaknya siklus ganjil
8. **Hati-hati overflow**: Jumlah lintasan bisa sangat besar, gunakan long long
9. **Topological sort + DP**: Kombinasi ini sangat kuat untuk masalah DAG
10. **Baca soal cermat**: Tentukan apakah graf berarah/tak berarah, berbobot/tak berbobot sebelum memilih algoritma

---

*Materi ini mencakup topik-topik graf lanjutan yang relevan untuk persiapan OSK Informatika 2026. Pastikan Anda memahami setiap algoritma, bisa men-trace secara manual, dan mampu mengenali kapan harus menggunakan masing-masing teknik.*
