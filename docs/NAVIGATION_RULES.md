---
layout: default
title: Navigation Rules
parent: Dokumentation
nav_order: 4
permalink: /docs/navigation-rules/
---

# Navigation Rules

## Jekyll Theme und GitHub Pages Konfiguration

### Übersicht

Dieses Repository wird als **GitHub Pages Website** veröffentlicht mit dem **Just the Docs** Theme.

- **Theme**: [Just the Docs](https://just-the-docs.com/)
- **Generator**: Jekyll (automatisch durch GitHub Pages)
- **URL**: https://digitale-waermewende.github.io/Digitale-Waermewende
- **Konfiguration**: `_config.yml` im Repository-Root

### Wichtige Theme-Eigenschaften

**Just the Docs Standardverhalten**:

- Automatische Navigation aus allen `.md` Dateien
- Hierarchische Struktur über Front Matter gesteuert
- **Standard-Limit: 3 Navigationsebenen** (Home → Level 1 → Level 2)
- Sortierung über `nav_order` (niedrigere Zahlen zuerst)

**Anforderungen für dieses Projekt**:

- **Mindestens 4 Navigationsebenen** erforderlich
- **Potentiell 5 Ebenen** für zukünftige Erweiterungen
- Lösung: Verwendung von `nav_exclude` für tiefe Ebenen + manuelle Verlinkung

## Navigations-Hierarchie (4-5 Ebenen)

### Geplante Struktur

```
Level 0: Home (index.md)
├─ Level 1: Stakeholder (stakeholder.md)
│  ├─ Level 2: Bund (stakeholder/bund/index.md)
│  │  ├─ Level 3: BBSR (stakeholder/bund/BBSR/index.md)
│  │  │  └─ Level 4: Einzeldokumente (nav_exclude: true)
│  │  └─ Level 3: KWW-Halle (stakeholder/bund/KWW-Halle/index.md)
│  │     └─ Level 4: Einzeldokumente (nav_exclude: true)
│  └─ Level 2: Länder (stakeholder/laender/index.md)
│     ├─ Level 3: Baden-Württemberg (stakeholder/laender/Baden-Wuerttemberg/index.md)
│     │  └─ Level 4: Einzeldokumente (nav_exclude: true)
│     └─ Level 3: Bayern, Brandenburg, etc.
├─ Level 1: Standards (standards.md)
│  ├─ Level 2: XPlanung (standards/XPlanung/index.md)
│  │  └─ Level 3: Einzeldokumente (nav_exclude: true)
│  └─ Level 2: ALKIS, etc.
└─ Level 1: Dokumentation (docs.md)
   └─ Level 2: Einzeldokumente
```

### Strategie für 4+ Ebenen

- **Ebenen 0-3**: Erscheinen in der automatischen Navigation (mit Front Matter)
- **Ebenen 4+**: Verwenden `nav_exclude: true` und werden aus der Sidebar-Navigation ausgeblendet
- **Ebene 4-5 Zugriff**: Manuelle Verlinkung von der übergeordneten Ebene-3-Indexseite

**Beispiel**:

- Ebene 3 = `stakeholder/bund/BBSR/index.md` → **IN Navigation sichtbar**
- Ebene 4 = `stakeholder/bund/BBSR/2025-09-21_BBSR_Waermeplanung-Forschung.md` → **NICHT in Navigation**, aber verlinkt auf der BBSR-Indexseite

## Index-Seiten für Ebene 3 (Organisationen/Themen)

Ebene-3-Indexseiten (`BBSR/index.md`, `Baden-Wuerttemberg/index.md`, etc.) dienen als **Inhaltsverzeichnis** für Ebene-4-Dokumente:

```markdown
---
layout: default
title: BBSR
parent: Bund
grand_parent: Stakeholder
nav_order: 1
has_children: true
permalink: /stakeholder/bund/bbsr/
---

# Bundesinstitut für Bau-, Stadt- und Raumforschung (BBSR)

## Über das BBSR
[Kurze Beschreibung der Organisation]

## Dokumente

### Forschung und Analysen
- [BBSR Wärmeplanung Forschung](2025-09-21_BBSR_Waermeplanung-Forschung.md) - Wissenschaftliche Begleitung des Wärmeplanungsgesetzes
- [BBSR Stakeholder-Dialog Ergebnispapier](2025-09-21_BBSR_Stakeholder-Dialog-Ergebnispapier.md) - Dokumentation des bundesweiten Dialogs
- [BBSR Analysen KOMPAKT 07/2024](2025-09-21_BBSR-Analysen-KOMPAKT-07-2024.md) - Status quo der kommunalen Wärmeplanung

## Externe Links
- [BBSR Website](https://www.bbsr.bund.de/)
- [BBSR Forschungsprogramm ExWoSt](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/exwost-node.html)
```

**Wichtig**:

- Manuelle Links zu allen Ebene-4-Dokumenten
- Gruppierung nach Themen/Kategorien
- Kurze Beschreibung für jedes Dokument

## Automatische Child-Page Navigation (Just the Docs)

Just the Docs zeigt **automatisch** alle Unterseiten (Child Pages) in der Sidebar-Navigation an, wenn `has_children: true` gesetzt ist.

### Wie es funktioniert

Wenn eine Seite `has_children: true` hat, dann:

1. **Sidebar**: Alle Unterseiten erscheinen automatisch hierarchisch
2. **Content**: Die Seite selbst kann rein beschreibenden Text enthalten
3. **Updates**: Bei neuen Unterseiten automatische Aktualisierung (kein manuelles Editieren nötig)

### Best Practice für Parent-Seiten (Level 1-2)

```markdown
---
layout: default
title: Stakeholder
nav_order: 2
has_children: true
permalink: /stakeholder/
---

# Stakeholder

Übersicht der beteiligten Akteure auf allen Verwaltungsebenen.

## Bereiche

Alle Unterbereiche sind in der Navigation auf der linken Seite aufgelistet:
- **Bund** - Nationale Koordination und Standards
- **Länder** - Landesspezifische Implementierungen

Die Navigation wird automatisch von Just the Docs aus den Front Matter-Definitionen der Unterseiten generiert.
```

### Vorteile

- ✅ **Keine Redundanz** - Links müssen nicht doppelt gepflegt werden
- ✅ **Automatische Updates** - Neue Unterseiten erscheinen sofort in der Navigation
- ✅ **Kein 404-Risiko** - Keine manuellen Links, die veralten können
- ✅ **Konsistente Navigation** - Immer synchron mit der Sidebar

### Nicht empfohlen

- ❌ Manuelle Links zu Unterseiten im Content (parallel zur Sidebar)
- ❌ Verwendung von `{{ site.baseurl }}` Links zu eigenen Child-Pages
- ❌ Duplikation der Navigationsstruktur im Markdown-Content

### Ausnahme: Level 3 Index-Seiten

Ebene-3-Seiten (wie `BBSR/index.md`) brauchen **manuelle Links** zu Level-4-Dokumenten, weil diese mit `nav_exclude: true` aus der Sidebar ausgeblendet sind.

## Konzept: Organisation vs. Standards

**Wichtige konzeptionelle Trennung** im Repository:

### Organisationen (unter stakeholder/)

**Zweck**: Dokumentation der Institutionen, die Standards verwalten

**Beispiele**:

- **XLeitstelle** (`stakeholder/bund/XLeitstelle/`)
  - Verwaltet: XPlanung, XBau, XTrasse
  - Fokus: Organisation, Aufgaben, Website-Links
  - Verweis auf: Standards-Bereich

- **AdV** (`stakeholder/bund/AdV/`)
  - Verwaltet: ALKIS
  - Fokus: Arbeitsgemeinschaft, Koordination
  - Verweis auf: ALKIS-Standard

### Standards (unter standards/)

**Zweck**: Dokumentation der technischen Standards selbst

**Beispiele**:

- **XPlanung** (`standards/XPlanung/`)
  - Technische Spezifikation für Bauleitplanung
  - Fachschema Wärmeplan
  - Verweis auf: XLeitstelle (Organisation)

- **ALKIS** (`standards/ALKIS/`)
  - Amtliches Liegenschaftskatasterinformationssystem
  - Technisches Datenmodell (AAA)
  - Verweis auf: AdV (Organisation)

### Bidirektionale Verlinkung

Organisationen und Standards verweisen wechselseitig aufeinander:

**Organisation → Standards** (von `stakeholder/bund/XLeitstelle/index.md`):

```markdown
## Verwaltete Standards
- [XPlanung](../../../standards/XPlanung/index.md)
- [XBau](../../../standards/XBau/index.md)
- [XTrasse](../../../standards/XTrasse/index.md)
```

**Standard → Organisation** (von `standards/XPlanung/index.md`):

```markdown
## Verwaltende Organisation
[XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md)
```

## Konzept: Gesetze

**Zweck**: Zentrale Dokumentation relevanter Gesetze mit Links zu Original-Texten und AI-Analysen.

### Grundprinzipien für Gesetzes-Dokumentation

1. **Original-Gesetzestexte verlinken**
   - Primärquelle: [Gesetze im Internet](https://www.gesetze-im-internet.de/)
   - Deep-Links zu einzelnen Paragraphen verwenden
   - Stand des Gesetzes angeben

2. **Klare Kennzeichnung von Inhalten**
   - **Original-Zitate**: Blockquote-Format (>) mit Quellenangabe
   - **AI-Analysen**: Deutlicher Disclaimer mit Datum und Modell
   - **Rechtlicher Hinweis**: Am Ende jeder Analyse

3. **Flache Hierarchie**
   - Standard: Alle Dateien direkt im Gesetzes-Ordner
   - Optional: Thematische Unterordner bei >10 Paragraphen

### Ordnerstruktur

```
gesetze/
├── index.md                      # Hauptübersicht aller Gesetze
├── WPG/
│   ├── index.md                  # Wärmeplanungsgesetz Übersicht
│   ├── wpg-§3-begriffe.md       # AI-Analyse zu §3
│   └── zusammenfassung.md        # Gesamtübersicht (AI)
├── BauGB/
│   ├── index.md                  # Baugesetzbuch Übersicht
│   ├── baugb-§9-bauplanung.md   # Einzelparagraph
│   └── xplanung-relevanz.md      # Thematische Übersicht
├── TKG/
│   └── index.md                  # Telekommunikationsgesetz
└── GEG/
    └── index.md                  # Gebäudeenergiegesetz
```

### Kennzeichnung von Gesetzeszitaten

**Original-Zitat** (immer mit Blockquote und Quelle):

```markdown
> **§3 Begriffsbestimmungen**
>
> (1) [Vollständiger Wortlaut...]
>
> (2) [Vollständiger Wortlaut...]

**Quelle:** [§3 WPG](https://www.gesetze-im-internet.de/wpg/__3.html), Gesetze im Internet
```

**AI-Analyse** (immer mit Disclaimer):

```markdown
## AI-Analyse

⚠️ **Hinweis:** Die folgende Analyse wurde von Claude (Anthropic) erstellt und stellt keine Rechtsberatung dar.

**Erstellt:** 2025-11-20
**AI-Modell:** Claude Sonnet 4.5 (Anthropic)

### Zusammenfassung

[AI-generierte Analyse...]
```

**Rechtlicher Disclaimer** (am Ende jeder Analyse):

```markdown
⚠️ **Rechtlicher Hinweis:**
Diese AI-Analyse dient ausschließlich informativen Zwecken und ersetzt keine qualifizierte Rechtsberatung. Für rechtsverbindliche Auskünfte konsultieren Sie bitte einen Rechtsanwalt oder die zuständige Behörde.

**Primärquelle:** [Link zum Original auf Gesetze im Internet]
```

### Querverweise zwischen Bereichen

**Von Gesetzen zu Standards**:

```markdown
## Verwandte Standards
- [XPlanung](../../standards/XPlanung/) - Digitale Bauleitplanung nach BauGB §9
```

**Von Standards zu Gesetzen**:

```markdown
## Rechtliche Grundlagen
- [Baugesetzbuch (BauGB)](../../gesetze/BauGB/) - Gesetzliche Basis für Bauleitplanung
- [§9 BauGB](../../gesetze/BauGB/baugb-§9-bauplanung.md) - Inhalt des Bebauungsplans
```

**Von Stakeholdern zu Gesetzen**:

```markdown
## Relevante Gesetze
- [Wärmeplanungsgesetz (WPG)](../../gesetze/WPG/) - Bundesgesetz zur Wärmeplanung
```

### Relevante Gesetze für Digitale Wärmewende

- **WPG** - Wärmeplanungsgesetz (Hauptgesetz)
- **BauGB** - Baugesetzbuch (für XPlanung relevant)
- **GEG** - Gebäudeenergiegesetz (Schnittstellen zur Wärmeplanung)
- **TKG** - Telekommunikationsgesetz (für XTrasse/XBreitband)

## Verwandte Dokumente

- [Front-Matter Templates](FRONTMATTER_TEMPLATES.md) - Front-Matter-Struktur
- [URL Guidelines](URL_GUIDELINES.md) - URL-Formatierung und interne Links
- [PDF Workflow](PDF_WORKFLOW.md) - Umgang mit PDF-Dateien
- [Structure Guide](STRUCTURE_GUIDE_Digitale-Waermewende.md) - Hauptdokument
