#!/usr/bin/env python3
"""Rebuild the upload packages from the skill source.
Usage (from the repo root):  python3 tools/package.py
Writes dist/cie-skill.zip and dist/cie-skill.skill (identical zips; some uploaders want .zip)."""
import os, sys, zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DIST = os.path.join(ROOT, 'cie-skill'), os.path.join(ROOT, 'dist')
skill_md = os.path.join(SRC, 'SKILL.md')
head = open(skill_md, encoding='utf-8').read().split('---')
if len(head) < 3 or 'name: cie-skill' not in head[1] or 'description:' not in head[1]:
    sys.exit('SKILL.md frontmatter must contain "name: cie-skill" and a description.')
os.makedirs(DIST, exist_ok=True)
skip_dirs, skip_files = {'__pycache__', '.git'}, {'.DS_Store'}
for ext in ('zip', 'skill'):
    out = os.path.join(DIST, f'cie-skill.{ext}')
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for d, dirs, files in os.walk(SRC):
            dirs[:] = sorted(x for x in dirs if x not in skip_dirs)
            for f in sorted(files):
                if f in skip_files or f.endswith('.pyc'):
                    continue
                full = os.path.join(d, f)
                z.write(full, os.path.relpath(full, ROOT))  # keeps the cie-skill/ folder inside the zip
    print('wrote', os.path.relpath(out, ROOT), f'({os.path.getsize(out)//1024} KB)')
