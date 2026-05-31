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
- **GEFCom2012/2014** — benchmark load forecasting yang luas dipakai.
- **ISO New England / PJM / ENTSO-E** — beban regional + cuaca publik.
- **London Smart Meter (UK Power Networks) / Pecan Street** — beban level rumah/feeder untuk multi-node.
- **PLN / utilitas Indonesia** (bila tersedia via kerja sama) — uji konteks lokal.
- **Cuaca**: NOAA / ERA5 / BMKG untuk fitur eksogen.

## 6. Risiko & Mitigasi
- *Topologi jaringan tak tersedia* → adjacency learnable / korelasi data-driven.
- *Data lokal terbatas* → mulai dari benchmark publik, transfer ke data lokal.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 data + baseline; 2–3 TFT+TGNN + probabilistik; 4 calibration + ablation; 5 uji shift/anomali + multi-node; 6 penulisan + rilis kode.
