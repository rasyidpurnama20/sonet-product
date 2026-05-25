#!/usr/bin/env python3
"""
Website Content & Topic Checker — FSM UNDIP
============================================
Mengecek dua hal utama:
1. Kelengkapan menu: apakah setiap halaman menu memiliki konten yang tidak kosong
2. Topic coverage: apakah website/berita memuat 7 topik informasi penting
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin, urlparse
import re
import time

# ─────────────────────────────────────────────
# KONFIGURASI
# ─────────────────────────────────────────────

WEBSITES = [
    {"url": "https://fsm.undip.ac.id/",     "nama": "Fakultas Sains dan Matematika", "short": "FSM"},
    {"url": "https://math.undip.ac.id/",    "nama": "Departemen Matematika",          "short": "MATH"},
    {"url": "https://bio.undip.ac.id/",     "nama": "Departemen Biologi",             "short": "BIO"},
    {"url": "https://fisika.undip.ac.id/",  "nama": "Departemen Fisika",              "short": "FISIKA"},
    {"url": "https://kimia.undip.ac.id/",   "nama": "Departemen Kimia",               "short": "KIMIA"},
    {"url": "https://stat.undip.ac.id/",    "nama": "Departemen Statistika",          "short": "STAT"},
    {"url": "https://if.undip.ac.id/",      "nama": "Departemen Informatika",         "short": "IF"},
    {"url": "https://biotek.undip.ac.id/",  "nama": "Departemen Bioteknologi",        "short": "BIOTEK"},
]

# 7 Topik wajib beserta kata kunci (regex pattern, case-insensitive)
TOPICS = {
    "Prospek Kerja Lulusan": [
        r"prospek\s+kerja", r"karir", r"lapangan\s+kerja", r"profil\s+lulusan",
        r"alumni\s+bekerja", r"career", r"pekerjaan\s+lulusan", r"peluang\s+kerja",
        r"profesi", r"industri\s+mitra"
    ],
    "Alumni": [
        r"\balumni\b", r"lulusan", r"tracer\s+study", r"ikatan\s+alumni",
        r"alumni\s+undip", r"himpunan\s+alumni", r"purna\s+siswa"
    ],
    "Kurikulum": [
        r"kurikulum", r"mata\s+kuliah", r"\bmatkul\b", r"silabus",
        r"rencana\s+studi", r"\bsks\b", r"curriculum", r"rps",
        r"struktur\s+program", r"capaian\s+pembelajaran"
    ],
    "Pendaftaran": [
        r"pendaftaran", r"\bdaftar\b", r"seleksi", r"\bsnbt\b", r"\butbk\b",
        r"\bsbmptn\b", r"\bpmb\b", r"penerimaan\s+mahasiswa",
        r"jalur\s+masuk", r"registrasi", r"admisi"
    ],
    "Fasilitas": [
        r"fasilitas", r"laboratorium", r"\blab\b", r"perpustakaan",
        r"\bgedung\b", r"sarana", r"prasarana", r"ruang\s+kuliah",
        r"studio", r"workshop", r"peralatan"
    ],
    "Prestasi": [
        r"prestasi", r"penghargaan", r"\baward\b", r"\bjuara\b",
        r"\blomba\b", r"kompetisi", r"achievement", r"medali",
        r"terbaik", r"unggulan", r"mahasiswa\s+berprestasi"
    ],
    "Riset & Pengabdian": [
        r"\briset\b", r"penelitian", r"pengabdian", r"publikasi",
        r"\bjurnal\b", r"\bresearch\b", r"\bpkm\b", r"\babdimas\b",
        r"hibah", r"seminar\s+nasional", r"konferensi"
    ],
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

MIN_CONTENT_LENGTH = 200   # karakter teks bersih agar dianggap "terisi"
REQUEST_DELAY      = 1.0   # detik antar request
TIMEOUT            = 15    # detik timeout per request


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def fetch(url, timeout=TIMEOUT, verify=True):
    """Fetch URL, return (response, BeautifulSoup) atau (None, None)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, verify=verify)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        return resp, soup
    except requests.exceptions.SSLError:
        return fetch(url, timeout=timeout, verify=False)
    except Exception as e:
        print(f"    [WARN] Gagal fetch {url}: {e}")
        return None, None


def clean_text(soup):
    """Ekstrak teks bersih dari soup (buang script/style)."""
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()
    return " ".join(soup.get_text(separator=" ").split())


def check_topic_in_text(text, patterns):
    """Return True jika salah satu pattern ditemukan dalam text."""
    text_lower = text.lower()
    for p in patterns:
        if re.search(p, text_lower):
            return True
    return False


def get_menu_items(soup, base_url):
    """
    Ekstrak item menu navigasi utama dari soup.
    Return list of dict: {"label": str, "url": str}
    """
    menus = []
    seen_urls = set()
    base_domain = urlparse(base_url).netloc

    # Prioritas: tag <nav>, lalu elemen dengan class/id mengandung 'nav' atau 'menu'
    nav_containers = []
    nav_tag = soup.find("nav")
    if nav_tag:
        nav_containers.append(nav_tag)

    for attr in ["class", "id"]:
        for el in soup.find_all(attrs={attr: re.compile(r"(navbar|nav-|main.menu|primary.menu|menu.utama)", re.I)}):
            if el not in nav_containers:
                nav_containers.append(el)

    # Fallback: ul dengan >= 3 item link
    if not nav_containers:
        for ul in soup.find_all("ul"):
            links = ul.find_all("a", href=True)
            if len(links) >= 3:
                nav_containers.append(ul)
                break

    for container in nav_containers:
        for a in container.find_all("a", href=True):
            label = a.get_text(strip=True)
            href  = a["href"].strip()

            # Skip anchor-only, javascript, kosong
            if not label or href in ("#", "", "javascript:void(0)") or href.startswith("javascript"):
                continue
            if href.startswith("#"):
                continue

            full_url = urljoin(base_url, href)
            parsed   = urlparse(full_url)

            # Hanya ambil link dalam domain yang sama atau subdomain UNDIP
            if "undip.ac.id" not in parsed.netloc:
                continue

            # Skip file download
            if re.search(r"\.(pdf|docx?|xlsx?|pptx?|zip|rar)$", full_url, re.I):
                continue

            if full_url not in seen_urls:
                seen_urls.add(full_url)
                menus.append({"label": label, "url": full_url})

        # Cukup ambil dari container pertama yang menghasilkan item
        if menus:
            break

    # Batasi max 15 menu agar tidak terlalu lambat
    return menus[:15]


def check_menu_content(menu_url):
    """
    Cek apakah halaman menu memiliki konten bermakna.
    Return: "✅ Terisi" | "⚠️ Tipis" | "❌ Kosong/Error"
    """
    _, soup = fetch(menu_url)
    if soup is None:
        return "❌ Error", 0

    text = clean_text(soup)
    length = len(text)

    if length >= MIN_CONTENT_LENGTH:
        return "✅ Terisi", length
    elif length > 50:
        return "⚠️ Tipis", length
    else:
        return "❌ Kosong", length


def collect_site_text(base_url, soup):
    """
    Kumpulkan teks dari:
    - Halaman utama
    - Halaman berita/artikel (jika ada link berita yang ditemukan)
    Return: string teks gabungan
    """
    texts = [clean_text(soup)]

    # Cari link yang mengarah ke halaman berita/konten
    news_patterns = re.compile(
        r"(berita|news|artikel|article|pengumuman|agenda|kegiatan|publikasi|post)", re.I
    )

    visited = set([base_url])
    news_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full = urljoin(base_url, href)
        if full in visited:
            continue
        if "undip.ac.id" not in full:
            continue
        if news_patterns.search(full) or news_patterns.search(a.get_text()):
            news_links.append(full)
            visited.add(full)

    # Kunjungi maksimal 5 halaman berita
    for link in news_links[:5]:
        time.sleep(REQUEST_DELAY)
        _, nsoup = fetch(link)
        if nsoup:
            texts.append(clean_text(nsoup))

    return " ".join(texts)


# ─────────────────────────────────────────────
# MAIN CHECKER
# ─────────────────────────────────────────────

def check_site(site):
    """Jalankan semua pengecekan untuk satu website. Return dict hasil."""
    url  = site["url"]
    nama = site["nama"]
    short = site["short"]

    print(f"\n{'─'*60}")
    print(f"🔍  {nama}")
    print(f"    {url}")
    print(f"{'─'*60}")

    resp, soup = fetch(url)
    if soup is None:
        print("    ❌ Tidak dapat diakses")
        return {
            "url": url, "nama": nama, "short": short,
            "accessible": False,
            "menu_results": [],
            "topic_results": {t: False for t in TOPICS},
            "menu_score": 0,
            "topic_score": 0,
        }

    print(f"    ✅ HTTP {resp.status_code}")

    # ── 1. CEK MENU ──────────────────────────────
    print("    📂 Ekstrak menu navigasi...")
    menus = get_menu_items(soup, url)
    print(f"       Ditemukan {len(menus)} item menu")

    menu_results = []
    for m in menus:
        time.sleep(REQUEST_DELAY)
        status, length = check_menu_content(m["url"])
        print(f"       {status}  [{length} kar]  {m['label']}")
        menu_results.append({
            "label":  m["label"],
            "url":    m["url"],
            "status": status,
            "length": length,
        })

    # Skor menu: persen halaman yang "Terisi"
    if menu_results:
        filled = sum(1 for m in menu_results if "Terisi" in m["status"])
        menu_score = filled / len(menu_results) * 100
    else:
        menu_score = 0.0

    # ── 2. CEK TOPIK ─────────────────────────────
    print("    📰 Analisis topik konten...")
    combined_text = collect_site_text(url, soup)

    topic_results = {}
    for topic, patterns in TOPICS.items():
        found = check_topic_in_text(combined_text, patterns)
        topic_results[topic] = found
        icon = "✅" if found else "❌"
        print(f"       {icon}  {topic}")

    topic_score = sum(1 for v in topic_results.values() if v) / len(TOPICS) * 100

    print(f"\n    📊 Skor Menu  : {menu_score:.0f}%  ({filled if menu_results else 0}/{len(menu_results)} terisi)")
    print(f"    📊 Skor Topik : {topic_score:.0f}%  ({sum(1 for v in topic_results.values() if v)}/{len(TOPICS)} topik)")

    return {
        "url": url, "nama": nama, "short": short,
        "accessible": True,
        "menu_results": menu_results,
        "topic_results": topic_results,
        "menu_score": menu_score,
        "topic_score": topic_score,
    }


# ─────────────────────────────────────────────
# REPORT GENERATOR
# ─────────────────────────────────────────────

def generate_report(all_results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []

    lines += [
        "# 🌐 Laporan Kelengkapan Konten Website FSM UNDIP",
        "",
        f"**Tanggal Pengecekan:** {now}  ",
        f"**Jumlah Website:** {len(all_results)}  ",
        f"**Minimum konten dianggap 'terisi':** {MIN_CONTENT_LENGTH} karakter  ",
        "",
        "---",
        "",
    ]

    # ── Ringkasan Skor ────────────────────────────────────────────
    lines += [
        "## 📊 Ringkasan Skor",
        "",
        "| No | Institusi | URL | Skor Menu | Skor Topik | Status |",
        "|:--:|-----------|-----|:---------:|:----------:|:------:|",
    ]

    for i, r in enumerate(all_results, 1):
        if not r["accessible"]:
            lines.append(f"| {i} | {r['nama']} | {r['url']} | — | — | ❌ Tidak Dapat Diakses |")
            continue
        ms = r["menu_score"]
        ts = r["topic_score"]
        avg = (ms + ts) / 2
        status = "🟢 Baik" if avg >= 70 else ("🟡 Cukup" if avg >= 50 else "🔴 Kurang")
        lines.append(f"| {i} | {r['nama']} | {r['url']} | {ms:.0f}% | {ts:.0f}% | {status} |")

    lines += ["", "---", ""]

    # ── Detail Menu per Website ────────────────────────────────────
    lines += [
        "## 📂 Detail Kelengkapan Menu",
        "",
        "> Status: ✅ Terisi (≥200 kar) · ⚠️ Tipis (<200 kar) · ❌ Kosong/Error",
        "",
    ]

    for r in all_results:
        lines += [
            f"### {r['nama']}",
            f"URL: {r['url']}  ",
            f"Skor Menu: **{r['menu_score']:.0f}%**",
            "",
        ]

        if not r["accessible"]:
            lines += ["_Website tidak dapat diakses._", ""]
            continue

        if not r["menu_results"]:
            lines += ["_Tidak ada item menu yang terdeteksi._", ""]
            continue

        lines += [
            "| No | Label Menu | URL | Status | Panjang Konten |",
            "|:--:|-----------|-----|:------:|:--------------:|",
        ]
        for j, m in enumerate(r["menu_results"], 1):
            lines.append(
                f"| {j} | {m['label']} | {m['url']} | {m['status']} | {m['length']:,} kar |"
            )
        lines += [""]

    lines += ["---", ""]

    # ── Tabel Topic Coverage ──────────────────────────────────────
    lines += [
        "## 📰 Cakupan 7 Topik Wajib",
        "",
        "> Pengecekan dilakukan pada teks halaman utama + halaman berita/konten yang ditemukan.",
        "",
    ]

    # Header tabel
    accessible = [r for r in all_results if r["accessible"]]
    header = "| Topik |"
    sep    = "|-------|"
    for r in accessible:
        header += f" {r['short']} |"
        sep    += ":---:|"

    lines += [header, sep]

    for topic in TOPICS:
        row = f"| {topic} |"
        for r in accessible:
            val = r["topic_results"].get(topic, False)
            row += " ✅ |" if val else " ❌ |"
        lines.append(row)

    lines += [""]

    # Skor per topik (berapa website memuat topik ini)
    lines += [
        "### Skor per Topik (% website yang memuat)",
        "",
        "| Topik | Jumlah Website | Persentase |",
        "|-------|:--------------:|:----------:|",
    ]
    for topic in TOPICS:
        count = sum(1 for r in accessible if r["topic_results"].get(topic, False))
        pct   = count / len(accessible) * 100 if accessible else 0
        bar   = "🟢" if pct >= 75 else ("🟡" if pct >= 50 else "🔴")
        lines.append(f"| {topic} | {count}/{len(accessible)} | {pct:.0f}% {bar} |")

    lines += ["", "---", ""]

    # ── Rekomendasi ───────────────────────────────────────────────
    lines += ["## 💡 Rekomendasi", ""]

    for r in all_results:
        if not r["accessible"]:
            lines += [f"### {r['short']} — {r['nama']}", "- ⚠️ Website tidak dapat diakses.", ""]
            continue

        issues = []

        # Menu kosong
        empty_menus = [m["label"] for m in r["menu_results"] if "Terisi" not in m["status"]]
        if empty_menus:
            issues.append(f"**Menu perlu diisi konten:** {', '.join(empty_menus)}")

        # Topik hilang
        missing_topics = [t for t, v in r["topic_results"].items() if not v]
        if missing_topics:
            issues.append(f"**Topik belum tercakup:** {', '.join(missing_topics)}")

        if issues:
            lines += [f"### {r['short']} — {r['nama']}", f"_(Skor Menu: {r['menu_score']:.0f}% | Skor Topik: {r['topic_score']:.0f}%)_", ""]
            for iss in issues:
                lines.append(f"- {iss}")
            lines.append("")
        else:
            lines += [f"### {r['short']} — {r['nama']}", "- ✅ Semua menu terisi dan semua topik tercakup!", ""]

    lines += [
        "---",
        "",
        "## 📖 Legenda",
        "",
        "| Simbol | Keterangan |",
        "|:------:|------------|",
        "| ✅ | Ada / Terisi / Topik ditemukan |",
        "| ⚠️ | Konten tipis (< 200 karakter) |",
        "| ❌ | Tidak ada / Kosong / Error |",
        "| 🟢 | Baik (≥ 75%) |",
        "| 🟡 | Cukup (50–74%) |",
        "| 🔴 | Kurang (< 50%) |",
        "",
        "---",
        "",
        f"_Report di-generate otomatis oleh **check_website.py** pada {now}_",
        "",
    ]

    return "\n".join(lines)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  WEBSITE CONTENT & TOPIC CHECKER — FSM UNDIP")
    print("=" * 60)
    print(f"  Waktu  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Target : {len(WEBSITES)} website")
    print("=" * 60)

    all_results = []
    for site in WEBSITES:
        result = check_site(site)
        all_results.append(result)
        time.sleep(REQUEST_DELAY)

    # Simpan report
    report = generate_report(all_results)
    out_path = "website_report.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n" + "=" * 60)
    print(f"  ✅  Report tersimpan: {out_path}")

    # Print ringkasan akhir
    accessible = [r for r in all_results if r["accessible"]]
    if accessible:
        avg_menu  = sum(r["menu_score"]  for r in accessible) / len(accessible)
        avg_topic = sum(r["topic_score"] for r in accessible) / len(accessible)
        print(f"  📊  Rata-rata Skor Menu  : {avg_menu:.0f}%")
        print(f"  📊  Rata-rata Skor Topik : {avg_topic:.0f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
