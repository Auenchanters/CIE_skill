---
name: cie-skill
description: Build exam-ready answer books (PDF) for college internal exams (CIE/IA), mid-terms, unit tests and semester exams from a student's question banks, past papers, model papers, assignments, lab manuals, tutorials, syllabus and class notes, then score the result after the exam. It always starts by asking the student for the model question paper, the syllabus, and their notes (PDFs, PPTs, photos), plus anything extra. Use this skill whenever a student shares question papers, PYQs, question banks, model questions, assignments, lab programs, lesson plans or class notes and asks to predict the paper, make study material or an answer book, "make the same PDF as before", prepare for a CIE/IA/internal/SEE, or check how close a prediction was, even if they never say "CIE". Covers theory, numerical, programming (C), language (e.g. Kannada) and soft-skills papers. Built from MSRIT (Ramaiah) first-semester exams but applies to any course.
---

# CIE Skill: exam answer books that cover the paper

This skill turns a pile of course material into one PDF **answer book**: every likely question written in exam wording, followed by the answer exactly as it should be written for full marks, with every number and program verified and the class's own diagrams. After the exam it scores the result honestly so the method keeps improving.

It has been tested on six real CIE-1 papers. The evidence behind every rule is in `references/lessons-log.md`; read it the first time you use this skill in a conversation. Per-course paper patterns are in `references/msrit-patterns.md`.

## What the evidence says (read before planning)

| Exam | Method | Result |
|---|---|---|
| Maths | Shortlist "most likely paper" | 1/12 parts exact. The question bank alone had 5/12 verbatim. |
| Physics | Full-bank coverage | 9/9 parts covered; theory verbatim, numericals same template with new numbers. |
| C programming | Full-bank answer book | 9/9 parts on topic, 7 fully answered; 4 of 9 parts were ★★ (never asked before). Gap: a 5-snippet "find the errors" part when the bank had 1 example. |
| Mechanical | Teacher's assignment first | 6/6 parts were assignment questions. Last year's paper: 0/6 verbatim. |

Three conclusions drive the workflow:
1. **Cover the bank; don't bet on a shortlist.** Stars order study; they never decide what to leave out.
2. **This term's teacher signals beat last year's paper.** An assignment set by the current teacher predicted 6/6; topics promoted only because last year asked them scored 0.
3. **Drill every question type, not just every topic.** A type that was a 1-mark sub-part last year can be a 5-mark part this year.

## Workflow

Follow these steps in order. Tell the student plainly which steps you could not do (e.g. "no past papers, so priorities come from the assignment only").

### Step 0: Ask for the inputs (always, before anything else)
Start every new course by asking for these in **one short message**, even if the request looks complete. List what you already received and ask only for what is missing; then wait for the reply.

1. **Model question paper(s).** Also last year's CIE/SEE papers for the same course and the question bank, if they have them.
2. **Syllabus.** Ideally the official portion for this specific test (e.g. the "CIE-1 syllabus" sheet), not just the full course syllabus.
3. **Notes, if they have them.** Class notes, the teacher's PDFs, PPT slides, Word documents, or photos of handwritten notes and slides. The class's own diagrams and wording come from here.
4. **Anything extra.** Teacher-set assignments, lab programs or tutorials, teacher hints ("assignment questions first"), the exam date and time, and the paper format if known.

Example:
> To build your answer book, send: (1) the model question paper, plus last year's paper or the question bank if you have them; (2) the syllabus, ideally the official portion for this test; (3) your notes, if you have any: PDFs, PPTs or photos; (4) anything extra, like the teacher's assignment, lab programs, hints from class, and the exam date.

If the student says they don't have an item, go ahead with what exists and state the cost in one line (no syllabus → the portion is a guess and is labelled *uncertain portion*; no past or model paper → priorities come from the syllabus and assignment only; no notes → answers use standard textbook content and diagrams, which may not match the class). Ask once; never refuse to start because an item is missing.

### Step 1: Pin down the portion and the format
Ask for the **official portion/syllabus for this specific test** (e.g. a "CIE-1 syllabus" sheet). Never infer the portion from lesson numbers like "L1–L13": in physics that guess starred out-of-portion topics and under-rated one that came as a 5-marker. Notes that say "CIE syllabus ends here" can also be wrong (soft skills: last year's paper asked past that line).
- If no official portion exists, use the assignment and notes the student received, and say so.
- A topic you're unsure about is **"uncertain portion"**, a separate label from **low priority**. Cover it compactly; never tell the student to skip it on a guess.
- Record the paper format if known (questions × marks, compulsory question, choice rules); `references/msrit-patterns.md` has the formats seen so far.

### Step 2: Collect and inventory the sources
Gather what the student sent in Step 0, and note what is missing: question bank / model questions; **teacher-set assignments for this term**; past papers for the **same test** (and other sections' versions); the SEE; tutorials and **lab programs**; lesson plan or syllabus; class notes, slides, teacher documents; textbook pages. Ask about **teacher instructions** (e.g. "complete the assignment questions first"); the teacher's order beats yours.
For reading files (scans, docx images, PDF figures) see `references/tooling.md`.

### Step 3: Map past papers to sources and rank the sources
For each past-paper part, find its source: assignment, QB item, model paper, tutorial/lab, or "new". Count verbatim repeats, same-type-new-numbers, and new questions. Put this table near the start of the PDF; it tells the student why to trust the sheet.

Rank sources in this order when they disagree (evidence in the lessons log):
1. **This term's teacher-set assignment and explicit teacher instructions** (mech: 6/6).
2. **Last year's paper for the same test** (physics: 6/9 near-verbatim; mech: 0/6). Measure it per course; it varies.
3. **Question bank** (maths: 5/12 verbatim).
4. **Tutorials and lab programs**: they return as the same template with new numbers.
5. **Model papers** (maths: 1/12).

A topic seen only in last year's paper stays ★★★, but goes **after** the assignment items in the study order.

### Step 4: Build the bank with coverage, not a shortlist
Answer **every** assignment, question-bank, model, tutorial and lab item in the portion, plus every syllabus topic. Stars:
- ★★★: appeared in a past paper for this course, **or** is a teacher-set assignment question.
- ★★: in the syllabus, bank, notes, tutorials or lab manual.
- ★: notes-only extras (not in the syllabus list).
- Plus a separate tag: *uncertain portion*.

Tag each answer with its source (e.g. `Asked: CIE-1 2025 Q2(c); Assignment 1 Ch.2 Q3`). Then add four things a topic list misses:
- **Type drills.** List every question *type* in the past papers (write the output, evaluate the expression step by step, find the errors, classify valid/invalid, differentiate, sketch and explain, numerical template). Give each type a drill set of **8–15 items**, not one example. For C "find the errors", start from `references/c-error-drills.md`.
- **Difference tables** for every pair of related concepts in the portion (compiler/interpreter, high-level/machine language, while/do-while, ferrous/non-ferrous, getchar/scanf…), even when the bank only asks to "explain" one of them.
- **Modular answers.** Papers join two topics in one 5-marker ("data types + storage classes", "define lathe + working principle"). Keep each answer self-contained and sized so two halves can be combined.
- **Parameterised templates.** For lab programs and tutorial numericals, solve once with the numbers as named constants and show where new numbers plug in (the electricity-bill slabs changed from 100/100/200 to 200/200/400).

For numericals, solve one of each type fully and give final answers for its twins.

### Step 5: Align with what the class was taught
Examiners mark against their own textbook and notes, so:
- **Use the class's diagrams.** Extract figures from the teacher's docx/PDF notes and embed them next to the matching answer (see `references/tooling.md`). Only draw your own schematic when the notes have none, and label it as such.
- **Match the textbook's classifications, formulas and wording.** When your version differs from the textbook, the textbook wins.
- **Check the class material for errors** and correct them visibly (e.g. a slide saying metals form anions).
- **Flag assignment questions the notes don't cover** (mech: the thermal plant came as an 8-marker and its answer was from a standard textbook, not the class notes). Ask the student early for the textbook page or slides for those; they are the likeliest questions with the weakest source.
- **Follow the teacher's order** if one was given.

### Step 6: Verify everything you can compute
- Every numerical: compute with Python using **the constants printed on the paper**.
- Every C program, "write the output" and "find the error" item: compile and run with `scripts/run_c.sh` (strict flags, timeout for infinite loops); paste real output.
- **gcc is not the examiner.** gcc accepts `$num1` as an identifier (an extension; it is invalid in standard C), compiles `printf("%d", &a)` with only a warning, and silently compiles `while (k <= 3);` into an infinite loop. Answer by the textbook rule, and use the compiler only to confirm.
- Flag undefined behaviour (e.g. `x++ * 2 + --x`): give the answer the examiner expects plus a one-line UB note for the student to write.
- Tutorial typos (unphysical results, unit slips): show the method, give both answers, and tell the student to state the assumption.
- Say where an answer is from standard knowledge rather than the student's notes.

### Step 7: Write the answer book
Use `assets/template.tex` and its `qa` box. The student rejected reference-style notes ("I'm studying to score full marks, not to gain knowledge") and cross-references ("see A4"), so every block is:
1. The question **in exam wording**, with its marks, and a grey line saying where it was asked before.
2. **"Answer:"** followed by the answer exactly as it should be written in the exam: diagram, labelled parts, working, table, program, real output, boxed final answer.
3. **Self-contained**: repeat a figure or table rather than pointing to another block.

Structure:
1. Title, exam date/time, portion, paper format.
2. "How to use this book" box: format, how reliable the book is (with the numbers from Step 3), priority legend, how to write for full marks.
3. Evidence table (past part → source), or a statement that priorities come from the assignment/syllabus.
4. Parts in the teacher's order, or: compulsory/always-asked types first (with their drill sets), then ★★★ "asked before", then ★★ syllabus, then programs/numericals.
5. Final "order of study" box sized to the time left.

Answer patterns per question type are in `references/answer-formats.md`.

**Visual QA is mandatory:** run `scripts/check_pdf.sh main.tex` and look at every page montage. Fix overlapping labels, clipped figures, overfull boxes, and bitmap (Type 3) fonts.

**Deliver early:** copy the PDF to `/mnt/user-data/outputs/` and call `present_files` as soon as it compiles cleanly, then refine. Long builds can hit tool-call limits before delivery.

### Step 8: After the exam, score it and update the log
When the student sends the actual paper:
1. Table: each part → in the book? (verbatim / same type / partial / missing), its star, and its source.
2. Report: verbatim hits, type coverage, **marks reachable studying ★★★ only vs ★★★ + ★★**, which source predicted best, any star that was wrong and why, and the lesson.
3. If you have no book for that course in the conversation history, say so; don't invent a comparison. Record the paper format anyway.
4. Append the result to `references/lessons-log.md` and the format to `references/msrit-patterns.md` if the student is updating the skill. Be blunt about misses; the student relies on this to calibrate trust.

## Course types
- **Theory and numerical (maths, physics, electronics, mechanical):** Steps 0–8 as written.
- **Programming (C):** "write the output" and "find the errors" are near-certain in the compulsory question; drills and compiled outputs matter most.
- **Language (e.g. Kannada Kali):** fixed templates (12-line self-introduction, introduction to the language, alphabet chart), vocabulary with English meaning and a sentence each, question-word and case-ending drills, jumbled-sentence practice. See `references/msrit-patterns.md`.
- **Soft skills:** L3 "apply to this context" questions. Answers name the concept, apply it to the given scenario, and end with a conclusion; practise re-framing each concept for several contexts.

## Communication rules
- Be direct and honest. Lead with the verdict and the numbers. Never claim a prediction is reliable without evidence.
- State limits up front: no past papers, unknown format, unconfirmed portion, answers not from their notes.
- Give a study order that fits the hours left, and say what to skip only if it is truly out of portion.
- Patterns were observed in one college, one stream and one year; a different section, cycle or teacher can change them. Re-check with the student's own papers.
- Keep chat replies short; the PDF carries the content.
