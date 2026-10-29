#!/usr/bin/env python3
"""Extract images from teacher notes (.docx or .pptx), label each with the text around it, and make a contact sheet.
Usage: python3 extract_figures.py notes.docx|slides.pptx outdir
docx: each image is labelled with the paragraph text just before it (e.g. "Facing", "Thread cutting").
pptx: each image is labelled with its slide number and the slide's text (title first).
Old .ppt/.doc: convert first with  soffice --headless --convert-to pptx file.ppt  (or docx)."""
import sys, os, re, zipfile, xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
z = zipfile.ZipFile(src)
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
rows = []

def save(member, name):
    with open(os.path.join(out, name), 'wb') as f:
        f.write(z.read(member))

if src.lower().endswith('.docx'):
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    V = '{urn:schemas-microsoft-com:vml}'
    rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
    doc = ET.fromstring(z.read('word/document.xml'))
    last = ''
    for p in doc.iter(W + 'p'):
        t = ''.join(x.text or '' for x in p.iter(W + 't')).strip()
        ids = [b.get(R + 'embed') for b in p.iter(A + 'blip')] + [b.get(R + 'id') for b in p.iter(V + 'imagedata')]
        if t: last = t
        for i in ids:
            target = rels.get(i)
            if not target: continue
            name = os.path.basename(target); save('word/' + target, name)
            rows.append((name, last[:80]))
elif src.lower().endswith('.pptx'):
    slides = sorted((n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)),
                    key=lambda n: int(re.findall(r'\d+', n)[-1]))
    for sl in slides:
        k = int(re.findall(r'\d+', sl)[-1])
        relp = f'ppt/slides/_rels/slide{k}.xml.rels'
        rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read(relp))} if relp in z.namelist() else {}
        x = ET.fromstring(z.read(sl))
        text = ' | '.join(t.text.strip() for t in x.iter(A + 't') if t.text and t.text.strip())
        for b in x.iter(A + 'blip'):
            target = rels.get(b.get(R + 'embed'))
            if not target: continue
            member = os.path.normpath(os.path.join('ppt/slides', target)).replace('\\', '/')
            name = f's{k:02d}_' + os.path.basename(target); save(member, name)
            rows.append((name, f'slide {k}: {text[:70]}'))
else:
    sys.exit('Give a .docx or .pptx file (convert .ppt/.doc with soffice first).')

for n, ctx in rows: print(f'{n}\t{ctx}')
thumbs = []
for n, _ in rows:
    try:
        im = Image.open(os.path.join(out, n)).convert('RGB')
    except Exception:
        continue  # emf/wmf etc.: convert separately if needed
    sz = im.size; im.thumbnail((260, 200))
    c = Image.new('RGB', (270, 225), 'white'); c.paste(im, (5, 20)); ImageDraw.Draw(c).text((5, 3), f'{n} {sz}', fill='red'); thumbs.append(c)
if thumbs:
    cols = 6; rws = (len(thumbs) + cols - 1) // cols
    sheet = Image.new('RGB', (270 * cols, 225 * rws), 'white')
    for k, t in enumerate(thumbs): sheet.paste(t, ((k % cols) * 270, (k // cols) * 225))
    sheet.save(os.path.join(out, 'contact_sheet.png')); print('contact sheet:', os.path.join(out, 'contact_sheet.png'))
