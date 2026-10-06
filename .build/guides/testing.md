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
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

**Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), running against a real MariaDB site.

**Where tests go:**
- Put the test next to the code it covers: `healthcare/healthcare/doctype/<name>/test_<name>.py`. About 82 test classes exist.
- Shared fixtures live in `healthcare/tests/utils.py`:
  - `HealthcareTestSuite` extends `erpnext.tests.utils.ERPNextTestSuite`.
  - `BootStrapTestData` creates master data: company, items, patients, practitioners, service units, templates, and insurance payors with `_Test ...` names.
- Recent work migrated all fork tests to `HealthcareTestSuite`. New tests should subclass it and call `super().setUp()`.

**Style:**
- Use module-level factory helpers, e.g. `create_appointment(...)` and `create_encounter(...)`.
- Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Assert with `self.assertEqual` against `frappe.db.get_value`.
- Test record names are prefixed `_Test`.

**Coverage expectations:**
- Codecov is configured: project threshold 0.5% and **patch target 85%** on PRs to `develop`.
- Coverage is collected only on scheduled (non-PR) CI runs.
- The labeler adds a **`needs-tests`** label when a PR touches `healthcare/**/*.py` without touching any `test*.py`.
