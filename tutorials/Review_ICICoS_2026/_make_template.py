"""
_make_template.py
Membuat review-template.docx — form review ICICoS 2026.
Jalankan sekali: python3 _make_template.py
Ganti dengan template resmi panitia jika sudah tersedia.
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


def sf(run, bold=False, size=11, color=None):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)


def heading(doc, text, center=False):
    p = doc.add_paragraph()
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    sf(r, bold=True, size=14 if center else 11)


def divider(doc):
    p = doc.add_paragraph("─" * 68)
    sf(p.runs[0], size=8, color=(0xAA, 0xAA, 0xAA))


def inline_field(doc, label):
    p = doc.add_paragraph()
    sf(p.add_run(label), bold=True)
    sf(p.add_run("  "))
    sf(p.add_run("[...]"))


def block_field(doc, label):
    p = doc.add_paragraph()
    sf(p.add_run(label), bold=True)
    p2 = doc.add_paragraph()
    p2.paragraph_format.left_indent = Inches(0.25)
    sf(p2.add_run("[...]"))
    doc.add_paragraph()


def decision_field(doc, label, options):
    p = doc.add_paragraph()
    sf(p.add_run(label), bold=True)
    p2 = doc.add_paragraph()
    p2.paragraph_format.left_indent = Inches(0.25)
    for i, opt in enumerate(options):
        sf(p2.add_run(opt))
        if i < len(options) - 1:
            sf(p2.add_run(" / "))
    doc.add_paragraph()


doc = Document()
for s in doc.sections:
    s.top_margin = s.bottom_margin = Inches(1.0)
    s.left_margin = s.right_margin = Inches(1.25)

heading(doc, "REVIEW FORM — ICICoS 2026", center=True)
heading(doc, "International Conference on Information and Communication Technology", center=True)
divider(doc)

p = doc.add_paragraph(); sf(p.add_run("PAPER IDENTITY"), bold=True, size=10, color=(0x55,0x55,0x55))
inline_field(doc, "Paper ID      :")
inline_field(doc, "Paper Title   :")
inline_field(doc, "Reviewer ID   :")
divider(doc)

p = doc.add_paragraph(); sf(p.add_run("EVALUATION SCORES   (1 = Very Poor  ·  3 = Acceptable  ·  5 = Excellent)"), bold=True, size=10, color=(0x55,0x55,0x55))
inline_field(doc, "1.  Originality / Novelty          :")
inline_field(doc, "2.  Technical Quality              :")
inline_field(doc, "3.  Clarity of Presentation        :")
inline_field(doc, "4.  Relevance to ICICoS            :")
inline_field(doc, "5.  Quality of References          :")
inline_field(doc, "6.  Overall Score                  :")
divider(doc)

p = doc.add_paragraph(); sf(p.add_run("REVIEW COMMENTS"), bold=True, size=10, color=(0x55,0x55,0x55))
block_field(doc, "7.  Summary of the Paper")
block_field(doc, "8.  Strengths")
block_field(doc, "9.  Weaknesses and Suggestions for Improvement")
block_field(doc, "10. Questions for Authors  (optional — leave blank if none)")
block_field(doc, "11. Confidential Comments to Editor  (optional — not shown to authors)")
divider(doc)

p = doc.add_paragraph(); sf(p.add_run("DECISION"), bold=True, size=10, color=(0x55,0x55,0x55))
decision_field(doc, "12. Overall Recommendation", ["Accept", "Minor Revision", "Major Revision", "Reject"])
decision_field(doc, "13. Reviewer Confidence",    ["Expert", "Knowledgeable", "Passing Knowledge", "Basic"])
divider(doc)

p = doc.add_paragraph("Thank you for your contribution to ICICoS 2026.")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
sf(p.runs[0], size=9, color=(0x88,0x88,0x88))

doc.save("form-review-icicos.docx")
print("✅  form-review-icicos.docx created.")
