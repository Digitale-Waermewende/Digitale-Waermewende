---
layout: default
title: XTrasse
parent: Standards
nav_order: 2
has_children: false
permalink: /standards/xtrasse/
---

# XTrasse - Standard für Leitungsinfrastruktur

XTrasse ist der verbindliche Standard für die Modellierung und Verwaltung von Leitungsnetzen in Deutschland. Als Erweiterung von XPlanung ermöglicht XTrasse die standardisierte Erfassung ober- und unterirdischer Infrastrukturen.

## Was ist XTrasse?

**Definition**: Datenaustauschstandard für die Planung, den Bau und Betrieb von leitungsgebundener Infrastruktur

**Status und Entwicklung**:
- **Seit 2021 verbindlich** für Breitbandausbau (IT-Planungsrat-Beschluss)
- **Aktuelle Version**: XTrasse 2.0 (2023) mit 6 Anwendungsfällen
- **Technische Basis**: Erweiterung von XPlanung auf gleicher Grundlage
- **Austauschformat**: XTrasseGML (XML/GML-basiert)

**Erfasste Leitungssparten**:
- **Wärmenetze/Fernwärme** ⭐ (zentral für Wärmeplanung)
- Stromnetze (alle Spannungsebenen)
- Gasnetze
- Wasserversorgung
- Abwassernetze
- Telekommunikation/Breitband

## Anwendungsfälle (XTrasse 2.0)

Die aktuelle Version 2.0 definiert **6 Anwendungsfälle**:

1. **Bestandsnetze** - Erfassung vorhandener Leitungen
2. **Breitbandausbau** - Glasfasernetze (primärer Anwendungsfall)
3. **Genehmigungsverfahren** nach TKG (Telekommunikationsgesetz)
4. **Interkommunale Konzepte** - übergreifende Infrastrukturplanung
5. **Detailplanungen** - präzise Trassenverläufe
6. **Infrastrukturatlas** - Bundesnetzagentur-Integration

## Relevanz für Wärmenetze

### Trassenplanung für Fernwärme
XTrasse ermöglicht die standardisierte Erfassung von:
- **Wärmenetz-Trassen**: Vor- und Rücklauf von Fernwärmeleitungen
- **Leitungsdurchmesser**: Dimensionierung der Netzinfrastruktur
- **Tiefenlage**: Verlegungstiefe und Kreuzungen mit anderen Leitungen
- **Anschlusspunkte**: Einspeise- und Abnahmepunkte
- **Bestand UND Planung**: Erfassung bestehender und geplanter Netze

### Komplementäre Funktion zu ALKIS und XPlanung
XTrasse ist Teil eines **dreigliedrigen Systems**:
- **ALKIS**: Oberirdische Bestandsdaten (Gebäude, Flurstücke)
- **XTrasse**: Ober- und unterirdische Leitungsnetze (Bestand und Planung)
- **XPlanung**: Planungsdokumente und Soll-Zustände

**Wichtig**: ALKIS erfasst **keine Leitungsnetze** - diese Lücke schließt XTrasse für Wärmenetze, Gasnetze und alle anderen leitungsgebundenen Infrastrukturen.

### Koordination mit anderen Netzen
Ein zentraler Vorteil von XTrasse ist die **Koordination mit anderen Leitungsnetzen**:
- Vermeidung von Konflikten bei Neu- und Umbaumaßnahmen
- Gemeinsame Trassennutzung (z.B. Fernwärme + Glasfaser)
- Abstimmung mit Gas-, Strom- und Wassernetzen
- Reduzierung von Baukosten durch koordinierte Verlegung

### Integration in Wärmeplanung
- Darstellung geplanter Wärmenetz-Trassen in kommunalen Wärmeplänen
- Export als XTrasse für Netzbetreiber und Tiefbauämter
- Grundlage für Bauantragstellung und Genehmigungsverfahren
- Integration mit XPlanung-Wärmeplan-Objektarten

## Verwaltende Organisation

**[XLeitstelle Planen und Bauen](../../stakeholder/bund/XLeitstelle/index.md)**
- Koordination der XTrasse-Entwicklung
- Pflege der Spezifikation
- Bereitstellung von Dokumentation

## Spezifikation und Dokumentation

- **Spezifikation**: [XTrasse 1.2 (PDF)](https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf)
- **XLeitstelle**: [XLeitstelle Website](https://xleitstelle.de)

## Dokumente in diesem Bereich

### Verhältnis zu XBreitband

**[Verhältnis von XTrasse zu XBreitband](2025-11-19_XTrasse-XBreitband-Verhaeltnis_Research.md)**
Umfassende Analyse der Beziehung zwischen XTrasse (Datenmodell für Leitungsnetze) und XBreitband (Nachrichtenstandard für Genehmigungsverfahren). Erklärt technische Unterschiede, gesetzlichen Kontext (IT-Planungsrat-Beschluss 2021/40), funktionale Komplementarität und Relevanz für Wärmenetze.

## Weitere Informationen

### Verhältnis zu ALKIS und XPlanung
Ausführliche Analyse des Zusammenspiels aller drei Standards für die Wärmeplanung:
- **[ALKIS-XPlanung-XTrasse Verhältnis](../Datenintegration/index.md)** - Technische Integration der drei komplementären Systeme

### Primärquellen und Dokumentation
- **Spezifikation**: [XTrasse 2.0](https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf)
- **IT-Planungsrat**: Beschluss 2021 zur Verbindlichkeit
- **Technische Details**: Siehe Datenintegrations-Dokumente

## Verwandte Bereiche

### Rechtliche Grundlagen
- **[Telekommunikationsgesetz (TKG)](../../gesetze/TKG/)** - Gesetzliche Basis für XTrasse/XBreitband
  - [§127 TKG](../../gesetze/TKG/index.md#127---zustimmung-zur-nutzung-öffentlicher-wege) - XBreitband-Verfahren (verpflichtend durch IT-PLR 2021/40)
  - [§146 TKG](../../gesetze/TKG/index.md#146---mitverlegung) - Koordinierte Verlegung (relevant für Wärmeleitungen)
- **[IT-Staatsvertrag](../../gesetze/IT-Staatsvertrag/)** - IT-PLR-Beschluss 2021/40 (XTrasse verbindlich bis 2026)

### Organisation und Standards
- **Governance**: [IT-Planungsrat](../../stakeholder/bund/IT-Planungsrat/) - Beschließt Standards
- **Betrieb**: [XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md) - Operative Umsetzung
- **Integration**: [Datenintegration](../Datenintegration/index.md) (ALKIS-XPlanung-XTrasse Zusammenspiel)
- **Weitere Standards**: [XPlanung](../XPlanung/index.md), [XBau](../XBau/index.md), [ALKIS](../ALKIS/index.md)
