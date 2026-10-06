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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), running against a real MariaDB site.
- **Base class:** every test class extends `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. Recent commits migrated all fork tests to it. Override `setUp` and **always call `super().setUp()`**.
- **Shared fixtures:** `BootStrapTestData` creates the master data (company, items, patients, practitioners, service units, templates, insurance payors…). Its records use the `_Test` prefix.
- **Layout:** put `test_<doctype>.py` next to its DocType (`healthcare/healthcare/doctype/<name>/test_<name>.py`). There are about 85 test files.
- **Writing tests:**
  - Write module-level helper factories (`create_appointment(...)`, `create_encounter(...)`).
  - Look up fixtures deterministically with `frappe.get_list(..., pluck="name")`.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Coverage:** collected in CI only on non-PR (scheduled) runs (`WITH_COVERAGE`) and uploaded to Codecov. `codecov.yml` sets the thresholds.
- **Fork note:** the wiki records that there is no CI baseline on `biograph-fh`. Compare failures against untouched `biograph-fh` before attributing them to your change.
