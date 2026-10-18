#!/usr/bin/env python3
"""Create missing module folders and memory maps; never overwrite existing notes."""
import argparse
import csv
import json
import re
from pathlib import Path
from workspace import ROOT,config

def put(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists(): path.write_text(text.rstrip()+'\n',encoding='utf-8')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--module',action='append',help='Explicit course code, for example ICT202')
    args=parser.parse_args()
    data=config(); modules=args.module or data['default_modules']
    for raw in modules:
        code=raw.upper()
        if not re.fullmatch(r'ICT\d{3,4}',code): parser.error('Use an explicit ICT module code.')
        entry=next((n for n in data['notebooks'] if n['id']==code),None)
        if entry is None:
            entry={'id':code,'title':'Samuel - '+code,'kind':'module',
                   'source_dir':data['study_root']+'/'+code,
                   'memory_dir':data['vault_root']+'/'+data['study_root']+'/'+code}
            data['notebooks'].append(entry)
            if code not in data['default_modules']: data['default_modules'].append(code)
        source=ROOT/entry['source_dir']; memory=ROOT/entry['memory_dir']
        folders=['00 Inbox','99 Review','Readings','Labs','Slides/00 Unsorted']
        folders += [f'Assignments/Assignment {n}' for n in data['initial_assignments']]
        folders += [f'Slides/Lesson{n}' for n in data['initial_lessons']]
        links=[]
        for folder in folders:
            put(source/folder/'.gitkeep','')
            if folder.startswith('Assignments/Assignment '):
                filename='00 Assignment Map.md'
            elif folder.startswith('Slides/Lesson'):
                filename='00 Lesson Map.md'
            else: continue
            put(memory/folder/filename,f'---\nnote_type: scope-map\nmodule: {code}\nstatus: awaiting_files\nsource_ids: []\n---\n\n# {code}: {folder}\n\nAwaiting source files.\n')
            links.append(f"- [[{data['study_root']}/{code}/{folder}/{filename[:-3]}|{folder}]]")
        put(memory/'00 Topic Map.md',f'# {code}\n\nAwaiting source files.\n\n'+'\n'.join(links))
        for name in ['01 Research Questions','02 Concept Map','04 Contradictions','05 Misconceptions','06 Recall Queue']:
            put(memory/(name+'.md'),f'# {code}: {name[3:]}\n\nAwaiting source review.')
        template=ROOT/data['notebooks'][0]['memory_dir']/'03 Evidence Ledger.csv'
        with template.open(encoding='utf-8',newline='') as handle: columns=next(csv.reader(handle))
        ledger=memory/'03 Evidence Ledger.csv'
        if not ledger.exists():
            ledger.parent.mkdir(parents=True,exist_ok=True)
            with ledger.open('w',encoding='utf-8',newline='') as handle: csv.writer(handle,lineterminator='\n').writerow(columns)
        for folder in ['Concepts','Sources','Sessions','Exports/NotebookLM']:put(memory/folder/'.gitkeep','')
        put(source/'01 NotebookLM Processing Prompt.md',f'# {code} processing prompt\n\nUse only selected sources. Cite each claim and locator. Report missing evidence. Return an unverified_synthesis handoff with concepts, contradictions, and recall questions. If sources are empty, stop and report awaiting files.')
        put(source/'README.md',f'# {code}\n\nPlace raw files in 00 Inbox. Read README_AI.md at the repository root. Keep new source contents private by default.')
        print(code+': missing folders created; existing files preserved')
    (ROOT/'ecosystem.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    return 0

if __name__=='__main__': raise SystemExit(main())
