# Konzept: Gesetze-Ordner

## Übersicht

Zentraler Anlaufpunkt für relevante Gesetze zur digitalen Wärmewende mit strikter Trennung zwischen Original-Gesetzestexten und Sekundärmaterial.

## Zielsetzung

1. **Schneller Zugang** zu Original-Gesetzestexten über [Gesetze im Internet](https://www.gesetze-im-internet.de/)
2. **Klare Quellenangaben** bei allen Zitaten und Zusammenfassungen
3. **Transparente Autorschaft** bei AI-generierten Inhalten
4. **Deep-Links** zu einzelnen Paragraphen
5. **Konsistente Zitat-Kennzeichnung**

## Ordnerstruktur

```
gesetze/
├── index.md                          # Hauptübersicht aller Gesetze
├── WPG/
│   ├── index.md                      # Wärmeplanungsgesetz Übersicht
│   ├── wpg-§3-begriffe.md           # AI-Analyse zu §3
│   ├── wpg-§13-inhalte.md           # AI-Analyse zu §13
│   └── zusammenfassung.md            # Gesamtübersicht (AI)
├── BauGB/
│   ├── index.md                      # Baugesetzbuch Übersicht
│   ├── baugb-§9-bauplanung.md       # Einzelparagraph-Analyse
│   ├── xplanung-relevanz.md          # Thematische Übersicht
│   └── xplanung/                     # Optional: Unterordner bei vielen Paragraphen
│       ├── baugb-§9-bauplanung.md
│       └── baugb-§11-vertrag.md
├── TKG/
│   ├── index.md                      # Telekommunikationsgesetz Übersicht
│   └── xtrasse-xbreitband.md         # Relevanz für XTrasse/XBreitband
├── GEG/
│   ├── index.md                      # Gebäude-Energiegesetz Übersicht
│   └── wpg-schnittstellen.md         # Schnittstellen zum WPG
└── templates/
    ├── gesetz-index-template.md      # Vorlage für Gesetzes-Übersicht
    └── paragraph-analyse-template.md  # Vorlage für Paragraphen-Analyse
```

**Strukturprinzip:**
- **Standard:** Alle Dateien direkt im Gesetzes-Ordner (flache Hierarchie)
- **Bei Bedarf:** Thematische Unterordner wenn >10 Paragraphen-Analysen
- **Vorteil:** Übersichtlich, kann organisch wachsen

## Dateinamen-Konvention

### Gesetzes-Übersicht (index.md)
- Format: `gesetze/[ABKÜRZUNG]/index.md`
- Beispiel: `gesetze/WPG/index.md`

### Paragraphen-Analysen
- Format: `[abkürzung]-§[nummer]-[kurztitel].md`
- Beispiele:
  - `wpg-§3-begriffe.md`
  - `wpg-§13-inhalte.md`
  - `baugb-§9-bauplanung.md`

### Thematische Analysen
- Format: `[thema]-relevanz.md` oder `[thema]-schnittstellen.md`
- Beispiele:
  - `xplanung-relevanz.md`
  - `wpg-schnittstellen.md`

## Front Matter Standards

### Gesetzes-Index (index.md)
```yaml
---
layout: default
title: [Gesetzesname ausgeschrieben]
parent: Gesetze
nav_order: [Nummer]
has_children: true
permalink: /gesetze/[abkürzung]/
---
```

### Paragraphen-Analyse (direkt im Gesetzes-Ordner)
```yaml
---
layout: default
title: "§[Nummer] [Kurztitel]"
parent: [Gesetzesname]
grand_parent: Gesetze
nav_exclude: true  # Optional, bei vielen Paragraphen
permalink: /gesetze/[abkürzung]/paragraph-[nummer]/
---
```

### Paragraphen-Analyse (in thematischem Unterordner)
```yaml
---
layout: default
title: "§[Nummer] [Kurztitel]"
parent: [Unterordner-Name]
grand_parent: [Gesetzesname]
nav_exclude: true
permalink: /gesetze/[abkürzung]/[unterordner]/paragraph-[nummer]/
---
```

## Content-Struktur für Gesetzes-Index

### Template für `index.md`

```markdown
---
layout: default
title: [Gesetzesname ausgeschrieben]
parent: Gesetze
nav_order: [Nummer]
has_children: true
permalink: /gesetze/[abkürzung]/
---

# [Gesetzesname] ([ABKÜRZUNG])

## Original-Gesetzestext

🔗 **Primärquelle (Gesetze im Internet):**
- [Volltext [ABKÜRZUNG]](https://www.gesetze-im-internet.de/[pfad]/)
- Stand: [Datum der letzten Änderung laut Website]

## Relevanz für Digitale Wärmewende

[1-2 Sätze zur Bedeutung des Gesetzes]

## Wichtige Paragraphen

### §[Nummer] - [Titel]
- 🔗 [Link zum Paragraphen](https://www.gesetze-im-internet.de/[pfad]/__[nummer].html)
- [1 Satz zur Relevanz]
- [AI-Analyse vorhanden]([dateiname].md)

### §[Nummer] - [Titel]
- 🔗 [Link zum Paragraphen](https://www.gesetze-im-internet.de/[pfad]/__[nummer].html)
- [1 Satz zur Relevanz]

## Querverweise

**Verwandte Gesetze:**
- [Link zu anderem Gesetz im Repository]

**Verwandte Standards:**
- [Link zu Standards-Dokumentation]

**Stakeholder:**
- [Link zu relevanten Stakeholdern]

---

*Primärquelle: Bundesministerium der Justiz - [Gesetze im Internet](https://www.gesetze-im-internet.de/)*
```

## Content-Struktur für Paragraphen-Analyse

### Template für Paragraphen-Dokumente

```markdown
---
layout: default
title: "§[Nummer] [Kurztitel]"
parent: [Gesetzesname]
grand_parent: Gesetze
nav_exclude: true
permalink: /gesetze/[abkürzung]/paragraph-[nummer]/
---

# §[Nummer] [Paragraphen-Titel] - [ABKÜRZUNG]

## Original-Gesetzestext

🔗 **Primärquelle:**
- [§[Nummer] [ABKÜRZUNG] auf Gesetze im Internet](https://www.gesetze-im-internet.de/[pfad]/__[nummer].html)

---

## Gesetzeszitat

> **§[Nummer] [Titel]**
>
> (1) [Vollständiger Wortlaut Absatz 1]
>
> (2) [Vollständiger Wortlaut Absatz 2]
>
> [weitere Absätze...]

**Quelle:** [§[Nummer] [ABKÜRZUNG]](https://www.gesetze-im-internet.de/[pfad]/__[nummer].html), Gesetze im Internet

---

## AI-Analyse

⚠️ **Hinweis:** Die folgende Analyse wurde von Claude (Anthropic) erstellt und stellt keine Rechtsberatung dar.

**Erstellt:** [Datum]
**AI-Modell:** Claude [Version] (Anthropic)

### Zusammenfassung

[Absatz 1: Kernaussage des Paragraphen]

[Absatz 2: Wichtige Details]

### Relevanz für [spezifischer Kontext]

[Erklärung der praktischen Bedeutung]

### Schlüsselbegriffe

**[Begriff 1]**
- Definition laut Absatz ([Nummer])
- Bedeutung: [Erklärung]

**[Begriff 2]**
- Definition laut Absatz ([Nummer])
- Bedeutung: [Erklärung]

### Wichtige Absätze im Detail

#### Absatz (1): [Thema]

**Zitat:**
> [Relevanter Teil des Absatzes]

**Erläuterung:** [AI-Analyse des Absatzes]

#### Absatz (2): [Thema]

**Zitat:**
> [Relevanter Teil des Absatzes]

**Erläuterung:** [AI-Analyse des Absatzes]

### Querverweise

**Innerhalb des Gesetzes:**
- [§[Nummer] [Titel]](link) - [Bezug]

**Zu anderen Gesetzen:**
- [Gesetz §Nummer](link) - [Bezug]

### Praktische Anwendung

[Beispiele oder Erklärung der praktischen Umsetzung]

---

## Weiterführende Informationen

**Im Repository:**
- [Link zu verwandten Dokumenten]

**Externe Quellen:**
- [Link zu Kommentaren, falls vorhanden]
- [Link zu Anwendungshinweisen]

---

⚠️ **Rechtlicher Hinweis:**
Diese AI-Analyse dient ausschließlich informativen Zwecken und ersetzt keine qualifizierte Rechtsberatung. Für rechtsverbindliche Auskünfte konsultieren Sie bitte einen Rechtsanwalt oder die zuständige Behörde.

**Primärquelle:** [Link zum Originalparagraphen auf Gesetze im Internet]
```

## Kennzeichnungs-Standards

### 1. Original-Gesetzeszitate

**Immer verwenden:**
```markdown
> **§[Nummer] [Titel]**
>
> [Vollständiger Wortlaut]

**Quelle:** [§[Nummer] [ABKÜRZUNG]](URL), Gesetze im Internet
```

**Eigenschaften:**
- Blockquote-Format (>)
- Fettgedruckte Paragraphen-Nummer
- Vollständige Quellenangabe mit Link

### 2. AI-generierte Inhalte

**Immer mit Disclaimer beginnen:**
```markdown
## AI-Analyse

⚠️ **Hinweis:** Die folgende Analyse wurde von Claude (Anthropic) erstellt und stellt keine Rechtsberatung dar.

**Erstellt:** [Datum]
**AI-Modell:** Claude [Version] (Anthropic)
```

### 3. Teilzitate innerhalb von Analysen

**Format:**
```markdown
**Zitat:**
> [Relevanter Textausschnitt]

**Erläuterung:** [AI-Analyse]
```

### 4. Rechtlicher Disclaimer

**Am Ende jedes Analyse-Dokuments:**
```markdown
⚠️ **Rechtlicher Hinweis:**
Diese AI-Analyse dient ausschließlich informativen Zwecken und ersetzt keine qualifizierte Rechtsberatung. Für rechtsverbindliche Auskünfte konsultieren Sie bitte einen Rechtsanwalt oder die zuständige Behörde.
```

## Deep-Link-Struktur

### Gesetze im Internet URL-Schema

**Basis-URL:** `https://www.gesetze-im-internet.de/`

**Gesamt-Gesetz:**
```
https://www.gesetze-im-internet.de/[gesetz-id]/
```

**Einzelner Paragraph:**
```
https://www.gesetze-im-internet.de/[gesetz-id]/__[nummer].html
```

**Beispiele:**

| Gesetz | Gesetz-ID | Beispiel-URL |
|--------|-----------|--------------|
| WPG | wpg | https://www.gesetze-im-internet.de/wpg/ |
| WPG §3 | wpg | https://www.gesetze-im-internet.de/wpg/__3.html |
| BauGB | bbaug | https://www.gesetze-im-internet.de/bbaug/ |
| BauGB §9 | bbaug | https://www.gesetze-im-internet.de/bbaug/__9.html |
| GEG | geg | https://www.gesetze-im-internet.de/geg/ |
| TKG | tkg_2021 | https://www.gesetze-im-internet.de/tkg_2021/ |

**Link-Format im Markdown:**
```markdown
- [§3 WPG - Begriffsbestimmungen](https://www.gesetze-im-internet.de/wpg/__3.html)
```

## Haupt-Index: gesetze/index.md

```markdown
---
layout: default
title: Gesetze
nav_order: 3
has_children: true
permalink: /gesetze/
---

# Gesetze zur Digitalen Wärmewende

Zentrale Übersicht relevanter Gesetze mit Links zu Original-Texten und AI-gestützten Analysen.

## Primärquelle

🔗 **[Gesetze im Internet](https://www.gesetze-im-internet.de/)** - Bundesministerium der Justiz

Alle Gesetzestexte verlinken auf die offizielle Plattform des Bundesministeriums der Justiz.

## Gesetze

### [Wärmeplanungsgesetz (WPG)](WPG/)
Bundesgesetz zur Wärmeplanung und Dekarbonisierung der Wärmeversorgung.

🔗 [Original-Gesetzestext WPG](https://www.gesetze-im-internet.de/wpg/)

**Schlüssel-Paragraphen:**
- [§3 - Begriffsbestimmungen](https://www.gesetze-im-internet.de/wpg/__3.html)
- [§13 - Inhalt der Wärmeplanung](https://www.gesetze-im-internet.de/wpg/__13.html)
- [§26 - Bereitstellung von Daten](https://www.gesetze-im-internet.de/wpg/__26.html)

### [Baugesetzbuch (BauGB)](BauGB/)
Relevanz für XPlanung und digitale Bauleitplanung.

🔗 [Original-Gesetzestext BauGB](https://www.gesetze-im-internet.de/bbaug/)

**Für XPlanung relevant:**
- [§9 - Inhalt des Bebauungsplans](https://www.gesetze-im-internet.de/bbaug/__9.html)
- [§11 - Städtebaulicher Vertrag](https://www.gesetze-im-internet.de/bbaug/__11.html)

### [Gebäudeenergiegesetz (GEG)](GEG/)
Energetische Anforderungen an Gebäude, Schnittstellen zur Wärmeplanung.

🔗 [Original-Gesetzestext GEG](https://www.gesetze-im-internet.de/geg/)

### [Telekommunikationsgesetz (TKG)](TKG/)
Relevanz für XTrasse und XBreitband (Infrastrukturplanung).

🔗 [Original-Gesetzestext TKG](https://www.gesetze-im-internet.de/tkg_2021/)

## Hinweise zur Nutzung

### Original-Gesetzestexte
Alle direkten Links führen zu **[Gesetze im Internet](https://www.gesetze-im-internet.de/)**, der offiziellen Publikationsplattform des Bundesministeriums der Justiz.

### AI-Analysen
Analysen und Zusammenfassungen sind als solche gekennzeichnet und wurden von Claude (Anthropic) erstellt. Sie dienen ausschließlich informativen Zwecken.

### Aktualität
Die Gesetzestexte auf "Gesetze im Internet" werden zeitnah aktualisiert. Der Stand ist jeweils auf der verlinkten Seite angegeben.

---

⚠️ **Rechtlicher Hinweis:**
Dieses Repository dient informativen Zwecken und ersetzt keine qualifizierte Rechtsberatung. Für rechtsverbindliche Auskünfte konsultieren Sie bitte einen Rechtsanwalt oder die zuständige Behörde.
```

## Workflow für neues Gesetz

### 1. Struktur anlegen
```bash
mkdir gesetze/[ABKÜRZUNG]
# Unterordner nur bei Bedarf (>10 Paragraphen)
```

### 2. Index erstellen
- Template `gesetz-index-template.md` kopieren
- Front Matter anpassen
- Gesetz-ID für URLs recherchieren
- Wichtigste Paragraphen identifizieren und verlinken

### 3. Haupt-Index aktualisieren
- Neues Gesetz in `gesetze/index.md` eintragen
- nav_order anpassen

### 4. Optional: Paragraphen-Analysen
- Dateien direkt im Gesetzes-Ordner anlegen
- Template `paragraph-analyse-template.md` verwenden
- AI-Disclaimer immer inkludieren
- Vollständiges Zitat vor Analyse einfügen
- Deep-Link zum Original setzen

### 5. Optional: Thematische Unterordner
- Nur bei >10 Paragraphen-Analysen
- Thematische Gruppierung (z.B. `xplanung/`, `waermeplanung/`)
- Eigene index.md für Unterordner erstellen

## Best Practices

### URLs
✅ **Immer:**
- Deep-Links zu Paragraphen verwenden
- Vollständige Quellenangabe mit Link
- Links auf "Gesetze im Internet" prüfen

❌ **Niemals:**
- Plain-Text URLs ohne Markdown-Link
- Sekundärquellen statt Original verlinken
- PDFs ohne Original-Link

### Zitate
✅ **Immer:**
- Blockquote-Format (>)
- Vollständige Quellenangabe
- Paragraph-Nummer und Titel angeben

❌ **Niemals:**
- Paraphrasen als Zitate kennzeichnen
- Zitate ohne Quellenangabe
- Gekürzte Zitate ohne Auslassungszeichen

### AI-Inhalte
✅ **Immer:**
- Deutlich als AI-generiert kennzeichnen
- Erstellungsdatum und Modell angeben
- Rechtlichen Disclaimer einfügen

❌ **Niemals:**
- AI-Analysen als Fachgutachten darstellen
- Disclaimer weglassen
- AI-Inhalt mit Original-Text vermischen ohne Kennzeichnung

### Navigation
✅ **Empfohlen:**
- `nav_exclude: true` bei vielen Paragraph-Analysen (>5)
- Wichtigste Paragraphen in Index-Datei verlinken
- Thematische Gruppierung bei vielen Gesetzen

## Integration mit bestehendem Repository

### Querverweise zu Standards
```markdown
**Verwandte Standards:**
- [XPlanung](../../standards/XPlanung/) - Digitale Bauleitplanung nach BauGB
- [XTrasse](../../standards/XTrasse/) - Infrastrukturplanung nach TKG
```

### Querverweise zu Stakeholdern
```markdown
**Zuständige Behörden:**
- [Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen](../../stakeholder/bund/BMWSB/)
```

### Querverweise aus anderen Bereichen
In `standards/XPlanung/index.md`:
```markdown
## Rechtliche Grundlagen
- [Baugesetzbuch (BauGB)](../../gesetze/BauGB/) - Gesetzliche Basis für Bauleitplanung
- [§9 BauGB - Inhalt des Bebauungsplans](../../gesetze/BauGB/baugb-§9-bauplanung.md)
```

## Qualitätskriterien

### Checkliste für Gesetzes-Index
- [ ] Front Matter vollständig
- [ ] Link zum Volltext auf "Gesetze im Internet"
- [ ] Stand des Gesetzes angegeben
- [ ] Mindestens 3 wichtige Paragraphen mit Deep-Links
- [ ] Kurze Relevanz-Erklärung (1-2 Sätze)
- [ ] Querverweise zu verwandten Gesetzen/Standards
- [ ] Rechtlicher Disclaimer am Ende

### Checkliste für Paragraphen-Analyse
- [ ] Front Matter mit nav_exclude
- [ ] Deep-Link zum Original-Paragraphen
- [ ] Vollständiges Zitat im Blockquote-Format
- [ ] Quellenangabe mit Link
- [ ] AI-Disclaimer mit Datum und Modell
- [ ] Klare Trennung zwischen Zitat und Analyse
- [ ] Rechtlicher Disclaimer am Ende
- [ ] Querverweise zu verwandten Paragraphen

## Wartung

### Regelmäßige Prüfungen
- **Quartalsweise:** Links zu "Gesetze im Internet" prüfen
- **Bei Gesetzesänderungen:** Stand aktualisieren, betroffene Analysen markieren
- **Jährlich:** Vollständigkeit der wichtigsten Gesetze prüfen

### Bei Gesetzesänderungen
1. Stand in index.md aktualisieren
2. Betroffene Paragraph-Analysen mit Hinweis versehen
3. Optional: Neue Analyse mit aktuellem Stand erstellen
4. Alte Analyse archivieren oder historischen Vermerk hinzufügen

---

**Version:** 1.0
**Erstellt:** 2025-11-20
**Status:** Konzept zur Diskussion
