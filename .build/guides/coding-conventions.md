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
  - healthcare/healthcare/doctype/clinical_note/clinical_note.js
  - patient_portal/src/components/Payment.vue
---

**Python** (ruff, configured in `pyproject.toml`):
- Indent with **tabs** (`indent-style = "tab"`), use double quotes, and keep lines to 110 characters. E501 is ignored but the formatter wraps.
- Lint rule sets are `F, E, W, I, UP, B, RUF`, with a long ignore list that includes F401 unused imports. Do not add unused imports anyway: recent commits removed some (`fix: drop unused imports`).
- Import order uses custom isort sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate groups with blank lines (see `patient_appointment.py`).
- Import internal modules by full dotted path: `from healthcare.healthcare.doctype.x.x import fn`.
- Controllers are `class PascalCaseDoctype(Document)` and use Frappe lifecycle methods (`validate`, `on_submit`, `on_cancel`). Server functions are `snake_case`, and anything reachable from the client is decorated with `@frappe.whitelist()` (about 182 of them).
- Wrap user-facing strings in `_()` from `frappe`. Format with `.format()` and `frappe.bold()`. Use `get_link_to_form` for links.
- Use `frappe.qb` / `frappe.db.get_all` / `frappe.db.get_value` for queries. Raw `frappe.db.sql` exists; prefer the query builder in new code.
- Files start with a copyright header comment: `# Copyright (c) <year>, ... and contributors` / `# For license information, please see license.txt`.
- Many legacy files are listed in `.pre-commit-config.yaml`'s top-level `exclude` (about 600 paths) and are not auto-formatted. Some use spaces. When you edit one, match its existing style and do not add new ruff findings.

**JavaScript (desk):**
- Prettier: tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`.
- ESLint flat config: `eslint:recommended` plus Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Form scripts use `frappe.ui.form.on("Doctype", { refresh(frm) {...}, fieldname: function(frm) {...} })`.
- Wrap strings in `__()`.

**Vue (portal):**
- Write SFCs with `<script setup>`. Import components from `frappe-ui` (`Card`, `ErrorMessage`, `createResource`). Style with Tailwind utility classes. Components are PascalCase files in `patient_portal/src/components/`.
- Prettier skips `patient_portal/`.

**Naming:**
- DocType folders and files use snake_case of the DocType name (`patient_appointment/patient_appointment.py`).
- Patches go in `healthcare/patches/v16_0/<verb>_<what>.py`.
