# Code Analysis Rules - AST ONLY

## BANNED Tools for Python Code Analysis

The following are COMPLETELY BANNED for parsing/analyzing Python code:

- `grep` - BANNED
- `sed` - BANNED
- `awk` - BANNED
- Regular expressions for extracting code structure - BANNED

## Required Approach: AST

Always use Python's `ast` module for code analysis:

```python
import ast
from pathlib import Path

def find_functions(filepath: Path) -> list[str]:
    """Find all function names in a Python file."""
    source = filepath.read_text(encoding="utf-8")
    tree = ast.parse(source)

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]

def find_imports(filepath: Path) -> list[str]:
    """Find all imports in a Python file."""
    source = filepath.read_text(encoding="utf-8")
    tree = ast.parse(source)

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return imports

def find_classes(filepath: Path) -> list[str]:
    """Find all class names in a Python file."""
    source = filepath.read_text(encoding="utf-8")
    tree = ast.parse(source)

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
    ]
```

## Why AST?

1. **Correctness**: AST understands Python syntax properly
2. **Robustness**: Handles edge cases (strings, comments, multiline)
3. **Maintainability**: Standard library, no external dependencies
4. **Performance**: Optimized C implementation

## Exceptions

Using grep/sed/awk is allowed for:
- Log file analysis
- Non-Python text files (YAML, JSON, Markdown, etc.)

**NOT allowed even when "simpler":**
- `"import_name" in source` — use `ast.Import`/`ast.ImportFrom` nodes
- `"class_name" in source` — use `ast.ClassDef` nodes
- `"function_name" in source` — use `ast.FunctionDef` nodes
- `source.count("keyword")` — use `ast.Constant` string value checks
- Any `str.find()`, `str.count()`, `re.search()` on Python source code

## Documented Failures

### 2026-02-22: test_demo_script.py string-based analysis

`test_demo_script.py` used `"argparse" in source` and `"VoiceConfig" in source`
to check for imports — string-based code analysis disguised as "simple checks."
This violated the AST-only rule. Rewritten to use `ast.walk()` with proper
`ast.Import`, `ast.ImportFrom`, and `ast.Constant` node inspection.

**Lesson:** "It's just a test" and "it's simpler" are NOT valid exceptions.
The AST-only rule applies to ALL Python source analysis in ALL contexts.
