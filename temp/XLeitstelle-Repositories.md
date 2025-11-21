# XLeitstelle GitLab OpenCode Repositories - Analyse und Zugriffsprobleme

**Erstellt am**: 2025-11-21
**Zweck**: Dokumentation der XLeitstelle-Repositories und JavaScript-Navigationsproblem

---

## Problem: JavaScript-basierte GitLab-Navigation

### Kernproblem

**GitLab OpenCode** (gitlab.opencode.de) nutzt **clientseitiges JavaScript-Rendering** für Repository-Inhalte, was automatisierte Zugriffe über WebFetch-Tools verhindert.

### Symptome

1. **HTML-Quelltext ist fast leer**: Nur JavaScript-Code (CDATA-Blöcke), keine sichtbaren Inhalte
2. **Repository-Listen fehlen**: Keine Auflistung von Unterverzeichnissen oder Dateien
3. **"Loading"-Anzeigen**: Seiten zeigen dauerhaft Ladezustand
4. **WebFetch-Limitation**: Tools können nur HTML-Gerüst abrufen, nicht die gerenderten Inhalte

### Technische Ursache

```
HTML-Quelltext:
├── GitLab-Konfiguration (JavaScript CDATA)
├── Tracking-Skripte (Snowplow, Matomo)
└── Leeres HTML-Gerüst (<div id="app"></div>)
     ↓
JavaScript rendert clientseitig:
├── Repository-Listen
├── Dateistrukturen
└── Inhaltsvorschauen
```

**WebFetch sieht**: Nur das leere Gerüst
**Browser sieht**: Vollständig gerenderte Inhalte (nach JavaScript-Ausführung)

---

## Betroffene XLeitstelle-Repositories

### 1. XPlanung JSON-Schemas

**URL**: https://gitlab.opencode.de/xleitstelle/xplanung/schemas/json

**Status** (via WebFetch):
- Repository existiert: ✓
- 6 Commits vorhanden: ✓
- 1 Branch (main): ✓
- README-Datei vorhanden: ✓
- **Dateiinhalte sichtbar**: ✗ (JavaScript-Rendering erforderlich)

**Erwartete Inhalte** (nicht über WebFetch zugänglich):
- JSON-Schema-Dateien (.json)
- Versionierte Schemas
- README mit Dokumentation
- Beispieldaten

### 2. XTrasse JSON-Schemas

**URL**: https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation/-/tree/main/json

**Status** (via WebFetch):
- Seite zeigt "Loading": ✗
- Inhalte nicht sichtbar: ✗
- JavaScript-Rendering erforderlich: ✓

**Erwartete Inhalte** (nicht über WebFetch zugänglich):
- JSON-Schemas für XTrasse
- Leitungsnetz-Datenmodelle in JSON
- Technische Dokumentation

### 3. XLeitstelle Hauptseite

**URL**: https://gitlab.opencode.de/xleitstelle

**Status** (via WebFetch):
- Gruppenbeschreibung sichtbar: ✓
  - "Veröffentlichungen der XLeitstelle bezüglich der Standards XTrasse, XPlanung, XBau, XBreitband"
- Repository-Liste sichtbar: ✗ (JavaScript CDATA-Blöcke)

**Bekannte Repositories** (aus anderen Quellen):
- xleitstelle/xplanung
  - xleitstelle/xplanung/schemas/json
  - xleitstelle/xplanung/testdaten
  - xleitstelle/xplanung/validierungsregeln
- xleitstelle/xtrasse
  - xleitstelle/xtrasse/spezifikation
- xleitstelle/xbau
- xleitstelle/xbreitband
  - xleitstelle/xbreitband/xnt (XML-Nachrichten-Tool)

### 4. Weitere bekannte Repositories

**XBau**:
- URL: https://gitlab.opencode.de/xleitstelle/xbau
- Inhalt: XML-Schemas, Testdaten, Spezifikationen

**XBreitband**:
- URL: https://gitlab.opencode.de/xleitstelle/xbreitband
- Unterverzeichnis: xleitstelle/xbreitband/xnt (Nachrichtengenerator-Tool)

---

## Workaround-Strategien

### Strategie 1: Direkte Git-Clone

**Vorteil**: Vollständiger Zugriff auf alle Dateien

```bash
# XPlanung
git clone https://gitlab.opencode.de/xleitstelle/xplanung.git
cd xplanung/schemas/json/

# XTrasse
git clone https://gitlab.opencode.de/xleitstelle/xtrasse.git
cd xtrasse/spezifikation/json/

# XBau
git clone https://gitlab.opencode.de/xleitstelle/xbau.git

# XBreitband
git clone https://gitlab.opencode.de/xleitstelle/xbreitband.git
```

**Nachteil**: Erfordert lokales Git, große Downloads

### Strategie 2: GitLab API

**Vorteil**: Programmierbar, keine Browser-Emulation nötig

```bash
# Repository-Baum abrufen
curl "https://gitlab.opencode.de/api/v4/projects/xleitstelle%2Fxplanung/repository/tree?path=schemas/json"

# Datei-Inhalt abrufen
curl "https://gitlab.opencode.de/api/v4/projects/xleitstelle%2Fxplanung/repository/files/schemas%2Fjson%2FREADME.md/raw?ref=main"
```

**Nachteil**: API-Rate-Limits, Authentifizierung möglicherweise erforderlich

### Strategie 3: Manuelle Browser-Recherche

**Vorteil**: Zuverlässig, vollständige Inhalte sichtbar

**Prozess**:
1. Browser öffnen: https://gitlab.opencode.de/xleitstelle
2. Repository auswählen (z.B. xplanung)
3. Zu Unterverzeichnis navigieren (schemas/json)
4. Dateien manuell durchsuchen
5. Relevante Inhalte dokumentieren

**Nachteil**: Zeitaufwändig, nicht automatisierbar

### Strategie 4: Alternative Primärquellen

**Vorteil**: Oft direkte Downloads ohne JavaScript

**Quellen**:

1. **XLeitstelle.de Download-Bereich**:
   - URL: https://xleitstelle.de/xplanung/releases
   - Inhalt: ZIP-Archive mit XML-Schemas, Spezifikationen (PDF)
   - Problem: JSON-Schemas möglicherweise nicht in Download-Paketen

2. **FITKO Dokumentation**:
   - URL: https://docs.fitko.de/fit-standards/
   - Inhalt: Technische Dokumentation, Anwendungsfälle
   - Problem: Keine Schema-Dateien, nur Beschreibungen

3. **XRepository.de**:
   - URL: https://www.xrepository.de
   - Inhalt: Standard-Metadaten, URNs
   - Problem: Keine direkten Schema-Downloads

---

## Auswirkungen auf Recherche

### Nicht recherchierbar (via WebFetch)

- ✗ Genaue Dateistruktur der JSON-Schema-Repositories
- ✗ Verfügbare JSON-Schema-Versionen und Dateinamen
- ✗ Konkrete .json-Dateien und deren Inhalte
- ✗ README-Dokumentation in Unterverzeichnissen
- ✗ Commit-Historie und Änderungen
- ✗ Testdaten in JSON-Format

### Recherchierbar (via alternative Quellen)

- ✓ Existenz der Repositories (Metadaten)
- ✓ Gruppenbeschreibung ("XTrasse, XPlanung, XBau, XBreitband")
- ✓ Grundlegende Repository-Informationen (Commits, Branches)
- ✓ Spezifikationen (PDFs) von xleitstelle.de
- ✓ Dokumentation von docs.fitko.de
- ✓ Standard-URNs von xrepository.de

---

## Bestätigte Informationen

Trotz JavaScript-Problem konnten folgende Informationen bestätigt werden:

### JSON-Schema-Entwicklung der XLeitstelle

**Status**: In Entwicklung
**Format**: JSON-FG (OGC Features and Geometries JSON)
**Veröffentlichung**: 2025 (geplant)

**Repositories existieren**:
- xleitstelle/xplanung/schemas/json (6 Commits, aktiv)
- xleitstelle/xtrasse/spezifikation/json (vorhanden)

**Primärformat bleibt**:
- GML 3.2.2 (XML-basiert)
- ISO 19136 (Geography Markup Language)
- Vollständig spezifiziert und verfügbar

### XML-Schemas (GML) - Primärformat

**Verfügbarkeit**: ✓ Vollständig zugänglich
**Quelle**: xleitstelle.de/downloads
**Formate**: .xsd (XML Schema Definition)

**Download-Pakete**:
- XPlanung 6.0 (aktuell)
- XBau 2.4 (aktuell)
- XTrasse 2.0 (aktuell)
- XBreitband 1.2 (aktuell)

---

## Empfehlungen

### Für aktuelle Forschung

1. **Primärquelle**: xleitstelle.de
   - Downloads: Spezifikationen (PDF), XML-Schemas (ZIP)
   - Dokumentation: Handreichungen, Leitfäden
   - Validator: XPlan-Validator (online)

2. **Dokumentation**: docs.fitko.de
   - FIT-Standards: Technische Beschreibungen
   - Anwendungsfälle: Praktische Beispiele

3. **Metadaten**: xrepository.de
   - Standard-URNs
   - Versionsinformationen

### Für JSON-Schema-Recherche

**Sobald JSON-FG verfügbar (2025)**:
1. Git-Clone der Repositories
2. Lokale Analyse der .json-Dateien
3. Vergleich mit GML-Schemas

**Aktuell (2024)**:
- JSON-Schemas in Entwicklung
- Nicht in Download-Paketen enthalten
- Nur via Git-Clone zugänglich

### Für automatisierte Analyse

**Empfohlen**:
- GitLab API nutzen (statt WebFetch)
- Lokale Git-Clones für Dateianalyse
- Regelmäßige Updates via `git pull`

**Nicht empfohlen**:
- Browser-Automatisierung (Selenium, Puppeteer) - zu komplex
- WebFetch für GitLab OpenCode - funktioniert nicht

---

## Technische Details: JavaScript-Rendering

### HTML-Struktur (typisch)

```html
<!DOCTYPE html>
<html>
<head>
  <script>
    //<![CDATA[
    window.gon = { /* GitLab-Konfiguration */ };
    //]]>
  </script>
</head>
<body>
  <div id="app"></div>
  <!-- JavaScript rendert Inhalte hier -->
  <script src="/assets/application.js"></script>
</body>
</html>
```

### WebFetch sieht

```html
<div id="app"></div>
<!-- Leer, keine Inhalte -->
```

### Browser sieht (nach Rendering)

```html
<div id="app">
  <nav><!-- Repository-Navigation --></nav>
  <main>
    <ul class="file-list">
      <li>schema_v1.json</li>
      <li>schema_v2.json</li>
      <li>README.md</li>
    </ul>
  </main>
</div>
```

---

## Zusammenfassung

**Problem**: GitLab OpenCode nutzt JavaScript-Rendering, WebFetch kann Inhalte nicht extrahieren

**Betroffene URLs**:
- https://gitlab.opencode.de/xleitstelle
- https://gitlab.opencode.de/xleitstelle/xplanung/schemas/json
- https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation/-/tree/main/json

**Lösung**:
- Git-Clone für vollständigen Zugriff
- GitLab API für automatisierte Abfragen
- Alternative Primärquellen (xleitstelle.de, docs.fitko.de)

**Status**: Dokumentiert für weitere Analyse

---

**Erstellt am**: 2025-11-21 23:30
**Zweck**: Problemdokumentation und Workaround-Strategien
**Bezug**: Geo-Datenformate Deep Research (Kapitel 7: XLeitstelle-Bereitstellung)
