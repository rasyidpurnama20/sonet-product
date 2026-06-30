# Investigasi Nilai Tugas — OAK MIK1624201 Kelas A

**Mata Kuliah:** MIK1624201 - Organisasi dan Arsitektur Komputer
**Kelas:** A | **Tahun Ajaran:** 2025 Genap
**File sumber:** `nilai-oak/OAK_MIK1624201_2025_2_A.xlsx` (sheet `Worksheet`)
**Tanggal investigasi:** 30 Juni 2026

## Latar Belakang

Investigasi ini berawal dari pengecekan nilai Tugas 01 dan Tugas 02 atas nama
**CINDY CLAUDIA SIHOTANG** (NIM 24060125120049). Nilai Tugas 02 yang tampil = **20**,
yang sekilas terlihat sangat rendah pada skala 0-100.

## Temuan Cindy Claudia Sihotang

| Komponen | Nilai (apa adanya di file) |
|----------|----------------------------|
| Tugas 01 (Nilai 0-100) | 68,75 |
| Tugas 02 (Nilai 0-100) | 20 |

## Temuan Utama: Anomali Skala Kolom "Tugas 02"

Setelah memeriksa seluruh 39 mahasiswa di kelas A, ditemukan ketidaksesuaian antara
**label kolom** dan **rentang nilai aktual**:

| Kolom | Label di header | Min | Max | Rata-rata | Nilai unik yang muncul |
|-------|-----------------|-----|-----|-----------|------------------------|
| Tugas 01 | "Tugas 01 (Nilai 0-100)" | 50 | 100 | 87,90 | 50; 62,5; 65,62; 68,75; 71,88; 75; 84,38; 87,5; 90,62; 93,75; 96,88; 100 |
| Tugas 02 | "Tugas 02 (Nilai 0-100)" | 0 | 20 | 9,23 | **hanya 0, 10, dan 20** |

### Interpretasi

- Kolom **Tugas 01** sudah berada pada skala 0-100 (sesuai label).
- Kolom **Tugas 02** secara label tertulis 0-100, **namun seluruh nilainya hanya 0/10/20**.
  Ini sangat kuat mengindikasikan kolom tersebut sebenarnya diisi pada **skala 0-20**,
  bukan 0-100. Jadi nilai "20" milik Cindy sebenarnya adalah **nilai maksimum** di kelas,
  bukan nilai rendah.
- Jika dikonversi ke skala 0-100, nilai 20 setara dengan **100**, nilai 10 setara **50**,
  dan 0 tetap **0**.

## Dampak

Bila kolom Tugas 02 (skala 0-20) ikut dihitung sebagai komponen "Nilai Tugas" pada
skala 0-100 tanpa konversi, maka **bobot Tugas 02 akan tertekan jauh di bawah seharusnya**
dan merugikan seluruh mahasiswa yang mengerjakan Tugas 02 dengan baik — termasuk Cindy.

## Rekomendasi

1. Konfirmasi ke pengampu apakah Tugas 02 memang dinilai pada skala 0-20.
2. Jika ya, normalkan kolom Tugas 02 ke skala 0-100 (kalikan 5) sebelum digabung ke
   komponen "Nilai Tugas (10%)".
3. Perbaiki label header kolom agar konsisten dengan skala yang dipakai
   (mis. "Tugas 02 (Nilai 0-20)") untuk menghindari salah tafsir di kemudian hari.
4. Periksa apakah anomali serupa terjadi pada file/kelas OAK lain di folder `nilai-oak`.

## Catatan Metodologi

Data dibaca langsung dari sheet `Worksheet` file `.xlsx` menggunakan `openpyxl`
(mode `data_only`, membaca nilai hasil, bukan formula). Rentang baris data: baris ke-8
hingga akhir (39 mahasiswa).
