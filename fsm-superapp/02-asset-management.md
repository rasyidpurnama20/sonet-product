# 📦 Modul 2: Asset Management System
## Analisis Lengkap — SWOT → RACI → Data Readiness → FMEA → RICE

> **Deskripsi Modul:** Sistem pengelolaan seluruh aset fisik FSM UNDIP secara digital — mulai dari pencatatan, QR labeling, tracking lokasi & kondisi, histori perawatan, mutasi, hingga analytics berbasis AI untuk perencanaan pengadaan dan penggantian aset.

---

## 📋 Fitur Lengkap

### 🟢 Basic
| # | Fitur | Deskripsi |
|---|---|---|
| 1 | Database aset digital | Katalog seluruh aset: nama, kode, spesifikasi, nilai, tahun pengadaan |
| 2 | QR code aset | Generate & cetak label QR per aset untuk identifikasi cepat via scan |
| 3 | Lokasi aset | Mapping aset ke ruangan/gedung spesifik |
| 4 | Status aset | Kondisi: Baik / Perlu Perawatan / Rusak / Hilang / Dihapuskan |
| 5 | Histori maintenance | Catatan lengkap setiap perawatan, perbaikan, kalibrasi per aset |
| 6 | Mutasi/peminjaman aset | Catat perpindahan aset antar ruangan, peminjaman ke pihak luar |

### 🔵 Advanced
| # | Fitur | Deskripsi |
|---|---|---|
| 7 | Audit aset via mobile scan | Tim audit scan QR via HP → update status & lokasi secara langsung |
| 8 | Reminder kalibrasi/perawatan | Alert otomatis X hari sebelum jadwal kalibrasi instrumen lab |
| 9 | Tracking umur aset | Visualisasi usia aset vs masa pakai normal → identifikasi yang perlu penggantian |
| 10 | Integrasi dengan ticketing | Aset rusak dari tiket → status aset otomatis terupdate |
| 11 | Monitoring utilisasi alat lab | Frekuensi pemakaian alat per minggu/bulan dari data booking |

### 🟣 Premium
| # | Fitur | Deskripsi |
|---|---|---|
| 12 | Indoor asset tracking realtime | BLE beacon/RFID → lokasi aset presisi per ruangan |
| 13 | AI rekomendasi penggantian aset | Model ML analisis usia + histori perbaikan + biaya → saran pengadaan |
| 14 | Prediksi depresiasi aset | Kalkulasi nilai buku aktual + proyeksi penurunan nilai |
| 15 | Smart inventory analytics | Insight: aset paling sering rusak, lab paling intensif, pola pengadaan |
| 16 | Digital twin ruangan & aset | 3D visualisasi tata letak ruangan + aset di dalamnya |

---

## 🔍 Analisis SWOT

### Strengths (Kekuatan Internal)
| # | Kekuatan | Implikasi |
|---|---|---|
| S1 | Aset FSM memiliki nilai ekonomis tinggi | Justifikasi investasi sistem sangat kuat (mencegah kehilangan aset) |
| S2 | Ada laboran & admin inventaris yang dedicated | SDM operasional sudah ada, tinggal digitalisasi proses |
| S3 | Kewajiban pelaporan BMN ke SIMAK-BMN UNDIP | Sistem ini bisa menjadi feeder data resmi yang akurat |
| S4 | Prodi Informatika/Ilmu Komputer ada di FSM | Mahasiswa TA bisa membantu pengembangan & pengujian |
| S5 | Banyak aset berharga (alat lab, komputer, instrumen) | High value assets → ROI sistem sangat jelas terukur |

### Weaknesses (Kelemahan Internal)
| # | Kelemahan | Risiko |
|---|---|---|
| W1 | Data aset saat ini sangat tidak akurat | "Garbage in, garbage out" — sistem tidak berguna jika data buruk |
| W2 | Tidak ada standar kode aset yang konsisten | Duplikasi data, aset sama beda nama di tiap unit |
| W3 | Laboran masing-masing departemen jalan sendiri | Silo data, sulit konsolidasi ke sistem terpusat |
| W4 | Banyak aset tua tidak punya dokumentasi | Retroactive entry sangat makan waktu & tenaga |
| W5 | Takut audit digital karena aset "tidak lengkap" | Resistensi input data karena khawatir ketahuan kekurangan |

### Opportunities (Peluang Eksternal)
| # | Peluang | Potensi Manfaat |
|---|---|---|
| O1 | Kewajiban pelaporan BMN ke pemerintah | Sistem ini solusi sekaligus compliance tool |
| O2 | Label QR code murah dan mudah dicetak | Implementasi fisik sangat terjangkau |
| O3 | Cloud storage murah (S3, GCS) | Foto & dokumen aset bisa disimpan tanpa batas biaya besar |
| O4 | Skema KKN-T / Magang mahasiswa | Mahasiswa bisa bantu entri data awal secara terstruktur |
| O5 | Integrasi dengan e-procurement UNDIP | Aset baru langsung masuk database tanpa entri manual |

### Threats (Ancaman Eksternal)
| # | Ancaman | Mitigasi |
|---|---|---|
| T1 | Aset hilang tapi tidak dilaporkan digital | Audit fisik rutin + konsekuensi jelas jika tidak melapor |
| T2 | Data aset disalahgunakan (marking palsu) | Audit trail lengkap + approval dua lapis untuk perubahan status |
| T3 | Integrasi SIMAK-BMN UNDIP sulit/tidak ada API | Gunakan export format kompatibel (Excel/CSV standar BMN) |
| T4 | Resistensi laboran yang "nyaman" dengan cara lama | Change management + benefit nyata (tidak dikejar audit manual) |
| T5 | Vendor IoT/RFID tidak tersedia lokal | Pilot dengan QR dulu, IoT sebagai roadmap jangka panjang |

---

## 👥 RACI Matrix

| Aktivitas | WD II | Admin Inventaris | Laboran | Teknisi | Kaprodi/Koord. | IT Dev |
|---|---|---|---|---|---|---|
| Input data aset baru | I | A | R | C | I | — |
| Generate & tempel QR code | I | A/R | R | C | I | — |
| Update lokasi aset | I | A | R | R | I | — |
| Update status kondisi aset | I | A | R | R | I | — |
| Catat histori maintenance | I | A | C | R | I | — |
| Proses mutasi/peminjaman aset | I | A | R | C | C | — |
| Audit fisik aset | C | A | R | R | C | — |
| Konfigurasi reminder kalibrasi | C | A | R | C | I | C |
| Generate laporan aset ke pimpinan | A | R | C | I | I | I |
| Validasi penggantian/penghapusan aset | A | C | C | C | R | — |
| Pengembangan & pemeliharaan sistem | C | C | I | I | I | A/R |
| Integrasi dengan SIMAK-BMN | A | R | I | I | I | C |

---

## 📦 Data Readiness Assessment

### Data yang Dibutuhkan

| Data | Sumber Saat Ini | Status | Aksi yang Diperlukan |
|---|---|---|---|
| Daftar aset lengkap FSM | SIMAK-BMN, arsip fisik per lab | 🟡 Ada, tidak akurat | Rekonsiliasi fisik + digitalisasi |
| Kode aset standar | Tidak ada standar FSM | 🔴 Belum ada | Buat standard kode aset (prefix dept) |
| Spesifikasi teknis aset | Manual barang, dokumen pengadaan | 🔴 Tersebar, tidak digital | Scan & entry data bertahap |
| Lokasi aset saat ini | Pengetahuan laboran (tacit) | 🔴 Tidak terdokumentasi | Survey fisik per ruangan |
| Histori perawatan | Tidak ada | 🔴 Tidak ada | Mulai fresh dari hari pertama |
| Nilai perolehan & tahun | Dokumen keuangan/pengadaan | 🟡 Parsial | Rekonsiliasi dengan bagian keuangan |
| Jadwal kalibrasi alat lab | Ada di beberapa lab, tidak semua | 🟡 Parsial | Standarisasi & import |
| Foto aset | Tidak ada | 🔴 Tidak ada | Foto saat digitalisasi aset |
| Data pengguna aset | Tidak ada | 🔴 Tidak ada | Assign PIC per aset saat entry |

### Data Readiness Score
| Dimensi | Score (1–5) | Keterangan |
|---|---|---|
| Ketersediaan Data | 2/5 | Data ada tapi sangat tersebar & tidak terstruktur |
| Kualitas Data | 1/5 | Banyak inkonsistensi, duplikasi, data kadaluarsa |
| Aksesibilitas Data | 2/5 | Sebagian di SIMAK-BMN pusat, akses terbatas |
| Governance Data | 1/5 | Tidak ada PIC data terpusat, tiap lab jalan sendiri |
| **Total Rata-rata** | **1.5/5** | 🔴 Butuh "Data Clean Sprint" intensif sebelum go-live |

### Strategi Data Migration (Bertahap)
```
Sprint 0 (2 minggu): Workshop standarisasi kode aset + template entri data
Sprint 1 (4 minggu): Input aset prioritas — lab aktif & alat mahal dulu
Sprint 2 (4 minggu): Input sisa aset kelas 2 (furniture, komputer, dll)
Sprint 3 (2 minggu): Rekonsiliasi data — cek fisik vs digital, resolve gap
Ongoing: Input aset baru otomatis dari proses pengadaan
```

---

## ⚠️ FMEA (Failure Mode and Effects Analysis)

| # | Failure Mode | Efek Kegagalan | S | O | D | RPN | Tindakan Pencegahan |
|---|---|---|---|---|---|---|---|
| 1 | Data aset awal tidak akurat | Sistem tidak bisa dipercaya, tidak dipakai | 10 | 8 | 3 | **240** 🔴 | Audit fisik sebelum go-live, verifikasi 2 pihak |
| 2 | Label QR rusak/hilang | Aset tidak bisa di-scan, tracking gagal | 6 | 7 | 4 | **168** 🔴 | Label tahan air, backup kode manual, re-print mudah |
| 3 | Mutasi aset tidak dicatat | Aset "hilang" padahal dipindah | 8 | 7 | 4 | **224** 🔴 | Approval workflow mutasi, notif ke admin |
| 4 | Status aset tidak diupdate setelah perbaikan | Data kondisi aset tidak akurat | 7 | 8 | 4 | **224** 🔴 | Integrasi otomatis dengan ticketing modul 1 |
| 5 | Laboran tidak mau entri data | Database kosong, investasi mubazir | 9 | 6 | 2 | **108** 🔴 | Onboarding intensif + reward compliance |
| 6 | Duplikasi aset di sistem | Laporan aset tidak valid | 7 | 5 | 3 | **105** 🔴 | Auto-detect duplicate (kode/nama/lokasi mirip) |
| 7 | Kehilangan aset tidak dilaporkan | Kerugian tidak terdeteksi | 9 | 5 | 4 | **180** 🔴 | Audit berkala + alert aset tidak aktif lama |
| 8 | Foto aset tidak diupload | Verifikasi kondisi sulit | 4 | 6 | 5 | **120** 🔴 | Foto wajib saat entri, upload dari kamera langsung |
| 9 | Sistem tidak terintegrasi dengan keuangan | Anggaran pengadaan tidak efisien | 7 | 4 | 4 | **112** 🔴 | API ke sistem keuangan atau export Excel standar |
| 10 | Resistensi audit digital | Audit tetap manual, sistem tidak dimanfaatkan | 8 | 5 | 3 | **120** 🔴 | Mandatorikan audit digital dalam SOP resmi WD II |

### Top 3 RPN — Prioritas Mitigasi Utama
1. **RPN 240** — Data awal tidak akurat → Wajibkan verifikasi fisik sebelum go-live
2. **RPN 224** — Mutasi tidak tercatat → Workflow approval wajib + notifikasi
3. **RPN 224** — Status tidak diupdate → Integrasi otomatis dengan ticketing

---

## 🍚 RICE Scoring — Prioritas Fitur

| # | Fitur | R | I | C | E | RICE Score | Prioritas |
|---|---|---|---|---|---|---|---|
| 1 | Database aset digital | 200 | 3 | 95% | 4 | **142.5** | 🥇 #1 |
| 2 | QR code aset | 200 | 3 | 90% | 2 | **270** | 🥇 #1 |
| 3 | Lokasi aset | 200 | 2 | 90% | 2 | **180** | 🥇 #2 |
| 4 | Status aset | 200 | 3 | 95% | 2 | **285** | 🥇 #1 |
| 5 | Histori maintenance | 100 | 2 | 85% | 3 | **56.7** | 🟡 #6 |
| 6 | Mutasi/peminjaman | 200 | 3 | 90% | 3 | **180** | 🥇 #2 |
| 7 | Audit via mobile scan | 50 | 3 | 85% | 5 | **25.5** | 🔵 #7 |
| 8 | Reminder kalibrasi | 50 | 3 | 85% | 3 | **42.5** | 🔵 #6 |
| 9 | Tracking umur aset | 20 | 2 | 80% | 4 | **8** | 🔵 #9 |
| 10 | Integrasi ticketing | 200 | 3 | 85% | 6 | **85** | 🔵 #5 |
| 11 | Monitoring utilisasi lab | 50 | 2 | 75% | 5 | **15** | 🔵 #8 |
| 12 | Indoor tracking realtime | 200 | 3 | 40% | 30 | **8** | 🟣 #12 |
| 13 | AI rekomendasi penggantian | 20 | 3 | 55% | 20 | **1.65** | 🟣 #14 |
| 14 | Prediksi depresiasi | 10 | 2 | 50% | 15 | **0.67** | 🟣 #15 |
| 15 | Smart inventory analytics | 20 | 2 | 60% | 10 | **2.4** | 🟣 #13 |
| 16 | Digital twin | 5 | 2 | 40% | 40 | **0.1** | 🟣 #16 |

### Kesimpulan RICE — Urutan Implementasi
```
FASE 1 (0–3 bulan):  QR code + database → status aset → lokasi → mutasi
FASE 2 (3–6 bulan):  Histori maintenance → integrasi ticketing → reminder kalibrasi
FASE 3 (6–12 bulan): Audit mobile → tracking umur → utilisasi lab → laporan analitik
FASE 4 (12+ bulan):  Indoor tracking → AI rekomendasi → prediksi depresiasi → digital twin
```

---

## 💡 Rekomendasi Strategis Khusus Modul Ini

1. **"Big Bang" entri data dengan KKN/magang:** Rekrut 10–20 mahasiswa KKN-T untuk entri data aset selama 1 bulan — efisien dan berdampak.
2. **QR label standar tahan lama:** Gunakan label vinyl waterproof + laminasi untuk aset lab — QR rusak adalah musuh utama sistem ini.
3. **Mulai dari lab aktif & aset mahal:** Prioritaskan alat senilai > Rp 5 juta dulu, baru furniture & aset kecil.
4. **Integrasi dengan SIMAK-BMN:** Jangan duplikasi sistem — jadikan super apps sebagai front-end yang feeding ke SIMAK-BMN resmi.
5. **Amnesty data awal:** Beri periode 3 bulan tanpa konsekuensi untuk laporan kondisi aset yang tidak sesuai dokumen — ini mendorong laboran jujur memasukkan data real.

---

*Dokumen ini bagian dari FSM Super Apps Analysis Suite | Lihat juga: [00-overview.md](./00-overview.md)*
