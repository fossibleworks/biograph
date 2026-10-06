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
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

**Python (ruff)**
- Indent with **tabs**, use **double quotes**, line length 110 (E501 is ignored, so long lines are tolerated). Target py310.
- Lint rule sets are `F,E,W,I,UP,B,RUF`. Notable ignores: F401 (unused imports), B904, E402, F403/F405.
- Import order: future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Separate each group with a blank line, as in `test_patient_appointment.py`.
- Use absolute imports from the package root, e.g. `from healthcare.healthcare.doctype.x.x import y`.
- Files and folders are `snake_case` matching the DocType name (`Patient Appointment` → `patient_appointment/patient_appointment.py`). Controller classes are `PascalCase` doctype names subclassing `Document`.
- Wrap user-facing strings in `_()` (`from frappe import _`), and use `.format()` for placeholders (`_("{0} with {1}").format(...)`).
- Expose server endpoints with `@frappe.whitelist()`. Prefer `frappe.qb` or `frappe.get_all`/`get_list` over raw SQL. Raw `frappe.db.sql` appears mainly in tests.
- Keep the license header comment at the top of doctype files, matching the existing ones.
- Semgrep's Frappe rules apply. Suppress a rule only with an inline `# nosemgrep` and a reason.

**JavaScript (Desk)**
- Prettier settings: tabs (`useTabs: true`, `tabWidth: 4`), `printWidth: 88`, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `__`, ...).
- Translate strings with `__("...")`.
- Form scripts follow the `frappe.ui.form.on("Doctype", {...})` pattern.

**Vue (patient_portal)**
- Vue 3 SFCs with PascalCase component names (`BookAppointmentModel.vue`, `PractitionerSelector.vue`). Use frappe-ui components (`Button`, `Dialog`, ...) and Tailwind utility classes. The `@/` alias points to `src/`.
- `patient_portal/` is excluded from Prettier, so match the formatting of the surrounding file.

**Commits:** Conventional Commits with lower-case type from `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`. A subject is required.
