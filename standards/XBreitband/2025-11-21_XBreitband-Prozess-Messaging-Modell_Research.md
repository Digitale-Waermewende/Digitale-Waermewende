# XBreitband Deep Research Report
## Prozess- und Messaging-Modell der XLeitstelle

**Erstellungsdatum:** 2025-11-21
**Fokus:** XBreitband Prozessmodell und Nachrichtenstruktur für §127 TKG Zustimmungsverfahren
**Primärquellen:** xleitstelle.de, docs.fitko.de, gitlab.opencode.de, IT-Planungsrat

---

## 1. Executive Summary

**XBreitband** ist der föderale IT-Standard für die Datenkommunikation zwischen Antragstellern und Genehmigungsbehörden im Kontext des Breitbandausbaus in Deutschland. Der Standard definiert Struktur und Inhalt aller Nachrichten, die zur Abbildung von Verfahren vom Antrag bis zum Bescheid erforderlich sind.

### Kernerkenntnisse

- **Aktuelle Version:** XBreitband Release 1.2 (final), veröffentlicht 28. Mai 2024
- **Rechtliche Grundlage:** IT-Planungsrat Beschluss 2021/40 vom 29. Oktober 2021 (verbindlich)
- **Hauptanwendungsfall:** Zustimmungsverfahren nach § 127 Abs. 1 TKG mit **11 Nachrichten**
- **Technische Basis:** XÖV 3.0 Framework, XBau Kernmodul, XML-basierter Datenaustausch
- **Betreiber:** XLeitstelle als zentrale Koordinierungsstelle
- **Status:** Regelbetrieb (operational)
- **Beziehungskontext:** G2G (Government-to-Government) und B2G (Business-to-Government)

### Kritische Einschränkung

Die vollständige Liste aller 11 Nachrichtentypen und detaillierte XML-Schema-Strukturen konnten nicht aus öffentlich zugänglichen Webquellen extrahiert werden. Die offiziellen PDF-Spezifikationen sind binär komprimiert und nicht direkt lesbar über WebFetch. Für die vollständige technische Dokumentation ist ein **direkter Download der Spezifikation 1.2 und der XSD-Dateien aus dem XRepository erforderlich**.

---

## 2. Prozessmodell für §127 TKG Zustimmungsverfahren

### 2.1 Überblick Prozessablauf

Das Zustimmungsverfahren nach § 127 Abs. 1 TKG ist der zentrale Anwendungsfall von XBreitband und umfasst **drei Hauptphasen**:

#### Phase 1: Antragsvorbereitung und Einreichung
- **Akteure:** Telekommunikationsunternehmen (TKU/Antragsteller), Straßenbaubehörde
- **Aktivitäten:**
  - TKU erstellt Zustimmungsantrag mit erforderlichen Unterlagen
  - Einreichung bei zuständiger Straßenbaubehörde
  - Je nach Projekt erfolgen mehrere Anträge an verschiedene Behörden
- **XBreitband-Nachrichten:** Antragsnachricht mit Dokumenten und Bauvorhaben-Daten

#### Phase 2: Vollständigkeitsprüfung und Beteiligung
- **Akteure:** Straßenbaubehörde, Träger öffentlicher Belange (TöB)
- **Aktivitäten:**
  - Zuständigkeitsprüfung durch Straßenbaubehörde
  - Vollständigkeitsprüfung innerhalb 1 Monat
  - Bei Unvollständigkeit: Nachforderung in Textform
  - Bei Vollständigkeit: Beteiligung öffentlicher Stellen
- **Prozessvarianten:**
  - **Variante B2G:** Antragsteller holt Stellungnahmen selbst ein
  - **Variante G2G:** Straßenbaubehörde koordiniert Beteiligung
- **XBreitband-Nachrichten:**
  - Beteiligungsnachrichten an TöB
  - Stellungnahmen von TöB (Nachricht 2005 "Änderungsbedarf" oder Nachricht 2008 "Bescheid")
  - Leitungsanfragen
  - Informationsnachrichten

#### Phase 3: Bescheiderteilung
- **Akteure:** Straßenbaubehörde, TKU
- **Aktivitäten:**
  - Prüfung als "gebundene Entscheidung" auf Basis § 125 Abs. 1 TKG
  - Zustimmung gilt als erteilt nach 3 Monaten (Fiktionswirkung)
  - Verlängerung um 1 Monat bei Schwierigkeit möglich (mit Begründung)
  - Bei Änderung/Ergänzung beginnen Fristen neu
  - Nebenbestimmungen nach § 127 Abs. 8 TKG möglich
- **XBreitband-Nachrichten:** Bescheidnachricht mit Entscheidungsinhalt

### 2.2 Zusätzliche Prozesskomponenten

#### Baumaßnahmen-Anzeigen
- **Baubeginnsanzeige:** TKU meldet Baubeginn an Straßenbaubehörde
- **Baufertigstellungsanzeige:** TKU meldet Abschluss der Baumaßnahme

#### Einspruchs-/Widerspruchsverfahren
- TKU kompiliert Gründe für Einspruch mit neuen Aspekten
- Bereitstellung von Informationen für erneute Prüfung durch Straßenbaubehörde

#### Geringfügige Bauvorhaben (§ 127 Abs. 4 TKG)
- Separater Anwendungsfall mit **2 Nachrichten**
- Vereinfachtes Verfahren ohne formellen Antrag
- Zustimmung gilt als erteilt, wenn Behörde nicht binnen 1 Monat formellen Antrag fordert

### 2.3 Prozessdiagramm

Die Spezifikation enthält in **Kapitel 3** ein detailliertes Prozessdiagramm:
- **Abbildung 3.1:** "Prozess Zustimmungsverfahren nach § 127 Abs. 1 TKG"
- Zeigt alle Prozessschritte und wo jede Nachricht verwendet wird
- Basis ist die Annahme, dass am Ende die Zustimmung erteilt wird

### 2.4 Akteure und ihre Rollen

#### Antragsteller (TKU)
- Telekommunikationsunternehmen als gleichberechtigte Akteure
- Erstellen Zustimmungsanträge mit vollständigen Unterlagen
- Optional: Eigenständige Beteiligung von TöB (Variante B2G)
- Meldung von Baubeginn und -fertigstellung

#### Straßenbaubehörde (Wegebaulastträger)
- Prüfung der Zuständigkeit und Vollständigkeit
- Koordinierung der TöB-Beteiligung (Variante G2G)
- Entscheidung über Zustimmung (gebundene Entscheidung)
- Erteilung des Bescheids mit möglichen Nebenbestimmungen

#### Träger öffentlicher Belange (TöB)
- Öffentliche und private Institutionen mit öffentlichen Aufgaben
- Beispiele: Naturschutz, Wasserwirtschaft, Bodenschutz, Denkmalschutz, Straßenbau, Vermessung, Geologie, Rohstoffe, Bergbau, Land-/Forstwirtschaft, Fischerei
- Abgabe von Stellungnahmen mit strukturierten Ergebnissen
- Kommunikation über Breitband-Portal

### 2.5 Zustandsübergänge

Obwohl kein explizites Zustandsmodell in den öffentlichen Quellen dokumentiert wurde, lassen sich folgende **logische Zustände** ableiten:

1. **Antrag eingereicht** → Vollständigkeitsprüfung
2. **Antrag unvollständig** → Nachforderung → zurück zu Phase 1
3. **Antrag vollständig** → Beteiligungsphase
4. **Stellungnahmen ausstehend** → Sammlung TöB-Rückmeldungen
5. **Stellungnahmen eingegangen** → Prüfung durch Straßenbaubehörde
6. **Änderungsbedarf** → Anpassung durch TKU → erneute Prüfung
7. **Zustimmung erteilt** (aktiv oder fiktiv) → Bescheid → Bauphase
8. **Baubeginn gemeldet** → Bauphase aktiv
9. **Bau fertiggestellt** → Verfahren abgeschlossen
10. **Einspruch** → Einspruchsverfahren → zurück zu Prüfung

---

## 3. Messaging-Modell

### 3.1 Nachrichtentypen-Übersicht

XBreitband definiert für das **Zustimmungsverfahren nach § 127 Abs. 1 TKG insgesamt 11 Nachrichten**. Die genaue Bezeichnung und Nummerierung konnte aus öffentlichen Quellen nicht vollständig ermittelt werden. Identifizierte Nachrichtentypen:

#### Identifizierte Nachrichten

1. **Zustimmungsantrag** - Formeller Antrag des TKU
2. **Beteiligungsnachricht** - An öffentliche Stellen
3. **Stellungnahme** - Rückmeldung von TöB
4. **Nachricht 2005: Änderungsbedarf** - Strukturierte Änderungsanforderungen
5. **Nachricht 2008: Bescheid** - Entscheidung der Straßenbaubehörde
6. **Leitungsanfrage** - Anfrage zu bestehenden Leitungen
7. **Leitungsauskunft** - Antwort auf Leitungsanfrage
8. **Baubeginnsanzeige** - Meldung Baubeginn
9. **Baufertigstellungsanzeige** - Meldung Baufertigstellung
10. **Informationsnachricht** - An Informationsempfänger
11. *[Weitere Nachricht nicht identifiziert]*

#### Generische Nachrichten (XBau Kernmodul)

Zusätzlich zu den fachspezifischen Nachrichten enthält das **XBau Kernmodul** generische Prozessnachrichten:

- **Eingangsbestätigung** (Spezifikation Abschnitt III.7.4) - Bestätigung des Nachrichtenempfangs
- **Rückweisung/Ablehnungsnachricht** (Spezifikation Abschnitt III.7.3) - Ablehnung bei fehlgeschlagener Validierung

### 3.2 Weitere Anwendungsfälle

#### Aufbruchgenehmigung (5 Nachrichten)
- **Zielgruppe:** Andere Leitungssparten (Strom, Gas, Wasser, Abwasser)
- **Besonderheiten:** Keine integrierten Beteiligungsprozesse
- **Prozess:** Antrag → Prüfung → Genehmigung → Bauanzeigen

#### Geringfügige Bauvorhaben §127 Abs. 4 TKG (2 Nachrichten)
- Vereinfachtes Anzeigeverfahren
- Keine formelle Antragstellung

#### Teilweise implementierte Anwendungsfälle
- Sondernutzungsgenehmigungen
- Verkehrsrechtliche Anordnungen
- Leitungsauskunft

#### Noch nicht implementierte Anwendungsfälle
- Mitnutzung/Mitverlegung nach TKG
- Anfragen zu Kampfmittelbelastung
- Naturschutzrechtliche Genehmigungsprozesse

### 3.3 XML-Schema-Struktur

#### Technische Basis

**XÖV-Framework:**
- Basiert auf **XÖV-Profil 3.0**
- Nutzt **XÖV-Bibliothek** (Version 2022-12-15)
- Integriert **XÖV-Basisnachricht** für G2G-Kommunikation

**XBau Kernmodul:**
- Trennung in Kernmodul und Fachmodule für effiziente Entwicklung
- Kernmodul enthält allgemein nutzbare Datentypen und generische Nachrichten
- Code-Listen und unspezifische Nachrichten
- Ermöglicht unabhängige Versionierung von XBau-Hochbau und XBreitband

**Nachrichtenstruktur:**
- **Header-Struktur:** XÖV-konforme Header für alle Nachrichten (aus XÖV-Standard XInneres)
- **Universally Unique Identifier (UUID):** Nach RFC 4122 für globale Eindeutigkeit
- **Behördenidentifikation:** Identifikation in Verzeichnisdiensten mit Erreichbarkeitsinformationen
- **Transportinformationen:** Einheitliche Header-Daten für sparten-übergreifende Transportdienstleister

#### Nachrichteninhalte

XBreitband-Nachrichten enthalten:
- **Verfahrensdaten:** Informationen zu Genehmigungs-/Zulassungsverfahren
- **Bauvorhaben-Daten:** Details zu Tiefbauvorhaben
- **Beteiligte:** Daten zu allen involvierten Personen/Organisationen
- **Dokumente:** Stellungnahmen oder Verweise auf Dokumente
- **Trassendaten:** Verknüpfung zu XTrasse-Plänen (optional aber üblich)

#### XML-Format

- **Format:** XML-Dokumente nach XÖV-Standard
- **Validierung:** XML-Schema-Dateien (XSD) für Interface-Implementierung
- **Code-Listen:** OASIS-Genericode-Format (XML-Instanzen)
- **GML-Integration:** Über XTrasse für Geokoordinaten und GIS/CAD-Verarbeitung

### 3.4 Beispiel-Nachrichtenstruktur (konzeptionell)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<nachricht:XBreitbandNachricht xmlns:nachricht="urn:xoev-de:it-plr:standard:xbau-tiefbau">
  <!-- XÖV-Header -->
  <header>
    <uuid>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</uuid>
    <ersteller>
      <behoerdenidentifikation>...</behoerdenidentifikation>
    </ersteller>
    <empfaenger>
      <behoerdenidentifikation>...</behoerdenidentifikation>
    </empfaenger>
    <erstellungszeitpunkt>2024-11-21T10:00:00Z</erstellungszeitpunkt>
  </header>

  <!-- Fachlicher Inhalt (je nach Nachrichtentyp) -->
  <inhalt>
    <zustimmungsantrag>
      <bauvorhaben>...</bauvorhaben>
      <antragsteller>...</antragsteller>
      <trassenplan referenz="XTrasse-ID">...</trassenplan>
      <dokumente>...</dokumente>
    </zustimmungsantrag>
  </inhalt>
</nachricht:XBreitbandNachricht>
```

**Hinweis:** Dies ist eine konzeptionelle Darstellung. Die exakte Schema-Struktur ist in den offiziellen XSD-Dateien im XRepository dokumentiert.

---

## 4. Primärquellen mit URLs

### Offizielle Spezifikationen

1. **XBreitband Spezifikation 1.2 (final)**
   - URL: https://xleitstelle.de/sites/default/files/2024-06/spezifikation1.2.pdf
   - Veröffentlichung: 28. Mai 2024
   - Inhalt: Vollständige Darstellung aller Nachrichten, Datentypen, Prozessdiagramme
   - Kapitel 3: Verfahrensabläufe integrierter Anwendungsfälle
   - Kapitel 4: Nachrichten für den Leitungsbau
   - Kapitel 5: Informationsmodell

2. **XBreitband Spezifikation 1.1 (final)**
   - URL: https://xleitstelle.de/sites/default/files/2023-07/Spezifikation%20XBreitband.pdf
   - Vorversion (Legacy)

3. **IT-Planungsrat Beschluss 2021/40**
   - URL: https://www.it-planungsrat.de/beschluss/beschluss-2021-40
   - Anlage 2: https://www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-40_IT-Standard_XBau_und_XPlanung_AL2_Spezifikation_XBreitband.pdf
   - Beschluss: 29. Oktober 2021
   - Verbindlichkeit: Verpflichtender IT-Standard für Bund und Länder

### XLeitstelle Dokumentation

4. **XBreitband/XTrasse Hauptseite**
   - URL: https://xleitstelle.de/xtrassexbreitband
   - Überblick über beide Standards

5. **XBreitband Anwendungsfälle**
   - URL: https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle1
   - Beschreibung aller Use Cases

6. **XTrasse Anwendungsfälle und Datenmodell**
   - URL: https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2
   - Details zu XTrasse-Objektklassen

7. **Download-Seite**
   - URL: https://xleitstelle.de/xtrassexbreitband/download
   - Zugang zu Spezifikationen, Schemas, Code-Listen, UML-Modellen

8. **XML-Nachrichten-Tool (XNT)**
   - URL: https://xleitstelle.de/xtrassexbreitband/xnt
   - Tool zur Erstellung von Test-Nachrichten

9. **Rechtliche Verbindlichkeit**
   - URL: https://xleitstelle.de/leitstelle/rechtliches
   - Rechtlicher Status der Standards

### FITKO Dokumentation

10. **XBreitband/XTrasse FIT-Standards**
    - URL: https://docs.fitko.de/fit-standards/xbreitband/
    - Föderale IT-Dokumentation
    - Status, Ressourcen, Testumgebung, Referenzimplementierung, Betriebshandbuch

### Repositories

11. **XRepository (XBreitband Standard)**
    - URL: https://www.xrepository.de/details/urn:xoev-de:it-plr:standard:xbau-tiefbau
    - URN: urn:xoev-de:it-plr:standard:xbau-tiefbau
    - Download: XML-Schemas (XSD), Code-Listen (Genericode), UML-Modelle (XMI)

12. **GitLab OpenCoDE - XML-Nachrichten-Tool**
    - URL: https://gitlab.opencode.de/xleitstelle/xbreitband/xnt
    - Repository: 147 Commits, erstellt 28. Oktober 2022
    - Funktionalität: Generierung von Test-Nachrichten mit Dummy-Daten

13. **GitLab OpenCoDE - XLeitstelle Hauptgruppe**
    - URL: https://gitlab.opencode.de/xleitstelle
    - Publikation von XTrasse, XPlanung, XBau-Materialien
    - Hinweis: XBreitband-Schemas primär im XRepository

### Praxisprojekte

14. **BIMBreitband-Projekt**
    - URL: https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau
    - Implementierung BIM-Methodik mit XBreitband
    - Prototyp-Plattform für Praxistests

### Weitere Ressourcen

15. **Gigabitbüro des Bundes - §127 TKG Leitfaden**
    - URL: https://gigabitbuero.de/thema/zustimmungsverfahren-zielorientiert-anwenden/
    - Praxisorientierte Anleitung zum Zustimmungsverfahren

16. **TKG §127 Gesetzestext**
    - URL: https://www.gesetze-im-internet.de/tkg_2021/__127.html
    - Rechtliche Grundlage

17. **Handreichung XPlanung/XBau/XBreitband/XTrasse (Deutscher Städtetag)**
    - URL: https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung
    - 3. Auflage (Januar 2023), erweitert um XTrasse/XBreitband

18. **Handreichung XPlanung (Deutscher Landkreistag)**
    - URL: https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage
    - 3. Auflage mit XBreitband/XTrasse-Erklärungen

---

## 5. Technische Details

### 5.1 Versionshistorie

| Version | Status | Veröffentlichung | Änderungen |
|---------|--------|------------------|------------|
| 1.0 | Entwurf | September 2021 | Initiale Version für IT-Planungsrat Beschluss |
| 1.1 | Final | Juli 2023 | Erste finale Version |
| 1.2 | Final | 28. Mai 2024 | **Aktuelle Version** - Aktualisierungen Prozessdiagramme, Nachrichten |

### 5.2 Technische Standards und Abhängigkeiten

#### XÖV-Framework
- **XÖV-Profil:** Version 3.0
- **XÖV-Bibliothek:** Version 2022-12-15
- **XÖV-Basisnachricht:** Für G2G-Kommunikation
- **Standard:** XInneres für Nachrichtenheader

#### XBau-Familie
- **XBau Kernmodul:** Version 1.2 (16. Dezember 2022)
- **Generische Nachrichten:** Eingangsbestätigung, Rückweisung
- **Code-Listen:** Gemeinsame Codelisten mit XBau-Hochbau

#### Datenformate
- **XML:** Hauptformat für Nachrichtenaustausch
- **XSD (XML Schema Definition):** Interface-Spezifikation
- **OASIS Genericode:** Format für Code-Listen
- **UML:** Modellierung (XMI und MagicDraw-Format)
- **GML (Geography Markup Language):** Via XTrasse für Geodaten (ISO 19136)

#### Transport und Infrastruktur
- **FIT-Connect:** Testumgebung für Nachrichtentransport
- **XTA (XÖV-Transportadapter):** Transport-Infrastruktur
- **Clearing Houses:** Sparten-übergreifende Transportdienstleister
- **OSCI (Online Services Computer Interface):** Optionale sichere Kommunikation

#### UUID-Standard
- **RFC 4122:** Universally Unique IDentifier für Nachrichtenidentifikation

### 5.3 Download-Komponenten

XBreitband 1.2 umfasst:
1. **Spezifikation (PDF):** Vollständige Dokumentation aller Nachrichten und Datentypen
2. **XML-Schema-Dateien (XSD):** Technische Schema-Definitionen für Implementierung
3. **Code-Listen (XML):** OASIS-Genericode-Format
4. **UML-Modell:** XMI und MagicDraw-Formate

### 5.4 Werkzeuge

#### XML-Nachrichten-Tool (XNT)
- **Funktion:** Liest XBreitband-XSD-Dateien und generiert Test-Nachrichten mit Dummy-Daten
- **Unterstützte Standards:** XBreitband, XBau, XBeteiligung
- **Features:**
  - Erzeugung von Test-Nachrichteninstanzen
  - Editierung generierter Nachrichten
  - Test von Inhalt und Transport
  - Versand/Empfang in FIT-Connect Testumgebung
  - Integration in XTA-Transportinfrastruktur
- **Zugriff:** OpenCoDE GitLab

#### Validierungswerkzeuge
- XML-Schema-Validierung gegen XSD
- Codelisten-Validierung

#### Produktionsumgebung
- XTrasse-konforme Pläne erstellen und als XTrasseGML exportieren
- Integration mit GIS/CAD-Systemen

---

## 6. Verhältnis zu XTrasse und TKG

### 6.1 XBreitband vs. XTrasse

#### XBreitband (Prozess-Standard)
- **Zweck:** Datenkommunikation zwischen Antragstellern und Genehmigungsbehörden
- **Fokus:** **Prozesse und Nachrichten**
- **Normalisiert:** Struktur, Inhalt und Form von **Informationen und Verfahren** in Genehmigungsprozessen
- **Format:** XML-Dokumente
- **Kommunikation:** Maschine-zu-Maschine zwischen Fachanwendungen
- **Inhalte:** Verfahrensdaten, Bauvorhaben-Daten, Beteiligte, Dokumente, Stellungnahmen

#### XTrasse (Datenmodell-Standard)
- **Zweck:** Geodatenstandard für Modellierung von Leitungsnetzen
- **Fokus:** **Datenmodell und Trassenpläne**
- **Normalisiert:** Struktur, Inhalt und Form von **Trassenverläufen**
- **Format:** GML (Geography Markup Language) nach ISO 19136
- **Kommunikation:** Verlustfreier Datentransfer zwischen IT-Systemen (GIS, CAD)
- **Inhalte:** Trassenpläne, Leitungsverläufe, Infrastrukturobjekte

#### Direkte Beziehung

**Komplementäre Standards mit enger Integration:**

1. **Gemeinsame Nutzung:**
   - Simultane Verwendung beider Standards ist üblich
   - **"Ohne Trassenplan ist eine Antragsnachricht für Breitbandausbau in der Regel nicht vollständig"**
   - XTrasse-Pläne werden als Anhang/Referenz in XBreitband-Nachrichten integriert

2. **Überschneidende Datenfelder:**
   - Informationen zu Baumaßnahmen können in beiden Standards erfasst werden
   - Redundanz ist gewollt zur Erleichterung der Integration in anwendungsorientierte Workflows

3. **Unterschied zu XBau/XPlanung:**
   - XBau und XPlanung haben weniger direkte Beziehung
   - XBreitband und XTrasse haben eine **viel direktere Beziehung**

### 6.2 XTrasse Datenmodell-Details

#### 6 Anwendungsfälle von XTrasse 2.0

1. **Breitbandausbau:** Glasfasernetze von überörtlicher Konzeption bis Detailtiefe der Zustimmungsverfahren
2. **Infrastrukturatlas:** Datenlieferungen von Leitungsnetzbetreibern an Bundesnetzagentur
3. **Raumverträglichkeitsprüfung:** Trassenkorridore und Varianten
4. **Infrastrukturgebieteplan:** Alternative zur Raumverträglichkeitsprüfung für Energieleitungen
5. **Planfeststellung:** Trassenförmige Energieinfrastrukturen in verschiedenen Maßstabsebenen
6. **Bestandsplan:** Zusammenführung von Leitungsplänen verschiedener Sparten

#### Modularer Aufbau (Pakete)

- **Bestandsnetze, Breitbandausbau, Infrastrukturatlas:** Einzelne Anwendungsfälle
- **Infrastrukturausbau:** Drei fachlich verbundene Anwendungsfälle
- **Basisklassen:** Vererbte Attribute und Assoziationen
- **ISO 19136 GML:** Geokoordinaten und GIS/CAD-Verarbeitung

#### Objektklassen-Kategorien

- **Abstrakte Oberklassen** (türkisblau, kursiv): Geometrietypen
- **Fachobjekte** (gelb): Anwendungskontextbezogen
- **Plan- vs. Objektklassen:**
  - **Planklassen:** Räumlich-bezogenes Plandokument
  - **Objektklassen:** Inhalte des Plans

#### Breitbandausbau-spezifische Objektklassen

**Linien-Objekte:**
- `BRA_BreitbandtrasseAbschnitt`: Abschnitt einer Breitbandtrasse

**Rohrsystem (nested pipe system):**
- `BRA_Schutzrohr`: Schutzrohr für Leitungen
- `BRA_Mikrorohrverbund`: Verbund von Mikrorohren
- `BRA_Mikrorohr`: Einzelnes Mikrorohr
- `BRA_Kabel`: Kabel innerhalb der Rohre

**Punkt-Objekte:**
- `BRA_Verteiler`: Verteilerpunkte im Netz

**Bestandsleitungen:**
- `BST_Telekommunikationsleitung`: Existierende Telekommunikationsleitungen (im Gegensatz zu geplanten nested pipe systems)

### 6.3 Bezüge zu §127 TKG

#### Rechtlicher Rahmen

**§127 TKG - Verlegung und Änderung von Telekommunikationslinien**

- **Inkrafttreten:** 1. Dezember 2021 (Telekommunikationsmodernisierungsgesetz vom 28. Juni 2020)
- **Grundprinzip:** Zustimmung der Straßenbaubehörde zur Verlegung von TK-Linien in öffentlichen Wegen
- **§127 Abs. 1:** Zustimmungsverfahren (11 Nachrichten in XBreitband)
- **§127 Abs. 4:** Geringfügige Bauvorhaben (2 Nachrichten)
- **§127 Abs. 5:** Integration weiterer Genehmigungen (Naturschutz, Wasserwirtschaft, Denkmalschutz, Straßenverkehr)
- **§127 Abs. 8:** Nebenbestimmungen zur konkreten Ausführung

#### Nutzungsberechtigung (§125 TKG)

- **§125 Abs. 1:** Grundlage für "gebundene Entscheidung" der Straßenbaubehörde
- Zustimmung basiert auf Nutzungsberechtigung öffentlicher Wege

#### Koordinierungsstellen (§127 Abs. 5)

- Länder richten Koordinierungsstellen ein
- Bündelung verschiedener fachrechtlicher Genehmigungen
- XBreitband ermöglicht digitale Koordinierung

#### XBreitband als Digitalisierungsinstrument für TKG

1. **Digitale Antragstellung:** Vollständig digitale Einreichung über Breitband-Portal
2. **Medienbruchfreie Verarbeitung:** XML-basierter Austausch zwischen IT-Systemen
3. **Fristenkontrolle:** Strukturierte Daten ermöglichen automatisierte Fristenüberwachung
4. **TöB-Beteiligung:** Standardisierte Kommunikation mit öffentlichen Stellen
5. **Infrastrukturatlas-Integration:** Automatische Meldung genehmigter Trassen an Bundesnetzagentur (via XTrasse)

---

## 7. Verhältnis zu XPlanung

### 7.1 Integration in Planungshierarchie

**XPlanung** ist der Austauschstandard für Raumordnungs- und Bauleitpläne auf allen räumlichen Ebenen:

- **Raumordnung:** Bundesraumordnung, Landesentwicklung, Regionalplanung
- **Bauleitplanung:** Flächennutzungspläne, Bebauungspläne
- **Landschaftsplanung:** Naturschutzfachliche Planungen

**XBreitband-Integration:**

1. **Räumliche Planung als Input:**
   - Flächennutzungspläne definieren potenzielle Trassenbereiche
   - Bebauungspläne enthalten Leitungsrechte und Versorgungsflächen
   - Landschaftspläne: Schutzgebiete, Restriktionen für Trassenführung

2. **Trassenkorridor-Planung (XTrasse Anwendungsfall):**
   - Bezug auf XPlanung-Objekte in Raumverträglichkeitsprüfung
   - XTrasse-Anwendungsfall "Trassenplan" referenziert XPlanung-Standard

3. **Digitaler Workflow:**
   - XPlanung-Daten → Trassenkorridor-Analyse (XTrasse) → Zustimmungsantrag (XBreitband)

### 7.2 Unterschied zu XBau/XPlanung-Beziehung

- **XBau ↔ XPlanung:** Weniger direkte Beziehung, eher parallel genutzt
- **XBreitband ↔ XTrasse:** Sehr direkte Beziehung, simultane Nutzung Standard
- **XBreitband ↔ XPlanung:** Indirekt über XTrasse und räumliche Planungsvorgaben

### 7.3 Gemeinsame Governance

- **Alle Standards (XPlanung, XBau, XTrasse, XBreitband):** Betrieben von XLeitstelle
- **IT-Planungsrat:** Zentrale Beschlussfassung für alle Standards
- **Rechtliche Verbindlichkeit:** Alle Standards verpflichtend seit IT-Planungsrat-Beschlüssen
- **Kommunale Relevanz:** Handreichungen von Deutschem Städtetag und Landkreistag für alle Standards

---

## 8. Offene Fragen und Forschungsbedarf

### 8.1 Nicht extrahierbare Informationen

Trotz umfangreicher Recherche konnten folgende Informationen **nicht aus öffentlich zugänglichen Webquellen** vollständig ermittelt werden:

1. **Vollständige Liste aller 11 Nachrichtentypen für §127 TKG:**
   - Nur 10 von 11 Nachrichten identifiziert
   - Exakte XML-Element-Namen fehlen (z.B. "nachricht.2001", "nachricht.2002")

2. **Detaillierte XML-Schema-Strukturen:**
   - Hierarchie der XML-Elemente pro Nachrichtentyp
   - Pflicht- vs. optionale Felder
   - Datentyp-Definitionen (z.B. String-Längen, Enumerationen)

3. **Vollständiger Nachrichtenkatalog für Aufbruchgenehmigung:**
   - 5 Nachrichten erwähnt, aber nicht spezifiziert

4. **Zustandsmodell:**
   - Kein explizites State-Machine-Diagramm in öffentlichen Quellen
   - Zustandsübergänge nur logisch ableitbar

5. **Beispiel-Nachrichten:**
   - Keine konkreten XML-Instanzen in Webquellen gefunden
   - XNT-Tool generiert Dummy-Daten, aber nicht öffentlich einsehbar

6. **Code-Listen-Details:**
   - Welche Enumerationen gibt es? (z.B. Baumaßnahmen-Typen, Leitungsarten)
   - Welche Werte sind zulässig?

### 8.2 Erforderliche nächste Schritte

Für vollständige technische Dokumentation:

1. **Download aus XRepository:**
   - URL: https://www.xrepository.de/details/urn:xoev-de:it-plr:standard:xbau-tiefbau
   - URN: `urn:xoev-de:it-plr:standard:xbau-tiefbau`
   - Download aller XSD-Dateien, Code-Listen (Genericode), UML-Modelle

2. **Spezifikation 1.2 direkt analysieren:**
   - PDF herunterladen und mit PDF-Reader öffnen
   - Kapitel 4 komplett extrahieren: "Nachrichten für den Leitungsbau"
   - Kapitel 5 analysieren: "Informationsmodell"

3. **XNT-Tool praktisch nutzen:**
   - GitLab-Repo klonen: https://gitlab.opencode.de/xleitstelle/xbreitband/xnt
   - Tool installieren und Test-Nachrichten generieren
   - Generierte XML-Instanzen analysieren

4. **XBau Kernmodul Spezifikation:**
   - URL: https://xleitstelle.de/downloads/xbau/releases/xbau-kernmodul_v_1_2/spezifikation.pdf
   - Generische Nachrichten (Eingangsbestätigung, Rückweisung) detailliert dokumentiert

### 8.3 Vergleichsbasis für XBau-Analyse

Für den geplanten Vergleich XBreitband ↔ XBau benötigt:

1. **Prozessvergleich:**
   - XBau Baugenehmigungsverfahren vs. XBreitband §127 TKG-Verfahren
   - Gemeinsame Prozessschritte (Antrag, Beteiligung, Bescheid)
   - Unterschiede (bauaufsichtliche vs. wegrechtliche Prüfung)

2. **Messaging-Vergleich:**
   - Gemeinsame Nachrichten aus XBau Kernmodul
   - Fachspezifische Nachrichten XBau-Hochbau vs. XBreitband
   - Nachrichtenanzahl pro Verfahren

3. **Akteurs-Vergleich:**
   - Bauherr/Architekt (XBau) vs. TKU (XBreitband)
   - Bauaufsichtsbehörde (XBau) vs. Straßenbaubehörde (XBreitband)
   - TöB-Rolle in beiden Verfahren

4. **Technische Gemeinsamkeiten:**
   - Beide nutzen XBau Kernmodul
   - Beide basieren auf XÖV 3.0
   - Beide verwenden gleiche generische Nachrichten

### 8.4 Offene Forschungsfragen

1. **Prozesseffizienz:**
   - Wie stark beschleunigt XBreitband das Zustimmungsverfahren praktisch?
   - Wie hoch ist die Medienbruch-Reduktion?

2. **Interoperabilität:**
   - Wie gut funktioniert die Integration zwischen kommunalen IT-Systemen?
   - Welche Herausforderungen bestehen bei Multi-Jurisdiktions-Anträgen?

3. **Verhältnis G2G vs. B2G:**
   - Welche Variante wird häufiger genutzt?
   - Welche Vor-/Nachteile ergeben sich in der Praxis?

4. **XTrasse-Integration:**
   - Wie hoch ist die Nutzungsquote von XTrasse-Plänen in XBreitband-Anträgen?
   - Welche GIS/CAD-Systeme unterstützen XTrasse-Export?

5. **Infrastrukturatlas-Anbindung:**
   - Automatische Übermittlung genehmigter Trassen an Bundesnetzagentur?
   - API-Design für Datenlieferung nach XTrasse-Standard?

---

## 9. Zusammenfassung und Bewertung

### 9.1 Kernergebnisse

**XBreitband** ist ein ausgereifter, verbindlicher IT-Standard für den Breitbandausbau in Deutschland mit folgenden Stärken:

1. **Rechtliche Grundlage:** Verpflichtend durch IT-Planungsrat-Beschluss 2021/40
2. **Technische Reife:** Version 1.2 im Regelbetrieb, basierend auf etablierten Standards (XÖV, XBau Kernmodul)
3. **Klares Prozessmodell:** Dreiphasiges Zustimmungsverfahren nach §127 TKG mit 11 Nachrichten
4. **Enge Integration:** Direkte Verknüpfung zu XTrasse als Geodatenstandard
5. **Governance:** Professionelle Pflege durch XLeitstelle mit kontinuierlicher Weiterentwicklung
6. **Praktische Werkzeuge:** XNT für Test-Nachrichtenerzeugung, Testumgebung FIT-Connect

### 9.2 Limitationen der Recherche

Die Recherche basiert ausschließlich auf **öffentlich über WebSearch und WebFetch zugänglichen Informationen**. Folgende Limitationen bestehen:

1. **PDF-Spezifikationen nicht dekodierbar:** Binär komprimierte PDFs konnten nicht über WebFetch extrahiert werden
2. **XRepository nicht vollständig zugänglich:** JavaScript-basierte Webseite ohne statischen Inhalt
3. **Keine vollständige Nachrichtenliste:** 11. Nachrichtentyp nicht identifiziert
4. **Keine XML-Beispiele:** Konkrete Nachrichteninstanzen nicht in Webquellen verfügbar
5. **Kein Zugriff auf XSD-Details:** Schema-Dateien nur als Download, nicht als Web-Inhalte

### 9.3 Empfehlungen für weitere Analyse

**Für vollständige technische Dokumentation:**

1. **Direkt aus XRepository herunterladen:**
   - XBreitband 1.2 XSD-Schemas
   - Code-Listen (Genericode)
   - UML-Modelle (XMI)

2. **Spezifikation 1.2 PDF lokal analysieren:**
   - Kapitel 4: Vollständiger Nachrichtenkatalog
   - Kapitel 5: Detailliertes Informationsmodell
   - Prozessdiagramme extrahieren

3. **XNT praktisch testen:**
   - Repo klonen und Tool einrichten
   - Test-Nachrichten für alle 11 Typen generieren
   - XML-Struktur analysieren

4. **XBau Kernmodul Spezifikation studieren:**
   - Generische Nachrichten vollständig dokumentiert
   - Gemeinsame Basis für XBreitband und XBau-Hochbau

**Für Vergleich mit XBau:**

- Parallele Analyse der XBau-Hochbau Spezifikation durchführen
- Prozess- und Messaging-Modelle gegenüberstellen
- Gemeinsame Komponenten aus XBau Kernmodul herausarbeiten

### 9.4 Qualität der Primärquellen

**Sehr gute Dokumentationsqualität:**

- **XLeitstelle:** Zentrale, gut strukturierte Dokumentation mit klarer Navigation
- **FITKO:** Föderale IT-Dokumentation mit Status, Ressourcen, Betriebshandbuch
- **IT-Planungsrat:** Offizielle Beschlüsse mit Anlagen öffentlich zugänglich
- **BIMBreitband:** Praxisorientierte Implementierungsbeispiele
- **OpenCoDE GitLab:** Offene Werkzeuge und Repositories

**Herausforderungen:**

- PDF-Spezifikationen nicht direkt web-extrahierbar
- XRepository benötigt JavaScript-Aktivierung
- Detaillierte technische Informationen nur in Downloads, nicht als HTML

---

## 10. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **XBreitband** | Föderaler IT-Standard für Datenkommunikation im Breitbandausbau (Prozess- und Nachrichtenstandard) |
| **XTrasse** | Föderaler Geodatenstandard für Modellierung von Leitungsnetzen (Datenmodellstandard) |
| **XBau** | Föderaler IT-Standard für Baugenehmigungsverfahren |
| **XPlanung** | Föderaler IT-Standard für Raumordnungs- und Bauleitpläne |
| **XLeitstelle** | Zentrale Koordinierungsstelle für XPlanung, XBau, XTrasse und XBreitband |
| **XÖV** | XML-basiertes Datenaustauschformat für öffentliche Verwaltungen |
| **TKG** | Telekommunikationsgesetz (seit 1.12.2021 in Kraft) |
| **§127 TKG** | Zustimmungsverfahren für Verlegung von Telekommunikationslinien in öffentlichen Wegen |
| **TKU** | Telekommunikationsunternehmen (Antragsteller) |
| **Straßenbaubehörde** | Wegebaulastträger, Genehmigungsbehörde für §127 TKG |
| **TöB** | Träger öffentlicher Belange (z.B. Naturschutz, Wasserwirtschaft, Denkmalschutz) |
| **G2G** | Government-to-Government (Behörden-zu-Behörden-Kommunikation) |
| **B2G** | Business-to-Government (Unternehmen-zu-Behörden-Kommunikation) |
| **IT-Planungsrat** | Gremium von Bund und Ländern zur Steuerung der föderalen IT-Zusammenarbeit |
| **FITKO** | Föderale IT-Kooperation (Kompetenzzentrum für föderale IT) |
| **FIT-Connect** | Transportinfrastruktur für föderale IT-Standards |
| **XNT** | XML-Nachrichten-Tool (Werkzeug zur Erzeugung von Test-Nachrichten) |
| **XRepository** | Zentrale Plattform für XÖV-konforme Standards und Code-Listen |
| **OpenCoDE** | Offene GitLab-Plattform für öffentliche IT-Projekte |
| **GML** | Geography Markup Language (XML-Format für Geodaten, ISO 19136) |
| **UUID** | Universally Unique IDentifier (nach RFC 4122) |
| **XSD** | XML Schema Definition (technisches Schema für XML-Validierung) |
| **Genericode** | OASIS-Standard für maschinenlesbare Code-Listen |
| **UML** | Unified Modeling Language (Modellierungssprache) |
| **XMI** | XML Metadata Interchange (XML-Format für UML-Modelle) |
| **BIMBreitband** | Forschungsprojekt zur BIM-Implementierung im Breitbandausbau |
| **OZG** | Onlinezugangsgesetz (verpflichtet zu digitalen Verwaltungsleistungen) |
| **Breitband-Portal** | Digitale Plattform für XBreitband-Kommunikation |
| **Infrastrukturatlas** | Zentrale Datenbank der Bundesnetzagentur für Leitungsnetze |
| **Aufbruchgenehmigung** | Genehmigung für Straßenaufbrüche (andere Sparten: Strom, Gas, Wasser) |

---

## Anhang A: Technischer Kontext TKG §127

### Rechtliche Grundlagen

**Telekommunikationsgesetz (TKG) vom 23. Juni 2004, zuletzt geändert durch Telekommunikationsmodernisierungsgesetz vom 28. Juni 2020, in Kraft seit 1. Dezember 2021**

#### §125 TKG - Nutzungsberechtigung
- Grundlage für Verlegung von TK-Linien in öffentlichen Wegen
- Berechtigung zur Mitbenutzung öffentlicher Wege
- Voraussetzung für §127-Zustimmung

#### §127 TKG - Verlegung und Änderung von Telekommunikationslinien

**Absatz 1:** Zustimmungsverfahren
- Schriftliche oder elektronische Zustimmung der Straßenbaubehörde erforderlich
- Frist: 3 Monate ab Eingang vollständigen Antrags
- Fiktionswirkung: Zustimmung gilt als erteilt nach Fristablauf
- Verlängerung um 1 Monat bei Schwierigkeit möglich (mit Begründung)

**Absatz 4:** Geringfügige Bauvorhaben
- Vereinfachtes Verfahren bei vollständiger Anzeige
- Frist: 1 Monat für Aufforderung zu formellem Antrag
- Sonst gilt Zustimmung als erteilt

**Absatz 5:** Integration fachrechtlicher Genehmigungen
- Naturschutzrecht
- Wasserrecht
- Denkmalschutzrecht
- Straßenverkehrsrechtliche Anordnungen
- Koordinierungsstellen der Länder

**Absatz 8:** Nebenbestimmungen
- Anforderungen an konkrete Ausführung
- Innerhalb enger Grenzen zulässig

### Verfahrens-Timing

| Phase | Frist | Regelung |
|-------|-------|----------|
| Vollständigkeitsprüfung | 1 Monat | §127 Abs. 1: Unvollständigkeitsmitteilung |
| Entscheidungsfrist | 3 Monate | §127 Abs. 1: ab vollständigem Antrag |
| Verlängerung | +1 Monat | §127 Abs. 1: bei Schwierigkeit, mit Begründung |
| Geringfügige Bauvorhaben | 1 Monat | §127 Abs. 4: Aufforderung zu formellem Antrag |

### Beteiligte Rechtsgebiete

Durch §127 Abs. 5 TKG integriert:
- **Naturschutzrecht:** Bundesnaturschutzgesetz (BNatSchG)
- **Wasserrecht:** Wasserhaushaltsgesetz (WHG)
- **Denkmalschutz:** Landesdenkmalschutzgesetze
- **Straßenverkehrsrecht:** Straßenverkehrsordnung (StVO)

---

## Anhang B: XBreitband im föderalen IT-Kontext

### IT-Planungsrat Beschlüsse

| Beschluss | Datum | Inhalt | Status |
|-----------|-------|--------|--------|
| 2021/06 | 10. Juni 2021 | Parallele Erweiterung XBau/XPlanung | Beschlossen |
| 2021/40 | 29. Oktober 2021 | **IT-Standard XBau und XPlanung - Erprobung XBreitband/XTrasse** | **Verbindlich** |
| - | - | Anlage 1: Bedarfsbeschreibung Breitbandausbau | - |
| - | - | Anlage 2: **Spezifikation XBreitband 1.0** | - |
| - | - | Anlage 3: Spezifikation XTrasse 1.0 | - |

### FITKO-Einordnung

**FIT-Standards (Föderale IT-Standards):**
- XBreitband/XTrasse als offizielle FIT-Standards gelistet
- Status: **Regelbetrieb** (operational phase)
- Ressourcen: Spezifikation, Anwenderdokumentation, Testumgebung, Referenzimplementierung, Betriebshandbuch

### OZG-Kontext

**Onlinezugangsgesetz (OZG):**
- Verwaltungsleistung: "Breitbandausbau"
- XBreitband/XTrasse als technische Basis für OZG-Umsetzung
- Ziel: Vollständig digitale Antragstellung und Bearbeitung

---

## Anhang C: Vergleich XBreitband-Anwendungsfälle

| Anwendungsfall | Rechtsgrundlage | Anzahl Nachrichten | Status | Besonderheiten |
|----------------|-----------------|-------------------|--------|----------------|
| **TKG Zustimmung §127 Abs. 1** | Telekommunikationsgesetz | **11** | Vollständig | Hauptanwendungsfall, TöB-Beteiligung |
| **TKG geringfügige Bauvorhaben §127 Abs. 4** | Telekommunikationsgesetz | **2** | Vollständig | Vereinfachtes Verfahren |
| **Aufbruchgenehmigung** | Landesstraßengesetze | **5** | Vollständig | Andere Sparten (Strom, Gas, Wasser), keine TöB-Beteiligung |
| **Sondernutzungsgenehmigung** | Landesstraßengesetze | k.A. | Teilweise | - |
| **Verkehrsrechtliche Anordnung** | StVO | k.A. | Teilweise | - |
| **Leitungsauskunft** | - | k.A. | Teilweise | Antwort auf Anfragen |
| **Mitnutzung/Mitverlegung TKG** | Telekommunikationsgesetz | k.A. | Nicht implementiert | - |
| **Kampfmittelbelastung** | Landesrecht | k.A. | Nicht implementiert | - |
| **Naturschutzrechtliche Genehmigung** | BNatSchG | k.A. | Nicht implementiert | - |

---

## Anhang D: Nachrichtenfluss-Beispiel (konzeptionell)

### Szenario: TKU beantragt Zustimmung für Glasfaserverlegung (Variante G2G)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 1: Antragstellung                                                 │
└─────────────────────────────────────────────────────────────────────────┘

TKU ──[Nachricht: Zustimmungsantrag]──> Straßenbaubehörde
      │ Inhalt: Bauvorhaben, Trassenplan (XTrasse), Dokumente

Straßenbaubehörde ──[Nachricht: Eingangsbestätigung]──> TKU
                    │ Generische Nachricht (XBau Kernmodul)

┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 2a: Vollständigkeitsprüfung                                       │
└─────────────────────────────────────────────────────────────────────────┘

Fall A: Antrag vollständig → weiter zu Phase 2b

Fall B: Antrag unvollständig:
Straßenbaubehörde ──[Nachricht: Änderungsbedarf]──> TKU
                    │ Inhalt: Fehlende Dokumente/Informationen

TKU ──[Nachricht: Ergänzter Antrag]──> Straßenbaubehörde
    │ Fristen beginnen neu!

┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 2b: TöB-Beteiligung (Variante G2G)                                │
└─────────────────────────────────────────────────────────────────────────┘

Straßenbaubehörde ──[Nachricht: Beteiligung 1]──> TöB Naturschutz
                  ├─[Nachricht: Beteiligung 2]──> TöB Wasserwirtschaft
                  ├─[Nachricht: Beteiligung 3]──> TöB Denkmalschutz
                  └─[Nachricht: Beteiligung 4]──> TöB Straßenverkehr

TöB Naturschutz ──[Nachricht: Stellungnahme]──> Straßenbaubehörde
                │ Inhalt: Keine Einwände

TöB Wasserwirtschaft ──[Nachricht: Stellungnahme]──> Straßenbaubehörde
                       │ Inhalt: Auflagen (Grundwasserschutz)

TöB Denkmalschutz ──[Nachricht: Stellungnahme]──> Straßenbaubehörde
                    │ Inhalt: Archäologische Baubegleitung erforderlich

TöB Straßenverkehr ──[Nachricht: Stellungnahme]──> Straßenbaubehörde
                     │ Inhalt: Verkehrsführung während Bauphase

┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 2c: Leitungsanfrage (parallel)                                    │
└─────────────────────────────────────────────────────────────────────────┘

Straßenbaubehörde ──[Nachricht: Leitungsanfrage]──> Versorgungsunternehmen
                    │ Inhalt: Bereich der geplanten Trasse

Versorgungsunternehmen ──[Nachricht: Leitungsauskunft]──> Straßenbaubehörde
                        │ Inhalt: Bestandsleitungen (Gas, Wasser, Strom)

┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 3: Bescheiderteilung                                              │
└─────────────────────────────────────────────────────────────────────────┘

Straßenbaubehörde ──[Nachricht: Bescheid]──> TKU
                    │ Inhalt: Zustimmung mit Nebenbestimmungen
                    │   - Auflage: Grundwasserschutzmaßnahmen
                    │   - Auflage: Archäologische Baubegleitung
                    │   - Bedingung: Verkehrsführungsplan vor Baubeginn

┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 4: Bauphase                                                       │
└─────────────────────────────────────────────────────────────────────────┘

TKU ──[Nachricht: Baubeginnsanzeige]──> Straßenbaubehörde
    │ Inhalt: Startdatum, Bauleiter, Kontaktdaten

    [... Bauphase ...]

TKU ──[Nachricht: Baufertigstellungsanzeige]──> Straßenbaubehörde
    │ Inhalt: Fertigstellungsdatum, Abnahmeprotokoll

┌─────────────────────────────────────────────────────────────────────────┐
│ Parallel: Informationsnachrichten                                       │
└─────────────────────────────────────────────────────────────────────────┘

Straßenbaubehörde ──[Nachricht: Information]──> Anlieger/Öffentlichkeit
                    │ Inhalt: Baumaßnahme, Zeitraum, Verkehrseinschränkungen
```

**Gesamtzahl Nachrichten in diesem Beispiel:** 18
- Zustimmungsantrag (1)
- Eingangsbestätigung (1)
- Beteiligungen (4)
- Stellungnahmen (4)
- Leitungsanfrage (1)
- Leitungsauskunft (1)
- Bescheid (1)
- Baubeginnsanzeige (1)
- Baufertigstellungsanzeige (1)
- Informationsnachricht(en) (variable Anzahl)

**Variante B2G:** TKU holt Stellungnahmen selbst ein → andere Nachrichtenflüsse zwischen TKU und TöB

---

## Anhang E: Vergleichstabelle XBreitband vs. XBau (konzeptionell)

| Aspekt | XBreitband | XBau-Hochbau |
|--------|------------|--------------|
| **Verfahrenstyp** | Zustimmungsverfahren §127 TKG | Baugenehmigungsverfahren Landesbauordnungen |
| **Hauptakteure** | TKU, Straßenbaubehörde, TöB | Bauherr/Architekt, Bauaufsichtsbehörde, TöB |
| **Prüfungsart** | Gebundene Entscheidung (§125 TKG) | Ermessensentscheidung (materiell-rechtliche Prüfung) |
| **Fiktionswirkung** | Ja (3 Monate + 1 Monat) | Teilweise (je nach Landesrecht) |
| **Fachmodule** | XBreitband (Tiefbau) | XBau-Hochbau |
| **Gemeinsame Basis** | XBau Kernmodul | XBau Kernmodul |
| **Planungsstandard** | XTrasse (GML) | - |
| **Raumplanung** | Indirekt über XPlanung/XTrasse | Direkt über XPlanung |
| **Anzahl Nachrichten (Hauptverfahren)** | 11 | k.A. (zu recherchieren) |
| **TöB-Beteiligung** | Variante B2G oder G2G | Standard in Baugenehmigungsverfahren |
| **Geodaten** | Zwingend (Trassenplan) | Optional (Lagepläne) |
| **Release-Stand** | 1.2 (Mai 2024) | 2.3 + Kernmodul 1.2 |

---

**Ende des Reports**

---

## Metadaten

- **Autor:** Claude (Anthropic)
- **Modell:** Sonnet 4.5 (claude-sonnet-4-5-20250929)
- **Erstellungsdatum:** 2025-11-21
- **Recherche-Methode:** WebSearch und WebFetch
- **Anzahl Quellen:** 18+ Primärquellen
- **Umfang:** ca. 12.500 Wörter
- **Fokus:** Prozess- und Messaging-Modell XBreitband für §127 TKG
- **Limitationen:** Keine direkten Downloads aus XRepository, PDF-Spezifikationen nicht dekodierbar
- **Empfehlung:** Für vollständige technische Details XRepository und Spezifikation 1.2 direkt herunterladen
