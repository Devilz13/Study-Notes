#!/usr/bin/env python3
"""Validate configured source packages, Obsidian links, and retained file hashes."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote,urlsplit
from workspace import ROOT,config,rows,safe_path

WIKI=re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
LINK=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
REQUIRED=['00 Topic Map.md','01 Research Questions.md','02 Concept Map.md','03 Evidence Ledger.csv',
          '04 Contradictions.md','05 Misconceptions.md','06 Recall Queue.md']

def resolve(source,target,vault,scopes):
    target=target.strip()
    if target.startswith(('../','./')): return False
    candidates=[vault/(target if target.endswith('.md') else target+'.md')]
    local=source.parent/(target if target.endswith('.md') else target+'.md')
    candidates.append(local)
    for scope in scopes:
        if scope in source.parents or scope==source.parent:
            candidates.append(scope/(target if target.endswith('.md') else target+'.md'))
    if any(p.is_file() for p in candidates): return True
    return '/' not in target and len(list(vault.rglob(target+'.md')))==1

def main():
    errors=[];data=config();vault=ROOT/data['vault_root'];scopes=[]
    for notebook in data['notebooks']:
        memory=safe_path(ROOT,notebook['memory_dir']);source=safe_path(ROOT,notebook['source_dir']);scopes.append(memory)
        for name in REQUIRED:
            if not (memory/name).is_file():errors.append(notebook['id']+': missing '+name)
        if not (memory/'03 Evidence Ledger.csv').exists():continue
        ledger=rows(memory/'03 Evidence Ledger.csv'); ids=set()
        retained=[item for item in json.loads((ROOT/'config/retained-sources.json').read_text())
                  if item['path'].startswith(notebook['source_dir']+'/')]
        if retained:
            anchors=[row for row in ledger if row.get('source_id')=='SRC-0001']
            if len(anchors)!=1 or anchors[0].get('local_path')!=retained[0]['path']:
                errors.append(notebook['id']+': missing or incorrect canonical SRC-0001 row')
        for row in ledger:
            sid=row.get('source_id','')
            if not re.fullmatch(r'SRC-(?:[0-9]{4,}|[A-F0-9]{12})',sid):errors.append('Invalid source ID: '+sid)
            if sid in ids:errors.append('Duplicate scoped source ID: '+notebook['id']+'/'+sid)
            ids.add(sid)
            if row.get('decision') not in {'accepted','context','rejected','unreviewed'}:errors.append('Invalid source decision: '+sid)
            if row.get('decision')=='rejected' and not row.get('exclusion_reason'):errors.append('Missing rejection reason: '+sid)
            if row.get('external_upload') not in {'ask','allowed','not_allowed'}:errors.append('Invalid upload authorization: '+sid)
            if row.get('notebooklm_status') not in {'not_added','added','synced','excluded'}:errors.append('Invalid NotebookLM state: '+sid)
            path=row.get('local_path','')
            if path and not safe_path(ROOT,path).is_file():errors.append('Missing source file: '+path)
            if row.get('decision') in {'accepted','context'}:
                matches=[p for p in (memory/'Sources').glob('*.md') if p.stem==sid or p.stem.startswith(sid+' - ')]
                if len(matches)!=1:errors.append(notebook['id']+': expected one source note for '+sid)
        for note in (memory/'Sources').glob('SRC-*.md'):
            match=re.match(r'(SRC-(?:[0-9]{4,}|[A-F0-9]{12}))(?: - |$)',note.stem)
            if match and match.group(1) not in ids:errors.append('Source note has no ledger entry: '+str(note))
        curated={r['source_id'] for r in ledger if r.get('decision') in {'accepted','context'}}
        for folder in [source,memory/'Exports/NotebookLM']:
            manifest=folder/'source-manifest.csv'
            if not manifest.is_file():errors.append('Missing manifest: '+str(manifest));continue
            selected=rows(manifest)
            if {r['source_id'] for r in selected}!=curated:errors.append('Stale manifest: '+str(manifest))
            for row in selected:
                if row.get('upload_state')=='ready_for_import' and (row.get('external_upload')!='allowed' or not row.get('drive_file_url')):
                    errors.append('Manifest overstates upload readiness: '+row['source_id'])
        if not (source/'01 NotebookLM Processing Prompt.md').is_file():errors.append('Missing notebook prompt: '+notebook['id'])
    for item in json.loads((ROOT/'config/retained-sources.json').read_text()):
        path=safe_path(ROOT,item['path'])
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:errors.append('Retained source changed: '+item['path'])
    for path in vault.rglob('*'):
        if path.suffix.lower() in {'.pdf','.pptx','.docx','.xlsx'}:errors.append('Source binary is inside vault: '+str(path))
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts or '.local' in path.parts:continue
        text=re.sub(r'```.*?```','',path.read_text(encoding='utf-8'),flags=re.S)
        if vault in path.parents:
            for target in WIKI.findall(text):
                if not resolve(path,target,vault,scopes):errors.append(f'{path.relative_to(ROOT)}: unresolved [[{target}]]')
        for target in LINK.findall(text):
            if urlsplit(target).scheme or target.startswith('#') or '<' in target:continue
            dest=unquote(target.split('#')[0])
            if dest and not (path.parent/dest).exists():errors.append(f'{path.relative_to(ROOT)}: broken file link {target}')
    for name in ['README_AI.md','AGENTS.md','CLAUDE.md','skills/research-study/SKILL.md']:
        if not (ROOT/name).is_file():errors.append('Missing shared instruction file: '+name)
    for code in data['default_modules']:
        for number in data['initial_assignments']:
            if not (ROOT/data['study_root']/code/f'Assignments/Assignment {number}').is_dir():errors.append('Missing assignment folder')
        for number in data['initial_lessons']:
            if not (ROOT/data['study_root']/code/f'Slides/Lesson{number}').is_dir():errors.append('Missing lesson folder')
    if errors:
        for error in errors:print('ERROR: '+error)
        return 1
    print(f"OK: {len(data['notebooks'])} notebook packages; two module hierarchies; source hashes; memory and skill links")
    return 0

if __name__=='__main__':raise SystemExit(main())
