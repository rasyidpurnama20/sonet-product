#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Membangun file penilaian Pengenalan Pola A (pola-2026) yang FINAL & bersih.

Kolom keluaran:
  NIM, Nama,
  Classification Task (Intermediate),
  Evaluation Metric Quiz,
  Manual Classification Task (Beginner),
  Oral,                              <- dinilai dari folder oral/  (esai design cycle)
  Arsitektur,                        <- dinilai dari folder arsitektur/ (laporan DL MRI)
  Proyek (Presentasi + Keaktifan)    <- nilai milik pengampu (master sheet)

Catatan:
- ROSTER (master) adalah daftar resmi 50 mahasiswa berikut nilai
  Classification/Quiz/Manual + "Proyek (Presentasi + Keaktifan)" dari pengampu.
- Kolom Oral & Arsitektur (skala 0-10) ditambahkan dari hasil pembacaan submission.
  Sel kosong = tidak mengumpulkan.
- Penilaian kualitas laporan proyek kelompok TIDAK lagi dijadikan kolom terpisah
  agar tidak menduplikasi kolom "Proyek (Presentasi + Keaktifan)" milik pengampu.
- Justifikasi tiap nilai Oral & Arsitektur ada di penilaian-pola-2026-detail.csv.
"""
import csv, os

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# ROSTER MASTER (resmi): [NIM, Nama, ClassificationTask, Quiz, Manual, ProyekPK]
# ---------------------------------------------------------------------------
ROSTER = [
 ['24060119120041', 'Abida Akbar Rusyadin', '', '2.50', '', '0'],
 ['24060123120030', 'Adrian Asarel Deandra Kristiawan', '9.67', '5.00', '10.00', '95'],
 ['24060123120029', 'Aisha', '9.00', '10.00', '3.33', '80'],
 ['24060123130093', 'Arib Taufiqurrohman', '10.00', '7.50', '10.00', '92'],
 ['24060123130084', 'Assyifa Haqqi Dusanto', '8.00', '0.00', '3.33', '80'],
 ['24060123140201', 'Athiqotuz Zulaiva', '8.33', '10.00', '3.33', '80'],
 ['24060123130058', 'Axel Natakesuma', '10.00', '10.00', '3.33', '80'],
 ['24060123120002', 'Bagus Athallah', '10.00', '10.00', '8.33', '80'],
 ['24060123130051', 'Brilianita Eva Syafitri', '', '', '', '82'],
 ['24060123130079', 'Christiano Bryan Budiman', '9.33', '10.00', '6.67', '-10'],
 ['24060123140175', 'Cikal Wahyuning Bachtiar', '9.00', '10.00', '5.00', '80'],
 ['24060123130073', 'Dary Ihsan Amanullah', '', '', '', '85'],
 ['24060123140045', 'Dewi Larasati Mumpuni', '9.00', '', '8.33', '0'],
 ['24060123120040', 'Dhimas Luthfi Arnanda', '9.67', '7.50', '10.00', '87'],
 ['24060123130080', 'Dimas A Albanna Zain', '9.00', '7.50', '8.33', '82'],
 ['24060123120016', 'Dina Amelia', '', '', '', '82'],
 ['24060123140147', 'Eliza Talent Sirait', '7.67', '10.00', '5.00', '80'],
 ['24060123140111', 'Evia Auamara Unsa Nasyta', '10.00', '10.00', '8.33', '80'],
 ['24060123130098', 'Felis Eren Cristi Milala', '6.00', '7.50', '8.33', '80'],
 ['24060123140211', 'Ferza Farrell Wibowo', '', '0.00', '', '-10'],
 ['24060123130094', 'Gabriel Prakosa Ardhi', '8.67', '0.00', '6.67', '87'],
 ['24060123120028', 'George Imanuel Surya', '7.67', '0.00', '6.67', '87'],
 ['24060123130112', 'Gibran Ahmad Maulana', '10.00', '10.00', '10.00', '0'],
 ['24060123130110', 'Gusti Ayu Genta Bhuana Paramitha', '9.67', '10.00', '8.33', '0'],
 ['24060123140197', 'Hadyan Kholish Prasetio', '9.33', '2.50', '8.33', '90'],
 ['24060123140151', 'Haidar Ali Laudza', '8.33', '10.00', '8.33', '90'],
 ['24060120130039', 'Hikmal Arkan Nur Zaidan', '', '', '', '-10'],
 ['24060123120009', 'Indah Nurul Janah', '8.67', '5.00', '3.33', '87'],
 ['24060123140150', 'Indra Purwanto', '9.67', '0.00', '10.00', '80'],
 ['24060123130101', 'Jihan Saniyya Pudaliba', '', '', '', '-10'],
 ['24060123130117', 'Julius Tegar Aji Putra', '9.67', '10.00', '8.33', '90'],
 ['24060123140179', 'Kaila Talitha Putri', '9.67', '10.00', '10.00', '0'],
 ['24060123140152', 'Kayis Hilmi Farih', '', '', '0.00', '0'],
 ['24060123130081', 'Kevin Adi Santoso', '9.33', '10.00', '10.00', '0'],
 ['24060123140166', 'Khairiya Fatih Izzudin Emarin', '9.00', '0.00', '5.00', '90'],
 ['24060123120032', 'Lulu Nikita Sitanggang', '6.67', '7.50', '6.67', '0'],
 ['24060123140204', 'Mohammad Imron Rosyadi', '9.33', '10.00', '8.33', '90'],
 ['24060123140139', 'Mohammad Izza Hakiki', '', '', '', '87'],
 ['24060123130086', 'Muhammad Azka Subhan', '8.00', '', '6.67', '80'],
 ['24060123130107', 'Muhammad Renno Baihaqi', '6.33', '5.00', '8.33', '-10'],
 ['24060123130106', 'Muhammad Yoga Aminudin', '8.00', '7.50', '6.67', '0'],
 ['24060123120023', 'Nadia Syifa Khairunnisa', '9.33', '5.00', '8.33', '0'],
 ['24060123120038', 'Nazla Azzahra Hermana', '', '', '', '0'],
 ['24060123140148', 'Nicholas Gunawan', '9.67', '7.50', '10.00', '80'],
 ['24060123130067', 'Nindya Kirana', '8.00', '', '8.33', '0'],
 ['24060123140142', 'Parisya Lituhayu Chandrawati Gunawarman', '7.00', '', '3.33', '0'],
 ['24060123130100', 'Patriot Antaras Bangsa', '', '7.50', '', '77'],
 ['24060122140184', 'Raden Rico Dwianda', '', '0.00', '', '0'],
 ['24060123120010', 'Shopia Mudjahidah', '8.00', '10.00', '5.00', '82'],
 ['24060123130114', 'Tsuraya Olivia', '9.33', '5.00', '10.00', '0'],
]

# ---------------------------------------------------------------------------
# ORAL (NIM -> (nilai 0-10, justifikasi))
# Rubrik: cakupan pipeline design cycle (data->preprocessing->ekstraksi fitur->
# model->evaluasi) + ketepatan konsep lanjutan + kejelasan/relevansi.
# ---------------------------------------------------------------------------
ORAL = {
 "24060119120041": (6.5, "Bahasan terpencar (ekstraksi fitur ResNet/MobileNet, confusion matrix multikelas, piksel RGB); tidak menggambarkan siklus utuh."),
 "24060122140184": (4.0, "Isi reflektif personal tentang skripsi & kehadiran; sangat minim substansi teknis materi."),
 "24060123120002": (8.0, "Definisi + pipeline lengkap (pengumpulan, ekstraksi fitur, model, pelatihan, evaluasi) + confusion matrix + Bayesian; ringkas tapi tepat."),
 "24060123120009": (8.3, "Poin-poin detail: preprocessing, feature space, decision boundary, low/high dimensionality, supervised/unsupervised, evaluasi."),
 "24060123120010": (8.2, "Pipeline lengkap + reduksi dimensi/overfitting + evaluasi performa."),
 "24060123120023": (8.0, "Tahapan + decision boundary + confusion matrix, analogi bayi; cukup lengkap."),
 "24060123120028": (8.3, "Design cycle terstruktur: preprocessing, ekstraksi fitur, reduksi dimensi, klasifikasi, evaluation metrics."),
 "24060123120029": (8.7, "Siklus utuh: data collection, preprocessing, PCA, train/test, k-CV, confusion matrix, ROC-AUC, Bayesian (ada salah ketik)."),
 "24060123120030": (9.3, "Sangat detail: ekstraksi fitur (spektrogram, GLCM), evolusi Bayesian->ML->ANN/CNN, metrik MAE/MSE/ROC-AUC, few-shot learning."),
 "24060123120032": (9.4, "Komprehensif & koheren: konteks ML, preprocessing, feature space, decision boundary, over/underfitting, Bayesian, minimum distance, metrik lengkap."),
 "24060123120040": (9.0, "Siklus lengkap dgn contoh ikan, feature space, train/val/test, confusion matrix + ROC-AUC."),
 "24060123130058": (7.5, "Konteks birdclef, pola manual per kelas, ekstraksi/pemilihan fitur, evaluasi; relatif singkat."),
 "24060123130067": (8.5, "Pipeline suara burung rinci: ekstraksi frekuensi, mel-spectrogram, split 80:10:10, training, hyperparameter tuning, testing."),
 "24060123130079": (9.2, "Definisi + design cycle sistematis, ekstraksi fitur sebagai tahap krusial, Bayesian/SVM/CNN, metrik, sifat iteratif."),
 "24060123130080": (7.8, "Probabilitas Bayesian (prior/evidence/likelihood), olah data, confusion matrix & metrik; cukup padat."),
 "24060123130081": (7.5, "Feature space, masalah dimensi (terlalu sedikit/banyak), Bayesian/Random Forest; tanpa tahap evaluasi rinci."),
 "24060123130084": (9.2, "Sangat detail: data collection/understanding, sampling, imbalance/SMOTE, augmentasi, preprocessing, modeling (SVM/RF/NB/ensemble), evaluasi."),
 "24060123130093": (6.0, "Hanya membahas decision boundary sebagai evaluator; sangat singkat & sempit."),
 "24060123130094": (8.5, "Design cycle lengkap + deployment + confusion matrix & komponen TP/FP."),
 "24060123130098": (8.2, "Metode klasifikasi (NB/KNN/SVM/DT), Bayesian, evaluasi (confusion matrix, akurasi/presisi/recall/F1)."),
 "24060123130100": (8.0, "Tantangan pengolahan data (audio->gambar), fitur informatif, metrics score untuk membandingkan model."),
 "24060123130107": (7.5, "Pipeline utama terdaftar: preprocessing, ekstraksi/seleksi, decision boundary, representasi, learning, evaluasi."),
 "24060123130110": (8.0, "Konteks birdclef, pattern recognition, design cycle, confusion matrix, Bayesian (prior/likelihood/posterior)."),
 "24060123130112": (9.0, "Detail: definisi, ekstraksi fitur (GLCM/PCA), perbandingan ML klasik vs deep learning ANN/CNN/konvolusi."),
 "24060123130114": (7.3, "Decision boundary, preprocessing, fitur, over/underfitting; cukup singkat."),
 "24060123130117": (9.0, "Evaluasi sangat rinci: confusion matrix micro/macro/weighted F1, ROC-AUC (TPR/FPR), Bayesian, design cycle."),
 "24060123140045": (8.5, "Akuisisi citra, preprocessing, ekstraksi fitur (warna/bentuk/tekstur), pemilihan fitur, decision boundary, over/underfitting, transformasi data."),
 "24060123140111": (8.3, "Tahapan lengkap + Bayesian (prior/likelihood/posterior) + over/underfitting + confusion matrix."),
 "24060123140142": (7.0, "Analogi manusia, raw data, fitur lightness vs length; berhenti di pemilihan fitur, tanpa model/evaluasi."),
 "24060123140148": (8.0, "Informal namun lengkap: design cycle, pentingnya fitur, decision boundary, over/underfitting, evaluasi (confusion matrix-ROC-AUC), Bayesian."),
 "24060123140150": (6.5, "Hanya menyebut tahapan design cycle secara singkat tanpa elaborasi."),
 "24060123140151": (7.5, "Mesin mengenali pola, konsep fungsi input-output, design cycle iteratif, preprocessing/ekstraksi fitur."),
 "24060123140166": (7.0, "Speech recognition, belajar dari data, contoh bayi, confusion matrix & evaluasi; agak terpencar."),
 "24060123140175": (8.5, "Detail: deteksi karakteristik pola, preprocessing audio->mel-spectrogram, evaluation metric, konsep Bayesian."),
 "24060123140179": (8.5, "Cakupan luas: fitur, decision boundary, ROC-AUC, arsitektur (MobileNet/EfficientNet/ResNet/Transformer/attention), pre/post-processing, metrik."),
 "24060123140197": (7.8, "Mendaftar banyak topik (design cycle, spectrogram, preprocessing, dimensionality, jenis learning, F1, ROC-AUC); cenderung berupa daftar."),
 "24060123140201": (8.5, "Siklus dari desain sampai evaluasi, preprocessing, ekstraksi fitur, pemilihan model, confusion matrix (TP/TN/FP/FN) + metrik."),
 "24060123140204": (9.3, "Sangat tepat: fitur diskriminatif (lightness vs length), curse of dimensionality, Bayesian/minimum distance/minimum error, jenis learning, evaluasi & generalisasi."),
 "24060123140211": (7.3, "Mesin mengenali pola, contoh klasifikasi ikan, preprocessing/ekstraksi fitur, over/underfitting; tanpa tahap model/evaluasi."),
}

# ---------------------------------------------------------------------------
# ARSITEKTUR (NIM -> (nilai 0-10, justifikasi))
# Rubrik: kelengkapan section + kedalaman & ketepatan teknis + kecanggihan
# arsitektur + kerapian akademik.
# ---------------------------------------------------------------------------
ARSITEKTUR = {
 "24060122140184": (8.5, "U-Net; section lengkap (deskripsi, bentuk data, arsitektur, diagram, penjelasan, input/output, referensi, alur). Solid & rapi."),
 "24060123120002": (9.3, "U-Net multimodal BraTS2020 (FLAIR+T1ce), one-hot 4 kelas, tensor (2,128,128)->(4,128,128); detail & lanjutan."),
 "24060123120009": (8.7, "U-Net lengkap, spesifikasi data jelas, split 80/10/10, referensi & parameter."),
 "24060123120010": (9.0, "Attention U-Net, laporan formal lengkap (cover, judul-deskripsi-data-komponen), referensi & parameter."),
 "24060123120023": (8.7, "Attention U-Net, penjelasan attention gate pada skip connection; lengkap & jelas."),
 "24060123120028": (9.2, "SegNet, tabel bentuk data & breakdown tensor rinci, pembahasan pooling indices/kelas; mendalam."),
 "24060123120029": (8.8, "U-Net, section A-F lengkap, penjelasan encoder/decoder & komponen baik."),
 "24060123120030": (9.0, "ResUNet++ (backbone ResNet-34), arsitektur hibrid lanjutan dgn justifikasi residual."),
 "24060123120032": (8.8, "U-Net format IEEE, deskripsi & spesifikasi data rinci, split 800/100/100, referensi."),
 "24060123120038": (8.8, "U-Net, konteks medis kuat (statistik mortalitas, inter-observer error), referensi & parameter."),
 "24060123120040": (9.0, "Modified U-Net + Channel & Spatial Attention, pendekatan dua tahap (Davar & Fevens 2024); lanjutan."),
 "24060123130058": (8.7, "U-Net + encoder VGG16 (transfer learning ImageNet), tabel bentuk data; baik."),
 "24060123130067": (8.8, "SegNet, prosa rinci dgn penjelasan pooling indices & efisiensi memori; kedalaman teknis baik (minim sitasi)."),
 "24060123130079": (8.9, "Attention U-Net, tabel data, skema augmentasi, referensi & parameter."),
 "24060123130080": (8.3, "U-Net, laporan formal, bahas sub-region (WT/TC/ET); relatif lebih singkat & minim sitasi."),
 "24060123130081": (9.2, "ResUNet (Residual U-Net), banyak sitasi (Ronneberger, Lebani dll), justifikasi residual kuat."),
 "24060123130084": (8.7, "U-Net, justifikasi pemilihan dgn dukungan literatur; lengkap."),
 "24060123130086": (8.6, "U-Net, deskripsi & bentuk data jelas, referensi; baik."),
 "24060123130093": (9.4, "TransUNet (CNN+Transformer), membahas varian hibrid (CrossTransUNet, Neuro-TransUNet); komprehensif & lanjutan."),
 "24060123130094": (8.6, "U-Net 2D, binary semantic segmentation, lengkap & jelas."),
 "24060123130098": (8.5, "U-Net, tabel tensor; lengkap (ada salah tulis label '2 bukan tumor')."),
 "24060123130100": (8.6, "U-Net, section I-III rapi, penjelasan contracting/expansive path."),
 "24060123130106": (9.5, "Modified U-Net, format jurnal (abstrak/kata kunci), reduksi 1 downsampling utk jaga detail, sitasi [1]-[5] & parameter; sangat baik."),
 "24060123130110": (8.9, "Attention U-Net, tabel parameter & tensor per batch rinci, referensi."),
 "24060123130112": (9.5, "U-Net (FCN+skip), makalah akademik lengkap (Pendahuluan/Metode), tabel breakdown tensor per tahap, banyak sitasi & parameter."),
 "24060123130114": (7.8, "U-Net, isi paling singkat & dangkal; section inti ada tapi minim elaborasi & sitasi."),
 "24060123130117": (9.0, "U-Net, tabel breakdown layer rinci, preprocessing Z-score & augmentasi (elastic deformation), parameter."),
 "24060123140045": (8.9, "U-Net dgn dataset nyata (LGG MRI Kaggle, Buda 2019), konteks data kuat, referensi & parameter."),
 "24060123140111": (9.5, "DeepLabV3+, format jurnal lengkap (DOI/ISSN), arsitektur lanjutan & pembahasan mendalam."),
 "24060123140142": (9.0, "ResU-Net + Residual Blocks + Attention Gates, tabel parameter, bahas class imbalance; lanjutan."),
 "24060123140148": (8.9, "U-Net FLAIR BraTS2020, penjelasan benchmark BraTS, detail & lengkap."),
 "24060123140150": (8.9, "Attention U-Net, alur task jelas, penjelasan attention gate baik, lengkap."),
 "24060123140151": (8.8, "Attention U-Net, notasi tensor formal, 5 komponen (encoder/bottleneck/attention/decoder/output), referensi."),
 "24060123140152": (8.6, "U-Net, tabel pembagian data rinci, penjelasan encoder/decoder; baik (minim sitasi eksplisit)."),
 "24060123140166": (9.0, "Attention U-Net utk glioma T1-Weighted, tabel spesifikasi sangat rinci (Z-score, augmentasi elastic), parameter."),
 "24060123140175": (9.0, "3D U-Net (multimodal T1/T1ce/T2/FLAIR, voxel-wise, patching); arsitektur lanjutan & pemahaman domain kuat."),
 "24060123140179": (9.3, "Attention U-Net, format jurnal (abstrak, BCE+Dice loss, target DSC>0.85), referensi & parameter; sangat baik."),
 "24060123140197": (9.0, "U-Net, output one-hot [N,2,256,256] + softmax, tabel spesifikasi & parameter, sitasi TCGA."),
 "24060123140201": (8.7, "Attention U-Net, section A-C lengkap, penjelasan attention gate; baik."),
 "24060123140204": (8.9, "Attention U-Net (Oktay et al. 2018), augmentasi (flip/rotasi/elastic), referensi; baik."),
 "24060123140211": (9.4, "TransUNet (ResNet50 + ViT 12-layer), format akademik dgn abstrak, patch tokenization; komprehensif & lanjutan."),
}

def fmt(v):
    return "" if v is None else f"{v:.2f}"

def oral_v(nim): return ORAL.get(nim, (None,))[0]
def arsi_v(nim): return ARSITEKTUR.get(nim, (None,))[0]

rows = sorted(ROSTER, key=lambda x: x[1].lower())

# ---- CSV utama ----
out_main = os.path.join(BASE, "penilaian-pola-2026.csv")
with open(out_main, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["NIM", "Nama",
                "Classification Task (Intermediate)",
                "Evaluation Metric Quiz",
                "Manual Classification Task (Beginner)",
                "Oral", "Arsitektur",
                "Proyek (Presentasi + Keaktifan)"])
    for nim, nama, ct, quiz, manual, proyekpk in rows:
        w.writerow([nim, nama, ct, quiz, manual,
                    fmt(oral_v(nim)), fmt(arsi_v(nim)), proyekpk])

# ---- CSV detail justifikasi (Oral & Arsitektur) ----
out_detail = os.path.join(BASE, "penilaian-pola-2026-detail.csv")
with open(out_detail, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["NIM", "Nama",
                "Oral", "Justifikasi Oral",
                "Arsitektur", "Justifikasi Arsitektur"])
    for nim, nama, *_ in rows:
        o = ORAL.get(nim, (None, "(tidak mengumpulkan)"))
        a = ARSITEKTUR.get(nim, (None, "(tidak mengumpulkan)"))
        w.writerow([nim, nama, fmt(o[0]), o[1], fmt(a[0]), a[1]])

# ---- verifikasi ----
nims = [r[0] for r in rows]
assert len(nims) == len(set(nims)), "Ada NIM duplikat!"
print(f"Total mahasiswa  : {len(rows)} (unik, tanpa duplikat)")
print(f"Punya nilai Oral : {sum(1 for r in rows if oral_v(r[0]) is not None)}")
print(f"Punya Arsitektur : {sum(1 for r in rows if arsi_v(r[0]) is not None)}")
print(f"Ditulis: {out_main}")
print(f"Ditulis: {out_detail}")
