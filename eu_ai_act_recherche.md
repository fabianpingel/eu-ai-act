# EU AI Act – Vollständige Recherche (Stand: März 2026)

Quellen: artificialintelligenceact.eu, bundesregierung.de, bundesnetzagentur.de (KI-Service Desk),
ihk.de/hannover, e-recht24.de, eur-lex.europa.eu (Verordnung 2024/1689)

---

## 1. ÜBERBLICK UND RECHTLICHE GRUNDLAGE

- **Vollständiger Name:** Verordnung (EU) 2024/1689 – KI-Verordnung (AI Act)
- **Verabschiedung:** 21. Mai 2024 (EU-Mitgliedstaaten), veröffentlicht 12. Juli 2024
- **Rechtsgrundlage:** Artikel 114 AEUV (Binnenmarkt) + Artikel 16 AEUV (Datenschutz bei biometrischen Systemen)
- **Charakter:** Weltweit erstes umfassendes Regelwerk für Künstliche Intelligenz
- **Geltungsbereich:** Gilt nicht nach Unternehmensstandort, sondern danach, ob ein KI-System in der EU in Verkehr gebracht wird oder Auswirkungen auf EU-Bürger hat
- **Ausnahmen:** Private Nutzer, reine Forschungs-/Entwicklungssysteme, militärische/Verteidigungssysteme

---

## 2. DEFINITIONEN (Artikel 3 KI-Verordnung)

### KI-System
"Maschinengestütztes System, das für einen in unterschiedlichem Grade autonomen Betrieb ausgelegt ist" und anpassungsfähig sein kann, um Ausgaben wie Vorhersagen oder Entscheidungen zu treffen.

**Sieben Kernelemente:**
1. Maschinengestützt
2. Autonomiegrade (explizit oder implizit)
3. Anpassungsfähigkeit
4. Explizite/implizite Ziele
5. Ableiten von Eingabedaten
6. Ausgaben (Vorhersagen, Empfehlungen, Entscheidungen, Inhalte)
7. Interaktion mit physischer/digitaler Umgebung

### Akteure der Wertschöpfungskette

| Begriff | Artikel | Definition |
|---------|---------|-----------|
| **Anbieter (Provider)** | Art. 3(3) | Entwickelt KI-Systeme und bringt sie unter eigenem Namen in Verkehr oder nimmt sie in Betrieb |
| **Betreiber (Operator/User)** | Art. 3(4) | Nutzt KI-System in eigener Verantwortung (außer privatem Gebrauch) |
| **Bevollmächtigter** | Art. 3(5) | Von Anbieter schriftlich beauftragt, Pflichten in der Union zu erfüllen |
| **Einführer** | Art. 3(6) | Bringt KI-System aus Drittland in EU-Verkehr |
| **Händler** | Art. 3(7) | Stellt KI-System auf Unionsmarkt bereit (außer Anbieter/Einführer) |
| **Nachgelagerter Anbieter** | Art. 3(68) | Integriert KI-Modelle in eigene Systeme, unabhängig von Bezugsquelle |
| **GPAI-Modell** | Art. 3(63) | KI-Modell mit erheblicher allgemeiner Verwendbarkeit, das breites Spektrum unterschiedlicher Aufgaben kompetent erfüllen kann |

### Weitere wichtige Definitionen

| Begriff | Artikel | Definition |
|---------|---------|-----------|
| **Risiko** | Art. 3(2) | Kombination aus Schadenswahrscheinlichkeit und Schwere |
| **Inverkehrbringen** | Art. 3(9) | Erstmalige Bereitstellung auf EU-Markt |
| **Zweckbestimmung** | Art. 3(12) | Vorgesehene Verwendung laut Anbieterangaben |
| **Sicherheitsbauteil** | Art. 3(14) | Komponente, deren Ausfall Gesundheit/Sicherheit gefährdet |
| **Wesentliche Veränderung** | Art. 3(23) | Nachträgliche Änderung, nicht in ursprünglicher Bewertung vorgesehen |
| **Trainingsdaten** | Art. 3(29) | Daten zum Anpassen lernbarer Parameter |
| **Validierungsdaten** | Art. 3(30) | Zur Evaluation und Parametereinstellung |
| **Testdaten** | Art. 3(32) | Unabhängige Bewertung vor Inverkehrbringen |

### Biometrische Systeme

| Begriff | Artikel | Definition |
|---------|---------|-----------|
| **Biometrische Daten** | Art. 3(34) | Technisch gewonnene personenbezogene Daten zu physischen/physiologischen Merkmalen |
| **Biometrische Identifizierung** | Art. 3(35) | Automatisierte Feststellung der Identität durch Datenbankabgleich |
| **Biometrische Verifizierung** | Art. 3(36) | Eins-zu-eins-Abgleich zur Authentifizierung |
| **Emotionserkennung** | Art. 3(39) | System zur Feststellung von Emotionen aus biometrischen Daten |
| **Fernidentifizierung** | Art. 3(41) | Identifizierung ohne aktive Einbeziehung der Person |
| **Echtzeit-Fernidentifizierung (RBI)** | Art. 3(42) | Erfassung und Abgleich ohne erhebliche Verzögerung |

---

## 3. RISIKOBASIERTER ANSATZ – DIE VIER RISIKOSTUFEN

Grundprinzip: "Je höher das Risiko bei der Anwendung eingeschätzt wird, desto strenger sind auch die Vorgaben."

---

### Stufe 1: INAKZEPTABLES RISIKO – Verbotene Praktiken (Artikel 5)

**Gültig seit:** 2. Februar 2025

Systeme, die "gegen EU-Grundrechte verstoßen oder eine deutliche Bedrohung für die Sicherheit und Gesundheit darstellen."

**Wichtig:** Alle aufgeführten Bedingungen einer Verbotsnorm müssen gleichzeitig erfüllt sein (Alles-oder-Nichts-Prinzip).

#### Die 8 verbotenen Praktiken (Art. 5 Abs. 1):

| # | Praktik | Kernpunkt | Beispiel |
|---|---------|-----------|---------|
| (a) | **Schädliche Manipulation** | Unterschwellige/manipulative Techniken mit Verhaltensbeeinflussung und erheblichem Schaden | Chatbots, die zu Selbstverletzung anraten |
| (b) | **Ausnutzung von Vulnerabilität** | Ausnutzung von Alter, Behinderung oder wirtschaftlicher Situation | KI-Spielzeug, das Kinder zu Risiken verleitet |
| (c) | **Social Scoring** | Bewertung basierend auf Sozialverhalten mit ungerechtfertigter Benachteiligung | Fraud-Scoring mit ethnischen Merkmalen |
| (d) | **Straftat-Vorhersage** | Risikobewertung ausschließlich durch Profiling ohne objektive Fakten | Polizei nutzt nur biometrische Daten |
| (e) | **Ungezieltes Gesichtsauslesen** | Web-Scraping für Gesichtserkennungsdatenbanken | Milliarden Bilder von Social Media extrahieren |
| (f) | **Emotionsableitung am Arbeitsplatz/Bildung** | Emotionserkennung in Beschäftigung oder Bildung | Webcam-Monitoring von Beschäftigten |
| (g) | **Biometrische Kategorisierung** | Kategorisierung nach Ethnie, Sexualität, Religion via Biometrie | Social-Media-Ads basierend auf Orientierung |
| (h) | **Echtzeit-Fernidentifizierung (RBI)** | RBI-Systeme in öffentlichen Räumen zur Strafverfolgung | Polizeikameras mit Gesichtserkennung |

#### Ausnahmen zu Verbot (h) – Echtzeit-RBI:
Ausnahmsweise erlaubt für:
- Suche nach Opfern (Entführung, Menschenhandel, Ausbeutung, Vermisste)
- Abwehr konkreter, erheblicher Gefahr / Terroranschläge
- Fahndung nach Verdächtigen bestimmter Straftaten (Anhang II)
- **Voraussetzung:** Nationale Rechtsgrundlage mit Schutzmaßnahmen (Art. 5 Abs. 2–7)

**Orientierungshilfe:** EU-Kommission veröffentlichte am 4. Februar 2025 unverbindliche Leitlinien mit rechtlichen Erläuterungen und praktischen Beispielen.

---

### Stufe 2: HOHES RISIKO – Hochrisiko-KI-Systeme (Artikel 6–15, Anhang I und III)

**Anwendung:** Ab 2. August 2026 (Anhang III) bzw. 2. August 2027 (Anhang I)

#### Definition: Wann ist ein System Hochrisiko?

**Kategorie A – Anhang I (Regulierte Produkte):**
Das System ist selbst ein Produkt unter EU-Rechtsvorschriften oder fungiert als Sicherheitsbauteil UND eine Konformitätsbewertung durch Dritte vor Markteinführung ist erforderlich.

**Kategorie B – Anhang III (8 sensible Anwendungsbereiche):**
1. Biometrie (außer Verifikation)
2. Kritische Infrastruktur
3. Bildung und Berufsausbildung
4. Beschäftigung und Personalmanagement
5. Öffentliche Dienste und Sozialleistungen
6. Strafverfolgung
7. Migration, Asyl, Grenzkontrolle
8. Rechtspflege und demokratische Prozesse

#### Ausnahmen von der Hochrisiko-Einstufung (innerhalb Anhang III):
Ein System fällt NICHT unter Hochrisiko, wenn es:
- Eine "enge verfahrenstechnische Aufgabe" erfüllt
- Nur menschliche Ergebnisse verbessert (ohne Entscheidung zu ersetzen)
- Muster aufdeckt ohne eigenständige Entscheidungen zu treffen
- Vorbereitende Aufgaben übernimmt

**Ausnahme der Ausnahme:** Profiling natürlicher Personen bleibt immer hochriskant.

**Praxishinweis:** HR-Tools zur Kandidatenauswahl oder Leistungsbewertung zählen häufig als Hochrisiko-Systeme. Eine menschliche Kontrollinstanz ohne Alleinentscheidungsbefugnis kann die Klassifizierung senken.

#### Pflichten für Anbieter von Hochrisiko-KI (Art. 8–15):

| Anforderung | Artikel | Inhalt |
|-------------|---------|--------|
| **Risikomanagementsystem** | Art. 9 | Kontinuierlicher iterativer Prozess über gesamten Lebenszyklus |
| **Datenqualität** | Art. 10 | Trainings-, Validierungs- und Testdatensätze nach spezifizierten Kriterien |
| **Technische Dokumentation** | Art. 11 | Vor Inverkehrbringen; Nachweis der Anforderungserfüllung |
| **Protokollierung (Logs)** | Art. 12 | Automatische Aufzeichnung von Ereignissen zur Rückverfolgbarkeit |
| **Transparenz/Betriebsanleitung** | Art. 13 | Interpretierbarkeit der Ausgaben; Nutzerinformation |
| **Menschliche Aufsicht** | Art. 14 | Wirksame menschliche Beaufsichtigung ermöglichen |
| **Genauigkeit & Robustheit** | Art. 15 | Zuverlässiger Betrieb; Widerstand gegen Fehler und Manipulationen |
| **EU-Datenbankregistrierung** | Art. 71 | Registrierung in der EU-Datenbank vor Inverkehrbringen |
| **Konformitätsbewertung** | Art. 43 | Prüfverfahren; CE-Kennzeichnung |
| **Post-Markt-Überwachung** | Art. 72 | Überwachungssystem für Leistungsdaten während gesamter Lebensdauer |
| **Vorfallmeldung** | Art. 73 | Meldung schwerwiegender Vorfälle an Marktüberwachungsbehörden |
| **Aufbewahrungspflicht** | — | Protokolle und Dokumentation: 10 Jahre |

#### Pflichten für Betreiber von Hochrisiko-KI:
- KI-System gemäß Herstelleranweisungen verwenden
- Betriebsaufzeichnungen führen
- Folgenabschätzungen für bestimmte Hochrisiko-Systeme durchführen
- Menschliche Aufsicht gewährleisten
- Schwerwiegende Vorfälle an zuständige Behörden melden

---

### Stufe 3: BEGRENZTES RISIKO – Transparenzpflichten (Artikel 50)

**Anwendung:** Ab 2. August 2026

#### Betroffene Systeme:

**1. Direkte Mensch-Maschine-Interaktion (z.B. Chatbots):**
- Nutzer müssen informiert werden, dass sie mit einem KI-System interagieren
- Ausnahme: Wenn aus dem Kontext ersichtlich, dass es sich um ein KI-System handelt

**2. Systeme für synthetische Inhalte (Text, Video, Audio, Bild / Deepfakes):**
- Kennzeichnung in maschinenlesbarem Format erforderlich
- Inhalte müssen als künstlich erzeugt oder manipuliert erkennbar sein
- Technische Lösung muss "wirksam, interoperabel, belastbar und zuverlässig" sein
- Offenlegungspflicht für Deepfakes und KI-generierte Inhalte

**3. Emotionserkennung & biometrische Kategorisierung:**
- Betroffene Personen müssen über Betrieb informiert werden

**4. KI-generierte Texte zu öffentlichen Angelegenheiten:**
- Offenlegungspflicht für künstlich erzeugte/manipulierte Inhalte

#### Ausnahmen von Transparenzpflichten:
- Einsatz zur Strafverfolgung mit entsprechenden Schutzmaßnahmen
- Unterstützungsfunktionen ohne wesentliche Veränderung von Inhalten
- Künstlerische, kreative oder satirische Werke

**Beispiele für begrenztes Risiko:** Chatbots, Empfehlungsalgorithmen, Deepfake-Generatoren

---

### Stufe 4: MINIMALES/KEIN RISIKO

**Verpflichtungen:** Keine besonderen gesetzlichen Anforderungen

**Beispiele:** Spam-Filter, personalisierte Produktvorschläge, Computerspiele, KI-gestützte Übersetzungstools

**Empfehlung:** Freiwillige Verhaltenskodizes (Codes of Conduct) werden empfohlen.

---

## 4. GPAI-MODELLE – GENERAL PURPOSE AI (Artikel 51–56)

**Anwendung:** Ab 2. August 2025

### Definition (Art. 3 Nr. 63):
KI-Modelle mit "erheblicher allgemeiner Verwendbarkeit", die "ein breites Spektrum unterschiedlicher Aufgaben kompetent erfüllen" können. Typischerweise durch umfangreiches Training auf großen Datenmengen ohne spezifische Aufgabenvorgabe entwickelt. Typische Beispiele: Große Sprachmodelle (LLMs).

### Zwei Kategorien:

**1. Normale GPAI-Modelle (Art. 53):**
- Technische Dokumentation erstellen und aktualisieren (10 Jahre archivieren)
- Fähigkeiten, Grenzen und Trainingsdatenzusammenfassung offenlegen
- Urheberrechtsschutzstrategie implementieren (nur legale Inhalte crawlen)
- Nachgelagerte Anbieter informieren

**2. GPAI-Modelle mit systemischem Risiko (Art. 55):**
- Charakterisiert durch hohen Wirkungsgrad: trainiert mit mehr als 10²⁵ FLOPs
- Oder durch EU-Kommissionsentscheidung definiert
- Zusätzlich: Erweiterte Sicherheitsbewertungen, Cybersicherheitsmaßnahmen, Vorfallmeldung
- Safety & Security Framework erforderlich

### Anbieter-Definition für GPAI:
Anbieter ist, wer ein GPAI-Modell "entwickelt oder entwickeln lässt und es unter eigenem Namen oder Handelsmarke in Verkehr bringt". Nachgelagerte Modifizierer gelten nur als Anbieter bei "signifikanten Änderungen" (Rechenleistung >⅓ des ursprünglichen Trainings).

### Open-Source-Ausnahme:
GPAI-Modelle unter freien, quelloffenen Lizenzen sind von Dokumentations- und Bevollmächtigungspflichten befreit – **ausgenommen systemische Modelle**. Urheberrechts- und Veröffentlichungspflichten bleiben bestehen.

### Code of Practice (CoP):
Freiwilliger Standard (veröffentlicht Juli 2025) mit drei Kapiteln:
- Transparenz: Dokumentation und Informationsbereitstellung
- Urheberrecht: Compliance-Richtlinien beim Training
- Sicherheit & Gefahrenabwehr: Nur für Modelle mit systemischem Risiko

### Übergangsregelung:
GPAI-Modelle, die vor dem 2. August 2025 auf dem Markt waren, haben bis 2. August 2027 Zeit zur Compliance.

---

## 5. KI-KOMPETENZPFLICHT (Artikel 4)

**Gültig seit:** 2. Februar 2025

### Wer ist verpflichtet?
"Anbieter und Betreiber von KI-Systemen" – unabhängig von Branche oder Unternehmensgröße

### Kernpflicht:
Organisationen müssen sicherstellen, dass "ihr Personal und andere Personen, die in ihrem Auftrag mit dem Betrieb und der Nutzung von KI-Systemen befasst sind, über ein ausreichendes Maß an KI-Kompetenz verfügen."

### Betroffene Personengruppen:
- Eigenes Personal
- Auftragnehmer und Dienstleister
- Alle Personen mit Betriebsbefugnissen über KI-Systeme

### Definition KI-Kompetenz:
Umfasst "Fähigkeiten, Kenntnisse und Verständnis" für sachkundigen, verantwortungsvollen Einsatz mit Bewusstsein für Chancen und Risiken.

### Was ist NICHT vorgeschrieben:
- Formalisierte Standardtrainings
- Externe Zertifizierungen
- Einstellung eines KI-Beauftragten
- Regelmäßige behördliche Vorabprüfungen

### Was ist erforderlich:

**1. Bedarfsermittlung:**
- Welche Personen nutzen welche KI-Systeme?
- Welche Risiken sind damit verbunden?
- Welche Vorkenntnisse haben Mitarbeitende?

**2. Maßnahmengestaltung nach Kontext:**
Zu berücksichtigen:
- Individuelle Faktoren (Ausbildung, Erfahrung)
- Einsatzkontext und Risikostufe des Systems
- Organisationsrolle (Anbieter vs. Betreiber)
Format: Selbstlernprogramme, Workshops, Fortbildungen – intern oder extern möglich

**3. Kontinuierliche Auffrischung:**
- Regelmäßige Anpassung an technologische Entwicklungen
- Dynamischer, laufender Prozess

**4. Dokumentation (empfohlen):**
- Art der Maßnahmen
- Umfang (inhaltlich und zeitlich)
- Teilnehmende Personen

### Stufenkonzept für Schulungen:
- **Stufe 1:** Grundlagen von Daten und KI, allgemeine Chancen/Risiken
- **Stufe 2:** Organisationale Rolle, technische Aspekte, spezifische Risiken und rechtliche Einordnung
- **Stufe 3:** Rollenspezifische Trainings mit individuellen Schwerpunkten

### Konsequenzen bei Nichterfüllung:
Mangelnde KI-Kompetenz kann als Verletzung der Sorgfaltspflicht bewertet werden, besonders bei entstehenden Schäden.

### Kostenfreie Unterstützungsressourcen für KMU:
- **EU AI Office:** KI-Pakt, Webinare, Beispielsammlung
- **Mittelstand-Digital Zentren:** Rund 100 KI-Trainer für KMU bundesweit
- **Online-Kurse:** Elements of AI, KI-Campus, appliedAI Institute LMS
- **European Digital Innovation Hubs (EDIH):** Beratung für KMU

---

## 6. VOLLSTÄNDIGER ZEITPLAN – FRISTEN UND UMSETZUNGSPHASEN

| Datum | Regelungen |
|-------|-----------|
| **12. Juli 2024** | Veröffentlichung der KI-Verordnung im EU-Amtsblatt |
| **1. August 2024** | Inkrafttreten der Verordnung |
| **2. Februar 2025** | - KI-Kompetenzanforderungen (Art. 4) **[bereits aktiv]** |
| | - Verbotene Praktiken (Art. 5, 8 Verbote) **[bereits aktiv]** |
| **2. August 2025** | - GPAI-Modellvorschriften (Art. 51–56) |
| | - Nationale Behörden benennen |
| | - Notifizierungsbehörden einrichten |
| | - Zentrale Anlaufstelle benennen |
| **2. August 2026** | - Hochrisiko-KI-Systeme (Anhang III – 8 kritische Bereiche) |
| | - Transparenzpflichten (Art. 50) |
| | - KI-Reallabore (mindestens eines je Mitgliedstaat) |
| | - Sanktionsregeln |
| | - Kennzeichnungspflichten |
| **2. August 2027** | - Hochrisiko-KI-Systeme (Anhang I – regulierte Produkte) |
| | - GPAI-Modelle, die vor August 2025 auf dem Markt waren (Übergangsfrist) |
| **2. August 2030** | - Behördliche Hochrisiko-Systeme (Übergangsfrist) |
| **31. Dezember 2030** | - EU-IT-Großsysteme (Übergangsfrist) |

---

## 7. SANKTIONEN UND BUSSGELDER (Artikel 99)

| Verstoßart | Maximale Geldbuße |
|-----------|------------------|
| **Verbotene Praktiken (Art. 5)** | 35.000.000 € oder **7 % des weltweiten Jahresumsatzes** (höherer Wert gilt) |
| **Verstöße gegen Hochrisiko-Anforderungen** | 15.000.000 € oder **3 % des weltweiten Jahresumsatzes** |
| **Falsche/unvollständige Informationen gegenüber Behörden** | 7.500.000 € oder **1 % des weltweiten Jahresumsatzes** |
| **Dokumentations-/Transparenzverstöße** | Bis zu 10.000.000 € oder **2 % des Jahresumsatzes** |

**Hinweis:** Mehrere Quellen nennen "3 % des Jahresumsatzes" als allgemeinen Richtwert; der Gesetzestext der Verordnung 2024/1689 sieht gestaffelte Bußgelder bis 7 % vor.

**Wichtig für KMU:** Auch die Schulungspflicht (seit Februar 2025 aktiv) kann bereits jetzt zu Bußgeldern führen. Proaktive Vorbereitung minimiert Risiken.

---

## 8. ANBIETER vs. BETREIBER – UNTERSCHEIDUNG FÜR DIE PRAXIS

### KI-Anbieter (Provider)
**Wer gilt als Anbieter:**
- Natürliche Personen oder Organisationen, die KI-Systeme entwickeln
- Das System wird "unter eigenem Namen oder eigener Handelsmarke in Verkehr gebracht"
- Entgeltlichkeit spielt keine Rolle
- Unternehmenssitz in der EU ist nicht erforderlich, wenn das System dort vertrieben wird

**Achtung:** White-Label-Lösungen, die man anpasst und eigenständig vermarktet, machen das Unternehmen zum Anbieter.

**Umfangreichste Pflichten:** Technische Dokumentation, Risikomanagement, EU-Datenbankregistrierung, CE-Kennzeichnung, Post-Markt-Überwachung

### KI-Betreiber (Operator)
**Wer zählt als Betreiber:**
- Organisationen, die KI-Systeme "in eigener Verantwortung geschäftlich/beruflich verwenden"
- Interne Nutzung ohne Weiterentwicklung oder Marktfreigabe
- Beispiel: Chatbot im Kundensupport, HR-Tool zur Bewerberauswahl

**Geringere Pflichten:** Nutzung gemäß Herstelleranweisungen, Betriebsaufzeichnungen, menschliche Aufsicht, Vorfallmeldung

### Wechsel vom Betreiber zum Anbieter:
Ein Betreiber wird zum Anbieter, wenn er:
- Ein System modifiziert
- Es unter neuem Namen vertreibt
- Durch Anpassungen die Kriterien eines Hochrisiko-Systems erfüllt

---

## 9. PFLICHTEN IM ÜBERBLICK – NACH RISIKOSTUFE

### Für alle Unternehmen (ab 2. Februar 2025 – sofort!):
- **KI-Kompetenzpflicht:** Mitarbeitende, die mit KI arbeiten, müssen ausreichende Kenntnisse haben
- **Verbote einhalten:** Keine der 8 verbotenen Praktiken anwenden

### Für Betreiber mit Systemen des begrenzten Risikos (ab 2. August 2026):
- Nutzer über KI-Einsatz informieren (z.B. Chatbot-Hinweis)
- Interne Verhaltensrichtlinien (freiwillig, aber empfohlen)

### Für Anbieter mit Systemen des begrenzten Risikos (ab 2. August 2026):
- Transparenzpflichten: Nutzer informieren
- KI-generierte Inhalte maschinenlesbar kennzeichnen

### Für Betreiber von Hochrisiko-KI (ab 2. August 2026):
- Nutzung gemäß Herstelleranweisungen
- Betriebsaufzeichnungen führen
- Folgenabschätzungen durchführen
- Menschliche Aufsicht sicherstellen
- Schwerwiegende Vorfälle melden

### Für Anbieter von Hochrisiko-KI (ab 2. August 2026/2027):
- Risikomanagementsystem über gesamte Lebensdauer
- Datenqualität sicherstellen
- Technische Dokumentation erstellen
- Automatische Protokollierung implementieren
- EU-Datenbankregistrierung
- Konformitätsbewertung (CE-Kennzeichnung)
- Post-Markt-Überwachung
- Vorfallmeldung
- Aufbewahrung 10 Jahre

---

## 10. PRAXISCHECKLISTE FÜR KMU

### Schritt 1: Bestandsaufnahme
- Welche KI-Tools nutzen wir? (intern und von Dritten)
- Welche Risikoklasse haben diese Systeme?
- Setzen wir KI in HR, Kreditvergabe, Kundeninteraktion ein?

### Schritt 2: Rollenklärung
- Sind wir Anbieter oder Betreiber?
- Nutzen wir White-Label-Lösungen, die wir vermarkten? → Achtung: Anbieterpflichten!
- Haben wir GPAI-Modelle im Einsatz oder entwickeln wir sie?

### Schritt 3: Sofortmaßnahmen (bereits Pflicht seit Feb. 2025)
- KI-Kompetenz im Unternehmen sicherstellen
- Schulungskonzept entwickeln und dokumentieren
- Prüfen: Nutzen wir verbotene KI-Praktiken?

### Schritt 4: Verträge und Haftung
- AGB und Verträge mit KI-Anbietern prüfen
- Haftungsregelungen und Nutzungsbeschränkungen festlegen
- Verantwortlichkeiten zwischen Anbieter und Betreiber klären

### Schritt 5: DSGVO-Kompatibilität
- Privacy by Design einhalten
- Auftragsverarbeitungsverträge (AV-Verträge) abschließen
- Einwilligungen prüfen

### Schritt 6: Transparenz und Kennzeichnung (ab Aug. 2026)
- Chatbot-Hinweise implementieren
- KI-generierte Inhalte kennzeichnen
- Deepfake-Richtlinien erstellen

### Schritt 7: Dokumentation
- Entscheidungsprozesse festhalten
- Trainingsdaten und Algorithmen dokumentieren
- Schulungsmaßnahmen aufzeichnen

### Schritt 8: Interne Richtlinien
- KI-Nutzungsrichtlinie erstellen (Dateneingaben, Datenschutz, erlaubte Anwendungen)
- Ggf. KI-Beauftragten ernennen (nicht gesetzlich vorgeschrieben, aber empfehlenswert)

---

## 11. GOVERNANCE-STRUKTUR

### Europäische Ebene:
- **KI-Büro der EU-Kommission:** Koordiniert Gesamtumsetzung, überwacht GPAI-Modelle
- **Europäisches Gremium für KI (AI Board):** Beratendes Gremium (ein Vertreter je Mitgliedstaat)
- **Unabhängige wissenschaftliche Beratung:** Technische Unterstützung

### Nationale Ebene (Deutschland):
- **Marktüberwachungsbehörde:** Mindestens eine je Mitgliedstaat; in Deutschland zentral: **Bundesnetzagentur**
- **Notifizierungsbehörden:** Bewertung und Notifizierung von Konformitätsbewertungsstellen
- **Sektorale Behörden:** Für Anhang-I-Bereiche (Funkanlagen, Maschinen etc.)

**Benennung:** Bis 2. August 2025

### KoKIVO – Koordinierungs- und Kompetenzzentrum für die KI-Verordnung:
Eingerichtet bei der **Bundesnetzagentur** mit folgenden Aufgaben:
1. Fachliche Unterstützung der Marktüberwachungsbehörden
2. Koordinierung bei horizontalen Rechtsfragen
3. Technisches Fachwissen und Normierungsmitwirkung
4. Unterstützung bei Verhaltenskodizes für Unternehmen

**Zielgruppen:** Marktüberwachungsbehörden, KMU, Start-ups, Notifizierende Behörden

**Serviceangebote:**
- FAQ und Informationsmaterialien
- KI-Compliance Kompass (Prüfleitfaden)
- Kontaktformular für spezifische Fragen
- Veranstaltungen (KI-Café, Netzwerktreffen)

### Deutsches Umsetzungsgesetz:
- Kabinettsbeschluss: 11. Februar 2026
- Bundesminister Karsten Wildberger (Digitales und Staatsmodernisierung) hatte den Entwurf vorgelegt
- Ziel: "innovationsfreundlicher und verlässlicher Rechtsrahmen"
- Regelt: Welche Bundesbehörden für Marktüberwachung und Notifizierung zuständig sind

---

## 12. KI-REALLABORE (Regulatory Sandboxes)

**Rechtliche Grundlage:** KI-Verordnung, Artikel 57 ff.
**Frist:** Jeder EU-Mitgliedstaat muss bis **2. August 2026** mindestens ein einsatzbereites KI-Reallabor auf nationaler Ebene einrichten.

### Zweck:
Kontrollierte Umgebung zur Förderung von Innovationen; ermöglicht es, innovative KI-Systeme unter realen Bedingungen zu erproben, bevor sie auf den Markt kommen.

### Aktivitäten im Reallabor:
- Entwicklung, Training und Validierung innovativer KI-Systeme
- Tests unter realen Bedingungen
- Prüfung komplexer rechtlicher Fragestellungen
- Dokumentation in einem Abschlussbericht

**Formen:** Physisch, digital oder hybrid möglich

### Vorteile für KMU und Start-ups:
- Reduktion regulatorischer Unsicherheit
- Behördliche Unterstützung bei der Compliance
- Zugang zu praktischem Feedback und Expertise
- Beschleunigte Markteinführung innovativer Lösungen

### Deutsche Initiativen:
- **Pilotprojekt Deutschland:** Start Mai 2025
- **EUSAiR-Pilotprojekt (EU-weit):** Oktober 2025 – März 2026, bis zu 90 Anwendungsfälle

---

## 13. BESONDERHEITEN FÜR KMU (Zusammenfassung)

### KMU-freundliche Regelungen im AI Act:
- **Proportionalität:** Risikobasierter Ansatz erlaubt verhältnismäßige Compliance-Maßnahmen
- **Innovationsunterstützung:** Forschungs- und Entwicklungsausnahmen
- **KI-Reallabore:** Besonderer Zugang für KMU und Start-ups
- **Freiwillige Verhaltenskodizes:** Niedrigschwellige Compliance-Möglichkeit
- **Kostenfreie Unterstützung:** Mittelstand-Digital Zentren, ~100 KI-Trainer für KMU
- **European Digital Innovation Hubs:** Kostenlose Beratung

### Besondere Risiken für KMU:
- **White-Label-Falle:** Wer angepasste KI-Produkte vertreibt, ist Anbieter mit Vollpflichten
- **HR-Tools:** Bewerberselektion, Leistungsbewertung = häufig Hochrisiko
- **Sofortpflicht übersehen:** Schulungspflicht gilt bereits seit Feb. 2025 – keine Übergangsfrist!
- **Unklare Rollenabgrenzung:** Anbieter vs. Betreiber unbedingt rechtlich klären

### Empfehlung:
Aktiv werden ist dringend empfohlen, auch wenn nicht alle Regeln sofort gelten. Die Schulungspflicht gilt bereits jetzt. Unklare Rollen sollten mit rechtlicher Beratung geklärt werden.

---

## 14. QUELLENÜBERSICHT

| Quelle | URL | Status |
|--------|-----|--------|
| EU AI Act Hub | https://artificialintelligenceact.eu/ | 403 Fehler (Zugriff verweigert) |
| Bundesregierung AI Act | https://www.bundesregierung.de/breg-de/aktuelles/ai-act-2285944 | Teilinhalt verfügbar |
| Bundesregierung Umsetzung | https://www.bundesregierung.de/breg-de/aktuelles/umsetzung-ki-verordnung-2406638 | Vollinhalt verfügbar |
| IHK Hannover – Schulungspflicht | https://www.ihk.de/hannover/hauptnavigation/digitalisierung/aktuell-digitalisierung/ai-act-unternehmen-muessen-mitarbeitende-in-ki-schulen-6470624 | 403 Fehler (Zugriff verweigert) |
| e-recht24.de – KI-Anbieter | https://www.e-recht24.de/ki/13401-ki-anbieter.html | Vollinhalt verfügbar |
| Bundesnetzagentur KI-Kompass | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/2_Risiko/kompass/start.html | Navigationsstruktur verfügbar |
| Bundesnetzagentur – Hochrisiko | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/9_Hochrisiko/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Verbote | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/8_VerbotenePraktiken/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Transparenz | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/4_Transparenzpflichten/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Kompetenz | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/7_Kompetenz/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – GPAI | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/3_Modelle/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Definitionen | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/6_Definitionen/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Governance | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/11_Gov_u_Anlauf/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Reallabore | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/5_Innovationen/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Marktüberwachung | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/14_Marktueberwachung/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – KoKIVO | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/15_Koordinierung/start.html | Vollinhalt verfügbar |
| Bundesnetzagentur – Zeitplan | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/1_Ziel/start_ziel.html | Vollinhalt verfügbar |
| EUR-Lex Verordnung 2024/1689 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689 | Vollinhalt verfügbar |
| Bundesnetzagentur – Risikostufen | https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/2_Risiko/start_risiko.html | Vollinhalt verfügbar |
