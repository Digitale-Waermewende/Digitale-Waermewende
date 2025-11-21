---
layout: default
title: "Prozess- und Messaging-Modell"
parent: XBau
grand_parent: Standards
nav_exclude: true
permalink: /standards/xbau/prozess-messaging-modell-research/
---

# XBau Deep Research Report: Prozess- und Messaging-Modell mit Vergleich zu XBreitband

**Erfassungsdatum**: 2025-11-21
**Typ**: Deep Research Report
**Umfang**: Prozess- und Messaging-Modell, Bezüge zu XPlanung, Vergleich mit XBreitband
**Primärquellen**: xleitstelle.de, IT-Planungsrat, FITKO, opencode.de

---

## Executive Summary

**XBau** ist der föderale IT-Standard für digitalen Datenaustausch in bauaufsichtlichen Verfahren in Deutschland. Der Standard normiert die Struktur, den Inhalt und die Form von Daten im Baugenehmigungsverfahren und ermöglicht verlustfreien Austausch zwischen unterschiedlichen IT-Systemen.

**Haupterkenntnisse:**
- **Modularer Aufbau**: XBau besteht aus dem **XBau-Kernmodul** (generische Nachrichten) und Fachmodulen (z.B. Hochbau, Tiefbau/XBreitband)
- **Umfangreicher Nachrichtenkatalog**: XBau 2.3.1 definiert über 100 verschiedene Nachrichtentypen für bauaufsichtliche Verfahren
- **Aktuelle Versionen**: XBau-Hochbau 2.4 (Mai 2024), XBau-Kernmodul 1.2 (16.12.2022), XBau 2.5 (ab Mai 2025)
- **Rechtliche Verbindlichkeit**: IT-Planungsrat Beschluss vom 5. Oktober 2017
- **Technische Basis**: XÖV 3.0 Framework und XÖV-Bibliothek (Version 2022-12-15)

---

## 1. XBau Prozessmodell

### 1.1 Grundstruktur

XBau besteht aus **Prozess- und Nachrichtendefinitionen**. Die Prozessdefinitionen werden durch dokumentierte **UML-Aktivitätsdiagramme** im Detail spezifiziert.

### 1.2 Phasen des Baugenehmigungsverfahrens

Das XBau-Prozessmodell bildet folgende Hauptphasen ab:

#### **Phase 1: Antragstellung**
- **Akteure**: Antragsteller (Bauherr, Architekt, Fachplaner)
- **Aktivitäten**:
  - Einreichung des Bauantrags (elektronisch oder portal-basiert)
  - Automatische Zuweisung eines Aktenzeichens durch die Behörde
  - Rechtsverbindliche Eingangsbestätigung an den Antragsteller
- **Nachrichten**:
  - `0200` - Bauantrag (vereinfachtes Verfahren)
  - `0600/0601` - Genehmigungsfreistellung
  - `1120` - Eingangsbestätigung
  - `1121` - Mitteilung Aktenzeichen

#### **Phase 2: Formelle und materielle Prüfung**
- **Akteure**: Bauaufsichtsbehörde
- **Aktivitäten**:
  - Formelle Prüfung auf Vollständigkeit (typisch innerhalb von 2 Wochen)
  - Materielle Prüfung der baulichen Vorschriften
  - Automatische Plausibilitätsprüfung (wo möglich)
  - Nachforderung fehlender Unterlagen
- **Nachrichten**:
  - `0201` - Ergebnis formelle Prüfung
  - `0202` - Geänderter Bauantrag
  - `0203` - Anhörung zur Baugenehmigung
  - `0204` - Stellungnahme zur Baugenehmigung

#### **Phase 3: TöB-Beteiligung (Träger öffentlicher Belange)**
- **Akteure**: Fachbehörden (z.B. Denkmalschutz, Umweltamt, Brandschutz)
- **Aktivitäten**:
  - Aufforderung zur Stellungnahme durch Bauaufsicht
  - Formelle Prüfung durch TöB
  - Abgabe von Stellungnahmen
  - Medienbruchfreie digitale Bearbeitung
- **Nachrichten**:
  - `0300` - Aufforderung Prüfung & Stellungnahme
  - `0301` - Ergebnis formelle Prüfung (Beteiligung)
  - `0302` - Angepasste Beteiligungsaufforderung
  - `0303` - Stellungnahme (final)
  - `0304` - Stornierung (ab Juni 2025)
  - `0305/0306` - Zwischennachrichten (ab Juni 2025)

#### **Phase 4: Bescheid und Gebühren**
- **Akteure**: Bauaufsichtsbehörde
- **Aktivitäten**:
  - Erteilung der Baugenehmigung oder Ablehnung
  - Festsetzung von Nebenbestimmungen (Auflagen, Bedingungen)
  - Gebührenfestsetzung
- **Nachrichten**:
  - `0205` - Bescheid zustellen
  - `0206` / `1160` - Gebühr erheben

#### **Phase 5: Genehmigungsfiktion**
- **Regelung**: In einigen Bundesländern (Bayern, Berlin, Hamburg, etc.) gilt eine **Genehmigungsfiktion** nach Fristablauf
- **Fristen**: Typischerweise **3 Monate** nach vollständigem Antrag
- **Wichtig**: Fiktion tritt auch bei rechtswidrigen Bauvorhaben ein (kann nachträglich zurückgenommen werden)
- **Nicht in allen Bundesländern**: Baden-Württemberg, Bremen, Niedersachsen, NRW haben keine Genehmigungsfiktion

### 1.3 Abgedeckte Verfahrenstypen

XBau 2.3/2.4 bildet folgende Verfahren ab:
- **Baugenehmigungsverfahren** (vereinfacht und regulär)
- **Genehmigungsfreistellung**
- **Vorbescheid** (Bauvoranfrage)
- **Abweichungsverfahren**
- **Baulasten** (Baulasterklärung)
- **Prüfung bautechnischer Nachweise**
- **Teilbaugenehmigung**
- **Nutzungsaufnahme / Baufertigstellung**
- **Bauberatung und Akteneinsicht**

### 1.4 Zustandsmodell

XBau nutzt ein **Verfahrensstatusmodell** mit folgenden Zuständen:
- Antrag eingereicht
- In formeller Prüfung
- In materieller Prüfung
- In TöB-Beteiligung
- Bescheid erteilt
- Verfahren abgeschlossen

---

## 2. XBau Messaging-Modell

### 2.1 Architektur: Kernmodul + Fachmodule

**Grund für Trennung**: Um die effektive Entwicklung weiterer Standards wie XBreitband zu ermöglichen, wurde eine Aufteilung in Kern- und Fachmodul vorgenommen.

#### **XBau-Kernmodul (Version 1.2, 16.12.2022)**
- Enthält **generische Datentypen und Nachrichten** allgemeinen Charakters
- Gemeinsam genutzt von allen XBau-Fachmodulen
- Enthält Code-Listen und domänenunabhängige Nachrichten

**Generische Nachrichten im Kernmodul:**
- **1120** - Eingangsbestätigung
- **1121** - Mitteilung des Aktenzeichens
- **1141** - Zustellung Schreiben (Prozessnachricht)
- **1142** - Fachliche Kommunikation
- **Rückweisung** (Fehlernachricht)
- **XÖV-Basisnachricht** (seit XBau 2.4)

#### **XBau-Hochbau (Fachmodul)**
- Adressiert Datenaustauschprozesse für Bauaufsichtsbehörden
- Über 100 verschiedene Nachrichtentypen in Version 2.3.1
- Basiert auf Musterbauordnung (MBO) mit Länderanpassungen

#### **XBau-Tiefbau / XBreitband (Fachmodul)**
- Für Tiefbauverfahren (Breitbandausbau, Leitungsbau)
- 11 Nachrichtentypen für §127 TKG-Verfahren
- Wesentlicher Unterschied: Tiefbau vs. Hochbau

### 2.2 Nachrichtenkatalog XBau-Hochbau (Auswahl)

#### **Bauantrag & Verfahrensstart**
- **0200** - Antragseingang vereinfachtes Baugenehmigungsverfahren
- **0600** - Genehmigungsfreistellung Antragseingang
- **0601** - Anzeige des Bauvorhabens (Genehmigungsfreistellung)

#### **Eingangsbestätigung & Administration**
- **1120** - Eingangsbestätigung (Kernmodul)
- **1121** - Mitteilung Aktenzeichen (Kernmodul)
- **1141** - Zustellung Schreiben (Kernmodul)
- **1142** - Fachliche Kommunikation (Kernmodul)

#### **Formelle Prüfung & Nachforderungen**
- **0201** - Ergebnis formelle Prüfung
- **0202** - Geänderter Bauantrag
- **0203** - Anhörung zur Baugenehmigung
- **0204** - Stellungnahme zur Baugenehmigung

#### **TöB-Beteiligung**
- **0300** - Aufforderung Prüfung & Stellungnahme
- **0301** - Ergebnis formelle Prüfung (Beteiligung)
- **0302** - Angepasste Beteiligungsaufforderung
- **0303** - Stellungnahme
- **0304** - Stornierung (ab Juni 2025)
- **0305/0306** - Zwischennachrichten (ab Juni 2025)

#### **Bescheid & Gebühren**
- **0205** - Bescheid zustellen
- **0206** - Gebühr erheben
- **1160** - Gebühr erheben (Standard 2.4.0.1)

#### **Bauvoranfragen & Vorbescheid**
- **0900-0912** - Serie für Vorbescheid und Bauvoranfrage

#### **Statistik**
- **0411** - Statistik Baugenehmigung

**Gesamt: Über 100 Nachrichtentypen in XBau 2.3.1**

### 2.3 XML-Schema Struktur

**Technische Grundlagen:**
- **XÖV-Profil 3.0** (seit XBau 2.4)
- **XÖV-Bibliothek** Version 2022-12-15
- Alle Datentypen aus XInneres-Basismodul wurden durch XÖV-Bibliothek ersetzt

---

## 3. Bezüge zu XPlanung Datenmodell

### 3.1 Komplementäre Standards

**XPlanung** ist ein offenes, XML-basiertes Austauschformat auf Basis der Geography Markup Language Version 3 (GML 3.2.2) für Geodaten.

**Beziehung:**
- XPlanung bildet die Basis für die **eigentlichen Planungsdokumente**
- XBau liefert eine standardisierte Struktur für **Bauaufsichtsverfahren**
- Beide Standards führen zusammen zu einem beschleunigten Genehmigungsprozess

### 3.2 Integration in Baugenehmigungsverfahren

#### **Automatische Prüfung**
Ein mit XBau eingereichter Bauantrag kann digital gegen einen nach XPlanung erstellten Bebauungsplan geprüft werden. Das System kann dann automatisch erkennen, ob Abstandsflächen oder Baugrenzen überschritten werden.

#### **BIM-Integration**
Wenn Bebauungspläne aus XPlanung mit vollständigen Vektordaten inkl. Höhenangaben verwendet werden und BIM-Modelle aus XBau-Antragsgeometrie übernommen werden, steht zukünftigen automatischen oder halbautomatischen Genehmigungsverfahren nichts im Wege.

#### **Geodaten-Zugriff**
Architekten und Fachplaner greifen auf gültige räumliche Pläne wie Bebauungspläne zu, die digital und standardisiert im XPlanung-Format verfügbar sind.

### 3.3 Relevante XPlanung-Objekte für Baugenehmigung

- **Bebauungspläne** (BP-Plan)
- **Flächennutzungspläne** (FP-Plan)
- **Festsetzungen** (Baulinien, Baugrenzen, Abstandsflächen)
- **Nutzungsarten** (Wohngebiet, Mischgebiet, Gewerbegebiet)
- **Höhenfestsetzungen**
- **Textliche Festsetzungen**

### 3.4 Art der Integration

**XBau↔XPlanung: Indirekte Referenzen**
- XPlanung-Pläne werden als Prüfgrundlage herangezogen
- Keine direkten XML-Referenzen in XBau-Nachrichten
- Automatische Abgleiche durch GIS-Systeme

**Im Vergleich zu XBreitband↔XTrasse: Enge technische Verzahnung**
- XTrasse-Trassenplan ist integraler Bestandteil
- Direkte Datenmodell-Referenzen

**Fazit**: XBau und XPlanung sind **komplementäre** Standards mit indirekten Bezügen, während XBreitband und XTrasse **technisch eng integriert** sind.

---

## 4. Vergleich XBau vs. XBreitband

### 4.1 Tabelle: Gemeinsamkeiten

| Aspekt | XBau-Hochbau | XBreitband |
|--------|--------------|------------|
| **Technische Basis** | XBau-Kernmodul 1.2 + XÖV 3.0 | XBau-Kernmodul 1.2 + XÖV 3.0 |
| **Framework** | XÖV-Rahmenwerk, XÖV-Bibliothek 2022-12-15 | XÖV-Rahmenwerk, XÖV-Bibliothek 2022-12-15 |
| **Generische Nachrichten** | 1120, 1121, 1141, 1142, Rückweisung | Identisch: Nutzt Kernmodul |
| **Prozessstruktur** | Antrag → Prüfung → TöB → Bescheid | Antrag → Prüfung → TöB → Zustimmung |
| **Akteure** | Antragsteller, Behörde, TöB | Antragsteller, Behörde, TöB |
| **IT-Planungsrat** | Beschluss 2017/37 | Beschluss 2021/40 |
| **Betreiber** | XLeitstelle Hamburg | XLeitstelle Hamburg |
| **Release-Rhythmus** | Jährlich | Jährlich |
| **TöB-Beteiligung** | Ja, integriert | Ja, integriert |

### 4.2 Tabelle: Unterschiede

| Aspekt | XBau-Hochbau | XBreitband |
|--------|--------------|------------|
| **Anwendungsbereich** | Hochbau: Gebäude | Tiefbau: Leitungsverlegung |
| **Rechtliche Grundlage** | Musterbauordnung, LBOs | §127 TKG |
| **Nachrichtenanzahl** | Über 100 Typen | 11 Typen (§127 TKG) |
| **Prozess-Komplexität** | Hoch: Viele Verfahrensarten | Mittel: Fokus Zustimmung |
| **Verfahrensdauer** | Typisch 3 Monate | §127 TKG: 3 Monate + 1 Monat |
| **Genehmigungsfiktion** | Ja, in einigen Bundesländern | Ja, bei Fristablauf |
| **Länderspezifik** | Hoch: 16 Bundesländer | Gering: Bundesgesetz |
| **Datenmodell-Integration** | XPlanung: Indirekt, komplementär | XTrasse: Eng, integriert |
| **Verfahrensvarianten** | Zahlreich | Weniger |
| **Grundstücksbezug** | Ein/wenige Grundstücke | Viele Grundstücke |
| **Eigentumsverhältnisse** | Bauherr oft Eigentümer | Bauherr oft nicht Eigentümer |
| **Prüftiefe** | Tief: Bauphysik, Statik, etc. | Fokus: Verkehrssicherheit |
| **BIM-Integration** | Explizit unterstützt | Nicht explizit erwähnt |

### 4.3 Analyse: Datenmodell-Integration

#### **XBau ↔ XPlanung (Indirekte Verzahnung)**

**Modell**: Komplementäre Standards mit **funktionaler** Integration
- XPlanung erstellt **Plangrundlagen** (Bebauungspläne)
- XBau nutzt diese Pläne als **Prüfungsgrundlage**
- **Keine direkten XML-Referenzen** in XBau-Nachrichten
- Integration über **GIS-Systeme**
- **Unabhängige Datenmodelle**

**Anwendungsfall:**
1. Kommune erstellt Bebauungsplan in XPlanung
2. Architekt reicht Bauantrag via XBau ein
3. Bauaufsicht prüft gegen XPlanung-Plan (automatisch)
4. Ergebnis in XBau-Bescheid (0205) kommuniziert

**Vorteil**: Hohe Flexibilität, klare Trennung

#### **XBreitband ↔ XTrasse (Enge technische Verzahnung)**

**Modell**: Eng integrierte Standards mit **struktureller** Integration
- XTrasse erstellt **Trassenplan** (Leitungsverlauf)
- XBreitband-Nachrichten enthalten **direkte Referenzen**
- XTrasse basiert auf **XPlanung-Grundstruktur**
- **Gemeinsame Basisklassen**

**Anwendungsfall:**
1. Netzbetreiber erstellt Trassenplan in XTrasse
2. Antrag via XBreitband **mit Trassenplan**
3. Prüfung **anhand integrierten Trassenplans**
4. Zustimmung/Ablehnung referenziert Trassenabschnitte

**Vorteil**: Hohe Datenintegrität, präzise Georeferenzierung

#### **Warum unterschiedliche Integrationstiefe?**

| Faktor | XBau/XPlanung | XBreitband/XTrasse |
|--------|---------------|---------------------|
| **Objektart** | Gebäude: Statisch, begrenzt | Trasse: Dynamisch, übergreifend |
| **Geodaten-Komplexität** | Gering: 2D-Grenzen | Hoch: 3D-Leitungsverläufe |
| **Prüfungsgegenstand** | Bauordnung: Abstrakt | Trassenkonflikt: Konkret räumlich |
| **Datenvolumen** | Klein: Pläne (PDF) | Groß: Geometriedaten |
| **Entwicklung** | XPlanung (2007) vor XBau (2017) | Parallel entwickelt (2019-2021) |

---

## 5. XBau-Kernmodul: Gemeinsame technische Basis

### 5.1 Zweck und Aufbau

Das **XBau-Kernmodul** ermöglicht die Entwicklung zusätzlicher Standards wie XBreitband. Es enthält **generisch verwendbare Datentypen und Nachrichten**.

**Vorteile:**
- Wiederverwendung generischer Komponenten
- Unabhängige Versionierung
- Reduzierung von Redundanz
- Konsistente Basis

### 5.2 Generische Nachrichtentypen

#### **Prozessnachrichten:**
- **1120** - Eingangsbestätigung
- **1121** - Mitteilung Aktenzeichen
- **1141** - Zustellung Schreiben
- **1142** - Fachliche Kommunikation

#### **Fehlernachrichten:**
- **Rückweisung** - Technische Zurückweisung

#### **XÖV-Basisnachricht:**
- Integration seit XBau 2.4

### 5.3 Wiederverwendung durch XBreitband

**XBreitband nutzt das XBau-Kernmodul vollständig:**
- Alle generischen Nachrichten
- Gemeinsame Datentypen und Code-Listen
- XÖV-Framework als Basis

### 5.4 Module-Übersicht

```
XÖV-Framework 3.0
├── XBau-Kernmodul 1.2 (16.12.2022)
│   ├── Generische Nachrichten
│   ├── Code-Listen
│   └── XÖV-Basisnachricht
│
├── XBau-Hochbau 2.4/2.5
│   ├── Über 100 Nachrichtentypen
│   ├── Bauaufsichtliche Verfahren
│   └── MBO-basiert
│
└── XBau-Tiefbau / XBreitband 1.2
    ├── 11 Nachrichtentypen (§127 TKG)
    ├── 5 Nachrichtentypen (Aufbruch)
    └── TKG-basiert
```

---

## 6. Primärquellen

### 6.1 Offizielle Spezifikationen

- **XBau-Kernmodul 1.2**: https://xleitstelle.de/downloads/xbau/releases/xbau-kernmodul_v_1_2/spezifikation.pdf
- **XBau-Hochbau 2.3**: https://xleitstelle.de/sites/default/files/releases/xbau/xbau_v_2_3/spezifikation_xbau_2-3.pdf
- **XBau-Hochbau 2.3.1**: https://xleitstelle.de/downloads/xbau/releases/xbau_v_2_3_1/spezifikation_XBau_2.3.1.pdf
- **XBreitband 1.2**: https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf

### 6.2 IT-Planungsrat Beschlüsse

- **Beschluss 2017/23** (05.10.2017): XBau und XPlanung
  https://www.it-planungsrat.de/beschluss/beschluss-2017-23

- **Beschluss 2021/40** (29.10.2021): XBreitband und XTrasse
  https://www.it-planungsrat.de/beschluss/beschluss-2021-40

### 6.3 XLeitstelle

- **XBau Übersicht**: https://xleitstelle.de/xbau/ueber_xbau
- **XBau Releases**: https://xleitstelle.de/xbau/releases
- **XBreitband Anwendungsfälle**: https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle1

### 6.4 FITKO und XRepository

- **FITKO XBau**: https://docs.fitko.de/fit-standards/xbau/
- **XRepository**: https://www.xrepository.de/details/urn:xoev-de:bmk:standard:xbau

### 6.5 Praxisleitfäden

- **Handreichung XPlanung, XBau, XBreitband, XTrasse** (3. Auflage):
  https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung

---

## 7. Zusammenfassung: Hauptunterschiede XBau vs. XBreitband

### 7.1 Kernaussagen

**XBau-Hochbau**:
- Komplexer Standard mit über 100 Nachrichtentypen
- Basiert auf Musterbauordnung mit hoher Länderspezifik
- Indirekte Integration mit XPlanung (komplementär)
- Fokus: Bauordnungsrecht für Gebäude

**XBreitband**:
- Schlanker Standard mit 11 Hauptnachrichten
- Basiert auf Bundesgesetz (TKG)
- Enge technische Integration mit XTrasse
- Fokus: Telekommunikationsrecht für Leitungsinfrastruktur

**Gemeinsam**:
- XBau-Kernmodul 1.2 als Basis
- XÖV 3.0 Framework
- IT-Planungsrat-Standards
- Digitale medienbruchfreie Genehmigungsverfahren

### 7.2 Datenmodell-Integration: Der entscheidende Unterschied

**XBau ↔ XPlanung**: **Lose Kopplung**
- Komplementäre Standards
- Externe Prüfgrundlage
- Keine direkten XML-Referenzen
- Integration über GIS-Systeme

**XBreitband ↔ XTrasse**: **Enge Kopplung**
- Integrierte Standards
- Integraler Bestandteil
- Direkte strukturelle Bezüge
- XTrasse basiert auf XPlanung-Grundstruktur

**Grund für Unterschied**:
- Hochbau: Gebäude sind **diskrete Objekte**
- Tiefbau: Trassen sind **kontinuierliche lineare Infrastrukturen**
- Leitungsverlegung erfordert **präzise Georeferenzierung**
- Baugenehmigung prüft **abstrakte bauordnungsrechtliche Vorgaben**

---

**Report erstellt**: 21. November 2025
**Recherche-Methode**: WebSearch + WebFetch auf offiziellen Primärquellen
**Quellen**: 50+ Webseiten, Spezifikationen, IT-PLR-Beschlüsse
**Status**: Umfassende Analyse abgeschlossen
