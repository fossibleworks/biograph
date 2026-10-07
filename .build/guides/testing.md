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
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework:** Frappe's unittest-based test runner. Test classes subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on `erpnext.tests.utils.ERPNextTestSuite`. That module also contains `BootStrapTestData`, which seeds master data with `_Test` names: company, items, patients, practitioners, service units, templates, insurance payors and more.
- **Layout:** each test sits next to its DocType as `doctype/<dt>/test_<dt>.py` (about 85 test files). Shared helpers are in `healthcare/tests/`. Each module defines factory helpers such as `create_appointment(...)` and `create_encounter(...)`, which other tests import.
- **Style:** use `setUp()` with `super().setUp()`. Clean tables explicitly (`frappe.db.sql("delete from `tabX`")`). Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`. Assert with `self.assertEqual` and check validation with `with self.assertRaises(frappe.ValidationError)`. Re-read state with `frappe.db.get_value` or `doc.reload()`.
- **Running:** `bench --site test_site run-parallel-tests --app healthcare` in CI, against MariaDB 11.8. The server test job is skipped for PRs that only change `.css/.js/.md/.html/.csv`.
- **Coverage:** captured on scheduled and push runs (not on PRs) and uploaded to Codecov. `codecov.yml` requires a **patch coverage target of 85%** on PRs to develop, and project coverage may drop by at most 0.5%.
- The labeler adds a **`needs-tests`** label when `healthcare/**/*.py` changes without any `test*.py` change.
- **Fork caveat:** `biograph-fh` has no CI baseline yet. The first CI run on a goal PR becomes the baseline, and failures are compared against the ledger in `wiki/upstream-sync-version-16.md`.
- There are no JS or Vue unit tests in the repo. The `cypress/` path is excluded in pre-commit, but no Cypress suite exists.
