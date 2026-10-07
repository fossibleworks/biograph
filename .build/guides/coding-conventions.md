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
---

**Python** (ruff config in `pyproject.toml`, pinned at ruff v0.15.18 through pre-commit)
- **Tabs for indentation**, double quotes, line length 110 (E501 ignored). `ruff format` with `indent-style = "tab"`.
- Lint rules `F, E, W, I, UP, B, RUF`, with a documented ignore list (F401 unused imports, E402, B904, and others).
- Import order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Each group is separated by a blank line (custom isort sections).
- Use absolute imports from `healthcare.healthcare.doctype.<dt>.<dt>`.
- Naming: snake_case for modules, functions and fields. DocType folders are the snake_case form of the DocType name (`Patient Appointment` → `patient_appointment/patient_appointment.py`). Controller classes are PascalCase (`class PatientAppointment(Document)`). Custom exceptions subclass `frappe.ValidationError` with names like `OverlapError` or `MaximumCapacityError`.
- Expose server functions to the client with `@frappe.whitelist()` (about 180 in the codebase).
- Wrap user-facing strings in `_()` and use `{0}` placeholders with `.format()`, e.g. `_("Invalid Code Value: {0}").format(code_value)`.
- Prefer the Frappe ORM (`frappe.get_doc`, `frappe.db.get_value`, `frappe.get_all/get_list(..., pluck=)`). Raw `frappe.db.sql` exists (31 files) but must be parameterised. Semgrep's Frappe rules enforce this. Use `# nosemgrep` only with a reason.
- `typing-modules = ["frappe.types.DF"]` is set for DocType type hints.
- Many older files are listed in the pre-commit `exclude` block, so they are not reformatted yet. Do not mass-reformat them in unrelated PRs.

**JavaScript** (`eslint.config.mjs`, `.prettierrc.yaml`)
- `eslint:recommended`, with Frappe desk globals (`frappe`, `erpnext`, `$`, `moment`, …) declared.
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. The `patient_portal/` folder and some Jinja-heavy doctype JS files are excluded.
- Desk scripts use `frappe.ui.form.on('<DocType>', {...})`. User-facing strings use `__()`.
- The Vue portal uses single-file components in `patient_portal/src/components/*.vue`, PascalCase names (`BookAppointmentModel.vue`), and frappe-ui components.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. The type must be lower-case and the subject non-empty.
