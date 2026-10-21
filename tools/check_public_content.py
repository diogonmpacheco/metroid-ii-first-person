#!/usr/bin/env python3
"""Check staged publication blobs for this documentation-only scaffold."""
from pathlib import PurePosixPath
import posixpath
import re
import subprocess
import sys

ALLOWED = frozenset({
    '.gitignore', 'README.md', 'CREDITS.md', 'CONTRIBUTING.md',
    'docs/index.md', 'docs/setup.md', 'docs/asset-policy.md',
    'docs/architecture.md', 'docs/roadmap.md',
    '.github/ISSUE_TEMPLATE/config.yml',
    '.github/ISSUE_TEMPLATE/bug_report.yml',
    '.github/ISSUE_TEMPLATE/feature_request.yml',
    '.github/pull_request_template.md',
    '.github/workflows/check-public-content.yml',
    'tools/check_public_content.py',
})
MAX_BYTES = 128 * 1024
SENSITIVE = (
    re.compile(r'/(?:Users|Volumes)/\S+'),
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
)


def git(*args):
    return subprocess.check_output(['git', *args])


def main():
    errors, texts = [], {}
    entries = git('ls-files', '--stage', '-z').split(b'\0')
    for entry in entries:
        if not entry:
            continue
        header, name_bytes = entry.split(b'\t', 1)
        mode, sha, stage = header.decode('ascii').split()
        name = name_bytes.decode('utf-8')
        if name not in ALLOWED:
            errors.append(f'{name}: outside the documentation publication allowlist')
            continue
        if mode not in ('100644', '100755') or stage != '0':
            errors.append(f'{name}: symlinks, submodules and conflicted entries are excluded')
            continue
        size = int(git('cat-file', '-s', sha))
        if size > MAX_BYTES:
            errors.append(f'{name}: exceeds the text-template size limit')
            continue
        payload = git('cat-file', 'blob', sha)
        try:
            text = payload.decode('utf-8')
        except UnicodeDecodeError:
            errors.append(f'{name}: binary/non-UTF-8 payload')
            continue
        if any(ord(c) < 32 and c not in '\t\n\r' for c in text):
            errors.append(f'{name}: binary control bytes')
        if any(pattern.search(text) for pattern in SENSITIVE):
            errors.append(f'{name}: possible private path or credential')
        texts[name] = text
    for name in sorted(ALLOWED - texts.keys()):
        errors.append(f'{name}: required scaffold file is missing from the index')
    for name, text in texts.items():
        if not name.endswith('.md'):
            continue
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            target = target.split('#', 1)[0]
            resolved = posixpath.normpath(str(PurePosixPath(name).parent / target))
            if resolved not in texts:
                errors.append(f'{name}: broken or non-published local link {target}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(texts)} staged text files; allowlist, payload and local links checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
