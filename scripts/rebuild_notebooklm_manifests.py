#!/usr/bin/env python3
"""Rebuild curated NotebookLM packages for every configured notebook."""
import csv
from workspace import ROOT, config, rows

COLUMNS=('source_id','title','authors','year','source_type','venue','doi_or_url','role',
         'decision','rights','external_upload','upload_state','local_path','drive_path',
         'drive_file_url','notebooklm_status')

def state(row):
    if row.get('external_upload')!='allowed': return 'authorization_required'
    if not row.get('drive_file_url'): return 'drive_upload_required'
    return 'ready_for_import'

def main():
    for notebook in config()['notebooks']:
        selected=[row|{'upload_state':state(row)} for row in rows(ROOT/notebook['memory_dir']/'03 Evidence Ledger.csv')
                  if row.get('decision') in {'accepted','context'}]
        for destination in [ROOT/notebook['source_dir'],ROOT/notebook['memory_dir']/'Exports/NotebookLM']:
            destination.mkdir(parents=True,exist_ok=True)
            with (destination/'source-manifest.csv').open('w',encoding='utf-8',newline='') as handle:
                writer=csv.DictWriter(handle,fieldnames=COLUMNS,extrasaction='ignore',lineterminator='\n')
                writer.writeheader();writer.writerows(selected)
            guide=['# Curated source guide','', 'Notebook scope: '+notebook['id'], '',
                   'Only accepted or contextual evidence appears here. This guide does not authorize upload.', '',
                   '| Source ID | Title | Role | Decision | Upload state | Source location |',
                   '| --- | --- | --- | --- | --- | --- |']
            for row in selected:
                values=[row.get(k,'') for k in ['source_id','title','role','decision','upload_state']]
                values.append(row.get('drive_file_url') or row.get('local_path') or row.get('doi_or_url',''))
                guide.append('| '+' | '.join(v.replace('|','\\|').replace('\n',' ') for v in values)+' |')
            if not selected: guide.extend(['','Awaiting accepted sources. Do not generate factual study content from this empty package.'])
            (destination/'00 Curated Source Guide.md').write_text('\n'.join(guide)+'\n',encoding='utf-8')
        print(f"{notebook['id']}: {len(selected)} curated source(s)")
    return 0

if __name__=='__main__': raise SystemExit(main())
