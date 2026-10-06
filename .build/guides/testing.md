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
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner (unittest based), executed with `bench run-tests` / `run-parallel-tests` against a real site and a MariaDB/MySQL database.
- **Layout:** tests sit next to each DocType as `doctype/<name>/test_<name>.py` (about 85 test files), with shared helpers in `healthcare/tests/`.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates the master data (company, items, departments, practitioners, patients, service units, templates, and more). Reuse these factories rather than creating ad-hoc fixtures.
- Test methods are named `test_<behaviour>` and use `setUp` for per-test configuration (e.g. Healthcare Settings).
- **Coverage:** Codecov patch target is **85%** on PRs to `develop`, and project coverage may drop by at most 0.5%. CI collects coverage only on non-PR runs (`WITH_COVERAGE`).
- **CI note:** the `biograph-fh` fork has no CI history yet, so there is no baseline of failures (see the wiki ledger). When you change behaviour, run the affected doctype's tests locally.
