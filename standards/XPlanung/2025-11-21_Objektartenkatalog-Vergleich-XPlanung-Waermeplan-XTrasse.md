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

## 4. Basisklassen-Hierarchie und Vererbung

### 4.1 Gemeinsame Basis: XP_Basisobjekte

Alle drei Standards (XPlanung, Wärmeplan, XTrasse) nutzen **XP_Basisobjekte** als gemeinsame Basis für ihre Objektartenkataloge. Diese Package enthält abstrakte Oberklassen, die die grundlegende Struktur für alle Fachobjekte definieren.

#### XP_Objekt (Root-Basisklasse)

**XP_Objekt** ist die zentrale abstrakte Basisklasse mit **20 grundlegenden Attributen**:

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `uuid` | CharacterString | Eindeutiger Identifikator (UUID) |
| `rechtsstand` | XP_Rechtsstand | Rechtsstatus des Objekts |
| `rechtscharakter` | XP_Rechtscharakter | Rechtliche Bindungswirkung |
| `gehoertZuBereich` | XP_Bereich | Zuordnung zu Planbereich |
| `type` | XP_PlanArt | Art des Plans |
| `text` | CharacterString | Textliche Beschreibung |
| `aufschrift` | CharacterString | Planaufschrift |
| `refTextInhalt` | XP_ExterneReferenz | Verweis auf externe Textinhalte |
| `hatGenerAttribut` | XP_GenerAttribut | Generische Attribute |
| ... | ... | (15 weitere Attribute) |

**Vererbungshierarchie von XP_Objekt**:

```
XP_Objekt (abstract)
├── BP_Objekt (Bebauungsplan) → BP_* Fachobjekte
├── FP_Objekt (Flächennutzungsplan) → FP_* Fachobjekte
├── LP_Objekt (Landschaftsplan) → LP_* Fachobjekte
├── RP_Objekt (Raumordnungsplan) → RP_* Fachobjekte
├── SO_Objekt (Sonstige Planwerke) → SO_* Fachobjekte
└── WP_Objekt (Wärmeplan) → WP_* Fachobjekte
```

---

### 4.2 XPlanung 6.1 - Basisklassen

**Package**: `XPlanGML 6_1/Basisklassen/XP_Basisobjekte`

| Klasse | Typ | Funktion | Katalog-URL |
|--------|-----|----------|-------------|
| **XP_Objekt** | abstract | Root-Basisklasse für alle Fachobjekte | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Objekt.html) |
| **XP_Plan** | abstract | Basisklasse für alle Planwerke | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Plan.html) |
| **XP_Bereich** | abstract | Basisklasse für Planbereiche | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Bereich.html) |
| **XP_Flaechenobjekt** | abstract | Geometrie-Basisklasse (Fläche) | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Flaechenobjekt.html) |
| **XP_Linienobjekt** | abstract | Geometrie-Basisklasse (Linie) | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Linienobjekt.html) |
| **XP_Punktobjekt** | abstract | Geometrie-Basisklasse (Punkt) | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Punktobjekt.html) |
| **XP_Geometrieobjekt** | abstract | Geometrie-Basisklasse (multi) | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_Geometrieobjekt.html) |
| XP_TPO | abstract | Text-Punkt-Objekt | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_TPO.html) |
| XP_PTO | abstract | Plan-Text-Objekt | [Link](https://xleitstelle.de/downloads/catalogues/447/XPlanGML%206_1/Basisklassen/XP_Basisobjekte/XP_PTO.html) |
| ... | ... | (weitere 9 Klassen) | ... |

**Gesamt**: ~18 Klassen (12 abstrakt, 6 konkret)

---

### 4.3 Wärmeplan 0.84 - Basisklassen

**Package**: `XPlanGML 6_1/Wärmeplan/WP_Basisobjekte`

#### Gemeinsame Basis mit XPlanung

Wärmeplan nutzt **dieselben XP_Basisobjekte** wie XPlanung (geteilt).

#### Wärmeplan-spezifische Basisklassen

| Klasse | Typ | Funktion | Erbt von | Katalog-URL |
|--------|-----|----------|----------|-------------|
| **WP_Plan** | konkret | Wärmeplan-Hauptobjekt | XP_Plan | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Plan.html) |
| **WP_Bereich** | konkret | Wärmeplan-Bereich | XP_Bereich | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Bereich.html) |
| **WP_Objekt** | abstract | Basisklasse für WP_* Fachobjekte | XP_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Objekt.html) |
| **WP_Baublock** | abstract | Basisklasse für Baublöcke | WP_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Baublock.html) |
| **WP_Flächenobjekt** | abstract | Wärmeplan-Flächenobjekt | WP_Objekt + XP_Flaechenobjekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Flaechenobjekt.html) |
| **WP_Linienobjekt** | abstract | Wärmeplan-Linienobjekt | WP_Objekt + XP_Linienobjekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Linienobjekt.html) |
| **WP_Punktobjekt** | abstract | Wärmeplan-Punktobjekt | WP_Objekt + XP_Punktobjekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Punktobjekt.html) |
| **WP_Geometrieobjekt** | abstract | Wärmeplan-Geometrieobjekt | WP_Objekt + XP_Geometrieobjekt | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Geometrieobjekt.html) |
| WP_Version | DataType | Versionsnummer-Datentyp | - | [Link](https://xleitstelle.de/downloads/catalogues/468/XPlanGML%206_1/Wärmeplan/WP_Basisobjekte/WP_Version.html) |

**Gesamt**: 9 Klassen (6 abstrakt, 2 konkret, 1 DataType)

**Vererbungshierarchie Wärmeplan**:

```
XP_Objekt (XPlanung)
└── WP_Objekt (abstract)
    ├── WP_Baublock (abstract)
    ├── WP_Flächenobjekt (abstract) ← erbt auch von XP_Flaechenobjekt
    │   └── WP_Gebaeude, WP_Fernwaermenetz, WP_Anschlusszwang, ...
    ├── WP_Linienobjekt (abstract) ← erbt auch von XP_Linienobjekt
    │   └── WP_WaermeverbrauchLinie, WP_Leitung, ...
    ├── WP_Punktobjekt (abstract) ← erbt auch von XP_Punktobjekt
    │   └── WP_Speicher, WP_Erzeuger, ...
    └── WP_Geometrieobjekt (abstract) ← erbt auch von XP_Geometrieobjekt
        └── (Multi-Geometrie Objekte)

XP_Plan (XPlanung)
└── WP_Plan (konkret)

XP_Bereich (XPlanung)
└── WP_Bereich (konkret)
```

---

### 4.4 XTrasse 2.0 - Basisklassen

**Package**: `XTrasse/Basisklassen/XP_Basisobjekte`

#### XTrasse-Basisklassen (separate Implementierung)

XTrasse hat eine **eigene Implementierung** der XP_Basisobjekte (nicht geteilt mit XPlanung):

| Klasse | Typ | Funktion | Katalog-URL |
|--------|-----|----------|-------------|
| **XP_Objekt** | abstract | Root-Basisklasse (XTrasse-Version) | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Objekt.html) |
| **XP_Plan** | abstract | Basisklasse für XTrasse-Pläne | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Plan.html) |
| **XP_Bereich** | abstract | Basisklasse für XTrasse-Bereiche | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Bereich.html) |
| XP_Flaechenobjekt | abstract | Geometrie-Basisklasse (Fläche) | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Flaechenobjekt.html) |
| XP_Linienobjekt | abstract | Geometrie-Basisklasse (Linie) | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Linienobjekt.html) |
| XP_Punktobjekt | abstract | Geometrie-Basisklasse (Punkt) | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Basisklassen/XP_Basisobjekte/XP_Punktobjekt.html) |
| ... | ... | (weitere 3 Klassen) | ... |

**Gesamt**: ~9 Klassen (8 abstrakt, 1 konkret)

#### XTrasse-spezifische Basisklassen (Bestandsnetze)

**Package**: `XTrasse/Bestandsnetze/BST_Basisobjekte`

| Klasse | Typ | Funktion | Erbt von | Katalog-URL |
|--------|-----|----------|----------|-------------|
| **BST_Objekt** | abstract | Basisklasse für Bestandsnetz-Objekte | XP_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Objekt.html) |
| BST_Multi_Flaechenobjekt | abstract | Multi-Flächenobjekt | BST_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Multi_Flaechenobjekt.html) |
| BST_Multi_Linienobjekt | abstract | Multi-Linienobjekt | BST_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Multi_Linienobjekt.html) |
| BST_Multi_Punktobjekt | abstract | Multi-Punktobjekt | BST_Objekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Multi_Punktobjekt.html) |
| BST_Flaechenobjekt | abstract | Flächenobjekt | BST_Objekt + XP_Flaechenobjekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Flaechenobjekt.html) |
| BST_Linienobjekt | abstract | Linienobjekt | BST_Objekt + XP_Linienobjekt | [Link](https://xleitstelle.de/downloads/catalogues/443/XTrasse/Bestandsnetze/BST_Basisobjekte/BST_Linienobjekt.html) |

**Gesamt**: 6 Klassen (6 abstrakt)

**Vererbungshierarchie XTrasse**:

```
XP_Objekt (XTrasse-Version)
├── BST_Objekt (Bestandsnetze) → BST_* Fachobjekte
├── BRA_Objekt (Breitbandausbau) → BRA_* Fachobjekte
├── IGP_Objekt (Infrastrukturgebieteplan) → IGP_* Fachobjekte
├── PFS_Objekt (Planfeststellung) → PFS_* Fachobjekte
└── RVP_Objekt (Raumverträglichkeit) → RVP_* Fachobjekte

XP_Plan (XTrasse-Version)
├── BST_Plan (Bestandsnetz-Plan)
├── BRA_Plan (Breitbandausbau-Plan)
└── [weitere Plan-Typen]
```

---

### 4.5 Basisklassen-Vergleichstabelle

| Basisklasse | XPlanung 6.1 | Wärmeplan 0.84 | XTrasse 2.0 | Gemeinsam? |
|-------------|--------------|----------------|-------------|------------|
| **XP_Objekt** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja, aber separate Implementierungen |
| **XP_Plan** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja |
| **XP_Bereich** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja |
| **XP_Flaechenobjekt** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja |
| **XP_Linienobjekt** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja |
| **XP_Punktobjekt** | ✓ (abstract) | ✓ (geteilt) | ✓ (separate Version) | ⚠️ Konzeptuell ja |
| **WP_Objekt** | ✗ | ✓ (WP-spezifisch) | ✗ | ✗ Nur Wärmeplan |
| **WP_Plan** | ✗ | ✓ (konkret) | ✗ | ✗ Nur Wärmeplan |
| **WP_Bereich** | ✗ | ✓ (konkret) | ✗ | ✗ Nur Wärmeplan |
| **BST_Objekt** | ✗ | ✗ | ✓ (XTrasse-spezifisch) | ✗ Nur XTrasse |
| **BRA_Objekt** | ✗ | ✗ | ✓ (XTrasse-spezifisch) | ✗ Nur XTrasse |
| BP_Objekt | ✓ | ✗ | ✗ | ✗ Nur XPlanung |
| FP_Objekt | ✓ | ✗ | ✗ | ✗ Nur XPlanung |
| LP_Objekt | ✓ | ✗ | ✗ | ✗ Nur XPlanung |
| RP_Objekt | ✓ | ✗ | ✗ | ✗ Nur XPlanung |
| SO_Objekt | ✓ | ✗ | ✗ | ✗ Nur XPlanung |

**Legende**:
- ✓ = Vorhanden
- ✗ = Nicht vorhanden
- ⚠️ = Konzeptuell gemeinsam, aber separate Implementierung (XTrasse)
- (geteilt) = XPlanung und Wärmeplan teilen sich die Implementierung
- (separate Version) = XTrasse hat eigene Implementierung

**Wichtige Erkenntnis**:

- **XPlanung + Wärmeplan**: Teilen sich die XP_Basisobjekte-Implementierung (gemeinsames Schema)
- **XTrasse**: Hat eine separate Implementierung der XP_Basisobjekte (konzeptuell ähnlich, aber eigenständig)
- **Fachspezifische Basisklassen**: WP_Objekt (Wärmeplan), BP_Objekt/FP_Objekt/LP_Objekt/RP_Objekt/SO_Objekt (XPlanung), BST_Objekt/BRA_Objekt/... (XTrasse)

---

## 5. Fachspezifische Objektgruppen im Vergleich

Diese Sektion analysiert die fachspezifischen Objektgruppen (Fachobjekte), die über die gemeinsamen Basisklassen hinausgehen.

### 5.1 XPlanung 6.1 - Bebauungsplan-Objekte (BP_*)

**Zweck**: Modellierung von Bebauungsplänen gemäß BauGB §§ 8-10

| Objektgruppe | Package | Beispielobjekte | Typische Attribute |
|--------------|---------|-----------------|-------------------|
| **Baugebiete** | BP_Bebauung | BP_BauGrenze, BP_Baugebiet, BP_GeschossFlaeche | Art der baulichen Nutzung (§ 9 Abs. 1 Nr. 1 BauGB), GRZ, GFZ |
| **Verkehr** | BP_Verkehr | BP_Strassenverkehrsflaeche, BP_Parkierungsflaeche | Verkehrsart, Nutzungsart |
| **Grünflächen** | BP_Landwirtschaft_Wald_und_Grünflächen | BP_Gruenflaeche, BP_Waldflaeche, BP_Landwirtschaftsflaeche | Zweckbestimmung, Nutzungsart |
| **Ver- und Entsorgung** | BP_Ver_und_Entsorgung | BP_VerEntsorgung, BP_Fernwaerme | Versorgungsart (Gas, Fernwärme, Strom, Wasser) |
| **Naturschutz** | BP_Naturschutz_Landschaftsbild_Naturhaushalt | BP_Schutzflaeche, BP_AusgleichsFlaeche | Schutzziel, Ausgleichsmaßnahmen |
| **Wasser** | BP_Wasser | BP_Gewaesser, BP_Wasserwirtschaft | Gewässerart, Hochwasserschutz |
| **Gemeinbedarf** | BP_Gemeinbedarf_Spiel_Sportanlagen | BP_GemeinbedarfsFlaeche, BP_SpielSportanlage | Zweckbestimmung (Schule, Kita, Sport) |
| **Umwelt** | BP_Umwelt | BP_Immissionsschutz, BP_KlimaLuftboden | Emissionsarten, Schutzmaßnahmen |

**Anzahl Fachobjekte**: 100+ konkrete Objektarten

**Besonderheit**: Sehr detaillierte Modellierung von §9 BauGB Festsetzungen

---

### 5.2 Wärmeplan 0.84 - Wärmeplan-Objekte (WP_*)

**Zweck**: Modellierung kommunaler Wärmepläne gemäß WPG §§ 23-26

#### 5.2.1 Hauptobjektgruppen

| Objektgruppe | Anzahl | Beispielobjekte | Typische Attribute | Geometrie |
|--------------|--------|-----------------|-------------------|-----------|
| **Gebäude** | 2 | WP_Gebaeude ⭐, WP_GebaeudeWaermebedarf | uuid (ALKIS-ID), baualtersklasse, gebaeudetyp | Fläche |
| **Netzinfrastruktur** | 8 | WP_Fernwaermenetz, WP_Nahwaermenetz, WP_Bestandsnetz, WP_Leitung | Netzart, Betreiber, Vorlauftemperatur | Fläche/Linie |
| **Verbrauchsobjekte** | 4 | WP_WaermeverbrauchLinie, WP_Waermebedarf, WP_Waermesenke | Wärmedichte (kWh/m), Verbrauch (MWh/a) | Linie/Fläche |
| **Anschlussgebiete** | 5 | WP_Anschlusszwang, WP_Versorgungsgebiet, WP_AnschlussSynthMethan | Anschlussart, Energieträger, Rechtsstatus | Fläche |
| **Planungsobjekte** | 6 | WP_Netzausbaugebiet, WP_Transformationsgebiet, WP_Quartiersloesung | Umsetzungszeitraum, Maßnahmen | Fläche |
| **Potenziale** | 7 | WP_GeothermischesPotenzialgeb, WP_Solarthermieflaeche, WP_IndustrielleAbwaerme | Potenzial (MWh/a), Nutzungsgrad | Fläche/Punkt |
| **Erzeugung/Speicher** | 5 | WP_Energieerzeugungsanlage, WP_Waermespeicher, WP_Einspeisepunkt | Leistung (MW), Kapazität (MWh) | Punkt/Fläche |
| **Schutzgebiete** | 1 | WP_Ausschlussgebiet | Schutzgrund, Rechtsgrundlage | Fläche |

**Anzahl Fachobjekte**: 38 konkrete Objektarten (30+ in WP_Objekte, 6 Datentypen in WP_Sonstiges)

#### 5.2.2 Besonderheiten Wärmeplan

- **ALKIS-Integration**: WP_Gebaeude.uuid referenziert ALKIS-Gebäude-IDs (16-stellig)
- **Komplexe Datentypen**: WP_EnergieTraegerVerbrauch, WP_SektorVerbrauch (in WP_Sonstiges)
- **Zeitbezug**: Verbrauchsdaten mit Referenzjahr, Versionierung über WP_Version
- **Aggregationsebenen**: Gebäude → Baublock → Bereich → Plan

---

### 5.3 XTrasse 2.0 - Leitungsnetz-Objekte (BST_*, BRA_*, IGP_*, PFS_*, RVP_*)

**Zweck**: Modellierung von Leitungsnetzen (Bestand + Planung) gemäß TKG, EnWG

#### 5.3.1 BST_* (Bestandsnetze)

**Zweck**: Dokumentation vorhandener Leitungsnetze

| Objektgruppe | Beispielobjekte | Typische Attribute | Geometrie |
|--------------|-----------------|-------------------|-----------|
| **Leitungen** | BST_Leitung, BST_Leitungsabschnitt | Sparte (Wärme/Gas/Strom/Wasser/Telekom), Durchmesser, Material | Linie |
| **Verknüpfungen** | BST_Anschlusspunkt, BST_Muffe, BST_Schacht | Anschlussart, Tiefe | Punkt |
| **Verteiler** | BST_Verteiler, BST_Hausanschluss | Versorgungsart, Anzahl Anschlüsse | Punkt |
| **Sparten** | BST_Fernwaerme, BST_Gas, BST_Strom, BST_Wasser | Betreiber, Eigentümer, Baujahr | Linie/Fläche |

**Anzahl Fachobjekte**: 20+ konkrete Objektarten

**Besonderheit**: **BST_Fernwaerme** ist direkt relevant für Wärmeplanung! Dokumentiert bestehende Fernwärmenetze.

#### 5.3.2 BRA_* (Breitbandausbau)

**Zweck**: Glasfaserausbau gemäß TKG

| Objektgruppe | Beispielobjekte | Typische Attribute |
|--------------|-----------------|-------------------|
| **Infrastruktur** | BRA_Trasse, BRA_Kabeltrasse, BRA_Leerrohr | Ausbaustand, Förderung |

**Anzahl Fachobjekte**: 10+ konkrete Objektarten

#### 5.3.3 IGP_*, PFS_*, RVP_* (Infrastrukturausbau-Verfahren)

**Zweck**: Verfahrensdokumentation für Infrastrukturausbau

| Domäne | Zweck | Beispielobjekte |
|--------|-------|-----------------|
| **IGP** (Infrastrukturgebieteplan) | Ausweisen von Infrastrukturgebieten | IGP_Gebiet, IGP_Trasse |
| **PFS** (Planfeststellung) | Planfeststellungsverfahren | PFS_Trasse, PFS_Bauwerk |
| **RVP** (Raumverträglichkeitsprüfung) | Alternativenprüfung | RVP_Trassenkorridore, RVP_Varianten |

**Anzahl Fachobjekte**: 30+ konkrete Objektarten (zusammen)

---

### 5.4 Objektgruppen-Vergleichstabelle

| Fachbereich | XPlanung 6.1 | Wärmeplan 0.84 | XTrasse 2.0 | Überschneidungen |
|-------------|--------------|----------------|-------------|------------------|
| **Bebauungsplan** | ✓ (BP_* 100+ Objekte) | ✗ | ✗ | - |
| **Flächennutzungsplan** | ✓ (FP_* 80+ Objekte) | ✗ | ✗ | - |
| **Landschaftsplan** | ✓ (LP_* 40+ Objekte) | ✗ | ✗ | - |
| **Raumordnung** | ✓ (RP_* 50+ Objekte) | ✗ | ✗ | - |
| **Wärmeplanung** | ✗ | ✓ (WP_* 38 Objekte) | ✗ | - |
| **Gebäude (ALKIS)** | ⚠️ (indirekt über BP_Gebaeude) | ✓ (WP_Gebaeude mit uuid) | ✗ | WP_Gebaeude referenziert ALKIS |
| **Fernwärme** | ⚠️ (BP_Fernwaerme nur Planung) | ✓ (WP_Fernwaermenetz) | ✓ (BST_Fernwaerme Bestand) | **ÜBERSCHNEIDUNG!** |
| **Gas-Netze** | ⚠️ (BP_Gas nur Planung) | ⚠️ (WP_AnschlussSynthMethan) | ✓ (BST_Gas Bestand) | Potenzielle Überschneidung |
| **Leitungsnetze (allgemein)** | ✗ | ⚠️ (WP_Leitung für Wärme) | ✓ (BST_* alle Sparten) | Komplementär |
| **Trassenplanung** | ✗ | ✗ | ✓ (BRA_*, IGP_*, PFS_*, RVP_*) | - |
| **Naturschutz** | ✓ (BP_Schutzflaeche) | ⚠️ (WP_Ausschlussgebiet) | ⚠️ (IGP_Schutzgebiet) | Ähnliche Konzepte |

**Legende**:
- ✓ = Vorhanden und umfangreich
- ⚠️ = Teilweise vorhanden oder nur spezifischer Aspekt
- ✗ = Nicht vorhanden

---

### 5.5 Wichtige Synergien und Überschneidungen

#### 5.5.1 Fernwärme-Dreiklang ⭐

**Problem**: Fernwärme-Infrastruktur wird in allen drei Standards modelliert:

| Standard | Objektart | Fokus | Use Case |
|----------|-----------|-------|----------|
| **XPlanung** | BP_Fernwaerme | Bauleitplanung | Festsetzung von Fernwärme-Versorgungsgebieten (§9 BauGB) |
| **Wärmeplan** | WP_Fernwaermenetz | Energieplanung | Modellierung bestehender + geplanter Fernwärmenetze (WPG §25) |
| **XTrasse** | BST_Fernwaerme | Bestandsdokumentation | Technische Dokumentation vorhandener Fernwärmeleitungen |

**Lösung**: Bidirektionale Referenzierung über `uuid` oder `gml:id`

#### 5.5.2 ALKIS-Integration über WP_Gebaeude ⭐⭐⭐

**WP_Gebaeude.uuid** ist das Schlüsselattribut für die Verknüpfung mit ALKIS (Amtliches Liegenschaftskataster):

```
ALKIS (Gebäude-ID: 16-stellig)
    ↓
WP_Gebaeude.uuid
    ↓
WP_GebaeudeWaermebedarf.gehoertZuBereich (Referenz auf WP_Gebaeude)
    ↓
Energieverbrauchsdaten (MWh/a)
```

**Bedeutung**: Ermöglicht die Verknüpfung von amtlichen Geobasisdaten (ALKIS) mit Energiefachdaten (Wärmeplan)

#### 5.5.3 Schutzgebiete (Naturschutz)

Alle drei Standards modellieren Schutzgebiete, aber mit unterschiedlichem Fokus:

| Standard | Objektart | Rechtliche Basis | Zweck |
|----------|-----------|------------------|-------|
| XPlanung | BP_Schutzflaeche | BNatSchG, BauGB §9 | Bauleitplanerische Festsetzung von Schutzgebieten |
| Wärmeplan | WP_Ausschlussgebiet | WPG, BNatSchG | Gebiete ohne Wärmenetz-Ausbau (Schutzgrund) |
| XTrasse | IGP_Schutzgebiet | TKG, BNatSchG | Restriktionen für Trassenplanung |

**Potenzial**: Einheitliche Referenzierung von Schutzgebieten über externe Codelisten (z.B. BfN-Schutzgebietsverzeichnis)

---

### 5.6 Fazit: Komplementäre Fachdomänen

| Frage | Antwort | Begründung |
|-------|---------|------------|
| **Gibt es verschiedene Gruppen von Objekten?** | Ja | BP_* (Bauleitplanung), WP_* (Energieplanung), BST_*/BRA_* (Leitungsnetze) |
| **Gibt es gemeinsame Gruppen in allen drei Bereichen?** | Ja, auf Basisklassen-Ebene | XP_Basisobjekte (XP_Objekt, XP_Plan, XP_Bereich, Geometrieklassen) |
| **Gibt es Gruppen nur in ein oder zwei Bereichen?** | Ja | BP_*/FP_*/LP_*/RP_*/SO_* nur in XPlanung, WP_* nur in Wärmeplan, BST_*/BRA_*/IGP_*/PFS_*/RVP_* nur in XTrasse |
| **Gibt es Überschneidungen bei Fachobjekten?** | Ja, bei Fernwärme und Schutzgebieten | BP_Fernwaerme (Planung) ↔ WP_Fernwaermenetz (Energieplanung) ↔ BST_Fernwaerme (Bestand) |
| **Sind die Standards komplementär?** | Ja | XPlanung = Flächennutzung (BauGB), Wärmeplan = Energieplanung (WPG), XTrasse = Leitungsinfrastruktur (TKG/EnWG) |

**Kernaussage**: Die drei Standards decken komplementäre Fachdomänen ab, haben aber bei Fernwärme und Schutzgebieten thematische Überschneidungen. Die gemeinsame Basisklassen-Hierarchie (XP_Basisobjekte) ermöglicht eine konsistente GML-basierte Modellierung.

---

## 6. Verwandte Standards und Dokumente

### 6.1 XPlanung
- **[XPlanung Hauptdokument](index.md)** - Überblick und Relevanz für Wärmeplanung
- **[XPlanung Wärmeplan Objektartenkatalog Komplett](2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md)** - Detaillierte Dokumentation aller WP_* Objekte

### 6.2 XTrasse
- **[XTrasse Hauptdokument](../XTrasse/index.md)** - Leitungsnetze und Trassenplanung
  - Besonders relevant: **BST_Fernwaerme** (Bestandsnetze für Fernwärmeleitungen)
  - Komplementär zu WP_Fernwaermenetz (Wärmeplan) und BP_Fernwaerme (XPlanung)

### 6.3 Weitere Integration
- **[ALKIS](../ALKIS/index.md)** - Amtliches Liegenschaftskataster (Gebäudedaten, verknüpft über WP_Gebaeude.uuid)
- **[Datenintegration](../Datenintegration/index.md)** - Zusammenspiel von ALKIS, XPlanung und XTrasse

---

## 7. Zusammenfassung und Ausblick

### 7.1 Kernerkenntnisse

Dieser Vergleich der Objektartenkataloge von XPlanung 6.1, Wärmeplan 0.84 und XTrasse 2.0 zeigt:

1. **Gemeinsame Basis**: Alle drei Standards nutzen XP_Basisobjekte als konzeptionelle Basis
   - XPlanung + Wärmeplan: Teilen sich die Implementierung (gemeinsames Schema)
   - XTrasse: Eigene Implementierung (konzeptuell ähnlich, aber eigenständig)

2. **Fachliche Spezialisierung**:
   - **XPlanung**: 100+ Objekte für Bauleitplanung (BP_*, FP_*, LP_*, RP_*, SO_*)
   - **Wärmeplan**: 38 Objekte für Energieplanung (WP_*)
   - **XTrasse**: 60+ Objekte für Leitungsnetze (BST_*, BRA_*, IGP_*, PFS_*, RVP_*)

3. **Wichtige Synergien**:
   - **Fernwärme-Dreiklang**: BP_Fernwaerme (Planung) ↔ WP_Fernwaermenetz (Energieplanung) ↔ BST_Fernwaerme (Bestand)
   - **ALKIS-Integration**: WP_Gebaeude.uuid verbindet Geobasisdaten mit Energiefachdaten
   - **Schutzgebiete**: Alle drei Standards modellieren Naturschutz (BP_Schutzflaeche, WP_Ausschlussgebiet, IGP_Schutzgebiet)

4. **Komplementäre Funktion**:
   - XPlanung: Flächennutzung (BauGB)
   - Wärmeplan: Energieplanung (WPG)
   - XTrasse: Leitungsinfrastruktur (TKG, EnWG)

### 7.2 Praktische Bedeutung für die Wärmeplanung

Die drei Standards bilden zusammen ein **kohärentes Ökosystem** für die digitale Wärmeplanung:

| Phase | Standard | Rolle |
|-------|----------|-------|
| **Bauleitplanung** | XPlanung (BP_Fernwaerme) | Rechtliche Festsetzung von Versorgungsgebieten (§9 BauGB) |
| **Wärmeplanung** | Wärmeplan (WP_*) | Modellierung von Wärmebedarfen, Netzen, Potenzialen (WPG §§23-26) |
| **Umsetzung** | XTrasse (BST_Fernwaerme) | Technische Dokumentation und Trassenplanung (TKG, EnWG) |

### 7.3 Bidirektionale Referenzierung

Für eine vollständige Integration sollten die Standards über `uuid` oder `gml:id` Attribute referenziert werden:

```
BP_Fernwaerme.gml:id ← Referenz → WP_Fernwaermenetz.gml:id ← Referenz → BST_Fernwaerme.gml:id
        ↓                                    ↓                                   ↓
   Bauleitplan                          Wärmeplan                        Bestandsnetz
```

### 7.4 Ausblick

Zukünftige Entwicklungen könnten umfassen:
- Formalisierte Cross-Referenzen zwischen den Standards
- Gemeinsame Codelisten für Schutzgebiete und Energieträger
- Harmonisierung der Fernwärme-Objektarten (BP_Fernwaerme, WP_Fernwaermenetz, BST_Fernwaerme)
- Integration mit weiteren Fachdaten (BImSchG-Emissionsdaten, EnWG-Netzdaten)

---

*Dokument vollständig - alle 5 Phasen abgeschlossen:*
- Phase 1 ✅: Katalog-URLs identifiziert
- Phase 2 ✅: Package-Struktur-Vergleich
- Phase 3 ✅: Basisklassen-Hierarchie und Vererbung
- Phase 4 ✅: Fachspezifische Objektgruppen-Analyse
- Phase 5 ✅: Vollständige Integration und bidirektionale Links
