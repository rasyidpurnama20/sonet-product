# Buku Ajar: Manajemen Informasi Pribadi (Personal Information Management)

### Ilmu Mengelola "Barang-Barang Digital" Kita: Perspektif Kurasi, Folder Hierarkis, dan Pendekatan User-Subjective

---

**Buku ajar ini disusun berdasarkan buku sumber:**

> Bergman, O., & Whittaker, S. (2016). *The Science of Managing Our Digital Stuff*. Cambridge, MA: The MIT Press. ISBN 9780262035170. LCCN 2016015017.

- **Disiplin:** Interaksi Manusia–Komputer (Human–Computer Interaction/HCI), Ilmu Informasi, Psikologi Kognitif Terapan
- **Jenjang:** Sarjana (S1) tahun akhir dan Pascasarjana (S2) — program studi Informatika, Sistem Informasi, Ilmu Perpustakaan dan Informasi, serta Psikologi Kognitif
- **Edisi buku ajar:** Edisi 1
- **Tahun penyusunan:** 2024
- **Bahasa pengantar:** Bahasa Indonesia (istilah teknis disertai padanan/penjelasan)

> **Catatan penting tentang sumber dan keaslian.** Seluruh klaim, angka, persentase, dan temuan penelitian yang dirujuk dalam buku ajar ini berasal dari teks buku sumber Bergman & Whittaker (2016). Penulis buku ajar tidak menambahkan angka atau hasil studi baru. Bagian yang merupakan **elaborasi pedagogis** (analogi, studi kasus dalam konteks Indonesia, latihan) ditandai secara eksplisit agar pembaca dapat membedakan klaim para penulis asli dari pengayaan didaktis.

---

## Kata Pengantar

Setiap hari, jutaan orang menyimpan, menamai, memindahkan, mencari, dan kadang menghapus berkas (file), surel (email), foto, serta tautan (bookmark) di komputer, ponsel, dan layanan awan (cloud) mereka. Aktivitas yang tampak remeh ini sebenarnya adalah salah satu kegiatan paling fundamental dalam kehidupan digital modern. Namun, dibandingkan dengan riset tentang pencarian informasi publik di internet, kajian ilmiah tentang bagaimana individu mengelola **informasi pribadi**-nya sendiri masih relatif sedikit. Buku *The Science of Managing Our Digital Stuff* karya Ofer Bergman dan Steve Whittaker (MIT Press, 2016) hadir untuk mengisi kekosongan tersebut. Buku itu merangkum hampir dua dekade penelitian kedua penulis tentang **Personal Information Management (PIM)** — Manajemen Informasi Pribadi.

Buku ajar ini disusun untuk menerjemahkan, menstrukturkan, dan memperdalam gagasan-gagasan inti buku sumber tersebut ke dalam Bahasa Indonesia akademik, sehingga dapat digunakan sebagai bahan kuliah satu semester. Buku sumber bukanlah buku "tips dan trik" untuk merapikan komputer; ia adalah karya ilmiah yang membangun **landasan teoretis** bagi PIM sebagai bidang kajian yang berbeda dari manajemen informasi publik. Oleh karena itu, buku ajar ini pun mempertahankan karakter ilmiahnya: setiap bab berakar pada studi empiris yang dilaporkan dalam teks sumber.

**Untuk siapa buku ajar ini?**

- **Mahasiswa** Informatika, Sistem Informasi, dan Ilmu Perpustakaan & Informasi yang mempelajari Interaksi Manusia–Komputer, desain antarmuka, atau perilaku informasi.
- **Mahasiswa Psikologi Kognitif** yang tertarik pada penerapan teori memori, atensi, dan pengambilan keputusan pada teknologi sehari-hari.
- **Dosen dan peneliti** yang membutuhkan bahan ajar terstruktur tentang PIM.
- **Praktisi** perancang sistem (desainer UX, pengembang perangkat lunak) yang ingin memahami mengapa pengguna berperilaku seperti yang mereka lakukan terhadap data pribadi.

**Bagaimana menggunakan buku ajar ini?**

Buku ajar ini mengikuti struktur tiga bagian buku sumber. Setiap bab dirancang dengan komponen pembelajaran yang konsisten:

1. **Tujuan Pembelajaran** — sasaran terukur menggunakan kata kerja Taksonomi Bloom.
2. **Peta Konsep** — gambaran ringkas keterkaitan ide dalam bab.
3. **Materi Inti** — penjelasan mendalam berbasis teks sumber, dengan definisi istilah dan analogi.
4. **Istilah Kunci** — daftar istilah Inggris beserta penjelasan Indonesia.
5. **Contoh / Studi Kasus** — diadaptasi ke konteks Indonesia (mahasiswa, dosen, pekerja kantoran).
6. **Temuan Penelitian** — hasil studi yang dilaporkan dalam buku sumber.
7. **Rangkuman** — poin-poin utama.
8. **Latihan & Refleksi** — pertanyaan pemahaman, soal analisis tingkat tinggi (HOTS), dan tugas praktik.

Disarankan agar pembaca mengerjakan bagian Latihan & Refleksi sebelum melanjutkan ke bab berikutnya, karena banyak konsep yang bersifat kumulatif. Bagian Glosarium dan Daftar Pustaka di akhir buku dapat digunakan sebagai rujukan cepat.

Selamat belajar. Semoga buku ajar ini membantu Anda memandang aktivitas sehari-hari "merapikan barang digital" dengan kacamata ilmiah yang baru.

---

## Daftar Isi

- [Kata Pengantar](#kata-pengantar)
- [Bab Pendahuluan: Memetakan Manajemen Informasi Pribadi (PIM)](#bab-pendahuluan-memetakan-manajemen-informasi-pribadi-pim)

**BAGIAN I — Manajemen Informasi Pribadi: Perspektif Kurasi**

- [Pengantar Bagian I](#pengantar-bagian-i)
- [Bab 1 — Arsip Pribadi dan Proses Kurasi](#bab-1--arsip-pribadi-dan-proses-kurasi)
- [Bab 2 — Penyimpanan (Keeping)](#bab-2--penyimpanan-keeping)
- [Bab 3 — Pengelolaan (Management)](#bab-3--pengelolaan-management)
- [Bab 4 — Pemanfaatan (Exploitation)](#bab-4--pemanfaatan-exploitation)
- [Rangkuman Bagian I](#rangkuman-bagian-i)

**BAGIAN II — Folder Hierarkis dan Alternatifnya**

- [Pengantar Bagian II](#pengantar-bagian-ii)
- [Bab 5 — Alternatif Pencarian (The Search Alternative)](#bab-5--alternatif-pencarian-the-search-alternative)
- [Bab 6 — Alternatif Penandaan (The Tagging Alternative)](#bab-6--alternatif-penandaan-the-tagging-alternative)
- [Bab 7 — Alternatif Pengelolaan Kelompok (The Group Management Alternative)](#bab-7--alternatif-pengelolaan-kelompok-the-group-management-alternative)
- [Bab 8 — Mengapa Navigasi adalah Metode Pengambilan PIM yang Disukai?](#bab-8--mengapa-navigasi-adalah-metode-pengambilan-pim-yang-disukai)
- [Rangkuman Bagian II](#rangkuman-bagian-ii)

**BAGIAN III — Pendekatan User-Subjective dalam Desain Sistem PIM**

- [Pengantar Bagian III](#pengantar-bagian-iii)
- [Bab 9 — Pendekatan User-Subjective](#bab-9--pendekatan-user-subjective)
- [Bab 10 — Prinsip Subjective Importance (Kepentingan Subjektif)](#bab-10--prinsip-subjective-importance-kepentingan-subjektif)
- [Bab 11 — Prinsip Subjective Project Classification (Klasifikasi Proyek Subjektif)](#bab-11--prinsip-subjective-project-classification-klasifikasi-proyek-subjektif)
- [Bab 12 — Prinsip Subjective Context (Konteks Subjektif)](#bab-12--prinsip-subjective-context-konteks-subjektif)
- [Rangkuman Bagian III](#rangkuman-bagian-iii)

**Penutup dan Rujukan**

- [Bab Penutup: Sintesis, Kesimpulan, dan Implikasi untuk Pembaca Indonesia](#bab-penutup-sintesis-kesimpulan-dan-implikasi-untuk-pembaca-indonesia)
- [Glosarium](#glosarium)
- [Daftar Pustaka](#daftar-pustaka)

**Lampiran (Perangkat Pembelajaran)**

- [Lampiran A — Rencana Pembelajaran Semester (RPS)](#lampiran-a--rencana-pembelajaran-semester-rps)
- [Lampiran B — Tabel Induk Temuan Kuantitatif Lintas-Bab](#lampiran-b--tabel-induk-temuan-kuantitatif-lintas-bab)
- [Lampiran C — Bank Soal Ujian (UTS & UAS)](#lampiran-c--bank-soal-ujian-uts--uas)
- [Lampiran D — Rubrik Penilaian Tugas Praktik](#lampiran-d--rubrik-penilaian-tugas-praktik)
- [Lampiran E — Proyek Akhir Semester: Studi Mini Kurasi Pribadi](#lampiran-e--proyek-akhir-semester-studi-mini-kurasi-pribadi)

---

## Bab Pendahuluan: Memetakan Manajemen Informasi Pribadi (PIM)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** Personal Information Management (PIM) dan menyebutkan jenis-jenis butir informasi yang termasuk di dalamnya.
2. **Menjelaskan** mengapa PIM secara fundamental berbeda dari manajemen informasi publik.
3. **Menguraikan** tiga proses kurasi (keeping, management, exploitation) beserta keterkaitannya.
4. **Mengidentifikasi** struktur tiga bagian buku sumber dan tesis utama masing-masing bagian.
5. **Membedakan** pandangan "manusia sebagai konsumen informasi" dari pandangan "manusia sebagai kurator informasi".

### Peta Konsep

```
                 MANAJEMEN INFORMASI PRIBADI (PIM)
                              |
        "Aktivitas individu menyimpan butir informasi pribadi
                untuk diambil kembali di kemudian hari"
                              |
        +---------------------+----------------------+
        |                     |                      |
   Bagian I              Bagian II              Bagian III
  Perspektif         Folder Hierarkis        Pendekatan
   Kurasi             vs Alternatif         User-Subjective
        |                     |                      |
   3 proses kurasi:    Search / Tag / GIM     3 prinsip desain:
   - Keeping           vs Navigasi Folder     - Importance
   - Management        (folder tetap unggul)  - Project
   - Exploitation                             - Context
```

### Materi Inti

#### 1. Apa itu PIM?

Buku sumber membuka pembahasannya dengan sebuah definisi yang ringkas namun padat. *Personal Information Management* (PIM) — Manajemen Informasi Pribadi — adalah **aktivitas seorang individu menyimpan butir-butir informasi pribadi (personal information items) agar dapat diambil kembali di kemudian hari**. Aktivitas ini dapat berlangsung di lingkungan fisik (misalnya kantor), pada perangkat bergerak (mobile devices) seperti ponsel dan tablet, maupun pada komputer pribadi.

Pada komputer pribadi, yang dimaksud dengan "butir informasi" (information items) mencakup:

- **Dokumen** (documents) — berkas teks, lembar kerja (spreadsheets), presentasi.
- **Surel** (email) — pesan yang dikirim dan diterima.
- **Favorit web / penanda** (web favorites / bookmarks) — tautan ke halaman web.
- **Tugas** (tasks) — daftar pekerjaan.
- **Kontak** (contacts) — informasi orang.

Bergman & Whittaker menegaskan satu paradoks penting: meskipun PIM adalah aspek fundamental dari aktivitas berbasis komputer — dilakukan jutaan pengguna beberapa kali sehari — riset tentangnya secara mengejutkan masih sangat sedikit. Baru dalam beberapa tahun terakhir topik ini menarik perhatian ilmiah yang semakin besar.

> **Elaborasi pedagogis.** Bayangkan PIM seperti aktivitas seorang petani yang tidak hanya mencari makanan setiap hari (foraging), tetapi juga **menyimpan benih, menata lumbung, dan mengambil hasil panen** saat dibutuhkan. Buku sumber sendiri menggunakan analogi pertanian: praktik bercocok tanam memungkinkan nenek moyang kita mengolah sumber pangan untuk kebutuhan masa depan, alih-alih bergantung pada hasil pencarian yang tidak menentu. PIM adalah "pertanian informasi" untuk diri kita di masa depan.

#### 2. Tesis Utama Buku Sumber

Tema sentral buku sumber adalah: **PIM secara fundamental berbeda dari jenis manajemen informasi lainnya**, dan tujuannya adalah menyediakan landasan ilmiah bagi bidang baru ini. Ketiga bagian buku menopang tesis ini:

- **Bagian I** berargumen bahwa teori-teori informasi modern keliru dalam menempatkan tekanannya, karena fokus mereka hanya pada **penemuan informasi (information discovery) dalam data publik**. Buku ini mengangkat pentingnya **data pribadi** dan mengajukan **kurasi (curation)** sebagai model alternatif untuk PIM. Kurasi didefinisikan sebagai model tiga tahap: **keeping (penyimpanan), management (pengelolaan), dan exploitation (pemanfaatan)**.

- **Bagian II** menunjukkan bahwa teknologi yang berfungsi baik untuk bidang manajemen informasi lain justru **gagal untuk PIM**. Para penulis memeriksa metode **folder hierarkis (hierarchical folder)** yang kini mendominasi PIM dan membandingkannya dengan tiga alternatif yang diusulkan: cari-semuanya (search everything), tandai-semuanya (tag everything), dan organisasi kelompok (group organization). Berbagai studi menunjukkan bahwa metode-metode alternatif ini, yang berfungsi baik di web, justru kurang diadopsi untuk PIM — pengguna lebih memilih mengorganisasi dan menavigasi data pribadi secara manual.

- **Bagian III** memperkenalkan **pendekatan user-subjective (user-subjective approach)** untuk desain sistem PIM. Pendekatan ini memanfaatkan fakta bahwa dalam PIM, **orang yang mengorganisasi informasi adalah orang yang sama yang kelak mengambilnya kembali**. Karena itu, sistem PIM sebaiknya mengeksploitasi atribut subjektif (yang bergantung pada pengguna) dalam desainnya.

#### 3. Mengapa PIM Kurang Diperhatikan Secara Historis?

Buku sumber memberikan dua alasan. *Pertama*, hingga belakangan ini koleksi digital pribadi orang umumnya masih kecil. *Kedua* — dan ini lebih penting — pemikiran dalam ilmu informasi dan ilmu komputer secara historis terpusat pada **organisasi dan pengambilan data publik**. Teori manajemen informasi tradisional mempelajari bagaimana para profesional informasi (seperti pustakawan atau perancang basis data) menstrukturkan data publik agar mudah diakses, menggunakan properti objektif data atau skema kategorisasi yang disepakati bersama, seperti **sistem desimal Dewey (Dewey decimal system)**. Ilmu komputer juga berfokus pada koleksi publik, tetapi dengan pendekatan berbeda: mengembangkan teknik untuk mengindeks koleksi publik daring secara otomatis sehingga pengguna dapat mengaksesnya lewat **pencarian kata kunci (keyword search)**.

PIM berbeda. Alih-alih membahas bagaimana orang mengakses koleksi publik, kurasi PIM berfokus pada bagaimana **pengguna individu memilih, mengorganisasi, dan mengakses koleksi pribadi mereka**.

#### 4. Kurasi sebagai Komunikasi dengan Diri Sendiri di Masa Depan

Salah satu metafora paling berpengaruh dalam buku ini adalah memandang kurasi sebagai **komunikasi terarah-diri (self-directed communication)**. Pada bidang ilmu informasi lain, tujuan manajemen informasi adalah merancang **saluran komunikasi (communication channel)** antara dua orang dengan peran berbeda: seorang profesional informasi (perancang situs web atau pustakawan) mengorganisasi informasi sasaran agar konsumen informasi di ujung lain saluran dapat menemukan dan menggunakannya. Karena konsumen informasi berbeda-beda dalam profesi, pendidikan, latar belakang sosiokultural, dan tujuan penggunaan, profesional informasi umumnya hanya boleh memanfaatkan **atribut yang tidak bergantung pengguna (user-independent attributes)**. Ini adalah pendekatan "satu ukuran untuk semua" (one-size-fits-all).

Kurasi informasi pribadi berbeda, karena **orang yang menyimpan dan memutuskan organisasi informasi adalah orang yang sama yang kelak mengambilnya**. Maka kurasi dapat dipandang sebagai jenis komunikasi khusus: sebuah interaksi **solipsistik (solipsistic)** — yakni interaksi seseorang dengan dirinya sendiri — pada dua titik waktu yang berbeda: waktu penyimpanan dan waktu pengambilan. Karena saya tahu bahwa saya sedang mengorganisasi untuk diri saya di masa depan, saya dapat memakai skema organisasi yang tidak akan dipahami orang lain, tetapi mencerminkan interaksi personal saya dengan informasi tersebut.

#### 5. Tiga Proses Kurasi (Sekilas)

Buku sumber membangun model **daur hidup kurasi (curation life cycle)** tiga tahap, yang didasarkan pada kerangka kerja PIM yang berpengaruh dari Jones (2007) dan beririsan dengan analisis Marshall (2008):

1. **Keeping (Penyimpanan)** — keputusan tentang informasi apa yang akan dipertahankan dalam koleksi pribadi. Sulit karena menuntut kita **memprediksi kebutuhan informasi diri kita di masa depan**.
2. **Management (Pengelolaan)** — bagaimana mengorganisasi data yang telah disimpan agar peluang menemukannya kembali meningkat. Melibatkan pertukaran (trade-off) antara usaha mengelola dan imbalan saat pemanfaatan.
3. **Exploitation (Pemanfaatan)** — proses mengambil kembali (retrieving) informasi. Inilah jantung praktik kurasi; jika kita tidak dapat memanfaatkan informasi yang kita simpan, maka keputusan menyimpan dan aktivitas mengelola menjadi sia-sia.

Ketiga proses ini akan dibahas mendalam di Bab 2, 3, dan 4.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Personal Information Management (PIM) | Manajemen Informasi Pribadi; aktivitas individu menyimpan butir informasi pribadi untuk diambil kembali kelak. |
| Information item | Butir informasi; satu unit data seperti dokumen, surel, foto, atau bookmark. |
| Curation | Kurasi; proses aktif memilih, mengorganisasi, dan mengakses koleksi pribadi. |
| Keeping | Penyimpanan; keputusan apa yang dipertahankan. |
| Management | Pengelolaan; pengorganisasian informasi yang telah disimpan. |
| Exploitation | Pemanfaatan; pengambilan kembali (retrieval) informasi. |
| User-independent attribute | Atribut yang tidak bergantung pengguna (objektif), mis. format, ukuran, tanggal. |
| User-subjective approach | Pendekatan yang memanfaatkan atribut yang bergantung pada pengguna. |
| Self-directed communication | Komunikasi terarah-diri; metafora kurasi sebagai percakapan dengan diri sendiri di masa depan. |
| Consumption model | Model konsumsi; pandangan manusia sebagai pencari/pengonsumsi informasi publik baru. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus pengantar — Rina, mahasiswa semester 6.** Rina menyimpan slide kuliah di folder `Kuliah`, mengunduh jurnal ke folder `Download`, menerima draf laporan kelompok lewat surel dari teman-temannya, dan menandai (bookmark) beberapa artikel di peramban. Saat menyusun skripsi, ia menyadari informasi tentang satu topik tersebar di mana-mana. Rina adalah **kurator** dari koleksi pribadinya: ia memutuskan apa yang disimpan (keeping), bagaimana menatanya (management), dan berjuang menemukannya kembali (exploitation). Sepanjang buku ajar ini, kita akan kembali ke pengalaman seperti milik Rina untuk mengilustrasikan setiap konsep.

### Temuan Penelitian (dari Buku Sumber)

Pendahuluan buku sumber lebih bersifat konseptual, tetapi sudah menyiratkan beberapa temuan yang akan diperdalam:

- Para penulis telah meneliti PIM selama hampir dua puluh tahun dan menerbitkan lebih dari empat puluh makalah PIM, sepuluh di antaranya ditulis bersama.
- Sebagian besar perilaku akses web ternyata bersifat **akses-ulang (reaccess)**, bukan pencarian informasi baru: antara **58 persen hingga 81 persen** dari seluruh akses pengguna adalah halaman yang pernah diakses sebelumnya. Ini menjadi salah satu argumen kuat bahwa model "konsumsi informasi baru" tidaklah lengkap.

### Rangkuman

- PIM adalah aktivitas menyimpan butir informasi pribadi untuk diambil kembali kelak; mencakup dokumen, surel, bookmark, tugas, dan kontak.
- PIM berbeda dari manajemen informasi publik karena **organizer dan retriever adalah orang yang sama**.
- Buku sumber memandang PIM melalui lensa **kurasi**, dengan tiga proses: keeping, management, exploitation.
- Tesis buku: teknologi dari bidang lain (search, tagging, GIM) gagal untuk PIM; folder hierarkis tetap dominan; solusi yang tepat adalah pendekatan **user-subjective**.
- Kurasi adalah **komunikasi solipsistik** dengan diri sendiri di masa depan.

### Latihan & Refleksi

**A. Pemahaman**
1. Tuliskan definisi PIM dengan kata-kata Anda sendiri, lalu sebutkan lima jenis butir informasi.
2. Apa perbedaan antara atribut "user-independent" dan atribut "user-subjective"?
3. Sebutkan tiga proses dalam daur hidup kurasi.

**B. Analisis (HOTS)**
4. Buku sumber mengkritik "model konsumsi" yang memandang manusia sebagai pencari informasi baru. Mengapa fakta bahwa 58–81 persen akses web adalah akses-ulang menjadi bukti kuat untuk kritik ini? Jelaskan logika argumennya.
5. Mengapa metafora "komunikasi dengan diri sendiri di masa depan" memungkinkan penggunaan skema organisasi yang tidak akan dipahami orang lain? Berikan satu contoh skema penamaan folder yang hanya bermakna bagi Anda.

**C. Tugas Praktik**
6. Lakukan inventarisasi singkat: hitung perkiraan jumlah folder di komputer/ponsel Anda dan kedalaman maksimum subfoldernya. Tuliskan satu kalimat: apakah Anda lebih sering "menyimpan rapi" atau "membiarkan menumpuk"? Simpan catatan ini; kita akan membandingkannya dengan temuan riset pada bab-bab berikutnya.

---

# BAGIAN I — Manajemen Informasi Pribadi: Perspektif Kurasi

## Pengantar Bagian I

Setiap dari kita kini memiliki koleksi besar data digital pribadi: dokumen, lembar kerja, presentasi, dan foto yang kita buat sendiri, ditambah surel, pesan, teks, dokumen atau foto yang dibagikan orang lain, serta sumber daya publik (peta, halaman web) yang kita akses dari internet. Apa yang menyatukan data yang beragam ini menjadi sebuah **koleksi pribadi** adalah penilaian kita bahwa data tersebut **mungkin bernilai bagi kita di masa depan**. Karena itu kita berusaha memelihara dan secara aktif mengorganisasinya sendiri, agar terjamin aksesnya di kemudian hari.

Bagian I menyajikan pemahaman ilmiah tentang bagaimana kita **memilih, mengorganisasi, dan mengakses** koleksi pribadi semacam itu. Di sini PIM didefinisikan sebagai proses individu **mengkurasi (curate)** data pribadinya untuk diakses kembali. Kurasi melibatkan tiga proses berbeda: (1) bagaimana kita memutuskan informasi apa yang disimpan, (2) bagaimana kita mengorganisasi data yang disimpan, dan (3) strategi yang kita pakai untuk mengaksesnya kelak.

Bagian I terdiri atas empat bab: Bab 1 memberikan motivasi dan kerangka (sifat arsip pribadi, daur hidup kurasi, properti informasi); Bab 2, 3, dan 4 masing-masing membahas proses keeping, management, dan exploitation secara mendalam. Sesuai sikap metodologis para penulis, pembahasan terutama berfokus pada riset mereka sendiri, bukan tinjauan menyeluruh seluruh literatur PIM.

---

## Bab 1 — Arsip Pribadi dan Proses Kurasi

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membandingkan** pandangan "manusia sebagai konsumen" dengan "manusia sebagai kurator" informasi.
2. **Menganalisis** tiga pengalaman buruk informasi pribadi yang melatarbelakangi pentingnya kurasi.
3. **Menjelaskan** skala dan kompleksitas arsip pribadi menggunakan statistik dari buku sumber.
4. **Menguraikan** daur hidup kurasi dan keterkaitan antartahapnya.
5. **Mengklasifikasikan** butir informasi berdasarkan tiga properti: orientasi aksi/informasi, keunikan, dan cara akumulasi.
6. **Mengevaluasi** klaim bahwa masalah PIM bersifat "tahan terhadap perubahan teknologi".

### Peta Konsep

```
   BUKAN KONSUMEN, MELAINKAN KURATOR
              |
   3 pengalaman buruk:           Skala arsip pribadi (statistik)
   - data pribadi hilang         - surel ~2.846 / ~2.568
   - koleksi besar tak jelas     - berkas ~2.200
   - gagal urus item aktif       - foto >4.000 / 4.475
              |                   - kertas 62 kg ≈ tumpukan 30 m
   KURASI = komunikasi terarah-diri
              |
   DAUR HIDUP KURASI: Keeping -> Management -> Exploitation
              |
   PROPERTI INFORMASI:
   - Actionable vs Informative
   - Unique vs Non-unique
   - Active vs Passive accumulation
              |
   PIM "tahan" terhadap perubahan teknologi
```

### Materi Inti

#### 1.1 Bukan Konsumen, melainkan Kurator

Revolusi teknologi dua dekade terakhir ditandai meningkatnya **ketersediaan informasi**. Kita kini punya akses mudah ke peta, ensiklopedia, berita, informasi medis, dan media sosial. Hal ini melahirkan teori-teori yang memandang manusia sebagai **penjelajah (explorers)** yang terus-menerus mencari dan mengonsumsi informasi baru dari koleksi publik. Buku sumber berargumen bahwa pandangan "manusia sebagai konsumen informasi publik yang baru" ini **tidak memadai**, karena mengabaikan banyak masalah mendesak tentang bagaimana kita menyimpan, mengorganisasi, dan menggunakan kembali informasi **pribadi** kita.

Para penulis menyajikan tiga **pengalaman buruk** yang menurut mereka pasti pernah dialami setiap pembaca, dan ketiganya tidak berkaitan dengan informasi baru:

1. **Data pribadi hilang (Lost personal data).** Pengalaman cemas tidak dapat menemukan informasi penting yang kita tahu kita miliki — dokumen, nama atau nomor kontak, atau surel berisi informasi penting. Pengalaman ini terasa lebih menjengkelkan justru ketika kita sudah berusaha keras mengorganisasinya.
2. **Koleksi pribadi besar yang tidak jelas nilainya (Large, disorganized personal collections of unclear value).** Kemudahan menangkap dan berbagi informasi membuat kita semua memiliki koleksi besar. Ironisnya, kita kesulitan mengakses informasi berharga dari koleksi itu, sekaligus menyadari bahwa kita menumpuk banyak informasi bernilai rendah.
3. **Gagal menangani informasi peka-waktu yang menuntut aksi (Failing to deal with time-sensitive information that requires action).** Terutama dalam surel, kita kerap melewatkan permintaan atau tenggat yang menuntut tindakan — bahkan setelah bersusah payah membuat pengingat.

Benang merahnya: ketiga pengalaman ini menyangkut **kegagalan mengorganisasi/menstruktur informasi agar mudah dipakai ulang**, dan semuanya melibatkan informasi **pribadi**. Maka kita perlu memahami bagaimana kita mengkurasi informasi pribadi — sebuah pandangan alternatif yang disebut **kurasi informasi (information curation)**.

#### 1.2 Kurasi sebagai Komunikasi Terarah-Diri

Aspek kritis kurasi: **orang yang mengorganisasi informasi adalah juga orang yang mengambilnya**. Ini menjadikan kurasi "permainan yang berbeda" (a different sort of game) dari konsumsi, dengan aturan main yang berbeda dari bidang ilmu informasi lain (lihat pembahasan metafora komunikasi pada Bab Pendahuluan). Akses pun berubah sifat. Dalam manajemen informasi klasik, sukses sering berarti menemukan informasi yang memenuhi properti umum (misalnya "tiket pesawat murah ke Spanyol"), dan banyak butir dapat memenuhi kueri itu. Dalam PIM, pengguna sering punya **butir spesifik dalam pikiran**, sehingga kriteria sukses jauh lebih ketat: pengambilan baru berhasil bila butir tertentu itu yang ditemukan, dan ada kekecewaan kuat bila gagal (Whittaker, Bergman, & Clough 2010). Di sisi lain, pengetahuan sebelumnya kerap membuat pengambilan lebih mudah: pengguna dapat **mengenali (recognize)** butir sasaran dengan cepat tanpa perlu meneliti relevansinya seperti pada halaman web baru.

#### 1.3 Munculnya Koleksi Data Pribadi yang Besar

Motivasi kuat bagi pentingnya kurasi adalah kenyataan bahwa kita kini memiliki akumulasi besar informasi pribadi yang menuntut organisasi. Jika model konsumsi benar — bahwa kita selalu mencari sumber baru alih-alih bertindak dengan informasi yang sudah dimiliki — maka kita tidak akan mengharapkan orang memelihara arsip pribadi. Faktanya, orang **menyimpan informasi pribadi dalam jumlah sangat besar**. Buku sumber menyajikan sejumlah statistik untuk menggambarkan skala masalah kurasi:

| Jenis data | Temuan skala (dari buku sumber) | Sumber yang dikutip |
|---|---|---|
| Surel (disimpan) | Rata-rata sekitar **2.846** pesan disimpan (rangkuman 8 studi); peneliti bisa menyimpan jauh lebih banyak | Whittaker, Bellotti, & Gwizdka 2007; Fisher et al. 2006 |
| Surel (studi pemantauan) | Rata-rata arsip **2.568** pesan (345 pengguna, beberapa bulan) | Whittaker et al. 2011 |
| Berkas pribadi | Rata-rata sekitar **2.200** berkas di hard drive | Boardman & Sasse 2004 |
| Foto digital | Rata-rata lebih dari **4.000** gambar pribadi (kemungkinan masih meremehkan karena pertumbuhan eksponensial) | Whittaker, Bergman, & Clough 2010 |
| Bookmark | Orang menyimpan ratusan bookmark | Abrams et al. 1998; Aula et al. 2005; dll. |
| Arsip kertas | Rata-rata **62 kilogram** kertas, setara tumpukan direktori telepon setinggi **30 meter** | Whittaker & Hirschberg 2001 |

Orang tidak sekadar menyimpan secara pasif; mereka berupaya keras mengorganisasi. Bellotti et al. (2005) menemukan orang menghabiskan **10 persen** total waktu dalam surel untuk memfail dan mengorganisasi pesan, menghasilkan rata-rata **244 folder** surel — meski studi lebih baru (Whittaker et al. 2011) memperkirakan rata-rata lebih kecil, **46,89 folder**. Berkas komputer juga menunjukkan organisasi aktif: rata-rata **57 folder** dengan kedalaman rata-rata **3,3 subfolder** (Boardman & Sasse 2004). Bookmark web menghasilkan rata-rata **17 folder** dengan struktur subfolder kompleks.

Kurasi diperkirakan akan semakin penting karena teknologi baru (sensor di mana-mana, pelacak medis/kebugaran, video digital, kamera yang dapat dikenakan seperti Google Glass) mempermudah penangkapan jenis data pribadi baru, ditambah penyimpanan digital yang kian murah.

#### 1.4 Mendefinisikan Informasi Pribadi

Apa sesungguhnya "informasi pribadi"? Poin kritis: **tidak semua data pribadi dibuat sendiri**. Arsip pribadi juga memuat surel, teks, dan media sosial yang dibuat orang lain, serta data yang semula diakses dari arsip publik (peta, tautan sumber daring berguna). Yang menyatukan semua tipe data ini menjadi koleksi pribadi adalah **proyeksi nilai masa depan** bagi pengguna. Maka, yang mendefinisikan informasi pribadi **bukan tipe atau asal-usulnya, melainkan bahwa pengguna secara strategis memilih mengorganisasinya sendiri demi akses di masa depan**. Dengan kata lain: informasi pribadi adalah informasi yang **secara aktif dikurasi pengguna**.

#### 1.5 Daur Hidup Kurasi

Kurasi melibatkan aktivitas **berorientasi masa depan** — serangkaian praktik yang memilih dan mengelola informasi pribadi untuk mendorong pemanfaatan kelak. Model tiga tahap (keeping, management, exploitation) didasarkan pada kerangka PIM Jones (2007) dan beririsan dengan Marshall (2008).

- **Keeping.** Kita terus-menerus bertemu informasi baru; sebagian besar tidak relevan atau bersifat sekejap. Setelah kasus mudah disingkirkan, keputusan apa yang disimpan menjadi rumit karena menuntut **memprediksi kebutuhan diri masa depan**. Ada biaya menyimpan: bila terlalu banyak, muncul biaya organisasi dan kesulitan pengambilan. Ada pula trade-off strategis: menyimpan sendiri vs meregenerasi dari sumber publik atau meminta dari kolaborator.
- **Management.** Setelah memutuskan menyimpan, bagaimana mengelolanya agar terjamin nilainya kelak? Ini melibatkan trade-off antara **usaha** mengelola dan **imbalan** saat pemanfaatan. Metode intensif (mis. memfail ke folder terstruktur) cenderung memberi hasil lebih tinggi tetapi menuntut usaha awal besar; metode santai (membiarkan menumpuk) mengurangi biaya awal tetapi mempersulit penemuan kembali. Management bersifat **iteratif** dan **repetitif**: kita terus merevisi struktur; sebagian orang sesekali "bersih-bersih" (spring-clean) inbox. Teknologi awan (Google Drive, Dropbox, OneDrive) memunculkan **group information management (GIM)**, yang akan dibahas khusus di Bab 7.
- **Exploitation.** Inilah proses pengambilan kembali — jantung kurasi. Dua cara utama: **navigasi (navigation)** manual melalui hierarki folder, dan **pencarian (search)** lewat kueri kata kunci. Ada pula pendekatan ketiga berbasis **kebaruan/frekuensi (recency/frequency)**, seperti daftar dokumen terkini, tombol Back, dan riwayat peramban. Namun metode berbasis kebaruan bergantung pada keberhasilan pengambilan sebelumnya, sehingga harus dikombinasikan dengan metode lain; buku ini tidak banyak berfokus padanya.

**Keterkaitan antar proses.** Pemanfaatan yang berhasil sangat bergantung pada apa yang disimpan dan bagaimana dikelola. Semakin banyak disimpan, semakin besar usaha mengelola dan semakin sulit menemukan. Hasil di masa lalu memengaruhi perilaku masa depan: kegagalan pengambilan dapat membuat orang mengubah cara menyimpan atau mengelola.

#### 1.6 Properti Informasi

Tidak semua butir informasi setara. Tiga properti penting memengaruhi cara kurasi:

1. **Informatif vs Dapat-ditindaklanjuti (Informative vs Actionable).** Banyak surel bersifat **actionable** — penerima diharapkan merespons, sering dalam tenggat tertentu ("beri tahu saya sebelum Selasa"). Sebaliknya, halaman web hasil pencarian umumnya **informative** — menarik tetapi tidak menuntut tindakan bertenggat. Pemetaan ini tidak selalu rapi (ada surel FYI yang tidak menuntut aksi; ada halaman web berisi formulir). Butir actionable menuntut strategi **pengingatan (reminding)** khusus.
2. **Keunikan (Uniqueness).** Sebagian data (mis. berkas yang kita buat sendiri) mungkin hanya ada di komputer kita; bila tidak di-backup, hilang selamanya bila sistem rusak. Data lain tidak unik (mis. data web yang ada di banyak server). Keunikan didefinisikan **secara personal** — relatif terhadap tujuan dan kepentingan kita, dan kerap terkait dengan informasi yang kita investasikan usaha untuk membuatnya.
3. **Akumulasi & Keterlihatan: Pengarsipan Aktif vs Pasif (Active vs Passive Archiving).** Sebagian informasi terakumulasi otomatis (surel menumpuk secara default kecuali dihapus = **pasif**), sebagian lain menuntut tindakan untuk dipertahankan (halaman web perlu di-bookmark secara aktif = **aktif**).

**Tabel 1.1 (adaptasi dari buku sumber): Properti utama berbagai tipe informasi**

| Tipe informasi | Actionable atau Informative? | Keunikan | Akumulasi Aktif/Pasif |
|---|---|---|---|
| Dokumen kertas & elektronik pribadi | Actionable jika dibuat sendiri & terkini; arsip jangka panjang cenderung informative | Unik jika dibuat sendiri atau dianotasi | Pasif |
| Surel | Sering actionable; arsip jangka panjang cenderung informative | Berkisar dari unik hingga non-unik (kiriman massal) | Pasif |
| Kontak | Actionable | Non-unik | Aktif (ponsel) & pasif (surel) |
| Foto pribadi | Bukan actionable, bukan informative: bersifat **afektif** | Dominan unik | Pasif |
| Web | Informative | Non-unik | Aktif |

#### 1.7 Perilaku PIM dan Perubahan Teknologi

Bukankah kajian ilmiah PIM dipersulit oleh kenyataan bahwa teknologi terus berubah? Buku sumber menjawab dengan tema kunci: **masalah-masalah fundamental PIM secara mengejutkan tahan terhadap perubahan teknologi.** Studi tentang kertas, surel, dan dokumen web — beberapa dilakukan hampir dua puluh tahun sebelumnya — memunculkan masalah yang serupa meski teknologinya berbeda: kita masih lupa menangani item actionable vital, sulit menilai nilai informasi baru, menyimpan banyak informasi yang nilainya diragukan, dan gagal mengambil informasi penting yang sudah susah payah kita organisasi. Sebagai ilustrasi, produk **Inbox by Gmail** dari Google (dirilis 2015) berupaya mengatasi masalah mengingat surel actionable — masalah yang pertama kali diidentifikasi hampir dua puluh tahun sebelumnya (Whittaker & Sidner 1996).

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Curation life cycle | Daur hidup kurasi; model tiga tahap keeping–management–exploitation. |
| Actionable item | Butir yang menuntut tindakan (mis. surel yang harus dibalas), sering bertenggat. |
| Informative item | Butir yang bersifat informatif tetapi tidak menuntut tindakan bertenggat. |
| Uniqueness | Keunikan; apakah suatu butir hanya ada pada satu salinan milik pengguna. |
| Active/Passive accumulation | Akumulasi aktif (perlu tindakan untuk menyimpan) vs pasif (menumpuk otomatis). |
| Reminding | Pengingatan; strategi agar item actionable tidak terlupakan. |
| Affective | Afektif; bermuatan emosi (mis. foto pribadi). |
| Recognition vs recall | Pengenalan vs pengingatan-bebas; mengenali lebih mudah daripada memanggil dari ingatan. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 1.1 — Pak Budi pindah ruang kerja.** Pak Budi, dosen yang pindah ke ruangan baru yang lebih kecil, terpaksa menyortir arsip kertasnya. Mirip temuan studi office-move dalam buku sumber, ia menghabiskan waktu lama tetapi hanya membuang sedikit; sebagian besar tetap disimpan "siapa tahu perlu". Studi kasus ini akan kita rujuk lagi di Bab 2.
>
> **Studi kasus 1.2 — Klasifikasi tipe data Sinta.** Sinta, staf administrasi, memiliki: (a) surat tugas dari atasan yang harus dibalas Jumat (actionable, unik), (b) brosur produk vendor (informative, non-unik), (c) foto acara kantor (afektif, unik), (d) tautan portal regulasi pemerintah (informative, non-unik, akumulasi aktif). Latihlah diri Anda mengisi Tabel 1.1 untuk koleksi Sinta.

### Temuan Penelitian (dari Buku Sumber)

- Arsip surel rata-rata berkisar **~2.568–2.846** pesan; berkas **~2.200**; foto **>4.000**; arsip kertas rata-rata **62 kg** (≈ tumpukan 30 m).
- Pengorganisasian aktif: **10 persen** waktu surel untuk memfail; rata-rata **244** (atau **46,89**) folder surel; **57** folder berkas dengan kedalaman **3,3**; **17** folder bookmark.
- **58–81 persen** akses web adalah akses-ulang (revisits), bukan pencarian informasi baru.
- Masalah PIM bersifat **deep-rooted** dan tahan terhadap perubahan teknologi.

### Rangkuman

- Buku sumber menggeser pandangan "manusia konsumen" menjadi "manusia kurator".
- Tiga pengalaman buruk (data hilang, koleksi tak jelas nilainya, gagal urus item actionable) menyoroti pentingnya kurasi.
- Arsip pribadi sangat besar dan dikelola aktif, tetapi kerap tidak efektif.
- Daur hidup kurasi: keeping → management → exploitation, saling terkait.
- Properti informasi (actionable/informative, unik/non-unik, aktif/pasif) menentukan cara kurasi.
- Masalah PIM tahan terhadap perubahan teknologi.

### Latihan & Refleksi

**A. Pemahaman**
1. Sebutkan tiga pengalaman buruk informasi pribadi menurut buku sumber.
2. Apa beda butir actionable dan informative? Beri masing-masing satu contoh.
3. Mengapa foto pribadi disebut "afektif" dalam Tabel 1.1?

**B. Analisis (HOTS)**
4. Buku sumber menyatakan masalah PIM "tahan terhadap perubahan teknologi". Berikan satu argumen yang mendukung dan satu argumen yang menentang klaim ini, lalu nyatakan posisi Anda.
5. Mengapa keunikan didefinisikan "secara personal"? Bagaimana definisi personal ini memengaruhi keputusan backup data?
6. Statistik arsip kertas (62 kg) berasal dari studi hampir dua dekade lalu. Apakah relevansinya berkurang di era digital? Kaitkan jawaban Anda dengan tema "ketahanan terhadap teknologi".

**C. Tugas Praktik**
7. Buatlah tabel seperti Tabel 1.1 untuk sepuluh butir informasi nyata milik Anda. Klasifikasikan tiap butir pada tiga properti. Tuliskan satu paragraf refleksi: properti mana yang paling memengaruhi cara Anda menyimpannya?

---

## Bab 2 — Penyimpanan (Keeping)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** mengapa keputusan keeping sulit, dengan merujuk pada biaya pengelolaan dan biaya pemanfaatan.
2. **Menghubungkan** kesulitan keeping dengan keterbatasan psikologis dalam memprediksi masa depan (bias, loss aversion).
3. **Menganalisis** temuan studi keeping pada kertas, surel, kontak, web, dan foto.
4. **Membedakan** dua penyebab utama overkeeping: information overload dan deferred evaluation.
5. **Mengevaluasi** strategi penundaan (deferral) beserta dua kelemahannya.

### Peta Konsep

```
KEEPING = memutuskan menyimpan atau menghapus
        |
   Biaya: Management cost + Exploitation cost
        |
   Sulit karena: prediksi masa depan + bias psikologis (loss aversion / Prospect Theory)
        |
   Studi per media:
   - Kertas: buang hanya 22%, 23% data tak terbaca
   - Surel: simpan ~70%; actionable dihapus 0,5%, informative dihapus 30%
   - Kontak: 858 rata-rata, hanya 14% penting
   - Web: 58% bookmark tak pernah dipakai; post-retrieval value
   - Foto: 4.475 rata-rata, hapus 17%
        |
   AKAR MASALAH: information overload + deferred evaluation -> OVERKEEPING
```

### Materi Inti

#### 2.1 Mengapa Harus Memutuskan?

Keeping menyangkut keputusan mendasar: **mempertahankan atau menghapus** informasi yang kita temui. Kita tidak bisa menyimpan semuanya karena ada biaya:

- **Biaya pengelolaan (Management costs):** semakin banyak disimpan, semakin besar usaha mengorganisasi. Visi "informasi akan terorganisasi otomatis" belum terwujud.
- **Biaya pemanfaatan (Exploitation costs):** menyimpan informasi bernilai rendah memperbesar kesulitan pengambilan; terlalu banyak item mengganggu dan tidak efisien bila akses dilakukan via navigasi manual.

Setiap hari kita menerima surel baru, membuat berkas, dan menjelajah situs. Buku sumber mengutip data laju akuisisi: rata-rata **5 berkas baru per hari** dan **1 bookmark setiap 5 hari** (Boardman & Sasse 2004); **1 kontak baru per hari** (Whittaker, Jones, & Terveen 2002); sekitar **5 foto digital** (Whittaker, Bergman, & Clough 2010); surel bervariasi antara **5 hingga 60** (estimasi paling andal **24 pesan disimpan** per hari, dari **44** yang diterima — Whittaker et al. 2011). Angka-angka ini menyembunyikan kompleksitas: statistik mencatat keputusan menyimpan, tetapi tidak mencatat banyaknya keputusan membuang. Untuk surel saja, dengan asumsi konservatif volume tetap, ini setara **lebih dari 350.000 keputusan keeping** sepanjang lima puluh tahun kehidupan digital.

#### 2.2 Akar Kesulitan: Memprediksi Masa Depan

Mengapa keputusan keeping begitu sulit? Karena menuntut kita **memprediksi nilai masa depan** suatu butir (Bruce 2005). Ini masalah psikologis umum: riset menunjukkan manusia buruk dalam keputusan yang melibatkan masa depan, yang menuntut penalaran tentang situasi hipotetis. Prediksi kita bias: kita mengira masa depan akan sangat mirip masa kini, dan terlalu dipengaruhi peristiwa terkini atau yang mudah diingat (Gilbert 2009; Kahneman & Tversky 1979). Kita juga **menghindari kerugian (loss averse)**, sehingga memikirkan informasi dalam konteks kemungkinan dihapus membuat kita **menilainya terlalu tinggi**.

#### 2.3 Menyimpan Kertas

Salah satu dari sedikit studi langsung tentang keeping memeriksa arsip kertas terkait pekerjaan (Whittaker & Hirschberg 2001). Masalah metodologis: sulit menemukan konteks di mana orang benar-benar berfokus pada keputusan keeping. Studi ini menemukan situasi seperti itu — **pindah ke ruang kantor yang lebih kecil** dengan ruang penyimpanan lebih sedikit, sehingga memaksa orang memutuskan apa yang disimpan dan dibuang. Pendekatan **multi-metode** (kualitatif + kuantitatif) digunakan.

**Perilaku membuang.** Sesuai literatur loss aversion, terdapat bias kuat ke arah retensi. Bahkan setelah menghabiskan waktu lama (hampir **sembilan jam**) merasionalisasi data, peserta hanya membuang **22 persen** arsip asli; arsip akhir rata-rata menempati **lebih dari 18 kotak pindahan**. Yang dibuang sebagian adalah informasi yang dulu berharga kini usang — tetapi mengejutkan, **23 persen data yang dibuang tidak pernah dibaca**. Mengapa menyimpan sesuatu yang tak pernah dilihat? Dua masalah umum berkontribusi:

- **Kelebihan beban informasi (Information overload):** waktu tidak cukup untuk memproses semua informasi; data non-urgen ditaruh di tumpukan "untuk dibaca" dan menumpuk tanpa batas.
- **Evaluasi tertunda (Deferred evaluation):** orang sengaja menunda penilaian, membiarkan waktu berlalu agar penilaian lebih matang — tetapi jarang kembali untuk merasionalisasi.

Akibatnya arsip penuh informasi yang nilainya diragukan. **74 persen** peserta tidak membersihkan arsip selama lebih dari setahun, dan **84 persen** pembersihan dipicu peristiwa ekstrinsik (perubahan pekerjaan atau pindah kantor), bukan inisiatif spontan.

**Apa yang disimpan dan mengapa.** Hipotesis awal: sebagian besar yang disimpan akan **unik**. Keunikan memang penting: tiga jenis data unik menyumbang **49 persen** arsip — catatan kerja, arsip proyek yang selesai, dan dokumen legal (kontrak/pajak). Namun, di luar dugaan, keunikan **bukan satu-satunya** kriteria: hanya **49 persen** arsip asli yang unik, sementara **36 persen** adalah salinan dokumen yang tersedia publik. Mengapa menyimpan salinan dokumen publik yang mudah didapat? Studi ini mengidentifikasi **empat alasan**:

1. **Ketersediaan (Availability):** agar materi ada di tangan saat dibutuhkan, menghindari penundaan akses ulang.
2. **Pengingatan (Reminding):** salinan pribadi (terutama yang ditaruh di tempat terlihat) memperbesar peluang bertemu lagi dengan dokumen; mendukung tindakan tertunda.
3. **Ketidakpercayaan pada penyimpanan eksternal (Lack of trust in external stores):** orang tak percaya institusi/arsip lain (termasuk web) akan menyimpan dokumen yang mereka butuhkan.
4. **Sentimen (Sentiment):** alasan emosional — bagian dari sejarah intelektual atau identitas profesional.

Alasan potensial lain — **anotasi (annotations)** pribadi pada dokumen — ternyata berdaya guna terbatas: banyak orang menyatakan anotasi bernilai sekejap dan menjadi tak terbaca setelah beberapa waktu. Studi pencatatan jangka panjang menunjukkan kegunaan catatan tulisan tangan **menurun cepat bahkan setelah sebulan** (Kalnikaité & Whittaker 2007, 2008a).

#### 2.4 Menyimpan Surel

Surel berbeda dari berkas buatan sendiri maupun dokumen web: sebagian besar **dibuat orang lain** (kadang tak dikenal), banyak yang **actionable**, dan sangat **bervariasi** (tugas, lampiran, FYI, janji temu, pesan sosial, lelucon). Secara keseluruhan kita menyimpan sekitar **70 persen** pesan surel (Dabbish et al. 2005) — angka yang tinggi mengingat banyak pesan tampak tak relevan. Perilaku keeping berbeda untuk pesan informative vs actionable.

**Pesan informatif** menyusun sekitar **sepertiga (34 persen)** kiriman surel (Dabbish et al. 2005) dan diperlakukan mirip dokumen kertas: keputusan sulit, sehingga digunakan **strategi penundaan**. Information overload memperparah; volume pesan membuat orang menunda membaca tuntas dan sering tidak kembali. Salah satu faktor: panjang pesan — inbox memuat proporsi pesan panjang lebih tinggi (ditinggalkan untuk dibaca nanti).

**Pesan yang dapat ditindaklanjuti (actionable)** menuntut tindakan spesifik. Di dunia ideal, kita memproses sekali lalu menghapus — disebut **model satu-sentuhan (one-touch model)**. Pengguna membalas **65 persen** pesan actionable dengan segera (Dabbish et al. 2005), tetapi tetap **menyimpan 85 persen**-nya — sehingga "one-touch" tidak menggambarkan praktik nyata. Banyak tugas surel terlalu kompleks/panjang untuk dieksekusi seketika, sehingga **37 persen** ditunda. Tugas saling-bergantung (interdependent) yang menuntut kolaborasi memunculkan iterasi dan penundaan; estimasi pesan yang menjadi bagian utas percakapan (threading) berkisar **30–62 persen**. Akibatnya, pesan actionable hampir selalu disimpan sebagai pengingat (**hanya 0,5 persen dihapus**), jauh lebih rendah daripada pesan informatif (**30 persen dihapus**).

#### 2.5 Menyimpan Kontak

Whittaker, Jones, & Terveen (2002) menelaah kriteria memasukkan seseorang ke daftar kontak. Kita kelebihan beban kontak (di-cc, membaca posting teman/kolega/orang asing). Banyak klien surel kini otomatis merekam kontak, tetapi banyak yang tak pernah ditengok lagi bahkan tak dikenal. Sulit menebak kontak penting masa depan dari interaksi jangka pendek; kepentingan baru jelas seiring waktu. Peserta sering **overkeep** kontak (rolodex besar, tumpukan kartu nama), tetapi hanya mencatat informasi rinci untuk sebagian kecil. Faktor penentu kontak penting: **frekuensi dan kebaruan komunikasi**, serta durasi interaksi panjang. Temuan mencolok: meski arsip kontak rata-rata **858**, peserta menilai hanya **14 persen (118)** sebagai penting dan layak disimpan; mereka mengeluarkan pengirim spam. Inilah perbedaan kunci kontak dari surel/kertas: proporsi yang dinilai **tidak penting** jauh lebih besar.

#### 2.6 Menyimpan Halaman Web

Keputusan keeping web menampilkan dua jenis kesalahan: **commission** (overkeeping yang ternyata bernilai rendah) dan **omission** (gagal menyimpan yang ternyata dibutuhkan). Contoh commission: orang membuat bookmark yang tak pernah dipakai — Tauscher & Greenberg (1997) menunjukkan **58 persen** bookmark tak pernah digunakan. Contoh omission: Wen (2003) mengangkat istilah **post retrieval value** untuk sumber web yang diakses tetapi tidak dipertahankan, baru disadari kegunaannya kemudian; studinya menunjukkan orang hanya mampu menemukan kembali sekitar **20 persen** informasi yang sebelumnya mereka akses dan perhatikan.

#### 2.7 Menyimpan Foto

Dengan fotografi digital, jumlah foto meningkat masif. Studi terhadap orang tua berkeluarga muda (Whittaker, Bergman, & Clough 2010) menemukan rata-rata **4.475** gambar digital. Semua peserta menghapus sebagian (rata-rata diperkirakan **17 persen**), dengan alasan kualitas teknis buruk atau tidak menangkap peristiwa menarik. Namun penghapusan sulit: banyak foto yang disimpan adalah **nyaris-duplikat (near-duplicate)** — pengguna "menyimpan opsi" untuk sudut terbaik. Alasan overkeeping: persepsi biaya menyimpan banyak foto kecil, sehingga keputusan keeping tidak berfokus pada konteks pengambilan kelak. Seperti pada kertas dan surel, ada harapan kuat akan "kembali merapikan nanti" — yang jarang terjadi.

#### 2.8 Sintesis: Overkeeping dan Strategi Penundaan

Keputusan keeping sulit karena menuntut: (1) memprediksi kebutuhan pengambilan masa depan, (2) memperhitungkan bahwa kebutuhan dapat berubah, dan (3) memutuskan nilai di tengah information overload, sering berdasar pembacaan tidak tuntas. Kecenderungan utama adalah **overkeeping**. Penghapusan jarang: bervariasi dari **17 persen** (foto) hingga **30 persen** (surel). Kontak berbeda — karena terpapar banyak kontak, mayoritas (**86 persen**) dianggap tidak penting. Daripada keputusan sekali jadi, orang memakai **strategi penundaan (deferral)** dengan dua kelemahan: (1) jarang kembali mengevaluasi ulang, dan (2) koleksi penuh item nilai meragukan yang menyulitkan penemuan item benar-benar berharga.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Overkeeping | Menyimpan berlebihan, termasuk item yang tak pernah diakses. |
| Information overload | Kelebihan beban informasi; waktu tak cukup memproses semua input. |
| Deferred evaluation / Deferral | Evaluasi/keputusan tertunda; menunggu kepastian nilai informasi. |
| Loss aversion | Penghindaran kerugian; rugi terasa lebih besar daripada untung yang setara. |
| One-touch model | Model satu-sentuhan; idealnya memproses pesan sekali lalu menghapus. |
| Threading | Pengutasan; pesan yang menjadi bagian percakapan berantai. |
| Post retrieval value | Nilai pasca-pengambilan; nilai sumber web yang baru disadari setelah tak dipertahankan. |
| Error of commission/omission | Kesalahan menyimpan yang tak perlu / gagal menyimpan yang perlu. |
| Near-duplicate | Nyaris-duplikat; foto/berkas yang hampir identik. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 2.1 — Inbox Bu Dewi.** Bu Dewi, kepala bagian, menerima sekitar 40-an surel sehari. Pesan dari rektorat yang menuntut balasan ia biarkan di inbox sebagai pengingat (actionable, hampir tidak pernah dihapus), sementara buletin internal ia abaikan tetapi jarang dihapus (informative). Pola ini mencerminkan temuan: actionable dihapus ~0,5%, informative ~30%.
>
> **Studi kasus 2.2 — Galeri 9.000 foto Andi.** Andi punya ribuan foto wisuda dan keluarga, banyak nyaris-duplikat. Ia berniat "merapikan akhir pekan ini" — niat yang tak kunjung terlaksana. Ini ilustrasi "collect now, organize later, view in the future" yang dikutip buku sumber.

### Temuan Penelitian (dari Buku Sumber)

- Laju akuisisi: ~5 berkas/hari, 1 bookmark/5 hari, 1 kontak/hari, ~5 foto/hari, ~24 surel disimpan dari 44 diterima.
- >350.000 keputusan keeping surel sepanjang 50 tahun kehidupan digital.
- Kertas (office move): buang hanya **22%**, **23%** data dibuang tak pernah dibaca, **74%** tak bersih-bersih >1 tahun, **84%** pembersihan dipicu peristiwa ekstrinsik.
- Arsip kertas: **49%** unik, **36%** salinan publik; empat alasan menyimpan salinan publik.
- Surel: simpan **~70%**; informative **34%** kiriman; actionable dibalas segera **65%** tetapi disimpan **85%**; ditunda **37%**; threading **30–62%**; actionable dihapus **0,5%**, informative **30%**.
- Kontak: rata-rata **858**, penting hanya **14% (118)**; **86%** dianggap tak penting.
- Web: **58%** bookmark tak pernah dipakai; hanya **~20%** informasi web berhasil ditemukan kembali (Wen 2003).
- Foto: rata-rata **4.475**, dihapus **~17%**.

### Rangkuman

- Keeping sulit karena menuntut prediksi masa depan di tengah bias psikologis dan information overload.
- Dua mesin utama overkeeping: information overload dan deferred evaluation.
- Pola overkeeping konsisten lintas media (kertas, surel, kontak, foto); pengecualian sebagian: web dan kontak.
- Item actionable hampir selalu disimpan sebagai pengingat.
- Strategi penundaan memiliki dua kelemahan inheren.

### Latihan & Refleksi

**A. Pemahaman**
1. Sebutkan dua biaya yang membuat kita tidak bisa menyimpan semua informasi.
2. Jelaskan beda information overload dan deferred evaluation.
3. Mengapa pesan actionable hampir tidak pernah dihapus (0,5%)?

**B. Analisis (HOTS)**
4. Loss aversion (Kahneman & Tversky 1979) digunakan untuk menjelaskan overkeeping. Uraikan rantai sebab-akibat dari prinsip psikologis ini hingga ke perilaku menyimpan berlebihan.
5. Kontak menunjukkan pola berbeda dari surel/kertas (mayoritas dianggap tidak penting). Apa yang menyebabkan perbedaan ini, dan apa implikasinya bagi desain aplikasi kontak?
6. Buku sumber menyebut empat alasan menyimpan salinan dokumen publik. Manakah yang menurut Anda paling kuat di era cloud, dan mengapa?

**C. Tugas Praktik**
7. Selama tiga hari, catat setiap kali Anda memutuskan **menghapus** sesuatu (surel, berkas, foto). Hitung rasio hapus terhadap total item baru. Bandingkan rasio Anda dengan angka buku sumber (foto 17%, surel 30%). Tuliskan refleksi: apakah Anda seorang "overkeeper"?

---

## Bab 3 — Pengelolaan (Management)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membedakan** organisasi semantik dan temporal, serta mental cueing dan external cueing.
2. **Membandingkan** strategi filing dan piling beserta trade-off-nya.
3. **Menganalisis** strategi pengelolaan surel (no filing, frequent filing, spring cleaning).
4. **Menjelaskan** mengapa folder bisa gagal karena terlalu besar, terlalu kecil, atau terlalu banyak.
5. **Mengaitkan** perbedaan individu dan sifat kepribadian dengan strategi pengelolaan.

### Peta Konsep

```
MANAGEMENT = mengorganisasi item yang disimpan agar mudah diambil
        |
   Dua jenis organisasi:
   - Semantik (kemiripan konsep) -> mental cueing + external cueing
   - Temporal (kapan harus diproses) -> reminding
        |
   Strategi (Malone 1983): FILING vs PILING
        |
   Per media:
   - Kertas: filer vs piler (ambang 40%)
   - Berkas: 57 folder, kedalaman 3,3
   - Surel: no filing / frequent filing / spring cleaning
   - Web: bookmark + social tagging
   - Foto: struktur rudimenter (mirip pile)
        |
   Perbedaan individu & kepribadian (Big Five): Conscientiousness, Neuroticism
```

### Materi Inti

#### 3.1 Inti Kurasi

Management adalah **jantung kurasi**: dengan menata item yang disimpan, kita meningkatkan kemampuan mengambilnya kembali. Skala masalahnya besar. Dengan estimasi laju akuisisi harian (Boardman & Sasse 2004; dll.) dan asumsi konservatif tetap, sepanjang **lima puluh tahun** kehidupan digital kita akan menyimpan aktif sekitar **100.000 dokumen, 440.000 surel, dan 120.000 foto digital**.

Sebagian management terjadi lebih sering dari dugaan: studi longitudinal (Boardman & Sasse 2004) menemukan orang membuat **folder berkas baru tiap tiga hari** dan **folder surel baru tiap lima hari** — bukti bahwa orang terus merefleksikan dan merasa organisasinya kurang memadai. Namun reorganisasi besar atau penghapusan ekstensif jarang; orang cenderung memodifikasi struktur secara inkremental. Orang juga membuat **kesalahan management**: membangun sistem bookmark hierarkis rumit padahal **42 persen** bookmark tak pernah diakses (Tauscher & Greenberg 1997); menghabiskan **10 persen** waktu surel untuk memfail padahal akses lebih sering lewat inbox/pencarian daripada folder. Untuk foto, kesalahannya berlawanan: **gagal mengorganisasi** padahal jelas dibutuhkan.

#### 3.2 Cueing Semantik

Organisasi semantik (menstruktur item berdasarkan kemiripan konsep) adalah aktivitas kognitif fundamental manusia — bahkan bayi mengategorikan objek berdasar **eksemplar/prototipe** (mis. konsep "burung" berbasis robin, bukan penguin) (Rosch 1978). Dua aspek organisasi penting untuk pemanfaatan:

- **Mental cueing (pengisyaratan mental):** tindakan mengorganisasi membuat informasi inheren lebih mudah diingat. Mengingat satu item dalam struktur dapat memicu ingatan item terkait (Baddeley 1997; Craik & Lockhart 1972). Bahkan tanpa akses ke skema organisasi saat pengambilan, organisasi tetap membantu rekoleksi — mis. mencatat secara terstruktur meningkatkan daya ingat meski catatan tidak dipakai saat pengambilan (Kalnikaité & Whittaker 2008a).
- **External cueing (pengisyaratan eksternal):** produk organisasi (nama folder, isi folder) berfungsi sebagai **isyarat pengambilan eksternal**. Pengguna yang hanya mengandalkan search **tidak memiliki** isyarat mental/eksternal ini; mereka harus menghasilkan istilah pencarian dari nol, yang kurang akurat daripada **cued recall**.

Keberhasilan cueing tidak terjamin: memori manusia **bergantung konteks (context dependent)** (Tulving & Thomson 1973). Memilih label/folder menuntut prediksi bagaimana kita akan memikirkan informasi itu saat pengambilan — sulit, karena satu berkas bisa dikategorikan menurut penulis, topik, tanggal, atau proyek. Cara utama mengorganisasi pada sistem operasi adalah menyortir ke kategori (direktori/folder/subfolder) dan memberi label bermakna; folder bertingkat disebut **hierarki (hierarchies)**. Folder juga punya komponen **spasial** kuat (subfolder di dalam folder) yang turut membantu pengambilan (Jones & Dumais 1986).

#### 3.3 Cueing Temporal

Organisasi temporal kurang banyak diteliti namun penting karena banyak informasi bersifat actionable dan harus diproses sebelum tenggat — memunculkan masalah **reminding** (Sellen et al. 1997). Organisasi yang luas pun percuma bila kita lupa tenggatnya. Organisasi temporal juga berguna sebagai isyarat: orang dapat mengambil dokumen dengan mengasosiasikannya pada peristiwa pribadi/publik (**landmark**) yang terjadi dekat waktu pembuatan (Ringel et al. 2003), mirip **memori autobiografis** — orang buruk menentukan waktu absolut tetapi jauh lebih baik menempatkan peristiwa relatif terhadap landmark (Wagenaar 1986). Logfile pengambilan menunjukkan **bias ke informasi sangat baru (recency)**.

#### 3.4 Mengelola Kertas: Filing vs Piling

Malone (1983) mengidentifikasi dua strategi:

- **Filing (memfail):** membangun taksonomi hierarkis menyeluruh, dengan label tiap (sub)kategori dan item terkait-semantik disimpan dalam tiap kategori.
- **Piling (menumpuk):** lebih *laissez-faire*, kurang sistematis, tanpa substruktur; tumpukan lebih sedikit dan lebih besar, item terorganisasi menurut urutan akuisisi, sering untuk informasi actionable dan reminding.

**Trade-off.** Pile lebih mudah dibuat/dipelihara tetapi pengambilan dalam tiap tumpukan kurang efisien; namun karena tumpukan lebih sedikit, lokasi pengambilan juga sedikit (kompensasi). Tumpukan kronologis (terbaru di atas) mendorong **incidental finding** dan reminding, tetapi kertas yang ditaruh untuk pengingat bisa **terkubur** di bawah kertas baru. File memberi struktur dan label lebih koheren saat pengambilan tetapi menuntut usaha pembuatan/pemeliharaan besar dan bisa menjadi terlalu banyak tingkat.

Dalam studi office-move (Whittaker & Hirschberg 2001), peneliti menetapkan **ambang 40 persen** untuk mengklasifikasi seseorang sebagai *filer*. Temuan mengejutkan: **piler justru memiliki arsip lebih kecil** dan menyimpan lebih sedikit setelah pembersihan. Mengapa filer menumpuk lebih banyak? Kemungkinan **premature filing** (memfail prematur) — memasukkan dokumen berkualitas tak pasti ke sistem. Piler juga **mengakses persentase dokumen lebih besar** dalam setahun terakhir: dengan sedikit tumpukan yang sering disibak, informasi berharga naik ke atas. Filer punya lebih banyak data sehingga proporsi yang diakses lebih kecil. Yang menarik, filer **lebih sulit membuang** dokumen yang sudah difail karena investasi yang telah ditanam; informasi tak terfail lebih mudah dibuang.

#### 3.5 Mengelola Berkas dan Folder Digital

Boardman & Sasse (2004): rata-rata **57 folder**, kedalaman **3,3**; **58 persen** orang memfail sistematis saat membuat item, **35 persen** membiarkan banyak item di lokasi default (mirip piling), **6 persen** sebagian besar tak terfail. Namun studi skala besar (Bergman et al. 2010, **296 peserta**) menemukan orang memfail mayoritas berkas ke folder buatan sendiri, menyisakan hanya **12 persen** di folder default (mis. My Documents). Folder sering berfungsi sebagai **rencana (plans)** — struktur untuk mengorganisasi pekerjaan masa depan, mengingatkan tugas/subtugas. Ada pula **promosi informasi** lewat trik penamaan (mis. "aacurrent" agar naik ke atas urutan alfabet) — dibahas lagi di Bab 10. Jones, Phuwanartnurak, et al. (2005) menemukan orang mengorganisasi folder secara **bottom-up ad hoc**: saat menyadari beberapa berkas terkait, mereka membuat subfolder baru.

Alat baru seperti **tagging** memungkinkan banyak label per item (dibahas di Bab 6), tetapi studi lab tidak menemukan manfaat definitif tag dibanding folder.

#### 3.6 Mengelola Surel

Surel kompleks karena banyak pesan actionable. Wawasan kunci: **inbox sering diperlakukan seperti pile** untuk pesan actionable (tetap terlihat demi reminding), sedangkan folder surel untuk pesan informative yang aktif diklasifikasi.

**Pesan actionable.** Penundaan tak terelakkan. Strategi paling lazim (Whittaker & Sidner 1996): **no filing** — meninggalkan pesan di inbox. Sebagian (**25 persen**) mencoba memfail ke folder to-do (*frequent filers*), tetapi **95 persen** folder to-do ditinggalkan karena tidak memberi **opportunistic reminding**. Tang et al. (2008): rata-rata hanya **25 persen** pesan inbox terlihat sekaligus. Strategi ketiga adalah hibrida: **spring cleaning** (**35 persen** pengguna) — membiarkan menumpuk lalu sesekali membereskan besar-besaran. Bälter (2000) mengajukan progresi temporal: dari *frequent filer* → *spring cleaner* → *no filer* seiring meningkatnya volume (yang menerima paling banyak surel punya paling sedikit waktu mengorganisasi).

**Pesan informatif.** Memfail sulit karena membutuhkan usaha besar dan prediksi kebutuhan masa depan. Data Whittaker & Sidner (1996): rata-rata sekitar **39 folder** surel (Whittaker, Bellotti, & Gwizdka 2007); **35 persen** folder hanya memuat **1–2 item** (*failed folders* — terlalu kecil untuk berguna); studi kemudian menemukan angka lebih rendah **16 persen** (Fisher et al. 2006). Semakin banyak folder, semakin mungkin muncul folder gagal. Folder juga bisa gagal karena **terlalu besar** — sulit dipindai, hubungan antar pesan menipis (Bergman et al. 2010). Elsweiler, Baillie, & Ruthven (2008): *frequent filers* justru **mengingat lebih sedikit** tentang pesannya — konsisten dengan premature filing.

#### 3.7 Mengelola Halaman Web

Web umumnya **tidak actionable**. Bentuk pengelolaan lazim adalah **bookmarking**. Abrams et al. (1998): **68 persen** responden punya 11–100 bookmark; Boardman & Sasse (2004): rata-rata **17 folder** bookmark. Aula, Jhaveri, & Kaki (2005): **92 persen** memakai bookmark, rata-rata **220 tautan**, variasi besar (**21 persen** punya <50, **6 persen** tak punya; terbesar **2.589 tautan, 425 folder**). Pengguna berat bookmark (>500 tautan) periodik mereorganisasi (mirip spring cleaner). Abrams et al. mengidentifikasi empat tipe: **~50 persen** sporadic filers, **26 persen** tak pernah mengorganisasi, **~23 persen** membuat folder saat mengakses halaman, **~7 persen** membuat folder di akhir sesi. Folder mulai muncul setelah ambang **~35 bookmark**. Sistem **social tagging** Web 2.0 (Delicious, dll.) mengatasi sebagian biaya: tag dapat dibagi antar pengguna; dengan cukup pengguna, set tag bersama **stabil** pada label konsisten (Golder & Huberman 2006; Millen et al. 2007). Namun manfaat ini bergantung **massa kritis** pengguna.

#### 3.8 Mengelola Foto

Foto cenderung dibuat sendiri, **bukan informative maupun actionable**, melainkan menimbulkan respons **afektif** kuat, dan dianggap sangat penting/tak tergantikan. Namun dikelola dengan struktur **rudimenter** (Whittaker, Bergman, & Clough 2010): sedikit struktur hierarkis, lebih mirip pile daripada file; satu lokasi penyimpanan utama (mis. My Pictures), hierarki datar satu tingkat, folder heterogen. Bukti akses jarang: peserta lebih suka tampilan thumbnail, tetapi saat pengambilan folder muncul dalam tampilan "list" (default) — menandakan folder jarang dibuka. Anotasi foto sangat sedikit karena memberatkan dan karena orang tak sadar bahwa mereka akan lupa detail. Satu peserta merangkum sikapnya: "collect now, organize later, view in the future."

#### 3.9 Perbedaan Individu dan Kepribadian

Perbedaan individu lazim dalam PIM (Gwizdka 2004). Tipe pekerjaan diduga memengaruhi strategi, tetapi hubungannya belum jelas. Massey et al. (2014) menelaah apakah perbedaan management berasal dari **sifat kepribadian**. Studi pertama: peserta diminta menyimpulkan kepribadian seseorang dari tampilan sistem berkasnya — banyak yang menafsirkan folder/subfolder kompleks sebagai tanda kepribadian **Conscientious (teliti/cermat)**; isyarat ini ternyata cukup akurat. Studi kedua mengukur langsung relasi struktur sistem berkas dengan **Big Five** (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism — John 1990): **Conscientiousness memprediksi organisasi berkas** (orang teliti lebih sedikit menaruh berkas tak terorganisasi di desktop), sedangkan orang **Neurotic** menyimpan lebih banyak berkas tak terorganisasi (dan mungkin lebih banyak berkas) di desktop.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Semantic organization | Organisasi semantik; menata berdasarkan kemiripan konsep. |
| Temporal organization | Organisasi temporal; menata berdasarkan waktu/proses. |
| Mental cueing / External cueing | Pengisyaratan mental (memori) / eksternal (label, isi folder). |
| Filing / Piling | Memfail (hierarkis sistematis) / menumpuk (laissez-faire). |
| Premature filing | Memfail prematur; memfail item sebelum nilainya jelas. |
| No filing / Frequent filing / Spring cleaning | Tanpa memfail / sering memfail / bersih-bersih berkala (strategi surel). |
| Failed folder | Folder gagal; folder yang hanya memuat 1–2 item. |
| Opportunistic reminding | Pengingatan oportunistik; teringat tanpa sengaja saat melihat inbox. |
| Social tagging | Penandaan sosial; tag yang dibagikan antar pengguna. |
| Big Five | Lima dimensi kepribadian; di sini Conscientiousness & Neuroticism relevan. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 3.1 — Filer vs Piler di kantor.** Bu Sari memfail tiap dokumen ke subfolder rapi; Pak Tono membiarkan dokumen menumpuk di desktop. Sesuai temuan Whittaker & Hirschberg (2001), Pak Tono (piler) ternyata punya arsip lebih kecil dan lebih sering menyibak dokumennya, sedangkan Bu Sari enggan membuang dokumen yang sudah ia fail karena merasa "sudah terlanjur ditata".
>
> **Studi kasus 3.2 — Folder gagal mahasiswa.** Doni membuat folder terpisah untuk tiap mata kuliah, banyak yang hanya berisi satu-dua berkas — contoh *failed folders* (35% menurut Whittaker & Sidner). Ia juga membuat folder `aaaSKRIPSI` agar selalu muncul paling atas — contoh promosi informasi (Bab 10).

### Temuan Penelitian (dari Buku Sumber)

- Sepanjang 50 tahun: ~**100.000** dokumen, **440.000** surel, **120.000** foto disimpan aktif.
- Folder berkas baru tiap **3 hari**, folder surel baru tiap **5 hari** (Boardman & Sasse 2004).
- **42%** bookmark tak pernah diakses; **10%** waktu surel untuk memfail.
- Berkas: **57** folder, kedalaman **3,3**; hanya **12%** berkas di folder default (Bergman et al. 2010).
- Surel: no filing dominan; frequent filers **25%** (folder to-do ditinggalkan **95%**); spring cleaning **35%**; failed folders **35%** (kemudian **16%**); rata-rata **~39** folder.
- Bookmark: **92%** memakai, rata-rata **220** tautan; ambang folder **~35**.
- Foto: struktur rudimenter, mirip pile.
- Kepribadian: **Conscientiousness** memprediksi keteraturan; **Neuroticism** terkait desktop tak teratur.

### Rangkuman

- Management sulit karena menuntut prediksi konteks pengambilan masa depan.
- Organisasi semantik bekerja lewat mental & external cueing; organisasi temporal mendukung reminding.
- Filing dan piling punya trade-off; piling efektif untuk koleksi kecil, filing rentan premature filing dan folder gagal.
- Surel dikelola via no filing/frequent filing/spring cleaning; inbox berfungsi seperti pile untuk item actionable.
- Perbedaan individu dan kepribadian (terutama Conscientiousness & Neuroticism) memengaruhi strategi.

### Latihan & Refleksi

**A. Pemahaman**
1. Jelaskan beda mental cueing dan external cueing.
2. Sebutkan tiga strategi pengelolaan surel dan ciri masing-masing.
3. Apa yang dimaksud "failed folder" dan berapa persentasenya menurut Whittaker & Sidner (1996)?

**B. Analisis (HOTS)**
4. Mengapa piler dalam studi office-move justru memiliki arsip lebih kecil dan mengakses lebih banyak dokumen? Susun penjelasan kausalnya.
5. Folder dapat gagal karena terlalu besar maupun terlalu kecil. Rancang satu pedoman praktis untuk menghindari keduanya (kaitkan dengan heuristik yang akan dibahas di Bab 4).
6. Mengapa pengguna yang hanya mengandalkan search kehilangan keuntungan kognitif dibanding yang mengorganisasi folder? Hubungkan dengan konsep cued recall.

**C. Tugas Praktik**
7. Petakan sistem surel Anda: hitung jumlah folder, persentase folder berisi ≤2 item, dan estimasi waktu yang Anda habiskan memfail per minggu. Klasifikasikan diri Anda (no filer/frequent filer/spring cleaner) dan jelaskan alasannya.

---

## Bab 4 — Pemanfaatan (Exploitation)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membedakan** exploitation dari information seeking/foraging klasik.
2. **Menjelaskan** metode penelitian EPIR beserta kelebihan dan keterbatasannya.
3. **Menghitung** dan **menafsirkan** trade-off kedalaman vs ukuran folder (heuristik 21 item).
4. **Menganalisis** temuan pengambilan untuk berkas, surel, foto, dan web.
5. **Mengevaluasi** apakah strategi preparatory (foldering) lebih unggul daripada strategi oportunistik.

### Peta Konsep

```
EXPLOITATION = mengambil kembali informasi (jantung kurasi)
        |
   Berbeda dari foraging/seeking: target FAMILIAR & subjektif, dimediasi cueing
        |
   Metode riset: EPIR (elicited personal information retrieval)
        |
   Berkas: 94% sukses, 14,76 dtk; depth 2,86; 11,82 item/folder
       -> heuristik: jangan >21 item per folder
   Surel: scroll 62%, search 18%, folder 13%, sort 6%; high filer TIDAK lebih sukses
   Foto: sukses hanya 61% (lama); trial-and-error
   Web: akses-ulang dominan; link/back > search; recency kuat
```

### Materi Inti

#### 4.1 Exploitation vs Foraging/Seeking

Exploitation berbeda dari **information foraging** (Pirolli & Card 1995) dan **information seeking** (Belkin 1980; Marchionini 1995) yang menargetkan informasi **baru**. Pemanfaatan informasi pribadi yang **familiar** berbeda: (1) struktur pengambilan **diorganisasi subjektif**, bukan publik; (2) pengeksploitasi sering **mengingat detail** signifikan tentang target dan organisasinya. Orang memang mengingat banyak hal tentang dokumen pribadi: Gonçalves & Jorge (2004) menemukan karakteristik paling menonjol adalah **usia, lokasi, dan tujuan** dokumen; Blanc-Brude & Scapin (2007) menemukan lokasi, format, usia, kata kunci, dan peristiwa terkait sering diingat. Karena itu, akses tidak murni bergantung pada metadata publik (*scent* dalam istilah information foraging), melainkan dimediasi **cueing** (mental/eksternal). Pengambilan menggunakan dua strategi utama: **navigasi** (traversal manual + pemindaian visual dalam hierarki folder) dan **search**.

#### 4.2 Metode Penelitian: EPIR

Eksperimen lab konvensional unggul dalam kontrol variabel tetapi lemah **validitas ekologis** karena memakai item buatan, sementara dalam PIM pengguna sangat akrab dengan item dan organisasinya sendiri. Para penulis mengembangkan teknik **Elicited Personal Information Retrieval (EPIR)**: penguji meminta peserta mengambil **berkas dari koleksi pribadinya sendiri di komputernya sendiri**, sambil penguji menginisiasi pengambilan dan merekam layar untuk mengukur efisiensi dan keberhasilan. EPIR mempertahankan keunggulan eksperimen terkontrol sekaligus meningkatkan validitas ekologis. Keterbatasannya: pengambilan dipicu dengan menyebut nama berkas, bukan konteks kerja yang lebih luas. Alternatif lebih naturalistik (diari, logfile) punya masalah masing-masing (validitas eksternal kecil, kesulitan teknis/privasi).

#### 4.3 Mengakses Berkas: Studi Skala Besar dan Heuristik 21 Item

Bergman et al. (2010) meminta **296 peserta** mengambil **1.131 berkas aktif** dan menganalisis **5.035 langkah navigasi**, dimulai dari desktop dan direkam. Temuan struktur:

- Hierarki **dangkal**: berkas aktif diambil dari kedalaman rata-rata **2,86 folder**.
- Folder relatif **kecil**: rata-rata **11,82 berkas per folder** dengan rata-rata **10,64 subfolder**.
- Navigasi **berhasil dan efisien**: **94 persen** berkas berhasil diakses dalam rata-rata **14,76 detik**.

Regresi linear menghasilkan model trade-off **kedalaman vs ukuran folder**:

- Tiap langkah folder tambahan menambah waktu pengambilan **2,236 detik**.
- Tiap item tambahan dalam folder menambah **0,106 detik**.
- Rasio: **2,236 / 0,106 = 21,09**.

> **Prinsip kunci (heuristik dari buku sumber).**
> Satu langkah turun hierarki setara dengan memindai sekitar **21 item** dalam hal pengaruhnya pada waktu pengambilan. Maka, sebagai heuristik, **hindari menyimpan lebih dari 21 item per folder**; lebih baik buat satu tingkat subfolder tambahan.

Studi terkait (Bergman, Whittaker, et al. 2012) menemukan perbedaan waktu pengambilan Mac vs PC berasal dari **strategi organisasi** (pengguna Mac membuat hierarki lebih dangkal), bukan desain antarmuka; dan tampilan default Windows **suboptimal** — pengambilan tercepat ketika tampilan default menunjukkan **ikon**.

#### 4.4 Mengakses Surel: Preparatory vs Opportunistic

Studi naturalistik paling sistematis (Whittaker et al. 2011) membandingkan dua strategi pada **345 pengguna jangka panjang**, menganalisis **lebih dari 85.000 tindakan refinding**:

- **Preparatory retrieval:** memanfaatkan folder yang diorganisasi subjektif (akses folder).
- **Opportunistic retrieval:** scrolling, sorting, searching tanpa bergantung struktur sebelumnya.

Tindakan dicatat: folder access, sort, scroll (>1 detik), search. Sukses didefinisikan otomatis: membuka pesan target lalu membalas atau membaca lama. Temuan:

| Tindakan pengambilan surel | Proporsi |
|---|---|
| Scroll inbox | **62%** |
| Search | **18%** |
| Folder access | **13%** |
| Sort | **6%** |

Strategi **oportunistik lebih lazim** daripada foldering. *High filers* (proporsi surel di folder lebih tinggi) memang lebih mengandalkan folder (**16 persen** vs **7 persen** bagi *low filers*) dan memakai **lebih sedikit operasi** per urutan pencarian, **tetapi**: urutan pencarian mereka **sedikit lebih lama** (karena akses folder lebih lambat daripada search/sort), dan — bertentangan dengan ekspektasi — **tidak lebih berhasil** menemukan pesan dibanding low filers. Kesimpulan penting: perilaku preparatory (memfail rumit) **kurang efisien** dan **tidak meningkatkan keberhasilan**; perilaku oportunistik lebih cepat dan sama suksesnya.

Tentang memori surel, Elsweiler, Baillie, & Ruthven (2008): orang mengingat konten/tujuan/tugas terbaik (>**80 persen** benar meski pesan berbulan-bulan), kurang baik mengingat **pengirim** (cepat terlupa), dan paling buruk **informasi temporal** (turun ke **~50 persen**). Sebaliknya, Dumais et al. (2003) dengan sistem **Stuff I've Seen (SIS)** menemukan **74 persen** pencarian berfokus pada surel, dengan bias kebaruan kuat (**21 persen** item dari minggu terakhir, **~50 persen** dari bulan terakhir) dan **25 persen** menyertakan nama pengirim — perbedaan ini sebagian karena SIS mengamati perilaku naturalistik berfokus pesan baru.

#### 4.5 Mengakses Foto: Kegagalan untuk Materi Lama

Foto sangat dihargai, tetapi akses foto **lama** problematik. Dengan varian EPIR, peserta diminta menyebut peristiwa keluarga penting >1 tahun lalu lalu menunjukkan fotonya. Hasil: berhasil hanya pada **61 persen** tugas; pada **39 persen** sisanya peserta tak dapat menemukan foto. Dari kegagalan itu, **75 persen** melibatkan foto yang diyakini ada di komputer/CD tetapi tak ditemukan. Beberapa penyebab teridentifikasi: menyimpan terlalu banyak foto, penyimpanan tersebar di banyak perangkat, organisasi tidak sistematis, **false familiarity** (rasa akrab semu), dan kurangnya pemeliharaan. **67 persen** peserta berusaha memberi label, tetapi pelabelan tidak menjamin keberhasilan (skema penamaan tidak konsisten, makna label terlupa). Peserta yang konsisten memakai nama folder berbasis waktu (mis. "Spring13") **lebih berhasil** — meski hanya minoritas memakainya. Strategi pengambilan umum: **trial and error** menyibak seluruh koleksi.

#### 4.6 Mengakses Web: Akses-Ulang dan Kebaruan

Intuisi umum keliru: orang mengira akses web didominasi **search** dan **foraging**. Faktanya **akses-ulang (reaccess)** mendominasi, lewat mengikuti tautan, mengetik ulang URL, atau tombol Back. Awalnya web diakses lewat taksonomi buatan manusia (mis. Yahoo!), tetapi infeasible untuk miliaran dokumen sekarang. Temuan logfile:

- **Hub-and-spoke**: menemukan sumber otoritatif (hub), lalu menyebar ke tautan (spoke), biasanya kembali via Back (Catledge & Pitkow 1995).
- Tingkat **recurrence 58 persen** (Tauscher & Greenberg 1997); tombol Back **~30 persen** seluruh aksi web; Cockburn & Greenberg (2000) menemukan revisits **81 persen**.
- Wen (2003): keberhasilan akses-ulang hanya **20 persen**.
- Obendorf et al. (2007) mengontrol refresh otomatis → revisit **41 persen**. Strategi akses umum: hyperlink **44 persen**, formulir/mesin pencari **15 persen**, Back **14 persen**, tab/jendela baru **11 persen**, ketik URL **9 persen**. Untuk revisits: tautan **50 persen**, Back **31 persen**. Efek kebaruan besar: **73 persen** revisits dalam satu jam (50 persen dalam tiga menit).

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Information foraging / seeking | Pencarian/penjelajahan informasi baru (publik). |
| Ecological validity | Validitas ekologis; sejauh mana studi mencerminkan kondisi nyata. |
| EPIR | Elicited Personal Information Retrieval; metode pengambilan item pribadi terkendali. |
| Preparatory vs Opportunistic retrieval | Pengambilan persiapan (folder) vs oportunistik (scroll/sort/search). |
| High/Low filer | Pengguna dengan proporsi surel terfail tinggi/rendah. |
| False familiarity | Rasa akrab semu terhadap koleksi yang sebenarnya jarang diakses. |
| Hub-and-spoke | Pola akses web pusat-jari-jari. |
| Recurrence/Revisit rate | Tingkat akses-ulang halaman web. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 4.1 — Heuristik 21 item.** Maya menyimpan 150 berkas dalam satu folder `Tugas`. Berdasarkan heuristik buku sumber (maks ~21 item/folder), ia membagi menjadi subfolder per mata kuliah. Waktu pengambilannya turun karena trade-off depth-vs-size kini optimal.
>
> **Studi kasus 4.2 — Inbox Pak Hadi.** Pak Hadi rajin memfail surel ke puluhan folder (high filer), tetapi tetap sering men-scroll inbox saat mencari. Sesuai Whittaker et al. (2011), foldering-nya tidak membuatnya lebih sukses—hanya menambah usaha awal.

### Temuan Penelitian (dari Buku Sumber)

- Berkas (Bergman et al. 2010): sukses **94%**, waktu **14,76 dtk**, depth **2,86**, **11,82** item/folder, **10,64** subfolder; heuristik **≤21 item/folder** (rasio 2,236/0,106).
- Tampilan **ikon** default tercepat; pengguna Mac lebih dangkal.
- Surel (Whittaker et al. 2011): scroll **62%**, search **18%**, folder **13%**, sort **6%**; high filer **tidak** lebih sukses.
- Memori surel (Elsweiler et al. 2008): konten/tujuan **>80%**, pengirim cepat lupa, temporal **~50%**.
- SIS (Dumais et al. 2003): **74%** pencarian pada surel; **25%** menyertakan nama pengirim; bias kebaruan.
- Foto: sukses lama hanya **61%**; **67%** memberi label tetapi tak menjamin; nama folder berbasis waktu lebih berhasil.
- Web: recurrence **58%/81%**; Back **~30%**; Obendorf revisit **41%**; reaccess sukses **20%** (Wen).

### Rangkuman

- Exploitation memanfaatkan informasi familiar yang diorganisasi subjektif, dimediasi cueing.
- EPIR menyeimbangkan kontrol eksperimen dan validitas ekologis.
- Navigasi berkas sangat berhasil (94%) dan efisien; heuristik praktis: maksimal ~21 item per folder.
- Untuk surel, strategi oportunistik (scroll/search) lebih lazim dan tidak kalah sukses dari foldering.
- Foto lama sulit diakses (sukses hanya 61%); web didominasi akses-ulang dengan bias kebaruan.

### Latihan & Refleksi

**A. Pemahaman**
1. Apa keunggulan dan keterbatasan metode EPIR?
2. Jelaskan arti angka 2,236 dan 0,106 dalam model regresi Bergman et al. (2010).
3. Sebutkan empat tindakan refinding surel beserta proporsinya.

**B. Analisis (HOTS)**
4. Buktikan secara aritmetika asal heuristik "21 item per folder" dan jelaskan kapan heuristik ini bisa menyesatkan.
5. Mengapa high filers tidak lebih sukses meski berinvestasi memfail? Apa implikasinya bagi nasihat populer "rapikan inbox Anda"?
6. Foto lama sulit diambil sementara surel relatif mudah. Bandingkan penyebabnya dari sisi cueing dan frekuensi akses.

**C. Tugas Praktik**
7. Pilih satu folder berisi >21 item. Ukur waktu Anda menemukan satu berkas target. Pecah folder itu menjadi subfolder ≤21 item, lalu ukur ulang. Laporkan selisih waktu dan refleksi singkat.

---

## Rangkuman Bagian I

Bagian I berargumen bahwa intuisi yang berlaku tentang perilaku informasi tidaklah akurat: manusia bukan semata konsumen informasi publik baru, melainkan **kurator** yang menyimpan dan mengelola informasi pribadi berharga untuk akses masa depan. Kurasi adalah **komunikasi terarah-diri**, memanfaatkan atribut subjektif yang dapat dipahami "diri masa depan" pengguna.

Model **tiga tahap** (keeping, management, exploitation) dijabarkan beserta keterkaitannya. Secara umum pengguna **overkeep** (kecuali kontak berharga dan halaman web). Pengelolaan menunjukkan manfaat baik pada pile maupun file, tetapi mengorganisasi informasi actionable tetap menjadi tantangan besar. Pemanfaatan tetap bertumpu pada metode manual (navigasi) meski search desktop telah hadir. Baik keeping maupun management menuntut prediksi masa depan — informasi apa yang dibutuhkan dan bagaimana kita akan memikirkannya.

Masalah kurasi kian mendesak seiring pertumbuhan arsip pribadi. Telah diargumentasikan bahwa folder dianggap usang dan punya batasan teknis, sehingga muncul usulan teknologi pengganti — yang akan ditinjau di **Bagian II**. Namun, seperti akan ditunjukkan, terdapat sedikit dukungan empiris untuk mengganti folder yang diorganisasi subjektif dengan teknologi-teknologi baru tersebut; Bab 8 akan memberi alasan kognitif dan neurologisnya.

---

# BAGIAN II — Folder Hierarkis dan Alternatifnya

## Pengantar Bagian II

Meski usulan teknologi baru untuk PIM terus bermunculan, **folder** tetap menjadi cara utama orang mengelola dan mengambil informasi pribadinya. Saat memakai folder, orang pertama-tama menemukan/membuat folder yang mencirikan sebuah butir, lalu mengambilnya dengan menavigasi secara manual. Istilah *folder* berasal dari map kertas — wadah fisik berisi dokumen sekategori, dengan nama kategori ditulis di punggungnya. Folder virtual juga bernama dan dapat memuat **subfolder**, membentuk **hierarki folder (folder hierarchy)**.

Sejarah teknisnya: sistem operasi pertama yang memungkinkan penyimpanan personal lewat **direktori hierarkis** adalah **Multics** (pertengahan 1960-an); struktur ini lalu diterapkan pada Unix/Linux. Metafora lokasi makin jelas dengan **folder digital** pada **Xerox Star (1981)** — folder virtual adalah metafora visual untuk lokasi (item tampak "di dalam" folder, bisa di-*drag-and-drop*). Metafora ini lalu diadopsi Apple (Mac) dan Microsoft (Windows). Maka penyimpanan berbasis lokasi telah dipakai hampir tanpa modifikasi, terus-menerus, dan nyaris eksklusif selama beberapa dekade.

Sepanjang sejarahnya, metode hierarkis dikritik: (1) mengklasifikasi dapat **menyembunyikan** item dari pengguna (mengurangi reminding visual); (2) tindakan mengategorikan **menantang secara kognitif** karena item tidak selalu pas dalam satu folder; (3) yang terpenting, Lansdale (1988) berargumen bahwa folder hierarkis **memaksa** penyimpanan satu lokasi padahal item bisa termasuk beberapa kategori, sehingga memaksa pengguna mengingat lokasi persis saat pengambilan — sulit bila jeda waktu lama.

Kritik ini melahirkan tiga alternatif utama yang dibandingkan dengan folder di Bab 5–7: **search** (pencarian), **tags** (penandaan), dan **group classification** (klasifikasi kelompok/GIM). Setiap bab berbasis studi multi-metode skala besar para penulis. Hasilnya memunculkan **paradoks**: mengapa pengguna bertahan dengan folder padahal folder tampak punya banyak batasan intuitif? Jawabannya diberikan di **Bab 8**, yang menawarkan penjelasan kognitif dan neurologis.

---

## Bab 5 — Alternatif Pencarian (The Search Alternative)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** klaim pendekatan "search everything" untuk retrieval dan management.
2. **Menguraikan** tiga inovasi mesin pencari desktop modern (user-centered, incremental, cross-format).
3. **Menjelaskan** desain dua studi (Windows & Mac) Bergman et al. (2008).
4. **Menafsirkan** temuan bahwa preferensi navigasi bertahan terlepas dari kualitas mesin pencari.
5. **Mengevaluasi** metafora "search sebagai fire escape" (tangga darurat).

### Peta Konsep

```
SEARCH EVERYTHING: search akan menggantikan navigasi & meniadakan kebutuhan organisasi
        |
   Big leap mesin pencari: real-time index (1000x lebih cepat)
   -> user-centered, incremental search, cross-format
        |
   STUDI Bergman et al. (2008):
   - Windows (longitudinal, within-subjects, n=47)
   - Mac (cross-sectional, between-subjects, n=589)
        |
   HASIL: navigasi 56-68%, search hanya 7-15%
   - Windows: 7%->15% (3 minggu) -> 10% (7 bulan), tidak signifikan
   - Mac: tidak ada kenaikan sama sekali
        |
   KESIMPULAN: preferensi navigasi tidak bergantung kualitas mesin pencari
   Search = "fire escape" (pilihan terakhir, ~25% upper limit)
```

### Materi Inti

#### 5.1 Pendekatan "Search Everything"

Navigasi adalah proses dua fase (traversal hierarki + pindai isi folder); search adalah membuat kueri atribut target lalu memilih dari hasil. Pandangan yang lazim: search **lebih sederhana dan efisien**, dan sedang menggantikan navigasi (Russell & Lawrence 2007; Cutrell, Dumais, & Teevan 2006). Keunggulan intuitif search: **fleksibel** (tak perlu ingat lokasi), **efisien** (satu kueri vs banyak langkah navigasi), dan **meniadakan kebutuhan organisasi**. Argumen ini diperkuat tren web (navigasi taksonomi Yahoo! tergantikan search). Sejumlah peneliti karenanya mengusulkan mesin pencari menggantikan folder, tercermin pada judul-judul seperti *Searching to Eliminate Personal Information Management* (Cutrell et al. 2006) dan *Search Everything* (Russell & Lawrence 2007), serta sistem eksperimental: Phlat, SIS, Haystack, Placeless Documents, Lifestreams, MyLifeBits, iMeMex. Sebagian sistem ini menawarkan pendekatan hibrida; sebagian lain radikal menghapus penyimpanan berbasis folder.

#### 5.2 Lompatan Besar Mesin Pencari Desktop

Fertig, Freeman, & Gelernter (1996a) dahulu berargumen preferensi navigasi muncul karena **keterbatasan teknologi search** (mesin pencari saat itu lambat, hanya nama berkas, tanpa pengindeksan inkremental). Buku sumber mencatat bahwa peningkatan yang mereka antisipasi kini terwujud. Inovasi kunci: **indeks real-time** yang terus diperbarui (mis. Google Desktop, Apple Spotlight), membuat mesin pencari modern **seribu kali lebih cepat** daripada generasi lama pada komputer yang sama. Kecepatan ini memungkinkan tiga peningkatan:

1. **Desain berpusat-pengguna (user-centered):** mengurangi langkah dan kerumitan definisi kueri (tak perlu memilih nama berkas vs teks penuh, dsb.).
2. **Pencarian inkremental (incremental search):** pencarian mulai sejak karakter pertama; pengguna mendapat umpan balik konstan, bisa mengoreksi ejaan, dan berhenti begitu target tampak (Raskin 2000).
3. **Pencarian lintas-format (cross-format search):** mengikuti SIS (Dumais et al. 2003), satu kueri mengambil berkas, surel, pesan, dan riwayat web — mengatasi **project fragmentation problem** (dibahas di Bab 11).

#### 5.3 Desain Studi (Bergman et al. 2008)

Karena "search everything" berakar pada intuisi peneliti, evaluasinya menuntut desain **multi-metode** agar hasil tidak spesifik pada satu mesin pencari/metode. Dua studi komplementer dijalankan:

- **Studi Windows (longitudinal, within-subjects):** Google Desktop dipasang pada komputer **47** pengguna Windows XP yang sebelumnya memakai Windows Search Companion. Peserta dilatih dan didorong memakai search, lalu mengisi kuesioner kebiasaan pengambilan **tiga kali**: sebelum instalasi, setelah **tiga minggu** penggunaan, dan **tujuh bulan** kemudian.
- **Studi Mac (cross-sectional, between-subjects):** membandingkan **519** pengguna Mac OS X 10.4 dengan Spotlight (lebih canggih) vs **70** pengguna Mac OS 10.0–10.3 dengan Sherlock (lebih lama). Total **589** peserta. Desain antar-subjek mencegah peserta menebak tujuan studi.

Kuesioner sama meminta peserta mengestimasi frekuensi tiap opsi pengambilan (search, navigasi, recent documents, shortcut desktop, plus Smart Folders untuk Mac) sebagai persentase. Estimasi divalidasi terhadap perilaku nyata di dua prastudi — korelasinya **sangat tinggi** (persentase search sedikit di-*overestimate*), menandakan estimasi pengguna valid.

#### 5.4 Hasil: Navigasi Bertahan Apa Pun Kualitas Mesin Pencari

> **Temuan inti.** Terdapat preferensi kuat untuk **navigasi**. Pengguna mengestimasi memakai navigasi untuk **mayoritas** pengambilan (**56–68 persen**). Persentase search jauh lebih rendah: **11–15 persen** (Google Desktop, Sherlock, Spotlight) dan **7 persen** (Windows Search Companion, mungkin karena opsi search kurang terlihat).

- **Studi Windows:** instalasi Google Desktop menaikkan search dari **7 persen** menjadi **15 persen** setelah tiga minggu, tetapi **tujuh bulan** kemudian turun ke **10 persen** — **tidak signifikan** lebih tinggi dari baseline.
- **Studi Mac:** **tidak ada kenaikan** search sama sekali saat memakai mesin pencari yang lebih baik.

Persentase search **stabil** dan tidak dipengaruhi usia, lama penggunaan komputer, pengalaman, atau jam pemakaian harian. Studi lanjutan (Blau, Madmon, & Bergman 2013) menemukan persentase search **tidak dipengaruhi literasi komputer** — pakar tidak lebih sering memakai search daripada pemula.

Pengguna juga **mengingat lokasi** sebagian besar berkas: mereka mengestimasi mengingat lokasi persis **74–90 persen** berkas. Persentase berkas yang lokasinya tak diingat — semacam **batas atas (upper limit)** penggunaan search — diperkirakan sekitar **25 persen**, dan tidak terpengaruh mesin pencari yang lebih baik. Bahkan saat lokasi tak diingat, pengguna sering tetap memilih cara lain ketimbang search. Untuk klaim management, hanya **12 dari 481** pengguna Spotlight melaporkan menjadi kurang terorganisasi karena search; **12** lainnya justru menjadi lebih terorganisasi — tak ada bukti search membuat orang lebih ceroboh mengorganisasi.

#### 5.5 Search sebagai "Tangga Darurat"

Buku sumber menyimpulkan: preferensi navigasi atas search **tak bergantung** pada kualitas mesin pencari. Ini **tidak** berarti memperbaiki mesin pencari sia-sia — jika search adalah **"fire escape" (tangga darurat)** PIM yang dipakai sebagai pilihan terakhir, maka saat darurat (lupa lokasi) pengguna tentu ingin tangga darurat terbaik. Namun tidak ada bukti bahwa yang menghalangi penggunaan search adalah sifat "primitif" mesin pencari saat ini. Tantangan yang lebih realistis bagi pengembang: mendukung search untuk **~25 persen** berkas yang lokasinya tak diingat pengguna. Bab 8 mengeksplorasi alasan kognitif preferensi navigasi.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Search everything | Pendekatan yang mengklaim search akan menggantikan navigasi dan organisasi. |
| Real-time index | Indeks waktu-nyata yang terus diperbarui. |
| Incremental search | Pencarian inkremental; mulai sejak karakter pertama. |
| Cross-format search | Pencarian lintas-format (berkas, surel, web sekaligus). |
| Within-subjects / Between-subjects | Desain dalam-subjek (orang sama dibandingkan) / antar-subjek (kelompok berbeda). |
| Longitudinal / Cross-sectional | Studi memanjang (lintas waktu) / melintang (satu titik waktu). |
| Upper limit (of search) | Batas atas penggunaan search (~25%, item yang lokasinya tak diingat). |
| Fire escape (metafora) | Tangga darurat; search sebagai pilihan terakhir. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 5.1 — "Kenapa tidak search saja?"** Seorang dosen TI menyarankan mahasiswa berhenti merapikan folder dan "cukup search". Sesuai temuan Bergman et al. (2008), setelah beberapa minggu mahasiswa kembali ke navigasi: mereka mengingat lokasi ~74–90% berkasnya dan hanya memakai search saat benar-benar lupa (~25% kasus). Search berfungsi sebagai tangga darurat, bukan pintu utama.

### Temuan Penelitian (dari Buku Sumber)

- Navigasi **56–68%** pengambilan; search **11–15%** (mesin canggih) / **7%** (Windows Search Companion).
- Windows: search **7%→15%** (3 minggu) **→10%** (7 bulan), tidak signifikan.
- Mac (n=589): **tidak ada** kenaikan search.
- Persentase search stabil; tak dipengaruhi usia/pengalaman/literasi komputer (Blau et al. 2013).
- Lokasi berkas diingat **74–90%**; batas atas search **~25%**.
- Hanya **12/481** Spotlight users kurang terorganisasi (12 lain lebih terorganisasi).

### Rangkuman

- Pendekatan "search everything" mengklaim search lebih fleksibel/efisien dan meniadakan organisasi.
- Mesin pencari modern jauh lebih baik (indeks real-time, inkremental, lintas-format), tetapi preferensi navigasi bertahan.
- Dua studi multi-metode menunjukkan navigasi 56–68% vs search 7–15%, tanpa kenaikan berarti meski mesin diperbaiki.
- Search berperan sebagai tangga darurat untuk ~25% berkas yang lokasinya tak diingat.

### Latihan & Refleksi

**A. Pemahaman**
1. Sebutkan tiga klaim pendekatan "search everything".
2. Apa perbedaan desain within-subjects dan between-subjects dalam dua studi Bergman et al. (2008)?
3. Berapa persentase navigasi dan search yang ditemukan, dan apa "batas atas" penggunaan search?

**B. Analisis (HOTS)**
4. Studi Windows menunjukkan lonjakan sementara (7%→15%) lalu turun (→10%). Mengapa pola "naik lalu turun" ini penting untuk membantah klaim search everything?
5. Evaluasi metafora "fire escape". Apakah metafora ini mendukung atau menolak investasi pada mesin pencari yang lebih baik? Jelaskan.
6. Mengapa fakta bahwa literasi komputer tidak memengaruhi persentase search memperkuat argumen bahwa preferensi navigasi bersifat mendasar (bukan sekadar kebiasaan pemula)?

**C. Tugas Praktik**
7. Selama dua hari, hitung berapa kali Anda mengambil berkas via navigasi vs search. Hitung persentasenya dan bandingkan dengan rentang 56–68% (navigasi) dari buku sumber. Diskusikan apakah pola Anda konsisten dengan temuan tersebut.

---

## Bab 6 — Alternatif Penandaan (The Tagging Alternative)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** dua argumen utama keunggulan tag atas folder (multiple classification & no hierarchy).
2. **Membedakan** tag-label dan folder-label pada Gmail.
3. **Menafsirkan** hasil studi Bergman et al. (2013a) tentang preferensi folder vs tag.
4. **Menganalisis** mengapa pengguna lebih memilih single classification daripada multiple.
5. **Mengevaluasi** klaim bahwa tag "lebih kompatibel dengan kognisi manusia".

### Peta Konsep

```
TAG EVERYTHING: tag unggul karena (1) multiple classification (2) no hierarchy
        |
   Kritik folder: single classification + lokasi tersembunyi (Malone, Lansdale)
        |
   Tag di sistem PIM: Delicious (web), Gmail labels, Windows Vista+
        |
   STUDI Bergman et al. (2013a): Gmail (n=23) + Windows 7 (n=23), naturalistik
        |
   HASIL: preferensi kuat FOLDER
   - Gmail: folder-label 67% vs tag-label 33%; single 92% vs multiple 8%
   - Windows 7: 96% di folder spesifik; hanya 16% pakai tag
   - Navigasi 61-69%; tag retrieval 3-5%; multiple classification ~0
        |
   Tag bermanfaat untuk Web 2.0 (sosial), bukan PIM (familiar dengan koleksi sendiri)
```

### Materi Inti

#### 6.1 Dua Argumen "Tag Everything"

Tagging kerap diusulkan sebagai alternatif folder dengan dua keunggulan:

1. **Multiple classification (klasifikasi ganda):** dalam folder, satu item hanya disimpan di satu folder, padahal pengguna bisa memikirkan beberapa klasifikasi (mis. foto konferensi di Kopenhagen bisa masuk Pictures, Trips, Conferences, atau Copenhagen). Tag memungkinkan **berapa pun label** dipasang dan dipakai untuk pengambilan.
2. **No hierarchical location (tanpa lokasi hierarkis):** folder dapat menyembunyikan item; tagging menghapus hierarki/lokasi — semua item dalam **satu repositori datar**, diambil lewat tag search, tag selection, atau tag cloud.

Kritik folder yang mendasarinya: **single classification** menantang secara kognitif dan harus mengantisipasi penggunaan masa depan (Lansdale 1988: "menempatkan dokumen pada satu kategori menaruh informasi di luar jangkauan bila pengambilan dibutuhkan untuk alasan lain"); dan **metafora lokasi** membuat dokumen yang difail kehilangan fungsi reminding (Malone 1983).

#### 6.2 Tag, Web 2.0, dan Sistem PIM Saat Ini

Revolusi **Web 2.0** (pengguna berbagi konten) sangat memengaruhi adopsi tag. Situs seperti Flickr dan YouTube memungkinkan unggah konten beserta tag agar orang lain bisa mencarinya. Furnas et al. (2006) mengaitkan keberhasilan tagging dengan **aspek sosial**: berbagi tag membantu penemuan dan pengambilan, mengatasi **vocabulary problem** (orang berbeda memakai istilah berbeda untuk hal sama). Namun, seperti ditegaskan di Bagian I, keunggulan sosial ini **hanya berlaku** di setting sosial dengan banyak tag berbagi; manfaatnya **lenyap** bila tag dipakai untuk PIM individual (Pak, Pautz, & Iden 2007).

Tag kini terintegrasi ke sistem PIM:

- **Web favorites:** Delicious — bookmarking berbasis tag (sekaligus PIM dan Web 2.0).
- **Surel — Gmail labels (2004):** awalnya hanya sebagai **tag-label** (banyak label per surel, tetap di inbox = multiple classification). Sejak **2009**, label juga bisa sebagai **folder-label** (surel di-*drag* "ke dalam" label, hilang dari inbox, hanya satu label = single classification). Maka pengguna Gmail punya dua cara: tag-labeling vs folder-labeling.
- **Berkas — Windows Vista (dan 7/8/10):** tag berdampingan dengan hierarki folder; berkas bisa diberi banyak tag dan diambil via search, navigasi (sortir per tag), atau "arrange by".

#### 6.3 Sikap vs Perilaku

Bergman et al. (2013b) menguji **sikap**: dari **168** peserta, **77 persen** menganggap "memberi beberapa klasifikasi" ide bagus, **72 persen** setuju "dalam 20 tahun anak-anak akan kebanyakan memakai tag", dan **61 persen** setuju "kebanyakan orang memakai folder hanya karena kebiasaan". Jadi secara hipotetis pengguna **setuju** dengan pendukung tag everything. Tetapi bagaimana **perilaku** nyatanya?

Tinjauan studi lab terdahulu (delapan artikel; Tabel 6.1 buku sumber) menunjukkan hasil **campuran** untuk waktu penyimpanan, waktu pengambilan, kesalahan, klik, beban kognitif, dan frustrasi — **tidak ada indikasi jelas** tag lebih unggul. Kelemahan studi-studi itu: memakai tugas buatan eksperimenter, bukan informasi pribadi peserta, dan tidak membiarkan peserta memilih bebas. Satu pengecualian dari tim Google (Rodden & Leggett 2010): saat folder-label diperkenalkan ke jutaan pengguna Gmail, peluang membuat label **berlipat ganda** dan penyimpanan folder-label melampaui tag-label.

#### 6.4 Studi Bergman et al. (2013a): Folder vs Tag

Tujuan utama: menguji preferensi folder vs tag pada lingkungan yang mendukung keduanya (Gmail & Windows 7), secara naturalistik. Dua studi:

- **Studi Gmail (n=23):** kotak surel diperiksa setelah sebulan penggunaan bebas; peserta diberi penekanan penjelasan multiple classification.
- **Studi Windows 7 (n=23):** peserta dipaksa memakai tag selama **dua minggu** (*forced tagging*), lalu tugas pengambilan terkontrol, lalu kembali **lima minggu** kemudian untuk menguji preferensi pada fase **pilihan bebas**. Perangkat lunak khusus merekam lokasi dan jumlah tag tiap berkas. Pemeriksaan manipulasi menunjukkan kepatuhan: peserta menandai **71 persen** berkas yang diakses dan memakai multiple classification pada **55 persen** berkas yang ditandai.

> **Temuan inti.** Hasil menunjukkan **preferensi kuat** untuk folder atas tag, single atas multiple classification, hierarkis atas datar, dan pengambilan berbasis-lokasi atas non-lokasi.

**Folder vs Tag.**
- Gmail: **67 persen** pesan berlabel adalah folder-label vs **33 persen** tag-label. Alasan utama tagging ternyata ingin **menjaga surel terlihat di inbox**, bukan kebutuhan multiple classification.
- Windows 7: **96 persen** berkas disimpan di folder spesifik (bukan default); hanya **6 peserta (16 persen)** menandai berkas (dua di antaranya hanya satu berkas).
- Pengambilan lebih mencolok: Gmail rata-rata **16 persen** via membuka folder-label vs hanya **3 persen** via tag search; Windows 7 navigasi **61 persen** vs tag retrieval **5 persen**. Logfile Whittaker et al. (2011) selaras: folder **12 persen**, tag **1 persen**.

**Single vs Multiple Classification.**
- Gmail: **92 persen** surel berlabel memakai **satu** label vs **8 persen** banyak label. Pengambilan: peserta mengestimasi hanya **satu dari seribu** pesan diambil via banyak label.
- Windows 7: peserta menyatakan **tidak pernah** memakai multiple classification untuk pengambilan.

Tiga penjelasan preferensi single classification: (a) multiple classification **sulit & memakan waktu** (hampir separuh peserta Windows 7 menyatakan demikian; tag bersifat item-spesifik sehingga lebih menuntut kognitif — Pak et al. 2007); (b) **single classification cukup** (Bergman et al. 2008: lokasi diingat 74–90%; 2010: navigasi berhasil 94%); (c) **kategorisasi ganda membuat pengambilan menyeluruh tidak efisien** karena tag tumpang-tindih.

**Hierarkis vs Datar.** Gmail: **79 persen** peserta lebih memilih sistem pelabelan hierarkis; Windows 7: **86 persen** berkas disimpan di lokasi hierarkis non-datar. Bahkan Gmail kemudian (2010–2011) memperkenalkan **nested labels** (label hierarkis) menanggapi permintaan pengguna.

**Lokasi vs Non-Lokasi.** Navigasi dipakai **69 persen** (Gmail) dan **61 persen** (Windows 7) pengambilan. Tugas pengambilan terkontrol **tidak** menemukan tag lebih efisien — justru **lebih banyak gagal** dan **lebih lambat**.

#### 6.5 Tag sebagai "Cognitive Nodes": Kekeliruan Konseptual

Hsieh et al. (2008) mengklaim tag lebih kompatibel dengan kognisi manusia karena pemrosesan semantik mengikuti **spreading activation model** jaringan datar (Collins & Loftus 1975). Buku sumber membantah: meski model mirip-tag menyerupai representasi kognitif internal kita, **tidak otomatis** berarti tag adalah model terbaik untuk **menyimpan eksternal** informasi pribadi. Ini kekeliruan konseptual: tujuan klasifikasi PIM **bukan** mengeksternalkan representasi internal atau mendeskripsikan item secara lengkap, melainkan **mendukung pengambilan yang mudah, cepat, dan akurat**. Maka evaluasi harus fokus pada parameter retrieval (preferensi, kecepatan, akurasi), bukan kemiripan dengan sistem kognitif.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Tag / Tagging | Tanda/penandaan; metadata kata kunci untuk butir informasi. |
| Multiple classification | Klasifikasi ganda; beberapa label untuk satu item. |
| Single classification | Klasifikasi tunggal; satu lokasi/label per item. |
| Tag-label vs Folder-label (Gmail) | Label sebagai tag (item tetap di inbox) vs sebagai folder (item dipindahkan). |
| Flat repository | Repositori datar; tanpa hierarki. |
| Vocabulary problem | Masalah kosakata; orang berbeda memakai istilah berbeda. |
| Spreading activation model | Model aktivasi-menyebar; teori pemrosesan semantik jaringan datar. |
| Nested labels | Label bersarang; label hierarkis di Gmail. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 6.1 — Gmail Pak Eko.** Pak Eko mencoba memakai label Gmail sebagai tag agar surel bisa muncul di banyak kategori. Setelah sebulan, ia menyadari hanya memakai satu label per surel dan lebih sering membuka folder-label. Pola ini mencerminkan temuan 92% single label dan dominasi folder-label (67%).
>
> **Studi kasus 6.2 — Sikap vs perilaku mahasiswa.** Dalam survei kelas, mayoritas mahasiswa setuju "tag adalah masa depan" (mirip 72%). Namun ketika diminta menata berkas tugas selama dua minggu, hampir semua kembali ke folder—ilustrasi kesenjangan sikap-perilaku yang ditemukan buku sumber.

### Temuan Penelitian (dari Buku Sumber)

- Sikap (n=168): **77%** suka multiple classification, **72%** percaya masa depan tag, **61%** anggap folder sekadar kebiasaan.
- Gmail (n=23): folder-label **67%** vs tag-label **33%**; single label **92%** vs **8%**; retrieval folder-label **16%** vs tag search **3%**; navigasi **69%**.
- Windows 7 (n=23): berkas di folder spesifik **96%**; hanya **16%** memakai tag; navigasi **61%** vs tag retrieval **5%**; hierarkis **86%**.
- Logfile (Whittaker et al. 2011): folder **12%**, tag **1%**.
- Rodden & Leggett (2010): folder-label melipatgandakan pembuatan label.

### Rangkuman

- Tag diklaim unggul karena multiple classification dan tanpa hierarki, tetapi studi lab terdahulu memberi hasil campuran.
- Studi naturalistik Bergman et al. (2013a) menunjukkan preferensi **kuat dan tegas** untuk folder, single classification, hierarki, dan pengambilan berbasis lokasi.
- Multiple classification jarang dipakai karena lebih sulit, sering tidak perlu, dan membuat pengambilan menyeluruh tidak efisien.
- Tag bermanfaat untuk berbagi konten Web 2.0 (sosial), bukan untuk PIM individual karena pengguna akrab dengan koleksinya sendiri.

### Latihan & Refleksi

**A. Pemahaman**
1. Jelaskan beda tag-label dan folder-label di Gmail.
2. Sebutkan dua argumen utama "tag everything".
3. Berapa persentase pengguna Gmail yang memakai satu label saja (single classification)?

**B. Analisis (HOTS)**
4. Buku sumber menemukan kesenjangan antara **sikap** (positif terhadap tag) dan **perilaku** (memilih folder). Mengapa kesenjangan ini penting secara metodologis bagi riset desain?
5. Bantah klaim Hsieh et al. (2008) bahwa "tag lebih kompatibel dengan kognisi". Mengapa kemiripan dengan kognisi internal tidak menjamin keunggulan penyimpanan eksternal?
6. Mengapa tag berhasil di Flickr/YouTube tetapi gagal di PIM individual? Kaitkan dengan konsep "massa kritis" dan "familiaritas".

**C. Tugas Praktik**
7. Pilih 20 berkas. Coba beri masing-masing minimal dua tag yang relevan. Catat waktu dan tingkat kesulitan. Bandingkan pengalaman Anda dengan temuan bahwa "hampir separuh peserta menganggap tagging sulit/memakan waktu". Tuliskan kesimpulan.

---

## Bab 7 — Alternatif Pengelolaan Kelompok (The Group Management Alternative)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** Group Information Management (GIM) dan membandingkannya dengan PIM.
2. **Menjelaskan** dilema berbagi berkas (lampiran surel vs repositori bersama).
3. **Menafsirkan** temuan tingkat kegagalan pengambilan PIM vs GIM.
4. **Menguraikan** empat alasan mengapa pengambilan PIM lebih efektif (subjectivity, constructivism, episodic memory, locus of control).
5. **Mengevaluasi** trade-off PIM vs GIM dan implikasi desainnya.

### Peta Konsep

```
GIM = repositori bersama (Dropbox, Google Drive, OneDrive)
        |
   Dilema: lampiran surel (PIM) vs repositori bersama (GIM)
        |
   Masalah GIM: perbedaan gaya organisasi (Berlin et al.: purists/proliferators,
   syntactists/semanticists, scruffies/neatniks, savers/deleters), alerting, version control
        |
   STUDI Bergman, Whittaker & Falk (2014): n=275, 860 berkas
        |
   HASIL: gagal GIM 22% > PIM 13%
   - folder buatan orang lain gagal 28% vs sendiri 5% vs default 17%
        |
   4 alasan PIM unggul: subjectivity, constructivism, episodic memory, locus of control
```

### Materi Inti

#### 7.1 Apa itu GIM?

**Group Information Management (GIM)** (Erickson 2006) adalah pendekatan di mana strategi organisasi/pengambilan informasi **sebagian didelegasikan ke orang lain** — memanfaatkan organisasi orang lain untuk tujuan PIM. Ini makin penting dengan repositori kolaboratif berbasis awan (Dropbox, Google Drive, OneDrive) berjuta pengguna. Kerja modern inheren kolaboratif, sehingga pengguna kerap harus berbagi sumber daring. Pertanyaan bab ini: apakah memakai organisasi orang lain via GIM dapat mengatasi masalah PIM?

Ketika dua orang atau lebih berkolaborasi, muncul **dilema** berbagi berkas:
- **Lampiran surel + repositori pribadi** → tiap orang mengorganisasi dengan caranya sendiri = **PIM**.
- **Repositori bersama (awan)** → kelompok harus menyepakati organisasi = **GIM**.

Argumen teoretis untuk GIM kuat: PIM menuntut tiap kolaborator mengelola koleksinya sendiri (duplikasi berkas, waktu, dan usaha kognitif), serta menimbulkan masalah versi saat banyak salinan beredar via surel. Banyak organisasi karenanya mendorong tim memakai repositori bersama.

#### 7.2 Masalah-Masalah GIM dari Literatur

- **Perbedaan gaya organisasi (Berlin et al. 1993).** Tim peneliti yang awalnya yakin mudah menyepakati satu klasifikasi ternyata "salah, sangat salah". Mereka menemukan perbedaan individu: **purists** (satu lokasi per berkas) vs **proliferators** (semua lokasi mungkin); **syntactists** (berbasis isyarat episodik/konteks) vs **semanticists** (berbasis makna dokumen); **scruffies** ("hanya lima" kategori puncak) vs **neatniks** ("tiga ratus folder halus"); **savers** (simpan semua) vs **deleters** (minimal). Akibatnya anggota sering gagal menebak gaya idiosinkratik anggota lain saat mengambil dokumen.
- **Masalah alerting (Whittaker 1996; Lotus Notes).** Kolaborator sering tak sadar materi baru ditambahkan, sehingga mengirim surel pemberitahuan — yang justru merusak repositori bersama. Sistem seperti TeleNotes dan Topika mencoba alerting via surel, tetapi belum diadopsi luas; alerting tetap sulit (terlalu sedikit vs terlalu banyak menimbulkan overload).
- **Kurang rasa kepemilikan bersama (Rader 2009).** Dalam makalah "Yours, Mine and (Not) Ours", peserta membatasi aktivitas ke berkas sendiri dan ragu menghapus berkas yang mungkin berguna bagi orang lain, sehingga repositori menjadi berantakan.
- **Miskonsepsi awan (Voida, Olson, & Olson 2013).** Layanan berbeda, identitas digital berbeda, praktik kolaborator berbeda — begitu kompleks sampai satu peserta berkata memikirkannya "membuat kepala pusing".
- **Kontrol versi (Karlson, Smith, & Lee 2011).** Saat dua kolaborator mengubah versi berbeda secara sinkron, perlu digabung. Skema versi berbeda (angka vs tanggal) memperumit. Aplikasi awan (Google Drive) dapat meniadakan ini dengan koediting simultan.

Satu pengecualian: Massey et al. (2014) menemukan strategi sukses pada tim kecil (27 pekerja teknologi tinggi) — deskripsi metadata eksplisit dengan tautan, dan strategi implisit berbasis pengetahuan keahlian rekan — tetapi mungkin tidak berskala ke tim besar.

#### 7.3 Studi Bergman, Whittaker, & Falk (2014)

Studi pertama yang **langsung membandingkan** pengambilan GIM vs PIM untuk berbagi berkas dalam setting naturalistik: **275 pengguna** mengambil **860 berkas bersama** menggunakan metode **EPIR**. Penguji memakai mesin pencari desktop peserta untuk menemukan berkas yang penulisnya berbeda dari nama pengguna (menangkap baik berkas GIM maupun PIM, karena banyak layanan awan menyimpan salinan lokal). Berkas dalam folder yang sama dengan pencarian sebelumnya dikeluarkan untuk menghindari *priming*.

> **Temuan inti.** Saat memakai **GIM**, peluang **gagal** menemukan berkas (**22 persen**) **signifikan lebih tinggi** daripada **PIM (13 persen)**.

Pengguna lebih memilih berbagi via **surel (PIM)**: mengestimasi **86 persen** berkas dibagikan dan **65 persen** diterima via surel. Pendalaman menemukan akar masalah: tingkat kegagalan dari **folder buatan orang lain (28 persen)** lebih dari **lima kali** lipat folder buatan sendiri (**5 persen**), dan bahkan **lebih tinggi** daripada folder default seperti My Documents/Dropbox root (**17 persen**). Artinya: **memakai organisasi orang lain lebih buruk daripada tanpa organisasi sama sekali**. Jadi akar masalah bukan penyimpanan awan/GIM itu sendiri, melainkan **fakta bahwa orang lain yang membuat folder**.

#### 7.4 Empat Alasan PIM Lebih Efektif

Mengapa orang lebih ingat lokasi berkasnya sendiri (PIM) daripada GIM? Buku sumber mengajukan empat alasan:

1. **Subjektivitas klasifikasi (Subjectivity of classification).** Kategori suatu item tidak dapat diturunkan langsung dari item itu sendiri (Kwasnik 1991); ada banyak subjektivitas. Peserta jauh kurang berhasil menemukan berkas yang dikategorikan orang lain. Peserta 212: "Saya tidak bisa mengikuti pemikiran asosiatif orang lain."
2. **Konstruktivisme (Constructivism).** Pembelajar aktif merekonstruksi informasi dengan struktur mentalnya; pemrosesan aktif memperkuat memori. Dalam PIM, membuat folder dan mengorganisasi item secara aktif melibatkan pemikiran yang membantu pengambilan. Dalam GIM, "rasa sakit" kategorisasi dihilangkan (dilakukan orang lain), sehingga hilang pula "keuntungan" familiaritas.
3. **Memori episodik (Episodic memory).** Memori semantik = pengetahuan dunia bebas-konteks; memori episodik = ingatan pengalaman sendiri (mis. "saya mengerjakan dokumen ini saat liburan"). Dalam PIM, pengguna bisa bertumpu pada isyarat episodik penyimpanan; dalam GIM, informasi sering disimpan kolaborator sehingga isyarat episodik hilang.
4. **Pusat kendali (Locus of control).** Dalam PIM, orang mengendalikan organisasinya; dalam GIM, kendali terbatas karena organisasi sebagian dibuat orang lain. Kontrol yang berkurang menurunkan motivasi dan kinerja (Ajzen 2002).

Ketiga alasan terakhir juga relevan untuk **klasifikasi otomatis**: meski akurat, pengambilan bisa bermasalah karena pengguna kehilangan keterlibatan aktif.

#### 7.5 Perbandingan Penuh dan Implikasi Desain

GIM cenderung menghasilkan hierarki **lebih dalam** (mungkin karena khawatir orang lain sulit menemukan, atau karena tak ada penyimpanan desktop) — yang menambah waktu pengambilan. Buku sumber menyajikan perbandingan (Tabel 7.1, diadaptasi):

| Dimensi | PIM (surel) | Lebih baik? | GIM (awan) |
|---|---|---|---|
| Tingkat kegagalan pengambilan | 13% | PIM > GIM | 22% |
| Kesepakatan alat kolaborasi | Tak perlu | PIM > GIM | Perlu |
| Kesepakatan skema organisasi | Tak perlu | PIM > GIM | Perlu untuk pengambilan |
| Kontrol | Pengirim punya asli, bisa terima/tolak perubahan | PIM > GIM | Pengguna sering tak kendali atas perubahan/hapus orang lain |
| Alerting | Terkendali pengguna, andal, kontekstual | PIM > GIM | Sering terlalu sering/lemah/teknis |
| Kerja simultan | Tidak mungkin | GIM > PIM | Memungkinkan (Google Drive) |
| Email overload | Kolaborasi banyak update membebani surel | GIM > PIM | Versi baru langsung di repositori |

**Implikasi desain:** memungkinkan **editing simultan tetapi mempertahankan organisasi personal** — berkas di awan untuk kerja bersama, tetapi tiap peserta mengorganisasinya di foldernya sendiri. Solusi ini mungkin di Google Drive, tetapi desainnya tidak aktif mendorong kategorisasi folder (berbeda dari Mac/Windows yang meminta pengguna memfail). Para penulis sedang mengembangkan penyimpanan awan yang mendorong pengelolaan personal. Untuk versi, mereka merujuk desain **Old'nGray** (Bab 10) yang dapat digeneralisasi ke kasus GIM.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Group Information Management (GIM) | Manajemen Informasi Kelompok; organisasi sebagian didelegasikan ke orang lain. |
| Common/Shared repository | Repositori bersama (intranet/awan). |
| Purists/Proliferators, Syntactists/Semanticists, Scruffies/Neatniks, Savers/Deleters | Tipe gaya organisasi yang berbeda antar individu (Berlin et al. 1993). |
| Alerting | Pemberitahuan perubahan pada repositori bersama. |
| Version control / Versionset | Kontrol versi / himpunan versi berbeda dari berkas sama. |
| Subjectivity of classification | Subjektivitas klasifikasi; kategori tak bisa diturunkan dari item itu sendiri. |
| Constructivism | Konstruktivisme; pembelajaran aktif memperkuat memori. |
| Semantic vs Episodic memory | Memori semantik (pengetahuan) vs episodik (pengalaman). |
| Locus of control | Pusat kendali; tingkat kendali seseorang atas situasi. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 7.1 — Google Drive tim skripsi.** Tim Rani memakai Google Drive bersama. Ketika Rani mencari berkas yang difolderkan temannya, ia sering gagal—sesuai temuan kegagalan folder-buatan-orang-lain 28% vs folder sendiri 5%. Mereka akhirnya kembali mengirim berkas via surel dan menatanya sendiri (PIM), meningkatkan keberhasilan pengambilan.
>
> **Studi kasus 7.2 — Empat gaya di kantor.** Dalam satu divisi: Pak Anto (saver + neatnik) membuat ratusan folder halus, Bu Lia (deleter + scruffy) hanya lima folder. Saat berbagi repositori, keduanya saling bingung—ilustrasi perbedaan gaya Berlin et al. (1993).

### Temuan Penelitian (dari Buku Sumber)

- Studi Bergman, Whittaker, & Falk (2014): **275** pengguna, **860** berkas.
- Kegagalan **GIM 22%** vs **PIM 13%**.
- Folder buatan orang lain gagal **28%** vs buatan sendiri **5%** vs default **17%**.
- Berbagi via surel: kirim **86%**, terima **65%**.
- Empat alasan PIM unggul: subjectivity, constructivism, episodic memory, locus of control.

### Rangkuman

- GIM mendelegasikan sebagian organisasi ke orang lain melalui repositori bersama.
- Meski intuitif menguntungkan, pengambilan GIM kurang berhasil (22% gagal) daripada PIM (13%).
- Akar masalah: folder buatan orang lain (gagal 28%) — bahkan lebih buruk daripada tanpa organisasi (default 17%).
- Empat alasan PIM unggul berkaitan dengan keterlibatan aktif dan isyarat personal saat menyimpan.
- Implikasi desain: padukan editing simultan dengan organisasi personal.

### Latihan & Refleksi

**A. Pemahaman**
1. Apa perbedaan mendasar PIM dan GIM dalam hal siapa yang mengorganisasi?
2. Sebutkan tingkat kegagalan pengambilan GIM, PIM, folder orang lain, folder sendiri, dan default.
3. Sebutkan empat alasan PIM lebih efektif daripada GIM.

**B. Analisis (HOTS)**
4. Temuan paling mengejutkan: folder buatan orang lain (gagal 28%) lebih buruk daripada tanpa organisasi (default 17%). Jelaskan paradoks ini dengan konsep subjectivity of classification.
5. Bedakan peran memori semantik dan episodik dalam menjelaskan keunggulan PIM. Beri contoh konkret isyarat episodik.
6. Rancang fitur GIM yang menggabungkan keunggulan kerja simultan (GIM) dengan keunggulan organisasi personal (PIM). Apa tantangan implementasinya?

**C. Tugas Praktik**
7. Bersama dua teman, buat folder Google Drive bersama berisi 15 berkas yang difolderkan masing-masing. Lalu saling mengambil berkas teman dan catat tingkat keberhasilan. Bandingkan dengan temuan kegagalan 28% folder orang lain.

---

## Bab 8 — Mengapa Navigasi adalah Metode Pengambilan PIM yang Disukai?

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menyebutkan** tiga spekulasi awal Bergman et al. (2008): consistency, recognition vs recall, procedural vs declarative.
2. **Menjelaskan** paradigma dual-task dan komponen memori kerja (phonological loop, visuospatial sketchpad).
3. **Menafsirkan** temuan studi dual-task bahwa navigasi menuntut lebih sedikit atensi verbal.
4. **Menguraikan** temuan studi fMRI tentang aktivasi otak berbeda untuk navigasi vs search.
5. **Mengintegrasikan** penjelasan kognitif dan neurologis untuk preferensi navigasi.

### Peta Konsep

```
PARADOKS: folder unggul meski tampak punya batasan -> MENGAPA?
        |
   Spekulasi awal (Bergman et al. 2008):
   - Consistency
   - Recognition > Recall
   - Procedural > Declarative memory
        |
   STUDI 1 (Dual-task, n=62): navigasi -> lebih banyak kata diingat
       -> navigasi butuh lebih sedikit atensi verbal; search ~3x lebih lama
        |
   STUDI 2 (fMRI, n=17):
   - Navigasi -> aktivasi posterior bilateral (parahippocampal, "navigasi dunia nyata")
   - Search -> aktivasi frontal kiri (Broca, memori kerja verbal)
        |
   KESIMPULAN: navigasi memakai struktur otak "tua" evolusioner, minim bahasa
   -> preferensi navigasi tak akan berubah meski search membaik
```

### Materi Inti

#### 8.1 Tiga Spekulasi Awal

Bagian II menunjukkan folder hierarkis tetap disukai dan alternatif (search, tag, GIM) tak menggantikannya — sebuah **paradoks**. Bergman et al. (2008) menawarkan tiga spekulasi awal:

1. **Konsistensi (Consistency).** Konsistensi adalah keutamaan dalam desain/HCI karena memenuhi ekspektasi (Shneiderman & Plaisant 2010). Metode hierarkis "membosankan secara konsisten": berkas disimpan di satu "lokasi" dan tetap di sana. Sebaliknya, fleksibilitas search dapat merusak konsistensi (berkas sama bisa diambil lewat istilah berbeda; hasil bisa berubah karena perubahan algoritma indeks).
2. **Pengenalan vs pengingatan (Recognition vs recall).** Tugas pengenalan lebih mudah dan menuntut usaha kognitif lebih kecil daripada pengingatan (Mandler 1980). Search menuntut **menghasilkan istilah dari nol** (recall), sedangkan navigasi terutama berbasis **recognition** — tiap langkah memberi umpan balik visual/kontekstual inkremental.
3. **Memori prosedural vs deklaratif (Procedural vs declarative).** Search bertumpu pada memori **deklaratif** (harus tahu istilah ada di berkas), sedangkan navigasi dapat bertumpu pada memori **prosedural** (tahu *cara* menavigasi) dan "motor memory" lokasi.

Bab ini melaporkan **dua studi** dengan metode berbeda yang saling melengkapi.

#### 8.2 Studi Dual-Task

**Hipotesis:** navigasi disukai karena menuntut lebih sedikit **atensi verbal**. Manusia punya kapasitas atensi terbatas; proses kognitif kompleks bersaing memperebutkan sumber daya terbatas (Treisman 1969). Pengambilan berkas biasanya dilakukan dalam konteks **tugas utama** (mis. mahasiswa kimia mengambil berkas "Tabel Unsur" sambil menulis makalah). Maka rasional memilih metode pengambilan yang menuntut lebih sedikit atensi verbal, agar tugas utama tetap terjaga.

**Paradigma dual-task** mengeksplorasi pembagian usaha mental antara dua tugas bersamaan. Analogi **pengemudi yang mengobrol**: saat mengemudi rutin (otomatis), ia bisa fokus mengobrol (tugas sekunder); saat anak berlari ke jalan, seluruh atensinya tersedot ke mengemudi (tugas primer) dan ia tak mendengar penumpang. Kinerja tugas sekunder mengindikasikan alokasi atensi. Baddeley (1992) mengidentifikasi dua komponen **memori kerja (working memory)**: **phonological loop (verbal)** dan **visuospatial sketchpad (visual)**.

Studi Bergman, Tene-Rubinstein, & Shalom (2013) memakai tugas sekunder **verbal**: **delayed free recall** (mengingat daftar kata). Pada *immediate free recall*, orang mengingat **tujuh plus-minus dua** kata (Miller 1956); dengan penundaan/tugas antara, jumlahnya menurun. Untuk menahan kata di memori jangka pendek selama tugas antara, peserta perlu **phonological loop** (rehearsal) — sulit dilakukan saat tugas verbal yang menuntut. Dalam eksperimen, **pengambilan berkas adalah tugas antara**: peserta diberi daftar kata, mengambil berkas, lalu mengingat kata. Jumlah kata yang diingat menjadi indikator atensi verbal yang dituntut metode pengambilan.

> **Temuan inti.** Dengan desain within-subjects, **62 peserta** mengingat **lebih banyak kata** saat **menavigasi** daripada saat **search**. Karena navigasi lebih cepat (waktu memengaruhi rekoleksi), analisis dikontrol pada **27 pasang** pengambilan berwaktu serupa — efek tetap signifikan. Maka navigasi menuntut **lebih sedikit atensi verbal** daripada search. Search juga **~3 kali lebih lama**, lebih rentan kesalahan/kegagalan, dan dinilai lebih sulit.

Navigasi menuntut sedikit atensi karena pengguna sangat **familiar** dengan struktur foldernya (dibuat sendiri, makin akrab tiap navigasi), sehingga dapat dilakukan **semi-otomatis**. Search menuntut memikirkan istilah pencarian — terbukti menuntut atensi (Gwizdka 2010) — dan banyak opsi istilah yang tidak menambah familiaritas.

#### 8.3 Studi fMRI

Hipotesis lanjutan: navigasi berkas virtual memakai **struktur otak primitif** yang berevolusi untuk **navigasi fisik**. Studi Benn et al. (2015) memakai **functional magnetic resonance imaging (fMRI)** pada **17 peserta** sehat tangan-kanan yang mengambil berkas mereka sendiri (via EPIR) di Windows 7, dengan kondisi search dan navigasi serta dua tugas kontrol (mencocokkan aktivitas visual/motorik tanpa proses kognitif inti).

> **Temuan inti.** Navigasi menghasilkan aktivasi **posterior bilateral** otak, terkait **navigasi dunia nyata**, pengambilan dari memori, dan pemrosesan sensorik-perseptual tingkat rendah (mis. **parahippocampal gyrus**). Search menghasilkan aktivasi **terlateralisasi kiri** di area kuat terkait pemrosesan **linguistik (area Broca)** dan **memori kerja (superior frontal gyrus)**.

Area posterior yang aktif saat navigasi sama dengan yang dipakai untuk navigasi dunia nyata pada manusia maupun hewan (monyet, tikus, merpati); pasien dengan gangguan bahasa parah pun tetap baik dalam tugas navigasi — menyiratkan navigasi (virtual maupun nyata) **minim pemrosesan linguistik**. Sebaliknya, kebutuhan **menghasilkan istilah pencarian** menyedot sumber daya linguistik dan atensi, menjelaskan mengapa search dipakai sebagai **pilihan terakhir** meski fleksibel. Aktivasi frontal juga muncul saat navigasi (butuh sedikit sumber daya eksekutif/memori kerja), tetapi **tidak meluas ke struktur linguistik**.

#### 8.4 Integrasi: Bias Neurologis yang Mengakar

Gabungan kedua studi menjelaskan preferensi navigasi yang berulang terdokumentasi, sekaligus mengapa preferensi ini **tak berubah** meski teknologi search membaik (Bab 5) — dan kemungkinan **tidak akan berubah** dengan peningkatan search lebih lanjut. Sepanjang jutaan tahun evolusi, manusia mengembangkan mekanisme untuk mengambil item dari lokasi (nyata atau virtual) dengan menavigasi jalur yang sama saat menyimpannya. Bias neurologis mengakar ini memicu aktivasi rutin terkait-lokasi secara otomatis, **minim bahasa**, sehingga membebaskan sistem bahasa untuk tugas lain.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Consistency | Konsistensi; keutamaan desain yang memenuhi ekspektasi pengguna. |
| Recognition vs Recall | Pengenalan (lebih mudah) vs pengingatan-bebas (lebih sulit). |
| Procedural vs Declarative memory | Memori prosedural (tahu caranya) vs deklaratif (tahu faktanya). |
| Dual-task paradigm | Paradigma tugas-ganda; mengukur alokasi atensi antar dua tugas. |
| Working memory | Memori kerja; sistem penyimpanan sementara terbatas. |
| Phonological loop / Visuospatial sketchpad | Lingkar fonologis (verbal) / papan-sketsa visuospasial (visual). |
| Delayed free recall | Pengingatan-bebas tertunda; tugas memori standar. |
| fMRI | Functional magnetic resonance imaging; pencitraan aktivitas otak. |
| Parahippocampal gyrus | Girus parahipokampus; area terkait navigasi spasial. |
| Broca's area | Area Broca; area pemrosesan linguistik. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 8.1 — Menulis sambil mengambil berkas.** Saat menyusun laporan, Nadia perlu membuka berkas data. Bila ia menavigasi (rute familiar), ia tetap ingat kalimat yang sedang ditulis. Bila ia harus memikirkan kata kunci pencarian, alur pikirannya terputus—ilustrasi temuan bahwa search menyedot atensi verbal yang juga dibutuhkan tugas utama.

### Temuan Penelitian (dari Buku Sumber)

- Dual-task (n=62): navigasi → lebih banyak kata diingat; efek bertahan setelah dikontrol waktu (27 pasang); search **~3x lebih lama**.
- Memori kerja: phonological loop (verbal) & visuospatial sketchpad (Baddeley 1992); kapasitas **7±2** (Miller 1956).
- fMRI (n=17): navigasi → posterior bilateral (parahippocampal); search → frontal kiri (Broca, superior frontal gyrus).
- Navigasi minim pemrosesan linguistik; preferensi navigasi tak akan berubah dengan peningkatan search.

### Rangkuman

- Tiga spekulasi awal: konsistensi, recognition>recall, procedural>declarative.
- Studi dual-task: navigasi menuntut lebih sedikit atensi verbal, membebaskan kapasitas untuk tugas utama.
- Studi fMRI: navigasi memakai struktur posterior (navigasi spasial); search memakai struktur frontal kiri (linguistik).
- Preferensi navigasi berakar pada bias neurologis evolusioner dan kemungkinan permanen.

### Latihan & Refleksi

**A. Pemahaman**
1. Jelaskan analogi "pengemudi yang mengobrol" dalam paradigma dual-task.
2. Sebutkan dua komponen memori kerja menurut Baddeley.
3. Area otak mana yang aktif saat navigasi dan saat search?

**B. Analisis (HOTS)**
4. Mengapa peneliti perlu mengontrol waktu pengambilan (27 pasang berwaktu serupa) sebelum menyimpulkan navigasi menuntut atensi lebih sedikit? Apa ancaman validitas yang dihindari?
5. Buku sumber menyimpulkan preferensi navigasi "tidak akan berubah" meski search membaik. Apakah Anda setuju? Berikan satu skenario teknologi masa depan yang bisa menantang kesimpulan ini.
6. Hubungkan temuan Bab 8 dengan temuan Bab 5 (search bertahan rendah). Bagaimana penjelasan neurologis melengkapi temuan perilaku?

**C. Tugas Praktik**
7. Lakukan eksperimen mini ala dual-task: hafalkan 7 kata acak, lalu (a) navigasi ke satu berkas, recall kata; (b) ulangi dengan kata baru tetapi search ke berkas lain, recall kata. Bandingkan jumlah kata yang Anda ingat pada kedua kondisi dan kaitkan dengan teori atensi verbal.

---

## Rangkuman Bagian II

Tiga bab pertama Bagian II menelaah alternatif navigasi folder dan menunjukkan bahwa **search, tag, dan klasifikasi kelompok tidak mungkin menggantikan** hierarki folder untuk PIM. Bab 8 memberi penjelasan **kognitif dan neurologis** untuk preferensi navigasi. Ada pula alternatif teknis lain yang tidak dibahas langsung — seperti **klasifikasi otomatis** dan **semantic desktop** (penerapan machine learning untuk mengategorikan seluruh koleksi pribadi). Buku sumber menekankan pentingnya **menguji empiris** apakah pendekatan baru benar-benar mengungguli navigasi. Selama lebih dari tiga dekade ilmuwan mengembangkan sistem pengganti hierarki folder, tetapi sebagian besar tidak dievaluasi empiris dan **tidak satu pun diadopsi luas**, sementara folder dipakai hampir eksklusif oleh jutaan pengguna setiap hari.

Mengapa metode yang bekerja baik di luar PIM (search web, tag Web 2.0) kurang berguna dalam PIM? Isu kuncinya adalah **familiaritas**. Web dan Web 2.0 melibatkan miliaran dokumen yang strukturnya mustahil dikenali, sehingga modelnya adalah search dan konsumsi. PIM melibatkan koleksi jauh lebih kecil yang dikurasi sendiri; pengguna **akrab** dengan struktur foldernya sendiri, yang makin akrab tiap kali dinavigasi. Ditambah alasan kognitif Bab 8: navigasi kurang menuntut secara kognitif daripada search yang membutuhkan pemrosesan verbal kompleks.

Bagian I dan II membuktikan secara definitif bahwa PIM adalah "permainan yang berbeda". **Bagian III** menjelaskan metode desain yang dikembangkan khusus untuk PIM: **pendekatan user-subjective**. Berbeda dari search/tag/GIM, pendekatan ini **tidak berusaha menggantikan** folder hierarkis, melainkan memanfaatkan karakteristik unik PIM untuk **menyatukan metode baru ke dalam pendekatan hierarkis** yang mendasarinya.

---

# BAGIAN III — Pendekatan User-Subjective dalam Desain Sistem PIM

## Pengantar Bagian III

Bagian II menunjukkan bahwa teknologi yang berusaha menggantikan navigasi umumnya gagal. Namun hasil itu belum menjawab pertanyaan kritis: **bagaimana merancang sistem baru yang berhasil?** Riset kurasi bukan hanya tentang memahami cara orang menyimpan, mengorganisasi, dan memanfaatkan informasi, melainkan juga tentang **merancang teknologi** yang membantu mereka lebih sukses. Untuk itu, kita perlu kembali ke apa yang membedakan kurasi PIM: **familiaritas** — orang yang mengkurasi informasi adalah orang yang sama yang kelak mengambilnya.

Pendekatan **user-subjective** memanfaatkan fitur unik ini dan menyarankan sistem PIM **memakai atribut subjektif (bergantung pengguna) secara sistematis**. Ini adalah pendekatan desain **pertama** yang dikembangkan khusus untuk sistem PIM. Para penulis pertama menggariskan teorinya (Bergman, Beyth-Marom, & Nachmias 2003), lalu memberikan dukungan empiris (2008). Bagian III memperluasnya dengan **enam implementasi** prinsip yang telah dideploy dan dievaluasi positif. Bab 9 memperkenalkan pendekatan ini; Bab 10–12 masing-masing membahas satu prinsip desain: **importance (kepentingan), project-based organization (organisasi berbasis proyek), dan context (konteks)**.

---

## Bab 9 — Pendekatan User-Subjective

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mengulang** metafora komunikasi PIM dan implikasinya bagi desain.
2. **Membedakan** atribut publik (objektif) dan atribut subjektif (bergantung pengguna).
3. **Menjelaskan** temuan Kwasnik (1991) tentang dominasi atribut subjektif.
4. **Menyebutkan** tiga atribut subjektif dan tiga prinsip desain user-subjective.
5. **Menjelaskan** mengapa prinsip dirumuskan secara abstrak (generatif).

### Peta Konsep

```
PIM = komunikasi solipsistik: penyimpan = pengambil (diri sendiri, dua waktu)
        |
   Atribut: PUBLIK (objektif: format, ukuran, tanggal)
            vs SUBJEKTIF (bergantung pengguna: importance, project, context)
        |
   Kwasnik (1991): 30% atribut dokumen-terkait, 70% interaksi pengguna-informasi
        |
   3 PRINSIP user-subjective:
   1. Subjective Importance -> salience & accessibility (Bab 10)
   2. Subjective Project Classification -> item satu proyek dikumpulkan (Bab 11)
   3. Subjective Context -> item diambil dalam konteks penggunaan sebelumnya (Bab 12)
```

### Materi Inti

#### 9.1 Mengulang Metafora Komunikasi

Bidang manajemen informasi lain memandang tujuannya sebagai merancang **saluran komunikasi** antara profesional informasi (yang mengorganisasi) dan pengguna (yang menemukan dan mengonsumsi). Karena konsumen beragam, profesional hanya boleh memakai **atribut publik (user-independent)**. Sistem PIM unik: **penyimpan = pengambil**, sehingga PIM adalah komunikasi **solipsistik** antara seseorang dengan dirinya pada dua waktu (penyimpanan dan pengambilan). Pendekatan user-subjective memanfaatkan ini: sistem PIM sebaiknya **memakai atribut subjektif** selain atribut objektif tradisional, menangkapnya saat pengguna pertama berinteraksi dengan item (otomatis atau lewat *direct manipulation*) untuk membantu pengambilan kelak.

#### 9.2 Atribut Subjektif

Studi PIM awal yang menginspirasi pendekatan ini adalah **Kwasnik (1991)**, yang menganalisis deskripsi delapan dosen tentang cara mereka mengorganisasi dokumen pribadi. Hasilnya: minoritas (**30 persen**) atribut bersifat **dokumen-terkait** (penulis, bentuk, topik, judul), sedangkan mayoritas (**70 persen**) berkaitan dengan **interaksi pengguna–informasi** — bagaimana pengguna mempersepsi dan bertindak terhadap informasi (atribut situasional, disposisi, waktu, keadaan kognitif). Jadi organisasi alami orang lebih bertumpu pada **atribut subjektif** daripada atribut publik umum.

Definisi:
- **Atribut publik (public attributes):** bersifat **user-independent**; pengamat luar dapat menyimpulkannya langsung dari item tanpa mengamati pengguna. Contoh: format, ukuran, tanggal.
- **Atribut subjektif (subjective attributes):** bersifat **user-dependent**; tidak dapat diturunkan langsung dari item, tetapi sering dapat disimpulkan dari interaksi pengguna–informasi. Contoh: bila pengguna sering mengakses suatu item, kita simpulkan item itu **penting** baginya.

#### 9.3 Tiga Atribut dan Tiga Prinsip

Pendekatan user-subjective mengidentifikasi tiga atribut subjektif spesifik — **importance (kepentingan), project (proyek), dan context (konteks)** — dan mengusulkan satu prinsip desain untuk masing-masing:

> - **Prinsip Subjective Importance:** kepentingan subjektif suatu informasi sebaiknya menentukan derajat **salience visual** dan **aksesibilitasnya**.
> - **Prinsip Subjective Project Classification:** item yang berkaitan dengan **topik/proyek subjektif yang sama** sebaiknya diklasifikasikan bersama, **tanpa memandang format teknologi** atau aplikasi yang menghasilkannya.
> - **Prinsip Subjective Context:** informasi sebaiknya diambil dan dilihat pengguna **dalam konteks yang sama** dengan saat sebelumnya digunakan.

Prinsip-prinsip ini sengaja dirumuskan **abstrak** agar memungkinkan banyak kemungkinan desain. Sifat abstrak ini membuat prinsip bersifat **generatif** — dapat melahirkan beragam implementasi yang belum terbayangkan. Bab 10–12 mendefinisikan tiap atribut, mengusulkan prinsip desainnya, dan memberikan dukungan empiris dari sistem yang telah dideploy.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| User-subjective approach | Pendekatan yang memanfaatkan atribut bergantung-pengguna dalam desain PIM. |
| Public attribute | Atribut publik/objektif; dapat diturunkan langsung dari item. |
| Subjective attribute | Atribut subjektif; bergantung interaksi pengguna–informasi. |
| Solipsistic communication | Komunikasi solipsistik; pengguna berkomunikasi dengan dirinya di masa depan. |
| Direct manipulation | Manipulasi langsung; antarmuka dengan representasi objek dan aksi cepat-reversibel. |
| Generative principle | Prinsip generatif; rumusan abstrak yang dapat melahirkan banyak desain. |
| Salience | Salience; derajat keterlihatan/penonjolan visual. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 9.1 — Atribut subjektif Pak Rudi.** Saat ditanya bagaimana ia menata dokumen, Pak Rudi lebih banyak berkata "ini yang saya kerjakan waktu liburan", "ini penting, harus segera", "ini untuk proyek akreditasi"—bukan "ini PDF 2 MB". Ucapannya didominasi atribut subjektif (importance, context, project), persis temuan Kwasnik (1991): 70% atribut bersifat interaksi pengguna–informasi.

### Temuan Penelitian (dari Buku Sumber)

- Kwasnik (1991): **30%** atribut dokumen-terkait vs **70%** atribut interaksi pengguna–informasi.
- Pendekatan user-subjective adalah pendekatan desain **pertama** khusus PIM; **enam** implementasi telah dievaluasi positif.

### Rangkuman

- PIM unik karena penyimpan = pengambil → komunikasi solipsistik.
- Atribut publik objektif; atribut subjektif bergantung pengguna dan mendominasi organisasi alami (Kwasnik 1991).
- Tiga atribut subjektif (importance, project, context) melahirkan tiga prinsip desain.
- Prinsip dirumuskan abstrak agar generatif.

### Latihan & Refleksi

**A. Pemahaman**
1. Apa beda atribut publik dan subjektif? Beri dua contoh masing-masing.
2. Sebutkan tiga prinsip user-subjective.
3. Mengapa prinsip dirumuskan secara abstrak?

**B. Analisis (HOTS)**
4. Temuan Kwasnik (1991) menjadi fondasi pendekatan ini. Jelaskan bagaimana angka 70% mendukung gagasan bahwa sistem PIM harus memakai atribut subjektif.
5. Mengapa pendekatan user-subjective tidak berusaha menggantikan folder, berbeda dari search/tag/GIM? Apa keuntungan strategi "menambah ke" daripada "mengganti"?

**C. Tugas Praktik**
6. Rekam (tertulis) cara Anda mendeskripsikan 10 berkas Anda kepada teman. Klasifikasikan tiap deskripsi sebagai atribut publik atau subjektif. Hitung rasionya dan bandingkan dengan 30:70 milik Kwasnik.

---

## Bab 10 — Prinsip Subjective Importance (Kepentingan Subjektif)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Membedakan** subprinsip promosi dan demosi.
2. **Menjelaskan** demosi sebagai opsi tengah antara keep dan delete, dikaitkan dengan Prospect Theory.
3. **Menganalisis** strategi work-around demosi yang ditemukan pada pengguna.
4. **Menguraikan** tiga implementasi demosi: GrayArea, DMTR, Old'nGray, beserta hasil evaluasinya.
5. **Mengaitkan** prinsip demosi dengan pengambilan berbasis search.

### Peta Konsep

```
SUBJECTIVE IMPORTANCE: kepentingan -> salience & accessibility
        |
   Dua subprinsip:
   - PROMOSI: item penting -> sangat terlihat/mudah diakses
   - DEMOSI: item kurang penting -> kurang terlihat, TAPI tetap dalam konteks asli
        |
   Metafora jalan tol: lajur cepat (promosi), lajur lambat (demosi)
        |
   Demosi = opsi tengah keep vs delete (atasi Prospect Theory / loss aversion)
        |
   Work-around: arsip folder 40%, memori eksternal 61%, folder baru 32%, arsip dalam folder 24%; 79% pakai salah satu
        |
   Implementasi: GrayArea (manual), DMTR (kontak otomatis), Old'nGray (versi otomatis)
```

### Materi Inti

#### 10.1 Kepentingan adalah Subjektif

Kepentingan **bergantung pengguna**: satu item bisa sangat penting bagi seseorang dan tak penting bagi yang lain, bahkan berubah seiring waktu. Salah satu ukuran relevansi diturunkan dari interaksi: item yang **baru digunakan** umumnya dinilai lebih relevan (item terkini lebih mungkin diambil — lihat bias kebaruan di Bagian I). Prinsip **subjective importance** menyatakan kepentingan informasi sebaiknya menentukan derajat **salience visual** dan **aksesibilitas**. Ada dua subprinsip komplementer:

- **Prinsip promosi (promotion principle):** item penting sebaiknya **sangat terlihat dan mudah diakses** karena lebih mungkin diambil.
- **Prinsip demosi (demotion principle):** item kurang penting sebaiknya **didemosi** (dibuat kurang terlihat) agar tidak mengganggu, **tetapi tetap dipertahankan dalam konteks aslinya** untuk berjaga-jaga.

Promosi dan demosi **tidak bersaing** karena menangani kebutuhan berbeda. Mengingat sebagian besar item berkepentingan **sedang**, promosi memisahkan item **sangat penting** dari yang lain, sedangkan demosi memisahkan item **kurang penting**. Buku sumber memakai **metafora jalan tol**: sebagian besar kendaraan di lajur tengah (kepentingan sedang); ada **lajur cepat** untuk kendaraan cepat (promosi) dan **lajur lambat** untuk truk yang akan memperlambat lajur tengah (demosi).

Beberapa desain promosi sudah lazim (menaruh berkas penting di desktop — mengikuti Malone 1983; daftar dokumen terkini; Finder Highlights — Fitchett, Cockburn, & Gutwin 2014). Sebaliknya, **demosi adalah aspek baru** pendekatan user-subjective dan belum dieksplorasi sistematis, sehingga bab ini berfokus pada demosi.

#### 10.2 Demosi: Opsi Tengah antara Keep dan Delete

Mengapa penting menangani item kurang penting? Jones (2004) menyatakan keputusan "keep or not to keep" rawan dua kesalahan mahal: informasi yang tak disimpan hilang saat dibutuhkan; informasi tak relevan yang disimpan menciptakan **clutter (kekusutan)**. Item tak relevan **bersaing memperebutkan atensi** dan menutupi informasi penting; dalam pemindaian visual, jumlah *distracter* meningkatkan waktu menemukan target (Neisser 1964; Treisman & Gelade 1980). Ada pula **paradoks penghapusan (deletion paradox):** item tak penting menambah waktu pengambilan, tetapi meninjau dan memutuskan menghapusnya juga butuh waktu dan atensi.

Orang menghindari penghapusan karena alasan rasional (selalu bisa membayangkan situasi item dibutuhkan) maupun psikologis, banyak yang dijelaskan **Prospect Theory** (Kahneman & Tversky 1979):

- Orang menilai untung-rugi relatif terhadap **titik acuan subjektif**; keputusan menyimpan sudah dibuat saat berkas dibuat/diterima, sehingga "menyimpan" menjadi acuan default dan "menghapus" alternatif baru yang berisiko.
- Orang lebih memilih menghindari kerugian pasti (walau peluang kecil), dan menyimpan menghindari kehilangan item.
- Probabilitas objektif kecil dipersepsi lebih besar, sehingga peluang kecil "item dihapus ternyata dibutuhkan" terasa signifikan.
- **Kerugian terasa lebih besar daripada keuntungan setara** — potensi kehilangan item lebih memengaruhi emosi daripada keuntungan berkurangnya distracter.

**Demosi** menawarkan **opsi tengah**: membuat item kurang penting kurang terlihat **tanpa** menutup akses masa depan — memadukan keuntungan menghapus (mengurangi persaingan atensi) dan menyimpan (akses bila tiba-tiba dibutuhkan). Demosi juga mendukung penundaan dan memperpendek proses keputusan sulit menghapus. Hasil (Bergman et al. 2009) menunjukkan demosi **lebih mudah** daripada menghapus karena **berisiko lebih rendah**. Dahulu menghapus diperlukan untuk membebaskan ruang disk, tetapi kini penyimpanan murah, sehingga **demosi menjadi opsi ketiga** yang layak.

#### 10.3 Motivasi: Work-around Demosi

Riset multi-metode (Bergman, Beyth-Marom, & Nachmias 2008) menemukan pengguna memahami dan memakai promosi (mis. menaruh berkas penting di desktop). Tetapi karena sistem saat ini **tidak punya fitur demosi**, pengguna membuat **work-around**:

- **40 persen** memindahkan item kurang penting ke folder arsip;
- **61 persen** memindahkan ke memori eksternal (mis. CD);
- **32 persen** membuat folder baru dan memakai folder lama sebagai arsip;
- **24 persen** membuat folder arsip di dalam folder asli.

Secara total, **79 persen** peserta memakai satu atau lebih cara ini untuk membuat sebagian berkas kurang penting menjadi kurang terlihat — memvalidasi prinsip demosi dan memotivasi desain.

#### 10.4 Implementasi Demosi

**Penting:** antarmuka demosi harus **mempertahankan item dalam konteks aslinya** — inilah pembeda demosi dari penghapusan atau **pengarsipan (archiving)** yang memindahkan item keluar dari konteks. Mempertahankan konteks penting karena (Bagian II) orang cenderung mengambil item dari lokasi tempat mereka menyimpannya. Tiga desain demosi telah dievaluasi:

**(a) GrayArea.** Memungkinkan pengguna mendemosi berkas kurang penting dengan menyeretnya ke **area abu-abu di bagian bawah folder**. Siklus desain penuh (Bergman et al. 2009): mendokumentasikan work-around, menguji tiga prototipe kertas (umpan balik dari **79 peserta**), lalu mengembangkan prototipe kerja, dan mengevaluasinya dengan meminta **96 peserta** "membersihkan" dua folder dalam dua kondisi (dengan dan tanpa GrayArea). Hasil:

- GrayArea **mengurangi clutter folder 13 persen**: peserta menyimpan **67 persen** berkas dengan GrayArea vs **80 persen** tanpa.
- Persentase penghapusan turun dari **20 persen** (standar) ke **10 persen** (GrayArea).
- **23 persen** berkas didemosi = **10 persen** yang mungkin dihapus + **13 persen** yang mungkin disimpan.
- **81 persen** peserta merasa lebih mudah mendemosi daripada menghapus (demosi terasa kurang "final" — bisa dibatalkan dengan menyeret kembali ke atas).
- Mayoritas menyatakan akan memakai GrayArea bila tersedia di sistem operasinya.

**(b) DMTR.** Menangani **overkeeping kontak** di ponsel, tempat ukuran layar terbatas membuat kontak tak terpakai jadi masalah kritis. DMTR (Bergman, Komninos, et al. 2012) mendemosi kontak tak terpakai dengan menampilkannya di bagian bawah daftar dalam font lebih kecil dan tidak tebal — tetapi **otomatis**, bukan manual. Fase 1: **18 peserta** menilai kapan terakhir memakai tiap kontak — **47 persen** tak dipakai >6 bulan atau tak pernah (selaras Whittaker et al. 2002). Fase 2: kontak tak terpakai didemosi; setelah dua bulan, mengakses kontak terkini **mengurangi jumlah ketukan tombol dan waktu pengambilan secara signifikan**. Mayoritas peserta ingin memakai DMTR di ponsel berikutnya.

**(c) Old'nGray.** Menangani **recent version problem** — usaha menemukan versi terbaru yang benar di antara banyak versi. Old'nGray (Bergman et al. 2014) **otomatis mengidentifikasi versi terbaru** dan **mengaburkan (gray out)** ikon versi lama, sehingga pengguna mengenali versi terbaru **sekilas** lewat proses perseptual (bukan kognitif). Opsi tambahan (klik kanan): membuka versi terbaru walau di folder/lampiran lain; menampilkan semua versi; membatalkan pengaburan. Evaluasi within-subjects (**N=60**): Old'nGray **drastis mengurangi kegagalan akses dari 24 persen ke 4 persen** dan **waktu pengambilan dari 17,68 detik ke 6,56 detik**; manfaatnya meningkat dengan ukuran folder. **70 persen** peserta ingin diintegrasikan ke sistem operasi berikutnya.

#### 10.5 Demosi dan Search

Demosi tidak terbatas pada pengambilan folder; dapat diterapkan pada **search**. Hasil pencarian sering memuat item kurang penting (mis. versi lama dari folder arsip) karena kueri mencari lintas folder. Saran desain: **membedakan item yang ditandai GrayArea/Old'nGray dalam daftar hasil** lewat warna abu-abu (faded), agar pengguna lebih mudah mengenali versi terbaru yang tidak didemosi. Ini menunjukkan prinsip user-subjective dapat memperkaya **desain apa pun**, termasuk search. Para penulis juga sedang mengembangkan **DupliPix** yang sebagian menyembunyikan foto nyaris-duplikat.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Promotion / Demotion principle | Prinsip promosi (tonjolkan item penting) / demosi (redupkan item kurang penting). |
| Salience & accessibility | Keterlihatan visual & kemudahan akses. |
| Clutter | Kekusutan; tumpukan item tak relevan yang mengganggu. |
| Deletion paradox | Paradoks penghapusan; meninjau untuk menghapus juga memakan waktu. |
| Prospect Theory | Teori prospek; teori pengambilan keputusan untung-rugi (Kahneman & Tversky 1979). |
| Archiving | Pengarsipan; memindahkan item keluar dari konteks aslinya (beda dari demosi). |
| Recent version problem | Masalah versi terkini; sulit menemukan versi terbaru yang benar. |
| GrayArea / DMTR / Old'nGray | Tiga prototipe demosi (folder / kontak ponsel / versi berkas). |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 10.1 — "skripsi_final_FIX_revisi3_BENERAN.docx".** Banyak mahasiswa Indonesia menyimpan belasan versi skripsi dengan nama beruntun, lalu bingung mana yang terbaru—persis recent version problem. Old'nGray akan mengaburkan versi lama sehingga versi terbaru terlihat sekilas (kegagalan turun 24%→4%).
>
> **Studi kasus 10.2 — Kontak ponsel Bu Yuni.** Ponsel Bu Yuni penuh kontak lama yang tak pernah ditelepon. DMTR akan otomatis meredupkan kontak yang tak dipakai >6 bulan (≈47% kontak), mempercepat menemukan kontak aktif.

### Temuan Penelitian (dari Buku Sumber)

- Work-around demosi: arsip folder **40%**, memori eksternal **61%**, folder baru **32%**, arsip dalam folder **24%**; **79%** memakai salah satu.
- GrayArea (n=96): clutter turun **13%**; simpan **67%** vs **80%**; hapus **20%→10%**; demosi **23%**; **81%** merasa lebih mudah mendemosi.
- DMTR (n=18): **47%** kontak tak dipakai >6 bulan; ketukan & waktu turun signifikan.
- Old'nGray (n=60): kegagalan **24%→4%**; waktu **17,68→6,56 detik**; **70%** ingin di OS berikutnya.

### Rangkuman

- Prinsip subjective importance: kepentingan menentukan salience & aksesibilitas; terdiri atas promosi dan demosi.
- Demosi adalah opsi tengah keep–delete yang mengatasi hambatan psikologis (Prospect Theory) dengan mempertahankan konteks asli.
- 79% pengguna sudah membuat work-around demosi, memotivasi desain GrayArea, DMTR, Old'nGray.
- Ketiga prototipe terbukti efektif; prinsip demosi juga dapat memperkaya search.

### Latihan & Refleksi

**A. Pemahaman**
1. Jelaskan beda promosi dan demosi.
2. Mengapa demosi berbeda dari pengarsipan?
3. Sebutkan hasil utama evaluasi Old'nGray (kegagalan dan waktu).

**B. Analisis (HOTS)**
4. Hubungkan keempat poin Prospect Theory dengan mengapa orang enggan menghapus. Bagaimana demosi "menipu" hambatan psikologis ini?
5. Mengapa mempertahankan konteks asli (bukan memindah ke arsip) penting menurut temuan Bagian II? Kaitkan dengan preferensi pengambilan berbasis lokasi.
6. GrayArea bersifat manual, DMTR/Old'nGray otomatis. Diskusikan trade-off antara demosi manual dan otomatis dari sisi kontrol pengguna dan beban kognitif.

**C. Tugas Praktik**
7. Pilih satu folder berisi banyak versi berkas. Terapkan "demosi manual": pindahkan versi lama ke bagian bawah (mis. beri awalan `zz_`) tanpa menghapus. Ukur apakah menemukan versi terbaru menjadi lebih cepat, dan refleksikan kaitannya dengan Old'nGray.

---

## Bab 11 — Prinsip Subjective Project Classification (Klasifikasi Proyek Subjektif)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** project fragmentation problem dan tiga hierarki format.
2. **Menjelaskan** mengapa "proyek" adalah atribut subjektif.
3. **Menguraikan** solusi single hierarchy dan desain ProjectFolders.
4. **Membandingkan** dua pendekatan terdahulu: integration through search vs additional structure.
5. **Mengevaluasi** argumen bahwa desain antarmuka dapat mengubah perilaku pengguna.

### Peta Konsep

```
PROJECT FRAGMENTATION: item satu proyek tersebar di 3 hierarki format
   (dokumen / surel / favorit web)
        |
   "Project" = atribut SUBJEKTIF (item sama bisa proyek berbeda bagi orang berbeda)
        |
   Prinsip: item satu proyek dikumpulkan, tanpa memandang format
        |
   Solusi: SINGLE HIERARCHY -> desain ProjectFolders (dirancang, belum dievaluasi)
        |
   Pendekatan terdahulu: (1) integration through search (2) additional structure
   -> keduanya menerima fragmentasi sebagai keniscayaan; ProjectFolders mencegahnya
```

### Materi Inti

#### 11.1 Project Fragmentation Problem

Butir informasi jarang berdiri sendiri: saat mengerjakan dokumen, kita berdiskusi via surel dengan kolaborator, mungkin berbasis data dari situs yang di-bookmark. Idealnya materi terkait mudah diambil dan dilihat bersama (Dumais et al. 2003). Namun pengguna kerap kesulitan mengintegrasikan informasi satu proyek karena tersebar di berbagai aplikasi/folder. Contoh: **Jane**, mahasiswa kimia, punya folder "Chemistry" di **tiga hierarki bergantung-format** (dokumen, surel, favorit). Proyek kimianya **terfragmentasi**: saat mengerjakan kimia, ia harus menavigasi antar-folder terpisah — melelahkan.

> **Definisi.** **Project fragmentation problem** terjadi ketika pengguna yang mengerjakan satu proyek menyimpan item terkait proyek itu dalam **koleksi terpisah berdasarkan format**, lalu juga mengambilnya dari sana (Bergman, Beyth-Marom, & Nachmias 2006).

"Proyek" adalah **atribut subjektif** yang dipilih pengguna; item sama bisa diklasifikasi pada proyek berbeda untuk pengguna berbeda. Contoh: URL hotel konferensi bisa ditaruh di folder bernama konferensi (oleh peserta konferensi) atau folder "Honeymoon" (oleh calon pengantin yang berencana ke hotel sama).

#### 11.2 Prinsip dan Akar Masalah Desain

Prinsip **subjective project classification** menyatakan: desain sebaiknya memungkinkan **semua item satu proyek diklasifikasikan dalam kategori sama, tanpa memandang format teknologi**. Meski organisasi berbasis proyek didorong di sistem eksperimental, desain PIM saat ini justru **menghalanginya** — mendorong pengguna mengklasifikasi menurut proyek **tetapi di dalam hierarki bergantung-format**. Hasilnya **tiga hierarki**: dokumen di My Documents, surel di hierarki kotak surel, favorit di hierarki peramban. Satu-satunya pengecualian: berbagai format dokumen (Word, Excel, PowerPoint) bisa diklasifikasi dalam satu hierarki berkas.

**Motivasi (Bergman, Beyth-Marom, & Nachmias 2006, 2008):** pengguna cenderung merujuk item menurut **proyek**, bukan format. Meski memakai banyak format saat mengerjakan satu proyek, mereka biasanya menyimpannya ke tiga hierarki terpisah. Penamaan konsisten per proyek di ketiga hierarki adalah **pengecualian, bukan aturan**. Yang penting: ketika **desain mendukung**, pengguna **mau** menyimpan item lintas-format dalam satu folder proyek dan mengambilnya bersama; ketika desain tidak mendukung, mereka kembali ke tiga hierarki.

#### 11.3 Solusi Single Hierarchy: ProjectFolders

Untuk mengatasi fragmentasi, diusulkan **solusi hierarki tunggal (single hierarchy solution)**: semua item terkait proyek disimpan dalam folder yang sama tanpa memandang format, dengan menggabungkan tiga hierarki menjadi satu. Salah satu implementasinya adalah **ProjectFolders** (telah **dirancang tetapi belum diimplementasikan/dievaluasi**). ProjectFolders memungkinkan pengguna menyimpan semua dokumen, surel, favorit web, tugas, dan kontak terkait proyek dalam **satu folder, dipisahkan oleh tab**. Saat membuka aplikasi, hanya item terkait yang ditampilkan (surel untuk kotak surel, situs favorit untuk peramban). Solusi ini **tidak** menuntut penyatuan aplikasi PIM, hanya **lokasi penyimpanan default**-nya.

#### 11.4 Pendekatan Terdahulu

Upaya awal mengatasi fragmentasi terbagi dua kategori:

1. **Integrasi melalui pencarian (integration through search).** Alat seperti SIS, Lifestreams, dan Presto memungkinkan mencari item satu proyek lintas-format dalam satu kueri; hasil ditampilkan dalam satu konteks. Kini diterapkan pada mesin pencari Mac OS X dan Windows. Keterbatasan: (a) pengguna lebih memilih navigasi daripada search (Bab 5), dan (b) akurasi search desktop sering mengembalikan item yang hanya terkait longgar, sehingga mengganggu.
2. **Integrasi melalui struktur tambahan (integration through additional structure).** Alat seperti Raton Laveur, UMEA, TaskTracer, SWISH, serta perangkat lunak komersial (OneNote, Snippets, DragStrip) memungkinkan membuat proyek dalam struktur **tambahan** terpisah dari tiga hierarki. Keterbatasan: menambah struktur baru menambah **kompleksitas kognitif** dan satu lagi lokasi pengambilan untuk diingat.

Kedua pendekatan **menerima fragmentasi sebagai keniscayaan**. Sebaliknya, **ProjectFolders mencegah fragmentasi sejak awal**. Sebagian menganggapnya radikal karena menyatukan item dari berbagai aplikasi dan mengubah kebiasaan penyimpanan. Namun desain antarmuka kerap **mendikte** preferensi dan strategi pengguna (Shneiderman & Plaisant 2010). Contoh historis: dahulu tiap aplikasi dokumen menyarankan lokasi penyimpanan terpisah (WordStar vs Lotus Notes vs Photoshop), membuat pengguna menyebar berkas; kini, karena sistem menawarkan **satu lokasi** untuk semua dokumen (mis. My Documents), pengguna menyimpan dokumen lintas-format dalam folder sama. Maka ProjectFolders berpotensi memicu perubahan serupa untuk **semua** item terkait proyek.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Project fragmentation problem | Masalah fragmentasi proyek; item satu proyek tersebar di hierarki format berbeda. |
| Three hierarchies | Tiga hierarki: dokumen, surel, favorit web. |
| Project (sebagai atribut) | Proyek; atribut subjektif pengelompokan item (≈ aktivitas/tugas/peristiwa). |
| Single hierarchy solution | Solusi hierarki tunggal; satu folder untuk semua format dalam satu proyek. |
| ProjectFolders | Desain instansiasi prinsip (folder proyek dengan tab per format). |
| Integration through search / additional structure | Integrasi via pencarian / via struktur tambahan. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 11.1 — Proyek akreditasi prodi.** Dokumen borang ada di My Documents, surel koordinasi di Gmail, dan tautan regulasi di bookmark peramban. Tim harus melompat antar tiga tempat—contoh klasik project fragmentation. Dengan ProjectFolders, semua (dokumen, surel, favorit, tugas, kontak asesor) akan berada dalam satu folder "Akreditasi" berpisah tab.
>
> **Studi kasus 11.2 — Subjektivitas proyek.** Bagi Dosen A, file panduan magang masuk proyek "Mata Kuliah Magang"; bagi Kaprodi, file sama masuk proyek "Kerjasama Industri". Item sama, proyek berbeda—menegaskan "project" sebagai atribut subjektif.

### Temuan Penelitian (dari Buku Sumber)

- Pengguna merujuk item menurut **proyek**, bukan format (Bergman, Beyth-Marom, & Nachmias 2006, 2008).
- Ketika desain mendukung, pengguna **mau** menyimpan item lintas-format dalam satu folder proyek; bila tidak, kembali ke tiga hierarki.
- ProjectFolders **dirancang tetapi belum diimplementasikan/dievaluasi**.
- Perubahan historis (lokasi dokumen tunggal "My Documents") membuktikan desain antarmuka dapat mengubah perilaku.

### Rangkuman

- Project fragmentation: item satu proyek tersebar di tiga hierarki format, menyulitkan kerja terintegrasi.
- "Proyek" adalah atribut subjektif; prinsip menuntut item satu proyek dikumpulkan tanpa memandang format.
- Solusi single hierarchy diwujudkan ProjectFolders (folder proyek berpisah tab), belum dievaluasi.
- Pendekatan terdahulu (search / struktur tambahan) menerima fragmentasi; ProjectFolders mencegahnya. Desain antarmuka dapat mengubah perilaku.

### Latihan & Refleksi

**A. Pemahaman**
1. Definisikan project fragmentation problem dan sebutkan tiga hierarki.
2. Mengapa "proyek" disebut atribut subjektif?
3. Apa inti solusi single hierarchy?

**B. Analisis (HOTS)**
4. Bandingkan "integration through search" dan "additional structure". Mengapa keduanya dianggap kurang ideal dibanding ProjectFolders?
5. Buku sumber memakai contoh historis "My Documents" untuk berargumen bahwa desain mengubah perilaku. Evaluasi kekuatan analogi ini untuk memprediksi keberhasilan ProjectFolders.
6. ProjectFolders belum dievaluasi empiris. Rancang satu studi (metode, peserta, ukuran keberhasilan) untuk mengujinya, dengan mempertimbangkan validitas ekologis (lihat EPIR, Bab 4).

**C. Tugas Praktik**
7. Pilih satu proyek nyata Anda. Daftar semua item terkaitnya beserta lokasi (folder dokumen, label surel, bookmark). Hitung berapa "hierarki" berbeda yang harus Anda kunjungi. Rancang struktur folder proyek tunggal alternatif dan jelaskan keuntungannya.

---

## Bab 12 — Prinsip Subjective Context (Konteks Subjektif)

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** prinsip subjective context dan masalah hilangnya konteks.
2. **Mengidentifikasi** empat atribut konteks: internal, eksternal, sosial, temporal.
3. **Menguraikan** lima implementasi: ChittyChatty, ItemHistory, ContactMap, PiccyChatty, Starlight.
4. **Menjelaskan** mekanisme cotemporal indexing.
5. **Mengevaluasi** bukti deployment yang mendukung prinsip konteks.

### Peta Konsep

```
SUBJECTIVE CONTEXT: ambil informasi dalam KONTEKS yang sama saat sebelumnya dipakai
        |
   4 atribut konteks:
   - Internal (pikiran pengguna)    -> ChittyChatty (cotemporal indexing)
   - Eksternal (item lain yg dibuka)-> ItemHistory (Memex, Bush 1945)
   - Sosial (orang terkait)         -> ContactMap, PiccyChatty
   - Temporal (keadaan/tenggat)     -> Starlight (bintang makin terang dekat tenggat)
        |
   Bukti: deployment 2 tahun ChittyChatty meningkatkan nilai mahasiswa
```

### Materi Inti

#### 12.1 Masalah Hilangnya Konteks

Saat berinteraksi dengan informasi, kita melakukannya dalam suatu **konteks**; ketika interaksi berakhir, konteks **hilang** kecuali sengaja dipertahankan sistem. Riset menunjukkan orang sulit meregenerasi konteks lampau setelah waktu berlalu. Prinsip **subjective context** menyatakan: informasi sebaiknya diambil dalam **konteks yang sama** dengan saat sebelumnya digunakan, untuk menjembatani jeda waktu. **Motivasi:** proses umum PIM adalah menyuling informasi kompleks menjadi ringkasan untuk dipakai kelak (mis. mencatat rapat, meringkas kuliah). Kesulitan lazim: catatan menjadi sulit dipahami karena konteks aslinya terlupa — catatan terlalu singkat, penuh akronim/deskripsi teknis (Whittaker et al. 2008; Kalnikaité & Whittaker 2010).

Analisis isi wawancara **guided tour** (peserta menunjukkan cara mengelola informasinya) menunjukkan **separuh** ucapan peserta merujuk setidaknya satu atribut kontekstual (Bergman, Beyth-Marom, & Nachmias 2008). Empat **atribut konteks**:

- **Internal:** pikiran pengguna saat berinteraksi dengan item.
- **Eksternal (External):** item lain yang sedang ditangani bersamaan.
- **Sosial (Social):** orang lain terkait item (mis. kolaborator).
- **Temporal:** keadaan saat pengguna terakhir meninggalkan item dan rencana kerjanya.

#### 12.2 Lima Implementasi

**(a) ChittyChatty (konteks internal).** Mengatasi kesulitan menafsirkan catatan tanpa konteks. ChittyChatty memungkinkan pengguna merekonstruksi bagian relevan konteks asli dengan **menautkan catatan ke rekaman** konteks, lewat metode **cotemporal indexing (pengindeksan se-waktu)**: catatan pengguna direkam tersinkron dengan rekaman rapat/kuliah. Mengklik sebuah catatan membawa pengguna ke **waktu persis** catatan itu dibuat dan memutar ulang apa yang dikatakan saat itu. Bukti kuat: **deployment kelas dua tahun** menunjukkan ketersediaan sistem saat mencatat dan saat pengambilan **meningkatkan nilai** mahasiswa (yang lebih sering mengakses sistem memperoleh nilai lebih baik); evaluasi terkontrol menunjukkan pengguna sistem **mengungguli** yang memakai catatan tangan/handout (Kalnikaité & Whittaker 2010). Desain serupa efektif untuk video edukasi dan memori percakapan personal.

**(b) ItemHistory (konteks eksternal).** Terinspirasi visi **Memex** Vannevar Bush ("As We May Think", 1945) yang otomatis mengindeks item yang dilihat berurutan dalam "jejak asosiatif". Tujuh puluh tahun kemudian, sistem PIM masih belum memungkinkan mengikuti jejak dari satu item ke item lain yang dilihat **kira-kira bersamaan**. ItemHistory **mengindeks relasi ini otomatis**: saat mengerjakan satu item (mis. makalah kuliah), pengguna membuka beberapa item lain (halaman web, surel, dokumen); ItemHistory memungkinkan melihat dan mengambil **semua item yang terbuka bersamaan** dengan item saat ini.

**(c) ContactMap (konteks sosial).** Mengategorikan informasi pribadi menurut **konteks sosial** (Whittaker et al. 2004). Pengambilan surel sering melibatkan menyebut pengirim; label folder kadang mendeskripsikan individu/kelompok. ContactMap mengidentifikasi kelompok kontak penting dengan menganalisis interaksi surel (kontak yang sering dan lama di-emaili — Whittaker et al. 2002), menyimpulkan relasi dari ko-okurensi di kolom *to/from*. Kelompok ini mengorganisasi informasi desktop (dokumen/surel) lewat klaster spasial, ikon kelompok, dan kode warna. Mengklik kelompok mengambil surel/dokumen yang dipertukarkan; sistem juga mendukung **social reminding** (menandai item actionable per kelompok/kontak). ContactMap **mengungguli** klien surel biasa pada empat tugas komunikasi kerja berorientasi sosial.

**(d) PiccyChatty (konteks sosial).** Memakai **informasi sosial** untuk menyimpulkan kepentingan relatif item bersama (Kalnikaité & Whittaker 2008b). Dideploy dalam konteks edukasi: pengguna mencatat dan memotret saat kuliah; catatan/foto **terkoindeks se-waktu** ke rekaman kuliah (seperti ChittyChatty). Catatan/foto dikumpulkan lintas pengguna; sistem merekam berapa banyak orang mengakses tiap catatan/foto, lalu **menaikkan salience item yang sering diakses** (foto lebih besar atau catatan ditebalkan). Evaluasi: versi dengan informasi sosial **meningkatkan kinerja** pengguna; dalam deployment jangka panjang, mahasiswa pengguna versi sosial memperoleh **nilai kelas lebih tinggi**.

**(e) Starlight (konteks temporal).** Item actionable terdorong keluar pandangan di inbox lalu terlupa. Banyak pengguna menandai pesan penting (mis. bintang Gmail), tetapi pesan tetap bisa terdorong keluar pandangan. **Starlight** memberi pengingat berkelanjutan tentang item actionable dalam tampilan kronologis: menampilkan **bintang** untuk tiap pesan penting di bagian atas layar surel, dan membuat tiap bintang **"bersinar makin terang" saat tenggat mendekat**. Misalnya, sederet bintang menunjukkan jumlah item berbintang (walau hanya satu yang terlihat saat ini), dan bintang yang bersinar menandai tenggat yang mendesak.

### Istilah Kunci

| Istilah Inggris | Penjelasan Bahasa Indonesia |
|---|---|
| Subjective context | Konteks subjektif; situasi saat informasi sebelumnya digunakan. |
| Internal/External/Social/Temporal context | Konteks internal (pikiran)/eksternal (item lain)/sosial (orang)/temporal (waktu-keadaan). |
| Cotemporal indexing | Pengindeksan se-waktu; menyinkronkan catatan dengan rekaman. |
| Guided tour | Tur terpandu; teknik wawancara peserta menunjukkan pengelolaan informasinya. |
| Memex | Mesin asosiatif yang dibayangkan Vannevar Bush (1945). |
| Social reminding | Pengingatan sosial; menandai item actionable per kontak/kelompok. |
| ChittyChatty/ItemHistory/ContactMap/PiccyChatty/Starlight | Lima implementasi prinsip konteks. |

### Contoh / Studi Kasus (Konteks Indonesia)

> **Studi kasus 12.1 — Catatan kuliah Dina.** Dina mencatat "lihat teorema 3" tanpa konteks; sebulan kemudian ia lupa maksudnya. Dengan ChittyChatty (cotemporal indexing), mengklik catatan itu memutar ulang rekaman dosen saat catatan dibuat—konteks internal terpulihkan.
>
> **Studi kasus 12.2 — Inbox Pak Joko.** Surel tugas dari dekan terdorong ke bawah inbox dan nyaris terlewat tenggatnya. Starlight akan menampilkan bintang yang makin terang menjelang tenggat—konteks temporal yang menyelamatkan.

### Temuan Penelitian (dari Buku Sumber)

- Guided tour: **separuh** ucapan peserta merujuk atribut kontekstual (Bergman, Beyth-Marom, & Nachmias 2008).
- ChittyChatty: deployment **dua tahun** meningkatkan nilai; akses lebih sering → nilai lebih baik; mengungguli catatan tangan/handout (Kalnikaité & Whittaker 2010).
- ContactMap: mengungguli klien surel biasa pada empat tugas komunikasi sosial.
- PiccyChatty: versi dengan informasi sosial meningkatkan kinerja & nilai kelas.

### Rangkuman

- Konteks hilang setelah interaksi berakhir kecuali sengaja dipertahankan; prinsip subjective context menjembatani jeda waktu.
- Empat atribut konteks: internal, eksternal, sosial, temporal.
- Lima implementasi: ChittyChatty (internal), ItemHistory (eksternal), ContactMap & PiccyChatty (sosial), Starlight (temporal).
- Beberapa di antaranya dievaluasi positif dalam deployment nyata.

### Latihan & Refleksi

**A. Pemahaman**
1. Sebutkan empat atribut konteks beserta contoh implementasinya.
2. Jelaskan mekanisme cotemporal indexing pada ChittyChatty.
3. Bagaimana Starlight memanfaatkan konteks temporal?

**B. Analisis (HOTS)**
4. Mengapa bukti "akses lebih sering → nilai lebih baik" pada deployment ChittyChatty merupakan dukungan kuat (sekaligus terbatas) bagi prinsip konteks? Diskusikan kemungkinan penjelasan alternatif.
5. ContactMap dan PiccyChatty sama-sama mengeksploitasi konteks sosial tetapi dengan cara berbeda. Bandingkan keduanya.
6. Pilih satu atribut konteks dan rancang fitur baru (selain kelima contoh) yang mengimplementasikannya. Jelaskan bagaimana fitur Anda menangkap atribut tersebut.

**C. Tugas Praktik**
7. Selama mengikuti satu kuliah, catat secara digital dan beri penanda waktu (mis. rekam audio sambil mencatat). Seminggu kemudian, coba pahami catatan Anda dengan dan tanpa rekaman. Tuliskan refleksi tentang nilai cotemporal indexing.

---

## Rangkuman Bagian III

Bagian III berfokus pada bagaimana desain baru dapat membantu pengguna "memainkan permainan PIM" lebih efektif. Pendekatan **user-subjective** dan ketiga prinsipnya diperkenalkan, didemonstrasikan lewat **sembilan skema desain**. Dukungan untuk pendekatan ini bersifat ganda: *pertama*, riset awal (Bergman, Beyth-Marom, & Nachmias 2008) menunjukkan pengguna sistem PIM saat ini melakukan **work-around** untuk mengeksploitasi atribut subjektif dalam praktik alaminya; *kedua*, implementasi lanjutan menunjukkan **evaluasi pengguna positif** untuk enam desain berbeda yang diturunkan dari prinsip-prinsip ini.

Tiga catatan kunci. (1) Berbeda dari pendekatan search/tag everything, pendekatan user-subjective **tidak berusaha menggantikan** metode hierarkis; ia memandang folder sebagai pemberian dan berusaha **memperbaikinya** — menyatukan hierarki (ProjectFolders) dan menambah fitur (GrayArea). (2) Para penulis sengaja **tidak mematenkan** desainnya agar pengguna semua sistem operasi dapat memanfaatkannya; mereka berharap generasi berikutnya Windows, Mac, Linux, dan Chrome menyertakan desain seperti GrayArea dan Old'nGray, serta ponsel menyertakan DMTR. (3) Yang terpenting, pendekatan ini **generatif**: prinsip abstrak telah melahirkan desain konkret yang berguna dan sebelumnya tak terbayangkan; diharapkan perancang masa depan memakai pendekatan ini untuk menciptakan teknologi PIM dengan cara-cara baru yang tak terduga.

---

# Bab Penutup: Sintesis, Kesimpulan, dan Implikasi untuk Pembaca Indonesia

### Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. **Mensintesis** argumen ketiga bagian buku menjadi satu narasi utuh.
2. **Mengevaluasi** arah teknologi masa depan PIM yang diuraikan buku sumber.
3. **Merumuskan** implikasi praktis bagi mahasiswa, dosen, dan pekerja di Indonesia.
4. **Menjelaskan** sikap berhati-hati buku sumber terhadap "praktik baik (best practices)".
5. **Mengidentifikasi** arah riset masa depan (metode dan kerangka konseptual).

### 1. Sintesis Tiga Bagian

Buku sumber membangun argumen berlapis:

- **Bagian I** menetapkan bahwa ilmu informasi terlalu berfokus pada **konsumsi informasi publik baru** dan mengabaikan **kurasi informasi pribadi**. Kurasi dimodelkan tiga tahap (keeping, management, exploitation). Temuan utamanya: orang cenderung **overkeep**, kesulitan mengorganisasi item actionable, dan tetap bertumpu pada metode manual untuk pengambilan. Keeping dan management sulit karena menuntut **prediksi masa depan**.
- **Bagian II** mendokumentasikan **dominasi navigasi** dan kegagalan alternatif (search, tag, GIM) yang berhasil di domain lain namun tak menggeneralisasi ke PIM. Kuncinya adalah **familiaritas**: dalam PIM, pengguna mengorganisasi dan mengambil sendiri koleksi kecilnya. Bab 8 memberi penjelasan **kognitif-neurologis**: navigasi kurang menuntut atensi verbal dan memakai struktur otak navigasi spasial yang "tua", sedangkan search menyedot sumber daya linguistik.
- **Bagian III** menawarkan solusi konstruktif: pendekatan **user-subjective**, yang **tidak mengganti** folder melainkan memperkayanya dengan tiga prinsip (importance, project, context) dan sembilan skema desain, beberapa terbukti positif dalam deployment.

Benang merah keseluruhan: **PIM adalah permainan yang berbeda**, dengan aturan main yang ditentukan oleh fakta bahwa penyimpan dan pengambil adalah orang yang sama.

### 2. Penjelasan Psikologis sebagai Kontribusi Inti

Buku sumber menegaskan salah satu kontribusi terpentingnya adalah **menjelaskan fenomena PIM dengan psikologi**. Contoh: **overkeeping** dijelaskan lewat **Prospect Theory** (Kahneman & Tversky 1979) — pengguna berfokus pada kehilangan informasi, melebih-lebihkan risiko penghapusan, meremehkan biaya pengambilan. **Preferensi navigasi** dijelaskan lewat **tuntutan pemrosesan informasi** — search membutuhkan memori kerja verbal, navigasi memakai proses lokasi yang lebih primitif. **Pentingnya organisasi aktif** (saat memfail) dijelaskan oleh psikologi kognitif tentang peran organisasi aktif bagi rekoleksi — yang juga menjelaskan kesulitan GIM (hilangnya organisasi personal aktif).

### 3. Arah Teknologi Masa Depan (menurut Buku Sumber)

Buku sumber memetakan beberapa arah, dengan sikap **berhati-hati** karena sejarah PIM dipenuhi teknologi yang menjanjikan namun gagal:

- **Machine learning & semantic desktop:** mengorganisasi data otomatis. Belum ada deployment sukses dengan populasi pengguna nyata. Varian lebih sederhana (analisis otomatis untuk metadata, mis. pengenalan wajah pada foto) menjanjikan, tetapi kelemahannya **menghilangkan organisasi aktif pengguna** yang penting bagi pengambilan; metadata sebaiknya **diintegrasikan ke** hierarki yang ada.
- **Algoritma prediktif:** memanfaatkan bias kebaruan (History, tombol Back, daftar dokumen terkini). Cockburn dkk. mengembangkan algoritma yang memprediksi aksi berikutnya dan menggabungkannya dengan navigasi/search, mengurangi waktu pengambilan.
- **Teknologi actionable:** menangani reminding/tenggat. Pengecualian sukses: add-in **boomerang** dan **Inbox by Gmail** (fitur "snooze"), serta asisten kalender otomatis (mis. Google Calendar Goals).
- **GIM:** tumbuh pesat (Dropbox, Google Drive, OneDrive); dibutuhkan teknologi untuk organisasi bersama yang dapat diakses bersama — mungkin via penstrukturan sosial (prinsip konteks) atau hibrida PIM/GIM dengan **tampilan personal** atas data bersama.
- **Penangkapan & pengambilan multi-perangkat:** informasi tersebar di banyak perangkat memperumit pengambilan (sudah terlihat pada foto). Menyatukan perangkat adalah tantangan teknis besar; sebagian perilaku kurasi akan **bergantung perangkat** (mis. ukuran layar ponsel).
- **Lifelogging & quantified self:** arsip besar data yang ditangkap pasif (detak jantung, langkah, lokasi, gambar). Berbeda dari data PIM biasa; klaim "mengingat segalanya" telah dikritik. Namun perangkat yang dapat dikenakan dapat membantu menghasilkan **konteks user-subjective** yang kaya.

### 4. Sikap terhadap "Praktik Baik"

Penting dicatat: buku sumber **menolak memberi nasihat praktik baik** secara gegabah. Alasannya: (1) sulit mengukur apakah suatu praktik "baik"; (2) **perbedaan individu lazim** dalam PIM, sehingga praktik yang baik bagi sebagian orang belum tentu baik bagi yang lain. Mereka merujuk studi metode Delphi (Jones et al. 2015) yang mengidentifikasi **36 praktik PIM kunci** beserta pro-kontranya, dan menganjurkan pendekatan **edukatif**: memperluas wawasan pengguna tentang teknologi/strategi alternatif, lalu membiarkan mereka memilih.

> **Catatan untuk pembaca buku ajar.** Karena buku sumber menahan diri dari resep universal, "implikasi praktis" di bawah ini adalah **elaborasi pedagogis** yang diturunkan secara hati-hati dari temuan, **bukan** klaim langsung para penulis. Terapkan dengan mempertimbangkan perbedaan individu Anda sendiri.

### 5. Implikasi Praktis untuk Pembaca Indonesia (Elaborasi Pedagogis)

Berikut sejumlah implikasi yang dapat dipertimbangkan mahasiswa, dosen, dan pekerja kantoran di Indonesia. Setiap butir dikaitkan dengan temuan sumbernya.

1. **Navigasi folder layak dipertahankan.** Karena navigasi terbukti cepat, berhasil (94%), dan hemat atensi (Bab 4, 8), tidak perlu merasa "ketinggalan zaman" karena masih memakai folder. Search adalah **tangga darurat** yang baik, bukan pengganti.
2. **Terapkan heuristik ~21 item per folder.** Bila satu folder memuat jauh lebih dari 21 item, pertimbangkan menambah satu tingkat subfolder (Bab 4).
3. **Waspadai overkeeping.** Karena penundaan jarang ditindaklanjuti (Bab 2), jadwalkan "bersih-bersih" berkala secara sengaja, sadar bahwa Anda cenderung menilai informasi terlalu tinggi (loss aversion).
4. **Untuk item actionable, jaga keterlihatan.** Item yang menuntut tindakan sebaiknya tetap terlihat (inbox/desktop) atau memakai fitur "snooze"/pengingat (Bab 3, 12), karena folder to-do cenderung ditinggalkan (95%).
5. **Hati-hati berbagi via repositori bersama.** Untuk kolaborasi, pengambilan dari folder buatan orang lain rawan gagal (28%); pertimbangkan tetap menata salinan sendiri (PIM) atau menyepakati skema organisasi sejak awal (Bab 7).
6. **Beri nama folder/berkas berbasis waktu untuk foto/arsip lama.** Skema berbasis waktu (mis. "2024-Wisuda") terbukti lebih berhasil untuk pengambilan foto lama (Bab 4).
7. **Manfaatkan konteks.** Saat mencatat kuliah/rapat, simpan konteks (rekaman, item terkait, orang terkait) agar catatan tetap bermakna kelak (Bab 12).
8. **Kenali tipe diri Anda.** Filer atau piler, conscientious atau neurotik — tidak ada satu strategi untuk semua (Bab 3). Pilih strategi yang sesuai disposisi Anda.

### 6. Arah Riset Masa Depan (menurut Buku Sumber)

- **Memperluas metode:** dari studi eksploratif/kualitatif menuju pendekatan **kuantitatif** (mis. EPIR yang diperluas ke fase keeping/management, analisis struktur otomatis, dan logfile dengan kepekaan privasi).
- **Mengevaluasi desain baru:** menuntut implementasi dan evaluasi prototipe yang andal dan berfitur lengkap — proses mahal namun perlu.
- **Kerangka konseptual baru:** menjelaskan (bukan sekadar mendeskripsikan) perilaku PIM, dan meneliti **relasi antarproses** kurasi. Bergman (2013) memetakan **lima belas variabel** kunci yang mencirikan perilaku PIM untuk memfasilitasi riset kuantitatif (mis. depth & size folder yang memengaruhi keberhasilan/efisiensi pengambilan).

### 7. Penutup Buku Sumber

Para penulis menutup dengan menegaskan bahwa **kurasi berada di jantung penggunaan komputer sehari-hari** dan fundamental bagi banyak aktivitas daring. Mereka berharap buku ini menjadi landasan ilmiah dan inspirasi bagi kontribusi metode, teknologi, dan teori transformatif di bidang PIM.

### Rangkuman

- Tiga bagian buku menyatu dalam tesis: PIM berbeda karena penyimpan = pengambil.
- Kontribusi inti: penjelasan **psikologis** atas fenomena PIM (Prospect Theory, atensi verbal, organisasi aktif).
- Teknologi masa depan (ML, algoritma prediktif, actionable tech, GIM, multi-perangkat, lifelogging) menjanjikan tetapi harus dievaluasi empiris.
- Buku sumber menahan diri dari "praktik baik" universal karena perbedaan individu; implikasi praktis di buku ajar ini bersifat elaborasi.
- Arah riset: metode kuantitatif, evaluasi desain, kerangka konseptual penjelas.

### Latihan & Refleksi

**A. Pemahaman**
1. Rangkum tesis utama masing-masing bagian buku dalam satu kalimat.
2. Mengapa buku sumber enggan memberi nasihat "praktik baik"?
3. Sebutkan tiga arah teknologi masa depan PIM.

**B. Analisis (HOTS)**
4. Pilih satu temuan dari Bagian I/II dan tunjukkan bagaimana satu prinsip user-subjective (Bagian III) menjawabnya. Jelaskan rantai argumennya.
5. Lifelogging menghasilkan data yang "berbeda" dari data PIM biasa. Diskusikan mengapa, dan apakah pendekatan user-subjective tetap relevan untuk data semacam itu.
6. Evaluasi pernyataan: "Karena navigasi berakar neurologis, investasi pada AI untuk organisasi otomatis sia-sia." Setujukah Anda? Dukung dengan temuan dari beberapa bab.

**C. Tugas Praktik**
7. Susun "rencana kurasi pribadi" satu halaman untuk diri Anda yang mengintegrasikan minimal lima implikasi praktis (butir 1–8 di atas), disertai justifikasi dari bab terkait. Tandai mana yang Anda sesuaikan dengan disposisi/perbedaan individu Anda.

---

## Glosarium

Daftar istilah penting PIM (Inggris → Indonesia). Definisi diselaraskan dengan penggunaan dalam buku sumber.

| Istilah (EN) | Padanan/Penjelasan (ID) |
|---|---|
| **Personal Information Management (PIM)** | Manajemen Informasi Pribadi; aktivitas individu menyimpan butir informasi pribadi untuk diambil kembali kelak. |
| **Curation** | Kurasi; proses aktif memilih, mengorganisasi, dan mengakses koleksi pribadi. |
| **Curation life cycle** | Daur hidup kurasi; model tiga tahap keeping–management–exploitation. |
| **Keeping** | Penyimpanan; keputusan apa yang dipertahankan dalam koleksi. |
| **Management** | Pengelolaan; pengorganisasian informasi yang telah disimpan. |
| **Exploitation** | Pemanfaatan; pengambilan kembali (retrieval) informasi. |
| **Information item** | Butir informasi; satu unit data (dokumen, surel, foto, bookmark, kontak). |
| **Actionable item** | Butir yang menuntut tindakan, sering bertenggat. |
| **Informative item** | Butir informatif yang tidak menuntut tindakan bertenggat. |
| **Uniqueness** | Keunikan; apakah suatu butir hanya ada pada satu salinan milik pengguna. |
| **Active/Passive accumulation** | Akumulasi aktif (perlu tindakan menyimpan) vs pasif (menumpuk otomatis). |
| **Reminding** | Pengingatan; strategi agar item actionable tidak terlupakan. |
| **Overkeeping** | Menyimpan berlebihan, termasuk item yang tak pernah diakses. |
| **Information overload** | Kelebihan beban informasi; waktu tak cukup memproses semua input. |
| **Deferred evaluation / Deferral** | Evaluasi/keputusan tertunda menunggu kepastian nilai. |
| **Loss aversion** | Penghindaran kerugian; rugi terasa lebih besar daripada untung setara. |
| **Prospect Theory** | Teori prospek; teori pengambilan keputusan untung-rugi (Kahneman & Tversky 1979). |
| **One-touch model** | Model satu-sentuhan; ideal memproses pesan sekali lalu menghapus. |
| **Post retrieval value** | Nilai pasca-pengambilan; nilai sumber web yang baru disadari setelah tak dipertahankan. |
| **Filing / Piling** | Memfail (hierarkis sistematis) / menumpuk (laissez-faire). |
| **Premature filing** | Memfail prematur; memfail item sebelum nilainya jelas. |
| **No filing / Frequent filing / Spring cleaning** | Tanpa memfail / sering memfail / bersih-bersih berkala (strategi surel). |
| **Failed folder** | Folder gagal; folder yang hanya memuat 1–2 item. |
| **Mental cueing / External cueing** | Pengisyaratan mental (memori) / eksternal (label, isi folder). |
| **Semantic / Temporal organization** | Organisasi semantik (kemiripan konsep) / temporal (waktu). |
| **Hierarchy / Folder** | Hierarki / folder; struktur penyimpanan berbasis lokasi bertingkat. |
| **Navigation** | Navigasi; traversal manual dan pemindaian visual hierarki folder. |
| **Search** | Pencarian; pengambilan via kueri atribut/kata kunci. |
| **Recency / Frequency** | Kebaruan / frekuensi; basis daftar dokumen terkini, tombol Back, dsb. |
| **Ecological validity** | Validitas ekologis; sejauh mana studi mencerminkan kondisi nyata. |
| **EPIR (Elicited Personal Information Retrieval)** | Metode pengambilan item pribadi terkendali dari koleksi sendiri. |
| **Preparatory / Opportunistic retrieval** | Pengambilan persiapan (folder) vs oportunistik (scroll/sort/search). |
| **Search everything / Tag everything** | Pendekatan yang mengusulkan search/tag menggantikan folder. |
| **Real-time / Incremental / Cross-format search** | Pencarian waktu-nyata / inkremental / lintas-format. |
| **Tag / Tagging** | Tanda/penandaan; metadata kata kunci. |
| **Multiple / Single classification** | Klasifikasi ganda (banyak label) / tunggal (satu lokasi/label). |
| **Tag-label / Folder-label (Gmail)** | Label sebagai tag (tetap di inbox) / sebagai folder (item dipindahkan). |
| **Vocabulary problem** | Masalah kosakata; orang berbeda memakai istilah berbeda. |
| **Group Information Management (GIM)** | Manajemen Informasi Kelompok; organisasi sebagian didelegasikan ke orang lain. |
| **Subjectivity of classification** | Subjektivitas klasifikasi; kategori tak bisa diturunkan dari item itu sendiri. |
| **Constructivism** | Konstruktivisme; pembelajaran/pemrosesan aktif memperkuat memori. |
| **Semantic / Episodic memory** | Memori semantik (pengetahuan) / episodik (pengalaman). |
| **Locus of control** | Pusat kendali; tingkat kendali seseorang atas situasi. |
| **Dual-task paradigm** | Paradigma tugas-ganda; mengukur alokasi atensi antar dua tugas. |
| **Working memory** | Memori kerja; sistem penyimpanan sementara terbatas. |
| **Phonological loop / Visuospatial sketchpad** | Lingkar fonologis (verbal) / papan-sketsa visuospasial (visual). |
| **fMRI** | Functional magnetic resonance imaging; pencitraan aktivitas otak. |
| **User-subjective approach** | Pendekatan yang memanfaatkan atribut bergantung-pengguna dalam desain PIM. |
| **Public / Subjective attribute** | Atribut publik (objektif) / subjektif (bergantung pengguna). |
| **Subjective Importance principle** | Prinsip kepentingan subjektif; kepentingan menentukan salience & aksesibilitas. |
| **Promotion / Demotion** | Promosi (tonjolkan item penting) / demosi (redupkan item kurang penting). |
| **Deletion paradox** | Paradoks penghapusan; meninjau untuk menghapus juga memakan waktu. |
| **Subjective Project Classification principle** | Prinsip klasifikasi proyek subjektif; item satu proyek dikumpulkan tanpa memandang format. |
| **Project fragmentation problem** | Masalah fragmentasi proyek; item satu proyek tersebar di hierarki format berbeda. |
| **Single hierarchy solution / ProjectFolders** | Solusi hierarki tunggal / desain folder proyek berpisah tab. |
| **Subjective Context principle** | Prinsip konteks subjektif; informasi diambil dalam konteks penggunaan sebelumnya. |
| **Cotemporal indexing** | Pengindeksan se-waktu; menyinkronkan catatan dengan rekaman. |
| **Memex** | Mesin asosiatif yang dibayangkan Vannevar Bush (1945). |
| **Semantic desktop** | Desktop semantik; penerapan machine learning untuk mengategorikan koleksi pribadi. |
| **Lifelogging / Quantified self** | Pencatatan-hidup / diri-terkuantifikasi; arsip data pasif dari perangkat yang dapat dikenakan. |

---

## Daftar Pustaka

### Sumber Utama (Buku yang Diajarkan)

Bergman, O., & Whittaker, S. (2016). *The Science of Managing Our Digital Stuff*. Cambridge, MA: The MIT Press. ISBN 9780262035170.

### Rujukan yang Disebut di dalam Buku Sumber

> Catatan: daftar berikut memuat karya yang **secara eksplisit dirujuk dalam teks buku sumber** dan terverifikasi pada bagian References buku tersebut. Daftar ini bukan bibliografi lengkap buku sumber, melainkan rujukan yang dipakai dalam buku ajar ini. Rincian penerbitan diambil sebagaimana tercantum pada bagian References buku sumber.

- Abrams, D., Baecker, R., & Chignell, M. (1998). Information archiving with bookmarks: Personal Web space construction and organization. *CHI 1998*.
- Aula, A., Jhaveri, N., & Käki, M. (2005). Information search and re-access strategies of experienced web users. *WWW 2005*.
- Baddeley, A. (1992). Working memory. *Science*, 255(5044), 556–559.
- Baddeley, A. (1997). *Human Memory: Theory and Practice*. Psychology Press.
- Bälter, O. (2000). Keystroke level analysis of email message organization. *CHI 2000*.
- Bellotti, V., Ducheneaut, N., Howard, M., & Smith, I. (2003). Taking email to task: The design and evaluation of a task management centered email tool. *CHI 2003*.
- Bellotti, V., Ducheneaut, N., Howard, M., Smith, I., & Grinter, R. (2005). Quality versus quantity: E-mail-centric task management and its relation to overload. *Human–Computer Interaction*, 20(1–2), 89–138.
- Bellotti, V., & Smith, I. (2000). Informing the design of an information management system with iterative fieldwork. *DIS 2000*.
- Benn, Y., Bergman, O., Glazer, L., Arent, P., Wilkinson, I. D., Varley, R., & Whittaker, S. (2015). Navigating through digital folders uses the same brain structures as real world navigation. *Scientific Reports*, 5.
- Bergman, O. (2013). Variables for personal information management research. *Aslib Proceedings*, 65(5), 464–483.
- Bergman, O., Beyth-Marom, R., Leopold, A., Hadar, D., & Dekel, A. (2000). From "Learning-by-Viewing" to "Learning-by-Doing": A video annotation educational technology tool. *ED-MEDIA 2000*, 1555–1556.
- Bergman, O., Beyth-Marom, R., & Nachmias, R. (2003). The user-subjective approach to personal information management systems. *Journal of the American Society for Information Science and Technology*, 54(9), 872–878.
- Bergman, O., Beyth-Marom, R., & Nachmias, R. (2006). The project fragmentation problem in personal information management. *CHI 2006*, 271–274.
- Bergman, O., Beyth-Marom, R., & Nachmias, R. (2008). The user-subjective approach to personal information management systems design: Evidence and implementations. *Journal of the American Society for Information Science and Technology*, 59(2), 235–246.
- Bergman, O., Beyth-Marom, R., Nachmias, R., Gradovitch, N., & Whittaker, S. (2008). Improved search engines and navigation preference in personal information management. *ACM Transactions on Information Systems*, 26(4), 1–24.
- Bergman, O., Elyada, O., Dvir, N., Vaitzman, Y., & Ben Ami, A. (2015). Spotting the latest version of a file with Old'nGray. *Interacting with Computers*, 27(6), 630–639. [Desain Old'nGray; dirujuk dalam teks sebagai Bergman et al. 2014.]
- Bergman, O., Gradovitch, N., Bar-Ilan, J., & Beyth-Marom, R. (2013a). Folder vs. tag preference in personal information management. *Journal of the American Society for Information Science and Technology*, 64(10), 1995–2012.
- Bergman, O., Gradovitch, N., Bar-Ilan, J., & Beyth-Marom, R. (2013b). Tagging personal information: A contrast between attitudes and behavior. *Proceedings of ASIS&T*, 1–8.
- Bergman, O., Komninos, A., Liarokapis, D., & Clarke, J. (2012). You never call: Demoting unused contacts on mobile phones using DMTR. *Personal and Ubiquitous Computing*, 16(6), 757–766.
- Bergman, O., Tene-Rubinstein, M., & Shalom, J. (2013). The use of attention resources in navigation vs. search. *Personal and Ubiquitous Computing*, 17(3), 583–590.
- Bergman, O., Tucker, S., Beyth-Marom, R., Cutrell, E., & Whittaker, S. (2009). It's not that important: Demoting personal information of low subjective importance using GrayArea. *CHI 2009*, 269–278.
- Bergman, O., Whittaker, S., & Falk, N. (2014). Shared files: The retrieval perspective. *Journal of the American Society for Information Science and Technology*, 65(10), 1949–1963.
- Bergman, O., Whittaker, S., Sanderson, M., Nachmias, R., & Ramamoorthy, A. (2010). The effect of folder structure on personal file navigation. *Journal of the American Society for Information Science and Technology*, 61(12), 2426–2441.
- Bergman, O., Whittaker, S., Sanderson, M., Nachmias, R., & Ramamoorthy, A. (2012). How do we find personal files? The effect of OS, presentation and depth on file navigation. *CHI 2012*, 2977–2980.
- Berlin, L. M., Jeffries, R., O'Day, V. L., Paepcke, A., & Wharton, C. (1993). Where did you put it? Issues in the design and use of a group memory. *INTERACT '93 & CHI '93*, 23–30.
- Blanc-Brude, T., & Scapin, D. L. (2007). What do people recall about their documents? Implications for desktop search tools. *IUI 2007*, 102–111.
- Blau, M., Madmon, S., & Bergman, O. (2013). The effect of computer literacy on the percentage of personal file search. *Chais Conference 2013*, 92–93.
- Boardman, R. (2004). *Improving Tool Support for Personal Information Management*. PhD diss., Imperial College, London.
- Boardman, R., & Sasse, M. A. (2004). "Stuff goes into the computer and doesn't come out": A cross-tool study of personal information management. *CHI 2004*.
- Bruce, H. (2005). Personal anticipated information need. *Information Research*, 10(3).
- Bruce, H., Jones, W., & Dumais, S. (2004). Information behaviour that keeps found things found. *Information Research*, 10(1).
- Bush, V. (1945). As we may think. *Atlantic Monthly*, 176(1), 101–108.
- Catledge, L. D., & Pitkow, J. E. (1995). Characterizing browsing strategies in the World-Wide Web. *Computer Networks and ISDN Systems*, 27(6), 1065–1073.
- Civan, A., Jones, W., Klasnja, P., & Bruce, H. (2008). Better to organize personal information by folders or by tags? The devil is in the details. *Proceedings of ASIS&T*, 1–13.
- Cockburn, A., & Greenberg, S. (2000). Issues of page representation and organisation in web browser's revisitation tools. *Australasian Journal of Information Systems*, 7(2), 120–127.
- Collins, A. M., & Loftus, E. F. (1975). A spreading-activation theory of semantic processing. *Psychological Review*, 82(6), 407–428.
- Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684.
- Cutrell, E., Dumais, S. T., & Teevan, J. (2006). Searching to eliminate personal information management. *Communications of the ACM*, 49(1), 58–64.
- Cutrell, E., Robbins, D. C., Dumais, S. T., & Sarin, R. (2006). Fast, flexible filtering with Phlat. *CHI 2006*, 261–270.
- Dabbish, L. A., Kraut, R. E., Fussell, S., & Kiesler, S. (2005). Understanding email use: Predicting action on a message. *CHI 2005*.
- Dourish, P., Edwards, W. K., LaMarca, A., Lamping, J., Petersen, K., Salisbury, M., Terry, D. B., & Thornton, J. (2000). Extending document management systems with user-specific active properties. *ACM Transactions on Information Systems*, 18(2), 140–170.
- Dourish, P., Edwards, W. K., LaMarca, A., & Salisbury, M. (1999). Presto: An experimental architecture for fluid interactive document spaces. *ACM Transactions on Computer–Human Interaction*, 6(2), 133–161.
- Ducheneaut, N., & Bellotti, V. (2001). E-mail as habitat. *interactions*, 8(5), 30–38.
- Dumais, S. T., Cutrell, E., Cadiz, J. J., Jancke, G., Sarin, R., & Robbins, D. C. (2003). Stuff I've Seen: A system for personal information retrieval and re-use. *SIGIR 2003*, 72–79.
- Elsweiler, D., Baillie, M., & Ruthven, I. (2008). Exploring memory in email refinding. *ACM Transactions on Information Systems*, 26(4), 1–36.
- Elsweiler, D., Baillie, M., & Ruthven, I. (2011). What makes re-finding information difficult? A study of email re-finding. *Advances in Information Retrieval*, 568–579.
- Erickson, T. (2006). From PIM to GIM: Personal information management in group contexts. *Communications of the ACM*, 49(1), 74–75.
- Fertig, S., Freeman, E., & Gelernter, D. (1996a). "Finding and reminding" reconsidered. *SIGCHI Bulletin*, 28(1), 66–69.
- Fertig, S., Freeman, E., & Gelernter, D. (1996b). Lifestreams: An alternative to the desktop metaphor. *CHI 1996 Companion*, 410–411.
- Fisher, D., Brush, A. J., Gleave, E., & Smith, M. A. (2006). Revisiting Whittaker and Sidner's "email overload" ten years later. *CSCW 2006*.
- Fitchett, S., & Cockburn, A. (2012). AccessRank: Predicting what users will do next. *CHI 2012*, 2239–2242.
- Fitchett, S., & Cockburn, A. (2015). An empirical characterisation of file retrieval. *International Journal of Human–Computer Studies*, 74, 1–13.
- Fitchett, S., Cockburn, A., & Gutwin, C. (2013). Improving navigation-based file retrieval. *CHI 2013*, 2329–2338.
- Fitchett, S., Cockburn, A., & Gutwin, C. (2014). Finder Highlights: Field evaluation and design of an augmented file browser. *CHI 2014*, 3685–3694.
- Furnas, G. W., et al. (2006). Why do tagging systems work? *CHI 2006 Extended Abstracts*, 36–39.
- Gilbert, D. (2009). *Stumbling on Happiness*. Vintage.
- Golder, S. A., & Huberman, B. A. (2006). Usage patterns of collaborative tagging systems. *Journal of Information Science*, 32(2), 198–208.
- Gonçalves, D., & Jorge, J. A. (2004). "Tell me a story": Issues on the design of document retrieval systems. *Engineering Human Computer Interaction*.
- Gwizdka, J. (2004). Email task management styles: The cleaners and the keepers. *CHI 2004 Extended Abstracts*.
- Gwizdka, J. (2010). Distribution of cognitive load in web search. *Journal of the American Society for Information Science and Technology*, 61(11), 2167–2187.
- Hsieh, et al. (2008). [Studi perbandingan tag vs hierarki; dirujuk dalam Bab 6 buku sumber.]
- John, O. P. (1990). The "Big Five" factor taxonomy. In *Handbook of Personality: Theory and Research*.
- Jones, W. (2004). Finders, keepers? The present and future perfect in support of personal information management. *First Monday*, 9(3).
- Jones, W. (2007). *Keeping Found Things Found: The Study and Practice of Personal Information Management*. Morgan Kaufmann.
- Jones, W., & Teevan, J. (Eds.). (2007). *Personal Information Management*. University of Washington Press.
- Jones, W., Phuwanartnurak, A. J., Gill, R., & Bruce, H. (2005). Don't take my folders away! Organizing personal information to get things done. *CHI 2005 Extended Abstracts*, 1505–1508.
- Jones, W., et al. (2015). [Studi metode Delphi tentang praktik PIM; dirujuk dalam bab Kesimpulan.]
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291.
- Kalnikaité, V., & Whittaker, S. (2007). Software or wetware? Discovering when and why people use digital prosthetic memory. *CHI 2007*.
- Kalnikaité, V., & Whittaker, S. (2008a). Cueing digital memory: How and why do digital notes help us remember? *BCS HCI 2008*.
- Kalnikaité, V., & Whittaker, S. (2008b). Social summarization: Does social feedback improve access to speech data? *CSCW 2008*.
- Kalnikaité, V., & Whittaker, S. (2010). [Evaluasi ChittyChatty/PiccyChatty dalam konteks edukasi.]
- Kaptelinin, V. (2003). UMEA: Translating interaction histories into project contexts. *CHI 2003*.
- Karlson, A. K., Smith, G., & Lee, B. (2011). Which version is this? Improving the desktop experience within a copy-aware computing ecosystem. *CHI 2011*.
- Kirk, D., Sellen, A., Rother, C., & Wood, K. (2006). Understanding photowork. *CHI 2006*.
- Kwasnik, B. H. (1991). The importance of factors that are not document attributes in the organisation of personal documents. *Journal of Documentation*, 47(4), 389–398.
- Lansdale, M. (1988). The psychology of personal information management. *Applied Ergonomics*, 19(1), 55–66.
- Lutters, W. G., Ackerman, M. S., & Zhou, X. (2007). Group information management. In *Personal Information Management*.
- Malone, T. W. (1983). How do people organize their desks? Implications for the design of office information systems. *ACM Transactions on Information Systems*, 1(1), 99–112.
- Marshall, C. C. (2008a, 2008b). Rethinking personal digital archiving (Parts 1 & 2). *D-Lib Magazine*, 14(3/4).
- Massey, C., TenBrook, S., Tatum, C., & Whittaker, S. (2014). PIM and personality: What do our attempts to organize say about us? *CHI 2014*.
- Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
- Millen, D. R., Feinberg, J., & Kerr, B. (2006). Dogear: Social bookmarking in the enterprise. *CHI 2006*.
- Neisser, U. (1964). Visual search. *Scientific American*, 210(6), 94–102.
- Obendorf, H., Weinreich, H., Herder, E., & Mayer, M. (2007). Web page revisitation revisited. *CHI 2007*, 597–606.
- Pak, R., Pautz, S., & Iden, R. (2007). Information organization and retrieval: An assessment of taxonomical and tagging systems. *Cognitive Technology*, 12(1), 31–44.
- Petrelli, D., Whittaker, S., & Brockmeier, J. (2008). AutoTopography: What can physical mementos tell us about digital memories? *CHI 2008*.
- Pirolli, P., & Card, S. (1995). Information foraging in information access environments. *CHI 1995*.
- Quan, D., Bakshi, K., Huynh, D., & Karger, D. R. (2003). User interfaces for supporting multiple categorization. *INTERACT 2003*.
- Rader, E. (2009). Yours, mine and (not) ours: Social influences on group information repositories. *CHI 2009*, 2095–2098.
- Raskin, J. (2000). *The Humane Interface*. Addison-Wesley.
- Ringel, M., Cutrell, E., Dumais, S., & Horvitz, E. (2003). Milestones in time: The value of landmarks in retrieving information from personal stores. *INTERACT 2003*.
- Rodden, K., & Leggett, M. (2010). Best of both worlds: Improving Gmail labels with the affordances of folders. *CHI 2010 Extended Abstracts*, 4587–4596.
- Rosch, E. (1978). Principles of categorization. In *Cognition and Categorization*.
- Russell, D. M., & Lawrence, S. (2007). Search everything. In *Personal Information Management*.
- Sellen, A. J., & Whittaker, S. (2010). Beyond total capture: A constructive critique of lifelogging. *Communications of the ACM*, 53(5), 70–77.
- Shneiderman, B., & Plaisant, C. (2010). *Designing the User Interface* (5th ed.). Addison-Wesley.
- Tang, J. C., et al. (2008). [Studi visibilitas inbox; dirujuk dalam Bab 3.]
- Tauscher, L., & Greenberg, S. (1997). How people revisit web pages: Empirical findings and implications for the design of history systems. *International Journal of Human–Computer Studies*, 47(1), 97–137.
- Teevan, J., Alvarado, C., Ackerman, M. S., & Karger, D. R. (2004). The perfect search engine is not enough: A study of orienteering behavior in directed search. *CHI 2004*, 415–422.
- Treisman, A. M. (1969). Strategies and models of selective attention. *Psychological Review*, 76(3), 282–299.
- Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136.
- Tulving, E., & Thomson, D. M. (1973). Encoding specificity and retrieval processes in episodic memory. *Psychological Review*, 80(5), 352–373.
- Voida, S., Olson, J. S., & Olson, G. M. (2013). Turbulence in the clouds: Challenges of cloud-based information work. *CHI 2013*.
- Wagenaar, W. A. (1986). My memory: A study of autobiographical memory over six years. *Cognitive Psychology*, 18(2), 225–252.
- Wen, J. (2003). Post-valued recall web pages: User disorientation hits the big time. *IT & Society*, 1(3), 184–194.
- Whittaker, S. (1996). Talking to strangers: An evaluation of the factors affecting electronic collaboration. *CSCW 1996*.
- Whittaker, S. (2005). Supporting collaborative task management in email. *Human–Computer Interaction*, 20(1–2), 49–88.
- Whittaker, S., Bellotti, V., & Gwizdka, J. (2007). Email and PIM: Problems and possibilities. In *Personal Information Management*.
- Whittaker, S., Bergman, O., & Clough, P. (2010). Easy on that trigger dad: A study of long-term family photo retrieval. *Personal and Ubiquitous Computing*, 14(1), 31–43.
- Whittaker, S., & Hirschberg, J. (2001). The character, value, and management of personal paper archives. *ACM Transactions on Computer–Human Interaction*, 8(2), 150–170.
- Whittaker, S., Jones, Q., & Terveen, L. (2002). Contact management: Identifying contacts to support long-term communication. *CSCW 2002*.
- Whittaker, S., Matthews, T., Cerruti, J., Badenes, H., & Tang, J. (2011). Am I wasting my time organizing email? A study of email refinding. *CHI 2011*, 3449–3458.
- Whittaker, S., & Sidner, C. (1996). Email overload: Exploring personal information management of email. *CHI 1996*, 276–283.
- Whittaker, S., et al. (2004). ContactMap: Organizing communication in a social desktop. *ACM Transactions on Computer–Human Interaction*, 11(4), 445–471.

---

> **Pernyataan kepatuhan dan keaslian.** Buku ajar ini merupakan penyajian ulang dan elaborasi pedagogis dalam Bahasa Indonesia atas isi buku *The Science of Managing Our Digital Stuff* (Bergman & Whittaker, 2016, The MIT Press). Seluruh angka, persentase, dan temuan penelitian bersumber dari teks buku tersebut. Bagian elaborasi pedagogis (analogi, studi kasus Indonesia, latihan, dan implikasi praktis) telah ditandai sebagai tambahan didaktis dan bukan klaim langsung para penulis asli. Rincian rujukan pada Daftar Pustaka diselaraskan dengan bagian References buku sumber; bila suatu detail penerbitan tidak tampak penuh dalam ekstraksi teks, entri ditandai seperlunya. Konten teks sumber telah diparafrasa untuk mematuhi pembatasan lisensi (*content was rephrased for compliance with licensing restrictions*).

---

# Lampiran A — Rencana Pembelajaran Semester (RPS)

Lampiran ini menyajikan usulan RPS satu semester (14 pertemuan tatap muka + UTS + UAS) untuk mata kuliah berbasis buku ajar ini. RPS ini bersifat **elaborasi pedagogis** dan dapat disesuaikan dengan kalender akademik masing-masing program studi.

**Identitas Mata Kuliah (usulan)**
- Nama: Manajemen Informasi Pribadi / Personal Information Management
- Bobot: 3 SKS
- Prasyarat: Pengantar Interaksi Manusia–Komputer atau Sistem Informasi Dasar
- Capaian Pembelajaran Mata Kuliah (CPMK): Mahasiswa mampu menganalisis perilaku kurasi informasi pribadi, mengevaluasi metode pengambilan informasi, dan merancang fitur sistem PIM berbasis pendekatan user-subjective.

| Pertemuan | Topik | Bab Rujukan | Bentuk Kegiatan | Asesmen |
|---|---|---|---|---|
| 1 | Pengantar PIM; kontrak kuliah; konsep kurasi | Pendahuluan | Ceramah + diskusi | Inventarisasi koleksi pribadi (Tugas 1) |
| 2 | Arsip pribadi & daur hidup kurasi; properti informasi | Bab 1 | Ceramah + klasifikasi Tabel 1.1 | Latihan Bab 1 |
| 3 | Keeping: kertas, surel | Bab 2 (2.1–2.4) | Studi kasus + diskusi | Catatan rasio hapus (Tugas Bab 2) |
| 4 | Keeping: kontak, web, foto; overkeeping & deferral | Bab 2 (2.5–2.8) | Analisis temuan | Kuis 1 |
| 5 | Management: cueing semantik & temporal; filing vs piling | Bab 3 (3.1–3.4) | Ceramah + debat filer/piler | Latihan Bab 3 |
| 6 | Management: berkas, surel, web, foto; kepribadian | Bab 3 (3.5–3.9) | Pemetaan sistem surel | Tugas pemetaan |
| 7 | Exploitation: EPIR; navigasi berkas; heuristik 21 item | Bab 4 (4.1–4.4) | Latihan hitung heuristik | Latihan Bab 4 |
| — | **Ujian Tengah Semester (UTS)** | Bab 1–4 | Ujian tertulis | UTS (lihat Lampiran C) |
| 8 | Exploitation: foto & web; pengantar Bagian II | Bab 4 (4.5–4.6) + Pengantar II | Diskusi | — |
| 9 | Alternatif Search: search everything; studi Bergman 2008 | Bab 5 | Analisis desain studi | Kuis 2 |
| 10 | Alternatif Tagging: tag everything; folder vs tag | Bab 6 | Eksperimen tagging mini | Tugas tagging |
| 11 | Alternatif GIM: PIM vs GIM; empat alasan | Bab 7 | Eksperimen folder bersama | Latihan Bab 7 |
| 12 | Mengapa navigasi disukai: dual-task & fMRI | Bab 8 | Eksperimen dual-task mini | Latihan Bab 8 |
| 13 | Pendekatan User-Subjective; prinsip importance | Bab 9–10 | Studi desain GrayArea/Old'nGray | Tugas desain |
| 14 | Prinsip project & context; sintesis & implikasi | Bab 11–12 + Penutup | Presentasi proyek akhir | Proyek (Lampiran E) |
| — | **Ujian Akhir Semester (UAS)** | Bab 5–12 | Ujian tertulis | UAS (lihat Lampiran C) |

**Bobot Penilaian (usulan):** Kehadiran & partisipasi 10%; Kuis 10%; Tugas & Latihan 20%; UTS 25%; Proyek Akhir 15%; UAS 20%.

---

# Lampiran B — Tabel Induk Temuan Kuantitatif Lintas-Bab

Lampiran ini mengonsolidasikan angka-angka kunci dari buku sumber sebagai rujukan cepat. **Semua angka berasal dari teks buku Bergman & Whittaker (2016)**; gunakan bersama bab terkait untuk konteks penuh.

### B.1 Skala Arsip Pribadi (Bab 1)

| Metrik | Angka | Bab |
|---|---|---|
| Surel disimpan (rangkuman 8 studi) | ~2.846 | 1 |
| Surel disimpan (studi 345 pengguna) | ~2.568 | 1 |
| Berkas pribadi di hard drive | ~2.200 | 1 |
| Foto digital pribadi | >4.000 (4.475) | 1 |
| Arsip kertas | 62 kg (≈ tumpukan 30 m) | 1 |
| Folder surel | 244 / 46,89 | 1 |
| Folder berkas (kedalaman) | 57 (3,3) | 1 |
| Folder bookmark | 17 | 1 |
| Waktu memfail surel | 10% total waktu | 1 |
| Akses web yang berupa akses-ulang | 58%–81% | 1 |

### B.2 Keeping (Bab 2)

| Metrik | Angka |
|---|---|
| Laju akuisisi harian | 5 berkas; 1 bookmark/5 hari; 1 kontak; ~5 foto; ~24 surel (dari 44) |
| Keputusan keeping surel seumur hidup digital | >350.000 |
| Kertas dibuang (office move) | 22% |
| Data dibuang yang tak pernah dibaca | 23% |
| Tak bersih-bersih >1 tahun | 74% |
| Pembersihan dipicu peristiwa ekstrinsik | 84% |
| Arsip kertas unik / salinan publik | 49% / 36% |
| Surel disimpan | ~70% |
| Pesan informatif (proporsi kiriman) | 34% |
| Actionable dibalas segera | 65% |
| Actionable tetap disimpan | 85% |
| Actionable ditunda | 37% |
| Threading | 30%–62% |
| Actionable dihapus / Informatif dihapus | 0,5% / 30% |
| Kontak rata-rata / dinilai penting | 858 / 14% (118) |
| Bookmark tak pernah dipakai | 58% |
| Informasi web berhasil ditemukan kembali (Wen) | ~20% |
| Foto dihapus | ~17% |

### B.3 Management (Bab 3)

| Metrik | Angka |
|---|---|
| Penyimpanan aktif seumur hidup digital | ~100.000 dokumen; 440.000 surel; 120.000 foto |
| Folder berkas/surel baru | tiap 3 hari / 5 hari |
| Bookmark tak pernah diakses | 42% |
| Ambang filer (office move) | 40% |
| Berkas di folder default | 12% |
| Frequent filers / folder to-do ditinggalkan | 25% / 95% |
| Spring cleaning | 35% |
| Failed folders (1–2 item) | 35% (kemudian 16%) |
| Folder surel rata-rata | ~39 |
| Inbox terlihat sekaligus | 25% |
| Bookmark: pemakai / rata-rata tautan | 92% / 220 |
| Ambang munculnya folder bookmark | ~35 |

### B.4 Exploitation (Bab 4)

| Metrik | Angka |
|---|---|
| Studi navigasi berkas | 296 peserta; 1.131 berkas; 5.035 langkah |
| Keberhasilan / waktu navigasi | 94% / 14,76 detik |
| Kedalaman / item per folder / subfolder | 2,86 / 11,82 / 10,64 |
| Tambahan waktu per langkah folder / per item | 2,236 dtk / 0,106 dtk |
| Heuristik maksimal item per folder | ~21 (2,236/0,106 = 21,09) |
| Refinding surel | 345 pengguna; >85.000 aksi |
| Surel: scroll / search / folder / sort | 62% / 18% / 13% / 6% |
| Memori surel: konten / temporal | >80% / ~50% |
| SIS: pencarian pada surel / sertakan pengirim | 74% / 25% |
| Foto lama: keberhasilan / memberi label | 61% / 67% |
| Web revisit (Tauscher; Cockburn; Obendorf terkontrol) | 58% / 81% / 41% |

### B.5 Bagian II–III (Bab 5–12)

| Metrik | Angka | Bab |
|---|---|---|
| Navigasi vs search | 56–68% vs 7–15% | 5 |
| Windows: search 3 minggu → 7 bulan | 7%→15%→10% | 5 |
| Lokasi berkas diingat / batas atas search | 74–90% / ~25% | 5 |
| Sikap pro-tag (multiple/masa depan/kebiasaan) | 77% / 72% / 61% | 6 |
| Gmail: folder-label vs tag-label | 67% vs 33% | 6 |
| Gmail: single vs multiple label | 92% vs 8% | 6 |
| Windows 7: berkas di folder spesifik / pakai tag | 96% / 16% | 6 |
| GIM vs PIM gagal | 22% vs 13% | 7 |
| Folder orang lain / sendiri / default gagal | 28% / 5% / 17% | 7 |
| Berbagi via surel (kirim/terima) | 86% / 65% | 7 |
| Dual-task / fMRI peserta | 62 / 17 | 8 |
| Search lebih lama daripada navigasi | ~3x | 8 |
| Kapasitas memori kerja (Miller) | 7±2 | 8 |
| Kwasnik: atribut dokumen / subjektif | 30% / 70% | 9 |
| Work-around demosi (salah satu) | 79% | 10 |
| GrayArea: clutter turun / mudah didemosi | 13% / 81% | 10 |
| DMTR: kontak tak dipakai >6 bln | 47% | 10 |
| Old'nGray: kegagalan / waktu | 24%→4% / 17,68→6,56 dtk | 10 |
| Guided tour: ucapan rujuk konteks | separuh (50%) | 12 |

---

# Lampiran C — Bank Soal Ujian (UTS & UAS)

Lampiran ini menyediakan contoh soal untuk evaluasi. Dosen dapat memilih, memodifikasi, atau menambah bobot sesuai kebutuhan.

### C.1 Ujian Tengah Semester (Bab 1–4)

**Bagian I — Pilihan/Isian Singkat (skor 30)**
1. Definisikan PIM dan sebutkan tiga proses kurasi.
2. Lengkapi: rata-rata orang menyimpan ~____ surel dan ~____ berkas (sebutkan studinya).
3. Apa beda butir actionable dan informative?
4. Sebutkan dua penyebab utama overkeeping.
5. Apa kepanjangan dan inti metode EPIR?
6. Tuliskan heuristik jumlah item per folder dan asal angkanya.

**Bagian II — Esai Analisis (skor 40)**
7. Jelaskan metafora "kurasi sebagai komunikasi terarah-diri" dan kaitkan dengan mengapa PIM berbeda dari manajemen informasi publik. (15)
8. Studi office-move menemukan orang hanya membuang 22% arsip. Jelaskan mekanisme psikologis (loss aversion) dan organisasional (information overload + deferred evaluation) di balik temuan ini. (15)
9. Mengapa high filers dalam studi refinding surel tidak lebih sukses daripada low filers? Apa implikasinya bagi praktik memfail? (10)

**Bagian III — Studi Kasus Terapan (skor 30)**
10. Seorang staf memiliki folder `Proyek` berisi 180 berkas. Hitung perkiraan keuntungan waktu bila ia memecahnya menjadi subfolder ≤21 item, lalu uraikan trade-off depth-vs-size. Sertakan asumsi Anda.

### C.2 Ujian Akhir Semester (Bab 5–12)

**Bagian I — Isian Singkat (skor 30)**
1. Sebutkan persentase navigasi vs search menurut Bergman et al. (2008).
2. Apa "batas atas" penggunaan search dan apa artinya?
3. Bedakan tag-label dan folder-label di Gmail.
4. Sebutkan empat alasan PIM lebih efektif daripada GIM.
5. Area otak mana yang aktif saat navigasi dan saat search (studi fMRI)?
6. Sebutkan tiga prinsip user-subjective.

**Bagian II — Esai Analisis (skor 40)**
7. Jelaskan mengapa search dan tag berhasil di web/Web 2.0 tetapi gagal di PIM. Gunakan konsep familiaritas dan massa kritis. (15)
8. Integrasikan temuan studi dual-task dan fMRI untuk menjelaskan preferensi navigasi. Mengapa preferensi ini diperkirakan permanen? (15)
9. Jelaskan prinsip demosi dan bagaimana ia mengatasi hambatan Prospect Theory; sebutkan satu implementasinya beserta hasil evaluasi. (10)

**Bagian III — Desain (skor 30)**
10. Rancang satu fitur sistem PIM yang mengimplementasikan salah satu prinsip user-subjective (selain GrayArea, DMTR, Old'nGray, ProjectFolders, ChittyChatty, ItemHistory, ContactMap, PiccyChatty, Starlight). Jelaskan: prinsip yang dipakai, atribut subjektif yang ditangkap, cara kerja, dan rancangan evaluasinya (metode, peserta, ukuran keberhasilan).

---

# Lampiran D — Rubrik Penilaian Tugas Praktik

Rubrik analitik berikut dapat dipakai untuk menilai tugas praktik di akhir tiap bab maupun proyek akhir.

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|---|---|---|---|---|
| **Ketepatan konsep** | Konsep PIM dipakai tepat & mendalam; terhubung ke temuan sumber | Konsep tepat dengan sedikit kelemahan | Konsep dasar benar tetapi dangkal | Banyak miskonsepsi |
| **Penggunaan data/temuan** | Mengutip angka/temuan relevan dengan akurat | Mengutip sebagian temuan | Sedikit rujukan temuan | Tanpa rujukan temuan |
| **Analisis & refleksi** | Analisis kritis, membandingkan pengalaman dengan riset | Analisis memadai | Deskriptif, minim analisis | Tidak ada refleksi |
| **Penerapan/empirisme** | Eksperimen/pengukuran mandiri dilakukan rapi & dilaporkan | Pengukuran dilakukan sebagian | Pengukuran minim | Tidak ada pengukuran |
| **Komunikasi** | Sistematis, jelas, bahasa akademik | Jelas dengan sedikit kekurangan | Kurang sistematis | Sulit dipahami |

**Konversi skor:** Total maksimal 20. Nilai akhir = (total/20) × 100. Kategori: A (85–100), AB (75–84), B (65–74), BC (55–64), C (45–54), D/E (<45).

---

# Lampiran E — Proyek Akhir Semester: Studi Mini Kurasi Pribadi

**Tujuan.** Mengintegrasikan seluruh materi melalui studi empiris berskala kecil terhadap perilaku PIM diri sendiri atau partisipan sukarela, lalu mengusulkan perbaikan desain berbasis pendekatan user-subjective.

**Format.** Laporan 8–12 halaman + presentasi 10 menit. Boleh individu atau kelompok 2–3 orang.

**Struktur laporan yang disarankan:**

1. **Pendahuluan.** Latar belakang masalah PIM yang Anda amati (mis. kesulitan menemukan berkas, inbox menumpuk, foto lama hilang). Kaitkan dengan minimal dua bab buku ajar.
2. **Metode.** Pilih satu pendekatan terinspirasi sumber:
   - *Replikasi mini EPIR*: minta 3–5 partisipan mengambil berkas dari sistem mereka sendiri; ukur waktu dan keberhasilan (bandingkan dengan 94% / 14,76 detik).
   - *Profil struktur*: hitung jumlah folder, kedalaman, item per folder; bandingkan dengan 57 folder / kedalaman 3,3 / ≤21 item.
   - *Studi keeping/deletion*: catat rasio hapus selama seminggu; bandingkan dengan angka sumber (foto 17%, surel 30%).
3. **Hasil.** Sajikan data dalam tabel/grafik. Bandingkan temuan Anda dengan angka buku sumber pada Lampiran B.
4. **Analisis.** Terapkan kerangka teoretis: Prospect Theory (overkeeping), atensi verbal (preferensi navigasi), atribut subjektif (organisasi). Tandai mana yang sesuai dan mana yang menyimpang dari temuan sumber, serta kemungkinan sebabnya.
5. **Usulan Desain.** Ajukan satu fitur berbasis salah satu prinsip user-subjective (importance/project/context) yang menjawab masalah Anda. Jelaskan atribut subjektif yang ditangkap dan rancangan evaluasinya.
6. **Refleksi & Keterbatasan.** Diskusikan perbedaan individu (Bab 3) dan keterbatasan validitas studi mini Anda.

**Kriteria penilaian:** Gunakan rubrik Lampiran D, dengan penekanan tambahan pada **orisinalitas usulan desain** dan **kejujuran metodologis** (melaporkan keterbatasan).

> **Catatan etika & privasi.** Bila melibatkan partisipan lain, mintalah persetujuan, jangan membuka isi berkas pribadi mereka (ikuti praktik EPIR: cukup klik tanpa membuka), dan anonimkan data. Hormati privasi sebagaimana ditekankan buku sumber dalam pembahasan logfile dan EPIR.

---

*Akhir buku ajar.*
