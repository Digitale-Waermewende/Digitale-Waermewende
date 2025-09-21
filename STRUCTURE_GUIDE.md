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

## Offene Fragen zur Diskussion

1. Sollen PDF-Originale auch gespeichert werden oder nur Links?
2. Wie detailliert sollen Gesetzestexte aufbereitet werden?
3. Brauchen wir eine Versionierung für sich ändernde Dokumente?
4. Soll es Tags/Labels für Themen geben (z.B. #Förderung, #Datenformat)?

---
*Dieses Dokument ist ein lebender Entwurf und wird kontinuierlich angepasst.*