# Tooling notes (sandbox)

## Reading sources
- Phone photos of papers: crop and zoom the dense parts (code snippets, tables) with PIL before transcribing; small fonts misread easily (commas vs semicolons in `for`).
- Always read the file-reading skill before touching uploads. PDFs: `pdfinfo` + `pdffonts`. No fonts means a scan: rasterize with `pdftoppm -r 60 -png file.pdf p` and view montages (3 pages side by side) to read them.
- docx text: `extract-text file.docx`. **docx figures:** run `scripts/extract_figures.py file.docx outdir` to map each image to the paragraph text before it (this tells you which figure is "Facing", "Thread cutting", etc.) and produce a contact sheet to view.
- **PPT/PPTX notes:** text with `extract-text slides.pptx`; embedded pictures with `scripts/extract_figures.py slides.pptx outdir` (each labelled with its slide number and title). Diagrams drawn with PowerPoint shapes are not pictures: render the deck with `soffice --headless --convert-to pdf slides.pptx`, then `pdftoppm -r 80 -png slides.pdf s` and crop the slide you need. Convert old `.ppt`/`.doc` first with `soffice --headless --convert-to pptx` (or `docx`).
- PDF figures: `pdfimages -png file.pdf prefix`, skip tiny logos (< 120×80 px), contact-sheet the rest.
- Images the student pastes in chat are also on disk under /mnt/user-data/uploads and can be embedded directly.

## Verification
- Python for numericals (math/sympy). Print every intermediate value you put in the PDF.
- C: `scripts/run_c.sh prog.c [input.txt]` compiles with `-Wall -Wextra -std=c11 -pedantic -fno-dollars-in-identifiers`, prints every diagnostic, and runs with a 2 s timeout (exit 124 = infinite loop, 136 = division by zero). Paste the real stdout. `gcc -w` shows UB lines' actual output; still flag them.
- Without `-fno-dollars-in-identifiers`, gcc accepts `$num1` silently, even with `-pedantic`. Several exam "errors" are only warnings (`printf("%d", &a)`, `if (x = 10)`) or produce no diagnostic at all (`while (k <= 3);`). The compiler confirms; the textbook rule decides the answer.
- For interactive programs, a pseudo-terminal (Python `pty.fork`) gives a transcript that shows typed input, which looks like the exam's "sample output".

## LaTeX (pdflatex, OT1 fonts; cm-super is NOT installed)
- Bitmap Type 3 fonts appear (blurry) if you use: `\$` (use `\symbol{36}` in tt), `\S` (write "Sec."), `\textbullet` (set `\renewcommand{\labelitemi}{$\bullet$}`), `upquote`/`\textquotesingle`. Check with `pdffonts main.pdf | grep "Type 3"`.
- In `\texttt`: `~` → `\symbol{126}`, `^` → `\symbol{94}`; in normal text `|`, `<`, `>` must be in math mode.
- `\lstinline` breaks inside tabularx; use longtable/tabular with escaped `\texttt{}` instead. `lstlisting` works inside tcolorbox environments.
- Add `longtable` and `graphicx` to the preamble when used. Wrap wide TikZ figures in `\resizebox{\linewidth}{!}{...}`.
- When generating LaTeX from Python, use `r"..."` (double-quoted raw strings) for any text containing `''` closing quotes.
- Compile twice; then run `scripts/check_pdf.sh main.pdf` and look at the montages.

## Delivery
Copy to /mnt/user-data/outputs/ and call present_files as soon as the first clean build exists; refine afterwards.
