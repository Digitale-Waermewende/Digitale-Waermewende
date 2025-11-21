---
layout: default
title: XBreitband
parent: Standards
nav_order: 4
has_children: false
permalink: /standards/xbreitband/
---

# XBreitband - Nachrichtenstandard für Breitbandausbau

XBreitband ist der föderale IT-Standard für die Datenkommunikation im Breitbandausbau. Als Nachrichtenstandard regelt XBreitband den strukturierten Datenaustausch zwischen Telekommunikationsunternehmen, Kommunen und Behörden.

## Was ist XBreitband?

**Definition**: Nachrichtenstandard für digitale Verwaltungsverfahren im Breitbandausbau

**Status und Entwicklung**:
- **Seit 2021 verbindlich** (IT-Planungsrat-Beschluss 2021/40)
- **Aktuelle Version**: XBreitband Release 1.2 (28. Mai 2024)
- **Status**: Regelbetrieb (operational)
- **Technische Basis**: XÖV 3.0, XBau Kernmodul, XML-basiert

**Hauptanwendungsfall**: Zustimmungsverfahren nach **§127 TKG** (Nutzung öffentlicher Wege)

## Prozessmodell: 3-Phasen-Modell

XBreitband bildet einen strukturierten 3-Phasen-Prozess ab:

### Phase 1: Antragstellung
- **Akteure**: Telekommunikationsunternehmen → Straßenbaubehörde
- **Inhalte**: Zustimmungsantrag mit Bauvorhaben, Trassenplan (XTrasse), Dokumente
- **Nachrichten**: Zustimmungsantrag

### Phase 2: Vollständigkeitsprüfung & TöB-Beteiligung
- **Frist**: 1 Monat für Vollständigkeitsprüfung
- **Varianten**:
  - **B2G**: Telekommunikationsunternehmen holt Stellungnahmen selbst
  - **G2G**: Behörde koordiniert Beteiligung der Träger öffentlicher Belange
- **Nachrichten**: Beteiligungen, Stellungnahmen, Leitungsanfragen, Änderungsbedarfe

### Phase 3: Bescheiderteilung
- **Frist**: 3 Monate (+ 1 Monat Verlängerung möglich)
- **Fiktionswirkung**: Zustimmung gilt als erteilt nach Fristablauf ohne Bescheid
- **Nachrichten**: Bescheid mit möglichen Nebenbestimmungen

**Zusätzlich**: Baubeginns- und Baufertigstellungsanzeigen

## Messaging-Modell: 11 Nachrichten für §127 TKG

XBreitband definiert **11 spezialisierte Nachrichtentypen**:

1. **Zustimmungsantrag** - Initialer Antrag des TKU
2. **Beteiligungsnachricht** - Einbindung von TöB
3. **Stellungnahme** - Rückmeldungen der TöB
4. **Änderungsbedarf** - Anforderung von Nachbesserungen
5. **Bescheid** - Behördliche Entscheidung
6. **Leitungsanfrage** - Abfrage bestehender Leitungen
7. **Leitungsauskunft** - Auskunft über Bestandsleitungen
8. **Baubeginnsanzeige** - Meldung des Baubeginns
9. **Baufertigstellungsanzeige** - Meldung der Fertigstellung
10. **Informationsnachricht** - Allgemeine Kommunikation
11. *[weiterer Nachrichtentyp in Spezifikation]*

**Generische Nachrichten** (aus XBau Kernmodul):
- Eingangsbestätigung
- Rückweisung/Ablehnung

## Akteure und Rollen

### Antragsteller (Telekommunikationsunternehmen)
- Erstellen Anträge mit vollständigen Unterlagen
- Optional: Eigenständige TöB-Beteiligung (B2G-Variante)
- Melden Baubeginn und Fertigstellung

### Straßenbaubehörde
- Zuständigkeits- und Vollständigkeitsprüfung
- Koordinierung TöB-Beteiligung (G2G-Variante)
- Erteilung Bescheid (gebundene Entscheidung nach §127 TKG)

### Träger öffentlicher Belange (TöB)
- Naturschutz, Wasserwirtschaft, Denkmalschutz, Straßenverkehr, etc.
- Abgabe strukturierter Stellungnahmen
- Äußerung zu Bedenken und Auflagen

## Verhältnis zu XTrasse: Enge technische Integration

**XBreitband** (Nachrichtenstandard) und **XTrasse** (Datenmodell) sind **eng verzahnt**:

- XTrasse-Trassenplan ist **integraler Bestandteil** der Antragsnachricht
- XTrasse-Pläne werden **direkt in XBreitband-Nachrichten integriert**
- **Direkte strukturelle Bezüge** im Datenmodell
- XTrasse basiert auf **XPlanung-Grundstruktur** (gemeinsame Basisklassen)

**XTrasse liefert**:
- Genaue Trassenverläufe (GML-Format)
- Technische Details (Schutzrohre, Kabel, Verteiler)
- Tiefenlage und Kreuzungen
- GIS-kompatible Geodaten

**XBreitband nutzt**:
- XTrasse-Daten als Antragsbestandteil
- Referenzen zu XTrasse-Objekten
- Koordinaten und Trassenpläne für Bescheide

**Grund für enge Integration**:
- Tiefbau: Trassen sind **kontinuierliche lineare Infrastrukturen** über viele Grundstücke
- Leitungsverlegung erfordert **präzise Georeferenzierung** jedes Trassenmeters
- **Exakte 3D-Leitungsverläufe** als zentrale Datengrundlage erforderlich

## Relevanz für Wärmenetze

Obwohl XBreitband primär für Telekommunikation entwickelt wurde, sind **Prozess- und Messaging-Modell** relevant für zukünftige Standards zur Wärmenetz-Verlegung:

### Übertragbare Konzepte
- **Koordinierte Verlegung** (§146 TKG): Mehrere Leitungssparten gleichzeitig
- **Trassenplanung**: XTrasse-Integration als Vorbild
- **TöB-Beteiligung**: Strukturierte Stellungnahmen
- **Fiktionswirkung**: Automatische Genehmigung bei Fristablauf

### Synergien
- Gemeinsame Trassennutzung (Fernwärme + Glasfaser)
- Koordinierte Tiefbaumaßnahmen
- Einheitliche Prozesse für Leitungsinfrastruktur

## Verwaltende Organisation

**[XLeitstelle Planen und Bauen](../../stakeholder/bund/xleitstelle/)**
- Entwicklung und Pflege der XBreitband-Spezifikation
- Bereitstellung von Tools (XNT - XBreitband Nachrichtengenerator)
- Dokumentation und Support

## Spezifikation und Dokumentation

- **Spezifikation 1.2**: [XBreitband 1.2 (PDF)](https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf)
- **FITKO-Dokumentation**: [docs.fitko.de/fit-standards/xbreitband](https://docs.fitko.de/fit-standards/xbreitband/)
- **XRepository**: [XBau Tiefbau Standard](https://www.xrepository.de/details/urn:xoev-de:it-plr:standard:xbau-tiefbau)
- **GitLab OpenCode**: [XNT-Tool](https://gitlab.opencode.de/xleitstelle/xbreitband/xnt)
- **XLeitstelle**: [xleitstelle.de](https://xleitstelle.de)

## Dokumente in diesem Bereich

### Prozess- und Messaging-Modell Research

**[XBreitband Prozess- und Messaging-Modell - Deep Research](2025-11-21_XBreitband-Prozess-Messaging-Modell_Research.md)**
Umfassende Analyse des XBreitband-Standards mit detaillierter Beschreibung des 3-Phasen-Prozessmodells (Antragstellung, TöB-Beteiligung, Bescheiderteilung) und des Messaging-Modells mit 11 Nachrichtentypen. Dokumentiert Primärquellen, technische Details (XÖV 3.0, XBau Kernmodul), Akteure und Rollen sowie das enge Verhältnis zu XTrasse. Basis für Vergleich mit XBau.

### Vergleich mit XBau

**XBau vs. XBreitband - Systematischer Vergleich** (siehe [XBau Research](../xbau/2025-11-21_XBau-Prozess-Messaging-Modell-Vergleich-XBreitband_Research.md))

Der detaillierte Vergleich zwischen XBau-Hochbau und XBreitband zeigt fundamentale Unterschiede in der Datenmodell-Integration:

**Gemeinsamkeiten**:
- Gemeinsames **XBau-Kernmodul 1.2** mit identischen generischen Nachrichten (1120, 1121, 1141, 1142, Rückweisung)
- **XÖV 3.0 Framework** und XÖV-Bibliothek 2022-12-15 als technische Basis
- Ähnliche **Prozessstruktur**: Antrag → Prüfung → TöB-Beteiligung → Bescheid
- Beide IT-Planungsrat-Standards mit rechtlicher Verbindlichkeit
- **XLeitstelle Hamburg** als gemeinsamer Betreiber

**Unterschiede**:
- **Nachrichtenanzahl**: XBreitband 11 Typen vs. XBau 100+ Typen
- **Rechtliche Grundlage**: §127 TKG (Bundesgesetz) vs. Musterbauordnung/16 Landesbauordnungen
- **Länderspezifik**: Gering vs. Hoch (16 unterschiedliche Bundesländer)
- **Anwendungsbereich**: Tiefbau (Leitungsverlegung) vs. Hochbau (Gebäude)
- **Grundstücksbezug**: Viele Grundstücke vs. Ein/wenige Grundstücke

**Hauptunterschied - Datenmodell-Integration**:

*XBreitband ↔ XTrasse:* **ENGE KOPPLUNG**
- XTrasse-Trassenplan ist **integraler Bestandteil** der Antragsnachricht
- **Direkte strukturelle Bezüge** im Datenmodell
- XTrasse basiert auf XPlanung-Grundstruktur
- **Grund**: Trassen sind kontinuierliche lineare Infrastrukturen, die präzise 3D-Georeferenzierung erfordern

*XBau ↔ XPlanung:* **LOSE KOPPLUNG**
- XPlanung-Bebauungspläne als **externe Prüfgrundlage**
- **Keine direkten XML-Referenzen** zwischen Standards
- Integration über GIS-Systeme
- **Grund**: Gebäude sind diskrete Objekte auf definierten Grundstücken, abstrakte bauordnungsrechtliche Prüfung ausreichend

## Verwandte Bereiche

### Rechtliche Grundlagen
- **[Telekommunikationsgesetz (TKG)](../../gesetze/TKG/)** - Gesetzliche Basis für XBreitband
  - [§127 TKG](../../gesetze/TKG/index.md#127---zustimmung-zur-nutzung-öffentlicher-wege) - Zustimmungsverfahren (Hauptanwendungsfall)
  - [§146 TKG](../../gesetze/TKG/index.md#146---mitverlegung) - Koordinierte Verlegung
- **[IT-Staatsvertrag](../../gesetze/it-staatsvertrag/)** - IT-PLR-Beschluss 2021/40 (XBreitband verbindlich)

### Organisation und Standards
- **Governance**: [IT-Planungsrat](../../stakeholder/bund/it-planungsrat/) - Beschließt Standards (Beschluss 2021/40)
- **Betrieb**: [XLeitstelle](../../stakeholder/bund/xleitstelle/) - Entwicklung und Pflege XBreitband
- **Datenmodell**: [XTrasse](../xtrasse/) - Leitungsdatenmodell (eng verzahnt mit XBreitband)
- **Vergleich**: [XBau](../xbau/) - Hochbau-Standard mit XBau-Kernmodul als gemeinsamer Basis
- **Weitere Standards**: [XPlanung](../xplanung/), [ALKIS](../alkis/)
