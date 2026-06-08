# Materi 07 — Teori Graf Lanjutan: Menyederhanakan Masalah Kompleks

## 1. Mengapa Graf Bisa Menyederhanakan Masalah?

Banyak masalah dunia nyata bisa dimodelkan sebagai graf:
- **Peta kota** → Graf berbobot (jarak)
- **Jaringan sosial** → Graf tak berarah
- **Jadwal pelajaran** → Graf bipartit / pewarnaan
- **Prasyarat mata kuliah** → DAG (Directed Acyclic Graph)
- **Masalah kombinatorik** → Graf + penghitungan path

Kunci: **Kenali polanya, ubah ke graf, lalu gunakan algoritma yang tepat.**

---

## 2. Menghitung Banyak Lintasan (Count Paths)

### Pada Graf Berarah Tanpa Siklus (DAG)
Gunakan **Dynamic Programming** atau DFS + memoization.

```
dp[v] = banyak lintasan dari sumber ke v
dp[s] = 1  (titik awal)
dp[v] = Σ dp[u]  untuk setiap u → v
```

**Contoh:**
```
Graf: 1→2, 1→3, 2→4, 3→4, 4→5
dp[1]=1, dp[2]=1, dp[3]=1, dp[4]=dp[2]+dp[3]=2, dp[5]=dp[4]=2
```

**Kode C++:**
```cpp
vector<int> adj[105];
int dp[105];
bool visited[105];

int countPaths(int u, int target) {
    if (u == target) return 1;
    if (visited[u]) return dp[u];
    visited[u] = true;
    dp[u] = 0;
    for (int v : adj[u]) {
        dp[u] += countPaths(v, target);
    }
    return dp[u];
}
```

---

## 3. Jarak Terpendek di Graf Tak Berbobot (BFS)

BFS otomatis memberikan jarak terpendek pada graf tak berbobot.

```cpp
int bfs(int start, int n, vector<int> adj[]) {
    vector<int> dist(n+1, -1);
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist; // dist[v] = jarak dari start ke v
}
```

---

## 4. Total Jarak Semua Pasangan di Pohon

### Pendekatan Naif: O(n²)
Jalankan BFS dari setiap node. Cocok untuk n kecil.

```cpp
int totalPairDistance(int n, vector<int> adj[]) {
    int total = 0;
    for (int src = 1; src <= n; src++) {
        // BFS dari src
        vector<int> dist(n+1, -1);
        queue<int> q;
        q.push(src); dist[src] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        for (int v = 1; v <= n; v++) {
            if (v > src && dist[v] != -1) {
                total += dist[v];
            }
        }
    }
    return total;
}
```

### Pendekatan Efisien untuk Pohon: O(n)
Gunakan sifat pohon: jumlah kontribusi setiap edge.

**Ide:** Setiap edge (u, v) menghubungkan 2 komponen di pohon.
- Jika komponen kiri punya `k` node, komponen kanan punya `n-k` node
- Edge ini dilalui oleh `k × (n-k)` pasang node
- Kontribusi edge ke total jarak = `k × (n-k)`

```
Total = Σ untuk setiap edge: (ukuran subtree kiri) × (ukuran subtree kanan)
```

---

## 5. Dynamic Programming pada Graf (DAG DP)

### Masalah Path Maksimum
Pada grid atau DAG, cari lintasan dengan nilai maksimum.

**Khas OSN:** Grid dengan panah arah tertentu, cari lintasan dari sudut ke sudut.

```
dp[i][j] = nilai maksimum lintasan sampai ke sel (i,j)

Jika bisa bergerak ke kanan dan atas:
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + nilai[i][j]
```

**Kode C++ (grid, gerakan kanan & atas):**
```cpp
int dp[105][105];
int grid[105][105];

int maxPath(int R, int C) {
    dp[0][0] = grid[0][0];
    for (int i = 1; i < R; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
    for (int j = 1; j < C; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
    for (int i = 1; i < R; i++)
        for (int j = 1; j < C; j++)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j];
    return dp[R-1][C-1];
}
```

---

## 6. Pewarnaan Graf & Independent Set

### Independent Set
Himpunan simpul dimana **tidak ada dua simpul yang bertetangga**.

**Soal OSN tipe:** "Warnai simpul hitam/putih agar tidak ada dua hitam yang bertetangga."
= Cari semua **independent set** yang valid.

### Pendekatan: DP atau DFS Backtracking
Untuk graf kecil, coba semua kemungkinan pewarnaan (2^n kombinasi).

```cpp
int n; // jumlah simpul
bool adj[20][20];
int countIndependentSets() {
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        bool valid = true;
        for (int i = 0; i < n && valid; i++) {
            if (!(mask & (1<<i))) continue;
            for (int j = i+1; j < n && valid; j++) {
                if (!(mask & (1<<j))) continue;
                if (adj[i][j]) valid = false;
            }
        }
        if (valid) count++;
    }
    return count;
}
```

---

## 7. Graf Berbobot & Minimum Spanning Tree

### Kruskal's Algorithm
Menghubungkan semua node dengan total bobot terkecil.

**Langkah:**
1. Urutkan semua edge berdasarkan bobot (ascending)
2. Tambahkan edge ke MST jika tidak membentuk siklus (gunakan Union-Find)
3. Berhenti saat semua node terhubung

### Dijkstra's Algorithm
Mencari jarak terpendek dari satu sumber ke semua node (bobot non-negatif).

```cpp
vector<pair<int,int>> adj[105]; // {tetangga, bobot}
int dist[105];
bool visited[105];

void dijkstra(int start, int n) {
    fill(dist, dist+n+1, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    dist[start] = 0;
    pq.push({0, start});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (visited[u]) continue;
        visited[u] = true;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
}
```

---

## 8. Komponen Terhubung (Connected Components)

### Graf Tak Berarah
```cpp
int component[105];
bool visited[105];
vector<int> adj[105];

void dfs(int u, int comp) {
    visited[u] = true;
    component[u] = comp;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v, comp);
    }
}

int countComponents(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            dfs(i, count++);
        }
    }
    return count;
}
```

---

## 9. Deteksi Siklus

### Graf Berarah (DFS + Warna)
```cpp
// 0=belum dikunjungi, 1=sedang dikunjungi, 2=selesai
int color[105];

bool hasCycle(int u) {
    color[u] = 1;
    for (int v : adj[u]) {
        if (color[v] == 1) return true;  // back edge = siklus
        if (color[v] == 0 && hasCycle(v)) return true;
    }
    color[u] = 2;
    return false;
}
```

---

## 10. Topological Sort (Urutan Topologis)

Hanya berlaku untuk **DAG** (graf berarah tanpa siklus).
Menghasilkan urutan node dimana setiap edge u→v, u muncul sebelum v.

**Kahn's Algorithm (BFS-based):**
```cpp
vector<int> topoSort(int n, vector<int> adj[]) {
    vector<int> indegree(n+1, 0);
    for (int u = 1; u <= n; u++)
        for (int v : adj[u]) indegree[v]++;
    
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (indegree[i] == 0) q.push(i);
    
    vector<int> order;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            if (--indegree[v] == 0) q.push(v);
        }
    }
    return order;
}
```

---

## 11. Pigeonhole Principle pada Graf

**Prinsip:** Jika ada n kotak dan n+1 bola, minimal satu kotak berisi ≥2 bola.

**Aplikasi pada Graf:**
- Jika n+1 bilangan dari rentang 1..2n, pasti ada 2 bilangan yang selisihnya = kelipatan n
- Gunakan sisa bagi (modulo) sebagai "kotak"

**Teknik Mengelompokkan:**
Untuk masalah "2 bilangan selisihnya kelipatan X":
- Kelompokkan bilangan berdasarkan `nilai mod X`
- Kotak: sisa 0, 1, 2, ..., X-1 (total X kotak)
- Minimal ambil **X+1** bilangan untuk **menjamin** ada 2 di kotak yang sama
  → tapi kita perlu menghitung kotak yang **ada** isinya!

---

## 12. Ringkasan Strategi Pemilihan Algoritma

| Masalah | Algoritma |
|---------|-----------|
| Jarak terpendek, tak berbobot | BFS |
| Jarak terpendek, berbobot positif | Dijkstra |
| Deteksi siklus | DFS (color) |
| Urutan topologis | Kahn / DFS |
| Minimum spanning tree | Kruskal / Prim |
| Banyak lintasan di DAG | DP + DFS |
| Komponen terhubung | BFS / DFS / Union-Find |
| Independent set (graf kecil) | Bitmask DP |
| Path maksimum di grid | DP 2D |

---

## 13. Latihan
1. Graf berarah: 1→2, 1→3, 2→4, 3→4, 2→5, 3→5. Berapa banyak lintasan dari 1 ke 5?
2. Pohon dengan 5 node: 1-2, 1-3, 2-4, 2-5. Hitung total jarak semua pasangan node.
3. Graf dengan node {1,2,3,4} dan edge {1-2, 2-3, 3-4}. Berapa banyak independent set (termasuk set kosong)?
4. Gunakan BFS untuk mencari jarak dari node 1 ke semua node pada graf: 1-2, 1-3, 2-4, 3-4, 4-5.

*Jawaban di folder `../latihan/`*
