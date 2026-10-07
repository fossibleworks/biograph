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
  - patient_portal/.prettierrc.json
  - eslint.config.mjs
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs for indentation.** Double quotes, line length 110, target py310.
- Lint rules selected: F, E, W, I, UP, B, RUF. Several rules are ignored on purpose, including E501, F401 and B904.
- isort section order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with a blank line between groups. Example: `import frappe` / `from erpnext...` / `from healthcare...`.
- Wrap user-facing strings in `_()`, e.g. `frappe.throw(_("...").format(x))`. Build links with `get_link_to_form`.
- Names: snake_case functions and modules, PascalCase controller classes that match the DocType name (e.g. `class PatientAppointment(Document)`). DocType names are Title Case with spaces, e.g. `"Patient Appointment"`, `"Healthcare Settings"`.
- Prefer `frappe.qb` or `frappe.get_all` / `frappe.db.get_value` over raw `frappe.db.sql` in new code. Raw SQL still exists, mostly in older code and tests.
- Expose client-callable functions with `@frappe.whitelist()`.

**JavaScript (Desk)**
- Prettier: tabs, width 4, printWidth 88, `arrowParens: avoid`.
- ESLint flat config: `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap strings in `__()`.

**Vue (patient_portal)**
- Own Prettier config: no semicolons, single quotes. It is excluded from the root prettier hook.
- Use `<script setup>` style with frappe-ui components and Tailwind utility classes.

**Commits:** Conventional Commits, lower-case type from build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test. Scopes are optional, e.g. `fix(tests): ...`, `docs(wiki): ...`.
