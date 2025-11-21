---
layout: default
title: "XTrasse Bestandsdokumentation"
parent: XTrasse
grand_parent: Standards
nav_exclude: true
permalink: /standards/xtrasse/bestandsdokumentation-rechtlicher-status/
---

# XTrasse für Bestandsdokumentation unterirdischer Infrastruktur - Rechtlicher Status

**Erfassungsdatum**: 2025-11-21
**Frage**: Gibt es ein "amtliches" Dokument (Beschluss, Empfehlung) vom IT-Planungsrat, dass XTrasse mittelfristig für die Bestands-Dokumentation von (unterirdischen) Infrastruktur-Netzen genutzt werden soll?

---

## Zusammenfassung

**Status**: ⚠️ **Teilweise dokumentiert** - Bestandsdokumentation ist im XTrasse-Standard technisch vorgesehen, aber nicht durch einen expliziten IT-Planungsrat-Beschluss als verbindlich erklärt.

**Rechtliche Grundlage**:
- **Verbindlich**: IT-Planungsrat-Beschluss 2021/40 für **Breitbandausbau** (TKG-Zustimmungsverfahren)
- **Technisch vorhanden**: Anwendungsfall "Bestandsnetze" in XTrasse 2.0 Spezifikation
- **Nicht verbindlich**: Keine explizite Verpflichtung zur Bestandsdokumentation aller Infrastruktursparten

---

## IT-Planungsrat Beschluss 2021/40

### Beschlusstext

**Datum**: 29. Oktober 2021
**Beschluss**: IT-Standard XBau und XPlanung - Erweiterung um XBreitband und XTrasse
**Quelle**: [IT-Planungsrat Beschluss 2021-40](https://www.it-planungsrat.de/beschluss/beschluss-2021-40)

**Inhalt des Beschlusses**:

> Der IT-Planungsrat beschließt die **verbindliche Anwendung** der Standards "XBreitband" und "XTrasse" für den Anwendungsfall "Zustimmung nach TKG" im Kontext der Bereitstellung der OZG-Verwaltungsleistung Breitbandausbau.

**Anwendungsbereich laut Beschluss**:
- ✅ Breitbandausbau (Glasfasernetze)
- ✅ Zustimmungsverfahren nach Telekommunikationsgesetz (TKG)
- 🧪 Genehmigungen nach Straßen- und Wegegesetzen (Erprobung 2022)
- 🧪 Verkehrsrechtliche Anordnungen (Erprobung 2022)

**Nicht im Beschluss erwähnt**:
- ❌ Fernwärme, Gas, Strom, Wasser (keine Erwähnung)
- ❌ Bestandsdokumentation als verbindlicher Anwendungsfall
- ❌ Verpflichtung zur flächendeckenden Digitalisierung bestehender Netze

### Bewertung

Der IT-Planungsrat-Beschluss 2021/40 konzentriert sich **ausschließlich auf den Breitbandausbau**. Es gibt **keinen amtlichen Beschluss**, der XTrasse verbindlich für die Bestandsdokumentation aller Infrastruktursparten vorschreibt.

---

## XTrasse 2.0 Spezifikation - Anwendungsfall "Bestandsplan"

Obwohl der IT-Planungsrat-Beschluss sich auf Breitband fokussiert, definiert die **XTrasse 2.0 Spezifikation** selbst einen Anwendungsfall für Bestandsnetze.

### Anwendungsfall 6: Bestandsplan

**Quelle**: [XLeitstelle - XTrasse Anwendungsfälle](https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2)

**Beschreibung**:

> **Bestandsplan**: Leitungspläne der verschiedenen Sparten lassen sich in einem **Bestandsmodell zusammenführen**. Das TrasseGML kann anschließend in ein IFC-Modell transformiert werden.

**Zitat aus XLeitstelle**:

> "Erfasst werden der räumliche Verlauf geplanter Trassen, Attribute der Leitungen... Darüber hinaus können **Bestandsleitungen aller Leitungssparten** erfasst werden."

**Unterstützte Sparten** (laut Spezifikation):
- Telekommunikation
- Energieleitungen (allgemein genannt, keine Detaillierung)
- **Alle Leitungssparten** (pauschal erwähnt)

### Objektartenkatalog: BST_* Objekte (Bestandsnetze)

**Quelle**: XTrasse 2.0 Objektkatalog (Katalog-ID 443), dokumentiert in [Objektartenkatalog-Vergleich](/standards/xplanung/objektartenkatalog-vergleich/)

**Package-Struktur**:
```
XTrasse 2.0/
├── Bestandsnetze/
│   ├── BST_Basisobjekte (Basisklassen)
│   └── BST_Objekte
│       ├── Leitungen (BST_Leitung, BST_Leitungsabschnitt)
│       ├── Anschlüsse (BST_Anschlusspunkt, BST_Muffe)
│       ├── Schächte und Verteiler
│       └── Sparten-spezifische Objekte
```

**Sparten-spezifische BST-Objekte** (dokumentiert im Objektartenkatalog-Vergleich):

| Objektart | Sparte | Verwendung |
|-----------|--------|------------|
| **BST_Fernwaerme** | Wärme | Bestandsdokumentation Fernwärmeleitungen |
| **BST_Gas** | Gas | Bestandsdokumentation Gasleitungen |
| **BST_Strom** | Elektrizität | Bestandsdokumentation Stromleitungen |
| **BST_Wasser** | Wasser | Bestandsdokumentation Wasserleitungen |
| **BST_Leitung** | Alle | Generische Leitungsklasse mit Attribut "Sparte" |

**Attribute der BST_Leitung** (typisch):
- `sparte`: Enum (Wärme/Gas/Strom/Wasser/Telekom)
- `durchmesser`: Measure (mm)
- `material`: String
- `verlegetiefe`: Measure (m)
- `baujahr`: gYear
- `betreiber`: String
- `eigentuemer`: String

### Fernwärme-Dreiklang

**BST_Fernwaerme** ist Teil eines **komplementären Systems** für digitale Wärmeplanung:

```
Rechtliche Ebene:        BauGB §9        →  BP_Fernwaerme (XPlanung)
                              ↓                Festsetzung Versorgungsgebiet
Energieplanung:         WPG §23-26      →  WP_Fernwaermenetz (Wärmeplan)
                              ↓                Netzmodellierung + Planung
Technische Umsetzung:   TKG, EnWG       →  BST_Fernwaerme (XTrasse)
                                             Bestandsdokumentation
```

**Quelle**: [Objektartenkatalog-Vergleich](/standards/xplanung/objektartenkatalog-vergleich/) (Session 013, 2025-11-21)

---

## Interpretation: Technische Möglichkeit vs. Rechtliche Verbindlichkeit

### Was ist technisch möglich?

✅ XTrasse 2.0 **unterstützt technisch** die Bestandsdokumentation für:
- Fernwärme (BST_Fernwaerme)
- Gas (BST_Gas)
- Strom (BST_Strom)
- Wasser (BST_Wasser)
- Telekommunikation (BST_Telekommunikationsleitung)

✅ Anwendungsfall "Bestandsplan" ist in der Spezifikation definiert

✅ Objektartenkatalog enthält alle notwendigen BST_* Objektarten

### Was ist rechtlich verbindlich?

⚠️ **Nur Breitbandausbau** ist durch IT-PLR-Beschluss 2021/40 verbindlich

❌ **Keine Verpflichtung** zur Bestandsdokumentation von:
- Fernwärmenetzen
- Gasnetzen
- Stromnetzen
- Wassernetzen

❌ **Kein IT-Planungsrat-Beschluss** oder **Empfehlung**, der die mittelfristige Nutzung von XTrasse für Bestandsdokumentation aller Infrastruktursparten vorschreibt

### Warum ist Bestandsdokumentation trotzdem im Standard?

**Erklärung**: Der Anwendungsfall "Bestandsplan" dient primär der **Koordination bei Neubauprojekten**:

1. **Breitbandausbau** erfordert Kenntnis bestehender Leitungen (Kreuzungen, Schutzabstände)
2. **Leitungsauskunft** vor Baubeginn (Vermeidung von Beschädigungen)
3. **Interkommunale Konzepte** benötigen Übersicht aller Sparten
4. **BIM-Integration** erfordert vollständiges 3D-Leitungsmodell

**Zitat aus XLeitstelle**:

> "Bestandsinfrastrukturen sind ein **anwendungsfallübergreifendes Thema**" und können in allen Planklassen verwendet werden.

Die Bestandsdokumentation ist also eine **technische Voraussetzung** für effektive Trassenplanung, aber nicht das primäre Ziel des IT-PLR-Beschlusses.

---

## Weitere Quellen und Stakeholder

### XLeitstelle-Dokumentation

**Rechtliche Verbindlichkeit**:
[https://xleitstelle.de/leitstelle/rechtliches](https://xleitstelle.de/leitstelle/rechtliches)

> "XTrasse konzentriert sich auf spezifische Anwendungsfälle:
> - Zustimmung zur Leitungsverlegung nach Telekommunikationsgesetz (TKG) – **verbindlich**
> - Genehmigungen nach Straßen- und Wegegesetzen bei Breitbandtrassen – in Erprobung
> - Verkehrsrechtliche Anordnungen – in Erprobung"

**Keine Erwähnung** von Bestandsdokumentation als verbindlichem Anwendungsfall.

### FITKO (Föderale IT-Kooperation)

**Detailansicht XBreitband / XTrasse**:
[https://docs.fitko.de/fit-standards/xbreitband/](https://docs.fitko.de/fit-standards/xbreitband/)

FITKO finanziert die Pflege der Standards über das Kernbudget. Auch hier: **Fokus auf Breitbandausbau**, keine explizite Roadmap für andere Infrastruktursparten.

### Deutscher Städtetag

**Handreichung zu XPlanung, XBau, XBreitband und XTrasse**:
[Deutscher Städtetag Publikationen](https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung)

Praktische Handreichung für Kommunen zur Einführung der Standards. Schwerpunkt: **Breitband und Bauleitplanung**.

---

## Fazit

### Direkte Antwort auf die Frage

**Gibt es ein "amtliches" Dokument vom IT-Planungsrat für Bestandsdokumentation?**

🔴 **Nein**, es gibt **keinen IT-Planungsrat-Beschluss oder Empfehlung**, der XTrasse explizit für die mittelfristige Bestandsdokumentation von unterirdischen Infrastrukturnetzen (Fernwärme, Gas, Strom, Wasser) vorsieht.

✅ **Aber**: Die **XTrasse 2.0 Spezifikation** (technisches Dokument der XLeitstelle) enthält:
- Anwendungsfall "Bestandsplan" für alle Leitungssparten
- BST_* Objektarten für Fernwärme, Gas, Strom, Wasser
- Technische Möglichkeit zur vollständigen Bestandsdokumentation

### Rechtlicher Status nach Kategorien

| Kategorie | Status | Grundlage |
|-----------|--------|-----------|
| **Breitbandausbau** | ✅ Verbindlich | IT-PLR Beschluss 2021/40 |
| **Bestandsdokumentation Telekom** | ⚠️ Technisch möglich | XTrasse 2.0 Spezifikation |
| **Bestandsdokumentation Fernwärme** | ⚠️ Technisch möglich | XTrasse 2.0 Spezifikation (BST_Fernwaerme) |
| **Bestandsdokumentation Gas/Strom/Wasser** | ⚠️ Technisch möglich | XTrasse 2.0 Spezifikation (BST_*) |
| **Verbindliche Bestandsdokumentation (alle)** | ❌ Nicht vorgeschrieben | Kein IT-PLR-Beschluss |

### Interpretation

1. **Technische Vorbereitung**: XTrasse ist **technisch bereit** für Bestandsdokumentation aller Infrastruktursparten.

2. **Rechtliche Lücke**: Es fehlt ein **politischer Beschluss** oder eine **Empfehlung**, der Kommunen und Netzbetreiber verpflichtet oder ermutigt, XTrasse für Bestandsdokumentation zu nutzen.

3. **Strategische Bedeutung**: Für die **Wärmewende** wäre eine standardisierte Bestandsdokumentation von Fernwärmenetzen via **BST_Fernwaerme** hochrelevant, um:
   - Koordinierte Netzplanung zu ermöglichen
   - Konflikte mit anderen Leitungen zu vermeiden
   - Wärmepläne (WP_Fernwaermenetz) mit Bestandsdaten zu verknüpfen
   - Digitale Zwillinge für Wärmenetze aufzubauen

4. **Handlungsbedarf**: Ein künftiger IT-Planungsrat-Beschluss oder eine Empfehlung könnte die **mittelfristige Einführung** von XTrasse für Bestandsdokumentation beschleunigen.

---

## Primärquellen

### Offizielle Beschlüsse

- **IT-Planungsrat Beschluss 2021/40**: [https://www.it-planungsrat.de/beschluss/beschluss-2021-40](https://www.it-planungsrat.de/beschluss/beschluss-2021-40)
- **Beschlusstext (PDF)**: [https://www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-40_IT-Standard_XBau_und_XPlanung_AL3_Spezifikation_XTrasse.pdf](https://www.it-planungsrat.de/fileadmin/beschluesse/2021/Beschluss2021-40_IT-Standard_XBau_und_XPlanung_AL3_Spezifikation_XTrasse.pdf)

### XLeitstelle-Dokumentation

- **XTrasse Anwendungsfälle**: [https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2](https://xleitstelle.de/xtrassexbreitband/anwendungsfaelle2)
- **XTrasse Anwendungen**: [https://xleitstelle.de/xtrassexbreitband/anwendungen](https://xleitstelle.de/xtrassexbreitband/anwendungen)
- **Rechtliche Verbindlichkeit**: [https://xleitstelle.de/leitstelle/rechtliches](https://xleitstelle.de/leitstelle/rechtliches)
- **Standarderweiterung**: [https://xleitstelle.de/xtrassexbreitband/standarderweiterung](https://xleitstelle.de/xtrassexbreitband/standarderweiterung)
- **XTrasse 2.0 Objektkatalog**: [https://xleitstelle.de/downloads/catalogues/443/overview-summary.html](https://xleitstelle.de/downloads/catalogues/443/overview-summary.html)

### FITKO

- **XBreitband / XTrasse Detailansicht**: [https://docs.fitko.de/fit-standards/xbreitband/](https://docs.fitko.de/fit-standards/xbreitband/)

### BIMBreitband

- **Digitale Standards für den Breitbandausbau**: [https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau](https://www.bimbreitband.de/newsdetailseite/xtrasse-und-xbreitband-standards-fuer-den-breitbandausbau)

### Deutscher Städtetag

- **Handreichung zu XPlanung, XBau, XBreitband und XTrasse**: [https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung](https://www.staedtetag.de/publikationen/weitere-publikationen/2023/handreichung-xplanung)

### Interne Dokumente (Digitale-Waermewende Repository)

- **[XTrasse Hauptdokument](/standards/xtrasse/)** - Übersicht und Anwendungsfälle
- **[Objektartenkatalog-Vergleich](/standards/xplanung/objektartenkatalog-vergleich/)** - Detaillierte Analyse von BST_Fernwaerme und Fernwärme-Dreiklang
- **[XTrasse-XBreitband Verhältnis Research](/standards/xtrasse/xtrasse-xbreitband-verhaeltnis/)** - Vergleich der Nachrichtenstandards

---

**Letzte Aktualisierung**: 2025-11-21
**Status**: Research abgeschlossen, Primärquellen verifiziert
