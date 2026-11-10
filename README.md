# AI Code Quality Evaluator

A beginner-friendly Python **static analysis** project that checks Python files without executing them. Built as a learning portfolio project for reviewing and testing code, including AI-generated code.

## Features
- Reports Python syntax errors
- Flags bare `except:` clauses
- Flags direct calls to `eval()` and `exec()` for manual review
- Flags lines longer than 88 characters
- Includes six unit tests and GitHub Actions CI

## Run
Requires Python 3.10+; no third-party dependencies.

```bash
python evaluator.py examples/sample.py
```

## Test
```bash
python -m unittest discover -v
```

On GitHub, check the **Actions** tab for the latest test result.

## AI coding tools and review process
See [AI_USAGE_LOG.md](AI_USAGE_LOG.md) for a template. Complete it with your own actual prompts, code review, and test results before using this repository in an application.

## Limitations
This is a rule-based code checker, **not an AI model**, security audit, or correctness proof. It only detects a few patterns and can miss bugs. `eval` and `exec` checks only cover direct calls by those names.
