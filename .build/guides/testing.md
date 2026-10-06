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
  - healthcare/healthcare/doctype/patient_encounter/test_patient_encounter.py
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

## Framework
The Frappe/ERPNext integration test runner executes tests against a real MariaDB site. CI runs `bench --site test_site run-parallel-tests --app healthcare`.

## Layout
- Tests sit next to the code as `test_<module>.py`, inside each DocType or report folder. Examples:
  - `healthcare/healthcare/doctype/patient_encounter/test_patient_encounter.py`
  - `healthcare/healthcare/report/diagnosis_trends/test_diagnosis_trends.py`
- Shared fixtures live in `healthcare/tests/utils.py`.
- There are about 85 test files.

## Base class
- **All test classes extend `HealthcareTestSuite`**, defined in `healthcare/tests/utils.py`, which itself extends `erpnext.tests.utils.ERPNextTestSuite`. There are 82 such classes; recent work migrated the remaining fork tests to it.
- Always call `super().setUp()`.
- `BootStrapTestData` builds the master data: company, service items, practitioners, patients, templates, insurance payors and so on. Its record names follow the `_Test ...` naming convention.

## Test data
- Create records with `frappe.get_doc({...}).insert()`.
- Set fields like `customer_group` explicitly so tests are deterministic. Recent fixes target flaky patient initialisation.
- Assert validation failures with `self.assertRaises(frappe.ValidationError)`.

## Coverage expectations
- Codecov is configured with a **patch target of 85%** on PRs to develop. The project threshold is auto with 0.5% tolerance.
- Coverage is only captured on non-PR CI runs.
- The PR labeler adds `needs-tests` when `healthcare/**/*.py` changes without any `test*.py` change.

## Fork baseline
The fork has no CI history, so the first CI run on a goal PR becomes the baseline. See `wiki/upstream-sync-version-16.md`.
