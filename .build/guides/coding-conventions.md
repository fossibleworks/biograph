---
title: Coding Conventions
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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .git-blame-ignore-revs
---

**Python** (ruff, configured in `pyproject.toml`)
- Indent with **tabs**. Use double quotes. Line length is 110 (E501 is ignored). Target py310.
- Lint rules: F, E, W, I, UP, B, RUF, with Frappe-style ignores (F401 unused imports, E402, B904, and others).
- isort section order: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. A blank line separates the frappe, erpnext and healthcare groups. See `api/patient_portal.py`.
- Always import translations as `from frappe import _`, and wrap every user-facing string in `_()`. Use positional formatting with `.format()`: `_("User {0} is disabled").format(self.user_id)`.
- DocType controllers are `class PatientAppointment(Document)`. They use Frappe lifecycle hooks (`validate`, `on_submit`, `on_cancel`, `on_update`) that delegate to small `validate_*` / `set_*` methods.
- Mark API functions with `@frappe.whitelist()`. Module-level helpers use snake_case.
- Use the query builder for new queries: `frappe.qb.DocType(...)`, with `.run(as_dict=True)`. There are about 105 legacy `frappe.db.sql` calls. Avoid adding more raw SQL, and never interpolate user input into SQL (semgrep checks this).
- File headers often carry `# Copyright (c) <year>, ... and contributors` / `# For license information, please see license.txt`.
- Naming: DocType folders and files are snake_case versions of the DocType name (`patient_appointment/patient_appointment.py`). Tests are `test_<name>.py`. Patches are `healthcare/patches/v16_0/<verb_description>.py` with an `execute()` function.

**JavaScript**
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `cur_frm`, `__`, `$`, ...).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap strings in `__()`.
- The Vue portal (`patient_portal/.prettierrc.json`) uses no semicolons and single quotes. Components are PascalCase `.vue` files that use `<script setup>`/the Composition API, the `@/` alias for `src/`, and frappe-ui components.

**Commits**: Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lowercase.
