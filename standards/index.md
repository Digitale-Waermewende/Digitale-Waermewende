---
layout: default
title: Standards
nav_order: 3
has_children: true
permalink: /standards/
---

# Standards für die digitale Wärmeplanung

Technische Standards bilden das Rückgrat der digitalen Wärmeplanung in Deutschland. Diese Seite dokumentiert die relevanten Standards und ihr Zusammenspiel für die kommunale Wärmeplanung.

## Übersicht der Standards

Die digitale Wärmeplanung basiert auf **fünf komplementären Standards**, die unterschiedliche Aspekte der Planung und Datenhaltung abdecken:

### [XPlanung](/standards/xplanung/) - Planungsdokumente
- **Funktion**: Standard für raumbezogene Planwerke (Bauleitpläne, Wärmepläne)
- **Status**: Seit 2023 Pflichtstandard
- **Wärmeplanung**: Fachschema Wärmeplan für kommunale Wärmepläne
- **Organisation**: [XLeitstelle](/stakeholder/bund/xleitstelle/)

### [XTrasse](/standards/xtrasse/) - Leitungsinfrastruktur
- **Funktion**: Standard für Modellierung von Leitungsnetzen
- **Relevanz**: Wärmenetze, Gas-, Strom-, Wassernetze
- **Status**: Seit 2021 verbindlich für Breitband
- **Organisation**: [XLeitstelle](/stakeholder/bund/xleitstelle/)

### [XBau](/standards/xbau/) - Baugenehmigungen
- **Funktion**: Standard für Baugenehmigungsverfahren
- **Relevanz**: Heizungseinbau, energetische Sanierung
- **Status**: Seit 2023 Pflichtstandard
- **Organisation**: [XLeitstelle](/stakeholder/bund/xleitstelle/)

### [ALKIS](/standards/alkis/) - Liegenschaftsdaten
- **Funktion**: Amtliche Gebäude- und Flurstücksdaten
- **Relevanz**: Grundlage für Wärmebedarfsermittlung
- **Status**: Seit 2015 bundesweit eingeführt
- **Organisation**: [AdV](/stakeholder/bund/adv/)

### [Datenintegration](/standards/datenintegration/) - Zusammenspiel
- **Funktion**: Integration von ALKIS, XPlanung und XTrasse
- **Relevanz**: Technische Schnittstellen und Workflows
- **Dokumentation**: Best Practices und Herausforderungen

## Komplementäre Funktionen

Die Standards ergänzen sich gegenseitig:

**ALKIS** liefert die **Bestandsdaten**:
- Gebäudegeometrien und -funktionen
- Flurstücke und Nutzungen
- **Wichtig**: Enthält keine Leitungsnetze!

**XTrasse** erfasst die **Netzinfrastruktur**:
- Wärmenetze (Bestand und Planung)
- Koordination mit Gas-, Strom-, Wassernetzen
- Ober- und unterirdische Leitungen

**XPlanung** dokumentiert die **Planung**:
- Kommunale Wärmepläne
- Wärmeversorgungsgebiete
- Integration in Bauleitplanung

**XBau** steuert die **Umsetzung**:
- Genehmigungen für Heizungseinbau
- Energetische Sanierungsmaßnahmen
- Nachweispflichten nach GEG

## Technische Harmonisierung

Alle Standards basieren auf gemeinsamen technischen Grundlagen:
- **XML/GML**: Datenaustauschformate
- **ISO 19100-Serie**: Normative Basis
- **OGC-Standards**: Webservices und Schnittstellen
- **Open Source**: Offene Spezifikationen

## Verwaltende Organisationen

### XLeitstelle Planen und Bauen
Verantwortlich für **XPlanung, XBau und XTrasse**:
- Zentrale Koordinierungsstelle
- Entwicklung und Pflege der Standards
- Bereitstellung von Tools und Dokumentation
- [→ Zur XLeitstelle](/stakeholder/bund/xleitstelle/)

### AdV - Arbeitsgemeinschaft der Vermessungsverwaltungen
Verantwortlich für **ALKIS**:
- Koordination der 16 Landesvermessungsverwaltungen
- Pflege des AAA-Datenmodells
- GeoInfoDok-Dokumentation
- [→ Zur AdV](/stakeholder/bund/adv/)

## Weitere Ressourcen

### Praxisunterstützung
- **[KWW-Halle](/stakeholder/bund/kww-halle/)**: Kompetenzzentrum Kommunale Wärmeplanung
  - Datenkompass (bundeslandspezifisch)
  - Leitfäden und Werkzeuge
  - Veranstaltungen und Schulungen

### Technische Dokumentation
- **XLeitstelle**: Spezifikationen, Validatoren, Testdaten
- **AdV**: GeoInfoDok, NAS-Schnittstelle
- **IT-Planungsrat**: Beschlüsse zur Verbindlichkeit

---

**Navigation:** Alle Standards und ihre Dokumentation sind in der Navigation auf der linken Seite aufgelistet.
