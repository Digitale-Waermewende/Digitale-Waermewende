# Interne Links Korrektur - Analyse und Lösungen

**Datum**: 2025-11-18
**Status**: Analysiert - Bereit zur Korrektur

## Problem

Die neu erstellten Index-Dateien verwenden **Permalink-basierte interne Links** (z.B. `/standards/xplanung/`), die nur nach Jekyll-Build funktionieren, nicht aber im rohen Markdown auf GitHub.

**Beispiel (aktuell nicht funktionierend)**:
```markdown
[XPlanung](/standards/xplanung/)
```

## Ursache

Bei der Umstrukturierung wurden Permalink-URLs für interne Links verwendet, die erst nach dem Jekyll-Build auf GitHub Pages aufgelöst werden. Im Markdown-Kontext (z.B. beim Klick auf GitHub) funktionieren diese Links nicht.

## Richtige Lösung

**Just the Docs** und Jekyll unterstützen mehrere Link-Formate. Für **interne Links** sollten **relative Pfade** verwendet werden:

### Variante 1: Relative Pfade (empfohlen)
```markdown
<!-- Von stakeholder/bund/XLeitstelle/index.md nach standards/XPlanung/index.md -->
[XPlanung](../../../standards/XPlanung/index.md)

<!-- Von standards/index.md nach standards/XPlanung/index.md -->
[XPlanung](XPlanung/index.md)

<!-- Von standards/XPlanung/index.md nach stakeholder/bund/XLeitstelle/index.md -->
[XLeitstelle](../../stakeholder/bund/XLeitstelle/index.md)
```

### Variante 2: Site Baseurl (für Permalinks)
```markdown
[XPlanung]({{ site.baseurl }}{% link standards/XPlanung/index.md %})
```

### Vergleich mit funktionierenden Beispielen

**BBSR index.md** (funktioniert):
```markdown
<!-- Gleiche Ebene -->
[KWW-Halle](../KWW-Halle/)

<!-- Dokument im gleichen Ordner -->
[BBSR Wärmeplanung Forschung](2025-09-21_BBSR_Waermeplanung-Forschung.md)
```

## Betroffene Dateien und Links

### 1. stakeholder/bund/XLeitstelle/index.md

**Aktuell (falsch)**:
```markdown
[XPlanung](/standards/xplanung/)
[XBau](/standards/xbau/)
[XTrasse](/standards/xtrasse/)
```

**Korrigiert (richtig)**:
```markdown
[XPlanung](../../../standards/XPlanung/index.md)
[XBau](../../../standards/XBau/index.md)
[XTrasse](../../../standards/XTrasse/index.md)
```

**Pfadlogik**: `stakeholder/bund/XLeitstelle/` → `../` (zu bund) → `../` (zu stakeholder) → `../` (zu root) → `standards/XPlanung/index.md`

---

### 2. stakeholder/bund/AdV/index.md

**Aktuell (falsch)**:
```markdown
[ALKIS](/standards/alkis/)
[Datenintegration](/standards/datenintegration/)
[KWW-Halle](/stakeholder/bund/kww-halle/)
```

**Korrigiert (richtig)**:
```markdown
[ALKIS](../../../standards/ALKIS/index.md)
[Datenintegration](../../../standards/Datenintegration/index.md)
[KWW-Halle](../KWW-Halle/index.md)
```

**Pfadlogik**:
- Zu standards: `../../../standards/`
- Zu KWW-Halle (gleiche Ebene): `../KWW-Halle/`

---

### 3. standards/index.md

**Aktuell (falsch)**:
```markdown
[XPlanung](/standards/xplanung/)
[XTrasse](/standards/xtrasse/)
[XBau](/standards/xbau/)
[ALKIS](/standards/alkis/)
[Datenintegration](/standards/datenintegration/)
[XLeitstelle](/stakeholder/bund/xleitstelle/)
[AdV](/stakeholder/bund/adv/)
[KWW-Halle](/stakeholder/bund/kww-halle/)
```

**Korrigiert (richtig)**:
```markdown
[XPlanung](XPlanung/index.md)
[XTrasse](XTrasse/index.md)
[XBau](XBau/index.md)
[ALKIS](ALKIS/index.md)
[Datenintegration](Datenintegration/index.md)
[XLeitstelle](../stakeholder/bund/XLeitstelle/index.md)
[AdV](../stakeholder/bund/AdV/index.md)
[KWW-Halle](../stakeholder/bund/KWW-Halle/index.md)
```

**Pfadlogik**:
- Zu Unterordnern: `XPlanung/index.md` (direkt)
- Zu stakeholder: `../stakeholder/bund/`

---

### 4. standards/XPlanung/index.md

**Aktuell (falsch)**:
```markdown
[XLeitstelle](/stakeholder/bund/xleitstelle/)
[ALKIS-XPlanung Datenaustausch](/standards/datenintegration/)
[XBau](/standards/xbau/)
[XTrasse](/standards/xtrasse/)
```

**Korrigiert (richtig)**:
```markdown
[XLeitstelle](../../../stakeholder/bund/XLeitstelle/index.md)
[ALKIS-XPlanung Datenaustausch](../Datenintegration/index.md)
[XBau](../XBau/index.md)
[XTrasse](../XTrasse/index.md)
```

**Pfadlogik**:
- Zu XLeitstelle: `../../../stakeholder/bund/XLeitstelle/`
- Zu anderen Standards (gleiche Ebene): `../XBau/`

---

### 5. standards/XTrasse/index.md

**Aktuell (falsch)**:
```markdown
[XLeitstelle](/stakeholder/bund/xleitstelle/)
[Datenintegration](/standards/datenintegration/)
[XPlanung](/standards/xplanung/)
[XBau](/standards/xbau/)
[ALKIS](/standards/alkis/)
```

**Korrigiert (richtig)**:
```markdown
[XLeitstelle](../../../stakeholder/bund/XLeitstelle/index.md)
[Datenintegration](../Datenintegration/index.md)
[XPlanung](../XPlanung/index.md)
[XBau](../XBau/index.md)
[ALKIS](../ALKIS/index.md)
```

---

### 6. standards/XBau/index.md

**Aktuell (falsch)**:
```markdown
[XLeitstelle](/stakeholder/bund/xleitstelle/)
[XPlanung](/standards/xplanung/)
[XTrasse](/standards/xtrasse/)
```

**Korrigiert (richtig)**:
```markdown
[XLeitstelle](../../../stakeholder/bund/XLeitstelle/index.md)
[XPlanung](../XPlanung/index.md)
[XTrasse](../XTrasse/index.md)
```

---

### 7. standards/ALKIS/index.md

**Aktuell (falsch)**:
```markdown
[AdV](/stakeholder/bund/adv/)
[XPlanung](/standards/xplanung/)
[XTrasse](/standards/xtrasse/)
[KWW-Halle](/stakeholder/bund/kww-halle/)
[Datenintegration](/standards/datenintegration/)
```

**Korrigiert (richtig)**:
```markdown
[AdV](../../../stakeholder/bund/AdV/index.md)
[XPlanung](../XPlanung/index.md)
[XTrasse](../XTrasse/index.md)
[KWW-Halle](../../../stakeholder/bund/KWW-Halle/index.md)
[Datenintegration](../Datenintegration/index.md)
```

---

### 8. standards/Datenintegration/index.md

**Aktuell (falsch)**:
```markdown
[ALKIS](/standards/alkis/)
[XTrasse](/standards/xtrasse/)
[XPlanung](/standards/xplanung/)
[AdV](/stakeholder/bund/adv/)
[XLeitstelle](/stakeholder/bund/xleitstelle/)
[KWW-Halle](/stakeholder/bund/kww-halle/)
```

**Korrigiert (richtig)**:
```markdown
[ALKIS](../ALKIS/index.md)
[XTrasse](../XTrasse/index.md)
[XPlanung](../XPlanung/index.md)
[AdV](../../../stakeholder/bund/AdV/index.md)
[XLeitstelle](../../../stakeholder/bund/XLeitstelle/index.md)
[KWW-Halle](../../../stakeholder/bund/KWW-Halle/index.md)
```

---

## Pfad-Berechnungs-Regeln

### Von stakeholder/bund/[Organisation]/ zu:
- **standards/[Standard]/**: `../../../standards/[Standard]/index.md` (3x hoch, dann runter)
- **stakeholder/bund/[AndereOrg]/**: `../[AndereOrg]/index.md` (1x hoch, gleiche Ebene)

### Von standards/ zu:
- **standards/[Standard]/**: `[Standard]/index.md` (direkt runter)
- **stakeholder/bund/[Org]/**: `../stakeholder/bund/[Org]/index.md` (1x hoch, dann runter)

### Von standards/[Standard]/ zu:
- **standards/[AndererStandard]/**: `../[AndererStandard]/index.md` (1x hoch, gleiche Ebene)
- **stakeholder/bund/[Org]/**: `../../../stakeholder/bund/[Org]/index.md` (3x hoch, dann runter)

## Implementierungsplan

### Schritt 1: Automatische Ersetzungen
Für jede Datei die Permalink-Links durch relative Pfade ersetzen (siehe Tabellen oben).

### Schritt 2: Manuelle Verifikation
Jede geänderte Datei auf GitHub ansehen und Links testen.

### Schritt 3: STRUCTURE_GUIDE aktualisieren
Dokumentation für interne Links im STRUCTURE_GUIDE ergänzen.

## Empfehlung für STRUCTURE_GUIDE

Neue Sektion hinzufügen:

```markdown
### Interne Links zwischen Index-Dateien

**Regel**: Verwende **relative Pfade** für interne Links, nicht Permalinks.

**Beispiel (RICHTIG)**:
```markdown
<!-- Von standards/XPlanung/index.md zu standards/XTrasse/index.md -->
[XTrasse](../XTrasse/index.md)

<!-- Von stakeholder/bund/XLeitstelle/index.md zu standards/XPlanung/index.md -->
[XPlanung](../../../standards/XPlanung/index.md)
```

**Beispiel (FALSCH)**:
```markdown
[XTrasse](/standards/xtrasse/)  <!-- Funktioniert nicht in rohem Markdown -->
```

**Warum relative Pfade?**
- Funktionieren sowohl in rohem Markdown (GitHub) als auch nach Jekyll-Build
- Unabhängig von baseurl-Konfiguration
- Einfacher zu testen lokal
```

## Nächste Schritte

1. ✅ Analyse erstellt
2. ⏳ Links in allen 8 Index-Dateien korrigieren
3. ⏳ STRUCTURE_GUIDE aktualisieren
4. ⏳ Commit und Push
5. ⏳ Links auf GitHub testen

---

**Zusammenfassung**: 8 Index-Dateien benötigen Link-Korrekturen. Alle Permalink-basierten internen Links (`/standards/...`) müssen durch relative Pfade (`../standards/...`) ersetzt werden.
