#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Membangun file penilaian Pengenalan Pola A (pola-2026).

Kolom nilai sesuai urutan file:
  1. Classification Task (Intermediate)  -> ambil nilai tertinggi (Grade/10.00)
  2. Evaluation Metric Quiz              -> confusion matrix 4x4 dari NIM+99,
                                            hitung acc, f1 micro, f1 macro, f1 weighted,
                                            koreksi Response 2-5 -> nilai
  3. Manual Classification Task (Beginner) -> ambil nilai tertinggi (Grade/10.00)
"""
import csv, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
F1 = os.path.join(BASE, "Pengenalan Pola A-Classification Task (Intermediate)-grades.csv")
F2 = os.path.join(BASE, "Pengenalan Pola A-Evaluation Metric Quiz-responses.csv")
F3 = os.path.join(BASE, "Pengenalan Pola A-Manual Classification Task (Beginner)-grades.csv")

def read_rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.reader(f))

# ---------- File 1 & 3: ambil nilai tertinggi ----------
def highest_grades(path):
    rows = read_rows(path)
    header = rows[0]
    grade_idx = header.index("Grade/10.00")
    best = {}   # nim -> (name, grade)
    for r in rows[1:]:
        if not r or r[0].strip().lower().startswith("overall"):
            continue
        nim = r[0].strip()
        name = r[1].strip()
        try:
            g = float(r[grade_idx])
        except ValueError:
            continue
        if nim not in best or g > best[nim][1]:
            best[nim] = (name, g)
    return best

# ---------- File 2: confusion matrix dari NIM+99 ----------
def metrics_from_nim(nim):
    digits = [int(c) for c in (str(nim) + "99")]
    # ambil 16 digit pertama -> matriks 4x4 (row-major)
    digits = digits[:16]
    M = [digits[i*4:(i+1)*4] for i in range(4)]
    total = sum(sum(row) for row in M)
    diag = sum(M[i][i] for i in range(4))
    acc = diag / total if total else 0.0
    col_sum = [sum(M[r][c] for r in range(4)) for c in range(4)]
    row_sum = [sum(M[r]) for r in range(4)]
    f1 = []
    for i in range(4):
        tp = M[i][i]
        prec = tp / row_sum[i] if row_sum[i] else 0.0
        rec = tp / col_sum[i] if col_sum[i] else 0.0
        f1i = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
        f1.append(f1i)
    f1_macro = sum(f1) / 4
    # weighted dengan support = col_sum (true-class support pada orientasi ini)
    f1_weighted = sum(col_sum[i] * f1[i] for i in range(4)) / total if total else 0.0
    f1_micro = acc
    return acc, f1_micro, f1_macro, f1_weighted

def parse_val(s):
    s = (s or "").strip()
    if s in ("-", ""):
        return None
    m = re.search(r"(\d+)\s*/\s*(\d+)", s)        # pecahan a/b
    if m:
        b = int(m.group(2))
        return int(m.group(1)) / b if b else None
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(%?)", s) # angka pertama (+ optional %)
    if not m:
        return None
    num = float(m.group(1).replace(",", "."))
    if m.group(2) == "%":
        num /= 100.0
    return num

TOL = 0.01

def grade_quiz(path):
    rows = read_rows(path)
    header = rows[0]
    idx = {h: i for i, h in enumerate(header)}
    r2, r3, r4, r5 = idx["Response 2"], idx["Response 3"], idx["Response 4"], idx["Response 5"]
    result = {}  # nim -> (name, grade, detail)
    for r in rows[1:]:
        if not r or r[0].strip().lower().startswith("overall"):
            continue
        nim = r[0].strip()
        name = r[1].strip()
        acc, f1mi, f1ma, f1we = metrics_from_nim(nim)
        key = [acc, f1mi, f1ma, f1we]
        resp = [parse_val(r[r2]), parse_val(r[r3]), parse_val(r[r4]), parse_val(r[r5])]
        correct = 0
        marks = []
        for k, v in zip(key, resp):
            ok = v is not None and abs(v - k) <= TOL
            correct += 1 if ok else 0
            marks.append("V" if ok else "X")
        grade = round(correct * 2.5, 2)  # 4 soal x 2.5 = 10
        result[nim] = (name, grade, (acc, f1mi, f1ma, f1we), resp, marks)
    return result

f1_best = highest_grades(F1)
f3_best = highest_grades(F3)
quiz = grade_quiz(F2)

# ---------- gabung berdasar NIM ----------
all_nims = set(f1_best) | set(quiz) | set(f3_best)

def name_for(nim):
    for src in (quiz, f1_best, f3_best):
        if nim in src:
            return src[nim][0]
    return ""

rows_out = []
for nim in all_nims:
    name = name_for(nim)
    n1 = f1_best.get(nim, (None, None))[1]
    n2 = quiz.get(nim, (None, None))[1]
    n3 = f3_best.get(nim, (None, None))[1]
    rows_out.append((nim, name, n1, n2, n3))

rows_out.sort(key=lambda x: x[1].lower())

def fmt(v):
    return "" if v is None else f"{v:.2f}"

out_csv = os.path.join(BASE, "penilaian-pola-2026.csv")
with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["NIM", "Nama",
                "Classification Task (Intermediate)",
                "Evaluation Metric Quiz",
                "Manual Classification Task (Beginner)"])
    for nim, name, n1, n2, n3 in rows_out:
        w.writerow([nim, name, fmt(n1), fmt(n2), fmt(n3)])

# ---------- verifikasi sampel ----------
print("=== Verifikasi sampel file 2 (NIM -> acc, f1micro, f1macro, f1weighted) ===")
for nim in ["24060123140151", "24060123130112", "24060123120002"]:
    if nim in quiz:
        name, grade, (a, b, c, d), resp, marks = quiz[nim]
        print(f"{nim} {name}: acc={a:.4f} micro={b:.4f} macro={c:.4f} weighted={d:.4f}")
        print(f"   jawaban={resp} marks={marks} -> nilai {grade}")
print(f"\nTotal mahasiswa: {len(rows_out)}")
print(f"File ditulis: {out_csv}")
