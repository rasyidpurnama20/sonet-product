"""Generate chart images for Sejarah Teknologi & AI PPT"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
from pathlib import Path

OUT = Path("/projects/sandbox/sonet-product/assets")
OUT.mkdir(exist_ok=True)

BG   = "#0D1117"
CARD = "#161B22"
L0   = "#58A6FF"   # blue  – tech
L1   = "#F78166"   # red/orange – pekerjaan
L2   = "#56D364"   # green – pendidikan
L3   = "#E3B341"   # gold  – AI
L4   = "#BC8CFF"   # purple – para ahli
WHITE = "#E6EDF3"
GRAY  = "#8B949E"
LINE  = "#30363D"

def savefig(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f"  ✅  {name}")


# ─────────────────────────────────────────────────────────────────────────────
# CHART 1  — Bagan Alur Besar (vertical flowchart)
# ─────────────────────────────────────────────────────────────────────────────
def chart_alur_besar():
    fig, ax = plt.subplots(figsize=(7, 10))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,10)

    steps = [
        ("Manusia punya\nkebutuhan hidup", L2),
        ("Manusia bekerja\nuntuk bertahan", L0),
        ("Kerja manual\npunya keterbatasan", L1),
        ("Manusia menciptakan\nteknologi", L3),
        ("Teknologi ubah cara\nbekerja & belajar", L4),
        ("AI: tahap terbaru\nperubahan tersebut", "#FF6B6B"),
    ]
    step_h = 1.45
    for i, (txt, col) in enumerate(steps):
        y = 9.1 - i * step_h
        fancy = FancyBboxPatch((1.2, y-0.52), 7.6, 1.0,
            boxstyle="round,pad=0.08", linewidth=2,
            edgecolor=col, facecolor=col+"22", zorder=3)
        ax.add_patch(fancy)
        ax.text(5, y-0.02, txt, ha='center', va='center',
                fontsize=13, fontweight='bold', color=WHITE,
                multialignment='center', zorder=4)
        if i < len(steps)-1:
            ax.annotate("", xy=(5, y - step_h + 0.52),
                        xytext=(5, y - 0.52),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=2), zorder=2)
    ax.set_title("Alur Besar: Manusia → Teknologi → AI",
                 color=WHITE, fontsize=14, fontweight='bold', pad=10)
    savefig(fig, "hist_alur_besar.png")

chart_alur_besar()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 2  — Timeline Revolusi Teknologi (horizontal)
# ─────────────────────────────────────────────────────────────────────────────
def chart_timeline():
    fig, ax = plt.subplots(figsize=(13, 5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(-0.5, 10.5); ax.set_ylim(-1.8, 3.2)

    events = [
        (0,   "Pra-Mesin\nUap",  "Otot &\nhewan",   "#8B949E", "~1700"),
        (2,   "Mesin\nUap",      "Tenaga\nfisik",    "#F78166", "1760s"),
        (4,   "Listrik",         "Produksi\ncepat",  "#E3B341", "1880s"),
        (6,   "Komputer",        "Data &\nadmin",    "#58A6FF", "1950s"),
        (8,   "Internet",        "Akses\ninfo",      "#56D364", "1990s"),
        (10,  "AI",              "Kerja\npikiran",   "#BC8CFF", "2020s"),
    ]

    # main line
    ax.plot([-0.2, 10.2], [0, 0], color=LINE, lw=3, zorder=1)

    for x, name, sub, col, era in events:
        # dot
        ax.plot(x, 0, 'o', color=col, markersize=18, zorder=3)
        ax.plot(x, 0, 'o', color=BG,  markersize=10, zorder=4)
        ax.plot(x, 0, 'o', color=col, markersize=5,  zorder=5)
        # era label below
        ax.text(x, -0.55, era, ha='center', va='top',
                fontsize=9, color=GRAY)
        # name above
        ax.text(x, 0.55, name, ha='center', va='bottom',
                fontsize=11, fontweight='bold', color=col,
                multialignment='center')
        # sub below name
        ax.text(x, -1.05, sub, ha='center', va='top',
                fontsize=9, color=WHITE, multialignment='center')

    ax.set_title("Timeline Revolusi Teknologi & Dampaknya pada Pekerjaan",
                 color=WHITE, fontsize=13, fontweight='bold', pad=8)
    savefig(fig, "hist_timeline.png")

chart_timeline()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 3  — Pyramid / Stacked: Apa yang digantikan teknologi
# ─────────────────────────────────────────────────────────────────────────────
def chart_replaced():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
    for sp in ax.spines.values(): sp.set_edgecolor(LINE)
    ax.tick_params(colors=GRAY, labelsize=11)

    cats = ["Mesin Uap\n(1760s)", "Listrik\n(1880s)", "Komputer\n(1950s)",
            "Internet\n(1990s)", "AI\n(2020s)"]
    physical = [85, 90, 30, 10, 15]
    cognitive = [5,  10, 65, 80, 90]
    creative  = [0,  0,  5,  10, 35]

    x = np.arange(len(cats))
    w = 0.28
    ax.bar(x - w, physical,  w, color=L1,  label="Kerja Fisik/Manual",   zorder=3)
    ax.bar(x,     cognitive, w, color=L0,  label="Kerja Kognitif/Data",  zorder=3)
    ax.bar(x + w, creative,  w, color=L4,  label="Kreatif & Keputusan",  zorder=3)

    for bars in [ax.containers[0], ax.containers[1], ax.containers[2]]:
        ax.bar_label(bars, fmt='%d%%', padding=3,
                     fontsize=9, color=WHITE, fontweight='bold')

    ax.set_xticks(x); ax.set_xticklabels(cats, color=WHITE, fontsize=10)
    ax.set_ylabel("% Dampak Otomasi (estimasi)", color=GRAY, fontsize=10)
    ax.set_ylim(0, 108)
    ax.yaxis.grid(True, color=LINE, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(framealpha=0, labelcolor=WHITE, fontsize=10,
              loc='upper left')
    ax.set_title("Jenis Pekerjaan yang Terpengaruh Tiap Era Teknologi",
                 color=WHITE, fontsize=13, fontweight='bold', pad=10)
    fig.tight_layout()
    savefig(fig, "hist_replaced.png")

chart_replaced()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 4  — Sebelum vs Sesudah AI dalam Pendidikan (side-by-side)
# ─────────────────────────────────────────────────────────────────────────────
def chart_edu_before_after():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor(BG)

    sides = [
        ("Sebelum AI", L1, [
            "Sumber utama: guru & buku",
            "Kecepatan belajar\ndisamakan semua siswa",
            "Siswa tertinggal\nsulit dapat bantuan personal",
            "Guru sulit bimbing\nsiswa satu per satu",
            "Akses terbatas\npada lokasi & biaya",
        ]),
        ("Setelah AI", L2, [
            "Bisa bertanya kapan saja",
            "AI jelaskan ulang\ndengan cara berbeda",
            "AI tutor personal\nuntuk setiap siswa",
            "Pembelajaran adaptif\nsesuai kecepatan siswa",
            "Akses gratis\nke seluruh dunia",
        ]),
    ]

    for ax, (title, col, items) in zip(axes, sides):
        ax.set_facecolor(col+"15")
        ax.set_xlim(0, 10); ax.set_ylim(0, 10)
        ax.axis('off')
        # header
        hdr = FancyBboxPatch((0.3, 8.5), 9.4, 1.3,
              boxstyle="round,pad=0.1", facecolor=col+"44",
              edgecolor=col, linewidth=2)
        ax.add_patch(hdr)
        ax.text(5, 9.15, title, ha='center', va='center',
                fontsize=16, fontweight='bold', color=col)
        for i, item in enumerate(items):
            y = 7.3 - i * 1.48
            box = FancyBboxPatch((0.5, y-0.55), 9.0, 1.05,
                  boxstyle="round,pad=0.06", facecolor=CARD,
                  edgecolor=col+"55", linewidth=1.2)
            ax.add_patch(box)
            ax.text(5, y-0.02, item, ha='center', va='center',
                    fontsize=11, color=WHITE, multialignment='center')

    fig.suptitle("Pendidikan: Sebelum AI  vs  Setelah AI",
                 color=WHITE, fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout(pad=0.8)
    savefig(fig, "hist_edu_compare.png")

chart_edu_before_after()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 5  — Bagan AI vs Teknologi Sebelumnya (apa yang dibantu)
# ─────────────────────────────────────────────────────────────────────────────
def chart_ai_vs_prev():
    fig, ax = plt.subplots(figsize=(11, 5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,6)

    rows = [
        ("Mesin Uap",  "Tenaga Fisik",  "Otot & Pabrik",   L1),
        ("Listrik",    "Energi",        "Lampu, Motor",     L3),
        ("Komputer",   "Data",          "Hitung, Simpan",   L0),
        ("Internet",   "Informasi",     "Akses global",     L2),
        ("AI",         "Kognisi",       "Pikir, Tulis,\nAnalisis", "#FF6B6B"),
    ]

    col_x   = [0.4, 3.2, 6.2, 9.0]
    headers = ["Teknologi", "Yang Dibantu", "Contoh Tugas", "Kategori"]
    for hx, htxt in zip(col_x, headers):
        ax.text(hx, 5.55, htxt, fontsize=11, fontweight='bold',
                color=GRAY, va='top')
    ax.plot([0, 12], [5.35, 5.35], color=LINE, lw=1.5)

    for i, (tech, what, ex, col) in enumerate(rows):
        y = 4.6 - i * 0.88
        bg = FancyBboxPatch((0.2, y-0.35), 11.6, 0.78,
             boxstyle="round,pad=0.05", facecolor=col+"18",
             edgecolor=col+"55", linewidth=1)
        ax.add_patch(bg)
        ax.text(col_x[0]+0.1, y, tech,  fontsize=12, color=col,
                fontweight='bold', va='center')
        ax.text(col_x[1]+0.1, y, what,  fontsize=11, color=WHITE, va='center')
        ax.text(col_x[2]+0.1, y, ex,    fontsize=11, color=GRAY,
                va='center', multialignment='left')
        # category pill
        pill = FancyBboxPatch((col_x[3]-0.1, y-0.25), 2.8, 0.55,
               boxstyle="round,pad=0.05", facecolor=col+"33",
               edgecolor=col, linewidth=1.5)
        ax.add_patch(pill)
        ax.text(col_x[3]+1.3, y, "Fisik" if i<2 else
                ("Data" if i<3 else ("Info" if i<4 else "Kognitif")),
                fontsize=10, color=col, fontweight='bold',
                ha='center', va='center')

    ax.set_title("Apa yang Dibantu Setiap Teknologi?",
                 color=WHITE, fontsize=14, fontweight='bold',
                 x=0.44, y=0.98)
    savefig(fig, "hist_ai_vs_prev.png")

chart_ai_vs_prev()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 6  — Quotes para ahli: 5 cards
# ─────────────────────────────────────────────────────────────────────────────
def chart_expert_cards():
    fig, ax = plt.subplots(figsize=(13, 4.5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,5)

    experts = [
        ("Andrew Ng", L0,
         "\"AI is the new\nelectricity.\"",
         "Belajar AI =\nSenjata karir"),
        ("Jensen Huang", L3,
         "\"Kalah bukan\nkarena AI, tapi\nkarena tidak\npakai AI.\"",
         "Segera pakai\nAI tutor"),
        ("Elon Musk", L1,
         "\"Probably none\nof us will\nhave a job.\"",
         "Pekerjaan\nopsional + UBI"),
        ("Yuval Harari", "#FF6B6B",
         "\"AI will take\nover systems\nbuilt on words.\"",
         "AI masuk sistem\nberbasis bahasa"),
        ("Sal Khan", L2,
         "\"Biggest positive\ntransformation\neducation ever\nsaw.\"",
         "Tutor personal\nuntuk semua"),
    ]

    box_w = 2.35
    for i, (name, col, quote, key) in enumerate(experts):
        x = 0.2 + i * 2.56
        # card
        card = FancyBboxPatch((x, 0.2), box_w, 4.5,
               boxstyle="round,pad=0.08", facecolor=col+"18",
               edgecolor=col, linewidth=2)
        ax.add_patch(card)
        # header
        hdr = FancyBboxPatch((x, 3.75), box_w, 0.92,
              boxstyle="round,pad=0.06", facecolor=col+"44",
              edgecolor='none')
        ax.add_patch(hdr)
        ax.text(x + box_w/2, 4.2, name, ha='center', va='center',
                fontsize=10.5, fontweight='bold', color=col)
        # quote
        ax.text(x + box_w/2, 2.35, quote, ha='center', va='center',
                fontsize=9.5, color=WHITE, style='italic',
                multialignment='center')
        # key takeaway
        sep = FancyBboxPatch((x+0.15, 0.55), box_w-0.3, 0.92,
              boxstyle="round,pad=0.05", facecolor=col+"22",
              edgecolor=col+"55", linewidth=1)
        ax.add_patch(sep)
        ax.text(x + box_w/2, 1.02, key, ha='center', va='center',
                fontsize=9, color=col, fontweight='bold',
                multialignment='center')

    ax.set_title("Pendapat Para Ahli Dunia tentang AI",
                 color=WHITE, fontsize=14, fontweight='bold',
                 x=0.5, y=0.97)
    savefig(fig, "hist_expert_cards.png")

chart_expert_cards()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 7  — Bagan Alur Pekerjaan (flowchart horizontal)
# ─────────────────────────────────────────────────────────────────────────────
def chart_work_flow():
    fig, ax = plt.subplots(figsize=(13, 4.5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,5)

    nodes = [
        (1.0,  2.5, "Sejarah\nTeknologi\nUbah Kerja", L0),
        (3.3,  2.5, "Andrew Ng\nAI = Senjata\nbagi Pelajar", L0),
        (5.6,  2.5, "Jensen Huang\nYang Kalah =\nTidak Pakai AI", L3),
        (7.9,  2.5, "Yuval Harari\nAI Masuk\nSistem Bahasa", "#FF6B6B"),
        (10.2, 2.5, "Elon Musk\nPekerjaan\nOpsional + UBI", L1),
    ]
    for i, (x, y, txt, col) in enumerate(nodes):
        box = FancyBboxPatch((x-1.05, y-1.0), 2.1, 2.0,
              boxstyle="round,pad=0.08", facecolor=col+"22",
              edgecolor=col, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, txt, ha='center', va='center',
                fontsize=10, color=WHITE, fontweight='bold',
                multialignment='center')
        if i < len(nodes)-1:
            ax.annotate("", xy=(nodes[i+1][0]-1.06, 2.5),
                        xytext=(x+1.06, 2.5),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2))

    ax.set_title("Alur Pekerjaan Menurut Para Ahli",
                 color=WHITE, fontsize=13, fontweight='bold', pad=8)
    savefig(fig, "hist_work_flow.png")

chart_work_flow()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 8  — Bagan Alur Pendidikan (flowchart horizontal)
# ─────────────────────────────────────────────────────────────────────────────
def chart_edu_flow():
    fig, ax = plt.subplots(figsize=(13, 4.5))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,5)

    nodes = [
        (0.95, 2.5, "Sejarah\nPendidikan\nIkuti Teknologi", L2),
        (3.1,  2.5, "Andrew Ng\nAI Definisikan\nUlang Guru", L0),
        (5.3,  2.5, "Jensen Huang\nSegera Pakai\nAI Tutor", L3),
        (7.5,  2.5, "Bill Gates\nAI = Guru\nTerbaik", L2),
        (9.7,  2.5, "Sal Khan\nTransformasi\nTerbesar", "#56D364"),
        (11.9, 2.5, "Sam Altman\nGenerasi\nPaling Beruntung", L4),
    ]
    for i, (x, y, txt, col) in enumerate(nodes):
        box = FancyBboxPatch((x-1.02, y-1.0), 2.04, 2.0,
              boxstyle="round,pad=0.07", facecolor=col+"22",
              edgecolor=col, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, txt, ha='center', va='center',
                fontsize=9.5, color=WHITE, fontweight='bold',
                multialignment='center')
        if i < len(nodes)-1:
            ax.annotate("", xy=(nodes[i+1][0]-1.03, 2.5),
                        xytext=(x+1.03, 2.5),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.8))

    ax.set_title("Alur Pendidikan Menurut Para Ahli",
                 color=WHITE, fontsize=13, fontweight='bold', pad=8)
    savefig(fig, "hist_edu_flow.png")

chart_edu_flow()


# ─────────────────────────────────────────────────────────────────────────────
# CHART 9  — Bagan Besar Keseluruhan (vertical mega-flow, 2 columns)
# ─────────────────────────────────────────────────────────────────────────────
def chart_mega_flow():
    fig, ax = plt.subplots(figsize=(10, 11))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,12)

    steps = [
        ("Manusia punya\nkebutuhan hidup",          L2),
        ("Manusia bekerja\nuntuk memenuhi kebutuhan", L0),
        ("Kerja manual\nmemiliki batas",              L1),
        ("Manusia menciptakan\nteknologi",             L3),
        ("Mesin Uap — bantu\ntenaga fisik",            "#F78166"),
        ("Listrik — percepat\nproduksi",               L3),
        ("Komputer — bantu\ndata & administrasi",      L0),
        ("Internet — buka\nakses informasi",           L2),
        ("AI — bantu\nberpikir & belajar",             L4),
        ("Pekerjaan & pendidikan\nberubah besar-besaran", "#FF6B6B"),
        ("Manusia harus belajar\nulang & beradaptasi", L2),
    ]
    sh = 1.0
    for i, (txt, col) in enumerate(steps):
        y = 11.2 - i*sh
        box = FancyBboxPatch((0.8, y-0.38), 8.4, 0.78,
              boxstyle="round,pad=0.06", facecolor=col+"22",
              edgecolor=col, linewidth=1.8)
        ax.add_patch(box)
        ax.text(5, y-0.0, txt, ha='center', va='center',
                fontsize=11, fontweight='bold', color=WHITE,
                multialignment='center')
        if i < len(steps)-1:
            ax.annotate("", xy=(5, y - sh + 0.38),
                        xytext=(5, y - 0.38),
                        arrowprops=dict(arrowstyle="-|>",
                                        color=GRAY, lw=1.8))

    ax.set_title("Bagan Besar: Manusia → Teknologi → AI → Adaptasi",
                 color=WHITE, fontsize=13, fontweight='bold', pad=8)
    savefig(fig, "hist_mega_flow.png")

chart_mega_flow()
print("\n🎉 All charts done!")
