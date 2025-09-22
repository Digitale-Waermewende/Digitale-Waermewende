# XPlanung Fachschema Wärmeplan - Vollständiger Objektartenkatalog

## Metadaten
- **Standard**: XPlanung Fachschema kommunaler Wärmeplan
- **Version**: XPlanGML 6.1 (Entwurf)
- **Erfassungsdatum**: 2025-09-22
- **Hauptquelle**: XLeitstelle Hamburg
- **Status**: Entwurf zur Standardisierung kommunaler Wärmepläne

## Executive Summary

Das Fachschema Wärmeplan erweitert XPlanung um über 40 spezifische Objektarten für die kommunale Wärmeplanung gemäß Wärmeplanungsgesetz (WPG). Die maschinenlesbare HTML-Dokumentation ermöglicht die automatisierte Implementierung in GIS-Software.

## 1. Offizielle Dokumentation (Verifizierte URLs)

### Hauptressourcen
- **Objektartenkatalog Hauptseite**: https://xleitstelle.de/releases/objektartenkatalogWaermeplan ✅
- **XPlanGML 6.1 Package-Übersicht**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/package-summary.html

### Package-Dokumentation
- **WP_Basisobjekte**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/WP_Basisobjekte/package-summary.html
- **WP_Objekte**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/WP_Objekte/package-summary.html
- **WP_Sonstiges**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/WP_Sonstiges/package-summary.html

## 2. Package-Struktur und Hierarchie

```
Wärmeplan (Root Package)
├── WP_Basisobjekte (9 Klassen)
│   ├── Abstrakte Basisklassen
│   └── Konkrete Strukturklassen
├── WP_Objekte (30+ Fachobjekte)
│   ├── Netzinfrastruktur-Objekte
│   ├── Verbrauchsobjekte
│   └── Planungsobjekte
└── WP_Sonstiges (6 Datentypen)
    └── Komplexe Datenstrukturen
```

## 3. WP_Basisobjekte - Detaillierte Beschreibung

### 3.1 Konkrete Klassen

#### WP_Plan (Feature Type)
- **Beschreibung**: Modelliert einen Wärmeplan gemäß § 23 Wärmeplanungsgesetz
- **Zweck**: Hauptcontainer für alle Wärmeplan-Inhalte
- **Geometrie**: Keine direkte Geometrie

#### WP_Bereich (Feature Type)
- **Beschreibung**: Modelliert einen Bereich eines Wärmeplans
- **Zweck**: Strukturierung in Teilbereiche/Sektoren
- **Geometrie**: Flächengeometrie

### 3.2 Abstrakte Basisklassen

#### WP_Objekt (Abstract Feature Type)
- **Beschreibung**: Abstrakte Oberklasse für alle WP-Fachobjekte
- **Vererbung**: Basis für alle fachspezifischen Objektarten
- **Attribute**: Gemeinsame Basisattribute aller WP-Objekte

#### WP_Baublock (Abstract Feature Type)
- **Beschreibung**: Abstrakte Oberklasse für baublockbezogene WP-Fachobjekte
- **Parent**: WP_Objekt
- **Verwendung**: Aggregation auf Baublockebene

#### Geometrie-Basisklassen
- **WP_Flächenobjekt**: Multi-Flächengeometrie
- **WP_Linienobjekt**: Multi-Liniengeometrie
- **WP_Punktobjekt**: Multi-Punktgeometrie
- **WP_Geometrieobjekt**: Variable Geometrie

### 3.3 Datentyp
- **WP_Version**: Versionsinformationen des Plans

## 4. WP_Objekte - Vollständige Liste (30+ Objektarten)

### 4.1 Gebäude und ALKIS-Integration ⭐

#### WP_Gebaeude (ALKIS-Schlüsselobjekt)
- **URL**: https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/W%C3%A4rmeplan/WP_Objekte/WP_Gebaeude.html
- **Geometrie**: Fläche (XP_Flaechengeometrie)
- **Zweck**: Zentrale Gebäuderepräsentation mit ALKIS-Verknüpfung
- **🔗 ALKIS-Integration**:
  - **uuid-Attribut**: Speichert die 16-stellige ALKIS-ID
  - **Eindeutige Verknüpfung**: Gebäude-Identifikation über ALKIS
  - **Datenfluss**: ALKIS → WP_Gebaeude.uuid → Energiedaten
- **Pflichtattribute**:
  - `gebaeudetyp`: Wohngebäude, Dienstleistungsgebäude, etc.
  - `baualtersklasse`: "bis 1918", "1919-1948", ... , "ab 2021"
  - `position`: Gebäudegrundriss (aus ALKIS übernehmbar)
  - `rechtscharakter`: Rechtlicher Status
- **💡 Bedeutung**: Schlüsselobjekt für die Verknüpfung von ALKIS-Bestandsdaten mit Energieverbrauchsdaten!

### 4.2 Netzinfrastruktur

#### WP_AbwasserNetzAbschnitt
- **Geometrie**: Linie
- **Zweck**: Erfassung von Abwärmepotenzial aus Kanalisation
- **Attribute**: Durchfluss, Temperatur, Abwärmepotenzial

#### WP_WaermeverbrauchLinie ✅
- **URL**: https://xleitstelle.de/downloads/catalogues/437/XPlanGML/W%C3%A4rmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html
- **Geometrie**: Linie
- **Zweck**: Straßenabschnittsbezogene Wärmeliniendichte
- **Hauptattribut**: waermedichte (kWh/m)

### 4.3 Anschlussgebiete

#### WP_Anschlusszwang
- **Geometrie**: Fläche
- **Zweck**: Gebiete mit Anschluss- und Benutzungszwang
- **Rechtliche Basis**: Kommunale Satzung

#### WP_AnschlussSynthMethan
- **Geometrie**: Fläche
- **Zweck**: Gasverteilernetz mit synthetischem Methan
- **Energieträger**: Power-to-Gas

### 4.4 Ausschluss- und Schutzgebiete

#### WP_Ausschlussgebiet
- **Geometrie**: Fläche
- **Zweck**: Schutzgebiete ohne Wärmenetzausbau
- **Beispiele**: Naturschutz, Wasserschutz

### 4.5 Weitere wichtige Objektarten (Auswahl)
- WP_Bestandsnetz
- WP_Einspeisepunkt
- WP_Energieerzeugungsanlage
- WP_Fernwaermenetz
- WP_GebaeudeWaermebedarf
- WP_GeothermischesPotenzialgeb
- WP_Grossverbraucher
- WP_IndustrielleAbwaerme
- WP_Nahwaermenetz
- WP_Netzausbaugebiet
- WP_Neubaugebiet
- WP_Quartiersloesung
- WP_Sanierungsgebiet
- WP_Solarthermieflaeche
- WP_Speicherstandort
- WP_Transformationsgebiet
- WP_Uebergabestation
- WP_Umweltwaerme
- WP_Versorgungsgebiet
- WP_Waermebedarf
- WP_Waermeerzeugung
- WP_Waermenetzverdichtung
- WP_Waermesenke
- WP_Waermespeicher
- WP_Waermeueberschussgebiet

## 5. WP_Sonstiges - Komplexe Datentypen

### 5.1 WP_EnergieTraegerAnteil
- **Typ**: Data Type
- **Beschreibung**: Anteil Endenergieverbrauch der Energieträger
- **Struktur**: Prozentuale Aufteilung

### 5.2 WP_EnergieTraegerVerbrauch
- **Typ**: Data Type
- **Beschreibung**: Endenergieverbräuche nach Energieträgern
- **Einheit**: MWh/a

### 5.3 WP_EnergieTraegerVerbrauchsangaben
- **Typ**: Data Type
- **Beschreibung**: Leitungsgebundene Endenergieverbräuche
- **Differenzierung**: Strom, Gas, Fernwärme

### 5.4 WP_GebaeudeNetzanschluss
- **Typ**: Data Type
- **Beschreibung**: Gebäude-Netzanschluss-Informationen
- **ALKIS-Verknüpfung**: Referenzierung über WP_Gebaeude.uuid
- **Zweck**: Verknüpfung von Gebäuden mit Wärme-/Gasnetzen

### 5.5 WP_SektorVerbrauch
- **Typ**: Data Type
- **Beschreibung**: Sektorspezifische Endenergieverbräuche
- **Sektoren**: Haushalte, GHD, Industrie, Verkehr

### 5.6 WP_WaermeerzeugerEnergietraeger
- **Typ**: Data Type
- **Beschreibung**: Dezentrale Wärmeerzeuger
- **Technologien**: Wärmepumpe, Solarthermie, Biomasse

## 6. Technische Spezifikation

### 6.1 Standards und Konformität
- **Basis**: XPlanGML 6.1
- **Geometrie**: GML 3.2.2
- **Koordinatensystem**: ETRS89/UTM32
- **Modellierung**: UML 2.0
- **Kodierung**: UTF-8

### 6.2 Namespaces
```xml
xmlns:wp="http://www.xplanung.de/xplangml/6/1/waermeplan"
xmlns:xplan="http://www.xplanung.de/xplangml/6/1"
xmlns:gml="http://www.opengis.net/gml/3.2"
```

### 6.3 Validierung
- **XSD-Schema**: Verfügbar über XLeitstelle
- **Validator**: https://xleitstelle.de/validator
- **Konformitätsstufen**: Minimal, Standard, Vollständig

## 7. Integration mit anderen Standards

### 7.1 ALKIS-Integration über WP_Gebaeude

#### Direkte Verknüpfung (NEU ENTDECKT!)
- **WP_Gebaeude.uuid** = **ALKIS-ID** (16-stellig)
- **Datenfluss**:
  1. ALKIS-Export via NAS → Gebäude mit ID
  2. Import in Wärmeplan → WP_Gebaeude erstellen
  3. UUID-Feld mit ALKIS-ID befüllen
  4. Energiedaten über UUID verknüpfen

#### Vorteile dieser Lösung
- ✅ Eindeutige Gebäude-Identifikation
- ✅ Keine manuellen Zuordnungen nötig
- ✅ Automatisierbare Datenintegration
- ✅ Bundesweit einheitlich

#### Ergänzende Verknüpfungen
- Flurstückskennzeichen als Fallback
- Georeferenzierung über identische Koordinaten
- Adressdaten als zusätzliche Validierung

### 7.2 XTrasse-Integration
- Leitungsnetze für Wärmenetze
- Trassenführung und -planung
- Gemeinsame Geometriebasis

### 7.3 INSPIRE-Konformität
- Utility and Government Services
- Energy Resources
- Buildings (Annex III)

## 8. Praktische Anwendung

### 8.1 Mindestanforderungen WPG
Das Schema deckt alle Anforderungen aus:
- § 23 WPG (Inhalt der Wärmepläne)
- § 34 WPG (Veröffentlichung)
- Anlage 1 WPG (Bestandsanalyse)
- Anlage 2 WPG (Kartendarstellung)

### 8.2 Typischer Workflow
1. Bestandsanalyse mit WP_Bestandsnetz
2. Potenzialanalyse mit WP_GeothermischesPotenzialgeb etc.
3. Zielszenario mit WP_Netzausbaugebiet
4. Maßnahmen mit WP_Transformationsgebiet

### 8.3 Software-Unterstützung
- GIS-Systeme mit XPlanung-Plugin
- Spezielle Wärmeplanungssoftware
- Web-GIS für Bürgerbeteiligung

## 9. Herausforderungen und Lösungen

### 9.1 Komplexität
- **Problem**: 40+ Objektarten überfordern kleine Kommunen
- **Lösung**: Minimalprofil mit Pflichtfeldern definieren

### 9.2 Datenintegration
- **Problem**: Heterogene Datenquellen (EVU, Schornsteinfeger, etc.)
- **Lösung**: Mapping-Tabellen und Konverter

### 9.3 Visualisierung
- **Problem**: Komplexe Darstellung verschiedener Layer
- **Lösung**: Vordefinierte SLD-Styles bereitstellen

## 10. Fazit

Das XPlanung Fachschema Wärmeplan bietet eine umfassende und standardisierte Grundlage für die digitale kommunale Wärmeplanung. Mit über 40 spezifischen Objektarten können alle Aspekte des Wärmeplanungsgesetzes abgebildet werden. Die maschinenlesbare HTML-Dokumentation ermöglicht eine effiziente Implementierung in bestehende GIS-Infrastrukturen.

### Vorteile
- ✅ Vollständige Abdeckung der WPG-Anforderungen
- ✅ Maschinenlesbare Dokumentation
- ✅ Integration in XPlanung-Ökosystem
- ✅ Zukunftssicher durch Standardisierung

### Nächste Schritte
1. Pilotprojekte mit ausgewählten Kommunen
2. Entwicklung von Best-Practice-Beispielen
3. Schulungsprogramm für Planer
4. Feedback-Loop zur Weiterentwicklung

## Quellen
- XLeitstelle Hamburg: https://xleitstelle.de
- Wärmeplanungsgesetz (WPG): Bundesgesetzblatt 2024
- IT-Planungsrat Beschluss 2017/37

---
*Hinweis: Alle URLs wurden am 22.09.2025 auf Erreichbarkeit geprüft.*

*Letzte Aktualisierung: 2025-09-22*