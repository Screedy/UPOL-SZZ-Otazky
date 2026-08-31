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
  - \N \R \Z \Q \C              -> \mathbb{N} ...  (KaTeX shorthands Obsidian's
                                   MathJax does not know, they render red)
  - text$x$text                 -> text $x$ text  (Docmost padded inline math
                                   visually, Obsidian does not, so it looks cramped)
  - ![](files/<uuid>/img.png)   -> ![[<uuid>.png]] and the asset is flattened to
                                   files/<uuid>.png, so every image has a unique
                                   vault-wide name. Wikilink embeds resolve by
                                   name anywhere in the vault, which survives
                                   folder names containing ":" and duplicate
                                   "obrazek.png" basenames.

Fenced code blocks (```...```) and inline `code` are left byte-for-byte untouched.

Usage:
    python3 docmost_to_obsidian.py [PATH ...]     # files and/or dirs (dirs = *.md recursively)
    python3 docmost_to_obsidian.py --dry-run .    # report only, writes and moves nothing
    python3 docmost_to_obsidian.py --no-unescape  # skip backslash halving (already-converted files)
    python3 docmost_to_obsidian.py --selftest     # run built-in checks
"""
import argparse, html, pathlib, re, shutil, sys, urllib.parse

ESCAPABLE = r"""!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~"""
_unescape = re.compile(r'\\([' + ESCAPABLE + r'])')
_summary = re.compile(r'\s*<summary>(.*?)</summary>\s*$', re.I)
_callout_open = re.compile(r':::([a-z]+)\s*$')
_blackboard = re.compile(r'\\([NRZQC])(?![a-zA-Z])')
# inline math: a single-line $...$ span, never the $$ of a display block
_inline_math = re.compile(r'(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)')
_image = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
_asset = re.compile(r'^(?:/?api/)?files/([0-9a-fA-F-]{36})/(.+)$')

# Invisible junk Docmost leaves behind. Inside math these are fatal: MathJax
# rejects them as unexpected characters and paints the formula red.
INVISIBLES = {
    0x200B: None, 0x200C: None, 0x200D: None, 0xFEFF: None,   # zero-width -> gone
    0x00A0: ' ', 0x202F: ' ', 0x2009: ' ',                    # exotic spaces -> plain space
}

# a "$" glued straight onto one of these needs breathing room
GLUE_BEFORE = '*_)]}'   # ...**DTS**$M$  ->  **DTS** $M$
GLUE_AFTER = '([*_'     # $m=2$(binary) -> $m=2$ (binary);  $n$**v ...** -> $n$ **v ...**
# ...but emphasis wrapping bare punctuation stays tight:  $K$**:**  not  $K$ **:**
_emph_punct = re.compile(r'^[*_]{1,2}[?:.,;!]')


def _space_math(s):
    """Put a space between inline math and text glued to it."""
    out, last = [], 0
    for m in _inline_math.finditer(s):
        pre = s[m.start() - 1] if m.start() else ''
        post = s[m.end()] if m.end() < len(s) else ''
        chunk = m.group(0)
        if pre and (pre.isalnum() or pre in GLUE_BEFORE):
            chunk = ' ' + chunk
        if post and (post.isalnum() or post in GLUE_AFTER) \
                and not _emph_punct.match(s[m.end():]):
            chunk += ' '
        out.append(s[last:m.start()])
        out.append(chunk)
        last = m.end()
    out.append(s[last:])
    return ''.join(out)


def _flatten_asset(path):
    """files/<uuid>/img.png -> ('files/<uuid>.png', '<uuid>.png'), else None."""
    m = _asset.match(urllib.parse.unquote(path).lstrip('/').replace('/api/', '', 1)
                     if path.startswith('/api/') else urllib.parse.unquote(path).lstrip('/'))
    if not m:
        return None
    uuid, name = m.group(1), m.group(2)
    new_name = uuid + pathlib.PurePosixPath(name).suffix
    return 'files/' + new_name, new_name


def _rewrite_images(s, moves):
    def repl(m):
        alt, path = m.group(1), m.group(2)
        flat = _flatten_asset(path)
        if not flat:
            return m.group(0)
        new_rel, new_name = flat
        moves.append((urllib.parse.unquote(path).lstrip('/'), new_rel))
        return f'![[{new_name}|{alt}]]' if alt.strip() else f'![[{new_name}]]'
    return _image.sub(repl, s)


def _inline_pass(text, unescape_backslash, moves):
    """Everything that operates on prose, skipping inline-code spans."""
    parts = []
    for part in re.split(r'(`+[^`]*`+)', text):
        if part.startswith('`'):
            parts.append(part)
            continue
        if unescape_backslash:
            part = _unescape.sub(r'\1', part)
        part = html.unescape(part).translate(INVISIBLES)
        part = _blackboard.sub(r'\\mathbb{\1}', part)
        part = _rewrite_images(part, moves)
        part = _space_math(part)
        parts.append(part)
    return ''.join(parts)


def _strip_title(lines):
    """Drop the leading '# Page title' H1 - Obsidian already shows the filename."""
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith('---'):        # frontmatter, leave the file alone
            return lines
        if re.match(r'#\s+\S', line):     # exactly one '#', so not a '## section'
            rest = lines[i + 1:]
            while rest and not rest[0].strip():
                rest.pop(0)
            return lines[:i] + rest
        return lines
    return lines


def convert(text, unescape_backslash=True, strip_title=True):
    """Returns (new_text, moves). moves = [(old_rel_path, new_rel_path), ...]."""
    out, moves, in_fence, in_callout = [], [], False, False
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
            out.append('#### ' + _inline_pass(m.group(1), unescape_backslash, moves))
            continue
        m = _callout_open.match(s)
        if m and not in_callout:
            out.append(f'> [!{m.group(1)}]')
            in_callout = True
            continue
        if s == ':::' and in_callout:
            in_callout = False
            continue
        p = _inline_pass(line, unescape_backslash, moves)
        if in_callout:
            out.append('>' if p.strip() == '' else '> ' + p)
        else:
            out.append(p)
    if strip_title:
        out = _strip_title(out)
    return '\n'.join(out), moves


def selftest():
    t = lambda s, **k: convert(s, **k)[0]
    assert t(':::note\nhi\n:::') == '> [!note]\n> hi'
    assert t(r'$\\langle$') == r'$\langle$'                    # command un-doubled
    assert t(r'a \\\\ b') == r'a \\ b'                         # real newline kept
    assert t('## 1\\. Foo') == '## 1. Foo'                     # markdown escape dropped
    assert t('$17 &gt; 16$') == '$17 > 16$'                    # entity decoded
    assert t('<details>\n<summary>P</summary>\n\nx\n</details>') == '#### P\n\nx'
    assert t('```\n\\n &gt; $a$b\n```') == '```\n\\n &gt; $a$b\n```'  # code untouched
    # blackboard shorthands
    assert t(r'$f: \N \to \N$') == r'$f: \mathbb{N} \to \mathbb{N}$'
    # math spacing
    assert t('**DTS**$M$je funkce$S(n)$zde') == '**DTS** $M$ je funkce $S(n)$ zde'
    assert t('$m = 2$(binární)') == '$m = 2$ (binární)'
    assert t('$c$-krát a $p$, $q$.') == '$c$-krát a $p$, $q$.'  # punctuation left tight
    assert t('délky$n$**v nejhorším**') == 'délky $n$ **v nejhorším**'  # bold word gets space
    assert t('$K$**:** a $L$**?**') == '$K$**:** a $L$**?**'    # bold punctuation stays tight
    assert t('$$\na \\\\[1em] b\n$$') == '$$\na \\[1em] b\n$$'  # display block safe
    # invisible characters that break MathJax
    assert t('$a​b$') == '$ab$'                           # zero-width space removed
    assert t('$\\text{a b}$') == '$\\text{a b}$'          # nbsp -> plain space
    # leading H1 dropped, section headings kept
    assert t('# Title\n\n## 1. Foo\n\nbody') == '## 1. Foo\n\nbody'
    assert t('## 1. Foo\n\nbody') == '## 1. Foo\n\nbody'
    assert t('# Title\n\nbody', strip_title=False) == '# Title\n\nbody'
    # images
    txt, mv = convert('![](files/019fd79d-b8cd-73ad-b3a6-d492c650d2bf/obrazek.png)')
    assert txt == '![[019fd79d-b8cd-73ad-b3a6-d492c650d2bf.png]]', txt
    assert mv == [('files/019fd79d-b8cd-73ad-b3a6-d492c650d2bf/obrazek.png',
                   'files/019fd79d-b8cd-73ad-b3a6-d492c650d2bf.png')]
    txt, _ = convert('![](/api/files/019ec2d8-b712-74ac-a4dd-7c03af00adbb/Mac@2x.png)')
    assert txt == '![[019ec2d8-b712-74ac-a4dd-7c03af00adbb.png]]', txt
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


def apply_moves(base, moves, dry_run):
    """Flatten files/<uuid>/name.ext -> files/<uuid>.ext. Returns count of missing assets."""
    missing = 0
    for old_rel, new_rel in moves:
        old, new = base / old_rel, base / new_rel
        if new.exists():
            continue
        if not old.exists():
            missing += 1
            continue
        if dry_run:
            print(f'  would move {old_rel} -> {new_rel}')
            continue
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))
        if old.parent.is_dir() and not any(old.parent.iterdir()):
            old.parent.rmdir()
    return missing


def main():
    ap = argparse.ArgumentParser(description='Docmost -> Obsidian markdown converter.')
    ap.add_argument('paths', nargs='*', default=['.'], help='.md files or dirs (default: .)')
    ap.add_argument('--dry-run', action='store_true', help='report, change nothing')
    ap.add_argument('--no-unescape', action='store_true',
                    help='skip backslash halving (for files converted by an earlier run)')
    ap.add_argument('--keep-title', action='store_true',
                    help='keep the leading "# Page title" H1 (default: drop it)')
    ap.add_argument('--selftest', action='store_true', help='run built-in checks and exit')
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    total_missing = 0
    for f in gather(args.paths):
        old = f.read_text(encoding='utf-8')
        new, moves = convert(old, unescape_backslash=not args.no_unescape,
                             strip_title=not args.keep_title)
        if new == old and not moves:
            continue
        if new != old:
            print(('would change: ' if args.dry_run else 'converted: ') + str(f))
            if not args.dry_run:
                f.write_text(new, encoding='utf-8')
        total_missing += apply_moves(f.parent, moves, args.dry_run)
    if total_missing:
        print(f'\nWARNING: {total_missing} image(s) referenced but not on disk '
              f'(re-export from Docmost with attachments).', file=sys.stderr)


if __name__ == '__main__':
    main()
