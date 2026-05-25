#!/usr/bin/env python3
"""
Instagram Account Checker
Mengecek jumlah follower dan analisis konten postingan 3 bulan terakhir
untuk akun-akun Instagram resmi UNDIP.

CATATAN: Instagram aktif memblokir scraping dari IP datacenter / cloud.
Jika dijalankan dari cloud/sandbox, script ini mungkin gagal mengambil data.
Jalankan dari komputer lokal untuk hasil terbaik. Sebagai fallback, tersedia
opsi input manual via file `manual_ig_data.json`.
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

try:
    import instaloader
    HAS_INSTALOADER = True
except ImportError:
    HAS_INSTALOADER = False

import requests

# Daftar akun Instagram yang akan dicek
ACCOUNTS = [
    {"username": "fsmundip_official", "nama": "Fakultas Sains dan Matematika"},
    {"username": "math.undip.official", "nama": "Departemen Matematika"},
    {"username": "biologi_fsm_undip", "nama": "Departemen Biologi"},
    {"username": "fisikaundip", "nama": "Departemen Fisika"},
    {"username": "chemistry.diponegoro", "nama": "Departemen Kimia"},
    {"username": "statistikaundip.official", "nama": "Departemen Statistika"},
    {"username": "if.undip", "nama": "Departemen Informatika"},
    {"username": "bioteknologi.undip", "nama": "Departemen Bioteknologi"},
]

# Topik yang dicari di caption postingan
TOPICS = {
    "Prospek Kerja Lulusan": [
        "prospek kerja", "lulusan", "career", "karir", "lapangan kerja",
        "peluang kerja", "career opportunity", "alumni bekerja", "job",
        "industri", "dunia kerja", "tracer study"
    ],
    "Alumni": [
        "alumni", "alumnus", "lulusan", "wisuda", "wisudawan", "tracer",
        "ikatan alumni", "iluni", "reuni"
    ],
    "Kurikulum": [
        "kurikulum", "curriculum", "mata kuliah", "matkul", "silabus",
        "syllabus", "course", "sks", "semester", "rps"
    ],
    "Pendaftaran": [
        "pendaftaran", "daftar", "penerimaan", "registration", "snbp",
        "snbt", "um undip", "um-undip", "mandiri", "calon mahasiswa",
        "maba", "open recruitment", "open registration", "info pendaftaran"
    ],
    "Fasilitas": [
        "fasilitas", "facility", "laboratorium", "lab ", "gedung",
        "ruang kelas", "ruang kuliah", "perpustakaan", "library",
        "sarana", "prasarana"
    ],
    "Prestasi": [
        "prestasi", "juara", "achievement", "winner", "menang", "medali",
        "champion", "lomba", "kompetisi", "olimpiade", "award", "penghargaan",
        "best paper", "1st place", "runner up"
    ],
    "Riset dan Pengabdian": [
        "riset", "penelitian", "research", "publikasi", "publication",
        "jurnal", "journal", "pengabdian", "pkm ", "p2m", "community service",
        "abdimas", "pengabdian masyarakat"
    ],
}


def load_manual_data():
    """Load manual data fallback jika tersedia."""
    manual_path = os.path.join(os.path.dirname(__file__) or ".", "manual_ig_data.json")
    if os.path.exists(manual_path):
        try:
            with open(manual_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"  [WARN] Gagal load manual data: {e}")
    return {}


def analyze_caption_topics(caption):
    """Analisis caption untuk mendeteksi topik-topik yang dibahas."""
    if not caption:
        return []
    caption_lower = caption.lower()
    found_topics = []
    for topic, keywords in TOPICS.items():
        for kw in keywords:
            if kw in caption_lower:
                found_topics.append(topic)
                break
    return found_topics


def fetch_account_instaloader(username, months_back=3):
    """Coba fetch data akun via instaloader."""
    if not HAS_INSTALOADER:
        return None, "instaloader tidak terinstall"

    try:
        L = instaloader.Instaloader(
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            quiet=True,
        )

        profile = instaloader.Profile.from_username(L.context, username)

        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "followers": profile.followers,
            "following": profile.followees,
            "posts_total": profile.mediacount,
            "biography": profile.biography,
            "is_private": profile.is_private,
            "external_url": profile.external_url,
            "recent_posts": [],
        }

        if profile.is_private:
            return data, None

        # Ambil posts dalam 3 bulan terakhir
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=months_back * 30)
        posts = []
        try:
            for post in profile.get_posts():
                if post.date_utc.replace(tzinfo=timezone.utc) < cutoff_date:
                    break
                caption = post.caption or ""
                topics = analyze_caption_topics(caption)
                posts.append({
                    "date": post.date_utc.strftime("%Y-%m-%d"),
                    "caption_preview": caption[:200],
                    "topics": topics,
                    "likes": post.likes,
                    "url": f"https://www.instagram.com/p/{post.shortcode}/",
                })
                # Batasi jumlah post (rate limit)
                if len(posts) >= 50:
                    break
        except Exception as e:
            data["posts_error"] = f"Gagal fetch posts: {type(e).__name__}: {e}"

        data["recent_posts"] = posts
        return data, None

    except instaloader.exceptions.ProfileNotExistsException:
        return None, "Profile tidak ditemukan"
    except instaloader.exceptions.ConnectionException as e:
        return None, f"Connection error (kemungkinan IP diblokir): {e}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def fetch_account_html(username):
    """Fallback: coba fetch via HTML public page (og:description)."""
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        r = requests.get(url, headers=headers, timeout=15, allow_redirects=False)
        if r.status_code != 200:
            return None, f"HTTP {r.status_code} (kemungkinan diblokir/redirect login)"
        html = r.text
        # Cari og:description seperti: "1,234 Followers, 567 Following, 89 Posts - ..."
        m = re.search(r'<meta property="og:description" content="([^"]+)"', html)
        if not m:
            return None, "Meta og:description tidak ditemukan"
        desc = m.group(1)
        # Parse angka
        followers_m = re.search(r"([\d,\.KMB]+)\s+Followers?", desc, re.I)
        following_m = re.search(r"([\d,\.KMB]+)\s+Following", desc, re.I)
        posts_m = re.search(r"([\d,\.KMB]+)\s+Posts?", desc, re.I)
        return {
            "username": username,
            "followers_str": followers_m.group(1) if followers_m else None,
            "following_str": following_m.group(1) if following_m else None,
            "posts_str": posts_m.group(1) if posts_m else None,
            "raw_description": desc,
            "recent_posts": [],
            "note": "Data dari og:description (terbatas, tanpa analisis caption)",
        }, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def check_account(account, manual_data):
    """Jalankan pengecekan untuk satu akun."""
    username = account["username"]
    nama = account["nama"]
    print(f"\nMengecek: @{username} ({nama})")

    # Cek manual data dulu
    if username in manual_data:
        print(f"  [INFO] Menggunakan data manual dari manual_ig_data.json")
        data = manual_data[username]
        data.setdefault("username", username)
        data.setdefault("recent_posts", [])
        return {
            "account": account,
            "data": data,
            "source": "manual",
            "error": None,
        }

    # Coba instaloader
    data, err = fetch_account_instaloader(username)
    if data:
        print(f"  [OK] Followers: {data['followers']:,}")
        return {"account": account, "data": data, "source": "instaloader", "error": None}

    print(f"  [WARN] instaloader gagal: {err}")

    # Fallback ke HTML
    data, err2 = fetch_account_html(username)
    if data:
        print(f"  [OK] Data dari HTML (terbatas): {data.get('followers_str')}")
        return {"account": account, "data": data, "source": "html", "error": None}

    print(f"  [ERROR] HTML juga gagal: {err2}")
    return {
        "account": account,
        "data": None,
        "source": None,
        "error": f"instaloader: {err} | html: {err2}",
    }


def aggregate_topics(recent_posts):
    """Hitung berapa post yang membahas tiap topik."""
    counts = {topic: 0 for topic in TOPICS.keys()}
    for post in recent_posts:
        for topic in post.get("topics", []):
            if topic in counts:
                counts[topic] += 1
    return counts


def generate_report(all_results, months_back=3):
    """Generate laporan Instagram dalam format Markdown."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = []
    report.append("# Laporan Instagram Akun Resmi UNDIP")
    report.append("")
    report.append(f"**Tanggal Pengecekan:** {now}")
    report.append("")
    report.append(f"**Jumlah Akun:** {len(all_results)}")
    report.append("")
    report.append(f"**Periode Analisis Postingan:** {months_back} bulan terakhir")
    report.append("")
    report.append("---")
    report.append("")

    # Ringkasan Follower
    report.append("## Ringkasan Follower")
    report.append("")
    report.append("| No | Akun Instagram | Institusi | Followers | Posts | Sumber |")
    report.append("|:--:|----------------|-----------|----------:|------:|:------:|")

    for i, res in enumerate(all_results, 1):
        acc = res["account"]
        data = res["data"]
        username_link = f"[@{acc['username']}](https://www.instagram.com/{acc['username']}/)"
        if data is None:
            report.append(f"| {i} | {username_link} | {acc['nama']} | - | - | ❌ |")
        else:
            followers = data.get("followers")
            posts_total = data.get("posts_total")
            if followers is None and data.get("followers_str"):
                followers = data["followers_str"]
                posts_total = data.get("posts_str", "-")
            followers_str = f"{followers:,}" if isinstance(followers, int) else str(followers or "-")
            posts_str = f"{posts_total:,}" if isinstance(posts_total, int) else str(posts_total or "-")
            report.append(f"| {i} | {username_link} | {acc['nama']} | {followers_str} | {posts_str} | {res['source']} |")

    report.append("")
    report.append("---")
    report.append("")

    # Tabel Analisis Topik
    report.append(f"## Analisis Topik Postingan ({months_back} Bulan Terakhir)")
    report.append("")
    report.append("Jumlah postingan yang memuat informasi tentang topik berikut:")
    report.append("")

    header = "| Akun |"
    sep = "|------|"
    for topic in TOPICS.keys():
        # Singkat header
        short = topic.replace(" Lulusan", "").replace(" dan Pengabdian", "/Pengabdian")
        header += f" {short} | "
        sep += ":-:|"
    header += " Total Post |"
    sep += ":-:|"

    report.append(header)
    report.append(sep)

    for res in all_results:
        acc = res["account"]
        data = res["data"]
        row = f"| @{acc['username']} |"
        if data is None or not data.get("recent_posts"):
            for _ in TOPICS:
                row += " - |"
            row += " - |"
        else:
            counts = aggregate_topics(data["recent_posts"])
            for topic in TOPICS.keys():
                c = counts[topic]
                row += f" {c if c > 0 else '-'} |"
            row += f" {len(data['recent_posts'])} |"
        report.append(row)

    report.append("")
    report.append("---")
    report.append("")

    # Detail per akun
    report.append("## Detail per Akun")
    report.append("")

    for res in all_results:
        acc = res["account"]
        data = res["data"]
        report.append(f"### @{acc['username']} - {acc['nama']}")
        report.append("")

        if data is None:
            report.append(f"- **Status:** ❌ Tidak dapat fetch data")
            report.append(f"- **Error:** `{res['error']}`")
            report.append("")
            continue

        if data.get("full_name"):
            report.append(f"- **Nama:** {data['full_name']}")
        if data.get("followers") is not None:
            report.append(f"- **Followers:** {data['followers']:,}")
        if data.get("following") is not None:
            report.append(f"- **Following:** {data['following']:,}")
        if data.get("posts_total") is not None:
            report.append(f"- **Total Posts:** {data['posts_total']:,}")
        if data.get("followers_str"):
            report.append(f"- **Followers (raw):** {data['followers_str']}")
        if data.get("biography"):
            bio_preview = data["biography"][:200].replace("\n", " ")
            report.append(f"- **Bio:** {bio_preview}")
        if data.get("is_private"):
            report.append(f"- **Status:** Akun Private")
        if data.get("note"):
            report.append(f"- **Catatan:** {data['note']}")

        posts = data.get("recent_posts", [])
        report.append(f"- **Postingan dianalisis ({months_back} bulan):** {len(posts)}")

        if posts:
            counts = aggregate_topics(posts)
            report.append("")
            report.append("  **Topik yang dibahas:**")
            report.append("")
            report.append("  | Topik | Jumlah Post |")
            report.append("  |-------|:-----------:|")
            for topic, c in counts.items():
                icon = "✅" if c > 0 else "❌"
                report.append(f"  | {icon} {topic} | {c} |")

        if data.get("posts_error"):
            report.append(f"- **Posts error:** {data['posts_error']}")

        report.append("")

    report.append("---")
    report.append("")

    # Catatan
    report.append("## Catatan Teknis")
    report.append("")
    report.append("- Instagram aktif memblokir scraping dari IP datacenter/cloud (HTTP 403/302).")
    report.append("- Jika dijalankan dari sandbox/cloud, beberapa akun mungkin gagal di-fetch.")
    report.append("- **Untuk hasil terbaik, jalankan dari komputer lokal**.")
    report.append("- Sebagai fallback, edit file `manual_ig_data.json` (lihat contoh di repo) untuk")
    report.append("  memasukkan data follower secara manual.")
    report.append("- Analisis topik dilakukan via keyword matching pada caption postingan.")
    report.append("")
    report.append(f"*Report di-generate otomatis pada {now}*")
    report.append("")

    return "\n".join(report)


def main():
    print("=" * 60)
    print("  INSTAGRAM ACCOUNT CHECKER - UNDIP")
    print("=" * 60)
    print(f"\nWaktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Jumlah akun: {len(ACCOUNTS)}")

    if not HAS_INSTALOADER:
        print("\n[WARN] Library 'instaloader' tidak terinstall.")
        print("       Jalankan: pip install instaloader")

    manual_data = load_manual_data()
    if manual_data:
        print(f"\n[INFO] Manual data tersedia untuk: {list(manual_data.keys())}")

    all_results = []
    for acc in ACCOUNTS:
        result = check_account(acc, manual_data)
        all_results.append(result)

    report_content = generate_report(all_results)
    report_path = os.path.join(os.path.dirname(__file__) or ".", "instagram_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n" + "=" * 60)
    print(f"Report tersimpan di: {report_path}")
    print("=" * 60)

    success = sum(1 for r in all_results if r["data"] is not None)
    print(f"\nBerhasil: {success}/{len(all_results)} akun")


if __name__ == "__main__":
    main()
