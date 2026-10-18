"""Copy-only intake must preserve originals and resist unsafe plans."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('organizer',REPO/'skills/research-study/scripts/organize_files.py')
organizer=importlib.util.module_from_spec(spec);spec.loader.exec_module(organizer)


class FileIntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.inbox=self.root/'Samuel/Samuel Study/00 Inbox';self.inbox.mkdir(parents=True)

    def tearDown(self):self.temp.cleanup()

    def source(self,name,text='source'):
        path=self.inbox/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text);return path

    def plan(self):return organizer.plan(self.root,self.inbox,None,'study')

    def test_routes_and_copies_with_original_preserved(self):
        source=self.source('ICT111_Lesson1.txt');data=self.plan()
        self.assertEqual(data['files'][0]['action'],'copy')
        organizer.apply_plan(data,self.root)
        target=self.root/data['files'][0]['destination']
        self.assertEqual(target.read_bytes(),source.read_bytes());self.assertTrue(source.exists())
        self.assertEqual(self.plan()['files'][0]['action'],'duplicate')

    def test_ambiguous_file_and_conflicting_module_are_held(self):
        self.source('unknown.txt');self.source('ICT111 ICT201 Assignment 1.txt')
        self.assertTrue(all(r['action']=='review' for r in self.plan()['files']))

    def test_changed_input_is_rejected(self):
        source=self.source('ICT111 Assignment 1.txt');data=self.plan();source.write_text('changed')
        with self.assertRaises(ValueError):organizer.apply_plan(data,self.root)

    def test_parent_traversal_is_rejected(self):
        self.source('ICT111 Lesson1.txt');data=self.plan();data['files'][0]['destination']='../escape.txt'
        with self.assertRaises(ValueError):organizer.apply_plan(data,self.root)

    def test_destination_collision_is_preserved(self):
        self.source('ICT111 Lesson1.txt');data=self.plan();target=self.root/data['files'][0]['destination']
        target.parent.mkdir(parents=True);target.write_text('other version')
        with self.assertRaises(ValueError):organizer.apply_plan(data,self.root)
        self.assertEqual(target.read_text(),'other version')

    def test_work_source_is_held_in_public_study_scope(self):
        self.source('Samuel Work/ICT111 Lesson1.txt')
        self.assertEqual(self.plan()['files'][0]['action'],'review')


if __name__=='__main__':unittest.main()
