# Vorlagen – Hands-on-Material zum EU AI Act für kleine Organisationen

**Rechtsstand:** 9. November 2026 (KI-VO 2024/1689 i. d. F. Digital Omnibus VO (EU) 2026/1744; KI-MIG vom 22.07.2026)
**Lizenz:** CC BY 4.0 · **Kein Rechtsrat** – bei Hochrisiko-Systemen oder Anbieterrolle juristisch prüfen lassen.

Jede Vorlage gibt es als **Markdown** (lesbar, versionierbar, hier im Ordner) und als **DOCX** bzw. **XLSX**
zum direkten Ausfüllen (`docx/`, `xlsx/`). Die Office-Dateien werden aus den Markdown-Definitionen erzeugt:

```powershell
uv run --with python-docx --with openpyxl --with fonttools --with brotli python tools/build_vorlagen.py
```

## Übersicht und Einsatz im Workshop

| Nr. | Vorlage | Wofür | Rechtsgrundlage | Workshop-Block | Format |
|---|---|---|---|---|---|
| 01 | [KI-Inventar](01_ki_inventar.md) | Alle KI-Tools erfassen, Rolle/Risiko/AVV je Tool | Grundlage für Art. 4, 26, 50; Art. 30 DSGVO | Hands-on 1 | MD + **XLSX** |
| 02 | [Rollen- und Risiko-Check](02_rollen_risiko_check.md) | Pro System: KI-System? Rolle? Verbot? Hochrisiko? Transparenz? | Art. 3, 5, 6, 25, 50 | Hands-on 2 | MD + DOCX |
| 03 | [KI-Nutzungsrichtlinie](03_ki_nutzungsrichtlinie.md) | Regeln für Beschäftigte: erlaubte Tools, Daten, Prüfung, Kennzeichnung | Art. 4, 5, 50; DSGVO | Hands-on 3 | MD + DOCX |
| 04 | [Schulungskonzept und Nachweis](04_schulungskonzept_nachweis.md) | Bedarf, Maßnahmenplan, Teilnahmenachweis | Art. 4 | Hands-on 4 | MD + DOCX + **XLSX** |
| 05 | [Transparenz-Textbausteine](05_transparenz_textbausteine.md) | Chatbot-Hinweis, Deepfake-Label, KI-Text-Hinweis, Datenschutz-Passus | Art. 50 | Hands-on 5 | MD + DOCX |
| 06 | [Fragebogen an KI-Anbieter](06_fragebogen_ki_anbieter.md) | 12 Fragen vor Kauf/Verlängerung; interne Auswertung | Art. 6, 13, 26, 50; Art. 28 DSGVO | Hands-on 6 | MD + DOCX |
| 07 | [Information Beschäftigte und Betriebsrat](07_information_beschaeftigte_betriebsrat.md) | Musterschreiben vor Inbetriebnahme eines Hochrisiko-Systems | Art. 26 Abs. 7, 11; Art. 86; § 87 BetrVG | Modul 3 (HR) | MD + DOCX |
| 08 | [Vorfall- und Risiko-Protokoll](08_vorfall_protokoll.md) | Fehler, Beschwerden, schwerwiegende Vorfälle erfassen und melden | Art. 26 Abs. 5; Art. 73 | Modul 3 | MD + DOCX |
| 09 | [Fahrplan und Checkliste](09_fahrplan_checkliste.md) | Alle Maßnahmen nach Rolle und Zeitraum bis 12/2027 | alle | Abschluss | MD + DOCX |

## Empfohlene Reihenfolge nach dem Workshop

1. **Woche 1:** Inventar (01) → Rollen-/Risiko-Check (02) für jedes Tool → Verbots-Check abhaken.
2. **Woche 2–4:** Richtlinie (03) anpassen, kommunizieren, Kenntnisnahme sammeln → Schulungsnachweis (04) für den Workshop ablegen.
3. **Woche 2–4:** Transparenz-Bausteine (05) für Chatbot/Deepfakes/öffentliche Texte einsetzen – diese Pflichten gelten bereits.
4. **In den nächsten drei Monaten:** Anbieter-Fragebogen (06) an alle Tool-Anbieter, besonders HR/Bildung/Scoring.
5. **2027:** Hochrisiko-Vorbereitung mit 07 und 08; Fahrplan (09) vierteljährlich abhaken.

## Grundsätze der Vorlagen

- **Nur das, was das Gesetz verlangt** – plus wenige, klar als „Empfehlung" markierte Praxisschritte.
- **Platzhalter in [eckigen Klammern]**, kursive Ausfüllhinweise, Ankreuzfelder ☐.
- Formulierungen orientieren sich an Bundesnetzagentur, EU-Kommission und e-recht24.de; alle Rechtsgrundlagen sind genannt.
- Weiterführende Muster: GDD-Musterrichtlinie KI (05/2025), Bitkom-Umsetzungsleitfaden 2.0 und „KI und Mitbestimmung" (02/2026),
  Mittelstand-Digital Zentrum Berlin „KI-Richtlinie in 7 Schritten" – siehe `../src.txt`.
