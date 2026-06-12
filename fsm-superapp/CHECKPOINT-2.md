# CHECKPOINT-2 — Matriks Pengujian Komprehensif FSM LAPOR!

> **Tanggal:** Juni 2026  
> **Versi Aplikasi:** 0.2.0  
> **Tujuan:** Panduan pengujian manual/otomatis yang mencakup seluruh kombinasi
> role, unit, jabatan, dan skill/tag yang mungkin terjadi di lingkungan produksi.

---

## Referensi Master Data Pengujian

### Role
| Kode | Nama | Deskripsi |
|------|------|-----------|
| `SA` | Superadmin | Akses penuh ke seluruh sistem |
| `PIM` | Pimpinan | Menerima, menugaskan, memverifikasi tiket |
| `PET` | Petugas | Mengerjakan tugas, mengelola aset |
| `PEL` | Pelapor | Membuat dan memantau tiket sendiri |

### Unit (Fakultas & Direktorat)
| Kode | Nama Unit |
|------|-----------|
| `FAK` | Tingkat Fakultas (induk) |
| `AKADEMIK` | Unit Akademik & Kemahasiswaan |
| `SUMBERDAYA` | Unit Sumber Daya |
| `INFO` | Jurusan Informatika |
| `FISIKA` | Jurusan Fisika |
| `BIO` | Jurusan Biologi |
| `BIOTEK` | Jurusan Bioteknologi |
| `KIM` | Jurusan Kimia |
| `STAT` | Jurusan Statistika |
| `MAT` | Jurusan Matematika |

### Jabatan
| Kode | Nama Jabatan |
|------|-------------|
| `DKN` | Dekan |
| `WDSD` | Wakil Dekan Sumber Daya |
| `WDAK` | Wakil Dekan Akademik & Kemahasiswaan |
| `MGR` | Manajer |
| `SPVSD` | Supervisor Sumber Daya |
| `SPVAK` | Supervisor Akademik & Kemahasiswaan |
| `KORD` | Koordinator (Koordinator Laboratorium, dll.) |

### Skill / Tag Petugas
| Kode | Nama Skill | Warna |
|------|-----------|-------|
| `IT` | IT & Komputer | #0284c7 |
| `NET` | Internet & Jaringan | #0891b2 |
| `SND` | Sound System & AV | #7c3aed |
| `ELK` | Elektrikal & Listrik | #d97706 |
| `AC` | AC & HVAC | #16a34a |
| `KBR` | Kebersihan & Sanitasi | #65a30d |
| `KMN` | Keamanan & CCTV | #dc2626 |
| `CIV` | Sipil & Bangunan | #6b7280 |
| `GDG` | Gedung & Fasilitas | #ca8a04 |
| `KDR` | Kendaraan & Transportasi | #ea580c |

### Jenis Tiket (Kategori)
| Kode | Nama | Flag Penting |
|------|------|-------------|
| `CAT-IT` | Gangguan IT / Komputer | `requires_asset=true` |
| `CAT-NET` | Gangguan Jaringan Internet | — |
| `CAT-SND` | Sound System / AV | `self_executable=true` |
| `CAT-ELK` | Kelistrikan | `requires_pimpinan_verification=true` |
| `CAT-AC` | AC / Pendingin Ruangan | `requires_asset=true` |
| `CAT-KBR` | Kebersihan | `self_executable=true` |
| `CAT-CIV` | Kerusakan Bangunan | `requires_pimpinan_verification=true` |
| `CAT-GDG` | Fasilitas Gedung Umum | — |

### Jenis Pelapor
| Kode | Nama |
|------|------|
| `RT-DOS` | Dosen |
| `RT-MHS` | Mahasiswa |
| `RT-TEN` | Tenaga Kependidikan |
| `RT-UMM` | Umum |

---

## KELOMPOK A — Autentikasi & Akses Awal

### A1 — Login & Routing Role

| TC# | Aktor | Aksi | Data Uji | Hasil yang Diharapkan |
|-----|-------|------|----------|-----------------------|
| A-01 | Pelapor (mahasiswa) | Login via email/password | Email valid, password benar | Masuk → `/dashboard`, tile hanya: Tiket |
| A-02 | Pelapor (dosen) | Login via SSO UNDIP | Akun `@undip.ac.id` aktif | Redirect ke dashboard, reporter_type terdeteksi otomatis sebagai Dosen |
| A-03 | Petugas (IT, Unit Informatika) | Login via email | Akun aktif, role petugas | Dashboard menampilkan tile: Tiket, Tugas Saya, Buat Tugas, Manajemen Aset, Lihat Aset |
| A-04 | Pimpinan (Dekan) | Login via email | Akun aktif, role pimpinan | Dashboard menampilkan tile: Tiket, Dashboard SLA, Dashboard Biaya, Kondisi Aset, Monitoring Petugas |
| A-05 | Superadmin | Login via username | Username + password superadmin | Redirect ke `/dashboard`, semua tile muncul termasuk menu superadmin |
| A-06 | Superadmin | Login via email biasa | Akun tidak punya role superadmin | Gagal login, pesan "Akun ini bukan superadmin" |
| A-07 | Pelapor | Akses langsung `/superadmin/categories` | Tidak ada rule akses | Redirect ke `/dashboard` |
| A-08 | Petugas | Akses langsung `/dashboard/sla` | Tidak ada rule akses | Redirect ke `/dashboard` |
| A-09 | Pelapor | Akses langsung `/tugas-saya` | Role pelapor saja | Redirect ke `/dashboard` |
| A-10 | Semua role | Akses `/dashboard` tanpa login | Sesi belum ada | Redirect ke `/login` |

### A2 — Register & Reset Password

| TC# | Aktor | Aksi | Data Uji | Hasil yang Diharapkan |
|-----|-------|------|----------|-----------------------|
| A-11 | Calon pelapor baru | Register akun baru | Email baru, nama lengkap, password ≥6 karakter | Akun dibuat, email verifikasi terkirim |
| A-12 | Calon pelapor | Register email duplikat | Email yang sudah terdaftar | Pesan "EMAIL_ALREADY_REGISTERED" dengan opsi ke Login / Lupa Password |
| A-13 | User manapun | Lupa password | Email terdaftar | Email reset terkirim, halaman konfirmasi tampil |
| A-14 | User manapun | Reset password via link | Password baru ≥6 karakter, cocok | Password berhasil diubah, diarahkan ke login |

---

## KELOMPOK B — Pembuatan Tiket (Pelapor)

### B1 — Buat Tiket Normal

| TC# | Aktor | Unit | Jenis Pelapor | Kategori | Flag | Hasil yang Diharapkan |
|-----|-------|------|---------------|----------|------|-----------------------|
| B-01 | Pelapor mahasiswa | Informatika | `RT-MHS` | `CAT-NET` (Jaringan) | — | Tiket terkirim, status `dikirim`, nomor tiket `LPR-YYYY-NNNNNN` terbuat |
| B-02 | Pelapor dosen | Fisika | `RT-DOS` | `CAT-SND` (Sound System) | `self_executable` | Tiket terkirim; setelah diterima pimpinan, otomatis ditugaskan ke pelapor sendiri |
| B-03 | Pelapor tenaga kependidikan | Sumber Daya | `RT-TEN` | `CAT-KBR` (Kebersihan) | `self_executable` | Tiket terkirim, foto opsional (photo_required=false), keterangan wajib |
| B-04 | Pelapor mahasiswa | Biologi | `RT-MHS` | `CAT-IT` (IT) | `requires_asset` | Picker aset muncul wajib, tiket tidak bisa submit tanpa memilih aset |
| B-05 | Pelapor dosen | Kimia | `RT-DOS` | `CAT-AC` (AC) | `requires_asset` | Picker aset gedung Kimia muncul, SLA dapat dipilih |
| B-06 | Pelapor | Matematika | `RT-MHS` | `CAT-ELK` (Listrik) | `requires_pimpinan_verification` | Tiket terkirim, setelah selesai perlu verifikasi pimpinan |
| B-07 | Pelapor | Statistika | `RT-MHS` | `CAT-CIV` (Bangunan) | `requires_pimpinan_verification` | Tiket terkirim dengan foto wajib dan keterangan wajib |
| B-08 | Pelapor | Bioteknologi | `RT-DOS` | `CAT-GDG` (Fasilitas) | — | Tiket terkirim tanpa aset, SLA dipilih, lokasi GPS tercatat |
| B-09 | Pelapor | Akademik | `RT-TEN` | `CAT-NET` | — | Tiket terkirim, pelapor dapat melihat di "Tiket Saya" |
| B-10 | Superadmin | Semua unit | Semua jenis | Semua kategori | — | Superadmin bisa membuat tiket dari kategori apapun tanpa batasan jenis pelapor |

### B2 — Validasi & Edge Case Pembuatan Tiket

| TC# | Skenario | Kondisi | Hasil yang Diharapkan |
|-----|----------|---------|----------------------|
| B-11 | Submit tanpa foto | `photo_required=true` | Tombol submit disabled, pesan error foto wajib |
| B-12 | Submit tanpa kategori | Belum pilih jenis tiket | Tombol submit disabled |
| B-13 | Submit tanpa aset | `requires_asset=true`, aset belum dipilih | Tombol submit disabled |
| B-14 | Submit tanpa keterangan | `description_required=true` | Tombol submit disabled |
| B-15 | Kategori `allow_pelapor_create=false` | Pelapor coba pilih kategori petugas-only | Kategori tidak muncul di dropdown pelapor |
| B-16 | GPS tidak tersedia | Browser menolak izin lokasi | Tiket tetap bisa submit, lokasi kosong, pesan status GPS gagal |

---

## KELOMPOK C — Alur Workflow Tiket

### C1 — Menerima Tiket (Pimpinan / Superadmin)

| TC# | Aktor | Jabatan | Unit | Kategori Tiket | Hasil yang Diharapkan |
|-----|-------|---------|------|----------------|-----------------------|
| C-01 | Pimpinan | Dekan | Fakultas | `CAT-NET` (Jaringan) | Tombol "Terima" tersedia, setelah klik status → `diterima` |
| C-02 | Pimpinan | WD Sumber Daya | Sumber Daya | `CAT-ELK` (Listrik) | Terima tiket bidang sumber daya, status → `diterima` |
| C-03 | Pimpinan | WD Akademik | Akademik | `CAT-SND` (Sound System) | Terima tiket akademik → status `diterima`, karena `self_executable` langsung `ditugaskan` ke pelapor |
| C-04 | Pimpinan | Manajer | Sumber Daya | `CAT-KBR` (Kebersihan) | Terima → status `diterima` lalu `ditugaskan` ke pelapor (self_executable) |
| C-05 | Superadmin | — | Semua | Semua kategori | Bisa menerima tiket apapun, status → `diterima` |
| C-06 | Petugas | — | Informatika | `CAT-IT` | **Tidak bisa** menerima (tombol Terima tidak tampil untuk petugas) |
| C-07 | Pelapor | — | Fisika | `CAT-CIV` | **Tidak bisa** menerima (tidak ada aksi menerima untuk pelapor) |

### C2 — Menugaskan Tiket

| TC# | Aktor | Jabatan | Tag Petugas | Kategori Tiket | Tag Kategori | Hasil yang Diharapkan |
|-----|-------|---------|-------------|----------------|--------------|-----------------------|
| C-08 | Pimpinan | Dekan | — | `CAT-IT` | Tag: IT | Dropdown petugas hanya tampilkan petugas bertag IT aktif |
| C-09 | Pimpinan | WD Sumber Daya | — | `CAT-NET` | Tag: NET | Hanya petugas bertag Internet & Jaringan yang muncul |
| C-10 | Pimpinan | WD Akademik | — | `CAT-SND` | Tag: SND | Hanya petugas bertag Sound System yang muncul |
| C-11 | Pimpinan | Manajer | — | `CAT-ELK` | Tag: ELK | Hanya petugas bertag Elektrikal yang muncul |
| C-12 | Superadmin | — | — | `CAT-AC` | Tag: AC | Semua petugas bertag AC muncul, multi-select hingga 10 petugas |
| C-13 | Pimpinan | Supervisor SD | — | `CAT-KBR` | Tag: KBR | Tugaskan ke petugas kebersihan, bisa isi catatan penugasan |
| C-14 | Pimpinan | Dekan | — | `CAT-IT` | Tag: IT, NET | Petugas dengan salah satu dari tag IT atau NET muncul |
| C-15 | Superadmin | — | — | `CAT-CIV` | Tidak ada tag | Semua petugas aktif muncul (tanpa filter tag) |
| C-16 | Pimpinan | WDSD | — | Kategori yang jabatan ini tidak berhak | — | Tiket tidak tampil di daftar pimpinan tersebut |

### C3 — Penyelesaian Tiket

| TC# | Aktor | Status Awal | Kondisi | Hasil yang Diharapkan |
|-----|-------|-------------|---------|----------------------|
| C-17 | Petugas (assignee) | `ditugaskan` | — | Tombol "Selesai" tersedia, klik → modal catatan + foto bukti |
| C-18 | Petugas (bukan assignee) | `ditugaskan` | — | **Tidak ada** tombol Selesai |
| C-19 | Superadmin | `ditugaskan` | — | Bisa menyelesaikan tiket manapun |
| C-20 | Petugas | `ditugaskan` | `requires_asset=true` | Modal selesai tampilkan dropdown kondisi aset (Layak/Rusak/dll) |
| C-21 | Petugas | `diterima` | Belum ditugaskan | Tombol Selesai **tidak tampil** |
| C-22 | Pimpinan | `ditugaskan` | — | **Tidak ada** tombol Selesai (pimpinan tidak mengerjakan) |

### C4 — Verifikasi Pimpinan

| TC# | Aktor | Jabatan | Kategori | Flag | Hasil yang Diharapkan |
|-----|-------|---------|----------|------|-----------------------|
| C-23 | Pimpinan | Dekan | `CAT-ELK` | `requires_pimpinan_verification=true` | Setelah petugas selesai, tombol "Verifikasi" muncul untuk pimpinan |
| C-24 | Pimpinan | WD Sumber Daya | `CAT-CIV` | `requires_pimpinan_verification=true` | Verifikasi tersedia, klik → tiket ditandai `verified_at` |
| C-25 | Pimpinan | WD Akademik | `CAT-NET` | `requires_pimpinan_verification=false` | Tombol Verifikasi **tidak muncul** |
| C-26 | Superadmin | — | `CAT-ELK` | `requires_pimpinan_verification=true` | Superadmin juga bisa verifikasi |
| C-27 | Petugas | — | `CAT-ELK` | `requires_pimpinan_verification=true` | Petugas **tidak bisa** verifikasi |

---

## KELOMPOK D — Tiket: Fitur Lanjutan

### D1 — Lapor Progres & Perpanjangan SLA

| TC# | Aktor | Kondisi | Aksi | Hasil yang Diharapkan |
|-----|-------|---------|------|-----------------------|
| D-01 | Petugas (assignee) | Status `ditugaskan` | Lapor Progres | Modal terbuka: input persen 0–100, catatan, foto bukti opsional |
| D-02 | Petugas | Status `ditugaskan`, SLA diatur | Ajukan Perpanjangan SLA | Modal: tanggal baru + alasan; status perpanjangan → `pending` |
| D-03 | Pimpinan | Ada perpanjangan SLA pending | Setujui | `sla_due_at` diperbarui ke tanggal baru, status → `approved` |
| D-04 | Pimpinan | Ada perpanjangan SLA pending | Tolak | Status perpanjangan → `rejected`, SLA lama berlaku |
| D-05 | Superadmin | Ada perpanjangan SLA pending | Setujui/Tolak | Sama dengan pimpinan |
| D-06 | Petugas bukan assignee | — | Coba lapor progres | Tombol **tidak muncul** |
| D-07 | Pelapor | Status `dikirim` | Batalkan tiket | Modal konfirmasi → tiket `canceled_at` terisi |
| D-08 | Superadmin | Status apapun | Batalkan tiket | Superadmin bisa membatalkan tiket apapun |
| D-09 | Petugas | Status `ditugaskan` | Batalkan tiket | Petugas yang ditugaskan bisa batalkan dengan alasan |
| D-10 | Petugas | Status `ditugaskan` | Tandai Menunggu Vendor | Status substatus `pending_vendor=true`, catatan vendor terisi |

### D2 — Sub-Tugas & Biaya

| TC# | Aktor | Aksi | Data | Hasil yang Diharapkan |
|-----|-------|------|------|-----------------------|
| D-11 | Petugas | Tambah sub-tugas | Judul, assignee opsional, due date | Sub-tugas masuk daftar, status `open` |
| D-12 | Petugas | Update status sub-tugas | `open` → `in_progress` → `done` | Status berubah, evidence_url bisa diisi |
| D-13 | Pimpinan | Tambah sub-tugas | Judul, assignee petugas | Sub-tugas ditambahkan oleh pimpinan |
| D-14 | Petugas | Tambah biaya | Jumlah Rp. 500.000, deskripsi | Biaya muncul di detail tiket, total terakumulasi |
| D-15 | Pimpinan | Lihat biaya | — | Pimpinan dapat melihat biaya tiket |
| D-16 | Pelapor | Lihat biaya | — | Pelapor **tidak dapat** melihat biaya (canViewCosts = false) |
| D-17 | Petugas | Tambah komentar diskusi | Pesan teks | Komentar muncul di thread diskusi dengan nama dan waktu |
| D-18 | Pelapor | Tambah komentar | Pesan balasan | Pelapor bisa berpartisipasi di diskusi tiketnya sendiri |

---

## KELOMPOK E — Manajemen Tugas Petugas

### E1 — Buat Tugas (Petugas membuat dari nol)

| TC# | Aktor | Unit | Tag Petugas | Kategori | Hasil yang Diharapkan |
|-----|-------|------|-------------|----------|-----------------------|
| E-01 | Petugas IT | Informatika | `IT`, `NET` | `CAT-IT` | Form Buat Tugas: pilih kategori → dropdown pengerja hanya petugas IT/NET |
| E-02 | Petugas Elektrik | Sumber Daya | `ELK` | `CAT-ELK` | Bisa buat tugas, kategori ELK tersedia karena `allow_petugas_create=true` |
| E-03 | Petugas Kebersihan | Fakultas | `KBR` | `CAT-KBR` | Buat tugas kebersihan, self_executable: assignee = diri sendiri otomatis opsional |
| E-04 | Petugas | Bioteknologi | `AC` | `CAT-AC` | `requires_asset=true`: picker aset wajib muncul |
| E-05 | Superadmin | Semua | — | Semua | Bisa buat tugas dengan kategori apapun |
| E-06 | Pelapor | — | — | — | **Tidak bisa** akses `/task` → redirect `/dashboard` |
| E-07 | Pimpinan | — | — | — | Pimpinan **bisa** akses `/task` (sesuai legacy rule) |

### E2 — Tugas Saya (Antrian Kerja Petugas)

| TC# | Aktor | Tag | Kondisi | Hasil yang Diharapkan |
|-----|-------|-----|---------|----------------------|
| E-08 | Petugas IT, Informatika | `IT`, `NET` | Ada tiket kategori IT/NET | Tiket tampil di "Tugas Saya" karena tag cocok |
| E-09 | Petugas Kebersihan | `KBR` | Ada tiket kategori IT | Tiket IT **tidak muncul** (tag tidak cocok) |
| E-10 | Petugas Sound | Akademik | `SND` | Ada tiket Sound System | Tiket SND muncul di antrean |
| E-11 | Petugas | Multi-tag: `IT`, `ELK` | Tiket IT dan Listrik ada | Kedua tiket muncul di antrian |
| E-12 | Petugas | `IT` | Tiket sudah punya 10 assignee | Tidak bisa claim (batas MAX_ASSIGNEES_PER_REPORT) |

---

## KELOMPOK F — Dashboard & Monitoring (Pimpinan)

### F1 — Dashboard SLA

| TC# | Aktor | Jabatan | Unit | Filter | Hasil yang Diharapkan |
|-----|-------|---------|------|--------|-----------------------|
| F-01 | Pimpinan | Dekan | Fakultas | Semua periode | KPI: Total tiket, selesai, on-time %, melewati SLA, rata² penyelesaian |
| F-02 | Pimpinan | WD Sumber Daya | Sumber Daya | Bulan ini | Data difilter sesuai scope jabatan & unit |
| F-03 | Pimpinan | WD Akademik | Akademik | Tahun ini | Distribusi status per jenis tiket tampil |
| F-04 | Superadmin | — | Semua | Semua | Semua data tanpa filter unit |
| F-05 | Petugas | — | — | — | **Tidak bisa** akses `/dashboard/sla` |
| F-06 | Pelapor | — | — | — | **Tidak bisa** akses `/dashboard/sla` |

### F2 — Dashboard Biaya

| TC# | Aktor | Jabatan | Data Uji | Hasil yang Diharapkan |
|-----|-------|---------|----------|-----------------------|
| F-07 | Pimpinan | Dekan | Ada 10 tiket dengan biaya total Rp 5.000.000 | Total biaya, jumlah tiket berbiaya, rata-rata per tiket tampil |
| F-08 | Pimpinan | Manajer | — | Tren biaya per bulan (bar chart) dan per jenis tiket |
| F-09 | Superadmin | — | — | Biaya semua unit tampil, bisa filter periode |

### F3 — Kondisi Aset

| TC# | Aktor | Jabatan | Hasil yang Diharapkan |
|-----|-------|---------|----------------------|
| F-10 | Pimpinan | Dekan | Total aset, avg health, % layak, daftar aset kritis |
| F-11 | Pimpinan | WD Sumber Daya | Kondisi aset gedung sumber daya |
| F-12 | Superadmin | — | Semua aset semua unit, distribusi kondisi |

### F4 — Monitoring Petugas

| TC# | Aktor | Jabatan | Filter | Hasil yang Diharapkan |
|-----|-------|---------|--------|-----------------------|
| F-13 | Pimpinan | Dekan | Semua petugas | Kartu statistik per petugas: tiket selesai, on-time %, rata² waktu |
| F-14 | Pimpinan | WD Sumber Daya | Petugas unit SD | Filter hanya petugas unit Sumber Daya |
| F-15 | Pimpinan | Supervisor Akademik | Periode: bulan ini | Data bulan berjalan, daftar + perbandingan kinerja |
| F-16 | Superadmin | — | — | Semua petugas semua unit |
| F-17 | Pimpinan | — | Detail petugas tertentu | `/monitoring-petugas/daftar/:id` — riwayat tiket petugas |
| F-18 | Pimpinan | — | Perbandingan 2 petugas | `/monitoring-petugas/perbandingan` — grafik radar komparatif |

---

## KELOMPOK G — Manajemen Aset (Petugas)

### G1 — Manajemen Aset

| TC# | Aktor | Unit | Aksi | Data | Hasil yang Diharapkan |
|-----|-------|------|------|------|-----------------------|
| G-01 | Petugas | Informatika | Tambah aset baru | Nama: Proyektor #5, Ruang: Lab Komputer, Kondisi: Layak | Aset tersimpan, health score dihitung |
| G-02 | Petugas | Sumber Daya | Edit aset | Ubah kondisi dari Layak → Rusak Ringan | Kondisi diperbarui, histori tercatat |
| G-03 | Petugas | Fisika | Tambah detail pengadaan | Vendor: PT XYZ, harga Rp 15.000.000, garansi 2027 | Detail vendor & pengadaan tersimpan |
| G-04 | Petugas | Biologi | Cari aset | Keyword "AC" | Semua aset mengandung "AC" di nama/kode muncul |
| G-05 | Petugas | Kimia | Filter kondisi | Kondisi: Kritis | Hanya aset berkondisi Kritis yang tampil |
| G-06 | Pelapor | — | Akses `/aset` | — | **Tidak bisa** → redirect dashboard |
| G-07 | Pimpinan | — | Akses `/aset` | — | **Tidak bisa** → redirect dashboard |

### G2 — Lihat Aset & Perbarui Kondisi

| TC# | Aktor | Aksi | Kondisi | Hasil yang Diharapkan |
|-----|-------|------|---------|----------------------|
| G-08 | Petugas | Lihat detail aset | Kondisi: Baik | Riwayat maintenance tampil, tanpa auto-buat tiket |
| G-09 | Petugas | Perbarui kondisi | Kondisi saat ini: Baik → Rusak | Muncul picker Jenis Tiket + wajib foto → auto-buat tiket maintenance |
| G-10 | Petugas | Perbarui kondisi | Kondisi: Kritis | Tiket bertag kategori AC/Elektrikal otomatis terbuat |
| G-11 | Superadmin | Lihat semua aset | — | Semua aset semua unit tampil |

---

## KELOMPOK H — Superadmin: Master Data

### H1 — Manajemen Pengguna

| TC# | Aksi | Data Uji | Hasil yang Diharapkan |
|-----|------|----------|-----------------------|
| H-01 | Lihat daftar user | — | Semua user dengan role, jabatan, unit, jenis pelapor tampil |
| H-02 | Set jabatan user | User A → Jabatan: Dekan | Jabatan terupdate, `position_id` berubah |
| H-03 | Set unit user | User B → Unit: Informatika | `unit_id` berubah, user terikat ke unit tersebut |
| H-04 | Set jenis pelapor | User C → Jenis: Mahasiswa | `reporter_type_id` berubah |
| H-05 | Tambah role petugas | User D (hanya pelapor) → toggle petugas | Role petugas ditambahkan |
| H-06 | Hapus role pimpinan | User E (petugas+pimpinan) → toggle off pimpinan | Role pimpinan dihapus, user hanya petugas |
| H-07 | Atur tag/skill | User F → tag: IT, NET | User mendapat skill IT dan Jaringan |
| H-08 | Cari user | Keyword: "Budi" | Semua user bernama "Budi" tampil |
| H-09 | Impersonasi user | Klik Impersonasi → User Mahasiswa | Banner impersonasi tampil, dashboard berubah ke tampilan pelapor |
| H-10 | Impersonasi petugas IT | Klik Impersonasi → User Petugas | Menu Tugas Saya, Buat Tugas tampil, tidak ada menu superadmin |
| H-11 | Stop impersonasi | Klik "Kembali sebagai Superadmin" | Banner hilang, kembali ke tampilan superadmin |

### H2 — Manajemen Jenis Tiket (Kategori)

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-12 | Tambah kategori baru | Nama: "Gangguan Lift", Deskripsi: "..." | Kategori aktif tersimpan, muncul di form buat tiket |
| H-13 | Set kriteria jabatan | CAT-ELK → Jabatan: WDSD, WDAK | Hanya pimpinan dengan jabatan tsb yang bisa menerima/menugaskan |
| H-14 | Set tag wajib | CAT-NET → Tag: NET | Dropdown petugas hanya tampil yang bertag NET |
| H-15 | Set opsi SLA | CAT-IT → SLA: 4 jam, 8 jam, 1 hari | Dropdown SLA muncul di form buat tiket |
| H-16 | Toggle self_executable | CAT-SND → centang self_executable | Setelah diterima, otomatis ditugaskan ke pelapor |
| H-17 | Toggle requires_asset | CAT-AC → centang requires_asset | Picker aset wajib di form buat tiket |
| H-18 | Toggle photo_required=false | CAT-KBR → lepas foto wajib | Foto opsional di form buat tiket kebersihan |
| H-19 | Nonaktifkan kategori | CAT-GDG → Nonaktifkan | Kategori tidak muncul di form buat tiket |
| H-20 | Hapus kategori | CAT-GDG | Konfirmasi ganda muncul, hapus → kategori hilang |

### H3 — Manajemen Jabatan

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-21 | Tambah jabatan baru | Nama: "Koordinator Lab", Level: 4 | Jabatan aktif tersimpan |
| H-22 | Edit level jabatan | Dekan → Level: 1 | Level terupdate |
| H-23 | Nonaktifkan jabatan | Supervisor SD | Jabatan nonaktif, tidak muncul di dropdown pengguna baru |
| H-24 | Cari jabatan | Keyword "Wakil" | Kedua Wakil Dekan tampil |

### H4 — Manajemen Jenis Pelapor

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-25 | Tambah jenis pelapor | Nama: "Alumni" | Jenis pelapor baru aktif |
| H-26 | Nonaktifkan | RT-UMM | Jenis Umum nonaktif, tidak muncul di pilihan baru |
| H-27 | Set kriteria kategori | CAT-ELK → Jenis: Dosen, Tendik (bukan Mahasiswa) | Mahasiswa tidak bisa pilih kategori ELK |

### H5 — Manajemen Skill / Tag

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-28 | Tambah tag baru | Nama: "Plumbing", Warna: #0284c7, Kategori: Teknik | Tag tersimpan dengan warna dan chip berwarna |
| H-29 | Tambah tag tanpa warna | Nama: "Umum" | Tag chip tampil neutral (tanpa warna) |
| H-30 | Nonaktifkan tag | NET | Tag NET nonaktif, tidak muncul di filter petugas baru |
| H-31 | Hapus tag | Hapus tag "Plumbing" | Konfirmasi muncul, tag dihapus dari semua relasi user & kategori |
| H-32 | Pilih warna dari palet | 12 swatch warna tersedia | Klik swatch → warna terisi di field hex |

### H6 — Manajemen Unit

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-33 | Tambah unit induk | Nama: "Direktorat TIK" | Unit tanpa parent (root) tersimpan |
| H-34 | Tambah unit anak | Nama: "Subbag Jaringan", Induk: Sumber Daya | Hierarki tersimpan `parent_id` terisi |
| H-35 | Nonaktifkan unit | Unit Informatika | Unit nonaktif, user lama tetap terikat tapi pilihan baru tidak muncul |
| H-36 | Cari unit | Keyword "Bio" | Biologi dan Bioteknologi muncul |

### H7 — Manajemen Vendor

| TC# | Aksi | Data | Hasil yang Diharapkan |
|-----|------|------|-----------------------|
| H-37 | Tambah vendor | Nama: "PT Infra Teknologi", Jenis: IT & Jaringan, PIC: Andi, Telp: 0812xxx | Vendor aktif tersimpan |
| H-38 | Edit vendor | Ubah email vendor | Data vendor terupdate |
| H-39 | Nonaktifkan vendor | PT Infra Teknologi | Vendor nonaktif, tidak muncul di picker aset baru |
| H-40 | Hapus vendor | Vendor tanpa aset terkait | Vendor terhapus, konfirmasi muncul |
| H-41 | Migrasi belum jalan | Buka menu Vendor sebelum migrasi 0030 | Pesan informatif tampil, tidak crash |

### H8 — Menu & Hak Akses

| TC# | Aksi | Subjek | Efek | Hasil yang Diharapkan |
|-----|------|--------|------|-----------------------|
| H-42 | Buat menu baru | Key: sla_dashboard, Route: /dashboard/sla | — | Menu tersimpan, muncul di daftar |
| H-43 | Tambah aturan role | Menu: Dashboard SLA, Subjek: role=pimpinan, Efek: allow | Pimpinan | Pimpinan bisa akses /dashboard/sla |
| H-44 | Tambah aturan jabatan | Menu: Manajemen Tiket, Jabatan: WDSD, Efek: allow | User WDSD | User dengan jabatan WDSD bisa akses /manajemen-laporan |
| H-45 | Tambah aturan unit | Menu: Tugas Saya, Unit: Informatika, Efek: allow | Petugas Unit Info | Hanya petugas unit Informatika yang dapat akses |
| H-46 | Tambah aturan skill | Menu: Buat Tugas, Skill: IT, Efek: allow | Petugas IT | Petugas berskill IT bisa akses /task |
| H-47 | Tambah aturan user | Menu: Dashboard Biaya, User: ID-specific, Efek: allow | User spesifik | Hanya user tersebut yang lihat menu |
| H-48 | Tambah aturan deny | Menu: Dashboard SLA, Role: petugas, Efek: deny | Petugas | Petugas di-blok meski ada allow dari aturan lain |
| H-49 | Deny mengalahkan allow | Menu: X, allow(role:petugas) + deny(user:A) | User A (petugas) | User A tidak bisa lihat menu X |
| H-50 | Ubah visibilitas ke public | Menu: Tiket | — | Menu tampil untuk semua user login tanpa aturan |
| H-51 | Nonaktifkan menu | Menu: Lihat Aset | — | Menu tidak tampil di dashboard siapapun |
| H-52 | Hapus menu | Menu yang tidak diperlukan | — | Konfirmasi, menu + aturannya terhapus |

---

## KELOMPOK I — Notifikasi

| TC# | Trigger | Penerima | Hasil yang Diharapkan |
|-----|---------|---------|----------------------|
| I-01 | Tiket status → `diterima` | Pelapor pemilik | Notifikasi "Tiket Anda diterima" muncul di bell + halaman Notifikasi |
| I-02 | Tiket status → `ditugaskan` | Petugas yang ditugaskan | Notifikasi "Anda ditugaskan tiket #XXX" |
| I-03 | Tiket status → `diselesaikan` | Pelapor pemilik | Notifikasi "Tiket Anda diselesaikan" |
| I-04 | Tiket terverifikasi | Pelapor pemilik | Notifikasi `verified` tampil |
| I-05 | SLA terlampaui | Petugas assignee | Notifikasi overdue muncul |
| I-06 | Klik notifikasi | — | Mark sebagai dibaca, navigate ke `/laporan/:id` dengan `state.from=/notifications` |
| I-07 | Tandai semua dibaca | — | Semua notifikasi read_at terisi, badge hilang |
| I-08 | Filter "Belum dibaca" | — | Hanya notifikasi unread tampil |
| I-09 | Notifikasi dinonaktifkan di profil | Pelapor | Notif tidak dikirim jika `notification_prefs.enabled=false` |
| I-10 | Realtime update | — | Notifikasi baru masuk tanpa reload halaman |

---

## KELOMPOK J — Impersonasi (Superadmin)

| TC# | Skenario | Hasil yang Diharapkan |
|-----|----------|----------------------|
| J-01 | Impersonasi pelapor mahasiswa | Dashboard tampil hanya menu Tiket; menu superadmin hilang |
| J-02 | Impersonasi petugas IT (Unit Informatika, tag IT+NET) | Menu: Tugas Saya, Buat Tugas, Manajemen Aset, Lihat Aset tampil |
| J-03 | Impersonasi pimpinan (Dekan) | Menu: Dashboard SLA, Biaya, Kondisi Aset, Monitoring Petugas tampil |
| J-04 | Impersonasi petugas tanpa unit | Menu dasar petugas tampil, tanpa filter unit |
| J-05 | Impersonasi user dengan deny rule | Menu yang di-deny untuk user tersebut tidak tampil |
| J-06 | Reload saat impersonasi aktif | Impersonasi tetap aktif (localStorage), banner masih tampil |
| J-07 | Stop impersonasi | Kembali ke tampilan superadmin penuh |
| J-08 | Logout saat impersonasi | Impersonasi dihentikan, session superadmin dihapus |

---

## KELOMPOK K — Kombinasi Role Ganda

> User bisa punya lebih dari satu role sekaligus. Berikut kombinasi kritis.

| TC# | Role Kombinasi | Unit | Jabatan | Hasil yang Diharapkan |
|-----|---------------|------|---------|----------------------|
| K-01 | Petugas + Pimpinan | Sumber Daya | WD Sumber Daya | Menu: Tugas Saya, Buat Tugas, Aset, Dashboard SLA/Biaya/Kondisi semua muncul |
| K-02 | Petugas + Pimpinan | Akademik | WD Akademik | Bisa menugaskan dan mengerjakan tiket sekaligus |
| K-03 | Pelapor + Petugas | Informatika | Koordinator | Bisa buat tiket (sebagai pelapor) dan terima tugas (sebagai petugas) |
| K-04 | Pimpinan + Pelapor | Fisika | Dekan | Bisa buat tiket dan lihat dashboard pimpinan |
| K-05 | Superadmin + Petugas | — | — | Superadmin tetap punya semua akses, role petugas tidak membatasi |
| K-06 | Petugas, 3 unit berbeda | Info+Fisika+Biologi | — | Tiket dari ketiga unit muncul di antrian berdasarkan tag |

---

## KELOMPOK L — Keamanan & Isolasi Data

| TC# | Skenario | Metode | Hasil yang Diharapkan |
|-----|----------|--------|----------------------|
| L-01 | Pelapor A akses tiket Pelapor B (langsung via URL `/laporan/:id`) | Akses langsung | Halaman error atau data tidak tampil (RLS memblokir) |
| L-02 | Petugas akses halaman superadmin tanpa rule | Navigasi langsung | Redirect `/dashboard` (guard + RLS) |
| L-03 | Pimpinan coba hapus tiket | Akses API langsung | RLS menolak operasi DELETE |
| L-04 | User inject XSS di keterangan tiket | Input `<script>alert(1)</script>` | Teks tampil sebagai literal, tidak dieksekusi |
| L-05 | User inject CSV formula di nama | Input `=SUM(1+1)` | Di export CSV, karakter di-escape atau di-quote |
| L-06 | Non-superadmin coba grant role superadmin | API langsung | RPC `user_roles` menolak (RLS SECURITY DEFINER) |
| L-07 | Token expired saat di halaman | Session timeout | Auto-redirect ke `/login`, sesi bersih |
| L-08 | Akses storage file tanpa auth | URL langsung foto tiket orang lain | 403 atau signed URL expired |

---

## KELOMPOK M — PWA & Performa

| TC# | Skenario | Kondisi | Hasil yang Diharapkan |
|-----|----------|---------|----------------------|
| M-01 | Buka app offline | Jaringan diputus setelah load pertama | Layar OfflineScreen tampil, bukan blank |
| M-02 | Buka app tanpa jaringan sama sekali | Belum pernah cache | Splash screen offline tampil |
| M-03 | Kembali online | Jaringan tersambung kembali | App auto-refresh, layar offline hilang |
| M-04 | Install PWA | Android Chrome | Prompt "Tambah ke Layar Utama" muncul |
| M-05 | Notifikasi audio | Notif pertama setelah klik | Ringtone berbunyi (setelah user gesture) |
| M-06 | Double back di dashboard | Tekan back 2x dalam 2.5 detik | Modal "Keluar dari aplikasi?" muncul |

---

## KELOMPOK N — Profil & Pengaturan Akun

| TC# | Aktor | Aksi | Data | Hasil yang Diharapkan |
|-----|-------|------|------|-----------------------|
| N-01 | Semua role | Edit nama lengkap | Nama baru max 50 char | Nama terupdate di profil dan dashboard |
| N-02 | Semua role | Upload foto profil | File JPG/PNG max 10MB | Avatar tersimpan di Storage, tampil di topbar |
| N-03 | Semua role | Set nomor WhatsApp | `082112345678` | Tersimpan, bisa digunakan untuk link WA di monitoring |
| N-04 | Semua role | Atur preferensi notifikasi | Enable/disable per event | Notifikasi dikirim/tidak sesuai pengaturan |
| N-05 | Semua role | Ganti password | Request kirim email reset | Email reset terkirim, konfirmasi tampil |
| N-06 | Superadmin | Set email helpdesk | `helpdesk@fsm.undip.ac.id` | Email tersimpan, muncul di halaman Hubungi Admin |
| N-07 | User manapun | Hubungi admin | — | Halaman menampilkan email helpdesk, tombol `mailto:` berfungsi |

---

## KELOMPOK O — Ekspor Data (Pimpinan & Superadmin)

| TC# | Aktor | Filter | Format | Hasil yang Diharapkan |
|-----|-------|--------|--------|-----------------------|
| O-01 | Pimpinan | Semua tiket, bulan ini | Excel (.xlsx) | File terunduh berisi data tiket dengan kolom: no tiket, jenis, status, pelapor, petugas, SLA |
| O-02 | Superadmin | Filter: kategori IT, tahun ini | Excel | Hanya tiket kategori IT |
| O-03 | Pimpinan | Semua, periode custom | PDF | File PDF tergenerate |
| O-04 | Petugas | — | — | Tombol ekspor **tidak tampil** |
| O-05 | Pelapor | — | — | Tombol ekspor **tidak tampil** |

---

## Ringkasan Jumlah Test Case

| Kelompok | Nama | Jumlah TC |
|----------|------|-----------|
| A | Autentikasi & Akses Awal | 14 |
| B | Pembuatan Tiket (Pelapor) | 16 |
| C | Alur Workflow Tiket | 27 |
| D | Fitur Lanjutan Tiket | 18 |
| E | Manajemen Tugas Petugas | 12 |
| F | Dashboard & Monitoring Pimpinan | 18 |
| G | Manajemen Aset | 11 |
| H | Superadmin: Master Data | 52 |
| I | Notifikasi | 10 |
| J | Impersonasi | 8 |
| K | Kombinasi Role Ganda | 6 |
| L | Keamanan & Isolasi Data | 8 |
| M | PWA & Performa | 6 |
| N | Profil & Pengaturan | 7 |
| O | Ekspor Data | 5 |
| **Total** | | **218 Test Case** |

---

## Prioritas Eksekusi Pengujian

### 🔴 Kritikal (jalankan setiap release)
A-01 s.d. A-10, B-01 s.d. B-10, C-01 s.d. C-27, L-01 s.d. L-08

### 🟡 Penting (jalankan setiap sprint)
D-01 s.d. D-18, E-01 s.d. E-12, H-01 s.d. H-52, I-01 s.d. I-10

### 🟢 Regression (jalankan sebelum release mayor)
F-01 s.d. F-18, G-01 s.d. G-11, J-01 s.d. J-08, K-01 s.d. K-06, M-01 s.d. M-06, N-01 s.d. N-07, O-01 s.d. O-05

---

*Dokumen ini mengacu pada kode versi 0.2.0 dan mencerminkan kondisi fitur yang sudah diimplementasikan.*  
*Lihat juga: [TEST-PLAN.md](./docs/TEST-PLAN.md) · [TEST-REPORT.md](./docs/TEST-REPORT.md) · [WIREFRAME-HALAMAN.md](./docs/WIREFRAME-HALAMAN.md)*
