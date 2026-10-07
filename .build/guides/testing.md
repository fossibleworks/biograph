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
  - healthcare/tests/test_utils.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe/ERPNext test runner, built on unittest. Test classes extend `HealthcareTestSuite` (in `healthcare/tests/utils.py`), which subclasses ERPNext's `ERPNextTestSuite`.
- **Fixtures:** `BootStrapTestData` creates shared master data (company, service items, patients, practitioners, service units, templates, insurance payors) via `make_records`. `_Test …` naming is used for fixture records (e.g. `_Test Company`, `_Test Insurance Payor`). Reuse these builders rather than creating ad-hoc fixtures.
- **Layout:** each doctype keeps its test next to its code (`doctype/<name>/test_<name>.py`). There are about 85 test files. Cross-cutting tests live in `healthcare/tests/` (e.g. `test_utils.py`).
- **Running:** `bench --site test_site run-parallel-tests --app healthcare` in CI. This needs a bench site with ERPNext and a MariaDB instance.
- **Coverage:** captured on non-PR (scheduled) runs and uploaded to Codecov. `codecov.yml` sets the patch target at **85%** on PRs to develop and allows the project to drop at most 0.5%.
- **Baseline caveat:** the fork has no CI baseline for `biograph-fh` (see `wiki/upstream-sync-version-16.md`), so compare test failures against a locally recorded baseline.
