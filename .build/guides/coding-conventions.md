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
  - healthcare/healthcare/api/patient_portal.py
---

## Python
- Formatted by **ruff-format** with **tabs** for indentation and **double quotes**. Line length is 110, but E501 is ignored.
- Lint rules `F,E,W,I,UP,B,RUF`, with many ignores (for example F401 unused imports, B904, E402).
- **Import order** is custom: future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Each group is separated by a blank line.
- Use absolute imports such as `from healthcare.healthcare.doctype.x.x import X`.
- **Legacy files:** a large explicit list of older files is excluded from pre-commit in `.pre-commit-config.yaml`. Those files may still use 4-space indentation. Do not mass-reformat them; match the style of the file you are editing.
- **Frappe idioms:**
  - DocType controllers are `class PatientAppointment(Document)` with `validate`, `on_submit`, `on_cancel` hooks.
  - Module-level functions are exposed with `@frappe.whitelist()`.
  - Wrap user-facing strings in `_()` from `frappe`.
  - Use `frappe.qb` / `frappe.db` for queries.
  - Type hints use `frappe.types.DF` (configured in `typing-modules`).
- File names are snake_case and match the DocType (`patient_encounter/patient_encounter.py`). Class names are PascalCase.

## JavaScript
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint uses `eslint:recommended` with the `frappe`, `erpnext`, `$`, `jQuery`, `Vue` globals.
- Prettier skips `patient_portal/` and a few form scripts (`patient.js`, `medication_request.js`, `service_request.js`).
- Desk form scripts follow the `frappe.ui.form.on("DocType", {...})` pattern.

## Vue (patient_portal)
- Use the SFC pattern with frappe-ui components (`Button`, `toast`, …).
- PascalCase component file names, for example `BookAppointmentModel.vue`.
- Use the `@` alias for `src`.

## Commits
Use conventional commits, enforced by commitlint. The allowed types are `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower-case, with an optional scope (for example `fix(tests): ...`, `docs(wiki): ...`). Upstream-sync commits append a context suffix such as `(upstream sync B2)`.
