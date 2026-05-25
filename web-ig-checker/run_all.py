#!/usr/bin/env python3
"""
run_all.py — Jalankan semua checker sekaligus dan buat combined report.
"""

import os
import sys
import time
from datetime import datetime

print("=" * 60)
print("  WEB + INSTAGRAM CHECKER — FSM UNDIP")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

# ── 1. Website Checker ────────────────────────────────────────────
print("\n[1/2] Menjalankan Website Checker...")
print("─" * 60)

import check_website
check_website.main()

print("\n[2/2] Menjalankan Instagram Checker...")
print("─" * 60)

import check_instagram
check_instagram.main()

# ── 3. Gabungkan ke combined_report.md ───────────────────────────
print("\n[3/3] Menggabungkan laporan...")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sections = [
    f"# 📊 Laporan Gabungan — Website & Instagram FSM UNDIP",
    f"",
    f"**Tanggal:** {now}",
    f"",
    f"Laporan ini menggabungkan hasil pengecekan kelengkapan website dan analisis Instagram.",
    f"Lihat laporan detail di:",
    f"- [website_report.md](website_report.md)",
    f"- [instagram_report.md](instagram_report.md)",
    f"",
    f"---",
    f"",
]

for fname, title in [
    ("website_report.md",   "🌐 Website Report"),
    ("instagram_report.md", "📸 Instagram Report"),
]:
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        # Skip judul utama file karena sudah ada di combined
        lines = content.splitlines()
        # Turunkan heading level (# → ##, ## → ###, dst.) agar tidak clash
        adjusted = []
        for line in lines:
            if line.startswith("# "):
                adjusted.append("## " + line[2:])
            elif line.startswith("## "):
                adjusted.append("### " + line[3:])
            elif line.startswith("### "):
                adjusted.append("#### " + line[4:])
            else:
                adjusted.append(line)
        sections.append("\n".join(adjusted))
        sections.append("\n---\n")
    else:
        sections.append(f"## {title}\n\n_File tidak ditemukan._\n\n---\n")

sections.append(f"_Combined report di-generate pada {now}_\n")

with open("combined_report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(sections))

print("  ✅  combined_report.md tersimpan")
print("\n" + "=" * 60)
print("  SELESAI! File output:")
print("  - website_report.md")
print("  - instagram_report.md")
print("  - combined_report.md")
print("=" * 60)
