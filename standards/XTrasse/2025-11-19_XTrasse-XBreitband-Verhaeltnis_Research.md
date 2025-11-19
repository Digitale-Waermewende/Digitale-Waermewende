---
layout: default
title: "Verhältnis von XTrasse zu XBreitband"
parent: XTrasse
grand_parent: Standards
nav_exclude: true
permalink: /standards/xtrasse/xtrasse-xbreitband-verhaeltnis-research/
---

# Verhältnis von XTrasse zu XBreitband

## Zusammenfassung

**XTrasse** und **XBreitband** sind zwei komplementäre, aber eigenständige Standards für den digitalen Breitbandausbau in Deutschland, die sich in **Zweck, Anwendungsbereich und technischer Natur** grundlegend unterscheiden:

- **XTrasse** ist ein **Datenmodell** (Geodatenstandard) für die Modellierung und den Austausch von Leitungsnetzplänen
- **XBreitband** ist ein **Nachrichtenstandard** (Kommunikationsprotokoll) für die Datenkommunikation in Genehmigungsverfahren

Beide Standards stehen in einer **direkten funktionalen Beziehung**: Ohne Trassenplan (XTrasse) ist eine Antragsnachricht für Breitbandausbau (XBreitband) in der Regel nicht vollständig. Sie werden **gleichzeitig verwendet** und ergänzen sich gegenseitig.

**Rechtlicher Status**: XBreitband war der erste verpflichtend eingeführte Standard (IT-Planungsrat-Beschluss 2021/40 für TKG-Zustimmungsverfahren), während XTrasse zunächst als technisches Datenmodell entwickelt wurde.

## Kontext und Hintergrund

### Entstehung und Entwicklung

**Historischer Kontext:**
- **2017:** IT-Planungsrat-Beschluss zu XPlanung und XBau als Pflichtstandards
- **2021:** Erweiterung um XBreitband und XTrasse für Breitbandausbau (IT-PLR-Beschluss 2021/40 vom 29. Oktober 2021)
- **April 2024:** Release XBreitband 1.0 und XTrasse 1.0
- **2024:** XBreitband 1.2 und XTrasse 2.0 als aktuelle Versionen

**Entwicklungsansatz:**
Die Standards wurden zunächst als "Standarderweiterung Planen & Bauen" konzipiert, entwickelten sich jedoch zu eigenständigen Standards mit spezifischen Anwendungsbereichen.

**Betreuung:**
Beide Standards werden von der **XLeitstelle Planen und Bauen** beim Landesbetrieb Geoinformation und Vermessung (LGV) Hamburg koordiniert und gepflegt.

### Abgrenzung zu XPlanung/XBau

**Fundamentale Unterschiede:**

XTrasse/XBreitband unterscheiden sich grundlegend von XPlanung/XBau:

**Entstehungskontext:**
- **XPlanung-Planwerke:** Erstellt von Gebietskörperschaften (öffentliche Hand), langfristig bindend, hoheitliche Planungsinstrumente
- **Trässenpläne (XTrasse):** Erstellt von privatwirtschaftlichen Leitungsunternehmen, projektbezogen, unterschiedliche Gültigkeitsdauer

**Beziehungsstruktur:**
- **XPlanung/XBau:** Haben nur Schnittmengen, wenn planungsrechtliche Anforderungen in Baugenehmigungsverfahren relevant sind
- **XTrasse/XBreitband:** Stehen in einer **"weitaus direkteren Beziehung"** - sie sind funktional eng verknüpft und werden typischerweise gleichzeitig genutzt

**Unabhängigkeit:**
> "Sieht man vom Entstehungskontext ab, sind XTrasse/XBreitband neue, **unabhängig von XPlanung/XBau existierende Standards**."

## XTrasse - Der Geodatenstandard

### Definition und Zweck

**XTrasse** ist ein Datenstandard für die **Modellierung von Leitungsnetzen**, der den verlustfreien Transfer vollvektorisierter georeferenzierter Pläne zwischen unterschiedlichen IT-Systemen sowie deren internetgestützte Bereitstellung unterstützt.

### Technische Charakteristika

**Datenmodell:**
- UML-Modellierung (Unified Modeling Language)
- Vollvektorielle georeferenzierte Planwerke
- Maschinenlesbares, herstellerunabhängiges Format

**Verfügbare Formate:**
- **XTrasseGML:** XML-basiertes Format (Geography Markup Language)
- **XTrasseJSON:** JSON-basiertes Format
- **UML-Modell:** EnterpriseArchitect-Format

**Technische Dokumentation:**
- HTML-Objektartenkatalog mit abstrakten Klassen und Datentypen
- XML-Schema-Dateien
- JSON-Schema-Dateien

### Anwendungsfälle XTrasse 2.0

XTrasse 2.0 modelliert **sechs Anwendungsfälle**:

#### 1. Breitbandausbau (Telecommunications Infrastructure)
- **Zweck:** Planung des Glasfasernetzeinsatzes von strategischer Planung bis zu detaillierten Genehmigungsverfahren nach Telekommunikationsgesetz
- **Inhalte:** Trassenspezifikationen und Infrastrukturkomponenten
- **Besonderheit:** Primärer Überschneidungsbereich mit XBreitband

#### 2. Infrastrukturatlas
- **Zweck:** Netzbetreiber übermitteln Daten an die Bundesnetzagentur
- **Format:** XTrasseGML
- **Kontext:** Zentrale Infrastrukturdatenbank

#### 3. Raumverträglichkeitsprüfung (Spatial Compatibility Assessment)
- **Zweck:** Kartierung von Korridorplanungsstufen, Varianten und identifizierten räumlichen Konflikten
- **Anwendung:** Großinfrastrukturplanung (z.B. Energieleitungen)
- **Besonderheit:** Fokus auf Korridore und Alternativen

#### 4. Infrastrukturflächenplan (Infrastructure Areas Plan)
- **Zweck:** Alternative Herangehensweise für Energieleitungen
- **Status:** Noch in rechtlicher Prüfung
- **Kontext:** Experimenteller Planungsansatz

#### 5. Planfeststellung (Plan Approval)
- **Zweck:** Detaillierte Planung von Energieinfrastruktur-Trassen
- **Inhalte:** Attribute, Ausführungsdetails, Bestandsanschlüsse
- **Anwendung:** Formales Genehmigungsverfahren

#### 6. Bestandsplan (Existing Asset Plan)
- **Zweck:** Konsolidierung von Versorgungsleitungsplänen über verschiedene Sektoren
- **Inhalte:** Historische Infrastrukturdaten
- **Nutzen:** Gesamtübersicht bestehender Leitungsnetze

**Relevanz für Wärmewende:**
Die Anwendungsfälle 3-6 sind **hochrelevant für Wärmenetze**, da sie Planungs- und Genehmigungsprozesse für lineare Energieinfrastruktur standardisieren.

### Veröffentlichung und Hosting

**Plattform:** OpenCode GitLab
**Repository:** [https://gitlab.opencode.de/xleitstelle/xtrasse](https://gitlab.opencode.de/xleitstelle/xtrasse)
**Objektartenkatalog:** [https://xleitstelle.de/releases/objektartenkatalogxtrasse](https://xleitstelle.de/releases/objektartenkatalogxtrasse)

## XBreitband - Der Nachrichtenstandard

### Definition und Zweck

**XBreitband** ist der Standard für die **Datenkommunikation zwischen Antragsstellern und Genehmigungsbehörden** im Kontext des Breitbandausbaus. Er definiert Strukturen und Inhalte aller Nachrichten, die erforderlich sind, um die Prozesse in den jeweiligen Verfahren von der Antragstellung bis zum Bescheid abzubilden.

### Technische Charakteristika

**Nachrichtenstandard:**
- Strukturierte Kommunikation (Maschine-zu-Maschine)
- XÖV-konform (XML-basiertes Austauschformat der öffentlichen Verwaltung)
- Definierte Nachrichtentypen für Verwaltungsabläufe

**Dokumentation:**
- PDF-Spezifikation mit allen Nachrichten und Datentypen
- XML-Schema-Dateien für Schnittstellenimplementierung
- Codelisten im OASIS-Genericode-Format
- UML-Modell (XMI und MagicDraw-Format)

### Anwendungsfälle XBreitband

XBreitband deckt **zwei primäre Anwendungsszenarien** ab:

#### 1. Zustimmungsverfahren nach TKG (Telecommunications Act Approval)
**Kernverfahren:**
- **Rechtsgrundlage:** § 127 Abs. 1 TKG (Telekommunikationsgesetz)
- **Umfang:** 11 definierte Nachrichten
- **Zweck:** Koordination der Wegerechts-Sicherung für Breitbandausbau
- **Status:** **Verpflichtend** durch IT-Planungsrat-Beschluss 2021/40

**Ablauf:**
Antragstellung → Behördenbeteiligung → Prüfung → Zustimmung/Ablehnung → Bescheid

#### 2. Straßenrechtliche Genehmigungen (Street Opening Permits)
**Anwendungsbereich:**
- Genehmigungen nach Landesstraßengesetzen
- Versorgungsinfrastruktur (Strom, Gas, Wasser)
- **Umfang:** 5 wesentliche Nachrichten
- **Status:** Pilotphase

#### Weitere Anwendungsfälle (Teilweise implementiert)

**Sondernutzungsgenehmigungen:**
- Teilweise abgedeckt
- Unvollständige Nachrichtensequenzen

**Verkehrsrechtliche Anordnungen:**
- Bei Baumaßnahmen
- Pilotphase (seit 2022)

**Leitungsauskunft:**
- Noch nicht implementiert
- Identifizierter Bedarf

**Fehlende Bereiche:**
- Ausgleichsmaßnahmen nach Telekommunikationsgesetz
- Umweltschutzverfahren
- Erfordern Erweiterung der Anforderungsbeschreibung und IT-PLR-Beschluss

### Veröffentlichung und Hosting

**Plattform:** XRepository
**Spezifikation:** [https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf](https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf)
**Tool:** XML-Nachrichten-Tool (XNT) auf [GitLab](https://gitlab.opencode.de/xleitstelle/xbreitband/xnt)

## Die Beziehung zwischen XTrasse und XBreitband

### Funktionale Komplementarität

**Gleichzeitige Nutzung:**
> "Ohne einen Trassenplan ist eine Antragsnachricht für den Breitbandausbau **in der Regel nicht vollständig**."

Die Standards funktionieren als **zusammenhängendes System**:
- **XBreitband-Nachrichten** übermitteln administrative und verfahrensbezogene Informationen
- **XTrasse-Pläne** liefern die technisch-räumlichen Planungsdaten

### Inhaltliche Schnittmengen

**Gemeinsame Datenfelder:**
- Informationen über Baumaßnahmen können in beiden Standards erfasst werden
- Bestimmte Attribute einer Trasse lassen sich mit XTrasse UND XBreitband beschreiben

**Georeferenzierung:**
- Nicht auf XTrasse begrenzt
- Auch XBreitband-Nachrichten können georeferenzierte Lagedaten einer Trasse übermitteln

**Intentionale Redundanz:**
> "Diese Redundanz ist gewollt, um eine Integration in anwendungsorientierte Workflows zu erleichtern."
> (XBreitband Release 1.2 Spezifikation, 28. Mai 2024)

### Technische Abgrenzung

| Aspekt | XTrasse | XBreitband |
|--------|---------|------------|
| **Typ** | Datenmodell / Geodatenstandard | Nachrichtenstandard / Kommunikationsprotokoll |
| **Zweck** | Modellierung und Austausch von Leitungsplänen | Strukturierte Kommunikation in Verwaltungsverfahren |
| **Fokus** | Technisch-räumliche Plandarstellung | Administrative Verfahrensabläufe |
| **Format** | XTrasseGML, XTrasseJSON | XML-Nachrichten (XÖV-konform) |
| **Persistenz** | Langfristige Plandaten | Transaktionale Nachrichten |
| **Erstellende** | Privatwirtschaftliche Leitungsunternehmen | Antragsteller & Behörden |
| **Hosting** | OpenCode GitLab | XRepository |
| **Anwendungsfälle** | 6 (Infrastrukturplanung) | 2 primär + weitere in Entwicklung |

### Organisatorische Unterschiede

**XTrasse:**
- Konzentration auf **Plandarstellung**
- Sektorenübergreifend (Breitband, Energie, weitere Versorgung)
- Langfristige Infrastrukturdokumentation

**XBreitband:**
- Abbildung komplexer **Workflows** (Genehmigungen, Anzeigen, Beteiligungen)
- Prozessorientiert (Antragstellung → Bescheid)
- Transaktionale Kommunikation

### Das Konzept "Direkte Beziehung"

Im Gegensatz zu XPlanung/XBau (die nur Schnittmengen bei planungsrechtlichen Anforderungen haben) sind XTrasse/XBreitband **funktional verzahnt**:

**Typischer Workflow:**
1. **Planung:** Leitungsunternehmen erstellt Trassenplan in XTrasse
2. **Antrag:** Antragstellung über XBreitband-Nachricht (enthält Referenz auf XTrasse-Plan)
3. **Prüfung:** Behörde prüft XBreitband-Antrag und XTrasse-Plan
4. **Bescheid:** Genehmigung/Ablehnung via XBreitband-Nachricht

**Technische Integration:**
- XBreitband-Nachrichten können XTrasse-Pläne als Anhang oder Referenz enthalten
- Beide Standards müssen von IT-Systemen parallel verarbeitet werden
- Validierung erfolgt auf beiden Ebenen (Nachricht + Plan)

## Gesetzlicher und Rechtlicher Kontext

### Rechtsgrundlagen

**IT-Staatsvertrag und IT-Planungsrat-Vertrag:**
- Beschlüsse des IT-Planungsrats haben bindende Wirkung für öffentliche Verwaltung
- Grundlage für verbindliche Anwendung der Standards

**Telekommunikationsgesetz (TKG):**
- § 127 Abs. 1 TKG: Zustimmungsverfahren für Breitbandausbau
- Kernverfahren für XBreitband-Anwendung

**Landesstraßengesetze:**
- Straßenrechtliche Genehmigungen für Leitungsverlegung
- Pilotanwendung von XBreitband

### IT-Planungsrat-Beschluss 2021/40

**Beschlussdatum:** 29. Oktober 2021

**Verpflichtende Anwendung:**
> "Verbindliche Anwendung der Standards XBreitband und XTrasse für standardisierten Datenaustausch beim Breitbandausbau"

**Verpflichtender Anwendungsfall:**
- **"Zustimmung nach TKG"** im Kontext der OZG-Verwaltungsleistung Breitbandausbau

**Pilotanwendungsfälle (erprobt seit 2022):**
- Genehmigungen nach Straßen- und Wegegesetzen der Länder
- Verkehrsrechtliche Anordnungen bei Baumaßnahmen

**Implementierungsfristen:**

| IT-Verfahren | Frist für Konformität |
|--------------|----------------------|
| Neu implementiert oder wesentlich überarbeitet | **Sofort ab Beschlussfassung** (29.10.2021) |
| Andere IT-Verfahren | **Maximal 5 Jahre** (bis 29.10.2026) |

**Konsequenz:**
- Online-Verfahren für Kabelverlegung nach TKG, die vor Oktober 2021 existierten, können bis 2026 weiterlaufen
- **Neue IT-Verfahren** in diesem Rechtsbereich **müssen** XTrasseGML und XBreitband-Nachrichten verarbeiten können

### Rechtliche Verbindlichkeit im Detail

**Status der Standards (Stand 2025):**

| Standard | Rechtsgrundlage | Verbindlichkeit | Gültig seit | Frist bis |
|----------|----------------|-----------------|-------------|-----------|
| **XPlanung** | IT-PLR-Beschluss 2017 | Pflicht für alle IT-Systeme | 08.02.2018 | 08.02.2023 (abgelaufen) |
| **XBau** | IT-PLR-Beschluss 2017 | Pflicht für alle IT-Systeme | 08.02.2018 | 08.02.2023 (abgelaufen) |
| **XBreitband** | IT-PLR-Beschluss 2021/40 | Pflicht für TKG-Zustimmungsverfahren | 29.10.2021 | 29.10.2026 (Bestandssysteme) |
| **XTrasse** | IT-PLR-Beschluss 2021/40 | Pflicht für TKG-Zustimmungsverfahren | 29.10.2021 | 29.10.2026 (Bestandssysteme) |

**Gestaffelte Verbindlichkeit XBreitband/XTrasse:**

1. **Verpflichtend:** "Zustimmung für Leitungsverlegung" nach Telekommunikationsrecht (gleiche Fristen wie XPlanung/XBau)
2. **Pilotstatus:** Straßenrechtliche Genehmigungen und verkehrsrechtliche Anordnungen
3. **Anerkannter Bedarf, aber nicht verbindlich:** Drei weitere Anwendungsfälle - Standardisierung läuft, aber ohne Bindungspflicht

**Wichtige Klarstellung:**
> "Es gibt (noch) **keine gesetzliche Verpflichtung**, Pläne digital aufzustellen."

**Für XBau analog (gilt auch für XBreitband):**
> "Baubehörden sind nicht gesetzlich verpflichtet, digitale Baugenehmigungsverfahren anzubieten, aber digitale Baugenehmigungsverfahren müssen XBau-Nachrichten verarbeiten können."

**Bedeutung:**
- Behörden können weiterhin analoge Verfahren anbieten
- **Wenn** digitale Verfahren angeboten werden, **müssen** diese XBreitband/XTrasse-konform sein
- Software-Beschaffung der öffentlichen Hand muss XBreitband/XTrasse-Konformität sicherstellen

### Betrieb und Finanzierung

**Zuständigkeit:**
- Leitstelle XPlanung/XBau in Hamburg (= XLeitstelle) betreibt auch XBreitband/XTrasse
- Integration in bestehende Koordinierungsstrukturen

**Finanzierung:**
- Betriebs- und Pflegekosten in FITKO-Stammbudget aufgenommen
- Langfristige Sicherstellung der Standardpflege

**FITKO-Rolle:**
- Föderale IT-Kooperation
- Aufnahme in Lenkungskreis der XLeitstelle
- Koordination der Umsetzung über Verwaltungsebenen

## Änderungsmanagement und Weiterentwicklung

### Formales Änderungsmanagement

**Status (Stand 2024):**
> "Ein formales Änderungsmanagement für XBreitband und XTrasse **über ein Expertengremium im Aufbau**"

**Geplante Strukturen:**
- Expertengremium für fachliche Bewertung
- Transparente Change-Request-Prozesse
- Versionierung und Release-Management

### Aktuelle Versionen und Entwicklung

**XBreitband:**
- **Release 1.0:** April 2024
- **Release 1.2:** 28. Mai 2024 (aktuell)
- Kontinuierliche Erweiterung der Anwendungsfälle

**XTrasse:**
- **Release 1.0:** April 2024
- **Release 2.0:** 2024 (aktuell)
- 6 Anwendungsfälle modelliert

**Zukünftige Entwicklungen:**
- Erweiterung auf weitere Anwendungsfälle (Leitungsauskunft, Ausgleichsmaßnahmen)
- Potenzielle Einbindung weiterer Versorgungssektoren (Wasser, Fernwärme)
- Harmonisierung mit europäischen Standards

## Relevanz für die Digitale Wärmewende

### Direkte Anwendbarkeit

**XTrasse für Wärmenetze:**

1. **Fernwärmeleitungsplanung:**
   - XTrasse-Anwendungsfälle 3-6 (Raumverträglichkeit, Planfeststellung, Bestandspläne) sind direkt auf Fernwärmeleitungen übertragbar
   - Standardisierter Austausch von Fernwärme-Trassenplanungen

2. **Infrastrukturatlanten:**
   - Konsolidierung von Wärmenetzen mit anderen Versorgungsnetzen
   - Räumliche Verträglichkeitsprüfung bei Netzausbau

3. **Genehmigungsverfahren:**
   - Planfeststellung für Wärmenetzausbau
   - Integration in bestehende Leitungsinfrastruktur

**Übertragbarkeit des XBreitband-Modells:**

Obwohl XBreitband spezifisch für Breitband entwickelt wurde, bietet das Nachrichtenstandard-Konzept **Vorbildcharakter für Wärmenetze**:

1. **Genehmigungsworkflows:**
   - Strukturierte Kommunikation zwischen Wärmenetzbetreibern und Behörden
   - Standardisierte Antragsprozesse

2. **Beteiligungsverfahren:**
   - Einbindung von Stakeholdern
   - Transparente Verfahrensabläufe

3. **Digitalisierung der Verwaltung:**
   - Automatisierte Prüfungen
   - Medienbruchfreie Prozesse

### Methodische Relevanz

**Best Practices aus XTrasse/XBreitband:**

1. **Komplementäres Standard-Design:**
   - Trennung von Datenmodell (XTrasse) und Nachrichtenstandard (XBreitband)
   - Modularer Aufbau ermöglicht flexible Anwendung

2. **Intentionale Redundanz:**
   - Bewusste Überschneidungen erleichtern Integration in Workflows
   - Pragmatische Lösungen für Praxisanforderungen

3. **Gestaffelte Verbindlichkeit:**
   - Kernverfahren verpflichtend, Pilotbereiche experimentell
   - Schrittweise Ausweitung basierend auf Erfahrungen

4. **Sektorenübergreifender Ansatz:**
   - XTrasse nicht nur für Breitband, sondern für alle Leitungsnetze
   - Potenzial für integrierte Infrastrukturplanung

### Strategische Implikationen

**Potenzial für "XWärme"-Standards:**

Analog zu XBreitband/XTrasse könnten für Wärmenetze entwickelt werden:

1. **"XWärme" (Nachrichtenstandard):**
   - Genehmigungsverfahren für Wärmenetzausbau
   - Anschlussanträge und Versorgungsverträge
   - Fördermittelbeantragung

2. **XTrasse-Erweiterung:**
   - Explizite Objektarten für Fernwärmeleitungen
   - Wärmequellen und Übergabestationen
   - Wärmebedarfskartierung

**Koordination mit bestehenden Standards:**
- Integration von XPlanung (Fachschema Wärmeplan)
- Verbindung zu XBau (energetische Sanierung)
- Nutzung von XTrasse (Leitungsnetzplanung)

## Externe Ressourcen und Weiterführende Links

### Offizielle Dokumentation

**XLeitstelle Hauptportale:**
- **XBreitband/XTrasse Übersicht**: [https://xleitstelle.de/xtrassexbreitband](https://xleitstelle.de/xtrassexbreitband)
- **Standarderweiterung Planen & Bauen**: [https://xleitstelle.de/xtrassexbreitband/standarderweiterung](https://xleitstelle.de/xtrassexbreitband/standarderweiterung)
- **Rechtliche Verbindlichkeit**: [https://xleitstelle.de/leitstelle/rechtliches](https://xleitstelle.de/leitstelle/rechtliches)

**XTrasse-Ressourcen:**
- **Anwendungsfälle & Datenmodell**: [https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2](https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2)
- **Objektartenkatalog XTrasse**: [https://xleitstelle.de/releases/objektartenkatalogxtrasse](https://xleitstelle.de/releases/objektartenkatalogxtrasse)
- **GitLab Repository**: [https://gitlab.opencode.de/xleitstelle/xtrasse](https://gitlab.opencode.de/xleitstelle/xtrasse)
- **XTrasse 1.0 Ankündigung**: [https://xleitstelle.de/node/118](https://xleitstelle.de/node/118)

**XBreitband-Ressourcen:**
- **Anwendungsfälle XBreitband**: [https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle1](https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle1)
- **Änderungsmanagement und Releases**: [https://xleitstelle.de/xtrassexbreitband/download](https://xleitstelle.de/xtrassexbreitband/download)
- **Spezifikation XBreitband 1.2 (PDF)**: [https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf](https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf)
- **XBreitband im XRepository**: [https://www.xrepository.de/details/urn:xoev-de:it-plr:standard:xbau-tiefbau](https://www.xrepository.de/details/urn:xoev-de:it-plr:standard:xbau-tiefbau)

### Rechtliche Grundlagen

**IT-Planungsrat:**
- **IT-PLR Beschluss 2021/40**: [https://www.it-planungsrat.de/beschluss/beschluss-2021-40](https://www.it-planungsrat.de/beschluss/beschluss-2021-40)
- **Beschlussunterlage "Parallele Erweiterung der IT-Standards" (PDF)**: [https://www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-06_Parallele_Erweiterung_der_IT_Standards_AL1.pdf](https://www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-06_Parallele_Erweiterung_der_IT_Standards_AL1.pdf)
- **Bedarfsbeschreibung Breitbandausbau 1.0 (PDF)**: [https://xleitstelle.de/sites/default/files/2023-07/Bedarfsbeschreibung_Breitbandausbau_1.0.pdf](https://xleitstelle.de/sites/default/files/2023-07/Bedarfsbeschreibung_Breitbandausbau_1.0.pdf)

### FITKO und Koordination

**FITKO:**
- **XBreitband/XTrasse Detailansicht**: [https://docs.fitko.de/fit-standards/xbreitband/](https://docs.fitko.de/fit-standards/xbreitband/)
- **Aufnahme der FITKO in Lenkungskreis**: [https://xleitstelle.de/node/99](https://xleitstelle.de/node/99)

### Handreichungen und Praxishilfen

**Verbände-Dokumentation:**
- **Handreichung XPlanung (Deutscher Städtetag)**: [https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung](https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung)
- **Handreichung XPlanung 3. Auflage (Deutscher Landkreistag)**: [https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage](https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage)

**Fachpublikationen:**
- **BIMBreitband - XTrasse und XBreitband Standards**: [https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau](https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau)

### Tools und Anwendungen

- **XTrasse Anwendungen**: [https://xleitstelle.de/xtrassexbreitband/anwendungen](https://xleitstelle.de/xtrassexbreitband/anwendungen)
- **XML-Nachrichten-Tool (XNT) GitLab**: [https://gitlab.opencode.de/xleitstelle/xbreitband/xnt](https://gitlab.opencode.de/xleitstelle/xbreitband/xnt)

### OZG-Kontext

- **OZG-Leistungen Bauen & Wohnen**: [https://xleitstelle.de/ozgleistungen](https://xleitstelle.de/ozgleistungen)

## Zusammenfassung und Kernaussagen

### Die zentrale Beziehung

**XTrasse und XBreitband sind keine Unter-/Obermengen-Beziehung**, sondern **komplementäre Standards mit funktionaler Verzahnung**:

- **XTrasse** = Datenmodell für Leitungsnetzpläne (WAS wird gebaut?)
- **XBreitband** = Nachrichtenstandard für Genehmigungsverfahren (WIE wird genehmigt?)

### Historische Korrektur

Die anfängliche Vermutung "XBreitband ist eine Untermenge von XTrasse" ist **nicht korrekt**. Tatsächlich:

1. **XBreitband war zuerst verpflichtend** (IT-PLR-Beschluss 2021/40 für TKG-Verfahren)
2. **XTrasse wurde parallel entwickelt** als technisches Datenmodell
3. Beide sind **gleichwertig und gleichzeitig notwendig**

### Gesetzliche Situation

**XBreitband:**
- **Verpflichtend** für digitale IT-Systeme im TKG-Zustimmungsverfahren (seit 2021, Frist bis 2026)
- **Pilot** für straßenrechtliche Genehmigungen
- **Keine allgemeine gesetzliche Pflicht** zur Digitalisierung von Verfahren

**XTrasse:**
- **Verpflichtend** parallel zu XBreitband für TKG-Verfahren
- **Sektorenübergreifend** angelegt (nicht nur Breitband)
- **Potenzial** für weitere Infrastrukturbereiche (Energie, Wasser, Wärme)

### Technische Essenz

| Kriterium | XTrasse | XBreitband |
|-----------|---------|------------|
| **Kategorie** | Geodatenstandard | Kommunikationsprotokoll |
| **Persistenz** | Langfristige Plandaten | Transaktionale Nachrichten |
| **Ersteller** | Leitungsunternehmen | Antragsteller + Behörden |
| **Fokus** | Räumlich-technisch | Administrativ-prozessual |
| **Hosting** | OpenCode GitLab | XRepository |

### Relevanz für Wärmewende

**Direkt übertragbar:**
- XTrasse-Anwendungsfälle für Fernwärmeleitungen
- Genehmigungsworkflows aus XBreitband als Vorbild

**Strategisches Potenzial:**
- Entwicklung von "XWärme"-Nachrichtenstandard
- Integration in XPlanung (Fachschema Wärmeplan)
- Gesamtkoordination der Leitungsinfrastruktur

## Methodik dieser Research

**Recherche-Ansatz:**
- Primärquellen: XLeitstelle-Website (xleitstelle.de)
- Rechtliche Grundlagen: IT-Planungsrat-Beschlüsse
- Technische Dokumentation: Spezifikationen (PDF), Objektartenkataloge
- Sekundärquellen: FITKO-Dokumentation, Verbände-Handreichungen
- Vergleichende Analyse der Standarddokumente

**Limitation:**
Die Spezifikationen sind teilweise nur als PDF verfügbar, was detaillierte technische Analysen erschwert. Praktische Implementierungserfahrungen sind noch begrenzt (Standards seit 2024 im Regelbetrieb).

**Informationsstand:**
November 2025 - Aktuelle Standards: XBreitband 1.2, XTrasse 2.0

---
*Recherche durchgeführt am: 2025-11-19*
*Letzte Aktualisierung: 2025-11-19*
