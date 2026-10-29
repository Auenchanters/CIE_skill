# CIE Skill: exam answer books with Claude

A [Claude skill](https://support.claude.com/en/articles/12512180-using-skills-in-claude) that turns your course material into a **PDF answer book** for a college internal exam (CIE / IA / mid-term / SEE). Every likely question is written in exam wording with its marks, followed by the answer exactly as you should write it, using your class's own diagrams. Every program is compiled and every numerical is computed. After the exam, it scores how close it got.

Built and tested on first-semester CIE-1 papers at Ramaiah Institute of Technology (MSRIT), Bengaluru, October 2026. It works for any course and college; the MSRIT patterns are just a head start.

---

## Does it work?

Tested against six real papers. Honest results:

| Exam | Method | Result |
|---|---|---|
| Maths | Guessing a "most likely paper" | ❌ 1 of 12 parts exact. This is why the skill no longer guesses. |
| Physics | Answering the whole question bank | ✅ 9/9 parts covered |
| C programming | Full answer book, all code run | ✅ 9/9 parts on topic, 7 fully answered (one "find the errors" part was thin; fixed in this version) |
| Mechanical | Teacher's assignment first | ✅ 6/6 parts were assignment questions |

The lesson: **cover everything, prioritise, never bet on a shortlist.** The full evidence is in [`cie-skill/references/lessons-log.md`](cie-skill/references/lessons-log.md).

---

## Download

**Easiest:** download **[`dist/cie-skill.zip`](https://github.com/Auenchanters/CIE_skill/raw/main/dist/cie-skill.zip)**. Don't unzip it; you upload the zip as it is.

**Or clone the repo:**

```bash
git clone https://github.com/Auenchanters/CIE_skill.git
```

---

## Install

### On claude.ai (web) or the Claude desktop app

1. In **Settings**, turn on **Code execution and file creation**. The skill needs it to compile code and build the PDF.
2. Open the **Skills** settings (**Settings → Capabilities → Skills**; in newer versions, **Customize → Skills**).
3. Click **Upload skill** and choose `cie-skill.zip`.
4. Make sure the **cie-skill** toggle is on.

Menus move between app versions. If you can't find it, follow Anthropic's official guide: [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude). Skills availability depends on your plan; the guide says which plans include it.

### In Claude Code

```bash
git clone https://github.com/Auenchanters/CIE_skill.git
mkdir -p ~/.claude/skills
cp -r CIE_skill/cie-skill ~/.claude/skills/
```

On Windows, copy the `cie-skill` folder into `%USERPROFILE%\.claude\skills\`.

Claude Code runs on your own machine, so it needs: Python 3 with Pillow, a LaTeX install with `pdflatex` (TeX Live or MiKTeX, with tcolorbox, listings and tikz), poppler-utils (`pdftoppm`, `pdfinfo`, `pdffonts`), `gcc`, and optionally LibreOffice for reading PPT slides. claude.ai already has all of these.

---

## How to use it

**1. Start a chat and say what you need**, for example:

> Use the CIE skill to make an answer book for Programming in C, CIE-1 on 29 Oct.

**2. Claude will ask you for these. Send as many as you have:**

| # | What | Why it matters |
|---|---|---|
| 1 | **Model question paper.** Also last year's CIE/SEE paper and the question bank, if you have them. | Shows the format and the questions that repeat. |
| 2 | **Syllabus.** Ideally the official portion for this test (the "CIE-1 syllabus" sheet). | Stops it wasting your time on topics outside the portion. |
| 3 | **Notes, if you have them.** Teacher's PDFs, PPT slides, Word files, or photos of notes and slides. | Answers use your class's diagrams and wording, which is what examiners mark against. |
| 4 | **Anything extra.** Teacher's assignment, lab programs, tutorials, hints from class ("do the assignment first"), the exam date and time. | The teacher's assignment predicted 6/6 of the mechanical paper. |

Missing something? Say so; it continues with what you have and tells you what that costs.

**3. You get a PDF answer book**, with:
- A "How to use this book" box: paper format, how reliable the predictions are, and how to write for full marks.
- Every question in exam wording with marks, then the full answer. Stars show priority: ★★★ asked before or in the assignment, ★★ in the syllabus or bank, ★ extra.
- Practice sets for repeating question types (C "write the output", "find the errors", numerical templates).
- An order of study that fits the time you have left.

**4. After the exam**, send a photo of the actual paper:

> Here's the actual paper. Score the answer book against it.

You get a part-by-part comparison: what matched, what was missed, and which priority stars were wrong.

---

## Tips for the best result

- **Get the official portion for this test.** Guessing the portion from lesson numbers was the biggest early mistake.
- **Upload the teacher's assignment.** For mechanical, it predicted the whole paper; last year's paper predicted none of it word for word.
- **Send your actual notes, not generic ones.** Examiners mark against the class's own diagrams and definitions.
- **Collect papers from other sections.** More past papers make the priorities more reliable.
- **Study ★★★ first, but don't skip ★★.** In C, 4 of the 9 parts were ★★.

---

## What's inside

```
CIE_skill/
├── cie-skill/                    # the skill itself (what gets uploaded)
│   ├── SKILL.md                  # workflow Claude follows
│   ├── references/
│   │   ├── lessons-log.md        # scoreboard + 22 lessons from real papers
│   │   ├── msrit-patterns.md     # paper formats per course (maths, physics, C, mech, electronics, Kannada, soft skills)
│   │   ├── answer-formats.md     # how to write each question type for full marks
│   │   ├── c-error-drills.md     # 18 verified "find the errors" items for C
│   │   └── tooling.md            # reading PDFs/PPTs/photos, compiling, LaTeX fixes
│   ├── scripts/
│   │   ├── check_pdf.sh          # compile + visual check of the answer book
│   │   ├── run_c.sh              # strict compile and run for C programs
│   │   └── extract_figures.py    # pull diagrams out of teacher's Word/PPT notes
│   └── assets/template.tex       # answer-book LaTeX template
├── dist/
│   ├── cie-skill.zip             # ready to upload
│   └── cie-skill.skill           # same package, .skill extension
└── tools/package.py              # rebuilds dist/ after you edit the skill
```

---

## Updating the skill

1. Edit files inside `cie-skill/` (for example, add your course's paper format to `references/msrit-patterns.md`, or your exam results to `references/lessons-log.md`).
2. Rebuild the packages: `python3 tools/package.py`
3. Commit and push, then re-upload `dist/cie-skill.zip` in Claude (uploading again replaces the old version).

Scored a paper with it? Open an issue or a pull request with the course, the method, and what matched. Every result makes the next prediction better.

---

## Limitations

- The patterns come from one stream (AI&DS, physics cycle) in one semester. Other sections, cycles and teachers can set papers differently.
- It improves your odds; it does not guarantee the paper. Use the stars to order your study, not to skip topics.
- Where your notes don't cover something, it uses standard textbook content and says so. Check those answers against your class material.
- It's a study tool for preparing before the exam.
