# Vorlage 02 – Rollen- und Risiko-Check (pro KI-System)

| | |
|---|---|
| **Zweck** | Für jedes System aus dem KI-Inventar (Vorlage 01) die eigene Rolle und die Risikostufe nach der KI-VO bestimmen und die Einschätzung dokumentieren. |
| **Rechtsgrundlage** | Art. 3 Nr. 3/4 (Rollen), Art. 25 (Rollenwechsel bei Hochrisiko), Art. 5 (Verbote), Art. 6 + Anhang I/III (Hochrisiko), Art. 6 Abs. 3 (Ausnahmen), Art. 50 (Transparenz) |
| **Wer füllt aus** | Ansprechperson KI zusammen mit dem Fachbereich, der das Tool nutzt |
| **Aufwand** | 15–20 Minuten pro System |
| **Hilfsmittel** | BNetzA KI-Compliance-Kompass: https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/2_Risiko/kompass/start.html |

*Ausfüllhinweis: Ehrlich und konkret antworten. Die Einstufung eines fremden Tools trifft rechtlich der
Anbieter – fragt sie ab (Vorlage 06) und haltet hier fest, ob ihr sie plausibel findet.*

---

**System:** [Name] · **Inventar-Nr.:** [__] · **Datum:** [__.__.____] · **Bearbeitet von:** [Name]

## Teil A – Ist es überhaupt ein KI-System? (Art. 3 Nr. 1)

| Frage | ja | nein |
|---|---|---|
| Leitet das System aus Eingaben selbst ab, wie es Ausgaben (Text, Bild, Bewertung, Empfehlung, Entscheidung) erzeugt – statt nur feste, von Menschen programmierte Regeln/Formeln abzuarbeiten? | ☐ | ☐ |
| Enthält es ein trainiertes Modell (Sprachmodell, Bildmodell, Scoring-Modell, maschinelles Lernen)? | ☐ | ☐ |

→ Beide „nein" (z. B. Excel-Formeln, klassisches Regelwerk, feste Sortierlogik): **kein KI-System**, Check beenden.
*(Kommissions-Leitlinien zur Definition, 06.02.2025)*

## Teil B – Unsere Rolle

| Frage | ja | nein |
|---|---|---|
| B1 Haben wir das System selbst entwickelt oder entwickeln lassen **und** stellen es unter unserem Namen/unserer Marke Dritten bereit (Kunden, Öffentlichkeit)? | ☐ | ☐ |
| B2 Haben wir ein fremdes Modell (z. B. GPT, Gemini, Claude per API) in eine eigene Anwendung eingebaut, die wir Dritten anbieten? | ☐ | ☐ |
| B3 Vertreiben wir ein fremdes **Hochrisiko**-System unter unserem Namen (White Label)? | ☐ | ☐ |
| B4 Haben wir ein fremdes **Hochrisiko**-System wesentlich verändert oder seinen Zweck so geändert, dass es Hochrisiko wird? | ☐ | ☐ |
| B5 Nutzen wir das System nur intern oder für unsere Kunden, ohne es als Produkt weiterzugeben? | ☐ | ☐ |

**Ergebnis Rolle:**
☐ **Betreiber** (nur B5 „ja") – Normalfall
☐ **Anbieter** (B1, B2, B3 oder B4 „ja") – Anbieterpflichten der jeweiligen Risikostufe (bei B2 und Nicht-Hochrisiko: Art. 4, Art. 50 Abs. 1/2)
☐ **Beides**

*Hinweis: Fine-Tuning eines Basismodells macht euch nur dann zum Anbieter des Modells, wenn ihr mehr als ein Drittel
der ursprünglichen Trainingsrechenleistung einsetzt (GPAI-Leitlinien der Kommission). Prompting, RAG, Systemprompts: nein.*

## Teil C – Verbots-Check (Art. 5, seit 02.02.2025)

Macht das System eines der Folgenden? (Alle Merkmale eines Verbots müssen kumulativ vorliegen.)

| # | Verbot | trifft zu | trifft nicht zu |
|---|---|---|---|
| 1 | Unterschwellige oder manipulative Beeinflussung mit erheblichem Schaden | ☐ | ☐ |
| 2 | Ausnutzung von Alter, Behinderung, sozialer/wirtschaftlicher Lage | ☐ | ☐ |
| 3 | Social Scoring (Bewertung nach Sozialverhalten mit Benachteiligung in anderem Kontext) | ☐ | ☐ |
| 4 | Vorhersage von Straftaten allein aufgrund Profiling/Persönlichkeitsmerkmalen | ☐ | ☐ |
| 5 | Ungezieltes Sammeln von Gesichtsbildern aus Internet/Video für Datenbanken | ☐ | ☐ |
| 6 | **Emotionserkennung am Arbeitsplatz oder in Bildungseinrichtungen** (außer medizinisch/Sicherheit) | ☐ | ☐ |
| 7 | Biometrische Kategorisierung nach Ethnie, Religion, Sexualität, politischer Meinung | ☐ | ☐ |
| 8 | Biometrische Echtzeit-Fernidentifizierung im öffentlichen Raum **zur Strafverfolgung** | ☐ | ☐ |
| 9 | Erzeugung von Missbrauchsdarstellungen von Kindern oder nicht-einvernehmlichen Intimbildern (neu 2026) | ☐ | ☐ |

→ Ein „trifft zu": **Einsatz sofort stoppen**, rechtlich prüfen lassen.

## Teil D – Hochrisiko-Check (Art. 6, Anhang I / III)

**D1 Anhang I – Produkt:** Ist das KI-System Teil eines Produkts mit EU-Sicherheitsrecht und Drittprüfung
(Maschine, Medizinprodukt, Spielzeug, Aufzug, Funkanlage, Fahrzeug …)? ☐ ja → Hochrisiko Anhang I (Pflichten ab 02.08.2028) ☐ nein

**D2 Anhang III – Einsatzbereich:** Wird das System eingesetzt für …

| Nr. | Bereich | ja | nein |
|---|---|---|---|
| 1 | Biometrische Identifizierung/Kategorisierung/Emotionserkennung (nicht: reine 1:1-Verifizierung wie Handy-Entsperren) | ☐ | ☐ |
| 2 | Sicherheitskomponente kritischer Infrastruktur (Strom, Wasser, Verkehr, digitale Infrastruktur) | ☐ | ☐ |
| 3 | **Bildung**: Zulassung, Bewertung von Lernergebnissen, Niveaubestimmung, Prüfungsaufsicht | ☐ | ☐ |
| 4 | **Beschäftigung**: Stellenanzeigen zielgerichtet ausspielen, Bewerbungen sichten/filtern/bewerten, Beförderung/Kündigung, Aufgabenzuweisung nach Verhalten, Leistungs-/Verhaltensbewertung | ☐ | ☐ |
| 5 | Sozialleistungen (Behörden), **Kreditwürdigkeit** natürlicher Personen (nicht Betrugserkennung), **Lebens-/Krankenversicherung** (Risiko/Preis), Notfall-Triage | ☐ | ☐ |
| 6–8 | Strafverfolgung, Migration/Grenze, Justiz/Wahlen | ☐ | ☐ |

**D3 Ausnahme Art. 6 Abs. 3** (nur bei „ja" in D2 prüfen): Das System …

| | ja | nein |
|---|---|---|
| erledigt nur eine enge Verfahrensaufgabe (z. B. Daten strukturieren, Dokumente klassifizieren) | ☐ | ☐ |
| verbessert nur das Ergebnis einer bereits abgeschlossenen menschlichen Tätigkeit (z. B. Sprachglättung) | ☐ | ☐ |
| erkennt Muster/Abweichungen, ohne die menschliche Bewertung ohne Prüfung zu ersetzen | ☐ | ☐ |
| übernimmt nur eine vorbereitende Aufgabe für eine menschliche Bewertung | ☐ | ☐ |
| **Rückausnahme:** Erstellt es ein Profil natürlicher Personen (z. B. Ranking, Score, Persönlichkeitsprofil)? Dann **immer Hochrisiko**. | ☐ | ☐ |

**Ergebnis Hochrisiko:** ☐ nein ☐ ja, Anhang III (Betreiberpflichten Art. 26 ab 02.12.2027) ☐ ja, Anhang I (ab 02.08.2028) ☐ unklar → Anbieter fragen (Vorlage 06)

*Die Einstufung nach Art. 6 Abs. 3 trifft und dokumentiert der Anbieter (Art. 6 Abs. 4). Kommissions-Leitlinien liegen
Stand 11/2026 weiterhin nur als Entwurf vor.*

## Teil E – Transparenz-Check (Art. 50, seit 02.08.2026)

| Frage | ja | nein | Maßnahme |
|---|---|---|---|
| Interagieren Kunden/Bürger/Beschäftigte direkt mit dem System (Chat, Sprache)? | ☐ | ☐ | KI-Hinweis sichtbar (Vorlage 05, Baustein A) |
| Erzeugt es Bilder/Audio/Video, die reale Personen, Orte oder Ereignisse **täuschend echt** nachahmen? | ☐ | ☐ | Deepfake-Label (Vorlage 05, Baustein C) |
| Veröffentlichen wir damit Texte, die die Öffentlichkeit über Angelegenheiten von öffentlichem Interesse informieren, **ohne** redaktionelle Prüfung? | ☐ | ☐ | KI-Hinweis oder redaktionelle Freigabe dokumentieren (Baustein D/E) |
| Erkennt es Emotionen oder kategorisiert Personen biometrisch (nur in erlaubten Fällen)? | ☐ | ☐ | Betroffene informieren (Baustein F) |
| Sind wir **Anbieter** eines generativen Systems? | ☐ | ☐ | Maschinenlesbare Kennzeichnung (Art. 50 Abs. 2) sicherstellen |

## Ergebnis und Freigabe

**Rolle:** [Betreiber / Anbieter / beides]
**Risikostufe:** [verboten / hoch (Anhang I/III) / Transparenz / minimal]
**Begründung (2–3 Sätze):** [__________________________________________]
**Offene Punkte / Anbieter-Rückfragen:** [__________________________________________]
**Nächste Schritte:** [__________________________________________]
**Wiedervorlage:** [Datum] (spätestens bei Funktionsänderung des Tools)

Datum, Unterschrift: ____________________

---
*Vorlage aus dem Workshop „EU AI Act für kleine Organisationen" (PINGEL AI Solutions), Stand 11/2026, CC BY 4.0.
Kein Rechtsrat – bei „hoch" oder „Anbieter" juristisch prüfen lassen.*
