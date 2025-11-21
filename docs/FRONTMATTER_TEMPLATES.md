---
layout: default
title: Front-Matter Templates
parent: Dokumentation
nav_order: 2
permalink: /docs/frontmatter-templates/
---

# Front-Matter Templates

## Grundregel

**JEDE** Markdown-Datei MUSS mit einem YAML Front Matter Block beginnen (einzige Ausnahme: README.md Dateien).

## Front-Matter Struktur

### Minimale Anforderungen

```yaml
---
layout: default
title: "Seitentitel"
---
```

### Vollständiges Front-Matter

Abhängig von Navigationsebene:

```yaml
---
layout: default                # Immer "default" verwenden
title: "Seitentitel"          # Exakter Titel für Navigation (max. 50 Zeichen empfohlen)
parent: "Parent-Titel"        # Muss EXAKT dem title: des Parents entsprechen
grand_parent: "GrandP-Titel"  # Bei 3 Ebenen: Titel der Ebene darüber
nav_order: 1                  # Sortierung (niedrigere Zahlen zuerst)
has_children: true            # Nur bei Ordner-Indexseiten
nav_exclude: true             # Für Ebene 4+ (aus Navigation ausblenden)
permalink: /pfad/             # Optional, meist automatisch
---
```

## Templates nach Navigationsebene

### Level 0: Homepage (index.md)

```yaml
---
layout: default
title: Home
nav_order: 1
description: "Digitale Standards und Stakeholder-Analyse für die deutsche Wärmewende"
permalink: /
---
```

### Level 1: Hauptbereiche (stakeholder.md, standards.md, docs.md)

```yaml
---
layout: default
title: Stakeholder              # oder "Standards", "Dokumentation"
nav_order: 2                     # 2, 3, 4 für verschiedene Bereiche
has_children: true
permalink: /stakeholder/
---
```

### Level 2: Unterbereiche mit Kindern (stakeholder/bund/index.md)

```yaml
---
layout: default
title: Bund
parent: Stakeholder              # Exakt wie in stakeholder.md definiert
nav_order: 1
has_children: true
permalink: /stakeholder/bund/
---
```

### Level 3: Organisation/Thema mit Dokumenten (stakeholder/bund/BBSR/index.md)

```yaml
---
layout: default
title: BBSR
parent: Bund
grand_parent: Stakeholder
nav_order: 1
has_children: true               # Nur wenn manuelle Links zu Dokumenten
permalink: /stakeholder/bund/bbsr/
---
```

### Level 4: Einzeldokumente (stakeholder/bund/BBSR/2025-09-21_BBSR_*.md)

```yaml
---
layout: default
title: "BBSR Wärmeplanung Forschung"
parent: BBSR
grand_parent: Bund
nav_exclude: true                # AUS der Sidebar-Navigation ausblenden
permalink: /stakeholder/bund/bbsr/waermeplanung-forschung/
---
```

**Wichtig**:
- Ebene 4 Dokumente erscheinen NICHT in der Sidebar-Navigation
- Sie werden auf der Ebene-3-Indexseite (`BBSR/index.md`) manuell verlinkt
- Direkter Zugriff über URL ist weiterhin möglich

### Level 4: Research/Deep-Dive Dokumente (standards/XBau/2025-11-21_*.md)

```yaml
---
layout: default
title: "Prozess- und Messaging-Modell"
parent: XBau
grand_parent: Standards
nav_exclude: true
permalink: /standards/xbau/prozess-messaging-modell-research/
---
```

### Level 5: Unter-Dokumente (falls nötig)

```yaml
---
layout: default
title: "Detailanalyse XYZ"
nav_exclude: true                # AUS der Navigation
permalink: /stakeholder/bund/bbsr/waermeplanung-forschung/detail-xyz/
---
```

**Zugriff**: Nur über manuelle Links von Ebene 4 Dokumenten.

## Front-Matter Regeln

1. **Exakte String-Übereinstimmung**: `parent: "Bund"` muss EXAKT mit `title: "Bund"` übereinstimmen (inkl. Leerzeichen, Groß-/Kleinschreibung)
2. **Anführungszeichen bei Sonderzeichen**: Wenn Titel `:`, `#`, oder andere YAML-Sonderzeichen enthalten: `title: "BBSR: Analysen"` (mit Anführungszeichen)
3. **Keine Tabs**: Nur Leerzeichen für Einrückung (YAML-Standard)
4. **nav_order Konsistenz**: Innerhalb einer Ebene eindeutige Nummern verwenden
5. **has_children**: Nur setzen bei Seiten, die tatsächlich Unterseiten haben

## Spezielle Templates

### Gesetzes-Index

```yaml
---
layout: default
title: Wärmeplanungsgesetz
parent: Gesetze
nav_order: 1
has_children: true
permalink: /gesetze/wpg/
---
```

### Paragraphen-Analyse

```yaml
---
layout: default
title: "§3 Begriffsbestimmungen"
parent: Wärmeplanungsgesetz
grand_parent: Gesetze
nav_exclude: true  # Optional bei vielen Paragraphen
permalink: /gesetze/wpg/paragraph-3/
---
```

## Verwandte Dokumente

- [Navigation Rules](NAVIGATION_RULES.md) - Jekyll Theme und Navigations-Hierarchie
- [Structure Guide](STRUCTURE_GUIDE_Digitale-Waermewende.md) - Hauptdokument
