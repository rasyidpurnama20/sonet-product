#!/usr/bin/env python3
"""
Generate a compiled PDF from all OSN 2026 Informatika markdown files.
Produces a single long-form PDF with a clickable Table of Contents.
"""

import subprocess
import os
import re
import markdown
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(BASE_DIR, "osn-2026-informatika-kompilasi.pdf")

# Files in order: materi first, then latihan
MATERI_FILES = [
    "materi/01-aljabar-boolean-dan-logika.md",
    "materi/02-teori-himpunan.md",
    "materi/03-kombinatorika-dan-deret.md",
    "materi/04-graf-dan-pohon.md",
    "materi/05-algoritma-dasar-cpp.md",
    "materi/06-modulo-dan-teori-bilangan.md",
    "materi/07-teori-graf-lanjutan.md",
]

LATIHAN_FILES = [
    "latihan/latihan-01-aljabar-boolean-dan-logika.md",
    "latihan/latihan-02-teori-himpunan.md",
    "latihan/latihan-03-kombinatorika-dan-deret.md",
    "latihan/latihan-04-graf-dan-pohon.md",
    "latihan/latihan-05-algoritma-dasar-cpp.md",
    "latihan/latihan-06-modulo-dan-teori-bilangan.md",
    "latihan/latihan-07-teori-graf-lanjutan.md",
    "latihan/tryout-koja-1-pembahasan.md",
]

ALL_FILES = MATERI_FILES + LATIHAN_FILES


def slugify(text):
    """Create a URL-friendly slug from text."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


def extract_title(filepath):
    """Extract the first H1 heading from a markdown file."""
    full_path = os.path.join(BASE_DIR, filepath)
    with open(full_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
    # Fallback: use filename
    return os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()


def read_markdown(filepath):
    """Read markdown content from file."""
    full_path = os.path.join(BASE_DIR, filepath)
    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()


def build_toc(files):
    """Build a table of contents with links."""
    toc_items = []

    toc_items.append("## BAGIAN I: MATERI")
    for i, filepath in enumerate(MATERI_FILES):
        title = extract_title(filepath)
        anchor = f"section-{i+1}"
        toc_items.append(f"  {i+1}. [{title}](#{anchor})")

    toc_items.append("")
    toc_items.append("## BAGIAN II: LATIHAN")
    offset = len(MATERI_FILES)
    for i, filepath in enumerate(LATIHAN_FILES):
        title = extract_title(filepath)
        anchor = f"section-{offset+i+1}"
        toc_items.append(f"  {i+1}. [{title}](#{anchor})")

    return "\n".join(toc_items)


def build_full_markdown():
    """Build the complete markdown document."""
    parts = []

    # Title page
    parts.append("# Kompilasi Materi & Latihan OSN 2026 Informatika\n")
    parts.append("**Disusun untuk persiapan Olimpiade Sains Nasional (OSN) 2026**\n")
    parts.append("**Bidang: Informatika/Komputer**\n")
    parts.append("\n---\n")

    # Table of Contents
    parts.append("# Daftar Isi\n")
    parts.append(build_toc(ALL_FILES))
    parts.append("\n---\n")

    # Content sections
    for i, filepath in enumerate(ALL_FILES):
        anchor = f"section-{i+1}"
        content = read_markdown(filepath)
        # Add anchor div before the section content
        parts.append(f'\n<div id="{anchor}"></div>\n')
        parts.append(content)
        parts.append("\n\n---\n\n")

    return "\n".join(parts)


def markdown_to_html(md_text):
    """Convert markdown to HTML with extensions."""
    extensions = [
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
    ]
    extension_configs = {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
        },
        'markdown.extensions.toc': {
            'permalink': False,
        },
    }
    html = markdown.markdown(
        md_text,
        extensions=extensions,
        extension_configs=extension_configs,
    )
    return html


CSS_STYLES = """
@page {
    size: A4;
    margin: 2cm 2.5cm;
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
        color: #555;
    }
}

body {
    font-family: 'DejaVu Sans', 'Noto Sans', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #222;
    max-width: 100%;
}

h1 {
    font-size: 22pt;
    color: #1a237e;
    border-bottom: 3px solid #1a237e;
    padding-bottom: 8px;
    margin-top: 40px;
    page-break-before: always;
}

h1:first-of-type {
    page-break-before: avoid;
}

h2 {
    font-size: 16pt;
    color: #283593;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    margin-top: 30px;
}

h3 {
    font-size: 13pt;
    color: #3949ab;
    margin-top: 20px;
}

h4 {
    font-size: 12pt;
    color: #5c6bc0;
    margin-top: 16px;
}

code {
    font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
    font-size: 9.5pt;
    background-color: #f5f5f5;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e0e0e0;
}

pre {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    padding: 12px 16px;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 12px 0;
}

pre code {
    background-color: transparent;
    border: none;
    padding: 0;
    font-size: 9pt;
    line-height: 1.4;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #bbb;
    padding: 6px 10px;
    text-align: left;
}

th {
    background-color: #e8eaf6;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f5f5f5;
}

blockquote {
    border-left: 4px solid #7986cb;
    margin: 12px 0;
    padding: 8px 16px;
    background-color: #e8eaf6;
    font-style: italic;
}

hr {
    border: none;
    border-top: 2px solid #e0e0e0;
    margin: 30px 0;
}

ul, ol {
    margin: 8px 0;
    padding-left: 24px;
}

li {
    margin-bottom: 4px;
}

strong {
    color: #1a237e;
}

a {
    color: #1565c0;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* TOC styling */
#daftar-isi + h2,
#daftar-isi ~ h2 {
    page-break-before: avoid;
}

.toc-section {
    margin: 20px 0;
}

/* Highlight / code hilite */
.highlight {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    padding: 12px 16px;
    margin: 12px 0;
    page-break-inside: avoid;
}

/* Keep headings with content */
h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
}

/* Image sizing */
img {
    max-width: 100%;
    height: auto;
}

/* Cover page styling */
.cover-title {
    text-align: center;
    font-size: 28pt;
    margin-top: 200px;
}
"""


def generate_pdf():
    """Generate the compiled PDF."""
    print("Building full markdown document...")
    full_md = build_full_markdown()

    print(f"Total markdown length: {len(full_md)} characters")

    print("Converting markdown to HTML...")
    html_body = markdown_to_html(full_md)

    # Wrap in full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <title>Kompilasi Materi & Latihan OSN 2026 Informatika</title>
    <style>
    {CSS_STYLES}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

    # Save intermediate HTML for debugging
    html_path = os.path.join(BASE_DIR, "_compiled.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Intermediate HTML saved to: {html_path}")

    print("Generating PDF with WeasyPrint...")
    html_obj = HTML(string=full_html, base_url=BASE_DIR)
    html_obj.write_pdf(OUTPUT_PDF)

    # Clean up intermediate file
    os.remove(html_path)

    file_size = os.path.getsize(OUTPUT_PDF)
    print(f"PDF generated successfully: {OUTPUT_PDF}")
    print(f"File size: {file_size / (1024*1024):.2f} MB")


if __name__ == "__main__":
    generate_pdf()
