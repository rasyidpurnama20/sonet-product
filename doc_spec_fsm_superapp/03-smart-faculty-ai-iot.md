# 🧠 FSM Smart Faculty — Pengembangan Lanjutan AI/IoT

> **Jenis Dokumen:** Strategic Vision — Smart Faculty Roadmap
> **Posisi:** Lanjutan dari MVP (BASIC) → ADVANCED → **PREMIUM (Smart Faculty)**
> **Prinsip:** Hanya ide **berdampak tinggi + realistis di skala FSM**. AI/IoT bukan tujuan, tapi **alat menyelesaikan masalah operasional yang tidak terselesaikan oleh BASIC/ADVANCED**.
> **Versi:** 0.1 — Mei 2026

---

## 🎯 1. Filosofi & Filter Ide

### Filter Wajib (semua ide harus lulus 4 syarat)
| Filter | Pertanyaan Uji |
|---|---|
| **Impact** | Apakah menyelesaikan masalah yang dirasakan ≥3 segmen pengguna FSM? |
| **Data-Ready** | Apakah data fondasi tersedia setelah modul BASIC/ADVANCED berjalan ≥12 bulan? |
| **ROI Jelas** | Apakah penghematan biaya / peningkatan kualitas terukur dalam 12 bulan? |
| **Realistis Tim** | Apakah bisa dibangun tim FSM (mungkin dengan partner riset), bukan vendor mahal? |

### Anti-Pattern (Ditolak)
- ❌ AI generatif untuk fitur kosmetik (chatbot "Halo nama saya FSM-Bot")
- ❌ IoT untuk hal yang bisa diselesaikan dengan QR code
- ❌ Computer vision untuk masalah yang QR/RFID lebih murah
- ❌ Real-time tracking manusia (etika + tidak butuh)
- ❌ Blockchain untuk audit trail (Postgres + hash chain sudah cukup)
- ❌ "Digital twin" 3D faculty (cool, tapi tidak menyelesaikan masalah)

---

## 🗺️ 2. Peta Ide Berdampak Tinggi (Lulus Filter)

| # | Area | Ide Unggulan | Dampak Utama | Prasyarat | Horizon |
|---|---|---|---|---|---|
| 1 | Predictive Maintenance | **AC failure prediction** dari history tiket | Cegah 30–50% kerusakan AC kritis | 12 bulan data tiket | T+18 bln |
| 2 | Predictive Maintenance | **Sensor suhu/kelembaban di lab kritis** | Auto-tiket sebelum kerusakan | 5–10 sensor pilot | T+18 bln |
| 3 | Smart Asset Tracking | **BLE tag untuk aset bergerak mahal** (mikroskop, oscilloscope) | Hilangkan 90% kasus "aset tidak ditemukan" | Registry ADVANCED | T+24 bln |
| 4 | Smart Asset Tracking | **CV-based batch audit** (foto ruangan → identifikasi aset) | Audit tahunan dari 3 hari → 3 jam per lab | Foto aset terstandar | T+30 bln |
| 5 | Rekomendasi Ruang | **Smart room suggestion** (kapasitas + alat + jarak) | Kurangi 70% bolak-balik dosen cari ruang kosong | Booking ADVANCED | T+18 bln |
| 6 | Rekomendasi Ruang | **No-show prediction + auto-release** | Naikkan utilisasi lab dari ~40% → ~65% | 6 bln data booking | T+24 bln |
| 7 | Task Automation | **Auto-kategorisasi tiket** (text + foto) | Hilangkan 80% kerja dispatcher | 3.000+ tiket berlabel | T+15 bln |
| 8 | Task Automation | **Auto-routing tiket ke teknisi terbaik** | Kurangi waktu resolusi 40% | History performa teknisi | T+18 bln |
| 9 | Dashboard Pimpinan | **Anomaly detection KPI** (lonjakan tiket per gedung) | Pimpinan tahu masalah dalam <24 jam | 6 bln data ops | T+12 bln |
| 10 | Dashboard Pimpinan | **Natural language query** ("lab mana paling boros maintenance?") | Pimpinan tidak butuh data analyst | Data warehouse mini | T+24 bln |
| 11 | Riset & Publikasi | **Dataset publik anonimisasi facility ops Indonesia** | Kontribusi akademik unik + branding FSM | 18 bln data lengkap | T+24 bln |
| 12 | Riset & Publikasi | **Model predictive maintenance iklim tropis** | Paper Q1/Q2 + paten potensial | Data + sensor pilot | T+30 bln |

> Dari ~30 ide brainstorm, **12 lulus filter**. Sisanya dibuang karena gagal di salah satu syarat.

---

## 🔧 3. Predictive Maintenance

### 3.1 AC Failure Prediction *(Quick Win AI)*
**Masalah konkret FSM:** AC adalah keluhan #1 di laporan harian — basement Lab Kimia, ruang server, ruang kelas siang. Kerusakan biasanya didahului 2–4 minggu sinyal (boros listrik, suara, tetesan air).

**Solusi:**
- Klasifikasi tiket history dengan keyword "AC", "dingin", "bocor" + foto
- Hitung **rata-rata interval kerusakan per unit AC** (dari `asset_id` di tiket)
- Flag AC dengan: (a) 3+ tiket dalam 6 bulan, atau (b) interval menurun 30% dari baseline
- Trigger: **rekomendasi servis preventif** ke teknisi via dashboard

**Tipe model:** Awalnya **rule-based** (statistik sederhana), upgrade ke survival analysis (Cox PH) di tahun 2.

**ROI:** Kerusakan AC kritis di ruang server / lab → kerugian Rp 5–50 juta per insiden. Cegah 5–10 kasus/tahun = ~Rp 25–500 juta.

**Prasyarat:** ≥12 bulan data tiket + asset_id terisi rapi.

---

### 3.2 Sensor Suhu/Kelembaban di Lab Kritis *(IoT Pilot)*
**Masalah konkret:** Lab Kimia, Mikrobiologi, ruang server butuh kondisi stabil. Saat ini, kerusakan AC di malam hari atau weekend baru ketahuan Senin pagi → reagen rusak / sample mati.

**Solusi:**
- 5–10 sensor murah (ESP32 + DHT22, ~Rp 150–300rb/unit) di lab kritis
- Kirim data ke Supabase via HTTP (interval 5 menit)
- Edge Function evaluasi: jika suhu >threshold selama >15 menit → **auto-buat tiket prioritas tinggi** + notif WA dispatcher + Kepala Lab

**Total biaya pilot:** ~Rp 5–10 juta untuk 10 sensor + dev time.

**ROI:** Selamatkan 1 batch reagen / sample = ~Rp 10–100 juta. Break-even di insiden pertama yang dicegah.

**Prasyarat:** Modul Ticketing BASIC sudah jalan (sensor → trigger tiket).

> 🔬 **Bonus riset:** Publikasi *case study* "Low-cost IoT-based environmental monitoring for academic labs in tropical climate" — venue: IEEE IoT Magazine, Sensors (MDPI).

---

## 📦 4. Smart Asset Tracking

### 4.1 BLE Tag untuk Aset Bergerak Mahal
**Masalah konkret:** Mikroskop riset, oscilloscope, alat ukur dipinjam antar-lab. Saat audit, **20–30% aset "hilang sementara"** — sebenarnya ada di lab lain tapi tidak tercatat. Menghabiskan waktu laboran.

**Solusi:**
- Pasang **BLE beacon tag** (~Rp 50–100rb/tag) di ~200–500 aset >Rp 5 juta
- Setiap pintu lab punya **BLE gateway** (Raspberry Pi atau ESP32, ~Rp 500rb/unit, 40–80 unit)
- Gateway broadcast presence ke Supabase setiap 1 menit
- Dashboard menampilkan "Asset X terakhir terlihat di Lab Kimia 2 pukul 14:23"

**Total biaya:** ~Rp 30–80 juta untuk full deployment, atau pilot Rp 5–10 juta untuk 5 lab.

**ROI:** Audit tahunan dari 5 hari × 3 orang → 1 hari × 1 orang = hemat 12 hari kerja/tahun. Plus mencegah kehilangan permanen aset Rp 20–100 juta/tahun.

**Prasyarat:** Modul Asset Management ADVANCED.

---

### 4.2 Computer Vision untuk Batch Audit *(Eksperimental)*
**Masalah konkret:** Audit tahunan = laboran cek aset satu per satu × 40–80 lab × ratusan aset = **berminggu-minggu**.

**Solusi (eksperimental, butuh validasi):**
- Laboran ambil foto panorama ruangan dengan smartphone
- Model object detection (YOLOv8 fine-tuned dengan foto aset FSM) identifikasi aset di foto
- Cross-check dengan registry: yang ada vs yang seharusnya
- Output: **laporan audit otomatis dengan flag** "tidak terdeteksi" / "lokasi berbeda"

**Tipe model:** YOLOv8 fine-tuning dari ~5.000 foto aset (3–6 bulan koleksi data).

**Risiko:** Akurasi awal mungkin <80% — perlu human-in-the-loop verifikasi.

> 🔬 **Bonus riset:** Skripsi/tesis mahasiswa Teknik Informatika FSM. Paper potensial: "Vision-based asset auditing in academic facilities".

---

## 🏛️ 5. Rekomendasi Ruang/Lab

### 5.1 Smart Room Suggestion
**Masalah konkret:** Dosen ingin booking ruang untuk 30 mahasiswa dengan proyektor + AC. Saat ini scroll manual dari 15–25 gedung × ratusan ruangan. **5–10 menit per booking**.

**Solusi:**
- Form booking minta: jumlah peserta, kebutuhan alat (dropdown), preferensi gedung
- Backend rank ruang berdasarkan: (kapasitas match) + (alat tersedia) + (jarak dari gedung dosen) + (kondisi ruang dari tiket history)
- **Top 3 rekomendasi** otomatis muncul

**Tipe model:** Awalnya **scoring rule-based** (weighted sum), upgrade ke learning-to-rank di tahun 2.

**ROI:** Hemat 5 menit × 200 dosen × ~5 booking/bulan = **~80 jam/bulan** waktu dosen.

**Prasyarat:** Modul Booking BASIC + data alat per ruangan (dari Asset Management).

---

### 5.2 No-Show Prediction + Auto-Release
**Masalah konkret:** Lab di-booking tapi tidak datang → **utilisasi lab FSM diperkirakan ~40%**. Padahal ada antrean booking.

**Solusi:**
- IoT: sensor okupansi di pintu lab (PIR atau BLE detection mahasiswa) — opsional fase 2
- Tanpa IoT: **konfirmasi 1-klik wajib** 30 menit sebelum jadwal (via WA bot link)
- Tidak konfirmasi → **auto-release slot 15 menit setelah jadwal mulai** + notif user antrean berikutnya
- ML: prediksi probabilitas no-show dari history → flag booking risk tinggi untuk reminder ekstra

**Tipe model:** Logistic regression / XGBoost dari fitur (history user, hari/jam, jarak booking, durasi).

**ROI:** Naikkan utilisasi 40% → 65% = **+25% kapasitas tanpa tambah lab**. Ekuivalen ~10–20 lab "baru" tanpa biaya pembangunan.

**Prasyarat:** ≥6 bulan data booking + konfirmasi.

> 🔬 **Bonus riset:** Paper "Behavioral patterns of academic resource booking — predictors of no-show in Indonesian university". Venue: Journal of Educational Computing Research.

---

## 🤖 6. Task Automation

### 6.1 Auto-Kategorisasi Tiket *(Game Changer untuk Dispatcher)*
**Masalah konkret:** Dispatcher (1–2 tendik) baca semua tiket untuk kategorisasi: AC / listrik / air / IT / fasilitas. **200–450 tiket/bulan × 1 menit/tiket = 4–8 jam/minggu**.

**Solusi:**
- Multi-modal classifier: text (deskripsi tiket) + image (foto kerusakan) → kategori
- Approach 1 (cepat, tahun 2): API LLM (Gemini/Claude) dengan prompt few-shot
- Approach 2 (mandiri, tahun 3): fine-tuned BERT Indonesia + ResNet untuk gambar
- **Confidence threshold**: <80% → tetap dispatcher review; ≥80% → auto-kategori

**ROI:** Hilangkan ~80% beban dispatcher = ~6 jam/minggu × 12 bulan = ~280 jam/tahun. Setara 0,15 FTE.

**Prasyarat:** ≥3.000 tiket berlabel kategori (capai di bulan ke-9–12 MVP).

---

### 6.2 Auto-Routing Tiket ke Teknisi Optimal
**Masalah konkret:** Dispatcher pilih teknisi manual berdasarkan "feeling". Akibat: beban tidak merata, tiket sering di-reassign 2–3x.

**Solusi:**
- Score teknisi per tiket: (skill match dari kategori) + (lokasi dekat) + (current load) + (rating history)
- Top 1 ditawarkan, jika tolak dalam 10 menit → top 2
- ML model: collaborative filtering untuk *implicit* skill (siapa biasanya cepat menyelesaikan kategori X?)

**ROI:** Kurangi waktu resolusi rata-rata 40% (target dari 48 jam → 28 jam).

**Prasyarat:** Modul Ticketing ADVANCED + 6 bulan data assignment.

---

### 6.3 SOP Asisten untuk Laboran/Teknisi *(Bukan Chatbot Generic)*
**Masalah konkret:** Teknisi muda tidak hafal SOP. Saat tiket "kebocoran gas Lab Kimia 1", langkah pertama harus apa?

**Solusi:**
- Knowledge base SOP FSM (document semua SOP yang sudah ada) → vector DB (Supabase pgvector)
- Saat teknisi terima tiket → otomatis muncul **3 langkah pertama relevan** dari SOP
- RAG (Retrieval Augmented Generation) dengan LLM untuk Q&A spesifik

**ROI:** Kurangi error penanganan tiket 50%, terutama untuk teknisi baru.

**Prasyarat:** SOP FSM terdokumentasi (proyek paralel).

---

## 📊 7. Dashboard Pimpinan AI-Augmented

### 7.1 Anomaly Detection KPI
**Masalah konkret:** WD II / Dekan tidak punya waktu lihat dashboard tiap hari. Masalah baru ketahuan saat sudah jadi keluhan formal.

**Solusi:**
- Hitung baseline mingguan untuk: tiket per gedung, waktu resolusi, no-show rate, asset hilang
- Algoritma sederhana: **Z-score >2** atau **EWMA control chart** untuk deteksi shift
- Notif WA otomatis ke pimpinan: *"Tiket Gedung B minggu ini 3x lipat baseline (±AC). Perlu intervensi?"*

**Tipe model:** Statistik klasik (tidak butuh ML berat).

**ROI:** Pimpinan respond cepat → mencegah keluhan eskalasi ke media sosial.

**Prasyarat:** ≥6 bulan data ops untuk baseline.

---

### 7.2 Natural Language Query
**Masalah konkret:** Pimpinan bertanya "Lab mana paling boros maintenance tahun ini?" → tendik harus query manual → 1–2 hari.

**Solusi:**
- LLM (API) dengan **schema-aware SQL generation** → query Supabase
- Output: tabel + grafik + ringkasan teks
- Guardrail: hanya read-only query, whitelist tabel, audit log setiap query

**ROI:** Pimpinan mandiri akses data → keputusan lebih cepat.

**Prasyarat:** Data warehouse mini (materialized view dari modul) + budget API LLM (~Rp 1–3 juta/bulan).

---

### 7.3 Energy Analytics *(Jika Smart Meter Tersedia)*
**Masalah konkret:** Tagihan listrik FSM Rp X juta/bulan. Tidak ada visibility per gedung/lab.

**Solusi:**
- Integrasi data smart meter (jika UNDIP punya) atau partnership dengan PLN ICON+
- Korelasi konsumsi vs jadwal booking → identifikasi: AC menyala saat ruang kosong
- Rekomendasi: matikan AC otomatis 15 menit setelah booking selesai

**ROI:** 5–15% penghematan listrik = bisa **puluhan–ratusan juta/tahun** untuk skala FSM.

**Prasyarat:** Akses data smart meter (urusan eksternal — PLN/PT UNDIP).

> 🔬 **Bonus riset:** Paper sustainability + Indonesian SDG goals. Funding potensial dari Kemendikbudristek.

---

## 📚 8. Peluang Publikasi & Riset

> Karena FSM **adalah fakultas riset**, setiap modul Smart Faculty bisa jadi *kontribusi akademik*. Ini **keunggulan kompetitif vs vendor komersial** — produk vendor tidak menghasilkan paper.

| # | Topik Paper | Venue Target | Angle Unik | Lead |
|---|---|---|---|---|
| P1 | **RAD methodology in Indonesian academic context** | Information & Management, IJIM | Studi kasus 12 bulan FSM, kuantitatif adopsi | Dosen Sistem Informasi |
| P2 | **Real-world dataset of facility operations (anonimisasi)** | Scientific Data (Nature) | Dataset publik pertama dari kampus Indonesia | Dosen + IT FSM |
| P3 | **Predictive maintenance in tropical climate** | IEEE Trans. Industrial Informatics | Pola kerusakan AC khas Indonesia (humidity tinggi) | Teknik Mesin / Elektro |
| P4 | **PWA adoption in Indonesian higher education** | Computers in Human Behavior | Studi UX + adoption rate, n=4.500 | Dosen Psikologi/HCI |
| P5 | **Low-cost IoT for academic lab monitoring** | Sensors (MDPI) | ESP32 + DHT22, replicable di kampus lain | Teknik Elektro |
| P6 | **No-show prediction in academic resource booking** | J. Educational Data Mining | Behavioral analytics, ML komparasi | Statistika / SI |
| P7 | **Vision-based asset auditing** | IEEE Access | YOLOv8 fine-tuning, dataset academic asset | Informatika |
| P8 | **RLS-based security architecture for student systems** | Computers & Security | Studi kasus + threat model | IT FSM |

### Strategi Publikasi
- **3 paper pertama** dari data tahun 1 (Q4 2027)
- **Mahasiswa S1/S2** sebagai first author (skripsi/tesis terkait)
- **Open dataset** dirilis bersamaan untuk maksimalkan sitasi
- Kolaborasi dengan **fakultas lain UNDIP** (Psikologi, SI) untuk paper multi-disiplin

---

## 🛣️ 9. Roadmap 3 Tahun Smart Faculty

```
Tahun 0–1: FOUNDATION (data collection)
─────────────────────────────────────────
MVP BASIC → ADVANCED untuk 4 modul
Output: 12 bulan data bersih, registry stabil

Tahun 1–2: AI RINGAN (rule + classical ML)
─────────────────────────────────────────
✅ Anomaly detection KPI (Q1 thn 2)
✅ Auto-kategorisasi tiket (Q2)
✅ Smart room suggestion (Q2)
✅ AC failure prediction rule-based (Q3)
✅ Auto-routing tiket (Q4)
🔬 Paper P1, P4 disubmit

Tahun 2–3: IoT PILOT + ADVANCED ML
─────────────────────────────────────────
✅ Sensor lab kritis 5–10 unit (Q1 thn 3)
✅ BLE tracking aset pilot 5 lab (Q2)
✅ NL query dashboard (Q2)
✅ No-show prediction model (Q3)
✅ Energy analytics (jika smart meter siap)
🔬 Paper P2, P3, P5, P6 disubmit

Tahun 3+: SCALE & PUBLISH
─────────────────────────────────────────
✅ Roll out IoT ke seluruh lab kritis
✅ Replicate ke fakultas lain UNDIP
🔬 Paper P7, P8
🏆 Branding "FSM Smart Faculty UNDIP" — pilot nasional
```

---

## 💰 10. Anggaran Indikatif Smart Faculty (3 Tahun)

| Kategori | Tahun 2 | Tahun 3 | Tahun 4 |
|---|---|---|---|
| **Cloud upgrade** (Supabase Pro+, vector DB) | Rp 6 juta | Rp 12 juta | Rp 18 juta |
| **API LLM** (Gemini/Claude untuk kategorisasi + NL query) | Rp 12 juta | Rp 24 juta | Rp 36 juta |
| **IoT hardware** (sensor + gateway) | — | Rp 30 juta | Rp 50 juta |
| **BLE tags & gateway** | — | Rp 10 juta (pilot) | Rp 50 juta (full) |
| **Compute training ML** (GCP/AWS credit) | — | Rp 15 juta | Rp 20 juta |
| **Mahasiswa riset stipend** | Rp 10 juta | Rp 20 juta | Rp 30 juta |
| **Paper APC (open access)** | — | Rp 30 juta (3 paper) | Rp 50 juta |
| **Total/tahun** | **~Rp 28 juta** | **~Rp 141 juta** | **~Rp 254 juta** |

> Sumber pendanaan potensial: Hibah Kemendikbudristek (Penelitian Terapan), CSR mitra industri, internal UNDIP, monetisasi dataset/SaaS ke kampus lain.

---

## ⚠️ 11. Risiko & Etika AI/IoT

| Risiko | Mitigasi |
|---|---|
| **Bias data** — model belajar dari pola lama yang mungkin diskriminatif (misal: tiket prodi tertentu di-prioritaskan) | Audit fairness mingguan; metrik per prodi/gedung dipantau |
| **AI menggantikan manusia** — kekhawatiran tendik/dispatcher | Framing: AI = asisten, bukan pengganti. Tetap human-in-the-loop |
| **Privasi IoT tracking** — sensor PIR di lab terkesan "memata-matai" | Sosialisasi transparan; data agregat saja, tidak per-individu |
| **Ketergantungan API LLM** — jika harga naik / API down | Fallback rule-based; rencana fine-tune model lokal di tahun 4 |
| **Akurasi model rendah → kepercayaan hilang** | Confidence threshold + human review wajib di awal |
| **Data leak via prompt LLM** — PII terkirim ke vendor | PII scrubbing sebelum prompt; pakai LLM dengan kontrak data privacy |
| **Lock-in vendor IoT** | Pilih hardware open standard (BLE, ESP32), hindari proprietary stack |

---

## ✅ 12. Kriteria Go/No-Go untuk Smart Faculty

### Go (Hijau) — Lanjutkan ke Smart Faculty Tier
- ✅ Data BASIC/ADVANCED **stabil ≥12 bulan** (registry aset >80% lengkap, tiket berlabel >90%)
- ✅ Adopsi modul utama ≥70% target user
- ✅ Anggaran riset ≥Rp 100 juta/tahun disetujui
- ✅ Minimal **2 dosen** terlibat sebagai principal investigator paper
- ✅ Tim dev punya 1 orang yang paham ML basics (atau hire fresh grad Informatika)

### No-Go (Merah) — Tunda Smart Faculty
- 🛑 Data masih kotor / banyak missing field
- 🛑 Adopsi modul BASIC <50%
- 🛑 Tidak ada budget khusus AI/IoT
- 🛑 Tidak ada akademisi yang berkomitmen untuk publikasi

---

## 🏛️ 13. Putusan Strategis (Top 5 Prioritas)

> Dari 12 ide lulus filter, **5 ide paling tinggi dampak/biaya** untuk dieksekusi pertama:

| Rank | Ide | Alasan Prioritas | Mulai |
|---|---|---|---|
| 1 | **Anomaly detection KPI** | Statistik sederhana, dampak pimpinan langsung, biaya near-zero | Q1 Tahun 2 |
| 2 | **Auto-kategorisasi tiket** | Hilangkan beban dispatcher, ROI cepat | Q2 Tahun 2 |
| 3 | **Smart room suggestion** | Hemat waktu 200+ dosen, scoring sederhana | Q2 Tahun 2 |
| 4 | **Sensor IoT lab kritis (pilot)** | Biaya rendah Rp 5–10 juta, dampak besar (selamatkan reagen/sample) | Q3 Tahun 2 |
| 5 | **AC failure prediction** | Cegah kerugian terbesar (server, lab) | Q3 Tahun 2 |

5 ide sisanya → Tahun 3.

---

## 🧾 Catatan Versi
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1 | Mei 2026 | Versi awal — 12 ide lulus filter, top 5 prioritas, roadmap 3 tahun |

---

> 🌱 **Smart Faculty bukan tentang teknologi mewah, tapi tentang menyelesaikan masalah nyata FSM dengan biaya proporsional.** AI/IoT yang tidak menghasilkan baik (a) penghematan operasional, (b) peningkatan kualitas, atau (c) publikasi akademik — **harus ditolak**.
