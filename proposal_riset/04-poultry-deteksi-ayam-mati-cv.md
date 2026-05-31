# Proposal 04 — Deteksi Otomatis Ayam Mati di Kandang Broiler via Edge-AI Computer Vision

**Domain:** Smart Poultry / Computer Vision (Edge-AI)
**Target luaran:** Q1 journal (Computers and Electronics in Agriculture / Biosystems Engineering), prototipe edge device.

---

## 1. Latar Belakang
Mortalitas harian adalah indikator kesehatan flock yang kritis. Bangkai yang terlambat diangkat memicu penyakit, menurunkan kesejahteraan, dan menambah biaya. Inspeksi manual di kandang besar (puluhan ribu ekor) lambat, mahal, dan tidak kontinu. Computer vision menawarkan pemantauan otomatis 24/7, namun deteksi "ayam mati" sulit karena postur ayam mati menyerupai ayam tidur/duduk, oklusi tinggi, kepadatan padat, dan pencahayaan buruk.

## 2. Gap Penelitian
1. **Ambiguitas mati vs istirahat:** Deteksi berbasis frame tunggal sering keliru membedakan ayam mati dari ayam tidur/berbaring; **isyarat temporal (immobility)** jarang dimanfaatkan secara eksplisit.
2. **Edge real-time:** Banyak studi pakai model berat (server-GPU); deteksi **on-device latensi rendah & hemat daya** di lingkungan kandang nyata belum matang.
3. **Domain shift & kondisi nyata:** Variasi breed, kepadatan, litter, debu, dan pencahayaan IR menyebabkan penurunan performa lintas-kandang.
4. **Dataset langka & tidak seimbang:** Anotasi kejadian kematian sangat sedikit (rare event), menimbulkan class imbalance ekstrem.

## 3. Novelty
- **Spatio-temporal detection**: gabungan detektor objek (YOLO) + **modul immobility temporal** (tracking + analisis pergerakan selama jendela menit) untuk membedakan mati vs istirahat.
- **Edge-optimized pipeline**: model ringan (YOLO-nano/RT-DETR-tiny) dengan quantization (INT8) + pruning untuk Jetson/Raspberry Pi + akselerator, target <100 ms/frame.
- **Few-shot / anomaly framing** untuk rare event: kombinasi deteksi + skor anomali immobility agar tidak bergantung pada banyak label kematian.
- **Domain-generalization**: augmentasi sintetik (lighting/dust/density) + uji lintas-kandang.

## 4. Metodologi
**Baseline:** YOLOv8/v11 frame-based, Faster R-CNN, klasifikasi postur per-bounding-box.

**Pipeline usulan:**
1. *Deteksi & tracking*: detektor ringan + multi-object tracking (ByteTrack) untuk ID per ekor.
2. *Fitur temporal*: pergerakan/optical-flow & durasi immobility per track; flag kandidat "tak bergerak lama".
3. *Klasifikasi event*: head spatio-temporal (mis. fitur track → MLP/transformer kecil) mengeluarkan probabilitas "mati" + lokasi.
4. *Edge deployment*: konversi ONNX/TensorRT, INT8 quantization, uji daya & throughput.

**Pelatihan:** transfer dari COCO/poultry pretrain; focal loss untuk imbalance; augmentasi domain.

**Ablation:** frame-only vs +temporal; ukuran model vs akurasi/latensi; pengaruh quantization; lintas-kandang generalization.

**Metrik:** precision/recall/F1 & AP deteksi, akurasi event mati (per-jam), false alarm/hari, latensi & konsumsi daya di edge, waktu hingga deteksi (detection delay).

## 5. Dataset
- **Dataset publik unggas**: "Chicken/Poultry detection" (Roboflow Universe), **Broiler/Chicken behavior datasets** (mis. dataset deteksi & postur ayam yang tersedia publik).
- **Akuisisi mandiri**: pemasangan kamera RGB + IR di kandang mitra (kolaborasi peternakan/Fakultas Peternakan), anotasi event kematian dengan validasi petugas.
- **Sintetik/augmentasi**: rendering kondisi pencahayaan/kepadatan untuk memperkaya rare event.

> Catatan etik: protokol animal-welfare & persetujuan mitra peternakan diperlukan.

## 6. Risiko & Mitigasi
- *Label kematian sangat langka* → anomaly/few-shot + akuisisi terjadwal saat rutinitas pengangkatan bangkai.
- *Oklusi & kepadatan* → kamera multi-sudut + tracking; fokus area lantai.
- *Generalisasi lintas-kandang* → uji hold-out kandang + domain augmentation.

## 7. Rencana 6 Bulan (ringkas)
Bulan 1 setup kamera + pengumpulan data; 2 anotasi + baseline YOLO; 3–4 modul temporal + edge optimization; 5 uji lapangan lintas-kandang; 6 penulisan + rilis dataset/kode.
