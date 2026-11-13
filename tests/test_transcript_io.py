"""Integration checks for source preservation, segmentation and safe output naming."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'youtube-to-article/scripts/transcript_io.py'
spec = importlib.util.spec_from_file_location('transcript_io', SCRIPT)
io = importlib.util.module_from_spec(spec)
spec.loader.exec_module(io)


class TranscriptIOTests(unittest.TestCase):
    def invoke(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)

    def test_all_real_examples_reconstruct_exactly_and_keep_sources(self):
        examples = list((ROOT / 'transcript_examples').glob('*.md'))
        self.assertEqual(len(examples), 5)
        with tempfile.TemporaryDirectory() as temp:
            for n, source in enumerate(examples):
                with self.subTest(source=source.name):
                    original = source.read_bytes()
                    result = self.invoke('prepare', source, Path(temp) / str(n))
                    self.assertEqual(result.returncode, 0, result.stderr)
                    work = Path(temp) / str(n)
                    manifest = json.loads((work / 'manifest.json').read_text())
                    lines, start, end = io.transcript_region(original.decode('utf-8-sig'))
                    reconstructed = ''.join((work / s['file']).read_text() for s in manifest['segments'])
                    self.assertEqual(reconstructed, ''.join(lines[start:end]))
                    self.assertEqual(manifest['source_sha256'], hashlib.sha256(original).hexdigest())
                    self.assertEqual(source.read_bytes(), original)
                    previous_end = start
                    for segment in manifest['segments']:
                        self.assertEqual(segment['source_start_line'], previous_end + 1)
                        previous_end = segment['source_end_line']
                    self.assertEqual(previous_end, end)

    def test_missing_ambiguous_empty_and_code_headings(self):
        for text in ('hello', '## Transcript\n\n', '## Transcript\na\n## Transcript\nb\n', '```md\n## Transcript\nfake\n```\n'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                io.transcript_region(text)
        text = '---\ntitle: x\n---\n## Transcript\n\n### Topic\n**0:00** · real\n\n## Links\nextra\n'
        lines, start, end = io.transcript_region(text)
        self.assertIn('real', ''.join(lines[start:end]))
        self.assertNotIn('extra', ''.join(lines[start:end]))
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'invalid.md'
            source.write_text('No transcript here.')
            work = Path(temp) / 'work'
            result = self.invoke('prepare', source, work)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(work.exists())

    def test_numbered_outputs_and_source_aliases(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            source = directory / 'lecture.md'
            source.write_text('Original input')
            draft = directory / 'draft.md'
            draft.write_text('# Reviewed article\n')
            first = directory / 'lecture.article.md'
            first.write_text('Keep existing')
            third = directory / 'lecture.article.3.md'
            third.write_text('Keep third')
            second = self.invoke('save', source, draft)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(Path(second.stdout.strip()).name, 'lecture.article.2.md')
            fourth = self.invoke('save', source, draft)
            self.assertEqual(Path(fourth.stdout.strip()).name, 'lecture.article.4.md')
            alias = directory / 'alias.md'
            alias.symlink_to(source)
            saved = self.invoke('save', source, draft, '--output-filename', 'alias.md')
            self.assertEqual(Path(saved.stdout.strip()).name, 'alias.2.md')
            custom = self.invoke('save', source, draft, '--output-filename', 'lecture.md')
            self.assertEqual(Path(custom.stdout.strip()).name, 'lecture.2.md')
            self.assertEqual(source.read_text(), 'Original input')
            self.assertEqual(first.read_text(), 'Keep existing')
            self.assertEqual(third.read_text(), 'Keep third')
            invalid = self.invoke('save', source, draft, '--output-filename', '../escape.md')
            self.assertNotEqual(invalid.returncode, 0)
            self.assertFalse((directory.parent / 'escape.md').exists())

    def test_prepare_never_reuses_existing_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'input.md'
            source.write_text('## Transcript\n\n**0:00** · A claim.\n')
            result = self.invoke('prepare', source, temp)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((Path(temp) / 'manifest.json').exists())


if __name__ == '__main__':
    unittest.main()
