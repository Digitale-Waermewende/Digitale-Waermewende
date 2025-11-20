---
layout: default
title: Workflow Deep Research
parent: Dokumentation
nav_order: 2
permalink: /docs/workflow-deep-research/
---

# Workflow: Prompt-basierte Deep Research

## Übersicht

Dieser Workflow beschreibt den standardisierten Prozess für prompt-basierte Deep Research Projekte im Digitale-Waermewende Repository. Der Workflow umfasst Research, Dokumentation, Ablage und Verlinkung.

## Workflow-Schritte

### 1. Research-Auftrag definieren

**Input:**
- Primäre URL zum Research-Thema
- Ziel-Ablageort im Repository
- Kontext/Hintergrund (z.B. Plattform-Einführung)

**Beispiel:**
```
URL: https://gitlab.opencode.de/xleitstelle
Ablageort: standards/XPlanung/
Kontext: OpenCode-Plattform Einführung
```

### 2. Deep Research durchführen

**Vorgehen:**
1. **Hauptseite analysieren**
   - Primäre URL aufrufen und Inhalt erfassen
   - Übersicht über Struktur und Inhalte erstellen

2. **Unterseiten recherchieren**
   - Alle verlinkten Unterseiten lesen
   - Relevante Informationen extrahieren
   - Querverbindungen identifizieren

3. **Besonders relevante Quellen dokumentieren**
   - URLs zu wichtigen Unterseiten mit eigener Beschreibung
   - Externe Referenzen und Primärquellen
   - Technische Dokumentationen

4. **Kontext recherchieren**
   - Hintergrundwissen zur Plattform/Organisation
   - Einordnung in größeren Kontext
   - Relevanz für Digitale Wärmewende

### 3. Markdown-Datei erstellen

#### 3.1 Dateiname

**Format:** `YYYY-MM-DD_DescriptiveName_Research.md`

**Beispiele:**
- `2025-11-19_XLeitstelle-GitLab-OpenCode_Research.md`
- `2025-11-19_ALKIS-Waermeplanung-Integration_Research.md`
- `2025-11-19_WMS-Standards-Kommunal_Research.md`

**Regeln:**
- Datum = Erstellungsdatum (nicht Research-Datum der Quellen)
- DescriptiveName = Aussagekräftig, kebab-case
- Suffix immer `_Research.md`

#### 3.2 Front Matter

**Template:**
```yaml
---
layout: default
title: "[Beschreibender Titel]"
parent: [Parent-Ordner]
grand_parent: [Grand-Parent-Ordner]
nav_exclude: true
permalink: /[pfad]/[dateiname-ohne-datum]/
---
```

**Automatische Ableitung:**
- `parent`: Name des direkten Überordners (z.B. "XPlanung")
- `grand_parent`: Name des Ordners darüber (z.B. "Standards")
- `permalink`: Pfad ohne Datum-Präfix

**Beispiel für `standards/XPlanung/2025-11-19_XLeitstelle-GitLab_Research.md`:**
```yaml
---
layout: default
title: "XLeitstelle GitLab Repository"
parent: XPlanung
grand_parent: Standards
nav_exclude: true
permalink: /standards/xplanung/xleitstelle-gitlab-research/
---
```

#### 3.3 Dokumentstruktur

**Standard-Aufbau:**

```markdown
---
[Front Matter wie oben]
---

# [Titel]

## Kontext und Hintergrund
[Einführung zur Plattform/Organisation/Kontext]

## Übersicht
[Zusammenfassung der Haupterkenntnisse]

## [Thematische Abschnitte]
[Strukturierte Darstellung der Research-Ergebnisse]

### Unterabschnitt 1
[Details...]

### Unterabschnitt 2
[Details...]

## Wichtige Ressourcen

### Primärquellen
- **[Beschreibung]**: [URL](URL)
- **[Beschreibung]**: [URL](URL)

### Weiterführende Links
- **[Beschreibung]**: [URL](URL)

### Technische Dokumentation
- **[Beschreibung]**: [URL](URL)

## Relevanz für Digitale Wärmewende
[Einordnung und Bedeutung]

## Offene Fragen
[Optional: Ungeklärte Punkte für weitere Research]

---
*Recherche durchgeführt am: [Datum]*
*Letzte Aktualisierung: [Datum]*
```

**Wichtig:**
- Alle URLs MÜSSEN klickbar sein: `[URL](URL)` Format
- Strukturierte Überschriften für Navigation
- Klare Abschnitte für verschiedene Informationstypen

### 4. Datei ablegen

**Vorgehen:**
1. Zielordner identifizieren (z.B. `standards/XPlanung/`)
2. Datei mit korrektem Namen erstellen
3. Front Matter Parent/Grand_parent prüfen
4. Permalink validieren

**Ablageorte nach Kategorie:**

| Kategorie | Ablageort | Parent | Grand Parent |
|-----------|-----------|--------|--------------|
| Standard-Research | `standards/[Standard]/` | [Standard] | Standards |
| Organisation-Research | `stakeholder/[Kategorie]/[Organisation]/` | [Organisation] | [Kategorie] |
| Bundesland-Research | `stakeholder/laender/[Bundesland]/` | [Bundesland] | Länder |
| Übergreifende Research | `docs/` | - | - |

### 5. Verlinkung von Index-Datei

**Pflicht: Verlinkung von Parent Index**

Die Research-Datei MUSS von der `index.md` des Parent-Ordners verlinkt werden.

**Beispiel `standards/XPlanung/index.md`:**

```markdown
## Recherchen und Analysen

### GitLab Repositories
- [XLeitstelle GitLab Repository](2025-11-19_XLeitstelle-GitLab_Research.md)

### Implementierungsstudien
- [XPlanung Monitoring Umsetzungsstand](2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md)
```

**Verlinkungsregeln:**
- Relative Pfade verwenden (z.B. `2025-11-19_Dateiname_Research.md`)
- Gruppierung nach Themen wenn mehrere Research-Dateien
- Aussagekräftige Linktexte (ohne Datum)

### 6. Optionale Querverweise

**Wann Querverweise erstellen:**
- Research ist für mehrere Bereiche relevant
- Verbindung zu anderen Standards/Organisationen
- Ergänzende Information zu bestehendem Dokument

**Beispiele für Querverweise:**

**Fall 1: Von anderem Standard verlinken**
```markdown
<!-- In standards/ALKIS/index.md -->
## Verwandte Standards
- [XLeitstelle GitLab](../XPlanung/2025-11-19_XLeitstelle-GitLab_Research.md) -
  OpenCode Plattform für XPlanung-Entwicklung
```

**Fall 2: Von Organisation verlinken**
```markdown
<!-- In stakeholder/bund/XLeitstelle/index.md -->
## Entwicklungsressourcen
- [XLeitstelle GitLab Repository](../../../standards/XPlanung/2025-11-19_XLeitstelle-GitLab_Research.md)
```

**Fall 3: Inline-Verweis in bestehendem Dokument**
```markdown
Die XLeitstelle nutzt GitLab für die Entwicklung
([Details siehe Research](2025-11-19_XLeitstelle-GitLab_Research.md)).
```

## Prompt-Vorlage für Claude Code

### Vorlage für neue Deep Research

```
Ich benötige eine Deep Research zu folgendem Thema:

URL: [Primäre URL]
Ablageort: [Zielordner im Repository]
Kontext: [Hintergrundinformation zur Plattform/Organisation]

Bitte führe folgende Schritte aus:

1. Research durchführen:
   - Hauptseite analysieren
   - Alle verlinkten Unterseiten lesen
   - Besonders relevante Quellen mit eigener URL dokumentieren
   - [Spezifischen Kontext] recherchieren und erklären

2. Markdown-Datei erstellen:
   - Dateiname: YYYY-MM-DD_[DescriptiveName]_Research.md
   - Front Matter mit nav_exclude: true, automatischen Parents
   - Strukturierte Dokumentation gemäß WORKFLOW_Deep-Research.md

3. Datei ablegen in: [Zielordner]

4. Verlinkung erstellen:
   - Von [Parent-Index-Datei]
   - Optional: [Weitere Querverweise falls relevant]

5. Commit und Push mit aussagekräftiger Commit-Message

Bitte verwende den Workflow aus docs/WORKFLOW_Deep-Research.md
```

### Beispiel-Prompt (XLeitstelle GitLab)

```
Ich benötige eine Deep Research zu folgendem Thema:

URL: https://gitlab.opencode.de/xleitstelle
Ablageort: standards/XPlanung/
Kontext: OpenCode-Plattform (was ist das, wer betreibt sie, Bedeutung für Open Source in Deutschland)

Bitte führe folgende Schritte aus:

1. Research durchführen:
   - GitLab-Hauptseite der XLeitstelle analysieren
   - Alle Repositories und Projekte durchsehen
   - Besonders relevante Projekte mit eigener URL dokumentieren
   - OpenCode-Plattform recherchieren und erklären

2. Markdown-Datei erstellen:
   - Dateiname: 2025-11-19_XLeitstelle-GitLab-OpenCode_Research.md
   - Front Matter mit parent: XPlanung, grand_parent: Standards
   - Strukturierte Dokumentation gemäß WORKFLOW_Deep-Research.md

3. Datei ablegen in: standards/XPlanung/

4. Verlinkung erstellen:
   - Von standards/XPlanung/index.md
   - Optional: Von stakeholder/bund/XLeitstelle/index.md

5. Commit und Push

Bitte verwende den Workflow aus docs/WORKFLOW_Deep-Research.md
```

## Qualitätskriterien

### Checkliste vor Commit

- [ ] Dateiname folgt Format `YYYY-MM-DD_DescriptiveName_Research.md`
- [ ] Front Matter vollständig (title, parent, grand_parent, nav_exclude, permalink)
- [ ] Parent/Grand_parent korrekt automatisch abgeleitet
- [ ] Alle URLs sind klickbar (Format `[URL](URL)`)
- [ ] Kontext/Hintergrund erklärt (z.B. Plattform-Einführung)
- [ ] Wichtige Unterseiten mit eigenen URLs dokumentiert
- [ ] Strukturierte Abschnitte mit klaren Überschriften
- [ ] Relevanz für Digitale Wärmewende beschrieben
- [ ] Datei im korrekten Ordner abgelegt
- [ ] Verlinkung von Parent-Index-Datei erstellt
- [ ] Relative Pfade für alle internen Links
- [ ] Optionale Querverweise wo sinnvoll

### Qualitätsmerkmale guter Research

**Vollständigkeit:**
- Alle relevanten Unterseiten erfasst
- Wichtige Querverbindungen identifiziert
- Kontext ausreichend erklärt

**Struktur:**
- Klare thematische Gliederung
- Logischer Aufbau (Überblick → Details)
- Navigationfreundliche Überschriften

**Verlinkung:**
- Wichtige Quellen direkt verlinkt
- Beschreibende Linktexte
- Keine toten Links

**Relevanz:**
- Bezug zur Digitalen Wärmewende hergestellt
- Praktische Anwendbarkeit erklärt
- Einordnung in Repository-Kontext

## Wartung und Updates

### Research-Datei aktualisieren

Wenn sich Quellen ändern oder neue Informationen verfügbar werden:

1. Datei im Editor öffnen
2. Änderungen/Ergänzungen vornehmen
3. "Letzte Aktualisierung" Datum anpassen
4. Commit mit Beschreibung der Änderungen

**Commit-Message Format:**
```
docs: Update [DescriptiveName] Research

- [Was wurde aktualisiert]
- [Neue Informationen]
- [Geänderte Links]
```

### Veraltete Research archivieren

Falls Research nicht mehr relevant:

1. Verlinkungen entfernen (Index-Dateien)
2. Datei optional nach `docs/archive/` verschieben
3. Commit mit Begründung

## Best Practices

### 1. Research-Tiefe
- **Nicht zu oberflächlich**: Alle wichtigen Unterseiten lesen
- **Nicht zu detailliert**: Fokus auf Relevanz für Wärmewende
- **Balance finden**: Tiefe abhängig von Bedeutung des Themas

### 2. URL-Dokumentation
- **Primärquellen bevorzugen**: Offizielle Dokumentation verlinken
- **Stabile URLs**: Permalinks wenn verfügbar
- **Archivierung bedenken**: Wichtige Inhalte zusammenfassen (nicht nur verlinken)

### 3. Kontext-Erklärung
- **Zielgruppe**: Für Domain-Experten mit begrenztem Coding-Wissen
- **Einführung**: Plattformen/Organisationen erklären
- **Akronyme**: Beim ersten Vorkommen ausschreiben

### 4. Verlinkung
- **Von Parent Index**: Immer erforderlich
- **Querverweise**: Nur wenn wirklich relevant
- **Bidirektionale Links**: Wenn möglich beide Richtungen verlinken

## Beispiele

### Beispiel 1: Standard-Research (XLeitstelle GitLab)

**Dateiname:** `standards/XPlanung/2025-11-19_XLeitstelle-GitLab-OpenCode_Research.md`

**Front Matter:**
```yaml
---
layout: default
title: "XLeitstelle GitLab Repository auf OpenCode"
parent: XPlanung
grand_parent: Standards
nav_exclude: true
permalink: /standards/xplanung/xleitstelle-gitlab-opencode-research/
---
```

**Verlinkung:**
- Hauptverlinkung: `standards/XPlanung/index.md`
- Querverweis: `stakeholder/bund/XLeitstelle/index.md`

### Beispiel 2: Organisations-Research

**Dateiname:** `stakeholder/bund/BBSR/2025-11-19_BBSR-Waermeplanung-Datenportal_Research.md`

**Front Matter:**
```yaml
---
layout: default
title: "BBSR Wärmeplanung Datenportal"
parent: BBSR
grand_parent: Bund
nav_exclude: true
permalink: /stakeholder/bund/bbsr/waermeplanung-datenportal-research/
---
```

**Verlinkung:**
- Hauptverlinkung: `stakeholder/bund/BBSR/index.md`
- Querverweis: `standards/XPlanung/index.md` (falls XPlanung-relevant)

### Beispiel 3: Übergreifende Research

**Dateiname:** `docs/2025-11-19_OpenCode-Plattform-Deutschland_Research.md`

**Front Matter:**
```yaml
---
layout: default
title: "OpenCode Plattform Deutschland"
nav_exclude: true
permalink: /docs/opencode-plattform-deutschland-research/
---
```

**Verlinkung:**
- Von verschiedenen relevanten Index-Dateien
- Als Querverweis in verwandten Research-Dokumenten

## Troubleshooting

### Problem: Front Matter Parent nicht korrekt

**Symptom:** Navigation funktioniert nicht wie erwartet

**Lösung:**
1. Prüfe exakte Schreibweise des Parent-Ordners
2. Vergleiche mit `index.md` des Parent-Ordners
3. Stelle sicher, dass Parent-Ordner `has_children: false` oder gar nicht gesetzt hat

### Problem: Links funktionieren nicht

**Symptom:** Klick auf internen Link führt zu 404

**Lösung:**
- Verwende relative Pfade statt Permalinks
- Siehe `docs/2025-11-18_Interne-Links-Korrektur-Analyse.md`
- Siehe `STRUCTURE_GUIDE_Digitale-Waermewende.md` Abschnitt "Interne Verlinkung"

### Problem: URLs nicht klickbar

**Symptom:** URLs werden als Plain Text angezeigt

**Lösung:**
- Format: `[URL](URL)` statt nur `URL`
- Tool: `tools/make_urls_clickable.py` für automatische Konvertierung

## Integration in Repository

Diese Workflow-Datei wird in `CLAUDE.md` referenziert:

```markdown
## Workflows

### Deep Research
- Dokumentation: `docs/WORKFLOW_Deep-Research.md`
- Standardisierter Prozess für prompt-basierte Research-Projekte
- Umfasst Research, Dokumentation, Ablage und Verlinkung
```

---
*Version: 1.0*
*Erstellt: 2025-11-19*
*Letzte Aktualisierung: 2025-11-19*
