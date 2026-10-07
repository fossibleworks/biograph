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

**Python (ruff, config in `pyproject.toml`):**
- Indent with **tabs**, use double quotes, line length 110, target py310. Run `ruff format` with `docstring-code-format`.
- Lint rules `F, E, W, I, UP, B, RUF`, with a documented ignore list. Unused imports (F401) are ignored, and line length (E501) is not enforced.
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Each group is separated by a blank line (see `test_patient_appointment.py`).
- Many legacy files are listed in the `.pre-commit-config.yaml` `exclude` block. Don't mass-reformat them, because that inflates diffs and breaks upstream cherry-picks.
- Naming: DocType folders and modules are `snake_case` versions of the DocType name (`patient_appointment/patient_appointment.py`). Controller classes are CamelCase (`PatientAppointment(Document)`). Custom exceptions subclass `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`).
- Wrap user-facing strings in `_()`. Use `.format()` placeholders inside the translated string, e.g. `_("Please set {0}").format(...)`.
- Expose API methods with `@frappe.whitelist()`.

**JavaScript (ESLint flat config + Prettier):**
- Indent with tabs (tabWidth 4), printWidth 88, `arrowParens: avoid`.
- `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment` …). Wrap desk strings in `__()`.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`.
- The Patient Portal (Vue SFCs) is excluded from Prettier and follows its existing style (frappe-ui components, `createResource`).

**Commits:** Conventional Commits, enforced by commitlint: types `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case type, non-empty subject. Upstream-sync work uses `git cherry-pick -x`.
