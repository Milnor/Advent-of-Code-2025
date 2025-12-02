# Advent-of-Code-2025

* Install and run (assumes virtual environment in place)

```bash
pip install -e .        # editable install, uses source without rebuilding
pip install -e .[dev]   # dev dependencies
python3 -m advent25
```

## Code Quality Checks

```bash
pylint --rcfile=.pylintrc src
mypy --explicit-package-bases --check-untyped-defs .
```
