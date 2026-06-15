# SOAL UJIAN AKHIR SEMESTER (UAS)
## Internet of Things — Kelas Mat-D
### Semester Genap 2025/2026

---

| | |
|---|---|
| **Mata Kuliah** | Internet of Things |
| **Kelas** | Mat-D |
| **Hari/Tanggal** | _________________________ |
| **Waktu** | 120 menit |
| **Sifat Ujian** | Tutup Buku |
| **Dosen** | _________________________ |

---

## PETUNJUK UMUM

1. Tuliskan **nama lengkap** dan **NIM** pada setiap lembar jawaban.
2. Kerjakan **seluruh soal** — tidak ada pilihan soal.
3. Soal terdiri atas **2 bagian**:
   - **Bagian A** — 5 soal Pilihan Ganda (masing-masing **4 poin**)
   - **Bagian B** — 10 soal Uraian (masing-masing **8 poin**)
4. **Total nilai = 100 poin.**
5. Kerjakan soal uraian dengan **terstruktur dan argumentatif** — jawaban singkat tanpa penjelasan tidak akan mendapat poin penuh.
6. Dilarang menggunakan perangkat elektronik apapun.
7. Dilarang bekerja sama. Pelanggaran mengakibatkan nilai **0**.

---

---

# BAGIAN A — PILIHAN GANDA
### (5 soal × 4 poin = 20 poin)

> **Petunjuk:** Pilih **satu** jawaban yang paling tepat. Lingkari atau tuliskan huruf jawaban pada lembar jawaban.

---

**A1.** Sebuah perangkat IoT mengirimkan data sensor suhu setiap 5 detik ke broker MQTT. Untuk memastikan setiap pesan **dijamin diterima tepat satu kali** (*exactly-once delivery*) — tidak kurang dan tidak lebih — level QoS yang harus digunakan adalah...

- **a)** QoS 0 — *At most once* (Fire and Forget)
- **b)** QoS 1 — *At least once* (bisa duplikat)
- **c)** QoS 2 — *Exactly once* (handshake 4 langkah)
- **d)** QoS 3 — *Guaranteed once* (enkripsi penuh)

---

**A2.** Pada arsitektur IoT **5-layer**, terdapat layer yang bertugas menerjemahkan data mentah dari perangkat fisik ke format yang dapat dikomunikasikan ke layer di atasnya, sekaligus berfungsi sebagai *gateway* antar-perangkat. Layer tersebut adalah...

- **a)** *Objects Layer* (Perception Layer)
- **b)** *Object Abstraction Layer*
- **c)** *Service Management Layer*
- **d)** *Application Layer*

---

**A3.** Perhatikan skenario berikut: *"Seorang penyerang membanjiri gateway IoT sebuah rumah sakit dengan jutaan paket palsu sehingga gateway tidak mampu memproses data dari monitor pasien ICU."*

Serangan ini merupakan ancaman terhadap aspek **mana** dari prinsip CIA (*Confidentiality, Integrity, Availability*)?

- **a)** Confidentiality (Kerahasiaan)
- **b)** Integrity (Integritas)
- **c)** Availability (Ketersediaan)
- **d)** Authentication (Autentikasi)

---

**A4.** Dalam sistem komunikasi IoT yang aman, dikenal konsep **enkripsi hibrida** (*hybrid encryption*). Pernyataan yang **paling tepat** menggambarkan enkripsi hibrida adalah...

- **a)** Menggunakan dua algoritma enkripsi simetris secara bergantian untuk menggandakan keamanan
- **b)** Menggunakan enkripsi asimetris (RSA/ECC) untuk menukar kunci sesi, lalu enkripsi simetris (AES) untuk mengenkripsi data payload
- **c)** Menggunakan hash (SHA-256) dikombinasikan dengan digital signature untuk memverifikasi integritas data
- **d)** Menggunakan VPN tunnel dan firewall secara bersamaan pada lapisan jaringan

---

**A5.** Pada **Triple Layered Business Model Canvas (TLBMC)**, dimensi **Lingkungan (*Environmental*)** mengevaluasi bisnis dari perspektif...

- **a)** Struktur biaya operasional dan aliran pendapatan (*revenue streams*) perusahaan
- **b)** Hubungan antar-pemangku kepentingan dan kanal distribusi produk
- **c)** Dampak ekologis, jejak karbon, penggunaan sumber daya alam, dan keberlanjutan (*sustainability*)
- **d)** Nilai sosial yang diciptakan untuk komunitas lokal dan karyawan perusahaan

---

---

# BAGIAN B — SOAL URAIAN
### (10 soal × 8 poin = 80 poin)

> **Petunjuk:** Jawab setiap soal secara **terstruktur, lengkap, dan mendalam**. Sertakan istilah teknis yang tepat. Poin diberikan per sub-pertanyaan sesuai bobot yang tercantum.

---

## SOAL B1 — Arsitektur IoT & Edge Computing
**(8 poin)**

Sebuah perusahaan manufaktur otomotif ingin mengimplementasikan sistem **Predictive Maintenance** berbasis IoT di pabrik yang memiliki **500 mesin produksi**. Setiap mesin dipasang **8 sensor** (suhu, getaran, arus listrik, tekanan oli, kelembaban, RPM, torsi, emisi gas). Data harus diproses dalam waktu **< 50 milidetik** untuk mencegah kerusakan mesin yang bisa mengakibatkan kerugian miliaran rupiah.

**(a)** Rancang arsitektur IoT lengkap dengan memanfaatkan tiga lapisan komputasi: **Edge Computing** (pada mesin), **Fog Computing** (pada area pabrik), dan **Cloud Computing** (pusat data). Jelaskan fungsi spesifik dan komponen perangkat keras yang dibutuhkan di masing-masing lapisan. **(3 poin)**

**(b)** Jelaskan **alur data lengkap** dari sensor hingga ke dashboard engineering, termasuk protokol komunikasi yang paling tepat di setiap segmen (*sensor ke edge*, *edge ke fog*, *fog ke cloud*). Berikan **justifikasi teknis** mengapa protokol tersebut dipilih dibandingkan alternatifnya. **(3 poin)**

**(c)** Identifikasi **minimal 3 tantangan kritis** dalam implementasi sistem ini (teknis maupun operasional), dan jelaskan solusi konkret untuk masing-masing tantangan tersebut. **(2 poin)**

---

## SOAL B2 — Keamanan IoT Multi-Layer
**(8 poin)**

Sebuah sistem **Smart Hospital** memiliki **2.000 perangkat IoT** yang terhubung ke jaringan intranet rumah sakit, terdiri dari: monitor denyut jantung pasien ICU, infusion pump otomatis (mengatur dosis obat), kamera CCTV ruang operasi, dan sensor lingkungan (suhu, kelembaban, sterilitas ruangan).

Pada suatu hari, tim keamanan mendeteksi aktivitas anomali: ada perangkat yang mengirimkan data ke IP eksternal yang tidak dikenal.

**(a)** Identifikasi dan analisis **4 vektor serangan paling kritis** yang mungkin terjadi pada sistem ini. Untuk setiap vektor, jelaskan dampaknya terhadap aspek **CIA** (*Confidentiality, Integrity, Availability*) dan konsekuensi nyata bagi keselamatan pasien. **(3 poin)**

**(b)** Rancang strategi pertahanan **defense-in-depth** berlapis yang mencakup: *network segmentation*, *device authentication*, *enkripsi komunikasi end-to-end*, dan *intrusion detection system (IDS)*. Jelaskan bagaimana lapisan-lapisan ini saling melengkapi. **(3 poin)**

**(c)** Jelaskan perbedaan fundamental antara **Data Security** dan **Data Privacy** dalam konteks sistem ini. Berikan **1 contoh konkret pelanggaran** untuk masing-masing, beserta implikasi hukumnya di Indonesia. **(2 poin)**

---

## SOAL B3 — Desain Sistem IoT Kritis
**(8 poin)**

Pemerintah Kota Semarang menugaskan Anda sebagai konsultan untuk merancang **Smart Flood Early Warning System (SFEWS)** terintegrasi guna melindungi 1 juta penduduk dari banjir rob. Sistem harus mampu memberikan **peringatan dini minimal 45 menit** sebelum banjir tiba, bekerja 24/7/365, dan **tetap berfungsi saat infrastruktur jaringan sebagian rusak** akibat banjir itu sendiri.

**(a)** Rancang arsitektur sistem secara lengkap: tentukan **jenis dan jumlah sensor** yang dibutuhkan, **topologi jaringan** (termasuk teknologi komunikasi yang tahan banjir), **infrastruktur server**, dan **antarmuka pengguna** (untuk operator dan warga). Narasi dalam format terstruktur dengan flow data yang jelas. **(3 poin)**

**(b)** Bagaimana sistem Anda menjamin keandalan **99,9% uptime** (maksimal downtime ~8,7 jam/tahun), mengingat banjir justru dapat merusak sensor dan jaringan komunikasi? Rancang strategi **redundansi** dan **failover otomatis** yang komprehensif. **(3 poin)**

**(c)** Analisis dampak implementasi sistem ini menggunakan kerangka **Triple Layered BMC** — aspek Ekonomi (siapa yang bayar, nilai bisnis), Lingkungan (dampak ekologis), dan Sosial (dampak bagi masyarakat, khususnya kelompok rentan). **(2 poin)**

---

## SOAL B4 — Protokol & Komunikasi IoT
**(8 poin)**

Sebuah startup agritech mengembangkan sistem **Precision Agriculture IoT** untuk monitoring kebun kelapa sawit di Kalimantan. Lahan seluas **5.000 hektar** tersebar di daerah terpencil tanpa infrastruktur internet kabel. Sistem membutuhkan **2.000 sensor node** (kelembaban tanah, pH, suhu udara, intensitas cahaya) dengan target daya tahan baterai **minimal 2 tahun**.

**(a)** Bandingkan secara mendalam **3 teknologi komunikasi nirkabel**: **LoRaWAN**, **NB-IoT**, dan **Zigbee Mesh** untuk skenario ini. Evaluasi berdasarkan 5 dimensi: jangkauan, konsumsi daya, bandwidth, biaya implementasi, dan ketersediaan infrastruktur. Tentukan **rekomendasi akhir** beserta justifikasinya. **(3 poin)**

**(b)** Jelaskan secara mendalam mekanisme kerja protokol **MQTT** meliputi: arsitektur broker-client, mekanisme *publish/subscribe*, hierarki topic (berikan contoh skema topic untuk skenario ini), perbedaan QoS 0/1/2, dan fitur *Last Will and Testament (LWT)*. Bagaimana MQTT mengoptimalkan konsumsi bandwidth dibanding HTTP/REST? **(3 poin)**

**(c)** Rancang **skema topologi jaringan lengkap** yang menggabungkan teknologi pilihan Anda dengan gateway lapangan, *backhaul* ke internet, dan server cloud. Identifikasi titik-titik kritis jaringan dan strategi mitigasinya. **(2 poin)**

---

## SOAL B5 — Kriptografi & Autentikasi IoT
**(8 poin)**

Sistem **Smart Grid** nasional menggunakan **500.000 smart meter** yang berkomunikasi dengan pusat kendali PLN setiap 15 menit. Data yang ditransmisikan mencakup: konsumsi listrik real-time, status perangkat, dan perintah kontrol (remote disconnect/reconnect). Keamanan menjadi sangat kritis karena manipulasi data dapat menyebabkan pemadaman listrik massal.

**(a)** Jelaskan mekanisme kerja serangan **replay attack** pada smart meter IoT. Bagaimana kombinasi **timestamp** + **nonce** + **sequence number** dapat mencegah serangan ini secara efektif? Berikan ilustrasi alur serangan dan pencegahannya. **(2 poin)**

**(b)** Rancang skema **mutual authentication** (autentikasi dua arah) antara smart meter dan server PLN menggunakan **Public Key Infrastructure (PKI)**. Jelaskan langkah-langkah lengkap: pembuatan sertifikat, proses handshake TLS/DTLS, verifikasi identitas kedua pihak, dan manajemen Certificate Revocation List (CRL). **(4 poin)**

**(c)** Smart meter menggunakan mikrokontroler dengan sumber daya komputasi terbatas (CPU 32-bit, RAM 256KB). Jelaskan mengapa **ECC (Elliptic Curve Cryptography)** lebih disukai daripada **RSA** untuk perangkat ini, dan bagaimana **enkripsi hibrida** (ECC + AES-128) bekerja dalam satu sesi komunikasi. **(2 poin)**

---

## SOAL B6 — Analisis Kegagalan & Fault Tolerance
**(8 poin)**

Sistem monitoring kualitas air di **50 titik sungai** di Jawa Tengah mengalami **kegagalan total selama 72 jam** akibat rentetan kejadian: (1) gateway utama di Semarang terkena petir dan mati, (2) server cloud mengalami downtime maintenance tidak terjadwal, (3) 12 sensor rusak akibat banjir bandang, (4) operator tidak mendapat notifikasi apapun karena sistem alerting ikut mati.

**(a)** Lakukan **Root Cause Analysis (RCA)** menggunakan metode **5 Whys** atau **Fishbone Diagram** terhadap kegagalan ini. Identifikasi **Single Points of Failure (SPOF)** yang seharusnya sudah diantisipasi sejak tahap desain. **(2 poin)**

**(b)** Rancang ulang arsitektur sistem dengan menerapkan prinsip-prinsip **fault tolerance** berikut: (i) redundansi gateway aktif-pasif, (ii) *local data buffering* pada setiap sensor node, (iii) mekanisme *failover* otomatis dengan waktu recovery < 5 menit, (iv) sistem alerting multi-channel yang independen dari infrastruktur utama, dan (v) *watchdog timer* pada perangkat keras. Jelaskan bagaimana setiap mekanisme bekerja. **(4 poin)**

**(c)** Bagaimana strategi **data recovery** untuk 72 jam data yang hilang? Pertimbangkan: kemampuan buffering data di sensor (storage lokal), rekonstruksi data melalui interpolasi, dan **SOP (Standard Operating Procedure)** pemulihan pasca-insiden. **(2 poin)**

---

## SOAL B7 — Integrasi AI dan IoT
**(8 poin)**

Sebuah **Smart Building** perkantoran 20 lantai di Jakarta mengintegrasikan IoT dengan kecerdasan buatan untuk mengoptimalkan konsumsi energi sistem **HVAC** (pendingin udara), pencahayaan, lift, dan peralatan kantor. Tagihan listrik ditargetkan turun **30%** tanpa mengurangi kenyamanan penghuni.

**(a)** Jelaskan perbedaan pendekatan dan trade-off antara **Cloud AI**, **Fog AI**, dan **Edge AI** dalam konteks optimasi energi gedung ini. Untuk setiap pendekatan, jelaskan: di mana komputasi dilakukan, latensi respons, ketahanan terhadap koneksi internet terputus, dan contoh use case yang cocok. **(3 poin)**

**(b)** Rancang **pipeline Machine Learning** end-to-end untuk memprediksi kebutuhan energi per zona gedung per jam ke depan. Jelaskan: (i) fitur input yang relevan (sebutkan minimal 6 fitur), (ii) arsitektur model yang tepat (*time-series forecasting*), (iii) proses training dan validasi, dan (iv) strategi deployment ke edge device dengan sumber daya terbatas (*model compression/quantization*). **(3 poin)**

**(c)** Identifikasi **2 risiko keamanan spesifik** yang muncul akibat mengintegrasikan model AI pada perangkat edge IoT: **adversarial attack** (manipulasi input sensor untuk menipu model) dan **model poisoning** (manipulasi proses training). Jelaskan mekanisme serangan dan langkah mitigasinya. **(2 poin)**

---

## SOAL B8 — Regulasi, Privasi & Etika IoT
**(8 poin)**

Sebuah perusahaan teknologi merancang sistem **Smart City** di Surabaya yang mengintegrasikan **300.000 sensor dan kamera** di seluruh kota: kamera CCTV dengan kemampuan *facial recognition*, sensor pergerakan, pelacak kendaraan, dan sensor suara di ruang publik. Data dikumpulkan real-time dan disimpan di data center selama 5 tahun.

**(a)** Analisis kepatuhan sistem ini terhadap **Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)** Indonesia. Identifikasi **minimal 4 potensi pelanggaran konkret** dan usulkan **solusi teknis-arsitektural** untuk masing-masing. **(3 poin)**

**(b)** Jelaskan konsep **Privacy by Design (PbD)** dan bagaimana **7 prinsip PbD** diterapkan pada arsitektur sistem IoT ini sejak tahap perancangan. Fokuskan pada: *data minimization*, *purpose limitation*, *anonymization/pseudonymization*, dan *user consent management*. **(3 poin)**

**(c)** Terdapat dilema etika yang mendasar: *penggunaan facial recognition dapat membantu menangkap kriminal dan meningkatkan keamanan publik, namun sekaligus melanggar hak privasi seluruh warga yang melintas*. Diskusikan dilema ini menggunakan **minimal 2 framework etika** (misalnya: utilitarianisme, deontologi, atau virtue ethics) dan usulkan kebijakan teknis yang dapat menyeimbangkan kedua kepentingan tersebut. **(2 poin)**

---

## SOAL B9 — Skalabilitas & Manajemen Perangkat IoT
**(8 poin)**

Sebuah perusahaan telekomunikasi nasional mengelola platform IoT dengan **10 juta perangkat aktif** yang tersebar di seluruh Indonesia. Setiap perangkat mengirimkan telemetri setiap 30 detik. Setiap hari, **100.000 perangkat (1%)** perlu mendapatkan pembaruan firmware (*OTA update*) karena patch keamanan kritis.

**(a)** Rancang sistem **Device Lifecycle Management (DLM)** yang mencakup: (i) *device provisioning* aman (zero-touch provisioning), (ii) monitoring kesehatan perangkat real-time dengan anomaly detection, (iii) manajemen *OTA firmware update* bertahap (*staged rollout* dengan canary deployment), dan (iv) prosedur *device decommissioning* yang aman. **(3 poin)**

**(b)** Rancang arsitektur **back-end** yang mampu menangani **10 juta koneksi konkuren** dan **20 juta pesan/menit** dengan latensi < 200ms. Jelaskan: peran *message broker* (MQTT cluster), *time-series database*, strategi *horizontal scaling* dan *load balancing*, serta arsitektur *microservices* yang relevan. **(3 poin)**

**(c)** Bagaimana memastikan keamanan proses **OTA firmware update** untuk mencegah **supply chain attack** (distribusi firmware palsu/berbahaya)? Jelaskan mekanisme lengkap: *code signing* dengan kunci privat vendor, verifikasi *hash* di perangkat, *secure boot*, dan prosedur *rollback* otomatis jika firmware baru menyebabkan kegagalan. **(2 poin)**

---

## SOAL B10 — Inovasi, Desain Sistem, & Business Model
**(8 poin)**

Anda adalah **co-founder** sebuah startup yang akan mempresentasikan produk IoT kepada panel investor senilai Rp 5 miliar. Produk Anda bernama **"NutriSense"** — sistem monitoring dan otomatisasi **hidroponik cerdas** berbasis IoT untuk segmen *urban farming* perkotaan. NutriSense menargetkan dua segmen: (A) rumah tangga yang ingin menanam sayuran sendiri, dan (B) restoran/hotel yang ingin memiliki kebun vertikal indoor.

**(a)** Rancang arsitektur teknis **NutriSense** secara lengkap dan konkret. Tentukan: (i) minimal **6 jenis sensor** beserta justifikasi fungsinya, (ii) platform hardware (MCU/SBC) dengan alasan pemilihan, (iii) protokol komunikasi dan konektivitas, (iv) infrastruktur cloud dan database, serta (v) fitur aplikasi mobile yang membedakan NutriSense dari kompetitor. **(3 poin)**

**(b)** Kembangkan **Triple Layered Business Model Canvas (TLBMC) lengkap** untuk NutriSense:
- **Aspek Ekonomi:** proposisi nilai, segmen pelanggan, aliran pendapatan (minimal 3 stream berbeda), struktur biaya, mitra kunci, dan saluran distribusi.
- **Aspek Lingkungan:** dampak positif/negatif ekologis, penggunaan air vs pertanian konvensional, jejak karbon, dan strategi keberlanjutan.
- **Aspek Sosial:** dampak pada ketahanan pangan perkotaan, aksesibilitas (siapa yang bisa/tidak bisa menjangkau), dampak pada lapangan kerja pertanian tradisional, dan nilai komunitas.
**(3 poin)**

**(c)** Identifikasi **3 risiko terbesar** yang mengancam keberlangsungan NutriSense (bukan hanya risiko teknis — pertimbangkan juga risiko pasar, regulasi, dan model bisnis). Untuk setiap risiko, rancang strategi **mitigasi konkret** yang meyakinkan investor. **(2 poin)**

---

---

## LEMBAR JAWABAN

> Tulis jawaban di bawah masing-masing soal atau di lembar terpisah yang telah diberi label soal.

| Bagian | Soal | Bobot | Nilai Diperoleh |
|--------|------|-------|-----------------|
| A | A1–A5 | 20 | |
| B | B1 | 8 | |
| B | B2 | 8 | |
| B | B3 | 8 | |
| B | B4 | 8 | |
| B | B5 | 8 | |
| B | B6 | 8 | |
| B | B7 | 8 | |
| B | B8 | 8 | |
| B | B9 | 8 | |
| B | B10 | 8 | |
| | **TOTAL** | **100** | |

---

*Dokumen ini dibuat untuk keperluan akademik Mata Kuliah Internet of Things, Kelas Mat-D, Semester Genap 2025/2026.*
