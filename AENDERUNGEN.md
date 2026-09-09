# Änderungsprotokoll

## 2026-09-09 (2) – Einsteiger-Teil ergänzt

Rückmeldung: Für Neueinsteiger fehlten Sinn und Zweck des Gesetzes, Begriffserklärungen (z. B. KI-MIG) und eine
nachvollziehbare Methode zur Risikoeinstufung; vieles war vorausgesetzt.

- **Neue Folien (41 → 47):** 4 „Warum gibt es den AI Act?" (Problem, Ziele Art. 1, Grundidee Produktsicherheit,
  was er nicht ist), 6 „Wie das Gesetz funktioniert" (vier Fragen, Aufbau der Verordnung, Lesehilfe), 7 „Begriffe"
  (18 Begriffe inkl. KI-MIG, Omnibus, Anbieter/Betreiber, Anhang I/III, FRIA, Praxiskodex), 21 „Risikostufe bewerten –
  sechs Schritte", 22 „Beispiel Elektro Müller GmbH" (vier Tools durchgerechnet), 23 „Pflichten je Stufe – Gesamtmatrix"
  (Anbieter/Betreiber × vier Stufen × Geltung).
- **Neu `glossar.md`:** 35 Begriffe mit Fundstellen, als Handout.
- **`eu_ai_act_recherche.md`:** neues Kapitel 0 (Einführung, Funktionsweise, Bewertungsmethode mit Beispiel, Pflichtenmatrix).
- **Sprechtext** für alle neuen Folien; **Rezept**: Modul 1 auf 50 min, Modul 2 auf 65 min (Ende 13:50), Kurzvariante
  für erfahrenes Publikum, neuer Abschnitt 2.3; alle Foliennummern in Sprechtext, Rezept und Folien-Querverweisen angepasst.
- Agenda-Folie und README aktualisiert.

## 2026-09-09 – Komplettüberarbeitung auf Rechtsstand 9. September 2026

Vorgängerstand: März 2026 (Initial-Commit). Anlass: Digital Omnibus (VO (EU) 2026/1744, in Kraft 27.07.2026),
deutsches Durchführungsgesetz KI-MIG (in Kraft 29.07.2026), Praxiskodex Kennzeichnung (10.06.2026) sowie
sachliche Fehler im bisherigen Material.

### Eingearbeitete Rechtsänderungen

| Thema | Alt (Material 03/2026) | Neu |
|---|---|---|
| Hochrisiko Anhang III | ab 02.08.2026 | **ab 02.12.2027** |
| Hochrisiko Anhang I | ab 02.08.2027 | **ab 02.08.2028** |
| Art. 4 KI-Kompetenz | „sicherstellen" | „Maßnahmen zur **Förderung**", kein garantiertes Niveau pro Person; Aufsicht seit 02.08.2026 |
| Art. 50 | ab 02.08.2026 | gilt seit 02.08.2026; nur Abs. 2 (maschinenlesbare Kennzeichnung, Anbieter) für Altsysteme bis 02.12.2026 |
| Verbote Art. 5 | 8 | **9** (neu: CSAM/nicht-einvernehmliche Intimbilder) |
| KMU-Erleichterungen | KMU | zusätzlich Small Mid-Caps (< 750 MA, ≤ 150 Mio. € Umsatz) |
| Reallabor-Frist | 02.08.2026 | 02.08.2027 |
| Deutschland | Kabinettsentwurf 11.02.2026 | **KI-MIG** vom 22.07.2026 (BGBl. 2026 I Nr. 223): BNetzA zentral, BaFin, Länder, KoKIVO, Beschwerdestelle, Reallabor, nationale Bußgelder bis 50.000 € |
| Praxiskodex Art. 50 | Entwurf | final 10.06.2026, ~190 Unterzeichner; Kommissions-Leitlinien Art. 50 vom 08.05.2026 |
| Leitlinien Art. 6 | angekündigt | Entwurf 05/2026, nicht final |
| BNetzA-URLs | `…/KI/start.html` | `…/KI/start_ki.html` (alte URL 404) |
| Mittelstand-Digital | BMWK | BMWE; Netzwerk läuft Ende 2026 aus, Neustart 2027 |

### Korrigierte Fehler im bisherigen Material

1. **Bußgelder KMU:** „Es gilt der höhere Betrag, Prozentsatz trifft KMU hart" → für KMU/Start-ups/SMC gilt der **niedrigere** Betrag (Art. 99 Abs. 6). Folie 19 alt / 27 neu, Rezept, Sprechtext.
2. **Bußgeldstufe „10 Mio. € / 2 %"** existiert nicht; Art. 50 fällt unter 15 Mio. € / 3 % (Art. 99 Abs. 4).
3. **„Bußgelder ab August 2026"** → Kapitel XII anwendbar seit 02.08.2025 (Art. 113 b); Art. 101 (GPAI) seit 02.08.2026; in Deutschland praktisch durchsetzbar seit KI-MIG.
4. **Grundrechte-Folgenabschätzung (Art. 27) als allgemeine Betreiberpflicht** → nur öffentliche Stellen, private Erbringer öffentlicher Dienste, Anhang III Nr. 5b/5c. Normales KMU mit HR-Tool: keine FRIA.
5. **„KI-Werbetexte und Social-Media-Posts müssen gekennzeichnet werden"** → falsch; Art. 50 Abs. 4 erfasst nur Deepfakes und Texte zu Themen öffentlichen Interesses ohne redaktionelle Kontrolle; Abs. 2 ist Anbieterpflicht.
6. **Betreiberpflichten Art. 26 unvollständig** → ergänzt: Eingabedaten (Abs. 4), Aussetzen/Melden (Abs. 5), Logs ≥ 6 Monate (Abs. 6), Information Beschäftigte/Betriebsrat vor Inbetriebnahme (Abs. 7), DSFA-Verweis (Abs. 9), Information Betroffener (Abs. 11), Recht auf Erläuterung (Art. 86).
7. **„Betreiber (Operator)"** → Betreiber = deployer; „operator" = Akteur (Art. 3 Nr. 8).
8. **„Alle 8 Bedingungen eines Verbots müssen zutreffen"** → alle Tatbestandsmerkmale des jeweiligen Verbots (kumulativ).
9. **Emotionserkennung am Arbeitsplatz ohne Ausnahme** → Ausnahme für medizinische und Sicherheitsgründe (Art. 5 Abs. 1 f).
10. **„Live-Gesichtserkennung im Einkaufszentrum = verboten"** → Verbot (h) nur Strafverfolgung; private Echtzeit-Fernidentifizierung ist Hochrisiko (Anhang III Nr. 1a).
11. **White-Label pauschal als Anbieter-Falle** → Art. 25 nur Hochrisiko; eigene App mit fremdem Modell = originärer Anbieter nach Art. 3 Nr. 3 (meist Nicht-Hochrisiko); Fine-Tuning → GPAI-Anbieter erst ab ⅓ Trainingsrechenleistung.
12. **Zeitplan überholt** (Hochrisiko 08/2026, Anhang I 08/2027, „Sanktionen ab 08/2026").
13. **README „~60 Folien"** → 26 alt, 41 neu.
14. Veraltete Zeitbezüge im Sprechtext („Normalfall 2025", „seit über einem Jahr").
15. Quellen-Statustabelle mit „403 Fehler"-Einträgen aus `eu_ai_act_recherche.md` entfernt.
16. Definition „KI-System" (Art. 3 Nr. 1, Leitlinien 02/2025) neu aufgenommen: Excel/regelbasierte Software ist kein KI-System.

### Neu

- **Folien:** 5 (KI-System-Definition), 8 (Änderungen 2026), 9 (Zuständigkeiten DE), 12 (Rollen-Grenzfälle), 15 (Ausnahme Art. 6 Abs. 3), 23 (öffentliche Stellen, Vereine), 25 (GPAI & Software-KMU), 28 (12 Mythen), 29–35 (Hands-on).
- **Vorlagen (`vorlagen/`)**: 01 KI-Inventar (XLSX mit Dropdowns), 02 Rollen- & Risiko-Check, 03 KI-Nutzungsrichtlinie, 04 Schulungskonzept & Nachweis (+ Teilnehmerliste XLSX), 05 Transparenz-Textbausteine, 06 Fragebogen an KI-Anbieter, 07 Information Beschäftigte & Betriebsrat, 08 Vorfall-Protokoll, 09 Fahrplan & Checkliste.
- **Tools:** `build_vorlagen.py` (Markdown → DOCX/XLSX), `check_links.py`.
- **Präsentation:** Foliennummern/IDs automatisch, Deep-Links `#fNN`, Taste `F` für Vollbild, Google-Fonts-Import korrigiert (stand zuvor nach anderen Regeln und wurde ignoriert), Hands-on-Layout, 3-spaltiges Verbote-Grid.
- `src.txt`: von 6 auf ~100 kategorisierte, geprüfte URLs mit Beschreibung und Stand.

### Link-Prüfung (09.09.2026)

`python tools/check_links.py` (urllib mit curl-Fallback): 102 URLs in 14 Dateien, 100 erreichbar oder bekannt
bot-blockiert (403 bei artificialintelligenceact.eu und consilium.europa.eu – im Browser erreichbar). 2 × HTTP 503 bei
ihk.de (Hannover, Lippe zu Detmold): Bot-Schutz der IHK-Plattform, im Browser erreichbar, in `src.txt` entsprechend markiert.
Entfernt/ersetzt: `bundesnetzagentur.de/…/KI/start.html` (404), `elementsofai.com/de` (→ elementsofai.de),
`e-recht24.de/ki/11416-chatbots-dsgvo.html` (→ …-konform-einsetzen.html), `e-recht24.de/ki/13485-ki-handwerker.html` (404, entfernt).

### Offene Punkte / bewusst vorsichtig formuliert

- Kommissions-Leitlinien zur Hochrisiko-Einstufung (Art. 6): Stand 09/2026 nur Entwurf.
- Harmonisierte Normen: keine im Amtsblatt → keine Konformitätsvermutung.
- EU-Datenbank (Art. 71): Live-Status nicht verifiziert.
- Deutsches KI-Reallabor (§ 13 KI-MIG): Antragsverfahren nicht veröffentlicht.
- Mittelstand-Digital: Nachfolgeprogramm ab 2027.
- Wortlaut der KI-MIG-Bußgeldvorschriften (§§ 15, 17) über gesetze-im-internet.de geprüft; Detailauslegung durch Behörden steht aus.
