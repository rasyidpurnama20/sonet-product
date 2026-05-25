#!/usr/bin/env python3
"""
Instagram Checker — FSM UNDIP
==============================
Mengecek:
1. Jumlah followers, following, dan total post per akun Instagram
2. Cakupan 7 topik wajib pada postingan 3 bulan terakhir
"""

import requests
import json
import re
import time
from datetime import datetime, timedelta, timezone

# ─────────────────────────────────────────────
# KONFIGURASI
# ─────────────────────────────────────────────

ACCOUNTS = [
    {"username": "fsmundip_official",          "nama": "Fak. Sains & Matematika", "short": "FSM"},
    {"username": "math.undip.official",         "nama": "Departemen Matematika",   "short": "MATH"},
    {"username": "biologi_fsm_undip",           "nama": "Departemen Biologi",      "short": "BIO"},
    {"username": "fisikaundip",                 "nama": "Departemen Fisika",       "short": "FISIKA"},
    {"username": "chemistry.diponegoro",        "nama": "Departemen Kimia",        "short": "KIMIA"},
    {"username": "statistikaundip.official",    "nama": "Departemen Statistika",   "short": "STAT"},
    {"username": "if.undip",                    "nama": "Departemen Informatika",  "short": "IF"},
    {"username": "bioteknologi.undip",          "nama": "Departemen Bioteknologi", "short": "BIOTEK"},
]


TOPICS = {
    "Prospek Kerja Lulusan": [
        r"prospek\s+kerja", r"karir", r"lapangan\s+kerja", r"profil\s+lulusan",
        r"alumni\s+bekerja", r"career", r"pekerjaan", r"peluang\s+kerja",
        r"profesi", r"industri\s+mitra",
    ],
    "Alumni": [
        r"\balumni\b", r"lulusan", r"tracer\s+study", r"ikatan\s+alumni",
        r"alumni\s+undip", r"himpunan\s+alumni",
    ],
    "Kurikulum": [
        r"kurikulum", r"mata\s+kuliah", r"\bmatkul\b", r"silabus",
        r"rencana\s+studi", r"\bsks\b", r"curriculum", r"\brps\b",
        r"struktur\s+program", r"capaian\s+pembelajaran",
    ],
    "Pendaftaran": [
        r"pendaftaran", r"\bdaftar\b", r"seleksi", r"\bsnbt\b", r"\butbk\b",
        r"\bsbmptn\b", r"\bpmb\b", r"penerimaan\s+mahasiswa",
        r"jalur\s+masuk", r"registrasi", r"admisi",
    ],
    "Fasilitas": [
        r"fasilitas", r"laboratorium", r"\blab\b", r"perpustakaan",
        r"\bgedung\b", r"sarana", r"prasarana", r"ruang\s+kuliah",
        r"studio", r"workshop", r"peralatan",
    ],
    "Prestasi": [
        r"prestasi", r"penghargaan", r"\baward\b", r"\bjuara\b",
        r"\blomba\b", r"kompetisi", r"achievement", r"medali",
        r"terbaik", r"unggulan", r"mahasiswa\s+berprestasi",
    ],
    "Riset & Pengabdian": [
        r"\briset\b", r"penelitian", r"pengabdian", r"publikasi",
        r"\bjurnal\b", r"\bresearch\b", r"\bpkm\b", r"\babdimas\b",
        r"hibah", r"seminar\s+nasional", r"konferensi",
    ],
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8",
    "Referer": "https://www.instagram.com/",
}

REQUEST_DELAY = 3.0   # detik antar akun (hindari rate-limit)
MONTHS_BACK   = 3     # periode analisis postingan



# ─────────────────────────────────────────────
# SCRAPING HELPERS
# ─────────────────────────────────────────────

def _get_cutoff_date():
    """Tanggal batas: MONTHS_BACK bulan yang lalu dari sekarang."""
    now = datetime.now(tz=timezone.utc)
    # Hitung bulan mundur secara manual
    month = now.month - MONTHS_BACK
    year  = now.year
    while month <= 0:
        month += 12
        year  -= 1
    return now.replace(year=year, month=month)


def _check_topic(text, patterns):
    text_lower = text.lower()
    return any(re.search(p, text_lower) for p in patterns)


def _parse_count(raw):
    """
    Ubah string follower seperti '12.3K', '1.2M', '5,432' menjadi integer.
    """
    if raw is None:
        return None
    raw = str(raw).strip().replace(",", "").replace(".", "")
    # Handle K/M suffix
    raw_orig = str(raw).strip()
    raw_orig_lower = raw_orig.lower()
    try:
        if raw_orig_lower.endswith("k"):
            return int(float(raw_orig_lower[:-1]) * 1_000)
        elif raw_orig_lower.endswith("m"):
            return int(float(raw_orig_lower[:-1]) * 1_000_000)
        else:
            # Sudah di-strip koma/titik di atas
            return int(raw)
    except (ValueError, AttributeError):
        return None


def _fmt_count(n):
    """Format integer ke string readable, misal 12345 -> '12,345'."""
    if n is None:
        return "N/A"
    return f"{n:,}"



def fetch_profile_via_api(username, session):
    """
    Coba ambil data profil melalui endpoint JSON publik Instagram.
    Strategi 1: /?__a=1&__d=dis  (kadang masih berjalan untuk akun publik)
    Return dict profil atau None.
    """
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    try:
        resp = session.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            user = (
                data.get("graphql", {}).get("user")
                or data.get("data", {}).get("user")
                or data.get("user")
            )
            if user:
                return user
    except Exception:
        pass
    return None


def fetch_profile_via_html(username, session):
    """
    Fallback: parse halaman HTML profil publik.
    Ekstrak dari tag <script type="application/ld+json"> atau meta tags.
    Return dict dengan key: followers, following, posts, bio, posts_data
    """
    url = f"https://www.instagram.com/{username}/"
    result = {
        "followers": None, "following": None,
        "posts_count": None, "bio": "",
        "posts_data": [], "method": "html",
        "blocked": False,
    }
    try:
        resp = session.get(url, timeout=15)
        if resp.status_code in (401, 403, 429):
            result["blocked"] = True
            return result

        html = resp.text

        # ── Coba ekstrak dari JSON dalam <script> ──────────────────
        # Instagram menyematkan data awal di window.__additionalDataLoaded atau _sharedData
        shared_match = re.search(r"window\._sharedData\s*=\s*(\{.*?\});</script>", html, re.S)
        if shared_match:
            try:
                shared = json.loads(shared_match.group(1))
                entry  = shared.get("entry_data", {}).get("ProfilePage", [{}])[0]
                user   = entry.get("graphql", {}).get("user", {})
                if user:
                    result["followers"]   = user.get("edge_followed_by", {}).get("count")
                    result["following"]   = user.get("edge_follow", {}).get("count")
                    result["posts_count"] = user.get("edge_owner_to_timeline_media", {}).get("count")
                    result["bio"]         = user.get("biography", "")
                    edges = user.get("edge_owner_to_timeline_media", {}).get("edges", [])
                    result["posts_data"]  = _extract_posts_from_edges(edges)
                    result["method"]      = "sharedData"
                    return result
            except Exception:
                pass

        # ── Fallback: meta description & OG tags ──────────────────
        # Instagram meta: "X Followers, Y Following, Z Posts"
        meta_desc = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
            html, re.I
        )
        if meta_desc:
            desc = meta_desc.group(1)
            # Contoh: "12.3K Followers, 150 Following, 200 Posts"
            fl = re.search(r"([\d,.]+[KkMm]?)\s+[Ff]ollower", desc)
            fw = re.search(r"([\d,.]+[KkMm]?)\s+[Ff]ollowing", desc)
            po = re.search(r"([\d,.]+[KkMm]?)\s+[Pp]ost",     desc)
            if fl:
                result["followers"]   = _parse_count(fl.group(1))
            if fw:
                result["following"]   = _parse_count(fw.group(1))
            if po:
                result["posts_count"] = _parse_count(po.group(1))

        # ── Coba JSON-LD ──────────────────────────────────────────
        for script in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                ld = json.loads(script)
                if isinstance(ld, list):
                    ld = ld[0]
                if ld.get("@type") == "ProfilePage":
                    interaction = ld.get("interactionStatistic", [])
                    for stat in (interaction if isinstance(interaction, list) else [interaction]):
                        itype = stat.get("interactionType", "")
                        val   = stat.get("userInteractionCount")
                        if "Follow" in itype:
                            result["followers"] = _parse_count(val)
            except Exception:
                pass

        # ── Coba ekstrak caption dari HTML ────────────────────────
        # Ambil teks alt dari gambar (Instagram sering menaruh caption di alt)
        captions = re.findall(r'"accessibility_caption"\s*:\s*"([^"]+)"', html)
        if not captions:
            captions = re.findall(r'"text"\s*:\s*"([^"]{20,500})"', html)
        result["posts_data"] = [{"caption": c, "timestamp": None} for c in captions[:50]]

    except Exception as e:
        result["error"] = str(e)

    return result


def _extract_posts_from_edges(edges):
    """Ekstrak list post dari GraphQL edges."""
    posts = []
    for edge in edges:
        node = edge.get("node", {})
        caption_edges = node.get("edge_media_to_caption", {}).get("edges", [])
        caption = ""
        if caption_edges:
            caption = caption_edges[0].get("node", {}).get("text", "")
        ts = node.get("taken_at_timestamp")
        posts.append({"caption": caption, "timestamp": ts})
    return posts



# ─────────────────────────────────────────────
# MAIN CHECKER
# ─────────────────────────────────────────────

def check_account(account, session):
    """Cek satu akun Instagram. Return dict hasil."""
    username = account["username"]
    nama     = account["nama"]
    short    = account["short"]

    print(f"\n{'─'*60}")
    print(f"📸  @{username}  —  {nama}")
    print(f"{'─'*60}")

    # Coba API dulu, fallback ke HTML
    raw = fetch_profile_via_api(username, session)
    method = "api"
    if raw is None:
        print("    [INFO] API endpoint tidak tersedia, fallback ke HTML...")
        raw = fetch_profile_via_html(username, session)
        method = raw.get("method", "html") if isinstance(raw, dict) else "html"
    else:
        method = "api"

    # Normalisasi data dari raw
    if isinstance(raw, dict) and "followers" in raw:
        # Sudah dari fetch_profile_via_html
        followers   = raw.get("followers")
        following   = raw.get("following")
        posts_count = raw.get("posts_count")
        posts_data  = raw.get("posts_data", [])
        blocked     = raw.get("blocked", False)
    else:
        # Dari API GraphQL
        followers   = raw.get("edge_followed_by", {}).get("count") if raw else None
        following   = raw.get("edge_follow",       {}).get("count") if raw else None
        edges       = (raw.get("edge_owner_to_timeline_media", {}).get("edges", [])
                       if raw else [])
        posts_count = (raw.get("edge_owner_to_timeline_media", {}).get("count")
                       if raw else None)
        posts_data  = _extract_posts_from_edges(edges)
        blocked     = False

    if blocked:
        print("    ⚠️  Instagram memblokir akses (login wall / rate limit)")
        return {
            "username": username, "nama": nama, "short": short,
            "accessible": False, "blocked": True,
            "followers": None, "following": None, "posts_count": None,
            "analyzed_posts": 0,
            "topic_results": {t: False for t in TOPICS},
            "topic_score": 0,
            "note": "Diblokir Instagram (butuh login)",
        }

    print(f"    👥 Followers : {_fmt_count(followers)}")
    print(f"    👤 Following : {_fmt_count(following)}")
    print(f"    📸 Total Post: {_fmt_count(posts_count)}")
    print(f"    🔧 Metode    : {method}")

    # Filter postingan dalam MONTHS_BACK bulan terakhir
    cutoff   = _get_cutoff_date()
    recent   = []
    no_ts    = []  # postingan tanpa timestamp (tetap dianalisis)

    for p in posts_data:
        ts = p.get("timestamp")
        if ts is None:
            no_ts.append(p)
        else:
            try:
                dt = datetime.fromtimestamp(int(ts), tz=timezone.utc)
                if dt >= cutoff:
                    recent.append(p)
            except Exception:
                no_ts.append(p)

    # Jika tidak ada yang punya timestamp, analisis semua yang ada
    to_analyze = recent if recent else (no_ts[:30] if no_ts else [])
    ts_note = (f"{len(recent)} postingan sejak {cutoff.strftime('%Y-%m-%d')}"
               if recent else f"{len(to_analyze)} postingan (tanpa timestamp, analisis semua tersedia)")

    print(f"    📅 Dianalisis: {ts_note}")

    # Gabungkan semua caption untuk analisis topik
    combined_text = " ".join(p.get("caption", "") for p in to_analyze)

    topic_results = {}
    for topic, patterns in TOPICS.items():
        found = _check_topic(combined_text, patterns)
        topic_results[topic] = found
        icon = "✅" if found else "❌"
        print(f"    {icon}  {topic}")

    topic_score = sum(1 for v in topic_results.values() if v) / len(TOPICS) * 100
    print(f"\n    📊 Skor Topik: {topic_score:.0f}%")

    return {
        "username": username, "nama": nama, "short": short,
        "accessible": True, "blocked": False,
        "followers": followers, "following": following,
        "posts_count": posts_count,
        "analyzed_posts": len(to_analyze),
        "ts_note": ts_note,
        "topic_results": topic_results,
        "topic_score": topic_score,
        "method": method,
    }



# ─────────────────────────────────────────────
# REPORT GENERATOR
# ─────────────────────────────────────────────

def generate_report(all_results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cutoff_str = _get_cutoff_date().strftime("%Y-%m-%d")
    lines = []

    lines += [
        "# 📸 Laporan Instagram FSM UNDIP",
        "",
        f"**Tanggal Pengecekan:** {now}  ",
        f"**Periode Analisis Postingan:** {cutoff_str} s/d sekarang ({MONTHS_BACK} bulan terakhir)  ",
        f"**Jumlah Akun:** {len(all_results)}  ",
        "",
        "---",
        "",
    ]

    # ── Tabel Follower Summary ─────────────────────────────────────
    lines += [
        "## 👥 Ringkasan Follower & Aktivitas",
        "",
        "| No | Akun | Institusi | Followers | Following | Total Post | Post Dianalisis | Status |",
        "|:--:|------|-----------|----------:|----------:|-----------:|:---------------:|:------:|",
    ]

    for i, r in enumerate(all_results, 1):
        acct = f"[@{r['username']}](https://instagram.com/{r['username']})"
        if not r["accessible"]:
            reason = "Login Wall" if r.get("blocked") else "Error"
            lines.append(
                f"| {i} | {acct} | {r['nama']} | — | — | — | — | ⚠️ {reason} |"
            )
            continue
        ts_score = r["topic_score"]
        status = "🟢" if ts_score >= 70 else ("🟡" if ts_score >= 40 else "🔴")
        lines.append(
            f"| {i} | {acct} | {r['nama']} | "
            f"{_fmt_count(r['followers'])} | "
            f"{_fmt_count(r['following'])} | "
            f"{_fmt_count(r['posts_count'])} | "
            f"{r['analyzed_posts']} | "
            f"{status} {ts_score:.0f}% |"
        )

    lines += ["", "---", ""]

    # ── Tabel Topic Coverage ──────────────────────────────────────
    accessible = [r for r in all_results if r["accessible"]]

    lines += [
        "## 📰 Cakupan 7 Topik Wajib pada Postingan",
        "",
        f"> Analisis caption postingan {MONTHS_BACK} bulan terakhir.",
        "> ✅ = topik ditemukan dalam caption  ❌ = tidak ditemukan",
        "",
    ]

    if accessible:
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
        lines.append("")

        # Skor per topik
        lines += [
            "### Skor per Topik (% akun yang membahas)",
            "",
            "| Topik | Jumlah Akun | Persentase |",
            "|-------|:-----------:|:----------:|",
        ]
        for topic in TOPICS:
            count = sum(1 for r in accessible if r["topic_results"].get(topic, False))
            pct   = count / len(accessible) * 100 if accessible else 0
            bar   = "🟢" if pct >= 75 else ("🟡" if pct >= 50 else "🔴")
            lines.append(f"| {topic} | {count}/{len(accessible)} | {pct:.0f}% {bar} |")
        lines.append("")
    else:
        lines += ["> _Tidak ada akun yang dapat dianalisis._", ""]

    lines += ["---", ""]

    # ── Rekomendasi ───────────────────────────────────────────────
    lines += ["## 💡 Rekomendasi Konten", ""]

    for r in all_results:
        acct_link = f"[@{r['username']}](https://instagram.com/{r['username']})"
        if not r["accessible"]:
            lines += [
                f"### {r['short']} — {r['nama']} ({acct_link})",
                f"- ⚠️ Akun tidak dapat diakses saat pengecekan. Pastikan akun **tidak di-private** dan dapat diakses publik.",
                "",
            ]
            continue

        missing = [t for t, v in r["topic_results"].items() if not v]
        if missing:
            lines += [
                f"### {r['short']} — {r['nama']} ({acct_link})",
                f"_(Skor Topik: {r['topic_score']:.0f}% | {r['analyzed_posts']} postingan dianalisis)_",
                "",
                "**Topik yang belum dibahas dalam postingan terbaru:**",
            ]
            for t in missing:
                lines.append(f"- {t}")
            lines.append("")
        else:
            lines += [
                f"### {r['short']} — {r['nama']} ({acct_link})",
                f"- ✅ Semua 7 topik wajib ditemukan dalam postingan terbaru!",
                "",
            ]

    lines += [
        "---",
        "",
        "## 📖 Catatan Teknis",
        "",
        "- Data diambil dari halaman **publik** Instagram tanpa API resmi.",
        "- Jika Instagram menampilkan halaman login (login wall), data follower tidak dapat diambil.",
        "  Solusi: gunakan tool seperti [Instaloader](https://instaloader.github.io/) dengan akun login.",
        "- Analisis topik berdasarkan **pencocokan kata kunci** (regex) pada caption postingan.",
        "  Akurasi bergantung pada kata kunci yang tersedia di caption (bukan Stories/Reels tanpa teks).",
        "",
        "---",
        "",
        f"_Report di-generate otomatis oleh **check_instagram.py** pada {now}_",
        "",
    ]

    return "\n".join(lines)



# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  INSTAGRAM CHECKER — FSM UNDIP")
    print("=" * 60)
    print(f"  Waktu    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Target   : {len(ACCOUNTS)} akun")
    print(f"  Periode  : {MONTHS_BACK} bulan terakhir")
    print("=" * 60)

    # Gunakan Session agar cookie/headers konsisten
    session = requests.Session()
    session.headers.update(HEADERS)

    # Kunjungi homepage dulu agar dapat cookie awal
    try:
        session.get("https://www.instagram.com/", timeout=10)
        time.sleep(1)
    except Exception:
        pass

    all_results = []
    for account in ACCOUNTS:
        result = check_account(account, session)
        all_results.append(result)
        print(f"    ⏳ Menunggu {REQUEST_DELAY}s sebelum akun berikutnya...")
        time.sleep(REQUEST_DELAY)

    # Simpan report
    report = generate_report(all_results)
    out_path = "instagram_report.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n" + "=" * 60)
    print(f"  ✅  Report tersimpan: {out_path}")

    accessible = [r for r in all_results if r["accessible"]]
    if accessible:
        avg_topic = sum(r["topic_score"] for r in accessible) / len(accessible)
        total_fl  = sum(r["followers"] or 0 for r in accessible)
        print(f"  📊  Rata-rata Skor Topik : {avg_topic:.0f}%")
        print(f"  👥  Total Followers      : {_fmt_count(total_fl)}")
    blocked = sum(1 for r in all_results if r.get("blocked"))
    if blocked:
        print(f"  ⚠️   Akun diblokir/login wall: {blocked}/{len(all_results)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
