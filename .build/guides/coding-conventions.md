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
  - healthcare/healthcare/doctype/patient/patient.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - commitlint.config.js
---

**Python** (enforced by ruff through pre-commit; config in `pyproject.toml`)
- **Tabs for indentation**, double quotes, line length 110 (E501 is ignored, so long lines are tolerated).
- Lint set `F,E,W,I,UP,B,RUF`. Several rules are ignored (F401 unused imports, B904, E402, ...).
- **Import order** (isort sections): stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local, with a blank line between groups. See `patient.py` and `test_fee_validity.py`.
- Use absolute imports from the package root: `from healthcare.healthcare.doctype.<x>.<x> import ...`.
- Files start with a `# Copyright (c) <year>, ... and contributors` / `# See license.txt` header.
- Doctype controllers are `class <DocTypeName>(Document)`, with hooks `validate`, `on_submit`, `on_cancel`, etc.
- Exposed functions use `@frappe.whitelist()` (182 uses).
- Prefer `frappe.qb` (query builder) or `frappe.db.get_value/get_list` over raw SQL. Raw `frappe.db.sql` still appears in about 90 places, mostly older code and tests.
- Wrap user-visible strings in `_()` from `frappe`. Use `.format()` placeholders: `_("... {0}").format(...)`. Don't put f-strings inside `_()`.
- Naming: snake_case modules and functions. DocType names are Title Case with spaces ("Patient Appointment") and map to snake_case folders.

**JavaScript**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Desk scripts use `frappe.ui.form.on("DocType", {...})`, `__()` for translatable strings, `frappe.call`, `frappe.show_alert` and `frappe.msgprint`.
- `patient_portal/` is excluded from Prettier. It uses Vue SFCs with 2-space indentation and frappe-ui components.

**Legacy exclusions:** `.pre-commit-config.yaml` has a large global `exclude` list (about 640 legacy files) that skips formatting. Code you touch there still has to read like its surroundings. Don't reformat whole excluded files in unrelated PRs.

**Commits:** Conventional Commits (`feat|fix|chore|docs|refactor|perf|test|ci|build|style|revert`, lower-case type), enforced by commitlint. The fork often adds a scope or suffix, e.g. `fix: ... (upstream sync B2)`.
