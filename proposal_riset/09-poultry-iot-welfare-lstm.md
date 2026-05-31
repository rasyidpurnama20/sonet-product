# Proposal 09 — Sistem IoT Multi-Sensor & Deep Learning untuk Monitoring Kesejahteraan dan Prediksi Bobot Broiler

**Domain:** Smart Poultry / IoT & Time-Series Deep Learning
**Target luaran:** Q1 journal (Computers and Electronics in Agriculture / IEEE Internet of Things Journal), prototipe sistem end-to-end.

---

## 1. Latar Belakang
Produktivitas broiler ditentukan oleh kondisi mikroklimat (suhu, kelembapan, NH3, CO2), kualitas air/pakan, dan perilaku flock. Pemantauan manual tidak kontinu dan reaktif. Sensor IoT murah memungkinkan pemantauan kontinu, namun nilai terbesar muncul bila data sensor diubah menjadi **prediksi & peringatan dini** (stres panas, kualitas udara buruk, penyimpangan pertumbuhan) yang dapat ditindaklanjuti.

## 2. Gap Penelitian
1. **Dari monitoring ke prediksi:** Banyak sistem IoT peternakan berhenti pada dashboard; **model prediktif** (forecast bobot, indeks kesejahteraan, early warning) yang tervalidasi masih terbatas.
2. **Fusi multi-sensor heterogen:** Integrasi sinyal lingkungan + perilaku + konsumsi untuk satu indikator kesehatan/produktivitas belum matang.
3. **Generalologi antar-kandang & antar-siklus:** Model sering tidak stabil lintas batch/musim.
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
- **Akuisisi mandiri** di kandang mitra: time-series lingkungan + bobot berkala + log kejadian (kolaborasi Fakultas Peternakan).
- **Dataset broiler/lingkungan publik** (mis. dataset performa pertumbuhan & mikroklimat yang tersedia di repositori riset) untuk pretraining/benchmark.
- **Data cuaca eksternal** (BMKG) sebagai konteks ambient.

> Catatan etik: protokol kesejahteraan hewan & persetujuan mitra.

## 6. Risiko & Mitigasi
- *Sensor rusak/drift* → kalibrasi berkala + model toleran missing-data.
- *Variasi antar-siklus* → latih multi-batch + fitur kalender/musim.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 rancang & pasang node IoT; 2 koleksi data + baseline; 3–4 fusi multi-task + uncertainty; 5 uji lapangan + edge deploy; 6 penulisan + rilis.
