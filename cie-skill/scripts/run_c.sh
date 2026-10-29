#!/bin/bash
# Usage: run_c.sh prog.c [input.txt]
# Compiles with strict flags (standard C, no gcc '$' extension), prints every diagnostic,
# then runs with a 2-second timeout (exit 124 = infinite loop) and optional stdin file.
set -u
SRC="$1"; IN="${2:-/dev/null}"; BIN="/tmp/run_c_$$"
echo "== diagnostics (gcc -Wall -Wextra -std=c11 -pedantic -fno-dollars-in-identifiers)"
gcc -Wall -Wextra -std=c11 -pedantic -fno-dollars-in-identifiers "$SRC" -o "$BIN" -lm 2>&1 | grep -E "error|warning" || echo "(none)"
if [ -x "$BIN" ]; then
  echo "== output"
  timeout 2 "$BIN" < "$IN"; rc=$?
  echo; echo "== exit code: $rc$( [ $rc -eq 124 ] && echo ' (timed out: infinite loop?)' )$( [ $rc -eq 136 ] && echo ' (SIGFPE: division by zero?)' )"
  rm -f "$BIN"
else
  echo "== did not compile"
fi
echo "Reminder: gcc accepting code does not make it correct for the exam; answer by the C standard/textbook rule."
