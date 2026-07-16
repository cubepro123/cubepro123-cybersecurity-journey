# 🐍 Python Security Basics — Portfolio

Hi — I refactored this repo to make it easier for potential employers to review your work and to show clear, testable examples of the skills you described.

Summary of what's in this repo now:

- A concise overview of your goals and top projects.
- How to run the example scripts and tests.
- A short highlight of the skills employers look for.

---

## Highlights

- Author: cubepro123 (Bol)
- Primary focus: input validation, safe loops, basic automation and scripting
- Quick example: weapon_armory_checker.py — now refactored into functions, supports CLI arguments, and has unit tests and CI.

## Run the example

Create a virtual environment, install test deps, and run the example interactively:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 weapon_armory_checker.py
```

Or run non-interactively:

```bash
python3 weapon_armory_checker.py --choice katana
```

## Test / CI

Run tests locally:

```bash
pytest -q
```

A GitHub Actions workflow runs the test suite on pushes and pull requests.

## What employers will see

- Clean, documented scripts with clear entry points
- Unit tests that prove basic correctness
- CI that shows you follow best practices (tests on push)

## Next improvements you might want

- Add a few more small projects in a projects/ directory demonstrating file parsing, simple network scanning (safe, local-only), or secure config handling.
- Add a short demo video or GIF showing a script run (optional) and a short CV or contact section.

---

If you want I can also split out a projects/ directory and convert other examples in progress-log.md into testable modules.
