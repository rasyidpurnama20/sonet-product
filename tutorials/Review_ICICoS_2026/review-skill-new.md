# Skill Ekstraksi Paper — ICICoS 2026

Tujuan dokumen ini: membantu kamu membaca paper lebih cepat dan lebih terarah sebelum mengisi form review. Tiga prompt di bawah dijalankan ke ChatGPT setelah PDF paper diupload ke chat.

Jalankan berurutan. Koreksi hasil AI sebelum lanjut — AI bisa salah baca tabel dan angka.

---

## Prompt 1 — Gambaran Awal

```
Baca paper ini. Tulis hanya fakta dari paper — belum perlu penilaian.

Tipe paper: ML/Deep Learning | Sistem/Implementasi | Survei | Lainnya

Struktur yang ada (✓), tidak ada (✗), ada tapi bermasalah (⚠):
Abstract · Introduction · Related Work · Methodology · Results · Discussion · Conclusion · References

Inti:
- Masalah yang diselesaikan (1 kalimat)
- Metode atau sistem yang diusulkan
- Klaim kontribusi — kutip langsung dari teks, jangan parafrase
- Keterbatasan yang diakui penulis (kalau ada)
```

> Cek: klaim kontribusinya realistis atau terlalu berlebihan dibanding isi paper?

---

## Prompt 2 — Detail Teknis

Pilih blok yang sesuai tipe paper dari Prompt 1.

**ML / Deep Learning**

```
Lanjutkan dari paper yang sama — hanya fakta.

- Dataset: nama, ukuran, tahun, sumber
- Baseline yang dibandingkan: nama dan tahun publikasi
- Metrik evaluasi
- Hasil terbaik yang diklaim — angka dan nama tabel/gambar sumbernya
- Ada ablation study? Kalau iya, komponen apa
- Framework, hardware, detail training (lr, epoch, batch size)
- Total referensi, referensi termuda, referensi tertua
```

**Sistem / Implementasi**

```
Lanjutkan dari paper yang sama — hanya fakta.

- Komponen utama sistem — referensikan ke gambar arsitektur
- Tech stack: backend, frontend, database
- Metrik yang diukur: latency, throughput, atau lainnya
- Status: production, prototype, atau simulasi
- Kode tersedia publik? Di mana
- Total referensi, referensi termuda, referensi tertua
```

**Survei / Literature Review**

```
Lanjutkan dari paper yang sama — hanya fakta.

- Jumlah paper yang disurvei dan rentang tahunnya
- Database pencarian yang digunakan
- Kriteria inklusi dan eksklusi
- Cara penulis mengkategorikan paper
- Research gap yang diidentifikasi
- Ada tabel perbandingan? Di tabel berapa
```

> Setelah prompt ini: buka paper asli dan cocokkan angka di tabel. AI sering salah baca angka dalam tabel yang rapat.

---

## Prompt 3 — Cek Konsistensi

```
Dari paper yang sama, jawab tiga hal ini secara ringkas — sebut halaman atau tabel kalau relevan.

1. Abstract vs hasil
   Tiap klaim kuantitatif di abstract — ada buktinya di results atau tabel?
   Format: "Klaim '...' → ada di Table X" atau "→ tidak ditemukan"

2. Referensi
   Berapa persen dari 2022–2025? Ada metode penting di bidang ini yang seharusnya dikutip tapi tidak ada?

3. Satu hal paling mencolok yang hilang
   Satu eksperimen, analisis, atau informasi yang logisnya ada tapi tidak ditemukan di paper ini.
```

---

## Sebelum lanjut ke form review

Tiga hal yang harus kamu punya sebelum mengisi:

- [ ] Klaim kontribusi yang dikutip verbatim dari paper
- [ ] Angka hasil yang sudah dicek di tabel asli
- [ ] Kelemahan utama yang kamu sendiri setuju — bukan hanya hasil AI

Kalau sudah, buka `review-prompts-new.md` untuk draft review dan pengisian form.
