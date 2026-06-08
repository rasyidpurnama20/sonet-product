# Sumber 05 — Tools & Environment Belajar

Setup alat bantu dan lingkungan belajar yang direkomendasikan untuk persiapan OSK Informatika.

---

## 💻 Compiler & IDE C++

OSK Informatika Bagian C menggunakan **C++**. Berikut setup yang direkomendasikan:

### 1. Online IDE (tanpa install)
| Platform | URL | Keterangan |
|----------|-----|------------|
| Replit | https://replit.com | Online IDE, bisa langsung coding C++ |
| Programiz | https://www.programiz.com/cpp-programming/online-compiler/ | Simpel, cocok untuk pemula |
| Compiler Explorer | https://godbolt.org | Lihat output assembly, bagus untuk memahami kode |
| OnlineGDB | https://onlinegdb.com/online_c++_compiler | Compiler + debugger online |
| ideone | https://ideone.com | Mendukung banyak bahasa termasuk C++ |

### 2. Offline IDE (install di komputer)
| IDE | URL | Keterangan |
|-----|-----|------------|
| Code::Blocks | http://www.codeblocks.org | Ringan, cocok untuk pemula, bundled dengan GCC |
| Visual Studio Code | https://code.visualstudio.com | Modern, extensible, butuh setup GCC terpisah |
| Dev-C++ (Orwell) | https://sourceforge.net/projects/orwelldevcpp/ | Klasik untuk olimpiade, ringan |
| CLion | https://www.jetbrains.com/clion/ | Profesional (berbayar, gratis untuk pelajar) |

### 3. Compiler
- **GCC/G++:** Compiler C++ standar yang digunakan di olimpiade.
  - Linux: sudah terinstall, gunakan `g++ -o output file.cpp`
  - Windows: Install via MinGW (https://www.mingw-w64.org/)

---

## 🔧 Tools Tambahan

### Visualisasi Algoritma
| Tool | URL | Kegunaan |
|------|-----|----------|
| VisuAlgo | https://visualgo.net | Animasi visual algoritma: sorting, graph, tree, dll. |
| Algorithm Visualizer | https://algorithm-visualizer.org | Jalankan dan lihat animasi algoritma secara interaktif |
| CS USF Visualization | https://www.cs.usfca.edu/~galles/visualization/ | Visualisasi struktur data klasik |

### Tools Matematika & Logika
| Tool | URL | Kegunaan |
|------|-----|----------|
| Wolfram Alpha | https://www.wolframalpha.com | Hitung kombinatorika, deret, aljabar |
| Desmos | https://www.desmos.com | Grafik fungsi, eksplorasi matematika |
| Truth Table Generator | Cari di Google: "truth table generator" | Membuat tabel kebenaran aljabar Boolean |

---

## 📝 Template Kode C++ untuk OSK

### Template Dasar
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // Kode kamu di sini
    
    return 0;
}
```

### Template dengan fungsi umum
```cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    // Kode kamu di sini
    
    return 0;
}
```

---

## ⌨️ Perintah Compile & Run C++ (Terminal/CMD)

```bash
# Compile
g++ -o nama_program nama_file.cpp

# Compile dengan flag debug
g++ -Wall -Wextra -o nama_program nama_file.cpp

# Compile dengan standar C++17
g++ -std=c++17 -o nama_program nama_file.cpp

# Run
./nama_program           # Linux/Mac
nama_program.exe         # Windows

# Compile + Run sekaligus
g++ -o sol sol.cpp && ./sol
```

---

## 📋 Cheat Sheet Sintaks C++ untuk OSK

### Input/Output
```cpp
cin >> a >> b;           // baca 2 variabel
cout << a << " " << b << "\n";  // cetak dengan newline
```

### Array
```cpp
int arr[100];
int n; cin >> n;
for (int i = 0; i < n; i++) cin >> arr[i];
```

### Sorting
```cpp
sort(arr, arr + n);                    // ascending
sort(arr, arr + n, greater<int>());    // descending
```

### String
```cpp
string s;
cin >> s;
cout << s.length() << "\n";
cout << s[0] << "\n";   // karakter pertama
```

### Vektor
```cpp
vector<int> v;
v.push_back(10);
v.push_back(20);
for (int x : v) cout << x << " ";
```

---

## 🗂️ Cara Organisasi File Latihan

```
latihan/
├── bebras/         ← soal Bagian A
│   ├── 2024/
│   └── 2023/
├── studi-kasus/    ← soal Bagian B
│   └── latihan-01.md
└── trace-cpp/      ← soal Bagian C
    ├── soal-01.cpp
    └── soal-01-penjelasan.md
```
