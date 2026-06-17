# Panduan Transformasi Proposal AICS-Lab UNDIP — Versi Generik & Publik

| Atribut | Detail |
|---|---|
| **Jenis Dokumen** | Panduan Revisi Editorial & Struktural (Internal) |
| **Dasar Dokumen** | *Partnership Proposal: Development of the AI & Cybersecurity Laboratory — UNDIP × Positive Technologies (2026)* |
| **Tujuan** | Menghasilkan versi proposal yang *partner-agnostic*, aman secara hukum, dan siap distribusi publik |
| **Bahasa Panduan** | Bahasa Indonesia (teks pengganti dalam Bahasa Inggris, sesuai dokumen asli) |
| **Versi Panduan** | 2.0 |
| **Tanggal** | Juni 2026 |
| **Status** | Aktif — untuk diimplementasikan sebelum distribusi |

---

> **💡 CARA MENGGUNAKAN DOKUMEN INI**
>
> Dokumen ini adalah **panduan kerja editorial** bagi tim penyusun proposal AICS-Lab. Untuk setiap bagian proposal yang perlu direvisi, tersedia:
> - 🔴 **Teks Asli** — kutipan langsung dari dokumen sumber
> - ✅ **Teks Pengganti** — teks generik siap pakai
> - 📌 **Alasan** — mengapa perubahan ini penting
> - 🏷️ **Prioritas**: `KRITIS` `TINGGI` `SEDANG`
>
> **Mulai dari mana?** Gunakan [Matriks Ringkasan Perubahan](#8-matriks-ringkasan-perubahan) untuk melihat semua perubahan sekaligus, lalu kerjakan berurutan dari prioritas `KRITIS` → `TINGGI` → `SEDANG`.



---

## Daftar Isi

1. [Prinsip Dasar Generalisasi](#1-prinsip-dasar-generalisasi)
2. [Daftar Kata Kunci Berbahaya](#2-daftar-kata-kunci-berbahaya)
3. [Peta Perubahan — Cover & Halaman Judul](#3-peta-perubahan--cover--halaman-judul)
4. [Peta Perubahan — Endorsement Sheet](#4-peta-perubahan--endorsement-sheet)
5. [Peta Perubahan — Executive Summary](#5-peta-perubahan--executive-summary)
6. [Peta Perubahan — Section 1: Introduction](#6-peta-perubahan--section-1-introduction)
7. [Peta Perubahan — Section 2: The Parties and Partnership Scheme](#7-peta-perubahan--section-2-the-parties-and-partnership-scheme)
8. [Matriks Ringkasan Perubahan](#8-matriks-ringkasan-perubahan)
9. [Peta Perubahan — Section 3: Laboratory Concept](#9-peta-perubahan--section-3-laboratory-concept)
10. [Peta Perubahan — Section 4: Technical Specifications and Equipment](#10-peta-perubahan--section-4-technical-specifications-and-equipment)
11. [Peta Perubahan — Section 5: Academic Programmes](#11-peta-perubahan--section-5-academic-programmes)
12. [Peta Perubahan — Section 6: Budget and Investment](#12-peta-perubahan--section-6-budget-and-investment)
13. [Peta Perubahan — Section 7: Governance and KPIs](#13-peta-perubahan--section-7-governance-and-kpis)
14. [Peta Perubahan — Section 8: Risk Management *(Paling Sensitif)*](#14-peta-perubahan--section-8-risk-management-paling-sensitif)
15. [Peta Perubahan — Section 9 & 10: Timeline dan Closing](#15-peta-perubahan--section-9--10-timeline-dan-closing)
16. [Penanganan Gambar & Figur](#16-penanganan-gambar--figur)
17. [Arsitektur Dokumen Dua Lapis](#17-arsitektur-dokumen-dua-lapis)
18. [Template Generik: Deskripsi Mitra Ideal](#18-template-generik-deskripsi-mitra-ideal)
19. [Panduan Version Control Dokumen](#19-panduan-version-control-dokumen)
20. [Pembagian Peran & Tanggung Jawab](#20-pembagian-peran--tanggung-jawab)
21. [Glosarium Istilah Teknis](#21-glosarium-istilah-teknis)
22. [Checklist Validasi Pra-Distribusi](#22-checklist-validasi-pra-distribusi)
23. [Langkah Selanjutnya](#23-langkah-selanjutnya)

---


## 1. Prinsip Dasar Generalisasi

Proposal kerja sama strategis yang kuat harus bersifat ***partner-agnostic*** pada bagian-bagian yang bersirkulasi publik. Lima prinsip berikut menjadi acuan seluruh perubahan dalam panduan ini:

| # | Prinsip | Penerapan Konkret |
|---|---|---|
| 1 | **Deskripsikan kebutuhan, bukan produk mitra** | Tulis "platform SIEM enterprise" bukan "MaxPatrol SIEM" |
| 2 | **Tetapkan kriteria mitra ideal, bukan nama** | Tulis "mitra yang memiliki rekam jejak di NDR" bukan "Positive Technologies" |
| 3 | **Fokus pada kapabilitas fungsional, bukan merek dagang** | Tulis "platform cyber-range global" bukan "Standoff 365" |
| 4 | **Jaga netralitas geopolitik dalam narasi institusional** | Hapus sub-bab 8.2 dari versi publik sepenuhnya |
| 5 | **Pisahkan dokumen publik dari lampiran teknis terbatas** | Nama mitra spesifik hanya muncul di Lampiran Teknis (distribusi terbatas) |

---

## 2. Daftar Kata Kunci Berbahaya

Sebelum mendistribusikan proposal versi generik, lakukan *Find & Replace* atau pencarian manual untuk **seluruh kata kunci berikut**. Target: **0 kemunculan** di dokumen utama.

| # | Kata Kunci | Kemunculan di Dokumen Asli | Tindakan |
|---|---|---|---|
| 1 | `Positive Technologies` | ±18 kemunculan | Ganti / hapus |
| 2 | `MaxPatrol SIEM` | ±5 kemunculan | Ganti dengan "Enterprise SIEM platform" |
| 3 | `MaxPatrol VM` | ±5 kemunculan | Ganti dengan "Vulnerability Management solution" |
| 4 | `PT NAD` / `PT Network Attack Discovery` | ±5 kemunculan | Ganti dengan "Network Detection & Response (NDR) system" |
| 5 | `PT Sandbox` | ±5 kemunculan | Ganti dengan "Sandbox analysis platform" |
| 6 | `PT AF` / `PT Application Firewall` | ±5 kemunculan | Ganti dengan "Application Firewall solution" |
| 7 | `PT ISIM` | ±2 kemunculan | Ganti dengan "Industrial/OT security platform" |
| 8 | `Standoff 365` | ±8 kemunculan | Ganti dengan "the partner's global cyber-range platform" |
| 9 | `The Standoff` | ±2 kemunculan | Ganti dengan "the partner's cyber-range simulation event" |
| 10 | `Russian Federation` | ±5 kemunculan | Hapus dari dokumen utama |
| 11 | `sanctions` / `sanctions list` | ±3 kemunculan | Hapus dari dokumen utama |
| 12 | `geopolitical` | ±2 kemunculan | Hapus dari dokumen utama |
| 13 | `Pola Dwipa` *(konsultan arsitektur)* | ±1 kemunculan | Pertimbangkan untuk digeneralisasi jika perlu |

> ⚠️ **Perhatian:** Kata kunci yang dihapus dari *dokumen utama* tetap harus tercatat lengkap di **Lampiran Teknis** (lihat [Bagian 17](#17-arsitektur-dokumen-dua-lapis)).

---


## 3. Peta Perubahan — Cover & Halaman Judul

🏷️ **Prioritas: KRITIS**

| Elemen | 🔴 Teks Asli | ✅ Teks Pengganti |
|---|---|---|
| Subjudul kerjasama | *A Strategic Collaboration between Diponegoro University and **Positive Technologies (Russian Federation)*** | *A Strategic Collaboration between Diponegoro University and an International Cybersecurity Industry Partner* |
| Logo mitra | Logo Positive Technologies | Kosongkan dengan placeholder `[Partner Logo — to be inserted upon MoU finalization]` |
| Keterangan bawah cover | *Positive Technologies (Russian Federation) / Faculty of Science and Mathematics* | *Faculty of Science and Mathematics, Diponegoro University* |

📌 **Alasan:** Cover adalah bagian pertama yang dilihat dan paling sering difoto/disebar. Nama mitra tersanksi pada cover dapat langsung dikaitkan dengan UNDIP secara institusional di media.

---

## 4. Peta Perubahan — Endorsement Sheet

🏷️ **Prioritas: TINGGI**

| Elemen | 🔴 Teks Asli | ✅ Teks Pengganti |
|---|---|---|
| Kolom "Partner" | *Positive Technologies (Russian Federation)* | *[International Cybersecurity Industry Partner — to be formally identified in the Letter of Intent]* |
| Kolom "Period of Program" | *2026–2028* | Pertahankan — tidak mengandung nama perusahaan |
| Kolom "Indicative Investment" | *± IDR 45.1 billion (CAPEX)* | Pertahankan — tidak mengandung nama perusahaan |
| Tanda tangan | Semua kolom tanda tangan | Pertahankan — dokumen internal resmi |

📌 **Alasan:** Endorsement Sheet adalah dokumen internal berklasifikasi. Meskipun tidak bersirkulasi publik, nama mitra resmi sebaiknya hanya tercantum **setelah LoI ditandatangani**, bukan pada tahap proposal awal.

---

## 5. Peta Perubahan — Executive Summary

🏷️ **Prioritas: KRITIS** *(Bagian paling sering dibaca dan dikutip)*

### 5.1 Paragraf Pengenalan Mitra

🔴 **Teks Asli:**
> *"To guarantee world-class quality from its first day of operation, UNDIP is pursuing a strategic partnership with **Positive Technologies (Russian Federation)**, a leading cybersecurity company. The partner brings a portfolio of advanced solutions, including **MaxPatrol SIEM, MaxPatrol VM, PT Network Attack Discovery, PT Sandbox**, and **PT Application Firewall**, together with access to its global cyber-range through the **Standoff 365** platform."*

✅ **Teks Pengganti:**
> *"To guarantee world-class quality from its first day of operation, UNDIP is pursuing a strategic partnership with a leading international cybersecurity company. The selected partner brings a portfolio of advanced security solutions — encompassing Security Information and Event Management (SIEM), Vulnerability Management (VM), Network Attack Discovery, Sandboxing, and Application Firewall capabilities — together with access to a globally operated cyber-range platform for hands-on offensive and defensive training."*

📌 **Alasan:** Executive Summary adalah bagian yang paling sering dikutip dalam presentasi, siaran pers, dan pengajuan anggaran. Menyebut nama mitra tersanksi di sini berisiko paling besar terhadap reputasi institusional.

---

### 5.2 Daftar Key Highlights

| Poin Key Highlights | 🔴 Teks Asli | ✅ Teks Pengganti |
|---|---|---|
| Partner | *Positive Technologies (Russian Federation) — MaxPatrol SIEM/VM, PT NAD, PT Sandbox, PT AF, and the Standoff 365 cyber-range* | *An internationally recognized cybersecurity company providing enterprise SIEM/VM, network detection, sandboxing, and application firewall solutions, with access to a global cyber-range platform* |
| Scheme | *Staged and equal — LoI → MoU → MoA → Implementation Arrangement* | **Pertahankan** — tidak mengandung nama perusahaan |
| Status | *DED completed (June 2026); site preparation commenced 17 June 2026* | **Pertahankan** — tidak mengandung nama perusahaan |
| Impact | *Certified digital talent, flagship research, innovation down-streaming...* | **Pertahankan** — tidak mengandung nama perusahaan |

---


## 6. Peta Perubahan — Section 1: Introduction

### 6.1 Sub-bab 1.1 Background and Rationale

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Seluruh isi sub-bab ini menggunakan data nasional (BSSN, proyeksi talenta digital, pertumbuhan ekonomi digital) yang independen dari pilihan mitra. **Tidak ada perubahan diperlukan.**

---

### 6.2 Sub-bab 1.2 Objectives

🏷️ **Prioritas: TINGGI**

Hanya Poin 1 yang perlu direvisi:

🔴 **Teks Asli (Poin 1):**
> *"To establish a world-class AI and cybersecurity laboratory on the 7th floor of the FSM Central Laboratory Building **through strategic cooperation with Positive Technologies**."*

✅ **Teks Pengganti:**
> *"To establish a world-class AI and cybersecurity laboratory on the 7th floor of the FSM Central Laboratory Building through strategic cooperation with a qualified international industry partner."*

📌 Poin 2–5 tidak menyebut nama perusahaan — **pertahankan**.

---

### 6.3 Sub-bab 1.3 Expected Benefits

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Semua poin manfaat bersifat fungsional (untuk UNDIP/FSM, mahasiswa, mitra, bangsa). **Tidak ada perubahan diperlukan.**

---

### 6.4 Sub-bab 1.4 Legal and Policy Basis

🏷️ **Prioritas: SEDANG**

Tidak ada nama perusahaan, namun disarankan **menambahkan satu butir baru** untuk memperkuat dasar generalisasi:

✅ **Butir Tambahan (sisipkan setelah butir terakhir):**
> *"The framework for this partnership follows the principle of partner-neutrality in institutional procurement and cooperation, ensuring that no single vendor dependency compromises the academic integrity or operational continuity of the laboratory. Partner selection is subject to due diligence, legal review, and inter-ministerial clearance where applicable, prior to the formalization of any binding arrangement."*

---

## 7. Peta Perubahan — Section 2: The Parties and Partnership Scheme

### 7.1 Sub-bab 2.1 The Parties *(Perubahan Terbesar di Seluruh Dokumen)*

🏷️ **Prioritas: KRITIS**

🔴 **Teks Asli:**
> *"Positive Technologies (Russian Federation) is a leading cybersecurity company whose portfolio includes MaxPatrol SIEM, MaxPatrol VM (vulnerability management), PT Network Attack Discovery (PT NAD), PT Sandbox, PT Application Firewall (PT AF), and PT ISIM (industrial/OT security). The company also operates the global Standoff cyber-range and the Standoff 365 platform and maintains active cybersecurity education initiatives. (Corporate figures will be verified during due diligence in Phase 0.)"*

✅ **Teks Pengganti:**
> *"The Industry Partner is a qualified international cybersecurity company selected on the basis of the following criteria: (a) demonstrated expertise in enterprise-grade security solutions, including SIEM, vulnerability management, network detection and response, sandboxing, and application firewall technologies; (b) operation of, or access to, a globally scalable cyber-range platform enabling realistic offensive and defensive simulation exercises; (c) active cybersecurity education, certification, and Training of Trainers (ToT) programmes with verifiable outcomes; and (d) willingness to contribute technology, curriculum, and training capacity under an in-kind arrangement fully aligned with academic and public-interest objectives. The identity of the selected partner will be formalized in the Letter of Intent (LoI) and publicly disclosed at the MoU signing stage, following completion of due diligence."*

📌 **Alasan:** Pendekatan berbasis kriteria menunjukkan bahwa UNDIP memiliki standar seleksi yang jelas dan tidak sekadar menerima tawaran pertama yang datang. Ini memperkuat posisi institusional dan memberikan fleksibilitas jika mitra perlu diganti.

---

### 7.2 Sub-bab 2.2 Cooperation Scheme and Scope

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Seluruh 7 poin lingkup kerja sama bersifat fungsional. **Tidak ada perubahan diperlukan.**

---

### 7.3 Sub-bab 2.3 Contribution of the Parties — Tabel

🏷️ **Prioritas: TINGGI**

🔴 **Baris Asli:**

| Party | Form of Contribution | Indicative Share |
|---|---|---|
| Positive Technologies | Solution licenses (MaxPatrol SIEM/VM, PT NAD, PT Sandbox, PT AF), Standoff 365 cyber-range access, curriculum, ToT, certification (in-kind) | ±20% of CAPEX (in-kind) |

✅ **Baris Pengganti:**

| Party | Form of Contribution | Indicative Share |
|---|---|---|
| Industry Partner | Enterprise cybersecurity solution licenses (SIEM, VM, NDR, Sandbox, Application Firewall), global cyber-range platform access, curriculum modules, Training of Trainers (ToT), and professional certification programmes (in-kind contribution) | ±20% of CAPEX (in-kind) |

---


## 8. Matriks Ringkasan Perubahan

> Gunakan tabel ini sebagai **dashboard kerja**. Tandai kolom ✔ setelah selesai direvisi.

| # | Lokasi di Proposal | Jenis Perubahan | Prioritas | Selesai? |
|---|---|---|---|---|
| 1 | Cover — Subjudul kerjasama | Hapus nama mitra | 🔴 **KRITIS** | ☐ |
| 2 | Cover — Logo mitra | Ganti dengan placeholder | 🔴 **KRITIS** | ☐ |
| 3 | Cover — Keterangan bawah | Hapus nama mitra | 🔴 **KRITIS** | ☐ |
| 4 | Endorsement Sheet — Kolom "Partner" | Ganti dengan placeholder | 🟠 **TINGGI** | ☐ |
| 5 | Executive Summary — Paragraf mitra | Tulis ulang seluruh paragraf | 🔴 **KRITIS** | ☐ |
| 6 | Executive Summary — Key Highlights (Partner) | Ganti dengan deskripsi kapabilitas | 🔴 **KRITIS** | ☐ |
| 7 | Sec. 1.2 Objectives — Poin 1 | Hapus "with Positive Technologies" | 🟠 **TINGGI** | ☐ |
| 8 | Sec. 1.4 Legal Basis | Tambahkan butir partner-neutrality | 🟡 **SEDANG** | ☐ |
| 9 | Sec. 2.1 The Parties — Deskripsi mitra | Tulis ulang seluruhnya | 🔴 **KRITIS** | ☐ |
| 10 | Sec. 2.3 Tabel Kontribusi — Baris mitra | Ganti nama kolom Party | 🟠 **TINGGI** | ☐ |
| 11 | Sec. 3.3 Zoning — Zone 2 | Ganti "Standoff 365" → deskripsi platform | 🟡 **SEDANG** | ☐ |
| 12 | Sec. 4.2 Equipment List — Baris 10 | Ganti nama produk → kategori teknis | 🟠 **TINGGI** | ☐ |
| 13 | Sec. 4.3 Fit-out — Baris Software & Licenses | Ganti nama produk → kategori teknis | 🟠 **TINGGI** | ☐ |
| 14 | Sec. 5.1 Master's Programme — Deskripsi fitur | Hapus nama produk dan perusahaan | 🟡 **SEDANG** | ☐ |
| 15 | Sec. 5.2 Cyber-Range — CTF events | Ganti "The Standoff" → deskripsi umum | 🟡 **SEDANG** | ☐ |
| 16 | Sec. 6.1 CAPEX — Baris 5 | Ganti nama mitra | 🟠 **TINGGI** | ☐ |
| 17 | Sec. 8 Tabel Risiko — Baris 8 (Geopolitik) | Generalisasi atau hapus baris ini | 🟠 **TINGGI** | ☐ |
| 18 | Sec. 8.2 Geopolitical Considerations | **Hapus seluruh sub-bab** | 🔴 **KRITIS** | ☐ |
| 19 | Sec. 10 Closing — Kalimat penutup | Hapus nama mitra | 🟡 **SEDANG** | ☐ |
| 20 | Figure 1, 2, 3 — Caption gambar | Periksa dan revisi jika perlu | 🟡 **SEDANG** | ☐ |

**Legenda:** 🔴 KRITIS = Wajib sebelum distribusi apapun | 🟠 TINGGI = Wajib sebelum distribusi publik | 🟡 SEDANG = Disarankan untuk versi final

---


## 9. Peta Perubahan — Section 3: Laboratory Concept

### 9.1 Sub-bab 3.1 Vision and Positioning

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Visi dan positioning laboratorium bersifat universal. **Tidak ada perubahan diperlukan.**

---

### 9.2 Sub-bab 3.2 Location and Building Context

🏷️ **Perhatian: PERIKSA NAMA KONSULTAN**

Dokumen menyebut nama konsultan arsitektur: *"PT. Pola Dwipa"*. Nama ini bukan mitra strategis dan tidak berisiko, namun jika dokumen ditujukan untuk distribusi di luar UNDIP, **pertimbangkan untuk menggeneralisasi** menjadi *"the appointed architectural consultant"* agar dokumen tidak tampak sebagai referensi proyek internal.

---

### 9.3 Sub-bab 3.3 Functional Zoning — Zone 2

🏷️ **Prioritas: SEDANG**

🔴 **Teks Asli di Tabel:**
> *Cyber-Range and SOC: red/blue/purple team simulation, video wall, **Standoff 365 connection***

✅ **Teks Pengganti:**
> *Cyber-Range and SOC: red/blue/purple team simulation, video wall, connection to the partner's global cyber-range platform*

---

## 10. Peta Perubahan — Section 4: Technical Specifications and Equipment

### 10.1 Sub-bab 4.1 Technology Architecture

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Deskripsi arsitektur teknologi (compute, network, security, applications layers) bersifat generik. Tidak menyebut nama produk spesifik. **Tidak ada perubahan diperlukan.**

---

### 10.2 Sub-bab 4.2 Indicative Equipment List — Baris 10

🏷️ **Prioritas: TINGGI**

| No | Kategori | 🔴 Asli | ✅ Pengganti |
|---|---|---|---|
| 10 | Security Software | *MaxPatrol SIEM, MaxPatrol VM, PT NAD, PT Sandbox, PT AF; Standoff 365 access (academic license)* | *Enterprise SIEM platform, Vulnerability Management (VM) solution, Network Detection & Response (NDR) system, Sandbox analysis platform, Application Firewall; global cyber-range platform access (academic/partnership license)* |

📌 Baris 1–9 dan 11 bersifat generik berdasarkan spesifikasi teknis hardware. **Pertahankan.**

---

### 10.3 Sub-bab 4.3 Floor 7 Fit-out Requirements — Baris Software & Licenses

🏷️ **Prioritas: TINGGI**

| Kategori | 🔴 Asli | ✅ Pengganti |
|---|---|---|
| Software & licenses | *MaxPatrol SIEM/VM, PT NAD, PT Sandbox, PT AF, Standoff 365; AI/ML & MLOps tooling* | *Enterprise SIEM/VM, NDR, Sandbox analysis, and Application Firewall solutions; global cyber-range platform license; AI/ML frameworks and MLOps tooling* |

---

## 11. Peta Perubahan — Section 5: Academic Programmes

### 11.1 Sub-bab 5.1 Master's Programme

🏷️ **Prioritas: SEDANG**

🔴 **Teks Asli:**
> *"Its distinctive features are cyber-range-based learning **(Standoff 365)**, embedded professional certification, and **co-supervision with Positive Technologies experts**."*

✅ **Teks Pengganti:**
> *"Its distinctive features are cyber-range-based learning via the partner's globally operated simulation platform, embedded professional certification, and co-supervision with seasoned industry practitioners from the partner organisation."*

📌 Tabel kurikulum 39 SKS, daftar konsentrasi, dan rincian semester tidak menyebut nama perusahaan. **Pertahankan seluruhnya.**

---

### 11.2 Sub-bab 5.2 Training, Certification, Research, Community Engagement

🏷️ **Prioritas: SEDANG**

🔴 **Teks Asli:**
> *"Cyber-Range and Competitions: hosting and participation in **The Standoff** and national/international Capture-the-Flag (CTF) events."*

✅ **Teks Pengganti:**
> *"Cyber-Range and Competitions: hosting and participation in the partner's cyber-range simulation events and national/international Capture-the-Flag (CTF) competitions."*

📌 Poin lain (Education & Curriculum, Certification & Training, ToT, Collaborative Research, Down-streaming) tidak menyebut nama perusahaan. **Pertahankan.**

---


## 12. Peta Perubahan — Section 6: Budget and Investment

### 12.1 Sub-bab 6.1 CAPEX — Baris 5

🏷️ **Prioritas: TINGGI**

| No | 🔴 Komponen Asli | ✅ Komponen Pengganti | Sumber Dana |
|---|---|---|---|
| 5 | *Positive Technologies solutions, licenses & platform access — Rp 6,0 miliar* | *Industry partner cybersecurity solutions, licenses & cyber-range platform access — Rp 6,0 miliar* | Partner in-kind / academic license |

📌 Semua baris CAPEX lainnya (1–4, 6–8) tidak menyebut nama perusahaan. **Pertahankan.**

---

### 12.2 Sub-bab 6.2 OPEX dan 6.3 Funding Sources

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Kedua sub-bab menggunakan terminologi generik (RKAT, hibah, PNBP). **Tidak ada perubahan diperlukan.**

---

## 13. Peta Perubahan — Section 7: Governance and KPIs

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Sub-bab 7.1 (struktur tata kelola) dan 7.2 (tabel KPI) tidak menyebut nama perusahaan spesifik. **Tidak ada perubahan diperlukan.**

---

## 14. Peta Perubahan — Section 8: Risk Management *(Paling Sensitif)*

### 14.1 Tabel Risiko — Baris 8 (Risiko Geopolitik)

🏷️ **Prioritas: TINGGI**

🔴 **Baris Asli:**

| Risk | Category | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| *Geopolitical / international sanctions exposure* | Compliance | Medium | Medium | *Due diligence; prudent payment/procurement channels; focus on academic/in-kind scope; legal and inter-ministerial consultation* |

📌 **Rekomendasi:** Hapus baris ini dari dokumen utama. Keberadaannya secara implisit mengidentifikasi mitra dan mengakui risiko sanksi di depan publik. Pindahkan ke Lampiran Teknis.

✅ **Jika baris tetap dipertahankan** (digeneralisasi):

| Risk | Category | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| *International cooperation and regulatory compliance risk* | Compliance | Medium | Low | *Conduct legal review of all cooperation agreements under applicable Indonesian law; verify partner's legal standing in relevant jurisdictions; obtain inter-ministerial clearance where required prior to LoI finalization* |

---

### 14.2 Sub-bab 8.2 Compliance, Ethics, and Geopolitical Considerations

🏷️ **Prioritas: KRITIS — Hapus Seluruh Sub-bab**

🔴 **Isi Sub-bab Asli yang Harus Dihapus:**
> *"It is noted, factually and neutrally, that Positive Technologies has been placed on the sanctions lists of certain Western states since 2021. This cooperation is conducted under Indonesian national law, which does not apply those sanctions..."*

📌 **Mengapa wajib dihapus dari versi publik:**
- Merupakan pengakuan eksplisit atas eksposur sanksi yang tidak perlu dipublikasikan
- Teks "pembelaan" justru memperkuat persepsi bahwa risiko tersebut nyata dan serius
- Berpotensi dikutip oleh media, auditor, atau pihak ketiga sebagai bukti bahwa UNDIP *knowingly* bermitra dengan entitas bermasalah
- Tidak relevan dalam versi generik karena nama mitra sudah tidak disebutkan

✅ **Teks Pengganti untuk Sub-bab 8.2:**

> **8.2 Compliance, Ethics, and International Cooperation Standards**
>
> *The laboratory will operate under responsible-use principles, with a strictly defensive and educational orientation, in full compliance with Indonesian national law, including the Personal Data Protection (PDP) Law, AI ethics guidelines, and applicable information-security governance standards. All international cooperation arrangements will be reviewed by UNDIP's legal counsel and, where required, coordinated with relevant government ministries and agencies to ensure full regulatory compliance prior to formalization of any binding agreement.*

---


## 15. Peta Perubahan — Section 9 & 10: Timeline dan Closing

### 15.1 Section 9: Implementation Timeline

🏷️ **Prioritas: TIDAK ADA PERUBAHAN**

Tabel fase, milestone, dan jadwal kuartalan tidak menyebut nama mitra secara spesifik. **Tidak ada perubahan diperlukan.**

---

### 15.2 Section 10: Closing

🏷️ **Prioritas: SEDANG**

🔴 **Teks Asli:**
> *"By combining UNDIP's academic capacity with the world-class technological capabilities of **Positive Technologies**, the laboratory is positioned to become a national and regional reference..."*

✅ **Teks Pengganti:**
> *"By combining UNDIP's academic capacity with the world-class technological capabilities of its industry partner, the laboratory is positioned to become a national and regional reference for AI and cybersecurity education, research, and services."*

---

## 16. Penanganan Gambar & Figur

🏷️ **Prioritas: SEDANG** *(Bagian yang sering terlewatkan)*

Proposal asli memiliki **3 figur** yang perlu diperiksa teksnya:

| Figur | Caption Asli | Status | Tindakan |
|---|---|---|---|
| **Figure 1** | *"Proposed site of the AI & Cybersecurity Laboratory at the FSM Central Laboratory Building, Diponegoro University."* | ✅ Aman | Tidak ada perubahan |
| **Figure 2** | *"Building access and vertical circulation supporting the 7th-floor laboratory development."* | ✅ Aman | Tidak ada perubahan |
| **Figure 3** | *"AICS-Lab Technology Architecture"* | ✅ Aman | Tidak ada perubahan |

📌 **Periksa juga:** Apakah di dalam gambar (bukan hanya caption) terdapat teks, logo, atau watermark yang menyebut nama mitra? Jika dokumen dalam format `.pdf` atau `.docx`, zoom ke setiap gambar untuk memastikan tidak ada branding vendor yang tertanam di dalam grafik arsitektur teknologi (Figure 3 khususnya).

---

## 17. Arsitektur Dokumen Dua Lapis

Pendekatan profesional yang direkomendasikan adalah membagi proposal menjadi **dua dokumen terpisah** dengan tingkat distribusi yang berbeda:

```
┌────────────────────────────────────────────────────────────┐
│  LAPISAN 1: PROPOSAL UTAMA (Versi Generik / Publik)        │
│  Distribusi: Bebas                                          │
│  ✓ Pimpinan universitas                                    │
│  ✓ Kementerian / BSSN                                      │
│  ✓ Publikasi website / media                               │
│  ✓ Lampiran dokumen RKAT                                   │
│  ✓ Presentasi kepada mitra potensial lain                  │
└────────────────────────────────────────────────────────────┘
              ↓ dilengkapi oleh ↓
┌────────────────────────────────────────────────────────────┐
│  LAPISAN 2: LAMPIRAN TEKNIS (Confidential)                 │
│  Distribusi: Terbatas — Internal + Mitra Terpilih          │
│  ✓ Tim negosiasi UNDIP                                     │
│  ✓ Tim hukum / Biro Kerjasama                              │
│  ✓ Mitra (setelah LoI ditandatangani)                      │
│  ✓ Auditor internal (jika diperlukan)                      │
└────────────────────────────────────────────────────────────┘
```

### Isi Minimum Lampiran Teknis (Confidential)

| # | Komponen | Keterangan |
|---|---|---|
| 1 | Identitas lengkap mitra | Positive Technologies, Russian Federation; profil perusahaan |
| 2 | Daftar produk spesifik | MaxPatrol SIEM/VM, PT NAD, PT Sandbox, PT AF, PT ISIM, Standoff 365 |
| 3 | Hasil due diligence | Profil keuangan, rekam jejak, kapasitas delivery mitra |
| 4 | Legal opinion | Hasil review tim hukum UNDIP tentang status mitra dan implikasi hukum |
| 5 | Status regulasi mitra | Dokumentasi status sanksi, respons legal UNDIP, clearance Kemenlu |
| 6 | Klausul data sovereignty | Kepemilikan data riset, pembatasan akses pihak ketiga, lokasi server |
| 7 | Klausul kepemilikan IP | Hak paten, hak publikasi, bagi hasil komersialisasi riset bersama |
| 8 | Rincian lisensi software | Jenis lisensi, durasi, jumlah seat, ketentuan renewalnya |
| 9 | Dokumen LoI / MoU draft | Versi draft yang sedang dinegosiasikan |
| 10 | Rencana exit strategy | Prosedur jika mitra menarik diri atau kerja sama berakhir lebih awal |

**Keuntungan Arsitektur Dua Lapis:**
- Proposal utama tetap sah bersirkulasi tanpa membuka eksposur risiko geopolitik
- Detail teknis dan legal tetap terdokumentasi untuk akuntabilitas internal
- Jika mitra berubah di masa depan, hanya Lampiran Teknis yang perlu diperbarui — proposal utama tetap valid dan dapat digunakan kembali

---


## 18. Template Generik: Deskripsi Mitra Ideal

Teks berikut siap disalin langsung ke dalam proposal versi generik sebagai pengganti seluruh paragraf deskripsi mitra (Sub-bab 2.1):

---

> **The Industry Partner**
>
> The laboratory partner is a qualified international company specializing in enterprise cybersecurity solutions and education. Selection is based on the following criteria:
>
> **(a)** A proven track record in Security Information and Event Management (SIEM), Vulnerability Management (VM), Network Detection and Response (NDR), Sandbox Analysis, and Application Firewall technologies at enterprise scale;
>
> **(b)** Operation of, or formal access to, a globally accessible cyber-range platform enabling realistic red/blue/purple team simulation exercises relevant to current threat landscapes;
>
> **(c)** Established cybersecurity certification programmes and Training of Trainers (ToT) capabilities with verifiable delivery outcomes at the academic or professional level;
>
> **(d)** Legal standing in full accordance with Indonesian national law and the applicable regulations governing international cooperation of higher-education institutions (*Peraturan Menteri* on international cooperation of PTN); and
>
> **(e)** Commitment to knowledge transfer, curriculum co-development, and academic licensing arrangements on terms consistent with public-interest and national digital-sovereignty objectives.
>
> The identity of the selected partner will be disclosed in the Letter of Intent (LoI) and formally established in the Memorandum of Understanding (MoU) between the parties. Due diligence — encompassing technical assessment, financial verification, legal review, and inter-ministerial consultation where applicable — will be completed prior to finalization of the LoI.

---

> ⚠️ **Catatan Perbaikan dari Versi Sebelumnya:** Kalimat dalam poin (d) versi lama berbunyi *"legal standing in good accordance"* — ini tidak gramatikal dalam Bahasa Inggris formal. Versi di atas telah diperbaiki menjadi *"in full accordance"*.

---

## 19. Panduan Version Control Dokumen

Setiap versi proposal yang bersirkulasi harus memiliki **identifikasi versi yang jelas** untuk menghindari kebingungan antara versi asli dan versi generik.

### Konvensi Penamaan File

| Kondisi | Nama File yang Disarankan |
|---|---|
| Versi asli (dengan nama mitra) | `AICS-Lab-Proposal-v1.0-INTERNAL-CONFIDENTIAL.pdf` |
| Versi generik (tanpa nama mitra) | `AICS-Lab-Proposal-v2.0-PUBLIC.pdf` |
| Lampiran teknis | `AICS-Lab-Technical-Annex-v1.0-CONFIDENTIAL.pdf` |

### Header Dokumen yang Disarankan

Tambahkan blok informasi di halaman 2 (setelah cover) pada versi generik:

> | Atribut | Keterangan |
> |---|---|
> | **Nomor Dokumen** | FSM-UNDIP-AICS-2026-02 |
> | **Versi** | 2.0 (Generalized Public Version) |
> | **Menggantikan** | Versi 1.0 (June 2026, for internal review only) |
> | **Klasifikasi** | Public / Unrestricted |
> | **Disiapkan oleh** | Department of Informatics, FSM UNDIP |
> | **Disetujui oleh** | Dean of FSM / Vice-Rector for Research and Innovation |
> | **Tanggal Berlaku** | [Tanggal distribusi pertama] |

---

## 20. Pembagian Peran & Tanggung Jawab

Agar revisi ini dapat dieksekusi secara terstruktur, berikut pembagian kerja yang disarankan:

| Peran | Tanggung Jawab | Prioritas Pertama |
|---|---|---|
| **Editor Utama** (Sekretariat Dept. Informatika) | Melakukan *Find & Replace* seluruh kata kunci berbahaya (Bagian 2); merevisi teks sesuai panduan di Bagian 3–15 | Mulai dari Cover, Executive Summary, Sec. 2.1 |
| **Reviewer Teknis** (Dosen senior / Kaprodi) | Memvalidasi bahwa deskripsi kapabilitas teknis pengganti (SIEM, NDR, dll.) sudah akurat secara teknis | Sec. 4.2, 4.3, template Bagian 18 |
| **Reviewer Legal** (Tim Hukum UNDIP / Biro Kerjasama) | Memvalidasi teks Sec. 1.4 tambahan, pengganti Sec. 8.2, dan memastikan tidak ada implikasi hukum dari teks baru | Sec. 1.4, 8.2, template Bagian 18 poin (d) |
| **Penyusun Lampiran Teknis** (Tim negosiasi / Kaprodi) | Menyiapkan dokumen Lampiran Teknis Confidential sesuai daftar isi di Bagian 17 | Semua komponen Lampiran Teknis |
| **Validasi Akhir** (Dekan FSM / Wakil Rektor) | Menyetujui versi generik untuk distribusi; menandatangani dokumen versi final | Checklist Bagian 22 |

---

## 21. Glosarium Istilah Teknis

Untuk memudahkan pembaca non-teknis memahami istilah pengganti yang digunakan dalam versi generik:

| Istilah | Kepanjangan | Penjelasan Singkat |
|---|---|---|
| **SIEM** | Security Information and Event Management | Platform yang mengumpulkan dan menganalisis log keamanan secara real-time untuk mendeteksi ancaman |
| **VM** | Vulnerability Management | Sistem untuk mengidentifikasi, mengelola, dan memprioritaskan kerentanan di infrastruktur IT |
| **NDR** | Network Detection and Response | Solusi yang memonitor lalu lintas jaringan untuk mendeteksi serangan yang tidak terdeteksi oleh antivirus |
| **Sandbox** | Sandbox Analysis Platform | Lingkungan terisolasi untuk menganalisis file/program berbahaya tanpa risiko terhadap sistem utama |
| **SOC** | Security Operations Center | Pusat pemantauan dan respons insiden keamanan siber secara 24/7 |
| **WAF/AF** | Web/Application Firewall | Perisai keamanan yang memfilter dan memonitor lalu lintas HTTP ke aplikasi web |
| **Cyber-Range** | — | Lingkungan simulasi virtual untuk latihan serangan dan pertahanan siber secara realistis |
| **CTF** | Capture the Flag | Kompetisi keamanan siber di mana peserta memecahkan tantangan teknis untuk menemukan "flag" tersembunyi |
| **ToT** | Training of Trainers | Program melatih instruktur/dosen agar dapat mengajarkan kompetensi tertentu secara mandiri |
| **LoI** | Letter of Intent | Surat pernyataan niat awal untuk bekerja sama, bersifat non-binding |
| **MoU** | Memorandum of Understanding | Nota kesepahaman antar institusi, mengikat secara moral namun tidak selalu hukum |
| **MoA** | Memorandum of Agreement | Perjanjian yang lebih teknis dan mengikat, mengatur detail kerja sama |
| **CAPEX** | Capital Expenditure | Pengeluaran modal satu kali untuk aset tetap (infrastruktur, peralatan) |
| **OPEX** | Operating Expenditure | Biaya operasional rutin tahunan (listrik, lisensi, gaji, pemeliharaan) |
| **PNBP** | Penerimaan Negara Bukan Pajak | Pendapatan institusi PTN-BH dari layanan/penelitian (non-pajak) |
| **OT Security** | Operational Technology Security | Keamanan siber untuk sistem pengendalian industri (mesin, SCADA, IoT pabrik) |

---


## 22. Checklist Validasi Pra-Distribusi

Sebelum proposal versi generik didistribusikan, tim wajib menyelesaikan seluruh item berikut. Isi kolom **PJ** dan **Tanggal** saat setiap item selesai diverifikasi.

### A. Verifikasi Keyword (Find & Replace)

| # | Item Validasi | Target | PJ | Tanggal | ✔ |
|---|---|---|---|---|---|
| A1 | Cari `Positive Technologies` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A2 | Cari `MaxPatrol` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A3 | Cari `Standoff 365` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A4 | Cari `PT NAD` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A5 | Cari `PT Sandbox` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A6 | Cari `PT AF` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A7 | Cari `PT ISIM` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A8 | Cari `Russian Federation` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A9 | Cari `sanctions` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A10 | Cari `geopolitical` di seluruh dokumen | 0 kemunculan | | | ☐ |
| A11 | Cari `The Standoff` di seluruh dokumen | 0 kemunculan | | | ☐ |

### B. Verifikasi Konten

| # | Item Validasi | PJ | Tanggal | ✔ |
|---|---|---|---|---|
| B1 | Semua referensi mitra diganti dengan deskripsi fungsional generik | | | ☐ |
| B2 | Sub-bab 8.2 (Geopolitical Considerations) telah dihapus atau diganti sepenuhnya | | | ☐ |
| B3 | Baris risiko geopolitik di Tabel Sec. 8 telah dihapus atau digeneralisasi | | | ☐ |
| B4 | Teks pengganti telah divalidasi akurasinya secara teknis oleh reviewer teknis | | | ☐ |
| B5 | Butir tambahan di Sec. 1.4 (partner-neutrality) telah disisipkan | | | ☐ |
| B6 | Caption dan konten Figure 1, 2, 3 sudah diperiksa (tidak ada branding vendor) | | | ☐ |

### C. Verifikasi Hukum & Proses

| # | Item Validasi | PJ | Tanggal | ✔ |
|---|---|---|---|---|
| C1 | Legal review internal UNDIP telah memberikan clearance untuk konten versi generik | | | ☐ |
| C2 | Lampiran Teknis (Confidential) sudah disiapkan sebagai dokumen terpisah | | | ☐ |
| C3 | Dokumen versi generik telah diberi nomor dokumen dan versi (v2.0) | | | ☐ |
| C4 | File versi generik dinamai dengan konvensi yang benar (`...-PUBLIC.pdf`) | | | ☐ |
| C5 | Versi lama (v1.0 internal) telah ditarik dari sirkulasi atau diberi label SUPERSEDED | | | ☐ |

### D. Persetujuan Final

| # | Item Validasi | PJ | Tanggal | ✔ |
|---|---|---|---|---|
| D1 | Dekan FSM menyetujui versi generik untuk distribusi | | | ☐ |
| D2 | Wakil Rektor Riset & Inovasi menyetujui versi generik | | | ☐ |
| D3 | Biro Kerjasama UNDIP memvalidasi kesesuaian format dengan standar kerjasama internasional | | | ☐ |

---

## 23. Langkah Selanjutnya

Setelah panduan ini diterima, berikut urutan tindakan yang disarankan:

```
TAHAP 1 — Sebelum LoI Ditandatangani (Segera)
  ├── Distribusikan panduan ini ke Editor Utama dan Reviewer Legal
  ├── Mulai revisi proposal berdasarkan Matriks Ringkasan (Bagian 8)
  │   Urutan: KRITIS dulu → TINGGI → SEDANG
  └── Minta legal opinion resmi dari tim hukum UNDIP

TAHAP 2 — Paralel dengan Revisi (2–4 Minggu)
  ├── Susun Lampiran Teknis (Confidential) sesuai daftar isi Bagian 17
  ├── Konsultasi resmi dengan Kemenlu RI (sebelum LoI)
  └── Selesaikan due diligence terhadap mitra

TAHAP 3 — Sebelum Distribusi Pertama
  ├── Jalankan Checklist Validasi Pra-Distribusi (Bagian 22) secara lengkap
  ├── Dapatkan persetujuan Dekan & Wakil Rektor (kolom D)
  └── Distribusikan versi generik; arsipkan versi v1.0 sebagai CONFIDENTIAL

TAHAP 4 — Saat LoI Ditandatangani
  └── Update Lampiran Teknis dengan identitas mitra yang sudah dikonfirmasi
```

---

*Dokumen ini (v2.0) adalah panduan teknis-editorial internal untuk tim penyusun proposal AICS-Lab UNDIP. Penerapan seluruh perubahan yang diuraikan di atas menghasilkan proposal yang lebih kuat secara institusional, lebih aman secara hukum, lebih fleksibel secara strategis, dan siap didistribusikan kepada khalayak yang lebih luas.*

*Perbaikan dari versi sebelumnya (v1.0): penambahan Daftar Isi, Cara Menggunakan, Daftar Kata Kunci Berbahaya, pengecekan Figur, Arsitektur Dokumen Dua Lapis yang diperluas, perbaikan kesalahan bahasa Inggris di template mitra, Panduan Version Control, Pembagian Peran, Glosarium, dan Checklist yang diperluas dengan kolom PJ.*
