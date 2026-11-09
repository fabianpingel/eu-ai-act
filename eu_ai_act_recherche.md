# EU AI Act – Recherche-Grundlage für den KMU-Workshop

**Rechtsstand: 9. November 2026**
**Vorgängerversion:** März 2026 (vor Digital Omnibus und KI-MIG – inhaltlich überholt, siehe `AENDERUNGEN.md`)

Dieses Dokument ist die fachliche Referenz für Foliensatz, Sprechtext, Rezept und Vorlagen. Alle Aussagen
sind mit Artikel/Absatz belegt; Quellen-URLs stehen kategorisiert in `src.txt`. Es ersetzt keine Rechtsberatung.

**Bevorzugte Quellen:** Verordnungstext (EUR-Lex / ai-act-law.eu DE), Bundesnetzagentur KI-Service-Desk,
e-recht24.de (KI-Rubrik), EU-Kommission (Leitlinien, Praxiskodizes), gesetze-im-internet.de (KI-MIG).

---

## 0. Einführung für Einsteiger

### 0.1 Warum gibt es den AI Act?

**Ausgangslage.** KI-Systeme treffen oder beeinflussen Entscheidungen über Menschen (Bewerbung, Kredit, Sozialleistungen,
Polizeiarbeit), erzeugen täuschend echte Inhalte und arbeiten für Betroffene intransparent. Bekannt gewordene Fälle,
die den Gesetzgeber geprägt haben: das 2018 eingestellte Amazon-Recruiting-System, das Bewerberinnen systematisch
abwertete; die niederländische „Toeslagenaffaire", in der ein Risikoalgorithmus tausende Familien zu Unrecht des
Kindergeldbetrugs beschuldigte (Rücktritt der Regierung 2021); Clearview AI mit einer aus Milliarden Netzfotos
erstellten Gesichtsdatenbank; Deepfakes und Stimmen-Klone für Betrug und Desinformation. Vor dem AI Act gab es für
KI-Anwendungen keine gemeinsamen Regeln – die DSGVO regelt Daten, das Produktsicherheitsrecht Maschinen.

**Ziele (Art. 1, Erwägungsgründe 1–8):** Funktionieren des Binnenmarkts mit einheitlichen Regeln; Förderung
menschenzentrierter, vertrauenswürdiger KI; hohes Schutzniveau für Gesundheit, Sicherheit und Grundrechte
(Demokratie, Rechtsstaat, Umwelt); Unterstützung von Innovation – u. a. durch Reallabore und KMU-Erleichterungen.

**Grundidee:** Reguliert wird nicht die Technologie, sondern die **riskante Anwendung**. Der AI Act folgt dem
Muster des europäischen Produktsicherheitsrechts („New Legislative Framework"): Anforderungen an das Produkt,
Konformitätsbewertung, CE-Kennzeichnung, Marktüberwachung. Ein Hochrisiko-KI-System wird behandelt wie eine
Maschine oder ein Medizinprodukt; harmlose Anwendungen bleiben weitgehend unreguliert.

**Was der AI Act nicht ist:** kein Verbot von KI; kein Datenschutzgesetz (DSGVO gilt parallel); kein
Haftungsgesetz (die geplante KI-Haftungsrichtlinie wurde 2025 zurückgezogen; es gelten BGB und Produkthaftung);
kein Gesetz nur für große Technologiekonzerne – er gilt für alle beruflichen Nutzer, aber nach Risiko abgestuft.

### 0.2 Wie das Gesetz funktioniert – vier Fragen

1. **Ist es ein KI-System?** (Art. 3 Nr. 1; Abschnitt 4) – kein gelerntes Modell → das Gesetz gilt nicht.
2. **Welche Rolle habe ich?** Anbieter (baut/vertreibt) oder Betreiber (nutzt) – Art. 3 Nr. 3/4; Abschnitt 4 und 11.
3. **Welche Risikostufe hat die Anwendung?** verboten / hoch / Transparenz / minimal – bestimmt durch den
   Einsatzzweck (Art. 5, 6, 50; Abschnitt 6).
4. **Welche Pflichten folgen?** Rolle × Risikostufe → konkrete Liste (Abschnitt 0.4, 7–9).

**Aufbau der Verordnung:** Kap. I Allgemeines, Begriffe, Art. 4 KI-Kompetenz · Kap. II Art. 5 Verbote ·
Kap. III Hochrisiko (Art. 6 Einstufung, 8–15 Anforderungen, 16–25 Anbieter und Lieferkette, 26–27 Betreiber) ·
Kap. IV Art. 50 Transparenz · Kap. V GPAI-Modelle · Kap. VI Innovation/Reallabore · Kap. VII Governance ·
Kap. VIII EU-Datenbank · Kap. IX Marktüberwachung · Kap. X Verhaltenskodizes · Kap. XII Sanktionen ·
Kap. XIII Übergangsvorschriften (Art. 113 Geltungsbeginn) · Anhänge I (Produktrecht), III (Hochrisiko-Bereiche),
IV (technische Dokumentation) u. a.

**Drei Grundsätze für Einsteiger:** (a) Verordnung, nicht Richtlinie – gilt unmittelbar; das KI-MIG regelt nur
Behörden. (b) Gestufter Start nach Art. 113 – daher die vielen Daten (Abschnitt 2). (c) Der Anbieter stuft sein
System ein und dokumentiert das (Art. 6 Abs. 4); der Betreiber fragt die Einstufung ab und plausibilisiert sie.

**Lesehilfe:** Artikel = Regel, Anhang = Liste, Erwägungsgrund = Begründung. Deutscher Text artikelweise:
https://ai-act-law.eu/de/ · Begriffe: `glossar.md` (35 Einträge).

### 0.3 Risikostufe bewerten – Methode in sechs Schritten

| Schritt | Frage | Ergebnis |
|---|---|---|
| **1 Beschreiben** | Was tut das System genau, für wen, mit welchen Daten? Zweckbestimmung des Anbieters (Art. 3 Nr. 12)? | Steckbrief im KI-Inventar (Vorlage 01) |
| **2 Verbot?** | Passt eine der 9 Praktiken aus Art. 5 – mit allen Tatbestandsmerkmalen? | ja → verboten, Einsatz stoppen |
| **3 Produkt?** | Ist die KI Sicherheitsbauteil eines CE-pflichtigen Produkts (Anhang I)? | ja → Hochrisiko, Pflichten ab 02.08.2028 |
| **4 Bereich?** | Einsatz in einem der 8 Bereiche von Anhang III? Falls ja: Ausnahme Art. 6 Abs. 3 (enge Verfahrensaufgabe, Verbesserung, Mustererkennung, Vorbereitung)? Profiling natürlicher Personen → keine Ausnahme | ja → Hochrisiko, Pflichten ab 02.12.2027; Ausnahme → weiter |
| **5 Transparenz?** | Interaktion mit Menschen, generierte Inhalte, Deepfakes, Texte zu Themen öffentlichen Interesses, Emotionserkennung/biometrische Kategorisierung? | ja → Art. 50 (seit 02.08.2026) |
| **6 Sonst** | Nichts davon? | minimales Risiko – Art. 4 und DSGVO bleiben |

**Faustregeln:** „Bewertet oder entscheidet es über Menschen?" → Hochrisiko-Verdacht · „Redet es oder erzeugt es
Inhalte?" → Transparenz · „Hilft es nur intern beim Arbeiten?" → meist minimal. Ein System kann mehrere Stufen
treffen (z. B. HR-Chatbot: hoch + Transparenz) – höchste Stufe plus Art. 50 prüfen. Ergebnis mit Begründung
dokumentieren (Vorlage 02), Anbieter-Einstufung einholen (Vorlage 06), bei Widerspruch nachfragen;
Hilfsmittel: BNetzA KI-Compliance-Kompass.

**Beispiel Elektro Müller GmbH (30 Beschäftigte):**

| Tool | Schritte | Stufe | Betreiberpflichten |
|---|---|---|---|
| ChatGPT Team (Angebote, E-Mails; keine Kundendaten) | 2 nein · 3/4 nein · 5 nein (interne Texte, Angebote geprüft) | minimal | Art. 4, Richtlinie, AVV, Trainings-Opt-out |
| Website-Chatbot (Öffnungszeiten, Termine) | 2 nein · 3/4 nein · 5 ja (Interaktion) | Transparenz | KI-Hinweis sichtbar, Datenschutzerklärung, AVV, Art. 4 |
| Bewerberportal mit Score/Ranking | 2 nein · 4 ja: Anhang III Nr. 4; Score = Profiling → keine Ausnahme | hoch (ab 12/2027) | jetzt: Anbieter-Fragebogen, Betriebsrat; ab 12/2027: Art. 26 |
| Werkstattkamera „Stimmungsbarometer" | 2 ja: Art. 5 Abs. 1 f, kein Medizin-/Sicherheitszweck | verboten | abschalten, Anbieter informieren, dokumentieren |

### 0.4 Pflichten je Stufe – Gesamtmatrix

| Stufe | Anbieter muss … | Betreiber muss … | Gilt seit / ab |
|---|---|---|---|
| **verboten** (Art. 5) | nicht in Verkehr bringen; Anbieter generativer Bild-KI: Schutzmaßnahmen gegen Missbrauchsinhalte bis 02.12.2026 | nicht einsetzen, laufende Systeme abschalten | 02.02.2025 |
| **hoch** (Art. 6, Anhang I/III) | Risikomanagement (9), Daten-Governance (10), technische Dokumentation (11, KMU-Formular), Protokollierung (12), Betriebsanleitung (13), Aufsicht ermöglichen (14), Genauigkeit/Robustheit/Cybersicherheit (15), QM (17), Aufbewahrung 10 Jahre (18), Konformitätsbewertung (43), Konformitätserklärung + CE (47, 48), Registrierung EU-Datenbank (49), Beobachtung nach Inverkehrbringen (72), Vorfallmeldung (73) | Betriebsanleitung befolgen (26 Abs. 1), kompetente Aufsicht (Abs. 2), Eingabedaten (Abs. 4), überwachen/aussetzen/melden (Abs. 5), Logs ≥ 6 Monate (Abs. 6), Beschäftigte + Arbeitnehmervertretung vorab informieren (Abs. 7), DSFA-Infos nutzen (Abs. 9), Betroffene informieren (Abs. 11), Erläuterung geben (Art. 86). Zusätzlich nur öffentliche Stellen/öffentliche Dienste/Kredit/Versicherung: FRIA (27); nur Behörden: Registrierung (Abs. 8, 49 Abs. 3) | Anhang III: **02.12.2027** · Anhang I: 02.08.2028 |
| **Transparenz** (Art. 50) | Interaktion erkennbar machen (Abs. 1); generierte Inhalte maschinenlesbar kennzeichnen (Abs. 2; Altsysteme bis 02.12.2026) | KI-Hinweis sichtbar halten; Deepfakes offenlegen; KI-Texte zu öffentlichen Themen offenlegen oder redaktionell verantworten; bei Emotionserkennung/biometrischer Kategorisierung informieren (Abs. 3, 4) | 02.08.2026 |
| **minimal** | keine spezifischen Pflichten; freiwillige Verhaltenskodizes (Art. 95) | keine spezifischen Pflichten | – |
| **alle Stufen** | **Art. 4 KI-Kompetenz** (Maßnahmen fördern, dokumentieren) · **DSGVO** (AVV, Information, ggf. DSFA) · Urheber-, Wettbewerbs-, Arbeitsrecht | ebenso | 02.02.2025 / seit jeher |

Lesart für kleine Organisationen: Betreiber-Spalte, Zeilen „Transparenz" und „alle Stufen" = heutige Liste.
Zeile „hoch" wird erst 2027 relevant und nur bei Nutzung eines Anhang-III-Systems.

---

## 1. Rechtsgrundlagen

| Rechtsakt | Kurzname | Datum | Bedeutung |
|---|---|---|---|
| Verordnung (EU) 2024/1689 | KI-Verordnung (KI-VO), AI Act | ABl. 12.07.2024, in Kraft 01.08.2024 | Grundverordnung, unmittelbar geltend in allen EU-Staaten |
| Verordnung (EU) 2026/1744 | „Digital Omnibus on AI", KI-Omnibus | ABl. 24.07.2026, in Kraft **27.07.2026** | Ändert die KI-VO: Fristen, Art. 4, Art. 50, neues Verbot, KMU/SMC-Erleichterungen |
| KI-Marktüberwachungs- und Innovationsförderungs-Gesetz (**KI-MIG**) | deutsches Durchführungsgesetz | 22.07.2026, BGBl. 2026 I Nr. 223, in Kraft **29.07.2026** | Zuständige Behörden in Deutschland, Reallabor, nationale Bußgelder |

**Charakter:** Verordnung, keine Richtlinie – gilt ohne nationales Umsetzungsgesetz. Das KI-MIG regelt nur,
*welche deutsche Behörde was macht*, keine zusätzlichen materiellen Pflichten für Unternehmen.

**Räumlicher Anwendungsbereich (Art. 2 Abs. 1):** Anknüpfung an Inverkehrbringen/Inbetriebnahme in der
EU bzw. an Nutzung, deren Ausgabe in der EU verwendet wird – nicht an den Firmensitz. Ein US-Tool, das in
Deutschland eingesetzt wird, fällt darunter; der deutsche Betreiber hat eigene Pflichten.

---

## 2. Zeitplan – Stand 9. November 2026

| Datum | Was gilt | Status |
|---|---|---|
| 01.08.2024 | Inkrafttreten KI-VO | ✅ |
| 02.02.2025 | Verbotene Praktiken (Art. 5), KI-Kompetenz (Art. 4), Kapitel I–II | ✅ gilt |
| 02.08.2025 | GPAI-Pflichten (Kap. V), Governance (Kap. VII), **Sanktionen Kap. XII außer Art. 101** (Art. 113 b) | ✅ gilt |
| 27.07.2026 | Digital Omnibus (VO 2026/1744) tritt in Kraft | ✅ |
| 29.07.2026 | KI-MIG tritt in Kraft; BNetzA zentrale Marktüberwachung | ✅ |
| **02.08.2026** | **Transparenzpflichten Art. 50** (Abs. 1, 3, 4 voll; Abs. 2 s. u.); Aufsicht über Art. 4 durch nationale Behörden; Art. 101 GPAI-Bußgelder; allgemeiner Geltungsbeginn | ✅ gilt |
| 02.12.2026 | Ende Übergangsfrist Art. 50 Abs. 2 (maschinenlesbare Kennzeichnung) für Systeme, die vor 02.08.2026 auf dem Markt waren; technische Umsetzung neues Verbot (CSAM/Intimbilder) | ⏳ |
| 02.08.2027 | GPAI-Modelle, die vor 02.08.2025 auf dem Markt waren, müssen konform sein; **Reallabor-Pflicht der Mitgliedstaaten** (verschoben von 02.08.2026) | ⏳ |
| **02.12.2027** | **Hochrisiko-Pflichten Anhang III** (Kap. III Abschn. 1–3, Art. 26/27 Betreiber) – verschoben von 02.08.2026 | ⏳ |
| **02.08.2028** | **Hochrisiko-Pflichten Anhang I** (KI in regulierten Produkten) – verschoben von 02.08.2027 | ⏳ |
| 02.08.2030 | Hochrisiko-Systeme öffentlicher Stellen, die vor Geltungsbeginn in Betrieb waren | ⏳ |

**Merksatz für den Workshop:** *„Drei Dinge gelten heute: Verbote, KI-Kompetenz, Transparenz. Hochrisiko
kommt Dezember 2027 – jetzt vorbereiten, nicht panisch umsetzen."*

---

## 3. Was der Digital Omnibus (VO 2026/1744) geändert hat

| Punkt | Vorher (KI-VO 2024) | Nachher (seit 27.07.2026) |
|---|---|---|
| Hochrisiko Anhang III | 02.08.2026 | **02.12.2027** |
| Hochrisiko Anhang I | 02.08.2027 | **02.08.2028** |
| Art. 4 KI-Kompetenz | „Maßnahmen ergreifen, um … sicherzustellen" | „Maßnahmen ergreifen, um die Entwicklung von KI-Kompetenz zu **fördern**"; ausdrücklich **kein garantiertes Kompetenzniveau** für einzelne Personen; zusätzlich Förderpflicht von Kommission und Mitgliedstaaten |
| Art. 50 Abs. 2 (maschinenlesbare Kennzeichnung durch Anbieter) | 02.08.2026 | Für Systeme, die vor 02.08.2026 auf dem Markt waren: Übergang bis **02.12.2026**. Alle anderen Art.-50-Pflichten unverändert ab 02.08.2026 |
| Art. 5 Verbote | 8 Verbote | **9 Verbote**: neu KI-Systeme zur Erzeugung von Darstellungen sexuellen Kindesmissbrauchs (CSAM) und nicht-einvernehmlicher intimer Inhalte („Nudify-Apps"); technische Schutzmaßnahmen bis 02.12.2026 |
| KMU-Erleichterungen | KMU/Start-ups | Erweitert auf **Small Mid-Caps (SMC)**: < 750 Beschäftigte und ≤ 150 Mio. € Umsatz bzw. ≤ 129 Mio. € Bilanzsumme. Gilt für vereinfachte Doku (Art. 11), proportionales QM, Reallabor-Vorrang, niedrigere Bußgeldobergrenze (Art. 99 Abs. 6) |
| Art. 6 Abs. 3 Ausnahme-Registrierung | Registrierung in EU-Datenbank (Art. 49 Abs. 2) | Bleibt, mit reduziertem Informationsumfang (Anhang VIII Abschn. B gekürzt) |
| Reallabore (Art. 57) | bis 02.08.2026 | bis **02.08.2027** |
| Bias-Erkennung (neu Art. 4a) | nur Hochrisiko | Verarbeitung besonderer Datenkategorien zur Bias-Erkennung/-Korrektur auch für andere KI-Systeme, wenn unbedingt erforderlich |
| AI Office | GPAI-Modelle | zusätzlich zuständig für KI-Systeme auf GPAI-Basis desselben Unternehmens |
| Sanktionen Art. 99 | – | **unverändert** (weiterhin seit 02.08.2025 anwendbar) |
| Materielle Hochrisiko-Anforderungen (Art. 8–27) | – | **inhaltlich unverändert**, nur später anwendbar |

**Hinweis für Teilnehmer:** Fachartikel und Kanzlei-Blogs von vor Juli 2026 nennen noch den 2. August 2026
als Hochrisiko-Stichtag und teils „2. Februar 2027" als Kennzeichnungs-Übergang (Kommissionsvorschlag,
im Trilog auf 2. Dezember 2026 verkürzt). Beides ist überholt.

---

## 4. Definitionen (Art. 3)

### KI-System (Art. 3 Nr. 1)
Maschinengestütztes System, das für einen in unterschiedlichem Grade autonomen Betrieb ausgelegt ist,
nach Inbetriebnahme anpassungsfähig sein kann und aus Eingaben **ableitet**, wie Ausgaben (Vorhersagen,
Inhalte, Empfehlungen, Entscheidungen) erzeugt werden, die physische oder virtuelle Umgebungen beeinflussen.

**Kommissions-Leitlinien zur Definition (06.02.2025) – was KEIN KI-System ist:**
- Software, die nur vordefinierte Regeln/Formeln abarbeitet (Tabellenkalkulation mit festen Formeln, Excel-Makro)
- klassische Sortier-/Suchalgorithmen mit festen Regeln, einfache Heuristiken
- klassische Statistik/Regression ohne Lernkomponente, wenn keine Ableitungsfähigkeit im Sinne der Definition vorliegt

**Typische KI-Systeme im KMU:** ChatGPT/Copilot/Gemini, Website-Chatbots, Bild-/Video-Generatoren,
Transkriptions-/Übersetzungs-KI, Bewerber-Screening/-Ranking, Betrugs-/Kredit-Scoring, Bildanalyse.

### Akteure (Art. 3 Nr. 3–8) – Begriffe korrekt zuordnen

| Deutsch | Englisch | Art. 3 | Definition |
|---|---|---|---|
| **Anbieter** | Provider | Nr. 3 | Entwickelt ein KI-System/GPAI-Modell oder lässt es entwickeln **und** bringt es unter eigenem Namen/Marke in Verkehr oder nimmt es in Betrieb – entgeltlich oder unentgeltlich |
| **Betreiber** | **Deployer** | Nr. 4 | Verwendet ein KI-System in eigener Verantwortung, außer im Rahmen persönlicher, nicht-beruflicher Tätigkeit |
| Bevollmächtigter | Authorised representative | Nr. 5 | Schriftlich beauftragte EU-Vertretung eines Drittland-Anbieters |
| Einführer | Importer | Nr. 6 | Bringt System eines Drittland-Anbieters in der EU in Verkehr |
| Händler | Distributor | Nr. 7 | Stellt System in der Lieferkette bereit, ohne Anbieter/Einführer zu sein |
| **Akteur** | **Operator** | Nr. 8 | Oberbegriff für alle Vorgenannten (+ Produkthersteller) |

> ⚠ Häufiger Fehler: „Betreiber (Operator)". Richtig ist **Betreiber = Deployer**; „Operator" ist der
> Sammelbegriff „Akteur".

### Weitere Begriffe
- **Deepfake (Nr. 60):** durch KI erzeugter oder manipulierter Bild-, Ton- oder Videoinhalt, der wirklichen
  Personen, Gegenständen, Orten, Einrichtungen oder Ereignissen ähnelt und einer Person fälschlicherweise
  als echt oder wahrheitsgemäß erscheinen würde.
- **GPAI-Modell (Nr. 63):** KI-Modell mit erheblicher allgemeiner Verwendbarkeit für ein breites Spektrum
  von Aufgaben (z. B. GPT, Claude, Gemini, Llama, Mistral).
- **Wesentliche Veränderung (Nr. 23):** nachträgliche Änderung, die in der ursprünglichen Konformitätsbewertung
  nicht vorgesehen war und die Konformität beeinträchtigt oder die Zweckbestimmung ändert.
- **KI-Kompetenz (Nr. 56):** Fähigkeiten, Kenntnisse und Verständnis, um KI-Systeme sachkundig einzusetzen
  und sich der Chancen und Risiken bewusst zu sein.
- **KMU:** < 250 Beschäftigte und ≤ 50 Mio. € Umsatz oder ≤ 43 Mio. € Bilanzsumme (Empfehlung 2003/361/EG).
  **SMC (neu):** < 750 Beschäftigte, ≤ 150 Mio. € Umsatz / ≤ 129 Mio. € Bilanzsumme.

---

## 5. Anwendungsbereich und Ausnahmen (Art. 2)

| Abs. | Ausnahme | Praxis |
|---|---|---|
| 3 | Ausschließlich militärische, Verteidigungs- oder nationale Sicherheitszwecke | – |
| 6 | KI-Systeme/-Modelle eigens für wissenschaftliche Forschung und Entwicklung | Forschungseinrichtungen |
| 8 | Forschungs-, Test- und Entwicklungstätigkeiten vor Inverkehrbringen (außer Tests unter Realbedingungen) | interne Prototypen |
| 10 | Betreiber, die natürliche Personen sind, bei ausschließlich persönlicher, nicht-beruflicher Nutzung | Privatnutzung |
| 12 | Freie und quelloffene KI-Systeme – **außer** wenn Hochrisiko, verboten oder Art. 50 einschlägig | Open-Source-Modelle |

**Nicht ausgenommen:** Vereine, gemeinnützige Organisationen, Kommunen, Freiberufler, Kleinstunternehmen.
„Beruflich" umfasst auch ehrenamtliche/organisatorische Tätigkeit im Namen einer Organisation.

---

## 6. Risikostufen

### 6.1 Verbotene Praktiken (Art. 5) – seit 02.02.2025, 9 Verbote

| # | Verbot (Art. 5 Abs. 1) | Kern | Ausnahme / Abgrenzung | KMU-Relevanz |
|---|---|---|---|---|
| 1 | (a) Unterschwellige/manipulative Techniken | Verhaltensverzerrung + erheblicher Schaden | Alle Merkmale kumulativ | gering |
| 2 | (b) Ausnutzung von Vulnerabilität | Alter, Behinderung, soziale/wirtschaftliche Lage | – | gering; Vorsicht bei Marketing-Automation gegenüber Kindern |
| 3 | (c) Social Scoring | Bewertung nach Sozialverhalten mit ungerechtfertigter Benachteiligung | – | gering |
| 4 | (d) Straftat-Prognose | allein aufgrund Profiling/Persönlichkeitsmerkmalen | Unterstützung menschlicher Bewertung auf Faktenbasis | keine |
| 5 | (e) Ungezieltes Gesichts-Scraping | Aufbau von Gesichtsdatenbanken aus Internet/Video | – | keine |
| 6 | (f) **Emotionserkennung am Arbeitsplatz und in Bildungseinrichtungen** | Ableitung von Emotionen aus biometrischen Daten | **medizinische oder Sicherheitsgründe** | **hoch**: Stimmungs-/Aufmerksamkeitsanalyse von Beschäftigten, Schülern |
| 7 | (g) Biometrische Kategorisierung | Rückschluss auf Ethnie, politische/religiöse Überzeugung, Sexualität etc. | Kennzeichnung rechtmäßig erworbener Datensätze | gering |
| 8 | (h) Biometrische Echtzeit-Fernidentifizierung in öffentlichen Räumen | **nur zu Strafverfolgungszwecken** | eng begrenzte Ausnahmen mit Genehmigung | keine – **private** Echtzeit-Gesichtserkennung (z. B. Einzelhandel) ist nicht verboten, sondern **Hochrisiko** (Anhang III Nr. 1a) |
| 9 | **neu** (Omnibus) KI zur Erzeugung von CSAM / nicht-einvernehmlichen intimen Inhalten | Generierung solcher Inhalte | technische Schutzpflicht für Anbieter bis 02.12.2026 | Anbieter generativer Bild-KI |

**Auslegung (Kommissions-Leitlinien 04.02.2025):** Jedes Verbot ist ein Bündel **kumulativer**
Tatbestandsmerkmale – alle müssen erfüllt sein. Kein „in der Nähe" reicht.

### 6.2 Hochrisiko-KI (Art. 6, Anhänge I und III) – Anhang III ab 02.12.2027, Anhang I ab 02.08.2028

**Zwei Wege in die Hochrisiko-Klasse:**
- **Anhang I:** KI ist Produkt oder Sicherheitsbauteil unter Harmonisierungsrecht **mit** Drittzertifizierung
  (Maschinen, Spielzeug, Aufzüge, Medizinprodukte, Funkanlagen, Fahrzeuge …).
- **Anhang III:** eigenständige Systeme in 8 Bereichen:

| Nr. | Bereich | Für kleine Organisationen relevant |
|---|---|---|
| 1 | Biometrie (Fernidentifizierung, Kategorisierung nach sensiblen Merkmalen, Emotionserkennung) | private Gesichtserkennung; **1:1-Verifizierung ist ausgenommen** |
| 2 | Kritische Infrastruktur (Sicherheitskomponenten Verkehr, Wasser, Gas, Strom, digitale Infrastruktur) | Versorger, Stadtwerke |
| 3 | **Bildung**: Zulassung, Leistungsbewertung, Niveaubestimmung, Prüfungsaufsicht | Bildungsträger, Vereine mit Kursangebot, Schulen |
| 4 | **Beschäftigung**: (a) Einstellung/Auswahl – gezielte Stellenanzeigen, **Sichten/Filtern von Bewerbungen**, Bewertung von Bewerbern; (b) Entscheidungen über Beschäftigungsbedingungen, Beförderung, Kündigung, Aufgabenzuweisung nach Verhalten/Persönlichkeit, **Überwachung/Bewertung von Leistung und Verhalten** | **jedes KMU mit KI im HR-Prozess** |
| 5 | Grundlegende Dienste: (a) Sozialleistungen (Behörden), (b) **Kreditwürdigkeit/Bonität** natürlicher Personen (Ausnahme Betrugserkennung), (c) Risikobewertung/Preis bei **Lebens- und Krankenversicherung**, (d) Notfall-Triage | Banken, Versicherer, Kommunen |
| 6 | Strafverfolgung | Behörden |
| 7 | Migration, Asyl, Grenze | Behörden |
| 8 | Rechtspflege, demokratische Prozesse (Wahlbeeinflussung) | Justiz |

**Ausnahme Art. 6 Abs. 3:** Kein Hochrisiko trotz Anhang III, wenn das System kein erhebliches
Risiko darstellt, weil es (a) eine enge Verfahrensaufgabe erfüllt, (b) das Ergebnis einer bereits
abgeschlossenen menschlichen Tätigkeit verbessert, (c) Entscheidungsmuster/Abweichungen erkennt, ohne die
menschliche Bewertung ohne Überprüfung zu ersetzen, oder (d) eine vorbereitende Aufgabe übernimmt.
**Rückausnahme:** Bei **Profiling natürlicher Personen** immer Hochrisiko. Der **Anbieter** dokumentiert
die Einschätzung vor Inverkehrbringen und registriert sich (Art. 6 Abs. 4, Art. 49 Abs. 2, seit Omnibus
mit reduziertem Umfang). **Kommissions-Leitlinien zu Art. 6:** Entwurf vom 19./20.05.2026, Konsultation
im Sommer 2026 – Stand 09.11.2026 weiterhin nicht final verabschiedet.

**Praxis HR-Tool:** Reines Keyword-Matching mit anschließender vollständiger menschlicher Sichtung kann
unter (d)/(c) fallen; ein Ranking/Score über Bewerber ist Profiling → Hochrisiko. Die Einstufung trifft
der Anbieter; der Betreiber sollte sie beim Anbieter abfragen (Vorlage 06).

### 6.3 Transparenzpflichten (Art. 50) – seit 02.08.2026

| Abs. | Adressat | Pflicht | Ausnahmen |
|---|---|---|---|
| 1 | **Anbieter** | Systeme für direkte Interaktion mit Menschen so gestalten, dass die Person weiß, dass sie mit KI interagiert | wenn aus Sicht einer aufmerksamen Person offensichtlich; Strafverfolgung |
| 2 | **Anbieter** | Ausgaben generativer Systeme (Text, Bild, Audio, Video) in **maschinenlesbarem Format** kennzeichnen (Wasserzeichen, C2PA-Metadaten …); wirksam, interoperabel, belastbar | Unterstützungsfunktion für Standardbearbeitung; keine wesentliche Änderung der Eingabe; Strafverfolgung. **Übergang bis 02.12.2026 für Altsysteme** |
| 3 | **Betreiber** | Bei Emotionserkennung / biometrischer Kategorisierung: betroffene Personen über den Betrieb informieren (DSGVO beachten) | Strafverfolgung |
| 4 UAbs. 1 | **Betreiber** | **Deepfakes** offenlegen (Bild/Audio/Video, das künstlich erzeugt/manipuliert ist) | offensichtlich künstlerisch/satirisch/fiktional: Offenlegung, die Werkgenuss nicht beeinträchtigt |
| 4 UAbs. 2 | **Betreiber** | KI-generierten/manipulierten **Text**, der veröffentlicht wird, **um die Öffentlichkeit über Angelegenheiten von öffentlichem Interesse zu informieren**, offenlegen | **menschliche Überprüfung/redaktionelle Kontrolle** mit Verantwortungsübernahme |

**Was daraus für KMU folgt – und was NICHT:**
- Website-Chatbot: Hinweis „Sie chatten mit einer KI" – Pflicht liegt beim Anbieter des Chatbots, der Betreiber
  muss sicherstellen, dass der Hinweis in seiner Einbindung sichtbar ist (Vertrag/Konfiguration).
- **Keine allgemeine Kennzeichnungspflicht** für KI-erstellte Werbetexte, Produktbeschreibungen, Newsletter,
  interne Texte, Social-Media-Posts ohne Täuschungscharakter. Ein pauschaler Disclaimer ist weder nötig noch
  ausreichend (eRecht24, Stand 29.07.2026).
- Deepfake nur bei **täuschend echter** Nachahmung realer Personen/Orte/Ereignisse; Retusche, Beleuchtung,
  Hintergrund entfernen sind keine Deepfakes. KI-generiertes Symbolbild eines Büros: kein Deepfake.
- Maschinenlesbare Kennzeichnung (Abs. 2) ist **Anbieter**pflicht – wer aber eine eigene App mit GPT-API
  in Verkehr bringt, ist Anbieter dieses Systems und muss Abs. 1/2 selbst erfüllen (z. B. über die
  Kennzeichnungsfunktionen des Modellanbieters).
- **Praxiskodex Kennzeichnung (Code of Practice on Transparency of AI-generated Content):** final
  10.06.2026, ca. 190 Unterzeichner; von Kommission und KI-Gremium als **angemessener** Nachweisweg
  bestätigt (Juli 2026). EU-Icon-Set für Labels (Nutzung optional). Wer den Kodex unterzeichnet und
  einhält, kann die Erfüllung von Abs. 2, 4 und 5 darüber nachweisen.
- **Kommissions-Leitlinien zu Art. 50:** Entwurf 08.05.2026, **final 20.07.2026** (C(2026) 5054,
  Pressemitteilung IP/26/1653). Erläutern alle fünf Absätze mit Beispielen; ausdrücklich erfasst sind
  KI-Agenten (Abs. 1). Bloße Rechtschreib- und Grammatikkorrektur ist keine Generierung.

### 6.4 Minimales Risiko
Alle übrigen Systeme (Spam-Filter, Empfehlungen, Übersetzung, Bildoptimierung, Suche, interne
Textassistenz). **Keine spezifischen Pflichten** aus Kap. III/IV. Trotzdem gelten: Art. 4 KI-Kompetenz
(rollen-, nicht risikoabhängig), DSGVO, Urheberrecht, UWG, Geschäftsgeheimnisschutz. Verhaltenskodizes
nach Art. 95 sind **freiwillig**.

---

## 7. KI-Kompetenz (Art. 4) – seit 02.02.2025, Wortlaut geändert 27.07.2026

**Neuer Wortlaut (sinngemäß):** Anbieter und Betreiber ergreifen Maßnahmen, um die Entwicklung eines
ausreichenden Maßes an KI-Kompetenz ihres Personals und anderer Personen, die in ihrem Auftrag KI-Systeme
betreiben und nutzen, **zu fördern** – unter Berücksichtigung von technischem Wissen, Erfahrung,
Ausbildung und Schulung sowie des Einsatzkontexts und der betroffenen Personen. **Die Pflicht verlangt
nicht, ein bestimmtes Kompetenzniveau einer bestimmten Person zu garantieren.**

**Wer:** jeder Anbieter und Betreiber – jede Größe, jede Branche, auch bei ausschließlicher Nutzung von
ChatGPT/Copilot (minimales Risiko). Umfasst Beschäftigte **und** Auftragnehmer/Freelancer, die im Auftrag KI nutzen.

**Was NICHT gefordert ist (Kommission Q&A 07.05.2025; BNetzA; Omnibus):**
- kein Pflichtzertifikat, keine Prüfung, kein vorgeschriebenes Format oder Stundenumfang
- kein KI-Beauftragter
- kein garantiertes Kompetenzniveau je Person
- **kein eigener Bußgeldtatbestand** in Art. 99 (Art. 4 ist dort nicht gelistet). Durchsetzung durch
  Marktüberwachung seit 02.08.2026 mittelbar (Anordnungen, Sorgfaltsmaßstab bei Schäden, Haftung).

**Was die BNetzA empfiehlt (drei Grundsteine):**
1. **Bedarf ermitteln:** Wer nutzt welche Systeme mit welchem Risiko? Vorkenntnisse?
2. **Maßnahmen gestalten:** nach Rolle (Anbieter/Betreiber), Kontext, Risiko; Formate frei (Workshop,
   E-Learning, Leitfaden, Peer-Learning). Stufenmodell: (1) Grundlagen KI/Daten/Chancen/Risiken,
   (2) rollenspezifisch: rechtliche Einordnung, spezifische Risiken, (3) fachspezifische Vertiefung.
3. **Dokumentieren, evaluieren, auffrischen:** Art, Umfang, Teilnehmende, Datum – empfohlen, nicht
   vorgeschrieben; dient als Nachweis bei Anfragen und im Schadensfall.

**Dieser Workshop** ist eine Stufe-1/2-Maßnahme; Teilnahmeliste (Vorlage 04) = Nachweis.

---

## 8. Betreiberpflichten (Art. 26, 27, 86) – Hochrisiko, ab 02.12.2027

| Art. 26 | Pflicht | Praxis kleine Organisation |
|---|---|---|
| Abs. 1 | Verwendung gemäß **Betriebsanleitung** des Anbieters; geeignete technische/organisatorische Maßnahmen | Anleitung lesen, Zweck einhalten, Prozess dokumentieren |
| Abs. 2 | **Menschliche Aufsicht** durch Personen mit erforderlicher Kompetenz, Ausbildung, Befugnis und Unterstützung | Verantwortliche benennen, schulen, Zeit einräumen |
| Abs. 3 | Aufsichtsmaßnahmen unbeschadet anderer Pflichten; Freiheit bei Organisation | – |
| Abs. 4 | **Eingabedaten** (soweit kontrolliert) relevant und repräsentativ für die Zweckbestimmung | keine Fremd-/Altdaten unreflektiert einspielen |
| Abs. 5 | Betrieb **überwachen**; bei Risiko (Art. 79 Abs. 1) **Anbieter/Händler/Einführer und Marktüberwachung informieren, Nutzung aussetzen**; schwerwiegende Vorfälle **unverzüglich** melden | Vorfall-Protokoll (Vorlage 08), BNetzA-Kontakt |
| Abs. 6 | **Protokolle aufbewahren, mindestens 6 Monate** (soweit unter Kontrolle des Betreibers) | Log-Export mit Anbieter klären |
| Abs. 7 | **Vor Inbetriebnahme am Arbeitsplatz: Arbeitnehmervertreter und betroffene Beschäftigte informieren** | Vorlage 07; § 87 BetrVG zusätzlich prüfen |
| Abs. 8 | Registrierung in EU-Datenbank – **nur Behörden/öffentliche Stellen** (Art. 49 Abs. 3) | Kommunen |
| Abs. 9 | Anbieter-Informationen für **DSFA nach Art. 35 DSGVO** nutzen | keine neue KI-DSFA, sondern die vorhandene DSGVO-Pflicht |
| Abs. 10 | Nachträgliche biometrische Fernidentifizierung – nur Strafverfolgung | – |
| Abs. 11 | **Betroffene natürliche Personen informieren**, wenn das System Entscheidungen über sie trifft oder unterstützt | Bewerber, Kunden, Bürger |
| Abs. 12 | Zusammenarbeit mit Behörden | – |

**Art. 27 Grundrechte-Folgenabschätzung (FRIA) – nur für:**
- Einrichtungen des öffentlichen Rechts und private Einrichtungen, die **öffentliche Dienste** erbringen
  (Bildung, Gesundheit, Soziales, Wohnen, Justiz …),
- Betreiber von Systemen nach **Anhang III Nr. 5 b (Kreditwürdigkeit) und 5 c (Lebens-/Krankenversicherung)**.
Inhalt: Prozesse, Zeitraum/Häufigkeit, betroffene Personengruppen, spezifische Schadensrisiken,
Aufsichtsmaßnahmen, Maßnahmen bei Risikoeintritt; Ergebnis an Marktüberwachung melden (Fragebogen der
Kommission). **Ein KMU mit HR-Tool muss keine FRIA machen.** Nationales Bußgeld bei Unterlassung: § 15
KI-MIG bis 50.000 € (nicht gegen Behörden, § 17 Abs. 2).

**Art. 86 Recht auf Erläuterung:** Personen, die von einer Entscheidung auf Basis eines Anhang-III-Systems
(außer Nr. 2) mit Rechtswirkung oder erheblicher Beeinträchtigung betroffen sind, können vom **Betreiber**
eine klare, aussagekräftige Erläuterung der Rolle des KI-Systems und der wesentlichen Entscheidungselemente
verlangen.

---

## 9. Anbieterpflichten Hochrisiko (Überblick) und KMU-Erleichterungen

| Art. | Pflicht |
|---|---|
| 9 | Risikomanagementsystem über den gesamten Lebenszyklus |
| 10 | Daten-Governance: Trainings-/Validierungs-/Testdaten, Bias-Prüfung |
| 11 + Anh. IV | Technische Dokumentation – **vereinfachtes Formular für KMU/SMC** |
| 12 | Automatische Protokollierung |
| 13 | Transparenz + Betriebsanleitung für Betreiber |
| 14 | Menschliche Aufsicht technisch ermöglichen |
| 15 | Genauigkeit, Robustheit, Cybersicherheit |
| 17 | Qualitätsmanagementsystem – **proportional für KMU/SMC** |
| 18 | Aufbewahrung technische Dokumentation **10 Jahre** |
| 43 | Konformitätsbewertung (meist interne Kontrolle; Biometrie ggf. notifizierte Stelle) |
| 47/48 | EU-Konformitätserklärung, CE-Kennzeichnung |
| 49/71 | Registrierung in der **öffentlichen EU-Datenbank** |
| 72/73 | Beobachtung nach dem Inverkehrbringen; Meldung schwerwiegender Vorfälle (15 Tage, bei Todesfall 10 Tage, weitverbreitet 2 Tage) |
| 62 | **KMU-Maßnahmen:** vorrangiger Reallabor-Zugang, Sensibilisierung, reduzierte Gebühren für Konformitätsbewertung |

**Harmonisierte Normen (CEN-CENELEC JTC 21):** Seit **19.10.2026** ist mit **EN 18286:2026**
(Qualitätsmanagementsystem) die erste Norm im Amtsblatt zitiert (Durchführungsbeschluss (EU) 2026/2274) →
Konformitätsvermutung nach Art. 40 **nur für Art. 17** (QM-System). Für alle übrigen Anforderungen
(u. a. prEN 18228 Risikomanagement) Stand 11/2026 keine Vermutung; weitere Normen sind angekündigt.

---

## 10. GPAI-Modelle (Art. 51–56) – seit 02.08.2025

- **Anbieter des Modells** (OpenAI, Google, Anthropic, Meta, Mistral, Aleph Alpha …): technische Dokumentation,
  Informationen für nachgelagerte Anbieter, Urheberrechts-Strategie, Trainingsdaten-Zusammenfassung.
  Systemisches Risiko (> 10²⁵ FLOP): zusätzlich Evaluierung, Risikominderung, Vorfallmeldung, Cybersicherheit.
- **GPAI-Praxiskodex** (10.07.2025) als Nachweisweg; Kommissions-Leitlinien GPAI (18.07.2025).
- **Ein KMU wird durch API-Nutzung, Prompting, RAG oder Systemprompts NICHT GPAI-Anbieter.** Fine-Tuning
  macht erst dann zum Anbieter eines (modifizierten) GPAI-Modells, wenn die Modifikation mehr als **⅓ der
  ursprünglichen Trainingsrechenleistung** einsetzt (Leitlinien).
- Wer ein KI-**System** auf GPAI-Basis baut und in Verkehr bringt, ist **Anbieter dieses Systems** (Art. 3 Nr. 3)
  → Art. 4, Art. 50 Abs. 1/2, ggf. Hochrisiko-Prüfung. Das AI Office ist seit Omnibus auch für solche
  Systeme zuständig, wenn Modell- und Systemanbieter dasselbe Unternehmen sind.

---

## 11. Rollenwechsel und Grenzfälle (Art. 25, Art. 3 Nr. 3)

**Art. 25 Abs. 1 – gilt nur für Hochrisiko-Systeme.** Händler, Einführer, Betreiber oder Dritte werden
Anbieter, wenn sie
- (a) ihren **Namen/ihre Marke** auf ein bereits in Verkehr gebrachtes Hochrisiko-System setzen,
- (b) eine **wesentliche Veränderung** vornehmen, die es Hochrisiko bleiben lässt,
- (c) die **Zweckbestimmung** so ändern, dass es Hochrisiko wird.
Der ursprüngliche Anbieter muss dann kooperieren (Abs. 2).

**Außerhalb Hochrisiko:** Kein Rollenwechsel nach Art. 25. Aber: Wer ein KI-System (auch mit fremdem
Modell) entwickeln lässt und **unter eigenem Namen in Verkehr bringt**, ist originär Anbieter nach Art. 3
Nr. 3 – mit den Pflichten der jeweiligen Risikoklasse (bei Chatbot: Art. 50 Abs. 1, Art. 4).

**Typische Fälle:**

| Fall | Rolle | Pflichten |
|---|---|---|
| ChatGPT/Copilot intern nutzen | Betreiber | Art. 4; DSGVO |
| Fremden Chatbot auf Website einbinden (Anbieter-Branding sichtbar) | Betreiber | Art. 4; sicherstellen, dass KI-Hinweis sichtbar bleibt |
| Eigene Kunden-App mit GPT-API, eigener Name | **Anbieter** eines KI-Systems (nicht Hochrisiko) | Art. 4, Art. 50 Abs. 1 (+ Abs. 2 bei generierten Inhalten), Dokumentation eigener Prüfung |
| HR-Tool eines Anbieters nutzen | Betreiber Hochrisiko (ab 12/2027) | Art. 26; Anbieter-Einstufung abfragen |
| HR-Tool unter eigenem Namen weiterverkaufen (White Label) | **Anbieter** (Art. 25 Abs. 1 a) | Vollständige Anbieterpflichten |
| GPT fine-tunen mit kleinen Datensätzen | kein GPAI-Anbieter | – |

---

## 12. Sanktionen (Art. 99–101 KI-VO, §§ 15–17 KI-MIG)

**Anwendbar seit 02.08.2025** (Art. 113 b), Art. 101 (GPAI-Bußgelder der Kommission) seit 02.08.2026.
In Deutschland praktisch durchsetzbar seit Behördenbenennung durch das KI-MIG (29.07.2026).

| Stufe | Verstoß | Obergrenze Unternehmen | **KMU/Start-up/SMC: niedrigerer Wert** (Art. 99 Abs. 6) |
|---|---|---|---|
| Abs. 3 | Verbote Art. 5 | 35 Mio. € **oder** 7 % Weltjahresumsatz (höherer Wert) | der niedrigere der beiden Werte |
| Abs. 4 | Pflichten von Anbietern (Art. 16), Bevollmächtigten, Einführern, Händlern, **Betreibern (Art. 26)**, notifizierten Stellen, **Transparenz (Art. 50)** | 15 Mio. € oder 3 % | der niedrigere Wert |
| Abs. 5 | Falsche/unvollständige/irreführende Angaben gegenüber Behörden | 7,5 Mio. € oder 1 % | der niedrigere Wert |

**Es gibt keine Stufe „10 Mio. € / 2 %".** Art. 4 (KI-Kompetenz) ist in Art. 99 **nicht** als
Bußgeldtatbestand gelistet. Art. 27 (FRIA) und Art. 86 ebenfalls nicht → dafür nationales Bußgeld
**§ 15 KI-MIG bis 50.000 €** (auch für fehlende Mitwirkung/Information gegenüber Behörden, Art. 21, 45).
**§ 17 Abs. 2 KI-MIG:** keine Geldbußen gegen Behörden und öffentliche Stellen (§ 2 Abs. 1/2 BDSG).

**Beispielrechnung KMU, 2 Mio. € Umsatz, Verstoß gegen Art. 50:** 3 % = 60.000 € < 15 Mio. € → Obergrenze
60.000 €. Bemessung nach Art. 99 Abs. 7 (Art, Schwere, Dauer, Kooperation, Größe, frühere Verstöße).

**Weitere Risiken jenseits der KI-VO:** DSGVO-Bußgelder (Art. 83), UWG-Abmahnungen bei irreführender
KI-Werbung, Haftung nach BGB/ProdHaftG (KI-Haftungsrichtlinie wurde 2025 zurückgezogen), arbeitsrechtliche
Folgen bei Verletzung von § 87 BetrVG.

---

## 13. Governance in Deutschland (KI-MIG)

| § | Regelung |
|---|---|
| 2 | **Bundesnetzagentur** = zentrale Marktüberwachungsbehörde, soweit nichts anderes bestimmt. **BaFin** für KI in regulierten Finanztätigkeiten. Produkt-Marktüberwachungsbehörden für Anhang-I-Produkte. **Landesbehörden** für KI-Systeme öffentlicher Stellen der Länder und für Mediendienstanbieter (Landesmedienanstalten). |
| 4 | KI-Marktüberwachungskammer (Bund-Länder-Koordination) |
| 5 | **Koordinierungs- und Kompetenzzentrum (KoKIVO)** bei der BNetzA: Sachverständige, horizontale Rechtsfragen, Verhaltenskodizes, Zivilgesellschaft, **Schulungs- und Sensibilisierungsangebote** |
| 6 | Zentrale Anlaufstelle |
| 8 | **Zentrale Beschwerdestelle** (Art. 85 KI-VO) bei der BNetzA |
| 9 | Zusammenarbeit, Einbindung der Datenschutzbehörden |
| 13 | **KI-Reallabor** bei der BNetzA; Vorrang für KMU/Start-ups (Art. 62) und Forschung; Antragsverfahren Stand 11/2026 noch nicht veröffentlicht |
| 15–17 | Nationale Bußgelder (s. o.) |
| 20 | Nationales Register über Hochrisiko-KI-Systeme |

**BNetzA KI-Service-Desk** (seit 03.07.2025): Einstiegsseite `/DE/Fachthemen/Digitales/KI/start_ki.html`,
**KI-Compliance-Kompass** (interaktive Relevanzprüfung), FAQ, Factsheet „KI-Verordnung – Fokus KMU und
Start-ups", Kontaktformular, Beschwerdestelle. Die frühere URL `…/KI/start.html` ist tot (404).

**EU-Ebene:** AI Office (Kommission) für GPAI und GPAI-basierte Systeme desselben Anbieters; AI Board;
AI Act Service Desk (ai-act-service-desk.ec.europa.eu) mit Artikel-Explorer und Compliance-Checker.

---

## 14. Schnittstellen: DSGVO, Arbeitsrecht, Urheberrecht

**DSGVO** gilt parallel und unabhängig von der Risikoklasse:
- Rechtsgrundlage für jede Verarbeitung personenbezogener Daten in KI-Tools; **AVV (Art. 28 DSGVO)** mit dem
  KI-Anbieter, Drittlandtransfer prüfen (Data Privacy Framework, SCC).
- DSFA (Art. 35 DSGVO) bei hohem Risiko – Art. 26 Abs. 9 KI-VO verweist darauf.
- Art. 22 DSGVO: automatisierte Einzelentscheidungen; Auskunft (Art. 15) und Art. 86 KI-VO greifen ineinander.
- **DSK-Orientierungshilfen:** „KI und Datenschutz" (06.05.2024, Anwender), „KI-Systeme" für Entwickler/
  Hersteller (17.06.2025), RAG-Systeme (10/2025); LfDI BW Navigator ONKIDA.
- Faustregel Richtlinie: keine Kundendaten, Gesundheitsdaten, Geschäftsgeheimnisse in Tools ohne AVV und
  Datenschutz-Konfiguration (Trainingsopt-out/Enterprise-Tarife).

**Arbeitsrecht:**
- Art. 26 Abs. 7 KI-VO: Information von Beschäftigten und Vertretung **vor** Inbetriebnahme eines Hochrisiko-
  Systems (Informationspflicht, kein Mitbestimmungsrecht aus der KI-VO).
- **§ 87 Abs. 1 Nr. 6 BetrVG**: technische Einrichtungen zur Verhaltens-/Leistungskontrolle → echte
  Mitbestimmung, gilt für weit mehr KI-Tools als nur Hochrisiko; § 80 Abs. 3 BetrVG: Sachverständige bei KI;
  § 90 BetrVG. Bitkom-Leitfaden „KI und Mitbestimmung" (02/2026) mit Eckpfeilern einer Betriebsvereinbarung.
- Emotionserkennung am Arbeitsplatz ist verboten (Art. 5 Abs. 1 f), außer medizinisch/Sicherheit.

**Urheberrecht/UWG:** reine KI-Outputs sind nicht urheberrechtlich geschützt, können aber fremde Rechte
verletzen; irreführende KI-Bilder in der Werbung sind abmahnfähig (eRecht24-Checkliste).

---

## 15. Was das Gesetz NICHT fordert (verifiziert)

| Mythos | Richtig ist | Fundstelle |
|---|---|---|
| „Wir brauchen einen KI-Beauftragten." | Keine Pflicht. Sinnvoll: eine verantwortliche Ansprechperson | Art. 4, Art. 26 – keine Rollenpflicht |
| „Mitarbeiter brauchen ein KI-Zertifikat." | Kein Zertifikat, kein Format, kein Stundenumfang, kein garantiertes Niveau | Art. 4 n. F.; Kommission Q&A 07.05.2025 |
| „Jeder KI-Text muss gekennzeichnet werden." | Nur Deepfakes und Texte öffentlichen Interesses ohne redaktionelle Kontrolle (Betreiber); maschinenlesbare Kennzeichnung ist Anbieterpflicht | Art. 50 Abs. 2, 4 |
| „Wir müssen eine Grundrechte-Folgenabschätzung machen." | Nur öffentliche Stellen, Erbringer öffentlicher Dienste, Kreditwürdigkeit, Lebens-/Krankenversicherung | Art. 27 Abs. 1 |
| „Wir müssen unsere KI-Tools registrieren." | Registrierung nur durch Anbieter (und Behörden als Betreiber) | Art. 49, 71 |
| „Wir brauchen eine Genehmigung, bevor wir KI einsetzen." | Keine Vorab-Genehmigung; Eigenverantwortung + Marktüberwachung | Kap. III, IX |
| „Hochrisiko-Pflichten gelten seit August 2026." | Anhang III ab 02.12.2027, Anhang I ab 02.08.2028 | Art. 113 n. F. (Omnibus) |
| „ChatGPT ist im Unternehmen verboten / Hochrisiko." | Minimales Risiko; Art. 4 und DSGVO beachten | Art. 6, Anhang III |
| „Bußgelder treffen KMU mit dem höheren Betrag." | KMU/Start-ups/SMC: **niedrigerer** Betrag | Art. 99 Abs. 6 |
| „Die KI-VO verlangt eine Betriebsvereinbarung." | KI-VO: nur Information (Art. 26 Abs. 7, Hochrisiko). Mitbestimmung folgt aus BetrVG | Art. 26 Abs. 7; § 87 BetrVG |
| „Verhaltenskodizes sind Pflicht." | Freiwillig | Art. 95 |
| „Wir müssen Protokolle 10 Jahre aufheben." | Betreiber: mind. 6 Monate; 10 Jahre gilt für Anbieter-Dokumentation | Art. 26 Abs. 6; Art. 18 |

---

## 16. Offene Punkte / Unsicherheiten (Stand 09.11.2026)

- Kommissions-Leitlinien zur Hochrisiko-Einstufung (Art. 6): weiterhin nur Entwurf (05/2026).
- Harmonisierte Normen: nur EN 18286 (QM, Art. 17) im Amtsblatt (19.10.2026); übrige Normen ausstehend.
- EU-Datenbank (Art. 71): Live-Betriebsstatus nicht verifiziert.
- Leitlinien zur Meldung schwerwiegender Vorfälle (Art. 73): nur Entwurf (09/2025) bekannt.
- Deutsches KI-Reallabor (§ 13 KI-MIG): Antragsverfahren nicht veröffentlicht; Frist 02.08.2027.
- Mittelstand-Digital: altes Netzwerk endet 31.12.2026; neues Netzwerk ab 01.01.2027 mit sechs überregionalen
  Zentren (je 2–3 Länder, mindestens eine Anlaufstelle pro Land), ab Mai 2027 elf Branchen- und Themenzentren
  (BMWE-Pressemitteilung 20.10.2026). Zuständiges Zentrum vor dem Workshop auf mittelstand-digital.de prüfen.
- Verfügbarkeit „Elements of AI" (deutsch) über KI-Campus nicht tagesaktuell bestätigt.
- Exakte Bußgeldpraxis der BNetzA: noch keine veröffentlichten Verfahren.

---

## 17. Quellen
Vollständiges, kategorisiertes Verzeichnis mit Stand-Angaben: **`src.txt`**. Zentrale Primärquellen:
- KI-VO konsolidiert (DE): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689 · artikelweise https://ai-act-law.eu/de/
- Digital Omnibus VO (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- KI-MIG: https://www.gesetze-im-internet.de/ki-mig/
- BNetzA KI-Service-Desk: https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/start_ki.html
- eRecht24 KI-Rubrik: https://www.e-recht24.de/ki/
