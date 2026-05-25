#!/usr/bin/env python3
"""
Instagram Checker - UNDIP
Ambil followers, jumlah post, dan analisis topik postingan 3 bulan terakhir.

Cara pakai:
    pip install instaloader
    python check_instagram.py

Catatan: Instagram memblokir IP datacenter. Jalankan dari komputer lokal,
atau isi manual_ig_data.json sebagai fallback.
"""

import json, os, re, sys, signal
from datetime import datetime, timedelta, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout

# ── Akun yang dicek ────────────────────────────────────────────────
ACCOUNTS = [
    {"username": "fsmundip_official",        "nama": "Fak. Sains dan Matematika"},
    {"username": "math.undip.official",       "nama": "Departemen Matematika"},
    {"username": "biologi_fsm_undip",         "nama": "Departemen Biologi"},
    {"username": "fisikaundip",               "nama": "Departemen Fisika"},
    {"username": "chemistry.diponegoro",      "nama": "Departemen Kimia"},
    {"username": "statistikaundip.official",  "nama": "Departemen Statistika"},
    {"username": "if.undip",                  "nama": "Departemen Informatika"},
    {"username": "bioteknologi.undip",        "nama": "Departemen Bioteknologi"},
]

# ── Topik yang dicari di caption ───────────────────────────────────
TOPICS = {
    "Prospek Kerja": ["prospek kerja", "peluang kerja", "career", "karir", "dunia kerja", "tracer study", "job fair"],
    "Alumni":        ["alumni", "wisuda", "wisudawan", "ikatan alumni", "iluni"],
    "Kurikulum":     ["kurikulum", "mata kuliah", "silabus", "sks", "rps"],
    "Pendaftaran":   ["pendaftaran", "snbp", "snbt", "um undip", "calon mahasiswa", "pmb", "daftar"],
    "Fasilitas":     ["fasilitas", "laboratorium", "lab ", "perpustakaan", "sarana", "gedung"],
    "Prestasi":      ["prestasi", "juara", "lomba", "kompetisi", "olimpiade", "penghargaan", "medali", "winner"],
    "Riset & Abdimas": ["riset", "penelitian", "research", "publikasi", "jurnal", "pengabdian", "abdimas", "pkm "],
}

MONTHS_BACK  = 3
MAX_POSTS    = 30       # batas post per akun
FETCH_TIMEOUT = 12      # detik max per akun (agar total < 2 menit)
DIR = os.path.dirname(os.path.abspath(__file__))


# ── Topic helper ───────────────────────────────────────────────────

def topic_of(text):
    t = text.lower()
    return [name for name, kws in TOPICS.items() if any(k in t for k in kws)]


# ── Manual data fallback ───────────────────────────────────────────

def load_manual():
    path = os.path.join(DIR, "manual_ig_data.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return {k: v for k, v in raw.items() if not k.startswith("_")}


# ── Fetch satu akun via instaloader ───────────────────────────────

def _fetch_one(username):
    import instaloader
    L = instaloader.Instaloader(
        download_pictures=False, download_videos=False,
        download_video_thumbnails=False, download_geotags=False,
        download_comments=False, save_metadata=False, quiet=True,
    )
    L.context.max_connection_attempts = 1

    p = instaloader.Profile.from_username(L.context, username)

    posts = []
    if not p.is_private:
        cutoff = datetime.now(timezone.utc) - timedelta(days=MONTHS_BACK * 30)
        for post in p.get_posts():
            if post.date_utc.replace(tzinfo=timezone.utc) < cutoff:
                break
            cap = post.caption or ""
            posts.append({
                "date":    post.date_utc.strftime("%Y-%m-%d"),
                "caption": cap[:300],
                "topics":  topic_of(cap),
                "url":     f"https://www.instagram.com/p/{post.shortcode}/",
            })
            if len(posts) >= MAX_POSTS:
                break

    return {
        "username":    p.username,
        "full_name":   p.full_name,
        "followers":   p.followers,
        "following":   p.followees,
        "posts_total": p.mediacount,
        "bio":         p.biography,
        "private":     p.is_private,
        "posts":       posts,
    }


def fetch(username):
    """Fetch dengan hard timeout agar tidak hang lama."""
    try:
        import instaloader  # noqa: early check
    except ImportError:
        return None, "instaloader belum terinstall — jalankan: pip install instaloader"

    with ThreadPoolExecutor(max_workers=1) as ex:
        fut = ex.submit(_fetch_one, username)
        try:
            return fut.result(timeout=FETCH_TIMEOUT), None
        except FuturesTimeout:
            return None, f"Timeout setelah {FETCH_TIMEOUT}s (IP mungkin diblokir)"
        except Exception as e:
            msg = str(e)
            if "403" in msg or "ProfileNotExists" in msg:
                return None, "IP diblokir Instagram — jalankan dari komputer lokal"
            return None, msg[:120]


# ── Buat report Markdown ───────────────────────────────────────────

def make_report(results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Laporan Instagram Akun UNDIP", "",
        f"**Tanggal:** {now}  ",
        f"**Periode postingan:** {MONTHS_BACK} bulan terakhir", "", "---", "",
    ]

    # Ringkasan follower
    lines += ["## Ringkasan", "",
              "| No | Akun | Institusi | Followers | Total Post | Post Dianalisis |",
              "|:--:|------|-----------|----------:|:----------:|:---------------:|"]
    for i, r in enumerate(results, 1):
        acc, d = r["account"], r["data"]
        link = f"[@{acc['username']}](https://www.instagram.com/{acc['username']}/)"
        if d:
            fo = f"{d['followers']:,}" if isinstance(d.get('followers'), int) else str(d.get('followers', '—'))
            pt = f"{d['posts_total']:,}" if isinstance(d.get('posts_total'), int) else str(d.get('posts_total', '—'))
            pa = len(d.get('posts', []))
            lines.append(f"| {i} | {link} | {acc['nama']} | {fo} | {pt} | {pa} |")
        else:
            lines.append(f"| {i} | {link} | {acc['nama']} | — | — | — |")
    lines += ["", "---", ""]

    # Tabel topik
    tnames = list(TOPICS.keys())
    lines += [f"## Topik Postingan ({MONTHS_BACK} Bulan Terakhir)", "",
              "| Akun | " + " | ".join(tnames) + " |",
              "|------|" + "|".join([":-:"] * len(tnames)) + "|"]
    for r in results:
        acc, d = r["account"], r["data"]
        if not d or not d.get("posts"):
            lines.append("| @" + acc['username'] + " | " + " | ".join(["—"]*len(tnames)) + " |")
        else:
            cnt = {t: 0 for t in tnames}
            for p in d["posts"]:
                for t in p.get("topics", []):
                    if t in cnt: cnt[t] += 1
            vals = [str(cnt[t]) if cnt[t] else "—" for t in tnames]
            lines.append(f"| @{acc['username']} | " + " | ".join(vals) + " |")
    lines += ["", "---", ""]

    # Detail per akun
    lines += ["## Detail per Akun", ""]
    for r in results:
        acc, d, err = r["account"], r["data"], r["error"]
        lines.append(f"### @{acc['username']} — {acc['nama']}")
        if not d:
            lines += [f"- **Status:** Gagal fetch", f"- **Keterangan:** {err}", ""]
            continue
        fo = f"{d['followers']:,}" if isinstance(d.get('followers'), int) else str(d.get('followers', '—'))
        lines += [
            f"- **Nama:** {d.get('full_name', '—')}",
            f"- **Followers:** {fo}",
            f"- **Following:** {d.get('following', '—')}",
            f"- **Total Post:** {d.get('posts_total', '—')}",
            f"- **Bio:** {(d.get('bio') or '—')[:150]}",
        ]
        posts = d.get("posts", [])
        lines.append(f"- **Post dianalisis ({MONTHS_BACK} bln):** {len(posts)}")
        if posts:
            lines += ["", "  | Tanggal | Topik | Preview Caption |",
                      "  |---------|-------|-----------------|"]
            for p in posts[:10]:
                cap = p['caption'].replace('\n', ' ')[:80] + ("…" if len(p['caption']) > 80 else "")
                tp  = ", ".join(p['topics']) if p['topics'] else "—"
                lines.append(f"  | {p['date']} | {tp} | {cap} |")
        lines.append("")

    lines += ["---", "", f"*Di-generate otomatis pada {now}*", ""]
    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  INSTAGRAM CHECKER — UNDIP")
    print("=" * 55, "\n")

    manual = load_manual()
    if manual:
        print(f"[Manual data] tersedia untuk: {list(manual.keys())}\n")

    results = []
    for acc in ACCOUNTS:
        u = acc["username"]
        print(f"→ @{u:<35}", end=" ", flush=True)

        if u in manual:
            d = {**manual[u], "posts": manual[u].get("posts", [])}
            fo = d.get('followers', '?')
            fo_str = f"{fo:,}" if isinstance(fo, int) else str(fo)
            print(f"[manual] {fo_str} followers")
            results.append({"account": acc, "data": d, "error": None})
            continue

        data, err = fetch(u)
        if data:
            fo_str = f"{data['followers']:,}" if isinstance(data.get('followers'), int) else "?"
            print(f"[OK] {fo_str} followers, {len(data['posts'])} post dianalisis")
        else:
            print(f"[GAGAL] {err}")
        results.append({"account": acc, "data": data, "error": err})

    # Simpan report
    report = make_report(results)
    out = os.path.join(DIR, "instagram_report.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(report)

    ok = sum(1 for r in results if r["data"])
    print(f"\nSelesai: {ok}/{len(ACCOUNTS)} akun berhasil → {out}")

    if ok == 0:
        print("\n[!] Semua gagal — IP sandbox diblokir Instagram.")
        print("    → Jalankan dari komputer lokal, ATAU isi manual_ig_data.json")


if __name__ == "__main__":
    main()
