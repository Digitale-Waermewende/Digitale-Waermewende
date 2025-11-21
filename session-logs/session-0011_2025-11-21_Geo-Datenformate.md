---
layout: default
title: "Session 0011"
parent: Session Log
nav_exclude: true
permalink: /session-log/session-0011/
---

# Session 011 - 2025-11-21 22:05 - Geo-Datenformate Standard hinzugefügt

**Metadaten**: 2025-11-21 | 22:05 - 23:15 | Commits: [503185e](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/503185e)

### User-Eingaben

#### 1. Initiale Anfrage
```
Erstelle einen neuen Ordner Standards/Geo-Datenformate. Führe einen Deep Research zu Shapefile, WFS
und GeoJSON durch. Erkläre den Aufbau und die Historie der drei Datenformate. Erkläre den UNterschied
zwischen Datenformat und Schema. Erkläre die Schema-Hierarchie OCG/INSPIRE/Schemata der XLeitstelle
für WFS und GeoJSON. Erkläre die Unterschiede zwischen WFS und GeoJSON (mit REST-API) bezüglich eines
Datenustausches zwischen verschiedenen Software-Lösungen bzw. webbasierten Plattformen. Beschreibe,
wie die XLeitstelle ihre Standard sowohl als WFS bzs XML Schema als auch als JSON Schema zur Verfügung
stellen. Verlinke zu allen Aussagen auf gepüfte Primärquellen.
```

### Ergebnisse

**Commits**: [503185e](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/503185e)

**Neue Seiten**:
- [Geo-Datenformate](/standards/geo-datenformate/)
- [Geo-Datenformate Deep Research](/standards/geo-datenformate/2025-11-21_Geo-Datenformate-Shapefile-WFS-GeoJSON_Research.md)

**Geänderte Seiten**:
- (keine)

### Entscheidungen

**Neuer Standard-Bereich Geo-Datenformate etabliert**:
- Dokumentation der technischen Grundlagen für räumlichen Datenaustausch
- Fokus auf drei zentrale Formate: Shapefile, WFS, GeoJSON
- Relevanz für XLeitstelle-Standards (XPlanung, XBau, XTrasse)

**Shapefile dokumentiert (ESRI, 1990er)**:
- Aufbau: Mindestens 3 Dateien (.shp Geometrien, .shx Index, .dbf Attribute)
- Optional: .prj (Koordinatensystem in WKT-Format)
- Geometrietypen: Point, Polyline, Polygon, Multi*
- **Limitierungen identifiziert**: 2GB-Grenze, 10-Zeichen-Feldnamen, kein Unicode, dBASE-Format (1980er)
- **Alternative empfohlen**: GeoPackage (OGC-Standard)
- Weiterhin verbreitet in Desktop-GIS (QGIS, ArcGIS)

**WFS dokumentiert (OGC, 2002-2010)**:
- Versionshistorie: 1.0 (2002), 1.1 (2005), 2.0 (2010)
- Operationen: GetCapabilities, DescribeFeatureType, GetFeature, Transaction
- Datenformat: GML (Geography Markup Language), XML-basiert
- Client-Server-Architektur über HTTP
- **Modernisierung**: WFS 3.0 umbenannt zu OGC API Features (REST/JSON statt SOAP/XML)

**GeoJSON dokumentiert (Community/IETF, 2008/2016)**:
- Community-Standard 2008 → IETF RFC 7946 (August 2016)
- JSON-basiert, menschenlesbar
- 7 Geometrietypen: Point, LineString, Polygon, Multi*, GeometryCollection
- **Strikt WGS84 (EPSG:4326)** - keine anderen CRS erlaubt laut RFC
- Vorteile: Einfach, JavaScript-nativ, web-freundlich
- Nachteile: Größere Dateien, keine räumliche Indexierung
- **Erweiterung**: JSON-FG (OGC Features and Geometries JSON, 2025) löst CRS-Limitierung

**Fundamentale Konzepte erklärt**:

*Datenformat vs. Schema:*
- **Datenformat (Container)**: WIE werden Daten gespeichert? (Shapefile, GML, JSON)
  - Syntax, Encoding, physische Struktur
- **Schema (Inhalt)**: WAS bedeuten die Daten? (XPlanung, ALKIS, INSPIRE)
  - Objektarten, Attribute, Datentypen, Validierungsregeln, Semantik
- **Beispiel**: XPlanung (Schema) kann in GML (Format) ODER JSON-FG (Format) codiert werden
- ISO 19109 definiert Mapping UML → technische Schemas

*Schema-Hierarchie dokumentiert:*
```
ISO 19100 Serie (Normative Basis)
    ↓
OGC-Standards (Technische Grundlagen: GML, WFS, Simple Features)
    ↓
INSPIRE (34 EU-Themen: Land Use, Utility Networks, Buildings)
    ↓
XLeitstelle (Deutsche Fachspezifika: XPlanung, XBau, XTrasse, XBreitband)
```
- **OGC**: WIE werden Geo-Daten ausgetauscht? (Technologie)
- **INSPIRE**: WAS wird ausgetauscht? (EU-weite Harmonisierung)
- **XLeitstelle**: Deutsche Bauplanung nach BauGB

**WFS vs. GeoJSON für Datenaustausch analysiert**:

Vergleichstabelle erstellt mit Kriterien:
- Protokoll: SOAP/XML vs. REST/HTTP
- Datenformat: GML (XML) vs. GeoJSON (JSON)
- Standardisierung: OGC-Standard vs. Community/RFC vs. OGC API Features
- Transaktionen: Ja (WFS) vs. Nein (GeoJSON) vs. Ja (OGC API Features)
- Performance: Langsam (XML) vs. Schnell (JSON)
- Komplexität: Hoch vs. Niedrig vs. Mittel

**Anwendungsfälle identifiziert**:
- **WFS 2.0**: Desktop-GIS, Transaktionen, INSPIRE-Compliance, Legacy-Systeme
- **GeoJSON/REST**: Web-Apps, mobile Apps, Visualisierung, Prototypen
- **OGC API Features**: Moderne GDI, Best-of-both-worlds, zukunftssicher

**XLeitstelle-Bereitstellung dokumentiert**:
- **Primärformat**: GML 3.2.2 (ISO 19136), XML-Schemas (.xsd), UML-Modelle (ISO 19109)
- **JSON-Format**: JSON-FG in Entwicklung (Veröffentlichung 2025 erwartet)
- **Konvertierungstools**: GDAL/ogr2ogr, ShapeChange (modellgetrieben), FME, QGIS
- **Repositories**: gitlab.opencode.de/xleitstelle
  - XML-Schemas für XPlanung, XBau, XTrasse, XBreitband
  - Testdaten in GML
  - Validierungsregeln (Schematron)
  - XPlan-Validator (syntaktisch, semantisch, geometrisch)

**Deep Research Methodik**:
- 60+ Primärquellen recherchiert und verlinkt
- Offizielle Spezifikationen: ESRI (Shapefile White Paper 1998), IETF RFC 7946, OGC WFS 2.0
- Standards-Organisationen: OGC.org, INSPIRE Knowledge Base, XLeitstelle.de
- OpenCode-Repositories für praktische Beispiele

**Offene Fragen dokumentiert**:
- XRepository.de (keine konkreten Infos gefunden - Alternative: gitlab.opencode.de)
- Exaktes Shapefile-Veröffentlichungsjahr (frühe 1990er, genaues Jahr unklar)
- JSON-FG finales Release-Datum (2025 erwartet)

---

