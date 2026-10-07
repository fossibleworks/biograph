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

# Testing

- Framework: Frappe's unittest-based runner. Tests subclass **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which extends ERPNext's `ERPNextTestSuite`.
- `BootStrapTestData` creates shared master data: company, items, patients, practitioners, service units, templates and insurance payors. Test records use the `_Test ...` naming prefix.
- Layout: tests sit next to the code as `doctype/<name>/test_<name>.py`. There are about 85 test files. Cross-cutting tests go in `healthcare/tests/`.
- Style:
  - In `setUp()`, call `super().setUp()`, then clean tables with `frappe.db.sql("delete from `tab...`")`.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Use module-level `create_*` helper factories.
  - Assert with `assertEqual` / `assertRaises`.
- Running tests: `bench --site test_site run-parallel-tests --app healthcare`. CI does this on PRs that change Python files, plus a nightly schedule.
- Coverage:
  - Collected only on non-PR (scheduled) runs and uploaded to Codecov.
  - `codecov.yml` sets a **patch target of 85%** for pulls against `develop`.
  - The project threshold is auto, with 0.5% tolerance.
- Note: the fork (`biograph-fh`) currently has no CI baseline run. The first goal-PR CI run serves as the baseline (see `wiki/upstream-sync-version-16.md`).
