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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/src/PatientPortal.vue
---

**Python** (ruff 0.15.18 via pre-commit, configured in `pyproject.toml`)
- **Tabs** for indentation, double quotes, line length 110 (E501 is ignored). Target is py310.
- Lint rule set: `F,E,W,I,UP,B,RUF`, with notable ignores: F401 (unused imports), F403/F405, E402, B904.
- Import order uses custom isort sections: future → stdlib → third-party → `frappe` → `erpnext` → `healthcare`, with a blank line between each group.
- Use absolute dotted imports such as `from healthcare.healthcare.doctype.x.x import ...`.
- Wrap user-facing strings in `_()` (`from frappe import _`), using positional `{0}` formatting: `_("Patient {0} is not admitted in the service unit {1}").format(...)`.
- Prefer `frappe.qb` for new queries. Raw `frappe.db.sql` still exists (about 91 call sites, versus about 80 using qb).
- Doctype naming: the folder and module use snake_case (`patient_appointment`), the class uses PascalCase (`PatientAppointment`), and the DocType name uses Title Case ("Patient Appointment"). Expose client-callable functions with `@frappe.whitelist()`.
- Older files carry a `# Copyright (c) <year>, ...` / `# See license.txt` header.
- **Legacy exclusion:** about 620 legacy paths are listed in the `exclude` block of `.pre-commit-config.yaml`, so pre-commit skips them. When you touch them, do not add new ruff findings. The sync ledger records ruff counts before and after.

**JavaScript/Vue** (prettier and eslint)
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `__`, `$`, `erpnext`, `moment`, ...).
- Desk strings use `__('...')`.
- Portal uses Vue 3 `<script setup>`, frappe-ui components (`Tabs`, `Dialog`, `createResource`), the `@/` alias for `src/`, and PascalCase component filenames (`BookAppointmentModel.vue`). Variables are often snake_case (`portal_tabs`, `alert_dialog`).

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Use a lower-case type and an optional scope, for example `fix(tests): ...` or `docs(wiki): ...`.
