#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mengisi POLA_PAIK6808_2025_2_A.xlsx:
  - Kolom H "Nilai Quiz" (0-100)        = rata2(Classification Task, Evaluation Metric Quiz,
                                          Manual Classification Task) [skala 0-10] x 10
  - Kolom F "Nilai Hasil Proyek" (0-100)= rata2(Oral, Arsitektur, Proyek(Presentasi+Keaktifan))
                                          setelah skala disamakan ke 0-100
                                          (Oral x10, Arsitektur x10, ProyekPK apa adanya)

Sumber nilai: penilaian-pola-2026.csv
Sel kosong (tidak mengumpulkan) dihitung sebagai 0 dalam rata-rata.
Nilai Proyek(Presentasi+Keaktifan) dipakai apa adanya (termasuk 0 dan -10).
"""
import csv, os, openpyxl

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "penilaian-pola-2026.csv")
XLSX = os.path.join(BASE, "POLA_PAIK6808_2025_2_A.xlsx")

def num(s):
    s = (s or "").strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None

# baca CSV penilaian -> per NIM
data = {}
with open(CSV, encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        nim = row["NIM"].strip()
        data[nim] = {
            "ct":     num(row["Classification Task (Intermediate)"]),
            "quiz":   num(row["Evaluation Metric Quiz"]),
            "manual": num(row["Manual Classification Task (Beginner)"]),
            "oral":   num(row["Oral"]),
            "arsi":   num(row["Arsitektur"]),
            "ppk":    num(row["Proyek (Presentasi + Keaktifan)"]),
        }

def kuis_100(d):
    # tiga komponen skala 0-10, kosong=0, rata-rata, lalu x10 -> 0-100
    vals = [d["ct"] or 0.0, d["quiz"] or 0.0, d["manual"] or 0.0]
    return round(sum(vals) / 3 * 10, 2)

def proyek_100(d):
    # samakan skala ke 0-100: Oral x10, Arsitektur x10, ProyekPK apa adanya; kosong=0
    oral = (d["oral"] or 0.0) * 10
    arsi = (d["arsi"] or 0.0) * 10
    ppk  = d["ppk"] if d["ppk"] is not None else 0.0
    return round((oral + arsi + ppk) / 3, 2)

wb = openpyxl.load_workbook(XLSX)
ws = wb["Worksheet"]

PREVIEW = []
missing_in_csv = []
for r in range(8, ws.max_row + 1):
    nim = ws.cell(r, 1).value
    nama = ws.cell(r, 2).value
    if nim is None and nama is None:
        continue
    nim = str(nim).strip()
    if nim not in data:
        missing_in_csv.append((r, nim, nama))
        continue
    d = data[nim]
    kuis = kuis_100(d)
    proyek = proyek_100(d)
    ws.cell(r, 6).value = proyek   # F = Nilai Hasil Proyek
    ws.cell(r, 8).value = kuis     # H = Nilai Quiz
    PREVIEW.append((nim, nama, d, kuis, proyek))

wb.save(XLSX)

print(f"{'NIM':<16}{'KUIS(H)':>8}{'PROYEK(F)':>10}  detail(ct,quiz,man | oral,arsi,ppk)  Nama")
for nim, nama, d, kuis, proyek in PREVIEW:
    det = f"({d['ct']},{d['quiz']},{d['manual']} | {d['oral']},{d['arsi']},{d['ppk']})"
    print(f"{nim:<16}{kuis:>8}{proyek:>10}  {det:<44} {nama}")
print(f"\nTerisi: {len(PREVIEW)} mahasiswa")
print(f"NIM di xlsx tapi tidak ada di CSV: {missing_in_csv}")
csv_nims = set(data); xlsx_nims = {str(ws.cell(r,1).value).strip() for r in range(8,ws.max_row+1) if ws.cell(r,1).value}
print(f"NIM di CSV tapi tidak ada di xlsx: {sorted(csv_nims - xlsx_nims)}")
