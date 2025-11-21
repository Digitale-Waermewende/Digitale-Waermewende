---
layout: default
title: "Planungstypen in Deutschland"
parent: XPlanung
grand_parent: Standards
nav_exclude: true
permalink: /standards/xplanung/planungstypen-deutschland/
---

# Planungstypen in Deutschland: Bebauungsplan, Flächennutzungsplan, Landschaftsplan und Raumordnung

**Erfassungsdatum**: 2025-11-21
**Typ**: Rechtsquellen-Recherche
**Umfang**: Vier zentrale Planungstypen mit gesetzlichen Grundlagen
**Primärquellen**: Baugesetzbuch (BauGB), Bundesnaturschutzgesetz (BNatSchG), Raumordnungsgesetz (ROG)

---

## Überblick

Dieses Dokument erklärt die vier zentralen Planungstypen des deutschen Planungsrechts, die in XPlanung digital modelliert werden. Die Erklärungen basieren auf den jeweiligen gesetzlichen Grundlagen und stellen die hierarchische Beziehung zwischen den Planungsebenen dar.

```
Planungshierarchie (von übergeordnet zu konkret):

Bundesebene/Landesebene:  Raumordnung (ROG)
                                 ↓
Kommunale Ebene:          Flächennutzungsplan (§5 BauGB) - vorbereitend
                                 ↓
Kommunale Ebene:          Bebauungsplan (§8-10 BauGB) - verbindlich

Parallel (Naturschutz):   Landschaftsplan (§8-12 BNatSchG)
```

---

## 1. Bebauungsplan (Verbindlicher Bauleitplan)

### 1.1 Definition

Der **Bebauungsplan** ist ein Instrument der räumlichen Planung in Deutschland, das rechtsverbindliche Festsetzungen für die städtebauliche Ordnung eines Teils des Gemeindegebiets enthält und die Grundlage für weitere zur Durchführung des Baugesetzbuchs (BauGB) erforderliche Maßnahmen bildet.

**Rechtscharakter**: Verbindlicher Bauleitplan mit Satzungscharakter (§10 BauGB)

### 1.2 Rechtliche Grundlage

**Baugesetzbuch (BauGB)**
- **Vollständiger Titel**: Baugesetzbuch in der Fassung der Bekanntmachung vom 3. November 2017 (BGBl. I S. 3634)
- **Primärquelle**: [BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/)
- **Inkrafttreten**: 1. Juli 1987 (Ablösung des Bundesbaugesetzes BBauG)

### 1.3 Zentrale Vorschriften

#### § 8 BauGB - Zweck des Bebauungsplans

> Der Bebauungsplan enthält die rechtsverbindlichen Festsetzungen für die städtebauliche Ordnung. Er bildet die Grundlage für weitere, zur Durchführung dieses Gesetzbuchs erforderliche Maßnahmen.

**Quelle**: [§8 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__8.html)

#### § 9 BauGB - Inhalt des Bebauungsplans

§9 Abs. 1 BauGB listet die zulässigen Festsetzungen auf, darunter:
- Nr. 1: Art und Maß der baulichen Nutzung
- Nr. 12: Versorgungsflächen (Gas, Fernwärme, Elektrizität, Wasser, Abwasser)
- Nr. 20: Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft

**Quelle**: [§9 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__9.html)

#### § 10 BauGB - Beschluss, Genehmigung und Inkrafttreten des Bebauungsplans

> Die Gemeinde beschließt den Bebauungsplan als Satzung.

**Quelle**: [§10 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__10.html)

#### § 30 BauGB - Zulässigkeit von Vorhaben im Geltungsbereich eines Bebauungsplans

> Im Geltungsbereich eines Bebauungsplans, der allein oder gemeinsam mit sonstigen baurechtlichen Vorschriften mindestens Festsetzungen über die Art und das Maß der baulichen Nutzung, die überbaubaren Grundstücksflächen und die örtlichen Verkehrsflächen enthält (qualifizierter Bebauungsplan), ist ein Vorhaben zulässig, wenn es diesen Festsetzungen nicht widerspricht und die Erschließung gesichert ist.

**Quelle**: [§30 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__30.html)

### 1.4 Relevanz für Wärmeplanung

- **§9 Abs. 1 Nr. 12 BauGB**: Festsetzung von Versorgungsflächen für **Fernwärme**
- **§9 Abs. 1 Nr. 23 lit. b BauGB**: Gebiete, in denen bei der Errichtung von Gebäuden bestimmte bauliche Maßnahmen für den Einsatz erneuerbarer Energien getroffen werden müssen
- **Komplementär zu WPG §27**: Berücksichtigungspflicht von Wärmeplänen in der Bauleitplanung

**XPlanung-Modellierung**: BP_Fernwaerme, BP_VerEntsorgung

---

## 2. Flächennutzungsplan (Vorbereitender Bauleitplan)

### 2.1 Definition

Der **Flächennutzungsplan** (FNP) ist ein vorbereitender Bauleitplan, der für das gesamte Gemeindegebiet die sich aus der beabsichtigten städtebaulichen Entwicklung ergebende Art der Bodennutzung nach den voraussehbaren Bedürfnissen der Gemeinde in den Grundzügen darstellt.

**Rechtscharakter**: Vorbereitender Bauleitplan ohne unmittelbare Rechtswirkung gegenüber Bürgern

### 2.2 Rechtliche Grundlage

**Baugesetzbuch (BauGB)**

### 2.3 Zentrale Vorschriften

#### § 5 BauGB - Inhalt des Flächennutzungsplans

> (1) Im Flächennutzungsplan ist für das ganze Gemeindegebiet die sich aus der beabsichtigten städtebaulichen Entwicklung ergebende Art der Bodennutzung nach den voraussehbaren Bedürfnissen der Gemeinde in den Grundzügen darzustellen.

**Quelle**: [§5 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__5.html)

**Darstellungsmöglichkeiten nach §5 Abs. 2 BauGB** (Auswahl):
- Nr. 1: Bauflächen nach der allgemeinen Art ihrer baulichen Nutzung (Wohnbauflächen, gemischte Bauflächen, gewerbliche Bauflächen)
- Nr. 2: Flächen für den Gemeinbedarf sowie für Sport- und Spielanlagen
- Nr. 4: Flächen für Versorgungsanlagen (Elektrizität, Gas, Fernwärme, Wasser, Abwasser)
- Nr. 7: Flächen für die Landwirtschaft und Wald
- Nr. 10: Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft

#### § 8 Abs. 2 BauGB - Verhältnis zum Bebauungsplan

> Bebauungspläne sind aus dem Flächennutzungsplan zu entwickeln.

**Quelle**: [§8 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__8.html)

### 2.4 Entwicklungsgebot

Der Flächennutzungsplan ist die **Grundlage für Bebauungspläne** (§8 Abs. 2 BauGB). Bebauungspläne müssen aus dem FNP "entwickelt" werden, was bedeutet, dass sie mit den Darstellungen des FNP übereinstimmen oder im Einklang mit der Planungskonzeption stehen müssen.

### 2.5 Rechtswirkung

Der Flächennutzungsplan entfaltet gegenüber Bürgern **keine unmittelbare rechtliche Wirkung**, sondern bindet nur die Gemeinde selbst und andere öffentliche Planungsträger (§5 Abs. 1 S. 2 BauGB: "Bindung öffentlicher Planungsträger").

**XPlanung-Modellierung**: FP_Ver_und_Entsorgung, FP_Gemeinbedarf_Spiel_Sportanlagen

---

## 3. Landschaftsplan (Naturschutzplanung)

### 3.1 Definition

Der **Landschaftsplan** konkretisiert die Ziele des Naturschutzes und der Landschaftspflege für den jeweiligen Planungsraum und zeigt die Erfordernisse und Maßnahmen zur Verwirklichung dieser Ziele für Planungen und Verwaltungsverfahren auf.

**Rechtscharakter**: Fachplanung des Naturschutzes, eigenständig oder integriert in Bauleitplanung (Grünordnungsplan)

### 3.2 Rechtliche Grundlage

**Bundesnaturschutzgesetz (BNatSchG)**
- **Vollständiger Titel**: Gesetz über Naturschutz und Landschaftspflege (Bundesnaturschutzgesetz - BNatSchG)
- **Fassung**: Vom 29. Juli 2009 (BGBl. I S. 2542), zuletzt geändert durch Artikel 3 des Gesetzes vom 8. Dezember 2022 (BGBl. I S. 2240)
- **Primärquelle**: [BNatSchG - Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/)

### 3.3 Zentrale Vorschriften

#### § 8 BNatSchG - Aufgaben und Inhalte der Landschaftsplanung

> Die Landschaftsplanung hat die Aufgabe, die Ziele des Naturschutzes und der Landschaftspflege für den jeweiligen Planungsraum zu konkretisieren und die Erfordernisse und Maßnahmen zur Verwirklichung dieser Ziele auch für die Planungen und Verwaltungsverfahren aufzuzeigen, deren Entscheidungen sich auf Natur und Landschaft im Planungsraum auswirken können.

**Quelle**: [§8 BNatSchG - Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/__8.html)

#### § 9 BNatSchG - Landschaftsprogramme und Landschaftsrahmenpläne

Landschaftsplanung auf Landesebene:
- **Landschaftsprogramme**: Für das gesamte Gebiet eines Landes (§9 Abs. 1 BNatSchG)
- **Landschaftsrahmenpläne**: Für Teilräume des Landes (§9 Abs. 3 BNatSchG)

**Quelle**: [§9 BNatSchG - Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/__9.html)

#### § 11 BNatSchG - Landschaftspläne

> (1) Die in den Landschaftsrahmenplänen für Teile des Planungsraums konkretisierten Ziele, Erfordernisse und Maßnahmen des Naturschutzes und der Landschaftspflege werden auf der Grundlage der Landschaftsrahmenpläne für die Gebiete der Gemeinden in Landschaftsplänen dargestellt.

**Quelle**: [§11 BNatSchG - Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/__11.html)

#### § 11 Abs. 3 BNatSchG - Verhältnis zur Bauleitplanung

> Die Pläne sollen Angaben enthalten über
> 1. den vorhandenen und den zu erwartenden Zustand von Natur und Landschaft,
> 2. die konkretisierten Ziele des Naturschutzes und der Landschaftspflege,
> 3. die Beurteilung des vorhandenen und zu erwartenden Zustands von Natur und Landschaft nach Maßgabe dieser Ziele einschließlich der sich daraus ergebenden Konflikte,
> 4. die Erfordernisse und Maßnahmen zur Umsetzung der konkretisierten Ziele des Naturschutzes und der Landschaftspflege, insbesondere
>    - Schutz bestimmter Teile von Natur und Landschaft im Sinne des Kapitels 4 sowie der Biotope, Lebensgemeinschaften und Lebensstätten der Tiere und Pflanzen wild lebender Arten,
>    - Wiederherstellung beeinträchtigter Bereiche von Natur und Landschaft,
>    - Vermeidung, Ausgleich oder Minderung von Beeinträchtigungen von Natur und Landschaft.

### 3.4 Hierarchie der Landschaftsplanung

```
Bundesebene:                    (keine eigenen Landschaftspläne)
                                       ↓
Landesebene:              Landschaftsprogramm (§9 Abs. 1 BNatSchG)
                                       ↓
Regionalebene:            Landschaftsrahmenplan (§9 Abs. 3 BNatSchG)
                                       ↓
Kommunale Ebene:          Landschaftsplan (§11 BNatSchG)
                                       ↓
Integration in Bauleitplanung: Grünordnungsplan
```

### 3.5 Relevanz für Wärmeplanung

- **Ausschlussgebiete**: Naturschutzgebiete, Landschaftsschutzgebiete als Restriktionen für Wärmenetzausbau
- **Biotopvernetzung**: Berücksichtigung bei Trassenplanung für Fernwärmeleitungen
- **Komplementär zu WPG**: Berücksichtigung von Schutzgebieten bei der Wärmeplanung

**XPlanung-Modellierung**: LP_Flaechenschutzobjekte, LP_SchutzPflegeEntwicklung
**Wärmeplan-Modellierung**: WP_Ausschlussgebiet (mit Schutzgrund Naturschutz)

---

## 4. Raumordnung (Übergeordnete Planung)

### 4.1 Definition

**Raumordnung** ist die zusammenfassende, übergeordnete Planung und Ordnung des Raums. Sie dient dazu, flächenmäßig umfangreiche Gebietseinheiten planmäßig zu ordnen, zu entwickeln und zu sichern, um sicherzustellen, dass der vorhandene Lebensraum optimal genutzt werden kann.

**Rechtscharakter**: Öffentliche Aufgabe von Bund und Ländern (§1 ROG)

### 4.2 Rechtliche Grundlage

**Raumordnungsgesetz (ROG)**
- **Vollständiger Titel**: Raumordnungsgesetz vom 22. Dezember 2008 (BGBl. I S. 2986)
- **Primärquelle**: [ROG - Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/)
- **Letzte Änderung**: Artikel 1 des Gesetzes vom 22. März 2023 (BGBl. 2023 I Nr. 88)

### 4.3 Zentrale Vorschriften

#### § 1 ROG - Aufgabe und Leitvorstellung der Raumordnung

> (1) Der Gesamtraum der Bundesrepublik Deutschland und seine Teilräume sind durch Raumordnungspläne, durch raumordnerische Zusammenarbeit und durch Abstimmung raumbedeutsamer Planungen und Maßnahmen zu entwickeln, zu ordnen und zu sichern. Dabei sind
> 1. unterschiedliche Anforderungen an den Raum aufeinander abzustimmen und die auf der jeweiligen Planungsebene auftretenden Konflikte auszugleichen,
> 2. Vorsorge für einzelne Nutzungen und Funktionen des Raums zu treffen.

**Quelle**: [§1 ROG - Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/__1.html)

#### § 2 ROG - Grundsätze der Raumordnung

§2 ROG enthält 15 zentrale Grundsätze, darunter:
- Abs. 2 Nr. 4: Klimaschutz und Klimaanpassung
- Abs. 2 Nr. 5: Nachhaltige Energieversorgung, insbesondere durch zunehmende Nutzung erneuerbarer Energien

**Quelle**: [§2 ROG - Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/__2.html)

#### § 7 ROG - Allgemeine Vorschriften über Raumordnungspläne

> (1) Die Grundsätze der Raumordnung sind nach Maßgabe der Leitvorstellung und des Gegenstromprinzips (§ 1) für den Gesamtraum und die Teilräume durch Raumordnungspläne zu konkretisieren.

**Quelle**: [§7 ROG - Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/__7.html)

#### § 8 ROG - Raumordnungspläne

**Bundesebene**:
- Raumordnungsplan des Bundes (§17 ROG) für die ausschließliche Wirtschaftszone (AWZ)

**Landesebene**:
- Landesentwicklungspläne oder Landesraumentwicklungsprogramme
- Regionalpläne für Teilräume der Länder

**Quelle**: [§8 ROG - Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/__8.html)

### 4.4 Hierarchie der Raumordnung

```
Bundesebene:              Raumordnungsplan des Bundes (§17 ROG)
                          - Nur für ausschließliche Wirtschaftszone
                                     ↓
Landesebene:              Landesentwicklungsplan / Landesraumentwicklungsprogramm
                          - Für gesamtes Landesgebiet (§8 Abs. 1 Nr. 1 ROG)
                                     ↓
Regionalebene:            Regionalplan / Regionaler Raumordnungsplan
                          - Für Teilräume des Landes (§8 Abs. 1 Nr. 2 ROG)
                                     ↓
Kommunale Ebene:          Bauleitplanung (FNP, B-Plan) nach BauGB
                          - Anpassungspflicht an Ziele der Raumordnung (§1 Abs. 4 BauGB)
```

### 4.5 Gegenstromprinzip

§1 Abs. 3 ROG formuliert das **Gegenstromprinzip**:

> Bei der Aufstellung der Raumordnungspläne sind die Rahmenbedingungen der Siedlungs- und sonstigen Raumnutzung, die wirtschaftlichen, sozialen, ökologischen und kulturellen Erfordernisse sowie die natürlichen Gegebenheiten des Gesamtraums und seiner Teilräume zu berücksichtigen. Die Entwicklung, Ordnung und Sicherung der Teilräume soll sich in die Gegebenheiten und Erfordernisse des Gesamtraums einfügen; die Entwicklung, Ordnung und Sicherung des Gesamtraums soll die Gegebenheiten und Erfordernisse seiner Teilräume berücksichtigen (**Gegenstromprinzip**).

### 4.6 Relevanz für Wärmeplanung

- **§2 Abs. 2 Nr. 4 ROG**: Klimaschutz und Klimaanpassung als Grundsatz der Raumordnung
- **§2 Abs. 2 Nr. 5 ROG**: Nachhaltige Energieversorgung, insbesondere durch zunehmende Nutzung erneuerbarer Energien
- **Regionalplanung**: Festlegung von Eignungsgebieten für Windenergie, Geothermie, Biomasse
- **Anpassungspflicht**: Kommunale Wärmepläne müssen Ziele der Raumordnung beachten

**XPlanung-Modellierung**: RP_Energieversorgung, RP_Freiraumstruktur

---

## 5. Hierarchie und Verhältnis der Planungstypen

### 5.1 Rangfolge der Planungsebenen

```
Übergeordnet:    Raumordnung (ROG) - Bund/Länder/Regionen
                        ↓ (Anpassungspflicht)
Kommunal:        Flächennutzungsplan (§5 BauGB) - vorbereitend
                        ↓ (Entwicklungsgebot)
Kommunal:        Bebauungsplan (§8-10 BauGB) - verbindlich

Parallel:        Landschaftsplan (§8-12 BNatSchG) - Naturschutzfachplanung
                        ↓ (Integration möglich)
                 Grünordnungsplan (Teil des Bebauungsplans)
```

### 5.2 Rechtliche Bindungen

| Planungstyp | Rechtscharakter | Bindungswirkung | Rechtsnorm |
|-------------|-----------------|-----------------|------------|
| **Raumordnungsplan** | Verwaltungsinterner Plan | Bindung öffentlicher Planungsträger (§4 ROG) | ROG §7-8 |
| **Flächennutzungsplan** | Vorbereitender Bauleitplan | Bindung öffentlicher Planungsträger (§7 BauGB) | BauGB §5 |
| **Bebauungsplan** | Satzung | Bindung aller Rechtssubjekte (§30 BauGB) | BauGB §8-10 |
| **Landschaftsplan** | Fachplanung Naturschutz | Je nach Landesrecht unterschiedlich | BNatSchG §11 |

### 5.3 Anpassungspflicht der Bauleitplanung

**§1 Abs. 4 BauGB** - Anpassung an Ziele der Raumordnung:

> Die Bauleitpläne sind den Zielen der Raumordnung anzupassen.

**Quelle**: [§1 BauGB - Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/__1.html)

Dies bedeutet: Kommunale Bauleitpläne (FNP und B-Plan) müssen die Ziele der Raumordnung beachten und dürfen ihnen nicht widersprechen.

---

## 6. Digitale Modellierung in XPlanung

### 6.1 XPlanung-Packages nach Planungstyp

| Planungstyp | XPlanung-Package | Präfix | Anzahl Objektarten |
|-------------|------------------|--------|---------------------|
| **Bebauungsplan** | Bebauungsplan/ | BP_* | 100+ |
| **Flächennutzungsplan** | Flaechennutzungsplan/ | FP_* | 80+ |
| **Landschaftsplan** | Landschaftsplan/ | LP_* | 40+ |
| **Raumordnungsplan** | Raumordnungsplan/ | RP_* | 50+ |

**Quelle**: [Objektartenkatalog-Vergleich: XPlanung, Wärmeplan und XTrasse](2025-11-21_Objektartenkatalog-Vergleich-XPlanung-Waermeplan-XTrasse.md)

### 6.2 Gemeinsame Basisklassen

Alle vier Planungstypen erben von der gemeinsamen Basisklasse **XP_Objekt** (XP_Basisobjekte):

```
XP_Objekt (abstract)
├── BP_Objekt (Bebauungsplan) → BP_* Fachobjekte
├── FP_Objekt (Flächennutzungsplan) → FP_* Fachobjekte
├── LP_Objekt (Landschaftsplan) → LP_* Fachobjekte
└── RP_Objekt (Raumordnungsplan) → RP_* Fachobjekte
```

### 6.3 XPlanung-Objektartenkatalog

- **XPlanung 6.1**: [Katalog-ID 447](https://xleitstelle.de/downloads/catalogues/447/)
- **Offizielle Seite**: [XLeitstelle Objektartenkatalog](https://xleitstelle.de/releases/objektartenkatalog_6_0)

---

## 7. Relevanz für die Wärmeplanung

### 7.1 Integration von Wärmeplanung in Planungsebenen

| Planungstyp | Wärmewende-Relevanz | Rechtsgrundlage |
|-------------|---------------------|-----------------|
| **Raumordnung** | Festlegung von Eignungsgebieten für erneuerbare Energien (Geothermie, Biomasse) | ROG §2 Abs. 2 Nr. 4-5 |
| **Flächennutzungsplan** | Darstellung von Versorgungsflächen für Fernwärme (§5 Abs. 2 Nr. 4 BauGB) | BauGB §5 |
| **Bebauungsplan** | Festsetzung von Fernwärme-Versorgungsgebieten (§9 Abs. 1 Nr. 12, 23 BauGB) | BauGB §9, WPG §27 |
| **Landschaftsplan** | Ausschlussgebiete für Wärmenetzausbau (Naturschutzgebiete) | BNatSchG §11 |

### 7.2 Wärmeplanungsgesetz (WPG) und Bauleitplanung

**§27 WPG - Berücksichtigungspflicht in der Bauleitplanung**:

Die Gemeinden haben bei der Aufstellung, Änderung, Ergänzung und Aufhebung von Bauleitplänen die **Wärmepläne zu berücksichtigen**.

**Quelle**: [Wärmeplanungsgesetz](../../gesetze/WPG/index.md)

### 7.3 Komplementarität der Standards

```
Rechtliche Ebene:        BauGB §9        →  BP_Fernwaerme (XPlanung)
                              ↓
Energieplanung:         WPG §23-26      →  WP_Fernwaermenetz (Wärmeplan)
                              ↓
Technische Umsetzung:   TKG, EnWG       →  BST_Fernwaerme (XTrasse)
```

**Siehe auch**: [Objektartenkatalog-Vergleich](2025-11-21_Objektartenkatalog-Vergleich-XPlanung-Waermeplan-XTrasse.md) - Fernwärme-Dreiklang (Sektion 5.5.1)

---

## 8. Zusammenfassung

### 8.1 Kernunterschiede

| Aspekt | Bebauungsplan | Flächennutzungsplan | Landschaftsplan | Raumordnung |
|--------|---------------|---------------------|-----------------|-------------|
| **Rechtsgrundlage** | BauGB §8-10 | BauGB §5 | BNatSchG §8-12 | ROG |
| **Planungsebene** | Kommunal | Kommunal | Kommunal/Regional/Land | Bund/Land/Regional |
| **Rechtscharakter** | Satzung (verbindlich) | Verwaltungsinterner Plan | Fachplanung | Verwaltungsinterner Plan |
| **Maßstab** | 1:500 - 1:2.000 | 1:5.000 - 1:50.000 | Variabel | 1:100.000 - 1:500.000 |
| **Detaillierungsgrad** | Parzellenscharf | Grobkörnig | Mittel | Grobkörnig |
| **Bindungswirkung** | Alle Rechtssubjekte | Nur öffentl. Planungsträger | Je nach Landesrecht | Nur öffentl. Planungsträger |

### 8.2 Hierarchische Beziehungen

1. **Raumordnung** gibt Ziele vor → Anpassungspflicht für FNP/B-Plan (§1 Abs. 4 BauGB)
2. **Flächennutzungsplan** ist Grundlage → Entwicklungsgebot für B-Plan (§8 Abs. 2 BauGB)
3. **Bebauungsplan** setzt verbindlich um → Direkte Rechtswirkung (§30 BauGB)
4. **Landschaftsplan** läuft parallel → Integration über Grünordnungsplan möglich

---

## 9. Primärquellen und weiterführende Links

### 9.1 Gesetzestexte (Primärquellen)

- **[Baugesetzbuch (BauGB)](https://www.gesetze-im-internet.de/bbaug/)** - Gesetze im Internet, Bundesministerium der Justiz
- **[Bundesnaturschutzgesetz (BNatSchG)](https://www.gesetze-im-internet.de/bnatschg_2009/)** - Gesetze im Internet
- **[Raumordnungsgesetz (ROG)](https://www.gesetze-im-internet.de/rog_2008/)** - Gesetze im Internet

### 9.2 Verwandte Dokumente

**Standards**:
- [XPlanung Hauptdokument](index.md) - Überblick und Relevanz für Wärmeplanung
- [Objektartenkatalog-Vergleich](2025-11-21_Objektartenkatalog-Vergleich-XPlanung-Waermeplan-XTrasse.md) - Detaillierte Analyse der digitalen Modellierung

**Gesetze**:
- [Wärmeplanungsgesetz (WPG)](../../gesetze/WPG/index.md) - §27 Berücksichtigungspflicht in Bauleitplanung
- [Baugesetzbuch (BauGB)](../../gesetze/BauGB/index.md) - Gesetzliche Basis für Bauleitplanung

**Stakeholder**:
- [XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md) - Verwaltende Organisation für XPlanung

---

⚠️ **Rechtlicher Hinweis:**
Diese Zusammenfassung dient ausschließlich informativen Zwecken und ersetzt keine qualifizierte Rechtsberatung. Für rechtsverbindliche Auskünfte konsultieren Sie bitte einen Rechtsanwalt oder die zuständige Behörde.

**Primärquellen:**
- [Baugesetzbuch (BauGB) auf Gesetze im Internet](https://www.gesetze-im-internet.de/bbaug/)
- [Bundesnaturschutzgesetz (BNatSchG) auf Gesetze im Internet](https://www.gesetze-im-internet.de/bnatschg_2009/)
- [Raumordnungsgesetz (ROG) auf Gesetze im Internet](https://www.gesetze-im-internet.de/rog_2008/)
