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

- **Framework:** Frappe's test runner (unittest-based), run as `bench --site test_site run-parallel-tests --app healthcare` in CI against a real MariaDB site with ERPNext installed.
- **Layout:** tests sit next to their code as `test_<doctype>.py` inside each doctype folder (about 85 test files). There are also `healthcare/tests/test_utils.py`, `regional/india/abdm/test_abdm.py` and `custom_doctype/test_sales_invoice.py`.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on `ERPNextTestSuite`. `BootStrapTestData` creates the master data (company, items, patients, practitioners, service units, templates, insurance payors…). Records use the `_Test …` naming prefix.
- **Style:** tests are integration tests. `setUp` calls `super().setUp()`, cleans tables, and creates docs through module-level `create_*` helpers (e.g. `create_appointment`, `create_encounter`). Assert on DB state (`frappe.db.get_value`) and use `assertRaises(frappe.ValidationError …)` for validations. Toggle settings with `frappe.db.set_single_value("Healthcare Settings", …)`.
- **Coverage:** Codecov patch target is **85%** on PRs to `develop`, and the project threshold allows at most a 0.5% drop. Coverage is captured on scheduled/non-PR CI runs.
- **Not tested in CI:** CI skips PRs that only touch `**.js/.css/.md/.html/.csv`. There is no frontend unit-test setup for `patient_portal/`.
