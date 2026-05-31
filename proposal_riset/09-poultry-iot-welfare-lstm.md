# Proposal 09 — Sistem IoT Multi-Sensor & Deep Learning untuk Monitoring Kesejahteraan dan Prediksi Bobot Broiler

**Domain:** Smart Poultry / IoT & Time-Series Deep Learning
**Target luaran:** Q1 journal (Computers and Electronics in Agriculture / IEEE Internet of Things Journal), prototipe sistem end-to-end.

---

## 1. Latar Belakang
Produktivitas broiler ditentukan oleh kondisi mikroklimat (suhu, kelembapan, NH3, CO2), kualitas air/pakan, dan perilaku flock. Pemantauan manual tidak kontinu dan reaktif. Sensor IoT murah memungkinkan pemantauan kontinu, namun nilai terbesar muncul bila data sensor diubah menjadi **prediksi & peringatan dini** (stres panas, kualitas udara buruk, penyimpangan pertumbuhan) yang dapat ditindaklanjuti.

## 2. Gap Penelitian
1. **Dari monitoring ke prediksi:** Banyak sistem IoT peternakan berhenti pada dashboard; **model prediktif** (forecast bobot, indeks kesejahteraan, early warning) yang tervalidasi masih terbatas.
2. **Fusi multi-sensor heterogen:** Integrasi sinyal lingkungan + perilaku + konsumsi untuk satu indikator kesehatan/produktivitas belum matang.
3. **Generalisasi antar-kandang & antar-siklus:** Model sering tidak stabil lintas batch/musim.
4. **Edge & keandalan:** Inferensi lokal saat konektivitas buruk dan penanganan data hilang/sensor rusak jarang dibahas.

## 3. Novelty
- **Multi-sensor fusion + multi-task DL**: satu model memprediksi (a) kurva bobot/FCR, (b) indeks kesejahteraan/heat-stress, (c) early-warning kualitas udara, dari fusi sensor lingkungan + perilaku (aktivitas/sebaran flock).
- **Forecast + uncertainty**: prediksi mikroklimat & bobot dengan interval untuk kontrol proaktif (ventilasi/pemanas).
- **Robust missing-data**: arsitektur toleran data hilang (masking/imputasi terintegrasi) untuk sensor tak andal.
- **Edge-cloud hybrid**: inferensi ringan di edge + sinkronisasi cloud; kontrol loop tertutup opsional.

## 4. Metodologi
**Baseline:** ambang aturan (rule-based), regresi linear/GBDT untuk bobot, LSTM univariat suhu.

**Arsitektur usulan:**
1. *Akuisisi*: node sensor (DHT/SHT suhu-kelembapan, NH3/CO2, kamera aktivitas, timbangan otomatis) → broker MQTT.
2. *Pra-pemrosesan*: sinkronisasi, imputasi, masking sensor hilang.
3. *Model*: encoder per-modalitas → fusi (attention) → backbone temporal (LSTM/Temporal Conv/Transformer) → multi-task heads (bobot, welfare index, early-warning) dengan uncertainty.
4. *Deploy*: edge (microcontroller/SBC) + dashboard; alarm berbasis ambang prediktif.

**Pelatihan:** multi-task loss berbobot; quantile untuk forecast; augmentasi dropout sensor.

**Ablation:** single- vs multi-sensor; multi-task vs single-task; robustness terhadap k sensor hilang; generalisasi lintas-kandang/siklus.

**Metrik:** MAE bobot/FCR, lead-time & F1 early-warning heat-stress/air quality, kalibrasi interval, uptime/keandalan edge, korelasi indeks welfare dengan penilaian ahli.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **USDA-ARS Broiler Farm Particulate Matter & Ammonia Time-Series** — data.gov (USDA-ARS). Time-series amonia (ppb, interval 1 menit) + konsentrasi partikel dalam/luar kandang; open data pemerintah AS. Benchmark deret-waktu lingkungan kandang.
2. **Ammonia Emissions from Twelve U.S. Broiler Chicken Houses** — USDA National Agricultural Library. Pengukuran amonia/ventilasi multi-kandang; open access. Benchmark kualitas udara/emisi.
3. **`IceKhoffi/chicken-health-behavior-multimodal` (HuggingFace)** — sinyal perilaku/aktivitas (visual+audio) untuk fusi multi-modal & indeks kesejahteraan.

> Minimal dua benchmark publik (USDA-ARS data.gov + USDA-NAL ammonia) memenuhi syarat untuk pemodelan lingkungan; HF multimodal menambah dimensi perilaku.

### 5.2 Data Pelengkap (label bobot berpasangan)
- **Akuisisi mandiri** di kandang mitra: time-series lingkungan + bobot berkala + log kejadian (kolaborasi Fakultas Peternakan) — diperlukan untuk label bobot/FCR berpasangan.
- **Data cuaca eksternal** (BMKG / ERA5) sebagai konteks ambient.

> Catatan etik: protokol kesejahteraan hewan & persetujuan mitra.

## 6. Risiko & Mitigasi
- *Sensor rusak/drift* → kalibrasi berkala + model toleran missing-data.
- *Variasi antar-siklus* → latih multi-batch + fitur kalender/musim.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 rancang & pasang node IoT; 2 koleksi data + baseline; 3–4 fusi multi-task + uncertainty; 5 uji lapangan + edge deploy; 6 penulisan + rilis.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **(2023).** Application of Machine Learning Algorithms for On-Farm Monitoring and Prediction of Broilers' Live Weight. *Agriculture*, 13(12), 2193. — prediksi bobot broiler non-invasif.
- **(2025).** Development of an Algorithm for Predicting Broiler Shipment Weight in a Smart Farm Environment. *Agriculture*, 15(5), 539. — forecast bobot panen di smart farm.
- **(2025).** An Integrated Multi-Sensor AI Platform for Enhanced Welfare and Productivity. arXiv:2510.15757. — sensing murah + edge analytics (Raspberry Pi 5) + forecasting; sangat dekat dengan usulan.
- **(2019, review).** Automated techniques for monitoring the behaviour and welfare of broilers and laying hens — towards precision livestock farming. *Animal* `[cek]`. — landasan PLF.
- **Dataset:** akuisisi mandiri time-series lingkungan + bobot; data cuaca BMKG sebagai konteks ambient.

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). data.gov/USDA adalah open data pemerintah AS; ekstraksi HTTP otomatis terbatas karena SPA, tautan adalah laman resmi.

- USDA-ARS — Broiler Farm Particulate Matter & Ammonia Time-Series (data.gov) — https://catalog.data.gov/dataset/data-from-characterization-of-particle-size-distributions-and-water-soluble-ions-in-partic
- USDA-NAL — Ammonia Emissions from Twelve U.S. Broiler Chicken Houses — https://www.nal.usda.gov/exhibits/ipd/frostonchickens/items/show/290
- HF `chicken-health-behavior-multimodal` — https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal
