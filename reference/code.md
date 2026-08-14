# The Code Slop Reference

Code slop is the fingerprint of AI-generated code. It is distinct from "bad code": it is code that is structurally over-engineered, superficially documented, and loaded with padding. Tools in the ecosystem (see `ecosystem.md`) detect it automatically.

## The tells

### 1. Empty functions and fake implementations

Functions that exist, are documented, and do nothing or throw. AI generates these to satisfy a requested API shape.

```python
def process_payment(transaction):
    """Process a payment transaction and update the ledger."""
    # TODO: implement
    pass
```

Detection: functions whose bodies are `pass`, `throw`, `return None`, or a comment.

### 2. Inflated comments

Comments that restate what the code does instead of why. AI pads code with narration because it is trained to be helpful.

```python
# Increment the counter by 1
counter += 1
```

Detection: comment-to-code ratio far above the codebase norm; comments that paraphrase the next line.

### 3. Fake documentation

Docstrings that describe parameters never used and claims the code does not make good on. AI documentation is confident and wrong.

Detection: docstrings longer than the function body; documented parameters that do not appear in the signature.

### 4. Over-engineering

Abstraction layers, factory factories, and configuration systems for problems that need a function. AI generates architecture to look professional.

Detection: classes with a single method, interfaces with one implementation, generic wrappers around direct calls.

### 5. Swallowed errors

```python
try:
    result = api.call()
except Exception:
    pass
```

AI writes defensive error handling that hides failures. The comment "fail silently" is the tell.

Detection: empty `except` blocks, exceptions caught and logged with no action.

### 6. Unsafe casts and unguarded access

AI assumes types and shapes are valid because the training data does. Production data disagrees.

```python
value = data["user"]["name"].upper()
```

Detection: chained indexing without existence checks, casts without validation.

### 7. Dead code and unused imports

AI leaves the full scaffolding of every generation attempt: unused imports, unused variables, helper functions nothing calls.

Detection: linters flag these by default; AI output consistently fails `ruff`, `eslint`, `tsc --noUnusedLocals`.

### 8. Duplication as safety

AI reimplements the same logic in every file instead of importing, because importing requires understanding the codebase. Copy-paste is the low-risk token path.

Detection: identical blocks across files that should share one function.

### 9. The "comprehensive" solution

AI solves the requested problem plus four adjacent problems nobody asked for, with a config file exposing all six. Scope is the padding.

Detection: PR size unrelated to the ticket; flags and options nothing sets.

### 10. Hallucinated APIs and dependencies

AI calls functions that do not exist, imports packages it invented, and references library features the installed version lacks.

Detection: builds fail with `ModuleNotFoundError` for packages never installed, or `AttributeError` on third-party objects.

## The rule of thumb

AI code is written to be *read by a reviewer*, not to *run in production*. The single most effective review pass: run the code. Slop survives reading and dies on execution.

## The de-slop pass

1. Delete every comment that restates code. Keep only "why" comments.
2. Delete every empty or throw-only function.
3. Run the linter with all warnings as errors. Fix everything it flags.
4. Remove unused imports and variables.
5. Collapse duplication into one shared function.
6. Prove every error path does something observable.
7. Shrink the PR to the ticket.
