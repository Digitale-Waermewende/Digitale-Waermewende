---
layout: default
title: Datenintegration
parent: Standards
nav_order: 5
has_children: true
permalink: /standards/datenintegration/
---

# Datenintegration - Zusammenspiel der Standards für die Wärmeplanung

Die Integration von ALKIS, XPlanung und XTrasse ist entscheidend für eine erfolgreiche digitale Wärmeplanung. Diese Seite dokumentiert das Zusammenspiel der drei komplementären Systeme.

## Überblick: Drei komplementäre Systeme

Die kommunale Wärmeplanung erfordert das Zusammenspiel **dreier komplementärer Standards**:

### [ALKIS](../ALKIS/index.md) - Oberirdische Bestandsdaten
- **Funktion**: Amtliche Liegenschaftsdaten (Ist-Zustand oberirdisch)
- **Daten**: Gebäude, Flurstücke, Nutzungen, Geometrien
- **Zeitbezug**: Gegenwart (Bestand)
- **Räumlich**: Oberirdische Objekte
- **Wichtig**: Enthält **keine Leitungsnetze**

### [XTrasse](../XTrasse/index.md) - Leitungsnetze
- **Funktion**: Modellierung von Leitungsinfrastrukturen (Bestand und Planung)
- **Daten**: Wärmenetze, Gas, Strom, Wasser, Abwasser
- **Zeitbezug**: Gegenwart UND Zukunft
- **Räumlich**: Ober- und unterirdisch
- **Besonderheit**: Schließt Lücke von ALKIS bei Netzinfrastrukturen

### [XPlanung](../XPlanung/index.md) - Planungsdokumente
- **Funktion**: Digitaler Austausch von Planungsdaten (Soll-Zustand)
- **Daten**: Wärmepläne, Bauleitpläne, Festsetzungen
- **Zeitbezug**: Zukunft (Planung)
- **Räumlich**: Planungsräume und -flächen
- **Erweiterung**: Fachschema Wärmeplan

## Technische Integration

### Gemeinsame Basis
Alle drei Standards nutzen:
- **XML** als Datenformat
- **GML** (Geography Markup Language) für Geometrien
- **ISO 19100-Serie** als Normgrundlage
- **OGC-Standards** für Webservices

### Datenverknüpfung für Wärmeplanung

**Typischer Workflow**:

1. **ALKIS** liefert Gebäudegrundrisse und -funktionen
   - Wohngebäude, Gewerbe, Industrie
   - Geometrien für Wärmebedarfsberechnung

2. **XTrasse** erfasst bestehende und geplante Wärmenetze
   - Vorhandene Fernwärmeleitungen
   - Geplante Trassenverläufe
   - Koordination mit anderen Leitungsnetzen

3. **XPlanung** integriert beides im kommunalen Wärmeplan
   - Wärmeversorgungsgebiete
   - Eignungsgebiete für Wärmenetze
   - Festsetzungen in Bauleitplänen

### Verknüpfung über IDs
- **ALKIS-ID**: 16-stelliger eindeutiger Gebäudeidentifikator
- **Flurstückskennzeichen**: Räumliche Referenz
- **Koordinaten**: GML-Geometrien als gemeinsame Basis

## Herausforderungen

### Keine direkte Schnittstelle
**Wichtig**: Es gibt **keine direkte Schnittstelle** zwischen ALKIS und XPlanung/XTrasse. Die Integration erfolgt über:

1. **Datenexport** aus ALKIS via NAS-Schnittstelle (XML/GML)
2. **Import** in GIS/Planungssoftware mit NAS-Konverter
3. **Referenzierung** über gemeinsame Identifikatoren
4. **Anreicherung** mit weiteren Daten (Energie, Wärmenetze)
5. **Export** als XPlanGML mit Wärmeplan-Schema

### Datenverfügbarkeit
- **ALKIS**: Über Landesvermessungsämter (gebührenpflichtig)
- **XTrasse**: Dezentral bei Netzbetreibern und Kommunen
- **XPlanung**: Bei Planungsbehörden und Planungsbüros

## Best Practices für Wärmeplanung

### 1. Gebäudebestand erfassen
- ALKIS-Daten über Landesvermessungsamt beschaffen
- Gebäudefunktionen und Geometrien extrahieren
- Mit Energieverbrauchsdaten anreichern (EVU, Schornsteinfeger)

### 2. Netzinfrastruktur erfassen
- Bestehende Wärmenetze über Netzbetreiber (XTrasse-Format)
- Gasnetze und Stromnetze für Koordination
- Abwassernetze für Abwärmepotenziale

### 3. Wärmeplanung erstellen
- Wärmebedarfsanalyse auf ALKIS-Gebäudedaten
- Netzeignungsgebiete unter Berücksichtigung von XTrasse-Daten
- Export als XPlanGML mit Fachschema Wärmeplan

### 4. In Bauleitplanung integrieren
- Wärmeplan-Festsetzungen in Bebauungsplänen
- Koordination mit anderen Fachplanungen
- Digitaler Austausch über XPlanung

## Dokumente in diesem Bereich

### ALKIS-XPlanung Integration

**[ALKIS-XPlanung Datenaustausch](2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md)**
Technische Analyse der Datenintegration zwischen ALKIS und XPlanung für gebäudespezifische Wärmeplanung. Beschreibt den mehrstufigen Prozess über NAS-Schnittstelle und GML-Konvertierung.

### Verhältnis der drei Standards

**[ALKIS-XPlanung-XTrasse Verhältnis](2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md)**
Umfassende Analyse des Zusammenspiels von ALKIS, XPlanung und XTrasse. Erklärt die komplementären Funktionen, Entwicklungsgeschichten und technische Integration der drei Systeme für die Wärmeplanung.

## Verwandte Bereiche

- **Standards**: [ALKIS](../ALKIS/index.md), [XPlanung](../XPlanung/index.md), [XTrasse](../XTrasse/index.md)
- **Organisationen**: [AdV](../../stakeholder/bund/AdV/index.md), [XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md)
- **Praxishilfen**: [KWW-Halle](../../stakeholder/bund/KWW-Halle/index.md) (Datenkompass)
