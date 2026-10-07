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
  - .git-blame-ignore-revs
---

# Coding conventions

## Python
- **ruff** with line length 110 and target py310. Lint set: `F,E,W,I,UP,B,RUF`, with many legacy ignores (e.g. `F401`, `E501`, `B904`).
- **ruff-format** uses **tabs** for indentation and **double quotes**.
- Import order (isort sections): future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. A blank line separates each group.
- Use absolute imports: `from healthcare.healthcare.doctype.x.x import ...`.
- Imports from inside DocType folders are allowed.
- Each DocType controller is a `Document` subclass named in PascalCase after the DocType (e.g. `PatientAppointment`). Files and folders use snake_case.
- Wrap user-facing strings in `_()` (from `frappe import _`).
- Server endpoints use `@frappe.whitelist()`.
- Use `frappe.utils` helpers (`getdate`, `flt`, `nowdate`, `add_days`).
- `.pre-commit-config.yaml` excludes many legacy files from hooks. Don't reformat unrelated legacy code in a feature PR. Keep the diff minimal and add no new ruff findings.

## JavaScript
- **ESLint** (flat config, `eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, `__`).
- **Prettier**: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- Prettier skips `patient_portal/` and a few large doctype scripts.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. Translatable strings use `__()`.
- Portal: Vue 3 SFCs in PascalCase (`BookAppointmentModel.vue`). The `@` alias points to `patient_portal/src`.

## Commits
- Conventional Commits, enforced by commitlint.
- Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case.
- Formatting-only commits go in `.git-blame-ignore-revs`.
