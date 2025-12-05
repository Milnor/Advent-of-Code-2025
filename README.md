# Advent-of-Code-2025

<img width="488" height="486" alt="Screenshot 2025-12-05 170801" src="https://github.com/user-attachments/assets/672289e9-e4b9-4b71-b586-3dbfaabe4aac" />

* Install and run

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

## Code Quality & Correctness Checks

```bash
pylint --rcfile=.pylintrc src
mypy --explicit-package-bases --check-untyped-defs .
python3 -m unittest test/test_challenges.py
```

## Credits

* README artwork by DALL·E
