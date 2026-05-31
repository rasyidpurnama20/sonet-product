# Proteksi Data Modern: Menjamin Keterpulihan Seluruh Beban Kerja Modern

## Buku Ajar untuk Mahasiswa Sistem Informasi/Teknik Informatika, Administrator Sistem, dan Praktisi TI

---

### Metadata dan Informasi Bibliografis

> **Buku Sumber (Sumber Tunggal):**
> Preston, W. Curtis. (2021). *Modern Data Protection: Ensuring Recoverability of All Modern Workloads*. Sebastopol, CA: O'Reilly Media, Inc. Edisi Pertama, Mei 2021. ISBN: 978-1-492-09405-0.

| Aspek | Keterangan |
|---|---|
| **Judul Buku Ajar** | Proteksi Data Modern: Menjamin Keterpulihan Seluruh Beban Kerja Modern |
| **Buku Rujukan Utama** | *Modern Data Protection* karya W. Curtis Preston |
| **Penulis Sumber** | W. Curtis Preston (dikenal sebagai "Mr. Backup") |
| **Penerbit Sumber** | O'Reilly Media, Inc. |
| **Tahun** | 2021 |
| **Cakupan** | Backup, recovery, archive, disaster recovery, dan proteksi data untuk beban kerja tradisional maupun modern (VM, cloud, kontainer/Kubernetes, basis data, SaaS, IoT) |
| **Bahasa Pengantar** | Bahasa Indonesia akademik (istilah teknis dipertahankan dalam bahasa Inggris disertai penjelasan) |
| **Jenis Dokumen** | Buku ajar (*buku ajar*) terstruktur secara pedagogis |

> **Catatan tentang Atribusi:** Buku ajar ini disusun secara setia berdasarkan isi buku sumber. Pendapat, rekomendasi, dan opini yang merupakan sikap pribadi penulis sumber diatribusikan secara eksplisit dengan frasa seperti "menurut Preston" atau "menurut penulis sumber". Tidak ada klaim vendor, angka, atau spesifikasi yang dikarang; seluruh contoh dan data teknis bersumber dari naskah asli. Beberapa contoh diadaptasi ke konteks Indonesia untuk keperluan pedagogis dengan tetap mempertahankan substansi argumen penulis. Catatan ini ditambahkan untuk kepatuhan terhadap pembatasan lisensi konten.

---

## Kata Pengantar

### Tujuan Buku Ajar

Buku ajar ini bertujuan menyajikan kembali pengetahuan komprehensif tentang **proteksi data modern** (*modern data protection*) yang terkandung dalam karya W. Curtis Preston, dalam bentuk yang terstruktur secara pedagogis dan menggunakan Bahasa Indonesia akademik. Proteksi data — yang mencakup *backup* (pencadangan), *recovery* (pemulihan), *archive* (pengarsipan), dan *disaster recovery* (pemulihan bencana) — adalah salah satu fungsi paling fundamental sekaligus paling sering diremehkan dalam dunia teknologi informasi. Sebagaimana ditegaskan berulang kali oleh penulis sumber: *"Tidak ada yang peduli apakah Anda bisa mem-backup. Mereka hanya peduli apakah Anda bisa melakukan restore."*

Buku ini menyiapkan pembaca untuk memahami:

1. **Mengapa** proteksi data diperlukan (lanskap ancaman: kesalahan manusia, kegagalan mekanis, bencana alam, dan ransomware).
2. **Apa** yang perlu dilindungi (server fisik dan virtual, laptop, basis data, cloud, kontainer, SaaS, IoT).
3. **Bagaimana** melindunginya (berbagai metode perangkat lunak, perangkat keras target, dan layanan).
4. **Dengan apa** mengukur keberhasilan (metrik RTO, RPO, RTA, RPA, dan kepatuhan terhadap aturan 3-2-1).

### Untuk Siapa Buku Ini

Buku ajar ini ditujukan untuk:

- **Mahasiswa program studi Sistem Informasi (SI) dan Teknik Informatika (TI)** yang mempelajari infrastruktur TI, administrasi sistem, manajemen data, dan keamanan informasi.
- **Administrator sistem (sysadmin), administrator basis data (DBA), dan insinyur infrastruktur** yang bertanggung jawab atas keberlangsungan operasi data organisasi.
- **Praktisi TI dan pengambil keputusan** (arsitek solusi, manajer TI) yang perlu merancang, mengevaluasi, atau mengganti sistem proteksi data.

### Prasyarat

Untuk memperoleh manfaat maksimal, pembaca sebaiknya telah memiliki pemahaman dasar tentang:

- Konsep sistem operasi (Windows, Linux/Unix), berkas (*file*), dan sistem berkas (*filesystem*).
- Konsep jaringan komputer dasar (LAN, WAN, bandwidth).
- Konsep penyimpanan (*storage*): disk, RAID, dan konsep dasar basis data.
- Pengenalan virtualisasi (*virtual machine*) dan komputasi awan (*cloud computing*).

Pembaca tanpa latar belakang ini tetap dapat mengikuti karena setiap istilah teknis didefinisikan saat pertama kali muncul.

### Cara Menggunakan Buku Ini

Buku ini disusun secara berurutan dan **kumulatif**: konsep pada bab-bab awal (terutama aturan 3-2-1, perbedaan backup vs archive, serta RTO/RPO) menjadi fondasi bagi seluruh bab berikutnya. Disarankan membaca secara berurutan, terutama bagi pembaca pemula.

Setiap bab inti memuat komponen pedagogis yang konsisten:

- **Tujuan Pembelajaran** — sasaran kompetensi mengacu pada Taksonomi Bloom.
- **Peta Konsep** — gambaran ringkas keterkaitan konsep dalam bab.
- **Materi Inti** — uraian mendalam dengan definisi, tabel perbandingan, dan diagram-teks.
- **Istilah Kunci** — daftar istilah bahasa Inggris beserta penjelasan Indonesia.
- **Studi Kasus/Contoh** — skenario nyata, sebagian diadaptasi ke konteks Indonesia.
- **Praktik Baik & Kesalahan Umum** — panduan operasional praktis.
- **Rangkuman** — inti sari bab.
- **Latihan & Refleksi** — soal pemahaman, analisis tingkat tinggi (HOTS), dan tugas perancangan.

> **Prinsip Pemandu (dari penulis sumber):** *Aturan 3-2-1 adalah hukum fundamental yang menjadi dasar seluruh backup — bagi desain backup, aturan ini seperti E = mc² bagi fisika. Bila desain Anda tidak mematuhinya, ada sesuatu yang salah secara fatal.*

---

## Daftar Isi

- [Kata Pengantar](#kata-pengantar)
- [Bab Pendahuluan: Mengapa Proteksi Data Penting](#bab-pendahuluan-mengapa-proteksi-data-penting)

### BAGIAN I — Fondasi Konseptual Proteksi Data
- [Pengantar Bagian I](#pengantar-bagian-i)
- [Bab 1 — Risiko terhadap Data: Mengapa Kita Mem-Backup](#bab-1--risiko-terhadap-data-mengapa-kita-mem-backup)
- [Bab 2 — Mengumpulkan dan Menentukan Tingkat Layanan](#bab-2--mengumpulkan-dan-menentukan-tingkat-layanan)
- [Bab 3 — Backup dan Archive Sangat Berbeda](#bab-3--backup-dan-archive-sangat-berbeda)
- [Bab 4 — Dasar-Dasar Backup dan Recovery](#bab-4--dasar-dasar-backup-dan-recovery)

### BAGIAN II — Teknologi Penyimpanan dan Sumber Data
- [Pengantar Bagian II](#pengantar-bagian-ii)
- [Bab 5 — Menggunakan Disk dan Deduplikasi untuk Proteksi Data](#bab-5--menggunakan-disk-dan-deduplikasi-untuk-proteksi-data)
- [Bab 6 — Sumber Data Tradisional](#bab-6--sumber-data-tradisional)
- [Bab 7 — Melindungi Basis Data](#bab-7--melindungi-basis-data)
- [Bab 8 — Sumber Data Modern](#bab-8--sumber-data-modern)

### BAGIAN III — Metode Perangkat Lunak dan Pemulihan Bencana
- [Pengantar Bagian III](#pengantar-bagian-iii)
- [Bab 9 — Metode Perangkat Lunak Backup dan Recovery](#bab-9--metode-perangkat-lunak-backup-dan-recovery)
- [Bab 10 — Metode Perangkat Lunak Archive](#bab-10--metode-perangkat-lunak-archive)
- [Bab 11 — Metode Disaster Recovery](#bab-11--metode-disaster-recovery)

### BAGIAN IV — Target Penyimpanan dan Solusi Komersial
- [Pengantar Bagian IV](#pengantar-bagian-iv)
- [Bab 12 — Target Proteksi Data](#bab-12--target-proteksi-data)
- [Bab 13 — Tantangan Proteksi Data Komersial](#bab-13--tantangan-proteksi-data-komersial)
- [Bab 14 — Solusi Proteksi Data Tradisional](#bab-14--solusi-proteksi-data-tradisional)
- [Bab 15 — Solusi Proteksi Data Modern](#bab-15--solusi-proteksi-data-modern)
- [Bab 16 — Mengganti atau Meng-upgrade Sistem Backup Anda](#bab-16--mengganti-atau-meng-upgrade-sistem-backup-anda)

### Penutup dan Lampiran
- [Bab Penutup: Sintesis dan Merancang Strategi Proteksi Data Menyeluruh](#bab-penutup-sintesis-dan-merancang-strategi-proteksi-data-menyeluruh)
- [Glosarium (EN → ID)](#glosarium-en--id)
- [Daftar Pustaka](#daftar-pustaka)

---

## Bab Pendahuluan: Mengapa Proteksi Data Penting

### Hakikat Proteksi Data

Setiap organisasi modern — baik perusahaan swasta, lembaga pemerintah, organisasi nirlaba, maupun institusi pendidikan — menjalankan operasinya di atas **data**. Data adalah aset yang, jika hilang, dapat melumpuhkan organisasi, menimbulkan kerugian finansial besar, merusak reputasi, hingga menyebabkan tuntutan hukum. Oleh karena itu, kemampuan untuk **memulihkan** data setelah suatu insiden bukanlah kemewahan, melainkan kebutuhan dasar.

Penulis sumber, W. Curtis Preston, membuka bukunya dengan satu kalimat yang menjadi mantra seluruh disiplin ini:

> *"No one cares if you can backup. Only if you can restore."*
> — Mr. Backup
>
> (Tidak ada yang peduli apakah Anda bisa mem-*backup*; mereka hanya peduli apakah Anda bisa melakukan *restore*.)

Pesan ini menggeser fokus dari sekadar "membuat salinan" ke tujuan sesungguhnya: **keterpulihan (*recoverability*)**. Sebuah backup yang tidak pernah diuji pemulihannya bukanlah backup yang dapat diandalkan.

### Tiga Istilah Inti yang Wajib Dipahami Sejak Awal

Sebelum mendalami bab-bab teknis, tiga konsep berikut perlu dipahami terlebih dahulu karena akan muncul di hampir setiap bab.

#### 1. Aturan 3-2-1 (The 3-2-1 Rule)

> **Definisi:** Simpan **3** versi data Anda, pada **2** media yang berbeda, dengan **1** salinan disimpan di tempat lain (di luar lokasi utama).

Menurut Preston, aturan ini adalah fondasi yang menentukan apakah sesuatu layak disebut "backup" atau hanya "salinan (*copy*)". Tiga versi memberi perlindungan terhadap rangkaian kesalahan (misalnya berkas rusak yang ikut ter-backup). Dua media mencegah kegagalan satu jenis media menghapus semua salinan sekaligus. Satu salinan di tempat lain melindungi terhadap bencana yang dapat menghancurkan seluruh lokasi. Aturan ini akan dibahas mendalam pada Bab 3.

#### 2. RTO — Recovery Time Objective (Sasaran Waktu Pemulihan)

> **Definisi:** Seberapa cepat Anda perlu memulihkan operasi setelah suatu bencana — yaitu durasi *downtime* yang dapat ditoleransi yang telah disepakati semua pihak.

#### 3. RPO — Recovery Point Objective (Sasaran Titik Pemulihan)

> **Definisi:** Seberapa banyak data yang dapat Anda relakan hilang setelah suatu insiden besar, diukur dalam satuan waktu (misalnya, RPO satu jam berarti Anda menyetujui kehilangan hingga satu jam data).

RTO dan RPO adalah dua metrik yang **mengendalikan seluruh desain** sistem proteksi data dan akan dibahas mendalam pada Bab 2 dan Bab 4.

```
Diagram-Teks: Garis Waktu Insiden, RPO, dan RTO

        RPO                         RTO
  |<--------->|                |<----------------->|
  |           |                |                   |
[Backup     [INSIDEN          [Mulai             [Operasi
 terakhir]   terjadi]          pemulihan]          normal kembali]
  |           |                                    |
  +-- Data yang hilang --+    +--- Waktu henti (downtime) ---+
      (selisih = RPO)               (selisih = RTO)
```

RPO mengukur jarak waktu antara backup terakhir yang valid dan saat insiden — inilah data yang berpotensi hilang. RTO mengukur jarak waktu antara saat insiden dan saat operasi pulih sepenuhnya. Penting dicatat (sebagaimana ditegaskan Preston): jam RTO mulai berdetak saat insiden terjadi dan baru berhenti saat aplikasi benar-benar daring kembali dan bisnis kembali normal — bukan sekadar saat penyalinan data selesai.

### Lanskap Ancaman: Mengapa Pemulihan Dibutuhkan

Buku sumber menyusun ancaman terhadap data berdasarkan urutan kemungkinan terjadinya, dari yang paling sering ke yang paling jarang:

1. **Bencana akibat manusia (*human disasters*)** — kecelakaan/kesalahan (*PEBKAC*, "*problem exists between keyboard and chair*"), kode yang buruk (*bad code*), serangan jahat, dan ancaman dari dalam (*rogue admin*).
2. **Ransomware** — kini menjadi alasan nomor satu organisasi terpaksa menjalankan rencana pemulihan bencananya.
3. **Kegagalan mekanis atau sistem** — gangguan listrik, kegagalan perangkat keras (meski makin jarang berkat RAID dan media solid-state).
4. **Bencana alam** — banjir, kebakaran, gempa bumi, badai, tornado, dan *sinkhole*.

Setiap kategori ancaman ini akan dibahas pada Bab 1. Yang terpenting untuk dipahami sejak awal: ketahanan perangkat keras (seperti RAID dan replikasi) **tidak** menggantikan kebutuhan backup, karena ketahanan hanya melindungi terhadap kegagalan perangkat — bukan terhadap kesalahan manusia, serangan, atau kerusakan data itu sendiri.

### Ransomware: Faktor Pengubah Permainan

Salah satu benang merah buku sumber adalah betapa **ransomware** telah mengubah lanskap proteksi data. Ransomware adalah perangkat lunak jahat (*malware*) yang secara diam-diam mengenkripsi data korban, lalu menawarkan kunci dekripsi dengan imbalan tebusan (*ransom*). Dengan munculnya **ransomware-as-a-service (RaaS)** — layanan kriminal yang memudahkan siapa pun melancarkan serangan — risiko ini meningkat setiap hari. Satu-satunya jawaban yang sahih terhadap ransomware, menurut Preston, adalah sistem disaster recovery dengan RTO yang cukup pendek sehingga organisasi dapat mengabaikan tuntutan tebusan dan memulihkan diri sendiri. Konsep ini dibahas mendalam pada Bab 11.

### Struktur Buku Ajar

Buku ajar ini membagi keenam belas bab buku sumber ke dalam empat **Bagian** tematik:

- **Bagian I (Bab 1–4):** Fondasi konseptual — risiko, tingkat layanan, perbedaan backup/archive, serta dasar backup dan recovery.
- **Bagian II (Bab 5–8):** Teknologi penyimpanan dan sumber data — disk dan deduplikasi, sumber data tradisional, basis data, serta sumber data modern.
- **Bagian III (Bab 9–11):** Metode perangkat lunak dan pemulihan bencana.
- **Bagian IV (Bab 12–16):** Target penyimpanan, tantangan komersial, serta solusi tradisional dan modern, ditutup dengan panduan mengganti/meng-upgrade sistem.

Mari kita mulai dengan memahami mengapa, pada hakikatnya, kita perlu mem-backup data.

---


## BAGIAN I — Fondasi Konseptual Proteksi Data

### Pengantar Bagian I

Bagian I meletakkan fondasi konseptual yang menopang seluruh isi buku. Tanpa pemahaman atas konsep-konsep di sini, pembahasan teknologi dan solusi pada bagian selanjutnya akan kehilangan konteks.

Bagian ini terdiri atas empat bab:

- **Bab 1** menjawab pertanyaan *mengapa* kita mem-backup, dengan menelaah seluruh kategori risiko terhadap data: dari kesalahan manusia, kode yang buruk, serangan jahat dan ransomware, ancaman internal, kegagalan mekanis, hingga bencana alam.
- **Bab 2** menjelaskan bagaimana mengumpulkan kebutuhan organisasi dan menetapkan **tingkat layanan (*service levels*)** — termasuk definisi awal RTO dan RPO — serta proses tata kelola untuk merancang sistem proteksi data.
- **Bab 3** menggariskan perbedaan mendasar antara **backup** dan **archive** — sebuah pembedaan yang, menurut Preston, termasuk tiga hal terpenting yang terus-menerus perlu ia jelaskan. Di sinilah aturan 3-2-1, enkripsi, *air gap*, dan *immutability* dibahas tuntas.
- **Bab 4** menyelami dasar-dasar teknis backup dan recovery: pengujian pemulihan, level backup (*full*, *incremental*, *differential*), metrik kapasitas dan pemulihan, serta mitos-mitos yang umum beredar.

> **Prinsip Pemandu Bagian I:** Proteksi data dimulai bukan dari teknologi, melainkan dari pemahaman atas *risiko* yang dihadapi dan *kebutuhan* organisasi. Teknologi hanyalah cara untuk memenuhi kebutuhan tersebut.

---

## Bab 1 — Risiko terhadap Data: Mengapa Kita Mem-Backup

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mengidentifikasi** (C1) berbagai kategori risiko terhadap data: bencana akibat manusia, kegagalan mekanis/sistem, dan bencana alam.
2. **Menjelaskan** (C2) mekanisme kerja ransomware dan ransomware-as-a-service serta mengapa ia menjadi ancaman utama saat ini.
3. **Membedakan** (C2) ancaman eksternal dan ancaman internal (*rogue admin*) terhadap data.
4. **Menganalisis** (C4) bagaimana praktik pembatasan akses (*least privilege*, *separation of powers*, *multiperson authentication*) menekan risiko ancaman internal.
5. **Menilai** (C5) mengapa ketahanan perangkat keras (RAID, replikasi) tidak menggantikan kebutuhan backup.
6. **Mengaitkan** (C4) setiap kategori risiko dengan urgensi penerapan aturan 3-2-1.

### Peta Konsep

```
RISIKO TERHADAP DATA
│
├── 1. BENCANA AKIBAT MANUSIA (paling sering)
│     ├── Kecelakaan / kesalahan (PEBKAC, fat-finger)
│     ├── Bad code (skrip & perangkat lunak komersial)
│     ├── Serangan jahat (terorisme, serangan elektronik)
│     ├── Ransomware & RaaS
│     └── Ancaman internal (rogue admin, logic bomb)
│           └── Mitigasi: named accounts, least privilege,
│               separation of powers, multiperson authentication
│
├── 2. KEGAGALAN MEKANIS / SISTEM
│     ├── Gangguan listrik
│     ├── "There is no cloud" (hanya komputer orang lain)
│     └── Kegagalan sistem / program
│
└── 3. BENCANA ALAM (lebih mungkin dari kegagalan HW modern)
      ├── Banjir, Kebakaran, Gempa
      └── Badai/Topan/Siklon, Tornado, Sinkhole
            └── Semua bermuara pada: ATURAN 3-2-1
```

### Materi Inti

#### Pembuka: Kisah "Yang Nyaris Lolos"

Penulis sumber membuka bab ini dengan pengakuan jujur tentang kegagalan pribadinya di awal karier. Saat baru dua bulan menjadi penanggung jawab backup, ia kehilangan basis data Oracle bernama *paris* — basis data pembelian (*purchasing*) untuk organisasi bernilai miliaran dolar. Ia tidak menyadari bahwa basis data Oracle harus dimatikan (*shutdown*) sebelum di-backup, sebuah tugas yang sebelumnya dijalankan oleh *cron job* di server lama yang tidak ia ketahui keberadaannya. Ketika disk pada server baru rusak, ia mendapati seluruh log backup penuh kesalahan, dan backup yang tampak baik ternyata sudah ditimpa (*overwritten*) dua hari sebelumnya karena siklus rotasi enam minggu.

Beruntung, seorang administrator sistem berhasil "membangkitkan" disk yang mati dan memulihkan data langsung dari disk; organisasi hanya kehilangan data beberapa hari. Kisah ini menanamkan pelajaran-pelajaran yang menggerakkan seluruh karier penulis dan menjadi pengingat: **apa yang tidak di-backup, tidak bisa di-restore**.

> **Catatan Konteks Indonesia:** Skenario serupa lazim terjadi di organisasi Indonesia — misalnya ketika basis data aplikasi koperasi atau sistem akademik kampus dipindahkan antar-server, dan langkah penghentian basis data sebelum pencadangan terlewat. Akibatnya, salinan yang tampak ada justru tidak dapat dipulihkan saat dibutuhkan.

#### A. Bencana Akibat Manusia

Mayoritas *restore* dan *disaster recovery* hari ini dijalankan akibat manusia melakukan sesuatu — sengaja atau tidak — yang merusak lingkungan komputasi. Karena inilah jenis insiden yang paling umum, sistem backup dan DR harus benar-benar andal dalam memulihkan dari kategori ini.

**Kecelakaan dan Kesalahan (*Accidents*).** Manusia membuat kesalahan: menyalin berkas yang salah, menghapus berkas penting lalu mengosongkan *trash*, atau salah ketik (*fat-finger*). Istilah jenaka untuk ini adalah **PEBKAC** (*Problem Exists Between Keyboard And Chair*). Yang sering dilupakan: bukan hanya *end user* yang melakukan kesalahan, melainkan juga administrator sistem, jaringan, dan basis data — dan kesalahan administrator berdampak jauh lebih besar karena hak akses mereka. Contoh kesalahan administrator yang disebut buku sumber:

- Menghapus tabel yang salah dalam basis data (*drop the wrong table*).
- Memformat drive yang salah, menghapus *filesystem* yang baik.
- Melakukan restore basis data pengembangan ke atas basis data produksi.
- Menulis skrip untuk menghapus direktori *home* yatim (*orphaned*) yang justru menghapus seluruh direktori *home*.
- Menghapus VM yang salah.

> **Studi Kasus dari Sumber — "That's Not What I Meant!":** Seorang penguji QA menjalankan instalasi sebagai *root* yang keliru membuat direktori bernama harfiah `$HOME/foo`. Untuk membersihkannya, ia mengetik `rm -rf $HOME` pada sistem Unix di mana `$HOME` untuk *root* adalah `/`. Akibatnya seluruh sistem terhapus. Tidak ada *golden image* maupun backup untuk server QA tersebut; untungnya sebagian besar data kritis berada di server NFS terpisah.

**Kode yang Buruk (*Bad Code*).** Kerusakan dapat berasal dari skrip *shell* yang terlalu agresif, bug pada perangkat lunak inti yang merusak data secara diam-diam, hingga praktik buruk pengembang internal. Buku sumber mencontohkan tim pengembang yang menyimpan seluruh *code tree* di `/tmp` pada sistem HP-UX di mana `/tmp` berada di RAM — semuanya lenyap saat server di-*reboot*. Perangkat lunak komersial pun tidak kebal: penulis menceritakan fitur "*fast-and-silent*" pada perangkat lunak backup yang, akibat bug, membuat satu konsultan tanpa sengaja menimpa (*relabel*) **seluruh** tape dalam *tape library* pelanggan hanya dengan dua klik. Untungnya pelanggan memiliki salinan luar lokasi (*off-site*) — sebuah penerapan aturan 3-2-1.

**Serangan Jahat (*Malicious Attacks*).** Terbagi atas:

- **Terorisme** — kerusakan fisik yang disengaja (peristiwa 9/11 menjadi contoh: beberapa organisasi lenyap karena *hot site* DR mereka berada di menara kembar yang lain). Ini menegaskan bahwa "1" dalam aturan 3-2-1 berarti **jauh**.
- **Serangan elektronik (*electronic attacks*)** — umumnya melalui *malware* yang masuk lewat *phishing* atau rekayasa sosial (*social engineering*). Penulis menyaksikan demonstrasi seorang pakar keamanan yang seluruh serangannya mengeksploitasi kerentanan manusia, bukan *firewall* — bahkan kabel pengisi daya yang menyebarkan *malware* lewat port USB.

**Ransomware.** *Malware* yang paling marak. Setelah masuk, ransomware mengenkripsi data secara diam-diam, lalu menawarkan kunci dekripsi dengan imbalan tebusan — dari ratusan dolar (individu) hingga jutaan dolar (organisasi besar). Tren ini diperparah oleh **ransomware-as-a-service (RaaS)**: organisasi kriminal yang menjalankan serangan atas pesanan, mengambil bagian dari keuntungan. RaaS menghilangkan satu-satunya hambatan yang tersisa (keahlian teknis), sehingga setiap organisasi makin rentan. Menurut Preston, ransomware adalah **alasan nomor satu** Anda mungkin benar-benar perlu menggunakan sistem DR Anda — lebih mungkin daripada bencana alam atau administrator nakal.

**Ancaman Internal (*Internal Threats*).** Banyak organisasi gagal bersiap terhadap serangan dari dalam. Ancaman paling umum adalah **rogue admin** — karyawan/kontraktor dengan hak istimewa yang menjadi tidak puas dan memilih merugikan organisasi. Buku sumber menyebut dua kasus nyata:

- **Yung-Hsun Lin (2004)** — administrator Unix yang memasang "*logic bomb*" pada 70 server yang diatur menghancurkan data jika ia dipecat. Bom logika itu ditemukan sebelum aktif; ia dihukum pada 2006.
- **Joe Venzor** — memasang pintu belakang (*backdoor*) yang menyamar sebagai *printer*; saat dipecat, ia mengaktifkan *malware* yang mematikan seluruh manufaktur dalam satu jam.

Untuk membatasi "radius ledakan" (*blast radius*) dari mereka yang memiliki hak istimewa, buku sumber merekomendasikan:

| Praktik | Penjelasan |
|---|---|
| **Named accounts** | Semua orang masuk sebagai dirinya sendiri; hak *root*/admin diperoleh lewat mekanisme tercatat (mis. `sudo`). |
| **Jangan bagikan sandi root** | Atur sandi acak yang tidak dicatat; akses diberikan lewat sistem ber-log. |
| **Nonaktifkan program ber-shell access** | Perintah seperti `vi` yang dapat "lari" ke *shell* sebaiknya dibatasi agar tindakan tidak lolos pencatatan. |
| **Login superuser hanya dari konsol** | Batasi akses superuser hanya dari konsol (fisik/virtual) yang aksesnya dicatat. |
| **Off-host logging** | Setiap akses akun superuser dicatat sebagai insiden keamanan, disimpan di tempat yang tak bisa dihapus penyerang. |
| **Batasi boot dari media alternatif** | Mencegah admin mem-*boot* server lalu menyunting pengaturan. |
| **Separation of powers** | Sistem backup/DR (garis pertahanan terakhir) dikelola entitas berbeda dari yang mengelola infrastruktur yang dilindunginya. |
| **Role-based administration** | Pisahkan peran: operasi harian, konfigurasi kebijakan, dan restore — agar satu orang tidak bisa berbuat terlalu banyak. |
| **Least privilege** | Setiap orang/proses hanya memiliki tingkat akses minimum yang diperlukan. |
| **Multiperson authentication** | "*Four-eyes authentication*" — dua orang harus mengautentikasi aktivitas sensitif (mis. menghapus backup, mengurangi *retention*). |

> **Catatan kritis dari sumber:** Tidak ada teknik yang sepenuhnya kebal. Bahkan enkripsi langsung dikalahkan jika penyerang berhasil masuk sebagai pengguna istimewa. Tugas sistem proteksi data adalah **mengurangi** risiko sebanyak mungkin, bukan menghilangkannya total. *"Itulah, kawan, mengapa kita mem-backup."*

#### B. Kegagalan Mekanis atau Sistem

Pada awal 1990-an, inilah alasan nomor satu penggunaan sistem backup. Kini sangat berbeda karena: (1) sebagian besar data kritis berada di media solid-state yang lebih tahan; dan (2) sistem penyimpanan redundan seperti **RAID** dan **erasure coding** menjadi norma. Namun:

- **Gangguan listrik (*power disruptions*).** *Datacenter* yang baik memiliki daya redundan dan generator, tetapi pemadaman tak terduga dapat merusak data yang sedang ditulis. Data terstruktur umumnya selamat berkat fitur integritas, tetapi proses *media recovery* basis data dapat memakan waktu lebih lama daripada *restore* penuh.
- **"There Is No Cloud."** Penulis menegaskan: cloud hanyalah "komputer orang lain". Komputer dan disk di cloud tetap dapat gagal. Tidak semua penyimpanan cloud setara: *object storage* umumnya direplikasi ke banyak lokasi, sedangkan sebagian besar *block storage* hanyalah satu LUN pada satu *storage array* di satu *datacenter* — tanpa redundansi — sehingga **harus** di-backup.
- **Kegagalan sistem (*system failure*).** Pemrogram membuat kesalahan dan hal buruk terjadi. Penulis sendiri kehilangan versi pertama bab ini akibat kombinasi kesalahan perangkat lunak dan pengguna (perangkat dikte Dragon yang menutup dokumen tanpa menyimpan) — namun ia menegaskan ini contoh di mana backup pun tidak menolong, karena dokumen hanya ada di RAM.

> **Mitos penting (dipratinjau di sini, dibahas tuntas di Bab 4):** RAID **tidak** menggantikan backup. RAID hanya melindungi *volume* dari kegagalan perangkat fisik, bukan *filesystem* di atasnya. Jika Anda menghapus berkas, terkena ransomware, atau men-*drop* tabel, RAID tidak dapat menolong.

#### C. Bencana Alam

Karena tingginya ketahanan perangkat keras masa kini, Anda justru **lebih mungkin** mengalami bencana alam daripada kegagalan perangkat keras. Bencana alam adalah salah satu alasan terbesar pentingnya aturan 3-2-1. Kunci bertahan adalah merancang sistem DR di sekitar jenis bencana yang relevan dengan wilayah Anda:

| Bencana | Karakteristik (menurut sumber) | Implikasi Desain |
|---|---|---|
| **Banjir (*Floods*)** | Sprinkler rusak, atap bocor, atau luapan sungai. Komputer dan air tidak akur. | Tempatkan situs DR di luar dataran banjir; pertimbangkan dataran tinggi. |
| **Kebakaran (*Fires*)** | Kebakaran hutan atau korsleting tunggal. Komputer dan asap tidak akur. | Backup dan DR yang solid; situs DR di luar jangkauan kebakaran. |
| **Gempa (*Earthquakes*)** | Umumnya minor; sangat lokal. | Rak di-*shock mount*; situs DR di luar radius kerusakan (relatif mudah karena gempa lokal). |
| **Badai/Topan/Siklon** | Memberi peringatan dini; storm surge & kerusakan bangunan. | Situs DR di luar jalur badai; sumber menyebut DR berbasis cloud sebagai opsi terbaik karena lokasi DR bisa di mana saja. |
| **Tornado** | Sangat terkonsentrasi dan tak terduga. | Situs DR jauh dari "tornado alley". |
| **Sinkhole** | Tanpa peringatan, diam, sangat merusak. | Pastikan situs DR jauh dari lokasi utama. |

> **Catatan Konteks Indonesia:** Indonesia berada di "Cincin Api" (*Ring of Fire*) dengan risiko gempa, tsunami, letusan gunung berapi, dan banjir yang tinggi. Prinsip yang sama berlaku: situs DR sebaiknya ditempatkan di zona seismik dan zona banjir yang berbeda dari lokasi utama. Misalnya, organisasi dengan *datacenter* utama di Jakarta sebaiknya tidak menempatkan situs DR-nya di kota yang sama atau di lempeng/zona bencana yang sama. DR berbasis cloud lintas-region menjadi pilihan menarik karena memungkinkan pemisahan geografis yang luas.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Backup** | Salinan data yang disimpan terpisah dari aslinya, digunakan untuk memulihkan (*restore*) data ke keadaan semula. |
| **Restore** | Tindakan mengembalikan data ke keadaan semula menggunakan backup. |
| **Disaster Recovery (DR)** | Proses pemulihan ketika sebagian besar lingkungan komputasi menjadi tidak beroperasi. |
| **PEBKAC** | Akronim jenaka "*Problem Exists Between Keyboard And Chair*" — kesalahan akibat pengguna. |
| **Ransomware** | Malware yang mengenkripsi data dan menuntut tebusan untuk kunci dekripsi. |
| **RaaS (Ransomware-as-a-Service)** | Layanan kriminal yang menyediakan/menjalankan serangan ransomware atas pesanan. |
| **Rogue admin** | Administrator ber-hak istimewa yang menyalahgunakan akses untuk merugikan organisasi. |
| **Logic bomb** | Kode jahat yang diatur aktif pada kondisi tertentu (mis. saat pelaku dipecat). |
| **Blast radius** | "Radius ledakan" — cakupan kerusakan yang dapat ditimbulkan satu insiden/akun. |
| **Least privilege** | Prinsip pemberian akses minimum yang diperlukan untuk suatu tugas. |
| **Separation of powers** | Pemisahan wewenang agar tidak ada satu pihak yang dapat merusak sekaligus melindungi. |
| **Multiperson / four-eyes authentication** | Autentikasi yang memerlukan dua orang untuk tindakan sensitif. |
| **RAID / Erasure coding** | Teknik penyimpanan redundan yang melindungi terhadap kegagalan perangkat (bukan pengganti backup). |
| **Object storage / Block storage** | Dua jenis penyimpanan cloud; object storage umumnya direplikasi, block storage umumnya tidak. |

### Studi Kasus

**Kasus 1 — Serangan Ransomware pada Penyedia Layanan Lokal.** Sebuah perusahaan penyedia layanan TI di Indonesia menyimpan backup pada server backup berbasis Windows yang terhubung langsung ke jaringan produksi melalui SMB. Ketika satu laptop karyawan terinfeksi ransomware melalui lampiran *phishing*, malware menyebar lewat protokol Windows (mis. RDP) dan mengenkripsi baik sistem primer maupun direktori backup yang terlihat sebagai folder pada server backup. Akibatnya, perusahaan kehilangan kedua salinan sekaligus. Analisis menurut prinsip buku sumber: pelanggaran terjadi karena tidak adanya *air gap* dan karena backup berada pada sistem operasi serta jaringan yang sama dengan sistem yang dilindunginya (dibahas tuntas di Bab 3 dan Bab 14).

**Kasus 2 — Rogue Admin pada Organisasi Pemerintah.** Seorang administrator yang akan habis masa kontraknya memiliki akses penuh ke sistem produksi **dan** sistem backup. Ia berpotensi menghapus seluruh backup, memperpendek *retention* menjadi nol, lalu merusak data primer — semua tanpa memicu alarm. Penerapan *separation of powers* (memisahkan pengelola backup dari pengelola infrastruktur) dan *multiperson authentication* (dua orang untuk menghapus backup) akan menekan risiko ini secara signifikan.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Terapkan aturan 3-2-1 sebagai patokan minimum untuk setiap dataset bernilai.
- Gunakan *named accounts*, *least privilege*, dan *separation of powers* untuk membatasi *blast radius*.
- Aktifkan *multiperson authentication* untuk operasi sensitif (penghapusan backup, pengubahan *retention*).
- Tempatkan salinan DR jauh secara geografis dari lokasi utama, di luar zona bencana yang sama.

**Kesalahan Umum:**
- Menganggap RAID atau replikasi sudah cukup sebagai pengganti backup.
- Menyimpan satu-satunya backup di akun/region cloud yang sama dengan data yang dilindungi.
- Memberi satu orang akses penuh ke infrastruktur sekaligus sistem backup.
- Menempatkan situs DR terlalu dekat dengan lokasi utama (mis. di gedung yang sama).

### Rangkuman

Ada banyak alasan untuk mem-backup data. Alasan pertama dan utama: **apa yang tidak di-backup tidak bisa di-restore**. Ancaman terhadap data, diurutkan berdasarkan kemungkinan, dimulai dari bencana akibat manusia (kecelakaan, kode buruk, serangan jahat, ransomware, ancaman internal), lalu kegagalan mekanis/sistem, dan bencana alam. Seandal apa pun komputasi dan penyimpanan masa kini, ketahanan perangkat keras hanya melindungi dari kegagalan perangkat — bukan dari serangan terhadap data itu sendiri atau bencana yang menghancurkan seluruh *datacenter*. Singkatnya, backup, recovery, dan DR kini lebih penting dan lebih kompleks daripada sebelumnya — sehingga kita perlu menetapkan kebutuhan dengan benar sebelum merancang sistem (pokok bahasan Bab 2).

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Sebutkan tiga kategori utama risiko terhadap data menurut buku sumber, dan urutkan berdasarkan kemungkinan terjadinya.
2. Jelaskan dengan kata-kata Anda sendiri apa itu PEBKAC dan mengapa kesalahan administrator lebih berbahaya daripada kesalahan *end user*.
3. Apa yang membedakan ransomware biasa dari ransomware-as-a-service (RaaS)?

**Analisis/HOTS (C4–C5):**
4. Mengapa RAID dan replikasi tidak dapat menggantikan backup? Bangun argumen yang membedakan "kegagalan perangkat" dari "kerusakan/penghapusan data".
5. Analisislah bagaimana kombinasi *separation of powers* dan *multiperson authentication* dapat menggagalkan skenario *rogue admin*. Identifikasi pula keterbatasannya.
6. Mengapa, di era sekarang, sebuah organisasi lebih mungkin mengalami bencana alam daripada kegagalan perangkat keras? Apa implikasinya bagi penempatan situs DR di Indonesia?

**Tugas Perancangan:**
7. Sebuah koperasi simpan-pinjam memiliki satu *datacenter* kecil di kota Anda. Susun daftar risiko (manusia, sistem, alam) yang relevan dengan lokasi tersebut, lalu rancang prinsip-prinsip mitigasi awal (termasuk penempatan salinan DR) yang patuh terhadap aturan 3-2-1. Jelaskan asumsi Anda.

---


## Bab 2 — Mengumpulkan dan Menentukan Tingkat Layanan

> *Bab ini dalam buku sumber ditulis oleh Jeff Rochlin, seorang praktisi berpengalaman lama di bidang operasi TI.*

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mendefinisikan** (C1) RTO dan RPO serta menjelaskan perannya sebagai dua metrik penggerak desain proteksi data.
2. **Menguraikan** (C2) proses pengumpulan kebutuhan dari para *subject matter expert* (SME) di seluruh organisasi.
3. **Menerapkan** (C3) kerangka tata kelola (*framework*) — dewan peninjau, manajemen proyek, dan dokumentasi — dalam merancang sistem proteksi data.
4. **Menganalisis** (C4) hubungan antara klasifikasi data, model *charge-back*, dan biaya pemenuhan RTO/RPO.
5. **Merancang** (C6) kerangka kebutuhan, RACI chart, dan *runbook* untuk sebuah sistem proteksi data.

### Peta Konsep

```
MENENTUKAN TINGKAT LAYANAN (SERVICE LEVELS)
│
├── Memahami apa yang dikerjakan organisasi
├── Membangun KERANGKA (framework)
│     ├── Template dokumen (revision history, glossary, dst.)
│     ├── Dewan Peninjau: Requirements, Design (DRB/ARB),
│     │   Operations (ORB), Change (CAB)
│     └── Manajemen proyek (PMO)
│
├── MENGUMPULKAN KEBUTUHAN
│     ├── RPO & RTO (metrik penggerak)
│     ├── Temukan SME: data creators, eksekutif,
│     │   compliance & governance (GDPR/CCPA, DPO)
│     ├── Solicit & Review requirements
│     ├── SLA, charge-back model, data classification
│
├── MERANCANG & MEMBANGUN
│     ├── Banyak desain (pie-in-the-sky → value engineering)
│     ├── Tinjau (PDR, PRR), pilih, bangun, uji RPO/RTO
│
└── DOKUMENTASI & IMPLEMENTASI
      ├── Tanggung jawab operasional (RACI: R-A-C-I)
      ├── Operations manual / SOP / RUNBOOK
      └── Implementasi sistem baru
```

### Materi Inti

#### Memahami Organisasi dan Membangun Kerangka

Langkah pertama adalah memahami **apa yang dikerjakan organisasi**. Bila Anda bekerja di tim proteksi data, maka — sebagaimana ditegaskan buku sumber — **semua orang di organisasi adalah pelanggan Anda**. Sebelum mengumpulkan kebutuhan, bangunlah sebuah **kerangka (*framework*)** yang mencakup:

- **Template dokumen** — dengan bagian-bagian seperti *revision history*, kebijakan/cakupan (*policy/scope*), **glosarium** (membantu pemangku kepentingan non-teknis), dan lampiran.
- **Dewan peninjau/penasihat (*review/advisory boards*)** yang bekerja secara iteratif:

| Dewan | Anggota & Tujuan |
|---|---|
| **Requirements review** | Termasuk sponsor manajemen senior (mis. CIO) untuk memastikan dukungan organisasi. |
| **Design review (DRB/ARB)** | Tim teknis (rekayasa sistem, basis data, penyimpanan, jaringan, keamanan siber); meliputi *preliminary design review* (PDR) dan *production readiness review* (PRR). |
| **Operations review (ORB)** | Tim operasional yang akan menjalankan layanan; menghasilkan *runbook*. |
| **Change review (CAB)** | "Penjaga gerbang" semua perubahan sebelum masuk produksi. |
| **Project management (PMO)** | Mengoordinasi pekerjaan, sumber daya, jadwal, dan akuntabilitas. |

#### RTO dan RPO: Dua Metrik Penggerak

> **RPO (Recovery Point Objective):** seberapa banyak data yang Anda setujui dapat hilang dalam satuan waktu.
> **RTO (Recovery Time Objective):** seberapa cepat Anda perlu memulihkan operasi setelah bencana.

Kedua metrik ini menggerakkan **setiap** rencana proteksi data dan dibahas mendalam di Bab 4. Pada tahap pengumpulan kebutuhan, keduanya menjadi pertanyaan utama yang diajukan kepada para pemangku kepentingan.

#### Menemukan dan Mewawancarai Para SME

**Subject Matter Expert (SME)** adalah pakar pada area spesifik organisasi. Mereka terbagi atas beberapa kelompok:

- **Data creators (pencipta data).** Dari mana data berasal? Tim produksi/operasi, manajemen produk, intelijen bisnis, layanan data. Mereka membantu memahami betapa sulit/mahalnya menciptakan ulang data dari nol — informasi penting untuk menetapkan RPO. Tanyakan *churn rate* (laju perubahan) data: berapa banyak transaksi per jam/hari.
- **Eksekutif.** Memberi wawasan tentang kecepatan operasi organisasi dan tenggat. Mereka cenderung meminta "semua dilindungi, tanpa downtime", hingga disodori biaya sistem yang sepenuhnya redundan dan tersebar geografis. Dari diskusi ini, RTO ditentukan dengan mempertimbangkan biaya yang dapat ditanggung organisasi.
- **Compliance & governance.** Memastikan kepatuhan terhadap hukum/regulasi privasi. Buku sumber menyebut **GDPR** (Uni Eropa) yang mensyaratkan penghapusan informasi pengguna sepenuhnya atas permintaan — termasuk dari backup dan archive — serta **CCPA** (California) yang mensyaratkan pelaporan seluruh data pelanggan, termasuk di backup. SME dari tim legal/governance (mis. *Data Protection Officer*/DPO) perlu dilibatkan.

> **Catatan Konteks Indonesia:** Sebagaimana GDPR dan CCPA di buku sumber, Indonesia memiliki **Undang-Undang Pelindungan Data Pribadi (UU PDP, UU No. 27 Tahun 2022)** yang turut mengatur hak subjek data dan kewajiban pengendali data. Prinsip yang sama berlaku: kebijakan *retention*, penghapusan, dan akses data — termasuk yang tersimpan di backup dan archive — harus mematuhi kerangka hukum yang relevan. Libatkan SME hukum/kepatuhan sejak awal. *(Konten disusun ulang untuk kepatuhan terhadap pembatasan lisensi; UU PDP disebut sebagai padanan kontekstual, bukan bagian dari buku sumber.)*

Saat **mewawancarai** SME: bawa dokumentasi dan diagram penjelas, sediakan "penerjemah" untuk audiens non-teknis, hormati waktu mereka (beberapa pertemuan singkat sering lebih baik daripada satu pertemuan panjang), dan temui kelompok secara terpisah agar pandangan mereka tidak saling memengaruhi terlalu dini.

#### Meninjau Kebutuhan: SLA, Charge-back, dan Klasifikasi Data

Setelah mengumpulkan kebutuhan, satukan semua pihak dalam tinjauan kebutuhan. Beberapa konsep penting muncul di sini:

- **Service-Level Agreement (SLA).** Tetapkan SLA untuk memenuhi RPO/RTO yang disepakati. Ingat bahwa proteksi data adalah pengguna *bandwidth* jaringan terbesar di organisasi, dan setiap sumber daya (jaringan, penyimpanan, bahkan tape) memiliki batas fisik yang berbiaya.
- **Model charge-back.** Setiap departemen bertanggung jawab secara finansial atas jumlah layanan yang digunakannya. Ini mendorong departemen untuk tidak melindungi data yang tidak perlu, sekaligus memantik diskusi tentang klasifikasi data.
- **Klasifikasi data (*data classification*).** Tidak semua data setara. Mengklasifikasikan data menjadi *critical*, *important*, *nice to have*, dan *expendable* berdampak langsung pada RPO dan RTO. Namun, banyak sistem proteksi data didesain dengan satu klasifikasi tunggal: "*important*".

> **Peringatan dari sumber:** Tekankan agar departemen tidak menghilangkan data yang benar-benar mereka butuhkan demi menekan biaya. Tugas utama adalah menyelamatkan organisasi saat terjadi masalah — *"jika tidak dilindungi, tidak bisa dipulihkan."*

Akhiri tinjauan dengan tanda tangan (fisik atau digital tervalidasi) dari semua peserta — akuntabilitas mendorong ketelitian.

#### Merancang dan Membangun Sistem

Buatlah **beberapa desain** dengan trade-off berbeda:

1. **Desain "pie in the sky"** — solusi ideal "uang bukan masalah" yang sepenuhnya memenuhi RPO/RTO. Ini menjadi cetak biru sekaligus tolok ukur biaya solusi sempurna.
2. **Value engineering** — solusi terbaik kedua yang masih memenuhi sasaran tetapi dengan kompromi (mis. biaya muka lebih rendah dengan konsekuensi pekerjaan tambahan saat eksekusi).

> **Contoh dari sumber (studio film animasi):** Tim kreatif menghasilkan jutaan berkas kecil dalam proses *compositing* dan *rendering*. Mungkin cukup menyimpan hanya berkas yang dibuat tim kreatif untuk memenuhi RPO, tetapi Anda perlu menciptakan ulang jutaan berkas turunan untuk mencapai RTO. Waktu komputasi dan manusia untuk memproses ulang menambah biaya — namun bisa jadi lebih murah daripada menangkap semua berkas dalam backup awal. Intinya: RTO harus membenarkan jumlah data yang harus di-*restore* dan dibersihkan (RPO).

Tinjau desain melalui DRB (dengan PDR dan PRR), iterasi umpan balik, pilih, lalu bangun. Jalankan secara paralel beberapa minggu, lalu lakukan uji skala penuh yang membuktikan pencapaian RPO/RTO. *"Mencapai sasaran pemulihan adalah satu-satunya alasan Anda menjalani seluruh proses ini."*

#### Tanggung Jawab Operasional dan Dokumentasi

Setiap orang harus tahu tanggung jawabnya. Gunakan **RACI chart**:

| Huruf | Makna |
|---|---|
| **R — Responsible** | Pihak yang mengerjakan aktivitas. |
| **A — Accountable** | Pihak yang dimintai pertanggungjawaban atas penyelesaian. |
| **C — Collaborator** | Pihak yang berkolaborasi untuk menyelesaikan aktivitas. |
| **I — Informed** | Pihak yang terus diberi informasi perkembangan. |

Contoh RACI chart (diadaptasi dari sumber):

| Tugas | Systems Admin | Data Ops | NOC | Head of IT |
|---|---|---|---|---|
| Jalankan job malam (*nightly job*) | R | A | C | I |
| Manajemen insiden gangguan data | A | C | R | I |
| Pengujian triwulanan | R | A | C | I |

**Dokumentasi itu baik (*Documentation Is Good*).** Tidak ada yang suka menulis dokumentasi, tetapi penulis sumber menyajikan "argumen penjualan" yang persuasif: Anda tidak akan bisa cuti, libur, tidur nyenyak, atau dipromosikan jika Anda selalu menjadi satu-satunya orang yang harus dipanggil saat sesuatu rusak. Dokumentasi memungkinkan operator *shift* malam menyelesaikan masalah tanpa membangunkan Anda.

**Runbook.** *Operations runbook* (alias SOP/*operations manual*) mengikuti template yang sama dengan dokumen desain dan kebutuhan. Ia berisi *checklist* tugas rutin berdasarkan frekuensi, bagian *FAQ*, dan daftar kontak (termasuk informasi kontrak dukungan vendor).

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Service Level / SLA** | Tingkat layanan yang dijanjikan; *Service-Level Agreement* adalah kesepakatannya. |
| **RPO / RTO** | Sasaran titik pemulihan / sasaran waktu pemulihan. |
| **SME (Subject Matter Expert)** | Pakar pada area spesifik organisasi. |
| **DRB / ARB** | *Design/Architecture Review Board* — dewan peninjau desain/arsitektur. |
| **PDR / PRR** | *Preliminary Design Review* / *Production Readiness Review*. |
| **CAB** | *Change Advisory Board* — dewan penasihat perubahan. |
| **PMO** | *Project Management Office* — kantor manajemen proyek. |
| **Charge-back model** | Model pembebanan biaya layanan ke departemen pengguna. |
| **Data classification** | Klasifikasi data menurut tingkat kekritisan. |
| **RACI** | Kerangka tanggung jawab: *Responsible, Accountable, Collaborator, Informed*. |
| **Runbook / SOP** | Manual operasional berisi prosedur dan checklist. |
| **DPO (Data Protection Officer)** | Pejabat pelindungan data, SME untuk kepatuhan privasi. |
| **GDPR / CCPA** | Kerangka hukum privasi UE / California (padanan di Indonesia: UU PDP). |

### Studi Kasus

**Kasus — Sistem Informasi Akademik Kampus.** Sebuah universitas hendak membangun sistem proteksi data untuk sistem informasi akademik (SIA), keuangan, dan repositori riset. Tim proteksi data:
1. Mengidentifikasi SME: bagian akademik (data creator nilai & KRS), bagian keuangan (data transaksi), dan unit hukum (kepatuhan UU PDP terhadap data pribadi mahasiswa).
2. Menetapkan RPO/RTO berbeda per dataset: SIA saat masa KRS (puncak transaksi) memerlukan RPO/RTO ketat; data riset historis dapat bertoleransi RPO/RTO lebih longgar.
3. Menyusun dua desain (ideal vs *value-engineered*) dan menyajikannya ke dewan peninjau.
4. Menetapkan RACI: tim infrastruktur (R) menjalankan backup harian, kepala UPT TI (A) bertanggung jawab, NOC (C), dan pimpinan (I).
5. Menyusun *runbook* berisi prosedur restore SIA dan kontak vendor.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Dapatkan RTO/RPO dari **organisasi**, bukan dari tim TI, dan dokumentasikan dengan tanda tangan.
- Sajikan beberapa alternatif desain dengan trade-off biaya yang jelas.
- Bangun *runbook* dari sudut pandang orang yang akan menjalankan tugas.

**Kesalahan Umum:**
- Menebak RTO/RPO tanpa berkonsultasi dengan unit bisnis (baik karena malas maupun karena mengasumsikan permintaan tidak realistis).
- Menerima RTO/RPO begitu saja lalu mengabaikannya.
- Menjadikan dokumentasi sebagai renungan akhir, bukan bagian integral proyek.

### Rangkuman

Merancang sistem proteksi data dimulai dari memahami organisasi dan membangun kerangka tata kelola. Dua metrik penggerak — RTO dan RPO — harus berasal dari organisasi melalui proses pengumpulan kebutuhan yang melibatkan SME dari pencipta data, eksekutif, dan kepatuhan. Konsep SLA, *charge-back*, dan klasifikasi data membantu menyeimbangkan biaya dan kebutuhan. Desain dibuat dalam beberapa alternatif, ditinjau secara iteratif (PDR, PRR), dibangun, dan diuji terhadap RPO/RTO. Akhirnya, tanggung jawab operasional dipetakan dengan RACI chart, dan seluruh sistem didokumentasikan dalam *runbook* agar dapat dijalankan tanpa ketergantungan pada perancangnya. Jika Anda mengoperasikan sistem backup tanpa SLA RTO/RPO yang disepakati, Anda sedang mengundang masalah.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Definisikan RTO dan RPO. Mengapa keduanya disebut "metrik penggerak" desain proteksi data?
2. Jelaskan peran masing-masing dewan: requirements review, DRB, ORB, dan CAB.
3. Apa makna setiap huruf dalam RACI?

**Analisis/HOTS (C4–C5):**
4. Mengapa eksekutif cenderung meminta "RTO dan RPO nol", dan bagaimana cara yang tepat menanggapi permintaan tersebut menurut buku sumber?
5. Analisislah bagaimana model *charge-back* dapat memengaruhi keputusan klasifikasi data sebuah departemen.

**Tugas Perancangan:**
6. Untuk sebuah rumah sakit daerah, susun kerangka kebutuhan proteksi data: identifikasi minimal empat SME, usulkan RPO/RTO berbeda untuk minimal tiga dataset, dan buat RACI chart untuk tiga tugas operasional utama.

---


## Bab 3 — Backup dan Archive Sangat Berbeda

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mendefinisikan** (C1) secara tepat istilah *backup*, *copy*, *restore*, *archive*, dan *retrieve*.
2. **Membedakan** (C2) backup dari archive berdasarkan tujuan penyimpanan dan cara pengambilan kembali.
3. **Menjelaskan** (C2) tiga komponen aturan 3-2-1 dan menerapkannya untuk menilai apakah suatu salinan layak disebut backup.
4. **Menganalisis** (C4) teknik perlindungan data backup/archive: enkripsi, *air gap* (fisik & virtual), dan *immutability*.
5. **Mengevaluasi** (C5) klaim vendor tentang "immutability" dan mengidentifikasi salah-label yang umum.

### Peta Konsep

```
BACKUP vs ARCHIVE
│
├── BACKUP = salinan data, disimpan terpisah, untuk RESTORE
│     ├── "Copy": reproduksi byte-for-byte (bukan snapshot virtual)
│     ├── "Stored separately": bukan convenience copy
│     ├── "For restoring": kembalikan SATU hal ke SATU titik waktu
│     └── ATURAN 3-2-1 (3 versi, 2 media, 1 di tempat lain)
│
├── ARCHIVE = salinan referensi, disimpan dgn metadata, untuk RETRIEVE
│     ├── Serve as reference (bukan untuk restore)
│     ├── Additional metadata (full-text search, dst.)
│     └── RETRIEVE = ambil banyak hal dari rentang tanggal lebar
│
└── MELINDUNGI BACKUP & ARCHIVE
      ├── Encryption (in-flight & at-rest)
      ├── Air gap (fisik: tape di rak; virtual: obfuscation)
      └── Immutability (tak dapat diubah; perlu banyak kontrol)
```

### Materi Inti

Penulis sumber mengambil sikap tegas: backup dan archive adalah **dua tindakan yang sangat berbeda** untuk **dua tujuan yang berbeda**. Memang ada produk yang memenuhi kedua kebutuhan, dan itu tidak masalah. Yang menjadi masalah adalah menggunakan produk yang jelas-jelas hanya produk backup untuk memenuhi kebutuhan archive — praktik yang umum tetapi menambah risiko dan biaya.

#### Apa Itu Backup?

> **Definisi:** *Backup adalah salinan data yang disimpan terpisah dari aslinya dan digunakan untuk memulihkan (*restore*) data ke keadaan semula, biasanya setelah data dihapus atau rusak.*

Tiga elemen definisi ini perlu dibedah:

**1. "Copy" (Salinan).** Sebuah *copy* adalah reproduksi byte-for-byte yang berisi konten identik dengan aslinya. Perintah `cp` (Linux) atau `copy` (Windows), serta perintah backup (`tar`, `dump`, `cpio`, atau perangkat lunak komersial) menghasilkan *copy*. Salinan sejati mencakup seluruh metadata, terutama pengaturan keamanan dan izin.

Yang **bukan** salinan: **snapshot virtual** yang dibuat di *filesystem* atau sistem penyimpanan (mis. snapshot di NAS filer, XFS, Volume Shadow Copy Services/VSS di Windows, atau snapshot hypervisor seperti VMware/Hyper-V). Snapshot ini tidak berisi konten asli — ia **merujuk** ke aslinya untuk sebagian besar datanya. Setiap "salinan" yang membutuhkan aslinya untuk berfungsi bukanlah salinan sejati, melainkan **salinan virtual**. Namun, mereplikasi snapshot ke sistem lain menjadikannya salinan sejati — bahkan salinan yang lebih unggul, karena seluruh data dalam volume tersebut berasal dari titik waktu yang sama.

> **Catatan terminologi:** Beberapa hal yang disebut "snapshot" sebenarnya *image copy*. Contoh: AWS EBS "snapshots" sebenarnya salinan byte-for-byte, sehingga lebih tepat disebut *image copy*. Penulis menyebut snapshot virtual NAS sebagai *convenience copy* — nyaman, tetapi bukan backup.

**2. "Stored Separately from the Original" (Disimpan Terpisah dari Aslinya).** Jika salinan disimpan di *filesystem*, komputer, atau basis data yang sama, itu hanyalah *convenience copy*. Salinan yang dapat dihancurkan oleh hal yang sama yang menghancurkan aslinya bukanlah backup.

**3. "For the Purposes of Restoring" (Untuk Tujuan Pemulihan).** Di sinilah inti pembedaan: *mengapa* Anda membuat salinan. Jika untuk memulihkan aslinya saat rusak, itu **backup**. (Archive juga salinan yang disimpan terpisah, tetapi dibuat untuk *retrieve*, bukan *restore*.)

#### Apa Itu Restore?

> **Definisi:** *Restore* mengembalikan **satu hal** ke **satu titik waktu**.

Untuk melakukan restore, Anda membutuhkan: nama server/VM/aplikasi, kredensial yang tepat, nama subset (*filesystem*, direktori, tabel, *bucket*), nama objek (berkas/record), dan — yang krusial — **tanggal** saat objek berada dalam keadaan yang diinginkan. Umumnya restore mengembalikan ke titik waktu yang **relatif baru** (kemarin atau lebih baru), dengan pengecualian (mis. memulihkan berkas yang terhapus enam bulan lalu, atau memulihkan ke titik sebelum infeksi ransomware). *"A restore returns a single thing to a single point in time. That's it."*

#### Aturan 3-2-1 Secara Mendalam

> **Aturan 3-2-1:** Miliki setidaknya **tiga** versi data Anda, pada **dua** media yang berbeda, dengan **satu** di antaranya disimpan di tempat lain.

Penulis menyebut aturan ini sebagai "hukum fundamental yang menjadi dasar seluruh backup — bagi desain backup, ia seperti E = mc² bagi fisika." Mari bedah tiga komponennya:

**"Tiga versi data Anda."** Dalam pemahaman penulis, ini berarti tiga versi *tambahan* (asli tidak dihitung). Tiga versi memberi perlindungan terhadap rangkaian kesalahan — misalnya berkas yang rusak diam-diam lalu ikut ter-backup, sehingga versi terbaru pun rusak. Tiga adalah minimum, bukan maksimum. Aplikasi produktivitas modern dan *transaction log* basis data bahkan menciptakan ribuan versi sepanjang hari.

**"Pada dua media yang berbeda."** Jangan simpan semua backup pada media yang sama — apalagi pada media yang sama dengan aslinya.

> **Contoh dari sumber (Mac OS Time Machine):** Mempartisi satu disk menjadi dua "drive" lalu mem-backup partisi pertama ke partisi kedua adalah praktik yang keliru. Bila disk fisiknya rusak, Anda kehilangan keduanya. Backup harus berada pada disk/komputer yang berbeda.

> **Implikasi penting (SaaS):** Penulis menolak menerima versi yang disimpan di dalam produk SaaS (mis. *Microsoft 365 Retention Policies*, *Google Archive*) sebagai backup yang sah, karena semuanya hanya versi tambahan yang disimpan di sistem yang sama dengan yang dilindunginya — melanggar bagian "dua media".

**"Satu di antaranya di tempat lain."** Dahulu berbunyi "*off-site*". Idenya: setidaknya satu salinan berada pada jarak yang sangat aman dari objek yang dilindungi.

> **Studi Kasus dari sumber — codespaces.com (2014):** Perusahaan ini mengiklankan diri sebagai tempat aman menyimpan kode dengan "triple redundancy" dan banyak backup. Namun semua backup disimpan di **akun dan region yang sama**. Seorang peretas memperoleh akses akun istimewa (sebagian karena MFA tidak diaktifkan) dan menuntut tebusan. Saat perusahaan mencoba mengunci akun, peretas menghapus segalanya — VM, *object storage*, basis data, **dan backup**. Perusahaan itu berhenti beroperasi. *"The 3-2-1 rule matters."*

Saran penulis untuk sumber daya cloud: buat **akun terpisah di region terpisah** yang khusus menampung backup, lakukan *cross-region backup*, dan kunci akses akun ini sekuat mungkin (idealnya *multiperson authentication*; bila tak tersedia, simulasikan dengan MFA yang dua faktornya dibagi ke dua orang).

#### Apa Itu Archive?

> **Definisi:** *Archive adalah salinan data yang disimpan di lokasi terpisah, dibuat untuk berfungsi sebagai salinan referensi, dan disimpan dengan metadata yang cukup untuk menemukan data tersebut tanpa mengetahui dari mana asalnya.*

Dua bagian pertama definisi ini sama dengan backup. Yang membedakan adalah **tujuan** penyimpanan dan pengambilan, serta **cara** penyimpanan dan pengambilan:

- **Untuk berfungsi sebagai referensi.** Archive tidak digunakan untuk memulihkan server/berkas ke keadaan semula, melainkan untuk menemukan data demi tujuan lain (sering kali *e-discovery*). Contoh: produsen satelit mengarsipkan gambar CAD agar dapat dirujuk bertahun-tahun kemudian.
- **Disimpan dengan metadata tambahan.** Metadata (mis. pengirim, penerima, subjek, tanggal email; atau nama proyek) disimpan agar mudah dikueri. Sistem archive canggih mendukung *full-text search* — pencarian berdasarkan konten berkas/email, bukan sekadar metadata.

> **Penegasan dari sumber:** Memindahkan backup ke media penyimpanan jangka panjang yang lebih murah **bukan** "mengarsipkan backup". Tidak ada yang namanya "mengarsipkan backup" — Anda hanya memindahkan backup ke penyimpanan jangka panjang. *"Old backups do not magically turn into archives any more than old grape juice turns into wine."* Lamanya penyimpanan tidak menentukan apakah sesuatu backup atau archive; **mengapa** dan **bagaimana** ia disimpanlah yang menentukan.

#### Apa Itu Retrieve?

> **Definisi:** *Retrieve* mengumpulkan **sekelompok informasi terkait** berdasarkan konten dan metadatanya, biasanya dari **banyak server/aplikasi** dan **rentang tanggal yang lebar**.

*Retrieve* adalah kebalikan dari *restore*. Saat melakukan *retrieve*, Anda umumnya tidak memiliki informasi yang dibutuhkan untuk *restore* (nama server, direktori, dsb.). Contoh: "semua email yang mengandung kata *Apollo* dalam tiga tahun terakhir, dari berbagai sistem email, tanpa tahu nama servernya."

> **Inti pembedaan:** *"In the same way backups make lousy archives, archives make lousy backups."* (Sebagaimana backup buruk untuk archive, archive pun buruk untuk backup.) Inilah mengapa *Microsoft 365 Retention Policies* dan *Google Archive* — yang merupakan archive — buruk untuk restore.

#### Melindungi Data Backup dan Archive

Data proteksi (backup/archive) juga rentan terhadap kegagalan perangkat, bencana, dan tindakan manusia. Tiga teknik utama untuk melindunginya:

**1. Enkripsi (*Encryption*).** Hal terbaik untuk mencegah akses tak sah adalah mengenkripsi data. Perangkat backup modern mendukung enkripsi perangkat keras dan manajemen kunci pihak ketiga; perangkat lunak/layanan modern mendukung enkripsi *in-flight* (saat transit) dan *at-rest* (saat diam). Enkripsi tidak mencegah pencurian/penghapusan backup, tetapi mencegah peretas **membaca**-nya — sehingga menggagalkan pemerasan.

> **Studi Kasus dari sumber (Bonobos/Walmart):** Seseorang mengakses dan mempublikasikan basis data pelanggan 70 GB dengan mengakses **backup cloud**-nya. Data dipublikasikan dalam bentuk teks-biasa. Pelajaran: backup yang disimpan di cloud oleh pihak yang bukan pakar cloud sering kali tidak diamankan dan tidak dienkripsi. Enkripsi akan menghentikan serangan ini.

**2. Air Gap (Celah Udara).** Secara harfiah, *air gap* adalah celah udara antara sistem yang dilindungi dan sistem pelindung — pemisahan untuk membatasi *blast radius* dari "*rolling disaster*" (satu sistem menulari yang lain).

- **Air gap fisik.** Dahulu selalu ada: backup ke tape, lalu tape diserahkan ke "*man in a van*" yang membawanya ke fasilitas penyimpanan (mis. Iron Mountain). Setiap media dilacak via *barcode*, dipindai masuk/keluar, dengan *two-person authentication* untuk akses di luar jadwal.
- **Air gap virtual.** Karena kini hampir semua sistem terhubung internet, penulis memperkenalkan istilah **virtual air gap**. Cara mencapainya:

| Metode | Penjelasan |
|---|---|
| **Nonaktifkan/batasi RDP** | RDP adalah vektor serangan ransomware paling umum; batasi via VPN dan MFA. |
| **Sistem operasi berbeda** | Gunakan OS berbeda untuk server backup (mis. Linux) dari server produksi (umumnya Windows). |
| **Pisahkan penyimpanan** | Jangan *mount* sistem target dedup sebagai direktori/drive yang langsung dapat diakses OS server backup (hindari NFS/SMB langsung). |
| **Gunakan object storage** | Mengubah protokol penyimpanan mengaburkan backup dari serangan biasa. |
| **Gunakan immutable storage** | Penyimpanan yang menjaga data selama periode tertentu, bahkan Anda pun tak dapat menghapusnya. |
| **Gunakan tape** | "Tidak ada *air gap* yang lebih baik daripada salinan tape di rak di lokasi fisik berbeda." Jangan lupa enkripsi tape. |
| **Gunakan layanan backup** | Layanan di mana administrator pun tidak memiliki akses *login* ke server backup. |

**3. Immutability (Ketidakberubahan).** Sesuatu yang *immutable* tidak dapat diubah oleh siapa pun, termasuk personel istimewa. Jika Anda menetapkan data harus *immutable* selama 90 hari, Anda tidak dapat mengubahnya menjadi 45 hari kemudian untuk data yang sudah ditulis. (Anda boleh mengubah periode *retention*, tetapi hanya berlaku untuk data yang ditulis **setelah** perubahan.)

Empat catatan penting tentang immutability menurut sumber:

| Catatan | Penjelasan |
|---|---|
| **Tidak ada yang benar-benar abadi** | Tape WORM dan media optik tetap bisa terbakar; immutable storage tetap tunduk pada hukum fisika. Idenya: hilangkan dan mitigasi risiko sebanyak mungkin. |
| **Immutability butuh banyak kontrol** | Sistem berbasis disk menggunakan *object storage* dengan nilai *hash* per objek; ubah konten, *hash* berubah. Sistem harus "dikeraskan" (*hardened*), akses fisik dikontrol. |
| **Immutable bukan berarti kebal (*impervious*)** | Sistem dapat membuktikan objek tak berubah, tetapi tidak menghilangkan risiko akses fisik/kerusakan (tape WORM yang meleleh tetap tak berguna). |
| **Banyak yang salah-label "immutable"** | Beberapa vendor menyebut backup mereka *immutable* padahal hanya "*protected against attacks*". Bila admin backup masih dapat **mengurangi *retention*** (mis. ke nol hari, efektif menghapus), maka backup itu **tidak** *immutable*. Tanyakan ini kepada vendor. |

> **Opini penulis:** Cloud-based immutable storage saat ini menawarkan opsi terbaik untuk *immutability* — biasanya direplikasi ke banyak lokasi, menawarkan *immutability* sebagai opsi, dan memastikan pelanggaran fisik *datacenter* tidak membahayakan data ini.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Copy** | Reproduksi byte-for-byte berisi konten identik dengan aslinya (termasuk metadata). |
| **Convenience copy** | Salinan yang nyaman tetapi disimpan berdekatan dengan aslinya; bukan backup. |
| **Virtual snapshot** | Salinan virtual yang merujuk ke aslinya; bukan salinan sejati hingga direplikasi. |
| **Image copy** | Salinan byte-for-byte (mis. "EBS snapshot") yang sebenarnya salinan penuh, bukan snapshot virtual. |
| **3-2-1 rule** | 3 versi, 2 media, 1 di tempat lain — penentu apakah sesuatu adalah backup. |
| **Archive** | Salinan referensi dengan metadata, untuk *retrieve* (bukan restore). |
| **Retrieve** | Mengambil banyak data terkait berdasarkan konten/metadata dari rentang tanggal lebar. |
| **E-discovery** | Penemuan data elektronik untuk keperluan hukum. |
| **Encryption (in-flight/at-rest)** | Enkripsi data saat transit / saat tersimpan. |
| **Air gap (physical/virtual)** | Pemisahan (fisik/elektronik) antara sistem produksi dan sistem proteksi. |
| **Rolling disaster** | Bencana berantai di mana satu sistem menulari sistem lain. |
| **Immutability / WORM** | Ketidakberubahan data / *Write Once Read Many*. |
| **Man in a van** | Istilah lama untuk kurir yang membawa tape ke penyimpanan luar lokasi. |

### Studi Kasus

**Kasus — "Backup Mahal untuk Archive".** Sebuah organisasi menerima satu permintaan *e-discovery* untuk email yang cocok kriteria tertentu selama tiga tahun. Organisasi tidak memiliki sistem archive email, tetapi memiliki *full backup* mingguan Exchange selama tiga tahun. Andai mereka memiliki archive email, mereka cukup mengajukan satu kueri (mis. "semua email tiga tahun terakhir dari Curtis yang berisi frasa '3-2-1 rule'") dan menerima berkas PST untuk diserahkan ke pengacara. Karena hanya punya backup, mereka harus melakukan *restore* berulang dari 156 minggu yang lalu, satu per satu — proses yang sangat mahal dan rumit. Pelajaran: **jangan gunakan sistem backup sebagai sistem archive.**

**Kasus Konteks Indonesia — Kepatuhan UU PDP.** Sebuah perusahaan e-commerce lokal menyimpan backup berisi data pribadi pelanggan selama tujuh tahun "untuk berjaga-jaga". Ketika seorang pelanggan menggunakan hak untuk dilupakan, perusahaan kesulitan menghapus data tersebut dari backup yang dirancang untuk *mengingat*, bukan *melupakan*. Sebagaimana dicatat penulis sumber tentang GDPR, isu ini belum memiliki panduan baku. Pelajaran: kebijakan *retention* backup harus dirancang dengan mempertimbangkan kewajiban kepatuhan, dan kebutuhan jangka panjang sebaiknya dipenuhi oleh sistem **archive** yang andal melakukan *retrieve*, bukan oleh backup. *(Adaptasi konteks; UU PDP bukan bagian dari buku sumber.)*

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Pastikan setiap backup mematuhi aturan 3-2-1. Bila tidak, "itu bukan backup".
- Enkripsi semua backup (*in-flight* dan *at-rest*).
- Terapkan *air gap* (fisik atau virtual) dan, jika memungkinkan, *immutable storage* berbasis cloud.

**Kesalahan Umum:**
- Menyebut snapshot virtual sebagai backup.
- Menyimpan satu-satunya salinan backup di akun/region cloud yang sama.
- Menggunakan produk backup untuk kebutuhan archive (dan sebaliknya).
- Mempercayai klaim "immutable" tanpa memverifikasi apakah admin masih bisa memperpendek *retention*.

### Rangkuman

Backup dan archive adalah dua hal yang sangat berbeda. **Backup** adalah salinan sekunder dari data primer, dibuat untuk *restore* (mengembalikan satu hal ke satu titik waktu). **Archive** adalah salinan referensi dengan metadata, dibuat untuk *retrieve* (mengambil banyak data dari rentang tanggal lebar, sering untuk *e-discovery*). Backup sejati mematuhi **aturan 3-2-1**: tiga versi, dua media, satu di tempat lain. Data backup dan archive — sebagai garis pertahanan terakhir — harus dilindungi melalui **enkripsi**, **air gap** (fisik atau virtual), dan **immutability**. Fitur archive bawaan produk SaaS bukanlah backup karena tidak mematuhi 3-2-1 dan dirancang untuk *retrieve*, bukan *restore*.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Tuliskan definisi backup dan archive, lalu jelaskan perbedaan tujuannya.
2. Mengapa snapshot virtual NAS bukan termasuk backup hingga ia direplikasi?
3. Uraikan tiga komponen aturan 3-2-1 dan tujuan masing-masing.

**Analisis/HOTS (C4–C5):**
4. Analisis kasus codespaces.com: bagian mana dari aturan 3-2-1 yang dilanggar, dan bagaimana pelanggaran itu berujung pada kebangkrutan?
5. Evaluasilah pernyataan vendor: "Backup kami immutable karena dilindungi dari ransomware." Pertanyaan kritis apa yang harus Anda ajukan menurut buku sumber?
6. Mengapa "mengarsipkan backup" adalah konsep yang keliru? Kaitkan dengan perbedaan *restore* dan *retrieve*.

**Tugas Perancangan:**
7. Rancang strategi perlindungan data backup untuk sebuah perusahaan fintech: tentukan bagaimana Anda akan menerapkan enkripsi, *virtual air gap*, dan *immutability*, serta jelaskan bagaimana desain Anda mematuhi aturan 3-2-1.

---


## Bab 4 — Dasar-Dasar Backup dan Recovery

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) pentingnya pengujian pemulihan (*recovery testing*) sebagai konsep paling dasar.
2. **Membedakan** (C2) berbagai level backup: *full*, *incremental* (typical, cumulative/differential, dengan level, *block-level*), *synthetic full*, dan *incremental forever*.
3. **Mendefinisikan** (C1) dan **menghitung** (C3) metrik pemulihan (RTO, RPO, RTA, RPA) dan metrik kapasitas.
4. **Mengevaluasi** (C5) mitos-mitos umum tentang backup dan archive.
5. **Membedakan** (C2) backup tingkat-item (*item-level*) dan tingkat-citra (*image-level*) serta metode seleksi backup.
6. **Menganalisis** (C4) keunggulan *selective exclusion* dibanding *selective inclusion*.

### Peta Konsep

```
DASAR BACKUP & RECOVERY
│
├── RECOVERY TESTING ("backup belum jadi backup sebelum diuji")
│
├── LEVEL BACKUP
│     ├── Full (traditional)
│     ├── Incremental: typical, cumulative (differential),
│     │   dengan level (TOH), block-level, source dedupe
│     ├── Synthetic full (copy / virtual / incremental forever)
│     └── "Apakah level backup masih relevan?"
│
├── METRIK
│     ├── Pemulihan: RTO, RPO | RTA, RPA
│     ├── Kapasitas: lisensi, storage, throughput, compute
│     ├── Backup window, success/failure, retention
│     └── Right to be forgotten
│
├── MITOS (RAID, replikasi, IaaS/PaaS, SaaS, simpan bertahun, tape mati)
│
└── ITEM vs IMAGE LEVEL + METODE SELEKSI
      ├── Item-level vs Image-level (CBT, file-level recovery dari image)
      └── Selective inclusion vs Selective exclusion; tag/folder-based
```

### Materi Inti

#### Pengujian Pemulihan (*Recovery Testing*)

Konsep paling dasar: satu-satunya alasan kita mem-backup adalah agar dapat melakukan *restore*. Dan satu-satunya cara mengetahui apakah Anda dapat melakukan restore adalah dengan **mengujinya**. Pengujian rutin juga melatih personel — agar restore besar pertama yang mereka lakukan bukan saat keadaan darurat produksi. Frekuensi pengujian sebaiknya sebanding dengan frekuensi restore aktual: uji DR besar beberapa kali setahun, tetapi restore berkas/VM individual sebaiknya dilakukan setidaknya sekali seminggu per orang. Cloud mempermudah ini karena Anda tidak perlu memperebutkan sumber daya.

> *"A backup isn't a backup until it's been tested!"* — Ben Patridge

#### Level Backup

Pada dasarnya ada dua kategori besar: mem-backup **semuanya** (*full backup*) atau hanya yang **berubah** (*incremental backup*). Sebagian besar level adalah warisan era tape.

**Traditional Full Backup.** Menyalin semua dari sistem yang di-backup (kecuali yang dikecualikan). Memerlukan I/O besar dan dapat sangat memengaruhi performa, terutama jika beberapa VM pada hypervisor yang sama melakukan *full backup* serentak.

**Traditional Incremental Backup.** Mem-backup semua berkas/record yang berubah sejak backup sebelumnya. Kecuali dinyatakan lain, *incremental* bersifat *full-file* (seluruh berkas di-backup meski hanya satu blok berubah). Variannya:

| Jenis Incremental | Perilaku |
|---|---|
| **Typical incremental** | Mem-backup data yang berubah sejak backup **apa pun** sebelumnya (full atau incremental). Paling umum. |
| **Cumulative incremental** | Mem-backup semua yang berubah sejak **full backup** terakhir. Restore hanya butuh full + cumulative terakhir. Penulis menyebutnya "cumulative incremental", menghindari istilah *differential* karena maknanya berbeda antar-produk. |
| **Incremental dengan level (0–9)** | Level 0 = full; level N mem-backup yang berubah sejak level di bawahnya. Dasar bagi skema **Tower of Hanoi (TOH)**. |
| **Block-level incremental** | Hanya mem-backup blok/byte yang berubah (kurang dari satu berkas). Membutuhkan mekanisme pelacakan (mis. *bitmap*/CBT pada hypervisor). Jauh lebih hemat I/O & bandwidth. |
| **Source-side deduplication** | Perluasan *block-level*: memproses blok baru untuk mengecek apakah sudah pernah dilihat sistem; jika sudah, tidak di-backup lagi. Paling hemat (dibahas Bab 5). |

**Tower of Hanoi (TOH).** Skema progresif (mis. `0 3 2 5 4 7 6 ...`) yang membuat sebagian besar berkas yang berubah ter-backup **dua kali** — melindungi dari kegagalan satu media, relevan di dunia tape. Namun, penulis menekankan prinsip **K.I.S.S.** (*Keep It Simple*): bila skema membingungkan Anda, restore-nya pun akan menyulitkan.

**Synthetic Full Backup.** Backup yang berperilaku seperti *full* saat restore, tetapi dibuat **tanpa** *full backup* tradisional. Tiga metode:

1. **Synthetic full by copying** — menyalin berkas/blok dari backup yang tersedia ke media lain (bisa dijalankan kapan saja tanpa membebani klien, tetapi membebani I/O disk sumber & target).
2. **Virtual synthetic full** — hanya pada sistem *target deduplication*; backup baru cukup "menunjuk" ke blok dari backup lain (hampir instan, tanpa pergerakan data).
3. **Incremental forever** — sistem dirancang dari awal agar tidak pernah lagi membutuhkan *full backup*; setiap item dari incremental terbaru disimpan sebagai objek terpisah (umumnya di *object storage*). Hanya layak dengan disk sebagai target.

**Apakah Level Backup Masih Relevan?** Level backup adalah warisan era tape. Di era disk dan *target deduplication*, *full backup* setiap hari pun tidak memboroskan penyimpanan, dan tidak ada lagi pemuatan puluhan tape incremental. Sistem modern bahkan hanya menggunakan satu level: *block-level incremental*. Semakin Anda menggunakan teknologi modern, semakin tidak relevan pembahasan level.

> **Tentang *Archive Bit* di Windows:** Bit "*ready for archiving*" menandai berkas baru/berubah agar di-backup, lalu dihapus setelahnya. Masalahnya: program backup pertama yang berjalan akan menghapus bit ini, sehingga program kedua tidak akan mem-backup berkas yang sama — sehingga pengguna dapat menggagalkan tujuan sistem backup. Penulis tidak pernah menyukai *archive bit*; untungnya bit ini hampir tidak relevan lagi pada backup tingkat-VM.

#### Metrik

**Metrik Pemulihan (paling penting).** Tidak ada yang peduli berapa lama Anda mem-backup; mereka peduli berapa lama Anda *restore* dan berapa banyak data hilang.

- **RTO (Recovery Time Objective)** — durasi pemulihan yang disepakati. Jamnya mulai saat insiden dan berhenti saat aplikasi **benar-benar daring** dan bisnis normal kembali — bukan sekadar saat penyalinan data selesai. Boleh ada beberapa RTO berbeda untuk aplikasi berbeda.
- **RPO (Recovery Point Objective)** — jumlah data yang dapat hilang, diukur dalam waktu. Tidak ada gunanya menyepakati RPO satu jam jika backup hanya berjalan sekali sehari (RPO terbaik = 24 jam).
- **RTA & RPA (Recovery Time/Point Actual)** — diukur hanya saat pemulihan terjadi (nyata atau uji). RTA/RPA mengukur sejauh mana objektif (RTO/RPO) benar-benar tercapai. Kenyataannya, RTA/RPA banyak organisasi jauh dari RTO/RPO yang disepakati.

> **Aturan praktis (Stuart Liddle, dikutip sumber):** Tentukan frekuensi backup dengan membagi RPO dengan tiga. RPO tiga hari → backup setiap hari, sehingga dua kegagalan backup berturut-turut masih dapat ditoleransi tanpa melewati RPO.

```
Diagram-Teks: RTO/RPO (objektif) vs RTA/RPA (aktual)

  Yang DISEPAKATI:        Yang TERUKUR saat restore:
  ┌───────────┐           ┌───────────┐
  │   RPO     │ <-------> │   RPA     │  (kehilangan data nyata)
  │   RTO     │ <-------> │   RTA     │  (waktu pemulihan nyata)
  └───────────┘           └───────────┘
  Jika RPA/RTA jauh dari RPO/RTO → redesain sistem atau revisi objektif.
```

**Metrik Kapasitas.** Perlu dipantau pada sistem on-premises maupun cloud:

| Metrik | Penjelasan |
|---|---|
| **License/workload usage** | Jumlah lisensi & beban kerja yang di-backup; pantau agar tidak kehabisan. |
| **Storage capacity & usage** | Apakah kapasitas cukup untuk backup & DR? *Object storage* tumbuh otomatis dan ditagih per pemakaian; *block storage* ditagih per kapasitas yang disediakan. |
| **Throughput capacity & usage** | Kecepatan menerima backup (MB/s atau TB/jam). Penting agar throughput backup cocok dengan kecepatan tape (lihat Bab 12). |
| **Compute capacity & usage** | Kemampuan komputasi di belakang sistem; cloud yang dirancang dengan benar dapat menskalakan otomatis. |

**Backup Window.** Rentang waktu yang diizinkan untuk menjalankan backup (mis. 18.00–06.00). Pantau seberapa penuh *window* terisi. Sistem *incremental forever* (CDP, near-CDP, *block-level*, *source dedupe*) umumnya tidak memerlukan *backup window* karena berjalan singkat dengan dampak performa rendah — sehingga dapat berjalan sepanjang hari (mis. setiap jam atau setiap lima menit). CDP sejati berjalan terus-menerus.

**Keberhasilan & Kegagalan, serta Retention.** Pantau persentase keberhasilan backup/recovery dari waktu ke waktu. **Retention** ditentukan oleh organisasi (kebutuhan hukum/regulasi), bukan oleh TI; tentukan pula berapa lama data disimpan pada tiap *tier* penyimpanan. Terkait ini, **right to be forgotten** (hak untuk dilupakan, dipopulerkan GDPR/CCPA) menimbulkan pertanyaan sulit: bagaimana menghapus data dari sistem backup yang dirancang untuk *mengingat*? Penulis mengakui belum ada jawaban baku.

#### Mitos Backup dan Archive

Penulis membantah sejumlah mitos yang kerap muncul dalam rapat:

| Mitos | Bantahan |
|---|---|
| "Tidak perlu mem-backup RAID." | RAID hanya melindungi *volume* dari kegagalan perangkat, bukan *filesystem*. Penghapusan, ransomware, atau *drop table* tetap merusak data. |
| "Tidak perlu mem-backup data yang direplikasi." | Replikasi menyalin **semua** — termasuk kesalahan dan virus. "Replikasi tidak memperbaiki kesalahan Anda; ia hanya membuat kesalahan Anda lebih efisien." |
| "Tidak perlu mem-backup IaaS/PaaS." | Vendor menyediakan fasilitas backup, tetapi tidak mem-backup atas nama Anda. Keluarkan backup dari akun & region asalnya. |
| "Tidak perlu mem-backup SaaS." | Layanan SaaS besar (mis. Microsoft 365, Google Workspace) hampir tidak pernah menyertakan backup. Cari kata "backup/recovery/restore" di kontrak Anda — biasanya tidak ada. |
| "Backup harus disimpan bertahun-tahun." | Produk backup umumnya bukan produk archive. Menyimpan backup bertahun-tahun untuk *e-discovery* mengundang biaya besar. Penulis pribadi menyetel *retention* 18 bulan. |
| "Tape sudah mati." | Tape bukan target awal yang baik untuk backup (karena ketidakcocokan kecepatan), tetapi sangat baik untuk **archive jangka panjang**: lebih murah, lebih andal menulis bit, dan tahan menyimpan lama. "Lebih banyak tape terjual hari ini daripada sebelumnya." |

#### Item-Level vs Image-Level

- **Item-level backup** — mem-backup item individual (mis. berkas). Mendukung restore granular tetapi *incremental*-nya umumnya *full-file*.
- **Image-level backup** — mem-backup *image* disk (mis. berkas VMDK/VHD pada level hypervisor). **Changed-Block Tracking (CBT)** memungkinkan *image-level* melakukan *block-level incremental*. Restore *image* jauh lebih cepat untuk *filesystem* berkepadatan tinggi (banyak berkas kecil per TB).
- **File-level recovery dari image-level backup** — dipecahkan dengan: (a) *mount* berkas VMDK sebagai volume virtual (drag-and-drop berkas), atau (b) meng-*index* image sebelumnya agar restore file-level langsung didukung.
- **Combining image- and file-level** — sebagian besar pelanggan kini mem-backup VM pada *image level* sambil tetap dapat melakukan *incremental* dan restore *item-level*. Ini juga mempermudah *bare-metal recovery*.

#### Metode Seleksi Backup

Penting agar yang Anda kira ter-backup memang benar-benar ter-backup. **Prasyarat:** sistem backup harus mengetahui keberadaan sistem yang di-backup (sistem tidak otomatis mendeteksi SaaS atau hypervisor baru).

- **Selective inclusion** — administrator menetapkan secara individual apa yang di-backup (mis. "hanya drive D:"). **Risiko:** setiap penambahan basis data/filesystem baru harus dikonfigurasi manual; bila terlewat, data baru tidak pernah ter-backup.
- **Selective exclusion (automatic inclusion)** — mem-backup semua kecuali yang dikecualikan (mis. `/tmp`). **Lebih aman:** efek terburuknya hanya mem-backup data tak berguna, bukan melewatkan data penting.
- **Tag-based / folder-based inclusion** — VM/basis data baru otomatis mendapat kebijakan backup berdasarkan *tag*/folder. **Wajib** memiliki kebijakan backup *default* untuk menangkap sistem yang tidak ber-*tag*, lalu memantaunya.

> **Prinsip dari sumber:** *"No one ever got fired because their backup system backed up too much data, but plenty of people have been fired for not backing up enough data."* Maka, gunakan *selective exclusion* secara default; prioritaskan keamanan/perlindungan dahulu, biaya kemudian.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Full / Incremental backup** | Backup seluruhnya / hanya yang berubah. |
| **Cumulative incremental (differential)** | Backup semua perubahan sejak full terakhir. |
| **Block-level incremental** | Backup hanya blok yang berubah. |
| **Synthetic full** | Backup yang berperilaku full tanpa full backup sesungguhnya. |
| **Incremental forever** | Sistem yang tidak pernah lagi membutuhkan full backup. |
| **Changed-Block Tracking (CBT)** | Pelacakan blok yang berubah (mis. oleh hypervisor). |
| **RTO / RPO / RTA / RPA** | Objektif & aktual waktu/titik pemulihan. |
| **Backup window** | Rentang waktu yang diizinkan untuk backup. |
| **Retention** | Lama penyimpanan backup/archive (ditentukan organisasi). |
| **Right to be forgotten** | Hak untuk dilupakan (penghapusan data pribadi). |
| **Item-level / Image-level** | Backup tingkat item / tingkat citra disk. |
| **Selective inclusion / exclusion** | Metode seleksi: sertakan eksplisit / kecualikan eksplisit. |
| **Tower of Hanoi (TOH)** | Skema level backup agar berkas ter-backup ganda. |

### Studi Kasus

**Kasus — Menghitung RTA pada Restore Tape (diadaptasi dari Bab 13 sumber).** Sebuah *datacenter* dengan *full backup* 500 TB, laju perubahan 10% (50 TB/hari), RPO 24 jam, dan *backup window* 10 jam. *Full* bulanan disebar merata (≈17,86 TB/hari) + 50 TB incremental = 67,86 TB/hari, memerlukan throughput ≈1,88 GB/s. Untuk server 10 TB dengan RTO 4 jam: satu drive LTO-8 pada 750 MB/s memulihkan dalam ≈3,7 jam (masih masuk RTO). Namun, bila digunakan *multiplexing* 20 untuk membuat tape "bahagia" saat backup, kecepatan restore turun menjadi ≈1/20 (≈37,5 MB/s), sehingga restore 10 TB memakan ≈74 jam — **jauh** melewati RTO. Inilah alasan utama orang beralih dari tape sebagai target awal backup. (Detail tape dibahas di Bab 12.)

**Kasus — RAID Bukan Backup (Kurt Buff, dikutip sumber).** Seorang teman menggunakan Windows NT4 Workstation pada RAID1 tanpa backup, karena merasa "aman". Sebuah *patch* OS merusak *filesystem* akibat inkompatibilitas *driver*, meski disk-nya baik-baik saja. Ia kehilangan ribuan foto. Pelajaran: RAID melindungi terhadap kegagalan perangkat, bukan kerusakan *filesystem*.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Uji pemulihan secara rutin; iklankan metrik keberhasilan restore untuk membangun kepercayaan.
- Bandingkan RTA/RPA dengan RTO/RPO secara jujur; bila timpang, revisi objektif atau desain.
- Gunakan *selective exclusion* (automatic inclusion) sebagai default.

**Kesalahan Umum:**
- Tidak pernah menguji restore (sehingga RTA/RPA tidak diketahui).
- Menyetel RPO ketat tetapi hanya menjalankan backup sekali sehari.
- Mengandalkan *selective inclusion* sehingga sistem baru terlewat dari backup.
- Menyimpan backup bertahun-tahun seolah-olah ia archive.

### Rangkuman

Konsep paling dasar adalah pengujian pemulihan: backup belum menjadi backup hingga diuji. Level backup (*full*, *incremental*, *synthetic full*, *incremental forever*) sebagian besar warisan era tape dan makin tidak relevan di era disk/deduplikasi. Metrik pemulihan (RTO, RPO, RTA, RPA) mengendalikan desain — dan kejujuran membandingkan objektif dengan aktual sangat penting. Metrik kapasitas (lisensi, penyimpanan, throughput, komputasi), *backup window*, serta kebijakan *retention* turut dipantau. Berbagai mitos (RAID/replikasi/IaaS/PaaS/SaaS tidak perlu di-backup; backup disimpan bertahun-tahun; tape mati) perlu diluruskan. Akhirnya, backup *image-level* (dengan CBT) dan strategi *selective exclusion* menjadi pendekatan yang lebih aman dan efisien di lingkungan modern.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bedakan *typical incremental*, *cumulative incremental*, dan *block-level incremental*.
2. Jelaskan tiga cara membuat *synthetic full backup*.
3. Apa perbedaan RTO/RPO (objektif) dengan RTA/RPA (aktual)?

**Analisis/HOTS (C4–C5):**
4. Mengapa *selective exclusion* lebih aman daripada *selective inclusion*? Gunakan prinsip "tidak ada yang dipecat karena mem-backup terlalu banyak data".
5. Evaluasilah mitos "tidak perlu mem-backup SaaS". Bukti apa yang disarankan penulis untuk memverifikasinya?
6. Dengan aturan praktis "RPO dibagi tiga", hitung frekuensi backup untuk RPO 6 jam dan jelaskan toleransinya terhadap kegagalan backup.

**Tugas Perancangan:**
7. Untuk sistem informasi perpustakaan dengan *full backup* 2 TB dan laju perubahan 5%/hari, rancang strategi level backup (pilih antara *incremental forever* berbasis disk vs full+incremental tradisional). Tetapkan RPO/RTO yang masuk akal, lalu jelaskan bagaimana Anda akan mengujinya.

---


## BAGIAN II — Teknologi Penyimpanan dan Sumber Data

### Pengantar Bagian II

Setelah memahami fondasi konseptual, Bagian II membahas **bagaimana** data disimpan dalam sistem proteksi dan **apa saja** sumber data yang perlu dilindungi. Bagian ini menandai pergeseran besar dalam industri: dari era tape ke era disk dan deduplikasi, serta dari *datacenter* tradisional ke beban kerja modern (cloud, kontainer, IoT).

Empat bab dalam bagian ini:

- **Bab 5** menjelaskan teknologi yang membuat disk layak secara ekonomi sebagai target backup: **deduplikasi**. Bab ini juga membahas berbagai arsitektur penggunaan disk (D2D2T, D2D2D, D2C, D2D2C) serta konsep pemulihan (*image recovery*, *file-level recovery*, *instant recovery*).
- **Bab 6** membahas sumber data **tradisional**: server fisik (termasuk NAS), server virtual (VM, VSS, API hypervisor), serta desktop, laptop, dan perangkat seluler.
- **Bab 7** — menurut penulis kemungkinan bab terpenting — membahas **basis data**: model penyajian, model basis data, model konsistensi, terminologi, serta cara mem-backup dan memulihkan basis data tradisional, PaaS, dan *serverless*.
- **Bab 8** membahas sumber data **modern**: cloud publik (IaaS, PaaS, *serverless*, SaaS), cloud hibrida, Docker/Kubernetes, dan IoT, serta cara membuat keputusan backup.

> **Prinsip Pemandu Bagian II:** "Cloud bukanlah sihir; cloud hanyalah komputer orang lain." Apa pun teknologi penyimpanan dan jenis sumber datanya, prinsip dasar proteksi data — terutama aturan 3-2-1 — tetap berlaku.

---

## Bab 5 — Menggunakan Disk dan Deduplikasi untuk Proteksi Data

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) cara kerja deduplikasi (*chunking*, *hashing*, *hash table*) dan apa yang dapat dilakukannya.
2. **Membedakan** (C2) *target deduplication* dan *source deduplication*, serta *inline* vs *post-process*.
3. **Menganalisis** (C4) cakupan deduplikasi (*dedupe scope*) dan mengapa rasio deduplikasi tidak boleh dibandingkan antar-vendor.
4. **Membandingkan** (C4) arsitektur penggunaan disk: *disk staging*, D2D2T, D2D2D, D2C, dan D2D2C.
5. **Membedakan** (C2) konsep pemulihan: *image recovery*, *file-level recovery*, dan *instant recovery*.
6. **Mengevaluasi** (C5) jenis pemulihan yang tepat untuk skenario tertentu.

### Peta Konsep

```
DISK & DEDUPLIKASI
│
├── DEDUPLIKASI (membuat disk layak ekonomis)
│     ├── Cara kerja: chunk → hash (SHA-1/2/256) → hash table → buang duplikat
│     ├── Dedupe scope: backup set < host < appliance < site < global
│     ├── Jangan bandingkan rasio dedup; bandingkan disk terpakai
│     ├── Target vs Source dedupe; Hybrid; Inline vs Post-process
│
├── DISK DALAM SISTEM BACKUP
│     ├── Disk staging (cache satu malam)
│     ├── D2D2T, D2D2D, D2C, D2D2C
│
└── KONSEP PEMULIHAN
      ├── Image recovery (cepat utk filesystem padat)
      ├── File-level recovery (direct, SMB/NFS mount, image mount, SaaS)
      └── Instant recovery (boot VM langsung dari backup)
```

### Materi Inti

Disk berevolusi dari nyaris tak terpakai dalam backup menjadi **target utama** sebagian besar backup hari ini. Dua pendorong: (1) munculnya *disk array* berbasis disk ATA/SATA yang jauh lebih murah; dan (2) — yang benar-benar membuat disk layak — **deduplikasi**, yang menurunkan biaya disk setidaknya satu orde besaran (*order of magnitude*).

#### Deduplikasi (*Deduplication*)

> **Definisi:** Deduplikasi (*dedupe*) adalah identifikasi dan eliminasi data duplikat dalam suatu dataset yang dapat mencakup banyak backup dari banyak tempat sepanjang waktu.

**Apa yang dapat dilakukan dedupe?** Dedupe dapat mengurangi kebutuhan disk secara dramatis dengan mengeliminasi data duplikat:

- **Versi sepanjang waktu** — banyak versi berkas yang sama (mis. spreadsheet yang disunting tiap hari) sebagian besar identik; dedupe hanya menyimpan bagian unik tiap versi.
- **Berkas sama di banyak tempat** — berkas/OS yang sama pada ratusan VM hanya disimpan sekali.
- **Duplikat tersembunyi** — berkas yang sama tersebar di laptop, folder *Sent* email, *Inbox* penerima, dan beberapa *file server* — semua dikenali dan dieliminasi.

**Cara kerja dedupe.** Sistem mengiris data menjadi potongan kecil (*chunks*, beberapa kilobyte hingga ratusan kilobyte, ukuran tetap atau variabel). Tiap *chunk* dijalankan melalui algoritma *hashing* kriptografis (SHA-1, SHA-2, atau SHA-256) yang menghasilkan urutan alfanumerik unik untuk konten tersebut. Sistem memeriksa *hash table* (*dedupe index*): jika *hash* sudah ada, *chunk* dianggap redundan; jika belum, *chunk* unik disimpan (umumnya setelah dikompresi) dan *hash* ditambahkan.

> **Contoh dari sumber:** SHA-1 untuk kalimat "The quick brown fox jumps over the lazy dog." adalah `408D94384216F890FF7A0C3528E8BED1E0B01621`. Mengubah satu huruf saja menghasilkan *hash* yang sepenuhnya berbeda.

**Dedupe scope (cakupan).** Semakin luas cakupan, semakin banyak duplikat dieliminasi, tetapi semakin banyak sumber daya dibutuhkan:

| Scope | Penjelasan |
|---|---|
| **Backup set** | Hanya membandingkan backup dalam satu set (mis. backup basis data tertentu). |
| **Host** | Membandingkan seluruh backup satu host. |
| **Appliance** | Semua backup ke satu *appliance* dibandingkan (paling umum). |
| **Site** | Semua backup dari satu situs. |
| **Global** | Semua backup ke sistem dibandingkan, lintas tipe/host/situs. |

**Jangan bandingkan rasio dedup.** Rasio yang diiklankan vendor berdasarkan kondisi lab dengan data buatan dan tidak dapat dibandingkan antar-vendor. *"An SE once told a customer to do 30 full backups to the same appliance — look, 30:1 dedupe ratio!"* Yang penting bukan rasio, melainkan **berapa banyak disk yang dipakai** untuk mem-backup dataset yang sama dengan cara backup normal Anda. **Ukuran *chunk* penting:** semakin kecil irisan, semakin baik dedup tetapi semakin banyak *hash* yang harus dibuat & dicari — selalu ada *trade-off* performa vs efektivitas. *Object storage* pada dasarnya adalah sistem deduplikasi tingkat-berkas.

**Target vs Source Deduplication:**

| Aspek | Target Dedupe | Source Dedupe |
|---|---|---|
| Lokasi proses | Di *appliance* setelah backup diterima | Di klien, sebelum data dikirim |
| Koneksi | NFS/SMB, VTL, atau protokol proprietary | Bagian dari perangkat lunak backup |
| Keunggulan | Sedikit perubahan konfigurasi (cabut tape, colok appliance) | Hemat bandwidth & CPU; ramah VM/cloud/remote |
| Rasio tampak | Lebih besar | Lebih kecil (data sudah dieliminasi sebelum server) |

**Inline vs Post-process (pada target dedupe):**

- **Inline** — dedup dilakukan *in-band*, *in-memory*, di CPU **sebelum** data ditulis ke disk. Keunggulan: tidak memboroskan siklus I/O menulis data yang sudah dikenal; backup langsung siap direplikasi. Kelemahan: butuh CPU lebih kuat, dapat memperlambat backup yang masuk.
- **Post-process (asynchronous)** — dedup dilakukan *out of band* **setelah** data ditulis ke disk. Bekerja lebih baik untuk *instant recovery* karena menyimpan salinan terbaru dalam format asli di disk biasa.

> **Opini penulis:** Bila merancang dari nol, kecil kemungkinan memilih *target deduplication* dibanding *source deduplication*, karena keunggulan *source dedupe* dalam mengelola replikasi dan *retention*.

#### Menggunakan Disk dalam Sistem Backup

| Arsitektur | Penjelasan |
|---|---|
| **Disk staging** | Beli disk cukup untuk backup satu malam sebagai *cache*, lalu segera salin ke tape. Mengatasi ketidakcocokan kecepatan, tetapi sebagian besar restore tetap dari tape. |
| **D2D2T (Disk-to-Disk-to-Tape)** | Beli disk (terdeduplikasi) cukup untuk seluruh *retention*; semua backup ke disk lalu disalin ke tape sebagai salinan *off-site*. Disk menjadi sumber utama restore. |
| **D2D2D (Disk-to-Disk-to-Disk)** | Backup ke disk terdeduplikasi, lalu replikasi ke sistem disk lain dari vendor yang sama. Bisa dikelola appliance (transparan) atau perangkat lunak backup. |
| **D2C (Direct-to-Cloud)** | Membutuhkan *source dedupe*; *chunk* unik dikirim langsung ke cloud. Tantangan: *initial seed* (backup pertama) dan restore besar. |
| **D2D2C (Disk-to-Disk-to-Cloud)** | Backup ke disk on-premises lalu replikasi ke cloud sebagai salinan *just-in-case*; cloud menggantikan peran tape/Iron Mountain. |

> **Catatan:** Anda **tidak dapat** mencampur vendor deduplikasi pada replikasi. Saat menyalin data terdeduplikasi ke tape, praktik terbaik adalah me-*rehydrate* (mengembalikan ke bentuk penuh) terlebih dahulu, karena menyimpan data terdeduplikasi di tape berisiko (satu berkas bisa tersebar di banyak tape).

#### Konsep Pemulihan

**Image Recovery.** Memulihkan *image backup* (mis. VMDK/VHD) langsung ke perangkat. Mengatasi isu *filesystem* dan jauh lebih cepat untuk *filesystem* berkepadatan tinggi (mis. volume 2 TB berisi jutaan berkas HTML kecil). Kelemahan: pendekatan "semua atau tidak sama sekali", dan harus dipulihkan ke tempat yang dapat me-*mount*-nya. Di luar dunia VM, *image recovery* terutama terlihat pada *bare-metal recovery*.

**File-Level Recovery.** Mayoritas restore adalah pemulihan satu berkas penting. Tiga cara:

1. **Direct restore** — pilih berkas di UI; perangkat lunak berkomunikasi dengan agen di mesin tujuan. Tantangan: VM sering tidak memiliki agen (di-backup pada level hypervisor).
2. **SMB/NFS mount** — berbagi drive via SMB (Windows) atau NFS (Linux). Lebih aman digunakan sesekali sebagai *sumber* restore daripada sebagai tujuan tulis.
3. **Image mount** — menjadikan *image* dapat di-*mount* sebagai drive (seperti ISO), lalu drag-and-drop berkas.

> **Memulihkan data SaaS:** Umumnya ada kemitraan API dua arah antara vendor SaaS dan vendor backup. Namun tidak selalu: untuk Microsoft 365, vendor backup harus menggunakan *Outlook Web Access* (tidak ada API khusus backup); beberapa bagian (mis. *Yammer*, *Planner*) tidak bisa di-backup, dan percakapan dalam *Teams channels* (saat itu) bisa di-backup tetapi **tidak bisa di-restore**.

**Instant Recovery.** Hasil sampingan dari backup berbasis disk (mustahil dengan tape). Idenya: *mount* *image* boot drive VM secara *read/write* lalu **boot** VM langsung dari backup — memulihkan VM secara instan tanpa restore tradisional. Dua cara: (a) backup disimpan dalam format asli sehingga langsung dapat di-*mount*; atau (b) perangkat lunak menyiapkan *image* di muka.

- **Penyimpanan penting.** Sistem *post-process* bekerja lebih baik untuk *instant recovery* karena menyimpan salinan terbaru dalam format asli. Sistem *inline* harus terus me-*rehydrate*/dedup, sehingga performanya terbatas (sumber: "satu VM lambat; lebih dari beberapa, buruk sekali").
- **Kasus penggunaan.** *Instant recovery* **bukan** pengganti rencana DR. Cocok untuk menghidupkan satu-dua VM saat ketersediaan lebih penting daripada performa, atau untuk uji/pengembangan. Salah satu pemakaian realistis: hidupkan VM secara instan sebagai pengganti sementara, lalu gunakan *Storage vMotion* untuk memindahkannya ke VM produksi sambil restore sebenarnya berjalan.

**Memilih Jenis Pemulihan.** Sering kali pilihan ditentukan oleh produk Anda. Bila semua tersedia: gunakan *file-level direct restore* untuk kebanyakan kasus; gunakan *image restore* untuk *filesystem* berkepadatan tinggi atau saat memulihkan seluruh VM; gunakan *instant recovery* bila waktu sangat krusial.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Deduplication (dedupe)** | Identifikasi & eliminasi data duplikat. |
| **Chunk** | Potongan data hasil irisan untuk dedup. |
| **Hash / hash table (dedupe index)** | Nilai unik konten / basis data semua hash. |
| **Dedupe scope** | Cakupan perbandingan dedup (backup set → global). |
| **Target / Source deduplication** | Dedup di appliance / di klien. |
| **Inline / Post-process** | Dedup sebelum / sesudah ditulis ke disk. |
| **Rehydrate** | Mengembalikan data terdeduplikasi ke bentuk penuh. |
| **Disk staging / D2D2T / D2D2D / D2C / D2D2C** | Arsitektur penggunaan disk dalam backup. |
| **Image recovery** | Pemulihan citra disk langsung ke perangkat. |
| **Instant recovery** | Boot VM langsung dari backup tanpa restore tradisional. |
| **Storage vMotion** | Fitur VMware untuk memindahkan VM yang sedang berjalan. |

### Studi Kasus

**Kasus — Patch Tuesday dan Source Dedupe.** Sebuah organisasi mem-backup 100 VM Windows sehari setelah hari *patch*, ketika ratusan megabyte *patch* diunduh ke tiap VM. Dengan *source deduplication*, blok baru hanya di-backup dari VM pertama; 99 VM lain tidak mengirim ulang blok yang sama. Inilah keunggulan *source dedupe* dalam menghemat bandwidth lintas jaringan.

**Kasus — Filesystem Berkepadatan Tinggi.** Sebuah volume 2 TB berisi jutaan berkas HTML kecil. Restore *file-level* akan memakan waktu sangat lama, sedangkan *image-level recovery* nyaris tidak memakan waktu. Pelajaran: kepadatan berkas menentukan pilihan jenis pemulihan.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Saat mengevaluasi dedup, uji dengan **data produksi Anda** dan bandingkan **disk terpakai**, bukan rasio.
- Pilih *source dedupe* untuk lingkungan remote/cloud/laptop demi penghematan bandwidth.
- Untuk *instant recovery*, uji performa dengan jumlah VM senyata mungkin (bukan hanya satu-dua).

**Kesalahan Umum:**
- Membandingkan rasio dedup antar-vendor untuk mengambil keputusan.
- Mencampur vendor deduplikasi saat replikasi.
- Menyimpan data terdeduplikasi langsung ke tape tanpa *rehydrate*.
- Mengandalkan *instant recovery* sebagai rencana DR penuh.

### Rangkuman

Disk menjadi target utama backup berkat **deduplikasi**, yang mengiris data menjadi *chunk*, meng-*hash*-nya, dan mengeliminasi duplikat. Cakupan dedup berkisar dari *backup set* hingga *global*; rasio dedup **tidak** boleh dibandingkan antar-vendor — yang penting adalah disk yang benar-benar terpakai. *Target dedupe* mudah diadopsi, tetapi *source dedupe* lebih hemat bandwidth dan lebih ramah cloud. Berbagai arsitektur disk (staging, D2D2T, D2D2D, D2C, D2D2C) menawarkan trade-off berbeda. Untuk pemulihan, tersedia *image recovery* (cepat untuk *filesystem* padat), *file-level recovery* (paling umum), dan *instant recovery* (boot VM langsung dari backup) — masing-masing dengan kasus penggunaan yang tepat.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Jelaskan langkah-langkah cara kerja deduplikasi dari *chunk* hingga *hash table*.
2. Bedakan *target* dan *source deduplication*, serta *inline* dan *post-process*.
3. Apa perbedaan *image recovery*, *file-level recovery*, dan *instant recovery*?

**Analisis/HOTS (C4–C5):**
4. Mengapa rasio deduplikasi tidak boleh dijadikan dasar perbandingan antar-vendor? Apa metrik yang seharusnya digunakan?
5. Analisis mengapa sistem *post-process* lebih cocok untuk *instant recovery* dibanding *inline*.
6. Bandingkan D2C dan D2D2C dari sudut pandang peran cloud dan tantangan restore besar.

**Tugas Perancangan:**
7. Rancang arsitektur penggunaan disk untuk kantor cabang dengan bandwidth terbatas yang ingin backup tersimpan juga di cloud. Pilih antara D2C dan D2D2C, jelaskan penanganan *initial seed* dan restore besar, serta mekanisme dedup yang Anda pilih.

---


## Bab 6 — Sumber Data Tradisional

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mengidentifikasi** (C1) sumber data tradisional: server fisik (termasuk NAS), server virtual, desktop/laptop, dan perangkat seluler.
2. **Membedakan** (C2) *standard backup* dan *bare-metal backup* pada server fisik.
3. **Menjelaskan** (C2) tiga cara mem-backup NAS filer: proxy, NDMP, dan replikasi snapshot.
4. **Menjelaskan** (C2) konsep VSS dan API backup tingkat hypervisor (VADP, Hyper-V VSS writer).
5. **Menganalisis** (C4) mengapa "memperlakukan VM sebagai mesin fisik" bermasalah (*noisy neighbor*).
6. **Mengevaluasi** (C5) opsi backup untuk desktop/laptop dan perangkat seluler.

### Peta Konsep

```
SUMBER DATA TRADISIONAL
│
├── SERVER FISIK
│     ├── Standard backup (agen + jadwal)
│     ├── Bare-metal backup (recovery server itu sendiri)
│     └── Backup NAS: proxy (NFS/SMB) | NDMP | replikasi snapshot
│
├── SERVER VIRTUAL (VM)
│     ├── VM-level backup (pura-pura fisik → noisy neighbor)
│     ├── VSS (crash-consistent vs application-consistent)
│     └── Backup tingkat hypervisor: VADP, Hyper-V VSS,
│         snapshot-based, HCI, CI, hypervisor lain (KVM/AHV)
│
├── DESKTOP & LAPTOP (laptop sbg cache; opsi backup)
│
└── PERANGKAT SELULER (cloud sync, physical sync, MDM)
```

### Materi Inti

Dahulu, semua data ada di *datacenter* — server fisik, terhubung *dumb terminal*. Kini, server jarang fisik dan sering tidak berada di gedung organisasi; laptop, ponsel, dan tablet pun menyimpan data organisasi. *"The datacenter is no longer the center of data."* Bab ini membahas beban kerja **tradisional**: komputer (server fisik & virtual, desktop, laptop, perangkat seluler).

#### Server Fisik

Server fisik tunggal menjalankan satu OS (Windows, Linux, Unix komersial) dan dapat berperan sebagai Active Directory, DNS, *file server* (NAS), *application server*, atau *database server*. Dua jenis backup perlu dipertimbangkan:

- **Standard backup** — mem-backup data dari layanan yang disediakan server (filesystem, layanan direktori, konfigurasi DNS, atau data basis data). Caranya: pasang agen perangkat lunak backup dan konfigurasikan jadwal.
- **Bare-metal backup** — berfokus memulihkan **server fisiknya sendiri**. Tantangan terbesar pada server fisik *legacy*: bila server rusak, Anda harus mengganti perangkat keras beserta OS dan konfigurasinya. Kesulitan utama: mengumpulkan informasi *boot-level* dari *boot drive*, yang berada di bawah lapisan *filesystem*. *Bare-metal recovery* menjadi kurang populer setelah virtualisasi merebak.

> **Catatan:** Buku sumber tidak membahas *mainframe* dan *minicomputer* (penulis tak pernah berinteraksi dengannya), tetapi mengakui keduanya belum mati — *"setelah kiamat nuklir, kita masih akan melihat penjual mainframe dan tape drive."*

**Backup NAS.** NAS filer adalah server khusus yang umumnya **tidak** mendukung pemasangan agen standar. Tiga pilihan:

| Metode | Penjelasan | Keunggulan/Kelemahan |
|---|---|---|
| **Proxy (NFS/SMB)** | Pasang klien backup pada server standar yang me-*mount* share NFS/SMB lalu mem-backup dari sana. | (+) Berkas tampak seperti biasa, dapat di-restore ke mana saja. (−) Lalu lintas backup tampak seperti lalu lintas pengguna; filer tak bisa memprioritaskan; bisa merugikan performa pengguna. |
| **NDMP** | API yang dibuat khusus industri NAS; perangkat lunak backup berkomunikasi langsung dengan filer. | (+) Efisien. (−) Vendor filer menentukan format backup (semua berbeda: `dump`/`tar`/`cpio`), sehingga **tidak portabel** antar-vendor; mengikat Anda ke vendor filer. |
| **Replikasi snapshot** | Buat snapshot pada satu filer dan replikasikan ke filer lain. | (+) "Cara resmi"; tercepat untuk restore. (−) Risiko *rolling disaster* yang menghapus ketiga salinan. |

> **Saran penulis untuk NAS:** Gunakan replikasi snapshot untuk salinan siap-pakai lokal, **lalu** gunakan sistem backup (idealnya *source dedupe*) untuk salinan *off-site* — mendapatkan "yang terbaik dari kedua dunia": salinan lokal siap-pakai dan salinan jarak-jauh *just-in-case*. Penulis kini lebih memilih proxy NFS/SMB daripada NDMP karena portabilitas data dan kesederhanaan.

#### Server Virtual (VM)

VM adalah "sesuatu yang berpura-pura menjadi mesin fisik"; OS-nya (*guest OS*) masih mengira ia berjalan di sistem fisik. Di bawahnya ada **hypervisor** (vSphere, Hyper-V, KVM, Xen, AHV) pada server fisik. Dua kategori besar backup VM:

**VM-level backup (pura-pura fisik).** Memasang agen di *guest OS* dan mem-backup seperti mesin fisik. Masalah utamanya adalah **I/O**: *full backup* sangat membebani, dan jika banyak VM pada hypervisor yang sama melakukannya serentak, ini menciptakan masalah **noisy neighbor** — memperlambat semua VM. Inilah yang mendorong vendor hypervisor menyediakan API backup tingkat-hypervisor.

**Apa itu VSS?** *Volume Shadow Copy Service* (VSS) adalah sistem snapshot khusus di Windows yang memungkinkan backup *application-consistent* atas *filesystem*/aplikasi. Dua jenis konsistensi:

| Jenis | Penjelasan |
|---|---|
| **Crash-consistent** | Sekonsisten "mencabut listrik lalu mem-backup". Biasanya cukup, tetapi backup individual dapat rusak tanpa diketahui hingga dibutuhkan. |
| **Application-consistent** | Konsisten sedemikian rupa sehingga aplikasi selalu dapat memulihkan diri. Lebih diinginkan. |

VSS bekerja melalui **VSS writer** per aplikasi (mis. SQL Writer). Saat backup dimulai, sistem backup (sebagai *requestor*) meminta snapshot dari tiap VSS writer, lalu mem-backup dari snapshot konsisten tersebut. VSS juga dapat memotong (*truncate*) *transaction log* SQL Server/Exchange setelah backup.

**Backup khusus untuk hypervisor:**

| Metode | Penjelasan |
|---|---|
| **VADP** | *vSphere Storage APIs for Data Protection* — API VMware paling dikenal; mendukung *full* & *block-level incremental* (via CBT) tanpa memasang klien di VM. Berintegrasi dengan VSS di VM Windows untuk konsistensi aplikasi. Untuk VM Linux tidak ada padanan VSS; VMware hanya menyinkronkan RAM ke disk sebelum snapshot. |
| **Hyper-V VSS writer** | Hyper-V berjalan di Windows, sehingga memiliki VSS writer; alur mirip VADP. |
| **Snapshot-based backup** | Sistem penyimpanan mengintegrasikan API backup hypervisor dengan kemampuan snapshot-nya; cepat, dampak rendah, harus direplikasi agar sah sebagai backup. |
| **HCI (Hyper-Converged Infrastructure)** | Perangkat keras khusus menjalankan hypervisor dengan penyimpanan terintegrasi; sering menyertakan proteksi data berbasis snapshot bawaan (kadang terintegrasi DR ke cloud). |
| **CI (Converged Infrastructure)** | Sistem lebih besar dari beberapa vendor; umumnya memakai hypervisor standar sehingga tak perlu penanganan khusus. |
| **Hypervisor lain (KVM/AHV)** | Perlu memastikan API proteksi data setara dengan VMware/Hyper-V; pilih vendor backup yang mendukung atau gunakan proteksi bawaan HCI. |

#### Desktop dan Laptop

Pertanyaan kuncinya: **apakah data disimpan di perangkat?** Beberapa laptop hanya berfungsi sebagai *cache* untuk menciptakan data di cloud (mis. Chromebook ke Google Workspace) — jika tidak pernah menyimpan data, bahkan penulis pun tidak melihat perlunya mem-backup. Namun bila pengguna benar-benar menciptakan data lokal, perangkat tersebut perlu di-backup. Opsi backup desktop/laptop perlu mempertimbangkan bahwa perangkat tidak selalu menyala — backup harus agak otonom dan berjalan saat perangkat aktif. Sumber juga menekankan metode yang ramah-bandwidth (mis. *source dedupe* / *block-level incremental forever*) untuk laptop.

#### Perangkat Seluler

| Metode | Penjelasan |
|---|---|
| **Cloud sync** | Data disinkronkan ke layanan cloud. |
| **Physical sync** | Sinkronisasi fisik ke komputer. |
| **Mobile device backup** | Backup perangkat seluler. |
| **MDM (Mobile Device Management)** | Manajemen perangkat seluler — mengelola dan mengamankan perangkat. |

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Standard backup / Bare-metal backup** | Backup data layanan / backup untuk memulihkan server fisiknya. |
| **NAS filer** | Server berkas khusus (NFS/SMB). |
| **NDMP** | *Network Data Management Protocol* — protokol backup khusus NAS. |
| **Hypervisor / Guest OS** | Perangkat lunak penjalan VM / OS di dalam VM. |
| **VSS / VSS writer** | *Volume Shadow Copy Service* dan komponen per-aplikasinya. |
| **Crash-consistent / Application-consistent** | Tingkat konsistensi backup. |
| **VADP** | API proteksi data vSphere. |
| **CBT (Changed-Block Tracking)** | Pelacakan blok berubah pada hypervisor. |
| **HCI / CI** | *Hyper-Converged* / *Converged Infrastructure*. |
| **Noisy neighbor** | Masalah performa akibat banyak VM membebani I/O hypervisor serentak. |
| **MDM** | *Mobile Device Management*. |

### Studi Kasus

**Kasus — Noisy Neighbor di Lingkungan Virtual Kampus.** Sebuah pusat data kampus menjalankan 30 VM pada satu host VMware dan mem-backup-nya dengan memperlakukan tiap VM sebagai mesin fisik (agen di tiap VM, *full backup* serentak). Akibatnya I/O host jenuh, backup berjalan sangat lambat, dan performa seluruh VM (termasuk SIA) anjlok. Solusi sesuai sumber: beralih ke backup tingkat-hypervisor (VADP) dengan *block-level incremental* (CBT) dan integrasi VSS untuk VM Windows, sehingga tidak perlu agen di tiap VM dan dampak I/O jauh berkurang.

**Kasus — Backup Laptop Dosen yang Bepergian.** Para dosen menyimpan data riset di laptop yang sering dibawa ke luar kampus. Backup yang dijadwalkan dari server (menjangkau laptop) tidak akan berhasil karena laptop tidak selalu daring di jaringan kampus. Solusi: gunakan metode backup laptop yang otonom dan ramah-bandwidth (*source dedupe*) yang berjalan saat laptop aktif, sehingga restore pun dapat dilakukan meski pengguna berada di luar kantor.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Gunakan backup tingkat-hypervisor (VADP/Hyper-V VSS) alih-alih memperlakukan VM sebagai mesin fisik.
- Untuk NAS, kombinasikan replikasi snapshot (lokal) + *source dedupe* (off-site).
- Backup laptop harus otonom, ramah-bandwidth, dan dapat di-restore dari luar kantor.

**Kesalahan Umum:**
- Menjalankan *full backup* serentak pada banyak VM di host yang sama (*noisy neighbor*).
- Mengandalkan NDMP yang mengunci Anda ke satu vendor filer.
- Mengabaikan backup laptop yang menyimpan data unik.

### Rangkuman

Sumber data tradisional mencakup server fisik (memerlukan *standard* dan kadang *bare-metal backup*), NAS (proxy, NDMP, atau replikasi snapshot), server virtual (sebaiknya di-backup pada level hypervisor via VADP/VSS untuk menghindari *noisy neighbor* dan memperoleh konsistensi aplikasi), serta desktop, laptop, dan perangkat seluler. Kunci backup VM adalah memanfaatkan API hypervisor dan VSS; kunci backup NAS adalah memadukan kecepatan replikasi snapshot dengan keamanan salinan *off-site*; kunci backup endpoint adalah otonomi dan efisiensi bandwidth.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bedakan *standard backup* dan *bare-metal backup*.
2. Jelaskan tiga metode backup NAS beserta kelebihan/kekurangannya.
3. Apa perbedaan backup *crash-consistent* dan *application-consistent*, dan bagaimana VSS membantu?

**Analisis/HOTS (C4–C5):**
4. Mengapa memperlakukan VM sebagai mesin fisik menimbulkan masalah *noisy neighbor*? Bagaimana VADP mengatasinya?
5. Evaluasilah kapan sebuah laptop **tidak** perlu di-backup menurut buku sumber, dan kapan ia wajib di-backup.
6. Mengapa NDMP dapat mengunci organisasi ke satu vendor filer? Apa alternatif yang lebih portabel?

**Tugas Perancangan:**
7. Rancang strategi backup untuk pusat data kampus yang 100% tervirtualisasi (VMware) dengan beberapa NAS filer dan ratusan laptop dosen. Tentukan metode untuk VM, NAS, dan laptop, serta jelaskan alasannya.

---


## Bab 7 — Melindungi Basis Data

> *Menurut penulis sumber, ini kemungkinan bab terpenting dalam buku, karena darah-kehidupan (lifeblood) sebagian besar organisasi tersimpan dalam basis data, dan masalah backup/recovery tersulit dalam kariernya berkaitan dengan basis data.*

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) tiga model penyajian basis data: *traditional software*, *Platform-as-a-Service* (PaaS), dan *serverless*.
2. **Mengidentifikasi** (C1) berbagai model basis data (relational, key-value, document, dll.) dan model konsistensi (*immediate*, *eventual*, *hybrid*).
3. **Menjelaskan** (C2) terminologi basis data tradisional (*instance*, *tablespace*, *partition/shard*, *transaction log*, dll.).
4. **Menjelaskan** (C2) tiga tantangan inti backup basis data: *moving target*, *point-in-time*, dan *rolling forward*.
5. **Membandingkan** (C4) metode backup basis data tradisional: *cold*, *hot backup mode*, *split replica*, *snap-and-sweep*, *dump-and-sweep*, *stream-to-backup*, dan *transaction log backup*.
6. **Menjelaskan** (C2) backup PaaS/serverless dan langkah-langkah memulihkan basis data.

### Peta Konsep

```
MELINDUNGI BASIS DATA
│
├── MODEL PENYAJIAN: Traditional | PaaS | Serverless
├── MODEL BASIS DATA: Relational, Key-value, Time series,
│   Document, Graph, Search engine, Wide column
├── MODEL KONSISTENSI: Immediate | Eventual | Hybrid
├── TERMINOLOGI: instance, database, table, index, row,
│   attribute, data file, tablespace, partition/shard,
│   master file, transaction, transaction log
│
├── 3 TANTANGAN INTI: moving target, point-in-time, rolling forward
│
├── BACKUP TRADISIONAL: cold, split replica, hot backup mode,
│   snap-and-sweep, dump-and-sweep, stream-to-backup, txn log
├── BACKUP PaaS/SERVERLESS: dump-and-sweep, integrated BaaS
└── RECOVERY: identifikasi masalah → restore data files →
    apply media recovery → start database
```

### Materi Inti

Menurut db-engines.com, ada belasan tipe dan ratusan produk basis data, masing-masing dengan proses backup/recovery unik. Tujuan bab ini adalah memberi pemahaman cukup untuk mengevaluasi metodologi backup basis data Anda dan berbicara dengan DBA secara kredibel.

#### Model Penyajian Basis Data (*Delivery Models*)

| Model | Penjelasan | Tanggung Jawab Backup |
|---|---|---|
| **Traditional database software** | Anda membeli lisensi, mengunduh, dan memasang di server/VM yang Anda kelola. Anda bertanggung jawab atas segalanya. | Sepenuhnya milik Anda; banyak pilihan, sebagian tidak valid. |
| **Platform-as-a-Service (PaaS)** | Anda hanya melihat aplikasi; akses infrastruktur terbatas/nihil. Anda menentukan *apa* yang disediakan (mis. jumlah replika), penyediaan otomatis. Contoh: AWS RDS. | Biasanya disediakan mekanisme backup; ikuti dokumentasi. |
| **Serverless** | Bahkan tidak perlu menentukan penyediaan; Anda langsung memasukkan data. Contoh: AWS DynamoDB, Aurora Serverless. | Metode backup ditentukan vendor. |

> Analogi penulis: PaaS seperti transmisi otomatis vs *stick shift* — lebih sedikit kontrol, tetapi jauh lebih mudah.

#### Model Basis Data (*Database Models*)

Buku sumber membahas model paling populer:

| Model | Penjelasan & Contoh |
|---|---|
| **Relational (RDBMS)** | "Basis data orang tua kita" — tabel berskema, baris (*row*) dengan atribut, dikueri via SQL. Contoh: Oracle, SQL Server, DB2, MySQL, PostgreSQL. |
| **Key-value** | Skema sederhana kunci-nilai. NoSQL. Contoh: Redis, DynamoDB. |
| **Time series** | NoSQL untuk data berstempel-waktu. Contoh: Prometheus (banyak di Kubernetes). |
| **Document** | NoSQL untuk dokumen (sering JSON). Contoh: MongoDB. |
| **Graph** | Menggunakan struktur graf untuk kueri. Contoh: Neo4j, Amazon Neptune. |
| **Search engine** | NoSQL teroptimasi pencarian. Contoh: Elasticsearch, Splunk. |
| **Wide column** | NoSQL tanpa-skema dengan sangat banyak kolom. Contoh: Cassandra. |

#### Model Konsistensi (*Consistency Models*)

Penting untuk memutuskan cara backup/restore, terutama pada basis data multi-node:

| Model | Penjelasan |
|---|---|
| **Immediate (strong) consistency** | Semua pengguna melihat data sama pada saat yang sama. Umumnya RDBMS tradisional. Sedikit bug, tetapi membatasi performa multi-node. |
| **Eventual consistency** | Semua pembacaan *akhirnya* mengembalikan nilai sama (analogi: propagasi DNS). Umum pada basis data besar multi-node. |
| **Hybrid consistency** | Penulisan *eventually consistent*, tetapi dapat menentukan tingkat konsistensi per panggilan API pada pembacaan. Contoh: DynamoDB, MongoDB, Couchbase. |

> **Mengapa penting:** Anda harus mem-backup (atau dapat me-*restore*) data yang **konsisten**. Mem-backup node yang kedaluwarsa, atau node berbeda dari titik waktu berbeda, menimbulkan **masalah integritas referensial** (*referential integrity*). Untuk basis data multi-node *eventually consistent*, backup-lah semua node pada saat yang sama sebisa mungkin (mis. snapshot semua node serentak).

> **Peringatan dari sumber:** Fitur ketahanan (replikasi/sharding) hanya melindungi terhadap kegagalan **perangkat keras**. Bila DBA *drop* tabel penting atau penyerang menghapus basis data, replikasi hanya akan menyebarkan kerusakan itu dengan lebih efisien. *"This is why we back up databases, too."*

#### Terminologi Basis Data Tradisional

| Istilah | Penjelasan ringkas |
|---|---|
| **Instance** | Sekumpulan proses tempat basis data berkomunikasi melalui memori bersama; bisa menampung banyak basis data. |
| **Database** | Koleksi objek basis data. |
| **Table** | Pengelompokan informasi terkait (berskema pada RDBMS). |
| **Index** | Objek untuk pencarian khusus; sering dapat **dibangun ulang** dari tabel saat recovery. |
| **Row / Attribute** | Baris (record) / nilai tunggal dalam tabel. |
| **Data file** | Tempat data disimpan (*raw device* atau *cooked file*). |
| **Tablespace** | Koleksi satu/lebih *data file*; tempat tabel disisipkan. |
| **Partition / Shard** | Membagi tabel ke banyak *tablespace*/node. *Sharding* = menyebar ke banyak node. |
| **Master file** | Berkas yang melacak semua elemen instalasi (mis. *control file* Oracle, *Master Database* SQL Server). |
| **Transaction** | Aktivitas yang mengubah atribut (simple/complex; ditandai *begin/end transaction*). |
| **Transaction log** | Catatan tiap transaksi; untuk *rollback* setelah crash dan *roll forward* saat recovery (Oracle: *redo log*; MySQL: *binary log*; PostgreSQL: *Write Ahead Log*). |

#### Tiga Tantangan Inti Backup Basis Data Tradisional

1. **Moving target.** *Data file* terus berubah selama ada pembaruan; mem-backup-nya seperti berkas biasa menghasilkan backup tak berguna (inilah yang nyaris menamatkan karier penulis). Anda harus membuatnya "diam" atau backup via API-nya.
2. **Point-in-time.** Backup hanya dapat memulihkan ke titik waktu backup tersebut. Backup harian → RPO terbaik 24 jam tanpa bantuan log.
3. **Rolling forward (atau backward).** *Transaction log* dapat diputar ulang setelah restore *point-in-time* untuk memajukan basis data ke titik beberapa menit sebelum insiden, atau memutar balik transaksi yang tak lengkap.

#### Metode Backup Basis Data yang Disajikan Tradisional

| Metode | Penjelasan |
|---|---|
| **Cold backup** | Matikan *instance* lalu backup *data file* langsung. Paling aman, tetapi merepotkan operasional. |
| **Split replica** | (NoSQL) pastikan replika mutakhir, pisahkan dari konfigurasi, lalu backup replika (mirip cold backup tanpa mematikan basis data). |
| **Hot backup mode** | Tempatkan basis data dalam mode backup khusus (mis. Oracle `alter database begin backup`) sehingga *data file* dapat di-backup meski berubah. |
| **Snap-and-sweep** | Gunakan perintah snapshot dari basis data untuk menghasilkan snapshot konsisten, lalu *sweep* (backup) snapshot tersebut. Cocok untuk multi-node sharded; backup semua node serentak. |
| **Dump-and-sweep** | Jalankan *dump* basis data (mis. `mysqldump`, Oracle RMAN), lalu *sweep* hasilnya dengan backup filesystem. Paling populer; tidak butuh agen, tetapi bergantung pada *scripting* (rawan kesalahan penanganan error). |
| **Stream-to-backup product** | Pasang agen backup; backup di-*stream* langsung ke produk backup. Pelaporan error baik, tetapi DBA sering enggan memasang agen dan mungkin ada biaya tambahan. |
| **Transaction log backup** | Backup *transaction log* (bahkan beberapa kali sehari) untuk *media recovery*; opsinya sama dengan backup *data file*. Hati-hati dengan *truncating* log (hanya satu proses yang boleh mem-backup log). |
| **Master file** | Jika ada berkas pelacak (mis. *control file* Oracle), backup juga. |

> **Beware of Scripting (peringatan dari sumber):** Banyak metode (terutama *dump-and-sweep*) memerlukan *scripting* ekstensif. Penanganan error yang baik sering terlewat; backup bisa tampak berjalan padahal hanya bagian backup filesystem yang bekerja. *Scripting* populer, tetapi tidak tanpa risiko.

#### Backup PaaS dan Serverless

Tidak seperti SaaS besar, backup **disertakan** sebagai bagian paket pada PaaS/serverless, dan umumnya lebih mudah. Dua opsi:

- **Dump-and-sweep** — jarang menjadi satu-satunya opsi; PaaS kecil mungkin menyediakan *scheduler* dan tempat mengirim *dump file*.
- **Integrated Backup-as-a-Service** — vendor membuat *image copy* berkala (sering disebut "snapshot") yang otomatis disalin ke sistem penyimpanan terpisah. Mirip *snap-and-sweep* tetapi otomatis. Sering kali ini satu-satunya cara mem-backup basis data PaaS/serverless.

> **Catatan kepatuhan 3-2-1:** Tanyakan kepada vendor PaaS/serverless seberapa baik backup mematuhi aturan 3-2-1. Menyimpan backup di *object storage* pada **akun yang sama** tidak cukup — ingat kasus codespaces.com. Selalu **uji** backup, karena beberapa metode (terutama bagian *restore*) tidak berfungsi. Contoh: AWS RDS Oracle mendukung *backup* RMAN tetapi **tidak** mendukung *restore* RMAN.

**Catatan metode backup per produk (ringkasan dari sumber):** Oracle (RMAN, atau `begin/end backup`, atau VSS di Windows); SQL Server (`backup database`, atau VSS); DB2 (`backup database`, flag *snapshot*); MySQL (Enterprise Backup untuk InnoDB, `mysqldump` universal tetapi lambat); PostgreSQL (`pg_dump`; untuk RPO ketat aktifkan WAL + `pg_start_backup`/`pg_stop_backup`); MongoDB (Atlas: *continuous cloud backup* dgn PITR; `mongodump` untuk *deployment* kecil); Cassandra (`nodetool snapshot`, atau snapshot cloud seluruh klaster); DynamoDB (PITR otomatis); Neo4j (`neo4j-admin backup`, sebaiknya dari *read replica*).

#### Memulihkan Basis Data

Langkah-langkah tingkat tinggi memulihkan basis data tradisional:

1. **Identify what's wrong.** Identifikasi mengapa basis data tidak berjalan — kadang hanya *control file* yang rusak (recovery cepat), sehingga Anda tak perlu me-*restore* seluruh basis data 5 TB.
2. **Restore data files.** Pulihkan *data file* dari lokasi backup. (*Dump-and-sweep* mungkin memerlukan restore dua-fase: restore *dump file* dulu dari sistem backup, baru jalankan perintah restore basis data.)
3. **Apply media recovery.** Putar ulang *transaction log* terhadap basis data yang di-restore dari titik waktu lebih lama, untuk memajukannya ke titik sebelum insiden. Juga diperlukan setelah *hot backup*/*snap-and-sweep* untuk menyelaraskan semua *data file*.
4. **Start the database.** Jika semua langkah benar, basis data dapat dijalankan kembali.

Untuk basis data PaaS/serverless modern, recovery jauh lebih sederhana karena dikelola vendor (sering hanya memilih titik waktu).

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **RDBMS / SQL / NoSQL** | Sistem basis data relasional / bahasa kueri terstruktur / "not-only-SQL". |
| **Immediate / Eventual / Hybrid consistency** | Model konsistensi data. |
| **Referential integrity** | Integritas keterkaitan antar-data; rusak bila node di-restore ke titik waktu berbeda. |
| **Instance / Tablespace / Partition / Shard** | Terminologi struktur basis data tradisional. |
| **Transaction log (redo/binary log/WAL)** | Catatan transaksi untuk recovery. |
| **Moving target** | Tantangan: *data file* berubah selama di-backup. |
| **Cold / Hot backup mode** | Backup dengan basis data mati / dalam mode khusus saat hidup. |
| **Snap-and-sweep / Dump-and-sweep** | Metode backup via snapshot+sweep / dump+sweep. |
| **Stream-to-backup** | Backup di-stream langsung ke produk backup. |
| **Media recovery / Point-in-time recovery (PITR)** | Pemutaran ulang log untuk memajukan/menyelaraskan basis data. |
| **PaaS / Serverless database** | Basis data sebagai layanan dengan/tanpa penyediaan. |

### Studi Kasus

**Kasus — "The One That Got Away" (basis data *paris*).** Kisah pembuka buku: basis data Oracle *paris* gagal dipulihkan karena penulis tidak menyadari bahwa Oracle harus dimatikan (atau ditempatkan dalam *hot backup mode*) sebelum mem-backup *data file*-nya. Backup yang ada penuh kesalahan, dan salinan lama sudah ditimpa siklus rotasi enam minggu. Pelajaran: pahami bagaimana basis data Anda menjawab ketiga tantangan inti (*moving target*, *point-in-time*, *rolling forward*).

**Kasus — RDS Oracle: Backup Bisa, Restore Tidak.** AWS RDS Oracle mendukung *backup* RMAN tetapi tidak menyediakan fasilitas *restore* dari backup RMAN tersebut. Pelajaran (dan prinsip umum sumber): **selalu uji** metode backup PaaS, khususnya bagian *restore*-nya, karena keberadaan backup tidak menjamin keterpulihan.

**Kasus Konteks Indonesia — Basis Data Aplikasi Pembayaran Kampus.** Sebuah aplikasi pembayaran UKT menggunakan PostgreSQL. Untuk memenuhi RPO ketat di masa pembayaran, tim mengaktifkan *Write Ahead Log* (WAL) dan menggunakan `pg_start_backup`/`pg_stop_backup` di sekitar backup filesystem. Saat recovery, mereka me-restore filesystem lalu memutar ulang WAL untuk memajukan basis data hingga beberapa menit sebelum insiden — mencapai RPO ketat tanpa basis data mahal.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Pahami bagaimana basis data Anda menangani *moving target*, *point-in-time*, dan *rolling forward*.
- Backup *transaction log* secara berkala untuk RPO ketat.
- Untuk multi-node *eventually consistent*, snapshot semua node serentak.
- Selalu uji *restore*, bukan hanya *backup*.

**Kesalahan Umum:**
- Mem-backup *data file* basis data seperti berkas biasa (tanpa menanganinya sebagai *moving target*).
- Mengandalkan skrip *dump-and-sweep* tanpa penanganan error yang baik.
- Mengira ketahanan/replikasi cukup, padahal tidak melindungi dari *drop table*/penghapusan.
- Menyimpan satu-satunya backup PaaS di akun yang sama (melanggar 3-2-1).

### Rangkuman

Basis data sulit di-backup karena tiga tantangan inti: *data file* yang terus berubah (*moving target*), keterbatasan *point-in-time*, dan kebutuhan *rolling forward* via *transaction log*. Cara melindunginya bergantung pada **model penyajian**: basis data tradisional menawarkan banyak metode (*cold*, *hot backup mode*, *split replica*, *snap-and-sweep*, *dump-and-sweep*, *stream-to-backup*, plus *transaction log backup*), sedangkan PaaS/serverless umumnya menyertakan backup terintegrasi yang lebih sederhana. Model konsistensi menentukan strategi backup multi-node demi menjaga integritas referensial. Pemulihan mengikuti empat langkah: identifikasi masalah, restore *data file*, *apply media recovery*, lalu start basis data. Di atas segalanya: ketahanan bukan backup, dan backup harus selalu diuji restore-nya.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bedakan model penyajian *traditional*, PaaS, dan *serverless*.
2. Jelaskan tiga tantangan inti backup basis data tradisional.
3. Apa fungsi *transaction log* dalam recovery basis data?

**Analisis/HOTS (C4–C5):**
4. Bandingkan *dump-and-sweep* dan *stream-to-backup* dari sudut pandang kebutuhan *scripting*, pelaporan error, dan penerimaan DBA.
5. Mengapa model konsistensi memengaruhi cara backup basis data multi-node? Jelaskan risiko integritas referensial.
6. Evaluasilah kasus RDS Oracle (backup bisa, restore tidak). Prinsip umum apa yang dapat ditarik?

**Tugas Perancangan:**
7. Untuk sistem informasi rumah sakit dengan basis data PostgreSQL (transaksi padat) dan MongoDB (dokumen rekam medis), rancang strategi backup dan recovery yang memenuhi RPO ketat. Jelaskan metode per basis data dan bagaimana Anda mengujinya.

---


## Bab 8 — Sumber Data Modern

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) layanan cloud publik: IaaS, PaaS, *serverless*, dan SaaS, beserta tanggung jawab backup masing-masing.
2. **Menjelaskan** (C2) perbedaan *block storage* dan *object storage* di cloud serta implikasi proteksi datanya.
3. **Menganalisis** (C4) mengapa data SaaS (mis. Microsoft 365, Salesforce) tetap perlu di-backup meski "sangat tersedia".
4. **Menjelaskan** (C2) tantangan backup Docker/Kubernetes (Dockerfiles, images, etcd, persistent volumes, databases).
5. **Mengevaluasi** (C5) kebutuhan backup IoT dan *edge computing*.
6. **Merancang** (C6) keputusan backup berdasarkan kekritisan dan karakteristik sumber data.

### Peta Konsep

```
SUMBER DATA MODERN  ("Cloud bukan sihir; hanya komputer orang lain")
│
├── PUBLIC CLOUD
│     ├── IaaS (EC2/EBS): block vs object storage
│     ├── PaaS (RDS): integrated backup
│     ├── Serverless (DynamoDB): backup bawaan
│     └── SaaS (M365, Salesforce, Slack, GitHub): backup TIDAK termasuk
│           └── "You Need to Protect the Cloud"
│
├── HYBRID CLOUD (NFS/SMB gateway, cloud in a box)
│
├── DOCKER & KUBERNETES
│     ├── Dockerfiles & images (repository → backup)
│     ├── Kubernetes etcd (etcdctl snapshot save)
│     ├── Persistent volumes (CSI), Databases
│     └── K8s: jalur baru (application/namespace backup)
│
├── IoT / EDGE (sinkron ke pusat? simpan lokal?)
│
└── MEMBUAT KEPUTUSAN BACKUP
      ├── Criticality to the organization (RPO)
      └── Consider the source (bandwidth, cara restore, RTO)
```

### Materi Inti

Penulis menegaskan kembali: *"The cloud is not magic! There is no such thing as the cloud; there is only someone else's computer."* Cloud, SaaS, dan Kubernetes tidak mengubah aturan fundamental proteksi data dan kepemilikan data. Datanya milik Anda dan tanggung jawab Anda untuk mem-backup-nya — kecuali ada **secara tertulis** bahwa pihak lain melakukannya untuk Anda, dan bahkan itu pun harus Anda uji.

#### Public Cloud

**Infrastructure-as-a-Service (IaaS).** Contoh: AWS EC2 (compute) dan EBS (block storage). Tidak ada backup yang disediakan; Anda harus memulai dan mengelolanya. Dua pilihan: (a) pasang versi cloud dari produk backup dan backup VM seperti server fisik jarak-jauh (gunakan metode ramah-bandwidth karena ada *egress charges*); atau (b) — lebih umum — gunakan **alat bawaan vendor**.

Dua jenis penyimpanan di cloud:

| | Block storage (mis. EBS) | Object storage (mis. S3, Azure Blob, GCS) |
|---|---|---|
| **Sifat** | Satu LUN/RAID array di satu *datacenter*; tanpa redundansi inheren. | Datar (*flat*); objek diidentifikasi *hash* kontennya (UID). |
| **Redundansi** | Harus di-backup. | Umumnya direplikasi ke ≥3 lokasi; *self-healing*. |
| **Backup** | "EBS snapshot" = *image copy* penuh ke S3; incremental berikutnya hanya byte berubah; tanpa *egress charge*; bisa integrasi VSS. | Fitur proteksi bawaan (verifikasi *hash*, deteksi *bit rot*, opsi WORM). |
| **Penagihan** | Per kapasitas disediakan. | Per gigabyte tersimpan + *request pricing* (GET/PUT). |

> Karena fitur proteksi *object storage* memenuhi banyak syarat 3-2-1, banyak organisasi tidak mem-backup *object storage*. Namun, **lindungi** ia: cari *open buckets* (yang dapat dibaca siapa saja), aktifkan MFA, dan simpan backup penting di akun/region terpisah.

**Platform-as-a-Service (PaaS).** Mis. AWS RDS (MySQL, Oracle, dll.). Pelanggan menentukan konfigurasi, penyediaan otomatis. Backup terintegrasi (snapshot *application-consistent* disimpan ke S3). Sering ini satu-satunya cara backup. Tetap **lindungi** backup tersebut (lihat "You Need to Protect the Cloud").

**Serverless services.** Mis. AWS DynamoDB — cukup autentikasi dan simpan pasangan kunci-nilai; penskalaan otomatis. Sangat tahan, tetapi tetap perlu di-backup; biasanya tersedia konfigurasi backup berkala.

**Software-as-a-Service (SaaS).** Aplikasi siap-pakai (Microsoft 365, Google Workspace, Salesforce, Slack, GitHub). Ciri umum: tidak perlu infrastruktur, pembaruan otomatis, model *pay-as-you-go*, dan — yang krusial — **backup tidak termasuk**. Yang ada hanyalah fitur kenyamanan (mis. *recycle bin*, *versioning*) yang tidak mematuhi 3-2-1.

- **Salesforce (SFDC).** Layanan CRM, pada hakikatnya basis data khusus (istilah "object" = tabel). Sangat integral, tetapi banyak organisasi tidak mem-backup-nya. Layanan pemulihan resmi Salesforce dinilai penulis sebagai "layanan backup terburuk yang pernah saya lihat" (RTA enam hingga delapan minggu, proses restore sangat manual). Alat gratis tidak terotomatisasi. Penulis merekomendasikan alat komersial yang mem-backup secara otomatis.
- **Microsoft 365.** Rangkaian Exchange Online, SharePoint, OneDrive, Teams. Fitur seperti *Retention Policies* hanyalah fitur kenyamanan (seperti *recycle bin*) yang disimpan di sistem yang sama, dan hanya dapat diakses melalui sistem *e-discovery* — yang **tidak** sama dengan sistem *restore* (tidak memahami folder, struktur organisasi, atau *point-in-time*).

> **"You Need to Protect the Cloud":** Apa pun layanan cloud-nya, datanya tetap perlu dilindungi. Keluarkan backup dari akun & region asalnya.

#### Hybrid Cloud

- **NFS/SMB gateway** — jembatan antara penyimpanan on-premises dan cloud.
- **The cloud in a box** — perangkat lokal yang menyajikan layanan mirip-cloud.

#### Docker dan Kubernetes

Kontainer "merusak" backup dengan cara baru. Untuk memulihkan lingkungan Docker/Kubernetes, lindungi komponen-komponen berikut:

| Komponen | Cara melindungi |
|---|---|
| **Dockerfiles & YAML** | Simpan di repository ber-versi (mis. GitHub), lalu backup repository tersebut. Jika *image* berjalan tanpa Dockerfile, gunakan `docker image history` untuk membuatnya — tetapi hindari situasi ini. |
| **Docker images** | Simpan di registry (privat/Docker Hub/cloud) lalu backup. Jika tak punya image, buat via `docker commit`. |
| **Kubernetes etcd** | Basis data konfigurasi klaster (state + konfigurasi). Backup via `etcdctl snapshot save db` lalu simpan `snapshot.db` ke penyimpanan eksternal. |
| **Persistent volumes** | Tergantung jenis (volume tradisional, *bind mount*, NFS, *object*). Tantangan: data berubah → perlu *application-consistent*. **CSI** (*Container Storage Interface*, GA sejak K8s 1.13) menyederhanakan via snapshot PV, *clone*, bahkan injeksi agen backup. |
| **Databases** | Backup-lah dengan metode basis data yang tepat (Bab 7): matikan kontainer lalu backup direktori; atau jalankan perintah dump (mis. `mysqldump`) ke volume *bind-mount*; atau injeksi perintah *quiesce* di K8s untuk *snap-and-sweep*. |

> **Kubernetes: Jalur Baru.** Kubernetes memungkinkan melihat **seluruh aplikasi** di satu tempat, sehingga dapat mem-backup semua komponennya sekaligus. Dua pendekatan: **application-based** (menangkap pod, secrets, PVC, services sebagai satu backup aplikasi) dan **namespace-based** (menangkap segala isi *namespace*). Ini "jalur baru" yang menarik bagi proteksi data.

#### Internet of Things (IoT)

IoT adalah bagian dari *edge computing* — perangkat di tepi jejak data organisasi. Perangkat pengumpul data (mis. *smart meter*, sensor lalu lintas, kamera CCTV) menghasilkan data yang harus dilindungi; perangkat penampil tidak menciptakan data. Umumnya IoT mengirim data ke layanan cloud (tidak ada server fisik untuk dikhawatirkan), tetapi periksa apakah perangkat menyinkronkan data atau menyimpannya **lokal**. Penyimpanan lokal lebih problematik (perlu cara kreatif mem-backup ke lokasi terpusat, dengan dedup/identifikasi perubahan byte untuk mengurangi beban). Contoh "badai sempurna": sistem CCTV definisi tinggi yang datanya besar dan sulit direplikasi — solusi umumnya aktivasi-gerak (*motion activation*).

#### Membuat Keputusan Backup

| Pertimbangan | Penjelasan |
|---|---|
| **Criticality to the organization** | Seberapa mahal mengganti data ini? Bobotkan dataset berbeda; kaitkan dengan **RPO**. Pertimbangkan pula waktu — restore lambat punya biaya *downtime* tersendiri (kaitkan dengan **RTO**). |
| **Consider the source** | Pertimbangkan keunikan sumber: jenis VM (cloud vs hypervisor), bandwidth tersedia (kritis untuk laptop/remote/cloud), sifat perubahan data (basis data perlu penanganan khusus), dan **cara restore** (mis. laptop harus bisa di-restore dari luar kantor). |

> **Prinsip dari sumber:** Jika berargumen "haruskah ini di-backup?", ajukan dua pertanyaan: (1) Apakah data bernilai bagi organisasi? (2) Apakah sudah di-backup dengan cara yang mematuhi 3-2-1? Jika bernilai dan belum di-backup secara sah, maka harus di-backup.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **IaaS / PaaS / Serverless / SaaS** | Tingkatan layanan cloud. |
| **Egress charges** | Biaya lalu lintas keluar dari cloud (memengaruhi backup/restore). |
| **Object storage / Block storage** | Penyimpanan objek (UID berbasis hash, redundan) / blok (LUN, perlu di-backup). |
| **Open bucket** | *Bucket object storage* yang dapat dibaca siapa saja (risiko keamanan). |
| **Request pricing (GET/PUT)** | Penagihan per operasi I/O pada object storage. |
| **etcd** | Basis data konfigurasi/state klaster Kubernetes. |
| **CSI (Container Storage Interface)** | Antarmuka standar penyimpanan kontainer; mendukung snapshot PV. |
| **Persistent Volume (PV) / PVC** | Volume persisten / klaim volume di Kubernetes. |
| **Edge computing / IoT** | Komputasi di tepi / Internet of Things. |
| **Application/Namespace-based backup** | Pendekatan backup K8s berbasis aplikasi/namespace. |

### Studi Kasus

**Kasus — Microsoft 365 Tanpa Backup.** Sebuah organisasi mengira data Exchange Online, SharePoint, dan OneDrive mereka "sudah di-backup oleh Microsoft". Ketika sebuah akun dirusak dan strukturnya hilang, mereka mencoba memulihkan lewat *Retention Policies* — tetapi hanya bisa diakses melalui *e-discovery*, yang tidak memahami folder atau *point-in-time*. Hasilnya: tumpukan email/berkas dalam satu level, termasuk berkas yang sudah dihapus. Pelajaran: SaaS tetap perlu backup pihak ketiga yang mematuhi 3-2-1.

**Kasus — Kubernetes di Startup Lokal.** Sebuah *startup* fintech menjalankan aplikasi di Kubernetes dengan basis data dalam *persistent volume*. Awalnya mereka hanya mem-backup *image* tanpa etcd dan PV. Setelah memahami Bab 8, mereka menambahkan: backup repository Dockerfile/YAML di GitHub, `etcdctl snapshot save` untuk etcd, snapshot PV via CSI, dan backup basis data dengan metode yang tepat — lalu beralih ke *application-based backup* agar seluruh aplikasi terlindungi sekaligus.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Backup data SaaS dengan alat pihak ketiga yang mematuhi 3-2-1.
- Keluarkan backup cloud dari akun & region asalnya; aktifkan MFA; cari *open buckets*.
- Untuk K8s, lindungi Dockerfiles/YAML, etcd, PV, dan basis data; pertimbangkan *application-based backup*.

**Kesalahan Umum:**
- Mengira SaaS/cloud "sudah di-backup" tanpa bukti tertulis.
- Menyamakan *e-discovery* dengan *restore*.
- Hanya mem-backup *image* kontainer tanpa etcd dan *persistent volumes*.
- Mengabaikan data IoT yang tersimpan lokal di perangkat *edge*.

### Rangkuman

Sumber data modern — IaaS, PaaS, *serverless*, SaaS, Docker/Kubernetes, dan IoT — semuanya tetap memerlukan backup, karena "cloud bukan sihir". Di cloud, *object storage* relatif terlindungi (redundan, *self-healing*) sementara *block storage* harus di-backup; alat bawaan vendor umumnya menjadi cara utama. SaaS besar **tidak** menyertakan backup; fitur kenyamanan seperti *Retention Policies* bukan backup karena melanggar 3-2-1 dan hanya mendukung *e-discovery*. Kubernetes menuntut perlindungan Dockerfiles/YAML, etcd, *persistent volumes*, dan basis data — sekaligus menawarkan "jalur baru" *application/namespace-based backup*. IoT memerlukan perhatian khusus bila data tersimpan lokal. Keputusan backup didasarkan pada **kekritisan** (RPO/RTO) dan **karakteristik sumber** (bandwidth, cara restore).

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bedakan IaaS, PaaS, *serverless*, dan SaaS dari sisi tanggung jawab backup.
2. Jelaskan perbedaan *block storage* dan *object storage* di cloud serta implikasinya.
3. Sebutkan komponen Kubernetes yang perlu di-backup dan caranya.

**Analisis/HOTS (C4–C5):**
4. Mengapa data SaaS tetap perlu di-backup meski "sangat tersedia"? Mengapa *e-discovery* bukan pengganti *restore*?
5. Evaluasilah kapan data IoT mudah dilindungi dan kapan menjadi "badai sempurna".
6. Bagaimana *criticality* dan *consider the source* memandu keputusan backup? Berikan contoh trade-off.

**Tugas Perancangan:**
7. Sebuah organisasi menggunakan Microsoft 365, AWS (EC2+RDS), dan Kubernetes. Rancang keputusan backup untuk setiap beban kerja, jelaskan bagaimana Anda memastikan kepatuhan 3-2-1, dan identifikasi sumber data yang paling kritis.

---


## BAGIAN III — Metode Perangkat Lunak dan Pemulihan Bencana

### Pengantar Bagian III

Setelah memahami fondasi konseptual (Bagian I) serta teknologi penyimpanan dan sumber data (Bagian II), Bagian III membahas **metode** yang digunakan perangkat lunak untuk melakukan backup, archive, dan pemulihan bencana. Fokusnya adalah *metode*, bukan produk — sebuah daftar tentang berbagai hal yang dapat dilakukan produk, sehingga Anda dapat memahami pilihan sebelum mengevaluasi solusi komersial pada Bagian IV.

Tiga bab dalam bagian ini:

- **Bab 9** memetakan seluruh metode perangkat lunak backup/recovery menjadi dua kelompok besar berdasarkan cara restore: metode yang mendukung **traditional restore** (multiplexing, full+incremental, *file-level/block-level incremental forever*, *source dedupe*) dan metode yang mendukung **instant recovery** (replikasi, CDP, snapshot, near-CDP, CDM).
- **Bab 10** menyelami **archive** secara lebih dalam: perbedaan *retrieval* vs *restore*, tipe-tipe sistem archive (*batch*, *real-time*, *HSM-style*), dan cara memutuskan kebutuhan archive.
- **Bab 11** membahas **disaster recovery** — yang menjadi "paramount" akibat ransomware: apa yang ada dalam rencana DR, membangun *recovery site* (cold/warm/hot), mekanisme pemulihan (replikasi data primer vs replikasi backup), pilihan perangkat lunak vs layanan (DRaaS), dan penyusunan *DR runbook*.

> **Prinsip Pemandu Bagian III:** "Restore adalah satu-satunya yang penting." Maka metode-metode dikelompokkan berdasarkan kemampuan restore-nya, dan keseluruhan rencana DR dinilai berdasarkan **RTA** — waktu pemulihan aktual.

---

## Bab 9 — Metode Perangkat Lunak Backup dan Recovery

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) metode yang mendukung *traditional restore* dan yang mendukung *instant recovery*.
2. **Menjelaskan** (C2) *multiplexing* dan masalah *shoe-shining* terbalik yang ditimbulkannya saat restore.
3. **Membandingkan** (C4) metode *traditional restore*: full+incremental, *file-level incremental forever*, *block-level incremental forever*, dan *source dedupe*.
4. **Menjelaskan** (C2) metode *instant recovery*: replikasi (sync/async), CDP, snapshot (CoW/RoW/hold-writes), near-CDP, dan CDM.
5. **Mengevaluasi** (C5) mengapa replikasi atau snapshot **sendirian** bukan backup yang sah.
6. **Menilai** (C5) pemanfaatan backup untuk tujuan lain (*leveraging backups*).

### Peta Konsep

```
METODE PERANGKAT LUNAK BACKUP/RECOVERY (dikelompokkan per cara RESTORE)
│
├── MENDUKUNG TRADITIONAL RESTORE (perlu menyalin saat restore)
│     ├── Multiplexing (cepat saat backup, lambat saat restore)
│     ├── Full + Incremental tradisional (+ synthetic full)
│     ├── File-level incremental forever
│     ├── Block-level incremental forever (CBT)
│     └── Source deduplication (paling hemat)
│
├── MENDUKUNG INSTANT RECOVERY (siap pakai saat restore dimulai)
│     ├── Replication (sync/async/hybrid) — bukan backup sendirian
│     ├── CDP (async + change log; titik pemulihan tak terbatas)
│     ├── Snapshots (CoW/RoW/hold-writes) — bukan backup sendirian
│     ├── Near-CDP (snapshot + replikasi = backup sah)
│     └── Copy Data Management (CDM)
│
└── LEVERAGING BACKUPS (e-discovery, kepatuhan, deteksi ransomware,
    CDM untuk test/dev, analitik) + MEMILIH METODE
```

### Materi Inti

Penulis mendefinisikan *backup* secara luas: **apa pun yang merupakan salinan data, disimpan terpisah dari aslinya, yang dapat digunakan untuk memulihkan sistem asli bila rusak.** Dengan definisi ini, replikasi, snapshot, dan CDP pun masuk pertimbangan — meski beberapa di antaranya **bukan** backup sah bila berdiri sendiri. Janji penulis: apa pun yang ia sebut "backup" dalam bab ini mematuhi aturan 3-2-1.

Seluruh metode dibagi berdasarkan **cara restore**: yang memerlukan *traditional restore* (menyalin data setelah restore dimulai) dan yang mendukung *instant recovery* (sistem segera tersedia saat restore dimulai).

#### Metode yang Mendukung Traditional Restore

**Multiplexing.** Bukan gaya backup, melainkan teknik menulis ke tape yang mengatasi *speed mismatch* (tape ingin cepat; backup, terutama incremental, lambat). *Multiplexing* menjalin (*interleave*) banyak backup menjadi satu aliran besar yang cepat. Masalahnya: saat restore, sistem membaca semua aliran dan membuang sebagian besar — bila menjalin 36 backup, kecepatan restore ≈1/36 kecepatan drive. Ini "*shoe-shining* terbalik". (Satu vendor mengatasinya dengan ukuran *chunk* besar.)

**Full dan Incremental Tradisional.** Dimulai *full* lalu rangkaian *incremental*/*cumulative incremental*, lalu *full* lagi. Populer dan teruji, tetapi boros: *full* berulang membuang energi, dan restore harus memulihkan *full* lalu tiap *incremental* berurutan (banyak data ditimpa berkali-kali). *Synthetic full* (lihat Bab 4) membantu mengurangi pergerakan data.

**File-Level Incremental Forever.** Hanya satu *full* (sintetis atau tidak), lalu *incremental* selamanya. Keputusan backup pada **level berkas** (seluruh berkas di-backup bila berubah). Lebih efisien dari full+incremental; tahu persis versi berkas mana yang perlu di-restore. Tidak cocok dengan tape.

**Block-Level Incremental Forever.** Keputusan pada **level blok** via **CBT** (mis. dari hypervisor). Sangat mengurangi data yang ditransfer dari klien — berguna untuk sistem jarak-jauh. Hanya bekerja dengan disk sebagai target (akses acak).

**Source Deduplication.** Tipe *incremental forever* yang tidak pernah mem-backup *chunk* yang sudah pernah dilihat sistem — bahkan lebih hemat dari *block-level incremental*. Paling efektif untuk laptop, kantor cabang, dan VM cloud. Kelemahan: mungkin perlu mengganti perangkat lunak backup.

> **Tabel perbandingan metode traditional restore (peringkat 1=terbaik, dari sumber):**

| Metode | Bandwidth | Storage | Ramah VM/cloud | Tape/Disk |
|---|---|---|---|---|
| Traditional full+incremental | 4 | 4 | 4 | Keduanya |
| File-level incremental forever | 3 | 3 | 3 | Keduanya |
| Block-level incremental forever | 2 | 2 | 2 | Keduanya |
| Source deduplication | 1 | 1 | 1 | Disk |

#### Metode yang Mendukung Instant Recovery

**Replikasi.** Menyalin perubahan dari *volume* sumber ke *volume* target (umumnya level blok). Dua jenis:

- **Synchronous** — perubahan direplikasi **sebelum** ACK ke aplikasi; sumber & target selalu 100% sinkron. Cocok untuk *hot site*, tetapi latensi dapat tinggi (kasus pasca-9/11: replikasi sinkron 300 mil dibatalkan karena ~9 ms per *round trip*). *"Kesalahan operator dan korupsi data juga 100% tersinkron."* (Dan Frith)
- **Asynchronous** — antrian perubahan direplikasi sesuai bandwidth; target dapat tertinggal (menentukan RPA). Dapat *write coalescing* bila terlalu tertinggal.
- **Hybrid** — penulis menganggap "sinkron" itu biner; bila boleh tertinggal, itu bukan sinkron.

> **Keterbatasan replikasi:** Tidak ada "tombol mundur" — kesalahan/korupsi ikut direplikasi. Replikasi **sendirian** melanggar 3-2-1 (hanya satu versi; tidak ada "3"). *"It's missing the 3!"*

**Continuous Data Protection (CDP).** Pada hakikatnya **replikasi asinkron + change log** (tombol mundur). Dapat me-restore ke *sekarang* atau jam/hari lalu, hampir instan. Menggabungkan DR dan backup dalam satu sistem dengan **titik pemulihan tak terbatas**. Dua tipe: yang menjaga *image* siap-pakai, dan yang menyajikan *volume* virtual dari titik waktu mana pun. Kelemahan: sangat mahal dalam I/O, CPU, memori, jaringan, penyimpanan, dan harga perangkat lunak.

**Snapshots.** Salinan virtual yang bergantung pada *volume* primer. Tiga cara menangani perubahan blok:

| Metode | Penjelasan |
|---|---|
| **Copy-on-write (CoW)** | Menyalin blok lama ke area khusus sebelum ditimpa. Paling umum; performa menurun seiring banyaknya snapshot. |
| **Redirect-on-write (RoW)** | Menulis blok baru di lokasi lain dan mengalihkan *pointer*. Bisa banyak snapshot tanpa penalti performa (mis. NetApp). |
| **Hold all writes** | (VMware) menahan semua tulisan ke volume asli hingga snapshot dilepas, lalu memutarnya ulang. Jangan disimpan lama. |

> Snapshot **sendirian** bukan backup: bergantung pada volume sumber (melanggar "2" dan "1" dalam 3-2-1). Namun snapshot adalah **sumber yang sangat baik** untuk backup (mis. VSS).

**Near-Continuous Data Protection (Near-CDP).** Kombinasi **snapshot + replikasi** — sebuah sistem proteksi data yang **sah**. Umumnya: ambil snapshot volume primer, lalu replikasikan. Dengan mereplikasi ke sistem on-site lalu off-site, Anda mematuhi 3-2-1. Penulis mengakui ia yang mencetuskan istilah ini; near-CDP memberi titik pemulihan sesering tiap detik/menit. Kelemahan: sering mengikat ke satu vendor (risiko *rolling bug*), bisa lebih mahal, dan integrasi aplikasi sering kurang baik.

**Copy Data Management (CDM).** Mirip near-CDP tetapi bertujuan menyediakan salinan untuk **banyak keperluan** (backup, test/dev, analitik) sambil meminimalkan penyimpanan. Menggunakan *data split* (replikasi asinkron) + log untuk menyajikan volume di titik waktu mana pun. Fokus pada penurunan biaya penyimpanan dan peningkatan pemanfaatan salinan, bukan sekadar DR berperforma tinggi.

> **Tabel perbandingan produk instant-recovery (ringkasan dari sumber):**

| Metode | Pulih korupsi logis | Pulih kegagalan sistem/disk | Direkomendasikan utk backup/DR | RTA | RPA | Biaya |
|---|---|---|---|---|---|---|
| Replication saja | Tidak | Ya | Tidak | 0 | 0 | Tinggi |
| Snapshots saja | Ya | Tidak | Tidak | Menit* | Menit* | Sedang |
| CDP | Ya | Ya | Ya | 0 | 0 | Sangat tinggi |
| Near-CDP | Ya | Ya | Ya | Menit | Menit | Sedang |
| CDM | Ya | Ya | Tergantung | Menit | Menit | Sedang |

(*jika tanpa kegagalan perangkat keras)

> **Peringatan:** Jangan gunakan replikasi atau snapshot **saja** untuk backup/DR — replikasi saja tak bisa pulih dari korupsi logis (virus), dan snapshot saja tak bisa pulih dari kegagalan perangkat keras.

#### Memanfaatkan Backup untuk Lebih (*Leveraging Backups*)

Karena backup kini umumnya di disk (akses acak), data backup dapat dimanfaatkan untuk: **e-discovery**, **pemeriksaan kepatuhan** (mis. mendeteksi data sensitif yang salah tempat), **deteksi ransomware** (mis. *machine learning* mendeteksi lonjakan jumlah berkas pada incremental), **CDM untuk test/dev**, dan **analitik historis**. Penulis menyambut ide ini selama sistem backup tetap terlindungi — tetapi mengingatkan agar tidak membuat sistem backup yang "dapat digunakan ulang" tetapi buruk dalam backup/restore itu sendiri.

#### Memutuskan Metode Backup

Tidak ada metode sempurna; setiap metode punya kelebihan dan kekurangan. Pertanyaan kunci: **Apakah yang Anda miliki sekarang sudah memenuhi kebutuhan?** Dapatkah memenuhi RTO/RPO dalam anggaran? Sering kali masalahnya bukan perangkat lunak/keras, melainkan **konfigurasi** (*wetware*). Bila ingin instant recovery, pilihan baik adalah CDP, near-CDP, CDM, atau produk modern lain. Pastikan RTO nol benar-benar dibutuhkan — tidak ada salahnya RTA delapan jam bila RTO 24 jam.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Traditional restore / Instant recovery** | Restore menyalin data / sistem segera tersedia. |
| **Multiplexing** | Menjalin banyak backup menjadi satu aliran cepat (memperlambat restore). |
| **(File/Block)-level incremental forever** | Incremental selamanya pada level berkas/blok. |
| **Replication (sync/async/hybrid)** | Replikasi data; sinkron menjamin 100% sama, asinkron dapat tertinggal. |
| **Write coalescing** | Menggabungkan beberapa tulisan saat replikasi tertinggal jauh. |
| **CDP / Near-CDP** | *Continuous* / *Near-Continuous Data Protection*. |
| **Snapshot (CoW/RoW/hold-writes)** | Salinan virtual; tiga cara menangani perubahan blok. |
| **CDM (Copy Data Management)** | Pengelolaan salinan data untuk banyak keperluan. |
| **Change log** | Log perubahan (tombol mundur) pada CDP. |
| **Leveraging backups** | Memanfaatkan backup untuk e-discovery, kepatuhan, deteksi ransomware, dll. |

### Studi Kasus

**Kasus — Mengapa Replikasi Saja Tidak Cukup.** Sebuah bank lokal mereplikasi basis data inti secara sinkron ke situs DR untuk pemulihan cepat. Suatu hari, DBA tanpa sengaja men-*drop* tabel penting. Karena replikasi tidak memiliki "tombol mundur", kesalahan itu langsung tereplikasi ke situs DR. Pelajaran: replikasi melanggar "3" dalam 3-2-1; gabungkan dengan sistem yang dapat mundur (mis. CDP atau near-CDP).

**Kasus — Near-CDP untuk Virtualisasi.** Sebuah perusahaan menggunakan appliance HCI dengan proteksi data berbasis near-CDP: snapshot VM (dengan VSS) lalu replikasi ke lokasi lain. Ini memberi titik pemulihan tiap jam, pemulihan instan, penghematan penyimpanan ala *block-level incremental*, dan kepatuhan 3-2-1 — selama satu salinan berada off-site.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Pilih metode berdasarkan kebutuhan restore (traditional vs instant) dan RTO/RPO nyata.
- Gunakan near-CDP (snapshot+replikasi) bila menginginkan instant recovery yang patuh 3-2-1.
- Periksa apakah masalah sesungguhnya adalah konfigurasi (*wetware*), bukan produk.

**Kesalahan Umum:**
- Menggunakan replikasi atau snapshot **saja** sebagai backup/DR.
- Mengejar RTO nol (CDP mahal) padahal RTO organisasi jauh lebih longgar.
- Menjala *multiplexing* terlalu tinggi sehingga restore sangat lambat.

### Rangkuman

Metode perangkat lunak backup/recovery dikelompokkan berdasarkan cara restore. Metode **traditional restore** (full+incremental, *file/block-level incremental forever*, *source dedupe*) menyalin data setelah restore dimulai; *source dedupe* paling hemat tetapi mungkin menuntut penggantian perangkat lunak. Metode **instant recovery** (replikasi, CDP, snapshot, near-CDP, CDM) membuat sistem segera tersedia — tetapi replikasi atau snapshot **sendirian bukan backup sah** (melanggar 3-2-1). Near-CDP (snapshot+replikasi) adalah sistem proteksi data sah dengan titik pemulihan rapat. Backup modern juga dapat dimanfaatkan untuk e-discovery, kepatuhan, deteksi ransomware, dan analitik. Pilih metode berdasarkan kebutuhan nyata, bukan sekadar "rumput tetangga lebih hijau".

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bedakan *traditional restore* dan *instant recovery*.
2. Jelaskan tiga cara snapshot menangani perubahan blok (CoW, RoW, hold-writes).
3. Apa perbedaan replikasi sinkron dan asinkron?

**Analisis/HOTS (C4–C5):**
4. Mengapa replikasi **dan** snapshot, jika berdiri sendiri, bukan backup yang sah? Kaitkan dengan 3-2-1.
5. Mengapa CDP disebut "menggabungkan DR dan backup", dan apa harga yang harus dibayar?
6. Evaluasilah klaim "kami butuh CDP dengan RTO nol" untuk sebuah organisasi dengan RTO 24 jam.

**Tugas Perancangan:**
7. Untuk aplikasi e-commerce kritis (RTO/RPO sangat ketat) dan sistem pelaporan internal (RTO/RPO longgar), pilih metode yang berbeda untuk masing-masing. Jelaskan trade-off dan bagaimana setiap pilihan mematuhi 3-2-1.

---


## Bab 10 — Metode Perangkat Lunak Archive

> *Bab ini dalam buku sumber ditulis oleh Dan Frith (@penguinpunk), seorang veteran industri dari Australia.*

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) hakikat archive sebagai "salinan primer dari data sekunder".
2. **Membedakan** (C2) *retrieval* (dari archive) dan *restore* (dari backup).
3. **Membandingkan** (C4) tiga tipe sistem archive: *traditional batch*, *real-time*, dan *HSM-style*.
4. **Mengevaluasi** (C5) apakah sebuah organisasi membutuhkan sistem archive.
5. **Menganalisis** (C4) persyaratan archive: format data, media penyimpanan, portabilitas, metadata, dan *immutability*.

### Peta Konsep

```
METODE PERANGKAT LUNAK ARCHIVE
│
├── HAKIKAT: archive = salinan PRIMER dari data SEKUNDER
│     (backup = salinan sekunder dari data primer)
│
├── RETRIEVAL vs RESTORE
│     ├── Restore: 1 berkas, 1 titik waktu, 1 sistem (butuh nama+tanggal)
│     └── Retrieval: banyak data, rentang tanggal lebar, berbasis konten
│
├── TIPE SISTEM ARCHIVE
│     ├── Traditional batch (pakai → arsip → hapus dari sumber)
│     ├── Real-time (salin saat dibuat; untuk audit/kepatuhan)
│     └── HSM-style (pindah ke storage lebih murah seiring usia; stub)
│
└── MEMUTUSKAN SISTEM ARCHIVE
      ├── Apakah perlu? (jenis data, retensi, kepatuhan)
      └── Persyaratan: format, media, portabilitas, metadata,
          immutability, terpisah/terintegrasi
```

### Materi Inti

Archive adalah "sistem proteksi data yang kemungkinan Anda butuhkan tetapi kemungkinan besar tidak Anda miliki". Sebagaimana didefinisikan di Bab 3, archive adalah salinan terpisah yang berfungsi sebagai **referensi**, disimpan dengan metadata yang cukup untuk ditemukan tanpa mengetahui asalnya. Frith menambahkan definisi yang elegan:

> *Backup = salinan **sekunder** dari data **primer**. Archive = salinan **primer** dari data **sekunder**.*

Data archive umumnya tidak lagi mutakhir, jarang diakses, atau tidak lagi bernilai tinggi bagi penciptanya — tetapi perlu disimpan demi alasan **legislatif dan kepatuhan**. Mengapa tidak dihapus saja? Karena banyak regulasi mewajibkan penyimpanan (mis. firma akuntansi menyimpan data klien beberapa tahun untuk audit; lembaga pemerintah/keuangan menyimpan catatan interaksi publik bertahun-tahun). Frith pernah bekerja di organisasi pemerintah yang menyimpan berkas kasus "seumur hidup klien plus 99 tahun".

Menyimpan archive pada sistem lebih murah tidak berarti risiko kehilangan lebih besar; *trade-off*-nya biasanya **kecepatan**. Sistem archive biasanya lambat dalam *retrieval* dan throughput, dan sering dilindungi via replikasi (bukan backup tradisional), karena melindungi repositori archive yang besar secara harian menjadi tantangan tersendiri. Karena itu banyak solusi memakai banyak salinan di banyak lokasi.

#### Retrieval versus Restore

| | Restore (dari backup) | Retrieval (dari archive) |
|---|---|---|
| **Informasi dibutuhkan** | Nama server, direktori, berkas, tabel, **dan tanggal** tunggal. | Tidak mengasumsikan informasi itu; hanya perkiraan kapan dibuat, mungkin siapa, dan gambaran konten. |
| **Lingkup** | Satu berkas, satu titik waktu, satu sistem. | Banyak berkas/email, rentang tanggal lebar, lintas banyak server. |
| **Contoh** | "Pulihkan `/home/curtis/resume.doc` dari server *elvis* tanggal 1 September." | "Semua berkas/email berisi kata 'wowza' yang dibuat/dikirim/diterima dalam tiga tahun terakhir." |

#### Tipe Sistem Archive

| Tipe | Penjelasan | Kasus Penggunaan |
|---|---|---|
| **Traditional batch archive** | Data dipakai sementara, lalu diarsipkan ke tempat aman, lalu **dihapus** dari lokasi asal. Diberi metadata (nama proyek, alat, pengguna, periode) untuk *retrieval* kelak. | Firma konstruksi mengarsipkan data tender yang gagal; produsen satelit mengarsipkan desain model satelit. |
| **Real-time archive** | Saat data dibuat/disimpan di produksi, salinan otomatis dibuat untuk archive. Diakses via portal pencarian granular, bukan klien email biasa. | Audit/kepatuhan; *journal mailbox* email; Microsoft 365 *Retention Policies*, Google Archive. |
| **HSM-style archive** | *Hierarchical Storage Management*: seiring usia/jarang-akses, data dipindah ke storage lebih murah (object storage, cold storage, tape), meninggalkan *stub*/pointer atau mengandalkan mesin pencari. | Mengurangi beban storage produksi (mis. memindahkan email tua/besar ke archive). |

> **"Isn't That Backup?"** Frith menegaskan kembali: *Microsoft 365 Retention Policies* dan *Google Workspace Archive* adalah **archive**, bukan backup. Keduanya tidak menyimpan citra *point-in-time*, tidak dapat memulihkan kotak surat ke keadaan kemarin, dan tidak mematuhi 3-2-1. Mereka bisa *retrieval*, tetapi buruk untuk *restore*.

#### Memutuskan Sistem Archive

**Apakah Anda membutuhkannya?** Pertimbangkan jenis data (terstruktur vs tidak terstruktur — data tak terstruktur lebih cocok diarsipkan), apakah data tumbuh pesat di volume jaringan besar, apakah data dihasilkan pengguna atau mesin (data log/monitoring mesin tumbuh pesat, jarang dilihat manusia → kandidat baik archive), serta **kebutuhan retensi**. Sering kali organisasi tidak memahami persyaratan retensinya dan berkata "simpan semuanya selamanya" — yang akhirnya membengkakkan storage. Libatkan tim legal & kepatuhan (gunakan proses Bab 2).

**Persyaratan archive:**

| Persyaratan | Penjelasan |
|---|---|
| **Format data** | Akankah data terbaca di masa depan? Berkas teks-biasa relatif aman; format aplikasi proprietary (mis. AbiWord, Access) berisiko. |
| **Media penyimpanan** | Hindari media yang akan sulit dibaca (Iomega Jaz, DDS lama, *punch card*). Pilih sistem yang mendukung **portabilitas data**. |
| **Portabilitas & sustainability** | Archive berbasis perangkat lunak memungkinkan memindahkan data antar-platform; idealnya juga mendukung fitur perangkat keras (enkripsi, dedup) bila tersedia. |
| **Human-readable vs aplikasi** | Apakah data perlu dibaca manusia atau cukup dipahami aplikasi modern? Pertimbangkan ekspor ke format terbuka atau virtualisasi sistem lama. |
| **Metadata akurat** | Metadata (waktu dibuat, diakses, oleh siapa) harus dipertahankan saat transfer; penting untuk konteks dan pencarian. |
| **Immutability** | Untuk bukti pengadilan, data tidak boleh berubah; *immutability* memberi keamanan terhadap perusakan/ransomware. |
| **Akses & pencarian** | Sediakan *frontend* aplikasi (bila human-readable) atau alat pencarian + tagging metadata yang andal. |
| **Terpisah atau terintegrasi** | Pertimbangkan *storage sprawl* dan kepatuhan legislatif. Sistem archive boleh terpisah dari backup (tim pengelola pun bisa berbeda, mis. di unit *records management*/kepatuhan). |

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Archive** | Salinan primer dari data sekunder; untuk referensi/retrieval. |
| **Retrieval** | Pengambilan banyak data berbasis konten/metadata dari rentang tanggal lebar. |
| **Traditional batch archive** | Arsipkan lalu hapus dari sumber, diberi metadata proyek. |
| **Real-time archive** | Salinan otomatis saat data dibuat; untuk audit/kepatuhan. |
| **HSM (Hierarchical Storage Management)** | Memindahkan data ke storage lebih murah seiring usia; meninggalkan *stub*. |
| **Stub** | Penanda/pointer yang ditinggalkan di sistem sumber untuk *retrieval*. |
| **Full-text search** | Pencarian berdasarkan konten, bukan sekadar metadata. |
| **Storage sprawl** | Pertumbuhan storage tak terkendali. |
| **Data portability** | Kemampuan memindahkan data antar-platform. |

### Studi Kasus

**Kasus — Firma Konstruksi.** Sebuah firma membentuk tim ad-hoc untuk menggarap tender (jembatan, gedung). Bila tender gagal, tim dibubarkan dan datanya dipindah ke sistem archive sebagai referensi proyek lain — bukan disimpan permanen di storage produksi yang mahal. *Traditional batch archive* menjaga pertumbuhan storage produksi tetap terkendali.

**Kasus — Email HSM.** Pada awal abad ini, server email banyak organisasi kelebihan beban akibat lampiran besar. Karena semua email diarsipkan otomatis (*real-time archive*), admin dapat menentukan email lebih tua dari *n* hari dan lebih besar dari *n* megabyte dipindah ke archive dan dihapus dari sistem primer (*HSM-style*) — mengurangi beban storage primer.

**Kasus Konteks Indonesia — Arsip Rekam Medis.** Sebuah rumah sakit wajib menyimpan rekam medis bertahun-tahun sesuai regulasi. Menggunakan sistem **backup** untuk ini akan mahal dan buruk saat *retrieval*. Solusi sesuai bab ini: sistem **archive** (kemungkinan *HSM-style* + media tahan lama seperti tape) dengan metadata dan *immutability* agar rekam medis dapat dicari, terjaga keasliannya, dan memenuhi kepatuhan.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Bedakan kebutuhan *retrieval* (archive) dari *restore* (backup); pilih sistem yang sesuai.
- Pilih sistem archive yang mendukung **portabilitas data** dan **metadata** akurat.
- Libatkan tim legal & kepatuhan dalam menetapkan retensi.

**Kesalahan Umum:**
- Menggunakan produk backup sebagai archive (dan sebaliknya).
- Menyimpan archive pada media yang akan sulit dibaca di masa depan.
- "Simpan semuanya selamanya" tanpa memahami kebutuhan retensi nyata.

### Rangkuman

Archive adalah salinan primer dari data sekunder, dibuat untuk *retrieval* (bukan *restore*) demi referensi dan kepatuhan. *Retrieval* berbeda mendasar dari *restore*: ia mengambil banyak data berbasis konten dari rentang tanggal lebar tanpa mengetahui nama server/berkas. Tiga tipe sistem archive — *traditional batch*, *real-time*, dan *HSM-style* — melayani kebutuhan berbeda. Keputusan mengadopsi archive bergantung pada jenis data, kebutuhan retensi, dan kepatuhan; persyaratan utamanya meliputi format data, media, portabilitas, metadata, *immutability*, dan akses/pencarian. Fitur archive bawaan SaaS bukanlah backup.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Jelaskan definisi Frith: "backup = salinan sekunder data primer; archive = salinan primer data sekunder".
2. Bedakan *retrieval* dan *restore* dengan contoh.
3. Jelaskan tiga tipe sistem archive.

**Analisis/HOTS (C4–C5):**
4. Mengapa data log/monitoring mesin menjadi kandidat baik untuk archive?
5. Evaluasilah risiko format data proprietary dan media usang dalam archive jangka panjang.
6. Mengapa *Microsoft 365 Retention Policies* disebut archive, bukan backup?

**Tugas Perancangan:**
7. Rancang sistem archive untuk arsip akademik universitas (skripsi, tesis, dataset riset) yang harus disimpan puluhan tahun. Tentukan tipe archive, media, strategi metadata/portabilitas, dan kebutuhan *immutability*.

---


## Bab 11 — Metode Disaster Recovery

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) mengapa ransomware menjadikan disaster recovery (DR) sebagai prioritas utama.
2. **Mengidentifikasi** (C1) komponen rencana DR dan membedakannya dari *business continuity planning* (BCP).
3. **Mengevaluasi** (C5) mengapa "sekotak tape" dan "appliance dedup tereplikasi" bukan rencana DR yang memadai.
4. **Membandingkan** (C4) opsi *recovery site*: *roll your own*, *recovery-site-as-a-service*, dan public cloud, serta konfigurasi *cold/warm/hot site*.
5. **Membandingkan** (C4) mekanisme pemulihan: replikasi data primer vs replikasi backup, serta *conversion* vs *transformation*.
6. **Menyusun** (C6) struktur *DR runbook*.

### Peta Konsep

```
METODE DISASTER RECOVERY  ("It's all about the RTA")
│
├── RANSOMWARE MENGUBAH SEGALANYA (jangan bayar tebusan)
├── BUKAN DR PLAN: sekotak tape | appliance dedup tereplikasi
├── DR vs BCP (BCP lebih luas: fasilitas, SDM, dll.)
│
├── MEMBANGUN RECOVERY SITE
│     ├── Roll your own | Recovery-site-as-a-service | Public cloud
│     └── Cold / Warm / Hot site
│
├── MEKANISME PEMULIHAN
│     ├── Replikasi data primer (array/host/storage-virtualization)
│     ├── Replikasi backup (butuh dedup; perlu pre-restore)
│     └── Platform format: conversion (lambat) vs transformation (cepat)
│
├── SOFTWARE atau SERVICE (DR software vs DRaaS)
└── DR RUNBOOK (overview, inventory, kontak, prosedur, eskalasi)
```

### Materi Inti

Selama bertahun-tahun, "rencana DR" banyak organisasi hanyalah sekotak tape di vendor penyimpanan luar lokasi — yang sebenarnya bukan rencana sama sekali. Kini DR menjadi **paramount** karena satu hal: **ransomware**.

#### Ransomware Mengubah Segalanya

Tidak memiliki rencana DR yang bekerja sangat cepat menjadikan Anda target empuk ransomware. Berbeda dengan bencana alam (yang menghancurkan fisik dan mengundang simpati), korban ransomware dihadapkan pada pilihan menggiurkan: **membayar tebusan**. Setiap hari *downtime* berbiaya, dan organisasi tertekan membayar karena dianggap "tombol mudah".

> **"Please Do Not Pay the Ransom" (penegasan dari sumber):** Membayar tebusan adalah ide buruk. Ia membuat ransomware makin menarik bagi pelaku, merusak reputasi merek, berpotensi melanggar regulasi (mis. GDPR), dan tidak menjamin pemulihan (Anda berurusan dengan kriminal). Satu-satunya jawaban sahih: rencana DR dengan RTA pendek.

#### DR versus Business Continuity Planning (BCP)

**BCP** adalah proses yang jauh lebih luas untuk memastikan organisasi tetap berjalan setelah peristiwa besar — mencakup manajemen fasilitas, personel, kantor sementara, dan jalur komunikasi. DR adalah **bagian** dari BCP yang berfokus pada membawa data dan sistem kembali daring. Buku sumber berfokus pada DR (membawa data/sistem kembali daring), bukan BCP secara keseluruhan. Contoh BCP yang diuji nyata: pandemi COVID-19 (organisasi beradaptasi bekerja dari rumah).

#### Apa yang Ada dalam Rencana DR?

Rencana DR mengasumsikan Anda memulai dari nol. Pertanyaan yang harus terjawab:

- Dari mana sumber daya komputasi/penyimpanan/jaringan diperoleh?
- Bagaimana melindungi lingkungan pengganti (yang menjadi produksi baru)?
- Apa kebutuhan pemulihan (RPO/RTO; apakah RTA/RPA sanggup)?
- Apa prioritas dan prasyarat pemulihan?
- Siapa yang menjalankan (dan rencana bila orang itu tak tersedia — "garis suksesi")?
- Seberapa baik dokumentasinya (DR runbook)?
- Seberapa banyak yang **terotomatisasi**? (Otomasi adalah kunci.)
- Sudahkah **diuji**?

> **Studi Kasus dari sumber — "You Can Run, but You Can't Hide":** Karena dokumentasi yang buruk, penulis dilacak dan ditelepon ke rumah sakit saat anaknya lahir, hanya karena tim tidak membaca dokumentasi yang sudah ada. Pelajaran: dokumentasi yang baik (dan pelatihan menggunakannya) membebaskan Anda.

**Yang BUKAN rencana DR:**

- **Sekotak tape.** Tape buruk untuk DR karena DR menuntut puluhan/ratusan *restore single-threaded* serentak; setiap server butuh drive sendiri, dan *multiplexing* membuat restore lambat.
- **Appliance dedup tereplikasi saja.** Lebih baik dari sekotak tape, tetapi masalahnya tetap pada **restore** itu sendiri. Memulai *full restore* setelah bencana menghasilkan RTA yang tak dapat diterima — sehingga organisasi tertekan membayar tebusan.

> **"It's All About the RTA":** Satu-satunya cara memenuhi RTO/RPO yang cukup pendek untuk mengabaikan ransomware adalah bila **restore sudah selesai sebelum dibutuhkan**. Analogi penulis: *"The time to take Dramamine is too late to take Dramamine."* Saat Anda perlu mulai restore, sudah terlambat untuk mulai.

#### Membangun Recovery Site

> *Recovery site* adalah tempat fisik/virtual yang menggantikan lingkungan komputasi Anda bila bencana terjadi.

| Opsi | Penjelasan |
|---|---|
| **Roll your own** | Bangun & pelihara *datacenter* terpisah sendiri (rencana "OG"). Sangat mahal (≈menggandakan biaya komputasi). Sebagian menekan biaya dengan peralatan lama (berisiko kapasitas kurang). |
| **Recovery-site-as-a-service** | Bayar perusahaan untuk menyediakan & memelihara perangkat keras. Bisa dedikasi (mahal, risiko rendah) atau berbagi (lebih murah, tetapi berisiko "*run on the bank*" saat bencana regional). |
| **Public cloud** | "Lahir untuk DR." Kapasitas berlebih sehingga tak ada "*run on the bank*"; biaya nyaris nol hingga deklarasi bencana. Bisa pilih region berbeda untuk menghindari bencana regional. |

> **Public Cloud Was Born for DR:** Anda hanya membayar penyimpanan salinan data saat tidak bencana; ribuan VM baru dibayar **hanya saat dibutuhkan**. *Snapshot* di cloud dapat menyimpan data tereplikasi dengan separuh harga penyimpanan primer; restore beberapa menit dan paralel di semua VM.

**Cold, Warm, dan Hot Site:**

| Site | Penjelasan | RTA/RPA |
|---|---|---|
| **Cold site** | Peralatan tersedia tetapi belum di-restore; restore dimulai saat bencana. | Paling lambat; paling murah. |
| **Warm site** | Mayoritas mutakhir tetapi dimatikan hingga dibutuhkan; mungkin tertinggal beberapa jam/hari. | Seimbang biaya & kecepatan (paling umum). |
| **Hot site** | Menyala penuh dan tersinkron; *failover* dalam hitungan detik. | RTA/RPA mendekati nol; paling mahal (perlu replikasi sinkron). |

Pilihan bergantung pada RTO/RPO. RTO/RPO nol → hanya *hot site*. Mayoritas organisasi (RTO/RPO dalam hitungan jam) menemukan *warm site* sebagai keseimbangan terbaik, terutama bila perangkat lunak/layanan dapat melakukan *incremental restore* pasca-bencana untuk memperbarui situs.

#### Mekanisme Pemulihan

Sistem DR modern mengandalkan penyalinan elektronik melalui salah satu dari dua metode:

**1. Replikasi data primer.** Mereplikasi setiap perubahan dari dataset primer ke dataset pemulihan (umumnya level storage). Metode:

| Metode | Penjelasan |
|---|---|
| **Array-based** | Satu array mereplikasi ke array lain. Paling umum, andal, tetapi mahal (vendor sama; tak bisa tawar-menawar). |
| **Host-based** | Replikasi di dalam host; fleksibel (campur vendor storage). |
| **Storage virtualization** | Perangkat keras di antara server & storage; fleksibel campur vendor, tetapi dukungan dari vendor host/storage terbatas. |

**2. Replikasi backup.** Membutuhkan **deduplikasi** (tanpa dedup, data terlalu besar untuk direplikasi). Masalahnya: backup harus di-*restore* untuk berguna. Karena DR modern menuntut pemulihan **sudah dilakukan di muka**, replikasi backup memerlukan proses **pre-restore** otomatis berkala (mis. *incremental restore* tiap pagi ke *image* di recovery site).

**Isu format platform (*conversion* vs *transformation*).** Bila format disk hypervisor sumber ≠ hyperscaler tujuan, perlu disesuaikan:

| Pendekatan | Penjelasan | Dampak RTA |
|---|---|---|
| **Conversion** | Seluruh *image* VM dijalankan melalui alat konversi (mis. AWS Import Tool). Andal tetapi **lambat** (uji penulis: 100 GB ≈4 jam; 1 TB bisa 24–48 jam). | Sangat besar. |
| **Transformation** | Vendor proteksi data mengubah berkas **di tempat** (membungkus, menyisipkan driver) tanpa memipa seluruh disk. **Cepat** (beberapa menit per disk, terlepas ukuran). | Kecil. |

> Konsekuensinya pada RTA/RPA besar. Dengan *conversion*, Anda terpaksa memilih antara RPA pendek (konversi backup terbaru, RTA panjang) atau RTA pendek (gunakan backup yang sudah dikonversi, tetapi RPA panjang).

#### Software atau Service

| Pilihan | Keunggulan | Kelemahan |
|---|---|---|
| **Commercial DR software** | **Kontrol** penuh atas server, keamanan, firewall, akun. | **Kontrol** = tanggung jawab penuh keamanan/patch; **biaya** (overprovisioning). Banyak serangan ransomware sukses karena patch tidak dipasang. |
| **DR-as-a-Service (DRaaS)** | Infrastruktur dikelola vendor; Anda cukup memasang agen. Semua keuntungan SaaS. | **Kehilangan kontrol**; Anda mungkin masih mengelola recovery site (kecuali public cloud). |

> Pada DRaaS sejati, Anda tidak pernah *login* sebagai administrator pada server/storage apa pun. Bila Anda masih *login* sebagai superuser, itu sekadar perangkat lunak berlangganan, bukan DRaaS.

#### DR Runbook

*DR runbook* adalah instruksi rencana DR yang harus cukup terdokumentasi agar orang teknis yang tidak familier pun dapat menjalankannya tanpa bantuan. Strukturnya:

- **Runbook goals** & **overview**
- **Technology inventory** (inventaris teknologi)
- **Contact information** (informasi kontak)
- **Procedures** (prosedur langkah demi langkah)
- **Exception processing with escalation** (penanganan pengecualian dengan eskalasi)

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Disaster Recovery (DR)** | Pemulihan saat sebagian besar lingkungan komputasi tidak beroperasi. |
| **Business Continuity Planning (BCP)** | Perencanaan keberlangsungan bisnis (lebih luas dari DR). |
| **RTA / RPA** | Waktu/titik pemulihan aktual — fokus utama DR. |
| **Recovery site** | Tempat pengganti lingkungan komputasi saat bencana. |
| **Cold / Warm / Hot site** | Tingkat kesiapan situs pemulihan. |
| **Run on the bank** | Kelangkaan sumber daya berbagi saat banyak organisasi membutuhkannya serentak. |
| **Array/Host-based replication** | Replikasi berbasis array/host. |
| **Conversion / Transformation** | Penyesuaian format disk: lambat (pipa seluruh image) / cepat (di tempat). |
| **DRaaS** | *Disaster-Recovery-as-a-Service*. |
| **DR runbook** | Dokumentasi prosedur pemulihan bencana. |

### Studi Kasus

**Kasus — DR Berbasis Cloud dengan Transformation.** Sebuah perusahaan mem-backup tiap jam dan melakukan *incremental update* ke *image* pemulihan di cloud. Dengan proses **transformation** (≈15 menit), saat bencana pukul 05.30, konfigurasi pulih sebelum pukul 07.00 — RTA ≈30 menit, RPA hanya beberapa menit. Bandingkan dengan **conversion** (4 jam): perusahaan terpaksa memilih antara RPA pendek (RTA ≈4,5 jam) atau RTA pendek (RPA ≈5 jam). Pelajaran: pilihan teknologi penyesuaian format sangat memengaruhi RTA/RPA.

**Kasus Konteks Indonesia — DR Lintas-Region untuk Pemda.** Sebuah pemerintah daerah di zona rawan gempa membangun DR berbasis public cloud di region berbeda. Saat tidak bencana, mereka hanya membayar penyimpanan salinan data; ribuan VM baru dibayar hanya saat deklarasi bencana. Region yang dipilih berada di luar zona seismik yang sama, sehingga aman dari bencana regional yang menimpa lokasi utama.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Rancang DR agar restore **sudah selesai** sebelum dibutuhkan (warm/hot site).
- Otomatiskan dan **uji** rencana DR secara rutin; pelihara *runbook*.
- Pertimbangkan public cloud untuk DR (skalabilitas & pemisahan geografis).
- Pilih solusi dengan *transformation* (bukan *conversion*) bila RTA penting.

**Kesalahan Umum:**
- Menganggap sekotak tape atau appliance dedup tereplikasi sebagai rencana DR.
- Membayar tebusan ransomware.
- Tidak menguji rencana DR sehingga RTA/RPA nyata tidak diketahui.
- Menempatkan *hot site* terlalu dekat dengan lokasi utama.

### Rangkuman

Disaster recovery menjadi prioritas utama karena ransomware — dan satu-satunya jawaban sahih adalah rencana DR dengan **RTA** pendek (jangan membayar tebusan). DR adalah bagian dari BCP yang lebih luas. Sekotak tape maupun appliance dedup tereplikasi-saja bukan rencana DR memadai, karena masalahnya pada restore yang lambat. Kunci sukses: pemulihan sudah dilakukan di muka (*warm*/*hot site*), idealnya di public cloud. Mekanisme pemulihan dapat berupa replikasi data primer atau replikasi backup (dengan dedup dan *pre-restore*); penyesuaian format platform sebaiknya via *transformation* yang cepat, bukan *conversion* yang lambat. Pilih antara perangkat lunak DR (kontrol penuh, tanggung jawab penuh) dan DRaaS (dikelola vendor). Akhirnya, *DR runbook* yang terdokumentasi, terotomatisasi, dan teruji adalah penentu keberhasilan.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Mengapa ransomware menjadikan DR sebagai prioritas utama?
2. Bedakan DR dan BCP.
3. Jelaskan perbedaan *cold*, *warm*, dan *hot site*.

**Analisis/HOTS (C4–C5):**
4. Mengapa "sekotak tape" dan "appliance dedup tereplikasi saja" bukan rencana DR memadai?
5. Bandingkan *conversion* dan *transformation* serta dampaknya pada RTA/RPA.
6. Evaluasilah argumen "jangan bayar tebusan" dari sudut pandang biaya jangka pendek vs kerusakan jangka panjang.

**Tugas Perancangan:**
7. Susun kerangka *DR runbook* dan rancang strategi DR berbasis public cloud (pilih cold/warm/hot site) untuk sebuah perusahaan logistik dengan RTO 4 jam dan RPO 1 jam. Jelaskan mekanisme pemulihan dan bagaimana Anda akan mengujinya.

---


## BAGIAN IV — Target Penyimpanan dan Solusi Komersial

### Pengantar Bagian IV

Bagian terakhir ini menutup buku dengan pembahasan praktis tentang **perangkat keras target** tempat backup/archive disimpan, **tantangan** sistem proteksi data komersial, kategori-kategori **solusi** (tradisional dan modern), serta panduan **mengganti atau meng-upgrade** sistem backup.

Lima bab dalam bagian ini:

- **Bab 12** membahas seluruh target proteksi data: tape, media optik, *disk array*, *object storage*, *target deduplication appliances* (VTL, NAS), dan *public cloud storage* — termasuk cara memilih dan menyetel performanya.
- **Bab 13** memaparkan sejarah singkat backup dan **tantangan** sistem komersial (sizing, pemeliharaan, multi-vendor, sistem terpisah untuk DR/e-discovery, isu tape/disk, pembelian modal besar, sulit diskalakan, sulit berganti produk).
- **Bab 14** membahas **solusi tradisional** (*traditional backup* dan *target dedupe appliances*) beserta keunggulan, tantangan, dan analisisnya.
- **Bab 15** membahas **solusi modern** (*virtualization-centric*, *hyper-converged backup appliances*/HCBA, *Data-Protection-as-a-Service*/DPaaS, *managed service providers*/MSP) dan bagaimana pasar beradaptasi.
- **Bab 16** memberikan panduan **mengganti/meng-upgrade** sistem: solusi mana yang tepat, pembagian tanggung jawab, pertimbangan TCO, dan kriteria memilih (showstoppers, *ease of use*, *scalability*, *future proofing*).

> **Catatan dari penulis sumber (Bab 14–16):** Penulis sengaja **tidak menyebut nama produk**. Ia membahas *kategori* solusi agar dapat berterus terang tentang kelebihan/kekurangan tanpa risiko hukum, dan agar buku tetap relevan lintas waktu. Buku ajar ini mengikuti pendekatan yang sama.

---

## Bab 12 — Target Proteksi Data

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mengevaluasi** (C5) keunggulan dan kelemahan tape: biaya, keandalan menulis (UBER), dan penyimpanan jangka panjang vs ketidakcocokan kecepatan.
2. **Menjelaskan** (C2) konsep *shoe-shining*, *repositioning*, dan *multiplexing* pada tape.
3. **Membandingkan** (C4) target: tape, optik, *disk array*, *object storage*, *target dedupe appliances* (VTL/NAS), dan *cloud storage* (block vs object).
4. **Menerapkan** (C3) prinsip penyetelan performa (*performance-tuning*) tape, RAID, dan *target dedupe*.
5. **Memilih** (C5) target backup yang sesuai dengan kebutuhan dan kendala.

### Peta Konsep

```
TARGET PROTEKSI DATA
│
├── TAPE
│     ├── Bagus: biaya, keandalan menulis (UBER), retensi jangka panjang
│     ├── Buruk: incremental kecil → shoe-shining/repositioning
│     └── Teknologi: LTO, IBM TS11x0, LTFS, robotic library
│
├── OPTIK (DVD/Blu-ray) — kapasitas kecil, lambat, UBER rendah
├── INDIVIDUAL DISK DRIVES (jarang; melanggar 3-2-1 bila menetap)
├── STANDARD DISK ARRAYS
├── OBJECT STORAGE (S3 sbg protokol & layanan; mungkin dominan kelak)
├── TARGET DEDUPE APPLIANCES (VTL vs NAS)
├── PUBLIC CLOUD STORAGE (cloud out, on-prem SW di cloud, cloud native)
│
└── MEMILIH & MENGGUNAKAN TARGET
      ├── Optimalkan yang ada (tuning tape/RAID/dedupe)
      └── Pilih perangkat lebih sesuai (software dulu, baru target)
```

### Materi Inti

Kini ada lebih banyak target proteksi data daripada sebelumnya. Bab ini memberi informasi yang tidak memihak agar Anda dapat memutuskan sendiri.

#### Tape Drives

Tape adalah perangkat proteksi data tertua yang masih dipakai. Tape lebih murah di hampir semua kasus, namun mayoritas industri tak lagi memakainya sebagai target **awal** backup. Mengapa?

**Apa yang tape kuasai (tiga hal):**

| Keunggulan | Penjelasan |
|---|---|
| **Biaya** | Jauh lebih murah dari *deduplicated disk*. Media dapat dipisah dari perangkat perekam (tidak mungkin pada disk). Konsumsi daya & pendinginan sangat rendah — tape di slot tidak memakai daya. "Bahkan jika disk gratis, ia tetap lebih mahal" setelah memperhitungkan daya & pendinginan. |
| **Keandalan menulis** | Diukur dengan **UBER** (*Uncorrected Bit Error Rate*). LTO-8 ber-UBER 10⁻¹⁹; SATA disk 10⁻¹⁴ — tape **10.000×** lebih baik dalam menulis bit. Tape mungkin tak memberi data (bila rusak), tetapi tidak akan memberi data yang **salah**; disk bisa. |
| **Retensi jangka panjang** | Tape dapat menyimpan data andal hingga **30 tahun**; disk yang menyala hanya ~5 tahun (akibat *bit rot*). Ditentukan ukuran *magnetic grain* dan suhu media (rumus KuV/kT). |

Tabel UBER (dari sumber):

| Media | UBER |
|---|---|
| Optical | 10⁻⁸ – 10⁻¹² (umumnya 10⁻¹⁰) |
| SATA Disk | 10⁻¹⁴ |
| Enterprise Disk | 10⁻¹⁵ |
| Enterprise SSD | 10⁻¹⁶ |
| LTO-8 | 10⁻¹⁹ |
| IBM TS1160 | 10⁻²⁰ |

**Apa yang tape buruk:** menulis **incremental kecil** (sedikit data sepanjang waktu). Untuk menulis andal, kepala perekam butuh rasio sinyal-ke-derau tinggi → tape harus bergerak cepat (LTO-8 ≈20 kaki/detik). LTO-8 penuh menuntut aliran masuk ≈750 MB/s, sedangkan incremental sering hanya beberapa MB/s. Bila aliran terlalu lambat, *buffer* kosong dan drive harus **repositioning** (berhenti, mundur, maju lagi — 3–6 detik). Drive yang terus melakukannya disebut **shoe-shining** (seperti menyemir sepatu). *"Your tape drive is not slow; your backup is slow."*

> **Studi Kasus dari sumber — "You Don't Need More Tape Drives!":** Stasiun TV memakai 18 tape drive untuk mem-backup ~20 TB dan masih gagal. Penulis mematikan 12 drive, mengaktifkan *inline copy* (asli + salinan serentak), mengubah seleksi ke semua *filesystem* lokal, dan menyetel *multiplexing*. Hasil: backup turun dari 24 jam ke 8 jam, dengan dua salinan, memakai 1/3 tape — sambil menemukan datacenter sebenarnya 30 TB (10 TB sebelumnya tak ter-backup). Inti: cocokkan kecepatan aliran dengan kecepatan tape.

**Teknologi tape:** **LTO** (dominan; LTO-8: 12 TB native/30 TB terkompresi, 300 MB/s native), **IBM TS11x0** (UBER 10⁻²⁰, lebih cepat), **LTFS** (*Linear Tape File System* — tape di-*mount* seperti *filesystem*; format independen-produk, ideal untuk archive), dan **robotic tape libraries** (kini terutama untuk archive jangka panjang; pelanggan terbesarnya justru perusahaan cloud besar).

#### Target Lainnya

| Target | Penjelasan |
|---|---|
| **Optical media (DVD/Blu-ray)** | Kapasitas kecil (Blu-ray 25/50 GB), lambat (*phase change* lambat), UBER rendah. Jarang dipakai untuk proteksi data; sebagian untuk arsip jangka panjang. |
| **Individual disk drives** | Jarang di datacenter besar. Disk kedua tak-dapat-dilepas sebagai target **melanggar 3-2-1** (tepat di sebelah aslinya). Ada disk lepasan untuk transportasi. |
| **Standard disk arrays** | Array disk standar sebagai target. |
| **Object storage** | Diidentifikasi *hash* konten; **S3** menjadi protokol de-facto (Azure Blob & GCS mendukungnya). Fleksibel (ganti penyedia cukup ganti tujuan). Penulis menduga *object storage* akan menjadi target dominan kelak. |
| **Target dedupe appliances (VTL)** | *Virtual Tape Library* — server berpura-pura jadi tape library di atas disk. Cepat (Fibre Channel), mudah integrasi dengan produk yang hanya tahu tape, tetapi mewarisi keterbatasan akses-serial. Kini kurang populer. |
| **Target dedupe appliances (NAS)** | Di-*mount* via NFS/SMB; lebih mudah dibagikan. DBA dapat backup langsung (dump-and-sweep). **Risiko keamanan:** backup terlihat sebagai direktori (mis. `C:\BACKUPS`) yang rentan ransomware — gunakan protokol proprietary yang menyembunyikan direktori. |
| **Public cloud storage** | *Cloud out* (salin backup ke S3 sebagai pengganti Iron Mountain), *on-prem software in cloud VMs* (butuh *filesystem*/block), atau *cloud native* (object storage sebagai target utama). |

#### Memilih dan Menggunakan Target

**Optimalkan yang sudah ada dulu** (misconfiguration adalah penyebab kegagalan backup tersering):

- **Tuning tape** — ketahui kecepatan minimum drive; cocokkan aliran masuk (≥ kecepatan minimum). Idealnya, jangan backup langsung ke tape; letakkan *disk cache* (lebih baik: *deduplicated disk array*) di depan tape.

> **Studi Kasus dari sumber — "Two Tons of Fertilizer in a One-Ton Truck":** Sepuluh drive LTO-2 (masing-masing 80 MB/s, min ≈25 MB/s) di belakang satu server dengan koneksi jaringan **100 Mb** (≈12 MB/s). 12 MB/s dibagi 10 drive = 1,2 MB/s/drive → *shoe-shining* parah → throughput total ≈5 MB/s. Penulis menyarankan upgrade jaringan dan mematikan 9 dari 10 drive — throughput langsung berlipat. *"Sistem dua kali lebih cepat dengan 1/10 sumber daya."*

- **Tuning RAID** — pertimbangkan dampak level RAID pada performa tulis (penalti paritas).
- **Tuning target dedupe** — jangan *full backup* hanya demi rasio dedup lebih baik; selidiki protokol koneksi tercepat (NFS/SMB/iSCSI/proprietary).

**Pilih perangkat yang lebih sesuai:** Pilih **perangkat lunak/layanan backup dulu**, baru target — agar tidak membeli target yang ternyata tidak dibutuhkan. **Pilih yang cocok untuk Anda** (hormati kendala anggaran & preferensi). Untuk *on-premises disk*, uji performa nyata (mis. kecepatan baca bisa 10× lebih lambat dari tulis), uji skenario kegagalan disk, *garbage collection*, backup+restore serentak, dan — bila berencana *instant recovery* — uji dengan banyak VM. Untuk *cloud disk*, pahami block vs object: block ≈2× lebih mahal tetapi cocok untuk pembacaan berkas besar *single-threaded*; object lebih murah, *self-healing*, tiga salinan, tetapi ada *request pricing* (GET/PUT) dan kurang optimal untuk restore berkas besar (kecuali perangkat lunak dirancang ulang untuk object).

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **UBER** | *Uncorrected Bit Error Rate* — laju kesalahan bit tak-terkoreksi. |
| **Bit rot** | Degradasi data magnetik seiring waktu. |
| **Shoe-shining / Repositioning** | Tape bolak-balik karena aliran data terlalu lambat. |
| **Signal-to-noise ratio** | Rasio sinyal-ke-derau; tinggi diperlukan untuk tulis andal. |
| **LTO / TS11x0** | Teknologi tape utama. |
| **LTFS** | *Linear Tape File System* — tape sebagai filesystem, format independen-produk. |
| **VTL (Virtual Tape Library)** | Disk yang berpura-pura jadi tape library. |
| **Object storage / Block storage** | Target cloud: objek (hash, redundan) / blok (LUN). |
| **Request pricing (GET/PUT)** | Biaya per operasi I/O object storage. |
| **Garbage collection** | Proses penghapusan backup lama pada sistem dedup. |

### Studi Kasus

**Kasus — Tape untuk Archive, Bukan Backup.** Sebuah perusahaan media menyimpan film pada tape LTO sebagai archive jangka panjang (memanfaatkan keandalan menulis & retensi 30 tahun), sekaligus mempertimbangkan Blu-ray karena anggapan lebih mudah dibaca 50 tahun lagi. Untuk backup harian, mereka memakai *deduplicated disk* (akses acak, cocok dengan incremental). Pelajaran: gunakan tape sesuai kekuatannya (archive), bukan kelemahannya (incremental kecil).

**Kasus Konteks Indonesia — Pulau dengan Internet Terbatas.** Sebuah organisasi dengan *datacenter* di pulau berinternet buruk tidak dapat mengandalkan backup berbasis cloud. Mereka menggunakan disk on-premises yang direplikasi ke array off-premises, lalu disalin ke tape dan dikirim ke penyimpanan luar lokasi. Saat badai menghancurkan pulau itu, **tape-lah satu-satunya yang tersisa**. Pelajaran: tape belum mati; ia tetap relevan dalam konteks tertentu.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Gunakan tape untuk **archive jangka panjang**, bukan target awal backup.
- Letakkan *disk cache*/*deduplicated disk* di depan tape untuk mencocokkan kecepatan.
- Pilih perangkat lunak backup **sebelum** membeli target; uji performa nyata.
- Untuk target dedupe NAS, sembunyikan direktori backup dari OS (anti-ransomware).

**Kesalahan Umum:**
- Menambah tape drive untuk mengatasi backup lambat (justru memperburuk *shoe-shining*).
- Backup langsung ke tape dengan incremental kecil.
- Menjadikan disk kedua tak-dapat-dilepas sebagai target (melanggar 3-2-1).
- Memilih object storage cloud semata karena murah tanpa mempertimbangkan *request pricing* & performa restore.

### Rangkuman

Tape unggul dalam **biaya**, **keandalan menulis** (UBER jauh lebih baik dari disk), dan **retensi jangka panjang** (30 tahun vs 5 tahun disk), tetapi buruk untuk **incremental kecil** akibat *shoe-shining* — sehingga kini ideal untuk **archive**, bukan target awal backup. Target lain meliputi optik (kapasitas kecil, lambat), *disk array*, *object storage* (kemungkinan dominan kelak), *target dedupe appliances* (VTL kalah populer dari NAS), dan *public cloud storage* (cloud out, on-prem-in-cloud, cloud native). Dalam memilih: optimalkan dulu yang ada (misconfiguration adalah penyebab kegagalan tersering), pilih perangkat lunak sebelum target, dan uji performa nyata di lingkungan Anda.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Sebutkan tiga hal yang dikuasai tape dan jelaskan masing-masing.
2. Apa itu *shoe-shining* dan mengapa terjadi?
3. Bedakan target dedupe VTL dan NAS.

**Analisis/HOTS (C4–C5):**
4. Mengapa "menambah tape drive" sering memperburuk performa backup? Gunakan kasus stasiun TV.
5. Evaluasilah kapan *object storage* cloud lebih unggul dan kapan *block storage* lebih sesuai sebagai target.
6. Mengapa tape disebut "ideal untuk archive, bukan backup"? Kaitkan dengan UBER dan ketidakcocokan kecepatan.

**Tugas Perancangan:**
7. Rancang pilihan target backup untuk organisasi dengan backup harian besar dan kebutuhan archive 10 tahun. Tentukan target untuk backup operasional dan untuk archive, serta jelaskan strategi penyetelan performa.

---


## Bab 13 — Tantangan Proteksi Data Komersial

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menceritakan** (C2) sejarah singkat backup dan bagaimana perangkat lunak komersial merevolusi proteksi data.
2. **Menerapkan** (C3) proses *sizing* sistem backup: ukuran *full*, laju perubahan, RTO/RPO, retensi, *backup window*, dan pertumbuhan.
3. **Menghitung** (C3) kebutuhan throughput dan kapasitas sistem backup.
4. **Mengidentifikasi** (C1) tantangan sistem backup komersial: pemeliharaan OS/perangkat lunak, multi-vendor, sistem terpisah untuk DR/e-discovery, isu tape/disk, pembelian modal besar, *overprovisioning*, dan kesulitan skala.
5. **Menganalisis** (C4) kesulitan berganti produk backup.

### Peta Konsep

```
TANTANGAN PROTEKSI DATA KOMERSIAL
│
├── SEJARAH SINGKAT (shell script & cron → produk komersial → tape library)
│
├── TANTANGAN:
│     ├── Sizing (full size, change rate, RTO/RPO, retensi, window, growth)
│     ├── Maintain backup server OS (target empuk; harus paling aman)
│     ├── Maintain backup software (upgrade = menakutkan)
│     ├── Manage multiple vendors (4-6 vendor)
│     ├── Sistem terpisah untuk DR & e-discovery
│     ├── Tape & disk related challenges (air gap)
│     ├── Pembelian modal besar & overprovisioning
│     └── Sulit diskalakan (indeks backup membengkak)
│
└── SULIT BERGANTI PRODUK (let them expire | use a service | restore+backup)
```

### Materi Inti

#### Sejarah Singkat Backup

Untuk memahami pentingnya perangkat lunak backup komersial, lihatlah masa sebelumnya. Pada 1993, penulis bekerja di bank bernilai $35 miliar dengan ratusan server Unix, semuanya di-backup oleh segelintir **shell script** dan **cron job** ke tape drive internal tiap server (`dump`, `tar`, `cpio`). Tidak ada konfigurasi, penjadwalan, pemantauan, atau pelaporan terpusat — harus login ke tiap server. Skripnya berasumsi satu server muat dalam satu tape; asumsi itu runtuh ketika server membesar (mis. HP T-500 berkapasitas 100 GB dengan tape 4 GB). Penulis lalu menemukan produk komersial (ARCServe, Alexandria, BudTool, SM-Arch) dan akhirnya *tape library* (Spectralogic) yang mengubah dunianya. Kisah ini terjadi di seluruh dunia: semakin kompleks komputasi terdistribusi, semakin penting perangkat lunak backup komersial.

#### Tantangan dengan Solusi Backup Komersial

**1. Sizing (Penentuan Ukuran).** Sebelum membeli, sistem harus diukur dengan benar. Nilai yang dibutuhkan: **ukuran satu *full backup***, **laju perubahan harian**, **RTO**, **RPO**, **retensi** on-site/off-site, **backup window**, dan **estimasi pertumbuhan** (3–5 tahun). Masalah umum: organisasi tidak tahu ukuran satu *full backup*.

> **Contoh perhitungan (dari sumber):** *Datacenter* 500 TB, laju perubahan 10% (50 TB/hari), RPO 24 jam, *full* bulanan disebar (≈17,86 TB/hari), *backup window* 10 jam.
> - Total harian = 17,86 + 50 = **67,86 TB/hari** → throughput ≈**1,88 GB/s**.
> - Untuk server 10 TB dengan RTO 4 jam: satu drive LTO-8 (750 MB/s) → ≈3,7 jam (masuk RTO). Namun dengan *multiplexing* 20, kecepatan restore ≈37,5 MB/s → ≈**74 jam** (jauh melewati RTO).
> - **Kapasitas:** retensi 13 bulan *full* (13 × 500 TB = 6,5 PB) + 90 hari incremental (90 × 50 TB = 4,5 PB) = **11 PB** (kapasitas efektif bila pakai dedup).
> - **Pertumbuhan:** 100%/tahun ≈ 700% terkompon dalam 3 tahun (kalikan tujuh).

Pelajaran kunci: **kemampuan restore sering mengendalikan desain lebih dari kemampuan backup**. Lebih mudah mem-backup 7 TB/jam dari seluruh datacenter daripada me-restore 2,5 TB/jam ke satu klien.

**2. Maintain Backup Server OS.** Server backup adalah "pintu depan" ke aset yang sangat diinginkan. OS-nya harus menjadi **server paling mutakhir dan paling aman** di datacenter — tetapi sering justru diabaikan.

**3. Maintain Backup Software.** Vendor terus menambah fungsi; Anda harus mengikuti pembaruan (terutama keamanan, segera). Agen backup di mana-mana juga harus di-upgrade. *"Tidak ada yang lebih menakutkan daripada meng-upgrade sistem backup Anda."*

> **Studi Kasus dari sumber — "Working as Designed" (1999, jelang Y2K):** Upgrade ke versi mayor membawa puluhan dampak tak diinginkan. Misalnya, fitur job-per-filesystem menjalankan skrip *hot backup mode* Oracle berulang, lalu job pertama yang selesai justru mengeluarkan Oracle dari mode backup. Respons vendor: "working as designed". Penulis menulis 175 skrip *shell* khusus untuk menyiasati "fitur" semacam itu, bekerja 95 jam/minggu. Pelajaran: uji versi baru perangkat lunak backup.

**4. Manage Multiple Vendors.** Sistem backup tradisional umumnya melibatkan ≥4 vendor (server backup, perangkat lunak, tape/disk, vendor *vaulting*) — sering 5–6 karena banyak organisasi punya 2–3 produk backup (akibat merger/akuisisi). Masalah terbesar: saling tuding (*finger-pointing*) saat ada inkompatibilitas.

**5. Separate System for DR.** Sistem backup biasa jarang memenuhi RTO DR (yang diukur dalam jam). Organisasi sering membeli sistem **kedua** (replikasi array-ke-array yang mahal) khusus DR.

**6. Separate System for E-Discovery.** Backup adalah teman terbaik untuk restore satu berkas, tetapi buruk untuk permintaan *e-discovery* (mis. "semua berkas berisi kata *whatchamacallit* dalam tiga tahun"). Ini mendorong kebutuhan sistem **archive** terpisah.

**7. Isu Tape & Disk.** Tape: *performance-tuning*, tape hilang, manajemen vendor *vaulting*. Disk: degradasi magnetik (*bit rot*) pada backup lama, dan — krusial — **disk tidak memiliki *air gap*** (rentan ransomware bila backup terlihat sebagai direktori).

**8. Pembelian Modal Besar & Overprovisioning.** Sistem dibeli via pembelian modal (*capital purchase*) besar, harus *overprovisioned* agar bertahan beberapa tahun, dan **sulit diskalakan**: pada titik tertentu server backup pusat tak sanggup memproses semua entri **indeks** dari semua backup, sehingga harus dibuat sistem backup terpisah yang tidak berbagi data.

#### Kesulitan Berganti Produk Backup

Berpindah produk backup itu sulit, terutama karena **data lama** (backup yang masih dalam retensi). Tiga pendekatan menurut sumber:

| Pendekatan | Penjelasan |
|---|---|
| **Let them expire** | Pertahankan sistem lama hanya untuk restore hingga backup lama kedaluwarsa, sambil mulai backup baru dengan sistem baru. |
| **Use a service** | Gunakan layanan untuk menyimpan/mengakses data lama. |
| **Restore and backup** | Restore data lama lalu backup ulang dengan sistem baru (mahal/lambat). |

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Sizing** | Penentuan ukuran sistem backup. |
| **Daily change rate** | Laju perubahan data harian (≈ukuran incremental). |
| **Backup window** | Rentang waktu yang diizinkan untuk backup. |
| **SWAG** | *Scientific Wild-Ass Guess* — perkiraan pertumbuhan. |
| **Backup index** | Indeks isi backup; membengkak dan membatasi skala. |
| **Vaulting vendor** | Vendor penyimpanan tape luar lokasi. |
| **Capital purchase (CapEx)** | Pembelian modal besar di muka. |
| **Overprovisioning** | Membeli kapasitas berlebih untuk mengantisipasi pertumbuhan. |
| **E-discovery** | Penemuan data elektronik untuk keperluan hukum. |

### Studi Kasus

**Kasus — Sizing yang Keliru.** Sebuah organisasi tidak mengetahui ukuran satu *full backup*-nya dan menjawab dengan "berapa banyak yang di-backup dalam seminggu". Tanpa angka ini, desain throughput dan kapasitas mustahil dilakukan dengan benar. Pelajaran: tentukan ukuran satu *full backup* sebagai langkah pertama *sizing*.

**Kasus — Restore Mengendalikan Desain.** Pada contoh 500 TB, mem-backup 7 TB/jam relatif mudah, tetapi *multiplexing* tinggi membuat restore 10 TB memakan 74 jam — jauh melewati RTO 4 jam. Pelajaran: kemampuan **restore** harus menjadi penggerak utama desain, bukan kemampuan backup.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Tentukan ukuran satu *full backup* dan laju perubahan sebelum *sizing*.
- Jadikan OS server backup paling aman & mutakhir di datacenter.
- Uji setiap upgrade perangkat lunak backup sebelum produksi.
- Pertimbangkan kemampuan restore sebagai penggerak desain.

**Kesalahan Umum:**
- Mengabaikan keamanan/patch server backup.
- Meng-upgrade perangkat lunak backup tanpa pengujian.
- Mengandalkan *multiplexing* tinggi sehingga restore lambat.
- Mengabaikan kebutuhan archive terpisah untuk e-discovery.

### Rangkuman

Perangkat lunak backup komersial merevolusi proteksi data dari era *shell script* dan *cron*. Namun ia membawa banyak tantangan: *sizing* yang rumit (memerlukan ukuran *full*, laju perubahan, RTO/RPO, retensi, *window*, pertumbuhan), pemeliharaan OS dan perangkat lunak server backup (upgrade yang menakutkan), pengelolaan banyak vendor, kebutuhan sistem terpisah untuk DR dan e-discovery, isu tape (tuning, kehilangan) dan disk (bit rot, tiadanya air gap), pembelian modal besar dengan *overprovisioning*, serta kesulitan skala akibat indeks backup yang membengkak. Berganti produk pun sulit karena data lama. Tantangan-tantangan inilah yang dijawab oleh berbagai kategori solusi pada Bab 14 dan 15.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Sebutkan nilai-nilai yang dibutuhkan untuk *sizing* sistem backup.
2. Mengapa OS server backup harus menjadi yang paling aman di datacenter?
3. Mengapa organisasi sering memerlukan sistem terpisah untuk DR dan e-discovery?

**Analisis/HOTS (C4–C5):**
4. Dengan contoh 500 TB, jelaskan mengapa kemampuan restore mengendalikan desain lebih dari kemampuan backup.
5. Analisislah mengapa indeks backup membatasi skalabilitas sistem tradisional.
6. Evaluasilah tiga pendekatan berganti produk backup (*let them expire*, *use a service*, *restore and backup*).

**Tugas Perancangan:**
7. Lakukan *sizing* untuk *datacenter* 200 TB dengan laju perubahan 8%/hari, RPO 24 jam, retensi 12 bulan *full* (bulanan) dan 60 hari incremental, *backup window* 8 jam. Hitung throughput dan kapasitas yang dibutuhkan, lalu identifikasi tantangan utama yang akan Anda hadapi.

---


## Bab 14 — Solusi Proteksi Data Tradisional

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mendefinisikan** (C1) apa yang dimaksud "solusi tradisional" (terutama melalui apa yang **bukan** solusi modern).
2. **Menjelaskan** (C2) keunggulan solusi backup tradisional, terutama keluasan cakupan (*breadth of coverage*) dan *snowball effect*.
3. **Menganalisis** (C4) tantangan solusi tradisional dengan merujuk pada tantangan Bab 13.
4. **Menjelaskan** (C2) cara kerja *target deduplication backup appliances* serta keunggulan dan tantangannya.
5. **Mengevaluasi** (C5) kapan solusi tradisional atau target dedupe tepat untuk sebuah lingkungan.

### Peta Konsep

```
SOLUSI PROTEKSI DATA TRADISIONAL  (tidak menyebut nama produk)
│
├── TRADITIONAL BACKUP SOLUTIONS (>20 thn; awalnya tape-centric)
│     ├── Keunggulan: breadth of coverage, snowball effect, agen, dump-and-sweep
│     ├── Tantangan: semua tantangan Bab 13
│     └── Analisis: masih dominan; pilih utk beban kerja beragam/legacy
│
└── TARGET DEDUPLICATION BACKUP APPLIANCES
      ├── Keunggulan: sedikit perubahan, replikasi off-site, dedup 10:1+
      ├── Tantangan: sizing (tebak rasio), dedup scope per-appliance,
      │   air gap, harga
      └── Analisis: gift bagi yang ingin lepas dari masalah tape
```

### Materi Inti

Industri proteksi data berevolusi melalui beberapa "gelombang". **Solusi tradisional** dahulu menguasai 100% pasar, lalu disusul solusi *virtualization-centric*, *hyper-converged*, dan *as-a-service*. Banyak (jika tidak sebagian besar) pengguna yang pindah tetap bertahan dengan pilihan barunya. Pasar hari ini adalah campuran produk lama dan baru.

#### Mendefinisikan Solusi Tradisional

Cara termudah mendefinisikannya: **bukan** solusi *virtualization-centric*, *target dedupe*, *hyper-converged*, atau *as-a-service*. Ciri solusi tradisional:

- Telah ada di industri **>20 tahun**, awalnya dirancang dengan **tape** di pusatnya (kini diadaptasi ke disk).
- Umumnya melakukan *full* lalu rangkaian *incremental*/*differential*, lalu *full* sesekali (bahkan bila *full* dapat disintesis).
- Dibeli sebagai perangkat lunak yang dipasang pada server backup pilihan Anda; ada **central backup server** dan satu/lebih **media/storage server**.

> **Catatan terminologi:** Istilah "master/slave servers" kini umumnya ditinggalkan karena konotasi historis negatif; "slave server" kini disebut *media/storage/device server*.

#### Keunggulan Solusi Tradisional

| Keunggulan | Penjelasan |
|---|---|
| **Breadth of coverage** | Keunggulan kompetitif terbesar: mencakup hampir semua OS (Unix, Windows, Linux, MacOS), hypervisor (vSphere, Hyper-V, AHV), dan basis data (Oracle, SQL Server, SAP, MySQL, Hadoop, MongoDB). Pelopor backup Kubernetes. |
| **Snowball effect** | Banyak digunakan karena cakupannya luas, dan cakupannya luas karena banyak digunakan — *snowball* yang menggelinding 30 tahun. |
| **Monitoring & reporting terpusat** | Tersedia, meski sebagian masih kurang (memunculkan industri alat pelaporan pihak ketiga). |
| **Backup agent** | Pelopor konsep agen backup yang berinteraksi dengan infrastruktur (sebelumnya hanya *shell script* + *dump-and-sweep*). |

> **Tentang alat pelaporan pihak ketiga:** Sangat berguna bila Anda memiliki >1 produk backup — menormalkan data dan melaporkan keberhasilan/tren/kapasitas lintas produk.

#### Tantangan Solusi Tradisional

Pengguna solusi tradisional mengalami **semua** tantangan Bab 13: sulit di-*sizing* (apalagi dengan dedup), pemeliharaan OS & perangkat lunak server backup, pengelolaan banyak vendor, kebutuhan sistem terpisah untuk DR dan e-discovery, isu tape (tuning, kehilangan, vendor *vaulting*) atau disk (degradasi, tiadanya *air gap*), pembelian modal besar, dan kesulitan skala (indeks server pusat membengkak → perlu sistem terpisah).

#### Analisis Solusi Tradisional

Solusi tradisional masih memegang **mayoritas pangsa pasar**. Saat penulisan, seluruh Fortune 100 dan sebagian besar Fortune 500 menjalankannya. Alasan utama memilihnya: **waktu di pasar** (teruji puluhan tahun R&D) dan **keluasan cakupan** (satu-satunya yang dapat mem-backup hampir semua yang dikembangkan dalam 30 tahun terakhir, termasuk varian Unix lama, IaaS/PaaS, Kubernetes, Hadoop, MongoDB, dan *bare-metal recovery* berbagai platform).

Solusi ini juga beradaptasi: menambah *source-side deduplication*, dukungan VADP/VSS dengan CBT, *synthetic full*, kemampuan memakai *object storage* cloud sebagai penyimpanan utama, dan replikasi backup antar-server pusat. Namun, semua kategori solusi modern (Bab 15) lahir untuk menjawab tantangan-tantangan tradisional. Pertanyaan bagi pengguna tradisional: apa yang dilakukan bila sebagian organisasi memerlukan solusi tradisional (mis. server Unix lama) sementara bagian lain tertarik ke solusi modern? Saran penulis (sama dengan saat era VMware): **pertimbangkan kompleksitas menjalankan banyak solusi backup** sebelum memindahkan sebagian beban kerja.

#### Target Deduplication Backup Appliances

*Target dedupe appliance* adalah *disk array* di belakang *head* (umumnya Linux), menyajikan diri sebagai NFS/SMB, iSCSI, atau VTL. Secara teknis bukan solusi backup mandiri, tetapi dibahas di sini karena (1) bagian umum dari banyak solusi backup, dan (2) bagi sebagian DBA, ini solusi backup lengkap (*dump-and-sweep* ke mount NFS/SMB yang lalu direplikasi off-site).

Appliance ini menjadi "hadiah luar biasa" untuk mengatasi masalah tape yang terlalu cepat. Alih-alih *disk caching* (parsial), kunci sukses adalah memiliki cukup disk untuk menampung banyak generasi *full*+*incremental* on-site — tetapi ini butuh disk sangat besar (500 TB → 6–11 PB). Di sinilah *target dedupe* berperan: mengiris backup, meng-*hash*, dan mengeliminasi duplikat.

**Keunggulan target dedupe:**

| Keunggulan | Penjelasan |
|---|---|
| **Sedikit perubahan** | Tidak perlu mengganti seluruh sistem backup; cukup arahkan backup ke perangkat baru. |
| **Versatil** | Banyak metode koneksi (NFS/SMB/iSCSI/VTL). |
| **Keandalan naik** | Beralih dari tape ke disk membuat backup lebih andal. |
| **Replikasi off-site** | Mereplikasi *new-unique bits* ke appliance kedua → on-site & off-site tanpa *man in a van*; mematuhi 3-2-1 tanpa menyentuh tape. |
| **Rasio dedup** | Pada lingkungan tradisional cenderung 10:1 atau lebih (11 PB → ≈1 PB disk fisik; bervariasi). |

**Tantangan target dedupe:**

| Tantangan | Penjelasan |
|---|---|
| **Sizing** | Tidak ada yang tahu seberapa baik data Anda ter-dedup hingga benar-benar di-dedup. *Dedupe scope* terbatas pada **satu *scale-up* appliance** — bila beli appliance kedua, masing-masing menjadi "pulau dedup". |
| **Underprovisioning → rush purchase** | Memicu pembelian darurat (tanpa daya tawar, berisiko terpaksa menghapus backup). Karena itu orang cenderung *overprovision*. |
| **Air gap** | Bila terhubung langsung via NFS/SMB/VTL, *rogue admin*/ransomware dapat merusak/menghapus semua backup. |
| **Harga** | Mahal; menambah dedup ke sistem lama lebih murah daripada mengganti seluruhnya, tetapi total solusi *greenfield* sering lebih mahal dari alternatif. Inilah mengapa banyak pengguna tetap menyalin ke tape untuk off-site. |

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Traditional backup solution** | Solusi >20 tahun, awalnya tape-centric, full+incremental. |
| **Breadth of coverage** | Keluasan cakupan OS/aplikasi/basis data. |
| **Snowball effect** | Efek bola salju: banyak dipakai → cakupan luas → makin banyak dipakai. |
| **Central / Media (storage) server** | Server backup pusat / server media. |
| **Target deduplication appliance** | Appliance dedup di sisi target (disk + head Linux). |
| **Dedup scope (scale-up)** | Cakupan dedup terbatas per appliance *scale-up*. |
| **Garbage collection** | Proses penghapusan backup lama pada sistem dedup. |

### Studi Kasus

**Kasus — Organisasi dengan Beban Kerja Beragam.** Sebuah perusahaan memiliki server Unix lama (HP-UX), VMware, basis data Oracle/MongoDB, dan beban kerja Kubernetes. Hanya solusi **tradisional** yang dapat mem-backup semuanya dalam satu sistem. Meski solusi modern mungkin lebih baik untuk beban kerja tertentu, memindahkan sebagiannya berarti menjalankan dua solusi — menambah kompleksitas. Pelajaran sumber: faktorkan kompleksitas multi-solusi dalam keputusan.

**Kasus — DBA dan Target Dedupe.** Para DBA mem-backup basis data via *dump-and-sweep* langsung ke mount NFS/SMB pada *target dedupe appliance*, yang lalu mereplikasi dump off-site. DBA senang, tim backup tak perlu mengurus backup basis data. Namun, karena backup terlihat sebagai direktori, perlu kewaspadaan terhadap risiko ransomware (gunakan protokol yang menyembunyikan direktori).

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Pilih solusi tradisional bila Anda butuh keluasan cakupan (beban kerja beragam/legacy).
- Lakukan *pilot* sebelum membeli *target dedupe* (rasio dedup tiap tipe data berbeda).
- Amankan koneksi target dedupe (hindari direktori yang terlihat OS).

**Kesalahan Umum:**
- Memindahkan sebagian beban kerja ke solusi baru tanpa mempertimbangkan kompleksitas multi-solusi.
- Menentukan *sizing* target dedupe berdasarkan rasio global, padahal membeli banyak appliance (pulau dedup).
- *Underprovisioning* yang memicu pembelian darurat.

### Rangkuman

Solusi proteksi data **tradisional** (didefinisikan sebagai yang bukan modern) telah ada >20 tahun, awalnya tape-centric, dengan keunggulan utama **keluasan cakupan** dan **snowball effect** — masih memegang mayoritas pangsa pasar. Namun mereka mewarisi seluruh tantangan Bab 13. **Target deduplication appliances** menjadi cara evolusioner (bukan revolusioner) mengatasi masalah tape: sedikit perubahan, replikasi off-site, rasio dedup 10:1+ — tetapi menghadapi tantangan *sizing* (tebak rasio, pulau dedup *scale-up*), *air gap*, dan harga. Saat memilih, pertimbangkan keluasan cakupan dan kompleksitas menjalankan banyak solusi.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Bagaimana penulis mendefinisikan "solusi tradisional"?
2. Jelaskan *breadth of coverage* dan *snowball effect*.
3. Bagaimana *target dedupe appliance* memungkinkan kepatuhan 3-2-1 tanpa tape?

**Analisis/HOTS (C4–C5):**
4. Mengapa solusi tradisional masih dominan meski pertumbuhan pendapatannya melambat?
5. Analisislah tantangan *sizing* target dedupe terkait "pulau dedup" *scale-up*.
6. Evaluasilah saran penulis untuk organisasi dengan beban kerja campuran legacy + modern.

**Tugas Perancangan:**
7. Sebuah perusahaan dengan banyak varian Unix lama dan VMware mempertimbangkan menambah *target dedupe appliance* pada solusi tradisionalnya. Rancang rencana *pilot* untuk mengukur rasio dedup per tipe data dan jelaskan bagaimana Anda menangani *air gap* serta off-site.

---


## Bab 15 — Solusi Proteksi Data Modern

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) empat kategori solusi modern: *virtualization-centric*, *hyper-converged backup appliances* (HCBA), *Data-Protection-as-a-Service* (DPaaS), dan *managed service providers* (MSP).
2. **Menganalisis** (C4) keunggulan dan tantangan setiap kategori, termasuk isu keamanan Windows pada solusi *virtualization-centric*.
3. **Membedakan** (C2) arsitektur *scale-up* dan *scale-out* serta relevansinya bagi HCBA.
4. **Mengevaluasi** (C5) kapan DPaaS atau MSP tepat, termasuk isu *design obfuscation* dan tanggung jawab.
5. **Menjelaskan** (C2) cara pasar beradaptasi: *traditional appliances*, *subscription pricing*, dan respons terhadap cloud (*lift-and-shift*).

### Peta Konsep

```
SOLUSI PROTEKSI DATA MODERN  (semua disk-centric)
│
├── VIRTUALIZATION-CENTRIC (Windows+disk; VADP; instant recovery & auto-test)
│     └── Tantangan: kerentanan Windows/RDP/C:\BACKUPS
├── HYPER-CONVERGED BACKUP APPLIANCES (HCBA; scale-out; Linux)
│     └── Tantangan: scale-down buruk; compute & storage tak terpisah
├── DATA-PROTECTION-AS-A-SERVICE (DPaaS; SaaS; pisahkan backup dari produksi)
│     └── Tantangan: bandwidth WAN; initial seed; restore besar; obfuscation
├── FULLY MANAGED SERVICE PROVIDERS (MSP; outsourcing penuh)
│     └── "outsource operasi, tak bisa outsource tanggung jawab"
│
└── ADAPTASI PASAR: traditional appliances | subscription pricing
    (bukan SaaS) | respons cloud (cloud out, lift-and-shift)
```

### Materi Inti

Semua produk di bab ini dirancang dengan **disk** di pusatnya dan lahir untuk menjawab pergeseran pasar tertentu. *Virtualization-centric* lahir karena solusi lama kurang menjawab virtualisasi; HCBA menjawab segmentasi (4–5 vendor); DPaaS menjawab kebutuhan yang sama dengan pendekatan SaaS.

#### Virtualization-Centric Solutions

Saat VMware populer, satu-satunya cara backup VM awalnya adalah memperlakukannya sebagai mesin fisik (masalah I/O). VMware mencoba **VCB** (gagal; penulis menjulukinya "Very Crappy Backup"), lalu **VADP** dengan CBT. Karena solusi tradisional lama tidak segera memperbaiki masalah ini, lahirlah solusi **virtualization-centric** yang mengambil pendekatan **disk-only, Windows-only**, berfokus pada VMware (kemudian Hyper-V). Penyederhanaan ini memudahkan R&D dan penggunaan.

**Keunggulan:**

| Keunggulan | Penjelasan |
|---|---|
| **Mudah dipahami** | Berbasis Windows & disk; UI Windows tipikal, tanpa manual Unix raksasa. |
| **Akses langsung ke data backup** | Penyimpanan mirip *copy*/snapshot → *mount* VMDK/VHD untuk *single-file recovery*; *browse* email Exchange tanpa restore basis data penuh. |
| **Instant recovery & automated testing** | Dua fitur terbesar yang dibawa ke industri: boot VM instan dari backup, dan **pengujian pemulihan otomatis** puluhan VM. "Pengubah permainan." |

**Tantangan:** Kerentanan keamanan. Backup yang tersimpan di `C:\BACKUPS` mudah dirusak; server backup berbasis **Windows** (target nomor satu ransomware), dan **RDP** (vektor serangan umum). Mitigasi: dukungan **Linux media server**, penyalinan ke **immutable storage** (mis. S3 Object Lock), dan protokol proprietary yang menyembunyikan direktori. Namun server backup utama tetap Windows.

> **Analisis:** Populer untuk lingkungan Windows-centric/virtualization-centric. Kerentanan Windows kini menjadi perhatian lebih besar; pertumbuhan pendapatan beberapa vendor melambat (sebagian diakuisisi *private equity*). Penulis berpendapat kerentanan Windows ada di jantung tren ini. Solusi ini **tidak** mengurangi jumlah vendor (banyak masih pakai *target dedupe*), dan sebagian besar tantangan Bab 13 lainnya tetap ada. Alasan utama memilihnya: Anda lingkungan Windows-centric yang familier dengan mitigasi keamanannya.

#### Hyper-Converged Backup Appliances (HCBA)

HCBA adalah sistem penyimpanan **scale-out** khusus untuk *secondary storage*/backup. Untuk memahaminya, bedakan:

- **Scale-up** — mulai dengan satu *node* + disk; tumbuh dengan menambah disk di belakang *node* itu (terbatas oleh daya *node* awal; indeks bisa membengkak).
- **Scale-out** — mulai dengan serangkaian *node* (masing-masing dengan compute & storage) dalam klaster; tumbuh dengan menambah *node*.

HCBA menerapkan *scale-out* pada backup, mengatasi *single point of failure* dan batas skala indeks. Menggunakan penyimpanan internal (target dedup sendiri, bukan pihak ketiga).

**Keunggulan:**

| Keunggulan | Penjelasan |
|---|---|
| **Scale-out** | Mudah diskalakan tanpa pemborosan; tak perlu *overprovision* berlebihan; bila *underprovision*, cukup tambah *node*. |
| **Anti-ransomware** | Arsitektur berbasis **Linux** (keunggulan keamanan atas pesaing on-premises terdekat). |
| **Appliance model** | "Satu nomor untuk ditelepon" bila ada masalah. |
| **Instant recovery & auto-test** | Mengadopsi fitur dari *virtualization-centric*. |
| **Reuse of backup data** | Memopulerkan pemanfaatan data backup (deteksi virus/ransomware, analisis penggunaan). |
| **Integrated dedupe & cloud** | Dedup terintegrasi yang skalabel; dapat menyalin backup ke object storage cloud. |

**Tantangan:**

| Tantangan | Penjelasan |
|---|---|
| **Scale-down buruk** | Menggunakan *target dedupe* sehingga kurang baik untuk situs kecil/remote (perlu appliance virtual lokal); tidak sefleksibel *source dedupe*. |
| **Provisioning untuk reuse** | Memanfaatkan data backup butuh compute/I/O tambahan → *overprovisioned* saat proses tak berjalan. |
| **Compute & storage tak terpisah** | Tiap *node* membawa compute & storage; tak bisa menskalakan keduanya secara independen. |

> **Analisis:** HCBA paling jauh mengatasi tantangan Bab 13 di kategori on-premises (termasuk kerentanan Windows, via Linux). Lebih sederhana didesain (tak perlu mendesain server/disk/tape terpisah), umumnya satu vendor, upgrade OS+aplikasi via satu *image* (seperti *firmware*). Sebagian mengadopsi cloud untuk DR dan menambah e-discovery. Tetap pembelian modal, tetapi *overprovisioning* untuk pertumbuhan tak diperlukan. Bagi banyak lingkungan, HCBA menawarkan keunggulan terbanyak dengan kekurangan paling sedikit di kategori on-premises.

#### Data-Protection-as-a-Service (DPaaS)

DPaaS untuk yang ingin **keluar dari bisnis backup** sepenuhnya — tidak membeli/menyewa/memelihara infrastruktur backup apa pun (seperti "SaaSifikasi TI" pada CRM, email, dll.).

Tantangan yang harus diselesaikan: **bandwidth WAN** (apakah cukup untuk backup harian — laws of physics), **initial seed** (backup pertama besar — sering via *sneakernet*: appliance dikirim, di-seed, dikirim balik), dan **restore besar** (tiga opsi: *local cache*, *recovery to the cloud* — pilihan terbaik menurut penulis, dan *reverse seeding* — terburuk, RTA berhari-hari).

> **Analisis:** Mengikuti tren SaaSifikasi TI. Keunggulan besar: **pemisahan data produksi dan backup** (melindungi dari *rolling ransomware*). Tantangan utama: realistiskah menempatkan infrastruktur backup di seberang WAN? DPaaS paling menarik bagi yang ingin keluar dari bisnis backup dan/atau melindungi backup dari ransomware. Contoh beban kerja yang sering diserahkan ke DPaaS: situs remote, laptop, SaaS, IaaS/PaaS.

#### Fully Managed Service Providers (MSP)

MSP (yang benar-benar *managed*) adalah tingkat layanan tertinggi: Anda **memberi tahu apa yang diinginkan**, lalu MSP mengonfigurasi dan **menjalankannya** untuk Anda. MSP dapat memakai banyak produk di belakang (mis. produk DR untuk sistem kritis, DPaaS untuk SaaS/cloud, on-prem untuk datacenter).

**Keunggulan:** menggunakan solusi *best-of-breed* tanpa perlu mempelajari/mengonfigurasi/mengelola; menghilangkan operasi harian dari organisasi. "Tidak ada yang mau menjadi orang backup" — MSP memberi admin yang berdedikasi pada backup.

**Tantangan:** sama dengan DPaaS bila via WAN (bandwidth, *initial seed*, restore besar), ditambah **design obfuscation** lebih besar (pelanggan tahu lebih sedikit tentang arsitektur; MSP dapat menukar komponen). Yang krusial:

> **"You cannot outsource responsibility."** Anda dapat meng-*outsource* operasi, tetapi **tidak** tanggung jawab. Bila MSP gagal memulihkan datacenter saat krisis, MSP kehilangan kontrak — tetapi **Anda** mungkin kehilangan pekerjaan. Jangan lengah; tetap pantau MSP.

#### Adaptasi Pasar

| Adaptasi | Penjelasan |
|---|---|
| **Traditional backup appliances** | Vendor tradisional/virtualization-centric menawarkan versi *appliance* (satu vendor, lebih mudah), tetapi tanpa skalabilitas *scale-out* HCBA. |
| **Subscription pricing** | Membayar bulanan/tahunan (OpEx) alih-alih pembelian modal besar. **Bukan SaaS** — Anda tetap mengelola perangkat keras & perangkat lunak; hanya cara membayar yang berubah. Waspadai vendor yang menyebut *subscription* sebagai "SaaS". |
| **Respons cloud** | *Cloud out* (salin backup ke S3 sebagai pengganti tape); *on-prem software in cloud VMs* (*lift-and-shift* — mahal karena VM jalan 24×7 dan butuh *block storage*; tidak menyelesaikan sebagian besar tantangan); *cloud native* (dirancang ulang untuk object storage — paling efisien tetapi jarang). |

> **Catatan tentang lift-and-shift:** Dipandang sebagai solusi sementara karena biayanya tinggi (VM 24×7, *block storage*, *egress charges* saat restore). Pemindahan jangka panjang ke cloud sebaiknya disertai *refactoring* — tetapi vendor *lift-and-shift* umumnya belum melakukannya.

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **Virtualization-centric solution** | Solusi disk-only/Windows-only berfokus VMware/Hyper-V. |
| **VCB / VADP** | API backup VMware (gagal / berhasil). |
| **HCBA (Hyper-Converged Backup Appliance)** | Appliance backup *scale-out* berbasis Linux. |
| **Scale-up / Scale-out** | Tumbuh dengan menambah disk / menambah node. |
| **DPaaS** | *Data-Protection-as-a-Service*. |
| **MSP (Managed Service Provider)** | Penyedia yang menjalankan proteksi data atas nama Anda. |
| **Design obfuscation** | Ketidakjelasan arsitektur bagi pelanggan layanan. |
| **Sneakernet / Initial seed** | Pengiriman fisik appliance untuk backup pertama. |
| **Reverse seeding** | Pengiriman fisik untuk restore besar (RTA berhari-hari). |
| **Lift-and-shift** | Memindahkan VM apa adanya ke cloud tanpa *refactoring*. |
| **Subscription pricing (≠ SaaS)** | Model pembayaran berlangganan (bukan SaaS). |

### Studi Kasus

**Kasus — Lingkungan Windows-Centric.** Sebuah perusahaan 100% Windows + VMware memilih solusi *virtualization-centric* karena kemudahan dan fitur *instant recovery*/auto-test. Mereka memitigasi risiko dengan **Linux media server**, **immutable S3 (Object Lock)**, dan konfigurasi yang menyembunyikan direktori backup dari OS. Pelajaran: solusi ini cocok bila Anda paham dan menangani risiko keamanan Windows-centric.

**Kasus — UMKM Memilih DPaaS.** Sebuah UMKM teknologi di Indonesia tidak memiliki staf khusus backup dan ingin "keluar dari bisnis backup". Mereka memilih DPaaS untuk melindungi laptop, SaaS (Microsoft 365), dan VM cloud. Sebelum berlangganan, mereka melakukan percakapan *sizing* untuk memastikan bandwidth cukup, dan memastikan penyedia memiliki jawaban untuk *initial seed* dan restore besar. Keuntungan tambahan: backup terpisah dari produksi, melindungi dari *rolling ransomware*.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Cocokkan kategori solusi dengan profil lingkungan (Windows-centric → virtualization-centric; ingin scale-out on-prem → HCBA; ingin keluar dari bisnis backup → DPaaS/MSP).
- Pada solusi Windows-centric, pindahkan backup ke Linux/immutable storage.
- Pada MSP, tetap pantau dan pahami detail layanan & biaya.

**Kesalahan Umum:**
- Menggunakan konfigurasi default Windows + `C:\BACKUPS` (rentan ransomware).
- Menyamakan *subscription pricing* dengan SaaS.
- *Lift-and-shift* sebagai solusi cloud jangka panjang tanpa *refactoring*.
- Lengah pada MSP (mengira tanggung jawab ikut ter-*outsource*).

### Rangkuman

Solusi proteksi data **modern** semuanya disk-centric dan lahir untuk menjawab pergeseran pasar. **Virtualization-centric** mudah dipakai dan membawa *instant recovery* serta pengujian otomatis, tetapi rentan akibat fondasi Windows/RDP/`C:\BACKUPS`. **HCBA** menerapkan arsitektur *scale-out* berbasis Linux yang mengatasi banyak tantangan on-premises, meski kurang baik *scale-down* dan tak memisahkan compute/storage. **DPaaS** memungkinkan keluar dari bisnis backup dan memisahkan backup dari produksi (anti-ransomware), dengan tantangan bandwidth/seed/restore. **MSP** meng-*outsource* operasi sepenuhnya — tetapi tanggung jawab tetap milik Anda. Pasar beradaptasi via *appliance* tradisional, *subscription pricing* (bukan SaaS), dan respons cloud (di mana *lift-and-shift* dipandang sementara).

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Sebutkan empat kategori solusi modern dan ciri masing-masing.
2. Bedakan arsitektur *scale-up* dan *scale-out*.
3. Apa perbedaan *subscription pricing* dan SaaS?

**Analisis/HOTS (C4–C5):**
4. Mengapa fondasi Windows menjadi kelemahan keamanan utama solusi *virtualization-centric*, dan bagaimana memitigasinya?
5. Mengapa HCBA "paling jauh" mengatasi tantangan on-premises? Apa keterbatasannya?
6. Evaluasilah prinsip "you cannot outsource responsibility" dalam konteks MSP.

**Tugas Perancangan:**
7. Sebuah organisasi ragu antara HCBA (on-premises) dan DPaaS. Buat matriks keputusan berdasarkan: keinginan keluar dari bisnis backup, bandwidth WAN, skalabilitas, keamanan ransomware, dan model biaya. Rekomendasikan pilihan dengan justifikasi.

---


## Bab 16 — Mengganti atau Meng-upgrade Sistem Backup Anda

### Tujuan Pembelajaran

Setelah mempelajari bab ini, pembaca diharapkan mampu:

1. **Mengaitkan** (C4) pengetahuan dari seluruh bab untuk menentukan solusi mana yang tepat.
2. **Menjelaskan** (C2) *unique selling proposition* (USP) tiap kategori solusi.
3. **Membedakan** (C2) pembagian tanggung jawab (hardware, software, configuration, monitoring, operation) antara organisasi dan vendor.
4. **Menganalisis** (C4) *Total Cost of Ownership* (TCO) — bukan sekadar biaya akuisisi.
5. **Menerapkan** (C3) kriteria pemilihan: *showstoppers*, *ease of use*, *scalability*, dan *future proofing*.

### Peta Konsep

```
MENGGANTI / MENG-UPGRADE SISTEM BACKUP
│
├── PRASYARAT: pahami difference backup/archive, 3-2-1, apa yg di-backup,
│   cara backup, DR, tape & disk, tantangan, solusi tradisional & modern
│
├── SOLUSI MANA YANG TERBAIK? (USP per kategori)
├── TANGGUNG JAWAB ANDA (HW, SW, config, monitoring, operation)
│     └── "you can never outsource responsibility"
├── SEBELUM BERTINDAK
│     ├── This is YOUR backup system (requirements driven)
│     ├── Pahami requirements, yang dimiliki, yang tak disukai
│     └── TCO bukan sekadar acquisition cost
│
└── MEMILIH SOLUSI
      ├── Find any showstoppers (+ nice-to-haves)
      ├── Prioritize ease of use
      ├── Prioritize scalability
      └── Prioritize future proofing
```

### Materi Inti

Penulis mengingatkan: bila Anda melompat ke bab ini berharap diberi tahu produk mana yang harus dibeli — tidak secepat itu. Bab ini adalah puncak yang mengandaikan pemahaman seluruh buku. Ringkasan hal-hal penting yang harus Anda kuasai: perbedaan **backup vs archive** (Bab 3), **aturan 3-2-1** (Bab 3), **apa yang di-backup** termasuk SaaS (Bab 8), **cara backup** (Bab 9), **disaster recovery** (Bab 11), **tape tidak jahat** & **disk tidak sempurna** (Bab 12), **tantangan** (Bab 13), serta **solusi tradisional & modern** (Bab 14–15).

#### Solusi Mana yang Terbaik untuk Anda?

> *"There is no one perfect backup product."* Yang ada adalah produk yang lebih cocok dengan cara Anda berfungsi. Mulailah dengan memahami **kebutuhan unik** Anda (proses Bab 2), lalu pahami **USP** tiap kategori:

| Kategori | USP (kapan tepat) | Tantangan utama |
|---|---|---|
| **Traditional backup** | Datacenter dengan campuran beban kerja legacy (Unix, basis data lama) + virtualisasi + modern (IaaS, Kubernetes); ingin satu solusi "*one-size-fits-all*". | TCO & kompleksitas; tidak semua dalam satu solusi unggul. |
| **Target dedupe** | Punya solusi backup dan kesulitan backup ke tape atau tak puas dengan dedup bawaan; ingin on-site & off-site via replikasi tanpa banyak perubahan. | Lebih mahal di lingkungan *greenfield* dibanding solusi yang menggabungkan keduanya. |
| **Virtualization-centric** | Lingkungan Windows-centric/Windows-only yang familier menangani keamanan Windows. | Konfigurasikan agar disk backup tak terlihat OS (anti-ransomware). |
| **HCBA** | Ingin solusi on-premises yang mengatasi sebagian besar tantangan Bab 13; arsitektur *scale-out* mudah didesain, dipelihara, diskalakan. | Tak perlu kapasitas 3–5 tahun di muka; tambah seiring waktu. |
| **DPaaS** | Tak ingin lagi mendesain/memelihara/menskalakan solusi on-premises (seperti email/CRM). | *Design obfuscation* (pengalaman tak konsisten, tagihan melonjak). |
| **Fully managed MSP** | Ingin sistem proteksi data sepenuhnya *hands-off*. | Bagaimana bila vendor mengganti solusi di belakang; pahami detail biaya. |
| **Traditional appliances** | Suka solusi saat ini tetapi tak suka kerja merancang/mengonfigurasi perangkat keras. | Tak ada skalabilitas *scale-out* HCBA. |
| **On-premises in the cloud** | Ada mandat *cloud-first* tetapi tak ingin ganti solusi (lift-and-shift). | Tagihan cloud tinggi (VM 24×7, *block storage*). |

#### Tanggung Jawab Anda

Ketahui siapa bertanggung jawab atas setiap tugas dalam siklus hidup sistem proteksi data:

| Tugas | Penjelasan |
|---|---|
| **Hardware** | Mendesain, membayar, meng-upgrade OS, menghubungkan storage, memastikan performa. |
| **Software** | Mengonfigurasi perangkat lunak backup mengenali sumber daya; memeliharanya aman & mutakhir. |
| **Configuration** | Memasang agen, menghubungkan sumber, membuat *job* & jadwal (besar di awal, berkelanjutan). |
| **Monitoring** | Memastikan sistem benar-benar bekerja (dari sekadar melihat UI harian hingga tiket otomatis). |
| **Operation** | Tugas berkelanjutan (tukar tape, hapus backup lama, tambah ruang). |

Pada sebagian besar solusi (tradisional, target dedupe, virtualization-centric, HCBA, traditional appliances, on-prem-in-cloud), **organisasi Anda** bertanggung jawab atas semua tugas. Dengan **DPaaS**, hardware & software bukan lagi tanggung jawab Anda (Anda tetap *configure*, *operate*, *monitor*). Dengan **MSP**, bahkan tugas-tugas itu pun di-*outsource*. Namun:

> **"You can outsource design, maintenance, operations, and monitoring. You can never outsource responsibility."** Bila sistem gagal, organisasi Andalah yang menderita. Ini sangat penting bila memakai MSP (dapat menimbulkan kelengahan).

#### Sebelum Anda Bertindak

Banyak orang langsung membeli saat ada masalah. Sering kali penulis hanya **mengganti masuk-keluar solusi yang sama**! Sebelum menghabiskan uang:

- **This Is Your Backup System.** Datanya milik Anda. Kebutuhan & cara kerja unik Anda yang menentukan solusi terbaik — bukan vendor.
- **Pahami requirements Anda** (proses Bab 2). Mengonfigurasi tanpa memahami kebutuhan nyata adalah pemborosan.

> **Studi Kasus dari sumber:** Sebuah organisasi frustrasi karena backup gagal tiap malam (RPO 24 jam tak tercapai) lalu menghabiskan ratusan ribu dolar mengganti sistem demi RPO 12 jam — kemudian mengetahui organisasinya hanya membuat data baru sekali seminggu (RPO satu minggu sudah cukup). Pelajaran: pahami kebutuhan **sebelum** membelanjakan uang.

- **Pahami apa yang Anda miliki.** Miliki SME internal; bila tidak ada, ini pengeluaran pertama yang tepat (jasa profesional untuk mengonfigurasi optimal).
- **Pahami apa yang tidak Anda sukai** (biasanya mudah — semua ingat restore yang gagal).

> **Studi Kasus dari sumber — "Did I Do That?":** Sebuah vendor SaaS memerlukan *cold backup* basis data (mematikan layanan), dijadwalkan tiap dua minggu. Karena 90% bisnis tahunan datang dalam ~5 hari, seorang operator yang mengikuti manual mematikan basis data **di tengah** periode puncak itu — menjadi berita nasional, dan saham anjlok 50%. Pelajaran: pahami betul apa yang tidak boleh dilakukan sistem backup.

- **Consider TCO, Not Just Acquisition Cost.** Tiga pilihan: *tweak* sistem saat ini, *upgrade* sebagian, atau *replace*. Tiap pilihan punya elemen TCO berbeda (biaya pemeliharaan, pelatihan, kompleksitas multi-sistem, biaya cloud/egress untuk on-prem-in-cloud, biaya bandwidth untuk SaaS/MSP).

#### Memilih Solusi

| Kriteria | Penjelasan |
|---|---|
| **Find any showstoppers** | Fitur yang **tak dapat ditawar** (mis. "harus dikelola via web tanpa agen lokal"). *Showstopper* mempersempit kandidat secara drastis. Tambahkan pula daftar *nice-to-have* untuk menilai kandidat yang setara. "Keputusan sebesar ini dibuat oleh Spock, bukan Kirk." |
| **Prioritize ease of use** | "UI seperti lelucon; bila harus dijelaskan, ia tidak bagus." Karena *pintu putar* admin backup, kemudahan menekan biaya pelatihan. |
| **Prioritize scalability** | Seberapa mudah menambah compute/storage tanpa membuang yang sudah dibeli. Yang termudah diskalakan: **HCBA, DPaaS, dan MSP berbasis cloud** (mulai kecil, tambah bertahap). DPaaS sering menagih hanya yang dipakai (turun pun bisa). |
| **Prioritize future proofing** | Lihat arsitektur & rekam jejak vendor terhadap teknologi baru (saat itu: Kubernetes/Docker). Pikirkan ke mana lingkungan Anda menuju (on-premises besar vs cloud) 3–5 tahun ke depan. |

### Istilah Kunci

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **USP (Unique Selling Proposition)** | Alasan unik memilih suatu solusi. |
| **TCO (Total Cost of Ownership)** | Total biaya kepemilikan (bukan sekadar akuisisi). |
| **Showstopper / Nice-to-have** | Fitur tak-dapat-ditawar / fitur tambahan yang diinginkan. |
| **Ease of use / Scalability / Future proofing** | Kemudahan pakai / skalabilitas / kesiapan masa depan. |
| **CapEx / OpEx** | Belanja modal / belanja operasional. |
| **Wetware** | "Konfigurasi/manusia" — sering jadi akar masalah, bukan perangkat. |

### Studi Kasus

**Kasus — RPO yang Tidak Dibutuhkan.** (Lihat di atas) Mengganti sistem demi RPO 12 jam padahal kebutuhan nyata RPO satu minggu = pemborosan ratusan ribu dolar. Pelajaran: kebutuhan mengendalikan keputusan.

**Kasus — Showstopper Mempersempit Kandidat.** Sebuah perusahaan menetapkan *showstopper*: solusi penyimpanan harus menyediakan 90 hari *snapshot* yang dapat ditelusuri pengguna. Persyaratan tunggal ini mengeliminasi sebagian besar solusi (yang memakai *copy-on-write* dengan penurunan performa), menyisakan tiga-empat kandidat. Pelajaran: identifikasi *showstopper* untuk menyederhanakan keputusan.

### Praktik Baik & Kesalahan Umum

**Praktik Baik:**
- Pahami kebutuhan, apa yang dimiliki, dan apa yang tak disukai **sebelum** membeli.
- Pertimbangkan TCO menyeluruh, bukan sekadar harga akuisisi.
- Identifikasi *showstoppers* & *nice-to-haves*; prioritaskan *ease of use*, *scalability*, *future proofing*.
- Kurangi risiko dengan mengurangi jumlah jenis produk/vendor (idealnya hilangkan tape dari backup/DR; sisakan untuk archive).

**Kesalahan Umum:**
- Membeli solusi baru padahal masalahnya adalah konfigurasi (*wetware*).
- Mengejar RTO/RPO yang tidak benar-benar dibutuhkan organisasi.
- Mengabaikan biaya pelatihan dan kompleksitas multi-sistem dalam TCO.
- Memilih solusi karena "penjualnya paling lihai" (Kirk), bukan berdasarkan kebutuhan (Spock).

### Rangkuman

Mengganti atau meng-upgrade sistem backup harus berlandaskan pemahaman seluruh buku, dimulai dari kebutuhan unik organisasi (proses Bab 2) dan USP tiap kategori solusi. Ketahui pembagian tanggung jawab (hardware, software, configuration, monitoring, operation) — dan ingat bahwa **tanggung jawab tidak dapat di-outsource**. Sebelum membelanjakan uang, pahami kebutuhan, apa yang dimiliki, dan apa yang tak disukai; pertimbangkan **TCO** menyeluruh, bukan sekadar biaya akuisisi. Dalam memilih, identifikasi *showstoppers* (dan *nice-to-haves*), lalu prioritaskan *ease of use*, *scalability*, dan *future proofing*. Cara terbaik mengurangi risiko perpindahan adalah mengurangi jumlah produk/vendor — umumnya dengan menghilangkan tape dari backup/DR dan menyisakannya untuk archive.

### Latihan & Refleksi

**Pemahaman (C1–C2):**
1. Sebutkan prasyarat pemahaman (dari bab-bab sebelumnya) sebelum mengganti sistem backup.
2. Jelaskan lima area tanggung jawab dalam siklus hidup sistem proteksi data.
3. Apa perbedaan *showstopper* dan *nice-to-have*?

**Analisis/HOTS (C4–C5):**
4. Mengapa "tanggung jawab tidak dapat di-outsource", dan apa implikasinya bagi pengguna MSP?
5. Analisislah kasus "RPO yang tidak dibutuhkan": kesalahan proses apa yang terjadi?
6. Mengapa *ease of use* dan *scalability* sangat penting menurut penulis? Kaitkan dengan "pintu putar admin backup" dan TCO.

**Tugas Perancangan:**
7. Sebuah universitas hendak mengganti sistem backup-nya. Susun: (a) daftar kebutuhan (RTO/RPO/retensi), (b) 2–3 *showstoppers* dan beberapa *nice-to-haves*, (c) analisis TCO ringkas untuk dua kandidat (mis. HCBA vs DPaaS), dan (d) rekomendasi akhir berdasarkan *ease of use*, *scalability*, dan *future proofing*.

---


## Bab Penutup: Sintesis dan Merancang Strategi Proteksi Data Menyeluruh

### Tujuan Bab Penutup

Bab penutup ini menyintesiskan keseluruhan buku menjadi sebuah kerangka praktis untuk **merancang strategi proteksi data menyeluruh**, lalu menutup dengan pandangan tren masa depan dan relevansi bagi organisasi di Indonesia.

### Benang Merah Seluruh Buku

Beberapa prinsip muncul berulang di hampir setiap bab dan layak menjadi pegangan utama:

> **1. Yang penting adalah RESTORE.** *"No one cares if you can backup. Only if you can restore."* Seluruh desain harus berorientasi pada keterpulihan, dan keterpulihan hanya dibuktikan melalui **pengujian**.

> **2. Aturan 3-2-1 adalah hukum fundamental.** Tiga versi, dua media, satu di tempat lain. Bila desain Anda tidak mematuhinya, ada yang salah secara fatal. Gunakan aturan ini untuk menilai apakah sesuatu benar-benar terlindungi — termasuk SaaS dan cloud.

> **3. Backup ≠ Archive.** Backup untuk *restore* (satu hal, satu titik waktu); archive untuk *retrieve* (banyak hal, rentang lebar). Jangan gunakan yang satu untuk pekerjaan yang lain.

> **4. Kebutuhan mengendalikan desain.** RTO/RPO berasal dari organisasi, bukan TI. Pahami kebutuhan sebelum memilih teknologi.

> **5. Ransomware mengubah segalanya.** DR dengan RTA pendek adalah satu-satunya jawaban sahih; jangan bayar tebusan. Lindungi backup dengan enkripsi, *air gap*, dan *immutability*.

> **6. Cloud bukan sihir.** Cloud hanyalah komputer orang lain; aturan proteksi data tetap berlaku, dan datanya tetap tanggung jawab Anda.

### Kerangka Merancang Strategi Proteksi Data Menyeluruh

Berikut sintesis langkah-demi-langkah yang merangkai seluruh bab:

```
ALUR MERANCANG STRATEGI PROTEKSI DATA MENYELURUH

[1] PAHAMI RISIKO (Bab 1)
     └→ Manusia, sistem, alam, ransomware

[2] KUMPULKAN KEBUTUHAN (Bab 2)
     └→ SME, RTO/RPO, klasifikasi data, kepatuhan (UU PDP),
        SLA, RACI, runbook

[3] TETAPKAN FONDASI KONSEP (Bab 3-4)
     └→ Backup vs archive, 3-2-1, enkripsi/air gap/immutability,
        level backup, metrik (RTO/RPO/RTA/RPA), pengujian

[4] PETAKAN SUMBER DATA (Bab 6-8)
     └→ Server fisik/virtual, NAS, basis data, cloud (IaaS/PaaS/
        SaaS/serverless), Kubernetes, IoT — semua perlu backup

[5] PILIH TEKNOLOGI & METODE (Bab 5, 9-12)
     └→ Disk & dedup, metode (incremental forever/source dedup/
        near-CDP), archive, DR (warm/hot site, cloud), target
        (disk/object/tape utk archive)

[6] PILIH KATEGORI SOLUSI (Bab 13-16)
     └→ Tradisional / target dedupe / virtualization-centric /
        HCBA / DPaaS / MSP — berdasarkan USP, TCO, showstoppers,
        ease of use, scalability, future proofing

[7] DOKUMENTASIKAN, OTOMATISKAN, UJI, ITERASI
     └→ Runbook, RACI, pengujian restore & DR berkala
```

**Penjelasan ringkas tiap tahap:**

1. **Pahami risiko** (Bab 1) — sadari bahwa ancaman terbesar adalah manusia dan ransomware, bukan sekadar kegagalan perangkat keras.
2. **Kumpulkan kebutuhan** (Bab 2) — libatkan SME, tetapkan RTO/RPO dari organisasi, klasifikasikan data, dan patuhi regulasi (di Indonesia: UU PDP).
3. **Tetapkan fondasi konsep** (Bab 3–4) — pastikan setiap desain mematuhi 3-2-1, membedakan backup/archive, dan mengukur RTO/RPO vs RTA/RPA secara jujur.
4. **Petakan sumber data** (Bab 6–8) — identifikasi seluruh tempat data tercipta dan tersimpan; ingat bahwa SaaS/cloud/Kubernetes/IoT pun perlu backup.
5. **Pilih teknologi & metode** (Bab 5, 9–12) — manfaatkan disk & deduplikasi, pilih metode sesuai kebutuhan restore (instant recovery via near-CDP, dsb.), dan rancang DR berbasis cloud; gunakan tape untuk archive.
6. **Pilih kategori solusi** (Bab 13–16) — cocokkan USP kategori dengan profil organisasi, pertimbangkan TCO, dan terapkan kriteria pemilihan.
7. **Dokumentasikan, otomatiskan, uji, iterasi** — *runbook*, RACI, dan pengujian restore/DR berkala adalah penentu keberhasilan akhir.

### Tren Masa Depan

Berdasarkan pandangan penulis sumber, beberapa tren akan terus membentuk proteksi data:

- **Pergeseran ke cloud.** Dalam beberapa tahun, hampir semua organisasi akan menggunakan cloud dalam proteksi datanya. Pertanyaannya: membeli/menjalankan perangkat lunak sendiri di cloud, atau beralih ke layanan terkelola (DPaaS/MSP)?
- **Object storage sebagai target dominan.** Penulis menduga *object storage* akan menjadi target backup dominan seiring waktu.
- **Immutability & anti-ransomware.** *Immutable storage* (terutama berbasis cloud) akan menjadi fitur yang jauh lebih penting daripada sebelumnya.
- **Pemanfaatan data backup (*data management*).** Penggunaan ulang data backup untuk e-discovery, kepatuhan, deteksi ransomware (via *machine learning*), test/dev, dan analitik akan tumbuh menjadi industri besar — selama sistem backup tetap pandai melakukan backup/restore.
- **Kubernetes sebagai "jalur baru".** Kontainer dan orkestrasi membuka cara baru melihat proteksi data (backup berbasis aplikasi/namespace).
- **Tape tetap hidup untuk archive.** Meski "pensiun" dari backup/DR bagi sebagian besar organisasi, tape tetap relevan untuk penyimpanan jangka panjang/archive.

### Relevansi untuk Organisasi di Indonesia

Prinsip-prinsip dalam buku ini berlaku universal, tetapi konteks Indonesia menambah pertimbangan khusus:

- **Risiko bencana alam tinggi.** Indonesia berada di "Cincin Api" dengan risiko gempa, tsunami, letusan, dan banjir. Penempatan situs DR di **zona seismik dan zona banjir yang berbeda** dari lokasi utama menjadi krusial — DR berbasis cloud lintas-region sangat relevan.
- **Kepatuhan UU PDP.** Undang-Undang Pelindungan Data Pribadi (UU No. 27 Tahun 2022) menuntut pengelolaan retensi, penghapusan, dan akses data pribadi — termasuk yang tersimpan di backup dan archive. Libatkan SME hukum/kepatuhan sejak tahap pengumpulan kebutuhan. *(UU PDP disebut sebagai padanan kontekstual; bukan bagian dari buku sumber.)*
- **Kendala bandwidth di wilayah tertentu.** Sebagaimana kisah "pulau dengan internet terbatas" di buku sumber, sebagian wilayah Indonesia memiliki keterbatasan bandwidth. Di sini, kombinasi disk on-premises + replikasi + tape (untuk salinan luar lokasi) atau *initial seed* via *sneakernet* untuk DPaaS perlu dipertimbangkan.
- **Adopsi cloud & SaaS yang meningkat.** Banyak organisasi Indonesia mengadopsi Microsoft 365, Google Workspace, dan layanan cloud. Penting menyadari bahwa **backup tidak termasuk** dalam SaaS — perlu solusi pihak ketiga yang mematuhi 3-2-1.
- **Keterbatasan SDM khusus backup.** "Tidak ada yang mau menjadi orang backup" berlaku di mana saja. DPaaS/MSP dapat menjadi pilihan menarik bagi UMKM dan organisasi dengan SDM TI terbatas — selama tanggung jawab tetap dipantau.

### Penutup

Proteksi data modern adalah disiplin yang luas dan kompleks, tetapi berporos pada gagasan sederhana: **pastikan data dapat dipulihkan**. Dengan memahami risiko, menetapkan kebutuhan dari organisasi, mematuhi aturan 3-2-1, membedakan backup dari archive, memilih teknologi dan kategori solusi yang tepat, serta — yang terpenting — **menguji** pemulihan secara rutin, sebuah organisasi dapat menghadapi kesalahan manusia, kegagalan sistem, bencana alam, dan ransomware dengan percaya diri.

Sebagaimana penulis sumber menutup bukunya: bila Anda terlibat dalam perdebatan "haruskah ini di-backup?", ajukan dua pertanyaan — apakah data bernilai bagi organisasi, dan apakah sudah di-backup dengan cara yang mematuhi 3-2-1? Bila bernilai dan belum terlindungi secara sah, maka harus di-backup. Dan untuk semua yang peduli agar seluruh data terlindungi: *"3-2-1 rule forever!"*

---

## Glosarium (EN → ID)

| Istilah (EN) | Penjelasan (ID) |
|---|---|
| **3-2-1 rule** | Aturan fundamental backup: tiga versi data, pada dua media berbeda, satu di antaranya di tempat lain. |
| **Air gap (physical/virtual)** | Pemisahan (fisik atau elektronik) antara sistem produksi dan sistem proteksi untuk membatasi *blast radius*. |
| **Application-consistent backup** | Backup yang konsisten sehingga aplikasi selalu dapat memulihkan diri. |
| **Archive** | Salinan referensi dengan metadata, dibuat untuk *retrieve* (bukan *restore*). |
| **Archive bit** | Penanda di Windows untuk berkas baru/berubah yang perlu di-backup. |
| **Asynchronous replication** | Replikasi yang membolehkan target tertinggal dari sumber; dampak performa rendah. |
| **Backup** | Salinan data terpisah dari aslinya, untuk memulihkan (*restore*) ke keadaan semula. |
| **Backup window** | Rentang waktu yang diizinkan untuk menjalankan backup. |
| **Bare-metal backup/recovery** | Backup/pemulihan untuk membangun ulang server fisik dari nol. |
| **Bit rot** | Degradasi data magnetik seiring waktu. |
| **Blast radius** | Cakupan kerusakan yang dapat ditimbulkan satu insiden/akun. |
| **Block-level incremental** | Backup hanya blok yang berubah (via CBT). |
| **Block storage** | Penyimpanan blok (LUN); umumnya tanpa redundansi, perlu di-backup. |
| **Business Continuity Planning (BCP)** | Perencanaan keberlangsungan bisnis (lebih luas dari DR). |
| **CBT (Changed-Block Tracking)** | Pelacakan blok yang berubah sejak backup terakhir. |
| **CDM (Copy Data Management)** | Pengelolaan salinan data untuk banyak keperluan (backup, test/dev, analitik). |
| **CDP (Continuous Data Protection)** | Replikasi asinkron + *change log*; titik pemulihan tak terbatas. |
| **Charge-back model** | Pembebanan biaya layanan ke departemen pengguna. |
| **Chunk** | Potongan data hasil irisan untuk deduplikasi. |
| **Cold/Warm/Hot site** | Tingkat kesiapan situs pemulihan (lambat/sedang/cepat). |
| **Cold backup** | Backup basis data dengan instance dimatikan. |
| **Convenience copy** | Salinan nyaman yang berdekatan dengan aslinya; bukan backup. |
| **Conversion / Transformation** | Penyesuaian format disk DR: lambat (pipa seluruh image) / cepat (di tempat). |
| **Copy** | Reproduksi byte-for-byte berisi konten identik aslinya. |
| **Copy-on-write (CoW)** | Metode snapshot: salin blok lama sebelum ditimpa. |
| **CSI (Container Storage Interface)** | Antarmuka penyimpanan kontainer; mendukung snapshot PV. |
| **Daily change rate** | Laju perubahan data harian (≈ ukuran incremental). |
| **Data classification** | Klasifikasi data menurut tingkat kekritisan. |
| **Deduplication (dedupe)** | Identifikasi & eliminasi data duplikat. |
| **Dedupe scope** | Cakupan perbandingan dedup (backup set → global). |
| **Differential / Cumulative incremental** | Backup semua perubahan sejak full terakhir. |
| **Disaster Recovery (DR)** | Pemulihan saat sebagian besar lingkungan komputasi tidak beroperasi. |
| **DPaaS (Data-Protection-as-a-Service)** | Proteksi data sebagai layanan SaaS. |
| **DPO (Data Protection Officer)** | Pejabat pelindungan data untuk kepatuhan privasi. |
| **DRaaS (DR-as-a-Service)** | Disaster recovery sebagai layanan. |
| **Dump-and-sweep** | Backup basis data via *dump* lalu *sweep* dengan backup filesystem. |
| **E-discovery** | Penemuan data elektronik untuk keperluan hukum. |
| **Edge computing / IoT** | Komputasi di tepi / Internet of Things. |
| **Egress charges** | Biaya lalu lintas keluar dari cloud. |
| **Encryption (in-flight/at-rest)** | Enkripsi data saat transit / saat tersimpan. |
| **Erasure coding** | Teknik penyimpanan redundan (mirip RAID). |
| **etcd** | Basis data konfigurasi/state klaster Kubernetes. |
| **Eventual consistency** | Konsistensi yang tercapai *akhirnya* (mis. propagasi DNS). |
| **Four-eyes / Multiperson authentication** | Autentikasi yang memerlukan dua orang. |
| **Full backup** | Backup seluruh data. |
| **Garbage collection** | Proses penghapusan backup lama pada sistem dedup. |
| **GDPR / CCPA** | Kerangka hukum privasi UE / California (padanan Indonesia: UU PDP). |
| **Hash / hash table (dedupe index)** | Nilai unik konten / basis data semua hash. |
| **HCBA (Hyper-Converged Backup Appliance)** | Appliance backup *scale-out* berbasis Linux. |
| **HCI / CI** | *Hyper-Converged* / *Converged Infrastructure*. |
| **Hot backup mode** | Mode khusus basis data agar dapat di-backup saat hidup. |
| **HSM (Hierarchical Storage Management)** | Memindahkan data ke storage lebih murah seiring usia. |
| **Hypervisor / Guest OS** | Perangkat lunak penjalan VM / OS di dalam VM. |
| **Image-level backup / Image recovery** | Backup/pemulihan citra disk (mis. VMDK/VHD). |
| **Immediate (strong) consistency** | Semua pengguna melihat data sama pada saat yang sama. |
| **Immutability / WORM** | Ketidakberubahan data / *Write Once Read Many*. |
| **Incremental backup** | Backup hanya data yang berubah. |
| **Incremental forever** | Sistem yang tidak pernah lagi membutuhkan full backup. |
| **Inline / Post-process dedupe** | Dedup sebelum / sesudah ditulis ke disk. |
| **Instance / Tablespace / Partition / Shard** | Terminologi struktur basis data tradisional. |
| **Instant recovery** | Boot VM langsung dari backup tanpa restore tradisional. |
| **Item-level backup** | Backup tingkat item (mis. berkas). |
| **Least privilege** | Pemberian akses minimum yang diperlukan. |
| **Lift-and-shift** | Memindahkan VM apa adanya ke cloud tanpa *refactoring*. |
| **LTFS** | *Linear Tape File System* — tape sebagai filesystem, format independen-produk. |
| **LTO / TS11x0** | Teknologi tape utama. |
| **Media recovery / PITR** | Pemutaran ulang log untuk memajukan/menyelaraskan basis data. |
| **Moving target** | Tantangan: *data file* basis data berubah selama di-backup. |
| **MSP (Managed Service Provider)** | Penyedia yang menjalankan proteksi data atas nama Anda. |
| **Multiplexing** | Menjalin banyak backup menjadi satu aliran cepat (memperlambat restore). |
| **NDMP** | *Network Data Management Protocol* — protokol backup khusus NAS. |
| **Near-CDP** | Snapshot + replikasi = sistem proteksi data sah dengan titik pemulihan rapat. |
| **Noisy neighbor** | Masalah performa akibat banyak VM membebani I/O hypervisor serentak. |
| **Object storage** | Penyimpanan objek (UID berbasis hash); umumnya redundan & *self-healing*. |
| **Open bucket** | *Bucket object storage* yang dapat dibaca siapa saja (risiko keamanan). |
| **Overprovisioning** | Membeli kapasitas berlebih untuk mengantisipasi pertumbuhan. |
| **PEBKAC** | "*Problem Exists Between Keyboard And Chair*" — kesalahan pengguna. |
| **Persistent Volume (PV) / PVC** | Volume persisten / klaim volume di Kubernetes. |
| **RACI** | Kerangka tanggung jawab: *Responsible, Accountable, Collaborator, Informed*. |
| **RAID** | Teknik penyimpanan redundan yang melindungi terhadap kegagalan perangkat. |
| **Ransomware / RaaS** | Malware penuntut tebusan / *Ransomware-as-a-Service*. |
| **Recovery site** | Tempat pengganti lingkungan komputasi saat bencana. |
| **Redirect-on-write (RoW)** | Metode snapshot: tulis blok baru di lokasi lain, alihkan pointer. |
| **Rehydrate** | Mengembalikan data terdeduplikasi ke bentuk penuh. |
| **Referential integrity** | Integritas keterkaitan antar-data. |
| **Replication (sync/async/hybrid)** | Replikasi data; sinkron menjamin 100% sama, asinkron dapat tertinggal. |
| **Request pricing (GET/PUT)** | Biaya per operasi I/O object storage. |
| **Restore** | Mengembalikan satu hal ke satu titik waktu menggunakan backup. |
| **Retention** | Lama penyimpanan backup/archive (ditentukan organisasi). |
| **Retrieve** | Mengambil banyak data berbasis konten/metadata dari rentang tanggal lebar. |
| **Right to be forgotten** | Hak untuk dilupakan (penghapusan data pribadi). |
| **Rogue admin** | Administrator ber-hak istimewa yang menyalahgunakan akses. |
| **Rolling disaster** | Bencana berantai di mana satu sistem menulari sistem lain. |
| **RPO / RTO** | Sasaran titik pemulihan / sasaran waktu pemulihan (objektif). |
| **RPA / RTA** | Titik/waktu pemulihan aktual (terukur saat pemulihan). |
| **Scale-up / Scale-out** | Tumbuh dengan menambah disk / menambah node. |
| **Selective inclusion / exclusion** | Metode seleksi: sertakan eksplisit / kecualikan eksplisit (automatic inclusion). |
| **Separation of powers** | Pemisahan wewenang agar tak ada pihak yang dapat merusak sekaligus melindungi. |
| **Shoe-shining / Repositioning** | Tape bolak-balik karena aliran data terlalu lambat. |
| **Sizing** | Penentuan ukuran sistem backup. |
| **Snapshot (virtual)** | Salinan virtual yang bergantung pada volume sumber. |
| **Snap-and-sweep** | Backup via snapshot dari basis data lalu *sweep*. |
| **Sneakernet / Initial seed** | Pengiriman fisik appliance untuk backup pertama. |
| **Source / Target deduplication** | Dedup di klien / di appliance. |
| **Split replica** | Backup NoSQL dengan memisahkan replika yang mutakhir. |
| **Storage vMotion** | Fitur VMware memindahkan VM yang sedang berjalan. |
| **Stub** | Penanda/pointer yang ditinggalkan HSM di sistem sumber. |
| **Synchronous replication** | Replikasi sebelum ACK; sumber & target selalu 100% sama. |
| **Synthetic full backup** | Backup berperilaku full tanpa full backup sesungguhnya. |
| **TCO (Total Cost of Ownership)** | Total biaya kepemilikan (bukan sekadar akuisisi). |
| **Tower of Hanoi (TOH)** | Skema level backup agar berkas ter-backup ganda. |
| **Transaction log (redo/binary log/WAL)** | Catatan transaksi untuk recovery basis data. |
| **USP (Unique Selling Proposition)** | Alasan unik memilih suatu solusi. |
| **VADP** | *vSphere Storage APIs for Data Protection*. |
| **VSS / VSS writer** | *Volume Shadow Copy Service* dan komponen per-aplikasinya. |
| **VTL (Virtual Tape Library)** | Disk yang berpura-pura menjadi tape library. |
| **Wetware** | "Konfigurasi/manusia" — sering jadi akar masalah backup. |
| **Write coalescing** | Menggabungkan beberapa tulisan saat replikasi tertinggal jauh. |

---

## Daftar Pustaka

### Sumber Utama

1. Preston, W. Curtis. (2021). *Modern Data Protection: Ensuring Recoverability of All Modern Workloads*. Sebastopol, CA: O'Reilly Media, Inc. Edisi Pertama (Mei 2021). ISBN: 978-1-492-09405-0.
   - *Seluruh isi buku ajar ini disusun berdasarkan buku sumber tersebut. Kontributor bab dalam buku sumber: Bab 2 oleh Jeff Rochlin; Bab 10 oleh Dan Frith (@penguinpunk). Kata Pengantar (Foreword) oleh Chris Mellor (Editor, Blocks & Files).*

### Konsep, Standar, dan Rujukan yang Disebut dalam Buku Sumber

Daftar berikut adalah konsep, aturan, teknologi, dan kerangka hukum yang **disebut secara eksplisit** dalam buku sumber dan dibahas dalam buku ajar ini. Daftar ini tidak mengklaim sumber primer di luar yang dirujuk penulis.

2. **Aturan 3-2-1 (The 3-2-1 Rule)** — prinsip fundamental backup (tiga versi, dua media, satu di tempat lain) yang dirujuk penulis di hampir seluruh bab.
3. **RTO/RPO dan RTA/RPA** — metrik pemulihan (objektif dan aktual) yang menjadi penggerak desain proteksi data.
4. **RAID dan Erasure Coding** — teknik penyimpanan redundan yang dibahas sebagai pelindung kegagalan perangkat (bukan pengganti backup).
5. **Tower of Hanoi (TOH) backup schedule** — skema rotasi level backup; rujukan permainan matematis disebut penulis (http://www.math.toronto.edu/mathnet/games/towers.html).
6. **GDPR (General Data Protection Regulation)** — kerangka hukum privasi Uni Eropa, termasuk *right to be forgotten*, yang disebut terkait retensi backup/archive.
7. **CCPA (California Consumer Privacy Act)** — undang-undang privasi California yang disebut terkait pelaporan data pelanggan di backup.
8. **Algoritma hashing kriptografis (SHA-1, SHA-2, SHA-256)** — dasar deduplikasi dan identifikasi objek (UID) pada object storage.
9. **Teknologi tape (LTO, IBM TS11x0, LTFS)** dan nilai **UBER** — dirujuk dalam pembahasan keandalan dan retensi jangka panjang.
10. **API & teknologi virtualisasi (VMware VADP, VCB; Windows VSS; CBT; Hyper-V)** — dirujuk dalam backup tingkat hypervisor.
11. **Layanan cloud yang disebut sebagai contoh** (AWS EC2/EBS/S3/RDS/DynamoDB/Aurora, Azure Blob, Google Cloud Storage, VMware Cloud) — disebut penulis sebagai ilustrasi, bukan endorsemen.
12. **db-engines.com** — dirujuk penulis untuk klasifikasi model dan produk basis data.
13. **Backup Central & podcast "Restore It All"** — sumber pembaruan pasca-publikasi yang disebut penulis (backupcentral.com).
14. Preston, W. Curtis. *Backup & Recovery*. O'Reilly Media — buku terdahulu penulis yang dirujuk untuk topik *bare-metal recovery* dan alat backup open source.

### Rujukan Kontekstual (Adaptasi Indonesia — bukan bagian dari buku sumber)

15. **Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** — disebut dalam buku ajar ini sebagai padanan kontekstual GDPR/CCPA untuk pembaca di Indonesia. Rujukan ini ditambahkan untuk keperluan adaptasi pedagogis dan **bukan** bagian dari buku sumber.

---

> **Catatan Akhir Kepatuhan:** Buku ajar ini adalah penyajian ulang (parafrasa, ringkasan, dan penataan pedagogis) atas isi buku *Modern Data Protection* karya W. Curtis Preston (O'Reilly Media, 2021). Seluruh konsep teknis, contoh, dan opini bersumber dari naskah asli; opini yang merupakan sikap pribadi penulis diatribusikan secara eksplisit. Tidak ada klaim vendor, angka, atau spesifikasi yang dikarang. Konten telah disusun ulang demi kepatuhan terhadap pembatasan lisensi, dengan tetap menjaga akurasi faktual dan substansi argumen penulis sumber. Penambahan konteks Indonesia (mis. UU PDP, Cincin Api) ditandai secara eksplisit sebagai adaptasi dan bukan bagian dari buku sumber.

*— Selesai —*
