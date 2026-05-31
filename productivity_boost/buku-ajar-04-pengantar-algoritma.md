# Pengantar Algoritma: Buku Ajar Berbasis *Introduction to Algorithms* (CLRS) Edisi Keempat

> **Buku Ajar untuk Mahasiswa Ilmu Komputer / Teknik Informatika**
> Disusun secara sistematis dan pedagogis berdasarkan satu sumber utama:
> Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, dan Clifford Stein. *Introduction to Algorithms*, Fourth Edition. Cambridge, Massachusetts: The MIT Press, 2022. ISBN 9780262046305 (LCCN 2021037260).

---

## Metadata Buku Ajar

| Atribut | Keterangan |
|---|---|
| **Judul buku ajar** | Pengantar Algoritma: Buku Ajar Berbasis CLRS Edisi Keempat |
| **Sumber utama** | *Introduction to Algorithms*, Fourth Edition (dikenal luas sebagai "CLRS") |
| **Penulis sumber** | Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein |
| **Penerbit** | The MIT Press, Cambridge, Massachusetts & London, England |
| **Tahun terbit** | 2022 (Edisi ke-4) |
| **Cakupan** | 8 Bagian, 35 Bab + Apendiks Latar Belakang Matematis |
| **Bahasa pengantar** | Bahasa Indonesia akademik (istilah teknis dipertahankan dalam Bahasa Inggris dengan penjelasan) |
| **Tingkat** | Sarjana (S1) tahun ke-2 sampai ke-4; dapat dipakai pada jenjang pascasarjana awal |
| **Prasyarat** | Struktur Data dasar, Matematika Diskret, Kalkulus dasar, dan kemampuan pemrograman prosedural |

**Sitasi lengkap (gaya umum):**

> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). The MIT Press.

---

## Kata Pengantar

### Tujuan Buku Ajar

Buku ajar ini disusun sebagai pendamping berbahasa Indonesia untuk mempelajari isi *Introduction to Algorithms* Edisi Keempat secara terstruktur. Tujuannya bukan menggantikan buku sumber, melainkan **menjembatani** pembaca berbahasa Indonesia agar dapat:

1. Memahami **definisi formal** algoritma, struktur data, dan analisis kompleksitas.
2. Membaca dan menulis **pseudocode** bergaya CLRS dengan benar.
3. Menganalisis **waktu (running time)** dan **ruang (space)** suatu algoritma menggunakan notasi asimtotik O, Ω, dan Θ.
4. Menguasai paradigma desain algoritma utama: *divide-and-conquer*, *dynamic programming*, *greedy*, analisis teramortisasi, serta algoritma graf, dan menempatkan permasalahan dalam lanskap **kompleksitas komputasi** (P, NP, NP-complete).

### Untuk Siapa Buku Ini

Buku ini ditujukan untuk **mahasiswa ilmu komputer dan teknik informatika** yang telah menyelesaikan mata kuliah pemrograman dasar dan struktur data pengantar. Buku ini juga bermanfaat bagi praktisi rekayasa perangkat lunak yang ingin memperdalam dasar teoretis, serta peserta yang mempersiapkan diri menghadapi wawancara teknis atau kompetisi pemrograman.

### Prasyarat Matematika

Pembaca diasumsikan menguasai, atau bersedia mengulang melalui **Bagian VIII (Apendiks)**, hal-hal berikut:

- **Notasi penjumlahan (summation)** dan manipulasi deret (lihat Apendiks A).
- **Himpunan, relasi, fungsi, dan graf** sebagai objek matematis (Apendiks B).
- **Pencacahan (counting) dan probabilitas** dasar: permutasi, kombinasi, variabel acak, nilai harapan (Apendiks C).
- **Matriks** dan operasi aljabar liniernya (Apendiks D).
- Logaritma, eksponen, fungsi lantai (floor) ⌊x⌋ dan langit-langit (ceiling) ⌈x⌉, serta induksi matematika.

### Cara Penggunaan Buku Ajar

Setiap bab disusun dengan pola pedagogis yang konsisten:

- **Tujuan Pembelajaran** — dirumuskan dengan kata kerja Taksonomi Bloom yang terukur.
- **Peta Konsep** — gambaran ringkas keterkaitan ide dalam bab.
- **Materi Inti** — definisi formal, ide algoritma, pseudocode, penjelasan langkah, analisis kompleksitas, argumen korektness, dan trace contoh.
- **Istilah Kunci** — daftar istilah (Inggris) dengan penjelasan Indonesia.
- **Contoh / Studi Kasus** — penelusuran (trace) algoritma pada input kecil, kerap dalam bentuk tabel.
- **Rangkuman** — poin-poin esensial.
- **Latihan & Soal** — campuran soal pemahaman, analisis kompleksitas (HOTS), dan implementasi/tracing.

**Saran belajar:** Bacalah Bab Pendahuluan dan Bagian I secara berurutan karena menjadi fondasi seluruh buku. Setelah itu, Bagian II–VI dapat dibaca relatif independen sesuai kebutuhan, sementara Bagian VII bersifat topik pilihan. Kerjakan latihan sebelum melihat pembahasan, dan biasakan menuliskan ulang pseudocode dengan tangan untuk memperkuat pemahaman.

### Konvensi Notasi

Sepanjang buku digunakan konvensi berikut, mengikuti gaya CLRS:

- `A[1 : n]` menyatakan larik (array) `A` dengan indeks 1 sampai `n`.
- Operator `=` dalam pseudocode menyatakan **penugasan (assignment)**; perbandingan kesetaraan ditulis `==`.
- `lg n` berarti logaritma basis 2 (log₂ n); `ln n` logaritma natural; `log n` basis 10 bila tidak disebut lain. Dalam notasi asimtotik, basis logaritma sering tak relevan karena berbeda faktor konstan.
- Atribut objek ditulis dengan notasi titik, mis. `x.key`, `G.V`, `G.E`.
- `Θ`, `O`, `Ω`, `o`, `ω` adalah notasi asimtotik yang didefinisikan formal di Bab 3.

---

## Daftar Isi

- [Bab Pendahuluan: Algoritma, Struktur Data, dan Model Komputasi](#bab-pendahuluan-algoritma-struktur-data-dan-model-komputasi)
- [BAGIAN I — Fondasi (Foundations)](#bagian-i--fondasi-foundations)
  - [Bab 1 — Peran Algoritma dalam Komputasi](#bab-1--peran-algoritma-dalam-komputasi)
  - [Bab 2 — Memulai: Insertion Sort dan Merge Sort](#bab-2--memulai-insertion-sort-dan-merge-sort)
  - [Bab 3 — Mengkarakterisasi Waktu Eksekusi (Notasi Asimtotik)](#bab-3--mengkarakterisasi-waktu-eksekusi-notasi-asimtotik)
  - [Bab 4 — Divide-and-Conquer dan Teorema Master](#bab-4--divide-and-conquer-dan-teorema-master)
  - [Bab 5 — Analisis Probabilistik dan Algoritma Acak](#bab-5--analisis-probabilistik-dan-algoritma-acak)
- [BAGIAN II — Pengurutan dan Statistik Terurut](#bagian-ii--pengurutan-dan-statistik-terurut)
  - [Bab 6 — Heapsort](#bab-6--heapsort)
  - [Bab 7 — Quicksort](#bab-7--quicksort)
  - [Bab 8 — Pengurutan dalam Waktu Linear](#bab-8--pengurutan-dalam-waktu-linear)
  - [Bab 9 — Median dan Statistik Terurut](#bab-9--median-dan-statistik-terurut)
- [BAGIAN III — Struktur Data](#bagian-iii--struktur-data)
  - [Bab 10 — Struktur Data Elementer](#bab-10--struktur-data-elementer)
  - [Bab 11 — Tabel Hash](#bab-11--tabel-hash)
  - [Bab 12 — Pohon Pencarian Biner (BST)](#bab-12--pohon-pencarian-biner-bst)
  - [Bab 13 — Pohon Merah-Hitam (Red-Black Trees)](#bab-13--pohon-merah-hitam-red-black-trees)
- [BAGIAN IV — Teknik Desain dan Analisis Lanjutan](#bagian-iv--teknik-desain-dan-analisis-lanjutan)
  - [Bab 14 — Pemrograman Dinamis (Dynamic Programming)](#bab-14--pemrograman-dinamis-dynamic-programming)
  - [Bab 15 — Algoritma Serakah (Greedy)](#bab-15--algoritma-serakah-greedy)
  - [Bab 16 — Analisis Teramortisasi (Amortized Analysis)](#bab-16--analisis-teramortisasi-amortized-analysis)
- [BAGIAN V — Struktur Data Lanjutan](#bagian-v--struktur-data-lanjutan)
  - [Bab 17 — Augmentasi Struktur Data](#bab-17--augmentasi-struktur-data)
  - [Bab 18 — B-Trees](#bab-18--b-trees)
  - [Bab 19 — Struktur Data untuk Himpunan Terpisah (Disjoint Sets)](#bab-19--struktur-data-untuk-himpunan-terpisah-disjoint-sets)
- [BAGIAN VI — Algoritma Graf](#bagian-vi--algoritma-graf)
  - [Bab 20 — Algoritma Graf Elementer](#bab-20--algoritma-graf-elementer)
  - [Bab 21 — Minimum Spanning Trees (MST)](#bab-21--minimum-spanning-trees-mst)
  - [Bab 22 — Lintasan Terpendek Sumber-Tunggal](#bab-22--lintasan-terpendek-sumber-tunggal)
  - [Bab 23 — Lintasan Terpendek Semua-Pasangan](#bab-23--lintasan-terpendek-semua-pasangan)
  - [Bab 24 — Aliran Maksimum (Maximum Flow)](#bab-24--aliran-maksimum-maximum-flow)
  - [Bab 25 — Pencocokan pada Graf Bipartit](#bab-25--pencocokan-pada-graf-bipartit)
- [BAGIAN VII — Topik Terpilih](#bagian-vii--topik-terpilih)
  - [Bab 26 — Algoritma Paralel](#bab-26--algoritma-paralel)
  - [Bab 27 — Algoritma Daring (Online Algorithms)](#bab-27--algoritma-daring-online-algorithms)
  - [Bab 28 — Operasi Matriks](#bab-28--operasi-matriks)
  - [Bab 29 — Pemrograman Linear (Linear Programming)](#bab-29--pemrograman-linear-linear-programming)
  - [Bab 30 — Polinomial dan FFT](#bab-30--polinomial-dan-fft)
  - [Bab 31 — Algoritma Teori Bilangan](#bab-31--algoritma-teori-bilangan)
  - [Bab 32 — Pencocokan String (String Matching)](#bab-32--pencocokan-string-string-matching)
  - [Bab 33 — Algoritma Machine Learning](#bab-33--algoritma-machine-learning)
  - [Bab 34 — NP-Completeness](#bab-34--np-completeness)
  - [Bab 35 — Algoritma Aproksimasi](#bab-35--algoritma-aproksimasi)
- [BAGIAN VIII — Apendiks: Latar Belakang Matematis](#bagian-viii--apendiks-latar-belakang-matematis)
- [Bab Penutup: Sintesis dan Pemilihan Algoritma](#bab-penutup-sintesis-dan-pemilihan-algoritma)
- [Glosarium (EN → ID)](#glosarium-en--id)
- [Daftar Pustaka](#daftar-pustaka)

---

## Bab Pendahuluan: Algoritma, Struktur Data, dan Model Komputasi

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** istilah *algoritma* dan *struktur data* secara formal serta membedakan keduanya.
2. **Menjelaskan** mengapa efisiensi (waktu dan ruang) menjadi sumber daya komputasi yang sama pentingnya dengan perangkat keras.
3. **Menguraikan** model komputasi RAM (Random-Access Machine) sebagai dasar pengukuran biaya algoritma.
4. **Menafsirkan** peran pseudocode sebagai bahasa komunikasi algoritma yang independen terhadap bahasa pemrograman.
5. **Membandingkan** secara kualitatif laju pertumbuhan fungsi yang umum muncul dalam analisis algoritma.

### Peta Konsep

```
                 PERSOALAN KOMPUTASI
                         |
         +---------------+---------------+
         |                               |
    ALGORITMA                       STRUKTUR DATA
 (prosedur komputasi)          (organisasi data)
         |                               |
   dianalisis dengan              mendukung operasi
   MODEL RAM                      (sisip, hapus, cari)
         |                               |
         +-------------- EFISIENSI -------+
                   (waktu & ruang)
                         |
                NOTASI ASIMTOTIK (Θ, O, Ω)
```

### Materi Inti

#### Apa itu Algoritma?

Secara informal, sebuah **algoritma (algorithm)** adalah prosedur komputasi yang terdefinisi dengan baik (well-defined), yang menerima suatu nilai atau himpunan nilai sebagai **masukan (input)** dan menghasilkan suatu nilai atau himpunan nilai sebagai **keluaran (output)** dalam waktu berhingga. Algoritma dengan demikian merupakan rangkaian langkah komputasi yang mengubah masukan menjadi keluaran.

Sebuah algoritma juga dapat dipandang sebagai alat untuk menyelesaikan **persoalan komputasi (computational problem)** yang terspesifikasi dengan baik. Spesifikasi persoalan menyatakan secara umum hubungan masukan/keluaran yang diinginkan; algoritma menjelaskan prosedur komputasi spesifik untuk mencapai hubungan tersebut.

Sebagai contoh kanonik, perhatikan **persoalan pengurutan (sorting problem)**:

> **Masukan:** Sebuah barisan dari `n` bilangan ⟨a₁, a₂, …, aₙ⟩.
> **Keluaran:** Sebuah permutasi (penataan ulang) ⟨a′₁, a′₂, …, a′ₙ⟩ dari barisan masukan sedemikian sehingga a′₁ ≤ a′₂ ≤ … ≤ a′ₙ.

Suatu algoritma dikatakan **benar (correct)** jika untuk setiap **instance (kasus uji)** masukan, ia berhenti (halts) dengan keluaran yang benar. Algoritma yang benar **menyelesaikan (solves)** persoalan komputasi yang diberikan.

#### Apa itu Struktur Data?

Sebuah **struktur data (data structure)** adalah cara menyimpan dan mengorganisasi data sehingga data tersebut dapat diakses dan dimodifikasi secara efisien. Tidak ada satu struktur data tunggal yang optimal untuk semua keperluan; karenanya penting memahami kekuatan dan keterbatasan beberapa struktur data. Algoritma dan struktur data saling bergantung: pemilihan struktur data yang tepat sering menentukan efisiensi algoritma, dan sebaliknya algoritma menentukan operasi apa yang harus didukung struktur data secara efisien (mis. penyisipan, penghapusan, pencarian).

#### Mengapa Efisiensi Penting?

Komputer secepat apa pun memiliki keterbatasan kecepatan dan memori. **Waktu komputasi (computing time)** dan **ruang memori (memory space)** adalah sumber daya yang langka dan harus digunakan secara hemat. Algoritma yang efisien dari segi waktu dan ruang membantu kita memanfaatkan sumber daya ini.

Pentingnya efisiensi paling jelas terlihat ketika ukuran masukan `n` membesar. Misalkan kita membandingkan dua algoritma pengurutan: *insertion sort* dengan waktu kira-kira c₁n² dan *merge sort* dengan waktu kira-kira c₂n lg n. Untuk `n` kecil, faktor konstan c₁ dan c₂ dapat membuat insertion sort lebih cepat. Namun begitu `n` cukup besar, keunggulan n lg n atas n² menjadi sangat menentukan: pada masukan satu juta elemen, perbedaannya dapat berarti antara hitungan detik dan hitungan jam atau hari. Inilah sebabnya **laju pertumbuhan (order of growth, rate of growth)** waktu eksekusi menjadi fokus utama analisis algoritma.

Tabel berikut memberikan intuisi laju pertumbuhan beberapa fungsi yang umum:

| Fungsi | Nama | Sifat |
|---|---|---|
| Θ(1) | konstan | tidak bergantung ukuran masukan |
| Θ(lg n) | logaritmik | tumbuh sangat lambat |
| Θ(n) | linear | sebanding ukuran masukan |
| Θ(n lg n) | linearitmik | batas bawah pengurutan berbasis perbandingan |
| Θ(n²) | kuadratik | umum pada algoritma berpasangan sederhana |
| Θ(n³) | kubik | mis. perkalian matriks naif, Floyd-Warshall |
| Θ(2ⁿ) | eksponensial | tidak praktis untuk `n` besar |
| Θ(n!) | faktorial | tidak praktis bahkan untuk `n` sedang |

#### Model Komputasi: Random-Access Machine (RAM)

Untuk menganalisis algoritma secara independen dari perangkat keras tertentu, digunakan model abstrak bernama **Random-Access Machine (RAM)**. Dalam model RAM:

- Instruksi dieksekusi **satu per satu**, tanpa operasi konkuren.
- Tersedia instruksi-instruksi dasar yang masing-masing memerlukan **waktu konstan**: operasi aritmetika (tambah, kurang, kali, bagi, sisa/modulo, pembulatan lantai/langit-langit), operasi pemindahan data (memuat/load, menyimpan/store, menyalin/copy), dan operasi kontrol (percabangan kondisional, pemanggilan dan kembalinya subrutin).
- Setiap **akses memori** memerlukan waktu konstan, tidak peduli di alamat mana data berada (sifat *random access*).
- Tipe data berupa bilangan bulat (integer) dan riil (floating-point). Diasumsikan setiap kata (word) data memiliki lebar terbatas; untuk masukan berukuran `n`, sebuah bilangan bulat umumnya direpresentasikan dalam c·lg n bit untuk suatu konstanta c ≥ 1, sehingga muat dalam satu kata.

Model RAM memungkinkan kita menghitung **waktu eksekusi (running time)** sebagai jumlah operasi dasar atau "langkah" yang dijalankan. Asumsi bahwa setiap langkah memakan waktu konstan inilah yang membuat analisis menjadi sederhana namun cukup prediktif terhadap kinerja nyata.

#### Peran Pseudocode

Sepanjang buku ini, algoritma disajikan dalam **pseudocode**. Pseudocode adalah cara mengekspresikan algoritma yang:

- **Independen bahasa pemrograman** — tidak terikat sintaks C, Java, atau Python tertentu.
- **Mengutamakan kejelasan ide** — menggunakan kalimat bahasa alami bila itu cara paling ringkas mengomunikasikan suatu langkah, sambil mengabaikan detail teknis (penanganan kesalahan, manajemen memori) yang tidak esensial bagi pemahaman algoritma.
- **Ringkas dan presisi** — memuat struktur kontrol yang jelas (perulangan `for`/`while`, percabangan `if`/`else`).

Konvensi pseudocode CLRS yang penting: indentasi menunjukkan blok; `//` mengawali komentar; variabel bersifat lokal terhadap prosedur kecuali dinyatakan global; objek diakses lewat notasi titik (`x.key`); parameter dilewatkan **by value** untuk tipe sederhana, sementara objek/larik dilewatkan lewat **pointer/referensi** sehingga modifikasi terlihat oleh pemanggil.

### Istilah Kunci

- **Algorithm (algoritma):** prosedur komputasi terdefinisi baik yang mengubah masukan menjadi keluaran dalam langkah berhingga.
- **Data structure (struktur data):** cara menyimpan dan mengorganisasi data agar efisien diakses/dimodifikasi.
- **Computational problem (persoalan komputasi):** spesifikasi hubungan masukan–keluaran yang diinginkan.
- **Instance (kasus/instans):** masukan konkret yang memenuhi batasan persoalan.
- **Correctness (kebenaran):** sifat algoritma yang selalu berhenti dengan keluaran benar untuk setiap instance.
- **Running time (waktu eksekusi):** jumlah langkah dasar yang dijalankan algoritma, sebagai fungsi ukuran masukan.
- **RAM model (model RAM):** model komputasi sekuensial dengan operasi dasar berbiaya konstan.
- **Order of growth (laju pertumbuhan):** perilaku asimtotik waktu eksekusi saat ukuran masukan membesar.
- **Pseudocode:** notasi semi-formal untuk mendeskripsikan algoritma secara jelas dan independen bahasa.

### Rangkuman

Algoritma adalah inti dari komputasi: prosedur yang mengubah masukan menjadi keluaran dengan benar. Struktur data menyediakan fondasi penyimpanan yang efisien. Karena waktu dan ruang adalah sumber daya terbatas, kita mengukur **efisiensi** algoritma melalui laju pertumbuhan waktu eksekusi dalam model RAM, dan kita mengomunikasikan algoritma melalui pseudocode. Buku ini akan mengembangkan alat matematis (notasi asimtotik, rekurens) untuk menganalisis efisiensi secara rigor, lalu menerapkannya pada berbagai paradigma desain dan domain persoalan.

### Latihan & Soal

1. **(Pemahaman)** Jelaskan perbedaan antara *persoalan komputasi* dan *algoritma*. Berikan satu contoh persoalan dengan dua algoritma berbeda untuk menyelesaikannya.
2. **(Pemahaman)** Sebutkan tiga jenis operasi dasar yang dianggap berbiaya konstan dalam model RAM.
3. **(Analisis/HOTS)** Misalkan algoritma A berjalan dalam 100n langkah dan algoritma B dalam 2n² langkah. Untuk nilai `n` berapakah A mulai lebih cepat daripada B? Tafsirkan hasilnya dalam konteks pentingnya laju pertumbuhan.
4. **(Analisis/HOTS)** Urutkan fungsi berikut menurut laju pertumbuhan dari paling lambat ke paling cepat: n², 2ⁿ, n lg n, n!, lg n, n, n³.
5. **(Diskusi)** Mengapa pseudocode lebih disukai daripada kode bahasa pemrograman riil ketika menyajikan algoritma dalam buku teks? Apa kelemahannya?

---

# BAGIAN I — Fondasi (Foundations)

## Pengantar Bagian I

Bagian I meletakkan dasar yang akan dipakai sepanjang buku. Empat tema besar dikembangkan di sini. **Pertama**, kita memahami peran algoritma sebagai teknologi yang setara pentingnya dengan perangkat keras (Bab 1). **Kedua**, kita memulai dengan algoritma pengurutan konkret — *insertion sort* dan *merge sort* — sembari memperkenalkan dua teknik fundamental: pembuktian kebenaran melalui **loop invariant** dan desain melalui **divide-and-conquer** (Bab 2). **Ketiga**, kita membangun bahasa matematis untuk menggambarkan waktu eksekusi, yaitu **notasi asimtotik** O, Ω, dan Θ (Bab 3). **Keempat**, kita memperluas divide-and-conquer dengan teknik penyelesaian **rekurens (recurrence)**, yang berpuncak pada **Teorema Master** (Bab 4). Bagian ini ditutup dengan **analisis probabilistik dan algoritma acak** (Bab 5), yang memperkenalkan cara berpikir tentang masukan "rata-rata" dan algoritma yang membuat pilihan acak.

Tujuan keseluruhan Bagian I adalah membekali pembaca dengan kerangka berpikir: bagaimana mendesain algoritma, bagaimana membuktikannya benar, dan bagaimana menganalisis efisiensinya secara presisi.

---

## Bab 1 — Peran Algoritma dalam Komputasi

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** mengapa algoritma layak dipandang sebagai sebuah *teknologi*.
2. **Mengidentifikasi** contoh-contoh persoalan nyata yang membutuhkan algoritma efisien.
3. **Membandingkan** dampak pemilihan algoritma yang lebih baik terhadap kinerja dibandingkan peningkatan perangkat keras.
4. **Menilai** peran algoritma dalam sistem yang lebih besar (perangkat lunak, jaringan, basis data, kriptografi).

### Peta Konsep

```
Algoritma sebagai TEKNOLOGI
   |
   +-- Efisiensi algoritma vs. kecepatan perangkat keras
   +-- Persoalan nyata: rute, genom, web, kriptografi, optimasi
   +-- Persoalan "hard" (NP-complete) -> belum ada solusi efisien
```

### Materi Inti

#### Algoritma sebagai Teknologi

Walaupun komputer menjadi semakin cepat dan memori semakin murah, **algoritma yang efisien tetap krusial**. Alasannya: total kinerja sistem ditentukan oleh perangkat keras *dan* algoritma. Seringkali perbaikan algoritma menghasilkan lompatan kinerja yang jauh melampaui peningkatan perangkat keras.

Ilustrasi klasik adalah perbandingan *insertion sort* (≈ c₁n²) dengan *merge sort* (≈ c₂n lg n). Andaikan kita menjalankan insertion sort pada komputer yang sangat cepat (mis. 10 miliar instruksi/detik) dengan kode yang dioptimalkan, dan merge sort pada komputer lambat (mis. 10 juta instruksi/detik) dengan kode yang ditulis kurang efisien. Untuk masukan berukuran besar, merge sort pada komputer lambat tetap akan **menyelesaikan tugas jauh lebih dahulu** daripada insertion sort pada komputer cepat, karena keunggulan asimtotik n lg n atas n² akhirnya mendominasi semua faktor konstan dan perbedaan perangkat keras. Inilah inti pesan bahwa algoritma adalah teknologi.

#### Contoh-contoh Persoalan yang Memerlukan Algoritma

- **Proyek genom manusia:** mengidentifikasi gen, menyimpan, dan menganalisis basis data DNA memerlukan algoritma yang canggih.
- **Internet dan World Wide Web:** menemukan rute data yang baik (lihat algoritma lintasan terpendek), serta mesin pencari yang mengindeks miliaran halaman.
- **Perdagangan elektronik dan kriptografi:** keamanan transaksi bergantung pada algoritma teori bilangan seperti RSA (Bab 31).
- **Optimasi sumber daya / alokasi:** persoalan pemrograman linear (Bab 29) dan aliran jaringan (Bab 24).

#### Persoalan yang "Sulit"

Tidak semua persoalan memiliki algoritma efisien yang diketahui. Beberapa persoalan tergolong **NP-complete** (Bab 34): hingga kini tidak diketahui algoritma berwaktu polinomial untuknya, dan jika ditemukan satu saja, maka semua persoalan NP-complete dapat diselesaikan secara efisien. Mengenali bahwa suatu persoalan NP-complete penting secara praktis: alih-alih mencari solusi eksak yang mustahil cepat, kita beralih ke **algoritma aproksimasi** (Bab 35) atau heuristik.

### Istilah Kunci

- **Technology (teknologi):** dalam konteks ini, algoritma diperlakukan sebagai komponen sistem yang menentukan kinerja, setara dengan perangkat keras.
- **NP-complete:** kelas persoalan yang dipercaya tidak memiliki algoritma berwaktu polinomial (dibahas tuntas di Bab 34).
- **Order of growth (laju pertumbuhan):** ukuran utama "kebaikan" suatu algoritma untuk masukan besar.

### Studi Kasus: Algoritma vs. Perangkat Keras

Misalkan komputer A mengeksekusi 10¹⁰ operasi/detik menjalankan insertion sort (2n² operasi), dan komputer B mengeksekusi 10⁷ operasi/detik menjalankan merge sort (50 n lg n operasi). Untuk n = 10⁷ (sepuluh juta bilangan):

| Komputer | Algoritma | Estimasi waktu |
|---|---|---|
| A (cepat) | insertion sort, 2n² | 2·(10⁷)² / 10¹⁰ = 2·10¹⁴/10¹⁰ ≈ 20.000 detik (≈ 5,5 jam) |
| B (lambat) | merge sort, 50 n lg n | 50·10⁷·lg(10⁷) / 10⁷ ≈ 50·23,3 ≈ 1.163 detik (≈ 20 menit) |

Komputer lambat dengan algoritma lebih baik menang telak. Inilah argumen kuantitatif "algoritma sebagai teknologi".

### Rangkuman

Algoritma adalah teknologi inti komputasi. Efisiensi algoritma sering lebih menentukan kinerja keseluruhan daripada kecepatan perangkat keras, terutama untuk masukan besar. Algoritma hadir di balik genomika, internet, kriptografi, dan optimasi. Sebagian persoalan (NP-complete) belum memiliki solusi efisien, dan mengenali hal ini memandu kita memilih strategi alternatif.

### Latihan & Soal

1. **(Pemahaman)** Berikan dua contoh aplikasi nyata yang memerlukan algoritma efisien dan jelaskan persoalan komputasinya.
2. **(Analisis/HOTS)** Dengan parameter pada studi kasus di atas, tentukan ukuran `n` terkecil agar merge sort pada komputer B mengungguli insertion sort pada komputer A.
3. **(Diskusi)** Mengapa mengetahui bahwa sebuah persoalan adalah NP-complete tetap berguna secara praktis bagi seorang insinyur?
4. **(Analisis)** Jika perangkat keras menjadi 1000× lebih cepat, berapa kali lipat pertambahan ukuran masukan yang dapat ditangani algoritma Θ(n²) dalam waktu tetap? Bandingkan dengan algoritma Θ(n lg n).

---

## Bab 2 — Memulai: Insertion Sort dan Merge Sort

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menuliskan** pseudocode *insertion sort* dan menjelaskan cara kerjanya langkah demi langkah.
2. **Membuktikan** kebenaran insertion sort menggunakan teknik **loop invariant** (inisialisasi, pemeliharaan, terminasi).
3. **Menganalisis** waktu eksekusi kasus terbaik, terburuk, dan rata-rata insertion sort.
4. **Merancang** algoritma dengan paradigma **divide-and-conquer** dan mengilustrasikannya melalui *merge sort*.
5. **Menurunkan** rekurens waktu eksekusi merge sort dan menyimpulkan kompleksitas Θ(n lg n).

### Peta Konsep

```
PENGURUTAN
  |
  +-- Insertion sort (incremental) --> Θ(n^2) worst, Θ(n) best
  |       |
  |       +-- bukti: LOOP INVARIANT
  |
  +-- Merge sort (divide-and-conquer) --> Θ(n lg n)
          |
          +-- divide / conquer / combine
          +-- prosedur MERGE -> Θ(n)
          +-- rekurens T(n) = 2T(n/2) + Θ(n)
```

### Materi Inti

#### 2.1 Insertion Sort

**Insertion sort** adalah algoritma yang efisien untuk mengurutkan sejumlah kecil elemen. Idenya menyerupai cara seseorang menyusun kartu di tangan: ambil satu kartu, lalu sisipkan ke posisi yang benar di antara kartu-kartu yang sudah terurut di tangan kiri. Algoritma ini bersifat **incremental** dan mengurutkan **di tempat (in place)** — hanya memerlukan memori tambahan konstan.

```text
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Sisipkan A[i] ke dalam subbarisan terurut A[1 : i-1].
4      j = i - 1
5      while j > 0 and A[j] > key
6          A[j + 1] = A[j]      // geser elemen yang lebih besar ke kanan
7          j = j - 1
8      A[j + 1] = key            // tempatkan key pada posisi yang benar
```

**Penjelasan langkah:** Larik dibagi konseptual menjadi bagian kiri yang sudah terurut (`A[1 : i-1]`) dan bagian kanan yang belum. Pada setiap iterasi `for`, elemen `A[i]` (disebut `key`) "diambil keluar", lalu elemen-elemen yang lebih besar di sebelah kirinya digeser satu posisi ke kanan (baris 5–7) sampai ditemukan tempat yang tepat, dan `key` ditempatkan di situ (baris 8).

##### Bukti Kebenaran melalui Loop Invariant

> **Loop invariant (invarian perulangan)** untuk perulangan `for`:
> *Pada awal setiap iterasi perulangan baris 1–8 dengan indeks `i`, subarray `A[1 : i-1]` terdiri atas elemen-elemen yang semula ada di `A[1 : i-1]`, tetapi kini dalam keadaan terurut menaik.*

Pembuktian kebenaran dengan loop invariant memerlukan tiga hal:

1. **Inisialisasi (initialization):** Invarian benar sebelum iterasi pertama. Saat `i = 2`, subarray `A[1 : 1]` berisi satu elemen, yaitu elemen asli, dan jelas terurut.
2. **Pemeliharaan (maintenance):** Jika invarian benar sebelum suatu iterasi, ia tetap benar sebelum iterasi berikutnya. Badan perulangan menggeser `A[i-1], A[i-2], …` ke kanan sampai posisi tepat untuk `key` ditemukan, lalu menyisipkan `key`. Akibatnya `A[1 : i]` kini terurut, sehingga invarian untuk `i+1` terpenuhi.
3. **Terminasi (termination):** Perulangan berhenti ketika `i` melampaui `n`, yaitu `i = n+1`. Substitusi ke invarian memberi: `A[1 : n]` berisi elemen asli dalam keadaan terurut. Inilah keluaran yang diinginkan; algoritma benar. ∎

##### Analisis Kompleksitas

Misalkan tⱼ menyatakan banyaknya kali uji `while` (baris 5) dijalankan untuk nilai `i = j`.

- **Kasus terbaik (best case):** Larik sudah terurut. Uji `while` gagal seketika; tᵢ = 1. Waktu total adalah fungsi linear: **Θ(n)**.
- **Kasus terburuk (worst case):** Larik terurut menurun (terbalik). Setiap elemen harus dibandingkan dengan seluruh elemen di kirinya; tᵢ = i. Penjumlahan menghasilkan deret aritmetika ∑ᵢ₌₂ⁿ i = Θ(n²). Jadi waktu terburuk adalah **Θ(n²)**.
- **Kasus rata-rata (average case):** Rata-rata separuh elemen kiri harus digeser, sehingga tetap **Θ(n²)**.
- **Ruang:** **Θ(1)** tambahan (in place).

| Kasus | Waktu | Catatan |
|---|---|---|
| Terbaik | Θ(n) | masukan sudah terurut |
| Rata-rata | Θ(n²) | masukan acak |
| Terburuk | Θ(n²) | masukan terurut terbalik |
| Ruang | Θ(1) | in place, stabil |

Insertion sort bersifat **stabil (stable)**: elemen dengan kunci sama mempertahankan urutan relatif aslinya.

#### 2.2 Menganalisis Algoritma

Menganalisis algoritma berarti memprediksi sumber daya yang dibutuhkannya — terutama waktu eksekusi — dalam model RAM. Kita menyatakan waktu eksekusi sebagai fungsi ukuran masukan `n`, lalu memusatkan perhatian pada **laju pertumbuhan** fungsi tersebut (lihat Bab 3) sembari mengabaikan konstanta dan suku-suku berorde rendah.

#### 2.3 Merancang Algoritma: Divide-and-Conquer dan Merge Sort

Banyak algoritma bersifat **rekursif (recursive)**: untuk menyelesaikan persoalan, mereka memanggil dirinya sendiri pada subpersoalan yang lebih kecil. Pendekatan **divide-and-conquer** mengikuti tiga langkah pada setiap level rekursi:

1. **Divide (bagi):** pecah persoalan menjadi beberapa subpersoalan yang merupakan instance lebih kecil dari persoalan yang sama.
2. **Conquer (taklukkan):** selesaikan subpersoalan secara rekursif. Jika ukurannya cukup kecil (kasus dasar), selesaikan langsung.
3. **Combine (gabung):** gabungkan solusi subpersoalan menjadi solusi persoalan asal.

**Merge sort** menerapkan pola ini untuk pengurutan:

```text
MERGE-SORT(A, p, r)
1  if p >= r              // nol atau satu elemen? sudah terurut
2      return
3  q = ⌊(p + r) / 2⌋      // titik tengah A[p : r]
4  MERGE-SORT(A, p, q)        // urutkan rekursif A[p : q]
5  MERGE-SORT(A, q + 1, r)    // urutkan rekursif A[q+1 : r]
6  // Gabungkan A[p : q] dan A[q+1 : r] ke dalam A[p : r].
7  MERGE(A, p, q, r)
```

Inti penggabungan ada pada prosedur `MERGE`, yang menggabungkan dua subarray terurut `A[p : q]` dan `A[q+1 : r]` menjadi satu subarray terurut `A[p : r]` dalam waktu **Θ(n)** untuk total n = r − p + 1 elemen. Idenya: bandingkan elemen terkecil dari kedua subarray dan salin yang lebih kecil ke larik hasil, ulangi sampai habis. Penggunaan nilai **sentinel (∞)** di akhir setiap subarray menyederhanakan penanganan kondisi habis.

```text
MERGE(A, p, q, r)
 1  nL = q - p + 1                  // panjang A[p : q]
 2  nR = r - q                      // panjang A[q+1 : r]
 3  misalkan L[0 : nL-1] dan R[0 : nR-1] larik baru
 4  for i = 0 to nL - 1             // salin A[p : q] ke L
 5      L[i] = A[p + i]
 6  for j = 0 to nR - 1             // salin A[q+1 : r] ke R
 7      R[j] = A[q + j + 1]
 8  i = 0; j = 0; k = p
 9  while i < nL and j < nR         // selama kedua larik masih ada elemen
10      if L[i] <= R[j]
11          A[k] = L[i]; i = i + 1
12      else A[k] = R[j]; j = j + 1
13      k = k + 1
14  while i < nL                    // sisa L
15      A[k] = L[i]; i = i + 1; k = k + 1
16  while j < nR                    // sisa R
17      A[k] = R[j]; j = j + 1; k = k + 1
```

##### Analisis: Rekurens Merge Sort

Misalkan T(n) waktu terburuk merge sort pada n elemen. Untuk n = 1, waktunya konstan Θ(1). Untuk n > 1: langkah *divide* menghitung titik tengah dalam Θ(1); langkah *conquer* menyelesaikan dua subpersoalan berukuran n/2 dengan biaya 2T(n/2); langkah *combine* (MERGE) memerlukan Θ(n). Maka:

> T(n) = Θ(1), bila n = 1
> T(n) = 2T(n/2) + Θ(n), bila n > 1

Penyelesaian rekurens ini (lihat Bab 4) memberikan **T(n) = Θ(n lg n)**. Karena n lg n tumbuh lebih lambat daripada n², merge sort mengungguli insertion sort untuk `n` yang cukup besar. Kekurangan merge sort: ia **tidak in place** — versi standar memerlukan ruang tambahan Θ(n) untuk larik bantu pada MERGE.

| Algoritma | Waktu terbaik | Waktu rata-rata | Waktu terburuk | Ruang | Stabil? |
|---|---|---|---|---|---|
| Insertion sort | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) | ya |
| Merge sort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Θ(n) | ya |

### Istilah Kunci

- **Insertion sort:** algoritma pengurutan incremental, in place, stabil; terbaik untuk n kecil.
- **Loop invariant (invarian perulangan):** pernyataan yang benar pada awal setiap iterasi; alat baku pembuktian kebenaran (inisialisasi, pemeliharaan, terminasi).
- **In place (di tempat):** algoritma yang hanya memerlukan memori tambahan konstan.
- **Stable sort (pengurutan stabil):** mempertahankan urutan relatif elemen berkunci sama.
- **Divide-and-conquer:** paradigma bagi–taklukkan–gabung.
- **Merge (penggabungan):** menggabung dua barisan terurut menjadi satu dalam waktu linear.
- **Recurrence (rekurens):** persamaan yang mendefinisikan T(n) dalam bentuk T pada masukan lebih kecil.
- **Sentinel:** nilai penjaga (mis. ∞) yang menyederhanakan kondisi batas.

### Contoh / Studi Kasus: Trace Insertion Sort

Urutkan A = ⟨5, 2, 4, 6, 1, 3⟩. Tabel menunjukkan isi larik setelah setiap iterasi `for` (nilai `i`):

| Iterasi (i) | key | Larik setelah penyisipan |
|---|---|---|
| awal | — | [5, 2, 4, 6, 1, 3] |
| i=2 | 2 | [2, 5, 4, 6, 1, 3] |
| i=3 | 4 | [2, 4, 5, 6, 1, 3] |
| i=4 | 6 | [2, 4, 5, 6, 1, 3] |
| i=5 | 1 | [1, 2, 4, 5, 6, 3] |
| i=6 | 3 | [1, 2, 3, 4, 5, 6] |

### Contoh / Studi Kasus: Trace Merge Sort

Untuk A = ⟨5, 2, 4, 7, 1, 3, 2, 6⟩ (n = 8), pohon rekursi membagi hingga 1 elemen lalu menggabung:

```
[5 2 4 7 1 3 2 6]
   /            \
[5 2 4 7]    [1 3 2 6]
  / \          / \
[5 2][4 7]  [1 3][2 6]
 ...merge ke atas...
[2 5][4 7] -> [2 4 5 7]      [1 3][2 6] -> [1 2 3 6]
[2 4 5 7] + [1 2 3 6] -> [1 2 2 3 4 5 6 7]
```

### Rangkuman

Insertion sort menyusun larik secara incremental dengan waktu Θ(n²) terburuk tetapi Θ(n) untuk masukan hampir terurut, in place dan stabil. Merge sort menerapkan divide-and-conquer untuk mencapai Θ(n lg n) pada semua kasus, dengan ongkos ruang tambahan Θ(n). Loop invariant adalah alat baku membuktikan kebenaran perulangan, sementara rekurens adalah alat baku menganalisis algoritma rekursif.

### Latihan & Soal

1. **(Tracing)** Jalankan insertion sort pada A = ⟨31, 41, 59, 26, 41, 58⟩ dan tunjukkan larik setelah setiap iterasi.
2. **(Pemahaman)** Tulis ulang INSERTION-SORT agar mengurutkan menurun (descending).
3. **(Analisis/HOTS)** Buktikan kebenaran MERGE menggunakan loop invariant untuk perulangan baris 9–13.
4. **(Analisis)** Tunjukkan bahwa waktu terburuk insertion sort adalah Θ(n²) dengan menuliskan dan mengevaluasi penjumlahan yang relevan.
5. **(Implementasi)** Persoalan pencarian: tulis pseudocode *linear search* dan rumuskan loop invariant-nya; nyatakan waktu terbaik/terburuknya.
6. **(HOTS)** *Inversi*: pasangan indeks (i, j) dengan i < j tetapi A[i] > A[j]. Jelaskan hubungan antara jumlah inversi dan waktu eksekusi insertion sort. Rancang modifikasi merge sort untuk menghitung jumlah inversi dalam Θ(n lg n).

---

## Bab 3 — Mengkarakterisasi Waktu Eksekusi (Notasi Asimtotik)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** secara formal notasi O, Ω, dan Θ beserta notasi ketat o dan ω.
2. **Membuktikan** keanggotaan suatu fungsi dalam kelas asimtotik tertentu menggunakan definisi (konstanta c dan n₀).
3. **Menerapkan** notasi asimtotik untuk menyederhanakan ekspresi waktu eksekusi.
4. **Membedakan** batas atas (upper bound), batas bawah (lower bound), dan batas ketat (tight bound).
5. **Mengenali** fungsi dan notasi standar: logaritma, eksponen, faktorial, fungsi lantai/langit-langit.

### Peta Konsep

```
NOTASI ASIMTOTIK
  |
  +-- O(g)  : batas ATAS asimtotik (<=)
  +-- Ω(g)  : batas BAWAH asimtotik (>=)
  +-- Θ(g)  : batas KETAT (=), iff O dan Ω
  +-- o(g)  : batas atas TIDAK ketat (<)
  +-- ω(g)  : batas bawah TIDAK ketat (>)
```

### Materi Inti

#### 3.1 Notasi O, Ω, dan Θ

Notasi asimtotik menggambarkan perilaku fungsi waktu eksekusi T(n) ketika n menuju tak hingga, dengan mengabaikan konstanta perkalian dan suku-suku berorde rendah. Fungsi yang dimaksud didefinisikan atas bilangan asli.

> **Notasi Θ (Theta) — batas ketat asimtotik.**
> Θ(g(n)) = { f(n) : terdapat konstanta positif c₁, c₂, dan n₀ sehingga 0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n) untuk semua n ≥ n₀ }.
> Artinya f(n) terjepit (sandwiched) antara c₁·g(n) dan c₂·g(n) untuk n yang cukup besar. Kita tulis f(n) = Θ(g(n)).

> **Notasi O (Big-Oh) — batas atas asimtotik.**
> O(g(n)) = { f(n) : terdapat konstanta positif c dan n₀ sehingga 0 ≤ f(n) ≤ c·g(n) untuk semua n ≥ n₀ }.
> O memberikan batas atas: f tumbuh tidak lebih cepat dari g (hingga faktor konstan).

> **Notasi Ω (Big-Omega) — batas bawah asimtotik.**
> Ω(g(n)) = { f(n) : terdapat konstanta positif c dan n₀ sehingga 0 ≤ c·g(n) ≤ f(n) untuk semua n ≥ n₀ }.
> Ω memberikan batas bawah: f tumbuh tidak lebih lambat dari g.

**Teorema (hubungan Θ, O, Ω):** Untuk dua fungsi f dan g, f(n) = Θ(g(n)) jika dan hanya jika f(n) = O(g(n)) dan f(n) = Ω(g(n)). Dengan kata lain, batas ketat sama dengan batas atas sekaligus batas bawah.

#### 3.2 Definisi Formal dan Contoh

**Contoh 1.** Tunjukkan bahwa ½n² − 3n = Θ(n²). Kita cari c₁, c₂, n₀ sehingga c₁n² ≤ ½n² − 3n ≤ c₂n². Membagi dengan n²: c₁ ≤ ½ − 3/n ≤ c₂. Ruas kanan dipenuhi oleh c₂ = ½ untuk semua n ≥ 1. Ruas kiri dipenuhi oleh c₁ = 1/14 untuk n ≥ 7. Maka dengan n₀ = 7, c₁ = 1/14, c₂ = ½, kesetaraan asimtotik terbukti. ∎

**Contoh 2.** 6n³ ≠ Θ(n²): tidak ada konstanta c₂ sehingga 6n³ ≤ c₂n² untuk semua n besar, sebab itu menuntut 6n ≤ c₂, mustahil saat n → ∞.

**Notasi tidak ketat:**

> **o (little-oh):** f(n) = o(g(n)) berarti untuk *setiap* konstanta c > 0 terdapat n₀ sehingga 0 ≤ f(n) < c·g(n) untuk n ≥ n₀. Intuisi: f menjadi *tidak signifikan* relatif terhadap g; lim f(n)/g(n) = 0. Contoh: 2n = o(n²).
> **ω (little-omega):** kebalikan o; f(n) = ω(g(n)) berarti g(n) = o(f(n)); lim f(n)/g(n) = ∞. Contoh: n²/2 = ω(n).

#### 3.3 Notasi dan Fungsi Standar

- **Monotonisitas:** fungsi monoton naik/turun.
- **Lantai dan langit-langit:** ⌊x⌋ = bilangan bulat terbesar ≤ x; ⌈x⌉ = bilangan bulat terkecil ≥ x. Berlaku x − 1 < ⌊x⌋ ≤ x ≤ ⌈x⌉ < x + 1.
- **Logaritma:** lg n = log₂ n; ln n = logₑ n. Identitas penting: a^(log_b c) = c^(log_b a); log_b(xy) = log_b x + log_b y; log_b a = (ln a)/(ln b). Dalam notasi asimtotik, basis logaritma tidak penting karena hanya berbeda faktor konstan: log_b n = Θ(lg n).
- **Eksponen dan faktorial:** n! tumbuh lebih cepat daripada 2ⁿ. **Aproksimasi Stirling:** n! = √(2πn)·(n/e)ⁿ·(1 + Θ(1/n)), sehingga lg(n!) = Θ(n lg n).
- **Fungsi iterasi logaritma:** lg* n (log bintang), tumbuh sangat lambat; muncul pada analisis disjoint sets.

**Kaidah praktis menyederhanakan:** abaikan konstanta perkalian dan ambil suku dominan. Contoh: 3n³ + 100n² + 7 = Θ(n³); 5 lg n + 2 = Θ(lg n).

### Istilah Kunci

- **Asymptotic notation (notasi asimtotik):** notasi untuk laju pertumbuhan fungsi pada n besar.
- **O / Ω / Θ:** batas atas / batas bawah / batas ketat asimtotik.
- **o / ω:** batas atas / bawah yang tidak ketat (strictly).
- **Tight bound (batas ketat):** Θ; deskripsi paling informatif.
- **Stirling's approximation:** aproksimasi untuk n!.
- **Floor / ceiling (lantai/langit-langit):** ⌊x⌋ dan ⌈x⌉.

### Contoh / Studi Kasus: Klasifikasi Fungsi

| f(n) | Kelas ketat | Alasan singkat |
|---|---|---|
| 7n + 3 | Θ(n) | linear, abaikan konstanta |
| 2n² + n lg n | Θ(n²) | n² mendominasi n lg n |
| lg(n!) | Θ(n lg n) | dari Stirling |
| 3ⁿ + n¹⁰ | Θ(3ⁿ) | eksponensial mengalahkan polinomial |
| 100 | Θ(1) | konstan |

### Rangkuman

Notasi asimtotik adalah bahasa untuk menggambarkan laju pertumbuhan. Θ memberi batas ketat, O batas atas, Ω batas bawah, sedangkan o dan ω adalah versi tak ketat. Saat menganalisis algoritma, kita menyederhanakan ekspresi waktu dengan mengabaikan konstanta dan suku rendah, lalu menyatakan hasilnya dengan notasi yang paling informatif (biasanya Θ untuk satu algoritma, atau O ketika hanya batas atas yang dapat dijamin).

### Latihan & Soal

1. **(Pemahaman)** Buktikan dengan definisi bahwa 3n² + 10n = Θ(n²); sebutkan c₁, c₂, n₀.
2. **(Pemahaman)** Apakah 2^(n+1) = O(2ⁿ)? Apakah 2^(2n) = O(2ⁿ)? Jelaskan.
3. **(Analisis/HOTS)** Buktikan bahwa untuk fungsi nonnegatif, max(f(n), g(n)) = Θ(f(n) + g(n)).
4. **(Analisis)** Buktikan o(g) ∩ ω(g) = ∅ (suatu fungsi tidak bisa sekaligus o(g) dan ω(g)).
5. **(HOTS)** Susun urutan kelas asimtotik berikut menaik: n, 2ⁿ, n lg n, n^(1/2), n!, (lg n)², n/lg n, n^lg n.

---

## Bab 4 — Divide-and-Conquer dan Teorema Master

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Memformulasikan** rekurens dari algoritma divide-and-conquer.
2. **Menyelesaikan** rekurens dengan metode **substitusi**, **pohon rekursi (recursion tree)**, dan **metode master**.
3. **Menyatakan** ketiga kasus **Teorema Master** secara tepat dan menerapkannya.
4. **Menganalisis** algoritma perkalian matriks naif dan **algoritma Strassen**.
5. **Mengevaluasi** kapan Teorema Master tidak berlaku dan alternatif (mis. Akra-Bazzi).

### Peta Konsep

```
REKURENS T(n) = a T(n/b) + f(n)
   |
   +-- Metode substitusi (tebak + induksi)
   +-- Metode pohon rekursi (jumlahkan biaya per level)
   +-- METODE MASTER (3 kasus, bandingkan f(n) vs n^(log_b a))
Aplikasi: Merge sort, perkalian matriks (naif Θ(n^3), Strassen Θ(n^2.81))
```

### Materi Inti

#### 4.1 Perkalian Matriks dan Strassen

Perkalian dua matriks n×n secara langsung (definisi cᵢⱼ = ∑ aᵢₖ·bₖⱼ) memerlukan **Θ(n³)** operasi skalar. Pendekatan divide-and-conquer naif membagi matriks menjadi blok-blok n/2 × n/2 dan menghasilkan rekurens T(n) = 8T(n/2) + Θ(n²), yang juga bermuara ke Θ(n³).

**Algoritma Strassen** mengurangi jumlah perkalian rekursif dari 8 menjadi **7** (dengan menambah beberapa penjumlahan), menghasilkan rekurens:

> T(n) = 7T(n/2) + Θ(n²)

yang berdasarkan Teorema Master menghasilkan **T(n) = Θ(n^(lg 7)) ≈ Θ(n^2.81)**, lebih baik daripada Θ(n³) secara asimtotik. Strassen menjadi tonggak sejarah karena menunjukkan bahwa batas Θ(n³) bukanlah batas alami.

#### 4.2 Metode Substitusi

Langkah: (1) **Tebak** bentuk solusi. (2) Gunakan **induksi matematika** untuk menentukan konstanta dan membuktikan tebakan.

**Contoh.** Untuk T(n) = 2T(⌊n/2⌋) + n, kita tebak T(n) = O(n lg n). Hipotesis induksi: T(m) ≤ c·m lg m untuk m < n. Maka T(n) ≤ 2·c·⌊n/2⌋·lg⌊n/2⌋ + n ≤ c·n·lg(n/2) + n = c·n·lg n − c·n + n ≤ c·n·lg n asalkan c ≥ 1. Tebakan terbukti. ∎

#### 4.3 Metode Pohon Rekursi

Pohon rekursi memvisualkan biaya tiap level. Untuk T(n) = 2T(n/2) + cn (merge sort), tiap level berbiaya total cn, dan ada lg n + 1 level, sehingga total Θ(n lg n). Pohon rekursi cocok untuk *menebak* solusi yang lalu diverifikasi dengan substitusi.

#### 4.5 Metode Master

Metode master memberi "resep" untuk rekurens berbentuk:

> T(n) = a·T(n/b) + f(n),  dengan a > 0 dan b > 1 konstanta, f(n) fungsi *driving* (mengemudi) nonnegatif.

Di sini a adalah jumlah subpersoalan, n/b ukuran tiap subpersoalan, dan f(n) biaya divide + combine. Fungsi **watershed (pembatas air)** adalah n^(log_b a). Kita membandingkan f(n) dengan watershed.

> **Teorema Master (Theorem 4.1 pada CLRS).** Dengan a > 0, b > 1, dan f(n) nonnegatif:
> 1. **Kasus 1.** Jika f(n) = O(n^(log_b a − ε)) untuk suatu konstanta ε > 0, maka **T(n) = Θ(n^(log_b a))**. (Watershed mendominasi; biaya daun mendominasi.)
> 2. **Kasus 2.** Jika f(n) = Θ(n^(log_b a)·lg^k n) untuk suatu konstanta k ≥ 0, maka **T(n) = Θ(n^(log_b a)·lg^(k+1) n)**. (Pertumbuhan setara; tambah satu faktor lg n. Kasus tersering: k = 0 → Θ(n^(log_b a)·lg n).)
> 3. **Kasus 3.** Jika f(n) = Ω(n^(log_b a + ε)) untuk suatu ε > 0, **dan** memenuhi *kondisi regularitas* a·f(n/b) ≤ c·f(n) untuk suatu c < 1 dan n cukup besar, maka **T(n) = Θ(f(n))**. (Fungsi driving mendominasi; biaya akar mendominasi.)

Catatan penting: pada Kasus 1 dan 3, pemisahan antara f(n) dan watershed harus **polinomial** (selisih berfaktor n^ε). Bila pemisahannya hanya logaritmik, Teorema Master tidak berlaku — terdapat "celah" antara Kasus 1 dan 2, serta antara Kasus 2 dan 3.

**Penerapan (tiga contoh kanonik):**

| Rekurens | a, b | n^(log_b a) | f(n) | Kasus | Solusi |
|---|---|---|---|---|---|
| T(n)=9T(n/3)+n | 9, 3 | n² | n | Kasus 1 (ε≤1) | Θ(n²) |
| T(n)=T(2n/3)+1 | 1, 3/2 | n⁰=1 | 1 | Kasus 2 (k=0) | Θ(lg n) |
| T(n)=3T(n/4)+n lg n | 3, 4 | n^0.793 | n lg n | Kasus 3 | Θ(n lg n) |
| T(n)=2T(n/2)+Θ(n) | 2, 2 | n | n | Kasus 2 | **Θ(n lg n)** (merge sort) |
| T(n)=7T(n/2)+Θ(n²) | 7, 2 | n^2.81 | n² | Kasus 1 | **Θ(n^lg7)** (Strassen) |

#### 4.6–4.7 Catatan Lanjutan

CLRS menyertakan bukti **teorema master kontinu** dan metode **Akra-Bazzi** yang lebih umum (mampu menangani rekurens dengan subpersoalan berukuran tak seragam). Akra-Bazzi berguna ketika Teorema Master tidak mencakup bentuk rekurens yang dihadapi.

### Istilah Kunci

- **Recurrence (rekurens):** persamaan T(n) dalam bentuk T pada argumen lebih kecil.
- **Substitution method (metode substitusi):** tebak solusi lalu buktikan dengan induksi.
- **Recursion tree (pohon rekursi):** visualisasi biaya tiap level rekursi.
- **Master method / Master theorem:** resep penyelesaian T(n) = aT(n/b) + f(n).
- **Watershed function (fungsi pembatas):** n^(log_b a), pembanding terhadap f(n).
- **Regularity condition (kondisi regularitas):** a·f(n/b) ≤ c·f(n), c < 1; syarat Kasus 3.
- **Strassen's algorithm:** perkalian matriks Θ(n^lg7).
- **Akra-Bazzi:** metode rekurens yang lebih umum dari master theorem.

### Contoh / Studi Kasus: Memilih Kasus Master

Selesaikan T(n) = 4T(n/2) + n. Di sini a = 4, b = 2 → n^(log₂4) = n². f(n) = n = O(n^(2−1)). Pemisahan polinomial dengan ε = 1 → **Kasus 1**, sehingga **T(n) = Θ(n²)**.

Selesaikan T(n) = 4T(n/2) + n². Watershed n²; f(n) = n² = Θ(n²·lg⁰n) → **Kasus 2** (k = 0) → **T(n) = Θ(n² lg n)**.

Selesaikan T(n) = 4T(n/2) + n³. f(n) = n³ = Ω(n^(2+1)); cek regularitas: 4·(n/2)³ = n³/2 ≤ c·n³ dengan c = ½ < 1 → **Kasus 3** → **T(n) = Θ(n³)**.

### Rangkuman

Rekurens adalah jantung analisis divide-and-conquer. Tiga metode penyelesaian: substitusi (tebak+induksi), pohon rekursi (jumlah per level), dan metode master (resep tiga kasus). Teorema Master membandingkan fungsi driving f(n) dengan watershed n^(log_b a). Strassen menunjukkan kekuatan pendekatan ini dengan menurunkan perkalian matriks ke Θ(n^2.81). Ketika Teorema Master tak berlaku (pemisahan non-polinomial), gunakan Akra-Bazzi atau metode lain.

### Latihan & Soal

1. **(Pemahaman)** Nyatakan ketiga kasus Teorema Master dengan kata-kata Anda sendiri.
2. **(Tracing/Analisis)** Selesaikan dengan metode master: (a) T(n)=2T(n/4)+1; (b) T(n)=2T(n/4)+√n; (c) T(n)=2T(n/4)+n; (d) T(n)=2T(n/4)+n².
3. **(HOTS)** Mengapa T(n)=2T(n/2)+n lg n tidak dapat diselesaikan langsung oleh Kasus 3? Selesaikan dengan pohon rekursi.
4. **(Analisis)** Gunakan metode substitusi untuk membuktikan T(n)=T(n−1)+n adalah Θ(n²).
5. **(HOTS)** Jelaskan mengapa kondisi regularitas diperlukan pada Kasus 3 dan berikan intuisinya melalui pohon rekursi.

---

## Bab 5 — Analisis Probabilistik dan Algoritma Acak

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** the hiring problem sebagai motivasi analisis probabilistik.
2. **Menggunakan** indicator random variable untuk menghitung nilai harapan.
3. **Membedakan** analisis kasus rata-rata (asumsi distribusi masukan) dan algoritma acak (randomisasi internal).
4. **Menganalisis** waktu harapan algoritma acak, mis. randomized hiring dan permutasi acak.

### Peta Konsep

```
KETIDAKPASTIAN
  |
  +-- Analisis probabilistik: ASUMSI distribusi masukan
  +-- Algoritma acak: algoritma MEMBUAT pilihan acak
        |
        +-- Indicator random variable I{A} (0/1)
        +-- E[X] linearitas harapan -> hitung biaya rata-rata
```

### Materi Inti

#### 5.1 The Hiring Problem

**Persoalan perekrutan (hiring problem):** Anda mewawancarai n kandidat satu per satu untuk satu posisi. Setiap kali kandidat lebih baik dari asisten saat ini, Anda memecat asisten lama dan merekrut yang baru (berbiaya tinggi cₕ). Berapa biaya perekrutan yang diharapkan?

```text
HIRE-ASSISTANT(n)
1  best = 0                    // kandidat fiktif terburuk
2  for i = 1 to n
3      wawancarai kandidat i
4      if kandidat i lebih baik dari kandidat best
5          best = i
6          rekrut kandidat i   // berbiaya cH
```

**Kasus terburuk:** kandidat datang dalam urutan menaik kualitas → kita merekrut n kali, biaya Θ(n·cₕ). Tetapi ini pesimistis. Analisis probabilistik bertanya: berapa biaya *rata-rata*?

#### 5.2 Indicator Random Variable

> **Indicator random variable (variabel acak indikator)** untuk kejadian A:
> I{A} = 1 jika A terjadi, 0 jika tidak. Sifat kunci: **E[I{A}] = Pr{A}** (nilai harapan indikator = probabilitas kejadian).

Misalkan Xᵢ = I{kandidat i direkrut}. Total perekrutan X = ∑ᵢ Xᵢ. Dengan **linearitas harapan**:

E[X] = ∑ᵢ E[Xᵢ] = ∑ᵢ Pr{kandidat i direkrut}.

Kandidat i direkrut jika dan hanya jika ia lebih baik dari i−1 kandidat sebelumnya, yaitu ia yang terbaik di antara i kandidat pertama. Pada urutan acak seragam, peluangnya **1/i**. Maka:

E[X] = ∑ᵢ₌₁ⁿ (1/i) = Hₙ = ln n + O(1) = **Θ(lg n)**.

Jadi secara rata-rata kita hanya merekrut sekitar ln n kali — jauh lebih kecil daripada n. (Hₙ adalah **bilangan harmonik**.)

#### 5.3 Algoritma Acak

Bila kita tidak mau bergantung pada asumsi distribusi masukan, kita dapat **mengacak masukan sendiri**: permutasikan kandidat secara acak seragam sebelum diproses (RANDOMIZED-HIRE-ASSISTANT). Dengan demikian *tidak ada* masukan terburuk tetap; analisis berlaku atas keacakan internal algoritma, bukan atas asumsi distribusi alami masukan. Biaya harapannya tetap Θ(cₕ·lg n).

Untuk mempermutasi larik secara acak seragam, gunakan:

```text
RANDOMIZE-IN-PLACE(A, n)
1  for i = 1 to n
2      tukar A[i] dengan A[RANDOM(i, n)]   // pilih indeks acak i..n
```

Prosedur ini menghasilkan **permutasi acak seragam** (uniform random permutation): setiap dari n! permutasi berpeluang sama 1/n!. Buktinya menggunakan loop invariant bahwa sebelum iterasi ke-i, subarray A[1 : i−1] berisi salah satu dari (n)(n−1)…(n−i+2) permutasi parsial dengan peluang sama.

**Perbedaan penting:**
- **Analisis probabilistik** mengasumsikan masukan berasal dari distribusi tertentu; hasilnya adalah perilaku *rata-rata atas masukan*.
- **Algoritma acak** membuat keputusan acak; waktunya disebut **expected running time (waktu harapan)** dan tidak bergantung pada distribusi masukan.

### Istilah Kunci

- **Probabilistic analysis (analisis probabilistik):** analisis dengan asumsi distribusi pada masukan.
- **Randomized algorithm (algoritma acak):** algoritma yang membuat pilihan acak internal.
- **Indicator random variable (variabel indikator):** I{A} ∈ {0,1} dengan E[I{A}] = Pr{A}.
- **Linearity of expectation (linearitas harapan):** E[∑Xᵢ] = ∑E[Xᵢ], berlaku tanpa syarat kebebasan.
- **Harmonic number (bilangan harmonik):** Hₙ = ∑1/i = ln n + O(1).
- **Expected running time (waktu harapan):** ekspektasi waktu atas keacakan algoritma.
- **Uniform random permutation:** permutasi acak dengan tiap susunan berpeluang sama.

### Contoh / Studi Kasus: Hiring untuk n = 4

Jika kualitas datang dalam urutan acak, peluang merekrut pada langkah i adalah 1/i. E[X] = 1 + 1/2 + 1/3 + 1/4 = 25/12 ≈ 2,08. Bandingkan dengan kasus terburuk 4 perekrutan.

### Rangkuman

Analisis probabilistik dan algoritma acak menangani ketidakpastian masukan. Indicator random variable, bersama linearitas harapan, adalah alat ampuh untuk menghitung biaya rata-rata: pada hiring problem menghasilkan E[X] = Hₙ = Θ(lg n). Mengacak masukan sendiri (randomisasi) menghilangkan ketergantungan pada asumsi distribusi dan menjadi fondasi algoritma seperti randomized quicksort (Bab 7) dan randomized selection (Bab 9).

### Latihan & Soal

1. **(Pemahaman)** Definisikan indicator random variable dan buktikan E[I{A}] = Pr{A}.
2. **(Analisis)** Dengan indikator, hitung nilai harapan banyaknya "kemunculan terbaik sejauh ini" pada permutasi acak n elemen.
3. **(HOTS)** Buktikan RANDOMIZE-IN-PLACE menghasilkan permutasi acak seragam menggunakan loop invariant.
4. **(Analisis)** Pada hiring problem, berapa peluang Anda merekrut tepat satu kali (hanya kandidat pertama)?
5. **(HOTS)** Jelaskan perbedaan jaminan yang diberikan analisis kasus rata-rata versus analisis algoritma acak terhadap "masukan musuh (adversarial input)".

---

# BAGIAN II — Pengurutan dan Statistik Terurut

## Pengantar Bagian II

Pengurutan (sorting) adalah persoalan fundamental dengan banyak algoritma yang mengilustrasikan beragam teknik desain. Bagian ini membahas **heapsort** (Bab 6) yang memanfaatkan struktur data *heap*; **quicksort** (Bab 7) yang cepat dalam praktik dengan randomisasi; **pengurutan waktu linear** (Bab 8) yang menembus batas Ω(n lg n) dengan asumsi tambahan tentang masukan; dan **median serta statistik terurut** (Bab 9) yang memilih elemen ke-k.

**Batas bawah penting:** setiap algoritma pengurutan berbasis **perbandingan (comparison sort)** memerlukan **Ω(n lg n)** perbandingan dalam kasus terburuk. Heapsort dan merge sort mencapai batas ini (optimal secara asimtotik); quicksort mencapainya rata-rata. Algoritma waktu linear (counting, radix, bucket) bukan comparison sort sehingga dapat lebih cepat dengan asumsi khusus.

| Algoritma | Terbaik | Rata-rata | Terburuk | Ruang | In place | Stabil |
|---|---|---|---|---|---|---|
| Insertion sort | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) | ya | ya |
| Merge sort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Θ(n) | tidak | ya |
| Heapsort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Θ(1) | ya | tidak |
| Quicksort | Θ(n lg n) | Θ(n lg n) | Θ(n²) | Θ(lg n)* | ya | tidak |
| Counting sort | Θ(n+k) | Θ(n+k) | Θ(n+k) | Θ(n+k) | tidak | ya |
| Radix sort | Θ(d(n+k)) | Θ(d(n+k)) | Θ(d(n+k)) | Θ(n+k) | tidak | ya |
| Bucket sort | Θ(n) | Θ(n) | Θ(n²) | Θ(n) | tidak | ya |

(*Ruang quicksort adalah ukuran tumpukan rekursi; Θ(lg n) harapan dengan partisi seimbang.)

---

## Bab 6 — Heapsort

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** struktur data *binary heap* dan properti max-heap/min-heap.
2. **Mengimplementasikan** prosedur MAX-HEAPIFY, BUILD-MAX-HEAP, dan HEAPSORT dalam pseudocode.
3. **Membuktikan** bahwa BUILD-MAX-HEAP berjalan dalam waktu linear O(n).
4. **Menganalisis** waktu eksekusi heapsort sebagai Θ(n lg n).
5. **Menerapkan** heap sebagai **priority queue** dengan operasi sisip/ekstrak.

### Peta Konsep

```
BINARY HEAP (array, complete binary tree)
  |  PARENT(i)=⌊i/2⌋, LEFT(i)=2i, RIGHT(i)=2i+1
  +-- MAX-HEAPIFY (O(lg n))  : perbaiki 1 pelanggaran
  +-- BUILD-MAX-HEAP (O(n))  : bangun heap dari array
  +-- HEAPSORT (Θ(n lg n))   : ekstrak max berulang
  +-- PRIORITY QUEUE         : INSERT, MAXIMUM, EXTRACT-MAX, INCREASE-KEY
```

### Materi Inti

#### 6.1 Heap

**Binary heap** adalah larik yang dapat dipandang sebagai **pohon biner hampir lengkap (nearly complete binary tree)**: setiap level penuh kecuali mungkin level terbawah, yang terisi dari kiri. Larik `A` memiliki atribut `A.heap-size`. Indeks akar adalah 1, dan untuk simpul `i`:

- `PARENT(i) = ⌊i/2⌋`
- `LEFT(i) = 2i`
- `RIGHT(i) = 2i + 1`

Pada **max-heap**, berlaku **max-heap property**: A[PARENT(i)] ≥ A[i] untuk setiap i selain akar — nilai induk selalu ≥ nilai anak, sehingga elemen terbesar berada di akar. Pada **min-heap** berlaku sebaliknya (akar = minimum). Tinggi heap berisi n elemen adalah Θ(lg n).

#### 6.2 Memelihara Properti Heap: MAX-HEAPIFY

MAX-HEAPIFY mengasumsikan subpohon di LEFT(i) dan RIGHT(i) sudah max-heap, tetapi A[i] mungkin lebih kecil dari anaknya sehingga melanggar properti. Prosedur "menenggelamkan" A[i] ke bawah hingga properti pulih.

```text
MAX-HEAPIFY(A, i)
 1  l = LEFT(i)
 2  r = RIGHT(i)
 3  if l <= A.heap-size and A[l] > A[i]
 4      largest = l
 5  else largest = i
 6  if r <= A.heap-size and A[r] > A[largest]
 7      largest = r
 8  if largest != i
 9      tukar A[i] dengan A[largest]
10      MAX-HEAPIFY(A, largest)        // rekursi ke subpohon terpengaruh
```

**Analisis:** T(n) ≤ T(2n/3) + Θ(1), sebab subpohon anak berukuran maksimum 2n/3 (terburuk saat level terbawah terisi separuh). Menurut Kasus 2 Teorema Master, **T(n) = O(lg n)** — atau setara, O(h) untuk simpul berketinggian h.

#### 6.3 Membangun Heap: BUILD-MAX-HEAP

Elemen A[⌊n/2⌋+1 : n] adalah daun (heap berisi 1 elemen). BUILD-MAX-HEAP memanggil MAX-HEAPIFY pada simpul internal dari bawah ke atas:

```text
BUILD-MAX-HEAP(A, n)
1  A.heap-size = n
2  for i = ⌊n/2⌋ downto 1
3      MAX-HEAPIFY(A, i)
```

**Analisis waktu linear:** Walau ada O(n) panggilan MAX-HEAPIFY masing-masing O(lg n) (memberi batas longgar O(n lg n)), batas yang lebih ketat memanfaatkan fakta bahwa biaya MAX-HEAPIFY adalah O(h) dan jumlah simpul berketinggian h paling banyak ⌈n/2^(h+1)⌉. Maka total biaya:

> ∑_{h=0}^{⌊lg n⌋} ⌈n/2^(h+1)⌉ · O(h) = O(n · ∑_{h=0}^∞ h/2^h) = O(n · 2) = **O(n)**.

Jadi BUILD-MAX-HEAP berjalan dalam **waktu linear O(n)**. (Digunakan deret ∑ h/2^h = 2.)

#### 6.4 Algoritma Heapsort

Heapsort: bangun max-heap, lalu berulang kali tukar akar (maksimum) dengan elemen terakhir, kecilkan heap, dan pulihkan properti dengan MAX-HEAPIFY.

```text
HEAPSORT(A, n)
1  BUILD-MAX-HEAP(A, n)
2  for i = n downto 2
3      tukar A[1] dengan A[i]        // tempatkan maksimum di posisi akhir
4      A.heap-size = A.heap-size - 1 // singkirkan elemen yang sudah benar
5      MAX-HEAPIFY(A, 1)             // pulihkan max-heap pada sisa
```

**Analisis:** BUILD-MAX-HEAP O(n); perulangan menjalankan n−1 kali MAX-HEAPIFY masing-masing O(lg n) → O(n lg n). Total **Θ(n lg n)**, in place, **ruang Θ(1)**. Heapsort **tidak stabil**.

#### 6.5 Priority Queue

**Priority queue** memelihara himpunan S elemen berkunci dan mendukung: INSERT, MAXIMUM, EXTRACT-MAX, INCREASE-KEY (untuk max-priority queue). Diimplementasikan dengan heap, semua operasi berjalan **O(lg n)**.

```text
HEAP-EXTRACT-MAX(A)
1  if A.heap-size < 1
2      error "heap underflow"
3  max = A[1]
4  A[1] = A[A.heap-size]
5  A.heap-size = A.heap-size - 1
6  MAX-HEAPIFY(A, 1)
7  return max

HEAP-INCREASE-KEY(A, i, key)
1  if key < A[i]
2      error "kunci baru lebih kecil dari kunci saat ini"
3  A[i] = key
4  while i > 1 and A[PARENT(i)] < A[i]
5      tukar A[i] dengan A[PARENT(i)]   // naikkan elemen
6      i = PARENT(i)

MAX-HEAP-INSERT(A, key, n)
1  A.heap-size = A.heap-size + 1
2  A[A.heap-size] = -∞
3  HEAP-INCREASE-KEY(A, A.heap-size, key)
```

Priority queue adalah landasan banyak algoritma graf (Dijkstra, Prim) dan penjadwalan.

### Istilah Kunci

- **Binary heap:** larik yang merepresentasikan pohon biner hampir lengkap.
- **Max-heap / min-heap property:** induk ≥ anak / induk ≤ anak.
- **MAX-HEAPIFY:** memulihkan properti heap di satu simpul, O(lg n).
- **BUILD-MAX-HEAP:** membangun heap dari larik tak terurut, O(n).
- **Heapsort:** pengurutan in place Θ(n lg n) berbasis heap.
- **Priority queue (antrian prioritas):** ADT dengan operasi INSERT/EXTRACT-MAX berbasis kunci prioritas.

### Contoh / Studi Kasus: Trace BUILD-MAX-HEAP

A = ⟨4, 1, 3, 2, 16, 9, 10, 14, 8, 7⟩, n = 10. MAX-HEAPIFY dipanggil dari i = 5 turun ke 1. Hasil akhir adalah max-heap dengan akar 16: ⟨16, 14, 10, 8, 7, 9, 3, 2, 4, 1⟩.

### Rangkuman

Heap adalah struktur larik yang efisien untuk mengakses elemen ekstrem. MAX-HEAPIFY (O(lg n)) memelihara properti; BUILD-MAX-HEAP membangun heap dalam O(n) linear (analisis ketat dengan deret ∑h/2^h). Heapsort mengurutkan in place dalam Θ(n lg n) tetapi tidak stabil. Heap juga mengimplementasikan priority queue dengan operasi O(lg n).

### Latihan & Soal

1. **(Tracing)** Tunjukkan langkah MAX-HEAPIFY(A, 3) pada A = ⟨27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0⟩.
2. **(Pemahaman)** Mengapa daun heap adalah indeks ⌊n/2⌋+1 sampai n?
3. **(Analisis/HOTS)** Buktikan secara rinci bahwa BUILD-MAX-HEAP berjalan dalam O(n).
4. **(Analisis)** Apakah heapsort stabil? Berikan contoh tandingan.
5. **(Implementasi)** Tulis HEAP-DELETE(A, i) yang menghapus elemen indeks i dalam O(lg n).
6. **(HOTS)** Jelaskan kapan heapsort lebih disukai daripada quicksort dan sebaliknya.

---

## Bab 7 — Quicksort

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendeskripsikan** quicksort sebagai algoritma divide-and-conquer berbasis partisi.
2. **Mengimplementasikan** prosedur PARTITION dan menyatakan loop invariant-nya.
3. **Menganalisis** waktu terburuk Θ(n²) dan rata-rata Θ(n lg n).
4. **Menjelaskan** randomized quicksort dan mengapa randomisasi menghindari kasus terburuk deterministik.
5. **Mengevaluasi** keunggulan praktis quicksort dibanding pengurut Θ(n lg n) lainnya.

### Peta Konsep

```
QUICKSORT (divide-and-conquer, in place)
  |
  +-- PARTITION (Θ(n)) : pilih pivot, atur < pivot | > pivot
  +-- rekursi pada dua sisi
  +-- Terburuk Θ(n^2) (partisi tak seimbang)
  +-- Rata-rata Θ(n lg n)
  +-- RANDOMIZED-QUICKSORT: pivot acak -> harapan Θ(n lg n)
```

### Materi Inti

#### 7.1 Deskripsi Quicksort

Quicksort mengurutkan in place dengan pola divide-and-conquer:

- **Divide:** partisi A[p : r] menjadi dua subarray A[p : q−1] dan A[q+1 : r] sehingga setiap elemen di A[p : q−1] ≤ A[q] ≤ setiap elemen di A[q+1 : r]. Indeks q (posisi *pivot*) dihitung saat partisi.
- **Conquer:** urutkan kedua subarray secara rekursif.
- **Combine:** tidak ada pekerjaan — karena partisi in place, larik langsung terurut.

```text
QUICKSORT(A, p, r)
1  if p < r
2      // partisi sekitar pivot, yang berakhir di A[q]
3      q = PARTITION(A, p, r)
4      QUICKSORT(A, p, q - 1)     // urutkan sisi rendah
5      QUICKSORT(A, q + 1, r)     // urutkan sisi tinggi
```

#### Prosedur PARTITION

PARTITION memilih pivot x = A[r] (elemen terakhir), lalu menata ulang sehingga elemen ≤ x berada di kiri dan > x di kanan, mengembalikan indeks akhir pivot.

```text
PARTITION(A, p, r)
1  x = A[r]                 // pivot
2  i = p - 1                // batas akhir sisi rendah
3  for j = p to r - 1       // proses tiap elemen selain pivot
4      if A[j] <= x         // apakah elemen ini milik sisi rendah?
5          i = i + 1        // slot baru di sisi rendah
6          tukar A[i] dengan A[j]
7  tukar A[i + 1] dengan A[r]   // pivot tepat di kanan sisi rendah
8  return i + 1             // indeks baru pivot
```

> **Loop invariant PARTITION:** Pada awal tiap iterasi baris 3–6, untuk indeks k:
> (1) jika p ≤ k ≤ i maka A[k] ≤ x; (2) jika i+1 ≤ k ≤ j−1 maka A[k] > x; (3) jika k = r maka A[k] = x.
> Saat perulangan berakhir, semua elemen terpartisi benar; baris 7 menempatkan pivot ke posisinya.

Waktu PARTITION pada subarray berukuran n adalah **Θ(n)** (sekali pindai).

#### 7.2 Performa Quicksort

Performa bergantung pada keseimbangan partisi:

- **Terburuk:** Partisi selalu maksimal tak seimbang (mis. larik sudah terurut → pivot selalu elemen terbesar/terkecil → satu sisi berukuran n−1, sisi lain 0). Rekurens T(n) = T(n−1) + Θ(n) → **Θ(n²)**.
- **Terbaik:** Partisi seimbang sempurna, T(n) = 2T(n/2) + Θ(n) → **Θ(n lg n)**.
- **Kasus "cukup seimbang":** Bahkan pemisahan 9:1 menghasilkan Θ(n lg n), karena kedalaman pohon rekursi tetap Θ(lg n). Ini menjelaskan ketangguhan quicksort.

#### 7.3 Versi Acak (Randomized Quicksort)

Untuk menghindari skenario terburuk pada masukan tertentu, pilih pivot **secara acak**:

```text
RANDOMIZED-PARTITION(A, p, r)
1  i = RANDOM(p, r)
2  tukar A[r] dengan A[i]      // pivot acak dipindah ke posisi akhir
3  return PARTITION(A, p, r)

RANDOMIZED-QUICKSORT(A, p, r)
1  if p < r
2      q = RANDOMIZED-PARTITION(A, p, r)
3      RANDOMIZED-QUICKSORT(A, p, q - 1)
4      RANDOMIZED-QUICKSORT(A, q + 1, r)
```

Dengan pivot acak, **tidak ada** masukan tetap yang selalu memicu Θ(n²); waktu harapan menjadi **Θ(n lg n)** untuk masukan apa pun.

#### 7.4 Analisis Kasus Rata-rata

Waktu eksekusi didominasi banyaknya perbandingan dalam PARTITION. Misalkan X = jumlah perbandingan. Dengan indicator random variable Xᵢⱼ = I{elemen ke-i dan ke-j terurut dibandingkan}, dua elemen zᵢ dan zⱼ dibandingkan paling banyak sekali, dengan peluang 2/(j−i+1). Maka:

> E[X] = ∑ᵢ ∑_{j>i} 2/(j−i+1) = O(n lg n),

menggunakan bilangan harmonik Hₙ. Jadi **E[waktu RANDOMIZED-QUICKSORT] = Θ(n lg n)**. Kompleksitas ruang adalah Θ(lg n) harapan (kedalaman tumpukan rekursi).

### Istilah Kunci

- **Pivot:** elemen acuan yang membagi larik dalam partisi.
- **PARTITION:** menata ulang larik relatif terhadap pivot dalam Θ(n).
- **Randomized quicksort:** quicksort dengan pivot acak; harapan Θ(n lg n).
- **Balanced partition (partisi seimbang):** kunci performa baik; bahkan 9:1 cukup.
- **Tail recursion:** optimasi untuk membatasi kedalaman tumpukan.

### Contoh / Studi Kasus: Trace PARTITION

A = ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, p=1, r=8, pivot x = 4. Pindai j; i bertambah saat A[j] ≤ 4. Hasil: elemen ≤ 4 (yakni 2,1,3) dipindah ke kiri, lalu pivot 4 ditempatkan → A = ⟨2, 1, 3, 4, 7, 5, 6, 8⟩, q = 4.

| j | A[j] | aksi | larik |
|---|---|---|---|
| 1 | 2 | ≤4, i=1, tukar(1,1) | [2,8,7,1,3,5,6,4] |
| 2 | 8 | >4 | [2,8,7,1,3,5,6,4] |
| 3 | 7 | >4 | [2,8,7,1,3,5,6,4] |
| 4 | 1 | ≤4, i=2, tukar(2,4) | [2,1,7,8,3,5,6,4] |
| 5 | 3 | ≤4, i=3, tukar(3,5) | [2,1,3,8,7,5,6,4] |
| 6 | 5 | >4 | sama |
| 7 | 6 | >4 | sama |
| akhir | — | tukar(4,8) | [2,1,3,4,7,5,6,8], q=4 |

### Rangkuman

Quicksort adalah divide-and-conquer in place yang sangat cepat dalam praktik. PARTITION (Θ(n)) menata larik di sekitar pivot. Kasus terburuk Θ(n²) terjadi pada partisi tak seimbang, tetapi randomisasi pivot menjamin waktu harapan Θ(n lg n) tanpa bergantung pada masukan. Faktor konstan kecil dan lokalitas memori membuat quicksort sering mengungguli merge sort/heapsort dalam praktik.

### Latihan & Soal

1. **(Tracing)** Jalankan PARTITION pada A = ⟨13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11⟩.
2. **(Pemahaman)** Nilai q apa yang dikembalikan PARTITION bila semua elemen sama? Modifikasi agar membelah di tengah.
3. **(Analisis/HOTS)** Turunkan rekurens dan selesaikan waktu terburuk quicksort.
4. **(Analisis)** Tunjukkan partisi terbaik memberi Θ(n lg n) dengan pohon rekursi.
5. **(HOTS)** Jelaskan mengapa randomisasi menghilangkan ketergantungan kasus terburuk pada masukan tertentu.
6. **(Implementasi)** Tambahkan optimasi *tail-recursion* agar kedalaman tumpukan O(lg n) pada kasus terburuk.

---

## Bab 8 — Pengurutan dalam Waktu Linear

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membuktikan** batas bawah Ω(n lg n) untuk comparison sort melalui model **decision tree**.
2. **Mengimplementasikan** counting sort, radix sort, dan bucket sort.
3. **Menganalisis** waktu Θ(n+k), Θ(d(n+k)), dan Θ(n) (rata-rata) masing-masing.
4. **Menjelaskan** asumsi yang memungkinkan pengurutan menembus batas Ω(n lg n).

### Peta Konsep

```
BATAS BAWAH comparison sort: Ω(n lg n) (decision tree, n! daun)
  |
  +-- Counting sort  : kunci di [0..k], Θ(n+k), stabil
  +-- Radix sort     : d digit, panggil counting sort per digit, Θ(d(n+k))
  +-- Bucket sort    : masukan terdistribusi seragam, Θ(n) rata-rata
```

### Materi Inti

#### 8.1 Batas Bawah untuk Pengurutan

**Comparison sort** hanya memperoleh informasi urutan melalui perbandingan antar elemen (≤, <, =, >, ≥). Setiap comparison sort dapat dimodelkan sebagai **decision tree (pohon keputusan)**: pohon biner di mana tiap simpul internal adalah perbandingan dan tiap daun adalah suatu permutasi keluaran. Karena ada **n!** kemungkinan permutasi, pohon harus memiliki ≥ n! daun. Pohon biner berketinggian h memiliki ≤ 2^h daun, sehingga 2^h ≥ n!, yakni h ≥ lg(n!) = Θ(n lg n) (dari Stirling).

> **Teorema (batas bawah).** Setiap comparison sort memerlukan **Ω(n lg n)** perbandingan dalam kasus terburuk.

Konsekuensi: merge sort dan heapsort **optimal secara asimtotik** di antara comparison sort.

#### 8.2 Counting Sort

**Counting sort** mengasumsikan masukan adalah n bilangan bulat dalam rentang 0..k. Ia menghitung, untuk tiap nilai, berapa banyak elemen ≤ nilai itu, lalu menempatkan elemen ke posisi akhirnya. Tidak ada perbandingan antar elemen.

```text
COUNTING-SORT(A, n, k)
 1  misalkan B[1 : n] dan C[0 : k] larik baru
 2  for i = 0 to k
 3      C[i] = 0
 4  for j = 1 to n
 5      C[A[j]] = C[A[j]] + 1        // C[i] = jumlah elemen bernilai i
 6  for i = 1 to k
 7      C[i] = C[i] + C[i - 1]       // C[i] = jumlah elemen <= i
 8  for j = n downto 1               // mundur agar STABIL
 9      B[C[A[j]]] = A[j]
10      C[A[j]] = C[A[j]] - 1
11  return B
```

**Analisis:** baris 2–3 Θ(k); 4–5 Θ(n); 6–7 Θ(k); 8–10 Θ(n). Total **Θ(n + k)**. Bila k = O(n), maka Θ(n). Counting sort **stabil** (penting agar dapat dipakai sebagai subrutin radix sort). Ruang Θ(n + k).

#### 8.3 Radix Sort

**Radix sort** mengurutkan bilangan berdasarkan digit, dari digit **paling tak signifikan (least significant digit)** ke paling signifikan, memakai pengurut stabil (biasanya counting sort) per digit.

```text
RADIX-SORT(A, n, d)
1  for i = 1 to d                    // i = 1 adalah digit paling tak signifikan
2      gunakan pengurutan stabil untuk mengurutkan A berdasarkan digit ke-i
```

**Analisis:** dengan d digit dan tiap digit dalam rentang 0..k−1, tiap lintasan counting sort Θ(n + k); total **Θ(d(n + k))**. Bila d konstan dan k = O(n), radix sort berjalan **Θ(n)**. Kestabilan pengurut per digit adalah syarat mutlak korektness.

#### 8.4 Bucket Sort

**Bucket sort** mengasumsikan masukan diambil dari distribusi **seragam (uniform)** pada [0, 1). Ia membagi [0,1) menjadi n "ember (bucket)" yang sama besar, menyebar elemen ke ember sesuai nilainya, mengurutkan tiap ember (mis. dengan insertion sort), lalu menyambung ember secara berurutan.

```text
BUCKET-SORT(A, n)
1  misalkan B[0 : n-1] larik list (ember) yang awalnya kosong
2  for i = 1 to n
3      sisipkan A[i] ke list B[⌊n · A[i]⌋]
4  for i = 0 to n - 1
5      urutkan list B[i] dengan insertion sort
6  sambung list B[0], B[1], …, B[n-1] secara berurutan
```

**Analisis:** Dengan asumsi seragam, nilai harapan jumlah elemen per ember adalah konstan, sehingga total waktu harapan **Θ(n)**. Kasus terburuk (semua elemen jatuh di satu ember) adalah **Θ(n²)**, tetapi jarang terjadi pada masukan seragam.

### Istilah Kunci

- **Comparison sort:** pengurutan yang hanya membandingkan elemen.
- **Decision tree (pohon keputusan):** model untuk batas bawah perbandingan; ≥ n! daun.
- **Counting sort:** pengurutan bilangan bulat 0..k dalam Θ(n+k), stabil.
- **Radix sort:** pengurutan per digit (LSD ke MSD) memakai pengurut stabil.
- **Bucket sort:** menyebar ke ember; Θ(n) rata-rata untuk masukan seragam.
- **Stable (stabil):** properti pengurut yang dibutuhkan radix sort.

### Contoh / Studi Kasus: Trace Radix Sort

Bilangan tiga digit: 329, 457, 657, 839, 436, 720, 355.

| Awal | Sortir digit-1 (satuan) | digit-2 (puluhan) | digit-3 (ratusan) |
|---|---|---|---|
| 329 | 720 | 720 | 329 |
| 457 | 355 | 329 | 355 |
| 657 | 436 | 436 | 436 |
| 839 | 457 | 839 | 457 |
| 436 | 657 | 355 | 657 |
| 720 | 329 | 457 | 720 |
| 355 | 839 | 657 | 839 |

Hasil akhir terurut: 329, 355, 436, 457, 657, 720, 839.

### Rangkuman

Comparison sort tak bisa lebih cepat dari Ω(n lg n) (terbukti via decision tree). Dengan asumsi tambahan tentang masukan, pengurutan dapat linear: counting sort Θ(n+k) untuk bilangan bulat terbatas (stabil), radix sort Θ(d(n+k)) untuk bilangan ber-d digit, dan bucket sort Θ(n) rata-rata untuk masukan terdistribusi seragam. Kestabilan menjadi syarat penting untuk radix sort.

### Latihan & Soal

1. **(Pemahaman)** Mengapa batas Ω(n lg n) tidak melanggar fakta counting sort berjalan Θ(n+k)?
2. **(Tracing)** Jalankan counting sort pada A = ⟨6,0,2,0,1,3,4,6,1,3,2⟩ dengan k = 6.
3. **(Analisis/HOTS)** Buktikan radix sort benar dengan argumen induksi atas digit dan kestabilan.
4. **(Analisis)** Mengapa counting sort harus stabil agar dapat dipakai radix sort?
5. **(HOTS)** Untuk mengurutkan n bilangan bulat di rentang 0..n³−1, bagaimana memilih basis radix agar Θ(n)? Jelaskan.

---

## Bab 9 — Median dan Statistik Terurut

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** persoalan **selection** (mencari elemen ke-i terkecil) dan median.
2. **Menentukan** minimum/maksimum dengan jumlah perbandingan minimal.
3. **Menganalisis** RANDOMIZED-SELECT dengan waktu harapan Θ(n).
4. **Menjelaskan** algoritma seleksi waktu terburuk linear (median-of-medians).

### Peta Konsep

```
ORDER STATISTICS: elemen ke-i terkecil
  +-- Minimum/Maksimum : n-1 perbandingan; keduanya 3⌊n/2⌋
  +-- RANDOMIZED-SELECT : harapan Θ(n), terburuk Θ(n^2)
  +-- SELECT (median-of-medians) : terburuk Θ(n)
```

### Materi Inti

#### Definisi

**Statistik terurut ke-i (i-th order statistic)** dari himpunan n elemen adalah elemen ke-i terkecil. Minimum = statistik ke-1; maksimum = ke-n. **Median** adalah elemen "tengah": untuk n ganjil pada posisi (n+1)/2; untuk n genap ada median bawah ⌊(n+1)/2⌋ dan median atas ⌈(n+1)/2⌉.

#### 9.1 Minimum dan Maksimum

Mencari minimum saja membutuhkan tepat **n−1** perbandingan (optimal). Mencari minimum **dan** maksimum sekaligus dapat dilakukan dengan **3⌊n/2⌋** perbandingan (bukan 2n−2): proses elemen berpasangan, bandingkan keduanya dulu, lalu yang kecil dengan min dan yang besar dengan max.

#### 9.2 Seleksi Waktu Harapan Linear

RANDOMIZED-SELECT meniru quicksort tetapi hanya berekursi ke **satu** sisi partisi (sisi yang memuat elemen yang dicari):

```text
RANDOMIZED-SELECT(A, p, r, i)     // cari elemen ke-i terkecil di A[p:r]
1  if p == r
2      return A[p]
3  q = RANDOMIZED-PARTITION(A, p, r)
4  k = q - p + 1                  // peringkat pivot dalam A[p:r]
5  if i == k
6      return A[q]                // pivot adalah jawabannya
7  elseif i < k
8      return RANDOMIZED-SELECT(A, p, q - 1, i)
9  else
10     return RANDOMIZED-SELECT(A, q + 1, r, i - k)
```

**Analisis:** Karena hanya satu sisi yang direkursi, rekurens harapan menjadi E[T(n)] ≤ E[T(n/2-ish)] + Θ(n), menghasilkan **waktu harapan Θ(n)**. Kasus terburuk tetap **Θ(n²)** (partisi selalu buruk), tetapi sangat tidak mungkin dengan pivot acak.

#### 9.3 Seleksi Waktu Terburuk Linear: SELECT (Median-of-Medians)

Algoritma SELECT menjamin **Θ(n) terburuk** dengan memilih pivot "baik" secara deterministik:

1. Bagi n elemen menjadi ⌈n/5⌉ kelompok berisi 5 elemen.
2. Cari median tiap kelompok (perbandingan konstan per kelompok).
3. Rekursif cari **median dari ⌈n/5⌉ median** itu → jadikan pivot x.
4. Partisi sekitar x; rekursi ke sisi yang relevan.

Karena pivot median-of-medians menjamin setidaknya ≈ 3n/10 elemen berada di tiap sisi, ukuran subpersoalan rekursif ≤ 7n/10. Rekurensnya:

> T(n) ≤ T(⌈n/5⌉) + T(7n/10 + 6) + Θ(n),

yang dapat dibuktikan (substitusi) menghasilkan **T(n) = Θ(n)**, karena 1/5 + 7/10 = 9/10 < 1. Dalam praktik RANDOMIZED-SELECT lebih cepat karena konstanta lebih kecil; SELECT bernilai teoretis (jaminan terburuk linear).

### Istilah Kunci

- **Order statistic (statistik terurut):** elemen ke-i terkecil.
- **Median:** statistik terurut tengah.
- **Selection problem (persoalan seleksi):** menemukan elemen ke-i.
- **RANDOMIZED-SELECT:** seleksi berbasis partisi acak; harapan Θ(n).
- **Median-of-medians (SELECT):** seleksi deterministik terburuk Θ(n).

### Contoh / Studi Kasus

Cari median (i = 5) dari A = ⟨6, 19, 4, 12, 14, 9, 15, 7, 8⟩ (n = 9). Setelah beberapa partisi acak, RANDOMIZED-SELECT mengembalikan elemen ke-5 terkecil = 9. (Urutan: 4,6,7,8,9,12,14,15,19.)

### Rangkuman

Persoalan seleksi mencari elemen ke-i tanpa mengurutkan seluruh data. Minimum & maksimum dapat ditemukan dalam 3⌊n/2⌋ perbandingan. RANDOMIZED-SELECT memberikan waktu harapan Θ(n) (terburuk Θ(n²)), sementara SELECT median-of-medians menjamin Θ(n) terburuk dengan memilih pivot berkualitas secara deterministik.

### Latihan & Soal

1. **(Pemahaman)** Tunjukkan minimum membutuhkan tepat n−1 perbandingan.
2. **(Analisis)** Jelaskan mengapa min+max dapat dicapai dalam 3⌊n/2⌋ perbandingan.
3. **(HOTS)** Mengapa ukuran kelompok 5 (bukan 3) menjamin SELECT linear? Apa yang terjadi bila kelompok 3?
4. **(Tracing)** Jalankan RANDOMIZED-SELECT untuk mencari elemen ke-3 terkecil pada larik kecil pilihan Anda.
5. **(Analisis/HOTS)** Buktikan rekurens median-of-medians menghasilkan Θ(n).

---

# BAGIAN III — Struktur Data

## Pengantar Bagian III

Struktur data adalah cara mengorganisasi data untuk mendukung operasi tertentu secara efisien. Bagian ini membangun dari yang elementer ke yang canggih: **struktur elementer** (larik, matriks, stack, queue, linked list, pohon berakar) di Bab 10; **tabel hash** untuk pencarian rata-rata O(1) di Bab 11; **pohon pencarian biner (BST)** dengan operasi O(h) di Bab 12; dan **pohon merah-hitam (red-black tree)** yang menjamin tinggi O(lg n) sehingga semua operasi O(lg n) di Bab 13. Sebuah **set dinamis (dynamic set)** mendukung operasi seperti SEARCH, INSERT, DELETE, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR. Pilihan struktur data menentukan kompleksitas operasi-operasi tersebut.

---

## Bab 10 — Struktur Data Elementer

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membedakan** larik, matriks, stack, queue, dan linked list beserta operasinya.
2. **Mengimplementasikan** operasi PUSH/POP (stack) dan ENQUEUE/DEQUEUE (queue) dalam O(1).
3. **Mengimplementasikan** operasi linked list: pencarian, penyisipan, penghapusan.
4. **Menjelaskan** representasi pohon berakar dengan banyak anak.

### Peta Konsep

```
STRUKTUR ELEMENTER
  +-- Array / Matrix : akses indeks O(1)
  +-- Stack (LIFO)   : PUSH, POP -> O(1)
  +-- Queue (FIFO)   : ENQUEUE, DEQUEUE -> O(1)
  +-- Linked list    : SEARCH O(n), INSERT/DELETE O(1) jika simpul diketahui
  +-- Rooted trees   : pointer parent/child / left-child right-sibling
```

### Materi Inti

#### 10.1 Larik, Matriks, Stack, dan Queue

**Larik (array)** menyimpan elemen pada lokasi memori bersebelahan; akses elemen ke-i adalah O(1) berkat alamat = basis + i·ukuran. **Matriks** dapat disimpan *row-major* atau *column-major*.

**Stack (tumpukan)** menerapkan kebijakan **LIFO (Last-In First-Out)**. Operasi PUSH dan POP berjalan O(1), diimplementasikan dengan larik plus atribut `S.top`:

```text
PUSH(S, x)              POP(S)
1 if S.top == S.size    1 if STACK-EMPTY(S)
2   error "overflow"    2   error "underflow"
3 S.top = S.top + 1     3 S.top = S.top - 1
4 S[S.top] = x          4 return S[S.top + 1]
```

**Queue (antrian)** menerapkan **FIFO (First-In First-Out)**. ENQUEUE menambah di ekor, DEQUEUE mengambil dari kepala; keduanya O(1), umumnya dengan larik melingkar (circular array) berisi atribut `head` dan `tail`.

#### 10.2 Linked List

**Linked list (senarai berantai)** menyimpan elemen dalam simpul (node) yang terhubung lewat pointer. Pada **doubly linked list**, tiap simpul `x` punya `x.key`, `x.next`, dan `x.prev`.

```text
LIST-SEARCH(L, k)             LIST-INSERT(L, x)            LIST-DELETE(L, x)
1 x = L.head                  1 x.next = L.head            1 if x.prev != NIL
2 while x != NIL and x.key!=k 2 if L.head != NIL           2   x.prev.next = x.next
3   x = x.next                3   L.head.prev = x          3 else L.head = x.next
4 return x                    4 L.head = x                 4 if x.next != NIL
                              5 x.prev = NIL               5   x.next.prev = x.prev
```

- **LIST-SEARCH:** O(n) terburuk (pencarian linear).
- **LIST-INSERT (di kepala):** O(1).
- **LIST-DELETE (simpul diketahui):** O(1); dengan penggunaan **sentinel** `L.nil`, kode menjadi lebih ringkas (circular doubly linked list dengan sentinel).

#### 10.3 Representasi Pohon Berakar

- **Binary tree:** tiap simpul punya `p` (induk), `left`, `right`.
- **Pohon berderajat tak terbatas:** gunakan representasi **left-child, right-sibling** — tiap simpul punya pointer ke anak pertama (`left-child`) dan saudara berikutnya (`right-sibling`), sehingga memori O(n) tanpa bergantung jumlah anak.

### Istilah Kunci

- **Stack (LIFO):** struktur tumpukan; PUSH/POP O(1).
- **Queue (FIFO):** struktur antrian; ENQUEUE/DEQUEUE O(1).
- **Linked list:** simpul terhubung pointer; sisip/hapus O(1) jika simpul diketahui.
- **Sentinel:** simpul penjaga untuk menyederhanakan kondisi batas.
- **Left-child, right-sibling:** representasi pohon berderajat sembarang dengan ruang O(n).

### Contoh / Studi Kasus

Stack S dengan operasi PUSH(4), PUSH(1), PUSH(3), POP, PUSH(8): isi menjadi [4, 1, 8] dengan top di 8 (POP menghapus 3).

### Rangkuman

Struktur data elementer menyediakan blok bangunan: larik (akses O(1)), stack (LIFO), queue (FIFO), linked list (sisip/hapus O(1)), dan pohon berakar. Pilihan representasi menentukan operasi mana yang efisien. Sentinel menyederhanakan implementasi linked list.

### Latihan & Soal

1. **(Pemahaman)** Bedakan kapan menggunakan stack vs queue dalam algoritma graf.
2. **(Implementasi)** Implementasikan dua stack dalam satu larik agar tidak overflow kecuali kedua stack penuh.
3. **(Analisis/HOTS)** Implementasikan queue menggunakan dua stack; analisis kompleksitas teramortisasi DEQUEUE.
4. **(Implementasi)** Tulis LIST-REVERSE untuk membalik doubly linked list dalam O(n) dan O(1) ruang tambahan.

---

## Bab 11 — Tabel Hash

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** direct-address table dan keterbatasannya.
2. **Mendeskripsikan** tabel hash, fungsi hash, dan faktor muat (load factor) α.
3. **Membandingkan** resolusi tabrakan via **chaining** dan **open addressing**.
4. **Menganalisis** waktu pencarian rata-rata O(1 + α) di bawah asumsi *simple uniform hashing*.
5. **Menjelaskan** universal hashing dan motivasinya.

### Peta Konsep

```
TABEL HASH: pemetaan kunci -> slot via h(k)
  +-- Direct-address table : ruang O(|U|), tak praktis
  +-- Hashing: h: U -> {0..m-1}, load factor α = n/m
  +-- Tabrakan (collision):
        +-- Chaining (linked list per slot) : SEARCH O(1+α) rata-rata
        +-- Open addressing (probing)       : tanpa list, butuh α<1
  +-- Universal hashing : pilih h acak -> jaminan probabilistik
```

### Materi Inti

#### 11.1 Direct-Address Table

Bila kunci berasal dari semesta kecil U = {0, 1, …, m−1}, kita pakai larik T[0 : m−1] dengan T[k] menyimpan elemen berkunci k. Operasi SEARCH/INSERT/DELETE semua **O(1)**. Kelemahan: ruang **O(|U|)** — boros bila |U| jauh lebih besar daripada jumlah kunci aktual.

#### 11.2 Tabel Hash

**Tabel hash (hash table)** memetakan kunci k ke slot **h(k)** dalam rentang {0, …, m−1} via **fungsi hash (hash function)** h, dengan m biasanya jauh lebih kecil daripada |U|. Ruang menjadi O(m). **Faktor muat (load factor)** α = n/m, dengan n jumlah elemen.

**Tabrakan (collision):** dua kunci berbeda dapat dipetakan ke slot sama. Dua strategi resolusi:

**Chaining (perantaian):** Tiap slot menyimpan linked list elemen yang ber-hash ke situ.

```text
CHAINED-HASH-INSERT(T, x): sisipkan x di kepala list T[h(x.key)]
CHAINED-HASH-SEARCH(T, k): cari k dalam list T[h(k)]
CHAINED-HASH-DELETE(T, x): hapus x dari list T[h(x.key)]
```

> **Teorema (chaining).** Di bawah asumsi **simple uniform hashing** (tiap kunci sama mungkin ber-hash ke slot mana pun, independen), pencarian rata-rata (berhasil maupun gagal) memakan waktu **Θ(1 + α)**. Bila n = O(m), maka α = O(1) dan semua operasi rata-rata **O(1)**.

#### 11.3 Fungsi Hash

Fungsi hash yang baik mendekati asumsi simple uniform hashing. Metode umum:

- **Metode pembagian (division method):** h(k) = k mod m. Pilih m bilangan prima yang tidak dekat pangkat 2.
- **Metode perkalian (multiplication method):** h(k) = ⌊m·(k·A mod 1)⌋ untuk konstanta 0 < A < 1.

#### 11.4 Open Addressing

Pada **open addressing**, semua elemen disimpan **dalam tabel itu sendiri** (tanpa list). Saat tabrakan, kita **probe (selidiki)** urutan slot sampai menemukan slot kosong (penyisipan) atau kunci (pencarian). Diperlukan **α < 1**. Skema probing:

- **Linear probing:** h(k, i) = (h′(k) + i) mod m — sederhana, rentan *primary clustering*.
- **Quadratic probing:** h(k, i) = (h′(k) + c₁i + c₂i²) mod m.
- **Double hashing:** h(k, i) = (h₁(k) + i·h₂(k)) mod m — kualitas terbaik.

Di bawah asumsi **uniform hashing**, jumlah probe harapan pada pencarian gagal adalah ≤ 1/(1−α), dan pencarian berhasil ≤ (1/α)·ln(1/(1−α)). Misal α = 0,5 → ≤ 2 probe; α = 0,9 → ≤ 10 probe.

#### 11.5 Universal Hashing

Jika fungsi hash tetap, seorang "musuh" dapat memilih n kunci yang semuanya ber-hash ke slot sama (kinerja Θ(n)). **Universal hashing** mengatasi ini dengan memilih fungsi hash **secara acak** dari sebuah keluarga ℋ saat program berjalan, sehingga tidak ada masukan tetap yang selalu buruk. Keluarga ℋ disebut **universal** bila untuk sembarang dua kunci berbeda, peluang tabrakan ≤ 1/m. Ini memberi jaminan kinerja harapan yang baik terlepas dari distribusi kunci.

### Istilah Kunci

- **Hash table / hash function:** tabel pemetaan kunci→slot; fungsi h.
- **Load factor (faktor muat) α = n/m.**
- **Collision (tabrakan):** dua kunci ke slot sama.
- **Chaining:** resolusi tabrakan dengan linked list per slot.
- **Open addressing / probing:** menyimpan semua elemen dalam tabel; menyelidiki slot.
- **Simple uniform hashing:** asumsi distribusi seragam kunci ke slot.
- **Universal hashing:** memilih h acak dari keluarga universal untuk jaminan probabilistik.

### Contoh / Studi Kasus

m = 9, h(k) = k mod 9. Sisipkan 5, 28, 19, 15, 20, 33, 12, 17, 10. Slot: 5→5, 28→1, 19→1 (tabrak, chaining), 15→6, 20→2, 33→6 (tabrak), 12→3, 17→8, 10→1 (tabrak). Slot 1 berisi list {28, 19, 10}.

### Rangkuman

Tabel hash menyediakan pencarian/penyisipan/penghapusan rata-rata O(1) dengan ruang O(m). Tabrakan ditangani via chaining (list per slot, O(1+α)) atau open addressing (probing, butuh α<1). Fungsi hash yang baik mendekati simple uniform hashing; universal hashing memilih fungsi acak untuk menggagalkan masukan adversarial. Kinerja terburuk Θ(n) tetap mungkin bila banyak tabrakan.

### Latihan & Soal

1. **(Pemahaman)** Apa kelemahan utama direct-address table dan bagaimana hashing mengatasinya?
2. **(Tracing)** Sisipkan kunci 10, 22, 31, 4, 15, 28, 17, 88, 59 ke tabel m=11 dengan linear probing, h(k)=k mod 11.
3. **(Analisis/HOTS)** Turunkan jumlah probe harapan pencarian gagal pada open addressing = 1/(1−α).
4. **(Analisis)** Mengapa double hashing mengurangi clustering dibanding linear probing?
5. **(HOTS)** Jelaskan bagaimana universal hashing memberi jaminan terhadap masukan adversarial.

---

## Bab 12 — Pohon Pencarian Biner (BST)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menyatakan** properti pohon pencarian biner (binary-search-tree property).
2. **Mengimplementasikan** SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, INSERT, DELETE.
3. **Menganalisis** kompleksitas operasi sebagai O(h), dengan h tinggi pohon.
4. **Menjelaskan** mengapa tinggi pohon acak adalah O(lg n) harapan, dan terburuk Θ(n).

### Peta Konsep

```
BINARY SEARCH TREE (BST)
  Properti: kiri <= x.key <= kanan
  +-- INORDER-WALK -> keluaran terurut (Θ(n))
  +-- SEARCH/MIN/MAX/SUCCESSOR/INSERT/DELETE -> O(h)
  +-- h = O(lg n) (seimbang) ... Θ(n) (terburuk, rantai)
```

### Materi Inti

#### 12.1 Apa itu BST?

**Binary search tree (BST)** adalah pohon biner yang tiap simpulnya `x` memiliki `x.key`, `x.left`, `x.right`, `x.p` dan memenuhi:

> **Properti BST:** Untuk simpul x, jika y berada di subpohon **kiri** x maka y.key ≤ x.key; jika y di subpohon **kanan** maka y.key ≥ x.key.

Akibat properti ini, **inorder tree walk** menghasilkan kunci dalam urutan menaik dalam **Θ(n)**:

```text
INORDER-TREE-WALK(x)
1 if x != NIL
2     INORDER-TREE-WALK(x.left)
3     cetak x.key
4     INORDER-TREE-WALK(x.right)
```

#### 12.2 Operasi Query

```text
TREE-SEARCH(x, k)               TREE-MINIMUM(x)
1 if x==NIL or k==x.key         1 while x.left != NIL
2     return x                  2     x = x.left
3 if k < x.key                  3 return x
4     return TREE-SEARCH(x.left, k)
5 else return TREE-SEARCH(x.right, k)
```

- **TREE-SEARCH:** menelusuri satu lintasan dari akar; O(h).
- **TREE-MINIMUM/MAXIMUM:** ikuti pointer kiri/kanan terus; O(h).
- **TREE-SUCCESSOR(x):** jika subpohon kanan ada → minimum subpohon kanan; jika tidak → naik sampai bergerak dari anak kiri. O(h).

#### 12.3 Penyisipan dan Penghapusan

```text
TREE-INSERT(T, z)
 1  y = NIL ; x = T.root
 2  while x != NIL              // turun mencari posisi daun
 3      y = x
 4      if z.key < x.key
 5          x = x.left
 6      else x = x.right
 7  z.p = y
 8  if y == NIL
 9      T.root = z              // pohon semula kosong
10  elseif z.key < y.key
11      y.left = z
12  else y.right = z
```

**TREE-DELETE** menangani tiga kasus untuk simpul z: (1) tanpa anak — cukup hapus; (2) satu anak — angkat anak menggantikan z; (3) dua anak — ganti z dengan **suksesornya** (minimum subpohon kanan), yang pasti tak punya anak kiri. CLRS menggunakan subrutin TRANSPLANT untuk mengganti subpohon. Semua O(h).

#### Analisis Tinggi

Semua operasi dinamis berjalan **O(h)** dengan h tinggi pohon. Bila BST dibangun dari penyisipan acak n kunci, tinggi harapannya **O(lg n)**, sehingga operasi rata-rata O(lg n). Namun dalam kasus terburuk (mis. penyisipan terurut menaik), pohon merosot menjadi **rantai** dengan h = n−1 → operasi Θ(n). Inilah motivasi pohon seimbang (Bab 13).

### Istilah Kunci

- **Binary search tree (BST):** pohon biner dengan properti urutan kiri ≤ x ≤ kanan.
- **Inorder tree walk:** penelusuran yang menghasilkan urutan menaik, Θ(n).
- **Successor / predecessor:** elemen terkecil yang lebih besar / terbesar yang lebih kecil.
- **TRANSPLANT:** subrutin mengganti satu subpohon dengan subpohon lain.
- **Height (tinggi) h:** menentukan kompleksitas operasi O(h).

### Contoh / Studi Kasus

Sisipkan 15, 6, 18, 3, 7, 17, 20, 13, 9 ke BST kosong. Akar 15; subpohon kiri {6,3,7,13,9}, kanan {18,17,20}. Inorder walk: 3,6,7,9,13,15,17,18,20.

### Rangkuman

BST menyimpan kunci dengan properti urutan yang memungkinkan inorder walk menghasilkan data terurut (Θ(n)) dan operasi dinamis O(h). Tinggi h menentukan segalanya: O(lg n) untuk pohon seimbang/acak, Θ(n) untuk pohon merosot. Untuk menjamin O(lg n) di kasus terburuk, diperlukan pohon seimbang seperti red-black tree.

### Latihan & Soal

1. **(Tracing)** Bangun BST dari 50, 30, 70, 20, 40, 60, 80 dan tuliskan inorder, preorder, postorder.
2. **(Pemahaman)** Tunjukkan inorder walk menghasilkan urutan menaik (argumen induksi).
3. **(Implementasi)** Tulis TREE-SUCCESSOR dan jelaskan kedua kasusnya.
4. **(Analisis/HOTS)** Mengapa penyisipan kunci terurut membuat BST merosot? Apa dampaknya pada kompleksitas?
5. **(HOTS)** Buktikan TREE-DELETE menjaga properti BST untuk ketiga kasus.

---

## Bab 13 — Pohon Merah-Hitam (Red-Black Trees)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menyatakan** kelima properti red-black tree.
2. **Membuktikan** bahwa red-black tree berisi n simpul internal memiliki tinggi ≤ 2 lg(n+1).
3. **Menjelaskan** operasi **rotasi (rotation)** kiri dan kanan.
4. **Menggambarkan** prinsip pemulihan properti pada INSERT dan DELETE dalam O(lg n).

### Peta Konsep

```
RED-BLACK TREE = BST + pewarnaan simpul (merah/hitam)
  5 properti -> tinggi <= 2 lg(n+1) -> operasi O(lg n)
  +-- ROTATE (kiri/kanan) O(1) : restrukturisasi lokal
  +-- RB-INSERT + RB-INSERT-FIXUP (rotasi + recolor)
  +-- RB-DELETE + RB-DELETE-FIXUP
```

### Materi Inti

#### 13.1 Properti Red-Black Tree

**Red-black tree** adalah BST dengan satu bit warna ekstra per simpul (MERAH atau HITAM) dan menggunakan **sentinel** `T.nil` (hitam) untuk daun/induk akar. Kelima properti:

> 1. Setiap simpul berwarna **merah** atau **hitam**.
> 2. **Akar** berwarna **hitam**.
> 3. Setiap **daun** (T.nil) berwarna **hitam**.
> 4. Jika sebuah simpul **merah**, maka **kedua anaknya hitam** (tidak ada dua merah berurutan).
> 5. Untuk setiap simpul, semua lintasan dari simpul itu ke daun keturunannya memuat **jumlah simpul hitam yang sama** (disebut **black-height**, bh).

Properti-properti ini menjamin pohon **kira-kira seimbang**.

> **Lema (tinggi).** Red-black tree dengan n simpul internal memiliki tinggi paling banyak **2 lg(n + 1)**.

*Ide bukti:* black-height akar ≥ h/2 (karena properti 4 mencegah dua merah beruntun, separuh simpul pada lintasan minimal hitam), dan subpohon berakar di simpul x memuat ≥ 2^(bh(x)) − 1 simpul internal. Gabungan keduanya menghasilkan h ≤ 2 lg(n+1). ∎

Akibatnya, SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR (operasi BST yang tak mengubah struktur) berjalan **O(lg n)** karena O(h) = O(lg n).

#### 13.2 Rotasi

**Rotasi** adalah operasi lokal O(1) yang mempertahankan properti BST sambil mengubah struktur untuk menyeimbangkan pohon.

```text
LEFT-ROTATE(T, x)
 1  y = x.right                 // y menjadi akar baru subpohon
 2  x.right = y.left            // subpohon kiri y menjadi kanan x
 3  if y.left != T.nil
 4      y.left.p = x
 5  y.p = x.p                   // sambungkan induk x ke y
 6  if x.p == T.nil
 7      T.root = y
 8  elseif x == x.p.left
 9      x.p.left = y
10  else x.p.right = y
11  y.left = x                  // x menjadi anak kiri y
12  x.p = y
```

RIGHT-ROTATE simetris. Rotasi mengubah hubungan pointer dalam O(1) tanpa melanggar urutan kunci.

#### 13.3–13.4 Penyisipan dan Penghapusan

**RB-INSERT** menyisipkan simpul baru (diberi warna **merah**) seperti TREE-INSERT, lalu memanggil **RB-INSERT-FIXUP** untuk memulihkan properti yang mungkin dilanggar (terutama properti 4: dua merah berurutan). FIXUP menggunakan kombinasi **pewarnaan ulang (recoloring)** dan **rotasi**, menangani tiga kasus tergantung warna "paman (uncle)" simpul. Karena tiap iterasi naik dua level pohon dan tinggi O(lg n), **RB-INSERT = O(lg n)** dengan jumlah rotasi **konstan** (≤ 2).

**RB-DELETE** menghapus simpul seperti TREE-DELETE, lalu **RB-DELETE-FIXUP** memulihkan properti (terutama jika simpul yang dihapus/dipindah berwarna hitam, melanggar properti 5). FIXUP menangani empat kasus dengan rotasi dan pewarnaan; **RB-DELETE = O(lg n)** dengan jumlah rotasi ≤ 3.

| Operasi | Red-Black Tree | BST tak seimbang |
|---|---|---|
| SEARCH | O(lg n) | O(h) = Θ(n) terburuk |
| INSERT | O(lg n) | O(h) |
| DELETE | O(lg n) | O(h) |
| MIN/MAX/SUCCESSOR | O(lg n) | O(h) |

### Istilah Kunci

- **Red-black tree:** BST berwarna dengan 5 properti penyeimbang.
- **Black-height (bh):** jumlah simpul hitam pada lintasan ke daun.
- **Rotation (rotasi):** restrukturisasi lokal O(1) yang menjaga properti BST.
- **Recoloring (pewarnaan ulang):** mengubah warna simpul saat FIXUP.
- **Sentinel T.nil:** simpul penjaga hitam untuk semua daun.

### Contoh / Studi Kasus

Menyisipkan 41, 38, 31, 12, 19, 8 secara berurutan ke red-black tree memicu serangkaian recoloring dan rotasi untuk menjaga tinggi tetap O(lg n). Misal saat menyisipkan menghasilkan dua simpul merah berurutan, RB-INSERT-FIXUP melakukan rotasi yang menyeimbangkan kembali subpohon.

### Rangkuman

Red-black tree adalah BST yang menjaga keseimbangan melalui pewarnaan dan lima properti, menjamin tinggi ≤ 2 lg(n+1) sehingga **semua** operatif set dinamis berjalan O(lg n) bahkan dalam kasus terburuk. Rotasi (O(1)) adalah primitif restrukturisasi; INSERT dan DELETE memulihkan properti dengan rotasi (jumlah konstan) dan pewarnaan ulang. RB-tree menjadi fondasi banyak struktur lanjutan (mis. augmentasi di Bab 17).

### Latihan & Soal

1. **(Pemahaman)** Sebutkan kelima properti red-black tree.
2. **(Analisis/HOTS)** Buktikan tinggi red-black tree dengan n simpul internal ≤ 2 lg(n+1).
3. **(Tracing)** Tunjukkan efek LEFT-ROTATE pada sebuah subpohon contoh.
4. **(HOTS)** Mengapa simpul baru pada RB-INSERT diwarnai merah, bukan hitam?
5. **(Analisis)** Jelaskan mengapa RB-INSERT-FIXUP melakukan paling banyak 2 rotasi sedangkan RB-DELETE-FIXUP paling banyak 3.

---

# BAGIAN IV — Teknik Desain dan Analisis Lanjutan

## Pengantar Bagian IV

Bagian ini memperkenalkan tiga teknik desain dan analisis yang ampuh. **Pemrograman dinamis (dynamic programming, DP)** di Bab 14 menyelesaikan persoalan optimasi dengan menggabungkan solusi subpersoalan yang **tumpang tindih (overlapping)**, menyimpan hasilnya agar tidak dihitung ulang. **Algoritma serakah (greedy)** di Bab 15 membuat pilihan lokal optimal pada tiap langkah, dan untuk kelas persoalan tertentu pilihan ini menghasilkan optimum global. **Analisis teramortisasi (amortized analysis)** di Bab 16 menganalisis biaya rata-rata per operasi sepanjang barisan operasi, bukan biaya terburuk per operasi tunggal.

Dua sifat kunci membedakan DP dari greedy: DP memerlukan **substruktur optimal** dan **subpersoalan tumpang tindih**; greedy memerlukan **substruktur optimal** dan **properti pilihan serakah (greedy-choice property)**.

---

## Bab 14 — Pemrograman Dinamis (Dynamic Programming)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mengidentifikasi** dua ciri DP: **optimal substructure** dan **overlapping subproblems**.
2. **Merumuskan** rekurens DP untuk rod cutting, matrix-chain multiplication, dan LCS.
3. **Mengimplementasikan** pendekatan **top-down memoization** dan **bottom-up**.
4. **Menganalisis** kompleksitas waktu/ruang algoritma DP dan **merekonstruksi** solusi optimal.

### Peta Konsep

```
DYNAMIC PROGRAMMING (untuk masalah OPTIMASI)
  Syarat: 1) optimal substructure  2) overlapping subproblems
  +-- Top-down + memoization (tabel hasil)
  +-- Bottom-up (isi tabel dari subproblem kecil)
  +-- Contoh: Rod cutting Θ(n^2), Matrix-chain Θ(n^3), LCS Θ(mn)
  +-- Rekonstruksi solusi via tabel pilihan
```

### Materi Inti

#### Dua Ciri Persoalan DP

> **Optimal substructure (substruktur optimal):** solusi optimal persoalan memuat solusi optimal subpersoalan.
> **Overlapping subproblems (subpersoalan tumpang tindih):** ruang subpersoalan "kecil", sehingga algoritma rekursif menyelesaikan subpersoalan yang sama berulang kali. DP menyimpan (memoize) hasil agar tiap subpersoalan dihitung sekali.

#### 14.1 Rod Cutting (Pemotongan Batang)

**Persoalan:** Diberikan batang sepanjang n inci dan tabel harga pᵢ untuk potongan sepanjang i, tentukan pemotongan yang memaksimalkan total pendapatan rₙ.

Rekurens substruktur optimal:

> rₙ = max₁≤ᵢ≤ₙ (pᵢ + rₙ₋ᵢ),   dengan r₀ = 0.

Rekursi naif berjalan **Θ(2ⁿ)** (eksponensial) karena subpersoalan dihitung berulang. DP menurunkannya menjadi **Θ(n²)**:

```text
BOTTOM-UP-CUT-ROD(p, n)
1  misalkan r[0 : n] larik baru
2  r[0] = 0
3  for j = 1 to n              // selesaikan subproblem ukuran j
4      q = -∞
5      for i = 1 to j
6          q = max(q, p[i] + r[j - i])
7      r[j] = q
8  return r[n]
```

Dua perulangan bersarang → **Θ(n²)** waktu, **Θ(n)** ruang. Untuk merekonstruksi potongan, simpan larik pilihan `s[j]` (ukuran potongan pertama optimal).

#### 14.2 Matrix-Chain Multiplication

**Persoalan:** Diberikan rantai matriks A₁A₂…Aₙ dengan dimensi p₀×p₁, p₁×p₂, …, tentukan **pemberian tanda kurung (parenthesization)** yang meminimalkan jumlah perkalian skalar. Perkalian matriks bersifat asosiatif, tetapi urutan pengelompokan sangat memengaruhi biaya.

Misalkan m[i, j] = biaya minimum mengalikan AᵢAᵢ₊₁…Aⱼ:

> m[i, i] = 0;
> m[i, j] = min_{i≤k<j} ( m[i, k] + m[k+1, j] + p_{i−1}·p_k·p_j ),  untuk i < j.

```text
MATRIX-CHAIN-ORDER(p, n)
 1  misalkan m[1:n, 1:n] dan s[1:n-1, 2:n] larik baru
 2  for i = 1 to n
 3      m[i, i] = 0
 4  for l = 2 to n                          // l = panjang rantai
 5      for i = 1 to n - l + 1
 6          j = i + l - 1
 7          m[i, j] = ∞
 8          for k = i to j - 1
 9              q = m[i, k] + m[k+1, j] + p[i-1]·p[k]·p[j]
10              if q < m[i, j]
11                  m[i, j] = q
12                  s[i, j] = k             // titik belah optimal
13  return m dan s
```

**Analisis:** tiga perulangan bersarang → **Θ(n³)** waktu, **Θ(n²)** ruang. Tabel `s` dipakai oleh PRINT-OPTIMAL-PARENS untuk merekonstruksi pengelompokan.

#### 14.3 Elemen Pemrograman Dinamis

- **Memoization (top-down):** tulis algoritma rekursif alami, tetapi simpan hasil tiap subpersoalan dalam tabel; cek tabel sebelum menghitung. Cocok bila tidak semua subpersoalan perlu dihitung.
- **Bottom-up:** isi tabel dari subpersoalan terkecil ke terbesar. Biasanya lebih efisien konstantanya.
- Keduanya menghasilkan kompleksitas asimtotik sama bila semua subpersoalan dikunjungi.

#### 14.4 Longest Common Subsequence (LCS)

**Persoalan:** Diberikan dua barisan X = ⟨x₁,…,xₘ⟩ dan Y = ⟨y₁,…,yₙ⟩, cari **subbarisan bersama terpanjang (LCS)**. Subbarisan tidak harus kontigu.

Misalkan c[i, j] = panjang LCS dari prefiks Xᵢ dan Yⱼ:

> c[i, j] = 0,                          jika i = 0 atau j = 0;
> c[i, j] = c[i−1, j−1] + 1,             jika xᵢ = yⱼ;
> c[i, j] = max(c[i−1, j], c[i, j−1]),   jika xᵢ ≠ yⱼ.

```text
LCS-LENGTH(X, Y, m, n)
 1  misalkan b[1:m, 1:n] dan c[0:m, 0:n] larik baru
 2  inisialisasi c[i,0]=0 dan c[0,j]=0
 3  for i = 1 to m
 4      for j = 1 to n
 5          if X[i] == Y[j]
 6              c[i,j] = c[i-1,j-1] + 1 ; b[i,j] = "↖"
 7          elseif c[i-1,j] >= c[i,j-1]
 8              c[i,j] = c[i-1,j] ; b[i,j] = "↑"
 9          else c[i,j] = c[i,j-1] ; b[i,j] = "←"
10  return c dan b
```

**Analisis:** **Θ(mn)** waktu dan ruang. Tabel arah `b` digunakan untuk merekonstruksi LCS dengan menelusur balik dari c[m, n].

#### 14.5 Optimal Binary Search Trees

DP juga menyelesaikan **pohon pencarian biner optimal**: diberikan kunci dengan probabilitas akses, bangun BST yang meminimalkan biaya pencarian harapan, dalam **Θ(n³)** (atau Θ(n²) dengan optimasi Knuth).

### Istilah Kunci

- **Dynamic programming (DP):** teknik optimasi dengan subpersoalan tumpang tindih + substruktur optimal.
- **Optimal substructure:** solusi optimal memuat solusi optimal subpersoalan.
- **Overlapping subproblems:** subpersoalan berulang dalam ruang kecil.
- **Memoization:** menyimpan hasil rekursif (top-down).
- **Bottom-up:** mengisi tabel dari kecil ke besar.
- **LCS:** subbarisan bersama terpanjang.
- **Parenthesization:** pengelompokan kurung pada rantai matriks.

### Contoh / Studi Kasus: LCS

X = "ABCBDAB", Y = "BDCABA". LCS panjang 4, mis. "BCBA" atau "BDAB". Tabel c diisi Θ(mn); penelusuran balik dari c[7,6] memberi salah satu LCS.

### Rangkuman

DP menyelesaikan persoalan optimasi yang memiliki substruktur optimal dan subpersoalan tumpang tindih, dengan menyimpan hasil subpersoalan (memoization top-down atau pengisian tabel bottom-up). Contoh kanonik: rod cutting (Θ(n²)), matrix-chain (Θ(n³)), LCS (Θ(mn)). Tabel pilihan memungkinkan rekonstruksi solusi optimal, bukan sekadar nilainya.

### Latihan & Soal

1. **(Pemahaman)** Jelaskan perbedaan memoization dan bottom-up; kapan masing-masing lebih disukai?
2. **(Tracing)** Hitung tabel m untuk rantai dengan dimensi p = ⟨5, 10, 3, 12, 5⟩.
3. **(Analisis/HOTS)** Buktikan optimal substructure untuk rod cutting.
4. **(Implementasi)** Tulis prosedur rekonstruksi LCS dari tabel b.
5. **(HOTS)** Ubah LCS-LENGTH agar memakai ruang Θ(min(m,n)) jika hanya panjang LCS yang dibutuhkan.

---

## Bab 15 — Algoritma Serakah (Greedy)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** strategi greedy dan dua sifat pendukungnya: **greedy-choice property** dan **optimal substructure**.
2. **Merancang** algoritma greedy untuk activity selection.
3. **Membangun** kode Huffman dan membuktikan keoptimalannya.
4. **Membedakan** kapan greedy berhasil dan kapan DP diperlukan.

### Peta Konsep

```
GREEDY: pilih optimum LOKAL tiap langkah
  Syarat: 1) greedy-choice property  2) optimal substructure
  +-- Activity selection : Θ(n) setelah terurut
  +-- Huffman codes      : O(n lg n), kode prefiks optimal
  +-- vs DP: greedy tak meninjau ulang pilihan
```

### Materi Inti

#### 15.1 Activity Selection

**Persoalan:** Diberikan n aktivitas dengan waktu mulai sᵢ dan selesai fᵢ, pilih himpunan **aktivitas saling kompatibel (tak tumpang tindih)** terbesar yang dapat dijadwalkan pada satu sumber daya.

**Strategi greedy:** Urutkan aktivitas menurut **waktu selesai menaik**, lalu pilih aktivitas pertama yang selesai paling awal, kemudian berulang pilih aktivitas berikutnya yang mulai setelah aktivitas terakhir terpilih selesai.

```text
GREEDY-ACTIVITY-SELECTOR(s, f, n)   // diasumsikan f sudah terurut menaik
1  A = {a₁}
2  k = 1
3  for m = 2 to n
4      if s[m] >= f[k]          // aktivitas m kompatibel dengan terakhir terpilih
5          A = A ∪ {aₘ}
6          k = m
7  return A
```

**Analisis:** **Θ(n)** setelah pengurutan (yang Θ(n lg n)). Total **Θ(n lg n)**, atau Θ(n) bila sudah terurut. Bukti keoptimalan menggunakan argumen *exchange*: pilihan greedy (aktivitas selesai terawal) selalu termuat dalam suatu solusi optimal.

#### 15.2 Elemen Strategi Greedy

> **Greedy-choice property:** solusi optimal global dapat dicapai dengan membuat pilihan lokal optimal pada tiap langkah (tanpa meninjau ulang).
> **Optimal substructure:** setelah membuat pilihan greedy, subpersoalan sisa juga diselesaikan optimal.

Perbedaan dengan DP: greedy membuat pilihan **sebelum** menyelesaikan subpersoalan dan **tidak pernah meninjau ulang**, sementara DP mempertimbangkan semua pilihan. Tidak semua persoalan menerima greedy (mis. **0-1 knapsack** memerlukan DP, sedangkan **fractional knapsack** dapat greedy).

#### 15.3 Kode Huffman

**Persoalan:** Diberikan himpunan karakter dengan frekuensi, bangun **kode prefiks (prefix code)** biner yang meminimalkan panjang total pengkodean (kompresi). Kode prefiks: tidak ada codeword yang menjadi awalan codeword lain, sehingga dekode tak ambigu.

**Algoritma Huffman (greedy):** Berulang gabungkan dua simpul berfrekuensi terkecil menjadi satu simpul induk (frekuensi = jumlah keduanya), menggunakan **min-priority queue**.

```text
HUFFMAN(C)
1  n = |C|
2  Q = C                                  // min-priority queue berdasarkan frekuensi
3  for i = 1 to n - 1
4      alokasikan simpul baru z
5      z.left  = x = EXTRACT-MIN(Q)
6      z.right = y = EXTRACT-MIN(Q)
7      z.freq = x.freq + y.freq
8      INSERT(Q, z)
9  return EXTRACT-MIN(Q)                   // akar pohon Huffman
```

**Analisis:** n−1 iterasi, masing-masing dua EXTRACT-MIN dan satu INSERT pada heap → **O(n lg n)**. Keoptimalan dibuktikan dengan greedy-choice (dua karakter paling jarang dapat ditempatkan sebagai daun terdalam bersaudara) dan optimal substructure.

#### 15.4 Offline Caching

CLRS juga membahas **offline caching**, di mana strategi greedy **furthest-in-future** (mengeluarkan blok yang paling jauh dipakai lagi) optimal jika seluruh barisan akses diketahui di muka.

### Istilah Kunci

- **Greedy algorithm:** memilih optimum lokal tiap langkah.
- **Greedy-choice property:** pilihan lokal optimal mengarah ke optimum global.
- **Optimal substructure:** subpersoalan sisa juga optimal.
- **Activity selection:** memilih himpunan aktivitas kompatibel terbanyak.
- **Prefix code (kode prefiks):** kode tanpa codeword yang menjadi awalan codeword lain.
- **Huffman code:** kode prefiks optimal dibangun greedy.
- **Exchange argument:** teknik bukti keoptimalan greedy.

### Contoh / Studi Kasus: Huffman

Karakter dengan frekuensi a:45, b:13, c:12, d:16, e:9, f:5 (dalam ribuan). Huffman menghasilkan kode prefiks variabel-panjang; karakter sering (a) memperoleh codeword pendek, karakter jarang (f) codeword panjang, meminimalkan total bit.

### Rangkuman

Algoritma greedy membuat pilihan lokal optimal yang, untuk kelas persoalan dengan greedy-choice property dan optimal substructure, menghasilkan solusi global optimal. Activity selection (Θ(n lg n)) dan kode Huffman (O(n lg n)) adalah contoh kanonik. Greedy lebih sederhana dan cepat daripada DP, tetapi tidak selalu benar—diperlukan bukti (sering via exchange argument).

### Latihan & Soal

1. **(Pemahaman)** Apa dua sifat yang harus dipenuhi agar greedy benar?
2. **(Tracing)** Jalankan GREEDY-ACTIVITY-SELECTOR pada aktivitas dengan (s,f) tertentu.
3. **(Analisis/HOTS)** Buktikan greedy-choice property untuk activity selection (exchange argument).
4. **(HOTS)** Tunjukkan dengan contoh bahwa greedy gagal untuk 0-1 knapsack tetapi berhasil untuk fractional knapsack.
5. **(Analisis)** Buktikan kode Huffman menghasilkan kode prefiks dengan panjang harapan minimum.

---

## Bab 16 — Analisis Teramortisasi (Amortized Analysis)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** konsep biaya teramortisasi sepanjang barisan operasi.
2. **Menerapkan** metode **agregat (aggregate)**, **akunting (accounting)**, dan **potensial (potential)**.
3. **Menganalisis** tabel dinamis (dynamic table) dengan penggandaan.
4. **Membedakan** biaya teramortisasi dari biaya kasus terburuk dan rata-rata probabilistik.

### Peta Konsep

```
AMORTIZED ANALYSIS: biaya rata-rata per operasi atas BARISAN operasi
  +-- Metode agregat : total biaya / n
  +-- Metode akunting : "biaya muka" + simpanan kredit
  +-- Metode potensial : fungsi potensial Φ; ĉ = c + ΔΦ
  Aplikasi: stack multipop, biner counter, dynamic table
```

### Materi Inti

#### Gagasan Dasar

**Analisis teramortisasi** menghitung biaya **rata-rata per operasi** dalam suatu **barisan operasi** kasus terburuk, **tanpa** melibatkan probabilitas. Tujuannya: menunjukkan bahwa walaupun satu operasi mungkin mahal, rata-rata sepanjang barisan tetap kecil. Ini berbeda dari kasus rata-rata yang mengandalkan distribusi masukan.

#### 16.1 Metode Agregat

Hitung batas atas T(n) untuk **total** biaya n operasi, lalu biaya teramortisasi per operasi = T(n)/n.

**Contoh — stack dengan MULTIPOP:** Operasi PUSH, POP (O(1)) dan MULTIPOP(S, k) yang mem-pop hingga k elemen. Walau satu MULTIPOP bisa O(n), total biaya **n operasi** atas stack kosong adalah O(n) (tiap elemen di-push sekali dan di-pop paling banyak sekali). Maka biaya teramortisasi per operasi = **O(1)**.

#### 16.2 Metode Akunting

Tetapkan **biaya teramortisasi (amortized cost)** ĉᵢ ke tiap operasi, yang bisa berbeda dari biaya nyata cᵢ. Operasi murah "membayar lebih" dan menyimpan **kredit**; operasi mahal "memakai" kredit. Syarat valid: total ĉ ≥ total c untuk setiap barisan, yakni saldo kredit tak pernah negatif.

**Contoh — stack:** tetapkan ĉ(PUSH) = 2 (1 untuk push, 1 disimpan sebagai kredit melekat pada elemen), ĉ(POP) = 0, ĉ(MULTIPOP) = 0. Karena tiap elemen membawa kredit untuk pop-nya sendiri, saldo selalu ≥ 0. Biaya teramortisasi O(1).

#### 16.3 Metode Potensial

Definisikan **fungsi potensial (potential function)** Φ yang memetakan keadaan struktur data ke bilangan riil. Biaya teramortisasi operasi ke-i:

> ĉᵢ = cᵢ + Φ(Dᵢ) − Φ(Dᵢ₋₁),

dengan Dᵢ keadaan setelah operasi ke-i. Total: ∑ĉᵢ = ∑cᵢ + Φ(Dₙ) − Φ(D₀). Jika Φ(Dₙ) ≥ Φ(D₀) (mis. Φ ≥ 0 dan Φ(D₀)=0), maka ∑ĉᵢ adalah batas atas total biaya nyata.

**Contoh — stack:** Φ = jumlah elemen di stack. PUSH: ĉ = 1 + 1 = 2; POP/MULTIPOP: ĉ = c − c = 0. Konsisten dengan metode lain.

#### 16.4 Tabel Dinamis (Dynamic Tables)

**Persoalan:** Tabel/larik yang membesar saat penuh. Strategi **penggandaan (doubling):** saat penuh, alokasikan tabel berukuran **dua kali** dan salin elemen. Satu penyisipan yang memicu penggandaan berbiaya Θ(n), tetapi penyisipan tersebut jarang.

**Analisis:** Dengan metode agregat/potensial, biaya total n penyisipan adalah **O(n)**, sehingga biaya teramortisasi tiap TABLE-INSERT adalah **O(1)**. Fungsi potensial yang umum: Φ = 2·num − size. Bila tabel juga menyusut (saat ¼ penuh, menyusut setengah), TABLE-DELETE juga teramortisasi O(1), menghindari *thrashing*.

| Operasi | Biaya terburuk tunggal | Biaya teramortisasi |
|---|---|---|
| Stack PUSH/POP/MULTIPOP | O(n) (MULTIPOP) | O(1) |
| Increment binary counter | O(k) (k bit) | O(1) |
| TABLE-INSERT (doubling) | Θ(n) | O(1) |

### Istilah Kunci

- **Amortized analysis:** biaya rata-rata per operasi atas barisan kasus terburuk (tanpa probabilitas).
- **Aggregate method:** total biaya dibagi jumlah operasi.
- **Accounting method:** biaya teramortisasi + sistem kredit.
- **Potential method:** fungsi potensial Φ; ĉ = c + ΔΦ.
- **Dynamic table:** tabel yang membesar/menyusut; penggandaan memberi insert O(1) teramortisasi.
- **Credit (kredit):** "tabungan" biaya untuk operasi mahal mendatang.

### Contoh / Studi Kasus: Binary Counter

INCREMENT pada counter biner k-bit: satu operasi bisa membalik k bit (saat 0111…1 → 1000…0), tetapi rata-rata jumlah bit yang dibalik per INCREMENT adalah ≤ 2 (bit ke-0 selalu, bit ke-1 separuh waktu, dst.: ∑1/2ⁱ < 2). Maka **biaya teramortisasi O(1)** per INCREMENT, total n operasi O(n).

### Rangkuman

Analisis teramortisasi menunjukkan bahwa biaya rata-rata per operasi sepanjang barisan bisa jauh lebih kecil daripada biaya terburuk satu operasi. Tiga metode—agregat, akunting, dan potensial—saling melengkapi. Aplikasi penting: stack MULTIPOP (O(1)), binary counter (O(1)), dan tabel dinamis dengan penggandaan (insert O(1) teramortisasi). Teknik ini menjadi dasar analisis struktur data lanjutan seperti disjoint sets (Bab 19).

### Latihan & Soal

1. **(Pemahaman)** Mengapa analisis teramortisasi tidak melibatkan probabilitas?
2. **(Analisis)** Dengan metode potensial, analisis biaya INCREMENT counter biner (pilih Φ = jumlah bit-1).
3. **(Analisis/HOTS)** Buktikan biaya teramortisasi TABLE-INSERT dengan penggandaan adalah O(1) memakai Φ = 2·num − size.
4. **(HOTS)** Mengapa menyusutkan tabel pada saat ¼ penuh (bukan ½) menghindari thrashing? Analisis.
5. **(Implementasi)** Rancang stack yang mendukung PUSH, POP, dan MULTIPOP dengan analisis teramortisasi lengkap (ketiga metode).

---

# BAGIAN V — Struktur Data Lanjutan

## Pengantar Bagian V

Bagian ini menyajikan struktur data yang lebih canggih untuk kebutuhan khusus. **Augmentasi struktur data** (Bab 17) menunjukkan cara menambahkan informasi pada struktur yang ada (mis. red-black tree) untuk mendukung operasi baru tanpa mengorbankan efisiensi. **B-Trees** (Bab 18) dirancang untuk penyimpanan sekunder (disk), meminimalkan operasi I/O dengan simpul berderajat tinggi. **Struktur data untuk himpunan terpisah (disjoint sets)** (Bab 19) mendukung operasi gabung/cari yang sangat efisien dengan heuristik union by rank dan path compression.

---

## Bab 17 — Augmentasi Struktur Data

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** metodologi augmentasi struktur data dalam empat langkah.
2. **Merancang** order-statistic tree untuk SELECT dan RANK dalam O(lg n).
3. **Membuktikan** teorema augmentasi untuk red-black tree.
4. **Menerapkan** augmentasi pada interval tree.

### Peta Konsep

```
AUGMENTASI: tambah info ke struktur (mis. RB-tree) untuk operasi baru
  Langkah: 1) pilih struktur dasar 2) tentukan info tambahan
           3) verifikasi info dipelihara 4) kembangkan operasi baru
  +-- Order-statistic tree: x.size -> OS-SELECT, OS-RANK O(lg n)
  +-- Interval tree: x.max -> INTERVAL-SEARCH O(lg n)
```

### Materi Inti

#### 17.1 Dynamic Order Statistics

**Order-statistic tree** adalah red-black tree yang tiap simpul `x` diaugmentasi dengan `x.size` = jumlah simpul di subpohon berakar di x (termasuk x). Ini memungkinkan:

- **OS-SELECT(x, i):** kembalikan simpul dengan kunci ke-i terkecil di subpohon x, dalam **O(lg n)**.
- **OS-RANK(T, x):** kembalikan peringkat (rank) x dalam urutan terurut, dalam **O(lg n)**.

```text
OS-SELECT(x, i)
1  r = x.left.size + 1            // peringkat x dalam subpohonnya
2  if i == r
3      return x
4  elseif i < r
5      return OS-SELECT(x.left, i)
6  else return OS-SELECT(x.right, i - r)
```

Atribut `size` dipelihara saat INSERT/DELETE dan rotasi dengan biaya konstan tambahan per simpul pada lintasan, sehingga operasi tetap **O(lg n)**.

#### 17.2 Cara Mengaugmentasi Struktur Data

Metodologi empat langkah:

1. **Pilih** struktur data dasar (mis. red-black tree).
2. **Tentukan** informasi tambahan yang dipelihara.
3. **Verifikasi** informasi tambahan dapat dipelihara untuk operasi dasar (INSERT, DELETE, rotasi) tanpa menambah biaya asimtotik.
4. **Kembangkan** operasi baru yang memanfaatkan informasi tambahan.

> **Teorema augmentasi (red-black).** Jika atribut tambahan `f` pada tiap simpul x hanya bergantung pada informasi di x, x.left, dan x.right (termasuk f anak-anaknya), maka f dapat dipelihara pada semua operasi INSERT dan DELETE dalam O(lg n) tanpa memengaruhi kompleksitas asimtotik.

#### 17.3 Interval Tree

**Interval tree** mengaugmentasi red-black tree (dikunci pada titik awal interval `i.low`) dengan `x.max` = nilai akhir maksimum di subpohon. Operasi INTERVAL-SEARCH menemukan interval yang **tumpang tindih** dengan interval query dalam **O(lg n)**:

```text
INTERVAL-SEARCH(T, i)
1  x = T.root
2  while x != T.nil and i tidak tumpang tindih dengan x.int
3      if x.left != T.nil and x.left.max >= i.low
4          x = x.left
5      else x = x.right
6  return x
```

### Istilah Kunci

- **Augmentasi (data structure augmentation):** menambah informasi ke struktur untuk operasi baru.
- **Order-statistic tree:** RB-tree dengan atribut `size`; SELECT/RANK O(lg n).
- **Interval tree:** RB-tree dengan atribut `max`; pencarian tumpang tindih O(lg n).
- **Size attribute:** jumlah simpul subpohon.

### Contoh / Studi Kasus

Pada order-statistic tree, OS-RANK menghitung rank kunci tertentu dengan menjumlahkan ukuran subpohon kiri sepanjang lintasan dari simpul ke akar. Untuk pohon 17 simpul, OS-SELECT(root, 5) menelusuri ≤ tinggi pohon ≈ 5 langkah → O(lg n).

### Rangkuman

Augmentasi memperkaya struktur data yang ada dengan informasi tambahan untuk mendukung operasi baru, mengikuti metodologi empat langkah dan teorema augmentasi. Order-statistic tree menambahkan `size` untuk SELECT/RANK O(lg n); interval tree menambahkan `max` untuk pencarian tumpang tindih O(lg n). Kuncinya: informasi tambahan harus dapat dipelihara secara lokal saat operasi dan rotasi.

### Latihan & Soal

1. **(Pemahaman)** Sebutkan empat langkah metodologi augmentasi.
2. **(Tracing)** Jalankan OS-SELECT untuk i=4 pada order-statistic tree contoh.
3. **(Analisis/HOTS)** Buktikan `x.size` dapat dipelihara dalam O(1) per rotasi.
4. **(Implementasi)** Tulis OS-RANK dan analisis kompleksitasnya.
5. **(HOTS)** Mengapa interval tree menggunakan `max` dan bukan `min`? Buktikan kebenaran INTERVAL-SEARCH.

---

## Bab 18 — B-Trees

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** B-tree dan properti keseimbangannya berdasarkan derajat minimum t.
2. **Menjelaskan** motivasi B-tree untuk penyimpanan sekunder (disk).
3. **Mengimplementasikan** B-TREE-SEARCH, B-TREE-INSERT (dengan split), dan prinsip penghapusan.
4. **Menganalisis** kompleksitas operasi O(t·log_t n) waktu CPU dan O(log_t n) akses disk.

### Peta Konsep

```
B-TREE (derajat minimum t >= 2) -> seimbang, tinggi O(log_t n)
  +-- Simpul: t-1 .. 2t-1 kunci ; t .. 2t anak
  +-- SEARCH : O(t log_t n) CPU, O(log_t n) disk reads
  +-- INSERT : split simpul penuh saat turun (top-down)
  +-- DELETE : merge/borrow agar simpul tak kurang dari t-1 kunci
```

### Materi Inti

#### Motivasi: Penyimpanan Sekunder

Akses **disk (penyimpanan sekunder)** jauh lebih lambat daripada memori utama. B-tree meminimalkan jumlah **akses disk** dengan membuat tiap simpul memuat **banyak kunci** (sesuai ukuran satu blok/halaman disk), sehingga pohon menjadi sangat "pendek dan lebar". Tinggi B-tree dengan n kunci adalah **O(log_t n)**, jauh lebih kecil daripada BST biner.

#### 18.1 Definisi B-Tree

B-tree dengan **derajat minimum (minimum degree)** t ≥ 2 memenuhi:

> 1. Setiap simpul x punya atribut: `x.n` (jumlah kunci), kunci `x.key₁ ≤ … ≤ x.key_{x.n}` terurut, `x.leaf` (boolean).
> 2. Setiap simpul internal punya `x.n + 1` pointer anak.
> 3. **Batas kunci:** setiap simpul (kecuali akar) punya **≥ t−1** kunci; setiap simpul punya **≤ 2t−1** kunci. Jadi simpul internal punya antara t dan 2t anak. Akar punya ≥ 1 kunci (bila pohon tak kosong).
> 4. **Semua daun berada pada kedalaman sama** (= tinggi pohon).

Simpul dengan tepat 2t−1 kunci disebut **penuh (full)**.

> **Lema (tinggi).** B-tree dengan n ≥ 1 kunci dan derajat minimum t ≥ 2 memiliki tinggi h ≤ log_t((n+1)/2).

#### 18.2 Operasi Dasar

**B-TREE-SEARCH** mirip pencarian BST tetapi membuat keputusan bercabang di antara `x.n+1` anak pada tiap simpul. Waktu CPU **O(t·log_t n)** dan akses disk **O(log_t n)**.

**B-TREE-INSERT** menggunakan pendekatan **satu lintasan turun (single pass down)**: saat menelusuri ke bawah, setiap simpul **penuh** yang dijumpai langsung **dibelah (split)** lewat B-TREE-SPLIT-CHILD, sehingga selalu ada ruang untuk penyisipan di daun. Pembelahan memindahkan kunci median ke induk dan memecah simpul penuh menjadi dua. Operasi berjalan **O(t·log_t n)** CPU, **O(log_t n)** disk.

```text
B-TREE-SPLIT-CHILD(x, i)   // x.cᵢ penuh (2t-1 kunci); belah jadi dua
  - alokasikan simpul z; pindahkan t-1 kunci teratas dari y=x.cᵢ ke z
  - naikkan kunci median y.key_t ke x pada posisi i
  - sisipkan z sebagai anak x
```

**Penghapusan** lebih rumit: untuk menjaga batas ≥ t−1 kunci, sebelum turun ke anak yang punya tepat t−1 kunci, dilakukan **peminjaman (borrow)** kunci dari saudara atau **penggabungan (merge)** dengan saudara. Tetap **O(t·log_t n)**.

### Istilah Kunci

- **B-tree:** pohon pencarian seimbang berderajat tinggi untuk disk.
- **Minimum degree t:** parameter; tiap simpul 't−1' s.d. '2t−1' kunci.
- **Full node (simpul penuh):** memuat 2t−1 kunci.
- **Split (pembelahan):** memecah simpul penuh, menaikkan median ke induk.
- **Disk access (akses disk):** ukuran biaya dominan; B-tree meminimalkannya.

### Contoh / Studi Kasus

Untuk t = 2 (B-tree disebut juga 2-3-4 tree), tiap simpul punya 1–3 kunci dan 2–4 anak. Menyisipkan barisan kunci memicu pembelahan saat simpul penuh (3 kunci), menaikkan median ke induk. Tinggi tetap O(log n) dan semua daun sejajar.

### Rangkuman

B-tree adalah pohon pencarian seimbang berderajat tinggi yang dirancang meminimalkan akses disk: tiap simpul memuat banyak kunci (t−1 hingga 2t−1), tinggi O(log_t n), dan semua daun pada kedalaman sama. SEARCH, INSERT (dengan split top-down), dan DELETE (dengan borrow/merge) berjalan O(t·log_t n) CPU dan O(log_t n) akses disk. B-tree adalah fondasi sistem basis data dan sistem berkas.

### Latihan & Soal

1. **(Pemahaman)** Mengapa B-tree cocok untuk penyimpanan sekunder, bukan memori utama?
2. **(Analisis)** Buktikan tinggi B-tree h ≤ log_t((n+1)/2).
3. **(Tracing)** Sisipkan kunci F, S, Q, K, C, L, H, T, V, W, M, R, N, P, A, B, X, Y, D, Z, E ke B-tree dengan t=3.
4. **(HOTS)** Jelaskan mengapa pendekatan single-pass-down pada INSERT menghindari kebutuhan naik kembali.
5. **(Analisis)** Mengapa penghapusan memerlukan borrow/merge? Apa yang dijamin keduanya?

---

## Bab 19 — Struktur Data untuk Himpunan Terpisah (Disjoint Sets)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** operasi MAKE-SET, UNION, dan FIND-SET pada struktur disjoint-set.
2. **Membandingkan** representasi linked-list dan disjoint-set forest.
3. **Menerapkan** heuristik **union by rank** dan **path compression**.
4. **Menyatakan** kompleksitas teramortisasi O(α(n)) per operasi.

### Peta Konsep

```
DISJOINT SETS: kelola koleksi himpunan terpisah
  Operasi: MAKE-SET(x), UNION(x,y), FIND-SET(x)
  +-- Linked-list representation (weighted-union)
  +-- Disjoint-set FOREST (pohon, parent pointer)
        +-- Union by rank
        +-- Path compression
        -> m operasi: O(m α(n)), α tumbuh ekstrem lambat
```

### Materi Inti

#### 19.1 Operasi Disjoint-Set

Struktur **disjoint-set (union-find)** memelihara koleksi himpunan terpisah yang dinamis, masing-masing diidentifikasi oleh **representative (wakil)**:

- **MAKE-SET(x):** buat himpunan baru berisi hanya x.
- **UNION(x, y):** gabungkan himpunan yang memuat x dan yang memuat y.
- **FIND-SET(x):** kembalikan wakil himpunan yang memuat x.

Aplikasi penting: menentukan komponen terhubung, dan algoritma **Kruskal** untuk MST (Bab 21).

#### 19.2 Representasi Linked-List

Tiap himpunan = linked list; wakil = elemen pertama. FIND-SET O(1), tetapi UNION naif bisa O(n) karena memperbarui pointer. Dengan heuristik **weighted union** (selalu sambung list yang lebih pendek ke yang lebih panjang), barisan m operasi yang melibatkan n MAKE-SET berjalan **O(m + n lg n)**.

#### 19.3 Disjoint-Set Forest

Representasi lebih efisien: tiap himpunan adalah **pohon berakar**; tiap simpul menunjuk **induknya** (`x.p`), dan akar menunjuk dirinya sendiri (wakil). Dua heuristik mempercepat drastis:

- **Union by rank:** tiap akar menyimpan `rank` (batas atas tinggi). Saat UNION, akar berank lebih kecil ditautkan ke akar berank lebih besar.
- **Path compression:** saat FIND-SET, buat tiap simpul pada lintasan menunjuk **langsung ke akar**, meratakan pohon.

```text
MAKE-SET(x)            FIND-SET(x)                 UNION(x, y)
1 x.p = x              1 if x != x.p               1 LINK(FIND-SET(x), FIND-SET(y))
2 x.rank = 0          2     x.p = FIND-SET(x.p)    LINK(x, y):
                      3 return x.p                  if x.rank > y.rank: y.p = x
                      (path compression)            else: x.p = y
                                                     if x.rank == y.rank: y.rank++
```

#### 19.4 Analisis: Fungsi Ackermann Invers

> **Teorema.** Dengan **kedua** heuristik (union by rank + path compression), barisan m operasi MAKE-SET, UNION, FIND-SET yang melibatkan n MAKE-SET berjalan dalam waktu **O(m · α(n))**, dengan α adalah **invers fungsi Ackermann** — fungsi yang tumbuh sangat lambat sehingga α(n) ≤ 4 untuk semua n yang praktis (n ≤ 2^65536 atau lebih).

Dengan kata lain, biaya teramortisasi per operasi **hampir konstan**. Inilah salah satu hasil analisis paling elegan dalam ilmu komputer.

### Istilah Kunci

- **Disjoint sets / union-find:** koleksi himpunan terpisah dinamis.
- **MAKE-SET / UNION / FIND-SET:** operasi inti.
- **Representative (wakil):** identitas himpunan.
- **Union by rank:** sambung pohon berank kecil ke yang besar.
- **Path compression:** ratakan lintasan ke akar saat FIND-SET.
- **α(n) (invers Ackermann):** fungsi sangat lambat; ≤ 4 secara praktis.

### Contoh / Studi Kasus

Mulai dengan 6 elemen terpisah {1},{2},…,{6}. Setelah UNION(1,2), UNION(3,4), UNION(1,3): himpunan menjadi {1,2,3,4} (satu pohon), {5}, {6}. FIND-SET pada elemen 4 mengembalikan wakil himpunan {1,2,3,4}, dan path compression meratakan pohon.

### Rangkuman

Disjoint-set mendukung MAKE-SET, UNION, FIND-SET. Representasi disjoint-set forest dengan union by rank dan path compression mencapai biaya teramortisasi O(α(n)) per operasi—hampir konstan dalam praktik. Struktur ini krusial untuk komponen terhubung dan algoritma Kruskal.

### Latihan & Soal

1. **(Pemahaman)** Jelaskan peran wakil (representative) dalam disjoint-set.
2. **(Tracing)** Lakukan barisan MAKE-SET/UNION/FIND-SET dan tunjukkan struktur pohon dengan kedua heuristik.
3. **(Analisis/HOTS)** Mengapa kombinasi union by rank + path compression memberi O(m α(n))?
4. **(Analisis)** Tunjukkan weighted-union linked-list memberi O(m + n lg n).
5. **(HOTS)** Jelaskan bagaimana disjoint-set dipakai dalam algoritma Kruskal (Bab 21).

---

# BAGIAN VI — Algoritma Graf

## Pengantar Bagian VI

Graf memodelkan relasi antar objek dan muncul di hampir semua domain: jaringan, peta jalan, jejaring sosial, penjadwalan, dan kompilasi. Bagian ini membahas algoritma graf fundamental: **penelusuran elementer** BFS/DFS dan topological sort (Bab 20); **minimum spanning tree** Kruskal dan Prim (Bab 21); **lintasan terpendek sumber-tunggal** Bellman-Ford dan Dijkstra (Bab 22); **lintasan terpendek semua-pasangan** Floyd-Warshall dan Johnson (Bab 23); **aliran maksimum** Ford-Fulkerson (Bab 24); dan **pencocokan pada graf bipartit** (Bab 25).

### Representasi Graf

Graf G = (V, E) direpresentasikan dengan dua cara utama:

- **Adjacency list (daftar ketetanggaan):** larik Adj[1 : |V|] di mana Adj[u] adalah list tetangga u. Ruang **Θ(V + E)**, ideal untuk **graf jarang (sparse)** (|E| ≪ |V|²).
- **Adjacency matrix (matriks ketetanggaan):** matriks |V|×|V| dengan aᵢⱼ = 1 jika ada sisi (i, j). Ruang **Θ(V²)**, ideal untuk **graf padat (dense)** atau bila perlu cek sisi O(1).

(Catatan konvensi: dalam notasi asimtotik algoritma graf, kita menulis V dan E sebagai pengganti |V| dan |E|.)

---

## Bab 20 — Algoritma Graf Elementer

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membandingkan** representasi adjacency list dan adjacency matrix.
2. **Mengimplementasikan** **Breadth-First Search (BFS)** dan menghitung jarak terpendek (jumlah sisi).
3. **Mengimplementasikan** **Depth-First Search (DFS)** beserta waktu penemuan/penyelesaian dan klasifikasi sisi.
4. **Menerapkan** DFS untuk **topological sort** dan **strongly connected components (SCC)**.
5. **Menganalisis** kompleksitas Θ(V + E) untuk BFS dan DFS.

### Peta Konsep

```
PENELUSURAN GRAF
  +-- BFS (queue) : lapisan demi lapisan; jarak terpendek (unweighted); Θ(V+E)
  +-- DFS (rekursi/stack) : kedalaman; waktu d/f; Θ(V+E)
        +-- klasifikasi sisi: tree, back, forward, cross
        +-- Topological sort (DAG) : urutan linear; Θ(V+E)
        +-- SCC (dua DFS) : komponen terhubung kuat
```

### Materi Inti

#### 20.2 Breadth-First Search (BFS)

**BFS** menjelajah graf "lapisan demi lapisan" dari simpul sumber s, mengunjungi semua simpul berjarak k sebelum berjarak k+1. Menggunakan **queue (FIFO)** dan pewarnaan simpul (WHITE=belum ditemukan, GRAY=di frontier, BLACK=selesai). BFS menghitung **jarak terpendek** (jumlah sisi) dari s ke semua simpul pada graf tak berbobot, dan membangun **breadth-first tree**.

```text
BFS(G, s)
 1  for setiap vertex u ∈ G.V − {s}
 2      u.color = WHITE ; u.d = ∞ ; u.π = NIL
 3  s.color = GRAY ; s.d = 0 ; s.π = NIL
 4  Q = ∅
 5  ENQUEUE(Q, s)
 6  while Q ≠ ∅
 7      u = DEQUEUE(Q)
 8      for setiap vertex v ∈ G.Adj[u]      // periksa tetangga u
 9          if v.color == WHITE              // v baru ditemukan?
10              v.color = GRAY
11              v.d = u.d + 1
12              v.π = u
13              ENQUEUE(Q, v)                // v sekarang di frontier
14      u.color = BLACK                      // u selesai diproses
```

**Analisis:** Setiap simpul di-enqueue/dequeue tepat sekali (O(V)), dan tiap sisi diperiksa sekali (list) atau dua kali (graf tak berarah) → total **Θ(V + E)**. Atribut `v.d` memberi jarak terpendek; `v.π` membentuk pohon BFS untuk merekonstruksi lintasan.

#### 20.3 Depth-First Search (DFS)

**DFS** menjelajah "sedalam mungkin" sebelum mundur (backtrack). Tiap simpul memperoleh dua **timestamp**: `u.d` (discovery/penemuan) dan `u.f` (finish/penyelesaian), memenuhi struktur kurung bersarang (**parenthesis theorem**).

```text
DFS(G)                              DFS-VISIT(G, u)
1 for setiap u ∈ G.V               1 time = time + 1
2     u.color = WHITE              2 u.d = time ; u.color = GRAY
3     u.π = NIL                    3 for setiap v ∈ G.Adj[u]
4 time = 0                         4     if v.color == WHITE
5 for setiap u ∈ G.V               5         v.π = u
6     if u.color == WHITE          6         DFS-VISIT(G, v)
7         DFS-VISIT(G, u)          7 u.color = BLACK
                                   8 time = time + 1 ; u.f = time
```

**Analisis:** Inisialisasi Θ(V); DFS-VISIT dipanggil tepat sekali per simpul, dan loop dalamnya menjumlahkan |Adj[u]| = Θ(E) → total **Θ(V + E)**.

**Klasifikasi sisi (edge classification):** DFS mengklasifikasikan sisi menjadi **tree edge** (sisi pohon DFS), **back edge** (ke leluhur — menandakan **siklus**), **forward edge** (ke keturunan non-anak), dan **cross edge** (antar subpohon). Pada graf tak berarah hanya ada tree dan back edge.

#### 20.4 Topological Sort

**Topological sort** dari **DAG (directed acyclic graph)** adalah pengurutan linear simpul sehingga jika ada sisi (u, v), maka u mendahului v. Berguna untuk penjadwalan dengan ketergantungan (mis. urutan mengenakan pakaian, urutan kompilasi modul).

```text
TOPOLOGICAL-SORT(G)
1  panggil DFS(G) untuk menghitung u.f tiap simpul u
2  saat tiap simpul selesai (finish), tambahkan ke DEPAN sebuah linked list
3  return linked list simpul (terurut menurun menurut waktu f)
```

**Analisis:** **Θ(V + E)** (didominasi DFS). Bukti kebenaran: sisi (u, v) berarti u selesai setelah v (u.f > v.f), sehingga u muncul lebih dulu dalam urutan menurun f.

#### 20.5 Strongly Connected Components (SCC)

**SCC** dari graf berarah adalah partisi simpul ke kelas-kelas di mana setiap dua simpul saling **terjangkau (mutually reachable)**. Algoritma SCC (Kosaraju/Tarjan-style yang dibahas CLRS):

```text
STRONGLY-CONNECTED-COMPONENTS(G)
1  panggil DFS(G) untuk menghitung u.f
2  hitung transpos Gᵀ (balik arah semua sisi)
3  panggil DFS(Gᵀ), memproses simpul dalam urutan menurun u.f
4  tiap pohon DFS pada langkah 3 adalah satu SCC
```

**Analisis:** dua DFS + transpos → **Θ(V + E)**.

### Istilah Kunci

- **Adjacency list / matrix:** representasi graf (Θ(V+E) / Θ(V²)).
- **BFS:** penelusuran lebar; jarak terpendek tak berbobot; queue; Θ(V+E).
- **DFS:** penelusuran dalam; timestamp d/f; Θ(V+E).
- **Edge classification:** tree/back/forward/cross; back edge ⇒ siklus.
- **Topological sort:** urutan linear DAG; Θ(V+E).
- **Strongly connected component (SCC):** komponen saling terjangkau.
- **DAG (directed acyclic graph):** graf berarah tanpa siklus.

### Contoh / Studi Kasus: Topological Sort

Untuk DAG ketergantungan pakaian (kaus kaki → sepatu, celana → sepatu, dst.), DFS menghasilkan waktu f; mengurutkan menurun memberi urutan pemakaian valid. Misal: jam tangan, celana dalam, celana, sabuk, kemeja, dasi, jas, kaus kaki, sepatu.

### Rangkuman

BFS (queue) menjelajah lapisan demi lapisan dan menghitung jarak terpendek tak berbobot; DFS (rekursi) menjelajah secara mendalam, memberi timestamp dan mengklasifikasi sisi. Keduanya Θ(V+E). DFS menjadi dasar topological sort (urutan DAG) dan SCC (dua DFS). Algoritma elementer ini adalah blok bangunan hampir semua algoritma graf lanjutan.

### Latihan & Soal

1. **(Tracing)** Jalankan BFS dari simpul s pada graf contoh; tunjukkan d dan π tiap simpul.
2. **(Tracing)** Jalankan DFS; tuliskan d/f dan klasifikasikan tiap sisi.
3. **(Pemahaman)** Mengapa back edge pada DFS menandakan adanya siklus?
4. **(Analisis/HOTS)** Buktikan TOPOLOGICAL-SORT benar menggunakan sifat u.f > v.f untuk sisi (u,v).
5. **(HOTS)** Jelaskan mengapa DFS pada Gᵀ dalam urutan menurun f menghasilkan SCC yang benar.

---

## Bab 21 — Minimum Spanning Trees (MST)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** persoalan minimum spanning tree pada graf berbobot tak berarah.
2. **Menyatakan** metode generik MST dan konsep **safe edge** serta **cut**.
3. **Mengimplementasikan** algoritma **Kruskal** dan **Prim**.
4. **Menganalisis** kompleksitas keduanya: O(E lg V).

### Peta Konsep

```
MST: subgraf pohon merentang berbobot minimum
  Metode generik: tambah SAFE EDGE berulang
  Teorema cut: light edge melintasi cut yang respek A adalah aman
  +-- Kruskal (disjoint-set, urut sisi) : O(E lg V)
  +-- Prim (priority queue, tumbuh dari akar) : O(E lg V)
```

### Materi Inti

#### 21.1 Menumbuhkan MST

**Minimum spanning tree (MST)** dari graf berbobot tak berarah terhubung G = (V, E) dengan bobot w adalah pohon merentang (subset sisi yang menghubungkan semua simpul tanpa siklus) dengan **total bobot minimum**. MST memiliki |V|−1 sisi.

**Metode generik** menumbuhkan himpunan sisi A yang selalu merupakan subset suatu MST, dengan menambahkan **safe edge (sisi aman)** satu per satu:

```text
GENERIC-MST(G, w)
1  A = ∅
2  while A belum membentuk spanning tree
3      cari sisi (u, v) yang AMAN untuk A
4      A = A ∪ {(u, v)}
5  return A
```

**Konsep kunci:**
- **Cut (potongan)** (S, V−S): partisi simpul. Sebuah sisi **melintasi (crosses)** cut bila satu ujungnya di S dan ujung lain di V−S.
- Cut **menghormati (respects)** A bila tak ada sisi A yang melintasinya.
- **Light edge:** sisi berbobot minimum yang melintasi cut.

> **Teorema (sisi aman).** Misalkan A subset suatu MST, (S, V−S) cut yang menghormati A, dan (u, v) light edge melintasi cut tersebut. Maka (u, v) **aman** untuk A.

#### 21.2 Algoritma Kruskal

**Kruskal** memperlakukan tiap simpul sebagai pohon terpisah, lalu **mengurutkan semua sisi menurut bobot menaik** dan menambahkan tiap sisi bila ia menghubungkan dua pohon berbeda (tidak membentuk siklus). Menggunakan struktur **disjoint-set** (Bab 19).

```text
MST-KRUSKAL(G, w)
 1  A = ∅
 2  for setiap vertex v ∈ G.V
 3      MAKE-SET(v)
 4  buat satu list dari semua sisi G.E
 5  urutkan list sisi menurut bobot w menaik
 6  for setiap sisi (u, v) dari list terurut
 7      if FIND-SET(u) ≠ FIND-SET(v)        // beda komponen → tak ada siklus
 8          A = A ∪ {(u, v)}
 9          UNION(u, v)
10  return A
```

**Analisis:** Pengurutan sisi **O(E lg E)**. Operasi disjoint-set total O(E·α(V)). Karena lg E = O(lg V) (sebab |E| < |V|²), total waktu **O(E lg V)**.

#### 21.2 Algoritma Prim

**Prim** menumbuhkan **satu pohon** dari simpul akar r, pada tiap langkah menambahkan **light edge** yang menghubungkan pohon ke simpul di luar pohon. Menggunakan **min-priority queue** berkunci `v.key` (bobot sisi teringan yang menghubungkan v ke pohon).

```text
MST-PRIM(G, w, r)
 1  for setiap u ∈ G.V
 2      u.key = ∞ ; u.π = NIL
 3  r.key = 0
 4  Q = ∅
 5  for setiap u ∈ G.V
 6      INSERT(Q, u)
 7  while Q ≠ ∅
 8      u = EXTRACT-MIN(Q)                   // tambahkan u ke pohon
 9      for setiap v ∈ G.Adj[u]              // perbarui key tetangga non-pohon
10          if v ∈ Q and w(u, v) < v.key
11              v.π = u
12              v.key = w(u, v)
13              DECREASE-KEY(Q, v, w(u, v))
```

**Analisis:** Dengan **binary heap**: V kali EXTRACT-MIN (O(lg V) masing-masing) + E kali DECREASE-KEY (O(lg V)) → **O((V + E) lg V) = O(E lg V)** untuk graf terhubung. Dengan **Fibonacci heap**, DECREASE-KEY teramortisasi O(1) → O(E + V lg V).

| Algoritma | Struktur data | Waktu |
|---|---|---|
| Kruskal | disjoint-set + sorting | O(E lg V) |
| Prim (binary heap) | min-priority queue | O(E lg V) |
| Prim (Fibonacci heap) | min-priority queue | O(E + V lg V) |

### Istilah Kunci

- **Minimum spanning tree (MST):** pohon merentang berbobot minimum.
- **Safe edge (sisi aman):** sisi yang dapat ditambahkan tanpa keluar dari suatu MST.
- **Cut / light edge:** partisi simpul / sisi terringan yang melintasi cut.
- **Kruskal's algorithm:** greedy berbasis pengurutan sisi + disjoint-set.
- **Prim's algorithm:** greedy menumbuhkan satu pohon + priority queue.

### Contoh / Studi Kasus

Graf 9-simpul klasik (a..i) dengan bobot beragam. MST memiliki total bobot 37 (mis. sisi {a-b:4, b-c:8, ... } pilihan yang membentuk pohon minimum). Kruskal menambahkan sisi termurah dulu (mis. bobot 1, 2, 2, ...) selama tak membentuk siklus; Prim menumbuhkan dari a dengan menambah light edge tiap langkah.

### Rangkuman

MST menghubungkan semua simpul dengan total bobot minimum. Metode generik menambahkan safe edge berdasarkan teorema cut. Kruskal mengurutkan sisi dan menggunakan disjoint-set (O(E lg V)); Prim menumbuhkan satu pohon dengan priority queue (O(E lg V) dengan binary heap). Keduanya adalah algoritma greedy yang terbukti optimal.

### Latihan & Soal

1. **(Pemahaman)** Definisikan cut, light edge, dan safe edge.
2. **(Tracing)** Jalankan Kruskal dan Prim pada graf berbobot contoh; bandingkan urutan penambahan sisi.
3. **(Analisis/HOTS)** Buktikan teorema sisi aman (cut theorem).
4. **(Analisis)** Mengapa total waktu Kruskal dapat ditulis O(E lg V) meski pengurutan O(E lg E)?
5. **(HOTS)** Kapan Prim dengan Fibonacci heap menguntungkan dibanding binary heap?

---

## Bab 22 — Lintasan Terpendek Sumber-Tunggal

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** persoalan single-source shortest paths dan konsep **relaxation**.
2. **Mengimplementasikan** **Bellman-Ford** (dengan deteksi siklus berbobot negatif) dan **Dijkstra**.
3. **Menganalisis** kompleksitas O(VE) dan O((V+E) lg V).
4. **Menjelaskan** lintasan terpendek pada DAG dalam Θ(V+E).

### Peta Konsep

```
SHORTEST PATHS (single source)
  RELAX(u,v,w): if v.d > u.d + w(u,v) then perbarui
  +-- DAG (topological order)        : Θ(V+E)
  +-- Bellman-Ford (bobot negatif OK): O(VE), deteksi siklus negatif
  +-- Dijkstra (bobot non-negatif)   : O((V+E) lg V) dgn binary heap
```

### Materi Inti

#### Dasar: Inisialisasi dan Relaxation

Tiap simpul menyimpan estimasi `v.d` (batas atas bobot lintasan terpendek) dan `v.π` (predecessor). Bobot lintasan terpendek aktual dilambangkan δ(s, v).

```text
INITIALIZE-SINGLE-SOURCE(G, s)      RELAX(u, v, w)
1 for setiap v ∈ G.V                1 if v.d > u.d + w(u, v)
2     v.d = ∞ ; v.π = NIL           2     v.d = u.d + w(u, v)
3 s.d = 0                           3     v.π = u
```

**Relaxation (relaksasi)** menguji apakah lintasan ke v dapat diperpendek melalui u; bila ya, perbarui v.d dan v.π. Semua algoritma lintasan terpendek berulang melakukan relaksasi sisi, berbeda hanya pada **urutan** relaksasi.

#### 22.1 Algoritma Bellman-Ford

**Bellman-Ford** menangani sisi **berbobot negatif** dan **mendeteksi siklus berbobot negatif** yang terjangkau dari sumber. Ia merelaksasi **semua sisi** sebanyak |V|−1 kali.

```text
BELLMAN-FORD(G, w, s)
1  INITIALIZE-SINGLE-SOURCE(G, s)
2  for i = 1 to |G.V| − 1
3      for setiap sisi (u, v) ∈ G.E
4          RELAX(u, v, w)
5  for setiap sisi (u, v) ∈ G.E         // cek siklus negatif
6      if v.d > u.d + w(u, v)
7          return FALSE
8  return TRUE
```

**Analisis:** Inisialisasi Θ(V); |V|−1 lintasan masing-masing merelaksasi |E| sisi → **O(VE)**. Mengembalikan FALSE bila ada siklus berbobot negatif yang terjangkau dari s, TRUE jika tidak (lalu v.d = δ(s,v) untuk semua v).

> **Korektness (Lema).** Jika tak ada siklus berbobot negatif terjangkau dari s, maka setelah |V|−1 lintasan, v.d = δ(s, v) untuk semua v terjangkau (memakai **path-relaxation property**: lintasan terpendek punya ≤ |V|−1 sisi).

#### 22.2 Lintasan Terpendek pada DAG

Pada **DAG**, relaksasi sisi dalam **urutan topologis** menyelesaikan persoalan dalam **Θ(V + E)** — bahkan dengan sisi berbobot negatif (tak mungkin ada siklus).

```text
DAG-SHORTEST-PATHS(G, w, s)
1  topological sort simpul G
2  INITIALIZE-SINGLE-SOURCE(G, s)
3  for setiap u dalam urutan topologis
4      for setiap v ∈ G.Adj[u]
5          RELAX(u, v, w)
```

Aplikasi: analisis **critical path** pada PERT chart (negasikan bobot atau ubah min→max).

#### 22.3 Algoritma Dijkstra

**Dijkstra** menyelesaikan single-source shortest paths bila **semua bobot non-negatif** (w(u,v) ≥ 0). Ia memelihara himpunan S simpul yang bobot terpendeknya sudah final, dan berulang memilih simpul u ∈ V−S dengan estimasi minimum (via **min-priority queue**), menambahkannya ke S, lalu merelaksasi sisi keluar u. Dijkstra dapat dipandang sebagai generalisasi BFS untuk graf berbobot.

```text
DIJKSTRA(G, w, s)
 1  INITIALIZE-SINGLE-SOURCE(G, s)
 2  S = ∅
 3  Q = ∅
 4  for setiap vertex u ∈ G.V
 5      INSERT(Q, u)
 6  while Q ≠ ∅
 7      u = EXTRACT-MIN(Q)
 8      S = S ∪ {u}
 9      for setiap vertex v ∈ G.Adj[u]
10          RELAX(u, v, w)
11          if relaksasi menurunkan v.d
12              DECREASE-KEY(Q, v, v.d)
```

**Analisis:** V kali INSERT + V kali EXTRACT-MIN + ≤ E kali DECREASE-KEY. Dengan **binary heap**, tiap operasi O(lg V) → **O((V + E) lg V)**. Dengan **Fibonacci heap** → O(V lg V + E). Dengan larik sederhana → O(V²) (baik untuk graf padat). Dijkstra **greedy** dan benar karena bobot non-negatif menjamin sekali simpul diekstrak, estimasinya sudah final.

| Algoritma | Bobot negatif? | Waktu | Struktur |
|---|---|---|---|
| DAG-Shortest-Paths | ya (DAG saja) | Θ(V+E) | urutan topologis |
| Bellman-Ford | ya (+ deteksi siklus neg.) | O(VE) | relaksasi semua sisi |
| Dijkstra (binary heap) | tidak | O((V+E) lg V) | min-priority queue |
| Dijkstra (Fibonacci heap) | tidak | O(V lg V + E) | min-priority queue |

### Istilah Kunci

- **Single-source shortest paths:** lintasan terpendek dari satu sumber ke semua simpul.
- **Relaxation (relaksasi):** memperbaiki estimasi v.d melalui sisi (u,v).
- **δ(s, v):** bobot lintasan terpendek aktual.
- **Bellman-Ford:** menangani bobot negatif, O(VE), deteksi siklus negatif.
- **Dijkstra:** bobot non-negatif, greedy, priority queue.
- **Negative-weight cycle (siklus berbobot negatif):** membuat lintasan terpendek tak terdefinisi.

### Contoh / Studi Kasus: Dijkstra

Graf 5-simpul (s,t,x,y,z) dengan bobot non-negatif. Dijkstra mengekstrak s (d=0), lalu simpul terdekat berikutnya, merelaksasi sisi keluar. Hasil akhir d memberi jarak terpendek; π membentuk pohon lintasan terpendek.

### Rangkuman

Semua algoritma lintasan terpendek berbasis relaksasi sisi; perbedaannya pada urutan dan asumsi bobot. DAG: urutan topologis, Θ(V+E). Bellman-Ford: |V|−1 lintasan relaksasi, O(VE), menangani bobot negatif dan mendeteksi siklus negatif. Dijkstra: greedy dengan priority queue, O((V+E) lg V), hanya untuk bobot non-negatif. Pemilihan algoritma bergantung pada ada/tidaknya bobot negatif dan kepadatan graf.

### Latihan & Soal

1. **(Tracing)** Jalankan Bellman-Ford pada graf 5-simpul; tunjukkan d dan π setelah tiap lintasan.
2. **(Tracing)** Jalankan Dijkstra dari sumber s pada graf berbobot non-negatif contoh.
3. **(Pemahaman)** Mengapa Dijkstra gagal pada bobot negatif? Berikan contoh tandingan.
4. **(Analisis/HOTS)** Buktikan path-relaxation property untuk Bellman-Ford.
5. **(HOTS)** Bagaimana memodifikasi Bellman-Ford agar menetapkan v.d = −∞ untuk simpul pada lintasan dengan siklus negatif?

---

## Bab 23 — Lintasan Terpendek Semua-Pasangan

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Merumuskan** persoalan all-pairs shortest paths (APSP).
2. **Mengimplementasikan** **Floyd-Warshall** berbasis pemrograman dinamis.
3. **Menganalisis** kompleksitas Θ(V³) dan ruang.
4. **Menjelaskan** algoritma **Johnson** untuk graf jarang.

### Peta Konsep

```
ALL-PAIRS SHORTEST PATHS
  +-- Matriks: ekstensi seperti perkalian matriks, Θ(V^3 lg V)
  +-- FLOYD-WARSHALL (DP atas simpul antara k) : Θ(V^3)
  +-- JOHNSON (reweighting + Dijkstra tiap simpul): O(V^2 lg V + VE), baik utk sparse
```

### Materi Inti

#### 23.2 Algoritma Floyd-Warshall

**Floyd-Warshall** menghitung lintasan terpendek antara **semua pasangan** simpul, menangani sisi berbobot negatif (tanpa siklus negatif). Berbasis **pemrograman dinamis** atas himpunan "simpul antara (intermediate vertices)".

Misalkan d⁽ᵏ⁾ᵢⱼ = bobot lintasan terpendek dari i ke j yang hanya boleh melewati simpul antara dari {1, …, k}. Rekurens:

> d⁽⁰⁾ᵢⱼ = wᵢⱼ;
> d⁽ᵏ⁾ᵢⱼ = min( d⁽ᵏ⁻¹⁾ᵢⱼ , d⁽ᵏ⁻¹⁾ᵢₖ + d⁽ᵏ⁻¹⁾ₖⱼ ).

Intuisi: untuk tiap pasangan (i, j), apakah memakai simpul k sebagai antara memperpendek lintasan?

```text
FLOYD-WARSHALL(W, n)
1  D⁽⁰⁾ = W
2  for k = 1 to n
3      misalkan D⁽ᵏ⁾ = (d⁽ᵏ⁾ᵢⱼ) matriks n×n baru
4      for i = 1 to n
5          for j = 1 to n
6              d⁽ᵏ⁾ᵢⱼ = min( d⁽ᵏ⁻¹⁾ᵢⱼ , d⁽ᵏ⁻¹⁾ᵢₖ + d⁽ᵏ⁻¹⁾ₖⱼ )
7  return D⁽ⁿ⁾
```

**Analisis:** tiga perulangan bersarang → **Θ(V³)** waktu, **Θ(V²)** ruang (matriks dapat di-*update in place* sehingga tak perlu n matriks). Matriks predecessor Π memungkinkan rekonstruksi lintasan.

#### 23.1 Pendekatan Perkalian Matriks

APSP juga dapat diselesaikan dengan ekstensi mirip **perkalian matriks** (operasi min-plus), menghasilkan **Θ(V³ lg V)** via pengulangan kuadrat (repeated squaring) — lebih lambat dari Floyd-Warshall tetapi instruktif secara konseptual.

#### 23.3 Algoritma Johnson untuk Graf Jarang

**Johnson** efisien untuk **graf jarang**: ia melakukan **reweighting (pembobotan ulang)** menggunakan Bellman-Ford satu kali (menghilangkan bobot negatif tanpa mengubah lintasan terpendek), lalu menjalankan **Dijkstra dari setiap simpul**. Total waktu **O(V² lg V + VE)** (dengan Fibonacci heap) — lebih baik daripada Θ(V³) bila E = o(V²).

| Algoritma | Bobot negatif | Waktu | Cocok untuk |
|---|---|---|---|
| Floyd-Warshall | ya (tanpa siklus neg.) | Θ(V³) | graf padat |
| Matriks (min-plus) | ya | Θ(V³ lg V) | konseptual |
| Johnson | ya (reweighting) | O(V² lg V + VE) | graf jarang |

### Istilah Kunci

- **All-pairs shortest paths (APSP):** lintasan terpendek semua pasangan.
- **Floyd-Warshall:** DP atas simpul antara; Θ(V³).
- **Intermediate vertex (simpul antara):** simpul yang boleh dilewati dalam d⁽ᵏ⁾.
- **Johnson's algorithm:** reweighting + Dijkstra per simpul; baik untuk graf jarang.
- **Reweighting:** transformasi bobot agar non-negatif tanpa mengubah lintasan terpendek.

### Contoh / Studi Kasus

Untuk graf 5-simpul dengan beberapa bobot negatif, Floyd-Warshall mengisi matriks D⁽⁰⁾ sampai D⁽⁵⁾. Pada iterasi k, tiap entri diperbarui bila lintasan via simpul k lebih pendek. Hasil D⁽⁵⁾ adalah matriks jarak terpendek antar semua pasangan.

### Rangkuman

APSP menghitung lintasan terpendek semua pasangan. Floyd-Warshall (DP atas simpul antara) memberi solusi elegan Θ(V³) yang menangani bobot negatif, ideal untuk graf padat. Johnson menggabungkan reweighting (Bellman-Ford) dan Dijkstra per simpul untuk efisiensi O(V² lg V + VE) pada graf jarang. Pemilihan bergantung pada kepadatan graf.

### Latihan & Soal

1. **(Tracing)** Jalankan Floyd-Warshall pada matriks bobot 4×4 contoh; tunjukkan D⁽ᵏ⁾ tiap iterasi.
2. **(Pemahaman)** Jelaskan makna d⁽ᵏ⁾ᵢⱼ dan rekurensnya.
3. **(Analisis/HOTS)** Buktikan Floyd-Warshall benar dengan induksi atas k.
4. **(Analisis)** Kapan Johnson lebih cepat daripada Floyd-Warshall? Buktikan dengan perbandingan asimtotik.
5. **(HOTS)** Bagaimana mendeteksi siklus berbobot negatif dari hasil Floyd-Warshall?

---

## Bab 24 — Aliran Maksimum (Maximum Flow)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Memodelkan** flow network dengan kapasitas, sumber, dan sink.
2. **Menyatakan** sifat aliran dan teorema **max-flow min-cut**.
3. **Mengimplementasikan** metode **Ford-Fulkerson** dan varian **Edmonds-Karp**.
4. **Menerapkan** max-flow untuk pencocokan bipartit maksimum.

### Peta Konsep

```
FLOW NETWORK G=(V,E), kapasitas c, sumber s, sink t
  +-- Residual network Gf, augmenting path
  +-- FORD-FULKERSON: cari augmenting path, tambah aliran
        +-- Edmonds-Karp (BFS) : O(V E^2)
  +-- Teorema MAX-FLOW MIN-CUT
  +-- Aplikasi: maximum bipartite matching
```

### Materi Inti

#### 24.1 Flow Network

**Flow network (jaringan aliran)** adalah graf berarah G = (V, E) dengan **kapasitas (capacity)** non-negatif c(u, v) ≥ 0 pada tiap sisi, sebuah **sumber (source)** s dan **sink (tujuan)** t. Sebuah **aliran (flow)** f memenuhi:

> 1. **Batas kapasitas (capacity constraint):** 0 ≤ f(u, v) ≤ c(u, v) untuk semua sisi.
> 2. **Konservasi aliran (flow conservation):** untuk setiap simpul selain s dan t, total aliran masuk = total aliran keluar.

**Nilai aliran** |f| adalah total aliran keluar dari s (= total masuk ke t). Persoalan **maximum flow** mencari aliran bernilai maksimum dari s ke t.

#### 24.2 Metode Ford-Fulkerson

**Ide:** Mulai dengan aliran nol; berulang cari **augmenting path (lintasan penambah)** — lintasan dari s ke t di **residual network (jaringan residual)** Gf yang masih punya kapasitas tersisa — lalu tambah aliran sepanjang lintasan itu sebesar kapasitas residual minimumnya. Ulangi sampai tak ada augmenting path.

```text
FORD-FULKERSON-METHOD(G, s, t)
1  inisialisasi aliran f = 0
2  while ada augmenting path p di residual network Gf
3      augmentasikan aliran f sepanjang p
4  return f
```

**Residual network Gf:** memuat sisi dengan kapasitas residual cf(u,v) = c(u,v) − f(u,v), termasuk **sisi balik (residual/back edge)** yang memungkinkan "membatalkan" aliran sebelumnya.

> **Teorema Max-Flow Min-Cut.** Nilai aliran maksimum sama dengan kapasitas **potongan minimum (minimum cut)** yang memisahkan s dan t. Tiga pernyataan ekuivalen: (1) f adalah aliran maksimum; (2) Gf tak punya augmenting path; (3) |f| = c(S, T) untuk suatu cut (S, T).

**Analisis:** Dengan kapasitas bilangan bulat dan nilai aliran maksimum |f*|, Ford-Fulkerson naif berjalan **O(E·|f*|)** (tiap augmentasi menambah aliran ≥ 1). Varian **Edmonds-Karp** memilih augmenting path **terpendek (jumlah sisi)** via **BFS**, menjamin **O(V·E²)** terlepas dari nilai kapasitas.

#### 24.3 Maximum Bipartite Matching

Persoalan **maximum bipartite matching** (mencari himpunan pasangan terbanyak antara dua kelompok) dapat **direduksi ke max-flow**: bangun jaringan dengan sumber s → semua simpul kiri, simpul kanan → sink t, dan tiap sisi berkapasitas 1. Nilai aliran maksimum = ukuran matching maksimum. Dengan Ford-Fulkerson berjalan **O(V·E)**.

### Istilah Kunci

- **Flow network:** graf berarah dengan kapasitas, sumber s, sink t.
- **Flow (aliran):** fungsi memenuhi batas kapasitas dan konservasi.
- **Residual network (Gf):** kapasitas tersisa + sisi balik.
- **Augmenting path:** lintasan s→t di Gf untuk menambah aliran.
- **Max-flow min-cut theorem:** aliran maksimum = kapasitas cut minimum.
- **Edmonds-Karp:** Ford-Fulkerson dengan BFS; O(VE²).

### Contoh / Studi Kasus

Jaringan dengan s, dua simpul antara, dan t, kapasitas sisi tertentu. Ford-Fulkerson menemukan augmenting path, menambah aliran sebesar bottleneck, lalu mengulang. Setelah tak ada augmenting path, nilai aliran = kapasitas min-cut.

### Rangkuman

Max-flow mencari aliran maksimum dari s ke t dalam jaringan berkapasitas. Metode Ford-Fulkerson berulang menemukan augmenting path di residual network; Edmonds-Karp (BFS) menjamin O(VE²). Teorema max-flow min-cut menghubungkan aliran maksimum dengan potongan minimum. Banyak persoalan (mis. bipartite matching) direduksi ke max-flow.

### Latihan & Soal

1. **(Pemahaman)** Sebutkan dua sifat yang harus dipenuhi sebuah aliran.
2. **(Tracing)** Jalankan Ford-Fulkerson pada jaringan contoh; tunjukkan residual network tiap augmentasi.
3. **(Analisis/HOTS)** Nyatakan dan jelaskan teorema max-flow min-cut.
4. **(Analisis)** Mengapa Edmonds-Karp berjalan O(VE²) terlepas dari nilai kapasitas?
5. **(HOTS)** Tunjukkan reduksi maximum bipartite matching ke max-flow dan analisis kompleksitasnya.

---

## Bab 25 — Pencocokan pada Graf Bipartit

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** matching dan maximum matching pada graf bipartit.
2. **Menjelaskan** algoritma berbasis augmenting path (revisit max-flow).
3. **Menerapkan** algoritma **stable marriage** (Gale-Shapley).
4. **Mengenali** algoritma **Hungarian** untuk persoalan penugasan (assignment).

### Peta Konsep

```
MATCHINGS pada graf bipartit
  +-- Maximum bipartite matching (via max-flow / augmenting path)
  +-- Stable matching: Gale-Shapley (deferred acceptance) -> O(n^2)
  +-- Assignment problem: Hungarian algorithm (min-cost matching)
```

### Materi Inti

#### 25.1 Maximum Bipartite Matching (Ditinjau Ulang)

**Matching** M pada graf adalah subset sisi tanpa simpul bersama. **Maximum matching** memaksimalkan |M|. Pada graf bipartit (simpul terbagi dua kelompok L dan R, sisi hanya antar kelompok), maximum matching dapat ditemukan via reduksi ke max-flow (Bab 24) atau langsung dengan pencarian **augmenting path** (lintasan berselang-seling antara sisi non-matching dan matching, dimulai dan diakhiri simpul tak terjodohkan). Kompleksitas dasar **O(V·E)**.

#### 25.2 Stable Marriage Problem

**Persoalan pernikahan stabil (stable marriage):** Diberikan n pria dan n wanita, masing-masing dengan **daftar preferensi** lengkap, cari pencocokan yang **stabil** — tidak ada pasangan (m, w) yang sama-sama lebih memilih satu sama lain daripada pasangan mereka saat ini (tidak ada *blocking pair*).

**Algoritma Gale-Shapley (deferred acceptance):** Setiap pria "melamar" ke wanita sesuai urutan preferensinya; wanita menerima lamaran terbaik sejauh ini secara sementara dan menolak yang lain. Proses berlanjut sampai semua terjodohkan.

```text
GALE-SHAPLEY (ringkas)
1  semua pria dan wanita bebas
2  while ada pria m yang bebas dan belum melamar semua wanita
3      w = wanita teratas dalam daftar m yang belum dilamar m
4      if w bebas: jodohkan (m, w)
5      elseif w lebih memilih m daripada pasangannya m':
6          jodohkan (m, w); m' menjadi bebas
7      else w menolak m
```

**Analisis:** **O(n²)** (tiap pria melamar paling banyak n wanita). Selalu menghasilkan matching stabil; versi pria-melamar bersifat *man-optimal*.

#### 25.3 Algoritma Hungarian untuk Assignment Problem

**Assignment problem (persoalan penugasan):** Cari **perfect matching berbobot minimum (atau maksimum)** pada graf bipartit berbobot lengkap — mis. menugaskan n pekerja ke n tugas dengan total biaya minimum. **Algoritma Hungarian** menyelesaikannya dalam waktu polinomial (umumnya **O(V³)**) menggunakan teknik dual/labeling.

### Istilah Kunci

- **Matching:** subset sisi tanpa simpul bersama.
- **Maximum matching:** matching berukuran terbesar.
- **Augmenting path (matching):** lintasan berselang yang memperbesar matching.
- **Stable matching / blocking pair:** matching tanpa pasangan yang saling lebih memilih.
- **Gale-Shapley:** algoritma deferred acceptance, O(n²).
- **Hungarian algorithm:** assignment berbobot minimum, O(V³).

### Contoh / Studi Kasus

Tiga pria {A,B,C} dan tiga wanita {X,Y,Z} dengan preferensi tertentu. Gale-Shapley (pria melamar) menghasilkan matching stabil dalam beberapa putaran lamaran/penolakan, dijamin tanpa blocking pair.

### Rangkuman

Pencocokan bipartit punya banyak varian: maximum matching (via max-flow/augmenting path, O(VE)), stable marriage (Gale-Shapley, O(n²), tanpa blocking pair), dan assignment berbobot (Hungarian, O(V³)). Konsep augmenting path adalah benang merah antara matching dan aliran maksimum.

### Latihan & Soal

1. **(Pemahaman)** Definisikan matching, maximum matching, dan augmenting path.
2. **(Tracing)** Jalankan Gale-Shapley pada instance preferensi 3×3.
3. **(Analisis/HOTS)** Buktikan Gale-Shapley selalu menghasilkan matching stabil.
4. **(Analisis)** Mengapa Gale-Shapley berjalan O(n²)?
5. **(HOTS)** Jelaskan hubungan augmenting path pada matching dengan augmenting path pada max-flow.

---

# BAGIAN VII — Topik Terpilih

## Pengantar Bagian VII

Bagian ini menyajikan topik lanjutan yang memperluas wawasan algoritmik ke berbagai domain: komputasi paralel, algoritma daring, aljabar linear komputasi, optimasi, pemrosesan sinyal (FFT), teori bilangan dan kriptografi, pencocokan string, machine learning, serta dua puncak teori kompleksitas — NP-completeness dan algoritma aproksimasi. Topik-topik ini menunjukkan keluasan dan kedalaman penerapan ide-ide algoritmik fundamental dari bagian sebelumnya.

---

## Bab 26 — Algoritma Paralel

### Tujuan Pembelajaran

1. **Menjelaskan** model **fork-join parallelism** dan platform multithreaded dinamis.
2. **Menghitung** ukuran kinerja: **work**, **span**, dan **parallelism**.
3. **Menganalisis** algoritma paralel (perkalian matriks, merge sort paralel).
4. **Menerapkan** hukum **work law** dan **span law**.

### Peta Konsep

```
PARALELISME fork-join
  +-- spawn / sync / parallel for
  +-- Work T1, Span T∞, Parallelism = T1/T∞
  +-- Speedup T1/Tp <= P, batas oleh span
```

### Materi Inti

**Fork-join parallelism** memodelkan komputasi paralel dengan primitif `spawn` (memunculkan subkomputasi yang dapat berjalan paralel), `sync` (menunggu subkomputasi selesai), dan `parallel for`. Komputasi dimodelkan sebagai DAG.

Dua ukuran kunci:
- **Work (T₁):** total waktu pada **satu** prosesor (jumlah semua operasi).
- **Span (T∞):** waktu pada prosesor **tak terbatas** (jalur kritis terpanjang dalam DAG).
- **Parallelism = T₁/T∞:** percepatan maksimum teoretis.

> **Work law:** Tₚ ≥ T₁/P (dengan P prosesor).
> **Span law:** Tₚ ≥ T∞.

**Speedup** = T₁/Tₚ ≤ P. Algoritma mencapai *linear speedup* bila T₁/Tₚ ≈ P. Contoh: **parallel merge sort** memiliki work Θ(n lg n) dan span Θ(lg³ n), memberikan parallelism tinggi. **Parallel matrix multiplication** memiliki work Θ(n³) dan span Θ(lg² n).

### Istilah Kunci
- **Work / Span / Parallelism:** T₁ / T∞ / T₁:T∞.
- **spawn / sync:** primitif fork-join.
- **Speedup:** percepatan T₁/Tₚ.

### Rangkuman
Algoritma paralel dianalisis lewat work (T₁) dan span (T∞); parallelism = T₁/T∞ membatasi percepatan. Fork-join (spawn/sync) adalah model umum. Merge sort dan perkalian matriks memiliki versi paralel dengan parallelism tinggi.

### Latihan & Soal
1. **(Pemahaman)** Definisikan work, span, dan parallelism.
2. **(Analisis)** Jika T₁ = 100 dan T∞ = 10, berapa parallelism dan speedup maksimum pada 8 prosesor?
3. **(HOTS)** Mengapa span menjadi batas bawah Tₚ berapa pun jumlah prosesor?

---

## Bab 27 — Algoritma Daring (Online Algorithms)

### Tujuan Pembelajaran

1. **Membedakan** algoritma **online** dan **offline**.
2. **Mendefinisikan** **competitive ratio** dan **competitive analysis**.
3. **Menganalisis** persoalan elevator, self-organizing list (move-to-front), dan online caching.

### Peta Konsep

```
ONLINE: keputusan tanpa tahu masa depan
  +-- Competitive ratio: COST_online <= c · COST_optimal + α
  +-- Move-to-front (list) : 4-competitive
  +-- Online caching (LRU) : k-competitive
```

### Materi Inti

**Algoritma online** harus membuat keputusan **tanpa mengetahui masukan masa depan** (berbeda dengan offline yang melihat seluruh masukan). Kualitasnya diukur dengan **competitive ratio**: algoritma online disebut **c-competitive** bila untuk setiap barisan masukan, biayanya ≤ c × biaya optimal offline (plus konstanta).

**Contoh:**
- **Self-organizing list (move-to-front, MTF):** setelah mengakses elemen, pindahkan ke depan list. MTF terbukti **4-competitive** terhadap strategi offline optimal (dianalisis dengan metode potensial — kaitan dengan Bab 16).
- **Online caching (paging):** strategi **LRU (Least Recently Used)** adalah **k-competitive** (k = ukuran cache). Tak ada algoritma online deterministik yang lebih baik dari k-competitive.

### Istilah Kunci
- **Online vs offline:** tanpa/dengan informasi masa depan.
- **Competitive ratio:** rasio biaya online terhadap optimal offline.
- **Move-to-front (MTF):** heuristik list, 4-competitive.
- **LRU:** strategi caching, k-competitive.

### Rangkuman
Algoritma online membuat keputusan irreversibel tanpa melihat masa depan; kualitasnya diukur dengan competitive ratio terhadap optimal offline. MTF (4-competitive) dan LRU (k-competitive) adalah contoh klasik, sering dianalisis dengan metode potensial.

### Latihan & Soal
1. **(Pemahaman)** Apa arti algoritma "c-competitive"?
2. **(Analisis/HOTS)** Jelaskan analisis potensial yang menunjukkan MTF 4-competitive.
3. **(HOTS)** Mengapa tak ada algoritma paging online deterministik yang lebih baik dari k-competitive?

---

## Bab 28 — Operasi Matriks

### Tujuan Pembelajaran

1. **Menyelesaikan** sistem persamaan linear via dekomposisi **LU/LUP**.
2. **Menjelaskan** inversi matriks dan hubungannya dengan perkalian matriks.
3. **Menerapkan** matriks **symmetric positive-definite** dan **least-squares approximation**.

### Peta Konsep

```
OPERASI MATRIKS
  +-- Solve Ax=b : LUP decomposition, forward/back substitution Θ(n^3)
  +-- Inversi matriks ~ kompleksitas perkalian matriks
  +-- SPD + least squares (regresi)
```

### Materi Inti

**Menyelesaikan sistem linear Ax = b:** dekomposisikan A = L·U (lower × upper triangular), atau **LUP** (P·A = L·U dengan pivoting untuk stabilitas numerik), lalu selesaikan dengan **forward substitution** (Ly = Pb) dan **back substitution** (Ux = y). Total **Θ(n³)**.

**Inversi matriks** dan **perkalian matriks** memiliki kompleksitas asimtotik yang **setara**: jika salah satu dapat dilakukan dalam O(nᶜ), maka begitu pula yang lain. Maka inversi juga dapat memanfaatkan Strassen.

**Least-squares approximation:** mencari x yang meminimalkan ‖Ax − b‖² (regresi linear), diselesaikan via **normal equations** AᵀA x = Aᵀb, di mana AᵀA bersifat **symmetric positive-definite (SPD)** sehingga dapat difaktorkan stabil (Cholesky).

### Istilah Kunci
- **LU / LUP decomposition:** faktorisasi segitiga (dengan pivoting).
- **Forward/back substitution:** menyelesaikan sistem segitiga.
- **Symmetric positive-definite (SPD):** matriks dengan sifat numerik baik.
- **Least squares:** aproksimasi minimum kuadrat (regresi).

### Rangkuman
Sistem linear diselesaikan via dekomposisi LUP + substitusi (Θ(n³)). Inversi setara perkalian matriks secara kompleksitas. Least-squares (regresi) memanfaatkan matriks SPD melalui normal equations.

### Latihan & Soal
1. **(Pemahaman)** Mengapa pivoting (LUP) diperlukan?
2. **(Analisis)** Tunjukkan inversi dan perkalian matriks setara secara asimtotik.
3. **(HOTS)** Turunkan normal equations untuk least squares.

---

## Bab 29 — Pemrograman Linear (Linear Programming)

### Tujuan Pembelajaran

1. **Memformulasikan** persoalan optimasi sebagai **linear program (LP)** bentuk standar/slack.
2. **Menjelaskan** algoritma **simplex** dan konsep **duality**.
3. **Memodelkan** persoalan (max-flow, shortest path) sebagai LP.

### Peta Konsep

```
LINEAR PROGRAMMING: optimalkan fungsi linear dengan kendala linear
  +-- Bentuk standar / slack form
  +-- SIMPLEX (eksponensial worst-case, cepat dalam praktik)
  +-- Duality: primal <-> dual
  +-- Polynomial: interior-point / ellipsoid
```

### Materi Inti

**Linear program (LP)** mengoptimalkan **fungsi objektif linear** terhadap sehimpunan **kendala linear** (persamaan/pertaksamaan). Bentuk standar: maksimalkan cᵀx terhadap Ax ≤ b, x ≥ 0.

**Algoritma simplex** bergerak dari satu **vertex** (titik sudut) daerah layak (polytope) ke vertex tetangga yang memperbaiki objektif, hingga optimum. Simplex **eksponensial pada kasus terburuk** tetapi **sangat cepat dalam praktik**. Algoritma **interior-point** dan **ellipsoid** menyelesaikan LP dalam **waktu polinomial**.

**Duality (kedualan):** setiap LP (primal) memiliki LP **dual** terkait; nilai optimum keduanya sama (**strong duality**). Banyak persoalan (max-flow, shortest path, matching) dapat dirumuskan sebagai LP, dan teorema seperti max-flow min-cut adalah manifestasi LP duality.

### Istilah Kunci
- **Linear program (LP):** optimasi linear dengan kendala linear.
- **Simplex:** algoritma vertex-to-vertex; eksponensial worst-case.
- **Duality:** korespondensi primal-dual; strong duality.
- **Feasible region (polytope):** himpunan solusi yang memenuhi kendala.

### Rangkuman
LP mengoptimalkan objektif linear di bawah kendala linear. Simplex efisien dalam praktik (eksponensial terburuk); interior-point/ellipsoid polinomial. Duality menyatukan banyak teorema optimasi, termasuk max-flow min-cut.

### Latihan & Soal
1. **(Pemahaman)** Tuliskan bentuk standar LP.
2. **(Analisis/HOTS)** Rumuskan single-source shortest path sebagai LP.
3. **(HOTS)** Jelaskan hubungan LP duality dengan teorema max-flow min-cut.

---

## Bab 30 — Polinomial dan FFT

### Tujuan Pembelajaran

1. **Membedakan** representasi polinomial **koefisien** dan **point-value**.
2. **Menjelaskan** **DFT (Discrete Fourier Transform)** dan algoritma **FFT (Fast Fourier Transform)**.
3. **Menganalisis** percepatan perkalian polinomial dari Θ(n²) menjadi Θ(n lg n).

### Peta Konsep

```
PERKALIAN POLINOMIAL
  +-- Representasi koefisien: perkalian (konvolusi) Θ(n^2)
  +-- Representasi point-value: perkalian Θ(n)
  +-- FFT: evaluasi di akar satuan ke-n (divide-and-conquer) Θ(n lg n)
        koefisien --FFT--> point-value --kalikan--> --IFFT--> koefisien
```

### Materi Inti

Polinomial dapat direpresentasikan dalam **koefisien** A(x) = ∑aₖxᵏ atau **point-value** {(x₀, y₀), …}. Perkalian polinomial (konvolusi) berjalan **Θ(n²)** dalam representasi koefisien, tetapi hanya **Θ(n)** dalam point-value.

**FFT** mempercepat konversi antar representasi dengan mengevaluasi polinomial pada **akar satuan ke-n (n-th roots of unity)** ω secara **divide-and-conquer**: pisahkan suku genap dan ganjil, evaluasi rekursif. Rekurens T(n) = 2T(n/2) + Θ(n) → **Θ(n lg n)**. Strategi perkalian polinomial:

> koefisien → **(FFT)** → point-value → **(kalikan titik demi titik, Θ(n))** → **(inverse FFT)** → koefisien.

Total **Θ(n lg n)**, jauh lebih cepat dari Θ(n²). FFT adalah salah satu algoritma paling berpengaruh (pemrosesan sinyal, perkalian bilangan besar, kompresi).

### Istilah Kunci
- **Coefficient / point-value representation:** dua representasi polinomial.
- **DFT / FFT:** transformasi Fourier diskret / cepat.
- **Roots of unity (akar satuan):** titik evaluasi ωⁿ = 1.
- **Convolution (konvolusi):** operasi yang setara perkalian polinomial.

### Contoh / Studi Kasus
Mengalikan dua polinomial berderajat n−1 secara naif butuh n² perkalian koefisien; dengan FFT (evaluasi di 2n akar satuan, kalikan, inverse) cukup Θ(n lg n).

### Rangkuman
FFT mengevaluasi polinomial di akar satuan secara divide-and-conquer (Θ(n lg n)), memungkinkan perkalian polinomial/konvolusi dalam Θ(n lg n) alih-alih Θ(n²). Strategi: FFT → kalikan point-value → inverse FFT.

### Latihan & Soal
1. **(Pemahaman)** Mengapa perkalian polinomial dalam representasi point-value hanya Θ(n)?
2. **(Tracing)** Hitung FFT untuk vektor koefisien berukuran 4.
3. **(Analisis/HOTS)** Turunkan rekurens FFT dan buktikan Θ(n lg n).

---

## Bab 31 — Algoritma Teori Bilangan

### Tujuan Pembelajaran

1. **Menerapkan** algoritma **Euclid** untuk GCD dan versi *extended*.
2. **Menghitung** aritmetika modular: eksponensiasi modular cepat.
3. **Menjelaskan** **kriptosistem kunci publik RSA** dan dasar teori bilangannya.
4. **Menjelaskan** uji keprimaan (primality testing) probabilistik.

### Peta Konsep

```
TEORI BILANGAN
  +-- EUCLID (GCD) : O(lg b) pembagian
  +-- Extended Euclid : gcd + koefisien Bézout
  +-- Modular exponentiation (square-and-multiply) : O(lg n) perkalian
  +-- RSA : kriptografi kunci publik
  +-- Primality testing (Miller-Rabin) : probabilistik
```

### Materi Inti

**Algoritma Euclid** menghitung **GCD (greatest common divisor)** berdasarkan gcd(a, b) = gcd(b, a mod b):

```text
EUCLID(a, b)
1  if b == 0
2      return a
3  else return EUCLID(b, a mod b)
```

Berjalan **O(lg b)** pemanggilan (kaitan dengan bilangan Fibonacci pada kasus terburuk). **Extended Euclid** juga menghasilkan koefisien Bézout (x, y) sehingga ax + by = gcd(a, b), penting untuk mencari **invers modular**.

**Eksponensiasi modular cepat (modular exponentiation)** menghitung aᵇ mod n dengan **square-and-multiply** dalam **O(lg b)** perkalian modular — esensial untuk RSA.

**RSA** adalah **kriptosistem kunci publik (public-key cryptosystem)** yang keamanannya bersandar pada kesulitan **memfaktorkan bilangan besar**. Kunci dibangun dari dua bilangan prima besar p, q; enkripsi/dekripsi adalah eksponensiasi modular. **Uji keprimaan Miller-Rabin** adalah algoritma **acak (Monte Carlo)** untuk menentukan keprimaan dengan probabilitas kesalahan yang dapat dibuat sangat kecil.

### Istilah Kunci
- **GCD / Euclid's algorithm:** pembagi persekutuan terbesar, O(lg b).
- **Extended Euclid:** menghasilkan koefisien Bézout dan invers modular.
- **Modular exponentiation:** aᵇ mod n via square-and-multiply, O(lg b).
- **RSA:** kriptografi kunci publik berbasis kesulitan faktorisasi.
- **Miller-Rabin:** uji keprimaan probabilistik.

### Rangkuman
Algoritma teori bilangan (Euclid GCD O(lg b), eksponensiasi modular O(lg b)) menopang kriptografi modern. RSA memanfaatkan kesulitan faktorisasi; Miller-Rabin menguji keprimaan secara probabilistik. Operasi-operasi ini bekerja pada bilangan besar (representasi multi-kata).

### Latihan & Soal
1. **(Tracing)** Hitung gcd(252, 198) dengan Euclid; tunjukkan tiap langkah.
2. **(Implementasi)** Tulis modular exponentiation square-and-multiply.
3. **(HOTS)** Jelaskan mengapa keamanan RSA bergantung pada kesulitan faktorisasi.

---

## Bab 32 — Pencocokan String (String Matching)

### Tujuan Pembelajaran

1. **Mendefinisikan** persoalan string matching (mencari kemunculan pola P dalam teks T).
2. **Menganalisis** algoritma naif, **Rabin-Karp**, automata berhingga, dan **KMP (Knuth-Morris-Pratt)**.
3. **Membandingkan** kompleksitas: naif O((n−m+1)m), KMP Θ(n+m).

### Peta Konsep

```
STRING MATCHING: cari pola P[1..m] dalam teks T[1..n]
  +-- Naive : O((n-m+1) m)
  +-- Rabin-Karp (hashing rolling) : rata-rata O(n+m), worst O((n-m+1)m)
  +-- Finite automaton : Θ(n) cocok + Θ(m|Σ|) preprocessing
  +-- KMP (fungsi prefiks) : Θ(n + m)
```

### Materi Inti

Persoalan **string matching**: temukan semua posisi pola P[1 : m] muncul dalam teks T[1 : n].

- **Naif (brute force):** coba tiap pergeseran; **O((n−m+1)·m)** terburuk.
- **Rabin-Karp:** gunakan **hashing** dengan *rolling hash* untuk membandingkan pola dengan substring secara cepat; rata-rata **O(n+m)**, terburuk O((n−m+1)m).
- **Finite automaton:** bangun automaton berhingga dari pola (preprocessing Θ(m·|Σ|)), lalu pindai teks dalam **Θ(n)**.
- **KMP (Knuth-Morris-Pratt):** hitung **fungsi prefiks (prefix function)** π yang menyatakan panjang prefiks-sekaligus-sufiks terpanjang, sehingga tidak perlu memundurkan pointer teks saat ketidakcocokan. Preprocessing Θ(m), pencocokan Θ(n) → total **Θ(n + m)**.

```text
KMP-MATCHER(T, P)  (ringkas)
1  π = COMPUTE-PREFIX-FUNCTION(P)
2  q = 0                          // jumlah karakter cocok sejauh ini
3  for i = 1 to n
4      while q > 0 and P[q+1] ≠ T[i]
5          q = π[q]               // mundur via fungsi prefiks (tanpa mundurkan i)
6      if P[q+1] == T[i]
7          q = q + 1
8      if q == m
9          laporkan kemunculan pada pergeseran i − m ; q = π[q]
```

### Istilah Kunci
- **String matching:** mencari pola dalam teks.
- **Rabin-Karp:** pencocokan berbasis rolling hash.
- **Prefix function (π):** prefiks yang sekaligus sufiks terpanjang; inti KMP.
- **Finite automaton matcher:** pemindaian teks dengan automaton pola.

### Contoh / Studi Kasus
Mencari P = "ababaca" dalam teks. Fungsi prefiks π pola memungkinkan KMP melompati perbandingan berulang, sehingga teks dipindai sekali dalam Θ(n).

### Rangkuman
String matching dapat dilakukan naif (O((n−m+1)m)), Rabin-Karp (rata-rata O(n+m)), automaton berhingga (Θ(n) + preprocessing), atau KMP yang menjamin Θ(n+m) lewat fungsi prefiks yang menghindari pemunduran pointer teks.

### Latihan & Soal
1. **(Tracing)** Hitung fungsi prefiks π untuk P = "ababaca".
2. **(Analisis)** Bandingkan kompleksitas naif vs KMP.
3. **(HOTS)** Jelaskan mengapa KMP tidak pernah memundurkan pointer teks i.

---

## Bab 33 — Algoritma Machine Learning

### Tujuan Pembelajaran

1. **Menjelaskan** algoritma **clustering** (mis. k-means).
2. **Menjelaskan** algoritma **multiplicative-weights**.
3. **Menerapkan** **gradient descent** untuk optimasi.

### Peta Konsep

```
MACHINE-LEARNING ALGORITHMS
  +-- Clustering (k-means) : minimalkan jarak intra-cluster
  +-- Multiplicative weights : pakar/expert, regret rendah
  +-- Gradient descent : minimalkan fungsi via langkah -∇f
```

### Materi Inti

**Clustering** mengelompokkan data ke kluster sehingga titik dalam satu kluster mirip. **k-means** berulang: (1) tetapkan tiap titik ke pusat (centroid) terdekat; (2) hitung ulang centroid sebagai rata-rata kluster. Konvergen ke minimum lokal fungsi objektif (jumlah kuadrat jarak).

**Algoritma multiplicative-weights** memelihara bobot atas sekumpulan "pakar/pilihan", menaikkan/menurunkan bobot berdasarkan kinerja, dan menjamin **regret** rendah relatif terhadap pakar terbaik — berguna dalam pembelajaran daring dan teori permainan.

**Gradient descent** meminimalkan fungsi terdiferensialkan f dengan bergerak ke arah **negatif gradien**: x ← x − η·∇f(x), dengan η laju pembelajaran (learning rate). Fondasi pelatihan model machine learning modern.

### Istilah Kunci
- **Clustering / k-means:** pengelompokan; iterasi assign–update.
- **Multiplicative weights:** pembaruan bobot multiplikatif; regret rendah.
- **Gradient descent:** optimasi via −∇f; learning rate η.

### Rangkuman
Bab ini menghubungkan algoritma dengan machine learning: k-means (clustering), multiplicative-weights (pembelajaran daring dengan jaminan regret), dan gradient descent (optimasi iteratif). Ketiganya mengandalkan prinsip iterasi dan optimasi yang dianalisis secara algoritmik.

### Latihan & Soal
1. **(Pemahaman)** Jelaskan dua langkah iterasi k-means.
2. **(Analisis)** Mengapa k-means hanya menjamin minimum lokal?
3. **(HOTS)** Bagaimana learning rate η memengaruhi konvergensi gradient descent?

---

## Bab 34 — NP-Completeness

### Tujuan Pembelajaran

1. **Mendefinisikan** kelas **P**, **NP**, dan **NP-complete**.
2. **Menjelaskan** **reducibility** (reduksi polinomial) dan peran teorema **Cook-Levin**.
3. **Membuktikan** NP-completeness suatu persoalan via reduksi.
4. **Mengenali** persoalan NP-complete kanonik (SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP, SUBSET-SUM).

### Peta Konsep

```
KOMPLEKSITAS
  P  = dapat DISELESAIKAN waktu polinomial
  NP = dapat DIVERIFIKASI waktu polinomial
  NP-complete = NP ∩ NP-hard (paling sulit dalam NP)
  +-- Reduksi polinomial: ≤p
  +-- Cook-Levin: SAT adalah NP-complete (pertama)
  +-- P =? NP (pertanyaan terbuka)
```

### Materi Inti

#### Kelas P dan NP

- **P (polynomial time):** kelas persoalan keputusan yang dapat **diselesaikan** oleh algoritma berwaktu polinomial O(nᵏ).
- **NP (nondeterministic polynomial time):** kelas persoalan yang **solusinya dapat diverifikasi** dalam waktu polinomial bila diberi "sertifikat (certificate)". Jelas P ⊆ NP.
- Pertanyaan **P = NP?** adalah salah satu masalah terbuka terbesar dalam ilmu komputer.

#### Reducibility

Persoalan A **dapat direduksi secara polinomial** ke B (ditulis A ≤ₚ B) bila ada fungsi berwaktu polinomial yang mengubah instance A menjadi instance B dengan jawaban yang sama. Bila A ≤ₚ B dan B mudah (∈ P), maka A mudah; sebaliknya bila A sulit, maka B sulit.

#### NP-Complete dan NP-Hard

> Persoalan B adalah **NP-hard** bila setiap persoalan A ∈ NP memenuhi A ≤ₚ B. Persoalan B adalah **NP-complete** bila B ∈ NP **dan** B NP-hard.

NP-complete adalah persoalan "tersulit" dalam NP: bila **satu saja** persoalan NP-complete dapat diselesaikan dalam waktu polinomial, maka **P = NP** dan semua persoalan NP dapat diselesaikan efisien.

> **Teorema Cook-Levin.** Persoalan **SAT (boolean satisfiability)** adalah NP-complete. Ini adalah persoalan NP-complete **pertama**, menjadi "akar" dari semua bukti NP-completeness berikutnya.

#### Strategi Bukti NP-Completeness

Untuk membuktikan persoalan X NP-complete: (1) tunjukkan X ∈ NP (ada verifikasi polinomial); (2) pilih persoalan NP-complete Y yang sudah diketahui; (3) konstruksi reduksi polinomial Y ≤ₚ X. Rantai reduksi historis: SAT → 3-CNF-SAT → CLIQUE → VERTEX-COVER → HAM-CYCLE → TSP, dan SUBSET-SUM.

| Persoalan | Deskripsi singkat |
|---|---|
| SAT / 3-CNF-SAT | apakah formula boolean dapat dipenuhi |
| CLIQUE | apakah ada klik berukuran k |
| VERTEX-COVER | apakah ada vertex cover berukuran k |
| HAM-CYCLE | apakah ada siklus Hamilton |
| TSP (decision) | apakah ada tur ≤ panjang k |
| SUBSET-SUM | apakah ada subset berjumlah target t |

### Istilah Kunci
- **P / NP:** dapat diselesaikan / diverifikasi dalam waktu polinomial.
- **Certificate (sertifikat):** bukti solusi yang diverifikasi cepat.
- **Polynomial reduction (≤ₚ):** transformasi polinomial antar persoalan.
- **NP-hard / NP-complete:** sekeras semua NP / NP-hard sekaligus ∈ NP.
- **Cook-Levin theorem:** SAT NP-complete pertama.

### Contoh / Studi Kasus
Membuktikan CLIQUE NP-complete: (1) CLIQUE ∈ NP (verifikasi himpunan k simpul saling terhubung dalam waktu polinomial); (2) reduksi 3-CNF-SAT ≤ₚ CLIQUE dengan membangun graf dari klausa. Reduksi ini menunjukkan jika CLIQUE mudah maka SAT mudah.

### Rangkuman
P adalah persoalan yang dapat diselesaikan polinomial; NP yang dapat diverifikasi polinomial. NP-complete adalah persoalan tersulit dalam NP: menyelesaikan satu efisien berarti P = NP. Teorema Cook-Levin menetapkan SAT sebagai NP-complete pertama; persoalan lain dibuktikan via reduksi polinomial. Mengenali NP-completeness mengarahkan kita ke pendekatan aproksimasi atau heuristik (Bab 35).

### Latihan & Soal
1. **(Pemahaman)** Bedakan P, NP, NP-hard, dan NP-complete.
2. **(Pemahaman)** Apa peran sertifikat dalam definisi NP?
3. **(Analisis/HOTS)** Uraikan langkah membuktikan suatu persoalan NP-complete.
4. **(HOTS)** Mengapa menyelesaikan satu persoalan NP-complete dalam waktu polinomial menyiratkan P = NP?
5. **(Analisis)** Berikan reduksi VERTEX-COVER ≤ₚ ... atau jelaskan reduksi 3-CNF-SAT ke CLIQUE.

---

## Bab 35 — Algoritma Aproksimasi

### Tujuan Pembelajaran

1. **Menjelaskan** motivasi algoritma aproksimasi untuk persoalan NP-hard.
2. **Mendefinisikan** **approximation ratio** ρ(n).
3. **Menganalisis** algoritma aproksimasi: vertex-cover (2-aproksimasi), TSP, set-cover, subset-sum.

### Peta Konsep

```
APPROXIMATION ALGORITHMS (untuk NP-hard)
  Approximation ratio ρ(n): C/C* (atau C*/C) <= ρ(n)
  +-- Vertex cover : 2-approximation
  +-- TSP (triangle inequality) : 2-approximation (MST-based)
  +-- Set cover : ln(n)-approximation (greedy)
  +-- Subset-sum : FPTAS (trimming)
```

### Materi Inti

Karena persoalan NP-hard tak punya algoritma eksak polinomial yang diketahui, **algoritma aproksimasi** menghasilkan solusi yang **dekat optimal** dalam waktu polinomial. Untuk persoalan minimisasi, algoritma adalah **ρ(n)-aproksimasi** bila biaya solusinya C memenuhi C/C* ≤ ρ(n), dengan C* biaya optimal (untuk maksimisasi, C*/C ≤ ρ(n)).

**Contoh-contoh:**

- **Vertex-cover (2-aproksimasi):** berulang ambil sebuah sisi yang belum tertutup, masukkan **kedua** ujungnya ke cover. Menghasilkan cover ≤ 2× optimal — **2-aproksimasi**.

```text
APPROX-VERTEX-COVER(G)
1  C = ∅
2  E' = G.E
3  while E' ≠ ∅
4      pilih sembarang sisi (u, v) ∈ E'
5      C = C ∪ {u, v}
6      hapus dari E' semua sisi yang menyentuh u atau v
7  return C
```

- **TSP dengan triangle inequality (2-aproksimasi):** bangun MST, lakukan preorder walk → tur ≤ 2× optimal.
- **Set-cover (ln n-aproksimasi):** greedy pilih himpunan yang menutup elemen tak tertutup terbanyak; rasio H(maks) ≈ ln n.
- **Subset-sum:** memiliki **FPTAS (fully polynomial-time approximation scheme)** — dapat mendekati optimum sedekat 1+ε yang diinginkan dengan waktu polinomial dalam n dan 1/ε, lewat teknik **trimming** daftar.

| Persoalan | Rasio aproksimasi |
|---|---|
| Vertex-cover | 2 |
| TSP (triangle inequality) | 2 |
| Set-cover (greedy) | H(n) ≈ ln n + 1 |
| Subset-sum | FPTAS (1+ε) |

### Istilah Kunci
- **Approximation algorithm:** solusi mendekati optimal dalam waktu polinomial.
- **Approximation ratio ρ(n):** jaminan kualitas relatif terhadap optimum.
- **2-approximation:** solusi ≤ 2× optimal.
- **PTAS / FPTAS:** skema aproksimasi (sepenuhnya) polinomial.

### Contoh / Studi Kasus
APPROX-VERTEX-COVER pada graf 7-simpul: tiap sisi terpilih menambahkan 2 simpul. Karena tiap sisi terpilih saling tak berbagi simpul (matching), optimum harus memuat ≥ 1 ujung tiap sisi tersebut, sehingga |C| ≤ 2·|C*|.

### Rangkuman
Untuk persoalan NP-hard, algoritma aproksimasi memberi solusi terjamin dekat optimal dalam waktu polinomial, diukur dengan approximation ratio. Contoh: vertex-cover dan metric-TSP (2-aproksimasi), set-cover (≈ln n), dan subset-sum (FPTAS). Ini adalah respons praktis terhadap ketidaktraktabilan (intractability) NP-hardness.

### Latihan & Soal
1. **(Pemahaman)** Definisikan approximation ratio untuk minimisasi dan maksimisasi.
2. **(Analisis/HOTS)** Buktikan APPROX-VERTEX-COVER adalah 2-aproksimasi.
3. **(Tracing)** Jalankan greedy set-cover pada instance kecil.
4. **(HOTS)** Jelaskan perbedaan PTAS dan FPTAS; mengapa subset-sum punya FPTAS?
5. **(Analisis)** Buktikan tur TSP berbasis MST ≤ 2× optimal dengan triangle inequality.

---

# BAGIAN VIII — Apendiks: Latar Belakang Matematis

## Pengantar Bagian VIII

Apendiks menyediakan fondasi matematis yang dipakai sepanjang buku. Materi ini bukan untuk dibaca berurutan, melainkan sebagai rujukan saat dibutuhkan: **penjumlahan (summations)** untuk analisis perulangan, **himpunan/relasi/fungsi/graf** sebagai bahasa formal, **pencacahan dan probabilitas** untuk analisis acak, serta **matriks** untuk algoritma aljabar linear.

---

## Apendiks A — Penjumlahan (Summations)

### Tujuan Pembelajaran
1. **Menghitung** penjumlahan deret umum (aritmetika, geometri, harmonik).
2. **Membatasi (bound)** penjumlahan dengan integral dan deret pembanding.

### Materi Inti

**Rumus penjumlahan penting:**

- **Deret aritmetika:** ∑ᵢ₌₁ⁿ i = n(n+1)/2 = Θ(n²).
- **Jumlah kuadrat:** ∑ᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6 = Θ(n³).
- **Deret geometri:** ∑ᵢ₌₀ⁿ xⁱ = (xⁿ⁺¹ − 1)/(x − 1) untuk x ≠ 1; bila |x| < 1, ∑ᵢ₌₀^∞ xⁱ = 1/(1−x).
- **Deret harmonik:** Hₙ = ∑ᵢ₌₁ⁿ 1/i = ln n + O(1) = Θ(lg n).

**Teknik membatasi penjumlahan:** (1) batas dengan deret geometri; (2) **integral approximation** — untuk f monoton, ∫f mendekati ∑f; (3) pemisahan suku dominan. Teknik ini muncul saat menganalisis BUILD-MAX-HEAP (∑ h/2ʰ = 2) dan quicksort (Hₙ).

### Latihan & Soal
1. Buktikan ∑i = n(n+1)/2 dengan induksi.
2. Tunjukkan ∑ᵢ₌₀^∞ i/2ⁱ = 2.
3. **(HOTS)** Batasi ∑ᵢ₌₁ⁿ lg i dan kaitkan dengan lg(n!).

---

## Apendiks B — Himpunan, Relasi, Fungsi, dan Graf

### Tujuan Pembelajaran
1. **Menggunakan** notasi himpunan, relasi, dan fungsi secara formal.
2. **Mendefinisikan** graf, pohon, dan terminologinya.

### Materi Inti

**Himpunan (set):** koleksi objek; operasi ∪ (gabungan), ∩ (irisan), − (selisih); himpunan kuasa 2^S; kardinalitas |S|. **Relasi (relation):** subset produk Cartesian; sifat refleksif, simetris, transitif; **relasi ekuivalensi** mempartisi himpunan. **Fungsi (function):** pemetaan; injektif (satu-satu), surjektif (onto), bijektif.

**Graf (graph):** G = (V, E) dengan V simpul dan E sisi. Graf **berarah (directed)/tak berarah (undirected)**; **derajat (degree)**; **lintasan (path)**, **siklus (cycle)**; graf **terhubung (connected)**. **Pohon (tree):** graf tak berarah terhubung tanpa siklus; pohon dengan n simpul punya tepat n−1 sisi. **Rooted tree:** pohon dengan satu simpul akar.

### Latihan & Soal
1. Buktikan pohon n simpul punya n−1 sisi.
2. Tunjukkan relasi "≡ mod m" adalah relasi ekuivalensi.
3. **(HOTS)** Berapa banyak fungsi bijektif dari himpunan n elemen ke dirinya?

---

## Apendiks C — Pencacahan dan Probabilitas

### Tujuan Pembelajaran
1. **Menghitung** permutasi dan kombinasi.
2. **Menerapkan** probabilitas dasar, variabel acak, dan nilai harapan.

### Materi Inti

**Pencacahan (counting):** aturan perkalian dan penjumlahan; **permutasi** n objek = n!; **kombinasi** C(n, k) = n!/(k!(n−k)!); **koefisien binomial** dan teorema binomial.

**Probabilitas:** ruang sampel, kejadian, Pr{A}; probabilitas bersyarat Pr{A|B}; **kejadian independen**. **Variabel acak (random variable)** dan **nilai harapan (expectation)** E[X] = ∑x·Pr{X=x}; **linearitas harapan** E[X+Y] = E[X]+E[Y]; **variabel indikator** (Bab 5). **Distribusi** Bernoulli, binomial, geometrik. Pertaksamaan **Markov** dan **Chebyshev** untuk membatasi ekor distribusi.

### Latihan & Soal
1. Hitung C(10, 3) dan jelaskan maknanya.
2. Buktikan linearitas harapan untuk dua variabel acak.
3. **(HOTS)** Dengan variabel indikator, hitung jumlah harapan titik tetap (fixed point) permutasi acak.

---

## Apendiks D — Matriks

### Tujuan Pembelajaran
1. **Melakukan** operasi matriks dasar (penjumlahan, perkalian, transpos, invers).
2. **Mengenali** matriks khusus (identitas, diagonal, SPD).

### Materi Inti

**Matriks (matrix)** adalah larik dua dimensi. Operasi: penjumlahan (elemen demi elemen), **perkalian** (C = AB dengan cᵢⱼ = ∑ₖ aᵢₖbₖⱼ, Θ(n³) naif), **transpos** Aᵀ, **invers** A⁻¹ (jika ada). Matriks khusus: **identitas** I, **diagonal**, **segitiga**, **symmetric** (A = Aᵀ), **positive-definite**. Sifat: perkalian matriks **asosiatif** tetapi **tidak komutatif** — sifat asosiatif inilah yang dieksploitasi matrix-chain multiplication (Bab 14).

### Latihan & Soal
1. Hitung perkalian dua matriks 2×2.
2. Buktikan (AB)ᵀ = BᵀAᵀ.
3. **(HOTS)** Tunjukkan perkalian matriks tidak komutatif dengan contoh tandingan.

---

# Bab Penutup: Sintesis dan Pemilihan Algoritma

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Memetakan** keterkaitan antar paradigma desain algoritma.
2. **Memilih** algoritma yang tepat berdasarkan karakteristik persoalan.
3. **Menempatkan** persoalan dalam lanskap kompleksitas (P, NP, NP-complete).
4. **Mensintesis** pengetahuan seluruh buku menjadi kerangka pengambilan keputusan.

## Peta Keterkaitan Teknik Desain

```
                      PERSOALAN
                          |
        +-----------------+------------------+
        |                 |                  |
   DIVIDE & CONQUER   DYNAMIC PROG.       GREEDY
   (subproblem        (subproblem         (pilihan lokal
    independen)        tumpang tindih +     optimal +
        |              optimal substr.)     greedy-choice)
   merge sort,        rod cutting,         activity sel.,
   quicksort,         matrix-chain,        Huffman,
   Strassen, FFT      LCS, Floyd-Warshall  Kruskal, Prim, Dijkstra
        |                 |                  |
        +-------- ANALISIS: rekurens, ------+
                  notasi asimtotik,
                  amortized analysis
```

## Perbandingan Paradigma

| Paradigma | Ciri persoalan | Contoh | Kekuatan |
|---|---|---|---|
| **Divide & Conquer** | subpersoalan independen | merge sort, quicksort, Strassen, FFT | rekursi bersih, mudah diparalelkan |
| **Dynamic Programming** | subpersoalan tumpang tindih + optimal substructure | rod cutting, LCS, matrix-chain, Floyd-Warshall | menghindari komputasi ulang |
| **Greedy** | greedy-choice property + optimal substructure | activity selection, Huffman, MST, Dijkstra | sederhana & cepat, butuh bukti |
| **Amortized** | barisan operasi struktur data | dynamic table, disjoint sets | biaya rata-rata realistis |

**Catatan penting:** beberapa algoritma graf adalah hibrida. Dijkstra dan Prim bersifat **greedy** tetapi memakai **priority queue**; Floyd-Warshall adalah **dynamic programming** atas graf; Bellman-Ford berbasis **relaksasi berulang** (mirip iterasi DP).

## Lanskap Kompleksitas: P vs NP

```
            SEMUA PERSOALAN
                  |
            +-----+------+
            |            |
        DAPAT DIPUTUSKAN  TAK DAPAT DIPUTUSKAN (halting problem)
            |
       +----+-----+
       |          |
       P      NP \ P (jika P ≠ NP)
   (tractable)    |
              NP-complete (tersulit dalam NP)
              -> gunakan: aproksimasi, heuristik,
                 parameter tetap, kasus khusus
```

- Jika persoalan ∈ **P**: cari algoritma polinomial terbaik (sering DP/greedy/graf).
- Jika persoalan **NP-complete**: jangan habiskan waktu mencari algoritma eksak polinomial. Gunakan **algoritma aproksimasi** (Bab 35), **heuristik**, **branch-and-bound**, **algoritma eksak eksponensial** untuk instance kecil, atau **eksploitasi struktur khusus** masukan.

## Kerangka Pemilihan Algoritma

Ketika menghadapi persoalan baru, tanyakan secara berurutan:

1. **Apa persoalannya secara formal?** (masukan, keluaran, kendala) — rumuskan presis.
2. **Apakah ada algoritma standar?** (pengurutan, pencarian, lintasan terpendek, MST, dsb.) — gunakan yang sudah terbukti.
3. **Berapa ukuran masukan tipikal?** — untuk n kecil, algoritma sederhana (insertion sort, brute force) bisa memadai; untuk n besar, laju pertumbuhan menentukan.
4. **Struktur data apa yang mendukung operasi yang dibutuhkan secara efisien?** (hash table, heap, BST seimbang, disjoint-set).
5. **Apakah persoalan ini NP-hard?** — jika ya, beralih ke aproksimasi/heuristik.
6. **Apakah ada karakteristik khusus** (bobot non-negatif → Dijkstra; DAG → urutan topologis; masukan hampir terurut → insertion sort) yang dapat dieksploitasi?
7. **Verifikasi kebenaran** (loop invariant, induksi) dan **analisis kompleksitas** (waktu & ruang) sebelum implementasi.

## Tabel Ringkasan Kompleksitas Master

| Persoalan / Algoritma | Waktu | Catatan |
|---|---|---|
| Insertion sort | Θ(n²) terburuk, Θ(n) terbaik | in place, stabil |
| Merge sort | Θ(n lg n) | stabil, ruang Θ(n) |
| Heapsort | Θ(n lg n) | in place |
| Quicksort | Θ(n lg n) harapan, Θ(n²) terburuk | cepat dalam praktik |
| Counting sort | Θ(n + k) | non-perbandingan, stabil |
| Radix sort | Θ(d(n + k)) | per digit |
| BST (seimbang) | O(lg n) per operasi | O(h) umum |
| Red-black tree | O(lg n) | tinggi terjamin |
| Hash table | O(1) rata-rata | terburuk Θ(n) |
| B-tree | O(log_t n) akses disk | penyimpanan sekunder |
| Disjoint sets | O(α(n)) teramortisasi | hampir konstan |
| BFS / DFS | Θ(V + E) | penelusuran graf |
| Topological sort | Θ(V + E) | DAG |
| Kruskal / Prim (MST) | O(E lg V) | greedy |
| Dijkstra (binary heap) | O((V+E) lg V) | bobot non-negatif |
| Bellman-Ford | O(VE) | bobot negatif, deteksi siklus |
| Floyd-Warshall | Θ(V³) | semua pasangan |
| Ford-Fulkerson / Edmonds-Karp | O(VE²) | max-flow |
| Strassen | Θ(n^2.81) | perkalian matriks |
| FFT | Θ(n lg n) | perkalian polinomial |
| KMP | Θ(n + m) | string matching |

## Rangkuman Penutup

Buku ini telah membangun perjalanan dari fondasi (algoritma, model RAM, notasi asimtotik) menuju paradigma desain (divide-and-conquer, DP, greedy, amortized), beragam struktur data (heap, hash, BST, RB-tree, B-tree, disjoint-set), algoritma graf yang kaya, dan akhirnya ke teori kompleksitas (P, NP, NP-complete) beserta respons praktisnya (aproksimasi). Benang merahnya: **rumuskan persoalan dengan presisi, pilih teknik yang sesuai struktur persoalan, buktikan kebenaran, dan analisis efisiensi**. Algoritma adalah teknologi; penguasaannya membekali kita memecahkan persoalan komputasi secara elegan dan efisien.

---

# Glosarium (EN → ID)

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Algorithm** | Algoritma: prosedur komputasi terdefinisi baik yang mengubah masukan menjadi keluaran dalam langkah berhingga. |
| **Amortized analysis** | Analisis teramortisasi: biaya rata-rata per operasi atas barisan operasi kasus terburuk. |
| **Approximation ratio** | Rasio aproksimasi: jaminan kedekatan solusi aproksimasi terhadap optimum. |
| **Asymptotic notation** | Notasi asimtotik: O, Ω, Θ untuk laju pertumbuhan fungsi. |
| **Augmenting path** | Lintasan penambah: lintasan yang memperbesar aliran (max-flow) atau matching. |
| **Binary search tree (BST)** | Pohon pencarian biner: pohon biner dengan properti urutan kiri ≤ x ≤ kanan. |
| **Breadth-first search (BFS)** | Penelusuran melebar: menjelajah graf lapisan demi lapisan via queue. |
| **B-tree** | Pohon pencarian seimbang berderajat tinggi untuk penyimpanan sekunder. |
| **Competitive ratio** | Rasio kompetitif: ukuran kualitas algoritma online terhadap optimal offline. |
| **Comparison sort** | Pengurutan berbasis perbandingan; batas bawah Ω(n lg n). |
| **Counting sort** | Pengurutan dengan menghitung kemunculan; Θ(n+k), stabil. |
| **Cut (graph)** | Potongan: partisi simpul graf; light edge adalah sisi termurah yang melintasinya. |
| **Decision tree** | Pohon keputusan: model untuk batas bawah comparison sort. |
| **Depth-first search (DFS)** | Penelusuran mendalam: menjelajah sedalam mungkin sebelum mundur; timestamp d/f. |
| **Disjoint sets (union-find)** | Himpunan terpisah: MAKE-SET, UNION, FIND-SET; O(α(n)) teramortisasi. |
| **Divide-and-conquer** | Bagi-dan-taklukkan: bagi, taklukkan rekursif, gabung. |
| **Dynamic programming (DP)** | Pemrograman dinamis: optimasi via subpersoalan tumpang tindih + substruktur optimal. |
| **Dijkstra's algorithm** | Lintasan terpendek sumber-tunggal, bobot non-negatif, greedy + priority queue. |
| **Edge classification** | Klasifikasi sisi DFS: tree, back, forward, cross. |
| **Expected running time** | Waktu harapan: ekspektasi waktu atas keacakan algoritma. |
| **FFT (Fast Fourier Transform)** | Transformasi Fourier cepat; perkalian polinomial Θ(n lg n). |
| **Floyd-Warshall** | Lintasan terpendek semua-pasangan via DP; Θ(V³). |
| **Flow network** | Jaringan aliran: graf berarah dengan kapasitas, sumber, sink. |
| **Greedy algorithm** | Algoritma serakah: memilih optimum lokal tiap langkah. |
| **Hash table** | Tabel hash: pemetaan kunci→slot; rata-rata O(1). |
| **Heap (binary heap)** | Larik merepresentasikan pohon biner hampir lengkap; max/min-heap. |
| **Heapsort** | Pengurutan in place berbasis heap; Θ(n lg n). |
| **In place** | Di tempat: memerlukan memori tambahan konstan. |
| **Insertion sort** | Pengurutan incremental; Θ(n²) terburuk, stabil. |
| **Knuth-Morris-Pratt (KMP)** | Pencocokan string Θ(n+m) via fungsi prefiks. |
| **Loop invariant** | Invarian perulangan: pernyataan benar pada awal tiap iterasi; alat bukti kebenaran. |
| **Master theorem** | Teorema master: resep menyelesaikan T(n)=aT(n/b)+f(n). |
| **Matching** | Pencocokan: subset sisi tanpa simpul bersama. |
| **Maximum flow** | Aliran maksimum: nilai aliran terbesar dari s ke t. |
| **Merge sort** | Pengurutan divide-and-conquer; Θ(n lg n), stabil. |
| **Minimum spanning tree (MST)** | Pohon merentang berbobot minimum. |
| **NP-complete** | Persoalan tersulit dalam NP; ∈ NP dan NP-hard. |
| **Order statistic** | Statistik terurut: elemen ke-i terkecil. |
| **Pivot** | Elemen acuan partisi dalam quicksort. |
| **Priority queue** | Antrian prioritas: INSERT/EXTRACT-MIN(MAX) berbasis kunci. |
| **Quicksort** | Pengurutan divide-and-conquer berbasis partisi; harapan Θ(n lg n). |
| **RAM model** | Model komputasi sekuensial dengan operasi dasar berbiaya konstan. |
| **Randomized algorithm** | Algoritma acak: membuat pilihan acak internal. |
| **Recurrence** | Rekurens: persamaan T(n) dalam bentuk T pada masukan lebih kecil. |
| **Red-black tree** | BST berwarna dengan 5 properti; tinggi O(lg n). |
| **Relaxation** | Relaksasi: memperbaiki estimasi jarak v.d melalui sisi. |
| **Rotation** | Rotasi: restrukturisasi lokal O(1) pada BST. |
| **Topological sort** | Pengurutan topologis DAG; Θ(V+E). |
| **Vertex cover** | Vertex cover: himpunan simpul yang menutup semua sisi. |

---

# Daftar Pustaka

## Sumber Utama

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). Cambridge, Massachusetts: The MIT Press. ISBN 9780262046305. (LCCN 2021037260). — **Buku sumber tunggal yang menjadi dasar seluruh buku ajar ini.**

## Algoritma, Teorema, dan Konsep Bernama (sebagaimana dirujuk dalam buku sumber)

Daftar berikut mencantumkan algoritma dan hasil bernama yang dibahas dalam buku ajar ini beserta tokoh yang terkait, sebagaimana disajikan dalam *Introduction to Algorithms* Edisi Keempat:

- **Master Theorem** (Teorema Master) — metode penyelesaian rekurens divide-and-conquer (Bab 4 buku sumber).
- **Strassen's Algorithm** — Volker Strassen, perkalian matriks Θ(n^lg7).
- **Akra-Bazzi method** — Mohamad Akra & Louay Bazzi, generalisasi rekurens.
- **Huffman Coding** — David A. Huffman, kode prefiks optimal.
- **Kruskal's Algorithm** — Joseph Kruskal, minimum spanning tree.
- **Prim's Algorithm** — Robert C. Prim (dan Vojtěch Jarník), minimum spanning tree.
- **Dijkstra's Algorithm** — Edsger W. Dijkstra, lintasan terpendek sumber-tunggal (bobot non-negatif).
- **Bellman-Ford Algorithm** — Richard Bellman & Lester Ford Jr., lintasan terpendek dengan bobot negatif.
- **Floyd-Warshall Algorithm** — Robert Floyd & Stephen Warshall, lintasan terpendek semua-pasangan.
- **Johnson's Algorithm** — Donald B. Johnson, lintasan terpendek semua-pasangan untuk graf jarang.
- **Ford-Fulkerson Method** — Lester Ford Jr. & Delbert Fulkerson, aliran maksimum.
- **Edmonds-Karp Algorithm** — Jack Edmonds & Richard Karp, varian Ford-Fulkerson berbasis BFS.
- **Max-Flow Min-Cut Theorem** — teorema dualitas aliran maksimum/potongan minimum.
- **Gale-Shapley Algorithm** — David Gale & Lloyd Shapley, pencocokan stabil (deferred acceptance).
- **Hungarian Algorithm** — Harold Kuhn (berdasarkan karya Kőnig & Egerváry), persoalan penugasan.
- **Rabin-Karp Algorithm** — Michael O. Rabin & Richard Karp, pencocokan string berbasis hashing.
- **Knuth-Morris-Pratt (KMP) Algorithm** — Donald Knuth, James Morris, & Vaughan Pratt, pencocokan string Θ(n+m).
- **Fast Fourier Transform (FFT)** — dipopulerkan oleh James Cooley & John Tukey, transformasi Fourier diskret cepat.
- **RSA Cryptosystem** — Ron Rivest, Adi Shamir, & Leonard Adleman, kriptografi kunci publik.
- **Miller-Rabin Primality Test** — Gary Miller & Michael Rabin, uji keprimaan probabilistik.
- **Euclid's Algorithm** — Euclid, perhitungan greatest common divisor (GCD).
- **Cook-Levin Theorem** — Stephen Cook & Leonid Levin, SAT adalah NP-complete (persoalan NP-complete pertama).
- **Stirling's Approximation** — James Stirling, aproksimasi n!.

> **Catatan keterbacaan dan kepatuhan:** Seluruh penjelasan, definisi, pseudocode, dan analisis dalam buku ajar ini ditulis ulang dalam Bahasa Indonesia akademik dan diparafrasekan dari materi pada buku sumber; nama algoritma, istilah teknis, dan pseudocode keyword dipertahankan dalam Bahasa Inggris sesuai konvensi keilmuan. Penomoran teorema dan hasil kompleksitas mengikuti fakta algoritmik yang mapan dalam buku sumber. Konten disusun ulang untuk kepatuhan terhadap ketentuan lisensi.

---

*Akhir Buku Ajar — "Pengantar Algoritma: Buku Ajar Berbasis CLRS Edisi Keempat".*
