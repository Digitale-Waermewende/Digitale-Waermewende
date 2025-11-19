# Anleitung: Klickbare SVG-Grafiken in Markdown-Dateien

## Übersicht

Diese Anleitung erklärt, wie klickbare SVG-Grafiken in Markdown-Dateien eingebettet werden, die von Jekyll in HTML-Seiten mit funktionierenden Links gerendert werden.

**Anwendungsfall:** Interaktive Visualisierungen der Stakeholder- und Standards-Landschaft mit klickbaren Links zu Detail-Seiten.

## Grundlagen

### Was sind klickbare SVG-Grafiken?

SVG (Scalable Vector Graphics) ist ein XML-basiertes Vektorgrafikformat, das:
- Skalierbar ohne Qualitätsverlust ist
- Text und Formen präzise darstellt
- **Interaktive Elemente** wie Links unterstützt
- In modernen Browsern nativ funktioniert

### Warum SVG für Diagramme verwenden?

**Vorteile gegenüber PNG/JPG:**
- ✅ Skalierbar auf allen Bildschirmgrößen
- ✅ Klickbare Links direkt in der Grafik
- ✅ Scharfe Darstellung auf Retina-Displays
- ✅ Kleine Dateigröße für einfache Diagramme
- ✅ Suchmaschinen können Text indizieren
- ✅ Barrierefrei mit `<title>` und `<desc>` Tags

## Methode 1: SVG als externe Datei mit `<object>` Tag

**Dies ist die empfohlene Methode für klickbare SVG-Grafiken!**

### Schritt 1: SVG-Datei erstellen

Speichere die SVG-Datei z.B. in `assets/images/`:

**Datei:** `assets/images/beispiel-diagramm.svg`

```xml
<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <!-- Hintergrund -->
  <rect width="600" height="400" fill="#f8f9fa"/>

  <!-- Titel -->
  <text x="300" y="30" text-anchor="middle" font-size="24" font-weight="bold">
    Mein Diagramm
  </text>

  <!-- Klickbares Element 1 -->
  <a xlink:href="/Digitale-Waermewende/standards/xplanung/" target="_top">
    <rect x="50" y="100" width="200" height="100" fill="#4CAF50" rx="10"/>
    <text x="150" y="145" text-anchor="middle" fill="white" font-size="18" font-weight="bold">
      XPlanung
    </text>
    <text x="150" y="170" text-anchor="middle" fill="white" font-size="14">
      Raumplanung
    </text>
    <title>Zum XPlanung-Standard</title>
  </a>

  <!-- Klickbares Element 2 -->
  <a xlink:href="/Digitale-Waermewende/standards/xbau/" target="_top">
    <rect x="300" y="100" width="200" height="100" fill="#2196F3" rx="10"/>
    <text x="400" y="145" text-anchor="middle" fill="white" font-size="18" font-weight="bold">
      XBau
    </text>
    <text x="400" y="170" text-anchor="middle" fill="white" font-size="14">
      Baugenehmigung
    </text>
    <title>Zum XBau-Standard</title>
  </a>
</svg>
```

### Schritt 2: In Markdown einbetten

**Datei:** `meine-seite.md`

```markdown
---
layout: default
title: Meine Seite
---

# Beispielseite mit klickbarer SVG-Grafik

Klicken Sie auf die Elemente im Diagramm:

<object data="{{ '/assets/images/beispiel-diagramm.svg' | relative_url }}" type="image/svg+xml" width="600" height="400">
  Ihr Browser unterstützt keine eingebetteten SVG-Grafiken.
</object>
```

**Wichtig:**
- Für die SVG-Einbettung: Jekyll `relative_url` Filter verwenden
- Für Links innerhalb der SVG: Absolute Pfade mit baseurl und `target="_top"`

### Schritt 3: Pfade richtig setzen

**In SVG-Datei (Links):**
```xml
<!-- WICHTIG: Verwende absolute Pfade mit baseurl und target="_top" -->
<!-- Das target="_top" sorgt dafür, dass der Link im Hauptfenster öffnet, nicht im <object> Frame -->
<a xlink:href="/Digitale-Waermewende/standards/xplanung/" target="_top">
<a xlink:href="/Digitale-Waermewende/stakeholder/bund/xleitstelle/" target="_top">
```

**In Markdown (Einbettung):**
```markdown
<!-- Verwende Jekyll's relative_url Filter für die SVG-Einbettung -->
<object data="{{ '/assets/images/diagramm.svg' | relative_url }}" type="image/svg+xml" width="600" height="400">
  Ihr Browser unterstützt keine eingebetteten SVG-Grafiken.
</object>
```

**Warum diese Pfade?**
- **SVG-Links benötigen absolute Pfade** weil sie im `<object>` Kontext ausgeführt werden
- **`target="_top"`** ist essentiell - ohne dies würde die Zielseite im SVG-Frame geladen
- **Jekyll Permalinks verwenden** (lowercase, trailing slash): `/standards/xplanung/` nicht `/standards/XPlanung/index.html`
- **`relative_url` Filter** fügt automatisch den baseurl hinzu: `/Digitale-Waermewende/assets/...`

## Methode 2: Inline SVG direkt im Markdown

**Vorteil:** Keine externe Datei nötig
**Nachteil:** Unübersichtlich bei komplexen Grafiken

```markdown
---
layout: default
title: Inline SVG Beispiel
---

# Seite mit Inline-SVG

<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
  <a href="standards/XPlanung/index.html">
    <rect x="50" y="50" width="150" height="80" fill="#4CAF50" rx="5"/>
    <text x="125" y="95" text-anchor="middle" fill="white" font-size="16">
      XPlanung
    </text>
    <title>Zum XPlanung-Standard</title>
  </a>
</svg>

Weiterer Markdown-Text...
```

**Beachte:** Inline-SVG verwendet `href` (nicht `xlink:href`)!

## Methode 3: SVG via Jekyll Include

### Schritt 1: SVG in `_includes/svg/` speichern

**Datei:** `_includes/svg/standards-uebersicht.svg`

```xml
<svg width="800" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- SVG-Inhalt hier -->
</svg>
```

### Schritt 2: In Markdown einbinden

```markdown
---
layout: default
title: Standards Übersicht
---

# Unsere Standards

{% raw %}{% include svg/standards-uebersicht.svg %}{% endraw %}
```

**Vorteil:** Wiederverwendbar in mehreren Seiten

## Best Practices

### 1. Link-Format

**✅ RICHTIG: Verwende `.html` Endungen für Jekyll-generierte Seiten**
```xml
<a xlink:href="standards/XPlanung/index.html">
<a xlink:href="../stakeholder/bund/XLeitstelle/index.html">
```

**❌ FALSCH: Nicht `.md` Dateien verlinken**
```xml
<!-- Dies funktioniert NICHT: -->
<a xlink:href="standards/XPlanung/index.md">
```

### 2. Accessibility (Barrierefreiheit)

**Immer `<title>` Tags für Tooltips verwenden:**
```xml
<a xlink:href="standards/XPlanung/index.html">
  <rect x="50" y="50" width="150" height="80" fill="#4CAF50"/>
  <text x="125" y="90" text-anchor="middle" fill="white">XPlanung</text>
  <title>Zum XPlanung-Standard navigieren</title>
</a>
```

**Optionale `<desc>` Tags für Beschreibungen:**
```xml
<svg ...>
  <desc>
    Diagramm der Standards-Landschaft mit Links zu XPlanung, XBau, XTrasse und XBreitband
  </desc>
  <!-- Rest des SVG -->
</svg>
```

### 3. Hover-Effekte mit CSS

**Erstelle:** `assets/css/svg-styles.css`

```css
/* Hover-Effekte für klickbare SVG-Elemente */
svg a:hover rect,
svg a:hover circle,
svg a:hover ellipse {
  opacity: 0.8;
  cursor: pointer;
}

svg a:hover text {
  text-decoration: underline;
  cursor: pointer;
}

/* Fokus-Stil für Tastatur-Navigation */
svg a:focus {
  outline: 2px solid #4CAF50;
  outline-offset: 2px;
}

/* Container-Styling */
.svg-container {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background: white;
  margin: 20px 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.svg-container object {
  display: block;
  margin: 0 auto;
}
```

**In Jekyll `_config.yml` oder Layout einbinden:**
```html
<link rel="stylesheet" href="{{ '/assets/css/svg-styles.css' | relative_url }}">
```

**Nutzung im Markdown:**
```markdown
<div class="svg-container">
  <object data="assets/images/diagramm.svg" type="image/svg+xml" width="800" height="600"></object>
</div>
```

### 4. Responsive SVG

**Methode A: Feste Größe mit max-width**
```markdown
<object data="assets/images/diagramm.svg" type="image/svg+xml"
        width="800" height="600" style="max-width: 100%; height: auto;">
</object>
```

**Methode B: Container mit CSS**
```css
.svg-responsive {
  width: 100%;
  max-width: 800px;
  height: auto;
}
```

```markdown
<object data="assets/images/diagramm.svg" type="image/svg+xml" class="svg-responsive"></object>
```

**Methode C: SVG mit viewBox (im SVG selbst)**
```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Inhalt -->
</svg>
```
Dann im Markdown:
```markdown
<object data="assets/images/diagramm.svg" type="image/svg+xml" style="width: 100%; height: auto;"></object>
```

## Farb-Empfehlungen für Standards-Visualisierung

Konsistente Farbgebung für bessere Orientierung:

```xml
<!-- Standards -->
XPlanung:   #4CAF50 (Grün)
XBau:       #FF9800 (Orange)
XTrasse:    #2196F3 (Blau)
XBreitband: #9C27B0 (Lila)
ALKIS:      #795548 (Braun)

<!-- Stakeholder-Ebenen -->
Bund:       #1976D2 (Dunkelblau)
Länder:     #388E3C (Dunkelgrün)
Kommunen:   #F57C00 (Dunkelorange)

<!-- Weitere Elemente -->
Verbindungen:        #666666 (Grau, gestrichelt)
Hintergrund:         #f8f9fa (Hellgrau)
Text auf dunkel:     #ffffff (Weiß)
Text auf hell:       #212121 (Sehr dunkelgrau)
```

## Debugging und Troubleshooting

### Problem: Links funktionieren nicht

**Lösung 1: `<object>` statt `<img>` verwenden**
```markdown
<!-- ❌ Links funktionieren NICHT: -->
![Diagramm](assets/images/diagramm.svg)

<!-- ✅ Links funktionieren: -->
<object data="assets/images/diagramm.svg" type="image/svg+xml"></object>
```

**Lösung 2: Pfade prüfen**
- Öffne die SVG-Datei direkt im Browser
- Prüfe, ob Links dort funktionieren
- Passe Pfade in `xlink:href` entsprechend an

**Lösung 3: Jekyll-Build prüfen**
```bash
cd Digitale-Waermewende
bundle exec jekyll serve
# Öffne http://localhost:4000 und teste
```

### Problem: SVG wird nicht angezeigt

**Lösung 1: MIME-Type prüfen**

Erstelle/Überprüfe `.htaccess` (falls Apache):
```
AddType image/svg+xml svg svgz
```

Oder in Jekyll `_config.yml`:
```yaml
include:
  - assets/images/*.svg
```

**Lösung 2: Fallback hinzufügen**
```markdown
<object data="assets/images/diagramm.svg" type="image/svg+xml" width="800" height="600">
  <img src="assets/images/diagramm-fallback.png" alt="Diagramm" width="800" height="600">
</object>
```

### Problem: Hover-Effekte funktionieren nicht

**Lösung:** CSS muss im **Haupt-HTML** sein, nicht im SVG!

```html
<!-- In _layouts/default.html oder Header -->
<style>
  svg a:hover rect { opacity: 0.8; }
  svg a:hover text { text-decoration: underline; }
</style>
```

**Alternative:** Styles direkt im SVG-`<defs>`:
```xml
<svg ...>
  <defs>
    <style type="text/css">
      <![CDATA[
        a:hover rect { opacity: 0.8; cursor: pointer; }
        a:hover text { text-decoration: underline; }
      ]]>
    </style>
  </defs>
  <!-- Rest des SVG -->
</svg>
```

## Vollständiges Beispiel: Standards-Übersicht

### Datei: `assets/images/standards-uebersicht.svg`

```xml
<svg width="900" height="400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <!-- Internes CSS -->
  <defs>
    <style type="text/css">
      <![CDATA[
        .standard-box {
          transition: opacity 0.3s;
        }
        .standard-box:hover {
          opacity: 0.85;
          cursor: pointer;
        }
        .standard-title {
          font-family: Arial, sans-serif;
          font-weight: bold;
        }
        .standard-subtitle {
          font-family: Arial, sans-serif;
        }
      ]]>
    </style>
  </defs>

  <!-- Hintergrund -->
  <rect width="900" height="400" fill="#f8f9fa"/>

  <!-- Titel -->
  <text x="450" y="40" text-anchor="middle" font-size="28" font-weight="bold" fill="#212121">
    Digitale Standards für die Wärmewende
  </text>

  <!-- XPlanung -->
  <a xlink:href="../standards/XPlanung/index.html">
    <g class="standard-box">
      <rect x="50" y="100" width="180" height="120" fill="#4CAF50" rx="10"/>
      <text x="140" y="150" text-anchor="middle" fill="white" font-size="20" class="standard-title">
        XPlanung
      </text>
      <text x="140" y="180" text-anchor="middle" fill="white" font-size="14" class="standard-subtitle">
        Raumplanung
      </text>
      <title>Zum XPlanung-Standard</title>
    </g>
  </a>

  <!-- XBau -->
  <a xlink:href="../standards/XBau/index.html">
    <g class="standard-box">
      <rect x="260" y="100" width="180" height="120" fill="#FF9800" rx="10"/>
      <text x="350" y="150" text-anchor="middle" fill="white" font-size="20" class="standard-title">
        XBau
      </text>
      <text x="350" y="180" text-anchor="middle" fill="white" font-size="14" class="standard-subtitle">
        Baugenehmigung
      </text>
      <title>Zum XBau-Standard</title>
    </g>
  </a>

  <!-- XTrasse -->
  <a xlink:href="../standards/XTrasse/index.html">
    <g class="standard-box">
      <rect x="470" y="100" width="180" height="120" fill="#2196F3" rx="10"/>
      <text x="560" y="150" text-anchor="middle" fill="white" font-size="20" class="standard-title">
        XTrasse
      </text>
      <text x="560" y="180" text-anchor="middle" fill="white" font-size="14" class="standard-subtitle">
        Leitungsnetze
      </text>
      <title>Zum XTrasse-Standard</title>
    </g>
  </a>

  <!-- XBreitband -->
  <a xlink:href="../standards/XBreitband/index.html">
    <g class="standard-box">
      <rect x="680" y="100" width="180" height="120" fill="#9C27B0" rx="10"/>
      <text x="770" y="150" text-anchor="middle" fill="white" font-size="20" class="standard-title">
        XBreitband
      </text>
      <text x="770" y="180" text-anchor="middle" fill="white" font-size="14" class="standard-subtitle">
        Breitband
      </text>
      <title>Zum XBreitband-Standard</title>
    </g>
  </a>

  <!-- Verwaltende Organisation -->
  <text x="450" y="280" text-anchor="middle" font-size="16" fill="#666">
    Koordiniert von:
  </text>

  <a xlink:href="../stakeholder/bund/XLeitstelle/index.html">
    <g class="standard-box">
      <ellipse cx="450" cy="340" rx="120" ry="40" fill="#1976D2"/>
      <text x="450" y="350" text-anchor="middle" fill="white" font-size="18" font-weight="bold">
        XLeitstelle Hamburg
      </text>
      <title>Zur XLeitstelle Organisation</title>
    </g>
  </a>
</svg>
```

### Datei: `standards/index.md`

```markdown
---
layout: default
title: Standards
has_children: true
nav_order: 2
---

# Digitale Standards

Übersicht der relevanten Standards für die digitale Wärmewende:

<div class="svg-container">
  <object data="../assets/images/standards-uebersicht.svg" type="image/svg+xml"
          width="900" height="400" style="max-width: 100%; height: auto;">
    Ihr Browser unterstützt keine eingebetteten SVG-Grafiken.
  </object>
</div>

## Die Standards im Detail

Klicken Sie auf die Elemente im Diagramm oder nutzen Sie die Links unten:

- [XPlanung](XPlanung/index.md) - Raumplanung und Bauleitplanung
- [XBau](XBau/index.md) - Baugenehmigungsverfahren
- [XTrasse](XTrasse/index.md) - Leitungsnetze und Trassenplanung
- [XBreitband](XBreitband/index.md) - Breitbandausbau (zur Info)
```

## Tools für SVG-Erstellung

### Online-Tools (empfohlen für Anfänger)
- **draw.io / diagrams.net**: Kostenlos, exportiert SVG mit Links
- **Figma**: Professionell, kostenlose Version verfügbar
- **Inkscape**: Open Source Desktop-App

### Code-basiert (empfohlen für Entwickler)
- **D3.js**: JavaScript-Library für datengesteuerte Grafiken
- **Mermaid**: Markdown-basierte Diagramme (Jekyll-Plugin verfügbar)
- **PlantUML**: UML-Diagramme aus Text

### Handgeschrieben (für einfache Diagramme)
Direkt in einem Text-Editor schreiben, wie in den Beispielen gezeigt.

## Checkliste für klickbare SVG-Grafiken

- [ ] SVG-Datei erstellt und in `assets/images/` gespeichert
- [ ] Links verwenden `.html` Endungen (nicht `.md`)
- [ ] Pfade sind relativ zur finalen HTML-Position korrekt
- [ ] `<title>` Tags für Tooltips hinzugefügt
- [ ] `<object>` Tag im Markdown verwendet (nicht `<img>`)
- [ ] `type="image/svg+xml"` Attribut gesetzt
- [ ] Breite/Höhe oder `max-width: 100%` für Responsiveness
- [ ] CSS für Hover-Effekte hinzugefügt (optional)
- [ ] Lokaler Jekyll-Test durchgeführt (`bundle exec jekyll serve`)
- [ ] Links in der eingebetteten SVG getestet
- [ ] Fallback-Text oder Bild bereitgestellt

## Weitere Ressourcen

- **MDN SVG Tutorial**: [https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial)
- **SVG Accessibility**: [https://www.w3.org/WAI/tutorials/images/complex/](https://www.w3.org/WAI/tutorials/images/complex/)
- **Jekyll Assets**: [https://jekyllrb.com/docs/assets/](https://jekyllrb.com/docs/assets/)

---
*Version: 1.0*
*Erstellt: 2025-11-19*
