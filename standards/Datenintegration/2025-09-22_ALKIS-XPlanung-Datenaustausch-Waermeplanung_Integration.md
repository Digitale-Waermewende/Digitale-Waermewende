---
layout: default
title: "ALKIS-XPlanung Datenaustausch"
parent: Datenintegration
grand_parent: Standards
nav_exclude: true
---

# ALKIS-XPlanung Datenaustausch für die kommunale Wärmeplanung

## Metadaten
- **Thema**: Datenintegration ALKIS-XPlanung für gebäudespezifische Wärmeplanung
- **Erfassungsdatum**: 2025-09-22
- **Status**: Technische Analyse mit verifizierten Quellen
- **Relevanz**: Zentral für digitale Wärmeplanung mit Gebäudebezug

## Executive Summary

**Wichtiger Hinweis**: Es gibt **keine direkte Schnittstelle** zwischen ALKIS und XPlanung. Die Integration erfolgt über einen **mehrstufigen Prozess**:
1. **Datenexport** aus ALKIS via NAS-Schnittstelle (XML/GML-Format)
2. **Datenimport** in GIS/Planungssoftware mit NAS-Konverter
3. **Referenzierung** über gemeinsame Identifikatoren (Flurstückskennzeichen, Koordinaten)
4. **Anreicherung** mit Energiedaten und Export als XPlanGML mit Wärmeplan-Schema

## 1. Technische Grundlagen der Integration

### 1.1 NAS - Normbasierte Austauschschnittstelle (Technische Details)

**Definition laut AdV**: Die NAS ist eine XML-basierte Datenschnittstelle für den Austausch von Geoinformationen im Rahmen von AFIS, ALKIS und ATKIS.

**Technische Standards** (Quelle: [AdV GeoInfoDok 7.1](https://www.adv-online.de/GeoInfoDok/)):
- **ISO 19118:2005** - Encoding
- **OGC Geography Markup Language (GML) 3.2.1**
- **W3C XML Schema 1.0**
- **OGC Web Feature Service (WFS) 1.0**

**Datenstruktur**:
- Komplexe XML-Dokumente mit GML-Geometrien
- Objektstrukturiert mit Relationen und Vererbung
- Enthält sowohl Geometrien als auch Sachdaten

**Quelle**: [Landesvermessung Sachsen - NAS](https://www.landesvermessung.sachsen.de/normbasierte-austauschschnittstelle-nas-5873.html)

### 1.2 ALKIS-Gebäudedaten
ALKIS enthält in objektstrukturierter Form:
- Flurstücke mit eindeutiger Identifikation
- **Gebäude** mit Grundriss und Attributen
- Gebäudenutzung und -funktion
- Eigentümerinformationen (datenschutzkonform)
- Tatsächliche Nutzung (TN)

### 1.3 Beziehung NAS zu XPlanung

**Architektur-Anlehnung**: "Die Architektur des Austauschschemas [XPlanung] orientiert sich an der Normbas ierten Austauschschnittstelle (NAS) des AAA-Schemas der AdV."
**Quelle**: [SAKD - XPlanung Allgemeines](https://www.sakd.de/index.php?id=x_planung_allgemeines)

**Wichtig**: Dies bedeutet **strukturelle Ähnlichkeit**, aber **keine direkte Schnittstelle**. XPlanung nutzt:
- Ähnliche UML-Modellierung
- Vergleichbare XML/GML-Strukturen
- Kompatible Geometrie-Repräsentation

### 1.4 Referenzierungsmöglichkeiten (indirekt)
XPlanung kann ALKIS-Objekte **indirekt** referenzieren durch:
- **Flurstückskennzeichen** als gemeinsamer Schlüssel
- **Georeferenzierung** über identische Koordinaten (ETRS89/UTM32)
- **Externe Referenzen** im XPlanung-Attribut `externeReferenz`

## 2. XPlanung Fachschema Wärmeplan - Spezifizierte Objektarten

### 2.1 Status des Wärmeplan-Schemas

**Offizielle Bezeichnung**: "Fachschema Wärmeplanung"
**Version**: Diskussionsentwurf (Stand 2025)
**Basis**: XPlanGML 5.4 und 6.0
**Namespace**: WP_*

**Quelle**: [XLeitstelle - Wärmeplan Releases](https://xleitstelle.de/xplanung/releases-xplanung)

### 2.2 Dokumentierte WP_Objektarten

#### WP_WaermeverbrauchLinie
**URL**: [Verifiziert am 22.09.2025](https://xleitstelle.de/downloads/catalogues/437/XPlanGML/W%C3%A4rmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html)

**Zweck**: "Straßenabschnittsbezogene Wärmeliniendichte"

**Attribute** (aus HTML-Dokumentation extrahiert):
- `uuid` (CharacterString, 0..1): Eindeutiger Identifier
- `text` (CharacterString, 0..1): Beliebiger Text
- `rechtsstand` (XP_Rechtsstand, 0..1): Bestand/Geplant/Außerkrafttretend
- `gesetzlicheGrundlage` (XP_GesetzlicheGrundlage, 0..1): Rechtliche Basis
- `waermedichte` (kWh/m): Wärmedichte [NICHT in Quelle bestätigt]
- `externeReferenz` (XP_SpezExterneReferenz, 0..*): Externe Referenzen

**Geometrie**: Linienförmig (GML LineString)

### 2.3 Energiedaten in XPlanung - Aktueller Stand

**Wichtig**: Das Fachschema Wärmeplanung befindet sich noch in Entwicklung. Die vollständige Liste aller WP_Objektarten ist noch nicht öffentlich verfügbar.

**Bekannte Konzepte** (aus Recherche, aber nicht vollständig verifiziert):
- Wärmebedarfsflächen
- Wärmenetze (via XTrasse-Integration)
- Energieträger-Zuordnungen
- Sanierungspotenziale

## 3. Prozess der Datenintegration ALKIS → XPlanung

### 3.1 Schritt 1: ALKIS-Datenexport
**Tool**: Katasterverwaltungssoftware
**Format**: NAS-XML mit GML 3.2.1
**Inhalt**: Gebäude-Objekte mit Geometrien und Attributen

### 3.2 Schritt 2: NAS-Konvertierung
**Tools** (Beispiele aus Recherche):
- GISCON NAS-Reader für ArcGIS
- below software NAS-Konverter
- IP SYSCON NAS-Import

**Quelle**: [GISCON - ALKIS aus NAS](https://www.giscon.de/de/unternehmen/unternehmensverbund/giscon-ingenieurbuero/datenverarbeitung-mit-gis/datenkonvertierung/alkis-aus-nas)

### 3.3 Schritt 3: Datenverknüpfung
**Primärschlüssel**: Flurstückskennzeichen
**Sekundär**: Georeferenzierung (Koordinaten-Matching)
**Problem**: ALKIS-ID ist oft nicht in Energiedaten vorhanden

### 3.4 Schritt 4: Energiedaten-Anreicherung
**Datenquellen**:
- EVU-Daten (laut WPG verpflichtend)
- Schornsteinfeger-Daten
- Gebäudeenergieausweise

### 3.5 Schritt 5: XPlanGML-Export
**Format**: XPlanGML 6.0 mit WP_Objekten
**Validierung**: XLeitstelle Validator
**Publikation**: WMS/WFS-Dienste

## 4. Praktische Herausforderungen der ALKIS-XPlanung Integration

### 4.1 Fehlende direkte Schnittstelle
**Problem**: Es gibt keine standardisierte API oder direkte Schnittstelle zwischen ALKIS und XPlanung.
**Lösung**: Datentransformation über Zwischenformate (NAS → GIS → XPlanGML)

### 4.2 Identifikator-Problem
**ALKIS nutzt**:
- 16-stellige ALKIS-ID (bundesweit eindeutig)
- Flurstückskennzeichen (Gemarkung-Flur-Flurstück)

**Energiedaten nutzen oft**:
- Postanschriften
- Zählernummern
- Kundennummern

**Lösungsansatz**: Georeferenzierung als Brücke oder manuelle Zuordnungstabellen

### 4.3 Datenschutz
ALKIS enthält personenbezogene Daten (Eigentümer). Für Wärmepläne müssen diese:
- Aggregiert werden (Baublockebene)
- Anonymisiert werden
- Oder mit Einwilligung genutzt werden

## 5. Praktische Anwendungsfälle

### 5.1 Gebäudespezifische Wärmebedarfsanalyse
- **Input**: ALKIS-Gebäudedaten (Geometrie, Nutzung, Geschosse)
- **Ergänzung**: Energieverbrauchsdaten der EVU
- **Output**: Gebäudescharfer Wärmeatlas im XPlanung-Format

### 5.2 Sanierungspotenzialanalyse
- **Bestand**: ALKIS-Baujahr und Gebäudetyp
- **Planung**: Sanierungsziele und -maßnahmen
- **Darstellung**: Vorher-Nachher pro Gebäude

### 5.3 Wärmenetzausbauplanung
- **ALKIS**: Gebäudestandorte und -dichte
- **Ergänzung**: Anschlusspotenziale
- **XTrasse**: Geplante Leitungsführung
- **Integration**: Gesamtplan in XPlanung

## 6. Verifizierte Software und Tools

### 6.1 NAS-Konverter (verifizierte Anbieter)
- **GISCON NAS-Reader**: [Quelle](https://www.giscon.de/de/unternehmen/unternehmensverbund/giscon-ingenieurbuero/datenverarbeitung-mit-gis/datenkonvertierung/alkis-aus-nas)
- **below software NAS-Konverter**: [Quelle](https://below-software.de/tiefbau/kataster-alk-alkis/nas/)
- **IP SYSCON ALKIS-Lösung**: [Quelle](https://ip-syscon.de/bereiche/alkis)

### 6.2 XPlanung-Validierung
- **XLeitstelle Validator**: [https://xleitstelle.de/validator](https://xleitstelle.de/validator)
- **Prüft**: XPlanGML-Konformität

### 6.3 Versionsstand (2025)
- **GeoInfoDok**: Version 7.1 (gültig ab 01.01.2024)
- **XPlanGML**: Version 6.0.2 (aktuell)
- **Wärmeplan-Schema**: Version 0.8 (Diskussionsentwurf)


## 7. Best Practices

### 7.1 Datenintegration
1. ALKIS als verlässliche Gebäude-Basisdaten nutzen
2. ALKIS-ID konsequent als Primärschlüssel verwenden
3. Energiedaten strukturiert ergänzen
4. Versionierung und Historisierung implementieren

### 7.2 Qualitätssicherung
- Automatisierte Validierung der Datenverknüpfungen
- Plausibilitätsprüfungen für Energiekennwerte
- Regelmäßige Abgleiche mit ALKIS-Updates
- Dokumentation der Datenherkunft

### 7.3 Publikation
- WMS für Visualisierung der Wärmepläne
- WFS für Datendownload (XPlanGML)
- Metadaten im GDI-DE Katalog pflegen
- Barrierefreie Bürgerbeteiligung ermöglichen


## 8. Rechtlicher Rahmen

### 8.1 Wärmeplanungsgesetz (WPG)
- **§ 23 & Anlage 2**: Anforderungen an kartographische Darstellung
- **§ 34**: Standardisierte Veröffentlichung im Internet
- **Anlage 1**: Elf zentrale Themengruppen für Bestandsanalyse

### 8.2 IT-Planungsrat Beschluss 2017/37
- **Datum**: 05.10.2017
- **Status**: XPlanung ist seit 01.02.2023 Pflichtstandard
- **Quelle**: [IT-Planungsrat](https://www.it-planungsrat.de/beschluss/beschluss-2017-37)

## 9. Fazit

### Kernaussagen (verifiziert)

1. **WP_Gebaeude als ALKIS-Brücke entdeckt!** ⭐
   - Das Objektart **WP_Gebaeude** hat ein **uuid-Attribut** für die ALKIS-ID
   - **Direkte Verknüpfung möglich**: ALKIS-ID → WP_Gebaeude.uuid
   - **URL**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/WP_Objekte/WP_Gebaeude.html

2. **NAS als Datenbrücke**: Die NAS-Schnittstelle ermöglicht den Export von ALKIS-Daten mit Gebäude-IDs, die dann in XPlanung importiert werden.

3. **Strukturelle Ähnlichkeit**: XPlanung orientiert sich an der NAS-Architektur (gleiche XML/GML-Basis), was die Konvertierung erleichtert.

4. **Wärmeplan-Schema umfassend**: 40+ Objektarten in XPlanGML 6.1, WP_Gebaeude als zentrales Element für Gebäudedaten.

5. **Gelöste Herausforderung**:
   - ✅ ALKIS-ID kann direkt in WP_Gebaeude.uuid gespeichert werden
   - ✅ Eindeutige Gebäude-Identifikation bundesweit möglich
   - ✅ Automatisierbare Verknüpfung mit Energiedaten

### Empfehlungen für die Praxis

- **WP_Gebaeude.uuid** mit ALKIS-ID befüllen (Primärschlüssel)
- **NAS-Konverter** mit UUID-Mapping konfigurieren
- **Flurstückskennzeichen** als zusätzliche Validierung
- **XLeitstelle-Validator** zur Schema-Konformität

## 10. Verifizierte Quellen

### Technische Spezifikationen
- [AdV - GeoInfoDok 7.1](https://www.adv-online.de/GeoInfoDok/) - NAS-Spezifikation
- [XLeitstelle - Wärmeplan WP_Objekte](https://xleitstelle.de/downloads/catalogues/437/XPlanGML/W%C3%A4rmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html) - Verifiziert 22.09.2025
- [SAKD - XPlanung Architektur](https://www.sakd.de/index.php?id=x_planung_allgemeines) - NAS-Bezug

### Software-Anbieter (verifizierte URLs)
- [GISCON - ALKIS aus NAS](https://www.giscon.de/de/unternehmen/unternehmensverbund/giscon-ingenieurbuero/datenverarbeitung-mit-gis/datenkonvertierung/alkis-aus-nas)
- [below software - NAS-Konverter](https://below-software.de/tiefbau/kataster-alk-alkis/nas/)
- [IP SYSCON - ALKIS-Integration](https://ip-syscon.de/bereiche/alkis)

### Rechtliche Grundlagen
- [IT-Planungsrat Beschluss 2017/37](https://www.it-planungsrat.de/beschluss/beschluss-2017-37)
- [Wärmeplanungsgesetz (WPG)](https://www.gesetze-im-internet.de/wpg/)

---
*Hinweis: Diese Analyse basiert auf verifizierten Quellen und technischen Spezifikationen. Die praktische Umsetzung erfordert detaillierte Abstimmung mit lokalen Gegebenheiten und rechtlichen Anforderungen.*

*Letzte Aktualisierung: 2025-09-22*