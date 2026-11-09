#!/usr/bin/env python3
"""Build fillable DOCX and XLSX files from the Markdown templates in vorlagen/.

Usage:  uv run --with python-docx --with openpyxl --with fonttools --with brotli
            python tools/build_vorlagen.py
Output: vorlagen/docx/NN_*.docx (all templates 01-09) and
        vorlagen/xlsx/01_ki_inventar.xlsx, vorlagen/xlsx/04_teilnehmerliste.xlsx

The Markdown files are the single source of truth. The converter understands headings,
paragraphs, tables, lists, block quotes, horizontal rules and **bold**/*italic*/`code`.

Layout follows the PINGEL AI Solutions brand (fabian-pingel.de): Red Hat Display for
headings, Red Hat Text for body text, navy #182145 and signal blue #2b5fe8. The fonts
are embedded into every DOCX, so the documents look right on machines without Red Hat
installed. Excel cannot embed fonts; there Red Hat is used if installed, otherwise
Excel falls back to its default font.
"""

from __future__ import annotations

import io
import re
import uuid
from pathlib import Path

from docx import Document
from docx.document import Document as DocumentObject
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.packuri import PackURI
from docx.opc.part import Part
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.styles.style import BaseStyle
from docx.table import _Cell
from docx.text.paragraph import Paragraph
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from lxml import etree
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "vorlagen"
OUT_DOCX = SRC / "docx"
OUT_XLSX = SRC / "xlsx"
FONT_DIR = ROOT / "fonts"
LOGO = ROOT / "tools" / "assets" / "logo-wordmark.png"

# Markentokens, siehe pingel-ai-website/brand/tokens.css
NAVY = "182145"
ACCENT = "2B5FE8"  # Signalblau
TEXT = "1A2340"
MUTED = "56658A"
BORDER_COLOR = "DBE2F0"
BG = "F4F7FC"
BG_ALT = "EBF0FA"
TINT = "E6EDFF"

FONT_TEXT = "Red Hat Text"
FONT_DISPLAY = "Red Hat Display"
FONT_CODE = "Consolas"

STAND = "11/2026"
FOOTER = f"EU AI Act für kleine Organisationen · PINGEL AI Solutions · Stand {STAND} · CC BY 4.0 · Kein Rechtsrat"

# Mittlere Zeichenbreite bei 9 pt Tabellenschrift, für die Verteilung der Spaltenbreiten
CHAR_WIDTH = Cm(0.19)
# Ab so vielen Spalten wird ein Dokument im Querformat gesetzt (KI-Inventar)
LANDSCAPE_COLUMNS = 10

INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def rgb(hex_color: str) -> RGBColor:
    """Convert a hex color token like "182145" to a python-docx color."""
    return RGBColor.from_string(hex_color)


# ─────────────────────────── Schriften einbetten ───────────────────────────


def static_instance(woff2: Path, weight: int) -> bytes:
    """Cut a static TrueType instance out of a variable WOFF2 font.

    Word can neither read WOFF2 nor embed variable fonts reliably, so each needed
    weight becomes its own TTF with proper family and style names.

    Args:
        woff2: Path to the variable font.
        weight: Value for the wght axis (400 regular, 700 bold).

    Returns:
        The TTF file content.
    """
    font = instancer.instantiateVariableFont(TTFont(woff2), {"wght": weight}, updateFontNames=True)
    font.flavor = None
    buf = io.BytesIO()
    font.save(buf)
    return buf.getvalue()


def load_embedded_fonts() -> dict[str, dict[str, bytes]]:
    """Prepare the font files to embed, keyed by family and Word embed slot.

    Returns:
        Mapping family name -> {"embedRegular"/"embedBold"/...: TTF bytes}.
    """
    text = FONT_DIR / "RedHatText-latin.woff2"
    italic = FONT_DIR / "RedHatText-Italic-latin.woff2"
    display = FONT_DIR / "RedHatDisplay-latin.woff2"
    return {
        FONT_TEXT: {
            "embedRegular": static_instance(text, 400),
            "embedBold": static_instance(text, 700),
            "embedItalic": static_instance(italic, 400),
            "embedBoldItalic": static_instance(italic, 700),
        },
        FONT_DISPLAY: {
            "embedRegular": static_instance(display, 400),
            "embedBold": static_instance(display, 700),
        },
    }


def obfuscate(data: bytes, key: str) -> bytes:
    """Obfuscate a font for embedding as required by ECMA-376 Part 1, 17.8.1.

    The first 32 bytes are XORed with the GUID from w:fontKey, read as bytes in
    reverse order of its hex notation.

    Args:
        data: The TTF file content.
        key: GUID without braces, e.g. "0A1B...".

    Returns:
        The obfuscated font (.odttf).
    """
    key_bytes = bytes.fromhex(key.replace("-", ""))[::-1]
    head = bytes(b ^ key_bytes[i % 16] for i, b in enumerate(data[:32]))
    return head + data[32:]


def embed_fonts(doc: DocumentObject, fonts: dict[str, dict[str, bytes]]) -> None:
    """Embed the given fonts into the document's font table.

    Args:
        doc: The document to modify.
        fonts: Output of load_embedded_fonts().
    """
    font_table = doc.part.part_related_by(RT.FONT_TABLE)
    root = etree.fromstring(font_table.blob)
    for family, slots in fonts.items():
        el = OxmlElement("w:font")
        el.set(qn("w:name"), family)
        for tag, val in (("w:charset", "00"), ("w:family", "swiss"), ("w:pitch", "variable")):
            child = OxmlElement(tag)
            child.set(qn("w:val"), val)
            el.append(child)
        for slot, data in slots.items():
            # Fester Schlüssel je Schnitt: gleiche Eingabe ergibt gleiche Datei, kein Git-Rauschen
            key = str(uuid.uuid5(uuid.NAMESPACE_URL, f"pingel-font/{family}/{slot}")).upper()
            name = family.replace(" ", "") + "-" + slot.removeprefix("embed")
            part = Part(
                PackURI(f"/word/fonts/{name}.odttf"),
                "application/vnd.openxmlformats-officedocument.obfuscatedFont",
                obfuscate(data, key),
                doc.part.package,
            )
            embed = OxmlElement(f"w:{slot}")
            embed.set(qn("r:id"), font_table.relate_to(part, RT.FONT))
            embed.set(qn("w:fontKey"), "{" + key + "}")
            el.append(embed)
        root.append(el)
    font_table._blob = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    # Ohne diesen Schalter ignoriert Word die eingebetteten Schriften; er steht laut Schema hinter w:zoom
    settings = doc.settings.element
    settings.find(qn("w:zoom")).addnext(OxmlElement("w:embedTrueTypeFonts"))
    # Die python-docx-Vorlage ist als Word 2010 markiert; 15 = aktuelles Format, kein „Kompatibilitätsmodus“
    for setting in settings.iter(qn("w:compatSetting")):
        if setting.get(qn("w:name")) == "compatibilityMode":
            setting.set(qn("w:val"), "15")


# ─────────────────────────── Formatierungshelfer ───────────────────────────


def set_rfonts(rpr: etree._Element, family: str) -> None:
    """Set an explicit font on a run or style property element.

    Theme attributes (asciiTheme etc.) take precedence over explicit names in Word,
    so they are removed.

    Args:
        rpr: A w:rPr element.
        family: Font family name.
    """
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
        rfonts.attrib.pop(qn(f"w:{attr}"), None)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{attr}"), family)


def style_text(style: BaseStyle, family: str, size: float, color: str, bold: bool = False) -> None:
    """Apply font family, size, color and weight to a paragraph style.

    Args:
        style: The style to change.
        family: Font family name.
        size: Font size in points.
        color: Hex color token.
        bold: Whether the style is bold.
    """
    set_rfonts(style.element.get_or_add_rPr(), family)
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = rgb(color)
    # Themenfarben haben in Word Vorrang vor dem RGB-Wert
    color_el = style.element.rPr.find(qn("w:color"))
    for attr in ("themeColor", "themeShade", "themeTint"):
        color_el.attrib.pop(qn(f"w:{attr}"), None)


def border_el(tag: str, color: str, size_eighths: int, space: int = 1) -> etree._Element:
    """Build a single border element like w:bottom or w:left.

    Args:
        tag: Element tag, e.g. "w:bottom".
        color: Hex color token.
        size_eighths: Line width in eighths of a point.
        space: Distance to the text in points.

    Returns:
        The border element.
    """
    el = OxmlElement(tag)
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(size_eighths))
    el.set(qn("w:space"), str(space))
    el.set(qn("w:color"), color)
    return el


def paragraph_border(ppr: etree._Element, side: str, color: str, size_eighths: int, space: int = 1) -> None:
    """Add a border on one side of a paragraph (or paragraph style).

    Args:
        ppr: A w:pPr element.
        side: "top", "bottom", "left" or "right".
        color: Hex color token.
        size_eighths: Line width in eighths of a point.
        space: Distance to the text in points.
    """
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        ppr.append(pbdr)
    pbdr.append(border_el(f"w:{side}", color, size_eighths, space))


def paragraph_shade(ppr: etree._Element, fill: str) -> None:
    """Give a paragraph a background color.

    Args:
        ppr: A w:pPr element.
        fill: Hex color token.
    """
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    ppr.append(shd)


def shade(cell: _Cell, fill: str) -> None:
    """Give a table cell a background color.

    Args:
        cell: The table cell.
        fill: Hex color token.
    """
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)


def add_runs(paragraph: Paragraph, text: str, size: float | None = None, color: str | None = None) -> None:
    """Add text with **bold**, *italic* and `code` markup as formatted runs.

    Args:
        paragraph: Target paragraph.
        text: Markdown inline text.
        size: Optional font size in points.
        color: Optional hex color token.
    """
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            set_rfonts(run._r.get_or_add_rPr(), FONT_CODE)
        else:
            run = paragraph.add_run(part)
        if size:
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = rgb(color)


def add_field(paragraph: Paragraph, instr: str, size: float, color: str) -> None:
    """Add a simple Word field such as PAGE or NUMPAGES.

    Args:
        paragraph: Target paragraph.
        instr: Field instruction.
        size: Font size in points.
        color: Hex color token.
    """
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    paragraph._p.append(fld)
    run = paragraph.add_run("1")
    run.font.size = Pt(size)
    run.font.color.rgb = rgb(color)
    fld.append(run._r)


# ─────────────────────────── Markdown → DOCX ───────────────────────────


def parse_table(lines: list[str]) -> list[list[str]]:
    """Split Markdown table lines into cell rows, dropping the separator row.

    Args:
        lines: Raw table lines starting with "|".

    Returns:
        Rows of stripped cell texts.
    """
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        # Trennzeile „|---|---|“; eine ganz leere Zeile („| | |“) ist dagegen ein leerer Kopf
        if any(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows


def column_widths(rows: list[list[str]], ncols: int, total: int) -> list[int]:
    """Distribute the table width over the columns by content.

    Every column gets at least the width of its longest word, so headers such as
    "Anzahl" are never broken letter by letter. Remaining space goes to columns with
    long text.

    Args:
        rows: Table rows including the header.
        ncols: Number of columns.
        total: Available width in EMU.

    Returns:
        Column widths in EMU.
    """
    minimum, desired = [], []
    for j in range(ncols):
        texts = [re.sub(r"[*`]", "", r[j]) if j < len(r) else "" for r in rows]
        longest_word = max((len(w) for t in texts for w in t.split()), default=1)
        # + 3 Zeichen für die Zellinnenabstände links und rechts
        lo = min(max(longest_word, 2), 16) + 3
        minimum.append(lo)
        desired.append(min(max(max(len(t) for t in texts), lo), 50))
    available = total / CHAR_WIDTH
    if sum(desired) <= available:
        chars = desired
    else:
        extra = max(available - sum(minimum), 0)
        slack = sum(d - m for d, m in zip(desired, minimum, strict=True)) or 1
        chars = [m + extra * (d - m) / slack for d, m in zip(desired, minimum, strict=True)]
    return [int(total * c / sum(chars)) for c in chars]


def add_table(doc: DocumentObject, rows: list[list[str]]) -> None:
    """Add a brand-styled table: navy header row, light rules, zebra rows.

    Tables with an empty header ("| | |") are key-value tables; their header is
    dropped and the key column is tinted instead.

    Args:
        doc: Target document.
        rows: Parsed table rows, header first.
    """
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    is_kv = not any(rows[0])
    if is_kv:
        rows = rows[1:]
    table = doc.add_table(rows=0, cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Feine Linien in Rahmenfarbe statt der schwarzen Gitterlinien von „Table Grid“
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        borders.append(border_el(f"w:{side}", BORDER_COLOR, 4, 0))
    table._tbl.tblPr.append(borders)

    section = doc.sections[-1]
    widths = column_widths(rows, ncols, section.page_width - section.left_margin - section.right_margin)
    table.autofit = False

    for i, row in enumerate(rows):
        tr = table.add_row()
        cells = tr.cells
        is_head = i == 0 and not is_kv
        if is_head:
            # Kopfzeile wiederholt sich beim Seitenumbruch
            tr_pr = tr._tr.get_or_add_trPr()
            tr_pr.append(OxmlElement("w:tblHeader"))
        for j in range(ncols):
            txt = row[j] if j < len(row) else ""
            cells[j].width = widths[j]
            p = cells[j].paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if is_head:
                shade(cells[j], NAVY)
                add_runs(p, txt.replace("**", ""), size=8.5, color="FFFFFF")
                for r in p.runs:
                    r.bold = True
            else:
                if is_kv and j == 0:
                    shade(cells[j], BG_ALT)
                elif not is_kv and i % 2 == 0:
                    shade(cells[j], BG)
                add_runs(p, txt, size=9)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def setup_document(title: str, landscape: bool = False) -> DocumentObject:
    """Create an empty document with brand styles, header and footer.

    Args:
        title: Document title shown in the page header.
        landscape: Set the pages in landscape orientation (for very wide tables).

    Returns:
        The prepared document.
    """
    doc = Document()

    styles = doc.styles
    style_text(styles["Normal"], FONT_TEXT, 10.5, TEXT)
    styles["Normal"].paragraph_format.line_spacing = 1.15
    style_text(styles["Heading 1"], FONT_DISPLAY, 20, NAVY, bold=True)
    style_text(styles["Heading 2"], FONT_DISPLAY, 13.5, NAVY, bold=True)
    style_text(styles["Heading 3"], FONT_DISPLAY, 11.5, NAVY, bold=True)
    styles["Heading 1"].paragraph_format.space_before = Pt(0)
    styles["Heading 1"].paragraph_format.space_after = Pt(10)
    styles["Heading 2"].paragraph_format.space_before = Pt(16)
    styles["Heading 2"].paragraph_format.space_after = Pt(6)
    styles["Heading 3"].paragraph_format.space_before = Pt(12)
    styles["Heading 3"].paragraph_format.space_after = Pt(4)
    # H2 mit Linie in Signalblau, wie im PDF-Layout
    paragraph_border(styles["Heading 2"].element.get_or_add_pPr(), "bottom", ACCENT, 10, 3)
    for name in ("Header", "Footer"):
        style_text(styles[name], FONT_TEXT, 7.5, MUTED)
        # Die Word-Vorlage hat Mittel- und Rechts-Tab bei 16,5 cm; nur unser Rechts-Tab soll gelten
        styles[name].paragraph_format.tab_stops.clear_all()
    # Auch Absatzmarken, Aufzählungszeichen und Tabellenvorlagen sollen nicht auf Calibri zurückfallen
    default_rpr = doc.styles.element.find(qn("w:docDefaults")).find(qn("w:rPrDefault")).find(qn("w:rPr"))
    set_rfonts(default_rpr, FONT_TEXT)
    # Deutsch statt Englisch: richtige Rechtschreibprüfung beim Ausfüllen und deutsche Silbentrennung
    default_rpr.find(qn("w:lang")).set(qn("w:val"), "de-DE")
    # Silbentrennung, damit schmale Tabellenspalten nicht mitten im Wort umbrechen
    doc.settings.element.find(qn("w:defaultTabStop")).addnext(OxmlElement("w:autoHyphenation"))
    # Theme-Schriften (Calibri/Cambria) ersetzen: gilt für alle Word-Formatvorlagen, die Nutzer später wählen
    theme = doc.part.part_related_by(RT.THEME)
    theme._blob = re.sub(
        rb'(<a:majorFont>\s*<a:latin typeface=")[^"]*',
        rb"\g<1>" + FONT_DISPLAY.encode(),
        re.sub(rb'(<a:minorFont>\s*<a:latin typeface=")[^"]*', rb"\g<1>" + FONT_TEXT.encode(), theme.blob),
    )

    section = doc.sections[0]
    if landscape:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width, section.page_height = section.page_height, section.page_width
    section.left_margin = section.right_margin = Cm(2)
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(1.8)
    section.header_distance = Cm(0.9)
    section.footer_distance = Cm(0.8)
    text_width = section.page_width - section.left_margin - section.right_margin

    hp = section.header.paragraphs[0]
    hp.paragraph_format.tab_stops.add_tab_stop(text_width, WD_TAB_ALIGNMENT.RIGHT)
    hp.add_run().add_picture(str(LOGO), width=Cm(2.8))
    hp.add_run("\t" + title)
    paragraph_border(hp._p.get_or_add_pPr(), "bottom", ACCENT, 8, 3)

    fp = section.footer.paragraphs[0]
    fp.paragraph_format.tab_stops.add_tab_stop(text_width, WD_TAB_ALIGNMENT.RIGHT)
    paragraph_border(fp._p.get_or_add_pPr(), "top", BORDER_COLOR, 4, 4)
    fp.add_run(FOOTER + "\tSeite ")
    add_field(fp, "PAGE", 7.5, MUTED)
    fp.add_run(" von ")
    add_field(fp, "NUMPAGES", 7.5, MUTED)
    return doc


def md_to_docx(md_path: Path, out_path: Path, fonts: dict[str, dict[str, bytes]]) -> None:
    """Convert one Markdown template into a branded DOCX file.

    Args:
        md_path: Source Markdown file.
        out_path: Target DOCX path.
        fonts: Fonts to embed, see load_embedded_fonts().
    """
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), md_path.stem)
    landscape = any(ln.strip().startswith("|") and ln.count("|") > LANDSCAPE_COLUMNS for ln in lines)
    doc = setup_document(title.replace("**", ""), landscape)

    i = 0
    para_buf: list[str] = []

    def flush_para() -> None:
        """Write the collected paragraph lines as one paragraph."""
        nonlocal para_buf
        if para_buf:
            p = doc.add_paragraph()
            add_runs(p, " ".join(s.strip() for s in para_buf))
            p.paragraph_format.space_after = Pt(6)
            para_buf = []

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush_para()
            i += 1
            continue
        if s.startswith("|"):
            flush_para()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            add_table(doc, parse_table(tbl))
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush_para()
            level = min(len(m.group(1)), 3)
            h = doc.add_heading("", level=level)
            add_runs(h, m.group(2).replace("**", ""))
            i += 1
            continue
        if re.fullmatch(r"-{3,}|\*{3,}", s):
            flush_para()
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(8)
            paragraph_border(p._p.get_or_add_pPr(), "bottom", BORDER_COLOR, 4)
            i += 1
            continue
        if s.startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.4)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(8)
            add_runs(p, " ".join(q for q in quote if q))
            # Hinweiskasten: Akzent-Tönung mit Linie in Signalblau links
            ppr = p._p.get_or_add_pPr()
            paragraph_border(ppr, "left", ACCENT, 18, 8)
            paragraph_shade(ppr, TINT)
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if m:
            flush_para()
            indent = len(m.group(1)) // 2
            numbered = m.group(2)[0].isdigit()
            p = doc.add_paragraph(style="List Number" if numbered else "List Bullet")
            p.paragraph_format.left_indent = Cm(0.63 * (indent + 1))
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, m.group(3))
            i += 1
            # Fortsetzungszeilen der Aufzählung
            while (
                i < len(lines)
                and lines[i].startswith("  ")
                and lines[i].strip()
                and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i])
                and not lines[i].strip().startswith("|")
            ):
                add_runs(p, " " + lines[i].strip())
                i += 1
            continue
        para_buf.append(s)
        i += 1
    flush_para()
    embed_fonts(doc, fonts)
    doc.save(out_path)


# ─────────────────────────── XLSX ───────────────────────────

HEAD_FILL = PatternFill("solid", fgColor=NAVY)
HEAD_FONT = Font(name=FONT_TEXT, bold=True, color="FFFFFF", size=10)
KEY_FILL = PatternFill("solid", fgColor=BG_ALT)
THIN = Side(style="thin", color=BORDER_COLOR)
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def brand_fonts(ws: Worksheet) -> None:
    """Switch every cell of a sheet to Red Hat Text, keeping size, color and style.

    Args:
        ws: The worksheet.
    """
    for row in ws.iter_rows():
        for cell in row:
            f = cell.font
            cell.font = Font(name=FONT_TEXT, size=f.sz or 10, bold=f.b, italic=f.i, color=f.color)


def style_header(ws: Worksheet, ncols: int, row: int = 1) -> None:
    """Style a header row in navy, freeze it and enable the auto filter.

    Args:
        ws: The worksheet.
        ncols: Number of columns.
        row: Row number of the header.
    """
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEAD_FILL
        cell.font = HEAD_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BORDER
    ws.row_dimensions[row].height = 32
    ws.freeze_panes = ws.cell(row=row + 1, column=1)
    ws.auto_filter.ref = f"A{row}:{get_column_letter(ncols)}{row + 200}"


def add_dropdown(ws: Worksheet, col_letter: str, options: list[str], first_row: int, last_row: int = 300) -> None:
    """Restrict a column range to a list of allowed values.

    Args:
        ws: The worksheet.
        col_letter: Column, e.g. "G".
        options: Allowed values.
        first_row: First row of the range.
        last_row: Last row of the range.
    """
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
    dv.error = "Bitte Wert aus der Liste wählen"
    dv.errorTitle = "Ungültig"
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}{first_row}:{col_letter}{last_row}")


def build_inventar(md_path: Path, out_path: Path) -> None:
    """Build the AI inventory workbook from the table in template 01.

    Args:
        md_path: Markdown source of template 01.
        out_path: Target XLSX path.
    """
    text = md_path.read_text(encoding="utf-8")
    # Inventartabelle = erste Tabelle nach Überschrift "## Inventar"
    block = text.split("## Inventar", 1)[1].split("## Legende", 1)[0]
    rows = parse_table([ln for ln in block.splitlines() if ln.strip().startswith("|")])
    header, body = rows[0], rows[1:]
    wb = Workbook()
    ws = wb.active
    ws.title = "KI-Inventar"
    ws.append([h.replace("**", "") for h in header])
    for r in body:
        ws.append([c.replace("*", "") for c in r])
    for _ in range(25):
        ws.append([""] * len(header))
    widths = [5, 24, 18, 26, 20, 26, 12, 14, 22, 22, 18, 16, 14, 30]
    for idx, w in enumerate(widths[: len(header)], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(header)):
        for cell in row:
            cell.alignment = WRAP
            cell.border = BORDER
    # Nummerierung
    for n, row in enumerate(range(2, ws.max_row + 1), start=1):
        ws.cell(row=row, column=1, value=n)
    brand_fonts(ws)
    style_header(ws, len(header))
    # Beispielzeilen kursiv/gedämpft
    for row in range(2, 2 + len(body)):
        for cell in ws[row]:
            cell.font = Font(name=FONT_TEXT, italic=True, color=MUTED, size=10)
    # Dropdowns
    add_dropdown(ws, "G", ["ja", "nein", "unklar"], 2)
    add_dropdown(ws, "H", ["Betreiber", "Anbieter", "beides", "unklar"], 2)
    add_dropdown(
        ws,
        "I",
        [
            "minimal",
            "Transparenz (Art. 50)",
            "hoch (Anhang III) – ab 02.12.2027",
            "hoch (Anhang I) – ab 02.08.2028",
            "verboten",
            "unklar",
        ],
        2,
    )
    add_dropdown(
        ws,
        "J",
        [
            "keiner",
            "Chatbot-Hinweis",
            "Deepfake-Label",
            "KI-Text öffentl. Interesse",
            "Emotionserkennung/Biometrie-Info",
        ],
        2,
    )
    add_dropdown(ws, "K", ["AVV ja", "AVV fehlt", "nicht erforderlich", "prüfen"], 2)
    add_dropdown(ws, "M", ["ja", "nein", "geplant"], 2)

    lg = wb.create_sheet("Legende")
    legend = [
        ("Feld", "Bedeutung / Hinweise"),
        (
            "Unsere Rolle",
            "Betreiber (deployer): wir nutzen ein fremdes System in eigener Verantwortung. Anbieter (provider): wir "
            "haben es entwickelt/entwickeln lassen und bringen es unter eigenem Namen in Verkehr – auch eigene App mit "
            "GPT-Schnittstelle oder White Label (Art. 3 Nr. 3/4, Art. 25 KI-VO).",
        ),
        (
            "Risikostufe",
            "verboten (Art. 5) · hoch (Anhang I ab 02.08.2028 / Anhang III ab 02.12.2027) · Transparenz (Art. 50, seit "
            "02.08.2026) · minimal (nur Art. 4 + DSGVO). Einstufung mit Vorlage 02 und BNetzA KI-Compliance-Kompass.",
        ),
        (
            "Art.-50-Fall",
            "Chatbot-Hinweis (Interaktion) · Deepfake-Label (täuschend echte Bilder/Videos/Audios) · KI-Text zu Themen "
            "öffentlichen Interesses ohne redaktionelle Prüfung · Information bei Emotionserkennung/biometrischer "
            "Kategorisierung. Normale Werbe-/Produkttexte: kein Fall.",
        ),
        (
            "AVV / Vertrag",
            "Auftragsverarbeitungsvertrag nach Art. 28 DSGVO, Drittlandtransfer (DPF/SCC), Trainings-Opt-out, "
            "Enterprise-/Team-Tarif.",
        ),
        ("Schulung erfolgt", "Nutzergruppe hat Basisschulung (Art. 4) erhalten; Nachweis in Vorlage 04."),
        (
            "Pflege",
            "Bei jedem neuen Tool ergänzen, mindestens halbjährlich prüfen; mit Verarbeitungsverzeichnis (Art. 30 "
            "DSGVO) abgleichen.",
        ),
        (
            "Rechtsstand",
            f"{STAND} – KI-VO 2024/1689 i. d. F. Digital Omnibus VO (EU) 2026/1744; KI-MIG. Kein Rechtsrat. "
            "CC BY 4.0, PINGEL AI Solutions.",
        ),
    ]
    for r in legend:
        lg.append(list(r))
    lg.column_dimensions["A"].width = 20
    lg.column_dimensions["B"].width = 110
    for row in lg.iter_rows(min_row=2, max_col=2):
        for cell in row:
            cell.alignment = WRAP
            cell.border = BORDER
    brand_fonts(lg)
    for row in range(2, lg.max_row + 1):
        lg.cell(row=row, column=1).fill = KEY_FILL
        lg.cell(row=row, column=1).font = Font(name=FONT_TEXT, bold=True, color=NAVY, size=10)
    style_header(lg, 2)
    wb.save(out_path)


def build_teilnehmerliste(out_path: Path) -> None:
    """Build the attendance list and training plan workbook for template 04.

    Args:
        out_path: Target XLSX path.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Teilnehmerliste"
    ws["A1"] = "Nachweis KI-Kompetenz-Maßnahme (Art. 4 KI-VO) – Teilnehmerliste"
    meta = [
        "Organisation",
        "Maßnahme / Titel",
        "Datum",
        "Format & Dauer",
        "Referent/in bzw. Quelle",
        "Stufe (1 Grundlagen / 2 Rolle & Recht / 3 fachspezifisch)",
        "Inhalte (Stichworte)",
        "Unterlagen abgelegt unter",
    ]
    for idx, key in enumerate(meta, start=3):
        ws.cell(row=idx, column=1, value=key)
        ws.cell(row=idx, column=1).fill = KEY_FILL
        for c in (1, 2):
            ws.cell(row=idx, column=c).border = BORDER
        ws.merge_cells(start_row=idx, start_column=2, end_row=idx, end_column=5)
    head_row = 12
    headers = ["Nr.", "Name", "Abteilung / Rolle", "Teilnahme (ja/online/nachgeholt)", "Unterschrift"]
    for c, h in enumerate(headers, start=1):
        ws.cell(row=head_row, column=c, value=h)
    for n in range(1, 31):
        r = head_row + n
        ws.cell(row=r, column=1, value=n)
        for c in range(1, len(headers) + 1):
            ws.cell(row=r, column=c).border = BORDER
            ws.cell(row=r, column=c).alignment = WRAP
        ws.row_dimensions[r].height = 22
    add_dropdown(ws, "D", ["ja", "online", "nachgeholt am …", "entschuldigt"], head_row + 1, head_row + 30)
    for col, w in zip("ABCDE", (6, 30, 26, 26, 30), strict=True):
        ws.column_dimensions[col].width = w
    ws.cell(
        row=head_row + 33,
        column=1,
        value="Bestätigung der Durchführung – Datum, Name, Unterschrift Verantwortliche/r:",
    )
    ws.cell(row=head_row + 36, column=1, value=FOOTER)
    brand_fonts(ws)
    ws["A1"].font = Font(name=FONT_DISPLAY, bold=True, size=14, color=NAVY)
    for idx in range(3, 3 + len(meta)):
        ws.cell(row=idx, column=1).font = Font(name=FONT_TEXT, bold=True, color=NAVY, size=10)
    ws.cell(row=head_row + 33, column=1).font = Font(name=FONT_TEXT, bold=True, color=NAVY, size=10)
    ws.cell(row=head_row + 36, column=1).font = Font(name=FONT_TEXT, size=8, color=MUTED)
    style_header(ws, len(headers), row=head_row)
    ws.freeze_panes = None

    plan = wb.create_sheet("Maßnahmenplan")
    plan.append(
        ["Stufe", "Zielgruppe", "Inhalte", "Format", "Dauer", "Turnus", "Anbieter / Material", "Termin", "Erledigt"]
    )
    rows = [
        (
            "1 Grundlagen",
            "alle Nutzenden",
            "Was ist KI, Sprachmodelle, Halluzination/Bias, Chancen/Risiken, Richtlinie, Datenschutz-Grundregeln",
            "Workshop / Online-Kurs",
            "60–90 Min",
            "Einstieg, dann jährlich",
            "dieser Workshop; KI-Campus; appliedAI; Elements of AI",
            "",
            "",
        ),
        (
            "2 Rolle & Recht",
            "Führung, Marketing, HR, Service, IT",
            "KI-VO-Grundzüge, Rollen, Risikostufen, Art. 50, Art. 26, Prüfroutinen, Meldewege",
            "Workshop / Leitfaden",
            "90–120 Min",
            "jährlich, bei Rechtsänderung",
            "Workshop „EU AI Act für kleine Organisationen“; BNetzA-Kompass; eRecht24",
            "",
            "",
        ),
        (
            "3 Fachspezifisch",
            "HR (Hochrisiko), Produkt/IT (Anbieter), Datenschutz",
            "Betriebsanleitung, menschliche Aufsicht, Diskriminierung, Logging, Vorfallmeldung; Anbieter: Doku, "
            "Kennzeichnung",
            "Anbieter-Schulung, Beratung",
            "nach Bedarf",
            "vor Inbetriebnahme, dann jährlich",
            "Tool-Anbieter; Mittelstand-Digital; Fachanwalt",
            "",
            "",
        ),
        (
            "Onboarding",
            "neue Beschäftigte",
            "Stufe 1 komprimiert + Richtlinie unterschreiben",
            "Selbstlernpaket + Gespräch",
            "45 Min",
            "innerhalb 4 Wochen",
            "intern",
            "",
            "",
        ),
    ]
    for r in rows:
        plan.append(list(r))
    for _ in range(6):
        plan.append([""] * 9)
    add_dropdown(plan, "I", ["ja", "nein", "teilweise"], 2, 40)
    for col, w in zip("ABCDEFGHI", (16, 26, 48, 22, 12, 24, 40, 12, 10), strict=True):
        plan.column_dimensions[col].width = w
    for row in plan.iter_rows(min_row=2, max_row=plan.max_row, max_col=9):
        for cell in row:
            cell.alignment = WRAP
            cell.border = BORDER
    brand_fonts(plan)
    style_header(plan, 9)
    wb.save(out_path)


# ─────────────────────────── main ───────────────────────────


def main() -> None:
    """Build all DOCX and XLSX files."""
    OUT_DOCX.mkdir(exist_ok=True)
    OUT_XLSX.mkdir(exist_ok=True)
    fonts = load_embedded_fonts()
    md_files = sorted(SRC.glob("[0-9][0-9]_*.md"))
    for md in md_files:
        out = OUT_DOCX / (md.stem + ".docx")
        md_to_docx(md, out, fonts)
        print("DOCX ", out.relative_to(ROOT))
    build_inventar(SRC / "01_ki_inventar.md", OUT_XLSX / "01_ki_inventar.xlsx")
    print("XLSX ", "vorlagen/xlsx/01_ki_inventar.xlsx")
    build_teilnehmerliste(OUT_XLSX / "04_teilnehmerliste.xlsx")
    print("XLSX ", "vorlagen/xlsx/04_teilnehmerliste.xlsx")
    print(f"\n{len(md_files)} DOCX + 2 XLSX erzeugt.")


if __name__ == "__main__":
    main()
