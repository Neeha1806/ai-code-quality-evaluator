"""Simple static checks for Python source code (does not execute it)."""
import ast
from pathlib import Path
import sys


def evaluate(source: str) -> list[str]:
    """Return a list of potential problems in Python source."""
    findings = []
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return [f"Syntax error on line {error.lineno}: {error.msg}"]

    for number, line in enumerate(source.splitlines(), start=1):
        if len(line) > 88:
            findings.append(f"Line {number}: Line exceeds 88 characters ({len(line)}).")

    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            findings.append(f"Line {node.lineno}: Avoid bare except clauses.")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
            findings.append(f"Line {node.lineno}: Review use of {node.func.id}(); it can be unsafe with untrusted input.")
    if not findings:
        findings.append("No issues found by these basic checks (not a guarantee of correctness).")
    return findings


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python evaluator.py path/to/file.py")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Could not read file: {error}")
        raise SystemExit(1)
    for finding in evaluate(source):
        print(f"- {finding}")


if __name__ == "__main__":
    main()
