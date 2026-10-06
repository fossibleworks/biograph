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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`). It needs a bench site with ERPNext installed and runs on MariaDB in CI.
- **Layout:** tests sit next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 files). Report tests sit next to their reports.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates the shared master data (company, items, practitioners, patients, service units, templates, insurance payors). Call `super().setUp()`.
- **Fixtures:** test records use a `_Test ` name prefix (e.g. `_Test Insurance Payor`). Tests often clean up with `frappe.db.sql("delete from `tabX`")` in `setUp`.
- **Coverage:** Codecov sets a **patch target of 85%** on PRs to `develop`, and the project coverage may drop by at most 0.5%. Coverage is only captured on scheduled and non-PR runs.
- **CI scope:** the server-test workflow skips PRs that only touch `*.js`, `*.css`, `*.md`, `*.html` or `*.csv`. Patient-portal (Vue) code has no JS test suite.
- **Fork note:** the fork (`biograph-fh`) has no CI baseline yet. Local bench runs may also be unavailable, so record in the PR when tests could not run locally.
