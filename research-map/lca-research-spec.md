# Research Spec: Life Cycle Assessment (LCA)

> **Template ini memiliki bagian bertanda `[ISI]` — jika dibiarkan kosong, estimasi default akan digunakan secara otomatis.**

---

## 1. Identitas Peneliti

| Field | Value |
|-------|-------|
| Nama | `[ISI: Nama lengkap Anda]` |
| Institusi | `[ISI: Universitas / Lembaga]` |
| Bidang Spesialisasi | Ilmu Lingkungan / Environmental Science |
| Level | Profesor / Peneliti Senior |
| Email Korespondensi | `[ISI: email@institusi.ac.id]` |

---

## 2. Judul & Topik Penelitian

**Judul Sementara:**
> `[ISI: Judul spesifik Anda]`
> *(Estimasi default jika kosong: "Life Cycle Assessment of [Produk/Sistem] in Indonesian Context: Environmental Impact and Sustainability Implications")*

**Objek LCA (Functional Unit):**
> `[ISI: Produk / proses / sistem yang dikaji — contoh: 1 kg beras organik, 1 kWh listrik dari PLTSa, 1 unit kendaraan listrik]`

**Sistem Batas (System Boundary):**
- [ ] Cradle-to-Gate
- [ ] Cradle-to-Grave
- [ ] Cradle-to-Cradle
- [ ] `[ISI: custom boundary lainnya]`

---

## 3. Latar Belakang & Motivasi

**Masalah utama yang diangkat:**
> `[ISI: 2–3 kalimat deskripsi masalah lingkungan yang melatarbelakangi penelitian ini]`
> *(Estimasi default: Kebutuhan data emisi dan dampak lingkungan berbasis LCA di Indonesia masih sangat terbatas, sementara kebijakan transisi energi dan net-zero 2060 membutuhkan basis data ilmiah yang solid.)*

**Research Gap:**
> `[ISI: Apa yang belum dijawab oleh literatur sebelumnya?]`
> *(Estimasi default: Mayoritas studi LCA menggunakan database Eropa (ecoinvent) yang tidak merepresentasikan kondisi Indonesia — intensitas energi, mix bahan bakar, dan pola konsumsi sangat berbeda.)*

---

## 4. Pertanyaan Penelitian

1. `[ISI: RQ utama]`
2. `[ISI: RQ pendukung 1]`
3. `[ISI: RQ pendukung 2 — opsional]`

*(Estimasi default jika kosong:)*
1. *Berapa besar dampak lingkungan (GWP, AP, EP) dari [objek LCA] sepanjang siklus hidupnya?*
2. *Fase mana (produksi / penggunaan / akhir masa pakai) yang berkontribusi paling besar terhadap emisi karbon?*
3. *Bagaimana dampak LCA berubah jika menggunakan sumber energi terbarukan sebagai skenario alternatif?*

---

## 5. Metodologi

### 5.1 Standar & Framework
- Mengikuti **ISO 14040 / 14044**
- Software LCA: `[ISI: SimaPro / OpenLCA / GaBi / lainnya]` *(Default: OpenLCA — open source)*
- Database inventori: `[ISI: ecoinvent / ELCD / data primer / lainnya]` *(Default: ecoinvent 3.x + data primer lapangan)*

### 5.2 Kategori Dampak yang Dikaji
- [ ] Global Warming Potential (GWP) — CO₂ eq.
- [ ] Acidification Potential (AP)
- [ ] Eutrophication Potential (EP)
- [ ] Ozone Depletion (ODP)
- [ ] `[ISI: kategori dampak tambahan]`

### 5.3 Sumber Data
| Tipe Data | Sumber |
|-----------|--------|
| Data primer | `[ISI: survei lapangan / wawancara / pengukuran langsung]` |
| Data sekunder | `[ISI: publikasi / database industri / BPS]` |
| Data emisi | ecoinvent / `[ISI: database lokal]` |

### 5.4 Analisis Tambahan
- [ ] Sensitivity Analysis
- [ ] Uncertainty Analysis (Monte Carlo)
- [ ] Scenario Analysis / Comparative LCA
- [ ] `[ISI: lainnya]`

---

## 6. Target Publikasi

| Field | Value |
|-------|-------|
| Jurnal Target | `[ISI: nama jurnal]` *(Default: Journal of Cleaner Production — Q1 Scimago)* |
| Quartile Target | `[ISI: Q1 / Q2]` *(Default: Q1)* |
| Deadline Submit | `[ISI: bulan / tahun]` |
| Bahasa Manuskrip | `[ISI: Inggris / Indonesia]` *(Default: Inggris)* |

**Jurnal alternatif yang direkomendasikan (Q1/Q2, Scopus):**
- *Journal of Cleaner Production* (IF ~11, Q1)
- *Science of the Total Environment* (IF ~9, Q1)
- *Resources, Conservation & Recycling* (IF ~13, Q1)
- *International Journal of Life Cycle Assessment* (IF ~5, Q1, khusus LCA)
- *Sustainable Production and Consumption* (IF ~7, Q2)

---

## 7. Timeline

| Fase | Durasi | Keterangan |
|------|--------|-----------|
| Studi literatur & definisi scope | `[ISI]` *(Default: 3 minggu)* | Review ISO 14040, paper LCA sejenis |
| Pengumpulan data inventori (LCI) | `[ISI]` *(Default: 4–6 minggu)* | Data primer + sekunder |
| Pemodelan & kalkulasi LCA | `[ISI]` *(Default: 3 minggu)* | Menggunakan software LCA |
| Analisis & interpretasi | `[ISI]` *(Default: 2 minggu)* | Sensitivity, scenario |
| Penulisan manuskrip | `[ISI]` *(Default: 3 minggu)* | Draft → revisi → submit |

---

## 8. Tim Peneliti

| Nama | Peran | Institusi |
|------|-------|-----------|
| `[ISI]` | Principal Investigator | `[ISI]` |
| `[ISI]` | Co-Investigator / Data Collection | `[ISI]` |
| `[ISI]` | Mahasiswa S2/S3 | `[ISI]` |

---

## 9. Anggaran & Pendanaan

| Item | Estimasi Biaya |
|------|---------------|
| Lisensi software LCA | `[ISI]` *(Default: Rp 0 jika OpenLCA; ~$3.000/tahun SimaPro)* |
| Pengumpulan data lapangan | `[ISI]` |
| Akses jurnal / database | `[ISI]` |
| Sumber pendanaan | `[ISI: BRIN / Dikti / Mandiri / lainnya]` |

---

## 10. Catatan & Konteks Tambahan

> `[ISI: Informasi tambahan apa pun yang relevan — konteks kebijakan, kolaborasi industri, data yang sudah dimiliki, dll.]`

---

*Spec ini mengikuti kerangka ISO 14040/14044 dan best practice penulisan proposal LCA akademik.*
*Bagian `[ISI]` yang kosong akan diestimasi secara otomatis sesuai konteks ilmu lingkungan Indonesia.*
