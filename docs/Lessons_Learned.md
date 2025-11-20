---
layout: default
title: Lessons Learned
parent: Dokumentation
nav_order: 4
permalink: /docs/lessons-learned/
---

# Lessons Learned - Digitale Wärmewende Projekt

Dokumentation von Problemen, Lösungen und gewonnenen Erkenntnissen.

---

## Inhaltsverzeichnis

- [Template für neue Einträge](#template-für-neue-einträge)
- [Lessons Learned](#lessons-learned)
  - [2025-11-19: Jekyll Build-Fehler durch {% raw %}{% include %}{% endraw %} in Code-Beispiel](#2025-11-19-jekyll-build-fehler-durch-include-in-code-beispiel)

---

## Template für neue Einträge

Verwenden Sie diese Struktur für neue Lessons Learned Einträge:

```markdown
## YYYY-MM-DD: Kurzer Titel des Problems

### Problem

**Symptom:**
- Was ist passiert?
- Welche Fehler wurden beobachtet?

**Ursache:**
- Warum ist es passiert?
- Was war die Root Cause?

**Auswirkung:**
- Welche Konsequenzen hatte das Problem?
- Wer/Was war betroffen?

### Lösungsweg

1. Schritt 1: Erste Diagnose-Schritte
2. Schritt 2: Hypothesen testen
3. Schritt 3: Lösung implementieren
4. Schritt 4: Verifikation

### Was wir gelernt haben

#### Haupterkenntnisse
- Erkenntnis 1: Was haben wir verstanden?
- Erkenntnis 2: Welche Konzepte sind wichtig?
- Erkenntnis 3: Was war überraschend?

#### Best Practices
- Was machen wir jetzt anders?
- Welche Prozesse ändern wir?

### Prävention für die Zukunft

**Checklists:**
- [ ] Check 1
- [ ] Check 2

**Workflows:**
- Neuer Prozess A
- Neuer Prozess B

### Verwandte Commits

- `hash` - Commit-Beschreibung
- `hash` - Fix-Beschreibung

### Referenzen

- [Link zu Dokumentation]
- [Link zu verwandten Issues]
```

**Hinweise zur Verwendung:**
- Fügen Sie neue Einträge chronologisch ein (neueste oben)
- Aktualisieren Sie das Inhaltsverzeichnis
- Verlinken Sie relevante Commits
- Fügen Sie Screenshots/Logs als Dateien im `docs/` Ordner hinzu

---

## Lessons Learned

### 2025-11-19: Jekyll Build-Fehler durch {% raw %}{% include %}{% endraw %} in Code-Beispiel

### Problem

**Symptom:**
- GitHub Pages Build schlug fehl mit Fehler: `Could not locate the included file 'svg/standards-uebersicht.svg'`
- Index.md Änderungen (SVG-Test Link) wurden nicht deployed
- svg-test.md Seite zeigte 404
- Obwohl Dateien korrekt im Repository waren und lokal commited/gepusht wurden

**Ursache:**
In der Datei `docs/ANLEITUNG_Klickbare-SVG-Grafiken.md` befand sich ein Code-Beispiel für Jekyll Includes:

```markdown
### Schritt 2: In Markdown einbinden

```markdown
---
layout: default
title: Standards Übersicht
---

# Unsere Standards

{% include svg/standards-uebersicht.svg %}
```
```

**Das Problem:** Jekyll verarbeitet Liquid-Tags wie `{% include %}` auch innerhalb von Markdown Code-Blöcken und versuchte, die (nicht existierende) Datei `svg/standards-uebersicht.svg` tatsächlich zu inkludieren.

**Auswirkung:**
- Jekyll Build brach ab
- Keine neuen Änderungen wurden auf GitHub Pages deployed
- Die Website zeigte den letzten erfolgreichen Build (Commit 451a179)
- Neuere Commits (3d465a6, d776087, ca13e45) wurden nicht deployed

### Lösungsweg

**1. Symptome identifiziert (mehrere Versuche):**
- Strg+F5 half nicht (kein Cache-Problem)
- Links waren in GitHub Repository sichtbar, aber nicht auf der Website
- Vermutung: GitHub Pages Build-Problem

**2. Build-Logs analysiert:**
User kopierte GitHub Actions Build-Log, der zeigte:
```
Liquid Exception: Could not locate the included file 'svg/standards-uebersicht.svg'
in any of ["/github/workspace/_includes", "/tmp/jekyll-remote-theme-20251119-7-6mjwk6/_includes"].
Ensure it exists in one of those directories and is not a symlink as those are not allowed in safe mode.
in docs/ANLEITUNG_Klickbare-SVG-Grafiken.md
```

**3. Ursache gefunden:**
Der `{% include %}` Tag in Zeile 166 wurde von Jekyll als echter Befehl interpretiert, nicht als Code-Beispiel.

**4. Lösung implementiert:**
Code-Beispiel mit `{% raw %}` und `{% endraw %}` Tags umschließen:

```markdown
# Unsere Standards

{% raw %}{% include svg/standards-uebersicht.svg %}{% endraw %}
```

**5. Verifikation:**
- Commit 903b741: "fix: Escapiere Jekyll include in SVG-Anleitung Code-Beispiel"
- Build erfolgreich
- Website deployed mit allen neuen Änderungen

### Was wir gelernt haben

#### 1. Jekyll Liquid-Tag Verarbeitung

**Problem:**
Jekyll verarbeitet Liquid-Tags (`{% ... %}`, `{{ ... }}`) überall im Dokument, auch in Code-Blöcken.

**Lösung:**
Code-Beispiele mit Liquid-Tags müssen escapiert werden:

```liquid
{% raw %}
  {% include file.html %}
  {{ variable }}
{% endraw %}
```

**Best Practice:**
- Immer `{% raw %}` ... `{% endraw %}` verwenden für Liquid-Code-Beispiele
- Gilt auch für Inline-Code: {% raw %}`{{ variable }}`{% endraw %}
- Alternative: HTML Entity Codes verwenden

#### 2. Build-Fehler Diagnose

**Wichtige Erkenntnis:**
Wenn GitHub Pages nicht aktualisiert wird:

1. **Nicht Cache-Problem, wenn:**
   - Strg+F5 hilft nicht
   - Mehrere Browser zeigen gleiches Ergebnis
   - Änderungen sind im GitHub Repository sichtbar

2. **Build-Logs sind essentiell:**
   - GitHub Actions → "pages build and deployment"
   - Fehler oft sehr spezifisch: Datei, Zeile, Problem
   - Logs zeigen welcher Commit gebaut wurde

3. **Deployment-Historie prüfen:**
   - Welcher Commit ist live?
   - Vergleich mit neuesten Commits
   - Bei Diskrepanz → Build-Problem

#### 3. Schrittweise Fehlersuche

**Erfolgreiche Strategie:**

1. **Symptom beschreiben:** Website zeigt alte Version
2. **Cache ausschließen:** Strg+F5, andere Browser
3. **GitHub vs. Live vergleichen:** Welcher Commit ist deployed?
4. **Build-Logs anfordern:** Konkrete Fehlermeldung finden
5. **Datei & Zeile identifizieren:** Exakte Fehlerquelle
6. **Root Cause:** Warum passiert das?
7. **Fix implementieren:** Minimal invasive Lösung
8. **Verifizieren:** Build erfolgreich, Website aktualisiert

#### 4. Dokumentations-Fallstricke

**Vorsicht bei:**
- Dokumentation von Template-Engines (Jekyll, Hugo, etc.)
- Code-Beispiele mit speziellen Zeichen (`{`, `%`, `$`)
- Verschachtelte Code-Blöcke
- Beispiele für Konfigurationsdateien mit Variablen

**Empfehlung:**
- Testing-Strategie für Dokumentation
- Lokaler Jekyll-Build vor Commit (wenn möglich)
- Code-Beispiele in separate Test-Dateien auslagern

#### 5. Jekyll Safe Mode Einschränkungen

**Erkenntnisse:**
- GitHub Pages läuft im "Safe Mode"
- Keine Symlinks erlaubt
- Eingeschränkte Plugins
- Striktere Validierung als lokaler Build

**Konsequenz:**
- Was lokal funktioniert, kann auf GitHub Pages fehlschlagen
- GitHub Actions Logs sind die "Source of Truth"
- Bei Problemen: Build-Logs zuerst prüfen

### Prävention für die Zukunft

#### Dokumentations-Checklist

Bei Anleitungen mit Code-Beispielen:

- [ ] Liquid-Tags in Code-Blöcken mit {% raw %}`{% raw %}`{% endraw %} escapen
- [ ] Geschweife Klammern in YAML-Beispielen prüfen
- [ ] Nach Commit: GitHub Actions Build-Status prüfen
- [ ] Bei 404 auf neuen Seiten: Erst Build-Logs prüfen, nicht Cache

#### Repository-Struktur

```
docs/
  ANLEITUNG_*.md         # Aktive Anleitungen
  WORKFLOW_*.md          # Aktive Workflows
  Lessons_Learned.md     # Diese Datei
archive/
  YYYY-MM-DD/            # Archivierte Dokumente
  ARCHIVE_LOG.md         # Commit-Historie
temp/
  TODO_*.md              # Temporäre Arbeiten
```

#### Workflow bei Problemen

1. **Symptom dokumentieren** (Screenshot, Fehlermeldung)
2. **Build-Logs prüfen** (GitHub Actions)
3. **Fehler eingrenzen** (Datei, Zeile, Kontext)
4. **Minimal Fix** (kleinste mögliche Änderung)
5. **Verifizieren** (Build-Status, Live-Seite)
6. **Dokumentieren** (in Lessons_Learned.md)

### Verwandte Commits

- **Problem verursacht durch:** `3d465a6` - Add SVG guide and interactive test diagram
- **Problem entdeckt:** Mehrere Commits später, als Website nicht aktualisierte
- **Problem gelöst:** `903b741` - fix: Escapiere Jekyll include in SVG-Anleitung Code-Beispiel
- **Weitere Fixes:**
  - `f5c5bab` - fix: Korrigiere SVG-Pfad mit Jekyll relative_url Filter
  - `c757dfc` - fix: Korrigiere SVG-Links mit absolutem Pfad
  - `cc8bee8` - fix: Füge target="_top" zu SVG-Links hinzu

### Referenzen

- [Jekyll Liquid Documentation](https://jekyllrb.com/docs/liquid/)
- [Jekyll Raw Tag](https://jekyllrb.com/docs/liquid/tags/#code-snippet-highlighting)
- [GitHub Pages Build Logs](https://github.com/Digitale-Waermewende/Digitale-Waermewende/actions)
- Archive Log: `archive/ARCHIVE_LOG.md`
- Fehlerhafte Datei: `docs/ANLEITUNG_Klickbare-SVG-Grafiken.md` (Zeile 166)

---

*[Zurück zum Inhaltsverzeichnis](#inhaltsverzeichnis)*
