## Problem wording conventions

- For both golden skeletons and golden solutions, use LeetCode's original
  problem wording; do not paraphrase the statement, explanations, or hints.
- When the full original text cannot be reproduced from an external source,
  ask the user to provide it and preserve that supplied wording exactly.
  Keep the official URL available; do not silently substitute a summary.
- Do not add a `Problem statement (paraphrased):` label, custom-judge
  sections, or `TODO: Implement the solution` comments.

## Golden Python LeetCode skeleton

When the user requests a "golden Python LeetCode skeleton":

- Create `{problem-number}-{LeetCode-title-with-hyphens}/main.py`.
  Reuse an existing problem directory when available. Preserve existing
  solutions and user edits; do not replace them with a blank skeleton.
- Do not create `settings.json`.
- Follow the layout and standard-library import block used in the
  repository's existing Python skeletons.
- Start with `#!/usr/bin/env python3` and a module docstring containing:
  - Author: CBOMBS
  - The current creation date
  - Problem number, official title, and LeetCode URL
  - Complete problem statement, official examples with explanations,
    constraints, and any official follow-ups
  - A `Hints` section when LeetCode provides official hints, with each
    hint labeled `Hint 1`, `Hint 2`, etc., in the original order and in
    sentence/paragraph form
  - `Usage: python3 ./main.py`
- Use the supplied problem statement or verify the official LeetCode
  source, including its hints. Include all available official hints in
  the top module docstring, preserving their meaning and paragraph form.
  Omit the Hints section when none are provided. Do not invent missing
  problem details, follow-ups, or hints.
- Preserve LeetCode's Python 3 solution class and exact method signature,
  including parameter names and type annotations.
- Leave the algorithm unimplemented. Use a minimal
  placeholder return compatible with the expected return type so the
  local examples can run. Do not add TODO comments.
  Include the official LeetCode hints as required
  above, but do not add extra solution hints unless requested.
- Add `Solution.__repr__` returning `"Solution"` to reduce debugger noise.
- Include any required LeetCode structures, such as `ListNode` or
  `TreeNode`, with compatible constructors and compact, nonrecursive
  `__repr__` methods.
- Add simple local helpers only as needed to construct and display
  example data structures. Keep helper comments brief.
- Under `if __name__ == "__main__":`, prepare every official example
  with explicit, separately named input, expected, and result variables
  so each example is easy to inspect in the debugger.
- Give each example independent mutable inputs.
- Print clearly labeled actual and expected results for every example.
  For in-place problems, display the relevant mutated state as well.
- Verify Python syntax and run `main.py` from the problem directory.
  Placeholder results may differ from expected results; verification
  confirms that the skeleton runs, not that the problem is solved.
- Do not add acceptance claims, test-pass counts, or solution complexity
  analysis to an unimplemented skeleton.

## Golden Python LeetCode Solution

When asked for a **“golden Python LeetCode solution”**:

- Read the problem’s existing `main.py` first
- Create `optimal.py` in the same directory
- Do not modify `main.py` unless explicitly requested
- Use the optimal standard algorithm
- Keep LeetCode’s `Solution` class and required method signature
- Include only necessary imports
- Match nearby golden solutions’ formatting
- Verify examples and edge cases; use broader generated tests when practical
- Keep chat responses **mega concise**

### File Format

- Begin with `#!/usr/bin/env python3`
- Include a concise top documentation block with:
  - `Author: ChatGPT + CBOMBS`
  - Current date
  - LeetCode number, title, and problem URL
  - Original problem wording, examples, and constraints, following the
    problem wording conventions above
  - Quick time and space complexity chart
- Define complexity variables and distinguish auxiliary space from output storage
- Exclude local testing helpers from the algorithm’s complexity
- Use no sentence-ending periods in comments or docstrings below the top block
- Python member access, URLs, decimal numbers, and other required punctuation remain allowed

### Function Documentation

Use concise docstrings for solution and helper functions:

```python
"""
Brief function description

@param name: Parameter description
@result: Return value description
"""
```

- Document each applicable parameter
- Simple `__repr__` methods may use one-line docstrings
- Add helpful inline comments explaining **why**, especially pointer changes and tricky conditions
- Avoid repetitive comments and excessive terminology

### Local Tests

- Include approximately **3 useful cases** directly under `if __name__ == "__main__":`
- Prefer problem examples plus a meaningful edge or branching case
- Show expected outputs
- Usually leave one case active and the others commented out
- Include linked-list construction and display helpers when needed

### Complexity-Only Requests

- Analyze the user’s actual implementation
- For unfinished code, clearly label complexity as describing the intended approach
- Preserve implementation logic
- Remove “intended” or “unfinished” wording once the completed implementation is verified

### Algorithm Diagrams

When requested:

- Match the finalized #24 **soft lavender style**, with off-white/lilac inner panels and gentle contrast
- Use four explanatory panels when suitable
- Match the requested script’s exact algorithm and variable names
- Keep each variable’s color consistent across code, labels, and arrows
- Verify pointer positions, link directions, intermediate states, and final results
- Save the image in the problem directory with a descriptive filename
