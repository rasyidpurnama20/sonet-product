# Proposal 05 — Deteksi Dini Penyakit Pernapasan Unggas via Analisis Bioakustik Berbasis Deep Learning

**Domain:** Smart Poultry / Acoustic Deep Learning
**Target luaran:** Q1 journal (Computers and Electronics in Agriculture / Poultry Science), sistem monitoring akustik kontinu.

---

## 1. Latar Belakang
Penyakit pernapasan (mis. Newcastle Disease, Infectious Bronchitis) menimbulkan gejala suara khas (bersin, ngorok/rales, batuk) sebelum tanda klinis terlihat jelas. Vokalisasi flock juga mencerminkan stres, kepadatan, dan kenyamanan termal. Pemantauan akustik bersifat **non-invasif, murah, dan kontinu**, namun pengenalan suara penyakit tertantang oleh derau kandang (kipas, pakan, mesin), tumpang-tindih suara banyak ekor, dan label medis yang langka.

## 2. Gap Penelitian
1. **Deteksi dini (pre-clinical):** Sebagian besar studi mengklasifikasi kondisi yang sudah jelas; **deteksi perubahan akustik sebelum gejala klinis** masih minim.
2. **Robust terhadap derau industri:** Performa di lingkungan kandang nyata (kipas/blower berisik) belum teruji luas.
3. **Label medis terbatas:** Ground-truth diagnosis berbiaya tinggi → kebutuhan pendekatan **self-supervised/weakly-supervised**.
4. **Flock-level vs individual:** Pemodelan sinyal level-flock (campuran banyak ekor) untuk indikator kesehatan agregat masih kurang.

## 3. Novelty
- **Self-supervised audio pretraining** (contrastive / masked-spectrogram) pada rekaman kandang tak berlabel, lalu fine-tune ke deteksi suara penyakit → mengatasi kelangkaan label.
- **Deteksi dini berbasis drift**: pemodelan **baseline akustik flock sehat** + deteksi anomali/perubahan distribusi sebagai sinyal peringatan dini, bukan sekadar klasifikasi.
- **Denoising-aware front-end**: pemisahan suara unggas dari derau mesin (source separation) sebelum klasifikasi.
- **Edge-ready** monitoring kontinu (mikrofon array murah + model ringan).

## 4. Metodologi
**Baseline:** CNN atas log-mel spectrogram, PANNs/AST (audio transformer) fine-tuned, SVM atas fitur MFCC.

**Pipeline usulan:**
1. *Pra-pemrosesan*: VAD unggas, denoising/source-separation, log-mel/learnable front-end.
2. *Pretraining SSL*: masked spectrogram modeling / contrastive (SimCLR-audio) pada data kandang tak berlabel.
3. *Downstream*: klasifikasi suara (sehat/bersin/rales/batuk) + regresi indeks kesehatan flock; modul deteksi anomali (autoencoder/one-class) untuk early warning.
4. *Temporal aggregation*: tren harian indeks akustik → alarm dini.

**Pelatihan:** loss kontrastif (pretrain), cross-entropy + class weighting (downstream), reconstruction loss (anomaly).

**Ablation:** SSL vs from-scratch; pengaruh denoising; flock-level vs window-level; sensitivitas SNR; lead-time deteksi vs konfirmasi klinis.

**Metrik:** F1/AUC per kelas suara, AUROC anomaly, **lead-time** deteksi sebelum diagnosis klinis, robustness vs derau (dB), latensi edge.

## 5. Dataset

### 5.1 Dataset Benchmark Publik (≥2, wajib — terverifikasi terbuka)
1. **Poultry Vocalization Signal Dataset for Early Disease Detection** — Mendeley Data (DOI: 10.17632/zp4nf2dxbh). 346 berkas audio: *healthy* (139), *noise* (86), *unhealthy* (121). Benchmark klasifikasi suara sehat/sakit.
2. **SmartEars** — Mendeley Data (DOI: 10.17632/dy6gtvt4mk). 6.000 klip 5-detik (Healthy / Sick / None) untuk monitoring pernapasan; open access.
3. **Stress-Induced Audio Responses in Hens** — Zenodo (record 10433023). Audio respons stres (kontrol vs treatment); untuk deteksi anomali/stres.
4. **`IceKhoffi/chicken-health-behavior-multimodal` (HuggingFace)** — audio (+visual) untuk deteksi dini gangguan kesehatan.

> Minimal dua benchmark publik (Mendeley Poultry Vocalization + SmartEars) memenuhi syarat; Zenodo & HF menambah variasi stres/anomali.

### 5.2 Data Pelengkap & Augmentasi
- **ESC-50 / AudioSet (subset farm/animal)** — pretraining tambahan & sumber derau.
- **Augmentasi derau industri**: mixing dengan suara kipas/blower untuk robustness.
- **Akuisisi mandiri** (opsional): rekaman kandang + log diagnosis dokter hewan sebagai label lemah.

> Catatan etik: koordinasi dengan dokter hewan & protokol kesejahteraan hewan.

## 6. Risiko & Mitigasi
- *Label diagnosis langka* → SSL + weak labels + anomaly detection.
- *Derau ekstrem* → source separation + augmentasi + mic array.
- *Variasi breed/usia* → pemodelan baseline adaptif per flock.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 setup audio + koleksi data; 2 pretraining SSL + baseline; 3–4 downstream + anomaly early-warning; 5 uji lapangan + validasi klinis; 6 penulisan + rilis.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Mao, A., et al. (2022).** Automated identification of chicken distress vocalizations using deep learning models. *Journal of the Royal Society Interface*, 19(186), 20210921. doi:10.1098/rsif.2021.0921. — rujukan inti vokalisasi distress.
- **Manikandan, V., et al. (2025).** Decoding Poultry Welfare from Sound — A Machine Learning Framework for Non-Invasive Acoustic Monitoring. *Sensors*, 25(9), 2912. — kerangka monitoring akustik kesejahteraan.
- **(2026).** Automatic chick cough detection (ASCT-CC) berbasis Audio Spectrogram Transformer dengan local multi-head attention. *Frontiers in Veterinary Science* `[cek vol]`. — deteksi batuk di lingkungan riil.
- **AI-Driven Bioacoustics in Poultry Farming (2025).** Systematic review analisis vokalisasi untuk stres & penyakit (*preprint*) `[cek]`. — survei domain.
- **Dataset:** SmartEars / SmartEars-style spectrogram corpora; HuggingFace `chicken-vocalization-classifier` & `chicken-health-behavior-multimodal` (audio+visual) `[cek lisensi]`.

*Content was rephrased for compliance with licensing restrictions.*


## 9. Tautan Akses Dataset (1-klik)
> Verifikasi keberadaan via pencarian web (Mei 2026). Mendeley/Zenodo adalah repositori data ber-DOI; ekstraksi HTTP otomatis terbatas karena SPA, tautan adalah laman resmi.

- Mendeley — Poultry Vocalization Signal Dataset for Early Disease Detection — https://data.mendeley.com/datasets/zp4nf2dxbh
- Mendeley — SmartEars (respiratory monitoring) — https://data.mendeley.com/datasets/dy6gtvt4mk/2
- Zenodo — Stress-Induced Audio Responses in Hens — https://zenodo.org/records/10433023
- HF `chicken-health-behavior-multimodal` — https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal
