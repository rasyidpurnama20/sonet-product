# Proposal 10 — Spatio-Temporal Aftershock Forecasting: Integrasi Neural Point Process dengan ETAS

**Domain:** Seismologi / Deep Learning (Forecasting)
**Target luaran:** Q1 journal (GRL / JGR: Solid Earth / Nature Communications), evaluasi prospektif.

---

## 1. Latar Belakang
Setelah gempa utama, rentetan aftershock menimbulkan bahaya lanjutan. Model standar **ETAS (Epidemic-Type Aftershock Sequence)** menggambarkan pemicuan temporal (Omori) dan produktivitas (skala magnitudo), namun komponen spasialnya sering disederhanakan (kernel isotropik) dan tidak menangkap kontrol struktural (geometri patahan, Coulomb stress, heterogenitas). Pendekatan DL/point-process dapat memperkaya ekspresivitas spasial sambil mempertahankan interpretabilitas fisik ETAS.

## 2. Gap Penelitian
1. **Spasial kaku:** Kernel spasial ETAS klasik isotropik & stasioner; pola aftershock nyata anisotropik dan dikontrol struktur sesar.
2. **Hybrid fisika–DL belum matang:** Penggabungan **neural temporal/spatio-temporal point process** dengan prior ETAS/Coulomb yang tetap interpretable masih terbatas.
3. **Evaluasi prospektif & ketidakpastian:** Banyak studi hanya retrospektif; uji **pseudo-prospektif** dengan skor probabilistik baku (CSEP-style) jarang.
4. **Generalologi lintas-sekuens/region** kurang diuji.

## 3. Novelty
- **Neural ETAS hybrid**: spatio-temporal neural point process yang **memperluas kernel spasial** (anisotropik, data-driven) dengan **regularisasi/prior dari Coulomb stress & geometri sesar**, mempertahankan struktur Omori-produktivitas yang interpretable.
- **Fitur fisik terintegrasi**: ΔCFS (Coulomb), jarak ke bidang sesar, mainshock focal mechanism sebagai input.
- **Probabilistik & terkalibrasi**: keluaran laju kejadian λ(x,y,t) dengan ketidakpastian; dievaluasi gaya CSEP.
- **Evaluasi pseudo-prospektif** lintas sekuens besar (berbagai region/tektonik).

## 4. Metodologi
**Baseline:** ETAS klasik (MLE), ETAS spasial Gaussian, Reasenberg-Jones, model laju empiris.

**Arsitektur usulan:**
1. *Temporal core*: neural Hawkes / temporal point process meniru pemicuan ETAS.
2. *Spatial module*: kernel spasial data-driven (mixture/normalizing-flow) dikondisikan fitur fisik (ΔCFS, geometri).
3. *Conditioning*: mainshock parameters + katalog historis.
4. *Output*: intensitas λ(x,y,t,m) → forecast jumlah & distribusi spasial aftershock per jendela waktu.

**Pelatihan:** maximum likelihood point-process + regularisasi prior fisika; rolling/expanding window.

**Ablation:** ETAS vs neural-ETAS; isotropik vs anisotropik; dengan/tanpa fitur Coulomb; pengaruh panjang riwayat; transfer lintas-region.

**Metrik:** log-likelihood/information gain per gempa (CSEP), N-test/S-test/M-test, CRPS spasial, kalibrasi, skill vs ETAS baseline.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **SCEDC + ComCat (USGS)** — Southern California Earthquake Data Center & USGS Comprehensive Catalog; katalog aftershock berkualitas tinggi, terbuka (AWS Open Data / API USGS). Set pelatihan/uji utama.
2. **JMA Unified Catalog (Jepang)** — sekuens besar (mis. Tohoku 2011, Kumamoto 2016); terbuka. Uji lintas-region.
3. **INGV (Italia) / ISC-GEM (global)** — katalog sekuens tambahan; terbuka.

> Minimal dua benchmark publik (SCEDC/ComCat + JMA) memenuhi syarat; INGV/ISC-GEM untuk generalisasi lintas-tektonik.

### 5.2 Data Pelengkap & Fitur Fisik
- **Indonesia (BMKG / USGS ComCat)** — uji konteks lokal (sekuens megathrust/strike-slip).
- **Fitur fisik**: model sesar **Slab2 (USGS)** & perhitungan Coulomb (Coulomb 3.x / ΔCFS dari katalog) — terbuka.

## 6. Risiko & Mitigasi
- *Kelengkapan katalog (Mc) pasca-mainshock* → estimasi Mc adaptif + filtering.
- *Overfitting fisika tertentu* → regularisasi + evaluasi lintas-region.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 katalog + ETAS baseline; 2–3 neural-ETAS + fitur fisik; 4 ablation; 5 evaluasi pseudo-prospektif CSEP; 6 penulisan.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Ogata, Y. (1988).** Statistical models for earthquake occurrences and residual analysis for point processes. *Journal of the American Statistical Association*, 83(401), 9–27. — model ETAS klasik (baseline).
- **Dascher-Cousineau, K., Shen, O., Beroza, G.C. (2023).** Using deep learning for flexible and scalable earthquake forecasting (RECAST). *Geophysical Research Letters*, 50(17), e2023GL103909. — neural temporal point process.
- **Stockman, S., Lawson, D.J., Werner, M.J. (2023).** Forecasting the 2016–2017 Central Apennines earthquake sequence with a neural point process. arXiv:2301.09948 `[cek venue]`. — NPP unggul saat ada incompleteness.
- **(2023).** CL-ETAS: kombinasi deep learning + ETAS (ConvLSTM). arXiv:2310.02574. — hybrid fisika–DL.
- **(2024).** A Benchmark for Earthquake Forecasting with Neural Point Processes. arXiv:2410.08226. — protokol evaluasi NPP.
- **Dataset & evaluasi:** SCEDC/ComCat (USGS), JMA, INGV, BMKG; skor gaya CSEP; fitur Coulomb (Slab2/Coulomb 3.x).

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). Tautan adalah laman resmi penyedia.

- SCEDC (AWS Open Data) — https://registry.opendata.aws/southern-california-earthquake-data/
- USGS ComCat — https://earthquake.usgs.gov/data/comcat/
- JMA Unified Catalog — https://www.data.jma.go.jp/svd/eqev/data/bulletin/index_e.html
- INGV ISIDe — http://terremoti.ingv.it/ · ISC-GEM — http://www.isc.ac.uk/iscgem/ · Slab2 (USGS) — https://www.sciencebase.gov/catalog/item/5aa1b00ee4b0b1c392e86467
