# Archiv

Dieses Verzeichnis enthält archivierte Dateien aus dem Projekt Digitale-Waermewende.

## Struktur

```
archive/
  YYYY-MM-DD/          # Archiv nach Datum
    [Dateien]          # Archivierte Inhalte
  ARCHIVE_LOG.md       # Chronologisches Log aller Archivierungen
  README.md            # Diese Datei
```

## Zweck

- **Aufbewahrung** abgeschlossener Arbeiten und obsoleter Dateien
- **Nachvollziehbarkeit** durch Git-Historie und ARCHIVE_LOG.md
- **Bereinigung** der aktiven Projektstruktur

## Archivierungs-Richtlinien

### Was wird archiviert?
- Erledigte TODO-Listen und Analysen
- Backup-Dateien nach erfolgreicher Migration
- Obsolete Dokumentation
- Abgeschlossene temporäre Arbeiten aus `temp/`

### Wann archivieren?
- Nach Abschluss größerer Projektphasen
- Bei strukturellen Umorganisationen
- Wenn Dateien nicht mehr aktiv benötigt werden, aber historisch relevant sind

## Zugriff

Alle archivierten Dateien bleiben:
- In der Git-Historie verfügbar
- Lokal im `archive/` Ordner
- Dokumentiert im `ARCHIVE_LOG.md`

## Backup-Strategie

**Aktuell (2025-11-20):**
- Repository: ~18 MB
- Git LFS: ~6 MB (von 1 GB)
- Status: Keine Komprimierung notwendig

**Bei Bedarf (>500 MB LFS):**
- Alte Archive können gezippt werden
- ZIP-Dateien in Git LFS verschieben
- Originale lokal löschen
- Im ARCHIVE_LOG.md dokumentieren

## Siehe auch

- `/temp/` - Temporäre Arbeiten (nicht versioniert/excluded)
- `ARCHIVE_LOG.md` - Detailliertes Log
- `CLAUDE.md` - Projekt-Instruktionen
