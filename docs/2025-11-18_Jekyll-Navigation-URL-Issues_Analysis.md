# Jekyll Navigation und URL-Probleme - Analyse und To-Do Liste

## Metadaten
- **Erfassungsdatum**: 2025-11-18
- **Typ**: Technische Analyse
- **Status**: Analyse abgeschlossen, Umsetzung ausstehend
- **Betroffenes System**: Jekyll mit Just the Docs Theme auf GitHub Pages

## Zusammenfassung

Die GitHub Pages Website hat drei Hauptprobleme:
1. **Folder-Links führen zu 404-Fehlern** statt Listen von Seiten anzuzeigen
2. **Alle Seiten erscheinen als lange Liste** in der linken Navigation ohne hierarchische Struktur
3. **URLs in Markdown-Dateien sind nicht klickbar** in den generierten HTML-Seiten

Alle drei Probleme haben mit fehlenden oder unvollständigen **Front Matter**-Konfigurationen in den Markdown-Dateien zu tun.

---

## Problem 1: Folder-Links zeigen 404-Fehler

### Symptom
Klickt man in der Navigation auf einen Folder (z.B. "Bund" oder "Länder"), erscheint ein 404-Fehler statt einer Übersichtsseite mit Links zu den Unterseiten.

### Ursache
Die `index.md`-Dateien in den Unterordnern haben **unvollständiges Front Matter**:

**Aktueller Zustand** (z.B. `stakeholder/bund/index.md`):
```yaml
---
layout: page
title: Bund
---
```

**Problem**: Fehlendes Front Matter für Just the Docs Theme:
- Keine `parent`-Angabe → Seite wird nicht als Kind von "Stakeholder" erkannt
- Keine `nav_order`-Angabe → Unklare Sortierung
- Kein `permalink` → Jekyll generiert möglicherweise falschen URL-Pfad

### Lösung
Front Matter ergänzen mit:
```yaml
---
layout: default
title: Bund
parent: Stakeholder
nav_order: 1
permalink: /stakeholder/bund/
---
```

### Betroffene Dateien
- `stakeholder/bund/index.md`
- `stakeholder/laender/index.md`
- Potentiell: alle anderen Unterordner in `stakeholder/`, `standards/`, `docs/`

---

## Problem 2: Alle Seiten in langer Liste ohne Hierarchie

### Symptom
Die linke Navigation zeigt alle Markdown-Seiten aus allen Unterordnern als flache Liste unterhalb der Hauptordner, statt sie hierarchisch zu gruppieren.

### Ursache
**Content-Dateien haben KEIN Front Matter**:

Die meisten Dokumente (z.B. alle BBSR-Dateien, KWW-Dateien, Länder-Analysen) haben **überhaupt kein YAML Front Matter**. Sie starten direkt mit dem Markdown-Titel:

```markdown
# BBSR - Forschung und Stakeholder-Dialog zur kommunalen Wärmeplanung

## Metadaten
...
```

**Ohne Front Matter**:
- Just the Docs kann die Seite nicht korrekt in die Navigation einordnen
- Die Seite wird als Top-Level-Seite behandelt
- Keine parent-child-Beziehung wird erkannt

### Lösung
Jede Content-Datei braucht Front Matter am Anfang:

```yaml
---
layout: default
title: BBSR Wärmeplanung Forschung
parent: BBSR
grand_parent: Bund
nav_order: 1
---
```

**Wichtig**:
- `parent` muss exakt dem `title` der übergeordneten Seite entsprechen
- Bei drei Ebenen (Home → Stakeholder → Bund → BBSR) wird `grand_parent` benötigt
- Für vier Ebenen gibt es Limitierungen in Just the Docs (maximal 3 Ebenen)

### Betroffene Dateien
**Alle Content-Dateien ohne Front Matter**, u.a.:
- `stakeholder/bund/BBSR/*.md` (3 Dateien)
- `stakeholder/bund/KWW-Halle/*.md`
- `stakeholder/bund/XPlanung/*.md`
- `stakeholder/laender/*/*.md` (alle Bundesländer-Analysen, ~30+ Dateien)
- `standards/*.md` (4 Dateien)
- Potentiell weitere

**Geschätzte Anzahl**: ~50-60 Dateien

---

## Problem 3: URLs sind nicht klickbar

### Symptom
URLs, die in den Markdown-Dateien als Text stehen, werden in den generierten HTML-Seiten nicht als klickbare Links dargestellt.

### Ursache
**URLs sind als Plain Text formatiert**, nicht als Markdown-Links:

**Aktuell** (z.B. in BBSR-Datei Zeile 8-9):
```markdown
- **URLs**:
  - https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html
  - https://www.bbsr.bund.de/BBSR/DE/forschung/fachbeitraege/wohnen-immobilien/wohnungswirtschaft/kommunale-waermeplanung/waermeplanung.html
```

**Problem**:
- Markdown rendert Plain-Text-URLs nicht automatisch als anklickbare Links
- GitHub Pages / Jekyll verlangt explizite Link-Syntax

### Lösung
URLs in Markdown-Link-Format umwandeln:

**Option 1 - Mit Beschreibung**:
```markdown
- **URLs**:
  - [Stakeholder-Dialog Wärmeplanung](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html)
  - [Kommunale Wärmeplanung](https://www.bbsr.bund.de/BBSR/DE/forschung/fachbeitraege/wohnen-immobilien/wohnungswirtschaft/kommunale-waermeplanung/waermeplanung.html)
```

**Option 2 - URL selbst als Link**:
```markdown
- **URLs**:
  - <https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html>
  - <https://www.bbsr.bund.de/BBSR/DE/forschung/fachbeitraege/wohnen-immobilien/wohnungswirtschaft/kommunale-waermeplanung/waermeplanung.html>
```

**Empfehlung**: Option 1 für bessere Lesbarkeit, Option 2 für vollständige URL-Sichtbarkeit.

### Betroffene Dateien
Alle Dateien mit URLs in Metadaten oder Fließtext - manuelles Durchsuchen erforderlich oder automatisches Script.

**Bekannte Beispiele**:
- `stakeholder/bund/BBSR/2025-09-21_BBSR_Waermeplanung-Forschung.md`
- `standards/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`
- Wahrscheinlich alle anderen Recherche- und Analyse-Dateien

---

## Zusätzliche Erkenntnisse

### Navigations-Hierarchie Problem
Just the Docs unterstützt **maximal 3 Navigationsebenen**:
1. Ebene: Home
2. Ebene: Stakeholder, Standards, Docs
3. Ebene: Bund, Länder
4. Ebene: ~~BBSR, KWW-Halle~~ ← **NICHT möglich mit Standard-Navigation**

**Aktuelle Struktur erfordert 4 Ebenen**:
```
Home → Stakeholder → Bund → BBSR → einzelne Dokumente
```

**Lösungsoptionen**:
- **A**: Ebene reduzieren (BBSR-Dokumente direkt unter "Bund")
- **B**: Collections verwenden (komplexer)
- **C**: Custom Navigation schreiben (erfordert Liquid Templates)

### README.md vs index.md
In einigen Ordnern existiert `README.md` statt `index.md`:
- `stakeholder/bund/README.md`
- `stakeholder/laender/README.md`
- `standards/README.md`

**Problem**: Just the Docs erkennt `index.md` besser als Ordner-Landing-Page.

**Lösung**: README.md in index.md umbenennen oder zusätzliches index.md erstellen.

---

## To-Do Liste

### Phase 1: Grundstruktur beheben (Priorität: HOCH)

#### 1.1 Index-Seiten für Hauptbereiche korrigieren
- [ ] `stakeholder.md` - Front Matter überprüfen und vervollständigen
- [ ] `standards.md` - Front Matter überprüfen und vervollständigen
- [ ] `docs.md` - Front Matter überprüfen und vervollständigen

#### 1.2 Index-Seiten für Unterordner erstellen/korrigieren
- [ ] `stakeholder/bund/index.md` - Front Matter ergänzen (parent: Stakeholder)
- [ ] `stakeholder/laender/index.md` - Front Matter ergänzen (parent: Stakeholder)
- [ ] Überprüfen ob weitere Unterordner index.md benötigen

#### 1.3 Navigations-Hierarchie entscheiden
- [ ] Entscheidung: Wie soll die Navigation strukturiert sein?
  - Option A: 3 Ebenen (Home → Stakeholder → Bund/BBSR zusammen)
  - Option B: 4 Ebenen mit Collections
  - Option C: Flachere Struktur mit besserer Benennung
- [ ] Dokumentation der gewählten Struktur

### Phase 2: Content-Dateien Front Matter hinzufügen (Priorität: HOCH)

**Vorbereitung**:
- [ ] Liste aller .md-Dateien ohne Front Matter erstellen
- [ ] Mapping-Schema erstellen: Datei → parent → grand_parent

**Stakeholder/Bund**:
- [ ] `stakeholder/bund/BBSR/*.md` (3 Dateien) - Front Matter hinzufügen
- [ ] `stakeholder/bund/KWW-Halle/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/bund/XPlanung/*.md` - Front Matter hinzufügen

**Stakeholder/Länder**:
- [ ] `stakeholder/laender/Baden-Wuerttemberg/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Bayern/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Brandenburg/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Berlin/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Bremen/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Hamburg/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Hessen/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Mecklenburg-Vorpommern/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Niedersachsen/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Nordrhein-Westfalen/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Rheinland-Pfalz/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Saarland/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Sachsen/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Sachsen-Anhalt/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Schleswig-Holstein/*.md` - Front Matter hinzufügen
- [ ] `stakeholder/laender/Thueringen/*.md` - Front Matter hinzufügen

**Standards**:
- [ ] `standards/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md`
- [ ] `standards/2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md`
- [ ] `standards/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`
- [ ] `standards/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md`

### Phase 3: URLs in klickbare Links umwandeln (Priorität: MITTEL)

**Strategie festlegen**:
- [ ] Entscheiden: Option 1 (beschreibende Links) vs. Option 2 (< >-Syntax)
- [ ] Template für URL-Formatierung erstellen

**Automatisierung prüfen**:
- [ ] Prüfen: Können URLs automatisch per Script gefunden werden?
- [ ] Falls ja: Script schreiben für automatische Umwandlung
- [ ] Falls nein: Manuelle Liste erstellen

**Content-Dateien durchgehen**:
- [ ] `stakeholder/bund/` - alle Dateien URLs umwandeln
- [ ] `stakeholder/laender/` - alle Dateien URLs umwandeln
- [ ] `standards/` - alle Dateien URLs umwandeln
- [ ] `docs/` - alle Dateien URLs umwandeln

### Phase 4: Testing und Validierung (Priorität: HOCH)

- [ ] Lokaler Jekyll-Build testen (falls möglich)
- [ ] GitHub Pages Deployment testen
- [ ] Navigation testen: Alle Links funktionieren
- [ ] 404-Fehler prüfen: Keine mehr vorhanden
- [ ] Hierarchie testen: Seiten sind korrekt gruppiert
- [ ] URLs testen: Alle URLs sind klickbar

### Phase 5: Optimierung (Priorität: NIEDRIG)

- [ ] `nav_order` für alle Seiten optimieren (sinnvolle Sortierung)
- [ ] Seiten-Titel vereinheitlichen (konsistente Namenskonvention)
- [ ] Überflüssige Dateien entfernen oder in exclude-Liste aufnehmen
- [ ] Performance prüfen: Ladezeiten der Navigation

---

## Front Matter Templates

### Template für Top-Level Seiten (stakeholder.md, standards.md, docs.md)
```yaml
---
layout: default
title: [Seitenname]
nav_order: [Nummer]
has_children: true
permalink: /[pfad]/
---
```

### Template für 2. Ebene (z.B. stakeholder/bund/index.md)
```yaml
---
layout: default
title: [Unterbereich-Name]
parent: [Parent-Title]
nav_order: [Nummer]
has_children: true
permalink: /[parent-pfad]/[pfad]/
---
```

### Template für 3. Ebene (z.B. stakeholder/bund/BBSR/datei.md)
```yaml
---
layout: default
title: [Dokumenten-Titel]
parent: [2nd-Level-Title]
grand_parent: [1st-Level-Title]
nav_order: [Nummer]
---
```

### Template für 4. Ebene (falls Collections verwendet)
```yaml
---
layout: default
title: [Dokumenten-Titel]
parent: [3rd-Level-Title]
grand_parent: [2nd-Level-Title]
nav_exclude: true  # Alternative: Aus Navigation ausblenden
---
```

---

## Technische Hinweise

### Just the Docs Spezifikationen
- **Max. Navigation Level**: 3 (ohne Collections)
- **Parent-Matching**: Exakte String-Übereinstimmung mit `title:`
- **Sortierung**: Nach `nav_order:` (niedrigere Zahlen zuerst), dann alphabetisch

### Häufige Fehler
1. **Tippfehler in parent**: `parent: "Stakeholder "` (mit Leerzeichen) ≠ `title: "Stakeholder"`
2. **Fehlende Anführungszeichen**: Bei Titeln mit Sonderzeichen immer `title: "Titel: Mit Doppelpunkt"`
3. **Falsche Einrückung**: YAML ist whitespace-sensitiv
4. **Permalink-Konflikte**: Zwei Seiten mit gleichem permalink erzeugen Fehler

### Validierung
```bash
# Lokaler Test (falls Jekyll installiert)
bundle exec jekyll serve

# Front Matter Syntax prüfen
# (YAML-Validator online: https://www.yamllint.com/)
```

---

## Geschätzter Aufwand

| Phase | Aufgabe | Dateien | Aufwand | Priorität |
|-------|---------|---------|---------|-----------|
| 1 | Index-Seiten korrigieren | ~5-10 | 30-60 Min | HOCH |
| 2 | Content Front Matter | ~50-60 | 3-5 Std | HOCH |
| 3 | URLs umwandeln | ~50-60 | 2-4 Std | MITTEL |
| 4 | Testing | - | 1-2 Std | HOCH |
| 5 | Optimierung | ~50-60 | 1-2 Std | NIEDRIG |
| **TOTAL** | | **~50-60** | **7-14 Std** | |

**Automatisierungspotential**:
- Front Matter könnte per Script hinzugefügt werden (Aufwand: 2-3h Entwicklung, spart 2-3h Arbeit)
- URL-Umwandlung könnte per Regex automatisiert werden

---

## Nächste Schritte

1. **Entscheidung treffen**: Navigations-Hierarchie (3 vs. 4 Ebenen)
2. **Prototyp erstellen**: 1-2 Bereiche komplett durcharbeiten (z.B. BBSR)
3. **Testen**: Funktioniert die gewählte Struktur?
4. **Skalieren**: Alle anderen Bereiche nach gleichem Muster

---

## Quellen und Referenzen

- [Just the Docs Documentation](https://just-the-docs.com/)
- [Jekyll Front Matter](https://jekyllrb.com/docs/front-matter/)
- [GitHub Pages + Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
