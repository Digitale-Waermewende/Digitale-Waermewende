---
layout: default
title: SVG-Test
nav_order: 4
has_children: false
permalink: /svg-test/
---

# Test: Klickbare SVG-Grafiken

Diese Seite demonstriert die Verwendung von klickbaren SVG-Grafiken in Markdown-Dateien für die Visualisierung der Beziehungen zwischen Standards und Stakeholdern.

## Interaktives Test-Diagramm

Das folgende Diagramm zeigt die wichtigsten Standards für die digitale Wärmewende und ihre koordinierende Organisation. **Klicken Sie auf die farbigen Boxen**, um zu den entsprechenden Bereichen zu navigieren:

<object data="assets/images/test-diagram.svg" type="image/svg+xml" width="800" height="500">
  <p>Ihr Browser unterstützt keine eingebetteten SVG-Grafiken. Bitte verwenden Sie einen modernen Browser wie Chrome, Firefox oder Edge.</p>
</object>

## Erläuterung der Elemente

- **XPlanung** (Grün): Standard für Bauleitplanung und kommunale Wärmepläne
- **XTrasse** (Blau): Standard für Leitungsinfrastruktur und Wärmenetze
- **XBau** (Orange): Standard für Baugenehmigungsverfahren
- **XLeitstelle** (Violett): Koordinierende Organisation (LGV Hamburg)

Die gestrichelten Linien zeigen die organisatorische Zugehörigkeit der Standards zur XLeitstelle.

## Technische Details

Diese SVG-Grafik wurde gemäß der **[Anleitung für klickbare SVG-Grafiken](docs/ANLEITUNG_Klickbare-SVG-Grafiken.md)** erstellt.

### Verwendete Technik

- **Datei**: `assets/images/test-diagram.svg`
- **Einbettung**: `<object>` Tag (empfohlene Methode)
- **Link-Format**: Relative Pfade zu `.html` Dateien (z.B. `../../standards/XPlanung/index.html`)
- **Farben**: Entsprechend den Empfehlungen für Standards-Kategorien

### Test-Hinweise

1. **Klickbarkeit testen**: Klicken Sie auf jede Box, um zu prüfen, ob die Navigation funktioniert
2. **Hover-Effekt**: Bewegen Sie die Maus über die Boxen - sie sollten leicht transparent werden
3. **Tooltip**: Beim Hover sollte ein Tooltip mit zusätzlichen Informationen erscheinen
4. **Browser-Kompatibilität**: Getestet in Chrome, Firefox und Edge

## Anwendungsfälle

Solche interaktiven Diagramme können verwendet werden für:

- **Übersichtsseiten**: Visualisierung der Zusammenhänge auf der Startseite
- **Stakeholder-Landschaft**: Interaktive Karte der beteiligten Organisationen
- **Standard-Übersicht**: Navigation zwischen verwandten Standards
- **Prozess-Diagramme**: Klickbare Workflow-Darstellungen

## Weiterführende Dokumentation

- **Anleitung**: [Klickbare SVG-Grafiken in Markdown](docs/ANLEITUNG_Klickbare-SVG-Grafiken.md)
- **Hauptseite**: [Zurück zur Startseite](index.md)
