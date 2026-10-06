---
title: Coding Conventions
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
---

**Python (ruff, `pyproject.toml`)**
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored), target py310.
- Lint rule sets are F, E, W, I, UP, B and RUF, with Frappe-friendly ignores (F401, E402, B904, and others).
- Import order: stdlib, third-party, `frappe`, `erpnext`, `healthcare`, local. Each group is its own isort section.
- Type hints for DocType fields come from `frappe.types.DF`.
- Modules, doctype folders and functions use `snake_case`. Controller classes use `PascalCase` matching the DocType name (`class PatientAppointment(Document)`).
- Wrap every user-facing string in `_()` (`from frappe import _`). Use `.format()` placeholders like `{0}`.
- Client-callable server functions use `@frappe.whitelist()`.
- Most legacy files are on the pre-commit `exclude` list. New files are not, so they must pass the linters.

**JavaScript**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, …).
- Desk forms use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js`. List and tree views go in `<doctype>_list.js` / `_tree.js`.
- Wrap UI strings in `__()`.
- The patient portal (Vue SFC with `<script setup>`, `@/` alias to `src`) is excluded from prettier.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test. Types are lower-case. Scopes are common, e.g. `fix(tests):` and `docs(wiki):`.
