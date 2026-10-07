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
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - commitlint.config.js
  - patient_portal/src/components/BookAppointmentModel.vue
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored, so the limit is a guideline).
- Lint set: `F, E, W, I, UP, B, RUF`. Notable ignores: F401 (unused imports), F403/F405, B904, E402.
- isort section order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Put a blank line between groups, as in:
  ```python
  import frappe
  from frappe.utils import add_days, nowdate

  from erpnext.accounts.doctype.pos_profile.test_pos_profile import make_pos_profile

  from healthcare.tests.utils import HealthcareTestSuite
  ```
- Use absolute dotted imports (`healthcare.healthcare.doctype.<name>.<name>`).
- Use Frappe idioms: a controller class per doctype (`class PatientAppointment(Document)`) with `validate`/`on_submit`/`on_cancel` hooks; `@frappe.whitelist()` for anything the client calls; `frappe.db.get_value` / `get_single_value` / `frappe.qb` (about 80 uses), or `frappe.db.sql` (about 91 uses) with parameters.
- Wrap user-facing strings in `_()`. Prefer `_("... {0}").format(x)` over f-strings inside `_()`.
- **Legacy exclusion list:** `.pre-commit-config.yaml` has a large `exclude:` block listing almost every existing file, so most legacy code is *not* auto-formatted. When you touch a listed file, keep its existing style. Do not reformat the whole file, because that creates huge diffs and upstream-sync conflicts. New files are linted.

**JavaScript (desk)**
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint flat config (`eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, …).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})` and `__()` for strings.

**Vue (patient_portal)**
- `<script setup>` style with `import { ref, computed } from 'vue'`, frappe-ui components (`Button`, `Dialog`, `createResource`, …), and the `@/` alias for `src/`. Prettier is **not** run on `patient_portal/`.

**Naming:** doctype folders and files use snake_case of the DocType name (`patient_appointment/patient_appointment.py`), and DocType names are Title Case ("Patient Appointment"). Patches go in `healthcare/patches/v<major>_0/<verb_phrase>.py` and are registered in `patches.txt`.

**Commits:** Conventional Commits, enforced by commitlint (`build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, lowercase type, non-empty subject), for example `fix(tests): ...` or `docs(wiki): ...`.
