# Proposal 07 — Probabilistic Solar PV Power Forecasting Berbasis Deep Learning dengan Sky-Image & Numerical Weather Fusion

**Domain:** Energy / Renewable Forecasting
**Target luaran:** Q1 journal (Applied Energy / Solar Energy / IEEE Trans. Sustainable Energy).

---

## 1. Latar Belakang
Pembangkitan PV surya sangat fluktuatif akibat awan, sehingga menyulitkan penjadwalan, manajemen ramp, dan stabilitas jaringan. Forecasting multi-horizon (intra-hour hingga day-ahead) yang **akurat dan probabilistik** penting untuk integrasi PV penetrasi tinggi. Sumber prediktor beragam: citra langit (sky camera), satelit, dan Numerical Weather Prediction (NWP), masing-masing unggul pada horizon berbeda.

## 2. Gap Penelitian
1. **Fusi multi-sumber lintas-horizon:** Sky-image baik untuk intra-hour, NWP untuk day-ahead; **fusi adaptif** yang memilih sumber sesuai horizon masih kurang matang.
2. **Ramp & event awan:** Prediksi **kejadian ramp** tajam (awan lewat) sering buruk; metrik berfokus rata-rata menyembunyikan kegagalan ini.
3. **Probabilistik terkalibrasi** untuk PV (interval andal) belum standar.
4. **Generalisasi lintas-lokasi/iklim** (mis. tropis berawan Indonesia) jarang diuji.

## 3. Novelty
- **Multi-modal fusion network**: encoder citra langit (CNN/ViT) + encoder NWP/satelit + temporal backbone, dengan **gating adaptif per-horizon** yang membobot sumber sesuai lead-time.
- **Ramp-aware training**: loss yang menekankan akurasi pada periode ramp (event-weighted) + deteksi awan eksplisit dari sky-image.
- **Distributional forecasting**: kuantil + conformal calibration untuk interval; skor CRPS sebagai target utama.
- **Cross-climate evaluation**: uji transfer ke iklim tropis (Indonesia) dengan domain adaptation.

## 4. Metodologi
**Baseline:** persistence & smart-persistence (clear-sky index), LSTM, N-BEATS, gradient boosting atas NWP, model sky-image CNN tunggal.

**Arsitektur usulan:**
1. *Sky-image branch*: CNN/ViT atas urutan citra → fitur gerak awan (opsi optical flow).
2. *NWP/satellite branch*: encoder fitur cuaca (irradiance, awan, suhu).
3. *Fusion*: gating per-horizon (attention) menggabungkan kedua branch + fitur clear-sky.
4. *Temporal head*: multi-horizon quantile output + conformal calibration.

**Pelatihan:** pinball loss + event-weighting untuk ramp; normalisasi dengan clear-sky index; rolling backtest.

**Ablation:** image-only vs NWP-only vs fusion; gating adaptif vs fixed; ramp-weighting on/off; transfer lintas-lokasi.

**Metrik:** nRMSE/nMAE per horizon, **CRPS & pinball**, PICP/PINAW, **ramp detection score** (mis. F1 ramp events), skill score vs smart-persistence.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **SKIPP'D** — SKy Images & PV Generation Dataset (Nie et al. 2023, *Solar Energy*). 3 tahun citra langit + output PV tersinkron, siap-pakai DL; terbuka via GitHub `yuhao-nie/Stanford-solar-forecasting-dataset`.
2. **NSRDB (NREL)** — National Solar Radiation Database; irradiance historis terbuka untuk clear-sky & fitur.
3. **SURFRAD / BSRN** — jaringan radiasi permukaan; irradiance berkualitas tinggi, terbuka.

> Minimal dua benchmark publik (SKIPP'D + NSRDB) memenuhi syarat; SURFRAD/BSRN sebagai sumber irradiance tambahan.

### 5.2 Data Pelengkap / Akses Terbatas
- **ERA5 / GFS NWP** — prediktor cuaca day-ahead (terbuka).
- **Data PV lokal Indonesia** (PLTS / kampus) bila tersedia — uji iklim tropis.

## 6. Risiko & Mitigasi
- *Sinkronisasi multi-sumber* → pipeline penyelarasan waktu yang ketat.
- *Data tropis terbatas* → transfer dari dataset publik + domain adaptation.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 data + baseline persistence/LSTM; 2–3 multi-modal fusion + probabilistik; 4 ramp-aware + ablation; 5 transfer lintas-iklim; 6 penulisan + rilis.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Nie, Y., et al. (2023).** SKIPP'D: a SKy Images and Photovoltaic Power Generation Dataset for short-term solar forecasting. *Solar Energy*, 255, 171–179. arXiv:2207.00913. — dataset citra langit + output PV (kode publik di GitHub `yuhao-nie/Stanford-solar-forecasting-dataset`).
- **Nie, Y., et al. (2024).** Open-source sky image datasets for solar forecasting with deep learning: a comprehensive survey. *Renewable and Sustainable Energy Reviews* `[cek vol]`. — survei dataset.
- **Nie, Y., et al. (2024).** SkyGPT: probabilistic ultra-short-term solar forecasting using synthetic sky images from a physics-constrained VideoGPT. *Advances in Applied Energy* `[cek]`. — pembangkitan citra langit + probabilistik.
- **(2024).** Sky Image-Based Solar Forecasting Using Deep Learning With Heterogeneous Multi-Location Data: Dataset Fusion versus Transfer Learning. *Applied Energy*, 369, 123467. — relevan untuk generalisasi lintas-lokasi.
- **Dataset:** SKIPP'D; NSRDB (NREL); SURFRAD/BSRN; ERA5/GFS untuk fitur NWP.

*Content was rephrased for compliance with licensing restrictions.*
