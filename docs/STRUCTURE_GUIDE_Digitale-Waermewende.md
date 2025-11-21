---
layout: default
title: Struktur-Leitfaden
parent: Dokumentation
nav_order: 1
permalink: /docs/structure-guide/
---

# Struktur-Leitfaden für das Repository Digitale Wärmewende

## Zweck dieses Dokuments

Dieses Dokument definiert, wie das Repository organisch wachsen soll und nach welchen Regeln Inhalte strukturiert werden.

## Detaillierte Dokumentation

Für spezifische Themen siehe die folgenden Unterdokumente:

- **[Front-Matter Templates](FRONTMATTER_TEMPLATES.md)** - YAML Front-Matter für alle Navigationsebenen
- **[URL Guidelines](URL_GUIDELINES.md)** - URL-Formatierung und interne Verlinkung
- **[Navigation Rules](NAVIGATION_RULES.md)** - Jekyll Theme, Navigation, Hierarchie-Konzepte
- **[PDF Workflow](PDF_WORKFLOW.md)** - Umgang mit PDF-Dateien und Git LFS

## Grundprinzipien

1. **Quellenbasiert**: Primäre Quellen stehen im Mittelpunkt
2. **Evolutionär**: Die Struktur wächst mit den Inhalten
3. **Multi-Stakeholder**: Verschiedene Nutzergruppen (AI-Agenten, Entwickler, Domain-Experten)
4. **Nachvollziehbar**: Jede Quelle wird dokumentiert und eingeordnet
5. **URL-First**: Klickbare, verifizierte URLs zu Original-Informationen in allen Dokumenten

## Schnellreferenz

### Front-Matter (ZWINGEND für alle .md Dateien)

Siehe **[Front-Matter Templates](FRONTMATTER_TEMPLATES.md)** für vollständige Templates.

**Minimal**:
```yaml
---
layout: default
title: "Seitentitel"
---
```

**Research-Dokumente (Level 4)**:
```yaml
---
layout: default
title: "Kurztitel"
parent: [Organisation/Standard]
grand_parent: [Bund/Standards]
nav_exclude: true
permalink: /pfad/
---
```

### URLs (immer als Markdown-Links)

Siehe **[URL Guidelines](URL_GUIDELINES.md)** für Details.

✅ **RICHTIG**: `[Beschreibung](https://url.de)`
❌ **FALSCH**: `URL: https://url.de`

## Dateinamenskonvention

```
YYYY-MM-DD_[Organisation]_[Titel].md
```

Beispiel: `2024-03-15_KWW-Halle_Leitfaden-Waermeplanung.md`

## Dokumentstruktur für Quellen

Jede Quellendatei MUSS folgende Struktur haben:

```markdown
---
layout: default
title: "[Kurztitel für Navigation]"
parent: [Organisation/Bundesland]
grand_parent: [Bund/Länder]
nav_exclude: true              # Für Ebene 4 Dokumente
---

# [Vollständiger Titel]

## Metadaten
- **Organisation**: [Herausgeber]
- **Erfassungsdatum**: YYYY-MM-DD
- **Typ**: [Gesetz|Leitfaden|Standard|Bericht|Recherche|Analyse|...]
- **URLs**:
  - [Beschreibung](https://vollständige-url.de)
  - [Weitere Quelle](https://andere-url.de)
- **Lokal gespeichert**: [Pfad zur PDF-Datei] (Dateigröße)
- **Relevanz**: [Kurze Beschreibung warum wichtig]

## Zusammenfassung
[2-3 Sätze Kernaussage]

## Wichtige Punkte
- [Hauptpunkt 1]
- [Hauptpunkt 2]

## Verbindungen
- Bezug zu: [andere relevante Dokumente]

## Originalzitate
> [Wichtige Passagen im Original]

## Notizen
[Eigene Anmerkungen, offene Fragen]
```

## Aktuelle Struktur

```
Digitale-Waermewende/
├── docs/                 # Projektdokumentation
├── stakeholder/
│   ├── bund/            # Bundesebene
│   └── laender/         # Länderebene
├── standards/           # Datenstandards
└── gesetze/             # Relevante Gesetze
```

## Ordnerstrukturen

### Bundesländer-Organisation

```
stakeholder/laender/
├── index.md                        # Level 2: Übersicht alle Länder
├── Baden-Wuerttemberg/
│   ├── index.md                    # Level 3: Übersicht BW
│   └── [Dokumente].md              # Level 4: Einzeldokumente (nav_exclude: true)
├── Bayern/
│   ├── index.md                    # Level 3: Übersicht Bayern
│   └── [Dokumente].md              # Level 4: Einzeldokumente
└── [Weitere Bundesländer]/
```

### Standards-Organisation

```
standards/
├── index.md (als standards.md im Root)   # Level 1: Übersicht aller Standards
├── XPlanung/
│   ├── index.md                          # Level 2: XPlanung Übersicht
│   └── [Dokumente].md                    # Level 3: Einzeldokumente (nav_exclude: true)
├── ALKIS/
└── [Weitere Standards]/
```

### Gesetze-Organisation

```
gesetze/
├── index.md                      # Hauptübersicht aller Gesetze
├── WPG/
│   ├── index.md                  # Wärmeplanungsgesetz Übersicht
│   └── wpg-§3-begriffe.md       # AI-Analyse zu §3
├── BauGB/
├── TKG/
└── GEG/
```

## Session Log - Dokumentation der Claude Code Kommunikation

### Zweck

Das Session Log dokumentiert alle Claude Code Sessions zur Nachvollziehbarkeit der Repository-Entwicklung.

### Datei

- **Location**: `SESSION_LOG.md` im Repository-Root
- **Navigation**: Level 1 (nav_order: 10) - direkt aus Hauptnavigation sichtbar
- **Format**: Chronologisch, neueste Sessions oben

### Workflow

1. Session durchführen
2. Nach Abschluss: SESSION_LOG.md öffnen
3. Neuen Session-Eintrag an den Anfang einfügen (neueste oben)
4. Metadaten, Eingaben, Ergebnisse, Entscheidungen dokumentieren
5. Commit mit `docs: Session [NUMMER] dokumentiert - [Kurztitel]`

## Qualitätskriterien

### Für alle .md Dateien (ZWINGEND)

- [ ] Front Matter Block ist vorhanden und vollständig
- [ ] `layout: default` ist gesetzt
- [ ] `title:` ist definiert
- [ ] `parent:` und ggf. `grand_parent:` sind korrekt gesetzt
- [ ] `nav_exclude: true` für alle Ebene 4+ Dokumente
- [ ] URLs sind als klickbare Markdown-Links formatiert (nicht als Plain Text)

### Für Quellendokumente

- [ ] Jede Quelle hat vollständige Metadaten
- [ ] Erfassungsdatum ist dokumentiert (YYYY-MM-DD Format)
- [ ] Original-URL ist als klickbarer Link angegeben (falls online)
- [ ] Relevanz für Wärmewende ist erklärt
- [ ] Verbindungen zu anderen Dokumenten sind notiert

### Für Index-Seiten (Ebene 2-3)

- [ ] `has_children: true` ist gesetzt
- [ ] Manuelle Links zu allen Unterdokumenten sind vorhanden
- [ ] Kurze Beschreibung für jedes verlinkte Dokument
- [ ] Gruppierung nach sinnvollen Kategorien

## Commit-Konventionen

```
feat: Neue Quelle oder Struktur hinzugefügt
docs: Dokumentation aktualisiert
fix: Fehlerkorrektur
refactor: Struktur reorganisiert
```

Beispiel: `feat: KWW-Halle Leitfaden 2024 hinzugefügt`

---

*Dieses Dokument ist ein lebender Entwurf und wird kontinuierlich angepasst.*
