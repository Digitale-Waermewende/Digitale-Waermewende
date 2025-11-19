---
layout: default
title: "XLeitstelle GitLab Repository auf OpenCode"
parent: XPlanung
grand_parent: Standards
nav_exclude: true
permalink: /standards/xplanung/xleitstelle-gitlab-opencode-research/
---

# XLeitstelle GitLab Repository auf OpenCode

## Kontext und Hintergrund

### Die OpenCode-Plattform

**OpenCode** ist die zentrale Open-Source-Plattform der deutschen öffentlichen Verwaltung, betrieben durch das **ZenDiS (Zentrum für Digitale Souveränität der Öffentlichen Verwaltung)** im Auftrag des Bundesministeriums des Inneren (BMI).

**Zweck und Vision:**
- Zentrale Anlaufstelle für unabhängige Digitalisierung der deutschen Verwaltung
- Plattform für Verwaltungsmitarbeitende und Entwickler zur gemeinsamen Software-Entwicklung
- Förderung digitaler Souveränität durch Nutzung bewährter Open-Source-Lösungen
- Umsetzung nationaler IT-Architekturrichtlinien

**Gehostete Projekttypen:**
- E-Government-Lösungen (z.B. GA-Lotse für Gesundheitsämter)
- Smart-City-Anwendungen (z.B. Smart Village App)
- IT-Architektur-Projekte (z.B. OZG-Rahmenarchitektur)
- Geodaten- und Planungsstandards (z.B. XLeitstelle-Projekte)

**Standards:**
- Alle Projekte folgen Open Source Initiative Standards
- BSI-Grundschutzrichtlinien werden angewendet
- GitLab als Hosting-Infrastruktur

**Plattform-URL:** [https://opencode.de](https://opencode.de)

### Die XLeitstelle Planen und Bauen

**Organisatorische Einbindung:**
Die XLeitstelle Planen und Bauen ist beim **Landesbetrieb Geoinformation und Vermessung (LGV)** der Freien und Hansestadt Hamburg angesiedelt.

**Hauptaufgabe:**
Zentrale Fach- und Koordinierungsstelle für die kontinuierliche Pflege und Weiterentwicklung von vier bundesweiten Standards:
- **XPlanung** - Raumplanung und Bauleitplanung
- **XBau** - Baugenehmigungsverfahren
- **XTrasse** - Leitungsnetzplanung und Trassenführung
- **XBreitband** - Breitbandausbau

**Koordination:**
- Zusammenarbeit mit Bauministerkonferenz (BMKZ)
- Abstimmung mit Raumentwicklungsministerkonferenz (RMKZ)
- Integration in die deutsche Geodateninfrastruktur (GDI)

**Kontakt:**
- Adresse: Neuenfelder Straße 19, 21109 Hamburg
- E-Mail: xleitstelle@gv.hamburg.de
- Website: [https://xleitstelle.de](https://xleitstelle.de)

**Historischer Kontext:**
Die Entwicklung des semantischen Datenmodells und objektorientierten Datenaustauschformats begann 2003 und etablierte die Grundlage für digitale Standardisierung in Planungs- und Bauprozessen.

## Übersicht XLeitstelle GitLab-Gruppe

**GitLab-URL:** [https://gitlab.opencode.de/xleitstelle](https://gitlab.opencode.de/xleitstelle)

**Beschreibung:**
Die XLeitstelle nutzt die OpenCode-Plattform zur Veröffentlichung von Schemata, Skripten und Tools für die vier betreuten Standards. Art und Umfang der publizierten Ressourcen variieren je nach Standard.

**Organisationsstruktur:**
Die GitLab-Gruppe ist hierarchisch nach Standards organisiert:
- `xleitstelle/xplanung/` - XPlanung-Repositories
- `xleitstelle/xbau/` - XBau-Repositories (separate Gruppe)
- `xleitstelle/xtrasse/` - XTrasse-Repositories
- `xleitstelle/xbreitband/` - XBreitband-Repositories

## XPlanung-Repositories

### 1. XPlan-Tools

**URL:** [https://gitlab.opencode.de/xleitstelle/xplanung/xplan-tools](https://gitlab.opencode.de/xleitstelle/xplanung/xplan-tools)

**Zweck:**
Werkzeuge für Zugriff auf und Manipulation von XPlanung-Daten.

**Technische Details:**
- **Lizenz:** European Union Public License 1.2 (EUPL-1.2)
- **Aktivität:** 137 Commits auf Main-Branch
- **Branches:** 10 aktive Entwicklungszweige
- **Releases:** 26 veröffentlichte Versionen
- **Erstellung:** 1. Februar 2024
- **Status:** Aktiv gepflegt und weiterentwickelt

**Dokumentation:**
- README.md vorhanden
- CHANGELOG.md für Versionsnachverfolgung
- LICENSE.md mit vollständiger Lizenz

**Relevanz für Wärmewende:**
XPlan-Tools ermöglicht programmatischen Zugriff auf Bauleitpläne, die Wärmeplanungsgebiete und energetische Vorgaben enthalten können.

### 2. Testdaten

**URL:** [https://gitlab.opencode.de/xleitstelle/xplanung/testdaten](https://gitlab.opencode.de/xleitstelle/xplanung/testdaten)

**Zweck:**
Bereitstellung von Testdatensätzen für XPlanung-Implementierungen.

**Technische Details:**
- **Aktivität:** 16 Commits
- **Branches:** 1 Branch (Main)
- **Erstellung:** 27. November 2023
- **Status:** Früh-stadiges Projekt / Archiv

**Dokumentation:**
- README.md vorhanden

**Relevanz für Wärmewende:**
Testdaten sind essentiell für die Entwicklung und Validierung von Software, die XPlanung-Daten für Wärmeplanungszwecke verarbeitet.

### 3. Validierungsregeln / Standard

**URL:** [https://gitlab.opencode.de/xleitstelle/xplanung/validierungsregeln/standard](https://gitlab.opencode.de/xleitstelle/xplanung/validierungsregeln/standard)

**Zweck:**
Formale Validierungsregeln für XPlanung-Daten im Standardformat.

**Technische Details:**
- **Lizenz:** GNU LGPLv2.1
- **Aktivität:** 268 Commits auf Main-Branch
- **Branches:** 2 aktive Branches
- **Tags:** 42 Tags
- **Releases:** 16 veröffentlichte Versionen
- **Erstellung:** 7. September 2022
- **Status:** Etabliertes, aktiv gepflegtes Projekt

**Dokumentation:**
- README.md vorhanden
- CONTRIBUTING.md für Beitragsrichtlinien
- Integriertes Wiki
- Diskussionsforum aktiv

**Relevanz für Wärmewende:**
Validierungsregeln stellen sicher, dass XPlanung-Daten, die Wärmeplanungsinformationen enthalten, standardkonform und maschinell verarbeitbar sind.

## XTrasse-Repositories

### XTrasse - Hauptgruppe

**URL:** [https://gitlab.opencode.de/xleitstelle/xtrasse](https://gitlab.opencode.de/xleitstelle/xtrasse)

**Beschreibung:**
XTrasse ist ein Datenstandard für die Modellierung von Leitungsnetzen, der den verlustfreien Austausch vollvektorisierter georeferenzierter Pläne zwischen Versorgungsunternehmen und Verwaltung in Genehmigungsverfahren unterstützt.

**Standard-Historie:**
- **April 2024:** Veröffentlichung XTrasse 1.0 als neuer Standard
- **Status 2025:** Operativ und verpflichtender Geodatenstandard für Leitungspläne

**Anwendungsfälle XTrasse 2.0:**
1. Breitbandausbau
2. Planungsgenehmigung
3. Räumliche Verträglichkeitsprüfung
4. Infrastrukturflächenplanung
5. Bestandsinfrastrukturpläne
6. Infrastrukturatlas

**Basis:**
XTrasse basiert auf dem formal verbindlichen XPlanung-Geodatenstandard und ist speziell für Breitbandausbau-Anwendungsfälle erweitert.

### XTrasse / Spezifikation

**URL:** [https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation](https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation)

**Zweck:**
Offizielle Spezifikationsdokumentation des XTrasse-Standards.

### XTrasse / Anwendungen

**URL:** [https://gitlab.opencode.de/xleitstelle/xtrasse/anwendungen](https://gitlab.opencode.de/xleitstelle/xtrasse/anwendungen)

**Zweck:**
Referenzanwendungen und Tools für die Arbeit mit XTrasse-Daten.

**Relevanz für Wärmewende:**
XTrasse ist hochrelevant für Wärmenetze, da es den standardisierten Austausch von Leitungsnetzplänen (inkl. Fernwärmeleitungen) ermöglicht. Die räumliche Verträglichkeitsprüfung und Infrastrukturplanung sind zentral für kommunale Wärmeplanung.

## XBreitband-Repositories

### XBreitband - Hauptgruppe

**URL:** [https://gitlab.opencode.de/xleitstelle/xbreitband](https://gitlab.opencode.de/xleitstelle/xbreitband)

**Beschreibung:**
XBreitband ist der Nachrichtenstandard für Breitbandausbau-Prozesse, eine Erweiterung der XPlanung- und XBau-Standards.

**Standard-Entwicklung:**
- **IT-Planungsrat-Beschluss:** Erweiterung von XPlanung/XBau für Breitbandausbau-Anwendungsfälle
- **April 2024:** Release XBreitband 1.0
- **Aktuell (2025):** XBreitband 1.2

**Release-Inhalte XBreitband 1.2:**
- Spezifikation in PDF-Format mit allen Nachrichten und Datentypen
- XML-Schema-Dateien für Schnittstellenimplementierung
- Codelisten gemäß XBreitband-Definition
- Zugrundeliegendes UML-Modell

**Veröffentlichung:**
XBreitband wird im XRepository zur Bereitstellung XÖV-konformer Standards und Codelisten publiziert.

### XBreitband / XML-Nachrichten-Tool (XNT)

**URL:** [https://gitlab.opencode.de/xleitstelle/xbreitband/xnt](https://gitlab.opencode.de/xleitstelle/xbreitband/xnt)

**Zweck:**
Das XML-Nachrichten-Tool (XNT) liest XML-Schema-Dateien von XBreitband (sowie XBau, XBeteiligung, etc.) und unterstützt bei der Erstellung standardkonformer Nachrichten.

**Verfügbarkeit:**
- Bereitgestellt auf OpenCode-Plattform
- Auch als Testnachrichten-Werkzeug verfügbar

**Relevanz für Wärmewende:**
Indirekte Relevanz - die Tools und Prozesse für Breitbandausbau können als Best Practices für standardisierten Datenaustausch in der Wärmenetzplanung dienen.

## Services der XLeitstelle

Die XLeitstelle bietet über GitLab und die eigene Website verschiedene Services:

### 1. Standard-Spezifikation und Versionsverwaltung
- Kontinuierliche Pflege der Standards XPlanung, XBau, XTrasse, XBreitband
- Versionierte Releases auf GitLab
- Änderungsmanagement und Release-Dokumentation

### 2. Änderungsmanagement
- **JIRA-Ticketing-Systeme** für strukturierte Change Requests
- Transparente Nachverfolgung von Standardänderungen
- Community-basiertes Feedback-System

### 3. Validierung und Test-Tools
- **XPlan-Validator:** Technisches Validierungswerkzeug für XPlanung-Daten
- Validierungsregeln als Open Source
- Testdaten-Repositories für Entwickler

### 4. Open-Source-Repositories
- Schemata, Skripte und Tools auf OpenCode-Plattform
- EUPL-1.2 und LGPL-Lizenzierung für maximale Wiederverwendbarkeit
- Community-Beiträge über GitLab Merge Requests

### 5. Dokumentation und Leitfäden
- **Handreichung zu XPlanung, XBau, XBreitband und XTrasse** (3. Auflage)
  - Herausgegeben von Deutschem Städtetag und Landkreistag
  - Integriert IT-Planungsrat-Beschlüsse zu XTrasse und XBreitband
- **Leitfaden XPlanung** auf xleitstelle.de
- Umfassende technische Dokumentation

### 6. Forum und Vernetzung
- Professionelles Networking für Praktiker
- Erfahrungsaustausch zwischen Implementierern
- Community-Support

## Relevanz für Digitale Wärmewende

### Direkte Relevanz

**XPlanung als Basis:**
- Bauleitpläne können Wärmeplanungsgebiete ausweisen
- Energetische Vorgaben und Versorgungskonzepte in Bebauungsplänen
- Standardisierte Darstellung von Fernwärmevorranggebieten

**XTrasse für Wärmenetze:**
- Standardisierter Austausch von Fernwärmeleitungsplänen
- Räumliche Verträglichkeitsprüfung bei Netzausbau
- Infrastrukturatlanten für Wärmeversorgung
- Genehmigungsverfahren für Wärmenetzausbau
- Integration mit Bestandsinfrastruktur (Gas, Strom, Wasser)

**Validierung und Qualitätssicherung:**
- Sicherstellung maschinenlesbarer Wärmeplanungsdaten
- Automatisierte Prüfung von Planungsdokumenten
- Interoperabilität zwischen verschiedenen Fachverfahren

### Methodische Relevanz

**Best Practices für Standardisierung:**
- Erfolgreiche Etablierung bundesweiter Geodatenstandards
- Koordination zwischen Bund, Ländern und Kommunen
- Open-Source-basierte Entwicklung und Community-Building
- Systematisches Änderungsmanagement

**Übertragbare Ansätze:**
- Versionierung und Release-Management
- Validierungsregeln und Test-Tools
- Öffentliche Repositories für Transparenz
- Handreichungen für Praktiker

**Organisatorisches Modell:**
- Zentrale Fach- und Koordinierungsstelle (XLeitstelle)
- Einbindung in bestehende Verwaltungsstrukturen (LGV Hamburg)
- Abstimmung mit Fachministerkonferenzen
- Nutzung öffentlicher Infrastruktur (OpenCode)

## Externe Ressourcen und Weiterführende Links

### XLeitstelle Hauptportale
- **XLeitstelle Website**: [https://xleitstelle.de](https://xleitstelle.de)
- **XLeitstelle GitLab Gruppe**: [https://gitlab.opencode.de/xleitstelle](https://gitlab.opencode.de/xleitstelle)
- **OpenCode Plattform**: [https://opencode.de](https://opencode.de)

### XPlanung-Ressourcen
- **XPlan-Tools Repository**: [https://gitlab.opencode.de/xleitstelle/xplanung/xplan-tools](https://gitlab.opencode.de/xleitstelle/xplanung/xplan-tools)
- **Testdaten Repository**: [https://gitlab.opencode.de/xleitstelle/xplanung/testdaten](https://gitlab.opencode.de/xleitstelle/xplanung/testdaten)
- **Validierungsregeln Repository**: [https://gitlab.opencode.de/xleitstelle/xplanung/validierungsregeln/standard](https://gitlab.opencode.de/xleitstelle/xplanung/validierungsregeln/standard)
- **Der Leitfaden XPlanung**: [https://xleitstelle.de/leitfaden](https://xleitstelle.de/leitfaden)

### XTrasse-Ressourcen
- **XTrasse GitLab Gruppe**: [https://gitlab.opencode.de/xleitstelle/xtrasse](https://gitlab.opencode.de/xleitstelle/xtrasse)
- **XTrasse Spezifikation**: [https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation](https://gitlab.opencode.de/xleitstelle/xtrasse/spezifikation)
- **XTrasse Anwendungen**: [https://gitlab.opencode.de/xleitstelle/xtrasse/anwendungen](https://gitlab.opencode.de/xleitstelle/xtrasse/anwendungen)
- **XTrasse 1.0 Ankündigung**: [https://xleitstelle.de/node/118](https://xleitstelle.de/node/118)

### XBreitband-Ressourcen
- **XBreitband GitLab Gruppe**: [https://gitlab.opencode.de/xleitstelle/xbreitband](https://gitlab.opencode.de/xleitstelle/xbreitband)
- **XML-Nachrichten-Tool (XNT)**: [https://gitlab.opencode.de/xleitstelle/xbreitband/xnt](https://gitlab.opencode.de/xleitstelle/xbreitband/xnt)
- **XBreitband/XTrasse Übersicht**: [https://xleitstelle.de/xtrassexbreitband](https://xleitstelle.de/xtrassexbreitband)
- **Änderungsmanagement und Releases**: [https://xleitstelle.de/xtrassexbreitband/download](https://xleitstelle.de/xtrassexbreitband/download)

### Dokumentation und Handreichungen
- **Handreichung XPlanung (Deutscher Städtetag)**: [https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung](https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung)
- **Handreichung XPlanung 3. Auflage (Deutscher Landkreistag)**: [https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage](https://www.landkreistag.de/publikationen/3277-handreichung-xplanung-3-auflage)
- **XBau Detailansicht (FITKO)**: [https://docs.fitko.de/fit-standards/xbau/](https://docs.fitko.de/fit-standards/xbau/)

### Institutionelle Ressourcen
- **Landesbetrieb Geoinformation und Vermessung Hamburg**: [https://www.hamburg.de/bsw/landesbetrieb-geoinformation-und-vermessung](https://www.hamburg.de/bsw/landesbetrieb-geoinformation-und-vermessung)
- **XLeitstelle Team**: [https://xleitstelle.de/leitstelle/team](https://xleitstelle.de/leitstelle/team)
- **XLeitstelle Impressum**: [https://xleitstelle.de/impressum](https://xleitstelle.de/impressum)

### Weitere Informationsquellen
- **DiPlanung / ozgxplanung (xPlanBox)**: [https://gitlab.opencode.de/diplanung/ozgxplanung](https://gitlab.opencode.de/diplanung/ozgxplanung)
- **BIMBreitband - XTrasse und XBreitband Standards**: [https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau](https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau)
- **XLeitstelle Termine 2025**: [https://xleitstelle.de/node/137](https://xleitstelle.de/node/137)

## Zusammenfassung der GitLab-Aktivität (Stand November 2025)

### XPlanung-Repositories
| Repository | Commits | Branches | Releases | Status | Lizenz |
|------------|---------|----------|----------|--------|--------|
| XPlan-Tools | 137 | 10 | 26 | Aktiv | EUPL-1.2 |
| Testdaten | 16 | 1 | - | Archiv | - |
| Validierungsregeln | 268 | 2 | 16 | Aktiv | LGPL-2.1 |

### Beobachtete Merge-Request-Aktivität
- Aktive Entwicklung in XPlan-Tools (Januar 2025)
- Verbesserungen an Migrations-Skripten
- Bug-Fixes für Validierungsregeln
- Updates am XPlanValidator

### Community-Engagement
- CONTRIBUTING.md in Validierungsregeln-Repository
- Aktive Diskussionsforen
- Wiki-Integration
- Transparentes Issue-Tracking via JIRA

## Offene Fragen und Potenzial für weitere Research

### Technische Fragen
1. Welche konkreten XPlanung-Objektarten sind für Wärmeplanung relevant?
2. Wie können XTrasse-Leitungsdaten mit Wärmenetzplanungen integriert werden?
3. Existieren bereits XPlanung-Profile speziell für Wärmeplanung?

### Organisatorische Fragen
1. Gibt es Abstimmung zwischen XLeitstelle und BBSR zur kommunalen Wärmeplanung?
2. Welche Rolle spielt die XLeitstelle im Kontext des Wärmeplanungsgesetzes (WPG)?
3. Existieren Pilotprojekte zur Integration von Wärmeplanung in XPlanung?

### Strategische Fragen
1. Kann das XLeitstelle-Modell als Vorbild für eine "Wärmeplanungs-Koordinierungsstelle" dienen?
2. Wie können Best Practices aus XTrasse-Entwicklung für Wärmenetzdaten genutzt werden?
3. Welche Synergien existieren zwischen Breitbandausbau und Wärmenetzausbau?

## Methodik dieser Research

**Recherche-Ansatz:**
- Analyse der OpenCode-Plattform und deren Rolle
- WebFetch auf GitLab-URLs (begrenzt durch JavaScript-basierte Oberfläche)
- WebSearch zur Ergänzung fehlender Repository-Details
- Analyse der offiziellen XLeitstelle-Website
- Auswertung von Sekundärquellen (Städtetag, Landkreistag, FITKO)

**Limitation:**
Die GitLab-Oberfläche von OpenCode ist stark JavaScript-basiert, was direkten WebFetch-Zugriff auf Repository-Inhalte erschwert. Detaillierte Code-Analysen würden direkten Repository-Zugriff oder API-Nutzung erfordern.

**Informationsstand:**
November 2025 - Aktuelle Standards und Repository-Status zum Recherche-Zeitpunkt.

---
*Recherche durchgeführt am: 2025-11-19*
*Letzte Aktualisierung: 2025-11-19*
