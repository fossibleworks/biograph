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
  - commitlint.config.js
  - healthcare/healthcare/api/patient_portal.py
---

**Python (ruff, configured in `pyproject.toml`)**
- Indent with **tabs**, use **double quotes**, and keep lines to 110 characters. Lint rule sets: F, E, W, I, UP, B, RUF (several are ignored, such as F401 and E501).
- Import order uses custom isort sections: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Put a blank line between groups, as in `patient_appointment.py`.
- Use `typing-modules = ["frappe.types.DF"]` for DocType field type hints. Recent commits add type hints (`fix: add type hints`).
- **Naming:**
  - DocType folders and modules are snake_case (`patient_appointment`). Controller classes are PascalCase and match the DocType name (`class PatientAppointment(Document)`).
  - Custom exceptions subclass `frappe.ValidationError` (`MaximumCapacityError`, `OverlapError`).
  - Module-level functions are snake_case, and RPC entry points are marked `@frappe.whitelist()`.
- Controllers implement Frappe lifecycle hooks (`validate`, `before_save`, `on_update`, `on_submit`, `on_cancel`) and split the work into small `validate_*` and `set_*` methods.
- Wrap every user-facing string with `_()` in Python and `__()` in JS.
- Prefer `frappe.qb` and `frappe.get_list` / `frappe.db.get_value` over raw `frappe.db.sql`. Raw SQL still exists, about 91 call sites.
- Older files carry `# Copyright (c) <year>, ESS LLP and contributors` headers.

**JavaScript and Vue**
- Prettier settings: tabs (`useTabs: true`, `tabWidth: 4`), `printWidth: 88` and `arrowParens: "avoid"`. Prettier skips `patient_portal/**` and a few large form scripts.
- ESLint uses `eslint:recommended`, with Frappe desk globals (`frappe`, `erpnext`, `$`, `moment`, `__`) declared in `eslint.config.mjs`.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` and live next to the DocType.
- Portal components are PascalCase `.vue` files in `patient_portal/src/components/`. The `@` alias points to `src`.

**Lint debt:** the large `exclude` list in `.pre-commit-config.yaml` keeps many legacy files out of linting. Do not widen it for new files. Keep each file's lint count the same or lower (the sync ledger tracks a before → after count).

**Commits** follow Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Use lower-case types with an optional scope, for example `fix(tests): …` or `docs(wiki): …`.
