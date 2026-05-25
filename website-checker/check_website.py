#!/usr/bin/env python3
"""
Website Completeness Checker
Mengecek kelengkapan elemen-elemen penting pada website institusi UNDIP.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import sys

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

# Kriteria pengecekan
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


def fetch_page(url, timeout=15):
    """Fetch halaman website dan return BeautifulSoup object."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=timeout, verify=True)
        response.raise_for_status()
        return response, BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.SSLError:
        try:
            response = requests.get(url, headers=headers, timeout=timeout, verify=False)
            return response, BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            print(f"  [ERROR] Gagal fetch {url}: {e}")
            return None, None
    except Exception as e:
        print(f"  [ERROR] Gagal fetch {url}: {e}")
        return None, None


def check_logo(soup):
    """Cek keberadaan logo (img di header atau dengan class/id logo)."""
    # Cek img dengan kata 'logo' di class, id, alt, atau src
    logos = soup.find_all("img", attrs={"src": re.compile(r"logo", re.I)})
    if logos:
        return True
    logos = soup.find_all("img", attrs={"alt": re.compile(r"logo", re.I)})
    if logos:
        return True
    logos = soup.find_all("img", attrs={"class": re.compile(r"logo", re.I)})
    if logos:
        return True
    # Cek elemen dengan class/id logo
    logo_el = soup.find(attrs={"class": re.compile(r"logo", re.I)})
    if logo_el:
        return True
    logo_el = soup.find(attrs={"id": re.compile(r"logo", re.I)})
    if logo_el:
        return True
    return False


def check_navigation(soup):
    """Cek keberadaan menu navigasi."""
    nav = soup.find("nav")
    if nav:
        return True
    # Cek elemen dengan class/id menu atau navbar
    menu = soup.find(attrs={"class": re.compile(r"(nav|menu|navbar)", re.I)})
    if menu:
        return True
    menu = soup.find(attrs={"id": re.compile(r"(nav|menu|navbar)", re.I)})
    if menu:
        return True
    # Cek ul dengan beberapa li > a (pattern menu)
    uls = soup.find_all("ul")
    for ul in uls:
        links = ul.find_all("a")
        if len(links) >= 4:
            return True
    return False


def check_institution_name(soup, nama):
    """Cek keberadaan nama institusi di halaman."""
    text = soup.get_text().lower()
    # Cek kata kunci umum
    keywords = ["fakultas", "departemen", "program studi", "undip", "diponegoro"]
    for kw in keywords:
        if kw in text:
            return True
    # Cek nama spesifik
    if nama.lower().split()[-1] in text:
        return True
    return False


def check_contact(soup):
    """Cek keberadaan informasi kontak."""
    text = soup.get_text().lower()
    # Cek email pattern
    email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
    if email_pattern.search(soup.get_text()):
        return True
    # Cek telepon pattern
    phone_keywords = ["telp", "telepon", "phone", "tel:", "fax", "(024)", "+62"]
    for kw in phone_keywords:
        if kw in text:
            return True
    # Cek alamat
    address_keywords = ["jl.", "jalan", "alamat", "semarang", "tembalang"]
    for kw in address_keywords:
        if kw in text:
            return True
    return False


def check_social_media(soup):
    """Cek keberadaan link media sosial."""
    social_patterns = [
        "facebook.com", "fb.com",
        "twitter.com", "x.com",
        "instagram.com",
        "youtube.com",
        "linkedin.com",
        "tiktok.com",
    ]
    links = soup.find_all("a", href=True)
    for link in links:
        href = link["href"].lower()
        for pattern in social_patterns:
            if pattern in href:
                return True
    # Cek icon social media
    social_icons = soup.find_all(attrs={"class": re.compile(r"(facebook|twitter|instagram|youtube|linkedin|social|fa-facebook|fa-twitter|fa-instagram)", re.I)})
    if social_icons:
        return True
    return False


def check_footer(soup):
    """Cek keberadaan footer."""
    footer = soup.find("footer")
    if footer:
        return True
    footer = soup.find(attrs={"class": re.compile(r"footer", re.I)})
    if footer:
        return True
    footer = soup.find(attrs={"id": re.compile(r"footer", re.I)})
    if footer:
        return True
    return False


def check_news(soup):
    """Cek keberadaan section berita/artikel."""
    text = soup.get_text().lower()
    news_keywords = ["berita", "news", "artikel", "article", "pengumuman", "announcement", "agenda", "kegiatan", "event"]
    for kw in news_keywords:
        if kw in text:
            return True
    # Cek elemen dengan class berita/news
    news_el = soup.find(attrs={"class": re.compile(r"(news|berita|article|post|blog|pengumuman)", re.I)})
    if news_el:
        return True
    return False


def check_banner(soup):
    """Cek keberadaan banner/hero image/slider."""
    # Cek slider/carousel
    slider = soup.find(attrs={"class": re.compile(r"(slider|carousel|hero|banner|swiper|slide)", re.I)})
    if slider:
        return True
    slider = soup.find(attrs={"id": re.compile(r"(slider|carousel|hero|banner)", re.I)})
    if slider:
        return True
    # Cek img besar di awal halaman
    imgs = soup.find_all("img")
    for img in imgs:
        src = img.get("src", "").lower()
        if any(kw in src for kw in ["banner", "hero", "slide", "header"]):
            return True
    return False


def check_search(soup):
    """Cek keberadaan fitur pencarian."""
    # Cek input search
    search_input = soup.find("input", attrs={"type": "search"})
    if search_input:
        return True
    search_input = soup.find("input", attrs={"name": re.compile(r"(search|q|s|query|keyword)", re.I)})
    if search_input:
        return True
    search_input = soup.find("input", attrs={"placeholder": re.compile(r"(cari|search|telusuri)", re.I)})
    if search_input:
        return True
    # Cek form search
    search_form = soup.find("form", attrs={"action": re.compile(r"search", re.I)})
    if search_form:
        return True
    search_form = soup.find("form", attrs={"class": re.compile(r"search", re.I)})
    if search_form:
        return True
    # Cek icon search
    search_icon = soup.find(attrs={"class": re.compile(r"(fa-search|search-icon|icon-search|bi-search)", re.I)})
    if search_icon:
        return True
    return False


def check_responsive(soup):
    """Cek keberadaan viewport meta tag."""
    viewport = soup.find("meta", attrs={"name": "viewport"})
    if viewport:
        return True
    return False


def check_ssl(url):
    """Cek apakah website menggunakan HTTPS."""
    return url.startswith("https://")


def check_favicon(soup):
    """Cek keberadaan favicon."""
    favicon = soup.find("link", attrs={"rel": re.compile(r"(icon|shortcut)", re.I)})
    if favicon:
        return True
    favicon = soup.find("link", attrs={"href": re.compile(r"favicon", re.I)})
    if favicon:
        return True
    return False


def check_accreditation(soup):
    """Cek keberadaan info akreditasi atau visi-misi."""
    text = soup.get_text().lower()
    keywords = ["akreditasi", "visi", "misi", "unggul", "terakreditasi", "ban-pt", "abet", "asiin", "sertifikasi"]
    for kw in keywords:
        if kw in text:
            return True
    return False


def check_academic_links(soup):
    """Cek keberadaan link akademik (SIA, e-learning, dll)."""
    text = soup.get_text().lower()
    links = soup.find_all("a", href=True)
    academic_keywords = ["sia", "e-learning", "elearning", "kurikulum", "curriculum",
                         "akademik", "academic", "sso", "undip.ac.id/sia",
                         "kuliah", "jadwal", "siap", "herregistrasi"]
    # Cek di text
    for kw in academic_keywords:
        if kw in text:
            return True
    # Cek di href
    for link in links:
        href = link.get("href", "").lower()
        for kw in academic_keywords:
            if kw in href:
                return True
    return False


def check_meta_description(soup):
    """Cek keberadaan meta description."""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content", "").strip():
        return True
    # Cek og:description sebagai alternatif
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    if og_desc and og_desc.get("content", "").strip():
        return True
    return False


def check_website(site):
    """Jalankan semua pengecekan untuk satu website."""
    url = site["url"]
    nama = site["nama"]
    print(f"\n🔍 Mengecek: {nama} ({url})")

    response, soup = fetch_page(url)

    if soup is None:
        print(f"  ❌ Tidak dapat mengakses website")
        return {
            "url": url,
            "nama": nama,
            "accessible": False,
            "results": {c: False for c in CRITERIA},
            "score": 0,
            "error": "Tidak dapat diakses",
        }

    status_code = response.status_code if response else None
    print(f"  ✅ Status: {status_code}")

    results = {}
    results["Logo"] = check_logo(soup)
    results["Navigasi"] = check_navigation(soup)
    results["Nama Institusi"] = check_institution_name(soup, nama)
    results["Kontak"] = check_contact(soup)
    results["Media Sosial"] = check_social_media(soup)
    results["Footer"] = check_footer(soup)
    results["Berita/Artikel"] = check_news(soup)
    results["Banner/Hero Image"] = check_banner(soup)
    results["Search"] = check_search(soup)
    results["Responsive Meta"] = check_responsive(soup)
    results["SSL/HTTPS"] = check_ssl(url)
    results["Favicon"] = check_favicon(soup)
    results["Akreditasi/Visi-Misi"] = check_accreditation(soup)
    results["Link Akademik"] = check_academic_links(soup)
    results["Meta Description"] = check_meta_description(soup)

    score = sum(1 for v in results.values() if v) / len(results) * 100

    for criterion, status in results.items():
        icon = "✅" if status else "❌"
        print(f"  {icon} {criterion}")

    print(f"  📊 Skor: {score:.0f}%")

    return {
        "url": url,
        "nama": nama,
        "accessible": True,
        "results": results,
        "score": score,
        "status_code": status_code,
    }


def generate_report(all_results):
    """Generate laporan dalam format Markdown."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = []
    report.append("# 📋 Laporan Kelengkapan Website UNDIP")
    report.append("")
    report.append(f"**Tanggal Pengecekan:** {now}")
    report.append("")
    report.append(f"**Jumlah Website:** {len(all_results)}")
    report.append("")
    report.append("---")
    report.append("")

    # Ringkasan Skor
    report.append("## 📊 Ringkasan Skor")
    report.append("")
    report.append("| No | Website | Institusi | Skor | Status |")
    report.append("|:--:|---------|-----------|:----:|:------:|")

    for i, result in enumerate(all_results, 1):
        if not result["accessible"]:
            report.append(f"| {i} | {result['url']} | {result['nama']} | - | ❌ Tidak Dapat Diakses |")
        else:
            score = result["score"]
            if score >= 80:
                status = "🟢 Baik"
            elif score >= 60:
                status = "🟡 Cukup"
            else:
                status = "🔴 Kurang"
            report.append(f"| {i} | {result['url']} | {result['nama']} | {score:.0f}% | {status} |")

    report.append("")
    report.append("---")
    report.append("")

    # Tabel Detail Kelengkapan
    report.append("## 📝 Detail Kelengkapan")
    report.append("")

    # Header tabel
    header = "| Kriteria |"
    separator = "|----------|"
    short_names = []
    for result in all_results:
        # Ambil subdomain sebagai header pendek
        short = result["url"].replace("https://", "").replace("http://", "").split(".")[0].upper()
        short_names.append(short)
        header += f" {short} |"
        separator += ":---:|"

    report.append(header)
    report.append(separator)

    # Isi tabel
    for criterion in CRITERIA:
        row = f"| {criterion} |"
        for result in all_results:
            if not result["accessible"]:
                row += " ⚠️ |"
            elif result["results"].get(criterion, False):
                row += " ✅ |"
            else:
                row += " ❌ |"
        report.append(row)

    report.append("")
    report.append("---")
    report.append("")

    # Legenda
    report.append("## 📖 Legenda")
    report.append("")
    report.append("| Simbol | Keterangan |")
    report.append("|:------:|------------|")
    report.append("| ✅ | Elemen ditemukan |")
    report.append("| ❌ | Elemen tidak ditemukan |")
    report.append("| ⚠️ | Website tidak dapat diakses |")
    report.append("| 🟢 | Skor >= 80% (Baik) |")
    report.append("| 🟡 | Skor 60-79% (Cukup) |")
    report.append("| 🔴 | Skor < 60% (Kurang) |")
    report.append("")
    report.append("---")
    report.append("")

    # Rekomendasi
    report.append("## 💡 Rekomendasi")
    report.append("")

    for result in all_results:
        if not result["accessible"]:
            report.append(f"### {result['nama']} ({result['url']})")
            report.append(f"- ⚠️ Website tidak dapat diakses saat pengecekan")
            report.append("")
            continue

        missing = [k for k, v in result["results"].items() if not v]
        if missing:
            report.append(f"### {result['nama']} ({result['url']})")
            report.append(f"- **Skor:** {result['score']:.0f}%")
            report.append(f"- **Elemen yang perlu ditambahkan:**")
            for m in missing:
                report.append(f"  - {m}")
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
        result = check_website(site)
        all_results.append(result)

    # Generate report
    report_content = generate_report(all_results)

    # Simpan report
    report_path = "report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n" + "=" * 60)
    print(f"📄 Report tersimpan di: {report_path}")
    print("=" * 60)

    # Print ringkasan
    accessible = sum(1 for r in all_results if r["accessible"])
    avg_score = sum(r["score"] for r in all_results if r["accessible"])
    if accessible > 0:
        avg_score /= accessible
    print(f"\n📊 Rata-rata skor: {avg_score:.0f}% ({accessible}/{len(all_results)} website dapat diakses)")


if __name__ == "__main__":
    main()
