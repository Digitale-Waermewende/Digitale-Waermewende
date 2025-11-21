---
layout: default
title: Navigation und Sitemap
parent: XLeitstelle
grand_parent: Bund
nav_order: 1
permalink: /stakeholder/bund/xleitstelle/navigation-sitemap/
---

# XLeitstelle.de - Navigation und Sitemap-Analyse

**Erfassungsdatum**: 2025-11-21
**Zweck**: Dokumentation der Navigation zu XPlanung/Wärmeplan-Objektkatalogen

---

## Problem: Fehlende XML-Sitemap

**Test**: https://www.xleitstelle.de/sitemap.xml
**Ergebnis**: ✗ 404 Not Found

**Alternative**: https://www.xleitstelle.de/robots.txt
**Ergebnis**: ✓ Existiert, enthält aber **keine Sitemap-Referenzen**

**Schlussfolgerung**: xleitstelle.de bietet **keine XML-Sitemap** an.

---

## Navigation zu Wärmeplan-Objektkatalogen

Die detaillierten Objekt- und Attributbeschreibungen für Wärmepläne sind nicht prominent platziert, sondern erfordern mehrstufige Navigation oder direkte URL-Kenntnis.

### Navigationspfad (über Website)

1. **Hauptseite**: https://www.xleitstelle.de
2. **XPlanung-Bereich**: https://www.xleitstelle.de/xplanung
3. **Releases**: https://xleitstelle.de/xplanung/releases (oder /xplanung/releases-xplanung)
4. **Wärmeplan-Ordner**: Sichtbar in der Ordnerliste als "Wärmeplan Version 0.9X"
5. **Objektkatalog**: Zugriff über spezifische URLs (siehe unten)

**Problem**: Versionsspezifische URLs (z.B. `/xplanung/releases-xplanung/waermeplan-version-09x`) funktionieren nicht (404-Fehler).

### Direkte URLs zu Objektkatalogen (empfohlen)

#### Version 0.84 (neueste, August 2025)

**Hauptkatalog**: https://xleitstelle.de/downloads/catalogues/468/

**Übersicht ohne Frames**: https://xleitstelle.de/downloads/catalogues/468/overview-summary.html

**Katalog-Details**:
- Version: 0.84
- Datum: 27.08.2025
- Schema-Basis: XPlanGML 6.1
- Beschreibung: "Entwurf für ein Fachschema zur Modellierung von kommunalen Wärmeplänen"

**Struktur**:
```
XPlanGML 6_1/
├── Basisklassen/
│   ├── XP_Basisobjekte (Kern-Basisklassen)
│   ├── XP_Codelisten (Planübergreifende externe Codelisten)
│   ├── XP_Enumerationen (Gemeinsame Aufzählungen)
│   ├── XP_Geometrietypen (Spezialisierte Geometrietypen)
│   ├── XP_KomplexeDatentypen (Komplexe Datentypen)
│   └── XP_Praesentationsobjekte (Graphische Darstellung)
├── Wärmeplan/
│   ├── WP_Basisobjekte (Basisklassen für WP_Plan, WP_Bereich)
│   ├── WP_Objekte (Fachobjekte: Bestand, Potenzial, Darstellung)
│   └── WP_Sonstiges (Nicht-räumliche Features, aggregierte Daten)
```

**Zugriff auf einzelne Objekte** (Beispiel):
- Format: `/downloads/catalogues/468/XPlanGML/Wärmeplan/WP_Objekte/[Objektname].html`
- Beispiel: https://xleitstelle.de/downloads/catalogues/468/XPlanGML/Wärmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html

#### Version 0.7 (Dezember 2024)

**Hauptkatalog**: https://xleitstelle.de/downloads/catalogues/437/

**Übersicht ohne Frames**: https://xleitstelle.de/downloads/catalogues/437/overview-summary.html

**Katalog-Details**:
- Version: 0.7
- Datum: 15.12.2024
- Schema-Basis: XPlanung 7.0
- Beschreibung: "A specialist schema for depicting municipal heat planning"

**Struktur**:
```
XPlanGML/
├── Basisklassen/
│   ├── XP_Basisobjekte
│   └── XP_Geometrietypen
├── Wärmeplan/
│   ├── WP_Basisobjekte (Basisklassen für WP_Plan, WP_Bereich, Domänenobjekte)
│   └── WP_Objekte (Bestandsaufnahme, Potenzialanalyse, Visualisierung)
```

**Zugriff auf einzelne Objekte** (Beispiel):
- Format: `/downloads/catalogues/437/XPlanGML/Wärmeplan/WP_Objekte/[Objektname].html`
- Beispiel: https://xleitstelle.de/downloads/catalogues/437/XPlanGML/Wärmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html

---

## Technisches Problem: HTML Frames

Die Objektkataloge nutzen **veraltete HTML-Frames** (frameset), was zu Problemen führt:

**Symptom**: Browser zeigen Meldung "Das Design dieses Dokuments basiert auf HTML frames. Wenn Sie diese Nachricht sehen nutzen Sie einen Browser der nicht frame-kompatibel ist."

**Lösung**: Nutzen der **overview-summary.html** statt der Hauptseite:
- ✗ `/downloads/catalogues/468/` (Frames, problematisch)
- ✓ `/downloads/catalogues/468/overview-summary.html` (Frame-freie Alternative)

**WebFetch-Kompatibilität**:
- Frame-basierte Seiten: Begrenzte Sichtbarkeit
- overview-summary.html: Vollständig zugänglich

---

## Beispiel: Objektbeschreibung WP_WaermeverbrauchLinie

**URL**: https://xleitstelle.de/downloads/catalogues/437/XPlanGML/Wärmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html

**Objekttyp**: Feature Class
**Definition**: Straßenabschnittsbezogene Wärmeliniendichte
**Übergeordnete Klasse**: WP_Linienobjekt
**Package**: WP_Objekte

### Attribute (Auswahl)

| Name | Datentyp | Kardinalität | Beschreibung |
|------|----------|--------------|--------------|
| uuid | CharacterString | 0..1 | Eindeutige Objekt-ID |
| text | CharacterString | 0..1 | Beliebiger Text |
| position | XP_Liniengeometrie | 1 | Liniengeometrie (erforderlich) |
| **waermedichte** | Measure | 1 | Wärmedichte in kWh/m (erforderlich) |
| aufschrift | CharacterString | 0..1 | Spezifischer Beschriftungstext |
| rechtsstand | Enumeration | 0..1 | Status (geplant, bestehend, etc.) |
| rechtscharakter | Enumeration | 1 | Rechtscharakter (24 Werte: Festsetzung, etc.) |
| gesetzlicheGrundlage | XP_GesetzlicheGrundlage | 0..1 | Gesetzliche Grundlage |
| gehoertZuBereich | XP_Bereich | 1 | Zuordnung zu Bereich (erforderlich) |

### Navigationsmöglichkeiten

- **Übergeordnete Klasse**: Link zu WP_Linienobjekt
- **Package**: Link zu WP_Objekte (alle Objekte im Package)
- **Datentyp-Referenzen**: Links zu XP_Bereich, XP_GesetzlicheGrundlage, etc.

---

## Alternative Navigationswege

### Via Suche

**XLeitstelle-Suche**: https://xleitstelle.de/suche?fulltext=Objektartenkatalog

**Ergebnisse**: Listet verfügbare Objektkataloge (XPlanung-Versionen, Wärmeplan, XTrasse)

### Via Releases-Seite

**XPlanung-Releases**: https://xleitstelle.de/xplanung/releases-xplanung

**Inhalt**: Ordnerliste mit allen XPlanung-Versionen und "Wärmeplan Version 0.9X"

**Problem**: Direkte URLs zu Unterordnern (z.B. `/waermeplan-version-09x`) funktionieren nicht

### Via Fachschema-Seite

**URL-Varianten** (getestet):
- `/fachschema-waermeplan` → 404
- `/xplanung/fachschema-waermeplan` → 404
- `/releases/objektartenkatalogWaermeplan` → Existiert (minimal, keine Downloads sichtbar)
- `/Waermeplanung` → 404

**Schlussfolgerung**: Fachschema-Seiten sind vorhanden, aber nicht über konsistente URL-Muster erreichbar.

---

## Empfehlungen für Navigation

### Für Menschen (Browser)

1. **Haupteinstieg**: https://www.xleitstelle.de/xplanung
2. **Wärmeplan-Bereich**: Menü-Navigation zu "Fachschema Wärmeplan"
3. **Objektkatalog**: Suche nutzen oder direkte URLs zu `/downloads/catalogues/`

### Für automatisierte Zugriffe (WebFetch, Tools)

**Empfohlen**:
- Direkte URLs zu `/downloads/catalogues/[Nummer]/overview-summary.html`
- Keine Frames, vollständige Inhalte sichtbar

**Vermeiden**:
- Frame-basierte Hauptseiten (`/downloads/catalogues/[Nummer]/`)
- Versionsspezifische Release-URLs (`/releases-xplanung/waermeplan-version-09x`)

### Best Practice: Katalog-URL-Struktur

**Muster**: `https://xleitstelle.de/downloads/catalogues/[Katalog-ID]/overview-summary.html`

**Bekannte Katalog-IDs**:
- **468**: Wärmeplan 0.84 (August 2025, neueste)
- **437**: Wärmeplan 0.7 (Dezember 2024)
- Weitere IDs für andere XPlanung-Versionen (z.B. XPlanung 6.0, 6.1)

**Einzelobjekt-Zugriff**: `https://xleitstelle.de/downloads/catalogues/[Katalog-ID]/XPlanGML/[Package]/[Subpackage]/[Objektname].html`

---

## Vergleich: Traditionelle Website vs. Repository

| Aspekt | xleitstelle.de | gitlab.opencode.de |
|--------|----------------|-------------------|
| **Sitemap** | ✗ Keine XML-Sitemap | ✗ Nicht relevant (Repository) |
| **Navigation** | Menü-basiert, mehrschichtig | Code-basiert (Ordnerstruktur) |
| **Objektkataloge** | HTML-Seiten (frame-basiert) | Nicht verfügbar (nur Quellcode) |
| **Direkte URLs** | ✓ Funktionieren (ohne Frames) | ✗ JavaScript-Rendering erforderlich |
| **WebFetch-Zugriff** | ✓ Vollständig (außer Frames) | ✗ Nur Metadaten |
| **Primäre Funktion** | Dokumentation, Spezifikationen | Versionskontrolle, Entwicklung |

**Schlussfolgerung**: Für Objektkataloge und Attributbeschreibungen ist **xleitstelle.de die einzige praktikable Quelle**. GitLab OpenCode enthält nur Quellcode (XML-Schemas), keine menschenlesbaren Kataloge.

---

## Zusammenfassung

**Problem**: Keine XML-Sitemap, komplexe Navigation zu Wärmeplan-Objektkatalogen

**Lösung - Direkte URLs**:
- Wärmeplan 0.84 (neueste): https://xleitstelle.de/downloads/catalogues/468/overview-summary.html
- Wärmeplan 0.7: https://xleitstelle.de/downloads/catalogues/437/overview-summary.html

**Technische Herausforderung**: HTML-Frames (veraltet)
- **Workaround**: overview-summary.html nutzen

**Navigation für Menschen**:
1. xleitstelle.de/xplanung
2. Menü: "Fachschema Wärmeplan"
3. Oder: Suche nach "Objektartenkatalog"

**Navigation für Tools**:
- Direkte URLs zu `/downloads/catalogues/[ID]/overview-summary.html`
- Einzelobjekte: `/downloads/catalogues/[ID]/XPlanGML/Wärmeplan/WP_Objekte/[Objektname].html`

**Status**: Dokumentiert für effizientere Navigation

---

**Erstellt am**: 2025-11-21
**Zweck**: Navigationshilfe für XLeitstelle-Objektkataloge
**Bezug**: Geo-Datenformate Research, XPlanung/Wärmeplan-Dokumentation
