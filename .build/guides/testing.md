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
  - healthcare/healthcare/report/diagnosis_trends/test_diagnosis_trends.py
---

- **Framework:** the Frappe test runner (unittest-based). Run tests with `bench --site <site> run-tests --app healthcare` (or `--module ...`).
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It extends ERPNext's `ERPNextTestSuite`. Call `super().setUp()`.
- **Fixtures:** `BootStrapTestData` in `healthcare/tests/utils.py` builds shared master data: company, items, patients, practitioners, service units, templates and insurance payors. Records use the `_Test ` prefix (`_Test Company`, `_Test Medical Department`). Add new shared master data there with `make_records`.
- **Layout:** put tests next to the code as `test_<module>.py` inside the doctype or report folder (for example `healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py`). Shared helpers live in `healthcare/tests/`. The repo has about 85 test files.
- **Style:** test methods are named `test_<behaviour>`. Tests set up state through module-level helpers (`create_appointment`, `create_encounter`) and toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`. They assert on DB state with `frappe.db.get_value`.
- **Coverage:** Codecov requires a **patch coverage target of 85%** on PRs. Project coverage may drop by at most 0.5%.
- **CI caveat:** this fork has no `ci.yml` test workflow. Only linters run in CI, so run the relevant tests locally on a bench. `wiki/upstream-sync-version-16.md` records that no CI test baseline exists.
