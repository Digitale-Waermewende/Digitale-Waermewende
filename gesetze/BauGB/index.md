---
layout: default
title: Baugesetzbuch
parent: Gesetze
nav_order: 2
has_children: true
permalink: /gesetze/baugb/
---

# Baugesetzbuch (BauGB)

## Original-Gesetzestext

🔗 **Primärquelle (Gesetze im Internet):**
- [Volltext BauGB](https://www.gesetze-im-internet.de/bbaug/)
- **Stand:** 27. Oktober 2025 (BGBl. 2025 I Nr. 257)
- **Ausfertigungsdatum:** 3. November 2017 (aktuelle Bekanntmachung)
- **Fundstelle:** BGBl. I S. 3634

## Relevanz für Digitale Wärmewende

Das Baugesetzbuch ist **die rechtliche Grundlage für die Bauleitplanung in Deutschland**. Es definiert, welche Inhalte in Flächennutzungsplänen und Bebauungsplänen dargestellt bzw. festgesetzt werden können - und damit auch die Grundlage für deren digitale Abbildung durch den **XPlanung-Standard**.

### XPlanung als digitales Abbild des BauGB

Der Standard **XPlanung** formalisiert die im BauGB definierten Planungsinhalte in ein maschinenlesbares Datenformat:
- **BauGB definiert** rechtlich, was in Bauleitplänen stehen muss/kann
- **XPlanung formalisiert** diese Inhalte als standardisierte Objektarten
- **Seit Februar 2023** ist XPlanung Pflichtstandard für alle Verwaltungen

### Relevanz für Wärmeplanung

Wärmepläne nach WPG können über die Bauleitplanung rechtlich verbindlich werden:
- **§27 WPG**: Ausweis-Entscheidungen müssen in Bauleitplanungen berücksichtigt werden
- **§5 BauGB**: Flächennutzungsplan kann Flächen für Energieversorgung darstellen
- **§9 BauGB**: Bebauungsplan kann Versorgungsflächen für Wärme festsetzen
- **§11 BauGB**: Städtebauliche Verträge können Anforderungen an erneuerbare Energien regeln

## Struktur des Gesetzes

Das BauGB gliedert sich in vier Kapitel:

1. **Erstes Kapitel: Allgemeines Städtebaurecht**
   - Enthält die Regelungen zur Bauleitplanung (§§1-13)
   - Bauordnungsrechtliche und sonstige Vorschriften

2. **Zweites Kapitel: Besonderes Städtebaurecht**
   - Städtebauliche Sanierung, Entwicklung, Umlegung

3. **Drittes Kapitel: Sonstige Vorschriften**
   - Entschädigungsregelungen, Erschließung

4. **Viertes Kapitel: Überleitungs- und Schlussvorschriften**

## Wichtige Paragraphen für XPlanung

Die folgenden Paragraphen bilden die rechtliche Grundlage für digitale Bauleitpläne und damit für die Umsetzung der Wärmeplanung:

### §5 BauGB - Inhalt des Flächennutzungsplans
- 🔗 [Link zum Paragraphen](https://www.gesetze-im-internet.de/bbaug/__5.html)
- **Funktion**: Preparatory land-use plan (vorbereitende Bauleitplanung)
- **Form**: "Darstellungen" (rechtlich nicht direkt bindend für Bürger)
- **Inhalt**: Art der Bodennutzung für das gesamte Gemeindegebiet

**Relevant für Wärmeplanung (Abs. 2):**
- Flächen für Versorgungsanlagen, Abfallentsorgung, Abwasserbeseitigung
- Anlagen und Einrichtungen zur Erzeugung von Strom oder Wärme aus erneuerbaren Energien oder Kraft-Wärme-Kopplung
- Anlagen und Einrichtungen zur Nutzung solarer Strahlungsenergie in, an oder auf Dach- und Außenwandflächen
- Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Klima (natürlicher Klimaschutz und Anpassung an den Klimawandel)

**XPlanung-Bezug**: Diese Darstellungen werden als XPlanung-Objektarten im Fachschema "Flächennutzungsplan" abgebildet.

### §9 BauGB - Inhalt des Bebauungsplans
- 🔗 [Link zum Paragraphen](https://www.gesetze-im-internet.de/bbaug/__9.html)
- **Funktion**: Legally binding development plan (verbindliche Bauleitplanung)
- **Form**: "Festsetzungen" (rechtsverbindlich)
- **Inhalt**: Konkrete Regelungen für Teilgebiete der Gemeinde

**Relevant für Wärmeplanung (Abs. 1):**
- Art und Maß der baulichen Nutzung
- Flächen für Versorgungsanlagen und -leitungen (Elektrizität, Gas, Wärme, Kälte, Wasser)
- Flächen für Anlagen zur Erzeugung, Verteilung, Nutzung oder Speicherung von Strom, Wärme oder Kälte aus erneuerbaren Energien oder Kraft-Wärme-Kopplung
- Gebiete, in denen bei der Errichtung von Gebäuden bestimmte bauliche Maßnahmen für den Einsatz erneuerbarer Energien getroffen werden müssen
- Aus Gründen des Klimaschutzes: Gebiete für Kraft-Wärme-Kopplung und erneuerbare Energien

**XPlanung-Bezug**: Diese Festsetzungen werden als XPlanung-Objektarten im Fachschema "Bebauungsplan" abgebildet.

### §11 BauGB - Städtebaulicher Vertrag
- 🔗 [Link zum Paragraphen](https://www.gesetze-im-internet.de/bbaug/__11.html)
- **Funktion**: Vertragliche Vereinbarungen zwischen Gemeinde und Projektträgern
- **Form**: Schriftform erforderlich

**Relevant für Wärmeplanung (Abs. 1):**
- Vereinbarungen können Anforderungen an die energetische Qualität von Gebäuden und an den Einsatz erneuerbarer Energien enthalten
- Ermöglicht Kooperationen für Wärmenetz-Infrastruktur
- Kostenübernahme für Infrastrukturmaßnahmen regelbar

**XPlanung-Bezug**: Städtebauliche Verträge können in XPlanung referenziert werden.

## Bauleitplanung und XPlanung

### Rechtliche Grundlage

Das BauGB definiert in **§1 Abs. 2**:
> "Bauleitpläne sind der Flächennutzungsplan (vorbereitender Bauleitplan) und der Bebauungsplan (verbindlicher Bauleitplan)."

Diese beiden Planungsebenen werden durch XPlanung digital abgebildet:

1. **Flächennutzungsplan (§5 BauGB)**
   - Darstellungen für das gesamte Gemeindegebiet
   - XPlanung Fachschema: "FP_Plan"

2. **Bebauungsplan (§9 BauGB)**
   - Festsetzungen für Teilgebiete
   - XPlanung Fachschema: "BP_Plan"

### Zweistufiges Planungssystem

- **Flächennutzungsplan**: Rahmenplanung ("Darstellungen")
- **Bebauungsplan**: Konkretisierung und rechtsverbindliche Festsetzungen
- **Entwicklungsgebot**: Bebauungspläne sind aus dem Flächennutzungsplan zu entwickeln

XPlanung bildet dieses hierarchische System durch entsprechende Objektarten und Verknüpfungen ab.

### Integration von Wärmeplanung

**Rechtliche Verzahnung WPG ↔ BauGB:**

1. **§27 WPG**: Gebietsausweisungen (Wärmenetze, Wasserstoffnetze) müssen in Abwägungs- und Ermessensentscheidungen bei Bauleitplanungen berücksichtigt werden

2. **§5 BauGB**: Kann Flächen für Wärmeversorgung aus erneuerbaren Energien darstellen

3. **§9 BauGB**: Kann Versorgungsflächen für Wärme und Anlagen zur Wärmeerzeugung festsetzen

4. **XPlanung**: Das Fachschema Wärmeplan ermöglicht die digitale Integration von Wärmeplänen in die Bauleitplanung

## Querverweise

**Verwandte Gesetze:**
- [Wärmeplanungsgesetz (WPG)](../WPG/) - Wärmepläne sind in Bauleitplanung zu berücksichtigen (§27 WPG)
- [Gebäudeenergiegesetz (GEG)](https://www.gesetze-im-internet.de/geg/) - Energetische Anforderungen an Gebäude
- Baunutzungsverordnung (BauNVO) - Detaillierte Regelungen zu Baugebieten

**Verwandte Standards:**
- [XPlanung](../../standards/XPlanung/) - Digitaler Standard für Bauleitplanung nach BauGB
- [XPlanung Fachschema Wärmeplan](../../standards/XPlanung/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md) - Integration von Wärmeplanung

**Stakeholder:**
- [XLeitstelle](../../stakeholder/bund/XLeitstelle/) - Verwaltung des XPlanung-Standards
- Kommunen/Gemeinden - Planungsverantwortliche Stellen
- Planungsbüros - Ersteller von Bauleitplänen
- Landesbehörden - Genehmigung und Aufsicht

## Externe Ressourcen

### Gesetzestexte
- [BauGB Volltext](https://www.gesetze-im-internet.de/bbaug/)
- [§5 BauGB - Flächennutzungsplan](https://www.gesetze-im-internet.de/bbaug/__5.html)
- [§9 BauGB - Bebauungsplan](https://www.gesetze-im-internet.de/bbaug/__9.html)
- [§11 BauGB - Städtebaulicher Vertrag](https://www.gesetze-im-internet.de/bbaug/__11.html)

### Fachliche Ressourcen
- [BBSR - Bundesinstitut für Bau-, Stadt- und Raumforschung](https://www.bbsr.bund.de/)
- [XPlanung Handreichung (PDF)](https://xleitstelle.de/sites/default/files/2023-01/Handreichung_3_Auflage_2023-01-04.pdf) - Erläutert digitale Umsetzung des BauGB

---

*Primärquelle: Bundesministerium der Justiz - [Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/)*
*Stand der Dokumentation: 20. November 2025*
