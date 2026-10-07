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

- **Framework:** Frappe's unittest-based runner. Test classes extend **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses ERPNext's `ERPNextTestSuite`. Recent commits moved all fork tests to this base class. When you override `setUp`, call `super().setUp()`.
- **Fixtures:** `BootStrapTestData` creates shared master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors and more. Test record names start with `_Test`. Tests usually fetch existing records (`frappe.get_list("Patient", pluck="name")[0]`) instead of creating companies inline. Keep tests deterministic.
- **Layout:** each test sits next to its DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Cross-cutting tests go in `healthcare/tests/`.
- **Style:** `assertEqual` / `assertTrue` against `frappe.db.get_value(...)`. Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`. Module-level helper factories such as `create_appointment(...)` are used.
- **Running:** `bench --site test_site run-parallel-tests --app healthcare`. CI runs this against MariaDB 11.8 on every PR (except changes to only css/js/md/html/csv files) and nightly.
- **Coverage:** captured on non-PR runs and uploaded to Codecov. `codecov.yml` sets a **patch target of 85%** on PRs and a project threshold of 0.5%.
- **Baseline note:** `wiki/upstream-sync-version-16.md` records that the fork had no earlier CI history for `ci.yml`. Compare the first goal-PR CI run against the commit that introduced each failure.
