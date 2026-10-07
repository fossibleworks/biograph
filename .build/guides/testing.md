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
  - healthcare/healthcare/doctype/clinical_note/test_clinical_note.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

**Framework:** Frappe's test runner (unittest style) on a real MariaDB site. Tests run through `bench run-parallel-tests --app healthcare` and `bench run-tests`.

**Layout:** tests sit next to their controllers, as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 test modules. Shared fixtures are in `healthcare/tests/utils.py`.

**Base class**
- Subclass `HealthcareTestSuite` (from `healthcare.tests.utils`), which extends ERPNext's `ERPNextTestSuite`.
- `BootStrapTestData` creates master data with `_Test`-prefixed names, such as `_Test Company`, `_Test Medical Department` and `_Test Insurance Payor`. Reuse these records instead of creating ad-hoc ones.
- In `setUp`, call `super().setUp()`, then clean the tables your test mutates. For example, `test_patient_appointment.py` deletes from `tabPatient Appointment`.
- Change settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Module-level `create_*` helpers build test documents.
- Assert with `self.assertEqual` and `self.assertTrue`, and re-read state with `frappe.db.get_value`.
- Some scaffolds are stubs (`class TestClinicalNote(HealthcareTestSuite): pass`).

**Coverage expectations**
- `codecov.yml` sets a **patch target of 85%** on PRs and lets project coverage drop by at most 0.5%.
- Coverage is captured on non-PR runs (the nightly schedule) and uploaded to Codecov.
- The PR labeler adds a **`needs-tests`** label when `healthcare/**/*.py` changes without any `test*.py` change.
- The PR template asks that all UI and unit tests pass locally.

**Fork caveat:** the fork's CI tests against Frappe and ERPNext `version-16`. The wiki notes that `biograph-fh` has no CI baseline yet. Compare any CI failure against the commit that introduced it.
