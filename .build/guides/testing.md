---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/tests/utils.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's test runner (unittest-based). Test classes subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite` and bootstraps master data (company, items, patients, practitioners, service units, templates, …) through `BootStrapTestData`.
- **Layout:** each doctype has a co-located `test_<doctype>.py` inside its doctype folder. There are about 85 test files. Shared helpers live in `healthcare/tests/`.
- **Style:**
  - `setUp` calls `super().setUp()`, clears the relevant tables, and looks up fixtures with `frappe.get_list(..., pluck="name")`.
  - Settings are toggled with `frappe.db.set_single_value`.
  - Module-level factory helpers are used, e.g. `create_appointment(...)`.
  - Assertions use `self.assertEqual` / `assertRaises`.
- **Running:** tests need a bench with ERPNext and a MariaDB site. CI runs `bench --site test_site run-parallel-tests --app healthcare`, and it skips PRs that touch only css/js/md/html/csv.
- **Coverage:** captured on scheduled/non-PR runs and uploaded to Codecov. `codecov.yml` sets the patch target at **85%** for PRs against `develop`, with a 0.5% project threshold.
- **Fork note:** the fork has no CI baseline yet. The first goal-PR CI run is the baseline (per the upstream-sync ledger).
