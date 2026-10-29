# C "find the errors" drill set (verified)

CIE-1 2026 had a 5-mark part with 5 snippets; CIE-1 2025 had it as a 1-mark item. Use these as the starting drill set and add more from the student's notes. Every item was compiled with `gcc 13 -Wall -Wextra -std=c11 -pedantic` and run; "gcc says" is what the compiler actually reported. Answer by the C rule, not by whether gcc compiles it.

Answer pattern for each: **Error** (quote the line) → **Why** (rule; compile-time / logical / runtime) → **Corrected code** → output.

| # | Snippet | Error and rule | Kind | gcc says | Correction |
|---|---|---|---|---|---|
| 1 | `int 2num = 50;` | Identifier cannot start with a digit | Compile | error: invalid suffix "num" on integer constant | `int num2 = 50;` |
| 2 | `for (i = 1, i <= 5, i++)` | `for` needs two semicolons, not commas | Compile | error: expected ';' before ')' | `for (i = 1; i <= 5; i++)` |
| 3 | `if (a > 5 && < b)` | `<` needs a left operand | Compile | error: expected expression before '<' | `if (a > 5 && a < b)` |
| 4 | `printf("Value = %d", &a);` | `%d` needs an int; `&a` is an address | Logical (prints an address) | warning only (-Wformat) | `printf("Value = %d", a);` |
| 5 | `if (i == 3) break 2;` | C's `break` takes no number; it exits only the innermost loop | Compile | error: expected ';' before numeric constant | `break;` (use a flag or `goto` to leave two loops) |
| 6 | `scanf("%d", n);` | `scanf` needs the address | Runtime crash / garbage | warning only | `scanf("%d", &n);` |
| 7 | `if (x = 10)` | `=` assigns; always true | Logical | warning only (-Wparentheses) | `if (x == 10)` |
| 8 | `int a = 5 printf(...)` | Missing semicolon | Compile | error: expected ',' or ';' before 'printf' | `int a = 5;` |
| 9 | `float f = 3.5; printf("%d", f);` | Wrong format specifier for float | Logical (garbage) | warning only | `printf("%f", f);` |
| 10 | `while (k <= 3); { ... k++; }` | Stray `;` makes an empty loop body; `k` never changes | Runtime (infinite loop) | **no warning** | `while (k <= 3) { ... }` |
| 11 | `case m:` (m a variable) | Case labels must be integer constants | Compile | error: case label does not reduce to an integer constant | `case 2:` |
| 12 | `char c = "A";` | `"A"` is a string; a char uses single quotes | Compile warning / wrong value | warning (-Wint-conversion) | `char c = 'A';` |
| 13 | `if (x > 5) continue;` outside a loop | `continue` is only valid inside a loop | Compile | error: continue statement not within a loop | remove it, or put it in a loop |
| 14 | `int int = 5;` | A keyword cannot be an identifier | Compile | error: two or more data types in declaration specifiers | `int num = 5;` |
| 15 | `printf("%d", a / b);` with b = 0 | Integer division by zero | Runtime | no warning; "Floating point exception" at run time | check `if (b != 0)` first |
| 16 | `int x; printf("%d", x);` | Uninitialised local (auto) variable holds garbage | Logical | warning (-Wuninitialized) | `int x = 0;` |
| 17 | `printf("Hello World);` | Missing closing `"` | Compile | error: missing terminating " character | `printf("Hello World");` |
| 18 | `switch (a) { case 1: ...; case 3: ...; case 4: ...; }` | Missing `break` → fall-through (prints "threefour" for a = 3) | Logical | warning (-Wimplicit-fallthrough) | add `break;` after each case |

Identifier trap: `$num1` is **invalid** in standard C (allowed characters are letters, digits, underscore), but gcc accepts it silently as an extension; compile with `-fno-dollars-in-identifiers` to see the standard error ("stray '$' in program"). `+add` is invalid (special character); `num2` and `a_2` are valid.
