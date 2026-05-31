# Proposal 01 — Real-time Earthquake Early Warning: Prediksi Magnitudo & Ground-Motion Multi-Stasiun dengan CNN–Transformer untuk Jaringan Jarang Indonesia

**Domain:** Seismologi / Deep Learning
**Target luaran:** Q1 journal (Geophysical Research Letters / Seismological Research Letters), demonstrasi sistem real-time.

---

## 1. Latar Belakang
Earthquake Early Warning (EEW) memberikan jeda detik hingga puluhan detik sebelum guncangan kuat tiba. Sistem klasik (mis. ElarmS, PLUM, FinDer) bergantung pada parameter empiris (tau-c, Pd) yang sensitif terhadap saturasi magnitudo dan konfigurasi jaringan. Indonesia memiliki seismisitas sangat tinggi namun kerapatan stasiun rendah dan tidak merata — kondisi yang menantang bagi metode klasik maupun model DL yang dilatih pada jaringan padat (Jepang/California).

## 2. Gap Penelitian
1. **Saturasi & latensi magnitudo:** Pendekatan single-station berbasis fitur P-wave awal cenderung saturasi pada M>7 dan butuh akumulasi data sehingga menambah latensi.
2. **Generalisasi ke jaringan jarang:** Model EEW DL state-of-the-art (mis. TEAM) diuji pada jaringan padat; performa pada jaringan jarang & tidak merata (Indonesia) belum tervalidasi.
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

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **STEAD** — STanford EArthquake Dataset (Mousavi et al. 2019, *IEEE Access*). ~1,2 juta waveform 3-komponen berlabel; terbuka via GitHub `smousavi05/STEAD`. Untuk pra-pelatihan/benchmark encoder.
2. **INSTANCE** — Italian seismic dataset for ML (Michelini et al. 2021, *ESSD*). ~1,2 juta trace + metadata ground-motion lengkap; terbuka via INGV (pi.ingv.it/instance). Benchmark multi-stasiun + label PGA/PGV/SA.
3. **Japan K-NET/KiK-net (NIED)** — jaringan strong-motion padat; terbuka via registrasi gratis NIED. Pretraining EEW + label ground-motion.

> Minimal dua benchmark publik (STEAD + INSTANCE) sudah memenuhi syarat; K-NET/KiK-net sebagai benchmark ketiga.

### 5.2 Data Pelengkap / Akses Terbatas (evaluasi lokal)
- **Indonesia BMKG / GEOFON / IRIS-FDSN** — waveform regional untuk evaluasi jaringan jarang (event M≥5; BMKG via permohonan resmi, GEOFON/IRIS via FDSN web services terbuka).
- **Label ground-motion** dihitung dari rekaman (PGA/PGV/SA) di stasiun target.

## 6. Risiko & Mitigasi
- *Label M besar langka di Indonesia* → transfer learning + augmentasi dari Jepang/Italia.
- *Kualitas metadata heterogen* → kurasi otomatis + filter SNR.
- *Latensi real-time* → model ringan (<10 ms inferensi/GPU), uji pada replay stream.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1–2 kurasi data + baseline; 3–4 arsitektur & pelatihan; 5 ablation + evaluasi jaringan jarang; 6 penulisan + demo replay real-time.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Münchmeyer, J., Bindi, D., Leser, U., Tilmann, F. (2021).** The transformer earthquake alerting model (TEAM): a new versatile approach to earthquake early warning. *Geophysical Journal International*, 225(1), 646–656. arXiv:2009.06316. — baseline EEW DL utama.
- **Münchmeyer, J., et al. (2021).** Earthquake magnitude and location estimation from real-time seismic waveforms with a transformer network. *Geophysical Journal International*, 226(2), 1086–1100. arXiv:2101.02010. — set stasiun dinamis, permutation-invariant.
- **Jozinović, D., et al. (2022).** Transfer learning: improving neural network based prediction of earthquake ground shaking for an area with insufficient training data. *Geophysical Journal International*, 229(1), 704–718. — dasar strategi transfer untuk jaringan jarang.
- **Zhu, W. & Beroza, G.C. (2019).** PhaseNet: a deep-neural-network-based seismic arrival-time picking method. *Geophysical Journal International*, 216(1), 261–273.
- **Mousavi, S.M., et al. (2020).** Earthquake transformer (EQTransformer). *Nature Communications*, 11, 3952.
- **Dataset:** STEAD — Mousavi et al. (2019), *IEEE Access*, 7, 179464–179476; INSTANCE — Michelini et al. (2021), *Earth System Science Data*, 13, 5509–5544.

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). Ekstraksi HTTP otomatis untuk beberapa portal SPA tidak selalu berhasil; tautan di bawah adalah laman resmi.

- STEAD — https://github.com/smousavi05/STEAD
- INSTANCE — https://instance.ingv.it/
- K-NET/KiK-net (NIED) — https://www.kyoshin.bosai.go.jp/
- GEOFON (FDSN) — https://geofon.gfz-potsdam.de/ · IRIS FDSN — https://service.iris.edu/
