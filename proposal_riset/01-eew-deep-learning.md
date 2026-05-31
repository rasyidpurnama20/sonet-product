# Proposal 01 — Real-time Earthquake Early Warning: Prediksi Magnitudo & Ground-Motion Multi-Stasiun dengan CNN–Transformer untuk Jaringan Jarang Indonesia

**Domain:** Seismologi / Deep Learning
**Target luaran:** Q1 journal (Geophysical Research Letters / Seismological Research Letters), demonstrasi sistem real-time.

---

## 1. Latar Belakang
Earthquake Early Warning (EEW) memberikan jeda detik hingga puluhan detik sebelum guncangan kuat tiba. Sistem klasik (mis. ElarmS, PLUM, FinDer) bergantung pada parameter empiris (tau-c, Pd) yang sensitif terhadap saturasi magnitudo dan konfigurasi jaringan. Indonesia memiliki seismisitas sangat tinggi namun kerapatan stasiun rendah dan tidak merata — kondisi yang menantang bagi metode klasik maupun model DL yang dilatih pada jaringan padat (Jepang/California).

## 2. Gap Penelitian
1. **Saturasi & latensi magnitudo:** Pendekatan single-station berbasis fitur P-wave awal cenderung saturasi pada M>7 dan butuh akumulasi data sehingga menambah latensi.
2. **Generalologi jaringan jarang:** Model EEW DL state-of-the-art (mis. TEAM) diuji pada jaringan padat; performa pada jaringan jarang & tidak merata (Indonesia) belum tervalidasi.
3. **Prediksi ground-motion langsung:** Sebagian besar sistem memprediksi magnitudo lalu memetakan ke intensitas via GMPE; prediksi **peak ground motion langsung di lokasi target** dengan ketidakpastian masih jarang dalam kerangka real-time end-to-end.
4. **Robust terhadap stasiun hilang:** Ketahanan terhadap dropout stasiun / data gap belum menjadi metrik evaluasi standar.

## 3. Novelty
- **Arsitektur CNN–Transformer multi-stasiun** yang memproses jendela waktu yang tumbuh (expanding window) sejak deteksi P pertama, dengan **set-transformer** yang permutation-invariant terhadap jumlah & urutan stasiun sehingga adaptif pada jaringan jarang/variabel.
- **Dual-head prediksi**: (a) magnitudo, (b) peak ground motion (PGA/PGV/SA) langsung di lokasi target arbitrer, dengan **uncertainty** (Gaussian/quantile) untuk pengambilan keputusan ambang.
- **Curriculum jaringan-jarang**: pelatihan dengan augmentasi station-dropout untuk meniru kondisi Indonesia, ditambah fine-tuning lintas-region (transfer dari jaringan padat).
- **Evaluasi berbasis lead-time vs akurasi** sebagai kurva trade-off, bukan akurasi statis.

## 4. Metodologi
**Baseline pembanding:** tau-c/Pd regresi, ElarmS-style, TEAM (reimplementasi), single-station CNN.

**Arsitektur usulan:**
1. *Per-station encoder*: CNN 1D (waveform 3-komponen) → embedding per stasiun + positional encoding metadata (jarak episentral estimasi, koordinat, SNR).
2. *Network aggregator*: Transformer/Set-Transformer dengan attention antar-stasiun (permutation-invariant, mendukung jumlah stasiun variabel).
3. *Temporal head*: expanding-window inference (0.5s, 1s, 2s, 4s, ... setelah P) untuk menghasilkan estimasi yang diperbarui kontinu.
4. *Output heads*: magnitudo (regresi + uncertainty), ground-motion target-site (quantile regression).

**Pelatihan:** loss = NLL Gaussian (magnitudo) + pinball loss (quantile GM); augmentasi: station dropout, noise injection, time-shift; optimizer AdamW + cosine schedule.

**Ablation:** (a) jumlah stasiun (1→N), (b) pengaruh station-dropout curriculum, (c) transfer learning vs from-scratch, (d) attention interpretability.

**Metrik:** MAE/bias magnitudo vs lead-time, ground-motion residual (ln-units), warning time gained, false/missed alert rate pada ambang MMI, robustness terhadap k stasiun hilang.

## 5. Dataset
- **STEAD** (STanford EArthquake Dataset) — pra-pelatihan encoder waveform.
- **INSTANCE** (Italia) — benchmark multi-stasiun bermetadata lengkap.
- **Japan K-NET/KiK-net (NIED)** — jaringan padat untuk pretraining EEW & label ground-motion.
- **Indonesia BMKG / GEOFON / IRIS-FDSN** — waveform regional untuk fine-tuning & evaluasi jaringan jarang (event M≥5 katalog BMKG/USGS).
- **Label ground-motion**: dihitung dari rekaman (PGA/PGV/SA) pada stasiun target.

> Catatan akses: data BMKG via permohonan resmi / FDSN web services; K-NET/KiK-net via registrasi NIED.

## 6. Risiko & Mitigasi
- *Label M besar langka di Indonesia* → transfer learning + augmentasi dari Jepang/Italia.
- *Kualitas metadata heterogen* → kurasi otomatis + filter SNR.
- *Latensi real-time* → model ringan (<10 ms inferensi/GPU), uji pada replay stream.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1–2 kurasi data + baseline; 3–4 arsitektur & pelatihan; 5 ablation + evaluasi jaringan jarang; 6 penulisan + demo replay real-time.
