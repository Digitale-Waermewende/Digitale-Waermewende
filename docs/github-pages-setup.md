# GitHub Pages Setup - Anleitung

## Strategischer Ansatz für die Veröffentlichung

Ihre MD-Dokumente können über GitHub Pages öffentlich zugänglich gemacht werden. Hier ist die empfohlene Strategie:

## 1. Bereits erstellte Konfiguration

Ich habe folgende Dateien für Sie vorbereitet:

### ✅ `_config.yml` - Jekyll-Konfiguration
- Theme: minima (schlicht und funktional)
- Navigation zu allen Hauptbereichen
- Automatische Sitemaps und SEO-Tags
- PDF-Dateien werden ausgeschlossen

### ✅ `index.md` - Startseite
- Übersicht aller Bundesländer-Analysen
- Direktlinks zu den wichtigsten Dokumenten
- Strukturierte Navigation nach Regionen
- Best Practices hervorgehoben

### ✅ `README.md` - Angepasst
- Link zur GitHub Pages Dokumentation
- Klare Struktur für Repository-Besucher

## 2. GitHub Pages aktivieren

### Schritte zur Aktivierung:

1. **Öffnen Sie Ihr Repository auf GitHub:**
   ```
   https://github.com/Digitale-Waermewende/Digitale-Waermewende
   ```

2. **Navigieren Sie zu Settings:**
   - Klicken Sie auf "Settings" im Repository-Menü

3. **GitHub Pages konfigurieren:**
   - Scrollen Sie zu "Pages" im linken Menü
   - Source: "Deploy from a branch"
   - Branch: "master" oder "main" auswählen
   - Folder: "/ (root)" auswählen
   - Klicken Sie "Save"

4. **Warten Sie 2-5 Minuten**
   - GitHub baut die Seite automatisch
   - URL wird sein: https://digitale-waermewende.github.io/Digitale-Waermewende/

## 3. Optional: Custom Domain

Falls Sie eine eigene Domain haben (z.B. waermewende-doku.de):

1. Erstellen Sie eine `CNAME` Datei im Repository-Root
2. Fügen Sie Ihre Domain ein (ohne https://)
3. Konfigurieren Sie DNS bei Ihrem Domain-Provider

## 4. Struktur-Vorteile

### Was funktioniert automatisch:
- ✅ Alle MD-Dateien werden zu HTML konvertiert
- ✅ Navigation zwischen Dokumenten funktioniert
- ✅ PDFs werden nicht veröffentlicht (Speicherplatz)
- ✅ Responsive Design für Mobile/Desktop

### URLs Ihrer Dokumente:
```
Basis: https://digitale-waermewende.github.io/Digitale-Waermewende/

Beispiele:
/stakeholder/bund/KWW-Halle/2025-09-21_KWW-Datenkompass
/stakeholder/bund/KWW-Halle/2025-09-21_KWW-Datenkompass-Bayern-Analyse
```

## 5. Wartung und Updates

### Bei neuen Dokumenten:
1. MD-Datei erstellen/bearbeiten
2. Git commit & push
3. GitHub Pages aktualisiert automatisch (2-5 Min)

### Index-Seite aktualisieren:
- Bei neuen Bundesländern: `index.md` ergänzen
- Bei neuen Kategorien: Navigation erweitern

## 6. Erweiterte Optionen

### Falls mehr Gestaltung gewünscht:

**Option A: Anderes Jekyll-Theme**
```yaml
# In _config.yml ändern:
theme: just-the-docs  # Dokumentations-fokussiert
# oder
remote_theme: pmarsceill/just-the-docs
```

**Option B: Lokales Testen**
```bash
# Ruby und Jekyll installieren
gem install bundler jekyll
# Im Repository:
bundle init
bundle add jekyll
bundle exec jekyll serve
# Öffnen: http://localhost:4000
```

## 7. Nächste Schritte

1. **Commit der neuen Dateien:**
   ```bash
   git add _config.yml index.md docs/github-pages-setup.md
   git commit -m "GitHub Pages Konfiguration hinzugefügt"
   git push
   ```

2. **GitHub Pages aktivieren** (siehe Punkt 2)

3. **URL testen** nach 5 Minuten

4. **Optional:** Badge in README wurde bereits hinzugefügt

## Vorteile Ihrer Lösung

- 🌍 **Öffentlich zugänglich** ohne Hosting-Kosten
- 🔍 **SEO-optimiert** durch Jekyll
- 📱 **Responsive** auf allen Geräten
- 🔄 **Automatische Updates** bei Git-Push
- 📊 **Strukturierte Navigation** bereits vorbereitet
- 🏷️ **Versionskontrolle** durch Git

## Support

Bei Problemen mit GitHub Pages:
- GitHub Pages Dokumentation: https://docs.github.com/pages
- Jekyll Dokumentation: https://jekyllrb.com/docs/
- Status-Seite: https://www.githubstatus.com/

---
*Diese Anleitung wurde für das Digitale-Waermewende Projekt erstellt.*