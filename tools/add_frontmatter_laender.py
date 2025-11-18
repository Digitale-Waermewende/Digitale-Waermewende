#!/usr/bin/env python3
"""
Script zum automatischen Hinzufügen von Front Matter zu Bundesländer-Dokumenten

Scannt alle .md Dateien in stakeholder/laender/*/ und fügt passendes Front Matter hinzu.
Erstellt Backups vor Änderungen.

Autor: Claude Code
Datum: 2025-11-18
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Bundesländer-Mapping: Ordnername -> Vollständiger Name
BUNDESLAENDER = {
    'Baden-Wuerttemberg': 'Baden-Württemberg',
    'Bayern': 'Bayern',
    'Berlin': 'Berlin',
    'Brandenburg': 'Brandenburg',
    'Bremen': 'Bremen',
    'Hamburg': 'Hamburg',
    'Hessen': 'Hessen',
    'Mecklenburg-Vorpommern': 'Mecklenburg-Vorpommern',
    'Niedersachsen': 'Niedersachsen',
    'Nordrhein-Westfalen': 'Nordrhein-Westfalen',
    'Rheinland-Pfalz': 'Rheinland-Pfalz',
    'Saarland': 'Saarland',
    'Sachsen': 'Sachsen',
    'Sachsen-Anhalt': 'Sachsen-Anhalt',
    'Schleswig-Holstein': 'Schleswig-Holstein',
    'Thueringen': 'Thüringen'
}

# Kürzel-Mapping für XPlanung-Dokumente
KUERZEL_MAPPING = {
    'BW': 'Baden-Württemberg',
    'BY': 'Bayern',
    'BE': 'Berlin',
    'BB': 'Brandenburg',
    'HB': 'Bremen',
    'HH': 'Hamburg',
    'HE': 'Hessen',
    'MV': 'Mecklenburg-Vorpommern',
    'NI': 'Niedersachsen',
    'NW': 'Nordrhein-Westfalen',
    'RP': 'Rheinland-Pfalz',
    'SL': 'Saarland',
    'SN': 'Sachsen',
    'ST': 'Sachsen-Anhalt',
    'SH': 'Schleswig-Holstein',
    'TH': 'Thüringen'
}


def has_frontmatter(content: str) -> bool:
    """Prüft ob Datei bereits Front Matter hat"""
    return content.strip().startswith('---')


def extract_bundesland_from_path(filepath: Path) -> str:
    """Extrahiert Bundesland-Namen aus Dateipfad"""
    # Ordner ist das parent directory
    ordner = filepath.parent.name
    return BUNDESLAENDER.get(ordner, ordner)


def detect_document_type(filename: str) -> str:
    """Erkennt Dokumenttyp aus Dateinamen"""
    if 'KWW-Datenkompass' in filename:
        return 'kww'
    elif 'xplanung' in filename.lower():
        return 'xplanung'
    else:
        return 'unknown'


def extract_kuerzel(filename: str) -> str:
    """Extrahiert Bundesland-Kürzel aus XPlanung-Dateinamen"""
    # Suche nach Mustern wie _BE_, _HH_, etc.
    match = re.search(r'_([A-Z]{2})_', filename)
    if match:
        return match.group(1)

    # Fallback: chat4_by -> BY, deep_research_ext -> aus Ordnername
    patterns = [
        r'chat4_([a-z]{2})',  # chat4_by, chat4_bw
        r'xplanung_([A-Z]{2})_',  # xplanung_BE_
    ]
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            return match.group(1).upper()

    return None


def create_frontmatter(filepath: Path, bundesland: str, doc_type: str) -> str:
    """Erstellt Front Matter für Dokument"""

    # Permalink-Name aus Ordnernamen (lowercase, mit bindestrichen)
    ordner_name = filepath.parent.name.lower()

    if doc_type == 'kww':
        title = f"KWW-Datenkompass {bundesland}"
        permalink = f"/stakeholder/laender/{ordner_name}/kww-datenkompass/"
    elif doc_type == 'xplanung':
        title = f"XPlanung {bundesland}"
        permalink = f"/stakeholder/laender/{ordner_name}/xplanung/"
    else:
        title = filepath.stem  # Fallback: Dateiname ohne Extension
        permalink = f"/stakeholder/laender/{ordner_name}/{filepath.stem.lower()}/"

    frontmatter = f"""---
layout: default
title: "{title}"
parent: {bundesland}
grand_parent: Länder
nav_exclude: true
permalink: {permalink}
---

"""
    return frontmatter


def process_file(filepath: Path) -> dict:
    """Verarbeitet eine einzelne Datei"""
    result = {
        'file': str(filepath),
        'status': 'skipped',
        'message': ''
    }

    # Lese Datei
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f"Fehler beim Lesen: {e}"
        return result

    # Prüfe ob Front Matter bereits vorhanden
    if has_frontmatter(content):
        result['status'] = 'skipped'
        result['message'] = 'Hat bereits Front Matter'
        return result

    # Extrahiere Bundesland
    bundesland = extract_bundesland_from_path(filepath)

    # Erkenne Dokumenttyp
    doc_type = detect_document_type(filepath.name)

    # Bei XPlanung: Versuche Kürzel zu extrahieren für Validierung
    if doc_type == 'xplanung':
        kuerzel = extract_kuerzel(filepath.name)
        if kuerzel and kuerzel in KUERZEL_MAPPING:
            # Validiere dass Bundesland passt
            expected_bundesland = KUERZEL_MAPPING[kuerzel]
            if expected_bundesland != bundesland:
                result['status'] = 'warning'
                result['message'] = f"Kürzel {kuerzel} passt nicht zu Ordner {bundesland}"
                # Nutze Kürzel-Bundesland als führend
                bundesland = expected_bundesland

    # Erstelle Front Matter
    frontmatter = create_frontmatter(filepath, bundesland, doc_type)

    # Erstelle Backup
    backup_path = filepath.with_suffix('.md.backup')
    try:
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f"Fehler beim Backup: {e}"
        return result

    # Schreibe neue Datei mit Front Matter
    new_content = frontmatter + content
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        result['status'] = 'success'
        result['message'] = f'Front Matter hinzugefügt (Typ: {doc_type})'
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f"Fehler beim Schreiben: {e}"
        # Restore backup
        with open(backup_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return result

    return result


def main():
    """Hauptfunktion"""
    # UTF-8 für Windows Console
    import sys
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 70)
    print("Front Matter Bulk-Update für stakeholder/laender")
    print("=" * 70)
    print()

    # Basis-Pfad
    base_path = Path(__file__).parent.parent / 'stakeholder' / 'laender'

    if not base_path.exists():
        print(f"[X] Pfad nicht gefunden: {base_path}")
        return

    print(f"Basis-Pfad: {base_path}")
    print()

    # Sammle alle .md Dateien (außer index.md und README.md)
    files_to_process = []
    for bundesland_ordner in base_path.iterdir():
        if not bundesland_ordner.is_dir():
            continue
        if bundesland_ordner.name.startswith('.'):
            continue

        for md_file in bundesland_ordner.glob('*.md'):
            # Überspringe index.md (wird manuell erstellt)
            if md_file.name in ['index.md', 'README.md']:
                continue
            files_to_process.append(md_file)

    print(f"Gefundene Dateien: {len(files_to_process)}")
    print()

    # Verarbeite Dateien
    results = {
        'success': [],
        'skipped': [],
        'error': [],
        'warning': []
    }

    for filepath in sorted(files_to_process):
        result = process_file(filepath)
        results[result['status']].append(result)

        # Status-Präfix (ASCII-safe für Windows)
        prefix = {
            'success': '[OK]',
            'skipped': '[SKIP]',
            'error': '[ERR]',
            'warning': '[WARN]'
        }[result['status']]

        # Relative Pfad für Ausgabe
        rel_path = filepath.relative_to(base_path)
        print(f"{prefix} {rel_path}")
        print(f"      {result['message']}")

    # Zusammenfassung
    print()
    print("=" * 70)
    print("Zusammenfassung")
    print("=" * 70)
    print(f"Erfolgreich: {len(results['success'])}")
    print(f"Uebersprungen: {len(results['skipped'])}")
    print(f"Warnungen: {len(results['warning'])}")
    print(f"Fehler: {len(results['error'])}")
    print()

    # Details bei Fehlern
    if results['error']:
        print("Fehler-Details:")
        for result in results['error']:
            print(f"  - {result['file']}: {result['message']}")
        print()

    # Protokoll schreiben
    log_file = base_path / f"frontmatter_update_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("Front Matter Bulk-Update Protokoll\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Verarbeitete Dateien: {len(files_to_process)}\n")
        f.write(f"Erfolgreich: {len(results['success'])}\n")
        f.write(f"Übersprungen: {len(results['skipped'])}\n")
        f.write(f"Fehler: {len(results['error'])}\n")
        f.write("\nDetails:\n")
        for status in ['success', 'skipped', 'warning', 'error']:
            f.write(f"\n{status.upper()}:\n")
            for result in results[status]:
                f.write(f"  {result['file']}: {result['message']}\n")

    print(f"Protokoll gespeichert: {log_file.name}")
    print()
    print("Fertig!")


if __name__ == '__main__':
    main()
