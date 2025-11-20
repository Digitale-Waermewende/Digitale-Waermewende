# TODO: XLeitstelle und Standards Umstrukturierung

**Datum**: 2025-11-18
**Status**: ✅ Genehmigt - Bereit zur Implementierung

## Zielsetzung

Klare Trennung zwischen:
- **Stakeholder/Organisationen**: XLeitstelle (Standards XPlanung/XBau/XTrasse) und AdV (Standard ALKIS)
- **Standards** (Level 1): XPlanung, XTrasse, XBau, ALKIS, Datenintegration (die technischen Standards selbst)

## Konzeptionelle Struktur

```
stakeholder/bund/
├── XLeitstelle/               # NEU: Organisation (XPlanung, XBau, XTrasse)
│   └── index.md               # Überblick XLeitstelle + Deep Links zu www.xleitstelle.de
├── AdV/                       # NEU: Organisation (ALKIS)
│   └── index.md               # Arbeitsgemeinschaft der Vermessungsverwaltungen

standards/                     # LEVEL 1
├── XPlanung/                  # ERWEITERT (Level 2)
│   ├── index.md               # NEU
│   ├── 2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md              # VERSCHOBEN
│   ├── 2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md            # VERSCHOBEN
│   └── 2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md          # VERSCHOBEN
├── XTrasse/                   # NEU (Level 2)
│   └── index.md
├── XBau/                      # NEU (Level 2)
│   └── index.md
├── ALKIS/                     # NEU (Level 2)
│   └── index.md               # Keine Dokumente (die gehen nach Datenintegration)
└── Datenintegration/          # NEU (Level 2)
    ├── index.md
    ├── 2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md  # VERSCHOBEN
    └── 2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md # VERSCHOBEN
```

## Implementierungs-Reihenfolge

**Phase 1**: Ordnerstruktur erstellen
**Phase 2**: Dateien verschieben + Front Matter anpassen
**Phase 3**: Index-Dateien mit Inhalt erstellen (inkl. XLeitstelle-Recherche)
**Phase 4**: Aufräumen und STRUCTURE_GUIDE
**Phase 5**: Testing und Commit

---

## Phase 1: Ordnerstruktur erstellen

### 1.1 Stakeholder-Ordner
- [ ] Erstelle `stakeholder/bund/XLeitstelle/` Ordner
- [ ] Erstelle `stakeholder/bund/AdV/` Ordner

### 1.2 Standards-Ordner
- [ ] Erstelle `standards/XPlanung/` Ordner
- [ ] Erstelle `standards/XTrasse/` Ordner
- [ ] Erstelle `standards/XBau/` Ordner
- [ ] Erstelle `standards/ALKIS/` Ordner
- [ ] Erstelle `standards/Datenintegration/` Ordner

### 1.3 Checkpoint
- [ ] Prüfe: Alle 7 Ordner existieren
- [ ] Keine Dateien darin (nur leere Ordner)

---

## Phase 2: Dateien verschieben und Front Matter anpassen

### 2.1 XPlanung - 3 Dateien verschieben

**Datei 1**: `stakeholder/bund/XPlanung/2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md`
- [ ] Verschiebe nach: `standards/XPlanung/2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md`
- [ ] Front Matter aktualisieren (Level 3):
  ```yaml
  ---
  layout: default
  title: "XPlanung Monitoring Umsetzungsstand"
  parent: XPlanung
  grand_parent: Standards
  nav_exclude: true
  ---
  ```

**Datei 2**: `standards/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md`
- [ ] Verschiebe nach: `standards/XPlanung/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md`
- [ ] Front Matter aktualisieren (Level 3):
  ```yaml
  ---
  layout: default
  title: "XPlanung XLeitstelle Wärmeplanung"
  parent: XPlanung
  grand_parent: Standards
  nav_exclude: true
  ---
  ```

**Datei 3**: `standards/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md`
- [ ] Verschiebe nach: `standards/XPlanung/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md`
- [ ] Front Matter aktualisieren (Level 3):
  ```yaml
  ---
  layout: default
  title: "XPlanung Wärmeplan Objektartenkatalog"
  parent: XPlanung
  grand_parent: Standards
  nav_exclude: true
  ---
  ```

### 2.2 Datenintegration - 2 ALKIS-Dateien verschieben

**Datei 4**: `standards/2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md`
- [ ] Verschiebe nach: `standards/Datenintegration/2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md`
- [ ] Front Matter aktualisieren (Level 3):
  ```yaml
  ---
  layout: default
  title: "ALKIS-XPlanung Datenaustausch"
  parent: Datenintegration
  grand_parent: Standards
  nav_exclude: true
  ---
  ```

**Datei 5**: `standards/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`
- [ ] Verschiebe nach: `standards/Datenintegration/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`
- [ ] Front Matter aktualisieren (Level 3):
  ```yaml
  ---
  layout: default
  title: "ALKIS-XPlanung-XTrasse Verhältnis"
  parent: Datenintegration
  grand_parent: Standards
  nav_exclude: true
  ---
  ```

### 2.3 Checkpoint
- [ ] Prüfe: Alle 5 Dateien verschoben
- [ ] Prüfe: Front Matter korrekt aktualisiert
- [ ] Git status prüfen

---

## Phase 3: Index-Dateien erstellen mit Inhalt

### 3.1 XLeitstelle (Organisation) - MIT RECHERCHE

**3.1.1 WebFetch Recherche**
- [ ] WebFetch auf www.xleitstelle.de durchführen
- [ ] Struktur der Website erfassen
- [ ] Relevante Bereiche für Wärmewende identifizieren
- [ ] Deep Links zu allen wichtigen Bereichen sammeln

**3.1.2 Index erstellen**
- [ ] Erstelle `stakeholder/bund/XLeitstelle/index.md`
- [ ] Front Matter (Level 3):
  ```yaml
  ---
  layout: default
  title: XLeitstelle
  parent: Bund
  grand_parent: Stakeholder
  nav_order: 3
  has_children: false
  permalink: /stakeholder/bund/xleitstelle/
  ---
  ```
- [ ] Inhalt:
  - Was ist die XLeitstelle?
  - Aufgaben und Rolle
  - Verwaltete Standards: **[XPlanung](/standards/xplanung/)**, **[XBau](/standards/xbau/)**, **[XTrasse](/standards/xtrasse/)**
  - Deep Links zu xleitstelle.de Bereichen (klickbar!)
  - Relevanz für Wärmewende
  - Externe Links

### 3.2 AdV (Organisation)

- [ ] Erstelle `stakeholder/bund/AdV/index.md`
- [ ] Front Matter (Level 3):
  ```yaml
  ---
  layout: default
  title: AdV
  parent: Bund
  grand_parent: Stakeholder
  nav_order: 4
  has_children: false
  permalink: /stakeholder/bund/adv/
  ---
  ```
- [ ] Inhalt:
  - Was ist die AdV? (Arbeitsgemeinschaft der Vermessungsverwaltungen)
  - Aufgaben und Rolle
  - Verwalteter Standard: **[ALKIS](/standards/alkis/)**
  - **Hinweis**: AdV-Website hat aktuell keine Wärmewende-spezifischen Inhalte
  - **ALKIS-Infos für Wärmeplanung**: [KWW-Konferenz 2024 PDF](../KWW-Halle/KWW-Konferenz_2024_Daten_Jeschke.pdf)
    - Quelle: [KWW-Konferenz 2024](https://www.kww-halle.de/veranstaltungen/kww-konferenz/2024)
  - Externe Links (adv-online.de)

### 3.3 Standards/index.md aktualisieren

- [ ] Prüfe `standards/index.md`
- [ ] Aktualisiere Beschreibung für 5 neue Unterbereiche
- [ ] Sicherstellen: `has_children: true`

### 3.4 XPlanung/index.md

- [ ] Erstelle `standards/XPlanung/index.md`
- [ ] Front Matter (Level 2):
  ```yaml
  ---
  layout: default
  title: XPlanung
  parent: Standards
  nav_order: 1
  has_children: true
  permalink: /standards/xplanung/
  ---
  ```
- [ ] Inhalt:
  - Was ist XPlanung?
  - Technische Spezifikation für Bauleitplanung
  - **Relevanz für Wärmewende**: Integration von Wärmeplan-Objektarten in Bauleitpläne
  - Verweis auf Organisation: **[XLeitstelle](/stakeholder/bund/xleitstelle/)**
  - **Dokumente** in diesem Bereich (Links zu den 3 verschobenen Dateien)

### 3.5 XTrasse/index.md

- [ ] Erstelle `standards/XTrasse/index.md`
- [ ] Front Matter (Level 2):
  ```yaml
  ---
  layout: default
  title: XTrasse
  parent: Standards
  nav_order: 2
  has_children: false
  permalink: /standards/xtrasse/
  ---
  ```
- [ ] Inhalt:
  - Was ist XTrasse?
  - Standard für Leitungsinfrastruktur (Gas, Wasser, Strom, Fernwärme)
  - **Relevanz für Wärmenetze**: Trassenplanung, Leitungsverläufe, Koordination mit anderen Netzen
  - Verweis auf Organisation: **[XLeitstelle](/stakeholder/bund/xleitstelle/)**

### 3.6 XBau/index.md

- [ ] Erstelle `standards/XBau/index.md`
- [ ] Front Matter (Level 2):
  ```yaml
  ---
  layout: default
  title: XBau
  parent: Standards
  nav_order: 3
  has_children: false
  permalink: /standards/xbau/
  ---
  ```
- [ ] Inhalt:
  - Was ist XBau?
  - Standard für Baugenehmigungsverfahren
  - **Relevanz für Wärmewende**: Heizungseinbau, energetische Sanierung, Baugenehmigungen
  - Verweis auf Organisation: **[XLeitstelle](/stakeholder/bund/xleitstelle/)**

### 3.7 ALKIS/index.md

- [ ] Erstelle `standards/ALKIS/index.md`
- [ ] Front Matter (Level 2):
  ```yaml
  ---
  layout: default
  title: ALKIS
  parent: Standards
  nav_order: 4
  has_children: false
  permalink: /standards/alkis/
  ---
  ```
- [ ] Inhalt:
  - Was ist ALKIS? (Amtliches Liegenschaftskatasterinformationssystem)
  - Gebäude- und Grundstücksdaten der Vermessungsverwaltungen
  - **Relevanz für Wärmewende**: Gebäudebestand, Geometrien, Nutzungsarten, Grundlage für Wärmebedarfsermittlung
  - Verweis auf Organisation: **[AdV](/stakeholder/bund/adv/)**
  - **ALKIS-Infos für Wärmeplanung**: [KWW-Konferenz 2024 PDF](../bund/KWW-Halle/KWW-Konferenz_2024_Daten_Jeschke.pdf)
  - **Datenintegration**: Siehe auch [Datenintegration](/standards/datenintegration/)

### 3.8 Datenintegration/index.md

- [ ] Erstelle `standards/Datenintegration/index.md`
- [ ] Front Matter (Level 2):
  ```yaml
  ---
  layout: default
  title: Datenintegration
  parent: Standards
  nav_order: 5
  has_children: true
  permalink: /standards/datenintegration/
  ---
  ```
- [ ] Inhalt:
  - Überblick Datenintegration zwischen Standards
  - **Zusammenspiel**: ALKIS → XPlanung → XTrasse für Wärmeplanung
  - Schnittstellen und Datenaustausch
  - Best Practices für Wärmeplanung
  - Herausforderungen und offene Fragen
  - **Dokumente** in diesem Bereich (Links zu den 2 ALKIS-Dateien)

---

## Phase 4: Aufräumen und Dokumentation

### 4.1 Alte XPlanung-Organisation löschen
- [ ] Prüfe ob `stakeholder/bund/XPlanung/` leer ist (sollte nach Verschiebung leer sein)
- [ ] Lösche `stakeholder/bund/XPlanung/` Ordner
- [ ] Git status prüfen

### 4.2 Navigation prüfen
- [ ] `stakeholder/bund/index.md` prüfen (automatische Navigation sollte XLeitstelle und AdV zeigen)
- [ ] `standards/index.md` prüfen (sollte 5 Standards zeigen)

### 4.3 STRUCTURE_GUIDE aktualisieren
- [ ] Dokumentiere Konzept: Organisation vs. Standards
- [ ] Beispiel für XLeitstelle (Organisation mit Verweisen auf 3 Standards)
- [ ] Beispiel für AdV (Organisation mit Verweis auf 1 Standard)
- [ ] Beispiel für Standards mit Level 2 Unterordnern

### 4.4 Querverweise prüfen
- [ ] Git-Suche: Gibt es andere Dokumente, die auf alte Pfade verweisen?
  - `git grep "stakeholder/bund/XPlanung"`
  - `git grep "standards/2025-09-22_ALKIS"`
- [ ] Falls gefunden: Verweise aktualisieren

---

## Phase 5: Testing und Commit

### 5.1 Lokale Prüfung
- [ ] Alle neuen Index-Dateien haben korrektes Front Matter
- [ ] Alle verschobenen Dateien haben aktualisiertes Front Matter
- [ ] Alle URLs in Index-Dateien sind klickbare Markdown-Links
- [ ] Bidirektionale Verweise funktionieren:
  - XLeitstelle → (XPlanung, XBau, XTrasse)
  - AdV → ALKIS
  - Jeder Standard → zurück zur Organisation
- [ ] Git status prüfen

### 5.2 Commit
- [ ] `git add` alle neuen/verschobenen Dateien
- [ ] `git add` geänderte index.md Dateien
- [ ] `git add` aktualisierter STRUCTURE_GUIDE
- [ ] `git rm` gelöschter XPlanung-Ordner
- [ ] Commit mit ausführlicher Nachricht:
  ```
  Umstrukturierung: Organisation vs. Standards getrennt

  - NEU: XLeitstelle Organisation (XPlanung, XBau, XTrasse)
  - NEU: AdV Organisation (ALKIS)
  - NEU: 5 Standards-Unterbereiche (XPlanung, XTrasse, XBau, ALKIS, Datenintegration)
  - VERSCHOBEN: 3 XPlanung-Dateien → standards/XPlanung/
  - VERSCHOBEN: 2 ALKIS-Dateien → standards/Datenintegration/
  - Front Matter aktualisiert für alle verschobenen Dateien
  - Bidirektionale Verlinkung zwischen Organisationen und Standards
  ```
- [ ] Push zu GitHub

### 5.3 GitHub Pages Test
- [ ] Warte 2-3 Minuten auf Jekyll Build
- [ ] Prüfe Navigation: Stakeholder → Bund → XLeitstelle
- [ ] Prüfe Navigation: Stakeholder → Bund → AdV
- [ ] Prüfe Navigation: Standards → (XPlanung, XTrasse, XBau, ALKIS, Datenintegration)
- [ ] Prüfe: XPlanung zeigt 3 Dokumente
- [ ] Prüfe: Datenintegration zeigt 2 Dokumente
- [ ] Prüfe: Alle Links funktionieren

---

## Zusammenfassung der Verschiebungen

**3 Dateien → standards/XPlanung/**:
1. `stakeholder/bund/XPlanung/2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md`
2. `standards/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md`
3. `standards/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md`

**2 Dateien → standards/Datenintegration/**:
1. `standards/2025-09-22_ALKIS-XPlanung-Datenaustausch-Waermeplanung_Integration.md`
2. `standards/2025-09-22_ALKIS-XPlanung-XTrasse-Verhaeltnis-Waermeplanung_Recherche.md`

**Insgesamt**: 5 Dateien verschoben, 7 neue Index-Dateien erstellt, 1 Ordner gelöscht

---

## Hinweise

- **Reihenfolge einhalten**: Erst Ordner, dann Verschiebungen, dann Index-Dateien
- **XLeitstelle mit WebFetch**: Recherche vor Index-Erstellung
- **Alle URLs klickbar**: Markdown-Link-Format verwenden
- **Bidirektionale Verweise**: Organisation ↔ Standards
- **Front Matter Level 3**: Für alle Dokumente unter Standards/XPlanung/ und Standards/Datenintegration/
- **nav_exclude: true**: Für alle Level 3 Recherche-Dokumente
- **KWW-Konferenz PDF**: Relative Pfade korrekt setzen

---

**Status**: ✅ Genehmigt - Bereit zur Implementierung in der definierten Reihenfolge
