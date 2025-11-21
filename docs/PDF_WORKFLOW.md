---
layout: default
title: PDF Workflow
parent: Dokumentation
nav_order: 5
permalink: /docs/pdf-workflow/
---

# PDF Workflow

## Grundsatz

PDF-Dateien von wichtigen Primärquellen werden lokal gespeichert und versioniert, um dauerhafte Verfügbarkeit zu gewährleisten.

## Wichtiger Hinweis zur PDF-Verarbeitung

**Stand 2025-09-21**: Eine direkte Online-Analyse von PDF-Dateien, die auf Webseiten verlinkt sind, ist mit Claude Code nicht möglich. Das WebFetch-Tool kann nur die HTML-Metadaten der verlinkenden Seite auslesen, nicht aber den PDF-Inhalt selbst. Daher ist ein lokaler Download der PDF-Datei zwingend erforderlich, bevor der Inhalt mit dem Read-Tool analysiert werden kann.

## 1. Download von PDFs

```bash
# Mit curl herunterladen (Windows-kompatibel)
curl -L -o "Dateiname.pdf" "https://url-zum-pdf.de/dokument.pdf"

# Alternativ mit vollständigen Parametern
curl -L -o "Dateiname.pdf" "https://url.de/dokument.pdf?__blob=publicationFile&v=3"
```

### Namenskonvention für PDFs

- Kurze, beschreibende Namen ohne Datum im Dateinamen
- Beispiele: `BBSR-Analysen-KOMPAKT-07-2024.pdf`, `Stakeholder-Dialog-Waermeplanung.pdf`

## 2. PDF mit Read-Tool lesen

```python
# Nach dem Download kann die PDF lokal gelesen werden
Read("E:/Documents/Coding/Digitale-Waermewende/stakeholder/bund/Dateiname.pdf")
```

## 3. Markdown-Dokumentation erstellen

Für jede wichtige PDF-Datei MUSS eine begleitende Markdown-Datei erstellt werden:

**Dateiname:** `YYYY-MM-DD_[Organisation]_[Titel].md`

**Inhalt muss enthalten:**

```markdown
## Metadaten
- **Lokal gespeichert**: stakeholder/bund/Dateiname.pdf (Dateigröße)
- **URL**: [Original-Download-URL]
- **ISBN/DOI**: [falls vorhanden]
```

## 4. Git Workflow für PDFs

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

## 5. Git LFS für PDF-Dateien

**Status: ✅ AKTIV seit 2025-11-18**

Dieses Repository verwendet **Git LFS** (Large File Storage) für alle PDF-Dateien.

### Was bedeutet das?

- Alle `*.pdf` Dateien werden automatisch über Git LFS verwaltet
- Die eigentlichen PDF-Dateien werden separat gespeichert
- Im Repository liegt nur ein kleiner "Zeiger" auf die Datei
- Repository bleibt klein und schnell, auch mit vielen/großen PDFs

### Konfiguration

- Datei: `.gitattributes` im Repository-Root
- Regel: `*.pdf filter=lfs diff=lfs merge=lfs -text`
- Alle PDFs werden automatisch erkannt und über LFS verwaltet

### Kostenlose Limits (GitHub Free)

- **1 GB LFS-Speicher** inklusive
- **1 GB Bandbreite** pro Monat inklusive
- Bei Bedarf: 50 GB Datenpaket für ~5 USD/Monat

### Aktueller Stand

- 15 PDF-Dateien bereits migriert (~50 MB)
- Platz für mehrere Dutzend weitere PDFs (2-15 MB)

### Wichtig für die tägliche Arbeit

- **KEINE Änderungen** im Workflow nötig!
- PDFs werden wie gewohnt mit `git add` und `git commit` hinzugefügt
- Git LFS arbeitet automatisch im Hintergrund
- Push/Pull funktionieren normal (Git LFS lädt PDFs hoch/herunter)

### PDF-Größenlimits

- Einzeldatei-Limit: 100 MB (GitHub LFS)
- Sehr große PDFs (>50 MB): Falls möglich, nur als Link referenzieren

### Versionierung

- Bei aktualisierten PDFs: Alte Version behalten, neue mit Versionsnummer
- Beispiel: `Leitfaden-v1.pdf` → `Leitfaden-v2.pdf`

### Datenschutz

- Keine internen/vertraulichen Dokumente hochladen
- Nur öffentlich verfügbare Quellen

### Prüfen ob LFS aktiv ist

```bash
# Liste aller LFS-verwalteten Dateien anzeigen
git lfs ls-files

# LFS-Status prüfen
git lfs status
```

## 6. Beispiel-Workflow

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

## Verwandte Dokumente

- [Structure Guide](STRUCTURE_GUIDE_Digitale-Waermewende.md) - Hauptdokument
- [Front-Matter Templates](FRONTMATTER_TEMPLATES.md) - Front-Matter-Struktur
- [URL Guidelines](URL_GUIDELINES.md) - URL-Formatierung
