#!/usr/bin/env python3
"""
Script zum automatischen Konvertieren von Plain-Text URLs zu klickbaren Markdown-Links

Konvertiert URLs in spezifischen Mustern zu Markdown-Link-Format.
Beispiel: "- **URL**: https://example.com" → "- **URL**: [https://example.com](https://example.com)"

Autor: Claude Code
Datum: 2025-11-18
"""

import re
from pathlib import Path
from datetime import datetime

# Dateien die bearbeitet werden sollen
TARGET_FILES = [
    'standards/XPlanung/2025-09-22_XPlanung-Monitoring-Umsetzungsstand_Recherche.md',
    'standards/XPlanung/2025-09-21_XPlanung-XLeitstelle-Waermeplanung_Recherche.md',
    'standards/XPlanung/2025-09-22_XPlanung-Waermeplan-Objektartenkatalog-Komplett.md'
]

# URL-Muster die konvertiert werden sollen
URL_PATTERNS = [
    # Pattern 1: "- **Beliebiges Label**: URL"
    # Matcht jedes Label zwischen ** ** gefolgt von : und einer URL
    (
        r'(-\s+\*\*[^*]+\*\*:\s+)(https?://[^\s\)\]]+)(?!\))',
        r'\1[\2](\2)'
    ),
    # Pattern 2: Standalone URLs nach Bullet Points (ohne Label)
    # Nur wenn URL am Zeilenanfang nach "- " steht und noch nicht in [...] ist
    (
        r'^(\s*-\s+)(https?://[^\s\[\]]+)(\s*[✅❌⚠️]?\s*)$',
        r'\1[\2](\2)\3'
    ),
]


def is_already_clickable(line: str) -> bool:
    """Prüft ob Zeile bereits klickbare URLs enthält"""
    # Prüfe auf Markdown-Link-Format [text](url)
    if re.search(r'\[.*?\]\(https?://.*?\)', line):
        return True
    return False


def convert_urls_in_line(line: str) -> tuple[str, int]:
    """
    Konvertiert URLs in einer Zeile zu klickbaren Links

    Returns:
        (konvertierte_zeile, anzahl_konvertierungen)
    """
    # Skip wenn bereits klickbare Links vorhanden
    if is_already_clickable(line):
        return line, 0

    original_line = line
    conversions = 0

    # Wende alle Patterns an
    for pattern, replacement in URL_PATTERNS:
        if re.search(pattern, line, re.MULTILINE):
            new_line = re.sub(pattern, replacement, line, flags=re.MULTILINE)
            if new_line != line:
                line = new_line
                conversions += 1

    return line, conversions


def process_file(filepath: Path) -> dict:
    """Verarbeitet eine einzelne Datei"""
    result = {
        'file': str(filepath),
        'status': 'skipped',
        'message': '',
        'conversions': 0,
        'lines_changed': 0
    }

    # Prüfe ob Datei existiert
    if not filepath.exists():
        result['status'] = 'error'
        result['message'] = 'Datei nicht gefunden'
        return result

    # Lese Datei
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f'Fehler beim Lesen: {e}'
        return result

    # Verarbeite Zeilen
    new_lines = []
    total_conversions = 0
    lines_changed = 0

    for line in lines:
        new_line, conversions = convert_urls_in_line(line)
        new_lines.append(new_line)

        if conversions > 0:
            total_conversions += conversions
            lines_changed += 1

    # Keine Änderungen?
    if total_conversions == 0:
        result['status'] = 'skipped'
        result['message'] = 'Keine URLs zum Konvertieren gefunden'
        return result

    # Erstelle Backup
    backup_path = filepath.with_suffix('.md.backup')
    try:
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f'Fehler beim Backup: {e}'
        return result

    # Schreibe neue Datei
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        result['status'] = 'success'
        result['message'] = f'{total_conversions} URLs konvertiert in {lines_changed} Zeilen'
        result['conversions'] = total_conversions
        result['lines_changed'] = lines_changed
    except Exception as e:
        result['status'] = 'error'
        result['message'] = f'Fehler beim Schreiben: {e}'
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
    print("URL-Konvertierung: Plain Text → Klickbare Markdown-Links")
    print("=" * 70)
    print()

    # Basis-Pfad
    base_path = Path(__file__).parent.parent

    print(f"Basis-Pfad: {base_path}")
    print(f"Zu verarbeitende Dateien: {len(TARGET_FILES)}")
    print()

    # Verarbeite Dateien
    results = {
        'success': [],
        'skipped': [],
        'error': []
    }

    total_conversions = 0

    for target_file in TARGET_FILES:
        filepath = base_path / target_file
        print(f"Verarbeite: {target_file}")

        result = process_file(filepath)
        results[result['status']].append(result)
        total_conversions += result['conversions']

        # Status-Präfix
        prefix = {
            'success': '[OK]',
            'skipped': '[SKIP]',
            'error': '[ERR]'
        }[result['status']]

        print(f"  {prefix} {result['message']}")
        print()

    # Zusammenfassung
    print("=" * 70)
    print("Zusammenfassung")
    print("=" * 70)
    print(f"Erfolgreich: {len(results['success'])} Dateien")
    print(f"Uebersprungen: {len(results['skipped'])} Dateien")
    print(f"Fehler: {len(results['error'])} Dateien")
    print(f"TOTAL URLs konvertiert: {total_conversions}")
    print()

    # Details bei Erfolg
    if results['success']:
        print("Erfolgreich bearbeitete Dateien:")
        for result in results['success']:
            rel_path = Path(result['file']).relative_to(base_path)
            print(f"  - {rel_path}: {result['conversions']} URLs in {result['lines_changed']} Zeilen")
        print()

    # Details bei Fehlern
    if results['error']:
        print("Fehler-Details:")
        for result in results['error']:
            print(f"  - {result['file']}: {result['message']}")
        print()

    # Protokoll schreiben
    log_file = base_path / 'standards' / 'XPlanung' / f"url_conversion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("URL-Konvertierung Protokoll\n")
        f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Verarbeitete Dateien: {len(TARGET_FILES)}\n")
        f.write(f"Erfolgreich: {len(results['success'])}\n")
        f.write(f"Übersprungen: {len(results['skipped'])}\n")
        f.write(f"Fehler: {len(results['error'])}\n")
        f.write(f"Total URLs konvertiert: {total_conversions}\n")
        f.write("\nDetails:\n")
        for status in ['success', 'skipped', 'error']:
            f.write(f"\n{status.upper()}:\n")
            for result in results[status]:
                f.write(f"  {result['file']}: {result['message']}\n")

    print(f"Protokoll gespeichert: {log_file.name}")
    print()
    print("Fertig!")


if __name__ == '__main__':
    main()
