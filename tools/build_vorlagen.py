#!/usr/bin/env python3
"""Erzeugt aus den Markdown-Vorlagen in vorlagen/ ausfüllbare DOCX- und XLSX-Dateien.

Aufruf:  python tools/build_vorlagen.py
Ausgabe: vorlagen/docx/NN_*.docx (alle Vorlagen 01–09) und
         vorlagen/xlsx/01_ki_inventar.xlsx, vorlagen/xlsx/04_teilnehmerliste.xlsx

Die Markdown-Dateien sind die einzige Quelle (Single Source of Truth). Der Konverter versteht
Überschriften, Absätze, Tabellen, Aufzählungen, Zitate, Trennlinien sowie **fett**/*kursiv*/`code`.
Abhängigkeiten: python-docx, openpyxl.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "vorlagen"
OUT_DOCX = SRC / "docx"
OUT_XLSX = SRC / "xlsx"

NAVY = RGBColor(0x18, 0x21, 0x45)
GOLD = RGBColor(0xC4, 0x90, 0x2A)
GREY = RGBColor(0x5A, 0x6A, 0x8A)
FOOTER = "EU AI Act für kleine Organisationen · PINGEL AI Solutions · Stand 09/2026 · CC BY 4.0 · Kein Rechtsrat"

INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


# ─────────────────────────── Markdown → DOCX ───────────────────────────

def add_runs(paragraph, text: str, size: float | None = None, color: RGBColor | None = None) -> None:
    """Fügt Text mit **fett**, *kursiv*, `code` als Runs ein."""
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2]); run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1]); run.italic = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1]); run.font.name = "Consolas"
        else:
            run = paragraph.add_run(part)
        if size:
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = color


def shade(cell, hex_fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue  # Trennzeile
        rows.append(cells)
    return rows


def add_table(doc: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header = rows[0]
    is_kv = ncols == 2 and header[0] == ""  # Kopf-Metatabelle „| | |“
    for i, row in enumerate(rows):
        cells = table.add_row().cells
        for j in range(ncols):
            txt = row[j] if j < len(row) else ""
            p = cells[j].paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            if i == 0 and not is_kv:
                shade(cells[j], "182145")
                add_runs(p, txt.replace("**", ""), size=8.5, color=RGBColor(0xFF, 0xFF, 0xFF))
                for r in p.runs:
                    r.bold = True
            else:
                if is_kv and j == 0:
                    shade(cells[j], "F0F4FB")
                add_runs(p, txt, size=9)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def md_to_docx(md_path: Path, out_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    doc = Document()
    for section in doc.sections:
        section.left_margin = section.right_margin = Cm(2)
        section.top_margin = section.bottom_margin = Cm(1.8)
        fp = section.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_runs(fp, FOOTER, size=7.5, color=GREY)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"; style.font.size = Pt(10.5)
    for lvl, size in ((1, 18), (2, 13.5), (3, 11.5)):
        hs = doc.styles[f"Heading {lvl}"]
        hs.font.name = "Calibri"; hs.font.size = Pt(size); hs.font.bold = True
        hs.font.color.rgb = NAVY if lvl < 3 else GOLD

    i = 0
    para_buf: list[str] = []

    def flush_para():
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
            flush_para(); i += 1; continue
        if s.startswith("|"):
            flush_para()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i]); i += 1
            add_table(doc, parse_table(tbl)); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush_para()
            level = min(len(m.group(1)), 3)
            h = doc.add_heading("", level=level)
            add_runs(h, m.group(2).replace("**", ""))
            i += 1; continue
        if re.fullmatch(r"-{3,}|\*{3,}", s):
            flush_para()
            p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
            r = p.add_run("─" * 60); r.font.color.rgb = RGBColor(0xDD, 0xE3, 0xF0); r.font.size = Pt(6)
            i += 1; continue
        if s.startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip()); i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            p.paragraph_format.space_after = Pt(6)
            add_runs(p, " ".join(q for q in quote if q), size=10.5)
            shade_p = OxmlElement("w:shd"); shade_p.set(qn("w:val"), "clear"); shade_p.set(qn("w:fill"), "F7F1E3")
            p._p.get_or_add_pPr().append(shade_p)
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
            while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) and not lines[i].strip().startswith("|"):
                add_runs(p, " " + lines[i].strip()); i += 1
            continue
        para_buf.append(s); i += 1
    flush_para()
    doc.save(out_path)


# ─────────────────────────── XLSX ───────────────────────────

HEAD_FILL = PatternFill("solid", fgColor="182145")
HEAD_FONT = Font(bold=True, color="FFFFFF", size=10)
THIN = Side(style="thin", color="DDE3F0")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def style_header(ws, ncols: int, row: int = 1) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEAD_FILL; cell.font = HEAD_FONT; cell.alignment = Alignment(wrap_text=True, vertical="center"); cell.border = BORDER
    ws.row_dimensions[row].height = 32
    ws.freeze_panes = ws.cell(row=row + 1, column=1)
    ws.auto_filter.ref = f"A{row}:{get_column_letter(ncols)}{row + 200}"


def add_dropdown(ws, col_letter: str, options: list[str], first_row: int, last_row: int = 300) -> None:
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
    dv.error = "Bitte Wert aus der Liste wählen"; dv.errorTitle = "Ungültig"
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}{first_row}:{col_letter}{last_row}")


def build_inventar(md_path: Path, out_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    # Inventartabelle = erste Tabelle nach Überschrift "## Inventar"
    block = text.split("## Inventar", 1)[1].split("## Legende", 1)[0]
    rows = parse_table([ln for ln in block.splitlines() if ln.strip().startswith("|")])
    header, body = rows[0], rows[1:]
    wb = Workbook()
    ws = wb.active; ws.title = "KI-Inventar"
    ws.append([h.replace("**", "") for h in header])
    for r in body:
        ws.append([c.replace("*", "").replace("**", "") for c in r])
    for _ in range(25):
        ws.append([""] * len(header))
    style_header(ws, len(header))
    widths = [5, 24, 18, 26, 20, 26, 12, 14, 22, 22, 18, 16, 14, 30]
    for idx, w in enumerate(widths[: len(header)], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(header)):
        for cell in row:
            cell.alignment = WRAP; cell.border = BORDER
    # Nummerierung
    for n, row in enumerate(range(2, ws.max_row + 1), start=1):
        ws.cell(row=row, column=1, value=n)
    # Beispielzeilen kursiv/grau
    for row in range(2, 2 + len(body)):
        for cell in ws[row]:
            cell.font = Font(italic=True, color="5A6A8A", size=10)
    # Dropdowns
    add_dropdown(ws, "G", ["ja", "nein", "unklar"], 2)
    add_dropdown(ws, "H", ["Betreiber", "Anbieter", "beides", "unklar"], 2)
    add_dropdown(ws, "I", ["minimal", "Transparenz (Art. 50)", "hoch (Anhang III) – ab 02.12.2027", "hoch (Anhang I) – ab 02.08.2028", "verboten", "unklar"], 2)
    add_dropdown(ws, "J", ["keiner", "Chatbot-Hinweis", "Deepfake-Label", "KI-Text öffentl. Interesse", "Emotionserkennung/Biometrie-Info"], 2)
    add_dropdown(ws, "K", ["AVV ja", "AVV fehlt", "nicht erforderlich", "prüfen"], 2)
    add_dropdown(ws, "M", ["ja", "nein", "geplant"], 2)

    lg = wb.create_sheet("Legende")
    legend = [
        ("Feld", "Bedeutung / Hinweise"),
        ("Unsere Rolle", "Betreiber (deployer): wir nutzen ein fremdes System in eigener Verantwortung. Anbieter (provider): wir haben es entwickelt/entwickeln lassen und bringen es unter eigenem Namen in Verkehr – auch eigene App mit GPT-Schnittstelle oder White Label (Art. 3 Nr. 3/4, Art. 25 KI-VO)."),
        ("Risikostufe", "verboten (Art. 5) · hoch (Anhang I ab 02.08.2028 / Anhang III ab 02.12.2027) · Transparenz (Art. 50, seit 02.08.2026) · minimal (nur Art. 4 + DSGVO). Einstufung mit Vorlage 02 und BNetzA KI-Compliance-Kompass."),
        ("Art.-50-Fall", "Chatbot-Hinweis (Interaktion) · Deepfake-Label (täuschend echte Bilder/Videos/Audios) · KI-Text zu Themen öffentlichen Interesses ohne redaktionelle Prüfung · Information bei Emotionserkennung/biometrischer Kategorisierung. Normale Werbe-/Produkttexte: kein Fall."),
        ("AVV / Vertrag", "Auftragsverarbeitungsvertrag nach Art. 28 DSGVO, Drittlandtransfer (DPF/SCC), Trainings-Opt-out, Enterprise-/Team-Tarif."),
        ("Schulung erfolgt", "Nutzergruppe hat Basisschulung (Art. 4) erhalten; Nachweis in Vorlage 04."),
        ("Pflege", "Bei jedem neuen Tool ergänzen, mindestens halbjährlich prüfen; mit Verarbeitungsverzeichnis (Art. 30 DSGVO) abgleichen."),
        ("Rechtsstand", "9. September 2026 – KI-VO 2024/1689 i. d. F. Digital Omnibus VO (EU) 2026/1744; KI-MIG. Kein Rechtsrat. CC BY 4.0, PINGEL AI Solutions."),
    ]
    for r in legend:
        lg.append(list(r))
    style_header(lg, 2)
    lg.column_dimensions["A"].width = 20; lg.column_dimensions["B"].width = 110
    for row in lg.iter_rows(min_row=2, max_col=2):
        for cell in row:
            cell.alignment = WRAP; cell.border = BORDER
    wb.save(out_path)


def build_teilnehmerliste(out_path: Path) -> None:
    wb = Workbook()
    ws = wb.active; ws.title = "Teilnehmerliste"
    ws["A1"] = "Nachweis KI-Kompetenz-Maßnahme (Art. 4 KI-VO) – Teilnehmerliste"
    ws["A1"].font = Font(bold=True, size=13, color="182145")
    meta = [("Organisation", ""), ("Maßnahme / Titel", ""), ("Datum", ""), ("Format & Dauer", ""),
            ("Referent/in bzw. Quelle", ""), ("Stufe (1 Grundlagen / 2 Rolle & Recht / 3 fachspezifisch)", ""),
            ("Inhalte (Stichworte)", ""), ("Unterlagen abgelegt unter", "")]
    for idx, (k, v) in enumerate(meta, start=3):
        ws.cell(row=idx, column=1, value=k).font = Font(bold=True)
        ws.cell(row=idx, column=2, value=v)
        ws.cell(row=idx, column=1).fill = PatternFill("solid", fgColor="F0F4FB")
        for c in (1, 2):
            ws.cell(row=idx, column=c).border = BORDER
    ws.merge_cells(start_row=3, start_column=2, end_row=3, end_column=5)
    for r in range(4, 11):
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    head_row = 12
    headers = ["Nr.", "Name", "Abteilung / Rolle", "Teilnahme (ja/online/nachgeholt)", "Unterschrift"]
    for c, h in enumerate(headers, start=1):
        ws.cell(row=head_row, column=c, value=h)
    style_header(ws, len(headers), row=head_row)
    ws.freeze_panes = None
    for n in range(1, 31):
        r = head_row + n
        ws.cell(row=r, column=1, value=n)
        for c in range(1, len(headers) + 1):
            ws.cell(row=r, column=c).border = BORDER; ws.cell(row=r, column=c).alignment = WRAP
        ws.row_dimensions[r].height = 22
    add_dropdown(ws, "D", ["ja", "online", "nachgeholt am …", "entschuldigt"], head_row + 1, head_row + 30)
    for col, w in zip("ABCDE", (6, 30, 26, 26, 30)):
        ws.column_dimensions[col].width = w
    ws.cell(row=head_row + 33, column=1, value="Bestätigung der Durchführung – Datum, Name, Unterschrift Verantwortliche/r:").font = Font(bold=True)
    ws.cell(row=head_row + 36, column=1, value=FOOTER).font = Font(size=8, color="5A6A8A")

    plan = wb.create_sheet("Maßnahmenplan")
    plan.append(["Stufe", "Zielgruppe", "Inhalte", "Format", "Dauer", "Turnus", "Anbieter / Material", "Termin", "Erledigt"])
    rows = [
        ("1 Grundlagen", "alle Nutzenden", "Was ist KI, Sprachmodelle, Halluzination/Bias, Chancen/Risiken, Richtlinie, Datenschutz-Grundregeln", "Workshop / Online-Kurs", "60–90 Min", "Einstieg, dann jährlich", "dieser Workshop; KI-Campus; appliedAI; Elements of AI", "", ""),
        ("2 Rolle & Recht", "Führung, Marketing, HR, Service, IT", "KI-VO-Grundzüge, Rollen, Risikostufen, Art. 50, Art. 26, Prüfroutinen, Meldewege", "Workshop / Leitfaden", "90–120 Min", "jährlich, bei Rechtsänderung", "Workshop „EU AI Act für kleine Organisationen“; BNetzA-Kompass; eRecht24", "", ""),
        ("3 Fachspezifisch", "HR (Hochrisiko), Produkt/IT (Anbieter), Datenschutz", "Betriebsanleitung, menschliche Aufsicht, Diskriminierung, Logging, Vorfallmeldung; Anbieter: Doku, Kennzeichnung", "Anbieter-Schulung, Beratung", "nach Bedarf", "vor Inbetriebnahme, dann jährlich", "Tool-Anbieter; Mittelstand-Digital; Fachanwalt", "", ""),
        ("Onboarding", "neue Beschäftigte", "Stufe 1 komprimiert + Richtlinie unterschreiben", "Selbstlernpaket + Gespräch", "45 Min", "innerhalb 4 Wochen", "intern", "", ""),
    ]
    for r in rows:
        plan.append(list(r))
    for _ in range(6):
        plan.append([""] * 9)
    style_header(plan, 9)
    add_dropdown(plan, "I", ["ja", "nein", "teilweise"], 2, 40)
    for col, w in zip("ABCDEFGHI", (16, 26, 48, 22, 12, 24, 40, 12, 10)):
        plan.column_dimensions[col].width = w
    for row in plan.iter_rows(min_row=2, max_row=plan.max_row, max_col=9):
        for cell in row:
            cell.alignment = WRAP; cell.border = BORDER
    wb.save(out_path)


# ─────────────────────────── main ───────────────────────────

def main() -> None:
    OUT_DOCX.mkdir(exist_ok=True); OUT_XLSX.mkdir(exist_ok=True)
    md_files = sorted(p for p in SRC.glob("[0-9][0-9]_*.md"))
    for md in md_files:
        out = OUT_DOCX / (md.stem + ".docx")
        md_to_docx(md, out)
        print("DOCX ", out.relative_to(ROOT))
    inv = SRC / "01_ki_inventar.md"
    build_inventar(inv, OUT_XLSX / "01_ki_inventar.xlsx"); print("XLSX ", "vorlagen/xlsx/01_ki_inventar.xlsx")
    build_teilnehmerliste(OUT_XLSX / "04_teilnehmerliste.xlsx"); print("XLSX ", "vorlagen/xlsx/04_teilnehmerliste.xlsx")
    print(f"\n{len(md_files)} DOCX + 2 XLSX erzeugt.")


if __name__ == "__main__":
    main()
