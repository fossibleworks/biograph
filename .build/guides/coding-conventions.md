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
  - healthcare/controllers/queries.py
  - commitlint.config.js
---

# Coding conventions

## Python
- **ruff** handles linting and formatting. Selected rules are `F, E, W, I, UP, B, RUF`, with many ignores (E501, F401, W191, B904, ...). **Indent with tabs**, use **double quotes**, line length 110.
- isort-style section order: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local, with a blank line between sections.
- Typing helpers come from `frappe.types.DF`.
- Naming:
  - Each DocType lives in `doctype/<snake_case>/` with `<snake_case>.py`, `.js` and `.json`. The controller class is the PascalCase DocType name (`class PatientAppointment(Document)`).
  - Functions and methods are `snake_case`, and validators are named `validate_*`.
  - Server methods that the client can call use `@frappe.whitelist()`. Link-field search queries also add `@frappe.validate_and_sanitize_search_inputs`.
- Prefer `frappe.qb` or the `frappe.db.get_*` APIs over raw `frappe.db.sql`. Both styles exist in the code.
- Wrap every user-facing string in `_()`, using positional `{0}` with `.format()` outside the `_()` call.
- Older files keep `# Copyright (c) ..., ESS LLP and contributors` headers.

## JavaScript (Desk)
- Form scripts use `frappe.ui.form.on('<DocType>', { setup, onload, refresh, <field>: fn })`.
- Translate strings with `__()`.
- prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals.

## Vue (portal)
- SFCs in `patient_portal/src/components/` are PascalCase (`BookAppointmentModel.vue`). Import frappe-ui components and resources. Use the `@` alias for `src/`.
- The portal is excluded from prettier.

## Legacy exclusions
- About 620 legacy files are listed in the pre-commit `exclude`. When editing one, follow the style already in that file and do not reformat the whole file. New files must pass every hook.
- Commit messages are Conventional Commits (lower-case type from the commitlint enum), for example `fix(tests): ...` or `docs(wiki): ...`.
