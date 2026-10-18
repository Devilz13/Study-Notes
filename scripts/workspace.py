"""Shared paths for the Samuel research-study workspace."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def config(root=ROOT):
    return json.loads((root/'ecosystem.json').read_text(encoding='utf-8'))

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))

def safe_path(root, relative):
    path=Path(relative)
    resolved=(root/path).resolve()
    if path.is_absolute() or '..' in path.parts or root.resolve() not in resolved.parents:
        raise ValueError('Path escapes the workspace: '+relative)
    return resolved
