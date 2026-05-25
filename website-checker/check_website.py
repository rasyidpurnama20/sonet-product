#!/usr/bin/env python3
"""
Website Completeness Checker
Mengecek kelengkapan elemen-elemen penting pada website institusi UNDIP.

Pengecekan meliputi:
1. Kelengkapan elemen UI standar (logo, navigasi, footer, dll.)
2. Kelengkapan konten setiap menu (non-kosong / update)
3. Topik berita yang dimuat (prospek kerja, alumni, kurikulum, dll.)
"""

import re
import sys
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# Daftar website yang akan dicek
WEBSITES = [
    {"url": "https://fsm.undip.ac.id/", "nama": "Fakultas Sains dan Matematika"},
    {"url": "https://math.undip.ac.id/", "nama": "Departemen Matematika"},
    {"url": "https://bio.undip.ac.id/", "nama": "Departemen Biologi"},
    {"url": "https://fisika.undip.ac.id/", "nama": "Departemen Fisika"},
    {"url": "https://kimia.undip.ac.id/", "nama": "Departemen Kimia"},
    {"url": "https://stat.undip.ac.id/", "nama": "Departemen Statistika"},
    {"url": "https://if.undip.ac.id/", "nama": "Departemen Informatika"},
    {"url": "https://biotek.undip.ac.id/", "nama": "Departemen Bioteknologi"},
]

# Kriteria pengecekan halaman utama
CRITERIA = [
    "Logo",
    "Navigasi",
    "Nama Institusi",
    "Kontak",
    "Media Sosial",
    "Footer",
    "Berita/Artikel",
    "Banner/Hero Image",
    "Search",
    "Responsive Meta",
    "SSL/HTTPS",
    "Favicon",
    "Akreditasi/Visi-Misi",
    "Link Akademik",
    "Meta Description",
]

# Topik yang dicari di konten berita / website
TOPICS = {
    "Prospek Kerja Lulusan": [
        "prospek kerja", "lapangan kerja", "peluang kerja", "career",
        "karir", "dunia kerja", "career opportunity", "tracer study",
        "industri", "alumni bekerja"
    ],
    "Alumni": [
        "alumni", "alumnus", "wisuda", "wisudawan", "ikatan alumni",
        "iluni", "tracer", "reuni alumni"
    ],
    "Kurikulum": [
        "kurikulum", "curriculum", "mata kuliah", "matkul", "silabus",
        "syllabus", "rps", "sks", "struktur kurikulum"
    ],
    "Pendaftaran": [
        "pendaftaran", "penerimaan", "snbp", "snbt", "um undip", "um-undip",
        "calon mahasiswa", "calon mahasiswa baru", "info pendaftaran",
        "pmb", "registration", "open recruitment"
    ],
    "Fasilitas": [
        "fasilitas", "facility", "laboratorium", "ruang kuliah", "ruang kelas",
        "perpustakaan", "library", "sarana prasarana", "sarana dan prasarana"
    ],
    "Prestasi": [
        "prestasi", "juara", "achievement", "winner", "menang", "medali",
        "champion", "lomba", "kompetisi", "olimpiade", "penghargaan",
        "best paper", "runner up"
    ],
    "Riset dan Pengabdian": [
        "riset", "penelitian", "research", "publikasi", "publication",
        "jurnal", "journal", "pengabdian", "p2m", "abdimas",
        "pengabdian masyarakat", "pkm "
    ],
}

# Konfigurasi crawl
MAX_MENU_LINKS = 12         # Jumlah menu maksimum yang dicek
MAX_NEWS_LINKS = 10         # Jumlah berita maksimum yang dianalisis topiknya
MIN_CONTENT_CHARS = 200     # Minimum karakter agar dianggap "tidak kosong"
REQUEST_TIMEOUT = 15


def fetch_page(url, timeout=REQUEST_TIMEOUT):
    """Fetch halaman website dan return BeautifulSoup object."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout, verify=True)
        response.raise_for_status()
        return response, BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.SSLError:
        try:
            response = requests.get(url, headers=headers, timeout=timeout, verify=False)
            return response, BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            return None, None
    except Exception as e:
        return None, None


# ==================== CEK ELEMEN HALAMAN UTAMA ====================

def check_logo(soup):
    if soup.find_all("img", attrs={"src": re.compile(r"logo", re.I)}):
        return True
    if soup.find_all("img", attrs={"alt": re.compile(r"logo", re.I)}):
        return True
    if soup.find_all("img", attrs={"class": re.compile(r"logo", re.I)}):
        return True
    if soup.find(attrs={"class": re.compile(r"logo", re.I)}):
        return True
    if soup.find(attrs={"id": re.compile(r"logo", re.I)}):
        return True
    return False


def check_navigation(soup):
    if soup.find("nav"):
        return True
    if soup.find(attrs={"class": re.compile(r"(nav|menu|navbar)", re.I)}):
        return True
    if soup.find(attrs={"id": re.compile(r"(nav|menu|navbar)", re.I)}):
        return True
    for ul in soup.find_all("ul"):
        if len(ul.find_all("a")) >= 4:
            return True
    return False


def check_institution_name(soup, nama):
    text = soup.get_text().lower()
    for kw in ["fakultas", "departemen", "program studi", "undip", "diponegoro"]:
        if kw in text:
            return True
    if nama.lower().split()[-1] in text:
        return True
    return False


def check_contact(soup):
    text = soup.get_text().lower()
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", soup.get_text()):
        return True
    for kw in ["telp", "telepon", "phone", "tel:", "fax", "(024)", "+62"]:
        if kw in text:
            return True
    for kw in ["jl.", "jalan", "alamat", "semarang", "tembalang"]:
        if kw in text:
            return True
    return False


def check_social_media(soup):
    patterns = ["facebook.com", "fb.com", "twitter.com", "x.com",
                "instagram.com", "youtube.com", "linkedin.com", "tiktok.com"]
    for link in soup.find_all("a", href=True):
        href = link["href"].lower()
        for p in patterns:
            if p in href:
                return True
    if soup.find_all(attrs={"class": re.compile(
            r"(facebook|twitter|instagram|youtube|linkedin|social|fa-facebook|fa-twitter|fa-instagram)", re.I)}):
        return True
    return False


def check_footer(soup):
    if soup.find("footer"):
        return True
    if soup.find(attrs={"class": re.compile(r"footer", re.I)}):
        return True
    if soup.find(attrs={"id": re.compile(r"footer", re.I)}):
        return True
    return False


def check_news(soup):
    text = soup.get_text().lower()
    for kw in ["berita", "news", "artikel", "article", "pengumuman",
               "agenda", "kegiatan", "event"]:
        if kw in text:
            return True
    if soup.find(attrs={"class": re.compile(r"(news|berita|article|post|blog|pengumuman)", re.I)}):
        return True
    return False


def check_banner(soup):
    if soup.find(attrs={"class": re.compile(
            r"(slider|carousel|hero|banner|swiper|slide)", re.I)}):
        return True
    if soup.find(attrs={"id": re.compile(r"(slider|carousel|hero|banner)", re.I)}):
        return True
    for img in soup.find_all("img"):
        src = img.get("src", "").lower()
        if any(kw in src for kw in ["banner", "hero", "slide", "header"]):
            return True
    return False


def check_search(soup):
    if soup.find("input", attrs={"type": "search"}):
        return True
    if soup.find("input", attrs={"name": re.compile(r"(search|q|s|query|keyword)", re.I)}):
        return True
    if soup.find("input", attrs={"placeholder": re.compile(r"(cari|search|telusuri)", re.I)}):
        return True
    if soup.find("form", attrs={"action": re.compile(r"search", re.I)}):
        return True
    if soup.find("form", attrs={"class": re.compile(r"search", re.I)}):
        return True
    if soup.find(attrs={"class": re.compile(
            r"(fa-search|search-icon|icon-search|bi-search)", re.I)}):
        return True
    return False


def check_responsive(soup):
    return soup.find("meta", attrs={"name": "viewport"}) is not None


def check_ssl(url):
    return url.startswith("https://")


def check_favicon(soup):
    if soup.find("link", attrs={"rel": re.compile(r"(icon|shortcut)", re.I)}):
        return True
    if soup.find("link", attrs={"href": re.compile(r"favicon", re.I)}):
        return True
    return False


def check_accreditation(soup):
    text = soup.get_text().lower()
    for kw in ["akreditasi", "visi", "misi", "unggul", "terakreditasi",
               "ban-pt", "abet", "asiin", "sertifikasi"]:
        if kw in text:
            return True
    return False


def check_academic_links(soup):
    text = soup.get_text().lower()
    keywords = ["sia", "e-learning", "elearning", "kurikulum", "akademik",
                "academic", "sso", "kuliah", "jadwal", "siap", "herregistrasi"]
    for kw in keywords:
        if kw in text:
            return True
    for link in soup.find_all("a", href=True):
        href = link.get("href", "").lower()
        for kw in keywords:
            if kw in href:
                return True
    return False


def check_meta_description(soup):
    md = soup.find("meta", attrs={"name": "description"})
    if md and md.get("content", "").strip():
        return True
    od = soup.find("meta", attrs={"property": "og:description"})
    if od and od.get("content", "").strip():
        return True
    return False


# ==================== CEK MENU & KONTEN ====================

def extract_menu_links(soup, base_url):
    """Ekstrak link menu utama dari navigasi."""
    base_domain = urlparse(base_url).netloc
    menu_links = []
    seen = set()

    # Cari menu utama (nav, header menu)
    nav_candidates = []
    for el in soup.find_all("nav"):
        nav_candidates.append(el)
    for el in soup.find_all(attrs={"class": re.compile(
            r"(main-menu|primary-menu|navbar|nav-menu|menu-main)", re.I)}):
        nav_candidates.append(el)
    for el in soup.find_all(attrs={"id": re.compile(
            r"(main-menu|primary-menu|navbar|nav-menu|menu-main)", re.I)}):
        nav_candidates.append(el)

    if not nav_candidates:
        # Fallback: ambil ul terbesar
        uls = soup.find_all("ul")
        if uls:
            nav_candidates = [max(uls, key=lambda u: len(u.find_all("a")))]

    for nav in nav_candidates:
        for a in nav.find_all("a", href=True):
            href = a["href"].strip()
            text = a.get_text(strip=True)
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            if not text or len(text) < 2:
                continue
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            # Hanya same-domain
            if parsed.netloc and parsed.netloc != base_domain:
                continue
            # Skip URL yang sama dengan base
            normalized = full_url.split("#")[0].rstrip("/")
            if normalized == base_url.rstrip("/"):
                continue
            if normalized in seen:
                continue
            seen.add(normalized)
            # Skip file download (pdf, doc, dll)
            if re.search(r"\.(pdf|doc|docx|xls|xlsx|ppt|pptx|zip|rar)$", full_url, re.I):
                continue
            menu_links.append({"text": text, "url": full_url})
            if len(menu_links) >= MAX_MENU_LINKS:
                return menu_links
    return menu_links


def get_main_content_text(soup):
    """Ambil teks dari area konten utama (exclude header/footer/nav/script)."""
    soup_copy = BeautifulSoup(str(soup), "html.parser")
    # Hapus elemen non-konten secara konservatif
    for tag in soup_copy.find_all(["script", "style", "noscript", "nav", "header", "footer"]):
        tag.decompose()

    # Coba temukan area konten utama
    candidates = []
    # 1. <main> tag
    m = soup_copy.find("main")
    if m:
        candidates.append(m)
    # 2. <article> tag
    a = soup_copy.find("article")
    if a:
        candidates.append(a)
    # 3. div dengan id/class yang mengindikasikan konten
    for sel_attr in ["id", "class"]:
        for el in soup_copy.find_all(attrs={sel_attr: re.compile(
                r"\b(content|main-content|page-content|post-content|entry-content|article-content|site-content|primary)\b",
                re.I)}):
            candidates.append(el)

    # Pilih kandidat dengan teks terpanjang
    best = None
    best_len = 0
    for c in candidates:
        t = c.get_text(strip=True)
        if len(t) > best_len:
            best_len = len(t)
            best = c

    target = best if best else soup_copy.find("body") or soup_copy
    text = re.sub(r"\s+", " ", target.get_text(" ", strip=True))
    return text


def check_menu_content(menu_links):
    """Cek apakah konten setiap menu tidak kosong."""
    results = []
    for link in menu_links:
        url = link["url"]
        resp, soup = fetch_page(url, timeout=10)
        if soup is None:
            results.append({
                "text": link["text"],
                "url": url,
                "status": "error",
                "content_chars": 0,
                "is_empty": True,
            })
            continue

        text = get_main_content_text(soup)
        chars = len(text)
        is_empty = chars < MIN_CONTENT_CHARS
        results.append({
            "text": link["text"],
            "url": url,
            "status": "ok",
            "content_chars": chars,
            "is_empty": is_empty,
        })
    return results


# ==================== CEK BERITA & TOPIK ====================

def find_news_links(soup, base_url):
    """Cari link ke berita / artikel."""
    base_domain = urlparse(base_url).netloc
    news_links = []
    seen = set()

    # Cari elemen yang kemungkinan adalah berita
    candidates = soup.find_all(attrs={"class": re.compile(
        r"(news|berita|article|post|blog|entry|item)", re.I)})

    for c in candidates:
        for a in c.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            if parsed.netloc and parsed.netloc != base_domain:
                continue
            normalized = full_url.split("#")[0].rstrip("/")
            if normalized in seen or normalized == base_url.rstrip("/"):
                continue
            # Skip file
            if re.search(r"\.(pdf|doc|docx|jpg|jpeg|png|gif)$", full_url, re.I):
                continue
            seen.add(normalized)
            text = a.get_text(strip=True)
            if len(text) < 10:  # judul terlalu pendek
                continue
            news_links.append({"title": text, "url": full_url})
            if len(news_links) >= MAX_NEWS_LINKS:
                return news_links
    return news_links


def analyze_text_topics(text):
    """Cari topik mana saja yang ada di text."""
    text_lower = text.lower()
    found = []
    for topic, keywords in TOPICS.items():
        for kw in keywords:
            if kw in text_lower:
                found.append(topic)
                break
    return found


def check_news_topics(news_links, homepage_text=""):
    """Untuk setiap berita, fetch dan analisis topiknya."""
    topic_counts = {topic: 0 for topic in TOPICS.keys()}
    news_details = []
    dates_found = []

    # Hitung dari homepage juga (judul berita biasanya ada di homepage)
    for topic in analyze_text_topics(homepage_text):
        topic_counts[topic] += 0  # akan dihitung dari berita individu

    for link in news_links:
        resp, soup = fetch_page(link["url"], timeout=10)
        if soup is None:
            news_details.append({
                "title": link["title"],
                "url": link["url"],
                "topics": [],
                "date": None,
                "status": "error",
            })
            continue
        text = get_main_content_text(soup)
        topics = analyze_text_topics(link["title"] + " " + text)
        for t in topics:
            topic_counts[t] += 1

        # Coba ekstrak tanggal
        date = extract_date(soup, text)
        if date:
            dates_found.append(date)

        news_details.append({
            "title": link["title"],
            "url": link["url"],
            "topics": topics,
            "date": date,
            "status": "ok",
        })

    return topic_counts, news_details, dates_found


def extract_date(soup, text):
    """Coba ekstrak tanggal posting berita."""
    # Cek meta tag
    for prop in ["article:published_time", "og:updated_time"]:
        m = soup.find("meta", attrs={"property": prop})
        if m and m.get("content"):
            try:
                return m["content"][:10]
            except Exception:
                pass
    # Cek time tag
    t = soup.find("time")
    if t:
        if t.get("datetime"):
            return t["datetime"][:10]
        if t.get_text(strip=True):
            return t.get_text(strip=True)[:30]
    # Pattern tanggal Indonesia
    months = ("januari|februari|maret|april|mei|juni|juli|agustus|"
              "september|oktober|november|desember")
    m = re.search(rf"(\d{{1,2}})\s+({months})\s+(\d{{4}})", text, re.I)
    if m:
        return f"{m.group(1)} {m.group(2)} {m.group(3)}"
    # Pattern YYYY-MM-DD
    m = re.search(r"\b(20\d{2})-(\d{2})-(\d{2})\b", text)
    if m:
        return m.group(0)
    return None


def is_news_recent(dates_found, months=6):
    """Cek apakah ada berita dalam X bulan terakhir."""
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=months * 30)
    months_id = {
        "januari": 1, "februari": 2, "maret": 3, "april": 4, "mei": 5,
        "juni": 6, "juli": 7, "agustus": 8, "september": 9,
        "oktober": 10, "november": 11, "desember": 12,
    }
    for d in dates_found:
        try:
            # Format YYYY-MM-DD
            m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
            if m:
                dt = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                if dt > cutoff:
                    return True, d
                continue
            # Format Indonesia
            for name, num in months_id.items():
                m = re.search(rf"(\d{{1,2}})\s+{name}\s+(\d{{4}})", d, re.I)
                if m:
                    dt = datetime(int(m.group(2)), num, int(m.group(1)))
                    if dt > cutoff:
                        return True, d
                    break
        except Exception:
            continue
    return False, None


# ==================== MAIN CHECK ====================

def check_website(site):
    """Jalankan semua pengecekan untuk satu website."""
    url = site["url"]
    nama = site["nama"]
    print(f"\n[{nama}] {url}")

    response, soup = fetch_page(url)

    if soup is None:
        print(f"  ERROR: Tidak dapat akses website")
        return {
            "url": url, "nama": nama, "accessible": False,
            "results": {c: False for c in CRITERIA}, "score": 0,
            "menu_results": [], "topic_counts": {t: 0 for t in TOPICS.keys()},
            "news_details": [], "news_recent": False, "latest_news_date": None,
            "error": "Tidak dapat diakses",
        }

    print(f"  Status: {response.status_code}")

    # 1. Cek elemen halaman utama
    results = {
        "Logo": check_logo(soup),
        "Navigasi": check_navigation(soup),
        "Nama Institusi": check_institution_name(soup, nama),
        "Kontak": check_contact(soup),
        "Media Sosial": check_social_media(soup),
        "Footer": check_footer(soup),
        "Berita/Artikel": check_news(soup),
        "Banner/Hero Image": check_banner(soup),
        "Search": check_search(soup),
        "Responsive Meta": check_responsive(soup),
        "SSL/HTTPS": check_ssl(url),
        "Favicon": check_favicon(soup),
        "Akreditasi/Visi-Misi": check_accreditation(soup),
        "Link Akademik": check_academic_links(soup),
        "Meta Description": check_meta_description(soup),
    }
    score = sum(1 for v in results.values() if v) / len(results) * 100
    print(f"  Skor elemen: {score:.0f}%")

    # 2. Cek menu & konten
    print(f"  Menelusuri menu...")
    menu_links = extract_menu_links(soup, url)
    print(f"    Menemukan {len(menu_links)} menu, mengecek konten...")
    menu_results = check_menu_content(menu_links)
    empty_count = sum(1 for m in menu_results if m["is_empty"])
    print(f"    Menu dengan konten kosong/error: {empty_count}/{len(menu_results)}")

    # 3. Cek berita & topik
    print(f"  Menganalisis berita...")
    news_links = find_news_links(soup, url)
    homepage_text = get_main_content_text(soup)
    topic_counts, news_details, dates = check_news_topics(news_links, homepage_text)
    news_recent, latest_date = is_news_recent(dates)
    topics_present = sum(1 for c in topic_counts.values() if c > 0)
    print(f"    Berita dianalisis: {len(news_details)}, topik terdeteksi: {topics_present}/{len(TOPICS)}")
    if latest_date:
        print(f"    Berita terbaru terdeteksi: {latest_date}")

    return {
        "url": url, "nama": nama, "accessible": True,
        "results": results, "score": score,
        "status_code": response.status_code,
        "menu_results": menu_results,
        "topic_counts": topic_counts,
        "news_details": news_details,
        "news_recent": news_recent,
        "latest_news_date": latest_date,
    }


# ==================== REPORT GENERATION ====================

def generate_report(all_results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = []
    report.append("# Laporan Kelengkapan Website UNDIP")
    report.append("")
    report.append(f"**Tanggal Pengecekan:** {now}")
    report.append("")
    report.append(f"**Jumlah Website:** {len(all_results)}")
    report.append("")
    report.append("---")
    report.append("")

    # ===== Ringkasan Skor =====
    report.append("## 1. Ringkasan Skor Kelengkapan Elemen")
    report.append("")
    report.append("| No | Website | Institusi | Skor | Status |")
    report.append("|:--:|---------|-----------|:----:|:------:|")
    for i, r in enumerate(all_results, 1):
        if not r["accessible"]:
            report.append(f"| {i} | {r['url']} | {r['nama']} | - | Tidak Dapat Diakses |")
        else:
            score = r["score"]
            status = "Baik" if score >= 80 else ("Cukup" if score >= 60 else "Kurang")
            report.append(f"| {i} | {r['url']} | {r['nama']} | {score:.0f}% | {status} |")
    report.append("")
    report.append("---")
    report.append("")

    # ===== Detail Kelengkapan Elemen =====
    report.append("## 2. Detail Kelengkapan Elemen UI")
    report.append("")
    short_names = []
    header = "| Kriteria |"
    sep = "|----------|"
    for r in all_results:
        short = r["url"].replace("https://", "").replace("http://", "").split(".")[0].upper()
        short_names.append(short)
        header += f" {short} |"
        sep += ":---:|"
    report.append(header)
    report.append(sep)
    for criterion in CRITERIA:
        row = f"| {criterion} |"
        for r in all_results:
            if not r["accessible"]:
                row += " - |"
            elif r["results"].get(criterion, False):
                row += " Y |"
            else:
                row += " N |"
        report.append(row)
    report.append("")
    report.append("---")
    report.append("")

    # ===== Cek Konten Menu =====
    report.append("## 3. Cek Konten Setiap Menu")
    report.append("")
    report.append("Pengecekan apakah halaman setiap menu memiliki konten (tidak kosong / dapat diakses).")
    report.append(f"Threshold konten minimum: {MIN_CONTENT_CHARS} karakter.")
    report.append("")
    report.append("### 3.1 Ringkasan Menu per Website")
    report.append("")
    report.append("| Website | Total Menu Dicek | Konten OK | Kosong/Error |")
    report.append("|---------|:----------------:|:---------:|:------------:|")
    for r in all_results:
        if not r["accessible"]:
            report.append(f"| {r['nama']} | - | - | - |")
            continue
        total = len(r["menu_results"])
        empty = sum(1 for m in r["menu_results"] if m["is_empty"])
        ok = total - empty
        report.append(f"| {r['nama']} | {total} | {ok} | {empty} |")
    report.append("")

    report.append("### 3.2 Detail Menu per Website")
    report.append("")
    for r in all_results:
        if not r["accessible"]:
            continue
        report.append(f"#### {r['nama']} (`{r['url']}`)")
        report.append("")
        if not r["menu_results"]:
            report.append("> Tidak ada menu yang berhasil diekstrak dari navigasi.")
            report.append("")
            continue
        report.append("| Menu | URL | Status | Karakter Konten |")
        report.append("|------|-----|:------:|----------------:|")
        for m in r["menu_results"]:
            status_icon = "OK" if (m["status"] == "ok" and not m["is_empty"]) else (
                "KOSONG" if m["status"] == "ok" else "ERROR")
            url_short = m["url"]
            if len(url_short) > 60:
                url_short = url_short[:57] + "..."
            menu_text = m["text"][:40]
            report.append(f"| {menu_text} | [{url_short}]({m['url']}) | {status_icon} | {m['content_chars']} |")
        report.append("")

    report.append("---")
    report.append("")

    # ===== Analisis Topik Berita =====
    report.append("## 4. Analisis Topik pada Berita")
    report.append("")
    report.append("Pengecekan apakah berita/artikel website memuat topik berikut:")
    report.append("- Prospek Kerja Lulusan")
    report.append("- Alumni")
    report.append("- Kurikulum")
    report.append("- Pendaftaran")
    report.append("- Fasilitas")
    report.append("- Prestasi")
    report.append("- Riset dan Pengabdian")
    report.append("")
    report.append("### 4.1 Ringkasan Topik per Website")
    report.append("")
    header = "| Website |"
    sep = "|---------|"
    for topic in TOPICS.keys():
        short = topic.replace(" Lulusan", "").replace(" dan Pengabdian", "/Pengabdian")
        header += f" {short} |"
        sep += ":-:|"
    header += " Berita Update |"
    sep += ":-:|"
    report.append(header)
    report.append(sep)
    for r in all_results:
        if not r["accessible"]:
            continue
        row = f"| {r['nama']} |"
        for topic in TOPICS.keys():
            c = r["topic_counts"].get(topic, 0)
            row += f" {c if c > 0 else '-'} |"
        recent_str = "Y" if r["news_recent"] else ("?" if not r["latest_news_date"] else "N")
        if r["latest_news_date"]:
            recent_str += f" ({r['latest_news_date']})"
        row += f" {recent_str} |"
        report.append(row)
    report.append("")
    report.append("> Angka = jumlah berita yang memuat topik tersebut.  ")
    report.append("> Berita Update: Y = ada berita dalam 6 bulan terakhir, N = tidak ada, ? = tanggal tidak terdeteksi.")
    report.append("")

    report.append("### 4.2 Detail Berita per Website")
    report.append("")
    for r in all_results:
        if not r["accessible"]:
            continue
        report.append(f"#### {r['nama']}")
        report.append("")
        if not r["news_details"]:
            report.append("> Tidak ada link berita yang berhasil diekstrak.")
            report.append("")
            continue
        report.append("| Judul | Tanggal | Topik Terdeteksi |")
        report.append("|-------|---------|------------------|")
        for n in r["news_details"][:10]:
            title = n["title"][:60] + ("..." if len(n["title"]) > 60 else "")
            date = n["date"] or "-"
            topics = ", ".join(n["topics"]) if n["topics"] else "-"
            report.append(f"| [{title}]({n['url']}) | {date} | {topics} |")
        report.append("")

    report.append("---")
    report.append("")

    # ===== Legenda =====
    report.append("## 5. Legenda")
    report.append("")
    report.append("| Simbol | Keterangan |")
    report.append("|:------:|------------|")
    report.append("| Y | Elemen ditemukan / Tersedia |")
    report.append("| N | Elemen tidak ditemukan |")
    report.append("| OK | Konten halaman tersedia (>= 200 karakter) |")
    report.append("| KOSONG | Halaman dapat diakses tapi konten kurang |")
    report.append("| ERROR | Halaman tidak dapat diakses |")
    report.append("")
    report.append("---")
    report.append("")

    # ===== Rekomendasi =====
    report.append("## 6. Rekomendasi")
    report.append("")
    for r in all_results:
        if not r["accessible"]:
            report.append(f"### {r['nama']} ({r['url']})")
            report.append(f"- Website tidak dapat diakses saat pengecekan.")
            report.append("")
            continue

        recommendations = []
        missing_elem = [k for k, v in r["results"].items() if not v]
        if missing_elem:
            recommendations.append(f"**Elemen UI belum lengkap:** {', '.join(missing_elem)}")

        empty_menus = [m["text"] for m in r["menu_results"] if m["is_empty"]]
        if empty_menus:
            recommendations.append(f"**Menu konten kosong/error:** {', '.join(empty_menus[:5])}")

        missing_topics = [t for t, c in r["topic_counts"].items() if c == 0]
        if missing_topics:
            recommendations.append(f"**Topik berita belum dimuat:** {', '.join(missing_topics)}")

        if not r["news_recent"] and r["latest_news_date"]:
            recommendations.append(f"**Berita kurang update.** Berita terbaru terdeteksi: {r['latest_news_date']}")

        if recommendations:
            report.append(f"### {r['nama']} ({r['url']})")
            report.append(f"- Skor elemen: {r['score']:.0f}%")
            for rec in recommendations:
                report.append(f"- {rec}")
            report.append("")

    report.append("---")
    report.append("")
    report.append(f"*Report di-generate otomatis oleh Website Completeness Checker pada {now}*")
    report.append("")
    return "\n".join(report)


def main():
    print("=" * 60)
    print("  WEBSITE COMPLETENESS CHECKER - UNDIP")
    print("=" * 60)
    print(f"\nWaktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Jumlah website: {len(WEBSITES)}")

    all_results = []
    for site in WEBSITES:
        try:
            result = check_website(site)
        except Exception as e:
            print(f"  EXCEPTION: {type(e).__name__}: {e}")
            result = {
                "url": site["url"], "nama": site["nama"], "accessible": False,
                "results": {c: False for c in CRITERIA}, "score": 0,
                "menu_results": [], "topic_counts": {t: 0 for t in TOPICS.keys()},
                "news_details": [], "news_recent": False, "latest_news_date": None,
                "error": str(e),
            }
        all_results.append(result)

    report_content = generate_report(all_results)
    import os
    report_path = os.path.join(os.path.dirname(__file__) or ".", "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n" + "=" * 60)
    print(f"Report tersimpan di: {report_path}")
    print("=" * 60)

    accessible = sum(1 for r in all_results if r["accessible"])
    avg_score = sum(r["score"] for r in all_results if r["accessible"])
    if accessible > 0:
        avg_score /= accessible
    print(f"\nRata-rata skor elemen: {avg_score:.0f}% ({accessible}/{len(all_results)} dapat diakses)")


if __name__ == "__main__":
    main()
