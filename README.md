# EU AI Act – Workshop für kleine Organisationen

Workshop-Material zur EU-KI-Verordnung (Verordnung (EU) 2024/1689 in der Fassung des „Digital Omnibus"
VO (EU) 2026/1744) für kleine und mittlere Unternehmen, Software-KMU, Vereine und Kommunen – ohne eigene
Rechtsabteilung. Mit Hands-on-Vorlagen, damit die Pflichten nicht nur verstanden, sondern erledigt werden.

**Rechtsstand:** 9. September 2026
**Format:** Halbtages-Workshop (ca. 4 Stunden) mit HTML-Präsentation (47 Folien) und 9 Vorlagen
**Autor:** PINGEL AI Solutions · Lizenz CC BY 4.0

---

## Inhalt des Repositorys

| Datei / Ordner | Inhalt |
|---|---|
| [`praesentation.html`](praesentation.html) | Interaktive Präsentation, 47 Folien (inkl. Einsteiger-Grundlagen, Glossar, Bewertungsmethode) – im Browser öffnen, keine Abhängigkeiten |
| [`workshop_rezept.md`](workshop_rezept.md) | Ablauf, Module, Lernziele, Übungen, Zielgruppen-Varianten, FAQ, Handout |
| [`sprechtext.md`](sprechtext.md) | Sprechtext und Moderationsnotizen je Folie, Antworten auf schwierige Fragen |
| [`glossar.md`](glossar.md) | Glossar mit 35 Begriffen für Einsteiger (AI Act, Omnibus, KI-MIG, Anbieter/Betreiber, Anhang I/III, FRIA, Praxiskodex …), als Handout nutzbar |
| [`eu_ai_act_recherche.md`](eu_ai_act_recherche.md) | Fachliche Referenz: Rechtsstand 09/2026, Omnibus, KI-MIG, alle Artikel mit Fundstellen, „Was das Gesetz NICHT fordert" |
| [`vorlagen/`](vorlagen/README.md) | 9 Vorlagen als Markdown + generierte DOCX/XLSX (Inventar, Risiko-Check, Richtlinie, Schulungsnachweis, Transparenz-Texte, Anbieter-Fragebogen, Betriebsrat-Info, Vorfall-Protokoll, Fahrplan) |
| [`tools/build_vorlagen.py`](tools/build_vorlagen.py) | Erzeugt DOCX/XLSX aus den Markdown-Vorlagen (python-docx, openpyxl) |
| [`tools/check_links.py`](tools/check_links.py) | Prüft alle URLs in Quellen, Präsentation und Vorlagen |
| [`src.txt`](src.txt) | Kategorisiertes Quellenverzeichnis (~100 URLs mit Stand-Angabe) |
| [`AENDERUNGEN.md`](AENDERUNGEN.md) | Änderungsprotokoll: Rechtsänderungen, korrigierte Fehler, offene Punkte |
| `Logo.svg`, `Original.svg` | Grafik-Assets |
| `fonts/` | Schriften Red Hat Display/Text (lokal eingebunden, SIL Open Font License – siehe `fonts/OFL-RedHat.txt`) |

---

## Präsentation starten

```powershell
Start-Process praesentation.html
```

Navigation: Pfeiltasten, Klick, Wischen · `Home`/`End` · `F` = Vollbild · Deep-Link `praesentation.html#f22` springt zu Folie 22.

## Vorlagen regenerieren

```powershell
pip install python-docx openpyxl
python tools/build_vorlagen.py       # vorlagen/docx/*.docx, vorlagen/xlsx/*.xlsx
python tools/check_links.py          # Link-Report
```

Die Markdown-Dateien in `vorlagen/` sind die einzige Quelle; die Office-Dateien sind generiert und werden mit committet.

---

## Zielgruppen & Lernziele

Nach dem Workshop können Teilnehmende:

1. für jedes KI-System **Rolle** (Anbieter/Betreiber) und **Risikostufe** bestimmen,
2. die **drei heute geltenden Pflichten** erfüllen – Verbote (Art. 5), KI-Kompetenz (Art. 4), Transparenz (Art. 50) – mit den Vorlagen,
3. die **Hochrisiko-Pflichten ab 2. Dezember 2027** (Art. 26, ggf. Art. 27) planen,
4. benennen, **was das Gesetz nicht fordert** (kein KI-Beauftragter, keine Zertifikate, keine Kennzeichnung aller KI-Texte, keine FRIA für normale KMU, keine Registrierung als Betreiber),
5. kostenlose Hilfsangebote nutzen (Bundesnetzagentur KI-Service-Desk, eRecht24, Mittelstand-Digital, KI-Campus).

---

## Rechtsstand in Kürze (09/2026)

| Was | Seit / ab |
|---|---|
| Verbotene Praktiken (9), KI-Kompetenz | 2. Feb 2025 |
| GPAI-Pflichten, Bußgeldvorschriften | 2. Aug 2025 |
| Digital Omnibus (VO 2026/1744), KI-MIG | 27. / 29. Juli 2026 |
| Transparenzpflichten Art. 50, Aufsicht durch Bundesnetzagentur | 2. Aug 2026 |
| Hochrisiko Anhang III (HR, Bildung, Kredit …) | **2. Dez 2027** |
| Hochrisiko Anhang I (Produkte) | 2. Aug 2028 |

---

## Quellen

Bevorzugt deutschsprachige Primär- und Praxisquellen: Verordnungstext (EUR-Lex, ai-act-law.eu), Bundesnetzagentur
KI-Service-Desk, e-recht24.de, EU-Kommission (Leitlinien, Praxiskodizes), gesetze-im-internet.de (KI-MIG),
Datenschutzkonferenz, Bitkom, GDD. Vollständige Liste: [`src.txt`](src.txt).

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0) – siehe [LICENSE](LICENSE).

## Hinweis

Dieses Material ersetzt **keine** individuelle Rechtsberatung. Es dient der Erstorientierung und Umsetzung
der Grundpflichten. Bei Hochrisiko-Systemen oder Anbieterrolle ist fachkundige juristische Beratung einzuholen.
