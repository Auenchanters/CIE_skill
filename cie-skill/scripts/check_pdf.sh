#!/bin/bash
# Usage: check_pdf.sh main.tex   (compiles twice, reports problems, renders page montages)
set -u
TEX="$1"; BASE="${TEX%.tex}"
pdflatex -interaction=nonstopmode "$TEX" > /tmp/l1.txt; pdflatex -interaction=nonstopmode "$TEX" > /tmp/l2.txt
echo "Errors:";   grep -E "^!" -A2 /tmp/l2.txt | head -20
echo "Overfull boxes: $(grep -c Overfull /tmp/l2.txt)"
echo "Pages: $(pdfinfo "$BASE.pdf" | awk '/Pages/{print $2}')"
echo "Type 3 (bitmap) fonts: $(pdffonts "$BASE.pdf" | grep -c 'Type 3')"
rm -f /tmp/chk-*.png; pdftoppm -r 45 -png "$BASE.pdf" /tmp/chk
python3 - << 'PY'
import glob
from PIL import Image
fs=sorted(glob.glob('/tmp/chk-*.png')); ims=[Image.open(f) for f in fs]
if ims:
    w,h=ims[0].size
    for k in range(0,len(ims),6):
        sub=ims[k:k+6]; o=Image.new('RGB',(w*len(sub),h),'white')
        for i,im in enumerate(sub): o.paste(im,(i*w,0))
        o.save(f'/tmp/montage_{k//6}.png'); print('montage:',f'/tmp/montage_{k//6}.png')
PY
