---
title: Coding conventions
category: coding-conventions
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - pyproject.toml
  - .pre-commit-config.yaml
  - .prettierrc.yaml
  - eslint.config.mjs
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - .git-blame-ignore-revs
  - patient_portal/.prettierrc.json
---

**Python** (ruff config in `pyproject.toml`, pinned ruff v0.15.18 via pre-commit)
- **Tabs** for indentation, **double quotes**, line length 110. `E501` is ignored, so long lines are tolerated.
- Lint rules: `F, E, W, I, UP, B, RUF`, with Frappe-friendly ignores (F401, F403/F405, E402, B904, W191, etc.).
- **Import order** (isort sections): future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Separate each group with a blank line, as in the test modules.
- `typing-modules = ["frappe.types.DF"]`, so doctype controllers may use auto-generated `DF` type hints.
- **Naming:** modules and folders are `snake_case` matching the DocType name (`patient_appointment/patient_appointment.py`). Controller classes are PascalCase DocType names (`class PatientAppointment(Document)`). Custom exceptions use PascalCase with an `Error` suffix. Whitelisted functions are `snake_case`.
- Wrap user-facing strings in `_()` (`from frappe import _`).
- Many legacy files are listed in the `.pre-commit-config.yaml` global exclude. They are **not** auto-formatted, so do not reformat them wholesale. Touch only the lines you change, and don't add new ruff findings. Mass-format commits go in `.git-blame-ignore-revs`.

**JavaScript** (Desk scripts, `.prettierrc.yaml` and `eslint.config.mjs`)
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: "avoid"`.
- ESLint `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `jQuery`, ...).
- Wrap user-facing strings in `__()`.
- `patient_portal/` is excluded from root Prettier and has its own `patient_portal/.prettierrc.json`. Vue SFCs use `<template>` plus Tailwind utility classes.

**Commits:** Conventional Commits enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, always lower-case. A scope is optional, for example `fix(tests):` or `docs(wiki):`.
