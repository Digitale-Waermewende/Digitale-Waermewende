---
layout: default
title: ALKIS
parent: Standards
nav_order: 4
has_children: false
permalink: /standards/alkis/
---

# ALKIS - Amtliches Liegenschaftskatasterinformationssystem

ALKIS ist das bundesweit einheitliche System zum Nachweis der Geobasisdaten des Liegenschaftskatasters und bildet die Grundlage für räumliche Analysen in der kommunalen Wärmeplanung.

## Was ist ALKIS?

**Definition**: ALKIS ist das bundesweit einheitliche System zum Nachweis der Geobasisdaten des Liegenschaftskatasters.

**Wichtig**: ALKIS ist ein **Standard**, kein Software-System. Es definiert die Datenstruktur und Austauschformate, die von verschiedenen Software-Systemen implementiert werden.

**Vorgängersysteme**: Ersetzt seit 2015 die Vorgängersysteme:
- **ALK** (Automatisierte Liegenschaftskarte)
- **ALB** (Automatisiertes Liegenschaftsbuch)

**Entwicklungsgeschichte**:
- **1997**: Entscheidung zur AAA-Modell-Entwicklung
- **2003**: Beginn der Konzeption
- **2008**: Start der Migration in ersten Bundesländern
- **2015**: Bundesweite Einführung abgeschlossen
- **2024**: Migration auf AAA-Version 7.1

**Technische Basis**:
- **Objektorientierte Modellierung** nach AAA-Referenzmodell (AFIS-ALKIS-ATKIS)
- **GeoInfoDok-Standard**: Dokumentation des Datenmodells
- **NAS-Schnittstelle**: Normbasierte Austauschschnittstelle (XML/GML)
- **ISO/OGC-konform**: GML 3.2.2, WFS
- **Eindeutige IDs**: 16-stellige ALKIS-IDs bundesweit einmalig
- **Bundesweit einheitlich**: Über alle 16 Bundesländer

**Verwaltung**: [AdV](/stakeholder/bund/adv/) (Arbeitsgemeinschaft der Vermessungsverwaltungen)

## Erfasste Daten für die Wärmeplanung

### Gebäudedaten
- **Gebäudegrundrisse** und Umringe
- **Gebäudefunktionen**: Wohnen, Gewerbe, Industrie, etc.
- **Geschosszahlen**
- **Dachformen** (teilweise)

### Flurstücks- und Eigentumsdaten
- **Flurstücksgrenzen** und -nummern
- **Flächenangaben**
- **Grundbuchblattnummern**
- **Nutzungsarten**

### Räumliche Bezugsdaten
- **Adressen** und Lagebezeichnungen
- **Topografische Objekte**
- **Siedlungs- und Verkehrsflächen**

## Relevanz für die Wärmeplanung

### Gebäudebestand und Wärmebedarf
ALKIS liefert die **Grundlage für Wärmebedarfsermittlung**:
- Gebäudegeometrien für Volumenberechnung
- Nutzungsarten für spezifische Wärmebedarfe
- Siedlungsstrukturen für Wärmedichteanalysen
- Referenzgeometrien für Energieverbrauchsdaten

### Wichtige Einschränkung

⚠️ **Was ALKIS NICHT enthält**:
- **Keine Leitungsnetze** (Wärme, Gas, Strom, Wasser) → siehe [XTrasse](/standards/xtrasse/)
- **Keine unterirdischen Infrastrukturen**
- **Keine Energieverbrauchsdaten**
- **Keine Heizungsanlagen**
- **Keine Dämmstandards**

### Integration mit anderen Standards
ALKIS ist Teil eines **dreigliedrigen Systems**:
- **ALKIS**: Oberirdische Bestandsdaten (Gebäude, Flurstücke)
- **[XTrasse](/standards/xtrasse/)**: Leitungsnetze (Wärmenetze, Gas, etc.)
- **[XPlanung](/standards/xplanung/)**: Planungsdokumente (Wärmepläne)

Ausführliche Informationen zur Integration: **[Datenintegration](/standards/datenintegration/)**

## ALKIS-Informationen für die Wärmeplanung

### Praxisorientierte Quellen
- **[KWW-Konferenz 2024 PDF](../../stakeholder/bund/KWW-Halle/KWW-Konferenz_2024_Daten_Jeschke.pdf)** - ALKIS-Basisinformationen für Wärmeplanung
- **Quelle**: [KWW-Konferenz 2024](https://www.kww-halle.de/veranstaltungen/kww-konferenz/2024)

### Datenzugang
- **Landesvermessungsämter**: Zuständig für ALKIS-Daten in den Bundesländern
- **NAS-Schnittstelle**: Technischer Zugang über XML/GML-Export
- **KWW-Datenkompass**: Bundeslandspezifische Übersicht zur Datenbeschaffung

## Verwaltende Organisation

**[AdV - Arbeitsgemeinschaft der Vermessungsverwaltungen](/stakeholder/bund/adv/)**
- Koordination der 16 Landesvermessungsverwaltungen
- Entwicklung und Pflege des ALKIS-Standards
- Dokumentation: GeoInfoDok 7.1

## Weitere Informationen

### Technische Integration und Datenmodell
Ausführliche Analysen zur Integration von ALKIS in die Wärmeplanung:
- **[ALKIS-XPlanung-XTrasse Verhältnis](/standards/datenintegration/)** - Detaillierte Beschreibung von ALKIS-Kernmerkmalen, Datenstruktur und Zusammenspiel mit anderen Standards
- **[ALKIS-XPlanung Datenaustausch](/standards/datenintegration/)** - Technischer Prozess der NAS-Schnittstelle und GML-Konvertierung

### Primärquellen
- **AdV GeoInfoDok 7.1**: Offizielle Dokumentation des ALKIS-Datenmodells
- **AAA-Referenzmodell**: AFIS-ALKIS-ATKIS Modellierung
- **ISO 19100-Serie**: Normative Grundlagen

## Externe Ressourcen

- **AdV Website**: [https://www.adv-online.de](https://www.adv-online.de)
- **GeoInfoDok**: [AdV GeoInfoDok](https://www.adv-online.de/GeoInfoDok/)
- **Landesvermessungsämter**: [AdV Liegenschaftskataster](https://www.adv-online.de/AdV-Produkte/Liegenschaftskataster/)

## Verwandte Bereiche

- **Organisation**: [AdV](/stakeholder/bund/adv/)
- **Integration**: [Datenintegration](/standards/datenintegration/) (ALKIS-XPlanung-XTrasse Zusammenspiel)
- **Weitere Standards**: [XPlanung](/standards/xplanung/), [XTrasse](/standards/xtrasse/)
- **Praxisinfos**: [KWW-Halle](/stakeholder/bund/kww-halle/) (Datenkompass, KWW-Konferenz PDF)
