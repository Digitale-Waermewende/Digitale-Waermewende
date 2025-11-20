# Update-Plan für stakeholder/laender

**Datum**: 2025-11-18
**Status**: Geplant - Bereit zur Umsetzung

## Problemanalyse

Der Ordner `stakeholder/laender/` enthält 30 Markdown-Dateien für 16 Bundesländer, die noch nicht an die aktuelle Repository-Struktur angepasst sind.

### Identifizierte Probleme

1. **Fehlende Index-Dateien**: Kein Bundesland hat eine `index.md` Datei
2. **Fehlendes Front Matter**: Die meisten Dokumente haben kein YAML Front Matter
3. **Keine Navigation**: Dokumente erscheinen nicht in der Jekyll/Just the Docs Navigation
4. **Veraltete README.md**: Die README.md entspricht nicht dem Jekyll-Format

## Bestandsaufnahme

### Vorhandene Struktur

```
stakeholder/laender/
├── index.md (✅ hat Front Matter)
├── README.md (❌ veraltet, nicht Jekyll-konform)
├── Baden-Wuerttemberg/
│   ├── 2025-09-21_KWW-Datenkompass-Baden-Wuerttemberg-Analyse.md (❌ kein Front Matter)
│   └── xplanung_chat4_bw_full.md (❌ kein Front Matter)
├── Bayern/
│   ├── 2025-09-21_KWW-Datenkompass-Bayern-Analyse.md (❌ kein Front Matter)
│   └── xplanung_chat4_by_full.md (❌ kein Front Matter)
├── [13 weitere Bundesländer mit ähnlicher Struktur]
└── [3 Bundesländer nur mit XPlanung-Dokumenten: Berlin, Bremen, Hamburg]
```

### Bundesländer mit Dokumenten

**Mit KWW-Datenkompass UND XPlanung (4)**:
- Baden-Württemberg
- Bayern
- Brandenburg
- Sachsen

**Nur mit KWW-Datenkompass (9)**:
- Hessen
- Mecklenburg-Vorpommern
- Niedersachsen
- Nordrhein-Westfalen
- Rheinland-Pfalz
- Saarland
- Sachsen-Anhalt
- Schleswig-Holstein
- Thüringen

**Nur mit XPlanung-Dokumenten (3)**:
- Berlin (xplanung_BE_deep_research.md)
- Bremen (xplanung_HB_deep_research.md)
- Hamburg (xplanung_HH_deep_research.md)

## Update-Plan

### Phase 1: Index-Dateien erstellen (16 Bundesländer)

Für jedes Bundesland eine `index.md` Datei erstellen mit:

**Front Matter Template**:
```yaml
---
layout: default
title: [Bundesland-Name]
parent: Länder
grand_parent: Stakeholder
nav_order: [1-16]
has_children: false  # Wird auf true gesetzt, wenn Ebene-4-Dokumente existieren
permalink: /stakeholder/laender/[bundesland]/
---
```

**Content-Struktur**:
```markdown
# [Bundesland-Name]

Wärmeplanung und digitale Standards in [Bundesland-Name].

## Übersicht

[Kurze Beschreibung der Wärmeplanungs-Aktivitäten im Bundesland]

## Dokumente in diesem Bereich

### KWW-Datenkompass
[falls vorhanden]
- [KWW-Datenkompass [Bundesland]](2025-09-21_KWW-Datenkompass-[Bundesland]-Analyse.md) - Datenbeschaffung für alle 11 WPG-Themengruppen

### XPlanung-Implementierung
[falls vorhanden]
- [XPlanung in [Bundesland]](xplanung_[Kürzel]_...) - Umsetzungsstand und technische Infrastruktur

## Externe Links
[Landesspezifische Websites, Energieagenturen, etc.]
```

### Phase 2: Front Matter zu bestehenden Dokumenten hinzufügen (30 Dateien)

#### Template für KWW-Datenkompass Analysen (13 Dateien)

```yaml
---
layout: default
title: "KWW-Datenkompass [Bundesland]"
parent: [Bundesland-Name]
grand_parent: Länder
nav_exclude: true  # Ebene 4 - nicht in Sidebar
permalink: /stakeholder/laender/[bundesland]/kww-datenkompass/
---
```

#### Template für XPlanung Deep Research Dokumente (17 Dateien)

```yaml
---
layout: default
title: "XPlanung [Bundesland]"
parent: [Bundesland-Name]
grand_parent: Länder
nav_exclude: true  # Ebene 4 - nicht in Sidebar
permalink: /stakeholder/laender/[bundesland]/xplanung/
---
```

### Phase 3: README.md entfernen oder umbenennen

**Option 1 (empfohlen)**: README.md löschen
- Der Inhalt ist veraltet
- Die `index.md` übernimmt diese Funktion

**Option 2**: Als Archiv-Dokument umbenennen
- Umbenennen zu `_archive_old_readme.md`
- `nav_exclude: true` setzen

### Phase 4: index.md aktualisieren

Die Haupt-Index-Datei `stakeholder/laender/index.md` erweitern mit:

```markdown
## Alle Bundesländer

Die Navigation auf der linken Seite zeigt alle dokumentierten Bundesländer. Jedes Bundesland enthält:
- **KWW-Datenkompass**: Bundeslandspezifische Datenbeschaffung für Wärmeplanung
- **XPlanung-Implementierung**: Umsetzungsstand digitaler Standards

### Legende

📊 = KWW-Datenkompass verfügbar
🗺️ = XPlanung-Dokumentation verfügbar
```

## Implementierungsplan

### Schritt 1: Vorbereitung
- [ ] Navigations-Reihenfolge festlegen (alphabetisch oder nach Größe)
- [ ] Bundesland-Kürzel-Mapping erstellen

### Schritt 2: Index-Dateien (16 Dateien)
- [ ] Baden-Württemberg/index.md
- [ ] Bayern/index.md
- [ ] Berlin/index.md
- [ ] Brandenburg/index.md
- [ ] Bremen/index.md
- [ ] Hamburg/index.md
- [ ] Hessen/index.md
- [ ] Mecklenburg-Vorpommern/index.md
- [ ] Niedersachsen/index.md
- [ ] Nordrhein-Westfalen/index.md
- [ ] Rheinland-Pfalz/index.md
- [ ] Saarland/index.md
- [ ] Sachsen/index.md
- [ ] Sachsen-Anhalt/index.md
- [ ] Schleswig-Holstein/index.md
- [ ] Thüringen/index.md

### Schritt 3: Front Matter hinzufügen (30 Dateien)

**KWW-Datenkompass (13 Dateien)**:
- [ ] Baden-Württemberg/2025-09-21_KWW-Datenkompass-Baden-Wuerttemberg-Analyse.md
- [ ] Bayern/2025-09-21_KWW-Datenkompass-Bayern-Analyse.md
- [ ] Brandenburg/2025-09-21_KWW-Datenkompass-Brandenburg-Analyse.md
- [ ] Hessen/2025-09-21_KWW-Datenkompass-Hessen-Analyse.md
- [ ] Mecklenburg-Vorpommern/2025-09-21_KWW-Datenkompass-Mecklenburg-Vorpommern-Analyse.md
- [ ] Niedersachsen/2025-09-21_KWW-Datenkompass-Niedersachsen-Analyse.md
- [ ] Nordrhein-Westfalen/2025-09-21_KWW-Datenkompass-Nordrhein-Westfalen-Analyse.md
- [ ] Rheinland-Pfalz/2025-09-21_KWW-Datenkompass-Rheinland-Pfalz-Analyse.md
- [ ] Saarland/2025-09-21_KWW-Datenkompass-Saarland-Analyse.md
- [ ] Sachsen/2025-09-21_KWW-Datenkompass-Sachsen-Analyse.md
- [ ] Sachsen-Anhalt/2025-09-21_KWW-Datenkompass-Sachsen-Anhalt-Analyse.md
- [ ] Schleswig-Holstein/2025-09-21_KWW-Datenkompass-Schleswig-Holstein-Analyse.md
- [ ] Thüringen/2025-09-21_KWW-Datenkompass-Thueringen-Analyse.md

**XPlanung Dokumente (17 Dateien)**:
- [ ] Baden-Wuerttemberg/xplanung_chat4_bw_full.md
- [ ] Bayern/xplanung_chat4_by_full.md
- [ ] Berlin/xplanung_BE_deep_research.md
- [ ] Brandenburg/xplanung_chat4_bb_full.md
- [ ] Bremen/xplanung_HB_deep_research.md
- [ ] Hamburg/xplanung_HH_deep_research.md
- [ ] Hessen/xplanung_HE_deep_research_ext.md
- [ ] Mecklenburg-Vorpommern/xplanung_MV_deep_research.md
- [ ] Niedersachsen/xplanung_NI_deep_research.md
- [ ] Nordrhein-Westfalen/xplanung_NW_deep_research_ext.md
- [ ] Rheinland-Pfalz/xplanung_RP_deep_research_ext.md
- [ ] Saarland/xplanung_SL_deep_research_ext.md
- [ ] Sachsen/xplanung_chat4_sn_full.md
- [ ] Sachsen-Anhalt/xplanung_ST_deep_research.md
- [ ] Schleswig-Holstein/xplanung_SH_deep_research.md
- [ ] Thueringen/xplanung_TH_deep_research.md

### Schritt 4: Aufräumen
- [ ] README.md entfernen oder archivieren
- [ ] index.md (Haupt-Länder-Index) aktualisieren

### Schritt 5: Qualitätskontrolle
- [ ] Alle Front Matter validieren
- [ ] Navigation lokal testen (Jekyll serve)
- [ ] Links überprüfen

### Schritt 6: Git
- [ ] Alle Änderungen committen
- [ ] Push zum Repository

## Bundesland-Kürzel und nav_order

| nav_order | Bundesland | Kürzel | KWW | XPlanung |
|-----------|-----------|--------|-----|----------|
| 1 | Baden-Württemberg | BW | ✅ | ✅ |
| 2 | Bayern | BY | ✅ | ✅ |
| 3 | Berlin | BE | ❌ | ✅ |
| 4 | Brandenburg | BB | ✅ | ✅ |
| 5 | Bremen | HB | ❌ | ✅ |
| 6 | Hamburg | HH | ❌ | ✅ |
| 7 | Hessen | HE | ✅ | ✅ |
| 8 | Mecklenburg-Vorpommern | MV | ✅ | ✅ |
| 9 | Niedersachsen | NI | ✅ | ✅ |
| 10 | Nordrhein-Westfalen | NW | ✅ | ✅ |
| 11 | Rheinland-Pfalz | RP | ✅ | ✅ |
| 12 | Saarland | SL | ✅ | ✅ |
| 13 | Sachsen | SN | ✅ | ✅ |
| 14 | Sachsen-Anhalt | ST | ✅ | ✅ |
| 15 | Schleswig-Holstein | SH | ✅ | ✅ |
| 16 | Thüringen | TH | ✅ | ✅ |

## Beispiel-Templates

### Beispiel: Baden-Württemberg/index.md

```markdown
---
layout: default
title: Baden-Württemberg
parent: Länder
grand_parent: Stakeholder
nav_order: 1
has_children: false
permalink: /stakeholder/laenden/baden-wuerttemberg/
---

# Baden-Württemberg

Wärmeplanung und digitale Standards in Baden-Württemberg.

## Übersicht

Baden-Württemberg gehört zu den Vorreitern in der kommunalen Wärmeplanung. Das Bundesland verfügt über eine gut ausgebaute Geodateninfrastruktur (GDI-BW) und bietet umfassende Unterstützung für Kommunen bei der Datenbeschaffung.

## Dokumente in diesem Bereich

### KWW-Datenkompass
- [KWW-Datenkompass Baden-Württemberg](2025-09-21_KWW-Datenkompass-Baden-Wuerttemberg-Analyse.md) - Datenbeschaffung für alle 11 WPG-Themengruppen mit BW-spezifischen Quellen

### XPlanung-Implementierung
- [XPlanung in Baden-Württemberg](xplanung_chat4_bw_full.md) - Dezentrale Veröffentlichung über kommunale OGC-Dienste, katalogisiert im GDI-BW

## Landesspezifische Ressourcen

- **Geodateninfrastruktur**: [GDI-BW](https://www.geoportal-bw.de/)
- **Metadatenkatalog**: [GDI-BW Metadaten](https://metadaten.geoportal-bw.de/)
- **Landesvermessung**: [LGL Baden-Württemberg](https://www.lgl-bw.de/)
- **Energieatlas**: [Energieatlas Baden-Württemberg](https://www.energieatlas-bw.de/)

## Besonderheiten

- Starke Koordination durch GDI-BW
- Leitfaden für Bauleitpläne verfügbar
- Mehrere Städte (Karlsruhe, Freiburg, Mannheim) mit robusten XPlanung-Services
- ALKIS-Daten über LGL-BW verfügbar
```

### Beispiel: Front Matter für KWW-Datenkompass

Datei: `Baden-Wuerttemberg/2025-09-21_KWW-Datenkompass-Baden-Wuerttemberg-Analyse.md`

```yaml
---
layout: default
title: "KWW-Datenkompass Baden-Württemberg"
parent: Baden-Württemberg
grand_parent: Länder
nav_exclude: true
permalink: /stakeholder/laender/baden-wuerttemberg/kww-datenkompass/
---
```

Dann folgt der bestehende Inhalt (bleibt unverändert):
```markdown
# KWW-Datenkompass Baden-Württemberg - Detailanalyse

## Metadaten
...
```

## Zeitaufwand-Schätzung

- **Index-Dateien erstellen** (16 Dateien): ~2-3 Stunden
  - Je Bundesland: Grundstruktur + spezifische Recherche für externe Links

- **Front Matter hinzufügen** (30 Dateien): ~1 Stunde
  - Automatisierbar per Skript oder manuell

- **Aufräumen & Qualitätskontrolle**: ~30 Minuten

**Gesamt**: ~3,5-4,5 Stunden

## Automatisierungsmöglichkeiten

### Front Matter Bulk-Update (empfohlen)

Ein Python- oder Bash-Skript könnte:
1. Alle `.md` Dateien ohne Front Matter identifizieren
2. Bundesland und Dokumenttyp aus Dateiname extrahieren
3. Passendes Front Matter-Template einfügen
4. Datei mit Front Matter + Original-Content speichern

**Vorteil**: Schneller, konsistenter, weniger fehleranfällig

### Manuelle Umsetzung

Pro:
- Volle Kontrolle über jeden Titel
- Möglichkeit zur individuellen Anpassung

Contra:
- Zeitaufwändig bei 30 Dateien
- Höheres Fehlerrisiko (Tippfehler, inconsistente Formatierung)

## Entscheidungsfragen für den Benutzer

1. **nav_order für Bundesländer**: Alphabetisch (wie in der Tabelle) oder nach Einwohnerzahl/Relevanz?
2. **README.md**: Löschen oder archivieren?
3. **Automatisierung**: Soll ein Skript für Front Matter-Bulk-Update erstellt werden?
4. **has_children**: Sollen die Länder-Index-Seiten `has_children: false` haben (Dokumente werden nur auf Indexseite verlinkt) oder `has_children: true` (würde erfordern, dass Level-4-Dokumente in der Sidebar erscheinen)?

## Empfehlung

**Vorgehen**: Schrittweise Umsetzung in 3 Commits:
1. **Commit 1**: Index-Dateien für alle 16 Bundesländer
2. **Commit 2**: Front Matter zu allen 30 bestehenden Dokumenten
3. **Commit 3**: README.md aufräumen, Haupt-Index aktualisieren

**Begründung**:
- Klare Trennung der Änderungstypen
- Einfacheres Review
- Bei Problemen: Einzelne Commits können zurückgenommen werden

---

**Nächste Schritte**: Warte auf Benutzer-Feedback zu den Entscheidungsfragen vor Implementierung.
