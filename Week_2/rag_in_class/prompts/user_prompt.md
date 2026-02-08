You are a software engineer refactoring Python code.


## Inputs
1) Existing implementation file (content inserted below)
2) Pytest file(s) for this task (content inserted below)


## Goal
Refactor the implementation to improve readability and maintainability while preserving behavior EXACTLY as validated by the provided tests.


## Hard constraints
- Do NOT change the function name(s) referenced by the tests.
- Do NOT rename public identifiers for style (including capitalization or underscore changes).
- Do NOT change function signatures (parameter count, order, defaults must remain identical).
- Do NOT change return types or return conventions (e.g., returning None vs False, int vs float, list vs tuple).
- Do NOT change printed output behavior (if any).
- Do NOT add new required dependencies.
- Do NOT change algorithmic behavior, edge-case behavior, or numeric behavior.
- Do NOT change comparison semantics (>, >=, ==, is).
- Do NOT change numeric semantics (// vs /, rounding behavior, float precision).
- Do NOT change the meaning of any parameter (including whether an index is 0-based vs 1-based; whether k means k-th smallest vs k-th largest; and whether bounds are inclusive vs exclusive).
- Do NOT change ordering semantics (ascending vs descending; tie-handling; stable vs unstable behavior).
- Do NOT change mathematical conventions (e.g., quadrant behavior; atan vs atan2; angle range; sign conventions; domain/range assumptions).
- Do NOT algebraically rewrite expressions or replace call forms with "equivalent" alternatives if operand order, coercion, or argument interpretation could change.
- Do NOT move or normalize return/break/continue placement; preserve early-exit behavior exactly.
- If the original behavior seems “wrong”, surprising, or non-idiomatic, preserve it anyway unless the tests clearly require a change.
- Treat the original implementation as ground truth: do NOT fix apparent bugs, typos, or quirks unless tests explicitly demand it.
- If the original code relies on specific quirks (case-sensitivity, sentinel values, None handling), preserve them EXACTLY.


## Minimal differential mode
- Make the smallest possible change set needed to improve readability.
- Do NOT rewrite, optimize, or restructure the algorithm.
- Do NOT “simplify” logic, even if it appears redundant.
- Preserve the exact control-flow shape:
  - same loops
  - same condition boundaries
  - same return points
  - same early-exit placement inside loops/branches
- Prefer:
  - whitespace/formatting
  - clearer local variable names
  - comments or docstrings
- Avoid:
  - new helper functions
  - new comprehensions
  - changing loop ranges
  - changing condition structure
- If a test expects None in any branch, you MUST return None (never substitute False, 0, or empty values).


## Refactoring Rules 
- Rename local variables only (NOT public functions/classes used by tests).
- Add comments and/or docstrings.
- Reformat code for clarity.
- Extract very small internal helpers ONLY if:
  - they are not imported by tests
  - they do not change control flow or behavior


## Self checks before finals
Before producing the final answer, mentally simulate the tests:
- Identify exactly which functions/classes the tests call and confirm they still exist with the same names.
- Verify edge cases implied by tests (empty inputs, None, 0/1, negative values).
- Verify numeric operations exactly match the original behavior.
- Verify return values for “no result” cases (None vs False vs 0).
- Verify parameter meaning is unchanged (0-based vs 1-based, inclusive/exclusive bounds, k-th smallest/largest, etc.).
- Verify ordering/tie-handling is unchanged.
- Verify math conventions are unchanged (atan vs atan2, quadrant/range/sign conventions, etc.).
- Verify expression and call argument order remain behaviorally identical (especially around coercion-sensitive operations).
- Verify early returns/break/continue trigger on the same iterations/branches as before.
- Pick 2–3 concrete assertions from the provided tests and sanity-check that the refactored logic would produce the same values.
- If unsure about any behavior, preserve the original logic rather than “improving” it.


## Output Format is strict
- Provide exactly ONE Python code block containing the full refactored implementation.
- After the code block, provide a checklist of 5–10 bullets.
- Do NOT include any additional text.


---


## Implementation file content
<<<IMPLEMENTATION>>>





