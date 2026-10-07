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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .git-blame-ignore-revs
---

# Coding conventions

## Python (ruff, `pyproject.toml`)
- Indent with **tabs**, use **double quotes**, and keep lines to **110** characters (E501 is ignored). Target py310.
- Lint rule sets: F, E, W, I, UP, B, RUF, with an ignore list (for example F401, E402, B904).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate the groups with blank lines.
- Use `frappe.types.DF` for typing.
- Doctype controllers are `class <DocTypeName>(Document)` in `<snake_name>.py`. Use the lifecycle methods `validate`, `on_submit`, `on_cancel` and so on, and split them into small `validate_*` / `set_*` helpers.
- Module-level functions called from JS are decorated `@frappe.whitelist()`.
- Wrap user-facing strings in `_()`, with `.format()` placeholders `{0}`.
- Custom errors subclass `frappe.ValidationError` (for example `OverlapError`, `MaximumCapacityError`).
- Each file starts with a copyright/license header comment.

## JavaScript
- Prettier: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. It excludes `patient_portal/` and a few large doctype JS files.
- ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, ...).
- Desk scripts use `frappe.ui.form.on('<DocType>', {...})`. Wrap strings in `__()`.

## Vue (patient_portal)
- SFCs use PascalCase names (`BookAppointmentModel.vue`). Import frappe-ui components (`Card`, `Button`, `ErrorMessage`) and use the `@` alias for `src`.

## Legacy-exclusion caveat
`.pre-commit-config.yaml` excludes about 620 existing healthcare paths from the hooks, so many old files do not follow the style. When you edit such a file, match the style in that file and don't reformat it wholesale; whole-file rewrites make upstream (marley) syncs harder. Formatting-only commits are listed in `.git-blame-ignore-revs`.
