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
  - healthcare/tests/test_utils.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner (unittest-based) runs against a real MariaDB site. Use `bench --site test_site run-parallel-tests --app healthcare` (CI) or `bench run-tests` locally.
- **Layout:** co-locate `test_<doctype>.py` inside each DocType folder (about 85 test files). Cross-cutting tests go in `healthcare/tests/` (e.g. `test_utils.py`).
- **Base class:** test classes subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`. Nearly every test class does this. `HealthcareTestSuite` builds on ERPNext's `ERPNextTestSuite` and bootstraps master data via `BootStrapTestData`:
  - `_Test Company` and accounts like `Debtors - _TC`
  - patients, practitioners, service units, and templates
  - `_Test Insurance Payor`, and similar records
- **Style:**
  - `setUp` calls `super().setUp()` and often clears tables with `frappe.db.sql("delete from `tab...`")`.
  - Module-level factory helpers (`create_appointment`, `create_encounter`) build fixtures.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Assert with `assertEqual`/`assertTrue`.
  - Test records use the `_Test ` prefix.
- **Coverage expectations** (`codecov.yml`):
  - patch coverage target **85%** on PRs
  - project coverage `auto` with a 0.5% threshold
  - CI must pass first
- CI skips server tests for PRs that only touch css/js/md/html/csv.
- The fork has no CI baseline yet (see `wiki/upstream-sync-version-16.md`). Record pre-existing failures when you compare.
