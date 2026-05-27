"""Generate lca-tofu-paper.pdf using ReportLab — academic journal style."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import ListFlowable, ListItem

# ── Output path ───────────────────────────────────────────────────────────────
OUTPUT = "/projects/sandbox/sonet-product/research-map/lca-tofu-paper.pdf"

# ── Page layout ───────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=3*cm, rightMargin=2.5*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm,
    title="LCA of Tofu Production in Semarang City",
    author="Abdul Jabbar, Putri Alifa Kholil, Desiana Fitri Awati",
)

W = A4[0] - 3*cm - 2.5*cm   # usable text width

# ── Colour palette ────────────────────────────────────────────────────────────
DARK   = colors.HexColor("#1a1a2e")
ACCENT = colors.HexColor("#16213e")
RULE   = colors.HexColor("#457b9d")
HEAD_BG= colors.HexColor("#e8f4f8")
ALT_BG = colors.HexColor("#f8fbfd")


# ── Styles ────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

sTitle = S("sTitle","Normal",
    fontSize=16, leading=22, alignment=TA_CENTER,
    textColor=DARK, spaceAfter=6, fontName="Helvetica-Bold")

sAuthors = S("sAuthors","Normal",
    fontSize=10, leading=14, alignment=TA_CENTER,
    textColor=ACCENT, spaceAfter=2)

sAffil = S("sAffil","Normal",
    fontSize=8.5, leading=12, alignment=TA_CENTER,
    textColor=colors.HexColor("#555555"), spaceAfter=8)

sAbstractLabel = S("sAbstractLabel","Normal",
    fontSize=9, leading=12, alignment=TA_CENTER,
    fontName="Helvetica-Bold", textColor=DARK, spaceBefore=4, spaceAfter=2)

sAbstract = S("sAbstract","Normal",
    fontSize=9, leading=13, alignment=TA_JUSTIFY,
    leftIndent=1.2*cm, rightIndent=1.2*cm,
    textColor=colors.HexColor("#222222"), spaceAfter=4)

sKeywords = S("sKeywords","Normal",
    fontSize=8.5, leading=12, alignment=TA_LEFT,
    leftIndent=1.2*cm, rightIndent=1.2*cm,
    textColor=colors.HexColor("#444444"), spaceAfter=6)

sH1 = S("sH1","Normal",
    fontSize=11.5, leading=16, fontName="Helvetica-Bold",
    textColor=DARK, spaceBefore=14, spaceAfter=5,
    borderPad=0)

sH2 = S("sH2","Normal",
    fontSize=10.5, leading=14, fontName="Helvetica-Bold",
    textColor=ACCENT, spaceBefore=10, spaceAfter=4)

sH3 = S("sH3","Normal",
    fontSize=10, leading=13, fontName="Helvetica-BoldOblique",
    textColor=colors.HexColor("#2c4a6e"), spaceBefore=8, spaceAfter=3)

sBody = S("sBody","Normal",
    fontSize=10, leading=15, alignment=TA_JUSTIFY,
    spaceAfter=6, textColor=colors.HexColor("#111111"))

sNote = S("sNote","Normal",
    fontSize=8.5, leading=12, alignment=TA_JUSTIFY,
    textColor=colors.HexColor("#555555"),
    leftIndent=0.5*cm, spaceAfter=4, fontName="Helvetica-Oblique")

sRef = S("sRef","Normal",
    fontSize=8.5, leading=13, alignment=TA_JUSTIFY,
    textColor=colors.HexColor("#222222"), spaceAfter=3,
    leftIndent=1*cm, firstLineIndent=-1*cm)

sBullet = S("sBullet","Normal",
    fontSize=9.5, leading=14, alignment=TA_JUSTIFY,
    leftIndent=0.8*cm, spaceAfter=2,
    textColor=colors.HexColor("#111111"))

sTableHead = S("sTableHead","Normal",
    fontSize=8.5, leading=11, fontName="Helvetica-Bold",
    alignment=TA_CENTER, textColor=DARK)

sTableCell = S("sTableCell","Normal",
    fontSize=8.5, leading=11, alignment=TA_CENTER,
    textColor=colors.HexColor("#111111"))

sTableCellL = S("sTableCellL","Normal",
    fontSize=8.5, leading=11, alignment=TA_LEFT,
    textColor=colors.HexColor("#111111"))

sCaption = S("sCaption","Normal",
    fontSize=8.5, leading=12, alignment=TA_LEFT,
    fontName="Helvetica-Bold", textColor=DARK,
    spaceBefore=4, spaceAfter=2)


# ── Helper: numbered section heading ─────────────────────────────────────────
def h1(num, text): return Paragraph(f"{num}. {text}", sH1)
def h2(num, text): return Paragraph(f"{num} {text}", sH2)
def h3(num, text): return Paragraph(f"{num} {text}", sH3)
def body(text):    return Paragraph(text, sBody)
def note(text):    return Paragraph(f"<i>{text}</i>", sNote)
def sp(h=6):       return Spacer(1, h)
def rule(color=RULE, thickness=1): return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

# ── Helper: table style builder ───────────────────────────────────────────────
def base_table_style(header_rows=1):
    cmds = [
        ("BACKGROUND",   (0,0), (-1, header_rows-1), HEAD_BG),
        ("TEXTCOLOR",    (0,0), (-1, header_rows-1), DARK),
        ("FONTNAME",     (0,0), (-1, header_rows-1), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("LEADING",      (0,0), (-1,-1), 11),
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, header_rows),(-1,-1),[colors.white, ALT_BG]),
        ("GRID",         (0,0), (-1,-1), 0.4, colors.HexColor("#b0cce0")),
        ("LINEABOVE",    (0,0), (-1,0),  1.0, RULE),
        ("LINEBELOW",    (0,-1),(-1,-1), 1.0, RULE),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ]
    return TableStyle(cmds)

# ── Content accumulator ───────────────────────────────────────────────────────
story = []


# ══════════════════════════════════════════════════════════════════════════════
# TITLE BLOCK
# ══════════════════════════════════════════════════════════════════════════════
story += [
    sp(4),
    Paragraph("Life Cycle Assessment of Small-Scale Tofu Production in<br/>Semarang City: Hotspot Analysis Using CML-IA and AWARE Methods", sTitle),
    sp(6),
    Paragraph("Abdul Jabbar<super>1</super>, Putri Alifa Kholil<super>1,*</super>, Desiana Fitri Awati<super>1</super>", sAuthors),
    Paragraph("<super>1</super> Study Program of Environmental Science, Faculty of Mathematics and Natural Sciences,<br/>Universitas Negeri Semarang, Semarang, Indonesia", sAffil),
    Paragraph("<super>*</super>Corresponding author: putrialifa@mail.unnes.ac.id", sAffil),
    sp(4),
    rule(RULE, 1.5),
]

# ── Abstract ──────────────────────────────────────────────────────────────────
story += [
    Paragraph("Abstract", sAbstractLabel),
    Paragraph(
        "The tofu industry is one of the most important food-processing sectors in Indonesia, given its "
        "high consumption rate and notable nutritional value. However, the environmental impacts of each "
        "production stage have not been comprehensively identified. Life Cycle Assessment (LCA) with a "
        "gate-to-gate system boundary was applied to evaluate the environmental impacts of tofu production "
        "at a small and medium-sized enterprise (SME) in Semarang City. The LCA was conducted using SimaPro "
        "10.3 software with the CML-IA Baseline impact assessment method, covering five impact categories: "
        "Global Warming Potential (GWP), Ozone Layer Depletion (ODP), Fresh Water Aquatic Ecotoxicity "
        "(FAET), Acidification, and Eutrophication. Water use was assessed using the AWARE method. Results "
        "demonstrate that the washing and boiling stages are the primary contributors to environmental "
        "impacts. Normalization results indicate that Fresh Water Aquatic Ecotoxicity is the most dominant "
        "impact category (1.33\u00d710\u00b3 kg 1,4-DB eq), followed by Global Warming Potential "
        "(5.28\u00d710\u00b3 kg CO\u2082 eq). The main environmental hotspots are organic wastewater from "
        "washing, soaking, and coagulation stages, and firewood combustion during boiling. Recommended "
        "improvement strategies include wastewater treatment systems, water recycling, and fuel substitution.",
        sAbstract),
    Paragraph("<b>Keywords:</b> Life Cycle Assessment; tofu production; CML-IA Baseline; AWARE; environmental hotspot; Semarang", sKeywords),
    rule(RULE, 1.5),
    sp(4),
]


# ══════════════════════════════════════════════════════════════════════════════
# 1. INTRODUCTION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("1", "Introduction"),
    body("Industrial activity is one of the primary drivers of global economic growth [1]. The tofu industry "
         "represents a significant food-processing sector in Indonesia owing to its high consumption rate and "
         "notable nutritional value. According to Statistics Indonesia (BPS), average per capita tofu "
         "consumption reached approximately 0.163 kg per week in 2024, indicating that tofu remains a staple "
         "food in many Indonesian households [2]. This high demand has driven increased production activity, "
         "resulting in greater resource and energy consumption, as well as waste and emissions that may cause "
         "environmental pollution if not properly managed [3]."),
    body("Such impacts are particularly evident in river water quality, as the discharge of industrial "
         "wastewater can cause Biochemical Oxygen Demand (BOD) and Chemical Oxygen Demand (COD) levels to "
         "exceed regulatory standards. In the tofu industry in Mojokerto, liquid waste was reported to contain "
         "BOD exceeding 2,000 mg/L and COD exceeding 5,000 mg/L \u2014 far above the standard thresholds of "
         "approximately 50\u2013100 mg/L [4]. Furthermore, the environmental impacts associated with each "
         "tofu production stage have not yet been comprehensively identified. A systematic approach such as "
         "Life Cycle Assessment (LCA) is therefore required to evaluate the full environmental burden of the "
         "tofu production process [5]."),
    body("Life Cycle Assessment (LCA) is a standardized method used to systematically evaluate the "
         "environmental impacts of a product or process based on all input and output flows throughout its "
         "life cycle [6]. This method identifies production stages that constitute environmental hotspots, "
         "thereby serving as the scientific basis for developing targeted environmental improvement strategies "
         "[7]. Previous LCA studies of the tofu industry predominantly focused on climate change categories "
         "and thus failed to comprehensively evaluate other environmental concerns such as water pollution, "
         "water scarcity, and solid waste generation across all production stages [8, 9]."),
    body("Therefore, this study aims to analyze the environmental impacts of tofu production in Semarang City "
         "using an LCA approach with a gate-to-gate system boundary \u2014 encompassing all stages from "
         "washing to packaging \u2014 in order to identify environmental hotspots and formulate more "
         "sustainable improvement strategies."),
]


# ══════════════════════════════════════════════════════════════════════════════
# 2. METHODS
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("2", "Methods"),
    body("This research utilized a quantitative LCA methodology to assess the environmental impacts of tofu "
         "production at an SME in Semarang City. The evaluation was performed in compliance with "
         "<b>SNI ISO 14040:2016</b> and <b>SNI ISO 14044:2016</b>, comprising four sequential phases: "
         "(1) goal and scope definition, (2) life cycle inventory analysis, (3) life cycle impact assessment, "
         "and (4) interpretation. Primary data were obtained through direct field measurements, structured "
         "interviews, and on-site documentation during a complete production batch. Secondary data were "
         "sourced from peer-reviewed literature and the Ecoinvent v3 database within SimaPro 10.3 [6]."),

    h2("2.1", "Goal and Scope Definition"),
    body("This study assesses the environmental impacts of tofu production at the facility level, focusing on "
         "water use, energy consumption, and waste generation at each production stage. The <b>functional "
         "unit</b> is defined as <b>1 kg of tofu produced</b>, consistent with comparable LCA studies of tofu "
         "and soy-based food processing. Inventory data were collected on a per-batch basis: one full "
         "production day with 1,400 kg of soybeans as raw material input, yielding 3,681 kg of tofu."),
    body("The <b>system boundary</b> adopts a gate-to-gate approach encompassing all unit processes from "
         "initial soybean washing to final molding and packaging (Figure 1). Upstream operations "
         "(soybean farming, transportation) and downstream activities (distribution, consumption, end-of-life) "
         "were excluded, consistent with prior gate-to-gate LCA investigations of similar Indonesian tofu "
         "SMEs [8, 9]."),
]

# Figure 1 box
fig1_data = [["Figure 1. Gate-to-Gate System Boundary of Tofu Production LCA"],
             ["Washing \u2192 Soaking \u2192 Grinding \u2192 Boiling \u2192 Filtration \u2192 Coagulation \u2192 Molding & Packaging"]]
fig1 = Table(fig1_data, colWidths=[W])
fig1.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0), HEAD_BG),
    ("FONTNAME",      (0,0),(-1,0), "Helvetica-Bold"),
    ("FONTNAME",      (0,1),(-1,1), "Helvetica"),
    ("FONTSIZE",      (0,0),(-1,-1), 9),
    ("ALIGN",         (0,0),(-1,-1), "CENTER"),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("BOX",           (0,0),(-1,-1), 1.0, RULE),
    ("GRID",          (0,0),(-1,-1), 0.4, colors.HexColor("#b0cce0")),
]))
story += [sp(4), fig1, sp(8)]


story += [
    h2("2.2", "Life Cycle Inventory (LCI) Analysis"),
    body("The inventory analysis phase involves identification and quantitative collection of all input and "
         "output flows for each unit process [11]. Data include soybean inputs, water and energy consumption, "
         "and waste outputs (liquid waste, solid waste, and atmospheric emissions). The full inventory is "
         "presented in Table 1."),
]

# Table 1 — LCI
story.append(Paragraph("Table 1. Life Cycle Inventory Data of Tofu Production (per batch / production day).", sCaption))
lci_header = [
    [Paragraph("Stage", sTableHead), Paragraph("Input", sTableHead),
     Paragraph("Qty", sTableHead), Paragraph("Unit", sTableHead),
     Paragraph("Output", sTableHead), Paragraph("Qty", sTableHead), Paragraph("Unit", sTableHead)]
]
lci_rows = [
    ["Washing",      "Soybeans",       "1,400", "kg",  "Washed soybeans",    "1,540", "kg"],
    ["",             "Water",          "2,800", "L",   "Wastewater",         "2,660", "L"],
    ["",             "Electricity",    "0.60",  "kWh", "CO\u2082 emissions", "0.51",  "kg"],
    ["Soaking",      "Soybeans",       "1,540", "kg",  "Hydrated soybeans",  "3,640", "kg"],
    ["",             "Water",          "2,700", "L",   "Wastewater",         "600",   "L"],
    ["",             "Electricity",    "0.45",  "kWh", "CO\u2082 emissions", "0.38",  "kg"],
    ["Grinding",     "Hyd. soybeans",  "3,640", "kg",  "Soybean slurry",     "7,840", "kg"],
    ["",             "Water",          "4,200", "L",   "Wastewater",         "0",     "L"],
    ["",             "Electricity",    "17.00", "kWh", "CO\u2082 emissions", "14.45", "kg"],
    ["Boiling",      "Soybean slurry", "7,840", "kg",  "Boiled slurry",      "15,652","kg"],
    ["",             "Water",          "8,400", "L",   "Steam (evap.)",      "588",   "L"],
    ["",             "Firewood",       "800",   "kg",  "CO\u2082 emissions", "1,397", "kg"],
    ["",             "",               "",      "",    "CH\u2084 emissions",  "0.050", "kg"],
    ["",             "",               "",      "",    "N\u2082O emissions",  "0.374", "kg"],
    ["Filtration",   "Boiled slurry",  "15,652","kg",  "Soy milk",           "14,052","kg"],
    ["",             "",               "",      "",    "Okara (residue)",    "1,600", "kg"],
    ["Coagulation",  "Soy milk",       "14,052","kg",  "Tofu curd",          "3,681", "kg"],
    ["",             "Coagulant water","421",   "L",   "Whey",               "10,434","L"],
    ["Molding &\nPkg", "Tofu curd",    "3,681", "kg",  "Final product",      "3,681", "kg"],
    ["",             "Water",          "100",   "L",   "Wastewater",         "100",   "L"],
]
col_w = [2.3*cm, 3.2*cm, 1.4*cm, 1.2*cm, 3.5*cm, 1.4*cm, 1.2*cm]
lci_table_data = lci_header + [[Paragraph(str(c), sTableCellL if i in (0,1,4) else sTableCell)
                                 for i,c in enumerate(row)] for row in lci_rows]
lci_t = Table(lci_table_data, colWidths=col_w, repeatRows=1)
lci_t.setStyle(base_table_style(1))
lci_t.setStyle(TableStyle([("ALIGN",(0,0),(1,-1),"LEFT")]))
story += [lci_t, sp(8)]


story += [
    h2("2.3", "Life Cycle Impact Assessment (LCIA)"),
    body("The LCIA phase evaluates and quantifies potential environmental impacts generated by the product "
         "system [6]. The <b>CML-IA Baseline</b> method was applied via SimaPro 10.3, covering: Global "
         "Warming Potential (GWP\u2081\u2080\u2080\u2090, kg CO\u2082 eq), Ozone Layer Depletion (ODP, kg "
         "CFC-11 eq), Fresh Water Aquatic Ecotoxicity (FAET, kg 1,4-DB eq), Acidification (AP, kg SO\u2082 "
         "eq), and Eutrophication (EP, kg PO\u2084\u00b3\u207b eq). Water use and potential water scarcity "
         "were additionally assessed using the <b>AWARE (Available WAter REmaining)</b> method."),

    h2("2.4", "Interpretation"),
    body("The interpretation phase contextualizes LCIA results to identify hotspot categories and production "
         "stages contributing the greatest environmental burdens [12]. <b>Normalization</b> was applied using "
         "CML-IA Baseline reference values to place all impact categories on a common dimensionless scale, "
         "enabling direct comparison of relative environmental significance."),
]

# ══════════════════════════════════════════════════════════════════════════════
# 3. RESULTS AND DISCUSSION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("3", "Results and Discussion"),
    h2("3.1", "Environmental Impact of Tofu Production"),
    body("The LCIA reveals measurable environmental impacts across all five assessed categories. "
         "Results are summarized in Table 2. Note that the filtration stage does not appear in the "
         "impact results because no direct energy inputs or emissions were entered in the inventory "
         "model for this stage; SimaPro therefore generates no characterization values for filtration."),
]

# Table 2 — LCIA results
story.append(Paragraph("Table 2. Environmental Impact of Tofu Production per Batch by Production Stage.", sCaption))
lcia_header = [[Paragraph(h, sTableHead) for h in
    ["Impact Category","Unit","Total","Washing","Soaking","Grinding","Boiling","Coagulation","Molding"]]]
lcia_rows = [
    ["GWP\u2081\u2080\u2080", "kg CO\u2082 eq", "5.28\u00d710\u00b3", "3.56\u00d710\u00b3", "0.945", "35.8", "1.63\u00d710\u00b3", "55.8", "5.9"],
    ["ODP",   "kg CFC-11 eq",   "6.11\u00d710\u207b\u2075", "5.93\u00d710\u207b\u2075", "2.1\u00d710\u207b\u2079", "7.93\u00d710\u207b\u2078", "1.07\u00d710\u207b\u2076", "5.02\u00d710\u207b\u2077", "1.29\u00d710\u207b\u2077"],
    ["FAET",  "kg 1,4-DB eq",   "1.33\u00d710\u00b3", "1.22\u00d710\u00b3", "0.651", "24.6", "70.6", "14.1", "2.75"],
    ["Acidification","kg SO\u2082 eq", "4.59","3.53","0.00245","0.0925","0.723","0.226","0.0176"],
    ["Eutrophication","kg PO\u2084\u00b3\u207b eq","9.10","8.30","0.0034","0.128","0.409","0.250","0.00838"],
]
lcia_col_w = [2.3*cm, 2.3*cm, 1.7*cm, 1.7*cm, 1.3*cm, 1.4*cm, 1.7*cm, 1.7*cm, 1.4*cm]
lcia_data = lcia_header + [[Paragraph(str(c), sTableCellL if i==0 else sTableCell)
                             for i,c in enumerate(row)] for row in lcia_rows]
lcia_t = Table(lcia_data, colWidths=lcia_col_w, repeatRows=1)
lcia_t.setStyle(base_table_style(1))
story += [lcia_t, sp(8)]


story += [
    h3("3.1.1", "Global Warming Potential (GWP)"),
    body("Total GWP amounts to 5.28\u00d710\u00b3 kg CO\u2082 eq. The washing stage is the largest "
         "contributor at 3.56\u00d710\u00b3 kg CO\u2082 eq (\u224867.4%), followed by the boiling stage "
         "at 1.63\u00d710\u00b3 kg CO\u2082 eq (\u224830.9%). The dominance of washing is attributed to "
         "large water volumes consumed, which indirectly require energy for water supply and distribution, "
         "generating greenhouse gas emissions. Organic-laden washing wastewater also has the potential to "
         "produce methane (CH\u2084) if discharged untreated. The boiling stage contributes significantly "
         "through firewood combustion, releasing CO\u2082, CH\u2084, and N\u2082O \u2014 all potent "
         "greenhouse gases."),

    h3("3.1.2", "Ozone Layer Depletion (ODP)"),
    body("Total ODP registers 6.11\u00d710\u207b\u2075 kg CFC-11 eq, with washing dominating at "
         "5.93\u00d710\u207b\u2075 kg CFC-11 eq (\u224897.1%). This impact is not attributed to water "
         "itself but to the energy-intensive infrastructure supporting water supply and distribution, "
         "which generates indirect emissions linked to ozone-depleting substances within the LCA "
         "system boundary."),

    h3("3.1.3", "Fresh Water Aquatic Ecotoxicity (FAET)"),
    body("Total FAET reaches 1.33\u00d710\u00b3 kg 1,4-DB eq. The washing stage is the primary "
         "contributor at 1.22\u00d710\u00b3 kg 1,4-DB eq (\u224891.7%). The large volumes of "
         "organic-laden wastewater from soybean washing \u2014 containing residual organic matter, "
         "dissolved solids, and impurities \u2014 constitute a significant toxicity threat to freshwater "
         "organisms if discharged without treatment. The boiling stage contributes 70.6 kg 1,4-DB eq "
         "(\u22485.3%) through atmospheric deposition of combustion byproducts (NO\u2093, SO\u2093) "
         "into aquatic environments."),

    h3("3.1.4", "Acidification"),
    body("Total Acidification impact is 4.59 kg SO\u2082 eq. The washing stage accounts for 3.53 kg "
         "SO\u2082 eq (\u224876.9%), linked to SO\u2082 and NO\u2093 emissions from energy generation "
         "supporting water provision. The boiling stage contributes 0.723 kg SO\u2082 eq (\u224815.8%) "
         "through firewood combustion, producing gases that may form acid rain and degrade soil and "
         "water quality."),

    h3("3.1.5", "Eutrophication"),
    body("Total Eutrophication impact is 9.10 kg PO\u2084\u00b3\u207b eq, with washing dominant at "
         "8.30 kg PO\u2084\u00b3\u207b eq (\u224891.2%). This is driven by nutrient-rich washing "
         "wastewater containing nitrogen and phosphorus compounds from soybean residues. Discharge of "
         "these nutrients can trigger excessive algal proliferation, depleting dissolved oxygen and "
         "disrupting aquatic ecosystems. The boiling stage contributes 0.409 kg PO\u2084\u00b3\u207b eq "
         "(\u22484.5%) through atmospheric NO\u2093 deposition."),
]


# ── 3.2 AWARE ─────────────────────────────────────────────────────────────────
story += [
    h2("3.2", "Water Use Assessment (AWARE Method)"),
    body("Water use was assessed using the AWARE method to determine potential water scarcity across all "
         "production stages. Total water scarcity impact is <b>515 m\u00b3 world eq</b> for the entire "
         "production system (Table 3)."),
]

story.append(Paragraph("Table 3. Water Use Assessment Results per Production Stage (AWARE Method).", sCaption))
aware_header = [[Paragraph(h, sTableHead) for h in ["Production Stage","Water Scarcity (m\u00b3 world eq)","Share (%)"]]]
aware_rows = [
    ["Boiling",               "294",  "57.09"],
    ["Grinding",              "101",  "19.61"],
    ["Soaking",               "39.3", "7.63"],
    ["Coagulation",           "38.2", "7.42"],
    ["Washing",               "35.8", "6.95"],
    ["Molding & Packaging",   "7.63", "1.48"],
    ["Total",                 "515",  "100"],
]
aware_col_w = [5*cm, 5.5*cm, 3*cm]
aware_data = aware_header + [[Paragraph(c, sTableCellL if i==0 else sTableCell)
                               for i,c in enumerate(row)] for row in aware_rows]
aware_t = Table(aware_data, colWidths=aware_col_w, repeatRows=1)
aware_t.setStyle(base_table_style(1))
aware_t.setStyle(TableStyle([
    ("FONTNAME",(0,7),(- 1,7),"Helvetica-Bold"),
    ("BACKGROUND",(0,7),(-1,7), HEAD_BG),
]))
story += [aware_t, sp(6),
    body("The boiling stage is the dominant contributor (\u224857.1%), reflecting both direct water "
         "consumption and the substantial upstream water demand associated with firewood supply chains. "
         "The grinding stage contributes the second largest share (\u224819.6%), as continuous water "
         "addition is required to achieve appropriate slurry consistency. Within the AWARE framework, the "
         "environmental burden is determined not solely by volumetric water use but also by the upstream "
         "energy system and supply chain characteristics of each production stage."),
]


# ── 3.3 Normalization ─────────────────────────────────────────────────────────
story += [
    h2("3.3", "Normalization"),
    body("Normalization was performed using CML-IA Baseline reference values to place all impact "
         "categories on a common dimensionless scale, enabling direct comparison of relative "
         "environmental significance (Table 4)."),
]

story.append(Paragraph("Table 4. Normalization Results of Tofu Production Environmental Impacts (CML-IA Baseline).", sCaption))
norm_header = [[Paragraph(h, sTableHead) for h in ["Impact Category","Normalized Value","Rank"]]]
norm_rows = [
    ["Fresh Water Aquatic Ecotoxicity (FAET)", "2.57\u00d710\u207b\u2079", "1"],
    ["Global Warming Potential (GWP)",         "1.05\u00d710\u207b\u2079", "2"],
    ["Eutrophication",                         "6.89\u00d710\u207b\u00b9\u2070", "3"],
    ["Acidification",                          "1.63\u00d710\u207b\u00b9\u2070", "4"],
    ["Ozone Layer Depletion (ODP)",            "6.84\u00d710\u207b\u00b9\u00b3", "5"],
]
norm_col_w = [8*cm, 4*cm, 1.6*cm]
norm_data = norm_header + [[Paragraph(c, sTableCellL if i==0 else sTableCell)
                             for i,c in enumerate(row)] for row in norm_rows]
norm_t = Table(norm_data, colWidths=norm_col_w, repeatRows=1)
norm_t.setStyle(base_table_style(1))
norm_t.setStyle(TableStyle([("FONTNAME",(0,1),(-1,1),"Helvetica-Bold")]))
story += [norm_t, sp(6),
    body("Normalization confirms that <b>Fresh Water Aquatic Ecotoxicity (FAET) is the dominant "
         "environmental impact category</b>, indicating that tofu production exerts the greatest pressure "
         "on freshwater ecosystems. Although GWP frequently receives priority attention in sustainability "
         "discussions, its normalized contribution ranks second, indicating that freshwater pollution "
         "represents a more acute concern at the facility scale assessed. Eutrophication (rank 3) "
         "further reinforces the urgency of addressing nutrient-laden wastewater streams."),
]


# ── 3.4 Hotspots ──────────────────────────────────────────────────────────────
story += [
    h2("3.4", "Hotspot Identification and Improvement Strategies"),
    body("Based on the integrated LCIA and normalization results, two primary environmental hotspots "
         "are identified:"),

    Paragraph("<b>Hotspot 1: Organic Liquid Waste</b> (Washing, Soaking, Coagulation Stages)", sH3),
    body("The organic-laden wastewater streams from washing, soaking, and coagulation (whey) are the "
         "principal drivers of FAET and Eutrophication \u2014 ranked first and third in normalized "
         "impact. These effluents are characterized by high BOD, COD, and nutrient loads [13, 14]. "
         "Recommended interventions:"),
]
story.append(ListFlowable([
    ListItem(Paragraph("<i>Anaerobic treatment systems</i> (biodigester/IPAL biogas) to reduce BOD/COD while recovering biogas energy", sBullet), bulletText="\u2022"),
    ListItem(Paragraph("<i>Constructed wetlands or biofilter systems</i> for nutrient removal prior to discharge", sBullet), bulletText="\u2022"),
    ListItem(Paragraph("<i>Water recycling and recirculation</i> within washing and soaking stages to reduce volumetric discharge", sBullet), bulletText="\u2022"),
    ListItem(Paragraph("<i>Whey valorization</i> (e.g., as animal feed or fermentation substrate) to divert high-nutrient streams", sBullet), bulletText="\u2022"),
], bulletType="bullet", leftIndent=20, bulletFontSize=10))

story += [
    Paragraph("<b>Hotspot 2: Firewood Combustion</b> (Boiling Stage)", sH3),
    body("The boiling stage dominates GWP, AWARE water scarcity, and is the second-largest contributor "
         "to acidification and eutrophication. Combustion of 800 kg firewood per batch releases "
         "1,397 kg CO\u2082, 0.0499 kg CH\u2084, and 0.3744 kg N\u2082O. Recommended interventions:"),
]
story.append(ListFlowable([
    ListItem(Paragraph("<i>Fuel substitution</i> to LPG, biomethane from on-site biodigesters, or high-efficiency biomass systems", sBullet), bulletText="\u2022"),
    ListItem(Paragraph("<i>Improved boiler or insulated boiling tank systems</i> to minimize heat loss and reduce fuel consumption per batch", sBullet), bulletText="\u2022"),
    ListItem(Paragraph("<i>Waste heat recovery</i> from boiling exhaust to pre-heat water in upstream stages", sBullet), bulletText="\u2022"),
], bulletType="bullet", leftIndent=20, bulletFontSize=10))

story.append(body("The LCA-based approach demonstrates that improvements targeting liquid waste management "
    "at the source yield greater environmental reduction benefits than end-of-pipe interventions [10, 15]. "
    "Prioritizing these two hotspots is expected to substantially reduce the overall environmental footprint "
    "of tofu production in Semarang City."))


# ══════════════════════════════════════════════════════════════════════════════
# 4. CONCLUSION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("4", "Conclusion"),
    body("Based on the Life Cycle Assessment of tofu production in Semarang City using a gate-to-gate "
         "approach, the following conclusions are drawn:"),
]
story.append(ListFlowable([
    ListItem(Paragraph("<b>Tofu production generates measurable environmental impacts</b> across all five "
        "assessed categories: GWP (5.28\u00d710\u00b3 kg CO\u2082 eq), ODP (6.11\u00d710\u207b\u2075 kg "
        "CFC-11 eq), FAET (1.33\u00d710\u00b3 kg 1,4-DB eq), Acidification (4.59 kg SO\u2082 eq), and "
        "Eutrophication (9.10 kg PO\u2084\u00b3\u207b eq).", sBullet), bulletText="1."),
    ListItem(Paragraph("<b>The washing and boiling stages are the primary contributors</b> to environmental "
        "impact across all categories, driven by high water consumption and firewood combustion, respectively.", sBullet), bulletText="2."),
    ListItem(Paragraph("<b>Fresh Water Aquatic Ecotoxicity (FAET) is the dominant impact category</b> based "
        "on normalization results (2.57\u00d710\u207b\u2079), confirming that organic liquid waste "
        "\u2014 particularly washing effluents, whey, and coagulation waste \u2014 constitutes the most "
        "critical environmental hotspot.", sBullet), bulletText="3."),
    ListItem(Paragraph("<b>Water scarcity</b> (AWARE method) totals 515 m\u00b3 world eq, with the boiling "
        "stage as dominant contributor (57.1%), largely driven by the upstream water demand of firewood "
        "supply chains.", sBullet), bulletText="4."),
    ListItem(Paragraph("<b>Improvement strategies</b> should prioritize: (a) implementation of wastewater "
        "treatment and recycling systems for washing, soaking, and coagulation effluents; and (b) "
        "substitution of firewood with cleaner fuel alternatives to reduce greenhouse gas emissions and "
        "water scarcity impacts.", sBullet), bulletText="5."),
], bulletType="bullet", leftIndent=20, bulletFontSize=10))

story.append(body("The findings provide actionable, evidence-based guidance for improving the environmental "
    "sustainability of SME-scale tofu production and can inform environmental management policies for the "
    "tofu industry in Semarang City and Central Java."))


# ══════════════════════════════════════════════════════════════════════════════
# REFERENCES
# ══════════════════════════════════════════════════════════════════════════════
story += [
    rule(RULE, 1),
    h1("", "References"),
]
refs = [
    "[1] Ghisellini, P., Cialani, C. & Ulgiati, S. (2016). A review on circular economy: The expected transition to a balanced interplay of environmental and economic systems. <i>Journal of Cleaner Production</i>, 114, 11\u201332. https://doi.org/10.1016/j.jclepro.2015.09.007",
    "[2] Dewi, A.N. & Setiawan, D. (2024). Bisnis kuliner: Studi kasus CV. Gehu Extra Pedas Chili Hot. <i>Jurnal Manajemen dan Bisnis Islam</i>, 1(1), 5\u201323.",
    "[3] Rosyidah, M., Masruri, A. & Putra, R.A. (2020). Assessment (LCA) method on tofu production. <i>International Journal of Science, Technology & Management</i>, 1(4), 428\u2013435.",
    "[4] Sjafruddin, R., Agustang, A. & Pertiwi, N. (2022). Estimasi limbah industri tahu dan kajian penerapan sistem produksi bersih. <i>Jurnal Ilmiah Mandala Education</i>, 8(2), 1229\u20131237. https://doi.org/10.36312/jime.v8i2.2826",
    "[5] Islami, M.C.P.A. & Harnaningrum, R.N. (2025). Integration of waste management and environmental impact assessment for sustainable manufacturing in Sukolego tofu production. 6(2), 71\u201377.",
    "[6] Hauschild, M.Z., Rosenbaum, R.K. & Olsen, S.I. (2017). <i>Life Cycle Assessment: Theory and Practice</i>. Springer. https://doi.org/10.1007/978-3-319-56475-3",
    "[7] Chitaka, T.Y. & Goga, T. (2023). The evolution of life cycle assessment in the food and beverage industry: A review. <i>Cambridge Prisms: Plastics</i>, 1, 1\u20136. https://doi.org/10.1017/plc.2023.4",
    "[8] Nugroho, M.E., Setyono, P. & Rachmawati, S. (2024). Analisis emisi gas rumah kaca dengan LCA dan AHP industri tahu. <i>Jurnal Ilmu Lingkungan</i>, 22(6), 1504\u20131512. https://doi.org/10.14710/jil.22.6.1504-1512",
    "[9] Kartika Wardana, S. et al. (2024). Penilaian dampak lingkungan dengan LCA pada industri tahu Kampung Jangkar Kulon, Cilegon Banten. <i>Jurnal Teknologi Kimia Unimal</i>, 13(2), 97\u2013106. https://doi.org/10.29103/jtku.v13i2.16429",
    "[10] Bj\u00f8rnbet, M.M. & Vild\u00e5sen, S.S. (2021). Life cycle assessment to ensure sustainability of circular business models in manufacturing. <i>Sustainability</i>, 13(19). https://doi.org/10.3390/su131911014",
    "[11] Saavedra-Rubio, K. et al. (2022). Stepwise guidance for data collection in the LCI phase: Building technology-related LCI blocks. <i>Journal of Cleaner Production</i>, 366, 132903. https://doi.org/10.1016/j.jclepro.2022.132903",
    "[12] Rasyid, M. & Anggriani, R. (2024). Penerapan LCA pada proses produksi minyak kayu putih di Desa Sawa-Namlea. <i>Journal of Social Science Research</i>, 4(3), 18970\u201318984.",
    "[13] Seroja, R., Effendi, H. & Hariyadi, S. (2018). Tofu wastewater treatment using vetiver grass and zeliac. <i>Applied Water Science</i>, 8(1), 1\u20136. https://doi.org/10.1007/s13201-018-0640-y",
    "[14] Satar, I. & Permadi, A. (2022). Treating the tofu wastewater using a green technology of microbial fuel cell system. <i>Indonesian Journal of Environmental Management and Sustainability</i>, 6(1), 162\u2013167.",
    "[15] Apriyanti, D., Pratikno, F.A. & Hertadi, C.D.P. (2025). Penilaian dampak lingkungan menggunakan LCA pada proses produksi tempe di SIKS. <i>Jurnal Mitra Teknik Industri</i>, 4(1), 19\u201327. https://doi.org/10.24912/jmti.v4i1.34600",
]
for r in refs:
    story.append(Paragraph(r, sRef))

# ── Page number footer callback ───────────────────────────────────────────────
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(A4[0]/2, 1.5*cm, f"Page {doc.page}")
    canvas.restoreState()

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(f"PDF generated: {OUTPUT}")
