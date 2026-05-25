# Website & Instagram Completeness Checker - Spesifikasi

## Deskripsi

Tool otomatis untuk mengecek kelengkapan website institusi/fakultas dan akun Instagram resmi UNDIP. Tool ini terdiri dari dua script utama:

1. **`check_website.py`** — Mengecek kelengkapan website dari sisi elemen UI, kelengkapan menu, dan topik berita.
2. **`check_instagram.py`** — Mengecek jumlah follower dan menganalisis topik postingan Instagram dalam 3 bulan terakhir.

## Target

### Website (8 situs)

| No | Website | Institusi |
|----|---------|-----------|
| 1 | https://fsm.undip.ac.id/ | Fakultas Sains dan Matematika |
| 2 | https://math.undip.ac.id/ | Departemen Matematika |
| 3 | https://bio.undip.ac.id/ | Departemen Biologi |
| 4 | https://fisika.undip.ac.id/ | Departemen Fisika |
| 5 | https://kimia.undip.ac.id/ | Departemen Kimia |
| 6 | https://stat.undip.ac.id/ | Departemen Statistika |
| 7 | https://if.undip.ac.id/ | Departemen Informatika |
| 8 | https://biotek.undip.ac.id/ | Departemen Bioteknologi |

### Akun Instagram (8 akun)

| No | Username | Institusi |
|----|----------|-----------|
| 1 | @fsmundip_official | Fakultas Sains dan Matematika |
| 2 | @math.undip.official | Departemen Matematika |
| 3 | @biologi_fsm_undip | Departemen Biologi |
| 4 | @fisikaundip | Departemen Fisika |
| 5 | @chemistry.diponegoro | Departemen Kimia |
| 6 | @statistikaundip.official | Departemen Statistika |
| 7 | @if.undip | Departemen Informatika |
| 8 | @bioteknologi.undip | Departemen Bioteknologi |

## Pengecekan Website

### A. Kelengkapan Elemen UI (15 kriteria)

| No | Elemen | Deskripsi |
|----|--------|-----------|
| 1 | Logo | Logo institusi pada header |
| 2 | Navigasi | Menu navigasi utama |
| 3 | Nama Institusi | Nama fakultas/departemen yang jelas |
| 4 | Kontak | Email, telepon, alamat |
| 5 | Media Sosial | Link akun media sosial |
| 6 | Footer | Bagian footer website |
| 7 | Berita/Artikel | Konten berita atau artikel |
| 8 | Banner/Hero Image | Hero image / slider |
| 9 | Search | Fitur pencarian |
| 10 | Responsive Meta | Viewport meta tag |
| 11 | SSL/HTTPS | Penggunaan protokol HTTPS |
| 12 | Favicon | Ikon website pada tab |
| 13 | Akreditasi/Visi-Misi | Info akreditasi atau visi-misi |
| 14 | Link Akademik | Link ke sistem akademik (SIA, e-learning) |
| 15 | Meta Description | SEO meta description |

### B. Kelengkapan Konten Setiap Menu

- Tool melakukan crawl ke link-link menu utama dari navigasi.
- Setiap halaman menu di-fetch, lalu konten utama (di luar nav/header/footer) dihitung.
- Halaman dianggap "kosong" jika konten utama < 200 karakter.
- Maksimum 12 menu dicek per website (untuk efisiensi).

### C. Topik Berita yang Dimuat

Tool men-crawl link berita/artikel dari halaman utama, kemudian setiap berita diperiksa apakah memuat informasi tentang:

| Topik | Kata kunci yang dicari |
|-------|-----------------------|
| **Prospek Kerja Lulusan** | prospek kerja, peluang kerja, career, karir, tracer study, dunia kerja |
| **Alumni** | alumni, alumnus, wisuda, ikatan alumni, iluni |
| **Kurikulum** | kurikulum, mata kuliah, silabus, sks, RPS |
| **Pendaftaran** | pendaftaran, SNBP, SNBT, UM Undip, calon mahasiswa, PMB |
| **Fasilitas** | fasilitas, laboratorium, ruang kuliah, perpustakaan, sarana prasarana |
| **Prestasi** | prestasi, juara, lomba, kompetisi, penghargaan, medali |
| **Riset dan Pengabdian** | riset, penelitian, publikasi, pengabdian, P2M, PKM, abdimas |

Sekaligus dicek **kebaruan berita** — apakah ada berita yang dipost dalam 6 bulan terakhir.

## Pengecekan Instagram

### A. Data Profil

- Jumlah followers
- Jumlah following
- Jumlah total posts
- Bio dan informasi profil

### B. Analisis Postingan 3 Bulan Terakhir

Setiap caption postingan dianalisis untuk topik yang sama dengan website (prospek kerja, alumni, kurikulum, pendaftaran, fasilitas, prestasi, riset & pengabdian). Hasilnya berupa jumlah postingan yang membahas tiap topik.

### Catatan Teknis Instagram

Instagram aktif memblokir scraping dari **IP datacenter / cloud** (HTTP 302/403). Konsekuensinya:

- Jika dijalankan dari sandbox/cloud, sebagian besar akun akan **gagal** di-fetch.
- **Untuk hasil terbaik**, jalankan script dari komputer lokal.
- Sebagai fallback, tersedia file `manual_ig_data.json` untuk input data secara manual.

## Output

| File | Deskripsi |
|------|-----------|
| `report.md` | Laporan kelengkapan website (elemen UI + menu + topik berita) |
| `instagram_report.md` | Laporan Instagram (followers + topik postingan) |

## Teknologi

- **Bahasa**: Python 3.11+
- **Library**: `requests`, `beautifulsoup4`, `instaloader`
- **Output**: Markdown

## Cara Penggunaan

```bash
cd website-checker
pip install -r requirements.txt

# Cek website
python check_website.py

# Cek Instagram (jalankan dari komputer lokal untuk hasil terbaik)
python check_instagram.py
```

## Struktur File

```
website-checker/
├── SPEC.md                  # File ini
├── requirements.txt         # Python dependencies
├── check_website.py         # Script pengecekan website
├── check_instagram.py       # Script pengecekan Instagram
├── manual_ig_data.json      # Fallback manual untuk data Instagram
├── report.md                # Output laporan website
└── instagram_report.md      # Output laporan Instagram
```
