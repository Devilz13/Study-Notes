#!/usr/bin/env python3
"""Fail when expected generated output is missing, untracked, staged, or modified."""
import subprocess
from workspace import ROOT, config


def expected_outputs(data):
    paths=[]
    for notebook in data['notebooks']:
        for folder in [notebook['source_dir'], notebook['memory_dir']+'/Exports/NotebookLM']:
            paths.extend(folder+'/'+name for name in ['source-manifest.csv','00 Curated Source Guide.md'])
    return paths


def check(root, paths):
    tracked=subprocess.run(['git','ls-files','-z','--',*paths],cwd=root,
                           capture_output=True,text=True,check=True).stdout.split('\0')
    missing=sorted(set(paths)-set(tracked))
    changed=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all','--',*paths],
                           cwd=root,capture_output=True,text=True,check=True).stdout
    messages=['Expected generated file is not tracked: '+path for path in missing]
    if changed: messages.append('Generated outputs differ from the checked-out commit:\n'+changed.rstrip())
    return messages


def main():
    errors=check(ROOT,expected_outputs(config()))
    for message in errors: print('ERROR: '+message)
    if errors: return 1
    print('OK: all expected generated manifests and guides are tracked and current')
    return 0


if __name__=='__main__': raise SystemExit(main())
