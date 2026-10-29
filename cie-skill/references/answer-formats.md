# Answer formats that score full marks

Every block in the book: **question in exam wording + marks + "asked in" line → "Answer:" → the answer as it should be written.** Self-contained: repeat a figure or table rather than writing "see A4".

## Theory / explain / describe (5–8 marks)
1. Definition or principle in one or two lines.
2. **Diagram first** (the class's figure if one exists), fully labelled.
3. Components / parts, numbered, one line each.
4. Working, as numbered steps in flow order (source → process → output).
5. Advantages and disadvantages (3 each) when the topic is a machine, plant or method. If the question says "any 2", write exactly 2 of each, clearly numbered.

## Differentiate / compare / distinguish
A table with a **Basis** column and 5–6 rows (definition, working, speed, memory/files, errors, examples), then one example of each side. If one part asks for two pairs ("compiler vs interpreter **and** HLL vs machine language"), write two short tables of 4–5 rows each, not one long one. Prepare a table for every concept pair in the portion, even ones the bank only asks to "explain".

## Compound parts (two topics in one 5-marker)
Two headed mini-answers, each about half the marks' worth: e.g. "Basic data types" (table) + "Storage classes" (table + one program with output). Keep bank answers modular so they can be joined like this.

## Derivations
State assumptions, draw the figure, number each equation, show every substitution, box the result, add one line on its significance (e.g. B12 = B21; A/B ∝ ν³).

## Numericals and parameterised templates
Given → formula → substitution with units → boxed answer with units. Use the constants printed on the paper. The method line earns marks even if arithmetic slips. For tutorial/lab templates, show the general method once and mark which numbers the examiner is likely to change.

## Maths "show that / prove"
Write the theorem used (e.g. Euler: x u_x + y u_y = n u), show partial derivatives separately, substitute on a separate line, finish with "Hence proved". For maxima/minima, tabulate stationary points with r, s, t, rt − s² and nature.

## C programming
- **Programs:** #include, int main(void), declarations, prompt + scanf (with &), logic, labelled printf, return 0, one or two comments, a sample run showing typed input. If the question names a construct (switch, symbolic constant, pretest loop, getchar/putchar), use exactly that construct. For slab/rate problems (electricity bill, fares), put the limits and rates in `#define` constants.
- **Write the output / evaluate step by step:** one line naming the precedence and associativity used (`* / %` left to right, then `+ -`, then relational, then `&&`, then `||`), then a step table, then the boxed result. Know integer division, pre/post increment, short-circuit, switch fall-through, empty-loop semicolons, char arithmetic and bitwise rules.
- **Find the errors and justify corrections:** for each snippet: *Error* (quote the line) → *Why* (the rule broken; say compile-time, logical or runtime) → *Corrected code* → output after correction. Drill set: `c-error-drills.md`.
- **Classify valid/invalid identifiers:** a table: identifier | valid/invalid | reason (rule number). Answer by the C standard: `$` is invalid even though gcc accepts it.
- **Undefined behaviour:** write the expected left-to-right answer plus a one-line UB note.

## Language papers (e.g. Kannada Kali, written in English letters)
- Self-introduction / language introduction: memorised template of exactly the asked number of lines, numbered so the examiner can count them.
- Translate-and-answer: write the English translation of the question first, then a full-sentence answer in Kannada (not a one-word answer).
- Word meanings: word → English meaning → one simple sentence using it.
- Jumbled sentences: rewrite in subject–object–verb order; verb at the end.

## Soft skills (L3 application)
Definition of the concept in one line → apply each named element of the concept to the given context (the context in the question, not a generic student example) in numbered points → conclusion. Use the course's terms by name (logos/ethos/pathos, SWOC, Eisenhower quadrants).

## Order of study box
Fit it to the hours left: compulsory/always-asked types and their drills first (e.g. C output and error questions), then ★★★ assignment items, then ★★★ past-paper items, then ★★ (programs/numerical types, difference tables), then uncertain-portion items.
