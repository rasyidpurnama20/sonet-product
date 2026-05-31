# Proposal 02 — Spatio-Temporal Graph Neural Network untuk Earthquake Early Warning dengan Dynamic Station Graph

**Domain:** Seismologi / Graph Neural Networks
**Target luaran:** Q1 journal (GRL / JGR: Solid Earth), kontribusi metodologis GNN.

---

## 1. Latar Belakang
Jaringan seismik secara alami adalah **graf**: stasiun sebagai node, relasi spasial (jarak, azimut, koherensi gelombang) sebagai edge. EEW membutuhkan integrasi informasi multi-stasiun yang terus berubah saat front gelombang menyebar. Model berbasis grid/sekuens mengabaikan struktur geometris jaringan, sementara GNN dapat memodelkannya secara eksplisit dan tetap valid pada konfigurasi stasiun yang bervariasi.

## 2. Gap Penelitian
1. **Graf statis vs dinamis:** Mayoritas GNN seismologi memakai graf k-NN/jarak statis. Untuk EEW, himpunan stasiun "aktif" tumbuh seiring waktu (gelombang tiba bertahap) sehingga **topologi graf seharusnya dinamis**, namun ini jarang dimodelkan.
2. **Spatio-temporal coupling:** Penggabungan dimensi spasial (antar-stasiun) dan temporal (evolusi waveform) dalam satu arsitektur GNN untuk EEW masih terbatas.
3. **Konstruksi edge berbasis fisika:** Edge umumnya hanya jarak; informasi fisik (ray-path, beda waktu tempuh teoretis, koherensi) belum dimanfaatkan.
4. **Skalabilitas & latensi** GNN untuk inferensi real-time belum banyak dibahas.

## 3. Novelty
- **Dynamic Spatio-Temporal GNN (DST-GNN)**: graf yang node/edge-nya diaktifkan progresif sesuai waktu tiba gelombang; message passing diperbarui setiap langkah waktu.
- **Physics-informed edges**: bobot edge dikondisikan oleh beda waktu tempuh teoretis (model kecepatan 1D) + koherensi sinyal, bukan sekadar jarak Euclidean.
- **Edge/attention learning**: GAT belajar pasangan stasiun mana yang paling informatif untuk estimasi sumber, sekaligus memberi interpretabilitas.
- **Output bertahap & robust**: prediksi magnitudo/lokasi/ground-motion yang stabil terhadap penambahan/penghapusan node.

## 4. Metodologi
**Baseline:** TEAM/Transformer multi-stasiun (Proposal 01), GCN statis, set-transformer tanpa struktur graf.

**Arsitektur usulan:**
1. *Node features*: embedding waveform per stasiun (CNN 1D) + metadata (koordinat, ketinggian, SNR, status aktif/belum).
2. *Graph construction*: kandidat edge dari k-NN + Delaunay, bobot dipelajari (learned attention) dengan prior fisika (Δt travel-time, koherensi).
3. *Spatial layer*: GAT / message-passing antar-stasiun.
4. *Temporal layer*: GRU/temporal attention pada embedding node lintas langkah waktu → DST-GNN block bertumpuk.
5. *Heads*: lokasi (lat/lon/depth), magnitudo, ground-motion target, semuanya dengan uncertainty.

**Pelatihan:** multi-task loss (lokasi + magnitudo + GM) berbobot; augmentasi station-dropout & temporal masking; AdamW.

**Ablation:** graf statis vs dinamis; physics-edge vs distance-edge; GAT vs GCN vs MPNN; jumlah hop; sensitivitas terhadap penghapusan stasiun.

**Metrik:** akurasi lokasi (km), MAE magnitudo vs lead-time, GM residual, warning-time, robustness node-dropout, biaya komputasi/latensi.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **INSTANCE** (Michelini et al. 2021, *ESSD*) — metadata stasiun kaya; ideal untuk konstruksi graf multi-stasiun. Terbuka via INGV.
2. **STEAD** (Mousavi et al. 2019, *IEEE Access*) — pretraining encoder node; terbuka via GitHub.
3. **SCEDC / Southern California** — Southern California Earthquake Data Center; waveform + katalog lokasi/magnitudo terbuka (AWS Open Data `scedc-pds`).

> Minimal dua benchmark publik (INSTANCE + STEAD) memenuhi syarat; SCEDC menambah jaringan padat dengan ground-truth.

### 5.2 Data Pelengkap / Akses Terbatas
- **Japan K-NET/KiK-net (NIED)** — registrasi gratis; jaringan padat untuk pelatihan EEW.
- **Indonesia BMKG / GEOFON (FDSN)** — uji generalisasi jaringan jarang (BMKG via permohonan; GEOFON terbuka).

## 6. Risiko & Mitigasi
- *Kompleksitas graf dinamis* → mulai dari graf semi-dinamis (snapshot per interval), tingkatkan bertahap.
- *Overfitting struktur jaringan tertentu* → latih lintas-region + augmentasi geometri.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 persiapan data + baseline GCN statis; 2–3 implementasi DST-GNN + physics edges; 4 ablation; 5 evaluasi lintas-region + latensi; 6 penulisan.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **McBrearty, I.W. & Beroza, G.C. (2023).** Earthquake Phase Association with Graph Neural Networks (GENIE). *Bulletin of the Seismological Society of America*, 113(2), 524–547. arXiv:2209.07086. — graf stasiun + graf sumber; rujukan inti GNN seismik.
- **McBrearty, I.W. & Beroza, G.C. (2022).** Earthquake Location and Magnitude Estimation with Graph Neural Networks. arXiv:2203.05144 (IEEE ICIP 2022) `[cek]`. — GNN mendukung jumlah/posisi stasiun bervariasi.
- **Münchmeyer, J., et al. (2021).** TEAM. *Geophysical Journal International*, 225(1), 646–656. — baseline transformer multi-stasiun.
- **Zhu, W., et al. (2022).** GaMMA: earthquake phase association using a Bayesian Gaussian mixture model. *JGR: Solid Earth*, 127, e2021JB023249 `[cek]`.
- **Dataset:** INSTANCE (Michelini et al. 2021, *ESSD* 13:5509); STEAD (Mousavi et al. 2019, *IEEE Access* 7:179464).

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). Tautan adalah laman resmi penyedia.

- INSTANCE — https://instance.ingv.it/
- STEAD — https://github.com/smousavi05/STEAD
- SCEDC (AWS Open Data) — https://registry.opendata.aws/southern-california-earthquake-data/
- K-NET/KiK-net (NIED) — https://www.kyoshin.bosai.go.jp/ · GEOFON — https://geofon.gfz-potsdam.de/
