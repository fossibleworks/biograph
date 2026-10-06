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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/public/js/observation_widget.js
---

**Python (ruff, `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110, target py310.
- Enabled lint rule sets: F, E, W, I, UP, B, RUF (several ignored: E501, F401, B904, …).
- Import order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with a blank line between sections.
- Doctype controllers are `class PascalCaseName(Document)` in `doctype/<snake_case>/<snake_case>.py`. Methods are snake_case and grouped as `validate_*` / `set_*` calls from `validate()`.
- Wrap user-facing strings in `_()` (`from frappe import _`).
- Expose server methods to the client with `@frappe.whitelist()`.
- Files start with the Frappe copyright and license header.

**JavaScript (prettier + ESLint):**
- Tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`.
- ESLint uses `eslint:recommended`, with `frappe`, `erpnext`, `$`, `jQuery` and `__` declared as globals.
- Desk scripts use `frappe.ui.form.on("DocType", {...})`.
- Translate strings with `__("...")`.
- Prettier skips `patient_portal/` and a few jinja-laden doctype scripts.

**Vue (patient_portal):** SFCs in `src/components/PascalCase.vue`. Import components from `frappe-ui`. Use the `@` alias for `src`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test, with an optional scope such as `fix(tests):` or `docs(wiki):`. The type must be lower-case.
