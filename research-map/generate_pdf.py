"""
Generate lca-tofu-paper.pdf  --  academic journal style via ReportLab.
Run:  python3 generate_pdf.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether,
)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT

OUTPUT = "/projects/sandbox/sonet-product/research-map/lca-tofu-paper.pdf"

# ── page geometry ──────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=3*cm, rightMargin=2.5*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm,
    title="LCA of Small-Scale Tofu Production in Semarang City",
    author="Abdul Jabbar, Putri Alifa Kholil, Desiana Fitri Awati",
)
W = A4[0] - 3*cm - 2.5*cm          # usable text width

# ── colour palette ─────────────────────────────────────────────────────────────
DARK    = colors.HexColor("#1a1a2e")
ACCENT  = colors.HexColor("#16213e")
RULE    = colors.HexColor("#457b9d")
HEAD_BG = colors.HexColor("#e8f4f8")
ALT_BG  = colors.HexColor("#f8fbfd")
AMBER   = colors.HexColor("#b45309")

# ── paragraph styles ───────────────────────────────────────────────────────────
_base = getSampleStyleSheet()

def S(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=_base[parent], **kw)

sTitle   = S("sTitle",   fontSize=15, leading=20, alignment=TA_CENTER,
             fontName="Helvetica-Bold", textColor=DARK, spaceAfter=5)
sAuthor  = S("sAuthor",  fontSize=10, leading=14, alignment=TA_CENTER,
             textColor=ACCENT, spaceAfter=2)
sAffil   = S("sAffil",   fontSize=8.5, leading=12, alignment=TA_CENTER,
             textColor=colors.HexColor("#555555"), spaceAfter=8)
sAbsLbl  = S("sAbsLbl",  fontSize=9, alignment=TA_CENTER,
             fontName="Helvetica-Bold", textColor=DARK, spaceBefore=4, spaceAfter=2)
sAbs     = S("sAbs",     fontSize=9, leading=13, alignment=TA_JUSTIFY,
             leftIndent=1.2*cm, rightIndent=1.2*cm,
             textColor=colors.HexColor("#222222"), spaceAfter=3)
sKW      = S("sKW",      fontSize=8.5, leading=12, alignment=TA_LEFT,
             leftIndent=1.2*cm, rightIndent=1.2*cm,
             textColor=colors.HexColor("#444444"), spaceAfter=5)
sH1      = S("sH1",      fontSize=11.5, leading=16, fontName="Helvetica-Bold",
             textColor=DARK, spaceBefore=14, spaceAfter=5)
sH2      = S("sH2",      fontSize=10.5, leading=14, fontName="Helvetica-Bold",
             textColor=ACCENT, spaceBefore=10, spaceAfter=4)
sH3      = S("sH3",      fontSize=10, leading=13, fontName="Helvetica-BoldOblique",
             textColor=colors.HexColor("#2c4a6e"), spaceBefore=8, spaceAfter=3)
sBody    = S("sBody",    fontSize=10, leading=15, alignment=TA_JUSTIFY,
             spaceAfter=6, textColor=colors.HexColor("#111111"))
sNote    = S("sNote",    fontSize=8.5, leading=12, alignment=TA_JUSTIFY,
             textColor=colors.HexColor("#555555"), leftIndent=0.5*cm,
             spaceAfter=4, fontName="Helvetica-Oblique")
sRef     = S("sRef",     fontSize=8.5, leading=12.5, alignment=TA_JUSTIFY,
             textColor=colors.HexColor("#222222"), spaceAfter=4,
             leftIndent=1*cm, firstLineIndent=-1*cm)
sRefNote = S("sRefNote", fontSize=8, leading=11, alignment=TA_JUSTIFY,
             textColor=AMBER, leftIndent=1.5*cm, spaceAfter=3,
             fontName="Helvetica-Oblique")
sTH      = S("sTH",      fontSize=8.5, leading=11, fontName="Helvetica-Bold",
             alignment=TA_CENTER, textColor=DARK)
sTC      = S("sTC",      fontSize=8.5, leading=11,
             alignment=TA_CENTER, textColor=colors.HexColor("#111111"))
sTCL     = S("sTCL",     fontSize=8.5, leading=11,
             alignment=TA_LEFT,   textColor=colors.HexColor("#111111"))
sCap     = S("sCap",     fontSize=8.5, leading=12, alignment=TA_LEFT,
             fontName="Helvetica-Bold", textColor=DARK,
             spaceBefore=4, spaceAfter=2)

# ── helper functions ───────────────────────────────────────────────────────────
def h1(n, t): return Paragraph(f"{n}. {t}", sH1)
def h2(n, t): return Paragraph(f"{n} {t}", sH2)
def h3(n, t): return Paragraph(f"{n} {t}", sH3)
def body(t):  return Paragraph(t, sBody)
def note(t):  return Paragraph(f"<i>{t}</i>", sNote)
def sp(h=6):  return Spacer(1, h)
def rule(thick=1):
    return HRFlowable(width="100%", thickness=thick,
                      color=RULE, spaceAfter=4, spaceBefore=4)

def tblstyle(n_hdr=1):
    return TableStyle([
        ("BACKGROUND",    (0, 0), (-1, n_hdr-1), HEAD_BG),
        ("FONTNAME",      (0, 0), (-1, n_hdr-1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("LEADING",       (0, 0), (-1, -1), 11),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, n_hdr), (-1, -1), [colors.white, ALT_BG]),
        ("GRID",          (0, 0), (-1, -1), 0.35, colors.HexColor("#b0cce0")),
        ("LINEABOVE",     (0, 0), (-1, 0),  0.9, RULE),
        ("LINEBELOW",     (0,-1), (-1,-1),  0.9, RULE),
        ("TOPPADDING",    (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
    ])

def page_num(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(3*cm, 1.4*cm,
        "Jabbar et al. / LCA of Tofu Production in Semarang City")
    canvas.drawRightString(A4[0]-2.5*cm, 1.4*cm, str(doc.page))
    canvas.restoreState()

# ── story accumulator ──────────────────────────────────────────────────────────
story = []


# ══════════════════════════════════════════════════════════════════════════════
# TITLE BLOCK
# ══════════════════════════════════════════════════════════════════════════════
story += [
    sp(4),
    Paragraph(
        "Life Cycle Assessment of Small-Scale Tofu Production in Semarang City:<br/>"
        "Hotspot Analysis Using CML-IA and AWARE Methods", sTitle),
    sp(5),
    Paragraph(
        "Abdul Jabbar<super>1</super>,\u2002"
        "Putri Alifa Kholil<super>1,*</super>,\u2002"
        "Desiana Fitri Awati<super>1</super>", sAuthor),
    Paragraph(
        "<super>1</super>\u202fStudy Program of Environmental Science, "
        "Faculty of Mathematics and Natural Sciences,<br/>"
        "Universitas Negeri Semarang, Semarang, Indonesia", sAffil),
    Paragraph(
        "<super>*</super>Corresponding author: putrialifa@mail.unnes.ac.id", sAffil),
    sp(4),
    rule(1.4),
]

# ── Abstract ──────────────────────────────────────────────────────────────────
story += [
    Paragraph("Abstract", sAbsLbl),
    Paragraph(
        "The tofu industry is one of the most important food-processing sectors in Indonesia, "
        "given its high consumption rate and notable nutritional value. However, the environmental "
        "impacts of each production stage have not been comprehensively identified. Life Cycle "
        "Assessment (LCA) with a gate-to-gate system boundary was applied to evaluate the "
        "environmental impacts of tofu production at a small and medium-sized enterprise (SME) in "
        "Semarang City. The LCA was conducted using SimaPro\u202f10.3 with the CML-IA Baseline "
        "method, covering five impact categories: Global Warming Potential (GWP), Ozone Layer "
        "Depletion (ODP), Fresh Water Aquatic Ecotoxicity (FAET), Acidification, and "
        "Eutrophication. Water use was additionally assessed using the AWARE method. The results "
        "demonstrate that the washing and boiling stages are the primary contributors to "
        "environmental impacts across all assessed categories. Normalization results indicate that "
        "Fresh Water Aquatic Ecotoxicity is the most dominant impact category "
        "(1.33\u00d710\u00b3\u202fkg 1,4-DB\u202feq), followed by Global Warming Potential "
        "(5.28\u00d710\u00b3\u202fkg CO\u2082\u202feq). The principal environmental hotspots are "
        "the organic wastewater generated during the washing, soaking, and coagulation stages, "
        "as well as firewood combustion during boiling. Recommended improvement strategies include "
        "the implementation of wastewater treatment systems, water recycling practices, and fuel "
        "substitution.", sAbs),
    Paragraph(
        "<b>Keywords:</b> Life Cycle Assessment; tofu production; CML-IA Baseline; AWARE; "
        "environmental hotspot; Semarang", sKW),
    rule(1.4),
    sp(4),
]

# ══════════════════════════════════════════════════════════════════════════════
# 1. INTRODUCTION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("1", "Introduction"),
    body("Industrial activity is one of the primary drivers of global economic growth [1]. "
         "The tofu industry represents a significant food-processing sector in Indonesia owing "
         "to its high consumption rate and notable nutritional value. According to Statistics "
         "Indonesia (BPS), average per capita tofu consumption reached approximately 0.163\u202fkg "
         "per week in 2024, indicating that tofu remains a staple food in many Indonesian "
         "households [2]. This high demand has driven increased production activity, resulting in "
         "greater resource and energy consumption, as well as the generation of waste and emissions "
         "that may cause environmental pollution if not properly managed [3]."),
    body("Such impacts are particularly evident in river water quality, as the discharge of "
         "industrial wastewater can cause Biochemical Oxygen Demand (BOD) and Chemical Oxygen "
         "Demand (COD) levels to exceed regulatory standards. In the case of the tofu industry in "
         "Mojokerto, liquid waste was reported to contain BOD levels exceeding 2,000\u202fmg/L and "
         "COD levels exceeding 5,000\u202fmg/L, far above the standard thresholds of approximately "
         "50 to 100\u202fmg/L [4]. Furthermore, the environmental impacts associated with each "
         "stage of tofu production have not yet been comprehensively identified. A systematic "
         "approach such as Life Cycle Assessment (LCA) is therefore required to evaluate the full "
         "environmental burden of the tofu production process [5]."),
    body("Life Cycle Assessment (LCA) is a standardized method used to systematically evaluate "
         "the environmental impacts of a product or process based on all input and output flows "
         "throughout its life cycle [6]. This method is capable of identifying production stages "
         "that constitute environmental hotspots, thereby serving as the scientific basis for "
         "developing targeted environmental improvement strategies [7]. Previous studies have "
         "applied LCA to assess the environmental impacts of the tofu industry; however, these "
         "studies predominantly focused on climate change impact categories and thus failed to "
         "comprehensively evaluate other environmental concerns, such as water pollution loads, "
         "water scarcity, and solid waste generation across all production stages [8, 9]."),
    body("Therefore, this study aims to analyze the environmental impacts of tofu production in "
         "Semarang City using an LCA approach with a gate-to-gate system boundary, encompassing "
         "all stages from washing to packaging, in order to identify environmental hotspots and "
         "formulate more sustainable improvement strategies."),
]

# ══════════════════════════════════════════════════════════════════════════════
# 2. METHODS
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("2", "Methods"),
    body("This research utilized a quantitative methodology based on Life Cycle Assessment (LCA) "
         "to assess the environmental impacts of tofu production at an SME in Semarang City. The "
         "evaluation was performed in compliance with <b>SNI ISO\u202f14040:2016</b> and "
         "<b>SNI ISO\u202f14044:2016</b>, comprising four sequential phases: (1)\u202fgoal and "
         "scope definition, (2)\u202flife cycle inventory analysis, (3)\u202flife cycle impact "
         "assessment, and (4)\u202finterpretation. Primary data were obtained through direct field "
         "measurements, structured interviews with the facility operator, and on-site documentation "
         "during a complete production batch. Secondary data were sourced from peer-reviewed "
         "scientific literature and the Ecoinvent\u202fv3 database within SimaPro\u202f10.3 [6]."),
    h2("2.1", "Goal and Scope Definition"),
    body("This study aims to assess the environmental impacts of tofu production at the facility "
         "level, focusing on water use, energy consumption, and waste generation at each "
         "production stage. The <b>functional unit</b> was established as <b>1\u202fkg of tofu "
         "produced</b>, consistent with functional units used in comparable LCA studies of tofu "
         "and soy-based food processing. All inventory data were initially collected on a "
         "per-batch basis representing one complete production day, with 1,400\u202fkg of soybeans "
         "as raw material input yielding 3,681\u202fkg of tofu."),
    body("The <b>system boundary</b> adopts a gate-to-gate approach, encompassing all unit "
         "processes from the initial washing of soybeans to final molding and packaging (Figure 1). "
         "Upstream operations, including soybean farming and transportation, as well as downstream "
         "activities such as distribution, consumption, and end-of-life management, were excluded "
         "from the system boundary. This delineation is consistent with prior gate-to-gate LCA "
         "investigations of similar Indonesian tofu SMEs [8, 9]."),
]

# Figure 1 box
fig1 = Table(
    [["Figure 1. Gate-to-Gate System Boundary"],
     ["Washing \u2192 Soaking \u2192 Grinding \u2192 Boiling \u2192 "
      "Filtration \u2192 Coagulation \u2192 Molding & Packaging"]],
    colWidths=[W])
fig1.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0), HEAD_BG),
    ("FONTNAME",      (0,0),(-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),(-1,-1), 9),
    ("ALIGN",         (0,0),(-1,-1), "CENTER"),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("BOX",           (0,0),(-1,-1), 0.9, RULE),
    ("LINEBELOW",     (0,0),(-1,0),  0.5, colors.HexColor("#b0cce0")),
]))
story += [sp(4), fig1, sp(8)]


story += [
    h2("2.2", "Life Cycle Inventory (LCI) Analysis"),
    body("The inventory analysis phase involves the identification and collection of quantitative "
         "data on all input and output flows for each unit process within the product system, in "
         "accordance with the defined functional unit [11]. Data collected include soybean inputs, "
         "water and energy consumption, and waste outputs comprising liquid waste, solid waste, "
         "and atmospheric emissions. The complete inventory dataset is presented in Table 1."),
    Paragraph("Table 1. Life Cycle Inventory Data of Tofu Production (per batch / production day).", sCap),
]

lci_hdr = [[Paragraph(h, sTH) for h in
    ["Stage","Input","Qty","Unit","Output","Qty","Unit"]]]
lci_rows = [
    ["Washing",     "Soybeans",        "1,400","kg", "Washed soybeans",   "1,540","kg"],
    ["",            "Water",           "2,800","L",  "Wastewater",        "2,660","L"],
    ["",            "Electricity",     "0.60", "kWh","CO\u2082 emissions","0.51", "kg"],
    ["Soaking",     "Soybeans",        "1,540","kg", "Hydrated soybeans", "3,640","kg"],
    ["",            "Water",           "2,700","L",  "Wastewater",        "600",  "L"],
    ["",            "Electricity",     "0.45", "kWh","CO\u2082 emissions","0.38", "kg"],
    ["Grinding",    "Hyd. soybeans",   "3,640","kg", "Soybean slurry",    "7,840","kg"],
    ["",            "Water",           "4,200","L",  "Wastewater",        "0",    "L"],
    ["",            "Electricity",     "17.00","kWh","CO\u2082 emissions","14.45","kg"],
    ["Boiling",     "Soybean slurry",  "7,840","kg", "Boiled slurry",     "15,652","kg"],
    ["",            "Water",           "8,400","L",  "Steam loss",        "588",  "L"],
    ["",            "Firewood",        "800",  "kg", "CO\u2082 emissions","1,397","kg"],
    ["",            "",                "",     "",   "CH\u2084 emissions","0.0499","kg"],
    ["",            "",                "",     "",   "N\u2082O emissions","0.3744","kg"],
    ["Filtration",  "Boiled slurry",   "15,652","kg","Soy milk",          "14,052","kg"],
    ["",            "",                "",     "",   "Okara (residue)",   "1,600","kg"],
    ["Coagulation", "Soy milk",        "14,052","kg","Tofu curd",         "3,681","kg"],
    ["",            "Coagulant water", "421",  "L",  "Whey",              "10,434","L"],
    ["Molding &\nPkg","Tofu curd",     "3,681","kg", "Final product",     "3,681","kg"],
    ["",            "Water",           "100",  "L",  "Wastewater",        "100",  "L"],
]
cw = [2.1*cm, 3.0*cm, 1.35*cm, 1.15*cm, 3.4*cm, 1.35*cm, 1.15*cm]
lci_data = lci_hdr + [
    [Paragraph(str(c), sTCL if i in (0,1,4) else sTC) for i,c in enumerate(r)]
    for r in lci_rows]
lci_t = Table(lci_data, colWidths=cw, repeatRows=1)
lci_t.setStyle(tblstyle(1))
lci_t.setStyle(TableStyle([("ALIGN",(0,0),(1,-1),"LEFT")]))
story += [lci_t, sp(8)]

story += [
    h2("2.3", "Life Cycle Impact Assessment (LCIA)"),
    body("The LCIA phase evaluates and quantifies the potential environmental impacts generated "
         "by the product system based on the compiled inventory data [6]. In this study, the "
         "<b>CML-IA Baseline</b> method was applied using SimaPro\u202f10.3, covering five impact "
         "categories: Global Warming Potential (GWP\u2081\u2080\u2080\u2090, kg CO\u2082\u202feq), "
         "Ozone Layer Depletion (ODP, kg CFC-11\u202feq), Fresh Water Aquatic Ecotoxicity "
         "(FAET, kg 1,4-DB\u202feq), Acidification (AP, kg SO\u2082\u202feq), and Eutrophication "
         "(EP, kg PO\u2084\u00b3\u207b\u202feq). Water use and potential water scarcity were "
         "additionally assessed using the <b>AWARE (Available WAter REmaining)</b> method to "
         "evaluate water deprivation relative to regional water availability."),
    h2("2.4", "Interpretation"),
    body("The interpretation phase contextualizes LCIA results to identify hotspot impact "
         "categories and the production stages contributing the greatest environmental burdens. "
         "Normalization was subsequently applied using the CML-IA Baseline reference values to "
         "compare impact categories expressed in different units on a common dimensionless scale, "
         "thereby enabling the relative significance of each impact to be determined. "
         "Interpretation was focused strictly within the gate-to-gate system boundary to ensure "
         "that results accurately reflect the stages exerting the greatest environmental "
         "influence [6]."),
]

# ══════════════════════════════════════════════════════════════════════════════
# 3. RESULTS AND DISCUSSION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("3", "Results and Discussion"),
    h2("3.1", "Environmental Impact of Tofu Production"),
    body("The LCIA reveals that tofu production generates measurable environmental impacts across "
         "all five assessed categories. The quantitative results per production stage are "
         "summarized in Table 2."),
    Paragraph("Table 2. Environmental Impact of Tofu Production per Batch by Production Stage.", sCap),
]

lcia_hdr = [[Paragraph(h, sTH) for h in
    ["Impact Category","Unit","Total","Washing","Soaking","Grinding","Boiling","Coagulation","Molding"]]]
lcia_rows = [
    ["GWP\u2081\u2080\u2080","kg CO\u2082 eq",
     "5.28\u00d710\u00b3","3.56\u00d710\u00b3","0.945","35.8","1.63\u00d710\u00b3","55.8","5.9"],
    ["ODP","kg CFC-11 eq",
     "6.11\u00d710\u207b\u2075","5.93\u00d710\u207b\u2075","2.1\u00d710\u207b\u2079",
     "7.93\u00d710\u207b\u2078","1.07\u00d710\u207b\u2076","5.02\u00d710\u207b\u2077","1.29\u00d710\u207b\u2077"],
    ["FAET","kg 1,4-DB eq",
     "1.33\u00d710\u00b3","1.22\u00d710\u00b3","0.651","24.6","70.6","14.1","2.75"],
    ["Acidification","kg SO\u2082 eq","4.59","3.53","0.00245","0.0925","0.723","0.226","0.0176"],
    ["Eutrophication","kg PO\u2084\u00b3\u207b eq","9.10","8.30","0.0034","0.128","0.409","0.250","0.00838"],
]
cw2 = [2.2*cm, 2.1*cm, 1.6*cm, 1.6*cm, 1.2*cm, 1.3*cm, 1.6*cm, 1.6*cm, 1.35*cm]
lcia_data = lcia_hdr + [
    [Paragraph(str(c), sTCL if i==0 else sTC) for i,c in enumerate(r)]
    for r in lcia_rows]
lcia_t = Table(lcia_data, colWidths=cw2, repeatRows=1)
lcia_t.setStyle(tblstyle(1))
story += [lcia_t, sp(4),
    note("Note: The filtration stage does not appear in the impact results because no direct "
         "energy inputs or emissions were entered in the inventory model for this stage; it "
         "therefore generates no characterization values in SimaPro."),
    sp(6)]


story += [
    h3("3.1.1", "Global Warming Potential (GWP)"),
    body("Total GWP amounts to 5.28\u00d710\u00b3\u202fkg CO\u2082\u202feq. The washing stage "
         "is the largest contributor at 3.56\u00d710\u00b3\u202fkg CO\u2082\u202feq "
         "(approximately 67.4%), followed by the boiling stage at 1.63\u00d710\u00b3\u202fkg "
         "CO\u2082\u202feq (approximately 30.9%). The dominance of the washing stage is attributed "
         "to the large volumes of water consumed during soybean cleaning, which indirectly require "
         "energy for water supply and distribution, thereby generating greenhouse gas emissions. "
         "In addition, organic-laden washing wastewater has the potential to generate methane "
         "(CH\u2084) if discharged without treatment. The boiling stage contributes significantly "
         "to GWP owing to the combustion of firewood, which releases CO\u2082, CH\u2084, and "
         "N\u2082O, all of which are potent greenhouse gases with long-term atmospheric warming "
         "effects."),
    h3("3.1.2", "Ozone Layer Depletion (ODP)"),
    body("Total ODP registers 6.11\u00d710\u207b\u2075\u202fkg CFC-11\u202feq, with the washing "
         "stage dominating at 5.93\u00d710\u207b\u2075\u202fkg CFC-11\u202feq (approximately "
         "97.1%). This impact is not attributed to water consumption per se, but rather to the "
         "energy-intensive infrastructure required for water supply and distribution within the "
         "production chain, which generates indirect emissions linked to ozone-depleting "
         "substances. Although this category contributes the least in normalized terms, its "
         "disproportionate concentration in the washing stage highlights the indirect environmental "
         "burden of high water use."),
    h3("3.1.3", "Fresh Water Aquatic Ecotoxicity (FAET)"),
    body("Total FAET reaches 1.33\u00d710\u00b3\u202fkg 1,4-DB\u202feq, with the washing stage "
         "as the primary contributor at 1.22\u00d710\u00b3\u202fkg 1,4-DB\u202feq (approximately "
         "91.7%). The large volumes of organic-laden wastewater generated during soybean washing "
         "contain residual organic matter, dissolved solids, and impurities that constitute a "
         "significant toxicity risk to freshwater organisms if discharged without adequate "
         "treatment. The boiling stage contributes 70.6\u202fkg 1,4-DB\u202feq (approximately "
         "5.3%) through the atmospheric deposition of combustion byproducts, including nitrogen "
         "oxides (NO\u2093) and sulfur oxides (SO\u2093), into aquatic environments."),
    h3("3.1.4", "Acidification"),
    body("Total Acidification impact is 4.59\u202fkg SO\u2082\u202feq. The washing stage accounts "
         "for 3.53\u202fkg SO\u2082\u202feq (approximately 76.9%), associated with SO\u2082 and "
         "NO\u2093 emissions from energy generation required for water provision. The boiling stage "
         "contributes 0.723\u202fkg SO\u2082\u202feq (approximately 15.8%) through firewood "
         "combustion, which releases acidifying gaseous precursors that may react with atmospheric "
         "moisture to form acid deposition, potentially degrading both soil and water quality in "
         "the surrounding environment."),
    h3("3.1.5", "Eutrophication"),
    body("Total Eutrophication impact is 9.10\u202fkg PO\u2084\u00b3\u207b\u202feq, with the "
         "washing stage dominant at 8.30\u202fkg PO\u2084\u00b3\u207b\u202feq (approximately "
         "91.2%). This impact is driven primarily by nutrient-rich washing wastewater that contains "
         "nitrogen and phosphorus compounds derived from soybean residues. When discharged into "
         "receiving water bodies without treatment, these compounds can trigger excessive "
         "proliferation of algae and aquatic microorganisms, leading to depletion of dissolved "
         "oxygen and disruption of aquatic ecosystem function. The boiling stage contributes "
         "0.409\u202fkg PO\u2084\u00b3\u207b\u202feq (approximately 4.5%) through atmospheric "
         "deposition of NO\u2093 emissions generated during firewood combustion."),
]

# ── 3.2 AWARE ─────────────────────────────────────────────────────────────────
story += [
    h2("3.2", "Water Use Assessment (AWARE Method)"),
    body("Water use was assessed using the AWARE method to quantify potential water scarcity, "
         "expressed as the volume of water deprived from downstream users per unit of water "
         "consumed at a given location. The total water scarcity impact for the entire production "
         "system amounts to <b>515\u202fm\u00b3 world\u202feq</b> (Table 3)."),
    Paragraph("Table 3. Water Use Assessment Results by Production Stage (AWARE Method).", sCap),
]

aware_hdr = [[Paragraph(h, sTH) for h in
    ["Production Stage","Water Scarcity (m\u00b3 world\u202feq)","Share (%)"]]]
aware_rows = [
    ["Boiling",              "294",  "57.09"],
    ["Grinding",             "101",  "19.61"],
    ["Soaking",              "39.3", "7.63"],
    ["Coagulation",          "38.2", "7.42"],
    ["Washing",              "35.8", "6.95"],
    ["Molding & Packaging",  "7.63", "1.48"],
    ["Total",                "515",  "100"],
]
cw3 = [5.2*cm, 5.8*cm, 2.6*cm]
aware_data = aware_hdr + [
    [Paragraph(c, sTCL if i==0 else sTC) for i,c in enumerate(r)]
    for r in aware_rows]
aware_t = Table(aware_data, colWidths=cw3, repeatRows=1)
aware_t.setStyle(tblstyle(1))
aware_t.setStyle(TableStyle([
    ("FONTNAME",   (0,7),(-1,7),"Helvetica-Bold"),
    ("BACKGROUND", (0,7),(-1,7), HEAD_BG),
]))
story += [aware_t, sp(6),
    body("The boiling stage is the dominant contributor (approximately 57.1%), reflecting both "
         "direct water consumption during soybean slurry cooking and the substantial upstream "
         "water demand embedded in the firewood supply chain. Within the AWARE framework, the "
         "environmental burden is determined not solely by the volume of water consumed, but also "
         "by the water intensity of the upstream energy system and associated supply chains. The "
         "grinding stage contributes the second largest share (approximately 19.6%), as continuous "
         "water addition is required throughout this process to achieve the appropriate slurry "
         "consistency and extraction efficiency."),
]


# ── 3.3 Normalization ──────────────────────────────────────────────────────────
story += [
    h2("3.3", "Normalization"),
    body("Normalization was performed using the CML-IA Baseline reference values to place all "
         "impact categories on a common dimensionless scale, enabling direct and meaningful "
         "comparison of relative environmental significance across categories with different "
         "units (Table 4)."),
    Paragraph("Table 4. Normalization Results of Tofu Production Environmental Impacts "
              "(CML-IA Baseline).", sCap),
]

norm_hdr = [[Paragraph(h, sTH) for h in ["Impact Category","Normalized Value","Rank"]]]
norm_rows = [
    ["Fresh Water Aquatic Ecotoxicity (FAET)", "2.57\u00d710\u207b\u2079", "1"],
    ["Global Warming Potential (GWP)",         "1.05\u00d710\u207b\u2079", "2"],
    ["Eutrophication",                         "6.89\u00d710\u207b\u00b9\u2070","3"],
    ["Acidification",                          "1.63\u00d710\u207b\u00b9\u2070","4"],
    ["Ozone Layer Depletion (ODP)",            "6.84\u00d710\u207b\u00b9\u00b3","5"],
]
cw4 = [8.0*cm, 4.2*cm, 1.4*cm]
norm_data = norm_hdr + [
    [Paragraph(c, sTCL if i==0 else sTC) for i,c in enumerate(r)]
    for r in norm_rows]
norm_t = Table(norm_data, colWidths=cw4, repeatRows=1)
norm_t.setStyle(tblstyle(1))
norm_t.setStyle(TableStyle([("FONTNAME",(0,1),(-1,1),"Helvetica-Bold")]))
story += [norm_t, sp(6),
    body("Normalization confirms that <b>Fresh Water Aquatic Ecotoxicity (FAET) is the dominant "
         "environmental impact category</b> in this production system, indicating that tofu "
         "production exerts the greatest relative pressure on freshwater ecosystems. This finding "
         "underscores that organic liquid waste management, particularly the treatment of effluents "
         "from the washing, soaking, and coagulation stages, constitutes the most critical "
         "environmental challenge in the analyzed production system."),
    body("Although Global Warming Potential frequently receives primary attention in environmental "
         "sustainability discourse, its normalized contribution ranks second in this study, "
         "indicating that freshwater pollution represents a more acute environmental concern at "
         "the facility scale assessed. Eutrophication, which ranks third in normalized impact, "
         "further reinforces the urgency of addressing nutrient-laden wastewater streams as a "
         "priority intervention. Acidification and Ozone Layer Depletion, while present, "
         "contribute relatively minor normalized values, suggesting that their management, though "
         "important, does not constitute the primary environmental priority for this production "
         "system."),
]

# ── 3.4 Hotspot Identification and Improvement Strategies ─────────────────────
story += [
    h2("3.4", "Hotspot Identification and Improvement Strategies"),
    body("The integrated analysis of LCIA results and normalization outcomes identifies two primary "
         "environmental hotspots in the tofu production system, namely the generation of organic "
         "liquid waste across the washing, soaking, and coagulation stages, and the combustion of "
         "firewood during the boiling stage. These hotspots correspond, respectively, to the "
         "dominant drivers of Fresh Water Aquatic Ecotoxicity and Eutrophication (ranked first "
         "and third in normalized impact), and of Global Warming Potential and water scarcity."),
    body("With respect to the first hotspot, the organic-laden wastewater streams generated during "
         "washing, soaking, and coagulation are characterized by high BOD, COD, and nutrient "
         "loads [13, 14], and their uncontrolled discharge poses significant risks to receiving "
         "aquatic ecosystems. The implementation of anaerobic treatment systems, such as "
         "biodigesters or integrated biogas wastewater treatment units, represents an effective "
         "and technically appropriate intervention for SME-scale operations, as such systems "
         "simultaneously reduce organic loading while generating biogas as a recoverable energy "
         "resource. Complementary measures include the application of constructed wetland or "
         "biofilter systems for tertiary nutrient removal prior to effluent discharge, as well as "
         "counter-current water recycling and recirculation within the washing and soaking stages "
         "to reduce both volumetric water consumption and wastewater generation. Furthermore, the "
         "valorization of whey, for instance as a protein-rich substrate for animal feed or as a "
         "feedstock for fermentation processes, offers a viable pathway for diverting high-nutrient "
         "liquid streams away from the wastewater treatment system, thereby reducing the overall "
         "nutrient load requiring treatment [10]."),
    body("With respect to the second hotspot, the boiling stage contributes disproportionately to "
         "GWP and water scarcity owing to its reliance on firewood as the primary thermal energy "
         "source. The combustion of 800\u202fkg of firewood per production batch releases "
         "1,397\u202fkg CO\u2082, 0.0499\u202fkg CH\u2084, and 0.3744\u202fkg N\u2082O, "
         "collectively representing a substantial greenhouse gas burden. Transitioning to cleaner "
         "energy sources, such as liquefied petroleum gas (LPG) or biomethane derived from "
         "on-site biodigesters, would directly reduce these emissions while also decreasing the "
         "upstream water footprint associated with firewood supply chains. In parallel, the "
         "adoption of improved combustion systems or thermally insulated boiling tanks would reduce "
         "specific fuel consumption per unit of output through minimization of heat loss, while "
         "waste heat recovery from boiler exhaust could be directed toward pre-heating process "
         "water at upstream stages, thereby improving overall energy efficiency. The LCA-based "
         "analysis demonstrates that improvement interventions targeting liquid waste management "
         "and energy use efficiency at the source generate substantially greater environmental "
         "benefits than conventional end-of-pipe approaches [10, 15]."),
]


# ══════════════════════════════════════════════════════════════════════════════
# 4. CONCLUSION
# ══════════════════════════════════════════════════════════════════════════════
story += [
    h1("4", "Conclusion"),
    body("This study applied Life Cycle Assessment with a gate-to-gate system boundary to evaluate "
         "the environmental performance of small-scale tofu production at an SME in Semarang City. "
         "The assessment encompassed five impact categories under the CML-IA Baseline method, "
         "supplemented by water scarcity analysis using the AWARE method, and yielded quantitative "
         "evidence on the distribution of environmental burdens across all production stages."),
    body("The results demonstrate that tofu production generates measurable impacts across all "
         "assessed categories, with total values of 5.28\u00d710\u00b3\u202fkg CO\u2082\u202feq "
         "for GWP, 6.11\u00d710\u207b\u2075\u202fkg CFC-11\u202feq for ODP, "
         "1.33\u00d710\u00b3\u202fkg 1,4-DB\u202feq for FAET, 4.59\u202fkg SO\u2082\u202feq for "
         "Acidification, and 9.10\u202fkg PO\u2084\u00b3\u207b\u202feq for Eutrophication. The "
         "washing and boiling stages consistently emerge as the principal contributors across all "
         "impact categories, driven by high water consumption and firewood combustion, "
         "respectively. Normalization of these results reveals that Fresh Water Aquatic Ecotoxicity "
         "constitutes the dominant environmental impact category, with a normalized value of "
         "2.57\u00d710\u207b\u2079, confirming that the organic liquid waste streams generated "
         "throughout the production process represent the most critical environmental hotspot. "
         "Water scarcity, as assessed by the AWARE method, totals 515\u202fm\u00b3 world\u202feq, "
         "with the boiling stage accounting for 57.1% of this burden, a value that reflects not "
         "only direct water use but also the embedded water demand of firewood procurement and "
         "combustion."),
    body("These findings indicate that environmental improvement efforts should be strategically "
         "directed toward two priority areas. The first is the establishment of structured liquid "
         "waste management systems, including anaerobic treatment, nutrient recovery, and water "
         "recycling, to address the dominant freshwater ecotoxicity and eutrophication burdens "
         "arising from washing, soaking, and coagulation effluents. The second is the substitution "
         "of firewood with cleaner fuel alternatives and the adoption of energy-efficient thermal "
         "systems in the boiling stage, which would simultaneously reduce greenhouse gas emissions, "
         "acidification potential, and water scarcity impacts. These conclusions are consistent "
         "with broader findings in the LCA literature on soy-based food processing, which "
         "collectively emphasize the critical importance of wastewater management and energy source "
         "selection as the primary levers for environmental performance improvement in tofu "
         "production systems [8, 9]. The findings of this study provide actionable, "
         "evidence-based guidance for plant operators and policymakers seeking to improve the "
         "environmental sustainability of SME-scale tofu production, and may inform the development "
         "of sector-specific environmental management standards for the tofu industry in Semarang "
         "City and Central Java."),
]

# ══════════════════════════════════════════════════════════════════════════════
# REFERENCES
# ══════════════════════════════════════════════════════════════════════════════
story += [
    rule(0.7),
    Paragraph("<b>References</b>", sH1),
    Paragraph(
        "<font color='#b45309'>\u2605</font> = reference validity could not be independently "
        "confirmed; authors should verify prior to journal submission.",
        sNote),
    sp(4),
]

refs = [
    ("[1]", "Ghisellini, P., Cialani, C. & Ulgiati, S. (2016). A review on circular economy: "
            "The expected transition to a balanced interplay of environmental and economic systems. "
            "<i>Journal of Cleaner Production</i>, 114, 11\u201332. "
            "https://doi.org/10.1016/j.jclepro.2015.09.007", False),
    ("[2] \u2605", "Dewi, A.\u202fN. & Setiawan, D. (2024). Bisnis kuliner: Studi kasus CV. Gehu "
            "Extra Pedas Chili Hot. <i>Jurnal Manajemen dan Bisnis Islam</i>, 1(1), 5\u201323. "
            "[<font color='#b45309'>Note: Cited for BPS per capita consumption data; journal "
            "relevance to LCA data source could not be independently verified. Consider replacing "
            "with a direct BPS statistical publication.</font>]", True),
    ("[3]", "Rosyidah, M., Masruri, A. & Putra, R.\u202fA. (2020). Assessment (LCA) method on "
            "tofu production. <i>International Journal of Science, Technology and Management</i>, "
            "1(4), 428\u2013435.", False),
    ("[4]", "Sjafruddin, R., Agustang, A. & Pertiwi, N. (2022). Estimasi limbah industri tahu "
            "dan kajian penerapan sistem produksi bersih. "
            "<i>Jurnal Ilmiah Mandala Education</i>, 8(2), 1229\u20131237. "
            "https://doi.org/10.36312/jime.v8i2.2826", False),
    ("[5] \u2605", "Islami, M.\u202fC.\u202fP.\u202fA. & Harnaningrum, R.\u202fN. (2025). "
            "Integration of waste management and environmental impact assessment for sustainable "
            "manufacturing in Sukolego tofu production. "
            "<i>[Journal name not specified in source document]</i>, 6(2), 71\u201377. "
            "[<font color='#b45309'>Note: Journal name is missing. Authors must complete this "
            "reference before submission.</font>]", True),
    ("[6]", "Hauschild, M.\u202fZ., Rosenbaum, R.\u202fK. & Olsen, S.\u202fI. (2017). "
            "<i>Life Cycle Assessment: Theory and Practice</i>. Springer, Cham. "
            "https://doi.org/10.1007/978-3-319-56475-3", False),
    ("[7]", "Chitaka, T.\u202fY. & Goga, T. (2023). The evolution of life cycle assessment in "
            "the food and beverage industry: A review. "
            "<i>Cambridge Prisms: Plastics</i>, 1, 1\u20136. "
            "https://doi.org/10.1017/plc.2023.4", False),
    ("[8]", "Nugroho, M.\u202fE., Setyono, P. & Rachmawati, S. (2024). Analisis emisi gas rumah "
            "kaca dengan Life Cycle Assessment (LCA) dan Analytical Hierarchy Process (AHP) "
            "industri tahu. <i>Jurnal Ilmu Lingkungan</i>, 22(6), 1504\u20131512. "
            "https://doi.org/10.14710/jil.22.6.1504-1512", False),
    ("[9]", "Kartika Wardana, S. et al. (2024). Penilaian dampak lingkungan dengan LCA pada "
            "industri tahu Kampung Jangkar Kulon, Cilegon Banten. "
            "<i>Jurnal Teknologi Kimia Unimal</i>, 13(2), 97\u2013106. "
            "https://doi.org/10.29103/jtku.v13i2.16429", False),
    ("[10]","Bj\u00f8rnbet, M.\u202fM. & Vild\u00e5sen, S.\u202fS. (2021). Life cycle assessment "
            "to ensure sustainability of circular business models in manufacturing. "
            "<i>Sustainability</i>, 13(19), article 11014. "
            "https://doi.org/10.3390/su131911014", False),
    ("[11]","Saavedra-Rubio, K. et al. (2022). Stepwise guidance for data collection in the LCI "
            "phase: Building technology-related LCI blocks. "
            "<i>Journal of Cleaner Production</i>, 366, article 132903. "
            "https://doi.org/10.1016/j.jclepro.2022.132903", False),
    ("[12] \u2605","Rasyid, M. & Anggriani, R. (2024). Penerapan LCA pada proses produksi minyak "
            "kayu putih di Desa Sawa-Namlea. "
            "<i>Journal of Social Science Research</i>, 4(3), 18970\u201318984. "
            "[<font color='#b45309'>Note: Journal peer-review status could not be confirmed. "
            "Consider replacing with ISO\u202f14044:2006 or a verified LCA methodology "
            "reference.</font>]", True),
    ("[13]","Seroja, R., Effendi, H. & Hariyadi, S. (2018). Tofu wastewater treatment using "
            "vetiver grass (<i>Vetiveria zizanioides</i>) and zeliac. "
            "<i>Applied Water Science</i>, 8(1), 1\u20136. "
            "https://doi.org/10.1007/s13201-018-0640-y", False),
    ("[14]","Satar, I. & Permadi, A. (2022). Treating the tofu wastewater (TWW) using a green "
            "technology of microbial fuel cell (MFC) system. "
            "<i>Indonesian Journal of Environmental Management and Sustainability</i>, "
            "6(1), 162\u2013167.", False),
    ("[15]","Apriyanti, D., Pratikno, F.\u202fA. & Hertadi, C.\u202fD.\u202fP. (2025). "
            "Penilaian dampak lingkungan menggunakan LCA pada proses produksi tempe di SIKS. "
            "<i>Jurnal Mitra Teknik Industri</i>, 4(1), 19\u201327. "
            "https://doi.org/10.24912/jmti.v4i1.34600", False),
]

for num, text, _flag in refs:
    # number + text side by side using a mini table for hanging indent
    row = [[Paragraph(f"<b>{num}</b>", sTC),
            Paragraph(text, sRef)]]
    rt = Table(row, colWidths=[1.1*cm, W-1.1*cm])
    rt.setStyle(TableStyle([
        ("VALIGN",       (0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",  (0,0),(-1,-1), 0),
        ("RIGHTPADDING", (0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1), 2),
    ]))
    story.append(rt)

# ══════════════════════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════════════════════
doc.build(story, onFirstPage=page_num, onLaterPages=page_num)
print(f"PDF generated: {OUTPUT}")
