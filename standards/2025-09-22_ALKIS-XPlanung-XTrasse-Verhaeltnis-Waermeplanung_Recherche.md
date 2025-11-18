# ALKIS, XPlanung und XTrasse: Verhältnis, Unterschiede und Bedeutung für die Wärmeplanung

## Metadaten
- **Organisationen**: AdV (Arbeitsgemeinschaft der Vermessungsverwaltungen), XLeitstelle, BBSR, IT-Planungsrat, Landesvermessungsämter
- **Erfassungsdatum**: 2025-09-22
- **Typ**: Deep Research / Technische Analyse
- **Hauptquellen**: AdV-Dokumentationen, XLeitstelle, BBSR-Publikationen, IT-Planungsrat-Beschlüsse
- **Relevanz**: Klärung der Beziehung zwischen ALKIS, XPlanung und XTrasse für die kommunale Wärmeplanung

## Zusammenfassung

ALKIS (Amtliches Liegenschaftskatasterinformationssystem), XPlanung und XTrasse sind **drei komplementäre Systeme** der deutschen Geodateninfrastruktur:
- **ALKIS** (seit 2015): Amtliche Liegenschaftsdaten und Gebäudeinformationen (Ist-Zustand oberirdisch)
- **XPlanung** (seit 2003): Digitaler Austausch von Planungsdaten (Soll-Zustand)
- **XTrasse** (seit 2021): Modellierung und Verwaltung von Leitungsnetzen (Bestand und Planung)

Für die Wärmeplanung ist die Kombination aller drei Systeme erforderlich: ALKIS liefert Gebäudedaten, XTrasse kann Wärmenetze abbilden, und XPlanung ermöglicht die standardisierte Darstellung der Wärmepläne.


**ALKIS und XPlanung sind parallel entwickelte, sich ergänzende Systeme**:
- Beide entstanden ab 2003 zeitgleich
- Unterschiedliche Zwecke und Anwendungsbereiche
- Technische Harmonisierung, aber keine Nachfolgebeziehung


**ALKIS erfasst NUR oberirdisch sichtbare Objekte**:
- Flurstücke, Gebäude, Nutzungsflächen
- KEINE unterirdischen Infrastrukturen oder Leitungsnetze
- Für Trassen ist XTrasse zuständig

## ALKIS - Amtliches Liegenschaftskatasterinformationssystem

### Definition und Zweck
ALKIS ist das bundesweit einheitliche System zum Nachweis der Geobasisdaten des Liegenschaftskatasters. Es ersetzt seit 2015 die Vorgängersysteme ALK (Automatisierte Liegenschaftskarte) und ALB (Automatisiertes Liegenschaftsbuch).

### Kernmerkmale
- **Standard**, kein Software-System
- **Objektorientierte Modellierung** nach AAA-Referenzmodell
- **Bundesweit einheitlich** über alle Bundesländer
- **Normbasierte Austauschschnittstelle** (NAS)
- **XML-basiert** nach GeoInfoDok-Standard
- **ISO/OGC-konform** (GML 3.2.2, WFS)

### Erfasste Daten
1. **Flurstücke** (Grundstücke)
   - Geometrien und Grenzen
   - Flächenangaben
   - Nutzungsarten

2. **Gebäude**
   - Grundrisse und Umringe
   - Gebäudefunktionen (Wohnen, Gewerbe, etc.)
   - Geschosszahlen
   - Dachformen (teilweise)

3. **Eigentumsinformationen**
   - Grundbuchblattnummern
   - Eigentumsarten

4. **Tatsächliche Nutzung**
   - Siedlungsflächen
   - Verkehrsflächen
   - Vegetationsflächen

5. **ALKIS-ID**
   - Eindeutiger 16-stelliger Identifikator
   - Bundesweit einmalig
   - Verknüpfungsschlüssel für Datensätze

### Was ALKIS NICHT erfasst
⚠️ **Kritische Einschränkung für Wärmeplanung:**
- **KEINE Leitungsnetze** (Wärme, Strom, Gas, Wasser, Abwasser)
- **KEINE unterirdischen Infrastrukturen**
- **KEINE Energieverbrauchsdaten**
- **KEINE Heizungsanlagen**
- **KEINE Dämmstandards**

### Entwicklungsgeschichte
- **1997**: Entscheidung zur AAA-Modell-Entwicklung
- **2003**: Beginn der Konzeption
- **2008**: Start der Migration in ersten Bundesländern
- **2015**: Bundesweite Einführung abgeschlossen
- **2024**: Migration auf AAA-Version 7.1

## XPlanung - Standard für digitale Planungsdaten

### Definition und Zweck
XPlanung ist der verbindliche Standard für den verlustfreien Austausch digitaler Bauleitpläne, Raumordnungspläne und Landschaftspläne zwischen unterschiedlichen IT-Systemen.

### Kernmerkmale
- **XML/GML-basiert** (Geography Markup Language)
- **UML-modelliert** (Unified Modeling Language)
- **Rechtlich verbindlich** seit 2023 (IT-Planungsrat)
- **Aktuelle Version**: 6.0
- **Fachschema Wärmeplan** seit 2024

### Anwendungsbereiche
1. **Bauleitplanung**
   - Flächennutzungspläne (FNP)
   - Bebauungspläne (B-Plan)

2. **Raumordnung**
   - Regionalpläne
   - Landesentwicklungspläne

3. **Landschaftsplanung**
   - Landschaftspläne
   - Grünordnungspläne

4. **NEU: Wärmeplanung**
   - Kommunale Wärmepläne
   - WP_Objekte (spezielle Objektarten)

### Was XPlanung NICHT kann
⚠️ **Ohne Erweiterungen:**
- **KEINE Bestandsdaten von Leitungsnetzen**
- **KEINE Trassenmodellierung**
- Dafür ist XTrasse erforderlich

### Entwicklungsgeschichte
- **2003**: Beginn der Entwicklung
- **2008**: Version 2.0
- **2017**: IT-Planungsrat-Beschluss zur Verbindlichkeit
- **2023**: Übergangsfrist endet - Pflicht für alle Verwaltungen
- **2024**: Fachschema Wärmeplan veröffentlicht

## XTrasse - Standard für Leitungsnetze und Infrastrukturtrassen

### Definition und Zweck
XTrasse ist der Geodatenstandard für die Modellierung von Leitungsnetzen und Infrastrukturtrassen. Es ermöglicht den verlustfreien Austausch von vollständig vektorisierten, georeferenzierten Trassenplänen zwischen Versorgungsunternehmen und Verwaltungen.

### Kernmerkmale
- **Erweiterung von XPlanung** (baut auf gleicher technischer Basis auf)
- **Eigenständiger Standard** neben XPlanung
- **XTrasseGML** als Austauschformat
- **Version 2.0** mit 6 Anwendungsfällen
- **Verbindlich** seit 2021 für Breitbandausbau

### Erfasste Infrastrukturen
XTrasse kann **alle Leitungssparten** abbilden:
- **Wärmenetze/Fernwärme**
- **Abwassernetze**
- **Stromnetze** (alle Spannungsebenen)
- **Gasnetze**
- **Telekommunikation/Breitband**
- **Wasserversorgung**

### Anwendungsfälle (Version 2.0)
1. **Bestandsnetze** - Erfassung vorhandener Leitungen
2. **Breitbandausbau** - Glasfasernetze
3. **Genehmigungsverfahren** nach TKG
4. **Interkommunale Konzepte**
5. **Detailplanungen**
6. **Infrastrukturatlas** (Bundesnetzagentur)

### Integration mit XPlanung
- **Technische Basis**: Nutzt XPlanung-Modellierungsprinzipien
- **Modularer Aufbau**: Pakete für verschiedene Anwendungsfälle
- **Kompatible Schnittstellen**: Nahtlose Integration möglich
- **Gemeinsame Verwaltung**: Durch XLeitstelle

### Entwicklungsgeschichte
- **2017**: Erste Konzepte
- **2021**: IT-Planungsrat-Beschluss zur Verbindlichkeit
- **2021**: XTrasse 1.0 veröffentlicht
- **2023**: XTrasse 2.0 mit erweitertem Funktionsumfang
- **2024**: Produktionsumgebung mit QGIS verfügbar

## Verhältnis ALKIS - XPlanung - XTrasse

### Komplementäre Funktionen

#### Datenebenen
- **ALKIS**: Oberirdische Bestandsdaten (Gebäude, Flurstücke)
- **XTrasse**: Unterirdische und oberirdische Leitungsnetze (Bestand und Planung)
- **XPlanung**: Planungsdokumente und Soll-Zustände

#### Zeitbezüge
- **ALKIS**: Ist-Zustand (Gegenwart)
- **XTrasse**: Ist-Zustand UND Planungszustand (Gegenwart und Zukunft)
- **XPlanung**: Soll-Zustand (Zukunft)

#### Räumliche Abdeckung
- **ALKIS**: Oberirdisch sichtbare Objekte
- **XTrasse**: Ober- und unterirdische Infrastrukturen
- **XPlanung**: Planungsräume und -flächen

### Technische Integration

#### Gemeinsame Standards
Alle drei Systeme nutzen:
- **XML** als Basis
- **GML** für Geometrien
- **ISO 19100-Serie** als Normgrundlage
- **OGC-Standards** für Webservices

#### Datenverknüpfung für Wärmeplanung
1. **ALKIS** liefert Gebäudegrundrisse und -funktionen
2. **XTrasse** erfasst bestehende und geplante Wärmenetze
3. **XPlanung** integriert beides im kommunalen Wärmeplan

#### Beispiel-Workflow
```xml
<!-- ALKIS: Gebäude -->
<AX_Gebaeude>
  <alkisID>DENW1234567890ABCDEF</alkisID>
  <gebaeudefunktion>1010</gebaeudefunktion> <!-- Wohngebäude -->
</AX_Gebaeude>

<!-- XTrasse: Wärmenetz -->
<XT_Leitung>
  <leitungsart>Fernwaerme</leitungsart>
  <durchmesser>DN300</durchmesser>
  <verlauf>...</verlauf>
</XT_Leitung>

<!-- XPlanung: Wärmeplan -->
<WP_Versorgungsgebiet>
  <alkisID>DENW1234567890ABCDEF</alkisID>
  <anschlussLeitung href="XT_Leitung_ID"/>
  <versorgungsart>Fernwaerme</versorgungsart>
</WP_Versorgungsgebiet>
```

## Bedeutung für die Wärmeplanung

### Datengrundlagen

#### Aus ALKIS benötigt
- Gebäudegrundrisse und -funktionen
- Grundstücksgrenzen
- Nutzungsarten
- ALKIS-ID als Verknüpfungsschlüssel

#### Aus XTrasse benötigt
- Bestehende Wärmenetze (Verlauf, Dimensionen)
- Anschlusspunkte
- Kapazitäten
- Geplante Erweiterungen

#### In XPlanung dargestellt
- Eignungsgebiete für Wärmenetze
- Prioritätsgebiete
- Wärmeversorgungsarten
- Transformationspfade

### Praktische Herausforderungen

#### Datenverfügbarkeit
- **ALKIS**: Flächendeckend vorhanden ✅
- **XTrasse für Wärmenetze**: Meist noch nicht vorhanden ❌
- **XPlanung-Wärmepläne**: In Entwicklung ⚠️

#### Datenqualität
- **ALKIS**: Hohe Qualität, aber energetische Daten fehlen
- **Wärmenetzdaten**: Oft nur analog oder in proprietären Formaten
- **Integration**: Aufwändige Konvertierung erforderlich

#### Koordination
- **Verschiedene Datenhalter**: Katasterämter, Netzbetreiber, Planungsämter
- **Unterschiedliche Aktualisierungszyklen**
- **Fehlende Standards** bei vielen Versorgern

### Lösungsansätze

#### Kurzfristig
1. **ALKIS-Daten** als Basis nutzen
2. **Wärmenetzdaten** manuell digitalisieren
3. **Provisorische Verknüpfung** über Georeferenzierung

#### Mittelfristig
1. **XTrasse-Adoption** bei Fernwärmeversorgern fördern
2. **Konvertierungstools** entwickeln
3. **Schulungen** für alle Beteiligten

#### Langfristig
1. **Vollständige Integration** ALKIS-XTrasse-XPlanung
2. **Automatisierte Workflows**
3. **Digitaler Zwilling** der kommunalen Energieinfrastruktur

## Aktuelle Entwicklungen 2024

### Gesetzliche Verpflichtungen
- **Wärmeplanungsgesetz (WPG)** seit 01.01.2024
- **XPlanung-Pflicht** für alle Planungen
- **XTrasse-Pflicht** bisher nur für Breitband

### Technische Entwicklungen

#### ALKIS AAA-Version 7.1
- Migration 2024 in allen Bundesländern
- Verbesserte Gebäudedaten
- Stabilere ALKIS-IDs

#### XTrasse-Produktionsumgebung
- **QGIS** als Basis
- **PostgreSQL/SQLite** für Datenhaltung
- **ldproxy** für Schnittstellen
- Kostenlos verfügbar über XLeitstelle

#### Wärmeatlas Deutschland 4.0
- Integration der ALKIS-ID ✅
- Verknüpfung mit XTrasse vorbereitet
- Export nach XPlanung möglich

### Software-Integration 2024
- **Vectorworks 2024**: ALKIS-Import, XPlanung-Export
- **IP SYSCON**: XPlanung/XTrasse für ArcGIS Pro
- **CAIGOS**: Vollständige ALKIS-XPlanung-XTrasse-Integration
- **QGIS**: XTrasse-Produktionsumgebung

## Best Practices für Kommunen

### Datenmanagement
1. **ALKIS-Daten** konsequent als Gebäudebasis nutzen
2. **Bestandsaufnahme** der Wärmenetze (auch wenn noch nicht in XTrasse)
3. **ALKIS-ID** als zentralen Schlüssel etablieren
4. **Schrittweise Migration** zu XTrasse planen

### Technische Umsetzung
1. **XPlanung-kompatible Software** einsetzen
2. **XTrasse-fähige Tools** evaluieren (z.B. QGIS-Produktionsumgebung)
3. **Schnittstellen** zwischen Systemen definieren
4. **Testläufe** mit kleinen Gebieten

### Organisatorisch
1. **Koordination** zwischen Kataster-, Planungs- und Tiefbauamt
2. **Datenaustausch** mit Netzbetreibern vereinbaren
3. **Schulungen** für XTrasse frühzeitig planen
4. **Externe Unterstützung** bei Konvertierung erwägen

## Handlungsempfehlungen

### Für Kommunen
1. **Sofort**: ALKIS-Gebäudedaten für Wärmeplanung aufbereiten
2. **2024/25**: Wärmenetzdaten digitalisieren (Vorbereitung für XTrasse)
3. **2025/26**: XTrasse-Migration der Bestandsnetze
4. **Ab 2026**: Vollständig digitaler Workflow ALKIS-XTrasse-XPlanung

### Für Netzbetreiber
1. **Evaluierung**: XTrasse-Kompatibilität prüfen
2. **Pilotprojekt**: Teilnetz in XTrasse konvertieren
3. **Schulung**: Mitarbeiter auf Standard vorbereiten
4. **Integration**: Schnittstellen zu kommunalen Systemen

### Für Planungsbüros
1. **Software-Update**: XTrasse-Unterstützung sicherstellen
2. **Kompetenzaufbau**: XTrasse-Expertise entwickeln
3. **Workflow-Anpassung**: Drei-Ebenen-Integration einplanen
4. **Qualitätssicherung**: Validierung über alle drei Systeme

## Fazit

Die erfolgreiche digitale Wärmeplanung erfordert das **Zusammenspiel aller drei Systeme**:

- **ALKIS** liefert die unverzichtbare **Gebäudedatengrundlage**
- **XTrasse** ermöglicht die **Abbildung der Leitungsnetze** (Bestand und Planung)
- **XPlanung** integriert alles im **standardisierten Wärmeplan**

Die größte Herausforderung liegt in der **praktischen Umsetzung**:
- ALKIS ist etabliert ✅
- XPlanung wird zunehmend genutzt ⚠️
- XTrasse für Wärmenetze steht noch am Anfang ❌

**Kritischer Erfolgsfaktor** ist die Überwindung der Datensilos zwischen:
- Katasterämtern (ALKIS)
- Netzbetreibern (proprietäre Systeme → XTrasse)
- Planungsämtern (XPlanung)

Die technischen Standards sind vorhanden und ausgereift. Die Herausforderung liegt in der **organisatorischen Umsetzung** und der **Datenkonvertierung** bestehender Systeme.

## Quellen

### Primärquellen ALKIS
- **AdV (2024)**: AAA-Referenzmodell Version 7.1. Arbeitsgemeinschaft der Vermessungsverwaltungen der Länder der Bundesrepublik Deutschland. [www.adv-online.de]
- **Bezirksregierung Köln (2024)**: ALKIS-Standard NRW - Migration auf AAA 7.1. [www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/liegenschaftskataster/alkis-standard]
- **LGLN Niedersachsen (2024)**: AFIS-ALKIS-ATKIS Projekt. Landesamt für Geoinformation und Landesvermessung. [www.lgln.niedersachsen.de]

### Primärquellen XPlanung
- **XLeitstelle (2024)**: Fachschema Wärmeplan - Objektartenkatalog. Version 6.0. Hamburg. [xleitstelle.de/releases/objektartenkatalogWaermeplan]
- **IT-Planungsrat (2017)**: Beschluss 2017/40 - Verbindliche Einführung XPlanung/XBau. [www.it-planungsrat.de]
- **IT-Planungsrat (2021)**: Beschluss 2021/40 - IT-Standard XBau und XPlanung. [www.it-planungsrat.de/beschluss/beschluss-2021-40]

### Primärquellen XTrasse
- **XLeitstelle (2023)**: XTrasse 2.0 - Standard für die Modellierung von Leitungsnetzen. [xleitstelle.de/xtrassexbreitband/anwendungsfaelle2]
- **XLeitstelle (2021)**: XTrasse 1.0 als neuer Standard für die Modellierung von Leitungsnetzen veröffentlicht. [xleitstelle.de/node/118]
- **IT-Planungsrat (2021)**: Spezifikation XTrasse - Anlage 3 zu Beschluss 2021/40. [www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-40_IT-Standard_XBau_und_XPlanung_AL3_Spezifikation_XTrasse.pdf]

### Handreichungen und Leitfäden
- **Deutscher Städtetag (2023)**: Handreichung zu XPlanung, XBau, XBreitband und XTrasse. [www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung]
- **Deutscher Landkreistag (2024)**: Handreichung XPlanung - 3. Auflage. [www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage]
- **DStGB (2023)**: Handreichung XPlanung und XBau. Deutscher Städte- und Gemeindebund. [www.dstgb.de]

### Forschung und Analysen
- **BBSR (2024)**: Analysen KOMPAKT 07/2024 - Status quo der Kommunalen Wärmeplanung. [www.bbsr.bund.de]
- **BBSR (2025)**: Stakeholder-Dialog Wärmeplanung - Ergebnispapier. DOI: 10.58007/sxc3-d095
- **BIMBreitband (2024)**: Digitale Standards für den Breitbandausbau: XTrasse und XBreitband. [www.bimbreitband.de]

### Technische Dokumentationen
- **GeoInfoDok 7.1 (2024)**: Dokumentation zur Modellierung der Geoinformationen des amtlichen Vermessungswesens. AdV.
- **XPlanGML 6.0 (2024)**: Spezifikation des XPlanung-Standards. XLeitstelle Hamburg.
- **NAS 7.1 (2024)**: Normbasierte Austauschschnittstelle - Technische Beschreibung. AdV.
- **XTrasseGML 2.0 (2023)**: Objektmodell und Austauschformat für Leitungsnetze. XLeitstelle.

### Praxisbeispiele und Tools
- **geomer GmbH (2024)**: Wärmeatlas Deutschland 4.0 - Integration von ALKIS-ID. [www.geomer.de]
- **DEEA (2024)**: Der Datenkompass zur Kommunalen Wärmeplanung. Deutsche Energie-Effizienz-Agentur. [deea.de]
- **Nexiga (2024)**: Daten zur Wärmeplanung - Integration von ALKIS und Energiedaten. [nexiga.com]
- **XLeitstelle (2024)**: XTrasse-Produktionsumgebung mit QGIS. Download und Dokumentation. [xleitstelle.de/xtrassexbreitband/anwendungen]

### Open Data Portale
- **Berlin Open Data (2024)**: ALKIS Berlin Gebäude - WFS. [daten.berlin.de]
- **GovData (2024)**: ALKIS Gebäude - Bundesweites Portal. [www.govdata.de]
- **MetaVer (2024)**: ALKIS - ausgewählte Daten Hamburg. [metaver.de]

---
*Letzte Aktualisierung: 2025-09-22*
*Erweitert um XTrasse-Integration und Primärquellen*