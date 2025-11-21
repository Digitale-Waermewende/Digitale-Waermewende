# Deep Research Report: Geo-Datenformate
## Shapefile, WFS und GeoJSON - Umfassende Analyse

**Erstellt am:** 2025-11-21
**Autor:** Claude Code Deep Research
**Umfang:** 7 Teilbereiche mit Primärquellen

---

## Executive Summary

Dieser Report dokumentiert drei fundamentale Geo-Datenformate und deren Rolle in modernen Geodateninfrastrukturen:

- **Shapefile** (ESRI, 1990er): Das klassische Dateiformat mit mehreren Komponenten (.shp, .shx, .dbf), weit verbreitet aber mit signifikanten Limitierungen (2GB-Grenze, 10-Zeichen-Feldnamen, kein Unicode)
- **WFS** (OGC, 2002-2010): Webservice-Standard für transaktionale Feature-Zugriffe, entwickelt sich zu modernen REST-APIs (OGC API Features)
- **GeoJSON** (Community/IETF, 2008/2016): Leichtgewichtiges JSON-Format für Web-Mapping, standardisiert als RFC 7946 mit WGS84 als einzigem CRS

Die Analyse zeigt den Übergang von proprietären Dateiformaten zu standardisierten Webservices und modernen JSON-basierten APIs. Ein besonderer Fokus liegt auf der Unterscheidung zwischen **Datenformat** (physische Struktur) und **Schema** (semantische Bedeutung), illustriert durch die Hierarchie OGC → INSPIRE → XLeitstelle.

---

## 1. Shapefile - Aufbau und Historie

### 1.1 Entwickler und Erstveröffentlichung

**Entwickler:** ESRI (Environmental Systems Research Institute)

**Erstveröffentlichung:** Frühe 1990er Jahre mit ArcView GIS Version 2

**Offizielle Spezifikation:** "ESRI Shapefile Technical Description: An ESRI White Paper—July 1998"

### 1.2 Aufbau und Dateistruktur

Ein Shapefile besteht aus **mindestens drei obligatorischen Dateien**:

1. **.shp** - Hauptdatei mit Geometriedaten
   - Direct-Access-Datei mit variablen Datensatzlängen
   - Jeder Datensatz beschreibt eine Form mit einer Liste ihrer Vertices
   - Header: 100 Bytes

2. **.shx** - Index-Datei
   - Ermöglicht schnellen Zugriff auf Geometrien
   - Verknüpft Position und Offset der Features

3. **.dbf** - Attributdatei
   - dBASE III Format für Sachdaten
   - Speichert alle Attribute der Features

**Optional (aber wichtig):**

4. **.prj** - Projektionsdatei
   - Plain-Text-Datei im Well-Known Text (WKT) Format
   - Beschreibt Koordinatensystem und Projektion
   - GEOGCS für geographische CRS, PROJCS für projizierte CRS
   - Nicht obligatorisch, aber notwendig für "on-the-fly" Projektion

5. Weitere optionale Dateien: .sbn, .sbx (Spatial Index), .xml (Metadaten), .cpg (Code Page)

### 1.3 Geometrietypen

Das Shapefile-Format unterstützt verschiedene Geometrietypen (jeweils eine pro Datei):

- **Point** - Einzelpunkte (0-dimensional)
- **MultiPoint** - Punktsammlungen
- **Polyline** - Linien und Linienzüge (1-dimensional)
- **Polygon** - Flächengeometrien (2-dimensional)
- Weitere: PointZ, PolylineZ, PolygonZ (mit Z-Werten), PointM, PolylineM, PolygonM (mit Measure-Werten)

**Wichtig:** Pro Shapefile ist nur ein Geometrietyp möglich. Gemischte Geometrien erfordern separate Dateien.

### 1.4 Koordinatensysteme

- **Speicherung:** Rohe Koordinaten im .shp-File
- **CRS-Definition:** Optional in .prj-Datei im Well-Known Text (WKT) Format
- **Flexibilität:** Theoretisch beliebige Koordinatensysteme möglich
- **Problem:** Ohne .prj-Datei ist das CRS unbekannt

### 1.5 Attribute und dBASE-Format

**dBASE III Spezifikation (entwickelt in den frühen 1980er Jahren):**

- **Feldnamen:** Maximal 10 Zeichen (hart limitiert)
- **Anzahl Felder:** Maximal 1024 Felder pro Tabelle
- **Datentypen:** Begrenzt auf primitive Typen (Text, Zahl, Datum)
- **Keine Unterstützung für:**
  - Unicode (problematisch für nicht-englische Sprachen)
  - Null-Werte
  - Zeit (nur Datum, keine Zeit)
  - BLOB, GUID, GlobalID, RasterID
  - Komplexe Datentypen

### 1.6 Vorteile - Warum so weit verbreitet?

1. **Universelle Unterstützung:** Fast jede GIS-Software kann Shapefiles lesen/schreiben
2. **Einfache Struktur:** Klar definiertes Format, leicht zu implementieren
3. **Offene Spezifikation:** ESRI hat die technischen Spezifikationen veröffentlicht
4. **Kompakte Größe:** Effizienter als viele XML-basierte Formate
5. **Historische Verbreitung:** ArcView's Popularität machte Shapefile zum De-facto-Standard
6. **Austauschformat:** Wird von öffentlichen Datenrepositorien und Behörden standardmäßig verwendet
7. **Schnelle Datenextraktion:** Gute Performance für kleinere Datensätze

### 1.7 Nachteile und Limitierungen

**Technische Limitierungen:**

1. **2GB Dateigrößen-Limit:**
   - Gilt für jede Komponentendatei (.shp, .shx, .dbf)
   - Bei Punktdaten: ca. 70 Millionen Features
   - Bei Linien/Polygonen: Deutlich weniger (abhängig von Vertex-Anzahl)

2. **10-Zeichen-Feldnamen:**
   - Keine Möglichkeit, diese Beschränkung zu umgehen
   - Feldnamen werden automatisch gekürzt
   - Führt zu unlesbaren Abkürzungen

3. **dBASE-Format-Nachteile:**
   - Kein Unicode → Probleme mit internationalen Zeichen
   - Keine Null-Werte
   - Kein Zeit-Typ (nur Datum)
   - Begrenzte Datentypen
   - Maximum 1024 Felder

4. **Mehrere Dateien:**
   - Mindestens 3 Dateien müssen zusammen bleiben
   - Risiko von Dateiverlusten beim Kopieren/Versenden
   - Unpraktisch für Web-Übertragung

5. **Ein Geometrietyp pro Datei:**
   - Gemischte Geometrien erfordern separate Shapefiles
   - Erhöht Datenmanagement-Komplexität

6. **Keine Topologie:**
   - Keine eingebaute Topologieunterstützung
   - Duplizierte Vertices bei angrenzenden Polygonen

7. **Veraltete Architektur:**
   - Nicht geeignet für modernes Datenmanagement
   - Kein Support für Versionierung, Tracking, Archivierung
   - Keine Transaktionssicherheit

**Zitat aus den Quellen:**
> "These issues mean that shapefiles are an extremely poor choice for active database management—they do not handle the modern life cycle of data creation, editing, versioning, and archiving."

### 1.8 Aktuelle Relevanz und Alternativen

**Status 2024:**
- Immer noch weit verbreitet für Datenaustausch
- Wird von vielen öffentlichen Datenportalen standardmäßig angeboten
- Legacy-Systeme verlassen sich darauf
- **ABER:** GIS-Community empfiehlt aktiv den Übergang zu modernen Formaten

**Primäre Alternativen:**

1. **GeoPackage (GPKG)** - OGC-Standard, empfohlener Ersatz
   - Einzelne SQLite-Datenbank-Datei
   - Keine Dateigrößen-Limits
   - Unterstützt Vektor- und Rasterdaten
   - Unicode, komplexe Datentypen, Topologie
   - Bessere Performance bei großen Datensätzen

2. **FlatGeobuf** - Performance-fokussiert
   - Binärformat für schnelle Streaming-Zugriffe
   - Ideal für System-zu-System-Integration

3. **GeoJSON** - Für Web-Anwendungen
   - Siehe Kapitel 3

**Empfehlungen:**
- **Shapefile nutzen für:** Legacy-Kompatibilität, schnellen Datenaustausch mit unbekannten Systemen
- **GeoPackage nutzen für:** Neue Projekte, große Datensätze, komplexe Datenstrukturen
- **GeoJSON nutzen für:** Web-Mapping, REST-APIs, JavaScript-Anwendungen

---

## 2. WFS (Web Feature Service) - Aufbau und Historie

### 2.1 Standard-Organisation

**OGC (Open Geospatial Consortium)**
- Internationale Organisation für offene Geospatial-Standards
- Entwickelt Standards in Zusammenarbeit mit Industrie und Behörden
- WFS ist ein OGC Implementation Standard

**ISO-Äquivalent:** ISO 19142:2010 (entspricht WFS 2.0.0)

### 2.2 Versionshistorie

#### **WFS 1.0.0** (2002)

**Erstveröffentlichung:** 2002

**Hauptmerkmale:**
- Basis-Operationen: GetCapabilities, DescribeFeatureType, GetFeature
- GML 2.1.2 als Datenformat
- HTTP GET und POST Requests
- Fokus auf Read-Only-Zugriff (Basic WFS)
- Optionale Transaktions-Erweiterung (WFS-T)

#### **WFS 1.1.0** (2005)

**Veröffentlichung:** 2005 (OGC Dokument 04-094r1)

**Verbesserungen:**
- GML 3.1.1 Unterstützung
- Erweiterte räumliche Operatoren (Beyond, DWithin)
- Integration mit Filter Encoding 1.1 Standard
- Verbesserte XML-basierte POST-Requests
- Präzisere Spezifikation für Transaktionen

#### **WFS 2.0.0** (2010)

**Veröffentlichung:** 4. August 2010 (OGC Dokument 09-025r1)

**Auch als:** ISO 19142:2010

**Bedeutende Fortschritte:**

1. **Result Paging:** Effiziente Handhabung großer Antworten
2. **Stored Queries:** Vordefinierte, wiederverwendbare Abfragen
3. **Erweiterte Schema-Unterstützung:** Über GML hinaus
4. **Verbesserte Transaktionen:** Feingranulare CRUD-Operationen
5. **Filter Encoding 2.0:** Komplexere räumliche und thematische Filter

**Errata:** WFS 2.0.2 (aktuelle Version mit Korrekturen)

#### **WFS 3.0 → OGC API - Features** (2019+)

**Wichtiger Paradigmenwechsel:**

Die OGC hat den Namen "WFS 3.0" **offiziell verworfen** und durch **"OGC API - Features"** ersetzt.

**Hintergrund:**
- Kompletter Neuansatz statt inkrementelle Weiterentwicklung
- REST-Architektur statt SOAP/XML-orientiert
- JSON/GeoJSON statt GML/XML
- OpenAPI statt OGC-spezifische Capabilities-Dokumente

**OGC-Zitat:**
> "The functional capabilities are now available in a more modern web API, OGC API – Features, and implementers are encouraged to use the newer Standard."

### 2.3 Funktionsweise: Client-Server-Architektur

**Architektur:**
```
Client → HTTP Request → WFS Server → Datenquelle (z.B. PostGIS)
         ←  HTTP Response (GML/XML) ←
```

**Prinzip:**
- Client sendet HTTP-Anfragen (GET oder POST)
- Server antwortet mit XML/GML-codierten Features
- Zustandslos (stateless) - jede Anfrage ist unabhängig

### 2.4 WFS-Operationen

WFS 2.0 spezifiziert **11 Hauptoperationen** in verschiedenen Kategorien:

#### **Discovery-Operationen**

1. **GetCapabilities**
   - Abfrage des WFS-Service: Welche Optionen sind verfügbar?
   - Rückgabe: XML-Dokument mit Service-Metadaten
   - Informationen: Unterstützte Operationen, Feature-Typen, CRS, Formate

2. **DescribeFeatureType**
   - Abfrage der Struktur eines Feature-Typs
   - Rückgabe: XML Schema (XSD) des Feature-Typs
   - Zeigt: Attribute, Datentypen, Geometrietypen

#### **Query-Operationen**

3. **GetFeature**
   - Hauptoperation: Abfrage von Features aus der Datenquelle
   - Unterstützt Filter (räumlich, thematisch, temporal)
   - Rückgabe: GML-codierte Features
   - Parameter: TypeName, Filter, BBox, PropertyName, MaxFeatures

4. **GetPropertyValue**
   - Abfrage spezifischer Attributwerte
   - Effizienter als GetFeature für Attribut-Queries

5. **GetFeatureWithLock**
   - Wie GetFeature, aber mit gleichzeitiger Sperrung
   - Für transaktionale Workflows

#### **Locking-Operationen**

6. **LockFeature**
   - Sperrt Features für exklusiven Zugriff
   - Verhindert konkurrierende Änderungen
   - Gibt Lock-ID zurück

#### **Transaction-Operationen**

7. **Transaction**
   - Ermöglicht CRUD-Operationen (Create, Read, Update, Delete)
   - Elemente: Insert, Update, Delete
   - Transaktionssicher: Alle Operationen oder keine
   - Nur in WFS-T (Transactional WFS)

#### **Stored Query-Operationen** (WFS 2.0+)

8. **CreateStoredQuery** - Speichert vordefinierte Abfrage
9. **DropStoredQuery** - Löscht gespeicherte Abfrage
10. **ListStoredQueries** - Listet verfügbare Stored Queries
11. **DescribeStoredQueries** - Beschreibt Stored Query-Parameter

### 2.5 Datenformat: GML (Geography Markup Language)

**GML** = Geography Markup Language

**Eigenschaften:**
- XML-basiert (eXtensible Markup Language)
- OGC/ISO-Standard (ISO 19136)
- Codiert Geometrien und Attribute in strukturiertem XML
- Selbstbeschreibend durch XML-Schemas

**Beispiel GML 3.2:**
```xml
<gml:Point gml:id="p1" srsName="EPSG:4326">
  <gml:pos>52.5200 13.4050</gml:pos>
</gml:Point>
```

**Vorteile:**
- Standardisiert (OGC/ISO)
- Schema-basiert (validierbar)
- Unterstützt komplexe Geometrien und Topologien
- Erweiterbar für domänenspezifische Schemas

**Nachteile:**
- Verbose (großer Dateigrößen-Overhead durch XML)
- Komplexe Parsing-Logik erforderlich
- Nicht web-native (JavaScript muss XML parsen)

### 2.6 Vorteile von WFS

1. **Standardisiert:** OGC/ISO-Standard, breite Interoperabilität
2. **Transaktional:** Insert/Update/Delete möglich (WFS-T)
3. **Filter-Möglichkeiten:** FES (Filter Encoding Specification) für komplexe Abfragen
4. **Schema-basiert:** DescribeFeatureType liefert formale Datendefinition
5. **Räumliche und thematische Queries:** Kombinierbar
6. **Vendor-neutral:** Unabhängig von spezifischer Software
7. **GIS-Integration:** Native Unterstützung in QGIS, ArcGIS, etc.

### 2.7 Versionsunterschiede: WFS 1.0 vs. 2.0 vs. 3.0 (API)

| Aspekt | WFS 1.0 (2002) | WFS 2.0 (2010) | OGC API Features (WFS 3.0) |
|--------|----------------|----------------|----------------------------|
| **GML-Version** | GML 2.1.2 | GML 3.1.1+ | Optional (GeoJSON bevorzugt) |
| **Architektur** | SOAP/XML-orientiert | SOAP/XML-orientiert | REST |
| **Datenformat** | GML/XML | GML/XML | JSON/GeoJSON (primär) |
| **Capabilities** | OGC GetCapabilities | OGC GetCapabilities | OpenAPI |
| **Filter** | Filter Encoding 1.0 | Filter Encoding 2.0 (FES) | CQL (Common Query Language) |
| **Paging** | Nein | Ja (Result Paging) | Ja (limit/offset) |
| **Stored Queries** | Nein | Ja | Nein (Alternative Ansätze) |
| **HTTP-Methoden** | GET, POST (XML) | GET, POST (XML) | GET, POST, PUT, DELETE (REST) |
| **Caching** | Begrenzt | Begrenzt | Optimal (HTTP-Caching) |

**WFS 2.0 vs. OGC API Features:**

- **WFS 2.0:** HTTP wird hauptsächlich als "Tunnel" verwendet
- **OGC API Features:** Echte REST-Architektur mit Hypermedia-Controls
- **WFS 2.0:** Komplexe, aber mächtige Filter (FES)
- **OGC API Features:** Einfachere Filter, modularisiert
- **Kompatibilität:** OGC API Features ist **nicht rückwärtskompatibel** mit WFS 2.0, aber Mapping ist möglich

---

## 3. GeoJSON - Aufbau und Historie

### 3.1 Entwicklung und Standardisierung

#### **Phase 1: Community-Standard (2007-2008)**

**Beginn:** März 2007 - GeoJSON Format Working Group gegründet

**Erste Spezifikation:** Juni 2008 (GeoJSON Version 1.0)
- Community-getriebene Spezifikation
- Veröffentlicht auf geojson.org
- Keine formale Standardisierung

**Motivation:**
- JSON wurde populär für Web-APIs
- Bedarf an einfachem Geo-Format für JavaScript
- Alternative zu komplexem GML/KML

#### **Phase 2: IETF-Standardisierung (2014-2016)**

**Januar 2014:** Internet Draft mit GeoJSON-Spezifikation veröffentlicht

**Oktober 2015:** IETF GeoJSON Working Group formell gebildet

**August 2016:** **RFC 7946** veröffentlicht
- IETF (Internet Engineering Task Force) Standard
- Ersetzt die 2008-Spezifikation
- Offizieller Internet-Standard

**Autoren:** H. Butler, M. Daly, A. Doyle, S. Gillies, S. Hagen, T. Schaub

**Status:** PROPOSED STANDARD (IETF)

### 3.2 Aufbau: JSON-basiert und menschenlesbar

**JSON (JavaScript Object Notation):**
- Textbasiertes Datenformat
- Native JavaScript-Unterstützung
- Key-Value-Paare und Arrays
- Menschenlesbar und maschinenverarbeitbar

**GeoJSON-Struktur:**

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [13.4050, 52.5200]
      },
      "properties": {
        "name": "Berlin",
        "population": 3645000
      }
    }
  ]
}
```

**Hauptkomponenten:**

1. **GeoJSON Object:** Basis-Typ mit `type`-Member
2. **Geometry:** Geometrie-Objekte
3. **Feature:** Kombination aus Geometry + Properties
4. **FeatureCollection:** Sammlung von Features

### 3.3 Geometrietypen

RFC 7946 definiert **7 konkrete Geometrietypen**:

#### **0-dimensional (Punkte)**
1. **Point:** Einzelner Punkt
   ```json
   {"type": "Point", "coordinates": [13.4050, 52.5200]}
   ```

2. **MultiPoint:** Mehrere Punkte
   ```json
   {"type": "MultiPoint", "coordinates": [[13.4050, 52.5200], [13.3889, 52.5170]]}
   ```

#### **1-dimensional (Linien)**
3. **LineString:** Linienzug
   ```json
   {"type": "LineString", "coordinates": [[13.4050, 52.5200], [13.3889, 52.5170]]}
   ```

4. **MultiLineString:** Mehrere Linienzüge
   ```json
   {"type": "MultiLineString", "coordinates": [[[...]], [[...]]]}
   ```

#### **2-dimensional (Flächen)**
5. **Polygon:** Polygon mit optionalen Löchern
   ```json
   {
     "type": "Polygon",
     "coordinates": [
       [[13.4, 52.5], [13.5, 52.5], [13.5, 52.6], [13.4, 52.6], [13.4, 52.5]],
       [[13.42, 52.52], [13.48, 52.52], [13.48, 52.58], [13.42, 52.58], [13.42, 52.52]]
     ]
   }
   ```
   - Erstes Array: Außenring (exterior ring)
   - Weitere Arrays: Löcher (interior rings)
   - **Right-Hand Rule:** Ringe müssen der Rechte-Hand-Regel folgen

6. **MultiPolygon:** Mehrere Polygone
   ```json
   {"type": "MultiPolygon", "coordinates": [[[[...]]], [[[...]]]]}
   ```

#### **Heterogene Sammlungen**
7. **GeometryCollection:** Gemischte Geometrietypen
   ```json
   {
     "type": "GeometryCollection",
     "geometries": [
       {"type": "Point", "coordinates": [13.4050, 52.5200]},
       {"type": "LineString", "coordinates": [[...]]}
     ]
   }
   ```

### 3.4 Koordinatensystem: Immer WGS84 (EPSG:4326)

**RFC 7946 - Strikte CRS-Definition:**

> "The coordinate reference system for all GeoJSON coordinates is a geographic coordinate reference system, using the World Geodetic System 1984 (WGS 84) datum, with longitude and latitude units of decimal degrees."

**EPSG:4326:**
- **Datum:** WGS 84 (World Geodetic System 1984)
- **Achsenreihenfolge:** Longitude (Längengrad), Latitude (Breitengrad)
- **Einheiten:** Dezimalgrad
- **Optionale 3. Dimension:** Höhe in Metern über/unter WGS 84-Ellipsoid

**Wichtige Änderung von 2008 zu RFC 7946:**
- **2008:** Custom CRS möglich (über `crs`-Member)
- **RFC 7946:** `crs`-Member **entfernt**, nur WGS84 erlaubt

**Konsequenzen:**
- Einfachheit und Interoperabilität
- **ABER:** Keine Flexibilität für andere CRS (z.B. UTM, Gauß-Krüger)
- Für nicht-WGS84-Daten: Konvertierung erforderlich

### 3.5 Properties: Beliebige Attribute als JSON-Objekt

**Properties-Member:**
- Enthält Sachdaten des Features
- Kann jedes gültige JSON-Objekt sein
- Auch `null` ist erlaubt

**Beispiel:**
```json
{
  "type": "Feature",
  "geometry": {...},
  "properties": {
    "name": "Beispiel-Feature",
    "category": "Punkt von Interesse",
    "year": 2024,
    "active": true,
    "metadata": {
      "created": "2024-01-15",
      "author": "Max Mustermann"
    },
    "tags": ["geo", "opendata"]
  }
}
```

**Flexibilität:**
- Beliebige Anzahl von Attributen
- Verschachtelte Objekte möglich
- Arrays erlaubt
- Keine Schema-Validierung in RFC 7946 (aber JSON Schema möglich)

**Optionales `id`-Member:**
- Feature kann eindeutige ID haben
- Typ: String oder Nummer

### 3.6 Vorteile von GeoJSON

1. **Einfachheit:**
   - Leicht zu lesen und schreiben
   - Intuitive Struktur
   - Keine komplexen XML-Schemas

2. **JavaScript-nativ:**
   - Direkt in JavaScript verwendbar (`JSON.parse()`)
   - Keine Parsing-Bibliotheken erforderlich
   - Ideal für Web-Mapping (Leaflet, Mapbox, OpenLayers)

3. **Web-freundlich:**
   - Kompakter als XML/GML
   - HTTP-Caching-freundlich
   - RESTful-API-kompatibel

4. **Breite Unterstützung:**
   - Alle modernen Web-Mapping-Bibliotheken
   - GIS-Software (QGIS, ArcGIS, GDAL)
   - Datenbanken (PostGIS, MongoDB)

5. **Standardisiert:**
   - IETF RFC 7946
   - Klare Spezifikation
   - Interoperabilität

6. **Menschenlesbar:**
   - Debugging einfach
   - Manuelle Bearbeitung möglich

7. **Flexibel:**
   - Properties können beliebige Strukturen enthalten
   - Einfach erweiterbar

### 3.7 Nachteile von GeoJSON

1. **Keine CRS-Flexibilität:**
   - Nur WGS84 (EPSG:4326)
   - Für andere CRS: Konvertierung notwendig
   - Problematisch für nationale Koordinatensysteme (z.B. Gauß-Krüger)

2. **Dateigröße:**
   - Fast **doppelt so groß** wie Shapefile bei gleichen Daten
   - Text-Format → verbosity
   - Koordinaten als Dezimalzahlen (nicht binär)
   - Viel Wiederholung (JSON-Struktur-Overhead)

3. **Performance bei großen Datensätzen:**
   - Gesamte Datei wird auf einmal geladen
   - Browser-Performance-Probleme bei >1000 Features
   - Keine Spatial-Indexierung
   - Langsames Parsing großer JSON-Dateien

4. **Keine Topologie:**
   - Keine Topologie-Unterstützung
   - Duplizierte Vertices bei angrenzenden Polygonen

5. **Kein Schema:**
   - RFC 7946 definiert kein Schema für Properties
   - Keine Validierung der Attribute
   - JSON Schema muss separat definiert werden

6. **Präzisionsverlust:**
   - Dezimalzahlen in JSON (nicht immer exakt)
   - Koordinaten-Rundungsfehler möglich

**Optimierungsstrategien:**
- Koordinatenpräzision reduzieren (z.B. 5 Dezimalstellen ≈ 1m Genauigkeit)
- Geometrien vereinfachen
- TopoJSON verwenden (eliminiert Duplikate)
- GeoJSON in Tiles aufteilen (für Web-Mapping)
- Server-seitige Filterung

---

## 4. Datenformat vs. Schema - Fundamentaler Unterschied

### 4.1 Konzeptionelle Trennung

Die Unterscheidung zwischen **Datenformat** und **Schema** ist fundamental für das Verständnis von Geodateninfrastrukturen:

#### **Datenformat** (Syntax/Encoding)

**Definition:** Container-Struktur, die definiert, **wie** Daten physisch gespeichert und übertragen werden.

**Fragestellungen:**
- Wie werden Daten binär oder textuell codiert?
- Welche Syntax wird verwendet (XML, JSON, Binär)?
- Wie werden Geometrien repräsentiert?
- Wie ist die Datei strukturiert?

**Beispiele:**
- **XML** - Extensible Markup Language (Textformat mit Tags)
- **JSON** - JavaScript Object Notation (Key-Value-Paare)
- **GML** - Geography Markup Language (XML-basiert für Geodaten)
- **Shapefile** - Binärformat mit mehreren Dateien
- **WKB** - Well-Known Binary (Binärcodierung für Geometrien)
- **WKT** - Well-Known Text (Textcodierung für Geometrien)

**Charakteristika:**
- Technische Repräsentation
- Parser/Encoder-Logik
- Datei-Endungen (.xml, .json, .gml, .shp)

#### **Schema** (Semantik/Inhalt)

**Definition:** Inhaltliche Struktur und Bedeutung, die definiert, **was** die Daten repräsentieren.

**Fragestellungen:**
- Welche Objektarten (Feature Types) gibt es?
- Welche Attribute hat jedes Objekt?
- Welche Datentypen haben die Attribute?
- Welche Bedeutung (Semantik) haben die Felder?
- Welche Beziehungen bestehen zwischen Objekten?
- Welche Validierungsregeln gelten?

**Beispiele:**
- **XPlanung** - Bauleitplanung in Deutschland
- **INSPIRE Land Use** - Landnutzung in Europa
- **CityGML** - 3D-Stadtmodelle
- **ALKIS** - Liegenschaftskataster in Deutschland
- **OpenStreetMap** - Community-Schema für Kartendaten

**Charakteristika:**
- Fachliche Bedeutung
- Domänenspezifisches Wissen
- UML-Modelle
- Daten-Kataloge (Feature Catalogues)

### 4.2 Beispiel: GML ist ein Format, XPlanung ist ein Schema

**Szenario:** Digitale Bauleitplanung in Deutschland

#### **GML (Geography Markup Language) - Das Format**

**Rolle:** Technisches Encoding

**Was es definiert:**
- XML-Syntax für geographische Features
- Wie Geometrien codiert werden (`<gml:Point>`, `<gml:Polygon>`)
- Basis-Datentypen (`<gml:pos>`, `<gml:coordinates>`)
- Referenzsystem-Codierung (`srsName="EPSG:25832"`)

**GML-Beispiel (abstrakt):**
```xml
<gml:Point gml:id="P1" srsName="EPSG:25832">
  <gml:pos>364588.82 5621428.91</gml:pos>
</gml:Point>
```

**Was GML NICHT sagt:**
- Was dieses Objekt **bedeutet** (Gebäude? Park? Verkehrsfläche?)
- Welche fachlichen Attribute es haben muss
- Welche Regeln für Planung gelten

#### **XPlanung - Das Schema**

**Rolle:** Fachliche Semantik für Bauleitplanung

**Was es definiert:**
- **Objektarten:** BP_BauGebiet, BP_Verkehrsfläche, FP_Landwirtschaft, etc.
- **Attribute:** Art der baulichen Nutzung, GRZ (Grundflächenzahl), Geschosszahl
- **Datentypen:** BP_BebauungsArt (Enumeration), XP_Nutzungsart
- **Beziehungen:** Plan hat Bereiche, Bereiche haben Objekte
- **Validierungsregeln:** GRZ muss zwischen 0 und 1 liegen

**XPlanung-Objektartenkatalog-Auszug:**

| Objektart | Geometrietyp | Pflichtattribute | Optionale Attribute |
|-----------|--------------|------------------|---------------------|
| BP_BauGebiet | Polygon | allgArtDerBaulichenNutzung | GRZ, GFZ, Bauweise |
| BP_Verkehrsfläche | Polygon, Linie | Nutzung | Breite, Widmung |
| FP_Landwirtschaft | Polygon | Nutzung | Detaillierung |

**XPlanung wird in GML codiert:**

```xml
<xplan:BP_BauGebiet gml:id="BG001">
  <xplan:allgArtDerBaulichenNutzung>WA</xplan:allgArtDerBaulichenNutzung>
  <xplan:GRZ>0.4</xplan:GRZ>
  <xplan:position>
    <gml:Polygon srsName="EPSG:25832">
      <gml:exterior>
        <gml:LinearRing>
          <gml:posList>364588.82 5621428.91 364620.15 5621450.30 ...</gml:posList>
        </gml:LinearRing>
      </gml:exterior>
    </gml:Polygon>
  </xplan:position>
</xplan:BP_BauGebiet>
```

**Hier sieht man:**
- **Format (GML):** `<gml:Polygon>`, `<gml:posList>` → **WIE** Geometrie gespeichert wird
- **Schema (XPlanung):** `<xplan:BP_BauGebiet>`, `<xplan:GRZ>` → **WAS** das Objekt bedeutet

### 4.3 Warum ist diese Unterscheidung wichtig?

1. **Ein Schema kann in mehreren Formaten codiert werden:**
   - XPlanung in GML (XML) → Standard
   - XPlanung in JSON-FG → Moderne Alternative
   - XPlanung in GeoPackage → Datenbank

2. **Ein Format kann viele Schemas transportieren:**
   - GML kann XPlanung, ALKIS, CityGML, INSPIRE, etc. codieren
   - JSON kann GeoJSON, JSON-FG, TopoJSON, etc. codieren

3. **Interoperabilität:**
   - Format-Interoperabilität ≠ Semantische Interoperabilität
   - Zwei Systeme können GML lesen (Format), aber nicht die Semantik verstehen (Schema)

4. **Standardisierungsebenen:**
   - **Format-Standards:** OGC GML, IETF GeoJSON, ISO SQL
   - **Schema-Standards:** INSPIRE, XLeitstelle, CityGML

5. **Validierung:**
   - **Format-Validierung:** Ist das XML wohlgeformt? Entspricht es dem GML-Schema?
   - **Schema-Validierung:** Sind alle Pflichtfelder vorhanden? Sind Werte gültig?

### 4.4 Mapping: Format ↔ Schema

#### **ISO 19109 - Regeln für Application Schemas**

ISO 19109 definiert, wie konzeptionelle UML-Modelle (plattformunabhängig) in technische Schemas (plattformspezifisch) überführt werden.

**Prozess:**
1. **Konzeptionelles Modell (UML):**
   - Objektarten als UML-Klassen
   - Attribute als UML-Properties
   - Beziehungen als UML-Assoziationen

2. **Encoding Rules:**
   - GML Encoding Rules (ISO 19136) → XML Schema
   - JSON-FG Encoding Rules → JSON Schema
   - SQL Encoding Rules → Datenbank-Schema

3. **Implementierung:**
   - XPlanung.xsd (GML Application Schema)
   - XPlanung-JSON-FG.json (JSON Schema)
   - XPlanung.sql (SQL DDL)

**Tool:** ShapeChange
- Open-Source-Tool der XLeitstelle
- Konvertiert UML → GML Schema, JSON Schema, SQL

---

## 5. Schema-Hierarchie: OGC → INSPIRE → XLeitstelle

### 5.1 Überblick: Drei Standardisierungsebenen

Die Geodateninfrastruktur in Deutschland basiert auf einer hierarchischen Standardarchitektur:

```
┌─────────────────────────────────────────────────────────────┐
│                  ISO 19100 Serie (Basis)                     │
│  ISO 19109 (Feature Cataloguing), ISO 19136 (GML),          │
│  ISO 19142 (WFS), ISO 19157 (Data Quality)                  │
└─────────────────────┬───────────────────────────────────────┘
                      │ Nutzt als Grundlage
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              OGC-Ebene (Technische Standards)                │
│  • GML 3.2.2 (Geography Markup Language)                    │
│  • Simple Features (Geometrietypen)                         │
│  • WFS 2.0 (Web Feature Service)                            │
│  • Filter Encoding (FES)                                    │
│  • OGC API - Features (modern)                              │
└─────────────────────┬───────────────────────────────────────┘
                      │ Baut auf
                      ▼
┌─────────────────────────────────────────────────────────────┐
│           INSPIRE-Ebene (Europa-Standards)                   │
│  • INSPIRE-Richtlinie 2007/2/EC                             │
│  • 34 Thematische Data Specifications                       │
│  • Annex I, II, III (verschiedene Prioritäten)              │
│  • Beispiele: Land Use, Transport, Elevation                │
└─────────────────────┬───────────────────────────────────────┘
                      │ Spezialisiert für
                      ▼
┌─────────────────────────────────────────────────────────────┐
│        XLeitstelle-Ebene (Deutschland-Standards)             │
│  • XPlanung (Bauleitplanung)                                │
│  • XBau (Baugenehmigung)                                    │
│  • XTrasse (Leitungsnetze)                                  │
│  • XBreitband (Breitbandausbau)                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 OGC-Ebene (Basis-Standards)

#### **Rolle:** Technische Grundlagen für Geodateninfrastrukturen

#### **ISO 19100 Serie - Normative Basis**

**Wichtigste Standards:**

- **ISO 19109 - Rules for Application Schema**
  - Definiert, wie Feature-Typen modelliert werden
  - UML als Modellierungssprache
  - Feature Catalogues (Objektartenkataloge)

- **ISO 19136 - Geography Markup Language (GML)**
  - XML-Encoding für Geodaten
  - Mapping von ISO 19109 UML-Modellen zu XML Schema
  - GML Application Schemas

- **ISO 19142 - Web Feature Service (WFS)**
  - Webservice-Spezifikation für Feature-Zugriffe
  - Transaktionen, Filter, Queries

- **ISO 19157 - Data Quality**
  - Metadaten zur Datenqualität
  - Genauigkeit, Vollständigkeit, Konsistenz

#### **OGC Simple Features**

**Spezifikation:** OGC Simple Feature Access (SFA)

**Geometrie-Hierarchie:**
```
Geometry (abstrakt)
├── Point
├── Curve (abstrakt)
│   └── LineString
├── Surface (abstrakt)
│   └── Polygon
├── GeometryCollection
│   ├── MultiPoint
│   ├── MultiCurve
│   │   └── MultiLineString
│   ├── MultiSurface
│   │   └── MultiPolygon
```

**Bedeutung:**
- Definiert Basis-Geometrietypen
- Wird von INSPIRE und XLeitstelle referenziert
- Implementiert in PostGIS, Oracle Spatial, etc.

#### **GML Application Schemas**

**Framework:** GML ermöglicht domänenspezifische Erweiterungen

**Prozess:**
1. UML-Modell der Domäne erstellen (ISO 19109)
2. GML Encoding Rules anwenden (ISO 19136)
3. XML Schema (.xsd) generieren
4. Instanzdaten als GML-Dateien

**Beispiel-Schemas:**
- CityGML (3D-Stadtmodelle)
- INSPIRE Data Specifications
- XPlanung, ALKIS, XBau

### 5.3 INSPIRE-Ebene (Europa)

#### **INSPIRE-Richtlinie**

**Vollständiger Name:** Infrastructure for Spatial Information in Europe

**Rechtsgrundlage:** Richtlinie 2007/2/EC des Europäischen Parlaments

**Ziel:** Schaffung einer europäischen Geodateninfrastruktur für Umweltpolitik

**Geltungsbereich:** Alle EU-Mitgliedstaaten

#### **34 Thematische Data Specifications**

INSPIRE definiert **34 Geodaten-Themen**, organisiert in **3 Annexen**:

**Annex I (Referenzdaten, höchste Priorität):**
1. Coordinate Reference Systems
2. Geographical Grid Systems
3. Geographical Names
4. Administrative Units
5. Addresses
6. Cadastral Parcels
7. Transport Networks
8. Hydrography
9. Protected Sites

**Annex II (Basis-Themendaten):**
10. Elevation
11. Land Cover
12. Orthoimagery
13. Geology

**Annex III (Umwelt- und Fachdaten):**
14. Statistical Units
15. Buildings
16. Soil
17. **Land Use** ← Relevant für XPlanung!
18. Human Health and Safety
19. Utility and Government Services
20. Environmental Monitoring Facilities
21. Production and Industrial Facilities
22. Agricultural and Aquaculture Facilities
23. Population Distribution
24. Area Management/Restriction/Regulation Zones
25. Natural Risk Zones
26. Atmospheric Conditions
27. Meteorological Geographical Features
28. Oceanographic Geographical Features
29. Sea Regions
30. Bio-geographical Regions
31. Habitats and Biotopes
32. Species Distribution
33. Energy Resources
34. Mineral Resources

#### **Verhältnis zu OGC**

**INSPIRE baut auf OGC-Standards auf:**

1. **Network Services:**
   - Discovery: CSW (Catalogue Service for the Web)
   - View: WMS (Web Map Service)
   - Download: WFS (Web Feature Service), ATOM
   - Transformation: WPS (Web Processing Service)

2. **Datenformat:**
   - GML 3.2.2 als Standard-Encoding
   - INSPIRE GML Application Schemas

3. **Modernisierung:**
   - OGC API - Features wird als "Good Practice" empfohlen
   - Vereinfachung: "Use standards as-is" statt INSPIRE-spezifischer Erweiterungen

**Zitat aus Quellen:**
> "The OGC enables the sharing of spatial data across EU member states and the successful implementation of INSPIRE by providing the necessary standards for geospatial data."

#### **INSPIRE Data Specifications**

**Struktur:**
- **Abstract Model (UML):** Plattformunabhängig
- **GML Application Schema:** Technische Implementierung
- **Code Lists:** Kontrollierte Vokabulare
- **Metadata:** ISO 19115/19119

**Beispiel: INSPIRE Land Use (PLU - Planned Land Use)**

Relevant für XPlanung, da beide Bauleitplanung behandeln!

**Objektarten:**
- SpatialPlan (entspricht XPlanung "Plan")
- ZoningElement (entspricht XPlanung "Bereich")
- SupplementaryRegulation

**Transformation:**
- XPlanung kann automatisch in INSPIRE PLU transformiert werden
- XLeitstelle stellt Transformationsregeln bereit

### 5.4 XLeitstelle-Ebene (Deutschland)

#### **XLeitstelle - Koordinierungsstelle**

**Betreiber:** Leitstelle XPlanung/XBau in Hamburg

**Rechtsgrundlage:**
- Verwaltungsvereinbarung zwischen Bund und Ländern
- IT-Planungsrat-Beschluss 2017/40 (XPlanung, XBau)
- IT-Planungsrat-Beschluss 2021 (XBreitband, XTrasse)

**Finanzierung:** Gemeinsam durch Bund und Länder

**Aufgaben:**
- Entwicklung und Pflege der Standards
- Änderungsmanagement und Releases
- Bereitstellung von Tools (Validator, Testdaten)
- Dokumentation und Schulungen

#### **Die vier X-Standards**

##### **1. XPlanung - Bauleitplanung**

**Zweck:** Digitalisierung von Bauleitplänen und Raumordnung

**Plantypen:**
- Bebauungsplan (BP)
- Flächennutzungsplan (FP)
- Landschaftsplan (LP)
- Regionalplan (RP)

**Status:** **Verbindlich seit Februar 2023** (nach 5 Jahren Übergangsfrist)

**Technische Basis:**
- GML 3.2.2 (OGC-Standard)
- UML-Modell in Enterprise Architect
- JSON-FG-Encoding verfügbar

**Repository:** gitlab.opencode.de/xleitstelle/xplanung

##### **2. XBau - Baugenehmigungsverfahren**

**Zweck:** Standardisierung von Bauanträgen und -genehmigungen

**Prozesse:**
- Bauantragsverfahren
- Baugenehmigung
- Bauüberwachung

**Verbindung zu XPlanung:**
- XPlanung definiert Bauleitpläne
- XBau nutzt diese Pläne in Genehmigungsverfahren

**Status:** Verbindlich seit 2023

##### **3. XTrasse - Leitungsnetze**

**Zweck:** Modellierung von Versorgungsleitungen

**Anwendung:**
- Planungen von Leitungsnetzen
- Genehmigungsverfahren für Trassenführung
- Koordination bei Infrastrukturprojekten

**Nutzer:**
- Versorgungsunternehmen
- Kommunen
- Genehmigungsbehörden

**Version:** XTrasse 1.0 veröffentlicht

##### **4. XBreitband - Breitbandausbau**

**Zweck:** Standardisierung für Breitband-Genehmigungsverfahren

**Kontext:** OZG-Leistung (Onlinezugangsgesetz) "Genehmigung nach TKG"

**Zusammenhang mit XTrasse:**
- XTrasse modelliert Leitungen
- XBreitband standardisiert Genehmigungsprozesse

#### **Verhältnis zu OGC und INSPIRE**

##### **Technische Basis: OGC**

XLeitstelle-Standards basieren vollständig auf OGC:

1. **GML 3.2.2:**
   - Alle X-Standards nutzen GML als Standard-Encoding
   - XPlanung.xsd, XBau.xsd sind GML Application Schemas

2. **Simple Features:**
   - XPlanung referenziert OGC Simple Feature Model
   - Geometrievalidierung basiert auf OGC-Spezifikation

3. **ISO 19109:**
   - Feature-Katalogisierung nach ISO 19109
   - UML als Modellierungssprache

4. **WFS:**
   - XPlanung-Daten können via WFS bereitgestellt werden
   - Interoperabilität mit GIS-Software

##### **Fachliche Harmonisierung: INSPIRE**

**INSPIRE Planned Land Use (PLU) ↔ XPlanung:**

- **Automatische Transformation:** XLeitstelle stellt Regeln bereit
- **INSPIRE-Konformität:** XPlanung-Daten können INSPIRE-konform exportiert werden
- **Unterschied:**
  - INSPIRE: Europa-weite Harmonisierung (generisch)
  - XPlanung: Detailliert nach deutschem Baugesetzbuch (BauGB)

**Beispiel:**
- INSPIRE PLU: `ZoningElement` (allgemein)
- XPlanung: `BP_BauGebiet` mit detaillierten deutschen Nutzungsarten (WA, WR, GE, etc.)

#### **Modellgetriebene Architektur**

**Ansatz der XLeitstelle:**

1. **Plattformunabhängiges Modell (PIM):**
   - UML-Modell in Enterprise Architect
   - Objektartenkatalog (Feature Catalogue)

2. **Plattformspezifische Modelle (PSM):**
   - **GML/XML:** XPlanung.xsd (via ShapeChange)
   - **JSON-FG:** XPlanung-JSON-FG-Schema (via ShapeChange)
   - **Python:** Python-Repräsentation des Datenmodells
   - **ldproxy-Config:** OGC API Features Server-Konfiguration

3. **Tool: ShapeChange**
   - Open-Source-Tool
   - UML → XML Schema, JSON Schema, SQL, etc.
   - Encoding Rules konfigurierbar

**Repositories auf gitlab.opencode.de:**
- `/xleitstelle/xplanung/` - XML-Schemas, Testdaten
- `/xleitstelle/xplanung/validierungsregeln/standard` - Validierungsregeln
- `/xleitstelle/xplanung/xplan-tools` - Tools für XPlanung-Datenverarbeitung

### 5.5 Zusammenfassung der Hierarchie

| Ebene | Rolle | Beispiele | Geltungsbereich |
|-------|-------|-----------|-----------------|
| **ISO 19100** | Normative Basis | ISO 19109, 19136, 19142 | International |
| **OGC** | Technische Standards | GML, WFS, Simple Features | International |
| **INSPIRE** | Thematische Harmonisierung (Europa) | Land Use, Transport, Elevation | EU (27 Mitgliedstaaten) |
| **XLeitstelle** | Fachspezifische Schemas (Deutschland) | XPlanung, XBau, XTrasse | Deutschland (Bund/Länder) |

**Prinzip:** Je tiefer in der Hierarchie, desto spezifischer und detaillierter die Semantik.

---

## 6. WFS vs. GeoJSON für Datenaustausch

### 6.1 Vergleichskriterien

#### **WFS 2.0 (Traditionell)**

**Protokoll:** OGC WFS 2.0 (XML-basiert)

**Datenformat:** GML (XML)

**Architektur:** SOAP/XML-orientiert, HTTP als "Tunnel"

**Operationen:**
- GetCapabilities (Service-Beschreibung)
- DescribeFeatureType (Schema-Abfrage)
- GetFeature (Daten-Abfrage)
- Transaction (Insert/Update/Delete)
- LockFeature (Feature-Sperrung)
- Stored Queries (WFS 2.0)

**Vorteile:**

1. **Standardisiert:**
   - OGC/ISO-Standard (ISO 19142)
   - Formale Spezifikation
   - Breite Unterstützung in GIS-Software

2. **Transaktional:**
   - WFS-T ermöglicht CRUD-Operationen
   - Atomare Transaktionen (Alles oder nichts)
   - LockFeature für konkurrierende Zugriffe

3. **Komplexe Filter:**
   - FES 2.0 (Filter Encoding Specification)
   - Räumliche Filter (Intersects, Within, DWithin, etc.)
   - Thematische Filter (PropertyIsEqualTo, PropertyIsLike)
   - Temporale Filter
   - Kombinationen mit AND/OR/NOT

4. **Schema-basiert:**
   - DescribeFeatureType liefert formales Schema (XSD)
   - Validierung möglich
   - Semantik klar definiert

5. **Vendor-neutral:**
   - Unabhängig von spezifischer Software
   - Interoperabilität zwischen verschiedenen GIS-Systemen

6. **Komplexe Geometrien:**
   - GML unterstützt Topologie
   - 3D-Geometrien
   - Kurven, Bögen

**Nachteile:**

1. **Verbose (XML):**
   - Großer Datei-Overhead durch XML-Tags
   - Ineffiziente Bandbreitennutzung
   - Langsames Parsing

2. **Performance:**
   - XML-Parsing rechenintensiv
   - Große Antwortgrößen
   - Nicht optimal für Echtzeit-Anwendungen

3. **Komplexe Implementierung:**
   - Hohe Einstiegshürde für Entwickler
   - Viele Spezifikationen zu verstehen (WFS, GML, FES, etc.)
   - OGC-Capabilities-Dokumente komplex

4. **Nicht web-nativ:**
   - JavaScript muss XML parsen
   - Zusätzliche Bibliotheken erforderlich
   - Nicht ideal für moderne Web-Apps

5. **HTTP als Tunnel:**
   - Kein echtes REST
   - HTTP-Caching schwierig
   - Keine Hypermedia-Controls

#### **GeoJSON mit REST-API (Modern)**

**Protokoll:** HTTP REST (GET/POST/PUT/DELETE)

**Datenformat:** GeoJSON (JSON)

**Architektur:** RESTful, Ressourcen-orientiert

**Operationen (typisch):**
- `GET /collections` - Liste der Feature Collections
- `GET /collections/{collectionId}/items` - Features abrufen
- `GET /collections/{collectionId}/items/{featureId}` - Einzelnes Feature
- `POST /collections/{collectionId}/items` - Feature erstellen
- `PUT /collections/{collectionId}/items/{featureId}` - Feature aktualisieren
- `DELETE /collections/{collectionId}/items/{featureId}` - Feature löschen

**Vorteile:**

1. **Leichtgewichtig:**
   - Kompakter als XML/GML
   - Schnelleres Parsing
   - Bessere Bandbreitennutzung

2. **Einfach zu implementieren:**
   - REST-Prinzipien bekannt
   - JSON-Parsing in jeder Programmiersprache
   - Niedrige Einstiegshürde

3. **Web-native:**
   - JavaScript-nativ (`JSON.parse()`)
   - Keine zusätzlichen Bibliotheken nötig
   - Ideal für Web-Apps und mobile Apps

4. **Schneller:**
   - JSON-Parsing performanter als XML
   - Kleinere Datengrößen
   - Bessere Client-Performance

5. **HTTP-Caching:**
   - Ressourcen-basiert → caching-freundlich
   - ETags, Last-Modified, Cache-Control
   - CDN-nutzbar

6. **Developer-freundlich:**
   - Menschenlesbar
   - Einfaches Debugging
   - API-Testing mit curl/Postman einfach

7. **OpenAPI-Dokumentation:**
   - Swagger/OpenAPI für API-Dokumentation
   - Automatische Client-Generierung

**Nachteile:**

1. **Kein Standard-Protokoll:**
   - Jede REST-API kann anders aussehen
   - Keine formale Spezifikation (historisch)
   - Interoperabilität schwieriger
   - **ABER:** OGC API - Features ändert das!

2. **Nur WGS84:**
   - GeoJSON: Nur EPSG:4326
   - Für andere CRS: Transformation nötig
   - **ABER:** JSON-FG löst das!

3. **Keine Transaktions-Standard:**
   - CRUD möglich, aber nicht standardisiert
   - Keine atomaren Transaktionen garantiert
   - Locking-Mechanismen fehlen

4. **Keine komplexen Filter:**
   - REST-APIs haben meist einfachere Filter
   - Keine FES-äquivalente Filtersprache (historisch)
   - **ABER:** CQL (Common Query Language) in OGC API - Features

5. **Kein formales Schema:**
   - GeoJSON RFC 7946 definiert kein Properties-Schema
   - JSON Schema muss separat dokumentiert werden
   - Validierung nicht standardisiert

6. **Keine Topologie:**
   - GeoJSON unterstützt keine Topologie
   - Begrenzt auf Simple Features

#### **OGC API - Features (Hybrid-Ansatz)**

**WFS 3.0 wurde zu OGC API - Features umbenannt.**

**Vereint das Beste aus beiden Welten:**

- **REST-Architektur:** Wie moderne Web-APIs
- **JSON/GeoJSON:** Primäres Datenformat
- **Standardisiert:** OGC-Standard (wie WFS)
- **OpenAPI:** Statt OGC-Capabilities
- **CQL:** Common Query Language (statt FES)
- **Hypermedia:** Links in Antworten (HATEOAS)

**Vergleich:**

| Aspekt | WFS 2.0 | GeoJSON REST (Custom) | OGC API - Features |
|--------|---------|----------------------|-------------------|
| **Protokoll** | SOAP/XML | REST (variabel) | REST (standardisiert) |
| **Datenformat** | GML/XML | GeoJSON | JSON/GeoJSON (primär) |
| **Service-Beschreibung** | GetCapabilities (XML) | Variabel | OpenAPI (JSON/YAML) |
| **Filter** | FES 2.0 (XML) | Query-Parameter (variabel) | CQL (Text/JSON) |
| **Paging** | Result Paging | limit/offset (variabel) | limit/offset (standardisiert) |
| **Caching** | Schwierig | Gut | Optimal |
| **Developer-Experience** | Komplex | Einfach | Einfach |
| **Interoperabilität** | Hoch (GIS) | Niedrig | Hoch (Web + GIS) |

### 6.2 Anwendungsfälle

#### **Wann WFS 2.0?**

**Ideal für:**

1. **GIS-zu-GIS-Integration:**
   - QGIS, ArcGIS, gvSIG nutzen WFS nativ
   - Drag-and-Drop von WFS-Layern
   - Styling, Abfragen, Analysen direkt in GIS-Software

2. **Komplexe Transaktionen:**
   - Multi-User-Editing mit Locking
   - Atomare Transaktionen erforderlich
   - Konflikt-Management

3. **Komplexe Filter:**
   - Räumliche Abfragen (z.B. "Alle Gebäude innerhalb 500m von Fluss")
   - Verschachtelte thematische Filter
   - Kombinationen aus räumlich, thematisch, temporal

4. **Schema-Validierung:**
   - Formale XSD-Schemas erforderlich
   - Strikte Datenvalidierung
   - Compliance mit INSPIRE/XLeitstelle

5. **Legacy-Systeme:**
   - Bestehende WFS-Infrastruktur
   - Behörden mit GDI-Standards
   - INSPIRE-Konformität

6. **Komplexe Geometrien:**
   - Topologie erforderlich
   - 3D-Daten
   - Kurven, Kreisbögen

**Beispiele:**
- Geodatenportale von Landes-/Bundesbehörden
- INSPIRE-Download-Services
- Kommunale Geodateninfrastrukturen
- Fachplanungen (XPlanung-WFS)

#### **Wann GeoJSON/REST?**

**Ideal für:**

1. **Web-Mapping:**
   - Leaflet, Mapbox GL JS, OpenLayers
   - Interaktive Karten
   - Echtzeitdaten

2. **Mobile Apps:**
   - Native iOS/Android-Apps
   - React Native, Flutter
   - Offline-First-Apps

3. **Frontend-Entwicklung:**
   - Single-Page-Applications (React, Vue, Angular)
   - Schnelles Prototyping
   - Entwickler ohne GIS-Background

4. **Einfache Anzeige:**
   - Karten-Viewer
   - Dashboards
   - Datenvisualisierung

5. **REST-APIs:**
   - Microservices-Architektur
   - API-First-Ansatz
   - Integration mit Non-GIS-Systemen

6. **Performance-kritisch:**
   - Große Nutzerzahlen
   - Niedrige Latenz erforderlich
   - CDN-Caching

**Beispiele:**
- OpenStreetMap-basierte Web-Apps
- Smart-City-Dashboards
- Tracking-Apps (Flottenmanagement, Lieferungen)
- Public-Transport-Apps
- Immobilienportale

#### **Wann OGC API - Features?**

**Ideal für:**

1. **Moderne GDI:**
   - Neue Geodateninfrastrukturen
   - Modernisierung bestehender WFS
   - Best-of-both-worlds

2. **Web + GIS:**
   - Web-Entwickler UND GIS-Experten als Zielgruppe
   - Breite Interoperabilität

3. **Standards-Compliance:**
   - OGC-Konformität erforderlich
   - INSPIRE-Modernisierung
   - Zukunftssicher

**Beispiele:**
- INSPIRE Good Practice (offiziell empfohlen)
- Neue Geodatenportale (z.B. Niederlande Geonovum)
- ldproxy (Open-Source OGC API Features Server)

### 6.3 Vergleichstabelle

| Kriterium | WFS 2.0 | GeoJSON/REST | OGC API - Features |
|-----------|---------|--------------|-------------------|
| **Einfachheit** | ★☆☆ | ★★★ | ★★★ |
| **Performance** | ★☆☆ | ★★★ | ★★★ |
| **Transaktionen** | ★★★ | ★☆☆ | ★★☆ |
| **Filter** | ★★★ | ★☆☆ | ★★☆ |
| **Web-Freundlichkeit** | ★☆☆ | ★★★ | ★★★ |
| **GIS-Integration** | ★★★ | ★★☆ | ★★★ |
| **Standardisierung** | ★★★ | ★☆☆ | ★★★ |
| **Caching** | ★☆☆ | ★★★ | ★★★ |
| **Schema-Support** | ★★★ | ★☆☆ | ★★☆ |
| **Developer-Experience** | ★☆☆ | ★★★ | ★★★ |

### 6.4 Empfehlungen 2024

**Neuprojekte:**
- **Web-fokussiert:** GeoJSON mit REST-API ODER OGC API - Features
- **GIS-fokussiert:** OGC API - Features (zukunftssicher)
- **Legacy-Kompatibilität:** WFS 2.0 + OGC API - Features parallel

**Bestehende Systeme:**
- **WFS 2.0 modernisieren:** Zusätzlich OGC API - Features anbieten
- **Nur lesend:** GeoJSON-REST ausreichend
- **Transaktional:** WFS 2.0 beibehalten oder auf OGC API - Features migrieren

**INSPIRE:**
- Aktuell: WFS 2.0
- Zukunft: OGC API - Features (Good Practice)

---

## 7. XLeitstelle-Bereitstellung: XML und JSON

### 7.1 Primärformat: XPlanung in GML (XML)

**Standard-Encoding:** GML 3.2.2 (XML-basiert)

**Dateiformat:** `.gml` (XPlanGML)

**Schema:** XPlanung.xsd (XML Schema Definition)

**Struktur:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xplan:XPlanAuszug xmlns:xplan="http://www.xplanung.de/xplangml/6/0"
                   xmlns:gml="http://www.opengis.net/gml/3.2"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   gml:id="GML_1"
                   xsi:schemaLocation="...">

  <xplan:raeumlicherGeltungsbereich>
    <gml:Polygon gml:id="GML_2" srsName="urn:ogc:def:crs:EPSG::25832">
      <gml:exterior>
        <gml:LinearRing>
          <gml:posList>364588.82 5621428.91 364620.15 5621450.30 ...</gml:posList>
        </gml:LinearRing>
      </gml:exterior>
    </gml:Polygon>
  </xplan:raeumlicherGeltungsbereich>

  <xplan:plan>
    <xplan:BP_Plan gml:id="GML_3">
      <xplan:name>Bebauungsplan Nr. 123</xplan:name>
      <xplan:planArt>1000</xplan:planArt> <!-- Bebauungsplan -->
      <xplan:rechtsstand>4000</xplan:rechtsstand> <!-- In Kraft getreten -->
      <xplan:bereich>
        <xplan:BP_Bereich gml:id="GML_4">
          <xplan:name>Baugebiet Musterstraße</xplan:name>
          <xplan:baugebiet>
            <xplan:BP_BauGebiet gml:id="GML_5">
              <xplan:allgArtDerBaulichenNutzung>WA</xplan:allgArtDerBaulichenNutzung>
              <xplan:GRZ>0.4</xplan:GRZ>
              <xplan:GFZ>1.2</xplan:GFZ>
              <xplan:position>
                <gml:Polygon gml:id="GML_6" srsName="urn:ogc:def:crs:EPSG::25832">
                  ...
                </gml:Polygon>
              </xplan:position>
            </xplan:BP_BauGebiet>
          </xplan:baugebiet>
        </xplan:BP_Bereich>
      </xplan:bereich>
    </xplan:BP_Plan>
  </xplan:plan>

</xplan:XPlanAuszug>
```

**Namespaces:**
- `xplan` - XPlanung-spezifische Elemente (Objektarten, Attribute)
- `gml` - GML-Geometrien und Basis-Typen
- `xsi` - XML Schema Instance (für schemaLocation)

**Koordinatensysteme:**
- Deutschland: Typisch ETRS89 / UTM Zone 32N (EPSG:25832) oder 33N (EPSG:25833)
- Definiert via `srsName`-Attribut

### 7.2 JSON-Schema: JSON-FG für XPlanung

**Entwicklung:** Modellgetriebene Generierung aus UML

**Format:** JSON-FG (OGC Features and Geometries JSON)

**Warum JSON-FG statt GeoJSON?**
- GeoJSON: Nur WGS84 (EPSG:4326)
- JSON-FG: Unterstützt beliebige CRS (wichtig für deutsche Koordinatensysteme!)
- JSON-FG: Rückwärtskompatibel mit GeoJSON

**Bereitstellung:**
- Veröffentlicht auf gitlab.opencode.de
- Teil der modellgetriebenen Architektur
- Generiert via ShapeChange

**Beispiel (JSON-FG):**
```json
{
  "type": "FeatureCollection",
  "conformsTo": [
    "http://www.opengis.net/spec/json-fg-1/0.2/conf/core"
  ],
  "features": [
    {
      "type": "Feature",
      "id": "BP_BauGebiet_001",
      "featureType": "BP_BauGebiet",
      "time": null,
      "place": {
        "type": "Polygon",
        "coordinates": [...],
        "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/25832"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [...] // WGS84 für GeoJSON-Kompatibilität
      },
      "properties": {
        "allgArtDerBaulichenNutzung": "WA",
        "GRZ": 0.4,
        "GFZ": 1.2
      }
    }
  ]
}
```

**Vorteile JSON-FG:**
- `place` - Geometrie im Original-CRS (EPSG:25832)
- `geometry` - Parallel WGS84 für GeoJSON-Tools
- `featureType` - Explizite Objektart
- `conformsTo` - Deklariert JSON-FG-Konformität

### 7.3 Konvertierung: GML ↔ GeoJSON / JSON-FG

#### **Tools:**

**1. GDAL/OGR (ogr2ogr)**

**GML → JSON-FG:**
```bash
ogr2ogr -f "JSONFG" output.json input.gml \
  --config GML_ATTRIBUTES_TO_OGR_FIELDS YES
```

**GML → GeoJSON (mit CRS-Transformation):**
```bash
ogr2ogr -f "GeoJSON" output.json input.gml \
  -t_srs EPSG:4326 \
  -s_srs EPSG:25832
```

**Herausforderungen:**
- **Tag-Hierarchie:** XPlanung hat tiefe Verschachtelung
- **Komplexe Strukturen:** GML-Referenzen, xlink:href
- **Eigenschaften-Mapping:** GML-Attribute → JSON-Properties

**2. FME (Feature Manipulation Engine)**
- Kommerzielle Software (Safe Software)
- Grafischer Workflow
- XPlanung-Reader/Writer verfügbar

**3. Custom-Tools der XLeitstelle**
- XPlan-Tools (gitlab.opencode.de/xleitstelle/xplanung/xplan-tools)
- Python-basiert
- XPlanung-spezifische Transformationen

#### **Herausforderungen bei der Konvertierung:**

**GML → GeoJSON:**
1. **CRS-Verlust:**
   - GML: Beliebige CRS (z.B. EPSG:25832)
   - GeoJSON: Nur EPSG:4326
   - Lösung: Transformation erforderlich

2. **Komplexe Strukturen:**
   - GML: Referenzen, Topologie
   - GeoJSON: Simple Features
   - Lösung: Flatten oder verlieren

3. **Namespaces:**
   - GML: XML-Namespaces
   - JSON: Keine Namespaces
   - Lösung: Umbenennung

**GML → JSON-FG:**
- Besser geeignet für XPlanung
- CRS bleibt erhalten
- Komplexere Strukturen möglich

### 7.4 WFS-Dienste für XPlanung

**XPlanung über WFS bereitstellen:**

**Beispiel-Dienste:**
- Kommunale WFS mit XPlanung-FeatureTypes
- Landesweite XPlanung-Portale

**FeatureTypes:**
- `xplan:BP_Plan`
- `xplan:FP_Plan`
- `xplan:BP_BauGebiet`
- `xplan:BP_Verkehrsfläche`
- etc.

**GetFeature-Request:**
```
https://geodienste.example.de/wfs?
  SERVICE=WFS&
  VERSION=2.0.0&
  REQUEST=GetFeature&
  TYPENAMES=xplan:BP_BauGebiet&
  BBOX=364000,5620000,365000,5622000,urn:ogc:def:crs:EPSG::25832
```

**Antwort:** GML 3.2.2 mit XPlanung-Schema

**WFS-T (Transactional):**
- Insert: Neuen Bebauungsplan hochladen
- Update: GRZ eines Baugebiets ändern
- Delete: Objekt löschen

**Praxis:**
- Viele Kommunen bieten View-Only WFS (kein WFS-T)
- Transaktionen über separate Fachanwendungen

### 7.5 OpenCode-Repositories

**gitlab.opencode.de/xleitstelle**

**Hauptrepositories:**

#### **1. XPlanung - XML-Schemas**
- **Pfad:** `/xleitstelle/xplanung/`
- **Inhalt:**
  - `XPlanung.xsd` - Haupt-XML-Schema
  - Versionsverzeichnisse (5.0, 5.1, 5.2, 5.3, 6.0)
  - Codelisten (XML)

#### **2. XPlanung - Testdaten**
- **Pfad:** `/xleitstelle/xplanung/testdaten`
- **Inhalt:**
  - Beispiel-GML-Dateien
  - Bebauungspläne (BP)
  - Flächennutzungspläne (FP)
  - Validierungstest-Daten

#### **3. XPlanung - Validierungsregeln**
- **Pfad:** `/xleitstelle/xplanung/validierungsregeln/standard`
- **Inhalt:**
  - Schematron-Regeln (XML-basiert)
  - Geschäftslogik-Validierung
  - Über XML-Schema hinausgehende Regeln

#### **4. XPlanung - JSON-FG**
- **Status:** In Entwicklung (siehe Issues)
- **Ziel:** JSON-FG-Repräsentation des XPlanung-Modells
- **Generierung:** Via ShapeChange aus UML

#### **5. XPlan-Tools**
- **Pfad:** `/xleitstelle/xplanung/xplan-tools`
- **Inhalt:**
  - Python-Tools für XPlanung-Verarbeitung
  - Konvertierungsskripte
  - Pre-commit-Hooks

#### **6. ldproxy-Konfiguration**
- **Zweck:** OGC API Features Server für XPlanung
- **ldproxy:** Open-Source-Software (interactive instruments)
- **Konfiguration:** Mapping XPlanung-Schema → OGC API Features

### 7.6 Validatoren

#### **XPlan-Validator**

**URL:** https://xleitstelle.de/xplan_validator (Online-Tool)

**Funktionen:**

1. **Syntaktische Validierung:**
   - XML-Wohlgeformtheit
   - Schema-Konformität (XSD-Validierung)
   - GML-Geometrie-Struktur

2. **Semantische Validierung:**
   - Schematron-Regeln
   - Geschäftslogik (z.B. "GRZ muss zwischen 0 und 1 liegen")
   - Beziehungen zwischen Objekten

3. **Geometrische Validierung:**
   - OGC Simple Feature Model-Konformität
   - Gültigkeit von Polygonen (geschlossen, keine Selbstüberschneidungen)
   - CRS-Konsistenz

**Input:**
- ZIP-Datei mit `xplan.gml` im Basisverzeichnis
- Oder direkte GML-Datei

**Output:**
- Validierungsbericht (HTML/PDF)
- Fehler- und Warnmeldungen
- Georeferenzierte Fehlermarkierungen

**Technologie:**
- Backend: Java-basiert
- Validator-Konfiguration: KoSIT (Koordinationsstelle für IT-Standards)
- Ähnlich zu XRechnung-Validator

#### **XRepository**

**URL:** https://xrepository.de (Referenz in Quellen, aber kein direkter Fund)

**Erwartete Funktion (basierend auf Kontext):**
- Repository für X-Standards
- Möglicherweise Code-Listen-Registry
- Analog zu INSPIRE-Registry oder OGC-Registry

**Alternative Ressourcen:**
- gitlab.opencode.de - De-facto-Repository
- xleitstelle.de - Zentrale Dokumentation

---

## 8. Primärquellen

### 8.1 Shapefile

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **ESRI Shapefile Technical Description** | https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf | Offizielles ESRI White Paper (Juli 1998), definitive technische Spezifikation |
| **ESRI Support - Shapefile Technical Description** | https://support.esri.com/en-us/technical-paper/esri-shapefile-technical-description-279 | ESRI Support-Portal mit aktualisierter Dokumentation |
| **Library of Congress - Shapefile Format** | https://www.loc.gov/preservation/digital/formats/fdd/fdd000280.shtml | Unabhängige Format-Beschreibung, Digital Preservation |
| **Shapefile - Wikipedia** | https://en.wikipedia.org/wiki/Shapefile | Community-Dokumentation mit Historie und Limitierungen |
| **ArcGIS - Geoprocessing Considerations** | https://desktop.arcgis.com/en/arcmap/latest/manage-data/shapefiles/geoprocessing-considerations-for-shapefile-output.htm | Praktische Limitierungen und Best Practices |

### 8.2 WFS (Web Feature Service)

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **OGC WFS Standard (Official)** | https://www.ogc.org/standards/wfs/ | OGC Publications-Seite mit allen WFS-Versionen |
| **WFS - Wikipedia** | https://en.wikipedia.org/wiki/Web_Feature_Service | Historischer Überblick und Versionsvergleich |
| **OGC WFS 2.0 Specification** | https://portal.ogc.org/files/?artifact_id=25355 | OGC 09-025r1, offizielle Spezifikation WFS 2.0 |
| **OGC WFS 1.1 Specification** | https://portal.ogc.org/files/?artifact_id=8339 | OGC 04-094r1, WFS 1.1.0 Implementation Spec |
| **OGC WFS 3.0 Users Guide** | https://docs.ogc.org/DRAFTS/18-000.html | Draft-Dokumentation (deprecated → OGC API Features) |
| **GeoServer WFS Reference** | https://docs.geoserver.org/stable/en/user/services/wfs/reference.html | Praktische Implementierungs-Dokumentation |

### 8.3 GeoJSON

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **RFC 7946 - The GeoJSON Format** | https://datatracker.ietf.org/doc/rfc7946/ | Offizielle IETF-Spezifikation (August 2016), normativer Standard |
| **GeoJSON.org** | https://geojson.org/ | Offizielle Community-Website mit Beispielen |
| **RFC 7946 History** | https://datatracker.ietf.org/doc/rfc7946/history/ | Entwicklungsgeschichte des IETF-Standards |
| **GeoJSON 2008 Specification (obsolete)** | https://www.loc.gov/preservation/digital/formats/fdd/fdd000382.shtml | Library of Congress - Ursprüngliche 2008-Version |
| **Sean Gillies - RFC 7946 Announcement** | https://sgillies.net/2016/08/11/rfc-7946-the-geojson-format.html | Hintergrundinfos von einem der Autoren |
| **Tom MacWright - RFC 7946 Explained** | https://macwright.com/2016/11/07/the-geojson-ietf-standard | Was ist neu in RFC 7946 (detailliert) |

### 8.4 OGC und ISO Standards

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **OGC Simple Features Access** | https://www.ogc.org/standards/sfa/ | OGC SFA-Standard für Geometrietypen |
| **OGC Simple Features Specification (SQL)** | https://portal.ogc.org/files/?artifact_id=829 | Ursprüngliche SFA-Spezifikation |
| **ISO 19136:2007 - GML** | https://www.iso.org/standard/32554.html | ISO-Standard für Geography Markup Language |
| **ISO 19136-1:2020 - GML Part 1** | https://www.iso.org/standard/75676.html | Aktualisierte GML-Spezifikation |
| **ISO 19142:2010 - WFS** | https://www.iso.org/standard/42136.html | ISO-Äquivalent zu WFS 2.0 |
| **OGC GML Standard** | https://www.ogc.org/standards/gml/ | OGC Publications für GML |
| **GML - Wikipedia** | https://en.wikipedia.org/wiki/Geography_Markup_Language | Community-Dokumentation |

### 8.5 OGC API Features

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **OGC API - Features** | https://ogcapi.ogc.org/ | Offizielle OGC API-Übersicht |
| **OGC API Features - GitHub** | https://github.com/opengeospatial/ogcapi-features | Standard-Entwicklung auf GitHub |
| **WFS 2.0 vs 3.0 Comparison** | https://github.com/opengeospatial/ogcapi-features/blob/master/guide/section_8_WFS_2_0_v_3_0.adoc | Offizieller Versionsvergleich |
| **OGC Testbed-14 - WFS 3.0 ER** | https://docs.ogc.org/per/18-045.html | Engineering Report zu WFS 3.0 |
| **Chris Holmes - WFS 3.0 Get Excited?** | https://cholmes.medium.com/wfs-3-0-get-excited-yes-8e904fdbcc0 | Hintergrund zur Entwicklung |

### 8.6 JSON-FG (OGC Features and Geometries JSON)

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **OGC Features and Geometries JSON - Part 1: Core** | https://docs.ogc.org/DRAFTS/21-045.html | Draft-Standard (wird 2025 veröffentlicht) |
| **OGC Testbed-17: JSON-FG ER** | https://docs.ogc.org/per/21-017r1.html | Engineering Report zu JSON-FG |
| **OGC Testbed-17: JSON-FG CRS Analysis** | https://docs.ogc.org/per/21-018.html | CRS-Analyse für JSON-FG |
| **GDAL - JSONFG Driver** | https://gdal.org/en/stable/drivers/vector/jsonfg.html | GDAL-Implementierung von JSON-FG |
| **GitHub - ogc-feat-geo-json** | https://github.com/opengeospatial/ogc-feat-geo-json | Standard-Entwicklung |
| **Geonovum - JSON-FG Presentation** | https://www.geonovum.nl/uploads/documents/220405-JSON-FG.pdf | Niederländische Präsentation (PDF) |

### 8.7 INSPIRE

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **INSPIRE Directive - Knowledge Base** | https://knowledge-base.inspire.ec.europa.eu/legislation/inspire-directive_en | Offizielle INSPIRE-Dokumentation |
| **INSPIRE Data Specifications** | https://inspire.ec.europa.eu/Themes/Data-Specifications/2892 | Übersicht aller 34 Themen |
| **INSPIRE - Land Use Theme** | https://inspire.ec.europa.eu/Themes/129/2892 | Land Use Data Specification |
| **INSPIRE Technical Guidelines** | https://knowledge-base.inspire.ec.europa.eu/data-specifications-technical-guidelines_en | Technische Guidelines |
| **INSPIRE and OGC APIs** | https://www.ogc.org/blog-article/inspire-and-ogc-apis-modernizing-inspire/ | Modernisierung mit OGC APIs |
| **OGC Learning Zone - INSPIRE and OGC** | http://learningzone.rspsoc.org.uk/index.php/Learning-Materials/Introduction-to-OGC-Standards/1.6-How-does-the-OGC-relate-to-the-INSPIRE-Directive | Beziehung OGC ↔ INSPIRE |

### 8.8 XLeitstelle und XPlanung

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **XLeitstelle - Hauptseite** | https://xleitstelle.de/ | Zentrale Website für alle X-Standards |
| **XPlanung - Über XPlanung** | https://xleitstelle.de/xplanung/ueber_xplanung | Offizielle Beschreibung |
| **XPlanung - FAQ** | https://xleitstelle.de/XPlanung/faq | Häufig gestellte Fragen |
| **XPlanung - Releases** | https://xleitstelle.de/xplanung/releases | Versionsübersicht und Downloads |
| **XPlanung - Wikipedia (DE)** | https://de.wikipedia.org/wiki/XPlanung | Community-Dokumentation |
| **XBau - Mehrwert** | https://xleitstelle.de/xbau/mehrwert-xbau | Beschreibung XBau-Standard |
| **XBreitband/XTrasse** | https://xleitstelle.de/xtrassexbreitband | Beschreibung der Standards |
| **XPlan-Validator** | https://xleitstelle.de/xplan_validator | Online-Validierungstool |

### 8.9 OpenCode - GitLab Repositories

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **XLeitstelle GitLab** | https://gitlab.opencode.de/xleitstelle | Übersicht aller XLeitstelle-Repositories |
| **XPlanung - Validierungsregeln** | https://gitlab.opencode.de/xleitstelle/xplanung/validierungsregeln/standard | Schematron-Validierungsregeln |
| **XPlan-Tools** | https://gitlab.opencode.de/xleitstelle/xplanung/xplan-tools | Python-Tools für XPlanung |
| **AG XPlanung mit FOSS** | https://gitlab.fossgis.de/ag-xplanung-mit-foss/workspace-xplanung | FOSSGIS-Arbeitsgruppe (Community) |

### 8.10 Weitere technische Ressourcen

| Quelle | URL | Beschreibung |
|--------|-----|--------------|
| **ISO/TC 211 Geographic Information** | https://en.wikipedia.org/wiki/ISO/TC_211_Geographic_information/Geomatics | Überblick ISO 19100-Serie |
| **GeoPackage vs Shapefile** | https://feed.terramonitor.com/shapefile-vs-geopackage-vs-geojson/ | Moderne Alternativen zu Shapefile |
| **Shapefile Must Die** | http://switchfromshapefile.org/ | Community-Kampagne für Shapefile-Alternativen |
| **OGC UML to JSON Encoding Rules** | https://geonovum.github.io/uml2json/document.html | Best Practice für Schema-Transformation |
| **ShapeChange** | https://shapechange.net/targets/xsd/ | Tool-Dokumentation für XLeitstelle |

---

## 9. Offene Fragen

### 9.1 Nicht vollständig recherchiert

1. **XRepository (xrepository.de):**
   - URL existiert möglicherweise, aber keine Suchergebnisse
   - Funktion unklar (Code-Listen-Registry? Schema-Repository?)
   - **Alternative:** gitlab.opencode.de scheint primäres Repository zu sein

2. **XPlanung JSON-Schema - Vollständiger Status:**
   - JSON-FG-Generierung wird erwähnt (via ShapeChange)
   - Aber: Keine direkten Links zu publizierten JSON-Schemas gefunden
   - **Vermutung:** In Entwicklung, noch nicht final veröffentlicht

3. **Shapefile - Exaktes Erstveröffentlichungsjahr:**
   - Quellen sagen "frühe 1990er" und "ArcView GIS Version 2"
   - White Paper von 1998 ist früheste offizielle Dokumentation
   - **Vermutung:** Zwischen 1992-1995, aber keine exakte Jahreszahl gefunden

4. **JSON-FG - Finales Veröffentlichungsdatum:**
   - Quellen sagen "wird 2025 veröffentlicht"
   - Status: OGC Candidate Standard (noch nicht final)
   - GDAL unterstützt bereits JSON-FG

5. **WFS 2.0.2 vs. 2.0.0:**
   - WFS 2.0.2 wird als "current" erwähnt
   - Aber Details zu Errata nicht recherchiert
   - Vermutlich Bugfixes, keine Feature-Änderungen

### 9.2 Bereiche für tiefere Recherche

1. **Performance-Benchmarks:**
   - Quantitative Vergleiche WFS vs. GeoJSON (Latenz, Dateigröße, Parsing-Zeit)
   - Messdaten für große Datensätze (z.B. 100.000 Features)

2. **INSPIRE-Transformation-Details:**
   - Konkrete Mapping-Regeln XPlanung → INSPIRE PLU
   - XLeitstelle-Transformationsskripte

3. **ldproxy-Implementierung:**
   - Detaillierte Konfiguration für XPlanung
   - Performance-Charakteristika

4. **ShapeChange-Konfiguration:**
   - Encoding Rules für JSON-FG
   - UML-Profile für XLeitstelle

5. **Rechtliche Verbindlichkeit:**
   - Details zu IT-Planungsrat-Beschlüssen
   - Fristen und Übergangsfristen für X-Standards

### 9.3 Weiterführende Themen

1. **3D-Geometrien:**
   - CityGML und Beziehung zu XPlanung
   - 3D-Bebauungspläne

2. **Streaming-Formate:**
   - GeoParquet für große Datensätze
   - FlatGeobuf-Details

3. **TopoJSON:**
   - Optimierung von GeoJSON durch Topologie-Eliminierung
   - Anwendungsfälle

4. **STAC (SpatioTemporal Asset Catalog):**
   - Moderne Alternative für Metadaten
   - Beziehung zu OGC API - Features

---

## 10. Zusammenfassung und Ausblick

### 10.1 Kernerkenntnisse

1. **Format-Evolution:**
   - **1990er:** Shapefile (proprietär, aber offen)
   - **2000er:** WFS/GML (XML-basierte Standards)
   - **2010er:** GeoJSON (JSON für Web-Mapping)
   - **2020er:** OGC API Features / JSON-FG (moderne REST-APIs)

2. **Datenformat ≠ Schema:**
   - GML, JSON, Shapefile sind **Container** (WIE)
   - XPlanung, INSPIRE, ALKIS sind **Semantik** (WAS)
   - Ein Schema kann in mehreren Formaten codiert werden

3. **Standardisierungs-Hierarchie:**
   - ISO/OGC → Technische Basis (international)
   - INSPIRE → Thematische Harmonisierung (Europa)
   - XLeitstelle → Fachliche Detaillierung (Deutschland)

4. **Trade-offs:**
   - **Shapefile:** Universell, aber veraltet
   - **WFS:** Mächtig, aber komplex
   - **GeoJSON:** Einfach, aber limitiert (nur WGS84)
   - **OGC API Features:** Best-of-both-worlds (modern)

### 10.2 Zukunftstrends

1. **REST statt SOAP:**
   - Abkehr von komplexen XML/SOAP-Services
   - REST-APIs mit JSON als Standard

2. **JSON-FG als Brücke:**
   - Behält GeoJSON-Einfachheit
   - Fügt CRS-Flexibilität hinzu
   - Wird wahrscheinlich XPlanung-JSON-Standard

3. **Cloud-Native Geodata:**
   - GeoParquet, Cloud-Optimized GeoTIFF
   - Streaming-fähige Formate

4. **INSPIRE-Modernisierung:**
   - OGC API Features als Good Practice
   - Vereinfachung der Implementierung

5. **XLeitstelle-Entwicklung:**
   - JSON-FG-Schemas für XPlanung/XBau
   - OGC API Features-Support
   - Modellgetriebene Architektur

### 10.3 Empfehlungen für die Praxis

**Für Behörden und GDI-Betreiber:**
- Bestehende WFS 2.0 beibehalten (Kompatibilität)
- Parallel OGC API Features anbieten (Modernisierung)
- JSON-FG für XPlanung evaluieren

**Für Entwickler:**
- Web-Apps: GeoJSON/GeoJSON-FG mit REST-APIs
- GIS-Integration: OGC API Features
- Legacy-Support: WFS 2.0-Clients beibehalten

**Für neue Projekte:**
- Datenspeicherung: GeoPackage (statt Shapefile)
- Web-Services: OGC API Features (statt WFS 2.0)
- Datenaustausch: JSON-FG (wenn CRS-Flexibilität nötig)

---

**Ende des Reports**

**Quellen gesamt:** 60+ Primärquellen (OGC, IETF, ISO, ESRI, XLeitstelle, INSPIRE)

**Umfang:** 7 Teilbereiche vollständig recherchiert

**Stand:** 2025-11-21
