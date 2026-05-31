# Proposal 08 — Transfer & Self-Supervised Learning untuk Seismic Phase Picking di Wilayah Under-Instrumented (Studi Kasus Indonesia)

**Domain:** Seismologi / Deep Learning (Foundation Models & Transfer Learning)
**Target luaran:** Q1 journal (SRL / JGR: Solid Earth), model & katalog pick yang dirilis.

---

## 1. Latar Belakang
Phase picking (waktu tiba P/S) adalah fondasi pemrosesan katalog gempa. Model DL (PhaseNet, EQTransformer) sangat baik pada region tempat mereka dilatih (mis. California, Italia), namun **domain shift** (instrumen, kebisingan, geologi, distribusi magnitudo) menurunkan performa di wilayah under-instrumented seperti Indonesia. Pelabelan ulang berskala besar mahal dan lambat.

## 2. Gap Penelitian
1. **Domain shift lintas-jaringan:** Penurunan recall/presisi picker pra-latih saat dipindah ke jaringan/region baru belum dikuantifikasi & ditangani secara sistematis untuk Indonesia.
2. **Label lokal langka:** Strategi **few-shot / self-supervised** untuk adaptasi dengan sedikit label lokal masih minim.
3. **Robust terhadap derau lokal:** Kebisingan oseanik/antropogenik tropis berbeda dari region pelatihan.
4. **Evaluasi hilir:** Dampak kualitas pick terhadap lokasi/magnitudo katalog jarang dievaluasi end-to-end.

## 3. Novelty
- **Self-supervised pretraining** pada waveform kontinu Indonesia tak berlabel (contrastive/masked-waveform) → encoder yang sadar-domain, lalu fine-tune picking dengan label minimal.
- **Domain adaptation**: teknik adaptasi (mis. fine-tuning bertahap, pseudo-labeling beriterasi/teacher-student, adversarial domain alignment) untuk menjembatani region sumber→target.
- **Few-shot benchmark Indonesia**: protokol evaluasi & kurva "jumlah label vs akurasi".
- **Evaluasi end-to-end**: dampak terhadap akurasi lokasi & magnitudo katalog, bukan hanya metrik pick.

## 4. Metodologi
**Baseline:** PhaseNet & EQTransformer pra-latih (zero-shot), pelatihan from-scratch lokal, STA/LTA klasik.

**Pipeline usulan:**
1. *Pretraining SSL*: masked/contrastive learning pada arsip waveform kontinu Indonesia (GEOFON/BMKG/IRIS).
2. *Adaptasi*: pseudo-labeling teacher-student + fine-tuning dengan sedikit label terverifikasi; opsi adversarial alignment.
3. *Picker head*: arsitektur U-Net/transformer untuk probabilitas P/S.
4. *Hilir*: asosiasi (GaMMA) + lokasi → bandingkan katalog hasil.

**Pelatihan:** loss SSL (pretrain) + cross-entropy/Gaussian-label (pick); augmentasi noise lokal, time-shift, channel dropout.

**Ablation:** zero-shot vs fine-tune vs SSL+fine-tune; jumlah label lokal (few-shot curve); pseudo-labeling on/off; pengaruh augmentasi derau.

**Metrik:** precision/recall/F1 pick & residual waktu (s), peningkatan jumlah event terdeteksi, akurasi lokasi/magnitudo katalog, biaya pelabelan.

## 5. Dataset
- **STEAD / INSTANCE / California (NCEDC/SCEDC)** — sumber pra-latih & label melimpah.
- **Indonesia: BMKG, GEOFON (GFZ), IRIS-FDSN** — waveform kontinu & event regional (target adaptation/evaluasi).
- **Label lokal**: subset event tervalidasi analis BMKG / katalog ISC sebagai ground-truth few-shot.

## 6. Risiko & Mitigasi
- *Akses data BMKG* → gunakan FDSN/GEOFON publik + permohonan resmi; mulai dari arsip terbuka.
- *Pseudo-label noisy* → confidence thresholding + iteratif teacher-student.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 kurasi waveform + baseline zero-shot; 2 SSL pretraining; 3–4 domain adaptation + few-shot; 5 evaluasi katalog hilir; 6 penulisan + rilis model/katalog.


## 8. Referensi Kunci / Related Work
> Diverifikasi via pencarian web (Mei 2026). Tanda `[cek]` = venue/tahun sebaiknya dikonfirmasi ulang sebelum dikutip formal.

- **Zhu, W. & Beroza, G.C. (2019).** PhaseNet. *Geophysical Journal International*, 216(1), 261–273. — picker dasar.
- **Mousavi, S.M., et al. (2020).** EQTransformer. *Nature Communications*, 11, 3952. — deteksi + picking simultan.
- **Münchmeyer, J., et al. (2022).** Which picker fits my data? A quantitative evaluation of deep learning based seismic pickers. *JGR: Solid Earth*, 127, e2021JB023499. — bukti domain shift lintas-dataset.
- **Jozinović, D., et al. (2022).** Transfer learning untuk prediksi ground shaking pada area dengan data latih terbatas. *Geophysical Journal International*, 229(1), 704–718. — strategi transfer inti.
- **Dataset:** STEAD (Mousavi 2019, *IEEE Access*); INSTANCE (Michelini 2021, *ESSD*); waveform Indonesia via GEOFON/IRIS-FDSN/BMKG.

*Content was rephrased for compliance with licensing restrictions.*
