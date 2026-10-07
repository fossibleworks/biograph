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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

**Python (ruff, configured in `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110 (E501 is ignored). Format with `ruff format`.
- Lint rule sets: F, E, W, I, UP, B, RUF, with the ignores listed in `pyproject.toml` (e.g. F401 unused imports, B904).
- Import order: future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Each group is a separate section.
- Naming: modules and functions are `snake_case`. Controller classes are `PascalCase` and match the doctype (`class PatientAppointment(Document)`). Doctype folders are snake_case versions of the doctype name.
- Use full dotted paths for hook targets and imports (`healthcare.healthcare.doctype.<x>.<x>.<fn>`).
- Mark client-callable functions with `@frappe.whitelist()`. Newer code adds type hints to their arguments (`def get_print_format(doctype: str, name: str)`).
- Wrap user-facing strings in `_()` (`from frappe import _`).
- Many legacy files are listed in `.pre-commit-config.yaml`'s `exclude` block. Pre-commit skips them, but do not add new ruff findings to them (the upstream-sync ledger tracks before/after counts).

**JavaScript (desk):** Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `__`, `erpnext`, `$`, …). Wrap strings in `__()`. Form scripts use the `frappe.ui.form.on('<DocType>', {...})` pattern.

**Vue (patient_portal):** Prettier does not cover it. Components are PascalCase `.vue` files, often named `*Model.vue` for modal dialogs. They use `<script setup>` and frappe-ui `createResource` for data.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Lower-case type, non-empty subject. Scopes are optional, e.g. `docs(wiki): …`, `fix(tests): …`.
