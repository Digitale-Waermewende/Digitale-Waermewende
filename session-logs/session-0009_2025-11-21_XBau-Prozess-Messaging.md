---
layout: default
title: "Session 0009"
parent: Session Log
nav_exclude: true
permalink: /session-log/session-0009/
---

# Session 009 - 2025-11-21 20:20 - XBau Prozess-Messaging Analyse mit XBreitband-Vergleich

**Metadaten**: 2025-11-21 | 20:20 - 21:45 | Commits: [fbc6165](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/fbc6165)

### User-Eingaben

#### 1. Initiale Anfrage
```
Super Arbeit :-)), Bitte führe jetzt einen vergleichbaren Deep Research zum Prozess und
Messaging Modell bei XBau durch und nehme dabei Bezug auf das Daten-Modell ind XPlanung.
Arbeite dann die Gemeinsamkeiten und UNterschiede zwischen beiden Ansätzen heraus.
Erstelle am Ende ein Session-Log.
```

### Ergebnisse

**Commits**: [fbc6165](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/fbc6165)

**Neue Seiten**:
- [XBau Prozess- und Messaging-Modell Research](/standards/xbau/2025-11-21_XBau-Prozess-Messaging-Modell-Vergleich-XBreitband_Research.md)

**Geänderte Seiten**:
- [XBau](/standards/xbau/)

### Entscheidungen

**XBau Prozessmodell dokumentiert**:
- 5-Phasen-Modell: Antragstellung → Formelle/materielle Prüfung → TöB-Beteiligung → Bescheid → Genehmigungsfiktion
- Über 100 Nachrichtentypen für bauaufsichtliche Verfahren (XBau 2.3.1)
- 9 Verfahrenstypen abgedeckt (Baugenehmigung, Freistellung, Vorbescheid, Abweichung, Baulasten, etc.)
- Genehmigungsfiktion in einigen Bundesländern (Bayern, Berlin, Hamburg, etc.) nach 3 Monaten

**XBau Messaging-Modell analysiert**:
- Modularer Aufbau: XBau-Kernmodul 1.2 + Fachmodule (Hochbau 2.4, Tiefbau/XBreitband 1.2)
- Kernmodul enthält generische Nachrichten (1120, 1121, 1141, 1142, Rückweisung)
- XÖV 3.0 Framework, XÖV-Bibliothek 2022-12-15 als technische Basis
- Unabhängige Versionierung von Fachmodulen ermöglicht

**Bezüge zu XPlanung herausgearbeitet**:
- XBau und XPlanung sind **komplementäre Standards** mit **indirekter Integration**
- XPlanung-Bebauungspläne dienen als **externe Prüfgrundlage** für XBau-Bauanträge
- Automatische Prüfung: Bauantrag gegen Bebauungsplan (Abstandsflächen, Baugrenzen, Nutzungsarten)
- BIM-Integration ermöglicht: XPlanung-Höhendaten + XBau-BIM-Modelle → automatische/halbautomatische Genehmigung
- **Keine direkten XML-Referenzen** zwischen XBau-Nachrichten und XPlanung-Objekten

**Systematischer Vergleich XBau vs. XBreitband**:

*Gemeinsamkeiten identifiziert:*
- Gemeinsames XBau-Kernmodul 1.2 (identische generische Nachrichten)
- XÖV 3.0 Framework und XÖV-Bibliothek 2022-12-15
- Ähnliche Prozessstruktur: Antrag → Prüfung → TöB-Beteiligung → Bescheid
- Beide IT-Planungsrat-Standards mit rechtlicher Verbindlichkeit
- XLeitstelle Hamburg als gemeinsamer Betreiber
- Jährlicher Release-Rhythmus

*Unterschiede herausgearbeitet:*
- **Nachrichtenanzahl**: XBau 100+ vs. XBreitband 11
- **Rechtliche Grundlage**: Musterbauordnung/16 LBOs vs. Bundesgesetz (TKG)
- **Länderspezifik**: Hoch (16 Bundesländer) vs. Gering (Bundesgesetz)
- **Prozess-Komplexität**: Hoch (viele Verfahrensarten) vs. Mittel (fokussiert)
- **Anwendungsbereich**: Hochbau (Gebäude) vs. Tiefbau (Leitungen)
- **Grundstücksbezug**: Ein/wenige Grundstücke vs. Viele Grundstücke
- **Prüftiefe**: Tief (Bauphysik, Statik, Brandschutz) vs. Fokussiert (Verkehrssicherheit)

**Haupterkenntnis: Unterschiedliche Datenmodell-Integration**:

*XBau ↔ XPlanung: **LOSE KOPPLUNG***
- Komplementäre Standards mit funktionaler Integration
- XPlanung-Pläne als externe Prüfgrundlage
- Keine direkten XML-Referenzen
- Integration über GIS-Systeme
- Unabhängige Datenmodelle

*XBreitband ↔ XTrasse: **ENGE KOPPLUNG***
- Eng integrierte Standards mit struktureller Integration
- XTrasse-Trassenplan als integraler Bestandteil der Antragsnachricht
- Direkte strukturelle Bezüge im Datenmodell
- XTrasse basiert auf XPlanung-Grundstruktur
- Gemeinsame Basisklassen

**Erklärung des Unterschieds**:
- Hochbau: Gebäude sind **diskrete Objekte** auf definierten Grundstücken → abstrakte bauordnungsrechtliche Prüfung
- Tiefbau: Trassen sind **kontinuierliche lineare Infrastrukturen** über viele Grundstücke → präzise Georeferenzierung erforderlich
- Leitungsverlegung erfordert **exakte 3D-Leitungsverläufe** als Datengrundlage
- Baugenehmigung prüft gegen **abstrakte Bauordnungsvorgaben** (2D-Baugrenzen ausreichend)

**Deep Research Methodik**:
- 50+ Primärquellen analysiert (xleitstelle.de, IT-Planungsrat, FITKO, opencode.de)
- Vergleichstabellen erstellt (Gemeinsamkeiten, Unterschiede)
- XBau-Kernmodul als gemeinsame technische Basis dokumentiert
- Offene Fragen identifiziert (PDF-Spezifikationen nicht extrahierbar)

---

