---
layout: default
title: XPlanung
parent: Standards
nav_order: 1
has_children: true
permalink: /standards/xplanung/
---

# XPlanung - Standard für raumbezogene Planwerke

XPlanung ist der verbindliche Standard für den digitalen Austausch von Raumplanungsdaten in Deutschland.

## Was ist XPlanung?

**Definition**: Offener, XML-basierter Datenaustauschstandard für Bauleitpläne, Raumordnungspläne und Schutzgebiete

**Technische Basis**:
- Geography Markup Language (GML 3.2.2)
- Aktuelle Version: XPlanGML 6.0 (mit Fachschema Wärmeplan 6.1 in Entwicklung)
- Modelliert in UML (Unified Modeling Language)
- Open-Source, ISO/OGC-konform

**Rechtlicher Status**:
- **Seit 01.02.2023 Pflichtstandard** für alle Verwaltungen
- IT-Planungsrat Beschluss 2017/37
- Ersetzt analoge Planauskünfte durch digitalen Datenaustausch

## Anwendungsbereiche

### Bauleitplanung
- Flächennutzungspläne (FNP)
- Bebauungspläne (B-Plan)
- Vorhabenbezogene Bebauungspläne

### Raumordnung
- Raumordnungspläne der Länder
- Regionalpl

äne

### Schutzgebiete
- Naturschutzgebiete
- Landschaftsschutzgebiete
- Wasserschutzgebiete

## Relevanz für die Wärmeplanung

### Fachschema Wärmeplan
XPlanung wurde um ein spezialisiertes **Fachschema für kommunale Wärmepläne** erweitert:

- **Objektartenkatalog**: Über 40 spezifische Objektarten für Wärmeplanung
- **Integration**: Wärmepläne werden als eigenständige Planwerke in XPlanung abgebildet
- **Standardisierung**: Ermöglicht automatisierten Datenaustausch zwischen Kommunen und Planungsbüros
- **Dokumentation**: [XLeitstelle Objektartenkatalog Wärmeplan](https://xleitstelle.de/releases/objektartenkatalogWaermeplan)

### Wärmeplan-Objektarten (Auswahl)
- Wärmeversorgungsgebiete (Fernwärme, dezentral, etc.)
- Eignungsgebiete für Wärmenetze
- Potenzialgebiete für Wärmequellen
- Wärmebedarfsdichten
- Trassenverlaufsdarstellungen

### Integration in Bauleitplanung
Der kommunale Wärmeplan kann über XPlanung:
- In Flächennutzungspläne integriert werden
- Als Grundlage für Bebauungsplan-Festsetzungen dienen
- Mit anderen Fachplanungen (Gas-, Stromnetz) koordiniert werden

## Verwaltende Organisation

**[XLeitstelle Planen und Bauen](/stakeholder/bund/xleitstelle/)**
- Zentrale Koordinierungsstelle für XPlanung
- Entwicklung und Pflege des Standards
- Bereitstellung von Validatoren und Testdaten

## Dokumente in diesem Bereich

### XPlanung und Wärmeplanung

**[XPlanung XLeitstelle Wärmeplanung](2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md)**
Umfassende Recherche zu XPlanung, der XLeitstelle und digitalen Standards für die Wärmeplanung. Erklärt Grundlagen, rechtlichen Rahmen und die Rolle des Fachschemas Wärmeplan.

**[XPlanung Wärmeplan Objektartenkatalog](2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md)**
Vollständiger Objektartenkatalog des XPlanung Fachschemas Wärmeplan mit über 40 spezifischen Objektarten für die kommunale Wärmeplanung.

### Umsetzungsstand und Monitoring

**[XPlanung Monitoring Umsetzungsstand](2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md)**
Verifizierte Quellen zum Umsetzungsstand von XPlanung in Deutschland. Bundeslandspezifische Übersicht der verfügbaren XPlanung-Dienste und Monitoring-Ansätze.

## Externe Ressourcen

### XLeitstelle
- [XLeitstelle Website](https://xleitstelle.de)
- [XPlanung Releases](https://xleitstelle.de/xplanung/releases-xplanung)
- [Objektartenkatalog Wärmeplan](https://xleitstelle.de/releases/objektartenkatalogWaermeplan)
- [XPlanung Validator](https://xleitstelle.de/validator)

### Dokumentation
- [XPlanung Handreichung 3. Auflage (PDF)](https://xleitstelle.de/sites/default/files/2023-01/Handreichung_3_Auflage_2023-01-04.pdf)
- [XPlanung Leitfaden 2. Auflage (PDF)](https://xleitstelle.de/sites/default/files/2023-07/Leitfaden_XPlanung_2_Auflage.pdf)

### GitLab
- [XLeitstelle GitLab](https://gitlab.opencode.de/xleitstelle)
- [XPlanung Testdaten](https://gitlab.opencode.de/xleitstelle/xplanung/testdaten)

## Verwandte Bereiche

- **Organisation**: [XLeitstelle](/stakeholder/bund/xleitstelle/)
- **Datenintegration**: [ALKIS-XPlanung Datenaustausch](/standards/datenintegration/)
- **Weitere Standards**: [XBau](/standards/xbau/), [XTrasse](/standards/xtrasse/)
