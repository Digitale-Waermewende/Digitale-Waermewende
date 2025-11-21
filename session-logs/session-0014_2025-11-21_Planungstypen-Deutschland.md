---
layout: default
title: "Session 0014"
parent: Session Log
nav_exclude: true
permalink: /session-log/session-0014/
---

# Session 0014 - 2025-11-21 - Planungstypen in Deutschland dokumentiert

**Datum**: 2025-11-21
**Commits**: [819df37](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/819df37), [9b676e8](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/9b676e8)

### User-Eingaben

#### 1. Front-Matter-Problem
```
In der Hauptnavigation tauchen nach wie die Dateien "Deep Research Report: Geo-Datenformate"
"XBreitband Deep Research Report" warum? Ich dachte wir hätten das über Frontmatter gelöst.
```

#### 2. Planungstypen-Erklärung
```
Erkläre die Begriffe Bebauungsplan, Flächennutzungsplan, Landschaftsplan und Raumordnung.
Referenziere dazu die Gesetze bzw. andere vertrauenswürdige Primärquellen. Lege die
Ergebnisse der Recherche in Digitale-Waermewende\standards\XPlanung ab und verlinke das
Dokument in die Index-Datei commit, push und session-Log.
```

### Ergebnisse

**Commits**:
- [819df37](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/819df37) - Fix: Front-Matter für Geo-Datenformate und XBreitband Research-Dokumente
- [9b676e8](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/9b676e8) - Planungstypen in Deutschland dokumentiert

**Neues Dokument**:
- [Planungstypen in Deutschland](/standards/xplanung/planungstypen-deutschland/) (448 Zeilen)

**Aktualisierte Seiten**:
- [XPlanung](/standards/xplanung/) - Link zum Planungstypen-Dokument hinzugefügt
- Geo-Datenformate Research - Front-Matter ergänzt
- XBreitband Prozess-Messaging - Front-Matter ergänzt

### Entscheidungen

**Front-Matter-Problem behoben**:
- **Ursache**: Geo-Datenformate und XBreitband Research-Dokumente hatten kein Front-Matter
- **Symptom**: Beide erschienen als Top-Level-Dokumente in Hauptnavigation
- **Lösung**: Front-Matter mit `nav_exclude: true` für beide Dateien hinzugefügt
- **Ergebnis**: Dokumente nur noch über Index-Seiten erreichbar (Level 4)

**Planungstypen-Dokumentation erstellt**:

*1. Bebauungsplan (BauGB §8-10)*:
- Verbindlicher Bauleitplan mit Satzungscharakter (§10 BauGB)
- §8: Rechtsverbindliche Festsetzungen für städtebauliche Ordnung
- §9: Inhalt (Art/Maß der Nutzung, Versorgungsflächen für Fernwärme)
- §30: Zulässigkeit von Vorhaben (qualifizierter B-Plan)
- **XPlanung-Modellierung**: BP_* (100+ Objekte)
- **Wärmewende-Relevanz**: §9 Abs. 1 Nr. 12 (Fernwärme), Nr. 23 lit. b (erneuerbare Energien)

*2. Flächennutzungsplan (BauGB §5)*:
- Vorbereitender Bauleitplan für gesamtes Gemeindegebiet
- §5: Darstellung der beabsichtigten Bodennutzung in Grundzügen
- §8 Abs. 2: Entwicklungsgebot (B-Pläne aus FNP zu entwickeln)
- **Rechtswirkung**: Keine unmittelbare Bindung für Bürger, nur für öffentliche Planungsträger
- **XPlanung-Modellierung**: FP_* (80+ Objekte)
- **Wärmewende-Relevanz**: §5 Abs. 2 Nr. 4 (Versorgungsflächen für Fernwärme)

*3. Landschaftsplan (BNatSchG §8-12)*:
- Naturschutzfachplanung auf kommunaler Ebene
- §8: Konkretisierung der Ziele des Naturschutzes für Planungsraum
- §11: Landschaftspläne auf Grundlage von Landschaftsrahmenplänen
- **Hierarchie**: Landschaftsprogramm (Land) → Landschaftsrahmenplan (Region) → Landschaftsplan (Kommune)
- **XPlanung-Modellierung**: LP_* (40+ Objekte)
- **Wärmewende-Relevanz**: Ausschlussgebiete für Wärmenetzausbau (Naturschutzgebiete)

*4. Raumordnung (ROG)*:
- Übergeordnete Planung von Bund, Ländern und Regionen
- §1: Gesamtraum ordnen, entwickeln, sichern (Gegenstromprinzip)
- §2 Abs. 2 Nr. 4: Klimaschutz und Klimaanpassung als Grundsatz
- §2 Abs. 2 Nr. 5: Nachhaltige Energieversorgung (erneuerbare Energien)
- **Hierarchie**: Bund (AWZ) → Land (Landesentwicklungsplan) → Region (Regionalplan)
- **XPlanung-Modellierung**: RP_* (50+ Objekte)
- **Wärmewende-Relevanz**: Eignungsgebiete für Geothermie, Biomasse

**Planungshierarchie dokumentiert**:

```
Übergeordnet:    Raumordnung (ROG) - Bund/Länder/Regionen
                        ↓ (Anpassungspflicht §1 Abs. 4 BauGB)
Kommunal:        Flächennutzungsplan (§5 BauGB) - vorbereitend
                        ↓ (Entwicklungsgebot §8 Abs. 2 BauGB)
Kommunal:        Bebauungsplan (§8-10 BauGB) - verbindlich

Parallel:        Landschaftsplan (§8-12 BNatSchG) - Naturschutz
                        ↓ (Integration möglich)
                 Grünordnungsplan (Teil des B-Plans)
```

**Rechtliche Bindungen dokumentiert**:
- **Raumordnungsplan**: Bindung öffentlicher Planungsträger (§4 ROG)
- **Flächennutzungsplan**: Bindung öffentlicher Planungsträger (§7 BauGB)
- **Bebauungsplan**: Bindung aller Rechtssubjekte (§30 BauGB)
- **Landschaftsplan**: Je nach Landesrecht unterschiedlich

**Relevanz für Wärmeplanung herausgearbeitet**:
- **Raumordnung**: Festlegung von Eignungsgebieten für erneuerbare Energien
- **FNP**: Darstellung von Versorgungsflächen für Fernwärme
- **B-Plan**: Festsetzung von Fernwärme-Versorgungsgebieten (§9 Abs. 1 Nr. 12 BauGB)
- **Landschaftsplan**: Ausschlussgebiete für Wärmenetzausbau
- **WPG §27**: Berücksichtigungspflicht von Wärmeplänen in Bauleitplanung

**Komplementarität zu XPlanung-Standards**:
```
Rechtliche Ebene:        BauGB §9        →  BP_Fernwaerme (XPlanung)
                              ↓
Energieplanung:         WPG §23-26      →  WP_Fernwaermenetz (Wärmeplan)
                              ↓
Technische Umsetzung:   TKG, EnWG       →  BST_Fernwaerme (XTrasse)
```

### Technische Details

**Dokumentstruktur (9 Hauptsektionen)**:
1. Überblick und Planungshierarchie
2. Bebauungsplan (BauGB §8-10) - Definition, Vorschriften, Relevanz
3. Flächennutzungsplan (BauGB §5) - Definition, Entwicklungsgebot, Rechtswirkung
4. Landschaftsplan (BNatSchG §8-12) - Definition, Hierarchie, Integration
5. Raumordnung (ROG) - Definition, Grundsätze, Gegenstromprinzip
6. Hierarchie und Verhältnis der Planungstypen
7. Digitale Modellierung in XPlanung (BP_*, FP_*, LP_*, RP_*)
8. Relevanz für Wärmeplanung (WPG §27, Fernwärme-Festsetzungen)
9. Primärquellen und weiterführende Links

**Primärquellen-Referenzen**:
- **BauGB**: [Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/)
- **BNatSchG**: [Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/)
- **ROG**: [Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/)
- Direkte Links zu einzelnen Paragraphen (§8 BauGB, §5 BauGB, §11 BNatSchG, etc.)

**WebSearch-Quellen verwendet**:
- Gesetze im Internet (Bundesministerium der Justiz)
- dejure.org (Gesetzeskommentierung)
- Wikipedia (Hintergrundinfo)
- Bayerisches Staatsministerium (Fachinformationen)

**Vergleichstabellen erstellt**:
- Kernunterschiede (Rechtsgrundlage, Planungsebene, Rechtscharakter, Maßstab, Bindungswirkung)
- Relevanz für Wärmeplanung (alle vier Planungstypen)
- Digitale Modellierung in XPlanung (Package-Namen, Präfixe, Objektanzahl)

**Rechtlicher Disclaimer**:
Am Ende des Dokuments hinzugefügt: Hinweis auf Informationscharakter, keine Rechtsberatung, Primärquellen-Links

### Lessons Learned

**Front-Matter-Checkliste bewährt sich**:
- CLAUDE.md mit Front-Matter-Reminder hat diesmal funktioniert
- Problem lag bei älteren Dokumenten aus früheren Sessions
- Systematisches Prüfen von Altbeständen notwendig

**WebSearch für Rechtsquellen geeignet**:
- Gesetze im Internet als Primärquelle direkt auffindbar
- dejure.org für Paragraphen-Kommentierung hilfreich
- Kombinierter Ansatz (Gesetzestext + Fachliteratur) erfolgreich

**Hierarchische Darstellung wichtig**:
- ASCII-Diagramme für Planungshierarchie
- Vergleichstabellen für Übersichtlichkeit
- Klare Abgrenzung zwischen Planungsebenen

**Integration mit bestehendem Wissen**:
- Verknüpfung zu Objektartenkatalog-Vergleich
- Bezug zu WPG §27 (Berücksichtigungspflicht)
- Fernwärme-Dreiklang als Querverbindung

---

