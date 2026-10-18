"""Behavioral regressions for the two P2 review findings."""
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'scripts'))
import check_generated


def command(root,*args):
    return subprocess.run(args,cwd=root,text=True,capture_output=True)


class GeneratedOutputTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.paths=['packages/source-manifest.csv','packages/00 Curated Source Guide.md']
        for name in self.paths:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('generated\n')
        command(self.root,'git','init','-q')
        command(self.root,'git','add','.')
        self.commit('initial')

    def tearDown(self):self.temp.cleanup()

    def commit(self,title):
        result=command(self.root,'git','-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm',title)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_clean_generated_outputs_pass(self):
        self.assertEqual(check_generated.check(self.root,self.paths),[])

    def test_deleted_in_commit_then_regenerated_untracked_fails(self):
        target=self.paths[1]
        command(self.root,'git','rm','--',target);self.commit('omit generated guide')
        (self.root/target).write_text('generated\n')
        self.assertEqual(command(self.root,'git','diff','--exit-code').returncode,0)
        errors=check_generated.check(self.root,self.paths)
        self.assertTrue(errors)
        self.assertIn(target,'\n'.join(errors))

    def test_missing_expected_output_fails_even_when_git_is_clean(self):
        command(self.root,'git','rm','--',self.paths[0]);self.commit('omit manifest')
        self.assertTrue(check_generated.check(self.root,self.paths))

    def test_tracked_stale_output_fails(self):
        (self.root/self.paths[0]).write_text('stale\n')
        self.assertTrue(check_generated.check(self.root,self.paths))

    def test_staged_changes_fail(self):
        (self.root/self.paths[0]).write_text('new\n');command(self.root,'git','add','.')
        self.assertTrue(check_generated.check(self.root,self.paths))


class MultiSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.source='Samuel/Samuel Study/Shared References/test-topic'
        self.memory='Obsidian Vault/Samuel/Samuel Study/Shared References/test-topic'
        (self.root/'scripts').mkdir()
        for name in ['workspace.py','validate_study_structure.py','rebuild_notebooklm_manifests.py']:
            shutil.copy2(REPO/'scripts'/name,self.root/'scripts'/name)
        self.data={'vault_root':'Obsidian Vault','default_modules':[], 'initial_assignments':[1,2], 'initial_lessons':[1],
                   'study_root':'Samuel/Samuel Study','notebooks':[{'id':'test-topic','kind':'shared_reference',
                   'source_dir':self.source,'memory_dir':self.memory}]}
        self.write('ecosystem.json',json.dumps(self.data))
        canonical=self.source+'/Sources/Accepted/book.pdf'
        self.write(canonical,'original source')
        self.write('config/retained-sources.json',json.dumps([{'path':canonical,
                   'sha256':hashlib.sha256(b'original source').hexdigest()}]))
        for name in ['00 Topic Map.md','01 Research Questions.md','02 Concept Map.md','04 Contradictions.md',
                     '05 Misconceptions.md','06 Recall Queue.md']:
            self.write(self.memory+'/'+name,'# Test scope\n')
        for name in ['README_AI.md','AGENTS.md','CLAUDE.md','skills/research-study/SKILL.md',self.source+'/01 NotebookLM Processing Prompt.md']:
            self.write(name,'# Instructions\n')
        self.ledger=[self.row('SRC-0001','accepted',canonical),
                     self.row('SRC-0002','accepted'),self.row('SRC-0003','context'),self.row('SRC-0004','rejected')]
        self.ledger[-1]['exclusion_reason']='Out of scope'
        for row in self.ledger[:3]:self.write(self.memory+'/Sources/'+row['source_id']+' - Evidence.md','# Source\n')

    def tearDown(self):self.temp.cleanup()

    def write(self,path,text):
        file=self.root/path;file.parent.mkdir(parents=True,exist_ok=True);file.write_text(text)

    def row(self,sid,decision,path=''):
        return {'source_id':sid,'title':sid,'decision':decision,'exclusion_reason':'','local_path':path,
                'external_upload':'ask','drive_file_url':'','notebooklm_status':'not_added','doi_or_url':'https://example.invalid/paper'}

    def run_validator(self):
        path=self.root/self.memory/'03 Evidence Ledger.csv'
        with path.open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=self.ledger[0].keys(),lineterminator='\n')
            writer.writeheader();writer.writerows(self.ledger)
        rebuild=command(self.root,sys.executable,'scripts/rebuild_notebooklm_manifests.py')
        self.assertEqual(rebuild.returncode,0,rebuild.stderr)
        return command(self.root,sys.executable,'scripts/validate_study_structure.py')

    def test_accepts_multiple_sources_and_notes_with_rejected_candidate(self):
        result=self.run_validator();self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        with (self.root/self.source/'source-manifest.csv').open() as handle: selected=list(csv.DictReader(handle))
        self.assertEqual({r['source_id'] for r in selected},{'SRC-0001','SRC-0002','SRC-0003'})

    def test_canonical_anchor_is_still_required(self):
        self.ledger=self.ledger[1:]
        result=self.run_validator();self.assertNotEqual(result.returncode,0)
        self.assertIn('canonical SRC-0001',result.stdout)

    def test_each_supplemental_row_is_validated(self):
        self.ledger[1]['source_id']='bad'
        result=self.run_validator();self.assertNotEqual(result.returncode,0)
        self.assertIn('Invalid source ID',result.stdout)

    def test_each_curated_source_requires_its_own_note(self):
        (self.root/self.memory/'Sources/SRC-0002 - Evidence.md').unlink()
        result=self.run_validator();self.assertNotEqual(result.returncode,0)
        self.assertIn('source note for SRC-0002',result.stdout)

    def test_duplicate_scoped_id_is_rejected(self):
        self.ledger[1]['source_id']='SRC-0001'
        result=self.run_validator();self.assertNotEqual(result.returncode,0)
        self.assertIn('Duplicate scoped source ID',result.stdout)

    def test_rejected_candidate_requires_a_reason(self):
        self.ledger[-1]['exclusion_reason']=''
        result=self.run_validator();self.assertNotEqual(result.returncode,0)
        self.assertIn('Missing rejection reason',result.stdout)


if __name__=='__main__':unittest.main()
