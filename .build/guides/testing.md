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
  - .github/workflows/ci.yml
  - codecov.yml
---

**Framework:** Frappe's unittest-based test runner (`bench run-tests` / `run-parallel-tests`), run against a real MariaDB site with ERPNext installed. There are no JS unit tests (no `*.test.js`), and Cypress paths appear only in exclude lists.

**Layout**
- Tests sit next to their DocType: `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 test files, and reports follow the same pattern.
- Test classes are named `Test<DocType>` and subclass **`HealthcareTestSuite`** from `healthcare.tests.utils`. That class builds on ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` creates master data (company, items, patients, practitioners, service units, templates, ...).
- Shared helpers live in `healthcare/tests/utils.py` and `healthcare/tests/test_utils.py`. Doctype tests often expose `create_<thing>()` factory functions that other tests import, for example `create_appointment` in `test_patient_appointment.py`.
- `setUp` calls `super().setUp()`, then clears relevant tables with `frappe.db.sql("delete from \`tab...\`")` and toggles settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.

**CI and coverage**
- `ci.yml` runs the server tests on PRs that touch non-JS/CSS/MD/HTML files, and nightly. Coverage is captured only on non-PR runs and uploaded to Codecov.
- `codecov.yml`: project status threshold is 0.5%, and **patch coverage target is 85%** on PRs.
- This fork has **no CI baseline history**. The first CI run on a goal PR becomes the baseline (`wiki/upstream-sync-version-16.md`).
