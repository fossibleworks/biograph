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
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/fee_validity/fee_validity.js
---

# Coding conventions

## Python (ruff)
- Indent with **tabs** and use **double quotes**. Line length is 110, though E501 is ignored. Run `ruff format` with `docstring-code-format`.
- Enabled lint sets: `F, E, W, I, UP, B, RUF`. Ignored rules include F401 (unused imports), E402 and B904. Even so, recent commits clean up unused imports.
- Import sections, in order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Put a blank line between groups, for example `import frappe` … `from erpnext...` … `from healthcare...`.
- Type hints for doctype fields use `frappe.types.DF`.
- Naming:
  - DocType folders and modules are snake_case (`patient_appointment/patient_appointment.py`).
  - Controller classes are PascalCase and subclass `Document` (`class PatientAppointment(Document)`).
  - Custom exceptions end in `Error` and subclass `frappe.ValidationError`.
- Every user-facing string is wrapped in `_()` (`from frappe import _`).
- Queries use `frappe.qb` or `frappe.db.get_all/get_value/exists`. Raw `frappe.db.sql` appears mainly in tests and legacy code.
- Frappe Semgrep rules run in CI. Suppress one only with a justified `# nosemgrep`.
- New files carry the standard header: `# Copyright (c) <year>, ... and contributors` / `# See license.txt`.

## JavaScript
- Prettier settings: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Form scripts use `frappe.ui.form.on("<DocType Label>", {...})`. User strings are wrapped in `__()`.
- `patient_portal/` is excluded from Prettier. Match the style of the surrounding file there: Vue SFCs, 2-space indent and single quotes in the config files.

## Commits
- Commits follow conventional commits, checked by commitlint. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case. Scopes are used, for example `fix(tests):` and `docs(wiki):`.
