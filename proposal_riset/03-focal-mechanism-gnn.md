# Proposal 03 — Focal Mechanism Determination via Station-Network Graph Attention dengan Uncertainty Quantification

**Domain:** Seismologi / Graph Neural Networks
**Target luaran:** Q1 journal (GRL / BSSA), kontribusi metodologis (blind spot dari domain-map).

---

## 1. Latar Belakang
Focal mechanism (strike/dip/rake atau moment tensor) menggambarkan geometri patahan dan medan tegangan. Solusinya sangat bergantung pada **distribusi azimut & take-off angle** stasiun di focal sphere. Metode klasik (HASH, first-motion polarity, waveform inversion) sensitif terhadap cakupan stasiun yang buruk dan kesalahan polaritas. Ini adalah masalah yang **inheren geometris/graf**, namun pendekatan DL umumnya single-station atau konkatenasi sederhana.

## 2. Gap Penelitian
1. **Struktur graf eksplisit belum dimanfaatkan:** Sangat sedikit karya yang memodelkan jaringan stasiun sebagai graf di mana **topologi (cakupan azimut, geometri take-off angle)** dipelajari/dioptimalkan untuk inversi focal mechanism (blind spot #1 domain-map).
2. **Ketidakpastian:** Kebanyakan keluaran berupa point estimate; **posterior/uncertainty** atas strike/dip/rake masih jarang dalam kerangka DL.
3. **Cakupan azimut buruk:** Performa pada event dengan azimuthal gap besar (umum di jaringan jarang) belum dibahas secara sistematis.

## 3. Novelty
- **GNN dengan node = stasiun** (fitur: polaritas first-motion, amplitudo P/S, waveform pendek, take-off angle, azimut) dan **edge = relasi geometris di focal sphere** (beda azimut, beda take-off angle).
- **Graph attention (GAT)** yang belajar pasangan/triplet stasiun paling diskriminatif → interpretasi langsung di focal sphere.
- **Uncertainty-aware output**: distribusi atas strike/dip/rake via von Mises–Fisher / quantile / Monte-Carlo dropout, plus klasifikasi tipe sesar (normal/reverse/strike-slip).
- **Robust pada azimuthal gap**: augmentasi penghapusan stasiun untuk meniru cakupan buruk + kalibrasi ketidakpastian.

## 4. Metodologi
**Baseline:** HASH (first-motion), CNN single-station polarity → agregasi sederhana, MLP atas fitur konkatenasi.

**Arsitektur usulan:**
1. *Node features*: polaritas P (+/−), rasio amplitudo, embedding waveform pendek (CNN), take-off angle & azimut (dari lokasi + model kecepatan).
2. *Graph*: edge berbobot berdasarkan separasi azimut/take-off; learned attention (GAT).
3. *Readout*: graph-level pooling → head focal mechanism.
4. *Output*: parameter sumber (representasi kontinu rake via sin/cos; normal-vector double-couple) + uncertainty; opsional komponen moment tensor.

**Pelatihan:** loss geodesik pada ruang orientasi (Kagan angle) + NLL distribusi; augmentasi station-dropout & polarity-flip noise.

**Ablation:** graf geometris vs distance vs fully-connected; pengaruh jumlah/cakupan azimut stasiun; uncertainty calibration (reliability diagram); transfer ke jaringan jarang.

**Metrik:** Kagan angle vs solusi referensi, akurasi klasifikasi tipe sesar, kalibrasi ketidakpastian (PIT/coverage), degradasi terhadap azimuthal gap.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **SCEDC + katalog focal mechanism Southern California** (Yang et al. / Hauksson et al.) — ribuan solusi focal mechanism + waveform; terbuka via SCEDC (AWS Open Data `scedc-pds`) & SCEC. Set pelatihan utama.
2. **Global CMT (gCMT)** — katalog moment tensor global (event sedang–besar); terbuka via globalcmt.org. Label sumber + generalisasi global.
3. **STEAD** — terbuka via GitHub; pretraining encoder waveform + first-motion polarity.

> Minimal dua benchmark publik (SCEDC focal mechanism + Global CMT) memenuhi syarat; STEAD untuk pretraining.

### 5.2 Data Pelengkap / Akses Terbatas
- **Indonesia BMKG / GEOFON** — uji generalisasi pada jaringan jarang & azimuthal gap besar (BMKG via permohonan; GEOFON terbuka).

## 6. Risiko & Mitigasi
- *Label focal mechanism terbatas untuk event kecil* → fokus M≥3, augmentasi sintetik dari model double-couple.
- *Kesalahan polaritas otomatis* → gabungkan polaritas + amplitudo + waveform agar tidak bergantung satu fitur.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 kurasi katalog + baseline HASH/CNN; 2–3 GNN geometris + uncertainty; 4 ablation + kalibrasi; 5 evaluasi azimuthal-gap & transfer; 6 penulisan (GRL letter).


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Ross, Z.E., Meier, M.-A., Hauksson, E. (2018).** P-wave arrival picking and first-motion polarity determination with deep learning. *Journal of Geophysical Research: Solid Earth*, 123(6), 5120–5129. arXiv:1804.08804. — fondasi polaritas first-motion berbasis CNN.
- **Hara, S., et al. (2019).** P-wave first-motion polarity determination of waveform data in western Japan using deep learning. *Earth, Planets and Space*, 71, 127 `[cek nama penulis]`.
- **McBrearty, I.W. & Beroza, G.C. (2023).** Earthquake Phase Association with Graph Neural Networks (GENIE). *BSSA*, 113(2), 524–547. — pola pemodelan jaringan stasiun sebagai graf.
- **Li, S., et al. (2025).** A deep-learning framework for focal mechanism determination (aplikasi gempa Luding 2022). arXiv:2511.19185 `[cek]`. — tren terbaru DL focal mechanism.
- **Catatan blind spot:** GNN focal mechanism dengan struktur graf eksplisit + uncertainty masih jarang (lihat `research-map/01-domain-map.md`).
- **Dataset:** SCSN/SCEDC focal mechanism catalogs; Global CMT; STEAD.

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). Tautan adalah laman resmi penyedia.

- SCEDC — https://scedc.caltech.edu/ · AWS Open Data — https://registry.opendata.aws/southern-california-earthquake-data/
- Global CMT — https://www.globalcmt.org/
- STEAD — https://github.com/smousavi05/STEAD
- Indonesia: GEOFON — https://geofon.gfz-potsdam.de/ · IRIS FDSN — https://service.iris.edu/
