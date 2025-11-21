---
layout: default
title: URL Guidelines
parent: Dokumentation
nav_order: 3
permalink: /docs/url-guidelines/
---

# URL Guidelines

## Repository-Philosophie: Schneller Zugang zu Original-Informationen

### Kernzweck

Dieses Repository dient der **Unterstützung von KI-Agenten und Menschen**, Original-Informationen **möglichst schnell** zu finden und darauf zuzugreifen.

## URL-Anforderungen (KRITISCH)

**Alle Markdown-Dokumente MÜSSEN:**

### ✅ Klickbare URLs enthalten

- Jede URL MUSS als Markdown-Link formatiert sein
- NIEMALS Plain-Text-URLs verwenden
- URLs müssen direkt zu Original-Quellen führen

### ✅ Verifizierte URLs

- URLs müssen zum Zeitpunkt der Dokumentation funktionieren
- Bei toten Links: Archiv-URL (Wayback Machine) ergänzen
- URL-Checks bei Updates durchführen

### ✅ Prominente Platzierung

- URLs in Metadaten-Abschnitt am Anfang
- Wichtigste URLs im ersten Bildschirmbereich
- Externe Links zu Original-Ressourcen klar gekennzeichnet

## URL-Formatierung

**Alle URLs MÜSSEN als klickbare Links formatiert sein**:

### ❌ FALSCH (Plain Text)

```markdown
- URL: https://www.example.de/dokument
```

### ✅ RICHTIG (Option 1 - mit Beschreibung)

```markdown
- [Dokumententitel](https://www.example.de/dokument)
```

### ✅ RICHTIG (Option 2 - URL als Link)

```markdown
- <https://www.example.de/dokument>
```

### ✅ RICHTIG (Option 3 - in Metadaten)

```markdown
## Metadaten
- **URLs**:
  - [BBSR Stakeholder-Dialog](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html)
  - [BBSR Wärmeplanung Forschung](https://www.bbsr.bund.de/BBSR/DE/forschung/fachbeitraege/wohnen-immobilien/wohnungswirtschaft/kommunale-waermeplanung/waermeplanung.html)
```

## Empfehlungen nach Kontext

- **In Metadaten**: Option 3 (mit beschreibendem Text)
- **Im Fließtext**: Option 1 (mit Kontext)
- **Für technische Referenzen**: Option 2 (volle URL sichtbar)

## Beispiele

### Beispiel (RICHTIG)

```markdown
## Metadaten
- **Organisation**: BBSR
- **URLs**:
  - [BBSR Stakeholder-Dialog](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html)
  - [BBSR Analysen KOMPAKT](https://www.bbsr.bund.de/BBSR/DE/veroeffentlichungen/analysen-kompakt/2024/ak-07-2024.html)

## Externe Ressourcen
- [BBSR Website](https://www.bbsr.bund.de/)
- [BBSR Forschungsprogramm](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/)
```

### Beispiel (FALSCH)

```markdown
## Metadaten
- URL: https://www.bbsr.bund.de/...  ❌ (nicht klickbar)
- Siehe BBSR Website für Details  ❌ (kein Link)
```

## Warum URLs zentral sind

### Für KI-Agenten

- Direkte Navigation zu Primärquellen
- Automatische Verifikation möglich
- Strukturierte Datenextraktion

### Für Menschen

- Ein Klick zu Original-Informationen
- Keine manuelle URL-Suche nötig
- Zeitersparnis bei Recherche

### Für das Repository

- Nachvollziehbarkeit der Informationen
- Aktualitätsprüfung möglich
- Qualitätssicherung durch Quellenangaben

## Umgang mit Sitemaps und Navigations-Dokumenten

**Besonderheit:** Dokumente, die Website-Strukturen beschreiben (z.B. Sitemaps), MÜSSEN tatsächliche URLs zu den beschriebenen Bereichen enthalten.

### ❌ NICHT

```markdown
### KWP-Prozess
- Vorbereitung der KWP
- Durchführung der KWP
```

### ✅ SONDERN

```markdown
### [KWP-Prozess](https://www.kww-halle.de/kwp-prozess)
- [Vorbereitung der KWP](https://www.kww-halle.de/kwp-prozess/vorbereitung)
- [Durchführung der KWP](https://www.kww-halle.de/kwp-prozess/durchfuehrung)
```

Dies ermöglicht direkten Zugriff auf die Original-Ressourcen ohne manuelle Navigation auf der Ziel-Website.

## Interne Verlinkung zwischen Index-Dateien

**WICHTIG**: Für interne Links zwischen Index-Dateien und Dokumenten MÜSSEN **relative Pfade** verwendet werden, NICHT Permalinks.

### Warum relative Pfade?

**Permalinks funktionieren nur nach Jekyll-Build**:

```markdown
❌ FALSCH: [XPlanung](/standards/xplanung/)
```

- Funktioniert nur auf GitHub Pages nach dem Build
- Funktioniert NICHT im rohen Markdown auf GitHub
- Funktioniert NICHT in lokalen Previews

**Relative Pfade funktionieren überall**:

```markdown
✅ RICHTIG: [XPlanung](../../../standards/XPlanung/index.md)
```

- Funktioniert im rohen Markdown auf GitHub
- Funktioniert nach Jekyll-Build auf GitHub Pages
- Funktioniert in lokalen Editoren und Previews
- Unabhängig von baseurl-Konfiguration

## Pfad-Berechnungs-Regeln

### Von stakeholder/bund/[Organisation]/index.md zu:

**standards/[Standard]/index.md**:

```markdown
[XPlanung](../../../standards/XPlanung/index.md)
```

Pfadlogik: 3x hoch (`../` zu bund, `../` zu stakeholder, `../` zu root), dann runter zu `standards/XPlanung/index.md`

**stakeholder/bund/[AndereOrg]/index.md**:

```markdown
[KWW-Halle](../KWW-Halle/index.md)
```

Pfadlogik: 1x hoch (`../` zu bund), gleiche Ebene, runter zu `KWW-Halle/index.md`

### Von standards/index.md zu:

**standards/[Standard]/index.md**:

```markdown
[XPlanung](XPlanung/index.md)
```

Pfadlogik: Direkt runter zu Unterordner

**stakeholder/bund/[Org]/index.md**:

```markdown
[XLeitstelle](../stakeholder/bund/XLeitstelle/index.md)
```

Pfadlogik: 1x hoch (`../` zu root), dann runter zu `stakeholder/bund/XLeitstelle/index.md`

### Von standards/[Standard]/index.md zu:

**standards/[AndererStandard]/index.md**:

```markdown
[XTrasse](../XTrasse/index.md)
```

Pfadlogik: 1x hoch (`../` zu standards), gleiche Ebene, runter zu `XTrasse/index.md`

**stakeholder/bund/[Org]/index.md**:

```markdown
[XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md)
```

Pfadlogik: 2x hoch (`../` zu standards, `../` zu root), dann runter zu `stakeholder/bund/XLeitstelle/index.md`

## Vollständige Beispiele

### Beispiel 1: XLeitstelle verlinkt auf Standards

Datei: `stakeholder/bund/XLeitstelle/index.md`

```markdown
## Verwaltete Standards
- [XPlanung](../../../standards/XPlanung/index.md)
- [XBau](../../../standards/XBau/index.md)
- [XTrasse](../../../standards/XTrasse/index.md)
```

### Beispiel 2: Standard verlinkt auf Organisation

Datei: `standards/XPlanung/index.md`

```markdown
## Verwaltende Organisation
[XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md)
```

### Beispiel 3: Standard verlinkt auf andere Standards

Datei: `standards/ALKIS/index.md`

```markdown
## Verwandte Standards
- [XPlanung](../XPlanung/index.md)
- [XTrasse](../XTrasse/index.md)
```

### Beispiel 4: Links zu Dokumenten im gleichen Ordner

Datei: `stakeholder/bund/BBSR/index.md`

```markdown
## Dokumente
- [BBSR Wärmeplanung Forschung](2025-09-21_BBSR_Waermeplanung-Forschung.md)
```

Pfadlogik: Gleicher Ordner, kein `../` nötig

## Deep-Link-Format zu Gesetzesparagraphen

### Basis-URL

`https://www.gesetze-im-internet.de/`

### Gesamt-Gesetz

`https://www.gesetze-im-internet.de/[gesetz-id]/`

### Einzelner Paragraph

`https://www.gesetze-im-internet.de/[gesetz-id]/__[nummer].html`

### Beispiele

- WPG: `https://www.gesetze-im-internet.de/wpg/`
- WPG §3: `https://www.gesetze-im-internet.de/wpg/__3.html`
- BauGB: `https://www.gesetze-im-internet.de/bbaug/`
- BauGB §9: `https://www.gesetze-im-internet.de/bbaug/__9.html`

## Verwandte Dokumente

- [Front-Matter Templates](FRONTMATTER_TEMPLATES.md) - Front-Matter-Struktur
- [Navigation Rules](NAVIGATION_RULES.md) - Jekyll Theme und Navigation
- [Structure Guide](STRUCTURE_GUIDE_Digitale-Waermewende.md) - Hauptdokument
