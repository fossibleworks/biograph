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
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based test runner, run on a real MariaDB site (`bench run-tests` / `run-parallel-tests`). There is no pytest, and there are no JS or portal tests.
- **Layout:** every doctype keeps its tests beside the code as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Cross-cutting tests live in `healthcare/tests/`.
- **Base class:** subclass `healthcare.tests.utils.HealthcareTestSuite`, which extends ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates the shared master data: `_Test` company, patients, practitioners, service units, templates, insurance payors and so on. Call `super().setUp()`.
- **Conventions:**
  - Test records use the `_Test ...` naming prefix.
  - Module-level factory helpers (`create_appointment(...)`, `create_encounter(...)`) build fixtures.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Assert validation failures with `self.assertRaises(frappe.ValidationError)` or with the specific error class (e.g. `OverlapError`).
- **Coverage:** Codecov requires **85% patch coverage** on PRs to `develop`; the project threshold is 0.5%. CI collects coverage only on scheduled and non-PR runs.
- **Fork caveat:** the `biograph-fh` fork has no CI baseline yet, because `ci.yml` has never run there. Record known pre-existing failures, as the upstream-sync wiki does.
