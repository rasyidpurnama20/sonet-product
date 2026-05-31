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
- **Southern California (SCEDC) / ComCat (USGS)** — katalog aftershock berkualitas tinggi.
- **Japan JMA catalog** — sekuens besar (mis. Tohoku) untuk uji lintas-region.
- **Italia (INGV) / ISC-GEM global** — sekuens tambahan.
- **Indonesia (BMKG/USGS)** — uji konteks lokal (mis. sekuens megathrust/strike-slip).
- **Fitur fisik**: model sesar (USGS/Slab2) & perhitungan Coulomb (Coulomb 3.x / Coulomb stress dari katalog).

## 6. Risiko & Mitigasi
- *Kelengkapan katalog (Mc) pasca-mainshock* → estimasi Mc adaptif + filtering.
- *Overfitting fisika tertentu* → regularisasi + evaluasi lintas-region.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 katalog + ETAS baseline; 2–3 neural-ETAS + fitur fisik; 4 ablation; 5 evaluasi pseudo-prospektif CSEP; 6 penulisan.
