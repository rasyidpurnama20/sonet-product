# Proposal 06 — Short-Term Load Forecasting Probabilistik dengan Temporal Fusion Transformer & Temporal Graph Neural Network

**Domain:** Energy / Time-Series Deep Learning
**Target luaran:** Q1 journal (Applied Energy / IEEE Transactions on Smart Grid), benchmark + kode reprodusibel.

---

## 1. Latar Belakang
Short-Term Load Forecasting (STLF, horizon menit–hari) menopang unit commitment, demand response, dan integrasi energi terbarukan. Beban listrik dipengaruhi cuaca, kalender, dan perilaku konsumen yang heterogen antar-feeder/gardu. Munculnya PV atap, EV, dan beban fleksibel meningkatkan volatilitas, sehingga ramalan **probabilistik** (bukan titik) dan **spasial antar-node** makin penting.

## 2. Gap Penelitian
1. **Point vs probabilistik:** Banyak model fokus akurasi titik (MAPE); **kuantifikasi ketidakpastian** (interval/kuantil) yang terkalibrasi untuk pengambilan keputusan jaringan masih kurang dieksploitasi.
2. **Ketergantungan spasial diabaikan:** Beban antar gardu/feeder berkorelasi (topologi jaringan, geografi, cuaca bersama), namun banyak model memperlakukan tiap node independen.
3. **Distribution shift:** Perubahan perilaku (pasca-pandemi, adopsi EV/PV) membuat model usang; **adaptasi/online learning** jarang dibahas.
4. **Interpretabilitas** fitur (cuaca vs kalender vs lag) untuk operator masih terbatas.

## 3. Novelty
- **Hybrid TFT + Temporal GNN**: Temporal Fusion Transformer untuk dependensi temporal & variable selection yang interpretable, digabung **graph layer** yang memodelkan korelasi antar-node (feeder/gardu) → ramalan multi-node serempak.
- **Probabilistik terkalibrasi**: quantile/distributional forecasting + post-hoc calibration (conformal prediction) untuk interval andal.
- **Graph adaptif**: struktur graf antar-node dipelajari (adjacency learnable) bila topologi fisik tidak diketahui.
- **Robust terhadap shift**: skema fine-tuning/online update + evaluasi pada periode anomali (mis. hari libur, cuaca ekstrem).

## 4. Metodologi
**Baseline:** SARIMA/Prophet, LightGBM, LSTM/Seq2Seq, N-BEATS, TFT vanilla, DeepAR.

**Arsitektur usulan:**
1. *Input*: lag beban, fitur kalender (jam/hari/libur), cuaca (suhu, kelembapan, irradiance), encoder per-node.
2. *Spatial module*: Temporal GNN (adjacency dari topologi atau learnable) untuk pertukaran informasi antar-node.
3. *Temporal module*: TFT (LSTM encoder + interpretable multi-head attention + variable selection networks).
4. *Output*: quantile forecasts multi-horizon per node + conformal calibration.

**Pelatihan:** pinball/quantile loss; multi-horizon; early stopping; rolling-origin backtesting.

**Ablation:** TFT-only vs +GNN; graf fisik vs learnable; conformal vs raw quantiles; horizon pendek vs panjang; ketahanan pada periode anomali.

**Metrik:** MAPE/RMSE (titik), **pinball loss & CRPS** (probabilistik), PICP/PINAW (kalibrasi interval), per-node & agregat, biaya komputasi.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **GEFCom2012 & GEFCom2014** — Global Energy Forecasting Competition (Hong et al.). Benchmark load forecasting (titik & probabilistik) yang paling luas dipakai; terbuka.
2. **ISO New England / PJM / ENTSO-E** — beban regional + cuaca; open data operator jaringan.
3. **London Smart Meter (UK Power Networks)** & **Pecan Street (Dataport)** — beban level rumah/feeder untuk pemodelan multi-node/graf.

> Minimal dua benchmark publik (GEFCom2014 + ISO-NE/PJM) memenuhi syarat; smart-meter datasets untuk dimensi spasial multi-node.

### 5.2 Data Pelengkap / Akses Terbatas
- **PLN / utilitas Indonesia** (bila tersedia via kerja sama) — uji konteks lokal.
- **Cuaca**: NOAA / ERA5 / BMKG sebagai fitur eksogen.

## 6. Risiko & Mitigasi
- *Topologi jaringan tak tersedia* → adjacency learnable / korelasi data-driven.
- *Data lokal terbatas* → mulai dari benchmark publik, transfer ke data lokal.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 data + baseline; 2–3 TFT+TGNN + probabilistik; 4 calibration + ablation; 5 uji shift/anomali + multi-node; 6 penulisan + rilis kode.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Lim, B., Arık, S.Ö., Loeff, N., Pfister, T. (2021).** Temporal Fusion Transformers for interpretable multi-horizon time series forecasting. *International Journal of Forecasting*, 37(4), 1748–1764. — backbone temporal + variable selection interpretable.
- **Salinas, D., Flunkert, V., Gasthaus, J., Januschowski, T. (2020).** DeepAR: probabilistic forecasting with autoregressive recurrent networks. *International Journal of Forecasting*, 36(3), 1181–1191. — baseline probabilistik.
- **Oreshkin, B.N., et al. (2020).** N-BEATS: neural basis expansion analysis for interpretable time series forecasting. *ICLR*.
- **(2024/2025).** Graph Neural Networks for Electricity Load Forecasting. arXiv:2507.03690. — dependensi spasial antar-node beban.
- **Hong, T., et al. (2016).** Probabilistic energy forecasting: GEFCom2014 and beyond. *International Journal of Forecasting*, 32(3), 896–913. — benchmark + framing probabilistik.
- **Dataset:** GEFCom2012/2014; ISO-NE/PJM/ENTSO-E; London Smart Meter (UKPN); Pecan Street.

*Content was rephrased for compliance with licensing restrictions.*
