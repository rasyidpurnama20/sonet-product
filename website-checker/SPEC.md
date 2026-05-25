# Website Completeness Checker - Spesifikasi

## Deskripsi

Tool otomatis untuk mengecek kelengkapan elemen-elemen penting pada website institusi/fakultas. Tool ini melakukan crawling pada halaman utama website dan mengidentifikasi keberadaan komponen-komponen standar yang seharusnya ada pada website resmi.

## Target Website

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

## Kriteria Pengecekan

Tool akan mengecek keberadaan elemen-elemen berikut:

| No | Elemen | Deskripsi |
|----|--------|-----------|
| 1 | **Logo** | Gambar logo institusi pada header |
| 2 | **Navigasi** | Menu navigasi utama |
| 3 | **Judul/Nama Institusi** | Nama fakultas/departemen yang jelas |
| 4 | **Kontak** | Informasi kontak (email, telepon, alamat) |
| 5 | **Media Sosial** | Link ke akun media sosial |
| 6 | **Footer** | Bagian footer website |
| 7 | **Berita/Artikel** | Konten berita atau artikel terbaru |
| 8 | **Gambar/Banner** | Hero image atau banner utama |
| 9 | **Search** | Fitur pencarian |
| 10 | **Responsive Meta** | Viewport meta tag (indikator mobile-friendly) |
| 11 | **SSL/HTTPS** | Penggunaan protokol HTTPS |
| 12 | **Favicon** | Ikon website pada tab browser |
| 13 | **Akreditasi/Visi-Misi** | Informasi akreditasi atau visi-misi |
| 14 | **Link Akademik** | Link ke sistem akademik (SIA, e-learning, dll.) |
| 15 | **Meta Description** | SEO meta description tag |

## Output

- File report dalam format Markdown (`.md`)
- Tabel ringkasan kelengkapan per website
- Skor persentase kelengkapan
- Timestamp pengecekan

## Teknologi

- **Bahasa**: Python 3.11
- **Library**: `requests`, `beautifulsoup4`
- **Output**: Markdown file

## Cara Penggunaan

```bash
cd website-checker
pip install -r requirements.txt
python check_website.py
```

Hasil report akan tersimpan di file `report.md`.
