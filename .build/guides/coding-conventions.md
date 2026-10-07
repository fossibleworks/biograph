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
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/healthcare/doctype/patient/patient.py
---

**Python (ruff, configured in `pyproject.toml`)**
- Indent with **tabs**, use **double quotes**, line length 110 (E501 ignored), target py310.
- Lint rule sets: F, E, W, I, UP, B, RUF. Many rules are ignored to match Frappe style, including F401, E402, B904 and W191.
- Import order (isort sections): future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Each group is separated by a blank line, as in the test files.
- Type hints for doctype fields come from `frappe.types.DF` (typing-modules).
- Naming: snake_case modules and functions. Doctype controller classes are PascalCase and match the doctype name (`class Patient(Document)`). Doctype folders are the snake_case of the doctype title.
- Expose client-callable functions with `@frappe.whitelist()` (about 182 uses). Wrap every user-facing string in `_()` (about 494 uses).
- Files start with a copyright header comment (`# Copyright (c) <year>, <org> and Contributors` / `# See license.txt`).

**JavaScript**
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended`, with globals for `frappe`, `erpnext`, `$`, `jQuery` and `Vue`.
- Desk scripts use the `frappe.ui.form.on('<DocType>', {...})` style, and translatable strings use `__()`.
- The portal (`patient_portal/`) is not covered by Prettier. It uses 2-space indented Vite configs and Vue SFCs with the `@` alias pointing to `src`.

**Legacy exclusion:** `.pre-commit-config.yaml` holds a top-level `exclude` list of about 620 existing files that skip all hooks. Ruff and Prettier still apply to new files. When you touch an excluded file, follow its local style and do not reformat the whole file.

**Commits:** Conventional Commits, enforced by commitlint. Lower-case type from: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Optional scope, e.g. `fix(appointment): ...`.
