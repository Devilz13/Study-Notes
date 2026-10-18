#!/usr/bin/env python3
"""Install the portable research-study skill for Claude Code and/or Codex."""
import argparse
import shutil
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent',choices=['claude','codex','both'],required=True)
    parser.add_argument('--replace',action='store_true',help='Replace an existing skill after making a sibling backup.')
    args=parser.parse_args()
    source=Path(__file__).resolve().parents[1]/'skills/research-study'
    names=['claude','codex'] if args.agent=='both' else [args.agent]
    destinations=[Path.home()/('.claude' if n=='claude' else '.codex')/'skills/research-study' for n in names]
    for destination in destinations:
        if destination.is_symlink(): parser.error('Refuse to replace a symlink: '+str(destination))
        if destination.exists():
            if not args.replace: parser.error('Existing skill found. Review it before using --replace: '+str(destination))
            backup=destination.with_name('research-study.backup')
            if backup.exists(): parser.error('Backup already exists: '+str(backup))
    for destination in destinations:
        if destination.exists(): destination.rename(destination.with_name('research-study.backup'))
        shutil.copytree(source,destination)
        print(str(destination))
    return 0

if __name__=='__main__': raise SystemExit(main())
