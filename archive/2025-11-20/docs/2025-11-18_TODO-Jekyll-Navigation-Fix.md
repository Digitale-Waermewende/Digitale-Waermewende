# Detaillierte To-Do Liste: Jekyll Navigation und Front Matter Fix

## Metadaten
- **Erstellt**: 2025-11-18
- **Typ**: Implementierungs-Checkliste
- **Ziel**: 4-5 Ebenen Navigation mit Just the Docs Theme
- **Basis**: STRUCTURE_GUIDE_Digitale-Waermewende.md

## Übersicht

**Gesamtaufgabe**: Front Matter zu allen .md Dateien hinzufügen und Navigationsstruktur aufbauen

**Geschätzte Dateien**: ~60-70 Dateien
**Geschätzte Zeit**: 8-12 Stunden
**Strategie**: Ebene für Ebene von oben nach unten

---

## Phase 1: Basis-Struktur (Level 0-2) ✅ HÖCHSTE PRIORITÄT

### 1.1 Level 0: Homepage
- [ ] `index.md` - Front Matter überprüfen und aktualisieren
  ```yaml
  ---
  layout: default
  title: Home
  nav_order: 1
  description: "Digitale Standards und Stakeholder-Analyse für die deutsche Wärmewende"
  permalink: /
  ---
  ```

### 1.2 Level 1: Hauptbereiche (3 Dateien)

#### 1.2.1 Stakeholder
- [ ] `stakeholder.md` - Front Matter aktualisieren
  ```yaml
  ---
  layout: default
  title: Stakeholder
  nav_order: 2
  has_children: true
  permalink: /stakeholder/
  ---
  ```
- [ ] Inhalt anpassen: Manuelle Links entfernen (werden automatisch generiert)

#### 1.2.2 Standards
- [ ] `standards.md` - Front Matter aktualisieren
  ```yaml
  ---
  layout: default
  title: Standards
  nav_order: 3
  has_children: true
  permalink: /standards/
  ---
  ```
- [ ] Inhalt anpassen: Manuelle Links entfernen

#### 1.2.3 Dokumentation
- [ ] `docs.md` - Front Matter aktualisieren
  ```yaml
  ---
  layout: default
  title: Dokumentation
  nav_order: 4
  has_children: true
  permalink: /docs/
  ---
  ```
- [ ] Inhalt anpassen: Manuelle Links entfernen

### 1.3 Level 2: Unterbereiche mit Index-Seiten (3+ Dateien)

#### 1.3.1 Stakeholder/Bund
- [ ] `stakeholder/bund/index.md` - Erstellen oder aktualisieren
  ```yaml
  ---
  layout: default
  title: Bund
  parent: Stakeholder
  nav_order: 1
  has_children: true
  permalink: /stakeholder/bund/
  ---
  ```
- [ ] Inhalt: Kurze Beschreibung Bundesebene + Übersicht Organisationen

#### 1.3.2 Stakeholder/Länder
- [ ] `stakeholder/laender/index.md` - Aktualisieren
  ```yaml
  ---
  layout: default
  title: Länder
  parent: Stakeholder
  nav_order: 2
  has_children: true
  permalink: /stakeholder/laender/
  ---
  ```
- [ ] Inhalt: Kurze Beschreibung + Übersicht alle Bundesländer

#### 1.3.3 Standards/[Unterordner falls vorhanden]
- [ ] Prüfen: Gibt es Unterordner unter `standards/`?
- [ ] Falls ja: `index.md` für jeden erstellen (XPlanung, ALKIS, etc.)

---

## Phase 2: Level 3 Index-Seiten erstellen ✅ HOHE PRIORITÄT

### 2.1 Stakeholder/Bund Organisationen

**Existierende Unterordner identifizieren**:
- [ ] Liste erstellen: Welche Organisationen haben eigene Ordner?
  - BBSR
  - KWW-Halle
  - XPlanung
  - Weitere?

#### 2.1.1 BBSR
- [ ] `stakeholder/bund/BBSR/index.md` - NEU ERSTELLEN
  ```yaml
  ---
  layout: default
  title: BBSR
  parent: Bund
  grand_parent: Stakeholder
  nav_order: 1
  has_children: true
  permalink: /stakeholder/bund/bbsr/
  ---
  ```
- [ ] Inhalt erstellen:
  - Überschrift: "Bundesinstitut für Bau-, Stadt- und Raumforschung (BBSR)"
  - Kurze Beschreibung der Organisation
  - Abschnitt "Dokumente" mit manuellen Links zu allen .md Dateien im Ordner
  - Externe Links zur BBSR Website

#### 2.1.2 KWW-Halle
- [ ] `stakeholder/bund/KWW-Halle/index.md` - NEU ERSTELLEN
  ```yaml
  ---
  layout: default
  title: KWW-Halle
  parent: Bund
  grand_parent: Stakeholder
  nav_order: 2
  has_children: true
  permalink: /stakeholder/bund/kww-halle/
  ---
  ```
- [ ] Inhalt erstellen: Beschreibung + Links zu Dokumenten

#### 2.1.3 XPlanung (falls Ordner existiert)
- [ ] Prüfen ob `stakeholder/bund/XPlanung/` Ordner existiert
- [ ] Falls ja: `index.md` erstellen analog zu BBSR
  ```yaml
  ---
  layout: default
  title: XPlanung
  parent: Bund
  grand_parent: Stakeholder
  nav_order: 3
  has_children: true
  permalink: /stakeholder/bund/xplanung/
  ---
  ```

#### 2.1.4 Weitere Organisationen
- [ ] Alle anderen Unterordner in `stakeholder/bund/` durchgehen
- [ ] Für jeden Ordner: `index.md` erstellen mit obigem Template

### 2.2 Stakeholder/Länder (16 Bundesländer)

**Für JEDES Bundesland**:

#### Template für Bundesland-Index
```yaml
---
layout: default
title: [Bundesland-Name]
parent: Länder
grand_parent: Stakeholder
nav_order: [1-16]
has_children: true
permalink: /stakeholder/laender/[bundesland]/
---

# [Bundesland-Name]

## Dokumente

### Datenkompass-Analysen
- [KWW Datenkompass [BL]](YYYY-MM-DD_KWW-Datenkompass-[Bundesland]-Analyse.md) - [Kurzbeschreibung]

### XPlanung-Recherchen
- [XPlanung [BL] Deep Research](xplanung_[kuerzel]_deep_research.md) - [Kurzbeschreibung]

## Externe Links
- [Landesregierung](https://...)
```

#### Bundesländer-Liste (alphabetisch mit nav_order)

- [ ] **Baden-Württemberg** - `stakeholder/laender/Baden-Wuerttemberg/index.md` (nav_order: 1)
- [ ] **Bayern** - `stakeholder/laender/Bayern/index.md` (nav_order: 2)
- [ ] **Berlin** - `stakeholder/laender/Berlin/index.md` (nav_order: 3)
- [ ] **Brandenburg** - `stakeholder/laender/Brandenburg/index.md` (nav_order: 4)
- [ ] **Bremen** - `stakeholder/laender/Bremen/index.md` (nav_order: 5)
- [ ] **Hamburg** - `stakeholder/laender/Hamburg/index.md` (nav_order: 6)
- [ ] **Hessen** - `stakeholder/laender/Hessen/index.md` (nav_order: 7)
- [ ] **Mecklenburg-Vorpommern** - `stakeholder/laender/Mecklenburg-Vorpommern/index.md` (nav_order: 8)
- [ ] **Niedersachsen** - `stakeholder/laender/Niedersachsen/index.md` (nav_order: 9)
- [ ] **Nordrhein-Westfalen** - `stakeholder/laender/Nordrhein-Westfalen/index.md` (nav_order: 10)
- [ ] **Rheinland-Pfalz** - `stakeholder/laender/Rheinland-Pfalz/index.md` (nav_order: 11)
- [ ] **Saarland** - `stakeholder/laender/Saarland/index.md` (nav_order: 12)
- [ ] **Sachsen** - `stakeholder/laender/Sachsen/index.md` (nav_order: 13)
- [ ] **Sachsen-Anhalt** - `stakeholder/laender/Sachsen-Anhalt/index.md` (nav_order: 14)
- [ ] **Schleswig-Holstein** - `stakeholder/laender/Schleswig-Holstein/index.md` (nav_order: 15)
- [ ] **Thüringen** - `stakeholder/laender/Thueringen/index.md` (nav_order: 16)

**Hinweis**: Für jedes Bundesland prüfen, welche Dokumente tatsächlich im Ordner liegen!

### 2.3 Standards (falls Unterordner existieren)

- [ ] Prüfen: Gibt es Unterordner unter `standards/`?
- [ ] Falls nein: Diese Phase überspringen
- [ ] Falls ja: Für jeden Unterordner `index.md` erstellen

---

## Phase 3: Level 4 Dokumente - Front Matter hinzufügen ✅ MITTLERE PRIORITÄT

### Strategie
Alle Content-Dokumente (Ebene 4) erhalten Front Matter mit `nav_exclude: true`.

### Template für Level 4 Dokumente
```yaml
---
layout: default
title: "[Kurztitel für Breadcrumb]"
parent: [Organisation/Bundesland]
grand_parent: [Bund/Länder]
nav_exclude: true
---
```

**WICHTIG**:
- `parent` muss exakt dem `title` der Level-3-Indexseite entsprechen
- `grand_parent` muss exakt dem `title` der Level-2-Seite entsprechen
- URLs in Metadaten als Markdown-Links formatieren

---

### 3.1 Stakeholder/Bund/BBSR Dokumente (3 Dateien)

- [ ] `stakeholder/bund/BBSR/2025-09-21_BBSR_Waermeplanung-Forschung.md`
  ```yaml
  ---
  layout: default
  title: "BBSR Wärmeplanung Forschung"
  parent: BBSR
  grand_parent: Bund
  nav_exclude: true
  ---
  ```
  - [ ] URLs in Metadaten als Markdown-Links formatieren (Zeile 8-9)

- [ ] `stakeholder/bund/BBSR/2025-09-21_BBSR_Stakeholder-Dialog-Ergebnispapier.md`
  ```yaml
  ---
  layout: default
  title: "BBSR Stakeholder-Dialog"
  parent: BBSR
  grand_parent: Bund
  nav_exclude: true
  ---
  ```
  - [ ] URLs formatieren

- [ ] `stakeholder/bund/BBSR/2025-09-21_BBSR-Analysen-KOMPAKT-07-2024.md`
  ```yaml
  ---
  layout: default
  title: "BBSR Analysen KOMPAKT 07/2024"
  parent: BBSR
  grand_parent: Bund
  nav_exclude: true
  ---
  ```
  - [ ] URLs formatieren

### 3.2 Stakeholder/Bund/KWW-Halle Dokumente

**Dateien identifizieren**:
- [ ] Liste erstellen: Welche .md Dateien liegen in `stakeholder/bund/KWW-Halle/`?

**Für jede Datei**:
- [ ] Front Matter hinzufügen:
  ```yaml
  ---
  layout: default
  title: "[Kurztitel]"
  parent: KWW-Halle
  grand_parent: Bund
  nav_exclude: true
  ---
  ```
- [ ] URLs als Markdown-Links formatieren

**Bekannte Dateien** (basierend auf vorheriger Analyse):
- [ ] `2025-09-21_KWW-Halle_Sitemap-Kommentiert.md`
- [ ] `2025-09-21_KWW-Datenkompass.md`
- [ ] Weitere prüfen

### 3.3 Stakeholder/Bund/XPlanung Dokumente (falls vorhanden)

- [ ] `stakeholder/bund/XPlanung/2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md`
  ```yaml
  ---
  layout: default
  title: "XPlanung Monitoring Umsetzungsstand"
  parent: XPlanung
  grand_parent: Bund
  nav_exclude: true
  ---
  ```

### 3.4 Stakeholder/Länder - ALLE Bundesländer-Dokumente

**Für JEDES Bundesland** (16 Bundesländer):

#### Dokumenttypen pro Bundesland:
1. KWW-Datenkompass-Analysen: `2025-09-21_KWW-Datenkompass-[BL]-Analyse.md`
2. XPlanung-Recherchen: `xplanung_[kuerzel]_deep_research*.md`
3. Weitere spezifische Dokumente

#### Template für Bundesland-Dokumente
```yaml
---
layout: default
title: "[Dokumenttitel]"
parent: [Bundesland-Name]       # Exakt wie in index.md
grand_parent: Länder
nav_exclude: true
---
```

#### Baden-Württemberg
- [ ] `stakeholder/laender/Baden-Wuerttemberg/2025-09-21_KWW-Datenkompass-Baden-Wuerttemberg-Analyse.md`
  - Front Matter hinzufügen (parent: Baden-Württemberg)
  - URLs formatieren
- [ ] `stakeholder/laender/Baden-Wuerttemberg/xplanung_chat4_bw_full.md`
  - Front Matter hinzufügen
  - URLs formatieren

#### Bayern
- [ ] `stakeholder/laender/Bayern/2025-09-21_KWW-Datenkompass-Bayern-Analyse.md`
- [ ] `stakeholder/laender/Bayern/xplanung_chat4_by_full.md`

#### Berlin
- [ ] `stakeholder/laender/Berlin/xplanung_BE_deep_research.md`
- [ ] Weitere Dokumente prüfen

#### Brandenburg
- [ ] `stakeholder/laender/Brandenburg/2025-09-21_KWW-Datenkompass-Brandenburg-Analyse.md`
- [ ] `stakeholder/laender/Brandenburg/xplanung_chat4_bb_full.md`

#### Bremen
- [ ] `stakeholder/laender/Bremen/xplanung_HB_deep_research.md`
- [ ] Weitere Dokumente prüfen

#### Hamburg
- [ ] `stakeholder/laender/Hamburg/xplanung_HH_deep_research.md`
- [ ] Weitere Dokumente prüfen

#### Hessen
- [ ] `stakeholder/laender/Hessen/2025-09-21_KWW-Datenkompass-Hessen-Analyse.md`
- [ ] `stakeholder/laender/Hessen/xplanung_HE_deep_research_ext.md`

#### Mecklenburg-Vorpommern
- [ ] `stakeholder/laender/Mecklenburg-Vorpommern/2025-09-21_KWW-Datenkompass-Mecklenburg-Vorpommern-Analyse.md`
- [ ] `stakeholder/laender/Mecklenburg-Vorpommern/xplanung_MV_deep_research.md`

#### Niedersachsen
- [ ] `stakeholder/laender/Niedersachsen/2025-09-21_KWW-Datenkompass-Niedersachsen-Analyse.md`
- [ ] `stakeholder/laender/Niedersachsen/xplanung_NI_deep_research.md`

#### Nordrhein-Westfalen
- [ ] `stakeholder/laender/Nordrhein-Westfalen/2025-09-21_KWW-Datenkompass-Nordrhein-Westfalen-Analyse.md`
- [ ] `stakeholder/laender/Nordrhein-Westfalen/xplanung_NW_deep_research_ext.md`

#### Rheinland-Pfalz
- [ ] `stakeholder/laender/Rheinland-Pfalz/2025-09-21_KWW-Datenkompass-Rheinland-Pfalz-Analyse.md`
- [ ] `stakeholder/laender/Rheinland-Pfalz/xplanung_RP_deep_research_ext.md`

#### Saarland
- [ ] `stakeholder/laender/Saarland/2025-09-21_KWW-Datenkompass-Saarland-Analyse.md`
- [ ] `stakeholder/laender/Saarland/xplanung_SL_deep_research_ext.md`

#### Sachsen
- [ ] `stakeholder/laender/Sachsen/2025-09-21_KWW-Datenkompass-Sachsen-Analyse.md`
- [ ] `stakeholder/laender/Sachsen/xplanung_chat4_sn_full.md`

#### Sachsen-Anhalt
- [ ] `stakeholder/laender/Sachsen-Anhalt/2025-09-21_KWW-Datenkompass-Sachsen-Anhalt-Analyse.md`
- [ ] `stakeholder/laender/Sachsen-Anhalt/xplanung_ST_deep_research.md`

#### Schleswig-Holstein
- [ ] `stakeholder/laender/Schleswig-Holstein/2025-09-21_KWW-Datenkompass-Schleswig-Holstein-Analyse.md`
- [ ] `stakeholder/laender/Schleswig-Holstein/xplanung_SH_deep_research.md`

#### Thüringen
- [ ] `stakeholder/laender/Thueringen/2025-09-21_KWW-Datenkompass-Thueringen-Analyse.md`
- [ ] `stakeholder/laender/Thueringen/xplanung_TH_deep_research.md`

### 3.5 Standards Dokumente

**Aktuell direkt unter `standards/`** (keine Unterordner):

- [ ] `standards/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md`
  ```yaml
  ---
  layout: default
  title: "XPlanung-XLeitstelle Waermeplanung"
  parent: Standards
  nav_exclude: true
  ---
  ```

- [ ] `standards/2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md`
  ```yaml
  ---
  layout: default
  title: "ALKIS-XPlanung Datenaustausch"
  parent: Standards
  nav_exclude: true
  ---
  ```

- [ ] `standards/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`
  ```yaml
  ---
  layout: default
  title: "ALKIS-XPlanung-XTrasse Verhältnis"
  parent: Standards
  nav_exclude: true
  ---
  ```

- [ ] `standards/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md`
  ```yaml
  ---
  layout: default
  title: "XPlanung Waermeplan Objektartenkatalog"
  parent: Standards
  nav_exclude: true
  ---
  ```

**Für jedes Dokument**:
- [ ] URLs in Metadaten als Markdown-Links formatieren

### 3.6 Docs Dokumente

- [ ] `docs/github-pages-setup.md`
  ```yaml
  ---
  layout: default
  title: "GitHub Pages Setup"
  parent: Dokumentation
  nav_order: 1
  ---
  ```

- [ ] `docs/2025-11-18_Jekyll-Navigation-URL-Issues_Analysis.md`
  ```yaml
  ---
  layout: default
  title: "Jekyll Navigation Issues Analyse"
  parent: Dokumentation
  nav_order: 2
  ---
  ```

- [ ] Diese Datei (`2025-11-18_TODO-Jekyll-Navigation-Fix.md`)
  ```yaml
  ---
  layout: default
  title: "TODO Jekyll Navigation Fix"
  parent: Dokumentation
  nav_order: 3
  ---
  ```

---

## Phase 4: URL-Formatierung ✅ MITTLERE PRIORITÄT

### Strategie
Alle Plain-Text-URLs in Markdown-Links umwandeln.

### 4.1 Automatische Suche

**Script zum Finden von URLs**:
```bash
# Windows PowerShell
Select-String -Path "*.md" -Pattern "https?://" -Exclude "*index.md" -Recurse
```

**Oder manuell durchgehen**:
- [ ] Alle Dateien aus Phase 3 nochmal überprüfen

### 4.2 Formatierungs-Optionen

**Option 1 - Beschreibender Link** (EMPFOHLEN für Metadaten):
```markdown
- **URLs**:
  - [BBSR Stakeholder-Dialog](https://www.bbsr.bund.de/BBSR/DE/...)
```

**Option 2 - URL als Link** (für technische Referenzen):
```markdown
- <https://www.bbsr.bund.de/BBSR/DE/...>
```

### 4.3 Priorisierung

**HOCH**:
- [ ] Alle URLs in Metadaten-Abschnitten

**MITTEL**:
- [ ] URLs in Fließtext

**NIEDRIG**:
- [ ] URLs in Code-Blöcken oder Beispielen (können Plain-Text bleiben)

---

## Phase 5: Testing und Validierung ✅ KRITISCH

### 5.1 Lokaler Test (optional)

Falls Jekyll lokal installiert ist:
```bash
cd E:\Documents\Coding\Digitale-Waermewende
bundle exec jekyll serve
```

### 5.2 GitHub Pages Deployment

- [ ] Änderungen committen und pushen
- [ ] Warten auf GitHub Pages Build (~2-5 Minuten)
- [ ] Website öffnen: https://digitale-waermewende.github.io/Digitale-Waermewende

### 5.3 Manuelle Tests

**Navigation testen**:
- [ ] Home-Seite lädt
- [ ] Stakeholder → Bund → BBSR Navigation funktioniert
- [ ] Stakeholder → Länder → Baden-Württemberg Navigation funktioniert
- [ ] Standards Navigation funktioniert
- [ ] Dokumentation Navigation funktioniert

**404-Fehler prüfen**:
- [ ] Klick auf "Bund" → KEINE 404, sondern Bund-Übersichtsseite
- [ ] Klick auf "Länder" → KEINE 404, sondern Länder-Übersichtsseite
- [ ] Klick auf "BBSR" → KEINE 404, sondern BBSR-Indexseite
- [ ] Klick auf Bundesland → KEINE 404, sondern Bundesland-Indexseite

**Hierarchie testen**:
- [ ] Ebene 0-3 erscheinen in Sidebar-Navigation
- [ ] Ebene 4 Dokumente erscheinen NICHT in Sidebar
- [ ] Ebene 4 Dokumente sind von Ebene-3-Indexseiten verlinkt
- [ ] Breadcrumbs zeigen korrekte Hierarchie

**URLs testen**:
- [ ] Mindestens 5 verschiedene Dokumente öffnen
- [ ] URLs in Metadaten sind klickbar
- [ ] URLs öffnen korrekte externe Seiten

**Suche testen** (falls aktiviert):
- [ ] Suchfunktion findet Dokumente
- [ ] Suchergebnisse verlinken korrekt

### 5.4 Fehlersuche

**Bei Problemen**:

**Problem: Seite erscheint nicht in Navigation**
→ Prüfen: Front Matter vorhanden? `parent` korrekt geschrieben?

**Problem: 404-Fehler**
→ Prüfen: `permalink` korrekt? Dateiname stimmt mit Link überein?

**Problem: Falsche Hierarchie**
→ Prüfen: `parent` und `grand_parent` exakte String-Übereinstimmung mit `title`?

**Problem: Seite erscheint an falscher Stelle**
→ Prüfen: `nav_order` Nummerierung, `parent` Zuordnung

---

## Phase 6: Optimierung ✅ NIEDRIGE PRIORITÄT

### 6.1 nav_order Optimierung

- [ ] Innerhalb jeder Ebene: Sinnvolle Sortierung festlegen
- [ ] Wichtigste Dokumente/Organisationen niedrige Nummern geben
- [ ] Konsistente Nummerierung (1, 2, 3, ... oder 10, 20, 30, ...)

### 6.2 Titel-Vereinheitlichung

- [ ] Alle `title:` Werte auf Konsistenz prüfen
- [ ] Maximal 50 Zeichen für bessere Lesbarkeit
- [ ] Keine Sonderzeichen (außer mit Anführungszeichen)

### 6.3 Permalink-Optimierung

- [ ] Prüfen: Sind alle Permalinks sprechend und SEO-freundlich?
- [ ] Format: `/stakeholder/bund/bbsr/` (Kleinbuchstaben, keine Umlaute)

### 6.4 Performance

- [ ] Ladezeit der Homepage prüfen
- [ ] Navigation-Rendering-Zeit prüfen
- [ ] Falls langsam: `nav_exclude` für mehr Dokumente erwägen

---

## Automatisierungs-Potenzial

### Script-Ideen

**1. Front Matter Generator**
```python
# Pseudocode
for file in all_md_files:
    if not has_front_matter(file):
        level = detect_level(file)
        parent = detect_parent(file)
        add_front_matter(file, level, parent)
```

**2. URL Converter**
```python
# Pseudocode
for file in all_md_files:
    content = read_file(file)
    content = convert_plain_urls_to_links(content)
    write_file(file, content)
```

**Aufwand für Scripts**:
- Entwicklung: 2-3 Stunden
- Test & Debug: 1-2 Stunden
- **Einsparung**: 3-5 Stunden manuelle Arbeit

**Empfehlung**: Bei >50 Dateien lohnt sich Automatisierung!

---

## Fortschritt-Tracking

### Zusammenfassung

**Phase 1 (Level 0-2)**: ☐ 0/7 Dateien
**Phase 2 (Level 3 Index)**: ☐ 0/~20 Dateien
**Phase 3 (Level 4 Content)**: ☐ 0/~50 Dateien
**Phase 4 (URLs)**: ☐ 0/~50 Dateien
**Phase 5 (Testing)**: ☐ 0/10 Tests
**Phase 6 (Optimierung)**: ☐ Optional

**Gesamt**: ☐ 0/~140+ Aufgaben

### Meilensteine

- [ ] **Meilenstein 1**: Phase 1 abgeschlossen → Basis-Navigation funktioniert
- [ ] **Meilenstein 2**: Phase 2 abgeschlossen → 3-Ebenen-Navigation vollständig
- [ ] **Meilenstein 3**: Phase 3 abgeschlossen → Alle Dokumente haben Front Matter
- [ ] **Meilenstein 4**: Phase 5 abgeschlossen → Website voll funktionsfähig
- [ ] **Meilenstein 5**: Phase 6 abgeschlossen → Optimiert und produktionsreif

---

## Nächste Schritte

### Sofort starten mit:

1. **Phase 1.1**: `index.md` prüfen (5 Min)
2. **Phase 1.2.1**: `stakeholder.md` aktualisieren (10 Min)
3. **Phase 1.3.1**: `stakeholder/bund/index.md` erstellen (15 Min)
4. **Testen**: Git commit + push, GitHub Pages prüfen (10 Min)

→ **Erste 40 Minuten**: Basis-Struktur steht, erste Tests möglich

### Dann fortsetzen mit:

5. **Phase 2.1.1**: BBSR Index erstellen (20 Min)
6. **Phase 3.1**: BBSR Dokumente Front Matter (30 Min)
7. **Testen**: BBSR-Bereich vollständig funktionsfähig

→ **Nach 90 Minuten**: Ein kompletter Bereich (BBSR) als Prototyp fertig

### Pattern wiederholen für:

- KWW-Halle
- Alle 16 Bundesländer
- Standards
- Docs

---

## Support-Ressourcen

- [Just the Docs Documentation](https://just-the-docs.com/docs/navigation-structure/)
- [Jekyll Front Matter Guide](https://jekyllrb.com/docs/front-matter/)
- [GitHub Pages Troubleshooting](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)
- `STRUCTURE_GUIDE_Digitale-Waermewende.md` - Projektspezifische Regeln
