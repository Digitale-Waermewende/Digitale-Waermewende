---
layout: page
title: Dokumentation
permalink: /docs/
---

# Projektdokumentation

## Über dieses Projekt

Diese Dokumentationsplattform erfasst und analysiert die komplexe Stakeholder-Landschaft der digitalen Wärmewende in Deutschland. Der Fokus liegt auf der Identifikation und Förderung offener Datenstandards für die kommunale Wärmeplanung.

## Projektziele

1. **Transparenz schaffen**: Übersichtliche Darstellung aller relevanten Akteure und ihrer Datenquellen
2. **Best Practices identifizieren**: Erfolgreiche Ansätze aus verschiedenen Bundesländern dokumentieren
3. **Standards fördern**: Offene Datenstandards für die Wärmeplanung vorantreiben
4. **Wissenstransfer ermöglichen**: Erfahrungen zwischen Bundesländern teilen

## Methodik

### Datenerhebung
- Analyse der KWW-Datenkompasse für alle verfügbaren Bundesländer
- Auswertung von Primärquellen (PDFs, Webseiten, offizielle Dokumente)
- Strukturierte Erfassung nach einheitlichem Template

### Dokumentationsstandard
Alle Analysen folgen dem in [STRUCTURE_GUIDE_Digitale-Waermewende](../STRUCTURE_GUIDE_Digitale-Waermewende) definierten Format:
- Einheitliche Metadaten
- Strukturierte Inhaltsabschnitte
- Vergleichbare Bewertungskriterien

## Zentrale Erkenntnisse

### Digitalisierungsgefälle
Erhebliche Unterschiede zwischen Vorreiter-Bundesländern (NRW, Sachsen) und Nachzüglern

### Erfolgreiche Koordinationsmodelle
Zentrale Landesagenturen (ThEGA, KEA-BW, KEAN) bewähren sich als Koordinationsstellen

### Gemeinsame Herausforderungen
- Kehrbuchdaten meist nur auf Anfrage
- Fragmentierte Gasnetzbetreiber-Landschaft
- Unterschiedliche Digitalisierungsgrade bei Bauleitplänen

## Technische Hinweise

### Repository-Struktur
```
/stakeholder/         - Stakeholder-Dokumentation
  /bund/             - Bundesebene
  /laender/          - Länderebene
  /kommunen/         - Kommunale Ebene
/standards/          - Standards und Schnittstellen
/docs/              - Projektdokumentation
```

### Dateinamenskonvention
`YYYY-MM-DD_[Organisation]_[Titel].md`

### GitHub Pages
Diese Dokumentation wird automatisch über GitHub Pages veröffentlicht. Bei jedem Push werden die Änderungen innerhalb von 2-5 Minuten online sichtbar.

## Mitwirkung

Beiträge sind willkommen! Das Projekt ist Open Source unter Apache 2.0 Lizenz.

### Wie Sie beitragen können:
1. Fork des Repositories erstellen
2. Änderungen in eigenem Branch vornehmen
3. Pull Request mit Beschreibung erstellen

### Kontakt
Über das [GitHub Repository](https://github.com/Digitale-Waermewende/Digitale-Waermewende)

## Weiterführende Ressourcen

- [GitHub Pages Setup-Anleitung](./github-pages-setup)
- [KWW Kompetenzzentrum](https://www.kww-halle.de)
- [Wärmeplanungsgesetz (WPG)](https://www.gesetze-im-internet.de/wpg/)

---
[Zurück zur Startseite](../)