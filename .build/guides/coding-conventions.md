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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

# Coding conventions

## Python
- Lint and format with **Ruff** (`pyproject.toml`): line-length 110, **tabs** for indentation, double quotes, and docstring code formatting.
- Lint rules: `F, E, W, I, UP, B, RUF`, with Frappe-friendly ignores (E501, F401, F403/F405, W191, B904, etc.).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each group with a blank line, as in `import frappe` / `import erpnext` / `from healthcare...`.
- Use the `frappe.types.DF` typing module for DocType type hints.
- Naming: DocType folders and modules are `snake_case` versions of the DocType name (`patient_appointment/patient_appointment.py`). Controller classes are PascalCase (`class PatientAppointment(Document)`). Custom exceptions end in `Error`.
- Wrap every user-facing string in `_()`, using `.format()` placeholders like `{0}`.
- Prefer `frappe.qb` or `frappe.get_all` over raw SQL. Semgrep with Frappe's rules runs in CI.
- Expose server methods to the client only through `@frappe.whitelist()`.
- Many legacy files are listed in the `.pre-commit-config.yaml` global `exclude`, so they are not reformatted. Do not mass-reformat them; keep diffs minimal.

## JavaScript (Desk)
- **Prettier**: tabs (`useTabs: true`, tabWidth 4), printWidth 88, `arrowParens: avoid`.
- **ESLint** flat config (`eslint:recommended`) with the globals `frappe`, `erpnext`, `$`, `jQuery`, `__`, and so on.
- Form scripts use `frappe.ui.form.on('<DocType>', {...})`. Wrap all labels in `__()`.

## Vue (Patient Portal)
- Use `<script setup>`-style components in `patient_portal/src/components/PascalCase.vue`, with frappe-ui components and `createResource` for data, and Tailwind utility classes. `patient_portal/` is excluded from prettier.

## Commits
- Use Conventional Commits, enforced by commitlint. Allowed types are `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case, and the subject must not be empty.
