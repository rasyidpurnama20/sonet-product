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
- **INSTANCE** (Italia) — metadata kaya, ideal untuk konstruksi graf multi-stasiun.
- **STEAD** — pretraining encoder node.
- **Japan K-NET/KiK-net (NIED)** — jaringan padat untuk pelatihan EEW.
- **Southern California (SCSN / SCEDC)** — katalog padat + ground-truth lokasi/magnitudo.
- **Indonesia BMKG / GEOFON (FDSN)** — uji generalisasi jaringan jarang.

## 6. Risiko & Mitigasi
- *Kompleksitas graf dinamis* → mulai dari graf semi-dinamis (snapshot per interval), tingkatkan bertahap.
- *Overfitting struktur jaringan tertentu* → latih lintas-region + augmentasi geometri.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 persiapan data + baseline GCN statis; 2–3 implementasi DST-GNN + physics edges; 4 ablation; 5 evaluasi lintas-region + latensi; 6 penulisan.
