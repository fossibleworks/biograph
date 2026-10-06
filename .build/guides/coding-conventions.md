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
  - healthcare/healthcare/api/patient_portal.py
  - .git-blame-ignore-revs
---

**Python (ruff, `pyproject.toml`):**
- **Tabs** for indentation, double quotes, line-length 110 (E501 is ignored, so long lines are tolerated). Target py310.
- Lint rule sets: F, E, W, I, UP, B, RUF, with Frappe-typical ignores (F401, F403/F405, E402, B904, W191, ...).
- Import order is enforced by isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Put a blank line between each.
- Use absolute imports from `healthcare.healthcare.doctype.<x>.<x>`.
- Doctype controllers are classes named after the DocType in PascalCase (`class PatientAppointment(Document)`). Module and folder names are snake_case.
- Public server methods use `@frappe.whitelist()`.
- Prefer `frappe.qb` over raw `frappe.db.sql`. Both exist (about 80 vs 91 uses); new code in `api/` uses qb.
- Wrap every user-facing string in `_()` and use `.format()` placeholders (`_("Invalid Code Value: {0}").format(v)`).

**JavaScript / Vue (prettier + eslint):**
- Tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`.
- eslint 10 flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Desk strings use `__()`.
- The portal uses `<script setup>`-style Vue SFCs with Tailwind utility classes and the `@` alias for `src`.

**Upstream-shared code:** many legacy files are excluded from pre-commit (the long `exclude` list in `.pre-commit-config.yaml`). Do not mass-reformat them; that creates churn against upstream earthians/marley. Record mass-format commits in `.git-blame-ignore-revs`.
