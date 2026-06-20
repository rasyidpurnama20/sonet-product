"""
fill_review.py — ICICoS 2026 Review Template Filler
Mengisi review-template.docx: mengganti [...] dan menebalkan keputusan.
Dependensi: pip install python-docx
Penggunaan: python3 fill_review.py  →  output: review-filled.docx
"""
from docx import Document

# ══════════════════════════════════════════════════════
#  BAGIAN 1 — ISI DATA REVIEW DI SINI
# ══════════════════════════════════════════════════════
review_data = {
    "paper_id"          : "ICICoS-2026-042",
    "paper_title"       : "Adaptive Deep Learning for Earthquake Early Warning",
    "reviewer_id"       : "R-07",
    "score_originality" : "4",
    "score_technical"   : "3",
    "score_clarity"     : "4",
    "score_relevance"   : "5",
    "score_references"  : "3",
    "score_overall"     : "4",
    "summary"     : (
        "This paper proposes an adaptive deep learning framework for seismic "
        "early warning that dynamically adjusts model architecture based on "
        "incoming signal quality. The authors evaluate their approach on two "
        "public datasets and report improvements over conventional CNN baselines."
    ),
    "strengths"   : (
        "1. The adaptive signal-quality gating mechanism is a genuine novelty "
        "not observed in prior ICICoS submissions.\n"
        "2. Results on both STEAD and INSTANCE datasets are consistent and "
        "clearly presented in Table 2.\n"
        "3. The writing is well-structured and the introduction provides "
        "strong motivation."
    ),
    "weaknesses"  : (
        "1. Baseline comparison (Section 4.2) omits PhaseNet and EQTransformer. "
        "Please add or justify their exclusion.\n"
        "2. No ablation study is provided; the contribution of the gating "
        "mechanism versus the backbone cannot be isolated.\n"
        "3. All experiments use a single random seed. Please report mean ± std "
        "over at least 3 runs."
    ),
    "questions"   : (
        "1. How does the gating mechanism behave when signal quality degrades "
        "gradually versus abruptly? Is there a latency penalty?\n"
        "2. What is the inference time on a CPU-only edge device?"
    ),
    "confidential": "",
    # Pilih PERSIS: "Accept" | "Minor Revision" | "Major Revision" | "Reject"
    "decision"    : "Minor Revision",
    # Pilih PERSIS: "Expert" | "Knowledgeable" | "Passing Knowledge" | "Basic"
    "confidence"  : "Knowledgeable",
}

# ══════════════════════════════════════════════════════
#  BAGIAN 2 — KONFIGURASI
# ══════════════════════════════════════════════════════
TEMPLATE_PATH = "form-review-icicos.docx"
OUTPUT_PATH   = "review-filled.docx"

INLINE_FIELDS = {
    "Paper ID"          : "paper_id",
    "Paper Title"       : "paper_title",
    "Reviewer ID"       : "reviewer_id",
    "Originality"       : "score_originality",
    "Technical Quality" : "score_technical",
    "Clarity"           : "score_clarity",
    "Relevance"         : "score_relevance",
    "Quality of Ref"    : "score_references",
    "Overall Score"     : "score_overall",
}
BLOCK_LABELS = {
    "Summary of the Paper"      : "summary",
    "Strengths"                 : "strengths",
    "Weaknesses"                : "weaknesses",
    "Questions for Authors"     : "questions",
    "Confidential Comments"     : "confidential",
}
DECISION_LABELS = {
    "Overall Recommendation"    : "decision",
    "Reviewer Confidence"       : "confidence",
}

# ══════════════════════════════════════════════════════
#  BAGIAN 3 — FUNGSI INTI
# ══════════════════════════════════════════════════════
def fill_inline(para, value):
    for run in para.runs:
        if "[...]" in run.text:
            run.text = run.text.replace("[...]", value)
            return True
    return False

def fill_block(para, value):
    full = "".join(r.text for r in para.runs)
    if "[...]" not in full:
        return False
    if para.runs:
        para.runs[0].text = value
        for r in para.runs[1:]:
            r.text = ""
    return True

def bold_selection(para, selected):
    for run in para.runs:
        t = run.text.strip()
        if t and t != "/":
            run.bold = (t == selected)
    return True

# ══════════════════════════════════════════════════════
#  BAGIAN 4 — PROSES & VERIFIKASI
# ══════════════════════════════════════════════════════
def process(template_path, output_path, data):
    doc = Document(template_path)
    pending_block = pending_decision = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if pending_block:
            if "[...]" in para.text:
                fill_block(para, data.get(pending_block, ""))
            pending_block = None
            continue
        if pending_decision:
            bold_selection(para, data.get(pending_decision, ""))
            pending_decision = None
            continue
        for kw, fk in INLINE_FIELDS.items():
            if kw in text and "[...]" in text:
                fill_inline(para, data.get(fk, ""))
                break
        for kw, fk in BLOCK_LABELS.items():
            if kw in text:
                pending_block = fk
                break
        for kw, fk in DECISION_LABELS.items():
            if kw in text:
                pending_decision = fk
                break

    doc.save(output_path)
    print(f"\n✅  Tersimpan : {output_path}")
    print(f"    Decision  : {data['decision']}  (ditebalkan di item 12)")
    print(f"    Confidence: {data['confidence']}  (ditebalkan di item 13)")

def verify(output_path, data):
    doc = Document(output_path)
    errors, dec_ok, conf_ok = [], False, False
    for para in doc.paragraphs:
        if "[...]" in para.text:
            errors.append(f"  ⚠  Belum terisi: '{para.text[:60]}'")
        for run in para.runs:
            if run.text.strip() == data["decision"] and run.bold:
                dec_ok = True
            if run.text.strip() == data["confidence"] and run.bold:
                conf_ok = True
    print("\n── Verifikasi ──────────────────────────────────────────")
    print("  ✓  Tidak ada [...] tertinggal" if not errors else "\n".join(errors))
    print(f"  {'✓' if dec_ok  else '✗'}  Decision   '{data['decision']}'")
    print(f"  {'✓' if conf_ok else '✗'}  Confidence '{data['confidence']}'")

if __name__ == "__main__":
    process(TEMPLATE_PATH, OUTPUT_PATH, review_data)
    verify(OUTPUT_PATH, review_data)
