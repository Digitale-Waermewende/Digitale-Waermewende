# Struktur-Leitfaden für das Repository Digitale Wärmewende

## Zweck dieses Dokuments
Dieses Dokument definiert, wie das Repository organisch wachsen soll und nach welchen Regeln Inhalte strukturiert werden.

## Grundprinzipien

1. **Quellenbasiert**: Primäre Quellen stehen im Mittelpunkt
2. **Evolutionär**: Die Struktur wächst mit den Inhalten
3. **Multi-Stakeholder**: Verschiedene Nutzergruppen (AI-Agenten, Entwickler, Domain-Experten)
4. **Nachvollziehbar**: Jede Quelle wird dokumentiert und eingeordnet
5. **URL-First**: Klickbare, verifizierte URLs zu Original-Informationen in allen Dokumenten

## Repository-Philosophie: Schneller Zugang zu Original-Informationen

### Kernzweck
Dieses Repository dient der **Unterstützung von KI-Agenten und Menschen**, Original-Informationen **möglichst schnell** zu finden und darauf zuzugreifen.

### URL-Anforderungen (KRITISCH)

**Alle Markdown-Dokumente MÜSSEN:**

✅ **Klickbare URLs enthalten**
- Jede URL MUSS als Markdown-Link formatiert sein
- NIEMALS Plain-Text-URLs verwenden
- URLs müssen direkt zu Original-Quellen führen

✅ **Verifizierte URLs**
- URLs müssen zum Zeitpunkt der Dokumentation funktionieren
- Bei toten Links: Archiv-URL (Wayback Machine) ergänzen
- URL-Checks bei Updates durchführen

✅ **Prominente Platzierung**
- URLs in Metadaten-Abschnitt am Anfang
- Wichtigste URLs im ersten Bildschirmbereich
- Externe Links zu Original-Ressourcen klar gekennzeichnet

**Beispiel (RICHTIG):**
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

**Beispiel (FALSCH):**
```markdown
## Metadaten
- URL: https://www.bbsr.bund.de/...  ❌ (nicht klickbar)
- Siehe BBSR Website für Details  ❌ (kein Link)
```

### Warum URLs zentral sind

**Für KI-Agenten:**
- Direkte Navigation zu Primärquellen
- Automatische Verifikation möglich
- Strukturierte Datenextraktion

**Für Menschen:**
- Ein Klick zu Original-Informationen
- Keine manuelle URL-Suche nötig
- Zeitersparnis bei Recherche

**Für das Repository:**
- Nachvollziehbarkeit der Informationen
- Aktualitätsprüfung möglich
- Qualitätssicherung durch Quellenangaben

### Umgang mit Sitemaps und Navigations-Dokumenten

**Besonderheit:** Dokumente, die Website-Strukturen beschreiben (z.B. Sitemaps), MÜSSEN tatsächliche URLs zu den beschriebenen Bereichen enthalten.

**NICHT:**
```markdown
### KWP-Prozess
- Vorbereitung der KWP
- Durchführung der KWP
```

**SONDERN:**
```markdown
### [KWP-Prozess](https://www.kww-halle.de/kwp-prozess)
- [Vorbereitung der KWP](https://www.kww-halle.de/kwp-prozess/vorbereitung)
- [Durchführung der KWP](https://www.kww-halle.de/kwp-prozess/durchfuehrung)
```

Dies ermöglicht direkten Zugriff auf die Original-Ressourcen ohne manuelle Navigation auf der Ziel-Website.

## Jekyll Theme und GitHub Pages Konfiguration

### Übersicht
Dieses Repository wird als **GitHub Pages Website** veröffentlicht mit dem **Just the Docs** Theme.

- **Theme**: [Just the Docs](https://just-the-docs.com/)
- **Generator**: Jekyll (automatisch durch GitHub Pages)
- **URL**: https://digitale-waermewende.github.io/Digitale-Waermewende
- **Konfiguration**: `_config.yml` im Repository-Root

### Wichtige Theme-Eigenschaften

**Just the Docs Standardverhalten**:
- Automatische Navigation aus allen `.md` Dateien
- Hierarchische Struktur über Front Matter gesteuert
- **Standard-Limit: 3 Navigationsebenen** (Home → Level 1 → Level 2)
- Sortierung über `nav_order` (niedrigere Zahlen zuerst)

**Anforderungen für dieses Projekt**:
- **Mindestens 4 Navigationsebenen** erforderlich
- **Potentiell 5 Ebenen** für zukünftige Erweiterungen
- Lösung: Verwendung von `nav_exclude` für tiefe Ebenen + manuelle Verlinkung

### Navigations-Hierarchie (4-5 Ebenen)

**Geplante Struktur**:
```
Level 0: Home (index.md)
├─ Level 1: Stakeholder (stakeholder.md)
│  ├─ Level 2: Bund (stakeholder/bund/index.md)
│  │  ├─ Level 3: BBSR (stakeholder/bund/BBSR/index.md)
│  │  │  └─ Level 4: Einzeldokumente (nav_exclude: true)
│  │  └─ Level 3: KWW-Halle (stakeholder/bund/KWW-Halle/index.md)
│  │     └─ Level 4: Einzeldokumente (nav_exclude: true)
│  └─ Level 2: Länder (stakeholder/laender/index.md)
│     ├─ Level 3: Baden-Württemberg (stakeholder/laender/Baden-Wuerttemberg/index.md)
│     │  └─ Level 4: Einzeldokumente (nav_exclude: true)
│     └─ Level 3: Bayern, Brandenburg, etc.
├─ Level 1: Standards (standards.md)
│  ├─ Level 2: XPlanung (standards/XPlanung/index.md)
│  │  └─ Level 3: Einzeldokumente (nav_exclude: true)
│  └─ Level 2: ALKIS, etc.
└─ Level 1: Dokumentation (docs.md)
   └─ Level 2: Einzeldokumente
```

**Strategie für 4+ Ebenen**:
- **Ebenen 0-3**: Erscheinen in der automatischen Navigation (mit Front Matter)
- **Ebenen 4+**: Verwenden `nav_exclude: true` und werden aus der Sidebar-Navigation ausgeblendet
- **Ebene 4-5 Zugriff**: Manuelle Verlinkung von der übergeordneten Ebene-3-Indexseite

**Beispiel**:
- Ebene 3 = `stakeholder/bund/BBSR/index.md` → **IN Navigation sichtbar**
- Ebene 4 = `stakeholder/bund/BBSR/2025-09-21_BBSR_Waermeplanung-Forschung.md` → **NICHT in Navigation**, aber verlinkt auf der BBSR-Indexseite

## Front Matter Anforderungen für alle .md Dateien

### Grundregel
**JEDE** Markdown-Datei MUSS mit einem YAML Front Matter Block beginnen (einzige Ausnahme: README.md Dateien).

### Front Matter Struktur

**Minimale Anforderungen**:
```yaml
---
layout: default
title: "Seitentitel"
---
```

**Vollständiges Front Matter** (abhängig von Navigationsebene):
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

### Templates nach Navigationsebene

#### Level 0: Homepage (index.md)
```yaml
---
layout: default
title: Home
nav_order: 1
description: "Digitale Standards und Stakeholder-Analyse für die deutsche Wärmewende"
permalink: /
---
```

#### Level 1: Hauptbereiche (stakeholder.md, standards.md, docs.md)
```yaml
---
layout: default
title: Stakeholder              # oder "Standards", "Dokumentation"
nav_order: 2                     # 2, 3, 4 für verschiedene Bereiche
has_children: true
permalink: /stakeholder/
---
```

#### Level 2: Unterbereiche mit Kindern (stakeholder/bund/index.md)
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

#### Level 3: Organisation/Thema mit Dokumenten (stakeholder/bund/BBSR/index.md)
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

#### Level 4: Einzeldokumente (stakeholder/bund/BBSR/2025-09-21_BBSR_*.md)
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

#### Level 5: Unter-Dokumente (falls nötig)
```yaml
---
layout: default
title: "Detailanalyse XYZ"
nav_exclude: true                # AUS der Navigation
permalink: /stakeholder/bund/bbsr/waermeplanung-forschung/detail-xyz/
---
```

**Zugriff**: Nur über manuelle Links von Ebene 4 Dokumenten.

### Front Matter Regeln

1. **Exakte String-Übereinstimmung**: `parent: "Bund"` muss EXAKT mit `title: "Bund"` übereinstimmen (inkl. Leerzeichen, Groß-/Kleinschreibung)
2. **Anführungszeichen bei Sonderzeichen**: Wenn Titel `:`, `#`, oder andere YAML-Sonderzeichen enthalten: `title: "BBSR: Analysen"` (mit Anführungszeichen)
3. **Keine Tabs**: Nur Leerzeichen für Einrückung (YAML-Standard)
4. **nav_order Konsistenz**: Innerhalb einer Ebene eindeutige Nummern verwenden
5. **has_children**: Nur setzen bei Seiten, die tatsächlich Unterseiten haben

### Konzept: Organisation vs. Standards

**Wichtige konzeptionelle Trennung** im Repository:

#### Organisationen (unter stakeholder/)
**Zweck**: Dokumentation der Institutionen, die Standards verwalten

**Beispiele**:
- **XLeitstelle** (`stakeholder/bund/XLeitstelle/`)
  - Verwaltet: XPlanung, XBau, XTrasse
  - Fokus: Organisation, Aufgaben, Website-Links
  - Verweis auf: Standards-Bereich

- **AdV** (`stakeholder/bund/AdV/`)
  - Verwaltet: ALKIS
  - Fokus: Arbeitsgemeinschaft, Koordination
  - Verweis auf: ALKIS-Standard

#### Standards (unter standards/)
**Zweck**: Dokumentation der technischen Standards selbst

**Beispiele**:
- **XPlanung** (`standards/XPlanung/`)
  - Technische Spezifikation für Bauleitplanung
  - Fachschema Wärmeplan
  - Verweis auf: XLeitstelle (Organisation)

- **ALKIS** (`standards/ALKIS/`)
  - Amtliches Liegenschaftskatasterinformationssystem
  - Technisches Datenmodell (AAA)
  - Verweis auf: AdV (Organisation)

#### Bidirektionale Verlinkung
Organisationen und Standards verweisen wechselseitig aufeinander:

**Organisation → Standards**:
```markdown
## Verwaltete Standards
- [XPlanung](/standards/xplanung/)
- [XBau](/standards/xbau/)
- [XTrasse](/standards/xtrasse/)
```

**Standard → Organisation**:
```markdown
## Verwaltende Organisation
[XLeitstelle](/stakeholder/bund/xleitstelle/)
```

## Markdown-Datei Formatierungsstandards

### Datei-Aufbau

Jede Content-Markdown-Datei folgt dieser Struktur:

```markdown
---
[Front Matter Block - siehe oben]
---

# [Dokumententitel]

## Metadaten
- **Organisation**: [Herausgeber/Quelle]
- **Erfassungsdatum**: YYYY-MM-DD
- **Typ**: [Gesetz|Leitfaden|Recherche|Analyse|...]
- **URLs**:
  - [Beschreibung Link 1](https://vollständige-url.de)
  - [Beschreibung Link 2](https://andere-url.de)
- **Lokal gespeichert**: [Pfad zur PDF-Datei falls vorhanden]
- **Relevanz**: [Warum ist dieses Dokument wichtig]

## Zusammenfassung
[2-4 Sätze Kernaussage]

## [Weitere Abschnitte nach Bedarf]
...
```

### URL-Formatierung

**Alle URLs MÜSSEN als klickbare Links formatiert sein**:

❌ **FALSCH** (Plain Text):
```markdown
- URL: https://www.example.de/dokument
```

✅ **RICHTIG** (Option 1 - mit Beschreibung):
```markdown
- [Dokumententitel](https://www.example.de/dokument)
```

✅ **RICHTIG** (Option 2 - URL als Link):
```markdown
- <https://www.example.de/dokument>
```

✅ **RICHTIG** (Option 3 - in Metadaten):
```markdown
## Metadaten
- **URLs**:
  - [BBSR Stakeholder-Dialog](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/jahr/2024/stakeholder-dialog-waermeplanung/01-start.html)
  - [BBSR Wärmeplanung Forschung](https://www.bbsr.bund.de/BBSR/DE/forschung/fachbeitraege/wohnen-immobilien/wohnungswirtschaft/kommunale-waermeplanung/waermeplanung.html)
```

**Empfehlung**:
- In Metadaten: Option 3 (mit beschreibendem Text)
- Im Fließtext: Option 1 (mit Kontext)
- Für technische Referenzen: Option 2 (volle URL sichtbar)

### Interne Verlinkung

**Relative Links verwenden**:
```markdown
Siehe auch: [KWW Datenkompass](../KWW-Halle/2025-09-21_KWW-Datenkompass.md)
```

**Oder mit Jekyll-Variablen**:
```markdown
Siehe auch: [KWW Datenkompass]({{ site.baseurl }}/stakeholder/bund/kww-halle/datenkompass/)
```

### Index-Seiten für Ebene 3 (Organisationen/Themen)

Ebene-3-Indexseiten (`BBSR/index.md`, `Baden-Wuerttemberg/index.md`, etc.) dienen als **Inhaltsverzeichnis** für Ebene-4-Dokumente:

```markdown
---
layout: default
title: BBSR
parent: Bund
grand_parent: Stakeholder
nav_order: 1
has_children: true
permalink: /stakeholder/bund/bbsr/
---

# Bundesinstitut für Bau-, Stadt- und Raumforschung (BBSR)

## Über das BBSR
[Kurze Beschreibung der Organisation]

## Dokumente

### Forschung und Analysen
- [BBSR Wärmeplanung Forschung](2025-09-21_BBSR_Waermeplanung-Forschung.md) - Wissenschaftliche Begleitung des Wärmeplanungsgesetzes
- [BBSR Stakeholder-Dialog Ergebnispapier](2025-09-21_BBSR_Stakeholder-Dialog-Ergebnispapier.md) - Dokumentation des bundesweiten Dialogs
- [BBSR Analysen KOMPAKT 07/2024](2025-09-21_BBSR-Analysen-KOMPAKT-07-2024.md) - Status quo der kommunalen Wärmeplanung

## Externe Links
- [BBSR Website](https://www.bbsr.bund.de/)
- [BBSR Forschungsprogramm ExWoSt](https://www.bbsr.bund.de/BBSR/DE/forschung/programme/exwost/exwost-node.html)
```

**Wichtig**:
- Manuelle Links zu allen Ebene-4-Dokumenten
- Gruppierung nach Themen/Kategorien
- Kurze Beschreibung für jedes Dokument

### Automatische Child-Page Navigation (Just the Docs)

Just the Docs zeigt **automatisch** alle Unterseiten (Child Pages) in der Sidebar-Navigation an, wenn `has_children: true` gesetzt ist.

**Wie es funktioniert:**

Wenn eine Seite `has_children: true` hat, dann:
1. **Sidebar**: Alle Unterseiten erscheinen automatisch hierarchisch
2. **Content**: Die Seite selbst kann rein beschreibenden Text enthalten
3. **Updates**: Bei neuen Unterseiten automatische Aktualisierung (kein manuelles Editieren nötig)

**Best Practice für Parent-Seiten (Level 1-2):**

```markdown
---
layout: default
title: Stakeholder
nav_order: 2
has_children: true
permalink: /stakeholder/
---

# Stakeholder

Übersicht der beteiligten Akteure auf allen Verwaltungsebenen.

## Bereiche

Alle Unterbereiche sind in der Navigation auf der linken Seite aufgelistet:
- **Bund** - Nationale Koordination und Standards
- **Länder** - Landesspezifische Implementierungen

Die Navigation wird automatisch von Just the Docs aus den Front Matter-Definitionen der Unterseiten generiert.
```

**Vorteile:**
- ✅ **Keine Redundanz** - Links müssen nicht doppelt gepflegt werden
- ✅ **Automatische Updates** - Neue Unterseiten erscheinen sofort in der Navigation
- ✅ **Kein 404-Risiko** - Keine manuellen Links, die veralten können
- ✅ **Konsistente Navigation** - Immer synchron mit der Sidebar

**Nicht empfohlen:**
- ❌ Manuelle Links zu Unterseiten im Content (parallel zur Sidebar)
- ❌ Verwendung von `{{ site.baseurl }}` Links zu eigenen Child-Pages
- ❌ Duplikation der Navigationsstruktur im Markdown-Content

**Ausnahme: Level 3 Index-Seiten**
Ebene-3-Seiten (wie `BBSR/index.md`) brauchen **manuelle Links** zu Level-4-Dokumenten, weil diese mit `nav_exclude: true` aus der Sidebar ausgeblendet sind.

## Aktuelle Struktur (Minimal)

```
Digitale-Waermewende/
├── docs/                 # Projektdokumentation
├── stakeholder/         
│   ├── bund/            # Bundesebene
│   └── laender/         # Länderebene
└── standards/           # Datenstandards
```

## Regeln für Dokumentenorganisation

### 1. Quellenmanagement in `/stakeholder`

#### Dateinamenskonvention
```
YYYY-MM-DD_[Organisation]_[Titel].md
```
Beispiel: `2024-03-15_KWW-Halle_Leitfaden-Waermeplanung.md`

#### Dokumentstruktur für Quellen

Jede Quellendatei MUSS folgende Struktur haben (mit Front Matter):

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
- ...

## Verbindungen
- Bezug zu: [andere relevante Dokumente]
- Konflikt mit: [falls Widersprüche existieren]

## Originalzitate
> [Wichtige Passagen im Original]

## Notizen
[Eigene Anmerkungen, offene Fragen]
```

**WICHTIG**:
- Front Matter Block ist ZWINGEND erforderlich
- URLs MÜSSEN als klickbare Markdown-Links formatiert sein
- `nav_exclude: true` für alle Ebene-4-Dokumente (werden auf Indexseite verlinkt)

### 2. Bundesländer-Organisation

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
    ├── index.md
    └── [Dokumente].md
```

**Struktur**:
- **Level 2** (`laender/index.md`): Liste aller Bundesländer mit Links
- **Level 3** (`laender/Bayern/index.md`): Übersichtsseite für das Bundesland mit manuellen Links zu Dokumenten
- **Level 4** (einzelne `.md` Dateien): Dokumente mit `nav_exclude: true` (nicht in Sidebar)

**Einschlusskriterium**: Alle Bundesländer mit relevanten Wärmeplanungs-Daten oder -Standards

### 3. Standards-Organisation

```
standards/
├── index.md (als standards.md im Root)   # Level 1: Übersicht aller Standards
├── XPlanung/
│   ├── index.md                          # Level 2: XPlanung Übersicht
│   └── [Dokumente].md                    # Level 3: Einzeldokumente (nav_exclude: true)
├── ALKIS/
│   ├── index.md                          # Level 2: ALKIS Übersicht
│   └── [Dokumente].md                    # Level 3: Einzeldokumente
└── [Weitere Standards]/
    ├── index.md
    └── [Dokumente].md
```

**Struktur**:
- **Level 1** (`standards.md`): Hauptübersicht aller Standards-Bereiche
- **Level 2** (`standards/XPlanung/index.md`): Was ist XPlanung, Relevanz für Wärmeplanung
- **Level 3** (einzelne `.md` Dateien): Detailanalysen mit `nav_exclude: true`

**Alternative für flachere Struktur**:
Falls nur wenige Dokumente pro Standard existieren, können Level 2-Dokumente direkt unter `standards/` liegen ohne Unterordner.

## Wachstumsplan

### Phase 1: Quellensammlung (aktuell)
- [ ] Bundesebene: Gesetze, KWW-Halle, XLeitstelle
- [ ] Standards: XPlanung, INSPIRE dokumentieren
- [ ] Erste Bundesländer mit Wärmekatastern

### Phase 2: Analyse & Vernetzung
- [ ] Verbindungen zwischen Quellen dokumentieren
- [ ] Widersprüche und Lücken identifizieren
- [ ] Stakeholder-Matrix erstellen

### Phase 3: Daten & Tools
- [ ] `/data` - Beispieldaten, Testdaten
- [ ] `/tools` - Konverter, Validatoren
- [ ] API-Dokumentation

### Phase 4: Community
- [ ] Best Practices
- [ ] Case Studies von Kommunen
- [ ] Kontaktverzeichnis

## Commit-Konventionen

```
feat: Neue Quelle oder Struktur hinzugefügt
docs: Dokumentation aktualisiert
fix: Fehlerkorrektur
refactor: Struktur reorganisiert
```

Beispiel: `feat: KWW-Halle Leitfaden 2024 hinzugefügt`

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

## PDF-Dateien Workflow

### Grundsatz
PDF-Dateien von wichtigen Primärquellen werden lokal gespeichert und versioniert, um dauerhafte Verfügbarkeit zu gewährleisten.

### Wichtiger Hinweis zur PDF-Verarbeitung
**Stand 2025-09-21**: Eine direkte Online-Analyse von PDF-Dateien, die auf Webseiten verlinkt sind, ist mit Claude Code nicht möglich. Das WebFetch-Tool kann nur die HTML-Metadaten der verlinkenden Seite auslesen, nicht aber den PDF-Inhalt selbst. Daher ist ein lokaler Download der PDF-Datei zwingend erforderlich, bevor der Inhalt mit dem Read-Tool analysiert werden kann.

### 1. Download von PDFs
```bash
# Mit curl herunterladen (Windows-kompatibel)
curl -L -o "Dateiname.pdf" "https://url-zum-pdf.de/dokument.pdf"

# Alternativ mit vollständigen Parametern
curl -L -o "Dateiname.pdf" "https://url.de/dokument.pdf?__blob=publicationFile&v=3"
```

**Namenskonvention für PDFs:**
- Kurze, beschreibende Namen ohne Datum im Dateinamen
- Beispiele: `BBSR-Analysen-KOMPAKT-07-2024.pdf`, `Stakeholder-Dialog-Waermeplanung.pdf`

### 2. PDF mit Read-Tool lesen
```python
# Nach dem Download kann die PDF lokal gelesen werden
Read("E:/Documents/Coding/Digitale-Waermewende/stakeholder/bund/Dateiname.pdf")
```

### 3. Markdown-Dokumentation erstellen
Für jede wichtige PDF-Datei MUSS eine begleitende Markdown-Datei erstellt werden:

**Dateiname:** `YYYY-MM-DD_[Organisation]_[Titel].md`

**Inhalt muss enthalten:**
```markdown
## Metadaten
- **Lokal gespeichert**: stakeholder/bund/Dateiname.pdf (Dateigröße)
- **URL**: [Original-Download-URL]
- **ISBN/DOI**: [falls vorhanden]
```

### 4. Git Workflow für PDFs

```bash
# Status prüfen
git status

# PDF und Markdown-Dokumentation hinzufügen
git add stakeholder/bund/*.pdf
git add stakeholder/bund/*.md

# Commit mit aussagekräftiger Nachricht
git commit -m "feat: BBSR Analysen KOMPAKT 07/2024 - Status quo Wärmeplanung hinzugefügt

- PDF heruntergeladen (4.7MB)
- Umfassende Dokumentation erstellt
- Kernzahlen: 38% Kommunen aktiv, nur 2% mit fertigen Plänen"

# Push zum Repository
git push origin master
```

### 5. Git LFS für PDF-Dateien

**Status: ✅ AKTIV seit 2025-11-18**

Dieses Repository verwendet **Git LFS** (Large File Storage) für alle PDF-Dateien.

**Was bedeutet das?**
- Alle `*.pdf` Dateien werden automatisch über Git LFS verwaltet
- Die eigentlichen PDF-Dateien werden separat gespeichert
- Im Repository liegt nur ein kleiner "Zeiger" auf die Datei
- Repository bleibt klein und schnell, auch mit vielen/großen PDFs

**Konfiguration:**
- Datei: `.gitattributes` im Repository-Root
- Regel: `*.pdf filter=lfs diff=lfs merge=lfs -text`
- Alle PDFs werden automatisch erkannt und über LFS verwaltet

**Kostenlose Limits (GitHub Free):**
- **1 GB LFS-Speicher** inklusive
- **1 GB Bandbreite** pro Monat inklusive
- Bei Bedarf: 50 GB Datenpaket für ~5 USD/Monat

**Aktueller Stand:**
- 15 PDF-Dateien bereits migriert (~50 MB)
- Platz für mehrere Dutzend weitere PDFs (2-15 MB)

**Wichtig für die tägliche Arbeit:**
- **KEINE Änderungen** im Workflow nötig!
- PDFs werden wie gewohnt mit `git add` und `git commit` hinzugefügt
- Git LFS arbeitet automatisch im Hintergrund
- Push/Pull funktionieren normal (Git LFS lädt PDFs hoch/herunter)

**PDF-Größenlimits:**
- Einzeldatei-Limit: 100 MB (GitHub LFS)
- Sehr große PDFs (>50 MB): Falls möglich, nur als Link referenzieren

**Versionierung:**
- Bei aktualisierten PDFs: Alte Version behalten, neue mit Versionsnummer
- Beispiel: `Leitfaden-v1.pdf` → `Leitfaden-v2.pdf`

**Datenschutz:**
- Keine internen/vertraulichen Dokumente hochladen
- Nur öffentlich verfügbare Quellen

**Prüfen ob LFS aktiv ist:**
```bash
# Liste aller LFS-verwalteten Dateien anzeigen
git lfs ls-files

# LFS-Status prüfen
git lfs status
```

### 6. Beispiel-Workflow

```bash
# 1. PDF herunterladen
curl -L -o "BBSR-Analysen-KOMPAKT-07-2024.pdf" "https://www.bbsr.bund.de/.../ak-07-2024-dl.pdf"

# 2. Mit Read-Tool lesen und analysieren
# 3. Markdown-Dokumentation schreiben (YYYY-MM-DD_BBSR_Analysen-KOMPAKT.md)

# 4. Beide Dateien committen
git add stakeholder/bund/BBSR-Analysen-KOMPAKT-07-2024.pdf
git add stakeholder/bund/2025-09-21_BBSR_Analysen-KOMPAKT.md
git commit -m "feat: BBSR Status quo Analyse zur Wärmeplanung dokumentiert"

# 5. Zum Repository pushen
git push origin master
```

## Offene Fragen zur Diskussion

1. ~~Sollen PDF-Originale auch gespeichert werden oder nur Links?~~ → ✅ JA, wichtige PDFs lokal speichern
2. Wie detailliert sollen Gesetzestexte aufbereitet werden?
3. Brauchen wir eine Versionierung für sich ändernde Dokumente?
4. Soll es Tags/Labels für Themen geben (z.B. #Förderung, #Datenformat)?
5. ~~Soll Git LFS für große PDFs (>50MB) eingerichtet werden?~~ → ✅ JA, Git LFS aktiv seit 2025-11-18 für alle PDFs

---
*Dieses Dokument ist ein lebender Entwurf und wird kontinuierlich angepasst.*