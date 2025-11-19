---
layout: default
title: "XBau für Wärmenetze und Vergleich mit XBreitband"
parent: XBau
grand_parent: Standards
nav_exclude: true
permalink: /standards/xbau/xbau-waermenetze-vergleich-xbreitband-research/
---

# XBau für Wärmenetze und Vergleich mit XBreitband

## Zusammenfassung

**XBau** ist der gesetzlich vorgeschriebene Standard für die digitale Kommunikation in bauaufsichtlichen Verfahren in Deutschland. Für **Wärmenetze** ist die Anwendbarkeit von XBau jedoch **begrenzt**, da Fernwärmeleitungen in der Regel nicht dem Bauordnungsrecht, sondern dem **Planfeststellungsverfahren** unterliegen.

**Kernerkenntnisse:**

1. **XBau-Hochbau**: Fokus auf Hochbauprojekte (Gebäude, Anbauten, Umbauten) - **direkt relevant** für Heizungsanlagen in Gebäuden und Wärmeübergabestationen
2. **Planfeststellung für Fernwärmeleitungen**: Externe Fernwärmeleitungen benötigen **Planfeststellung oder Plangenehmigung** nach UVPG, nicht Baugenehmigung nach Bauordnungsrecht
3. **XBau-Kernmodul**: Bildet die gemeinsame Basis für XBau-Hochbau **und** XBreitband - modulare Architektur ermöglicht Wiederverwendung
4. **Vergleich mit XBreitband**: Beide sind Nachrichtenstandards, nutzen das gleiche Kernmodul, adressieren aber unterschiedliche Genehmigungsverfahren

**Relevanz für Wärmewende:**
- XBau ist **direkt relevant** für gebäudebezogene Wärmetechnik (Heizungsanlagen, Wärmeübergabestationen)
- Für Fernwärmenetzausbau ist XBau **nicht anwendbar** - hier greift Planfeststellungsrecht
- Potenzial für **XBau-Fachmodul "Planfeststellung"** analog zu XBau-Hochbau und XBreitband

## Kontext und Hintergrund

### Was ist XBau?

**XBau** ist der **föderale IT-Standard für die Kommunikation zwischen den Beteiligten in bauaufsichtlichen Verfahren**. Er definiert Strukturen und Inhalte aller Nachrichten, die erforderlich sind, um die Prozesse in den jeweiligen Verfahren von der Antragstellung bis zur Bescheiderteilung abzubilden.

**Entwicklung:**
- **Entwicklungsbeginn**: Parallel zu XPlanung (ab ca. 2003)
- **IT-PLR-Beschluss**: 5. Oktober 2017 (Beschluss 2017/37)
- **Verbindlich seit**: 8. Februar 2018
- **Übergangsfrist bis**: 8. Februar 2023 (5 Jahre)
- **Aktuelle Version**: XBau 2.4 (XBau-Hochbau) + XBau-Kernmodul 1.2

**Rechtsgrundlage:**
- IT-Staatsvertrag und IT-Planungsrat-Vertrag
- Onlinezugangsgesetz (OZG) - digitale Verwaltungsleistungen
- Musterbauordnung (MBO) als fachliche Basis

### Modulare Struktur seit Version 2.3

Ab XBau Version 2.3 (März 2022) wurde der Standard in eine **modulare Architektur** umstrukturiert:

**1. XBau-Kernmodul**
- Enthält allgemein verwendbare Datentypen und Nachrichten generischen Charakters
- Wiederverwendbar über verschiedene Standards hinweg
- Basis für XBau-Hochbau **und** XBreitband

**2. Fachmodule**
- **XBau-Hochbau**: Spezialisiert auf Hochbauprojekte und Bauordnungsrecht
- **XBreitband**: Spezialisiert auf Breitbandausbau (nutzt ebenfalls das Kernmodul)
- **Weitere Module möglich**: Architektur erlaubt zukünftige Fachmodule (z.B. Planfeststellung)

**Vorteil der Modularisierung:**
> "Die beiden Standards XBau-Hochbau und XBreitband können nun nicht nur separat eingesetzt, sondern auch unabhängig voneinander versioniert und weiterentwickelt werden."

## XBau-Hochbau: Der Baugenehmigungs-Standard

### Anwendungsbereich

**XBau-Hochbau** deckt die digitale Kommunikation in **bauaufsichtlichen Verfahren** ab:

**Verfahrenstypen:**
- Baugenehmigungsverfahren (Genehmigung, Freistellung, Abweichung, Vorbescheid)
- Informationsaustauschprozesse (Anzeigen, Beteiligungen, Mitteilungen)
- Antragstellung bis Bescheiderteilung

**Standardisierte Daten:**
- Antragsdaten
- Projektbeschreibungen
- Beteiligte
- Bauunterlagen
- Verfahrensstatus
- Statistische Auswertungen

### Technische Basis

**Grundlage:**
- **Musterbauordnung (MBO)** - bundesweites Referenzmodell
- **Landesbauordnungen** - länderspezifische Anpassungen möglich

**Version 2.2** (November 2020):
> "Integriert Informationen aus länderspezifischen Antragsformularen zur Verbesserung der praktischen Nutzbarkeit"

**Aktuelle Version 2.4**: Über 50 Änderungen und Erweiterungen, darunter:
- Neue Verfahren für Grundstücksteilung
- Fertigstellungsanzeige
- Bauberatung
- Vervollständigung der Baustatistik-Nachrichten

### Relevanz für Wärmenetze - Gebäudebezug

**Direkt relevant für:**

1. **Heizungsanlagen in Gebäuden**
   - Installation neuer Heizungsanlagen (Wärmepumpen, Gasthermen, etc.)
   - Umstellung von fossilen auf erneuerbare Heizsysteme
   - Genehmigungspflichtige Änderungen an Heizungsanlagen

2. **Wärmeübergabestationen**
   - Anschluss von Gebäuden an Fernwärmenetze
   - Installation von Wärmeübergabestationen (Hausanschlussstationen)
   - Technische Räume für Fernwärme-Equipment

3. **Energetische Sanierung**
   - Genehmigungen für umfassende energetische Gebäudesanierungen
   - Fassadendämmung, Fenster, Dach (mittelbar relevant für Wärmebedarf)
   - Integration von Solarthermie-Anlagen

4. **Wärmeerzeugungsanlagen**
   - Blockheizkraftwerke (BHKW) in/an Gebäuden
   - Holzheizungen, Pelletöfen
   - Wärmespeicher

**Genehmigungsprozess über XBau:**
- Digitaler Bauantrag mit Beschreibung der Heizungsanlage
- Einbindung von Fachplanern (TGA, Energieberater)
- Beteiligung von Schornsteinfeger, Immissionsschutz
- Digitale Bescheiderteilung

### Nicht abgedeckt: Fernwärmeleitungen

**Wichtige Abgrenzung:**
XBau-Hochbau ist **nicht anwendbar** auf externe Fernwärmeleitungen, da diese:
- **Nicht dem Bauordnungsrecht unterliegen**
- **Planfeststellungsverfahren** nach UVPG benötigen
- Von Kreisverwaltungsbehörden (nicht Bauämtern) genehmigt werden

## Planfeststellung für Fernwärmeleitungen

### Rechtlicher Rahmen

**Externe Fernwärmeleitungen bedürfen in der Regel der Planfeststellung oder Plangenehmigung durch die zuständige Kreisverwaltungsbehörde.**

**Gesetzliche Grundlage:**
- **§§ 65-67 UVPG** (Gesetz über die Umweltverträglichkeitsprüfung)
- Planfeststellung mit UVP oder Plangenehmigung erforderlich

**Voraussetzungen:**
- Rohrleitungsanlagen zum Befördern von Dampf oder Warmwasser
- Überschreiten des Bereichs eines Werksgeländes
- **Länge ≥ 5 km** außerhalb des Werksgeländes **oder**
- Lage im Außenbereich

**Zuständige Behörde:**
- **Kreisverwaltungsbehörde** (Landratsamt, kreisfreie Stadt)
- **Nicht** die Bauaufsichtsbehörde

### Unterschiede zum Baugenehmigungsverfahren

| Aspekt | Baugenehmigung (XBau) | Planfeststellung (Fernwärme) |
|--------|----------------------|------------------------------|
| **Rechtsgrundlage** | Landesbauordnung | UVPG, Fachplanungsgesetze |
| **Zuständigkeit** | Bauaufsichtsbehörde | Kreisverwaltungsbehörde |
| **Verfahren** | Bauordnungsrechtlich | Planungsrechtlich |
| **Gegenstand** | Gebäude, bauliche Anlagen | Lineare Infrastruktur |
| **Umweltprüfung** | i.d.R. nicht erforderlich | UVP bei ≥5 km |
| **Beteiligung** | Nachbarn, Fachbehörden | Öffentlichkeit, TÖB |
| **Standard** | **XBau-Hochbau** | **Kein digitaler Standard** |

### Genehmigungspraxis für Fernwärmeleitungen

**Aktueller Stand (2025):**
- **Keine Standardisierung** der Planfeststellungsverfahren für Fernwärme
- **Medienbrüche** zwischen Antragstellern und Behörden
- **Papierbasierte** oder PDF-basierte Einreichung
- **Keine XBau-Anwendung**, da außerhalb des Bauordnungsrechts

**Verfahrensablauf:**
1. **Antragstellung** beim Landratsamt/kreisfreier Stadt
2. **Einreichung von Planunterlagen** (Trassenverläufe, technische Beschreibung)
3. **Beteiligung** von Trägern öffentlicher Belange (TÖB)
4. **Öffentliche Auslegung** (bei UVP-Pflicht)
5. **Planfeststellungsbeschluss** oder Plangenehmigung
6. **Rechtsmittelfrist** und anschließende Bestandskraft

**Fristen gemäß Wärmeplanungsgesetz:**
> "Für Projekte mit Wärmenetzen müssen alle nach Landesrecht erforderlichen Genehmigungen bis zum 31. Dezember 2026 vorliegen, und das Wärmenetz muss bis zum Ende des vierten Jahres nach der letzten erforderlichen landesrechtlichen Genehmigung in Betrieb genommen werden."

### Wegenutzungsverträge und Gestattungsverträge

**Parallel zu Planfeststellung:**

**Wegenutzungsverträge** sind privatrechtliche Verträge, durch die Kommunen Unternehmen das Recht einräumen, ihre Straßen zur Verlegung von Versorgungsleitungen zu nutzen.

**Für Fernwärmeleitungen:**
- Lange als **Gestattungsverträge** bezeichnet
- Regelung der technischen und finanziellen Modalitäten
- Unabhängig von Planfeststellung, aber oft vorausgesetzt
- **AGFW (Energieeffizienzverband für Wärme, Kälte und KWK e.V.)** bietet Musterverträge

## XBau-Kernmodul: Die gemeinsame Basis

### Inhalt und Zweck

Das **XBau-Kernmodul** enthält **"allgemein verwendbare Datentypen und Nachrichten generischen Charakters"**, die über verschiedene Standards hinweg wiederverwendbar sind.

**Kernkomponenten:**

1. **G2G-Nachrichtenstruktur** (Government-to-Government)
   - Nachrichtenheader mit Identifikation, Leser, Autor
   - Nachrichtenidentifizierung
   - Ablehnungsnachrichten zur Fehlersignalisierung

2. **Querschnittsnachrichten**
   - Prozessübergreifende Nachrichten
   - Statusmeldungen
   - Anfragen und Antworten

3. **Basisdatentypen**
   - Adressen
   - Personen und Organisationen
   - Flurstücke und geografische Bezüge
   - Anhänge (Metadaten und Strukturen)

4. **Querschnitts-Codelisten**
   - Bundesländer
   - Gemeinden
   - Standardisierte Wertelisten

**Vorteil:**
> "Das Kernmodul macht Datentypen wiederverwendbar, die von beiden Fachmodulen [XBau-Hochbau und XBreitband] genutzt werden, sowie einige Codelisten und fachlich nicht spezifische Nachrichten."

### Versionen

**Aktuelle Version**: XBau-Kernmodul 1.2 (16. Dezember 2022)

**Entwicklung:**
- **Version 1.1**: März 2022 (zusammen mit XBau 2.3)
- **Version 1.2**: Dezember 2022

**Nutzer des Kernmoduls:**
- XBau-Hochbau 2.3, 2.3.1, 2.4
- XBreitband 1.0, 1.2

## Vergleich: XBau vs. XBreitband

### Gemeinsamkeiten

Beide Standards sind **Nachrichtenstandards** (im Gegensatz zu XTrasse als Datenmodell) und teilen fundamentale Eigenschaften:

| Aspekt | XBau-Hochbau | XBreitband |
|--------|--------------|------------|
| **Typ** | Nachrichtenstandard | Nachrichtenstandard |
| **Kernmodul** | ✅ XBau-Kernmodul 1.2 | ✅ XBau-Kernmodul 1.2 |
| **Zweck** | Genehmigungsverfahren | Genehmigungsverfahren |
| **Nachrichtentypen** | Anträge, Bescheide, Beteiligungen | Anträge, Bescheide, Beteiligungen |
| **Rechtsgrundlage** | IT-PLR-Beschluss 2017 | IT-PLR-Beschluss 2021 |
| **XÖV-konform** | ✅ Ja | ✅ Ja |
| **Betreuung** | XLeitstelle Hamburg | XLeitstelle Hamburg |
| **Hosting** | XRepository | XRepository |

**Technische Gemeinsamkeiten:**
- Beide nutzen **XML-basierte Nachrichtenformate**
- Beide verwenden **XÖV-Standards** (XML-basierter Datenaustausch der öffentlichen Verwaltung)
- Beide haben **maschinenlesbare, herstellerunabhängige** Datenformate
- Beide ermöglichen **verlustfreien Datenaustausch** zwischen IT-Systemen
- Beide unterstützen **G2G-Kommunikation** (Behörde-zu-Behörde)

**Architektonische Gemeinsamkeiten:**
> "Seit zukünftigen Entwicklungsbedarfen im Kernmodul minimal sein werden, können die beiden Standards XBau-Hochbau und XBreitband nun nicht nur separat eingesetzt, sondern auch unabhängig voneinander versioniert und weiterentwickelt werden."

### Unterschiede

Trotz gemeinsamer technischer Basis unterscheiden sich die Standards grundlegend in ihrem **Anwendungsbereich**:

#### 1. Fachlicher Anwendungsbereich

| Kriterium | XBau-Hochbau | XBreitband |
|-----------|--------------|------------|
| **Gegenstand** | Hochbauprojekte (Gebäude) | Tiefbauprojekte (Leitungsverlegung) |
| **Rechtsgebiet** | Bauordnungsrecht (LBO) | Telekommunikationsgesetz (TKG), Straßenrecht |
| **Infrastruktur** | Gebäude, Anbauten, Umbauten | Breitbandleitungen, Glasfaserkabel |
| **Verfahren** | Baugenehmigung, Freistellung | TKG-Zustimmung, Straßengenehmigung |
| **Behörde** | Bauaufsichtsbehörde | Straßenbaubehörde, TKG-Behörde |

#### 2. Prozessuale Unterschiede

**XBau-Hochbau:**
- Fokus auf **Bauwerke** und **bauliche Anlagen**
- **Nachbarschaftsbeteiligung** gemäß Bauordnungsrecht
- **Baustatistik** als integraler Bestandteil
- **Fertigstellungsanzeige** und Abnahme

**XBreitband:**
- Fokus auf **lineare Infrastruktur** im öffentlichen Raum
- **Straßenrechtliche** Genehmigungen und Auflagen
- **Koordination** mit bestehenden Leitungen (Leitungsauskunft)
- **Baustellenverkehrsführung** und temporäre Maßnahmen

#### 3. Verbindlichkeit und Fristen

| Aspekt | XBau-Hochbau | XBreitband |
|--------|--------------|------------|
| **Beschluss** | IT-PLR 2017/37 (5.10.2017) | IT-PLR 2021/40 (29.10.2021) |
| **Übergangsfrist** | Bis 8.2.2023 (5 Jahre) | Bis 29.10.2026 (5 Jahre) |
| **Verpflichtung** | Alle IT-Systeme für Baugenehmigungen | IT-Systeme für TKG-Zustimmungsverfahren |
| **Weitere AF** | - | Straßenrecht (Pilot), weitere in Entwicklung |

#### 4. Inhaltliche Schwerpunkte

**XBau-Hochbau umfasst:**
- Bauantragsdaten (Bauherr, Grundstück, Bauvorhaben)
- Bauvorlagen (Pläne, Berechnungen, Nachweise)
- Beteiligungsverfahren (Fachbehörden, Nachbarn)
- Baustatistik
- Spezielle Verfahren (Grundstücksteilung, Abbruchanzeige)

**XBreitband umfasst:**
- 11 Nachrichten für TKG-Zustimmungsverfahren
- 5 Nachrichten für straßenrechtliche Genehmigungen
- Trassenplanung (verweist auf XTrasse)
- Leitungsauskunft (in Entwicklung)
- Verkehrsrechtliche Anordnungen (Pilot)

#### 5. Beziehung zu anderen Standards

**XBau-Hochbau:**
- Enge Verzahnung mit **XPlanung** (Bauleitplanung)
- Beteiligungsverfahren nutzen XPlanung-Pläne
- Beschleunigung von Planungs- und Genehmigungsverfahren

**XBreitband:**
- **Direkte funktionale Beziehung** zu XTrasse
- > "Ohne einen Trassenplan ist eine Antragsnachricht für den Breitbandausbau in der Regel nicht vollständig"
- Intentionale Redundanz: Gemeinsame Datenfelder für Workflow-Integration

### Modulare Architektur als strategischer Vorteil

Die Trennung in Kernmodul und Fachmodule ermöglicht:

1. **Unabhängige Weiterentwicklung**: XBau-Hochbau und XBreitband können getrennt versioniert werden
2. **Wiederverwendbarkeit**: Kernmodul-Datentypen stehen beiden Fachmodulen zur Verfügung
3. **Skalierbarkeit**: Weitere Fachmodule können entwickelt werden (z.B. XBau-Planfeststellung)
4. **Konsistenz**: Gemeinsame Basis-Nachrichtenstrukturen über alle Standards

## Relevanz für die Digitale Wärmewende

### Direkte Anwendbarkeit: Gebäudebezogene Wärmetechnik

**XBau-Hochbau ist unmittelbar relevant für:**

1. **Heizungsanlagen-Genehmigungen**
   - Digitaler Bauantrag für neue Heizungsanlagen
   - Standardisierte Kommunikation mit Bauaufsicht
   - Einbindung von Fachplanern (TGA, Energieberatung)
   - Schnellere Genehmigungsverfahren

2. **Gebäudeenergiegesetz (GEG) Compliance**
   - Ab 2024: 65% erneuerbare Energien für neue Heizungen
   - XBau kann GEG-Nachweise strukturiert übermitteln
   - Automatisierte Prüfung der Anforderungen
   - Verknüpfung mit Fördermittelantrag (BAFA)

3. **Wärmeübergabestationen**
   - Genehmigung von Hausanschlussstationen für Fernwärme
   - Technische Räume für Fernwärme-Equipment
   - Koordination mit Fernwärme-Versorgern

4. **Energetische Gebäudesanierung**
   - Umfassende Sanierungen mit XBau abwickeln
   - Fördermittel-relevante Nachweise digital übermitteln
   - Integration mit Energieausweis-Erstellung

**Workflow-Beispiel:**
1. Architekt erstellt digitalen Bauantrag mit XBau-konformer Software
2. Heizungsplaner fügt technische Unterlagen hinzu (Heizlastberechnung, Schema)
3. Einreichung bei Bauaufsichtsbehörde via XBau-Nachricht
4. Automatische Weiterleitung an Fachbehörden (Schornsteinfeger, Immissionsschutz)
5. Digitaler Bescheid mit Auflagen
6. Fertigstellungsanzeige via XBau
7. Abnahme und Freigabe

### Indirekte Relevanz: Planfeststellung für Fernwärmeleitungen

**XBau-Hochbau ist NICHT anwendbar auf:**
- Externe Fernwärmeleitungen (Planfeststellung nach UVPG)
- Fernwärme-Haupttrassen (übergeordnete Infrastruktur)
- Übergemeindliche Wärmenetze

**Aber**: Die XBau-Architektur bietet ein **Modell** für Standardisierung:

**Potenzial für "XBau-Planfeststellung" oder "XFernwärme":**

Analog zur Entwicklung von XBau-Hochbau und XBreitband könnte ein **Fachmodul für Planfeststellungsverfahren** entwickelt werden:

1. **Nutzung des XBau-Kernmoduls** als Basis
2. **Spezialisierung** auf Planfeststellung und Plangenehmigung
3. **Abdeckung** von Fernwärmeleitungen, aber auch anderen Infrastrukturen (Pipelines, Stromtrassen)
4. **Standardisierte Nachrichten** für:
   - Planfeststellungsantrag
   - Beteiligung von TÖB
   - Öffentliche Auslegung
   - Einwendungen und Stellungnahmen
   - Planfeststellungsbeschluss

**Vorteil:**
- Wiederverwendung bewährter Nachrichtenstrukturen
- Konsistenz mit XBau-Hochbau und XBreitband
- Beschleunigung von Planfeststellungsverfahren
- Digitale Souveränität für kritische Infrastruktur

### Methodische Relevanz: Best Practices

**XBau bietet übertragbare Ansätze:**

1. **Modulare Architektur**
   - Trennung von Kernmodul und Fachmodulen
   - Wiederverwendbarkeit von Datentypen
   - Unabhängige Versionierung

2. **Stakeholder-Einbindung**
   - Entwicklung basierend auf praktischen Anforderungen
   - Integration von länderspezifischen Formularen (XBau 2.2)
   - Iterative Verbesserung durch Implementierungsprojekte

3. **OZG-Konformität**
   - Digitale Verwaltungsleistungen
   - "One-for-all"-Portale (z.B. Mecklenburg-Vorpommern)
   - Vermeidung von 16 länderspezifischen Lösungen

4. **BIM-Integration**
   - XBau unterstützt Building Information Modeling
   - Digitale Abbildung des Lebenszyklus-Starts von Bauwerken
   - Potenzial für Integration mit BIM-Modellen

**Übertragung auf Wärmewende:**
- Koordination zwischen Bund, Ländern, Kommunen
- Standardisierung trotz föderaler Vielfalt
- Praktische Nutzbarkeit als Entwicklungsziel

## Externe Ressourcen und Weiterführende Links

### Offizielle XBau-Dokumentation

**XLeitstelle Hauptportale:**
- **XBau Übersicht**: [https://xleitstelle.de/xbau](https://xleitstelle.de/xbau)
- **Was ist XBau**: [https://xleitstelle.de/xbau/ueber_xbau](https://xleitstelle.de/xbau/ueber_xbau)
- **Mehrwert des Standards**: [https://xleitstelle.de/xbau/mehrwert-xbau](https://xleitstelle.de/xbau/mehrwert-xbau)
- **Releases XBau**: [https://xleitstelle.de/xbau/releases](https://xleitstelle.de/xbau/releases)
- **Änderungsmanagement**: [https://xleitstelle.de/xbau/aenderungsantraege](https://xleitstelle.de/xbau/aenderungsantraege)

**Spezifikationen:**
- **XBau 2.2 Spezifikation**: [https://xleitstelle.de/downloads/xbau/releases/xbau_v_2_2/spezifikation.pdf](https://xleitstelle.de/downloads/xbau/releases/xbau_v_2_2/spezifikation.pdf)
- **XBau 2.3 Spezifikation**: [https://xleitstelle.de/sites/default/files/releases/xbau/xbau_v_2_3/spezifikation_xbau_2-3.pdf](https://xleitstelle.de/sites/default/files/releases/xbau/xbau_v_2_3/spezifikation_xbau_2-3.pdf)
- **XBau 2.3.1 Diff**: [https://xleitstelle.de/downloads/xbau/releases/xbau_v_2_3_1/Diff_V2.3_V2.3.1.pdf](https://xleitstelle.de/downloads/xbau/releases/xbau_v_2_3_1/Diff_V2.3_V2.3.1.pdf)
- **XBau-Kernmodul 1.2 Spezifikation**: [https://xleitstelle.de/downloads/xbau/releases/xbau-kernmodul_v_1_2/spezifikation.pdf](https://xleitstelle.de/downloads/xbau/releases/xbau-kernmodul_v_1_2/spezifikation.pdf)

**Ankündigungen:**
- **XBau 2.3 und Kernmodul 1.1 Release**: [https://xleitstelle.de/node/104](https://xleitstelle.de/node/104)

### FITKO und Digitale Baugenehmigung

**FITKO:**
- **XBau Detailansicht**: [https://docs.fitko.de/fit-standards/xbau/](https://docs.fitko.de/fit-standards/xbau/)

**Digitale Baugenehmigung:**
- **XBau-Standard**: [https://www.digitale-baugenehmigung.de/de/xbaustandard.html](https://www.digitale-baugenehmigung.de/de/xbaustandard.html)
- **XBau-Nachrichten**: [https://www.digitale-baugenehmigung.de/de/xbaunachrichten.html](https://www.digitale-baugenehmigung.de/de/xbaunachrichten.html)

**OZG-Portal:**
- **Themenfeld Bauen & Wohnen**: [https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-foederal/themenfelder/bauen-und-wohnen/bauen-und-wohnen-node.html](https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-foederal/themenfelder/bauen-und-wohnen/bauen-und-wohnen-node.html)

### XRepository

**Standards:**
- **XBau-Kernmodul im XRepository**: [https://www.xrepository.de/details/urn:xoev-de:bmk:standard:xbau-kernmodul_1.1](https://www.xrepository.de/details/urn:xoev-de:bmk:standard:xbau-kernmodul_1.1)
- **XBau 2.0 Spezifikation**: [https://www.xrepository.de/api/xrepository/urn:xoev-de:bmk:standard:xbau_2.0:dokument:Spezifikation_XBau_2.0:datei:spezifikation.pdf](https://www.xrepository.de/api/xrepository/urn:xoev-de:bmk:standard:xbau_2.0:dokument:Spezifikation_XBau_2.0:datei:spezifikation.pdf)

### Rechtliche Grundlagen

**IT-Planungsrat:**
- **Rechtliche Verbindlichkeit (XLeitstelle)**: [https://xleitstelle.de/leitstelle/rechtliches](https://xleitstelle.de/leitstelle/rechtliches)

**Vergleich mit XBreitband:**
- **Bedarfsbeschreibung Breitbandausbau 1.0**: [https://xleitstelle.de/sites/default/files/2023-07/Bedarfsbeschreibung_Breitbandausbau_1.0.pdf](https://xleitstelle.de/sites/default/files/2023-07/Bedarfsbeschreibung_Breitbandausbau_1.0.pdf)
- **Standarderweiterung Planen & Bauen**: [https://xleitstelle.de/xtrassexbreitband/standarderweiterung](https://xleitstelle.de/xtrassexbreitband/standarderweiterung)

### Handreichungen

**Verbände:**
- **Handreichung XPlanung/XBau 2. Auflage (Städtetag)**: [https://www.staedtetag.de/files/dst/docs/Publikationen/Weitere-Publikationen/2020/handreichung-xplanung-xbau-2-auflage.pdf](https://www.staedtetag.de/files/dst/docs/Publikationen/Weitere-Publikationen/2020/handreichung-xplanung-xbau-2-auflage.pdf)
- **Handreichung XPlanung, XBau, XBreitband, XTrasse (Städtetag)**: [https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung](https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung)
- **Handreichung XPlanung 3. Auflage (Landkreistag)**: [https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage](https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage)

**Landesspezifisch:**
- **XPlanung und XBau Niedersachsen**: [https://www.geodaten.niedersachsen.de/startseite/kommunale_gdi/xplanung_xbau/xplanung-xplangml-und-xbau-fur-die-bauleitplanung-117461.html](https://www.geodaten.niedersachsen.de/startseite/kommunale_gdi/xplanung_xbau/xplanung-xplangml-und-xbau-fur-die-bauleitplanung-117461.html)

### Fernwärme und Planfeststellung

**AGFW (Energieeffizienzverband):**
- **Wegenutzungsverträge für Fernwärmeleitungen**: [https://www.agfw.de/energiewirtschaft-recht-politik/recht/wegenutzungsvertraege-fuer-fernwaermeleitungen](https://www.agfw.de/energiewirtschaft-recht-politik/recht/wegenutzungsvertraege-fuer-fernwaermeleitungen)

**Beispiele:**
- **Energie-Atlas Bayern - Genehmigung**: [https://www.energieatlas.bayern.de/thema_abwaerme/genehmigung](https://www.energieatlas.bayern.de/thema_abwaerme/genehmigung)
- **Bezirksregierung Münster - Rohrfernleitungsanlagen**: [https://www.bezreg-muenster.de/de/planen_und_bauen/versorgungsleitungen/rohrfernleitungsanlagen/index.html](https://www.bezreg-muenster.de/de/planen_und_bauen/versorgungsleitungen/rohrfernleitungsanlagen/index.html)

**Richtlinien:**
- **SWE Energie - Richtlinie Planung und Bauausführung Fernwärme**: [https://www.swe-energie.de/site/energie/get/documents_E651597608/energie/documents/Downloads/flyer-und-publikationen/waerme/richtlinie_planung_bauausf%C3%BChrung_fernwaerme.pdf](https://www.swe-energie.de/site/energie/get/documents_E651597608/energie/documents/Downloads/flyer-und-publikationen/waerme/richtlinie_planung_bauausf%C3%BChrung_fernwaerme.pdf)

### Weitere Quellen

**Architektur und Implementierung:**
- **Blog zu XPlanung als verbindlicher Standard**: [https://blog.archikart.de/ab-2023-ist-xplanung-verbindlicher-digitaler-standard-fuer-planungsverfahren](https://blog.archikart.de/ab-2023-ist-xplanung-verbindlicher-digitaler-standard-fuer-planungsverfahren)

## Zusammenfassung und Kernaussagen

### XBau für Wärmenetze

**Direkte Relevanz:**
- ✅ **Heizungsanlagen in Gebäuden** (Wärmepumpen, Gasthermen, BHKW)
- ✅ **Wärmeübergabestationen** für Fernwärme-Anschluss
- ✅ **Energetische Gebäudesanierung** mit Heizungstausch
- ❌ **Externe Fernwärmeleitungen** (Planfeststellung, nicht XBau)

**Rechtliche Situation:**
- XBau deckt **Bauordnungsrecht** ab (Gebäude)
- Fernwärmeleitungen unterliegen **Planfeststellungsrecht** (UVPG)
- **Kein digitaler Standard** für Planfeststellung von Fernwärmeleitungen

### Vergleich XBau vs. XBreitband

**Gemeinsamkeiten:**
- Beide sind **Nachrichtenstandards** (nicht Datenmodelle wie XTrasse)
- Beide nutzen **XBau-Kernmodul 1.2** als gemeinsame Basis
- Beide standardisieren **Genehmigungsverfahren**
- Beide sind **XÖV-konform** und **IT-PLR-verbindlich**

**Unterschiede:**
- **XBau-Hochbau**: Bauordnungsrecht, Gebäude, Bauaufsichtsbehörden
- **XBreitband**: TKG/Straßenrecht, Leitungen, TKG-/Straßenbehörden

**Architektur:**
Modulare Struktur (Kernmodul + Fachmodule) ermöglicht:
- Unabhängige Weiterentwicklung
- Wiederverwendbarkeit
- Potenzial für weitere Fachmodule (z.B. Planfeststellung)

### Strategisches Potenzial

**Lücke identifiziert:**
- Planfeststellungsverfahren für Fernwärmeleitungen **nicht standardisiert**
- Medienbrüche und Ineffizienz in kritischer Infrastruktur

**Lösungsansatz:**
- Entwicklung eines **XBau-Fachmoduls "Planfeststellung"** oder **"XFernwärme"**
- Nutzung der bewährten XBau-Architektur
- Integration in OZG-Leistungen

**Übertragbare Best Practices:**
- Modulare Architektur
- Stakeholder-Einbindung
- Praktische Nutzbarkeit als Leitprinzip

## Methodik dieser Research

**Recherche-Ansatz:**
- Primärquellen: XLeitstelle-Website, FITKO-Dokumentation
- Rechtliche Grundlagen: IT-PLR-Beschlüsse, UVPG, Bauordnungsrecht
- Technische Dokumentation: Spezifikationen (soweit PDF-zugänglich)
- Sekundärquellen: Verbände (AGFW), Landesbehörden
- Vergleichende Analyse: XBau vs. XBreitband

**Limitation:**
- PDF-Spezifikationen nur begrenzt maschinenlesbar
- Fokus auf öffentlich verfügbare Dokumentation
- Praktische Implementierungserfahrungen nicht direkt erfasst

**Informationsstand:**
November 2025 - Aktuelle Versionen: XBau 2.4, XBau-Kernmodul 1.2, XBreitband 1.2

---
*Recherche durchgeführt am: 2025-11-19*
*Letzte Aktualisierung: 2025-11-19*
