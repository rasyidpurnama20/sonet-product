# Proposal Riset — Kumpulan 10 Proposal

> **Tujuan:** Sepuluh proposal riset siap-kembang (PhD/Q1-target) di tiga domain: **Seismologi & Deep Learning**, **Smart Poultry**, dan **Energy Forecasting**.
> **Format setiap proposal:** Gap Penelitian → Novelty → Metodologi → Dataset (plus judul, latar, target luaran).
> **Disusun:** Mei 2026

---

## Daftar Proposal

| # | Judul Singkat | Domain | File |
|---|---------------|--------|------|
| 01 | Real-time EEW: prediksi magnitudo & ground-motion multi-stasiun (CNN–Transformer) untuk jaringan jarang Indonesia | Seismologi/DL | [01-eew-deep-learning.md](01-eew-deep-learning.md) |
| 02 | Spatio-temporal GNN untuk Earthquake Early Warning dengan dynamic station graph | Seismologi/GNN | [02-eew-gnn-spatiotemporal.md](02-eew-gnn-spatiotemporal.md) |
| 03 | Focal mechanism determination via station-network GAT + uncertainty quantification | Seismologi/GNN | [03-focal-mechanism-gnn.md](03-focal-mechanism-gnn.md) |
| 04 | Deteksi ayam mati di kandang via Edge-AI computer vision (YOLO) | Poultry/CV | [04-poultry-deteksi-ayam-mati-cv.md](04-poultry-deteksi-ayam-mati-cv.md) |
| 05 | Deteksi dini penyakit unggas via analisis suara (acoustic deep learning) | Poultry/Audio DL | [05-poultry-akustik-deteksi-penyakit.md](05-poultry-akustik-deteksi-penyakit.md) |
| 06 | Short-term load forecasting dengan Temporal Fusion Transformer / Temporal GNN | Energy | [06-load-forecasting-tft.md](06-load-forecasting-tft.md) |
| 07 | Forecasting pembangkitan PV surya berbasis deep learning + data cuaca | Energy | [07-solar-pv-forecasting.md](07-solar-pv-forecasting.md) |
| 08 | Transfer learning seismic phase picking untuk wilayah under-instrumented (Indonesia) | Seismologi/DL | [08-seismic-phase-picking-transfer-learning.md](08-seismic-phase-picking-transfer-learning.md) |
| 09 | IoT multi-sensor + LSTM untuk monitoring kesejahteraan & prediksi bobot broiler | Poultry/IoT | [09-poultry-iot-welfare-lstm.md](09-poultry-iot-welfare-lstm.md) |
| 10 | Aftershock forecasting spatio-temporal (ETAS + deep learning) | Seismologi/DL | [10-aftershock-forecasting-st-dl.md](10-aftershock-forecasting-st-dl.md) |

---

---

## Dataset Benchmark Publik per Proposal (≥2 wajib)

> Setiap proposal **wajib** memakai minimal **2 dataset benchmark publik** yang sudah terverifikasi terbuka (lihat §5.1 di tiap file). Data restricted/akuisisi-mandiri hanya sebagai pelengkap (§5.2).

| # | Dataset Publik Utama (≥2) | Akses |
|---|----------------------------|-------|
| 01 | STEAD, INSTANCE (+ K-NET/KiK-net) | GitHub / INGV / NIED |
| 02 | INSTANCE, STEAD (+ SCEDC) | INGV / GitHub / AWS Open Data |
| 03 | SCEDC focal-mechanism catalog, Global CMT (+ STEAD) | SCEDC/SCEC / globalcmt.org |
| 04 | PIO broiler dataset, Roboflow "Chicken Detection & Tracking" (+ carcass-seg, HF multimodal) | Nature Sci. Data / Roboflow / HF |
| 05 | Mendeley Poultry Vocalization (zp4nf2dxbh), SmartEars (dy6gtvt4mk) (+ Zenodo 10433023) | Mendeley / Zenodo |
| 06 | GEFCom2012/2014, ISO-NE/PJM/ENTSO-E (+ London Smart Meter, Pecan Street) | open data |
| 07 | SKIPP'D, NSRDB (+ SURFRAD/BSRN) | GitHub / NREL / NOAA |
| 08 | STEAD, INSTANCE (+ NCEDC/SCEDC) | GitHub / INGV / AWS Open Data |
| 09 | USDA-ARS broiler PM/ammonia (data.gov), USDA-NAL ammonia (+ HF multimodal) | data.gov / USDA NAL |
| 10 | SCEDC/ComCat (USGS), JMA catalog (+ INGV, ISC-GEM) | USGS / JMA / INGV |

---

## Ringkasan Klaster Domain

- **Seismologi & Deep Learning (01, 02, 03, 08, 10):** memanfaatkan keahlian phase picking berbasis CNN serta tren GNN multi-stasiun, uncertainty-aware modeling, dan transfer learning lintas-jaringan. Target venue: GRL, JGR-SE, SRL, BSSA, GJI.
- **Smart Poultry (04, 05, 09):** hilirisasi AI/IoT untuk peternakan unggas — visi komputer edge, bioakustik, dan sensor lingkungan. Target venue: Computers and Electronics in Agriculture, Biosystems Engineering, IEEE IoT Journal.
- **Energy Forecasting (06, 07):** peramalan beban listrik dan pembangkitan PV untuk integrasi energi terbarukan. Target venue: Applied Energy, IEEE Trans. Smart Grid, Energy.

## Catatan Penggunaan

- Setiap proposal dirancang sebagai **dokumen mandiri** sehingga dapat dipecah menjadi pengajuan terpisah.
- Item dataset diberi tautan/identitas sumber konkret agar mudah diverifikasi.
- **Kebijakan dataset:** setiap proposal menjamin **minimal 2 dataset benchmark publik** (§5.1) yang terverifikasi terbuka; data akses-terbatas/akuisisi-mandiri hanya pelengkap (§5.2). Lihat tabel ringkasan di atas.
- Bagian metodologi memuat baseline, arsitektur usulan, ablation, dan metrik evaluasi agar langsung dapat dieksekusi.
- Setiap proposal memuat bagian **"Referensi Kunci / Related Work"** berisi sitasi yang sudah diverifikasi via pencarian web (Mei 2026). Entri dengan tanda `[cek]` masih perlu konfirmasi venue/tahun sebelum dikutip formal di manuskrip.
