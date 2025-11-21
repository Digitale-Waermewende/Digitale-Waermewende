---
layout: default
title: "Session 0016"
parent: Session Log
nav_exclude: true
permalink: /session-log/session-0016/
---

# Session 0016 - 2025-11-21 - FITKO als Stakeholder dokumentiert

**Datum**: 2025-11-21
**Commits**: [2f91fd7](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/2f91fd7)

## User-Eingabe

```
Erstelle in Digitale-Waermewende\stakeholder einen Ordner und eine Index-Datei für FITKO,
recherchiere das Selbstverständnis der Organisation, die Aufgaben und Projekte, im Zusammenhang
mit der XLeitstelle. Dokumentiere die 5-10 relevante Primärquellen in der Index-Datei. dann
commit, push und session-log
```

## Ergebnisse

**Commits**: [2f91fd7](https://github.com/Digitale-Waermewende/Digitale-Waermewende/commit/2f91fd7)

**Neue Seiten**:
- [FITKO](/stakeholder/fitko/)

**Geänderte Seiten**:
- (keine)

## Entscheidungen

### FITKO als neuer Stakeholder dokumentiert

**Platzierung**: stakeholder/FITKO/ (nicht stakeholder/bund/FITKO)
- Eigene Top-Level-Kategorie (wie IT-Planungsrat unter stakeholder/bund/)
- Begründung: FITKO ist föderale Organisation (nicht reine Bundesebene)

### Recherche-Strategie

**Primärquellen-Fokus**:
1. **WebSearch**: Überblick zu FITKO (Wikipedia, offizielle Seiten)
2. **WebFetch fitko.de**: Selbstverständnis, Mission, Kernwerte
3. **WebSearch XLeitstelle-Bezug**: Finanzierung, Governance
4. **WebFetch XLeitstelle**: Operative Zusammenarbeit dokumentieren
5. **WebSearch Projekte**: OZG, Registermodernisierung, FIT-Connect

**Verifizierte Quellen**: 10 Primärquellen (fitko.de, docs.fitko.de, IT-PLR, XLeitstelle)

### Dokumentierte Kerninformationen

**Organisation**:
- **Status**: Rechtsfähige bundesunmittelbare Anstalt des öffentlichen Rechts
- **Gründung**: 1. Januar 2020
- **Sitz**: Frankfurt am Main
- **Leitung**: Dr. André Göbel (Präsident seit 1.11.2023)
- **Mitarbeiter**: 111 (Stand Juni 2025)
- **Finanzierung**: 35% Bund, 65% Länder

**Selbstverständnis**:
> "Die FITKO gestaltet gemeinsam mit Bund, Ländern und Kommunen die Digitalisierung der Verwaltung in Deutschland."

**6 Prinzipien**:
1. Kooperativ
2. Vernetzt
3. Kompetent
4. Transparent
5. Neutral
6. Vermittelnd

**Verhältnis zum IT-Planungsrat**:
- IT-PLR: Politisch-strategische Weichen (Beschlussorgan)
- FITKO: Ausführende Organisation (Operative Umsetzung)

### XLeitstelle-Zusammenhang herausgearbeitet

**FITKO finanziert**:
- ✅ **XBreitband** (Stammbudget FITKO)
- ✅ **XTrasse** (Stammbudget FITKO)

**Nicht FITKO-finanziert**:
- ❌ **XPlanung** (82,5% Länder, 17,5% Bund - Königsteiner Schlüssel)
- ❌ **XBau** (Bund-Länder-Finanzierung)

**Governance**:
- FITKO-Vertreter im Lenkungskreis der XLeitstelle (seit März 2022)
- Strategische Steuerung der Standards-Entwicklung

**Zitat aus xleitstelle.de**:
> "Die Finanzierung des Betriebs von XBreitband / XTrasse erfolgt im Rahmen des Stammbudgets der FITKO."

### Wichtige Projekte dokumentiert

**1. OZG-Umsetzung** (Onlinezugangsgesetz):
- 575 Verwaltungsleistungen online (bis Ende 2022)
- Prinzip "Einer für Alle" (EfA)
- FITKO als operative Umsetzungsorganisation

**2. Registermodernisierung**:
- Technische, strukturelle, rechtliche Weiterentwicklung aller deutschen Register
- Once-Only-Prinzip (Daten nur einmal erheben)
- Registerübergreifende Identifikationsnummer (IDNr)
- Erprobungsprojekte: "Grenzen überwinden, Daten verbinden"

**3. FIT-Connect**:
- Infrastruktur für Datenübermittlung zwischen Verwaltungsebenen
- APIs und SDKs für Antragsübermittlung
- Zuständigkeitsermittlung
- Technische Datenschemata-Verhandlung

**4. FIT-Store**:
- Katalog wiederverwendbarer IT-Komponenten
- Föderale IT-Bausteine für OZG-Umsetzung

**5. Weitere Produkte**:
- 115 (Einheitliche Behördenrufnummer)
- Deutsche Verwaltungscloud
- Governikus (E-Government-Lösungen)
- GovData (Datenportal)
- FIM (Föderales Informationsmanagement)
- FINK (Föderales Netzwerkmanagement)

### Relevanz für Wärmewende herausgearbeitet

**Direkte Relevanz**:
- **XTrasse-Finanzierung**: FITKO finanziert Standard, der Fernwärmeleitungen modelliert (BST_Fernwaerme)
- **Koordinierte Verlegung**: Ermöglicht gemeinsame Planung von Wärme- und Breitbandnetzen
- **Digitale Wärmeplanung**: Standardisierte Bestandsdokumentation

**Indirekte Relevanz**:
- **Registermodernisierung**: Verknüpfung Gebäudedaten (ALKIS) mit Energiedaten
- **Once-Only-Prinzip**: Reduziert Aufwand für Wärmeplanung
- **OZG-Umsetzung**: Digitale Genehmigungsverfahren für Wärmenetze

## Technische Details

### Recherche-Methodik

**WebSearch-Queries**:
1. "FITKO Föderale IT-Kooperation Selbstverständnis Aufgaben Organisation"
2. "FITKO XLeitstelle Planen Bauen XPlanung XBau Finanzierung Zusammenarbeit"
3. "FITKO Projekte OZG Registermodernisierung FIT-Connect Digitalisierungsprogramme"

**WebFetch-URLs**:
1. https://www.fitko.de/ (Hauptseite, Selbstverständnis)
2. https://xleitstelle.de/leitstelle/betrieb_finanzierung (FITKO-Finanzierung XBreitband/XTrasse)

**Gefundene Informationen**:
- Organisation, Leitung, Mitarbeiterzahl (WebSearch + WebFetch)
- Selbstverständnis, Mission, 6 Prinzipien (WebFetch fitko.de)
- XLeitstelle-Finanzierung (WebFetch XLeitstelle)
- Projekte (WebSearch-Snippets)

### Dokumentstruktur

**Hauptsektionen**:
1. Was ist die FITKO? (Status, Gründung, Leitung)
2. Selbstverständnis (Mission, Kernwerte, 6 Prinzipien)
3. Aufgaben und Verantwortlichkeiten (4 Hauptaufgaben)
4. Finanzierung (Finanzierungsschlüssel, Budget-Kategorien)
5. Wichtige Projekte und Programme (5 Hauptprojekte + Weitere)
6. Beziehung zur XLeitstelle (Finanzierung, Governance, Operative Zusammenarbeit)
7. Relevanz für die Wärmewende (Direkt + Indirekt)
8. Gremienarbeit und Netzwerk
9. Primärquellen (10 Links)
10. Verwandte Bereiche (Organisation, Standards, Gesetze)

### Primärquellen (10)

**Offizielle FITKO-Webseiten** (5):
1. https://www.fitko.de/ (Hauptseite)
2. https://www.fitko.de/digitalisierungsbudget (Projekte)
3. https://docs.fitko.de/ (Technische Dokumentation)
4. https://docs.fitko.de/fit/policies/eckpunkte-umsetzung-ozg/ (OZG-Eckpunkte)
5. https://gitlab.opencode.de/fitko (Open-Source-Projekte)

**IT-Planungsrat** (2):
6. IT-PLR Beschluss 2018/04 - FITKO Factsheet (PDF)
7. IT-PLR Digitalisierungsbudget-Projekte

**XLeitstelle** (2):
8. XLeitstelle Betrieb & Finanzierung
9. XLeitstelle Rechtliche Verbindlichkeit

**Wikipedia** (1):
10. Föderale IT-Kooperation (Übersicht)

## Lessons Learned

### WebSearch + WebFetch Kombination effektiv

**Strategie**:
1. WebSearch für Überblick und URL-Identifikation
2. WebFetch für detaillierte Informationsentnahme
3. Mehrere Quellen triangulieren

**Ergebnis**: Vollständiges Bild von Organisation, Aufgaben und XLeitstelle-Bezug

### FITKO-Finanzierung zentral für XTrasse

**Erkenntnis**: FITKO finanziert nur XBreitband + XTrasse (nicht XPlanung/XBau)

**Bedeutung für Wärmewende**:
- XTrasse dokumentiert Fernwärmeleitungen (BST_Fernwaerme)
- FITKO-Finanzierung sichert langfristige Pflege des Standards
- Strategische Bedeutung für koordinierte Netzplanung

### Föderale Struktur verstehen

**FITKO vs. IT-PLR**:
- IT-PLR: Politisches Beschlussorgan (Bund + Länder)
- FITKO: Operative Umsetzung (rechtsfähige Anstalt)

**Parallele**: Ähnlich wie IT-PLR → XLeitstelle (Beschluss → Umsetzung)

### Registermodernisierung unterschätzt

**Potenzial für Wärmewende**:
- Once-Only-Prinzip reduziert Datenerhebungsaufwand
- ALKIS-Energiedaten-Verknüpfung ermöglicht präzise Wärmebedarfsermittlung
- Standardisierte Datenaustauschformate beschleunigen Wärmeplanung

**Bisher wenig dokumentiert**: Sollte in künftigen Recherchen vertieft werden

---

**Statistik**:
- Commits: 1
- Neue Seiten: 1 (270 Zeilen)
- Primärquellen: 10
- WebSearch-Queries: 3
- WebFetch-Aufrufe: 2
- Dokumentierte Projekte: 9

**Letzte Aktualisierung**: 2025-11-21
