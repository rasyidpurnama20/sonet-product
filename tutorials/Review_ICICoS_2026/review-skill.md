# Skill Ekstraksi Paper — ICICoS 2026

Sebelum mengisi form review, luangkan waktu untuk memahami paper dulu. Bukan berarti harus baca semua dari awal sampai akhir — tapi setidaknya kita tahu apa yang diklaim, bagaimana cara mereka membuktikannya, dan di mana celahnya.

Tiga prompt di bawah ini dirancang untuk dijalankan ke ChatGPT setelah kamu upload PDF paper. Jalankan berurutan, koreksi kalau AI salah baca, lalu pakai hasilnya sebagai bahan saat mengisi `review-template.docx`.

> AI bertugas mengumpulkan fakta dari paper. Penilaiannya tetap milik kamu.

---

## Prompt 1 — Gambaran Awal

Jalankan ini pertama. Tujuannya sederhana: tahu paper ini tentang apa, strukturnya lengkap tidak, dan apa yang diklaim penulis.

```
Baca paper ini dan ekstrak hal-hal berikut. Tulis apa adanya dari paper — jangan beri penilaian dulu, cukup fakta.

Tipe paper (pilih satu): ML/Deep Learning | Sistem/Implementasi | Survei | Lainnya

Kelengkapan struktur — tandai mana yang ada (✓), tidak ada (✗), atau ada tapi bermasalah (⚠):
Abstract · Introduction · Related Work · Methodology · Results · Discussion · Conclusion · References

Inti paper:
- Masalah yang coba diselesaikan (1 kalimat)
- Metode atau sistem yang diusulkan
- Klaim kontribusi utama — kutip langsung dari teks paper, jangan parafrase
- Keterbatasan yang diakui penulis (kalau ada)
```

Setelah dapat hasilnya, baca sebentar. Kalau klaim kontribusinya terasa berlebihan atau tidak sesuai isi paper, catat — itu bahan review yang berharga.

---

## Prompt 2 — Detail Teknis

Pilih blok sesuai tipe paper dari Prompt 1 tadi.

**Untuk paper ML / Deep Learning:**

```
Lanjutkan ekstraksi paper yang sama. Hanya fakta, belum perlu penilaian.

- Dataset: nama, ukuran, tahun rilis, sumber
- Metode pembanding (baseline): nama dan tahun publikasinya
- Metrik evaluasi yang digunakan
- Hasil terbaik yang diklaim — cantumkan angka, nama tabel atau gambar sumbernya
- Ada ablation study? Kalau iya, komponen apa yang diuji
- Framework, hardware, dan detail training (learning rate, epoch, batch size)
- Jumlah referensi, referensi termuda, referensi tertua
```

**Untuk paper Sistem / Implementasi:**

```
Lanjutkan ekstraksi paper yang sama. Hanya fakta, belum perlu penilaian.

- Komponen utama sistem — referensikan ke gambar arsitektur di paper
- Tech stack: backend, frontend, database
- Metrik yang diukur: latency, throughput, atau lainnya
- Status deployment: sudah production, masih prototype, atau simulasi saja
- Kode atau dataset tersedia publik? Kalau iya, di mana
- Jumlah referensi, referensi termuda, referensi tertua
```

**Untuk paper Survei / Literature Review:**

```
Lanjutkan ekstraksi paper yang sama. Hanya fakta, belum perlu penilaian.

- Rentang tahun dan jumlah paper yang disurvei
- Database pencarian yang digunakan
- Kriteria inklusi dan eksklusi
- Cara penulis mengkategorikan paper (taksonomi atau framework yang dipakai)
- Research gap yang diidentifikasi penulis
- Ada tabel perbandingan paper? Kalau iya, di tabel berapa
```

> Setelah prompt ini, cek angka-angka di tabel paper asli secara manual. AI cukup sering salah membaca angka dalam tabel, terutama kalau formatnya padat.

---

## Prompt 3 — Cek Konsistensi

Ini yang paling cepat tapi sering menemukan masalah paling substansial.

```
Dari paper yang sama, lakukan tiga pengecekan ini. Jawab ringkas, sebut nomor halaman atau nama tabel/gambar kalau relevan.

1. Cek abstract vs hasil
   Untuk setiap angka atau klaim di abstract — ada buktinya di section Results atau tabel? 
   Format: "Klaim '...' → didukung di Table X / tidak ditemukan"

2. Cek referensi
   Berapa persen referensi dari 2022–2025? 
   Ada metode atau paper penting di bidang ini yang seharusnya dikutip tapi tidak ada?

3. Satu hal yang paling mencolok hilang
   Satu eksperimen, analisis, atau informasi yang logisnya ada di paper ini tapi tidak ditemukan sama sekali.
```

---

## Sebelum lanjut ke review-prompts.md

Pastikan tiga hal ini sudah kamu punya:

- Klaim kontribusi yang dikutip langsung dari paper (bukan parafrase AI)
- Angka hasil yang sudah dicocokan dengan tabel aslinya
- Satu kelemahan paling mencolok yang kamu sendiri setuju

Kalau sudah, buka `review-prompts.md`.
