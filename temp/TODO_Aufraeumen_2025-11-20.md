# TODO: Aufräumen Digitale-Waermewende Repository

**Datum:** 2025-11-20
**Ziel:** Repository-Struktur bereinigen, Archiv und Temp-Ordner einrichten

---

## 1. Ordnerstruktur anlegen

### 1.1 Archiv-Ordner anlegen
- [ ] Ordner `archive/` auf Root-Ebene erstellen
- [ ] Git LFS für Archive konfigurieren
- [ ] `.gitattributes` Datei erstellen mit LFS-Tracking für Archive

### 1.2 Temp-Ordner anlegen
- [ ] Ordner `temp/` auf Root-Ebene erstellen
- [ ] Temp-Ordner in Jekyll `_config.yml` exclude Liste eintragen
- [ ] `.gitignore` aktualisieren für lokale Temp-Dateien (optional)

---

## 2. Root-Ebene aufräumen

### 2.1 Dateien verschieben
- [ ] `STRUCTURE_GUIDE_Digitale-Waermewende.md` → nach `docs/`
- [ ] Prüfen ob `docs.md` und `stakeholder.md` noch benötigt werden (scheinen Navigation-Dateien zu sein)

### 2.2 Zu behaltende Dateien auf Root
- [x] `index.md` - Hauptseite (behalten)
- [x] `svg-test.md` - Test-Seite (behalten)
- [x] `CLAUDE.md` - Projekt-Instruktionen (behalten)
- [x] `README.md` - GitHub-Readme (behalten)
- [x] `_config.yml` - Jekyll-Konfiguration (behalten)

---

## 3. docs/ Ordner aufräumen

### 3.1 TODO-Dateien → MANUELL prüfen und verschieben
**Zur manuellen Prüfung durch User:**
- [ ] `2025-11-18_TODO-Jekyll-Navigation-Fix.md` → temp/ oder archive/ ?
- [ ] `2025-11-18_TODO-XLeitstelle-Standards-Umstrukturierung.md` → temp/ oder archive/ ?
- [ ] `2025-11-18_Laender-Update-Plan.md` → temp/ oder archive/ ?

### 3.2 Analyse-Dateien → ins Archiv
- [ ] `2025-11-18_Interne-Links-Korrektur-Analyse.md` → `archive/`
- [ ] `2025-11-18_Jekyll-Navigation-URL-Issues_Analysis.md` → `archive/`

### 3.3 Sonstige Dateien prüfen
- [ ] `github-pages-build-error-log-2025-11-19.txt` → `archive/` (Build-Log aus Debugging)
- [ ] `github-pages-setup.md` → in `docs/` behalten oder nach `archive/` ?

### 3.4 Zu behaltende Dateien in docs/
- [x] `ANLEITUNG_Klickbare-SVG-Grafiken.md` - Aktive Anleitung (behalten)
- [x] `WORKFLOW_Deep-Research.md` - Aktiver Workflow (behalten)

---

## 4. Backup-Dateien aufräumen (32 Dateien)

### 4.1 Git LFS für Backups einrichten
- [ ] Git LFS installieren prüfen: `git lfs version`
- [ ] Git LFS initialisieren: `git lfs install`
- [ ] Tracking-Regel für Backups: `git lfs track "archive/**/*.backup"`

### 4.2 Backup-Dateien verschieben
**Quellen:**
- `stakeholder/laender/*/` (29 .backup Dateien)
- `standards/XPlanung/` (3 .backup Dateien)

**Ziel:**
- [ ] Alle .backup Dateien nach `archive/backup-laender/` verschieben
- [ ] Alternativ: `archive/backup-standards/` für Standards-Backups
- [ ] Backup-Dateien zu Git LFS hinzufügen
- [ ] Original-Speicherorte bereinigen

**Betroffene Dateien (32 gesamt):**
- Baden-Württemberg: 2 Dateien
- Bayern: 2 Dateien
- Berlin: 1 Datei
- Brandenburg: 2 Dateien
- Bremen: 1 Datei
- Hamburg: 1 Datei
- Hessen: 2 Dateien
- Mecklenburg-Vorpommern: 2 Dateien
- Niedersachsen: 2 Dateien
- Nordrhein-Westfalen: 2 Dateien
- Rheinland-Pfalz: 2 Dateien
- Saarland: 2 Dateien
- Sachsen: 2 Dateien
- Sachsen-Anhalt: 2 Dateien
- Schleswig-Holstein: 2 Dateien
- Thüringen: 2 Dateien
- XPlanung: 3 Dateien

---

## 5. Jekyll-Konfiguration anpassen

### 5.1 _config.yml anpassen
- [ ] `archive/` in `exclude:` Liste eintragen
- [ ] `temp/` in `exclude:` Liste eintragen
- [ ] `TODO_*.md` Pattern in `exclude:` Liste eintragen

### 5.2 Navigation bereinigen
- [ ] Prüfen ob temporäre Dateien noch in Navigation auftauchen
- [ ] Bei Bedarf `nav_exclude: true` in Front Matter ergänzen

---

## 6. Git LFS Setup (falls noch nicht vorhanden)

### 6.1 Installation prüfen
```bash
git lfs version
# Falls nicht installiert: https://git-lfs.github.com/
```

### 6.2 LFS für Repository einrichten
```bash
git lfs install
git lfs track "archive/**/*.backup"
git lfs track "archive/**/*.pdf"
```

### 6.3 .gitattributes prüfen/erstellen
- [ ] Datei `.gitattributes` im Root erstellen falls nicht vorhanden
- [ ] LFS-Tracking-Regeln eintragen

---

## 7. Testing und Validation

### 7.1 Lokale Tests
- [ ] Jekyll Build lokal testen (falls möglich)
- [ ] Prüfen dass archive/ und temp/ nicht in Navigation erscheinen

### 7.2 GitHub Pages Tests
- [ ] Commit und Push durchführen
- [ ] GitHub Actions Build-Log prüfen
- [ ] Website prüfen: Keine temporären Dateien in Navigation

---

## 8. Dokumentation aktualisieren

### 8.1 CLAUDE.md aktualisieren
- [ ] Neue Ordnerstruktur dokumentieren
- [ ] Archive-Nutzung beschreiben
- [ ] Temp-Ordner-Nutzung beschreiben

### 8.2 README.md aktualisieren
- [ ] Ordnerstruktur im README aktualisieren

---

## Offene Fragen

1. **docs.md und stakeholder.md auf Root-Ebene:**
   - Was ist der Zweck dieser Dateien?
   - Sollen sie behalten, verschoben oder gelöscht werden?

2. **github-pages-setup.md:**
   - Noch relevante Setup-Anleitung oder archivieren?

3. **Git LFS Größenlimit:**
   - Sind 32 .backup Dateien im Rahmen des GitHub Free LFS-Limits (1 GB)?
   - Alternative: Nur lokal archivieren ohne Git LFS?

---

## Reihenfolge der Durchführung

**Phase 1: Vorbereitung**
1. Archive und Temp Ordner anlegen
2. Git LFS einrichten
3. Jekyll _config.yml anpassen

**Phase 2: Verschieben**
4. Analyse-Dateien ins Archive
5. TODO-Dateien manuell prüfen und verschieben
6. Backup-Dateien ins LFS-Archive
7. STRUCTURE_GUIDE nach docs/

**Phase 3: Testing**
8. Commit und Push
9. GitHub Pages Build prüfen
10. Dokumentation aktualisieren

---

## Status Tracking

- **Erstellt:** 2025-11-20
- **Gestartet:** [Datum]
- **Abgeschlossen:** [Datum]
- **Commits:** [Liste der relevanten Commits]
