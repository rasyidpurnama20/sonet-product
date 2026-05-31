# 🎵 Katalog Musik Game — *Garuda Emblem*

Katalog konsep musik (BGM/OST) untuk game **Garuda Emblem** karya **Team Batalion** — sebuah *2D hyper-comical beat 'em up* arcade (solo & co-op) berlatar kampus **UNION (University of Rungeon)**. Pemain berperan sebagai **Farid** & **Rani Griffith**, anggota UKM jurnalistik *Garuda Emblem*, yang melawan balik setelah Rektor menyebar sayembara atas mereka — kampus pun berubah jadi medan perang.

> Referensi game: [itch.io — Team Batalion](https://team-batalion.itch.io/garuda-emblem) · [Steam](https://store.steampowered.com/app/3773640/) · [SteamDB](https://steamdb.info/app/3533170/info/)
> *Catatan: info dunia/cerita diparafrasekan dari sumber resmi untuk kepatuhan lisensi. Seluruh konsep musik di bawah adalah karya orisinal sebagai panduan komposisi.*

---

## 📌 Cara pakai katalog

Setiap lagu memuat **6 field** untuk memandu komposer/sound designer:

| Field | Penjelasan |
|---|---|
| **Story/Mood** | Konteks naratif & suasana yang ingin dibangun |
| **Chord Progression** | Progresi akord utama + variasi chorus/section |
| **Struktur Lagu** | Susunan section (intro/verse/hook/bridge/loop) |
| **Instrumen** | Palet instrumen & sound utama |
| **Referensi Genre** | Game/artis/genre acuan untuk arah produksi |
| **Variasi Loop** | Varian dinamis (calm/combat/stinger) untuk implementasi in-game |

---

## 🗂️ Struktur file (10 file × 5 lagu = 50)

| File | Lagu | Tema |
|---|---|---|
| [`01-tracks-01-05.md`](01-tracks-01-05.md) | 01–05 | Core/UI & Naratif |
| `02-tracks-06-10.md` | 06–10 | Core/UI + Stage Fakultas (awal) |
| `03-tracks-11-15.md` | 11–15 | Stage Fakultas |
| `04-tracks-16-20.md` | 16–20 | Stage Fakultas + Boss (awal) |
| `05-tracks-21-25.md` | 21–25 | Boss Fakultas |
| `06-tracks-26-30.md` | 26–30 | Boss Fakultas + Mini-game (awal) |
| `07-tracks-31-35.md` | 31–35 | Mini-game + Cutscene (awal) |
| `08-tracks-36-40.md` | 36–40 | Cutscene & Emosional |
| `09-tracks-41-45.md` | 41–45 | Final Act / Arc Rektor |
| `10-tracks-46-50.md` | 46–50 | Co-op / Arcade & Bonus |

---

## 🎼 Daftar 50 Lagu (Index)

### Core/UI & Naratif
1. Garuda Emblem — Main Theme
2. Pick Your Fighter — Character Select
3. Newsroom HQ — Base Camp Garuda Emblem
4. Campus Roam — Free-Roam Map
5. Kantin Black Market — Shop / Upgrade
6. Scoop Secured — Victory Theme
7. Deadline Missed — Game Over
8. Print the Legend — Credits / Staff Roll

### Stage Fakultas
9. Fakultas Teknik — Workshop Warzone
10. Fakultas MIPA/Sains — Lab Chaos
11. Fakultas Hukum — Courtyard of Order
12. Fakultas Kedokteran — Anatomy Alley
13. Fakultas Ekonomi — Market Mayhem
14. Fakultas Ilmu Komputer — Server Room Riot
15. Fakultas Seni — Gallery Brawl
16. Fakultas Olahraga — Stadium Showdown
17. Fakultas Pertanian — Greenhouse Rumble
18. Campus Plaza — Open-Air Clash

### Boss
19. Mid-Boss — Senior Hazer
20. Boss Teknik — "The Foreman"
21. Boss MIPA — "Dr. Reaktor"
22. Boss Hukum — "The Prosecutor"
23. Boss Kedokteran — "Scalpel"
24. Boss Ekonomi — "The Broker"
25. Boss Ilkom — "Null Pointer"
26. Boss Seni — "Maestro"
27. Boss Olahraga — "The Captain"
28. Boss Pertanian — "Greenskeeper"

### Mini-Game
29. Mini-Game — Collecting Trash
30. Mini-Game — Kantin Food-Stall Rush
31. Mini-Game — Library Stealth
32. Mini-Game — Motorbike Chase
33. Mini-Game — Rhythm Mabar
34. Mini-Game — Photo Scoop (Jurnalis Quest)

### Cutscene & Emosional
35. Opening Prologue — How It Began
36. The Bounty Announced — Rising Tension
37. Fallen Comrade — Lament
38. Flashback — Before the Storm
39. Plot Twist — Betrayal Revealed
40. Quiet Night at HQ — Calm Interlude

### Final Act / Arc Rektor
41. Rector's Tower — Final Approach
42. Final Boss — Rektor (Phase 1)
43. Final Boss — Rektor (Phase 2: True Form)
44. Final Boss — Last Stand (Phase 3)
45. Dawn over UNION — Ending

### Co-op / Arcade & Bonus
46. Arcade Mode — Endless Brawl
47. Double Trouble — Co-op Theme (Farid & Rani)
48. Underground Fight Club — Secret Stage
49. Boss Rush — Gauntlet
50. New Game+ — Main Theme Reprise

---

## 🔧 Catatan teknis global

- **Format loop:** semua track combat di-desain *seamless loop*; sediakan titik *loop start* setelah intro.
- **Tempo combat:** umumnya 140–175 BPM untuk stage/boss; hub & cutscene 70–110 BPM.
- **Layering adaptif:** banyak track punya stem terpisah (drum/lead/pad) untuk transisi calm↔combat.
- **Stinger:** sediakan 2–4 bar untuk victory/level-up/boss-appear.
