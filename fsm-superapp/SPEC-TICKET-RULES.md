# SPEC-TICKET-RULES — Panduan Penulisan Spesifikasi Tiket FSM LAPOR!

> **Versi:** 1.0.0  
> **Tanggal:** Juni 2026  
> **Berlaku untuk:** FSM LAPOR! v0.2.0+  
> **Referensi utama:** [CHECKPOINT-2.md](./CHECKPOINT-2.md) · [RKF Bidang Sumber Daya Juni 2026](./RKF_Bid_II_Juni_2026_final.md)  
> **App live:** https://apps-fsm.undip.ac.id (SSO FSM UNDIP)

---

## Daftar Isi

1. [Tujuan & Ruang Lingkup](#1-tujuan--ruang-lingkup)
2. [Konteks Produksi Terkini](#2-konteks-produksi-terkini)
3. [Master Data Referensi (Terupdate)](#3-master-data-referensi-terupdate)
4. [Jenis Tiket Pengembangan](#4-jenis-tiket-pengembangan)
5. [Template Spec Tiket](#5-template-spec-tiket)
6. [Aturan Wajib Penulisan](#6-aturan-wajib-penulisan)
7. [Panduan per Field](#7-panduan-per-field)
8. [Acceptance Criteria — Format & Standar](#8-acceptance-criteria--format--standar)
9. [Tautan ke Test Case CHECKPOINT-2](#9-tautan-ke-test-case-checkpoint-2)
10. [Prioritas & Label](#10-prioritas--label)
11. [Backlog dari Temuan RKF Juni 2026](#11-backlog-dari-temuan-rkf-juni-2026)
12. [Contoh Spec Tiket Lengkap](#12-contoh-spec-tiket-lengkap)

---

## 1. Tujuan & Ruang Lingkup

Dokumen ini mendefinisikan aturan baku penulisan **spec tiket pengembangan** untuk proyek FSM LAPOR! — Aplikasi Pelaporan Kinerja Pegawai Fakultas Sains dan Matematika, Universitas Diponegoro.

**Tujuan:**
- Memastikan setiap tiket dapat langsung dieksekusi tanpa ambiguitas oleh developer.
- Mengikat setiap spesifikasi ke master data dan test case yang sudah ada di CHECKPOINT-2.md.
- Mempercepat review dan approval dari Bidang Sumber Daya / Bidang TI & Komunikasi.
- Menjaga konsistensi antar sprint dan antar kontributor.

**Ruang lingkup:**  
Semua tiket pengembangan fitur baru (*feature*), perbaikan bug (*fix*), peningkatan (*improvement*), dan konfigurasi ulang data (*chore*) pada repository FSM LAPOR!.

---

## 2. Konteks Produksi Terkini

Berdasarkan **RKF Bidang Sumber Daya — Juni 2026** (Slide 04, 44–51):

| Aspek | Kondisi |
|-------|---------|
| **Status App** | Live di production: https://apps-fsm.undip.ac.id via SSO FSM |
| **Pengguna aktif** | Dosen, Tendik, Mahasiswa, Pimpinan (Dekan, WD, Manajer, Supervisor) |
| **Outsourcing baru** | Per **Juli 2026**: penambahan tim kebersihan (tag `KBR`) dan keamanan (tag `KMN`) — jumlah petugas bertambah signifikan |
| **Optimalisasi aset** | Aset tidak digunakan >1 tahun dapat **diusulkan dihapuskan** (keputusan MWA) |
| **Optimalisasi ruang** | MWA meminta optimalisasi pemanfaatan **ruang kelas bersama** |
| **IKU #32** | Target 91%, capaian 2025 = 90% — FSM LAPOR! berkontribusi langsung pada KPI ini |
| **Aksesibilitas** | Web + Mobile (PWA) — setiap spec harus menyebutkan target tampilan |

> ⚠️ **Implikasi wajib untuk semua tiket per Juli 2026:**  
> Setiap tiket yang menyentuh manajemen petugas, penugasan tiket, atau filter tag **harus mempertimbangkan skala penambahan petugas outsourcing KBR & KMN**.

---

## 3. Master Data Referensi (Terupdate)

Gunakan tabel berikut sebagai satu-satunya referensi saat menulis spec. Jangan mendefinisikan ulang nilai-nilai ini di dalam tiket.

### 3.1 Role
| Kode | Nama | Catatan |
|------|------|---------|
| `SA` | Superadmin | Akses penuh, bisa impersonasi |
| `PIM` | Pimpinan | Terima, tugaskan, verifikasi tiket |
| `PET` | Petugas | Kerjakan tugas, kelola aset |
| `PEL` | Pelapor | Buat & pantau tiket sendiri |

### 3.2 Unit (Terupdate — RKF Juni 2026)
| Kode | Nama Unit | Sumber |
|------|-----------|--------|
| `FAK` | Tingkat Fakultas (induk) | CHECKPOINT-2 |
| `AKADEMIK` | Unit Akademik & Kemahasiswaan | CHECKPOINT-2 |
| `SUMBERDAYA` | Unit Sumber Daya | CHECKPOINT-2 |
| `INFO` | Jurusan Informatika (S1) | CHECKPOINT-2 |
| `FISIKA` | Jurusan Fisika (S1) | CHECKPOINT-2 |
| `BIO` | Jurusan Biologi (S1) | CHECKPOINT-2 |
| `BIOTEK` | Jurusan Bioteknologi (S1) | CHECKPOINT-2 |
| `KIM` | Jurusan Kimia (S1) | CHECKPOINT-2 |
| `STAT` | Jurusan Statistika (S1) | CHECKPOINT-2 |
| `MAT` | Jurusan Matematika (S1) | CHECKPOINT-2 |
| `S2MAT` | Program Studi S2 Matematika | **RKF Juni 2026** |
| `S2BIO` | Program Studi S2 Biologi | **RKF Juni 2026** |
| `S2FIS` | Program Studi S2 Fisika | **RKF Juni 2026** |
| `S2KIM` | Program Studi S2 Kimia | **RKF Juni 2026** |
| `S3DSM` | Program Doktor Sains Matematika | **RKF Juni 2026** |
| `PROFISMED` | Profesi Fisikawan Medik | **RKF Juni 2026** |
| `DIPOSAINS` | Diposains Clean (unit bisnis) | **RKF Juni 2026** |

> 📌 Unit dengan kode **baru** (`S2MAT` dst.) belum ada di database production — tiket pengembangan yang melibatkan unit ini harus menyertakan task migrasi / seeding data.

### 3.3 Jabatan
| Kode | Nama Jabatan |
|------|-------------|
| `DKN` | Dekan |
| `WDSD` | Wakil Dekan Sumber Daya |
| `WDAK` | Wakil Dekan Akademik & Kemahasiswaan |
| `MGR` | Manajer |
| `SPVSD` | Supervisor Sumber Daya |
| `SPVAK` | Supervisor Akademik & Kemahasiswaan |
| `KORD` | Koordinator (Lab, dll.) |

### 3.4 Skill / Tag Petugas
| Kode | Nama Skill | Warna Hex | Catatan |
|------|-----------|-----------|---------|
| `IT` | IT & Komputer | `#0284c7` | — |
| `NET` | Internet & Jaringan | `#0891b2` | — |
| `SND` | Sound System & AV | `#7c3aed` | — |
| `ELK` | Elektrikal & Listrik | `#d97706` | — |
| `AC` | AC & HVAC | `#16a34a` | — |
| `KBR` | Kebersihan & Sanitasi | `#65a30d` | **Skala besar per Juli 2026** |
| `KMN` | Keamanan & CCTV | `#dc2626` | **Skala besar per Juli 2026** |
| `CIV` | Sipil & Bangunan | `#6b7280` | — |
| `GDG` | Gedung & Fasilitas | `#ca8a04` | — |
| `KDR` | Kendaraan & Transportasi | `#ea580c` | — |

### 3.5 Kategori Tiket (Jenis Laporan)
| Kode | Nama | Flags |
|------|------|-------|
| `CAT-IT` | Gangguan IT / Komputer | `requires_asset=true` |
| `CAT-NET` | Gangguan Jaringan Internet | — |
| `CAT-SND` | Sound System / AV | `self_executable=true` |
| `CAT-ELK` | Kelistrikan | `requires_pimpinan_verification=true` |
| `CAT-AC` | AC / Pendingin Ruangan | `requires_asset=true` |
| `CAT-KBR` | Kebersihan | `self_executable=true` |
| `CAT-CIV` | Kerusakan Bangunan | `requires_pimpinan_verification=true` |
| `CAT-GDG` | Fasilitas Gedung Umum | — |

### 3.6 Jenis Pelapor
| Kode | Nama |
|------|------|
| `RT-DOS` | Dosen |
| `RT-MHS` | Mahasiswa |
| `RT-TEN` | Tenaga Kependidikan |
| `RT-UMM` | Umum |

### 3.7 Status Tiket (Alur)
```
dikirim → diterima → ditugaskan → diselesaikan → [verified_at] → closed
                                             ↑
                               pending_vendor (substatus)
```

---

## 4. Jenis Tiket Pengembangan

| Tipe | Kode | Kapan Digunakan |
|------|------|-----------------|
| Feature baru | `feat` | Fitur yang belum ada di production |
| Perbaikan bug | `fix` | Bug teridentifikasi dari test case atau produksi |
| Improvement | `improvement` | Peningkatan performa/UX fitur yang sudah ada |
| Chore / Infra | `chore` | Migrasi data, seeding, konfigurasi env, refactor |
| Security | `security` | Berkaitan dengan Kelompok L (CHECKPOINT-2) |
| Test | `test` | Penulisan/update test otomatis |

---

## 5. Template Spec Tiket

Salin template berikut untuk setiap tiket baru. Field yang **[WAJIB]** tidak boleh kosong saat tiket dipindahkan ke status *In Progress*.

```markdown
## [TIPE] Judul Singkat Tiket

> **ID Tiket:** FSM-XXXX  
> **Tipe:** feat | fix | improvement | chore | security | test  
> **Prioritas:** 🔴 Kritikal | 🟡 Penting | 🟢 Regression  
> **Sprint Target:** Sprint-XX  
> **Estimasi:** X hari  
> **Assignee:** @nama  
> **Versi Target:** 0.X.X  
> **Platform:** Web | Mobile | Keduanya  

---

### Latar Belakang [WAJIB]

> Jelaskan mengapa tiket ini perlu dikerjakan. Hubungkan ke konteks bisnis / operasional
> (misalnya: outsourcing Juli 2026, IKU #32, laporan RKF, dll.)

### Deskripsi Fitur / Perubahan [WAJIB]

> Uraikan secara teknis dan fungsional apa yang harus dibangun atau diperbaiki.

### Aktor & Role yang Terlibat [WAJIB]

| Role | Aksi | Catatan |
|------|------|---------|
| `SA` / `PIM` / `PET` / `PEL` | ... | ... |

### Master Data yang Digunakan [WAJIB]

> Cantumkan kode unit, jabatan, tag, atau kategori yang relevan dari §3 dokumen ini.
> Contoh: Unit: `INFO`, `S2BIO` · Tag: `KBR`, `KMN` · Kategori: `CAT-KBR`

### Alur / Flow [WAJIB jika feat/improvement]

```
1. Aktor melakukan X
2. Sistem melakukan Y
3. Kondisi Z terpenuhi → hasil A
4. Kondisi Z tidak terpenuhi → hasil B (error/redirect)
```

### UI / UX Notes [opsional]

> Spesifikasi tampilan, komponen, atau behavior UI.
> Sebutkan: apakah web-only, mobile-only, atau keduanya.
> Referensikan wireframe jika ada: [WIREFRAME-HALAMAN.md](./docs/WIREFRAME-HALAMAN.md)

### Database / API Changes [WAJIB jika ada perubahan schema]

- Tabel / kolom baru: ...  
- Migrasi: migration_XXXX_nama.sql  
- RLS policy baru / diubah: ...  
- Edge function / RPC baru: ...  

### Acceptance Criteria [WAJIB]

- [ ] AC-01: ...
- [ ] AC-02: ...
- [ ] AC-03: ...

### Test Case yang Harus Lulus [WAJIB]

> Referensikan dari CHECKPOINT-2.md. Format: `[GROUP]-[NO]`

| TC# | Deskripsi Singkat | Status Sebelum | Target |
|-----|-------------------|----------------|--------|
| ... | ... | ❌ Fail / ✅ Pass / 🆕 New | ✅ Pass |

### Definition of Done [WAJIB]

- [ ] Kode ter-review minimal 1 orang
- [ ] Semua AC di atas terpenuhi
- [ ] Test case CHECKPOINT-2 yang direferensikan lulus
- [ ] Tidak ada console error di web & mobile
- [ ] Fitur tersedia di staging sebelum merge ke main

### Catatan Tambahan [opsional]

> Risiko, dependensi tiket lain, atau catatan deployment.
```

---

## 6. Aturan Wajib Penulisan

### R-01 — Satu Tiket, Satu Concern
Tiket tidak boleh menggabungkan lebih dari satu fitur independen. Jika ada dependensi, buat tiket terpisah dan referensikan dengan `Blocked by: FSM-XXXX`.

### R-02 — Kode Master Data Harus Konsisten
Selalu gunakan kode dari §3 (bukan nama bebas). Contoh: tulis `CAT-KBR` bukan "tiket kebersihan", tulis `WDSD` bukan "Wakil Dekan".

### R-03 — Sertakan Konteks Role Lengkap
Setiap fitur **harus** mendefinisikan behavior untuk semua role yang relevan, termasuk kasus negatif (role yang *tidak boleh* melakukan aksi).

### R-04 — Referensikan Test Case CHECKPOINT-2
Setiap tiket `feat`, `fix`, atau `improvement` wajib menyebutkan minimal satu test case dari CHECKPOINT-2.md. Jika test case baru, tandai dengan prefix `NEW-`.

### R-05 — Flag Kategori Harus Disebutkan
Jika tiket menyentuh logika pembuatan/penugasan tiket, tuliskan secara eksplisit flag kategori yang berlaku: `requires_asset`, `self_executable`, `requires_pimpinan_verification`, `photo_required`, `allow_pelapor_create`.

### R-06 — Pertimbangkan Skala Outsourcing (berlaku per Juli 2026)
Setiap tiket yang menyentuh petugas `KBR` atau `KMN` harus mempertimbangkan jumlah petugas yang bisa ratusan. Pastikan ada:
- Pagination pada daftar petugas
- Filter berdasarkan unit/tag
- Tidak ada hardcode jumlah petugas

### R-07 — Sebutkan Platform Target
Setiap tiket wajib menyebutkan `Platform: Web | Mobile | Keduanya`. Tiket PWA/Mobile merujuk ke Kelompok M CHECKPOINT-2.

### R-08 — Versi Tiket Wajib Ada
Cantumkan `Versi Target` agar changelog dan release notes dapat dihasilkan otomatis.

### R-09 — Migrasi Data Harus Terpisah
Jika ada perubahan schema (tabel baru, kolom baru, RLS baru), buat tiket `chore` migrasi **terpisah** yang menjadi prasyarat tiket fitur.

### R-10 — Unit Baru Butuh Tiket Seeding
Unit dari §3.2 yang bertanda **"RKF Juni 2026"** belum ada di production. Jika fitur memerlukan unit tersebut, wajib membuat tiket `chore` seeding data terlebih dahulu.

---

## 7. Panduan per Field

### 7.1 Prioritas
Gunakan prioritas dari sistem CHECKPOINT-2:

| Label | Kondisi |
|-------|---------|
| 🔴 **Kritikal** | Berkaitan dengan Kelompok A, B, C, L — Auth, alur tiket utama, keamanan data |
| 🟡 **Penting** | Berkaitan dengan Kelompok D, E, H, I — Fitur lanjutan, manajemen tugas, notifikasi, master data |
| 🟢 **Regression** | Berkaitan dengan Kelompok F, G, J, K, M, N, O — Dashboard, aset, impersonasi, PWA, ekspor |

### 7.2 Estimasi
- `fix` sederhana: 0.5–1 hari
- `feat` baru tanpa schema change: 2–3 hari
- `feat` baru dengan schema change + migrasi: 3–5 hari
- Dashboard/analytics baru: 3–5 hari
- `chore` migrasi/seeding: 0.5–1 hari

### 7.3 Judul Tiket
Format: `[TIPE] Subjek — Konteks`  
Contoh yang benar:
- `[feat] Penambahan unit S2 — Seeding master data`
- `[fix] Filter petugas KBR tidak pagination — Antisipasi outsourcing Juli 2026`
- `[improvement] Dashboard SLA — Tambah filter unit S2/S3`

Contoh yang salah:
- `Update unit` ← terlalu generik
- `Bug fix` ← tidak informatif

---

## 8. Acceptance Criteria — Format & Standar

Setiap AC ditulis dalam format **Given / When / Then** atau **kondisi terukur**:

```
- [ ] AC-01: Given petugas bertag KBR, When daftar petugas dimuat dengan 500+ entri, 
             Then pagination aktif dengan 20 item per halaman.
- [ ] AC-02: Tombol "Tugaskan" tidak tampil untuk role PEL.
- [ ] AC-03: Status tiket berubah dari `dikirim` → `diterima` setelah aksi Terima oleh PIM.
```

**Aturan AC:**
- Minimal 3 AC per tiket `feat`
- Minimal 1 AC per tiket `fix`
- AC negatif (hal yang **tidak** boleh terjadi) wajib ada untuk tiket yang menyentuh akses role
- AC performa wajib ada untuk tiket yang memengaruhi daftar dengan >100 item

---

## 9. Tautan ke Test Case CHECKPOINT-2

Gunakan tabel referensi ini saat mengisi kolom "Test Case yang Harus Lulus":

| Kelompok | Topik | Range TC | Prioritas |
|----------|-------|----------|-----------|
| **A** | Autentikasi & Akses | A-01 s.d. A-14 | 🔴 Kritikal |
| **B** | Pembuatan Tiket (Pelapor) | B-01 s.d. B-16 | 🔴 Kritikal |
| **C** | Alur Workflow Tiket | C-01 s.d. C-27 | 🔴 Kritikal |
| **D** | Fitur Lanjutan Tiket | D-01 s.d. D-18 | 🟡 Penting |
| **E** | Manajemen Tugas Petugas | E-01 s.d. E-12 | 🟡 Penting |
| **F** | Dashboard & Monitoring Pimpinan | F-01 s.d. F-18 | 🟢 Regression |
| **G** | Manajemen Aset | G-01 s.d. G-11 | 🟢 Regression |
| **H** | Superadmin: Master Data | H-01 s.d. H-52 | 🟡 Penting |
| **I** | Notifikasi | I-01 s.d. I-10 | 🟡 Penting |
| **J** | Impersonasi | J-01 s.d. J-08 | 🟢 Regression |
| **K** | Kombinasi Role Ganda | K-01 s.d. K-06 | 🟢 Regression |
| **L** | Keamanan & Isolasi Data | L-01 s.d. L-08 | 🔴 Kritikal |
| **M** | PWA & Performa | M-01 s.d. M-06 | 🟢 Regression |
| **N** | Profil & Pengaturan | N-01 s.d. N-07 | 🟢 Regression |
| **O** | Ekspor Data | O-01 s.d. O-05 | 🟢 Regression |

> Full detail setiap test case ada di [CHECKPOINT-2.md](./CHECKPOINT-2.md).

---

## 10. Prioritas & Label

### Label Tiket (GitHub / Issue Tracker)

| Label | Warna | Keterangan |
|-------|-------|------------|
| `kritikal` | 🔴 merah | Harus ada di setiap release |
| `penting` | 🟡 kuning | Setiap sprint |
| `regression` | 🟢 hijau | Sebelum release mayor |
| `outsourcing-juli-2026` | 🟠 oranye | Berkaitan dengan penambahan petugas KBR/KMN |
| `unit-baru` | 🔵 biru | Berkaitan dengan unit S2/S3 dari RKF |
| `iku-32` | 🟣 ungu | Berkontribusi langsung ke IKU #32 |
| `aset-optimasi` | 🩶 abu | Berkaitan dengan deaktivasi aset >1 tahun |
| `security` | ⚫ hitam | Kelompok L CHECKPOINT-2 |
| `blocked` | ⬜ abu-abu | Menunggu tiket lain selesai |

---

## 11. Backlog dari Temuan RKF Juni 2026

Berikut daftar tiket yang **perlu dibuat** berdasarkan hasil analisis RKF Bidang Sumber Daya Juni 2026. Status saat ini: **belum ada tiket**, perlu dibuatkan spec.

### 11.1 🟠 Outsourcing Petugas KBR & KMN (Target: Sebelum Juli 2026)

| ID Sementara | Tipe | Judul | Label |
|--------------|------|-------|-------|
| `BACKLOG-01` | `feat` | Bulk import petugas outsourcing via CSV | `outsourcing-juli-2026` |
| `BACKLOG-02` | `improvement` | Pagination wajib pada daftar petugas (min. per-20) | `outsourcing-juli-2026` |
| `BACKLOG-03` | `improvement` | Filter petugas berdasarkan unit + tag pada modal penugasan | `outsourcing-juli-2026` |
| `BACKLOG-04` | `chore` | Seeding akun petugas outsourcing KBR & KMN per unit | `outsourcing-juli-2026` |

### 11.2 🔵 Unit Baru S2/S3 (Target: Sprint berikutnya)

| ID Sementara | Tipe | Judul | Label |
|--------------|------|-------|-------|
| `BACKLOG-05` | `chore` | Seeding unit S2MAT, S2BIO, S2FIS, S2KIM, S3DSM, PROFISMED | `unit-baru` |
| `BACKLOG-06` | `improvement` | Dashboard SLA & Biaya: tambah filter unit S2/S3 | `unit-baru`, `iku-32` |
| `BACKLOG-07` | `improvement` | Monitoring Petugas: cakupan unit S2/S3 | `unit-baru` |

### 11.3 🩶 Optimalisasi Aset (Keputusan MWA)

| ID Sementara | Tipe | Judul | Label |
|--------------|------|-------|-------|
| `BACKLOG-08` | `feat` | Flag & workflow "usulkan deaktivasi" untuk aset tidak terpakai >1 tahun | `aset-optimasi` |
| `BACKLOG-09` | `improvement` | Filter aset: "Tidak digunakan > N bulan" di halaman Lihat Aset | `aset-optimasi` |
| `BACKLOG-10` | `feat` | Notifikasi otomatis: aset belum ada tiket maintenance selama >12 bulan | `aset-optimasi` |

### 11.4 🟣 IKU #32 — Sistem Informasi Penunjang Tata Kelola

| ID Sementara | Tipe | Judul | Label |
|--------------|------|-------|-------|
| `BACKLOG-11` | `improvement` | Ekspor laporan tiket ke format Excel dengan kolom IKU | `iku-32` |
| `BACKLOG-12` | `feat` | Halaman ringkasan kinerja sistem untuk laporan IKU (Pimpinan/SA) | `iku-32` |

---

## 12. Contoh Spec Tiket Lengkap

### Contoh 1 — Tiket Fix (Sederhana)

```markdown
## [fix] Filter petugas tidak pagination — Modal Penugasan Tiket

> **ID Tiket:** FSM-0101  
> **Tipe:** fix  
> **Prioritas:** 🟡 Penting  
> **Sprint Target:** Sprint-08  
> **Estimasi:** 1 hari  
> **Assignee:** @developer  
> **Versi Target:** 0.2.1  
> **Platform:** Web + Mobile  

### Latar Belakang

Per Juli 2026, tim outsourcing kebersihan dan keamanan akan bergabung. Jumlah petugas
bertag `KBR` dan `KMN` berpotensi melebihi 100 orang. Modal penugasan saat ini memuat
semua petugas sekaligus tanpa pagination → potensi freeze UI.

### Deskripsi

Tambahkan pagination (20 per halaman) dan filter tag pada dropdown petugas di modal
penugasan tiket.

### Aktor & Role

| Role | Aksi |
|------|------|
| `PIM` | Membuka modal penugasan, menelusuri daftar petugas |
| `SA` | Sama dengan PIM |

### Master Data

Unit: semua · Tag: `KBR`, `KMN` (fokus) · Kategori: `CAT-KBR`, `CAT-KMN`

### Alur

1. Pimpinan klik "Tugaskan" pada tiket berkategori `CAT-KBR`
2. Modal terbuka, hanya tampilkan petugas bertag `KBR` (filter otomatis)
3. Daftar terpaginasi: 20 item per halaman dengan navigasi ← →
4. Pimpinan bisa search nama petugas via input text
5. Pilih petugas → klik "Konfirmasi Penugasan"

### Acceptance Criteria

- [ ] AC-01: Daftar petugas di modal penugasan menampilkan maksimal 20 item per halaman.
- [ ] AC-02: Filter tag aktif otomatis sesuai kategori tiket yang dipilih.
- [ ] AC-03: Input search memfilter nama petugas secara real-time (debounce 300ms).
- [ ] AC-04: Role `PEL` tidak dapat mengakses modal penugasan (redirect ke `/dashboard`).

### Test Case CHECKPOINT-2

| TC# | Deskripsi | Status | Target |
|-----|-----------|--------|--------|
| C-08 | Dropdown petugas hanya tampilkan petugas bertag sesuai kategori | ✅ Pass | ✅ Pass |
| C-12 | Multi-select hingga 10 petugas | ✅ Pass | ✅ Pass |
| E-12 | Tidak bisa claim jika sudah 10 assignee | ✅ Pass | ✅ Pass |

### Definition of Done

- [ ] Kode ter-review minimal 1 orang
- [ ] Semua AC terpenuhi
- [ ] Test case C-08, C-12, E-12 lulus
- [ ] Tidak ada console error di web & mobile
- [ ] Tersedia di staging sebelum merge
```

---

### Contoh 2 — Tiket Feature Baru (Kompleks)

```markdown
## [feat] Workflow usulkan deaktivasi aset tidak terpakai >1 tahun

> **ID Tiket:** FSM-0102  
> **Tipe:** feat  
> **Prioritas:** 🟢 Regression  
> **Sprint Target:** Sprint-09  
> **Estimasi:** 4 hari  
> **Assignee:** @developer  
> **Versi Target:** 0.3.0  
> **Platform:** Web + Mobile  
> **Blocked by:** FSM-0103 (migrasi kolom `last_used_at` pada tabel `assets`)  

### Latar Belakang

RKF Bidang Sumber Daya Juni 2026 (Slide 04) menyebutkan keputusan MWA: aset yang tidak
digunakan lebih dari 1 tahun dapat diusulkan untuk dihapuskan. Diperlukan mekanisme
formal dalam FSM LAPOR! agar usulan ini tercatat, dapat diverifikasi pimpinan, dan
terintegrasi dengan data tiket.

### Deskripsi

Tambahkan tombol "Usulkan Deaktivasi" pada detail aset. Usulan memerlukan persetujuan
pimpinan. Jika disetujui, aset dinonaktifkan (`is_active=false`).

### Aktor & Role

| Role | Aksi | Catatan |
|------|------|---------|
| `PET` | Mengusulkan deaktivasi | Hanya jika `last_used_at` > 12 bulan lalu |
| `PIM` | Menyetujui / menolak usulan | — |
| `SA` | Menyetujui / menolak / deaktivasi paksa | — |
| `PEL` | Tidak bisa mengakses halaman aset | Redirect ke `/dashboard` |

### Master Data

Tag: semua · Kategori: tidak berlaku langsung

### Alur

1. Petugas buka detail aset (`/aset/:id`)
2. Jika `last_used_at` > 12 bulan: tombol "Usulkan Deaktivasi" tampil
3. Klik → modal konfirmasi: isi alasan (wajib, min. 20 karakter)
4. Sistem buat record `asset_deactivation_requests` dengan status `pending`
5. Notifikasi terkirim ke Pimpinan unit terkait
6. Pimpinan buka daftar usulan di `/dashboard/aset-deaktivasi`
7. Setujui → `is_active=false`, aset hilang dari picker buat tiket
8. Tolak → status `rejected`, catatan alasan penolakan tersimpan

### Database / API Changes

- Tabel baru: `asset_deactivation_requests` (`id`, `asset_id`, `requested_by`, `reason`, `status`, `reviewed_by`, `reviewed_at`, `rejection_note`)
- Kolom baru di `assets`: `last_used_at TIMESTAMPTZ`
- RLS: hanya PET unit sama & PIM yang bisa baca/tulis tabel baru
- RPC baru: `approve_deactivation_request(request_id uuid)`

### Acceptance Criteria

- [ ] AC-01: Tombol "Usulkan Deaktivasi" hanya muncul jika `last_used_at` > 12 bulan.
- [ ] AC-02: Alasan usulan wajib diisi minimal 20 karakter; submit disabled jika kurang.
- [ ] AC-03: Notifikasi terkirim ke Pimpinan unit aset setelah usulan dibuat.
- [ ] AC-04: Aset dengan status `pending` tidak bisa diusulkan ulang.
- [ ] AC-05: Setelah disetujui, aset tidak muncul di picker pembuatan tiket.
- [ ] AC-06: Role `PEL` tidak dapat mengakses halaman aset maupun endpoint API terkait.

### Test Case CHECKPOINT-2

| TC# | Deskripsi | Status | Target |
|-----|-----------|--------|--------|
| G-06 | Pelapor akses `/aset` → redirect | ✅ Pass | ✅ Pass |
| G-07 | Pimpinan akses `/aset` → redirect | ✅ Pass | ✅ Pass |
| G-09 | Update kondisi aset → auto-buat tiket | ✅ Pass | ✅ Pass |
| L-03 | Pimpinan coba hapus tiket via API | ✅ Pass | ✅ Pass |
| NEW-01 | PET usulkan deaktivasi aset >12 bln | 🆕 New | ✅ Pass |
| NEW-02 | PIM setujui usulan → aset nonaktif | 🆕 New | ✅ Pass |
| NEW-03 | PEL akses endpoint deaktivasi → 403 | 🆕 New | ✅ Pass |

### Definition of Done

- [ ] Tiket prasyarat FSM-0103 (migrasi) sudah merged
- [ ] Semua AC terpenuhi
- [ ] Test case lulus (termasuk NEW-01 s.d. NEW-03)
- [ ] Tidak ada console error
- [ ] Tersedia di staging sebelum merge ke main
```

---

*Dokumen ini mengacu pada CHECKPOINT-2.md (versi 0.2.0) dan RKF Bidang Sumber Daya Juni 2026.*  
*Update dokumen ini setiap kali ada perubahan master data atau kebijakan operasional baru dari Bidang Sumber Daya / Bidang TI & Komunikasi FSM.*
