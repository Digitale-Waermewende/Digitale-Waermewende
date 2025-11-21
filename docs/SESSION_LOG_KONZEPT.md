# Konzept: Session Log für Claude Code Kommunikation

## Zweck

Dokumentation aller Claude Code Sessions zur Nachvollziehbarkeit der Entwicklung des Repositories. Das Session Log dient als:

1. **Projekt-Tagebuch**: Chronologische Übersicht aller Änderungen
2. **Entscheidungsdokumentation**: Warum wurden bestimmte Strukturen gewählt?
3. **Lernressource**: Wie läuft die Kommunikation zwischen User und AI?
4. **Audit Trail**: Vollständige Nachvollziehbarkeit aller Commits

## Dateiname und Location

**Datei:** `SESSION_LOG.md`
**Location:** Repository-Root (`Digitale-Waermewende/SESSION_LOG.md`)
**Navigation:** Direkt aus Hauptnavigation sichtbar (Level 1)

## Front Matter für SESSION_LOG.md

```yaml
---
layout: default
title: Session Log
nav_order: 10
has_children: false
permalink: /session-log/
---
```

**Begründung für `nav_order: 10`:**
- Stakeholder: nav_order 2
- Standards: nav_order 3
- Gesetze: nav_order 4
- Dokumentation: nav_order 5
- Session Log: nav_order 10 (ganz unten, aber prominent)

## Struktur der SESSION_LOG.md

```markdown
---
layout: default
title: Session Log
nav_order: 10
has_children: false
permalink: /session-log/
---

# Session Log - Claude Code Kommunikation

Chronologische Dokumentation aller Claude Code Sessions für das Repository Digitale-Waermewende.

**Zweck**: Nachvollziehbarkeit der Entwicklung, Entscheidungsdokumentation, Audit Trail

---

## Session [NUMMER] - [YYYY-MM-DD HH:MM] - [KURZTITEL]

**Metadaten**: [Datum] | [HH:MM - HH:MM] | Commits: [hash1], [hash2]

### User-Eingaben

#### 1. Initiale Anfrage
```
[Exakte User-Eingabe im Terminal]
```

#### 2. Rückfrage von Claude (falls vorhanden)
[Claude's Rückfrage]

**User-Antwort**:
```
[Exakte Antwort des Users]
```

### Ergebnisse

**Commits**: [hash1](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/hash1), [hash2](https://github.com/...hash2)

**Neue Seiten**:
- [Seitentitel](/permalink/zur/seite/)

**Geänderte Seiten**:
- [Seitentitel](/permalink/zur/seite/)

### Entscheidungen

- [Kernentscheidung 1]
- [Kernentscheidung 2]

---

[Weitere Sessions chronologisch in umgekehrter Reihenfolge (neueste oben)]
```

## Beispiel einer Session (Ausgefüllt)

```markdown
## Session 003 - 2025-11-21 14:30 - IT-Planungsrat als Stakeholder

**Metadaten**: 2025-11-21 | 14:30 - 16:15 | Commits: [fce6b3d](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/fce6b3d)

### User-Eingaben

#### 1. Initiale Anfrage
```
Bitte erstelle unter Stakeholder einen Eintrag für den IT-Planungsrat.
Die Gesetze/IT-Staatsvertrag ist ein ganz guter Startpunkt.
Beschreibe hier genauer das Selbstverständnis und die Arbeitsweise der Organisation.
Verlinke dann Bidirektional zum Gesetze/IT-Staatsvertrag, zu Stakeholder/XLeitstelle
und den XStandards.
```

### Ergebnisse

**Commits**: [fce6b3d](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/fce6b3d)

**Neue Seiten**:
- [IT-Planungsrat](/stakeholder/bund/it-planungsrat/)

**Geänderte Seiten**:
- [IT-Staatsvertrag](/gesetze/it-staatsvertrag/)
- [XLeitstelle](/stakeholder/bund/xleitstelle/)
- [XPlanung](/standards/xplanung/)
- [XBau](/standards/xbau/)
- [XTrasse](/standards/xtrasse/)

### Entscheidungen

- IT-Planungsrat als Stakeholder unter `bund/` eingeordnet (nicht eigene Kategorie)
- Trennung von Governance-Ebene (IT-Planungsrat) und operativer Ebene (XLeitstelle) in allen XStandards etabliert
- Deep Research mit Task-Agent für umfassende Informationsbeschaffung
- Bidirektionale Verlinkungen zwischen Gesetzen, Organisationen und Standards
```

## Workflow für Session-Dokumentation

### 1. Session-Start
User oder Claude notiert Startzeit und initiale Anfrage.

### 2. Während der Session
- User-Eingaben werden wörtlich festgehalten
- Rückfragen von Claude werden dokumentiert
- User-Antworten werden notiert

### 3. Session-Ende
Nach Abschluss aller Commits:
1. SESSION_LOG.md öffnen
2. Neuen Session-Eintrag an den Anfang hinzufügen (neueste Sessions oben)
3. Metadaten ausfüllen (Datum, Zeit, Commits)
4. User-Eingaben chronologisch dokumentieren
5. Ergebnisse listen (Dateien, Commits mit Links)
6. Entscheidungen und Erkenntnisse festhalten
7. Lessons Learned notieren

### 4. Git Commit für Session Log
```bash
git add SESSION_LOG.md
git commit -m "docs: Session [NUMMER] dokumentiert - [Kurztitel]"
git push
```

## Metadaten-Template für Copy-Paste

```markdown
## Session [NR] - [YYYY-MM-DD HH:MM] - [KURZTITEL]

**Metadaten**: [Datum] | [HH:MM - HH:MM] | Commits: [hash](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/hash)

### User-Eingaben

#### 1. Initiale Anfrage
```
```

### Ergebnisse

**Commits**: [hash](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/hash)

**Neue Seiten**:
- [Titel](/permalink/zur/seite/)

**Geänderte Seiten**:
- [Titel](/permalink/zur/seite/)

### Entscheidungen

-

---
```

## Vorteile dieses Konzepts

### Für das Projekt
- ✅ Vollständige Nachvollziehbarkeit aller Änderungen
- ✅ Dokumentation von Entscheidungsprozessen
- ✅ Lernressource für zukünftige Sessions
- ✅ Audit Trail für alle Commits

### Für den User
- ✅ Überblick über alle Sessions und deren Ergebnisse
- ✅ Schneller Zugriff auf frühere Entscheidungen
- ✅ Verständnis, warum Strukturen so gewählt wurden

### Für Claude
- ✅ Kontext über frühere Sessions
- ✅ Verständnis über Projekt-Entwicklung
- ✅ Basis für kontinuierliche Verbesserung

## Integration in STRUCTURE_GUIDE

### Neuer Abschnitt im STRUCTURE_GUIDE

Füge nach dem Abschnitt "PDF-Dateien Workflow" (vor "Offene Fragen") folgenden neuen Abschnitt ein:

```markdown
## Session Log - Dokumentation der Claude Code Kommunikation

### Zweck
Das Session Log dokumentiert alle Claude Code Sessions zur Nachvollziehbarkeit der Repository-Entwicklung.

### Datei
- **Location**: `SESSION_LOG.md` im Repository-Root
- **Navigation**: Level 1 (nav_order: 10) - direkt aus Hauptnavigation sichtbar
- **Format**: Chronologisch, neueste Sessions oben

### Struktur jedes Session-Eintrags

**Metadaten**:
- Datum, Start-/Endzeit, Dauer
- Claude Modell
- Commit-Hashes

**User-Eingaben**:
- Wörtliche Dokumentation aller Terminal-Eingaben
- Claude's Rückfragen
- User-Antworten

**Ergebnisse**:
- Erstellte und geänderte Dateien
- Commits mit GitHub-Links
- Links zu erstellten Seiten

**Entscheidungen und Erkenntnisse**:
- Strukturelle und technische Entscheidungen
- Offene Fragen
- Lessons Learned

### Workflow
1. Session durchführen
2. Nach Abschluss: SESSION_LOG.md öffnen
3. Neuen Session-Eintrag an den Anfang einfügen
4. Metadaten, Eingaben, Ergebnisse, Entscheidungen dokumentieren
5. Commit mit "docs: Session [NUMMER] dokumentiert"

### Detailliertes Konzept
Siehe `docs/SESSION_LOG_KONZEPT.md` für vollständiges Konzept mit Templates und Beispielen.
```

## Front Matter für SESSION_LOG_KONZEPT.md

```yaml
---
layout: default
title: Session Log Konzept
parent: Dokumentation
nav_order: 2
permalink: /docs/session-log-konzept/
---
```

## Nächste Schritte

1. ✅ Konzept erstellen (diese Datei)
2. ⏳ Initiale SESSION_LOG.md erstellen
3. ⏳ STRUCTURE_GUIDE aktualisieren (neuer Abschnitt)
4. ⏳ Erste Session(s) nachträglich dokumentieren (wenn möglich)
5. ⏳ Commit und Push
