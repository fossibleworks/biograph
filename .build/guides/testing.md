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
  - healthcare/healthcare/doctype/nursing_task/test_nursing_task.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB site. CI runs `bench --site test_site run-parallel-tests --app healthcare` on PRs and nightly.
- **Layout:** Each doctype has a co-located `test_<doctype>.py` next to its controller. There are about 85 test files.
- **Base class:** Subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`.
  - `BootStrapTestData` seeds master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors, …
  - Call `super().setUp()`.
  - Look up seeded records with `frappe.get_list(..., pluck="name")`.
- **Style:**
  - Write module-level factory helpers (`create_appointment`, `create_encounter`).
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Assert DB state with `frappe.db.get_value`.
  - Test validation failures with `self.assertRaises(frappe.ValidationError, doc.insert)` or a specific subclass (e.g. `OverlapError`).
  - Prefix test records with `_Test`.
- **Coverage:** Coverage is captured on non-PR runs and uploaded to Codecov. Codecov has a **patch target of 85%** on PRs to `develop` and a project threshold of 0.5% (`require_ci_to_pass`).
- There are no JS or portal unit tests.
