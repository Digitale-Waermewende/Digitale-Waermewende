---
layout: default
title: "Objektartenkatalog-Vergleich"
parent: XPlanung
grand_parent: Standards
nav_exclude: true
permalink: /standards/xplanung/objektartenkatalog-vergleich/
---

# Objektartenkatalog-Vergleich: XPlanung, Wärmeplan und XTrasse

**Erfassungsdatum**: 2025-11-21
**Typ**: Vergleichende Analyse
**Umfang**: Objektartenkataloge, Package-Strukturen, Basisklassen-Hierarchie
**Primärquellen**: xleitstelle.de HTML-Objektartenkataloge

---

## Executive Summary

Dieser Bericht analysiert die Objektartenkataloge der drei XLeitstelle-Standards **XPlanung 6.1**, **Wärmeplan 0.84** und **XTrasse 2.0**. Die Analyse zeigt eine gemeinsame Basisklassen-Hierarchie (**XP_Basisobjekte**), fachspezifische Objektgruppen (**BP_\***, **WP_\***, **XT_\***) und die Integration aller drei Standards in ein kohärentes GML-basiertes Datenmodell.

**Kernerkenntnisse**:
- **Gemeinsame Basis**: Alle drei Standards erben von XP_Basisobjekte (Abstrakte Oberklassen)
- **Fachliche Spezialisierung**: Bebauungsplan (BP\_\*), Wärmeplan (WP\_\*), Leitungsnetze (XT\_\*)
- **Komplementäre Funktion**: XPlanung (Flächennutzung), Wärmeplan (Energieplanung), XTrasse (Leitungsinfrastruktur)

---

## 1. Katalog-URLs und Versionen

### 1.1 XPlanung 6.1 (Hauptstandard)

**Katalog-ID**: 447
**Hauptkatalog**: https://xleitstelle.de/downloads/catalogues/447/
**Übersicht ohne Frames**: https://xleitstelle.de/downloads/catalogues/447/overview-summary.html
**Offizielle Seite**: https://xleitstelle.de/releases/objektartenkatalog_6_0

**Version**: XPlanGML 6.1
**Status**: Veröffentlicht
**Umfang**: 7 Hauptdomänen, 40+ spezialisierte Packages

**URL-Muster für Einzelobjekte**:
```
https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/[Package]/[Subpackage]/[Objektname].html
```

**Beispiel**:
- Bebauungsplan-Objekt: `/447/XPlanGML%206_1/Bebauungsplan/BP_Sonstiges/BP_Plan.html`

---

### 1.2 Wärmeplan 0.84 (Fachschema)

**Katalog-ID**: 468
**Hauptkatalog**: https://xleitstelle.de/downloads/catalogues/468/
**Übersicht ohne Frames**: https://xleitstelle.de/downloads/catalogues/468/overview-summary.html
**Offizielle Seite**: https://xleitstelle.de/releases/objektartenkatalogWaermeplan

**Version**: 0.84 (Entwurf)
**Datum**: 27.08.2025
**Schema-Basis**: XPlanGML 6.1
**Beschreibung**: "Entwurf für ein Fachschema zur Modellierung von kommunalen Wärmeplänen"

**Umfang**: 3 Hauptpackages (Basisklassen, Wärmeplan-spezifisch)

**URL-Muster für Einzelobjekte**:
```
https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/[Subpackage]/[Objektname].html
```

**Beispiel**:
- Wärmeplan-Objekt: `/468/XPlanGML%206_1/Wärmeplan/WP_Objekte/WP_WaermeverbrauchLinie.html`

---

### 1.3 XTrasse 2.0 (Leitungsnetze)

**Katalog-ID**: 443
**Hauptkatalog**: https://xleitstelle.de/downloads/catalogues/443/
**Übersicht ohne Frames**: https://xleitstelle.de/downloads/catalogues/443/overview-summary.html
**Offizielle Seite**: https://xleitstelle.de/releases/objektartenkatalogxtrasse

**Version**: XTrasse 2.0
**Status**: Veröffentlicht
**Beschreibung**: Schema für die Modellierung von Leitungsnetzen

**Umfang**: 3 Hauptdomänen (Breitbandausbau, Bestandsnetze, Infrastrukturausbau), 4 Unterdomänen

**URL-Muster für Einzelobjekte**:
```
https://xleitstelle.de/downloads/catalogues/443/XTrasse/[Domäne]/[Subpackage]/[Objektname].html
```

**Beispiel**:
- Leitungsobjekt: `/443/XTrasse/Bestandsnetze/BST_Objekte/BST_Leitung.html`

---

## 2. Package-Struktur im Vergleich

### 2.1 XPlanung 6.1 - Vollständige Package-Hierarchie

```
XPlanGML 6_1/ (Root)
├── Basisklassen/                    # GEMEINSAM mit Wärmeplan + XTrasse
│   ├── XP_Basisobjekte              # Abstrakte Oberklassen
│   ├── XP_Codelisten                # Externe Codelisten
│   ├── XP_Enumerationen             # Aufzählungen
│   ├── XP_Geometrietypen            # Geometrie-Spezialisierungen
│   ├── XP_KomplexeDatentypen        # Komplexe Datentypen
│   └── XP_Praesentationsobjekte     # Graphische Darstellung
│
├── Bebauungsplan/                   # NUR XPlanung (BP_*)
│   ├── BP_Basisobjekte
│   ├── BP_Bebauung
│   ├── BP_Erhaltungssatzung_Denkmalschutz
│   ├── BP_Gemeinbedarf_Spiel_Sportanlagen
│   ├── BP_Landwirtschaft_Wald_und_Grünflächen
│   ├── BP_Naturschutz_Landschaftsbild_Naturhaushalt
│   ├── BP_Sonstiges
│   ├── BP_Umwelt
│   ├── BP_Verkehr
│   ├── BP_Wasser
│   └── BP_Ver_und_Entsorgung
│
├── Flaechennutzungsplan/            # NUR XPlanung (FP_*)
│   ├── FP_Basisobjekte
│   ├── FP_Bebauung
│   ├── FP_Gemeinbedarf_Spiel_Sportanlagen
│   ├── FP_Landwirtschaft_Wald_und_Grünflächen
│   ├── FP_Naturschutz_Landschaftsbild_Naturhaushalt
│   ├── FP_Sonstiges
│   ├── FP_Verkehr
│   ├── FP_Wasser
│   └── FP_Ver_und_Entsorgung
│
├── Landschaftsplan/                 # NUR XPlanung (LP_*)
│   ├── LP_Basisobjekte
│   ├── LP_Flaechenschutzobjekte
│   ├── LP_Landschaftsbildobjekte
│   ├── LP_SchutzPflegeEntwicklung
│   └── LP_Sonstiges
│
├── Raumordnungsplan/                # NUR XPlanung (RP_*)
│   ├── RP_Basisobjekte
│   ├── RP_Freiraumstruktur
│   ├── RP_Siedlungsstruktur
│   ├── RP_Sonstiges
│   └── RP_Verkehr
│
└── SonstigePlanwerke/               # NUR XPlanung (SO_*)
    ├── SO_Basisobjekte
    ├── SO_Bereich
    ├── SO_Bodenschutz
    ├── SO_Denkmalschutz
    └── SO_Sonstiges
```

**Anzahl Packages**: ~40 spezialisierte Packages
**Präfixe**: BP\_, FP\_, LP\_, RP\_, SO\_, XP\_

---

### 2.2 Wärmeplan 0.84 - Package-Hierarchie

```
XPlanGML 6_1/ (Root - GETEILT mit XPlanung)
├── Basisklassen/                    # GEMEINSAM mit XPlanung
│   ├── XP_Basisobjekte
│   ├── XP_Codelisten
│   ├── XP_Enumerationen
│   ├── XP_Geometrietypen
│   ├── XP_KomplexeDatentypen
│   └── XP_Praesentationsobjekte
│
└── Wärmeplan/                       # NUR Wärmeplan (WP_*)
    ├── WP_Basisobjekte              # 9 Klassen
    │   ├── WP_Plan                  # Konkret
    │   ├── WP_Bereich               # Konkret
    │   ├── WP_Objekt                # Abstrakt
    │   ├── WP_Baublock              # Abstrakt
    │   ├── WP_Flächenobjekt         # Abstrakt
    │   ├── WP_Linienobjekt          # Abstrakt
    │   ├── WP_Punktobjekt           # Abstrakt
    │   ├── WP_Geometrieobjekt       # Abstrakt
    │   └── WP_Version               # Datentyp
    │
    ├── WP_Objekte                   # 30+ Fachobjekte
    │   ├── Gebäude (WP_Gebaeude)
    │   ├── Netzinfrastruktur (WP_Fernwaermenetz, WP_Nahwaermenetz, ...)
    │   ├── Verbrauchsobjekte (WP_GebaeudeWaermebedarf, WP_WaermeverbrauchLinie, ...)
    │   ├── Anschlussgebiete (WP_Anschlusszwang, WP_AnschlussSynthMethan, ...)
    │   ├── Planungsobjekte (WP_Netzausbaugebiet, WP_Transformationsgebiet, ...)
    │   ├── Potenziale (WP_GeothermischesPotenzialgeb, WP_Solarthermieflaeche, ...)
    │   └── Schutzgebiete (WP_Ausschlussgebiet)
    │
    └── WP_Sonstiges                 # 6 Datentypen
        └── Komplexe Datenstrukturen (aggregierte Daten, Maßnahmen)
```

**Anzahl Packages**: 3 (Basisklassen geteilt, 2 Wärmeplan-spezifisch)
**Präfixe**: WP\_ (Wärmeplan), XP\_ (geteilt)

---

### 2.3 XTrasse 2.0 - Package-Hierarchie

```
XTrasse/ (Root - SEPARATES Schema)
├── Basisklassen/                    # TEILWEISE GEMEINSAM
│   ├── XP_Basisobjekte              # Ähnlich XPlanung
│   └── XP_Enumerationen             # Aufzählungen
│
├── Breitbandausbau/                 # NUR XTrasse (BRA_*)
│   ├── BRA_Basisobjekte
│   └── BRA_Objekte
│
├── Bestandsnetze/                   # NUR XTrasse (BST_*)
│   ├── BST_Basisobjekte
│   └── BST_Objekte
│       ├── Leitungen (BST_Leitung, BST_Leitungsabschnitt)
│       ├── Anschlüsse (BST_Anschlusspunkt, BST_Muffe)
│       ├── Schächte und Verteiler
│       └── Leitungssparten (Wärme, Gas, Strom, Wasser, Abwasser, Telekom)
│
├── Infrastrukturausbau/             # NUR XTrasse (IP_*, IGP_*, PFS_*, RVP_*)
│   ├── IP_Basisobjekte              # Gemeinsame Basis
│   │
│   ├── Infrastrukturgebieteplan/
│   │   ├── IGP_Basisobjekte
│   │   └── IGP_Objekte
│   │
│   ├── Planfeststellung/
│   │   ├── PFS_Basisobjekte
│   │   └── PFS_Objekte
│   │
│   └── Raumvertraeglichkeit/
│       ├── RVP_Basisobjekte
│       └── RVP_Objekte
│
└── Infrastrukturatlas/              # NUR XTrasse (ISA_*)
    ├── ISA_Basisobjekte
    └── ISA_Objekte
```

**Anzahl Packages**: ~15 spezialisierte Packages
**Präfixe**: BRA\_, BST\_, IP\_, IGP\_, PFS\_, RVP\_, ISA\_, XP\_

---

## 3. Package-Struktur Vergleichstabelle

| Package-Kategorie          | XPlanung 6.1       | Wärmeplan 0.84    | XTrasse 2.0       | Funktion                          |
|----------------------------|--------------------|--------------------|-------------------|-----------------------------------|
| **XP_Basisobjekte**        | ✓ (~15 Klassen)    | ✓ (geteilt)        | ✓ (~10 Klassen)   | Gemeinsame abstrakte Oberklassen  |
| **XP_Geometrietypen**      | ✓                  | ✓ (geteilt)        | ✓                 | Spezialisierte Geometrien         |
| **XP_Enumerationen**       | ✓                  | ✓ (geteilt)        | ✓                 | Aufzählungswerte                  |
| **XP_Codelisten**          | ✓                  | ✓ (geteilt)        | ✗                 | Externe Codelisten                |
| **Bebauungsplan (BP\_\*)** | ✓ (11 Packages)    | ✗                  | ✗                 | Bauleitplanung                    |
| **Flächennutzung (FP\_\*)** | ✓ (9 Packages)     | ✗                  | ✗                 | Flächennutzungsplanung            |
| **Landschaft (LP\_\*)**    | ✓ (5 Packages)     | ✗                  | ✗                 | Landschaftsplanung                |
| **Raumordnung (RP\_\*)**   | ✓ (5 Packages)     | ✗                  | ✗                 | Raumordnungsplanung               |
| **Wärmeplan (WP\_\*)**     | ✗                  | ✓ (3 Packages)     | ✗                 | Kommunale Wärmeplanung            |
| **Bestandsnetze (BST\_\*)** | ✗                  | ✗                  | ✓                 | Leitungsbestand                   |
| **Breitband (BRA\_\*)**    | ✗                  | ✗                  | ✓                 | Glasfaserausbau                   |
| **Infrastruktur (IGP, PFS, RVP)** | ✗            | ✗                  | ✓ (3 Unterdomänen)| Infrastrukturausbau-Verfahren     |

**Legende**:
- ✓ = Vorhanden
- ✗ = Nicht vorhanden
- (geteilt) = Package wird gemeinsam genutzt

---

## Verwandte Standards

### XPlanung
- [XPlanung Hauptdokument](index.md) - Überblick und Relevanz für Wärmeplanung

### XTrasse
- [XTrasse Hauptdokument](../XTrasse/index.md) - Leitungsnetze und Trassenplanung

---

*Dieses Dokument wird in den folgenden Phasen erweitert mit:*
- Phase 2 ✅: Package-Struktur-Vergleich (abgeschlossen)
- Phase 3: Basisklassen-Hierarchie und Vererbung
- Phase 4: Fachspezifische Objektgruppen-Analyse
- Phase 5: Praktische Beispiele und Navigation
