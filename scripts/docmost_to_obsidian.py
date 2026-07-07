#!/usr/bin/env python3
r"""Convert a Docmost markdown export into Obsidian-friendly markdown, in place.

Transforms:
  - :::type ... :::             -> Obsidian callouts   > [!type]
  - <details><summary>X</...>   -> a plain "#### X" heading (always expanded,
                                   the collapsible wrapper is dropped)
  - \\langle -> \langle         CommonMark backslash-unescape: halves the escapes
                                   Docmost doubles, so LaTeX commands render and
                                   real "\\" newlines survive; also drops markdown
                                   escapes like 1\. -> 1.  and  \[ -> [
  - &gt; &lt; &amp; ...          -> decoded to > < &  (HTML entities)

Fenced code blocks (```...```) are left byte-for-byte untouched.

Usage:
    python3 docmost_to_obsidian.py [PATH ...]     # files and/or dirs (dirs = *.md recursively)
    python3 docmost_to_obsidian.py --dry-run .    # list what would change, write nothing
    python3 docmost_to_obsidian.py --selftest     # run built-in checks
"""
import argparse, html, pathlib, re, sys

ESCAPABLE = r"""!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~"""
_unescape = re.compile(r'\\([' + ESCAPABLE + r'])')
_summary = re.compile(r'\s*<summary>(.*?)</summary>\s*$', re.I)
_callout_open = re.compile(r':::([a-z]+)\s*$')


def _inline(text, unescape_backslash=True):
    # Only touch text outside inline-code spans so backticked code stays literal.
    parts = []
    for part in re.split(r'(`+[^`]*`+)', text):
        if part.startswith('`'):
            parts.append(part)
            continue
        if unescape_backslash:
            part = _unescape.sub(r'\1', part)
        parts.append(html.unescape(part))
    return ''.join(parts)


def convert(text, unescape_backslash=True):
    """unescape_backslash=False skips the backslash pass (for files already halved)."""
    out, in_fence, in_callout = [], False, False
    for line in text.split('\n'):
        s = line.strip()
        if s.startswith('```'):
            in_fence = not in_fence
            out.append('> ' + line if in_callout else line)
            continue
        if in_fence:
            out.append('> ' + line if in_callout else line)
            continue
        if s in ('<details>', '</details>'):
            continue
        m = _summary.match(line)
        if m:
            out.append('#### ' + _inline(m.group(1), unescape_backslash))
            continue
        m = _callout_open.match(s)
        if m and not in_callout:
            out.append(f'> [!{m.group(1)}]')
            in_callout = True
            continue
        if s == ':::' and in_callout:
            in_callout = False
            continue
        p = _inline(line, unescape_backslash)
        if in_callout:
            out.append('>' if p.strip() == '' else '> ' + p)
        else:
            out.append(p)
    return '\n'.join(out)


def selftest():
    assert convert(':::note\nhi\n:::') == '> [!note]\n> hi'
    assert convert(r'$\\langle$') == r'$\langle$'          # command un-doubled
    assert convert(r'a \\\\ b') == r'a \\ b'               # real newline kept
    assert convert('## 1\\. Foo') == '## 1. Foo'           # markdown escape dropped
    assert convert('$17 &gt; 16$') == '$17 > 16$'          # entity decoded
    assert convert('<details>\n<summary>Příklad</summary>\n\nx\n</details>') == '#### Příklad\n\nx'
    assert convert('```\n\\n &gt;\n```') == '```\n\\n &gt;\n```'  # code left alone
    print('selftest ok')


def gather(paths):
    files = []
    for p in map(pathlib.Path, paths):
        if p.is_dir():
            files += sorted(p.rglob('*.md'))
        elif p.suffix == '.md':
            files.append(p)
        else:
            print('skip (not .md):', p, file=sys.stderr)
    return files


def main():
    ap = argparse.ArgumentParser(description='Docmost -> Obsidian markdown converter.')
    ap.add_argument('paths', nargs='*', default=['.'], help='.md files or dirs (default: .)')
    ap.add_argument('--dry-run', action='store_true', help='report, write nothing')
    ap.add_argument('--selftest', action='store_true', help='run built-in checks and exit')
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    for f in gather(args.paths):
        old = f.read_text(encoding='utf-8')
        new = convert(old)
        if new == old:
            continue
        if args.dry_run:
            print('would change:', f)
        else:
            f.write_text(new, encoding='utf-8')
            print('converted:', f)


if __name__ == '__main__':
    main()
