# ICICoS Paper Review — Extraction Skill
> 3 langkah · ~20 menit · Gunakan di ChatGPT Plus Project
> Juni 2026

Upload PDF paper ke chat, lalu jalankan ketiga prompt di bawah **secara berurutan**.
Koreksi hasil AI sebelum lanjut ke langkah berikutnya.

---

## Langkah 1 — Kenali Paper  *(5 menit)*

```
Baca paper ini. Ekstrak informasi berikut — tulis apa yang ada di paper,
jangan analisis dulu. Jika tidak ada, tulis "Tidak disebutkan".

TIPE PAPER
[ ] ML / Deep Learning      [ ] Sistem / Implementasi
[ ] Survei / Review         [ ] Lainnya: ___

STRUKTUR
Centang yang ada (√), beri tanda silang yang tidak ada (✗),
beri ⚠ yang ada tapi bermasalah:
[ ] Abstract   [ ] Introduction   [ ] Related Work   [ ] Methodology
[ ] Results    [ ] Discussion     [ ] Conclusion     [ ] References

INTI PAPER
- Masalah yang diselesaikan (1 kalimat):
- Solusi yang diusulkan (nama metode/sistem + ide utamanya):
- Klaim kontribusi utama — kutip kalimat langsung dari paper:
- Keterbatasan yang diakui penulis (jika ada):
```

> **Koreksi manual:** pastikan klaim kontribusi benar-benar kutipan verbatim, bukan parafrase.

---

## Langkah 2 — Gali Isi  *(10 menit)*

Pilih blok sesuai tipe paper yang ditemukan di Langkah 1.

### Untuk ML / Deep Learning

```
Lanjutkan ekstraksi — hanya fakta, tanpa penilaian.

EKSPERIMEN
- Dataset (nama · ukuran · tahun rilis · sumber):
- Baseline yang dibandingkan (daftar nama + tahun):
- Metrik evaluasi yang digunakan:
- Hasil terbaik yang diklaim (angka per dataset per metrik, dari tabel mana):
- Apakah ada ablation study? [ ] Ya — komponen apa? [ ] Tidak
- Framework dan hardware:

REFERENSI
- Total referensi · termuda · tertua:
- Ada paper 2023–2025? [ ] Ya  [ ] Tidak
```

### Untuk Sistem / Implementasi

```
Lanjutkan ekstraksi — hanya fakta, tanpa penilaian.

SISTEM
- Komponen utama (daftar, referensi ke figure arsitektur):
- Teknologi stack (backend · frontend · database):
- Metrik evaluasi (latency · throughput · dll.):
- Status deployment: [ ] Production  [ ] Prototype  [ ] Simulasi
- Kode tersedia (open source)? [ ] Ya (URL: ___)  [ ] Tidak

REFERENSI
- Total referensi · termuda · tertua:
```

### Untuk Survei / Literature Review

```
Lanjutkan ekstraksi — hanya fakta, tanpa penilaian.

CAKUPAN
- Jumlah paper yang disurvei · rentang tahun:
- Database pencarian yang digunakan:
- Kriteria inklusi/eksklusi:
- Ada PRISMA diagram? [ ] Ya  [ ] Tidak

ANALISIS
- Kategorisasi / taksonomi yang digunakan:
- Research gap yang diidentifikasi:
- Ada tabel perbandingan paper? [ ] Ya (Table ___)  [ ] Tidak
```

> **Koreksi manual:** cek angka di tabel paper asli — AI sering salah baca angka dalam tabel.

---

## Langkah 3 — Cek Konsistensi  *(5 menit)*

```
Lakukan tiga pengecekan singkat pada paper ini.
Jawab ringkas dan spesifik — sebut nomor halaman, section, atau tabel.

1. ABSTRACT vs HASIL
   Untuk setiap klaim kuantitatif di abstract, apakah ada buktinya
   di section results / tabel / gambar?
   Format jawaban:
   • Klaim "[tulis klaim]" → Didukung di [Table/Fig X, hal Y] / Tidak ditemukan

2. REFERENSI
   Berapa persen referensi dari 2022–2025?
   Adakah metode SOTA yang relevan untuk topik ini yang tidak dikutip?

3. SATU HAL TERPENTING YANG HILANG
   Satu eksperimen, analisis, atau informasi yang seharusnya ada
   di paper ini tapi tidak ada sama sekali:
```

> **Koreksi manual:** verifikasi temuan "Tidak ditemukan" secara langsung di PDF.

---

## Sebelum Lanjut ke Prompts

- [ ] Klaim kontribusi adalah kutipan verbatim dari paper
- [ ] Angka-angka hasil sudah dicocokkan dengan tabel asli
- [ ] Kamu tahu: **mana yang paling lemah** dari paper ini

Lanjutkan ke `review-prompts.md`.
