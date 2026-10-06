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
  - commitlint.config.js
  - .git-blame-ignore-revs
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored), target py310.
- Lint set: `F, E, W, I, UP, B, RUF`, with a documented ignore list (for example F401 unused imports, E402, B904).
- isort section order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Each group is separated by a blank line, as seen in `patient.py` and `fee_validity` tests.
- Use absolute imports from the `healthcare.` root. Wrap user-facing strings in `_()` from `frappe`.
- DocType controllers are classes named after the DocType in PascalCase (`class Patient(Document)`) in `doctype/<snake_case>/<snake_case>.py`. Server endpoints use `@frappe.whitelist()`.
- Prefer `frappe.qb` for new queries (see `api/patient_portal.py`).
- Note: `.pre-commit-config.yaml` has a top-level exclude covering about 600 legacy files, so pre-commit skips them. New files are linted. Don't add new paths to that exclude list.

**JavaScript**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`…).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap strings in `__()`.
- `patient_portal/` (Vue SFCs, Options API with frappe-ui components) is excluded from prettier.

**Commits:** Conventional Commits, enforced by commitlint (`feat|fix|chore|docs|refactor|perf|test|ci|build|style|revert`, lower-case type, non-empty subject). Upstream-sync commits add the suffix `(upstream sync Bn)`.
