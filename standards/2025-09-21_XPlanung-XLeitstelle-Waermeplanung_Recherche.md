# XPlanung, XLeitstelle und digitale Standards für die Wärmeplanung

## Metadaten
- **Organisationen**: XLeitstelle Hamburg, IT-Planungsrat, BBSR, EU (INSPIRE)
- **Erfassungsdatum**: 2025-09-21
- **Typ**: Recherche/Übersichtsdokument
- **Hauptquellen**: xleitstelle.de, gdi-de.org, EU-Richtlinien
- **Relevanz**: Kritische Standards für digitale Wärmeplanung und Datenaustausch

## Zusammenfassung
XPlanung ist der verbindliche Standard für den digitalen Austausch von Planungsdaten in Deutschland. Die XLeitstelle koordiniert dessen Entwicklung und hat ein Fachschema für die Wärmeplanung entwickelt. Beide basieren auf INSPIRE-Richtlinien der EU.

## Wichtige Begriffe erklärt

### 🏗️ XPlanung
**Definition**: Offener, XML-basierter Datenaustauschstandard für Raumplanungsdaten

**Kernmerkmale**:
- Basiert auf Geography Markup Language (GML 3.2.2)
- Aktuelle Version: 6.0
- Modelliert in UML (Unified Modeling Language)
- Formalisiert Inhalte aus BauGB, BauNVO, PlanzV, ROG, BNatSchG

**Verbindlichkeit**:
- ⚠️ **Seit 2023 PFLICHT** für alle Verwaltungen
- IT-Planungsrat-Beschluss vom 05.10.2017
- 5-Jahre-Übergangsfrist bis Februar 2023 abgelaufen

**Anwendungsbereiche**:
- Bauleitpläne (Flächennutzungspläne, Bebauungspläne)
- Raumordnungspläne
- Landschaftspläne
- NEU: Kommunale Wärmepläne

### 🏢 XLeitstelle
**Definition**: Zentrale Geschäfts- und Koordinierungsstelle für digitale Planungsstandards

**Standort**: Hamburg

**Zuständigkeiten**:
- Pflege und Weiterentwicklung von:
  - XPlanung (Raumplanung)
  - XBau (Bauanträge)
  - XTrasse (Infrastruktur)
  - XBreitband (Breitbandausbau)
  - **NEU: Fachschema Wärmeplan**

**Seit**: 2003 (Entwicklung XPlanung)

### 📊 Fachschema Wärmeplan / Objektartenkatalog
**Definition**: Spezifische Erweiterung von XPlanung für kommunale Wärmepläne

**Status**: Veröffentlicht und dokumentiert

**Struktur**: WP_Objekte (Wärmeplan-Objekte) mit spezifischen Klassen wie:
- **WP_WaermeverbrauchLinie**: Straßenabschnittsbezogene Wärmeliniendichte
  - Attribut `waermedichte`: Wärmedichte in kWh/m
  - Attribut `rechtsstand`: Geplant/Bestand/Außerkrafttretend
  - Geometrie: Linienförmig

**Ziel**: Standardisierte digitale Erfassung und Austausch von Wärmeplanungsdaten

**Problem**: 
- ⚠️ Noch geringe Bekanntheit in der Praxis
- Konkurrenz zu proprietären Lösungen
- KWW Halle fokussiert auf andere Aspekte

### 🌍 INSPIRE (Infrastructure for Spatial Information in Europe)
**Definition**: EU-Richtlinie zum Aufbau einer europäischen Geodateninfrastruktur

**Rechtsbasis**: Richtlinie 2007/2/EG (in Kraft seit 15.05.2007)

**Umsetzung Deutschland**:
- 17 Gesetze (Bund + 16 Länder)
- Koordination: GDI-DE beim BKG Frankfurt
- 34 Themenbereiche in 3 Anhängen

**Relevanz für Wärmeplanung**: 
- Grundlage für XPlanung
- Sichert EU-weite Interoperabilität
- Umweltdaten als Kernfokus

## Primärquellen mit Kommentaren

### 1. **XLeitstelle Hauptseite**
- **URL**: https://xleitstelle.de
- **Inhalt**: Zentrale Koordination aller X-Standards
- **Kommentar**: Offizielle Quelle, aber technisch orientiert. Wenig praxisnahe Beispiele.

### 2. **IT-Planungsrat Beschluss 2017/40**
- **Datum**: 05.10.2017
- **Inhalt**: Verbindliche Einführung XPlanung/XBau
- **Kommentar**: ⚠️ Rechtlich bindend! Übergangsfrist abgelaufen.

### 3. **BBSR Modellvorhaben XPlanung**
- **URL**: https://www.bbsr.bund.de/BBSR/DE/forschung/programme/moro/studien/2014/XPlanung/01-start.html
- **Organisation**: Bundesamt für Bauwesen und Raumordnung
- **Kommentar**: Wissenschaftliche Begleitung, praktische Erprobung

### 4. **Geodatenportal Niedersachsen - XPlanung**
- **URL**: https://www.geodaten.niedersachsen.de/startseite/kommunale_gdi/xplanung_xbau/
- **Kommentar**: Gutes Beispiel für Länderumsetzung, praxisnah

### 5. **INSPIRE-Richtlinie Deutschland**
- **URL**: https://www.gdi-de.org/en/INSPIRE
- **Organisation**: Geodateninfrastruktur Deutschland
- **Kommentar**: EU-Kontext, wichtig für Interoperabilität

### 6. **Fachschema Wärmeplan - Objektartenkatalog**
- **URL**: https://xleitstelle.de/releases/objektartenkatalogWaermeplan
- **Weitere Dokumentation**: https://xleitstelle.de/downloads/catalogues/437/XPlanGML/Wärmeplan/
- **Status**: ✅ Veröffentlicht und online
- **Inhalt**: 
  - WP_Objekte (Wärmeplan-spezifische Objektklassen)
  - Beispiel: WP_WaermeverbrauchLinie für Wärmeliniendichten
  - Integration in XPlanGML-Standard
- **Downloads verfügbar**:
  - Objektartenkatalog PDF (Version 5.4 und 6.0)
  - HTML-Dokumentation einzelner Objektarten
  - Testdaten über BitBucket Repository
- **Kommentar**: Technische Spezifikation vorhanden, aber komplex. Praxisbeispiele fehlen noch. Wichtig für Softwareentwickler.

## Kritische Bewertung durch Claude (Work in Pregress)
*Kommentar Homann: Die folgenden Abschnitte sind noch nicht manuell überarbeitet und enthalten z.T. falsche Wertungen durch Claude. Bitte mit Vorsicht lesen*

### ✅ Stärken
- Einheitlicher Standard verhindert Vendor-Lock-in
- Verlustfreier Datenaustausch zwischen Systemen
- EU-weite Kompatibilität durch INSPIRE
- Rechtliche Verbindlichkeit schafft Klarheit
- Wärmeplan-Schema ist technisch spezifiziert

### ⚠️ Schwächen
- **Geringe Bekanntheit** bei Wärmeplanern
- **Komplexität** schreckt kleine Kommunen ab
- **Konkurrenz** zwischen Standards (XPlanung vs. proprietär)
- **Medienbruch**: Viele Kommunen nutzen weiter PDF
- **Dokumentation** sehr technisch, wenig praxisorientiert

### 🔴 Hauptproblem
**Diskrepanz zwischen Anspruch und Realität**:
- XLeitstelle entwickelt Standards
- KWW Halle berät Kommunen
- → Wenig Koordination zwischen beiden
- → Kommunen nutzen weiter PDF

## Technische Details Wärmeplan-Schema

### Objektarten (Auswahl)
- **WP_WaermeverbrauchLinie**
  - Zweck: Erfassung von Wärmeliniendichten entlang Straßen
  - Pflichtattribut: `waermedichte` in kWh/m
  - Geometrie: Linie
  - Rechtsstand: Bestand/Planung/Außerkrafttretend

### Datenmodell
- Abgeleitet von XPlanGML-Basisklassen
- Eigener Namespace: WP_*
- UML-modelliert
- XML-Schema validierbar

### Integration
- Kompatibel mit XPlanGML 5.4 und 6.0
- GML 3.2.2 konform
- INSPIRE-kompatibel

## Handlungsempfehlungen

### Für Kommunen
1. **Sofort**: Prüfen ob Software XPlanung-kompatibel ist
2. **Mittelfristig**: Schulung zu XPlanung/Wärmeplan
3. **Langfristig**: Digitale Workflows etablieren

### Für Planungsbüros
1. **Kritisch**: Software muss XPlanung unterstützen (Pflicht!)
2. **Chance**: Frühzeitige Expertise als Wettbewerbsvorteil
3. **Risiko**: Ohne XPlanung keine öffentlichen Aufträge
4. **NEU**: WP_Objekte in Software implementieren

### Für das Projekt
1. **Dokumentieren**: Alle WP_Objektarten erfassen
2. **Vernetzen**: Brücke zwischen XLeitstelle und KWW schlagen
3. **Aufklären**: Best Practices für XPlanung in Wärmeplanung
4. **Testen**: Beispieldaten im WP-Format erstellen

## Verbindungen
- Ergänzt: KWW-Halle Sitemap (praktische Umsetzung)
- Konflikt mit: PDF als bevorzugtes Format
- Bezug zu: WPG (Wärmeplanungsgesetz), GEG
- Technische Basis für: Datenkompass, MLV

## Offene Fragen
1. Vollständige Liste aller WP_Objektarten?
2. Wie viele Kommunen nutzen bereits XPlanung für Wärmepläne?
3. Gibt es Beispieldaten im XPlanGML-Format für Wärmepläne?
4. Integration mit Technikkatalog des BMWK?
5. Schulungsangebote für WP-Schema?

## Nächste Schritte
- [x] Objektartenkatalog Wärmeplan gefunden und dokumentiert
- [ ] Alle WP_Objektarten systematisch erfassen
- [ ] Kontakt zu XLeitstelle für Praxisbeispiele
- [ ] Beispiel-Kommune mit XPlanung-Wärmeplan finden
- [ ] Mapping zwischen KWW-Tools und XPlanung erstellen
- [ ] Testdaten von BitBucket Repository analysieren

---
*Letzte Aktualisierung: 2025-09-21*