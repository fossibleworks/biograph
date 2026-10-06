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
  - .prettierrc.yaml
  - eslint.config.mjs
  - .pre-commit-config.yaml
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - commitlint.config.js
---

# Coding conventions

## Python (ruff, configured in `pyproject.toml`)
- **Tabs for indentation** and **double quotes** (`ruff format`: `indent-style = "tab"`, `quote-style = "double"`). Line length is 110, but E501 is ignored.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with a documented ignore list (for example, F401 unused imports and B904).
- **Import order** (isort sections): future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Put a blank line between groups, as in `test_fee_validity.py`.
- `typing-modules = ["frappe.types.DF"]`, so use `DF` type hints in doctype controllers.
- Naming: doctype folders and files are `snake_case` versions of the DocType name (`patient_appointment/patient_appointment.py`). Controller classes are `PascalCase` (`class PatientAppointment(Document)`). Module-level helpers are `snake_case`. API endpoints use `@frappe.whitelist()`.
- Wrap user-facing strings in `_()` (Python) or `__()` (JS) for translation.
- Use dotted paths in `hooks.py` (`healthcare.healthcare.doctype.<x>.<x>.<fn>`).
- Some files start with a copyright header (`# Copyright (c) 20xx, ... and Contributors` / `# See license.txt`).

## JavaScript
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. ESLint uses `eslint:recommended` (flat config) with Frappe globals (`frappe`, `erpnext`, `$`, `__`, ...).
- `patient_portal/` and a few large form scripts are excluded from Prettier.

## Legacy exclusions
`.pre-commit-config.yaml` has a large top-level `exclude` list of legacy files. Edits to those files are not auto-linted. Do not add new files to it. When you touch a listed file, avoid adding new ruff findings (the sync ledger tracks before/after counts).

## Commits
Use Conventional Commits (`feat|fix|chore|docs|refactor|perf|test|ci|build|style|revert`, lower-case type, non-empty subject). An optional scope is common: `fix(linters): ...`, `feat(appointment): ...`.
