# Web & Instagram Checker — Spesifikasi

## Deskripsi

Tool otomatis untuk mengecek dua hal utama:
1. **Kelengkapan konten website** — setiap menu tidak kosong dan topik-topik penting tercakup dalam berita/konten
2. **Performa Instagram** — jumlah follower dan cakupan topik penting pada postingan 3 bulan terakhir

---

## Target Website

| No | URL | Institusi |
|----|-----|-----------|
| 1 | https://fsm.undip.ac.id/ | Fakultas Sains dan Matematika |
| 2 | https://math.undip.ac.id/ | Departemen Matematika |
| 3 | https://bio.undip.ac.id/ | Departemen Biologi |
| 4 | https://fisika.undip.ac.id/ | Departemen Fisika |
| 5 | https://kimia.undip.ac.id/ | Departemen Kimia |
| 6 | https://stat.undip.ac.id/ | Departemen Statistika |
| 7 | https://if.undip.ac.id/ | Departemen Informatika |
| 8 | https://biotek.undip.ac.id/ | Departemen Bioteknologi |

## Target Instagram

| No | Akun | Institusi |
|----|------|-----------|
| 1 | https://www.instagram.com/fsmundip_official/ | Fakultas Sains dan Matematika |
| 2 | https://www.instagram.com/math.undip.official/ | Departemen Matematika |
| 3 | https://www.instagram.com/biologi_fsm_undip/ | Departemen Biologi |
| 4 | https://www.instagram.com/fisikaundip/ | Departemen Fisika |
| 5 | https://www.instagram.com/chemistry.diponegoro/ | Departemen Kimia |
| 6 | https://www.instagram.com/statistikaundip.official/ | Departemen Statistika |
| 7 | https://www.instagram.com/if.undip/ | Departemen Informatika |
| 8 | https://www.instagram.com/bioteknologi.undip/ | Departemen Bioteknologi |

---

## Modul 1: Website Checker (`check_website.py`)

### Cara Kerja
1. Crawl halaman utama (`/`) setiap website
2. Ekstrak semua item menu navigasi beserta link-nya
3. Kunjungi setiap halaman menu — cek apakah kontennya **tidak kosong** (ada teks bermakna, bukan hanya layout)
4. Crawl halaman berita/artikel terbaru
5. Analisis teks konten berita terhadap **7 topik wajib**

### Kriteria Pengecekan Menu
| Kondisi | Status |
|---------|--------|
| Halaman dapat diakses (HTTP 200) dan memiliki konten teks > 200 karakter | ✅ Ada & Terisi |
| Halaman dapat diakses tapi konten sangat sedikit (< 200 karakter) | ⚠️ Tipis |
| Halaman error / redirect tanpa konten | ❌ Kosong/Error |

### 7 Topik Wajib (Website & Instagram)
| No | Topik | Kata Kunci Pencarian |
|----|-------|----------------------|
| 1 | Prospek Kerja Lulusan | prospek kerja, karir, lapangan kerja, profil lulusan, alumni bekerja, career |
| 2 | Alumni | alumni, lulusan, tracer study, ikatan alumni |
| 3 | Kurikulum | kurikulum, mata kuliah, matkul, silabus, rencana studi, SKS, curriculum |
| 4 | Pendaftaran | pendaftaran, daftar, seleksi, SNBT, UTBK, SBMPTN, PMB, penerimaan mahasiswa |
| 5 | Fasilitas | fasilitas, laboratorium, lab, perpustakaan, gedung, sarana, prasarana, ruang |
| 6 | Prestasi | prestasi, penghargaan, award, juara, lomba, kompetisi, achievement |
| 7 | Riset & Pengabdian | riset, penelitian, pengabdian, publikasi, jurnal, research, PKM, abdimas |

### Output Website
- Tabel **Menu Coverage** — daftar menu + status konten (terisi/tipis/kosong)
- Tabel **Topik Coverage** — 7 topik × 8 website (✅/❌)
- Skor kelengkapan per website

---

## Modul 2: Instagram Checker (`check_instagram.py`)

### Cara Kerja
1. Akses halaman profil publik Instagram masing-masing akun
2. Ekstrak data: jumlah **followers**, **following**, **jumlah post**
3. Ekstrak caption postingan terbaru (minimal yang tersedia dari halaman profil)
4. Filter postingan dalam **3 bulan terakhir** berdasarkan timestamp
5. Analisis caption terhadap **7 topik wajib**

### Metode Scraping
- Menggunakan `requests` + parsing JSON dari `window._sharedData` atau endpoint GraphQL publik Instagram
- User-Agent browser digunakan agar tidak diblokir
- Fallback: ekstrak dari meta tags jika struktur JSON berubah

### Output Instagram
- Tabel **Follower Summary** — akun, followers, following, total post
- Tabel **Topik Coverage Postingan** — 7 topik × 8 akun untuk postingan 3 bulan terakhir
- Jumlah postingan yang dianalisis per akun

---

## Output Files

| File | Deskripsi |
|------|-----------|
| `website_report.md` | Laporan lengkap hasil cek website |
| `instagram_report.md` | Laporan lengkap hasil cek Instagram |
| `combined_report.md` | Laporan gabungan website + Instagram |

---

## Struktur Folder

```
web-ig-checker/
├── SPEC.md                  ← Spesifikasi ini
├── check_website.py         ← Script cek website
├── check_instagram.py       ← Script cek Instagram
├── run_all.py               ← Runner: jalankan semua checker sekaligus
├── requirements.txt         ← Dependensi Python
├── website_report.md        ← Output report website (auto-generated)
├── instagram_report.md      ← Output report Instagram (auto-generated)
└── combined_report.md       ← Output report gabungan (auto-generated)
```

---

## Cara Penggunaan

```bash
cd web-ig-checker
pip install -r requirements.txt

# Jalankan semua checker
python run_all.py

# Atau jalankan terpisah
python check_website.py
python check_instagram.py
```

---

## Teknologi

| Komponen | Detail |
|----------|--------|
| Bahasa | Python 3.11+ |
| HTTP Client | `requests` |
| HTML Parsing | `beautifulsoup4` |
| Output | Markdown (`.md`) |
| Encoding | UTF-8 |

---

## Catatan Teknis

- **Instagram**: Scraping dilakukan pada halaman publik tanpa login. Jika Instagram memblokir (rate limit / login wall), script akan memberikan pesan error dan melanjutkan ke akun berikutnya. Disarankan tambahkan delay antar request (2–5 detik).
- **Website**: Beberapa website mungkin memerlukan waktu load lebih lama. Default timeout adalah 15 detik.
- **Topik**: Pencocokan topik menggunakan regex case-insensitive pada teks halaman/caption. Hasil adalah deteksi keberadaan (ada/tidak ada), bukan frekuensi.

---

*Spesifikasi ini dibuat untuk keperluan audit kelengkapan konten digital FSM UNDIP.*
