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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs for indentation**, double quotes, line length 110 (E501 is ignored, so long lines are tolerated).
- Lint rule sets: `F, E, W, I, UP, B, RUF`. Several rules are relaxed, including F401 unused imports, E402, B904, and E741.
- **Import order** (isort sections): future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Put a blank line between groups, as in `test_patient_appointment.py`.
- Use absolute imports from the app root: `from healthcare.healthcare.doctype.<x>.<x> import ...`.
- **Naming:** DocType folders and files are `snake_case` of the DocType name (`patient_appointment/patient_appointment.py`). Controller classes are `PascalCase` DocType names extending `Document`. Error classes are `<Thing>Error(frappe.ValidationError)`. DocType names in code are Title Case strings (`"Patient Appointment"`).
- Wrap every user-facing string in `_()` (`from frappe import _`) and use positional `{0}` formatting: `_("... {0}").format(x)`.
- Mark server methods called from JS or the portal with `@frappe.whitelist()`. Restrict methods where relevant, e.g. `methods=["POST"]`. Use `allow_guest=True` only for the portal.
- Prefer the ORM (`frappe.get_doc`, `frappe.db.get_value`, `frappe.get_list(..., pluck="name")`, `frappe.qb`) over raw SQL. Raw `frappe.db.sql` exists in about 90 places, mostly older code and tests.
- `typing-modules = ["frappe.types.DF"]`: auto-generated type annotation blocks in controllers are allowed.

**JavaScript / Vue**
- Prettier: **tabs**, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended`, with Frappe globals (`frappe`, `__`, `$`, `moment`, `erpnext`...).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`, and wrap strings in `__()`.
- Portal: Vue 3 SFCs in PascalCase (`BookAppointmentModel.vue`), Tailwind utility classes, frappe-ui components, and the `@/` alias for `patient_portal/src`.

**Legacy exclusions:** `.pre-commit-config.yaml` holds a very long `exclude:` list (~600 lines) of existing files that are not yet lint-clean. Do not reformat excluded files wholesale. Keep diffs minimal so upstream cherry-picks stay applicable, and do not add new ruff findings to files you touch. The sync ledger tracks ruff counts before and after.
