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
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner (unittest-based), run through `bench run-tests` / `run-parallel-tests --app healthcare` against a real MariaDB site.
- **Layout:** tests sit next to the code, as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** subclass **`HealthcareTestSuite`** from `healthcare.tests.utils`, which builds on ERPNext's `ERPNextTestSuite`. Recent commits migrated all fork tests to it. Always call `super().setUp()`.
- **Fixtures:** `BootStrapTestData` creates master data (`_Test Company`, practitioners, patients, service units, templates, insurance payors and so on) through `make_records`. Test records are prefixed `_Test`. Look existing records up with `frappe.get_list(..., pluck="name")` instead of relying on fixed names, which keeps tests deterministic.
- Toggle settings through `frappe.db.set_single_value("Healthcare Settings", ...)` inside the test.
- Keep helper factories (`create_appointment`, `create_encounter`) in the test module and import them from other tests when needed.
- **Coverage:** Codecov. The patch target is **85%**, and the project may drop by at most 0.5%. Coverage is collected on scheduled and non-PR runs.
- **Baseline:** the fork's CI has no historical baseline (see the wiki ledger). Compare failures against the commit that introduced them.
