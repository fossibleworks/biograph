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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/public/js/healthcare_note.js
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored, so the limit is soft). Docstring code is formatted.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with Frappe-friendly ignores (F401, F403/F405, E402, B904 and others).
- Import order uses custom isort sections: `future → stdlib → third-party → frappe → erpnext → healthcare → first-party → local`. Example from `test_patient_appointment.py`: `import frappe` / `from frappe.utils import ...`, then a blank line, `from erpnext...`, a blank line, then `from healthcare...`.
- Type hints use `frappe.types.DF` (`typing-modules`).
- Naming:
  - DocType controllers are PascalCase classes named after the DocType (`class PatientAppointment(Document)`) and live in `snake_case` modules.
  - Lifecycle methods are `validate`, `before_save`, `on_update`, `after_insert`, `on_submit` and `on_cancel`. `validate` calls small helpers named `validate_*` and `set_*`.
  - Module-level helpers called from JS are decorated with `@frappe.whitelist()`.
- User-facing strings are wrapped in `_()` and use `{0}` placeholders with `.format()`.
- `.pre-commit-config.yaml` excludes about 620 legacy files from hooks, and some (for example `patient_appointment.py`) mix spaces and trailing whitespace. Do not add new files to that list. Do not reformat a whole excluded file as part of an unrelated change.

**JavaScript**
- Prettier settings: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. The `patient_portal/` folder and three large doctype JS files are excluded.
- ESLint uses `eslint:recommended` (flat config) with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Translatable strings use `__('…')`.
- Desk scripts use `frappe.ui.form.on('<DocType>', {...})`.

**Vue portal:** SFCs in `patient_portal/src/components` use PascalCase names (`BookAppointmentModel.vue`). The `@` alias maps to `src`. Styling uses Tailwind utility classes.

**Commits:** Conventional Commits, enforced by commitlint: lower-case type from `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test` and a non-empty subject. Scopes such as `fix(tests):` and `docs(wiki):` are used.
