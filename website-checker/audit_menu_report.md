# Laporan Audit Kelengkapan Menu Website FSM UNDIP

**Tanggal Audit:** 25 Mei 2026  
**Metode:** Crawl otomatis + verifikasi manual  
**Cakupan:** 8 website (1 Fakultas + 7 Departemen)

---

## Legenda Status

| Simbol | Keterangan |
|:------:|------------|
| ✅ | Konten tersedia dan lengkap |
| ⚠️ | Ada masalah (konten tipis / bug / data parsial) |
| ❌ | Kosong / tidak dapat diakses / halaman tidak tersedia |
| 🔀 | Redirect ke domain/halaman lain |
| 🚫 | Menu tidak ada / tidak ditemukan |

---

## Ringkasan Masalah per Website

| Website | ✅ OK | ⚠️ Masalah | ❌ Kosong | 🔀 Redirect | 🚫 Menu Hilang |
|---------|:-----:|:----------:|:---------:|:-----------:|:--------------:|
| FSM | 15 | 2 | 4 | 1 | — |
| Matematika | 5 | 7 | 4 | 1 | 1 |
| Biologi | 8 | 8 | 3 | 1 | — |
| Fisika | 8 | 7 | 2 | 1 | 1 |
| Kimia | 10 | 4 | 2 | 1 | 2 |
| Statistika | 8 | 5 | 4 | 1 | — |
| Informatika | 11 | 4 | 3 | 1 | — |
| Bioteknologi | 10 | 6 | 1 | 1 | 1 |

---


## 1. FSM — Fakultas Sains dan Matematika
**URL:** https://fsm.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK |
| | Visi dan Misi | ✅ | OK |
| | Struktur Organisasi | ❌ | Halaman kosong (38 karakter) |
| | Pimpinan Fakultas | ✅ | OK |
| | Pimpinan Dept/Prodi | ✅ | OK |
| | Departemen | ✅ | OK |
| | Video Profil Fakultas | ✅ | Link ke YouTube — OK |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke pmb.undip.ac.id (bukan halaman internal) |
| **Akademik** | Badan Konsultasi Mahasiswa | ✅ | OK |
| | Kalender Akademik | ❌ | Kosong (66 karakter) |
| | Kurikulum | ❌ | Kosong (77 karakter) |
| | Peraturan Akademik | ✅ | OK |
| **Penelitian** | Penelitian | ✅ | OK |
| | Pengabdian Masyarakat | ✅ | OK |
| | Informasi Jurnal | ❌ | Kosong (80 karakter) |
| **Fasilitas** | Fasilitas | ✅ | OK |
| **Layanan Publik** | Pelayanan | ⚠️ | Teks "data belum tersedia" |
| | Survei & IKM | ✅ | OK |
| **Mutu** | Akreditasi | ⚠️ | Data belum tersedia (170 karakter) |
| | PPID | ✅ | OK |
| | Success Story | ✅ | OK |
| **SDGs** | SDGs | ✅ | OK |
| **Direktori** | Direktori | ✅ | OK |

**Temuan utama FSM:**
- Menu Struktur Organisasi, Kalender Akademik, Kurikulum, dan Informasi Jurnal kosong
- Pelayanan dan Akreditasi belum diisi
- PMB redirect ke domain pmb.undip.ac.id, tidak ada halaman PMB internal

---


## 2. Matematika — Departemen Matematika
**URL:** https://math.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ⚠️ | Konten sangat tipis (167 karakter) |
| **Profil** | Sejarah | ✅ | OK |
| | Visi & Misi | ✅ | OK |
| | Pimpinan Dept/Prodi | ✅ | OK |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ✅ | OK |
| | Video Profil | ❌ | Kosong (18 karakter) |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke admission.undip.ac.id (bukan halaman B.Indonesia internal) |
| **Akademik** | Kalender Akademik | ✅ | OK |
| | Peraturan Akademik | ❌ | Data belum tersedia |
| | Kurikulum | ⚠️ | Konten sangat tipis (224 karakter), belum lengkap |
| | Akreditasi | ❌ | Kosong (18 karakter) |
| **Penelitian** | Penelitian | ✅ | OK |
| | Pengabdian Masyarakat | ⚠️ | Konten sangat tipis (328 karakter) |
| | Publikasi | ❌ | Data belum tersedia |
| **Fasilitas** | Fasilitas | ⚠️ | Konten sangat tipis (165 karakter) |
| **Layanan Publik** | Pelayanan / Layanan | ❌ | Data belum tersedia |
| | Survei 2024 | ⚠️ | Hasil survei tidak dapat diakses |
| **Direktori** | Direktori | ❌ | Kosong (66 karakter) |
| **Alumni Corner** | Alumni Corner | 🚫 | **Tidak ada di menu navigasi** |

**Temuan utama Matematika:**
- Video Profil, Akreditasi, Publikasi, Layanan, Direktori: kosong/tidak tersedia
- Peraturan Akademik, Kurikulum belum lengkap
- PMB redirect ke admission.undip.ac.id (bahasa Inggris), bukan halaman B.Indonesia
- Menu Alumni Corner tidak ada di navigasi
- Survei tidak dapat diakses

---


## 3. Biologi — Departemen Biologi
**URL:** https://bio.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK |
| | Visi & Misi | ⚠️ | Bug table of content (anchor internal rusak) |
| | Pimpinan Dept/Prodi | ✅ | OK |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ❌ | Bug table of content + profil kosong (96 karakter) |
| | Video Profil | ❌ | Data belum tersedia (37 karakter) |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke admission.undip.ac.id (B.Indonesia) |
| **Akademik** | Kalender Akademik | ⚠️ | Konten tipis (331 karakter) |
| | Peraturan Akademik | ⚠️ | Konten tipis (323 karakter) |
| | Informasi Kurikulum | ✅ | OK |
| | Peta Kurikulum (Matriks SSC-CPL) | ❌ | Halaman tidak tersedia (kosong 110 karakter) |
| | Distribusi Mata Kuliah | ⚠️ | Bug table of content |
| | RPS | ✅ | OK |
| | Akreditasi | ✅ | OK |
| **Penelitian** | Pengabdian Masyarakat | ❌ | Data belum tersedia |
| | Publikasi | ⚠️ | Foto/gambar tidak ter-load |
| **Fasilitas** | Fasilitas (Lab) | ⚠️ | Foto laboratorium tidak ter-load |
| | Perpustakaan | ❌ | Data belum tersedia |
| **Alumni Corner** | Alumni Corner | ✅ | OK |
| **Layanan Publik** | Pelayanan | ❌ | Bug table of content + data belum tersedia |
| | Survei & IKM | ⚠️ | Bug table of content + hasil survei tidak dapat diakses |
| **Direktori** | Direktori | ⚠️ | Bug table of content |
| **MBKM** | Merdeka Belajar Kampus Merdeka | ✅ | OK |

**Temuan utama Biologi:**
- Bug table of content tersebar di banyak halaman (Visi Misi, Tenaga Kependidikan, Distribusi MK, Pelayanan, Survei, Direktori)
- Foto tidak ter-load di Publikasi dan Fasilitas
- Peta Kurikulum (Matriks SSC-CPL): halaman tidak tersedia
- Video Profil, Pengabdian Masy, Perpustakaan, Pelayanan: kosong/belum tersedia
- PMB redirect ke admission.undip.ac.id (bahasa Inggris)

---


## 4. Fisika — Departemen Fisika
**URL:** https://fisika.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK |
| | Visi & Misi | ✅ | OK |
| | Pimpinan Dept/Prodi | ❌ | Konten sangat kosong (116 karakter) |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ⚠️ | Konten sangat tipis (166 karakter) |
| | Video Profil | ❌ | Kosong (18 karakter) |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke admission.undip.ac.id (B.Indonesia) |
| **Akademik** | Kalender Akademik | ⚠️ | Konten tipis (331 karakter) |
| | Peraturan Akademik | ⚠️ | Data belum tersedia, konten tipis (132 karakter) |
| | Kurikulum | ✅ | OK — konten lengkap (11.907 karakter) |
| | Akreditasi | ⚠️ | Konten sangat tipis (162 karakter) |
| **Penelitian** | Penelitian | ✅ | OK |
| | Pengabdian Masyarakat | ❌ | Data belum tersedia |
| | Publikasi | ⚠️ | Konten sangat tipis (155 karakter) |
| **Fasilitas** | Fasilitas | ✅ | OK |
| **Alumni Corner** | Alumni Corner | 🚫 | **Tidak ada di menu navigasi** |
| **Layanan Publik** | Pelayanan | ❌ | Data belum tersedia |
| | Survei & IKM | ✅ | OK |
| **Direktori** | Direktori | ✅ | OK |

**Temuan utama Fisika:**
- Pimpinan Dept dan Video Profil: kosong
- Tenaga Kependidikan, Kalender Akademik, Peraturan Akademik, Akreditasi, Publikasi: tipis/belum lengkap
- Pengabdian Masyarakat dan Pelayanan: data belum tersedia
- Alumni Corner tidak ada di menu
- PMB redirect ke admission.undip.ac.id

---


## 5. Kimia — Departemen Kimia
**URL:** https://kimia.undip.ac.id/  
*Catatan: Website Kimia menggunakan antarmuka Bahasa Inggris*

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda / Home | — | ✅ | OK |
| **Profil** | History (Sejarah) | ✅ | OK |
| | Vision & Mission | ✅ | OK |
| | Executive Board (Pimpinan) | ⚠️ | Konten sangat tipis (174 karakter) |
| | Lecturer Profile (Profil Dosen) | ✅ | OK |
| | Staff (Tenaga Kependidikan) | ✅ | OK |
| | Video Profile | ❌ | Kosong (20 karakter) |
| **PMB** | Admission | 🔀 | Redirect ke admission.undip.ac.id — halaman B.Indonesia tidak ada |
| **Akademik** | Academic Calendar | ✅ | OK |
| | Academic Regulation | ❌ | Buku pedoman kembali/redirect ke laman Peraturan Akademik (loop), kosong (99 karakter) |
| | Curriculum | ⚠️ | Data belum tersedia (crawl: OK 3628chr, tapi user konfirmasi kosong) |
| | Accreditation | ⚠️ | Konten sangat tipis (210 karakter) |
| **Penelitian** | Research | ✅ | OK |
| | Community Service | ⚠️ | Data belum tersedia |
| | Publikasi | 🚫 | **Tidak ada menu Publikasi** |
| **Fasilitas** | Facilities | ✅ | OK |
| **Alumni Corner** | Alumni Corner | 🚫 | **Tidak ada di menu navigasi** |
| **Layanan Publik** | Services (Pelayanan) | ⚠️ | Konten tipis (347 karakter), data belum tersedia |
| | Satisfaction Survey | ✅ | Link tersedia, tapi hasil survei tidak dapat diakses |
| **Direktori** | Directory | ✅ | OK |
| **Jadwal** | Jadwal Matkul | ❌ | Data belum tersedia |
| | Jadwal UTS | ❌ | Data belum tersedia |
| | Jadwal UAS | ❌ | Data belum tersedia |

**Temuan utama Kimia:**
- Video Profile, Academic Regulation (loop/redirect): kosong
- Jadwal Matkul, UTS, UAS: data belum tersedia
- Community Service: data belum tersedia
- Menu Publikasi dan Alumni Corner tidak ada di navigasi
- PMB hanya ada dalam Bahasa Inggris (admission), tidak ada versi B.Indonesia
- Survei tidak dapat diakses

---


## 6. Statistika — Departemen Statistika
**URL:** https://stat.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK |
| | Visi & Misi | ✅ | OK |
| | Pimpinan Dept/Prodi | ⚠️ | Konten sangat tipis (167 karakter) |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ⚠️ | Konten tipis (274 karakter) |
| | Video Profil | ❌ | Kosong (18 karakter) |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke admission.undip.ac.id (B.Indonesia) |
| **Akademik** | Kalender Akademik | ⚠️ | Konten tipis (331 karakter) |
| | Peraturan Akademik | ✅ | OK |
| | Kurikulum | ❌ | Kosong + data belum tersedia (36 karakter) |
| | Akreditasi | ❌ | Kosong (18 karakter) |
| **Penelitian** | Penelitian | ❌ | Kosong (33 karakter) |
| | Pengabdian Masyarakat | ✅ | OK |
| | Publikasi | ⚠️ | Konten sangat tipis (136 karakter) |
| **Fasilitas** | Fasilitas | ✅ | OK — sangat lengkap (10.237 karakter) |
| **Alumni Corner** | Alumni Corner | ✅ | OK |
| **Layanan Publik** | Pelayanan | ❌ | Data belum tersedia |
| | Survei & IKM | ✅ | OK |
| **Direktori** | Direktori | ✅ | OK |

**Temuan utama Statistika:**
- Video Profil, Kurikulum, Akreditasi, Penelitian: kosong/belum tersedia
- Pimpinan Dept, Tenaga Kependidikan, Kalender Akademik, Publikasi: konten sangat tipis
- Pelayanan: data belum tersedia
- PMB redirect ke admission.undip.ac.id

---


## 7. Informatika — Departemen Informatika
**URL:** https://if.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK |
| | Visi & Misi | ✅ | OK — konten lengkap (2.243 karakter) |
| | Pimpinan Dept/Prodi | ⚠️ | Konten sangat tipis (174 karakter) |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ⚠️ | Konten tipis (182 karakter) |
| | Video Profil | ❌ | Kosong (18 karakter) |
| | Kepakaran | ✅ | Link ke scholar.undip.ac.id — OK |
| **PMB** | PMB | 🔀 | Redirect ke pmb.undip.ac.id (bukan halaman internal) |
| **Akademik** | Kalender Akademik | ⚠️ | Konten tipis (331 karakter) |
| | Peraturan Akademik | ❌ | Kosong (102 karakter) |
| | Kurikulum | ✅ | OK — konten sangat lengkap (7.087 karakter) |
| | Akreditasi | ✅ | OK |
| | Informasi Tugas Akhir | ⚠️ | Konten tipis (139 karakter) |
| **Penelitian** | Laboratorium Riset | ✅ | OK — konten lengkap (4.925 karakter) |
| | Publikasi | ❌ | Kosong (111 karakter) |
| **Fasilitas** | Fasilitas | ✅ | OK |
| **Layanan Publik** | Pelayanan | ✅ | OK |
| | Survei & IKM | ✅ | OK |
| **Direktori** | Direktori | ✅ | OK |
| **Success Story** | Success Story | ✅ | OK — ada konten alumni karir |

**Temuan utama Informatika:**
- Video Profil, Peraturan Akademik, Publikasi: kosong
- Pimpinan Dept, Tenaga Kependidikan, Kalender Akademik, Info Tugas Akhir: konten tipis
- PMB redirect ke pmb.undip.ac.id
- **Unggul:** Visi Misi, Kurikulum, Akreditasi, Lab Riset, Pelayanan, Direktori semua OK

---


## 8. Bioteknologi — Departemen Bioteknologi
**URL:** https://biotek.undip.ac.id/

| Menu | Sub-Menu | Status | Keterangan |
|------|----------|:------:|------------|
| Beranda | — | ✅ | OK |
| **Profil** | Sejarah | ✅ | OK — sangat lengkap (4.857 karakter) |
| | Visi & Misi | ✅ | OK |
| | Pimpinan Dept/Prodi | ⚠️ | Konten tipis (338 karakter) |
| | Profil Dosen | ✅ | OK |
| | Tenaga Kependidikan | ⚠️ | Konten tipis (316 karakter) |
| | Video Profil | ❌ | Data belum tersedia (37 karakter) |
| **PMB** | Penerimaan Mahasiswa Baru | 🔀 | Redirect ke admission.undip.ac.id (B.Indonesia) |
| **Akademik** | Kalender Akademik | ⚠️ | Konten tipis (239 karakter) |
| | Peraturan Akademik | ✅ | OK |
| | Kurikulum | ✅ | OK — konten lengkap (3.346 karakter) |
| | Akreditasi | ⚠️ | Konten tipis (318 karakter) |
| **Penelitian** | Penelitian | ✅ | OK |
| | Pengabdian Masyarakat | ❌ | Data belum tersedia |
| | Publikasi | ✅ | OK |
| **Fasilitas** | Fasilitas | ✅ | OK — konten lengkap (4.037 karakter) |
| **Alumni Corner** | Alumni Corner | 🚫 | **Tidak ada di menu navigasi** |
| **Layanan Publik** | Pelayanan | ❌ | Data belum tersedia |
| | Survei & IKM | ✅ | OK |
| **Direktori** | Direktori | ✅ | OK — konten lengkap (4.345 karakter) |

**Temuan utama Bioteknologi:**
- Video Profil, Pengabdian Masyarakat, Pelayanan: kosong/data belum tersedia
- Pimpinan Dept, Tenaga Kependidikan, Kalender Akademik, Akreditasi: konten tipis
- Alumni Corner tidak ada di menu navigasi
- PMB redirect ke admission.undip.ac.id

---


---

## Rekap Masalah Lintas Website

### A. Masalah yang Muncul di SEMUA / Hampir Semua Website

| No | Masalah | Website Terdampak |
|----|---------|-------------------|
| 1 | **PMB redirect ke admission/pmb.undip.ac.id** (bukan halaman B.Indonesia internal) | FSM, Mat, Bio, Fis, Kim, Stat, IF, Biotek *(semua)* |
| 2 | **Video Profil kosong** | Mat, Bio, Fis, Kim, Stat, IF, Biotek *(7/8)* |
| 3 | **Kalender Akademik konten tipis** | FSM, Bio, Fis, Stat, IF, Biotek *(6/8)* |
| 4 | **Pelayanan data belum tersedia** | FSM, Mat, Bio, Fis, Kim, Stat, Biotek *(7/8)* |
| 5 | **Pimpinan Dept/Prodi konten tipis** | Fis, Stat, IF, Biotek *(4/8)* |
| 6 | **Tenaga Kependidikan kosong/tipis** | Bio, Fis, Stat, IF, Biotek *(5/8)* |
| 7 | **Akreditasi kosong atau tipis** | FSM, Mat, Fis, Kim, Stat, Biotek *(6/8)* |

### B. Masalah Bug Teknis

| No | Bug | Website |
|----|-----|---------|
| 1 | Bug **Table of Content** (anchor internal rusak) | Biologi (Visi Misi, Tenaga Kependidikan, Distribusi MK, Pelayanan, Survei, Direktori) |
| 2 | **Foto/gambar tidak ter-load** | Biologi (Publikasi, Fasilitas Lab) |
| 3 | **Loop redirect** Academic Regulation | Kimia |
| 4 | Halaman Peta Kurikulum **tidak tersedia** (404) | Biologi |
| 5 | **Survei tidak dapat diakses** | Mat, Bio, Kim |

### C. Menu Tidak Ada / Hilang dari Navigasi

| No | Menu yang Hilang | Website |
|----|-----------------|---------|
| 1 | **Alumni Corner** tidak ada di navigasi | Mat, Fis, Kim, Biotek |
| 2 | **Publikasi** tidak ada di menu Penelitian | Kimia |
| 3 | **Jadwal Matkul / UTS / UAS** data kosong | Kimia |

### D. Konten Data Belum Tersedia (per kategori)

| Kategori | Website dengan Masalah |
|----------|----------------------|
| Peraturan Akademik | Mat, Fis |
| Kurikulum | Mat, Stat |
| Pengabdian Masyarakat | Bio, Fis, Kim, Biotek |
| Publikasi | Mat, Kim |
| Direktori | Mat |
| Penelitian | Stat |

---


---

## Tabel Matriks Kelengkapan Menu (Ringkasan Visual)

> **Y** = Ada & OK &nbsp;|&nbsp; **⚠** = Ada tapi bermasalah &nbsp;|&nbsp; **✗** = Kosong/tidak tersedia &nbsp;|&nbsp; **🔀** = Redirect keluar &nbsp;|&nbsp; **—** = Tidak ada menu

| Menu / Konten | FSM | MAT | BIO | FIS | KIM | STAT | IF | BIOTEK |
|---------------|:---:|:---:|:---:|:---:|:---:|:----:|:--:|:------:|
| **Beranda** | Y | ⚠ | Y | Y | Y | Y | Y | Y |
| **Sejarah** | Y | Y | Y | Y | Y | Y | Y | Y |
| **Visi & Misi** | Y | Y | ⚠ | Y | Y | Y | Y | Y |
| **Struktur Organisasi** | ✗ | — | — | — | — | — | — | — |
| **Pimpinan Dept** | Y | Y | Y | ✗ | ⚠ | ⚠ | ⚠ | ⚠ |
| **Profil Dosen** | Y | Y | Y | Y | Y | Y | Y | Y |
| **Tenaga Kependidikan** | — | Y | ✗ | ⚠ | Y | ⚠ | ⚠ | ⚠ |
| **Video Profil** | Y | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **PMB (B.Indonesia)** | 🔀 | 🔀 | 🔀 | 🔀 | 🔀 | 🔀 | 🔀 | 🔀 |
| **Kalender Akademik** | ✗ | Y | ⚠ | ⚠ | Y | ⚠ | ⚠ | ⚠ |
| **Peraturan Akademik** | Y | ✗ | ⚠ | ⚠ | ✗ | Y | ✗ | Y |
| **Kurikulum** | ✗ | ⚠ | Y | Y | ⚠ | ✗ | Y | Y |
| **Akreditasi** | ⚠ | ✗ | Y | ⚠ | ⚠ | ✗ | Y | ⚠ |
| **Penelitian** | Y | Y | — | Y | Y | ✗ | — | Y |
| **Pengabdian Masy** | Y | ⚠ | ✗ | ✗ | ✗ | Y | — | ✗ |
| **Publikasi** | ⚠ | ✗ | ⚠ | ⚠ | — | ⚠ | ✗ | Y |
| **Fasilitas** | Y | ⚠ | ⚠ | Y | Y | Y | Y | Y |
| **Alumni Corner** | Y | — | Y | — | — | Y | Y | — |
| **Pelayanan** | ✗ | ✗ | ✗ | ✗ | ⚠ | ✗ | Y | ✗ |
| **Survei IKM** | Y | ⚠ | ⚠ | Y | ⚠ | Y | Y | Y |
| **Direktori** | Y | ✗ | ⚠ | Y | Y | Y | Y | Y |

---

## Prioritas Perbaikan

### 🔴 Prioritas Tinggi (Bermasalah di semua / hampir semua website)
1. **Buat halaman PMB dalam Bahasa Indonesia** untuk setiap departemen — semua website saat ini hanya mengarah ke admission.undip.ac.id
2. **Isi konten Video Profil** — 7 dari 8 departemen masih kosong
3. **Isi konten Pelayanan** — 7 dari 8 departemen belum tersedia
4. **Lengkapi Akreditasi** — 6 dari 8 departemen kosong atau sangat tipis
5. **Tambah konten Kalender Akademik** — mayoritas hanya memuat informasi sangat minimum

### 🟡 Prioritas Sedang (Bermasalah di beberapa website)
6. **Perbaiki bug Table of Content** di Biologi (6 halaman terdampak)
7. **Perbaiki foto yang tidak ter-load** di Biologi (Publikasi dan Fasilitas)
8. **Lengkapi Pengabdian Masyarakat** — Bio, Fis, Kim, Biotek belum tersedia
9. **Tambahkan menu Alumni Corner** di Matematika, Fisika, Kimia, Bioteknologi
10. **Tambahkan menu Publikasi** di Kimia
11. **Perbaiki loop redirect** Academic Regulation di Kimia

### 🟢 Prioritas Normal (Per departemen)
12. **Matematika:** Isi Peraturan Akademik, Kurikulum, Akreditasi, Direktori, Layanan
13. **Statistika:** Isi Kurikulum, Akreditasi, Penelitian, Publikasi
14. **Informatika:** Isi Peraturan Akademik, Publikasi, lengkapi Pimpinan Dept
15. **Kimia:** Isi Jadwal Matkul/UTS/UAS, perbaiki Academic Regulation
16. **FSM:** Isi Struktur Organisasi, Kurikulum, Informasi Jurnal

---

*Laporan ini di-generate dari hasil crawl otomatis + verifikasi manual pada 25 Mei 2026.*  
*Sumber data: script `check_website.py` + audit manual oleh tim.*
