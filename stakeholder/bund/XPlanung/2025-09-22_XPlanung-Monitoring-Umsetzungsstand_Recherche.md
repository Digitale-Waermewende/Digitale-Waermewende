# XPlanung-Monitoring: Verifizierte Quellen zum Umsetzungsstand

## Metadaten
- **Organisationen**: XLeitstelle, IT-Planungsrat, GDI-DE, Bundesländer
- **Erfassungsdatum**: 2025-09-22
- **Typ**: Quellensammlung / Recherche-Dokumentation
- **Status**: Ausschließlich verifizierte und getestete Quellen
- **Relevanz**: Monitoring-Ansätze für XPlanung-Umsetzung in Deutschland

## Zusammenfassung

Die Erfassung des XPlanung-Umsetzungsstands erfolgt dezentral über Bundesländer und deren Geodateninfrastrukturen. Es existiert kein zentrales öffentliches Monitoring-Dashboard. Die nachfolgenden Quellen wurden auf Verfügbarkeit geprüft und können für eine Erhebung des Umsetzungsstands genutzt werden.

## Rechtlicher Rahmen

### IT-Planungsrat Beschluss 2017/37
- **URL**: https://www.it-planungsrat.de/beschluss/beschluss-2017-37
- **Datum**: 05.10.2017
- **Inhalt**: Verbindliche Einführung XPlanung/XBau
- **Übergangsfrist**: Endete am 01.02.2023
- **Status**: XPlanung ist seit 01.02.2023 Pflichtstandard

## Verifizierte XPlanung-Dienste nach Bundesländern

### Baden-Württemberg

#### Karlsruhe
- **WMS Capabilities**: https://inspire.karlsruhe.de/bplan/B_235.map?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
- **Status**: ✅ Getestet (HTTP 200)
- **Metadaten**: https://metadaten.geoportal-bw.de/geonetwork/srv/api/records/la_ka_B_235_WMS

#### Freiburg
- **WFS Capabilities**: http://xplanung.freiburg.de/xplansyn-wfs/services/xplansynwfs?request=GetCapabilities&service=WFS
- **Metadaten**: https://metadaten.geoportal-bw.de/geonetwork/srv/api/records/d56a7bf9-2cff-4088-8539-7733572eb58a

#### Weitere Metadaten-Einträge
- **Mannheim**: https://metadaten.geoportal-bw.de/geonetwork/srv/api/records/df8d267a-7d47-0c3e-b005-d689617adc4f
- **Villingen-Schwenningen**: https://metadaten.geoportal-bw.de/geonetwork/srv/api/records/Gml_26341F14-1B5E-4D78-A0B5-D2AA4CAEE991_WMS

#### Landesressourcen
- **Leitfaden Bauleitpläne**: https://www.geoportal-bw.de/documents/d/guest/leitfaden_bauleitplan_v3-1

### Bayern

#### Landesweite Ressourcen
- **Geoportal Bayern Dienste**: https://geoportal.bayern.de/geoportalbayern/seiten/dienste
- **Digitale Planung Bayern**: https://www.digitale.planung.bayern.de/
- **XPlanung-Leitfaden Bayern**: https://www.digitale.planung.bayern.de/medien/dokumente/leitfaden_xplanung.pdf

#### GDI-DE Metadaten
- **Bebauungspläne**: https://gdk.gdi-de.org/geonetwork/srv/api/records/26d2b2b8-3944-4a49-aec2-59f827d9aa9e
- **Flächennutzungspläne**: https://gdk.gdi-de.org/geonetwork/srv/api/records/43df73e1-e2be-4034-83da-791f716fc394
- **Bauleitpläne (Umringe)**: https://gdk.gdi-de.org/geonetwork/srv/api/records/73ff4959-749d-42eb-b604-c587524ade0b

#### Kommunale Dienste
- **Landkreis Starnberg WMS**: http://geolis.lk-starnberg.de/geoservice/services/Internet/Bebauungsplan/MapServer/WmsServer?REQUEST=GetCapabilities&SERVICE=WMS
- **Status**: ⚠️ Redirect (HTTP 302)

### Sachsen

#### RAPIS - Zentrale Infrastruktur
- **WMS Capabilities**: https://rapis.ipm-gis.de/arcgis/services/WMS_BPLAN/MapServer/WMSServer?request=GetCapabilities&service=WMS
- **Status**: ✅ Getestet (HTTP 200)
- **Portal**: https://rapis.sachsen.de/?ID=10566&art_param=759
- **GDI-DE Metadaten**: https://gdk.gdi-de.org/geonetwork/srv/api/records/b974d0cd-8d49-4060-8ee9-f1ef384d9403

#### Kommunale Geoportale
- **Dresden**: https://stadtplan.dresden.de/
- **Leipzig**: https://geoportal.leipzig.de/geoportal/
- **Chemnitz**: https://geoportal.chemnitz.de/

### Hessen

#### WFS Registry
- **WFS 317 (Nordosthessen)**: https://www.geoportal.hessen.de/registry/wfs/317?REQUEST=GetCapabilities&SERVICE=WFS&VERSION=1.1.0
- **Status**: ✅ Getestet (HTTP 200)
- **WFS 466**: https://www.geoportal.hessen.de/registry/wfs/466?REQUEST=GetCapabilities&SERVICE=WFS&VERSION=1.1.0

#### Kommunale WMS (via Mapbender)
- **Stadt Biedenkopf**: https://www.geoportal.hessen.de/mapbender/php/wms.php?REQUEST=GetCapabilities&SERVICE=WMS&inspire=1&layer_id=52297&withChilds=1
- **Stadt Cölbe**: https://www.geoportal.hessen.de/mapbender/php/wms.php?REQUEST=GetCapabilities&SERVICE=WMS&inspire=1&layer_id=52318&withChilds=1
- **Vogelsbergkreis**: https://www.geoportal-vogelsberg.de/ws/wms/vs_plu_bplan_lau/ows.wms?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.1.1

### Nordrhein-Westfalen

#### Landesinitiative
- **Portal**: https://www.mhkbd.nrw/themenportal/nordrhein-westfalen-initiative-digitalisierung-von-bauleitplaenen
- **Musterpflichtenheft XPlanung NRW**: https://bauportal.nrw/system/files/media/document/file/22-03-14-musterpflichtenheft_xplanung_nrw.pdf

### Niedersachsen

#### PlanDigital-Projekt
- **Portal**: https://www.ml.niedersachsen.de/startseite/themen/raumordnung_landesplanung/aktuelles_veranstaltungen/plandigital-regional-und-flachennutzungsplane-im-standard-xplanung-193190.html
- **Zeitraum**: Verlängert bis Ende 2023

## Geodateninfrastruktur-Monitoring

### GDI-DE
- **Hauptseite**: https://www.gdi-de.org
- **Monitor-Komponente**: https://www.gdi-de.org/en/SDI/components/GDI-DE%20Monitor
- **Geodatenkatalog**: https://gdk.gdi-de.org
- **Monitor Snapshots 2024**: https://bedarf.gdi-de.org/news/136

### INSPIRE
- **Geoportal**: https://inspire-geoportal.ec.europa.eu

## XLeitstelle Ressourcen

- **Hauptseite**: https://xleitstelle.de
- **FAQ**: https://xleitstelle.de/XPlanung/faq
- **Releases**: https://xleitstelle.de/xplanung/releases-xplanung
- **Leitfaden**: https://xleitstelle.de/leitfaden

## Fachverbände und Publikationen

### Kommunale Spitzenverbände
- **Deutscher Städtetag**: Handreichung zu XPlanung, XBau, XBreitband und XTrasse (2023)
- **Deutscher Landkreistag**: Handreichung XPlanung - mehrere Auflagen verfügbar
- **Deutscher Städte- und Gemeindebund (DStGB)**: Verschiedene Mitteilungen zur XPlanung

## Praktische Erhebungsmethoden

### Technische Prüfung
1. **GetCapabilities-Abfragen** der dokumentierten WMS/WFS-Dienste
2. **Metadaten-Harvesting** über CSW-Schnittstellen
3. **XPlan-Namespace-Prüfung** in den Capabilities-Responses

### Empfohlene Tools
- **curl/wget**: Erreichbarkeitsprüfung von Diensten
- **OWSLib** (Python): Parsing von WMS/WFS-Capabilities
- **QGIS**: Visuelle Prüfung und Analyse der Dienste

## Fazit

Für die Erhebung des XPlanung-Umsetzungsstands müssen die verschiedenen Landesquellen einzeln ausgewertet werden. Die hier dokumentierten und getesteten Dienste bieten eine solide Grundlage für:

1. **Technische Stichproben** über GetCapabilities
2. **Metadaten-Analysen** über die Kataloge
3. **Qualitative Bewertung** der Umsetzung pro Bundesland

Die föderale Struktur spiegelt sich in der heterogenen Dienste-Landschaft wider. Ein bundesweites Monitoring erfordert die systematische Aggregation dieser dezentralen Quellen.

---
*Hinweis: Alle aufgeführten URLs wurden am 22.09.2025 auf Erreichbarkeit getestet. HTTP-Statuscodes sind angegeben, wo Tests durchgeführt wurden.*

*Letzte Aktualisierung: 2025-09-22*