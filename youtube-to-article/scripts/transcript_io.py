#!/usr/bin/env python3
"""Prepare transcript segments or save a reviewed article; no model calls."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


def transcript_region(text):
    """Recognize a unique ATX Transcript heading, outside YAML/fenced code."""
    lines = text.splitlines(keepends=True)
    headings = []
    fence = None
    frontmatter = bool(lines and lines[0].strip() == '---')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if frontmatter:
            if i and stripped in ('---', '...'):
                frontmatter = False
            continue
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            run = mark.group(1)
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not stripped[len(run):].strip():
                fence = None
            continue
        if fence:
            continue
        match = re.match(r'^ {0,3}(#{1,6})\s+(.+?)\s*$', line)
        if match:
            title = re.sub(r'\s+#+$', '', match.group(2)).strip()
            headings.append((i, len(match.group(1)), title))
    starts = [h for h in headings if h[2].casefold() == 'transcript']
    if len(starts) != 1:
        raise ValueError('A unique, clearly marked Transcript section is required; no article generated.')
    start, level, _ = starts[0]
    end = next((i for i, depth, _ in headings if i > start and depth <= level), len(lines))
    body = ''.join(lines[start + 1:end])
    if not body.strip():
        raise ValueError('Transcript section is empty; no article generated.')
    return lines, start + 1, end


def segments(lines, start, end, max_words):
    """Split at blank-line paragraph boundaries, never discard text."""
    result = []
    chunk_start = start
    count = 0
    paragraph_start = start
    for i in range(start, end):
        if not lines[i].strip() or i == end - 1:
            stop = i + 1
            words = len(''.join(lines[paragraph_start:stop]).split())
            if count and count + words > max_words:
                result.append((chunk_start, paragraph_start))
                chunk_start = paragraph_start
                count = 0
            count += words
            paragraph_start = stop
    if chunk_start < end:
        result.append((chunk_start, end))
    return result


def prepare(args):
    source = Path(args.input).resolve(strict=True)
    raw = source.read_bytes()
    text = raw.decode('utf-8-sig')
    lines, start, end = transcript_region(text)
    ranges = segments(lines, start, end, args.max_words)
    work = Path(args.work_directory).resolve()
    work.mkdir(parents=True, exist_ok=False)
    (work / 'context.md').write_text(''.join(lines[:start - 1]), encoding='utf-8')
    entries = []
    for number, (a, b) in enumerate(ranges, 1):
        body = ''.join(lines[a:b])
        name = f'segment-{number:04d}.md'
        (work / name).write_text(body, encoding='utf-8')
        times = re.findall(r'\*\*((?:\d+:)?\d+:\d{2})\*\*', body)
        entries.append({'file': name, 'source_start_line': a + 1,
                        'source_end_line': b, 'words': len(body.split()),
                        'first_timestamp': times[0] if times else None,
                        'last_timestamp': times[-1] if times else None})
    manifest = {'source': str(source), 'source_sha256': hashlib.sha256(raw).hexdigest(),
                'transcript_start_line': start + 1, 'transcript_end_line': end,
                'context_file': 'context.md', 'segments': entries,
                'note': 'Context is not article evidence. Segments need editorial conversion and fidelity review. Paragraphs larger than max_words stay intact. Read adjacent segments for continuity.'}
    (work / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'manifest': str(work / 'manifest.json'), 'segments': len(entries)}, ensure_ascii=False))


def save(args):
    source = Path(args.input).resolve(strict=True)
    draft = Path(args.reviewed_draft).resolve(strict=True)
    if draft == source:
        raise ValueError('Reviewed draft must be separate from the source transcript.')
    content = draft.read_text(encoding='utf-8')
    if not content.strip():
        raise ValueError('Reviewed draft is empty.')
    directory = Path(args.output_path).resolve() if args.output_path else source.parent
    name = args.output_filename if args.output_filename else source.stem + '.article.md'
    if Path(name).name != name or not name.endswith('.md') or name in ('.md', '..md'):
        raise ValueError('Output filename must be a basename ending in .md; use --output-path for its directory.')
    directory.mkdir(parents=True, exist_ok=True)
    base = Path(name).stem
    number = 1
    while True:
        candidate = directory / (name if number == 1 else f'{base}.{number}.md')
        # Resolve aliases before creating, including symlinks to the input.
        if candidate.resolve() == source:
            number += 1
            continue
        try:
            with candidate.open('x', encoding='utf-8') as stream:
                stream.write(content)
        except FileExistsError:
            number += 1
            continue
        print(str(candidate))
        return


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare', help='Extract a marked transcript into lossless sequential segments')
    prep.add_argument('input')
    prep.add_argument('work_directory', help='New directory; never overwrite an existing directory')
    prep.add_argument('--max-words', type=int, default=2500, help='Target segment word limit (default: 2500); paragraphs remain intact')
    prep.set_defaults(run=prepare)
    writer = sub.add_parser('save', help='Save an already reviewed draft without overwriting any file')
    writer.add_argument('input')
    writer.add_argument('reviewed_draft')
    writer.add_argument('--output-path')
    writer.add_argument('--output-filename')
    writer.set_defaults(run=save)
    args = parser.parse_args()
    if getattr(args, 'max_words', 1) <= 0:
        parser.error('--max-words must be positive')
    try:
        args.run(args)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
