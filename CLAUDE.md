# Claude Code Projekt-Instruktionen

## Wichtige Hinweise für Claude Code

### Front-Matter Pflicht (KRITISCH!)

**JEDE .md Datei MUSS mit Front-Matter beginnen!**

**Warum wichtig?**
- Ohne Front-Matter → erscheint fälschlicherweise in Hauptnavigation
- `nav_exclude: true` → verhindert Sidebar-Clutter bei Ebene 4+ Dokumenten
- Jekyll braucht diese Metadaten für korrekte Hierarchie

**Research/Deep-Dive Dokumente** (Ebene 4):
```yaml
---
layout: default
title: "[Kurztitel]"
parent: [Standard/Organisation]
grand_parent: [Standards/Bund/Länder]
nav_exclude: true
permalink: /pfad/zum/dokument/
---
```

**Vor jedem Commit**: Prüfen dass Front-Matter vorhanden ist!

### Detaillierte Dokumentation

Für spezifische Details siehe:
- **[Front-Matter Templates](docs/FRONTMATTER_TEMPLATES.md)** - YAML Front-Matter für alle Navigationsebenen
- **[URL Guidelines](docs/URL_GUIDELINES.md)** - URL-Formatierung und interne Verlinkung
- **[Navigation Rules](docs/NAVIGATION_RULES.md)** - Jekyll Theme, Navigation, Hierarchie
- **[PDF Workflow](docs/PDF_WORKFLOW.md)** - Umgang mit PDF-Dateien und Git LFS
- **[Structure Guide](docs/STRUCTURE_GUIDE_Digitale-Waermewende.md)** - Hauptdokument

### Datum-Format

**WICHTIG**: Bei Dateinamen immer das aktuelle Datum im Format YYYY-MM-DD verwenden.
- Nutze das Datum aus der `<env>` Umgebungsvariable
- Format: 2025-11-21 (nicht 2025-01-21!)
- Verwende "Erfassungsdatum" statt "Datum" in Metadaten zur Klarheit

### Repository-Struktur

Dieses Repository folgt den Regeln aus `STRUCTURE_GUIDE.md`:
- Dateinamen: `YYYY-MM-DD_[Organisation]_[Titel].md`
- Primärquellen werden nach dem Template in STRUCTURE_GUIDE dokumentiert
- Struktur wächst organisch mit den Inhalten

### Git-Konfiguration
- Repository: https://github.com/Digitale-Waermewende/Digitale-Waermewende
- Nutzer: digitale-waermewende
- Branch: master

### Projekt-Fokus
- Digitale Standards für die Wärmewende in Deutschland
- Stakeholder-Analyse (Bund, Länder, Kommunen)
- Datenstandards und Schnittstellen dokumentieren
- Primärquellen sammeln und kommentieren

### Workflows

#### Deep Research
- **Dokumentation**: `docs/WORKFLOW_Deep-Research.md`
- **Zweck**: Standardisierter Prozess für prompt-basierte Research-Projekte
- **Umfang**: Research, Dokumentation, Ablage und Verlinkung
- **Verwendung**: Nutze die Prompt-Vorlagen aus der Workflow-Datei für neue Deep Research Aufträge

## Kontext
Dieses Repository dokumentiert die komplexe Stakeholder-Landschaft der digitalen Wärmewende in Deutschland mit Fokus auf offene Datenstandards für die Wärmeplanung.