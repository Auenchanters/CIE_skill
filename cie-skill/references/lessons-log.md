# Lessons log (evidence behind the rules)

Source: MSRIT (Ramaiah Institute of Technology) first semester, CIE-1, 27–29 Oct 2026. AI&DS (CSE stream), physics cycle. One student's papers; other sections and cycles may differ.

## Scoreboard

| Exam | Method used | Result |
|---|---|---|
| Maths 26MAC11 (27 Oct) | Shortlist "most likely paper" from QB + model papers | **1/12** parts exact from the mock; ~9/12 question types covered. The question bank had **5/12 verbatim** (+2 variants), the same rate as the previous year's CIE-1 (5/12). Model papers contributed 1/12. The strongest pick (in 4 sources) did not appear. |
| Physics 26PYC12 (28 Oct) | Full-bank coverage (all model Qs + all tutorials) | **9/9** parts covered. All 6 theory parts verbatim or near-verbatim; **6/9** repeated last year's CIE-1 almost word for word. All 3 numericals were tutorial templates with **new numbers** (0 verbatim). |
| C 26PSCCS14 (29 Oct) | Full-bank answer book (36 pp), every program and output run with gcc | **9/9** parts on topic. Near-verbatim: 5 (identifier rules + classify; switch calculator; compiler vs interpreter; storage classes; while vs do-while). Same template, new numbers: 2 (evaluate expressions step by step; electricity bill with slabs 200/200/400 instead of the lab's 100/100/200). Partial: 2 (high-level vs machine language existed only as prose, not a difference table; **"find the errors" had 5 snippets, the book had 1 example**). **4/9 parts were ★★** (never asked before: getchar/putchar program, data types, HLL vs MLL, electricity-bill lab). "Structure of a C program", in all 3 past papers, did **not** come. ★★★-only study reaches ~22/30; ★★★ + ★★ reaches 30/30 (by choosing Q3). |
| Mech 26ESC134 (29 Oct) | Assignment-first bank, class figures, last year's paper solved as "Part 0" | **6/6** parts covered, **all 6 are Assignment-1 questions** (★★★). 2 word for word (role of ME in manufacturing and marine sectors; ferrous vs non-ferrous), 4 reworded (hydro plant; thermal plant + 2 adv/disadv; define lathe + working principle; sketch two lathe operations). Last year's CIE-1: **0/6 verbatim**, 2/6 same topic. Drilling and milling, promoted to ★★★ only because last year asked them: **0 marks**. CNC/3D printing (uncertain portion): not asked. ★★★-only study reaches 30/30. |
| Kannada Kali 26HSCP16K (28 Oct) | No book was made in this project | Not scored. Format recorded in `msrit-patterns.md`. |
| ESC133 (IEC) | Full bank built with skill v1 | Not scored yet (paper not shared). |
| Soft Skills | Quiz + solved past paper, no book | Not scored. Format from last year's paper recorded in `msrit-patterns.md`. |

## Lessons

1. **Coverage beats prediction.** Never make a shortlist the main product. (Maths; reconfirmed by C, where 4/9 parts were ★★.)
2. **Get the official portion first.** Guessing from lesson numbers caused two physics errors: out-of-portion topics starred ★★★, and holography rated ★ "maybe out" came as a 5-marker.
3. **"Uncertain portion" ≠ "low priority."** Cover uncertain topics; label them.
4. **Last year's paper for the same test is a strong predictor in some departments** (physics: 6/9) and weak in others (mech: 0/6 verbatim; maths: types only). Measure it per course.
5. **Theory repeats verbatim; numericals change numbers.** Memorise theory answers; learn numerical methods.
6. **Verify by execution.** Every C output and program run with gcc; every physics/maths number computed in Python. Two past-paper C items were undefined behaviour; give the expected answer and a UB note.
7. **Tutorial sheets contain typos** (e.g. "1064 µm" for Nd:YAG, "10 mW" giving a 20 m wavelength). Flag them; show the method; give both readings.
8. **Use the class's diagrams and the textbook's classification.** The first mech PDF used self-drawn diagrams and a different material classification from the textbook; the rebuilt PDF embeds the teacher's figures.
9. **Follow the teacher's study order** ("assignment questions first, then remaining syllabus"). Mech proved it: 6/6 parts were assignment questions.
10. **Class slides can be wrong** (metals vs non-metals slide said metals form anions). Correct visibly.
11. **Self-drawn TikZ diagrams need visual QA:** overlapping labels, a milling cutter on the wrong axis, a taper sketch missing the swivelled compound rest, drilling sketches with no tools. Check every figure as an examiner would.
12. **Deliver before polishing.** One build hit the tool-call limit before the file reached the outputs folder.
13. **This term's teacher signals beat last year's paper.** Mech: the current assignment predicted 6/6; topics promoted on last year's evidence alone (drilling, milling) scored 0. Rank sources: assignment/teacher instruction > last year's paper > QB > tutorials/labs > model papers.
14. **Drill every question type, not one example.** C "find the error" was a 1-mark sub-item in CIE-1 2025 and a 5-mark, 5-snippet part in 2026 (invalid identifier `2num`; commas instead of semicolons in `for`; missing operand in `a > 5 && < b`; `&a` passed to `%d`; `break 2;`). The book had 24 output drills but 1 error example. Now: 8–15 drills per type (`c-error-drills.md`).
15. **A 100% repeater can still skip.** "Structure of a C program" was in 3/3 past papers and did not come. Stars order study; they are not a forecast.
16. **Write a difference table for every concept pair.** "Differentiate" came in C (compiler/interpreter + HLL/MLL; while/do-while) and mech (ferrous/non-ferrous). HLL vs MLL existed only as prose.
17. **Expect compound parts.** One 5-marker joined two topics three times (data types + storage classes; compiler/interpreter + HLL/MLL; define lathe + working principle). Keep answers modular and half-mark sized.
18. **Lab programs return with new numbers**, like tutorial numericals: the electricity-bill slabs went from 100/100/200 to 200/200/400. Write them with named constants and show where the numbers plug in.
19. **gcc is not the examiner.** gcc 13 accepts `$num1` silently even with `-std=c11 -pedantic` (needs `-fno-dollars-in-identifiers`); the exam answer is "invalid". `printf("%d", &a)` and `while (k <= 3);` compile. Answer by the textbook rule.
20. **Answer book, not reference notes.** The student rejected a reference-style C sheet ("to score full marks, not to gain knowledge") and later the "see A4"-style cross-references in the ESC133 bank. Each block: exam-wording question + marks, then the answer as written, self-contained.
21. **Assignment questions without class notes are the weak spot.** The mech thermal plant answer came from a standard textbook (not in the notes) and was asked as an 8-marker. Ask for the textbook page early.
22. **Humanities notes can mis-state the portion and lack application practice** (soft skills: last year asked past the notes' "syllabus ends" line, and framed questions for teachers/administrators, not students).
