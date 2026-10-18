#!/usr/bin/env python3
"""Plan and copy course files without deleting, overwriting, or uploading originals."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

SUPPORTED = {'.pdf', '.ppt', '.pptx', '.doc', '.docx', '.odt', '.txt', '.md',
             '.csv', '.xlsx', '.xls', '.png', '.jpg', '.jpeg', '.webp', '.epub',
             '.mp3', '.mp4', '.wav', '.ipynb', '.py', '.c', '.cpp', '.h', '.tex'}
MODULE = re.compile(r'\bICT\d{3,4}\b', re.I)


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def within(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def route(relative: str, module: str | None, domain: str) -> tuple[str | None, str]:
    text = relative.replace('_', ' ')
    if domain != 'study' or 'samuel work' in text.lower():
        return None, 'Work material requires a separate private workspace and policy.'
    modules = {match.upper() for match in MODULE.findall(text)}
    if module:
        if modules and modules != {module}:
            return None, 'Module hints conflict with the requested module.'
        modules.add(module)
    if len(modules) != 1:
        return None, 'Missing or conflicting module code; inspect the document before routing.'
    course = next(iter(modules))
    assignment = {int(n) for n in re.findall(r'\b(?:assignment|assessment)\s*[- ]*0*(\d+)\b', text, re.I)}
    lesson = {int(n) for n in re.findall(r'\b(?:lesson|lecture)\s*[- ]*0*(\d+)\b', text, re.I)}
    if len(assignment) > 1 or len(lesson) > 1:
        return None, 'Conflicting assignment or lesson numbers.'
    prefix = f'Samuel/Samuel Study/{course}'
    if assignment:
        return f'{prefix}/Assignments/Assignment {next(iter(assignment))}', 'Explicit module and assignment number.'
    if lesson:
        return f'{prefix}/Slides/Lesson{next(iter(lesson))}', 'Explicit module and lesson number.'
    if re.search(r'\b(?:assignment|assessment)\b', text, re.I):
        return None, 'Assignment number is missing.'
    if Path(relative).suffix.lower() in {'.ppt', '.pptx'} or re.search(r'\bslides?\b', text, re.I):
        return f'{prefix}/Slides/00 Unsorted', 'Module known; lesson number needs review.'
    if re.search(r'\b(?:textbook|reading|article|paper|book)\b', text, re.I):
        return f'{prefix}/Readings', 'Explicit reading label.'
    if re.search(r'\b(?:lab|practical|tutorial)\b', text, re.I):
        return f'{prefix}/Labs', 'Explicit lab or tutorial label.'
    return None, 'Document role is unclear; do not guess from the extension.'


def plan(root: Path, inbox: Path, module: str | None, domain: str) -> dict:
    root, inbox = root.resolve(), inbox.resolve()
    if not inbox.is_dir():
        raise ValueError('Inbox is not a directory.')
    study = root / 'Samuel' / 'Samuel Study'
    if not study.is_dir():
        raise ValueError('Workspace is missing Samuel/Samuel Study.')
    known: dict[str, str] = {}
    for file in sorted(study.rglob('*')):
        if file.is_file() and not file.is_symlink() and not within(file, inbox) and file.suffix.lower() in SUPPORTED:
            known.setdefault(digest(file), str(file.relative_to(root)))
    rows = []
    for file in sorted(inbox.rglob('*')):
        if file.is_dir() and not file.is_symlink():
            continue
        relative = str(file.relative_to(inbox))
        if file.name.startswith('.') or file.name == 'README.md':
            continue
        row = {'source': str(file.absolute()), 'original_path': relative,
               'sha256': '', 'source_id': '', 'destination': '', 'action': 'review', 'reason': ''}
        if file.is_symlink() or not file.is_file():
            row['reason'] = 'Symlinks and special files are excluded.'
        elif file.suffix.lower() not in SUPPORTED:
            row['reason'] = 'Unsupported file type; do not open or execute it automatically.'
        else:
            file_hash = digest(file)
            row.update(sha256=file_hash, source_id='SRC-' + file_hash[:12].upper())
            destination, reason = route(relative, module, domain)
            row['reason'] = reason
            if destination:
                safe_name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', file.name).rstrip(' .')
                if len(safe_name) > 150:
                    safe_name = Path(safe_name).stem[:130] + Path(safe_name).suffix
                target = f"{destination}/{row['source_id']} - {safe_name}"
                existing = root / target
                if existing.exists():
                    if existing.is_symlink() or not existing.is_file() or digest(existing) != file_hash:
                        row['reason'] = 'Destination collision; preserve both files for review.'
                    else:
                        row.update(action='duplicate', destination=target, reason='Identical destination already exists.')
                elif file_hash in known:
                    row.update(action='duplicate', destination=known[file_hash],
                               reason='Exact byte duplicate; register another module link without deleting the original.')
                else:
                    row.update(action='copy', destination=target)
                    known[file_hash] = target
        rows.append(row)
    return {'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(),
            'root': str(root), 'inbox': str(inbox), 'domain': domain,
            'mode': 'copy_only', 'files': rows}


def apply_plan(data: dict, root: Path) -> list[dict]:
    root = root.resolve()
    if data.get('schema_version') != 1 or data.get('mode') != 'copy_only' or Path(data['root']).resolve() != root:
        raise ValueError('Plan format or workspace does not match.')
    inbox = Path(data['inbox']).resolve()
    allowed = (root / 'Samuel' / 'Samuel Study').resolve()
    actions = []
    prepared = []
    # Check the whole plan before the first copy; reject tampering and stale input.
    for row in data['files']:
        if row['action'] != 'copy':
            continue
        source = Path(row['source'])
        target_raw = Path(row['destination'])
        target = root / target_raw
        if target_raw.is_absolute() or '..' in target_raw.parts or source.is_symlink():
            raise ValueError('Unsafe source or destination in plan.')
        if not within(source.resolve(), inbox) or not within(target.resolve(), allowed):
            raise ValueError('Plan path escapes the permitted workspace.')
        if target.is_symlink() or any(parent.is_symlink() for parent in target.parents):
            raise ValueError('Destination includes a symlink.')
        if not source.is_file() or digest(source) != row['sha256']:
            raise ValueError('An input changed since the plan was made.')
        if target.exists() and (not target.is_file() or digest(target) != row['sha256']):
            raise ValueError('Destination collision; no files were overwritten.')
        prepared.append((row, source, target))
    for row, source, target in prepared:
        if target.exists():
            actions.append({'destination': row['destination'], 'status': 'already_present'})
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with source.open('rb') as src, target.open('xb') as dst:
                shutil.copyfileobj(src, dst)
        except FileExistsError:
            raise ValueError('Destination appeared during copying; original preserved.')
        if digest(target) != row['sha256']:
            raise ValueError('Copied file failed its hash check; original preserved. Inspect destination.')
        actions.append({'destination': row['destination'], 'status': 'copied', 'sha256': row['sha256']})
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    make = commands.add_parser('plan')
    make.add_argument('--root', type=Path, required=True)
    make.add_argument('--inbox', type=Path, required=True)
    make.add_argument('--output', type=Path, required=True)
    make.add_argument('--module', type=str.upper)
    make.add_argument('--domain', choices=['study', 'work'], default='study')
    run = commands.add_parser('apply')
    run.add_argument('--root', type=Path, required=True)
    run.add_argument('--plan', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'plan':
            if args.module and not MODULE.fullmatch(args.module):
                raise ValueError('Module must be an explicit code, for example ICT111.')
            data = plan(args.root, args.inbox, args.module, args.domain)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
            print(json.dumps({action: sum(r['action'] == action for r in data['files'])
                              for action in ['copy', 'duplicate', 'review']}))
        else:
            data = json.loads(args.plan.read_text(encoding='utf-8'))
            print(json.dumps(apply_plan(data, args.root), indent=2))
        return 0
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f'ERROR: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
