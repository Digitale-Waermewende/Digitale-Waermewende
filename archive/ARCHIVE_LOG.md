# Archiv-Log

Chronologische Übersicht aller archivierten Inhalte mit Commit-Referenzen.

---

## Format

Jeder Eintrag dokumentiert:
- **Datum** der Archivierung
- **Commit-Hash** für Git-Nachverfolgung
- **Zusammenfassung** was archiviert wurde und warum

---

## Einträge

### 2025-11-20 | Erstes Repository-Aufräumen

**Commit:** `11e286c` - [View on GitHub](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/11e286c)

**Zusammenfassung:**
- 32 .backup Dateien (164 KB) aus stakeholder/laender/ und standards/XPlanung/
- 3 Analyse-/Dokumentationsdateien aus docs/ (erledigt/obsolet)
- 2 Root-Level Dateien (docs.md, stakeholder.md - obsolet)
- 1 Build-Error-Log (Debugging abgeschlossen)
- STRUCTURE_GUIDE nach docs/ verschoben
- TODO-Liste nach temp/ verschoben

**Grund:** Initiales Aufräumen nach Projektstrukturierung und Jekyll-Migration

**Ziel:** `archive/2025-11-20/`

---

### 2025-11-20 | TODO-Dateien archivieren (Nachträglich)

**Commit:** `bb75794` - [View on GitHub](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/bb75794)

**Zusammenfassung:**
- 2 erledigte TODO-Dateien aus docs/
  - Jekyll-Navigation-Fix (21 KB) - alle 6 Phasen abgeschlossen
  - XLeitstelle-Standards-Umstrukturierung (14 KB) - Umstrukturierung umgesetzt

**Grund:** Aufgaben vollständig abgeschlossen

**Ziel:** `archive/2025-11-20/docs/`

---

### 2025-11-20 | Laender-Update-Plan archivieren

**Commit:** `5f0c590` - [View on GitHub](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/5f0c590)

**Zusammenfassung:**
- 1 erledigte TODO-Datei aus docs/
  - Laender-Update-Plan (12 KB) - Front Matter für alle 30 Länder-Dokumente hinzugefügt, 17 Index-Dateien erstellt

**Grund:** Aufgabe vollständig abgeschlossen (verifiziert durch Stichproben)

**Ziel:** `archive/2025-11-20/docs/`

---

### 2025-11-20 | Lessons_Learned.md temporär archiviert (Build-Probleme)

**Commit:** [wird ergänzt]

**Zusammenfassung:**
- 1 Datei aus docs/ wegen persistenter Jekyll Build-Fehler
  - Lessons_Learned.md - Zu viele verschachtelte Liquid-Tags verursachen Build-Fehler

**Grund:** Vermeidung weiterer Build-Failures, wird später überarbeitet

**Ziel:** `archive/2025-11-20/docs/`

---

<!-- Template für neue Einträge:

### YYYY-MM-DD | Kurzbeschreibung

**Commit:** `hash` oder [Link](https://github.com/...)

**Zusammenfassung:**
- X Dateien von [Quelle]
- Kurze Beschreibung was und warum

**Grund:** [Projektphase/Aufgabe/Grund]

**Ziel:** `archive/YYYY-MM-DD/`

-->
