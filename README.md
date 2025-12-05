# Advent-of-Code-2025

* Install and run (assumes virtual environment in place)

```bash
sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
```

```bash
pip install -e .[dev]   # -e = editable install, use source without rebuild
                        # [dev] install dev dependencies
python3 -m advent25
```

## Code Quality Checks

```bash
pylint --rcfile=.pylintrc src
mypy --explicit-package-bases --check-untyped-defs .
```
