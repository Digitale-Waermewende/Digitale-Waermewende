# Struktur-Leitfaden für das Repository Digitale Wärmewende

## Zweck dieses Dokuments
Dieses Dokument definiert, wie das Repository organisch wachsen soll und nach welchen Regeln Inhalte strukturiert werden.

## Grundprinzipien

1. **Quellenbasiert**: Primäre Quellen stehen im Mittelpunkt
2. **Evolutionär**: Die Struktur wächst mit den Inhalten
3. **Multi-Stakeholder**: Verschiedene Nutzergruppen (AI-Agenten, Entwickler, Domain-Experten)
4. **Nachvollziehbar**: Jede Quelle wird dokumentiert und eingeordnet

## Aktuelle Struktur (Minimal)

```
Digitale-Waermewende/
├── docs/                 # Projektdokumentation
├── stakeholder/         
│   ├── bund/            # Bundesebene
│   └── laender/         # Länderebene
└── standards/           # Datenstandards
```

## Regeln für Dokumentenorganisation

### 1. Quellenmanagement in `/stakeholder`

#### Dateinamenskonvention
```
YYYY-MM-DD_[Organisation]_[Titel].md
```
Beispiel: `2024-03-15_KWW-Halle_Leitfaden-Waermeplanung.md`

#### Dokumentstruktur für Quellen

Jede Quellendatei MUSS folgende Struktur haben:

```markdown
# [Vollständiger Titel]

## Metadaten
- **Organisation**: [Herausgeber]
- **Datum**: [Publikationsdatum]
- **Typ**: [Gesetz|Leitfaden|Standard|Bericht|...]
- **URL**: [Original-URL falls vorhanden]
- **Relevanz**: [Kurze Beschreibung warum wichtig]

## Zusammenfassung
[2-3 Sätze Kernaussage]

## Wichtige Punkte
- [Hauptpunkt 1]
- [Hauptpunkt 2]
- ...

## Verbindungen
- Bezug zu: [andere relevante Dokumente]
- Konflikt mit: [falls Widersprüche existieren]

## Originalzitate
> [Wichtige Passagen im Original]

## Notizen
[Eigene Anmerkungen, offene Fragen]
```

### 2. Bundesländer-Organisation

```
laender/
├── INDEX.md              # Übersicht alle Länder
├── bayern/
│   ├── README.md        # Zusammenfassung Bayern
│   └── [Quellen].md
├── nrw/
│   ├── README.md
│   └── [Quellen].md
└── ...
```

**Einschlusskriterium**: Nur Bundesländer mit eigenem Wärmekataster oder spezifischen Standards

### 3. Standards-Organisation

```
standards/
├── INDEX.md              # Übersicht aller Standards
├── xplanung/
│   └── README.md        # Was ist XPlanung, Relevanz für Wärmeplanung
├── inspire/
│   └── README.md
└── schnittstellen/
    └── README.md        # Dokumentation von APIs, Formaten
```

## Wachstumsplan

### Phase 1: Quellensammlung (aktuell)
- [ ] Bundesebene: Gesetze, KWW-Halle, XLeitstelle
- [ ] Standards: XPlanung, INSPIRE dokumentieren
- [ ] Erste Bundesländer mit Wärmekatastern

### Phase 2: Analyse & Vernetzung
- [ ] Verbindungen zwischen Quellen dokumentieren
- [ ] Widersprüche und Lücken identifizieren
- [ ] Stakeholder-Matrix erstellen

### Phase 3: Daten & Tools
- [ ] `/data` - Beispieldaten, Testdaten
- [ ] `/tools` - Konverter, Validatoren
- [ ] API-Dokumentation

### Phase 4: Community
- [ ] Best Practices
- [ ] Case Studies von Kommunen
- [ ] Kontaktverzeichnis

## Commit-Konventionen

```
feat: Neue Quelle oder Struktur hinzugefügt
docs: Dokumentation aktualisiert
fix: Fehlerkorrektur
refactor: Struktur reorganisiert
```

Beispiel: `feat: KWW-Halle Leitfaden 2024 hinzugefügt`

## Qualitätskriterien

- [ ] Jede Quelle hat vollständige Metadaten
- [ ] Datum der Quelle ist dokumentiert
- [ ] Original-URL ist angegeben (falls online)
- [ ] Relevanz für Wärmewende ist erklärt
- [ ] Verbindungen zu anderen Dokumenten sind notiert

## PDF-Dateien Workflow

### Grundsatz
PDF-Dateien von wichtigen Primärquellen werden lokal gespeichert und versioniert, um dauerhafte Verfügbarkeit zu gewährleisten.

### Wichtiger Hinweis zur PDF-Verarbeitung
**Stand 2025-09-21**: Eine direkte Online-Analyse von PDF-Dateien, die auf Webseiten verlinkt sind, ist mit Claude Code nicht möglich. Das WebFetch-Tool kann nur die HTML-Metadaten der verlinkenden Seite auslesen, nicht aber den PDF-Inhalt selbst. Daher ist ein lokaler Download der PDF-Datei zwingend erforderlich, bevor der Inhalt mit dem Read-Tool analysiert werden kann.

### 1. Download von PDFs
```bash
# Mit curl herunterladen (Windows-kompatibel)
curl -L -o "Dateiname.pdf" "https://url-zum-pdf.de/dokument.pdf"

# Alternativ mit vollständigen Parametern
curl -L -o "Dateiname.pdf" "https://url.de/dokument.pdf?__blob=publicationFile&v=3"
```

**Namenskonvention für PDFs:**
- Kurze, beschreibende Namen ohne Datum im Dateinamen
- Beispiele: `BBSR-Analysen-KOMPAKT-07-2024.pdf`, `Stakeholder-Dialog-Waermeplanung.pdf`

### 2. PDF mit Read-Tool lesen
```python
# Nach dem Download kann die PDF lokal gelesen werden
Read("E:/Documents/Coding/Digitale-Waermewende/stakeholder/bund/Dateiname.pdf")
```

### 3. Markdown-Dokumentation erstellen
Für jede wichtige PDF-Datei MUSS eine begleitende Markdown-Datei erstellt werden:

**Dateiname:** `YYYY-MM-DD_[Organisation]_[Titel].md`

**Inhalt muss enthalten:**
```markdown
## Metadaten
- **Lokal gespeichert**: stakeholder/bund/Dateiname.pdf (Dateigröße)
- **URL**: [Original-Download-URL]
- **ISBN/DOI**: [falls vorhanden]
```

### 4. Git Workflow für PDFs

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

### 5. Wichtige Hinweise

**PDF-Größenlimits:**
- GitHub erlaubt Dateien bis 100 MB
- Große PDFs (>50 MB) sollten nur als Link referenziert werden
- Alternative: Git LFS für große Dateien verwenden

**Versionierung:**
- Bei aktualisierten PDFs: Alte Version behalten, neue mit Versionsnummer
- Beispiel: `Leitfaden-v1.pdf` → `Leitfaden-v2.pdf`

**Datenschutz:**
- Keine internen/vertraulichen Dokumente hochladen
- Nur öffentlich verfügbare Quellen

### 6. Beispiel-Workflow

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

## Offene Fragen zur Diskussion

1. ~~Sollen PDF-Originale auch gespeichert werden oder nur Links?~~ → JA, wichtige PDFs lokal speichern
2. Wie detailliert sollen Gesetzestexte aufbereitet werden?
3. Brauchen wir eine Versionierung für sich ändernde Dokumente?
4. Soll es Tags/Labels für Themen geben (z.B. #Förderung, #Datenformat)?
5. Soll Git LFS für große PDFs (>50MB) eingerichtet werden?

---
*Dieses Dokument ist ein lebender Entwurf und wird kontinuierlich angepasst.*