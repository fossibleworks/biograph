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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - commitlint.config.js
  - patient_portal/.prettierrc.json
---

# Coding conventions

## Python (ruff, `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 not enforced). Format with `ruff format`.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with Frappe-friendly ignores (unused imports, `*` imports, tabs, B904, ...).
- Import order uses custom isort sections: stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with a blank line between each group.
- Use absolute dotted imports from the package root, e.g. `from healthcare.healthcare.doctype.patient_appointment.patient_appointment import ...`.
- Wrap user-facing strings in `_()` (`from frappe import _`). Use positional `{0}` placeholders and call `.format()` outside `_()`.
- Mark server endpoints with `@frappe.whitelist()`. Prefer `frappe.qb` / `frappe.get_all` over raw SQL.
- DocTypes: folder and module names are `snake_case` (`patient_appointment`), the DocType name is Title Case (`"Patient Appointment"`), and the controller class is PascalCase (`PatientAppointment(Document)`).
- Custom exceptions subclass `frappe.ValidationError` and are named `*Error` (`OverlapError`, `MaximumCapacityError`).
- Files start with a license/copyright header (`# Copyright (c) ..., ESS LLP and Contributors` / `# See license.txt`).

## JavaScript (Desk)
- **Tabs**, width 4, print width 88, `arrowParens: avoid` (Prettier). ESLint `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`, ...).
- Form scripts use `frappe.ui.form.on('<DocType>', { setup(frm) {...}, refresh(frm) {...} })`. Translate strings with `__('...')`.
- A few legacy form scripts are excluded from prettier (`patient.js`, `medication_request.js`, `service_request.js`). Do not mass-reformat them.

## Vue (patient_portal)
- Vue 3 SFCs in `src/components/PascalCase.vue`, `@/` alias to `src/`, Tailwind utility classes plus frappe-ui components. The portal has its own `.prettierrc.json` and is excluded from the root prettier hook.

## Commits
- Conventional Commits, enforced by commitlint. Types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case, non-empty subject.
