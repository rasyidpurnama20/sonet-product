"""
Generate all chart images for the webinar PPT v2.
Outputs PNG files to /projects/sandbox/sonet-product/assets/
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path("/projects/sandbox/sonet-product/assets")
OUT.mkdir(exist_ok=True)

# ── shared style ──────────────────────────────────────────────────────────
BG      = "#0A0A0F"
RED     = "#E63946"
BLUE    = "#00B4D8"
GOLD    = "#FFD166"
GREEN   = "#06D6A0"
WHITE   = "#FFFFFF"
GRAY    = "#AAAAAA"
CARD    = "#14141E"
MIDBLUE = "#1A3A5C"

def dark_fig(w=10, h=5.5):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    for spine in ax.spines.values():
        spine.set_edgecolor("#2A2A3E")
    ax.tick_params(colors=GRAY, labelsize=11)
    ax.xaxis.label.set_color(GRAY)
    ax.yaxis.label.set_color(GRAY)
    return fig, ax

# ════════════════════════════════════════════════════════════════════════════
# CHART 1 ── WEF Future of Jobs 2025  (170M created vs 92M displaced)
# ════════════════════════════════════════════════════════════════════════════
fig, ax = dark_fig(10, 5.8)

categories = ['Pekerjaan\nBaru Tercipta', 'Pekerjaan\nTerhapus', 'Net\nPeningkatan']
values     = [170, 92, 78]
colors     = [GREEN, RED, GOLD]

bars = ax.bar(categories, values, color=colors, width=0.45,
              zorder=3, edgecolor='none')

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            f'{val}M', ha='center', va='bottom',
            fontsize=22, fontweight='bold', color=WHITE)

ax.set_ylim(0, 210)
ax.set_ylabel('Jumlah Pekerjaan (juta)', color=GRAY, fontsize=12)
ax.set_title('WEF Future of Jobs Report 2025  •  Proyeksi hingga 2030',
             color=WHITE, fontsize=14, fontweight='bold', pad=14)
ax.yaxis.grid(True, color='#2A2A3E', linewidth=0.8, zorder=0)
ax.set_axisbelow(True)

# annotation
ax.text(0.99, 0.04, 'Sumber: World Economic Forum, Januari 2025',
        transform=ax.transAxes, ha='right', fontsize=9,
        color=GRAY, style='italic')

fig.tight_layout(pad=1.5)
fig.savefig(OUT / "chart_wef_jobs.png", dpi=150, bbox_inches='tight',
            facecolor=BG)
plt.close(fig)
print("✅  chart_wef_jobs.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 2 ── McKinsey AI Adoption at Work  2017 → 2025
# ════════════════════════════════════════════════════════════════════════════
fig, ax = dark_fig(10, 5.2)

years  = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
adopt  = [20,   27,   33,   50,   47,   55,   72,   80,   88]

ax.fill_between(years, adopt, alpha=0.18, color=BLUE)
ax.plot(years, adopt, color=BLUE, linewidth=3.5, zorder=5,
        marker='o', markersize=8, markerfacecolor=GOLD,
        markeredgecolor=BLUE, markeredgewidth=2)

for x, y in zip(years, adopt):
    offset = 7 if y < 80 else -12
    va = 'bottom' if y < 80 else 'top'
    ax.annotate(f'{y}%', (x, y), textcoords='offset points',
                xytext=(0, offset), ha='center', fontsize=10,
                color=WHITE, fontweight='bold')

# highlight 2025 bar
ax.axvline(2025, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.6)
ax.text(2025.05, 45, '2025\n88%', color=GOLD, fontsize=11,
        fontweight='bold')

ax.set_xlim(2016.5, 2025.8)
ax.set_ylim(0, 105)
ax.set_xticks(years)
ax.set_xticklabels([str(y) for y in years])
ax.set_ylabel('% Perusahaan Menggunakan AI', color=GRAY, fontsize=12)
ax.set_title('Tren Adopsi AI di Tempat Kerja Global  (McKinsey, 2025)',
             color=WHITE, fontsize=14, fontweight='bold', pad=14)
ax.yaxis.grid(True, color='#2A2A3E', linewidth=0.8)
ax.set_axisbelow(True)

ax.text(0.99, 0.04, 'Sumber: McKinsey Global Survey on AI, 2025',
        transform=ax.transAxes, ha='right', fontsize=9,
        color=GRAY, style='italic')

fig.tight_layout(pad=1.5)
fig.savefig(OUT / "chart_mckinsey_adoption.png", dpi=150,
            bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("✅  chart_mckinsey_adoption.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 3 ── AI in Education Statistics  (horizontal bar)
# ════════════════════════════════════════════════════════════════════════════
fig, ax = dark_fig(10, 5.5)

labels  = ['Siswa global\npakai AI',
           'Sekolah sudah\ngunakan AI tools',
           'Siswa pakai AI\nuntuk ujian',
           'Guru K-12 US\npakai AI lesson',
           'Adopsi GenAI\n(tertinggi semua industri)']
values  = [86, 67, 88, 68, 86]
colors2 = [BLUE, GREEN, GOLD, RED, "#9B5DE5"]

bars = ax.barh(labels, values, color=colors2, height=0.52,
               zorder=3, edgecolor='none')

for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 1.2, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', fontsize=16,
            fontweight='bold', color=WHITE)

ax.set_xlim(0, 103)
ax.xaxis.grid(True, color='#2A2A3E', linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
ax.set_xlabel('Persentase (%)', color=GRAY, fontsize=12)
ax.set_title('Statistik AI dalam Dunia Pendidikan Global  (2025)',
             color=WHITE, fontsize=14, fontweight='bold', pad=14)
ax.tick_params(axis='y', labelsize=11, labelcolor=WHITE)

ax.text(0.99, 0.02, 'Sumber: Digital Education Council, HEPI, WorldMetrics 2025',
        transform=ax.transAxes, ha='right', fontsize=9,
        color=GRAY, style='italic')

fig.tight_layout(pad=1.5)
fig.savefig(OUT / "chart_edu_stats.png", dpi=150, bbox_inches='tight',
            facecolor=BG)
plt.close(fig)
print("✅  chart_edu_stats.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 4 ── AI Jobs Disruption Donut  (% jobs at risk by 2030)
# ════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(10, 5.2))
fig.patch.set_facecolor(BG)

# left: donut job disruption
ax1 = axes[0]
ax1.set_facecolor(BG)
sizes   = [22, 78]
clrs    = [RED, "#1A3A5C"]
explode = (0.04, 0)
wedges, texts = ax1.pie(sizes, colors=clrs, explode=explode,
                         startangle=90,
                         wedgeprops={'linewidth': 2, 'edgecolor': BG,
                                     'width': 0.55})
ax1.text(0, 0, f'22%', ha='center', va='center',
         fontsize=28, fontweight='bold', color=RED)
ax1.set_title('Pekerjaan Terganggu\noleh AI pada 2030', color=WHITE,
              fontsize=13, fontweight='bold')
red_p  = mpatches.Patch(color=RED,     label='Terganggu (22%)')
blue_p = mpatches.Patch(color="#1A3A5C", label='Aman (78%)')
ax1.legend(handles=[red_p, blue_p], loc='lower center',
           framealpha=0, labelcolor=WHITE, fontsize=10,
           bbox_to_anchor=(0.5, -0.08))

# right: skill demand bar
ax2 = axes[1]
ax2.set_facecolor(CARD)
for spine in ax2.spines.values():
    spine.set_edgecolor("#2A2A3E")

skills  = ['AI Fluency', 'Data Analysis', 'Creative\nThinking',
           'Resilience\n& Agility', 'Tech Literacy']
demand  = [7.0, 5.2, 4.5, 4.1, 3.8]   # relative demand growth (x)
bar_colors = [GOLD, BLUE, GREEN, "#9B5DE5", RED]

bars2 = ax2.barh(skills, demand, color=bar_colors,
                  height=0.5, zorder=3)
for bar, val in zip(bars2, demand):
    ax2.text(bar.get_width() + 0.1,
             bar.get_y() + bar.get_height()/2,
             f'{val}x', va='center', fontsize=13,
             fontweight='bold', color=WHITE)

ax2.set_xlim(0, 9)
ax2.xaxis.grid(True, color='#2A2A3E', linewidth=0.8)
ax2.set_axisbelow(True)
ax2.set_xlabel('Pertumbuhan Permintaan (x kali)', color=GRAY, fontsize=10)
ax2.set_title('Skill Paling Dicari\ndi Era AI (2025)', color=WHITE,
              fontsize=13, fontweight='bold')
ax2.tick_params(colors=WHITE, labelsize=10)

fig.suptitle('WEF Future of Jobs Report 2025  •  Proyeksi 2030',
             color=GRAY, fontsize=11, y=0.02)
fig.tight_layout(pad=1.8)
fig.savefig(OUT / "chart_disruption_skills.png", dpi=150,
            bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("✅  chart_disruption_skills.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 5 ── Harari VS Andrew Ng  — Perspektif Side-by-Side (radar/spider)
# ════════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(10, 5.5))
fig.patch.set_facecolor(BG)

categories_r = ['Optimisme\nAI', 'Urgensi\nRegulasi',
                 'Peluang\nPendidikan', 'Risiko\nSosial',
                 'Kesiapan\nIndividu', 'Demokratisasi\nAkses']
N = len(categories_r)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

harari_vals = [2, 9, 5, 9, 4, 4]
ng_vals     = [9, 4, 10, 4, 9, 9]
harari_vals += harari_vals[:1]
ng_vals     += ng_vals[:1]

ax = fig.add_subplot(111, polar=True)
ax.set_facecolor(CARD)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.plot(angles, harari_vals, color=RED,  linewidth=2.5, linestyle='solid')
ax.fill(angles, harari_vals, color=RED,  alpha=0.20)
ax.plot(angles, ng_vals,     color=BLUE, linewidth=2.5, linestyle='solid')
ax.fill(angles, ng_vals,     color=BLUE, alpha=0.20)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories_r, color=WHITE, fontsize=10.5,
                   fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2','4','6','8','10'], color=GRAY, fontsize=8)
ax.grid(color='#2A2A3E', linewidth=0.8)
ax.spines['polar'].set_color('#2A2A3E')

h_patch = mpatches.Patch(color=RED,  label='🔴 Yuval Noah Harari')
n_patch = mpatches.Patch(color=BLUE, label='🔵 Andrew Ng')
ax.legend(handles=[h_patch, n_patch], loc='upper right',
          bbox_to_anchor=(1.38, 1.18), framealpha=0,
          labelcolor=WHITE, fontsize=12)

ax.set_title('Peta Perspektif: Harari vs Andrew Ng',
             color=WHITE, fontsize=14, fontweight='bold',
             pad=22, y=1.12)

fig.tight_layout()
fig.savefig(OUT / "chart_radar.png", dpi=150, bbox_inches='tight',
            facecolor=BG)
plt.close(fig)
print("✅  chart_radar.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 6 ── AI Education Market Growth  $5.88B → $32.27B
# ════════════════════════════════════════════════════════════════════════════
fig, ax = dark_fig(10, 5.2)

years_m = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
market  = [5.88, 7.73, 10.15, 13.33, 17.52, 23.02, 32.27]

ax.fill_between(years_m, market, alpha=0.22, color=GOLD)
ax.plot(years_m, market, color=GOLD, linewidth=3.5, marker='o',
        markersize=9, markerfacecolor=GOLD,
        markeredgecolor=BG, markeredgewidth=2, zorder=5)

for x, y in zip(years_m, market):
    offset = 9
    ax.annotate(f'${y}B', (x, y), textcoords='offset points',
                xytext=(0, offset), ha='center', fontsize=10.5,
                color=WHITE, fontweight='bold')

ax.set_xlim(2023.7, 2030.3)
ax.set_ylim(0, 40)
ax.set_xticks(years_m)
ax.set_ylabel('Nilai Pasar (USD Miliar)', color=GRAY, fontsize=12)
ax.set_title('Pertumbuhan Pasar AI dalam Pendidikan Global  (CAGR 31.2%)',
             color=WHITE, fontsize=14, fontweight='bold', pad=14)
ax.yaxis.grid(True, color='#2A2A3E', linewidth=0.8)
ax.set_axisbelow(True)

# annotate CAGR
ax.annotate('CAGR\n31.2%', xy=(2027, 13.33), xytext=(2025.5, 25),
            fontsize=13, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.8))

ax.text(0.99, 0.04, 'Sumber: Grand View Research, 2025',
        transform=ax.transAxes, ha='right', fontsize=9,
        color=GRAY, style='italic')

fig.tight_layout(pad=1.5)
fig.savefig(OUT / "chart_edu_market.png", dpi=150, bbox_inches='tight',
            facecolor=BG)
plt.close(fig)
print("✅  chart_edu_market.png")

# ════════════════════════════════════════════════════════════════════════════
# CHART 7 ── Quote visual: key numbers infographic
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 4.5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

stats = [
    (BLUE,  "88%",   "AI adoption\ndi tempat kerja\n(McKinsey 2025)"),
    (GREEN, "170M",  "pekerjaan baru\ntercipta\n(WEF 2025)"),
    (RED,   "92M",   "pekerjaan\ntergantikan\n(WEF 2025)"),
    (GOLD,  "86%",   "siswa global\ngunakan AI\n(2025)"),
    ("9B5DE5","$32B","pasar AI edu\nby 2030\n(Grand View)"),
]

for i, (col, big, small) in enumerate(stats):
    x = 0.1 + i * 0.2
    if col == "9B5DE5":
        col = "#9B5DE5"

    # card box
    rect = mpatches.FancyBboxPatch((x-0.085, 0.06), 0.17, 0.88,
        boxstyle="round,pad=0.02",
        linewidth=2, edgecolor=col,
        facecolor=CARD, transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)

    ax.text(x, 0.68, big, transform=ax.transAxes,
            ha='center', va='center', fontsize=28, fontweight='bold',
            color=col)
    ax.text(x, 0.28, small, transform=ax.transAxes,
            ha='center', va='center', fontsize=10,
            color=GRAY, multialignment='center')

ax.set_title('Fakta & Data Kunci — AI 2025',
             color=WHITE, fontsize=15, fontweight='bold',
             pad=6)

fig.tight_layout(pad=0.5)
fig.savefig(OUT / "chart_key_numbers.png", dpi=150, bbox_inches='tight',
            facecolor=BG)
plt.close(fig)
print("✅  chart_key_numbers.png")

print("\n🎉  All charts generated!")
import os
for f in sorted(OUT.glob("*.png")):
    size = os.path.getsize(f)
    print(f"   {f.name}  ({size//1024} KB)")
