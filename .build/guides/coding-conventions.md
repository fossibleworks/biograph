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
  - healthcare/healthcare/api/patient_portal.py
  - .pre-commit-config.yaml
---

**Python** (ruff, `pyproject.toml`):
- **Tabs** for indentation, double quotes, line length 110, target py310.
- Lint sets F, E, W, I, UP, B and RUF, with a documented ignore list. Line length and unused imports are ignored.
- Import sections are ordered future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local, with a blank line between each.
- `typing-modules = frappe.types.DF`.
- Strings: user-facing ones are wrapped in `_()` (`from frappe import _`).
- Endpoints: client-callable functions are decorated with `@frappe.whitelist()`.
- Queries: prefer `frappe.qb` (query builder) or `frappe.get_all`/`get_list` with `pluck=`. Raw `frappe.db.sql` exists, but mostly in legacy code and tests.
- Controllers are classes named after the doctype in PascalCase, with files in snake_case, e.g. `patient_appointment/patient_appointment.py` → `PatientAppointment`.
- Hook paths use the full dotted module path, e.g. `healthcare.healthcare.doctype.<dt>.<dt>.<fn>`.
- Type hints are being added to new code.

**JavaScript** (Prettier + ESLint):
- Tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`.
- ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `__`, `$`, `moment`, `erpnext`, …).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`.
- User-facing strings are wrapped in `__()`.
- Vue SFCs in `patient_portal/src/components` are PascalCase. Some use the existing `*Model.vue` naming for dialogs.

**Patches:** put them in `healthcare/patches/v<major>_0/<descriptive_name>.py` with an `execute()` function, and append them to `patches.txt`.

**Commits:** Conventional Commits, enforced by commitlint. Types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, all lower-case. Optional scope, e.g. `fix(tests): …`, `docs(wiki): …`.
