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
  - healthcare/healthcare/doctype/allergy/test_allergy.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's test runner (unittest-style), run inside a bench site. CI runs `bench --site test_site run-parallel-tests --app healthcare` against MariaDB, with ERPNext and payments installed.
- **Layout:** tests live next to the code as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Shared fixtures are in `healthcare/tests/utils.py`.
- **Base class:** every test class extends `HealthcareTestSuite` (a subclass of ERPNext's `ERPNextTestSuite`) and is named `Test<DocType>`. `BootStrapTestData` seeds master data with a `_Test` prefix: company, patients, practitioners, service units, templates, insurance payors and so on.
- **Patterns:** `setUp()` calls `super().setUp()`, clears the relevant tables, and toggles settings with `frappe.db.set_single_value("Healthcare Settings", ...)`. Records are built with module-level helpers such as `create_appointment(...)`. Assertions use `self.assertEqual` and `self.assertRaises`. Many doctypes still have stub tests (`pass`).
- **Coverage:** collected only on non-PR runs (the scheduled daily run) and uploaded to Codecov (`codecov.yml`, `CAPTURE_COVERAGE`). There is no enforced threshold on PRs.
- **Baseline note:** the fork had no CI history on `biograph-fh`. The first CI run on a goal PR is the baseline, so compare failures against the commit that introduced them.
- Portal (Vue) code has no JS test suite.
