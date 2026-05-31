# Reverse-Engineering Plan & Tracking Board
## Artikel: *Deep Learning for Earthquake Early Warning Systems: Single-Station vs Multi-Station*

> **Tujuan dokumen.** Dokumen ini membongkar (reverse-engineer) artikel review `artikel_review_2/main.tex`
> menjadi poin-poin yang bisa **dilacak (tracking)**. Setiap poin punya status:
>
> - `[x]` = sudah ada / selesai di artikel saat ini
> - `[~]` = ada tapi masih perlu diperkuat (data, sitasi, atau gambar)
> - `[ ]` = belum ada / backlog untuk increment berikutnya
>
> **Cara pakai:** centang/ubah status saat Anda meninjau tiap bagian. Bagian H (Backlog) adalah daftar
> kerja konkret untuk PR-PR berikutnya.
>
> _Catatan: Integrasi paper terbaru 2024–2026 dikirim lewat **PR #29**
> (`feature/dl-eew-recent-papers-2024-2026`). Dokumen ini sudah mencerminkan kondisi setelah PR tsb._

---

## A. Blueprint / Metadata Artikel

| Atribut | Nilai |
|---|---|
| Judul | Deep Learning for EEW: A Comprehensive Review of Single-Station vs Multi-Station Approaches |
| Kelas dokumen | `elsarticle` (mode `review`, `authoryear`) |
| Target jurnal | `Earth-Science Reviews` (`\journal{...}`) |
| Tipe | Review/survey (bukan eksperimen primer) |
| Penulis | Ahmad R. Purnama (Undip) |
| Gaya sitasi | `elsarticle-harv` (Harvard, author–year) |
| Panjang saat ini | ~44 halaman, 106 entri referensi |
| Toolchain build | `pdflatex` → `bibtex` → `pdflatex` ×2 |

- [x] Frontmatter: title, author, affiliation, abstract, keywords
- [x] Abstract memuat tesis "hybrid = jalan terbaik"
- [x] 10 keywords relevan
- [ ] (Opsional) ORCID & funding statement eksplisit di frontmatter

---

## B. Tesis Sentral & Kontribusi (the "spec")

**Tesis:** Single-station unggul di **latensi**, multi-station unggul di **akurasi karakterisasi sumber**;
**arsitektur hybrid/cascaded** yang memadukan keduanya adalah jalur menuju EEW generasi berikutnya.

Kontribusi yang dijanjikan di §1.4 (harus konsisten dgn isi):
- [x] K1 — Taksonomi arsitektur DL untuk EEW (per paradigma & per task)
- [x] K2 — Perbandingan kinerja terstandar antar metode
- [x] K3 — Analisis trade-off akurasi–latensi
- [x] K4 — Pertimbangan deployment (kompresi model, integrasi infra)
- [x] K5 — Open problems & arah masa depan (termasuk hybrid)
- [~] Verifikasi: setiap klaim kontribusi punya bukti/tabel/gambar pendukung di body

---

## C. Peta Bagian (Section-by-Section) + Checklist Konten

### §1 Introduction `\label{sec:introduction}`
- [x] Motivasi bencana (Tohoku 2011, Turki–Suriah 2023)
- [x] Prinsip fisik P/S wave & jendela peringatan
- [x] Sejarah singkat (Cooper 1868, UrEDAS) + sistem operasional dunia
- [x] §1.1 Limitasi metode tradisional (speed-accuracy, saturasi, false alert, jaringan jarang)
- [x] §1.2 Revolusi DL + **tren foundation/generalized model 2024–2026**
- [x] §1.3 Paradigma single vs multi (definisi tegas)
- [x] §1.4 Scope & kontribusi + peta paper

### §2 Fundamentals `\label{sec:fundamentals}`
- [x] §2.1 Prinsip fisik (Vp/Vs, persamaan kecepatan & warning time)
- [x] §2.2 On-site vs regional + rumus `\tau_c` (sudah sesuai definisi Kanamori)
- [x] §2.3 Tabel sistem operasional dunia (`tab:operational_systems`)
- [x] §2.4 Pipeline EEW (Gambar `fig:eew_pipeline`)
- [x] §2.5 Tantangan teknis (saturasi, false alert, heterogenitas jaringan)
- [ ] (Backlog) Tambah baris tabel: BMKG InaTEWS / konteks Indonesia

### §3 Deep Learning Foundations `\label{sec:dl_foundations}`
- [x] §3.1 CNN (Conv1D, U-Net, residual, dilated)
- [x] §3.2 RNN/LSTM/GRU (+ CRED, bidirectional vs causal untuk real-time)
- [x] §3.3 Attention/Transformer (+ EQTransformer, TEAM, ViT)
- [x] §3.4 GNN (GCN, GAT, GraphSAGE)
- [x] §3.5 Autoencoder & generative (denoising, augmentasi, anomali)
- [x] §3.6 Strategi training (augmentasi, class imbalance, transfer, regularisasi)
- [x] Gambar perbandingan arsitektur (`fig:architecture_comparison`)

### §4 Single-Station Methods `\label{sec:single_station}`
- [x] §4.1 Deteksi & phase picking: PhaseNet, EQTransformer, GPD
- [x] §4.1.4 Picker tambahan: ARRU, CapsPhase, ConvNetQuake, **FisH (2024)**
- [x] §4.1.5 Tabel perbandingan picker (`tab:single_station_pickers`)
- [x] §4.2 Estimasi magnitudo (CREIME, TEAM, uncertainty/MC-dropout)
- [x] §4.3 Lokasi & back-azimuth single station
- [x] §4.4 Kelebihan single-station
- [x] §4.5 Keterbatasan single-station

### §5 Multi-Station Methods `\label{sec:multi_station}`
- [x] §5.1 Deteksi jaringan & asosiasi fase (PhaseLink, graph associators, **PLAN**, **PhaseNet+**)
- [x] §5.2 Karakterisasi sumber (joint location-magnitude, focal mechanism)
- [x] §5.3 Prediksi ground motion (graph GM fields, **SC-GNN**, **SENSE**, **WaveCastNet**)
- [x] §5.4 Pendekatan GNN untuk EEW
- [x] §5.5 Kelebihan multi-station
- [x] §5.6 Keterbatasan multi-station

### §6 Comparative Analysis `\label{sec:comparative}`
- [x] §6.1 Tabel perbandingan kinerja menyeluruh (longtable) + **6 baris metode 2024–2026**
- [x] §6.2 Analisis trade-off akurasi–latensi
- [x] §6.3 Skalabilitas & robustness (kepadatan jaringan, station dropout)
- [x] §6.4 Pendekatan hybrid (`\label{sec:hybrid}`: cascaded/parallel)
- [x] §6.5 Cost-benefit per skenario deployment
- [~] (Perkuat) Gambar kurva akurasi-vs-latensi kuantitatif jika data tersedia

### §7 Datasets & Evaluation `\label{sec:datasets}`
- [x] §7.1 Dataset benchmark (STEAD, INSTANCE, LEN-DB, DiTing)
- [x] §7.2 Metrik evaluasi
- [x] §7.3 SeisBench (framework standar)
- [x] §7.4 Tantangan generalisasi lintas-dataset
- [ ] (Backlog) Tambah dataset terbaru (mis. PNW, CREW, dataset OBS/DAS)

### §8 Deployment Challenges `\label{sec:deployment}`
- [x] §8.1 Latensi & edge computing
- [x] §8.2 Kompresi & optimasi model (distillation, quantization)
- [x] §8.3 Arsitektur streaming inference (causal)
- [x] §8.4 Fault tolerance & graceful degradation
- [x] §8.5 Integrasi dgn infrastruktur eksisting
- [ ] (Backlog) Studi kasus DAS / smartphone-based EEW

### §9 Future Directions `\label{sec:future}`
- [x] §9.1 Foundation models (+contoh konkret: **SeisLM, SeisMoLLM, U-Trans**)
- [x] §9.2 **Recent Advances Toward Unified & Generalizable EEW (2024–2026)** — subbab baru
- [x] §9.3 Physics-Informed Neural Networks
- [x] §9.4 Federated learning lintas-negara
- [x] §9.5 Uncertainty quantification
- [x] §9.6 Explainable AI
- [x] §9.7 Multi-hazard early warning
- [x] §9.8 Self-supervised & few-shot untuk wilayah minim data

### §10 Conclusions `\label{sec:conclusions}`
- [x] 6 temuan kunci
- [x] Rekomendasi praktisi
- [x] Outlook (konvergensi paradigma)
- [x] Declaration of Competing Interest + Acknowledgments

---

## D. Inventaris Metode (yang harus terlacak di taksonomi)

**Single-station**
- [x] PhaseNet · [x] EQTransformer · [x] GPD · [x] CRED · [x] ARRU · [x] CapsPhase
- [x] ConvNetQuake · [x] CREIME · [x] FisH (unified, 2024)
- [ ] (Backlog) CREIME-A / model magnitudo single-station 2025–2026 lainnya

**Multi-station**
- [x] PhaseLink · [x] GaMMA/graph associators · [x] TEAM · [x] PLAN (2024) · [x] PhaseNet+ (2025)
- [x] SC-GNN (2024) · [x] SENSE (2024) · [x] WaveCastNet (2025) · [x] Bloemheuvel GNN · [x] MALMI
- [ ] (Backlog) GRAPES (wavefield-based EEW) · [ ] spatio-temporal graph detection (2025)

**Foundation / generalized**
- [x] SeisLM (2024) · [x] SeisMoLLM (2025) · [x] U-Trans (2026) · [x] Universal NN (2024)
- [ ] (Backlog) SeisCLIP · [ ] Seismic Foundation Model (SFM, eksplorasi)

---

## E. Inventaris Gambar & Tabel

| ID | Tipe | Isi | Status |
|---|---|---|---|
| `fig:eew_pipeline` | TikZ | Pipeline EEW + titik enhancement DL | [x] |
| `fig:architecture_comparison` | TikZ | Perbandingan CNN/RNN/Transformer/GNN | [x] |
| `tab:operational_systems` | Tabel | Sistem EEW operasional dunia | [x] |
| `tab:single_station_pickers` | Tabel | Perbandingan picker single-station | [x] |
| (longtable §6.1) | Tabel | Perbandingan kinerja menyeluruh (+6 baris baru) | [x] |
| — | Gambar | Kurva akurasi-vs-latensi kuantitatif | [ ] backlog |
| — | Gambar | Peta sebaran metode pada sumbu latensi–akurasi | [ ] backlog |

---

## F. Inventaris Referensi & Cakupan Tahun

- [x] Total entri `.bib`: **106** — semua tersitasi (0 uncited, 0 undefined)
- [x] Konsistensi key/tahun: `brown2011elarms` (sebelumnya `brown2017elarms`) sudah diperbaiki
- [x] Rumus `\tau_c` sudah sesuai definisi standar
- [x] **Tambahan 2024–2026 (10):** SeisLM, SeisMoLLM, U-Trans, Universal NN, FisH, PLAN,
      PhaseNet+, SC-GNN, SENSE, WaveCastNet

**Sebaran tahun (target: tetap segar s/d Juni 2026)**
- [x] 2024: ✔ beberapa · [x] 2025: ✔ (WaveCastNet, PhaseNet+, SeisMoLLM) · [x] 2026: ✔ (U-Trans)
- [ ] (Backlog) Tambah lagi paper 2025–2026 untuk memperkuat cakupan (lihat Bagian H)

---

## G. Build & Reproduksi

- [x] Compile bersih: 44 halaman, 0 error, 0 undefined citation, 0 warning BibTeX
- [x] Artefak LaTeX (`*.aux`, `*.bbl`, `*.log`, dll.) sudah di-`.gitignore`
- [x] Hanya `main.tex`, `references.bib`, `main.pdf` yang di-track
- [ ] (Opsional) Tambah GitHub Action untuk auto-compile LaTeX di setiap PR
- [ ] (Opsional) Tambah `Makefile`/`latexmkrc` agar build 1 perintah

**Langkah reproduksi:**
```bash
cd artikel_review_2
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## H. Backlog / Increment Berikutnya (trackable)

> Tiap item di sini dirancang jadi **satu PR kecil** agar aman dari limit & mudah di-review.

- [ ] **B1 — Batch referensi 2025–2026 lanjutan**
  kandidat terverifikasi: DAS-based EEW (Sci Rep 2026), physics-informed single-station
  detection+magnitude (Bull. Earthquake Eng. 2026), spatio-temporal graph detection (2025),
  GRAPES (wavefield EEW).
- [ ] **B2 — Konteks Indonesia**: tambah InaTEWS/BMKG di tabel sistem operasional + paragraf relevansi.
- [ ] **B3 — Gambar trade-off kuantitatif** (akurasi vs latensi; peta metode).
- [ ] **B4 — Perkuat §7** dengan dataset terbaru (PNW, OBS/DAS) + tabel ringkas dataset.
- [ ] **B5 — Studi kasus deployment** (edge/DAS/smartphone) di §8.
- [ ] **B6 — CI LaTeX** (GitHub Action) + `latexmkrc`.
- [ ] **B7 — Pengecekan akhir**: konsistensi notasi, daftar singkatan, proofread bahasa.

---

## I. Dashboard Status (ringkasan cepat)

| Area | Status |
|---|---|
| Struktur 10 bagian | ✅ lengkap |
| Taksonomi metode | ✅ lengkap (single/multi/foundation) |
| Integrasi paper 2024–2026 | ✅ 10 paper (via PR #29) |
| Build PDF | ✅ bersih, 44 hlm |
| Integritas sitasi | ✅ 106/106 tersitasi |
| Gambar kuantitatif trade-off | ⬜ backlog (B3) |
| Konteks Indonesia | ⬜ backlog (B2) |
| CI/otomasi build | ⬜ backlog (B6) |

_Terakhir diperbarui: 2026-05-31._
