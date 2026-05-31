# Rubrik Penilaian Standar — Kuis IoT (Mat-D 2026)

> Dokumen ini menjadi acuan baku untuk mengoreksi dan menilai Kuis 1 dan Kuis 2.
> Skala penilaian: **0–100** untuk tiap kuis.

---

## Skala Huruf (Standar Undip)

| Nilai Angka | Huruf | Keterangan |
|-------------|-------|------------|
| 80 – 100 | A | Sangat Baik |
| 75 – 79 | AB | Baik Sekali |
| 70 – 74 | B | Baik |
| 65 – 69 | BC | Cukup Baik |
| 60 – 64 | C | Cukup |
| 55 – 59 | CD | Kurang Cukup |
| 45 – 54 | D | Kurang |
| < 45 | E | Sangat Kurang / Tidak Memenuhi |

---

## KUIS 1 — Refleksi Materi Pasca-UTS & Kaitan dengan Proyek

**Pertanyaan:** *"Ceritakan materi yang sudah kalian pelajari setelah UTS dan kaitkan dengan proyek kelompok kalian."*

Materi inti pasca-UTS yang menjadi acuan jawaban benar:
1. **Keamanan IoT** — prinsip data security (CIA: *Confidentiality*/kerahasiaan, *Integrity*/integritas, *Availability*/ketersediaan), perbedaan **data security vs data privacy**, jenis ancaman (phishing, DoS/DDoS, MITM, spoofing, ransomware, malware), serta strategi pertahanan (enkripsi, autentikasi, AI, blockchain).
2. **Arsitektur IoT** — model **3-layer** (Perception → Network → Application) atau **5-layer** (Objects/Perception, Object Abstraction, Service Management, Application, Business), beserta komponen (sensor, mikrokontroler, gateway, cloud).
3. **Organisasi & Bisnis IoT** — **Triple Layered Business Model Canvas (TLBMC)**: aspek **Ekonomi, Lingkungan, Sosial**; pihak yang terlibat & alur data.
4. **Kaitan dengan proyek kelompok** — relevansi materi terhadap produk IoT yang dirancang.

### Kriteria & Bobot Kuis 1

| Kode | Kriteria | Bobot | Deskripsi Penilaian |
|------|----------|:-----:|---------------------|
| K1 | **Keamanan IoT** | 25 | Menjelaskan prinsip CIA, perbedaan data security & data privacy, ancaman dan/atau strategi pertahanan. |
| K2 | **Arsitektur IoT** | 25 | Menyebut & menjelaskan layer arsitektur (3/5-layer) dan komponen penyusunnya secara tepat. |
| K3 | **Organisasi & Bisnis IoT** | 20 | Menjelaskan aspek ekonomi, lingkungan, sosial (TLBMC) dan/atau organisasi & pihak terkait. |
| K4 | **Kaitan dengan Proyek** | 20 | Mengaitkan materi secara spesifik & relevan dengan proyek kelompok. |
| K5 | **Kejelasan & Kelengkapan** | 10 | Struktur jawaban, kelengkapan cakupan, dan kejelasan penyampaian. |
| | **TOTAL** | **100** | |

### Pedoman Skoring per Kriteria (Kuis 1)

- **Lengkap & tepat** → 85–100% bobot (mis. K1: 22–25)
- **Sebagian besar benar, ada kekurangan minor** → 65–84% bobot
- **Disebut umum/dangkal atau ada miskonsepsi** → 40–64% bobot
- **Disinggung sangat sedikit** → 20–39% bobot
- **Tidak dibahas** → 0–19% bobot

---

## KUIS 2 — Desain Sistem Smart Home Energy Monitoring

**Pertanyaan:** *"Analisis/rancang penerapan sistem Smart Home Energy Monitoring berbasis IoT (ide, arsitektur, keamanan, dan aspek bisnis)."*

Acuan jawaban ideal:
1. **Ide/Konsep** — pemantauan & kontrol konsumsi listrik *real-time*, notifikasi/peringatan over-consumption, auto-off perangkat, hemat energi.
2. **Arsitektur** — **sensor arus/tegangan** → **mikrokontroler (ESP32/NodeMCU/ESP8266)** → **konektivitas (WiFi/MQTT)** → **cloud/server** → **aplikasi seluler**; idealnya dipetakan ke layer (Perception/Network/Application) dengan alur input–proses–output.
3. **Keamanan** — autentikasi pengguna (password/biometrik/OTP), enkripsi (HTTPS/TLS/MQTT), prinsip CIA, kontrol akses, device ID unik.
4. **Aspek Bisnis** — target pasar/segmen, model bisnis/revenue (penjualan perangkat, langganan premium, kemitraan PLN/developer), Business Model Canvas / TLBMC.

### Kriteria & Bobot Kuis 2

| Kode | Kriteria | Bobot | Deskripsi Penilaian |
|------|----------|:-----:|---------------------|
| D1 | **Ide / Konsep** | 20 | Kejelasan ide, kebermanfaatan, relevansi dengan tema *energy monitoring*, orisinalitas. |
| D2 | **Arsitektur** | 30 | Ketepatan sensor, mikrokontroler, konektivitas, cloud, aplikasi; pemetaan layer & alur data. |
| D3 | **Keamanan** | 20 | Mekanisme keamanan yang relevan & benar (autentikasi, enkripsi, CIA, kontrol akses). |
| D4 | **Aspek Bisnis** | 20 | Target pasar, model bisnis/revenue, mitra, BMC/TLBMC. |
| D5 | **Kejelasan & Kelengkapan** | 10 | Kelengkapan keempat aspek serta struktur & kejelasan. |
| | **TOTAL** | **100** | |

### Pedoman Skoring per Kriteria (Kuis 2)

- **Lengkap, konkret, dan tepat** → 85–100% bobot
- **Cukup lengkap dengan kekurangan minor** → 65–84% bobot
- **Umum/dangkal atau ada miskonsepsi** → 40–64% bobot
- **Disinggung sangat sedikit / keliru fokus** → 20–39% bobot
- **Tidak dibahas / di luar tema** → 0–19% bobot

> **Catatan tema Kuis 2:** Jawaban yang menyimpang dari tema *energy monitoring* (mis. smart door lock, kursi anti-ngantuk, deteksi kebisingan) dikenai pengurangan pada D1 (relevansi ide) meskipun aspek lain dijelaskan baik.

---

## Catatan Umum Koreksi

- **Banyak typo/salah ketik** ditemukan pada hampir semua jawaban; tidak diberi penalti khusus selama maksud tetap jelas, tetapi memengaruhi K5/D5 jika mengganggu pemahaman.
- **Miskonsepsi yang sering muncul:**
  - Menukar definisi layer (mis. menyebut *application layer* = rumah/sensor, atau *perception layer* = mengolah data).
  - Menyebut "keterbatasan" alih-alih "kerahasiaan/confidentiality" pada prinsip CIA.
  - Menganggap ancaman (MITM, firmware tampering) sebagai "metode keamanan".
  - Mencampur konsep AI dan IoT tanpa kaitan arsitektur yang jelas.
- **Aspek yang paling sering hilang:** prinsip keamanan (CIA) pada Kuis 1, dan bagian **Keamanan** pada Kuis 2.
