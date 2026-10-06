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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .pre-commit-config.yaml
  - commitlint.config.js
---

**Python** (ruff, `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110. Rule sets: F, E, W, I, UP, B, RUF. Many rules are ignored, including F401 unused imports, E501, and B904.
- Import order: stdlib → third-party → `frappe` → `erpnext` → `healthcare`, with each group separated by a blank line. Use absolute dotted imports (`from healthcare.healthcare.doctype.fee_validity.fee_validity import ...`).
- Wrap user-facing strings in `_()` from `frappe` (`from frappe import _`).
- Each DocType's controller lives at `doctype/<snake_name>/<snake_name>.py` as `class PatientAppointment(Document)`. Hooks are methods such as `validate`, `on_submit`, and `on_cancel`. Client-callable functions use `@frappe.whitelist()`.
- Files start with a copyright/license header comment.
- `pre-commit-config.yaml` holds a very large exclude list of legacy files that are not linted. New files are linted, so don't add new entries to that list.

**JavaScript**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint: `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `__`, etc.).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap strings in `__()`.

**Vue (patient_portal)**
- Single-file components in PascalCase (`BookAppointmentModel.vue`, `PractitionerSelector.vue`), Tailwind classes, and frappe-ui components.

**Commits:** Conventional Commits (`feat|fix|chore|docs|refactor|perf|test|ci|build|style|revert`) with a lower-case type, enforced by commitlint. Upstream picks use `git cherry-pick -x`.
