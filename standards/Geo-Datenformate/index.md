---
layout: default
title: Geo-Datenformate
parent: Standards
nav_order: 5
has_children: false
permalink: /standards/geo-datenformate/
---

# Geo-Datenformate für die digitale Wärmeplanung

Geo-Datenformate bilden die technische Grundlage für den Austausch räumlicher Daten in der Wärmeplanung. Diese Seite dokumentiert die wichtigsten Formate und ihre Anwendung im Kontext der XLeitstelle-Standards.

## Überblick

Die digitale Wärmeplanung nutzt verschiedene Geo-Datenformate für unterschiedliche Anwendungsfälle:
- **Shapefile**: Klassisches Desktop-GIS-Format
- **WFS (Web Feature Service)**: Standardisierter webbasierter Datenaustausch
- **GeoJSON**: Modernes web-natives Format

## Die drei zentralen Formate

### Shapefile - Der Klassiker (seit 1990er)

**Entwickelt von**: ESRI (Environmental Systems Research Institute)
**Erstveröffentlichung**: Frühe 1990er, Spezifikation 1998

**Aufbau**: Mehrere Dateien (mindestens 3)
- `.shp` - Geometrien
- `.shx` - räumlicher Index
- `.dbf` - Attribute (dBASE-Format)
- `.prj` - Koordinatensystem (optional, aber wichtig)

**Vorteile**:
- Weit verbreitet in Desktop-GIS (QGIS, ArcGIS)
- Einfache Struktur
- Gute Software-Unterstützung

**Nachteile**:
- **2GB-Dateigrenze** pro Datei
- **10-Zeichen-Limit** für Feldnamen
- Kein Unicode-Support
- Veraltetes dBASE-Format (1980er)
- Keine Topologie

**Alternative**: **GeoPackage** (empfohlen von OGC)

### WFS (Web Feature Service) - Der Standard (seit 2002)

**Entwickelt von**: OGC (Open Geospatial Consortium)
**Versionen**: 1.0 (2002), 1.1 (2005), 2.0 (2010), 3.0 → OGC API Features

**Funktionsweise**: Client-Server-Architektur über HTTP
- `GetCapabilities` - Dienst-Metadaten
- `DescribeFeatureType` - Schema-Informationen
- `GetFeature` - Daten abrufen
- `Transaction` - Daten schreiben (optional)

**Datenformat**: **GML** (Geography Markup Language), XML-basiert

**Vorteile**:
- Standardisiert durch OGC
- Transaktional (Insert/Update/Delete möglich)
- Komplexe Filter (FES - Filter Encoding Standard)
- Schema-basierte Validierung

**Nachteile**:
- Verbose (XML)
- Komplexe Implementierung
- Performance-Overhead

**Moderne Variante**: **OGC API - Features** (ehemals WFS 3.0)
- REST-API statt SOAP
- JSON/GeoJSON statt XML/GML
- Einfachere Implementierung

### GeoJSON - Der Web-Native (seit 2008/2016)

**Entwickelt von**: Community (2008), später IETF RFC 7946 (2016)

**Aufbau**: JSON-basiert, menschenlesbar
```json
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [13.404954, 52.520008]
    },
    "properties": {
      "name": "Berlin",
      "population": 3645000
    }
  }]
}
```

**Geometrietypen**: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection

**Koordinatensystem**: **Immer WGS84** (EPSG:4326) laut RFC 7946

**Vorteile**:
- Einfach und lesbar
- JavaScript-nativ
- Web-freundlich
- Schnell zu parsen

**Nachteile**:
- Nur WGS84 (keine CRS-Flexibilität)
- Größere Dateien als Shapefile
- Keine räumliche Indexierung

**Moderne Erweiterung**: **JSON-FG** (OGC Features and Geometries JSON)
- Löst CRS-Limitierung
- Behält GeoJSON-Kompatibilität

## Datenformat vs. Schema

Ein fundamentaler Unterschied:

### Datenformat (Container)
**WIE werden Daten gespeichert?**
- Shapefile: Binär + dBASE
- GML: XML-basiert
- GeoJSON: JSON-basiert

**Syntax, Encoding, Struktur**

### Schema (Inhalt)
**WAS bedeuten die Daten?**
- Welche Objektarten gibt es?
- Welche Attribute?
- Welche Datentypen?
- Welche Beziehungen?

**Semantik, Validierung, Interoperabilität**

**Beispiel**:
- **XPlanung** ist ein **Schema** (definiert Bebauungspläne, Festsetzungen, etc.)
- **GML** ist ein **Datenformat** (XML-Container)
- XPlanung kann in **GML** ODER **JSON-FG** codiert werden

## Schema-Hierarchie: Von OGC zu XLeitstelle

Die Geo-Standards bauen hierarchisch aufeinander auf:

```
┌─────────────────────────────────────────┐
│   ISO 19100 Serie (Normative Basis)    │
│   ISO 19109 (Feature Cataloguing)      │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│        OGC-Standards (Technisch)        │
│   - Simple Features (Geometrien)        │
│   - GML (XML-Encoding)                  │
│   - WFS (Webservice-Protokoll)          │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│    INSPIRE (EU-weit, 34 Themen)         │
│   - Land Use                            │
│   - Utility Networks                    │
│   - Buildings                           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│   XLeitstelle (Deutschland, fachspez.)  │
│   - XPlanung (Bauleitplanung)           │
│   - XBau (Baugenehmigung)               │
│   - XTrasse (Leitungsnetze)             │
│   - XBreitband (Telekommunikation)      │
└─────────────────────────────────────────┘
```

**OGC-Ebene**: Technische Grundlagen (WIE werden Geo-Daten ausgetauscht?)
**INSPIRE-Ebene**: Thematische Harmonisierung (WAS wird ausgetauscht - EU-weit?)
**XLeitstelle-Ebene**: Fachspezifische Ausprägung (Deutsche Bauplanung)

## WFS vs. GeoJSON für Datenaustausch

### Vergleichstabelle

| Aspekt | WFS 2.0 (klassisch) | GeoJSON + REST | OGC API Features (modern) |
|--------|---------------------|----------------|---------------------------|
| **Protokoll** | SOAP/XML | REST/HTTP | REST/HTTP |
| **Datenformat** | GML (XML) | GeoJSON (JSON) | JSON/GeoJSON |
| **Standardisierung** | OGC-Standard | Community-Standard → RFC 7946 | OGC-Standard |
| **Transaktionen** | Ja (Transaction) | Nein (proprietär) | Ja (POST/PUT/DELETE) |
| **Filter** | FES (komplexe Filter) | Query-Parameter (einfach) | CQL2 (mächtig, aber einfacher) |
| **Schema** | DescribeFeatureType (XML Schema) | Kein Standard | JSON Schema |
| **Performance** | Langsam (XML-Parsing) | Schnell (JSON) | Schnell (JSON) |
| **Komplexität** | Hoch | Niedrig | Mittel |
| **Web-Integration** | Umständlich | Nativ | Nativ |
| **GIS-Integration** | Ausgezeichnet | Gut | Sehr gut |

### Anwendungsfälle

**Wann WFS 2.0?**
- Desktop-GIS-Integration (QGIS, ArcGIS)
- Transaktionale Bearbeitung erforderlich
- INSPIRE-Compliance notwendig
- Komplexe räumliche Filter
- Legacy-Systeme

**Wann GeoJSON + REST?**
- Web-Anwendungen (Leaflet, Mapbox)
- Mobile Apps
- Einfache Visualisierung
- Schnelle Prototypen
- Moderne Microservices

**Wann OGC API Features?**
- **Moderne Geodateninfrastrukturen**
- Best-of-both-worlds (Standard + einfach)
- RESTful APIs
- JSON-Schema-Validierung
- Zukunftssicher

## XLeitstelle-Bereitstellung: XML und JSON

### Primärformat: GML (XML)

Die XLeitstelle-Standards (XPlanung, XBau, XTrasse, XBreitband) basieren auf:
- **GML 3.2.2** (ISO 19136)
- **XML-Schemas** (.xsd-Dateien)
- **UML-Modelle** (ISO 19109 - Feature Cataloguing)

**Vorteile**:
- Schema-basierte Validierung
- Komplexe Datenstrukturen
- INSPIRE-kompatibel

### JSON-Schema: JSON-FG (in Entwicklung)

**JSON-FG** (OGC Features and Geometries JSON):
- Löst GeoJSON-Limitierungen (CRS-Flexibilität)
- Behält GeoJSON-Kompatibilität
- **Veröffentlichung**: 2025 erwartet

**XLeitstelle-Unterstützung**:
- JSON-FG-Schemas in Entwicklung
- Abwärtskompatibilität zu GeoJSON

### Konvertierung: GML ↔ GeoJSON

**Tools**:
- **GDAL/ogr2ogr**: Kommandozeilen-Tool für Geo-Formate
- **ShapeChange**: Modellgetrieben (UML → XML Schema / JSON Schema)
- **FME**: Kommerzielle ETL-Software
- **QGIS**: Desktop-GIS mit Export-Funktionen

**Beispiel (ogr2ogr)**:
```bash
# GML → GeoJSON
ogr2ogr -f GeoJSON output.geojson input.gml

# Shapefile → GeoJSON
ogr2ogr -f GeoJSON -t_srs EPSG:4326 output.geojson input.shp
```

### XLeitstelle-Repositories

**GitLab OpenCode**: [gitlab.opencode.de/xleitstelle](https://gitlab.opencode.de/xleitstelle)
- **XML-Schemas**: XPlanung, XBau, XTrasse, XBreitband (.xsd)
- **Testdaten**: Beispieldaten in GML
- **Validierungsregeln**: Schematron-Regeln für semantische Prüfung
- **Tools**: XPlan-Validator, XML-Nachrichten-Generator

**XPlan-Validator** (online):
- Syntaktische Validierung (XML Schema)
- Semantische Validierung (Schematron)
- Geometrische Prüfung (Topologie)

## Relevanz für Wärmeplanung

### Datenquellen
- **ALKIS** (Kataster): NAS/XML → WFS
- **XPlanung** (Wärmepläne): GML → WFS oder GeoJSON
- **XTrasse** (Wärmenetze): GML → WFS oder GeoJSON

### Anwendungsfälle
- **Desktop-GIS** (QGIS): Shapefile, WFS
- **Web-Plattformen**: GeoJSON, OGC API Features
- **Datenbereitstellung**: WFS (INSPIRE-konform)
- **Visualisierung**: GeoJSON (Webkarten)

### Best Practice
1. **Primärdaten**: GML (XPlanung-konform)
2. **WFS-Dienst**: Für GIS-Zugriff
3. **GeoJSON-Export**: Für Web-Anwendungen
4. **Dokumentation**: Schemas und Metadaten

## Dokumente in diesem Bereich

### Deep Research: Shapefile, WFS, GeoJSON

**[Geo-Datenformate Deep Research - Shapefile, WFS, GeoJSON](2025-11-21_Geo-Datenformate-Shapefile-WFS-GeoJSON_Research.md)**

Umfassende Analyse der drei zentralen Geo-Datenformate mit detaillierter Beschreibung von Aufbau und Historie:
- **Shapefile**: ESRI-Format (1990er), Aufbau (.shp/.shx/.dbf/.prj), Limitierungen (2GB, 10-Zeichen-Feldnamen), Alternative GeoPackage
- **WFS**: OGC-Standard (2002-2010), Versionen 1.0/2.0/3.0, Operationen (GetCapabilities, GetFeature, Transaction), GML-basiert, Modernisierung zu OGC API Features
- **GeoJSON**: Community/IETF (2008/2016), RFC 7946, JSON-basiert, strikt WGS84, JSON-FG als Erweiterung

Erklärt fundamentale Konzepte:
- **Datenformat vs. Schema**: Container (GML, JSON) vs. Inhalt (XPlanung, ALKIS)
- **Schema-Hierarchie**: ISO 19100 → OGC → INSPIRE → XLeitstelle
- **WFS vs. GeoJSON**: Vergleichstabelle, Anwendungsfälle, OGC API Features als moderne Synthese
- **XLeitstelle-Bereitstellung**: XML-Schemas (GML), JSON-FG (in Entwicklung), Konvertierungstools (GDAL, ShapeChange)

Dokumentiert mit 60+ Primärquellen (OGC, IETF, ESRI, XLeitstelle, OpenCode).

## Externe Ressourcen

### Spezifikationen
- **Shapefile**: [ESRI Shapefile Technical Description](https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf)
- **GeoJSON**: [IETF RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946)
- **WFS 2.0**: [OGC WFS 2.0 Specification](https://www.ogc.org/standard/wfs/)
- **OGC API Features**: [OGC API - Features](https://ogcapi.ogc.org/features/)

### Tools
- **GDAL**: [gdal.org](https://gdal.org/)
- **QGIS**: [qgis.org](https://qgis.org/)
- **XPlan-Validator**: [XLeitstelle Validator](https://xleitstelle.de/xplanung/validierung)

### Repositories
- **XLeitstelle GitLab**: [gitlab.opencode.de/xleitstelle](https://gitlab.opencode.de/xleitstelle)

## Verwandte Bereiche

### Standards
- **[XPlanung](../xplanung/)** - Nutzt GML 3.2.2, WFS-Dienste
- **[XBau](../xbau/)** - XML-basiert (XÖV 3.0)
- **[XTrasse](../xtrasse/)** - GML-basiert, Leitungsnetze
- **[ALKIS](../alkis/)** - NAS/XML, WFS-Dienste

### Organisation
- **[XLeitstelle](../../stakeholder/bund/xleitstelle/)** - Entwicklung XML-Schemas, JSON-FG
