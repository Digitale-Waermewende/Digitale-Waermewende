# XPlanung in Bayern (BY) — Deep Research (mit Capabilities)
*Stand: 22.09.2025 — Link‑Check: **geprüft am 22.09.2025***

## 1) Kurzfazit
Bayern bündelt landesweite Nachweise über den **Geodatenkatalog** (GDI‑DE/GDI‑BY) und veröffentlicht Bauleitplanung weitgehend **dezentral** über kommunale/kreisliche Dienste. Für Planungsträger liegt ein aktueller **XPlanung‑Leitfaden** des Staatsministeriums vor. Capabilities‑ und Metadaten‑Permalinks sind über das **Geoportal Bayern – Dienste** und den **GDI‑DE‑Katalog** gut auffindbar. Herausforderungen bestehen in der Heterogenität der kommunalen Veröffentlichungen, der Versionierung von XPlanGML und der einheitlichen Datenqualität【122†source】.

## 2) Rechtlicher Rahmen
- **IT‑Planungsrat Beschluss 2017/37** – Verbindliche Anwendung/Weiterentwicklung von XPlanung/XBau: https://www.it-planungsrat.de/beschluss/beschluss-2017-37

## 3) Technische Infrastruktur & Dienste (Land & Katalog)
- **Geoportal Bayern – Diensteübersicht** (Einstieg zu WMS/WFS‑Detailseiten): https://geoportal.bayern.de/geoportalbayern/seiten/dienste【122†source】  
- **Bayern – Bebauungspläne (Metadaten‑Permalink, GDI‑DE):** https://gdk.gdi-de.org/geonetwork/srv/api/records/26d2b2b8-3944-4a49-aec2-59f827d9aa9e【122†source】  
- **Bayern – Flächennutzungspläne (Metadaten‑Permalink, GDI‑DE):** https://gdk.gdi-de.org/geonetwork/srv/api/records/43df73e1-e2be-4034-83da-791f716fc394【122†source】  
- **Bayern – Bauleitpläne (Umringe) (Metadaten‑Permalink, GDI‑DE):** https://gdk.gdi-de.org/geonetwork/srv/api/records/73ff4959-749d-42eb-b604-c587524ade0b【122†source】

## 4) Organisation & Akteure
- **Bayerisches Staatsministerium für Wohnen, Bau und Verkehr** – fachliche Federführung XPlanung/Bauleitplanung.  
- **Landesamt für Digitalisierung, Breitband und Vermessung (LDBV)** – GDI‑Koordination, Geoportal Bayern, Katalogdienste.  
- **Kommunen/Landkreise** – Veröffentlichung und Pflege der XPlanGML‑Daten und OGC‑Dienste.

## 5) Tools & Projekte
- **XPlanung‑Leitfaden Bayern (PDF):** https://www.digitale.planung.bayern.de/medien/dokumente/leitfaden_xplanung.pdf【122†source】  
- **Geoportal Bayern – Dienste** als Recherche‑Tool für Capabilities und thematische Layer【122†source】.

## 6) Kommunale Umsetzung (Beispiele mit Capabilities/Metadaten)
- **Landkreis Starnberg – Bebauungspläne (WMS Capabilities):**  
  http://geolis.lk-starnberg.de/geoservice/services/Internet/Bebauungsplan/MapServer/WmsServer?REQUEST=GetCapabilities&SERVICE=WMS【122†source】
- **BayernAtlas / Kommunale B‑Pläne – Beispiel Schwabach (Landing‑Page/Viewer):**  
  https://www.schwabach.de/de/bebauungsplaene.html【132†source】

## 7) Herausforderungen / Risiken
- Unterschiedliche Umsetzungsstände und Software‑Stacks in Kommunen.  
- Versionierung/Profiltreue von **XPlanGML** (5.x/6.x).  
- Qualität/Attributierung und Aktualität; teils fehlende Download‑WFS.

## 8) Empfehlungen
- Landesweit abgestimmte Publikationsstandards (Darstellung, SLD, Stored Queries).  
- Systematische **Metadaten‑Pflege** (Kontakt, Lizenz, Aktualität).  
- Unterstützung kleinerer Kommunen (Templates, Hosting, QA).  
- Monitoring der Erreichbarkeit von Capabilities.

## 9) Quellen (prüfbare URLs)
- **Geoportal Bayern – Dienste:** https://geoportal.bayern.de/geoportalbayern/seiten/dienste【122†source】  
- **GDI‑DE Metadaten – Bebauungspläne:** https://gdk.gdi-de.org/geonetwork/srv/api/records/26d2b2b8-3944-4a49-aec2-59f827d9aa9e【122†source】  
- **GDI‑DE Metadaten – Flächennutzungspläne:** https://gdk.gdi-de.org/geonetwork/srv/api/records/43df73e1-e2be-4034-83da-791f716fc394【122†source】  
- **GDI‑DE Metadaten – Bauleitpläne (Umringe):** https://gdk.gdi-de.org/geonetwork/srv/api/records/73ff4959-749d-42eb-b604-c587524ade0b【122†source】  
- **LK Starnberg – B‑Pläne WMS Capabilities:** http://geolis.lk-starnberg.de/geoservice/services/Internet/Bebauungsplan/MapServer/WmsServer?REQUEST=GetCapabilities&SERVICE=WMS【122†source】  
- **Leitfaden XPlanung Bayern (PDF):** https://www.digitale.planung.bayern.de/medien/dokumente/leitfaden_xplanung.pdf【122†source】  
- **Schwabach – B‑Pläne (Viewer/Info):** https://www.schwabach.de/de/bebauungsplaene.html【132†source】
