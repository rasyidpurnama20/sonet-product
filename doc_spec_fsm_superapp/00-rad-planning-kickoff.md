# 📐 FSM UNDIP Super Apps — Dokumen Kickoff Rapid Application Development (RAD)

> **Jenis Dokumen:** Master Planning Document (Living Document)
> **Metodologi:** Rapid Application Development (RAD) — 4 Fase Klasik
> **Versi:** 0.1 — Mei 2026
> **Status:** 🟡 Draft Awal — siap untuk diskusi & validasi stakeholder
> **PIC Dokumen:** Tim Pengembangan Super Apps FSM UNDIP

---

## 🎯 1. Tujuan Dokumen

Dokumen ini adalah **titik awal (kickoff)** perencanaan pengembangan FSM UNDIP Super Apps menggunakan pendekatan **Rapid Application Development (RAD)**. Dokumen ini bertujuan untuk:

1. Menyamakan persepsi seluruh stakeholder mengenai ruang lingkup, target, dan pendekatan pengembangan.
2. Menetapkan kerangka kerja RAD yang akan diikuti dalam siklus pengembangan.
3. Mendefinisikan deliverables, timeline, dan kriteria sukses untuk setiap fase.
4. Menjadi rujukan utama untuk dokumen-dokumen turunan (spec teknis, ERD, wireframe, test plan, dsb).

> 📎 **Dokumen ini melengkapi** analisis strategis yang sudah ada di folder `fsm-superapp/` (SWOT, RACI, FMEA, RICE), dan mengubah hasil analisis tersebut menjadi rencana eksekusi yang konkret.

---

## 🚀 2. Mengapa RAD?

Pendekatan **Rapid Application Development** dipilih untuk FSM Super Apps karena karakteristik proyek ini sangat sesuai dengan kekuatan RAD:

| Karakteristik Proyek | Kesesuaian dengan RAD |
|---|---|
| Stakeholder beragam (mahasiswa, dosen, tendik, laboran, pimpinan) | ✅ RAD menekankan keterlibatan pengguna sejak awal |
| Kebutuhan masih akan banyak berkembang seiring adopsi | ✅ RAD iteratif & adaptif terhadap perubahan |
| Butuh quick wins agar adopsi terjaga | ✅ RAD menghasilkan prototipe fungsional dengan cepat |
| Resource pengembang terbatas (potensi mahasiswa/dosen) | ✅ RAD memprioritaskan reuse komponen & low-code tooling |
| Risiko proyek terhenti jika tidak ada hasil terlihat | ✅ RAD memberikan output visual setiap iterasi |

### 🔑 Prinsip RAD yang Kami Anut
1. **User-centric:** Pengguna akhir terlibat di setiap iterasi, bukan hanya saat UAT.
2. **Iterative prototyping:** Bangun → demo → revisi → bangun lagi, dalam siklus 1–2 minggu.
3. **Time-boxed:** Setiap fase punya batas waktu jelas; scope yang menyesuaikan, bukan deadline.
4. **Reuse over reinvent:** Manfaatkan komponen, framework, dan layanan yang sudah ada.
5. **Working software over comprehensive documentation:** Dokumen seperlunya, kode yang jalan diutamakan.

---

## 🧭 3. Empat Fase RAD untuk FSM Super Apps

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 1. Requirement│ ──▶ │ 2. User      │ ──▶ │ 3. Rapid     │ ──▶ │ 4. Cutover & │
│   Planning   │     │   Design     │     │ Construction │     │  Transition  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
   ~2 minggu          ~3–4 minggu          ~6–10 minggu          ~2 minggu
```

### Fase 1 — Requirement Planning (Perencanaan Kebutuhan)
**Tujuan:** Menyepakati ruang lingkup, prioritas modul, dan kriteria sukses bersama stakeholder kunci.

**Kegiatan utama:**
- Workshop JAD (Joint Application Design) bersama WD II, admin, laboran, perwakilan teknisi & mahasiswa
- Validasi prioritas modul berdasarkan analisis RICE yang sudah ada
- Definisi MVP (Minimum Viable Product) yang akan dibangun di iterasi pertama
- Penetapan KPI proyek (lihat bagian 8)

**Deliverables:**
- ✅ Daftar fitur MVP final dengan tanda tangan WD II
- ✅ User stories prioritas tinggi (format: As a … I want … so that …)
- ✅ Kriteria penerimaan (Acceptance Criteria) tiap user story
- ✅ Daftar stakeholder + matriks komunikasi

**Durasi target:** 2 minggu

---

### Fase 2 — User Design (Desain Bersama Pengguna)
**Tujuan:** Membuat rancangan sistem yang sudah divalidasi pengguna sebelum coding besar dimulai.

**Kegiatan utama:**
- Pembuatan wireframe low-fidelity (Figma / Whimsical) untuk setiap user story
- Co-design session: tunjukkan wireframe ke pengguna asli, revisi langsung
- Penyusunan ERD (Entity Relationship Diagram) awal
- Penyusunan kontrak API (OpenAPI/Swagger) untuk endpoint MVP
- Pemilihan tech stack final (lihat bagian 6)

**Deliverables:**
- ✅ Wireframe & mockup high-fidelity untuk MVP
- ✅ ERD versi 1.0 + data dictionary singkat
- ✅ OpenAPI spec untuk endpoint MVP
- ✅ Decision Log: pilihan teknologi + alasan

**Durasi target:** 3–4 minggu (overlap dengan akhir Fase 1)

---

### Fase 3 — Rapid Construction (Konstruksi Cepat)
**Tujuan:** Mengembangkan sistem secara iteratif dalam sprint pendek dengan demo rutin.

**Kegiatan utama:**
- Sprint 1–2 minggu, masing-masing diakhiri demo ke stakeholder
- Pengembangan paralel: backend, frontend, mobile (jika ada), data migration
- Continuous integration (CI) dari hari pertama
- User testing rutin di setiap akhir sprint
- Penyiapan environment staging untuk uji coba pengguna pilot

**Deliverables per sprint:**
- ✅ Build aplikasi yang berjalan di staging
- ✅ Demo video / sesi demo live
- ✅ Sprint report (apa yang selesai, blocker, rencana sprint berikutnya)
- ✅ Test report (unit + integration)

**Durasi target:** 6–10 minggu (3–5 sprint)

---

### Fase 4 — Cutover & Transition (Peluncuran & Transisi)
**Tujuan:** Memastikan transisi mulus dari sistem lama (manual) ke Super Apps, dengan adopsi terukur.

**Kegiatan utama:**
- Migrasi data master (ruangan, aset, pengguna) dari sumber lama
- Pelatihan pengguna (training-the-trainer + sesi langsung)
- Pilot launch di 1 gedung / 1 prodi → evaluasi → scale
- Hypercare period: standby tim 2 minggu pasca go-live
- Dokumentasi user manual & SOP digital

**Deliverables:**
- ✅ Aplikasi production yang stabil
- ✅ User manual (PDF + video singkat)
- ✅ SOP penggunaan resmi (ditandatangani WD II)
- ✅ Laporan adopsi 30 hari pertama

**Durasi target:** 2 minggu (pilot) + 1 bulan hypercare

---

## 📦 4. Ruang Lingkup Iterasi Pertama (MVP)

Berdasarkan analisis RICE pada dokumen `fsm-superapp/01-maintenance-ticketing.md` dan `02-asset-management.md`, **MVP iterasi pertama** difokuskan pada fitur paling strategis:

### MVP — Modul 1: Maintenance Ticketing System
| Fitur | Justifikasi |
|---|---|
| Form lapor kerusakan + upload foto | RICE 7.200 — quick win paling terasa |
| Status tracking tiket | RICE 5.700 — fondasi transparansi |
| Notifikasi WhatsApp/email | RICE 3.600 — aksesibilitas tanpa install app |
| Penugasan teknisi (manual oleh admin) | Operasional dasar penyelesaian tiket |
| Riwayat tiket per pengguna | Audit trail minimum |

### MVP — Modul 2: Asset Management System
| Fitur | Justifikasi |
|---|---|
| Database aset digital + QR code | RICE 270–285 — fondasi seluruh modul aset |
| Status & lokasi aset | RICE 180–285 — operasional dasar |
| Mutasi/peminjaman aset | RICE 180 — kebutuhan harian laboran |

### Modul 3 & 4 (Room Booking, Task Management)
Akan masuk **iterasi 2** setelah MVP modul 1 & 2 stabil (proyeksi bulan ke-4).

> **Asumsi tetap fleksibel** — prioritas final ditentukan di workshop JAD Fase 1.

---

## 👥 5. Tim & Peran (Squad RAD)

| Peran | Jumlah | Tanggung Jawab Utama |
|---|---|---|
| **Project Sponsor** | 1 | WD II — keputusan strategis, unblock politik |
| **Product Owner** | 1 | Admin Fakultas senior — kelola backlog, prioritisasi |
| **Tech Lead / Solution Architect** | 1 | Desain teknis, code review, decision teknologi |
| **Backend Developer** | 1–2 | API, database, integrasi |
| **Frontend Developer** | 1–2 | Web app (mobile-responsive) |
| **UI/UX Designer** | 1 | Wireframe, prototype, user testing |
| **QA / Tester** | 1 | Test plan, automation, UAT coordination |
| **Data Migration Specialist** | 1 (parsial) | ETL data master ke sistem baru |
| **Change Management Lead** | 1 | Sosialisasi, pelatihan, adopsi |
| **DevOps / SRE** | 1 (parsial) | CI/CD, infra, monitoring |

> Untuk fase awal, satu orang bisa merangkap beberapa peran. Tim minimum yang viable: **5 orang inti**.

---

## 🛠️ 6. Tech Stack — Kandidat Awal

> Pilihan final akan dikonfirmasi di Fase 2 (User Design) bersama Tech Lead.

| Lapisan | Kandidat Utama | Alasan |
|---|---|---|
| Frontend Web | Next.js (React) + TailwindCSS | Mobile-responsive, ekosistem matang, ramah dev junior |
| Backend API | NestJS (Node.js) atau Laravel (PHP) | Cepat dibangun, banyak resource lokal |
| Database | PostgreSQL | Open-source, andal, fitur lengkap |
| File Storage | S3-compatible (MinIO atau cloud) | Untuk foto aset, foto kerusakan |
| Notifikasi | WhatsApp Business API + SMTP | Sesuai rekomendasi modul ticketing |
| Auth | SSO UNDIP (jika tersedia) + OAuth fallback | Single source of identity |
| Hosting | On-premise UNDIP atau cloud nasional | Kepatuhan kebijakan kampus |
| Monitoring | Grafana + Prometheus / Sentry | Observability dari hari 1 |
| CI/CD | GitHub Actions atau GitLab CI | Standar industri, gratis untuk open-source |

---

## 📅 7. Timeline Indikatif (Fase 1–4)

```
Bulan ke-:   1    2    3    4    5    6
            ┌────┐
Fase 1:     │ RP │
            └────┴────┐
Fase 2:          │ UD │
                 └────┴──────────────┐
Fase 3:                │  Construction│
                       └──────────────┴────┐
Fase 4:                              │ C&T │
                                     └─────┘
                                     ▲
                                     │
                                Pilot → Go-Live
```

**Target Go-Live MVP:** Bulan ke-5 sejak kickoff resmi.

---

## 📊 8. KPI Proyek

### KPI Pengembangan
| KPI | Target |
|---|---|
| Sprint velocity stabil | ≥ 80% komitmen sprint terselesaikan |
| Defect rate post-sprint | < 5 critical bugs / sprint |
| Test coverage | ≥ 60% untuk modul backend |
| Lead time fitur (idea → staging) | < 2 minggu |

### KPI Adopsi (30 hari pasca go-live)
| KPI | Target |
|---|---|
| Tiket masuk via sistem | ≥ 50 tiket/minggu |
| Pengguna aktif unik | ≥ 500 orang |
| Rasio tiket yang ditutup dengan rating | ≥ 70% |
| NPS pengguna pilot | ≥ +30 |
| Tingkat error sistem | < 1% transaksi |

---

## 🛡️ 9. Risiko & Mitigasi (Ringkasan)

> Risiko detail per modul tersedia di analisis FMEA pada folder `fsm-superapp/`.

| Risiko | Probabilitas | Dampak | Mitigasi Utama |
|---|---|---|---|
| Resistensi adopsi pengguna | Tinggi | Tinggi | Change management lead + quick wins di MVP |
| Data master tidak siap saat go-live | Tinggi | Tinggi | Data sprint paralel sejak Fase 2 |
| Pergantian pimpinan saat proyek berjalan | Sedang | Tinggi | Institusionalisasi via SK + dokumentasi lengkap |
| Tech debt menumpuk karena RAD cepat | Sedang | Sedang | Refactoring sprint setiap 4 sprint sekali |
| Vendor/dev keluar di tengah proyek | Sedang | Tinggi | Kode di repo institusi + dokumentasi onboarding |
| Skope kreep antar fase | Tinggi | Sedang | Strict change control board mulai Fase 3 |

---

## 🔗 10. Hubungan dengan Dokumen Lain

| Dokumen | Lokasi | Hubungan |
|---|---|---|
| Master Feature Map | `fsm-superapp/00-overview.md` | Sumber prioritas modul & fitur |
| Analisis Modul Ticketing | `fsm-superapp/01-maintenance-ticketing.md` | Detail SWOT/RACI/FMEA/RICE Modul 1 |
| Analisis Modul Aset | `fsm-superapp/02-asset-management.md` | Detail SWOT/RACI/FMEA/RICE Modul 2 |
| Analisis Modul Booking | `fsm-superapp/03-room-lab-booking.md` | Untuk iterasi 2 |
| Analisis Modul Task | `fsm-superapp/04-task-management.md` | Untuk iterasi 2 |
| Roadmap Strategis | `fsm-superapp/05-roadmap-next-steps.md` | Konteks jangka panjang |

### Dokumen Turunan yang Akan Dibuat (Roadmap Dokumen)
- `01-user-stories-mvp.md` — Daftar lengkap user stories MVP dengan acceptance criteria
- `02-erd-and-data-dictionary.md` — Model data MVP
- `03-api-contract-mvp.md` — Spesifikasi REST API (OpenAPI)
- `04-wireframe-and-prototype.md` — Link prototype Figma + catatan desain
- `05-sprint-plan.md` — Breakdown sprint Fase 3
- `06-test-strategy.md` — Strategi pengujian end-to-end
- `07-deployment-and-runbook.md` — Panduan deploy & operasional
- `08-change-management-plan.md` — Strategi sosialisasi & pelatihan

---

## ✅ 11. Definition of Done (DoD) Tingkat Proyek

Sebuah fitur/modul dianggap **selesai** ketika seluruh kriteria berikut terpenuhi:

- [ ] Kode di-merge ke branch utama dan lulus CI
- [ ] Unit test ditulis dan coverage memenuhi target
- [ ] API terdokumentasi di OpenAPI spec
- [ ] UI sudah responsive (desktop + mobile browser)
- [ ] Sudah dilakukan UAT oleh minimal 2 pengguna asli (bukan tim dev)
- [ ] Tidak ada critical/high bug terbuka
- [ ] Audit log tercatat untuk setiap aksi penting
- [ ] Sudah dideploy ke environment staging dan didemo
- [ ] User manual / tooltip in-app sudah tersedia

---

## 📝 12. Langkah Berikutnya (Action Items)

| # | Action | PIC | Target |
|---|---|---|---|
| 1 | Validasi dokumen ini bersama WD II | Product Owner | +1 minggu |
| 2 | Jadwalkan workshop JAD Fase 1 | Product Owner | +2 minggu |
| 3 | Bentuk squad inti (5 orang minimum) | WD II + PO | +2 minggu |
| 4 | Setup repository & tooling kolaborasi (Git, Jira/Trello, Slack/WA group) | Tech Lead | +1 minggu |
| 5 | Susun draft user stories MVP berdasarkan dokumen ini | Product Owner | +3 minggu |
| 6 | Mulai data audit untuk persiapan migrasi | Data Specialist | Paralel sejak +2 minggu |

---

## 🧾 13. Catatan Versi

| Versi | Tanggal | Penulis | Perubahan |
|---|---|---|---|
| 0.1 | Mei 2026 | Tim Pengembangan FSM Super Apps | Versi awal — draft kickoff |

---

> 💬 **Ini adalah living document.** Setiap keputusan strategis baru wajib diperbarui di sini agar seluruh tim tetap satu pemahaman. Pertanyaan, saran, dan revisi dapat diajukan melalui kanal komunikasi resmi proyek.

*— Disusun untuk mendukung visi FSM UNDIP sebagai pelopor smart faculty di lingkungan Universitas Diponegoro.*
