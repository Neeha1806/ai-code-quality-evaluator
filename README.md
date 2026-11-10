# AI Code Quality Evaluator

A beginner-friendly Python project for reviewing Python source code using simple static checks. This project supports practicing code evaluation, testing, and AI-assisted development.

## Features
- Detects Python syntax errors
- Flags bare `except:` clauses
- Flags calls to `eval()` and `exec()` for manual review
- Does **not** execute the code being evaluated

This is a learning project, not a comprehensive security scanner or AI model.

## Run
Requires Python 3.10+; no third-party packages.

```bash
python evaluator.py examples/sample.py
```

## Test
```bash
python -m unittest -v
```

## AI-assisted development log
Document which AI coding tool you used, the prompts you tried, the suggestions you accepted or rejected, and how you verified results. Only claim work you actually performed.

## Limitations
The checks are intentionally basic. A clean report does not guarantee correct or secure code.
